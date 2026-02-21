---
project: VN-TGT-SEA-001
phase: 4
type: detail_design
document: "Manufacturing Drawing Specifications"
version: 1.0
created: 2026-02-11
status: draft
---

# Manufacturing Drawing Specifications — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Define the complete textual manufacturing drawing specification from which a CAD drafter produces production-ready engineering drawings. All dimensions, tolerances, GD&T callouts, material callouts, surface finishes, process notes, and inspection requirements for every fabricated component.
**Input:** [[../03_embodiment/DECS_D9_detail_specification.md]] (master engineering specification), [[../03_embodiment/PRAD_D8_design_structure.md]] (structural analysis), [[../03_embodiment/PRAD_A7_architecture_definition.md]] (architecture, modules, interfaces), [[../03_embodiment/OCP_C14_cost_analysis.md]] (BOM references), [[../03_embodiment/OCP_P15_production_planning.md]] (manufacturing processes, suppliers), [[../03_embodiment/DECS_S12_standards_compliance.md]] (welding, material, surface treatment standards)

---

## 1. Drawing System Overview

### 1.1 Drawing Numbering System

All drawings use the prefix **TRI-H** followed by the module code, part sequence number, and revision letter.

| Field | Format | Example | Description |
|-------|--------|---------|-------------|
| Project prefix | TRI-H | TRI-H | Fixed for this product |
| Module code | -M1, -M2 ... -M8, -SYS, -IF | TRI-H-M1 | Module per A7 decomposition |
| Part number | -001 to -999 | TRI-H-M1-001 | Sequential within module |
| Revision | -A, -B, -C ... | TRI-H-M1-001-A | Alpha revision; A = first release |

**Examples:**
- `TRI-H-M1-001-A` -- Hull Assembly drawing, first release
- `TRI-H-M4-002-A` -- CNC Face Plate detail, first release
- `TRI-H-IF-04-A` -- Reflector-to-Mast interface drawing, first release
- `TRI-H-SYS-001-A` -- System General Arrangement, first release

### 1.2 Drawing Standards

| Standard | Application |
|----------|-------------|
| ISO 128-20 / ISO 128-24 | Technical drawing -- general principles of presentation (lines, views) |
| ISO 1101:2017 | GD&T -- geometrical tolerancing |
| ISO 2768-mK | General tolerances: medium (linear), coarse (angular) -- DEFAULT for all dimensions without explicit tolerance |
| ISO 5457 | Drawing sheet sizes and formats |
| ISO 7200 | Title block data fields |
| ISO 8015 | Principle of independency (fundamental tolerancing principle) |

### 1.3 Drawing Conventions

| Convention | Value |
|------------|-------|
| Sheet sizes | A1 (841 x 594 mm) for assemblies; A3 (420 x 297 mm) for detail parts |
| Projection method | First angle projection (ISO standard, symbol in title block) |
| Dimension units | Millimeters (mm); angular dimensions in degrees (deg) |
| General tolerance class | ISO 2768-mK unless otherwise specified on individual dimensions |
| Scale | Assemblies: 1:20 or 1:25 (A1); Details: 1:5 or 1:2 (A3); full-scale details as needed |
| Line conventions | ISO 128 -- thick continuous for visible edges, thin dashed for hidden edges, thin chain for centerlines |
| Surface finish symbols | ISO 1302 -- Ra values in micrometers |
| Weld symbols | ISO 2553 / AWS A2.4 -- fillet, butt, and groove weld symbols |
| Material callout | In title block and on detail views per ISO 7200 |
| Revision table | Bottom-right corner per ISO 7200; track all drawing changes |

### 1.4 Tolerance Philosophy

Per [[../03_embodiment/DECS_D9_detail_specification.md]] Section 1:

| Tier | Tolerance Class | Application |
|------|----------------|-------------|
| T1 -- Precision | <=+/-0.05 mm linear, <=+/-0.05 deg angular | Reflector frame datum surfaces, dowel pin holes |
| T2 -- Close | +/-0.1 to +/-0.5 mm, +/-0.1 deg angular | Face plate flatness, mast top plate hole pattern |
| T3 -- Medium | +/-1 to +/-5 mm, +/-0.5 deg angular | Frame members, deck socket positions, mast length |
| T4 -- Coarse | +/-5 to +/-100 mm, +/-2 deg angular | Hull diameter, hull depth, foam fill density |

---

## 2. Drawing Register

### 2.1 System and Assembly Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-SYS-001 | System General Arrangement (Plan, Side, Section) | A1 | 1:25 | Required |
| TRI-H-SYS-002 | System Mass Budget and CG Diagram | A3 | NTS | Required |
| TRI-H-SYS-003 | System Weld Schedule | A3 | NTS | Required |
| TRI-H-SYS-004 | System Surface Treatment Schedule | A3 | NTS | Required |
| TRI-H-SYS-005 | System Fastener Schedule | A3 | NTS | Required |

### 2.2 M1: Hull Assembly Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-M1-001 | Hull Assembly (2-Section Ring Pontoon) | A1 | 1:20 | Required |
| TRI-H-M1-002 | Hull Section Detail (Half-Disc) | A1 | 1:10 | Required |
| TRI-H-M1-003 | Hull Section Joint Detail (IF-07) | A3 | 1:5 | Required |
| TRI-H-M1-004 | Scupper Drain Detail | A3 | 1:2 | Required |
| TRI-H-M1-005 | Foam Fill Port Detail | A3 | 1:2 | Required |

### 2.3 M2: Structural Frame Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-M2-001 | Frame Assembly | A1 | 1:20 | Required |
| TRI-H-M2-002 | Deck Socket Detail (x8) | A3 | 1:2 | Required |
| TRI-H-M2-003 | Mooring Pad Eye Assembly | A3 | 1:5 | Required |
| TRI-H-M2-004 | Tow Padeye Detail (x2) | A3 | 1:2 | Required |
| TRI-H-M2-005 | Center Hub Plate Detail | A3 | 1:5 | Required |
| TRI-H-M2-006 | Perimeter Ring Beam Layout | A1 | 1:10 | Required |

### 2.4 M3: Mast Assembly Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-M3-001 | Mast Assembly (x8 Identical) | A3 | 1:10 | Required |
| TRI-H-M3-002 | Mast Base Plate Detail | A3 | 1:2 | Required |
| TRI-H-M3-003 | Mast Top Plate Detail | A3 | 1:2 | Required |
| TRI-H-M3-004 | Mast Base Gusset Detail (x4 per mast) | A3 | 1:1 | Required |

### 2.5 M4: Reflector Assembly Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-M4-001 | Reflector Assembly (x8 Identical) | A1 | 1:5 | Required |
| TRI-H-M4-002 | CNC Face Plate Detail (x24 Identical) | A3 | 1:5 | Required |
| TRI-H-M4-003 | AM Frame Detail (x8 Identical) | A1 | 1:5 | Required |
| TRI-H-M4-004 | AM Frame Datum Surface Detail | A3 | 1:1 | Required |

### 2.6 M5-M8: Pre-Assembly, Beacon, Mooring, and Tow Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-M5-001 | Mast-Reflector Pre-Assembly (IF-04) | A3 | 1:10 | Required |
| TRI-H-M6-001 | GPS Beacon Installation Drawing | A3 | 1:5 | Required |
| TRI-H-M7-001 | Mooring Kit Assembly (3 Depth Variants) | A1 | 1:100 | Required |
| TRI-H-M8-001 | Tow Kit Assembly (Bridle + Drogue) | A3 | 1:20 | Required |

### 2.7 Interface Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-IF-01 | Frame-to-Hull Interface (IF-01) | A3 | 1:5 | Required |
| TRI-H-IF-02 | Pad Eye to Mooring Chain Interface (IF-02) | A3 | 1:5 | Required |
| TRI-H-IF-03 | Deck Socket to Mast Base Interface (IF-03) | A3 | 1:2 | Required |
| TRI-H-IF-04 | Reflector to Mast Top Interface (IF-04) | A3 | 1:2 | Required |
| TRI-H-IF-05 | GPS Beacon to Mast Interface (IF-05) | A3 | 1:2 | Required |
| TRI-H-IF-06 | Tow Padeye to Bridle Interface (IF-06) | A3 | 1:5 | Required |
| TRI-H-IF-07 | Hull Section Joint Interface (IF-07) | A3 | 1:5 | Required |

### 2.8 Installation Drawings

| Drawing # | Title | Sheet | Scale | Status |
|-----------|-------|-------|-------|--------|
| TRI-H-INS-001 | Field Assembly Sequence (Mast Erection) | A3 | NTS | Required |
| TRI-H-INS-002 | Mooring Connection Procedure | A3 | NTS | Required |
| TRI-H-INS-003 | Transport and Packaging Arrangement | A1 | 1:25 | Required |

**Total drawings: 33**

---

## 3. M1: Hull Assembly Drawings

### 3.1 TRI-H-M1-001: Hull Assembly (2-Section Ring Pontoon)

**General:**
- Overall outside diameter: 8,000 mm +/-100 mm (T4), measured across max chord at deck level
- Hull inner diameter (open deck): approximately 7,000 mm
- Hull depth (overall): 500 mm +/-50 mm (T4), measured at ring cross-section
- Ring width (pontoon cross-section): 500 mm nominal +/-30 mm (T4), inner to outer hull wall
- Configuration: 2 semicircular half-sections joined at IF-07 (diameter plane)
- Material: HDPE PE100, carbon-black UV-stabilized per ASTM D3350 Cell Class 345464C
- Melt flow index: <=0.4 g/10 min; density: 940-960 kg/m3
- Color: Black (carbon-black stabilized) or olive drab per customer specification
- Hull mass (shell only, no foam): 200 +/-30 kg

**Deck surface:**
- Flat, self-draining, non-skid texture
- Flatness: +/-10 mm (T4)
- Non-skid: molded-in diamond pattern or post-applied marine deck paint (grey textured)

**Scupper drains:**
- Quantity: 8x at hull inner edge
- Hole diameter: 100 mm +/-5 mm
- Position: equally spaced at 45 deg around inner perimeter
- Position tolerance: +/-20 mm along perimeter

**Frame mounting holes (IF-01):**
- Quantity: 84x holes around inner hull wall perimeter
- Hole diameter: 13 mm (clearance for M12)
- Spacing: 300 mm nominal between holes along hull inner circumference (~25.1 m)
- Position tolerance: +/-2 mm

**Tow padeye holes (IF-06):**
- Quantity: 2 sets of 4 holes (8 total)
- Hole diameter: 13 mm (clearance for M12)
- Pattern: 100 x 100 mm square per padeye
- Positions: R = 3,800 mm from hull center, +/-30 deg from bow axis (North), symmetric port/starboard
- Position tolerance: +/-20 mm along perimeter

**Hull marking zone:**
- Location: outer hull wall, one quadrant (0 deg / North side)
- Content: project code (VN-TGT-SEA-001), serial number, hull mass (measured), year of manufacture
- Method: stencil + marine marking paint, characters >= 50 mm height
- Durability: UV-resistant ink, legible after 12 months outdoor exposure

**Foam fill specification (shown in section view):**
- Material: closed-cell rigid polyurethane foam, marine grade, pour-in-place, 2-component
- Standard: ASTM D1622 (density), ASTM D2842 (water absorption), ASTM D1621 (compressive strength)
- Density: 32-48 kg/m3 (target 40 kg/m3), tolerance +/-5 kg/m3
- Fill factor: >=80% of hull internal volume (leave <=20% void for drainage and inspection)
- Foam mass: 100-150 kg (target 121 kg at 40 kg/m3)
- Water absorption: <=3% by volume after 48h immersion per ASTM D2842
- Compressive strength: >=150 kPa at 10% deformation per ASTM D1621

### 3.2 TRI-H-M1-002: Hull Section Detail (Half-Disc)

**Shell:**
- Shape: semicircular ring pontoon (half of 8,000 mm OD ring)
- Wall thickness: >=8 mm minimum, 12 mm nominal (rotomolded: 8-15 mm typical)
- Wall thickness tolerance: +0/-0 on minimum (verify at 8 sampling points per section via UT gauge)
- No maximum wall thickness (rotomolding variation accepted)

**IF-07 flange detail:**
- Flange width: 60 mm integral HDPE lip on each mating face (+/-5 mm)
- Flange thickness: 20 mm +/-2 mm
- Bolt pattern: 24x M10 clearance holes at ~520 mm spacing along joint perimeter (~12.6 m total)
- Bolt hole diameter: 11 mm +/-0.5 mm (clearance for M10)
- Alignment dowel locations: 3x 12 mm holes at 120 deg spacing for nylon alignment pins

**Foam fill ports:**
- Quantity: 2 per hull section (4 total)
- Diameter: 50 mm (+/-2 mm)
- Location: deck surface, spaced at 1/3 and 2/3 of section arc length
- Closure: threaded HDPE plug, sealed with Sikaflex 291 after foam cure

**UT measurement points (wall thickness verification):**
- 8 points per section (16 total), marked on drawing with "UT" symbol
- Locations: 4 on outer wall (90 deg spacing), 4 on inner wall (90 deg spacing)
- Accept: >=8 mm at all points

### 3.3 TRI-H-M1-003: IF-07 Joint Detail

**Cross-section through joint (full-size detail at 1:2):**

- Two HDPE flanges mated face-to-face
- EPDM gasket strip: 40 mm wide x 5 mm thick, continuous, Shore A 60 +/-5
- Gasket groove: machined or formed in one flange face, 40 mm wide x 3 mm deep
- Gasket compression (installed): 3.5-4.0 mm (30% of free thickness)

**Bolt pattern:**
- 24x M10 x 40 SS316 A4-70 hex bolts
- Spacing: ~520 mm along perimeter (+/-10 mm)
- Torque: 25 +/-3 N-m
- Tightening sequence: star pattern, 3 passes (finger tight, 15 N-m, 25 N-m)
- Washers: flat washer + fender washer on outer HDPE face

**Steel backing channel:**
- Section: C100 x 50 x 5 HDG steel
- Length: full joint length inside hull (continuous or in 2 halves)
- Coating: HDG >=85 um per ASTM A123
- Attachment: 6x M10 x 50 Gr 8.8 HDG through-bolts per side (12 total)
- Torque: 40 +/-3 N-m

**Section-to-section alignment:**
- Outer diameter match across joint: +/-3 mm step maximum
- Alignment dowels: 3x 12 mm nylon 6/6 pins at 120 deg spacing (push fit)

**External sealant:**
- Sikaflex 291 marine sealant, continuous 5 mm bead along exterior joint line
- Applied after bolt-up, secondary seal

---

## 4. M2: Structural Frame Drawings

### 4.1 TRI-H-M2-001: Frame Assembly

**Material and general notes:**
- Material: S235JR (or Q235B equivalent) per EN 10025-2
- Yield strength (min): 235 MPa (mill certificate required)
- Surface prep before HDG: Sa 2.5 (near-white blast) per ISO 8501-1
- Hot-dip galvanize: >=85 um average, >=70 um local minimum per ASTM A123 / ISO 1461
- All welds: fillet welds unless noted; E43xx electrode (AWS A5.1), continuous all-around unless noted
- Weld inspection: visual 100%; UT on pad eye full-penetration weld per AWS D1.1
- General tolerance: ISO 2768-m (medium class)

**Perimeter ring beam:**
- Section: L50 x 50 x 5 equal angle per EN 10056-1
- Ring diameter (neutral axis): 7,200 mm +/-5 mm (fits inside hull inner wall)
- Fabrication: 4x quarter-arc segments (or 8x octant segments), butt-welded
- Joint welds: full-penetration butt weld at ring segment joints, weld gap <=2 mm
- Cross-member connections: 6 mm fillet weld

**Radial cross members:**
- Quantity: 8x radial beams from center hub to perimeter ring
- Angular spacing: 45 deg +/-0.5 deg
- Section: L50 x 50 x 5 equal angle per EN 10056-1
- Length: ~3,600 mm (center hub to ring), +/-3 mm; fit to actual ring dimension
- Connection to ring: 6 mm fillet weld, both sides of angle
- Connection to center hub: 6 mm fillet weld to central plate

**Center hub plate:**
- Dimensions: 300 x 300 x 10 mm S235
- Position: geometric center of frame, +/-5 mm
- All 8 radial beams welded to this plate with 6 mm fillet weld

**Deck socket positions (8x):**
- Radius from frame center: 3,200 mm +/-5 mm
- Angular spacing: 45 deg +/-0.5 deg (positions R1 through R8)
- Socket orientation: vertical axis perpendicular to frame plane +/-0.5 deg

**Central mooring pad eye location:**
- At geometric center, directly above hub plate
- See TRI-H-M2-003 for detail

**Tow padeye locations (2x):**
- At R = 3,800 mm from center, +/-30 deg from North axis (bow)
- Symmetric port/starboard
- See TRI-H-M2-004 for detail

### 4.2 TRI-H-M2-002: Deck Socket Detail (x8 Identical)

**Socket sleeve:**
- Tube: 116 mm OD x 8 mm wall (100 mm ID after weld cleanup), 150 mm tall
- Material: seamless or ERW tube, S235
- Internal bore finish: machined or reamed to Ra <=12.5 um
- Internal bore: 100 +0/-1 mm after weld cleanup
- Chamfer at top: 2 mm x 45 deg lead-in chamfer (eases field mast insertion)

**Base plate:**
- Dimensions: 160 x 160 x 8 mm S235
- Flatness: +/-1 mm
- Welded around socket bottom: 6 mm fillet weld, continuous all-around (circumferential)
- Weld throat: >=5 mm (per D8 Section 3.2: weld stress 21.4 MPa, utilization 16.6%)

**Locking pin hole:**
- Diameter: 12 mm through socket wall (both sides)
- Position: 100 mm above base plate (top of socket flange)
- Position tolerance: +/-0.5 mm
- Note: "Cross-drill after assembly trial fit with mast -- holes must align through both socket walls and mast tube"

**Drain hole:**
- Diameter: 6 mm at socket bottom (lowest point)
- Purpose: prevents water pooling and corrosion

**Bolt pattern (base plate to frame):**
- 4x M12 clearance holes on 120 mm dia bolt circle
- Hole diameter: 13 mm
- Hole position tolerance: +/-0.5 mm
- Fasteners: M12 x 35 Gr 8.8 HDG
- Torque: 80 +/-5 N-m with hardened washers

### 4.3 TRI-H-M2-003: Mooring Pad Eye Assembly

**Eye plate:**
- Material: S235JR, 80 mm wide x 20 mm thick
- Height: 120 mm above backing plate
- Pin hole: 80 mm ID (ring formed from 25 mm dia round bar, welded to eye plate top, full-penetration weld)
- Welded edges rounded: R >=3 mm for stress concentration reduction
- Edge taper: plate tapers from 20 mm center to 12 mm at edges

**Eye plate weld:**
- Type: full-penetration groove weld to backing plate, both sides
- Electrode: E7018 low-hydrogen
- Preheat: >=50 deg C minimum
- Inspection: UT per AWS D1.1, Section 6
- Accept: no defects >=3 mm
- Note: "CRITICAL WELD -- load path for all mooring force"

**Backing plate (upgraded from 10 mm per D8 Section 3.1):**
- Dimensions: 200 x 200 x 14 mm S235
- Flatness: +/-0.5 mm
- Through-bolted to hub plate and cross members

**Bolt pattern:**
- 8x M16 Gr 8.8 HDG hex bolts on 150 x 150 mm square pattern
- Hole diameter: 17 mm clearance in backing plate, hub plate, and cross members
- Hole position tolerance: +/-0.5 mm
- Torque: 190 +/-10 N-m
- Hardened washers under heads and nuts

**Sacrificial zinc anode:**
- 0.5 kg zinc block, bolted adjacent to pad eye ring
- Attachment: M10 x 30 SS316 bolt through anode and backing plate
- Torque: 15 +/-2 N-m

**Proof load requirement (note on drawing):**
- "PROOF LOAD TEST REQUIRED: 1.5x SWL = 6,804 kgf (66,766 N) applied vertically through pad eye ring. No permanent deformation. Certify and stamp before first deployment."

### 4.4 TRI-H-M2-004: Tow Padeye Detail (x2 Identical)

**Ring:**
- Material: 20 mm dia round bar S235, 60 mm ID ring
- Welded to base plate (full-circumference fillet weld)
- Accepts 16 mm shackle pin

**Base plate:**
- Dimensions: 150 x 150 x 10 mm S235
- Through-bolted to hull + frame perimeter ring

**Bolt pattern:**
- 4x M12 Gr 8.8 HDG on 100 x 100 mm square
- Hole diameter: 13 mm clearance
- Hole position tolerance: +/-1 mm
- Torque: 80 +/-5 N-m
- With 50 x 50 x 5 SS316 fender washers on HDPE side

**Position:**
- 2x at R = 3,800 mm from center, +/-30 deg from North (bow axis)
- Position tolerance: +/-20 mm along perimeter
- Symmetric port/starboard

**SWL note on drawing:**
- "SWL >=3,762 kgf per padeye (3:1 on 1,254 kgf per-leg peak tow load)"

---

## 5. M3: Mast Assembly Drawings

### 5.1 TRI-H-M3-001: Mast Assembly (x8 Identical)

**Mast tube:**
- Tube OD: 60.3 mm (DN50 Schedule 40 equivalent) +/-0.5 mm per EN 10219-2 or ASTM A500
- Wall thickness: 4.0 mm nominal, >=3.6 mm minimum (10% under-tolerance per EN 10219)
- Inside diameter: 52.3 mm nominal (derived)
- Material: S235JR (or equivalent) seamless or ERW tube; mill certificate required; yield >=235 MPa
- Length (cut to length): 3,000 mm +/-5 mm (between base plate and top plate weld lines)
- Straightness: <=2 mm per meter (<=6 mm over full length)
- Surface prep before HDG: Sa 2.5 blast per ISO 8501-1
- HDG coating: >=85 um average, >=70 um local minimum per ASTM A123
- Note: "Batch galvanize complete mast assembly (tube + base plate + top plate + gussets) as single unit"

**Base plate:**
- Dimensions: 150 x 150 x 8 mm S235 plate
- Tolerance: +/-1 mm on length/width; +/-0.5 mm on thickness
- Edges: laser- or plasma-cut, deburred
- Bolt holes: 4x 14 mm clearance for M12 bolts on 120 mm bolt circle
- Hole position tolerance: +/-0.5 mm
- Tube-to-base plate weld: 6 mm fillet weld, continuous all-around, E43xx electrode
- Weld leg tolerance: 6 +/-1 mm
- Perpendicularity (tube to base plate): <=0.5 deg (check with angle square after welding)

**Top plate (enlarged per D9 -- 200 x 200 x 8 mm from original A7 specification of 120 x 120 x 8 mm):**
- Dimensions: 200 x 200 x 8 mm S235 plate
- Tolerance: +/-1 mm on length/width; +/-0.5 mm on thickness
- M10 tapped holes: 4x M10 tapped through holes on 160 x 160 mm square pattern
- Tapped hole position tolerance: +/-0.2 mm (Tier T2)
- Note: "Tap after galvanizing using stainless steel taps; or weld SS316 Helicoil-style threaded inserts before HDG"
- Dowel pin holes: 2x 8 mm H7 (+0.000/+0.015 mm) reamed holes on diagonal, 160 mm apart
- Dowel position tolerance: +/-0.05 mm (Tier T1)
- Note: "Ream after galvanizing; these datum holes define reflector alignment"
- Tube-to-top plate weld: 6 mm fillet weld, continuous all-around
- Weld leg: 6 +/-1 mm
- Perpendicularity (plate to tube): <=0.3 deg (CRITICAL for reflector verticality)
- Top surface flatness: <=0.1 mm across 200 mm
- Note: "Machine-skim top face after galvanizing if required; re-apply zinc-rich primer (Zinc Clad IV) on machined area"

**Locking pin hole:**
- Diameter: 12 mm through mast tube wall (both sides), at 30 mm above base plate top surface
- Alignment: both holes coaxial, centered on tube diameter
- Note: "Drill with mast assembled in matching deck socket -- holes must align with socket pin holes"

**Base gussets (per D8 Section 2.8):**
- Quantity: 4 per mast, at 90 deg apart around tube
- Angular spacing tolerance: +/-5 deg
- Gusset plate: 6 mm thick S235, right-triangle: 80 mm height x 40 mm base (+/-1 mm both dims)
- Plasma- or laser-cut
- Gusset-to-tube weld: 6 mm fillet weld, both sides of gusset, continuous
- Gusset-to-base plate weld: 6 mm fillet weld, full base edge, continuous
- Note: "Dress weld toe smooth to reduce fatigue notch"
- Effect: increases effective W at base by ~35% (W_eff ~ 12,473 mm3), reduces utilization from 104% to 77% at LC4

### 5.2 GD&T Notes for Mast Assembly

The following GD&T callouts shall appear on TRI-H-M3-001:

| Feature | GD&T Symbol | Tolerance | Datum | Notes |
|---------|-------------|-----------|-------|-------|
| Tube straightness | Straightness | 1 mm per 1,000 mm length | -- | Full length: <=6 mm total |
| Base plate perpendicularity to tube | Perpendicularity | 0.5 deg | Datum A (tube axis) | Check with angle square |
| Top plate perpendicularity to tube | Perpendicularity | 0.3 deg | Datum A (tube axis) | Critical for reflector orientation |
| Top plate flatness | Flatness | 0.1 mm | -- | Over 200 x 200 mm area |
| Dowel hole true position | True position | 0.05 mm dia | Datum B (top plate center) | Both holes, Tier T1 |
| M10 tapped hole true position | True position | 0.2 mm dia | Datum B (top plate center) | 4 holes, Tier T2 |
| Locking pin hole position | True position | 0.5 mm | Datum A (tube axis) | Both sides aligned |

**Mast assembly mass:** 22.0 kg nominal per unit (tube 16.6, base plate 1.4, top plate 2.5, 4x gussets 0.6, locking pin + lanyard 0.2, welds + HDG 0.7)

---

## 6. M4: Reflector Assembly Drawings

### 6.1 TRI-H-M4-001: Reflector Assembly (x8 Identical)

**Configuration:**
- 3 CNC face plates mounted to 1 AM structural frame
- 12x M6 x 20 A4-80 (SS316) socket head cap screws (4 per face)
- 6x 5 mm m6 x 12 mm SS316 dowel pins (2 per face)
- Nylock nut or Loctite 243 on all M6 fasteners
- Safety wire: MS20995-C32 (0.032" dia SS) through bolt heads in pairs, 6 wire loops per reflector

**Orthogonality specification (CRITICAL):**
- All 3 face-pair angles: 90.00 +/-0.10 deg (assembled)
- Verification: CMM measurement of all 3 face-pair angles per reflector
- Reject: any pair exceeding +/-0.10 deg

**Fastener torque:**
- M6 bolts: 8 +/-1 N-m
- Anti-seize: Tef-Gel on all fasteners

**Assembly environment note:**
- "Assemble in clean, covered workspace; no sand/grit on mating surfaces. Contamination between face plates and frame bosses degrades flatness and orthogonality."

**Galvanic isolation note:**
- "NOT required between face plates and frame (both aluminum alloys; potential difference ~50-100 mV; anodize on both provides isolation). Apply Tef-Gel anti-seize on all fasteners."

**Assembled mass:** 15.0 kg nominal (frame 8.5 + 3 faces at 5.18 each = 15.54 + fasteners 0.9). Target: <=17 kg maximum.

### 6.2 TRI-H-M4-002: CNC Face Plate Detail (x24 Identical)

**Material:**
- 6061-T6 aluminum per ASTM B209
- Mill certificate required (alloy composition, temper, mechanical properties)
- Temper verified by hardness test: Brinell 95 HB typical

**Plate dimensions:**
- Width: 800 mm +/-0.5 mm (T2), CNC-trimmed from oversized stock
- Height: 800 mm +/-0.5 mm (T2)
- Thickness: 3.00 mm +/-0.05 mm (T2)
- Note: "Verify thickness with micrometer at 5 points per plate (4 corners + center)"

**Flatness (reflective face):**
- <0.1 mm over full 800 x 800 mm face (T2)
- Measurement: CMM or granite surface plate with dial indicator
- Note: "CRITICAL for RCS performance. CNC fly-cut on vacuum fixture; stress-relieve if needed."

**Surface roughness (reflective face):**
- Ra <=6.3 um
- Measurement: profilometer, 3 readings per plate
- Note: "Fly-cut finish with sharp diamond or carbide insert; finer than original Ra 10 um specification -- achievable per D9 Section 5.1"

**Surface roughness (back face):**
- Ra <=12.5 um (standard milled finish, non-critical)

**Edge condition:**
- 0.5 mm x 45 deg chamfer on all edges (+/-0.2 mm)
- Note: "Deburr all edges; no sharp edges for handling safety"

**Mounting holes:**
- 4x 7 mm clearance holes for M6 bolts
- 2x 5 mm H7 (+0.000/+0.012 mm) reamed dowel holes
- All hole positions: +/-0.1 mm from datum edge (T2)
- Pattern: per reflector frame drawing; bolt holes at 4 corners, dowel holes on one edge (alignment datum)
- Note: "Faces A, B, C mount to orthogonal frame surfaces; hole patterns differ by face position. Match-drill to AM frame or per coordinated CNC program."

**Surface treatment:**
- Type II anodize (sulfuric acid) per MIL-A-8625F, Class 1 (clear/natural)
- Thickness: >=10 um, <=25 um
- Note: "Clear anodize preserves reflectivity; do NOT dye. Type II clear anodize is transparent to X-band radar (9.4 GHz)."

**Mass per plate:** 5.18 kg nominal (2,700 kg/m3 x 0.800 x 0.800 x 0.003), +/-0.3 kg

### 6.3 TRI-H-M4-003: AM Frame Detail (x8 Identical)

**Material:**
- AlSi10Mg per ASTM F3318
- Process: Laser Powder Bed Fusion (LPBF)
- Powder certification + build coupon tensile test required per build plate

**Post-processing:**
- T5 heat treatment: stress relief + artificial aging (300 deg C / 2h typical for AlSi10Mg T5)
- CNC post-machine: all datum surfaces, mounting bosses, bolt holes, dowel holes machined after printing and heat treatment
- Note: "AM bureau performs post-machining per CNC program supplied with this drawing"

**Orthogonality (MASTER TOLERANCE):**
- All 3 face-mounting surfaces at 90.00 deg to each other
- Tolerance: +/-0.05 deg per face pair (Tier T1)
- Verification: CMM on all 8 frames
- Reject: any pair exceeding +/-0.08 deg on raw frame before assembly

**Mounting bosses (face plate interface):**
- 3 sets of mounting surfaces, each with:
  - 4x M6 tapped holes (Helicoil M6 x 1.5D inserts in AlSi10Mg -- direct tapping unreliable for cyclic loads)
  - 2x 5 mm H7 (+0.000/+0.012 mm) reamed dowel holes
- Tapped hole position tolerance: +/-0.2 mm (T2)
- Dowel hole position tolerance: +/-0.05 mm (T1)
- Mounting boss surface flatness: <=0.05 mm per surface (CMM verified, T1)
- Note: "Post-machined reference surfaces for face plate seating"

**Base flange (mast interface):**
- Integral flange: 200 x 200 x 6 mm at bottom of frame
- Flatness: <=0.1 mm (T2)
- Alignment dowel holes: 2x 8 mm H7 (+0.000/+0.015 mm), on diagonal, 160 mm apart
- Dowel position tolerance: +/-0.05 mm (T1)
- Note: "Must match mast top plate dowel holes within 0.05 mm for repeatable alignment"
- M10 bolt clearance holes: 4x 11 mm on 160 x 160 mm square pattern
- Bolt hole position tolerance: +/-0.2 mm (T2)

**Surface roughness:**
- As-printed (non-critical surfaces): Ra 8-15 um acceptable
- Machined datums: Ra <=3.2 um (T2)

**Surface treatment:**
- Type III hard anodize per MIL-A-8625F, Class 1
- Thickness: >=25 um
- Note: "Hard coat for corrosion + wear resistance; dark grey/black appearance acceptable. All surfaces including machined datums anodized."

**Minimum wall thickness (lattice elements):** >=2.0 mm per LPBF design rules (walls <2 mm risk incomplete fusion)

**Frame overall envelope:** approximately 800 x 800 x 800 mm trihedral, +/-2 mm (T3)

**Mass per frame:** 8.5 kg nominal (lattice-optimized), +/-1.0 kg

**Mechanical properties (minimum, per build coupon):**
- sigma_y >=230 MPa (XY direction), >=210 MPa (Z direction)
- sigma_UTS >=350 MPa
- Elongation >=5%
- Note: "Test 1 coupon per build plate (8 frames may span 2-4 build plates)"

### 6.4 GD&T Notes for Reflector Components

**Face plate GD&T (TRI-H-M4-002):**

| Feature | GD&T Symbol | Tolerance | Datum | Notes |
|---------|-------------|-----------|-------|-------|
| Reflective face flatness | Flatness | 0.1 mm | -- | Over full 800 x 800 mm |
| Thickness | Size | 3.00 +/-0.05 mm | -- | 5-point measurement |
| Edge straightness | Profile of a line | 0.5 mm | -- | All 4 edges |
| Dowel hole true position | True position | 0.1 mm dia | Datum A (plate edge) | Both holes |
| M6 clearance hole position | True position | 0.2 mm dia | Datum A (plate edge) | All 4 holes |

**AM frame GD&T (TRI-H-M4-003):**

| Feature | GD&T Symbol | Tolerance | Datum | Notes |
|---------|-------------|-----------|-------|-------|
| Face A mounting surface flatness | Flatness | 0.05 mm | -- | Post-machined surface |
| Face B mounting surface perpendicularity to Face A | Perpendicularity | 0.05 deg | Datum A (Face A) | CMM verified |
| Face C mounting surface perpendicularity to Face A | Perpendicularity | 0.05 deg | Datum A (Face A) | CMM verified |
| Face B to Face C angle | Angularity | 0.05 deg | Datum A | Derived; all 3 pairs controlled |
| Base flange flatness | Flatness | 0.1 mm | -- | Mast interface surface |
| Base flange dowel position | True position | 0.05 mm dia | Datum B (base flange center) | Both holes, Tier T1 |
| M6 Helicoil position (all 12) | True position | 0.2 mm dia | Datum A | Per face |
| 5 mm dowel position (all 6) | True position | 0.05 mm dia | Datum A | Per face, Tier T1 |

---

## 7. M5-M8: Interface and Kit Drawings

### 7.1 TRI-H-M5-001: Mast-Reflector Pre-Assembly (IF-04)

**Fasteners:**
- 4x M10 x 25 A4-80 (SS316) hex bolts per unit
- Through reflector base flange clearance holes (11 mm) into mast top plate tapped holes (M10)
- Backup: M10 A4-80 Nylock prevailing-torque nuts (double-nutted for redundancy)
- Torque: 15 +/-2 N-m
- Note: "Low torque to avoid crushing anodize; Nylock provides vibration retention"

**Dowel pins:**
- 2x 8 mm m6 x 20 mm SS316 cylindrical dowel pins per unit
- Press fit into mast top plate H7 holes; slide fit into reflector base flange H7 holes
- Note: "Seat dowel pins first using soft mallet before inserting bolts"

**Galvanic isolation (REQUIRED -- HDG steel to anodized aluminum):**
- Nylon isolation bushings: 11 mm ID x 16 mm OD x 8 mm long in all 4 bolt holes
- Isolation washers: HDPE flat washers 20 mm OD x 11 mm ID x 2 mm thick under bolt heads and Nylock nuts
- Moisture barrier: Sikaflex 291 marine sealant, thin film on mating face
- Note: "Prevents HDG steel-to-anodized aluminum galvanic contact in salt spray environment"

**Safety wire:**
- MS20995-C32 (0.032" dia SS) through all 4 bolt heads in 2 pairs
- Note: "Backup to Nylock; prevents vibration loosening over 40,000 wave cycles"

### 7.2 TRI-H-M6-001: GPS Beacon Installation Drawing

**Beacon enclosure:**
- IP68 rated, polycarbonate or ABS-PC blend
- Dimensions: <=250 x 150 x 100 mm
- GNSS patch antenna facing zenith (upward) +/-5 deg

**Mounting clamp:**
- SS316 U-bolt bracket: 2x M8 x 60 mm ID U-bolts
- Saddle plate: 80 x 40 x 5 mm SS316
- Fits 60.3 mm mast OD
- U-bolt torque: 15 +/-2 N-m
- Enclosure-to-bracket: 4x M6 x 16 SS316 bolts, torque 5 +/-1 N-m

**Mounting height:** >=4,000 mm above deck level (>=4,500 mm AWL)
- Note: "Mount on designated GPS mast; use 500 mm extension tube (threaded coupler) if needed for height"

**Cable routing:**
- 5 m shielded coax, UV-resistant jacket
- Cable-tied to mast exterior at 300 mm intervals
- Drip loop at deck grommet

### 7.3 TRI-H-M7-001: Mooring Kit Assembly (3 Depth Variants)

**Kit A (15 m depth -- all-chain catenary):**
- 19 mm G30 HDG chain: 90 m (+/-1 m), 711 kg
- 75 kg Danforth anchor (HDG cast steel)
- 1x jaw-jaw swivel (SWL >=5,000 kgf, HDG)
- 4x Crosby G-2130 (or equivalent) 3/4" bolt-type anchor shackles (SWL 4,750 kgf each)
- Mousing wire: 1.6 mm SS on all shackle pins

**Kit B (30 m depth -- hybrid chain + rode):**
- 19 mm G30 HDG chain: 20 m (+/-1 m), 158 kg
- 24 mm polyester double-braid rode: 35 m (+/-0.5 m), UV-stabilized
- Spliced eyes with SS316 thimble at each end (rated >=6,000 kgf)
- 75 kg Danforth anchor
- 1x swivel, 4x shackles (same as Kit A)

**Kit C (50 m depth -- hybrid chain + rode):**
- 19 mm G30 HDG chain: 20 m (+/-1 m), 158 kg
- 24 mm polyester double-braid rode: 60 m (+/-0.5 m)
- Spliced eyes with SS316 thimble at each end
- 75 kg Danforth anchor
- 1x swivel, 4x shackles (same as Kit A)

**Chain specification:**
- Grade: G30 proof coil per ASTM A413 (or NACM equivalent)
- Size: 19 mm link diameter
- SWL: 5,800 kgf (56.9 kN)
- Breaking load: 17,400 kgf (170.7 kN)
- Coating: HDG >=85 um per ASTM A123
- Weight in air: 7.9 kg/m; weight submerged: 6.9 kg/m

### 7.4 TRI-H-M8-001: Tow Kit Assembly

**Tow bridle:**
- Material: Dyneema SK75 (UHMWPE), 16 mm, 12-strand construction
- SWL: >=8,000 kgf (78.5 kN); breaking load >=24,000 kgf
- Configuration: 2-point bridle, 60 deg included angle between legs
- Leg length: 15 m each (+/-0.5 m)
- Termination (bridle legs): soft eye with SS316 thimble (rated >=6,000 kgf), 72x core tuck minimum splice
- Chafe protection: Dyneema chafe sleeve, 600 mm length, at each padeye contact point

**Trailing drogue:**
- Type: conical sea drogue, 600 mm mouth diameter, 900 mm length
- Material: UV-stabilized nylon canvas, 600D minimum, reinforced rim with SS ring
- Bridle: 4-point to single tow point, 8 mm polyester, 2 m legs
- Attachment: shackled to stern tow padeye or dedicated drogue ring

---

## 8. System Assembly Drawing

### 8.1 TRI-H-SYS-001: System General Arrangement

**Views required:**
1. Plan view (top-down) -- show all 8 mast positions, pad eye, tow padeyes, scuppers, hull outline
2. Side view (elevation section through center) -- show hull depth, waterline, mast heights, reflector positions, GPS beacon, mooring line
3. Section A-A (through ring pontoon cross-section) -- show hull wall, foam fill, frame beam, deck socket

**Key dimensions to display on drawing:**

| Dimension | Value | Tolerance |
|-----------|-------|-----------|
| Platform outer diameter | 8,000 mm | +/-100 mm |
| Hull depth | 500 mm | +/-50 mm |
| Design draft (at 990 kg displacement) | ~19 mm | Calculated |
| Freeboard | ~481 mm | Derived |
| Deck socket circle radius | 3,200 mm from center | +/-5 mm |
| Mast height above deck | 3,000 mm | +/-5 mm |
| Reflector center height AWL | ~4,000 mm | Derived |
| GPS beacon height AWL | >=4,500 mm | Minimum |
| Total height above keel (max) | ~5,500 mm | Derived |
| Mast-to-mast arc distance (at R=3,200 mm) | 2,513 mm | Derived |
| Reflector edge-to-edge clearance | 1,713 mm | Derived |

**Mass budget table (on drawing):**

| # | Component | Qty | Mass Each (kg) | Total (kg) |
|---|-----------|-----|----------------|------------|
| 1 | Hull shell (HDPE) | 1 | 200 | 200 |
| 2 | PU foam fill | 1 | 121 | 121 |
| 3 | Structural frame assembly | 1 | 155 | 155 |
| 4 | Mast assemblies (tube + plates + gussets + pin) | 8 | 22.0 | 176 |
| 5 | Reflector assemblies (frame + 3 faces + fasteners) | 8 | 15.0 | 120 |
| 6 | GPS beacon assembly | 1 | 5.0 | 5 |
| 7 | On-hull mooring hardware | 1 | 15 | 15 |
| 8 | Hull section joint hardware (IF-07) | 1 | 12 | 12 |
| 9 | Frame-to-hull fasteners (IF-01) | 84 | 0.08 | 7 |
| 10 | Deck equipment, misc | -- | -- | 20 |
| 11 | Zinc anodes | 2 | 0.5 | 1 |
| | **ON-PLATFORM SUBTOTAL** | | | **832** |
| 12 | On-hull mooring chain segment (3 m) | 1 | 23.7 | 24 |
| 13 | Tolerance + unaccounted (10% margin) | | | 83 |
| | **TOTAL DISPLACEMENT** | | | **939** |
| | **Maximum allowable** | | | **1,100** |

**Module identification callouts:**
- Each module (M1-M8) labeled with drawing cross-reference
- Each interface (IF-01 to IF-07) labeled with circle callout and drawing cross-reference

---

## 9. Weld Schedule

### 9.1 Complete Weld Table

| Weld ID | Location | Joint Type | Weld Type | Size (mm) | Process | Electrode / Wire | Preheat | Interpass Max | Inspection | Accept Standard | Drawing Ref |
|---------|----------|-----------|-----------|-----------|---------|-----------------|---------|---------------|------------|-----------------|-------------|
| W-01 | Perimeter ring butt joints | Butt | Full penetration | Per section | MIG/MAG | ER70S-6 (0.9 mm) | None (t <25 mm) | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M2-006 |
| W-02 | Cross member to perimeter ring | Fillet (tee) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M2-001 |
| W-03 | Cross member to center hub | Fillet (tee) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M2-005 |
| W-04 | Deck socket sleeve to base plate | Fillet (circumferential) | Fillet | 6 mm leg (throat >=5 mm) | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M2-002 |
| W-05 | Deck socket base plate to frame | Fillet | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M2-002 |
| W-06 | **Pad eye plate to backing plate** | Groove (both sides) | **Full penetration** | Per WPS | **SMAW** | **E7018** | **>=50 deg C** | 250 deg C | **Visual + UT 100%** | **AWS D1.1 Sec 6** | **TRI-H-M2-003** |
| W-07 | Pad eye ring to eye plate | Fillet (full circumference) | Full penetration | Per ring section | MIG/MAG or SMAW | ER70S-6 / E7018 | >=50 deg C | 250 deg C | Visual + UT 100% | AWS D1.1 Sec 6 | TRI-H-M2-003 |
| W-08 | Tow padeye ring to base plate | Fillet (circumferential) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M2-004 |
| W-09 | Mast tube to base plate | Fillet (circumferential) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M3-001 |
| W-10 | Mast tube to top plate | Fillet (circumferential) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M3-001 |
| W-11 | Mast gusset to tube (both sides) | Fillet (lap) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M3-004 |
| W-12 | Mast gusset to base plate | Fillet (lap) | Fillet | 6 mm leg | MIG/MAG | ER70S-6 | None | 250 deg C | Visual 100% | AWS D1.1 Sec 6 | TRI-H-M3-004 |

### 9.2 Weld Notes

1. **All welders** must hold current qualification per AWS D1.1 or TCVN equivalent. Qualification records on file.
2. **Welder qualification minimum:** 3G (vertical up) for all fillet welds; groove weld qualification for W-06 and W-07.
3. **WPS and PQR** required for W-06 (pad eye full-penetration groove weld) -- CRITICAL SAFETY WELD.
4. **E7018 electrode** for W-06 and W-07: low-hydrogen, bake at 260 deg C / 2h before use if exposed to moisture.
5. **All fillet welds:** 6 mm leg (+/-1 mm), continuous all-around unless noted. No undercut >0.5 mm. No porosity >1.5 mm dia.
6. **Weld sequence:** complete all welding on frame assembly before HDG. Complete all welding on mast assembly before HDG.
7. **Post-weld treatment:** deburr weld spatter, grind smooth any weld toe notches at fatigue-critical locations (W-11, W-12 mast gussets).
8. **HDPE hull welds** (if hot-plate welded hull): per DVS 2207-1 for HDPE butt welds; extrusion welder for HDPE seams. Separate WPS for HDPE not covered in this steel weld schedule.

---

## 10. Surface Treatment Schedule

### 10.1 Complete Surface Treatment Table

| ID | Component | Material | Treatment | Specification | Min Thickness | Max Thickness | Color | Vendor Category | Notes |
|----|-----------|----------|-----------|---------------|---------------|---------------|-------|-----------------|-------|
| S-01 | Hull shell | HDPE PE100 | None | N/A | N/A | N/A | Black (carbon-black) | N/A | Inherent UV/salt resistance |
| S-02 | PU foam fill | Rigid PU | None | N/A | N/A | N/A | White/cream | N/A | Encapsulated in hull |
| S-03 | Frame perimeter ring | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | Sa 2.5 blast prep |
| S-04 | Frame cross members | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | Sa 2.5 blast prep |
| S-05 | Center hub plate | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | -- |
| S-06 | Pad eye assembly | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | UT weld inspection BEFORE HDG |
| S-07 | Deck sockets (x8) | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | Bore reamed smooth after HDG |
| S-08 | Tow padeyes (x2) | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | -- |
| S-09 | Mast tubes + plates + gussets (x8) | S235JR | Hot-dip galvanize | ASTM A123 / ISO 1461 | 85 um avg / 70 um local | -- | Silver-grey (zinc) | Local HDG plant | Full assembly galvanized as unit |
| S-10 | Mast top plates (x8) | S235JR | HDG + machine-skim top face | ASTM A123 + Zinc Clad IV primer | 85 um (sides) | -- | Silver-grey; top face bright + primer | Local HDG + machine shop | Top face flatness <=0.1 mm; re-apply zinc-rich primer on machined area |
| S-11 | Reflector face plates (x24) | 6061-T6 | Type II sulfuric anodize, Class 1 (clear) | MIL-A-8625F Type II | 10 um | 25 um | Clear/natural aluminum | Local anodizer (Saigon Anodizing) | Do NOT dye; preserves radar reflectivity |
| S-12 | Reflector AM frames (x8) | AlSi10Mg | Type III hard anodize, Class 1 | MIL-A-8625F Type III | 25 um | -- | Dark grey/black (natural) | ASEAN AM bureau (bundled) or local | Hard coat for corrosion + wear; all surfaces including machined datums |
| S-13 | Mooring chain | G30 steel | Hot-dip galvanize | ASTM A123 | 85 um | -- | Silver-grey (zinc) | Factory-applied by chain manufacturer | -- |
| S-14 | Anchor (Danforth) | Cast steel | Hot-dip galvanize | ASTM A123 | 85 um | -- | Silver-grey (zinc) | Factory-applied | -- |
| S-15 | Swivel | Alloy steel | Hot-dip galvanize | ASTM A123 | 85 um | -- | Silver-grey (zinc) | Factory-applied | -- |
| S-16 | Shackles (mooring) | Forged alloy steel | Hot-dip galvanize | ASTM A123 | 85 um | -- | Silver-grey (zinc) | Factory-applied (Crosby or equiv.) | -- |
| S-17 | GPS enclosure | ABS-PC blend | UV-stabilized compound | IP68 per IEC 60529 | N/A | N/A | Black or olive drab | COTS procurement | -- |
| S-18 | GPS bracket + U-bolts | SS316 | Passivation | ASTM A967 | N/A | N/A | Natural SS (silver) | Local fabrication | -- |
| S-19 | Deck surface (hull) | HDPE | Non-skid textured paint | Marine-grade deck paint | N/A | N/A | Grey | Local marine supply | Textured, self-draining |

### 10.2 Coating Measurement Requirements

| Coating Type | Measurement Method | Equipment | Frequency | Accept Criteria |
|--------------|-------------------|-----------|-----------|-----------------|
| HDG on steel | Magnetic thickness gauge | Elcometer 456 or equivalent | 3 readings per part, all parts | >=85 um avg, >=70 um local min |
| Type II anodize on Al | Eddy current gauge | Fischer Dualscope or equivalent | 3 readings per plate; 10% of batch + first article | >=10 um, <=25 um |
| Type III hard anodize on Al | Eddy current gauge | Fischer Dualscope or equivalent | 3 readings per frame; 100% of frames | >=25 um |

---

## 11. Fastener Schedule

### 11.1 Complete Fastener Table (Per Target Unit)

| F-ID | Location / Interface | Size | Grade / Material | Qty | Torque (N-m) | Locking Method | Corrosion Protection | Washer | Notes |
|------|---------------------|------|-----------------|-----|-------------|----------------|---------------------|--------|-------|
| F-01 | Frame-to-hull perimeter (IF-01) | M12 x 40 | SS316 A4-70 | 84 | 40 +/-3 | Nylock nut | Inherent (SS316) | 50x50x5 SS fender washer on HDPE side + SS flat washer on frame side | BOM 1.2.10 |
| F-02 | Pad eye backing plate to frame (IF-02) | M16 x 60 | Gr 8.8 HDG | 8 | 190 +/-10 | Nylock nut | HDG (>=85 um) | Hardened washer under head and nut | BOM 1.2.07 |
| F-03 | Deck socket base plate to frame (IF-03) | M12 x 35 | Gr 8.8 HDG | 32 | 80 +/-5 | Nylock nut | HDG (>=85 um) | Hardened washer | 4 per socket x 8 |
| F-04 | Tow padeye to hull/frame (IF-06) | M12 x 50 | Gr 8.8 HDG | 8 | 80 +/-5 | Nylock nut | HDG (>=85 um) | 50x50x5 SS fender washer on HDPE side | 4 per padeye x 2 |
| F-05 | Reflector face to AM frame (M4 internal) | M6 x 20 | A4-80 (SS316) SHCS | 96 | 8 +/-1 | Nylock nut + safety wire MS20995-C32 | Inherent (SS316) | -- | 12 per reflector x 8; Loctite 243 alternative |
| F-06 | Reflector face dowel pins (M4 internal) | 5 mm m6 x 12 | SS316 | 48 | N/A (press fit) | Press fit frame H7 / slide fit face H7 | Inherent (SS316) | -- | 6 per reflector x 8 |
| F-07 | Reflector to mast top (IF-04) | M10 x 25 | A4-80 (SS316) | 32 | 15 +/-2 | Nylock nut + safety wire MS20995-C32 | Inherent (SS316) | Nylon isolation bushing + HDPE isolation washers | 4 per mast x 8 |
| F-08 | Reflector to mast dowel pins (IF-04) | 8 mm m6 x 20 | SS316 | 16 | N/A (press fit) | Press into mast top plate H7 / slide into reflector flange H7 | Inherent (SS316) | -- | 2 per mast x 8 |
| F-09 | Mast locking pin (IF-03) | 10 mm spring ball-lock pin | SS316 | 8 | N/A (hand insert) | Ball-lock detent + R-clip + 300 mm SS wire lanyard | Inherent (SS316) | -- | 1 per mast x 8 |
| F-10 | GPS beacon U-bolts (IF-05) | M8 x 60 mm ID U-bolt | SS316 | 2 | 15 +/-2 | Nylock nut | Inherent (SS316) | Saddle plate 80x40x5 SS316 | BOM 1.6.09 |
| F-11 | GPS beacon enclosure to bracket (IF-05) | M6 x 16 | SS316 | 4 | 5 +/-1 | -- | Inherent (SS316) | -- | BOM 1.6.11 |
| F-12 | Hull section joint (IF-07) | M10 x 40 | SS316 A4-70 | 24 | 25 +/-3 | Nylock nut | Inherent (SS316) | Flat washer + fender washer on outer HDPE face | Star pattern tightening |
| F-13 | Hull section alignment dowels (IF-07) | 12 mm x 30 nylon | Nylon 6/6 | 3 | N/A (push fit) | Friction | N/A (polymer) | -- | Alignment only; no structural load |
| F-14 | Zinc anode to pad eye | M10 x 30 | SS316 | 1 | 15 +/-2 | -- | Inherent (SS316) | -- | BOM 1.2.18 |
| F-15 | Hull backing channel bolts (IF-07) | M10 x 50 | Gr 8.8 HDG | 12 | 40 +/-3 | Nylock nut | HDG (>=85 um) | -- | 6 per side, through HDPE + steel channel |
| | **TOTAL FASTENERS (approx.)** | | | **~344** | | | | | Excludes mooring/tow shackles |

### 11.2 Torque Summary (Quick Reference)

| Fastener | Torque (N-m) | Application |
|----------|-------------|-------------|
| M16 Gr 8.8 HDG | 190 +/-10 | Pad eye to frame (F-02) |
| M12 Gr 8.8 HDG | 80 +/-5 | Deck socket to frame (F-03), tow padeye (F-04) |
| M12 SS316 | 40 +/-3 | Frame to hull (F-01), backing channel (F-15) |
| M10 SS316 | 25 +/-3 | Hull section joint (F-12) |
| M10 SS316 | 15 +/-2 | Reflector to mast (F-07) |
| M8 SS316 | 15 +/-2 | GPS U-bolt (F-10) |
| M6 SS316 | 8 +/-1 | Reflector face to frame (F-05) |
| M6 SS316 | 5 +/-1 | GPS enclosure to bracket (F-11) |

---

## 12. Notes and Standards Block

### 12.1 Standard Notes (To Appear on ALL Drawings)

```
NOTES UNLESS OTHERWISE SPECIFIED:
1. DIMENSIONS IN MILLIMETERS.
2. ANGLES IN DEGREES.
3. GENERAL TOLERANCES PER ISO 2768-mK:
   LINEAR: +/-0.1 (0.5-6), +/-0.2 (6-30), +/-0.5 (30-120),
           +/-0.8 (120-400), +/-1.2 (400-1000), +/-2.0 (1000-2000),
           +/-3.0 (2000-4000), +/-4.0 (>4000)
   ANGULAR: +/-1 deg (<10 mm), +/-0'30" (10-50), +/-0'20" (50-120),
            +/-0'10" (120-400), +/-0'5" (>400)
4. REMOVE ALL BURRS AND SHARP EDGES. BREAK EDGES 0.5 mm x 45 deg UNLESS NOTED.
5. SURFACE FINISH: Ra 12.5 um UNLESS OTHERWISE SPECIFIED.
6. ALL STEEL WELDS PER AWS D1.1. WELDER QUALIFIED TO 3G MINIMUM.
   ELECTRODE: ER70S-6 (MIG/MAG) OR E7018 (SMAW) UNLESS NOTED.
7. ALL STEEL PARTS HOT-DIP GALVANIZED PER ASTM A123, >=85 um AVG
   UNLESS OTHERWISE SPECIFIED.
8. ALL SS316 FASTENERS: APPLY TEF-GEL ANTI-SEIZE ON THREADS BEFORE ASSEMBLY.
9. GALVANIC ISOLATION REQUIRED AT ALL STEEL-TO-ALUMINUM INTERFACES.
   SEE INTERFACE DRAWINGS FOR ISOLATION DETAIL.
10. MATERIAL CERTIFICATES REQUIRED FOR: S235 STEEL, 6061-T6 ALUMINUM,
    AlSi10Mg AM POWDER, G30 CHAIN, ANCHOR. FILE WITH QC DOCUMENTATION.
```

### 12.2 Referenced Standards (Complete List)

| Standard | Title | Application |
|----------|-------|-------------|
| ISO 128-20 / -24 | Technical drawings -- General principles of presentation | Drawing conventions |
| ISO 1101:2017 | GD&T -- Geometrical tolerancing | Tolerance callouts |
| ISO 2768-mK | General tolerances -- linear and angular dimensions | Default tolerance class |
| ISO 5457 | Drawing sheet sizes | A1, A3 sheet formats |
| ISO 7200 | Title blocks | Drawing title block format |
| ISO 8015 | Principle of independency | Tolerance interpretation |
| ISO 1302 | Surface texture indication | Surface finish symbols |
| ISO 2553 | Welding symbols | Weld callouts on drawings |
| ISO 8501-1 | Surface preparation grades | Sa 2.5 blast specification |
| AWS D1.1 | Structural Welding Code -- Steel | All structural steel welds |
| AWS A5.1 | Carbon steel electrodes for SMAW | E7018 electrode specification |
| DVS 2207-1 | Welding of thermoplastics -- heated tool | HDPE hull welds (if applicable) |
| ASTM A123 / ISO 1461 | Hot-dip galvanized coatings on iron and steel | HDG specification |
| MIL-A-8625F | Anodic coatings for aluminum and aluminum alloys | Type II (face plates), Type III (AM frames) |
| ASTM F3318 | AlSi10Mg via LPBF additive manufacturing | AM frame material standard |
| ASTM F3301 | AM process qualification (PBF-LB/M) | AM frame process control |
| ASTM B209 | Aluminum sheet and plate | 6061-T6 face plate material |
| EN 10025-2 | Hot-rolled structural steel (S235JR) | Frame and mast structural steel |
| EN 10219-2 | Cold-formed welded structural hollow sections | Mast tube specification |
| EN 10056-1 | Equal leg angles | Perimeter ring and cross members |
| ASTM A500 | Cold-formed welded and seamless structural tubing | Mast tube alternative |
| ASTM D3350 | Polyethylene pipe and fittings materials | HDPE hull material |
| ASTM D1621 / D1622 / D2842 | Rigid cellular plastics testing | PU foam specifications |
| ASTM A413 (NACM) | Steel chain standard | G30 proof coil chain |
| EN 818-3 | Short link chain -- grade 30 | Chain proof/breaking load |
| IEC 60529 | IP protection rating | GPS beacon enclosure (IP68) |
| ASTM A967 | Passivation of stainless steel | GPS bracket passivation |
| MIL-STD-810H | Environmental engineering | Environmental qualification basis |
| MIL-STD-882E | System safety | Safety program standard |
| IALA Guideline 1093 | Radar reflector performance measurement | RCS measurement protocol |
| API RP 2SK | Mooring system design (reference) | Mooring force methodology |
| TCVN 6259:2003 | Steel sea-going ship construction (reference) | Vietnamese welding/steel practice |

---

## Cross-References

### Phase 4 Documents (This Phase)
- This document: Manufacturing Drawing Specifications (textual basis for CAD production drawings)

### Phase 3 Source Documents
- [[../03_embodiment/DECS_D9_detail_specification.md]] -- Master engineering specification: all dimensions, tolerances, surface finishes, fastener schedule, inspection criteria
- [[../03_embodiment/PRAD_D8_design_structure.md]] -- Structural analysis: load cases, mast bending (gusset solution), pad eye sizing (14 mm backing plate), mooring chain (19 mm G30), hull stability (GM = 208 m)
- [[../03_embodiment/PRAD_A7_architecture_definition.md]] -- System architecture: 8 modules (M1-M8), 7 interfaces (IF-01 to IF-07), containment tree, ICD, assembly sequences
- [[../03_embodiment/OCP_C14_cost_analysis.md]] -- BOM item numbers (1.1.01 through 1.9.08), unit cost $29,655 at 10 units
- [[../03_embodiment/OCP_P15_production_planning.md]] -- Manufacturing processes, supplier identification, make/buy, QC plan, field deployment
- [[../03_embodiment/DECS_S12_standards_compliance.md]] -- Welding standards (AWS D1.1), material standards (EN 10025-2, ASTM B209, ASTM F3318), surface treatment standards (MIL-A-8625F, ASTM A123), test plan (7 tests, $28K)

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1); GEO-001 to GEO-010, FOR-001 to FOR-011, MAT-001 to MAT-010, SIG-001 to SIG-009
- [[../01_requirements/standards_mapping.md]] -- MIL-STD-810H, MIL-A-8625F, ASTM A123, ASTM F3318, AWS D1.1, ISO 2768-mK

### Phase 2 Source Documents
- [[../02_conceptual/concept_selection.md]] -- Concept A "Baseline Optimized" (VDI 2225: 81.8%)
- [[../02_conceptual/function_structure.md]] -- F1-F7 function decomposition

---

**Document Status:** Draft v1.0 -- Complete manufacturing drawing specification covering all 33 production drawings organized across 8 modules, 7 interfaces, and system-level documents. Key specification highlights:

1. **Drawing numbering system** TRI-H-[module]-[part]-[rev] with ISO 128/1101/2768-mK standards basis.
2. **33 drawings required** for full production release: 5 system, 5 hull (M1), 6 frame (M2), 4 mast (M3), 4 reflector (M4), 4 kit/beacon (M5-M8), 7 interface, 3 installation.
3. **All dimensions traced** to D9 detail specification with 4-tier tolerance philosophy (T1 precision through T4 coarse).
4. **12 welds scheduled** per AWS D1.1 with W-06 (pad eye groove weld) as CRITICAL requiring WPS/PQR, preheat, and UT inspection.
5. **19 surface treatments** specified covering HDG (ASTM A123), Type II anodize (MIL-A-8625F), Type III hard anodize (MIL-A-8625F), and deck coatings.
6. **~344 fasteners per unit** fully specified across 15 categories with size, grade, torque, locking method, and corrosion protection.
7. **Complete GD&T callouts** for all critical features: reflector orthogonality +/-0.05 deg (T1), face plate flatness <0.1 mm, mast perpendicularity <=0.3 deg, dowel pin positions +/-0.05 mm.
8. **30+ standards referenced** covering drawing practice, welding, materials, coatings, AM qualification, and environmental compliance.
