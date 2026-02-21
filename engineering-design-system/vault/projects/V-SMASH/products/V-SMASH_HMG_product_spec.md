---
project: V-SMASH
product: HMG
designation: VSM-HMG
version: 1.0
created: 2026-02-04
status: approved
vdi_score: 81%
target_price: $6,000
---

# V-SMASH HMG - PRODUCT SPECIFICATION
## 12.7mm Heavy Machine Gun Fire Control System

**Product Code:** VSM-HMG
**VDI 2225 Score:** 81% ✅
**Target Price:** $6,000
**Delivery:** Phase 1 (Month 12)

---

## PHASE 1: REQUIREMENTS

### 1.1 Product-Specific Requirements

| Req ID | Category | Requirement | Value | Type | Source |
|--------|----------|-------------|-------|------|--------|
| R01 | Performance | Detection range (drone) | ≥800m | D | HMG range |
| R02 | Performance | Effective range | ≥1000m | D | 12.7mm |
| R03 | Performance | Hit improvement | ≥4x | D | ODI S1-05 |
| R04 | Performance | Burst tracking | Maintain lock | D | HMG fire |
| R05 | Performance | Simultaneous tracks | ≥5 | D | R65 |
| R06 | Weapon | Primary caliber | 12.7x108mm | D | NSV/DShK |
| R07 | Weapon | Secondary calibers | 14.5mm, 7.62mm | W | Flexibility |
| R08 | Weapon | Recoil tolerance | 500g peak | D | HMG shock |
| R09 | Weapon | Trigger interface | Electronic 24V | D | Integration |
| R10 | Physical | Weight | ≤1.8 kg | D | HMG mount |
| R11 | Physical | Cable length | ≥2m | D | Control box |
| R12 | Environmental | Operating temp | -10°C to +55°C | D | Vietnam |
| R13 | Environmental | Sealing | IP67 | D | Field |
| R14 | Environmental | Shock rating | MIL-STD-810H | D | Recoil |
| R15 | Interface | HMG rail adapter | Custom | D | NSV mount |
| R16 | Safety | Human-in-the-loop | Mandatory | D | Legal |

### 1.2 Weapon Profiles Supported

| Caliber | BC (G7) | Muzzle Vel | Application |
|---------|---------|------------|-------------|
| 12.7x108mm | 0.620 | 850 m/s | NSV, DShK |
| 14.5x114mm | 0.750 | 1000 m/s | KPV |
| 7.62x54mmR | 0.180 | 830 m/s | PKM |

---

## PHASE 2: CONCEPTUAL DESIGN

### 2.1 Function Structure (HMG-Specific)

```
V-SMASH HMG FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════

F1: ACQUIRE TARGET INFORMATION
├── F1.1: Capture scene image ────────── CMOS HDR 1080p60
├── F1.2: Detect targets ─────────────── YOLOv8-nano
├── F1.3: Classify target type ───────── Drone classifier
└── F1.4: Measure range ──────────────── Passive (size-based)

F2: TRACK TARGET MOTION (Recoil-Compensated)
├── F2.2: Update track state ─────────── IMM Filter
├── F2.2R: Compensate recoil ─────────── Accelerometer-based
├── F2.5: Manage multiple tracks ─────── Fixed pool (5)
├── F2.6: Associate detections ───────── Hungarian Algorithm
└── F2.7: Prioritize targets ─────────── Distance-based

F3: COMPUTE FIRE SOLUTION (HMG-Optimized)
├── F3.1: Sense weapon orientation ───── 9-axis IMU (enhanced)
├── F3.2: Retrieve weapon profile ────── 12.7mm, 14.5mm, 7.62mm
├── F3.3: Calculate trajectory ───────── Point-mass 3DOF
├── F3.3R: Apply recoil prediction ───── Burst compensation
└── F3.4: Determine alignment error ──── Vector comparison

F4: CONTROL FIRE AUTHORIZATION
├── F4.1: Sense trigger (electronic) ─── 24V interface
├── F4.2: Evaluate hit probability ───── Threshold logic
├── F4.3: Authorize fire ─────────────── Boolean decision
└── F4.4: Time burst release ─────────── Burst timing

F5: ACTUATE TRIGGER MECHANISM
├── F5.1: Hold fire ──────────────────── Electronic gate
├── F5.2: Release fire ───────────────── 24V solenoid trigger
└── F5.3: Confirm fire event ─────────── Recoil + acoustic

F6: PROVIDE OPERATOR FEEDBACK
├── F6.1: Display aim point ──────────── Ruggedized display
├── F6.2: Show target lock status ────── LED + overlay
├── F6.3: Indicate fire readiness ────── Color + audio
└── F6.4: Display ammo count ─────────── Round counter (opt)
```

### 2.2 Working Principles Selected

| Function | Working Principle | Specification |
|----------|------------------|---------------|
| F1.1 | HDR CMOS | Sony IMX462, 85dB, 100g shock rated |
| F2.2R | Recoil compensation | BMI088 9-axis, 100g rating |
| F3.2 | HMG profiles | 12.7mm, 14.5mm, 7.62mm ballistics |
| F4.1 | Electronic trigger | 24V interface, parallel gate |
| F5.2 | HMG trigger | Compatible with NSV electronic |

---

## PHASE 3: EMBODIMENT DESIGN

### 3.1 Layout Design

```
V-SMASH HMG - SYSTEM LAYOUT
═══════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────┐
                    │           SENSOR HEAD (on HMG)          │
                    │  ┌───────────┐  ┌───────────────────┐  │
                    │  │ CMOS HDR  │  │ IMU (shock-rated) │  │
                    │  │ + OPTICS  │  │ BMI088            │  │
                    │  └───────────┘  └───────────────────┘  │
                    │         HMG RAIL ADAPTER                │
                    └────────────────┬────────────────────────┘
                                     │ 2m Cable
                                     │
    ┌────────────────────────────────┴────────────────────────┐
    │                    CONTROL BOX                           │
    │  ┌───────────────┐  ┌───────────────┐  ┌─────────────┐  │
    │  │ JETSON NANO   │  │ TRIGGER I/F   │  │ POWER       │  │
    │  │ + CARRIER     │  │ 24V GATE      │  │ MANAGEMENT  │  │
    │  └───────────────┘  └───────────────┘  └─────────────┘  │
    │                                                          │
    │  ┌───────────────────────────────────────────────────┐  │
    │  │              OPERATOR DISPLAY                      │  │
    │  │              (5" ruggedized LCD)                   │  │
    │  └───────────────────────────────────────────────────┘  │
    └─────────────────────────────────────────────────────────┘

Sensor Head: 180mm × 100mm × 120mm, 1.8 kg
Control Box: 200mm × 150mm × 80mm, 2.0 kg
Total System: 3.8 kg
```

### 3.2 DfX Review

| DfX Category | Score | Notes |
|--------------|-------|-------|
| DfM | 7/10 | Two-box design, shock mounting |
| DfA | 8/10 | Modular, field-separable |
| DfR | 8/10 | Shock-rated components |
| DfT | 7/10 | Recoil simulation required |
| DfC | 7/10 | Additional shock protection |
| DfE | 9/10 | IP67, MIL-STD-810H shock |
| DfMaint | 8/10 | Modular boxes, cable replacement |
| **OVERALL** | **7.7/10** | Good for HMG application |

### 3.3 Shock/Vibration Design

| Requirement | Solution |
|-------------|----------|
| 500g recoil | Silicone isolators, shock mounts |
| Continuous vibration | Loctite all fasteners, strain relief |
| IMU saturation | BMI088 with 100g range |
| Cable stress | Reinforced cable, strain relief both ends |

---

## PHASE 4: DETAIL DESIGN

### 4.1 Bill of Materials Summary

| Category | Cost | Notes |
|----------|------|-------|
| Processing | $200 | Jetson Nano + carrier |
| Sensors | $100 | IMX462 + BMI088 shock |
| Optics | $80 | Ruggedized window |
| Power | $60 | PMIC + connector |
| Actuation | $50 | 24V trigger interface |
| Sensor head housing | $120 | Shock-mounted Al |
| Control box housing | $100 | Ruggedized Al |
| Cable assembly | $50 | 2m shielded |
| Display | $150 | 5" ruggedized LCD |
| Misc | $40 | Connectors, labels |
| **SUBTOTAL** | **$950** | |
| Labor + Test | $200 | Shock testing |
| Software | $150 | HMG profiles |
| **TOTAL** | **$1,850** | |

### 4.2 Key Components

| Component | Specification | Shock Rating |
|-----------|---------------|--------------|
| BMI088 IMU | 9-axis | 100g |
| IMX462 | HDR CMOS | 50g (mounted) |
| Connectors | MIL-spec circular | 500g |
| Cable | Shielded, flex | 10M cycles |

### 4.3 Production Plan

| Phase | Activity | Timeline | Volume |
|-------|----------|----------|--------|
| Pilot | 10 units | M10-11 | 10 |
| LRIP | 50 units | M12-14 | 50 |
| FRP | 100/year | M15+ | 100/yr |

### 4.4 Integration Requirements

| HMG Platform | Interface | Notes |
|--------------|-----------|-------|
| NSV | Picatinny adapter + 24V | Primary target |
| DShK | Custom mount + 24V | Adapter kit |
| KPV | Custom mount + 24V | 14.5mm profile |
| PKM | Picatinny + manual trigger | Mechanical linkage |

---

## DOCUMENT LINKS

- [[V-SMASH_PRO_product_spec|PRO Specification]] (sensor base)
- [[V-SMASH_RE_06_SMASH_connectivity_analysis|Connectivity RE Analysis]]
- [[V-SMASH_P2_05_product_variants_spec|Product Variants v2.1]]
