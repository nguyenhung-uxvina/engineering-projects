---
project: VN-TGT-SEA-001
phase: 3
step: "E10 — Variant Evaluation"
group: DECS
version: 1.0
created: 2026-02-10
status: draft
---

# Step E10: Variant Evaluation — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Evaluate layout variants for key embodiment design decisions within the selected Concept A architecture, using mini VDI 2225 weighted scoring to select the optimal configuration for each subsystem.
**Method:** Pahl & Beitz DECS Step E10 — Variant Evaluation at embodiment level (layout alternatives within a single concept, NOT concept re-selection)
**Input:** [[PRAD_D8_design_structure.md]] (structural analysis), [[PRAD_A7_architecture_definition.md]] (architecture), [[RISM_R1_requirements_identification.md]] (74 embodiment requirements)
**Selected Concept:** Concept A "Baseline Optimized" (VDI 2225: 81.8%)

---

## 1. Scope and Approach

### 1.1 What This Step Is NOT

This is not a repeat of Phase 2 concept selection. Concept A was selected with 81.8% VDI 2225 score and is fixed. This step evaluates **layout variants** -- alternative embodiment configurations for specific subsystems where multiple valid implementations exist within Concept A.

### 1.2 Layout Decisions Requiring Variant Evaluation

Four design decisions were identified during D8 structural analysis and A7 architecture definition where the chosen configuration has viable alternatives:

| # | Decision | TBD Ref | Why Variants Exist |
|---|----------|---------|-------------------|
| 1 | Hull construction method | TBD-007 | 8.0 m diameter exceeds standard rotomold capacity; multiple fabrication paths |
| 2 | Mast configuration | TBD-011 | Free-standing baseline has 77% utilization; guyed or paired alternatives may reduce weight/cost |
| 3 | Mooring chain specification | D8 Sec 4.1 | 12 mm G30 failed SWL; 16 mm G30 marginal; higher-grade alternatives exist |
| 4 | Reflector mounting method | A7 IF-04 | Bolted baseline meets requirements; tool-free and permanent alternatives have operational trade-offs |

### 1.3 Evaluation Method

Each decision uses a mini VDI 2225 evaluation:
- **4-5 criteria** selected per decision (weighted to sum 1.0)
- **2-3 variants** scored 0-4 (0 = unacceptable, 1 = barely adequate, 2 = adequate, 3 = good, 4 = very good)
- **Weighted score** = sum(weight_i x score_i) / 4.0 x 100%
- **Threshold:** >= 65% to be considered viable; highest score selected

---

## 2. Decision 1: Hull Construction Method

### 2.1 Variant Descriptions

| Variant | Description | Key Features |
|---------|-------------|--------------|
| **A: 1-piece rotomolded** | Single 8.0 m diameter HDPE pontoon formed in one rotational mold | Seamless shell, no joint (IF-07 eliminated), requires large rotomold oven (8.5+ m capacity) |
| **B: 2-section bolted** | Two 4.0 m semicircular halves, bolted at centerline flange with EPDM gasket | Each half fits on standard flatbed (<=2.5 m road width per TRA-002), field-joinable, steel backing channel at joint |
| **C: 2-section welded on-site** | Two 4.0 m halves, HDPE extrusion-welded on-site before deployment | Permanent watertight joint, but requires HDPE welding equipment and trained operator in field |

### 2.2 Evaluation Criteria

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| C1 | Structural integrity (joint reliability) | 0.30 | Single most important -- hull failure = mission loss |
| C2 | Transportability (TRA-001, TRA-002) | 0.25 | Must fit standard transport without oversize permits |
| C3 | Manufacturing feasibility in Vietnam | 0.20 | Local content target >= 60%; supplier availability |
| C4 | Field maintainability | 0.15 | Ability to inspect, repair, and disassemble for storage |
| C5 | Cost (unit + tooling amortized over 10 units) | 0.10 | Lower weight -- cost follows design, not drives it |

### 2.3 Scoring

| Criterion | Wt | Var A: 1-piece Rotomold | Var B: 2-section Bolted | Var C: 2-section Welded |
|-----------|-----|-------------------------|-------------------------|-------------------------|
| C1: Structural integrity | 0.30 | 4 -- seamless, no joint, no leak path | 3 -- bolted joint with gasket; steel backing channel provides structural continuity; gasket needs periodic inspection | 3 -- welded HDPE joint is permanent; weld quality depends on operator skill; if done well, approaches monolithic |
| C2: Transportability | 0.25 | 1 -- 8.0 m diameter requires oversize flatbed + escort; may not fit through tunnels/bridges | 4 -- each half <=4.0 m, fits standard flatbed; 2 halves + mast crates fit one 40-ft container | 4 -- same as B for transport; joined at staging area |
| C3: Manufacturing feasibility | 0.20 | 1 -- no confirmed Vietnamese rotomold supplier with 8.5 m oven capacity; nearest likely in Thailand or China | 3 -- HDPE welding of 4.0 m sections is well within local capability; flanged construction is standard marine practice | 3 -- same fabrication as B; welding at staging site requires mobile HDPE extrusion welder |
| C4: Field maintainability | 0.15 | 2 -- monolithic hull cannot be disassembled for repair; damaged section requires full hull replacement or field patching | 4 -- can unbolt, separate halves for inspection, replace gasket, transport individually for repair | 2 -- welded joint is permanent; cannot separate for inspection; difficult to repair without cutting |
| C5: Cost | 0.10 | 2 -- rotomold tooling ~$15,000 amortized over 10 = $1,500/unit; but import cost of oversized mold adds premium | 3 -- no specialized tooling; standard HDPE welding + bolts + gasket; estimated $8,000/hull as baseline | 3 -- similar fabrication cost to B; additional cost for field welding equipment and operator |

### 2.4 Weighted Scores

| Variant | C1 (0.30) | C2 (0.25) | C3 (0.20) | C4 (0.15) | C5 (0.10) | Weighted Sum | Score (%) |
|---------|-----------|-----------|-----------|-----------|-----------|--------------|-----------|
| A: 1-piece rotomold | 1.20 | 0.25 | 0.20 | 0.30 | 0.20 | 2.15 | **53.8%** |
| **B: 2-section bolted** | 0.90 | 1.00 | 0.60 | 0.60 | 0.30 | **3.40** | **85.0%** |
| C: 2-section welded | 0.90 | 1.00 | 0.60 | 0.30 | 0.30 | 3.10 | **77.5%** |

### 2.5 Decision

**Selected: Variant B -- 2-section bolted hull (85.0%)**

Justification: Variant B scores highest across all criteria except structural integrity (where Variant A leads with a seamless shell). However, Variant A is severely penalized by transportability and manufacturing feasibility -- no confirmed Vietnamese rotomold supplier can accommodate 8.0 m diameter. The bolted joint in Variant B was structurally verified in D8 Section 5.3: 24x M10 SS316 bolts at 2.4% utilization with EPDM gasket and steel backing channel. This resolves TBD-007.

---

## 3. Decision 2: Mast Configuration

### 3.1 Variant Descriptions

| Variant | Description | Key Features |
|---------|-------------|--------------|
| **A: Free-standing cantilever** | 60 mm OD x 4 mm wall galvanized steel tube, 3.0 m above deck, base gusset reinforcement, socket-insert with locking pin | Current D8 baseline; 77.1% utilization at LC4; no cables or stays cluttering deck; clean silhouette |
| **B: Guyed masts (cable stays)** | Smaller tube (48 mm OD x 3 mm wall) with 2-3 cable stays per mast anchored to deck pad eyes | Lighter tube possible; but 8 masts x 2-3 stays = 16-24 cables crossing deck; trip/snag hazard; cable tensioning required |
| **C: A-frame pairs** | 4 A-frames (2 converging masts per corner, 90 deg apart), each supporting 2 reflectors | Reduces from 8 independent masts to 4 paired frames; inherently stable triangulated structure; but fewer mounting positions (4 not 8) |

### 3.2 Evaluation Criteria

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| C1 | Structural adequacy (FOR-011, FOR-010) | 0.25 | Must resist 1,100 N-m bending and 40,000 fatigue cycles |
| C2 | Field erection (ASM-006: <=15 min, 2 persons) | 0.25 | Equal weight to structural -- defines operational concept |
| C3 | RCS pattern uniformity (SIG-002, SIG-004) | 0.20 | 8-unit 45 deg spacing verified for <=+-2 dB; any change affects pattern |
| C4 | Deck clearance and safety | 0.15 | Crew must walk deck safely during field assembly and mooring operations |
| C5 | Weight and cost | 0.15 | Lower weight preserves margin; lower cost supports $35.6K target |

### 3.3 Scoring

| Criterion | Wt | Var A: Free-standing | Var B: Guyed | Var C: A-frame |
|-----------|-----|----------------------|--------------|----------------|
| C1: Structural adequacy | 0.25 | 3 -- 77.1% utilization with gusset; fatigue PASS at 9.7%; proven D8 analysis | 4 -- cable stays reduce bending to near-zero; tube can be lighter; but stay anchors add local stress on hull/frame | 3 -- triangulated A-frame inherently strong; but load sharing between paired masts is complex; uneven wave loading creates differential bending |
| C2: Field erection | 0.25 | 4 -- socket-insert + locking pin, <2 min per mast, tool-free (per A7 IF-03); 8 independent units, 2-person operation | 1 -- must insert mast + tension 2-3 stays per mast; 16-24 cable tensioning operations; requires turnbuckles and tension gauge; estimated 45+ min total | 2 -- 4 A-frames heavier than single masts (est. 50+ kg each); requires 3-4 persons to lift; fewer units but more complex alignment |
| C3: RCS pattern | 0.20 | 4 -- 8 reflectors at 45 deg = verified pattern with 770 m2 minimum and +-1.5 dB variation per Phase 2 analysis | 4 -- same 8 reflectors at 45 deg achievable with guyed masts; pattern unchanged | 2 -- 4 A-frames with 2 reflectors each places reflectors in pairs; inter-pair spacing is 90 deg, creating deeper nulls; minimum RCS drops below 700 m2 threshold (SIG-003 FAIL risk) |
| C4: Deck clearance | 0.15 | 4 -- clean deck; only 8 socket positions; full walk-around access | 1 -- 16-24 cable stays cross deck at ankle-to-knee height; trip hazard; cables interfere with mooring and tow operations | 3 -- 4 A-frames leave more open deck than 8 singles; but A-frame bases are wider, limiting access near corners |
| C5: Weight/cost | 0.15 | 3 -- 128 kg mast system + 4.8 kg gussets = 132.8 kg; $1,400 total (8 x $175) | 3 -- lighter tubes (~90 kg) but add cables + turnbuckles + deck eyes (~25 kg hardware); net ~115 kg; cost similar ($1,400 for tubes + $600 cable hardware) | 2 -- 4 A-frames with heavier construction; est. 160 kg total; welded paired structure more expensive to fabricate (~$2,200) |

### 3.4 Weighted Scores

| Variant | C1 (0.25) | C2 (0.25) | C3 (0.20) | C4 (0.15) | C5 (0.15) | Weighted Sum | Score (%) |
|---------|-----------|-----------|-----------|-----------|-----------|--------------|-----------|
| **A: Free-standing** | 0.75 | 1.00 | 0.80 | 0.60 | 0.45 | **3.60** | **90.0%** |
| B: Guyed | 1.00 | 0.25 | 0.80 | 0.15 | 0.45 | 2.65 | **66.3%** |
| C: A-frame | 0.75 | 0.50 | 0.40 | 0.45 | 0.30 | 2.40 | **60.0%** |

### 3.5 Decision

**Selected: Variant A -- Free-standing cantilever masts (90.0%)**

Justification: The free-standing mast dominates in field erection (the defining operational requirement) and RCS pattern uniformity. While guyed masts offer theoretical structural advantage, the 16-24 cable stays are operationally unacceptable -- they triple erection time, create trip hazards, and complicate mooring/tow operations. A-frames fail to meet the SIG-003 minimum RCS threshold due to 90 deg inter-pair spacing. The free-standing 60x4 tube with base gusset (D8 verified at 77.1% utilization) is structurally adequate with comfortable margin. This resolves TBD-011.

---

## 4. Decision 3: Mooring Chain Specification

### 4.1 Variant Descriptions

The D8 analysis (Section 4.1) established a required SWL of 4,536 kgf (3:1 safety factor on 1,512 kgf peak load at LC4). The following chain specifications are evaluated:

| Variant | Description | SWL (kgf) | Breaking (kgf) | Weight (kg/m in air) | Cost ($/m est.) |
|---------|-------------|-----------|-----------------|---------------------|-----------------|
| **A: 12 mm G30 HDG** | Standard proof coil, lightest option | 2,250 | 6,750 | 3.0 | $5 |
| **B: 16 mm G30 HDG** | Mid-size proof coil, near SWL threshold | 4,200 | 12,600 | 5.6 | $9 |
| **C: 12 mm G43 high-test** | High-test chain, same diameter as A but higher grade | 3,900 | 11,700 | 3.0 | $8 |

Note: D8 selected 19 mm G30 (SWL 5,800 kgf) after finding 12 mm and 16 mm G30 inadequate. This evaluation reconsiders whether a lighter high-test chain (G43) could meet requirements with less weight. The 19 mm G30 result from D8 serves as the reference benchmark.

### 4.2 Evaluation Criteria

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| C1 | SWL margin over 4,536 kgf requirement | 0.35 | Safety-critical -- insufficient SWL is disqualifying |
| C2 | Weight (kg/m submerged) | 0.20 | Heavier chain aids catenary but increases handling difficulty and mooring kit mass |
| C3 | Availability in Vietnam | 0.20 | G30 HDG is standard marine stock; G43 is specialty |
| C4 | Corrosion resistance (HDG uniformity) | 0.15 | Standard HDG on proof coil; high-test may have thinner galvanize on hardened links |
| C5 | Cost per meter | 0.10 | Unit cost across 20-90 m of chain per mooring kit |

### 4.3 Scoring

| Criterion | Wt | Var A: 12mm G30 | Var B: 16mm G30 | Var C: 12mm G43 |
|-----------|-----|-----------------|-----------------|-----------------|
| C1: SWL margin | 0.35 | 0 -- SWL 2,250 kgf = 49.6% of required 4,536 kgf; **DISQUALIFIED** (below 65% threshold) | 2 -- SWL 4,200 kgf = 92.6% of required; technically below 4,536 kgf; marginal by -7.4% | 1 -- SWL 3,900 kgf = 85.9% of required; below threshold by -14.1%; **FAILS** minimum SWL |
| C2: Weight | 0.20 | 4 -- 3.0 kg/m; lightest; easy handling | 3 -- 5.6 kg/m; moderate; good catenary weight for anchor performance | 4 -- 3.0 kg/m; same as 12mm G30; but lighter catenary reduces anchor holding |
| C3: Availability | 0.20 | 4 -- standard stock at every Vietnamese marine chandlery | 4 -- standard stock; 16mm is common fishing vessel chain | 2 -- G43 high-test not commonly stocked in Vietnam; likely import from Japan/Korea; 2-4 week lead time |
| C4: Corrosion resistance | 0.15 | 3 -- standard HDG G30; adequate zinc layer; proven marine service | 3 -- same HDG process; larger links have proportionally similar zinc coverage | 2 -- G43 has higher carbon steel; HDG adhesion to hardened steel may be reduced; risk of accelerated zinc loss |
| C5: Cost | 0.10 | 4 -- $5/m; cheapest option | 3 -- $9/m; moderate | 2 -- $8/m plus import premium; effective ~$12/m delivered |

### 4.4 Weighted Scores

| Variant | C1 (0.35) | C2 (0.20) | C3 (0.20) | C4 (0.15) | C5 (0.10) | Weighted Sum | Score (%) |
|---------|-----------|-----------|-----------|-----------|-----------|--------------|-----------|
| A: 12mm G30 | 0.00 | 0.80 | 0.80 | 0.45 | 0.40 | 2.45 | **61.3% -- DISQUALIFIED** |
| B: 16mm G30 | 0.70 | 0.60 | 0.80 | 0.45 | 0.30 | 2.85 | **71.3%** |
| C: 12mm G43 | 0.35 | 0.80 | 0.40 | 0.30 | 0.20 | 2.05 | **51.3% -- DISQUALIFIED** |

### 4.5 Decision

**No variant achieves SWL >= 4,536 kgf. D8 selection of 19 mm G30 HDG is CONFIRMED.**

Justification: The evaluation confirms the D8 finding. Variant A (12mm G30) is immediately disqualified at 49.6% of required SWL. Variant C (12mm G43) provides only 85.9% -- still 14% below threshold. Variant B (16mm G30) is the best of three candidates at 71.3%, but its SWL of 4,200 kgf falls 7.4% short of the 4,536 kgf requirement. The safety factor of 3:1 on peak mooring load is non-negotiable for an unattended sea target in SS 5-6.

**Confirmed selection: 19 mm G30 HDG chain** (SWL 5,800 kgf, 128% of required, 7.9 kg/m). This is the minimum chain size within the G30 product family that meets the 3:1 safety factor requirement. The added weight (7.9 vs 5.6 kg/m) actually benefits the catenary mooring by increasing anchor scope weight, reducing uplift at the anchor.

**Supplementary note on hybrid mooring:** Per D8 Section 4.2, the 19 mm chain is used only for the bottom section (20 m on the seabed) in medium and deep water configurations. A 24 mm polyester rode spans the water column, providing elastic shock absorption. This hybrid approach limits chain weight to 158 kg while maintaining catenary performance.

---

## 5. Decision 4: Reflector Mounting Method

### 5.1 Variant Descriptions

| Variant | Description | Key Features |
|---------|-------------|--------------|
| **A: Bolted to mast top plate** | 4x M10 bolts + 2x dia 8 mm dowel pins; Nordlock washers + Nylock nuts + safety wire; nylon galvanic isolation | Current D8/A7 baseline (IF-04); repeatable alignment +-0.05 deg; requires 17 mm wrench + torque wrench (50 N-m); factory pre-assembled as M5 unit |
| **B: Clamped (tool-free)** | Quick-release toggle clamps or cam-lock mechanism gripping reflector flange to mast top plate; spring-loaded alignment pins for positioning | No tools for field replacement; faster swap; but lower clamping force reduces vibration resistance; no proven marine toggle clamp at 15 kg sustained load in SS 6 |
| **C: Pre-welded (no field adjustment)** | Reflector frame permanently welded to mast top plate at factory; mast + reflector are a single inseparable unit | Eliminates IF-04 as a separable interface; maximum structural rigidity; but prevents reflector replacement; creates dissimilar metal weld (steel to AlSi10Mg -- not feasible without adapter) |

### 5.2 Evaluation Criteria

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| C1 | Alignment precision (SIG-009: +-0.1 deg) | 0.30 | Reflector orthogonality directly determines RCS performance |
| C2 | Vibration resistance (FOR-010: 40,000 cycles) | 0.25 | Must maintain clamping through 72h of SS 5-6 wave cycling |
| C3 | Field replaceability (MNT-003) | 0.20 | Damaged reflectors must be replaceable without hull return to factory |
| C4 | Assembly simplicity (ASM-004) | 0.15 | Factory pre-assembly of M5; occasional field separation |
| C5 | Galvanic isolation feasibility | 0.10 | HDG steel to AlSi10Mg aluminum couple must be managed |

### 5.3 Scoring

| Criterion | Wt | Var A: Bolted | Var B: Clamped | Var C: Pre-welded |
|-----------|-----|---------------|----------------|-------------------|
| C1: Alignment precision | 0.30 | 4 -- dowel pins provide repeatable +-0.05 deg positioning; torqued bolts maintain alignment permanently | 2 -- spring-loaded pins can achieve +-0.3 deg; clamp settling under vibration may drift; no proven track record for trihedral reflectors | 3 -- factory alignment can be precise; but thermal expansion differential (steel vs aluminum, delta_CTE = 11.7 vs 21.5 ppm/K) causes alignment shift of ~0.15 deg over -5 to +55C range |
| C2: Vibration resistance | 0.25 | 4 -- bolted + Nordlock + Nylock + safety wire = quadruple retention; proven in D8 fatigue analysis | 1 -- toggle clamps rely on spring force; springs fatigue and lose preload over 40,000 cycles; no marine-grade clamp data for this application | 4 -- welded joint has no loosening mechanism; maximum vibration resistance (assuming sound weld) |
| C3: Field replaceability | 0.20 | 4 -- unbolt 4x M10, lift off reflector, replace, re-bolt; dowel pins ensure re-alignment; 30 min per reflector | 4 -- release toggles, lift off, replace, re-engage; ~10 min per reflector; fastest option | 0 -- **DISQUALIFIED** -- cannot replace reflector without cutting weld; defeats modular M5 design concept |
| C4: Assembly simplicity | 0.15 | 3 -- requires torque wrench (50 N-m), soft mallet for dowels, safety wire pliers; 4 tools total; 30 min per unit | 3 -- tool-free engagement; but requires custom toggle clamp design + qualification testing; development risk | 2 -- factory weld setup is simple; but requires bimetallic adapter plate (steel-to-aluminum transition); adds complexity and mass |
| C5: Galvanic isolation | 0.10 | 3 -- nylon bushings + HDPE washers + Tef-Gel isolate bolted interface; proven marine solution | 3 -- clamp jaws can include nylon pads; isolation achievable but clamp surface area for isolation is smaller | 1 -- direct weld of dissimilar metals (steel to aluminum) is metallurgically infeasible without explosion-welded transition strip; adds $200+ per joint and 0.5 kg |

### 5.4 Weighted Scores

| Variant | C1 (0.30) | C2 (0.25) | C3 (0.20) | C4 (0.15) | C5 (0.10) | Weighted Sum | Score (%) |
|---------|-----------|-----------|-----------|-----------|-----------|--------------|-----------|
| **A: Bolted** | 1.20 | 1.00 | 0.80 | 0.45 | 0.30 | **3.75** | **93.8%** |
| B: Clamped | 0.60 | 0.25 | 0.80 | 0.45 | 0.30 | 2.40 | **60.0%** |
| C: Pre-welded | 0.90 | 1.00 | 0.00 | 0.30 | 0.10 | 2.30 | **57.5% -- DISQUALIFIED** |

### 5.5 Decision

**Selected: Variant A -- Bolted to mast top plate (93.8%)**

Justification: The bolted interface is the clear winner. It provides the highest alignment precision (dowel-pin repeatability to +-0.05 deg), proven vibration resistance (quadruple retention system verified in D8 fatigue analysis), and full field replaceability. Variant B (clamped) fails vibration resistance -- no commercial marine toggle clamp exists that maintains 15 kg holding force through 40,000 load cycles without spring fatigue. Variant C is disqualified by the inability to replace damaged reflectors in the field and by the metallurgical incompatibility of directly welding steel to aluminum.

---

## 6. Layout Decision Summary Table

| # | Design Decision | Variant A | Variant B | Variant C | **Selected** | Score | TBD Resolved |
|---|----------------|-----------|-----------|-----------|--------------|-------|--------------|
| 1 | Hull construction | 1-piece rotomold (53.8%) | **2-section bolted (85.0%)** | 2-section welded (77.5%) | **B: 2-section bolted** | 85.0% | TBD-007 |
| 2 | Mast configuration | **Free-standing (90.0%)** | Guyed (66.3%) | A-frame (60.0%) | **A: Free-standing** | 90.0% | TBD-011 |
| 3 | Mooring chain | 12mm G30 (DISQ) | 16mm G30 (71.3%) | 12mm G43 (DISQ) | **None -- 19mm G30 confirmed** | N/A | D8 confirmed |
| 4 | Reflector mount | **Bolted (93.8%)** | Clamped (60.0%) | Pre-welded (DISQ) | **A: Bolted** | 93.8% | IF-04 confirmed |

### 6.1 Disqualification Summary

| Decision | Variant | Reason for Disqualification |
|----------|---------|----------------------------|
| 3 | A: 12mm G30 | SWL 2,250 kgf = 49.6% of required 4,536 kgf; structural failure risk |
| 3 | C: 12mm G43 | SWL 3,900 kgf = 85.9% of required; below minimum threshold + poor Vietnamese availability |
| 4 | C: Pre-welded | Cannot replace reflectors in field (field replaceability score = 0); dissimilar metal weld infeasible |

---

## 7. Selected Layout Description

### 7.1 Consolidated Embodiment Configuration

Based on the four variant evaluations above, the final embodiment layout for Concept A "Baseline Optimized" is:

**Hull System (L1):**
- 2-section bolted HDPE hull, each half a 4.0 m semicircular ring pontoon
- Bolted flange joint at hull centerline: 24x M10 SS316 bolts, EPDM gasket, C100x50x5 HDG steel backing channel
- Closed-cell PU foam fill (40 kg/m3, 80% fill factor) in both halves
- Each section transportable on standard flatbed (TRA-002 compliant)
- Field-joinable at staging area in ~2 hours; field-separable for maintenance

**Mast System (L2.5):**
- 8x free-standing cantilever masts, 60 mm OD x 4 mm wall galvanized S235 steel
- 3.0 m above deck; base gusset reinforcement (4x triangular gussets, 6 mm plate)
- Socket-insert connection to deck (IF-03): 62 mm ID socket, M12 locking pin, R-clip
- Bending capacity: 1,466 N-m at 117.5 MPa allowable (77.1% utilization, SF = 2.0)
- Fatigue: PASS at 40,000 cycles (9.7% utilization at FAT 56)
- Field erection: <2 min per mast, tool-free (pliers for R-clip only), 2-person operation

**Mooring System (L0):**
- 19 mm G30 HDG chain for bottom section (SWL 5,800 kgf, 128% of 4,536 kgf requirement)
- 24 mm polyester rode for water column (SWL 4,500 kgf, SF = 3.0)
- Hybrid chain/rode system reduces total mooring weight from 711 kg (all-chain) to 172-232 kg
- 75-100 kg Danforth anchor (sand: 1,500 kgf holding; mud: dual anchor option)
- HDG swivel (5,000 kgf SWL) at fairlead for 360 deg weathervaning

**Reflector Mounting (IF-04):**
- Bolted connection: 4x M10 Grade 8.8 HDG bolts on 90 mm square pattern
- Alignment: 2x dia 8 mm H7/n6 dowel pins on diagonal (+-0.05 deg repeatability)
- Anti-vibration: Nordlock washer pairs + Nylock nuts + 0.8 mm SS safety wire
- Galvanic isolation: nylon bushings + HDPE washers + Tef-Gel anti-seize
- Helicoil inserts (M10 x 1.5D) in AlSi10Mg frame flange
- Factory pre-assembled as M5 unit; field-replaceable in 30 min per reflector

### 7.2 Mass Budget Impact

| Subsystem | D8/A7 Baseline (kg) | E10 Selected (kg) | Delta (kg) | Notes |
|-----------|---------------------|--------------------|------------|-------|
| L1: Hull | 350 | 350 | 0 | 2-section construction same mass as 1-piece |
| L2: Frame | 150 | 150 | 0 | No change |
| L2.5: Masts (8x) | 128 | 132.8 | +4.8 | Gusset plates added (confirmed) |
| L3: Reflectors (8x) | 120 | 120 | 0 | No change |
| L0: Mooring on-hull | 80 | 80 | 0 | No change |
| L5: GPS | 5 | 5 | 0 | No change |
| L1: Hull joint hardware | 0 | 6.2 | +6.2 | 24x M10 bolts + EPDM gasket + backing channel |
| Fasteners, misc | 147 | 136 | -11 | Reclassified: joint hardware moved to L1 |
| **Total** | **980** | **986** | **+6** | **Well within 1,100 kg limit (114 kg margin)** |

### 7.3 Cost Budget Impact

| Item | Baseline | E10 Impact | Revised |
|------|----------|------------|---------|
| Hull fabrication | $8,000 | +$200 (flange fabrication + gasket + backing channel) | $8,200 |
| Mast system | $1,400 | +$50 (gusset welding labor) | $1,450 |
| Mooring kit (medium depth) | $2,500 | No change (19mm G30 was already D8 selection) | $2,500 |
| Reflector mounting hardware | Included in M5 | No change (bolted was already baseline) | Included |
| **Total system** | **$33,400** | **+$250** | **$33,650** |
| **Per-unit target** | **$35,600** | | **$35,600 (margin $1,950)** |

### 7.4 TBD Resolution Summary

| TBD | Description | E10 Resolution | Status |
|-----|-------------|----------------|--------|
| TBD-007 | Hull fabrication method | **2-section bolted** (VDI 2225: 85.0%) | **RESOLVED** |
| TBD-011 | Mast configuration | **Free-standing cantilever with gusset** (VDI 2225: 90.0%) | **RESOLVED** |
| D8 chain | Mooring chain size | **19 mm G30 HDG confirmed** (all lighter options fail SWL) | **RESOLVED** |
| IF-04 | Reflector mount method | **Bolted + dowel-pinned** (VDI 2225: 93.8%) | **RESOLVED** |

---

## 8. Cross-References

### Phase 3 Documents
- [[PRAD_D8_design_structure.md]] -- Structural analysis: mast, frame, mooring, hull (input)
- [[PRAD_A7_architecture_definition.md]] -- System architecture, modules, interfaces (input)
- [[RISM_R1_requirements_identification.md]] -- 74 direct embodiment requirements (input)
- [[RISM_M4_material_analysis.md]] -- Material selection matrices (reference)
- [[PRAD_P5_principles_application.md]] -- Design principles (reference)
- [[PRAD_R6_rules_application.md]] -- Design rules (reference)

### Phase 2 Source Documents
- [[../02_conceptual/concept_selection.md]] -- Concept A selection (81.8%), risk register
- [[../02_conceptual/concept_evaluation.md]] -- VDI 2225 methodology reference

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1)

### Downstream Documents
- Detail design (Phase 4): Production drawings incorporating all E10 decisions
- BOM: Final bill of materials reflecting selected variants

---

*End of Step E10: Variant Evaluation. All four layout decisions resolved by VDI 2225 weighted scoring. The embodiment layout is now fully defined for Concept A "Baseline Optimized." Total mass: 986 kg (114 kg margin). Total cost: $33,650 ($1,950 margin to $35.6K target).*
