# VDC-33 Wiring Guide
## Arduino Safety Interlock System

**Version:** 1.0
**Date:** 2026-02-05

---

## 1. COMPONENT LIST

| Item | Specification | Qty | Notes |
|------|---------------|-----|-------|
| Arduino Nano | ATmega328P, USB-C | 1 | Main controller |
| MOSFET Module | IRF520 or IRLZ44N | 1 | Solenoid driver |
| Bi-color LED | Common cathode, 5mm | 1 | Status (R/G) |
| Green LED | 5mm | 1 | Ready indicator |
| Piezo Buzzer | 5V active | 1 | Audio feedback |
| Toggle Switch | SPST, panel mount | 1 | ARM switch |
| Slide Switch | SPST, panel mount | 1 | SAFETY switch |
| Microswitch | SPST-NO, lever | 1 | TRIGGER |
| Resistors | 10kΩ, 1/4W | 4 | Pull-down, voltage divider |
| Resistors | 330Ω, 1/4W | 3 | LED current limiting |
| 18650 Holder | 3S with leads | 1 | Battery pack |
| 18650 Cells | 3.7V 2600mAh | 3 | Li-ion cells |
| BMS Module | 3S 10A | 1 | Battery protection |

---

## 2. WIRING DIAGRAM

```
VDC-33 WIRING SCHEMATIC
═══════════════════════════════════════════════════════════════════════════

                           3S BATTERY PACK
                        ┌─────────────────────┐
                        │  [+]  BMS  [-]      │
                        │   │   3S   │        │
                        │   │  10A   │        │
                        └───┼────────┼────────┘
                            │        │
                           12V      GND
                            │        │
        ┌───────────────────┼────────┼───────────────────────────────────┐
        │                   │        │                                   │
        │    ┌──────────────┴────────┴──────────────┐                   │
        │    │         ARDUINO NANO                  │                   │
        │    │                                       │                   │
        │    │  VIN ←───────────────────────────────┼─── 12V            │
        │    │  GND ←───────────────────────────────┼─── GND            │
        │    │                                       │                   │
        │    │  D2  ←── ARM SWITCH ──────┬──[10kΩ]──┼─── GND            │
        │    │                           └──────────┼─── 5V (when ON)   │
        │    │                                       │                   │
        │    │  D3  ←── SAFETY SWITCH ──────────────┼─── GND (SAFE)     │
        │    │         (internal pull-up)           │    FLOAT (FIRE)   │
        │    │                                       │                   │
        │    │  D4  ←── TRIGGER ─────────┬──[10kΩ]──┼─── GND            │
        │    │                           └──────────┼─── 5V (pressed)   │
        │    │                                       │                   │
        │    │  A0  ←── VOLTAGE DIVIDER ────────────┤                   │
        │    │         (see below)                  │                   │
        │    │                                       │                   │
        │    │  D5  ──→ [330Ω] ──→ RED LED ─────────┼─── GND            │
        │    │  D6  ──→ [330Ω] ──→ GREEN LED ───────┼─── GND            │
        │    │  D8  ──→ [330Ω] ──→ READY LED ───────┼─── GND            │
        │    │                                       │                   │
        │    │  D9  ──→ BUZZER (+) ─────────────────┤                   │
        │    │         BUZZER (-) ──────────────────┼─── GND            │
        │    │                                       │                   │
        │    │  D7  ──→ MOSFET GATE ────────────────┤                   │
        │    │                                       │                   │
        │    └───────────────────────────────────────┘                   │
        │                                                                │
        │    ┌───────────────────────────────────────┐                   │
        │    │         MOSFET MODULE                 │                   │
        │    │                                       │                   │
        │    │  SIG ←── D7 (from Arduino)           │                   │
        │    │  VCC ←── 5V                          │                   │
        │    │  GND ←── GND                         │                   │
        │    │                                       │                   │
        │    │  V+  ←── 12V ────────────────────────┼─── 12V            │
        │    │  V-  ──→ SOLENOID (-) ───────────────┤                   │
        │    │         SOLENOID (+) ────────────────┼─── 12V            │
        │    │                                       │                   │
        │    └───────────────────────────────────────┘                   │
        │                                                                │
        └────────────────────────────────────────────────────────────────┘


VOLTAGE DIVIDER (Battery Monitoring)
═══════════════════════════════════════════════════════════════════════════

        12V (Battery +)
            │
           [10kΩ]
            │
            ├────────────→ A0 (Arduino)
            │
           [10kΩ]
            │
           GND

    Vout = Vin × R2/(R1+R2) = 12V × 10k/(10k+10k) = 6V max

    Note: Arduino A0 max is 5V, so:
    - At 12.6V battery: A0 sees 6.3V (slight overvoltage, add protection)
    - Better: Use 10kΩ/4.7kΩ for max 4.0V at 12.6V input

    RECOMMENDED DIVIDER:
    R1 = 10kΩ (top)
    R2 = 4.7kΩ (bottom)
    Ratio = 4.7/(10+4.7) = 0.32
    At 12.6V: A0 = 4.0V (safe)
    At 10.0V: A0 = 3.2V

═══════════════════════════════════════════════════════════════════════════
```

---

## 3. SWITCH WIRING DETAILS

### ARM Switch (Toggle)
```
ARM SWITCH WIRING
═══════════════════════════════════════════════════════════════════════════

    5V ────────┬──── ARM SWITCH ────┬───── D2 (Arduino)
               │       (SPST)       │
               │                   [10kΩ]
               │                    │
              OFF                  GND
         (disconnected)

    OFF position: D2 pulled LOW by 10kΩ to GND → armSwitchState = false
    ON position:  D2 pulled HIGH by 5V → armSwitchState = true

═══════════════════════════════════════════════════════════════════════════
```

### SAFETY Switch (Slide)
```
SAFETY SWITCH WIRING
═══════════════════════════════════════════════════════════════════════════

    D3 (Arduino, internal pull-up) ────── SAFETY SWITCH ────── GND
                                              (SPST)

    SAFE position (closed):  D3 = LOW (grounded) → safetySwitchState = true
    FIRE position (open):    D3 = HIGH (pull-up) → safetySwitchState = false

    Note: Internal pull-up enabled in firmware (INPUT_PULLUP)

═══════════════════════════════════════════════════════════════════════════
```

### TRIGGER Switch (Microswitch)
```
TRIGGER SWITCH WIRING
═══════════════════════════════════════════════════════════════════════════

    5V ────────┬──── TRIGGER (NO) ────┬───── D4 (Arduino)
               │    (microswitch)     │
               │                     [10kΩ]
               │                      │
           Released                  GND
         (disconnected)

    Released: D4 pulled LOW by 10kΩ → triggerState = false
    Pressed:  D4 pulled HIGH by 5V → triggerState = true

    Microswitch: Use normally-open (NO) contacts
    Recommended: Omron V-10G-1C25-K or similar

═══════════════════════════════════════════════════════════════════════════
```

---

## 4. LED WIRING

```
LED CONNECTIONS
═══════════════════════════════════════════════════════════════════════════

BI-COLOR STATUS LED (Common Cathode)
─────────────────────────────────────────────────────────────────────────────
           ┌──── RED anode ────[330Ω]──── D5 (PWM)
           │
    LED ───┼──── GREEN anode ──[330Ω]──── D6 (PWM)
           │
           └──── CATHODE ─────────────── GND

    Colors:
    • Green (safe):   D5=LOW,  D6=HIGH
    • Red (armed):    D5=HIGH, D6=LOW
    • Yellow (warn):  D5=HIGH, D6=HIGH
    • Off:            D5=LOW,  D6=LOW


READY LED (Single Green)
─────────────────────────────────────────────────────────────────────────────

    D8 ────[330Ω]────┤>├──── GND
                     LED

═══════════════════════════════════════════════════════════════════════════
```

---

## 5. SOLENOID DRIVER

```
MOSFET DRIVER CIRCUIT
═══════════════════════════════════════════════════════════════════════════

    12V (Battery) ──────────────────────┬──────────────────────────────┐
                                        │                              │
                                        │                              │
                                   SOLENOID                       FLYBACK
                                    VALVE                          DIODE
                                   ┌─────┐                        1N4007
                                   │     │                          │
                                   │  +  │←─────────────────────────┤
                                   │     │                          │
                                   │  -  │──────────────────────────┤
                                   └─────┘                          │
                                        │                           │
                                        │                           │
                                   ┌────┴────┐                      │
                                   │  DRAIN  │                      │
                                   │         │                      │
     D7 (Arduino) ────[1kΩ]────────│  GATE   │ MOSFET               │
                                   │         │ (IRF520/IRLZ44N)     │
                                   │ SOURCE  │                      │
                                   └────┬────┘                      │
                                        │                           │
                                       GND ─────────────────────────┘


    IMPORTANT:
    • Flyback diode MUST be installed across solenoid
    • Diode: Cathode to +12V, Anode to MOSFET drain
    • This protects MOSFET from back-EMF when solenoid closes

    If using IRF520 module:
    • Module has built-in flyback diode
    • Connect: SIG←D7, VCC←5V, GND←GND, V+←12V, V-←Solenoid(-)

═══════════════════════════════════════════════════════════════════════════
```

---

## 6. BATTERY SYSTEM

```
3S LiPo BATTERY SYSTEM
═══════════════════════════════════════════════════════════════════════════

    18650 CELLS (3S Configuration)
    ┌─────────┬─────────┬─────────┐
    │  CELL 1 │  CELL 2 │  CELL 3 │
    │  3.7V   │  3.7V   │  3.7V   │
    │ 2600mAh │ 2600mAh │ 2600mAh │
    └────┬────┴────┬────┴────┬────┘
         │         │         │
    ┌────┴─────────┴─────────┴────┐
    │         BMS MODULE          │
    │     3S 12.6V 10A           │
    │                             │
    │  B+ ── Cell 3+              │
    │  B3 ── Cell 3-/Cell 2+      │
    │  B2 ── Cell 2-/Cell 1+      │
    │  B- ── Cell 1-              │
    │                             │
    │  P+ ──→ System 12V          │
    │  P- ──→ System GND          │
    └─────────────────────────────┘

    VOLTAGE RANGES:
    ─────────────────────────────────────────────────────────────────────────
    Full charge:     12.6V (4.2V × 3)
    Nominal:         11.1V (3.7V × 3)
    Low warning:     10.5V (3.5V × 3)
    Cutoff:          10.0V (3.33V × 3)
    BMS cutoff:       9.0V (3.0V × 3) - hardware protection

    CAPACITY:
    ─────────────────────────────────────────────────────────────────────────
    Capacity: 2600mAh @ 11.1V = ~29 Wh

    Power consumption:
    • Standby (safe): ~50mA
    • Armed: ~80mA
    • Firing (50ms): ~2A peak

    Estimated runtime: 20+ hours standby, 500+ shots

═══════════════════════════════════════════════════════════════════════════
```

---

## 7. CONNECTOR PINOUT

```
RECOMMENDED CONNECTORS
═══════════════════════════════════════════════════════════════════════════

MAIN POWER (XT30 or similar)
─────────────────────────────────────────────────────────────────────────────
    Pin 1: +12V (red)
    Pin 2: GND (black)


SWITCH HARNESS (JST-XH 6-pin)
─────────────────────────────────────────────────────────────────────────────
    Pin 1: ARM_SW signal → D2
    Pin 2: ARM_SW +5V
    Pin 3: SAFETY_SW signal → D3
    Pin 4: TRIGGER signal → D4
    Pin 5: TRIGGER +5V
    Pin 6: GND (common)


LED HARNESS (JST-XH 4-pin)
─────────────────────────────────────────────────────────────────────────────
    Pin 1: RED → D5
    Pin 2: GREEN → D6
    Pin 3: READY → D8
    Pin 4: GND (common cathode)


SOLENOID (JST-VH 2-pin or quick-disconnect)
─────────────────────────────────────────────────────────────────────────────
    Pin 1: Solenoid + (to +12V)
    Pin 2: Solenoid - (to MOSFET drain)

═══════════════════════════════════════════════════════════════════════════
```

---

## 8. ASSEMBLY CHECKLIST

```
PRE-ASSEMBLY VERIFICATION
═══════════════════════════════════════════════════════════════════════════

☐ All components tested individually
☐ Arduino programmed and tested via USB
☐ MOSFET module tested with LED load
☐ Battery cells balanced and fully charged
☐ BMS module tested for cutoff function

WIRING ORDER
═══════════════════════════════════════════════════════════════════════════

☐ 1. Solder voltage divider resistors
☐ 2. Solder LED resistors (330Ω × 3)
☐ 3. Solder pull-down resistors (10kΩ × 2)
☐ 4. Connect Arduino GND first
☐ 5. Connect voltage divider to A0
☐ 6. Connect switches to D2, D3, D4
☐ 7. Connect LEDs to D5, D6, D8
☐ 8. Connect buzzer to D9
☐ 9. Connect MOSFET module
☐ 10. Connect solenoid with flyback diode
☐ 11. Connect battery last

POST-ASSEMBLY TESTS
═══════════════════════════════════════════════════════════════════════════

☐ Power on - Green LED lights
☐ Serial monitor shows status
☐ ARM switch changes state
☐ SAFETY switch changes state
☐ TRIGGER detected
☐ Battery voltage reads correctly
☐ "test led" command works
☐ "test buzzer" command works
☐ "test valve" command works (clicks)
☐ Full fire sequence test (with pressure)

═══════════════════════════════════════════════════════════════════════════
```

---

## 9. TROUBLESHOOTING

| Symptom | Possible Cause | Solution |
|---------|----------------|----------|
| No power LED | Battery disconnected | Check connections |
| Status LED always red | ARM stuck or wired wrong | Check ARM switch wiring |
| Won't arm | SAFETY stuck in SAFE | Check SAFETY switch |
| Won't fire | Multiple causes | Check serial status output |
| Valve clicks but weak | Low battery | Charge/replace battery |
| Erratic behavior | Noise on inputs | Add 100nF caps to switches |
| Battery reads wrong | Divider values wrong | Recalculate, measure |

---

## 10. SERIAL COMMANDS REFERENCE

| Command | Description |
|---------|-------------|
| `status` or `s` | Show full system status |
| `dwell <ms>` | Set dwell time (5-50ms) |
| `debug on` | Enable debug messages |
| `debug off` | Disable debug messages |
| `reset shots` | Reset shot counter to 0 |
| `test led` | Cycle through LED colors |
| `test buzzer` | Play buzzer tones |
| `test valve` | Pulse valve 50ms (SAFE only) |
| `help` or `?` | Show command help |

---

*Wiring guide for VDC-33 prototype safety interlock system.*
