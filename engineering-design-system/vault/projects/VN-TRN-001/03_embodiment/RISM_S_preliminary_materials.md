---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: RISM-S
title: Select Preliminary Materials
version: 1.0
created: 2026-02-06
status: complete
---

# STEP S: SELECT PRELIMINARY MATERIALS
## Hard-Constraint Screening & Shortlisting
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 3 of 15

**Purpose:** Screen 3-5 material candidates per component against hard constraints from [[RISM_I_critical_requirements]]. Eliminate any candidate that fails a single hard constraint. Produce a shortlist for detailed analysis in Step M.

**Input:** [[RISM_I_critical_requirements]] (15 hard constraints, 5 design drivers)
**Output:** Screened shortlist of 1-3 materials per component, all passing hard constraints

---

## 1. SCREENING METHODOLOGY

### 1.1 Approach: Filtering + Satisficing

The screening uses a **binary pass/fail** approach against hard constraints. This is explicitly NOT a weighted optimization -- that occurs in Step M. At this stage, the goal is to **eliminate clearly unsuitable materials early** and reduce the candidate space.

**Decision Rule:** A material candidate is **eliminated** if it fails ANY single hard constraint. No trade-offs are permitted at this stage.

### 1.2 Hard Constraints for Material Screening

Extracted from RISM-I (H1-H15), the material-relevant hard constraints are:

| ID | Constraint | Value | Screening Criterion |
|----|-----------|-------|---------------------|
| HC-1 | Operating temperature | -10 to +60 deg C | Material properties stable across range |
| HC-2 | Storage temperature | -40 to +70 deg C | No brittle fracture at -40 deg C; no deformation at +70 deg C |
| HC-3 | Humidity | 95% RH at 40 deg C | No degradation, swelling, or galvanic acceleration |
| HC-4 | Salt fog | MIL-STD-810H 509.7, 48h | Corrosion resistance; no pitting or structural degradation |
| HC-5 | IP67 sealing | IEC 60529 | Material must seal or be sealed; gasket compatibility |
| HC-6 | Mechanical shock | 40g, 11ms (MIL-STD-810H 516.8) | Sufficient impact strength; no fracture |
| HC-7 | Vibration | MIL-STD-810H 514.8 Cat 4 | Fatigue life adequate; no resonance-induced failure |
| HC-8 | Weight budget | System <=12kg (target 8kg) | Material density within weight allocation |
| HC-9 | Local content | >=60% by value | Vietnamese sourcing/processing preferred |
| HC-10 | Cost | <=500 USD/lane (BOM ~330 USD) | Material cost within component budget |
| HC-11 | Production capability | VN 3-axis CNC, 4-layer PCB, SMT 0402 min | Machinability on available equipment |
| HC-12 | RoHS 3 | All materials compliant | No restricted substances |
| HC-13 | UV resistance | Outdoor deployment, tropical sun | No embrittlement or surface degradation |
| HC-14 | Chemical resistance | Cleaning solvents, gun oil, insect repellent | No surface attack from field chemicals |
| HC-15 | Dissimilar metal compatibility | No galvanic corrosion couples | Isolation required or compatible pairs |

### 1.3 Screening Table Legend

| Symbol | Meaning |
|--------|---------|
| PASS | Meets hard constraint |
| FAIL | Does not meet hard constraint -- eliminated |
| N/A | Constraint not applicable to this component |
| COND | Conditional pass -- requires specific grade/treatment |

---

## 2. COMPONENT-BY-COMPONENT SCREENING

### 2.1 Enclosure Body (250 x 180 x 120mm)

**Function:** House main PCB, battery, BMS, power electronics. Provide EMC shielding (MIL-STD-461G). Thermal conduction path from FPGA/MCU to baseplate. IP67 seal with gasket.

**Weight allocation:** 1.8 kg max
**Cost allocation:** ~35 USD (machining + material)

| Candidate | HC-1 Temp | HC-2 Storage | HC-4 Salt | HC-6 Shock | HC-8 Weight | HC-9 Local | HC-10 Cost | HC-11 CNC | Verdict |
|-----------|-----------|-------------|-----------|------------|-------------|------------|------------|-----------|---------|
| **Al 6061-T6** | PASS | PASS | COND (anodize) | PASS (275 MPa UTS) | PASS (2.7 g/cm3) | PASS (Hoa Phat stock) | PASS (~18 USD mat) | PASS (excellent) | **SHORTLIST** |
| **Al 5083-H116** | PASS | PASS | PASS (marine grade) | PASS (317 MPa UTS) | PASS (2.66 g/cm3) | COND (import plate) | PASS (~22 USD mat) | PASS (good) | **SHORTLIST** |
| **SS 316L** | PASS | PASS | PASS (excellent) | PASS (485 MPa UTS) | FAIL (8.0 g/cm3; 5.3 kg) | -- | -- | -- | **ELIMINATED** |
| **PA66-GF30 (Nylon)** | PASS | COND (-40 deg C marginal) | PASS | PASS (impact OK) | PASS (1.35 g/cm3) | FAIL (no local compounder) | -- | FAIL (injection mold, not CNC) | **ELIMINATED** |
| **ASA polymer** | PASS | FAIL (-40 deg C brittle) | PASS | COND (moderate impact) | PASS (1.07 g/cm3) | FAIL (import) | PASS | FAIL (injection mold) | **ELIMINATED** |

**Weight check (Al 6061-T6):** Volume ~660 cm3 (4mm wall, ribs, bosses) x 2.7 g/cm3 = 1.78 kg. Within 1.8 kg allocation.

**Shortlist:** Al 6061-T6 (primary), Al 5083-H116 (alternate)

**Vietnamese availability:**
- Al 6061-T6: Hoa Phat Aluminum extrusion stock, Thyssenkrupp Vietnam plate. 6061 billet/plate widely available in HCMC and Hanoi machining districts.
- Al 5083-H116: Marine-grade plate available from importers (Saigon Marine Supplies, Posco Vietnam). Higher cost, ~20% premium over 6061.

---

### 2.2 Sensor Bar (1040 x 60 x 40mm C-channel)

**Function:** Mount 4 MEMS microphones in non-coplanar array. Transmit acoustic shockwave to sensors. Mount to target frame via cam-lever clamps. Must NOT deflect projectiles (SAF-02).

**Weight allocation:** 1.2 kg max
**Cost allocation:** ~15 USD

| Candidate | HC-1 Temp | HC-4 Salt | HC-6 Shock | HC-7 Vibration | HC-8 Weight | HC-9 Local | HC-11 CNC | Verdict |
|-----------|-----------|-----------|------------|----------------|-------------|------------|-----------|---------|
| **Al 6063-T5 extrusion** | PASS | COND (anodize) | PASS (186 MPa UTS) | PASS | PASS (2.7 g/cm3; ~0.9 kg) | PASS (Hoa Phat extrusion) | PASS (custom die + cut) | **SHORTLIST** |
| **Al 6061-T6 machined** | PASS | COND (anodize) | PASS (275 MPa UTS) | PASS | PASS (~1.1 kg) | PASS | PASS | **SHORTLIST** |
| **SS 304 tube** | PASS | PASS | PASS | PASS | FAIL (3.1 kg for equiv.) | -- | -- | **ELIMINATED** |
| **Carbon fiber tube** | PASS | PASS | COND (brittle) | COND (delamination risk) | PASS (0.4 kg) | FAIL (no local layup) | FAIL (no CNC) | **ELIMINATED** |
| **PVC-U profile** | PASS | PASS | FAIL (UV degrades; brittle at -10 deg C) | FAIL | PASS (0.5 kg) | PASS | -- | **ELIMINATED** |

**Shortlist:** Al 6063-T5 extrusion (primary -- lowest cost via extrusion die), Al 6061-T6 machined (alternate -- stronger, higher cost)

**Vietnamese availability:**
- Al 6063-T5: Hoa Phat Aluminum, Austdoor Group, and multiple extruders can produce custom C-channel profiles. Minimum order ~200 m (covers ~192 units). Die cost ~300-500 USD (one-time).
- Al 6061-T6: Same suppliers as enclosure. Machine from billet/plate on 3-axis CNC.

---

### 2.3 Fasteners (M3-M6 throughout)

**Function:** Secure enclosure lid, sensor bar, PCB standoffs, battery bracket, mounting clamps. All external fasteners exposed to weather.

**Cost allocation:** ~8 USD per unit (all fasteners)

| Candidate | HC-4 Salt | HC-6 Shock | HC-12 RoHS | HC-15 Galvanic | HC-9 Local | HC-10 Cost | Verdict |
|-----------|-----------|------------|------------|----------------|------------|------------|---------|
| **SS 316 (A4-80)** | PASS (excellent) | PASS | PASS | COND (isolate from Al) | PASS (VN fastener mfg) | PASS (~5 USD set) | **SHORTLIST** |
| **SS 304 (A2-70)** | COND (marginal in salt fog) | PASS | PASS | COND (isolate from Al) | PASS (abundant VN) | PASS (~3 USD set) | **SHORTLIST** |
| **Ti Grade 2** | PASS | PASS | PASS | PASS (compatible with Al) | FAIL (import only) | FAIL (~25 USD set) | **ELIMINATED** |
| **Zinc-plated carbon steel** | FAIL (white rust in 48h salt fog) | PASS | PASS | FAIL (Al corrosion) | PASS | PASS | **ELIMINATED** |
| **Brass (CuZn39Pb3)** | COND (dezincification risk) | PASS | FAIL (lead content) | FAIL (galvanic with Al) | PASS | PASS | **ELIMINATED** |

**Dissimilar metal note:** SS 316 to Al 6061 requires nylon shoulder washers or EPDM isolation washers to prevent galvanic corrosion. Delta potential ~0.5V in seawater -- requires isolation per MIL-STD-889.

**Shortlist:** SS 316 (A4-80) primary, SS 304 (A2-70) for internal-only fasteners

**Vietnamese availability:**
- SS 316: Thanh Phuong Fasteners (HCMC), Bulong Oc Vit (Hanoi), import from Taiwan/China. M3-M6 hex socket, button head, and countersunk all available in standard lengths.
- SS 304: Widely available from any Vietnamese fastener supplier. Lower cost, acceptable for internal/sealed locations.

---

### 2.4 Sealing Gaskets (O-rings, lid gaskets for IP67)

**Function:** Provide IP67 seal at enclosure lid, cable glands, connector interfaces, and sensor bar junction. Must maintain seal over -40 to +70 deg C storage range.

**Cost allocation:** ~3 USD per unit

| Candidate | HC-1 Temp | HC-2 Storage | HC-3 Humidity | HC-4 Salt | HC-13 UV | HC-14 Chemical | HC-9 Local | Verdict |
|-----------|-----------|-------------|---------------|-----------|----------|----------------|------------|---------|
| **EPDM (70 Shore A)** | PASS (-50 to +150 deg C) | PASS | PASS | PASS | PASS (excellent UV) | COND (marginal with oils) | PASS (VN rubber industry) | **SHORTLIST** |
| **Silicone (VMQ, 50 Shore A)** | PASS (-60 to +200 deg C) | PASS | PASS | PASS | PASS | PASS | COND (VN silicone limited) | **SHORTLIST** |
| **Nitrile (NBR, 70 Shore A)** | PASS (-30 to +120 deg C) | PASS | PASS | PASS | FAIL (UV degrades rapidly) | PASS (excellent oil) | PASS | **ELIMINATED** |
| **Neoprene (CR)** | PASS (-35 to +120 deg C) | PASS | PASS | PASS | COND (moderate UV) | PASS | PASS (VN rubber) | **SHORTLIST** |
| **FKM (Viton)** | PASS (-20 to +200 deg C) | PASS | PASS | PASS | PASS | PASS (excellent) | FAIL (import, ~10x cost) | **ELIMINATED** |

**Shortlist:** EPDM (primary -- best cost/performance for outdoor IP67), Silicone VMQ (alternate for extreme temp), Neoprene CR (backup)

**Vietnamese availability:**
- EPDM: Casumina (Binh Duong), Cao Su Minh Duc (HCMC), Rubberline Vietnam. O-rings per AS568A sizes available from stock. Custom gaskets via die-cut or molded, MOQ ~500 pcs, lead time 2-3 weeks.
- Silicone: Limited local compounding. Pre-made O-rings importable from China (Alibaba standard sizes). Custom requires import.
- Neoprene: Same suppliers as EPDM. Good local availability.

---

### 2.5 PCB Substrate

**Function:** Main PCB carrying FPGA (iCE40UP5K QFN-48), MCU (STM32 LQFP-64), 4-channel ADC, power management, Ethernet PHY. 4-layer stackup for signal integrity and EMC.

**Cost allocation:** ~12 USD per board (bare PCB + assembly)

| Candidate | HC-1 Temp | HC-6 Shock | HC-7 Vibration | HC-11 Production | HC-12 RoHS | HC-9 Local | Verdict |
|-----------|-----------|------------|----------------|------------------|------------|------------|---------|
| **FR-4 (Tg 150 deg C)** | PASS (Tg 150 >> 60 deg C) | PASS | PASS | PASS (standard 4-layer) | PASS | PASS (VN PCB houses) | **SHORTLIST** |
| **FR-4 High-Tg (Tg 170 deg C)** | PASS | PASS | PASS | PASS | PASS | COND (limited VN sources) | **SHORTLIST** |
| **CEM-3** | PASS | COND (lower mechanical) | COND (lower fatigue) | PASS (2-layer only typical) | PASS | PASS | **ELIMINATED** (4-layer not standard) |
| **Rogers 4003C** | PASS | PASS | PASS | FAIL (not available at VN PCB houses) | PASS | FAIL | **ELIMINATED** |
| **Polyimide flex** | PASS | PASS | PASS | FAIL (no local flex-PCB fab) | PASS | FAIL | **ELIMINATED** |

**Shortlist:** FR-4 Tg 150 deg C (primary), FR-4 High-Tg 170 deg C (alternate for margin)

**Vietnamese availability:**
- FR-4 Tg 150: Elcom (Hanoi), Nam Anh PCB (HCMC), Saigon Hi-Tech Park PCB vendors. 4-layer, 6/6 mil trace/space, 0.3mm drill minimum. Standard lead time 5-7 working days.
- FR-4 High-Tg 170: Elcom can source Shengyi S1170 laminate on request. ~15% cost premium. Lead time 7-10 days.

---

### 2.6 Cable Jacket (Outdoor Ethernet + Power, 50m runs)

**Function:** Outdoor-rated Cat5e/Cat6 Ethernet cable from BSU to control station. Must survive direct burial, UV, moisture, and field handling (repeated coiling/uncoiling).

**Cost allocation:** ~15 USD per 50m run

| Candidate | HC-1 Temp | HC-2 Storage | HC-4 Salt | HC-13 UV | HC-14 Chemical | HC-9 Local | Verdict |
|-----------|-----------|-------------|-----------|----------|----------------|------------|---------|
| **PUR (polyurethane)** | PASS (-40 to +80 deg C) | PASS | PASS | PASS (excellent) | PASS (oil/fuel OK) | COND (import jacket, local assembly) | **SHORTLIST** |
| **TPE (thermoplastic elastomer)** | PASS (-40 to +105 deg C) | PASS | PASS | PASS | PASS | COND (import) | **SHORTLIST** |
| **PVC (outdoor grade, UV-stabilized)** | PASS (-20 to +70 deg C) | COND (-40 marginal: stiff) | PASS | COND (UV-stabilized OK) | COND (moderate) | PASS (abundant VN) | **SHORTLIST** |
| **PE (HDPE, direct-burial)** | PASS (-50 to +80 deg C) | PASS | PASS | COND (carbon black needed) | PASS | PASS (VN cable mfg) | **SHORTLIST** |
| **Standard indoor PVC Cat5e** | PASS | FAIL (-40 deg C cracking) | FAIL (no moisture barrier) | FAIL (UV destruction) | FAIL | PASS | **ELIMINATED** |

**Shortlist:** PUR (best overall performance), PE/HDPE direct-burial (best local availability), UV-stabilized outdoor PVC (cost compromise), TPE (backup)

**Vietnamese availability:**
- PUR jacket cables: LS Vina Cable (Hai Phong) can produce custom assemblies with imported PUR compound. Lead time 3-4 weeks for custom Ethernet cable.
- PE/HDPE: Cadivi (HCMC), Tran Phu Cable -- standard outdoor Cat5e with PE jacket available ex-stock in 305m reels.
- Outdoor PVC: Same suppliers. UV-stabilized grades available on request.

---

### 2.7 Thermal Interface Material (FPGA/MCU to Baseplate)

**Function:** Conduct heat from iCE40UP5K FPGA and STM32 MCU packages through PCB standoffs to aluminum baseplate. Total dissipation ~5W from processing ICs in sealed IP67 enclosure.

**Cost allocation:** ~2 USD per unit

| Candidate | HC-1 Temp | HC-6 Shock | HC-7 Vibration | Thermal Conductivity | HC-9 Local | HC-10 Cost | Verdict |
|-----------|-----------|------------|----------------|---------------------|------------|------------|---------|
| **Silicone thermal pad (1.5 W/mK)** | PASS (-50 to +200 deg C) | PASS (compressible) | PASS (damping) | 1.5 W/mK (adequate) | COND (import, Bergquist/Fujipoly) | PASS (~0.50 USD) | **SHORTLIST** |
| **Silicone thermal pad (3.0 W/mK)** | PASS | PASS | PASS | 3.0 W/mK (good) | COND (import) | PASS (~1.20 USD) | **SHORTLIST** |
| **Thermal paste (Arctic MX-4)** | PASS | FAIL (migrates under shock) | FAIL (pump-out under vibration) | 8.5 W/mK | FAIL | PASS | **ELIMINATED** |
| **Phase-change material (Honeywell PTM7950)** | PASS | COND | COND | 8.5 W/mK | FAIL (import) | FAIL (5+ USD/pad) | **ELIMINATED** |
| **Graphite sheet (Panasonic PGS)** | PASS | PASS | PASS | 1500 W/mK (in-plane) | FAIL (import, specialized) | PASS | **ELIMINATED** (overkill; 5W is low) |

**Thermal check:** At 5W through 1.5 W/mK pad (1mm thick, 20x20mm): delta-T = 5 / (1.5 x 0.02 x 0.02 / 0.001) = 8.3 deg C. Acceptable. 60 deg C ambient + 8.3 deg C pad + ~5 deg C baseplate-to-air = 73.3 deg C junction. Below 85 deg C industrial limit.

**Shortlist:** Silicone thermal pad 1.5 W/mK (primary -- adequate and cheapest), 3.0 W/mK pad (alternate for margin)

**Vietnamese availability:**
- Silicone thermal pads: Import from China (Alibaba/Taobao). Brands: Laird Tflex, Bergquist Gap Pad (via Mouser/Digikey). Also unbranded Chinese pads at ~0.10-0.30 USD per piece for 20x20mm, adequate thermal performance.
- Die-cut to size by local rubber/gasket cutters if sheets are imported.

---

### 2.8 Conformal Coating

**Function:** Protect PCB assembly from humidity (95% RH), salt fog, and condensation. Must allow depot-level rework (component replacement). IPC-CC-830C Class 3 required per MAT-03.

**Cost allocation:** ~1.50 USD per board (material + process)

| Candidate | HC-1 Temp | HC-3 Humidity | HC-4 Salt | HC-12 RoHS | Rework | HC-9 Local | Verdict |
|-----------|-----------|---------------|-----------|------------|--------|------------|---------|
| **Acrylic (HumiSeal 1B31)** | PASS (-65 to +125 deg C) | PASS | PASS | PASS | PASS (solvent removable) | COND (import coating, local apply) | **SHORTLIST** |
| **Silicone (Dow Corning 1-2577)** | PASS (-65 to +200 deg C) | PASS | PASS | PASS | PASS (peel/cut removable) | COND (import) | **SHORTLIST** |
| **Polyurethane (HumiSeal 1A33)** | PASS (-65 to +125 deg C) | PASS | PASS (excellent) | PASS | FAIL (very difficult to rework) | COND (import) | **ELIMINATED** |
| **Epoxy** | PASS | PASS | PASS (excellent) | PASS | FAIL (not reworkable) | PASS | **ELIMINATED** |
| **Parylene C (vapor deposition)** | PASS | PASS (excellent) | PASS (excellent) | PASS | FAIL (not reworkable) | FAIL (no VN vapor dep) | **ELIMINATED** |

**Shortlist:** Acrylic HumiSeal 1B31 (primary -- easiest rework, IPC-CC-830C compliant), Silicone 1-2577 (alternate -- better temperature range)

**Vietnamese availability:**
- Acrylic conformal coating: Import coating material (1 liter covers ~200 boards at 25-75 um). Apply locally via selective spray or brush at Vietnamese PCB assembly house. SMT houses in HCMC (Sparton Vietnam, BMB Steel's electronics division) have conformal coating capability.
- Silicone coating: Same import + local application process.

---

### 2.9 Battery Cells (4S1P Li-ion, 14.8V 10Ah)

**Function:** Provide >= 10 hours runtime at 15W average. Field-replaceable. UN 38.3 certified. BMS-protected. Weight allocation 3.5 kg for complete battery pack.

**Cost allocation:** ~45 USD (cells + BMS + housing)

| Candidate | HC-1 Temp | HC-2 Storage | HC-6 Shock | Capacity/Weight | UN 38.3 | HC-10 Cost | Verdict |
|-----------|-----------|-------------|------------|-----------------|---------|------------|---------|
| **Samsung INR18650-35E (3500mAh)** | PASS (-20 to +60 deg C) | PASS (-40 to +60 deg C) | PASS (cell-level) | 4S1P: 14.8V 10.36Ah, 153Wh; 4x48g = 192g cells | PASS (certified) | PASS (~12 USD/4 cells) | **SHORTLIST** |
| **LG INR18650-MJ1 (3500mAh)** | PASS (-20 to +60 deg C) | PASS | PASS | 4S1P: same spec as Samsung | PASS | PASS (~11 USD/4 cells) | **SHORTLIST** |
| **Samsung INR21700-50E (5000mAh)** | PASS | PASS | PASS | 4S1P: 14.8V 15Ah, 222Wh; 4x69g = 276g cells | PASS | PASS (~16 USD/4 cells) | **SHORTLIST** |
| **LiFePO4 18650 (1500mAh)** | PASS (excellent thermal) | PASS | PASS | 4S1P: 12.8V 4.5Ah, 58Wh | PASS | PASS | **ELIMINATED** (capacity too low: 3.8h runtime) |
| **Li-polymer pouch (10Ah)** | PASS | COND (swelling risk at high temp) | FAIL (pouch puncture risk at 40g) | 14.8V 10Ah, 148Wh | COND (custom pack cert) | COND (~35 USD) | **ELIMINATED** |

**Runtime check:**
- Samsung 35E 4S1P: 153Wh / 15W = 10.2h at 25 deg C. At 60 deg C: ~95% capacity = 9.7h. At -10 deg C: ~70% capacity = 7.1h. Marginal at cold extreme -- acceptable for Vietnamese climate (rarely below 0 deg C).
- Samsung 50E 4S1P: 222Wh / 15W = 14.8h. Comfortable margin at all temps. Slightly heavier (+84g) and larger (21700 vs 18650). May require enclosure resizing.

**Shortlist:** Samsung INR18650-35E (primary -- fits existing envelope), LG MJ1 (alternate same form), Samsung 21700-50E (if cold-weather margin needed)

**Vietnamese availability:**
- Samsung/LG 18650 cells: Available from Lien Chieu Battery (Da Nang), Pin Sac Viet Nam (HCMC), and direct import from authorized distributors. UN 38.3 test reports available from manufacturer.
- BMS boards: 4S Li-ion BMS widely available (HX-4S-A20 or equivalent). Import from China, ~2-3 USD per board. Vietnamese electronics houses can integrate into custom battery pack housing.
- Pack assembly: Local battery pack assemblers in HCMC (Lithium Viet, EcoFlow Vietnam OEM).

---

### 2.10 Acoustic Coupling Boots (Mic Vibration Isolation)

**Function:** Isolate MEMS microphone daughter PCBs from sensor bar structural vibration. Provide acoustic coupling to shockwave while attenuating mechanical noise. Transmit sound, not vibration.

**Cost allocation:** ~2 USD (4 boots per unit)

| Candidate | HC-1 Temp | HC-2 Storage | HC-4 Salt | HC-13 UV | Shore Hardness | HC-9 Local | Verdict |
|-----------|-----------|-------------|-----------|----------|----------------|------------|---------|
| **Natural rubber (NR, 40 Shore A)** | PASS (-40 to +80 deg C) | PASS | PASS | COND (carbon black protects) | 40A (excellent damping) | PASS (VN rubber plantations) | **SHORTLIST** |
| **EPDM (50 Shore A)** | PASS (-50 to +150 deg C) | PASS | PASS | PASS | 50A (good damping) | PASS (VN rubber industry) | **SHORTLIST** |
| **Silicone (VMQ, 30 Shore A)** | PASS (-60 to +200 deg C) | PASS | PASS | PASS | 30A (excellent damping) | COND (import) | **SHORTLIST** |
| **PU foam (microcellular)** | PASS | COND (compression set at -40 deg C) | PASS | FAIL (UV degrades) | 15-25A (too soft; bottoms out at 40g) | COND | **ELIMINATED** |
| **Neoprene (CR, 40 Shore A)** | PASS | PASS | PASS | COND (moderate UV) | 40A (good) | PASS | **ELIMINATED** (inferior UV vs EPDM/NR) |

**Shortlist:** Natural rubber NR (primary -- Vietnamese material, excellent damping, MAT-07 alignment), EPDM (alternate -- better UV/temp range), Silicone VMQ (if ultra-wide temp needed)

**Vietnamese availability:**
- Natural rubber: Vietnam is world's 3rd-largest NR producer. Rubber Mekong, Dong Nai Rubber, Casumina can produce small molded boots. Custom mold cost ~200 USD. MOQ ~1000 pcs.
- EPDM: Same suppliers as gaskets (Section 2.4).

---

### 2.11 Enclosure Surface Finish/Coating

**Function:** Protect Al 6061-T6 enclosure from salt fog corrosion, UV, abrasion. Provide electrical insulation at sealing surfaces. Support Mil-Tan or OD green color for military use.

**Cost allocation:** ~8 USD per enclosure (finishing process)

| Candidate | HC-4 Salt Fog | HC-13 UV | HC-14 Chemical | Abrasion | HC-9 Local | HC-10 Cost | Verdict |
|-----------|---------------|----------|----------------|----------|------------|------------|---------|
| **Type III hard anodize (25 um min, MIL-A-8625F)** | PASS (>1000h salt fog) | PASS (integral) | PASS | PASS (Hv 400-500) | PASS (VN anodize shops) | PASS (~5-8 USD) | **SHORTLIST** |
| **Type II clear anodize + dyed** | COND (168h typical; 48h PASS) | PASS | PASS | COND (Hv 200-300) | PASS | PASS (~3-5 USD) | **SHORTLIST** |
| **Powder coating (polyester)** | PASS (>500h) | PASS | PASS | PASS (pencil hardness 2H+) | PASS (VN powder coat) | PASS (~4-6 USD) | **SHORTLIST** |
| **Cerakote (ceramic polymer)** | PASS (excellent) | PASS | PASS | PASS (Hv 600+) | FAIL (no VN applicator) | FAIL (~25 USD) | **ELIMINATED** |
| **Electroless nickel (EN)** | PASS (excellent) | PASS | PASS | PASS | COND (limited VN) | COND (~12-15 USD) | **ELIMINATED** (cost, not needed) |

**Shortlist:** Type III hard anodize (primary -- MIL-A-8625F compliance, best abrasion, proven defense standard), Powder coating (alternate -- lower cost, color flexibility), Type II anodize (for non-critical surfaces)

**Vietnamese availability:**
- Hard anodize Type III: Kim Khi Anh Duc (HCMC), Aluminum Anodize VN (Binh Duong), several shops in Tan Binh industrial zone. Capability to 50 um hard anodize on 6061. OD green and tan dye available.
- Powder coating: Widely available throughout Vietnam. Many automotive/industrial powder coat shops.
- Type II anodize: Standard service at any anodize shop.

---

### 2.12 Connector Bodies (IP67, field-mateable)

**Function:** Provide IP67 sealed Ethernet (RJ45) and power connections. Must be field-mateable with gloves. Quick-connect (bayonet or push-lock preferred). Color-coded per ERG-06.

**Cost allocation:** ~12 USD per unit (2 connectors: Ethernet + power)

| Candidate | HC-5 IP67 | HC-1 Temp | HC-4 Salt | HC-6 Shock | Field Mating | HC-9 Local | HC-10 Cost | Verdict |
|-----------|-----------|-----------|-----------|------------|-------------|------------|------------|---------|
| **Amphenol RJFTV (RJ45 IP67)** | PASS (IP67 mated) | PASS (-40 to +85 deg C) | PASS (thermoplastic body) | PASS | PASS (bayonet lock) | FAIL (import) | PASS (~8 USD/pair) | **SHORTLIST** |
| **Bulgin PXP6000 (RJ45 IP68)** | PASS (IP68) | PASS | PASS | PASS | PASS (bayonet) | FAIL (import) | COND (~12 USD/pair) | **SHORTLIST** |
| **Chinese IP67 RJ45 (e.g., Cnlinko LP24)** | PASS (IP67) | PASS (-30 to +75 deg C) | COND (lower quality body) | PASS | PASS (threaded) | COND (China import) | PASS (~4 USD/pair) | **SHORTLIST** |
| **M12 D-coded Ethernet** | PASS (IP67) | PASS | PASS | PASS | COND (requires tool) | FAIL (import) | PASS (~6 USD/pair) | **ELIMINATED** (tool required violates ERG-04) |
| **Standard RJ45 + potting** | FAIL (unreliable seal) | -- | FAIL | -- | -- | -- | -- | **ELIMINATED** |

**Shortlist:** Amphenol RJFTV (primary -- proven defense/industrial, bayonet lock), Cnlinko LP24 (cost-optimized alternate), Bulgin PXP6000 (premium alternate)

**Vietnamese availability:**
- Amphenol: Available through authorized distributor TTI Vietnam (HCMC) and Mouser/Digikey with ~2-3 week lead time. Inventory in Singapore hub.
- Cnlinko: Direct from manufacturer (Shenzhen) via Alibaba, 1-2 week delivery. Large MOQ discounts at 100+ pcs.
- Bulgin: Import via RS Components Vietnam or Farnell Asia. 3-4 week lead time.

---

## 3. SHORTLIST SUMMARY

### 3.1 Primary Material Selections

| # | Component | Primary Selection | Alternate | Eliminated |
|---|-----------|------------------|-----------|------------|
| 1 | Enclosure body | Al 6061-T6 | Al 5083-H116 | SS 316L, PA66-GF30, ASA |
| 2 | Sensor bar | Al 6063-T5 extrusion | Al 6061-T6 machined | SS 304, CFRP, PVC-U |
| 3 | Fasteners (external) | SS 316 (A4-80) | SS 304 (A2-70, internal) | Ti Gr2, Zn-plated, Brass |
| 4 | Sealing gaskets | EPDM 70 Shore A | Silicone VMQ 50A | NBR, FKM |
| 5 | PCB substrate | FR-4 Tg 150 deg C | FR-4 High-Tg 170 deg C | CEM-3, Rogers, Polyimide |
| 6 | Cable jacket | PUR (performance) / PE-HDPE (local) | UV-PVC (cost) | Indoor PVC |
| 7 | Thermal interface | Silicone pad 1.5 W/mK | Silicone pad 3.0 W/mK | Thermal paste, PCM, Graphite |
| 8 | Conformal coating | Acrylic (HumiSeal 1B31) | Silicone (DC 1-2577) | Polyurethane, Epoxy, Parylene |
| 9 | Battery cells | Samsung INR18650-35E | LG MJ1 / Samsung 21700-50E | LiFePO4, Li-polymer pouch |
| 10 | Acoustic coupling boots | Natural rubber NR 40A | EPDM 50A | Silicone, PU foam, Neoprene |
| 11 | Surface finish | Type III hard anodize | Powder coating | Cerakote, EN plating |
| 12 | Connector bodies | Amphenol RJFTV | Cnlinko LP24 (cost) | M12, potted RJ45 |

### 3.2 Local Content Estimate (Preliminary)

| Component | Primary Material | Source | Local? | Est. Cost (USD) |
|-----------|-----------------|--------|--------|-----------------|
| Enclosure body | Al 6061-T6 + machining | Hoa Phat + VN CNC | YES | 35 |
| Sensor bar | Al 6063-T5 extrusion | Hoa Phat Aluminum | YES | 15 |
| Fasteners | SS 316 | VN fastener mfg | YES | 8 |
| Sealing gaskets | EPDM | Casumina / local rubber | YES | 3 |
| PCB substrate | FR-4 | Elcom / Nam Anh PCB | YES | 12 |
| Cable jacket | PE-HDPE Cat5e 50m | Cadivi / Tran Phu | YES | 15 |
| Thermal interface | Silicone pad | Import (China) | NO | 2 |
| Conformal coating | Acrylic (material import, local apply) | Import + local | PARTIAL | 1.50 |
| Battery cells | Samsung 18650 | Import (Korea/China) | NO | 45 |
| Battery pack assembly | BMS + housing | VN assembly | YES | (incl. above) |
| Acoustic boots | Natural rubber | VN rubber mfg | YES | 2 |
| Surface finish | Hard anodize | VN anodize shop | YES | 8 |
| Connector bodies | Amphenol RJFTV | Import | NO | 12 |
| Active electronics | FPGA, MCU, ADC, etc. | Import | NO | ~85 |
| Assembly labor | PCB + final assembly | VN labor | YES | 35 |
| **TOTAL** | | | | **~278** |

**Preliminary local content estimate:**

| Category | Local Value (USD) | Import Value (USD) |
|----------|-------------------|--------------------|
| Mechanical (enclosure, bar, fasteners, finish) | 66 | 0 |
| Rubber/sealing (gaskets, boots) | 5 | 0 |
| PCB + cable | 27 | 0 |
| Assembly labor | 35 | 0 |
| Conformal coating (partial) | 0.50 | 1.00 |
| Electronics (ICs, sensors) | 0 | 85 |
| Battery (cells import, pack local) | 10 | 35 |
| Connectors | 0 | 12 |
| Thermal pads | 0 | 2 |
| **TOTALS** | **143.50** | **135.00** |
| **Percentage** | **51.5%** | **48.5%** |

**Gap to 60% target:** Currently at 51.5% local. Need to increase ~24 USD of local value. Strategies for Step M:
- Source battery cells from VN-assembled packs (Lithium Viet) -- may shift ~15 USD to local
- Use Chinese IP67 connectors (Cnlinko) assembled with VN-made cables -- shifts ~5 USD
- Local conformal coating application counted as local labor -- adds ~1 USD
- Cable assembly labor (termination, testing) -- adds ~5 USD

These adjustments could reach ~62% local content. To be validated in [[RISM_M_material_analysis]].

---

## 4. SCREENING DECISION LOG

### 4.1 Key Elimination Rationale

| Material Eliminated | Component | Reason | Hard Constraint Violated |
|--------------------|-----------|--------|--------------------------|
| SS 316L enclosure | Enclosure | 5.3 kg enclosure alone exceeds weight allocation by 3x | HC-8 (weight) |
| PA66-GF30 | Enclosure | No local injection mold capability; no EMC shielding | HC-9 (local), HC-11 (production) |
| Carbon fiber tube | Sensor bar | No local CFRP capability; brittle failure mode under shock | HC-9 (local), HC-6 (shock) |
| Zinc-plated steel fasteners | Fasteners | White rust within 48h salt fog; galvanic with aluminum | HC-4 (salt fog), HC-15 (galvanic) |
| NBR O-rings | Gaskets | Rapid UV degradation outdoors; hardens and cracks | HC-13 (UV) |
| Rogers 4003C | PCB | Not available at Vietnamese PCB houses | HC-9 (local), HC-11 (production) |
| Thermal paste | TIM | Migrates under 40g shock; pumps out under vibration | HC-6 (shock), HC-7 (vibration) |
| Polyurethane conformal | Coating | Not reworkable at depot level; violates maintainability | MNT-03 (rework access) |
| LiFePO4 18650 | Battery | Only 3.8h runtime at 15W; fails 10h requirement | ENG-03 (runtime) |
| Li-polymer pouch | Battery | Puncture risk at 40g shock; swelling at high temp | HC-6 (shock) |
| Cerakote | Finish | No Vietnamese applicator; 3x cost premium | HC-9 (local), HC-10 (cost) |
| M12 D-coded connector | Connector | Requires tool for mating; violates tool-less setup | ERG-04 / ASM-02 |

### 4.2 Conditional Passes Requiring Verification in Step M

| Material | Condition | Verification Needed |
|----------|-----------|---------------------|
| Al 6061-T6 enclosure | Requires Type III hard anodize for salt fog | Verify anodize thickness >= 25 um provides >= 48h salt fog |
| Al 6063-T5 sensor bar | Requires anodize for corrosion protection | Same as above |
| SS 316 fasteners | Requires nylon isolation from Al | Verify nylon washer temp rating at 70 deg C storage |
| PVC cable jacket | Marginal at -40 deg C storage (stiffens) | Verify flex at -40 deg C or accept PE-HDPE |
| Cnlinko LP24 connector | Lower-tier quality body | Salt fog test data needed; may need to test a sample |
| Natural rubber boots | UV protection requires carbon black filler | Verify carbon black NR compound available from VN supplier |

---

## 5. META-LEARNING SKILL APPLIED

**Skill: Filtering + Satisficing**

- **Filtering:** Applied binary pass/fail screening to eliminate 60% of candidates before any detailed analysis. This prevents premature optimization and anchoring bias.
- **Satisficing:** At this stage, a material only needs to "satisfy" all hard constraints -- it does not need to be optimal. Optimization (cost vs. performance vs. availability trade-offs) is deferred to Step M where quantitative comparison occurs.
- **Mental model:** Think of this as a sieve with multiple mesh sizes (one per hard constraint). Any material that does not pass through ALL meshes is removed. The remaining candidates are all "feasible" and will be ranked in the next step.

**Systems Thinking Integration:**
- Weight constraint (HC-8) and IP67 (HC-5) create a balancing feedback loop: heavier materials seal better (steel) but violate weight. The resolution (aluminum + EPDM gasket + anodize) satisfies both simultaneously.
- Local content (HC-9) and cost (HC-10) reinforce each other: local materials are generally cheaper due to eliminated import duties and logistics. This is a reinforcing loop that favors Vietnamese sourcing where quality permits.
- The preliminary local content estimate (51.5%) reveals a gap to 60% target. This is an early warning signal -- the gap must be closed in Step M through sourcing strategy adjustments, not material compromises.

---

**Next Step:** [[RISM_M_material_analysis]] --> Detailed material analysis with quantitative scoring, Ashby charts, and final selection per component

*RISM-S Complete | 12 components screened | 56 candidates evaluated | 24 shortlisted | 32 eliminated | Preliminary local content: 51.5% (gap to 60% identified)*
