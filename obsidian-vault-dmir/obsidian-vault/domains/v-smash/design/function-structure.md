# V-SMASH Function Structure

> **Document Type**: Conceptual Design - Function Decomposition
> **Version**: 1.1
> **Reference**: Pahl & Beitz Systematic Design Methodology

---

## 1. Overall Function Statement

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     V-SMASH FIRE CONTROL SYSTEM                          │
│                                                                          │
│  INPUT                                               OUTPUT              │
│  ─────                                               ──────              │
│  • Visual scene (E: light)                →  • Weapon fires at optimal  │
│  • Operator trigger intent (S: pressure)  →    moment (E: kinetic)      │
│  • Target motion in FOV (M: air/ground)   →  • Target neutralized       │
│  • Electrical power (E: battery)          →  • Engagement record (S)    │
│                                                                          │
│  OVERALL FUNCTION:                                                       │
│  "Optimize weapon fire timing to maximize hit probability on            │
│   moving targets while maintaining human decision authority"            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. E-M-S Flow Analysis

### Energy Flows (E)

| Flow ID | Energy Type | Source | Destination | Transformation |
|---------|-------------|--------|-------------|----------------|
| E1 | Light | Scene | Image sensor | Photoelectric conversion |
| E2 | Electrical | Battery | All subsystems | Power distribution |
| E3 | Mechanical | Operator | Trigger sensor | Force sensing |
| E4 | Electrical | Controller | Solenoid | Trigger actuation |
| E5 | Thermal | Processing | Environment | Heat dissipation |

### Material Flows (M)

| Flow ID | Material | Source | Destination | Notes |
|---------|----------|--------|-------------|-------|
| M1 | Projectile | Magazine | Target | Via weapon (external) |
| M2 | Air (target) | Environment | Tracking zone | Drone/bird discrimination |

### Signal Flows (S)

| Flow ID | Signal Type | Source | Destination | Purpose |
|---------|-------------|--------|-------------|---------|
| S1 | Image data | Sensor | Processor | Target detection input |
| S2 | Detection result | AI module | Tracker | Bounding boxes, class |
| S3 | Track state | Tracker | Ballistic computer | Position, velocity |
| S4 | Fire solution | Ballistic | Gate logic | Alignment error |
| S5 | Trigger pressure | Force sensor | Gate logic | Human intent |
| S6 | Gate command | Logic | Solenoid driver | Fire authorization |
| S7 | Status | All modules | Display | Operator feedback |
| S8 | Configuration | USB interface | Memory | Weapon profiles |

---

## 3. Function Hierarchy

```
F0: OPTIMIZE FIRE TIMING FOR MOVING TARGETS
│
├── F1: ACQUIRE TARGET
│   ├── F1.1: Capture scene image ─────────── WP: CMOS Sensor
│   ├── F1.2: Detect targets ──────────────── WP: YOLO-nano
│   ├── F1.3: Classify targets ────────────── WP: CNN Classifier
│   └── F1.4: Measure range ───────────────── WP: Passive Estimation
│
├── F2: TRACK TARGET
│   ├── F2.1: Initialize track ────────────── WP: Detection Association
│   ├── F2.2: Update track state ──────────── WP: Kalman Filter
│   ├── F2.3: Predict future position ─────── WP: CV Kalman Prediction
│   └── F2.4: Handle track loss ───────────── WP: Re-acquisition Logic
│
├── F3: COMPUTE FIRE SOLUTION
│   ├── F3.1: Sense weapon orientation ────── WP: 6-axis IMU
│   ├── F3.2: Retrieve weapon profile ─────── WP: Database Lookup
│   ├── F3.3: Calculate trajectory ────────── WP: Point-Mass 3DOF
│   └── F3.4: Determine alignment error ───── WP: Vector Comparison
│
├── F4: CONTROL FIRE AUTHORIZATION
│   ├── F4.1: Sense trigger pressure ──────── WP: Force Sensor
│   ├── F4.2: Evaluate hit probability ────── WP: Threshold Logic
│   ├── F4.3: Authorize/gate fire ─────────── WP: Boolean Decision
│   └── F4.4: Time trigger release ────────── WP: Precision Timing
│
├── F5: ACTUATE TRIGGER MECHANISM
│   ├── F5.1: Hold trigger (gate closed) ──── WP: Solenoid Hold
│   ├── F5.2: Release trigger (gate open) ─── WP: Solenoid Release
│   └── F5.3: Confirm fire event ──────────── WP: Acoustic/Recoil Sense
│
├── F6: PROVIDE OPERATOR FEEDBACK
│   ├── F6.1: Display aim point ───────────── WP: See-through Optic
│   ├── F6.2: Show target lock status ─────── WP: LED/Reticle Symbol
│   ├── F6.3: Indicate fire readiness ─────── WP: LED + Audio
│   └── F6.4: Display system status ───────── WP: OLED Screen
│
└── F_AUX: AUXILIARY FUNCTIONS
    ├── F_AUX.1: Manage power ─────────────── WP: PMIC + Battery
    ├── F_AUX.2: Record engagement ────────── WP: SD Card Storage
    ├── F_AUX.3: Configure weapon profile ─── WP: USB Interface
    ├── F_AUX.4: Update software ──────────── WP: USB Flash
    └── F_AUX.5: Provide fail-safe ────────── WP: Mechanical Bypass
```

---

## 4. Subfunction Decomposition Table

| ID | Subfunction | Type | Input | Output | Classification |
|----|-------------|------|-------|--------|----------------|
| F1.1 | Capture scene image | E→S | Light | Digital image | SENSE |
| F1.2 | Detect targets | S→S | Image | Bounding boxes | PROCESS |
| F1.3 | Classify targets | S→S | Detection | Class labels | PROCESS |
| F1.4 | Measure range | E→S | Light | Distance value | SENSE |
| F2.1 | Initialize track | S→S | Detection | Track ID | PROCESS |
| F2.2 | Update track | S→S | Detection + state | Updated state | PROCESS |
| F2.3 | Predict position | S→S | Track state | Future coords | PROCESS |
| F2.4 | Handle track loss | S→S | Track quality | Re-acquire/drop | DECIDE |
| F3.1 | Sense orientation | E→S | Angular motion | Aim vector | SENSE |
| F3.2 | Retrieve weapon profile | S→S | Weapon ID | Ballistic params | PROCESS |
| F3.3 | Calculate trajectory | S→S | Params + range | Impact point | PROCESS |
| F3.4 | Determine alignment | S→S | Aim + impact | Error angle | PROCESS |
| F4.1 | Sense trigger | E→S | Force | Pressure value | SENSE |
| F4.2 | Evaluate probability | S→S | Error + threshold | Probability | PROCESS |
| F4.3 | Authorize fire | S→S | Probability + trigger | Yes/No | DECIDE |
| F4.4 | Time release | S→E | Authorization | Timing signal | PROCESS |
| F5.1 | Hold trigger | E | Electrical | Mechanical hold | ACTUATE |
| F5.2 | Release trigger | E | Electrical | Mechanical release | ACTUATE |
| F5.3 | Confirm fire | E→S | Recoil/sound | Fire confirmation | SENSE |
| F6.1 | Display aim | S→E | Aim data | Light pattern | CONVERT |
| F6.2 | Show lock status | S→E | Track state | Visual indicator | CONVERT |
| F6.3 | Indicate readiness | S→E | Fire solution | Color/sound | CONVERT |
| F6.4 | Display status | S→E | System state | Text/symbols | CONVERT |

---

## 5. Critical Function Chains

### Chain 1: Target Acquisition → Fire (Primary)

```
F1.1 → F1.2 → F2.1 → F2.2 → F2.3 → F3.3 → F3.4 → F4.2 → F4.3 → F5.2
 │      │      │      │      │      │      │      │      │      │
 ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼      ▼
Image  Detect  Init   Update Predict Traj  Error  Prob   Auth   Fire
                Track  Track  Pos    Calc  Calc   Eval   Gate   !

TOTAL LATENCY BUDGET: <100ms
├── F1.1-F1.2: <30ms (detection)
├── F2.2-F2.3: <10ms (tracking)
├── F3.3-F3.4: <5ms (ballistics)
└── F4.2-F5.2: <5ms (authorization)
```

### Chain 2: Human-in-the-Loop Safety

```
F4.1 (Sense trigger) ──► F4.3 (Authorize) ──► F5.2 (Release)
        │                      │
        └──── MUST HAVE ───────┘
        
Human MUST press trigger first → System optimizes TIMING only
```

### Chain 3: Fail-Safe Path

```
IF (System failure detected):
    F_AUX.5 (Fail-safe) → Weapon operates NORMALLY (manual mode)
    
NO DEPENDENCY on electronics for basic weapon function
```

---

## 6. Solution-Neutral Verification

| Function | Solution-Neutral? | Check |
|----------|-------------------|-------|
| F1.2 Detect targets | ✅ | "Detect" not "use YOLO" |
| F2.2 Update track | ✅ | "Update" not "use Kalman" |
| F3.3 Calculate trajectory | ✅ | "Calculate" not "use point-mass" |
| F5.1 Hold trigger | ⚠️ | Consider "Block fire" as alternative |
| F6.1 Display aim | ✅ | "Display" not "project reticle" |

---

## 7. Related Documents

- [[requirements/v1.1-summary]] - Source requirements for functions
- [[design/morphological-matrix]] - Working principle options
- [[design/working-principles]] - Selected WP details
- [[decisions/log]] - Why these functions were chosen

---

*Document follows Pahl & Beitz Function Structure methodology*
*Last updated: 2026-01-26*
