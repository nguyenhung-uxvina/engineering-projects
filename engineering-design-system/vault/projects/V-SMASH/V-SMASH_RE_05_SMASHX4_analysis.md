---
project: V-SMASH
phase: 0-2
type: reverse_engineering
version: 1.0
created: 2026-02-04
status: complete
foreign_system: SMASH X4
origin: Israel (Smart Shooter Ltd.)
---

# REVERSE ENGINEERING ANALYSIS
## SMASH X4 Magnified Fire Control System

**Document ID:** V-SMASH_RE_05
**Analysis Date:** 2026-02-04
**Reference:** [[SKILL_reverse_engineering]]
**Methodology:** D-M-I-R aligned RE process

---

## 1. SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Designation** | SMASH X4 |
| **Manufacturer** | Smart Shooter Ltd. |
| **Origin** | Israel |
| **Category** | Magnified AI Fire Control Optic (4x) |
| **Introduction** | Eurosatory 2022 |
| **Specimen Type** | Commercial documentation + field reports |
| **Analysis Completeness** | Level 1-2 (external + partial subsystem) |
| **Relevance** | Reference for V-SMASH PRO extended range variant |

### 1.1 Product Positioning

```
SMASH PRODUCT FAMILY - MAGNIFICATION MATRIX
══════════════════════════════════════════════════════════════════════

                    1x (Reflex)              4x (Magnified)
                    ───────────              ──────────────
  WITHOUT LRF       SMASH 3000               SMASH X4
                    740g                     1,120g
                    C-UAS / CQB              DMR / Extended

  WITH LRF          N/A                      SMASH X4 + LRF
                                             1,250g
                                             Precision / Sniper

  CONFIGURATION     Standard                 Standard + ENv
  OPTIONS                                    (Enhanced Night Vision)


TARGET APPLICATIONS:
┌─────────────────┬─────────────────┬─────────────────┐
│   SMASH 3000    │    SMASH X4     │  SMASH X4+LRF   │
├─────────────────┼─────────────────┼─────────────────┤
│ • M4/AR-15      │ • M4/AR-15      │ • SR25/M110     │
│ • Close combat  │ • DMR role      │ • Sniper        │
│ • C-UAS (200m)  │ • C-UAS (250m)  │ • Precision     │
│ • Urban         │ • Extended (400m)│ • Long range    │
└─────────────────┴─────────────────┴─────────────────┘
```

### 1.2 Operational Context

| Parameter | SMASH 3000 (1x) | SMASH X4 (4x) | Notes |
|-----------|-----------------|---------------|-------|
| **Primary Mission** | C-UAS / CQB | **Extended range / DMR** | Role differentiation |
| **Target ID Range** | ~200m | **~400m** | +2x with magnification |
| **Engagement (Ground)** | ~300m | **~400m** | +33% |
| **Engagement (Drone)** | ~200m | **~250m** | +25% |
| **User Role** | Rifleman | **Designated Marksman** | Skill level |

### 1.3 Known Deployments

| Customer | Quantity | Platform | Role | Date |
|----------|----------|----------|------|------|
| **British Army** | ~500 units | L85A3 (SA80) | C-UAS | 2024 |
| 16 Air Assault Bde | First unit | SA80 A3 | Drone defense | Mar 2024 |
| RAF Regiment | Evaluation | L85A3 | C-UAS specialist | 2024 |
| Multiple NATO | Undisclosed | Various | Evaluation | Ongoing |

---

## 2. EXTERNAL CHARACTERIZATION

### 2.1 Physical Parameters

| Parameter | Without LRF | With LRF | Notes |
|-----------|-------------|----------|-------|
| **Length** | 206 mm | 206 mm | Same |
| **Width** | 89 mm | **102 mm** | +13mm for LRF |
| **Height** | 83 mm | 83 mm | Same |
| **Weight (Sight)** | **1,120g** | **1,250g** | +130g for LRF |
| **Magnification** | 4x | 4x | Fixed power |

### 2.2 Comparison to SMASH 3000

| Parameter | SMASH 3000 | SMASH X4 | Delta | Reason |
|-----------|------------|----------|-------|--------|
| **Length** | 181 mm | 206 mm | +14% | Magnifying optics |
| **Width** | 73.5 mm | 89 mm | +21% | Larger objective |
| **Height** | 75 mm | 83 mm | +11% | Optical path |
| **Weight** | 740g | 1,120g | **+51%** | Optics + LRF option |
| **Volume** | ~1,000 cm³ | ~1,520 cm³ | +52% | |

### 2.3 Physical Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SMASH X4 EXTERNAL LAYOUT                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  FRONT VIEW              TOP VIEW                  SIDE VIEW         │
│  ┌─────────┐            ┌──────────────────┐      ┌──────────────┐  │
│  │ ◉ CMOS  │            │[PWR][M][LOCK][0] │      │    ┌─────┐   │  │
│  │  sensor │            │  ────────────────  │      │    │EYEPC│   │  │
│  ├─────────┤            │                  │      │    └─────┘   │  │
│  │         │            │    SMASH X4      │      │  ┌────────┐  │  │
│  │ 4x OBJ  │            │   ═══════════    │      │  │  4x    │  │  │
│  │  LENS   │            │   [LRF module]   │      │  │ OPTIC  │  │  │
│  │  (40mm  │            │    (optional)    │      │  │ TUBE   │  │  │
│  │  class) │            │                  │      │  └────────┘  │  │
│  └─────────┘            └──────────────────┘      │  [FTM port]  │  │
│                                                    │  [USB-C]     │  │
│                         BOTTOM                     │  [Battery]   │  │
│                         ════════════════════       └──────────────┘  │
│                         MIL-STD-1913 clamp                           │
│                         (Picatinny rail)                             │
│                                                                      │
│  DIMENSIONS: 206 × 89 × 83 mm (no LRF)                              │
│              206 × 102 × 83 mm (with LRF)                           │
│  WEIGHT:     1,120g (no LRF) / 1,250g (with LRF)                    │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.4 Interface Specifications

| Interface | Specification | Purpose | Notes |
|-----------|---------------|---------|-------|
| **Mounting** | Picatinny MIL-STD-1913 | Weapon attachment | Standard rail |
| **Power** | Smart Li-ion battery | System power | 72h / 3,600 shots |
| **Data** | USB-C | Configuration | Weapon profiles, firmware |
| **Trigger** | FTM cable | Fire timing | Proprietary connector |
| **Eyepiece** | 4x magnified | Aiming/viewing | Adjustable diopter |
| **LRF (opt)** | Class 1 laser | Range measurement | 1,000m capability |

### 2.5 Environmental Ratings

| Parameter | Rating | Standard |
|-----------|--------|----------|
| **Operating temp** | -32°C to +49°C | MIL-STD-810G |
| **Storage temp** | -51°C to +71°C | MIL-STD-810G |
| **Shock** | Method 516.6 | MIL-STD-810G |
| **Vibration** | Method 514.6 | MIL-STD-810G |
| **EMC** | EMI qualified | MIL-STD-461E |
| **Sealing** | IP67 (inferred) | IEC 60529 |

---

## 3. SUBSYSTEM DECOMPOSITION

### 3.1 Major Assemblies

```
SMASH X4 SUBSYSTEM ARCHITECTURE
══════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│                        SMASH X4 SYSTEM                              │
├────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐           │
│  │   SENSOR     │   │  PROCESSING  │   │   OPTICAL    │           │
│  │   MODULE     │   │    UNIT      │   │   MODULE     │  ← LARGER │
│  │              │   │              │   │   (4x)       │           │
│  │ • CMOS cam   │──▶│ • SoC/FPGA   │──▶│ • 4x magn.   │           │
│  │ • IMU 6-axis │   │ • AI model   │   │   objective  │           │
│  │ • Wide FOV   │   │ • Tracker    │   │ • Eyepiece   │           │
│  │   lens       │   │ • Ballistic  │   │ • See-thru   │           │
│  │              │   │   computer   │   │   combiner   │           │
│  └──────────────┘   └──────┬───────┘   │ • Etched     │           │
│         │                  │           │   reticle    │  ← BACKUP │
│         │                  │           └──────────────┘           │
│         │           ┌──────▼───────┐                               │
│         │           │    FIRE      │   ┌──────────────┐           │
│         │           │   TIMING     │   │    LRF       │  ← OPTION │
│         │           │   (FTM)      │   │   MODULE     │           │
│         │           │              │   │              │           │
│         │           │ • Trigger    │   │ • Class 1    │           │
│         │           │   sensor     │   │   laser      │           │
│         │           │ • Gate logic │   │ • 1000m      │           │
│         │           │ • Precision  │   │   range      │           │
│         │           │   timer      │   │ • Auto input │           │
│         │           └──────┬───────┘   └──────────────┘           │
│         │                  │                                       │
│  ┌──────▼──────┐    ┌──────▼───────┐   ┌──────────────┐           │
│  │   POWER     │    │   WEAPON     │   │   USER       │           │
│  │   MODULE    │    │  INTERFACE   │   │  INTERFACE   │           │
│  │             │    │              │   │              │           │
│  │ • Smart     │───▶│ • FTM cable  │   │ • Buttons    │           │
│  │   Li-ion    │    │ • Connector  │   │ • Status     │           │
│  │ • BMS       │    │              │   │ • USB-C      │           │
│  │ • 72h       │    │              │   │ • App        │           │
│  └─────────────┘    └──────────────┘   └──────────────┘           │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘

KEY DIFFERENCES FROM SMASH 3000:
• +Magnified optical path (4x vs 1x)
• +Optional LRF module (1000m)
• +Etched reticle (battery-free backup)
• +Enhanced ballistic compensation (wind, inclination, cant)
• +Clip-on night vision compatibility
• Larger/heavier package (+51% weight)
```

### 3.2 Subsystem Mass Budget (Estimated)

| Subsystem | SMASH 3000 | SMASH X4 | SMASH X4+LRF | Notes |
|-----------|------------|----------|--------------|-------|
| Sensor Module | ~140g | ~160g | ~160g | Similar sensor |
| Processing Unit | ~80g | ~90g | ~90g | More ballistic calc |
| **Optical Module** | ~100g | **~350g** | ~350g | **4x magnification** |
| Fire Control (FTM) | ~40g | ~40g | ~40g | Same mechanism |
| **LRF Module** | N/A | N/A | **~130g** | **Optional** |
| Power Module | ~130g | ~140g | ~140g | Same capacity |
| Weapon Interface | ~80g | ~90g | ~90g | Heavier mount |
| Housing/Structure | ~120g | ~250g | ~260g | Larger body |
| **TOTAL** | **~740g** | **~1,120g** | **~1,250g** | |

### 3.3 Optical System Detail

```
SMASH X4 OPTICAL PATH
══════════════════════════════════════════════════════════════════════

SCENE ──▶ [OBJECTIVE] ──▶ [ERECTOR] ──▶ [COMBINER] ──▶ [EYEPIECE] ──▶ EYE
           (4x mag)        (image      (reticle +      (focus)
           ~40mm           inversion)   AI overlay)

                           ┌──────────┐
                           │ ETCHED   │ ← Battery-free backup
                           │ RETICLE  │
                           └────┬─────┘
                                │
                           ┌────▼─────┐
         [LED/OLED] ──────▶│ COMBINER │ ← AI-generated markers
         (AI overlay)      └────┬─────┘
                                │
                           ┌────▼─────┐
                           │ SEE-THRU │ ← Combined view
                           │  OPTIC   │
                           └──────────┘

OPERATING MODES:
┌─────────────────────────────────────────────────────────────────┐
│ MODE            │ POWER │ RETICLE    │ AI OVERLAY │ USE CASE   │
├─────────────────┼───────┼────────────┼────────────┼────────────┤
│ Etched Reticle  │ OFF   │ Etched ✓   │ None       │ Emergency  │
│ Day Mode        │ ON    │ Etched ✓   │ Projected  │ Standard   │
│ Night Mode      │ ON    │ Low-light  │ Projected  │ Low-light  │
│ Clip-On Mode    │ ON    │ Via NVD    │ Projected  │ Thermal/NV │
└─────────────────┴───────┴────────────┴────────────┴────────────┘
```

---

## 4. FUNCTIONAL RECONSTRUCTION

### 4.1 Overall Function Statement

> **"Provide AI-optimized fire control with 4x magnification for extended-range precision engagement of static and moving targets, with optional laser ranging and clip-on night vision compatibility."**

### 4.2 Function Structure (SMASH X4)

```
SMASH X4 FUNCTION STRUCTURE
══════════════════════════════════════════════════════════════════════

OVERALL FUNCTION: Extended-range AI-optimized precision fire control
                  with magnified optics and optional LRF

├── F1: ACQUIRE TARGET (Extended Range)
│   ├── F1.1: Capture scene image ────────── [WP: CMOS wide-FOV sensor]
│   ├── F1.2: Magnify scene (4x) ─────────── [WP: 4x optical system] ← NEW
│   ├── F1.3: Detect targets in scene ────── [WP: AI object detection]
│   ├── F1.4: Classify target type ───────── [WP: Neural classifier]
│   ├── F1.5: Measure range (manual) ─────── [WP: Size-based estimation]
│   └── **F1.6: Measure range (LRF)** ────── [WP: Laser rangefinder] ← OPTION
│
├── F2: TRACK TARGET MOTION
│   ├── F2.1: Initialize track ───────────── [WP: Detection-to-track]
│   ├── F2.2: Update track state ─────────── [WP: Kalman/IMM filter]
│   ├── F2.3: Predict future position ────── [WP: Motion extrapolation]
│   └── F2.4: Handle track loss ──────────── [WP: Re-acquisition logic]
│
├── F3: COMPUTE FIRE SOLUTION (Enhanced)
│   ├── F3.1: Sense weapon orientation ───── [WP: MEMS IMU 6-axis]
│   ├── F3.2: Retrieve weapon profile ────── [WP: Multi-caliber database]
│   ├── F3.3: Calculate trajectory ───────── [WP: Point-mass 3DOF model]
│   ├── F3.4: Compensate for wind ────────── [WP: Manual/sensor input] ← ENHANCED
│   ├── F3.5: Compensate for inclination ─── [WP: Inclinometer] ← ENHANCED
│   ├── F3.6: Compensate for cant ────────── [WP: Cant sensor] ← ENHANCED
│   └── F3.7: Determine alignment error ──── [WP: Vector comparison]
│
├── F4: CONTROL FIRE AUTHORIZATION (FTM)
│   ├── F4.1: Sense trigger pressure ─────── [WP: Force sensor]
│   ├── F4.2: Evaluate hit probability ───── [WP: Threshold logic]
│   ├── F4.3: Gate fire authorization ────── [WP: Boolean AND logic]
│   └── F4.4: Time trigger release ───────── [WP: Precision FTM <5ms]
│
├── F5: ACTUATE TRIGGER MECHANISM
│   ├── F5.1: Hold trigger (gate closed) ─── [WP: FTM actuator]
│   ├── F5.2: Release trigger (gate open) ── [WP: FTM release]
│   └── F5.3: Detect fire event ──────────── [WP: Recoil sense]
│
├── F6: PROVIDE OPERATOR FEEDBACK (Magnified)
│   ├── F6.1: Display magnified scene ────── [WP: 4x see-through optic] ← NEW
│   ├── F6.2: Display etched reticle ─────── [WP: Glass etching] ← NEW (backup)
│   ├── F6.3: Overlay AI aim point ───────── [WP: LED/OLED projection]
│   ├── F6.4: Indicate target lock ───────── [WP: Bounding box display]
│   ├── F6.5: Show fire readiness ────────── [WP: Color/symbol change]
│   └── F6.6: Display system status ──────── [WP: Status indicators]
│
├── **F7: ENABLE NIGHT OPERATIONS** ────────── ← NEW FUNCTION
│   ├── F7.1: Provide low-light mode ─────── [WP: Sensor gain adjustment]
│   └── F7.2: Interface with NVD clip-on ─── [WP: Optical passthrough]
│
└── F_AUX: AUXILIARY FUNCTIONS
    ├── F_AUX.1: Manage power ────────────── [WP: Smart BMS + Li-ion]
    ├── F_AUX.2: Store weapon profiles ───── [WP: Multi-caliber memory]
    ├── F_AUX.3: Enable configuration ────── [WP: USB-C + mobile app]
    ├── F_AUX.4: Update firmware ─────────── [WP: OTA-capable]
    └── F_AUX.5: Fail-safe to manual ─────── [WP: Etched reticle fallback]
```

### 4.3 New Working Principles (vs SMASH 3000)

| ID | Subfunction | SMASH 3000 WP | SMASH X4 WP | Application |
|----|-------------|---------------|-------------|-------------|
| WP-X1 | F1.2 Magnification | 1x reflex | **4x optical tube** | Extended ID range |
| WP-X2 | F1.6 Range (LRF) | N/A | **Class 1 laser 1km** | Precision ranging |
| WP-X3 | F3.4 Wind comp | N/A | **Manual/sensor input** | Long-range accuracy |
| WP-X4 | F3.5 Inclination | Basic | **Enhanced inclinometer** | Hill shooting |
| WP-X5 | F3.6 Cant comp | N/A | **Cant sensor** | Angled shots |
| WP-X6 | F6.2 Backup reticle | N/A | **Etched glass** | Battery-free aim |
| WP-X7 | F7.2 NVD interface | N/A | **Optical passthrough** | Night capability |

---

## 5. PERFORMANCE ESTIMATION

### 5.1 Engagement Range Comparison

| Target Type | SMASH 3000 (1x) | SMASH X4 (4x) | Improvement |
|-------------|-----------------|---------------|-------------|
| **Drone detection** | ~300m | ~500m | +67% |
| **Drone engagement** | ~200m | ~250m | +25% |
| **Ground ID** | ~200m | ~400m | +100% |
| **Ground engagement** | ~300m | ~400m | +33% |
| **Max LRF range** | N/A | **1,000m** | NEW |

### 5.2 Ballistic Compensation Capabilities

| Factor | SMASH 3000 | SMASH X4 | Notes |
|--------|------------|----------|-------|
| **Range** | Size-based est. | **LRF (1000m)** | Much more accurate |
| **Wind** | None/basic | **Manual input** | User enters windage |
| **Inclination** | Basic | **Enhanced** | Uphill/downhill |
| **Cant** | None | **Compensated** | Prevents off-axis error |
| **Temperature** | None | Likely compensated | Affects ballistics |
| **Humidity** | Claimed | Likely compensated | Minor effect |

### 5.3 Supported Weapon Platforms

| Platform | Caliber | Role | Range Benefit |
|----------|---------|------|---------------|
| M4 / AR-15 | 5.56mm | Carbine | ID improvement |
| **SR25 / M110** | **7.62mm** | **DMR / Sniper** | **Full system benefit** |
| L85A3 (SA80) | 5.56mm | Assault rifle | British deployment |
| AR-10 variants | 7.62mm | DMR | Extended range |

---

## 6. DESIGN PHILOSOPHY ASSESSMENT

### 6.1 X4 vs 3000 Paradigm Comparison

| Indicator | SMASH 3000 | SMASH X4 | Philosophy |
|-----------|------------|----------|------------|
| **Primary role** | C-UAS / CQB | **DMR / Precision** | Extended range |
| **Weight priority** | Aggressive (-33%) | **Capability over weight** | +51% acceptable |
| **Complexity** | Minimal | **Enhanced ballistics** | More compensation |
| **Backup mode** | None specified | **Etched reticle** | Critical for snipers |
| **Night capability** | Low-light mode | **Clip-on compatible** | 24/7 operations |
| **Price point** | Standard | **Premium** | Feature-driven |

### 6.2 Designer's Paradigm Statement (X4)

> **"Extend AI-assisted fire control to designated marksman and precision roles through magnified optics, laser ranging, and enhanced ballistic compensation, while maintaining battery-free backup capability for critical missions."**

### 6.3 Trade-off Analysis

| Trade-off | SMASH X4 Priority | Over | Rationale |
|-----------|-------------------|------|-----------|
| 1 | **Extended range** | Weight | DMR mission requirement |
| 2 | **Precision** | Simplicity | Enhanced compensation |
| 3 | **Redundancy** | Cost | Etched reticle backup |
| 4 | **Night capability** | Integration | Clip-on compatibility |
| 5 | **Modularity** | Compactness | Optional LRF |

---

## 7. APPLICATION RECOMMENDATIONS

### 7.1 New Requirements from SMASH X4 RE

| ID | Category | Requirement | Priority | Rationale |
|----|----------|-------------|----------|-----------|
| **R77** | Optics | Magnification option (≥3x) for PRO variant | W | Extended ID range for 12.7mm |
| **R78** | Performance | Optional LRF integration (≥500m) | W | Precision ranging for 12.7mm |
| **R79** | Ballistics | Wind compensation input | W | Long-range accuracy |
| **R80** | Ballistics | Inclination compensation | W | Hill/mountain terrain |
| **R81** | Ballistics | Cant compensation | W | Angled shooting positions |
| **R82** | Fail-safe | Etched reticle backup (magnified variant) | D | Battery-free aiming |
| **R83** | Night | Clip-on NVD/thermal compatibility | D | 24/7 operations |

### 7.2 V-SMASH PRO Enhancement Path

```
V-SMASH PRO EVOLUTION OPTIONS
══════════════════════════════════════════════════════════════════════

CURRENT V-SMASH PRO          ENHANCED V-SMASH PRO (X4-Inspired)
───────────────────          ──────────────────────────────────
• 1x reflex optic            • **3-4x magnified optic** (Option B)
• CMOS + Thermal             • CMOS + Thermal (retained)
• Sensor fusion              • Sensor fusion (retained)
• No LRF                     • **Optional LRF (500-1000m)**
• Basic ballistics           • **Enhanced compensation (wind/inc/cant)**
• No backup reticle          • **Etched reticle backup**
• Integrated NV              • Integrated NV (retained)

PRODUCT VARIANT MATRIX:

                    1x (Reflex)              3-4x (Magnified)
                    ───────────              ────────────────
  V-SMASH LITE      ✓ Standard               Not planned
                    $3,000

  V-SMASH PRO       ✓ Standard               ✓ Option (PRO-X)
                    $4,500-5,000             $6,000-7,000 (est.)

  V-SMASH PRO       N/A                      ✓ Option (PRO-X+LRF)
  + LRF                                      $7,000-8,000 (est.)
```

### 7.3 Technology Insertion Candidates

| Priority | Technology | SMASH X4 WP | V-SMASH Approach |
|----------|------------|-------------|------------------|
| 1 | Etched reticle | Glass etching | Include in magnified variant |
| 2 | LRF integration | Class 1 laser | Source commercial module |
| 3 | Wind compensation | Manual input | IMU + user input |
| 4 | Inclination comp | Inclinometer | Use IMU data |
| 5 | Cant compensation | Cant sensor | Use IMU data |
| 6 | Clip-on mode | Optical design | Design for thermal clip-on |

### 7.4 12.7mm Application Analysis

| Feature | SMASH X4 (5.56/7.62) | V-SMASH PRO-X (12.7mm) | Adaptation |
|---------|---------------------|------------------------|------------|
| **Magnification** | 4x | **3-4x** | Appropriate for 12.7mm range |
| **LRF range** | 1,000m | **1,500m** | Extended for 12.7mm envelope |
| **Wind comp** | Manual input | **Enhanced (12.7mm sensitive)** | Critical for heavy round |
| **Recoil tolerance** | Rifle-class | **HMG-class** | Ruggedized design |
| **Mount** | Picatinny | **Heavy-duty Picatinny** | 12.7mm recoil |

---

## 8. CROSS-REFERENCE TO V-SMASH

### 8.1 Function Comparison

| SMASH X4 Function | V-SMASH Equivalent | Gap Analysis |
|-------------------|-------------------|--------------|
| F1: Acquire (magnified) | F1: Acquire | ⚠️ No magnification option |
| F1.6: LRF ranging | F1.4: Passive ranging | ⚠️ LRF more accurate |
| F3.4-3.6: Enhanced ballistics | F3: Basic ballistics | ⚠️ Need compensation |
| F6.2: Etched reticle | F_AUX.5: Fail-safe | ⚠️ Need backup reticle |
| F7: Night operations | F1.5: Sensor fusion (PRO) | ✅ V-SMASH PRO better |

### 8.2 V-SMASH Competitive Positioning (Updated)

| Feature | SMASH X4 | V-SMASH LITE | V-SMASH PRO | V-SMASH PRO-X (Proposed) |
|---------|----------|--------------|-------------|--------------------------|
| **Price** | ~$25,000+ | **$3,000** | **$5,000** | **$7,000** |
| **Magnification** | 4x | 1x | 1x | **3-4x** |
| **LRF** | 1,000m | None | None | **500-1,000m** |
| **Thermal** | Clip-on only | Clip-on | **Integrated** | **Integrated** |
| **Sensor fusion** | None | None | **Yes** | **Yes** |
| **Etched backup** | Yes | No | No | **Yes** |
| **Wind/cant comp** | Yes | No | Basic | **Enhanced** |
| **Platform** | Rifle | Rifle | Rifle/12.7mm | **12.7mm optimized** |

---

## 9. LESSONS LEARNED

### 9.1 Key Insights from SMASH X4 RE

| Insight | Implication for V-SMASH |
|---------|-------------------------|
| **Magnification extends effective range 2x** | Consider PRO-X variant for 12.7mm |
| **LRF critical for precision** | Integrate LRF for 12.7mm application |
| **Etched reticle is DMR requirement** | Include for mission-critical backup |
| **Wind/inclination/cant matter at range** | Enhance ballistic computer for 12.7mm |
| **51% weight increase acceptable for DMR** | PRO-X can be heavier if needed |
| **British Army deploying for C-UAS** | 4x effective against drones too |

### 9.2 PRO-X Variant Recommendation

Based on SMASH X4 analysis, recommend exploring **V-SMASH PRO-X** variant:

| Parameter | V-SMASH PRO | V-SMASH PRO-X (Proposed) |
|-----------|-------------|--------------------------|
| **Target price** | $4,500-5,000 | $6,500-7,500 |
| **Magnification** | 1x | 3-4x |
| **LRF** | None | 500-1,000m optional |
| **Weight** | ~1,100g | ~1,500g |
| **Ballistics** | Basic | Enhanced (wind/inc/cant) |
| **Backup** | Fail-safe | **Etched reticle** |
| **Primary platform** | Rifle / 12.7mm | **12.7mm optimized** |

---

## 10. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-04 | Initial SMASH X4 RE analysis |

---

## APPENDIX A: SOURCE MATERIALS

### A.1 Primary Sources

| Source | Type | URL |
|--------|------|-----|
| Smart Shooter Official | Product page | [smart-shooter.com/gun/smash-x4](https://www.smart-shooter.com/gun/smash-x4/) |
| SMASH X4 Datasheet | Technical PDF | [PDF link](https://www.smart-shooter.com/wp-content/uploads/2024/03/SMASH-X4.pdf) |
| EDR Magazine | Eurosatory 2022 | [Product unveil](https://www.edrmagazine.eu/smartshooter-unveils-another-member-of-the-smash-family-the-smash-x4-a-fire-control-system-with-a-x4-magnifying-optic-scope) |
| Army Recognition | British trials | [British Army SMASH X4](https://armyrecognition.com/news/army-news/army-news-2024/british-army-tries-israeli-smartsights-mounted-on-rifle-against-fpv-uav) |
| Viking Arms PMD | Distributor | [SMASH X4](https://www.vikingarmsdefence.com/our-products/smartshooter-smash-x4/) |
| Joint Forces News | Product news | [X4 unveil](https://www.joint-forces.com/defence-equipment-news/54395-smart-shooter-unveils-smash-x4-fire-control-system) |

### A.2 Related V-SMASH Documents

- [[V-SMASH_00_project_brief|Project Brief v1.4]]
- [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+ RE (Gen 2)]]
- [[V-SMASH_RE_04_SMASH3000_analysis|SMASH 3000 RE (Gen 3)]]
- [[V-SMASH_RE_02_ARCAS_analysis|ARCAS RE]]
- [[V-SMASH_RE_03_ARBEL_analysis|ARBEL RE]]
- [[V-SMASH_P1_01_requirements_list|Requirements List v1.3]]
- [[V-SMASH_P2_01_function_structure|Function Structure v1.2]]

---

*This document was generated using the Engineering Design System reverse engineering methodology (D-M-I-R aligned). It analyzes the SMASH X4 magnified fire control system to inform potential V-SMASH PRO-X variant development for 12.7mm HMG applications.*
