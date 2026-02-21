---
project: V-SMASH
product: PRO
designation: VSM-P
version: 1.0
created: 2026-02-04
status: approved
vdi_score: 79%
target_price: $5,000
---

# V-SMASH PRO - PRODUCT SPECIFICATION
## 24/7 Operational AI Fire Control System

**Product Code:** VSM-P
**VDI 2225 Score:** 79% ✅
**Target Price:** $5,000
**Delivery:** Phase 2 (Month 24)

---

## PHASE 1: REQUIREMENTS

### 1.1 Product-Specific Requirements

| Req ID | Category | Requirement | Value | Type | Source |
|--------|----------|-------------|-------|------|--------|
| R01 | Performance | Detection range (drone, day) | ≥300m | D | ODI S1-02 |
| R02 | Performance | Detection range (drone, night) | ≥200m | D | ODI S1-22 |
| R03 | Performance | Detection accuracy | ≥95% | D | ODI S1-02 |
| R04 | Performance | Engagement time | ≤5 sec | D | ODI S1-01 |
| R05 | Performance | Tracking lock probability | ≥95% | D | ODI S1-02 |
| R06 | Performance | Hit improvement | ≥4x | D | ODI S1-05 |
| R07 | Performance | First-round Pk @ 200m | ≥70% | D | ODI S1-05 |
| R08 | Performance | Simultaneous tracks | ≥5 | D | R65 |
| R09 | Performance | Maneuver tracking | 3g | D | R60 |
| R10 | Performance | False positive rate | <5% | D | R58 |
| R11 | Physical | Weight (with battery) | ≤1.5 kg | D | Market |
| R12 | Environmental | Operating temp | -10°C to +55°C | D | Vietnam |
| R13 | Environmental | Sealing | IP67 | D | R14 |
| R14 | Environmental | Salt fog | 48 hours | W | Coastal |
| R15 | Sensor | Primary sensor | HDR ≥80dB | D | R61 |
| R16 | Sensor | Thermal sensor | LWIR 160x120 | D | R62 |
| R17 | Sensor | Sensor fusion | Weighted blend | D | R70 |
| R18 | Power | Battery life | ≥6 hours | D | Operational |
| R19 | Interface | Picatinny mount | MIL-STD-1913 | D | Standard |
| R20 | Interface | C4I data sharing | CoT/UDP | W | R67 |
| R21 | Safety | Human-in-the-loop | Mandatory | D | Legal |
| R22 | Local Content | Local manufacturing | ≥60% | D | Policy |

### 1.2 PRO-Specific Features (vs LITE)

| Feature | LITE | PRO | Benefit |
|---------|------|-----|---------|
| Thermal sensor | None | FLIR Lepton 3.5 | Night capability |
| HDR sensor | 65dB | ≥80dB | Dawn/dusk performance |
| Tracking filter | Kalman | IMM | 3g maneuver tracking |
| Data association | Nearest-Neighbor | Hungarian | Robust in clutter |
| Threat priority | Distance | Multi-factor AI | Intelligent targeting |
| C4I interface | None | CoT/UDP | Network integration |
| Sealing | IP65 | IP67 | All-weather |
| Lens heater | None | 2W resistive | Anti-fog |

---

## PHASE 2: CONCEPTUAL DESIGN

### 2.1 Function Structure (PRO-Applicable)

```
V-SMASH PRO FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════

F1: ACQUIRE TARGET INFORMATION (Enhanced)
├── F1.1: Capture scene image ────────── CMOS HDR 1080p60
├── F1.1T: Capture thermal image ─────── LWIR 160x120
├── F1.5: Fuse sensor data ───────────── Weighted blend
├── F1.2: Detect targets ─────────────── YOLOv8-nano + thermal
├── F1.6: Apply C-UAS AI model ───────── Drone-optimized CNN
├── F1.3: Classify target type ───────── Multi-class CNN
└── F1.4: Measure range ──────────────── Passive + thermal size

F2: TRACK TARGET MOTION (Enhanced)
├── F2.1: Initialize track ───────────── Detection-to-track
├── F2.2: Update track state ─────────── IMM Filter (3g)
├── F2.3: Predict future position ────── CV + CA models
├── F2.5: Manage multiple tracks ─────── Fixed pool (5)
├── F2.6: Associate detections ───────── Hungarian Algorithm
└── F2.7: Prioritize targets ─────────── Multi-factor AI

F7: COORDINATE MULTI-TARGET (PRO)
├── F7.1: Select primary target ──────── Auto + override
├── F7.2: Queue secondary targets ────── Priority queue
├── F7.3: Enable rapid switch ────────── State preservation
└── F7.4: Share target data ──────────── CoT over UDP

F3: COMPUTE FIRE SOLUTION
├── F3.1: Sense weapon orientation ───── 6-axis IMU
├── F3.2: Retrieve weapon profile ────── Database lookup
├── F3.3: Calculate trajectory ───────── Point-mass 3DOF
└── F3.4: Determine alignment error ──── Vector comparison

F4: CONTROL FIRE AUTHORIZATION
├── F4.1: Sense trigger pressure ─────── Force sensor
├── F4.2: Evaluate hit probability ───── Threshold logic
├── F4.3: Authorize/gate fire ────────── Boolean decision
└── F4.4: Time trigger release ───────── Precision timing

F5: ACTUATE TRIGGER MECHANISM
├── F5.1: Hold trigger ───────────────── 12V solenoid
├── F5.2: Release trigger ────────────── Electromechanical
└── F5.3: Confirm fire event ─────────── Acoustic sensor

F6: PROVIDE OPERATOR FEEDBACK
├── F6.1: Display aim point ──────────── See-through optic
├── F6.2: Show target lock status ────── LED + overlay
├── F6.3: Indicate fire readiness ────── Color + audio
└── F6.4: Display system status ──────── OLED screen

F_AUX: AUXILIARY FUNCTIONS
├── F_AUX.1: Manage power ────────────── Li-ion PMIC
├── F_AUX.2: Record engagement ───────── SD card
├── F_AUX.3: Configure weapon ────────── USB interface
├── F_AUX.4: Heat lens ───────────────── Resistive heater
└── F_AUX.5: Provide fail-safe ───────── Mechanical bypass
```

### 2.2 Working Principles Selected

| Function | Working Principle | Specification |
|----------|------------------|---------------|
| F1.1 | WP-001: HDR CMOS | Sony IMX462, 85dB |
| F1.1T | Thermal sensor | FLIR Lepton 3.5, 160x120 |
| F1.5 | WP-012: Sensor fusion | Weighted blend, auto α |
| F1.2 | WP-002: YOLO + thermal | Dual-input detection |
| F2.2 | IMM Filter | CV + CA + CT models |
| F2.6 | WP-007: Hungarian | O(n³), optimal assignment |
| F2.7 | WP-008: Multi-factor | Distance + velocity + type |
| F7.4 | WP-011: CoT protocol | UDP, AES-256 |

### 2.3 Concept Evaluation Summary

| Criterion | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| Performance | 15% | 4.0 | 0.60 |
| Reliability | 10% | 3.0 | 0.30 |
| Dev Cost | 15% | 3.0 | 0.45 |
| Prod Cost | 10% | 2.0 | 0.20 |
| Dev Time | 10% | 3.0 | 0.30 |
| Supply Chain | 15% | 3.0 | 0.45 |
| Local Content | 15% | 2.5 | 0.38 |
| Maintainability | 5% | 3.0 | 0.15 |
| Interoperability | 5% | 4.0 | 0.20 |
| **TOTAL** | **100%** | | **3.03/4 = 79%** |

---

## PHASE 3: EMBODIMENT DESIGN

### 3.1 Layout Design

```
V-SMASH PRO - LAYOUT (Top View)
═══════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────┐
    │                    OPTICAL ASSEMBLY                      │
    │  ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌───────────┐ │
    │  │ CMOS    │  │ THERMAL │  │ BEAM     │  │ SEE-THRU  │ │
    │  │ HDR     │  │ LWIR    │  │ COMBINER │  │ DISPLAY   │ │
    │  │ IMX462  │  │ LEPTON  │  │          │  │           │ │
    │  └─────────┘  └─────────┘  └──────────┘  └───────────┘ │
    │                    │ LENS HEATER (2W) │                  │
    └─────────────────────────────────────────────────────────┘
                           │
    ┌─────────────────────────────────────────────────────────┐
    │                 PROCESSING ASSEMBLY                      │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
    │  │ JETSON      │  │ CARRIER     │  │ IMU + CoT       │  │
    │  │ NANO        │  │ BOARD       │  │ NETWORK         │  │
    │  │ 4GB         │  │ (FUSION)    │  │                 │  │
    │  └─────────────┘  └─────────────┘  └─────────────────┘  │
    └─────────────────────────────────────────────────────────┘
                           │
    ┌─────────────────────────────────────────────────────────┐
    │                  POWER/ACTUATION                         │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
    │  │ BATTERY     │  │ PMIC        │  │ SOLENOID        │  │
    │  │ 3x 18650    │  │ + HEATER    │  │ DRIVER          │  │
    │  │ 10200mAh    │  │ CONTROL     │  │                 │  │
    │  └─────────────┘  └─────────────┘  └─────────────────┘  │
    └─────────────────────────────────────────────────────────┘

Dimensions: 170mm (L) × 90mm (W) × 110mm (H)
Weight: 1.5 kg (with battery)
```

### 3.2 DfX Review

| DfX Category | Score | Notes |
|--------------|-------|-------|
| DfM (Manufacturing) | 7/10 | Thermal integration adds complexity |
| DfA (Assembly) | 7/10 | More components, calibration needed |
| DfR (Reliability) | 8/10 | Thermal sensor proven, IP67 |
| DfT (Test) | 7/10 | Thermal calibration required |
| DfC (Cost) | 6/10 | Thermal sensor dominates cost |
| DfE (Environment) | 9/10 | IP67, lens heater, salt fog |
| DfMaint (Maintenance) | 7/10 | Thermal module replaceable |
| **OVERALL** | **7.3/10** | Acceptable for production |

### 3.3 Material Selection

| Component | Material | Supplier | Local % |
|-----------|----------|----------|---------|
| Housing | Al 6061-T6 anodized | Hoa Phat | 100% |
| Thermal window | Germanium AR coated | Import | 0% |
| Sealing | IP67 gaskets | Import | 0% |
| Lens cover | Sapphire AR coated | Import | 0% |

---

## PHASE 4: DETAIL DESIGN

### 4.1 Bill of Materials Summary

| Category | Cost | Local % |
|----------|------|---------|
| Processing | $200 | 25% |
| Sensors (CMOS+thermal) | $960 | 0% |
| Optics | $155 | 0% |
| Power | $45 | 45% |
| Actuation | $15 | 65% |
| Housing | $180 | 100% |
| Misc | $40 | 70% |
| **SUBTOTAL** | **$1,595** | |
| Labor + Test | $150 | 100% |
| Software | $175 | 100% |
| **TOTAL** | **$1,920** | **31%** |

### 4.2 Key Components

| Component | Specification | Unit Cost | Source |
|-----------|---------------|-----------|--------|
| Jetson Nano | 4GB | $150 | Import |
| Sony IMX462 | HDR 85dB | $75 | Import |
| FLIR Lepton 3.5 | 160x120 LWIR | $800 | Import |
| Lens heater | 2W resistive | $20 | Import |
| IP67 housing | Al 6061 | $180 | Local |

### 4.3 Production Plan

| Phase | Activity | Timeline | Volume |
|-------|----------|----------|--------|
| Pilot | 10 units | M22-23 | 10 |
| LRIP | 30 units | M24-26 | 30 |
| FRP | 150/year | M27+ | 150/yr |

### 4.4 Test Requirements

| Test | Standard | Criteria |
|------|----------|----------|
| Environmental | MIL-STD-810H | -10°C to +55°C, IP67 |
| Night performance | Internal | 200m detection @ 0.01 lux |
| Thermal fusion | Internal | Auto mode switching |
| Multi-target | Internal | 5 tracks, <50ms switch |
| C4I | TAK server | CoT interoperability |

---

## DOCUMENT LINKS

- [[V-SMASH_LITE_product_spec|LITE Specification]] (base variant)
- [[V-SMASH_P1_01_requirements_list|Full Requirements List]]
- [[V-SMASH_P2_01_function_structure|Function Structure v1.3]]
- [[V-SMASH_RE_03_ARBEL_analysis|ARBEL RE Analysis]] (thermal fusion)
- [[V-SMASH_RE_02_ARCAS_analysis|ARCAS RE Analysis]] (multi-target)
