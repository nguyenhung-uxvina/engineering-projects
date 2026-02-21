---
project: V-SMASH
phase: 2
type: product_portfolio
version: 3.0
created: 2026-02-04
updated: 2026-02-04
status: proposed
strategy: multi-tier platform family
---

# V-SMASH PRODUCT PORTFOLIO v3.0
## Vietnam-Specialized Fire Control System Family

**Document ID:** V-SMASH_P2_06
**Date:** 2026-02-04
**Source:** 10 RE Analyses + Vietnam Defense Requirements
**Status:** Proposed for Stakeholder Review

---

## 1. EXECUTIVE SUMMARY

### 1.1 RE Analysis Synthesis

Based on comprehensive reverse engineering of **10 foreign systems**, we propose an expanded **9-product portfolio** specialized for Vietnam's defense needs:

```
RE ANALYSIS → V-SMASH PRODUCT MAPPING
══════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────┐
│                   10 FOREIGN SYSTEMS ANALYZED                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  HANDHELD FCS:                                                       │
│  SMASH 2000+     ARCAS         ARBEL        SMASH 3000   SMASH X4  │
│  ───────────     ─────         ─────        ──────────   ────────  │
│  • Core FCS      • Multi-tgt   • C-UAS AI   • Lightweight • 4x mag │
│  • Human-loop    • AR display  • Fusion     • 72h battery • LRF    │
│  • Fail-safe     • C4I link    • Drone-opt  • Mesh net    • Etched │
│                                                                      │
│  PLATFORM/SYSTEM:                                                    │
│  SMASH Hopper    Hopper Light  SMASH DOME   SMASH Dragon           │
│  ────────────    ────────────  ──────────   ────────────           │
│  • 15kg RCWS     • 10kg ultra  • Integrated • Armed UAV            │
│  • 360° pan      • Single-man  • C-UAS sys  • Airborne FCS         │
│  • 40°/sec slew  • Portable    • Radar+FCS  • Future cap           │
│                                                                      │
│  CONNECTIVITY: MAGTAB/ATAK, HMG, UGV integration                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│              V-SMASH PRODUCT FAMILY (9 VARIANTS)                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  HANDHELD FCS                  PLATFORM-MOUNTED                     │
│  ────────────                  ────────────────                     │
│  V-SMASH LITE      $3,000      V-SMASH HMG       $6,000            │
│  V-SMASH PRO       $5,000      V-SMASH MARITIME  $6,500            │
│  V-SMASH PRO-X     $7,000      V-SMASH RCWS-LITE $8,000   ← NEW    │
│                                V-SMASH RCWS      $12,000           │
│                                                                      │
│  SYSTEM                        ACCESSORIES                          │
│  ──────                        ───────────                          │
│  V-SMASH DOME      $50,000     V-SMASH C4I HUB   $2,000            │
│  (Integrated C-UAS) ← NEW                                           │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Vietnam Defense Context

| Factor | Vietnam Requirement | V-SMASH Response |
|--------|---------------------|------------------|
| **Primary Threat** | FPV drones, loitering munitions | C-UAS optimized AI (R68) |
| **Key Platform** | 12.7mm HMG (NSV, DShK) | V-SMASH HMG variant |
| **Maritime** | South China Sea, patrol boats | V-SMASH MARITIME (IP68) |
| **Budget** | Cost-sensitive procurement | Tiered pricing ($3K-$12K) |
| **Local Content** | ≥60% requirement | 60-75% achieved |
| **C4I** | Vietnamese BMS integration | Open CoT protocol |
| **Climate** | Tropical (humid, hot, salt) | Enhanced environmental |

### 1.3 Portfolio Summary

| Variant | Role | Price | Weight | Key Feature | Source RE |
|---------|------|-------|--------|-------------|-----------|
| **LITE** | Training/Reserve | $3,000 | 1.0kg | Entry-level C-UAS | SMASH 2000+ |
| **PRO** | Operational 24/7 | $5,000 | 1.3kg | Thermal fusion | ARBEL |
| **PRO-X** | Extended Range | $7,000 | 1.5kg | 4x + LRF | SMASH X4 |
| **HMG** | Heavy Weapon | $6,000 | 1.8kg | 12.7mm mount | SMASH Conn |
| **MARITIME** | Naval/Coastal | $6,500 | 1.5kg | IP68 + salt fog | Vietnam-specific |
| **RCWS-LITE** | Infantry RCWS | $8,000 | 10kg | Single-soldier | Hopper Light |
| **RCWS** | Remote Station | $12,000 | 15kg | Full 360° C2 | SMASH Hopper |
| **DOME** | Integrated C-UAS | $50,000 | 50kg | Detect-track-engage | SMASH DOME |
| **C4I HUB** | Command | $2,000 | 0.5kg | Squad coordination | SMASH Conn |

---

## 2. PRODUCT FAMILY ARCHITECTURE

### 2.1 Platform Commonality Strategy

```
V-SMASH PLATFORM ARCHITECTURE
══════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────┐
                    │     COMMON CORE MODULE       │
                    │                              │
                    │  • Jetson Nano compute       │
                    │  • YOLOv8-nano detection     │
                    │  • Kalman/IMM tracking       │
                    │  • Multi-target (5 tracks)   │
                    │  • Fire control logic        │
                    │  • CoT networking stack      │
                    │                              │
                    │  Est. Cost: $300             │
                    │  80% shared across variants  │
                    └─────────────┬───────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
          ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  SENSOR MODULE  │    │  OPTIC MODULE   │    │ INTERFACE MODULE│
│                 │    │                 │    │                 │
│ A: CMOS only    │    │ A: 1x reflex    │    │ A: Picatinny    │
│ B: CMOS+Thermal │    │ B: 4x magnified │    │ B: HMG bracket  │
│ C: CMOS+Thermal │    │ C: 1x + stabilized│  │ C: RCWS mount   │
│    +HDR         │    │                 │    │ D: Naval rail   │
└─────────────────┘    └─────────────────┘    └─────────────────┘

VARIANT CONFIGURATION MATRIX:
┌──────────┬────────┬────────┬───────────┐
│ Variant  │ Sensor │ Optic  │ Interface │
├──────────┼────────┼────────┼───────────┤
│ LITE     │   A    │   A    │    A      │
│ PRO      │   B    │   A    │    A      │
│ PRO-X    │   C    │   B    │    A      │
│ HMG      │   B    │   A    │    B      │
│ MARITIME │   C    │   C    │    D      │
│ RCWS     │   C    │   A    │    C      │
└──────────┴────────┴────────┴───────────┘
```

### 2.2 Software Architecture

```
V-SMASH SOFTWARE STACK
══════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌────────────┐│
│  │ Detection   │ │ Tracking    │ │ Ballistics  │ │ Fire Ctrl  ││
│  │ (YOLOv8)    │ │ (Kalman/IMM)│ │ (3DOF)      │ │ (Gate)     ││
│  └─────────────┘ └─────────────┘ └─────────────┘ └────────────┘│
│                                                                  │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌────────────┐│
│  │ Multi-Tgt   │ │ Sensor      │ │ C4I/CoT     │ │ Display    ││
│  │ Manager     │ │ Fusion      │ │ Network     │ │ Overlay    ││
│  └─────────────┘ └─────────────┘ └─────────────┘ └────────────┘│
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│                    FEATURE FLAGS (Per Variant)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LITE:    Detection ✓ | Kalman ✓ | Basic Ballistics ✓           │
│                                                                  │
│  PRO:     + Thermal Fusion ✓ | IMM ✓ | Hungarian ✓ | CoT ✓      │
│                                                                  │
│  PRO-X:   + LRF Input ✓ | Wind Comp ✓ | Cant Comp ✓             │
│                                                                  │
│  HMG:     + Recoil Compensation ✓ | Extended Ballistics ✓       │
│                                                                  │
│  MARITIME:+ Motion Stabilization ✓ | Horizon Lock ✓             │
│                                                                  │
│  RCWS:    + Remote Control ✓ | Auto-Scan ✓ | Video Stream ✓     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. PRODUCT SPECIFICATIONS

### 3.1 V-SMASH LITE (Entry-Level)

```yaml
product: V-SMASH-LITE
code: VSM-L
role: Training, Reserve Units, Daylight C-UAS
target_price: $3,000
delivery: Month 12

re_source: SMASH 2000+ (core mechanism)

specifications:
  sensor:
    primary: Sony IMX290 (CMOS 1080p60, 65dB)
    thermal: None (NV clip-on compatible)
    imu: BMI160 6-axis

  processing:
    compute: Jetson Nano 4GB
    detection: YOLOv8-nano INT8
    tracking: Kalman Filter (1.5g maneuver)
    multi_target: 5 tracks, Nearest-Neighbor

  optics:
    magnification: 1x reflex
    fov: 15°
    backup: None

  networking:
    c4i: None
    bluetooth: None
    video_out: USB recording only

  physical:
    weight: <1.0 kg
    dimensions: 150×80×100 mm
    sealing: IP65
    mount: Picatinny MIL-STD-1913

  power:
    battery: 6800mAh (2×18650)
    runtime: >10 hours
    consumption: 4W average

  performance:
    detection_range: 300m (drone, day)
    hit_improvement: 3x vs iron sights
    false_positive: <10%

target_users:
  - Military training schools
  - Reserve/militia units
  - Daylight patrol missions
  - Budget-constrained units

local_content: 75%
```

### 3.2 V-SMASH PRO (Operational)

```yaml
product: V-SMASH-PRO
code: VSM-P
role: Front-line Infantry, 24/7 Operations
target_price: $5,000
delivery: Month 18

re_source: ARBEL (sensor fusion), ARCAS (multi-target), SMASH 3000 (networking)

specifications:
  sensor:
    primary: Sony IMX462 (CMOS 1080p60, 85dB HDR)
    thermal: FLIR Lepton 3.5 (160×120, LWIR)
    imu: BMI160 6-axis
    fusion: Weighted blend (70/30 day, 30/70 night)

  processing:
    compute: Jetson Nano 4GB
    detection: YOLOv8-nano + C-UAS training (R68)
    tracking: IMM Filter (3g maneuver)
    multi_target: 5 tracks, Hungarian algorithm
    prioritization: Multi-factor AI (distance, speed, heading)

  optics:
    magnification: 1x reflex
    fov: 15°
    lens_heater: 2W (anti-fog)
    backup: None

  networking:
    c4i: Cursor on Target (CoT) protocol
    bluetooth: BLE 5.0 (tablet link)
    encryption: AES-256
    video_out: H.264 stream (WiFi optional)

  physical:
    weight: <1.3 kg
    dimensions: 170×90×110 mm
    sealing: IP67
    mount: Picatinny MIL-STD-1913

  power:
    battery: 10200mAh (3×18650)
    runtime: >6 hours
    consumption: 8W average

  performance:
    detection_range_day: 300m (drone)
    detection_range_night: 200m (thermal)
    hit_improvement: 4x vs iron sights
    false_positive: <5%
    c4i_latency: <100ms

target_users:
  - Front-line infantry battalions
  - Special operations forces
  - Quick reaction forces
  - Border defense units

local_content: 60%
```

### 3.3 V-SMASH PRO-X (Extended Range) - NEW

```yaml
product: V-SMASH-PRO-X
code: VSM-PX
role: Designated Marksman, Extended Range Engagement
target_price: $7,000
delivery: Month 24

re_source: SMASH X4 (magnification, LRF, enhanced ballistics)

specifications:
  sensor:
    primary: Sony IMX462 (CMOS 1080p60, 85dB HDR)
    thermal: FLIR Lepton 3.5 (160×120, LWIR)
    lrf: Optional Class 1 laser (500-1000m)
    imu: BMI270 (higher precision)

  processing:
    compute: Jetson Nano 4GB
    detection: YOLOv8-nano + C-UAS training
    tracking: IMM Filter (3g maneuver)
    ballistics: Enhanced 3DOF (wind, cant, inclination)
    multi_target: 5 tracks, Hungarian algorithm

  optics:
    magnification: 4x fixed (40mm objective)
    fov: 8°
    lens_heater: 2W (anti-fog)
    backup: Etched glass reticle (battery-free)
    diopter: Adjustable -3 to +3

  ballistic_compensation:
    wind: Manual input (0-30 m/s)
    inclination: Auto (±60°)
    cant: Auto (±15°)
    temperature: Auto-compensated

  networking:
    c4i: CoT protocol
    bluetooth: BLE 5.0
    encryption: AES-256

  physical:
    weight: <1.5 kg
    dimensions: 210×95×90 mm
    sealing: IP67
    mount: Picatinny MIL-STD-1913

  power:
    battery: 10200mAh (3×18650)
    runtime: >5 hours (LRF active)
    consumption: 10W average

  performance:
    detection_range_day: 500m (drone)
    detection_range_night: 300m (thermal)
    engagement_range: 400-600m
    hit_improvement: 5x vs iron sights
    lrf_accuracy: ±1m @ 500m

target_users:
  - Designated marksman teams
  - Sniper support elements
  - Long-range C-UAS defense
  - HVT protection details

local_content: 55%
```

### 3.4 V-SMASH HMG (Heavy Machine Gun) - NEW

```yaml
product: V-SMASH-HMG
code: VSM-H
role: 12.7mm Heavy Machine Gun Fire Control
target_price: $6,000
delivery: Month 20

re_source: SMASH Connectivity (HMG support, DSEI 2025), SMASH 3000

specifications:
  sensor:
    primary: Sony IMX462 (HDR)
    thermal: FLIR Lepton 3.5
    imu: BMI270 (high-g rated)

  processing:
    compute: Jetson Nano 4GB
    detection: YOLOv8-nano + C-UAS
    tracking: IMM Filter (3g maneuver)
    ballistics: 12.7mm specific (NSV, DShK, M2 profiles)
    recoil_compensation: Active prediction

  optics:
    magnification: 1x reflex (wide FOV)
    fov: 20° (extended for HMG)
    lens_heater: 3W (heavy duty)
    backup: None (manual backup sight)

  physical:
    weight: <1.8 kg
    dimensions: 180×100×120 mm
    sealing: IP67
    mount: Heavy-duty bracket (NSV/DShK/M2 compatible)
    vibration: MIL-STD-810H enhanced (12.7mm recoil)
    shock: 500g peak (firing shock)

  ballistic_profiles:
    - NSV 12.7×108mm (API-B32, B-32)
    - DShK 12.7×108mm
    - M2 12.7×99mm (.50 BMG)
    - Customizable via USB

  networking:
    c4i: CoT protocol
    bluetooth: BLE 5.0
    vehicle_bus: CAN (MTB-20 compatible)

  performance:
    detection_range: 500m (drone)
    engagement_range: 400m (drone), 800m (ground)
    hit_improvement: 4x vs manual
    burst_optimization: 3-5 round burst control

target_users:
  - Infantry heavy weapons platoons
  - Vehicle-mounted HMG crews (BTR, M113)
  - Fixed defensive positions
  - Checkpoint security

target_platforms:
  - NSV 12.7mm (primary)
  - DShK 12.7mm
  - M2 Browning .50 cal
  - KORD 12.7mm

local_content: 62%
```

### 3.5 V-SMASH MARITIME (Naval/Coastal) - NEW

```yaml
product: V-SMASH-MARITIME
code: VSM-M
role: Naval Patrol, Coastal Defense
target_price: $6,500
delivery: Month 24

re_source: Vietnam-specific requirement (South China Sea defense)

specifications:
  sensor:
    primary: Sony IMX462 (HDR)
    thermal: FLIR Lepton 3.5
    imu: BMI270 + external horizon reference

  processing:
    compute: Jetson Nano 4GB
    detection: YOLOv8-nano + maritime training set
    tracking: IMM Filter + motion stabilization
    sea_state: Compensate up to Sea State 4

  optics:
    magnification: 1x stabilized reflex
    fov: 15°
    horizon_lock: Electronic stabilization
    lens_protection: Hydrophobic coating + wiper

  environmental:
    sealing: IP68 (submersible 1m/30min)
    salt_fog: MIL-STD-810H Method 509.7
    corrosion: Marine-grade anodizing
    humidity: 100% RH continuous

  physical:
    weight: <1.5 kg
    dimensions: 175×95×115 mm
    mount: Naval rail adapter (Picatinny to NATO STANAG)
    material: 316L stainless steel housing

  networking:
    c4i: CoT protocol
    bluetooth: BLE 5.0
    ship_integration: RS-422 (bridge system)

  performance:
    detection_range: 400m (small boat), 300m (drone)
    stabilization: ±5° pitch/roll compensation
    sea_state_limit: Sea State 4 (1.25-2.5m waves)

target_users:
  - Coast Guard patrol boats
  - Navy fast attack craft
  - Island garrison forces
  - Offshore platform security

target_platforms:
  - Patrol boat deck guns
  - Naval 12.7mm mounts
  - Island defense positions
  - Oil platform security

local_content: 58%
```

### 3.6 V-SMASH RCWS (Remote Weapon Station) - NEW

```yaml
product: V-SMASH-RCWS
code: VSM-R
role: Remote Controlled Weapon Station
target_price: $12,000
delivery: Month 30

re_source: SMASH Hopper (15kg LRCWS), SMASH Connectivity

specifications:
  system:
    type: Light Remote Controlled Weapon Station
    weight: <18 kg (complete system)
    weapons: 5.56mm to 12.7mm

  sensor_head:
    primary: Sony IMX462 (HDR)
    thermal: FLIR Boson 320 (higher resolution)
    laser: Class 1 LRF (1000m)
    illuminator: IR LED (optional)

  processing:
    compute: Jetson Xavier NX (upgraded)
    detection: YOLOv8-medium
    tracking: IMM Filter
    auto_scan: 360° continuous
    target_handoff: From external sensors

  mechanical:
    pan: 360° continuous
    tilt: -20° to +60°
    slew_rate: 60°/s
    accuracy: 0.1° pointing
    stabilization: 2-axis gyro-stabilized

  control:
    wired: 100m cable (ruggedized)
    wireless: Encrypted RF (500m)
    video: H.264/265 1080p30
    latency: <100ms (control loop)

  physical:
    weight: 18kg (without weapon)
    dimensions: 400×300×350 mm
    sealing: IP67
    mounting: Tripod, mast, vehicle, static

  c4i_integration:
    protocol: CoT + custom extensions
    external_sensors: Radar cue input
    bms: Vietnamese BMS compatible
    video: RTSP streaming

  modes:
    manual: Full operator control
    assisted: AI track, operator fire
    auto_track: AI track + alert
    sentry: Auto-scan + alert (no auto-fire)

  performance:
    detection_range: 800m (vehicle), 500m (drone)
    engagement_range: 600m (effective)
    reaction_time: <3s (target cue to track)

target_users:
  - Vehicle commanders (MTB-20)
  - Base defense units
  - Checkpoint security
  - Border surveillance posts

target_platforms:
  - MTB-20 RCWS (primary)
  - BTR-series APCs
  - Fixed defensive positions
  - Border surveillance towers

local_content: 45%
```

### 3.7 V-SMASH RCWS-LITE (Single-Soldier) - NEW

```yaml
product: V-SMASH-RCWS-LITE
code: VSM-RL
role: Infantry Squad Ultra-Light Remote Weapon Station
target_price: $8,000
delivery: Month 26

re_source: SMASH Hopper Light (single-soldier portable RCWS)

specifications:
  system:
    type: Ultra-Light Remote Controlled Weapon Station
    weight: <10 kg (without weapon)
    total_weight: <15 kg (with M16 + ammo)
    weapons: 5.56mm (M16, Galil)
    crew: Single soldier (carry, setup, operate)

  sensor_head:
    primary: Sony IMX462 (HDR)
    thermal: FLIR Lepton 3.5 (160×120)
    imu: BMI270 6-axis
    laser: None (weight optimization)

  processing:
    compute: Jetson Nano 4GB
    detection: YOLOv8-nano + C-UAS
    tracking: IMM Filter (3g maneuver)
    multi_target: 5 tracks
    auto_scan: 270° sector scan

  mechanical:
    pan: 270° (adjustable limits)
    tilt: -20° to +60°
    slew_rate: 25°/s (compact motors)
    accuracy: 0.2° pointing
    tripod: Folding legs (included)

  control:
    wired: 50m tether (primary)
    wireless: Optional BLE (short range)
    video: H.264 720p30
    latency: <150ms (control loop)

  physical:
    weight: 10kg (without weapon)
    dimensions: 300×250×300 mm (folded)
    sealing: IP65
    mounting: Integrated folding tripod
    transport: Backpack compatible

  power:
    battery: LiFePO4 14.8V 10Ah
    runtime: >2 hours (standalone)
    vehicle_power: 24V input (optional)
    consumption: 25W average

  modes:
    manual: Full operator control
    assisted: AI track, operator fire
    sentry: Auto-scan + alert (no auto-fire)

  performance:
    detection_range: 400m (drone), 500m (ground)
    engagement_range: 300m (5.56mm effective)
    setup_time: <3 minutes
    displacement_time: <2 minutes
    reaction_time: <5s (target cue to track)

target_users:
  - Infantry squad overwatch
  - Patrol base security
  - Temporary defensive positions
  - Covert ambush operations
  - Border patrol units

target_scenarios:
  - Jungle patrol (backpack carry)
  - Mountain positions (light transport)
  - Island outposts (limited logistics)
  - Squad rest security (one-man operation)

local_content: 55%

vietnam_advantages:
  - Jungle/mountain terrain (light, portable)
  - Single-soldier operation (reduces manpower)
  - M16/Galil compatible (VN inventory)
  - Low cost vs Hopper Light ($8K vs ~$50K)
```

### 3.8 V-SMASH DOME (Integrated C-UAS System) - NEW

```yaml
product: V-SMASH-DOME
code: VSM-D
role: Integrated Counter-UAS Defense System
target_price: $50,000 (basic), $80,000 (enhanced)
delivery: Month 36

re_source: SMASH DOME (layered detect-track-engage C-UAS)

configurations:
  basic:
    detection: EO/IR sensor only
    effector: V-SMASH RCWS
    price: $30,000
    range: 1 km detection

  standard:
    detection: EO/IR + upgraded thermal
    effector: V-SMASH RCWS
    c4i: V-SMASH C4I HUB integration
    price: $50,000
    range: 1.5 km detection

  enhanced:
    detection: EO/IR + external radar interface
    effector: V-SMASH RCWS (multiple)
    c4i: Full CoT/ATAK networking
    price: $80,000
    range: 2+ km detection (radar dependent)

system_architecture:
  detection_layer:
    eo_sensor:
      type: Sony IMX462 (HDR) + Pan-Tilt
      range: 1 km (drone detection)
      coverage: 360° (scanning)
    ir_sensor:
      type: FLIR Boson 640
      range: 1.5 km (thermal detection)
      netd: <40mK
    radar_interface:
      type: External (optional)
      protocols: Ethernet, RS-422
      compatible: DRS MHR, similar

  tracking_layer:
    processor: Jetson Xavier NX
    algorithms:
      detection: YOLOv8-medium + C-UAS
      tracking: IMM multi-target
      classification: Drone/bird/clutter AI
    capacity:
      simultaneous_tracks: 10
      update_rate: 10 Hz
      handoff_latency: <500ms

  engagement_layer:
    effector: V-SMASH RCWS (or RCWS-LITE)
    weapon: 5.56mm or 7.62mm
    range: 200-500m (kinetic)
    pk_single: >90%
    pk_burst: >95%
    rounds_per_kill: 2-5

  command_layer:
    c2_protocol: Cursor on Target (CoT)
    atak_compatible: Yes
    operator_interface: V-SMASH C4I HUB or tablet
    person_in_loop: Mandatory (all engagements)

operational_modes:
  standby:
    description: Low-power monitoring
    sensors: Radar only (if equipped)
    automation: Full auto detect

  alert:
    description: Threat detected
    sensors: All active
    automation: Auto track, alert operator

  engage:
    description: Target confirmed
    sensors: All + FCS
    automation: Semi-auto (operator confirms)

  manual:
    description: Operator full control
    sensors: Operator selected
    automation: None

performance:
  detection:
    range_eo: 1 km (drone, day)
    range_ir: 1.5 km (thermal)
    range_radar: 2-5 km (external)
    classification_accuracy: >95%
    false_positive: <5%

  engagement:
    detect_to_kill: <15 seconds
    engagement_range: 200-500m
    pk_drone: >90%
    cost_per_kill: <$10 (ammunition)

  coverage:
    azimuth: 360° (scanning)
    elevation: -10° to +70°
    simultaneous_engagements: 1 (basic), 2+ (networked)

physical:
  total_weight: ~50 kg (complete system)
  deployment: Vehicle, fixed position, temporary
  setup_time: <15 minutes
  power: 100-200W (24-48V DC or AC)
  sealing: IP65

target_users:
  - Base/FOB defense units
  - Critical infrastructure protection
  - Checkpoint security
  - Event security (temporary)
  - Border posts

target_threats:
  - Commercial surveillance drones
  - FPV attack drones
  - Loitering munitions
  - Drone swarms (limited)

local_content: 50%

development_phases:
  phase_1_basic:
    timeline: Month 24-30
    components: EO/IR + RCWS
    cost: $30K

  phase_2_standard:
    timeline: Month 30-36
    components: + C4I integration
    cost: $50K

  phase_3_enhanced:
    timeline: Month 36-42
    components: + Radar interface
    cost: $80K

vietnam_advantages:
  - Open CoT protocol (vs proprietary SMASH)
  - Local assembly reduces cost ($50K vs $150-400K)
  - Scalable from squad to installation
  - Integrates with VN BMS systems
  - Low cost per engagement (~$10)
```

### 3.9 V-SMASH C4I HUB (Command Accessory) - NEW

```yaml
product: V-SMASH-C4I-HUB
code: VSM-C
role: Squad Coordination and Command Link
target_price: $2,000
delivery: Month 18

re_source: SMASH Connectivity (MAGTAB integration, ATAK)

specifications:
  hardware:
    form_factor: Ruggedized Android tablet
    display: 8" 1200×1920 IPS (sunlight readable)
    processor: Snapdragon 865
    memory: 8GB RAM, 128GB storage
    battery: 10000mAh (12+ hours)

  connectivity:
    bluetooth: BLE 5.0 (up to 10 V-SMASH units)
    wifi: 802.11ax (ATAK mesh)
    cellular: 4G LTE (optional)
    gps: Multi-constellation

  software:
    os: Android 12 (hardened)
    app: V-SMASH Command (custom)
    atak: ATAK plugin compatible
    protocol: CoT/TAK

  features:
    map_display: All V-SMASH unit positions
    target_sharing: View/share all detected targets
    threat_priority: Squad-level threat ranking
    engagement_log: Real-time shot tracking
    blue_force: Friendly position overlay

  physical:
    weight: 500g
    dimensions: 220×140×15 mm
    sealing: IP65
    drop: MIL-STD-810H 1.2m

  capacity:
    max_units: 10 V-SMASH (BLE range)
    max_targets: 50 (displayed)
    update_rate: 1 Hz per unit

target_users:
  - Squad leaders
  - Platoon commanders
  - Operations centers
  - Forward observers

local_content: 40%
```

---

## 4. PRODUCT COMPARISON MATRIX

### 4.1 Capability Comparison

| Capability | LITE | PRO | PRO-X | HMG | MARITIME | RCWS-LITE | RCWS | DOME |
|------------|------|-----|-------|-----|----------|-----------|------|------|
| **DETECTION** | | | | | | | | |
| Day range (drone) | 300m | 300m | 500m | 500m | 400m | 400m | 800m | 1000m |
| Night range | — | 200m | 300m | 200m | 200m | 200m | 400m | 1500m |
| False positive | <10% | <5% | <5% | <5% | <5% | <5% | <3% | <5% |
| **TRACKING** | | | | | | | | |
| Max speed | 50m/s | 50m/s | 50m/s | 50m/s | 50m/s | 50m/s | 50m/s | 50m/s |
| Maneuver | 1.5g | 3g | 3g | 3g | 3g | 3g | 3g | 3g |
| Multi-target | 5 | 5 | 5 | 5 | 5 | 5 | 10 | **10** |
| **OPTICS** | | | | | | | | |
| Magnification | 1x | 1x | **4x** | 1x | 1x | 1x | 1x | 1x |
| LRF | — | — | **Yes** | — | — | — | **Yes** | — |
| Stabilization | — | — | — | — | **Yes** | — | **Yes** | — |
| **NETWORKING** | | | | | | | | |
| C4I (CoT) | — | ✓ | ✓ | ✓ | ✓ | Opt | ✓ | **✓** |
| Bluetooth | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Video stream | — | Opt | — | — | — | ✓ | **✓** | **✓** |
| Radar cue | — | — | — | — | — | — | ✓ | **✓** |
| **ENVIRONMENTAL** | | | | | | | | |
| Sealing | IP65 | IP67 | IP67 | IP67 | **IP68** | IP65 | IP67 | IP65 |
| Salt fog | — | — | — | — | **✓** | — | — | — |
| Recoil (12.7mm) | — | — | — | **✓** | — | — | ✓ | ✓ |
| **PHYSICAL** | | | | | | | | |
| Weight | 1.0kg | 1.3kg | 1.5kg | 1.8kg | 1.5kg | **10kg** | 15kg | **50kg** |
| Battery life | 10h | 6h | 5h | 6h | 6h | **2h** | 8h | Vehicle |
| Single-soldier | ✓ | ✓ | ✓ | — | ✓ | **✓** | — | — |

### 4.2 Price/Performance Positioning

```
V-SMASH PORTFOLIO POSITIONING
══════════════════════════════════════════════════════════════════════

        Capability
            ▲
            │                                                  ● DOME
   $50,000 ─┼─────────────────────────────────────────────────  (C-UAS System)
            │
            │
            │
   $12,000 ─┼─────────────────────────────────────────● RCWS
            │                                          (Remote Station)
            │
    $8,000 ─┼──────────────────────────────────● RCWS-LITE
            │                                   (Single-Soldier)
    $7,000 ─┼───────────────────────────● PRO-X
            │                            (Extended Range)
    $6,500 ─┼─────────────────────● MARITIME
            │                      (Naval)
    $6,000 ─┼───────────────● HMG
            │                (Heavy Weapon)
    $5,000 ─┼─────────● PRO
            │          (Operational)
            │
    $3,000 ─┼──● LITE
            │   (Entry)
    $2,000 ─┼● C4I HUB (Accessory)
            │
            └───────────────────────────────────────────▶ Price
            $0                                         $60,000

COMPETITOR REFERENCE:
• SMASH 3000:      ~$18,000 (similar to PRO)
• SMASH X4:        ~$25,000 (similar to PRO-X)
• SMASH Hopper:    ~$50,000 (similar to RCWS)
• Hopper Light:    ~$40,000 (similar to RCWS-LITE)
• SMASH DOME:      ~$150-400K (similar to DOME)

V-SMASH ADVANTAGE: 65-85% cost reduction across portfolio
```

---

## 5. VIETNAM-SPECIFIC FEATURES

### 5.1 Threat-Focused Design

| Vietnam Threat | V-SMASH Response | Product |
|----------------|------------------|---------|
| **FPV Attack Drones** | C-UAS optimized AI (≥5,000 drone images) | All |
| **Commercial Surveillance** | Multi-target tracking (5 tracks) | All |
| **Loitering Munitions** | High-maneuver tracking (3g) | PRO+ |
| **Small Boat Intrusion** | Maritime-optimized detection | MARITIME |
| **Mass Drone Swarm** | Priority queue, rapid switch | PRO+ |

### 5.2 Platform Integration (VPA Inventory)

| Platform | Weapon | V-SMASH Variant | Integration |
|----------|--------|-----------------|-------------|
| **Infantry** | AK-47/74 | LITE, PRO | Picatinny adapter |
| **Infantry** | M16/AR-15 | LITE, PRO, PRO-X | Direct Picatinny |
| **Heavy Weapons** | NSV 12.7mm | HMG | Custom bracket |
| **Heavy Weapons** | DShK 12.7mm | HMG | Custom bracket |
| **Vehicle** | MTB-20 RCWS | RCWS | CAN bus integration |
| **Naval** | Deck 12.7mm | MARITIME | Naval rail adapter |

### 5.3 Environmental Adaptation (Vietnam Climate)

| Climate Factor | Challenge | V-SMASH Solution | Products |
|----------------|-----------|------------------|----------|
| **High Humidity** | Fogging, corrosion | Lens heater, coatings | PRO+ |
| **Tropical Heat** | 40°C+ operation | Wide temp range, thermal mgmt | All |
| **Monsoon Rain** | Water ingress | IP67/IP68 sealing | PRO+ |
| **Salt Air (Coastal)** | Corrosion | Marine-grade materials | MARITIME |
| **Dust (Inland)** | Lens contamination | Sealed optics, wiper | All |

### 5.4 Local Production Strategy

```
V-SMASH LOCAL CONTENT BREAKDOWN
══════════════════════════════════════════════════════════════════════

                          LOCAL (Vietnam)           IMPORT
                          ─────────────────         ──────
LITE (75% local):
├── Housing/Machining ────────────────────●
├── PCB Assembly ─────────────────────────●
├── Battery Pack ─────────────────────────●
├── Cables/Connectors ────────────────────●
├── Final Assembly ───────────────────────●
├── CMOS Sensor ───────────────────────────────────────●
├── Compute Module ────────────────────────────────────●
└── IMU ───────────────────────────────────────────────●

PRO (60% local):
├── Housing/Machining ────────────────────●
├── PCB Assembly ─────────────────────────●
├── Battery Pack ─────────────────────────●
├── Final Assembly ───────────────────────●
├── HDR Sensor ────────────────────────────────────────●
├── Thermal Module ────────────────────────────────────●  ← Largest import
├── Compute Module ────────────────────────────────────●
└── Networking IC ─────────────────────────────────────●

LOCAL SUPPLIERS (Vietnam):
• Housing:      Hòa Phát (aluminum), local machining
• PCB Assembly: FPT, local EMS providers
• Battery:      VinFast supply chain (18650 cells)
• Cables:       Local harness manufacturers
• Testing:      Z113 (military acceptance)
```

---

## 6. MARKET ANALYSIS (VIETNAM FOCUS)

### 6.1 Domestic Market Segments

| Segment | Units (5yr) | Variant Mix | Revenue |
|---------|-------------|-------------|---------|
| **Army Infantry** | 1,500 | 60% LITE, 40% PRO | $5.7M |
| **Army Heavy Weapons** | 400 | 100% HMG | $2.4M |
| **Navy/Coast Guard** | 200 | 100% MARITIME | $1.3M |
| **Border Defense** | 300 | 50% PRO, 50% PRO-X | $1.8M |
| **Special Operations** | 100 | 70% PRO-X, 30% PRO | $0.6M |
| **Infantry Squads** | 200 | 100% RCWS-LITE | $1.6M |
| **Vehicle Units** | 150 | 100% RCWS | $1.8M |
| **Base/FOB Defense** | 30 | 100% DOME | $1.5M |
| **Command Elements** | 200 | 100% C4I HUB | $0.4M |
| **TOTAL DOMESTIC** | **3,080** | | **$17.1M** |

### 6.2 Export Potential (ASEAN + Partners)

| Country | Potential | Variants | Est. Units |
|---------|-----------|----------|------------|
| **Laos** | High (ally) | LITE, PRO | 200-400 |
| **Cambodia** | Medium | LITE, HMG | 100-200 |
| **Myanmar** | Low (restricted) | — | — |
| **Indonesia** | Medium | PRO, MARITIME | 100-300 |
| **Philippines** | Medium | PRO, MARITIME | 100-200 |
| **Bangladesh** | Medium | LITE, PRO | 100-200 |
| **TOTAL EXPORT** | | | **600-1,300** |

### 6.3 Total Addressable Market

| Market | Units | Revenue | Timeline |
|--------|-------|---------|----------|
| **Vietnam Domestic** | 3,080 | $17.1M | Years 1-5 |
| **ASEAN Export** | 1,100 | $5.2M | Years 3-7 |
| **Other Export** | 400 | $2.0M | Years 5-10 |
| **TOTAL** | **4,580** | **$24.3M** | 10 years |

---

## 7. DEVELOPMENT ROADMAP

### 7.1 Phased Delivery Schedule

```
V-SMASH DEVELOPMENT TIMELINE
══════════════════════════════════════════════════════════════════════

MONTH:  6   12   18   24   30   36   42   48
        │    │    │    │    │    │    │    │
        ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼

LITE    ████████▶ PRODUCTION
              │
PRO     ──────████████▶ PRODUCTION
                    │
C4I HUB ──────────██▶ PRODUCTION
                    │
HMG     ────────────████▶ PRODUCTION
                        │
MARITIME────────────────████▶ PRODUCTION
                            │
PRO-X   ──────────────────████▶ PRODUCTION
                            │
RCWS-LITE────────────────────██▶ PRODUCTION
                              │
RCWS    ────────────────────████▶ PRODUCTION
                                  │
DOME    ────────────────────────────████▶ PRODUCTION


PHASE 1 (Year 1):    LITE → Core capability, training
PHASE 2 (Year 2):    PRO, HMG, C4I HUB → Operational deployment
PHASE 3 (Year 3):    MARITIME, PRO-X, RCWS-LITE → Specialized roles
PHASE 4 (Year 4):    RCWS, DOME → Advanced systems
```

### 7.2 Technology Insertion Timeline

| Technology | Source RE | Insert Phase | Products |
|------------|-----------|--------------|----------|
| Core FCS | SMASH 2000+ | Phase 1 | All |
| Multi-target (5) | ARCAS | Phase 1 | All |
| C-UAS AI training | ARBEL | Phase 1 | All |
| Thermal fusion | ARBEL | Phase 2 | PRO+ |
| CoT networking | SMASH Conn | Phase 2 | PRO+ |
| HMG mount | SMASH Conn | Phase 2 | HMG |
| 4x magnification | SMASH X4 | Phase 3 | PRO-X |
| LRF integration | SMASH X4 | Phase 3 | PRO-X |
| Maritime stabilization | Vietnam-specific | Phase 3 | MARITIME |
| Single-soldier RCWS | Hopper Light | Phase 3 | RCWS-LITE |
| RCWS architecture | SMASH Hopper | Phase 4 | RCWS |
| Integrated C-UAS | SMASH DOME | Phase 4 | DOME |

---

## 8. FINANCIAL SUMMARY

### 8.1 Development Investment

| Phase | Products | Dev Cost | Timeline |
|-------|----------|----------|----------|
| Phase 1 | LITE | $150,000 | Months 1-12 |
| Phase 2 | PRO, C4I, HMG | $180,000 | Months 12-24 |
| Phase 3 | MARITIME, PRO-X, RCWS-LITE | $180,000 | Months 24-30 |
| Phase 4 | RCWS, DOME | $240,000 | Months 30-42 |
| **TOTAL** | **9 products** | **$750,000** | 42 months |

### 8.2 Unit Economics

| Product | Unit Cost | Price | Margin | Break-even |
|---------|-----------|-------|--------|------------|
| LITE | $800 | $3,000 | 73% | 68 units |
| PRO | $1,800 | $5,000 | 64% | 113 units |
| PRO-X | $2,500 | $7,000 | 64% | 48 units |
| HMG | $2,200 | $6,000 | 63% | 82 units |
| MARITIME | $2,400 | $6,500 | 63% | 50 units |
| RCWS-LITE | $3,500 | $8,000 | 56% | 36 units |
| RCWS | $5,500 | $12,000 | 54% | 27 units |
| DOME | $22,000 | $50,000 | 56% | 9 units |
| C4I HUB | $800 | $2,000 | 60% | 48 units |

### 8.3 10-Year Revenue Projection

| Year | Domestic | Export | Total |
|------|----------|--------|-------|
| 1 | $1.4M | $0 | $1.4M |
| 2 | $2.8M | $0.3M | $3.1M |
| 3 | $3.5M | $0.8M | $4.3M |
| 4 | $3.2M | $1.2M | $4.4M |
| 5 | $2.8M | $1.2M | $4.0M |
| 6-10 | $3.4M | $1.7M | $5.1M |
| **TOTAL** | **$17.1M** | **$5.2M** | **$22.3M** |

---

## 9. COMPETITIVE ADVANTAGE SUMMARY

### 9.1 V-SMASH vs. Foreign Systems

| Factor | SMASH Family | V-SMASH | Advantage |
|--------|--------------|---------|-----------|
| **Price** | $18,000-40,000 | $3,000-12,000 | **65-70% lower** |
| **Local Content** | 0% | 45-75% | **Sovereign supply** |
| **Vietnam Integration** | None | Native | **VPA inventory** |
| **C4I Protocol** | Proprietary | Open CoT | **Interoperability** |
| **Maritime Variant** | None | Yes | **SCS defense** |
| **Field Service** | Factory return | Local | **Faster repair** |
| **Export Control** | ITAR/EAR | Vietnamese | **Easier export** |

### 9.2 Key Differentiators

1. **Cost Leadership:** 65-70% cheaper than Israeli alternatives
2. **Vietnam-Optimized:** HMG mounts for NSV/DShK, maritime variant
3. **Open Standards:** CoT protocol for C4I (not proprietary lock-in)
4. **Local Production:** 45-75% Vietnamese content
5. **Platform Family:** 7 variants covering all VPA needs
6. **Climate Adapted:** Tropical humidity, salt fog, monsoon rated

---

## 10. RECOMMENDATIONS

### 10.1 Immediate Actions

| Action | Owner | Timeline | Priority |
|--------|-------|----------|----------|
| Approve 7-product portfolio | MoD | Week 1 | Critical |
| Allocate Phase 1 funding | Finance | Week 2 | Critical |
| Initiate thermal sensor procurement | Procurement | Week 2 | High |
| Begin LITE detailed design | Engineering | Week 3 | High |
| Establish local supplier agreements | Supply Chain | Week 4 | High |

### 10.2 Strategic Decisions Required

| Decision | Options | Recommendation |
|----------|---------|----------------|
| Portfolio scope | 2 vs 7 products | **7 products** (full coverage) |
| MARITIME variant | Include vs defer | **Include** (SCS priority) |
| RCWS development | In-house vs partner | **Partner** (reduce risk) |
| Export strategy | Domestic-first vs parallel | **Domestic-first** (de-risk) |

### 10.3 Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Thermal sensor supply | Qualify 2 suppliers (FLIR + Chinese) |
| 12.7mm recoil tolerance | Early prototype testing |
| Maritime corrosion | Partner with naval shipyard |
| RCWS complexity | Technology partnership option |

---

## 11. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-04 | Initial two-tier strategy (LITE + PRO) |
| 1.1 | 2026-02-04 | Multi-target update from ARCAS RE |
| 2.0 | 2026-02-04 | Complete portfolio revision based on 6 RE analyses. Added PRO-X, HMG, MARITIME, RCWS, C4I HUB. Vietnam-specialized design. 7-product family. |
| **3.0** | **2026-02-04** | **Expanded to 9-product family based on 10 RE analyses. Added RCWS-LITE (single-soldier, $8K) and DOME (integrated C-UAS, $50K). Updated market projections to $24.3M TAM. Added Hopper Light, SMASH DOME, SMASH Dragon to RE sources.** |

---

## APPENDIX A: RE ANALYSIS SUMMARY

| # | System | RE Document | Key Contributions |
|---|--------|-------------|-------------------|
| 1 | SMASH 2000+ | [[V-SMASH_RE_01_SMASH2000_analysis]] | Core FCS design, human-in-loop |
| 2 | ARCAS | [[V-SMASH_RE_02_ARCAS_analysis]] | Multi-target (10+), AR display, C4I |
| 3 | SMASH Dragon | [[V-SMASH_RE_03_SMASH_Dragon_analysis]] | Armed UAV payload (future) |
| 4 | SMASH 2000L/3000 | [[V-SMASH_RE_04_SMASH3000_analysis]] | Weight reduction, mesh networking |
| 5 | SMASH X4 | [[V-SMASH_RE_05_SMASHX4_analysis]] | Magnification, LRF, etched reticle |
| 6 | SMASH Connectivity | [[V-SMASH_RE_06_SMASH_connectivity_analysis]] | MAGTAB, RCWS, HMG, UGV |
| 7 | SMASH Hopper 5000 | [[V-SMASH_RE_07_SMASH_Hopper5000_analysis]] | Full RCWS (15kg, 360°) |
| 8 | SMASH Hopper Light | [[V-SMASH_RE_08_SMASH_HopperLight_analysis]] | Single-soldier RCWS (10kg) |
| 9 | SMASH DOME | [[V-SMASH_RE_09_SMASH_DOME_analysis]] | Integrated C-UAS system |
| 10 | ARBEL | ARCAS/ARBEL combined | C-UAS AI, sensor fusion |

---

## APPENDIX B: PRODUCT FAMILY SUMMARY

| Product | Code | Type | Weight | Price | Phase | Local % |
|---------|------|------|--------|-------|-------|---------|
| **LITE** | VSM-L | Handheld FCS | 1.0 kg | $3,000 | 1 | 75% |
| **PRO** | VSM-P | Handheld FCS | 1.3 kg | $5,000 | 2 | 60% |
| **PRO-X** | VSM-PX | Handheld FCS | 1.5 kg | $7,000 | 3 | 55% |
| **HMG** | VSM-H | Platform FCS | 1.8 kg | $6,000 | 2 | 62% |
| **MARITIME** | VSM-M | Naval FCS | 1.5 kg | $6,500 | 3 | 58% |
| **RCWS-LITE** | VSM-RL | Ultra-light RCWS | 10 kg | $8,000 | 3 | 55% |
| **RCWS** | VSM-R | Full RCWS | 15 kg | $12,000 | 4 | 45% |
| **DOME** | VSM-D | Integrated C-UAS | 50 kg | $50,000 | 4 | 50% |
| **C4I HUB** | VSM-C | Command Accessory | 0.5 kg | $2,000 | 2 | 40% |

---

*Related Documents:*
- [[V-SMASH_00_project_brief|Project Brief]]
- [[V-SMASH_P1_01_requirements_list|Requirements List v1.5]]
- [[V-SMASH_P2_01_function_structure|Function Structure v1.2]]
- [[V-SMASH_P2_02_morphological_matrix|Morphological Matrix v1.2]]
- [[V-SMASH_P2_05_product_variants_spec|Product Variants Spec v1.1]] (superseded)

---

*This document proposes an expanded V-SMASH product portfolio specialized for Vietnam's defense requirements, synthesizing insights from 10 foreign system reverse engineering analyses.*
