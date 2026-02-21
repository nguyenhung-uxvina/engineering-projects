---
project: V-SMASH
phase: 2
type: morphological_matrix
version: 1.3
created: 2026-01-18
updated: 2026-02-04
status: revised
---

# V-SMASH MORPHOLOGICAL MATRIX
## Phase 2: Conceptual Design - Working Principle Selection

**Prerequisite**: [[V-SMASH_P2_01_function_structure|Function Structure]] complete ✓

---

## 1. MORPHOLOGICAL MATRIX OVERVIEW

### Complete Matrix Table

| Subfunction | Option A | Option B | Option C | Option D |
|-------------|----------|----------|----------|----------|
| **F1.1 Image Capture** | CCD sensor | **CMOS sensor** ✓ | Thermal (LWIR) | — |
| **F1.2 Target Detection** | Template matching | Classical CV (HOG+SVM) | **Deep Learning (YOLO)** ✓ | — |
| **F1.3 Classification** | Rule-based | Random Forest | **Lightweight CNN** ✓ | — |
| **F1.4 Range Finding** | **Passive (size estimate)** ✓L | Laser Rangefinder | Stereo vision | — |
| **F1.5 Sensor Fusion** | **None (single sensor)** ✓L | **Weighted blend** ✓P | Decision-level | Deep fusion |
| **F1.6 AI Training Data** | **Generic objects** | **C-UAS optimized** ✓ | Transfer learning | Synthetic + real |
| **F2.2 Tracking** | Centroid tracking | **Kalman Filter** ✓ | Deep SORT | IMM Filter |
| **F2.3 Prediction** | Linear extrapolation | Polynomial fit | **CV Kalman** ✓ | — |
| **F2.5 Multi-Track Mgmt** | **Fixed pool (5)** ✓L | Dynamic pool (∞) | Priority-limited | — |
| **F2.6 Data Association** | **Nearest-Neighbor** ✓L | Hungarian Algorithm | GNN | JPDA |
| **F2.7 Threat Priority** | Manual only | **Distance-based** ✓L | **Multi-factor AI** ✓P | Learning-based |
| **F3.1 Orientation Sense** | Gyroscope only | **Gyro + Accel (6-axis)** ✓ | Full IMU (9-axis) | — |
| **F3.3 Ballistics** | Lookup table | **Point-mass 3DOF** ✓ | 6DOF model | — |
| **F4.1 Trigger Sense** | Limit switch | **Force sensor** ✓ | Optical gate | — |
| **F5.1/5.2 Trigger Gate** | Mechanical block | **Solenoid** ✓ | Servo motor | — |
| **F6.1 Aim Display** | Projected reticle | LCD overlay | **See-through optic** ✓ | — |
| **F6.3 Fire Indicator** | LED only | Audio only | **LED + Audio** ✓ | — |
| **F7.1 Target Selection** | **Operator only** ✓L | Auto (highest threat) | **Auto + Override** ✓P | — |
| **F7.2 Engagement Queue** | **None (single)** ✓L | FIFO queue | **Priority queue** ✓P | — |
| **F7.3 Rapid Switch** | Re-acquire | **State preserve** ✓ | Predictive handoff | — |
| **F7.4 Target Sharing** | **None** ✓L | Serial export | **C4I protocol** ✓P | Mesh network |
| **F_AUX.1 Power** | AA batteries | **Rechargeable Li-ion** ✓ | External power | — |
| **F_AUX.2 Recording** | Internal memory | **SD card** ✓ | Cloud upload | — |
| **F_AUX.5 Fail-safe** | Manual bypass switch | Auto-detect failure | **Auto + Manual** ✓ | — |
| | | | | |
| **F8: RCWS PLATFORM CONTROL (NEW v1.3)** | | | | |
| **F8.1 Pan Axis Control** | Stepper motor | **Brushless DC servo** ✓ | Direct drive | — |
| **F8.2 Tilt Axis Control** | Stepper motor | **Brushless DC servo** ✓ | Linear actuator | — |
| **F8.3 Stabilization** | **Passive (friction)** ✓L | **Gyro-stabilized 2-axis** ✓R | Inertially stabilized | — |
| **F8.4 Video Streaming** | Analog NTSC | **H.264 IP stream** ✓ | H.265 low-latency | — |
| **F8.5 Operator Interface** | **Wired RCU only** ✓L | **Wired + Wireless** ✓R | Tablet/smartphone | — |
| **F8.6 External Cueing** | **None** ✓L | Serial (RS-422) | **Ethernet/CoT** ✓R | — |
| **F8.7 Auto-Scan Mode** | **None (manual)** ✓L | **Sector scan** ✓R | Spiral search | Track-while-scan |
| **F8.8 Deployment** | **Fixed mount** ✓R | **Folding tripod** ✓L | Quick-release | Backpack integrated |
| | | | | |
| **F9: INTEGRATED C-UAS SYSTEM (NEW v1.3)** | | | | |
| **F9.1 Detection Sensor** | **EO/IR only** ✓B | EO/IR + Acoustic | **EO/IR + Radar** ✓S | Multi-layer |
| **F9.2 UAS Classification** | Rule-based (size) | **CNN classifier** ✓ | Multi-sensor fusion | Behavioral analysis |
| **F9.3 Track Management** | **Single sensor tracks** ✓B | **Sensor fusion** ✓S | Distributed fusion | — |
| **F9.4 Threat Prioritization** | **Distance only** ✓B | **Multi-factor** ✓S | AI/ML adaptive | — |
| **F9.5 PITL Interface** | Audio alert only | **Video + overlay** ✓ | AR headset | — |
| **F9.6 Fire Coordination** | **Manual command** ✓B | **Semi-auto (confirm)** ✓S | Auto-engage (future) | — |
| **F9.7 BDA Assessment** | **Operator visual** ✓B | **AI track loss** ✓S | Kill confirmation AI | — |
| **F9.8 C2 Networking** | **Standalone** ✓B | Serial export | **CoT/ATAK** ✓S | Link-16 gateway |

**✓** = Selected for baseline | **✓L** = LITE variant | **✓P** = PRO variant
**✓R** = RCWS variant | **✓L** = RCWS-LITE variant | **✓B** = DOME Basic | **✓S** = DOME Standard

---

## 2. CONCEPT VARIANT PATHS

### 2.1 Visual Concept Path Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        MORPHOLOGICAL MATRIX - CONCEPT PATHS                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  SUBFUNCTION        │ Option A        │ Option B        │ Option C              │
│  ═══════════════════╪═════════════════╪═════════════════╪═════════════════════  │
│  F1.1 Image Capture │ CCD ────────────│ CMOS ───────────│ Thermal              │
│                     │   │             │   │      │      │     │                 │
│  F1.2 Detection     │ Template ───────│ HOG+SVM ────────│ YOLO-nano            │
│                     │   │             │   │      │      │     │                 │
│  F1.3 Classify      │ Rule-based ─────│ Random Forest ──│ CNN                  │
│                     │   │             │   │      │      │     │                 │
│  F2.2 Tracking      │ Centroid ───────│ Kalman ─────────│ Deep SORT            │
│                     │   │             │   │      │      │     │                 │
│  F3.3 Ballistics    │ Table ──────────│ Point-mass ─────│ 6DOF                 │
│                     │   │             │   │      │      │     │                 │
│  F5.1 Trigger Gate  │ Mech block ─────│ Solenoid ───────│ E-trigger            │
│                     │   │             │   │             │     │                 │
│                     │   ▼             │   ▼             │     ▼                 │
│                     │                 │                 │                       │
│  CONCEPT PATHS:     │                 │                 │                       │
│                     │                 │                 │                       │
│  V1 (CLONE)        ═══A═══════════════A═══════════════A═════════════════       │
│  • All Option A    │ CCD→Template→Rule→Centroid→Table→Mech                     │
│  • Foreign replica │ Minimum tech risk, maximum foreign dependency             │
│                                                                                  │
│  V2 (LOCAL-FIRST)  ═══B═══════════════B═══════════════B═════════════════       │
│  • All Option B    │ CMOS→HOG+SVM→RF→Kalman→PM→Solenoid                        │
│  • Maximum local   │ Proven tech, local capability match                        │
│                                                                                  │
│  V3 (HYBRID)       ═══B═══════════════C═══════════════B═════════════════       │
│  • Mix B + C       │ CMOS→YOLO→CNN→Kalman→PM→Solenoid                          │
│  • Balanced        │ AI capability with local production                        │
│                                                                                  │
│  V4 (PHASED)       ═══B═══════════════B→C═════════════B═════════════════       │
│  • Start B, evolve │ CMOS→(HOG→YOLO)→(RF→CNN)→Kalman→PM→Solenoid              │
│  • SELECTED ✓      │ Risk-managed evolution, learning integration              │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

Legend: ═══ Connection path    → Evolution path    ✓ Selected concept
```

### 2.2 Concept Variant Descriptions

#### Concept V1: Direct Clone
**Strategy**: Replicate SMASH system as closely as possible

| Aspect | Specification |
|--------|--------------|
| **Approach** | All Option A - Foreign technology |
| **Pros** | Proven capability, minimum technical risk |
| **Cons** | Maximum import dependency, IP restrictions, high cost |
| **Local Content** | ~15% (assembly only) |
| **Development Risk** | Low (copy existing) |
| **Production Cost** | High (import components) |

#### Concept V2: Local-First
**Strategy**: Maximize local content and proven technology

| Aspect | Specification |
|--------|--------------|
| **Approach** | All Option B - Mature technology |
| **Pros** | High local content, proven algorithms, sustainable |
| **Cons** | Lower performance than AI, less competitive |
| **Local Content** | ~75% |
| **Development Risk** | Low-Medium (standard tech) |
| **Production Cost** | Low (local sourcing) |

#### Concept V3: Hybrid Optimal
**Strategy**: Best-of-breed selection for each subfunction

| Aspect | Specification |
|--------|--------------|
| **Approach** | Mix B+C - AI where beneficial, proven elsewhere |
| **Pros** | Good performance, balanced local content |
| **Cons** | Complex integration, higher NRE |
| **Local Content** | ~65% |
| **Development Risk** | Medium (AI integration) |
| **Production Cost** | Medium |

#### Concept V4: Phased Development ✓ **SELECTED**
**Strategy**: Start simple, evolve to AI capability

| Aspect | Specification |
|--------|--------------|
| **Approach** | B→C - Evolution path with learning |
| **Pros** | Risk mitigation, progressive capability growth, builds local expertise |
| **Cons** | Longer timeline to full capability |
| **Local Content** | Phase 1: 70%, Phase 2: 65% |
| **Development Risk** | Low-Medium (staged approach) |
| **Production Cost** | Medium (optimized over time) |

**Phase 1 (Months 1-12)**: CMOS + HOG/SVM + Kalman → Prove basic concept
**Phase 2 (Months 13-24)**: Upgrade to YOLO + CNN → Add AI capability

---

## 3. WORKING PRINCIPLE DETAILS

### WP-VSMASH-001: CMOS Image Capture

```yaml
id: "WP-VSMASH-001"
subfunction: "F1.1 - Capture scene image"
physical_effect: "Photoelectric effect in silicon"
form_design: "Rolling shutter CMOS sensor with ISP"

specification:
  resolution: "1920x1080 (Full HD)"
  frame_rate: "60 fps"
  dynamic_range: "65 dB"
  low_light: "0.1 lux with gain"
  interface: "MIPI CSI-2"

local_sourcing:
  option_1:
    part: "Sony IMX290"
    supplier: "Available via distributors"
    cost: "~$25 USD"
  option_2:
    part: "OmniVision OV2718"
    supplier: "China distributors"
    cost: "~$15 USD"

integration_notes:
  - "Standard industrial camera module form factor"
  - "Requires lens selection for FOV"
  - "ISP handles exposure, white balance"
```

### WP-VSMASH-002: YOLO-Nano Object Detection

```yaml
id: "WP-VSMASH-002"
subfunction: "F1.2 - Detect targets"
physical_effect: "CNN pattern matching"
form_design: "YOLOv8-nano optimized for edge deployment"

specification:
  model: "YOLOv8n (custom trained)"
  inference_time: "<30ms on target hardware"
  mAP: ">0.7 on custom dataset"
  classes: ["drone", "person", "vehicle", "aircraft"]
  input_size: "640x640"

training_requirements:
  dataset_size: "5000+ labeled images"
  compute: "GPU cluster (can rent cloud)"
  training_time: "~24 hours"
  validation: "Vietnam-specific test set"

local_capability:
  training: "Partner with university (HUST, VNU)"
  inference: "NVIDIA Jetson Nano/Xavier NX"
  expertise: "Growing AI community in Vietnam"

edge_optimization:
  quantization: "INT8 via TensorRT"
  pruning: "Remove unused classes"
  compilation: "ONNX → TensorRT engine"
```

### WP-VSMASH-003: Kalman Filter Tracking

```yaml
id: "WP-VSMASH-003"
subfunction: "F2.2 - Update track state"
physical_effect: "Recursive state estimation"
form_design: "Extended Kalman Filter (EKF)"

specification:
  state_vector: "[x, y, vx, vy, ax, ay]" # 6D state
  measurement: "[x, y]" # Detection centroid
  update_rate: "60 Hz (match sensor)"
  prediction_horizon: "100ms"

parameters:
  process_noise_Q:
    position: "1.0 px²"
    velocity: "5.0 px²/frame²"
    acceleration: "10.0 px²/frame⁴"
  measurement_noise_R:
    position: "4.0 px²" # Detection jitter

implementation:
  language: "C++ with Eigen library"
  complexity: "O(n³) per update (n=6)"
  memory: "<1 KB per track"

local_capability:
  algorithm: "Well-documented, textbook implementations"
  expertise: "Standard control theory"
  library: "OpenCV cv::KalmanFilter available"
```

### WP-VSMASH-004: Point-Mass Ballistic Model

```yaml
id: "WP-VSMASH-004"
subfunction: "F3.3 - Calculate trajectory"
physical_effect: "Newtonian mechanics + atmospheric drag"
form_design: "3DOF point-mass with drag coefficient"

equations:
  drag_force: "F_d = 0.5 * ρ * v² * C_d * A"
  gravity: "F_g = m * g"
  motion: "m * a = F_d + F_g + crosswind"

parameters:
  air_density: "Function of altitude, temperature"
  drag_model: "G1 or G7 ballistic coefficient"
  muzzle_velocity: "Per weapon profile"

weapon_profiles_supported:
  - caliber: "5.56x45mm NATO"
    bc_g7: "0.151"
    muzzle_velocity: "940 m/s"
  - caliber: "7.62x39mm"
    bc_g7: "0.115"
    muzzle_velocity: "715 m/s"
  - caliber: "7.62x54mmR"
    bc_g7: "0.180"
    muzzle_velocity: "830 m/s"
  - caliber: "12.7x108mm"
    bc_g7: "0.620"
    muzzle_velocity: "850 m/s"

implementation:
  method: "4th order Runge-Kutta integration"
  step_size: "1ms"
  range: "Up to 1000m"
  computation_time: "<1ms"

local_capability:
  algorithm: "Standard physics, well-documented"
  validation: "Requires range testing data"
  expertise: "Weapons institute capability"
```

### WP-VSMASH-005: Solenoid Trigger Gate

```yaml
id: "WP-VSMASH-005"
subfunction: "F5.1/F5.2 - Hold/Release trigger"
physical_effect: "Electromagnetic actuation"
form_design: "Push-type solenoid with return spring"

specification:
  response_time: "<5ms"
  holding_force: "20N minimum"
  stroke: "5-10mm"
  voltage: "12V DC"
  current: "500mA peak, 200mA hold"

mechanism_options:
  option_A:
    name: "Trigger blocking"
    description: "Solenoid blocks trigger linkage"
    pros: "Simple, retrofit to any weapon"
    cons: "Mechanical complexity"
  option_B:
    name: "Electronic trigger interrupt"
    description: "Electronic gate in trigger circuit"
    pros: "Clean integration for e-triggers"
    cons: "Requires electronic trigger (MTB-20 compatible)"

mtb20_integration:
  trigger_type: "Electronic (24V solenoid)"
  interface: "Parallel gate circuit"
  implementation: "FET switch in trigger line"
  advantage: "No mechanical modification needed"

local_sourcing:
  solenoid: "Available from China/domestic"
  driver: "MOSFET H-bridge, standard"
  cost: "~$5 USD per unit"
```

### WP-VSMASH-006: Multi-Track Pool Manager (NEW v1.1)

```yaml
id: "WP-VSMASH-006"
subfunction: "F2.5 - Manage multiple tracks"
physical_effect: "Data structure management"
form_design: "Fixed-size track pool with state machine"

specification:
  max_tracks: "5 simultaneous (R65)"
  track_states: ["tentative", "confirmed", "coasting", "deleted"]
  confirmation_threshold: "3 consecutive detections"
  coasting_timeout: "500ms (30 frames @ 60fps)"

options:
  option_A:
    name: "Fixed Pool (5)"
    description: "Pre-allocated array of 5 track slots"
    pros: "Deterministic memory, fast access, simple"
    cons: "Hard limit on targets"
    complexity: "O(1) access"
    memory: "~5 KB total"
    variant: "LITE ✓"
  option_B:
    name: "Dynamic Pool"
    description: "Linked list with dynamic allocation"
    pros: "Unlimited targets"
    cons: "Memory fragmentation, GC pauses"
    complexity: "O(n) search"
    memory: "Variable"
    variant: "Not recommended"
  option_C:
    name: "Priority-Limited"
    description: "Dynamic but drops low-priority when full"
    pros: "Adapts to threat density"
    cons: "More complex logic"
    complexity: "O(n log n)"
    memory: "Bounded"
    variant: "PRO option"

implementation:
  language: "C++ with fixed arrays"
  real_time: "No dynamic allocation in hot path"
  thread_safety: "Lock-free ring buffer"
```

### WP-VSMASH-007: Data Association Algorithm (NEW v1.1)

```yaml
id: "WP-VSMASH-007"
subfunction: "F2.6 - Associate detections to tracks"
physical_effect: "Optimal assignment problem"
form_design: "Cost matrix with assignment solver"

specification:
  input: "N detections, M tracks"
  output: "Matched pairs + unassigned"
  cost_function: "Mahalanobis distance"
  gating: "Chi-squared threshold (99.7%)"

options:
  option_A:
    name: "Nearest-Neighbor (NN)"
    description: "Greedy assignment to closest track"
    pros: "Very fast O(NM), simple"
    cons: "Suboptimal in clutter, track swap risk"
    complexity: "O(NM)"
    variant: "LITE ✓"
  option_B:
    name: "Hungarian Algorithm"
    description: "Global optimal assignment"
    pros: "Optimal solution, handles occlusion"
    cons: "O(n³) complexity"
    complexity: "O(n³)"
    variant: "PRO ✓"
  option_C:
    name: "Global Nearest Neighbor (GNN)"
    description: "Hungarian with gating"
    pros: "Optimal within gate"
    cons: "Still O(n³)"
    complexity: "O(n³)"
    variant: "PRO option"
  option_D:
    name: "JPDA"
    description: "Joint Probabilistic Data Association"
    pros: "Handles ambiguity probabilistically"
    cons: "Exponential in dense scenarios"
    complexity: "O(2^n)"
    variant: "Not recommended (too slow)"

implementation:
  lite: "Simple NN with distance threshold"
  pro: "Hungarian via scipy.optimize.linear_sum_assignment"
  real_time: "< 1ms for 5 tracks, 10 detections"
```

### WP-VSMASH-008: Threat Prioritization (NEW v1.1)

```yaml
id: "WP-VSMASH-008"
subfunction: "F2.7 - Prioritize targets by threat"
physical_effect: "Multi-criteria decision making"
form_design: "Weighted scoring function"

specification:
  output: "Ranked list of track IDs"
  update_rate: "Every frame (60 Hz)"
  factors: ["distance", "closing_speed", "heading", "type", "size"]

options:
  option_A:
    name: "Manual Only"
    description: "Operator selects target manually"
    pros: "Full human control"
    cons: "Slow, cognitive overload in swarm"
    variant: "Backup mode"
  option_B:
    name: "Distance-Based"
    description: "Closest target = highest priority"
    pros: "Simple, intuitive"
    cons: "Ignores threat trajectory"
    formula: "priority = 1 / distance"
    variant: "LITE ✓"
  option_C:
    name: "Multi-Factor Scoring"
    description: "Weighted combination of factors"
    pros: "Better threat assessment"
    cons: "Requires tuning"
    formula: "priority = w1/dist + w2*closing_speed + w3*heading_factor + w4*type_weight"
    weights:
      w1_distance: "0.4"
      w2_closing: "0.3"
      w3_heading: "0.2"
      w4_type: "0.1"
    variant: "PRO ✓"
  option_D:
    name: "Learning-Based"
    description: "ML model trained on engagement outcomes"
    pros: "Adapts to operational patterns"
    cons: "Requires training data, black box"
    variant: "Future (v2.0)"

implementation:
  lite: "Simple inverse distance"
  pro: "Configurable weight factors"
  tuning: "Field-adjustable via config file"
```

### WP-VSMASH-009: Target Selection Logic (NEW v1.1)

```yaml
id: "WP-VSMASH-009"
subfunction: "F7.1 - Select primary target"
physical_effect: "Decision logic"
form_design: "Priority queue with operator override"

specification:
  primary_target: "Single target for fire solution"
  secondary_targets: "Queued for rapid transition"
  override: "Operator can force-select any track"

options:
  option_A:
    name: "Operator Only"
    description: "Manual target designation required"
    pros: "Full control, no automation errors"
    cons: "Slow, cognitive load"
    variant: "LITE ✓ (with auto-suggest)"
  option_B:
    name: "Auto (Highest Threat)"
    description: "System selects highest priority"
    pros: "Fast response"
    cons: "May not match operator intent"
    variant: "Not standalone"
  option_C:
    name: "Auto + Override"
    description: "Auto-select with manual override"
    pros: "Best of both: speed + control"
    cons: "Slightly more complex"
    variant: "PRO ✓"

ui_feedback:
  primary: "Solid box around target"
  secondary: "Dashed box, numbered 2-5"
  override: "Button or gesture to select"
```

### WP-VSMASH-010: Engagement Queue (NEW v1.1)

```yaml
id: "WP-VSMASH-010"
subfunction: "F7.2 - Queue secondary targets"
physical_effect: "Queue data structure"
form_design: "Priority queue with engagement history"

options:
  option_A:
    name: "None (Single Target)"
    description: "Only one target tracked for engagement"
    pros: "Simplest, no queue logic"
    cons: "Must re-acquire after each engagement"
    variant: "LITE ✓"
  option_B:
    name: "FIFO Queue"
    description: "First-detected, first-engaged"
    pros: "Simple, predictable"
    cons: "Ignores threat priority"
    variant: "Not recommended"
  option_C:
    name: "Priority Queue"
    description: "Next target = next highest threat"
    pros: "Always engaging most dangerous"
    cons: "Queue order changes dynamically"
    variant: "PRO ✓"

rapid_transition:
  trigger: "Fire event detected or manual switch"
  action: "Pop next from queue, become primary"
  latency: "< 50ms to new fire solution"
```

### WP-VSMASH-011: Target Data Sharing (NEW v1.1)

```yaml
id: "WP-VSMASH-011"
subfunction: "F7.4 - Share target data externally"
physical_effect: "Data serialization + transmission"
form_design: "Tactical data link interface"

specification:
  data_packet:
    - track_id: "uint8"
    - position_lat_lon: "float64 x 2"
    - altitude: "float32"
    - velocity: "float32 x 3"
    - classification: "uint8"
    - confidence: "uint8"
    - timestamp: "uint64"
  packet_size: "~48 bytes per target"
  update_rate: "1-10 Hz configurable"

options:
  option_A:
    name: "None"
    description: "Standalone operation only"
    pros: "Simplest, no external dependencies"
    cons: "No force multiplication"
    variant: "LITE ✓"
  option_B:
    name: "Serial Export"
    description: "RS-232/422 ASCII output"
    pros: "Simple, universal"
    cons: "Point-to-point only"
    variant: "LITE option"
  option_C:
    name: "C4I Protocol"
    description: "Standard tactical data format (e.g., Link-16 simplified, CoT)"
    pros: "Interoperable, network-ready"
    cons: "Requires protocol stack"
    protocols:
      - "Cursor on Target (CoT) - XML over UDP"
      - "STANAG 4586 (simplified)"
      - "Custom JSON over TCP"
    variant: "PRO ✓"
  option_D:
    name: "Mesh Network"
    description: "Peer-to-peer target sharing"
    pros: "Resilient, distributed"
    cons: "Complex, latency"
    variant: "Future (v2.0)"

implementation:
  pro:
    interface: "Ethernet (RJ45) or WiFi"
    protocol: "CoT over UDP"
    encryption: "AES-256"
    integration: "TAK server compatible"
```

### WP-VSMASH-012: Sensor Fusion Algorithm (NEW v1.2 - ARBEL RE)

```yaml
id: "WP-VSMASH-012"
subfunction: "F1.5 - Fuse day and thermal imagery"
physical_effect: "Multi-spectral data combination"
form_design: "Pixel-level or feature-level fusion"

specification:
  input_day: "1920x1080 CMOS @ 60fps"
  input_thermal: "160x120 LWIR @ 9fps"
  output: "Fused detection stream"
  latency: "<20ms additional"

options:
  option_A:
    name: "None (Single Sensor)"
    description: "Day OR thermal, operator selected"
    pros: "Simplest, no fusion complexity"
    cons: "Reduced detection in mixed conditions"
    implementation: "Mode switch only"
    variant: "LITE ✓"
  option_B:
    name: "Weighted Blend"
    description: "Alpha-blend based on conditions"
    pros: "Smooth transition, proven technique"
    cons: "Requires tuning, may blur details"
    formula: "output = α*day + (1-α)*thermal_upscaled"
    alpha_control: "Auto (histogram) or manual"
    variant: "PRO ✓"
  option_C:
    name: "Decision-Level Fusion"
    description: "Run detection on both, merge results"
    pros: "Preserves detail from each sensor"
    cons: "Higher compute, association needed"
    implementation: "Dual YOLO + NMS merge"
    variant: "PRO option"
  option_D:
    name: "Deep Fusion"
    description: "Neural network learns optimal fusion"
    pros: "Best theoretical performance"
    cons: "Requires training data, complex"
    implementation: "Custom CNN fusion network"
    variant: "Future (v2.0)"

thermal_upscaling:
  method: "Bilinear interpolation"
  from: "160x120"
  to: "1920x1080 (or 640x480 ROI)"
  notes: "Thermal provides heat signature, not detail"

auto_mode_switching:
  conditions:
    day_only: "Ambient > 1000 lux"
    thermal_only: "Ambient < 10 lux"
    fusion: "10-1000 lux (dawn/dusk)"
  sensor: "Ambient light sensor or histogram analysis"

implementation:
  lite: "Manual mode switch (day/thermal)"
  pro: "Auto weighted blend with manual override"
  compute: "~5ms per frame (upscale + blend)"
```

### WP-VSMASH-013: C-UAS AI Training Data (NEW v1.2 - ARBEL RE)

```yaml
id: "WP-VSMASH-013"
subfunction: "F1.6 - AI model training for drone detection"
physical_effect: "Machine learning optimization"
form_design: "Domain-specific training dataset"

specification:
  requirement: "R68 - ≥5,000 drone images"
  classes: ["FPV_drone", "commercial_quad", "fixed_wing_uav", "loitering_munition", "bird", "background"]
  annotation: "Bounding box + class label"
  format: "YOLO format (txt + images)"

options:
  option_A:
    name: "Generic Objects"
    description: "Pre-trained COCO/ImageNet weights"
    pros: "Immediate availability, no collection"
    cons: "Poor drone-specific performance"
    expected_mAP: "~60% on drones"
    variant: "Not recommended"
  option_B:
    name: "C-UAS Optimized"
    description: "Custom dataset focused on drone threats"
    pros: "Best detection performance"
    cons: "Requires data collection effort"
    expected_mAP: "~85% on drones"
    variant: "Both ✓"
  option_C:
    name: "Transfer Learning"
    description: "Fine-tune generic model on small drone set"
    pros: "Faster than full training"
    cons: "Still needs 1,000+ drone images"
    expected_mAP: "~75% on drones"
    variant: "Initial development"
  option_D:
    name: "Synthetic + Real"
    description: "Mix real captures with rendered drones"
    pros: "Augment limited real data"
    cons: "Domain gap issues"
    mix_ratio: "70% real, 30% synthetic"
    variant: "Augmentation strategy"

data_collection_plan:
  sources:
    - "Field captures (Vietnam drone exercises)"
    - "Public datasets (Anti-UAV, DUT-UAV)"
    - "Partner contributions (military units)"
    - "Synthetic rendering (Blender/Unity)"
  targets:
    fpv_drone: "1,500 images"
    commercial_quad: "1,500 images"
    fixed_wing: "1,000 images"
    loitering_mun: "500 images"
    negatives: "1,000 images (birds, aircraft, clutter)"
  total: "5,500+ images"

training_infrastructure:
  compute: "Cloud GPU (AWS/GCP) or university cluster"
  framework: "Ultralytics YOLOv8"
  training_time: "~24-48 hours"
  validation: "20% holdout, Vietnam-specific test set"

implementation:
  phase_1: "Transfer learning on 1,000 images (Month 3)"
  phase_2: "Full C-UAS dataset training (Month 6)"
  ongoing: "Continuous improvement with field data"
```

### WP-VSMASH-014: RCWS Pan/Tilt Drive System (NEW v1.3 - Hopper RE)

```yaml
id: "WP-VSMASH-014"
subfunction: "F8.1/F8.2 - Control pan and tilt axes"
physical_effect: "Electromagnetic motor actuation"
form_design: "Brushless DC servo with absolute encoder"

specification:
  pan_range: "360° continuous (R93)"
  tilt_range: "-30° to +70° (R94)"
  slew_rate: "≥30°/sec (goal: 40°/sec) (R95)"
  positioning_accuracy: "±0.1° (≤1 mrad)"
  holding_torque: "Sufficient for 15kg payload"

options:
  option_A:
    name: "Stepper Motor"
    description: "Open-loop stepper with microstepping"
    pros: "Simple control, no encoder needed"
    cons: "Lower torque, can lose steps under load"
    cost: "Low (~$50/axis)"
    variant: "Not recommended for weapon"
  option_B:
    name: "Brushless DC Servo"
    description: "BLDC motor with absolute encoder feedback"
    pros: "High torque, smooth motion, precise"
    cons: "Higher cost, requires driver"
    cost: "Medium (~$200/axis)"
    variant: "RCWS ✓, RCWS-LITE ✓"
  option_C:
    name: "Direct Drive"
    description: "Torque motor without gearbox"
    pros: "Zero backlash, very smooth"
    cons: "Expensive, large size"
    cost: "High (~$800/axis)"
    variant: "Premium option"

motor_selection:
  rcws_full:
    motor: "Maxon EC-i 40 or equivalent"
    gearbox: "Harmonic drive (zero backlash)"
    encoder: "17-bit absolute"
  rcws_lite:
    motor: "Smaller BLDC (EC-max 22)"
    gearbox: "Planetary (acceptable backlash)"
    encoder: "14-bit absolute"

local_sourcing:
  motors: "Import (Maxon, Oriental Motor)"
  drivers: "Import or China equivalent"
  assembly: "Local integration"
  local_content: "30% (structure, wiring, assembly)"
```

### WP-VSMASH-015: Gyro-Stabilized Gimbal (NEW v1.3 - Hopper RE)

```yaml
id: "WP-VSMASH-015"
subfunction: "F8.3 - Stabilize weapon on moving platform"
physical_effect: "Inertial sensing + active compensation"
form_design: "2-axis gyro-stabilized gimbal"

specification:
  stabilization_axes: "2 (pan/tilt)"
  angular_rate_sensing: "MEMS gyroscope"
  stabilization_bandwidth: "≥10 Hz"
  residual_jitter: "<0.5 mrad RMS"
  base_motion_rejection: "Vehicle vibration, walking"

options:
  option_A:
    name: "Passive (Friction)"
    description: "Friction damping only, no active stabilization"
    pros: "Simplest, no electronics"
    cons: "Poor on moving platform"
    variant: "RCWS-LITE (static positions)"
  option_B:
    name: "Gyro-Stabilized 2-Axis"
    description: "Active rate gyro feedback to servo loop"
    pros: "Good stabilization, proven technology"
    cons: "Requires IMU, control complexity"
    implementation:
      sensor: "BMI088 or similar 6-axis IMU"
      bandwidth: "100 Hz control loop"
      algorithm: "PID with feedforward"
    variant: "RCWS ✓"
  option_C:
    name: "Inertially Stabilized"
    description: "Full INS with position hold"
    pros: "Best stabilization, geo-pointing"
    cons: "Expensive, complex"
    variant: "Future option"

control_algorithm:
  type: "Cascade PID"
  inner_loop: "Rate stabilization (gyro feedback)"
  outer_loop: "Position control (encoder feedback)"
  feedforward: "Base motion compensation"

local_capability:
  algorithm: "Standard control theory"
  imu: "Import (Bosch, STMicro)"
  integration: "Local capability"
```

### WP-VSMASH-016: Video Streaming System (NEW v1.3 - Hopper RE)

```yaml
id: "WP-VSMASH-016"
subfunction: "F8.4 - Stream video to remote operator"
physical_effect: "Digital video encoding and transmission"
form_design: "H.264 encoder with Ethernet/wireless link"

specification:
  resolution: "1080p (R97)"
  frame_rate: "30 fps minimum"
  latency: "<150ms end-to-end (R97)"
  bitrate: "2-10 Mbps adaptive"
  encryption: "AES-128 or better"

options:
  option_A:
    name: "Analog NTSC/PAL"
    description: "Traditional analog video link"
    pros: "Zero latency, simple"
    cons: "No encryption, limited range, interference"
    variant: "Legacy compatibility"
  option_B:
    name: "H.264 IP Stream"
    description: "Digital encoding over IP network"
    pros: "Standard protocols, encryption, networking"
    cons: "Some latency (50-150ms)"
    implementation:
      encoder: "Hardware H.264 (Jetson/RPi)"
      protocol: "RTSP or WebRTC"
      transport: "UDP/RTP for low latency"
    variant: "RCWS ✓, RCWS-LITE ✓"
  option_C:
    name: "H.265 Low-Latency"
    description: "HEVC with optimized pipeline"
    pros: "Better compression, lower bandwidth"
    cons: "Higher compute, some compatibility"
    variant: "Future upgrade"

datalink_options:
  wired:
    interface: "Ethernet (Cat6, up to 100m)"
    latency: "~50ms"
    reliability: "Highest"
  wireless:
    interface: "5GHz WiFi or proprietary"
    range: "100-500m LOS"
    latency: "~100ms"
    encryption: "WPA3 or AES"

local_sourcing:
  encoder: "NVIDIA Jetson or RPi with HW encode"
  radios: "Commercial WiFi or import"
  software: "GStreamer/FFmpeg (open source)"
  local_content: "60% (integration, housing)"
```

### WP-VSMASH-017: Remote Control Unit (NEW v1.3 - Hopper RE)

```yaml
id: "WP-VSMASH-017"
subfunction: "F8.5 - Receive operator commands"
physical_effect: "Human-machine interface"
form_design: "Handheld controller with joystick and display"

specification:
  controls:
    - "2-axis joystick (pan/tilt rate)"
    - "Zoom rocker"
    - "Fire button (with safety)"
    - "Mode selector"
    - "Emergency stop"
  display: "5-7 inch video monitor"
  connectivity: "Wired (primary) + Wireless (backup)"

options:
  option_A:
    name: "Wired RCU Only"
    description: "Tethered controller, no wireless"
    pros: "Secure, no jamming, simple"
    cons: "Limited mobility, cable management"
    cable_length: "10-50m"
    variant: "RCWS-LITE ✓"
  option_B:
    name: "Wired + Wireless"
    description: "Dual-mode with fallback"
    pros: "Flexibility, backup modes"
    cons: "More complex, two systems"
    wireless_range: "100-300m"
    variant: "RCWS ✓"
  option_C:
    name: "Tablet/Smartphone"
    description: "Commercial tablet as controller"
    pros: "Large display, familiar UI"
    cons: "Less rugged, touch latency"
    variant: "Training/demo option"

ergonomics:
  weight: "<1.5 kg"
  operating_time: "8 hours on charge"
  environmental: "IP65, -10°C to +55°C"
  grip: "Two-handed with neck strap"

local_sourcing:
  joystick: "Import (industrial grade)"
  display: "Import (ruggedized)"
  housing: "Local fabrication"
  electronics: "Local assembly"
  local_content: "50%"
```

### WP-VSMASH-018: External Cueing Interface (NEW v1.3 - DOME RE)

```yaml
id: "WP-VSMASH-018"
subfunction: "F8.6/F9.1 - Accept external target cue"
physical_effect: "Data communication protocol"
form_design: "Multi-protocol target handoff interface"

specification:
  input_data:
    - "Target azimuth/elevation"
    - "Target range (if available)"
    - "Target classification"
    - "Confidence level"
  response_time: "<500ms cue-to-on-target"
  protocols_supported: ["Serial", "Ethernet", "CoT"]

options:
  option_A:
    name: "None"
    description: "Standalone operation, no external input"
    pros: "Simplest, self-contained"
    cons: "No force multiplication"
    variant: "RCWS-LITE ✓, DOME Basic"
  option_B:
    name: "Serial (RS-422)"
    description: "Point-to-point serial command"
    pros: "Simple, robust, long distance"
    cons: "Single source only"
    protocol: "Custom ASCII or NMEA-style"
    variant: "Option for radar interface"
  option_C:
    name: "Ethernet/CoT"
    description: "IP network with tactical protocol"
    pros: "Multiple sources, standard format"
    cons: "Network complexity"
    protocol: "Cursor on Target (CoT) XML"
    integration: "TAK server compatible"
    variant: "RCWS ✓, DOME Standard ✓"

radar_integration:
  supported_radars:
    - "Ground surveillance radar"
    - "Drone detection radar"
    - "AESA panels"
  handoff_format:
    azimuth: "0-360° (degrees)"
    elevation: "-10° to +90° (degrees)"
    range: "Meters"
    classification: "Enum (drone, vehicle, person)"

implementation:
  parser: "XML/JSON parser for CoT"
  coordinate_transform: "Radar to gimbal frame"
  cue_smoothing: "Kalman filter on cue updates"
```

### WP-VSMASH-019: Sector Scan Logic (NEW v1.3 - Hopper RE)

```yaml
id: "WP-VSMASH-019"
subfunction: "F8.7 - Execute automatic scan patterns"
physical_effect: "Motion planning algorithm"
form_design: "Configurable sector scan with detection integration"

specification:
  scan_patterns:
    - "Sector scan (azimuth sweep)"
    - "Raster scan (2D coverage)"
    - "Spiral search (point of interest)"
  scan_rate: "Configurable (5-30°/sec)"
  detection_pause: "Auto-pause on detection"
  resume: "Auto-resume after track loss"

options:
  option_A:
    name: "None (Manual Only)"
    description: "Operator controls all motion"
    pros: "Full control, no automation"
    cons: "Operator fatigue, may miss threats"
    variant: "RCWS-LITE ✓"
  option_B:
    name: "Sector Scan"
    description: "Automated azimuth sweep between limits"
    pros: "Continuous coverage, reduces fatigue"
    cons: "Predictable pattern"
    parameters:
      sector_left: "-90° to +90°"
      sector_right: "-90° to +90°"
      scan_speed: "10°/sec default"
    variant: "RCWS ✓, DOME ✓"
  option_C:
    name: "Spiral Search"
    description: "Expanding spiral from cue point"
    pros: "Good for search after cue"
    cons: "Leaves gaps in coverage"
    variant: "Option"
  option_D:
    name: "Track-While-Scan"
    description: "Maintain track while scanning"
    pros: "Best situational awareness"
    cons: "Complex, requires multi-target"
    variant: "DOME Enhanced"

detection_integration:
  on_detection: "Pause scan, evaluate target"
  track_handoff: "If track confirmed, exit scan mode"
  no_track: "Resume scan after 2 seconds"
  operator_override: "Manual control always available"

implementation:
  motion_planner: "Trapezoidal velocity profile"
  integration: "Subscribe to detection events"
  state_machine: "IDLE → SCANNING → PAUSED → TRACKING"
```

### WP-VSMASH-020: Portable Deployment System (NEW v1.3 - Hopper Light RE)

```yaml
id: "WP-VSMASH-020"
subfunction: "F8.8 - Enable rapid portable deployment"
physical_effect: "Mechanical structure transformation"
form_design: "Folding tripod with quick-setup mechanism"

specification:
  setup_time: "<60 seconds by single soldier (R103)"
  teardown_time: "<60 seconds"
  carry_mode: "Backpack or carry case"
  deployed_height: "Adjustable 0.5-1.5m"
  stability: "Stable in 20 km/h wind"

options:
  option_A:
    name: "Fixed Mount"
    description: "Permanent vehicle/structure mount"
    pros: "Most stable, no setup"
    cons: "Not portable"
    variant: "RCWS (vehicle mount)"
  option_B:
    name: "Folding Tripod"
    description: "Collapsible legs with quick-lock"
    pros: "Portable, stable, proven design"
    cons: "Some setup time"
    features:
      - "Tool-free assembly"
      - "Self-leveling head"
      - "Spike/pad feet options"
      - "Carry strap integrated"
    variant: "RCWS-LITE ✓"
  option_C:
    name: "Quick-Release"
    description: "Rail mount for vehicle/tripod swap"
    pros: "Flexibility, fast changeover"
    cons: "Additional adapter weight"
    variant: "Option for RCWS"
  option_D:
    name: "Backpack Integrated"
    description: "Frame doubles as backpack"
    pros: "Hands-free carry, always together"
    cons: "Heavier frame, less modular"
    variant: "Future option"

single_soldier_requirement:
  total_weight: "≤10 kg system (R100)"
  carry_weight: "Single load"
  assembly: "No tools required"
  training: "30-minute familiarization"

local_sourcing:
  tripod: "Local aluminum fabrication"
  quick_locks: "Import or local"
  leveling_head: "Import mechanism"
  local_content: "70%"
```

### WP-VSMASH-021: C-UAS Detection Layer (NEW v1.3 - DOME RE)

```yaml
id: "WP-VSMASH-021"
subfunction: "F9.1 - Detect airspace threats"
physical_effect: "Multi-sensor detection"
form_design: "Layered sensor architecture"

specification:
  detection_range:
    eo_ir: "1-2 km (visual conditions) (R109)"
    radar: "2-5 km (optional) (R110)"
    acoustic: "0.5-1 km (optional)"
  coverage: "360° azimuth, 0-60° elevation"
  update_rate: "1-10 Hz depending on sensor"
  false_alarm_rate: "<1 per hour"

options:
  option_A:
    name: "EO/IR Only"
    description: "Optical sensors only"
    pros: "Lower cost, passive, proven"
    cons: "Weather limited, range limited"
    sensors:
      - "HD day camera (pan/scan or fixed array)"
      - "Thermal camera (optional)"
    variant: "DOME Basic ✓"
  option_B:
    name: "EO/IR + Acoustic"
    description: "Add microphone array"
    pros: "360° awareness, weather tolerant"
    cons: "Range limited, noise environment"
    acoustic:
      - "4+ microphone array"
      - "Direction finding"
      - "Drone signature matching"
    variant: "Option"
  option_C:
    name: "EO/IR + Radar"
    description: "Add drone detection radar"
    pros: "Best range, all-weather"
    cons: "Higher cost, RF signature"
    radar_options:
      - "2D scanning radar"
      - "3D AESA panel"
      - "FMCW micro-doppler"
    range: "2-5 km on small drone"
    variant: "DOME Standard ✓"
  option_D:
    name: "Multi-Layer"
    description: "EO/IR + Radar + Acoustic + RF detect"
    pros: "Maximum detection probability"
    cons: "Highest cost, complexity"
    variant: "DOME Enhanced (future)"

sensor_fusion:
  approach: "Track-level fusion"
  architecture: "Central fusion processor"
  output: "Unified track picture"

local_sourcing:
  cameras: "Import (industrial/security grade)"
  radar: "Import or partner (VIETTEL?)"
  acoustic: "Local development possible"
  integration: "Local capability"
  local_content: "40-50%"
```

### WP-VSMASH-022: UAS Classification AI (NEW v1.3 - DOME RE)

```yaml
id: "WP-VSMASH-022"
subfunction: "F9.2 - Classify detected UAS targets"
physical_effect: "Machine learning classification"
form_design: "CNN classifier with drone-specific training"

specification:
  classes:
    - "FPV racing drone"
    - "Commercial quadcopter"
    - "Fixed-wing UAV"
    - "Loitering munition"
    - "Bird (false alarm)"
    - "Aircraft (non-threat)"
  accuracy: "≥90% on known types (R112)"
  classification_time: "<100ms"
  confidence_output: "0-100%"

options:
  option_A:
    name: "Rule-Based (Size/Speed)"
    description: "Simple thresholds on track parameters"
    pros: "Interpretable, no training needed"
    cons: "Poor accuracy, easily fooled"
    rules:
      - "Size < X pixels = small drone"
      - "Speed > Y m/s = fixed wing"
    variant: "Fallback mode"
  option_B:
    name: "CNN Classifier"
    description: "Neural network trained on drone images"
    pros: "High accuracy, adapts to appearance"
    cons: "Requires training data, compute"
    architecture: "MobileNet-V2 or similar"
    input: "224x224 crop around detection"
    variant: "DOME ✓"
  option_C:
    name: "Multi-Sensor Fusion Classification"
    description: "Combine visual + radar + acoustic features"
    pros: "Most robust, all-weather"
    cons: "Complex, multiple sensors needed"
    features:
      visual: "Appearance, shape"
      radar: "RCS, micro-Doppler"
      acoustic: "Rotor signature"
    variant: "DOME Enhanced"
  option_D:
    name: "Behavioral Analysis"
    description: "Classify based on flight pattern"
    pros: "Works at range, before visual ID"
    cons: "Requires track history"
    patterns:
      - "Loitering"
      - "Direct approach"
      - "Surveillance orbit"
    variant: "Future enhancement"

training:
  dataset: "Shared with WP-013 (5,000+ images)"
  transfer_learning: "ImageNet pretrained backbone"
  fine_tuning: "Vietnam-specific drone types"
  validation: "Field testing required"

implementation:
  compute: "NVIDIA Jetson Xavier NX"
  framework: "TensorRT optimized"
  latency: "~50ms per classification"
```

### WP-VSMASH-023: PITL Engagement Interface (NEW v1.3 - DOME RE)

```yaml
id: "WP-VSMASH-023"
subfunction: "F9.5 - Coordinate engagement with operator"
physical_effect: "Human-machine decision interface"
form_design: "Video display with threat overlay and authorization"

specification:
  requirement: "Person-in-the-loop mandatory (R111)"
  display: "Live video with target overlay"
  authorization: "Explicit operator confirm required"
  decision_time: "Support rapid (2-5 second) decisions"
  audit: "Log all engagement decisions"

options:
  option_A:
    name: "Audio Alert Only"
    description: "Sound alarm, operator finds target"
    pros: "Simplest"
    cons: "Slow response, may miss"
    variant: "Not recommended"
  option_B:
    name: "Video + Overlay"
    description: "Live video with bounding box and threat info"
    pros: "Full situational awareness, proven"
    cons: "Requires good display"
    overlay_elements:
      - "Target bounding box (color = threat level)"
      - "Classification label"
      - "Range/bearing"
      - "Engagement recommendation"
      - "Confirm/Reject buttons"
    variant: "DOME ✓"
  option_C:
    name: "AR Headset"
    description: "Augmented reality with 3D threat cues"
    pros: "Immersive, hands-free"
    cons: "Expensive, training required"
    variant: "Future option"

engagement_workflow:
  1_detect: "System detects and classifies threat"
  2_alert: "Audio + visual alert to operator"
  3_present: "Show threat on display with recommendation"
  4_decide: "Operator confirms or rejects engagement"
  5_engage: "If confirmed, system commands effector"
  6_assess: "Show BDA, log outcome"

authorization_modes:
  manual: "Each target requires explicit confirm"
  semi_auto: "Confirm once, engage until revoked"
  watch_only: "Display only, no engagement"

audit_logging:
  fields:
    - timestamp
    - target_id
    - classification
    - threat_score
    - operator_decision
    - engagement_result
  storage: "Local + exportable"
  retention: "Mission duration minimum"
```

### WP-VSMASH-024: Battle Damage Assessment (NEW v1.3 - DOME RE)

```yaml
id: "WP-VSMASH-024"
subfunction: "F9.7 - Assess engagement outcome"
physical_effect: "Visual and track analysis"
form_design: "Post-engagement assessment logic"

specification:
  assessment_types:
    - "Target destroyed (crash observed)"
    - "Target damaged (behavior change)"
    - "Target lost (track expired)"
    - "Miss (target continues)"
  assessment_time: "<5 seconds post-engagement"
  reporting: "BDA result to operator and log"

options:
  option_A:
    name: "Operator Visual"
    description: "Operator observes and reports outcome"
    pros: "Most reliable, no AI needed"
    cons: "Slow, subjective, fatigue"
    variant: "DOME Basic ✓"
  option_B:
    name: "AI Track Loss"
    description: "Detect track termination or behavior change"
    pros: "Automatic, fast"
    cons: "May be ambiguous"
    indicators:
      - "Track lost for >3 seconds"
      - "Rapid altitude loss"
      - "Velocity → 0"
      - "New debris tracks"
    variant: "DOME Standard ✓"
  option_C:
    name: "Kill Confirmation AI"
    description: "Visual recognition of destroyed target"
    pros: "High confidence"
    cons: "Requires training data, compute"
    features:
      - "Explosion/debris detection"
      - "Impact point tracking"
      - "Before/after comparison"
    variant: "Future enhancement"

bda_workflow:
  1_engage: "Fire command sent to effector"
  2_observe: "Continue tracking during engagement"
  3_assess: "Analyze track state post-firing"
  4_report: "Generate BDA result"
  5_decide: "Re-engage if miss, next target if kill"

metrics:
  pk_tracking: "Probability of kill per engagement"
  rounds_per_kill: "Ammunition efficiency"
  time_to_kill: "Detection to neutralization"
```

### WP-VSMASH-025: CoT Protocol Stack (NEW v1.3 - DOME RE)

```yaml
id: "WP-VSMASH-025"
subfunction: "F9.8 - Network with C2/ATAK"
physical_effect: "Tactical data protocol"
form_design: "Cursor on Target (CoT) implementation"

specification:
  protocol: "Cursor on Target (CoT) v3.0"
  transport: "UDP multicast or TCP"
  message_types:
    - "Track report (position, velocity, class)"
    - "Alert (new threat)"
    - "Status (system health)"
    - "BDA report (engagement outcome)"
  update_rate: "1-5 Hz per track"
  encryption: "TLS or AES-256"

options:
  option_A:
    name: "Standalone"
    description: "No external networking"
    pros: "Simplest, no dependencies"
    cons: "No force multiplication"
    variant: "DOME Basic ✓"
  option_B:
    name: "Serial Export"
    description: "Simple text output"
    pros: "Easy integration"
    cons: "Point-to-point, limited"
    variant: "Legacy systems"
  option_C:
    name: "CoT/ATAK"
    description: "Standard tactical data format"
    pros: "Interoperable, widely supported"
    cons: "Requires network infrastructure"
    integration:
      - "TAK Server compatible"
      - "ATAK client display"
      - "WinTAK for command post"
    variant: "DOME Standard ✓"
  option_D:
    name: "Link-16 Gateway"
    description: "Bridge to military datalink"
    pros: "Military interoperability"
    cons: "Export controlled, expensive"
    variant: "Future/Partner"

cot_message_example:
  event_type: "a-f-A-M-F-Q" # Airborne, friend, aircraft, military, fixed-wing, quadcopter
  point:
    lat: "10.123456"
    lon: "106.654321"
    hae: "100" # height above ellipsoid
  detail:
    track:
      course: "270"
      speed: "15"
    classification: "FPV_drone"
    threat_level: "HIGH"
    source: "V-SMASH-DOME-001"

atak_integration:
  display: "Icon on map with threat info"
  alert: "Audio/visual on detection"
  coordination: "Multiple DOME units share tracks"
  handoff: "Manual engagement assignment"

local_capability:
  protocol_stack: "Open source (TAK SDK)"
  integration: "Software development"
  testing: "Requires ATAK network"
  local_content: "90% (software)"
```

---

## 4. CONCEPT COMPARISON TABLE

| Criterion | V1: Clone | V2: Local-First | V3: Hybrid | V4: Phased | **LITE** | **PRO** |
|-----------|-----------|-----------------|------------|------------|----------|---------|
| **Performance** | ★★★★ | ★★ | ★★★ | ★★★ | ★★★ | ★★★★ |
| **Local Content** | ★ | ★★★★ | ★★★ | ★★★★ | ★★★★ | ★★★ |
| **Development Risk** | ★★★★ | ★★★ | ★★ | ★★★ | ★★★★ | ★★★ |
| **Cost (Development)** | ★ | ★★★ | ★★★ | ★★★★ | ★★★★ | ★★★ |
| **Cost (Production)** | ★ | ★★★★ | ★★★ | ★★★ | ★★★★ | ★★★ |
| **Time to Market** | ★★ | ★★★ | ★★ | ★★★★ | ★★★★ | ★★★ |
| **Capability Growth** | ★★ | ★ | ★★★ | ★★★★ | ★★ | ★★★★ |
| **Supply Chain Risk** | ★ | ★★★★ | ★★★ | ★★★ | ★★★★ | ★★★ |
| **Multi-Target (R65)** | ★★★ | ★★ | ★★★ | ★★★ | ★★★ | ★★★★ |
| **C4I Ready (R67)** | ★★ | ★ | ★★ | ★★ | ★ | ★★★★ |
| **Sensor Fusion (R70)** | ★★★ | ★ | ★★ | ★★ | ★ | ★★★★ |
| **C-UAS AI (R68)** | ★★★ | ★★ | ★★★ | ★★★ | ★★★ | ★★★★ |

**★ Rating**: 1 star = Poor, 4 stars = Excellent

### LITE vs PRO Feature Matrix (v1.2)

| Feature | LITE | PRO |
|---------|------|-----|
| Max simultaneous tracks | 5 | 5 |
| Data association | Nearest-Neighbor | Hungarian |
| Threat prioritization | Distance-based | Multi-factor AI |
| Target selection | Operator + auto-suggest | Auto + override |
| Engagement queue | None (single) | Priority queue |
| Rapid target switch | Yes | Yes (faster) |
| Target data sharing | None | C4I protocol |
| Night capability | Clip-on compatible | Integrated thermal |
| **Sensor fusion (R70)** | **None (single sensor)** | **Weighted blend** |
| **C-UAS AI training (R68)** | **C-UAS optimized** | **C-UAS optimized** |
| **Passive ranging (R69)** | **Size-based backup** | **LRF primary** |
| **Target price** | **$3,000** | **$4,500-5,000** |

### RCWS vs RCWS-LITE Feature Matrix (NEW v1.3)

| Feature | RCWS-LITE | RCWS |
|---------|-----------|------|
| **Total weight (excl. weapon)** | **≤10 kg (R100)** | **≤15 kg (R92)** |
| Pan range | ±120° | 360° continuous (R93) |
| Tilt range | -20° to +45° | -30° to +70° (R94) |
| Slew rate | 20°/sec | ≥30°/sec (R95) |
| Stabilization | Passive (friction) | Gyro-stabilized 2-axis |
| Video streaming | H.264 IP (1080p) | H.264 IP (1080p) |
| Operator interface | Wired RCU only | Wired + Wireless |
| External cueing | None | Ethernet/CoT (R98) |
| Auto-scan | None (manual) | Sector scan |
| Deployment | Folding tripod (R103) | Fixed/vehicle mount |
| Setup time | <60 sec single soldier | Pre-installed |
| Setup personnel | 1 (R102) | 2 |
| **Target price** | **$8,000** | **$12,000** |

### DOME Configuration Matrix (NEW v1.3)

| Feature | DOME Basic | DOME Standard | DOME Enhanced |
|---------|------------|---------------|---------------|
| **Detection sensors** | EO/IR only | EO/IR + Radar | Multi-layer |
| Detection range | 1-2 km | 2-5 km | 5+ km |
| UAS classification | CNN classifier | CNN classifier | Multi-sensor fusion |
| Track management | Single sensor | Sensor fusion | Distributed fusion |
| Threat prioritization | Distance-based | Multi-factor | AI/ML adaptive |
| PITL interface | Video + overlay | Video + overlay | AR option |
| Fire coordination | Manual command | Semi-auto confirm | Auto-engage capable |
| BDA assessment | Operator visual | AI track loss | Kill confirmation AI |
| C2 networking | Standalone | CoT/ATAK | Link-16 gateway |
| **System weight** | ~30 kg | ~50 kg | ~80 kg |
| **Target price** | **$30,000** | **$50,000** | **$80,000** |

---

## 5. SELECTION RATIONALE (Preview)

**V4: Phased Development** selected based on:

1. **Risk Mitigation**: Progressive capability buildup reduces technical risk
2. **Learning Integration**: Each phase informs the next, building team expertise
3. **Budget Alignment**: Spread investment over time, demonstrate value early
4. **Local Expertise**: Capability growth matches Vietnamese industry development
5. **Flexibility**: Can pivot based on Phase 1 results

**VDI 2225 Score**: See [[V-SMASH_P2_03_concept_evaluation|Concept Evaluation v1.2]]
- LITE: 88%
- PRO: 79%

---

## 6. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-18 | Initial morphological matrix (15 subfunctions) |
| 1.1 | 2026-02-04 | Multi-target update: Added 7 new subfunctions (F2.5-F2.7, F7.1-F7.4), 6 new working principles (WP-006 to WP-011), LITE/PRO differentiation. Source: ARCAS RE analysis. |
| 1.2 | 2026-02-04 | Sensor fusion update: Added F1.5 (sensor fusion), F1.6 (AI training data), 2 new working principles (WP-012, WP-013). Source: ARBEL RE analysis. |
| **1.3** | **2026-02-04** | **RCWS/DOME update: Added F8 (RCWS Platform Control, 8 subfunctions) and F9 (Integrated C-UAS System, 8 subfunctions). Added 12 new working principles (WP-014 to WP-025). Added RCWS/RCWS-LITE and DOME configuration matrices. Source: Hopper 5000, Hopper Light, SMASH DOME RE analyses. Total: 40 subfunctions, 25 working principles.** |

---

## 7. SUMMARY STATISTICS (v1.3)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║              MORPHOLOGICAL MATRIX v1.3 - COMPLETE COVERAGE                 ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  Function Groups:     10 (F1-F9 + F_AUX)                                   ║
║  Subfunctions:        40 total                                             ║
║  Working Principles:  25 detailed specifications                           ║
║                                                                            ║
║  HANDHELD FCS:                                                             ║
║  └── F1-F7, F_AUX → LITE, PRO, PRO-X, HMG, MARITIME                       ║
║                                                                            ║
║  RCWS PLATFORM:                                                            ║
║  └── F1-F8, F_AUX → RCWS, RCWS-LITE (8 new subfunctions)                  ║
║                                                                            ║
║  INTEGRATED C-UAS:                                                         ║
║  └── F1-F9, F_AUX → DOME Basic/Standard/Enhanced (8 new subfunctions)     ║
║                                                                            ║
║  Product Coverage:    9 variants fully specified                           ║
║  RE Sources:          10 foreign systems analyzed                          ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

*Prev: [[V-SMASH_P2_01_function_structure|Function Structure v1.3]]*
*Next: [[V-SMASH_P2_03_concept_evaluation|Concept Evaluation v1.3]]*
*Back to: [[V-SMASH_00_project_brief|Project Brief]]*
*RE Sources: [[V-SMASH_RE_02_ARCAS_analysis|ARCAS]] | [[V-SMASH_RE_03_ARBEL_analysis|ARBEL]] | [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|Hopper 5000]] | [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light]] | [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME]]*
