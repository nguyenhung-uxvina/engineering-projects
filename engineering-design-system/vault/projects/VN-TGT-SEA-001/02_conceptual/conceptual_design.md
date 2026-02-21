---
project: VN-TGT-SEA-001
phase: 2
type: conceptual_design
version: 1.0
created: 2026-02-10
status: draft
revision: B.1
---

# Conceptual Design: VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Phase:** 2 — Conceptual Design (Pahl & Beitz)
**Input:** 116 requirements (Rev B.1), 73 ODI outcomes, Phase 0 feasibility
**Output:** Selected principle solution with VDI 2225 evaluation

---

## Step 1: Abstraction (5-Step Process)

### 1.1 Original Problem Statement

> "Design an 8.0m anchored HDPE sea target platform with 8 hybrid AM/CNC corner reflectors on steel masts producing >1,000 m² RCS at X-band, surviving SS 5-6 for 72 hours, at $35.6K/unit, for Vietnamese Navy anti-ship missile acceptance testing."

### 1.2 Five-Step Abstraction

| Step | Transformation | Before | After |
|------|----------------|--------|-------|
| **1. Remove preferences** | Remove material/technology choices | "HDPE hull", "AM/CNC reflectors", "steel masts" | "hull", "reflectors", "supports" |
| **2. Omit non-essential** | Remove secondary features | "GPS beacon", "tow equipment", "8.0m diameter" | Focus on core: float, hold, reflect |
| **3. Quantitative → qualitative** | Generalize numbers | ">1,000 m²", "SS 5-6", "$35.6K" | "frigate-class signature", "storm conditions", "affordable" |
| **4. Generalize** | Broaden scope | "anti-ship missile test target" | "radar-guided weapon evaluation target" |
| **5. Solution-neutral** | Remove all technology references | All specific solutions | Pure function statement |

### 1.3 Essential Problem Statement

> **"Provide a stationary, anchored floating body that presents a controlled, high-magnitude radar cross-section from all horizontal approach directions, surviving rough open-sea conditions for extended duration, requiring no personnel during engagement, at minimum lifecycle cost."**

### 1.4 Abstract Functions Identified

| # | Abstract Function | Corresponding Requirements |
|---|-------------------|---------------------------|
| AF-1 | Float stably at sea surface | GEO-001 to GEO-010, KIN-001 to KIN-004 |
| AF-2 | Hold position at designated location | FOR-001 to FOR-011, OPR-005, OPR-006 |
| AF-3 | Generate controlled radar signature | SIG-001 to SIG-009 |
| AF-4 | Support signature elements above water | GEO-005, GEO-010, FOR-011 |
| AF-5 | Report position to shore | ENR-001, ENR-002, SIG-007, SIG-008 |
| AF-6 | Enable transport and deployment | TRA-001 to TRA-006, ERG-001 to ERG-007, KIN-005 |
| AF-7 | Withstand environmental loads | OPR-001 to OPR-009, FOR-009, FOR-010 |
| AF-8 | Be producible at target cost | PRD-001 to PRD-008, CST-001 to CST-007 |

---

## Step 2: Function Structure

### 2.1 Overall Function

```
OVERALL FUNCTION: Present radar target at sea for weapon engagement
═══════════════════════════════════════════════════════════════════

INPUTS                          OUTPUTS
  E: Wave energy ──────────►    E: Reflected radar energy (RCS)
  E: Wind energy ──────────►    E: Dissipated energy (drag, motion)
  E: Current energy ───────►    S: GPS position data → shore
  S: Radar illumination ───►    S: Reflected radar signal → missile
  M: Seawater (contact) ──►     M: Debris (post-engagement)
```

### 2.2 Sub-Function Decomposition

```
┌─────────────────────────────────────────────────────────────────┐
│            PRESENT RADAR TARGET AT SEA FOR ENGAGEMENT           │
└───────────────────────────────┬─────────────────────────────────┘
                                │
    ┌───────────┬───────────┬───┴───┬───────────┬───────────┐
    │           │           │       │           │           │
    ▼           ▼           ▼       ▼           ▼           ▼
┌───────┐ ┌─────────┐ ┌────────┐ ┌──────┐ ┌────────┐ ┌────────┐
│  F1   │ │   F2    │ │  F3    │ │  F4  │ │  F5    │ │  F6    │
│Float  │ │ Hold    │ │Generate│ │Support│ │Report  │ │Deploy/ │
│stably │─│position │─│radar   │─│signat.│─│position│─│recover │
│at sea │ │at loc.  │ │signat. │ │above  │ │to shore│ │target  │
└───┬───┘ └────┬────┘ └───┬────┘ └──┬───┘ └───┬────┘ └───┬────┘
    │          │          │         │         │          │
    ▼          ▼          ▼         ▼         ▼          ▼
 Buoyancy  Anchoring  Reflection  Struct.   GPS/Radio  Tow/lift
 Stability Catenary   RCS ctrl   Mast/ped  Beacon     Connect
 Draft     Scope      360° cov   Marine    Battery    Crew ops
 Wave resp Weathervn  Freq match Corr prot Waterproof Storage

FLOWS:
───────► Energy (wave, wind, current → structure → mooring → seabed)
- - - -► Material (seawater ↔ hull, air ↔ above waterline)
═══════► Signal (radar → reflectors → return; GPS → satellite → shore)
```

### 2.3 Sub-Function Detail

| ID | Sub-Function | Input Flows | Output Flows | Critical Req. |
|----|--------------|-------------|--------------|---------------|
| **F1** | Float stably at sea surface | E: wave/wind loads; M: seawater | E: dissipated (drag); M: displaced water | GEO-001, KIN-001, SAF-007 |
| **F2** | Hold position at designated location | E: wind+current+wave drift forces | E: anchor holding force → seabed | FOR-004-007, OPR-005-006 |
| **F3** | Generate controlled radar signature | S: incident radar illumination | S: reflected radar (>1,000 m², 360°) | SIG-001-006, SIG-009 |
| **F4** | Support signature elements above water | E: structural loads (weight, wind, wave) | E: reaction forces → deck → hull | GEO-005, GEO-010, FOR-011 |
| **F5** | Report position to shore | E: battery power | S: GPS coordinates (±5m, 1 Hz) | ENR-001-002, SIG-007-008 |
| **F6** | Enable deployment and recovery | E: tug propulsion; M: tow line | E: tow resistance; S: crew instructions | ERG-001-007, TRA-001-006 |

### 2.4 Interface Definitions

| Interface | Between | Flow | Critical Constraint |
|-----------|---------|------|---------------------|
| I-1 | F1↔F2 | E: mooring load through hull | Pad eye SWL ≥4,536 kgf (FOR-006) |
| I-2 | F1↔F4 | E: structural loads through deck | Mast base moment ≥1,100 N·m (FOR-011) |
| I-3 | F3↔F4 | E: reflector weight on support | 15 kg per reflector at 3-4m AGL (GEO-005) |
| I-4 | F4↔F1 | E: deck socket to hull frame | Welded flange, cyclic ≥40,000 (FOR-010) |
| I-5 | F5↔F4 | E: beacon weight on mast | ≥4.5m AGL, <5 kg (GEO-006) |
| I-6 | F6↔F1 | E: tow load through bridle | Tow SWL ≥7,524 kgf (FOR-008) |

---

## Step 3: Working Principles Search

### 3.1 Principle Catalog per Sub-Function

#### F1: Float Stably at Sea Surface

| ID | Working Principle | Physical Effect | TRL | Cost | Advantages | Disadvantages |
|----|-------------------|----------------|-----|------|------------|---------------|
| **P1.1** | **Solid circular pontoon (HDPE + foam)** | Archimedes buoyancy, high waterplane area | 9 | LOW | Simple, unsinkable, low draft, rotomoldable | Large diameter for stability |
| P1.2 | Inflatable ring hull | Pneumatic buoyancy | 8 | LOW | Compact storage, light | Puncture risk in SS 5-6, limited lifespan |
| P1.3 | Multi-hull catamaran | Distributed waterplane | 9 | MED | Good stability, deck area | Complex structure, wider transport |
| P1.4 | Spar buoy (vertical cylinder) | Deep ballast, minimal waterplane | 8 | MED | Excellent heavy-weather, low motion | Difficult to tow, heavy, complex deploy |
| P1.5 | Steel barge (flat-bottom) | Displacement hull | 9 | MED | Simple, robust, proven | Heavy, corrosion, no foam fill safety |

#### F2: Hold Position at Designated Location

| ID | Working Principle | Physical Effect | TRL | Cost | Advantages | Disadvantages |
|----|-------------------|----------------|-----|------|------------|---------------|
| **P2.1** | **Single-point mooring (anchor + catenary)** | Gravity catenary, anchor friction | 9 | LOW | Simple, allows weathervane, proven | Swing circle, depth-dependent |
| P2.2 | Multi-point mooring (3-4 anchors) | Distributed restraint | 9 | MED | Tight position hold | Complex deploy, no weathervane, higher cost |
| P2.3 | Dynamic positioning (thrusters) | Active control | 7 | HIGH | Precise position, any depth | Power, cost, not passive, C2 required |
| P2.4 | Deadweight (concrete block) | Gravity only | 9 | LOW | Simple, cheap | Poor holding in storm, hard to deploy |

#### F3: Generate Controlled Radar Signature

| ID | Working Principle | Physical Effect | TRL | Cost | Advantages | Disadvantages |
|----|-------------------|----------------|-----|------|------------|---------------|
| **P3.1** | **Trihedral corner reflectors (passive)** | Retroreflection (3-bounce) | 9 | MED | Broadband, 360° (array), proven physics, no power | Size-dependent, ±15° beamwidth |
| P3.2 | Luneburg lens reflectors | Graded-index focusing | 7 | HIGH | Wide angle (±60°), compact | Expensive, heavy, fragile, moisture-sensitive |
| P3.3 | Active radar transponder/augmentor | Electronic amplification | 8 | HIGH | Any RCS level, compact | Power required, not passive, EMC, cost |
| P3.4 | Flat plate array (specular) | Specular reflection | 9 | LOW | Simple, cheap | Very narrow beamwidth (~2°), no 360° |
| P3.5 | Dielectric lens reflector | Refraction focusing | 6 | HIGH | Moderate angle coverage | Low TRL, expensive materials |

#### F4: Support Signature Elements Above Water

| ID | Working Principle | Physical Effect | TRL | Cost | Advantages | Disadvantages |
|----|-------------------|----------------|-----|------|------------|---------------|
| **P4.1** | **Fixed steel mast in deck socket** | Cantilever beam | 9 | LOW | Simple, field-erectable, proven | Windage, bending moment at base |
| P4.2 | Guyed mast (steel + cable stays) | Tensioned structure | 9 | LOW | Higher capacity, lighter mast | More complex erection, deck clutter |
| P4.3 | A-frame / tripod | Triangulated structure | 9 | MED | Very stable, high capacity | Heavy, complex, more deck area |
| P4.4 | Deck-mounted pedestal (low profile) | Short cantilever | 9 | LOW | Simple, minimal windage | Low height = sea clutter interference |

#### F5: Report Position to Shore

| ID | Working Principle | Physical Effect | TRL | Cost | Advantages | Disadvantages |
|----|-------------------|----------------|-----|------|------------|---------------|
| **P5.1** | **GPS beacon (satellite relay)** | GNSS + satellite data link | 9 | MED | Global coverage, ±5m, proven | Battery life, cost ($1,500-2,000) |
| P5.2 | AIS transponder | VHF radio broadcast | 9 | LOW | Standard marine, low cost | Line-of-sight only (~20 nm), power |
| P5.3 | Radar transponder (RACON) | Active radar response | 8 | MED | Visible on radar, no C2 | May interfere with seeker test |
| P5.4 | Iridium/satellite tracker | Satellite modem | 9 | MED | Reliable, global | Monthly service cost |

#### F6: Enable Deployment and Recovery

| ID | Working Principle | Physical Effect | TRL | Cost | Advantages | Disadvantages |
|----|-------------------|----------------|-----|------|------------|---------------|
| **P6.1** | **Surface tow by tug** | Drag resistance | 9 | LOW | Simple, proven, any tug | Weather-limited (SS 4-5), tow resistance |
| P6.2 | Self-propelled (outboard/electric) | Motor thrust | 8 | MED | Independent of tug | Power, cost, complexity, not passive |
| P6.3 | Helicopter sling load | Aerodynamic lift | 8 | HIGH | Fast, all-weather | Weight limit (~2,000 kg), expensive |
| P6.4 | Crane/davit launch from ship | Mechanical lift | 9 | MED | Controlled deployment | Requires ship with crane, limiting |

---

## Step 4: Morphological Matrix

### 4.1 Matrix

| Sub-Function | **Sol 1** | **Sol 2** | **Sol 3** | **Sol 4** |
|--------------|-----------|-----------|-----------|-----------|
| **F1: Float** | **P1.1 Solid HDPE pontoon** | P1.3 Catamaran | P1.4 Spar buoy | P1.5 Steel barge |
| **F2: Hold position** | **P2.1 Single-point mooring** | P2.2 Multi-point | P2.4 Deadweight | — |
| **F3: Generate RCS** | **P3.1 Corner reflectors** | P3.2 Luneburg lens | P3.3 Active transponder | P3.4 Flat plates |
| **F4: Support** | **P4.1 Fixed mast** | P4.2 Guyed mast | P4.3 A-frame | P4.4 Pedestal (low) |
| **F5: Position** | **P5.1 GPS beacon** | P5.2 AIS | P5.4 Iridium tracker | — |
| **F6: Deploy** | **P6.1 Surface tow** | P6.3 Helicopter | P6.4 Ship crane | — |

### 4.2 Concept Generation (4 Concepts)

```
CONCEPT PATHS THROUGH MORPHOLOGICAL MATRIX
═══════════════════════════════════════════════════════

         F1        F2        F3        F4        F5        F6
         Float     Hold      RCS       Support   Position  Deploy
         ─────     ────      ───       ───────   ────────  ──────
Con A:  [HDPE]───[SPM]────[Corner]──[Fixed]───[GPS]────[Tow]
         pont.    anchor    reflec.   mast      beacon    tug
                                     (3-4m)

Con B:  [Spar]───[SPM]────[Corner]──[A-frame]─[GPS]────[Tow]
         buoy    anchor    reflec.   tripod    beacon    tug

Con C:  [Catam]──[Multi]──[Corner]──[Guyed]───[AIS]────[Ship]
         aran     point    reflec.   mast      transp.   crane

Con D:  [Steel]──[SPM]────[Active]──[Pedestal]─[GPS]───[Tow]
         barge    anchor    transp.  (low)      beacon   tug
```

---

### 4.3 Concept Descriptions

#### Concept A: "Baseline Optimized" (Current Rev B.1 Architecture)

```
CONCEPT A: BASELINE OPTIMIZED
═══════════════════════════════

        ┌─R1─┐ (3-4m on mast)
       /│    │\
  ┌─R8─┐      ┌─R2─┐        8× corner reflectors
 /│    ││      ││    │\       on fixed steel masts
│ │    ││      ││    │ │      in deck sockets
├──────┤├──────┤├──────┤
│ ████████████████████ │      8.0m HDPE circular
│ ████ closed-cell ███ │      pontoon with foam fill
│ ████████████████████ │
└──────────┬───────────┘
           │ chain/rode (catenary)
           │
           ⚓ Danforth anchor (SPM)

F1: HDPE circular pontoon (8.0m) + closed-cell foam
F2: Single-point mooring (Danforth + chain/rode)
F3: 8× trihedral corner reflectors (0.8m, hybrid AM/CNC)
F4: 8× fixed steel masts (60mm×4mm, ~3m, deck sockets)
F5: GPS beacon (72h battery, elevated ≥4.5m)
F6: Surface tow (bridle + drogue)

Key features:
  - Proven architecture from Phase 0/1 analysis
  - Hybrid AM/CNC reflectors: CNC faces + AM frames (±0.1°)
  - Pre-deployable mooring concept
  - Fully passive, radar-only
  - 980 kg displacement, >93% reserve buoyancy
  - BM = 210.3 m (extreme stability)

Estimated unit cost: $35,640 @ 10 units
```

#### Concept B: "Spar Buoy"

```
CONCEPT B: SPAR BUOY
═════════════════════

    ┌─R─R─R─R─┐ (reflectors on A-frame top)
    │  A-frame  │
    │  tripod   │    Reflectors 4-6m above water
    │           │
  ~~│~~~~~~~~~~~│~~ waterline (~1m freeboard)
    │           │
    │  steel    │    Vertical steel cylinder
    │  cylinder │    ~1.5m dia × 6m tall
    │  (spar)   │    Lower 5m submerged
    │           │
    │  ballast  │    Concrete/steel ballast
    └─────⚓────┘    in lower compartment
           │
      chain/rode

F1: Steel spar buoy (1.5m dia × 6m, ballasted)
F2: Single-point mooring (Danforth + chain/rode)
F3: 4-6× trihedral corner reflectors (0.8m)
F4: A-frame/tripod at spar top
F5: GPS beacon (integrated)
F6: Surface tow (horizontal, then upend at site)

Key features:
  - Excellent heavy-weather performance (minimal waterplane)
  - Very low heave/pitch motion in SS 6
  - Natural weathervaning
  - High reflector elevation (4-6m)

Challenges:
  - Heavy (~2,500 kg), difficult to tow and deploy
  - Must be upended at site (crane or flooding ballast tanks)
  - Limited number of reflectors (space on top)
  - 360° coverage with fewer reflectors = larger nulls
  - Complex manufacturing (watertight cylinder)

Estimated unit cost: $55,000-70,000 @ 10 units
```

#### Concept C: "Multi-Hull Station Keeper"

```
CONCEPT C: MULTI-HULL STATION KEEPER
═════════════════════════════════════

  ┌─R─┐  guyed   ┌─R─┐
  │   │  mast    │   │    4× reflectors on
  │   │  ┌─R─┐  │   │    guyed masts
  │   │  │   │  │   │
 ═╤═══╤══╤═══╤══╤═══╤═    Cross-deck
  │hull│  │   │  │hull│    (catamaran)
  │ 1 │  │   │  │ 2  │
  └───┘  └───┘  └───┘
   ⚓──────⚓──────⚓        3-point mooring

F1: Catamaran (2× 1.2m × 8m HDPE hulls)
F2: Multi-point mooring (3× anchors, no weathervane)
F3: 4-8× trihedral corner reflectors (0.8m)
F4: Guyed masts on cross-deck
F5: AIS transponder (lower cost)
F6: Ship crane launch (modular assembly at ship)

Key features:
  - Good stability from catamaran configuration
  - Tight position holding (3-point mooring)
  - Modular construction

Challenges:
  - Multi-point mooring = 3× deploy complexity
  - No weathervaning → asymmetric storm loads
  - AIS only = line-of-sight position reporting
  - Higher cost (3 anchors, 2 hulls, cross-deck)
  - Requires ship with crane for deployment

Estimated unit cost: $50,000-65,000 @ 10 units
```

#### Concept D: "Active Signature Barge"

```
CONCEPT D: ACTIVE SIGNATURE BARGE
══════════════════════════════════

  ┌───────────────────────────┐
  │   active radar transponder │    X-band amplifier
  │   ┌─────────────────────┐ │    (programmable RCS)
  │   │  electronics box    │ │
  │   │  battery bank       │ │    Battery: 72h runtime
  │   └─────────────────────┘ │
  │                           │
  │  flat steel barge (6×3m)  │    Traditional barge
  │                           │
  └─────────────┬─────────────┘
                │
           chain/rode
                ⚓

F1: Flat steel barge (6m × 3m)
F2: Single-point mooring (Danforth + chain/rode)
F3: Active radar transponder (programmable RCS 100-10,000 m²)
F4: Low pedestal (electronics box on deck)
F5: GPS beacon (integrated with transponder)
F6: Surface tow

Key features:
  - Programmable RCS (any value, any frequency)
  - Compact (no large reflectors needed)
  - Simple structure

Challenges:
  - NOT passive (battery + electronics = complexity)
  - Active transponder may not match real ship RCS signature
  - EMC concerns during missile engagement
  - Military acceptance of "fake" vs "real" RCS questionable
  - Battery system adds cost, maintenance, safety issues
  - Steel barge: corrosion, heavy, no foam safety
  - Flat barge: poor SS 5-6 performance

Estimated unit cost: $80,000-120,000 @ 10 units
```

---

## Step 5: Concept Evaluation (VDI 2225)

### 5.1 Evaluation Criteria

Criteria derived from 116 requirements, weighted by ODI outcome priority:

| # | Criterion | Weight (g) | Rationale | Key Requirements |
|---|-----------|------------|-----------|------------------|
| 1 | **RCS performance** (>1,000 m², 360°, ±2 dB) | 0.20 | EXTREME outcome O-29, O-31; core product function | SIG-001 to SIG-006 |
| 2 | **Environmental survivability** (SS 5-6, 72h) | 0.20 | EXTREME outcome O-57; core differentiator | OPR-001 to OPR-004 |
| 3 | **Unit cost** (≤$36K @ 10 units) | 0.15 | EXTREME outcome O-71; competitive positioning | CST-001 to CST-007 |
| 4 | **Local content** (≥85%) | 0.08 | Vietnamese defense policy; market access | PRD-002, PRD-004, PRD-005 |
| 5 | **Deployment simplicity** (≤4 crew, ≤30 min) | 0.10 | HIGH outcome O-34; operational tempo | ERG-001 to ERG-007, ASM-006 |
| 6 | **Safety** (passive, 5+ km clearance) | 0.10 | Core differentiator vs competitors | SAF-001 to SAF-007 |
| 7 | **Development risk** (schedule, technology) | 0.10 | Budget $292K, 18-month timeline | SCH-001 to SCH-006 |
| 8 | **Production scalability** (≥6 units/month) | 0.07 | Volume demand 50-100 units/year | PRD-001, PRD-003, PRD-006 |
| **Σ** | | **1.00** | | |

> **Note:** Weights set BEFORE evaluation per VDI 2225 best practice. Weights reflect ODI opportunity scores: EXTREME outcomes (O-57, O-71, O-37) weighted highest.

### 5.2 VDI 2225 Scoring Scale

```
0 = Absolutely unsatisfactory (does not meet requirement)
1 = Just tolerable (barely meets minimum, high risk)
2 = Adequate (meets requirement with effort)
3 = Good (meets requirement comfortably)
4 = Very good (exceeds requirement, near-ideal)
```

### 5.3 Evaluation Matrix

| # | Criterion | g | Max | **A: Baseline** | **B: Spar Buoy** | **C: Multi-Hull** | **D: Active Barge** |
|---|-----------|---|-----|-----------------|------------------|--------------------|--------------------|
| 1 | RCS performance | 0.20 | 4 | **4** | 3 | 3 | 3 |
| 2 | Env. survivability | 0.20 | 4 | **3** | **4** | 3 | 1 |
| 3 | Unit cost | 0.15 | 4 | **3** | 1 | 2 | 0 |
| 4 | Local content | 0.08 | 4 | **3** | 3 | 3 | 2 |
| 5 | Deployment simplicity | 0.10 | 4 | **3** | 1 | 1 | 3 |
| 6 | Safety (passive) | 0.10 | 4 | **4** | 4 | 3 | 2 |
| 7 | Development risk | 0.10 | 4 | **3** | 2 | 2 | 2 |
| 8 | Production scalability | 0.07 | 4 | **3** | 2 | 2 | 2 |
| | | | | | | | |
| | **Σ(g × p)** | 1.00 | 4.00 | **3.27** | **2.60** | **2.40** | **1.59** |
| | **Score %** | | 100% | **81.8%** | **65.0%** | **60.0%** | **39.8%** |
| | **Decision** | | | **PROCEED** | **REVIEW** | **REVIEW** | **REJECT** |

### 5.4 Scoring Rationale

#### Concept A: Baseline Optimized — **81.8%** (PROCEED)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| RCS | **4** | 8 × 0.8m hybrid reflectors = 1,218 m² peak, ~1,050 m² average. Proven physics, AM frame ensures ±0.1° orthogonality. Well-established in Phase 0. |
| Survivability | **3** | 8.0m HDPE pontoon, BM=210.3m, foam-filled. Good stability. Mast windage adds 25% to wind load but within mooring capacity. SS 5-6 for 72h achievable. Not 4 because mast windage is a concern and unproven at SS 6. |
| Cost | **3** | $35,640 @ 10 units — meets $36K target. AM frames are the cost driver ($8K). Hybrid approach keeps cost manageable. Not 4 because AM frames prevent further cost reduction. |
| Local content | **3** | 85-90% local. Hull, frame, CNC plates, mooring all Vietnamese. AM frames imported (ASEAN). Not 4 because AM dependence on imports. |
| Deployment | **3** | 4 crew, ≤30 min. Tow + mooring connect + mast erection. Pre-deploy mooring helps. Mast erection adds ~15 min but manageable (31 kg/mast unit, socket insert). |
| Safety | **4** | Fully passive. No electronics except GPS beacon. No C2 vessel. 5+ km clearance. Radar-only = no fuel/propane. Best-in-class safety. |
| Risk | **3** | Hybrid AM/CNC is de-risked vs full AM. Main risk: military AM acceptance (50%). CNC fallback available (Concept D in original analysis). 8.0m HDPE and steel masts are proven technologies. |
| Production | **3** | HDPE pontoon, steel frame, CNC plates all local. AM frames need ASEAN bureau (3-week lead). 6/month achievable with 2+ AM suppliers. |

#### Concept B: Spar Buoy — **65.0%** (REVIEW)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| RCS | **3** | Corner reflectors on A-frame top. Limited space = fewer reflectors or smaller edge. 360° coverage harder with 4-6 reflectors (larger nulls). Could reach 1,000 m² but with ±4-5 dB variation. |
| Survivability | **4** | Spar buoys are the gold standard for heavy-weather ocean platforms. Minimal waterplane = minimal heave/pitch. Natural weathervaning. Proven in oil industry for decades in SS 6+. |
| Cost | **1** | Steel cylinder fabrication, ballast system, complex deployment = $55-70K. Nearly 2× the budget target. Pressure-tested watertight compartments add cost. |
| Local content | **3** | Steel spar can be fabricated locally. Ballast and reflectors local. Similar to Concept A for reflectors. |
| Deployment | **1** | Heavy (~2,500 kg). Must be towed horizontally then upended at site. Requires ballast flooding sequence or crane. Far exceeds 4-crew, 30-min target. Specialist operation. |
| Safety | **4** | Fully passive once deployed. Same safety profile as Concept A. |
| Risk | **2** | Spar buoy is proven technology BUT unfamiliar in VN defense context. Upending/deployment procedure is complex and risky in SS 4-5. No local precedent. |
| Production | **2** | Watertight cylinder fabrication is specialized. Ballast system adds complexity. Slower production rate than simple pontoon. |

#### Concept C: Multi-Hull Station Keeper — **60.0%** (REVIEW)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| RCS | **3** | Same reflectors as A, but catamaran cross-deck may cause structural reflections. Multi-hull geometry introduces unwanted RCS contributions. Achievable but requires RCS modeling. |
| Survivability | **3** | Catamaran has good stability. BUT: multi-point mooring prevents weathervaning → asymmetric storm loads. Higher risk of structural failure at hull-crossdeck connection in SS 6. |
| Cost | **2** | 2 hulls + cross-deck + 3 anchors + 3 mooring sets = $50-65K. Roughly 1.5-2× target. |
| Local content | **3** | HDPE hulls local. Steel cross-deck local. Same reflector supply chain as A. |
| Deployment | **1** | 3-point mooring deployment is complex. 3 anchors must be set accurately. Modular assembly adds time. Far exceeds 30-min target. Needs ship with crane. |
| Safety | **3** | Mostly passive, but AIS requires power. Multi-point mooring failure modes more complex than SPM. |
| Risk | **2** | Multi-point mooring in SS 5-6 is high risk. Cross-deck structural integrity critical. More failure modes than simple pontoon. |
| Production | **2** | 2 hulls per unit, plus cross-deck fabrication. More complex than single pontoon. |

#### Concept D: Active Signature Barge — **39.8%** (REJECT)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| RCS | **3** | Active transponder can produce any RCS value. BUT: "amplified" RCS may not match real ship signature characteristics (Doppler, glint, polarization). Military acceptance of "fake" RCS is questionable. |
| Survivability | **1** | Flat steel barge has poor stability in SS 5-6. Low freeboard = green water. Electronics vulnerable to immersion. **SHOWSTOPPER: score = 1 on critical criterion.** |
| Cost | **0** | $80-120K per unit. Active transponder ($30-50K), battery bank ($10K), electronics enclosure ($5K). Far exceeds $36K target. **SHOWSTOPPER: score = 0.** |
| Local content | **2** | Steel barge local, but active electronics (transponder, RF amplifier) fully imported. ~60% local at best. |
| Deployment | **3** | Simple tow and anchor. No mast erection needed. But electronics must be powered up and verified. |
| Safety | **2** | Active electronics = not fully passive. Battery bank = fire risk. RF emissions during engagement may interfere with missile seeker. |
| Risk | **2** | Active transponder acceptance by military is uncertain. EMC qualification required. Battery lifetime and reliability in marine environment. |
| Production | **2** | Electronics integration is specialized. RF calibration per unit. Lower production rate. |

### 5.5 Sensitivity Analysis

**What if weights change?**

| Scenario | Weight Shift | A Score | B Score | C Score | Winner |
|----------|-------------|---------|---------|---------|--------|
| **Base case** | As defined | **81.8%** | 65.0% | 60.0% | **A** |
| Survivability critical (+10%) | Surv 0.30, Cost 0.10, Deploy 0.05 | 79.3% | 72.5% | 60.0% | **A** |
| Cost critical (+10%) | Cost 0.25, Surv 0.15, Deploy 0.05 | 80.0% | 57.5% | 55.0% | **A** |
| Deployment critical (+10%) | Deploy 0.20, Surv 0.15, Risk 0.05 | 81.3% | 57.5% | 52.5% | **A** |
| Equal weights (all 12.5%) | All equal | 82.3% | 62.5% | 59.4% | **A** |

**Concept A wins in ALL weight scenarios.** The closest competitor (B: Spar Buoy) only approaches when survivability is heavily weighted, but its cost and deployment penalties keep it below 73%.

**Which criteria are decisive?**
- Cost (C3) is decisive: Concepts B, C, D cannot meet the $36K target
- Deployment (C5): Concepts B and C score 1 (showstopper-adjacent)
- Concept D has two showstoppers (survivability = 1, cost = 0)

---

## Step 6: Selection and Firm-Up

### 6.1 Selection Decision

```
╔═══════════════════════════════════════════════════════════════╗
║                  CONCEPT SELECTION DECISION                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  SELECTED: Concept A — "Baseline Optimized"                   ║
║                                                               ║
║  VDI 2225 Score: 81.8% (PROCEED)                              ║
║                                                               ║
║  Key advantages:                                              ║
║    1. Best RCS performance (4/4) — proven physics             ║
║    2. Best safety profile (4/4) — fully passive               ║
║    3. Meets cost target ($35.6K ≤ $36K)                       ║
║    4. Deployable by 4 crew in ≤30 min                         ║
║    5. 85-90% local content                                    ║
║    6. Lowest development risk (hybrid AM/CNC de-risked)       ║
║                                                               ║
║  Main risks:                                                  ║
║    1. Military AM acceptance (50% probability, HIGH impact)   ║
║    2. Mast structural performance in SS 6 (15%, MEDIUM)       ║
║    3. 8.0m HDPE hull fabrication method (TBD-007)             ║
║                                                               ║
║  Fallback: Concept A-CNC (same architecture, CNC-only        ║
║            reflectors at ±0.3° tolerance, $28.6K/unit,        ║
║            ~800-1,000 m² RCS — marginal but viable)           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### 6.2 Why Not the Others?

| Concept | Score | Elimination Reason |
|---------|-------|--------------------|
| **B: Spar Buoy** | 65.0% | Cost ($55-70K = 1.5-2× target), deployment complexity (upending, heavy), unfamiliar technology in VN |
| **C: Multi-Hull** | 60.0% | Cost ($50-65K), 3-point mooring complexity, no weathervaning in storms, deployment needs crane |
| **D: Active Barge** | 39.8% | **Two showstoppers:** cost = 0 ($80-120K), survivability = 1 (flat barge in SS 5-6). Not passive. |

### 6.3 Selected Concept — Preliminary Layout

```
CONCEPT A: PRELIMINARY LAYOUT (Rev B.1)
═══════════════════════════════════════════════════════

SIDE VIEW (Section through center):
                    GPS beacon (4.5m AGL)
                        │
                   ┌────┤────┐  Reflector (0.8m, 15 kg)
                   │    │    │  at 3-4m AGL
                   └────┤────┘
                        │     Steel mast (60mm×4mm,
                        │     ~3m above deck, 16 kg)
    ┌─R─┐              │              ┌─R─┐
    │   │   ┌──────────┤──────────┐   │   │
    │   │   │  deck (scuppers)    │   │   │
    └─┬─┘   │         pad        │   └─┬─┘
      │     │         eye        │     │
~~════╧═════╧═════════╧══════════╧═════╧════~~ waterline
    │ ████████████████████████████████████ │
    │ ████ HDPE hull (8.0m diameter) ████ │  0.5m depth
    │ ████ closed-cell foam fill ████████ │
    └────────────────┬───────────────────┘
                     │  chain (12-16mm G30, 30-50m)
                     │
                     │  polyester rode (20mm, 50-100m)
                     │
                     ⚓  Danforth/Bruce 30-50 kg

TOP VIEW:
                    N (0°)
                ┌─── R1 ───┐
               / │  mast   │ \
         R8 ─/   │         │   \─ R2
        /         GPS(4.5m)         \
       │                             │
  W ──R7     8.0m HDPE platform     R3── E
       │        ● pad eye            │
        \        (center)           /
         R6 ─\               /─ R4
               \             /
                └─── R5 ───┘
                    S (180°)

  8× masts in deck sockets at platform perimeter
  45° spacing, 2.01m clearance between reflectors
  Central pad eye for mooring attachment
  Scuppers around perimeter for self-draining

KEY DIMENSIONS:
  Platform diameter:     8.0 m
  Hull depth:            0.5 m
  Freeboard:            ~0.48 m (at 980 kg)
  Mast height:          ~3.0 m above deck
  Reflector center:      3.0-4.0 m AGL
  GPS beacon:           ≥4.5 m AGL
  Displacement:          980 kg
  Draft:                ~0.019 m (1.9 cm)
```

### 6.4 Architecture Summary (Selected)

| Layer | Component | Working Principle | Material | Mass |
|-------|-----------|-------------------|----------|------|
| **L0** | Storm mooring | P2.1: SPM catenary | Danforth + G30 chain + polyester rode | ~100 kg (in water) |
| **L1** | Flotation hull | P1.1: HDPE pontoon | HDPE rotomolded/welded + PU foam | ~350 kg |
| **L2** | Structural frame | Steel frame + pad eye | S235 galvanized mild steel | ~180 kg |
| **L2.5** | Mast system | P4.1: Fixed cantilever | Galvanized steel tube (60mm×4mm) | 128 kg (8×16 kg) |
| **L3** | Signature module | P3.1: Corner reflectors | CNC 6061-T6 faces + AM AlSi10Mg frames | 120 kg (8×15 kg) |
| **L3+** | Tracking beacon | P5.1: GPS satellite | COTS GPS + Li-ion battery | ~5 kg |
| | | | **Total displacement:** | **~980 kg** |

### 6.5 Phase 3 Entry Recommendations

Based on concept selection, Phase 3 (Embodiment Design) should prioritize:

| Priority | Task | TBD Reference | Risk Level |
|----------|------|---------------|------------|
| 1 | Mast structural design (free-standing vs guyed) | TBD-011 | MEDIUM |
| 2 | 8.0m HDPE hull fabrication method | TBD-007 | MEDIUM |
| 3 | Mooring catenary analysis (12mm vs 16mm chain) | TBD-011 | LOW |
| 4 | AM reflector prototype + RCS validation | TBD-003 | HIGH |
| 5 | Transport solution for 8.0m hull | TBD-008 | MEDIUM |
| 6 | Depth-dependent mooring kit variants | TBD-010 | LOW |

---

## Cross-References

- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1)
- [[../01_requirements/stakeholder_analysis.md]] — 10 stakeholders, RACI
- [[../00_odi/phase0_final_revision.md]] — Phase 0 final specs, cost model
- [[../00_odi/re_deep_analysis.md]] — Reflector physics, mooring analysis
- [[../00_odi/environmental_survivability.md]] — SS 5-6 analysis
- [[../00_odi/re_competitive_analysis.md]] — Competitive positioning
- [[../PROJECT_STATUS.md]] — Project status tracker
