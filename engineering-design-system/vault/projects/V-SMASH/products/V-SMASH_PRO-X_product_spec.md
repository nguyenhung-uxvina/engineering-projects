---
project: V-SMASH
product: PRO-X
designation: VSM-PX
version: 1.0
created: 2026-02-04
status: approved
vdi_score: 76%
target_price: $7,000
---

# V-SMASH PRO-X - PRODUCT SPECIFICATION
## Extended Range AI Fire Control System

**Product Code:** VSM-PX
**VDI 2225 Score:** 76% ✅
**Target Price:** $7,000
**Delivery:** Phase 2 (Month 24)

---

## PHASE 1: REQUIREMENTS

### 1.1 Product-Specific Requirements

| Req ID | Category | Requirement | Value | Type | Source |
|--------|----------|-------------|-------|------|--------|
| R01 | Performance | Detection range (drone, day) | ≥500m | D | Extended |
| R02 | Performance | Detection range (drone, night) | ≥300m | D | ODI S1-22 |
| R03 | Performance | Effective engagement range | ≥600m | D | Extended |
| R04 | Performance | Tracking lock probability | ≥95% | D | ODI S1-02 |
| R05 | Performance | Hit improvement | ≥5x | D | Extended |
| R06 | Optical | Magnification | 4x fixed | D | SMASH X4 |
| R07 | Optical | LRF range | 50-800m | D | R69 |
| R08 | Optical | LRF accuracy | ±1m | D | Precision |
| R09 | Optical | Reticle type | Etched glass backup | D | SMASH X4 |
| R10 | Sensor | Primary sensor | HDR ≥80dB | D | R61 |
| R11 | Sensor | Thermal sensor | LWIR (optional) | W | Cost option |
| R12 | Physical | Weight | ≤1.8 kg | D | Marksman |
| R13 | Environmental | Sealing | IP67 | D | Field |
| R14 | Interface | Picatinny mount | MIL-STD-1913 | D | Standard |
| R15 | Safety | Human-in-the-loop | Mandatory | D | Legal |

### 1.2 PRO-X Unique Features

| Feature | PRO | PRO-X | Application |
|---------|-----|-------|-------------|
| Magnification | 1x | 4x | Extended range ID |
| LRF | None | 800m | Precision ranging |
| Reticle | Electronic only | Etched + electronic | Backup aiming |
| Detection range | 300m | 500m | Long-range engagement |
| Effective range | 400m | 600m | Designated marksman |

---

## PHASE 2: CONCEPTUAL DESIGN

### 2.1 Function Structure (PRO-X Specific)

```
V-SMASH PRO-X FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════

F1: ACQUIRE TARGET INFORMATION (Extended Range)
├── F1.1: Capture scene image ────────── CMOS HDR 1080p60
├── F1.1M: Magnify image ─────────────── 4x optical zoom
├── F1.1T: Capture thermal image ─────── LWIR (optional)
├── F1.2: Detect targets ─────────────── YOLOv8-nano
├── F1.3: Classify target type ───────── Multi-class CNN
├── F1.4: Measure range (LRF) ────────── Eye-safe Class 1 laser
└── F1.4B: Measure range (backup) ────── Passive size-based

F2: TRACK TARGET MOTION
├── F2.2: Update track state ─────────── IMM Filter
├── F2.5: Manage multiple tracks ─────── Fixed pool (5)
├── F2.6: Associate detections ───────── Hungarian Algorithm
└── F2.7: Prioritize targets ─────────── Multi-factor AI

F3: COMPUTE FIRE SOLUTION (LRF-Enhanced)
├── F3.1: Sense weapon orientation ───── 6-axis IMU
├── F3.2: Retrieve weapon profile ────── Database lookup
├── F3.3: Calculate trajectory ───────── Point-mass 3DOF + LRF
├── F3.3L: Apply LRF correction ──────── Auto range input
└── F3.4: Determine alignment error ──── Vector comparison

F6: PROVIDE OPERATOR FEEDBACK (Enhanced)
├── F6.1: Display aim point ──────────── 4x magnified optic
├── F6.1B: Backup reticle ────────────── Etched glass BDC
├── F6.2: Show range readout ─────────── LRF display
├── F6.3: Indicate fire readiness ────── Color overlay
└── F6.4: Display system status ──────── OLED screen
```

### 2.2 Working Principles Selected

| Function | Working Principle | Specification |
|----------|------------------|---------------|
| F1.1M | 4x Optical | Fixed magnification, 6° FOV |
| F1.4 | Eye-safe LRF | Class 1, 50-800m, ±1m |
| F6.1B | Etched reticle | BDC for 5.56/7.62, illuminated |
| F3.3L | LRF auto-input | Serial to ballistic computer |

---

## PHASE 3: EMBODIMENT DESIGN

### 3.1 Layout Design

```
V-SMASH PRO-X - LAYOUT (Side View)
═══════════════════════════════════════════════════════════════

    ┌───────────────────────────────────────────────────────────┐
    │                    4X OPTICAL ASSEMBLY                     │
    │  ┌─────────┐  ┌──────────┐  ┌─────────┐  ┌────────────┐  │
    │  │ CMOS    │  │ 4X OPTIC │  │ BEAM    │  │ EYEPIECE   │  │
    │  │ SENSOR  │  │ ASSEMBLY │  │ SPLITTER│  │ + RETICLE  │  │
    │  └─────────┘  └──────────┘  └─────────┘  └────────────┘  │
    └───────────────────────────────────────────────────────────┘
           │
    ┌───────────────────────────────────────────────────────────┐
    │                    LRF MODULE                              │
    │  ┌─────────────────┐  ┌────────────────────────────────┐  │
    │  │ LASER EMITTER   │  │ RECEIVER + TIMING              │  │
    │  │ Eye-safe 905nm  │  │                                │  │
    │  └─────────────────┘  └────────────────────────────────┘  │
    └───────────────────────────────────────────────────────────┘
           │
    ┌───────────────────────────────────────────────────────────┐
    │  PROCESSING + POWER                                        │
    │  ┌───────────┐  ┌───────────┐  ┌─────────────────────┐   │
    │  │ JETSON    │  │ CARRIER   │  │ BATTERY 3x18650     │   │
    │  │ NANO      │  │ + LRF I/F │  │                     │   │
    │  └───────────┘  └───────────┘  └─────────────────────┘   │
    └───────────────────────────────────────────────────────────┘

Dimensions: 220mm (L) × 95mm (W) × 130mm (H)
Weight: 1.8 kg (with battery, no thermal)
Eye Relief: 70mm
```

### 3.2 DfX Review

| DfX Category | Score | Notes |
|--------------|-------|-------|
| DfM | 6/10 | LRF integration complex |
| DfA | 6/10 | Optical alignment critical |
| DfR | 7/10 | LRF proven technology |
| DfT | 6/10 | LRF calibration required |
| DfC | 5/10 | Optics + LRF costly |
| DfE | 8/10 | IP67, ruggedized |
| DfMaint | 7/10 | LRF module replaceable |
| **OVERALL** | **6.4/10** | Requires careful production |

---

## PHASE 4: DETAIL DESIGN

### 4.1 Bill of Materials Summary

| Category | Cost | Notes |
|----------|------|-------|
| Processing | $200 | Same as PRO |
| Sensors (CMOS only) | $100 | No thermal standard |
| 4x Optic assembly | $350 | Magnification + reticle |
| LRF module | $350 | Eye-safe, 800m |
| Power | $50 | 3x 18650 |
| Actuation | $15 | Same solenoid |
| Housing | $220 | Larger, LRF mount |
| Misc | $45 | |
| **SUBTOTAL** | **$1,330** | |
| Labor + Test | $180 | LRF calibration |
| Software | $200 | LRF integration |
| **TOTAL** | **$2,650** | |

### 4.2 Key Components

| Component | Specification | Unit Cost |
|-----------|---------------|-----------|
| 4x Optical assembly | Fixed, 6° FOV | $250 |
| Etched reticle | BDC, illuminated | $100 |
| LRF module | Eye-safe, 800m | $350 |
| IMX462 HDR | 85dB | $75 |

### 4.3 Target Markets

- Designated marksmen
- Sniper teams (spotter)
- Long-range C-UAS defense
- Export (premium segment)

---

## DOCUMENT LINKS

- [[V-SMASH_PRO_product_spec|PRO Specification]] (base for PRO-X)
- [[V-SMASH_RE_05_SMASHX4_analysis|SMASH X4 RE Analysis]]
- [[V-SMASH_P2_05_product_variants_spec|Product Variants v2.1]]
