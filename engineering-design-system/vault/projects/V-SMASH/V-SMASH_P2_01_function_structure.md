---
project: V-SMASH
phase: 2
type: function_structure
version: 1.3
created: 2026-01-18
updated: 2026-02-04
status: revised
---

# V-SMASH FUNCTION STRUCTURE
## Phase 2: Conceptual Design - Function Decomposition

**Prerequisite**: [[V-SMASH_P1_01_requirements_list|Requirements List]] complete ✓

---

## 1. OVERALL FUNCTION STATEMENT

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         V-SMASH FIRE CONTROL SYSTEM                      │
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

**Legend**:
- **E** = Energy flow
- **M** = Material flow
- **S** = Signal/Information flow

---

## 2. E-M-S FLOW ANALYSIS

### 2.1 Energy Flows

| Flow ID | Energy Type | Source | Destination | Transformation |
|---------|-------------|--------|-------------|----------------|
| E1 | Electrical | Battery | Power Management | Regulate voltage |
| E2 | Electrical | Power Mgmt | Processor | Computation |
| E3 | Electrical | Power Mgmt | Sensor | Image capture |
| E4 | Light | Scene | Sensor | Photoelectric conversion |
| E5 | Electrical | Power Mgmt | Display | Information display |
| E6 | Light | Display | Operator Eye | Visual feedback |
| E7 | Mechanical | Operator finger | Trigger sensor | Intent detection |
| E8 | Electrical | Fire Logic | Trigger gate | Actuation control |

### 2.2 Material Flows

| Flow ID | Material Type | Source | Destination | Transformation |
|---------|---------------|--------|-------------|----------------|
| M1 | Heat | Processor | Housing | Thermal dissipation |
| M2 | Heat | Display | Housing | Thermal dissipation |
| M3 | Air (target) | Environment | Field of View | Detection subject |

### 2.3 Signal Flows

| Flow ID | Signal Type | Source | Destination | Transformation |
|---------|-------------|--------|-------------|----------------|
| S1 | Image data | Sensor | Processor | Digitize scene |
| S2 | Detection result | AI Engine | Tracker | Target coordinates |
| S3 | Track state | Tracker | Predictor | Motion vector |
| S4 | Predicted position | Predictor | Ballistic Comp | Future target location |
| S5 | Weapon parameters | Memory | Ballistic Comp | Caliber, velocity |
| S6 | Fire solution | Ballistic Comp | Decision Logic | Alignment error |
| S7 | Trigger state | Trigger Sensor | Decision Logic | Operator intent |
| S8 | Fire authorization | Decision Logic | Trigger Gate | Release/hold |
| S9 | Status info | Processor | Display | Operator feedback |
| S10 | Video stream | Sensor | Recorder | Evidence storage |
| **S11** | **Track pool** | **Multi-Target Mgr** | **Priority Logic** | **All active tracks** | ← NEW
| **S12** | **Threat scores** | **Priority Logic** | **Target Selector** | **Ranked target list** | ← NEW
| **S13** | **Primary target ID** | **Target Selector** | **Predictor** | **Engage this target** | ← NEW
| **S14** | **Target data packet** | **Track Mgr** | **C4I Interface** | **Share externally (PRO)** | ← NEW
| **S15** | **Thermal image** | **Thermal Sensor** | **Fusion Module** | **LWIR frame (PRO)** | ← NEW v1.2 (R62)
| **S16** | **Fused image** | **Fusion Module** | **AI Detection** | **Enhanced scene (PRO)** | ← NEW v1.2 (R70)
| **S17** | **Drone classification** | **C-UAS AI** | **Classifier** | **Drone subtype** | ← NEW v1.2 (R68)
| | | | | | |
| | | **── RCWS/RCWS-LITE SIGNAL FLOWS (v1.3) ──** | | | |
| **S18** | **Pan command** | **Control Logic** | **Pan Motor** | **Azimuth position cmd** | ← NEW v1.3 (R93, R95)
| **S19** | **Tilt command** | **Control Logic** | **Tilt Motor** | **Elevation position cmd** | ← NEW v1.3 (R94)
| **S20** | **Position feedback** | **Encoders** | **Control Logic** | **Current orientation** | ← NEW v1.3 (R93)
| **S21** | **Remote video** | **Sensor** | **Datalink** | **H.264 stream** | ← NEW v1.3 (R97)
| **S22** | **Operator command** | **RCU** | **Control Logic** | **Joystick/trigger input** | ← NEW v1.3 (R97)
| **S23** | **External cue** | **Radar/C2** | **Track Mgr** | **Target handoff** | ← NEW v1.3 (R98, R113)
| | | | | | |
| | | **── DOME SYSTEM SIGNAL FLOWS (v1.3) ──** | | | |
| **S24** | **Detection alert** | **Detection Layer** | **Track Mgr** | **New contact** | ← NEW v1.3 (R108, R109)
| **S25** | **Classified track** | **Track Mgr** | **Threat Evaluator** | **UAS confirmed** | ← NEW v1.3 (R112)
| **S26** | **Engagement auth** | **Operator** | **Fire Coordinator** | **PITL confirm** | ← NEW v1.3 (R111)
| **S27** | **Effector command** | **Fire Coordinator** | **RCWS** | **Engage target X** | ← NEW v1.3 (R108)
| **S28** | **BDA report** | **RCWS** | **C2 Interface** | **Kill assessment** | ← NEW v1.3 (R114)
| **S29** | **CoT message** | **C2 Interface** | **ATAK/Network** | **Situational data** | ← NEW v1.3 (R114)

**Critical Flows** (bolded flows trace main function):
- **S1 → S2 → S11 → S12 → S13 → S3 → S4 → S6 → S8** (Multi-target-to-Fire decision chain)
- **S7 → S8** (Human-in-the-loop enforcement)
- **S11 → S14** (Target sharing - PRO variant)
- **S1 + S15 → S16 → S2** (Sensor fusion chain - PRO) ← NEW v1.2
- **S22 → S18/S19 → S20** (RCWS position control loop) ← NEW v1.3
- **S24 → S25 → S26 → S27 → S28** (DOME detect-to-kill chain) ← NEW v1.3

---

## 3. FUNCTION STRUCTURE HIERARCHY

```
V-SMASH OVERALL FUNCTION
│
├── F1: ACQUIRE TARGET INFORMATION (Sensor Fusion Enhanced v1.2)
│   ├── F1.1: Capture scene image ──────────── WP: CMOS Sensor
│   ├── F1.1T: Capture thermal image (PRO) ─── WP: LWIR Microbolometer  ← NEW (R62)
│   ├── **F1.5: Fuse sensor data (PRO)** ───── WP: Weighted Blend       ← NEW (R70)
│   ├── F1.2: Detect targets in scene ──────── WP: CNN/YOLO Detection
│   ├── **F1.6: Apply C-UAS AI model** ──────── WP: Drone-Optimized CNN  ← NEW (R68)
│   ├── F1.3: Classify target type ─────────── WP: Neural Classifier
│   └── F1.4: Measure target range ─────────── WP: Stereo/LRF + Passive (R69)
│
├── F2: TRACK TARGET MOTION (Multi-Target Enhanced v1.1)
│   ├── F2.1: Initialize track ─────────────── WP: Detection-to-Track
│   ├── F2.2: Update track state ───────────── WP: Kalman/IMM Filter
│   ├── F2.3: Predict future position ──────── WP: Motion Extrapolation
│   ├── F2.4: Handle track loss ────────────── WP: Re-acquisition Logic
│   ├── **F2.5: Manage multiple tracks** ───── WP: Track Pool Manager  ← NEW (R65)
│   ├── **F2.6: Associate detections** ──────── WP: Hungarian/GNN      ← NEW (R65)
│   └── **F2.7: Prioritize targets** ────────── WP: Threat Scoring     ← NEW (R66)
│
├── **F7: COORDINATE MULTI-TARGET ENGAGEMENT** ← NEW FUNCTION (R65-R67)
│   ├── F7.1: Select primary target ──────────── WP: Priority Queue
│   ├── F7.2: Queue secondary targets ─────────── WP: Engagement Scheduler
│   ├── F7.3: Enable rapid target switch ──────── WP: State Preservation
│   └── F7.4: Share target data (PRO) ─────────── WP: Tactical Data Link  ← (R67)
│
├── F3: COMPUTE FIRE SOLUTION
│   ├── F3.1: Sense weapon orientation ─────── WP: MEMS IMU
│   ├── F3.2: Retrieve weapon profile ──────── WP: Database Lookup
│   ├── F3.3: Calculate trajectory ─────────── WP: Point-Mass Model
│   └── F3.4: Determine alignment error ────── WP: Vector Comparison
│
├── F4: CONTROL FIRE AUTHORIZATION
│   ├── F4.1: Sense trigger pressure ───────── WP: Force Sensor
│   ├── F4.2: Evaluate hit probability ─────── WP: Threshold Logic
│   ├── F4.3: Authorize/gate fire ──────────── WP: Boolean Decision
│   └── F4.4: Time trigger release ─────────── WP: Precision Timing
│
├── F5: ACTUATE TRIGGER MECHANISM
│   ├── F5.1: Hold trigger (gate closed) ───── WP: Solenoid/Servo
│   ├── F5.2: Release trigger (gate open) ──── WP: Electromechanical
│   └── F5.3: Confirm fire event ───────────── WP: Acoustic/Recoil Sense
│
├── F6: PROVIDE OPERATOR FEEDBACK
│   ├── F6.1: Display aim point ────────────── WP: See-through Optic
│   ├── F6.2: Show target lock status ──────── WP: LED/Reticle Symbol
│   ├── F6.3: Indicate fire readiness ──────── WP: Color/Audio Cue
│   └── F6.4: Display system status ────────── WP: LCD/OLED Screen
│
├── F_AUX: AUXILIARY FUNCTIONS
│   ├── F_AUX.1: Manage power ──────────────── WP: PMIC + Battery
│   ├── F_AUX.2: Record engagement ─────────── WP: SD Card Storage
│   ├── F_AUX.3: Configure weapon profile ──── WP: USB/App Interface
│   ├── F_AUX.4: Update software ───────────── WP: OTA/USB Flash
│   └── F_AUX.5: Provide fail-safe ─────────── WP: Mechanical Bypass
│
├── **F8: RCWS PLATFORM CONTROL (RCWS/RCWS-LITE)** ← NEW v1.3 (R92-R107)
│   ├── F8.1: Control pan axis ────────────── WP: Servo Motor + Encoder
│   ├── F8.2: Control tilt axis ───────────── WP: Servo Motor + Encoder
│   ├── F8.3: Stabilize weapon ────────────── WP: Gyro-Stabilized Gimbal
│   ├── F8.4: Stream video remotely ───────── WP: H.264 Encoder + Datalink
│   ├── F8.5: Receive operator commands ───── WP: Wired/Wireless RCU
│   ├── F8.6: Accept external cue ─────────── WP: Radar/C2 Interface
│   ├── F8.7: Execute auto-scan ───────────── WP: Sector Scan Logic
│   └── F8.8: Provide portable deployment ─── WP: Folding Tripod (RCWS-LITE)
│
└── **F9: INTEGRATED C-UAS SYSTEM (DOME)** ← NEW v1.3 (R108-R115)
    ├── F9.1: Detect airspace threats ─────── WP: EO/IR Scanner + Radar
    ├── F9.2: Classify UAS targets ────────── WP: AI Classifier (Drone vs Bird)
    ├── F9.3: Manage multiple tracks ──────── WP: Track Fusion Manager
    ├── F9.4: Prioritize threats ──────────── WP: Threat Scoring Algorithm
    ├── F9.5: Coordinate with operator ────── WP: PITL Interface
    ├── F9.6: Command effector engagement ─── WP: RCWS Fire Coordinator
    ├── F9.7: Assess battle damage ────────── WP: Post-Engagement BDA
    └── F9.8: Network with C2/ATAK ────────── WP: CoT Protocol Stack
```

**WP** = Working Principle (initial candidate, to be evaluated in morphological matrix)

---

## 4. SUBFUNCTION DECOMPOSITION TABLE

| ID | Subfunction | Type | Input | Output | Classification |
|----|-------------|------|-------|--------|----------------|
| **F1: ACQUIRE TARGET INFORMATION (Sensor Fusion Enhanced v1.2)** | | | | | |
| F1.1 | Capture scene image | E→S | Light | Digital image | SENSE |
| **F1.1T** | **Capture thermal image (PRO)** | **E→S** | **IR radiation** | **Thermal frame** | **SENSE** |
| **F1.5** | **Fuse sensor data (PRO)** | **S→S** | **CMOS + thermal** | **Fused image** | **PROCESS** |
| F1.2 | Detect targets | S→S | Image/fused | Bounding boxes | PROCESS |
| **F1.6** | **Apply C-UAS AI model** | **S→S** | **Detections** | **Drone classifications** | **PROCESS** |
| F1.3 | Classify targets | S→S | Detection | Class labels | PROCESS |
| F1.4 | Measure range | E→S | Light + size | Distance value | SENSE |
| **F2: TRACK TARGET MOTION (Multi-Target)** | | | | | |
| F2.1 | Initialize track | S→S | Detection | Track ID | PROCESS |
| F2.2 | Update track | S→S | Detection + state | Updated state | PROCESS |
| F2.3 | Predict position | S→S | Track state | Future coords | PROCESS |
| F2.4 | Handle track loss | S→S | Track quality | Re-acquire/drop | DECIDE |
| **F2.5** | **Manage multiple tracks** | **S→S** | **All detections** | **Track pool (≤5)** | **PROCESS** |
| **F2.6** | **Associate detections** | **S→S** | **Detections + tracks** | **Matched pairs** | **PROCESS** |
| **F2.7** | **Prioritize targets** | **S→S** | **Track pool** | **Ranked list** | **DECIDE** |
| **F3: COMPUTE FIRE SOLUTION** | | | | | |
| F3.1 | Sense orientation | E→S | Angular motion | Aim vector | SENSE |
| F3.2 | Retrieve weapon profile | S→S | Weapon ID | Ballistic params | PROCESS |
| F3.3 | Calculate trajectory | S→S | Params + range | Impact point | PROCESS |
| F3.4 | Determine alignment | S→S | Aim + impact | Error angle | PROCESS |
| **F4: CONTROL FIRE AUTHORIZATION** | | | | | |
| F4.1 | Sense trigger | E→S | Force | Pressure value | SENSE |
| F4.2 | Evaluate probability | S→S | Error + threshold | Probability | PROCESS |
| F4.3 | Authorize fire | S→S | Probability + trigger | Yes/No | DECIDE |
| F4.4 | Time release | S→E | Authorization | Timing signal | PROCESS |
| **F5: ACTUATE TRIGGER MECHANISM** | | | | | |
| F5.1 | Hold trigger | E | Electrical | Mechanical hold | ACTUATE |
| F5.2 | Release trigger | E | Electrical | Mechanical release | ACTUATE |
| F5.3 | Confirm fire | E→S | Recoil/sound | Fire confirmation | SENSE |
| **F6: PROVIDE OPERATOR FEEDBACK** | | | | | |
| F6.1 | Display aim | S→E | Aim data | Light pattern | CONVERT |
| F6.2 | Show lock status | S→E | Track state | Visual indicator | CONVERT |
| F6.3 | Indicate readiness | S→E | Fire solution | Color/sound | CONVERT |
| F6.4 | Display status | S→E | System state | Text/symbols | CONVERT |
| **F7: COORDINATE MULTI-TARGET ENGAGEMENT** | | | | | |
| **F7.1** | **Select primary target** | **S→S** | **Ranked list** | **Primary ID** | **DECIDE** |
| **F7.2** | **Queue secondary targets** | **S→S** | **Remaining tracks** | **Engagement queue** | **PROCESS** |
| **F7.3** | **Enable rapid switch** | **S→S** | **Switch command** | **New primary** | **PROCESS** |
| **F7.4** | **Share target data (PRO)** | **S→S** | **Track data** | **C4I packet** | **CONVERT** |
| | | | | | |
| **F8: RCWS PLATFORM CONTROL (v1.3)** | | | | | |
| **F8.1** | **Control pan axis** | **S→E** | **Pan command** | **Azimuth motion** | **ACTUATE** |
| **F8.2** | **Control tilt axis** | **S→E** | **Tilt command** | **Elevation motion** | **ACTUATE** |
| **F8.3** | **Stabilize weapon** | **E→S→E** | **Gyro data** | **Compensation motion** | **PROCESS** |
| **F8.4** | **Stream video remotely** | **S→S** | **Video frames** | **Compressed stream** | **CONVERT** |
| **F8.5** | **Receive operator commands** | **S→S** | **RCU input** | **Control commands** | **SENSE** |
| **F8.6** | **Accept external cue** | **S→S** | **Radar/C2 data** | **Target handoff** | **PROCESS** |
| **F8.7** | **Execute auto-scan** | **S→S** | **Scan pattern** | **Sector coverage** | **PROCESS** |
| **F8.8** | **Provide portable deployment** | **M→M** | **Packed system** | **Deployed system** | **CONVERT** |
| | | | | | |
| **F9: INTEGRATED C-UAS SYSTEM (v1.3)** | | | | | |
| **F9.1** | **Detect airspace threats** | **E→S** | **Optical/RF energy** | **Contact reports** | **SENSE** |
| **F9.2** | **Classify UAS targets** | **S→S** | **Detections** | **UAS classification** | **PROCESS** |
| **F9.3** | **Manage multiple tracks** | **S→S** | **All contacts** | **Fused track picture** | **PROCESS** |
| **F9.4** | **Prioritize threats** | **S→S** | **Track data** | **Threat ranking** | **DECIDE** |
| **F9.5** | **Coordinate with operator** | **S→S** | **Threat + video** | **Engagement auth** | **DECIDE** |
| **F9.6** | **Command effector engagement** | **S→S** | **Auth + target** | **Fire command** | **PROCESS** |
| **F9.7** | **Assess battle damage** | **S→S** | **Post-fire video** | **Kill assessment** | **PROCESS** |
| **F9.8** | **Network with C2/ATAK** | **S→S** | **Local data** | **CoT messages** | **CONVERT** |

**Classification Legend**:
- **SENSE**: Physical phenomenon → Signal
- **PROCESS**: Signal transformation/computation
- **DECIDE**: Logic/rule-based decision making
- **ACTUATE**: Signal → Physical action
- **CONVERT**: Signal representation change

---

## 5. CRITICAL SUBFUNCTIONS (Must-Work List)

These subfunctions are **CRITICAL** - failure of any one results in mission failure:

| ID | Subfunction | Criticality Reason | Fallback |
|----|-------------|-------------------|----------|
| F1.1 | Capture scene image | No image = blind system | Manual optic |
| F1.2 | Detect targets | No detection = no engagement | Manual optic |
| F2.2 | Update track | Poor tracking = miss | Operator re-aim |
| **F2.5** | **Manage multiple tracks** | **Swarm overwhelm** | **Single-target mode** |
| **F2.6** | **Associate detections** | **Track swap = wrong target** | **Nearest-neighbor fallback** |
| F3.3 | Calculate trajectory | Wrong ballistics = miss | Manual lead estimation |
| F4.1 | Sense trigger | No trigger sense = no fire | Direct mechanical linkage |
| F4.3 | Authorize fire | Safety-critical function | **No fallback - must work** |
| F5.2 | Release trigger | Can't fire when commanded | Direct mechanical linkage |
| **F7.1** | **Select primary target** | **Engage wrong target** | **Operator manual select** |
| F_AUX.5 | Provide fail-safe | System failure resilience | **Must always work** |
| | | | |
| **F8: RCWS PLATFORM CONTROL** | | | |
| **F8.1** | **Control pan axis** | **Can't aim weapon** | **Manual traverse** |
| **F8.2** | **Control tilt axis** | **Can't elevate weapon** | **Manual elevation** |
| **F8.5** | **Receive operator commands** | **No control = useless** | **Wired backup** |
| **F8.8** | **Provide portable deployment** | **Can't setup = no use** | **Pre-configured** |
| | | | |
| **F9: INTEGRATED C-UAS SYSTEM** | | | |
| **F9.1** | **Detect airspace threats** | **Blind to threats** | **External radar cue** |
| **F9.5** | **Coordinate with operator** | **No PITL = unsafe** | **Must always work** |
| **F9.6** | **Command effector engagement** | **Can't engage** | **Manual RCWS control** |

**Design Implication**: Critical functions require:
- Redundancy analysis
- FMEA (Failure Modes and Effects Analysis)
- Robust working principles
- Testing emphasis

---

## 6. FUNCTION-TO-REQUIREMENT TRACEABILITY

| Function | Traces to Requirements |
|----------|----------------------|
| F1 | R01, R02, R03, R06, R58, R59, R61, R62, R68, R69, R70 (Detection, false positive, HDR, thermal, C-UAS AI, passive ranging, fusion) |
| F2 | R03, R04, R60, R65 (Tracking speed, latency, evasive maneuvers, multi-target) |
| F3 | R04, R24 (Fire solution speed, weapon compatibility) |
| F4 | R05, R31, R34 (Timing precision, safety) |
| F5 | R05, R32 (Timing, fail-safe) |
| F6 | R33, R36, R37, R38 (Feedback, ergonomics) |
| F7 | R65, R66, R67 (Multi-target, prioritization, C4I) |
| **F8** | **R92-R107** (RCWS weight, slew, elevation, azimuth, connectivity, setup, battery) ← **NEW v1.3** |
| **F9** | **R108-R115** (C-UAS detect-track-engage, PITL, multi-track, radar cue, CoT, cost) ← **NEW v1.3** |
| F_AUX | R21, R22, R27, R29, R32, R48, R62, R63, R64 (Power, interface, fail-safe, thermal, lens) |

**Coverage Check**: All Demands (D requirements) are covered by at least one function. ✓

### New Requirements Coverage (v1.1 + v1.2)

| Requirement | Function | Subfunction |
|-------------|----------|-------------|
| R58 (False positive) | F1 | F1.2, F1.3, F1.6 |
| R59 (Varying light) | F1 | F1.1, F1.5 |
| R60 (Evasive maneuvers) | F2 | F2.2, F2.3 |
| R61 (HDR) | F1 | F1.1 |
| R62 (Thermal) | F1, F_AUX | F1.1T, F_AUX.1 |
| R63 (Anti-fog) | F_AUX | F_AUX.1 |
| R64 (Lens protection) | F_AUX | F_AUX.1 |
| **R65 (Multi-target)** | **F2, F7** | **F2.5, F2.6, F7.1-F7.3** |
| **R66 (Prioritization)** | **F2, F7** | **F2.7, F7.1** |
| **R67 (C4I link)** | **F7** | **F7.4** |
| **R68 (C-UAS AI)** | **F1** | **F1.2, F1.6** | ← v1.2 (ARBEL RE)
| **R69 (Passive ranging)** | **F1** | **F1.4** | ← v1.2 (ARBEL RE)
| **R70 (Sensor fusion)** | **F1** | **F1.1T, F1.5** | ← v1.2 (ARBEL RE)
| | | | |
| **── RCWS Requirements (v1.3) ──** | | | |
| **R92 (RCWS weight ≤15kg)** | **F8** | **F8.1-F8.8** | ← Hopper 5000 RE |
| **R93 (Slew 0.1-40°/sec)** | **F8** | **F8.1, F8.2** | ← Hopper 5000 RE |
| **R94 (Elevation -30° to +70°)** | **F8** | **F8.2** | ← Hopper 5000 RE |
| **R95 (Azimuth 360°)** | **F8** | **F8.1** | ← Hopper 5000 RE |
| **R96 (Acceleration ≥100°/sec²)** | **F8** | **F8.1, F8.2** | ← Hopper 5000 RE |
| **R97 (Dual connectivity)** | **F8** | **F8.4, F8.5** | ← Hopper 5000 RE |
| **R98 (External cue)** | **F8** | **F8.6** | ← Hopper 5000 RE |
| **R99 (Temp -10° to +55°C)** | **F_AUX** | **F_AUX.1** | ← Hopper 5000 RE |
| | | | |
| **── RCWS-LITE Requirements (v1.3) ──** | | | |
| **R100 (Weight ≤10kg)** | **F8** | **F8.1-F8.8** | ← Hopper Light RE |
| **R101 (Single-soldier op)** | **F8** | **F8.5, F8.8** | ← Hopper Light RE |
| **R102 (Setup <3 min)** | **F8** | **F8.8** | ← Hopper Light RE |
| **R103 (Backpack portable)** | **F8** | **F8.8** | ← Hopper Light RE |
| **R104 (Slew ≥25°/sec)** | **F8** | **F8.1, F8.2** | ← Hopper Light RE |
| **R105 (Elevation -20° to +60°)** | **F8** | **F8.2** | ← Hopper Light RE |
| **R106 (Battery ≥2hr)** | **F_AUX** | **F_AUX.1** | ← Hopper Light RE |
| **R107 (Low profile)** | **F8** | **F8.8** | ← Hopper Light RE |
| | | | |
| **── DOME C-UAS Requirements (v1.3) ──** | | | |
| **R108 (Detect-track-engage)** | **F9** | **F9.1-F9.7** | ← SMASH DOME RE |
| **R109 (Detection ≥1km)** | **F9** | **F9.1** | ← SMASH DOME RE |
| **R110 (Detect-to-kill ≤15s)** | **F9** | **F9.1-F9.6** | ← SMASH DOME RE |
| **R111 (Person-in-loop)** | **F9** | **F9.5** | ← SMASH DOME RE |
| **R112 (Track ≥3 targets)** | **F9** | **F9.3, F9.4** | ← SMASH DOME RE |
| **R113 (Radar cue interface)** | **F9, F8** | **F9.1, F8.6** | ← SMASH DOME RE |
| **R114 (ATAK/CoT integration)** | **F9** | **F9.8** | ← SMASH DOME RE |
| **R115 (Cost/engagement ≤$10)** | **F9** | **F9.6** | ← SMASH DOME RE |

---

## 7. NEXT STEPS

Function structure complete (v1.3 with RCWS + DOME functions). Ready for:

1. **Morphological Matrix** → Update with F8/F9 working principles
2. **Concept Evaluation** → Add RCWS and DOME evaluation criteria
3. **Product Portfolio** → ✅ Updated to v3.0 (9 products)
4. **Phase 3** → Begin preliminary layout design (LITE first, then RCWS-LITE)
5. **RCWS Prototype** → Pan-tilt mechanism testing
6. **DOME Architecture** → Define sensor-effector integration

---

## 8. PRODUCT-FUNCTION MAPPING

| Product | Functions Used |
|---------|----------------|
| **LITE** | F1-F6, F_AUX (core FCS) |
| **PRO** | F1-F7, F_AUX (+ multi-target, C4I) |
| **PRO-X** | F1-F7, F_AUX (+ LRF, enhanced ballistics) |
| **HMG** | F1-F7, F_AUX (+ 12.7mm ballistics) |
| **MARITIME** | F1-F7, F_AUX (+ stabilization, IP68) |
| **RCWS-LITE** | F1-F8, F_AUX (+ portable RCWS control) |
| **RCWS** | F1-F8, F_AUX (+ full 360° RCWS control) |
| **DOME** | F1-F9, F_AUX (+ integrated C-UAS system) |
| **C4I HUB** | F7.4, F9.8 (network coordination) |

---

## 9. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-18 | Initial function structure (F1-F6, F_AUX) |
| 1.1 | 2026-02-04 | Multi-target tracking: Added F2.5-F2.7 (track management, association, prioritization), new F7 (multi-target coordination), updated signal flows S11-S14, updated traceability for R65-R67 from ARCAS RE analysis |
| 1.2 | 2026-02-04 | Sensor fusion: Added F1.1T (thermal capture), F1.5 (sensor fusion), F1.6 (C-UAS AI); added signal flows S15-S17; updated traceability for R68-R70 from ARBEL RE analysis |
| **1.3** | **2026-02-04** | **RCWS + DOME functions: Added F8 (RCWS Platform Control) with F8.1-F8.8; added F9 (Integrated C-UAS System) with F9.1-F9.8; added signal flows S18-S29; updated traceability for R92-R115 from Hopper 5000, Hopper Light, SMASH DOME RE analyses. Added product-function mapping.** |

---

*Prev: [[V-SMASH_P1_01_requirements_list|Requirements List v1.5]]*
*Next: [[V-SMASH_P2_02_morphological_matrix|Morphological Matrix v1.2]]*
*Back to: [[V-SMASH_00_project_brief|Project Brief]]*

**RE Sources:**
- Handheld: [[V-SMASH_RE_02_ARCAS_analysis|ARCAS]] | [[V-SMASH_RE_04_SMASH3000_analysis|SMASH 3000]]
- Platform: [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|Hopper 5000]] | [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light]]
- System: [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME]]
