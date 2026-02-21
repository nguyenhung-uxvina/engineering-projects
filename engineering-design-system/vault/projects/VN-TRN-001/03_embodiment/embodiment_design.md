---
project: VN-TRN-001
phase: 3
type: embodiment-design
version: 2.0
created: 2026-02-06
updated: 2026-02-06
status: gate-review
approach: 15-step-RISM-PRAD-DECS-OCP
---

# EMBODIMENT DESIGN - MASTER DOCUMENT
## VN-TRN-001: Vietnamese LOMAH Electronic Scoring System
### Version: 2.0 | Date: 2026-02-06
### Selected Concept: A "Baseline" (VDI 2225: 83.8%)
### Approach: 15-Step RISM-PRAD-DECS-OCP (Comprehensive)

---

## 1. APPROACH SELECTION

| Criterion | 7-Step Simplified | 15-Step RISM-PRAD-DECS-OCP |
|-----------|-------------------|----------------------------|
| Coverage | ~70% | ~95% |
| Best for | Small/simple projects | Complex defense systems |
| Meta-learning | Minimal | 13 skills integrated |
| Systems Thinking | Optional | Built-in at each step |
| DfX depth | Top 5 summary | Full 12-category review |
| **Selected** | — | **✅ This project** |

**Rationale:** VN-TRN-001 is a defense electronic system with 107 requirements, MIL-STD compliance, Vietnamese local content targets, and multi-stakeholder accountability. The comprehensive approach is warranted.

---

## 2. PROCESS OVERVIEW

```
RISM (Requirements & Material Foundation)        Steps 1-4
══════════════════════════════════════════
  R: Requirements Identification ─────────────── Step 1  ✅
  I: Identify Critical Requirements ─────────── Step 2  ✅
  S: Select Preliminary Materials ───────────── Step 3  ✅
  M: Material Analysis ──────────────────────── Step 4  ✅
          │
          ▼
PRAD (Principles & Rules Application)           Steps 5-8
══════════════════════════════════════════
  P: Principles Application ─────────────────── Step 5  ✅
  R: Rules Application ──────────────────────── Step 6  ✅
  A: Architecture Definition ────────────────── Step 7  ✅
  D: Design Structure ───────────────────────── Step 8  ✅
          │
          ▼
DECS (Detail & Evaluation)                      Steps 9-12
══════════════════════════════════════════
  D: Detail Specification ───────────────────── Step 9  ✅
  E: Evaluate Layout Variants ───────────────── Step 10 ✅
  C: Check Against Requirements ─────────────── Step 11 ✅
  S: Standards Compliance ───────────────────── Step 12 ✅
          │
          ▼
OCP (Optimization & Production)                 Steps 13-15
══════════════════════════════════════════
  O: Optimize Design ────────────────────────── Step 13 ✅
  C: Cost Analysis ──────────────────────────── Step 14 ✅
  P: Production Planning ────────────────────── Step 15 ✅
```

---

## 3. DOCUMENT MAP

### RISM: Requirements & Material Foundation

| Step | File | Key Output |
|------|------|------------|
| R | [[RISM_R_requirements]] | 81 embodiment requirements extracted from 107 total, organized in 11 categories |
| I | [[RISM_I_critical_requirements]] | 15 hard + 10 soft constraints; 8 conflicts resolved; 5 design drivers |
| S | [[RISM_S_preliminary_materials]] | Material candidate screening per component (3-5 candidates each) |
| M | [[RISM_M_material_analysis]] | 10 materials selected with weighted scoring; Vietnamese supplier mapping |

### PRAD: Principles & Rules Application

| Step | File | Key Output |
|------|------|------------|
| P | [[PRAD_P_principles]] | 8 Pahl & Beitz principles × 5 subsystems; 10 key design decisions |
| R | [[PRAD_R_rules]] | 4 Rules compliance: 98% overall; 3 simplification changes adopted |
| A | [[PRAD_A_architecture]] | 5 modules, 7 interfaces (ICD), information flow diagram |
| D | [[PRAD_D_structure]] | Structural analysis, load cases, thermal budget, definitive layout |

### DECS: Detail & Evaluation

| Step | File | Key Output |
|------|------|------------|
| D | [[DECS_D_detail_specification]] | All dimensions with tolerances; component specs; 2 tolerance stack-ups |
| E | [[DECS_E_evaluate_variants]] | 3 layout variants; L1 "Separate Box" selected at 92.5% |
| C | [[DECS_C_requirements_verification]] | 107/107 requirements traced to design features; gap analysis |
| S | [[DECS_S_standards_compliance]] | MIL-STD-810H/461G/882E detailed compliance; test plan |

### OCP: Optimization & Production

| Step | File | Key Output |
|------|------|------------|
| O | [[OCP_O_optimization]] | 18 optimizations; cost $377→$354; runtime 11.4→18.5h; Tj 89.7→74.8°C |
| C | [[OCP_C_cost_analysis]] | Detailed BOM; $354/lane; 64.6% local content; 10-lane range $18,540 |
| P | [[OCP_P_production_planning]] | 6-phase production flow; supplier list; QC plan; assembly sequence |

---

## 4. DESIGN SUMMARY (Post-Optimization)

### 4.1 BSU-V1 Key Specifications

| Parameter | Value | Requirement | Margin |
|-----------|-------|-------------|--------|
| **System weight** | 7.75 kg | ≤12 kg (MUST) | 35% |
| **Sensor bar** | 1040 × 60 × 40 mm | ≤1,300 mm (MUST) | 20% |
| **Processing enclosure** | 250 × 180 × 120 mm | ≤300×200×150 (WISH) | Within |
| **Scoring accuracy** | ±10 mm (design) | ±10 mm (MUST) | At target |
| **Calibration** | Zero calibration shots | Cal-free (MUST) | ✅ |
| **Battery runtime** | 18.5 h (realistic) | ≥10 h (MUST) | 85% |
| **Boot time** | ~10 s | ≤60 s (MUST) | 83% |
| **IP rating** | IP67 | IP67 (MUST) | At target |
| **Operating temp** | -10°C to +60°C | -10 to +60°C (MUST) | At target |
| **FPGA junction temp** | 74.8°C at 60°C amb | <100°C (component) | 25°C |
| **Unit cost** | $354/lane | ≤$500 (MUST) | 29% |
| **Local content** | 64.6% by cost | ≥60% (MUST) | 4.6% |
| **Setup time** | ~10 min (3 steps) | ≤15 min (MUST) | 33% |
| **MTTR** | ≤30 min (LRU swap) | ≤30 min (MUST) | At target |

### 4.2 Architecture Overview

```
BSU-V1 SYSTEM (Per Lane)
│
├── MODULE 1: Sensor Bar Assembly (1.2 kg)
│   ├── Al 6063-T5 C-channel extrusion (1040mm)
│   ├── 4× TDK ICS-40730 MEMS mics (non-coplanar: M1,M3 z=0; M2,M4 z=40mm)
│   ├── 4× Daughter PCBs (OPA1612 preamp + AD8338 AGC + Butterworth BPF)
│   ├── 4× Vietnamese natural rubber acoustic boots
│   └── 2× Cam-lever quick-mount clamps
│
├── MODULE 2: Main Processing (on Main PCB, 160×100mm 4-layer)
│   ├── Lattice iCE40UP5K FPGA (timing capture, 100MHz via PLL)
│   ├── TI ADS8684 ADC (4ch, 500kSPS, 16-bit)
│   ├── ST STM32H743 MCU (cal-free TDOA algorithm, BIT, Ethernet)
│   ├── Microchip LAN8720A Ethernet PHY + HanRun magnetics
│   ├── Winbond W25Q64 SPI Flash (8MB, dual firmware image)
│   ├── TI TMP117 temp sensor + ST LIS2DH12 accelerometer
│   └── Conformal coat: HumiSeal 1B31, IPC-CC-830C Class 3
│
├── MODULE 3: Power (on Power PCB, 80×60mm 2-layer)
│   ├── Samsung INR18650-35E 4S1P (14.8V, 10Ah, 148Wh)
│   ├── TI BQ76940 BMS + BQ27441 fuel gauge
│   ├── TI BQ25700A charger (12-28V input)
│   ├── TI TPS54331 (5V, 3A) + TPS62160 (3.3V, 1A ultra-low-noise)
│   └── Input protection: SMAJ58A TVS + SI2301CDS reverse polarity
│
├── MODULE 4: Enclosure (Al 6061-T6, IP67)
│   ├── Body: 250×180×120mm, 4mm walls, 6mm base plate (heat sink)
│   ├── Lid: 6× M4 SS316 bolts, EPDM O-ring (captive)
│   ├── Battery door: cam-latch, quick-release
│   ├── Hard anodize Type III (25μm) + RAL 6031 paint
│   └── 3× IP67 cable glands (ETH, PWR, Sensor)
│
└── MODULE 5: Cables
    ├── 500mm shielded sensor cable (bar↔enclosure, 7-pin circular IP67)
    ├── CAT6 ruggedized Ethernet (50m standard, PUR jacket)
    └── 12V DC power cable (optional, for extended operation)
```

### 4.3 DfX Compliance Summary

| DfX Category | Weight | Score | Status |
|-------------|--------|-------|--------|
| DfX#3: Corrosion Resistance | 0.25 | 100% | ✅ PASS |
| DfX#7: Production | 0.20 | 100% | ✅ PASS |
| DfX#9: Maintenance | 0.20 | 88% | ✅ PASS (manual pending Phase 4) |
| DfX#1: Durability | 0.20 | 100% | ✅ PASS |
| DfX#8: Assembly | 0.15 | 100% | ✅ PASS |
| **Weighted Average** | **1.00** | **97.4%** | **✅ PASS** |

### 4.4 Key Design Decisions

| Decision | Rationale | Reference |
|----------|-----------|-----------|
| Non-coplanar 4-mic array (40mm offset) | Calibration-free TDOA per expired Saab patent | [[PRAD_P_principles]] |
| FPGA + MCU hybrid (not MCU-only) | FPGA guarantees <2ns timing jitter for ±10mm accuracy | [[RISM_I_critical_requirements]] |
| Separate box layout (not integrated bar) | Lightest bar load (1.2 kg); best maintenance access | [[DECS_E_evaluate_variants]] |
| ADS8684 (4ch) instead of ADS8688 (8ch) | Only 4 channels needed; saves $5/unit | [[OCP_O_optimization]] |
| Al 6061-T6 enclosure (not polymer) | IP67 + EMC shielding + ballistic protection + heat sink | [[RISM_M_material_analysis]] |
| EPDM gaskets (not silicone) | Better ozone/UV resistance; Vietnamese rubber supply | [[RISM_S_preliminary_materials]] |
| Acrylic conformal (not silicone/polyurethane) | Easiest rework; good humidity protection | [[PRAD_R_rules]] |

---

## 5. META-LEARNING SKILLS APPLIED

| Step | Skill | Example |
|------|-------|---------|
| R | Categorization | 107 requirements → 11 physical constraint categories |
| I | Prioritization + Constraint ID | 15 hard + 10 soft; 8 conflicts; 5 design drivers |
| S | Filtering + Satisficing | 3-5 candidates per component, screened by hard constraints |
| M | Multi-criteria Decision | Weighted scoring matrix for materials |
| P | Principle → Application | 8 principles × 5 subsystems → 10 key decisions |
| R | Checklist Verification | 4 rules → 98% compliance; 3 changes adopted |
| A | Abstraction + Decomposition | 7 functions → 5 physical modules + 7 interfaces |
| D | Analysis → Synthesis | Load cases + thermal → definitive layout |
| D | Precision Specification | Tolerances as loose as function allows; 2 stack-ups |
| E | Multi-criteria Evaluation | 3 layout variants → L1 selected at 92.5% |
| C | Traceability + Verification | 107/107 requirements traced |
| S | Regulatory Mapping | MIL-STD-810H/461G/882E per-method compliance |
| O | Optimization Heuristics | 18 optimizations; free improvements first |
| C | Cost Modeling | Detailed BOM; scaling analysis; 10-year TCO |
| P | Process Planning | 6-phase flow; 15 suppliers; 20-step assembly |

---

## 6. SYSTEMS THINKING INTEGRATION

### 6.1 Reinforcing Loops (Virtuous Cycles)

| Loop | Description | Design Feature |
|------|-------------|----------------|
| R1 | Capability → demand → scale → lower cost → more demand | Cost-optimized BOM ($354); scalable architecture |
| R2 | Local production → expertise → quality → more local → less import | 64.6% local content; 15+ Vietnamese suppliers |
| R3 | Modular LRU → fast repair → availability → satisfaction → deployment | 5 independent modules; MTTR ≤30 min |

### 6.2 Leverage Points Applied

| Level | Intervention | Implementation |
|-------|-------------|----------------|
| L4 | Self-organization | 5 independently testable modules |
| L5 | Rules | "Never require calibration" — fundamental design rule |
| L6 | Information flows | BIT chain + shot counters + OTA updates |
| L8 | Negative feedback | Dual watchdog (FPGA + MCU); BMS 4-level protection |
| L9 | Reduce delays | 10s boot; quick-mount clamps; fast setup |

---

## 7. GATE 3 CHECKLIST (Phase 3 → Phase 4)

| # | Criterion | Target | Actual | Status |
|---|-----------|--------|--------|--------|
| 1 | Layout complete with dimensions | Yes | Definitive layout L1, fully dimensioned | ✅ PASS |
| 2 | All materials selected + justified | Yes | 10 materials, weighted scoring matrices | ✅ PASS |
| 3 | Top 5 DfX addressed | ≥80% each | 97.4% weighted average | ✅ PASS |
| 4 | Standards compliance verified | Analysis + test plan | MIL-STD-810H/461G/882E mapped per-method | ✅ PASS |
| 5 | Requirements verification | ≥80% | 107/107 traced (100%) | ✅ PASS |
| 6 | Cost within target | ≤$500/lane | $354/lane (70.8%) | ✅ PASS |
| 7 | Local content ≥60% | 60% | 64.6% | ✅ PASS |
| 8 | Critical interfaces defined | Yes | 7 interfaces (ICD) + 3 connector pinouts | ✅ PASS |
| 9 | Risks identified + mitigated | Yes | 8 conflicts + 4 hazards, all mitigated | ✅ PASS |
| 10 | Manufacturing plan defined | Yes | 6-phase flow, 15+ suppliers, assembly sequence | ✅ PASS |
| 11 | Systems analysis | Loops + leverage | 3 R-loops, 5 leverage points (L4-L9) | ✅ PASS |

**Result: 11/11 criteria PASSED**

---

## 8. PHASE 4 PREVIEW

Phase 4 (Detail Design) will produce production-ready documentation:

| Deliverable | Description |
|-------------|-------------|
| PCB schematics | Full circuit design (sensor, main, power boards) |
| PCB layout | Gerber files ready for fabrication |
| FPGA RTL | Verilog/VHDL for iCE40UP5K timing capture pipeline |
| Firmware | STM32H743 embedded software (FreeRTOS) |
| Mechanical drawings | CNC machining drawings (enclosure + sensor bar) |
| Complete BOM | Every component with exact P/N, supplier, lead time |
| Test procedures | Factory acceptance test, field verification |
| Web application | VN-LOMAH HTML5 scoring display + range management |
| User manual | Vietnamese-language O&M manual with troubleshooting |
| Prototype build | First 2 functional prototypes for DV testing |

---

*Embodiment Design v2.0 | VN-TRN-001 | 15-Step RISM-PRAD-DECS-OCP | $354/lane | 64.6% local | 15 files*
