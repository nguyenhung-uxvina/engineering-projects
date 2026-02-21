---
project: VN-TGT-SEA-001
phase: 3
step: "D9 — Detail Specification"
group: DECS
version: 1.0
created: 2026-02-10
status: draft
---

# Step D9: Detail Specification — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Specify all dimensions, tolerances, surface finishes, and assembly details for every component at production-release level. This document is the master engineering specification from which manufacturing drawings, inspection plans, and procurement documents are derived.
**Method:** Pahl & Beitz DECS Step D9 — Detail dimensioning, tolerance assignment, surface specification
**Input:** [[PRAD_D8_design_structure.md]] (structural analysis, design updates), [[PRAD_A7_architecture_definition.md]] (architecture, interfaces, modules M1-M8), [[RISM_M4_material_analysis.md]] (material selections, properties, cost)
**General Tolerance Standard:** ISO 2768-mK (medium tolerance class, coarse angular class) unless otherwise specified on individual dimensions.

---

## 1. Tolerance Philosophy

### 1.1 Guiding Principle

Tight tolerances are assigned ONLY where function demands them. The product is an expendable maritime target — not a precision instrument. Structural and buoyancy functions tolerate wide variation; radar reflector orthogonality does not.

### 1.2 Tolerance Tiers

| Tier | Tolerance Class | Typical Application | Justification |
|------|----------------|---------------------|---------------|
| **T1 — Precision** | <=+/-0.05 mm linear, <=+/-0.05 deg angular | Reflector frame alignment datums, dowel hole positions | Orthogonality requirement SIG-009: +/-0.1 deg assembled; AM frame must achieve +/-0.05 deg to allow tolerance stack-up with face plates |
| **T2 — Close** | +/-0.1 to +/-0.5 mm linear, +/-0.1 deg angular | Face plate flatness (<0.1 mm), mast top plate hole pattern, dowel pin reamed holes (H7) | Reflector RCS performance depends on face flatness and bolt/dowel alignment at IF-04 |
| **T3 — Medium** | +/-1 to +/-5 mm linear, +/-0.5 deg angular | Frame member lengths, deck socket positions, mast length, bolt hole positions | Structural fit-up; ISO 2768-m class adequate |
| **T4 — Coarse** | +/-5 to +/-100 mm linear, +/-2 deg angular | Hull diameter, hull depth, foam fill density, mooring chain length | Buoyancy and dimensional envelope; large tolerances acceptable for HDPE rotomolding |

### 1.3 Vietnamese CNC Capability Assumptions

| Operation | Achievable Tolerance | Machine Type | Notes |
|-----------|---------------------|-------------|-------|
| CNC milling (3-axis) | +/-0.05 mm | Mazak/Haas equivalent | Available at major VN CNC shops (Hanoi, HCMC) |
| CNC turning | +/-0.02 mm | Standard CNC lathe | Widely available |
| Fly-cutting (face plates) | Flatness <0.05 mm over 800 mm | 3-axis with vacuum fixture | Requires verified fixturing; shop capability must be confirmed |
| Reaming (dowel holes) | H7 tolerance (+0.000/+0.015 mm on 8 mm) | Drill press or CNC | Standard reamer tooling |
| Plasma cutting (steel) | +/-1.0 mm | CNC plasma table | Frame members and plates |
| HDPE welding | +/-3 mm | Manual extrusion welder | Hull fabrication |
| Rotomolding (HDPE) | +/-5 mm on major dims; +/-2 mm on wall thickness | Rotomold oven | Hull shell; wall uniformity depends on mold quality |

---

## 2. Hull Specifications (M1)

### 2.1 Hull Shell — HDPE Ring Pontoon

| Parameter | Specification | Tolerance | Tier | Notes |
|-----------|---------------|-----------|------|-------|
| Overall outside diameter | 8,000 mm | +/-100 mm | T4 | Measured across max chord at deck level |
| Hull depth (overall) | 500 mm | +/-50 mm | T4 | Measured at ring cross-section |
| Ring width (pontoon cross-section) | 500 mm nominal | +/-30 mm | T4 | Inner to outer hull wall |
| Wall thickness (HDPE shell) | >=8 mm minimum | +0/-0 (minimum) | T4 | Rotomolded: 8-15 mm typical; no maximum; verify minimum at 8 sampling points |
| Deck surface | Flat, self-draining, non-skid texture | Flatness +/-10 mm | T4 | Molded-in diamond pattern or post-applied non-skid coating |
| Scupper drains | 8x Ø100 mm holes at hull inner edge | Position +/-20 mm | T4 | Equally spaced at 45 deg; drainage to sea |
| Material | HDPE PE100, carbon-black UV-stabilized | Per ASTM D3350 Cell Class 345464C | — | Melt flow index <=0.4 g/10 min; density 940-960 kg/m3 |
| Color | Black (carbon-black stabilized) | — | — | Or olive drab per customer specification |
| Hull mass (shell only, no foam) | 200 +/-30 kg | — | — | Verify on floor scale before foam fill |

### 2.2 Foam Fill

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Material | Closed-cell rigid polyurethane foam | Per ASTM D1622 | Marine grade, pour-in-place, 2-component |
| Density | 32-48 kg/m3 | +/-5 kg/m3 | Verify by sample coupon cut from pour batch |
| Fill factor | >=80% of hull internal volume | Minimum | Leave <=20% void for drainage and inspection access |
| Foam mass | 100-150 kg (target 121 kg at 40 kg/m3) | — | Depends on actual density and fill factor |
| Water absorption | <=3% by volume after 48h immersion | Per ASTM D2842 | Critical for reserve buoyancy; reject if exceeded |
| Compressive strength | >=150 kPa at 10% deformation | Per ASTM D1621 | Resists green water pressure |

### 2.3 Two-Section Hull Joint (IF-07)

If the hull is fabricated as two semicircular halves for transport (TRA-002: max 2.5 m width on standard flatbed):

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Joint line | Diameter plane (centerline), divides hull into 2 equal halves | +/-5 mm from true centerline | Joint runs along full diameter including ring pontoon top/bottom/sides |
| Flange width | 60 mm integral HDPE lip on each half | +/-5 mm | Thermally welded or machined into hull wall |
| Flange thickness | 20 mm | +/-2 mm | Must resist bolt clamping without creep; verify HDPE creep at 40 N-m bolt torque |
| Bolt pattern | 24x M10 SS316 hex bolts at ~520 mm spacing | Spacing +/-10 mm | Along full joint perimeter (~12.6 m total length) |
| Bolt hole diameter | 11 mm clearance | +/-0.5 mm | Standard clearance for M10 |
| Gasket | EPDM rubber strip, 40 mm wide x 5 mm thick, continuous | — | Compressed between flanges; Shore A 60 +/-5 hardness |
| Gasket compression | 3.5-4.0 mm installed (30% compression) | — | Controlled by bolt torque 25 +/-3 N-m |
| Section-to-section alignment | Outer diameter match across joint | +/-3 mm step | Use alignment dowels (3x Ø12 mm nylon pins at 120 deg spacing) |
| Sealant | Sikaflex 291 marine sealant on exterior joint line | Continuous 5 mm bead | Secondary seal; applied after bolt-up |
| Steel backing channel | C100x50x5 HDG steel, full joint length, inside hull | — | Structural bridge across joint; bolted to hull with 6x M10 through-bolts per side |

---

## 3. Frame Specifications (M2)

### 3.1 Frame Material and General Requirements

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Material | S235JR (or Q235B equivalent) | EN 10025-2 |
| Yield strength (min) | 235 MPa | Mill certificate required |
| Surface finish (before HDG) | Sa 2.5 (near-white blast) | ISO 8501-1 |
| Hot-dip galvanize coating | >=85 um average, >=70 um local minimum | ASTM A123 / ISO 1461 |
| All welds | Fillet welds unless noted; E43xx electrode (AWS A5.1) | Continuous all-around unless noted |
| Weld inspection | Visual 100%; UT on pad eye full-penetration weld | AWS D1.1 |
| General tolerance (frame members) | ISO 2768-m | Medium class |

### 3.2 Perimeter Ring Beam

| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Section | L50x50x5 equal angle | Per EN 10056-1 |
| Ring diameter (neutral axis) | 7,200 mm (fits inside hull inner wall) | +/-5 mm |
| Joint type | Butt-welded segments (4x quarter-arcs or 8x octants) | Weld gap <=2 mm |
| Weld | Full-penetration butt weld at ring joints; 6 mm fillet weld at cross-member connections | — |

### 3.3 Radial Cross Members

| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Quantity | 8x radial beams from center hub to perimeter ring | At 45 deg spacing +/-0.5 deg |
| Section | L50x50x5 equal angle | Per EN 10056-1 |
| Length | ~3,600 mm (center hub to ring) | +/-3 mm; fit to actual ring |
| Connection to ring | 6 mm fillet weld, both sides of angle | — |
| Connection to center hub | 6 mm fillet weld to central plate (300x300x10 mm) | — |

### 3.4 Center Hub and Pad Eye Assembly (IF-02)

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Hub plate | 300x300x10 mm S235, center of frame | Position: center +/-5 mm | All 8 radial beams welded to this plate |
| **Pad eye ring** | 25 mm dia round bar, 80 mm ID, formed to ring | Weld to eye plate (full penetration) | Shackle pin passes through 80 mm ID |
| **Eye plate** | 80 mm wide x 20 mm thick S235, tapers to 12 mm at edges | Height: 120 mm above backing plate | Welded edges rounded R>=3 mm for stress concentration reduction |
| **Eye plate weld** | Full-penetration groove weld to backing plate, both sides | UT inspected per AWS D1.1 | CRITICAL weld — load path for all mooring force |
| **Backing plate** | 200x200x14 mm S235 (upgraded from 10 mm per D8 Section 3.1) | Flatness +/-0.5 mm | Through-bolted to hub plate and cross members |
| Bolt pattern (backing plate) | 8x M16 Gr 8.8 HDG on 150x150 mm square pattern | Hole position +/-0.5 mm | 17 mm clearance holes in backing plate, hub plate, cross members |
| Bolt torque (M16 Gr 8.8) | 190 +/-10 N-m | — | Hardened washers under heads and nuts |
| Sacrificial zinc anode | 0.5 kg zinc block, bolted adjacent to pad eye ring | — | M10 bolt through anode and backing plate |
| Proof load requirement | 1.5x SWL = 6,804 kgf applied vertically through pad eye ring | No permanent deformation | Before first deployment; certify and stamp |

### 3.5 Deck Socket Assemblies (IF-03, qty 8)

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Socket sleeve | 116 mm OD x 8 mm wall (100 mm ID after weld) x 150 mm tall | ID: 100 +0/-1 mm after weld cleanup | Seamless or ERW tube, S235 |
| Socket bore finish | Machined or reamed to Ra <=12.5 um | — | Smooth bore for mast insertion |
| Chamfer at socket top | 2 mm x 45 deg lead-in chamfer | — | Eases field insertion of mast base |
| Socket base plate | 160x160x8 mm S235, welded around socket bottom | Flatness +/-1 mm | Bolted to frame radial beam |
| Socket-to-base plate weld | 6 mm fillet weld, continuous all-around (circumferential) | Weld throat >=5 mm | Per D8 Section 3.2: weld stress 21.4 MPa, utilization 16.6% |
| Locking pin hole | Ø12 mm through socket wall AND mast tube, at 100 mm above base plate | Position +/-0.5 mm; holes aligned through both walls | Cross-drilled after assembly trial fit |
| Drain hole | Ø6 mm at socket bottom (lowest point) | — | Prevents water pooling and corrosion |
| Bolt pattern (base plate to frame) | 4x M12 Gr 8.8 HDG on 120 mm dia bolt circle | Hole position +/-0.5 mm | 13 mm clearance holes |
| Bolt torque (M12 Gr 8.8) | 80 +/-5 N-m | — | Hardened washers |
| Position on frame | Radius 3,200 mm from frame center, 8 positions at 45 deg spacing | Radius +/-5 mm; angle +/-0.5 deg | Per A7 Section 5.2 |

### 3.6 Tow Padeye Assemblies (IF-06, qty 2)

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Ring | 20 mm dia round bar, 60 mm ID | Welded to base plate | Accepts 16 mm shackle pin |
| Base plate | 150x150x10 mm S235 | — | Through-bolted to hull + frame perimeter ring |
| Bolt pattern | 4x M12 Gr 8.8 HDG on 100x100 mm square | Hole position +/-1 mm | 13 mm clearance holes |
| Bolt torque | 80 +/-5 N-m | — | With 50x50x5 SS fender washers on HDPE side |
| Position | 2x at R=3,800 mm from center, +/-30 deg from North (bow axis) | +/-20 mm along perimeter | Symmetric port/starboard |
| SWL | >=3,762 kgf per padeye (3:1 on 1,254 kgf per-leg peak tow load) | — | D8 Section: 4x M12 bolt shear 5,343 kgf >> 3,762 kgf |

### 3.7 Frame-to-Hull Connection (IF-01)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Bolt pattern | M12 x 40 SS316 hex bolts at 300 mm spacing around perimeter | ~84 bolts for 8.0 m inner circumference |
| Hole size | 13 mm clearance in both frame flange and HDPE hull | Oversized 1 mm for alignment |
| Washers (HDPE side) | 50x50x5 mm SS316 fender washers | Spread clamping load on soft HDPE |
| Sealant | Sikaflex 291 marine sealant between frame flange and hull | Moisture barrier and bedding compound |
| Torque | 40 +/-3 N-m | Controlled to prevent HDPE creep under sustained load |

---

## 4. Mast Specifications (M3, qty 8 identical)

### 4.1 Mast Tube

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Tube OD | 60.3 mm (DN50 Schedule 40 equivalent) | +/-0.5 mm | Per EN 10219-2 or ASTM A500 |
| Wall thickness | 4.0 mm nominal | >=3.6 mm minimum (10% under-tolerance per EN 10219) | D8 design based on 4.0 mm wall; gusset reinforcement at base compensates |
| Inside diameter | 52.3 mm nominal | — | Derived from OD and wall |
| Material | S235JR (or equivalent) seamless or ERW tube | Mill certificate required | Yield >=235 MPa |
| Length (cut to length) | 3,000 mm | +/-5 mm | Between base plate and top plate weld lines |
| Straightness | <=2 mm per meter (<=6 mm over full length) | — | Check with straight edge or laser alignment |
| Surface finish (before HDG) | Sa 2.5 blast | ISO 8501-1 | Standard pre-galvanize preparation |
| HDG coating | >=85 um average, >=70 um local minimum | Per ASTM A123 | Batch galvanize with base plate and top plate already welded |

### 4.2 Mast Base Plate

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Dimensions | 150x150x8 mm S235 plate | +/-1 mm on length/width; +/-0.5 mm on thickness | Laser- or plasma-cut, edges deburred |
| Bolt holes | 4x Ø14 mm clearance for M12 bolts on 120 mm bolt circle | Hole position +/-0.5 mm | Drill or CNC punch after welding to tube |
| Tube-to-base plate weld | 6 mm fillet weld, continuous all-around | Weld leg 6 +/-1 mm | E43xx electrode; weld before galvanizing |
| Perpendicularity (tube to plate) | <=0.5 deg | — | Check with angle square after welding |

### 4.3 Mast Base Gussets (per D8 Section 2.8)

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Quantity | 4 per mast, at 90 deg apart around tube | Angular spacing +/-5 deg | Oriented to resist bending in any direction |
| Gusset plate | 6 mm thick S235, right-triangle: 80 mm height x 40 mm base | +/-1 mm on both dimensions | Plasma- or laser-cut |
| Gusset-to-tube weld | 6 mm fillet weld, both sides of gusset | Continuous, both legs | Weld toe dressed smooth to reduce fatigue notch |
| Gusset-to-base plate weld | 6 mm fillet weld, full base edge | Continuous | — |
| Effect | Increases effective W at base by ~35% (W_eff ~ 12,473 mm3) | — | Reduces utilization from 104% to 77% at LC4 |
| Mass per mast | 0.60 kg (4 gussets) | — | Total +4.8 kg for 8 masts |

### 4.4 Mast Top Plate

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Dimensions | 200x200x8 mm S235 plate | +/-1 mm on length/width; +/-0.5 mm on thickness | A7 specifies 120x120x8 at IF-04; enlarged to 200x200 to improve reflector footprint stability and provide space for 4x M10 bolts + 2x dowel pins |
| M10 tapped holes | 4x M10 tapped through holes on 160x160 mm square pattern | Hole position +/-0.2 mm (Tier T2) | Tapped after galvanizing using stainless steel taps; alternatively, weld SS316 Helicoil-style threaded inserts before HDG |
| Dowel pin holes | 2x Ø8 H7 (+0.000/+0.015 mm) reamed holes on diagonal, 160 mm apart | Position +/-0.05 mm (Tier T1) | Reamed after galvanizing; define datum for reflector alignment |
| Tube-to-top plate weld | 6 mm fillet weld, continuous all-around | Weld leg 6 +/-1 mm | — |
| Perpendicularity (plate to tube) | <=0.3 deg | — | Critical for reflector verticality; check with precision square |
| Top surface flatness | <=0.1 mm across 200 mm | — | Machine-skim after galvanizing if required |

### 4.5 Locking Pin

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Type | Spring-loaded quick-release pin (ball-lock type) | — | Commercial marine hardware; one-hand operation |
| Pin diameter | 10 mm | +0/-0.05 mm | Fits through aligned 12 mm holes (2 mm clearance for field insertion) |
| Pin length | >=100 mm (passes through socket wall + mast tube + socket wall) | — | Total wall passage: 8 + ~4 + 8 = ~20 mm; pin must extend through both socket walls |
| Material | SS316 pin body; spring-steel internal spring | — | Corrosion-resistant; no galvanic issue in HDG socket |
| Retention | Integral ball-lock detent OR R-clip on outboard end | — | Prevents vibration-induced ejection; backup: 0.8 mm SS safety wire from pin lanyard eye to mast base plate |
| Lanyard | 300 mm SS316 wire rope lanyard, swaged both ends | — | Pin tethered to mast base plate to prevent loss at sea |

### 4.6 Mast Assembly Mass Summary

| Sub-component | Mass (kg) | Notes |
|---------------|-----------|-------|
| Tube (60.3 OD x 4.0 wall x 3,000 mm, HDG) | 16.6 | 7,850 x 703.7e-6 x 3.0 = 16.6 kg (incl. HDG ~0.5 kg) |
| Base plate (150x150x8 mm) | 1.4 | — |
| Top plate (200x200x8 mm) | 2.5 | — |
| 4x gussets (6 mm, 80x40 triangle) | 0.6 | — |
| Locking pin + lanyard | 0.2 | — |
| Welds + HDG on plates | 0.7 | — |
| **Mast assembly total** | **22.0** | Per unit; 8x = 176 kg total |

---

## 5. Reflector Specifications (M4, qty 8 identical)

### 5.1 Face Plates (3 per reflector, 24 total)

| Parameter | Specification | Tolerance | Tier | Notes |
|-----------|---------------|-----------|------|-------|
| Material | 6061-T6 aluminum per ASTM B209 | Mill certificate required | — | Temper verified by hardness test (Brinell 95 HB typical) |
| Plate dimensions | 800 x 800 mm | +/-0.5 mm on both edges | T2 | CNC-trimmed from oversized stock |
| Thickness | 3.0 mm | +/-0.1 mm | T2 | Rolled stock tolerance; verify with micrometer at 5 points per plate |
| Flatness | <0.1 mm over full 800x800 mm face | Measured on CMM or granite surface plate with dial indicator | T2 | CRITICAL for RCS. CNC fly-cut on vacuum fixture; stress-relieve if needed |
| Surface roughness (reflective face) | Ra <=6.3 um | Measured with profilometer; 3 readings per plate | T2 | Fly-cut finish; finer than Ra 10 um originally specified — achievable with sharp diamond or carbide insert |
| Surface roughness (back face) | Ra <=12.5 um | — | T3 | Standard milled finish; non-critical |
| Edge condition | 0.5 mm x 45 deg chamfer on all edges | +/-0.2 mm | T3 | Deburr all edges; no sharp edges for handling safety |
| Mounting holes | 4x Ø7 mm clearance for M6 bolts; 2x Ø5 H7 (+0.000/+0.012 mm) reamed dowel holes | Hole position +/-0.1 mm from datum edge | T2 | Bolt holes at 4 corners; dowel holes on one edge (alignment datum) |
| Hole pattern | Per reflector frame drawing (unique per face position: Face A, B, C) | Match-drilled to AM frame or per coordinated CNC program | — | Faces A/B/C mount to orthogonal frame surfaces; hole patterns differ by face |
| Surface treatment | Type II anodize (sulfuric acid) per MIL-A-8625F, Class 1 (clear/natural) | Thickness >=10 um, <=25 um | — | Clear anodize preserves reflectivity; do NOT dye |
| Post-anodize reflectivity | No degradation verification required | — | — | Type II clear anodize is transparent to X-band radar (9.4 GHz); skin depth 0.82 um << 10 um anodize layer (non-conductive layer on conductive substrate — radar penetrates anodize to metal) |
| Mass per plate | 5.18 kg nominal (2,700 x 0.800 x 0.800 x 0.003) | +/-0.3 kg | — | — |

### 5.2 AM Structural Frame (1 per reflector, 8 total)

| Parameter | Specification | Tolerance | Tier | Notes |
|-----------|---------------|-----------|------|-------|
| Material | AlSi10Mg per ASTM F3318 | Powder certification + build coupon tensile test | — | Laser Powder Bed Fusion (LPBF) |
| Heat treatment | T5 stress relief + artificial aging | Per ASTM F3318 or AM bureau SOP | — | 300 deg C / 2h (typical for AlSi10Mg T5) |
| Post-machining | Datum surfaces, mounting bosses, bolt holes, dowel holes CNC-machined after printing and heat treatment | — | — | AM bureau performs post-machining |
| **Orthogonality (critical)** | All 3 face-mounting surfaces at 90.00 deg to each other | +/-0.05 deg per face pair (Tier T1) | T1 | MASTER TOLERANCE — drives RCS performance. Verified by CMM on all 8 frames. Reject if any pair exceeds +/-0.08 deg. |
| Mounting bosses (face plate interface) | 3 sets of mounting surfaces, each with 4x M6 tapped holes + 2x Ø5 H7 dowel holes | Tapped holes: +/-0.2 mm position; Dowel holes: +/-0.05 mm position (T1) | T1/T2 | Helicoil M6 x 1.5D inserts in AlSi10Mg (direct tapping unreliable for cyclic loads) |
| Mounting boss surface flatness | <=0.05 mm per mounting surface | CMM verified | T1 | Post-machined; reference surface for face plate seating |
| Base flange (mast interface) | 200x200x6 mm integral flange at bottom of frame | Flatness <=0.1 mm | T2 | Mates with mast top plate at IF-04 |
| Alignment dowel holes (base flange) | 2x Ø8 H7 (+0.000/+0.015 mm), on diagonal 160 mm apart | Position +/-0.05 mm (T1) | T1 | Must match mast top plate dowel holes within 0.05 mm for repeatable alignment |
| M10 bolt clearance holes (base flange) | 4x Ø11 mm on 160x160 mm square pattern | Position +/-0.2 mm | T2 | Through-holes (clearance); mast top plate has tapped holes |
| Surface roughness (as-printed, non-critical) | Ra 8-15 um acceptable | — | — | Non-functional surfaces; cosmetic only |
| Surface roughness (machined datums) | Ra <=3.2 um | — | T2 | Post-machined mounting surfaces |
| Surface treatment | Type III hard anodize per MIL-A-8625F, Class 1 | Thickness >=25 um | — | Hard coat for corrosion + wear resistance; dark grey/black appearance acceptable |
| Minimum wall thickness (lattice elements) | >=2.0 mm | — | — | Per LPBF design rules; walls <2 mm risk incomplete fusion |
| Frame overall dimensions | Approximately 800x800x800 mm trihedral envelope | +/-2 mm on envelope | T3 | — |
| Mass per frame | 8.5 kg nominal (lattice-optimized) | +/-1.0 kg | — | Topology-optimized; actual mass depends on AM build parameters |
| Mechanical properties (minimum) | sigma_y >=230 MPa (XY), >=210 MPa (Z); sigma_UTS >=350 MPa; elongation >=5% | Per build coupon | — | Test 1 coupon per build plate (8 frames may span 2-4 build plates) |

### 5.3 Reflector Assembly (M4)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Face-to-frame fasteners | 4x M6x20 A4-80 (SS316) socket head cap screws per face (12 per reflector) | Torque: 8 +/-1 N-m; with Nylock nut or thread-locking compound (Loctite 243) |
| Face-to-frame dowel pins | 2x Ø5 m6 x 12 mm SS316 dowel pins per face (6 per reflector) | Light press fit into frame H7 holes; slide fit into face plate H7 holes |
| Galvanic isolation (face to frame) | NOT required (both aluminum alloys; potential difference ~50-100 mV; anodize on both provides isolation) | Apply anti-seize (Tef-Gel) on all fasteners |
| Safety wire | MS20995-C32 (0.032" dia SS safety wire) through bolt heads in pairs | 2 loops of 2 bolts per face = 6 wire loops per reflector |
| Assembly environment | Clean, covered workspace; no sand/grit on mating surfaces | Contamination between face plates and frame bosses degrades flatness |
| Assembled orthogonality verification | CMM measurement of all 3 face-pair angles | Pass: all pairs within +/-0.10 deg of 90.00 deg |
| Mass per reflector assembly | 15.0 kg nominal (frame 8.5 + 3 faces 5.18 each + fasteners 0.9) | Target: <=17 kg maximum |

### 5.4 Reflector-to-Mast Interface (IF-04)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Fasteners | 4x M10x25 A4-80 (SS316) hex bolts | Through reflector base flange clearance holes into mast top plate tapped holes |
| Nuts | M10 A4-80 Nylock prevailing-torque nuts | Backup to tapped hole; double-nutted for redundancy if field-serviceable |
| Torque | 15 +/-2 N-m | Low torque to avoid crushing anodize; Nylock provides vibration retention |
| Dowel pins | 2x Ø8 m6 x 20 mm SS316 cylindrical dowel pins | Press fit into mast top plate H7 holes; slide fit into reflector base flange H7 holes |
| Galvanic isolation | Nylon isolation bushings (11 mm ID x 16 mm OD x 8 mm long) in all 4 bolt holes | Prevents HDG steel-to-anodized aluminum galvanic contact |
| Isolation washers | HDPE flat washers (20 mm OD x 11 mm ID x 2 mm thick) under bolt heads and Nylock nuts | — |
| Moisture barrier | Sikaflex 291 marine sealant, thin film on mating face | Prevents electrolyte bridging in salt spray environment |
| Safety wire | MS20995-C32 through all 4 bolt heads in 2 pairs | Backup to Nylock; prevents vibration loosening over 40,000 wave cycles |

---

## 6. Mooring Specifications (M7)

### 6.1 Chain

| Parameter | Specification | Tolerance | Notes |
|-----------|---------------|-----------|-------|
| Grade | G30 proof coil per ASTM A413 (or NACM equivalent) | — | Proof tested at factory |
| Nominal size | 19 mm (3/4") link diameter | Per manufacturer standard | Revised from 12/16 mm per D8 Section 4.1: 19 mm SWL 5,800 kgf meets 4,536 kgf requirement |
| SWL | 5,800 kgf (56.9 kN) | Minimum | Per chain manufacturer WLL table |
| Breaking load | 17,400 kgf (170.7 kN) | Minimum | 3:1 design factor on SWL |
| Coating | Hot-dip galvanize >=85 um per ASTM A123 | — | Factory-applied |
| Weight in air | 7.9 kg/m nominal | — | — |
| Weight in water (submerged) | 6.9 kg/m nominal | — | — |
| Chain lengths per deployment depth | Kit A (15 m depth): 90 m; Kit B (30 m): 20 m; Kit C (50 m): 20 m | +/-1 m (cut to length) | Kit A: all-chain catenary; Kit B/C: hybrid chain + rode |
| End fittings | Enlarged end link or pear link for shackle connection at each end | — | — |

### 6.2 Polyester Rode (Kits B and C)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Material | Polyester double-braid rope | UV-stabilized, marine grade |
| Diameter | 24 mm (upgraded from 20 mm per D8 Section 4.2) | SWL ~4,500 kgf at 24 mm; SF 3.0 on 1,519 kgf peak |
| SWL | >=4,500 kgf | — |
| Breaking load | >=13,500 kgf | — |
| Lengths | Kit B (30 m): 35 m; Kit C (50 m): 60 m | +/-0.5 m |
| Termination | Spliced eye with SS316 thimble at each end | Eye splice per ABYC H-40; thimble rated >=6,000 kgf |
| Stretch at working load | 15-20% (provides shock absorption) | — |

### 6.3 Anchor

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Type (primary) | Danforth (fluke-style) | Best holding-to-weight ratio in sand/firm bottom |
| Weight (sand/hard bottom) | 75 kg | Holding power ~1,500 kgf in medium sand (20:1 ratio); marginal at LC4 — acceptable |
| Weight (mud/soft bottom) | 100 kg Danforth or dual 75 kg in tandem | Per D8 Section 4.3 |
| Material | Cast steel, HDG | >=85 um zinc coating |
| Shank length | Per manufacturer standard for rated weight class | — |
| Alternative (rocky bottom) | Bruce (claw) type, 100 kg | Holding ~1,500 kgf (15:1 ratio) |

### 6.4 Swivel

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Type | Jaw-jaw marine swivel | Allows 360 deg weathervaning |
| SWL | >=5,000 kgf (49.0 kN) | Minimum-rated component in mooring chain; 110% of required 4,536 kgf SWL |
| Breaking load | >=15,000 kgf | 3:1 on SWL |
| Material | Alloy steel, HDG | — |
| Connection | Jaw fits 19 mm chain link at bottom; jaw fits shackle pin at top | — |
| Rotation | Free rotation under load <=1,500 kgf; stiff above (acceptable) | — |

### 6.5 Shackles (Mooring System)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Type | Crosby G-2130 bolt-type anchor shackle (or equivalent) | — |
| Size | 3/4" (19 mm) pin diameter | — |
| SWL | 4,750 kgf (46.6 kN) | Exceeds 4,536 kgf requirement |
| Breaking load | >=28,500 kgf | 6:1 design factor (Crosby standard) |
| Material | Forged alloy steel, HDG | — |
| Quantity per mooring set | 4 (anchor-to-chain, chain-to-swivel, swivel-to-rode, rode-to-pad eye) | — |
| Pin security | Mousing wire (1.6 mm SS wire through pin hole and shackle body) on all shackles | Prevents pin loosening under cyclic load |

---

## 7. GPS Beacon Specifications (M6)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| GNSS receiver | Multi-constellation (GPS + GLONASS + BeiDou minimum) | CEP <=5 m (SIG-007) |
| Communication | Iridium Short Burst Data (SBD) modem | Global coverage, no cellular dependency |
| Reporting rate | 1 Hz position acquisition; report every 60 s to shore (configurable) | ENR-002 |
| Enclosure | IP68 rated (submersible to 2 m for 30 min) | Polycarbonate or ABS-PC blend |
| Enclosure dimensions | <=250 x 150 x 100 mm | — |
| Battery | Li-ion 18650 pack, >=20 Wh | >=72 h endurance at 1 Hz GPS + 60 s Iridium reporting (ENR-001) |
| Operating temperature | -10 deg C to +60 deg C | Tropical marine environment |
| Mounting clamp | SS316 U-bolt bracket, 2x M8 x 60 mm ID U-bolts | Fits 60.3 mm mast OD; saddle plate 80x40x5 mm SS316 |
| Mounting height | >=4,000 mm above deck level (>=4,500 mm AWL) | On designated GPS mast; use 500 mm extension tube if needed |
| U-bolt torque | 15 +/-2 N-m | — |
| Antenna orientation | GNSS patch antenna facing zenith (upward) +/-5 deg | Self-correcting wide-beam antenna |
| Cable | 5 m shielded coax, UV-resistant jacket, with drip loop at deck grommet | Cable-tied to mast exterior at 300 mm intervals |
| Mass | <=5 kg total (electronics 1.5, battery 1.0, enclosure 1.5, bracket 1.0) | — |
| Activation | Magnetic reed switch or waterproof push-button | Field-operable with gloves; no tools required |

---

## 8. Tow System Specifications (M8)

### 8.1 Tow Bridle

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Material | Dyneema SK75 (UHMWPE) | Highest strength-to-weight ratio for tow applications |
| Diameter | 16 mm, 12-strand construction | — |
| SWL | >=8,000 kgf (78.5 kN) | FOR-008: 3:1 on estimated 2,508 kgf peak tow load |
| Breaking load | >=24,000 kgf | — |
| Configuration | 2-point bridle; 2 legs from hull tow padeyes converge to single tow eye | 60 deg included angle between legs |
| Leg length | 15 m each | +/-0.5 m |
| Main tow line length | 50-100 m (adjustable to sea conditions) | — |
| Termination (bridle legs) | Soft eye with SS316 thimble (rated >=6,000 kgf) | Professional splice per Dyneema guidelines; 72x core tuck minimum |
| Termination (tow end) | Hard eye with SS316 thimble + Crosby G-2130 shackle | 3/4" shackle (SWL 4,750 kgf) |
| Chafe protection | Dyneema chafe sleeve, 600 mm length, at each padeye contact point | — |
| UV protection | Factory-applied cover braid (polyester) over core | — |

### 8.2 Trailing Drogue

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Type | Conical sea drogue | Yaw damping during tow |
| Diameter (mouth) | 600 mm | — |
| Length | 900 mm | — |
| Material | UV-stabilized nylon canvas, 600D minimum | Reinforced rim with SS ring |
| Bridle | 4-point bridle to single tow point on hull stern | 8 mm polyester, 2 m legs |
| Attachment | Shackled to stern tow padeye or dedicated drogue ring | — |

---

## 9. Fastener Schedule

All fasteners for one complete target unit (M1-M8 on-platform, excluding mooring and tow kit consumable shackles).

| # | Location | Size | Grade / Material | Qty/Unit | Torque (N-m) | Corrosion Protection | Notes |
|---|----------|------|------------------|----------|-------------|---------------------|-------|
| F-01 | Frame-to-hull perimeter (IF-01) | M12 x 40 | SS316 A4-70 | 84 | 40 +/-3 | Inherent (SS316) | With 50x50x5 SS fender washer on HDPE side |
| F-02 | Pad eye backing plate to frame (IF-02 structural) | M16 x 60 | Gr 8.8 HDG | 8 | 190 +/-10 | HDG (>=85 um) | With hardened washer under head and nut |
| F-03 | Deck socket base plate to frame (IF-03) | M12 x 35 | Gr 8.8 HDG | 32 (4 per socket x 8) | 80 +/-5 | HDG (>=85 um) | — |
| F-04 | Tow padeye to hull/frame (IF-06) | M12 x 50 | Gr 8.8 HDG | 8 (4 per padeye x 2) | 80 +/-5 | HDG (>=85 um) | With 50x50x5 SS fender washer on HDPE side |
| F-05 | Reflector face to AM frame (M4 internal) | M6 x 20 | A4-80 (SS316) SHCS | 96 (12 per refl x 8) | 8 +/-1 | Inherent (SS316) | Nylock nut or Loctite 243; safety wire in pairs |
| F-06 | Reflector face dowel pins (M4 internal) | Ø5 m6 x 12 | SS316 | 48 (6 per refl x 8) | N/A (press fit) | Inherent (SS316) | Light press into frame H7; slide in face H7 |
| F-07 | Reflector to mast top (IF-04) | M10 x 25 | A4-80 (SS316) | 32 (4 per mast x 8) | 15 +/-2 | Inherent (SS316) | Nylon isolation bushing + HDPE washers; Nylock nut; safety wire |
| F-08 | Reflector to mast dowel pins (IF-04) | Ø8 m6 x 20 | SS316 | 16 (2 per mast x 8) | N/A (press fit) | Inherent (SS316) | Press into mast top plate H7; slide into reflector flange H7 |
| F-09 | Mast locking pin (IF-03) | Ø10 spring ball-lock pin | SS316 | 8 | N/A (hand insert) | Inherent (SS316) | With 300 mm SS wire lanyard |
| F-10 | GPS beacon U-bolts (IF-05) | M8 x 60 mm ID U-bolt | SS316 | 2 | 15 +/-2 | Inherent (SS316) | Saddle plate 80x40x5 SS316 |
| F-11 | GPS beacon enclosure to bracket (IF-05) | M6 x 16 | SS316 | 4 | 5 +/-1 | Inherent (SS316) | — |
| F-12 | Hull section joint (IF-07, if 2-section) | M10 x 40 | SS316 A4-70 | 24 | 25 +/-3 | Inherent (SS316) | With flat washer + fender washer on outer HDPE face |
| F-13 | Hull section alignment dowels (IF-07) | Ø12 x 30 nylon | Nylon 6/6 | 3 | N/A (push fit) | N/A (polymer) | Alignment only; no structural load |
| F-14 | Zinc anode to pad eye | M10 x 30 | SS316 | 1 | 15 +/-2 | Inherent (SS316) | — |
| F-15 | Hull backing channel bolts (IF-07, if 2-section) | M10 x 50 | Gr 8.8 HDG | 12 (6 per side) | 40 +/-3 | HDG (>=85 um) | Through HDPE hull and steel channel |
| | **TOTAL FASTENERS (approx.)** | | | **~344** | | | Excluding mooring/tow shackles |

---

## 10. Surface Finish Schedule

| # | Component | Material | Primary Finish | Coating / Treatment | Min Thickness | Standard | Color | Notes |
|---|-----------|----------|----------------|---------------------|---------------|----------|-------|-------|
| S-01 | Hull shell | HDPE PE100 | As-molded or welded | None required | N/A | — | Black (carbon-black) | Inherent UV/salt resistance |
| S-02 | PU foam fill | Rigid PU | As-poured | None (encapsulated in hull) | N/A | — | White/cream | Not exposed to environment |
| S-03 | Frame perimeter ring | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | — |
| S-04 | Frame cross members | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | — |
| S-05 | Center hub plate | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | — |
| S-06 | Pad eye (ring + eye plate + backing plate) | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | UT-inspected weld before HDG |
| S-07 | Deck sockets (8x) | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | Bore reamed smooth after HDG |
| S-08 | Tow padeyes (2x) | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | — |
| S-09 | Mast tubes (8x) | S235JR | Sa 2.5 blast pre-HDG | Hot-dip galvanize | >=85 um avg, >=70 um local | ASTM A123 | Silver-grey (zinc) | Full assembly (tube + plates + gussets) HDG as unit |
| S-10 | Mast top plates (8x) | S235JR | Machine-skim top face after HDG | Hot-dip galvanize + machine top face | >=85 um (sides); top face machined bright | ASTM A123 | Silver-grey; top face bright | Top face flatness <=0.1 mm; re-apply zinc-rich primer (Zinc Clad IV) on machined area |
| S-11 | Reflector face plates (24x) | 6061-T6 Al | CNC fly-cut (reflective face); CNC mill (back face) | Type II sulfuric anodize, Class 1 (clear) | >=10 um, <=25 um | MIL-A-8625F Type II | Clear/natural aluminum | Do NOT dye; clear anodize preserves radar reflectivity |
| S-12 | Reflector AM frames (8x) | AlSi10Mg | As-printed (bulk); CNC post-machined (datums) | Type III hard anodize, Class 1 | >=25 um | MIL-A-8625F Type III | Dark grey/black (natural hard anodize) | Hard coat for corrosion + wear; machined datums anodized to same spec |
| S-13 | Mooring chain | G30 steel | As-manufactured | Hot-dip galvanize | >=85 um | ASTM A123 | Silver-grey (zinc) | Factory-applied by chain manufacturer |
| S-14 | Anchor (Danforth) | Cast steel | Shot-blasted | Hot-dip galvanize | >=85 um | ASTM A123 | Silver-grey (zinc) | — |
| S-15 | Swivel | Alloy steel | Machined | Hot-dip galvanize | >=85 um | ASTM A123 | Silver-grey (zinc) | — |
| S-16 | Shackles (mooring) | Forged alloy steel | As-forged | Hot-dip galvanize | >=85 um | ASTM A123 | Silver-grey (zinc) | Crosby G-2130 or equivalent |
| S-17 | GPS enclosure | ABS-PC blend | Injection molded | UV-stabilized compound | N/A | IP68 per IEC 60529 | Black or olive drab | — |
| S-18 | GPS bracket + U-bolts | SS316 | Machine-finished | Passivation | N/A | ASTM A967 (passivation) | Natural SS (silver) | — |
| S-19 | Tow bridle (Dyneema) | UHMWPE | As-manufactured | Cover braid (polyester UV jacket) | N/A | — | White or high-vis orange | — |
| S-20 | Drogue | Nylon 600D canvas | Sewn | UV-stabilized fabric | N/A | — | Orange (high-vis) | — |

---

## 11. Dimensional Summary — Key Assembly Dimensions

### 11.1 System-Level Dimensions

| Dimension | Nominal | Tolerance | Source |
|-----------|---------|-----------|--------|
| Platform outer diameter | 8,000 mm | +/-100 mm | GEO-001 |
| Hull depth | 500 mm | +/-50 mm | GEO-002 |
| Design draft (at 990 kg displacement) | ~19 mm | — | D8 Section 5.1 (calculated) |
| Freeboard | ~481 mm | — | Derived (hull depth - draft) |
| Deck socket circle radius | 3,200 mm from center | +/-5 mm | A7/D8 layout |
| Mast height above deck | 3,000 mm | +/-5 mm | GEO-010 |
| Reflector center height AWL | ~4,000 mm | — | 500 deck + 3,000 mast + 500 reflector CG |
| GPS beacon height AWL | >=4,500 mm | — | GEO-006; 500 mm extension tube if needed |
| Total height above keel (max) | ~5,500 mm | — | Keel to GPS beacon tip |
| Mast-to-mast arc distance (at R=3,200 mm) | 2,513 mm | — | pi x 6,400 / 8 |
| Reflector edge-to-edge clearance | 1,713 mm | — | 2,513 - 800 = 1,713 mm |
| Total displacement (as-built) | <=1,100 kg (target 990 kg) | — | GEO-007 limit; D8 mass update incl. gussets |

### 11.2 Critical Interface Dimensions

| Interface | Mating Dimension | Male Part | Female Part | Clearance / Fit |
|-----------|-----------------|-----------|-------------|-----------------|
| IF-03 (mast to socket) | Ø60.3 tube into Ø100 bore | Mast tube: 60.3 +/-0.5 mm | Socket bore: 100 +0/-1 mm | ~20 mm radial clearance; mast centered by base plate seating on socket flange |
| IF-04 (reflector to mast, bolts) | M10 bolts through Ø11 clearance into M10 tapped | Reflector flange: 4x Ø11 mm | Mast top plate: 4x M10 tapped | 1 mm diametral clearance; alignment by dowel pins |
| IF-04 (reflector to mast, dowels) | Ø8 H7/m6 | Reflector flange: 2x Ø8 H7 (+0/+0.015) | Mast top plate: 2x Ø8 H7 (+0/+0.015); Pin: Ø8 m6 (+0.009/+0.025) | Transition fit: pin press-fits into mast top plate (m6 in H7 = 0.006 to 0.025 mm interference); slide-fits into reflector flange |
| IF-02 (shackle to pad eye) | 19 mm shackle pin through 80 mm ID ring | Shackle pin: 19 mm | Pad eye ring: 80 mm ID | Large clearance; ring oversized for ease of field connection |
| IF-05 (GPS to mast) | 60.3 mm OD tube in M8 x 60 mm ID U-bolt | Mast tube: 60.3 mm | U-bolt: 60 mm ID (elastically deforms over tube) | Clamping friction holds GPS bracket; no precision fit |

---

## 12. Mass Budget — Final Revision

Updated from D8 Section 8.4, incorporating mast gussets (+4.8 kg), revised backing plate (+1.3 kg), and corrected mast mass (22.0 kg per unit with enlarged top plate).

| # | Component | Qty | Mass Each (kg) | Mass Total (kg) | Notes |
|---|-----------|-----|----------------|-----------------|-------|
| 1 | Hull shell (HDPE) | 1 | 200 | 200 | — |
| 2 | PU foam fill | 1 | 121 | 121 | At 40 kg/m3, 80% fill of 3.78 m3 |
| 3 | Structural frame (ring + cross + hub + padeyes) | 1 | 155 | 155 | Includes 14 mm backing plate (+1.3 kg from D8 update) |
| 4 | Mast assemblies (tube + plates + gussets + pin) | 8 | 22.0 | 176 | Revised from 16.3 kg; enlarged top plate 200x200x8 |
| 5 | Reflector assemblies (frame + 3 faces + fasteners) | 8 | 15.0 | 120 | — |
| 6 | GPS beacon assembly | 1 | 5.0 | 5 | — |
| 7 | On-hull mooring hardware (pad eye, swivel, shackles) | 1 | 15 | 15 | Top-side hardware only; chain/anchor deployed separately |
| 8 | Hull section joint hardware (IF-07, if 2-section) | 1 | 12 | 12 | 24x M10 bolts + backing channel + gasket |
| 9 | Frame-to-hull fasteners (IF-01) | 84 | 0.08 | 7 | M12 SS316 + washers |
| 10 | Deck equipment (cleats, lifting eyes, cable ties, misc) | — | — | 20 | Allowance |
| 11 | Zinc anodes | 2 | 0.5 | 1 | 1 at pad eye + 1 at waterline |
| | **ON-PLATFORM SUBTOTAL** | | | **832** | — |
| 12 | Mooring chain (on-hull segment, 3 m) | 1 | 23.7 | 24 | 3 m of 19 mm G30 at 7.9 kg/m; fairlead to first shackle |
| 13 | Tolerances and unaccounted items (10% margin) | — | — | 83 | — |
| | **TOTAL DISPLACEMENT (deployed, without mooring weight in water)** | | | **939** | Below 1,100 kg limit; 161 kg margin |

**Note:** Mooring chain and anchor weight below waterline is not included in platform displacement — submerged chain weight transfers to the seabed via catenary, not to the platform. Only the chain segment from fairlead to water surface contributes to platform displacement, and this is captured in item 12 above.

---

## 13. Inspection and Acceptance Criteria

### 13.1 First Article Inspection (FAI)

The following measurements and tests are mandatory on the FIRST unit produced. Subsequent units follow the reduced Production Inspection plan (Section 13.2).

| # | Item | Method | Accept Criteria | Reject Action |
|---|------|--------|----------------|---------------|
| FAI-01 | Hull OD | Tape measure at 4 positions | 8,000 +/-100 mm | Rework or scrap hull |
| FAI-02 | Hull wall thickness | UT thickness gauge at 8 positions | >=8 mm at all points | Reject hull |
| FAI-03 | Foam density | Cut sample coupon, weigh, measure volume | 32-48 kg/m3 | Reject foam batch; re-pour |
| FAI-04 | Foam water absorption | 48h immersion test on coupon | <=3% by volume | Reject foam batch |
| FAI-05 | Frame dimensional check | Tape + laser level; socket positions | Socket radius 3,200 +/-5 mm; angles 45 +/-0.5 deg | Rework frame |
| FAI-06 | HDG coating thickness | Magnetic thickness gauge at 10 points per assembly | >=85 um avg, >=70 um min | Re-galvanize |
| FAI-07 | Pad eye weld UT inspection | Ultrasonic testing per AWS D1.1 | No defects >3 mm | Repair weld and re-test |
| FAI-08 | Pad eye proof load test | Pull test to 6,804 kgf (1.5x SWL) | No permanent deformation | Reject pad eye assembly |
| FAI-09 | Mast straightness | Straight edge + feeler gauge | <=2 mm/m over 3,000 mm | Straighten or replace |
| FAI-10 | Mast top plate flatness | Granite flat + dial indicator | <=0.1 mm | Machine-skim |
| FAI-11 | Mast top plate perpendicularity | Precision square + feeler gauge | <=0.3 deg | Rework weld; re-machine |
| FAI-12 | Face plate flatness (all 24) | CMM or granite flat + dial indicator | <0.1 mm over 800 mm | Re-fly-cut on vacuum fixture |
| FAI-13 | Face plate Ra (reflective face) | Profilometer, 3 readings per plate | Ra <=6.3 um | Re-fly-cut |
| FAI-14 | Anodize thickness (face plates) | Eddy current gauge | >=10 um, <=25 um | Re-anodize |
| FAI-15 | AM frame orthogonality (all 8) | CMM, 3 face-pair angle measurements per frame | 90.00 +/-0.10 deg all pairs | Reject frame; re-print if >0.08 deg on raw frame |
| FAI-16 | AM frame tensile coupon | Tensile test per ASTM F3318 | sigma_y >=230 MPa (XY); elongation >=5% | Reject build plate lot |
| FAI-17 | Hard anodize thickness (frames) | Eddy current gauge | >=25 um | Re-anodize |
| FAI-18 | Assembled reflector orthogonality | CMM, 3 pairs per reflector | 90.00 +/-0.10 deg all pairs | Disassemble, identify root cause, reassemble |
| FAI-19 | Total platform mass | Floor scale | <=1,100 kg | Identify and remove excess mass |
| FAI-20 | GPS beacon 72h endurance | Power-on test in controlled environment | >=72 h at 1 Hz GPS + 60 s Iridium report | Replace battery pack; re-test |
| FAI-21 | RCS spot check (first article) | Outdoor or anechoic chamber measurement at X-band (9.4 GHz) | >=700 m2 minimum (SIG-003); avg across 360 deg >=1,000 m2 (SIG-002) | Diagnose reflector alignment; rework as needed |

### 13.2 Production Inspection (Subsequent Units)

| # | Item | Frequency | Method |
|---|------|-----------|--------|
| PI-01 | Hull OD and wall thickness | 100% | Tape + UT gauge |
| PI-02 | Foam density (batch sample) | 1 per foam batch | Coupon test |
| PI-03 | HDG thickness | 100% at 4 points per assembly | Magnetic gauge |
| PI-04 | Pad eye weld UT | 100% | UT per AWS D1.1 |
| PI-05 | Face plate flatness | 100% | CMM or granite flat |
| PI-06 | AM frame orthogonality | 100% | CMM |
| PI-07 | Assembled reflector orthogonality | 100% | CMM |
| PI-08 | Total platform mass | 100% | Floor scale |
| PI-09 | GPS endurance | 10% (1 per 10 units) or 100% if failure occurred | 72h run test |
| PI-10 | RCS measurement | 10% (1 per 10 units) | X-band range test |

---

## 14. Cross-References

### Phase 3 Documents (This Phase)

- [[PRAD_D8_design_structure.md]] -- Step D8: Structural analysis, load cases, mast bending (gusset solution), pad eye sizing (14 mm backing plate), mooring chain sizing (19 mm G30), catenary analysis, hull stability (GM = 208 m)
- [[PRAD_A7_architecture_definition.md]] -- Step A7: System architecture, 8 modules (M1-M8), 7 interfaces (IF-01 to IF-07), containment tree, assembly sequences, interface control document
- [[RISM_M4_material_analysis.md]] -- Step M4: Material selection matrices for all 5 component groups (HDPE hull, S235 HDG frame, 6061-T6 face plates, AlSi10Mg AM frames, G30 HDG chain)
- [[RISM_R1_requirements_identification.md]] -- Step R1: 74 direct embodiment requirements mapped to subsystems
- [[RISM_S3_material_selection.md]] -- Step S3: Material candidate screening

### Phase 1 Source Documents

- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1); GEO-001 to GEO-010, FOR-001 to FOR-011, MAT-001 to MAT-010, SIG-001 to SIG-009
- [[../01_requirements/standards_mapping.md]] -- MIL-STD-810H, MIL-A-8625F, ASTM A123, ASTM F3318, AWS D1.1, ISO 2768-mK

### Phase 2 Source Documents

- [[../02_conceptual/concept_selection.md]] -- Concept A "Baseline Optimized" (VDI 2225: 81.8%)
- [[../02_conceptual/function_structure.md]] -- F1-F7 function decomposition

### Standards Referenced

| Standard | Title | Application |
|----------|-------|-------------|
| ISO 2768-mK | General tolerances (medium linear, coarse angular) | All dimensions without explicit tolerance |
| ASTM A123 / ISO 1461 | Hot-dip galvanized coatings on iron and steel products | All S235 steel components |
| MIL-A-8625F | Anodic coatings for aluminum and aluminum alloys | Type II (face plates), Type III (AM frames) |
| ASTM F3318 | Standard for additive manufacturing of AlSi10Mg via LPBF | AM reflector frames |
| ASTM B209 | Aluminum and aluminum-alloy sheet and plate | 6061-T6 face plates |
| EN 10025-2 | Hot-rolled structural steel (S235JR) | Frame and mast material |
| EN 10219-2 | Cold-formed welded structural hollow sections | Mast tubes |
| AWS D1.1 | Structural welding code — steel | All structural welds |
| ASTM A413 (NACM) | Standard specification for steel chain | G30 proof coil chain |
| IEC 60529 | Degrees of protection provided by enclosures (IP code) | GPS beacon enclosure (IP68) |
| ASTM D3350 | Standard specification for polyethylene pipe and fittings materials | HDPE hull material |
| ASTM D1621 / D1622 / D2842 | Rigid cellular plastics (compressive, density, water absorption) | PU foam fill |

---

**Document Status:** Draft v1.0 — Complete detail specification covering all components, tolerances, surface finishes, fasteners, and inspection criteria. Key specification decisions:

1. General tolerance ISO 2768-mK applied system-wide; precision tolerances (T1: +/-0.05 deg, +/-0.05 mm) applied ONLY to reflector orthogonality datums and dowel pin positions.
2. Mast top plate enlarged to 200x200x8 mm (from 120x120x8 in A7) to accommodate 160x160 mm bolt/dowel pattern for improved reflector stability.
3. Face plate surface roughness tightened to Ra <=6.3 um (from <=10 um in A7) — achievable by CNC fly-cut with sharp insert.
4. 19 mm G30 chain confirmed (per D8 structural analysis); 24 mm polyester rode for hybrid kits (upgraded from 20 mm per D8 catenary analysis).
5. All 344 fasteners fully specified with size, grade, torque, and corrosion protection.
6. Total on-platform mass estimated at 939 kg with 161 kg margin to 1,100 kg limit.
7. Comprehensive FAI program (21 checks) and production inspection plan (10 checks) defined.
