---
project: VN-CUA-001
designation: VDC-33
type: experiment_procedures
phase: 4
version: 2.0
created: 2026-02-05
updated: 2026-02-08
status: ready
experiments: 6
total_test_time: "~14 hours (3 test days)"
total_shots: "~120"
---

# PHASE 4 — EXPERIMENT PROCEDURES
## VDC-33 Prototype Test Protocols & Data Collection

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Purpose:** Validate design assumptions, optimize parameters, inform VDC-100 full-scale design
**Input:** [[04_detail/prototype_design|Prototype Design]] + [[04_detail/prototype_BOM_procurement|BOM]]

---

# 1. EXPERIMENT INDEX & TEST SEQUENCE

## 1.1 Experiment Summary

| # | Experiment | Purpose | Priority | Duration | Shots |
|---|------------|---------|----------|----------|-------|
| **EXP-1** | Velocity vs Pressure | Characterize pneumatic performance | HIGH | 2h | 35 |
| **EXP-2** | Valve Timing Optimization | Optimize dwell time | HIGH | 3h | 35 |
| **EXP-3** | Safety Interlock Validation | Confirm safety architecture | CRITICAL | 2h | 12 |
| **EXP-4** | Projectile Stability | Select optimal fin configuration | HIGH | 4h | 12 |
| **EXP-5** | Recoil Characterization | Measure impulse for stock design | MEDIUM | 2h | 15 |
| **EXP-6** | Gas Consumption | Determine shots per fill | MEDIUM | 1h | 30 |

## 1.2 Recommended Test Sequence

```
RECOMMENDED TEST ORDER
═══════════════════════════════════════════════════════════════════════════════

DAY 1: Safety & Baseline (~4 hours)
─────────────────────────────────────────────────────────────────────────────
  [ ] EXP-3: Safety Interlock Validation     ** DO FIRST — CRITICAL **
      → Must pass 100% before any live firing
  [ ] EXP-1: Velocity vs Pressure
      → Establishes baseline V(P) curve for all other experiments

DAY 2: Optimization (~4 hours)
─────────────────────────────────────────────────────────────────────────────
  [ ] EXP-2: Valve Timing Optimization
      → Uses optimal pressure from EXP-1
  [ ] EXP-6: Gas Consumption
      → Uses optimal dwell from EXP-2

DAY 3: Dynamics (~6 hours)
─────────────────────────────────────────────────────────────────────────────
  [ ] EXP-4: Projectile Stability
      → Needs good weather/lighting for video
  [ ] EXP-5: Recoil Characterization
      → Uses standard pressure from EXP-1

TOTAL: 3 test days, ~14 hours of testing, ~120 shots

═══════════════════════════════════════════════════════════════════════════════
```

## 1.3 Experiment Dependencies

```
DEPENDENCY MAP
═══════════════════════════════════════════════════════════════════════════════

EXP-3 (Safety)
    |
    | MUST PASS FIRST
    v
EXP-1 (Velocity vs Pressure) ──────────────────> EXP-5 (Recoil)
    |                                                 (uses standard P)
    | provides optimal pressure
    v
EXP-2 (Valve Timing)
    |
    | provides optimal dwell
    v
EXP-6 (Gas Consumption)

EXP-4 (Projectile Stability) ← independent (uses standard P from EXP-1)

═══════════════════════════════════════════════════════════════════════════════
```

---

# 2. GENERAL SAFETY REQUIREMENTS

```
MANDATORY FOR ALL EXPERIMENTS
═══════════════════════════════════════════════════════════════════════════════

PERSONAL PROTECTIVE EQUIPMENT (PPE):
[ ] Safety glasses (ANSI Z87.1) — ALL personnel within 10m
[ ] Hearing protection (if >85 dB)
[ ] Closed-toe shoes
[ ] Gloves for pressure system handling

RANGE SAFETY:
[ ] Minimum 10m clear downrange
[ ] Adequate backstop (plywood + foam, able to stop 40 m/s projectile)
[ ] No personnel forward of firing line
[ ] Designated range officer for each session
[ ] First aid kit on site
[ ] Emergency contact posted

EQUIPMENT CHECKS (before each session):
[ ] Visual inspection of all seals/O-rings
[ ] Verify pressure gauge reads zero before handling
[ ] Check all fittings with soapy water at low pressure (30 bar)
[ ] Verify safety interlock function before loading
[ ] Chronograph battery charged (if used)

OPERATING PROCEDURES:
[ ] "RANGE HOT" call before any pressurized firing
[ ] "RANGE COLD" before anyone goes downrange
[ ] Depressurize before any maintenance or adjustment
[ ] One person fires, one person records data

EMERGENCY PROCEDURES:
• Leak: Point safe direction, allow natural depressurization
• Misfire: Wait 30 seconds, then safe and inspect
• Injury: First aid kit, call emergency services if needed
• Structural failure: Evacuate, depressurize from distance

═══════════════════════════════════════════════════════════════════════════════
```

---

# 3. EXP-1: VELOCITY VS PRESSURE

## 3.1 Objective

Characterize muzzle velocity as a function of regulated pressure to:
- Validate pneumatic model (V proportional to sqrt(P))
- Determine optimal operating pressure for VDC-100
- Establish velocity consistency (standard deviation <5%)

## 3.2 Equipment

| Item | Specification | Qty | From BOM |
|------|---------------|-----|----------|
| VDC-33 prototype | Assembled, safety tested | 1 | — |
| Chronograph | Airsoft/paintball type | 1 | TST-001 |
| Tennis balls | 58mm standard | 20 | PRJ-001 |
| Foam sabots | 32mm OD | 20 | PRJ-002 |
| Pressure gauge | 0-160 bar, calibrated | 1 | PNE-005 |
| Hex keys | For regulator adjustment | 1 set | HDW-010 |
| Data recording sheet | Printed | 1 | Below |

## 3.3 Test Setup

```
EXP-1 SETUP: VELOCITY vs PRESSURE
═══════════════════════════════════════════════════════════════════════════════

    FIRING LINE           2.0m          CHRONOGRAPH      8.0m        BACKSTOP
        |                                    |                           |
        v                                    v                           v
    +-------+                           +--------+                  +--------+
    |VDC-33 | =========================>| CHRONO | ================>|BACKSTOP|
    |(on    |                           |(tripod)|                  |(plywood|
    | rest) |                           |        |                  |+ foam) |
    +-------+                           +--------+                  +--------+
    Height: 1.2m                        Height: 1.2m (aligned)

ALIGNMENT:
• Chronograph sensors perpendicular to flight path
• Barrel axis through center of chronograph window
• Level both launcher and chronograph
• Use laser pointer or bore sight for alignment

═══════════════════════════════════════════════════════════════════════════════
```

## 3.4 Test Matrix

| Run | Pressure (bar) | Shots | Expected V (m/s) | Notes |
|-----|----------------|-------|-------------------|-------|
| 1 | 40 | 5 | ~18 | Below range, baseline |
| 2 | 50 | 5 | ~22 | Low end |
| 3 | 60 | 5 | ~27 | Target operating |
| 4 | 70 | 5 | ~30 | Target operating |
| 5 | 80 | 5 | ~33 | Target operating |
| 6 | 90 | 5 | ~36 | High end |
| 7 | 100 | 5 | ~38 | Maximum |
| | **TOTAL** | **35** | | |

## 3.5 Procedure

```
PROCEDURE: VELOCITY VS PRESSURE
═══════════════════════════════════════════════════════════════════════════════

PRE-TEST CHECKLIST:
[ ] Chronograph battery charged, display visible
[ ] Chronograph positioned 2.0m from muzzle, aligned
[ ] Launcher secured on stable rest at 1.2m height
[ ] 20x projectiles prepared (tennis ball + sabot)
[ ] Tank filled to 200+ bar
[ ] Regulator set to starting pressure (40 bar)
[ ] Safety interlock verified functional (EXP-3 passed)
[ ] Range clear, backstop in place
[ ] Data sheet ready, ambient conditions recorded

FIRING SEQUENCE (per pressure setting):
1. Record ambient conditions (temp, humidity, atm pressure)
2. Load projectile (tennis ball in sabot)
3. Verify pressure gauge reading matches set point
4. Clear range ("RANGE HOT")
5. Arm system (ARM switch ON)
6. Disengage safety (SAFETY to FIRE)
7. Fire (pull trigger)
8. Record velocity from chronograph
9. Safe system (SAFETY to SAFE, ARM OFF)
10. Repeat steps 2-9 for 5 shots
11. Calculate mean and std dev for this pressure

PRESSURE CHANGE:
1. Safe system completely
2. Adjust regulator to next pressure setting
3. Fire 1-2 dry shots (no chrono) to stabilize new pressure
4. Resume firing sequence

═══════════════════════════════════════════════════════════════════════════════
```

## 3.6 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════════
EXP-1: VELOCITY VS PRESSURE — DATA SHEET
═══════════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________  Witness: ____________

Ambient: Temp ___C  Humidity ___%  Atm Pressure ___ mbar
Equipment: Tank P(start) ___ bar  Chrono S/N ___________
Projectile mass: ___ g   Sabot mass: ___ g

───────────────────────────────────────────────────────────────────────────
RUN 1: Regulated Pressure = 40 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

RUN 2: Regulated Pressure = 50 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

RUN 3: Regulated Pressure = 60 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

RUN 4: Regulated Pressure = 70 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

RUN 5: Regulated Pressure = 80 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

RUN 6: Regulated Pressure = 90 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

RUN 7: Regulated Pressure = 100 bar
Shot |  V (m/s) | Notes
─────+──────────+──────────────────────────────────────────────────────
  1  |          |
  2  |          |
  3  |          |
  4  |          |
  5  |          |
─────+──────────+──────────────────────────────────────────────────────
Mean |          |  StdDev:         CV(%):

───────────────────────────────────────────────────────────────────────────
SUMMARY:
P (bar) |  40  |  50  |  60  |  70  |  80  |  90  | 100  |
--------+------+------+------+------+------+------+------+
Mean V  |      |      |      |      |      |      |      |
StdDev  |      |      |      |      |      |      |      |

Tank P(end): ___ bar    Total shots: ___

Signatures:
  Operator: _____________________    Date: ____________
  Witness:  _____________________    Date: ____________
═══════════════════════════════════════════════════════════════════════════════
```

## 3.7 Analysis Method

**Expected model:** V = k * sqrt(P * A / m)
- k = efficiency constant (0.7-0.9 typical for pneumatic launchers)
- P = regulated pressure (Pa)
- A = bore area (m^2)
- m = projectile mass (kg)

**Analysis steps:**
1. Plot V vs P (scatter with error bars)
2. Fit curve: V = a * P^b (expect b ~ 0.5)
3. Calculate R^2 to assess fit quality (target >0.95)
4. Identify optimal pressure for 35-40 m/s target
5. Assess consistency: CV should be <5%

**Scaling to VDC-100:**
- VDC-33 bore area: A1 = pi * (16mm)^2 = 804 mm^2
- VDC-100 bore area: A2 = pi * (50mm)^2 = 7854 mm^2
- Area ratio: 9.77x
- Same pressure → similar velocity → validates VDC-100 design

## 3.8 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| Velocity at 70 bar | 30-40 m/s | Adjust pressure, check seals |
| CV at each pressure | <5% | Improve seal, sabot fit |
| Curve fit R^2 | >0.95 | Check for leaks, valve issues |
| No misfires | 0 in 35 shots | Debug safety/valve circuit |

---

# 4. EXP-2: VALVE TIMING OPTIMIZATION

## 4.1 Objective

Optimize solenoid dwell time to maximize velocity while minimizing gas consumption.

## 4.2 Equipment

Same as EXP-1, plus:
- USB cable for Arduino programming
- Laptop with Arduino IDE

## 4.3 Test Matrix

**Fixed parameter:** Pressure from EXP-1 optimal (expected ~70 bar)

| Run | Dwell (ms) | Shots | Purpose |
|-----|------------|-------|---------|
| 1 | 5 | 5 | Minimum boundary |
| 2 | 8 | 5 | Expected optimal |
| 3 | 10 | 5 | Baseline |
| 4 | 12 | 5 | Extended |
| 5 | 15 | 5 | Extended |
| 6 | 20 | 5 | Maximum |
| 7 | 25 | 5 | Over-dwell check |

**Arduino modification:** Change `DWELL_MS` constant for each run, re-upload.

## 4.4 Procedure

```
PROCEDURE: VALVE TIMING
═══════════════════════════════════════════════════════════════════════════════

1. PREPARATION
   a. Set regulator to fixed pressure (from EXP-1 results)
   b. Connect Arduino to laptop via USB
   c. Open Arduino IDE with safety code
   d. Note starting tank pressure

2. FOR EACH DWELL SETTING:
   a. Modify DWELL_MS value in code
   b. Upload modified code (verify LED blink confirms upload)
   c. Disconnect USB
   d. Fire 5 shots, record velocities on chronograph
   e. Record tank pressure after 5 shots (for gas consumption)
   f. Reconnect USB for next modification

3. OSCILLOSCOPE MEASUREMENTS (Optional):
   a. Probe CH1: Solenoid drive signal (0-12V)
   b. Probe CH2: Trigger switch (0-5V)
   c. Measure actual dwell time vs programmed
   d. Measure solenoid response delay

═══════════════════════════════════════════════════════════════════════════════
```

## 4.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════════
EXP-2: VALVE TIMING — DATA SHEET
═══════════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________
Regulated pressure: ___ bar (from EXP-1)
Projectile mass: ___ g    Starting tank P: ___ bar

───────────────────────────────────────────────────────────────────────────
       | Dwell | Shot Velocities (m/s)      | Mean  | Tank P | dP per |
Run    | (ms)  |  1    2    3    4    5     | (m/s) | after  | 5 shots|
-------+-------+----------------------------+-------+--------+--------+
  1    |   5   |                            |       |        |        |
  2    |   8   |                            |       |        |        |
  3    |  10   |                            |       |        |        |
  4    |  12   |                            |       |        |        |
  5    |  15   |                            |       |        |        |
  6    |  20   |                            |       |        |        |
  7    |  25   |                            |       |        |        |

OSCILLOSCOPE (if available):
Programmed Dwell | Actual Dwell | Solenoid Delay | Notes
-----------------+--------------+----------------+-----
      5 ms       |              |                |
     10 ms       |              |                |
     15 ms       |              |                |

ANALYSIS:
  Optimal dwell (velocity plateau): _______ ms
  Gas efficiency peak: _______ ms
  Recommended VDC-100 dwell: _______ ms (add 20% margin)
═══════════════════════════════════════════════════════════════════════════════
```

## 4.6 Expected Results

```
EXPECTED VELOCITY VS DWELL CURVE
═══════════════════════════════════════════════════════════════════════════════

Velocity
(m/s)
   40 |                          *----*----*----*  (plateau)
      |                      *
   35 |                  *
      |              *
   30 |          *
      |      *
   25 |  *
      |
   20 +--+--+--+--+--+--+--+--+--+--+--+--+--+--
         5    8   10  12  15     20     25
                    Dwell Time (ms)

INTERPRETATION:
  Below 8ms:  Insufficient gas flow, low velocity
  8-12ms:     Steep increase, approaching optimal
  12-15ms:    Knee point, diminishing returns
  >15ms:      Plateau, wasting gas

OPTIMAL: Choose dwell just past knee point.
         Balance velocity vs gas efficiency.
         Add 20% margin for VDC-100 (larger volume to fill).

═══════════════════════════════════════════════════════════════════════════════
```

## 4.7 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| Clear knee point identified | Yes | Extend test range |
| Velocity plateau reached | Within 5% of max | Increase max dwell |
| Gas consumption linear | R^2 > 0.9 | Check for leaks |
| Solenoid response | <5ms delay | Replace solenoid |

---

# 5. EXP-3: SAFETY INTERLOCK VALIDATION

## 5.1 Objective

Verify the 3-level safety interlock prevents unintended discharge in ALL unsafe states and permits firing ONLY when all conditions are met.

**THIS EXPERIMENT MUST PASS 100% BEFORE ANY LIVE FIRING.**

## 5.2 Equipment

| Item | Specification | Qty |
|------|---------------|-----|
| VDC-33 prototype | Fully assembled | 1 |
| Multimeter | For continuity/voltage checks | 1 |
| Test jumper wires | For fault injection | 5 |
| Data recording sheet | Printed | 1 |
| Witness | Second person (mandatory) | 1 |

## 5.3 Test Phases

### Phase 1: Electrical Verification (No Pressure)

| Measurement | Expected | Actual | Pass? |
|-------------|----------|--------|-------|
| Battery voltage | 10.5-12.6V | | |
| Arduino 5V rail | 4.8-5.2V | | |
| Solenoid drive (when fired) | >10V | | |

### Phase 2: State Permutation Test (No Pressure)

All 8 combinations of ARM, SAFETY, TRIGGER:

| Test | ARM | SAFETY | TRIGGER | Expected | LED | Solenoid | Result |
|------|-----|--------|---------|----------|-----|----------|--------|
| S1 | OFF | SAFE | Released | NO FIRE | GREEN | No click | |
| S2 | OFF | SAFE | Pressed | NO FIRE | GREEN | No click | |
| S3 | OFF | FIRE | Released | NO FIRE | GREEN | No click | |
| S4 | OFF | FIRE | Pressed | NO FIRE | GREEN | No click | |
| S5 | ON | SAFE | Released | NO FIRE | GREEN | No click | |
| S6 | ON | SAFE | Pressed | NO FIRE | GREEN | No click | |
| S7 | ON | FIRE | Released | NO FIRE | RED | No click | |
| **S8** | **ON** | **FIRE** | **Pressed** | **FIRE** | **RED** | **Click** | |

### Phase 3: Failure Mode Test (No Pressure)

| Test | Failure Injected | Expected | Actual | Result |
|------|------------------|----------|--------|--------|
| F1 | Battery disconnected | NO FIRE, LED OFF | | |
| F2 | Low battery (<10V) | NO FIRE, warning buzzer | | |
| F3 | ARM switch stuck ON | NO FIRE if SAFE engaged | | |
| F4 | Solenoid wire disconnected | NO FIRE | | |
| F5 | Arduino reset during armed | NO FIRE (re-initializes safe) | | |

### Phase 4: Indication Test

| Test | State | Expected LED | Actual | Result |
|------|-------|--------------|--------|--------|
| I1 | Power OFF | OFF | | |
| I2 | Power ON, SAFE | GREEN | | |
| I3 | Power ON, ARMED | RED | | |
| I4 | Low battery | FLASH + buzzer | | |

### Phase 5: Live Fire Verification (50 bar, Foam Projectile)

| Test | State | Expected | Actual | Result |
|------|-------|----------|--------|--------|
| L1 | S8 (all ON) | FIRE | | |
| L2 | S8 (all ON) | FIRE | | |
| L3 | S8 (all ON) | FIRE | | |
| L4 | S6 (SAFE ON) | NO FIRE | | |
| L5 | S6 (SAFE ON) | NO FIRE | | |
| L6 | S6 (SAFE ON) | NO FIRE | | |

## 5.4 Procedure

```
PROCEDURE: SAFETY INTERLOCK VALIDATION
═══════════════════════════════════════════════════════════════════════════════

*** CRITICAL: Perform Phases 1-4 with DEPRESSURIZED system! ***

PHASE 1: ELECTRICAL VERIFICATION
1. Verify all wiring per schematic (prototype_design.md Section 6.3)
2. Power on system
3. Measure voltages at key points with multimeter
4. Record all readings

PHASE 2: STATE PERMUTATION (No pressure)
For each state S1-S8:
1. Set ARM switch to specified position
2. Set SAFETY switch to specified position
3. Observe LED indication (record color)
4. Pull trigger
5. Listen/feel for solenoid click
6. Record: CLICK or NO CLICK
Expected: Only S8 produces click

PHASE 3: FAILURE MODE (No pressure)
For each failure F1-F5:
1. Set system to ARMED state
2. Inject failure (disconnect wire, reduce voltage, etc.)
3. Pull trigger
4. Observe response — must be NO FIRE
5. Restore normal state before next test

PHASE 4: INDICATION
1. Cycle through each state
2. Verify LED color matches expected
3. Test low battery warning with voltage limiter

PHASE 5: LIVE FIRE (Only after Phases 1-4 pass 100%)
1. Pressurize to 50 bar (reduced pressure for safety)
2. Load foam-only projectile (no tennis ball)
3. Verify S8 fires correctly (3x)
4. Verify S6 blocks fire (3x)

═══════════════════════════════════════════════════════════════════════════════
```

## 5.5 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| State permutation | 8/8 pass | Debug logic, check wiring |
| Failure modes | 5/5 pass | Redesign fail-safe circuit |
| Indication | 4/4 pass | Check LED wiring/resistors |
| Live fire | 6/6 pass | Full system debug |
| **OVERALL** | **23/23 (100%)** | **DO NOT proceed until 100%** |

---

# 6. EXP-4: PROJECTILE STABILITY

## 6.1 Objective

Evaluate 3 fin configurations to select optimal design for VDC-100 projectile (VDC-P40E).

## 6.2 Test Setup

```
EXP-4 SETUP: STABILITY TEST
═══════════════════════════════════════════════════════════════════════════════

                              CAMERA POSITION
                                    |
                    +---------------+---------------+
                    |               |               |
    FIRING          |               v               |         BACKSTOP
    LINE            |         +----------+          |
      |             |         | HI-SPEED |          |             |
      |    2m       |   5m    |  CAMERA  |   3m     |    5m       |
      v             |         | (side)   |          |             v
  +-------+        |         +----------+          |        +---------+
  |VDC-33 |========*============================== *========|BACKSTOP |
  +-------+      Mark 1                          Mark 2    +---------+
                (2m)                             (7m)

CAMERA SETTINGS:
• Frame rate: 240 fps (or higher)
• Shutter: 1/1000s minimum
• Focus: Pre-set on flight path (2-7m)
• Lighting: Bright, even (outdoor daylight ideal)
• Markers: Visible at 2m intervals, white background optional

═══════════════════════════════════════════════════════════════════════════════
```

## 6.3 Test Configurations

| Config | Fin Set | BOM Part | Fins | Cant Angle | Expected Spin |
|--------|---------|----------|------|------------|---------------|
| A | P11 | PRJ-003 | 4 | 15 deg | High (~20 rps) |
| B | P12 | PRJ-004 | 4 | 10 deg | Medium (~12 rps) |
| C | P13 | PRJ-005 | 6 | 0 deg | None (drag only) |

**Fixed parameters:** Pressure from EXP-1 (expected ~70 bar), standard projectile mass

## 6.4 Procedure

```
PROCEDURE: PROJECTILE STABILITY
═══════════════════════════════════════════════════════════════════════════════

1. SETUP
   a. Position camera perpendicular to flight path at 5m distance
   b. Set camera to high-speed mode (240fps+)
   c. Mark distance intervals (2m, 4m, 6m) with visible markers
   d. Verify lighting adequate for 1/1000s shutter
   e. Test camera trigger synchronization

2. FOR EACH FIN CONFIGURATION (A, B, C):
   a. Assemble projectile with specified fins + nose weight + tennis ball
   b. Verify mass: record total mass
   c. Start camera recording
   d. Fire at standard pressure (from EXP-1)
   e. Stop recording
   f. Review footage immediately for obvious issues
   g. Repeat 4x per configuration (12 total shots)

3. VIDEO ANALYSIS (per shot):
   a. Count frames from muzzle exit to 5m mark
   b. Calculate velocity: V = distance / (frames / fps)
   c. Count visible rotations in flight
   d. Calculate spin rate: RPM = (rotations * fps * 60) / frames
   e. Score stability:
      STABLE (no wobble):           3 points
      SLIGHT WOBBLE (<10 deg):      2 points
      MODERATE WOBBLE (10-30 deg):  1 point
      TUMBLE (>30 deg or flip):     0 points

═══════════════════════════════════════════════════════════════════════════════
```

## 6.5 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════════
EXP-4: PROJECTILE STABILITY — DATA SHEET
═══════════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________
Camera: ____________  Frame rate: ___ fps  Shutter: _______
Pressure: ___ bar  Projectile base mass: ___ g

FIN SET A: 4-fin, 15 deg cant (P11)  Mass: ___ g
───────────────────────────────────────────────────────────────────────────
Shot |Frames|Velocity|Rotations| Spin  |Stability|Score|Notes
     |(5m)  | (m/s)  | (5m)    | (RPM) |         |     |
-----+------+--------+---------+-------+---------+-----+---------
  1  |      |        |         |       |         |     |
  2  |      |        |         |       |         |     |
  3  |      |        |         |       |         |     |
  4  |      |        |         |       |         |     |
-----+------+--------+---------+-------+---------+-----+---------
AVG  |      |        |         |       |         | /12 |

FIN SET B: 4-fin, 10 deg cant (P12)  Mass: ___ g
───────────────────────────────────────────────────────────────────────────
Shot |Frames|Velocity|Rotations| Spin  |Stability|Score|Notes
     |(5m)  | (m/s)  | (5m)    | (RPM) |         |     |
-----+------+--------+---------+-------+---------+-----+---------
  1  |      |        |         |       |         |     |
  2  |      |        |         |       |         |     |
  3  |      |        |         |       |         |     |
  4  |      |        |         |       |         |     |
-----+------+--------+---------+-------+---------+-----+---------
AVG  |      |        |         |       |         | /12 |

FIN SET C: 6-fin, 0 deg straight (P13)  Mass: ___ g
───────────────────────────────────────────────────────────────────────────
Shot |Frames|Velocity|Rotations| Spin  |Stability|Score|Notes
     |(5m)  | (m/s)  | (5m)    | (RPM) |         |     |
-----+------+--------+---------+-------+---------+-----+---------
  1  |      |        |         |       |         |     |
  2  |      |        |         |       |         |     |
  3  |      |        |         |       |         |     |
  4  |      |        |         |       |         |     |
-----+------+--------+---------+-------+---------+-----+---------
AVG  |      |        |         |       |         | /12 |

COMPARISON:
Fin Set | Avg Velocity | Avg Spin | Stability Score | Rank
--------+--------------+----------+-----------------+------
   A    |              |          |       /12       |
   B    |              |          |       /12       |
   C    |              |          |       /12       |

SELECTED FOR VDC-100: Fin Set _____
Rationale: ___________________________________________________

═══════════════════════════════════════════════════════════════════════════════
```

## 6.6 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| At least one config stable | Score >= 10/12 | Design new fin geometry |
| Spin rate achieved | 100-500 RPM | Adjust cant angle |
| No tumbling | 0 tumble events | Increase fin area |
| Consistent results | StdDev <20% | Check sabot fit, projectile assembly |

---

# 7. EXP-5: RECOIL CHARACTERIZATION

## 7.1 Objective

Measure recoil impulse to verify operator comfort and inform VDC-100 stock/pad design.

## 7.2 Test Setup (Scale Method)

```
EXP-5 SETUP: RECOIL MEASUREMENT
═══════════════════════════════════════════════════════════════════════════════

    +--------------------------------------------------+
    |           RIGID FRAME                             |
    |    (prevents lateral movement)                    |
    +------------------------+-------------------------+
                             |
    +------------------------+-------------------------+
    |   VDC-33 (secured to plate)                      |
    +------------------------+-------------------------+
                             |
                    +--------+--------+
                    |  MOUNTING PLATE |
                    | (transmits force)|
                    +--------+--------+
                             |
                    +--------+--------+
                    |  DIGITAL SCALE  |
                    |  (peak hold)    |
                    +--------+--------+
                             |
                    +--------+--------+
                    |   RIGID BASE    |
                    +-----------------+

    Measurement: Peak force (kg) x 9.81 = Peak force (N)
    Impulse = 0.5 x F_peak x t_duration (triangular pulse approx.)

═══════════════════════════════════════════════════════════════════════════════
```

## 7.3 Test Matrix

| Series | Pressure (bar) | Shots | Purpose |
|--------|----------------|-------|---------|
| 1 | 60 | 5 | Low end |
| 2 | 80 | 5 | Standard |
| 3 | 100 | 5 | Maximum |

## 7.4 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════════
EXP-5: RECOIL CHARACTERIZATION — DATA SHEET
═══════════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________
System mass (VDC-33 + mount): ___ kg    Projectile mass: ___ g

SERIES 1: Pressure = 60 bar
Shot | Peak Force (kg) | Peak Force (N) | Duration (ms) | Impulse (Ns)
-----+-----------------+----------------+---------------+-------------
  1  |                 |                |               |
  2  |                 |                |               |
  3  |                 |                |               |
  4  |                 |                |               |
  5  |                 |                |               |
AVG  |                 |                |               |

SERIES 2: Pressure = 80 bar
Shot | Peak Force (kg) | Peak Force (N) | Duration (ms) | Impulse (Ns)
-----+-----------------+----------------+---------------+-------------
  1  |                 |                |               |
  2  |                 |                |               |
  3  |                 |                |               |
  4  |                 |                |               |
  5  |                 |                |               |
AVG  |                 |                |               |

SERIES 3: Pressure = 100 bar
Shot | Peak Force (kg) | Peak Force (N) | Duration (ms) | Impulse (Ns)
-----+-----------------+----------------+---------------+-------------
  1  |                 |                |               |
  2  |                 |                |               |
  3  |                 |                |               |
  4  |                 |                |               |
  5  |                 |                |               |
AVG  |                 |                |               |

SCALING TO VDC-100:
VDC-33 measured impulse (100 bar): _______ Ns
Mass ratio (450g / 58g): 7.76x
Predicted VDC-100 impulse: J_33 x 7.76 = _______ Ns
VDC-100 requirement: <= 15 Ns
Margin: _______ Ns (_______ %)

[ ] PASS: Predicted impulse <= 15 Ns
[ ] FAIL: Redesign recoil mitigation needed

═══════════════════════════════════════════════════════════════════════════════
```

## 7.5 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| VDC-33 impulse measured | <2.5 Ns @ 100 bar | Check momentum calc |
| Scaled VDC-100 prediction | <15 Ns | Add recoil buffer to stock |
| Consistent measurements | StdDev <15% | Improve fixture rigidity |

---

# 8. EXP-6: GAS CONSUMPTION

## 8.1 Objective

Measure gas consumption per shot to validate cylinder sizing for VDC-100 (5+ shots per fill).

## 8.2 Procedure

```
PROCEDURE: GAS CONSUMPTION
═══════════════════════════════════════════════════════════════════════════════

1. SETUP
   a. Fill HPA tank to known pressure (record exact value)
   b. Install digital pressure gauge on tank (TST-003)
   c. Set regulator to test pressure (from EXP-1)
   d. Allow system to stabilize (2 minutes)

2. MEASUREMENT
   a. Record starting tank pressure: P_start
   b. Fire 10 shots at consistent pace (10 sec intervals)
   c. Allow pressure to stabilize (30 sec)
   d. Record ending tank pressure: P_end
   e. Calculate: dP = P_start - P_end
   f. Gas per shot: dP / 10 shots

3. REPEAT FOR DIFFERENT DWELL TIMES
   a. Test with dwell = 8ms, 12ms, 15ms (from EXP-2 results)
   b. Compare gas consumption per shot
   c. Calculate efficiency score: velocity / gas_per_shot

═══════════════════════════════════════════════════════════════════════════════
```

## 8.3 Data Recording Sheet

```
═══════════════════════════════════════════════════════════════════════════════
EXP-6: GAS CONSUMPTION — DATA SHEET
═══════════════════════════════════════════════════════════════════════════════

Date: ____________  Operator: ____________
Tank volume: ___ L (0.8L for 48ci)    Regulated P: ___ bar

TEST 1: Dwell = 8 ms
  Starting tank P: ___ bar    Shots: 10    Ending tank P: ___ bar
  dP: ___ bar    Gas per shot: ___ bar/shot

TEST 2: Dwell = 12 ms
  Starting tank P: ___ bar    Shots: 10    Ending tank P: ___ bar
  dP: ___ bar    Gas per shot: ___ bar/shot

TEST 3: Dwell = 15 ms
  Starting tank P: ___ bar    Shots: 10    Ending tank P: ___ bar
  dP: ___ bar    Gas per shot: ___ bar/shot

COMPARISON:
Dwell (ms) | Gas/shot (bar) | Velocity (from EXP-2) | Efficiency (V/gas)
-----------+----------------+-----------------------+-------------------
     8     |                |                       |
    12     |                |                       |
    15     |                |                       |

Best efficiency: Dwell = _______ ms

SHOTS PER FILL (VDC-33):
  Tank: 0.8L, Full: 200 bar, Min usable: 80 bar
  Usable range: 120 bar
  Gas per shot (optimal): ___ bar
  Shots per fill: 120 / ___ = ___ shots

SCALING TO VDC-100:
  VDC-100 tank: 0.5L @ 300 bar, Min: 120 bar, Usable: 180 bar
  Bore area ratio: (100/32)^2 = 9.77x
  Expected gas per shot: VDC-33 x 9.77 = ___ bar
  VDC-100 shots per fill: 180 / ___ = ___ shots

  Requirement: >= 5 shots per fill
  [ ] PASS    [ ] FAIL

═══════════════════════════════════════════════════════════════════════════════
```

## 8.4 Success Criteria

| Criterion | Target | Action if Failed |
|-----------|--------|------------------|
| VDC-33 shots per fill | >= 30 | Check for leaks |
| Scaled VDC-100 shots | >= 5 | Increase tank size or reduce dwell |
| Efficiency improves with shorter dwell | Yes | Expected behavior |

---

# 9. POST-TEST ANALYSIS PLAN

## 9.1 Data Compilation

After all 6 experiments, compile results into a single test report:

| Experiment | Key Result | VDC-100 Implication | Design Change? |
|------------|-----------|---------------------|----------------|
| EXP-1 | V = ___ m/s @ ___ bar | Operating pressure: ___ bar | |
| EXP-2 | Optimal dwell: ___ ms | Solenoid spec: ___ ms | |
| EXP-3 | ___/23 pass | Safety architecture: ___ | |
| EXP-4 | Best fin: Set ___ | Projectile fin design: ___ | |
| EXP-5 | Recoil: ___ Ns (VDC-100: ___ Ns) | Stock/pad design: ___ | |
| EXP-6 | Shots/fill: ___ (VDC-100: ___) | Cylinder sizing: ___ | |

## 9.2 Scale-Up Decision Matrix

| Parameter | VDC-33 Measured | Scale Factor | VDC-100 Predicted | Requirement | Pass? |
|-----------|-----------------|--------------|-------------------|-------------|-------|
| Muzzle velocity | ___ m/s | ~1.0x | ___ m/s | 35-45 m/s | |
| Operating pressure | ___ bar | 1.0x | ___ bar | 100 bar max | |
| Shots per fill | ___ shots | /3 (approx) | ___ shots | >= 5 | |
| Recoil impulse | ___ Ns | x7.8 | ___ Ns | <= 15 Ns | |
| Valve dwell time | ___ ms | ~1.5x | ___ ms | TBD | |

## 9.3 Lessons Learned Template

After testing, document:
1. What worked as expected?
2. What surprised us?
3. What would we do differently?
4. What design changes are needed for VDC-100?
5. What risks were retired by prototype testing?

---

# 10. DOCUMENT LINKS

## Phase 4 Documents
- [[04_detail/prototype_design|Prototype Design Specifications]]
- [[04_detail/prototype_BOM_procurement|BOM & Procurement]]
- [[04_detail/scale_up_production|Scale-Up & Production Design]]
- [[04_detail/gate_review|Gate 4A/4B Review]]

## Phase 3 Reference
- [[03_embodiment/DECS_detail_evaluation|Phase 3: DfX & Requirements]]

---

# 11. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **2.0** | **2026-02-08** | **Restructured from monolithic experiments file. Added dependency map, test sequence optimization, post-test analysis plan, scale-up decision matrix. All 6 experiments with complete protocols and data sheets.** |
| 1.0 | 2026-02-05 | Initial experiment procedures. |

---

*These procedures support rapid learning and risk reduction before full-scale VDC-100 commitment.*

**After testing:** [[04_detail/scale_up_production|Scale-Up & Production Design]] → [[04_detail/gate_review|Gate Review]]
