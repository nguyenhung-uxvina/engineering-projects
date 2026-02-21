---
project: VN-TRN-001
type: status-tracker
version: 1.3
created: 2026-02-06
updated: 2026-02-07
---

# VN-TRN-001 - Project Status

## Quick Status
```
Phase 4/4 | Detail Design | Status: ACTIVE
Progress: ████████████████░░░░ 80%
Next Gate: Phase 4→Production (Detail → Build)
```

## Phase Tracker

| Phase | Status | Start | End | Gate |
|-------|--------|-------|-----|------|
| Phase 0: ODI | COMPLETE | 2026-02-06 | 2026-02-06 | APPROVED |
| Phase 1: Requirements | COMPLETE | 2026-02-06 | 2026-02-06 | APPROVED |
| Phase 2: Conceptual | COMPLETE | 2026-02-06 | 2026-02-06 | APPROVED |
| Phase 3: Embodiment | COMPLETE | 2026-02-06 | 2026-02-06 | APPROVED |
| **Phase 4: Detail** | **ACTIVE** | 2026-02-06 | — | PENDING |

## Phase 0 Deliverables (Complete)

- [x] Reverse engineering analyses (8 competitors)
- [x] Project brief (00_project_brief.md)
- [x] ODI analysis (00_odi_analysis.md)
- [x] 52 outcome statements, opportunity scores
- [x] Growth strategy: Differentiated
- [x] Gate 0→1: APPROVED

## Phase 1 Deliverables (Complete)

- [x] Requirements list: 107 requirements across 16 categories
- [x] 68 MUST (D) + 39 WISH (W) requirements
- [x] 85% quantified (target: ≥80%)
- [x] Standards compliance matrix
- [x] ODI traceability
- [x] Conflict analysis (5 conflicts, all resolved)
- [x] Gate 1→2: APPROVED

## Phase 2 Deliverables (Complete)

- [x] 5-step abstraction: solution-neutral problem statement
- [x] Function structure: 7 functions (F1-F7) covering all requirements
- [x] Morphological matrix: 7 functions × 4 principles each
- [x] 4 concepts generated (A: Baseline, B: Portable, C: Multi-Mode, D: Ultra-Low)
- [x] VDI 2225 evaluation: 10 criteria, 4 concepts scored
- [x] **Selected: Concept A "Baseline" at 83.8%**
- [x] Fallback: Concept B "Portable" at 78.0%
- [x] Preliminary BOM: $368/lane, ~63% local content
- [x] Risk analysis: 4 risks with mitigations
- [x] Gate 2→3: APPROVED

## Phase 3 Deliverables (15-Step RISM-PRAD-DECS-OCP)

### Approach: Comprehensive (15 steps, 16 files)

- [x] **RISM** (Requirements & Material Foundation)
  - [x] Step 1: Requirements Identification — 81 embodiment requirements from 107 total
  - [x] Step 2: Critical Requirements — 15 hard + 10 soft constraints; 8 conflicts resolved
  - [x] Step 3: Preliminary Materials — 3-5 candidates per component screened
  - [x] Step 4: Material Analysis — 10 materials selected with weighted scoring
- [x] **PRAD** (Principles & Rules Application)
  - [x] Step 5: Principles Application — 8 principles × 5 subsystems; 10 key decisions
  - [x] Step 6: Rules Application — 4 rules, 98% compliance; 3 changes adopted
  - [x] Step 7: Architecture Definition — 5 modules, 7 interfaces (ICD)
  - [x] Step 8: Design Structure — Load cases, thermal budget, definitive layout
- [x] **DECS** (Detail & Evaluation)
  - [x] Step 9: Detail Specification — All dimensions with tolerances; 2 stack-ups
  - [x] Step 10: Evaluate Variants — 3 layouts; L1 "Separate Box" selected at 92.5%
  - [x] Step 11: Requirements Verification — 107/107 traced to design features
  - [x] Step 12: Standards Compliance — MIL-STD-810H/461G/882E detailed compliance
- [x] **OCP** (Optimization & Production)
  - [x] Step 13: Optimize Design — 18 optimizations; cost $377→$354; Tj 89.7→74.8°C
  - [x] Step 14: Cost Analysis — Detailed BOM; $354/lane; 64.6% local content
  - [x] Step 15: Production Planning — 6-phase flow; 19 suppliers; 20-step assembly

### Key Metrics (Post-Optimization)
- Unit cost: **$354/lane** (70.8% of $500 budget) — optimized from $377
- Local content: **64.6%** by cost (target ≥60%)
- Battery runtime: **18.5 hours** (MUST ≥10h, 85% margin)
- FPGA Tj: **74.8°C** at 60°C ambient (25.2°C margin)
- System weight: **7.75 kg** (MUST ≤12 kg, 35% margin)
- DfX weighted average: **97.4%**
- Gate 3 checklist: **11/11 PASSED**
- [x] Gate 3→4 review: **APPROVED** (2026-02-07)

## Phase 4 Deliverables (Detail Design — In Progress)

### Prototype Build
- [x] Prototype build plan (`04_detail/prototype_build_plan.md`) — 2 DV units, 20-week schedule, $16,524 budget
- [x] Procurement BOM (`04_detail/procurement_bom.md`) — 52+ line items, $1,674 material + $9,600 NRE
- [ ] PCB schematic (main board) — D-01
- [ ] PCB schematic (power board) — D-03
- [ ] PCB schematic (daughter board) — D-05
- [ ] PCB layout (main board) — D-02
- [ ] PCB layout (power board) — D-04
- [ ] PCB layout (daughter board) — D-06
- [ ] Mechanical drawings (enclosure) — D-09
- [ ] Mechanical drawings (sensor bar) — D-10
- [ ] FPGA RTL (iCE40UP5K) — D-07
- [ ] MCU firmware (STM32H743) — D-08
- [ ] Wiring harness drawing — D-11
- [ ] Assembly work instructions — D-12

### Gap Resolutions (from DECS-C)
- [x] SIG-05: ADC simultaneous sampling → 4× LF398 S&H solution selected (+$4/unit)
- [x] GEO-06: Enclosure weight → Requirement revision proposed (≤7kg with battery)
- [x] SIG-02: WiFi → System-level Ethernet-to-WiFi bridge; ESP32 footprint reserved
- [x] MNT-04: Domestic spares → In-country buffer inventory strategy
- [x] ENG-06: Solar >24V → Buck pre-regulator (TPS54331) added to power board
- [x] TRN-04: Air transport → 4S1P pack at 50.4Wh confirmed under 100Wh IATA limit

### Key Phase 4 Metrics
- Prototype budget: **$16,524** (2 DV units + NRE + test equipment)
- Schedule: **20 weeks** from design freeze to DV test report
- Success criteria: **10 criteria** (6 MUST + 4 TARGET)
- Risk register: **10 risks** managed (3 HIGH, 4 MEDIUM, 3 LOW)

## Key Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-06 | Project initiated as VN-TRN-001 | Formalize LOMAH development after 8 RE analyses |
| 2026-02-06 | Calibration-free acoustic TDOA as core technology | Expired Saab patent, proven technology, lowest risk |
| 2026-02-06 | Phase 0 ODI: APPROVED | 52 outcomes, 4 EXTREME opportunities identified |
| 2026-02-06 | 107 requirements in 16 categories | 85% quantified, all conflicts resolvable |
| 2026-02-06 | Phase 1: APPROVED | All gate criteria met |
| 2026-02-06 | Selected Concept A "Baseline" (83.8%) | Best accuracy + cal-free + low risk; Concept B fallback |
| 2026-02-06 | Phase 2: APPROVED | All gate criteria met, proceed to embodiment |
| 2026-02-06 | BSU-V1 layout finalized | Non-coplanar TDOA, FPGA+MCU hybrid, IP67 Al enclosure |
| 2026-02-06 | Local content 66.2%, cost $377/lane | Both within targets (≥60%, ≤$500) |
| 2026-02-06 | Upgraded to 15-step RISM-PRAD-DECS-OCP | User requested comprehensive approach with per-step files |
| 2026-02-06 | 18 optimizations applied | Cost $377→$354; runtime 11.4→18.5h; Tj 89.7→74.8°C |
| 2026-02-06 | ADC changed ADS8688→ADS8684 | Only 4 channels needed; saves $5/unit |
| 2026-02-06 | Non-coplanar offset 30→40mm | Better 3D resolution; free change |
| 2026-02-06 | **Phase 3: APPROVED** | 11/11 gate criteria PASSED; proceed to Phase 4 |
| 2026-02-07 | Phase 4 started: Prototype Build | First deliverable: build plan + procurement BOM |
| 2026-02-07 | ADC gap resolved: 4× LF398 S&H | Simultaneous sampling via external S&H before ADS8684; +$4/unit |
| 2026-02-07 | 6 DECS-C gaps resolved | All gaps have resolution plans with owners and deadlines |

## Files

| File | Location | Status |
|------|----------|--------|
| Project brief | `00_project_brief.md` | Complete |
| ODI analysis | `00_odi_analysis.md` | Complete |
| Requirements list | `01_requirements/requirements_list.md` | Complete v1.0 |
| Conceptual design | `02_conceptual/conceptual_design.md` | Complete v1.0 |
| **Embodiment master** | `03_embodiment/embodiment_design.md` | **v2.0 - Gate review** |
| RISM Step 1 | `03_embodiment/RISM_R_requirements.md` | Complete |
| RISM Step 2 | `03_embodiment/RISM_I_critical_requirements.md` | Complete |
| RISM Step 3 | `03_embodiment/RISM_S_preliminary_materials.md` | Complete |
| RISM Step 4 | `03_embodiment/RISM_M_material_analysis.md` | Complete |
| PRAD Step 5 | `03_embodiment/PRAD_P_principles.md` | Complete |
| PRAD Step 6 | `03_embodiment/PRAD_R_rules.md` | Complete |
| PRAD Step 7 | `03_embodiment/PRAD_A_architecture.md` | Complete |
| PRAD Step 8 | `03_embodiment/PRAD_D_structure.md` | Complete |
| DECS Step 9 | `03_embodiment/DECS_D_detail_specification.md` | Complete |
| DECS Step 10 | `03_embodiment/DECS_E_evaluate_variants.md` | Complete |
| DECS Step 11 | `03_embodiment/DECS_C_requirements_verification.md` | Complete |
| DECS Step 12 | `03_embodiment/DECS_S_standards_compliance.md` | Complete |
| OCP Step 13 | `03_embodiment/OCP_O_optimization.md` | Complete |
| OCP Step 14 | `03_embodiment/OCP_C_cost_analysis.md` | Complete |
| OCP Step 15 | `03_embodiment/OCP_P_production_planning.md` | Complete |
| **Prototype build plan** | `04_detail/prototype_build_plan.md` | **Complete v1.0** |
| **Procurement BOM** | `04_detail/procurement_bom.md` | **Complete v1.0** |

---

*Last updated: 2026-02-07*
