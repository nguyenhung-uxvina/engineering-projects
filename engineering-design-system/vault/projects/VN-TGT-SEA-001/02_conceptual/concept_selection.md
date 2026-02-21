---
project: VN-TGT-SEA-001
phase: 2
type: concept_selection
version: 1.0
created: 2026-02-10
status: draft
step: 6 of 6
---

# Step 6: Concept Selection — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Document the formal concept selection decision, present the selected architecture in detail, identify development risks, and define Phase 3 entry tasks.
**Method:** Pahl & Beitz Step 6 — Selection and Firm-Up (VDI 2221/2225)
**Input:** [[concept_evaluation.md]] — VDI 2225 evaluation of 4 concepts (Step 5)

---

## 1. Selection Decision

```
+===============================================================+
|                  CONCEPT SELECTION DECISION                     |
+=================================================================+
|                                                                 |
|  SELECTED: Concept A -- "Baseline Optimized"                    |
|                                                                 |
|  VDI 2225 Score: 81.8% (PROCEED)                                |
|                                                                 |
|  Key advantages:                                                |
|    1. Best RCS performance (4/4) -- 8x 0.8m hybrid reflectors  |
|       produce >1,000 m^2 average, proven retroreflection        |
|       physics, AM frame ensures +/-0.1 deg orthogonality        |
|    2. Best safety profile (4/4) -- fully passive, no active     |
|       electronics except GPS beacon, no C2 vessel, no fuel      |
|    3. Meets cost target ($35.6K <= $36K @ 10 units) -- hybrid   |
|       AM/CNC approach balances precision and affordability       |
|    4. Deployable by 4 crew in <=30 min -- pre-deployed mooring  |
|       concept, socket-insert mast erection, surface tow         |
|    5. 85-90% local content -- HDPE hull, steel frame, CNC       |
|       plates, mooring all Vietnamese-sourced                     |
|    6. Lowest development risk -- hybrid AM/CNC de-risks full-   |
|       AM approach, CNC fallback available, all other subsystems  |
|       are TRL 9 proven marine technology                         |
|                                                                 |
|  Main risks:                                                    |
|    1. Military AM acceptance (50% probability, HIGH impact)     |
|    2. Mast structural performance in SS 6 (15%, MEDIUM)         |
|    3. 8.0m HDPE hull fabrication method (20%, MEDIUM)           |
|                                                                 |
|  Fallback: Concept A-CNC variant                                |
|    - Same architecture, CNC-only reflectors                     |
|    - +/-0.3 deg tolerance (vs +/-0.1 deg hybrid)                |
|    - $28.6K/unit (20% below target)                             |
|    - ~800-1,000 m^2 RCS (marginal but viable for most seekers)  |
|                                                                 |
+=================================================================+
```

---

## 2. Elimination Rationale

Why each alternative concept was eliminated from further development:

| Concept | VDI 2225 Score | Primary Elimination Reason | Secondary Factors |
|---------|---------------|----------------------------|-------------------|
| **B: Spar Buoy** | **65.0%** | Cost ($55-70K = 1.5-2x target budget) | Deployment complexity (upending at site, ~2,500 kg, needs crane or ballast flooding), unfamiliar technology in Vietnamese defense context, limited reflector count on A-frame top |
| **C: Multi-Hull** | **60.0%** | Cost ($50-65K = 1.4-1.8x target budget) | 3-point mooring complexity (3 anchors, no weathervaning = asymmetric storm loads), deployment requires crane-equipped vessel, cross-deck fatigue risk in SS 6 |
| **D: Active Barge** | **39.8%** | **Two showstoppers:** Cost = 0 ($80-120K), Survivability = 1 (flat barge in SS 5-6) | Not passive (active transponder violates core design philosophy), "fake" RCS signature (wrong Doppler/glint/polarization characteristics), EMC interference risk during missile engagement, battery fire hazard |

### Elimination Decision Tree

```
                        All 4 Concepts
                              |
                 +------------+-----------+
                 |                        |
           Score >= 70%?           Score < 70%
           (VDI 2225)              ELIMINATE
                 |                        |
          +------+------+          +------+------+
          |             |          |      |      |
       Concept A     (none)     Con B  Con C  Con D
        81.8%                   65.0%  60.0%  39.8%
          |
    Any criterion = 0?
          |
         NO (min = 3)
          |
    PROCEED to Phase 3
```

**Key observations:**
- Concept A is the only concept that exceeds the 70% gate threshold
- Concept A wins in ALL sensitivity analysis scenarios (see [[concept_evaluation.md#6. Sensitivity Analysis]])
- Cost (criterion 3) is the decisive differentiator: only Concept A meets the $36K target
- Concept D has two independently disqualifying scores (cost = 0, survivability = 1)

---

## 3. Selected Concept Architecture

### 3.1 Side View

```
CONCEPT A: "BASELINE OPTIMIZED" -- SIDE VIEW (Section Through Center)
=========================================================================

                                GPS beacon (>= 4.5 m AGL)
                                    |
                                    * [beacon]
                                    |
                               +----+----+  Reflector (0.8m edge, 15 kg)
                               | corner  |  at 3.0-4.0 m AGL (center)
                               |reflector|  hybrid AM frame + CNC faces
                               +----+----+
                                    |
                                    |  Steel mast (60mm x 4mm galv tube)
                                    |  ~3.0 m above deck, 16 kg/mast
                                    |  socket-insert, field-erectable
     +--R--+                        |                        +--R--+
     |     |   +--------------------+--------------------+   |     |
     | ref |   |  STEEL DECK (scuppers around perimeter) |   | ref |
     +--+--+   |           pad eye (center)              |   +--+--+
        |      |             for SPM                     |      |
 ~~~~~~=+======+================+========================+======+=~~~~~ WL
     |  ################################################################  |
     |  ##  HDPE hull (8.0 m diameter, 0.5 m depth)  ##################  |  0.5 m
     |  ##  closed-cell PU foam fill (unsinkable)    ##################  |
     |  ################################################################  |
     +----------------------------------+-----------------------------------+
                                        |
                                        |  G30 chain (12-16 mm, 30-50 m)
                                        |
                                        |  polyester rode (20 mm, 50-100 m)
                                        |  (scope depends on depth)
                                        |
                                        |
                                     [anchor]  Danforth/Bruce 30-50 kg
                                   ///////////  SEABED  //////////////
```

### 3.2 Top View

```
CONCEPT A: "BASELINE OPTIMIZED" -- TOP VIEW
=========================================================================

                         N (000 deg)
                             |
                        +--- R1 ---+
                       / |  mast   | \
                      /  |  +refl  |  \
                R8 --/   |         |   \-- R2
               /         |         |         \
              /      GPS beacon    |          \
             |       (4.5m AGL)    |           |
             |           |         |           |
        W ---R7          |   8.0 m dia         R3--- E
        (270)            |   HDPE platform     (090)
             |           |         |           |
             |      central pad    |           |
              \      eye (SPM)    |          /
               \         |       |         /
                R6 --\   |       |   /-- R4
                      \  |       |  /
                       \ |       | /
                        +--- R5 ---+
                             |
                         S (180 deg)

        8 masts at 45 deg spacing around platform perimeter
        Mast circle radius: ~3.2 m from center
        Reflector-to-reflector clearance: ~2.01 m (arc)
        Central pad eye for single-point mooring
        Scuppers at platform perimeter for self-draining deck
        Tow bridle attachment: 2 points (fore/aft quadrants)
```

### 3.3 Key Dimensions

| Parameter | Value | Requirement Ref. |
|-----------|-------|-----------------|
| Platform diameter | 8.0 m | GEO-001 |
| Hull depth | 0.5 m | GEO-002 |
| Freeboard (at 980 kg) | ~0.48 m | GEO-003 |
| Draft (at 980 kg) | ~0.019 m (1.9 cm) | GEO-007 |
| Mast height above deck | ~3.0 m | GEO-010 |
| Reflector center height | 3.0-4.0 m AGL | GEO-005, SIG-003 |
| GPS beacon height | >=4.5 m AGL | GEO-006, SIG-007 |
| Total displacement | 980 kg | GEO-007 (limit 1,100 kg) |
| Reserve buoyancy | >93% | SAF-007 |
| Metacentric height (BM) | 210.3 m | KIN-001 |
| Mast spacing (arc) | 2.01 m | SIG-004 |
| Reflector edge length | 0.8 m | SIG-001 |
| Mooring scope (typical 30m depth) | ~5:1 to 7:1 | FOR-005 |
| Swing circle radius (30m depth) | ~70-240 m | OPR-006 |

---

## 4. Architecture Layer Summary

| Layer | Component | Working Principle | Material | Mass (kg) | Cost Est. |
|-------|-----------|-------------------|----------|-----------|-----------|
| **L0** | Storm mooring system | P2.1: SPM catenary — gravity catenary absorbs shock, Danforth/Bruce anchor holds via fluke friction + suction | Danforth/Bruce 30-50 kg anchor + G30 galvanized chain (12-16 mm, 30-50 m) + polyester braided rode (20 mm, 50-100 m) + swivel + shackles | ~100 | ~$2,500 |
| **L1** | Flotation hull | P1.1: HDPE solid circular pontoon — Archimedes buoyancy, extreme waterplane area gives BM = 210.3 m, closed-cell PU foam fill for unsinkability | HDPE rotomolded or welded shell + closed-cell PU rigid foam fill | ~350 | ~$8,000 |
| **L2** | Structural frame | Steel frame welded to hull inner surface — distributes mooring + mast loads, includes central pad eye (SWL 4,536 kgf) and tow bridle points (SWL 7,524 kgf) | S235 galvanized mild steel (flat bar + plate + pad eye) | ~180 | ~$3,500 |
| **L2.5** | Mast system | P4.1: Fixed cantilever in deck socket — 60 mm OD x 4 mm wall galvanized steel tube, bending capacity 1,303 N-m (18% margin over 1,100 N-m required), socket-insert for field erection | Galvanized steel tube (60 mm x 4 mm wall), S235, socket flanges welded to frame | 128 (8 x 16) | ~$1,400 |
| **L3** | Signature module (8 reflectors) | P3.1: Trihedral corner reflectors — 3-bounce retroreflection, sigma = 12*pi*a^4/lambda^2 = 152.3 m^2 per reflector | CNC machined 6061-T6 aluminum faces (3 per reflector) + AM AlSi10Mg lattice frames (orthogonality +/-0.1 deg) | 120 (8 x 15) | ~$16,000 |
| **L3+** | Tracking beacon | P5.1: GPS beacon with satellite relay — GNSS fix + Iridium data link, +/-5 m CEP, 1 Hz, 72h battery | COTS GPS/Iridium unit + Li-ion battery pack, IP67/68 enclosure | ~5 | ~$2,000 |
| | | | **TOTAL DISPLACEMENT** | **~983 kg** | **~$33,400** |

**Notes:**
- Total displacement ~983 kg is within the 1,100 kg limit (GEO-007), providing ~12% margin for fasteners, coatings, and design growth
- Unit cost estimate ~$33,400 for hardware; $35,640 fully loaded (includes labor, assembly, QC, margin) @ 10 units
- L0 mooring components are depth-dependent; mass and cost shown for typical 30 m depth deployment
- L3 cost is the primary cost driver ($16K = 48% of hardware cost) due to hybrid AM/CNC manufacturing

---

## 5. Development Risk Register (Selected Concept)

| # | Risk Description | Prob. | Impact | Risk Level | Mitigation Strategy | Residual Risk | Trend |
|---|------------------|-------|--------|------------|---------------------|---------------|-------|
| **R-1** | **Military AM acceptance** — Vietnamese Navy may not accept additive-manufactured components in a military procurement. No precedent for AM parts in VPN weapon systems. | **50%** | **HIGH** | **HIGH** | (a) Live-fire prototype demo with AM frames to prove performance equivalence; (b) CNC-only fallback (Concept A-CNC) available at $28.6K/unit with ~800-1,000 m^2 RCS; (c) Frame AM parts to ASTM F3301 with full material certification | MEDIUM | Stable -- requires prototype demo in Phase 3 to resolve |
| **R-2** | **Mast structural integrity in SS 6** — Free-standing 60 mm x 4 mm cantilever mast at 3.0 m height has only 18% bending moment margin (1,303 vs 1,100 N-m required). Fatigue from 40,000+ wave cycles in SS 6 over 72h is unverified. | **15%** | **MEDIUM** | **MEDIUM** | (a) Phase 3 detailed FEA of mast + socket under combined static/dynamic loads; (b) Guyed mast fallback (P4.2) reduces base moment by 60-80%; (c) Increase tube OD to 76 mm x 5 mm if margin insufficient (weight +3 kg/mast) | LOW | Favorable -- multiple design options |
| **R-3** | **8.0m HDPE hull fabrication** — No Vietnamese rotomolder has an 8.0m diameter capacity. Alternative is thermoplastic welding of HDPE sections, which introduces seam integrity and foam fill complexity. | **20%** | **MEDIUM** | **MEDIUM** | (a) 2-section hull design (2 x 4.0m half-discs, bolted + sealed at midline); (b) Local supplier qualification program in Phase 3; (c) Steel hull fallback (heavier but proven fabrication) | LOW-MEDIUM | Stable -- supplier survey needed |
| **R-4** | **AM reflector RCS mismatch** — Actual RCS of hybrid AM/CNC reflectors may differ from theoretical prediction due to surface roughness (AM Ra ~10 um), joint tolerances, or lattice frame RF scattering. | **15%** | **MEDIUM** | **LOW-MEDIUM** | (a) Reflector physics well-established (corner reflector RCS is classical EM theory); (b) CNC faces provide the reflecting surfaces (smooth, Ra < 1 um); (c) Prototype RCS measurement in Phase 3 using anechoic chamber or outdoor range; (d) AM frames are structural only, not reflecting surfaces | LOW | Favorable -- physics well understood |
| **R-5** | **Mooring anchor drag in SS 6** — Danforth/Bruce anchor in sand/mud may drag in sustained SS 6 conditions (peak mooring load 1,512 kgf with 3:1 SWL = 4,536 kgf anchor capacity required). Incorrect anchor setting or unfavorable seabed conditions increase drag risk. | **20%** | **HIGH** | **MEDIUM-HIGH** | (a) Proper anchor setting protocol: deploy in fair weather, set with tug at 2x working load; (b) Pre-deploy mooring system before target, allowing verification of anchor hold; (c) Phase 3 catenary analysis for 12 mm vs 16 mm chain selection; (d) Consider Bruce anchor (better in varied seabed) over Danforth | MEDIUM | Stable -- well-understood marine engineering |

### Risk Summary

```
RISK MATRIX (Selected Concept A)
==================================

              LOW IMPACT    MEDIUM IMPACT   HIGH IMPACT
            +-------------+---------------+-------------+
    HIGH    |             |               |    R-1      |
    (>40%)  |             |               | (AM accept) |
            +-------------+---------------+-------------+
    MEDIUM  |             |  R-3 (hull)   |    R-5      |
    (20-40%)|             |  R-4 (RCS)    | (anchor)    |
            +-------------+---------------+-------------+
    LOW     |             |  R-2 (mast)   |             |
    (<20%)  |             |               |             |
            +-------------+---------------+-------------+

Total risks: 5
  HIGH risk: 1 (R-1 -- mitigated by CNC fallback)
  MEDIUM-HIGH risk: 1 (R-5)
  MEDIUM risk: 2 (R-2, R-3)
  LOW-MEDIUM risk: 1 (R-4)
  Showstoppers: 0 (all risks have mitigations)
```

---

## 6. Phase 3 Entry Recommendations

Priority tasks for Embodiment Design (Phase 3), ordered by risk reduction impact:

| Priority | Task Description                                                                                                                                                                                                                                                                             | TBD Reference | Risk Addressed                             | Deliverable                                                                                | Est. Effort |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ | ----------- |
| **1**    | **Mast structural design** — Determine free-standing vs guyed configuration. Calculate bending moment, shear, fatigue life (40,000+ cycles). Select final tube section. Design socket-to-frame connection detail.                                                                            | TBD-011       | R-2 (mast SS 6)                            | Mast assembly drawing, FEA report, fatigue analysis                                        | 2-3 weeks   |
| **2**    | **8.0m HDPE hull fabrication method** — Survey Vietnamese HDPE fabricators. Determine 1-piece rotomold feasibility vs 2-section welded/bolted hull. Define foam fill procedure. Prototype hull section if needed.                                                                            | TBD-007       | R-3 (hull fab)                             | Supplier qualification report, hull fabrication drawing, foam fill procedure               | 3-4 weeks   |
| **3**    | **AM reflector prototype + RCS validation** — Manufacture 1 hybrid AM/CNC corner reflector (0.8m edge). Measure RCS in anechoic chamber or outdoor range. Compare measured vs predicted 152.3 m^2. Validate orthogonality +/-0.1 deg.                                                        | TBD-003       | R-1 (AM accept), R-4 (RCS mismatch)        | Prototype reflector, RCS measurement report, AM material certification                     | 4-6 weeks   |
| **4**    | **Mooring catenary analysis** — Model catenary behavior for 12 mm vs 16 mm G30 chain + 20 mm rode at 3 standard depths (15 m, 30 m, 50 m). Calculate scope ratios, horizontal restoring force curves, and peak anchor loads in SS 6.                                                         | TBD-011       | R-5 (anchor drag)                          | Catenary analysis report, chain/rode selection, anchor sizing per depth                    | 1-2 weeks   |
| **5**    | **Transport solution for 8.0m hull** — Determine oversize transport permit requirements (Vietnamese road regulations). Evaluate trailer options vs 2-section disassembly for standard flatbed. Define port handling procedure.                                                               | TBD-008       | Logistics, deployment                      | Transport plan, permit requirements, handling procedure                                    | 1-2 weeks   |
| **6**    | **Depth-dependent mooring kit definition** — Define 3 standard mooring kits for shallow (10-20 m), medium (20-40 m), and deep (40-60 m) water deployment. Specify chain length, rode length, anchor size, and total kit mass/cost for each.                                                  | TBD-010       | R-5 (anchor drag), operational flexibility | Mooring kit specifications (3 variants), BOM per variant, cost per variant                 | 1-2 weeks   |
| **7**    | **DfX review (4 priority categories)** — Conduct formal Design for X reviews: (a) DfCorrosion (marine environment, galvanic couples), (b) DfManufacture (local fabrication capabilities), (c) DfAssembly (field erection by 4 crew), (d) DfMaintenance (inter-test inspection/repair cycle). | --            | All risks, lifecycle cost                  | DfX checklist (4 categories), design change recommendations, material compatibility matrix | 2-3 weeks   |

### Phase 3 Schedule Estimate

```
PHASE 3 TIMELINE (Estimated)
=================================================================

Week:  1    2    3    4    5    6    7    8    9   10   11   12
       |----|----|----|----|----|----|----|----|----|----|----|----|

Task 1: Mast design        [====|====|====]
Task 2: Hull fabrication   [====|====|====|====]
Task 3: AM reflector proto      [====|====|====|====|====|====]
Task 4: Mooring analysis   [====|====]
Task 5: Transport solution      [====|====]
Task 6: Mooring kits            [====|====]
Task 7: DfX review                   [====|====|====]

GATE 3 REVIEW:                                            [G3]

Total Phase 3 duration: ~10-12 weeks
Critical path: Task 3 (AM reflector prototype + RCS validation)
```

---

## 7. Gate 2 Checklist

Phase 2 (Conceptual Design) exit gate review per Pahl & Beitz / VDI 2221:

| # | Gate Criterion | Status | Evidence |
|---|---------------|--------|----------|
| 1 | Function structure covers all requirements | **PASS** | 7 main functions (F1-F7) with 21 sub-functions cover all 116 requirements across 16 categories. 100% coverage verified in [[function_structure.md#5]]. |
| 2 | >= 3 concepts evaluated | **PASS** | 4 concepts evaluated: A (Baseline Optimized), B (Spar Buoy), C (Multi-Hull), D (Active Barge). See [[morphological_matrix.md]]. |
| 3 | VDI 2225 score >= 70% for selected concept | **PASS** | Concept A scored **81.8%** (threshold: 70%). Next highest: B at 65.0%. See [[concept_evaluation.md]]. |
| 4 | No evaluation criterion scored 0 for selected concept | **PASS** | Minimum score for Concept A is **3** (out of 4) across all 8 criteria. No showstoppers. Concept D had cost = 0 and was rejected. |
| 5 | Selection rationale documented | **PASS** | Elimination rationale for B, C, D documented with specific technical/cost reasons. Sensitivity analysis confirms A wins in all weight scenarios. See Section 2 above and [[concept_evaluation.md#6. Sensitivity Analysis]]. |
| 6 | Risks identified with mitigation plans | **PASS** | 5 development risks identified (R-1 through R-5), each with probability, impact, mitigation strategy, and residual risk assessment. 0 unmitigated showstoppers. See Section 5 above. |
| 7 | Preliminary layout sketched | **PASS** | Side view and top view ASCII layouts with full dimensioning provided. Key interfaces (hull-mooring, deck-mast, mast-reflector, mast-beacon) defined. See Section 3 above. |
| 8 | Technical feasibility confirmed | **PASS** | 95% confidence. All subsystems use TRL 8-9 technology. Only novel element is hybrid AM/CNC reflector frames (TRL 6-7), with CNC-only fallback proven at TRL 9. Physics of corner reflector RCS is classical and well-validated. |

### Gate 2 Result

```
+===============================================================+
|                    GATE 2 REVIEW RESULT                         |
+=================================================================+
|                                                                 |
|  Criteria passed:   8 / 8                                       |
|  Criteria failed:   0 / 8                                       |
|                                                                 |
|  Result:  *** ALL PASS ***                                      |
|                                                                 |
|  RECOMMENDATION: PROCEED TO PHASE 3 (Embodiment Design)        |
|                                                                 |
|  Phase 3 critical path: AM reflector prototype (4-6 weeks)      |
|  Phase 3 budget:        $100,000 (per program plan)             |
|  Phase 3 duration:      ~10-12 weeks                            |
|                                                                 |
+=================================================================+
```

**Decision required from project authority:**

```
A) APPROVE  -- Proceed to Phase 3 (Embodiment Design)
B) REVISE   -- Iterate on Phase 2 (specify items to revisit)
C) PAUSE    -- Stop here, resume later
D) CANCEL   -- Abandon project
```

**AWAITING DECISION -- do NOT proceed without explicit approval.**

---

## 8. Cross-References

### Phase 2 Documents (This Phase)

- [[abstraction.md]] -- Step 1: 5-step abstraction, essential problem statement, 8 abstract functions
- [[function_structure.md]] -- Step 2: 7 main functions, 21 sub-functions, E/M/S flows, 6 internal interfaces
- [[working_principles.md]] -- Step 3: Working principles catalog (6-7 options per function), compatibility assessment
- [[morphological_matrix.md]] -- Step 4: Morphological matrix, 4 concept descriptions with architecture diagrams
- [[concept_evaluation.md]] -- Step 5: VDI 2225 evaluation, scoring rationale, sensitivity analysis
- [[concept_selection.md]] -- Step 6: This document (selection decision, architecture, risks, Phase 3 plan)

### Phase 0 Source Documents

- [[../00_odi/odi_analysis.md]] -- ODI analysis (73 outcomes, 3 EXTREME)
- [[../00_odi/re_competitive_analysis.md]] -- Competitive analysis (5 competitors, FTO clear)
- [[../00_odi/re_deep_analysis.md]] -- Deep RE: reflector physics, mooring analysis, competitor teardown
- [[../00_odi/environmental_survivability.md]] -- SS 5-6 environmental loading, mooring capacity, TPMS removal
- [[../00_odi/phase0_final_revision.md]] -- Final Phase 0 specs: >1,000 m^2 RCS, 8.0m platform, Rev B.1 changes
- [[../00_odi/phase0_synthesis.md]] -- Original Phase 0 synthesis (superseded by final revision)
- [[../00_odi/hyperganic_feasibility.md]] -- AM feasibility study (retained as reference)

### Phase 1 Source Documents

- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), 16 Pahl-Beitz categories, 91% quantified
- [[../01_requirements/stakeholder_analysis.md]] -- 10 stakeholders, RACI matrix, needs/conflicts
- [[../01_requirements/standards_mapping.md]] -- MIL-STD-810H, 882E, TCVN, ASTM, AM standards (Rev B.1)
- [[../01_requirements/requirements_validation.md]] -- Validation report (12/12 gate criteria PASS)

### Project Management

- [[../PROJECT_STATUS.md]] -- Project status tracker
- [[../00_project_brief.md]] -- Original project brief (superseded by Rev B.1)
