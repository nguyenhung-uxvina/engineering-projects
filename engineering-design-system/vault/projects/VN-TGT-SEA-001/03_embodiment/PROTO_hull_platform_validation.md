---
project: VN-TGT-SEA-001
phase: 3
type: prototype_validation
step: "Hull Platform Prototype Build & Validation"
version: 1.0
created: 2026-02-10
status: draft
---

# HDPE Hull Platform — Prototype Build & Validation Plan

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Subsystem:** M1 Hull Assembly + IF-07 Two-Section Joint + IF-01 Frame-to-Hull Interface
**Purpose:** Fabricate one full-scale 8.0 m HDPE hull (2-section bolted), validate welding quality, joint watertightness, foam fill process, frame attachment, hydrostatic stability, and environmental durability before committing to production lot of 10 units.
**Input:** [[PRAD_D8_design_structure.md]] (Sections 5.1–5.4), [[DECS_D9_detail_specification.md]] (Section 2), [[DECS_E10_variant_evaluation.md]] (Decision 1), [[OCP_C14_cost_analysis.md]] (M1 BOM), [[OCP_P15_production_planning.md]] (Section 1.2, 4.1, 5.1)

---

## 1. Test Objectives

### 1.1 Why a Hull Prototype?

The hull is the single largest and heaviest subsystem (350 kg, 35.5% of displacement). Unlike the reflector (where AM is novel), the hull risk is in **process execution** — HDPE hot-plate welding of a 4.0 m semicircular hull section at production scale has not been validated with the Vietnamese supply chain. Key uncertainties:

1. **HDPE weld quality** — Hot-plate butt welds must achieve ≥80% of parent material tensile strength (≥17.6 MPa of 22 MPa HDPE PE100 yield)
2. **Two-section joint (IF-07)** — Bolted flange + EPDM gasket must be watertight at 72 h continuous immersion under cyclic wave loading
3. **Foam fill process** — Pour-in-place PU foam must achieve uniform density (32–48 kg/m³), ≥80% fill factor, and ≤3% water absorption
4. **HDPE creep under bolting** — M12 bolts at IF-01 and M10 bolts at IF-07 apply sustained compressive load on HDPE flanges; creep relaxation must not cause loosening over 72 h
5. **Hydrostatic performance** — Verify draft, freeboard, stability, and self-draining deck behavior at full design displacement

### 1.2 Test Objectives Summary

| # | Objective | Success Criterion | Requirement Ref |
|---|-----------|-------------------|-----------------|
| T-1 | HDPE weld tensile strength | ≥80% of parent (≥17.6 MPa) | HUL-001, HUL-003 |
| T-2 | IF-07 joint watertightness | Zero visible leak after 72 h immersion | HUL-005, OPR-002 |
| T-3 | IF-07 bolt torque retention | ≥80% of initial torque after 72 h under load | FOR-008 |
| T-4 | Foam fill density and coverage | 32–48 kg/m³ measured; ≥80% fill by volume; no void >200 mm dia | HUL-007, SAF-003 |
| T-5 | Foam water absorption | ≤3% by volume after 48 h immersion per ASTM D2842 | HUL-008, SAF-003 |
| T-6 | Hydrostatic stability | Draft ≤25 mm at 986 kg; freeboard ≥450 mm; self-draining deck | GEO-001, GEO-003, OPR-005 |
| T-7 | Reserve buoyancy (foam only) | Hull floats at ≤250 mm draft with 100 kg test load after simulated hull breach | SAF-003 |
| T-8 | Frame-to-hull (IF-01) bearing | No HDPE creep deformation >0.5 mm at washer after 72 h at 40 N·m | FOR-009 |
| T-9 | Supplier qualification | ≥1 Vietnamese HDPE fabricator confirmed capable of 4.0 m half-hull to D9 spec | PRD-002 |

---

## 2. Prototype Scope

### 2.1 Build Scope

One (1) complete M1 hull assembly per D9 Section 2 specification:

| Component | Specification | Qty | Notes |
|-----------|---------------|-----|-------|
| HDPE half-hull A | PE100, carbon-black UV-stabilized, 4.0 m semicircle, 500 mm depth, ≥8 mm wall | 1 | Hot-plate welded from HDPE sheet at supplier |
| HDPE half-hull B | Identical to A | 1 | Second half |
| Hull joint flanges (IF-07) | 60 mm wide × 20 mm thick integral HDPE lip, full diameter | Integral | Thermally welded onto each half-hull during fabrication |
| EPDM gasket | 40 mm × 5 mm, Shore A 60±5, continuous strip | 13 m | For full joint perimeter |
| Bolt set (IF-07) | 24× M10 SS316 hex bolt + flat washer + Nylock nut | 1 set | Spacing ~520 mm |
| Alignment dowels (IF-07) | 3× Ø12 mm nylon pins at 120° spacing | 1 set | Section-to-section alignment |
| Steel backing channel | C100×50×5 HDG steel, 2 pcs × ~4.0 m | 2 | Structural bridge inside joint |
| Sealant | Sikaflex 291, 5 mm continuous bead on exterior joint | 2 tubes | Secondary seal after bolt-up |
| PU rigid foam | Closed-cell, marine grade, 2-component pour-in-place | 250 kg | Enough for 80% fill at 40 kg/m³ |
| Scupper fittings | 8× Ø100 mm flush-mount HDPE | 8 | Self-draining deck |
| Deck non-skid | Textured paint, grey | 3 L | Optional for prototype |

**Not included in hull prototype (separate tests):**
- M2 structural frame (tested independently at steel fab shop — pad eye proof load)
- M3 masts, M4 reflectors, M5 units (tested per [[PROTO_reflector_rcs_validation.md]])
- M6 GPS, M7 mooring, M8 tow (COTS — no prototype validation needed)

### 2.2 Frame-to-Hull Simulation

To validate IF-01 without fabricating the full steel frame, a **representative test panel** will be used:

| Item | Description |
|------|-------------|
| Test panel | 500 × 500 × 8 mm S235 HDG plate with 4× M12 clearance holes on 300 mm spacing |
| HDPE test coupon | 500 × 500 × 12 mm PE100 sheet (simulates hull wall) |
| Fender washers | 4× 50×50×5 mm SS316 (per D9 Section 3.7) |
| Bolts | 4× M12×40 SS316 + Nylock nut |
| Purpose | Bolt to hull at IF-01 representative location, torque to 40 N·m, monitor HDPE creep over 72 h |

---

## 3. Prototype BOM and Budget

### 3.1 Bill of Materials

| # | Item | Qty | Unit Cost ($) | Extended ($) | Source |
|---|------|-----|---------------|-------------|--------|
| 3.1 | HDPE half-hull fabrication (2 sections, hot-plate welded, incl. flange lips) | 1 set | 3,200.00 | 3,200.00 | Local (Binh Minh Plastics or Tan Dai Hung) |
| 3.2 | EPDM gasket strip, 40×5 mm, 13 m | 1 lot | 104.00 | 104.00 | Local |
| 3.3 | SS316 M10 bolt + washer + Nylock nut set (24x) | 1 set | 48.00 | 48.00 | Local |
| 3.4 | Nylon alignment dowels, Ø12×30 mm (3x) | 1 set | 6.00 | 6.00 | Local |
| 3.5 | HDG steel backing channel, C100×50×5, 2×4.0 m | 2 pcs | 35.00 | 70.00 | Local |
| 3.6 | Sikaflex 291 marine sealant | 2 tubes | 18.00 | 36.00 | Import |
| 3.7 | PU rigid foam, 2-component, marine grade (40 kg/m³) | 250 kg | 4.00/kg | 1,000.00 | Local (Dong A Chemical) |
| 3.8 | Scupper drain fittings, Ø100 mm HDPE (8x) | 8 pcs | 6.00 | 48.00 | Local |
| 3.9 | Deck non-skid paint | 3 L | 25.00 | 75.00 | Import |
| 3.10 | IF-01 test panel (S235 HDG, 500×500×8 mm) | 1 pc | 25.00 | 25.00 | Local |
| 3.11 | IF-01 test coupon (PE100 HDPE, 500×500×12 mm) | 1 pc | 15.00 | 15.00 | Local |
| 3.12 | SS316 M12 bolt + fender washer + Nylock set (4x) | 1 set | 12.00 | 12.00 | Local |
| 3.13 | HDPE weld test coupons (6× 300×50×12 mm welded strips) | 6 pcs | 15.00 | 90.00 | Bundled with hull fabrication |
| 3.14 | Foam test coupons (extraction from pour batch) | 6 pcs | — | — | Cut from surplus foam |
| 3.15 | ASTM D2842 water absorption test (outsource to materials lab) | 3 samples | 50.00 | 150.00 | Lab (HCMC) |
| 3.16 | HDPE weld tensile testing (outsource, 6 specimens) | 6 tests | 35.00 | 210.00 | Lab (HCMC) |
| 3.17 | Transport — hull sections to assembly/test facility | 1 trip | 300.00 | 300.00 | Local freight |
| 3.18 | Test facility access — harbor or dock with crane, 5 days | 5 days | 150.00/day | 750.00 | Local harbor |
| | **TOTAL PROTOTYPE BOM** | | | **$6,139.00** | |

### 3.2 Labor

| Task | Hours | Rate ($/hr) | Cost ($) |
|------|-------|-------------|----------|
| Hull supplier liaison, spec review, FAI coordination | 8 | 30 | 240 |
| Hull section joining (IF-07 assembly) | 6 | 30 | 180 |
| PU foam fill (pour + cure monitoring) | 4 | 30 | 120 |
| Hull finishing (drill, trim, scuppers, markings) | 8 | 25 | 200 |
| IF-01 creep test setup + monitoring | 8 | 30 | 240 |
| Hydrostatic test (launch, ballast, 72 h monitoring) | 12 | 30 | 360 |
| Foam buoyancy test (simulated breach) | 4 | 30 | 120 |
| Weld specimen preparation + lab coordination | 4 | 25 | 100 |
| Data analysis, report writing | 16 | 40 | 640 |
| **TOTAL LABOR** | **70** | | **$2,200** |

### 3.3 Budget Summary

| Category | Cost ($) |
|----------|----------|
| Materials + fabrication | 6,139 |
| Labor | 2,200 |
| Contingency (10%) | 834 |
| **TOTAL** | **$9,173** |

**Context:** $9,173 = 9.2% of Phase 3 budget ($100K). Combined with reflector prototype ($8,791), total prototype spend = $17,964 (18.0% of Phase 3 budget).

---

## 4. Supplier Qualification

### 4.1 Candidate Suppliers

| Supplier | Location | Capability | Status |
|----------|----------|------------|--------|
| **Binh Minh Plastics (BMP)** | HCMC | HDPE pipe/sheet extrusion, hot-plate welding, ISO 9001. Largest HDPE processor in Vietnam. 4.0 m sections within capacity (pipe OD up to 2,000 mm standard; flat panel welding adaptable). | **PRIMARY — Request quotation** |
| **Tan Dai Hung** | HCMC | HDPE tank and liner fabrication. Experience with large-format HDPE welding for water treatment tanks (up to 5 m diameter). | **BACKUP 1** |
| **Tien Phong Plastics** | Hai Phong | HDPE pipe manufacturer, rotomolding capability (smaller diameters). May have hot-plate capacity for 4 m sections. Northern location preferred for Hai Phong assembly. | **BACKUP 2** |

### 4.2 Supplier Qualification Criteria

| # | Criterion | Requirement | Verification |
|---|-----------|-------------|-------------|
| SQ-1 | HDPE PE100 processing experience | ≥3 years processing PE100 grade, MFI ≤0.4 g/10 min | Review supplier portfolio, material certificates |
| SQ-2 | Hot-plate welding capability | Platen ≥600 mm, PE butt-weld per DVS 2207-1, weld bead control | Witness welding demonstration on 12 mm PE100 sheet |
| SQ-3 | Dimensional capability | 4.0 m semicircle, ±5 mm on major dimensions, wall ≥8 mm (±1 mm) | First Article Inspection (FAI) with UT thickness gauge |
| SQ-4 | Quality system | ISO 9001 or equivalent documented process control | Audit or certificate review |
| SQ-5 | Capacity | ≥2 hulls/month once validated | Confirm equipment availability, scheduling |
| SQ-6 | Weld test specimens | Supplier provides 6× welded test coupons from same material/process as hull | Include in PO specification |

### 4.3 Supplier Selection Process

1. Issue RFQ to all 3 candidates with D9 Section 2 drawing package + weld test coupon requirement
2. Evaluate quotations on price, lead time, weld coupon commitment, ISO certification
3. Award to lowest-qualified bidder; backup supplier receives sample order for 1 half-hull only
4. FAI on first half-hull before accepting second half

---

## 5. Fabrication Specification (for Supplier PO)

### 5.1 Hull Half-Section Requirements

| Parameter | Specification | Tolerance | Verification |
|-----------|---------------|-----------|-------------|
| Material | HDPE PE100, carbon-black UV-stabilized, per ASTM D3350 Cell Class 345464C | MFI ≤0.4 g/10 min; density 940–960 kg/m³ | Material certificate from resin supplier |
| Shape | Semicircular ring pontoon, 4,000±5 mm along diameter chord, 500±50 mm depth | See D9 Section 2.1 | Tape measure, templates |
| Ring width | 500±30 mm (cross-section of pontoon) | D9 Section 2.1 | Tape measure at 8 points |
| Wall thickness | ≥8 mm minimum (target 10–12 mm) | +0/−0 minimum | UT thickness gauge at 8 sampling points per half |
| Joint flange | 60±5 mm wide × 20±2 mm thick, integral HDPE lip, full diameter face | Thermally welded to hull wall or machined from solid | Calipers, visual |
| Bolt holes | 12× Ø11 mm clearance holes at ~520 mm spacing along flange | Position ±3 mm | Template check |
| Dowel holes | 1.5× Ø12.5 mm holes at specified positions (60°/180°/300° from chord end) | Position ±1 mm | Gauge pin check |
| Scupper holes | 4× Ø100 mm at hull inner edge, equally spaced | Position ±20 mm | Tape measure |
| Mass | 100±15 kg per half-section (shell only, no foam) | Weigh on calibrated scale | Floor scale |
| Weld quality | All hot-plate butt welds to DVS 2207-1; weld bead trimmed flush ±2 mm | No voids, no cold joints, no charring | Visual 100%; bend test on 3 coupons |

### 5.2 Weld Test Coupons

The supplier shall fabricate 6× weld test coupons from the same PE100 sheet stock and welding parameters as the hull sections:

| Coupon | Size | Weld Type | Test |
|--------|------|-----------|------|
| W-1, W-2, W-3 | 300×50×12 mm, weld at center | Hot-plate butt weld (same parameters as hull seams) | Tensile test per ASTM D638 (Type IV specimen cut from weld zone) |
| W-4, W-5 | 300×50×12 mm, weld at center | Same | Guided bend test per DVS 2203-2 (face bend + root bend) |
| W-6 | 300×50×12 mm, weld at center | Same | Reserve specimen |

**Accept/Reject:**
- Tensile: σ_uts ≥ 17.6 MPa (80% of PE100 parent: 22 MPa). Failure must be in parent material, not weld.
- Bend: No cracks on 4t radius bend (face and root). Weld zone must not separate.

---

## 6. Assembly Procedure

### 6.1 Hull Section Joining (IF-07)

| Step | Action | Detail | Hold Point? |
|------|--------|--------|-------------|
| J-1 | Receive and inspect 2 half-hulls | Incoming inspection per Section 5.1: wall thickness (UT at 8 points per half), dimensions, flange geometry, mass, surface quality. Review weld coupons. | **YES** — accept/reject before proceeding |
| J-2 | Position half-hulls on flat assembly floor | Align on level surface (flatness ≤10 mm over 4 m). Support with cradles at quarter points. Flanges face-to-face, joint plane vertical or horizontal (horizontal preferred for gasket seating). | No |
| J-3 | Dry-fit alignment | Mate flanges without gasket. Insert 3× Ø12 nylon dowel pins. Check outer diameter match across joint: step ≤3 mm per D9 Section 2.3. Adjust cradle shims if needed. | No |
| J-4 | Install EPDM gasket | Lay EPDM strip (40×5 mm) in continuous loop on one flange face. Join gasket ends with vulcanizing adhesive (overlap 50 mm). Verify gasket sits flat, no twists or gaps. | No |
| J-5 | Mate halves | Re-insert dowel pins through gasket holes. Bring flanges together. Gasket compressed uniformly. | No |
| J-6 | Bolt-up (stage 1: snug) | Install 24× M10 SS316 bolts through flange clearance holes. Finger-tight all bolts. | No |
| J-7 | Bolt-up (stage 2: torque to 15 N·m) | Torque all 24 bolts to 15 N·m in star pattern (opposing bolt pairs). Verify gasket compression uniform around perimeter. | No |
| J-8 | Bolt-up (stage 3: final torque 25±3 N·m) | Final torque all 24 bolts to 25 N·m in same star pattern. Measure gasket compression: target 3.5–4.0 mm compressed thickness (30% of 5 mm). Record all 24 bolt torques. | **RECORD** — torque values logged for T-3 re-check |
| J-9 | Install steel backing channels | Position 2× C100×50×5 HDG channel sections inside hull, spanning joint line. Bolt through hull wall with 6× M10 through-bolts per channel side (12 bolts total). Torque to 25 N·m. | No |
| J-10 | Apply external sealant | Apply continuous 5 mm bead of Sikaflex 291 along exterior joint line. Tool smooth. Allow 24 h cure. | No |
| J-11 | Mark bolt torque witness marks | Paint witness marks (torque stripe) across bolt head and flange on all 24 bolts for visual torque-loss monitoring. | No |

### 6.2 Foam Fill

| Step | Action | Detail | Hold Point? |
|------|--------|--------|-------------|
| F-1 | Prepare fill ports | Drill 2× Ø50 mm fill ports per hull section (4 total), positioned at top of ring section at 90° intervals. | No |
| F-2 | Mix PU foam components | Mix A+B components per manufacturer instructions. Target density: 40 kg/m³. Pour test coupon first (150×150×50 mm mold) for density verification. | No |
| F-3 | Pour foam — section 1 | Pour mixed foam through 2 fill ports into half-hull A. Monitor expansion visually. Fill to ~80% of internal volume (leave 20% void for drainage/inspection). | No |
| F-4 | Pour foam — section 2 | Repeat for half-hull B. | No |
| F-5 | Cure | Allow 24 h cure at ≥20°C ambient. Do not move hull during cure. | No |
| F-6 | Inspect foam fill | Tap test entire hull surface with rubber mallet. Map voids >200 mm diameter. Accept if ≤2 voids total and none at waterline zone (bottom 100 mm). | **YES** — reject if excessive voids |
| F-7 | Measure foam density | Cut 3× foam sample coupons (50×50×50 mm) from accessible void areas or from pour-batch test coupon. Weigh and measure. Calculate density. | **RECORD** — density must be 32–48 kg/m³ |
| F-8 | Seal fill ports | Plug fill ports with HDPE caps, hot-air welded or bolted with gasket. | No |

---

## 7. Test Plan

### 7.1 Test T-1: HDPE Weld Tensile Strength

| Parameter | Value |
|-----------|-------|
| Standard | ASTM D638 Type IV (modified: weld at specimen center) |
| Specimens | 3× from supplier weld coupons (W-1, W-2, W-3) |
| Equipment | Universal testing machine (UTM), 50 kN capacity (outsource to HCMC materials lab) |
| Crosshead speed | 50 mm/min per ASTM D638 |
| Measurement | Ultimate tensile strength (σ_uts), elongation at break, failure location (parent vs weld) |

**Pass/Fail:**
| Criterion | PASS | MARGINAL | FAIL |
|-----------|------|----------|------|
| σ_uts | ≥17.6 MPa (80% of parent 22 MPa) | 15.4–17.5 MPa (70–79%) | <15.4 MPa (<70%) |
| Failure location | Parent material | HAZ (heat-affected zone) | Weld centerline |
| Elongation | ≥300% | 200–299% | <200% |

### 7.2 Test T-2: IF-07 Joint Watertightness

| Parameter | Value |
|-----------|-------|
| Method | Immersion test — float assembled hull in harbor/test tank for 72 h continuous |
| Setup | Launch hull (no foam option: weight ballast to 200 mm draft; with foam: natural draft ~10 mm for empty hull). Mark waterline. |
| Inspection | Visual inspection of interior joint line at 1, 4, 8, 24, 48, 72 h. Look for drips, weeping, damp gasket, water stains. |
| Supplementary | After 72 h, remove hull from water. Unbolt 2 adjacent bolts at lowest joint point. Inspect gasket for swelling, deformation, permanent set. |
| Conditions | Ambient temperature ≥15°C. If harbor test: note wave height and tidal range for context. |

**Pass/Fail:**
| Criterion | PASS | MARGINAL | FAIL |
|-----------|------|----------|------|
| Leak at 72 h | Zero leaks | Minor weeping at ≤2 bolt holes (gasket adjustment resolves) | Continuous drip or flow at any location |
| Gasket condition | No permanent set >10% | Set 10–20% (acceptable with re-torque) | Set >20% or material failure |

### 7.3 Test T-3: IF-07 Bolt Torque Retention

| Parameter | Value |
|-----------|-------|
| Method | Breakaway torque measurement on all 24 bolts after 72 h immersion (during T-2) |
| Procedure | After completing T-2, use click torque wrench set to 20 N·m (80% of 25 N·m install torque). Attempt to tighten each bolt — if wrench clicks (bolt already above 20 N·m), PASS. If bolt turns before click, record breakaway torque. |
| Context | HDPE creep under bolt clamping load causes torque relaxation over time. PE100 at 20°C has a 50-year creep modulus of ~300 MPa (vs 900 MPa short-term). At 72 h, expect 10–20% relaxation per published PE creep data. |

**Pass/Fail:**
| Criterion | PASS | MARGINAL | FAIL |
|-----------|------|----------|------|
| Breakaway torque (avg) | ≥20.0 N·m (≥80% of 25 N·m) | 17.5–19.9 N·m (70–79%) | <17.5 N·m (<70%) |
| Any single bolt | ≥17.5 N·m | 15.0–17.4 N·m | <15.0 N·m |

**If MARGINAL:** Acceptable with re-torque procedure added to deployment SOP (re-torque all IF-07 bolts to 25 N·m before each deployment). This is standard practice for HDPE bolted joints.

### 7.4 Test T-4: Foam Fill Density and Coverage

| Parameter | Value |
|-----------|-------|
| Density | 3× coupon measurements from pour batch (Section 6.2, Step F-7) |
| Coverage | Tap test per Section 6.2, Step F-6: entire hull surface, map voids |
| Volume fill factor | Calculate from (hull mass with foam − hull mass without foam) / (internal volume × target density). Target ≥80%. |

**Pass/Fail:**
| Criterion | PASS | MARGINAL | FAIL |
|-----------|------|----------|------|
| Foam density | 32–48 kg/m³ | 28–31 or 49–55 kg/m³ | <28 or >55 kg/m³ |
| Fill factor | ≥80% | 70–79% | <70% |
| Voids | ≤2 voids >200 mm, none at waterline | 3–4 voids, none at waterline | >4 voids OR any void at waterline |

### 7.5 Test T-5: Foam Water Absorption (ASTM D2842)

| Parameter | Value |
|-----------|-------|
| Standard | ASTM D2842 — Water Absorption of Rigid Cellular Plastics |
| Specimens | 3× 50×50×25 mm coupons cut from pour-batch test block |
| Procedure | Weigh dry. Immerse in distilled water at 23°C for 48 h. Remove, blot surface, re-weigh within 1 min. Calculate % volume absorption. |
| Lab | Outsource to HCMC polymer testing lab |

**Pass/Fail:**
| Criterion | PASS | FAIL |
|-----------|------|------|
| Water absorption | ≤3.0% by volume | >3.0% by volume |

**Note:** If FAIL, the foam supplier or grade must be changed. Water absorption >3% compromises reserve buoyancy over the hull service life as foam slowly waterloggs.

### 7.6 Test T-6: Hydrostatic Stability

| Parameter | Value |
|-----------|-------|
| Method | Float assembled hull (with foam, no frame/masts) in calm water. Add calibrated ballast to simulate full system mass (986 kg − hull mass). Measure draft, freeboard, heel response. |
| Setup | Launch foam-filled hull in harbor. Hull mass (shell + foam): ~350 kg. Required ballast: 986 − 350 = 636 kg (sandbags or water drums, distributed per D8 KG estimate). |
| Measurements | (a) Draft at 4 points (fore/aft/port/starboard) with ruler from waterline to keel. (b) Freeboard at 4 points. (c) Heel test: shift 50 kg ballast 2.0 m off-center; measure heel angle with inclinometer. (d) Deck drainage: pour 50 L water on deck; time to drain through scuppers. |

**Pass/Fail:**
| Criterion | PASS | MARGINAL | FAIL |
|-----------|------|----------|------|
| Draft at 986 kg | ≤25 mm | 25–35 mm | >35 mm |
| Freeboard | ≥450 mm | 400–449 mm | <400 mm |
| Heel from 50 kg shift | <0.5° | 0.5–1.0° | >1.0° |
| Deck drainage (50 L) | <60 s | 60–120 s | >120 s or pooling |

**Expected results (from D8 Section 5.1):**
- Draft = 19.1 mm at 986 kg → PASS expected
- Freeboard = 481 mm → PASS expected
- GM = 207.9 m → heel from 50 kg at 2.0 m is arctan(50×9.81×2.0 / (986×9.81×207.9)) = arctan(981 / 2,010,400) = 0.03° → PASS by large margin

### 7.7 Test T-7: Reserve Buoyancy (Simulated Hull Breach)

| Parameter | Value |
|-----------|-------|
| Purpose | Verify hull is unsinkable (foam alone provides sufficient buoyancy) per D8 Section 5.4 |
| Method | After completing T-6, drill 4× Ø25 mm holes through hull bottom (below waterline) at 90° spacing. Allow 1 hour for water to fill void spaces within hull. Measure change in draft. Add 100 kg ballast atop hull (simulates partial equipment loading on a breached hull). Measure final draft. |
| Expected behavior | Water fills the 20% void space (~0.76 m³). Additional submergence: Δdraft = 0.76 m³ / 50.27 m² = 0.015 m = 15 mm. Total draft: ~34 mm. With 100 kg added: +2 mm. Total: ~36 mm. Hull remains afloat with >400 mm freeboard. |

**Pass/Fail:**
| Criterion | PASS | FAIL |
|-----------|------|------|
| Hull floats after breach | Stable float, draft ≤250 mm | Sinks, capsizes, or draft >250 mm |
| Foam integrity | Foam does not absorb visible water (cut open small section to verify after test) | Foam waterlogged |

**Note:** This is a destructive test for the hull. Conduct as the final test. The prototype hull is not reusable after breach holes are drilled.

### 7.8 Test T-8: IF-01 Frame-to-Hull Bearing (HDPE Creep)

| Parameter | Value |
|-----------|-------|
| Method | Bolt IF-01 test panel (Section 2.2) to hull at a representative location. Torque 4× M12 bolts to 40±3 N·m through fender washers (50×50×5 mm SS316). Measure washer impression depth in HDPE at 0, 1, 4, 8, 24, 48, 72 h using depth micrometer. |
| Purpose | Quantify HDPE compressive creep under sustained bolt clamping load. Determine if fender washer area (2,500 mm² per bolt) is sufficient to limit long-term creep. |
| Expected | PE100 creep at 40 N·m: bolt load ≈ 25 kN / 4 bolts = 6.25 kN per bolt. Bearing stress = 6,250 / 2,500 = 2.5 MPa. PE100 short-term compressive strength = 25 MPa. Utilization = 10%. At 10% utilization, expect <0.1 mm creep at 72 h per published PE100 data. |

**Pass/Fail:**
| Criterion | PASS | MARGINAL | FAIL |
|-----------|------|----------|------|
| Creep at 72 h | ≤0.3 mm | 0.3–0.5 mm | >0.5 mm |
| Bolt torque retention (re-check at 72 h) | ≥32 N·m (80% of 40) | 28–31.9 N·m (70–79%) | <28 N·m |

---

## 8. Schedule

### 8.1 Timeline (10 Weeks Total)

```
HULL PROTOTYPE SCHEDULE
Week:   1    2    3    4    5    6    7    8    9    10
════════════════════════════════════════════════════════════

PROCUREMENT
  Issue RFQ to 3 suppliers
  ├─RFQ─┤
  Evaluate quotes, award PO
       ├─EVAL─┤
  Supplier fabrication (2 half-hulls + weld coupons)
            ├───── FABRICATE (3-4 weeks) ─────┤

MATERIALS (parallel with fabrication)
  EPDM, bolts, foam, sealant, backing channel
  ├─ORDER─┤├──DELIVER──┤

ASSEMBLY
  Receive + inspect hulls (FAI)
                                    ├─FAI─┤
  Join sections (IF-07)
                                         ├─JOIN─┤
  Foam fill + 24h cure
                                              ├─FOAM + CURE─┤
  Finish (drill, scuppers, non-skid)
                                                        ├FINISH┤

TESTING
  Weld tensile test (lab, on coupons received Wk 5)
                                    ├─LAB─┤
  IF-01 creep panel install + 72h monitor
                                                     ├──72h──┤
  Hydrostatic test (launch, ballast, 72h float)
                                                     ├──72h FLOAT──┤
  Reserve buoyancy test (destructive, after float)
                                                              ├─BREACH─┤
  Data analysis + report
                                                                  ├─REPORT─┤

DELIVERY
  Prototype validation report                                         ▼ Wk 10
════════════════════════════════════════════════════════════════════════════════
```

### 8.2 Critical Path

**Supplier fabrication (Weeks 3–6)** is the critical path. HDPE hot-plate welding of 4.0 m half-hulls requires 3–4 weeks at the supplier including:
- Material procurement (PE100 sheet stock)
- Cutting and forming semicircular hull sections
- Hot-plate butt welding of panel seams
- Welding integral flange lips
- Drilling bolt holes and scupper holes
- Fabrication of 6 weld test coupons

### 8.3 Parallel Activities

| Activity | Runs in Parallel With |
|----------|-----------------------|
| Material procurement (foam, gaskets, bolts) | Supplier hull fabrication |
| Weld tensile testing (lab) | Hull assembly (coupons arrive with hull) |
| IF-01 creep test | Hydrostatic 72 h float test |
| Foam water absorption (lab) | Hydrostatic test |

---

## 9. Risk and Contingency

### 9.1 Risk Register

| # | Risk | Probability | Impact | Mitigation |
|---|------|------------|--------|------------|
| R-1 | Vietnamese HDPE supplier cannot fabricate 4.0 m semicircular hull section to spec | LOW-MEDIUM | HIGH — blocks production | 3 candidate suppliers identified. If all fail: (a) reduce to 3× 120° segments bolted (3-section hull), or (b) import from Thai HDPE fabricator. |
| R-2 | HDPE weld tensile strength <80% of parent | LOW | HIGH — structural concern | DVS 2207-1 welding standard is well-established for PE100. If fail: (a) adjust welding parameters (temperature, pressure, dwell time); (b) switch to extrusion welding with manual bead; (c) add external HDPE weld strips for reinforcement. |
| R-3 | IF-07 joint leaks during 72 h immersion | MEDIUM | MEDIUM — design iteration | Contingency: (a) increase bolt count from 24 to 30; (b) widen gasket from 40 to 60 mm; (c) add second gasket inboard of first; (d) apply Sikaflex 291 on both exterior AND interior faces of joint. |
| R-4 | Foam density out of range | LOW | LOW — adjust pour recipe | Foam supplier provides technical support for mix ratio adjustment. Pour test coupon before filling hull. |
| R-5 | Foam water absorption >3% | LOW | HIGH — undermines unsinkability | Change foam grade: specify closed-cell PU with skin integral (BASF Elastopor or equivalent marine-rated grade). ASTM D2842 <1% grades are commercially available. |
| R-6 | HDPE creep >0.5 mm at IF-01 bolt locations | LOW | MEDIUM — requires larger washers | Increase fender washer to 60×60×6 mm (area +44%) or add HDPE load-distribution plate (100×100×6 mm) under each bolt group. Reduces bearing stress proportionally. |
| R-7 | Harbor access unavailable for float test | LOW | MEDIUM — schedule delay | Alternative: inflate hull with foam, test in large temporary pool or pond. Or transport to nearest riverfront quay. |

### 9.2 Go/No-Go Decision Matrix

| Scenario | Tests Passed | Decision |
|----------|-------------|----------|
| All 9 tests PASS | T-1 through T-9 | **GO** — Proceed to production lot of 10 units with same supplier and process |
| T-1 MARGINAL + all others PASS | Weld 70–79% of parent | **CONDITIONAL GO** — Proceed with enhanced weld QC (100% bend test on every hull seam); add reinforcing weld strips at hull midspan |
| T-2 or T-3 MARGINAL | Minor leak or 70–79% torque retention | **CONDITIONAL GO** — Add re-torque procedure to deployment SOP; increase bolt count to 30 |
| Any CRITICAL test FAIL | T-1 FAIL (weld <70%) or T-5 FAIL (foam >3%) or T-7 FAIL (hull sinks) | **NO-GO** — Root cause analysis required. Do not proceed to production. Redesign, retest. |
| T-9 FAIL (no supplier qualified) | All 3 suppliers fail SQ criteria | **NO-GO** — Expand supplier search to Thailand/China HDPE fabricators. Consider rotomolding (Option A) if welding cannot be qualified. |

---

## 10. Deliverables

| # | Deliverable | Format | Contents |
|---|-------------|--------|----------|
| 10.1 | Supplier qualification report | PDF | RFQ evaluation, supplier audit notes, FAI results, capability confirmation |
| 10.2 | Hull FAI report | PDF | Incoming inspection data: wall thickness (16 UT measurements), dimensions, flange geometry, mass |
| 10.3 | Weld tensile test report | PDF (lab) | 3× tensile curves, σ_uts values, failure location photographs, PASS/FAIL determination |
| 10.4 | Weld bend test report | PDF (lab) | 2× bend test results, crack/no-crack determination |
| 10.5 | IF-07 assembly record | PDF | 24× bolt torque values, gasket compression measurements, photograph of completed joint |
| 10.6 | Foam fill record | PDF | Density measurements (3 coupons), tap test void map, fill factor calculation |
| 10.7 | Foam water absorption report | PDF (lab) | 3× ASTM D2842 results, PASS/FAIL |
| 10.8 | Hydrostatic test report | PDF | Draft/freeboard measurements at 0–72 h, heel test data, deck drainage time, photographs |
| 10.9 | Reserve buoyancy test report | PDF | Pre/post breach draft, foam condition after breach, photographs |
| 10.10 | IF-01 creep test report | PDF | Washer impression depth at 0–72 h (time series plot), bolt torque retention, PASS/FAIL |
| 10.11 | Hull prototype validation summary | PDF | Consolidated PASS/MARGINAL/FAIL for all 9 objectives, Go/No-Go recommendation, lessons learned |

---

## 11. Cross-References

### Phase 3 Source Documents
- [[PRAD_D8_design_structure.md]] — Hull stability (Section 5.1), wave slamming (5.2), joint analysis (5.3), reserve buoyancy (5.4)
- [[DECS_D9_detail_specification.md]] — Hull specs (Section 2.1–2.3), tolerances, materials
- [[DECS_E10_variant_evaluation.md]] — Decision 1: 2-section bolted hull selected at 85.0%
- [[OCP_C14_cost_analysis.md]] — M1 hull BOM: $4,118
- [[OCP_P15_production_planning.md]] — Hull manufacturing (Section 1.2), suppliers (Section 2.1), QC (Section 4)
- [[OCP_O13_design_optimization.md]] — Weight optimization W-1 (foam density), W-5 (fastener reduction)

### Companion Prototype Document
- [[PROTO_reflector_rcs_validation.md]] — AM reflector prototype build & RCS validation plan ($8.8K, 7 weeks)

### Phase 1 Requirements Traced
- HUL-001 through HUL-008: Hull structural and buoyancy requirements
- OPR-002: 72 h anchored survival at SS 5-6
- SAF-003: Unsinkable design (foam buoyancy ≥2× displacement)
- TRA-002: Transport width ≤2.5 m per section
- GEO-001, GEO-003: Platform dimensions and freeboard
- FOR-008, FOR-009: Structural joint and frame-to-hull integrity
- PRD-002: Local content ≥60%

---

*End of Hull Platform Prototype Validation Plan. Budget: $9,173 (9.2% of Phase 3). Schedule: 10 weeks. Critical path: HDPE supplier fabrication (Weeks 3–6). 9 test objectives with quantified PASS/MARGINAL/FAIL criteria. Go/No-Go decision gates defined.*
