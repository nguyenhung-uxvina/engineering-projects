---
project: VN-TGT-SEA-001
phase: 4
type: detail_design
document: "First Article Build Plan"
version: 1.0
created: 2026-02-11
status: draft
serial: TRI-H-001
methodology: "AS9102-adapted First Article Inspection (FAI)"
---

# First Article Build Plan — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Serial Number:** TRI-H-001 (First Article Unit)
**Purpose:** Provide a complete, production-ready build plan for the first article unit, integrating the factory assembly sequence (F01-F22) from [[OCP_P15_production_planning.md]] with First Article Inspection (FAI) measurement points from [[DECS_D9_detail_specification.md]] and standards-driven tests (T-01 through T-07) from [[DECS_S12_standards_compliance.md]]. This document governs all activities from raw material receiving through final acceptance and release of serial TRI-H-001.
**Scope:** Raw material receiving, incoming inspection, factory assembly, in-process verification, First Article Inspection (21 FAI checks), integrated test program (7 tests), non-conformance handling, documentation, and release.
**Methodology:** AS9102 First Article Inspection adapted for defense prototype manufacturing in Vietnamese context.

---

## 1. Purpose & Scope

### 1.1 Purpose

This First Article Build Plan serves as the master work instruction for manufacturing, inspecting, testing, and releasing the first production unit (TRI-H-001) of the THANH TRI-H fixed sea target. The first article build differs from subsequent production units in the following ways:

1. **100% dimensional inspection** on all components (FAI-01 through FAI-21 per [[DECS_D9_detail_specification.md]] Section 13.1)
2. **Full test integration** with all 7 standards-driven tests (T-01 through T-07 per [[DECS_S12_standards_compliance.md]] Section 6)
3. **Process validation** -- first-time verification that supplier capabilities, assembly procedures, and QC methods produce conforming hardware
4. **Baseline documentation** -- creation of the as-built data package that defines acceptance criteria for all subsequent units

### 1.2 Scope

| Aspect | Coverage |
|--------|----------|
| Hardware | 1 complete THANH TRI-H target system (M1 through M8, ~344 fasteners, 8 modules, 7 interfaces) |
| Inspection | 21 FAI measurement points (100% first article) |
| Testing | 7 standards-driven tests: T-01 salt fog, T-02 mooring proof load, T-03 RCS 360 deg, T-04 GPS endurance, T-05 sea trial 72h, T-06 deployment exercise, T-07 AM qualification |
| Documentation | Complete as-built data package: material certs, inspection records, test data, non-conformance reports |
| Acceptance | Release gate requiring all 21 FAI checks PASS + 7 tests PASS |

### 1.3 Applicable Documents

| Document | Reference | Content |
|----------|-----------|---------|
| [[PRAD_A7_architecture_definition.md]] | 8 modules (M1-M8), 7 interfaces (IF-01 to IF-07) | System architecture |
| [[DECS_D9_detail_specification.md]] | 4-tier tolerance, 21 FAI checks, 344 fasteners | Engineering specification |
| [[DECS_S12_standards_compliance.md]] | 26 standards, 7 tests, $28,000 test program | Standards compliance |
| [[DECS_C11_requirements_verification.md]] | 116 requirements, 72 verified, 34 pending-test | Verification status |
| [[OCP_C14_cost_analysis.md]] | BOM $17,862, labor $2,726, unit cost $29,655 @10 | Cost baseline |
| [[OCP_P15_production_planning.md]] | Assembly sequence F01-F22, 52 hrs active labor | Production plan |
| [[PROTO_reflector_rcs_validation.md]] | Reflector prototype, RCS validation plan | AM risk reduction |
| [[PROTO_hull_platform_validation.md]] | Hull prototype, weld/foam/stability validation | Hull risk reduction |

---

## 2. Prerequisites & Entry Criteria

### 2.1 Design Maturity Gates

The following must be complete before first article build commences:

| # | Prerequisite | Evidence | Status |
|---|-------------|----------|--------|
| PRE-01 | Phase 3 gate review passed | Gate checklist signed by stakeholders | REQUIRED |
| PRE-02 | All TBD items resolved or dispositioned | TBD-005 (AM supplier qualification), TBD-007 (hull fab method), TBD-008 (transport width) | REQUIRED |
| PRE-03 | Prototype validation complete | [[PROTO_reflector_rcs_validation.md]] and [[PROTO_hull_platform_validation.md]] results reviewed, lessons incorporated | REQUIRED |
| PRE-04 | AM supplier(s) qualified per ASTM F3301 | First article frames from >=2 bureaus inspected, tensile coupons pass (sigma_y >=230 MPa, El >=5%) | REQUIRED |
| PRE-05 | CNC shop qualified for face plates | >=3 sample plates verified: flatness <0.1 mm, Ra <=6.3 um | REQUIRED |
| PRE-06 | HDPE hull supplier qualified | 1 prototype hull section verified per [[PROTO_hull_platform_validation.md]] | REQUIRED |
| PRE-07 | Production drawings released | All module drawings issued at Rev A minimum | REQUIRED |
| PRE-08 | Tooling procured and verified | Welding jigs ($3,000), CNC vacuum fixture ($2,000), reflector alignment jig ($2,500), CMM fixture ($1,000) | REQUIRED |

### 2.2 Material Availability

All BOM items per [[OCP_C14_cost_analysis.md]] must be on-hand or confirmed delivery before build start:

| Material Group | Items | Lead Time | Source | Verification |
|---------------|-------|-----------|--------|--------------|
| HDPE hull shell (2 sections) | 1.1.01 | 3-5 weeks | Binh Minh Plastics / Tan Dai Hung (VN) | Supplier capability confirmed per PRE-06 |
| PU rigid foam (250 kg) | 1.1.02 | 1-2 weeks | Dong A Chemical (VN) | Material certificate, density test coupon |
| S235 steel frame + masts (galvanized) | 1.2.01-1.2.19, 1.3.01-1.3.08 | 2-3 weeks fab + 3-5 days HDG | Truong Hai Mechanical + Vinh Thanh HDG (VN) | Weld procedure qualification (WPS/PQR) |
| 6061-T6 Al sheet + CNC face plates (24x) | 1.4.02, 1.4.04 | 3-4 weeks import + 1-2 weeks CNC | Korea import + Hai Phong CNC (VN) | Mill cert per ASTM B209 |
| AlSi10Mg AM frames (8x) | 1.4.01, 1.4.03 | 2-3 weeks | Xometry Asia / Facfox (ASEAN) | Build report, CoA, CT scan (3 frames) |
| SS316 fasteners (all sizes) | Multiple items | 1-2 weeks | Bulong Viet (VN) | Cert per grade/standard |
| GPS/Iridium module + battery | 1.6.01-1.6.15 | 4-6 weeks | Import (Taiwan/US) | Manufacturer data sheet |
| Mooring kit (anchor, chain, rode) | 1.7.01-1.7.11 | 2-3 weeks | Vietnam Marine Equipment (VN) | Chain test cert per EN 818-3 |
| Dyneema tow bridle (pre-spliced) | 1.8.01-1.8.07 | 4-6 weeks | Marlow Ropes (import) | Rope cert, SWL >=8,000 kgf |

### 2.3 Personnel & Equipment

| Resource | Requirement | Availability |
|----------|-------------|-------------|
| Assembly technicians | 2 qualified, trained on reflector alignment | Must complete training module before F12 |
| QC inspector | 1 certified, CMM-capable or trained on digital angle gauge | Available in-house or contract |
| Welder (steel fab shop) | AWS D1.1 qualified, 3G minimum | Supplier responsibility; verify qualification records |
| Test engineers | 2 for RCS measurement, 1 for GPS endurance | Available in-house |
| Floor scale / crane scale | 2,000 kg rated, calibrated | Verify calibration cert current |
| Torque wrenches | 3 ranges: 1-20 N-m, 10-100 N-m, 50-200 N-m | Calibrate before build start |
| Digital angle gauge | Wixey WR300 Type 2 or CMM (resolution 0.05 deg) | Available or procure ($200) |
| UT flaw detector | Olympus Epoch 650 or equivalent | Available or rent |
| Surface roughness tester | Mitutoyo SJ-210 or equivalent | Available or rent |
| Coating thickness gauge | Elcometer 456 or Fischer Dualscope | Available or rent |

---

## 3. Build Sequence (Integrated Chronological Plan)

This section merges the factory assembly sequence F01-F22 from [[OCP_P15_production_planning.md]] with FAI measurement points from [[DECS_D9_detail_specification.md]] Section 13.1. Steps marked with [FAI-XX] require first article measurements. Steps marked [QC HOLD] require sign-off before proceeding.

### 3.1 Track A: Hull Fabrication (F01-F04)

| Step | Description | Duration | Personnel | FAI / QC | Accept Criteria |
|------|-------------|----------|-----------|----------|-----------------|
| **F01** | Receive and inspect hull shell (2 half-sections from HDPE fabricator) | 2.0 h | 2 (QC + handler) | **[FAI-01]** Hull OD at 4 positions; **[FAI-02]** Wall thickness UT at 8 positions | OD: 8,000 +/-100 mm; Wall: >=8 mm at all points |
| **F02** | Join hull sections (IF-07): align halves on flat floor, insert EPDM gasket, bolt 24x M10 SS in star pattern to 25 N-m, apply Sikaflex 291 exterior seal, install steel backing channel | 4.0 h | 3 (2 fitters + helper) | Record gasket compression, bolt torque log | Gasket compressed to 3.5-4.0 mm; torque 25 +/-3 N-m all bolts |
| **F03** | Fill hull with PU foam: mix and pour 2-component rigid PU foam through fill ports, allow 24h cure at >=20 deg C | 2.0 h pour + 24h cure | 2 (foam tech + helper) | **[FAI-03]** Cut sample coupon, weigh/measure for density; **[FAI-04]** 48h immersion test on coupon | Density: 32-48 kg/m3; Water absorption: <=3% by volume |
| **F04** | Trim and finish hull: trim flash, drill 84x M12 bolt holes for IF-01 (300 mm spacing), drill 8x M12 for IF-06 tow padeyes, install 8x scupper drains, apply markings | 4.0 h | 2 (fitter + helper) | Verify hole positions using template jig | Hole position: +/-2 mm from template |

### 3.2 Track B: Steel Frame & Masts (F05, F13)

| Step | Description | Duration | Personnel | FAI / QC | Accept Criteria |
|------|-------------|----------|-----------|----------|-----------------|
| **F05** | Receive and inspect steel frame (from fab shop, galvanized). Inspect welds, dimensions, socket positions, HDG thickness. | 3.0 h | 2 (QC + inspector) | **[FAI-05]** Frame dimensions: socket radius, angular spacing; **[FAI-06]** HDG thickness at 10 points; **[FAI-07]** Pad eye weld UT per AWS D1.1 | Sockets: R=3,200 +/-5 mm, 45 deg +/-0.5 deg; HDG: >=85 um avg, >=70 um min; UT: no defects >3 mm |
| | | | | **[QC HOLD]** -- critical weld inspection sign-off required | |
| **F13** | Receive and inspect masts (8x from fab shop, galvanized). Inspect straightness, perpendicularity, pin hole position, HDG thickness. | 1.5 h | 1 (QC) | **[FAI-09]** Mast straightness; **[FAI-10]** Top plate flatness; **[FAI-11]** Top plate perpendicularity; **[FAI-06]** HDG on masts | Straightness: <=2 mm/m; Flatness: <=0.1 mm; Perpendicularity: <=0.3 deg; HDG: >=85 um |

### 3.3 Track C: Reflectors (F10-F12, F14)

| Step | Description | Duration | Personnel | FAI / QC | Accept Criteria |
|------|-------------|----------|-----------|----------|-----------------|
| **F10** | Receive and inspect CNC face plates (24x, anodized). Measure flatness, roughness, dimensions, anodize thickness. | 3.0 h | 1 (QC) | **[FAI-12]** Flatness all 24 plates; **[FAI-13]** Ra on reflective face (3 readings per plate); **[FAI-14]** Anodize thickness | Flatness: <0.1 mm over 800 mm; Ra: <=6.3 um; Anodize: 10-25 um Type II |
| **F11** | Receive and inspect AM frames (8x from ASEAN bureau, hard anodized). CMM orthogonality, dimensions, material cert, anodize thickness. | 4.0 h | 1 (QC) | **[FAI-15]** Orthogonality of 3 face planes per frame (24 measurements total); **[FAI-16]** Tensile coupon results; **[FAI-17]** Hard anodize thickness | Orthogonality: 90.00 +/-0.10 deg all pairs; Tensile: sigma_y >=230 MPa, El >=5%; Anodize: >=25 um Type III |
| | | | | **[QC HOLD]** -- orthogonality critical, reject if any pair exceeds +/-0.08 deg on raw frame | |
| **F12** | Assemble 8x reflectors (M4): install helicoils, insert dowel pins, mount 3 face plates per frame, 12x M6 bolts + Nylock nuts to 8 N-m, safety wire bolt pairs, measure orthogonality | 4.0 h (30 min each) | 2 (assembly tech + QC) | **[FAI-18]** Assembled orthogonality: CMM or angle gauge, 3 face pairs per reflector (24 total measurements) | All pairs: 90.00 +/-0.10 deg; torque: 8 +/-1 N-m; safety wire present on all 6 loops per reflector |
| | | | | **[QC HOLD]** -- 100% orthogonality verification, each reflector signed off individually | |
| **F14** | Pre-assemble 8x mast-reflector units (M5, IF-04): install nylon isolation bushings, apply Tef-Gel, seat reflector on mast top plate (dowels engage), 4x M10 bolts + Nordlock + Nylock to 50 N-m, safety wire | 3.0 h (22 min each) | 2 (assembly techs) | Verify nylon isolators present on all 4 bolts + 2 pins per unit; torque log | Torque: 50 +/-5 N-m; dowel pins fully seated; nylon isolators confirmed visual |

### 3.4 Track D: Assembly Integration (F06-F09, F15-F22)

| Step | Description | Duration | Personnel | FAI / QC | Accept Criteria |
|------|-------------|----------|-----------|----------|-----------------|
| **F06** | Install frame into hull (IF-01): lower frame with hoist, align holes with drift pins, install 84x M12 SS316 bolts with fender washers (HDPE side) + Nylock nuts, torque in 3 passes (finger, 20, 40 N-m), apply Sikaflex sealant | 4.0 h | 3 (2 fitters + crane op) | Torque log all 84 bolts; sealant continuity check | Torque: 40 +/-3 N-m all bolts; continuous sealant bead |
| **F07** | Install tow padeyes (IF-06): 2x tow padeyes, 4x M12 Gr 8.8 HDG each, fender washers on HDPE side, torque to 80 N-m | 1.0 h | 2 (fitters) | Torque log | Torque: 80 +/-5 N-m |
| **F08** | Pad eye proof load test (IF-02): apply 1.5x SWL (6,804 kgf = 66.8 kN) via hydraulic jack, hold 60 s, inspect | 1.5 h | 2 (test tech + QC) | **[FAI-08]** No permanent deformation; bolt torque recheck; weld visual | Zero deformation; bolts at spec; no weld cracking |
| | | | | **[QC HOLD]** -- critical safety test, certify and stamp | |
| **F09** | Hydrostatic leak test: float hull in test tank or harbor, observe 4 h, inspect IF-07 joint, foam fill ports, bolt penetrations | 4.0 h | 2 (QC + handler) | No visible water ingress; hull joint dry; draft measurement | Zero leaks; draft consistent with analysis (~19 mm at platform mass) |
| | | | | **[QC HOLD]** -- reject if any leak detected | |
| **F15** | Assemble GPS beacon (M6): mount GNSS/Iridium in IP67 enclosure, connect battery, seal, mount bracket, functional test | 2.0 h | 1 (electronics tech) | GPS fix test, Iridium SBD send/receive | Fix acquired <5 min; SBD received at shore station |
| **F16** | Mount GPS beacon on designated mast (IF-05): attach bracket with 2x M8 SS U-bolts, orient antenna skyward | 0.5 h | 1 (assembly tech) | Torque log | Torque: 15 +/-2 N-m |
| **F17** | GPS 72h endurance test (first article MANDATORY): power on beacon, transmit at 1 Hz for 72 h, monitor SBD at shore station | 72 h (background) | 1 (monitoring) | **[FAI-20]** Battery endurance >=72 h | >=72 h continuous operation; position accuracy <=+/-5 m |
| | | | | **[QC HOLD]** -- first article mandatory 72h test | |
| **F18** | Prepare mooring kit (M7): splice rode eyes, assemble chain-swivel-rode-anchor-shackles, verify mousing wire | 2.0 h | 1 (rigger) | Visual inspection; chain cert review | All shackle pins moused; chain cert on file |
| **F19** | Prepare tow kit (M8): inspect Dyneema splice quality (tuck count >=24), assemble bridle legs + shackles + drogue, pack | 1.0 h | 1 (rigger) | Splice visual; rope cert | Tuck count >=24; SWL >=8,000 kgf per cert |
| **F20** | Final assembly verification: insert all 8 mast-reflector units into deck sockets (dry run), verify all locking pins engage, remove and package, weigh complete system | 2.0 h | 3 (2 assembly + QC) | **[FAI-19]** Total platform mass on floor scale | Mass: <=1,100 kg (target ~939 kg per D9 mass budget) |
| | | | | **[QC HOLD]** -- mass limit check; reject if >1,100 kg | |
| **F21** | 360 deg RCS measurement: target on turntable or towed in circle, measure RCS at 1-deg increments at X-band (9.4 GHz) | 4.0 h | 3 (2 test eng + operator) | **[FAI-21]** RCS vs SIG-001 through SIG-004 | Peak >=1,000 m2; avg 360 deg >=1,000 m2; min >=700 m2; variation <=+/-2 dB |
| | | | | **[QC HOLD]** -- release gate; reject if any SIG requirement fails | |
| **F22** | Documentation and packaging: compile all material certs, inspection reports, test data into unit documentation package; package for transport | 3.0 h | 2 (QC + handler) | Documentation completeness review | All certs, reports, and FAI records present |
| | | | | **[QC HOLD]** -- unit not released without complete documentation | |

### 3.5 Summary

| Track | Steps | Active Labor (h) | Wait Time | QC Holds |
|-------|-------|-------------------|-----------|----------|
| A: Hull | F01-F04 | 12.0 | 24h foam cure | 0 |
| B: Steel | F05, F13 | 4.5 | -- | 1 (F05 weld UT) |
| C: Reflectors | F10-F12, F14 | 14.0 | -- | 2 (F11 orthogonality, F12 assembled orthogonality) |
| D: Integration | F06-F09, F15-F22 | 24.0 | 72h GPS test (background) | 6 (F08, F09, F17, F20, F21, F22) |
| **TOTAL** | F01-F22 | **~54.5 h** | | **9 QC holds** |

---

## 4. FAI Measurement Plan

This section expands the 21 FAI checks from [[DECS_D9_detail_specification.md]] Section 13.1 with specific measurement methods, instruments, sample sizes, and data recording requirements for TRI-H-001.

### 4.1 Hull & Foam (FAI-01 through FAI-04)

| FAI # | Characteristic | Nominal | Tolerance | Instrument | Sample Size | Data Record | Accept / Reject |
|-------|---------------|---------|-----------|------------|-------------|-------------|-----------------|
| FAI-01 | Hull outside diameter | 8,000 mm | +/-100 mm | 10 m tape measure at 4 diametrals (0/90/45/135 deg) | 4 readings | Record all 4 values + average | ACCEPT: all within 7,900-8,100 mm; REJECT: rework or scrap hull |
| FAI-02 | Hull wall thickness | >=8 mm minimum | +0/-0 (minimum) | UT thickness gauge (Elcometer) at 8 positions (4 per half) | 8 readings | Record all 8 values + minimum | ACCEPT: all >=8 mm; REJECT: hull section rejected |
| FAI-03 | Foam density | 40 kg/m3 target | 32-48 kg/m3 | Scale + calipers on cut coupon (100x100x100 mm) | 1 coupon per pour batch | Mass, volume, calculated density | ACCEPT: 32-48 kg/m3; REJECT: re-pour with adjusted mix ratio |
| FAI-04 | Foam water absorption | <=3% | Maximum | 48h immersion per ASTM D2842, weigh before/after | 1 coupon per pour batch | Dry mass, wet mass, % absorption | ACCEPT: <=3%; REJECT: reject foam batch, re-pour |

### 4.2 Frame & Masts (FAI-05 through FAI-11)

| FAI # | Characteristic | Nominal | Tolerance | Instrument | Sample Size | Data Record | Accept / Reject |
|-------|---------------|---------|-----------|------------|-------------|-------------|-----------------|
| FAI-05 | Frame socket positions | R=3,200 mm at 45 deg spacing | R: +/-5 mm; angle: +/-0.5 deg | 10 m tape + digital protractor + laser level | All 8 sockets | Radius and angle for each socket | ACCEPT: all within spec; REJECT: rework frame |
| FAI-06 | HDG coating thickness | >=85 um average | >=70 um local min | Magnetic thickness gauge (Elcometer 456), 3 readings per part | 10 points on frame + 3 per mast (8 masts) = 34 total | All readings tabulated | ACCEPT: avg >=85 um, all >=70 um; REJECT: re-galvanize |
| FAI-07 | Pad eye weld UT | Full penetration, no defects | No indications >3 mm | UT flaw detector (Olympus Epoch 650) per AWS D1.1 | 100% of pad eye welds (eye-to-backing plate, both sides) | UT scan printout, defect map | ACCEPT: no defects >3 mm; REJECT: repair weld, re-test |
| FAI-08 | Pad eye proof load | 6,804 kgf (1.5x SWL) | No permanent deformation | Hydraulic jack (10-ton) + load cell + dial indicator | 1 test | Load cell reading, deformation measurement, photo | ACCEPT: zero permanent deformation, bolts at spec; REJECT: reject pad eye assembly |
| FAI-09 | Mast straightness | <=2 mm/m (<=6 mm over 3,000 mm) | Maximum | 1,000 mm straight edge + feeler gauge, 3 positions per mast | All 8 masts (24 readings) | Deviation at each position | ACCEPT: all <=2 mm/m; REJECT: straighten or replace |
| FAI-10 | Mast top plate flatness | <=0.1 mm | Maximum | Granite flat + dial indicator or CMM | All 8 top plates | Peak-to-valley deviation | ACCEPT: <=0.1 mm; REJECT: machine-skim top face |
| FAI-11 | Mast top plate perpendicularity | <=0.3 deg | Maximum | Precision square + feeler gauge | All 8 masts | Angle deviation from 90 deg | ACCEPT: <=0.3 deg; REJECT: rework weld, re-machine |

### 4.3 Reflector Components (FAI-12 through FAI-18)

| FAI # | Characteristic | Nominal | Tolerance | Instrument | Sample Size | Data Record | Accept / Reject |
|-------|---------------|---------|-----------|------------|-------------|-------------|-----------------|
| FAI-12 | Face plate flatness | <0.1 mm over 800 mm | Maximum | CMM or granite surface plate (1,000x1,000 mm) + dial indicator | All 24 plates (100%) | Peak-to-valley per plate, 3 measurements per plate | ACCEPT: all <0.1 mm; REJECT: re-fly-cut on vacuum fixture |
| FAI-13 | Face plate surface roughness | Ra <=6.3 um | Maximum | Profilometer (Mitutoyo SJ-210), 3 readings per plate across reflective face | All 24 plates (72 readings total) | Ra values for each reading | ACCEPT: all <=6.3 um; REJECT: re-fly-cut with sharp insert |
| FAI-14 | Anodize thickness (face plates) | 10-25 um Type II | Range | Eddy current gauge (Fischer Dualscope), 2 readings per plate | 10% sample + all first-article = all 24 plates | Thickness per plate | ACCEPT: 10-25 um; REJECT: re-anodize |
| FAI-15 | AM frame orthogonality | 90.00 deg per face pair | +/-0.10 deg (reject at +/-0.08 deg on raw frame) | CMM, 3 face-pair angles per frame | All 8 frames (24 angle measurements) | Angle per pair, deviation from 90.00 deg | ACCEPT: all <=+/-0.10 deg; REJECT: reject frame, re-print |
| FAI-16 | AM tensile coupon | sigma_y >=230 MPa (XY); El >=5% | Minimum | Tensile test per ASTM E8 (3 coupons per build plate: X, Y, Z) | 3 per build plate (8 frames span 2-4 plates = 6-12 coupons) | Yield, UTS, elongation per coupon | ACCEPT: all meet min; REJECT: reject entire build plate lot |
| FAI-17 | Hard anodize thickness (frames) | >=25 um Type III | Minimum | Eddy current gauge | All 8 frames, 3 readings each | Thickness per reading | ACCEPT: all >=25 um; REJECT: re-anodize |
| FAI-18 | Assembled reflector orthogonality | 90.00 deg per face pair | +/-0.10 deg | CMM or digital angle gauge, 3 pairs per reflector | All 8 reflectors (24 measurements) | Angle per pair, deviation from 90.00 deg | ACCEPT: all <=+/-0.10 deg; REJECT: disassemble, identify root cause, reassemble |

### 4.4 System Level (FAI-19 through FAI-21)

| FAI # | Characteristic | Nominal | Tolerance | Instrument | Sample Size | Data Record | Accept / Reject |
|-------|---------------|---------|-----------|------------|-------------|-------------|-----------------|
| FAI-19 | Total platform mass | 939 kg target | <=1,100 kg maximum (GEO-007) | Floor scale or crane scale (2,000 kg rated, calibrated) | 1 complete system | Measured mass, component breakdown if over | ACCEPT: <=1,100 kg; REJECT: identify and remove excess mass |
| FAI-20 | GPS beacon 72h endurance | >=72 h at 1 Hz GPS + 60 s Iridium | Minimum | Timer + Iridium SBD monitoring dashboard + battery logger | 1 beacon | Run time to battery cutoff, position fix rate, SBD success rate | ACCEPT: >=72 h; REJECT: replace battery pack, re-test |
| FAI-21 | RCS spot check (first article) | Peak >=1,000 m2; avg >=1,000 m2; min >=700 m2 | Per SIG-001 to SIG-004 | Portable X-band radar (9.4 GHz) + turntable or tow, data logger | 360 deg sweep at 1 deg increments | RCS vs angle plot, peak/avg/min values, dB variation | ACCEPT: all SIG-001 to SIG-004 met; REJECT: diagnose reflector alignment, rework |

---

## 5. Test Integration

This section maps the 7 standards-driven tests from [[DECS_S12_standards_compliance.md]] Section 6 into the first article build timeline. Tests T-07 and T-04 run in parallel with Track C; T-01 and T-02 precede integration; T-03 and T-05 follow assembly.

### 5.1 Test Sequence for First Article

| Test ID | Standard Basis | Description | Prerequisites | Integrated with Build Step | Cost | Duration |
|---------|---------------|-------------|---------------|---------------------------|------|----------|
| **T-07** | ASTM F3301/F3318 | AM frame qualification build: tensile coupons + CT scan + dimensional | AM frames ordered | Before F11 (incoming inspection) | $3,500 | 3 weeks (parallel with procurement) |
| **T-01** | MIL-STD-810H 509.7 | Salt fog 72h: 1 reflector-mast assy, 1 pad eye, 1 GPS, 3 chain links | 1 spare reflector-mast unit assembled | After F12, parallel with integration | $3,000 | 5 days |
| **T-04** | Functional | GPS beacon 72h endurance | GPS assembled at F15 | Integrated as F17 | $500 | 4 days |
| **T-02** | EN 818-3 / adapted | Mooring proof load: chain + shackle + swivel + pad eye assembly | Frame installed in hull (F06), pad eye proof load (F08 / FAI-08) | After F08, before F09 | $5,000 | 2 days |
| **T-03** | IALA 1093 adapted | RCS measurement 360 deg at X-band | All 8 reflectors assembled and mounted (F20) | Integrated as F21 / FAI-21 | $5,000 | 2 days |
| **T-05** | MIL-STD-810H 514.8/512.6 | Sea trial 72h at anchor in SS 5: hull integrity, mast retention, mooring performance | Complete assembled target; T-01, T-02, T-03, T-04 all PASS | After F22 (unit released for sea trial) | $8,000 | 5 days |
| **T-06** | Operational demo | Deployment exercise: crew timing, tool-free connections | T-05 PASS; crew trained | After T-05 recovery | $3,000 | 1 day |

### 5.2 Test Decision Gates

```
FIRST ARTICLE TEST FLOW — TRI-H-001
====================================

  T-07 (AM qual)     T-01 (Salt fog)     T-04 (GPS)
  [Week 1-3]         [Week 4-5]          [Week 5-8]
       │                  │                   │
       ▼                  ▼                   ▼
  GATE 1: T-07 PASS? ──→ GATE 2: T-01 PASS? + T-04 PASS?
       │ NO: reject AM lot    │ NO: resolve corrosion/GPS failure
       │ YES ──────────→      │ YES ──────────→
                              │
  T-02 (Mooring proof)       │
  [Week 6]                    │
       │                      │
       ▼                      ▼
  GATE 3: T-02 PASS? ────────→ Proceed to full assembly
       │ NO: resolve mooring failure
       │ YES ──────────→
                              │
  T-03 (RCS 360 deg) ←───────┘
  [Week 8-9]
       │
       ▼
  GATE 4: T-03 PASS? (SIG-001 to SIG-004)
       │ NO: diagnose reflector alignment
       │ YES ──────────→
                              │
  T-05 (Sea trial 72h)       │
  [Week 10-12]                │
       │                      │
       ▼                      ▼
  GATE 5: T-05 PASS? (OPR-002, OPR-003, FOR-007)
       │ NO: structural/mooring redesign
       │ YES ──────────→
                              │
  T-06 (Deployment drill)    │
  [Week 13]                   │
       │                      │
       ▼                      ▼
  GATE 6: T-06 PASS? (ERG-001 to ERG-006, ASM-006)
       │ NO: revise procedures, retrain crew
       │ YES ──────────→
                              │
  ┌────────────────────────────┘
  │ FIRST ARTICLE RELEASE
  └────────────────────────────→ Proceed to Lot 1 production
```

### 5.3 Test Facility Assignments

| Test | Facility | Location | Lead Time to Book |
|------|----------|----------|-------------------|
| T-01 | Salt fog chamber (ASTM B117) | QUATEST 3 (HCMC) or VKT Materials Lab (Hanoi) | 2 weeks |
| T-02 | Hydraulic load frame (>=50 kN) | University mechanical lab or shipyard test rig | 1 week |
| T-03 | X-band RCS range (9.4 GHz, turntable >=8 m) | Military facility or university anechoic | 4 weeks |
| T-04 | Lab bench (any location) | In-house assembly facility | -- |
| T-05 | Open sea (15-50 m depth, SS 5 access) | Navy-designated test range | 4 weeks + weather window |
| T-06 | Calm water (harbor, SS 2-3) | Naval base or commercial marina | 1 week |
| T-07 | AM bureau + mechanical test lab | Xometry Asia (SG) + university lab | 3 weeks |

---

## 6. Non-Conformance Handling

### 6.1 Non-Conformance Report (NCR) Process

All deviations from specification discovered during first article build shall be documented on a Non-Conformance Report (NCR):

| Step | Action | Responsible | Timeline |
|------|--------|-------------|----------|
| 1. Discovery | Inspector identifies out-of-tolerance condition; stops work at that station | QC Inspector | Immediate |
| 2. Documentation | NCR form completed: part ID, serial, characteristic, measured value, spec limit, severity classification | QC Inspector | Within 2 hours |
| 3. Classification | Classify severity: CRITICAL (safety/RCS), MAJOR (fit/function), MINOR (cosmetic) | QC Lead + Engineering | Within 4 hours |
| 4. Disposition | Determine disposition: REWORK, USE-AS-IS (with engineering justification), SCRAP, RETURN TO SUPPLIER | Engineering + QC Lead | Within 24 hours |
| 5. Corrective action | For CRITICAL/MAJOR: identify root cause, implement corrective action for subsequent units | Engineering | Within 1 week |
| 6. Closure | Verify corrective action effective; close NCR | QC Lead | Before next unit build |

### 6.2 Severity Classification

| Severity | Definition | Examples | Disposition Authority |
|----------|-----------|---------|----------------------|
| **CRITICAL** | Affects safety or primary performance (RCS) | FAI-07 weld defect; FAI-15/18 orthogonality out of spec; FAI-08 proof load failure; FAI-21 RCS below threshold | Chief Engineer only |
| **MAJOR** | Affects fit, function, or interchangeability | FAI-01 hull OD out of spec; FAI-06 HDG under-thickness; FAI-12 flatness exceeded; mass over limit | Engineering + QC Lead |
| **MINOR** | Cosmetic or documentation only | Surface scratches on non-reflective surfaces; marking legibility; non-critical dimension | QC Lead |

### 6.3 First Article Specific NCR Triggers

| FAI Check | Failure Mode | Immediate Action | Escalation |
|-----------|-------------|------------------|------------|
| FAI-15 (frame orthogonality) | Any pair >+/-0.10 deg | Quarantine frame; measure remaining 7 frames; notify AM supplier | If >1 frame fails: halt build, audit AM supplier process |
| FAI-18 (assembled orthogonality) | Any pair >+/-0.10 deg | Disassemble reflector; inspect frame datums and face plate holes; identify misalignment source | Root cause: frame (FAI-15 passed but assembled drift), face plates (hole position), or assembly procedure |
| FAI-21 (RCS) | Peak <1,000 m2 or min <700 m2 | Verify all 8 reflector orthogonalities in-situ; check mast perpendicularity; re-measure with calibrated radar | If reflectors individually OK: check inter-reflector interference pattern |
| FAI-08 (proof load) | Permanent deformation detected | Reject pad eye assembly; UT weld re-inspection; redesign backing plate thickness if needed | Engineering review of D8 structural analysis assumptions |

---

## 7. Documentation Package

### 7.1 As-Built Data Package Contents

The following documents shall be compiled for TRI-H-001 and retained as the first article baseline:

| # | Document | Source | Format |
|---|----------|--------|--------|
| 1 | **FAI Report** (21 checks) | QC inspection records from Section 4 | Tabulated results with pass/fail, signed by QC inspector |
| 2 | **Material Certificates** | Supplier mill certs, CoAs, powder certs | PDF copies filed per BOM item number (1.1.01 through 1.9.08) |
| 3a | HDPE hull: PE100 resin certificate | Binh Minh Plastics | Per ASTM D3350 |
| 3b | Steel: S235 mill certificate | Hoa Phat Group | Per EN 10025-2 (composition, mechanical, Charpy) |
| 3c | Aluminum: 6061-T6 mill certificate | Korean mill | Per ASTM B209 (alloy, temper, tensile) |
| 3d | AM powder: AlSi10Mg certificate of analysis | AM bureau powder supplier | Per ASTM B937 (composition, PSD, flowability) |
| 3e | Chain: G30 proof load certificate | Chain manufacturer | Per EN 818-3 |
| 3f | Dyneema: rope SWL certificate | Marlow Ropes | Manufacturer test cert |
| 4 | **AM Build Reports** (8 frames) | AM bureau | Laser power, scan speed, build orientation, support strategy per ASTM F3301 |
| 5 | **AM Tensile Test Report** | Mechanical test lab | sigma_y, UTS, elongation per ASTM E8 (3 coupons per build plate) |
| 6 | **CT Scan Report** (3 frames) | AM bureau or metrology lab | Internal defect map per ASTM E1570; accept: no voids >=1.0 mm |
| 7 | **HDG Coating Reports** | Vinh Thanh HDG | Thickness readings per ASTM A123 |
| 8 | **Anodize Certificates** | Saigon Anodizing (Type II) + Xometry (Type III) | Thickness per MIL-A-8625F |
| 9 | **Weld Inspection Reports** | Steel fab shop QC | Visual (100%) + UT (pad eye), per AWS D1.1 |
| 10 | **Torque Log** | Assembly technicians | All critical bolted joints: IF-01 (84x M12), IF-02 (8x M16), IF-04 (32x M10), M4 (96x M6) |
| 11 | **Orthogonality Data** (8 reflectors x 3 pairs) | QC inspector | 24 angle measurements, deviation from 90.00 deg |
| 12 | **RCS Test Data** | Test engineers | 360 deg sweep: RCS vs angle, peak/avg/min, dB variation |
| 13 | **GPS Endurance Test Data** | Test engineer | 72h run: fix rate, SBD success, battery voltage curve |
| 14 | **Salt Fog Test Report** (T-01) | QUATEST 3 or VKT lab | Post-72h inspection: visual, RCS, torque audit per ASTM B117 |
| 15 | **Proof Load Test Report** (T-02) | Test engineer | Load cell reading, deformation measurement, photos |
| 16 | **Sea Trial Report** (T-05) | Test engineers | 72h deployment data: GPS track, weather log, pre/post inspection |
| 17 | **Deployment Exercise Report** (T-06) | Operations lead | Crew timing, task sequence, lessons learned |
| 18 | **NCR Log** | QC Lead | All NCRs raised during build, dispositions, corrective actions |
| 19 | **Mass Statement** | QC inspector | Measured mass vs D9 mass budget (939 kg target, 1,100 kg limit) |
| 20 | **Photographs** | QC inspector | Key build stages, completed unit from 4 cardinal directions, close-ups of critical interfaces |

### 7.2 Document Control

| Aspect | Requirement |
|--------|-------------|
| Filing | All documents filed by serial number (TRI-H-001) in project archive |
| Retention | Minimum 10 years per defense procurement practice |
| Format | Hard copy + digital scan (PDF) |
| Approval | FAI Report signed by QC Inspector, countersigned by Chief Engineer |
| Distribution | 1 copy with unit; 1 copy retained at factory; 1 copy to customer |

---

## 8. Schedule

### 8.1 First Article Build Schedule (Gantt-Style)

```
FIRST ARTICLE BUILD SCHEDULE — TRI-H-001
==========================================================================
Week:   0    1    2    3    4    5    6    7    8    9   10   11   12   13
==========================================================================

PROCUREMENT (parallel, pre-build)
  Long-lead orders (Dyneema, GPS, AM frames)
  ├─ PO ─┤               ├── RECEIVE ──┤
  Standard materials (steel, HDPE, fasteners, foam)
  ├─ PO ─┤    ├── RECEIVE ──┤
  AM frames (8x, ASEAN bureau)
  ├─ PO ─┤    ├──── BUILD + HT + CNC + ANODIZE ────┤
                                    └── T-07 ──┤
                                    (tensile, CT scan)

TRACK A: HULL
  Hull fab (supplier)           ├─── F01 Receive ──┤
  Hull join + foam (F02-F03)         ├─ F02 ─┤24h├
  Hull trim + drill (F04)                     ├ F04 ┤
                                    Wk 3        Wk 5

TRACK B: STEEL
  Frame + mast fab (supplier)   ├──── FAB ────┤
  HDG                                    ├HDG┤
  Receive + inspect (F05, F13)              ├ F05,F13 ┤
                                    Wk 2         Wk 5

TRACK C: REFLECTORS
  Al import + CNC face plates        ├── IMPORT ──┤── CNC ──┤
  Anodize (Type II)                              ├ ANODIZE ┤
  Receive AM frames (F11)                    ├── F11 ──┤
  Receive face plates (F10)                       ├ F10 ┤
  Assemble reflectors (F12)                          ├ F12 ┤
  Pre-assemble M5 (F14)                                ├F14┤
                                    Wk 3              Wk 6  Wk 7

T-01: SALT FOG (parallel)
  Load specimens, 72h exposure        ├── T-01 ──┤
  Post-test inspection                         ├─┤
                                         Wk 5    Wk 6

TRACK D: INTEGRATION
  Install frame (F06)                                   ├F06┤
  Tow padeyes (F07)                                      ├┤
  Proof load (F08 / T-02)                                ├T-02┤
  Leak test (F09)                                          ├F09┤
  GPS assembly + mount (F15-F16)                   ├F15┤
  GPS endurance (F17)                              ├── 72h ──┤
  Mooring + tow kits (F18-F19)                    ├F18┤├F19┤
  Final dry-fit + mass (F20)                                   ├F20┤
  RCS measurement (F21 / T-03)                                  ├T-03┤
  Documentation (F22)                                              ├F22┤
                                                 Wk 6         Wk 8   Wk 9

T-05: SEA TRIAL
  Deploy, 72h at anchor, recover              ├──── T-05 ────┤
                                              Wk 10      Wk 12

T-06: DEPLOYMENT DRILL
  Crew exercise, timing                                    ├T-06┤
                                                           Wk 13

  FIRST ARTICLE RELEASE ─────────────────────────────────────→ ▼ Wk 13
==========================================================================
  Total program: 13 weeks from PO to first article release
  Critical path: AM frames (3 wk) → T-07 → F11 → F12 → F14 → F20 → T-03
==========================================================================
```

### 8.2 Key Milestones

| Milestone | Target Week | Dependency |
|-----------|-------------|------------|
| All purchase orders issued | Week 0 | Budget approval |
| AM frames + T-07 tensile results received | Week 4 | AM bureau delivery |
| Hull sections received and joined | Week 4-5 | HDPE supplier |
| Frame + masts galvanized and received | Week 5 | Steel fab + HDG |
| T-01 salt fog test complete | Week 6 | Reflector-mast specimen available |
| All reflectors assembled and verified (F12) | Week 6-7 | AM frames + face plates received |
| T-02 mooring proof load PASS | Week 7 | Frame installed |
| GPS 72h endurance PASS (F17) | Week 8 | GPS assembled |
| RCS 360 deg PASS (T-03 / F21) | Week 9 | Full assembly complete |
| T-05 sea trial complete | Week 12 | Assembly released + weather window |
| T-06 deployment exercise complete | Week 13 | Sea trial success |
| **First article release** | **Week 13** | All gates passed |

---

## 9. Budget

### 9.1 First Article Cost Breakdown

The first article unit incurs additional costs compared to the production baseline ($29,655 per unit @10 from [[OCP_C14_cost_analysis.md]]) due to first-time learning, 100% inspection overhead, and the integrated test program.

| Cost Element | Production Baseline (@10) | First Article Adder | First Article Total | Notes |
|-------------|---------------------------|--------------------|--------------------|-------|
| **BOM (materials)** | $17,862 | $0 | $17,862 | Same BOM as production |
| **Labor (manufacturing)** | $2,726 (247 h) | +$1,500 (first-unit learning loss, 85% curve = ~30% adder on first unit) | $4,226 | ~320 h for first unit vs 247 h steady-state |
| **Tooling (amortized)** | $2,500 (@10) | +$15,000 (full tooling cost on first unit) | $17,500 | Welding jigs $3K, CNC fixture $2K, alignment jig $2.5K, CMM fixture $1K, rotomold tooling $15K (if rotomold); $8.5K if welded hull |
| **Overhead** | $3,871 | +$500 | $4,371 | Additional production engineering for first article |
| **FAI inspection overhead** | -- | +$2,000 | $2,000 | 100% inspection on 21 FAI checks; CMM time, UT rental |
| **Test program (T-01 to T-07)** | -- | +$28,000 | $28,000 | Per [[DECS_S12_standards_compliance.md]] Section 6.2 |
| **Test logistics** | -- | +$4,000 | $4,000 | Transport to test facilities, sea trial vessel charter share |
| **Documentation** | $150 | +$1,000 | $1,150 | FAI report, as-built package, photo documentation |
| **Margin (10%)** | $2,696 | -- | $2,696 | Standard margin |
| | | | | |
| **FIRST ARTICLE TOTAL** | -- | -- | **~$81,805** | |
| *vs Production unit @10:* | *$29,655* | | *$52,150 adder* | |

### 9.2 Cost Justification

The first article adder of approximately $52,150 over production unit cost is driven by:

| Driver | Amount | % of Adder | Justification |
|--------|--------|-----------|---------------|
| Test program (T-01 to T-07) | $28,000 | 54% | One-time standards compliance verification; amortized across production run |
| Tooling (first unit bears full cost) | $15,000 | 29% | Tooling cost amortized to $250/unit at 100 units |
| First-unit learning loss | $1,500 | 3% | 85% learning curve; first unit ~30% more labor |
| FAI inspection overhead | $2,000 | 4% | 100% dimensional verification (21 checks); reduced to 10 checks for subsequent units |
| Test logistics | $4,000 | 8% | Transport, vessel charter, facility fees |
| Documentation | $1,000 | 2% | Comprehensive as-built package |

### 9.3 Comparison to Development Budget

| Budget Item | Allocation | First Article Consumption | Remaining |
|-------------|-----------|---------------------------|-----------|
| Phase 3 prototype fabrication | $55,000 | ~$22,000 (BOM + labor) | $33,000 |
| Phase 3 testing | $35,000 | ~$28,000 (T-01 to T-07) | $7,000 |
| Phase 3 AM first article | $12,000 | ~$10,700 (8 frames + test coupons) | $1,300 |
| Phase 4 detail design | $20,000 | ~$3,000 (documentation) | $17,000 |
| Contingency | $28,000 | ~$4,000 (test logistics) | $24,000 |
| **Total consumed** | | **~$67,700** | |
| **Development budget** | **$280,000** | | **$212,300 remaining** |

---

## 10. Success Criteria & Release

### 10.1 First Article Release Criteria

TRI-H-001 shall be released for acceptance only when ALL of the following conditions are met:

| # | Criterion | Evidence | Responsible |
|---|----------|----------|-------------|
| RC-01 | All 21 FAI checks (FAI-01 to FAI-21) recorded as PASS | Signed FAI Report | QC Inspector |
| RC-02 | All 7 tests (T-01 to T-07) recorded as PASS | Individual test reports | Test Engineers |
| RC-03 | All CRITICAL NCRs closed with corrective action verified | NCR Log | QC Lead |
| RC-04 | All MAJOR NCRs closed or dispositioned USE-AS-IS with engineering justification | NCR Log | Engineering |
| RC-05 | Complete documentation package assembled per Section 7 | Document checklist signed | QC Lead |
| RC-06 | Mass verified <=1,100 kg (FAI-19) | Mass statement | QC Inspector |
| RC-07 | RCS verified per SIG-001 to SIG-004 (FAI-21) | RCS test data | Test Engineers |
| RC-08 | GPS endurance verified >=72 h (FAI-20) | GPS endurance data | Test Engineer |
| RC-09 | Sea trial (T-05) demonstrated 72 h survival at SS 5+ | Sea trial report | Test Engineers |
| RC-10 | Deployment exercise (T-06) confirmed <=30 min, <=4 crew | Deployment report | Operations Lead |

### 10.2 Release Decision Authority

| Decision | Authority | Action |
|----------|-----------|--------|
| **RELEASE** -- all criteria met | Chief Engineer + QC Lead (dual signature) | Unit released for customer delivery or operational use; production baseline established for Lot 1 |
| **CONDITIONAL RELEASE** -- MINOR NCRs open | Chief Engineer | Unit released with documented limitations; corrective actions tracked to closure |
| **HOLD** -- MAJOR NCRs open or tests incomplete | Chief Engineer | Unit held at factory; remediation plan with timeline required |
| **REJECT** -- CRITICAL NCR unresolvable or fundamental design flaw | Chief Engineer + Program Manager | Unit quarantined; root cause analysis; design change required before next unit |

### 10.3 Transition to Production

Upon successful release of TRI-H-001, the following actions enable Lot 1 production (10 units per [[OCP_P15_production_planning.md]] Section 7):

| # | Action | Input | Output |
|---|--------|-------|--------|
| 1 | Baseline production inspection plan (PI-01 to PI-10) | FAI results identifying stable processes | Reduced inspection plan per D9 Section 13.2 |
| 2 | Lessons learned from first article build | NCR log, timing data, process observations | Updated work instructions for Lot 1 |
| 3 | Supplier performance evaluation | Delivery, quality, lead time data from first article | Confirmed supplier list for production |
| 4 | Cost actuals vs estimate | First article cost data | Revised cost estimate for Lot 1 units |
| 5 | Issue Lot 1 purchase orders | All materials validated, suppliers confirmed | POs for 10 units per P15 Section 7.1 |

### 10.4 Production Inspection Reduction

After successful first article release, subsequent units transition from 21 FAI checks to 10 production inspections per [[DECS_D9_detail_specification.md]] Section 13.2:

| FAI Check | First Article | Production (PI) | Rationale for Reduction |
|-----------|--------------|------------------|------------------------|
| FAI-01 Hull OD | 100% | PI-01: 100% | Safety-critical dimension |
| FAI-02 Wall thickness | 100% (8 points) | PI-01: 100% (4 points) | Reduced sampling after process confirmed |
| FAI-03 Foam density | 100% | PI-02: 1 per batch | Batch-level control sufficient |
| FAI-04 Foam absorption | 100% | -- | Process validated; omit unless batch changes |
| FAI-05 Frame dimensions | 100% | -- | Process validated at supplier |
| FAI-06 HDG thickness | 100% (34 points) | PI-03: 100% (4 per assembly) | Reduced sampling |
| FAI-07 Pad eye weld UT | 100% | PI-04: 100% | Safety-critical; never reduce |
| FAI-08 Proof load | 100% | 100% (first + every 10th) | Per P15 QC plan |
| FAI-09-11 Mast checks | 100% | -- | Process validated at supplier |
| FAI-12 Face plate flatness | 100% | PI-05: 100% | Performance-critical |
| FAI-13 Face plate Ra | 100% | -- | Process validated; spot check 10% |
| FAI-14 Anodize thickness | 100% | -- | Process validated; spot check 10% |
| FAI-15 AM frame orthogonality | 100% | PI-06: 100% | Performance-critical; never reduce |
| FAI-16 Tensile coupons | 3 per build plate | PI-06: 1 per build plate | Reduced after process capability proven |
| FAI-17 Hard anodize | 100% | -- | Process validated; spot check |
| FAI-18 Assembled orthogonality | 100% | PI-07: 100% | Performance-critical; never reduce |
| FAI-19 Total mass | 100% | PI-08: 100% | Safety-critical |
| FAI-20 GPS endurance | 100% | PI-09: 10% (1 per 10 units) | Process validated |
| FAI-21 RCS measurement | 100% | PI-10: 10% (1 per 10 units) | Process validated; full array test expensive |

---

## Cross-References

### Phase 4 Documents
- [[procurement_bom.md]] -- Detailed procurement BOM with supplier assignments
- [[acceptance_test_procedures.md]] -- Acceptance test procedures for production units
- [[logistics_sustainment_plan.md]] -- Logistics and sustainment plan
- [[manufacturing_drawing_specs.md]] -- Manufacturing drawing specifications
- [[deployment_operations_manual.md]] -- Deployment and operations manual

### Phase 3 Source Documents
- [[../03_embodiment/PRAD_A7_architecture_definition.md]] -- System architecture (M1-M8, IF-01 to IF-07)
- [[../03_embodiment/DECS_D9_detail_specification.md]] -- Detail specification (tolerances, FAI checks, fastener schedule)
- [[../03_embodiment/DECS_S12_standards_compliance.md]] -- Standards compliance (26 standards, 7 tests)
- [[../03_embodiment/DECS_C11_requirements_verification.md]] -- Requirements verification matrix (116 requirements)
- [[../03_embodiment/OCP_C14_cost_analysis.md]] -- Cost analysis (BOM, labor, volume pricing)
- [[../03_embodiment/OCP_P15_production_planning.md]] -- Production planning (F01-F22, suppliers, schedule)
- [[../03_embodiment/PROTO_reflector_rcs_validation.md]] -- Reflector prototype validation plan
- [[../03_embodiment/PROTO_hull_platform_validation.md]] -- Hull prototype validation plan

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1)
- [[../01_requirements/standards_mapping.md]] -- MIL-STD and ASTM standards mapping

---

*End of First Article Build Plan. This document governs the manufacture, inspection, testing, and release of serial TRI-H-001, the first production unit of the THANH TRI-H fixed sea target. All 21 FAI checks, 7 standards-driven tests, and 9 QC hold points must be satisfied before unit release. Upon successful first article completion, production transitions to the reduced PI-01 through PI-10 inspection plan for Lot 1 (10 units).*
