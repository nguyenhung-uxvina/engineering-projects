---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: RISM-I
title: Identify Critical Requirements
version: 1.0
created: 2026-02-06
status: complete
---

# STEP I: IDENTIFY CRITICAL REQUIREMENTS
## Prioritization, Conflicts & ODI Mapping
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 2 of 15

**Purpose:** Prioritize the 81 embodiment requirements by constraint strength, map to ODI opportunities, and identify embodiment-specific conflicts.

**Input:** [[RISM_R_requirements]] (81 embodiment requirements)
**Output:** Prioritized Requirements List with conflicts and resolution strategies

---

## 1. CONSTRAINT CLASSIFICATION

### 1.1 Hard Constraints (MUST - Cannot Violate)

These requirements are **non-negotiable**. Failure to meet any one is a showstopper.

| Rank | Req ID | Requirement | Value | Why Hard |
|------|--------|-------------|-------|----------|
| H1 | OPR-08 | Calibration-free | Zero cal shots | Core differentiator; ODI O-16 (Opp 15.0) |
| H2 | SIG-04 | Scoring accuracy | ±10mm at 300m | Primary function; MUST per VDI 2225 |
| H3 | OPR-07 | IP rating | IP67 | Tropical environment survival; non-negotiable |
| H4 | SAF-02 | No projectile deflection | Absolute | Range safety critical |
| H5 | SAF-04 | Battery safety | UN 38.3 + BMS | Liability; regulatory |
| H6 | FRC-01 | Shockwave tolerance | ≥164 dB SPL | Operational survival |
| H7 | ENG-03 | Battery runtime | ≥10 hours | Full training day; primary use case |
| H8 | PRD-01 | Local content | ≥60% by value | National policy requirement |
| H9 | CST-01 | Unit cost | ≤$500/lane | Budget constraint; business viability |
| H10 | GEO-04 | BSU weight | ≤12kg | Physical handling limit |
| H11 | FRC-03 | Shock (40g) | MIL-STD-810H 516.8 | Military transport survival |
| H12 | FRC-04 | Vibration | MIL-STD-810H 514.8 Cat 4 | Military transport survival |
| H13 | SAF-05 | EMC emissions | MIL-STD-461G | Range radio compatibility |
| H14 | OPR-01 | Operating temp | -10°C to +60°C | Vietnamese climate range |
| H15 | ASM-01 | Field assembly | ≤15 min/lane | Operational readiness |

### 1.2 Soft Constraints (WISH - Optimization Targets)

These improve the design but can be traded off against each other.

| Priority | Req ID | Requirement | Target | ODI Score |
|----------|--------|-------------|--------|-----------|
| S1 | GEO-04 | BSU weight | Target 8kg (MUST ≤12kg) | O-15 |
| S2 | KIN-05 | Shot-to-display latency | Target 200ms (MUST ≤500ms) | O-22 |
| S3 | SIG-04 | Scoring accuracy | Target ±5mm (MUST ±10mm) | O-21 |
| S4 | ENG-07 | Boot time | Target 30s (MUST ≤60s) | O-10 |
| S5 | QUA-06 | Design life | Target 20 years (MUST ≥15y) | O-47 |
| S6 | PRD-01 | Local content | Target 70% (MUST ≥60%) | O-52 |
| S7 | CST-01 | Unit cost | Target $377 (MUST ≤$500) | O-47 |
| S8 | ERG-04 | Tool-less setup | Target: zero tools | O-40 |
| S9 | ENG-06 | Solar charging | 18-36V input compatible | O-52 |
| S10 | GEO-08 | Armor detection zone | 4.0m × 3.0m | O-08 |

---

## 2. ODI OPPORTUNITY MAPPING

### 2.1 Top ODI Outcomes → Embodiment Impact

| ODI Outcome | Opp Score | Critical Embodiment Requirements | Design Impact |
|-------------|-----------|----------------------------------|---------------|
| **O-52: Foreign independence** | 16.5 | PRD-01, PRD-03, PRD-04, MNT-04 | Material sourcing strategy; Vietnamese machining; local PCB house |
| **O-49: Domestic spares** | 16.0 | PRD-04, MNT-04, MNT-07, MAT-04 | Daughter PCB mic mount; EPDM local rubber; standard fasteners |
| **O-16: Calibration-free** | 15.0 | OPR-08, SIG-04, SIG-05, SIG-07 | Non-coplanar sensor geometry; FPGA timing; expired patent algo |
| **O-28: Subsonic scoring** | 15.0 | (Phase 2 scope) | Architecture must accommodate future radar module |
| **O-47: 10-year TCO** | 14.5 | CST-01, CST-03, QUA-01, QUA-06 | Component derating; modular LRU; domestic spares |
| **O-21: Shot accuracy** | 14.0 | SIG-04, SIG-05, QUA-03 | ADC resolution; FPGA timing; sensor spacing |
| **O-51: Tropical resistance** | 14.0 | OPR-01 to OPR-07, MAT-01-05 | IP67; hard anodize; EPDM; conformal coat |
| **O-26: Wind/rain** | 13.0 | OPR-04, FRC-05, OPR-07 | IP67; aerodynamic profile; wind-resistant clamps |
| **O-10: Setup time** | 12.5 | ASM-01, ASM-03, ENG-07 | Cam-lever clamps; quick-connect; fast boot |

### 2.2 ODI-Weighted Embodiment Priority

Ranking embodiment decisions by cumulative ODI opportunity impact:

| Rank | Design Decision | ODI Outcomes Served | Cumulative Opp |
|------|----------------|---------------------|----------------|
| 1 | **Sensor geometry (non-coplanar)** | O-16, O-21, O-27, O-33 | 55.0 |
| 2 | **Material sourcing (local)** | O-52, O-49, O-47 | 47.0 |
| 3 | **Environmental protection (IP67)** | O-51, O-26, O-27 | 40.0 |
| 4 | **Quick-mount system** | O-10, O-12, O-40 | 35.5 |
| 5 | **Battery system (Li-ion, replaceable)** | O-34, O-49, O-52 | 34.5 |
| 6 | **Modular LRU design** | O-37, O-39, O-49 | 33.5 |
| 7 | **FPGA timing resolution** | O-21, O-16, O-33 | 32.0 |
| 8 | **Cost-optimized BOM** | O-47, O-52 | 31.0 |

---

## 3. EMBODIMENT-SPECIFIC CONFLICTS

### 3.1 Conflict Matrix

| # | Conflict | Req A | Req B | Severity | Resolution Strategy |
|---|---------|-------|-------|----------|-------------------|
| EC-1 | **Weight vs. IP67** | GEO-04 (≤12kg) | OPR-07 (IP67) | Medium | Al 6061-T6 (not steel); 4mm wall minimum; weight budget: enclosure 1.8kg, bar 1.2kg, battery 3.5kg, PCBs 1.3kg = 7.8kg ✅ |
| EC-2 | **Cost vs. FPGA accuracy** | CST-01 (≤$500) | SIG-04 (±10mm) | Medium | iCE40UP5K ($8) provides sufficient timing; no expensive Xilinx/Intel needed. FPGA adds $8 over MCU-only but enables ±10mm MUST. |
| EC-3 | **Local content vs. sensor quality** | PRD-01 (≥60%) | SIG-04 (±10mm), FRC-01 (164 dB) | Low | Accept MEMS mics as imported (3.7% of BOM). Maximize local in mechanical (45% of BOM), cables (4.6%), labor (10.7%), software (9.1%). |
| EC-4 | **Battery capacity vs. weight** | ENG-03 (≥10h) | GEO-04 (≤12kg target 8kg) | Low | Samsung INR18650-35E: 3,500mAh × 4S1P = 14.8V × 10Ah = 148Wh. At 13W avg = 11.4h ✅. Pack weight: 3.5kg (45% of 7.8kg). Acceptable. |
| EC-5 | **Setup speed vs. IP67 robustness** | ASM-01 (≤15min) | ASM-02 (mil-spec IP67) | Low | Amphenol RJFTV IP67 RJ45: quick-connect bayonet lock. Mates in <5s while maintaining IP67. No conflict. |
| EC-6 | **EMC shielding vs. acoustic transparency** | SAF-05 (MIL-STD-461G) | F1 (mic must hear shockwave) | Medium | Sensor bar is OUTSIDE the aluminum Faraday cage. Mics have acoustic ports in sensor bar. Shielded cable from bar to enclosure. Enclosure provides EMC shielding for electronics. |
| EC-7 | **Thermal management vs. sealed enclosure** | ENG-05 (15W dissipation) | OPR-07 (IP67, no vents) | Medium | 6mm aluminum base plate acts as heat sink. Thermal pad from FPGA/MCU to standoffs to base plate. At 15W, 60°C ambient, ΔT ≈ 15°C → junction < 85°C (industrial limit). No fan needed. |
| EC-8 | **Conformal coating vs. rework** | MAT-03 (IPC-CC-830C) | MNT-03 (field repair) | Low | Acrylic conformal (HumiSeal 1B31) is easiest to rework — solvent-removable. Field repair at depot level, not organizational. Field LRU swap = PCB replacement, not component-level. |

### 3.2 Conflict Resolution Summary

| Conflict | Resolved? | Method | Trade-off |
|----------|-----------|--------|-----------|
| EC-1: Weight vs IP67 | ✅ Yes | Al 6061-T6 density 2.7g/cm³ vs steel 8.0 | 7.8kg system, well within 12kg MUST |
| EC-2: Cost vs FPGA | ✅ Yes | iCE40UP5K at $8 vs $50+ Artix-7 | Minimal cost impact for accuracy guarantee |
| EC-3: Local vs sensor | ✅ Yes | Accept 3.7% import for MEMS; 66.2% local overall | Local content target met |
| EC-4: Battery vs weight | ✅ Yes | 4S1P Li-ion, 3.5kg for 11.4h | Battery = 45% of weight, acceptable for runtime |
| EC-5: Setup vs IP67 | ✅ Yes | Quick-connect IP67 connectors exist | No trade-off needed |
| EC-6: EMC vs acoustic | ✅ Yes | Spatial separation: mics outside, electronics inside | Shielded cable bridge |
| EC-7: Thermal vs sealed | ✅ Yes | Conduction cooling via aluminum base plate | No fan = no sealing complexity |
| EC-8: Coating vs rework | ✅ Yes | Acrylic conformal = solvent-removable | Field repair = LRU swap, not component-level |

**All 8 embodiment conflicts resolved. No showstoppers.**

---

## 4. DESIGN DRIVERS HIERARCHY

The top 5 design drivers that most constrain the BSU-V1 embodiment:

### 4.1 Driver 1: Calibration-Free Sensor Geometry (O-16, O-21)
**Impact:** Dictates the entire sensor bar layout — non-coplanar arrangement, minimum 4 sensors, specific spacing ratio. This is the single most constraining technical requirement.
- Drives: sensor bar length, mic placement, z-offset, PCB routing
- Constrains: bar cross-section, mounting bracket, cable routing

### 4.2 Driver 2: Tropical Environmental Protection (O-51, O-26)
**Impact:** IP67 throughout, tropical-grade materials, no ventilation openings, sealed connectors.
- Drives: enclosure material (aluminum + anodize), gasket design, connector selection, conformal coating
- Constrains: thermal management approach (conduction only), maintenance access

### 4.3 Driver 3: Vietnamese Production Capability (O-52, O-49)
**Impact:** All manufacturing within Vietnamese machining/PCB capability. No 5-axis CNC, no BGA, no exotic processes.
- Drives: enclosure designed for 3-axis CNC, PCB max 4-layer, SMT 0402 min QFN-48 max
- Constrains: component package selection, machining complexity

### 4.4 Driver 4: Cost Target ≤$500/lane (O-47)
**Impact:** BOM + labor + margin must fit within $500 selling price.
- Drives: component selection (cost-optimized), lot-size economics, standard parts preference
- Constrains: material grade selection, connector quality tier

### 4.5 Driver 5: Field Maintainability (O-37, O-39, O-49)
**Impact:** MTTR ≤30 min, domestic spares ≥80%, individual sensor replacement.
- Drives: modular LRU design, battery access door, daughter PCB mic mounts
- Constrains: internal layout (accessibility vs compactness)

---

## 5. CONSTRAINT INTERACTION MAP

```
                  ┌─────────────────────┐
                  │ CALIBRATION-FREE    │
                  │ SENSOR GEOMETRY     │
                  │ (Driver 1)          │
                  └──────────┬──────────┘
                             │
                    Dictates mic spacing
                    & non-coplanar offset
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                     │
        ▼                    ▼                     ▼
┌───────────────┐  ┌─────────────────┐  ┌──────────────────┐
│ SENSOR BAR    │  │ FPGA TIMING     │  │ ALGORITHM        │
│ DIMENSIONS    │  │ RESOLUTION      │  │ REQUIREMENTS     │
│ (1040mm)      │  │ (≤2ns)          │  │ (time-only TDOA) │
└───────┬───────┘  └────────┬────────┘  └──────────────────┘
        │                   │
        │         Drives ADC speed
        │         & power consumption
        │                   │
        ▼                   ▼
┌───────────────┐  ┌─────────────────┐
│ WEIGHT        │  │ THERMAL         │
│ BUDGET        │  │ MANAGEMENT      │
│ (7.8kg)       │  │ (15W sealed)    │
└───────┬───────┘  └────────┬────────┘
        │                   │
        └─────────┬─────────┘
                  │
        Constrains material
        & enclosure design
                  │
                  ▼
        ┌─────────────────┐
        │ IP67 ALUMINUM   │
        │ ENCLOSURE       │
        │ (Driver 2)      │
        └────────┬────────┘
                 │
        ┌────────┼────────┐
        │        │        │
        ▼        ▼        ▼
 ┌──────────┐ ┌──────┐ ┌──────────┐
 │ LOCAL    │ │ COST │ │ MAINTAIN │
 │ PRODCTN  │ │ ≤$500│ │ MTTR≤30m │
 │ (Dvr 3)  │ │(Dvr 4)│ │ (Dvr 5)  │
 └──────────┘ └──────┘ └──────────┘
```

---

## 6. META-LEARNING SKILL APPLIED

**Skills: Prioritization + Constraint Identification**
- Prioritized 81 requirements into 15 hard + 10 soft constraints
- Identified 8 embodiment-specific conflicts (all resolvable)
- Mapped ODI opportunity scores to physical design decisions
- Created design driver hierarchy (5 drivers govern 80% of decisions)

**Systems Thinking Integration:**
- Conflict EC-7 (thermal vs. sealed) = competing feedback loops: heat generation (R) vs. heat rejection (B)
- Resolution via conduction cooling leverages L12 (parameter: base plate thickness) rather than L4 (adding fan = new subsystem)
- Calibration-free (Driver 1) eliminates a reinforcing loop: "temperature drift → calibration needed → operational delay → user frustration"

---

**Next Step:** [[RISM_S_preliminary_materials]] → Screen materials by hard constraints

*RISM-I Complete | 15 hard + 10 soft constraints | 8 conflicts resolved | 5 design drivers identified*
