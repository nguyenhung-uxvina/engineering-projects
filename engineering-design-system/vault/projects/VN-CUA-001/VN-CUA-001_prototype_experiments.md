---
project: VN-CUA-001
designation: VDC-33
type: experiment_procedures
version: 1.0
created: 2026-02-05
status: draft
experiments: 6
---

# VN-CUA-001: VDC-33 PROTOTYPE EXPERIMENTS
## Test Procedures & Data Collection

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Purpose:** Validate design assumptions, optimize parameters for Phase 4
**Date:** 2026-02-05

---

## EXPERIMENT INDEX

| # | Experiment | Purpose | Priority | Duration |
|---|------------|---------|----------|----------|
| 1 | Velocity vs Pressure | Regulator specification | HIGH | 2 hours |
| 2 | Valve Timing Optimization | Solenoid driver design | HIGH | 3 hours |
| 3 | Safety Interlock Validation | Safety architecture | CRITICAL | 2 hours |
| 4 | Projectile Stability | Fin geometry selection | HIGH | 4 hours |
| 5 | Recoil Characterization | Stock/pad design | MEDIUM | 2 hours |
| 6 | Gas Consumption | Cylinder sizing | MEDIUM | 1 hour |

---

## GENERAL SAFETY REQUIREMENTS

```
⚠️ MANDATORY FOR ALL EXPERIMENTS
═══════════════════════════════════════════════════════════════════════════

PERSONAL PROTECTIVE EQUIPMENT (PPE):
☐ Safety glasses (ANSI Z87.1) - ALL personnel
☐ Hearing protection (if >85 dB)
☐ Closed-toe shoes

RANGE SAFETY:
☐ Minimum 10m clear downrange
☐ Adequate backstop (plywood + foam)
☐ No personnel forward of firing line
☐ Designated range officer for each session

EQUIPMENT CHECKS:
☐ Visual inspection of all seals/O-rings
☐ Verify pressure gauge reads zero before handling
☐ Check all fittings with soapy water at low pressure
☐ Verify safety interlock function before loading

EMERGENCY PROCEDURES:
• Leak: Point safe direction, allow natural depressurization
• Misfire: Wait 30 seconds, then safe and inspect
• Injury: First aid kit on site, emergency contact posted

═══════════════════════════════════════════════════════════════════════════
```

---

# EXPERIMENT 1: VELOCITY VS PRESSURE

## 1.1 Objective

Characterize muzzle velocity as a function of regulated pressure to:
- Validate pneumatic model
- Determine optimal operating pressure for VDC-100
- Establish velocity consistency (standard deviation)

## 1.2 Equipment Required

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | Assembled, tested | 1 |
| Chronograph | Airsoft/paintball type | 1 |
| Tennis balls | 58mm standard | 20 |
| Foam sabots | 32mm OD | 20 |
| Pressure gauge | 0-160 bar, calibrated | 1 |
| Adjustable regulator | Ninja SLP or similar | 1 |
| Data recording sheet | Printed | 1 |
| Hex keys | For regulator adjustment | 1 set |

## 1.3 Test Setup

```
EXPERIMENT 1 SETUP
═══════════════════════════════════════════════════════════════════════════

                    FIRING LINE                    CHRONOGRAPH
                        │                              │
                        │         2.0m                 │         8.0m
        ┌───────────────┼──────────────────────────────┼─────────────────┐
        │               │                              │                 │
        │   ┌───────────┴───────────┐      ┌──────────┴──────────┐     │
        │   │                       │      │                      │     │
        │   │      VDC-33          ═══════►│    CHRONOGRAPH      │     │
        │   │    (on rest)          │      │    (on tripod)       │     │
        │   │                       │      │                      │     │
        │   └───────────────────────┘      └─────────────────────┘     │
        │                                                               │
        │   Height: 1.2m                   Height: 1.2m (aligned)      │
        │                                                               │
        └───────────────────────────────────────────────────────────────┘
                                                              │
                                                      BACKSTOP
                                                   (plywood + foam)

ALIGNMENT:
• Chronograph sensors perpendicular to flight path
• Barrel axis through center of chronograph window
• Level both launcher and chronograph

═══════════════════════════════════════════════════════════════════════════
```

## 1.4 Procedure

### Pre-Test Checklist
```
☐ Chronograph battery charged, display visible
☐ Chronograph positioned 2.0m from muzzle
☐ Launcher secured on stable rest
☐ 20× projectiles prepared (tennis ball + sabot)
☐ Tank filled to 200+ bar
☐ Regulator set to starting pressure (40 bar)
☐ Safety interlock verified functional
☐ Range clear, backstop in place
☐ Data sheet ready
```

### Test Matrix

| Run | Pressure (bar) | Shots | Notes |
|-----|----------------|-------|-------|
| 1 | 40 | 5 | Below expected range |
| 2 | 50 | 5 | Low end |
| 3 | 60 | 5 | Target operating |
| 4 | 70 | 5 | Target operating |
| 5 | 80 | 5 | Target operating |
| 6 | 90 | 5 | High end |
| 7 | 100 | 5 | Maximum |

### Step-by-Step Procedure

```
PROCEDURE: VELOCITY VS PRESSURE
═══════════════════════════════════════════════════════════════════════════

1. SETUP (15 min)
   a. Position launcher on rest at 1.2m height
   b. Position chronograph at 2.0m, aligned with bore
   c. Verify alignment with laser pointer or bore sight
   d. Set regulator to 40 bar (first test point)
   e. Arm safety interlock, verify LED indication

2. FIRING SEQUENCE (per pressure setting)
   a. Record ambient conditions (temp, humidity)
   b. Load projectile (tennis ball in sabot)
   c. Verify pressure gauge reading
   d. Clear range ("RANGE HOT")
   e. Arm system (ARM switch ON)
   f. Disengage safety (SAFETY to FIRE)
   g. Fire (pull trigger)
   h. Record velocity from chronograph
   i. Safe system (SAFETY to SAFE, ARM OFF)
   j. Repeat steps b-i for 5 shots
   k. Calculate mean and std dev

3. PRESSURE CHANGE
   a. Depressurize system (if needed for adjustment)
   b. Adjust regulator to next pressure setting
   c. Re-pressurize and verify new setting
   d. Continue to step 2

4. DATA RECORDING
   a. Record all velocities immediately
   b. Note any anomalies (sabot separation, tumbling)
   c. Calculate statistics after each pressure point
   d. Plot preliminary data to check trends

═══════════════════════════════════════════════════════════════════════════
```

## 1.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════
EXPERIMENT 1: VELOCITY VS PRESSURE - DATA SHEET
═══════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________  Witness: ____________

Ambient Conditions:
  Temperature: _______ °C    Humidity: _______ %    Pressure: _______ mbar

Equipment:
  Tank pressure (start): _______ bar    Chronograph S/N: _______________
  Projectile mass: _______ g            Sabot mass: _______ g

═══════════════════════════════════════════════════════════════════════════
RUN 1: Regulated Pressure = 40 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════
RUN 2: Regulated Pressure = 50 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════
RUN 3: Regulated Pressure = 60 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════
RUN 4: Regulated Pressure = 70 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════
RUN 5: Regulated Pressure = 80 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════
RUN 6: Regulated Pressure = 90 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════
RUN 7: Regulated Pressure = 100 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Velocity (m/s) │ Notes
─────┼────────────────┼────────────────────────────────────────────────────
  1  │                │
  2  │                │
  3  │                │
  4  │                │
  5  │                │
─────┼────────────────┼────────────────────────────────────────────────────
Mean │                │  Std Dev:
═══════════════════════════════════════════════════════════════════════════

SUMMARY TABLE:
───────────────────────────────────────────────────────────────────────────
Pressure (bar) │  40  │  50  │  60  │  70  │  80  │  90  │ 100  │
───────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
Mean V (m/s)   │      │      │      │      │      │      │      │
Std Dev (m/s)  │      │      │      │      │      │      │      │
───────────────────────────────────────────────────────────────────────────

Tank pressure (end): _______ bar    Total shots fired: _______

Signatures:
  Operator: _____________________    Date: ____________
  Witness:  _____________________    Date: ____________

═══════════════════════════════════════════════════════════════════════════
```

## 1.6 Analysis Method

### Expected Model

For pneumatic launchers, velocity typically follows:

```
V = k × √(P × A / m)

Where:
  V = muzzle velocity (m/s)
  k = efficiency constant (0.7-0.9 typical)
  P = regulated pressure (Pa)
  A = bore area (m²)
  m = projectile mass (kg)
```

### Analysis Steps

1. **Plot V vs P** (scatter plot with error bars)
2. **Fit curve**: V = a × P^b (expect b ≈ 0.5)
3. **Calculate R²** to assess fit quality
4. **Identify optimal pressure** for target velocity (35-40 m/s)
5. **Assess consistency**: std dev should be <5% of mean

### Scaling to VDC-100

```
SCALING CALCULATION
═══════════════════════════════════════════════════════════════════════════

Given:
  VDC-33 bore area:  A₁ = π × (16mm)² = 804 mm²
  VDC-100 bore area: A₂ = π × (50mm)² = 7854 mm²
  Area ratio: A₂/A₁ = 9.77×

  VDC-33 projectile:  m₁ = 58g
  VDC-100 projectile: m₂ = 450g
  Mass ratio: m₂/m₁ = 7.76×

For same velocity at same pressure:
  Gas volume ratio ≈ (A₂/A₁) × (m₂/m₁)^0.5 ≈ 9.77 × 2.78 ≈ 27×

This informs:
  • Valve orifice sizing (scale by √ratio)
  • Dwell time adjustment
  • Chamber volume

═══════════════════════════════════════════════════════════════════════════
```

## 1.7 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| Velocity at 70 bar | 30-40 m/s | Adjust pressure, check seals |
| Std dev | <2 m/s (<5%) | Improve seal, sabot fit |
| Curve fit R² | >0.95 | Check for leaks, valve issues |
| No misfires | 0 in 35 shots | Debug safety/valve circuit |

---

# EXPERIMENT 2: VALVE TIMING OPTIMIZATION

## 2.1 Objective

Optimize solenoid dwell time to:
- Maximize velocity for given pressure
- Maximize gas efficiency (shots per fill)
- Determine minimum reliable dwell time

## 2.2 Equipment Required

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | With Arduino control | 1 |
| Chronograph | Airsoft/paintball type | 1 |
| Oscilloscope (optional) | 2-ch, 50MHz | 1 |
| Tennis balls + sabots | | 30 |
| USB cable | For Arduino programming | 1 |
| Laptop | With Arduino IDE | 1 |

## 2.3 Test Setup

Same physical setup as Experiment 1.

**Arduino Modification:** Change `DWELL_MS` constant for each test point.

```cpp
// Modify this value for each test run
const int DWELL_MS = 8;  // Test values: 5, 8, 10, 12, 15, 20, 25 ms
```

## 2.4 Procedure

### Test Matrix

| Run | Dwell (ms) | Pressure | Shots | Purpose |
|-----|------------|----------|-------|---------|
| 1 | 5 | 70 bar | 5 | Minimum boundary |
| 2 | 8 | 70 bar | 5 | Expected optimal |
| 3 | 10 | 70 bar | 5 | Baseline |
| 4 | 12 | 70 bar | 5 | Extended |
| 5 | 15 | 70 bar | 5 | Extended |
| 6 | 20 | 70 bar | 5 | Maximum |
| 7 | 25 | 70 bar | 5 | Over-dwell check |

### Step-by-Step

```
PROCEDURE: VALVE TIMING
═══════════════════════════════════════════════════════════════════════════

1. PREPARATION
   a. Set regulator to fixed pressure (70 bar from Exp 1 results)
   b. Connect Arduino to laptop via USB
   c. Open Arduino IDE with safety code
   d. Note starting tank pressure

2. FOR EACH DWELL SETTING:
   a. Upload modified code with new DWELL_MS value
   b. Verify upload successful (LED blink pattern)
   c. Disconnect USB
   d. Fire 5 shots, record velocities
   e. Record tank pressure after 5 shots
   f. Reconnect USB for next modification

3. OSCILLOSCOPE (Optional):
   a. Probe CH1: Solenoid drive signal (0-12V)
   b. Probe CH2: Trigger switch (0-5V)
   c. Measure actual dwell time vs programmed
   d. Measure solenoid response delay

4. DATA ANALYSIS:
   a. Plot velocity vs dwell time
   b. Identify knee point (diminishing returns)
   c. Calculate gas efficiency (shots/bar consumed)
   d. Select optimal dwell for VDC-100

═══════════════════════════════════════════════════════════════════════════
```

## 2.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════
EXPERIMENT 2: VALVE TIMING - DATA SHEET
═══════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________

Fixed Parameters:
  Regulated pressure: 70 bar
  Projectile mass: _______ g
  Starting tank pressure: _______ bar

═══════════════════════════════════════════════════════════════════════════
       │ Dwell │ Shot Velocities (m/s)      │ Mean  │ Tank P │ ΔP per │
Run    │ (ms)  │  1    2    3    4    5     │ (m/s) │ after  │ 5 shots│
───────┼───────┼────────────────────────────┼───────┼────────┼────────┤
  1    │   5   │                            │       │        │        │
  2    │   8   │                            │       │        │        │
  3    │  10   │                            │       │        │        │
  4    │  12   │                            │       │        │        │
  5    │  15   │                            │       │        │        │
  6    │  20   │                            │       │        │        │
  7    │  25   │                            │       │        │        │
═══════════════════════════════════════════════════════════════════════════

OSCILLOSCOPE MEASUREMENTS (if available):
───────────────────────────────────────────────────────────────────────────
Programmed Dwell │ Actual Dwell │ Solenoid Delay │ Notes
────────────────┼──────────────┼────────────────┼───────────────────────
      5 ms      │              │                │
      8 ms      │              │                │
     10 ms      │              │                │
     12 ms      │              │                │
═══════════════════════════════════════════════════════════════════════════

ANALYSIS:
  Optimal dwell (velocity plateau): _______ ms
  Gas efficiency peak: _______ ms
  Recommended VDC-100 dwell: _______ ms

═══════════════════════════════════════════════════════════════════════════
```

## 2.6 Expected Results

```
EXPECTED VELOCITY VS DWELL CURVE
═══════════════════════════════════════════════════════════════════════════

Velocity
(m/s)
   40 ┤                          ●────●────●────●  (plateau)
      │                      ●
   35 ┤                  ●
      │              ●
   30 ┤          ●
      │      ●
   25 ┤  ●
      │
   20 ┼──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──
         5    8   10  12  15     20     25
                    Dwell Time (ms)

INTERPRETATION:
• Below 8ms: Insufficient gas flow, low velocity
• 8-12ms: Steep increase, approaching optimal
• 12-15ms: Knee point, diminishing returns
• >15ms: Plateau, wasting gas

OPTIMAL SELECTION:
• Choose dwell just past knee point
• Balance velocity vs gas efficiency
• Add 20% margin for VDC-100 (larger volume)

═══════════════════════════════════════════════════════════════════════════
```

## 2.7 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| Clear knee point identified | Yes | Extend test range |
| Velocity plateau reached | Within 5% of max | Increase max dwell |
| Gas consumption linear | R² > 0.9 | Check for leaks |
| Solenoid response | <5ms delay | Replace solenoid |

---

# EXPERIMENT 3: SAFETY INTERLOCK VALIDATION

## 3.1 Objective

Verify that the 3-level safety interlock system:
- Prevents unintended discharge in all unsafe states
- Permits firing only when all conditions met
- Fails safe in all failure modes

## 3.2 Equipment Required

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | Fully assembled | 1 |
| Multimeter | For continuity checks | 1 |
| Test jumper wires | For fault injection | 5 |
| Data recording sheet | Printed | 1 |
| Witness | Second person | 1 |

## 3.3 Test Matrix

### State Permutation Test

All 8 combinations of ARM, SAFETY, TRIGGER:

| Test | ARM | SAFETY | TRIGGER | Expected | Actual |
|------|-----|--------|---------|----------|--------|
| S1 | OFF | SAFE | Released | NO FIRE | |
| S2 | OFF | SAFE | Pressed | NO FIRE | |
| S3 | OFF | FIRE | Released | NO FIRE | |
| S4 | OFF | FIRE | Pressed | NO FIRE | |
| S5 | ON | SAFE | Released | NO FIRE | |
| S6 | ON | SAFE | Pressed | NO FIRE | |
| S7 | ON | FIRE | Released | NO FIRE | |
| **S8** | **ON** | **FIRE** | **Pressed** | **FIRE** | |

### Failure Mode Test

| Test | Failure Injected | Expected | Actual |
|------|------------------|----------|--------|
| F1 | Battery disconnected | NO FIRE, LED OFF | |
| F2 | Low battery (<10V) | NO FIRE, warning | |
| F3 | ARM switch stuck ON | NO FIRE if SAFE | |
| F4 | Solenoid wire disconnected | NO FIRE | |
| F5 | Arduino reset during armed | NO FIRE (re-init) | |

### Indication Test

| Test | State | Expected LED | Actual |
|------|-------|--------------|--------|
| I1 | Power OFF | OFF | |
| I2 | Power ON, SAFE | GREEN | |
| I3 | Power ON, ARMED | RED | |
| I4 | Low battery | FLASH/buzzer | |

## 3.4 Procedure

```
PROCEDURE: SAFETY INTERLOCK VALIDATION
═══════════════════════════════════════════════════════════════════════════

⚠️ CRITICAL: Perform tests with DEPRESSURIZED system first!

PHASE 1: ELECTRICAL VERIFICATION (No pressure)
─────────────────────────────────────────────────────────────────────────────
1. Verify all wiring per schematic
2. Power on system
3. Measure voltages at key points:
   • Battery: _____ V (expect 10.5-12.6V)
   • Arduino 5V rail: _____ V (expect 4.8-5.2V)
   • Solenoid (when fired): _____ V (expect 11-12V)

PHASE 2: STATE PERMUTATION (No pressure)
─────────────────────────────────────────────────────────────────────────────
For each state S1-S8:
1. Set ARM switch to specified position
2. Set SAFETY switch to specified position
3. Observe LED indication (record color)
4. Pull trigger
5. Listen/feel for solenoid click (indicates valve attempt)
6. Record: CLICK or NO CLICK

Expected:
• S1-S7: NO CLICK (interlock working)
• S8: CLICK (fire permitted)

PHASE 3: FAILURE MODE (No pressure)
─────────────────────────────────────────────────────────────────────────────
For each failure F1-F5:
1. Set system to ARMED state (ARM=ON, SAFE=OFF)
2. Inject failure (disconnect wire, reduce voltage, etc.)
3. Pull trigger
4. Observe response
5. Restore normal state
6. Record result

Expected: All failures → NO FIRE

PHASE 4: LIVE FIRE VERIFICATION (With pressure)
─────────────────────────────────────────────────────────────────────────────
1. Pressurize to 50 bar (reduced for safety test)
2. Load inert projectile (foam only)
3. Verify S8 state fires correctly
4. Verify S6 state (SAFE engaged) blocks fire
5. Repeat 3× each to confirm reliability

═══════════════════════════════════════════════════════════════════════════
```

## 3.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════
EXPERIMENT 3: SAFETY INTERLOCK VALIDATION - DATA SHEET
═══════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________  Witness: ____________

PHASE 1: ELECTRICAL VERIFICATION
───────────────────────────────────────────────────────────────────────────
Battery voltage:        _______ V    (Pass: 10.5-12.6V)    ☐ PASS  ☐ FAIL
Arduino 5V rail:        _______ V    (Pass: 4.8-5.2V)      ☐ PASS  ☐ FAIL
Solenoid drive (fire):  _______ V    (Pass: >10V)          ☐ PASS  ☐ FAIL

PHASE 2: STATE PERMUTATION TEST
───────────────────────────────────────────────────────────────────────────
Test │ ARM │ SAFETY │TRIGGER │ Expected │ LED   │ Solenoid │ Result │
─────┼─────┼────────┼────────┼──────────┼───────┼──────────┼────────┤
 S1  │ OFF │  SAFE  │  REL   │ NO FIRE  │       │          │☐P  ☐F │
 S2  │ OFF │  SAFE  │ PRESS  │ NO FIRE  │       │          │☐P  ☐F │
 S3  │ OFF │  FIRE  │  REL   │ NO FIRE  │       │          │☐P  ☐F │
 S4  │ OFF │  FIRE  │ PRESS  │ NO FIRE  │       │          │☐P  ☐F │
 S5  │ ON  │  SAFE  │  REL   │ NO FIRE  │       │          │☐P  ☐F │
 S6  │ ON  │  SAFE  │ PRESS  │ NO FIRE  │       │          │☐P  ☐F │
 S7  │ ON  │  FIRE  │  REL   │ NO FIRE  │       │          │☐P  ☐F │
 S8  │ ON  │  FIRE  │ PRESS  │  FIRE    │       │          │☐P  ☐F │
───────────────────────────────────────────────────────────────────────────
                                        STATE TEST:  ___/8 PASS

PHASE 3: FAILURE MODE TEST
───────────────────────────────────────────────────────────────────────────
Test │ Failure Injected         │ Expected │ Observed │ Result │
─────┼──────────────────────────┼──────────┼──────────┼────────┤
 F1  │ Battery disconnected     │ NO FIRE  │          │☐P  ☐F │
 F2  │ Low battery (<10V)       │ NO FIRE  │          │☐P  ☐F │
 F3  │ ARM switch stuck ON      │ NO FIRE* │          │☐P  ☐F │
 F4  │ Solenoid wire disconnect │ NO FIRE  │          │☐P  ☐F │
 F5  │ Arduino reset while armed│ NO FIRE  │          │☐P  ☐F │
───────────────────────────────────────────────────────────────────────────
*With SAFETY engaged                    FAILURE TEST:  ___/5 PASS

PHASE 4: INDICATION TEST
───────────────────────────────────────────────────────────────────────────
Test │ State              │ Expected LED │ Observed │ Result │
─────┼────────────────────┼──────────────┼──────────┼────────┤
 I1  │ Power OFF          │ OFF          │          │☐P  ☐F │
 I2  │ Power ON, SAFE     │ GREEN        │          │☐P  ☐F │
 I3  │ Power ON, ARMED    │ RED          │          │☐P  ☐F │
 I4  │ Low battery        │ FLASH/buzz   │          │☐P  ☐F │
───────────────────────────────────────────────────────────────────────────
                                      INDICATION TEST:  ___/4 PASS

PHASE 5: LIVE FIRE VERIFICATION (50 bar, foam projectile)
───────────────────────────────────────────────────────────────────────────
Test │ State         │ Expected │ Observed │ Result │
─────┼───────────────┼──────────┼──────────┼────────┤
 L1  │ S8 (all ON)   │ FIRE     │          │☐P  ☐F │
 L2  │ S8 (all ON)   │ FIRE     │          │☐P  ☐F │
 L3  │ S8 (all ON)   │ FIRE     │          │☐P  ☐F │
 L4  │ S6 (SAFE ON)  │ NO FIRE  │          │☐P  ☐F │
 L5  │ S6 (SAFE ON)  │ NO FIRE  │          │☐P  ☐F │
 L6  │ S6 (SAFE ON)  │ NO FIRE  │          │☐P  ☐F │
───────────────────────────────────────────────────────────────────────────
                                        LIVE TEST:  ___/6 PASS

═══════════════════════════════════════════════════════════════════════════
OVERALL RESULT:  ___/23 TESTS PASSED

☐ ALL PASS - Safety interlock VALIDATED
☐ FAILURES - Document and resolve before proceeding

Notes/Observations:
___________________________________________________________________________
___________________________________________________________________________

Signatures:
  Operator: _____________________    Date: ____________
  Witness:  _____________________    Date: ____________
═══════════════════════════════════════════════════════════════════════════
```

## 3.6 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| State permutation | 8/8 pass | Debug logic, check wiring |
| Failure modes | 5/5 pass | Redesign fail-safe |
| Indication | 4/4 pass | Check LED wiring |
| Live fire | 6/6 pass | Full system debug |
| **OVERALL** | **23/23** | **Do not proceed until 100%** |

---

# EXPERIMENT 4: PROJECTILE STABILITY

## 4.1 Objective

Evaluate fin configurations to:
- Achieve stable flight (no tumbling)
- Optimize spin rate for net deployment
- Select best fin design for VDC-100 projectile

## 4.2 Equipment Required

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | Operational | 1 |
| Fin Set A | 4-fin, 15° cant | 4 projectiles |
| Fin Set B | 4-fin, 10° cant | 4 projectiles |
| Fin Set C | 6-fin, straight | 4 projectiles |
| High-speed camera | 240fps minimum | 1 |
| Tripod | For camera | 1 |
| Measuring tape | 10m | 1 |
| Markers | For range marking | 5 |

## 4.3 Test Setup

```
EXPERIMENT 4 SETUP: STABILITY TEST
═══════════════════════════════════════════════════════════════════════════

                              CAMERA POSITION
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
    FIRING          │               ▼               │         BACKSTOP
    LINE            │         ┌─────────┐          │
      │             │         │ HI-SPEED │          │             │
      │    2m       │   5m    │  CAMERA  │   3m     │    5m       │
      ▼             │         │ (side)   │          │             ▼
  ┌───────┐        │         └─────────┘          │        ┌─────────┐
  │VDC-33 │════════●═══════════════════════════════●═══════│BACKSTOP │
  └───────┘      Mark 1                          Mark 2    └─────────┘
                (2m)                             (7m)

CAMERA SETTINGS:
• Frame rate: 240 fps (or higher)
• Shutter: 1/1000s minimum
• Focus: Pre-set on flight path
• Field of view: Capture 2m-7m range
• Lighting: Bright, even (outdoor daylight ideal)

MARKERS:
• Visible distance markers at 2m intervals
• White background behind flight path (optional)

═══════════════════════════════════════════════════════════════════════════
```

## 4.4 Procedure

```
PROCEDURE: PROJECTILE STABILITY
═══════════════════════════════════════════════════════════════════════════

1. SETUP
   a. Position camera perpendicular to flight path
   b. Set camera to high-speed mode (240fps+)
   c. Mark distance intervals (2m, 4m, 6m)
   d. Verify lighting adequate for high shutter speed
   e. Test camera trigger synchronization

2. FOR EACH FIN CONFIGURATION (A, B, C):
   a. Load projectile with specified fins
   b. Start camera recording
   c. Fire at 70 bar (standard pressure)
   d. Stop recording
   e. Review footage immediately
   f. Repeat 4× per configuration

3. VIDEO ANALYSIS (per shot):
   a. Count frames from muzzle exit to 5m mark
   b. Calculate velocity: V = distance / (frames ÷ fps)
   c. Count visible rotations in flight
   d. Calculate spin rate: RPM = (rotations × fps × 60) / frames
   e. Assess stability: STABLE / WOBBLE / TUMBLE
   f. Note any anomalies (sabot separation, fin damage)

4. SCORING:
   Stability score per shot:
   • STABLE (no visible wobble): 3 points
   • SLIGHT WOBBLE (<10° deviation): 2 points
   • MODERATE WOBBLE (10-30°): 1 point
   • TUMBLE (>30° or flip): 0 points

═══════════════════════════════════════════════════════════════════════════
```

## 4.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════
EXPERIMENT 4: PROJECTILE STABILITY - DATA SHEET
═══════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________

Camera: ____________  Frame rate: _______ fps  Shutter: _______

Fixed Parameters:
  Pressure: 70 bar    Projectile base mass: _______ g

═══════════════════════════════════════════════════════════════════════════
FIN SET A: 4-fin, 15° cant angle
───────────────────────────────────────────────────────────────────────────
Shot │Frames│Velocity│Rotations│ Spin  │Stability│Score│Notes
     │(5m)  │ (m/s)  │ (5m)    │ (RPM) │         │     │
─────┼──────┼────────┼─────────┼───────┼─────────┼─────┼───────────────
  1  │      │        │         │       │         │     │
  2  │      │        │         │       │         │     │
  3  │      │        │         │       │         │     │
  4  │      │        │         │       │         │     │
─────┼──────┼────────┼─────────┼───────┼─────────┼─────┼───────────────
AVG  │      │        │         │       │         │ /12 │
═══════════════════════════════════════════════════════════════════════════
FIN SET B: 4-fin, 10° cant angle
───────────────────────────────────────────────────────────────────────────
Shot │Frames│Velocity│Rotations│ Spin  │Stability│Score│Notes
     │(5m)  │ (m/s)  │ (5m)    │ (RPM) │         │     │
─────┼──────┼────────┼─────────┼───────┼─────────┼─────┼───────────────
  1  │      │        │         │       │         │     │
  2  │      │        │         │       │         │     │
  3  │      │        │         │       │         │     │
  4  │      │        │         │       │         │     │
─────┼──────┼────────┼─────────┼───────┼─────────┼─────┼───────────────
AVG  │      │        │         │       │         │ /12 │
═══════════════════════════════════════════════════════════════════════════
FIN SET C: 6-fin, 0° (straight)
───────────────────────────────────────────────────────────────────────────
Shot │Frames│Velocity│Rotations│ Spin  │Stability│Score│Notes
     │(5m)  │ (m/s)  │ (5m)    │ (RPM) │         │     │
─────┼──────┼────────┼─────────┼───────┼─────────┼─────┼───────────────
  1  │      │        │         │       │         │     │
  2  │      │        │         │       │         │     │
  3  │      │        │         │       │         │     │
  4  │      │        │         │       │         │     │
─────┼──────┼────────┼─────────┼───────┼─────────┼─────┼───────────────
AVG  │      │        │         │       │         │ /12 │
═══════════════════════════════════════════════════════════════════════════

COMPARISON SUMMARY:
───────────────────────────────────────────────────────────────────────────
Fin Set │ Avg Velocity │ Avg Spin │ Stability Score │ Rank │
────────┼──────────────┼──────────┼─────────────────┼──────┤
   A    │              │          │       /12       │      │
   B    │              │          │       /12       │      │
   C    │              │          │       /12       │      │
───────────────────────────────────────────────────────────────────────────

SELECTED FOR VDC-100: Fin Set _____

Rationale:
___________________________________________________________________________
___________________________________________________________________________

═══════════════════════════════════════════════════════════════════════════
```

## 4.6 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| At least one config stable | Score ≥10/12 | Design new fin geometry |
| Spin rate achieved | 100-500 RPM | Adjust cant angle |
| No tumbling | 0 tumble events | Increase fin area |
| Consistent results | Std dev <20% | Check sabot fit |

---

# EXPERIMENT 5: RECOIL CHARACTERIZATION

## 5.1 Objective

Measure recoil impulse to:
- Verify operator comfort (<15 Ns requirement)
- Inform stock/recoil pad design for VDC-100
- Validate scaling predictions

## 5.2 Equipment Required

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | Operational | 1 |
| Digital scale | 50kg capacity, peak hold | 1 |
| Recoil fixture | Rigid mount to scale | 1 |
| Stopwatch | 0.01s resolution | 1 |
| Accelerometer (optional) | ADXL345 or smartphone | 1 |

## 5.3 Test Setup

```
EXPERIMENT 5 SETUP: RECOIL MEASUREMENT
═══════════════════════════════════════════════════════════════════════════

METHOD A: Scale-based (Simple)
─────────────────────────────────────────────────────────────────────────────

                    ┌─────────────────────────────────────┐
                    │           RIGID FRAME               │
                    │    (prevents lateral movement)      │
                    └──────────────────┬──────────────────┘
                                       │
    ┌──────────────────────────────────┼──────────────────────────────────┐
    │                                  │                                  │
    │   ┌──────────────────────────────┴──────────────────────────────┐  │
    │   │                        VDC-33                                │  │
    │   │                    (secured to plate)                        │  │
    │   └──────────────────────────────┬──────────────────────────────┘  │
    │                                  │                                  │
    │                         ┌────────┴────────┐                        │
    │                         │  MOUNTING PLATE │                        │
    │                         │  (transmits force)                       │
    │                         └────────┬────────┘                        │
    │                                  │                                  │
    │                         ┌────────┴────────┐                        │
    │                         │  DIGITAL SCALE  │                        │
    │                         │  (peak hold)    │                        │
    │                         └────────┬────────┘                        │
    │                                  │                                  │
    │                         ┌────────┴────────┐                        │
    │                         │   RIGID BASE    │                        │
    │                         └─────────────────┘                        │
    │                                                                     │
    └─────────────────────────────────────────────────────────────────────┘

Measurement: Peak force (kg) × 9.81 = Peak force (N)
Impulse estimate: F_peak × t_duration (from video or accelerometer)


METHOD B: Accelerometer-based (More accurate)
─────────────────────────────────────────────────────────────────────────────

    ┌───────────────────────────────────────────────────────────────────┐
    │                          VDC-33                                   │
    │                                                                   │
    │     ┌─────────────┐                                               │
    │     │ACCELEROMETER│ ← Mounted on receiver, aligned with bore     │
    │     │  (ADXL345)  │                                               │
    │     └──────┬──────┘                                               │
    │            │ I2C to Arduino                                       │
    └────────────│──────────────────────────────────────────────────────┘
                 │
         ┌───────┴───────┐
         │    ARDUINO    │──── Log acceleration at 1000 Hz
         │   (logging)   │
         └───────────────┘

Measurement: Integrate acceleration to get velocity change
Impulse: m_system × Δv = ∫F dt

═══════════════════════════════════════════════════════════════════════════
```

## 5.4 Procedure

```
PROCEDURE: RECOIL CHARACTERIZATION
═══════════════════════════════════════════════════════════════════════════

METHOD A: SCALE-BASED

1. SETUP
   a. Mount VDC-33 on rigid plate
   b. Place plate on digital scale (peak hold mode)
   c. Secure against lateral movement
   d. Zero scale with system in place
   e. Set pressure to test value

2. MEASUREMENT
   a. Load projectile
   b. Reset scale peak hold
   c. Fire
   d. Record peak force reading
   e. Repeat 5× per pressure setting

3. DATA PROCESSING
   a. Peak force = scale reading × 9.81 N
   b. Estimate impulse duration from video (~20-50ms typical)
   c. Impulse ≈ 0.5 × F_peak × t_duration (triangular pulse)


METHOD B: ACCELEROMETER-BASED

1. SETUP
   a. Mount accelerometer on receiver (use hot glue or tape)
   b. Connect to Arduino with logging code
   c. Set sample rate to 1000 Hz minimum
   d. Verify axis alignment (X = bore axis)

2. MEASUREMENT
   a. Load projectile
   b. Start data logging
   c. Fire
   d. Stop logging after 1 second
   e. Download data
   f. Repeat 5× per pressure setting

3. DATA PROCESSING
   a. Identify acceleration pulse (typically 10-50ms)
   b. Integrate: Δv = ∫a dt
   c. Calculate impulse: J = m_system × Δv
   d. Calculate equivalent force: F_avg = J / t_duration

═══════════════════════════════════════════════════════════════════════════
```

## 5.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════
EXPERIMENT 5: RECOIL CHARACTERIZATION - DATA SHEET
═══════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________

System mass (VDC-33 + mount): _______ kg
Projectile mass: _______ g

═══════════════════════════════════════════════════════════════════════════
TEST SERIES 1: Pressure = 60 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Peak Force │ Peak Force │ Duration │ Impulse  │ Notes
     │   (kg)     │    (N)     │   (ms)   │  (Ns)    │
─────┼────────────┼────────────┼──────────┼──────────┼────────────────
  1  │            │            │          │          │
  2  │            │            │          │          │
  3  │            │            │          │          │
  4  │            │            │          │          │
  5  │            │            │          │          │
─────┼────────────┼────────────┼──────────┼──────────┼────────────────
AVG  │            │            │          │          │
═══════════════════════════════════════════════════════════════════════════
TEST SERIES 2: Pressure = 80 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Peak Force │ Peak Force │ Duration │ Impulse  │ Notes
     │   (kg)     │    (N)     │   (ms)   │  (Ns)    │
─────┼────────────┼────────────┼──────────┼──────────┼────────────────
  1  │            │            │          │          │
  2  │            │            │          │          │
  3  │            │            │          │          │
  4  │            │            │          │          │
  5  │            │            │          │          │
─────┼────────────┼────────────┼──────────┼──────────┼────────────────
AVG  │            │            │          │          │
═══════════════════════════════════════════════════════════════════════════
TEST SERIES 3: Pressure = 100 bar
───────────────────────────────────────────────────────────────────────────
Shot │ Peak Force │ Peak Force │ Duration │ Impulse  │ Notes
     │   (kg)     │    (N)     │   (ms)   │  (Ns)    │
─────┼────────────┼────────────┼──────────┼──────────┼────────────────
  1  │            │            │          │          │
  2  │            │            │          │          │
  3  │            │            │          │          │
  4  │            │            │          │          │
  5  │            │            │          │          │
─────┼────────────┼────────────┼──────────┼──────────┼────────────────
AVG  │            │            │          │          │
═══════════════════════════════════════════════════════════════════════════

SCALING TO VDC-100:
───────────────────────────────────────────────────────────────────────────
VDC-33 measured impulse (100 bar): _______ Ns
Mass ratio (VDC-100/VDC-33): 450g / 58g = 7.76×
Velocity ratio: ~1× (same target)

Predicted VDC-100 impulse: J_100 = J_33 × 7.76 = _______ Ns

VDC-100 requirement: ≤15 Ns
Margin: _______ Ns (_______ %)

☐ PASS: Predicted impulse ≤15 Ns
☐ FAIL: Redesign recoil mitigation needed

═══════════════════════════════════════════════════════════════════════════
```

## 5.6 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| VDC-33 impulse measured | <2.5 Ns @ 100 bar | Check momentum calc |
| Scaled VDC-100 prediction | <15 Ns | Add recoil buffer |
| Consistent measurements | Std dev <15% | Improve fixture rigidity |

---

# EXPERIMENT 6: GAS CONSUMPTION

## 6.1 Objective

Measure gas consumption per shot to:
- Validate cylinder sizing (0.5L @ 300 bar for VDC-100)
- Determine shots per fill
- Optimize dwell time for efficiency

## 6.2 Equipment Required

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | Operational | 1 |
| Digital pressure gauge | 0-250 bar, 0.1 bar resolution | 1 |
| Tennis balls + sabots | | 30 |
| Calculator | | 1 |

## 6.3 Procedure

```
PROCEDURE: GAS CONSUMPTION
═══════════════════════════════════════════════════════════════════════════

1. SETUP
   a. Fill HPA tank to known pressure (record exact value)
   b. Install digital pressure gauge on tank
   c. Set regulator to test pressure (e.g., 70 bar)
   d. Allow system to stabilize (2 minutes)

2. MEASUREMENT
   a. Record starting tank pressure: P_start
   b. Fire 10 shots at consistent pace (10 sec intervals)
   c. Allow pressure to stabilize after last shot
   d. Record ending tank pressure: P_end
   e. Calculate: ΔP = P_start - P_end
   f. Gas per shot: ΔP / 10 shots

3. REPEAT FOR DIFFERENT DWELL TIMES
   a. Test with dwell = 8ms, 12ms, 15ms (from Exp 2)
   b. Compare gas consumption
   c. Identify most efficient dwell time

4. CALCULATE SHOTS PER FILL
   a. Usable pressure range: 300 bar → 120 bar (regulated output limit)
   b. Usable ΔP = 180 bar
   c. Shots per fill = 180 bar / (ΔP per shot)

═══════════════════════════════════════════════════════════════════════════
```

## 6.4 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════
EXPERIMENT 6: GAS CONSUMPTION - DATA SHEET
═══════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________

Tank volume: _______ L (e.g., 0.8L for 48ci)
Regulated pressure: _______ bar

═══════════════════════════════════════════════════════════════════════════
TEST 1: Dwell = 8 ms
───────────────────────────────────────────────────────────────────────────
Starting tank pressure:    _______ bar
Shots fired:               10
Ending tank pressure:      _______ bar
───────────────────────────────────────────────────────────────────────────
Pressure drop (ΔP):        _______ bar
Gas per shot:              _______ bar/shot

═══════════════════════════════════════════════════════════════════════════
TEST 2: Dwell = 12 ms
───────────────────────────────────────────────────────────────────────────
Starting tank pressure:    _______ bar
Shots fired:               10
Ending tank pressure:      _______ bar
───────────────────────────────────────────────────────────────────────────
Pressure drop (ΔP):        _______ bar
Gas per shot:              _______ bar/shot

═══════════════════════════════════════════════════════════════════════════
TEST 3: Dwell = 15 ms
───────────────────────────────────────────────────────────────────────────
Starting tank pressure:    _______ bar
Shots fired:               10
Ending tank pressure:      _______ bar
───────────────────────────────────────────────────────────────────────────
Pressure drop (ΔP):        _______ bar
Gas per shot:              _______ bar/shot

═══════════════════════════════════════════════════════════════════════════
COMPARISON:
───────────────────────────────────────────────────────────────────────────
Dwell (ms) │ Gas/shot (bar) │ Velocity (from Exp 2) │ Efficiency Score │
───────────┼────────────────┼───────────────────────┼──────────────────┤
     8     │                │                       │ V / gas =        │
    12     │                │                       │ V / gas =        │
    15     │                │                       │ V / gas =        │
───────────────────────────────────────────────────────────────────────────

BEST EFFICIENCY: Dwell = _______ ms

═══════════════════════════════════════════════════════════════════════════
SHOTS PER FILL CALCULATION (VDC-33):
───────────────────────────────────────────────────────────────────────────
Tank volume:               0.8 L
Full pressure:             200 bar (typical fill)
Minimum usable:            80 bar (reg cutoff)
Usable range:              120 bar
Gas per shot (optimal):    _______ bar

Shots per fill (VDC-33):   120 / _______ = _______ shots

═══════════════════════════════════════════════════════════════════════════
SCALING TO VDC-100:
───────────────────────────────────────────────────────────────────────────
VDC-100 tank volume:       0.5 L
VDC-100 full pressure:     300 bar
VDC-100 minimum usable:    120 bar
VDC-100 usable range:      180 bar

Bore area ratio:           (100/32)² = 9.77×
Expected gas per shot:     VDC-33 × 9.77 = _______ bar

VDC-100 shots per fill:    180 / _______ = _______ shots

Requirement: ≥5 shots per fill
Result: ☐ PASS  ☐ FAIL

═══════════════════════════════════════════════════════════════════════════
```

## 6.5 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| VDC-33 shots per fill | ≥30 | Check for leaks |
| Scaled VDC-100 shots | ≥5 | Increase tank size |
| Efficiency improves with shorter dwell | Yes | Expected behavior |

---

# SUMMARY: TEST SEQUENCE

```
RECOMMENDED TEST ORDER
═══════════════════════════════════════════════════════════════════════════

DAY 1: Safety & Baseline
─────────────────────────────────────────────────────────────────────────────
☐ EXP 3: Safety Interlock Validation (CRITICAL - do first!)
☐ EXP 1: Velocity vs Pressure (establish baseline)

DAY 2: Optimization
─────────────────────────────────────────────────────────────────────────────
☐ EXP 2: Valve Timing Optimization
☐ EXP 6: Gas Consumption

DAY 3: Dynamics
─────────────────────────────────────────────────────────────────────────────
☐ EXP 4: Projectile Stability (needs good weather/lighting)
☐ EXP 5: Recoil Characterization

TOTAL: 3 test days, ~14 hours of testing

═══════════════════════════════════════════════════════════════════════════
```

---

## DOCUMENT LINKS

- [[VN-CUA-001_prototype_BOM|Prototype Bill of Materials]]
- [[VN-CUA-001_P3_embodiment_design|Phase 3 Embodiment Design]]
- [[VN-CUA-001_product_spec|Product Specification]]

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial experiment procedures. 6 experiments with detailed protocols, data sheets, and success criteria.** |

---

*These procedures support rapid learning and risk reduction for VDC-100 detail design.*
