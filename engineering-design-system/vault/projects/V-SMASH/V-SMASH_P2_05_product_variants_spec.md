---
project: V-SMASH
phase: 2
type: product_specification
version: 2.1
created: 2026-02-04
updated: 2026-02-04
status: approved
strategy: multi-tier-platform-family
---

# V-SMASH PRODUCT VARIANTS SPECIFICATION
## Multi-Tier Platform Family: 9 Product Variants

**Document ID:** V-SMASH_P2_05
**Approval Date:** 2026-02-04
**Source:** ODI Analysis, Concept Evaluation v1.4, 10 RE Analyses

---

## 1. EXECUTIVE SUMMARY

### 1.1 Strategy Overview

The V-SMASH program adopts a **multi-tier platform family strategy** with 9 product variants across 4 categories:

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    V-SMASH PRODUCT FAMILY ARCHITECTURE                     ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  HANDHELD FCS ($3K-$7K)              PLATFORM-MOUNTED ($6K-$12K)          ║
║  ┌─────────────────────┐             ┌─────────────────────────┐          ║
║  │ V-SMASH LITE  $3,000│             │ V-SMASH HMG      $6,000 │          ║
║  │ V-SMASH PRO   $5,000│             │ V-SMASH MARITIME $6,500 │          ║
║  │ V-SMASH PRO-X $7,000│             │ V-SMASH RCWS-LITE$8,000 │          ║
║  └─────────────────────┘             │ V-SMASH RCWS    $12,000 │          ║
║                                      └─────────────────────────┘          ║
║  INTEGRATED SYSTEM ($50K)            ACCESSORY ($2K)                      ║
║  ┌─────────────────────┐             ┌─────────────────────────┐          ║
║  │ V-SMASH DOME $50,000│             │ V-SMASH C4I HUB  $2,000 │          ║
║  └─────────────────────┘             └─────────────────────────┘          ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

| Variant | Category | VDI Score | Target Price | Delivery | Primary Market |
|---------|----------|-----------|--------------|----------|----------------|
| **V-SMASH LITE** | Handheld | 88% | $3,000 | Phase 1 | Training, daylight C-UAS |
| **V-SMASH PRO** | Handheld | 79% | $5,000 | Phase 2 | 24/7 operational C-UAS |
| **V-SMASH PRO-X** | Handheld | 76% | $7,000 | Phase 2 | Extended range, LRF |
| **V-SMASH HMG** | Platform | 81% | $6,000 | Phase 1 | 12.7mm HMG integration |
| **V-SMASH MARITIME** | Platform | 75% | $6,500 | Phase 2 | Naval/coastal patrol |
| **V-SMASH RCWS-LITE** | Platform | 83% | $8,000 | Phase 2 | Single-soldier portable |
| **V-SMASH RCWS** | Platform | 74% | $12,000 | Phase 3 | Vehicle-mounted full |
| **V-SMASH DOME** | System | 73% | $50,000 | Phase 3 | Integrated C-UAS |
| **V-SMASH C4I HUB** | Accessory | 82% | $2,000 | Phase 2 | Squad coordination |

### 1.2 Strategic Rationale

1. **Risk Mitigation:** LITE/HMG deliver early capability while advanced products develop
2. **Market Segmentation:** Entry-level to premium capability spectrum
3. **Platform Commonality:** Core FCS module shared across all variants (60-80% reuse)
4. **ODI Alignment:** Full product family addresses all identified market opportunities
5. **Technology Scaling:** Same SMASH FCS technology from handheld to integrated system

---

## 2. PRODUCT COMPARISON MATRIX

### 2.1 Capability Comparison

| Category | Specification | LITE | PRO | Notes |
|----------|---------------|------|-----|-------|
| **DETECTION** | | | | |
| | Day detection range (drone) | 300m | 300m | Same |
| | Night detection range | — | **200m** | Thermal required |
| | Detection accuracy (day) | 95% | 95% | Same |
| | Detection in varying light | 85% | **95%** | HDR sensor |
| | False positive rate | <10% | **<5%** | Better training |
| **TRACKING** | | | | |
| | Max target speed | 50 m/s | 50 m/s | Same |
| | Maneuver tracking | 1.5g | **3g** | IMM filter |
| | Track-to-track handoff | Basic | **Advanced** | Multi-target |
| **MULTI-TARGET (NEW v1.1)** | | | | |
| | Simultaneous tracks | **5** | **5** | R65 - Both meet |
| | Data association | Nearest-Neighbor | **Hungarian** | PRO more robust |
| | Threat prioritization | Distance-based | **Multi-factor AI** | R66 - PRO only |
| | Target selection | Operator + suggest | **Auto + override** | Faster engagement |
| | Engagement queue | None (single) | **Priority queue** | Sequential engage |
| | Rapid switch latency | <100ms | **<50ms** | State preservation |
| | C4I target sharing | None | **CoT/UDP** | R67 - PRO only |
| **FIRE CONTROL** | | | | |
| | Fire solution latency | <100ms | <100ms | Same |
| | Trigger precision | <5ms | <5ms | Same |
| | Hit improvement | 3x | **4x** | Better tracking |
| **ENVIRONMENTAL** | | | | |
| | Operating temp | -10°C to +55°C | -10°C to +55°C | Same |
| | Sealing | IP65 | **IP67** | Enhanced |
| | Lens anti-fog | — | **Yes** | Heater |
| | Lens protection | — | **Optional** | Wiper |
| **SENSOR** | | | | |
| | Primary sensor | CMOS 1080p60 | CMOS 1080p60 | Same |
| | Thermal sensor | — | **LWIR 160x120** | FLIR Lepton |
| | Dynamic range | 65 dB | **≥80 dB** | HDR upgrade |
| | Night vision | Clip-on compatible | **Integrated** | |
| **PHYSICAL** | | | | |
| | Weight (handheld) | <1.2 kg | **<1.5 kg** | Thermal adds mass |
| | Dimensions | 150×80×100mm | 170×90×110mm | Slightly larger |
| | Power consumption | 5W avg | **8W avg** | Thermal power |
| | Battery life | >8 hours | **>6 hours** | Higher draw |

### 2.2 Requirements Compliance

| Req ID | Requirement | LITE | PRO | ODI Source |
|--------|-------------|------|-----|------------|
| **ORIGINAL (57)** | | | | |
| R01-R05 | Core detection/tracking | ✅ | ✅ | S1-01, S1-02 |
| R06 | Night operation | ⚠️ Clip-on | ✅ **Integrated** | S1-22 |
| R08-R11 | Range/effectiveness | ✅ | ✅ | S1-03, S1-05 |
| R12-R16 | Environmental | ✅ | ✅ | — |
| R14 | Sealing | ✅ IP65 | ✅ **IP67** | S1-19 |
| R18-R22 | Physical | ✅ | ✅ | — |
| R23-R30 | Integration | ✅ | ✅ | — |
| R31-R35 | Safety | ✅ | ✅ | — |
| R36-R57 | Other | ✅ | ✅ | — |
| **NEW ODI (7)** | | | | |
| R58 | False positive <5% | ❌ ~10% | ✅ **<5%** | S1-16 |
| R59 | Varying light 95% | ❌ ~85% | ✅ **95%** | S1-17 |
| R60 | 3g maneuver tracking | ❌ ~1.5g | ✅ **3g** | S1-24 |
| R61 | HDR ≥80dB | ❌ 65dB | ✅ **≥80dB** | S1-17 |
| R62 | Thermal sensor | ❌ | ✅ **LWIR** | S1-22 |
| R63 | Lens anti-fog | ❌ | ✅ **Heater** | S1-19 |
| R64 | Lens protection (W) | ❌ | ⚠️ Optional | S1-19 |
| **MULTI-TARGET (3) - ARCAS RE** | | | | |
| R65 | Multi-target ≥5 (D) | ✅ **5 tracks** | ✅ **5 tracks** | ARCAS RE |
| R66 | Threat prioritization (W) | ⚠️ Distance-based | ✅ **Multi-factor** | ARCAS RE |
| R67 | C4I data sharing (W) | ❌ None | ✅ **CoT/UDP** | ARCAS RE |
| **COMPLIANCE** | | **52/67 (78%)** | **65/67 (97%)** | |

---

## 3. TECHNICAL SPECIFICATIONS

### 3.1 V-SMASH-LITE Specifications

```yaml
variant: V-SMASH-LITE
designation: VSM-L
status: Primary Phase 1 Deliverable

sensor_subsystem:
  primary_sensor:
    type: CMOS
    model: Sony IMX290
    resolution: 1920x1080
    frame_rate: 60 fps
    dynamic_range: 65 dB
    low_light: 0.1 lux (with gain)
  thermal_sensor: None (NV clip-on compatible)
  imu:
    type: 6-axis MEMS
    model: BMI160
    gyro_range: ±2000°/s
    accel_range: ±16g

processing_subsystem:
  platform: NVIDIA Jetson Nano 4GB
  detection: YOLOv8-nano (INT8 quantized)
  tracking: Kalman Filter (6-state)
  ballistics: Point-mass 3DOF
  latency: <50ms end-to-end

multi_target_subsystem:  # NEW v1.1
  max_tracks: 5
  track_pool: Fixed array (pre-allocated)
  data_association: Nearest-Neighbor (O(NM))
  threat_prioritization: Distance-based (1/range)
  target_selection: Operator + auto-suggest
  engagement_queue: None (single target)
  switch_latency: <100ms
  c4i_interface: None

fire_control:
  trigger_sensor: FSR402 force sensor
  trigger_gate: 12V solenoid, <5ms response
  fire_modes: [AI-assisted, Manual]

optical_subsystem:
  magnification: 1x (reflex style)
  fov: 15°
  eye_relief: Unlimited
  reticle: Etched + electronic overlay

power_subsystem:
  battery: 18650 Li-ion × 2 (6800mAh total)
  voltage: 7.4V nominal
  consumption: 5W average
  runtime: >8 hours
  charging: USB-C PD, 2 hours

physical:
  weight: <1.2 kg (with battery)
  dimensions: 150 × 80 × 100 mm
  material: Aluminum 6061-T6, anodized
  sealing: IP65
  mounting: Picatinny (MIL-STD-1913)

environmental:
  operating_temp: -10°C to +55°C
  storage_temp: -40°C to +70°C
  humidity: 95% RH
  shock: MIL-STD-810H Method 516.8
  vibration: MIL-STD-810H Method 514.8

performance:
  detection_range_drone: 300m (day)
  detection_accuracy: 95%
  false_positive_rate: <10%
  tracking_maneuver: 1.5g
  hit_improvement: 3x vs iron sights
  first_round_pk: >60% @ 200m
  # Multi-target performance (NEW v1.1)
  simultaneous_tracks: 5
  track_switch_time: <100ms
  association_accuracy: 90% (NN limited in clutter)
  swarm_capacity: 5 targets max
```

### 3.2 V-SMASH-PRO Specifications

```yaml
variant: V-SMASH-PRO
designation: VSM-P
status: Phase 2 Deliverable (24/7 Capability)

sensor_subsystem:
  primary_sensor:
    type: CMOS (HDR)
    model: Sony IMX462  # Upgraded from IMX290
    resolution: 1920x1080
    frame_rate: 60 fps
    dynamic_range: 85 dB  # HDR capability
    low_light: 0.001 lux (starlight)
  thermal_sensor:
    type: LWIR uncooled microbolometer
    model: FLIR Lepton 3.5
    resolution: 160x120
    spectral_range: 8-14 μm
    netd: <50 mK
    fov: 57°
  imu:
    type: 6-axis MEMS
    model: BMI160
    gyro_range: ±2000°/s
    accel_range: ±16g

processing_subsystem:
  platform: NVIDIA Jetson Nano 4GB  # Same as LITE
  detection: YOLOv8-nano (INT8) + thermal fusion
  tracking: IMM Filter (Interacting Multiple Model)  # Upgraded
  ballistics: Point-mass 3DOF
  latency: <50ms end-to-end
  fusion: CMOS + Thermal weighted blend

multi_target_subsystem:  # NEW v1.1
  max_tracks: 5
  track_pool: Fixed array (pre-allocated)
  data_association: Hungarian Algorithm (O(n³))  # Upgraded
  threat_prioritization: Multi-factor AI scoring  # Upgraded
  priority_weights:
    distance: 0.4
    closing_speed: 0.3
    heading_factor: 0.2
    target_type: 0.1
  target_selection: Auto + manual override  # Upgraded
  engagement_queue: Priority queue  # Upgraded
  switch_latency: <50ms  # Faster
  c4i_interface:  # NEW - PRO only
    protocol: Cursor on Target (CoT)
    transport: UDP
    encryption: AES-256
    update_rate: 1-10 Hz configurable
    compatibility: TAK server

fire_control:
  trigger_sensor: FSR402 force sensor
  trigger_gate: 12V solenoid, <5ms response
  fire_modes: [AI-assisted, Manual, Thermal-priority]

optical_subsystem:
  magnification: 1x (reflex style)
  fov: 15°
  eye_relief: Unlimited
  reticle: Etched + electronic overlay
  lens_heater: Resistive, 2W  # Anti-fog
  lens_wiper: Optional accessory

power_subsystem:
  battery: 18650 Li-ion × 3 (10200mAh total)  # Larger
  voltage: 11.1V nominal
  consumption: 8W average (thermal active)
  runtime: >6 hours
  charging: USB-C PD, 3 hours

physical:
  weight: <1.5 kg (with battery)
  dimensions: 170 × 90 × 110 mm
  material: Aluminum 6061-T6, anodized
  sealing: IP67  # Upgraded
  mounting: Picatinny (MIL-STD-1913)

environmental:
  operating_temp: -10°C to +55°C
  storage_temp: -40°C to +70°C
  humidity: 95% RH
  shock: MIL-STD-810H Method 516.8
  vibration: MIL-STD-810H Method 514.8
  salt_fog: MIL-STD-810H Method 509.7  # Added

performance:
  detection_range_drone_day: 300m
  detection_range_drone_night: 200m  # Thermal
  detection_accuracy: 95%
  false_positive_rate: <5%  # Improved
  tracking_maneuver: 3g  # IMM filter
  hit_improvement: 4x vs iron sights
  first_round_pk: >70% @ 200m
  # Multi-target performance (NEW v1.1)
  simultaneous_tracks: 5
  track_switch_time: <50ms  # Faster than LITE
  association_accuracy: 98% (Hungarian optimal)
  swarm_capacity: 5 targets max (priority managed)
  c4i_latency: <100ms to TAK server
```

### 3.3 V-SMASH-PRO-X Specifications (Extended Range)

```yaml
variant: V-SMASH-PRO-X
designation: VSM-PX
status: Phase 2 Deliverable (Extended Range)
source_re: SMASH X4 Analysis

sensor_subsystem:
  primary_sensor:
    type: CMOS (HDR)
    model: Sony IMX462
    resolution: 1920x1080
    frame_rate: 60 fps
    dynamic_range: 85 dB
  thermal_sensor:
    type: LWIR uncooled microbolometer
    model: FLIR Lepton 3.5
    resolution: 160x120
  magnification_optic:
    type: 4x fixed magnification  # NEW - X4 feature
    fov: 6° (magnified)
    eye_relief: 70mm
  laser_rangefinder:
    type: Eye-safe Class 1  # NEW - X4 feature
    range: 50-800m
    accuracy: ±1m
    integration: Auto-input to ballistics

processing_subsystem:
  platform: NVIDIA Jetson Nano 4GB
  detection: YOLOv8-nano (INT8) + thermal fusion
  tracking: IMM Filter
  ballistics: Point-mass 3DOF with LRF input
  latency: <50ms end-to-end

multi_target_subsystem:
  max_tracks: 5
  data_association: Hungarian Algorithm
  threat_prioritization: Multi-factor AI
  c4i_interface: CoT/UDP

optical_subsystem:
  reticle_type: Etched glass (backup)  # NEW - X4 feature
  electronic_overlay: Yes
  magnification: 4x fixed
  illumination: Red/green selectable

physical:
  weight: <1.8 kg (with battery, optic, LRF)
  dimensions: 220 × 95 × 130 mm
  sealing: IP67
  mounting: Picatinny (MIL-STD-1913)

performance:
  detection_range_drone_day: 500m  # Extended vs PRO
  detection_range_drone_night: 300m
  effective_range: 600m (with LRF)
  hit_improvement: 5x vs iron sights

target_price: $7,000
```

### 3.4 V-SMASH-HMG Specifications (Heavy Machine Gun)

```yaml
variant: V-SMASH-HMG
designation: VSM-HMG
status: Phase 1 Deliverable
source_re: SMASH Connectivity Analysis

application:
  primary_weapon: 12.7x108mm (NSV, DShK)
  secondary_weapons: [14.5mm KPV, 7.62mm PKM]
  mounting: Vehicle pintle, tripod, fixed position

sensor_subsystem:
  primary_sensor:
    type: CMOS (HDR)
    model: Sony IMX462
    resolution: 1920x1080
    frame_rate: 60 fps
  thermal_sensor: Optional add-on
  imu:
    type: 9-axis MEMS  # Enhanced for HMG recoil
    model: BMI088
    shock_rating: 100g

processing_subsystem:
  platform: NVIDIA Jetson Nano 4GB
  detection: YOLOv8-nano (INT8)
  tracking: IMM Filter (recoil-compensated)
  ballistics: Point-mass 3DOF (12.7mm profile)

weapon_interface:
  trigger_interface: Electronic (24V compatible)
  recoil_compensation: Accelerometer-based
  weapon_profiles:
    - caliber: "12.7x108mm"
      bc_g7: "0.620"
      muzzle_velocity: "850 m/s"
    - caliber: "14.5x114mm"
      bc_g7: "0.750"
      muzzle_velocity: "1000 m/s"

physical:
  weight: <1.8 kg (ruggedized housing)
  dimensions: 180 × 100 × 120 mm
  sealing: IP67
  mounting: HMG rail adapter (custom)
  cable_length: 2m to control box

environmental:
  operating_temp: -10°C to +55°C
  shock: 500g peak (HMG recoil)
  vibration: Enhanced (vehicle + firing)

performance:
  detection_range: 800m (day), 400m (thermal)
  effective_range: 1000m (12.7mm)
  hit_improvement: 4x vs manual
  burst_tracking: Yes (track through burst)

target_price: $6,000
```

### 3.5 V-SMASH-MARITIME Specifications (Naval/Coastal)

```yaml
variant: V-SMASH-MARITIME
designation: VSM-M
status: Phase 2 Deliverable
source_re: Vietnam-specific requirements

application:
  primary: Patrol boat mounted weapons
  environment: South China Sea, coastal

sensor_subsystem:
  primary_sensor:
    type: CMOS (HDR)
    model: Sony IMX462
    resolution: 1920x1080
  thermal_sensor:
    type: LWIR
    model: FLIR Lepton 3.5

processing_subsystem:
  platform: NVIDIA Jetson Nano 4GB
  detection: YOLOv8-nano + maritime AI
  tracking: IMM Filter (wave-compensated)
  ballistics: Point-mass 3DOF + ship motion

maritime_features:
  wave_compensation: 6-DOF motion input
  horizon_stabilization: Yes
  salt_fog_protection: MIL-STD-810H Method 509.7
  anti_corrosion: Marine-grade anodize + conformal coat
  lens_wash: Integrated wiper + washer

physical:
  weight: <1.5 kg
  dimensions: 170 × 90 × 110 mm
  sealing: IP68 (1m submersion)  # Enhanced
  material: Marine aluminum 5083

environmental:
  operating_temp: -10°C to +55°C
  salt_fog: 500 hours
  humidity: 100% condensing

performance:
  detection_range: 300m (day), 200m (thermal)
  sea_state_operation: Up to Sea State 4
  hit_improvement: 3x (motion-compensated)

target_price: $6,500
```

### 3.6 V-SMASH-RCWS-LITE Specifications (Single-Soldier Portable)

```yaml
variant: V-SMASH-RCWS-LITE
designation: VSM-RL
status: Phase 2 Deliverable
source_re: SMASH Hopper Light Analysis
vdi_score: 83%

key_differentiator: "Can be carried, assembled and operated by a single soldier"

platform_subsystem:
  total_weight: ≤10 kg (excl. weapon)  # R100
  weapon_support: 7.62mm to 12.7mm  # R101
  setup_personnel: 1 person  # R102
  setup_time: <60 seconds  # R103

drive_subsystem:
  pan:
    range: ±120°  # Limited vs full RCWS
    speed: 20°/sec
    motor: Brushless DC servo
  tilt:
    range: -20° to +45°  # Limited
    speed: 15°/sec
    motor: Brushless DC servo
  stabilization: Passive (friction damped)  # No active gyro

deployment_subsystem:
  tripod:
    type: Folding aluminum  # R104
    height: 0.5-1.2m adjustable
    footprint: 0.8m diameter
    weight: 3 kg
  assembly: Tool-free, quick-lock
  spike_feet: Yes (soft ground)
  pad_feet: Yes (hard surface)

sensor_subsystem:
  fcs_module: V-SMASH PRO core
  video_streaming:
    resolution: 1080p
    codec: H.264
    latency: <150ms  # R97
    interface: Wired (primary)

control_subsystem:
  rcu:
    type: Wired handheld  # R105
    cable_length: 50m
    display: 5" LCD
    controls: Joystick + triggers
  wireless_backup: None (LITE version)
  external_cue: None (standalone)

power_subsystem:
  battery: Military BB-2590
  runtime: >4 hours  # R106
  voltage: 28V nominal

environmental:
  operating_temp: -10°C to +55°C  # R107
  humidity: 95% RH (tropical)
  sealing: IP65
  standards: MIL-STD-810G

performance:
  effective_range: 800m (7.62mm), 1200m (12.7mm)
  tracking: Inherited from FCS module
  hit_improvement: 3x vs manual

target_price: $8,000
local_content: 70%
```

### 3.7 V-SMASH-RCWS Specifications (Full Remote Weapon Station)

```yaml
variant: V-SMASH-RCWS
designation: VSM-R
status: Phase 3 Deliverable
source_re: SMASH Hopper 5000 Analysis
vdi_score: 74%

platform_subsystem:
  total_weight: ≤15 kg (excl. weapon)  # R92
  weapon_support: 7.62mm to 12.7mm
  mounting: Vehicle roof, fixed position

drive_subsystem:
  pan:
    range: 360° continuous  # R93
    speed: ≥40°/sec  # R95
    motor: Brushless DC servo
    encoder: 17-bit absolute
    gearbox: Harmonic drive (zero backlash)
  tilt:
    range: -30° to +70°  # R94
    speed: 30°/sec
    motor: Brushless DC servo
  stabilization:
    type: Gyro-stabilized 2-axis  # R96
    sensor: BMI088 6-axis IMU
    bandwidth: 10 Hz
    residual_jitter: <0.5 mrad RMS

sensor_subsystem:
  fcs_module: V-SMASH PRO core
  day_camera:
    type: CMOS 1080p60
    zoom: 10x optical (optional)
  thermal_camera:
    type: LWIR 640x480
    zoom: 2x digital
  video_streaming:
    resolution: 1080p
    codec: H.264
    latency: <100ms  # R97
    encryption: AES-128

control_subsystem:
  rcu:
    type: Wired + Wireless  # Dual mode
    wired_cable: 100m
    wireless_range: 300m
    display: 7" LCD ruggedized
  external_cue:
    interface: Ethernet + Serial
    protocol: Cursor on Target (CoT)  # R98
    handoff_time: <500ms
  auto_scan:
    mode: Sector scan
    sector: Configurable ±90°
    speed: 10°/sec

power_subsystem:
  input: 24-28V DC vehicle power
  consumption: 150W peak, 80W average
  battery_backup: 30 minutes (internal)

environmental:
  operating_temp: -30°C to +55°C  # R99 enhanced
  humidity: 95% RH
  sealing: IP67
  shock: MIL-STD-810G Method 516.8
  vibration: MIL-STD-810G Method 514.8

performance:
  effective_range: 1200m (12.7mm)
  slew_to_cue: <2 seconds (90°)
  tracking_accuracy: <1 mrad
  hit_improvement: 5x vs manual

target_price: $12,000
local_content: 55%
```

### 3.8 V-SMASH-DOME Specifications (Integrated C-UAS System)

```yaml
variant: V-SMASH-DOME
designation: VSM-D
status: Phase 3 Deliverable
source_re: SMASH DOME Analysis
vdi_score: 73%
configuration: Standard (with radar)

system_architecture:
  concept: Integrated detect-track-engage  # R108
  layers:
    detection: EO/IR + Radar
    tracking: Sensor fusion
    engagement: RCWS effector
  operation: Person-in-the-loop mandatory  # R111

detection_subsystem:
  eo_ir_scanner:
    type: Pan-tilt EO/IR head
    day_camera: 1080p with 20x zoom
    thermal_camera: 640x480 LWIR
    coverage: 360° continuous scan
    detection_range: 1-2 km (drone)  # R109
  radar:
    type: Drone detection radar  # R110
    range: 2-5 km
    coverage: 360° × 60°
    update_rate: 2 Hz
    micro_doppler: Yes (rotor detection)
    interface: Ethernet to fusion

processing_subsystem:
  platform: NVIDIA Jetson AGX Xavier
  detection_ai: YOLOv8-large + thermal
  classification:
    method: CNN classifier  # R112
    classes: [FPV, commercial_quad, fixed_wing, loitering_mun, bird]
    accuracy: ≥90%
  track_fusion:
    method: Track-level fusion  # R113
    max_tracks: 20
    association: Multi-hypothesis

engagement_subsystem:
  effector: V-SMASH RCWS
  engagement_range: 200-500m (kinetic)
  fire_control: SMASH AI-assisted
  pitl_interface:
    display: 15" tactical display
    overlay: Threat boxes, classification, range
    authorization: Explicit confirm required  # R111
  bda:
    method: AI track loss detection  # R114
    reporting: Automatic to C2

c2_subsystem:
  networking:
    protocol: Cursor on Target (CoT)  # R115
    transport: UDP multicast
    encryption: AES-256
    compatibility: TAK server, ATAK
  external_interface:
    radar_input: Yes (target handoff)
    higher_echelon: Battalion air defense net
  sensor_handoff: Bidirectional  # R113

physical:
  system_weight: ~50 kg (complete)
  components:
    - EO/IR scanner head: 15 kg
    - Radar unit: 20 kg (optional)
    - Processing cabinet: 10 kg
    - Cables/mounting: 5 kg
  deployment: Vehicle or fixed site
  setup_time: <30 minutes (2 persons)

power_subsystem:
  input: 220V AC or 28V DC
  consumption: 500W average
  generator_compatible: Yes
  ups_backup: 15 minutes

environmental:
  operating_temp: -20°C to +50°C
  humidity: 95% RH
  sealing: IP65 (outdoor)
  standards: MIL-STD-810G

performance:
  detection_range_eo: 2 km
  detection_range_radar: 5 km
  classification_time: <1 second
  engagement_range: 500m max
  targets_per_minute: 3-5 (kinetic)
  false_alarm_rate: <1 per hour

configurations:
  basic:
    sensors: EO/IR only
    price: $30,000
  standard:
    sensors: EO/IR + Radar
    price: $50,000
  enhanced:
    sensors: Multi-layer
    price: $80,000

target_price: $50,000 (standard)
local_content: 50%
```

### 3.9 V-SMASH-C4I-HUB Specifications (Squad Coordination)

```yaml
variant: V-SMASH-C4I-HUB
designation: VSM-C4I
status: Phase 2 Deliverable
source_re: SMASH Connectivity Analysis
vdi_score: 82%

purpose: "Enable squad-level target sharing and coordination between V-SMASH units"

connectivity:
  mesh_network:
    type: Tactical mesh radio
    frequency: 2.4 GHz / 900 MHz selectable
    range: 1-2 km (LOS)
    nodes: Up to 8 V-SMASH units
    topology: Self-forming mesh
  uplink:
    type: Optional higher echelon link
    interface: Ethernet to tactical radio
    protocol: CoT/UDP

processing:
  platform: Raspberry Pi 4 (ruggedized)
  software:
    - Track correlation
    - Sector assignment
    - Engagement deconfliction
    - Target handoff

display:
  screen: 5" sunlight readable LCD
  map_view: OpenStreetMap offline
  track_display: All friendly V-SMASH positions + shared tracks
  alerts: Priority target notification

features:
  target_sharing:
    latency: <500ms unit-to-unit
    format: CoT XML
    encryption: AES-128
  sector_management:
    assignment: Manual or auto-divide
    overlap_alert: Yes
  engagement_coordination:
    deconfliction: Prevents double-engagement
    handoff: One-button transfer
  situational_awareness:
    blue_force: All V-SMASH positions
    red_tracks: Shared hostile tracks

physical:
  weight: 0.5 kg
  dimensions: 120 × 80 × 40 mm
  sealing: IP67
  mounting: MOLLE/chest rig

power:
  battery: Internal 5000mAh
  runtime: >8 hours
  charging: USB-C

environmental:
  operating_temp: -10°C to +55°C
  humidity: 95% RH

target_price: $2,000
local_content: 75%
```

---

## 4. BILL OF MATERIALS COMPARISON

### 4.1 Complete BOM Summary (All 9 Products)

| Product | Unit Cost | Target Price | Margin | Local % |
|---------|-----------|--------------|--------|---------|
| **HANDHELD FCS** | | | | |
| LITE | $784 | $3,000 | 3.8x | 70% ✅ |
| PRO | $1,920 | $5,000 | 2.6x | 31% ⚠️ |
| PRO-X | $2,650 | $7,000 | 2.6x | 28% ⚠️ |
| **PLATFORM-MOUNTED** | | | | |
| HMG | $1,850 | $6,000 | 3.2x | 55% ⚠️ |
| MARITIME | $2,100 | $6,500 | 3.1x | 45% ⚠️ |
| RCWS-LITE | $2,800 | $8,000 | 2.9x | 70% ✅ |
| RCWS | $4,200 | $12,000 | 2.9x | 55% ⚠️ |
| **SYSTEM** | | | | |
| DOME | $18,000 | $50,000 | 2.8x | 50% ⚠️ |
| **ACCESSORY** | | | | |
| C4I HUB | $650 | $2,000 | 3.1x | 75% ✅ |

### 4.2 Detailed BOM by Category

#### Handheld FCS Products

| Category | LITE | PRO | PRO-X | Notes |
|----------|------|-----|-------|-------|
| Processing | $200 | $200 | $200 | Same Jetson Nano |
| Sensors | $60 | $960 | $1,100 | +Thermal, +LRF |
| Optics | $115 | $155 | $450 | 4x magnified optic |
| Power | $30 | $45 | $50 | Larger battery |
| Actuation | $15 | $15 | $15 | Same solenoid |
| Housing | $130 | $180 | $220 | Larger for LRF |
| LRF Module | — | — | $350 | PRO-X only |
| Misc | $34 | $40 | $45 | |
| Labor+Test | $100 | $150 | $180 | |
| Software | $100 | $175 | $200 | +LRF integration |
| **TOTAL** | **$784** | **$1,920** | **$2,650** | |

#### Platform Products

| Category | HMG | MARITIME | RCWS-LITE | RCWS |
|----------|-----|----------|-----------|------|
| FCS Core | $1,200 | $1,400 | $1,400 | $1,600 |
| Mount/Adapter | $150 | $200 | $400 | $600 |
| Motors | — | — | $300 | $800 |
| Gearbox | — | — | $100 | $400 |
| Tripod | — | — | $200 | — |
| Stabilization | — | — | — | $400 |
| Video Link | — | — | $150 | $250 |
| RCU | — | — | $300 | $500 |
| Housing | $200 | $250 | $350 | $500 |
| Marine Coat | — | $150 | — | — |
| Labor+Test | $200 | $250 | $400 | $550 |
| **TOTAL** | **$1,850** | **$2,100** | **$2,800** | **$4,200** |

#### System and Accessory

| Category | DOME | C4I HUB |
|----------|------|---------|
| RCWS Effector | $4,000 | — |
| EO/IR Scanner | $3,500 | — |
| Radar | $6,000 | — |
| Processing | $1,500 | $100 |
| Displays | $800 | $80 |
| Networking | $500 | $200 |
| Cables/Mount | $500 | $50 |
| Mesh Radio | — | $150 |
| Housing | $400 | $30 |
| Labor+Test | $1,200 | $40 |
| Software | $600 | $50 |
| **TOTAL** | **$18,000** | **$650** |

### 4.3 Local Content Analysis (All Products)

| Product | Local Value | Import Value | Local % | Target | Status |
|---------|-------------|--------------|---------|--------|--------|
| LITE | $549 | $235 | **70%** | ≥60% | ✅ Pass |
| PRO | $595 | $1,325 | **31%** | ≥60% | ⚠️ Waiver |
| PRO-X | $742 | $1,908 | **28%** | ≥60% | ⚠️ Waiver |
| HMG | $1,018 | $832 | **55%** | ≥60% | ⚠️ Close |
| MARITIME | $945 | $1,155 | **45%** | ≥60% | ⚠️ Waiver |
| RCWS-LITE | $1,960 | $840 | **70%** | ≥60% | ✅ Pass |
| RCWS | $2,310 | $1,890 | **55%** | ≥60% | ⚠️ Close |
| DOME | $9,000 | $9,000 | **50%** | ≥60% | ⚠️ Waiver |
| C4I HUB | $488 | $162 | **75%** | ≥60% | ✅ Pass |

**Local Content Summary:**
- ✅ **Pass (≥60%):** LITE, RCWS-LITE, C4I HUB (3 products)
- ⚠️ **Close (50-59%):** HMG, RCWS, DOME (3 products)
- ⚠️ **Waiver Required (<50%):** PRO, PRO-X, MARITIME (3 products)

**Mitigation Strategy:**
1. High-capability products (PRO variants, DOME) classified as "strategic capability" - waiver justified
2. Maritime-specific: Partner with VinFast/VIETTEL for local marine electronics
3. Focus local content efforts on high-volume products (LITE, RCWS-LITE)

---

## 5. DEVELOPMENT TIMELINE

### 5.1 Complete Product Roadmap

```
YEAR 1 (Months 1-12)                    YEAR 2 (Months 13-24)                 YEAR 3 (Months 25-36)
├────────────────────────────────────────┼────────────────────────────────────────┼────────────────────────┤

PHASE 1 PRODUCTS:
LITE    ═══════════════════════════════▶ PRODUCTION ════════════════════════════════════════════════════
HMG     ═══════════════════════════════▶ PRODUCTION ════════════════════════════════════════════════════

PHASE 2 PRODUCTS:
PRO     ──────────────────────────────────═══════════════════════════════════▶ PRODUCTION ═════════════
PRO-X   ──────────────────────────────────────────════════════════════════════▶ PRODUCTION ═════════════
MARITIME────────────────────────────────────════════════════════════════════════▶ PRODUCTION ═══════════
RCWS-LITE───────────────────────────────────════════════════════════════════════▶ PRODUCTION ═══════════
C4I HUB ──────────────────────────────────════════════════════════════▶ PRODUCTION ═════════════════════

PHASE 3 PRODUCTS:
RCWS    ────────────────────────────────────────────────────────────────────────════════════════════════▶
DOME    ────────────────────────────────────────────────────────────────────────════════════════════════▶

═══ = Active development    ▶ = Production start    ─── = Concept/planning
```

### 5.2 Milestone Schedule (All Products)

| Product | PDR | CDR | Prototype | Test | Production |
|---------|-----|-----|-----------|------|------------|
| **LITE** | M3 | M6 | M9 | M11 | **M12** |
| **HMG** | M3 | M6 | M9 | M11 | **M12** |
| **PRO** | M9 | M15 | M18 | M22 | **M24** |
| **PRO-X** | M12 | M18 | M21 | M23 | **M24** |
| **MARITIME** | M12 | M18 | M22 | M24 | **M26** |
| **RCWS-LITE** | M12 | M18 | M22 | M24 | **M26** |
| **C4I HUB** | M9 | M12 | M15 | M17 | **M18** |
| **RCWS** | M18 | M24 | M28 | M32 | **M34** |
| **DOME** | M18 | M24 | M30 | M34 | **M36** |

### 5.3 Development Investment by Phase

| Phase | Products | Timeline | Investment | Notes |
|-------|----------|----------|------------|-------|
| **Phase 1** | LITE, HMG | M1-12 | $400K | Core platform development |
| **Phase 2** | PRO, PRO-X, MARITIME, RCWS-LITE, C4I HUB | M13-26 | $250K | Variants and accessories |
| **Phase 3** | RCWS, DOME | M25-36 | $100K | System integration |
| **TOTAL** | 9 products | 36 months | **$750K** | |

### 5.4 Shared Development Activities

| Activity | Months | Products Benefiting | Notes |
|----------|--------|---------------------|-------|
| Core FCS algorithm | 1-6 | All 9 | Detection, tracking, ballistics |
| Jetson platform BSP | 1-4 | All 9 | Common software platform |
| YOLOv8 training | 3-9 | All 9 | C-UAS optimized dataset |
| PCB carrier board | 4-7 | LITE, PRO, PRO-X, HMG | Common electronics |
| Mechanical framework | 3-6 | Handheld variants | Shared housing design |
| MIL-STD-810 testing | 10-12 | LITE first | Results reused |
| CoT protocol stack | 9-15 | PRO, RCWS, DOME, C4I | Shared networking |
| RCWS drive system | 15-20 | RCWS-LITE, RCWS | Common motors/control |

---

## 6. TARGET MARKETS

### 6.1 Market Segmentation by Product

#### Handheld FCS Products

| Product | Primary Market | Secondary Market | Est. Volume (10yr) |
|---------|---------------|------------------|-------------------|
| **LITE** | Training, reserve forces | Export (budget) | 1,500 units |
| **PRO** | Front-line infantry, SOF | Vehicle crews | 800 units |
| **PRO-X** | Designated marksmen, snipers | Export (premium) | 200 units |

#### Platform Products

| Product | Primary Market | Secondary Market | Est. Volume (10yr) |
|---------|---------------|------------------|-------------------|
| **HMG** | Static positions, checkpoints | Vehicle pintle | 400 units |
| **MARITIME** | Patrol boats, coast guard | Island garrisons | 150 units |
| **RCWS-LITE** | Infantry rapid deployment | Expeditionary | 300 units |
| **RCWS** | APCs, MRAPs, fixed sites | Export | 150 units |

#### System and Accessory

| Product | Primary Market | Secondary Market | Est. Volume (10yr) |
|---------|---------------|------------------|-------------------|
| **DOME** | Air bases, critical sites | Naval vessels | 100 units |
| **C4I HUB** | Infantry squads | Vehicle sections | 2,500 units |

### 6.2 Complete Market Potential (10-Year Projection)

| Product | Units | Price | Revenue | Margin | Profit |
|---------|-------|-------|---------|--------|--------|
| **LITE** | 1,500 | $3,000 | $4.5M | 74% | $3.3M |
| **PRO** | 800 | $5,000 | $4.0M | 62% | $2.5M |
| **PRO-X** | 200 | $7,000 | $1.4M | 62% | $0.9M |
| **HMG** | 400 | $6,000 | $2.4M | 69% | $1.7M |
| **MARITIME** | 150 | $6,500 | $1.0M | 68% | $0.7M |
| **RCWS-LITE** | 300 | $8,000 | $2.4M | 65% | $1.6M |
| **RCWS** | 150 | $12,000 | $1.8M | 65% | $1.2M |
| **DOME** | 100 | $50,000 | $5.0M | 64% | $3.2M |
| **C4I HUB** | 2,500 | $2,000 | $5.0M | 68% | $3.4M |
| **TOTAL** | **6,100** | — | **$27.5M** | **67%** | **$18.5M** |

### 6.3 Revenue by Category

```
REVENUE DISTRIBUTION (10-Year)
═══════════════════════════════════════════════════════════════

Handheld FCS:        $9.9M  (36%) ████████████████░░░░░░░░░░░░░░░
Platform-Mounted:    $7.6M  (28%) ████████████░░░░░░░░░░░░░░░░░░░
Integrated System:   $5.0M  (18%) ████████░░░░░░░░░░░░░░░░░░░░░░░
Accessories:         $5.0M  (18%) ████████░░░░░░░░░░░░░░░░░░░░░░░
────────────────────────────────────────────────────────────────
TOTAL:              $27.5M (100%)
```

### 6.4 Export Potential

| Product | Export Appeal | Target Countries | Export Volume |
|---------|---------------|------------------|---------------|
| LITE | High (price) | ASEAN, Africa | 300 units |
| PRO | Medium | Select ASEAN | 100 units |
| RCWS-LITE | High (unique) | ASEAN, Middle East | 100 units |
| DOME | Low (complex) | Partner countries | 10 units |

**Total Export Potential:** 500+ units, ~$3M revenue

---

## 7. UPGRADE PATH

### 7.1 LITE to PRO Field Upgrade

**Feasibility:** ⚠️ **Limited** - Requires significant modification

| Component | Upgrade Difficulty | Cost | Notes |
|-----------|-------------------|------|-------|
| Thermal sensor | Medium | $900 | Requires housing mod |
| HDR sensor | High | $100 | PCB rework |
| Battery pack | Easy | $20 | Drop-in replacement |
| Lens heater | Medium | $50 | Wiring addition |
| IP67 seals | Medium | $30 | Gasket replacement |
| Software | Easy | $0 | OTA update |
| **TOTAL** | | **~$1,100** | Plus labor |

**Recommendation:** Due to upgrade complexity, recommend **purchasing PRO** rather than upgrading LITE. Offer trade-in program ($500 credit for LITE toward PRO purchase).

### 7.2 Future Variants (Roadmap)

| Variant | Target | Key Features | Timeline | Status |
|---------|--------|--------------|----------|--------|
| V-SMASH-LITE+ | $3,500 | LITE + HDR sensor | Month 18 | Planned |
| V-SMASH-PRO-LR | $8,000 | PRO + 4x zoom + LRF | Month 30 | Planned |
| V-SMASH-RWS | $15,000 | RCWS + MTB-20 full integration | Month 36 | Concept |
| **V-SMASH-SWARM** | **$12,000** | **10-track + mesh + AI coordination** | **Month 42** | **Concept** |

#### 7.2.1 V-SMASH-LITE+ (Enhanced Entry-Level)

```yaml
variant: V-SMASH-LITE+
designation: VSM-L+
status: Planned (Month 18)
concept: "LITE with HDR sensor for improved low-light performance"

upgrades_from_lite:
  sensor: Sony IMX462 (HDR 85dB) replacing IMX290 (65dB)
  low_light: 0.01 lux (vs 0.1 lux)
  varying_light: 95% detection (vs 85%)

unchanged_from_lite:
  - No thermal sensor
  - Same Kalman tracking (1.5g)
  - Same multi-target (5 tracks, NN)
  - Same form factor

target_market:
  - Budget-conscious units needing dawn/dusk capability
  - LITE upgrade path (sensor swap)
  - Export markets

unit_cost: $834 (+$50 sensor)
target_price: $3,500
margin: 4.2x
```

#### 7.2.2 V-SMASH-PRO-LR (Long Range)

```yaml
variant: V-SMASH-PRO-LR
designation: VSM-PLR
status: Planned (Month 30)
concept: "PRO with extended range capability for designated marksmen"

upgrades_from_pro:
  optic:
    magnification: 6x variable (vs 1x)
    fov: 4° (magnified)
  lrf:
    range: 1200m (vs none on PRO)
    accuracy: ±0.5m
  detection_range: 600m drone (vs 300m)
  effective_range: 800m (vs 400m)

differences_from_prox:
  - Higher magnification (6x vs 4x)
  - Better LRF (1200m vs 800m)
  - Longer eye relief for prone shooting
  - Includes thermal (PRO-X thermal optional)

target_market:
  - Designated marksmen
  - Sniper teams (spotter role)
  - Long-range C-UAS defense

unit_cost: $3,200
target_price: $8,000
margin: 2.5x
```

#### 7.2.3 V-SMASH-RWS (Remote Weapon Station - MTB-20 Integrated)

```yaml
variant: V-SMASH-RWS
designation: VSM-RWS
status: Concept (Month 36)
concept: "Full integration with MTB-20 RCWS for Vietnamese military vehicles"

system_integration:
  platform: MTB-20 Remote Weapon Station
  weapons: [12.7mm NSV, 14.5mm KPV, 7.62mm PKM, 40mm AGL]
  interface: Direct electronic trigger, shared power
  control: Unified operator console

differences_from_rcws:
  - MTB-20 specific mounting (vs generic)
  - Shared vehicle power (vs standalone)
  - Integrated with existing MTB-20 controls
  - Vietnam Army type-certified

capabilities:
  pan_range: 360° continuous
  tilt_range: -10° to +60°
  slew_rate: 60°/sec (MTB-20 drives)
  stabilization: MTB-20 gyro-stabilized platform
  video: Integrated with vehicle displays

target_market:
  - Vietnam Army vehicle fleet modernization
  - MTB-20 equipped APCs and trucks
  - New vehicle procurements

unit_cost: $5,500 (FCS module only, MTB-20 separate)
target_price: $15,000 (complete upgrade kit)
margin: 2.7x

dependencies:
  - MTB-20 manufacturer partnership
  - Vehicle integration testing
  - Type certification
```

#### 7.2.4 V-SMASH-SWARM (Advanced Multi-Target)

```yaml
variant: V-SMASH-SWARM
designation: VSM-SW
status: Concept (Month 42)
concept: "Advanced swarm defense with AI-coordinated multi-unit engagement"

advanced_capabilities:
  multi_target:
    max_tracks: 10 (vs 5 standard)
    track_pool: Dynamic allocation
    association: Multi-hypothesis tracking (MHT)

  swarm_defense:
    threat_classification: AI swarm pattern recognition
    engagement_priority: Predictive threat modeling
    coordination: Multi-unit sector division

  networking:
    mesh: Tactical mesh (8+ units)
    latency: <100ms unit-to-unit
    protocol: Enhanced CoT with track fusion
    encryption: AES-256 + frequency hopping

  ai_coordination:
    sector_management: Automatic division
    target_handoff: Predictive (before track loss)
    deconfliction: Real-time engagement coordination
    swarm_response: Coordinated sector saturation

processing:
  platform: NVIDIA Jetson Xavier NX (upgraded)
  ai_model: Custom swarm detection CNN
  track_fusion: Distributed Kalman fusion

target_market:
  - Critical infrastructure defense
  - Forward operating bases
  - Naval vessel close-in defense
  - High-value asset protection

unit_cost: $4,500
target_price: $12,000
margin: 2.7x

development_risk: HIGH
  - Requires mesh networking validation
  - AI swarm detection training data
  - Multi-unit coordination testing
  - Potential ITAR/export restrictions

dependencies:
  - C4I HUB platform maturity
  - Swarm attack training data collection
  - Multi-unit field trials
```

#### 7.2.5 Future Variants Development Roadmap

```
FUTURE VARIANTS TIMELINE (Month 18-48)
═══════════════════════════════════════════════════════════════════════════

M18         M24         M30         M36         M42         M48
│           │           │           │           │           │
├───────────┼───────────┼───────────┼───────────┼───────────┼───────────▶

LITE+       ══════════▶ PRODUCTION
            │ Dev │Test│

                        PRO-LR      ══════════▶ PRODUCTION
                        │   Dev    │   Test   │

                                    RWS         ══════════════▶ PRODUCTION
                                    │ MTB-20 Integration │Test│

                                                SWARM       ══════════════▶
                                                │  AI Dev  │ Field Test │

LEGEND: ══ Development    ▶ Production Start
```

#### 7.2.6 Future Variants Summary

| Variant | Base | Key Addition | NRE | Volume Est. | Revenue Est. |
|---------|------|--------------|-----|-------------|--------------|
| LITE+ | LITE | HDR sensor | $30K | 500 units | $1.75M |
| PRO-LR | PRO | 6x optic + LRF | $80K | 150 units | $1.2M |
| RWS | RCWS | MTB-20 integration | $150K | 200 units | $3.0M |
| SWARM | PRO | 10-track + mesh AI | $200K | 100 units | $1.2M |
| **TOTAL** | | | **$460K** | **950 units** | **$7.15M** |

**Total Future Portfolio (10-year):**
- Current 9 products: $27.5M
- Future 4 variants: $7.15M
- **Combined: $34.65M**

### 7.3 Multi-Target Software Upgrade (NEW v1.1)

**LITE → Enhanced Multi-Target (Software Only):**

| Feature | LITE Base | LITE + MT Upgrade | Notes |
|---------|-----------|-------------------|-------|
| Data association | Nearest-Neighbor | **Hungarian** | OTA update |
| Threat priority | Distance-based | **Multi-factor** | Config file |
| Engagement queue | None | **FIFO queue** | Software |
| **Upgrade Cost** | — | **$200** | License fee |

**Note:** LITE hardware supports enhanced multi-target algorithms. Software upgrade available for customers requiring improved clutter performance without full PRO capability.

---

## 8. DECISION SUMMARY

### 8.1 Approved Product Family (9 Products)

| Product | Specification | Price | Delivery | Local % | VDI Score |
|---------|---------------|-------|----------|---------|-----------|
| **LITE** | ✅ §3.1 | $3,000 | M12 | 70% ✅ | 88% |
| **PRO** | ✅ §3.2 | $5,000 | M24 | 31% ⚠️ | 79% |
| **PRO-X** | ✅ §3.3 | $7,000 | M24 | 28% ⚠️ | 76% |
| **HMG** | ✅ §3.4 | $6,000 | M12 | 55% ⚠️ | 81% |
| **MARITIME** | ✅ §3.5 | $6,500 | M26 | 45% ⚠️ | 75% |
| **RCWS-LITE** | ✅ §3.6 | $8,000 | M26 | 70% ✅ | 83% |
| **RCWS** | ✅ §3.7 | $12,000 | M34 | 55% ⚠️ | 74% |
| **DOME** | ✅ §3.8 | $50,000 | M36 | 50% ⚠️ | 73% |
| **C4I HUB** | ✅ §3.9 | $2,000 | M18 | 75% ✅ | 82% |

### 8.2 Strategic Decisions

| Decision | Outcome |
|----------|---------|
| Product Strategy | ✅ Multi-tier platform family (9 products) |
| Development Investment | ✅ $750K over 36 months |
| Revenue Target (10-year) | ✅ $27.5M TAM |
| Phase 1 Products | ✅ LITE, HMG (Month 12) |
| Local Content Policy | ✅ 3 products meet ≥60%, 6 products with waiver |
| DOME Enhanced | ❌ Deferred (VDI 55%, requires radar partner) |

### 8.3 Open Items

| Item | Owner | Due | Status |
|------|-------|-----|--------|
| MoD approval for 9-product family | Program Office | Week 2 | Pending |
| Local content waiver (6 products) | Program Office | Week 3 | Pending |
| Thermal sensor procurement | Procurement | Week 4 | Not started |
| Phase 1 kickoff (LITE, HMG) | Engineering | Week 2 | Ready |
| Radar partner identification (DOME) | Business Dev | Month 6 | Not started |
| RCWS motor supplier qualification | Procurement | Month 3 | Not started |

---

## 9. PRODUCT FAMILY SUMMARY

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    V-SMASH PRODUCT FAMILY v2.1                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  CURRENT PRODUCTS:   9 variants (approved)                                 ║
║  FUTURE VARIANTS:    4 variants (planned/concept)                          ║
║  PRICE RANGE:        $2,000 - $50,000                                      ║
║                                                                            ║
║  ─────────────────── CURRENT (9 PRODUCTS) ───────────────────             ║
║  DEVELOPMENT:        $750K over 36 months                                  ║
║  REVENUE (10yr):     $27.5M                                                ║
║                                                                            ║
║  PHASE 1 (M1-12):    LITE, HMG                 → $400K investment         ║
║  PHASE 2 (M13-26):   PRO, PRO-X, MARITIME,     → $250K investment         ║
║                      RCWS-LITE, C4I HUB                                    ║
║  PHASE 3 (M25-36):   RCWS, DOME                → $100K investment         ║
║                                                                            ║
║  ─────────────────── FUTURE (4 VARIANTS) ───────────────────              ║
║  DEVELOPMENT:        $460K over M18-48                                     ║
║  REVENUE (10yr):     $7.15M                                                ║
║                                                                            ║
║  M18: LITE+          Enhanced entry-level      → $30K NRE                 ║
║  M30: PRO-LR         Long-range marksman       → $80K NRE                 ║
║  M36: RWS            MTB-20 integration        → $150K NRE                ║
║  M42: SWARM          AI swarm defense          → $200K NRE                ║
║                                                                            ║
║  ─────────────────── TOTAL PORTFOLIO ───────────────────                  ║
║  PRODUCTS:           13 variants (9 current + 4 future)                    ║
║  INVESTMENT:         $1.21M total                                          ║
║  REVENUE (10yr):     $34.65M                                               ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-04 | Initial release - Two-tier product specification (LITE, PRO) |
| 1.1 | 2026-02-04 | Multi-target update from ARCAS RE: Added multi-target subsystem specs |
| 2.0 | 2026-02-04 | Major expansion to 9-product family: Added PRO-X, HMG, MARITIME, RCWS-LITE, RCWS, DOME, C4I HUB specifications (§3.3-3.9). Updated BOM for all products, market analysis ($27.5M TAM), development timeline (36 months, $750K). |
| **2.1** | **2026-02-04** | **Future variants roadmap expansion (§7.2): Added detailed specifications for LITE+ ($3.5K), PRO-LR ($8K), RWS ($15K), SWARM ($12K). Added development timeline M18-48, NRE estimates ($460K), revenue projections ($7.15M). Total portfolio potential now $34.65M.** |

---

*Related Documents:*
- [[V-SMASH_P0_01_ODI_analysis|ODI Analysis v1.1]]
- [[V-SMASH_P1_01_requirements_list|Requirements List v1.5]]
- [[V-SMASH_P2_02_morphological_matrix|Morphological Matrix v1.3]]
- [[V-SMASH_P2_03_concept_evaluation|Concept Evaluation v1.4]]
- [[V-SMASH_P2_06_product_portfolio_v2|Product Portfolio v3.0]]
- [[V-SMASH_00_project_brief|Project Brief]]

*RE Sources:*
- [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+]] - Core FCS
- [[V-SMASH_RE_02_ARCAS_analysis|ARCAS]] - Multi-target
- [[V-SMASH_RE_05_SMASHX4_analysis|SMASH X4]] - PRO-X
- [[V-SMASH_RE_06_SMASH_connectivity_analysis|Connectivity]] - HMG, C4I
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|Hopper 5000]] - RCWS
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light]] - RCWS-LITE
- [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME]] - DOME

