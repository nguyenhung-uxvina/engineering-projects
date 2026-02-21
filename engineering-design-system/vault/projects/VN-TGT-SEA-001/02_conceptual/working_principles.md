---
project: VN-TGT-SEA-001
phase: 2
type: working_principles
version: 1.0
created: 2026-02-10
status: draft
step: 3 of 6
---

# Step 3: Working Principles Search — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Systematically identify working principles for each sub-function from physical effects, solution catalogs, competitor analysis, and creative exploration.
**Method:** Multi-source principle search per Pahl & Beitz
**Input:** [[function_structure.md]] — 7 sub-functions with E/M/S flows

---

## 1. Search Sources

| Source | What It Provides | Applied To |
|--------|-----------------|------------|
| **Physical effects catalog** | Fundamental physics (buoyancy, reflection, catenary) | F1, F2, F3 |
| **Solution catalogs** | Proven mechanisms (anchors, reflectors, hulls) | All functions |
| **Literature/patents** | Published marine engineering, radar target design | F1, F2, F3 |
| **Competitor analysis** | Existing products (SINKEX, Hammerhead, HSMST, L-CATT) | All functions |
| **Biomimicry** | Nature-inspired (limited applicability for this product) | F1 (kelp anchoring) |
| **Vietnamese context** | Local materials, suppliers, capabilities | F1, F4, F6 |

---

## 2. Working Principles per Sub-Function

### 2.1 F1: Float Stably at Sea Surface

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P1.1** | **Solid circular pontoon (HDPE + foam)** | Archimedes buoyancy; high waterplane area (A_wp = πD²/4) gives extreme GM | **9** | **LOW** | Simple, unsinkable (foam-filled), rotomoldable, self-righting, very high GM (210+ m for 8m), low draft | Large footprint, high tow drag, may need 2-section for transport | Navigation buoys, ODAS buoys, small craft pontoons |
| P1.2 | Inflatable ring hull | Pneumatic buoyancy; fabric/rubber toroid with air chambers | 8 | LOW | Compact storage (deflated), lightweight (<200 kg), rapid inflate, cheap | Puncture/abrasion risk in SS 5-6, UV degradation, limited payload, short lifespan (2-3 years) | Inflatable decoys (Barracuda), liferafts |
| P1.3 | Catamaran (twin hull) | Distributed waterplane; two narrow hulls + cross-deck | 9 | MED | Good stability (wide beam), large deck area, lower drag than mono | Complex structure, wider transport, asymmetric loads, hull-crossdeck fatigue | USV hulls (CUSV), work platforms |
| P1.4 | Spar buoy (vertical cylinder) | Deep ballast, minimal waterplane → low motion response | 8 | MED-HIGH | Excellent heavy-weather (minimal heave/pitch), natural weathervaning, proven offshore | Heavy (2,000-3,000 kg), difficult tow (upending), complex deployment, limited reflector space on top | Oceanographic NDBC buoys, oil platform spars |
| P1.5 | Steel barge (flat-bottom) | Displacement hull; flat plate construction | 9 | MED | Simple, robust, proven, high payload capacity | Heavy, corrosion-prone, poor stability in SS 5-6, no foam fill safety, low freeboard | Target barges (ad-hoc VN Navy) |
| P1.6 | Trimaran (3 hulls) | Tri-hull waterplane distribution | 8 | HIGH | Very stable, large platform area, good seakeeping | Complex structure, expensive, transport difficulty | ACTUV (Seahunter) USV |

**Selection rationale:** P1.1 dominates on cost, simplicity, TRL, and local content. P1.4 (spar) has best heavy-weather performance but fails on deployment, cost, and weight. P1.2 (inflatable) cannot survive SS 5-6. P1.3 (catamaran) is viable but more complex and expensive.

---

### 2.2 F2: Hold Position at Designated Location

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P2.1** | **Single-point mooring (anchor + catenary chain/rode)** | Gravity catenary absorbs shock; anchor friction/suction holds seabed; SPM allows weathervane | **9** | **LOW** | Simple, proven, allows 360° weathervaning (reduces loads), pre-deployable, depth-adjustable | Swing circle (±70-240m), anchor drag risk, depth-dependent sizing | ODAS buoys, navigation buoys, mine countermeasure buoys |
| P2.2 | Multi-point mooring (3-4 anchors) | Multiple restraint lines converge on platform | 9 | MED-HIGH | Tight position hold (±10-20m), predictable orientation | Complex deploy (3-4 anchors), no weathervaning = asymmetric storm loads, 3-4× mooring hardware | Floating docks, fish farms, offshore platforms |
| P2.3 | Dynamic positioning (thrusters + GPS) | Active thrust counteracts drift; closed-loop GPS control | 7 | VERY HIGH | Precise position (±1m), any depth, no anchor | Power system ($30K+), not passive, C2 link required, electronics vulnerability in SS 5-6 | USVs (Hammerhead), survey vessels |
| P2.4 | Deadweight anchor (concrete block) | Gravity holding only (no flukes) | 9 | VERY LOW | Simplest, cheapest, no anchor setting needed | Poor holding in storm (weight only, no mechanical advantage), heavy to deploy | Mooring buoys (sheltered harbors) |
| P2.5 | Drag anchor + kellet | Anchor + midline weight (kellet) improves catenary angle | 9 | LOW | Better anchor holding efficiency, reduces chain scope | Additional hardware, slightly more complex deployment | Traditional mooring practice |

**Selection rationale:** P2.1 is the clear winner. SPM + weathervaning is essential for storm survival — asymmetric loads from P2.2 are dangerous in SS 6. P2.3 violates the passive operation requirement. P2.4 inadequate for SS 5-6 holding. P2.5 is a refinement of P2.1 for Phase 3.

---

### 2.3 F3: Generate Controlled Radar Signature

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P3.1** | **Trihedral corner reflector (passive, retroreflective)** | 3-bounce retroreflection returns radar energy to source; sigma = 12πa⁴/λ² | **9** | **MED** | Broadband, predictable RCS (well-characterized physics), passive, proven, scalable (a⁴), ±15° beamwidth per face, no power | Size-dependent (0.8m edge for >150 m² each), weight (15 kg/reflector hybrid), orthogonality critical (±0.1°) | Navigation reflectors (IALA), military radar augmentors, satellite calibration |
| P3.2 | Luneburg lens reflector | Graded dielectric index sphere focuses and returns radar; wide-angle (±60° per lens) | 7 | HIGH | Very wide angle coverage (fewer needed), compact for RCS, frequency-independent | Expensive ($5-10K each), heavy (solid dielectric sphere), moisture-sensitive, fragile, limited manufacturers | Military radar augmentor (Mil-spec Luneburg), satellite tracking |
| P3.3 | Active radar transponder/augmentor | Electronic receive → amplify → retransmit at X-band | 8 | VERY HIGH | Any RCS level (programmable), compact, frequency-selective | NOT passive, battery required, EMC issues during missile engagement, "fake" RCS (wrong Doppler/glint signature), military acceptance questionable | Shipboard RCS augmentors, radar test targets |
| P3.4 | Flat plate reflector array | Specular reflection (single-bounce) normal to plate surface | 9 | LOW | Simple, cheap, lightweight | Very narrow beamwidth (~2-3° per plate), impossible to achieve 360° with practical number of plates | Radar calibration targets (fixed) |
| P3.5 | Dihedral corner reflector | 2-bounce reflection in one plane; narrower than trihedral | 9 | LOW | Simpler than trihedral, lighter | Only reflects in one plane (2D, not 3D), needs many more for 360° coverage, lower RCS per unit | Chaff, simple radar reflectors |
| P3.6 | Wire mesh/array reflector | Conducting mesh approximates solid reflector at fraction of weight | 8 | LOW | Lightweight, low wind resistance, cheap | Mesh spacing must be < λ/10 (3.2mm at X-band) = fine mesh = fragile; corrosion at joints; RCS slightly lower than solid | Navigation reflectors (mesh type) |

**Selection rationale:** P3.1 is the established solution with well-characterized physics. At 0.8m edge with 8 reflectors, it achieves >1,000 m² RCS. The hybrid AM/CNC manufacturing approach solves the orthogonality challenge (±0.1°) while keeping cost manageable. P3.2 (Luneburg) has wider angular coverage but is 5-10× more expensive and fragile. P3.3 (active) violates the passive requirement and creates EMC concerns during actual missile engagement. P3.6 (mesh) is interesting as a cost/weight optimization to explore in Phase 3.

---

### 2.4 F4: Support Signature Elements Above Water

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P4.1** | **Fixed cantilever mast in deck socket** | Cantilever beam; bending moment = F × L at base; steel tube resists via section modulus | **9** | **LOW** | Simple, field-erectable (socket insert), no additional rigging, proven, local fabrication (galv steel tube) | All bending at base (fatigue critical), windage, limited height without large section | Navigation buoy masts, antenna masts, marine equipment |
| P4.2 | Guyed mast (mast + cable stays) | Tensioned cable stays share bending load; mast primarily in compression | 9 | LOW | Higher capacity for given mast weight, can go taller, reduces base moment by 60-80% | More parts (cables, turnbuckles, deck padeyes), longer erection time, deck clutter for mooring ops | Radio masts, marine antenna installations |
| P4.3 | A-frame / tripod | Three legs distribute load; stable triangle geometry | 9 | MED | Very stable, high capacity, inherently stiff, good fatigue | Heavy, takes more deck area, complex field erection, more material | Survey equipment supports, derrick frames |
| P4.4 | Deck-mounted pedestal (low, <1m) | Short cantilever; very low bending moment | 9 | VERY LOW | Simple, minimal windage, robust, trivial to install | Low height → sea clutter interference at SS 3+, reduced radar horizon, green water exposure of reflectors | Existing ad-hoc target buoys |
| P4.5 | Tensioned cable system (catenary mast) | Cables between hull perimeter posts; reflectors hang from cables | 6 | LOW | Low windage, light | Unproven concept, reflector alignment unstable in waves, complex rigging | No known defense application |
| P4.6 | Inflatable column | Pneumatic tubular mast | 7 | LOW | Lightweight, compact when deflated | Puncture risk, limited stiffness, flutter in wind, unproven for this application | Inflatable antenna masts (temporary) |

**Selection rationale:** P4.1 (fixed mast in socket) is the simplest, lowest-cost, and most field-friendly. For 3m height with 15 kg reflector + Bft 7 gust, a 60mm×4mm galvanized steel tube provides 18% margin on bending (allowable 1,303 N·m vs required 1,100 N·m). P4.2 (guyed) is the fallback if Phase 3 analysis shows P4.1 is marginal. P4.4 (pedestal) was the original v1.0 design but was rejected in Rev B.1 due to sea clutter interference at low heights.

---

### 2.5 F5: Report Position to Shore

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P5.1** | **GPS beacon with satellite relay** | GNSS position fix + Iridium/GlobalStar data relay to shore | **9** | **MED** ($1,500-2,000) | Global coverage, ±5m accuracy, proven, 1 Hz update, works anywhere | Battery life (72h needs Li-ion pack), monthly satellite service cost, submersion vulnerability | EPIRB, PLB, maritime tracking, NDBC buoys |
| P5.2 | AIS transponder (Class B) | VHF radio broadcast of MMSI + position on marine AIS frequencies | 9 | LOW ($300-500) | Standard marine equipment, all ships can see it, low cost, low power | Line-of-sight only (~20 nm to shore), may interfere with test range operations, visible to all vessels | Standard vessel tracking |
| P5.3 | Radar transponder (RACON) | Receives radar pulse, retransmits coded response | 8 | MED ($1,000-2,000) | Visible on any radar display, identifies target on range radar | May interfere with missile seeker acquisition (active radar response), power required, confusion risk during test | Navigation RAMARKs, lighthouse augmentors |
| P5.4 | Iridium satellite tracker | Iridium modem transmits GPS position at interval | 9 | MED ($500 unit + $20/month) | Reliable global coverage, compact, long battery (months at low update rate) | Lower update rate (typically 5-15 min, not 1 Hz), monthly cost | Asset tracking, fleet management |
| P5.5 | VHF radio beacon | Transmits on dedicated frequency for RDF | 8 | LOW ($200-400) | Simple, cheap, long battery life | Requires RDF equipment at shore, lower accuracy (±1-5°), line-of-sight | Traditional marine navigation |

**Selection rationale:** P5.1 (GPS beacon with satellite relay) is the only option that provides ±5m, 1 Hz, global, 72h coverage — all required by SIG-007, SIG-008, ENR-001. P5.2 (AIS) is interesting as a secondary/backup system (low cost). P5.3 (RACON) is rejected due to potential interference with the missile seeker.

---

### 2.6 F6: Enable Deployment and Recovery

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P6.1** | **Surface tow by tug (bridle + drogue)** | Drag resistance overcome by tug; bridle distributes load; drogue stabilizes yaw | **9** | **LOW** | Simple, any tug/workboat, proven, no specialized equipment, works in SS 4-5 | Weather-limited, tow drag high for flat pontoon, yaw instability (drogue mitigates), slow (3-5 kn) | Target towing (L-CATT, QST-35), barge towing |
| P6.2 | Self-propelled (outboard/electric motor) | Motor thrust for transit | 8 | MED ($5-10K for motor + batteries) | Independent of tug, faster positioning, more maneuverable | Not passive during transit, adds cost/weight/complexity, motor lost when target destroyed | USV targets (Hammerhead, HSMST) |
| P6.3 | Helicopter sling load | Aerodynamic lift + cable sling | 8 | HIGH ($10-20K per deployment) | Fast, all-weather, precise placement | Weight limit (~2,000 kg — OK for 980 kg), very expensive per deployment, requires helicopter availability | Military supply operations, buoy deployment |
| P6.4 | Ship crane/davit launch | Mechanical lift from ship deck | 9 | MED (requires crane-equipped vessel) | Controlled deployment, can launch in moderate seas, assembly possible on ship deck | Requires specific vessel capability, limits deployment flexibility | Oceanographic buoy deployment, NDBC |

**Selection rationale:** P6.1 (surface tow) is simplest and cheapest. Pre-deployed mooring concept means the tug only needs to tow the target to the mooring buoy and connect — reducing the weather window requirement. P6.2 (self-propelled) adds cost and complexity for an expendable target. P6.3 (helicopter) is too expensive for routine use. P6.4 (ship crane) is viable but limits operational flexibility.

---

### 2.7 F7: Withstand Environmental Loads

| ID | Working Principle | Physical Effect | TRL | Rel. Cost | Advantages | Disadvantages | Defense Examples |
|----|-------------------|----------------|-----|-----------|------------|---------------|-----------------|
| **P7.1** | **Robust over-design (safety factors on all components)** | Conservative structural design; 3:1 SWL on mooring, adequate section for masts, marine-grade materials | **9** | **LOW-MED** | Simple, proven approach, inspectable, maintainable | Adds weight, may be conservative in some areas | Standard marine engineering practice |
| P7.2 | Breakaway/sacrificial design | Designed weak points yield before critical failure; protects core structure by shedding non-essential components | 8 | LOW | Lightweight (less over-design), predictable failure modes | Loss of components (reflectors, masts) in extreme conditions = mission failure | Frangible antenna mounts, breakaway couplings |
| P7.3 | Submersible (dive below waves) | Target submerges below wave zone in extreme conditions; resurfaces when calm | 6 | HIGH | Eliminates all wave/wind loads during storm | Extremely complex, requires ballast control, electronics must be pressure-rated, may lose position | Submarine-launched targets |
| P7.4 | Wave-conforming flexible structure | Flexible hull follows wave surface rather than resisting it | 7 | MED | Reduces structural loads, lightweight | Flexible = RCS instability (reflector alignment shifts), fatigue at flex points, unproven concept | Flexible wave energy converters |

**Selection rationale:** P7.1 (robust over-design) is the appropriate approach for an expendable military target. 3:1 safety factors on mooring, adequate mast sections, and marine-grade materials provide reliable performance. P7.2 (breakaway) is interesting for the masts (Phase 3 could design mast/reflector as sacrificial in extreme conditions beyond SS 6) but core structure must be robust.

---

## 3. Principle Selection Summary

| Sub-Function | **Selected Primary** | **Selected Secondary / Fallback** | Eliminated |
|--------------|---------------------|-----------------------------------|------------|
| F1: Float | **P1.1 HDPE circular pontoon** | P1.3 Catamaran (if stability insufficient) | P1.2 (SS 5-6 risk), P1.4 (deploy), P1.5 (corrosion) |
| F2: Hold position | **P2.1 Single-point mooring** | P2.5 SPM + kellet (optimization) | P2.2 (no weathervane), P2.3 (not passive), P2.4 (weak) |
| F3: Generate RCS | **P3.1 Corner reflectors** | P3.6 Mesh reflectors (weight/cost opt.) | P3.2 (cost), P3.3 (not passive), P3.4 (narrow beam), P3.5 (2D only) |
| F4: Support | **P4.1 Fixed mast in socket** | P4.2 Guyed mast (if base moment marginal) | P4.3 (heavy), P4.4 (low height), P4.5 (unproven), P4.6 (puncture) |
| F5: Position | **P5.1 GPS beacon** | P5.2 AIS (secondary/backup) | P5.3 (seeker interference), P5.5 (low accuracy) |
| F6: Deploy | **P6.1 Surface tow** | P6.4 Ship crane (alternative) | P6.2 (cost for expendable), P6.3 (expensive) |
| F7: Withstand | **P7.1 Robust over-design** | P7.2 Breakaway masts (Phase 3 option) | P7.3 (complexity), P7.4 (RCS instability) |

---

## 4. Compatibility Assessment

Before combining into concepts (Step 4), check that selected principles are physically compatible:

| Combination | Compatible? | Notes |
|-------------|-------------|-------|
| P1.1 (HDPE pontoon) + P2.1 (SPM) | **YES** | Standard practice. Central pad eye. Proven. |
| P1.1 + P3.1 (corner reflectors) | **YES** | Reflectors at perimeter. Weight (120 kg) easily accommodated. |
| P1.1 + P4.1 (fixed mast) | **YES** | Deck sockets welded to steel frame on HDPE hull. Standard interface. |
| P3.1 + P4.1 | **YES** | Reflector bolted to mast top plate. Alignment via AM pins. |
| P2.1 + P4.1 | **YES** | SPM allows weathervaning; masts see equal loading from all directions. |
| P5.1 (GPS) + P4.1 (mast) | **YES** | GPS beacon on tallest mast or dedicated mast (≥4.5m AGL). |
| P6.1 (tow) + P1.1 | **YES** | Bridle attachment points on hull. Drogue for stability. High tow drag for 8.0m pontoon but acceptable at 3-5 kn. |
| P7.1 (robust) + all | **YES** | Over-design approach applies to all components. |

**Result: All primary selections are mutually compatible.** No interface conflicts detected. Proceed to morphological matrix (Step 4) for concept generation.

---

## Cross-References

- [[function_structure.md]] — Step 2: Function structure (input)
- [[morphological_matrix.md]] — Step 4: Concept generation (next)
- [[concept_evaluation.md]] — Step 5: VDI 2225 evaluation
- [[concept_selection.md]] — Step 6: Selection decision
- [[../00_odi/re_deep_analysis.md]] — Reflector physics, mooring analysis
- [[../00_odi/re_competitive_analysis.md]] — Competitor solutions
- [[../00_odi/environmental_survivability.md]] — Environmental loading analysis
