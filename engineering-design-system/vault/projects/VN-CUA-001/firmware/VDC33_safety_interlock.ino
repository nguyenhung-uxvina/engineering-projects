/*
 * ═══════════════════════════════════════════════════════════════════════════
 * VDC-33 SAFETY INTERLOCK FIRMWARE
 * Vietnamese Drone Catcher - 1:3 Scale Prototype
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * Project:     VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
 * Prototype:   VDC-33 (1:3 Scale Pneumatic Demonstrator)
 * Version:     1.0.0
 * Date:        2026-02-05
 * Author:      VN-CUA-001 Engineering Team
 *
 * Description:
 *   3-level safety interlock system for pneumatic net launcher prototype.
 *   Implements ARM switch, SAFETY switch, and TRIGGER with fail-safe design.
 *   All failures result in SAFE state (cannot fire).
 *
 * Hardware:
 *   - Arduino Nano (ATmega328P)
 *   - 3S LiPo battery (11.1V nominal)
 *   - Solenoid valve (12V, normally closed)
 *   - MOSFET driver module (IRF520 or similar)
 *   - Switches: ARM (toggle), SAFETY (slide), TRIGGER (microswitch)
 *   - LEDs: Status (bi-color R/G), Ready (green)
 *   - Buzzer: Piezo 5V active
 *   - Voltage divider for battery monitoring
 *
 * Safety Philosophy:
 *   - Fire ONLY when: ARM=ON, SAFETY=OFF, TRIGGER=PRESSED, BATTERY=OK
 *   - Any other state = SAFE (cannot fire)
 *   - Power loss = valve spring-closes = SAFE
 *   - Low battery = cutoff = SAFE
 *
 * ═══════════════════════════════════════════════════════════════════════════
 */

#include <EEPROM.h>

// ═══════════════════════════════════════════════════════════════════════════
// VERSION & BUILD INFO
// ═══════════════════════════════════════════════════════════════════════════

#define FIRMWARE_VERSION    "1.0.0"
#define BUILD_DATE          "2026-02-05"
#define HARDWARE_REV        "VDC-33-A"

// ═══════════════════════════════════════════════════════════════════════════
// PIN DEFINITIONS
// ═══════════════════════════════════════════════════════════════════════════

// Inputs
#define PIN_ARM_SWITCH      2     // ARM switch (HIGH = armed)
#define PIN_SAFETY_SWITCH   3     // SAFETY switch (LOW = safe, HIGH = fire enabled)
#define PIN_TRIGGER         4     // TRIGGER microswitch (HIGH = pressed)
#define PIN_BATTERY_SENSE   A0    // Battery voltage divider (3S LiPo)

// Outputs
#define PIN_VALVE           7     // MOSFET gate for solenoid valve
#define PIN_LED_RED         5     // Status LED red (PWM capable)
#define PIN_LED_GREEN       6     // Status LED green (PWM capable)
#define PIN_LED_READY       8     // Ready indicator LED
#define PIN_BUZZER          9     // Piezo buzzer (PWM capable)

// ═══════════════════════════════════════════════════════════════════════════
// CONFIGURATION CONSTANTS
// ═══════════════════════════════════════════════════════════════════════════

// Timing (milliseconds)
#define DEFAULT_DWELL_MS        12      // Default valve open time
#define MIN_DWELL_MS            5       // Minimum dwell time
#define MAX_DWELL_MS            50      // Maximum dwell time
#define DEBOUNCE_MS             50      // Switch debounce time
#define TRIGGER_LOCKOUT_MS      500     // Prevent rapid fire
#define STARTUP_DELAY_MS        1000    // Power-on delay for stability

// Battery thresholds (3S LiPo: 12.6V full, 9.0V empty)
// Voltage divider: 10k/10k = 0.5 ratio
// ADC: 5V reference, 1024 steps
// Voltage = ADC * 5.0 / 1024 * 2 (divider ratio)
#define BATTERY_FULL_MV         12600   // 12.6V = fully charged
#define BATTERY_NOMINAL_MV      11100   // 11.1V = nominal
#define BATTERY_WARNING_MV      10500   // 10.5V = low warning
#define BATTERY_CUTOFF_MV       10000   // 10.0V = cutoff (no fire)
#define BATTERY_CRITICAL_MV     9500    // 9.5V = critical (shutdown warning)

// ADC calibration (adjust based on actual voltage divider)
#define VREF_MV                 5000    // Arduino 5V reference
#define ADC_RESOLUTION          1024
#define VOLTAGE_DIVIDER_RATIO   2.0     // 10k/10k divider

// EEPROM addresses
#define EEPROM_DWELL_ADDR       0       // Dwell time storage
#define EEPROM_SHOT_COUNT_ADDR  4       // Shot counter (4 bytes)
#define EEPROM_MAGIC_ADDR       8       // Magic number for validation
#define EEPROM_MAGIC_VALUE      0xDC33  // "DC33" identifier

// ═══════════════════════════════════════════════════════════════════════════
// STATE DEFINITIONS
// ═══════════════════════════════════════════════════════════════════════════

enum SystemState {
  STATE_STARTUP,        // Initial power-on
  STATE_SAFE,           // Safety engaged or ARM off
  STATE_ARMED,          // Ready to fire (ARM on, SAFETY off)
  STATE_FIRING,         // Valve open, firing
  STATE_LOCKOUT,        // Post-fire lockout
  STATE_LOW_BATTERY,    // Battery warning
  STATE_FAULT           // System fault detected
};

enum BatteryState {
  BATT_FULL,
  BATT_NOMINAL,
  BATT_WARNING,
  BATT_CUTOFF,
  BATT_CRITICAL
};

// ═══════════════════════════════════════════════════════════════════════════
// GLOBAL VARIABLES
// ═══════════════════════════════════════════════════════════════════════════

// System state
volatile SystemState currentState = STATE_STARTUP;
volatile BatteryState batteryState = BATT_NOMINAL;

// Configuration
uint16_t dwellTimeMs = DEFAULT_DWELL_MS;
uint32_t shotCount = 0;

// Input states (debounced)
bool armSwitchState = false;
bool safetySwitchState = true;   // true = SAFE
bool triggerState = false;

// Timing
unsigned long lastDebounceTime = 0;
unsigned long lastFireTime = 0;
unsigned long lastBatteryCheck = 0;
unsigned long stateEntryTime = 0;

// Battery
uint16_t batteryVoltageMv = 0;
uint16_t batteryReadings[8];     // Rolling average
uint8_t batteryReadIndex = 0;

// Debug
bool debugMode = false;

// ═══════════════════════════════════════════════════════════════════════════
// FUNCTION PROTOTYPES
// ═══════════════════════════════════════════════════════════════════════════

void setup();
void loop();

// State machine
void updateStateMachine();
void enterState(SystemState newState);
void handleStateStartup();
void handleStateSafe();
void handleStateArmed();
void handleStateFiring();
void handleStateLockout();
void handleStateLowBattery();
void handleStateFault();

// Input handling
void readInputs();
bool readDebouncedSwitch(uint8_t pin, bool* lastState, bool activeLow);
void readBattery();
BatteryState classifyBatteryVoltage(uint16_t voltageMv);

// Output control
void setValve(bool open);
void setStatusLED(uint8_t red, uint8_t green);
void setReadyLED(bool on);
void beep(uint16_t freqHz, uint16_t durationMs);
void beepPattern(uint8_t pattern);

// Safety checks
bool canFire();
bool isSafeToArm();

// EEPROM
void loadSettings();
void saveSettings();
void saveShotCount();

// Serial interface
void handleSerial();
void printStatus();
void printHelp();

// ═══════════════════════════════════════════════════════════════════════════
// SETUP
// ═══════════════════════════════════════════════════════════════════════════

void setup() {
  // Initialize serial first for debug output
  Serial.begin(115200);
  while (!Serial && millis() < 3000); // Wait up to 3s for serial

  Serial.println(F("\n═══════════════════════════════════════════════════════"));
  Serial.println(F("  VDC-33 SAFETY INTERLOCK SYSTEM"));
  Serial.print(F("  Firmware: ")); Serial.println(FIRMWARE_VERSION);
  Serial.print(F("  Build: ")); Serial.println(BUILD_DATE);
  Serial.print(F("  Hardware: ")); Serial.println(HARDWARE_REV);
  Serial.println(F("═══════════════════════════════════════════════════════\n"));

  // Configure pins
  // Inputs with pull-ups/pull-downs as appropriate
  pinMode(PIN_ARM_SWITCH, INPUT);       // External pull-down expected
  pinMode(PIN_SAFETY_SWITCH, INPUT_PULLUP);  // Active LOW = safe
  pinMode(PIN_TRIGGER, INPUT);          // External pull-down expected
  pinMode(PIN_BATTERY_SENSE, INPUT);

  // Outputs - ensure safe state immediately
  pinMode(PIN_VALVE, OUTPUT);
  digitalWrite(PIN_VALVE, LOW);         // VALVE CLOSED (critical!)

  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_READY, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);

  // Initial LED state: all off during startup
  setStatusLED(0, 0);
  setReadyLED(false);

  // Load settings from EEPROM
  loadSettings();

  // Initialize battery readings array
  for (int i = 0; i < 8; i++) {
    batteryReadings[i] = 0;
  }

  // Initial battery read
  for (int i = 0; i < 8; i++) {
    readBattery();
    delay(10);
  }

  // Startup beep
  beep(1000, 100);
  delay(100);
  beep(1500, 100);
  delay(100);
  beep(2000, 200);

  // Enter startup state
  enterState(STATE_STARTUP);

  Serial.println(F("System initialized. Type 'help' for commands.\n"));
  printStatus();
}

// ═══════════════════════════════════════════════════════════════════════════
// MAIN LOOP
// ═══════════════════════════════════════════════════════════════════════════

void loop() {
  // Read all inputs
  readInputs();

  // Check battery periodically
  if (millis() - lastBatteryCheck > 500) {
    readBattery();
    lastBatteryCheck = millis();
  }

  // Update state machine
  updateStateMachine();

  // Handle serial commands
  handleSerial();

  // Small delay to prevent tight loop
  delay(1);
}

// ═══════════════════════════════════════════════════════════════════════════
// STATE MACHINE
// ═══════════════════════════════════════════════════════════════════════════

void updateStateMachine() {
  switch (currentState) {
    case STATE_STARTUP:
      handleStateStartup();
      break;
    case STATE_SAFE:
      handleStateSafe();
      break;
    case STATE_ARMED:
      handleStateArmed();
      break;
    case STATE_FIRING:
      handleStateFiring();
      break;
    case STATE_LOCKOUT:
      handleStateLockout();
      break;
    case STATE_LOW_BATTERY:
      handleStateLowBattery();
      break;
    case STATE_FAULT:
      handleStateFault();
      break;
  }
}

void enterState(SystemState newState) {
  if (newState == currentState) return;

  SystemState oldState = currentState;
  currentState = newState;
  stateEntryTime = millis();

  // Debug output
  if (debugMode) {
    Serial.print(F("[STATE] "));
    Serial.print(oldState);
    Serial.print(F(" -> "));
    Serial.println(newState);
  }

  // State entry actions
  switch (newState) {
    case STATE_STARTUP:
      setStatusLED(128, 128);   // Yellow during startup
      setReadyLED(false);
      break;

    case STATE_SAFE:
      setValve(false);          // Ensure valve closed
      setStatusLED(0, 255);     // Green = safe
      setReadyLED(false);
      if (oldState == STATE_ARMED) {
        beep(500, 100);         // Disarm beep
      }
      break;

    case STATE_ARMED:
      setStatusLED(255, 0);     // Red = armed
      setReadyLED(true);
      beep(1000, 50);           // Arm beep
      delay(50);
      beep(1000, 50);
      Serial.println(F("*** SYSTEM ARMED ***"));
      break;

    case STATE_FIRING:
      // Firing handled in state handler
      break;

    case STATE_LOCKOUT:
      setStatusLED(255, 0);     // Stay red
      setReadyLED(false);       // Not ready
      break;

    case STATE_LOW_BATTERY:
      setValve(false);
      setStatusLED(255, 128);   // Orange
      setReadyLED(false);
      beepPattern(3);           // Warning pattern
      Serial.println(F("!!! LOW BATTERY - FIRING DISABLED !!!"));
      break;

    case STATE_FAULT:
      setValve(false);
      setStatusLED(255, 0);     // Red
      setReadyLED(false);
      beepPattern(5);           // Fault pattern
      Serial.println(F("!!! SYSTEM FAULT !!!"));
      break;
  }
}

void handleStateStartup() {
  // Wait for startup delay
  if (millis() - stateEntryTime < STARTUP_DELAY_MS) {
    // Blink yellow during startup
    uint8_t brightness = (millis() / 100) % 2 ? 255 : 64;
    setStatusLED(brightness, brightness);
    return;
  }

  // Check battery
  if (batteryState == BATT_CUTOFF || batteryState == BATT_CRITICAL) {
    enterState(STATE_LOW_BATTERY);
    return;
  }

  // Transition to safe state
  enterState(STATE_SAFE);
}

void handleStateSafe() {
  // Check for low battery
  if (batteryState == BATT_CUTOFF || batteryState == BATT_CRITICAL) {
    enterState(STATE_LOW_BATTERY);
    return;
  }

  // Battery warning (blink green)
  if (batteryState == BATT_WARNING) {
    uint8_t blink = (millis() / 500) % 2 ? 255 : 64;
    setStatusLED(0, blink);
  } else {
    setStatusLED(0, 255);     // Solid green
  }

  // Check for arm condition
  if (armSwitchState && !safetySwitchState) {
    // ARM is ON and SAFETY is OFF (fire position)
    enterState(STATE_ARMED);
  }
}

void handleStateArmed() {
  // Immediate safety checks - return to safe if conditions lost
  if (!armSwitchState || safetySwitchState) {
    enterState(STATE_SAFE);
    return;
  }

  // Check for low battery
  if (batteryState == BATT_CUTOFF || batteryState == BATT_CRITICAL) {
    enterState(STATE_LOW_BATTERY);
    return;
  }

  // Battery warning (blink red)
  if (batteryState == BATT_WARNING) {
    uint8_t blink = (millis() / 250) % 2 ? 255 : 64;
    setStatusLED(blink, 0);
  } else {
    setStatusLED(255, 0);     // Solid red
  }

  // Check for fire command
  if (triggerState && canFire()) {
    enterState(STATE_FIRING);
  }
}

void handleStateFiring() {
  static bool valveOpened = false;

  // Safety check - abort if conditions lost
  if (!armSwitchState || safetySwitchState) {
    setValve(false);
    valveOpened = false;
    enterState(STATE_SAFE);
    return;
  }

  // Open valve if not already
  if (!valveOpened) {
    setValve(true);
    valveOpened = true;
    setStatusLED(255, 0);     // Bright red during fire

    if (debugMode) {
      Serial.print(F("[FIRE] Dwell: "));
      Serial.print(dwellTimeMs);
      Serial.println(F("ms"));
    }
  }

  // Wait for dwell time
  if (millis() - stateEntryTime >= dwellTimeMs) {
    setValve(false);
    valveOpened = false;

    // Increment shot counter
    shotCount++;
    saveShotCount();

    Serial.print(F("FIRED! Shot #"));
    Serial.println(shotCount);

    lastFireTime = millis();
    enterState(STATE_LOCKOUT);
  }
}

void handleStateLockout() {
  // Safety check
  if (!armSwitchState || safetySwitchState) {
    enterState(STATE_SAFE);
    return;
  }

  // Wait for trigger release
  if (!triggerState) {
    // Wait for lockout period
    if (millis() - lastFireTime >= TRIGGER_LOCKOUT_MS) {
      enterState(STATE_ARMED);
    }
  }

  // Blink ready LED during lockout
  setReadyLED((millis() / 100) % 2);
}

void handleStateLowBattery() {
  // Blink orange warning
  uint8_t blink = (millis() / 250) % 2 ? 255 : 0;
  setStatusLED(blink, blink / 2);

  // Check if battery recovered
  if (batteryState == BATT_NOMINAL || batteryState == BATT_FULL) {
    enterState(STATE_SAFE);
    return;
  }

  // Periodic warning beep
  if ((millis() / 5000) % 2 == 0 && (millis() % 5000) < 100) {
    beep(500, 100);
  }
}

void handleStateFault() {
  // Blink red rapidly
  uint8_t blink = (millis() / 100) % 2 ? 255 : 0;
  setStatusLED(blink, 0);

  // Ensure valve closed
  setValve(false);

  // Can only exit fault by power cycle
  // (intentionally no exit condition)
}

// ═══════════════════════════════════════════════════════════════════════════
// INPUT HANDLING
// ═══════════════════════════════════════════════════════════════════════════

void readInputs() {
  static bool lastArmState = false;
  static bool lastSafetyState = true;
  static bool lastTriggerState = false;
  static unsigned long lastArmChange = 0;
  static unsigned long lastSafetyChange = 0;
  static unsigned long lastTriggerChange = 0;

  // Read ARM switch (active HIGH)
  bool rawArm = digitalRead(PIN_ARM_SWITCH);
  if (rawArm != lastArmState) {
    lastArmChange = millis();
    lastArmState = rawArm;
  }
  if (millis() - lastArmChange > DEBOUNCE_MS) {
    armSwitchState = rawArm;
  }

  // Read SAFETY switch (active LOW = safe)
  bool rawSafety = !digitalRead(PIN_SAFETY_SWITCH);  // Invert: LOW = safe = true
  if (rawSafety != lastSafetyState) {
    lastSafetyChange = millis();
    lastSafetyState = rawSafety;
  }
  if (millis() - lastSafetyChange > DEBOUNCE_MS) {
    safetySwitchState = rawSafety;
  }

  // Read TRIGGER (active HIGH)
  bool rawTrigger = digitalRead(PIN_TRIGGER);
  if (rawTrigger != lastTriggerState) {
    lastTriggerChange = millis();
    lastTriggerState = rawTrigger;
  }
  if (millis() - lastTriggerChange > DEBOUNCE_MS) {
    triggerState = rawTrigger;
  }
}

void readBattery() {
  // Read ADC
  uint16_t adcValue = analogRead(PIN_BATTERY_SENSE);

  // Convert to millivolts
  // voltage = adc * Vref / resolution * divider_ratio
  uint32_t voltageMv = ((uint32_t)adcValue * VREF_MV * VOLTAGE_DIVIDER_RATIO) / ADC_RESOLUTION;

  // Rolling average
  batteryReadings[batteryReadIndex] = voltageMv;
  batteryReadIndex = (batteryReadIndex + 1) % 8;

  uint32_t sum = 0;
  for (int i = 0; i < 8; i++) {
    sum += batteryReadings[i];
  }
  batteryVoltageMv = sum / 8;

  // Classify battery state
  batteryState = classifyBatteryVoltage(batteryVoltageMv);
}

BatteryState classifyBatteryVoltage(uint16_t voltageMv) {
  if (voltageMv >= BATTERY_FULL_MV - 200) {
    return BATT_FULL;
  } else if (voltageMv >= BATTERY_WARNING_MV) {
    return BATT_NOMINAL;
  } else if (voltageMv >= BATTERY_CUTOFF_MV) {
    return BATT_WARNING;
  } else if (voltageMv >= BATTERY_CRITICAL_MV) {
    return BATT_CUTOFF;
  } else {
    return BATT_CRITICAL;
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// OUTPUT CONTROL
// ═══════════════════════════════════════════════════════════════════════════

void setValve(bool open) {
  // CRITICAL SAFETY: Only open valve if all conditions met
  if (open && !canFire()) {
    open = false;
    Serial.println(F("!!! VALVE OPEN BLOCKED BY SAFETY !!!"));
  }

  digitalWrite(PIN_VALVE, open ? HIGH : LOW);

  if (debugMode && open) {
    Serial.println(F("[VALVE] OPEN"));
  }
}

void setStatusLED(uint8_t red, uint8_t green) {
  analogWrite(PIN_LED_RED, red);
  analogWrite(PIN_LED_GREEN, green);
}

void setReadyLED(bool on) {
  digitalWrite(PIN_LED_READY, on ? HIGH : LOW);
}

void beep(uint16_t freqHz, uint16_t durationMs) {
  tone(PIN_BUZZER, freqHz, durationMs);
}

void beepPattern(uint8_t count) {
  for (uint8_t i = 0; i < count; i++) {
    beep(1000, 100);
    delay(150);
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// SAFETY CHECKS
// ═══════════════════════════════════════════════════════════════════════════

bool canFire() {
  // ALL conditions must be true to fire
  bool armOk = armSwitchState;
  bool safetyOff = !safetySwitchState;
  bool triggerPressed = triggerState;
  bool batteryOk = (batteryState != BATT_CUTOFF && batteryState != BATT_CRITICAL);
  bool stateOk = (currentState == STATE_ARMED || currentState == STATE_FIRING);
  bool notLocked = (millis() - lastFireTime >= TRIGGER_LOCKOUT_MS || lastFireTime == 0);

  bool canFire = armOk && safetyOff && triggerPressed && batteryOk && stateOk && notLocked;

  if (debugMode && triggerPressed && !canFire) {
    Serial.print(F("[SAFETY] Fire blocked: "));
    if (!armOk) Serial.print(F("ARM "));
    if (!safetyOff) Serial.print(F("SAFETY "));
    if (!batteryOk) Serial.print(F("BATTERY "));
    if (!stateOk) Serial.print(F("STATE "));
    if (!notLocked) Serial.print(F("LOCKOUT "));
    Serial.println();
  }

  return canFire;
}

bool isSafeToArm() {
  return (batteryState != BATT_CUTOFF && batteryState != BATT_CRITICAL);
}

// ═══════════════════════════════════════════════════════════════════════════
// EEPROM FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

void loadSettings() {
  // Check magic number
  uint16_t magic;
  EEPROM.get(EEPROM_MAGIC_ADDR, magic);

  if (magic != EEPROM_MAGIC_VALUE) {
    // First run or corrupted - initialize defaults
    Serial.println(F("Initializing EEPROM with defaults..."));
    dwellTimeMs = DEFAULT_DWELL_MS;
    shotCount = 0;
    saveSettings();
    return;
  }

  // Load dwell time
  EEPROM.get(EEPROM_DWELL_ADDR, dwellTimeMs);
  if (dwellTimeMs < MIN_DWELL_MS || dwellTimeMs > MAX_DWELL_MS) {
    dwellTimeMs = DEFAULT_DWELL_MS;
  }

  // Load shot count
  EEPROM.get(EEPROM_SHOT_COUNT_ADDR, shotCount);

  Serial.print(F("Loaded settings: Dwell="));
  Serial.print(dwellTimeMs);
  Serial.print(F("ms, Shots="));
  Serial.println(shotCount);
}

void saveSettings() {
  EEPROM.put(EEPROM_MAGIC_ADDR, (uint16_t)EEPROM_MAGIC_VALUE);
  EEPROM.put(EEPROM_DWELL_ADDR, dwellTimeMs);
  EEPROM.put(EEPROM_SHOT_COUNT_ADDR, shotCount);
}

void saveShotCount() {
  EEPROM.put(EEPROM_SHOT_COUNT_ADDR, shotCount);
}

// ═══════════════════════════════════════════════════════════════════════════
// SERIAL INTERFACE
// ═══════════════════════════════════════════════════════════════════════════

void handleSerial() {
  if (!Serial.available()) return;

  String cmd = Serial.readStringUntil('\n');
  cmd.trim();
  cmd.toLowerCase();

  if (cmd == "help" || cmd == "?") {
    printHelp();
  }
  else if (cmd == "status" || cmd == "s") {
    printStatus();
  }
  else if (cmd == "debug on") {
    debugMode = true;
    Serial.println(F("Debug mode ON"));
  }
  else if (cmd == "debug off") {
    debugMode = false;
    Serial.println(F("Debug mode OFF"));
  }
  else if (cmd.startsWith("dwell ")) {
    int newDwell = cmd.substring(6).toInt();
    if (newDwell >= MIN_DWELL_MS && newDwell <= MAX_DWELL_MS) {
      dwellTimeMs = newDwell;
      saveSettings();
      Serial.print(F("Dwell time set to "));
      Serial.print(dwellTimeMs);
      Serial.println(F("ms"));
    } else {
      Serial.print(F("Invalid dwell. Range: "));
      Serial.print(MIN_DWELL_MS);
      Serial.print(F("-"));
      Serial.print(MAX_DWELL_MS);
      Serial.println(F("ms"));
    }
  }
  else if (cmd == "reset shots") {
    shotCount = 0;
    saveShotCount();
    Serial.println(F("Shot counter reset"));
  }
  else if (cmd == "test led") {
    Serial.println(F("LED test: Red..."));
    setStatusLED(255, 0);
    delay(500);
    Serial.println(F("LED test: Green..."));
    setStatusLED(0, 255);
    delay(500);
    Serial.println(F("LED test: Yellow..."));
    setStatusLED(255, 255);
    delay(500);
    Serial.println(F("LED test: Ready..."));
    setReadyLED(true);
    delay(500);
    setReadyLED(false);
    setStatusLED(0, 255);
    Serial.println(F("LED test complete"));
  }
  else if (cmd == "test buzzer") {
    Serial.println(F("Buzzer test..."));
    beep(500, 200);
    delay(300);
    beep(1000, 200);
    delay(300);
    beep(2000, 200);
    Serial.println(F("Buzzer test complete"));
  }
  else if (cmd == "test valve") {
    if (currentState == STATE_SAFE && !armSwitchState) {
      Serial.println(F("Valve test (50ms pulse)..."));
      digitalWrite(PIN_VALVE, HIGH);
      delay(50);
      digitalWrite(PIN_VALVE, LOW);
      Serial.println(F("Valve test complete"));
    } else {
      Serial.println(F("Valve test blocked - must be SAFE with ARM off"));
    }
  }
  else if (cmd.length() > 0) {
    Serial.print(F("Unknown command: "));
    Serial.println(cmd);
    Serial.println(F("Type 'help' for commands"));
  }
}

void printStatus() {
  Serial.println(F("\n─────────────────────────────────────────────────────────"));
  Serial.println(F("                    VDC-33 STATUS"));
  Serial.println(F("─────────────────────────────────────────────────────────"));

  // State
  Serial.print(F("State:        "));
  switch (currentState) {
    case STATE_STARTUP:     Serial.println(F("STARTUP")); break;
    case STATE_SAFE:        Serial.println(F("SAFE")); break;
    case STATE_ARMED:       Serial.println(F("*** ARMED ***")); break;
    case STATE_FIRING:      Serial.println(F("!!! FIRING !!!")); break;
    case STATE_LOCKOUT:     Serial.println(F("LOCKOUT")); break;
    case STATE_LOW_BATTERY: Serial.println(F("LOW BATTERY")); break;
    case STATE_FAULT:       Serial.println(F("FAULT")); break;
  }

  // Inputs
  Serial.println(F("\nInputs:"));
  Serial.print(F("  ARM Switch:     "));
  Serial.println(armSwitchState ? F("ON") : F("OFF"));
  Serial.print(F("  SAFETY Switch:  "));
  Serial.println(safetySwitchState ? F("SAFE") : F("FIRE"));
  Serial.print(F("  TRIGGER:        "));
  Serial.println(triggerState ? F("PRESSED") : F("Released"));

  // Battery
  Serial.println(F("\nBattery:"));
  Serial.print(F("  Voltage:        "));
  Serial.print(batteryVoltageMv / 1000.0, 2);
  Serial.print(F("V ("));
  switch (batteryState) {
    case BATT_FULL:     Serial.print(F("FULL")); break;
    case BATT_NOMINAL:  Serial.print(F("OK")); break;
    case BATT_WARNING:  Serial.print(F("LOW")); break;
    case BATT_CUTOFF:   Serial.print(F("CUTOFF")); break;
    case BATT_CRITICAL: Serial.print(F("CRITICAL")); break;
  }
  Serial.println(F(")"));

  // Settings
  Serial.println(F("\nSettings:"));
  Serial.print(F("  Dwell time:     "));
  Serial.print(dwellTimeMs);
  Serial.println(F("ms"));
  Serial.print(F("  Shot count:     "));
  Serial.println(shotCount);
  Serial.print(F("  Debug mode:     "));
  Serial.println(debugMode ? F("ON") : F("OFF"));

  // Fire check
  Serial.println(F("\nFire Check:"));
  Serial.print(F("  Can fire:       "));
  Serial.println(canFire() ? F("YES") : F("NO"));

  Serial.println(F("─────────────────────────────────────────────────────────\n"));
}

void printHelp() {
  Serial.println(F("\n═══════════════════════════════════════════════════════"));
  Serial.println(F("                VDC-33 SERIAL COMMANDS"));
  Serial.println(F("═══════════════════════════════════════════════════════"));
  Serial.println(F("  status, s       - Show system status"));
  Serial.println(F("  dwell <ms>      - Set dwell time (5-50ms)"));
  Serial.println(F("  debug on/off    - Toggle debug output"));
  Serial.println(F("  reset shots     - Reset shot counter"));
  Serial.println(F("  test led        - Test LED indicators"));
  Serial.println(F("  test buzzer     - Test buzzer"));
  Serial.println(F("  test valve      - Test valve (SAFE mode only)"));
  Serial.println(F("  help, ?         - Show this help"));
  Serial.println(F("═══════════════════════════════════════════════════════\n"));
}

// ═══════════════════════════════════════════════════════════════════════════
// END OF FIRMWARE
// ═══════════════════════════════════════════════════════════════════════════
