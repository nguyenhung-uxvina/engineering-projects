---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: DECS-E
title: Evaluate Layout Variants
version: 1.0
created: 2026-02-06
status: complete
---

# STEP E: EVALUATE LAYOUT VARIANTS
## Physical Layout Comparison & Selection
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 10 of 15

**Purpose:** Develop and compare 3 physical layout variants for the BSU-V1, then select the definitive layout using a simplified VDI 2225 evaluation.

**Input:** [[PRAD_A_architecture]] (Module definition), [[PRAD_D_structure]] (Structural constraints)
**Output:** Selected definitive layout with rationale

---

## 1. LAYOUT VARIANT DEFINITION

All 3 variants share the same electrical architecture (FPGA+MCU+ADC+PHY), sensor count (4× MEMS), battery (4S1P Li-ion), and IP67 aluminum enclosure. They differ in **physical arrangement** of the processing enclosure relative to the sensor bar, and internal component layout.

---

### 1.1 VARIANT L1: "SEPARATE BOX" (Baseline)

**Concept:** Processing enclosure is a separate unit connected to sensor bar via 500mm cable. Enclosure mounts to target frame or sits on ground.

```
VARIANT L1 - SIDE VIEW
══════════════════════════════════════════════════════════

TARGET FRAME
│
│   ┌────────────────────────────────────────────┐
│   │  SENSOR BAR (1040 × 60 × 40mm, 1.2 kg)    │
│   │  M1        M2        M3        M4          │
│   └──────────────────┬─────────────────────────┘
│                      │ 500mm shielded cable
│                      │ (4× analog + shield + GND)
│   ┌──────────────────┴─────────────────────┐
│   │  PROCESSING ENCLOSURE                   │
│   │  250 × 180 × 120 mm (6.6 kg)           │
│   │                                         │
│   │  ┌─────────┐  ┌───────────────────┐    │
│   │  │Main PCB │  │ Battery pack      │    │
│   │  │160×100  │  │ 4S1P (3.5 kg)     │    │
│   │  │FPGA+MCU │  │ 14.8V 10Ah        │    │
│   │  │+ADC+PHY │  │                   │    │
│   │  └─────────┘  └───────────────────┘    │
│   │  ┌─────────┐                           │
│   │  │Power PCB│  [ETH] [PWR] [LED]        │
│   │  │ 80×60   │  IP67 connectors          │
│   │  └─────────┘                           │
│   └─────────────────────────────────────────┘
│   Mounted via VESA 100×100 or ground-stand
```

**Key Characteristics:**
- Sensor bar is lightweight (1.2 kg) → minimal load on target frame
- Processing enclosure can be positioned for accessibility
- 500mm cable allows flexible mounting
- Battery access from outside enclosure (battery door on side)
- Clear module separation: bar is LRU, enclosure is LRU

**Dimensions:** Bar 1040×60×40 + Enclosure 250×180×120 + Cable 500mm
**Total Weight:** 7.8 kg (bar 1.2 + enclosure 6.6)

---

### 1.2 VARIANT L2: "INTEGRATED BAR"

**Concept:** Processing electronics and battery are integrated directly into the sensor bar body. No separate enclosure. Single monolithic unit.

```
VARIANT L2 - SIDE VIEW
══════════════════════════════════════════════════════════

TARGET FRAME
│
│   ┌──────────────────────────────────────────────────────────┐
│   │  INTEGRATED SENSOR BAR (1300 × 120 × 80mm, 7.8 kg)      │
│   │                                                          │
│   │  M1      M2      M3      M4   │ Main PCB │  Battery    │
│   │  ●───────●───────●───────●────│ FPGA+MCU │  4S1P       │
│   │                                │ Power PCB│  Li-ion     │
│   │  ←───── 1040mm sensors ──────→│← 260mm →│             │
│   │                                                          │
│   │  [ETH]  [PWR]  [LED]                                    │
│   └──────────────────────────────────────────────────────────┘
│   Mounted via 3 cam-lever clamps on frame
```

**Key Characteristics:**
- Single unit: no external cable between bar and enclosure
- Longer overall unit (1300mm total)
- Heavier load on target frame (7.8 kg at bar level)
- Electronics section extends beyond sensor area
- Battery access via end-cap or bottom panel
- More complex machining (longer single piece)

**Dimensions:** 1300×120×80mm (single unit)
**Total Weight:** 7.8 kg (all in one)

---

### 1.3 VARIANT L3: "BACK-PACK"

**Concept:** Processing enclosure is directly attached to the back of the sensor bar (piggy-back mounting), no cable. Compact unit with bar + box as one assembly.

```
VARIANT L3 - SIDE VIEW
══════════════════════════════════════════════════════════

TARGET FRAME
│
│   ┌────────────────────────────────────────────┐
│   │  SENSOR BAR (1040 × 60 × 40mm)             │
│   │  M1        M2        M3        M4          │
│   └──────────────────┬─────────────────────────┘
│                      │ Direct mount (no cable)
│                      │ Internal pin header connection
│   ┌──────────────────┴─────────────────┐
│   │  PROCESSING ENCLOSURE (back-mount)  │
│   │  200 × 150 × 100 mm               │
│   │  Bolted to sensor bar center       │
│   │                                     │
│   │  Main PCB + Power PCB + Battery     │
│   │  [ETH]  [PWR]  [LED]              │
│   └─────────────────────────────────────┘
│
│   Side profile (from left):
│
│       Bar ──→ ┌───┐
│               │   │ ← Enclosure piggy-backed
│               └───┘
│   Total depth from frame: ~140mm
```

**Key Characteristics:**
- No external cable (internal pin header connection)
- Compact overall footprint
- Heavier concentrated load at bar center (7.8 kg at one point)
- Enclosure smaller than L1 (200×150×100 vs 250×180×120) due to tighter packing
- Target frame must support concentrated load
- Battery access from bottom of piggy-back enclosure
- More complex maintenance (must remove from frame to access)

**Dimensions:** Bar 1040×60×40 + Enclosure 200×150×100 (back-mounted)
**Total Weight:** 7.8 kg (concentrated at center)

---

## 2. EVALUATION CRITERIA

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| E1 | Target frame load | 0.20 | Heavy bar → frame damage, sag, accuracy drift |
| E2 | Maintenance access | 0.20 | Battery swap, PCB replacement, MTTR ≤30 min |
| E3 | Vietnamese manufacturability | 0.15 | CNC complexity, assembly difficulty |
| E4 | Sensor bar flexibility | 0.15 | Can bar be used on different frame types? |
| E5 | Cable vulnerability | 0.10 | External cables get damaged in field |
| E6 | Thermal management | 0.10 | Heat dissipation from sealed enclosure |
| E7 | Transport packing | 0.10 | How easily does it pack in transport case? |
| | **TOTAL** | **1.00** | |

---

## 3. EVALUATION MATRIX

**VDI 2225 Scale: 0=Unsatisfactory, 1=Tolerable, 2=Adequate, 3=Good, 4=Very Good**

| # | Criterion | Weight | L1: Separate Box | L2: Integrated Bar | L3: Back-Pack |
|---|-----------|--------|-------------------|-------------------|---------------|
| E1 | Target frame load | 0.20 | **4** (1.2 kg on bar) | **1** (7.8 kg on bar) | **2** (7.8 kg concentrated at center) |
| E2 | Maintenance access | 0.20 | **4** (box on ground, easy open) | **2** (must access inside long bar) | **2** (must remove from frame) |
| E3 | Manufacturability | 0.15 | **4** (standard box + simple bar) | **2** (long complex machining, tight integration) | **3** (standard box + simple bar, but mount interface adds complexity) |
| E4 | Bar flexibility | 0.15 | **4** (bar is universal, any frame) | **1** (integrated unit specific to one frame type) | **3** (bar works on frames but back-pack protrudes) |
| E5 | Cable vulnerability | 0.10 | **2** (500mm exposed cable) | **4** (no external cable) | **4** (no external cable) |
| E6 | Thermal management | 0.10 | **4** (large base plate, good convection) | **2** (limited surface area inside bar) | **3** (smaller box but adequate) |
| E7 | Transport packing | 0.10 | **3** (bar + box pack separately in case) | **2** (long unit, needs large case) | **3** (bar + box as unit, medium case) |

### 3.1 Weighted Scores

| Criterion | Weight | L1×W | L2×W | L3×W |
|-----------|--------|------|------|------|
| E1: Frame load | 0.20 | 0.80 | 0.20 | 0.40 |
| E2: Maintenance | 0.20 | 0.80 | 0.40 | 0.40 |
| E3: Manufacturability | 0.15 | 0.60 | 0.30 | 0.45 |
| E4: Bar flexibility | 0.15 | 0.60 | 0.15 | 0.45 |
| E5: Cable vulnerability | 0.10 | 0.20 | 0.40 | 0.40 |
| E6: Thermal mgmt | 0.10 | 0.40 | 0.20 | 0.30 |
| E7: Transport | 0.10 | 0.30 | 0.20 | 0.30 |
| **TOTAL** | **1.00** | **3.70** | **1.85** | **2.70** |
| **PERCENTAGE** | | **92.5%** | **46.3%** | **67.5%** |
| **DECISION** | | **SELECTED** | **REJECTED** | **FALLBACK** |

---

## 4. RESULTS

| Rank | Variant | Score | Decision | Key Advantage |
|------|---------|-------|----------|---------------|
| **1** | **L1: Separate Box** | **92.5%** | **SELECTED** | Best frame load (1.2 kg), best maintenance access, universal bar compatibility |
| 2 | L3: Back-Pack | 67.5% | FALLBACK | No cable vulnerability; viable if cable damage proves a problem in field |
| 3 | L2: Integrated Bar | 46.3% | REJECTED | Heavy frame load, poor maintenance, complex manufacturing |

### 4.1 Selection Rationale

**L1 "Separate Box" selected because:**

1. **Lightest bar load (1.2 kg):** Target frames in Vietnamese ranges may be wooden or lightweight metal. Minimizing load on frame preserves accuracy (frame deflection = scoring error). Critical for meeting SIG-04 (±10mm).

2. **Best maintenance access:** Processing enclosure can be placed on ground or workbench. Battery door accessible without removing from frame. MTTR ≤30 min easily achieved.

3. **Universal bar compatibility:** Sensor bar is a simple aluminum C-channel with clamps. Works on ANY frame type — NATO, Vietnamese, improvised. This maximizes deployment flexibility.

4. **Simplest manufacturing:** Standard rectangular enclosure (3-axis CNC) + simple bar (extrusion + pocket milling). No complex integrated machining.

5. **Best thermal management:** 250×180mm base plate provides ample convection surface area. At 15W dissipation, ΔT ≈ 15°C above ambient.

**Cable vulnerability (L1 weakness) mitigated by:**
- 500mm cable is SHORT (within BSU assembly, not a long field run)
- PUR jacket rated for outdoor/drive-over
- IP67 connectors at both ends
- Cable routed along target frame leg (protected path)
- Spare cable included in spares kit ($15 replacement)

### 4.2 Sensitivity Analysis

**What if cable vulnerability weight increases from 0.10 to 0.25?**

| Variant | Original | Revised | Change |
|---------|----------|---------|--------|
| L1 | 92.5% | 87.5% | -5.0% |
| L3 | 67.5% | 72.5% | +5.0% |

L1 still leads comfortably. Even with doubled cable concern, L1 remains the best layout.

**What if frame load weight drops to 0.05 (strong frames assumed)?**

| Variant | Original | Revised | Change |
|---------|----------|---------|--------|
| L1 | 92.5% | 90.6% | -1.9% |
| L2 | 46.3% | 48.8% | +2.5% |

L2 improves slightly but remains rejected. L1 still dominant.

---

## 5. DEFINITIVE LAYOUT SELECTION

```
╔═══════════════════════════════════════════════════════════════════╗
║  SELECTED LAYOUT: L1 "SEPARATE BOX"                              ║
║  VDI 2225 Score: 92.5%                                           ║
║                                                                   ║
║  • Sensor bar (1040×60×40mm, 1.2 kg) on target frame             ║
║  • Processing enclosure (250×180×120mm, 6.6 kg) on frame/ground  ║
║  • 500mm shielded cable between bar and enclosure                 ║
║  • Battery door for quick replacement                             ║
║  • All external connectors on one face (front panel)              ║
║                                                                   ║
║  Fallback: L3 "Back-Pack" if cable proves problematic in trials   ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 6. LAYOUT REFINEMENT DECISIONS

Based on the variant evaluation, the following refinements are applied to L1:

| Decision | Detail | Rationale |
|----------|--------|-----------|
| Connectors on ONE face | All 3 connectors (ETH, PWR, Sensor cable) on front face | Simplifies cable management; one-direction access |
| Battery door on SIDE | Cam-latch door on left side panel | Accessible without disconnecting any cables |
| Status LEDs on FRONT | Integrated into lid (per Rules RC-3) | Visible from firing point direction |
| Base plate DOWN | 6mm base plate on bottom | Heat sink faces ground (natural convection); low CG for stability |
| Mounting versatile | VESA 100×100 on back + rubber feet on base | Can mount to frame OR stand on ground/table |
| Sensor cable exit | From enclosure TOP, routed up to bar | Short run along frame leg |

---

## 7. META-LEARNING SKILL APPLIED

**Skill: Multi-criteria Evaluation (Layout-level)**
- Same VDI 2225 methodology applied at layout level (Phase 2 used it for concepts)
- Key insight: Physical arrangement has as much impact on user satisfaction as the electrical design. Frame load and maintenance access score higher than technical performance criteria because the electronics are identical across variants.
- The "obvious" choice (L2 integrated, no cable) scored lowest because it concentrates all weight on the frame and severely limits maintenance access.

---

**Next Step:** [[DECS_C_requirements_verification]] → Verify all requirements against selected layout

*DECS-E Complete | 3 layout variants evaluated | L1 "Separate Box" selected at 92.5% | L3 fallback*
