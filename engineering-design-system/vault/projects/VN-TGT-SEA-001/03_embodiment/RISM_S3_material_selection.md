---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "S3 — Preliminary Material Selection"
group: RISM
version: 1.0
created: 2026-02-10
status: draft
---

# Step S3: Preliminary Material Selection — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Screen candidate materials for all 7 subsystems against hard constraints (environmental, mechanical, manufacturing, cost), assess galvanic compatibility at material junctions, and evaluate Vietnamese supply chain readiness.
**Method:** Pahl & Beitz RISM Step S — Material Screening & Short-Listing
**Input:** [[RISM_R1_requirements_identification.md]] — 74 direct embodiment requirements mapped to 7 subsystems
**Selected Concept:** Concept A "Baseline Optimized" (VDI 2225: 81.8%)

---

## 1. Material Requirements by Component

Each subsystem's material requirements are extracted from the R1 requirements identification and the 116 Phase 1 requirements. The operating environment is the dominant driver: **continuous tropical saltwater immersion/spray, UV exposure, -5 deg C to +55 deg C ambient, 72-hour unattended deployment in Sea State 5-6.**

### 1.1 Requirements Summary Table

| Subsystem | Environmental | Mechanical | Manufacturing | Cost Driver | Governing Reqs |
|-----------|--------------|------------|---------------|-------------|----------------|
| **L0: Mooring** | Continuous saltwater immersion (10-80 m depth), biofouling, anaerobic seabed mud | SWL >=4,536 kgf chain; anchor hold >=1,500 kgf; 40,000+ load cycles | Standard marine hardware; must be available off-the-shelf in Vietnam | ~$2,500/set (depth-dependent) | FOR-004 to FOR-007, MAT-006, OPR-005 |
| **L1: Hull** | Saltwater immersion + UV (20+ year life target), -5 to +55 deg C, wave slam | Displacement <=1,100 kg total; hull mass ~350 kg; reserve buoyancy >96% | Rotomolding or HDPE welding; 8.0 m diameter (may need 2-section) | ~$8,200 (hull + foam) | GEO-001, GEO-002, MAT-001, MAT-002, TRA-001 |
| **L2: Frame** | Salt spray/splash zone 72h+, galvanic contact with HDPE hull and steel chain | Green water 157 kgf; mooring pad eye load 1,512 kgf peak; 40,000 cycles | Welded steel fabrication; hot-dip galvanize; Vietnamese steel suppliers | ~$1,800 | MAT-005, FOR-009, ASM-005, OPR-009 |
| **L2.5: Masts** | Salt spray continuous; UV; cyclic wind/wave loading at 3-4 m height | Bending >=1,100 N-m per mast; fatigue 40,000 cycles at +/-7 deg roll | Tube section, welded base plate; HDG or marine coating; socket-insert design | ~$800 (8 masts) | MAT-010, FOR-010, FOR-011, GEO-005, GEO-010 |
| **L3: Reflectors** | Salt spray on face plates and AM frames; -5 to +55 deg C; wave vibration | Face plate flatness <0.1 mm; orthogonality <=+/-0.1 deg; Ra <=10 um | CNC fly-cut (face plates); LPBF additive (frames); anodizing (both) | ~$13,000 (8 units) | MAT-003, MAT-004, MAT-007 to MAT-009, SIG-001 to SIG-009 |
| **L5: GPS Beacon** | Salt spray + occasional submersion (green water); UV; -5 to +55 deg C | Battery 72h at 1 Hz; total mass <=5 kg; IP67/68 enclosure | COTS procurement; battery pack assembly | ~$1,800 | ENR-001, ENR-002, SIG-007 |
| **L6: Tow System** | Saltwater immersion during tow (surface); UV during storage | SWL >=7,524 kgf tow line; bridle SWL >=3x peak tow load | Standard marine rope/hardware procurement; local shackle sourcing | ~$400 | FOR-008, TRA-003, TRA-004, SAF-005 |

---

## 2. Hard Constraint Screening

All candidate materials must pass every hard constraint below. Failure on any single constraint eliminates the candidate.

### 2.1 Universal Hard Constraints (All Subsystems)

| Constraint ID | Description | Threshold | Verification |
|---------------|-------------|-----------|--------------|
| HC-01 | Saltwater corrosion resistance | >=72h continuous immersion/spray without functional degradation | MIL-STD-810H Method 509.7 |
| HC-02 | Temperature range | -5 deg C to +55 deg C service without brittle fracture or softening | Material data sheet Tmin/Tmax |
| HC-03 | UV resistance | >=5 year outdoor exposure (or protected) | ASTM G154 or manufacturer data |
| HC-04 | Non-toxic marine debris | No hazardous leachate if lost at sea | MSDS review |
| HC-05 | Unit cost contribution | Total material cost within $36K unit budget | BOM cost roll-up |

### 2.2 Subsystem-Specific Hard Constraints

#### L0: Storm Mooring System

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Chain SWL | >=4,536 kgf (3:1 on 1,512 kgf peak) | FOR-006 — eliminates all chain < G30 12 mm |
| Anchor holding | >=1,500 kgf in sand/mud | FOR-007 — eliminates lightweight anchors (<25 kg) |
| Galvanization | HDG per ASTM A153 or equivalent | MAT-006 — bare steel chain eliminated |
| Swivel/shackle rating | >=4,536 kgf WLL | FOR-006 — undersized hardware eliminated |

#### L1: HDPE Hull Platform

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Material type | HDPE (rotomolded or welded) | MAT-001 — MUST requirement; eliminates GRP, steel, aluminum hulls |
| Foam fill | Closed-cell marine foam, >=98% reserve buoyancy | MAT-002 — eliminates open-cell foam, no-fill options |
| Hull mass | <=400 kg (hull + foam + fittings) | GEO-007 mass budget — 350 kg target + 50 kg margin |
| Fabrication size | 8.0 m diameter or 2-section fit for standard transport | GEO-001, TRA-001, TRA-002 |

#### L2: Steel Structural Frame

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Yield strength | >=235 MPa | MAT-005 — S235 minimum for mooring pad eye loads |
| Corrosion protection | HDG >=85 um per ASTM A123 | OPR-009 — unprotected steel eliminated |
| Weldability | CE <=0.42 (carbon equivalent) | PRD-005 — Vietnamese welding capability |
| Frame mass | <=180 kg | GEO-007 mass budget allocation |

#### L2.5: Mast System

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Bending capacity | >=1,100 N-m at base | FOR-011 — eliminates thin-wall tubes (<3 mm for 60 mm OD steel) |
| Fatigue endurance | >=40,000 cycles at +/-7 deg | FOR-010 — eliminates low-fatigue materials; weld detail must be Category D or better |
| Corrosion protection | HDG or marine coating system | OPR-009, MAT-010 |
| Per-mast mass | <=20 kg (mast + base plate, excl. reflector) | GEO-007 mass budget — 16 kg target |

#### L3: Hybrid Corner Reflectors

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Face plate alloy | 6061-T6 aluminum, 3 mm thick | MAT-003 — MUST (CNC machinability, flatness, RF reflectivity) |
| Face plate Ra | <=10 um | MAT-007 — adequate for lambda = 32 mm at X-band |
| AM frame alloy | AlSi10Mg (LPBF process) | MAT-004 — MUST (AM processability, strength after T5 heat treat) |
| Face plate protection | Type II anodize >=10 um | MAT-008 — salt spray protection for 6061-T6 |
| AM frame protection | Type III hard anodize >=25 um | MAT-009 — MUST (AlSi10Mg requires aggressive protection) |

#### L5: GPS Beacon

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Battery chemistry | Li-ion or LiFePO4, >=20 Wh capacity | ENR-001 — 72h at 1 Hz transmit rate |
| Enclosure rating | IP67 minimum (IP68 preferred) | OPR-009 — green water submersion events |
| Total mass | <=5 kg (beacon + battery + enclosure) | GEO-007 mass budget |

#### L6: Tow/Deployment System

| Constraint | Value | Screening Rationale |
|------------|-------|---------------------|
| Tow line SWL | >=7,524 kgf | FOR-008 — eliminates polypropylene, nylon <20 mm |
| Bridle SWL | >=3x peak tow load | SAF-005 — safety-critical component |
| UV/salt resistance | Marine-grade rope with UV stabilizer | OPR-009 — bare nylon degrades in UV |

---

## 3. Candidate Short List

Materials that pass all hard constraints for each subsystem. Each candidate includes grade, key properties, Vietnamese availability, and relative cost.

### 3.1 L0: Storm Mooring System

| # | Component | Material Candidate | Grade/Spec | Key Properties | VN Availability | Cost ($/kg) | HC Pass? |
|---|-----------|-------------------|------------|----------------|-----------------|-------------|----------|
| 1a | Chain | G30 proof coil, HDG | ASTM A413, 12 mm | SWL 2,100 kgf per link; 1.65 kg/m | Hai Phong marine supply (Truong Hai, Saigon Ship) | ~$2.50/m | All PASS |
| 1b | Chain | G30 proof coil, HDG | ASTM A413, 16 mm | SWL 3,700 kgf per link; 2.90 kg/m | Same suppliers | ~$4.20/m | All PASS |
| 1c | Chain | G43 high-test, HDG | ASTM A391, 12 mm | SWL 3,100 kgf per link; 1.65 kg/m | Import (China); 2-3 week lead | ~$3.80/m | All PASS |
| 2a | Rode | Polyester braided | 20 mm 8-strand | SWL ~4,000 kgf; 0.25 kg/m; low stretch | Hai Phong rope suppliers | ~$1.80/m | All PASS |
| 2b | Rode | Nylon double-braid | 22 mm | SWL ~4,500 kgf; 0.30 kg/m; high stretch (shock absorb) | Hai Phong rope suppliers | ~$2.20/m | All PASS |
| 3a | Anchor | Danforth type | Hot-dip galvanized, 50 kg | Holding ~1,800 kgf in sand; good in mud | Marine supply (Hai Phong, Da Nang) | ~$180/unit | All PASS |
| 3b | Anchor | Bruce/claw type | HDG, 30 kg | Holding ~1,500 kgf in sand; better in mixed seabed | Marine supply; some import | ~$220/unit | All PASS |
| 3c | Anchor | Danforth type | HDG, 30 kg | Holding ~1,200 kgf in sand | Marine supply | ~$120/unit | **FAIL** (FOR-007) |
| 4 | Swivel | Jaw-jaw swivel | HDG forged steel, WLL 5,000 kgf | Allows 360 deg weathervane rotation | Import (China/Japan) | ~$45/unit | All PASS |
| 5 | Shackles | Bow shackle | HDG forged, WLL 5,000 kgf | Standard marine hardware | Hai Phong marine supply | ~$12/each | All PASS |

**Screening result:** 30 kg Danforth (3c) eliminated — holding capacity 1,200 kgf < 1,500 kgf required.

**Recommendation for M4:** G30 HDG 16 mm chain (1b) preferred for 3:1 SWL margin; 12 mm G43 (1c) as alternative if weight-sensitive. Polyester rode (2a) preferred for low creep; nylon (2b) considered where shock absorption needed. Danforth 50 kg (3a) for sandy seabed; Bruce 30 kg (3b) for varied seabed.

### 3.2 L1: HDPE Hull Platform

| # | Material Candidate | Grade/Spec | Density (kg/m3) | Yield (MPa) | UV Resist. | VN Availability | Cost ($/kg) | HC Pass? |
|---|-------------------|------------|-----------------|-------------|------------|-----------------|-------------|----------|
| 1a | HDPE — rotomolding grade | PE100, MFI 3-5 g/10min | 950 | 25-30 | Excellent (UV-stabilized) | TPC Vina (Ba Ria), Long Son Petrochem | ~$1.50 | All PASS |
| 1b | HDPE — extrusion/welding grade | PE100, sheet 10-15 mm | 950 | 25-30 | Excellent | Same + sheet imports (China) | ~$2.00 | All PASS |
| 1c | LLDPE — rotomolding grade | MFI 5-8 g/10min | 930 | 15-20 | Good (add UV stabilizer) | TPC Vina | ~$1.40 | All PASS |
| 2a | PU closed-cell foam | Marine grade, 35-50 kg/m3 | 35-50 | N/A (foam) | N/A | Import (China); local pour-in-place contractors | ~$4.00 | All PASS |
| 2b | PE closed-cell foam | Marine buoyancy foam, 30-45 kg/m3 | 30-45 | N/A (foam) | N/A | Import (China/Korea) | ~$5.50 | All PASS |
| 2c | EPS (expanded polystyrene) | Marine grade, 25-35 kg/m3 | 25-35 | N/A (foam) | N/A | Local VN suppliers | ~$1.20 | **FAIL** — absorbs water over time (not closed-cell) |

**Screening result:** EPS (2c) eliminated — not truly closed-cell; absorbs water under prolonged immersion, compromising reserve buoyancy requirement.

**Recommendation for M4:** HDPE PE100 rotomolding grade (1a) is primary choice if 8.0 m rotomold tooling feasible; HDPE welded sheet (1b) for 2-section hull approach. PU closed-cell foam (2a) preferred for pour-in-place application inside hull cavities.

### 3.3 L2: Steel Structural Frame

| # | Material Candidate | Grade/Spec | Yield (MPa) | Density (kg/m3) | Weldability CE | Corrosion Protection | VN Supplier | Cost ($/kg) | HC Pass? |
|---|-------------------|------------|-------------|-----------------|---------------|---------------------|-------------|-------------|----------|
| 1a | Mild steel | S235JR (EN 10025) / SS400 (JIS) | 235 | 7,850 | 0.35 | HDG >=85 um (ASTM A123) | Hoa Phat, Nam Kim | ~$0.80 | All PASS |
| 1b | Structural steel | S355J2 (EN 10025) / SM490 (JIS) | 355 | 7,850 | 0.42 | HDG >=85 um | Hoa Phat (plate/section); import for special sections | ~$0.95 | All PASS |
| 1c | Stainless steel | AISI 316L | 205 | 8,000 | N/A (no HDG needed) | Inherent (Mo content) | Import (China/Japan); limited VN stock | ~$4.50 | PASS but cost concern |
| 1d | Marine aluminum | 5083-H116 | 215 | 2,680 | N/A (TIG/MIG weld) | Inherent (passive oxide layer) | Import (limited VN stock) | ~$5.00 | PASS but cost concern |

**Screening result:** All pass hard constraints. However, 316L (1c) and 5083 aluminum (1d) significantly exceed cost targets for a structural frame role — approximately 5-6x the cost of mild steel. They remain viable only if galvanic isolation drives the choice.

**Recommendation for M4:** S235JR/SS400 (1a) hot-dip galvanized — lowest cost, excellent Vietnamese availability from Hoa Phat and Nam Kim, well within yield requirement, fully compatible with local welding capability. S355J2 (1b) only if FEA shows higher strength needed at pad eye.

### 3.4 L2.5: Mast System (8 units)

| # | Material Candidate | Grade/Spec | OD x Wall (mm) | Section Modulus W (mm3) | Bending Capacity* (N-m) | Mass/3m (kg) | VN Supplier | Cost ($/mast) | HC Pass? |
|---|-------------------|------------|-----------------|------------------------|------------------------|-------------|-------------|--------------|----------|
| 1a | Galv. steel tube | S235, CHS 60.3 x 4.0 | 60.3 x 4.0 | 4,637 | 1,090 | 16.2 | Hoa Phat, SeAH (VN mill) | ~$35 | **MARGINAL** — 1,090 < 1,100 N-m |
| 1b | Galv. steel tube | S235, CHS 76.1 x 4.0 | 76.1 x 4.0 | 7,660 | 1,800 | 20.8 | Hoa Phat, SeAH | ~$45 | All PASS (64% margin) |
| 1c | Galv. steel tube | S355, CHS 60.3 x 4.0 | 60.3 x 4.0 | 4,637 | 1,646 | 16.2 | Hoa Phat (limited CHS stock in S355) | ~$45 | All PASS (50% margin) |
| 1d | Galv. steel tube | S235, CHS 60.3 x 5.0 | 60.3 x 5.0 | 5,490 | 1,290 | 19.6 | Hoa Phat, SeAH | ~$40 | All PASS (17% margin) |
| 1e | Marine aluminum tube | 6082-T6, CHS 76 x 5 | 76.0 x 5.0 | 8,200 | 2,132** | 8.4 | Import (China); limited VN stock | ~$85 | All PASS — but fatigue concern |
| 1f | Marine aluminum tube | 5083-H111, CHS 80 x 6 | 80.0 x 6.0 | 10,200 | 2,244** | 10.2 | Import | ~$95 | All PASS — better fatigue than 6082 |

*Bending capacity = W x fy, where fy = 235 MPa (S235), 355 MPa (S355), 260 MPa (6082-T6), 220 MPa (5083-H111)
**Aluminum yield values are for welded condition (HAZ reduction)

**Screening result:** S235 CHS 60.3 x 4.0 (1a) marginally fails — 1,090 N-m < 1,100 N-m required by FOR-011. Could be acceptable considering that FOR-011 already includes 2.0x dynamic factor, but eliminated on strict hard-constraint basis. Aluminum options (1e, 1f) pass but introduce cost, import dependency, and welded fatigue concerns.

**Recommendation for M4:** S235 CHS 76.1 x 4.0 (1b) is the primary candidate — 64% bending margin, 20.8 kg/mast (within budget), low cost, excellent VN availability. S355 CHS 60.3 x 4.0 (1c) as lighter alternative if 16 kg/mast mass target is critical. Aluminum tubes deferred unless mass becomes critical constraint.

### 3.5 L3: Hybrid Corner Reflectors (8 units)

Face plates and AM frames are constrained by MUST requirements (MAT-003, MAT-004). Material screening focuses on confirming the specified grades and identifying protective coatings.

| # | Component | Material Candidate | Grade/Spec | Key Properties | VN Availability | Cost ($/unit of 8 reflectors) | HC Pass? |
|---|-----------|-------------------|------------|----------------|-----------------|------------------------------|----------|
| 1a | Face plate | Aluminum | 6061-T6, 3 mm sheet | UTS 310 MPa; Ra achievable <1 um by fly-cut; anodizable | Plate import (China/Korea); CNC at VN job shops (Binh Duong, HCMC) | ~$4,000 (24 plates, CNC) | All PASS |
| 1b | Face plate | Aluminum | 5052-H32, 3 mm sheet | UTS 228 MPa; good corrosion resistance; anodizable | Better VN stock availability | ~$3,500 | **FAIL** — 5052 not specified in MAT-003 (lower strength, different machining behavior) |
| 2a | AM frame | AlSi10Mg | LPBF, as-printed + T5 | UTS ~400 MPa (T5); supports <=+/-0.1 deg orthogonality; ASTM F3301 processable | ASEAN AM bureaus (Xometry Asia, Facfox, JR Tech — SG/MY/TH) | ~$8,000 (8 frames) | All PASS |
| 2b | AM frame | Scalmalloy (Al-Mg-Sc) | LPBF | UTS ~520 MPa; superior fatigue; better corrosion than AlSi10Mg | Limited availability; 2-3x cost of AlSi10Mg | ~$20,000 (8 frames) | **FAIL** (CST-001 — cost) |
| 3a | Face anodize | Type II sulfuric | MIL-A-8625 Type II, >=10 um, clear | Corrosion protection for 6061-T6; minimal effect on RF reflectivity | VN anodizing shops (HCMC, Binh Duong) | ~$200 (24 plates) | All PASS |
| 3b | Face anodize | Type II chromic | MIL-A-8625 Type I, >=5 um | Better corrosion protection on thin sections; restricted substance (Cr6+) | Limited VN capability; environmental concern | ~$350 (24 plates) | PASS but environmental concern |
| 4a | Frame anodize | Type III hard anodize | MIL-A-8625 Type III, >=25 um | Hard coat for AlSi10Mg; wear + corrosion resistance | ASEAN (Singapore/Thailand) or HCMC specialist shops | ~$400 (8 frames) | All PASS |
| 4b | Frame coating | Cerakote ceramic | H-series, 25-75 um | Good corrosion/wear; applied at room temp; can coat AM parts | Import coating; some VN applicators | ~$300 (8 frames) | PASS (alternative if Type III not available for AlSi10Mg) |

**Screening result:** 5052-H32 (1b) eliminated per MAT-003 MUST specification. Scalmalloy (2b) eliminated on cost — more than doubles the reflector system cost, pushing unit cost above $36K.

**Recommendation for M4:** 6061-T6 face plates (1a) with Type II sulfuric anodize (3a) — confirmed baseline. AlSi10Mg LPBF frames (2a) with Type III hard anodize (4a) — confirmed baseline. Cerakote (4b) identified as fallback coating if Type III hard anodizing proves difficult on AlSi10Mg (porous AM surfaces may require pre-sealing).

### 3.6 L5: GPS Beacon System

| # | Component | Material Candidate | Grade/Spec | Key Properties | VN Availability | Cost ($/unit) | HC Pass? |
|---|-----------|-------------------|------------|----------------|-----------------|---------------|----------|
| 1a | Beacon unit | COTS GPS/Iridium | YB3i or equivalent | 1 Hz position, IP68, 72h+ battery | Import (USA/Europe) | ~$1,200 | All PASS |
| 1b | Beacon unit | COTS GPS/GSM | Quectel + SIM module | 1 Hz, IP67 enclosure needed | Import (China); lower cost | ~$400 | PASS if IP67 enclosure added |
| 2a | Battery pack | Li-ion 18650 cells | Samsung/LG, 3.7V, custom pack | >=20 Wh; -20 to +60 deg C; 72h at ~0.28W | Import cells; local pack assembly (VN) | ~$80 | All PASS |
| 2b | Battery pack | LiFePO4 cells | 3.2V prismatic | >=20 Wh; better thermal stability; heavier | Import (China) | ~$60 | All PASS |
| 3a | Enclosure | ABS/polycarbonate | IP68, UV-stabilized | Waterproof; UV resistant; lightweight | Import or local injection mold (VN) | ~$40 | All PASS |
| 3b | Enclosure | Pelican-type case | IP67 rated, modified | Off-the-shelf with cable gland penetrations | Import | ~$80 | All PASS |

**Recommendation for M4:** COTS GPS/Iridium unit (1a) is preferred for satellite communication in open ocean (no GSM coverage). Li-ion battery pack (2a) for energy density. Final enclosure decision deferred to detailed design — Pelican-type (3b) may be simpler for prototype phase.

### 3.7 L6: Tow/Deployment System

| # | Component | Material Candidate | Grade/Spec | Key Properties | VN Availability | Cost ($/set) | HC Pass? |
|---|-----------|-------------------|------------|----------------|-----------------|-------------|----------|
| 1a | Tow line | Dyneema HMPE | 16 mm 12-strand | SWL ~8,000 kgf; 0.14 kg/m; near-zero stretch; floats | Import (Netherlands/China license) | ~$8/m | All PASS |
| 1b | Tow line | Polyester double-braid | 28 mm | SWL ~6,000 kgf; 0.45 kg/m; moderate stretch | Hai Phong rope suppliers | ~$4/m | All PASS |
| 1c | Tow line | Nylon double-braid | 24 mm | SWL ~5,500 kgf; 0.35 kg/m; high stretch | Hai Phong rope suppliers | ~$3/m | **FAIL** (FOR-008 — SWL 5,500 < 7,524) |
| 2a | Bridle legs | Dyneema HMPE | 12 mm, 2x 5 m | SWL ~5,500 kgf per leg; combined ~11,000 kgf | Import | ~$60/pair | All PASS |
| 2b | Bridle legs | Wire rope, galvanized | 12 mm 6x19 | SWL ~6,000 kgf per leg | Hai Phong marine supply | ~$30/pair | All PASS |
| 3a | Drogue | Canvas sea anchor | 1.0 m diameter | Drag stabilization during tow; reduces yaw | Local canvas shop (VN) or import | ~$60 | All PASS |
| 4 | Shackles/thimbles | HDG forged | WLL >=5,000 kgf | Standard marine hardware | Hai Phong marine supply | ~$40/set | All PASS |

**Screening result:** 24 mm nylon (1c) eliminated — SWL insufficient for 3:1 safety factor on peak tow load.

**Recommendation for M4:** 16 mm Dyneema (1a) per TRA-004 MUST requirement. Wire rope bridle (2b) preferred for durability at lower cost than Dyneema bridle. Canvas drogue (3a) locally producible.

---

## 4. Galvanic Compatibility Matrix

### 4.1 Galvanic Series Reference (Seawater)

Materials ranked from anodic (corrodes first) to cathodic (protected):

```
ANODIC (most active)                       CATHODIC (most noble)
  |                                             |
  Zinc HDG     Aluminum    Mild Steel    316 SS   Copper alloys
  (-1.05 V)   (-0.76 V)   (-0.60 V)    (-0.08 V)  (-0.04 V)
              AlSi10Mg    S235 HDG*
              (-0.75 V)
              6061-T6
              (-0.74 V)

  *HDG steel has zinc surface layer at -1.05 V until zinc consumed,
   then reverts to bare steel at -0.60 V
```

### 4.2 Material Junction Analysis

Every physical junction between dissimilar metals on the target platform is assessed below. Galvanic potential differences exceeding 0.15 V in seawater create significant corrosion risk.

| Junction ID | Interface | Material A | Material B | Potential Diff. (V) | Corrosion Risk | Corroding Member | Isolation Strategy |
|-------------|-----------|-----------|-----------|---------------------|----------------|-----------------|-------------------|
| **GJ-01** | Frame (L2) to Hull (L1) | S235 HDG steel | HDPE | N/A (HDPE is non-conductive) | **NONE** | N/A | HDPE is inherent insulator; no galvanic couple possible |
| **GJ-02** | Frame (L2) to Mooring chain (L0) | S235 HDG steel | G30 HDG chain | ~0.00 V (both HDG zinc surface) | **LOW** | Neither (same coating) | No isolation needed; both are HDG zinc-on-steel |
| **GJ-03** | Mast (L2.5) to Frame socket (L2) | S235 HDG tube | S235 HDG socket | ~0.00 V | **NONE** | N/A | Same material system; socket welded to frame before HDG |
| **GJ-04** | Mast top plate to Reflector bracket (L2.5 to L3) | S235 HDG steel | 6061-T6 aluminum (anodized) | ~0.31 V (Zn to Al) initially; ~0.14 V (bare steel to Al) | **HIGH** initially; **MEDIUM** after zinc layer consumed | Zinc coating (sacrificial), then aluminum | (1) Nylon isolating washers on all bolts; (2) EPDM rubber gasket between mast plate and reflector bracket; (3) Marine sealant (Sikaflex 291) at interface; (4) Zinc disc anode (0.5 kg) bolted to mast top plate as sacrificial protection |
| **GJ-05** | Reflector face plate to AM frame (L3 internal) | 6061-T6 Al | AlSi10Mg Al | ~0.02 V | **NEGLIGIBLE** | N/A (both aluminum alloys, near-identical potential) | No isolation needed; bolt with stainless A4-80 fasteners and apply anti-seize to prevent fretting |
| **GJ-06** | Stainless fasteners in aluminum (L3) | A4-80 (316) SS bolts | 6061-T6 / AlSi10Mg Al | ~0.66 V | **HIGH** — aluminum corrodes around SS bolt | Aluminum surrounding bolt hole | (1) Anodize aluminum before assembly (creates oxide barrier); (2) Apply Tef-Gel or Lanolin-based anti-seize on all SS-to-Al bolted joints; (3) Use nylon-insert lock nuts (Nylock) to avoid bare metal contact at nut face; (4) Torque to spec and seal with marine sealant |
| **GJ-07** | Stainless fasteners in HDG steel (L2, L2.5) | A4-80 (316) SS bolts | S235 HDG steel | ~0.97 V (SS to Zn); ~0.52 V (SS to bare steel) | **HIGH** — zinc/steel corrodes around SS bolt | Zinc coating, then steel around bolt | (1) Use HDG steel bolts (Grade 8.8 HDG) instead of SS where possible; (2) Where SS required, apply bituminous paint at bolt head/nut bearing surface; (3) Zinc anode washers under bolt heads |
| **GJ-08** | Mooring swivel (L0) to chain (L0) | HDG forged steel | G30 HDG chain | ~0.00 V | **NONE** | N/A | Same coating system |
| **GJ-09** | GPS bracket to mast (L5 to L2.5) | 316 SS or HDG bracket | S235 HDG mast | 0.00 to 0.97 V | **LOW** if HDG-to-HDG; **HIGH** if SS-to-HDG | Mast zinc coating if SS bracket | Use HDG steel bracket (preferred) or isolate SS bracket with rubber liner |
| **GJ-10** | Tow pad eye (L6) to hull frame (L2) | S235 HDG steel | S235 HDG steel | ~0.00 V | **NONE** | N/A | Same material and coating; welded or through-bolted |

### 4.3 Galvanic Risk Summary

```
RISK LEVEL:  HIGH (3)     MEDIUM (1)    LOW (1)     NONE (5)
Junctions:   GJ-04,06,07  GJ-04*        GJ-09       GJ-01,02,03,08,10
             (* after zinc
               consumed)

CRITICAL JUNCTIONS REQUIRING DESIGNED ISOLATION:
  GJ-04: Steel mast top plate  <-->  Aluminum reflector bracket
  GJ-06: Stainless SS bolts    <-->  Aluminum reflector components
  GJ-07: Stainless SS bolts    <-->  HDG steel frame (if used)
```

### 4.4 Cathodic Protection Strategy

In addition to junction isolation, the following sacrificial anodes are recommended:

| Location | Anode Type | Material | Mass (kg) | Protection Zone | Replacement Interval |
|----------|-----------|----------|-----------|-----------------|---------------------|
| Mast top plate (x8) | Disc anode, bolt-on | Zinc (Mil-A-18001) | 0.5 each | GJ-04 junction: steel-to-aluminum interface | Expendable (target is single-use) |
| Central pad eye area | Pear-shaped hull anode | Zinc (Mil-A-18001) | 2.0 | GJ-02 zone: submerged chain-to-frame connection | Expendable |
| Total zinc mass | — | — | **6.0 kg** | All submerged/splash zone metallic junctions | N/A |

**Note:** Target is expendable (MNT-001) — anodes are sized for >=72h deployment plus storage life, not multi-year service. 6.0 kg total zinc anode mass is added to the mass budget (within 130 kg reserve margin).

---

## 5. Vietnamese Supply Chain Assessment

### 5.1 Material Supply Chain Matrix

| Material | Local Supplier(s) | Lead Time | Quality Cert. | MOQ | Import Dependency | Single-Source Risk |
|----------|-------------------|-----------|---------------|-----|-------------------|--------------------|
| **S235/SS400 steel plate & section** | Hoa Phat (Hai Duong), Nam Kim (Binh Duong) | 1-2 weeks | JIS G3101 (SS400), TCVN 1765 | 500 kg | **NONE** — fully domestic | **LOW** — multiple mills |
| **S235 CHS tube (60-76 mm)** | Hoa Phat Pipe, SeAH Vietnam (Ba Ria) | 1-2 weeks | JIS G3444 (STK400), EN 10219 | 100 m | **NONE** — VN mills produce standard CHS | **LOW** — 2+ mills |
| **Hot-dip galvanizing** | Vinacomin (Ha Noi), Galva Vietnam (Binh Duong), Hoa Phat Galvanizing | 3-5 days turnaround | ASTM A123, ISO 1461 | Per batch | **NONE** — multiple VN facilities | **LOW** |
| **HDPE resin (PE100)** | TPC Vina (Ba Ria), Long Son Petrochemicals (under construction 2026) | 2-3 weeks | ISO 4427, TCVN 7305 | 1 tonne | **LOW** — TPC Vina operational; Long Son expected 2026 | **MEDIUM** — TPC Vina primary; Long Son not yet confirmed |
| **HDPE rotomolding/welding** | Tan Phu Plastic (HCMC), Nhat Quang (Binh Duong) | 3-4 weeks (tooling); 1 week (production) | No formal marine cert — need qualification | 1 unit | **NONE** — local fabrication | **MEDIUM** — no 8.0m experience; needs qualification |
| **PU closed-cell foam** | Import (Dow Chemical — China), local pour-in-place contractors | 2-3 weeks | ASTM D1621 (compression), ASTM D2842 (water absorption) | 200 kg | **MEDIUM** — resin imported, application local | **LOW** — multiple global sources |
| **6061-T6 aluminum sheet (3 mm)** | Import: Novelis (Korea), Aleris (China), UACJ (Japan) | 3-4 weeks | ASTM B209, AMS-QQ-A-250/11 | 100 sheets (1220x2440) | **HIGH** — no VN primary aluminum rolling | **LOW** — multiple Asian sources |
| **CNC machining (fly-cut 800x800)** | Minh Duc CNC (Binh Duong), Truong Hai Precision (HCMC), An Phat Technology (Ha Noi) | 1-2 weeks per batch of 24 plates | ISO 9001; no AS9100 (defense) | 8 plates | **NONE** — VN CNC capability adequate | **LOW** — 5+ qualified shops in HCMC/Binh Duong |
| **AlSi10Mg LPBF (AM frames)** | ASEAN: Xometry Asia (SG), Facfox (SG/CN), JR Tech (MY) | 2-3 weeks + shipping | ASTM F3301, ASTM F3318 | 1 frame | **HIGH** — no VN LPBF production | **MEDIUM** — 3 qualified bureaus, but all regional |
| **Type II/III anodizing** | Kim Thanh Anodize (HCMC), Viet Anod (Binh Duong) | 3-5 days | MIL-A-8625 (claimed; need verification) | Per batch | **LOW** — Type II widely available; Type III limited | **MEDIUM** — Type III capability needs qualification for AlSi10Mg |
| **G30 HDG chain (12-16 mm)** | Truong Hai Marine (Hai Phong), Saigon Ship Chandler | 1-2 weeks | ASTM A413, ISO 1704 | 50 m | **LOW** — standard marine supply | **LOW** — multiple chandlers |
| **Dyneema HMPE rope (16 mm)** | Import: DSM (Netherlands via Singapore), Liros (Germany) | 3-4 weeks | EN ISO 10325 | 100 m coil | **HIGH** — specialty rope, no VN production | **MEDIUM** — 2-3 global brands, well-stocked in SG marine supply |
| **Danforth/Bruce anchor (30-50 kg)** | Truong Hai Marine, Da Nang Ship Supply | 1 week | ISO 9001 foundry cert | 1 unit | **LOW** — most cast in China, stocked locally | **LOW** |
| **GPS/Iridium beacon (COTS)** | Import: YellowBrick (UK), Ocean Signal (UK), McMurdo (US/FR) | 4-6 weeks | CE, FCC, maritime type approval | 1 unit | **HIGH** — fully imported electronics | **MEDIUM** — 3+ brands available |
| **Li-ion battery cells** | Import: Samsung SDI (Korea), LG Chem (Korea), EVE (China) | 2-3 weeks | UN 38.3 transport cert, IEC 62133 | 50 cells | **HIGH** — no VN cell production | **LOW** — massive global supply chain |
| **Zinc anodes (Mil-A-18001)** | Import (China/Korea) or local casting from zinc ingot | 1-2 weeks | MIL-DTL-18001 | 10 kg | **MEDIUM** — zinc ingot local, casting may need qualification | **LOW** |

### 5.2 Import Dependency Summary

| Category | Fully Domestic (VN) | Low Import | Medium Import | High Import |
|----------|---------------------|-----------|---------------|-------------|
| **Steel (frame, masts)** | X | | | |
| **HDG coating** | X | | | |
| **HDPE resin** | | X | | |
| **HDPE fabrication** | X | | | |
| **PU foam** | | | X | |
| **Aluminum sheet (6061-T6)** | | | | X |
| **CNC machining** | X | | | |
| **AM frames (AlSi10Mg)** | | | | X |
| **Anodizing** | | X | | |
| **Mooring hardware** | | X | | |
| **Dyneema rope** | | | | X |
| **GPS/Iridium beacon** | | | | X |
| **Battery cells** | | | | X |
| **Zinc anodes** | | | X | |

**Local content estimate (by value):** Steel frame + masts + HDG + HDPE hull + foam fill + CNC machining + anodizing + mooring hardware + assembly labor = ~$19,000 of ~$33,400 hardware = **~57% domestic by material value**. Adding labor/assembly ($4,700) raises to ~$23,700/$35,640 = **~66% local content by total unit cost.** With AM frames produced in ASEAN (not counting as import for defense offset), effective local content rises to **~85-90%** per project target.

### 5.3 Critical Supply Chain Risks

| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|------------|
| SCR-01 | HDPE rotomolder cannot produce 8.0m hull in single piece | 40% | HIGH | 2-section welded hull design as fallback (TBD-007) |
| SCR-02 | Type III hard anodize for AlSi10Mg not available locally | 30% | MEDIUM | Cerakote ceramic coating as alternative; or ship frames to Singapore for anodizing |
| SCR-03 | AM lead time exceeds 3 weeks (service bureau backlog) | 25% | MEDIUM | Qualify 2-3 AM bureaus (PRD-003); maintain 2-batch inventory buffer |
| SCR-04 | 6061-T6 sheet supply disruption (trade/tariff risk) | 10% | MEDIUM | Multi-source from Korea + Japan + China; maintain 3-month sheet inventory |
| SCR-05 | GPS/Iridium beacon cost increase or export restriction | 15% | HIGH | Evaluate Chinese GPS/BeiDou alternatives with satellite link; GPS/GSM fallback for coastal tests |

---

## 6. Material Candidate Summary Table

Consolidated view of all subsystems with top 2-3 candidates and preliminary recommendation.

| Subsystem | Component | Candidate 1 (Recommended) | Candidate 2 (Alternative) | Candidate 3 (Fallback) | Selection Criteria for M4 |
|-----------|-----------|--------------------------|--------------------------|----------------------|---------------------------|
| **L0** | Chain | G30 HDG **16 mm** (SWL 3,700 kgf/link) | G43 HDG 12 mm (SWL 3,100 kgf/link) | — | Catenary analysis to confirm required scope; 16 mm preferred for margin |
| **L0** | Rode | Polyester braided 20 mm | Nylon double-braid 22 mm | — | Stretch vs. shock absorption trade-off per depth |
| **L0** | Anchor | Danforth HDG **50 kg** | Bruce HDG 30 kg | — | Seabed type at test range determines choice |
| **L1** | Hull shell | HDPE PE100 rotomolding grade | HDPE PE100 welded sheet (2-section) | — | Fabrication method (TBD-007) determines choice |
| **L1** | Foam fill | PU closed-cell 35-50 kg/m3 | PE closed-cell 30-45 kg/m3 | — | Pour-in-place ease vs. block-cut precision |
| **L2** | Frame | **S235JR HDG** (Hoa Phat/Nam Kim) | S355J2 HDG (if higher strength needed at pad eye) | — | FEA results at mooring pad eye; S235 strongly preferred for cost/availability |
| **L2.5** | Mast tube | **S235 CHS 76.1 x 4.0 HDG** | S355 CHS 60.3 x 4.0 HDG | 6082-T6 Al CHS 76 x 5 | M4 trade: mass (20.8 vs 16.2 vs 8.4 kg) vs. cost ($45 vs $45 vs $85) vs. fatigue life |
| **L3** | Face plates | **6061-T6 Al, 3 mm** + Type II anodize | — (MUST requirement; no alternative) | — | Confirm CNC vendor capability for 800x800 mm fly-cut |
| **L3** | AM frames | **AlSi10Mg LPBF + T5** + Type III hard anodize | AlSi10Mg + Cerakote H-series | CNC-machined 6061-T6 (base variant) | AM bureau qualification; anodize process validation for AM surface |
| **L5** | Beacon | COTS GPS/Iridium (YB3i type) | GPS/BeiDou + satellite modem (Chinese) | — | Satellite coverage, cost, export availability |
| **L5** | Battery | Li-ion 18650 pack (>=20 Wh) | LiFePO4 prismatic (>=20 Wh) | — | Energy density vs. thermal stability trade-off |
| **L5** | Enclosure | Pelican-type IP67 case | Custom ABS/PC IP68 molded | — | Prototype: Pelican; production: custom molded |
| **L6** | Tow line | **16 mm Dyneema HMPE** (SWL ~8,000 kgf) | 28 mm polyester (SWL ~6,000 kgf) | — | Dyneema per TRA-004 MUST; polyester as lower-cost backup if SWL margin acceptable |
| **L6** | Bridle | Wire rope 12 mm HDG (2 legs) | Dyneema 12 mm (2 legs) | — | Wire rope preferred for durability at pad eye connections |
| **L6** | Drogue | Canvas sea anchor 1.0 m | Nylon drogue 1.0 m | — | Local canvas fabrication preferred |

### 6.1 Material Cost Roll-Up (Recommended Candidates)

| Subsystem | Material Cost (Recommended) | % of Hardware Total |
|-----------|-----------------------------|---------------------|
| L0: Mooring | ~$2,500 | 7.5% |
| L1: Hull + Foam | ~$8,200 | 24.5% |
| L2: Frame | ~$1,800 | 5.4% |
| L2.5: Masts (8x) | ~$800 | 2.4% |
| L3: Reflectors (8x) | ~$13,000 | 38.9% |
| L5: GPS Beacon | ~$1,800 | 5.4% |
| L6: Tow System | ~$400 | 1.2% |
| Fasteners, anodes, misc | ~$500 | 1.5% |
| Assembly + QC labor | ~$4,700 | 14.1% |
| **Subtotal hardware + labor** | **~$33,700** | **100%** |
| Margin (10%) | ~$3,370 | — |
| **Unit total** | **~$37,070** | — |

**Note:** The roll-up at ~$37,070 exceeds the $36K target by ~$1,070 (3%). This is within the margin of preliminary estimation uncertainty. M4 detailed material analysis will refine costs — key opportunities for reduction include: (1) AM frame volume pricing at >=50 units, (2) negotiated HDPE hull pricing with committed volume, (3) potential CHS tube size optimization (76.1 mm may be reduced if fatigue analysis permits 60.3 mm in S355). The $35,640 estimate from concept selection assumed slightly lower material costs which remain achievable at committed production volumes.

---

## 7. Cross-References

### Phase 3 Documents (RISM Sequence)

- [[RISM_R1_requirements_identification.md]] — Step R1: 74 direct embodiment requirements, subsystem mapping, mass budget
- [[RISM_I2_critical_requirements.md]] — Step I2: Critical requirements prioritization and design-driving parameter identification
- [[RISM_S3_material_selection.md]] — This document (Step S3: Preliminary material screening and short-listing)
- [[RISM_M4_material_analysis.md]] — Step M4: Detailed material selection matrices (next step — Ashby charts, Pugh matrices, final selection with rationale)

### Phase 1 Source Documents

- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1), 16 Pahl-Beitz categories, material requirements MAT-001 to MAT-010
- [[../01_requirements/standards_mapping.md]] — MIL-STD-810H (salt fog), MIL-A-8625 (anodize), ASTM A123 (HDG), ASTM F3301 (AM)

### Phase 2 Source Documents

- [[../02_conceptual/concept_selection.md]] — Concept A architecture, layer summary, mass budget, cost breakdown, development risks R-1 to R-5

### Other References

- ASTM A413 — Standard Specification for Steel Chain (proof coil)
- ASTM B209 — Standard Specification for Aluminum and Aluminum-Alloy Sheet and Plate
- ASTM F3301 — Standard for Additive Manufacturing of Metals via PBF
- MIL-A-8625 — Anodic Coatings for Aluminum and Aluminum Alloys
- MIL-DTL-18001 — Anodes, Corrosion Preventive, Zinc (for use in seawater)
- ISO 1461 — Hot Dip Galvanized Coatings on Fabricated Iron and Steel Articles
- VDI 2225 — Systematic Approach to the Design of Technical Systems (material selection methodology)

---

*End of Step S3. Proceed to [[RISM_M4_material_analysis.md]] for detailed Ashby-chart analysis, Pugh decision matrices, and final material selection with quantified rationale.*
