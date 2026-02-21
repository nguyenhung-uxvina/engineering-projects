---
project: V-SMASH
product: MARITIME
designation: VSM-M
version: 1.0
created: 2026-02-04
status: approved
vdi_score: 75%
target_price: $6,500
---

# V-SMASH MARITIME - PRODUCT SPECIFICATION
## Naval/Coastal AI Fire Control System

**Product Code:** VSM-M
**VDI 2225 Score:** 75% ✅
**Target Price:** $6,500
**Delivery:** Phase 2 (Month 26)

---

## PHASE 1: REQUIREMENTS

### 1.1 Product-Specific Requirements

| Req ID | Category | Requirement | Value | Type | Source |
|--------|----------|-------------|-------|------|--------|
| R01 | Performance | Detection range (day) | ≥300m | D | Standard |
| R02 | Performance | Detection range (night) | ≥200m | D | ODI S1-22 |
| R03 | Performance | Hit improvement | ≥3x | D | Wave motion |
| R04 | Performance | Sea state operation | Up to SS4 | D | Vietnam |
| R05 | Environmental | Sealing | IP68 (1m submersion) | D | Splash |
| R06 | Environmental | Salt fog | 500 hours | D | MIL-STD-810H |
| R07 | Environmental | Operating temp | -10°C to +55°C | D | Vietnam |
| R08 | Environmental | Humidity | 100% condensing | D | Marine |
| R09 | Sensor | Primary sensor | HDR CMOS | D | Standard |
| R10 | Sensor | Thermal sensor | LWIR | D | Night ops |
| R11 | Physical | Weight | ≤1.5 kg | D | Portable |
| R12 | Motion | Wave compensation | 6-DOF input | D | Marine |
| R13 | Motion | Horizon stabilization | Required | D | Marine |
| R14 | Protection | Anti-corrosion | Marine-grade | D | Salt |
| R15 | Protection | Lens wash | Wiper + washer | W | Spray |
| R16 | Interface | Picatinny mount | MIL-STD-1913 | D | Standard |

### 1.2 Marine-Specific Features

| Feature | Standard PRO | MARITIME | Reason |
|---------|--------------|----------|--------|
| Sealing | IP67 | IP68 | Splash/submersion |
| Salt fog | 48 hours | 500 hours | Long-term exposure |
| Coating | Anodize | Marine anodize + conformal | Corrosion |
| Material | Al 6061 | Al 5083 marine grade | Salt resistance |
| Lens | Standard | Hydrophobic + wiper | Spray |
| Motion comp | None | 6-DOF wave compensation | Ship motion |

---

## PHASE 2: CONCEPTUAL DESIGN

### 2.1 Function Structure (Maritime-Specific)

```
V-SMASH MARITIME FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════

F1: ACQUIRE TARGET INFORMATION
├── F1.1: Capture scene image ────────── CMOS HDR 1080p60
├── F1.1T: Capture thermal image ─────── LWIR 160x120
├── F1.5: Fuse sensor data ───────────── Weighted blend
├── F1.2: Detect targets ─────────────── YOLOv8-nano + maritime
├── F1.3: Classify target type ───────── Marine drone classes
└── F1.4: Measure range ──────────────── Passive + horizon ref

F2: TRACK TARGET MOTION (Wave-Compensated)
├── F2.2: Update track state ─────────── IMM Filter
├── F2.2W: Compensate wave motion ────── 6-DOF input
├── F2.2H: Stabilize to horizon ──────── Gyro-referenced
├── F2.5: Manage multiple tracks ─────── Fixed pool (5)
└── F2.6: Associate detections ───────── Hungarian Algorithm

F3: COMPUTE FIRE SOLUTION (Ship Motion)
├── F3.1: Sense weapon orientation ───── 9-axis IMU
├── F3.1S: Input ship motion ─────────── 6-DOF from AHRS
├── F3.2: Retrieve weapon profile ────── Database lookup
├── F3.3: Calculate trajectory ───────── Point-mass 3DOF + motion
└── F3.4: Determine alignment error ──── Vector comparison

F_AUX: AUXILIARY FUNCTIONS (Marine-Enhanced)
├── F_AUX.1: Manage power ────────────── Marine-rated PMIC
├── F_AUX.6: Protect lens ────────────── Wiper + washer
├── F_AUX.7: Heat lens ───────────────── Anti-fog heater
└── F_AUX.5: Provide fail-safe ───────── Mechanical bypass
```

### 2.2 Working Principles Selected

| Function | Working Principle | Specification |
|----------|------------------|---------------|
| F2.2W | Wave compensation | 6-DOF motion input from ship |
| F2.2H | Horizon stabilization | Gyro-referenced level |
| F3.1S | Ship motion input | Serial from ship AHRS |
| F_AUX.6 | Lens wiper | Motorized, fresh water wash |
| F_AUX.7 | Lens heater | 3W resistive, auto |

---

## PHASE 3: EMBODIMENT DESIGN

### 3.1 Layout Design

```
V-SMASH MARITIME - LAYOUT
═══════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────┐
    │                MARINE-PROTECTED ASSEMBLY                 │
    │  ┌─────────────────────────────────────────────────┐    │
    │  │              WIPER + WASHER SYSTEM              │    │
    │  │  ┌─────────┐  ┌─────────┐  ┌─────────────────┐ │    │
    │  │  │ WIPER   │  │ WASHER  │  │ HYDROPHOBIC     │ │    │
    │  │  │ MOTOR   │  │ NOZZLE  │  │ WINDOW          │ │    │
    │  │  └─────────┘  └─────────┘  └─────────────────┘ │    │
    │  └─────────────────────────────────────────────────┘    │
    │                         │                                │
    │  ┌─────────────────────────────────────────────────┐    │
    │  │              SENSOR ASSEMBLY (IP68)             │    │
    │  │  ┌─────────┐  ┌─────────┐  ┌─────────────────┐ │    │
    │  │  │ CMOS    │  │ THERMAL │  │ HEATER          │ │    │
    │  │  │ HDR     │  │ LWIR    │  │ (3W)            │ │    │
    │  │  └─────────┘  └─────────┘  └─────────────────┘ │    │
    │  └─────────────────────────────────────────────────┘    │
    │                         │                                │
    │  ┌─────────────────────────────────────────────────┐    │
    │  │              PROCESSING (Conformal Coated)      │    │
    │  │  ┌───────────┐  ┌───────────┐  ┌─────────────┐ │    │
    │  │  │ JETSON    │  │ 9-AXIS    │  │ SHIP MOTION │ │    │
    │  │  │ NANO      │  │ IMU       │  │ INTERFACE   │ │    │
    │  │  └───────────┘  └───────────┘  └─────────────┘ │    │
    │  └─────────────────────────────────────────────────┘    │
    │                                                          │
    │  ┌─────────────────────────────────────────────────┐    │
    │  │  MARINE AL 5083 HOUSING + CONFORMAL COAT        │    │
    │  └─────────────────────────────────────────────────┘    │
    └─────────────────────────────────────────────────────────┘

Dimensions: 170mm (L) × 90mm (W) × 110mm (H)
Weight: 1.5 kg (with battery)
Sealing: IP68 (1m for 30 min)
Salt Fog: 500 hours
```

### 3.2 DfX Review

| DfX Category | Score | Notes |
|--------------|-------|-------|
| DfM | 6/10 | Marine coatings add steps |
| DfA | 7/10 | Wiper mechanism adds complexity |
| DfR | 8/10 | Marine-proven materials |
| DfT | 6/10 | Salt fog chamber testing |
| DfC | 5/10 | Marine materials costly |
| DfE | 9/10 | IP68, 500hr salt fog |
| DfMaint | 7/10 | Wiper blade replacement |
| **OVERALL** | **6.9/10** | Marine-specific design |

### 3.3 Corrosion Protection

| Component | Protection Method |
|-----------|-------------------|
| Housing | Al 5083 marine + hard anodize |
| Fasteners | 316 stainless steel |
| PCB | Conformal coating (acrylic) |
| Connectors | Marine-rated, gold contacts |
| Window | Sapphire, hydrophobic coat |
| O-rings | Viton (salt-resistant) |

---

## PHASE 4: DETAIL DESIGN

### 4.1 Bill of Materials Summary

| Category | Cost | Notes |
|----------|------|-------|
| Processing | $200 | Jetson Nano |
| Sensors | $960 | CMOS + thermal |
| Optics | $155 | Sapphire + heater |
| Power | $45 | Marine-rated |
| Actuation | $15 | Solenoid |
| Wiper system | $80 | Motor + reservoir |
| Housing (Al 5083) | $250 | Marine anodize |
| Conformal coat | $50 | Full PCB coverage |
| Misc | $45 | Marine connectors |
| **SUBTOTAL** | **$1,800** | |
| Labor + Test | $250 | Salt fog testing |
| Software | $150 | Wave compensation |
| **TOTAL** | **$2,100** | |

### 4.2 Test Requirements

| Test | Standard | Criteria |
|------|----------|----------|
| Salt fog | MIL-STD-810H 509.7 | 500 hours |
| Submersion | IP68 | 1m for 30 min |
| Temperature | MIL-STD-810H | -10°C to +55°C |
| Wave motion | Internal | Sea State 4 tracking |
| Spray | Internal | Continuous for 1 hour |

### 4.3 Target Markets

- Vietnam Navy patrol boats
- Coast Guard vessels
- Island garrison defense
- Maritime security contractors

---

## DOCUMENT LINKS

- [[V-SMASH_PRO_product_spec|PRO Specification]] (sensor base)
- [[V-SMASH_P2_05_product_variants_spec|Product Variants v2.1]]
- [[V-SMASH_P1_01_requirements_list|Requirements List]]
