---
project: VN-TGT-SEA-001
phase: 2
type: morphological_matrix
version: 1.0
created: 2026-02-10
status: draft
step: 4 of 6
---

# Step 4: Morphological Matrix & Concept Generation --- VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Combine working principles into complete concept variants using the morphological matrix, then describe each concept in sufficient detail for VDI 2225 evaluation.
**Method:** Pahl & Beitz morphological matrix (Zwicky box) with systematic concept path generation
**Input:** [[working_principles.md]] --- 6 sub-functions with 3-5 working principles each (Step 3)
**Output:** 4 concept variants with architecture descriptions, mass breakdowns, and cost estimates

---

## 1. Morphological Matrix

### 1.1 Matrix Construction

The matrix combines the 6 primary sub-functions (rows) from the function structure (Step 2) with the viable working principles (columns) identified in the working principles search (Step 3). Sub-function F7 (Withstand Environment) is treated as a cross-cutting design philosophy applied to all concepts rather than an independent row, because it does not represent a separate physical mechanism --- it is an attribute of how each sub-function is designed.

```
MORPHOLOGICAL MATRIX: VN-TGT-SEA-001
=========================================================================

              Sol 1 (P_.1)         Sol 2 (P_.2/3)       Sol 3 (P_.3/4)       Sol 4 (P_.4/5)
              ================     ================     ================     ================

F1: FLOAT     P1.1                 P1.3                 P1.4                 P1.5
              Solid HDPE           Catamaran            Spar buoy            Steel barge
              circular pontoon     (2x HDPE hulls       (vertical steel      (flat-bottom
              8.0m, foam-filled    + cross-deck)        cylinder, ballast)   6x3m welded)
              ----------------     ----------------     ----------------     ----------------
              TRL 9, LOW cost      TRL 9, MED cost      TRL 8, MED-HI       TRL 9, MED cost
              BM=210m, 980 kg      BM~40m, ~1,200 kg    BM~0.1m, ~2,500 kg  BM~3m, ~1,800 kg
              93% reserve buoy.    Good deck area        Min. waterplane      High payload
              Proven, simple       Complex structure     Best seakeeping      Corrosion-prone


F2: HOLD      P2.1                 P2.2                 P2.4                 ---
POSITION      Single-point         Multi-point          Deadweight
              mooring (SPM)        mooring (3-pt)       (concrete block)
              ----------------     ----------------     ----------------
              TRL 9, LOW cost      TRL 9, MED-HI       TRL 9, VERY LOW
              Weathervane 360d     Tight position       No setting needed
              Catenary absorbs     No weathervane       Poor SS 5-6 hold
              Pre-deployable       3x anchor complex    Harbor use only


F3: GENERATE  P3.1                 P3.2                 P3.3                 P3.4
RCS           Corner reflectors    Luneburg lens        Active radar         Flat plate
              (trihedral, 0.8m)    (graded dielectric   transponder          array (specular
              8x hybrid AM/CNC     sphere, ~0.5m dia)   (X-band amp.)       reflection)
              ----------------     ----------------     ----------------     ----------------
              TRL 9, MED cost      TRL 7, HIGH cost     TRL 8, V.HIGH       TRL 9, LOW cost
              152 m^2 each         Wide angle +-60d     Programmable RCS     ~2-3d beamwidth
              Broadband passive    Fewer units needed   NOT passive          No 360d coverage
              +/-0.1d ortho.       $5-10K each          EMC concerns         Calibration only


F4: SUPPORT   P4.1                 P4.2                 P4.3                 P4.4
              Fixed steel mast     Guyed mast           A-frame / tripod     Pedestal (low,
              in deck socket       (mast + cable        (3 legs, stable      <1m height)
              60mm x 4mm tube      stays, turnbuckles)  triangle geometry)
              ----------------     ----------------     ----------------     ----------------
              TRL 9, LOW cost      TRL 9, LOW cost      TRL 9, MED cost      TRL 9, V.LOW
              Simple, field-erect  60-80% less base M   Very stiff           Min. windage
              Cantilever: all M    More parts/rigging   Heavy, complex       Sea clutter
              at base (fatigue)    Longer erect time    Good fatigue life    Green water risk


F5: REPORT    P5.1                 P5.2                 P5.4                 ---
POSITION      GPS beacon           AIS transponder      Iridium satellite
              (satellite relay)    (VHF broadcast)      tracker
              ----------------     ----------------     ----------------
              TRL 9, MED cost      TRL 9, LOW cost      TRL 9, MED cost
              +-5m, 1 Hz, 72h     20 nm LOS only       5-15 min interval
              Global coverage      All ships see it     Global, compact
              $1,500-2,000         $300-500             $500 + $20/month


F6: DEPLOY    P6.1                 P6.3                 P6.4                 ---
              Surface tow          Helicopter           Ship crane
              (bridle + drogue)    (sling load)         (davit launch)
              ----------------     ----------------     ----------------
              TRL 9, LOW cost      TRL 8, HIGH cost     TRL 9, MED cost
              Any tug/workboat     Fast, all-weather    Controlled launch
              SS 4-5, 3-5 kn       Weight < 2,000 kg    Needs crane vessel
              Simple, proven       $10-20K per deploy   Assembly on deck

=========================================================================
```

### 1.2 Matrix Summary Table

| Sub-Function | Sol 1 | Sol 2 | Sol 3 | Sol 4 |
|---|---|---|---|---|
| **F1: Float** | P1.1 Solid HDPE pontoon | P1.3 Catamaran | P1.4 Spar buoy | P1.5 Steel barge |
| **F2: Hold position** | P2.1 Single-point mooring | P2.2 Multi-point (3-pt) | P2.4 Deadweight | --- |
| **F3: Generate RCS** | P3.1 Corner reflectors | P3.2 Luneburg lens | P3.3 Active transponder | P3.4 Flat plates |
| **F4: Support** | P4.1 Fixed mast | P4.2 Guyed mast | P4.3 A-frame / tripod | P4.4 Pedestal (low) |
| **F5: Position** | P5.1 GPS beacon | P5.2 AIS | P5.4 Iridium tracker | --- |
| **F6: Deploy** | P6.1 Surface tow | P6.3 Helicopter | P6.4 Ship crane | --- |

**Matrix size:** 6 rows x 3-4 columns = theoretical 4 x 3 x 4 x 4 x 3 x 3 = 1,728 combinations. Most are physically incompatible or obviously inferior. Systematic compatibility screening (Step 3, Section 4) reduces to 4 viable concept paths.

---

## 2. Concept Paths Through the Matrix

### 2.1 Path Diagram

```
CONCEPT PATHS THROUGH MORPHOLOGICAL MATRIX
==========================================================================

         F1           F2           F3           F4           F5           F6
         Float        Hold         RCS          Support      Position     Deploy
         ----------   ----------   ----------   ----------   ----------   ----------
         P1.1 P1.3    P2.1 P2.2   P3.1 P3.2    P4.1 P4.2    P5.1 P5.2   P6.1 P6.3
         P1.4 P1.5    P2.4        P3.3 P3.4    P4.3 P4.4    P5.4        P6.4

Con A:  [P1.1]------[P2.1]------[P3.1]------[P4.1]------[P5.1]------[P6.1]
         HDPE         SPM          Corner       Fixed        GPS          Surface
         pontoon      anchor       reflectors   mast         beacon       tow
                                   (8x 0.8m)   (8x steel)

Con B:           [P1.4]------[P2.1]------[P3.1]------[P4.3]------[P5.1]------[P6.1]
                  Spar         SPM          Corner       A-frame      GPS          Surface
                  buoy         anchor       reflectors   tripod       beacon       tow
                                            (4-6x 0.8m)

Con C:       [P1.3]------[P2.2]------[P3.1]------[P4.2]------[P5.2]------[P6.4]
              Catamaran    Multi-pt     Corner       Guyed        AIS          Ship
              twin-hull    3 anchors    reflectors   mast         transpdr.    crane
                                        (4-8x 0.8m)

Con D:                                   [P1.5]------[P2.1]------[P3.3]------[P4.4]------[P5.1]------[P6.1]
                                          Steel        SPM          Active       Pedestal     GPS          Surface
                                          barge        anchor       transpndr    (low)        beacon       tow

==========================================================================

LEGEND:  [P_._ ]  = Selected working principle for that sub-function
         ------   = Connection path through matrix
```

### 2.2 Path Selection Rationale

| Concept | Philosophy | Why This Path? |
|---|---|---|
| **A: Baseline Optimized** | Proven, balanced, lowest risk | Combines the primary-selected principles from Step 3. Best-understood path. Directly continues Rev B.1 architecture. |
| **B: Spar Buoy** | Maximum seakeeping | Explores what happens when heavy-weather performance (F1) is maximized. Spar buoy is the offshore industry gold standard for wave survival. |
| **C: Multi-Hull Station Keeper** | Maximum position accuracy | Explores tight position-holding (F2) via multi-point mooring combined with catamaran stability. Represents a "naval platform" approach. |
| **D: Active Signature Barge** | Maximum RCS flexibility | Explores what happens when signature control (F3) is maximized via active electronics. Represents the "electronic warfare" approach. |

---

## 3. Detailed Concept Descriptions

### 3.1 Concept A: "Baseline Optimized" (Current Rev B.1)

**Philosophy:** Minimum-risk, maximum-value path using proven marine engineering with targeted AM innovation only where it creates decisive advantage (reflector orthogonality). Every component has TRL 9 except the AM mounting frames (TRL 7-8 for this application).

**Selected path:** F1-P1.1 + F2-P2.1 + F3-P3.1 + F4-P4.1 + F5-P5.1 + F6-P6.1

#### Architecture Description

The target is a single circular HDPE pontoon (8.0 m diameter) filled with closed-cell polyurethane foam, providing unsinkable flotation with >93% reserve buoyancy. Eight galvanized steel masts (60 mm OD x 4 mm wall, ~3 m above deck) are inserted into welded flange-plate deck sockets at the platform perimeter, spaced at 45-degree intervals. Each mast carries one hybrid AM/CNC trihedral corner reflector (0.8 m edge length, 15 kg) producing 152.3 m-squared RCS per reflector. The array of 8 reflectors provides 1,218 m-squared peak and approximately 1,050 m-squared average RCS through 360 degrees. A GPS beacon with 72-hour Li-ion battery is mounted at the top of the tallest mast (>=4.5 m AGL). The platform is moored via a single-point mooring (SPM) system --- a central pad eye connected through a fairlead to a catenary chain/rode leading to a Danforth or Bruce anchor on the seabed. The SPM allows full 360-degree weathervaning, minimizing storm loads. Deployment is by surface tow using a 2-point bridle and stabilizing drogue.

#### Layout Diagram

```
CONCEPT A: "BASELINE OPTIMIZED" (Rev B.1)
==========================================================================

SIDE VIEW (Section through center, looking East):
                                                           GPS beacon
                                                           (4.5m AGL)
                                                              |
                    Reflector R1                              |
                    (0.8m edge,    Reflector R5               |
                     15 kg)        (0.8m edge)               /|\
                   /=========\    /=========\               / | \
                  / 3-bounce  \  / 3-bounce  \             /  |  \
                 /  retro-     \/  retro-     \           /   |   \
                 \  reflect   /\   reflect   /         (antenna)
                  \=========/ || \=========/
                      |       ||      |
                      |   3m  ||  3m  |         Steel mast
                      |  mast ||  mast|         60mm OD x 4mm wall
                      |       ||      |         Galvanized
                      |       ||      |
      +---+-----------+--+----++---+--+----------+---+
      |scup|  deck socket |  pad   |  deck socket |scup|    Deck level
      |per |  (flange     |  eye   |  (flange     |per |    (+0.48m AGL)
      +----+--------------+--------+--------------+----+
      |=============================================|
      | ####  HDPE hull (8.0m diameter)  ########## |    Hull: 0.5m depth
      | ####  closed-cell PU foam fill  ########### |    Draft: ~0.019m
      | ####  (unsinkable)  ######################## |
      |=============================================|
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~ waterline
                                    |
                  Fairlead          | Swivel
                                    |
                                    |  12-16mm G30 galv. chain
                                    |  (length = 3-5x water depth)
                                    |
                                    |  20mm polyester rode
                                    |  (remainder of scope)
                                    |
                                    |  Scope 5:1 to 7:1
                                    |
                                   /_\  Danforth/Bruce anchor
                                  /___\ 30-50 kg (depth-dependent)
      ========================================= seabed (10-80m depth)


TOP VIEW:
                         N (0 deg)
                      .---R1---.
                    /  |  mast  |  \
                  /    | 60x4mm |    \
          R8---/       |        |      \---R2
          mast         |        |          mast
         /             |        |             \
        |              |  GPS   |              |
   W-- R7              | beacon |              R3 --E
        |              |(4.5m)  |              |
         \             |        |             /
          R6---\       | center |      /---R4
                  \    |pad eye |    /
                    \  |  *     |  /
                      '---R5---'
                         S (180 deg)

        Diameter: 8.0 m
        Reflector spacing: 45 deg (pi x 8.0 / 8 = 3.14m arc)
        Reflector envelope: ~1.13m diagonal
        Clearance between reflectors: 3.14 - 1.13 = 2.01m
        Mast sockets: 8x welded flange plates at perimeter
        Pad eye: center of deck, SWL 4,536 kgf
        Scuppers: 8x between mast positions, self-draining

==========================================================================
```

#### Component List and Mass Breakdown

| # | Component | Material | Qty | Unit Mass | Total Mass | Notes |
|---|---|---|---|---|---|---|
| 1 | HDPE pontoon hull (8.0m) | HDPE (rotomolded or welded) | 1 | 200 kg | 200 kg | 0.5m depth, circular |
| 2 | Closed-cell PU foam fill | Polyurethane 32 kg/m3 | 1 lot | 100 kg | 100 kg | Fill ~3.1 m3 void |
| 3 | Steel frame + pad eye | S235 galvanized mild steel | 1 | 150 kg | 150 kg | Ring + radial + center pad eye |
| 4 | Deck sockets (mast base) | S235 galvanized, flange plate | 8 | 4 kg | 32 kg | Welded to frame, bolted interface |
| 5 | Scuppers / drain fittings | HDPE / stainless | 8 | 0.5 kg | 4 kg | Self-draining deck |
| 6 | Steel masts (60mm x 4mm) | Galvanized steel tube | 8 | 16 kg | 128 kg | ~3m length, top plate for reflector |
| 7 | Corner reflectors (0.8m hybrid) | CNC 6061-T6 faces + AM AlSi10Mg frame | 8 | 15 kg | 120 kg | 3x face plates + 1x AM frame each |
| 8 | GPS beacon + Li-ion battery | COTS electronics | 1 | 5 kg | 5 kg | 72h, +-5m, 1 Hz, satellite relay |
| 9 | GPS mast extension | Galv. steel tube | 1 | 3 kg | 3 kg | Extends above reflectors to >=4.5m |
| 10 | Mooring hardware (on hull) | Galv. steel (shackle, swivel, fairlead) | 1 set | 8 kg | 8 kg | Connects pad eye to chain |
| 11 | Tow bridle + drogue | Dyneema line + fabric drogue | 1 set | 10 kg | 10 kg | 2-point bridle, SWL 7,524 kgf |
| 12 | Fasteners, safety wire | SS 316, Nylock | 1 lot | 5 kg | 5 kg | All bolts secured against vibration |
| 13 | Marine coatings | Epoxy + antifouling | 1 lot | 15 kg | 15 kg | Steel frame and mast protection |
| | | | | **TOTAL PLATFORM:** | **780 kg** | |
| | | | | | | |
| 14 | Anchor (Danforth/Bruce) | Galv. steel | 1 | 30-50 kg | 40 kg | Depth-dependent selection |
| 15 | Chain (12-16mm G30) | Galv. steel | 30-50 m | 3-6 kg/m | 120 kg | Bottom section of mooring line |
| 16 | Polyester rode (20mm) | Polyester braid | 50-100 m | 0.4 kg/m | 40 kg | Upper section, shock absorption |
| | | | | **TOTAL MOORING:** | **200 kg** | |
| | | | | | | |
| | | | | **TOTAL DISPLACEMENT:** | **~980 kg** | At deployed waterline |

#### Estimated Unit Cost (@ 10 units)

| Subsystem | Cost | % of Total |
|---|---|---|
| HDPE pontoon (8.0m) | $6,500 | 18.2% |
| Closed-cell foam fill | $1,000 | 2.8% |
| Steel frame + pad eye + sockets | $3,000 | 8.4% |
| Mast system (8x galv. steel + hardware) | $1,430 | 4.0% |
| Hybrid reflectors (8x: CNC faces + AM frames + QC) | $13,000 | 36.5% |
| Storm mooring system (anchor + chain + rode + HW) | $1,650 | 4.6% |
| GPS beacon (72h battery) | $1,800 | 5.1% |
| Tow equipment (bridle + drogue) | $400 | 1.1% |
| Assembly + QC + coatings | $4,000 | 11.2% |
| Margin (10%) | $2,860 | 8.0% |
| **TOTAL** | **$35,640** | **100%** |

#### Key Advantages

1. **Proven architecture** --- Every subsystem except AM reflector frames uses TRL 9 marine technology. The design has been iterated through Phase 0 and Phase 1 with detailed engineering analysis at each step.
2. **Best RCS performance** --- 8 x 0.8m hybrid reflectors deliver 1,218 m-squared peak, ~1,050 m-squared average, ~770 m-squared minimum. This is the only concept that achieves >1,000 m-squared average with high confidence.
3. **Fully passive / radar-only** --- No electronics except GPS beacon. No C2 link. No fuel, propane, or batteries (aside from GPS). Best-in-class safety with 5+ km clearance.
4. **Lowest cost** --- $35,640 at 10 units. Meets the $36K target. 85-90% local content.
5. **Simplest deployment** --- 4 crew, <=30 min. Pre-deploy mooring in fair weather. Tow target to mooring, connect, erect masts (socket insert), depart.

#### Key Disadvantages / Challenges

1. **AM frame supply chain** --- AM AlSi10Mg frames must be imported from ASEAN bureau. 3-week lead time per batch. Single-source risk unless multiple AM suppliers are qualified.
2. **8.0m HDPE hull fabrication** --- Exceeds standard rotomold capacity. May require multi-section welding or custom mold. TBD-007 to be resolved in Phase 3.
3. **Mast fatigue in storm** --- 60mm x 4mm galv. tube cantilever at 3m height. 18% margin on bending (1,303 N-m allowable vs 1,100 N-m required). Fatigue life at 40,000+ wave cycles needs Phase 3 validation. Weld quality at flange socket is critical.
4. **High tow drag** --- 8.0m diameter flat pontoon has significant tow resistance. Limited to 3-5 kn tow speed. Drogue required for yaw stability.
5. **Transport to port** --- 8.0m diameter may require oversize road transport or multi-section hull with field assembly.

#### Compatibility Check

All interfaces verified in Step 3 (working_principles.md, Section 4):
- P1.1 + P2.1: Standard SPM on circular pontoon. Central pad eye. COMPATIBLE.
- P1.1 + P4.1: Deck sockets welded to steel frame on HDPE hull. COMPATIBLE.
- P3.1 + P4.1: Reflector bolted to mast top plate, alignment via AM pins. COMPATIBLE.
- P2.1 + P4.1: SPM weathervaning means masts see equal loading from all directions. COMPATIBLE.
- P5.1 + P4.1: GPS beacon on tallest mast, unobstructed sky view. COMPATIBLE.
- P6.1 + P1.1: Bridle on hull tow points. High drag but acceptable at 3-5 kn. COMPATIBLE.

**No interface conflicts detected.**

---

### 3.2 Concept B: "Spar Buoy"

**Philosophy:** Maximize heavy-weather performance by minimizing waterplane area. The spar buoy form is the offshore industry standard for extreme sea states (SS 7+). This concept sacrifices simplicity, cost, and deployment ease for the best possible seakeeping.

**Selected path:** F1-P1.4 + F2-P2.1 + F3-P3.1 + F4-P4.3 + F5-P5.1 + F6-P6.1

#### Architecture Description

The target is a vertical steel cylinder (spar) approximately 1.5 m diameter and 6 m tall. The lower 4.5-5.0 m is submerged, with concrete or steel ballast in the bottom compartment providing a very low center of gravity. The minimal waterplane area (1.77 m-squared vs 50.3 m-squared for Concept A) means wave-induced heave and pitch motions are extremely small, even in SS 6+. An A-frame tripod structure sits on top of the spar, supporting 4-6 corner reflectors (0.8 m edge) at 4-6 m above the waterline. A GPS beacon is integrated at the apex. The spar is moored via SPM with a chain catenary. Deployment involves towing the spar horizontally to the site, then upending it by flooding ballast tanks or using a crane. This upending procedure is the most complex and risky aspect of the concept.

#### Layout Diagram

```
CONCEPT B: "SPAR BUOY"
==========================================================================

SIDE VIEW:
                           GPS beacon (6m AGL)
                              |
                         /----|----\
                        / Reflector \       4-6x corner reflectors
                       /  R1  R2 R3  \      (0.8m edge, 15 kg each)
                      /    (0.8m)     \     mounted on A-frame tripod
                     /                 \    at 4-6m above waterline
                    /     A-frame       \
                   /      tripod         \
                  /       structure       \
                 /________________________\
                |                          |
                |   Access hatch           |    Freeboard: ~1.0m
                |   (battery, mooring HW)  |
 ~~~~~~~~~~|~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~|~~~~~~~~~ waterline
                |                          |
                |                          |
                |    Watertight steel       |    Cylinder: 1.5m dia
                |    cylinder              |    Wall: 8-10mm steel
                |    (buoyancy chamber)    |    Length: 6.0m total
                |                          |    Submerged: ~5.0m
                |                          |
                |                          |
                |                          |
                |                          |
                |========================= |
                |  Concrete / steel        |    Ballast compartment
                |  ballast (~800 kg)       |    lowers CG for stability
                |  (bottom 1.0-1.5m)       |
                |__________________________|
                          |
                     chain + rode
                         /_\
                        /___\ anchor

TOP VIEW (at reflector level):

              Reflector R1 (0.8m)
                  |
           R6----+----R2         6 reflectors at 60 deg spacing
           |    / \    |         (or 4 at 90 deg spacing)
           |   / A \   |
           |  /frame\  |
           | /  top  \ |
           R5---------R3
                  |
                  R4

     A-frame base: ~1.5m triangle inscribed in spar diameter
     Reflector radius: ~1.2m from center
     Reflector spacing (6 units): 60 deg = less overlap than 8 at 45 deg

TOP VIEW (at waterplane):

           .-----------.
          /             \
         /               \
        |    1.5m dia     |       A_wp = pi/4 * 1.5^2 = 1.77 m^2
        |    waterplane   |       (vs 50.3 m^2 for Concept A)
        |                 |
         \               /
          \             /
           '-----------'

==========================================================================
```

#### Component List and Mass Breakdown

| # | Component | Material | Qty | Unit Mass | Total Mass | Notes |
|---|---|---|---|---|---|---|
| 1 | Steel cylinder (1.5m x 6.0m) | Marine steel S355, 8-10mm wall | 1 | 850 kg | 850 kg | Watertight compartments, hatches |
| 2 | Concrete ballast | Concrete (2,400 kg/m3) | 1 lot | 800 kg | 800 kg | Bottom 1.0-1.5m of cylinder |
| 3 | A-frame tripod | Galvanized steel tube, 50mm x 3mm | 1 | 60 kg | 60 kg | 3-leg structure on spar top |
| 4 | Corner reflectors (0.8m) | CNC 6061-T6 + AM AlSi10Mg | 4-6 | 15 kg | 75 kg | Mounted on A-frame apexes |
| 5 | GPS beacon + battery | COTS electronics | 1 | 5 kg | 5 kg | 72h, satellite relay |
| 6 | Mooring hardware (on spar) | Galv. steel | 1 set | 20 kg | 20 kg | Chain stopper, fairlead |
| 7 | Ballast tank fittings | Steel valves, flooding ports | 1 set | 30 kg | 30 kg | For upending procedure |
| 8 | Internal framing / bulkheads | Marine steel, 6mm | 1 lot | 150 kg | 150 kg | 2-3 watertight bulkheads |
| 9 | Marine coatings (epoxy + AF) | Marine paint system | 1 lot | 25 kg | 25 kg | Full immersion protection |
| 10 | Cathodic protection anodes | Zinc anodes | 4 | 5 kg | 20 kg | Sacrificial corrosion protection |
| 11 | Tow bridle / tow point | Steel lugs + Dyneema | 1 set | 15 kg | 15 kg | For horizontal tow |
| | | | | **TOTAL SPAR:** | **~2,050 kg** | (dry, without mooring) |
| | | | | | | |
| 12 | Anchor (Bruce, 50-70 kg) | Galv. steel | 1 | 60 kg | 60 kg | Heavier than Concept A |
| 13 | Chain (16mm G30) | Galv. steel | 40-60 m | 6 kg/m | 300 kg | Must handle heavier spar |
| 14 | Polyester rode (24mm) | Polyester braid | 60-100 m | 0.6 kg/m | 48 kg | Heavier rode needed |
| | | | | **TOTAL MOORING:** | **~408 kg** | |
| | | | | | | |
| | | | | **TOTAL DISPLACEMENT:** | **~2,500 kg** | At deployed waterline |

#### Estimated Unit Cost (@ 10 units)

| Subsystem | Cost | Notes |
|---|---|---|
| Steel cylinder fabrication | $15,000-20,000 | Watertight welding, pressure test, hatches |
| Concrete ballast + installation | $1,500 | Pour in controlled environment |
| A-frame tripod | $2,500 | Custom fabrication, galvanized |
| Reflectors (4-6x hybrid) | $7,200-10,800 | Same hybrid AM/CNC as Concept A |
| GPS beacon | $1,800 | Same as Concept A |
| Ballast tank fittings | $3,000 | Valves, flooding system |
| Internal structure / bulkheads | $4,000 | Watertight compartment fabrication |
| Marine coatings + cathodic protection | $3,000 | Full immersion system |
| Storm mooring (heavier spec) | $2,500 | Larger anchor + heavier chain |
| Tow equipment | $500 | Horizontal tow bridle |
| Assembly + QC + pressure testing | $8,000 | Extensive testing required |
| Margin (15% --- higher risk) | $7,500-9,000 | More unknowns |
| **TOTAL** | **$57,000-68,000** | **$55,000-70,000 range** |

#### Key Advantages

1. **Best seakeeping** --- Spar buoys are proven in the offshore oil industry for decades at SS 7+. Minimal waterplane area means heave response amplitude operator (RAO) is near zero. Platform roll/pitch is <+-2 degrees in SS 6 (vs +-5 degrees for Concept A).
2. **Excellent reflector stability** --- Minimal platform motion means reflectors maintain orthogonality with extremely low dynamic RCS variation (<0.5 dB loss from motion vs <1.0 dB for Concept A).
3. **Natural weathervaning** --- SPM mooring with deep draft provides strong self-aligning torque.
4. **High reflector elevation** --- 4-6 m AGL provides excellent radar horizon and reduces sea clutter interference.

#### Key Disadvantages / Challenges

1. **Heavy (2,500 kg)** --- 2.5x the mass of Concept A. Requires larger tug, more fuel, harder to handle.
2. **Complex deployment** --- Must be towed horizontally (cannot tow upright safely), then upended at site by controlled ballast flooding or crane lift. This is a specialist operation requiring trained crew and specific equipment. Far exceeds the 4-crew, 30-min target.
3. **Expensive ($55-70K)** --- 1.6-2.0x the cost target. Watertight cylinder fabrication, pressure testing, ballast system all add cost.
4. **Fewer reflectors** --- A-frame top has limited mounting area. 4-6 reflectors at 0.8m edge = fewer than 8. At 6 reflectors (60-degree spacing), 360-degree RCS coverage has +-4-5 dB variation vs +-2 dB for Concept A. At 4 reflectors, coverage becomes unacceptable.
5. **Corrosion management** --- Full steel immersion requires extensive coating system plus cathodic protection. Annual maintenance needed vs near-zero for HDPE.

#### Compatibility Check

- P1.4 + P2.1: SPM works well with spar. Natural weathervaning. COMPATIBLE.
- P1.4 + P4.3: A-frame mounts on spar top cap. COMPATIBLE but space-limited.
- P3.1 + P4.3: Reflectors on A-frame legs/apex. COMPATIBLE but fewer units (4-6 vs 8).
- P5.1 + P4.3: GPS at A-frame apex. COMPATIBLE.
- P6.1 + P1.4: Horizontal tow COMPATIBLE but requires upending procedure at site. **INTERFACE RISK: Upending is the critical operational challenge.**

**One interface concern:** The upending procedure (F6 to F1 transition) is complex and requires specialist equipment or flooding controls. This is not a physical incompatibility but an operational complexity that must be planned for.

---

### 3.3 Concept C: "Multi-Hull Station Keeper"

**Philosophy:** Maximize position accuracy by using a multi-point mooring system, combined with a catamaran hull for stability and deck area. This concept represents a "naval platform" approach --- tighter position control, conventional hull form, modular construction --- at the expense of deployment complexity and storm survivability.

**Selected path:** F1-P1.3 + F2-P2.2 + F3-P3.1 + F4-P4.2 + F5-P5.2 + F6-P6.4

#### Architecture Description

The target uses a catamaran hull --- two HDPE cylindrical pontoons (1.2 m diameter x 8 m long) connected by a galvanized steel cross-deck frame. The wide beam (~4 m between hull centers) provides good initial stability. Four to eight corner reflectors (0.8 m edge) are mounted on guyed masts, with cable stays running to deck padeyes to reduce base bending moments. A 3-point mooring system (3 anchors at 120-degree spacing) restricts the target to a small watch circle (+-10-20 m) but prevents weathervaning. An AIS transponder provides position data to shore (lower cost but line-of-sight only). Deployment requires a ship with crane capability to lower the assembled catamaran onto the water and set three separate anchor legs.

#### Layout Diagram

```
CONCEPT C: "MULTI-HULL STATION KEEPER"
==========================================================================

SIDE VIEW (Section through cross-deck, looking forward):

          R1 (guyed mast)            R2 (guyed mast)
          /=========\                /=========\
         / reflector  \              / reflector  \
         \   0.8m    /              \   0.8m    /
          \=========/                \=========/
              |                          |
         3m  |  cable stays    cable stays  |  3m
              |  /   \          /   \       |
              | /     \        /     \      |
              |/       \      /       \     |
     +--------+---------+----+---------+--------+
     |  cross-deck (galv. steel frame)           |    Cross-deck: ~1.0m
     |  (4.0m wide x 8.0m long)                 |    above waterline
     +----+----------------------------------+---+
          |                                  |
          |  HDPE hull 1                     |  HDPE hull 2
          |  (1.2m dia x 8.0m)              |  (1.2m dia x 8.0m)
 ~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~ waterline
          |                                  |
          |  foam-filled                     |  foam-filled
          |  (unsinkable)                    |  (unsinkable)
          |__________________________________|

                Mooring legs (3x)
               /        |        \
              /         |         \
          anchor 1   anchor 2   anchor 3
          (120 deg spacing)


TOP VIEW:
                              N
                              |
                    .----R1---|---R2----.
                   /     mast |   mast  \
                  /       |   |   |      \
          +------/--------+---+---+-------\------+
          |     /  cross-deck frame       |\     |
          |    /                           | \   |
     W ---+ R5|     AIS antenna            |R3 +--- E
          |    \                           | /   |
          |     \                         |/     |
          +------\--------+---+---+------/-------+
                  \       |   |   |     /
                   \     R6---|---R4   /
                    '---------|-------'
                              |
                              S
         ==== hull 1 ====   ==== hull 2 ====
          (1.2m x 8.0m)     (1.2m x 8.0m)

         Hull spacing (center-center): 4.0m
         Overall beam: ~5.2m
         Overall length: 8.0m
         6 reflectors on 6 guyed masts (60 deg spacing)
         3 mooring lines at 120 deg from cross-deck corners

==========================================================================
```

#### Component List and Mass Breakdown

| # | Component | Material | Qty | Unit Mass | Total Mass | Notes |
|---|---|---|---|---|---|---|
| 1 | HDPE hull pontoons (1.2m x 8m) | HDPE (rotomolded or welded) | 2 | 120 kg | 240 kg | Cylindrical, foam-filled |
| 2 | Closed-cell PU foam fill | Polyurethane 32 kg/m3 | 2 lots | 30 kg | 60 kg | Fill hull voids |
| 3 | Cross-deck frame | S235 galv. steel, box section | 1 | 250 kg | 250 kg | 4.0m x 8.0m, bolted to hulls |
| 4 | Hull-to-frame brackets | S235 galv. steel | 8 | 5 kg | 40 kg | Bolted saddle clamps |
| 5 | Guyed masts (50mm x 3mm) | Galv. steel tube | 6 | 10 kg | 60 kg | Shorter than Concept A (stays share load) |
| 6 | Cable stays + turnbuckles | SS 316 wire rope, 6mm | 18 | 2 kg | 36 kg | 3 stays per mast |
| 7 | Corner reflectors (0.8m) | CNC 6061-T6 + AM AlSi10Mg | 4-8 | 15 kg | 90 kg | 6 reflectors baseline |
| 8 | AIS transponder + antenna | COTS marine electronics | 1 | 3 kg | 3 kg | Class B, $300-500 |
| 9 | AIS battery pack | Li-ion, 72h | 1 | 4 kg | 4 kg | Power for AIS transmission |
| 10 | Mooring hardware (3 sets) | Galv. steel | 3 sets | 10 kg | 30 kg | Bridle points, fairleads |
| 11 | Marine coatings | Epoxy + antifouling | 1 lot | 20 kg | 20 kg | Cross-deck frame protection |
| 12 | Fasteners, safety wire | SS 316, Nylock | 1 lot | 7 kg | 7 kg | Bolted assembly |
| | | | | **TOTAL PLATFORM:** | **~840 kg** | |
| | | | | | | |
| 13 | Anchors (Danforth, 30 kg each) | Galv. steel | 3 | 30 kg | 90 kg | 3-point mooring |
| 14 | Chain (12mm G30) | Galv. steel | 3 x 30m | 3 kg/m | 270 kg | 3 legs |
| 15 | Polyester rode (20mm) | Polyester braid | 3 x 60m | 0.4 kg/m | 72 kg | 3 legs |
| | | | | **TOTAL MOORING:** | **~432 kg** | 3x the mooring hardware |
| | | | | | | |
| | | | | **TOTAL DISPLACEMENT:** | **~1,270 kg** | Heavier than A due to 3x mooring |

#### Estimated Unit Cost (@ 10 units)

| Subsystem | Cost | Notes |
|---|---|---|
| HDPE hulls (2x 1.2m x 8m) | $5,000 | Smaller but two units |
| Foam fill (2x) | $600 | Less volume than Concept A |
| Cross-deck frame (steel) | $6,000 | Custom fabrication, galvanized |
| Hull-to-frame brackets | $1,500 | 8 saddle clamps, machined |
| Guyed masts + stays + turnbuckles | $2,400 | 6 masts + 18 stays |
| Reflectors (6x hybrid) | $9,750 | Same unit cost, fewer units |
| AIS transponder + battery | $800 | Lower cost than GPS beacon |
| Mooring system (3x complete sets) | $4,950 | 3 anchors + 3 chain legs + 3 rode legs |
| Marine coatings | $1,500 | Frame protection |
| Assembly + QC | $6,000 | More complex modular assembly |
| Transport (wider load) | $1,500 | Oversize: 5.2m beam |
| Margin (12%) | $4,800 | |
| **TOTAL** | **$44,800-58,000** | **$50,000-65,000 range** |

#### Key Advantages

1. **Tight position holding** --- 3-point mooring restricts watch circle to +-10-20 m (vs +-70-240 m for SPM). Beneficial if test range requires precise target positioning relative to fixed instrumentation.
2. **Good static stability** --- Catamaran beam provides high BM (~40 m) with reasonable displacement. Good deck area for equipment mounting.
3. **Modular construction** --- Hulls, cross-deck, masts are separate modules. Can be transported individually and assembled at port or on ship deck.
4. **Lower mast loads** --- Guyed masts transfer 60-80% of bending to cable stays, reducing base moment significantly. Lighter mast sections possible.

#### Key Disadvantages / Challenges

1. **No weathervaning** --- 3-point mooring prevents rotation. In SS 5-6 with shifting wind, the catamaran experiences asymmetric wave/wind loads. Cross-deck structural fatigue at hull connections becomes critical. This is a significant storm-survivability concern.
2. **3x deployment complexity** --- Three anchors must be set at precise 120-degree spacing. Each anchor requires a separate setting pass by the workboat. Total deployment time is 2-4 hours (vs 30 min for Concept A). Requires skilled crew.
3. **Higher cost** --- $50-65K. Three mooring sets, cross-deck fabrication, and 2 hulls all add cost.
4. **AIS line-of-sight limitation** --- AIS transponder only works within ~20 nm of shore or ship. For deep-water test ranges beyond 20 nm, position reporting fails. This is a significant limitation for some operational scenarios (requirement SIG-008 specifies >=99% availability).
5. **Cross-deck fatigue** --- The hull-to-crossdeck connection experiences large cyclic loads in beam seas. Bolted joints must be designed for fatigue, adding weight and cost. This is the structural weak point of the catamaran concept.

#### Compatibility Check

- P1.3 + P2.2: Catamaran with 3-point mooring is standard practice for floating platforms. COMPATIBLE.
- P1.3 + P4.2: Guyed masts on cross-deck. COMPATIBLE but cable stays add deck clutter.
- P3.1 + P4.2: Reflectors on guyed masts. COMPATIBLE. Stays do not obstruct radar.
- P2.2 + weather: No weathervaning. **INTERFACE RISK: Asymmetric storm loads on cross-deck in SS 5-6.** Multi-point mooring in open sea with shifting conditions is riskier than SPM.
- P5.2 + operational range: AIS is line-of-sight only. **INTERFACE RISK: If test range is >20 nm from any receiver, position reporting fails.** Mitigation: add GPS beacon as backup ($1,500 additional cost).
- P6.4 + P1.3: Ship crane launch of catamaran modules. COMPATIBLE but requires crane-equipped vessel.

**Two interface concerns identified:** Asymmetric storm loads (F2-to-F1) and AIS range limitation (F5 operational).

---

### 3.4 Concept D: "Active Signature Barge"

**Philosophy:** Maximize RCS flexibility by using an active radar transponder instead of passive reflectors. This allows programmable RCS at any level, any frequency, and in a compact form factor. The tradeoff is fundamental: abandoning passive operation for electronic sophistication.

**Selected path:** F1-P1.5 + F2-P2.1 + F3-P3.3 + F4-P4.4 + F5-P5.1 + F6-P6.1

#### Architecture Description

The target is a flat-bottom welded steel barge (6 m x 3 m) carrying an active radar transponder system. The transponder receives incoming X-band radar illumination, amplifies it electronically, and retransmits at a calibrated power level to produce a programmable RCS (100 to 10,000 m-squared, adjustable). The compact electronics package sits on a low pedestal (<1 m) on the barge deck, protected by a watertight enclosure. A battery bank provides 72-hour operation. GPS beacon is integrated with the transponder's electronics suite. Mooring is SPM, and deployment is by surface tow --- both straightforward. The barge form is the simplest possible hull, but it provides poor seakeeping in high sea states due to flat-bottom slamming, low freeboard, and no foam safety fill.

#### Layout Diagram

```
CONCEPT D: "ACTIVE SIGNATURE BARGE"
==========================================================================

SIDE VIEW:

                   X-band antenna (receive + transmit)
                         |
                    +----|----+
                    | Radome  |      Watertight RF enclosure
                    | (fiber- |      on low pedestal (~0.8m)
                    | glass)  |
                    +----+----+
                         |
           +----+--------+--------+----+
           |GPS |  Electronics box     |    |    Deck level
           |ant |  +-----------------+ |    |    (+0.3m freeboard)
           |    |  | X-band amp.     | |    |
           |    |  | Controller      | |    |
           |    |  | Battery bank    | |    |
           |    |  | (Li-ion, 72h)   | |    |
           |    |  +-----------------+ |    |
           +----+-----------+----------+----+
           |    welded steel barge (6.0m x 3.0m)    |    Steel: 6mm plate
           |    flat bottom, 0.5m depth              |    No foam fill
           |    displacement ~1,800 kg               |
           +-------------------+--------------------+
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~ waterline
                                  |                      Draft: ~0.10m
                             chain + rode
                                 /_\
                                /___\ anchor (SPM)


TOP VIEW:

           +----------------------------------------------+
           |                                              |
           |     +------------------+                     |
           |     |  Electronics     |    GPS              |
           |     |  enclosure       |    antenna          |
           |     |  (1.5m x 1.0m)  |    (pole)           |
           |     |                  |                     |
           |     |   [Transponder]  |                     |
           |     |   [Battery x4]  |                     |
           |     |   [Controller]   |                     |
           |     +------------------+                     |
           |                                              |
           |     Steel barge 6.0m x 3.0m                  |
           |                                 * pad eye    |
           |                                              |
           +----------------------------------------------+
                              |
                         mooring line

           Overall: 6.0m x 3.0m x 0.5m deep
           Freeboard: ~0.3m (low!)
           No reflectors needed (active transponder)
           Compact, flat, easy to tow

==========================================================================
```

#### Component List and Mass Breakdown

| # | Component | Material | Qty | Unit Mass | Total Mass | Notes |
|---|---|---|---|---|---|---|
| 1 | Steel barge hull (6m x 3m x 0.5m) | Marine steel S235, 6mm plate | 1 | 900 kg | 900 kg | Welded flat-bottom, no foam |
| 2 | Internal framing / stiffeners | Steel angle, 50x50x5mm | 1 lot | 150 kg | 150 kg | Prevent panel buckling |
| 3 | Active radar transponder | X-band COTS military | 1 | 30 kg | 30 kg | Receive-amplify-retransmit |
| 4 | RF antenna (Tx + Rx) | Microwave antenna, radome | 1 set | 15 kg | 15 kg | Omnidirectional or sector |
| 5 | Battery bank (Li-ion, 72h) | Li-ion 48V, ~10 kWh | 1 | 80 kg | 80 kg | Powers transponder + GPS |
| 6 | Controller / power management | PCB + enclosure | 1 | 10 kg | 10 kg | RCS programming, diagnostics |
| 7 | Watertight electronics enclosure | SS 316 + gaskets, IP67 | 1 | 60 kg | 60 kg | Protects all electronics |
| 8 | Low pedestal mount | Galv. steel, welded | 1 | 25 kg | 25 kg | 0.8m height, bolted to deck |
| 9 | GPS beacon (integrated) | COTS electronics | 1 | 5 kg | 5 kg | Uses transponder power |
| 10 | Marine coatings + cathodic prot. | Epoxy + zinc anodes | 1 lot | 30 kg | 30 kg | Full steel protection |
| 11 | Mooring hardware | Galv. steel | 1 set | 10 kg | 10 kg | Pad eye, fairlead, swivel |
| 12 | Tow points + bridle | Galv. steel lugs + line | 1 set | 10 kg | 10 kg | 2-point tow |
| 13 | Deck drains / scuppers | Steel pipe fittings | 4 | 2 kg | 8 kg | Limited self-draining |
| 14 | Fasteners, cable glands | SS 316, marine grade | 1 lot | 5 kg | 5 kg | Watertight penetrations |
| | | | | **TOTAL BARGE:** | **~1,338 kg** | |
| | | | | | | |
| 15 | Anchor (Danforth, 40 kg) | Galv. steel | 1 | 40 kg | 40 kg | Standard sizing |
| 16 | Chain (12mm G30) | Galv. steel | 30-40 m | 3 kg/m | 105 kg | Standard catenary |
| 17 | Polyester rode (20mm) | Polyester braid | 60-80 m | 0.4 kg/m | 28 kg | Standard rode |
| | | | | **TOTAL MOORING:** | **~173 kg** | |
| | | | | | | |
| | | | | **TOTAL DISPLACEMENT:** | **~1,800 kg** | (including ballast water) |

#### Estimated Unit Cost (@ 10 units)

| Subsystem | Cost | Notes |
|---|---|---|
| Steel barge fabrication | $8,000 | Simple flat-bottom welding |
| Internal framing / stiffeners | $2,500 | Standard steel fab |
| Active radar transponder (X-band) | $30,000-50,000 | **COST DRIVER** --- military-grade RF amp |
| RF antenna system | $5,000-8,000 | Omnidirectional X-band |
| Battery bank (10 kWh Li-ion) | $8,000-12,000 | Marine-rated, 72h |
| Controller + power management | $3,000-5,000 | Custom PCB + firmware |
| Watertight enclosure (IP67) | $4,000 | SS 316 fabrication |
| Pedestal mount | $500 | Simple steel fab |
| GPS beacon (integrated) | $800 | Shares transponder power |
| Marine coatings + cathodic protection | $2,000 | Full steel protection |
| Mooring system | $1,650 | Standard SPM |
| Tow equipment | $400 | Standard bridle |
| Assembly + integration + RF calibration | $10,000 | **Specialized RF testing required** |
| Margin (15%) | $12,000-15,000 | High risk on electronics |
| **TOTAL** | **$88,000-120,000** | **$80,000-120,000 range** |

#### Key Advantages

1. **Programmable RCS** --- Active transponder can produce any RCS value from 100 to 10,000+ m-squared, adjustable before deployment. Can simulate patrol boat, corvette, frigate, or destroyer signatures.
2. **Compact form factor** --- No large reflectors, no tall masts. Low profile, easy to transport and store.
3. **Frequency flexibility** --- Transponder can potentially cover multiple bands (X, C, S) with antenna changes. Future-proof against seeker technology evolution.
4. **Simple tow deployment** --- Flat barge, low profile, easy to tow. No mast erection needed at sea.

#### Key Disadvantages / Challenges (TWO SHOWSTOPPERS)

1. **SHOWSTOPPER --- Cost ($80-120K):** The active transponder alone costs $30-50K. With battery bank ($8-12K), controller ($3-5K), RF antenna ($5-8K), and watertight enclosure ($4K), the electronics package totals $50-80K. This is 2.2-3.4x the entire Concept A unit cost. The $36K target is impossible to meet.
2. **SHOWSTOPPER --- SS 5-6 survivability:** A flat-bottom steel barge with 0.3m freeboard and no foam fill is extremely vulnerable in SS 5-6. Bottom slamming produces peak loads 5-10x displacement. Green water (wave overtopping) floods the deck every wave cycle in SS 4+. The watertight electronics enclosure must survive repeated immersion and impact. Hull integrity under slamming loads requires thick plate (8-10mm) which further increases weight and cost. The barge form fundamentally cannot survive SS 5-6 in open ocean.
3. **NOT passive** --- Violates the fundamental design philosophy. Active electronics require battery power, firmware, and pre-deployment activation. Failure modes multiply: firmware crash, battery drain, moisture ingress, RF component failure, cable chafing. The missile test depends on the electronics working correctly at the moment of engagement.
4. **RCS authenticity concerns** --- An amplified transponder signal has different characteristics than a real ship reflection: wrong Doppler signature (no scintillation from moving structural elements), wrong polarization pattern, wrong glint behavior, wrong angular dependence. Military acceptance of "fake" RCS is questionable for acceptance testing where the goal is to validate seeker performance against realistic targets.
5. **EMC during engagement** --- When a missile's active radar seeker illuminates the transponder, the transponder must re-radiate without interfering with the seeker's tracking loop. If the transponder's retransmission is phase-shifted or frequency-offset, it may confuse the seeker rather than assist it. This is an unresolved RF engineering challenge.

#### Compatibility Check

- P1.5 + P2.1: Steel barge with SPM. COMPATIBLE (standard practice for barges).
- P1.5 + P3.3: Active transponder on barge deck. COMPATIBLE physically, but electronics vulnerability to green water is high.
- P3.3 + P4.4: Transponder on low pedestal. COMPATIBLE but low height = sea clutter interference with the transponder's receive antenna.
- P5.1 + P3.3: GPS integrated with transponder electronics. COMPATIBLE (shared power/data bus).
- P6.1 + P1.5: Simple tow of flat barge. COMPATIBLE. Low drag.

**Two showstoppers identified:** Cost (score 0) and survivability (score 1). Concept D is included for completeness but cannot be recommended for further development.

---

## 4. Concept Comparison Summary Table

### 4.1 Quick Comparison

```
CONCEPT COMPARISON SUMMARY
==========================================================================

Parameter         Concept A          Concept B         Concept C         Concept D
                  "Baseline Opt."    "Spar Buoy"       "Multi-Hull"      "Active Barge"
                  ===============    ==============    ==============    ================

Hull form         HDPE 8.0m round    Steel spar        Cat 2x HDPE       Steel barge 6x3m
                  pontoon            1.5m x 6.0m       1.2m x 8.0m       flat-bottom

Displacement      980 kg             ~2,500 kg         ~1,270 kg         ~1,800 kg

RCS type          Passive corner     Passive corner    Passive corner    Active transponder
                  reflectors         reflectors        reflectors        (programmable)

Num. reflectors   8 x 0.8m          4-6 x 0.8m       4-8 x 0.8m       N/A (electronic)

RCS peak          1,218 m^2         610-914 m^2       610-1,218 m^2    100-10,000 m^2

RCS 360d avg      ~1,050 m^2        ~700-900 m^2     ~700-1,050 m^2    Any (programmed)

RCS variation     +/-2 dB           +/-4-5 dB         +/-2-3 dB        +/-0 dB (ideal)

Survivability     Good (SS 5-6)     Excellent (SS 7+)  Moderate (SS 5)  Poor (SS 3-4)

BM (stability)    210.3 m           ~0.1 m (deep CG)  ~40 m            ~3 m

Roll in SS 6      +/-5 deg          +/-2 deg          +/-8 deg         CAPSIZED / SWAMPED

Mooring           SPM (weathervane)  SPM (weathervane) 3-point (fixed)  SPM (weathervane)

Safety            Passive (best)    Passive (good)    Mostly passive    Active (RF risk)

Cost @ 10 units   $35,640           $55,000-70,000    $50,000-65,000   $80,000-120,000

Cost vs target    MEETS ($36K)      1.5-2.0x OVER     1.4-1.8x OVER    2.2-3.4x OVER

Local content     85-90%            70-80%            75-85%            50-60%

Deploy crew       4, 30 min         6-8, 2-4 hr       6-8, 2-4 hr      4, 30 min

Deploy method     Tow + mooring     Tow + upend       Crane + 3-anchor  Tow + mooring
                  connect            at site           deployment        connect

Development risk  LOW-MED           MEDIUM            MEDIUM            HIGH

Showstoppers      None              Cost, deploy      No weathervane    Cost (0), SS (1)

==========================================================================
```

### 4.2 Pugh-Style Screening (Before Full VDI 2225)

Using Concept A as the datum (baseline), a quick Pugh-style screening identifies which concepts merit full VDI 2225 evaluation:

| Criterion | Weight | A (Datum) | B vs A | C vs A | D vs A |
|---|---|---|---|---|---|
| RCS performance | 0.20 | 0 | - | S | S |
| Env. survivability | 0.20 | 0 | + | - | -- |
| Unit cost | 0.15 | 0 | -- | - | --- |
| Local content | 0.08 | 0 | - | S | -- |
| Deployment simplicity | 0.10 | 0 | -- | -- | S |
| Safety (passive) | 0.10 | 0 | S | - | -- |
| Development risk | 0.10 | 0 | - | - | -- |
| Production scalability | 0.07 | 0 | - | - | - |
| **Sum of +** | | | **1** | **0** | **0** |
| **Sum of S** | | | **1** | **3** | **2** |
| **Sum of -** | | | **5** | **4** | **5** |
| **Net** | | DATUM | **-4** | **-4** | **-5** |

**Legend:** + = better than A, S = same as A, - = worse than A, -- = much worse, --- = showstopper

**Screening result:** All three alternatives score net negative against Concept A. Concept D has showstoppers (cost, survivability) and is eliminated before full VDI 2225 evaluation. Concepts B and C proceed to full evaluation for completeness but are unlikely to overtake A.

### 4.3 Risk-Adjusted Ranking

| Rank | Concept | Est. Cost | Meets Requirements? | Overall Assessment |
|---|---|---|---|---|
| **1** | **A: Baseline Optimized** | $35,640 | YES --- all 116 requirements | **PROCEED to VDI 2225** |
| **2** | B: Spar Buoy | $55-70K | NO --- cost, deployment | **REVIEW** (VDI 2225 for record) |
| **3** | C: Multi-Hull Station Keeper | $50-65K | NO --- cost, SS 5-6, position rpt. | **REVIEW** (VDI 2225 for record) |
| **4** | D: Active Signature Barge | $80-120K | NO --- 2 showstoppers | **REJECT** (do not evaluate further) |

---

## 5. Cross-References

### Phase 2 Documents (Conceptual Design)

- [[abstraction.md]] --- Step 1: 5-step abstraction, essential problem statement
- [[function_structure.md]] --- Step 2: 7 sub-functions, E/M/S flows, interface definitions
- [[working_principles.md]] --- Step 3: Working principles per sub-function, compatibility assessment
- [[concept_evaluation.md]] --- Step 5 (next): VDI 2225 weighted evaluation of Concepts A, B, C
- [[concept_selection.md]] --- Step 6: Final selection decision and firm-up
- [[conceptual_design.md]] --- Phase 2 summary document (all 6 steps consolidated)

### Phase 0/1 Source Documents

- [[../00_odi/phase0_final_revision.md]] --- Rev B.1 specifications, cost model, RCS sizing
- [[../00_odi/re_deep_analysis.md]] --- Reflector physics (sigma = 12*pi*a^4/lambda^2), mooring analysis
- [[../00_odi/re_competitive_analysis.md]] --- Competitive positioning (SINKEX, Hammerhead, HSMST, L-CATT)
- [[../00_odi/environmental_survivability.md]] --- SS 5-6 environmental loading, operational concept
- [[../01_requirements/requirements_list.md]] --- 116 requirements (Rev B.1), 16 categories
- [[../01_requirements/stakeholder_analysis.md]] --- 10 stakeholders, deployment crew constraints
- [[../01_requirements/standards_mapping.md]] --- MIL-STD-810H, MIL-STD-461G mapping
- [[../PROJECT_STATUS.md]] --- Project status tracker
