---
project: VN-TGT-SEA-001
phase: 1
type: standards_mapping
version: 2.0
created: 2026-02-10
updated: 2026-02-10
status: draft
---

# Standards Compliance Matrix: VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Phase:** 1 — Task Clarification
**Purpose:** Map applicable military and civil standards to requirements, define compliance approach
**Source:** [[requirements_list.md]], [[stakeholder_analysis.md]] (S-10 Regulatory Authority)

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-10 | System | Initial standards mapping (125 requirements) |
| **2.0** | **2026-02-10** | **System** | **Rev B: Removed propane/LPG standards (TCVN 7441, 6153, 7111), removed hazards H-01/H-08, updated mooring loads (1,366 kgf peak), radar-only target** |

---

## 1. Applicable Standards Overview

### 1.1 Standard Categories

| Category | Standards | Applicability | Compliance Level |
|----------|----------|---------------|------------------|
| **Environmental** | MIL-STD-810H | HIGH — marine environment exposure | Tailored (selected methods) |
| **Safety** | MIL-STD-882E | HIGH — mooring, personnel risk | Full (PHA required) |
| **Marine Construction** | ISO 12215, DNV-GL | MEDIUM — reference only (not naval vessel) | Reference |
| **Radar Reflectors** | IALA Recommendation A-126 | LOW — navigation standard, adapted | Reference (augmented RCS target) |
| **AM Components** | ASTM F3301, ISO/ASTM 52910 | MEDIUM — AlSi10Mg qualification | Adapted (no structural load path) |
| **Materials** | ASTM B209 (aluminum), ASTM D1248 (HDPE) | HIGH — material certification | Full (incoming inspection) |
| **Corrosion** | MIL-STD-1568, ASTM B580 (anodize) | HIGH — 72h marine exposure | Tailored |
| **Vietnamese National** | TCVN (marine, safety) | HIGH — regulatory requirement | Full (TBD-002 mapping) |

### 1.2 Compliance Approach Legend

| Code | Meaning | Description |
|------|---------|-------------|
| **FC** | Full Compliance | Meet all requirements of cited section |
| **TC** | Tailored Compliance | Meet intent with documented tailoring rationale |
| **REF** | Reference Only | Used as design guidance, not mandatory compliance |
| **TBD** | To Be Determined | Awaiting regulatory clarification |
| **N/A** | Not Applicable | Standard does not apply to this product type |

---

## 2. MIL-STD-810H — Environmental Engineering Considerations

### 2.1 Method Selection Rationale

VN-TGT-SEA-001 is an **expendable, passive, anchored platform** operating in a **tropical maritime environment** for up to 72 hours per deployment. Radar-only signature (no IR/propane subsystem). The following methods apply:

| Method | Title | Applicability | Compliance | Requirements | Rationale |
|--------|-------|---------------|------------|--------------|-----------|
| **501.7** | High Temperature | FC | OPR-007 | Air temperature to +55°C | Vietnamese maritime peak |
| **502.7** | Low Temperature | TC | OPR-007 | Air temperature to -5°C (not -40°C) | Vietnamese maritime minimum; no arctic exposure |
| **507.6** | Humidity | TC | OPR-009 | 95% RH, 35°C, 72h continuous | Tropical maritime humidity exposure |
| **509.7** | Salt Fog | FC | OPR-009 | 72h continuous salt spray, 35°C, 5% NaCl | Simulates 72h anchored at sea |
| **510.7** | Sand and Dust | N/A | — | — | Maritime environment, no sand/dust exposure |
| **512.6** | Immersion | FC | OPR-002 | Hull: continuous immersion; deck equipment: intermittent wave wash | Green water in SS 5-6 |
| **514.8** | Vibration | TC | FOR-010 | Low-frequency wave cycling: 0.1-1 Hz, ±7°, 37,000 cycles | Wave-induced platform motion, not mechanical vibration |
| **516.8** | Shock | TC | FOR-005 | Peak mooring load **1,512 kgf** | Mooring snatch load, not pyrotechnic shock |
| **519.8** | Gunfire Shock | N/A | — | — | Expendable target; no post-impact requirements |
| **520.5** | Temperature-Humidity-Vibration-Altitude | N/A | — | — | Not a transportable electronic system |
| **521.4** | Icing/Freezing Rain | N/A | — | — | Tropical maritime operation only |

### 2.2 Test Tailoring Details

#### Method 509.7 — Salt Fog (PRIMARY environmental test)

| Parameter | Standard | Tailored | Rationale |
|-----------|----------|----------|-----------|
| Duration | 48h (standard) | **72h** (extended) | 72h deployment requirement |
| Temperature | 35°C ±2°C | 35°C ±2°C | No change |
| NaCl concentration | 5% ±1% | 5% ±1% | No change |
| Sample condition | Powered, operating | **Unpowered** (passive target) | GPS beacon tested separately at 72h powered |
| Pass criteria | No functional degradation | **RCS ≤1 dB degradation; GPS transmitting** | Product-specific criteria (radar-only target) |

#### Method 514.8 — Vibration (Tailored to wave cycling)

| Parameter | Standard | Tailored | Rationale |
|-----------|----------|----------|-----------|
| Frequency range | 5-500 Hz | **0.1-0.15 Hz** (wave period) | SS 5-6 wave period 7-10 s |
| Amplitude | Depends on category | **±7.5° roll, ±1.5° pitch** | Wave slope from environmental survivability analysis |
| Duration | 60 min per axis | **72h continuous** (or accelerated equivalent) | 37,000 cycles at deployment duration |
| Axis | 3 axes sequential | **Roll axis only** (dominant motion) | Circular pontoon, roll ≈ pitch |
| Pass criteria | No structural failure | **No bolt loosening; reflector alignment maintained ±0.1°; no structural crack** | Product-specific |

---

## 3. MIL-STD-882E — System Safety

### 3.1 Safety Program Requirements

| Task | Description | Phase | Requirements | Deliverable |
|------|-------------|-------|--------------|-------------|
| **Task 201** | System Safety Program Plan | Phase 1 | SAF-001 to SAF-007 | SSPP document |
| **Task 202** | System Safety Management | All | — | Program oversight |
| **Task 205** | Preliminary Hazard Analysis (PHA) | Phase 1-2 | SAF-001 to SAF-007 | PHA report |
| **Task 208** | Safety Assessment Report | Phase 3 | All SAF | SAR before live-fire |
| **Task 209** | Safety Review Board | Phase 3 gate | All SAF | SRB approval to proceed |

> **Rev B change:** Task 206 (Subsystem Hazard Analysis) no longer required — propane subsystem removed. Mooring and tow hazards addressed directly in PHA.

### 3.2 Preliminary Hazard Analysis — Hazard Identification

| Hazard # | Hazard | Severity | Probability | Risk (HRI) | Category | Mitigation | Requirement |
|----------|--------|----------|-------------|-------------|----------|------------|-------------|
| H-01 | **Mooring failure → drift into shipping lane** | II (Critical) | D (Remote) | MEDIUM | Mooring | Storm-rated mooring, GPS position monitoring, pre-deploy verification | SAF-005, FOR-006 |
| H-02 | **Personnel injury during tow in SS 5** | II (Critical) | C (Occasional) | HIGH | Tow | SWL-rated tow line, bridle attachment, drogue, crew PPE | SAF-007, TRA-004 |
| H-03 | **Reflector falls from mount in heavy seas** | III (Marginal) | D (Remote) | LOW | Structure | Nylock + safety wire, fatigue-rated mounts | FOR-010 |
| H-04 | **GPS beacon failure → target position unknown** | II (Critical) | D (Remote) | MEDIUM | Signals | 72h battery, waterproof mount, redundant Iridium option | ENR-001, SIG-007 |
| H-05 | **Target capsizes before missile engagement** | II (Critical) | E (Improbable) | LOW | Stability | GM ≥ 80 m (8.0m pontoon), inherently stable design | SAF-007, KIN-001 |
| H-06 | **Marine debris contamination post-engagement** | III (Marginal) | B (Probable) | MEDIUM | Environmental | HDPE + foam = non-toxic, recoverable; debris recovery plan | SAF-006 |
| H-07 | **Anchor drags → target off station at firing time** | II (Critical) | D (Remote) | MEDIUM | Mooring | Proper anchor type/size, scope ratio, pre-deploy verification, GPS monitoring | FOR-007, OPR-006 |
| H-08 | **Tow line parts → target adrift during transit** | III (Marginal) | D (Remote) | LOW | Tow | Dyneema SWL ≥8,000 kgf, bridle reduces shock; GPS beacon active | SAF-007, TRA-004 |

> **Rev B change:** Propane hazards (former H-01 propane leak, H-08 propane ignition failure) removed — no propane subsystem. Hazards renumbered. Total reduced from 10 → 8.

### 3.3 Risk Acceptance Matrix

| | Catastrophic (I) | Critical (II) | Marginal (III) | Negligible (IV) |
|---|---|---|---|---|
| **Frequent (A)** | UNACCEPTABLE | UNACCEPTABLE | UNACCEPTABLE | REVIEW |
| **Probable (B)** | UNACCEPTABLE | UNACCEPTABLE | **H-06** REVIEW | ACCEPTABLE |
| **Occasional (C)** | UNACCEPTABLE | **H-02** REVIEW | ACCEPTABLE | ACCEPTABLE |
| **Remote (D)** | REVIEW | **H-01,H-04,H-07** | **H-03,H-08** | ACCEPTABLE |
| **Improbable (E)** | REVIEW | **H-05** | ACCEPTABLE | ACCEPTABLE |

**Summary:** No UNACCEPTABLE risks. Two hazards in REVIEW category require documented mitigation:
- H-02 (tow crew safety): Mitigated by SWL-rated equipment, sea state limits, crew PPE
- H-06 (debris): Mitigated by non-toxic materials, debris recovery plan

> **Rev B improvement:** Removal of propane system eliminated 2 hazards (former H-01 Catastrophic propane leak, H-08 propane ignition failure), improving overall safety profile. No Catastrophic-severity hazards remain.

---

## 4. Vietnamese National Standards (TCVN)

### 4.1 Identified Applicable TCVN Standards

| Standard | Title (Translated) | Applicability | Compliance | Requirement | Status |
|----------|---------------------|---------------|------------|-------------|--------|
| **TCVN 6259:2003** | Rules for construction of steel sea-going ships | REF — not a vessel, reference design practice | REF | GEO-001, MAT-005 | Reference only (not classified as vessel) |
| **TCVN 8366:2010** | Pressure equipment — Technical requirements | N/A | — | — | **Rev B: N/A — no pressure systems** |
| **TCVN 9987:2013** | Marine navigation aids | REF — radar reflectors (navigation) | REF | GEO-005 | Military target, not navigation aid |

> **Rev B change:** TCVN 6153:1996 (pressure vessels), TCVN 7441:2004 (LPG safety), and TCVN 7111:2002 (transportable gas cylinders) removed — no propane/LPG subsystem. TCVN 8366:2010 reclassified to N/A.

### 4.2 TCVN Gap Analysis

| Gap | Description | Impact | Resolution Approach |
|-----|-------------|--------|---------------------|
| **No TCVN for military sea targets** | Novel product — no Vietnamese standard exists | HIGH | Propose compliance via MIL-STD-810H + MIL-STD-882E tailoring, document as technical basis |
| **No TCVN for AM components in military use** | AlSi10Mg LPBF not covered by Vietnamese standards | MEDIUM | Reference ASTM F3301 (AM PBF) + manufacturer material certification |

> **Rev B improvement:** Propane safety gap ("propane safety for at-sea unmanned platforms") eliminated — no propane subsystem. TCVN compliance simplified from 6 → 3 applicable standards (2 REF + 1 N/A).

> **TBD-002:** Full TCVN mapping requires engagement with VPN Technical Standards Division (S-10). Target: Phase 2 start.

---

## 5. Additive Manufacturing Standards

### 5.1 AM Component: AlSi10Mg Reflector Mounting Frame

| Standard | Scope | Applicability | Compliance | Notes |
|----------|-------|---------------|------------|-------|
| **ASTM F3301-18a** | PBF-LB/M process control | HIGH | TC | Process parameters for AlSi10Mg |
| **ASTM F3318-18** | AM AlSi10Mg mechanical properties | HIGH | FC | Minimum UTS, yield, elongation |
| **ISO/ASTM 52910:2018** | AM design guidelines | MEDIUM | REF | General DfAM principles |
| **ISO/ASTM 52904:2019** | AM qualification principles | MEDIUM | TC | Adapted for non-structural component |
| **ASTM B937-18** | AlSi10Mg chemical composition | HIGH | FC | Powder certification requirement |

### 5.2 AM Qualification Approach

The AM reflector mounting frame is **non-structural for safety purposes** — it carries only the weight of three 3.7 kg face plates (11.1 kg total). Failure of the AM frame results in RCS degradation (performance loss), NOT personnel safety hazard.

| Qualification Level | Requirement | Rationale |
|---------------------|-------------|-----------|
| **Material** | Powder certification per ASTM B937 (composition, PSD, flowability) | Ensure consistent feedstock |
| **Process** | Build parameters recorded per ASTM F3301 (laser power, speed, hatch, layer thickness) | Traceability |
| **Part** | Dimensional inspection (CMM or 3D scan), visual inspection (no cracks, delamination) | Geometric accuracy |
| **Performance** | Orthogonality verification (±0.1° between mounting surfaces), RCS measurement | Functional acceptance |
| **Certification** | Material test certificate + dimensional report + RCS test result per unit | Deliverable per frame |

---

## 6. Materials Standards

### 6.1 Material Certification Requirements

| Material | Application | Standard | Certification Required | Requirement |
|----------|-------------|----------|----------------------|-------------|
| **6061-T6 Aluminum** | CNC face plates | ASTM B209 | Mill certificate (composition, temper, mechanical) | MAT-003 |
| **AlSi10Mg (LPBF)** | AM mounting frames | ASTM F3318, B937 | Powder cert + build report + mechanical test coupons | MAT-004 |
| **HDPE** | Hull (rotomolded) | ASTM D1248, ASTM D4976 | Resin certificate (density, MFI, UV stabilizer) | MAT-001 |
| **Closed-cell PU foam** | Flotation fill | ASTM D1622 (density), ASTM D2842 (water absorption) | Density ≥32 kg/m³, water absorption ≤5% by volume | MAT-002 |
| **S235 steel** | Structural frame | EN 10025-2 | Mill certificate (composition, mechanical) | MAT-005 |
| **G30 chain, 12-16mm** | Mooring | EN 818-3 or equivalent | Test certificate (proof load, breaking load) | MAT-006 |
| **Hot-dip galvanize** | Steel corrosion protection | ASTM A123 / ISO 1461 | Zinc thickness ≥86 μm (for steel >6mm) | MAT-005 |
| **Anodize Type II** | Al face plate protection | MIL-A-8625F | Coating thickness ≥10 μm | MAT-008 |
| **Anodize Type III** | AM frame protection | MIL-A-8625F | Coating thickness ≥25 μm, hardness ≥60 HRC equivalent | MAT-009 |

> **Rev B.1 update:** Mooring chain **12-16mm pending Phase 2 catenary analysis (TBD-011)**. Rev B.1 peak mooring 1,512 kgf (masts increase windage).

---

## 7. Marine and Mooring Standards (Reference)

| Standard | Title | Applicability | Compliance | Notes |
|----------|-------|---------------|------------|-------|
| **API RP 2SK** | Design of mooring systems | REF | Single-point mooring sizing guidance | Used for force analysis methodology |
| **OCIMF MEG4** | Mooring equipment guidelines | REF | Chain and anchor sizing tables | Commercial vessel standard, adapted for small platform |
| **IALA Guideline 1093** | Marine aids: radar reflectors | REF | Reflector performance measurement method | Used for RCS verification protocol |
| **ISO 12215-5** | Small craft hull design pressures | REF | Hull scantling for wave loads | **8.0 m platform**, reference for structural sizing |

---

## 8. Standards Compliance Test Plan

### 8.1 Phase 3 Test Program — Standards-Driven Tests

| Test | Standard Basis | Duration | Cost | Requirements Verified |
|------|---------------|----------|------|-----------------------|
| **Salt fog 72h** | MIL-STD-810H 509.7 (tailored) | 3 days | $3,000 | OPR-009, MAT-008, MAT-009 |
| **Mooring load test** | API RP 2SK (adapted) | 2 days | $5,000 | FOR-006, FOR-007, ASM-005 |
| **RCS measurement (360°)** | IALA 1093 (adapted) | 2 days | $5,000 | SIG-001 to SIG-005, SIG-008 |
| **Sea trial — SS 5 anchor** | MIL-STD-810H 514.8 (tailored) | 3 days | $8,000 | OPR-002, OPR-003, OPR-004, KIN-001 |
| **GPS 72h endurance** | — (functional test) | 3 days | $500 | ENR-001, ENR-002, SIG-006, SIG-007 |
| **Deployment exercise** | — (operational demonstration) | 1 day | $3,000 | ERG-001 to ERG-005, OPR-001 |
| **TOTAL** | | | **$24,500** | |

> **Rev B change:** Propane pressure test ($500) removed — no propane subsystem. Total reduced from $25,000 → **$24,500**. Test count reduced from 7 → 6.

### 8.2 Phase 3 Test Sequence

```
STANDARDS COMPLIANCE TEST SEQUENCE (Rev B)
═══════════════════════════════════════════════════════

Week 1:  Salt fog test (72h) on component samples
         → Face plates, AM frames, GPS beacon
         → Pass criteria: RCS ≤1 dB loss, GPS functional

Week 2:  GPS 72h endurance test
         → 72h powered GPS beacon
         → Pass criteria: position fix ≥99% availability

Week 3:  Mooring hardware load test (shore-based)
         → Apply 4,536 kgf to chain/shackle/pad eye assembly
         → Pass criteria: no failure, no permanent deformation

Week 4:  RCS measurement (anechoic or open range)
         → Full 360° sweep at X-band (9.4 GHz)
         → Pass criteria: ≥1,000 m² average, ≤±2 dB, ≥700 m² minimum

Week 5-7: Sea trial (3-day anchor test, SS 5 target)
         → Deploy target, anchor 72h, measure position/condition
         → Pass criteria: anchor holds, all systems functional, RCS maintained

Week 8:  Deployment exercise (1 day)
         → Full crew deployment in SS 3-4, time measurement
         → Pass criteria: ≤30 min, ≤4 crew, tool-free connections
```

---

## 9. Compliance Summary Matrix

| Requirement ID | MIL-STD-810H | MIL-STD-882E | TCVN | ASTM/ISO | Compliance Level |
|----------------|:---:|:---:|:---:|:---:|---|
| GEO-001 to GEO-009 | — | — | REF (6259) | REF (12215) | REF |
| KIN-001 to KIN-005 | TC (514.8) | — | — | — | TC |
| FOR-001 to FOR-010 | TC (516.8) | Task 205 | — | REF (API 2SK) | TC |
| ENR-001 to ENR-004 | — | — | — | — | — |
| MAT-001 to MAT-009 | FC (509.7) | — | — | FC (B209, F3301) | FC |
| SIG-001 to SIG-008 | — | — | — | REF (IALA) | REF + T |
| SAF-001 to SAF-007 | — | FC (Tasks 201-209) | — | — | FC |
| ERG-001 to ERG-007 | — | Task 205 | — | — | TC |
| PRD-001 to PRD-008 | — | — | — | FC (F3301) | FC (AM only) |
| QUA-001 to QUA-007 | — | — | — | FC (52904) | FC (AM only) |
| ASM-001 to ASM-005 | — | — | — | — | — |
| TRA-001 to TRA-006 | — | — | — | — | — |
| OPR-001 to OPR-010 | FC (501,502,507,509,512) | — | — | — | TC |
| MNT-001 to MNT-004 | — | — | — | — | — |
| CST-001 to CST-007 | — | — | — | — | — |
| SCH-001 to SCH-006 | — | — | — | — | — |

> **Rev B changes to compliance matrix:**
> - ENR reduced from 7 → 4 (propane removed) — no TCVN compliance required for energy
> - SAF reduced from 10 → 7 (propane safety removed) — TCVN 7441 compliance no longer needed
> - SIG reduced from 11 → 8 (IR signature removed)
> - TRA reduced from 7 → 6 (propane transport removed) — TCVN 7111 compliance no longer needed
> - ASM reduced from 6 → 5 (superstructure assembly removed)
> - MNT reduced from 5 → 4 (propane inspection removed)

---

## Cross-References

- [[requirements_list.md]] — Full requirements list (116 requirements, 16 categories) — Rev B.1
- [[stakeholder_analysis.md]] — S-10 Regulatory Authority needs and communication plan
- [[requirements_validation.md]] — Completeness and gate criteria check
- [[../00_odi/phase0_final_revision.md]] — Specifications driving requirements
- [[../00_odi/environmental_survivability.md]] — Environmental conditions and test parameters
