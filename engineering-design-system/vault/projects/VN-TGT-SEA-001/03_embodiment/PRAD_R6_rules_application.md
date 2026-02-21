---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "R6 — Rules Application"
group: PRAD
version: 1.0
created: 2026-02-10
status: draft
---

# Step R6: Rules Application — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Apply the 4 Pahl & Beitz Basic Rules of Embodiment Design (Clarity, Simplicity, Safety, Economy) to all 7 subsystems of Concept A. Identify compliance gaps, simplification opportunities, failure mode mitigations, and cost efficiency improvements.
**Method:** Pahl & Beitz PRAD Step R6 — Systematic evaluation of each subsystem against the 4 basic rules, producing a 28-cell compliance matrix, part count analysis, failure mode summary, and cost efficiency assessment.
**Input:** [[RISM_R1_requirements_identification.md]] (74 direct embodiment requirements), [[RISM_I2_critical_requirements.md]] (55 hard constraints, 8 conflicts), [[../02_conceptual/concept_selection.md]] (Concept A architecture, risk register)
**Selected Concept:** Concept A "Baseline Optimized" (VDI 2225: 81.8%)

---

## 1. The Four Basic Rules of Embodiment Design

Per Pahl & Beitz (VDI 2221), every embodiment decision must satisfy four fundamental principles. These rules are applied before any detail dimensioning begins and serve as a design quality filter.

| Rule | German | Vietnamese | Core Principle |
|------|--------|------------|----------------|
| **Rule 1: CLARITY** | Eindeutigkeit | Ro rang | Every function must be clear and unambiguous. Load paths must be easy to trace. No "hidden failures" allowed. |
| **Rule 2: SIMPLICITY** | Einfachheit | Don gian | Minimum number of parts and features. Fewer interfaces = fewer failure modes. DfA principle applied. |
| **Rule 3: SAFETY** | Sicherheit | An toan | Fail-safe design: failure goes to safe state. Redundancy for critical functions. Clear failure indication. Safety hierarchy: safe-life > fail-safe > redundant. |
| **Rule 4: ECONOMY** | Wirtschaftlichkeit | Kinh te | Right material for function (not overkill). Full lifecycle cost considered. Manufacturing method appropriate to production volume (10-100 units/year). |

---

## 2. Rule 1: CLARITY (Ro rang)

### 2.1 Clarity Assessment by Subsystem

For each subsystem: Is the function clear? Can loads be traced from origin to ground? Are there any hidden failure modes?

#### L0: Storm Mooring System

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Single function: restrain platform at anchor point against environmental loads (wind + wave + current). No ambiguity. |
| **Load path traceable?** | YES | Environmental forces on hull/masts -> steel frame -> central pad eye -> G30 chain -> rode -> anchor -> seabed. Every link in the load path is a discrete, inspectable component. |
| **Hidden failures?** | ONE IDENTIFIED | Anchor drag is invisible from the surface. Target can drift off station without obvious visual indication until GPS position diverges. Mitigated by GPS beacon (L5) continuous position reporting. |

#### L1: HDPE Hull Platform

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Two functions: (1) provide buoyancy (Archimedes force at waterplane area 50.3 m^2), (2) provide mounting surface for frame, masts, and equipment. Clearly separated: HDPE shell = buoyancy, steel frame = structural. |
| **Load path traceable?** | YES | Buoyancy force acts uniformly across hull bottom. Concentrated loads (mooring, masts) transfer through steel frame (L2), NOT through HDPE hull. Hull is buoyancy envelope only. |
| **Hidden failures?** | ONE IDENTIFIED | Hull breach below waterline is not visible. Mitigated by closed-cell foam fill (MAT-002): even with hull breach, foam provides >96% reserve buoyancy. Hull cannot sink. |

#### L2: Steel Structural Frame

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Distribute concentrated loads (mooring pad eye, 8 mast sockets, 2 tow bridle points) across HDPE hull area. Frame is structural backbone; hull is flotation shell. Clear separation of concerns. |
| **Load path traceable?** | YES | Pad eye (1,512 kgf peak) -> frame radial members -> perimeter ring -> distributed bolts/welds to hull. Mast sockets (1,100 N-m each) -> socket weld to frame -> distributed to hull. |
| **Hidden failures?** | NONE | All welds and bolts are accessible for inspection. No concealed structural joints. HDG coating provides visual corrosion indicator (rust spots visible on galvanized surface). |

#### L2.5: Mast System (8 units)

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Single function: elevate corner reflector to 3.0-4.0 m AWL while resisting wind and wave bending loads. One mast per reflector, identical design, socket-insert interface. |
| **Load path traceable?** | YES | Wind/wave on reflector -> mast tube (bending) -> mast base flange -> deck socket (welded to L2 frame) -> frame -> hull. Cantilever beam model, analytically straightforward. |
| **Hidden failures?** | ONE IDENTIFIED | Fatigue crack initiation at mast-socket weld toe. Crack grows internally and is invisible until mast failure. Mitigated by: (a) conservative fatigue category selection, (b) visual inspection at weld toe before each deployment, (c) defined mast service life (40,000 cycles = ~56 deployments at 72h each in SS 5-6). |

#### L3: Hybrid Corner Reflectors (8 units)

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Single function: retroreflect incident radar energy. Three mutually orthogonal face plates produce 3-bounce reflection. sigma = 12*pi*a^4/lambda^2 = 152.3 m^2 per reflector. Physics is deterministic. |
| **Load path traceable?** | YES | Wind on face plates -> AM frame (carries face plate weight + wind pressure) -> 4-bolt mount + 2 dowel pins -> mast top plate. All mechanical, no hidden load sharing. |
| **Hidden failures?** | ONE IDENTIFIED | Orthogonality degradation from creep or thermal cycling. If face plate angles drift beyond +/-0.3 deg, individual RCS drops below 120 m^2. Mitigated by: (a) AM frame provides rigid geometry constraint, (b) alignment dowel pins prevent bolt-hole slop, (c) AlSi10Mg has negligible creep at service temperatures (-5 to +55 deg C). |

#### L5: GPS Beacon System

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Single function: report platform GPS position via satellite link at 1 Hz for 72h. COTS unit, commercially specified. |
| **Load path traceable?** | N/A | No structural load path; beacon is mounted via bracket/clamp at mast top. Mass ~5 kg, negligible structural impact. |
| **Hidden failures?** | ONE IDENTIFIED | Battery depletion is invisible externally. No low-battery visual indicator visible from standoff distance. Mitigated by: (a) satellite data link reports battery voltage, (b) 72h battery sized with 10% margin (actual ~80h capacity). |

#### L6: Tow/Deployment System

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Function clear?** | YES | Two functions: (1) tow platform from tender to deployment site, (2) stabilize yaw during tow via trailing drogue. Both are standard marine operations. |
| **Load path traceable?** | YES | Tow vessel -> Dyneema tow line -> shackle -> bridle legs -> 2 pad eyes on hull/frame -> frame -> hull. Drogue on separate pendant astern. |
| **Hidden failures?** | NONE | All tow hardware is visible and inspectable. Dyneema has no hidden fatigue signature (unlike wire rope which develops internal broken wires). Shackle pins are visually inspected before each tow. |

### 2.2 Clarity Summary

| Subsystem | Function Clear | Load Path Traceable | Hidden Failures | Clarity Status |
|-----------|---------------|--------------------|-----------------| --------------|
| L0: Mooring | YES | YES | 1 (anchor drag) | **PASS** |
| L1: Hull | YES | YES | 1 (hull breach) | **PASS** |
| L2: Frame | YES | YES | 0 | **PASS** |
| L2.5: Masts | YES | YES | 1 (fatigue crack) | **PASS** |
| L3: Reflectors | YES | YES | 1 (orthogonality drift) | **PASS** |
| L5: GPS Beacon | YES | N/A | 1 (battery depletion) | **PASS** |
| L6: Tow System | YES | YES | 0 | **PASS** |

**All 7 subsystems PASS Rule 1 (Clarity).** Five hidden failure modes identified; all have documented mitigations. No ambiguous load paths or dual-function confusion.

---

## 3. Rule 2: SIMPLICITY (Don gian)

### 3.1 Simplicity Assessment by Subsystem

For each subsystem: Part count, feature count, interface count. Can any parts be eliminated or combined?

#### L0: Storm Mooring System

- **Part count:** 7 (anchor, chain, rode, swivel, 2 shackles, pad eye connection)
- **Feature count:** Low — all COTS hardware, no custom machining
- **Interfaces:** 6 mechanical connections (anchor-chain, chain-swivel, swivel-rode, rode-shackle, shackle-pad eye, pad eye-frame)
- **Simplification:** NONE feasible. Every component serves a distinct function in the catenary load chain. Removing the swivel eliminates 360 deg weathervaning (KIN-003 failure). Removing the rode eliminates catenary shock absorption.

#### L1: HDPE Hull Platform

- **Part count:** 3 (hull shell, closed-cell foam fill, hull section joint if 2-piece)
- **Feature count:** Low — no penetrations below waterline; scuppers at deck edge
- **Interfaces:** 1 major (hull-to-frame bolt/weld), 1 conditional (hull section joint IF-07)
- **Simplification:** POSSIBLE — 1-piece hull eliminates IF-07 joint (saves ~15 kg in flanges, ~$400 in hardware). Requires oversize transport permit (TRA-002 trade-off). Decision at TBD-007.

#### L2: Steel Structural Frame

- **Part count:** ~12 (central hub plate, 4 radial members, perimeter ring, 8 socket flanges, pad eye assembly)
- **Feature count:** Medium — welded fabrication, bolt holes for hull attachment
- **Interfaces:** 3 (frame-to-hull, frame-to-pad eye, frame-to-mast sockets)
- **Simplification:** POSSIBLE — Integrate pad eye into central hub plate rather than separate pad eye + backing plate. Saves 1 part, 4 through-bolts. Requires hub plate thickness increase from 10 mm to 16 mm but eliminates a bolted interface.

#### L2.5: Mast System (8 units)

- **Part count per mast:** 4 (tube, base flange/plate, top plate, locking pin)
- **Total mast system:** 32 parts + 8 safety wire assemblies = ~40
- **Feature count:** Low per mast — welded tube-to-flange, drilled bolt holes on top plate
- **Interfaces:** 2 per mast (socket-insert at bottom, reflector mount at top)
- **Simplification:** POSSIBLE — Top plate can be welded to tube permanently (currently assumed), reducing field assembly to socket-insert + locking pin only. Already simplified by pre-assembly at factory.

#### L3: Hybrid Corner Reflectors (8 units)

- **Part count per reflector:** 8 (3 face plates, 1 AM frame, 2 alignment dowel pins, 4 mounting bolts with Nylock nuts — counted as 4 bolt assemblies)
- **Total reflector system:** 64 parts (8 x 8) + 8 safety wire sets = ~72
- **Feature count:** HIGH — CNC fly-cut faces (flatness <0.1 mm, Ra <=10 um), AM frame with precision alignment features, anodized surfaces
- **Interfaces:** 2 per reflector (face plate-to-frame 3x, reflector-to-mast 4-bolt mount)
- **Simplification:** LIMITED — Face plates cannot be combined (3 orthogonal planes). AM frame is already a single-piece structure replacing what would otherwise be 6-8 machined brackets. AM consolidation saves ~50% of parts vs CNC-only bracket assembly. Bolt count (4 per reflector-to-mast) is minimum for alignment stability.

#### L5: GPS Beacon System

- **Part count:** 4 (GNSS/Iridium module, Li-ion battery pack, IP67 enclosure, mast clamp bracket)
- **Feature count:** Low — COTS components, single cable connection
- **Interfaces:** 1 (clamp to mast)
- **Simplification:** NONE feasible. Already minimized as a COTS unit. Combining battery and module into a single enclosure is a supplier design decision.

#### L6: Tow/Deployment System

- **Part count:** 7 (tow line, 2 bridle legs, 2 bridle shackles, drogue, drogue pendant)
- **Feature count:** Low — COTS rope and hardware
- **Interfaces:** 3 (tow line-to-bridle, bridle-to-hull pad eyes, drogue-to-hull)
- **Simplification:** POSSIBLE — Single-point tow (eliminate bridle) acceptable at reduced speed per I2 (KIN-005 is soft constraint). Saves 3 parts. Trade-off: reduced yaw stability during tow. Recommended: keep 2-point bridle for operational reliability but note single-point as fallback.

### 3.2 Part Count Analysis

| Subsystem | Current Parts | Can Reduce? | Target | Method |
|-----------|---------------|-------------|--------|--------|
| L0: Mooring | 7 | NO | 7 | All components serve distinct chain-link functions |
| L1: Hull | 3 (2-section) | YES | 2 (1-piece) | Eliminate section joint IF-07; requires oversize transport |
| L2: Frame | ~12 | YES | ~10 | Integrate pad eye into hub plate; eliminate backing plate + 4 bolts |
| L2.5: Masts (total) | ~40 | MINOR | ~36 | Pre-weld top plates at factory (eliminates field bolt-up of 4 top plates for non-reflector-carrying mast variants) |
| L3: Reflectors (total) | ~72 | NO | ~72 | AM frame already consolidates ~50% of bracket parts vs CNC-only |
| L5: GPS Beacon | 4 | NO | 4 | Already COTS minimum |
| L6: Tow System | 7 | YES | 4 | Single-point tow fallback eliminates bridle (3 parts) |
| **TOTAL** | **~145** | — | **~135** | **~7% reduction feasible** |

**Simplicity verdict:** The design is already reasonably simple. The AM frame in L3 is a significant part-count consolidation. The main simplification opportunities are in L1 (1-piece hull) and L2 (integrated pad eye). Total system part count ~145 is acceptable for a 980 kg marine system.

---

## 4. Rule 3: SAFETY (An toan)

### 4.1 Safety Hierarchy

Per Pahl & Beitz, safety is achieved through a hierarchy of approaches (most preferred to least):

1. **Safe-life:** Component designed to survive full service life without failure (no inspection needed)
2. **Fail-safe:** If component fails, system goes to a safe state (no catastrophic consequence)
3. **Redundant:** Multiple components share function; one can fail without system failure

### 4.2 Safety Assessment by Subsystem

#### L0: Storm Mooring System

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Chain link fracture | CRITICAL — target drifts off station | FAIL-SAFE: GPS beacon continues transmitting position, HDPE hull remains afloat, non-hazardous drift (SAF-003) | GPS position divergence from anchor point detected by monitoring vessel/shore station | Chain sized at 3:1 SWL (FOR-006: 4,536 kgf vs 1,512 kgf peak). **Safe-life** approach: chain designed to never fail in service. |
| Anchor drag | HIGH — target drifts slowly | FAIL-SAFE: Same as chain fracture. Slow drift allows recovery. | GPS position creep; drift rate ~0.5-2 kn depending on conditions | Anchor holding >=1,500 kgf (FOR-007); proper setting protocol; pre-deployment verification pull test at 2x working load |
| Swivel seizure | MEDIUM — asymmetric mooring load | PARTIAL FAIL-SAFE: Platform cannot weathervane; mooring loads increase on one side; risk of chain overload in beam seas | Not detectable from standoff; requires close inspection | Swivel rated at 2x chain SWL; stainless steel bearing surfaces; annual replacement schedule |
| Pad eye weld failure | CRITICAL — total mooring loss | FAIL-SAFE: Same as chain fracture (drift + GPS tracking) | Post-failure only; weld is inspected pre-deployment | Through-bolted with 200x200x10 mm backing plate (ASM-005); weld sized at 3:1 on peak load; visual weld inspection (NDE on first article) |

**Safety approach:** Safe-life design (3:1 SWL throughout chain) with fail-safe backup (GPS tracking enables recovery after mooring failure).

#### L1: HDPE Hull Platform

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Hull breach (impact/fatigue) | HIGH — water ingress | FAIL-SAFE: Closed-cell foam fill provides >96% reserve buoyancy (MAT-002). Hull CANNOT sink. | Increased draft visible; waterlogged compartment detectable during recovery | Foam fill is the primary safety feature. HDPE is impact-resistant (no brittle fracture). |
| Hull section joint failure (IF-07) | MEDIUM — localized flooding of one section | FAIL-SAFE: Each section independently foam-filled. Even complete joint separation does not cause sinking. | Visible separation at joint; halves remain connected by frame | Bolted flange with gasket seal; frame (L2) structurally connects both halves |
| Capsize | CATASTROPHIC — total loss | CANNOT OCCUR: BM = 210.3 m, GM >> 0 at all conditions. Physics-guaranteed stable (SAF-007). | N/A | GM = 210+ m is inherent in 8.0 m diameter, 0.5 m depth, low CG geometry |

**Safety approach:** Fail-safe design through foam fill (unsinkable) and inherent stability (uncapsizable). No single failure mode leads to platform loss.

#### L2: Steel Structural Frame

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Frame member buckling | MEDIUM — local deformation | FAIL-SAFE: Load redistributes to adjacent members; platform remains afloat | Visible deformation at member | Frame sized conservatively (S235 at <=60% yield utilization) |
| Corrosion of HDG coating | LOW (short-term) — progressive degradation | SAFE-LIFE: HDG provides >=85 um zinc coating (ASTM A123); corrosion rate ~2 um/year in splash zone = 40+ year protective life | Visible rust spots on zinc surface indicate coating breakdown | HDG spec enforced at fabrication; touch-up zinc spray for field damage |
| Weld failure at mast socket | HIGH — loss of one mast/reflector | FAIL-SAFE: Loss of 1 of 8 reflectors degrades RCS by ~12.5% but system remains functional (7 reflectors still provide ~900 m^2 > 700 m^2 minimum SIG-003) | Mast tilting or falling visible | Socket welds inspected pre-deployment; fatigue life analysis per FOR-010 |

**Safety approach:** Safe-life (conservative sizing + HDG corrosion protection) with fail-safe redundancy (8 mast sockets — loss of one does not fail the system).

#### L2.5: Mast System (8 units)

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Mast tube fracture (fatigue) | HIGH — reflector falls to deck | FAIL-SAFE: Reflector lands on deck (not overboard); 7 remaining reflectors provide ~900 m^2 RCS. Safety wire prevents reflector from launching. | Mast visibly bent/broken; reflector on deck | Fatigue design to 40,000 cycles (FOR-010); 18% bending margin; visual weld inspection pre-deployment |
| Locking pin failure | MEDIUM — mast ejects from socket | FAIL-SAFE: Safety wire (SAF-006) retains mast in socket even if pin shears. Mast may tilt but does not separate. | Mast tilting/rattling in socket | Redundant retention: primary locking pin + secondary safety wire; both must fail for mast ejection |
| Mast-reflector bolt failure | MEDIUM — reflector detaches | FAIL-SAFE: Safety wire on bolt group prevents complete separation; reflector hangs from wire but does not fall. 7 remaining reflectors provide adequate RCS. | Reflector tilting on mast | 4-bolt Nylock pattern + 2 dowel pins + safety wire (ASM-004, SAF-006); triple redundant retention |

**Safety approach:** Redundant retention (pin + wire at socket; bolts + pins + wire at reflector). 8-unit array provides functional redundancy (N-1 still meets SIG-003 minimum RCS).

#### L3: Hybrid Corner Reflectors (8 units)

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Face plate delamination from frame | HIGH — individual RCS drops to near zero | FAIL-SAFE: 7 remaining reflectors provide ~900 m^2. Delaminated plate remains attached by residual bolts/adhesive. | Post-deployment inspection; RCS measurement would show degradation | Mechanical fastening (bolts through frame + face plate edge); adhesive is secondary bond |
| AM frame fracture | MEDIUM — face plates lose alignment | FAIL-SAFE: Face plates remain attached to mast via mounting bolts; RCS degraded but not zero. 7 units compensate. | Visible frame crack; face plate misalignment | AM frame designed to safe-life (T5 heat treatment for ductility); AlSi10Mg UTS 350 MPa, FOS >=3 |
| Corrosion of face plates | LOW (72h) — surface roughness increases | SAFE-LIFE: Type II anodize >=10 um (MAT-008) protects for >72h. At X-band (lambda=32 mm), surface roughness up to Ra 1 mm has negligible RCS effect. | Visual discoloration of aluminum surface | Anodizing; RCS physics tolerance to surface roughness |

**Safety approach:** 8-unit functional redundancy (N-1 adequate). Individual reflectors use safe-life corrosion protection and mechanical retention.

#### L5: GPS Beacon System

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Battery depletion | MEDIUM — position tracking lost | PARTIALLY SAFE: Platform remains afloat and visible; loses electronic tracking only | Battery voltage reported via Iridium link; low-battery alarm | 72h battery with 10% margin (~80h actual); satellite reports battery state |
| GPS module failure | MEDIUM — same as battery | PARTIALLY SAFE: Same as above | No position fixes received at monitoring station | COTS module with proven MTBF >50,000 hours |
| Enclosure breach (water ingress) | HIGH — electronics short-circuit | FAIL-SAFE: Module fails; platform remains afloat. Retroreflector marking tape on masts provides visual identification. | No satellite data received | IP67/68 enclosure; mounting above maximum green water height (>=4.5 m AWL) |

**Safety approach:** Non-safety-critical subsystem. Platform safety does not depend on GPS. Beacon provides operational awareness, not structural safety.

#### L6: Tow/Deployment System

| Failure Mode | Severity | Safe State? | Detection | Mitigation |
|-------------|----------|-------------|-----------|------------|
| Tow line parting | HIGH — target adrift during transit | FAIL-SAFE: Platform floats; GPS reports position; recovery vessel can re-attach. No personnel on target during tow. | Visual (tow line goes slack); GPS position diverges from intended track | 16 mm Dyneema SWL 8,000 kgf vs peak tow load ~2,500 kgf (FOR-008); FOS >=3 |
| Bridle leg failure | MEDIUM — asymmetric tow, yaw instability | PARTIAL: Remaining bridle leg + drogue maintains some control. Reduce speed. | Visible yaw oscillation; uneven tow line tension | Each bridle leg rated to full tow load independently |
| Drogue loss | LOW — increased yaw during tow | SAFE: Reduce tow speed; platform stable without drogue at <=2 kn | Visual (drogue pendant slack) | Pendant shackle inspected before tow; drogue is a non-critical stabilizer |

**Safety approach:** Safe-life (3:1 SWL on all tow hardware) with fail-safe (platform floats, GPS tracks, no personnel at risk).

### 4.3 Failure Mode Summary (Safety-Critical Mini-FMEA)

Focused on the 10 most severe failure modes per Rule 3:

| # | Subsystem | Failure Mode | Severity | Safe State? | Detection | Mitigation | Safety Approach |
|---|-----------|-------------|----------|-------------|-----------|------------|-----------------|
| 1 | L0 Mooring | Chain link fracture | CRITICAL | YES — GPS tracks drift | GPS divergence | 3:1 SWL; safe-life chain | Safe-life + fail-safe |
| 2 | L0 Mooring | Anchor drag | HIGH | YES — slow recoverable drift | GPS position creep | Proper setting; verification pull | Safe-life |
| 3 | L0 Mooring | Pad eye weld failure | CRITICAL | YES — same as chain fracture | Post-failure | 3:1 weld sizing; NDE first article | Safe-life + fail-safe |
| 4 | L1 Hull | Hull breach | HIGH | YES — foam prevents sinking | Increased draft | Closed-cell foam fill (MAT-002) | Fail-safe |
| 5 | L1 Hull | Capsize | CATASTROPHIC | CANNOT OCCUR | N/A | BM = 210.3 m; physics-guaranteed | Inherently safe |
| 6 | L2 Frame | Socket weld failure | HIGH | YES — 7/8 reflectors remain | Mast tilt visible | Fatigue analysis; inspection | Redundant (N-1) |
| 7 | L2.5 Masts | Tube fatigue fracture | HIGH | YES — reflector on deck, wire retains | Visible broken mast | 40,000 cycle life; inspection | Safe-life + redundant |
| 8 | L2.5 Masts | Locking pin shear | MEDIUM | YES — safety wire retains | Mast rattling | Redundant: pin + safety wire | Redundant |
| 9 | L3 Reflectors | Face plate delamination | HIGH | YES — 7/8 remain adequate | Post-deployment QC | Mechanical fastening; safe-life | Redundant (N-1) |
| 10 | L6 Tow | Tow line parting | HIGH | YES — GPS tracks; no crew on target | Visual + GPS | 3:1 SWL Dyneema | Safe-life + fail-safe |

**Key safety finding:** No single-point failure in the design leads to loss of life or unrecoverable asset loss. The combination of (a) foam-filled unsinkable hull, (b) GPS tracking after mooring failure, (c) 8-unit reflector redundancy, and (d) no personnel on the target during operation creates a robust fail-safe architecture.

---

## 5. Rule 4: ECONOMY (Kinh te)

### 5.1 Economy Assessment by Subsystem

For each subsystem: Is the material over-specified? Is the manufacturing method optimal for the 10-100 units/year production volume?

| Subsystem | Material | Over-designed? | Manufacturing | Volume-appropriate? (10-100 units) | Action |
|-----------|----------|----------------|---------------|--------------------------------------|--------|
| **L0: Mooring** | G30 HDG chain, Danforth/Bruce anchor | NO — G30 is the minimum grade for the 4,536 kgf SWL. G43 or G70 would be over-spec and more expensive. | COTS procurement from marine supply chain (Hai Phong, Da Nang) | YES — off-the-shelf at any volume | None needed |
| **L1: Hull** | HDPE rotomolded/welded + PU foam fill | NO — HDPE is the lowest-cost marine-grade polymer. GRP would cost 2-3x more. Steel hull would cost less but weigh 2-3x more (GEO-007 violation). | Rotomold (if 1-piece) or HDPE welding (if 2-section). Rotomold tooling ~$15K amortized over 10+ units = $1,500/unit. | MARGINAL — Rotomold tooling break-even at ~8 units; welding is more flexible at <10 units but slower. | **Decision needed:** Rotomold if >=10 units confirmed; HDPE welding if initial batch <10 (TBD-007). |
| **L2: Frame** | S235 mild steel, HDG | NO — S235 is the lowest structural grade that meets requirements. S275 or S355 would be over-spec (higher cost, same geometry). | Welded fabrication + HDG batch dipping. Vietnamese steel fabricators (Hoa Phat, local workshops). | YES — Standard job shop work at any volume. HDG dipping is batch-efficient for 8+ frames. | None needed |
| **L2.5: Masts** | Galvanized steel tube 60 mm x 4 mm | BORDERLINE — 18% bending margin (FOR-011). Tube size is near-minimum. NOT over-designed. 76 mm x 5 mm fallback would add 3 kg/mast and ~$20/mast but give 60% margin. | Tube cutting, flange welding, HDG. Standard pipe shop work. | YES — Simple fabrication, no specialized tooling. | Monitor: if FEA shows margin <15% after dynamic analysis, upsize to 76 mm x 5 mm (small cost/mass penalty). |
| **L3: Reflectors** | 6061-T6 CNC face plates + AlSi10Mg AM frames | PARTIALLY — AM frames are the highest-cost element ($16K = 48% of hardware). CNC-only alternative at +/-0.3 deg saves ~$8K/unit but degrades RCS to 800-1,000 m^2 (still meets SIG-001 marginally). | Hybrid AM/CNC: face plates CNC fly-cut locally (Vietnam), AM frames LPBF (ASEAN import — Singapore/Thailand). | MODERATE — AM is cost-effective only at >=10 units (amortized setup). CNC-only is better at <10 units. | **Key trade-off (CF-03):** Maintain AM baseline; prototype 1 unit in Phase 3 to validate RCS benefit. If military rejects AM, switch to CNC-only (cost drops to ~$8K for 8 reflectors). |
| **L5: GPS Beacon** | COTS GNSS/Iridium + Li-ion battery | NO — COTS is minimum-cost approach. Custom development would cost 10-50x more. | Procurement + minor integration (battery pack, enclosure, mast bracket). | YES — COTS procurement scales linearly. | None needed |
| **L6: Tow System** | 16 mm Dyneema + marine hardware | NO — Dyneema is lighter and stronger than equivalent polyester/nylon at similar cost. 16 mm is minimum diameter for 7,524 kgf SWL. | COTS marine rope and hardware procurement. | YES — Off-the-shelf at any volume. | None needed |

### 5.2 Cost Efficiency Assessment Summary

| Subsystem | Est. Cost | % of Unit | Over-designed? | Volume-appropriate? | Cost-down Opportunity |
|-----------|-----------|-----------|----------------|---------------------|-----------------------|
| L0: Mooring | $2,500 | 7.5% | NO | YES | NONE — COTS minimum |
| L1: Hull | $8,200 | 24.5% | NO | MARGINAL | Rotomold vs weld trade at TBD-007 |
| L2: Frame | $1,800 | 5.4% | NO | YES | NONE — local steel fab |
| L2.5: Masts | $800 | 2.4% | NO | YES | NONE — near minimum |
| L3: Reflectors | $13,000 | 38.9% | PARTIAL | MODERATE | CNC-only fallback saves $8K (CF-03) |
| L5: GPS Beacon | $1,800 | 5.4% | NO | YES | NONE — COTS |
| L6: Tow System | $400 | 1.2% | NO | YES | NONE — COTS minimum |
| Assembly/QC/margin | $5,100 | 14.7% | — | — | Optimize assembly time |
| **TOTAL** | **$33,600** | **100%** | — | — | **CNC-only reflectors: -$8K = $25.6K** |

**Economy verdict:** The design is cost-efficient for a 10-100 unit military marine product. The only significant cost-down opportunity is the AM-to-CNC-only reflector trade-off (CF-03), which saves ~24% of unit cost but degrades RCS precision. All other subsystems use minimum-spec COTS or standard local fabrication. Total $33.6K hardware is within the $36K unit target.

---

## 6. Rules Compliance Matrix

### 6.1 Compliance Matrix (7 Subsystems x 4 Rules = 28 Cells)

| Subsystem | Rule 1: CLARITY | Rule 2: SIMPLICITY | Rule 3: SAFETY | Rule 4: ECONOMY |
|-----------|-----------------|--------------------| ---------------|-----------------|
| **L0: Mooring** | **PASS** — Function unambiguous; load path: hull -> frame -> pad eye -> chain -> anchor. Hidden failure (anchor drag) mitigated by GPS. | **PASS** — 7 parts, all necessary. No simplification feasible without losing a required function. | **PASS** — Safe-life (3:1 SWL) + fail-safe (GPS tracking after mooring failure). No single-point catastrophic failure. | **PASS** — G30 chain is minimum grade; COTS procurement; $2,500 is competitive with commercial mooring kits. |
| **L1: Hull** | **PASS** — Buoyancy shell function clear. Frame handles structural loads. No dual-function ambiguity. | **PASS** — 2-3 parts. 1-piece hull saves 1 joint (TBD-007 pending). Already near-minimum part count. | **PASS** — Unsinkable (foam fill), uncapsizable (BM = 210.3 m). Fail-safe at most fundamental level. | **PASS** — HDPE is lowest-cost marine polymer. Rotomold amortization acceptable at >=10 units. |
| **L2: Frame** | **PASS** — Structural backbone function clear. All loads traceable. No hidden joints. | **PARTIAL** — ~12 parts; pad eye integration into hub plate can eliminate 5 parts. Action: integrate pad eye into central hub plate. | **PASS** — Safe-life HDG coating (40+ year life). N-1 socket redundancy. Conservative yield utilization (<=60%). | **PASS** — S235 minimum grade. Standard Vietnamese steel fabrication. $1,800 is competitive. |
| **L2.5: Masts** | **PASS** — Simple cantilever function. Load path analytically clear. Fatigue crack identified as hidden failure with inspection mitigation. | **PASS** — 4 parts per mast, 40 total. Pre-weld top plates at factory. Socket-insert minimizes field assembly. | **PASS** — Redundant retention (pin + wire). N-1 array redundancy. Safe-life fatigue design (40,000 cycles). | **PASS** — 60 mm x 4 mm tube is near-minimum for bending requirement. Standard pipe shop fabrication. $800 for 8 masts. |
| **L3: Reflectors** | **PASS** — Retroreflection physics deterministic. Load path through AM frame to mast mount clear. Orthogonality drift identified with mitigation. | **PARTIAL** — ~72 parts total (highest in system). AM frame consolidates ~50% vs CNC-only alternative, but 8 face plates per reflector x 3 = 24 precision surfaces. Action: investigate integrated 2-face plate design (2 faces from single bent sheet) — likely infeasible due to orthogonality but should be evaluated. | **PASS** — N-1 array redundancy. Safe-life corrosion protection (anodize). Mechanical retention with safety wire. | **PARTIAL** — AM frames are 48% of hardware cost ($16K). CNC-only fallback saves $8K but degrades precision. Decision pending prototype RCS validation in Phase 3 (CF-03). |
| **L5: GPS Beacon** | **PASS** — Single COTS function. No structural load path. Battery depletion identified with Iridium voltage reporting mitigation. | **PASS** — 4 parts. COTS minimum. Cannot simplify further. | **PASS** — Non-safety-critical subsystem. Platform safety independent of GPS. Beacon is operational awareness only. | **PASS** — COTS procurement. $1,800 is market price. No over-specification. |
| **L6: Tow** | **PASS** — Two clear functions (tow + yaw stabilize). Load path: vessel -> line -> bridle -> hull. All hardware visible. | **PASS** — 7 parts. Single-point tow fallback eliminates 3 parts but reduces yaw stability. Baseline configuration is appropriate. | **PASS** — Safe-life (3:1 SWL). Fail-safe (platform floats, GPS tracks, no personnel on target). | **PASS** — 16 mm Dyneema is minimum diameter for SWL. COTS hardware. $400 is minimal. |

### 6.2 Compliance Score

| Status | Count | Cells |
|--------|-------|-------|
| **PASS** | **25** | L0 all 4, L1 all 4, L2 (Clarity + Safety + Economy), L2.5 all 4, L3 (Clarity + Safety), L5 all 4, L6 all 4 |
| **PARTIAL** | **3** | L2 Simplicity (pad eye integration), L3 Simplicity (high part count), L3 Economy (AM cost) |
| **FAIL** | **0** | None |

```
+===============================================================+
|              RULES COMPLIANCE SCORE                             |
+=================================================================+
|                                                                 |
|  PASS:    25 / 28  (89.3%)                                      |
|  PARTIAL:  3 / 28  (10.7%)                                      |
|  FAIL:     0 / 28  ( 0.0%)                                      |
|                                                                 |
|  SCORE: 89.3% — EXCEEDS 85% TARGET                             |
|                                                                 |
|  3 PARTIAL items have defined actions:                          |
|    1. L2 Simplicity: Integrate pad eye into hub plate           |
|    2. L3 Simplicity: Evaluate 2-face bent sheet concept         |
|    3. L3 Economy: Prototype AM vs CNC-only (CF-03 resolution)   |
|                                                                 |
+=================================================================+
```

---

## 7. Action Items from Rules Application

| # | Rule | Subsystem | Issue | Action | Priority | Owner | Links to |
|---|------|-----------|-------|--------|----------|-------|----------|
| R6-01 | Simplicity | L2: Frame | Pad eye is separate component with 4 through-bolts + backing plate | Redesign: integrate pad eye forging into central hub plate (increase hub thickness 10->16 mm). Saves 5 parts, eliminates 1 bolted interface. | HIGH | Structural design | CF-08, ASM-005 |
| R6-02 | Simplicity | L3: Reflectors | 72 parts total across 8 reflectors is the highest subsystem part count | Evaluate: can any 2 face plates be formed from a single bent aluminum sheet? (Likely infeasible due to +/-0.1 deg orthogonality requirement but must be formally rejected.) | MEDIUM | Reflector design | SIG-009, MAT-003 |
| R6-03 | Economy | L3: Reflectors | AM frames cost $16K (48% of hardware). CNC-only fallback saves $8K. | Prototype: manufacture 1 hybrid AM/CNC reflector and 1 CNC-only reflector. Measure RCS of both. Present cost-benefit to customer. | HIGH | AM/CNC trade study | CF-03, R-1, SIG-001 |
| R6-04 | Economy | L1: Hull | Rotomold vs HDPE welding decision affects tooling cost amortization | Decision gate: confirm >=10 unit order before committing to rotomold tooling ($15K). If <10 units, use HDPE welding. | MEDIUM | Hull fabrication | TBD-007 |
| R6-05 | Clarity | All | 5 hidden failure modes identified across subsystems | Document: add all 5 hidden failure modes to project FMEA register with detection methods and inspection intervals. | HIGH | Systems engineering | SAF-003, FOR-010, ENR-001 |
| R6-06 | Safety | L2.5: Masts | Fatigue crack at weld toe is hidden failure mode | Require: visual inspection of all mast-socket weld toes before each deployment. Define inspection criteria (crack >2 mm = replace mast). | HIGH | Maintenance plan | FOR-010, SAF-006 |

---

## 8. Cross-References

### PRAD Workflow (Steps P5-A7-D8-R6)

- [[PRAD_P5_preliminary_layout.md]] -- Step P5: Preliminary layout and spatial arrangement (preceding step)
- [[PRAD_A7_form_design.md]] -- Step A7: Form design and dimensioning (parallel step)
- [[PRAD_D8_detail_design.md]] -- Step D8: Detailed design and manufacturing preparation (following step)

### RISM Workflow (Steps R1-I2-S3-M4)

- [[RISM_R1_requirements_identification.md]] -- 74 direct embodiment requirements mapped to 7 subsystems (primary input)
- [[RISM_I2_critical_requirements.md]] -- 55 hard constraints, 8 embodiment conflicts, criticality ranking (primary input)
- [[RISM_S3_material_selection.md]] -- Material screening against hard constraints (supports Rule 4 Economy)
- [[RISM_M4_material_analysis.md]] -- VDI 2225 material selection matrices (supports Rule 4 Economy)

### Phase 2 Source Documents

- [[../02_conceptual/concept_selection.md]] -- Concept A architecture (81.8% VDI 2225), risk register R-1 to R-5
- [[../02_conceptual/function_structure.md]] -- Function-to-subsystem mapping (F1-F7, 21 sub-functions)
- [[../02_conceptual/concept_evaluation.md]] -- Evaluation scores and sensitivity analysis

### Phase 1 Source Documents

- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), 16 Pahl & Beitz categories
- [[../01_requirements/standards_mapping.md]] -- MIL-STD-810H, 882E, TCVN, ASTM compliance mapping

---

*Document generated as part of the PRAD (Preliminary-layout, Rules-application, form-design, Detail-design) embodiment design process per Pahl & Beitz VDI 2221. This document verifies that the Concept A embodiment satisfies the 4 basic rules of embodiment design. 3 PARTIAL compliance items require resolution in subsequent PRAD steps (D8 Detail Design). Rules Compliance Score: 89.3% (target >=85%).*
