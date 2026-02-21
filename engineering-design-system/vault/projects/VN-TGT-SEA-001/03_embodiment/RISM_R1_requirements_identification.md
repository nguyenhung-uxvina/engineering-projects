---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "R1 — Requirements Identification"
group: RISM
version: 1.0
created: 2026-02-10
status: draft
---

# Step R1: Requirements Identification — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Extract and organize all embodiment-determining requirements from the Phase 1 requirements list, mapping each to the selected Concept A architecture.
**Method:** Pahl & Beitz RISM Step R — Categorize by embodiment impact type
**Input:** [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1)
**Selected Concept:** Concept A "Baseline Optimized" (VDI 2225: 81.8%)

---

## 1. Embodiment Relevance Screening

Of the 116 Phase 1 requirements, each is classified by its impact on embodiment design:

- **Direct:** Requirement directly determines a physical dimension, material, load, or interface
- **Indirect:** Requirement influences design through constraints on performance, cost, or operation
- **Non-embodiment:** Administrative, schedule, or policy requirement with no physical design impact

### 1.1 Screening Summary

| Category | Total | Direct | Indirect | Non-Embodiment |
|----------|-------|--------|----------|----------------|
| Geometry (GEO) | 10 | **10** | 0 | 0 |
| Kinematics (KIN) | 5 | **4** | 1 | 0 |
| Forces (FOR) | 11 | **11** | 0 | 0 |
| Energy (ENR) | 2 | **2** | 0 | 0 |
| Material (MAT) | 10 | **10** | 0 | 0 |
| Signals (SIG) | 9 | **7** | 2 | 0 |
| Safety (SAF) | 7 | **5** | 2 | 0 |
| Ergonomics (ERG) | 7 | **4** | 3 | 0 |
| Production (PRD) | 8 | 3 | **5** | 0 |
| Quality (QUA) | 6 | 2 | 4 | 0 |
| Assembly (ASM) | 6 | **5** | 1 | 0 |
| Transport (TRA) | 6 | **4** | 2 | 0 |
| Operation (OPR) | 10 | **6** | 4 | 0 |
| Maintenance (MNT) | 5 | 1 | 2 | 2 |
| Costs (CST) | 7 | 0 | **7** | 0 |
| Schedule (SCH) | 6 | 0 | 0 | **6** |
| **TOTAL** | **116** | **74** | **33** | **8** |

**Key finding:** 74 requirements (64%) are directly embodiment-determining. These drive the physical design. 33 requirements (28%) indirectly influence through constraints. 8 requirements (7%) are schedule/admin.

---

## 2. Embodiment Requirements by Physical Domain

### 2.1 Geometric Requirements (Shape, Size, Envelope)

These requirements fix physical dimensions and spatial relationships.

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| GEO-001 | Platform diameter | 8.0 m ±0.1 m | Hull (L1) | HDPE pontoon outer diameter; determines rotomold size or welded section count |
| GEO-002 | Hull depth | 0.5 m ±0.05 m | Hull (L1) | Ring pontoon cross-section; sets freeboard at design displacement |
| GEO-003 | Reflector edge length | 0.8 m ±0.005 m | Reflectors (L3) | CNC face plate blanks 800×800×3 mm; AM frame inner geometry |
| GEO-004 | Number of reflectors | 8 at 45° spacing | Reflectors (L3) + Masts (L2.5) | 8 mast positions on hull perimeter at 45° intervals |
| GEO-005 | Reflector mounting height | 3.0–4.0 m AWL | Masts (L2.5) | Mast height ≥2.5 m above deck + 0.5 m deck-to-waterline = 3.0–3.5 m AWL minimum |
| GEO-006 | GPS beacon height | ≥4.5 m AWL | Masts (L2.5) | Highest point; dedicated mast or tallest reflector mast extension |
| GEO-007 | Displacement limit | ≤1,100 kg | All systems | Mass budget allocation across all subsystems; ~980 kg design target with 120 kg margin |
| GEO-008 | Design draft | ≤3 cm | Hull (L1) | Hull waterplane area (50.3 m² at 8.0 m) gives T = 1.9 cm at 980 kg |
| GEO-009 | Reflector clearance | ≥1.5 m between adjacent | Masts (L2.5) | At 8.0 m perimeter, arc spacing = 3.14 m; 0.8 m reflectors leave 2.34 m — PASS |
| GEO-010 | Mast structure | 8 masts, ≥2.5 m above deck, 45° spacing | Masts (L2.5) | Deck socket positions, mast tube length, base plate geometry |

### 2.2 Kinematic Requirements (Motion, Positioning)

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| KIN-001 | Maximum roll angle | ≤±7.5° in SS 6 | Hull (L1) | Hull geometry determines GM; BM = 210.3 m ensures stiff roll |
| KIN-003 | Weathervaning freedom | 360° unrestricted | Mooring (L0) | Single-point mooring (SPM) with swivel; no rotation stops |
| KIN-004 | Maximum heave | ≤±3.0 m in SS 6 | Hull (L1) | Platform follows wave surface; D/Lp < 0.15 at 8.0 m |
| KIN-005 | Tow speed | ≥3.0 kn in SS 5 | Hull (L1) + Tow (L6) | Hull drag coefficient; bridle geometry; drogue sizing |

### 2.3 Force/Load Requirements (Static, Dynamic, Cyclic)

These are the most critical embodiment drivers — they size structural members.

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| FOR-001 | Steady wind force | 1,814 N (185 kgf) at Bft 7 | Mooring (L0), Masts (L2.5) | Mooring line tension; mast base bending moment |
| FOR-002 | Gust wind force | 3,557 N (363 kgf) peak | Mooring (L0), Masts (L2.5) | Peak dynamic mooring load calculation; mast gust loading |
| FOR-003 | Wave drift force | 3,765 N (384 kgf) in SS 6 | Mooring (L0) | Mooring catenary analysis; scope ratio |
| FOR-004 | Steady mooring load | ≤578 kgf | Mooring (L0) | Chain sizing (12–16 mm G30); swivel rating |
| FOR-005 | Peak mooring load | ≤1,512 kgf | Mooring (L0) | Chain SWL; anchor holding capacity; pad eye design |
| FOR-006 | Mooring SWL | ≥4,536 kgf (3:1) | Mooring (L0) | Chain grade/size selection; shackle rating; pad eye weld sizing |
| FOR-007 | Anchor holding | ≥1,500 kgf | Mooring (L0) | Anchor type (Danforth/Bruce), weight (50 kg min), seabed type |
| FOR-008 | Tow line SWL | ≥7,524 kgf | Tow (L6) | Dyneema/polyester rope diameter; bridle hardware |
| FOR-009 | Green water on deck | Withstand 1,538 N (157 kgf) | Frame (L2), Masts (L2.5) | Mast base and deck socket must resist lateral green water impact |
| FOR-010 | Cyclic endurance | ≥40,000 cycles at ±7° | Masts (L2.5), Frame (L2) | Fatigue analysis at mast-deck socket weld; reflector mount bolts |
| FOR-011 | Mast bending capacity | ≥1,100 N·m per mast | Masts (L2.5) | Tube section selection: 60 mm × 4 mm steel minimum; base plate thickness |

### 2.4 Energy Requirements

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| ENR-001 | GPS battery life | ≥72 hours | GPS Beacon (L5) | Li-ion battery capacity; enclosure volume; mounting location |
| ENR-002 | GPS transmit rate | ≥1 Hz | GPS Beacon (L5) | Current draw determines battery sizing (72h × 1 Hz × power/fix) |

### 2.5 Material Requirements (Strength, Corrosion, Properties)

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| MAT-001 | Hull material | HDPE (rotomolded/welded) | Hull (L1) | Rotomold tooling or HDPE welding procedures; wall thickness |
| MAT-002 | Flotation fill | Closed-cell marine foam (PU/PE) | Hull (L1) | Foam density, pour-in-place or block cut; bond to HDPE |
| MAT-003 | Reflector face plate | 6061-T6 Al, 3 mm | Reflectors (L3) | CNC fly-cut blanks 800×800×3 mm; flatness <0.1 mm |
| MAT-004 | Reflector frame | AlSi10Mg (LPBF, T5) | Reflectors (L3) | AM build volume, orientation, heat treatment; corrosion protection |
| MAT-005 | Structural frame | S235 mild steel, HDG | Frame (L2) | Frame sections (angle, channel, plate); galvanizing spec |
| MAT-006 | Mooring chain | G30 proof coil, HDG | Mooring (L0) | 12–16 mm chain; catenary length per depth |
| MAT-007 | Face plate finish | Ra ≤10 µm | Reflectors (L3) | CNC surface roughness specification |
| MAT-008 | Face plate protection | Type II anodize ≥10 µm | Reflectors (L3) | Anodizing process specification; color (clear/black) |
| MAT-009 | AM frame protection | Type III hard anodize ≥25 µm | Reflectors (L3) | Hard anodize specification for AlSi10Mg |
| MAT-010 | Mast material | Galvanized mild steel or marine Al | Masts (L2.5) | Tube specification (60 mm OD × 4 mm wall min); galvanize spec |

### 2.6 Signal/Performance Requirements

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| SIG-001 | Peak RCS | ≥1,000 m² at X-band | Reflectors (L3) | 8 × 152.3 m² per reflector; geometry controls RCS |
| SIG-002 | Average RCS (360°) | ≥1,000 m² | Reflectors (L3) | 45° spacing ensures overlap; ~1,050 m² calculated |
| SIG-003 | Minimum RCS (worst angle) | ≥700 m² | Reflectors (L3) | Null depth between reflectors; 8-unit array gives ~770 m² |
| SIG-004 | Angular variation | ≤±2 dB through 360° | Reflectors (L3) | Reflector count and spacing; verified by RCS simulation |
| SIG-005 | RCS at ±7° roll | ≤1 dB degradation | Reflectors (L3) + Masts (L2.5) | Mast must maintain reflector alignment within ±7° |
| SIG-009 | Orthogonality tolerance | ≤±0.1° per reflector | Reflectors (L3) | AM frame precision; assembly alignment pins |
| SIG-007 | GPS position accuracy | ≤±5 m CEP | GPS Beacon (L5) | Standard GNSS module specification |

### 2.7 Safety Requirements (Structural)

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| SAF-005 | Tow bridle SWL | ≥3× peak tow load | Tow (L6) | Bridle hardware sizing; attachment point design |
| SAF-006 | Reflector/mast retention | Safety wire + locking pins | Masts (L2.5), Reflectors (L3) | Anti-vibration fastening; redundant retention |
| SAF-007 | Positive GM all conditions | GM > 0 through SS 6 | Hull (L1) | GM = 210+ m — inherently stable; no capsize possible |
| SAF-003 | Drift after mooring failure | Non-hazardous for ≥24h | GPS Beacon (L5) | GPS continues transmitting; HDPE hull remains afloat |
| SAF-004 | Environmental debris | Non-toxic, recoverable | Hull (L1), Foam | HDPE + PU foam = non-toxic marine materials |

### 2.8 Assembly Requirements (Field + Factory)

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| ASM-001 | Reflector assembly time | ≤30 min per reflector | Reflectors (L3) | Bolt count, alignment method, torque spec |
| ASM-003 | Field tools | Standard hand tools only | All field-assembled | No specialized equipment; M10-M16 wrenches, torque wrench |
| ASM-004 | Reflector-to-mast attachment | Bolted + Nylock + alignment pins + safety wire | Masts (L2.5) → Reflectors (L3) | Interface: mast top plate with 4-bolt pattern + 2 dowel pins |
| ASM-005 | Mooring pad eye | Through-bolted, 200×200×10 mm backing plate | Frame (L2) → Mooring (L0) | Interface: 4× M16 through-bolts; backing plate distributes load |
| ASM-006 | Field mast erection | ≤15 min total (8 masts, 2-person) | Masts (L2.5) | Socket-insert design; locking pin; ~31 kg per mast+reflector unit |

### 2.9 Transport Requirements

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| TRA-001 | Container fit | ≥1 target per 40 ft container | Hull (L1) | 8.0 m hull may need 2-section design for 12.2 m container |
| TRA-002 | Road width limit | ≤2.5 m per section | Hull (L1) | Determines 2-section hull split or oversize permit |
| TRA-003 | Tow configuration | 2-point bridle + drogue | Tow (L6) | Bridle attachment points on hull; drogue size/attachment |
| TRA-004 | Tow line specification | 16 mm Dyneema, SWL ≥8,000 kgf | Tow (L6) | Rope specification and termination hardware |

### 2.10 Operational Requirements (Environment)

| ID | Requirement | Value | Concept A Subsystem | Design Impact |
|----|-------------|-------|---------------------|---------------|
| OPR-002 | Survival sea state | SS 5-6 for 72h | All structural | Drives all structural sizing and safety factors |
| OPR-003 | Survival wind | Bft 6-7 (gusts to 46 kn) | Masts (L2.5), Mooring (L0) | Wind loading on masts and reflectors |
| OPR-005 | Water depth range | 10–80 m | Mooring (L0) | 3 mooring kit variants; catenary scope ratios |
| OPR-007 | Temperature range | -5°C to +55°C | All materials | Material selection must cover range; no brittle fracture |
| OPR-009 | Salt spray | Continuous for 72h | All exposed | All materials must be marine-grade or protected |
| OPR-010 | Missile compatibility | X-band active radar seeker | Reflectors (L3) | RCS at 9.4 GHz; no RF-active components to interfere |

---

## 3. Subsystem-to-Requirement Mapping

Each Concept A subsystem is mapped to the requirements it must satisfy:

### 3.1 Mapping Summary

| Subsystem (Layer) | Direct Req. | Indirect Req. | Total | Critical Drivers |
|--------------------|-------------|---------------|-------|-----------------|
| **L0: Mooring** | 8 | 3 | 11 | FOR-005, FOR-006, FOR-007, OPR-005 |
| **L1: Hull** | 10 | 5 | 15 | GEO-001, GEO-002, GEO-007, MAT-001 |
| **L2: Frame** | 5 | 3 | 8 | MAT-005, FOR-009, ASM-005 |
| **L2.5: Masts** | 9 | 2 | 11 | GEO-005, GEO-010, FOR-010, FOR-011 |
| **L3: Reflectors** | 14 | 4 | 18 | SIG-001–SIG-005, SIG-009, GEO-003, MAT-003–004 |
| **L5: GPS Beacon** | 4 | 2 | 6 | ENR-001, ENR-002, SIG-007, GEO-006 |
| **L6: Tow System** | 4 | 1 | 5 | FOR-008, TRA-003, TRA-004, SAF-005 |
| **Cross-cutting** | — | 13 | 13 | OPR-002, OPR-009, CST-001, ERG-001–005 |

### 3.2 Detailed Subsystem Mapping

#### L0: Storm Mooring System

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| FOR-004 | Steady load ≤578 kgf | Chain + catenary absorbs steady loads |
| FOR-005 | Peak load ≤1,512 kgf | Chain SWL must exceed with 3:1 factor |
| FOR-006 | SWL ≥4,536 kgf | 12–16 mm G30 chain; rated shackles |
| FOR-007 | Anchor hold ≥1,500 kgf | Danforth 50 kg or Bruce 30 kg |
| MAT-006 | G30 proof coil, HDG | Standard marine supply chain |
| KIN-003 | 360° weathervane | SPM with swivel at anchor-chain junction |
| OPR-005 | 10–80 m depth | 3 mooring kits (scope ratio per depth) |
| ASM-005 | Through-bolted pad eye | Central pad eye with 200×200×10 mm backing plate |

#### L1: HDPE Hull Platform

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| GEO-001 | 8.0 m ±0.1 m diameter | Circular pontoon ring, rotomolded or 2-section welded |
| GEO-002 | 0.5 m ±0.05 m depth | Ring cross-section determines freeboard/draft |
| GEO-007 | ≤1,100 kg total | Hull mass ~350 kg target (incl. foam) |
| GEO-008 | Draft ≤3 cm | 50.3 m² waterplane at 980 kg → T = 1.9 cm |
| MAT-001 | HDPE | UV/salt/impact resistant; 20+ year marine life |
| MAT-002 | Closed-cell foam fill | Pour-in-place PU foam; >98% reserve buoyancy |
| KIN-001 | Roll ≤±7.5° | BM = 210.3 m; GM extremely high |
| SAF-007 | Positive GM all conditions | Cannot capsize — physics guarantee |
| TRA-001 | Fit 40 ft container | May need 2-section hull with bolted/welded joint |
| TRA-002 | ≤2.5 m road width | 2-section split at 4.0 m diameter each half |

#### L2: Steel Structural Frame

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| MAT-005 | S235, HDG | Angle/channel/plate; welded fabrication |
| FOR-009 | Green water 157 kgf | Frame stiffness resists deck loading |
| ASM-005 | Mooring pad eye | Through-bolted to frame; distributes to hull |
| GEO-010 | 8 deck sockets | Welded sockets at 45° intervals on frame perimeter |
| OPR-009 | Salt spray 72h | Hot-dip galvanized (≥85 µm per ASTM A123) |

#### L2.5: Mast System (8 units)

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| GEO-005 | 3.0–4.0 m AWL | Mast height ≥2.5 m above deck (deck at ~0.5 m AWL) |
| GEO-006 | GPS at ≥4.5 m AWL | One mast extended or separate GPS mast |
| GEO-010 | 8 masts, 45° spacing | Deck socket positions at R = 3.7 m from center |
| MAT-010 | Galvanized steel tube | 60 mm OD × 4 mm wall, HDG |
| FOR-010 | 40,000 fatigue cycles | Weld toe at socket-mast interface; fatigue detail category |
| FOR-011 | ≥1,100 N·m bending | Section modulus: W = 4,637 mm³ for 60×4 tube → capacity 1,303 N·m |
| ASM-006 | 15 min erection (8 masts) | Socket-insert with locking pin; 2-person, no crane |
| SAF-006 | Locking pins + safety wire | Redundant retention against vibration loosening |
| OPR-003 | Bft 6-7 survival | Gust loading on mast + reflector at 3 m arm |

#### L3: Hybrid Corner Reflectors (8 units)

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| GEO-003 | 0.8 m ±0.005 m edge | CNC face plate blank dimensions |
| GEO-004 | 8 units, 45° spacing | One reflector per mast |
| SIG-001 | Peak RCS ≥1,000 m² | σ = 12πa⁴/λ² = 152.3 m² per; 8 × 152.3 = 1,218 m² |
| SIG-002 | Avg RCS ≥1,000 m² | ~1,050 m² with 8-unit 45° array |
| SIG-003 | Min RCS ≥700 m² | ~770 m² at deepest null between reflectors |
| SIG-004 | ≤±2 dB variation | 8-unit array at 45° gives ±1.5 dB max variation |
| SIG-005 | ≤1 dB loss at ±7° roll | Trihedral tolerance ±15° → <3 dB; at ±7° only ~0.5 dB |
| SIG-009 | Orthogonality ≤±0.1° | AM frame alignment features; assembly dowel pins |
| MAT-003 | 6061-T6, 3 mm | CNC fly-cut face plates |
| MAT-004 | AlSi10Mg LPBF, T5 | AM structural frame; controls orthogonality |
| MAT-007 | Ra ≤10 µm | CNC surface finish (adequate for λ = 32 mm) |
| MAT-008 | Type II anodize ≥10 µm | Corrosion protection for 6061-T6 faces |
| MAT-009 | Type III hard anodize ≥25 µm | Corrosion protection for AlSi10Mg frame |
| ASM-004 | Bolted + Nylock + pins + safety wire | 4-bolt mount with 2 alignment dowels |

#### L5: GPS Beacon System

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| ENR-001 | 72h battery life | Li-ion pack ~20 Wh; waterproof enclosure |
| ENR-002 | 1 Hz position fix | GNSS module + Iridium/satellite relay |
| SIG-007 | ≤±5 m CEP | Standard GNSS performance |
| GEO-006 | Mounted ≥4.5 m AWL | On tallest mast or dedicated GPS mast |

#### L6: Tow/Deployment System

| Requirement | Value | Design Feature |
|-------------|-------|----------------|
| FOR-008 | Tow line SWL ≥7,524 kgf | 16 mm Dyneema (SWL 8,000 kgf) |
| TRA-003 | 2-point bridle + drogue | 60° spread bridle; trailing drogue for yaw stability |
| TRA-004 | 16 mm Dyneema, 50–100 m | Rope specification |
| SAF-005 | Bridle SWL ≥3× peak | Hardware rated per marine standards |

---

## 4. Requirements Density Map

Identifies where design constraints are tightest (highest requirement density = highest design risk):

| Subsystem | Req Density | Risk Level | Notes |
|-----------|-------------|------------|-------|
| **L3: Reflectors** | **18 requirements** | **HIGH** | Most constrained subsystem — RCS, material, tolerance, protection |
| **L1: Hull** | 15 requirements | HIGH | Size, weight, buoyancy, stability, transport all constrained |
| **L2.5: Masts** | 11 requirements | MEDIUM-HIGH | Structural, fatigue, erection, all interrelated |
| **L0: Mooring** | 11 requirements | MEDIUM-HIGH | Loads, depth range, pre-deployment concept |
| **L2: Frame** | 8 requirements | MEDIUM | Straightforward structural steel fabrication |
| **L5: GPS** | 6 requirements | LOW | COTS component with battery pack |
| **L6: Tow** | 5 requirements | LOW | Standard marine tow equipment |

---

## 5. Mass Budget Allocation

Based on the 116 requirements and ≤1,100 kg displacement limit, the mass budget is:

| Subsystem | Mass Target | % of Total | Design Margin |
|-----------|-------------|------------|---------------|
| L1: Hull (HDPE + foam) | 350 kg | 35.7% | ±20 kg |
| L2: Steel frame | 150 kg | 15.3% | ±15 kg |
| L2.5: Mast system (8×) | 130 kg (16.3 kg each) | 13.3% | ±10 kg |
| L3: Reflectors (8×) | 120 kg (15 kg each) | 12.2% | ±5 kg |
| L0: Mooring pad eye + hardware | 80 kg | 8.2% | ±10 kg |
| L5: GPS beacon + battery | 5 kg | 0.5% | ±1 kg |
| L6: Tow hardware (on-hull) | 15 kg | 1.5% | ±3 kg |
| Fasteners, misc, margin | 130 kg | 13.3% | Design reserve |
| **TOTAL** | **980 kg** | **100%** | **120 kg under limit** |

**Note:** Mooring chain/rode/anchor mass is NOT included in platform displacement — it is separate equipment deployed independently.

---

## 6. Interface Requirements Summary

From the embodiment requirements, 7 critical physical interfaces are identified:

| Interface ID | Between | Key Requirements | Interface Type | Criticality |
|-------------|---------|------------------|----------------|-------------|
| **IF-01** | Hull (L1) ↔ Frame (L2) | GEO-001, FOR-009 | Mechanical (bolted/welded) | HIGH — load path for mooring |
| **IF-02** | Frame (L2) ↔ Mooring (L0) | ASM-005, FOR-005, FOR-006 | Mechanical (through-bolted pad eye) | CRITICAL — peak 1,512 kgf |
| **IF-03** | Frame (L2) ↔ Masts (L2.5) | GEO-010, ASM-006 | Mechanical (socket-insert) | HIGH — field assembly interface |
| **IF-04** | Masts (L2.5) ↔ Reflectors (L3) | ASM-004, SIG-009 | Mechanical (bolted + pinned) | HIGH — alignment critical (±0.1°) |
| **IF-05** | Mast (L2.5) ↔ GPS (L5) | GEO-006 | Mechanical (clamp/bracket) | LOW — lightweight component |
| **IF-06** | Hull (L1) ↔ Tow (L6) | TRA-003, SAF-005 | Mechanical (padeyes + shackles) | MEDIUM — tow loads |
| **IF-07** | Hull (L1 sections) | TRA-001, TRA-002 | Mechanical (bolted flange or welded) | HIGH — if 2-section hull |

---

## 7. TBD Items Requiring Embodiment Resolution

| TBD | Description | Embodiment Step | Priority |
|-----|-------------|-----------------|----------|
| TBD-007 | Hull fabrication method (1-piece vs 2-section) | D8, O13 | HIGH |
| TBD-008 | Transport solution (oversize vs disassembly) | D8, P15 | HIGH |
| TBD-009 | CNC flatness specification (<0.1 mm TBV) | D9 | MEDIUM |
| TBD-010 | Depth-dependent mooring kits (3 variants) | D9, C14 | MEDIUM |
| TBD-011 | Mast design (free-standing vs guyed, chain size) | D8, D9 | HIGH |

---

## Cross-References

- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1), source document
- [[../02_conceptual/concept_selection.md]] — Concept A architecture, risk register
- [[../02_conceptual/function_structure.md]] — Function-to-subsystem mapping
- [[../02_conceptual/morphological_matrix.md]] — Concept A detailed description
- [[RISM_I2_critical_requirements.md]] — Step I2: Critical requirements prioritization (next)
- [[RISM_S3_material_selection.md]] — Step S3: Material candidate screening
- [[RISM_M4_material_analysis.md]] — Step M4: Material selection matrices
