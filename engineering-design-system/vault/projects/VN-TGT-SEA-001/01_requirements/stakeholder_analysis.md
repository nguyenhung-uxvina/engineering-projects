---
project: VN-TGT-SEA-001
phase: 1
type: stakeholder_analysis
version: 1.0
created: 2026-02-10
status: draft
---

# Stakeholder Analysis: VN-TGT-SEA-001

**Phase:** 1 — Task Clarification
**Purpose:** Identify all stakeholders, map their needs/concerns, establish RACI matrix for requirements sign-off
**Source:** Phase 0 ODI analysis (job executor, secondary executors), competitive analysis, operational concept

---

## 1. Stakeholder Registry

### 1.1 Stakeholders Identified (10)

| # | Stakeholder | Role | Organization | Interest Level | Influence Level |
|---|------------|------|-------------|---------------|----------------|
| S-01 | **Naval Test & Evaluation Director** | Job Executor (decision-maker) | VPN Weapons Test & Acceptance Directorate | **VERY HIGH** | **VERY HIGH** |
| S-02 | **Deployment Crew Chief** | Primary operator | VPN Tug Crew (3-4 sailors) | HIGH | MEDIUM |
| S-03 | **Missile System Operator** | Fires missile at target | VPN Firing Ship CIC | HIGH | HIGH |
| S-04 | **Safety Officer** | Manages exclusion zones | VPN Range Safety Division | **VERY HIGH** | HIGH |
| S-05 | **Scoring/Evaluation Officer** | Evaluates test results | VPN Weapons Test Directorate | MEDIUM | MEDIUM |
| S-06 | **Procurement Officer** | Purchases and budgets | VPN Material Command | HIGH | HIGH |
| S-07 | **Depot/Logistics Manager** | Stores and maintains inventory | VPN Naval Logistics Base | MEDIUM | LOW |
| S-08 | **Manufacturing Lead** | Produces the targets | Indigenous manufacturer (to be selected) | HIGH | MEDIUM |
| S-09 | **AM Service Bureau** | Prints reflector mounting frames | ASEAN AM bureau (Xometry/Facfox/JR Tech) | MEDIUM | LOW |
| S-10 | **Regulatory Authority** | Approves for military use | VPN Technical Standards Division + TCVN | MEDIUM | HIGH |

### 1.2 Stakeholder Influence-Interest Matrix

```
                    INFLUENCE
                LOW          MEDIUM         HIGH          VERY HIGH
           ┌─────────────┬─────────────┬─────────────┬─────────────┐
VERY HIGH  │             │             │ S-04 Safety │ S-01 Test   │
INTEREST   │             │             │ S-06 Procure│   Director  │
           ├─────────────┼─────────────┼─────────────┼─────────────┤
HIGH       │             │ S-02 Deploy │ S-03 Missile│             │
           │             │ S-08 Mfg    │ S-10 Regul. │             │
           ├─────────────┼─────────────┼─────────────┼─────────────┤
MEDIUM     │ S-09 AM     │ S-05 Scoring│             │             │
           │             │ S-07 Depot  │             │             │
           ├─────────────┼─────────────┼─────────────┼─────────────┤
LOW        │             │             │             │             │
           └─────────────┴─────────────┴─────────────┴─────────────┘

MANAGEMENT STRATEGY:
  Top-right (S-01):        MANAGE CLOSELY — full engagement, sign-off authority
  Top-middle (S-04, S-06): KEEP SATISFIED — address concerns proactively
  Middle (S-02,S-03,S-08): KEEP INFORMED — regular updates, input on design
  Bottom-left (S-09):      MONITOR — technical interface only
```

---

## 2. Stakeholder Needs & Concerns

### S-01: Naval Test & Evaluation Director (Job Executor)

| Aspect | Detail |
|--------|--------|
| **Core need** | Reliable missile acceptance test results that are accepted by missile manufacturer |
| **Top concerns** | Test failure rate (wasted $500K missile), test window availability (monsoon), signature adequacy |
| **Success metric** | 98%+ test success rate, year-round testing capability, accepted certification |
| **Requirements driven** | RCS >1,000 m², IR 250°C, SS 5-6 deployment, 72h anchor survival |
| **Decision authority** | Final approval on all specifications, gate reviews, acceptance testing |
| **Communication** | Monthly progress reviews, gate review presentations |

### S-02: Deployment Crew Chief

| Aspect | Detail |
|--------|--------|
| **Core need** | Safe, simple, fast deployment in rough seas |
| **Top concerns** | Personal safety during tow/mooring in SS 4-5, heavy lifting, complexity |
| **Success metric** | Deploy in <30 min from mooring pickup, no injuries, crew of ≤4 |
| **Requirements driven** | Max component weight <150 kg, tool-free connections, bridle tow system |
| **Decision authority** | Abort deployment if conditions unsafe |
| **Communication** | Deployment manual, hands-on training session |

### S-03: Missile System Operator

| Aspect | Detail |
|--------|--------|
| **Core need** | Target that missile seeker acquires and tracks reliably |
| **Top concerns** | RCS too low (lock failure), RCS fading during approach, IR ambiguity |
| **Success metric** | Seeker locks at >20 km, maintains lock to terminal, no break-lock events |
| **Requirements driven** | RCS >1,000 m² (frigate class), ±2 dB stability, IR 250°C 360° |
| **Decision authority** | Reports seeker performance; can request target specification changes |
| **Communication** | Pre-test brief, post-test debrief on seeker behavior |

### S-04: Safety Officer

| Aspect | Detail |
|--------|--------|
| **Core need** | Zero risk to support personnel and vessels |
| **Top concerns** | Personnel in danger zone, propane fire/explosion, mooring failure + drift into shipping lane, debris contamination |
| **Success metric** | 5+ km clearance maintained, no propane incidents, debris recovery plan |
| **Requirements driven** | Passive operation (no C2 vessel), propane safety, anchor holding in SS 6, environmental cleanup |
| **Decision authority** | "Safe to fire" authorization; can halt any operation |
| **Communication** | Safety review at each phase gate, hazard analysis review |

### S-05: Scoring/Evaluation Officer

| Aspect | Detail |
|--------|--------|
| **Core need** | Clear hit/miss determination and accurate documentation |
| **Top concerns** | Ambiguous results, GPS beacon failure, insufficient video coverage |
| **Success metric** | Definitive hit/miss within 5 min, GPS data for miss distance estimation |
| **Requirements driven** | GPS 72h battery, 1 Hz position, waterproof beacon, video-compatible design |
| **Decision authority** | Validates test results; recommends accept/reject |
| **Communication** | Test report template, data format specifications |

### S-06: Procurement Officer

| Aspect | Detail |
|--------|--------|
| **Core need** | Cost-effective, timely delivery, budget compliance |
| **Top concerns** | Unit cost exceeding budget, AM supply chain delays, sole-source dependency |
| **Success metric** | Unit cost ≤$38K, delivery within 13 weeks, ≥2 suppliers for each component |
| **Requirements driven** | Cost targets, local content ≥85%, production rate, supply chain diversity |
| **Decision authority** | Procurement approval, budget allocation, vendor selection |
| **Communication** | Quarterly cost reviews, vendor qualification reports |

### S-07: Depot/Logistics Manager

| Aspect | Detail |
|--------|--------|
| **Core need** | Easy storage, transport, and inventory management |
| **Top concerns** | Storage space, shelf life, container compatibility, propane storage regulations |
| **Success metric** | 2-3 targets per 40ft container, 5+ year shelf life, standard warehouse storage |
| **Requirements driven** | Dimensions, weight, packaging, propane storage compliance, reflector removability |
| **Decision authority** | Storage facility allocation, transport logistics |
| **Communication** | Packaging specification, storage requirements document |

### S-08: Manufacturing Lead

| Aspect | Detail |
|--------|--------|
| **Core need** | Producible design with available equipment and skills |
| **Top concerns** | AM component lead time, CNC tolerance achievability, HDPE rotomolding access, QC procedures |
| **Success metric** | 6-8 units/month production rate, <5% rejection rate, established QC process |
| **Requirements driven** | DFM requirements, material specifications, tolerance specifications, QC criteria |
| **Decision authority** | Production feasibility sign-off, manufacturing process selection |
| **Communication** | Design for manufacturing review at Phase 2-3, production trial feedback |

### S-09: AM Service Bureau

| Aspect | Detail |
|--------|--------|
| **Core need** | Clear design files, material specifications, and order volumes |
| **Top concerns** | Build volume requirements, material availability (AlSi10Mg), tolerance specifications |
| **Success metric** | Frame delivered within 3 weeks, ±0.05° tolerance on mounting surfaces, cost within quote |
| **Requirements driven** | AM frame design file format (STL/STEP), material certification, post-processing specification |
| **Decision authority** | Print feasibility assessment, process parameter recommendation |
| **Communication** | Technical specification package, PO with delivery schedule |

### S-10: Regulatory Authority

| Aspect | Detail |
|--------|--------|
| **Core need** | Compliance with military standards and Vietnamese regulations |
| **Top concerns** | No applicable TCVN for sea targets (novel product), AM component certification, propane safety |
| **Success metric** | Documented compliance approach for all applicable standards, waiver/tailoring for non-applicable |
| **Requirements driven** | MIL-STD-810H (environmental), MIL-STD-882E (safety), TCVN (propane, marine) |
| **Decision authority** | Standards compliance approval, test protocol approval |
| **Communication** | Standards compliance matrix review, test witnessing |

---

## 3. RACI Matrix

**R**=Responsible, **A**=Accountable, **C**=Consulted, **I**=Informed

| Activity | S-01 Test Dir | S-02 Deploy | S-03 Missile | S-04 Safety | S-05 Scoring | S-06 Procure | S-07 Depot | S-08 Mfg | S-09 AM | S-10 Regul |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Requirements sign-off** | **A** | C | C | C | I | C | I | C | I | C |
| **RCS specification** | A | I | **R** | I | I | I | I | C | C | I |
| **IR specification** | A | I | **R** | I | I | I | I | C | I | I |
| **Seakeeping specification** | A | **R** | I | C | I | I | I | C | I | C |
| **Mooring specification** | A | **R** | I | C | I | I | I | C | I | I |
| **Safety requirements** | A | C | I | **R** | I | I | I | I | I | C |
| **Cost targets** | C | I | I | I | I | **A** | I | **R** | C | I |
| **Production requirements** | C | I | I | I | I | C | I | **A** | C | I |
| **Transport/storage** | I | I | I | I | I | C | **A** | **R** | I | I |
| **Standards compliance** | C | I | I | C | I | I | I | C | I | **A** |
| **AM component spec** | C | I | I | I | I | C | I | **R** | **R** | I |
| **Test protocol** | **A** | C | C | **R** | **R** | I | I | I | I | C |
| **Phase gate review** | **A** | I | I | C | I | C | I | C | I | C |
| **Deployment procedures** | C | **A** | I | **R** | I | I | I | I | I | I |
| **Acceptance test** | **A** | R | R | R | **R** | I | I | I | I | C |

---

## 4. Stakeholder Requirements Summary

### 4.1 Requirements by Stakeholder (Top 3 per stakeholder)

| Stakeholder | Req #1 | Req #2 | Req #3 |
|------------|--------|--------|--------|
| S-01 Test Director | RCS >1,000 m² 360° | SS 5-6 deployment | Test success rate >98% |
| S-02 Deployment Crew | Max component <150 kg | Deploy in <30 min | 3-4 crew max |
| S-03 Missile Operator | RCS ±2 dB through 360° | IR 250°C MWIR 360° | Seeker lock at >20 km |
| S-04 Safety Officer | 5+ km clearance | No pyrotechnics | Mooring holds in SS 6 |
| S-05 Scoring Officer | GPS 72h battery | 1 Hz position data | Waterproof beacon |
| S-06 Procurement | Unit cost ≤$38K | Local content ≥85% | ≥2 suppliers per component |
| S-07 Depot/Logistics | Container compatible | 5+ year shelf life | Standard warehouse storage |
| S-08 Manufacturing | CNC + standard fab tools | <5% rejection rate | 6-8 units/month capability |
| S-09 AM Bureau | Standard STEP/STL files | AlSi10Mg available | 3-week lead time |
| S-10 Regulatory | MIL-STD-810H compliance | Safety analysis (882E) | Documented compliance |

### 4.2 Conflict Identification

| Conflict | Stakeholders | Resolution |
|----------|-------------|------------|
| Larger reflectors (S-01/S-03) vs lighter weight (S-02) | S-01+S-03 vs S-02 | 0.8m reflectors at 15 kg each — within manual handling. Use 2-person lift. |
| Higher sea state (S-01) vs crew safety (S-04) | S-01 vs S-04 | Pre-deploy mooring in fair weather; tow in SS 4-5 only; no SS 6 tow. |
| AM precision (S-01/S-03) vs local content (S-06) | S-01 vs S-06 | Hybrid design: CNC faces local (VN), AM frames outsourced (ASEAN). 85-90% local overall. |
| Low cost (S-06) vs storm mooring (S-01) | S-06 vs S-01 | Storm mooring adds $800-3,000 per unit. Justified by 40-60% expanded test window. |
| Expendable target (S-01) vs environmental (S-04) | S-01 vs S-04 | HDPE + foam debris is recoverable and non-toxic. Debris recovery plan included. |

---

## 5. Communication Plan

| Stakeholder | Frequency | Format | Content |
|------------|-----------|--------|---------|
| S-01 Test Director | Bi-weekly + gates | Meeting + report | Progress, decisions, gate reviews |
| S-02 Deployment Crew | Phase 1, Phase 3 | Workshop | Ergonomic review, deployment trial |
| S-03 Missile Operator | Phase 1, Phase 3 | Technical brief | RCS/IR specs, seeker compatibility data |
| S-04 Safety Officer | Monthly + gates | Safety report | Hazard analysis, safety review |
| S-05 Scoring Officer | Phase 1, Phase 3 | Technical brief | GPS specs, scoring interface |
| S-06 Procurement | Quarterly | Cost report | Budget tracking, vendor status |
| S-07 Depot/Logistics | Phase 3-4 | Spec review | Packaging, storage, transport docs |
| S-08 Manufacturing | Phase 2-4 | DFM review | Drawings, tolerances, process specs |
| S-09 AM Bureau | Phase 2-3 | PO + tech spec | Design files, material cert, schedule |
| S-10 Regulatory | Phase 1, Phase 3 | Compliance matrix | Standards mapping, test protocols |

---

## Cross-References

- [[../00_odi/odi_analysis.md]] — Job executor and secondary executors (ODI Step 1)
- [[../00_odi/phase0_final_revision.md]] — Final specifications driving requirements
- [[../00_odi/environmental_survivability.md]] — Operational concept (pre-deploy mooring)
- [[requirements_list.md]] — Requirements derived from stakeholder needs
- [[standards_mapping.md]] — Standards compliance (S-10 requirements)
