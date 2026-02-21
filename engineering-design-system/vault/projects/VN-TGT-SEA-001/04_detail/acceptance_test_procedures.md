---
project: VN-TGT-SEA-001
phase: 4
type: detail_design
document: "Acceptance Test Procedures"
version: 1.0
created: 2026-02-11
status: draft
---

# Acceptance Test Procedures (ATP) — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Formal, step-by-step acceptance test procedures for all 7 qualification tests (T-01 through T-07) from [[../03_embodiment/DECS_S12_standards_compliance.md]] and all production acceptance tests from [[../03_embodiment/OCP_P15_production_planning.md]] Section 4.3. These procedures are written to be executable by a trained technician without additional reference.
**Input:** [[../03_embodiment/DECS_S12_standards_compliance.md]], [[../03_embodiment/DECS_C11_requirements_verification.md]], [[../03_embodiment/OCP_P15_production_planning.md]], [[../03_embodiment/OCP_C14_cost_analysis.md]], [[../03_embodiment/PRAD_D8_design_structure.md]], [[../03_embodiment/DECS_D9_detail_specification.md]]
**Applicable Standards:** MIL-STD-810H, EN 818-3, IALA 1093, ASTM F3301/F3318, ASTM B117, AWS D1.1

---

## 1. Purpose and Scope

### 1.1 Purpose

This document defines the complete acceptance test program for the THANH TRI-H fixed sea target. It provides:

- Formal step-by-step test procedures for all 7 qualification tests (T-01 through T-07)
- Production acceptance test procedures for every manufactured unit (ATP-PA-01 through ATP-PA-08)
- Pass/fail criteria traceable to the 116 requirements in [[../01_requirements/requirements_list.md]]
- Data recording forms for each test
- Test sequence, dependencies, and decision gates

### 1.2 Scope

| Category | Coverage |
|----------|----------|
| Qualification tests (Type I) | 7 tests on first article: salt fog, proof load, RCS, GPS endurance, sea trial, deployment exercise, AM qualification |
| Production acceptance tests (Type II) | 8 tests on every unit: mass, dimensional, leak, fit, RCS, GPS, visual, documentation |
| Periodic tests (Type III) | 2 tests on sampled units: pad eye proof load (every 10th), GPS 72h endurance (every 5th) |
| Requirements verified | 34 PENDING-TEST requirements from [[../03_embodiment/DECS_C11_requirements_verification.md]] |

### 1.3 Definitions

| Term | Definition |
|------|-----------|
| **First Article** | The first complete unit (S/N 001) produced from production tooling and processes |
| **Test Article** | A component or assembly specifically designated for destructive or non-destructive testing |
| **SWL** | Safe Working Load -- maximum load for normal service |
| **DAF** | Dynamic Amplification Factor |
| **Pass** | Test article meets ALL listed acceptance criteria |
| **Conditional Pass** | Test article meets primary criteria but fails one or more secondary (WISH) criteria; disposition by engineering |
| **Fail** | Test article does not meet one or more mandatory acceptance criteria |

---

## 2. Test Classification

### 2.1 Type I: Qualification Tests (First Article Only)

Performed on the first production unit (S/N 001) or dedicated test articles. Must ALL PASS before production release.

| Test ID | Title | Standard Basis | Purpose |
|---------|-------|---------------|---------|
| ATP-01 | Salt Fog Test | MIL-STD-810H Method 509.7 | Corrosion resistance of all materials |
| ATP-02 | Mooring Hardware Proof Load | EN 818-3 / API RP 2SK adapted | Structural integrity of mooring load path |
| ATP-05 | Sea Trial -- 72h Anchored | MIL-STD-810H 514.8/512.6 tailored | Full-system environmental survival |
| ATP-06 | Deployment Exercise | Operational demonstration | Crew, timing, tool-free verification |
| ATP-07 | AM Frame Qualification | ASTM F3301/F3318 | AM material and process validation |

### 2.2 Type II: Production Acceptance Tests (Every Unit)

Performed on 100% of production units before delivery release.

| Test ID | Title | Purpose |
|---------|-------|---------|
| ATP-PA-01 | System Mass | Verify GEO-007: <=1,100 kg |
| ATP-PA-02 | Hull Dimensional | Verify GEO-001, GEO-002 |
| ATP-PA-03 | Hydrostatic Leak Test | Verify hull integrity at IF-07 |
| ATP-PA-04 | Mast Socket Fit Test | Verify IF-03 fit and pin engagement |
| ATP-PA-05 | 360-deg RCS Measurement | Verify SIG-001 to SIG-004 |
| ATP-PA-06 | GPS Beacon Function | Verify SIG-007, ENR-002 |
| ATP-PA-07 | Visual Inspection | Comprehensive surface/assembly checklist |
| ATP-PA-08 | Documentation Verification | Material certs, test records complete |

### 2.3 Type III: Periodic Tests (Sampled)

| Test ID | Title | Frequency | Purpose |
|---------|-------|-----------|---------|
| ATP-02P | Pad Eye Proof Load | Every 10th unit | Verify weld and bolt integrity at IF-02 |
| ATP-04P | GPS 72h Endurance | Every 5th unit | Verify ENR-001: >=72h battery life |

---

## 3. ATP-01: Salt Fog Test (MIL-STD-810H Method 509.7)

### 3.1 Objective and Requirements Traced

Verify that all materials and coatings withstand 72 hours of continuous salt fog exposure without degradation below acceptance thresholds.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| OPR-009 | Salt spray exposure 72h | No base metal corrosion |
| MAT-005 | S235 HDG steel corrosion protection | Zinc coating intact, no red rust |
| MAT-008 | 6061-T6 Type II anodize | No pitting through anodize layer |
| MAT-009 | AlSi10Mg Type III hard anodize | No pitting through hard coat |
| MAT-010 | Mast HDG coating | No red rust on mast tube or gussets |

### 3.2 Test Articles

| Item | Description | BOM Reference | Qty |
|------|-------------|---------------|-----|
| TA-01-1 | Complete reflector-mast assembly (M5 unit: mast tube + gussets + top plate + AM frame + 3 CNC face plates + all fasteners + isolation bushings) | BOM 1.3 + 1.4 + 1.5 | 1 |
| TA-01-2 | Pad eye assembly (eye plate + backing plate 200x200x14 mm + 4x M16 Gr 8.8 HDG bolts + zinc anode) | BOM 1.2.03 | 1 |
| TA-01-3 | GPS beacon assembly (powered, sealed IP67 enclosure with battery) | BOM 1.6 | 1 |
| TA-01-4 | Chain samples (19 mm G30 HDG, 300 mm links) | BOM 1.7.02 | 3 |

### 3.3 Equipment Required

| Equipment | Specification | Calibration |
|-----------|---------------|-------------|
| Salt fog chamber | ASTM B117 compliant, >=1.5 m3 internal volume, temperature-controlled | Annual calibration; verify 35 +/-2 deg C |
| NaCl solution | 5 +/-1% by weight analytical grade NaCl in DI water | Verify concentration by hydrometer before each test |
| pH meter | Range 6.5-7.2 (ASTM B117 requirement) | Calibrate before test |
| Calibrated thermometer | 0-100 deg C, +/-0.5 deg C resolution | Annual calibration |
| Digital caliper | 0-300 mm, 0.01 mm resolution | Annual calibration |
| Torque wrench | 1-50 N-m range | Annual calibration |
| Portable X-band radar (or access to RCS range) | 9.4 GHz, calibrated | Before and after RCS measurement |
| Camera (digital) | >=12 MP, macro capability | N/A |
| 10x magnifying loupe | — | N/A |

### 3.4 Pre-Test Setup

1. **Photograph** all test articles from 4 sides before test (reference condition).
2. **Measure** baseline RCS of TA-01-1 reflector assembly at X-band 9.4 GHz at 0 deg, 90 deg, 180 deg, 270 deg azimuth. Record in Data Form ATP-01-DF.
3. **Torque-audit** all bolted connections on TA-01-1: record torque values for M6 face-to-frame bolts (target 8 N-m), M10 reflector-to-mast bolts (target 15 N-m).
4. **Verify** GPS beacon TA-01-3 is powered ON, transmitting at 1 Hz, and shore station is receiving SBD messages.
5. **Verify** salt fog chamber temperature at 35 +/-2 deg C and NaCl solution at 5 +/-1%.
6. **Position** test articles in chamber: TA-01-1 upright (reflector at top), TA-01-2 vertically (eye plate up), TA-01-3 at operating orientation, TA-01-4 chains hung vertically. Ensure no article shields another from fog.

### 3.5 Test Execution

| Step | Time | Action |
|------|------|--------|
| 1 | T=0h | Close chamber. Activate salt fog generation. Confirm fog rate 1.0-2.0 mL/80 cm2/hr per ASTM B117. |
| 2 | T=0-72h | Maintain continuous salt fog at 35 +/-2 deg C, 5 +/-1% NaCl. |
| 3 | T=24h | Visual inspection through chamber window (do NOT open). Confirm fog generation active. Check GPS TA-01-3 still transmitting via shore station. |
| 4 | T=48h | Visual inspection through chamber window. Check GPS still transmitting. |
| 5 | T=72h | Stop salt fog generation. Allow 1 hour settling time. Open chamber. |
| 6 | T=73h | Remove all test articles. Rinse gently with deionized water to remove salt deposits. Allow 2 hours air-drying at room temperature. |

### 3.6 Post-Test Inspection

| Inspection | Method | Record |
|------------|--------|--------|
| **Visual (all articles)** | Examine all surfaces with unaided eye and 10x loupe per ASTM B117 rating methodology. Photograph all surfaces. | Corrosion rating per ASTM B117 (RA number). Note any white rust (zinc oxide), red rust (base metal), or pitting. |
| **RCS measurement (TA-01-1)** | Repeat baseline RCS measurement at same 4 azimuths using identical setup. Compare pre/post values. | Record RCS (dBsm) at each angle. Calculate degradation in dB. |
| **Torque audit (TA-01-1)** | Verify all bolted connections using calibrated torque wrench. Record break-away torque. | Pass if >=80% of original torque value retained on all bolts. |
| **GPS function check (TA-01-3)** | Verify GPS beacon is still transmitting. Check position accuracy against known reference. | Pass if beacon transmitting at 72h mark and position within +/-5 m of reference. |
| **Chain inspection (TA-01-4)** | Visual inspection of 3 chain samples for red rust, pitting, coating loss. Measure zinc remaining with magnetic gauge. | Record zinc thickness remaining. |
| **Galvanic interface (TA-01-1 IF-04)** | Remove one M10 bolt at reflector-to-mast interface. Inspect nylon bushing and mating surfaces for corrosion products. | No corrosion products at dissimilar metal interface. |

### 3.7 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| RCS degradation | <=1 dB at any measured angle | >1 dB degradation at any angle |
| Base metal corrosion (steel) | No red rust visible on any HDG steel surface | Red rust on any steel component |
| Base metal corrosion (aluminum) | No pitting through anodize layer on face plates or AM frames | Visible pitting to base metal |
| Galvanic corrosion at IF-04 | No corrosion products at steel/aluminum interface | Corrosion products present |
| GPS beacon operation | Transmitting at T=72h; position within +/-5 m | Not transmitting or position error >5 m |
| Bolt torque retention | >=80% of initial torque value on all bolted connections | <80% on any connection |
| Chain zinc coating | >=50 um zinc remaining (from initial >=85 um) | <50 um zinc remaining |

### 3.8 Data Recording Form (ATP-01-DF)

| Item | Pre-Test Value | Post-Test Value | Pass/Fail |
|------|---------------|----------------|-----------|
| RCS at 0 deg (dBsm) | ___ | ___ | ___ |
| RCS at 90 deg (dBsm) | ___ | ___ | ___ |
| RCS at 180 deg (dBsm) | ___ | ___ | ___ |
| RCS at 270 deg (dBsm) | ___ | ___ | ___ |
| Max RCS degradation (dB) | — | ___ | ___ |
| M6 bolt torque (sample 3 of 12) | ___ N-m | ___ N-m | ___ |
| M10 bolt torque (sample 2 of 4) | ___ N-m | ___ N-m | ___ |
| GPS transmitting at T=72h | — | YES / NO | ___ |
| GPS position error (m) | — | ___ | ___ |
| Red rust observed | — | YES / NO (location: ___) | ___ |
| Aluminum pitting observed | — | YES / NO (location: ___) | ___ |
| Chain zinc thickness (um) | ___ | ___ | ___ |
| **OVERALL ATP-01 RESULT** | | | **PASS / FAIL** |

Tested by: _________ Date: _________ Approved by: _________

### 3.9 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 5 days (1 day setup, 3 days exposure, 1 day post-inspection) |
| Estimated cost | $3,000 (chamber rental $1,500; RCS measurement $1,000; labor $500) |
| Facility | QUATEST 3 (HCMC) or VKT Materials Lab (Hanoi) |

---

## 4. ATP-02: Mooring Hardware Proof Load Test (EN 818-3 / API RP 2SK Adapted)

### 4.1 Objective and Requirements Traced

Verify that the complete mooring load path withstands proof load at SWL = 4,536 kgf (44,460 N) without permanent deformation.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| FOR-005 | Peak dynamic mooring load <=1,512 kgf | Load path carries 3x peak (SWL) |
| FOR-006 | Mooring system SWL >=4,536 kgf | Proof load held 5 min, no deformation |
| MAT-006 | G30 chain HDG | Chain links undamaged at SWL |

### 4.2 Test Articles

| Item | Description | Qty |
|------|-------------|-----|
| TA-02-1 | Complete mooring assembly: pad eye (20 mm eye plate + 200x200x14 mm backing plate + 4x M16 Gr 8.8 bolts) mounted on representative frame section, connected via shackle to 19 mm G30 chain (2 m sample) + shackle + swivel | 1 |

### 4.3 Equipment Required

| Equipment | Specification | Calibration |
|-----------|---------------|-------------|
| Hydraulic load frame or tensile test machine | Capacity >=100 kN (10,200 kgf) | Annual calibration |
| Calibrated load cell | 0-100 kN, Class 0.5 accuracy | Annual calibration |
| Dial indicator (deflection measurement) | 0-25 mm, 0.01 mm resolution | Annual calibration |
| Torque wrench | 50-250 N-m range | Annual calibration |
| Camera | >=12 MP | N/A |

### 4.4 Pre-Test Setup

1. **Assemble** pad eye to representative frame cross-member section using 4x M16 Gr 8.8 HDG bolts torqued to 190 +/-10 N-m.
2. **Mount** test fixture in hydraulic load frame: anchor backing plate side to fixed jaw; connect chain + shackle + swivel through pad eye ring to moving jaw.
3. **Install** dial indicator on backing plate to measure plate bending deflection during load.
4. **Torque-audit** and **record** all 4x M16 bolt torques.
5. **Photograph** complete test setup.
6. **Zero** load cell and dial indicator.

### 4.5 Test Execution

| Step | Action | Load (kN) | Duration |
|------|--------|-----------|----------|
| 1 | Apply preload to remove slack | 1.0 | 30 s |
| 2 | Load to 25% SWL (alignment check) | 11.1 | 60 s hold; verify load distribution even |
| 3 | Load to 50% SWL | 22.2 | 60 s hold; record deflection |
| 4 | Load to 75% SWL | 33.4 | 60 s hold; record deflection |
| 5 | **Load to 100% SWL (44.5 kN = 4,536 kgf)** | **44.5** | **5 minutes hold** |
| 6 | During 5-min hold: record load cell reading every 60 s; record deflection every 60 s; listen/watch for cracking, bolt loosening, yielding | — | — |
| 7 | Unload to zero | 0 | 60 s |
| 8 | Record residual deflection (permanent set) | 0 | After 5 min relaxation |

### 4.6 Post-Test Inspection

| Inspection | Method | Accept Criteria |
|------------|--------|----------------|
| Permanent deformation | Measure residual deflection on dial indicator | <=0.5 mm permanent set on backing plate |
| Eye plate | Visual + dimensional check for distortion at pin hole | No visible distortion; pin hole diameter unchanged +/-0.1 mm |
| Bolt torque | Re-torque all 4x M16 bolts; record break-away torque | >=170 N-m (>=90% of initial 190 N-m) |
| Weld inspection | Visual inspection of eye-to-backing plate full-penetration weld | No cracks, no weld toe cracking |
| Chain links | Visual inspection of 2 m chain sample | No link deformation, no visible damage |
| Swivel | Function check: rotate 360 deg under hand load | Free rotation, no binding |

### 4.7 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| Hold 44.5 kN for 5 min | Load maintained without drop >2% | Load drop >2% during hold |
| Permanent deformation | <=0.5 mm residual deflection | >0.5 mm residual deflection |
| Bolt torque retention | >=90% of initial torque | <90% on any bolt |
| Weld integrity | No cracks visible | Any crack at weld |
| Eye plate distortion | Pin hole within +/-0.1 mm of original | Measurable distortion |

### 4.8 Data Recording Form (ATP-02-DF)

| Parameter | Value |
|-----------|-------|
| Load cell reading at 100% SWL (kN) | ___ |
| Hold time at 100% SWL (min:sec) | ___ |
| Deflection at 25% SWL (mm) | ___ |
| Deflection at 50% SWL (mm) | ___ |
| Deflection at 75% SWL (mm) | ___ |
| Deflection at 100% SWL (mm) | ___ |
| Residual deflection after unload (mm) | ___ |
| M16 bolt #1 torque pre/post (N-m) | ___/___ |
| M16 bolt #2 torque pre/post (N-m) | ___/___ |
| M16 bolt #3 torque pre/post (N-m) | ___/___ |
| M16 bolt #4 torque pre/post (N-m) | ___/___ |
| Weld cracks observed | YES / NO |
| Pin hole diameter pre/post (mm) | ___/___ |
| **OVERALL ATP-02 RESULT** | **PASS / FAIL** |

Tested by: _________ Date: _________ Approved by: _________

### 4.9 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 2 days (1 day setup + fixture fabrication, 1 day test + inspection) |
| Estimated cost | $5,000 (load frame rental $2,500; fixture fabrication $1,500; labor $1,000) |
| Facility | University mechanical lab or shipyard test rig, capacity >=100 kN |

---

## 5. ATP-03: RCS Measurement (IALA 1093 Adapted)

### 5.1 Objective and Requirements Traced

Verify that the 8-reflector array achieves required RCS performance across 360 degrees at X-band.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| SIG-001 | RCS X-band peak combined | >=1,000 m2 (30 dBsm) |
| SIG-002 | RCS X-band 360-deg average | >=1,000 m2 |
| SIG-003 | RCS X-band 360-deg minimum | >=700 m2 (28.5 dBsm) |
| SIG-004 | RCS angular variation | <=+/-2 dB across 360 deg |
| QUA-001 | Each unit measured 360 deg | Production RCS verification |

### 5.2 Test Articles

| Item | Description | Qty |
|------|-------------|-----|
| TA-03-1 | Complete target: hull with frame, all 8 mast-reflector units installed in deck sockets with locking pins engaged | 1 |

### 5.3 Equipment Required

| Equipment | Specification | Calibration |
|-----------|---------------|-------------|
| X-band radar (transmitter + receiver) | 9.4 GHz (+/-0.1 GHz), calibrated power level | Annual calibration with reference target (metal sphere) |
| Reference target (calibration sphere) | Luneburg lens or metal sphere, known RCS (e.g., 1.0 m2) | Certified by manufacturer |
| Turntable or tow arrangement | Capable of 360-deg rotation at <=1 deg/s; supports >=2,000 kg | Level to +/-0.5 deg |
| Data acquisition system | Record amplitude vs. azimuth angle at >=1 sample/deg | — |
| Range marker | Distance >=100 m (far-field criterion: R >= 2D2/lambda, D=8 m, lambda=0.032 m; R_ff = 2x64/0.032 = 4,000 m ideal; 100 m acceptable for comparative measurement with calibration) | GPS-verified |
| Anemometer | Wind speed monitoring | — |
| Level (bubble or digital) | Platform level verification | — |

### 5.4 Pre-Test Setup

1. **Level** the target on turntable or floating in calm water. Verify platform level to +/-0.5 deg using bubble level at 4 quadrant positions.
2. **Verify** all 8 mast-reflector units installed: locking pins engaged, reflectors at correct height (~4.0 m AWL above turntable base).
3. **Calibrate** radar system using reference target at measurement range. Record calibration factor.
4. **Verify** test range is clear of reflective objects within +/-10 deg of measurement beam.
5. **Record** ambient conditions: temperature, wind speed (must be <15 m/s for measurement stability), humidity.
6. **Set** data acquisition to record RCS amplitude at 1-deg azimuth increments over 360 deg.

### 5.5 Test Execution

| Step | Action |
|------|--------|
| 1 | Position radar at designated range (>=100 m). Verify line-of-sight clear. |
| 2 | Rotate target (or rotate radar around stationary target) through 360 deg at <=1 deg/s. |
| 3 | Record RCS amplitude at each 1-deg increment (360 data points). |
| 4 | Repeat sweep in opposite direction for verification (total: 2 sweeps). |
| 5 | If any data anomaly, perform a third sweep. |
| 6 | Measure reference target (calibration sphere) at same range to confirm calibration stability. |

### 5.6 Post-Test Data Analysis

1. **Average** the two sweep datasets. Discard obvious outliers (multipath, interference).
2. **Convert** all amplitude values to RCS in m2 and dBsm using calibration factor.
3. **Calculate:**
   - Peak RCS: maximum value in 360-deg dataset
   - 360-deg average RCS: arithmetic mean of all 360 points (in linear m2, then convert to dBsm)
   - 360-deg minimum RCS: minimum value in dataset
   - Angular variation: max dBsm - min dBsm (in dB)
4. **Plot** RCS vs. azimuth polar plot.

### 5.7 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| Peak RCS | >=1,000 m2 (>=30.0 dBsm) | <1,000 m2 |
| 360-deg average RCS | >=1,000 m2 (>=30.0 dBsm) | <1,000 m2 |
| 360-deg minimum RCS | >=700 m2 (>=28.5 dBsm) | <700 m2 |
| Angular variation | <=4 dB (peak-to-trough) across full 360 deg | >4 dB variation |

### 5.8 Data Recording Form (ATP-03-DF)

| Parameter | Sweep 1 | Sweep 2 | Average | Pass/Fail |
|-----------|---------|---------|---------|-----------|
| Peak RCS (m2 / dBsm) | ___ | ___ | ___ | ___ |
| Peak RCS azimuth (deg) | ___ | ___ | — | — |
| 360-deg average RCS (m2 / dBsm) | ___ | ___ | ___ | ___ |
| 360-deg minimum RCS (m2 / dBsm) | ___ | ___ | ___ | ___ |
| Minimum RCS azimuth (deg) | ___ | ___ | — | — |
| Angular variation (dB) | ___ | ___ | ___ | ___ |
| Calibration sphere reading (m2) | ___ | ___ | ___ | — |
| Ambient temperature (deg C) | ___ | — | — | — |
| Wind speed (m/s) | ___ | — | — | — |
| **OVERALL ATP-03 RESULT** | | | | **PASS / FAIL** |

Tested by: _________ Date: _________ Approved by: _________

### 5.9 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 2 days (1 day setup + calibration, 1 day measurement + data analysis) |
| Estimated cost | $5,000 (range time $2,500; radar equipment $1,500; labor $1,000) |
| Facility | Military outdoor range (preferred) or university anechoic chamber; X-band 9.4 GHz capability; turntable >=8 m |

---

## 6. ATP-04: GPS Beacon Endurance Test

### 6.1 Objective and Requirements Traced

Verify that the GPS beacon operates continuously for >=72 hours at 1 Hz position acquisition and periodic Iridium SBD reporting.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| ENR-001 | GPS battery life >=72h | Transmitting at T=72h |
| ENR-002 | GPS transmit rate >=1 Hz | 1 Hz fix rate sustained |
| SIG-007 | Position accuracy <=+/-5 m CEP | CEP <=5 m over 72h |
| SIG-008 | Signal availability >=99% | Fix rate >=99% of 72h period |

### 6.2 Test Articles

| Item | Description | Qty |
|------|-------------|-----|
| TA-04-1 | Complete GPS beacon assembly (M6): GNSS module + Iridium SBD modem + Li-ion battery pack (20 Wh) + IP67 enclosure, fully sealed | 1 |

### 6.3 Equipment Required

| Equipment | Specification |
|-----------|---------------|
| Known reference position | Surveyed point with GPS coordinates known to +/-0.5 m |
| Iridium SBD monitoring dashboard | Shore station or cloud service receiving beacon messages |
| Battery voltage logger | External voltage tap or internal BMS logging at 1-min intervals |
| Temperature logger | Ambient temperature logging at 15-min intervals |
| Digital multimeter | For pre/post battery voltage check |
| Stopwatch or NTP-synced clock | Time reference |

### 6.4 Pre-Test Setup

1. **Verify** beacon is fully assembled with new/charged battery pack. Record initial battery voltage: ___ V.
2. **Place** beacon at known reference position outdoors with clear sky view (>=160 deg hemisphere).
3. **Power ON** beacon. Record start time T=0.
4. **Verify** first GPS fix acquired within 5 minutes. Record time to first fix (TTFF): ___ min.
5. **Verify** first Iridium SBD message received at shore station. Record first SBD time: ___.
6. **Configure** data logging: GPS position at 1 Hz (internal log); Iridium SBD at 60 s intervals; battery voltage at 1-min intervals.

### 6.5 Test Execution

| Step | Time | Action |
|------|------|--------|
| 1 | T=0h | Beacon activated. Logging begins. |
| 2 | T=1h | Check shore station: verify SBD messages receiving at 60 s intervals. |
| 3 | T=12h | Check shore station. Record battery voltage. |
| 4 | T=24h | Check shore station. Record battery voltage. Verify position accuracy. |
| 5 | T=48h | Check shore station. Record battery voltage. Verify position accuracy. |
| 6 | T=72h | **CRITICAL CHECK:** Verify beacon still transmitting. Record battery voltage. Download all logged data. |
| 7 | T=72h+ | Continue monitoring until beacon stops transmitting (battery depletion). Record total endurance time. |

### 6.6 Post-Test Analysis

1. **Calculate** total operational time from power-on to last valid GPS fix.
2. **Calculate** fix availability: (number of 1-sec epochs with valid fix) / (total 1-sec epochs in 72h = 259,200).
3. **Calculate** CEP: 50th percentile radial error from known reference position across all fixes.
4. **Plot** battery voltage vs. time curve; identify voltage cutoff point.
5. **Calculate** actual power consumption: 20 Wh / actual endurance (hours) = average power (W).

### 6.7 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| Endurance | >=72h continuous operation | <72h (battery depleted before 72h) |
| Fix rate | 1 Hz sustained for 72h | Sustained fix rate <1 Hz |
| Position accuracy | CEP <=5 m over 72h period | CEP >5 m |
| Fix availability | >=99% (<=2,592 missing fixes in 259,200 epochs) | <99% availability |
| Iridium SBD delivery | >=95% of scheduled SBD messages received at shore | <95% delivery rate |

### 6.8 Data Recording Form (ATP-04-DF)

| Parameter | Value | Pass/Fail |
|-----------|-------|-----------|
| Initial battery voltage (V) | ___ | — |
| Time to first fix (min) | ___ | — |
| Battery voltage at T=24h (V) | ___ | — |
| Battery voltage at T=48h (V) | ___ | — |
| Battery voltage at T=72h (V) | ___ | — |
| Total endurance (hours) | ___ | ___ |
| Fix availability (%) | ___ | ___ |
| CEP position error (m) | ___ | ___ |
| SBD delivery rate (%) | ___ | ___ |
| **OVERALL ATP-04 RESULT** | | **PASS / FAIL** |

Tested by: _________ Date: _________ Approved by: _________

### 6.9 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 4 days (72h continuous + 1 day data analysis) |
| Estimated cost | $500 (Iridium airtime $200; labor $300; no facility cost) |
| Facility | Any outdoor location with clear sky view (lab bench test acceptable with GPS antenna outdoors) |

---

## 7. ATP-05: Sea Trial -- 72h Anchored (MIL-STD-810H 514.8/512.6 Tailored)

### 7.1 Objective and Requirements Traced

Validate full-system survival at anchor for 72 hours in SS 5+ conditions.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| OPR-002 | Survival sea state SS 5-6 | No structural damage after 72h |
| OPR-003 | Survival wind Bft 6-7 | All components intact |
| OPR-004 | 72h endurance at anchor | Platform operational at T=72h |
| OPR-009 | Salt spray exposure 72h | No corrosion penetration |
| KIN-001 | Roll <=+/-7.5 deg SS 6 | Measured roll within limit |
| KIN-003 | 360-deg weathervaning | Free rotation observed |
| KIN-005 | Tow speed >=3 kn in SS 5 | Tow speed verified during transit |
| FOR-007 | Anchor holding >=1,500 kgf | No anchor drag during trial |
| FOR-010 | 40,000 cycle endurance | No fatigue cracks at mast base welds |

### 7.2 Test Articles

| Item | Description | Qty |
|------|-------------|-----|
| TA-05-1 | Complete first-article THANH TRI-H target, fully assembled with hull, frame, 8x mast-reflector units, GPS beacon, mooring kit, tow kit | 1 |

### 7.3 Equipment Required

| Equipment | Specification |
|-----------|---------------|
| Support vessel | >=15 m, capable of SS 5 operations, with deck crane or A-frame |
| Echo sounder | Depth measurement at deployment site |
| Weather monitoring station | Wind speed/direction, wave height (Hs), temperature |
| Strain gauges (bonded) | 2x gauges on mast #1 base gusset (axial + transverse) |
| Strain gauge data logger | 48-channel min, waterproof, battery-powered 72h |
| GPS beacon monitoring | Shore-based Iridium SBD dashboard |
| Portable X-band radar | 9.4 GHz for pre/post RCS spot check |
| Camera (waterproof) | Documentation of all phases |
| Torque wrench set | 1-50 N-m and 50-250 N-m |
| Marine VHF radio | Communications |

### 7.4 Pre-Test Setup

1. **Select** deployment site: designated Navy test area, 15-50 m depth, sand/hard bottom confirmed by chart or survey. Target SS 5 conditions during trial window.
2. **Install** strain gauges on mast #1 base gusset weld toes (2 gauges: axial bending + transverse). Connect to waterproof data logger mounted at hull deck level.
3. **Pre-deploy** mooring: anchor + chain + rode at site per Mooring Kit B (30 m depth) or appropriate kit. Set anchor at 2x working load from support vessel. Verify holding with GPS position monitoring for 30 minutes.
4. **Measure** pre-deployment: hull OD at 4 positions, draft at 4 positions, mast alignment angles (8x, using digital inclinometer).
5. **Measure** pre-deployment RCS: spot check at 4 cardinal angles (0, 90, 180, 270 deg) using portable radar from support vessel at 200 m range.
6. **Torque-audit** all bolted connections: 3 sample M6 face bolts, 3 sample M10 IF-04 bolts, all 8 locking pins verified engaged.
7. **Activate** GPS beacon and verify shore station receiving.
8. **Activate** strain gauge data logger. Record start time.

### 7.5 Test Execution

| Day | Action |
|-----|--------|
| **Day 1 (Deploy)** | Tow target to deployment site. Record tow speed (target >=3 kn in SS 5). Connect mooring at pre-deployed buoy. Erect all 8 masts if transported flat. Verify GPS, strain logger, and mooring connection. Support vessel departs to minimum 500 m standoff. |
| **Day 2 (Monitor)** | Monitor from shore via GPS beacon SBD every 60 s. Record: position (drift indicates anchor drag), wind/wave conditions from nearby met station. Support vessel conducts visual inspection pass at 200 m (photograph target from 4 sides). |
| **Day 3 (Monitor)** | Continue monitoring. Support vessel conducts second visual pass if conditions permit. Weather window monitoring: if SS exceeds 7, abort criteria apply (notify range safety). |
| **Day 4 (Recover)** | At T=72h: support vessel approaches target. Crew boards target deck. Perform ON-TARGET inspection before recovery. Disconnect mooring. Recover target to support vessel or tow to port. |

### 7.6 Post-Test Inspection (On-Target at T=72h Before Recovery)

| Inspection | Method | Accept Criteria |
|------------|--------|----------------|
| Visual -- all 8 masts | Walk around deck, inspect mast base welds, gussets, locking pins | No cracks, no loose pins, no visible damage |
| Visual -- hull | Inspect hull surface, section joint (IF-07), scuppers | No hull damage, no leaks, no delamination |
| Visual -- mooring | Inspect pad eye, shackle, chain topside, swivel | No deformation, shackle pin secure |
| Torque audit | Sample 3x M10 IF-04 bolts, 3x M6 face bolts | >=80% of initial torque retained |
| Draft measurement | Measure draft at 4 positions | Draft unchanged +/-5 mm from pre-deploy (no water ingress) |
| Mast alignment | Digital inclinometer on 8 masts | Alignment within +/-0.5 deg of pre-deploy |
| GPS beacon | Verify still transmitting at T=72h | Transmitting, position within +/-5 m |
| Strain logger | Recover data logger; download data | Data captured for full 72h |

### 7.7 Post-Recovery Inspection (Ashore)

| Inspection | Method | Accept Criteria |
|------------|--------|----------------|
| RCS spot check | Repeat 4-angle RCS measurement | <=1 dB degradation from pre-deploy |
| NDT -- mast base welds | Dye penetrant inspection (DPI) on 8 mast base gusset welds | No crack indications |
| Strain data analysis | Plot stress range vs. cycle count; compare to FAT 56 allowable | Max stress range <=206 MPa at accumulated cycles |
| Reflector orthogonality | CMM measurement on 2 sample reflectors | Within +/-0.10 deg of 90 deg on all face pairs |
| Mooring hardware | Visual + dimensional check of chain links, shackle pins, swivel | No deformation, no wear exceeding 5% of nominal diameter |
| Anchor inspection | Inspect flukes, shank; measure shank straightness | No bent flukes, shank straight +/-2 deg |

### 7.8 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| 72h survival | Target intact and floating at T=72h | Structural failure, capsize, sinking, or anchor drag >500 m |
| No structural cracks | DPI clean on all 8 mast base welds | Any crack indication |
| RCS maintenance | <=1 dB degradation from pre-deploy | >1 dB degradation |
| Draft unchanged | +/-5 mm of pre-deploy | >5 mm change (water ingress) |
| Mast alignment | Within +/-0.5 deg of pre-deploy | >0.5 deg shift on any mast |
| Bolt retention | >=80% torque retained on all sampled bolts | <80% on any bolt |
| GPS operational at T=72h | Transmitting with +/-5 m accuracy | Not transmitting or >5 m error |
| Strain range | Below FAT 56 allowable for accumulated cycles | Exceeds fatigue allowable |
| Tow speed (Day 1 transit) | >=3.0 kn sustained in SS 5 | <3.0 kn sustained |

### 7.9 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 5 days (1 day deploy, 3 days anchored, 1 day recover + initial inspection) + 2 days ashore inspection |
| Estimated cost | $8,000 (support vessel charter $4,000; strain gauges/logger $1,500; labor $2,000; consumables $500) |
| Facility | Navy-designated test range, 15-50 m depth, SS 5 access. 4 weeks advance coordination required. |

---

## 8. ATP-06: Deployment Exercise

### 8.1 Objective and Requirements Traced

Verify that a 4-person crew can deploy the target within time limits using tool-free connections.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| ERG-001 | Max crew <=4 personnel | No more than 4 crew on target |
| ERG-002 | Deployment time <=30 min (excl. tow) | Timed drill <=30 min |
| ERG-005 | Tool-free connections | Shackle key only tool used |
| ASM-001 | 8 reflector assembly <=4h (factory) | Reflector mount timing |
| ASM-006 | 8 masts erected <=15 min | Timed mast erection |
| SAF-001 | Min 5 km clearance during engagement | Verified by procedure |
| MNT-002 | Mooring recoverable for reuse | Recovery exercise included |
| MNT-003 | Pre-deployment inspection <=1h | Timed inspection |
| OPR-001 | Deployment in SS 4-5 | Conditions recorded |

### 8.2 Test Articles

| Item | Description | Qty |
|------|-------------|-----|
| TA-06-1 | Complete THANH TRI-H target, pre-assembled hull + frame, with 8x M5 units stored on vessel deck | 1 |
| TA-06-2 | Pre-deployed mooring (anchor + chain + rode + surface buoy) | 1 |

### 8.3 Equipment Required

| Equipment | Specification |
|-----------|---------------|
| Support vessel | >=12 m, with working deck, in sheltered water (SS 2-3) |
| Stopwatch | Digital, lap timer function |
| Video camera | Full recording of deployment exercise |
| Wind gauge | Anemometer for wind speed at test time |
| PPE | Life jackets, hard hats, non-skid footwear, gloves for all crew |

### 8.4 Pre-Test Setup

1. **Pre-deploy** mooring at exercise site (calm water, harbor or sheltered bay).
2. **Load** target hull + frame on support vessel deck or tow alongside.
3. **Load** 8x M5 mast-reflector units in vertical padded rack on vessel deck.
4. **Brief** 4-person crew on deployment sequence D-01 through D-18 per [[../03_embodiment/OCP_P15_production_planning.md]] Section 6.
5. **Start** video recording.

### 8.5 Test Execution

| Step | Timed Phase | Description | Time Limit |
|------|-------------|-------------|------------|
| 1 | Pre-deployment inspection | Crew inspects hull, masts, GPS, mooring hardware per checklist | <=60 min |
| 2 | Launch target | Float hull from vessel ramp or crane lift | Record time |
| 3 | Connect mooring | Pick up mooring buoy, shackle to pad eye (IF-02), mouse shackle pin | <=10 min |
| 4 | Erect 8 masts | Transfer M5 units from vessel, insert into deck sockets, engage locking pins, clip R-clips | <=15 min (target) |
| 5 | Verify GPS | Power on GPS beacon, confirm fix and SBD received at shore | <=5 min |
| 6 | Final visual check | Walk-around of all 8 masts, pin check, mooring check | <=5 min |
| 7 | Clear target | Crew returns to vessel; vessel departs | Record time |
| 8 | **TOTAL on-target time (Steps 3-7)** | — | **<=30 min** |
| 9 | Recovery exercise | Return to target; disconnect mooring; lower 8 masts; recover to vessel | Record time |

### 8.6 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| Crew size | <=4 personnel for all on-target tasks | >4 personnel required |
| On-target deployment time (Steps 3-7) | <=30 min | >30 min |
| Mast erection time (Step 4) | <=20 min (WISH: <=15 min) | >20 min |
| Tool-free connections | Only shackle key used (no wrenches, no power tools) | Power tools or wrenches required for field connections |
| All pins engaged | 8/8 locking pins visually confirmed | Any pin not engaged |
| GPS functional | Fix acquired <5 min, SBD received | No fix or no SBD within 5 min |
| Recovery exercise | Mooring disconnected, all masts lowered, target recovered | Unable to recover mooring or masts |

### 8.7 Data Recording Form (ATP-06-DF)

| Phase | Start Time | End Time | Duration | Notes |
|-------|-----------|----------|----------|-------|
| Pre-deploy inspection | ___ | ___ | ___ | ___ |
| Target launch | ___ | ___ | ___ | ___ |
| Mooring connection | ___ | ___ | ___ | ___ |
| Mast erection (8x) | ___ | ___ | ___ | ___ |
| GPS verification | ___ | ___ | ___ | ___ |
| Final walk-around | ___ | ___ | ___ | ___ |
| Crew departs target | ___ | — | — | ___ |
| **Total on-target (Steps 3-7)** | ___ | ___ | **___** | ___ |
| Recovery exercise | ___ | ___ | ___ | ___ |
| Crew size used | ___ persons | | | |
| Sea state at test | SS ___ | Wind ___ m/s | | |
| **OVERALL ATP-06 RESULT** | | | | **PASS / FAIL** |

Tested by: _________ Date: _________ Approved by: _________

### 8.8 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 1 day (multiple deployment/recovery cycles) |
| Estimated cost | $3,000 (support vessel $1,500; crew labor $1,000; consumables $500) |
| Facility | Calm water harbor or sheltered bay, SS 2-3, with boat ramp or crane access |

---

## 9. ATP-07: AM Frame Qualification (ASTM F3301/F3318)

### 9.1 Objective and Requirements Traced

Qualify the LPBF AM process and AlSi10Mg material for reflector frame production.

| Requirement | Description | Acceptance Criterion |
|-------------|-------------|---------------------|
| MAT-004 | AlSi10Mg LPBF + T5 | Mechanical properties meet ASTM F3318 |
| SIG-009 | Orthogonality <=+/-0.1 deg | CMM-verified on qualification frames |
| PRD-003 | >=2 qualified AM bureaus | First-article inspection of qualification frames |

### 9.2 Test Articles

| Item | Description | Qty |
|------|-------------|-----|
| TA-07-1 | Tensile test coupons, AlSi10Mg, from qualification build plate: X, Y, Z orientations | 3 per orientation = 9 coupons |
| TA-07-2 | Qualification AM frames, fully post-processed (T5 + CNC + Type III hard anodize) | 3 frames |
| TA-07-3 | Powder certification sample | 1 lot |

### 9.3 Equipment Required

| Equipment | Specification |
|-----------|---------------|
| Universal tensile test machine | >=100 kN capacity, ASTM E8 compliant |
| Extensometer | 25 mm gauge length, Class B-1 |
| Industrial CT scanner | Resolution <=0.1 mm voxel |
| CMM (Coordinate Measuring Machine) | Accuracy <=0.005 mm |
| Rockwell/Vickers hardness tester | HRB or HV scale |
| Eddy-current coating gauge | For Type III anodize thickness |
| Surface roughness tester | Profilometer, Ra measurement |
| Laser diffraction analyzer | Powder PSD (D10, D50, D90) |

### 9.4 Pre-Test: Powder Certification (TA-07-3)

| Check | Method | Accept Criteria | Standard |
|-------|--------|----------------|----------|
| Chemical composition | Review Certificate of Analysis (CoA) | Si: 9.0-11.0%; Mg: 0.25-0.45%; Fe: <=0.55%; balance Al | ASTM B937 |
| Particle size distribution | Laser diffraction (ASTM B822) or CoA | D10: 15-25 um; D50: 30-45 um; D90: 50-70 um | ASTM F3301 Sec 6 |
| Apparent density | Hall flowmeter (ASTM B212) or CoA | >=1.3 g/cm3 | ASTM F3301 Sec 6 |
| Flowability | Hall flow (ASTM B213) or CoA | <=30 s / 50 g | ASTM F3301 Sec 6 |
| Moisture content | Karl Fischer or CoA | <=0.05% by weight | ASTM F3301 Sec 6 |
| Recycled ratio | Build report documentation | <=30% recycled powder | AM bureau SOP |

### 9.5 Test Execution: Tensile Coupons (TA-07-1)

| Step | Action |
|------|--------|
| 1 | Receive 9 tensile coupons from AM bureau (3x X-direction, 3x Y-direction, 3x Z-direction), all from same build plate as qualification frames. |
| 2 | Verify coupon geometry per ASTM E8 (sub-size specimen: 25 mm gauge length, 6 mm width, 3 mm thickness). |
| 3 | Install coupon in tensile machine with extensometer. |
| 4 | Apply tensile load at 1 mm/min crosshead speed per ASTM E8. |
| 5 | Record: yield strength (0.2% offset), ultimate tensile strength, elongation at fracture. |
| 6 | Repeat for all 9 coupons. |

### 9.6 Test Execution: CT Scan (TA-07-2)

| Step | Action |
|------|--------|
| 1 | CT-scan all 3 qualification frames at <=0.1 mm voxel resolution. |
| 2 | Analyze scans for: internal voids >=1.0 mm diameter, layer delamination, unmelted powder pockets, support removal completeness. |
| 3 | Report all defects found with location, size, and classification. |

### 9.7 Test Execution: Dimensional and Orthogonality (TA-07-2)

| Step | Action |
|------|--------|
| 1 | CMM measurement of all 3 face-mounting surfaces on each of 3 frames (9 surface measurements). |
| 2 | Calculate angle between each face pair (AB, BC, AC) for each frame (9 angle measurements). |
| 3 | Measure bolt hole positions and dowel hole positions against CAD nominal. |
| 4 | Measure overall envelope dimensions. |
| 5 | Measure surface roughness on machined datums (profilometer). |
| 6 | Measure Type III hard anodize thickness (eddy-current gauge, 3 points per frame). |
| 7 | Measure hardness (3 points per frame, Rockwell B or Vickers HV). |

### 9.8 Pass/Fail Criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| Yield strength (XY) | >=230 MPa (all 6 XY coupons) | Any coupon <230 MPa |
| Yield strength (Z) | >=210 MPa (all 3 Z coupons) | Any coupon <210 MPa |
| UTS | >=350 MPa (all 9 coupons) | Any coupon <350 MPa |
| Elongation | >=5% (all 9 coupons) | Any coupon <5% |
| CT internal defects | No voids >=1.0 mm diameter | Any void >=1.0 mm |
| Layer delamination | None detected | Any delamination |
| Orthogonality | All 9 face-pair angles within 90.00 +/-0.10 deg | Any angle outside +/-0.10 deg |
| Dowel hole position | Within +/-0.05 mm of nominal | Any hole >0.05 mm off |
| Hard anodize thickness | >=25 um on all measurement points | Any point <25 um |
| Hardness | HRB 65-85 (or HV 100-130) | Outside range |
| Machined surface roughness | Ra <=3.2 um on datums | Ra >3.2 um |
| Powder certification | All parameters within specification | Any parameter out of spec |

### 9.9 Data Recording Form (ATP-07-DF)

**Tensile Coupons:**

| Coupon ID | Orientation | sigma_y (MPa) | sigma_UTS (MPa) | Elongation (%) | Pass/Fail |
|-----------|-------------|---------------|-----------------|----------------|-----------|
| X-1 | X | ___ | ___ | ___ | ___ |
| X-2 | X | ___ | ___ | ___ | ___ |
| X-3 | X | ___ | ___ | ___ | ___ |
| Y-1 | Y | ___ | ___ | ___ | ___ |
| Y-2 | Y | ___ | ___ | ___ | ___ |
| Y-3 | Y | ___ | ___ | ___ | ___ |
| Z-1 | Z | ___ | ___ | ___ | ___ |
| Z-2 | Z | ___ | ___ | ___ | ___ |
| Z-3 | Z | ___ | ___ | ___ | ___ |

**Orthogonality (3 frames x 3 face pairs):**

| Frame | Face Pair AB (deg) | Face Pair BC (deg) | Face Pair AC (deg) | Pass/Fail |
|-------|-------------------|-------------------|-------------------|-----------|
| F-01 | ___ | ___ | ___ | ___ |
| F-02 | ___ | ___ | ___ | ___ |
| F-03 | ___ | ___ | ___ | ___ |

**OVERALL ATP-07 RESULT:** **PASS / FAIL**

Tested by: _________ Date: _________ Approved by: _________

### 9.10 Test Duration and Cost

| Parameter | Value |
|-----------|-------|
| Total duration | 3 weeks (1 week AM build + 1 week post-processing + 1 week testing and reporting) |
| Estimated cost | $3,500 (AM frames + coupons $2,000; tensile testing $500; CT scan $500; CMM $300; labor $200) |
| Facility | AM bureau (build + post-process) + mechanical test lab + CT lab + metrology lab |

---

## 10. Production Acceptance Test Procedures

### ATP-PA-01: System Mass

| Parameter | Detail |
|-----------|--------|
| **Requirement** | GEO-007: <=1,100 kg total displacement |
| **Method** | Weigh complete unit on floor scale or crane scale (hull + frame + 8x M5 units + GPS + all fasteners, excluding mooring and tow kits) |
| **Equipment** | Floor scale or crane scale, rated >=2,000 kg, calibrated +/-2 kg |
| **Procedure** | (1) Zero scale. (2) Place/hang fully assembled target on scale. (3) Record mass. |
| **Pass** | <=1,100 kg |
| **Fail** | >1,100 kg |
| **Frequency** | 100% of units |
| **QC hold point** | YES -- reject if >1,100 kg |

### ATP-PA-02: Hull Dimensional

| Parameter | Detail |
|-----------|--------|
| **Requirements** | GEO-001: 8.0 m +/-0.1 m diameter; GEO-002: 0.5 m +/-0.05 m depth |
| **Method** | Tape measure across 4 diametrically opposed positions; depth measured at 4 quadrant points |
| **Equipment** | 10 m steel tape measure, spirit level |
| **Procedure** | (1) Measure OD at 0-180 deg, 45-225 deg, 90-270 deg, 135-315 deg. (2) Measure hull depth at 0 deg, 90 deg, 180 deg, 270 deg. (3) Record all 8 values. |
| **Pass** | All diameters 7,900-8,100 mm; all depths 450-550 mm |
| **Fail** | Any measurement outside tolerance |
| **Frequency** | 100% of units |

### ATP-PA-03: Hydrostatic Leak Test

| Parameter | Detail |
|-----------|--------|
| **Requirement** | Hull integrity at IF-07 (section joint) and all hull penetrations |
| **Method** | Float hull in test tank or harbor for 4 hours; inspect for leaks |
| **Equipment** | Test tank or harbor slip access; visual |
| **Procedure** | (1) Launch hull (assembled with frame, before mast installation). (2) Float for 4 hours minimum. (3) Inspect hull section joint (IF-07), all bolt penetrations, scupper drains, and foam fill ports for water ingress. (4) Measure draft at 4 positions before and after; compare to detect water ingress by draft increase. |
| **Pass** | No visible water ingress; draft unchanged +/-3 mm over 4 hours |
| **Fail** | Visible water leak at any point OR draft increase >3 mm |
| **Frequency** | 100% of units |
| **QC hold point** | YES -- reject if leak detected; repair and re-test |

### ATP-PA-04: Mast Socket Fit Test

| Parameter | Detail |
|-----------|--------|
| **Requirement** | IF-03: all 8 masts insert smoothly, locking pin engages |
| **Method** | Insert each of 8 mast-reflector units into deck sockets; verify fit, pin, and retention |
| **Equipment** | 8x M5 mast-reflector units, clevis pins, R-clips |
| **Procedure** | (1) For each of 8 sockets: insert mast tube into socket (should slide in with hand force only). (2) Push mast down until base plate seats on socket flange (verify contact, no gap). (3) Align locking pin holes. (4) Insert M12 clevis pin through both walls (should insert with hand force or light tap). (5) Engage R-clip. (6) Attempt to pull mast upward by hand -- verify pin holds. (7) Record pass/fail for each socket. |
| **Pass** | All 8 masts insert with 1.0-1.5 mm radial clearance; all 8 pins engage fully; base plates seat on flanges |
| **Fail** | Any mast does not insert (interference) or pin does not engage (misalignment) |
| **Frequency** | 100% of units |

### ATP-PA-05: 360-deg RCS Measurement (Production Protocol)

| Parameter | Detail |
|-----------|--------|
| **Requirements** | SIG-001: peak >=1,000 m2; SIG-002: avg >=1,000 m2; SIG-003: min >=700 m2; SIG-004: variation <=+/-2 dB |
| **Method** | Per ATP-03 procedure, adapted for production throughput |
| **Equipment** | Portable X-band radar (9.4 GHz); turntable or tow rotation; data logger |
| **Procedure** | (1) Install all 8 M5 units. (2) Rotate through 360 deg, record RCS at 5-deg increments (72 points; reduced from 1-deg for production speed). (3) Calculate peak, average, minimum, variation. |
| **Pass** | Peak >=1,000 m2; average >=1,000 m2; minimum >=700 m2; variation <=4 dB |
| **Fail** | Any SIG criterion not met |
| **Frequency** | 100% of units |
| **QC hold point** | YES -- reject if any SIG requirement fails; diagnose and rework reflector alignment |

### ATP-PA-06: GPS Beacon Function

| Parameter | Detail |
|-----------|--------|
| **Requirements** | SIG-007: position <=+/-5 m CEP; ENR-002: 1 Hz fix |
| **Method** | Power on GPS beacon at known reference position; verify fix and Iridium SBD |
| **Equipment** | Known reference position (surveyed), Iridium SBD monitoring account |
| **Procedure** | (1) Mount GPS beacon on mast (or test bracket). (2) Power ON. (3) Start timer. (4) Wait for GPS fix (must be <5 min). (5) Record reported position; compare to reference. (6) Verify Iridium SBD message received at shore station. (7) Record position error (m). |
| **Pass** | GPS fix <5 min; position error <=5 m from reference; SBD message received |
| **Fail** | No fix within 5 min OR position error >5 m OR SBD not received |
| **Frequency** | 100% of units |
| **QC hold point** | YES -- reject beacon if no fix or no SBD |

### ATP-PA-07: Visual Inspection (Comprehensive Checklist)

Inspect all of the following items. Record pass/fail for each.

| # | Item | Accept Criteria |
|---|------|----------------|
| 1 | Hull surface condition | No cracks, gouges, delamination >5 mm depth |
| 2 | Hull section joint (IF-07) | Sealant bead continuous, all 24x M10 bolts torqued and marked |
| 3 | Frame welds (visible) | No cracks, porosity, or undercut visible at weld toes |
| 4 | HDG coating (frame + masts) | No bare spots, no red rust, coating intact |
| 5 | Anodize (face plates) | No scratches through anodize layer on reflective surfaces |
| 6 | Anodize (AM frames) | Hard anodize intact, dark grey/black, no flaking |
| 7 | All safety wire | Present on all reflector bolt pairs (48 wire loops) and IF-04 bolt pairs (16 wire loops) |
| 8 | Nylock nuts | Present and engaged on all bolted connections |
| 9 | Galvanic isolation (IF-04) | Nylon bushings visible at all 32 bolt positions |
| 10 | Locking pin lanyards | 8/8 pins have wire lanyards attached to base plates |
| 11 | GPS enclosure seal | Enclosure sealed, cable glands tight, desiccant packs inside |
| 12 | Identification markings | Project code, serial number, mass, manufacture date legible |
| 13 | Reflective tape (SOLAS) | Applied at 4 quadrants on hull perimeter |
| 14 | Zinc anode | Installed adjacent to pad eye, bolt tight |

**Pass:** All 14 items satisfactory. **Fail:** Any item unsatisfactory -- correct and re-inspect.

**Frequency:** 100% of units.

### ATP-PA-08: Documentation Verification

All of the following documents must be present in the unit documentation package before release.

| # | Document | Source |
|---|----------|--------|
| 1 | Hull material certificate (HDPE PE100, ASTM D3350) | Hull supplier |
| 2 | Steel mill certificate (S235, EN 10025-2) | Steel supplier |
| 3 | Aluminum mill certificate (6061-T6, ASTM B209) | Al supplier |
| 4 | AM build report (powder lot, process parameters, heat treat) | AM bureau |
| 5 | AM tensile test certificate (ASTM E8/F3318) | AM bureau or test lab |
| 6 | HDG coating certificates (frame, masts, chain) | HDG plant |
| 7 | Type II anodize certificate (face plates) | Anodizer |
| 8 | Type III hard anodize certificate (AM frames) | Anodizer |
| 9 | Pad eye weld UT inspection report | QC inspector |
| 10 | Reflector orthogonality measurement records (8 reflectors, 24 angle measurements) | CMM operator |
| 11 | RCS test data and polar plot | Test engineer |
| 12 | GPS beacon function test record | Test technician |
| 13 | System mass record | QC inspector |
| 14 | Hydrostatic leak test record | QC inspector |
| 15 | Fastener torque records (IF-01, IF-02, IF-04) | Assembly technician |
| 16 | Final visual inspection checklist (ATP-PA-07) | QC inspector |
| 17 | Deployment manual (pictorial, VN/EN) | Engineering |

**Pass:** All 17 documents present and complete. **Fail:** Any document missing -- unit not released.

**Frequency:** 100% of units. **QC hold point:** YES -- unit not released without complete documentation.

---

## 11. Test Sequence and Dependencies

### 11.1 Qualification Test Sequence

```
QUALIFICATION TEST PROGRAM SCHEDULE
════════════════════════════════════════════════════════════════

Week 1:  [ATP-07 Start] AM qualification: build plate at AM bureau
         [ATP-01 Start] Salt fog: load specimens, begin 72h exposure
         [ATP-04 Start] GPS endurance: power on, begin 72h test

Week 2:  [ATP-01 Complete] Post-test inspection: visual, RCS, torque
         [ATP-04 Complete] GPS data review: availability, battery EOL
         [ATP-07 Continue] AM: heat treatment, post-machining, CT scan

Week 3:  [ATP-02] Mooring proof load: setup, apply 44,460 N, hold 5 min
         [ATP-07 Complete] AM: tensile testing, CMM, dimensional report

         ┌─────────────────────────────────────────────────────────┐
         │ DECISION GATE 1: ATP-01, ATP-02, ATP-04, ATP-07 PASS?  │
         │   YES --> proceed to ATP-03 and ATP-05                  │
         │   NO  --> resolve failures, retest before proceeding    │
         └─────────────────────────────────────────────────────────┘

Week 4:  [ATP-03] RCS measurement: 360-deg sweep at 9.4 GHz
         Pass: >=1,000 m2 avg, >=700 m2 min, <=+/-2 dB

Weeks 5-7: [ATP-05] Sea trial: deploy, 72h anchored at SS 5+, recover
         Day 1: Deploy and connect mooring
         Days 2-3: 72h monitoring (GPS, strain, weather)
         Day 4: Recovery and on-target inspection
         Days 5-7: Ashore inspection (DPI, RCS, CMM, strain analysis)

         ┌─────────────────────────────────────────────────────────┐
         │ DECISION GATE 2: ATP-03 and ATP-05 PASS?               │
         │   YES --> proceed to ATP-06                             │
         │   NO  --> root cause analysis, redesign if needed       │
         └─────────────────────────────────────────────────────────┘

Week 8:  [ATP-06] Deployment exercise: full crew drill, timing
         Pass: <=30 min, <=4 crew, tool-free connections

         ┌─────────────────────────────────────────────────────────┐
         │ DECISION GATE 3: ALL 7 QUALIFICATION TESTS PASS?       │
         │   YES --> PRODUCTION RELEASE AUTHORIZED                 │
         │   NO  --> Remediate and retest failed procedures        │
         └─────────────────────────────────────────────────────────┘
```

### 11.2 Prerequisites Chain

| Test | Prerequisites | Rationale |
|------|---------------|-----------|
| ATP-07 (AM qualification) | None | Must qualify AM process before producing reflector frames |
| ATP-01 (salt fog) | None | Can run in parallel with ATP-07 on pre-production articles |
| ATP-04 (GPS endurance) | None | Can run in parallel with ATP-01 and ATP-07 |
| ATP-02 (proof load) | None | Can run in parallel with Weeks 1-2 tests |
| ATP-03 (RCS measurement) | ATP-07 PASS | Requires qualified AM frames for first-article reflectors |
| ATP-05 (sea trial) | ATP-01, ATP-02, ATP-04 PASS | Must verify corrosion, mooring, and GPS before ocean deployment |
| ATP-06 (deployment exercise) | ATP-03, ATP-05 PASS | Must verify RCS performance and sea survival before operational demo |

---

## 12. Test Equipment List

### 12.1 Master Equipment Register

| # | Equipment | Specification | Qty | Calibration Cycle | Est. Cost |
|---|-----------|---------------|-----|-------------------|-----------|
| TE-01 | Salt fog chamber (ASTM B117) | >=1.5 m3, temp-controlled | 1 (rental) | Annual | $1,500/test |
| TE-02 | Hydraulic load frame | >=100 kN | 1 (rental) | Annual | $2,500/test |
| TE-03 | Calibrated load cell | 0-100 kN, Class 0.5 | 1 | Annual | $200 |
| TE-04 | Portable X-band radar | 9.4 GHz, calibrated | 1 | Annual | $2,500/test |
| TE-05 | Reference target (cal sphere) | Known RCS +/-0.5 dB | 1 | Certified | $500 |
| TE-06 | Turntable (RCS measurement) | 360 deg, <=1 deg/s, >=2,000 kg | 1 (rental) | Level verified | $1,000/test |
| TE-07 | Strain gauges + data logger | 48-channel, waterproof, 72h battery | 1 set | Calibrate before use | $1,500 |
| TE-08 | CMM | Accuracy <=0.005 mm | 1 (outsource) | Annual | $300/session |
| TE-09 | Tensile test machine | >=100 kN, ASTM E8 | 1 (outsource) | Annual | $500/session |
| TE-10 | Industrial CT scanner | <=0.1 mm voxel | 1 (outsource) | Annual | $500/session |
| TE-11 | Torque wrench set | 1-20 N-m, 20-100 N-m, 50-250 N-m | 3 | Annual | $200 |
| TE-12 | Magnetic coating gauge | >=1,000 um range | 1 | Annual | $100 |
| TE-13 | Eddy-current coating gauge | Anodize thickness | 1 | Annual | $150 |
| TE-14 | Digital angle gauge | 0-360 deg, 0.05 deg resolution | 1 | Annual | $100 |
| TE-15 | Surface roughness tester | Ra 0.01-100 um | 1 | Annual | $200 |
| TE-16 | Floor scale | 0-2,000 kg, +/-2 kg | 1 | Annual | $100 |
| TE-17 | UT flaw detector | AWS D1.1 compliant | 1 (outsource) | Annual | $300/session |
| TE-18 | pH meter | 0-14, +/-0.1 | 1 | Before test | $50 |
| TE-19 | DPI kit | Dye penetrant inspection set | 1 | N/A | $100 |
| TE-20 | Iridium SBD account | Monitoring dashboard | 1 | N/A | $200/yr |

### 12.2 Calibration Requirements

All test equipment must be calibrated by an accredited laboratory (ISO/IEC 17025) within the calibration cycle shown above. Calibration certificates must be available at the test facility during test execution and included in the test report.

---

## 13. Test Program Budget

### 13.1 Qualification Test Program (First Article)

| Test ID | Title | Est. Cost | Duration |
|---------|-------|-----------|----------|
| ATP-01 | Salt Fog Test | $3,000 | 5 days |
| ATP-02 | Mooring Proof Load | $5,000 | 2 days |
| ATP-03 | RCS Measurement | $5,000 | 2 days |
| ATP-04 | GPS Endurance | $500 | 4 days |
| ATP-05 | Sea Trial 72h | $8,000 | 7 days |
| ATP-06 | Deployment Exercise | $3,000 | 1 day |
| ATP-07 | AM Qualification | $3,500 | 3 weeks |
| | **QUALIFICATION TOTAL** | **$28,000** | **8 weeks** |

### 13.2 Production Acceptance Tests (Per Unit)

| Test ID | Title | Est. Cost/Unit | Notes |
|---------|-------|---------------|-------|
| ATP-PA-01 | System Mass | $20 | Scale time + labor |
| ATP-PA-02 | Hull Dimensional | $30 | Measurement labor |
| ATP-PA-03 | Hydrostatic Leak | $100 | Harbor/tank access + 4h labor |
| ATP-PA-04 | Mast Socket Fit | $30 | 30 min labor |
| ATP-PA-05 | 360-deg RCS | $500 | Radar time + setup + analysis |
| ATP-PA-06 | GPS Function | $20 | 15 min labor + Iridium airtime |
| ATP-PA-07 | Visual Inspection | $50 | 1h QC labor |
| ATP-PA-08 | Documentation | $50 | 1h document review |
| | **PRODUCTION TOTAL (per unit)** | **$800** | |

### 13.3 Periodic Tests (Amortized Per Unit)

| Test ID | Title | Frequency | Cost/Occurrence | Amortized/Unit |
|---------|-------|-----------|----------------|----------------|
| ATP-02P | Pad Eye Proof Load | Every 10th unit | $1,500 | $150 |
| ATP-04P | GPS 72h Endurance | Every 5th unit | $300 | $60 |
| | **PERIODIC TOTAL (amortized)** | | | **$210** |

### 13.4 Total Test Program Cost

| Element | Cost |
|---------|------|
| Qualification program (one-time) | $28,000 |
| Production acceptance (per unit) | $800 |
| Periodic tests (amortized per unit) | $210 |
| **Total for first 10 units** | **$28,000 + (10 x $800) + (10 x $210) = $38,100** |
| **Per-unit amortized (at 10 units)** | **$3,810** |
| **Per-unit amortized (at 50 units)** | **$1,570** ($28K/50 + $800 + $210) |

Budget source: $28,000 qualification within [[../03_embodiment/DECS_S12_standards_compliance.md]] $35,000 test budget allocation. Production per-unit cost ($800-1,000) included in QC overhead per [[../03_embodiment/OCP_C14_cost_analysis.md]] Section 4.

---

## 14. Requirements Traceability Matrix

### 14.1 Qualification Tests to Requirements

| ATP | Requirements Verified | Pass/Fail Criteria Summary |
|-----|----------------------|---------------------------|
| ATP-01 | OPR-009, MAT-005, MAT-008, MAT-009, MAT-010 | RCS degradation <=1 dB; no base metal corrosion; GPS transmitting at 72h; bolt torque >=80% retained |
| ATP-02 | FOR-005, FOR-006, MAT-006 | Hold 44,460 N for 5 min; no permanent deformation >=0.5 mm; bolt torque >=90% retained; no weld cracks |
| ATP-03 | SIG-001, SIG-002, SIG-003, SIG-004, QUA-001 | Peak >=1,000 m2; avg >=1,000 m2; min >=700 m2; variation <=4 dB |
| ATP-04 | ENR-001, ENR-002, SIG-007, SIG-008 | >=72h endurance; 1 Hz fix rate; CEP <=5 m; availability >=99% |
| ATP-05 | OPR-002, OPR-003, OPR-004, OPR-009, KIN-001, KIN-003, KIN-005, FOR-007, FOR-010 | 72h survival intact; no cracks; RCS <=1 dB degradation; draft unchanged; mast alignment <=0.5 deg; tow >=3 kn |
| ATP-06 | ERG-001, ERG-002, ERG-005, ASM-001, ASM-006, SAF-001, MNT-002, MNT-003, OPR-001 | <=4 crew; <=30 min deployment; tool-free; all pins engaged; GPS functional; mooring recoverable |
| ATP-07 | MAT-004, SIG-009, PRD-003 | sigma_y >=230 MPa (XY), >=210 MPa (Z); UTS >=350 MPa; elongation >=5%; orthogonality +/-0.10 deg; no CT defects >=1.0 mm; hard anodize >=25 um |

### 14.2 Production Tests to Requirements

| ATP | Requirements Verified | Pass/Fail Criteria Summary |
|-----|----------------------|---------------------------|
| ATP-PA-01 | GEO-007 | System mass <=1,100 kg |
| ATP-PA-02 | GEO-001, GEO-002 | Diameter 8.0 m +/-0.1 m; depth 0.5 m +/-0.05 m |
| ATP-PA-03 | SAF-007 (hull integrity) | No leaks over 4h; draft unchanged +/-3 mm |
| ATP-PA-04 | GEO-004, GEO-010 | All 8 masts insert, pins engage, base plates seat |
| ATP-PA-05 | SIG-001, SIG-002, SIG-003, SIG-004, QUA-001 | Per ATP-03 criteria (production protocol at 5-deg increments) |
| ATP-PA-06 | SIG-007, ENR-002 | GPS fix <5 min; position <=5 m error; SBD received |
| ATP-PA-07 | MAT-005, MAT-008, MAT-009, MAT-010, SAF-006 | All visual checklist items satisfactory |
| ATP-PA-08 | QUA-004 (documentation) | All 17 documents present and complete |

### 14.3 Coverage Summary

| Status | Count | % of 34 PENDING-TEST |
|--------|-------|---------------------|
| Covered by qualification tests (Type I) | 27 | 79% |
| Covered by production tests (Type II) | 29 | 85% |
| Covered by both Type I + Type II | 24 | 71% |
| **Total unique requirements covered** | **34** | **100%** |

All 34 PENDING-TEST requirements from [[../03_embodiment/DECS_C11_requirements_verification.md]] are covered by at least one test procedure in this document.

---

## 15. Cross-References

### Phase 4 Documents
- [[acceptance_test_procedures.md]] -- This document

### Phase 3 Source Documents
- [[../03_embodiment/DECS_S12_standards_compliance.md]] -- Standards compliance, 7 tests (T-01 to T-07), test facilities, costs, sequence
- [[../03_embodiment/DECS_C11_requirements_verification.md]] -- 116 requirements, 34 PENDING-TEST, verification methods
- [[../03_embodiment/OCP_P15_production_planning.md]] -- QC plan (Section 4), final acceptance (Section 4.3), assembly sequence
- [[../03_embodiment/OCP_C14_cost_analysis.md]] -- BOM item references, unit cost $29,655
- [[../03_embodiment/PRAD_D8_design_structure.md]] -- Structural analysis, load cases, acceptance values
- [[../03_embodiment/DECS_D9_detail_specification.md]] -- Dimensions, tolerances, surface finishes, fastener schedule, FAI criteria

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), all acceptance criteria origins
- [[../01_requirements/standards_mapping.md]] -- MIL-STD-810H, MIL-STD-882E, ASTM F3318 compliance basis

### Project Management
- [[../PROJECT_STATUS.md]] -- Project status tracker

---

**Document Status:** Draft v1.0 -- Complete acceptance test procedures for all 7 qualification tests and 8 production acceptance tests.

**Key Summary:**
1. **7 qualification tests** (ATP-01 through ATP-07) covering corrosion, structural, RCS, GPS, sea survival, deployment, and AM process -- total cost $28,000, 8 weeks
2. **8 production tests** (ATP-PA-01 through ATP-PA-08) on every unit -- total cost ~$800/unit
3. **2 periodic tests** (proof load every 10th unit, GPS endurance every 5th) -- amortized ~$210/unit
4. **34/34 PENDING-TEST requirements** fully covered by at least one procedure
5. **3 decision gates** in qualification sequence ensure no test proceeds without prerequisite results
6. All procedures executable by a trained technician with specified equipment and calibration
7. Total qualification program ($28,000) within the $35,000 test budget from [[../03_embodiment/DECS_S12_standards_compliance.md]]
