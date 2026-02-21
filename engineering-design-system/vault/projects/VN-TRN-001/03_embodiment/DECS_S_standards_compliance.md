---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: DECS-S
title: Standards Compliance
version: 1.0
created: 2026-02-06
status: complete
---

# STEP S: STANDARDS COMPLIANCE
## Regulatory & Standards Mapping for BSU-V1
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 12 of 15

**Purpose:** Comprehensively map all applicable military, international, and Vietnamese standards to BSU-V1 design features, define test conditions, and develop a test plan for design verification and production validation.

**Input:** [[DECS_E_evaluate_variants]] (Selected layout L1), [[embodiment_design]] (Detailed component design)
**Output:** Complete standards compliance matrix, detailed test conditions, hazard analysis, test plan

---

## 1. APPLICABLE STANDARDS LIST

### 1.1 Standards Summary

| # | Standard | Title | Edition | Scope | Applicability |
|---|----------|-------|---------|-------|---------------|
| 1 | MIL-STD-810H | Environmental Engineering Considerations and Laboratory Tests | 2019 (Change 2, 2023) | Environmental stress screening for military equipment | **PRIMARY** - All environmental requirements |
| 2 | MIL-STD-461G | Requirements for the Control of Electromagnetic Interference | 2015 | EMC emissions and susceptibility | **PRIMARY** - EMC compliance |
| 3 | MIL-STD-882E | System Safety | 2012 | System safety engineering and management | **PRIMARY** - Hazard analysis |
| 4 | IEC 62368-1 | Audio/Video, Information and Communication Technology Equipment - Safety | Ed. 3, 2018 | Product safety for IT/AV equipment | **SECONDARY** - Electrical safety |
| 5 | IEC 60529 | Degrees of Protection Provided by Enclosures (IP Code) | Ed. 2.2, 2013 | Ingress protection rating | **PRIMARY** - IP67 verification |
| 6 | IPC-CC-830C | Qualification and Performance of Electrical Insulating Compound for Printed Wiring Assemblies | 2019 | Conformal coating requirements | **PROCESS** - PCB coating |
| 7 | IPC-A-610 | Acceptability of Electronic Assemblies | Rev. H, 2020 | Soldering and assembly workmanship | **PROCESS** - Class 2 production |
| 8 | MIL-A-8625F | Anodic Coatings for Aluminum and Aluminum Alloys | 2003 (Amendment 1) | Aluminum anodizing specification | **PROCESS** - Enclosure finish |
| 9 | UN 38.3 | Transport of Dangerous Goods - Lithium Battery Tests | Rev. 8, 2023 | Lithium battery safety for transport | **PRIMARY** - Battery certification |
| 10 | FASIT | Future Army System of Integrated Targets | v5.0 | Target system communication protocol | **INTERFACE** - Interoperability |
| 11 | TCVN 7447 | Vietnamese Electrical Installation Standard | 2010 (based on IEC 60364) | Electrical installation requirements | **NATIONAL** - Vietnamese compliance |
| 12 | TCVN 6450 | Vietnamese EMC Standard | 2016 (based on CISPR 22/32) | Electromagnetic compatibility | **NATIONAL** - Vietnamese compliance |

### 1.2 Standards Hierarchy

```
TIER 1 - MANDATORY (Design-Critical)
├── MIL-STD-810H    → Environmental survivability
├── MIL-STD-461G    → EMC emissions/susceptibility
├── MIL-STD-882E    → System safety
├── IEC 60529       → IP67 ingress protection
└── UN 38.3         → Li-ion battery transport

TIER 2 - MANDATORY (Process/Quality)
├── IPC-CC-830C     → Conformal coating qualification
├── IPC-A-610       → Assembly workmanship (Class 2)
└── MIL-A-8625F     → Anodizing specification

TIER 3 - COMPLIANCE (Market Access)
├── IEC 62368-1     → Product safety (export markets)
├── FASIT           → US/NATO interoperability
├── TCVN 7447       → Vietnamese electrical standard
└── TCVN 6450       → Vietnamese EMC standard
```

### 1.3 Requirements Traceability

| Standard | Mapped Requirements |
|----------|---------------------|
| MIL-STD-810H | OPR-01, OPR-02, OPR-03, OPR-04, OPR-05, OPR-06, OPR-07, FRC-03, FRC-04 |
| MIL-STD-461G | SAF-05, SIG-01, SIG-02 |
| MIL-STD-882E | SAF-01 through SAF-06 |
| IEC 62368-1 | SAF-01, SAF-03 |
| IEC 60529 | OPR-07, ASM-02 |
| IPC-CC-830C | MAT-03 |
| IPC-A-610 | PRD-03, PRD-05 |
| MIL-A-8625F | MAT-01 |
| UN 38.3 | ENG-04, TRN-04, SAF-04 |
| FASIT | SIG-06 |
| TCVN 7447 | SAF-01 |
| TCVN 6450 | SAF-05 |

---

## 2. MIL-STD-810H DETAILED COMPLIANCE

### 2.1 Method 501.7 - High Temperature

| Parameter | Detail |
|-----------|--------|
| **Method** | 501.7 High Temperature |
| **Applicable Procedure** | Procedure II - Operation (Cyclic) |
| **Test Condition** | Category A4: Hot-Dry (Desert); 60C constant for steady-state, 44C to 71C diurnal cycle |
| **BSU-V1 Test Condition** | 60C constant (operating), 70C constant (storage) |
| **Duration** | Operating: 7 consecutive days with 4-hour hot soak at 60C per cycle; Storage: 7 days at 70C |
| **Solar Radiation** | Not required (BSU-V1 is not directly solar-exposed; anodized+painted surface) |
| **Humidity** | Dry cycle (5-10% RH at temperature) |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| Industrial-grade ICs (-40C to +85C) | All active components rated 25C above max operating temp |
| FR-4 Tg170 PCB substrate | Glass transition temperature 170C >> 60C operating |
| EPDM gaskets rated to 150C continuous | Gasket integrity maintained at 70C storage |
| No LCD display in BSU | Eliminates common high-temp failure mode |
| Conservative component derating (50% voltage) | Reduced thermal stress on semiconductors |
| 6mm aluminum base plate as heat sink | Thermal path FPGA/MCU -> thermal pad -> base plate -> ambient |
| Thermal analysis: at 60C ambient, 15W dissipation, junction temp ~85C | Within 85C industrial rating |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Analysis** | Thermal simulation (IcePak or equivalent) of enclosure at 60C ambient, 15W dissipation |
| **Test** | MIL-STD-810H 501.7 Procedure II at certified lab |
| **Functional Test During** | System operates continuously during hot soak; verify TDOA accuracy, Ethernet connectivity, BIT status |
| **Pass/Fail Criteria** | System operational throughout; no degradation of scoring accuracy beyond +/-10mm; no thermal shutdown; no permanent damage after storage exposure |
| **Estimated Duration** | 14 days (7 operational + 7 storage) |
| **Estimated Cost** | $3,000-5,000 |

---

### 2.2 Method 502.7 - Low Temperature

| Parameter | Detail |
|-----------|--------|
| **Method** | 502.7 Low Temperature |
| **Applicable Procedure** | Procedure II - Operation |
| **Test Condition** | Category C1: Mild Cold; -10C operating, -40C storage |
| **BSU-V1 Test Condition** | -10C continuous operating, -40C storage |
| **Duration** | Operating: 72 hours at -10C; Storage: 24 hours at -40C |
| **Rate of Change** | Standard (not to exceed 3C per minute) |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| Industrial-grade ICs (-40C to +85C) | 30C margin below -10C operating |
| Li-ion Samsung INR18650-35E rated -20C discharge | Battery operable at -10C (derated capacity ~70%) |
| Calibration-free TDOA algorithm | No temperature-dependent calibration needed; speed-of-sound change is implicit in algorithm |
| No LCD or fluid-filled components | Eliminates freeze vulnerability |
| EPDM gaskets rated to -40C | Gasket sealing maintained at -40C storage |
| Acrylic conformal coating (HumiSeal 1B31) rated -65C to +125C | No cracking at low temperature |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Analysis** | Battery capacity curve analysis at -10C; power budget verification at reduced capacity |
| **Test** | MIL-STD-810H 502.7 Procedure II at certified lab |
| **Functional Test During** | Cold-start from -10C; TDOA accuracy verification; battery runtime measurement at -10C |
| **Pass/Fail Criteria** | System boots and operates at -10C; TDOA accuracy within +/-10mm; battery provides minimum 4 hours at -10C; no permanent damage after -40C storage |
| **Estimated Duration** | 5 days (72h operation + 24h storage + transition) |
| **Estimated Cost** | $2,500-4,000 |

---

### 2.3 Method 507.6 - Humidity

| Parameter | Detail |
|-----------|--------|
| **Method** | 507.6 Humidity |
| **Applicable Procedure** | Procedure III - Aggravated (Tropical Cycling) |
| **Test Condition** | 95% RH at 40C, cycling to 30C; 10 daily cycles |
| **Condensation** | Condensation expected during temperature transitions |
| **Duration** | 10 complete 24-hour cycles (240 hours total) |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| IP67 enclosure (IEC 60529) | Prevents moisture ingress during normal cycling |
| IPC-CC-830C Class 3 conformal coating | Protects PCB even if condensation forms on internal surfaces |
| EPDM O-ring gasket (AS568A) | Maintains seal under thermal cycling |
| Nickel-plated connectors (no exposed copper) | Prevents galvanic corrosion from condensation |
| Dissimilar metal isolation (nylon washers) | Prevents galvanic cell formation in humid conditions |
| FR-4 Tg170 with low moisture absorption | Substrate Dk/Df stability under humidity |
| Desiccant pack inside enclosure (optional) | Absorbs trapped moisture during assembly |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Analysis** | Insulation resistance calculation for conformal-coated PCB |
| **Test** | MIL-STD-810H 507.6 Procedure III at certified chamber |
| **Functional Test During** | Power on system after each 24-hour cycle; verify BIT, accuracy, insulation resistance |
| **Post-Test Inspection** | Open enclosure after final cycle; inspect for internal condensation, corrosion, coating delamination |
| **Pass/Fail Criteria** | System fully operational after each cycle; insulation resistance >100 Mohm; no visible corrosion; conformal coating intact; no intermittent faults |
| **Estimated Duration** | 12 days (10 cycles + setup + post-inspection) |
| **Estimated Cost** | $4,000-6,000 |

---

### 2.4 Method 509.7 - Salt Fog

| Parameter | Detail |
|-----------|--------|
| **Method** | 509.7 Salt Fog (Corrosion) |
| **Applicable Procedure** | Procedure I - Salt Fog Exposure |
| **Test Condition** | 5% NaCl solution by weight; 35C (+/-2C); 48-hour exposure |
| **Sample Orientation** | Operational mounting orientation (sensor bar horizontal, enclosure vertical/angled) |
| **pH Range** | 6.5 to 7.2 (neutral salt fog) |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| Hard anodize Type III (25um) per MIL-A-8625F | Aluminum corrosion barrier; salt spray rated >336 hours |
| UV-resistant paint over anodize (RAL 6031) | Secondary corrosion barrier |
| SS 316 fasteners throughout | Superior pitting resistance in chloride environments (PREN = 24) |
| Nylon washers at Al/SS interfaces | Eliminates galvanic couple (Al/SS, -0.5V potential difference) |
| Nickel-plated connectors | No exposed copper or brass |
| EPDM gaskets (ozone + salt resistant) | Gasket material unaffected by NaCl |
| PUR cable jackets | Resistant to salt water degradation |
| No ventilation holes or unprotected openings | Full IP67 sealing |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Test** | MIL-STD-810H 509.7 Procedure I in salt fog chamber |
| **Post-Test Inspection** | Visual inspection per ASTM B117 rating scale; check all external surfaces, fastener heads, connector interfaces, gasket interfaces |
| **Functional Test After** | Full BIT cycle; TDOA accuracy check; connector mate/demate force measurement |
| **Pass/Fail Criteria** | No red rust on any surface; no white corrosion product on anodized surfaces exceeding 5% of area; all connectors fully functional; system operational; no degradation of IP67 seal |
| **Estimated Duration** | 4 days (48h exposure + 1 day inspection + 1 day functional test) |
| **Estimated Cost** | $2,000-3,500 |

---

### 2.5 Method 510.7 - Sand and Dust

| Parameter | Detail |
|-----------|--------|
| **Method** | 510.7 Sand and Dust |
| **Applicable Procedure** | Procedure I - Blowing Dust (<150um particles) |
| **Test Condition** | Wind velocity 8.9 m/s (29 ft/s); dust concentration 10.6 +/-7 g/m3; temperature 60C +/-3C; humidity <30% RH |
| **Dust Type** | Red China clay or equivalent (140 mesh passing) |
| **Duration** | 6 hours blowing dust |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| IP67 enclosure (IP6X = dust-tight) | No penetration of dust into enclosure |
| No ventilation openings | Fully sealed enclosure design |
| IP67 panel-mount connectors (Amphenol RJFTV) | Connectors sealed when mated; dust caps for unmated |
| MEMS microphones sealed with rubber boot | Vietnamese natural rubber boot isolates sensor from dust |
| Cam-lever clamps (stainless steel) | No moving parts affected by dust ingress |
| Hard anodize surface | Abrasion-resistant surface coating |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Test** | MIL-STD-810H 510.7 Procedure I in sand/dust chamber |
| **Inspection After** | Disassemble and inspect for dust penetration at all sealing interfaces |
| **Functional Test After** | System power-on, BIT, TDOA accuracy verification |
| **Pass/Fail Criteria** | No dust penetration into enclosure interior; all connector seals intact; system fully operational; no audible/acoustic degradation from dust on sensor boots |
| **Estimated Duration** | 2 days (6h exposure + cleaning + inspection + functional test) |
| **Estimated Cost** | $2,500-4,000 |

---

### 2.6 Method 514.8 - Vibration

| Parameter | Detail |
|-----------|--------|
| **Method** | 514.8 Vibration |
| **Applicable Procedure** | Procedure I - General Vibration; Category 4 - Composite Wheeled Vehicle |
| **Test Type** | Random vibration (broadband) |
| **Frequency Range** | 5 Hz to 500 Hz |
| **Test Levels (Cat 4)** | Vertical: 1.04 grms; Lateral/Longitudinal: 0.2 grms |
| **Duration** | 60 minutes per axis (3 axes = 180 minutes total) |
| **Configuration** | Packed in transport case (transport exposure) |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| PCB rubber isolator standoffs (4x per PCB) | Attenuates vibration at PCB mounting (resonance damping) |
| 4mm aluminum enclosure walls | Structural rigidity; high first-mode frequency (>200 Hz estimated) |
| No unsupported PCB spans >80mm | Prevents board flexural resonance within excitation band |
| Battery pack strapped and foam-padded | Prevents battery movement within enclosure |
| All connectors torqued to spec | Prevents connector back-out from vibration |
| Wire harness strain-relieved and tie-wrapped | No free-hanging wires to fatigue |
| Rotomolded PE transport case with custom foam | Vibration isolation during transport |
| Lock-wire on critical fasteners (enclosure lid bolts) | Prevents bolt loosening |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Analysis** | FEA modal analysis of enclosure + PCB assembly; verify first mode >200 Hz |
| **Test** | MIL-STD-810H 514.8, Cat 4, random vibration on electrodynamic shaker |
| **Monitoring During** | Accelerometer on PCB; system powered and operating; continuous BIT monitoring |
| **Functional Test After** | Full functional test; TDOA accuracy; visual inspection for loosened fasteners |
| **Pass/Fail Criteria** | System operates throughout vibration; no intermittent faults; no hardware failures; all fasteners remain tight; no permanent deformation; TDOA accuracy within +/-10mm post-test |
| **Estimated Duration** | 3 days (setup + 3 axes + functional test + inspection) |
| **Estimated Cost** | $5,000-8,000 |

---

### 2.7 Method 516.8 - Shock

| Parameter | Detail |
|-----------|--------|
| **Method** | 516.8 Shock |
| **Applicable Procedure** | Procedure I - Functional Shock |
| **Shock Pulse** | Half-sine, 40g peak, 11ms duration |
| **Number of Shocks** | 3 shocks in each direction on each of 3 axes = 18 total shocks |
| **Configuration** | Operational (powered on) |

**Design Features Ensuring Compliance:**

| Feature | Contribution |
|---------|-------------|
| PCB rubber isolator standoffs | Shock attenuation at PCB mount points |
| 4mm aluminum walls + 6mm base plate | Structural integrity under 40g acceleration |
| Battery retention strap (stainless steel cam buckle) | Prevents battery mass displacement under 40g (battery = 3.5 kg = 1,372N at 40g) |
| M4 enclosure lid bolts x 8 at 2.5Nm torque | Lid retention under shock (combined bolt shear capacity >5,000N) |
| Sensor daughter PCBs screw-mounted (2x M2 each) | Retains 5g MEMS mic assemblies under 40g shock |
| Flash memory (no HDD) | No mechanical storage failure mode |
| Through-hole connectors (RJ45, power) soldered to PCB | No purely friction-fit connections that could dislodge |
| LIS2DH12 accelerometer monitors shock events | Logs shock exposure for health monitoring |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Analysis** | Stress analysis of battery retention under 40g; PCB standoff deflection calculation |
| **Test** | MIL-STD-810H 516.8 Procedure I on shock machine or drop table |
| **Monitoring During** | System powered on; BIT status logged; accelerometer data recorded |
| **Functional Test After** | Complete functional test; TDOA accuracy; internal visual inspection |
| **Pass/Fail Criteria** | System operates throughout all 18 shocks; no intermittent faults during or after; no displaced components; battery retention intact; TDOA accuracy within +/-10mm |
| **Estimated Duration** | 2 days (setup + 18 shocks + functional test + inspection) |
| **Estimated Cost** | $3,000-5,000 |

---

### 2.8 Method 521.4 - Icing/Freezing Rain

| Parameter | Detail |
|-----------|--------|
| **Method** | 521.4 Icing/Freezing Rain |
| **Applicable Procedure** | Procedure I - Icing/Freezing Rain |
| **Test Condition** | Temperature: -10C to -5C; freezing rain/mist accretion; ice thickness 13mm on exposed surfaces |
| **Duration** | 4 hours of ice accretion + 3 hours cold soak at -10C |

**Applicability Assessment for Vietnamese Deployment:**

| Factor | Assessment |
|--------|------------|
| **Vietnamese climate** | Tropical; icing is NOT expected in typical deployment locations |
| **Northern highlands (Sa Pa, Lao Cai)** | Occasional frost/sleet in winter (December-February); light icing possible |
| **Export markets** | ASEAN countries are tropical; icing unlikely |
| **Risk assessment** | LOW - Icing is not a primary design driver for VN-TRN-001 |

**Design Features (Inherent Compliance):**

| Feature | Contribution |
|---------|-------------|
| Low operating temperature rated to -10C | System operates in icing conditions |
| No moving parts on exterior | No freeze-up of mechanisms |
| IP67 sealing | Ice meltwater does not penetrate |
| Cam-lever clamps (stainless steel) | Operable with gloves; ice buildup on lever is tolerable |
| Sensor rubber boots | Acoustic coupling maintained through thin ice layer (shockwave energy >> ice impedance) |

**Verification Approach:**

| Method | Detail |
|--------|--------|
| **Approach** | Analysis + limited test (NOT full MIL-STD-810H test) |
| **Rationale** | Vietnamese deployment: icing probability <1%; cost of full test not justified for initial production |
| **Analysis** | Confirm no mechanisms affected by ice; confirm acoustic coupling through ice |
| **If Required Later** | Add icing test for export variants to temperate-climate countries |
| **Pass/Fail Criteria (Analysis)** | No icing-vulnerable mechanisms identified; acoustic performance analytically unaffected |
| **Estimated Cost** | $500 (analysis only); $3,000-5,000 if full test required |

---

### 2.9 MIL-STD-810H Summary

| Method | Test | Severity | Duration | Cost Est. | Status |
|--------|------|----------|----------|-----------|--------|
| 501.7 | High Temperature | +60C op / +70C stor | 14 days | $3,000-5,000 | Designed |
| 502.7 | Low Temperature | -10C op / -40C stor | 5 days | $2,500-4,000 | Designed |
| 507.6 | Humidity | 95% RH, 40C, 10 cycles | 12 days | $4,000-6,000 | Designed |
| 509.7 | Salt Fog | 5% NaCl, 48 hours | 4 days | $2,000-3,500 | Designed |
| 510.7 | Sand/Dust | Procedure I, 6 hours | 2 days | $2,500-4,000 | Designed |
| 514.8 | Vibration | Cat 4, random, 3 axes | 3 days | $5,000-8,000 | Designed |
| 516.8 | Shock | 40g, 11ms, 18 pulses | 2 days | $3,000-5,000 | Designed |
| 521.4 | Icing | -10C, 13mm ice | Analysis only | $500 | Designed |
| | **TOTAL** | | **~42 days** | **$22,500-40,500** | |

---

## 3. MIL-STD-461G EMC COMPLIANCE

### 3.1 Applicable Requirements

The BSU-V1 is classified as a **Ground, Fixed Installation** per MIL-STD-461G Table II. The following requirements apply:

| Requirement | Title | Frequency Range | Limit | Applicability |
|-------------|-------|-----------------|-------|---------------|
| RE102 | Radiated Emissions, Electric Field | 10 kHz - 18 GHz | Per Figure RE102-2 (Ground) | All electronic emissions from BSU-V1 |
| CE102 | Conducted Emissions, Power Leads | 10 kHz - 10 MHz | Per Figure CE102-1 | Power input cable emissions |
| RS103 | Radiated Susceptibility, Electric Field | 10 kHz - 18 GHz | 10 V/m (general), 20 V/m (specified areas) | Immunity to external RF |
| CS101 | Conducted Susceptibility, Power Leads | 30 Hz - 150 kHz | Per Figure CS101-1 | Power line noise immunity |

### 3.2 RE102 - Radiated Emissions

| Parameter | Detail |
|-----------|--------|
| **Frequency Range** | 10 kHz to 18 GHz |
| **Limit** | Per MIL-STD-461G Figure RE102-2 (e.g., ~24 dBuV/m at 10 kHz, decreasing to ~20 dBuV/m at 10 MHz, then ~24 dBuV/m at 18 GHz) |
| **Measurement Distance** | 1 meter |
| **Antenna** | Rod (below 30 MHz), biconical (30-200 MHz), horn (above 200 MHz) |

**Emission Sources in BSU-V1:**

| Source | Frequency | Risk Level |
|--------|-----------|------------|
| FPGA clock (48 MHz + harmonics) | 48 MHz, 96 MHz, 144 MHz... | HIGH |
| MCU clock (480 MHz + harmonics) | 480 MHz, 960 MHz... | HIGH |
| Ethernet PHY (25 MHz reference) | 25 MHz and harmonics | MEDIUM |
| DC-DC converters (switching freq 500 kHz-1 MHz) | 500 kHz - 3 MHz | MEDIUM |
| SPI bus (FPGA to ADC, up to 20 MHz) | 20 MHz and harmonics | LOW |

**Design Features for RE102 Compliance:**

| Feature | Shielding Effectiveness | Detail |
|---------|------------------------|--------|
| **Al 6061-T6 enclosure (4mm wall)** | >80 dB at 1 GHz | Continuous aluminum enclosure acts as Faraday cage; skin depth of Al at 100 MHz = 8.5um << 4mm wall |
| **Conductive gasket at lid/body interface** | >60 dB | EPDM gasket with embedded conductive mesh (BeCu fingerstock at 4 screw locations) OR conductive EMI gasket at lid perimeter |
| **IP67 filtered RJ45 connector** | >40 dB common-mode | Amphenol RJFTV with integrated magnetics (1000BaseT transformer provides >40 dB CM rejection) |
| **Pi-filter on power input** | >60 dB at 10 MHz | Common-mode choke (10mH) + 2x 100nF Y-caps + 10uF X-cap at power connector |
| **Shielded sensor cable (500mm)** | >40 dB | Braided shield with 360-degree termination at both connectors |
| **4-layer PCB with continuous ground plane** | N/A (internal) | Layer 2 = solid ground plane; minimizes loop area for high-speed signals |
| **Spread-spectrum clocking on FPGA** | -10 dB peak reduction | iCE40UP5K supports +/-0.5% spread spectrum on PLL output |
| **Decoupling capacitors (100nF + 10uF per IC)** | N/A (internal) | Reduces high-frequency current loops |

**Estimated Shielding Effectiveness of Complete Enclosure:**

| Frequency | Enclosure SE | Connector/Gasket SE | Limiting Factor | Effective SE |
|-----------|-------------|---------------------|-----------------|-------------|
| 100 kHz | >100 dB | >60 dB | Connector filter | >60 dB |
| 10 MHz | >100 dB | >60 dB | Power filter | >60 dB |
| 100 MHz | >80 dB | >50 dB | Gasket gaps | >50 dB |
| 1 GHz | >80 dB | >40 dB | Connector aperture | >40 dB |
| 10 GHz | >60 dB | >30 dB | Any aperture >3mm | >30 dB |

**Assessment:** With >30 dB effective shielding at all frequencies and typical internal emissions of <60 dBuV/m at 1m, the design provides >20 dB margin against RE102 limits. **Compliance expected.**

### 3.3 CE102 - Conducted Emissions on Power Leads

| Parameter | Detail |
|-----------|--------|
| **Frequency Range** | 10 kHz to 10 MHz |
| **Limit** | Per MIL-STD-461G Figure CE102-1 (e.g., ~94 dBuV at 10 kHz, decreasing to ~60 dBuV at 500 kHz, then ~60 dBuV to 10 MHz) |
| **Measurement** | LISN (Line Impedance Stabilization Network) on power leads |

**Design Features for CE102 Compliance:**

| Feature | Detail |
|---------|--------|
| **Pi-filter at power input connector** | Common-mode choke (Murata DLW21HN, 10mH) + 2x 100nF Y-capacitors (ceramic, 50V) + 10uF X-capacitor (film) |
| **TVS diode (SMAJ58A)** | Transient suppression at power entry |
| **Separate analog/digital power rails** | TPS62160 (3.3V analog) isolated from TPS54331 (5V digital) |
| **DC-DC converter layout** | Input capacitor (ceramic 22uF) placed <5mm from converter VIN pin; tight loop area |
| **Battery as internal power source** | When running on battery, external power leads are disconnected = no CE102 emissions on power port |

**Assessment:** Pi-filter provides >60 dB attenuation in CE102 frequency range. Battery operation eliminates conducted emissions entirely. **Compliance expected.**

### 3.4 RS103 - Radiated Susceptibility

| Parameter | Detail |
|-----------|--------|
| **Frequency Range** | 10 kHz to 18 GHz |
| **Test Level** | 10 V/m (general ground environment) |
| **Modulation** | 1 kHz, 80% AM modulation |

**Design Features for RS103 Compliance:**

| Feature | Contribution |
|---------|-------------|
| **Al enclosure (4mm wall) = Faraday cage** | >60 dB shielding at all frequencies = field inside enclosure <0.01 V/m at 10 V/m external |
| **Shielded cables with 360-degree termination** | Prevents cable-coupled RF ingress |
| **Filtered I/O connectors** | Common-mode chokes on Ethernet; pi-filter on power |
| **Sensor cable shielding** | Braided shield with drain wire; terminated at both ends |
| **PCB ground plane (Layer 2)** | Low-impedance return path reduces susceptibility of internal traces |

**Susceptibility Concern Areas:**

| Area | Risk | Mitigation |
|------|------|------------|
| MEMS microphone acoustic coupling | MEMS mic has RF susceptibility if unshielded | Rubber boot + metal sensor bar housing provides shielding; mic analog path has 1kHz HPF rejecting RF demodulation |
| Ethernet cable as antenna | Unshielded cable length (50m) could couple RF | Shielded CAT6 cable; integrated magnetics with CM rejection; Ethernet PHY has inherent noise immunity |
| Power cable as antenna | Power cable (when external) could couple RF | Pi-filter at power entry; TVS diode for transient protection |

**Assessment:** Aluminum enclosure provides >60 dB shielding against 10 V/m field. Internal field will be <0.01 V/m, far below susceptibility thresholds of modern ICs. **Compliance expected.**

### 3.5 CS101 - Conducted Susceptibility on Power Leads

| Parameter | Detail |
|-----------|--------|
| **Frequency Range** | 30 Hz to 150 kHz |
| **Test Level** | Per Figure CS101-1: ~5V pp at 30 Hz decreasing to ~1V pp at 150 kHz (superimposed on DC power) |

**Design Features for CS101 Compliance:**

| Feature | Contribution |
|---------|-------------|
| **Input protection (TVS + reverse polarity MOSFET)** | Handles large transients (50V per ENG-08) |
| **Wide input range DC-DC converters** | TPS54331 operates 10.5-28V; rejects input ripple >70 dB |
| **Input bulk capacitance** | 2x 100uF electrolytic + 22uF ceramic at power entry |
| **Pi-filter on power input** | Attenuates injected signals >60 dB above 10 kHz |
| **Battery operation mode** | Internal battery isolates electronics from external power lead |
| **BMS IC (BQ76940) input filtering** | Charger input has additional LC filtering |

**Assessment:** DC-DC converters inherently reject input noise. Pi-filter provides additional attenuation. Battery mode eliminates susceptibility path entirely. **Compliance expected.**

### 3.6 MIL-STD-461G Summary

| Requirement | Frequency Range | Design Margin | Key Feature | Status |
|-------------|----------------|---------------|-------------|--------|
| RE102 | 10 kHz - 18 GHz | >20 dB estimated | Al enclosure + filtered I/O | Designed |
| CE102 | 10 kHz - 10 MHz | >20 dB estimated | Pi-filter + battery mode | Designed |
| RS103 | 10 kHz - 18 GHz | >50 dB estimated | Al enclosure (Faraday cage) | Designed |
| CS101 | 30 Hz - 150 kHz | >30 dB estimated | DC-DC rejection + pi-filter | Designed |

**Note on TCVN 6450:** Vietnamese EMC standard TCVN 6450 is based on CISPR 22/32 (now CISPR 32:2015), which specifies Class A (industrial) or Class B (residential) emission limits. MIL-STD-461G RE102/CE102 limits are generally MORE stringent than CISPR Class A. Therefore, passing MIL-STD-461G automatically satisfies TCVN 6450 Class A requirements.

---

## 4. MIL-STD-882E SYSTEM SAFETY

### 4.1 Hazard Analysis Methodology

Per MIL-STD-882E, hazard analysis uses a risk matrix combining **Severity** (I-IV) and **Probability** (A-E):

**Severity Categories:**

| Category | Description | BSU-V1 Interpretation |
|----------|-------------|----------------------|
| I - Catastrophic | Death or system loss | Fatality on range |
| II - Critical | Severe injury, major system damage | Serious injury, BSU destroyed |
| III - Marginal | Minor injury, minor system damage | Minor injury, degraded performance |
| IV - Negligible | Less than minor injury | Nuisance, cosmetic damage |

**Probability Levels:**

| Level | Description | BSU-V1 Interpretation |
|-------|-------------|----------------------|
| A - Frequent | Likely to occur often | >1 in 100 unit-years |
| B - Probable | Will occur several times | 1 in 100 to 1 in 1,000 unit-years |
| C - Occasional | Likely to occur sometime | 1 in 1,000 to 1 in 10,000 unit-years |
| D - Remote | Unlikely but possible | 1 in 10,000 to 1 in 100,000 unit-years |
| E - Improbable | So unlikely, may never occur | <1 in 100,000 unit-years |

**Risk Assessment Matrix:**

| | Frequent (A) | Probable (B) | Occasional (C) | Remote (D) | Improbable (E) |
|---|---|---|---|---|---|
| **I - Catastrophic** | HIGH | HIGH | HIGH | SERIOUS | MEDIUM |
| **II - Critical** | HIGH | HIGH | SERIOUS | SERIOUS | MEDIUM |
| **III - Marginal** | HIGH | SERIOUS | MEDIUM | MEDIUM | LOW |
| **IV - Negligible** | SERIOUS | MEDIUM | MEDIUM | LOW | LOW |

### 4.2 Hazard 1: Li-Ion Battery Thermal Runaway

| Parameter | Detail |
|-----------|--------|
| **Hazard ID** | HAZ-001 |
| **Hazard** | Li-ion battery thermal runaway leading to fire or explosion |
| **Severity** | II - Critical (fire/burns, BSU destroyed) |
| **Probability** | D - Remote (BMS-protected cells, proven Samsung chemistry) |
| **Initial Risk** | SERIOUS |
| **Related Requirements** | SAF-04, ENG-04 |

**Hazard Analysis:**

| Cause | Mechanism | Likelihood |
|-------|-----------|------------|
| External short circuit | Damaged cable or connector fault shorts battery terminals | Remote - fused protection |
| Internal cell defect | Manufacturing defect in Samsung INR18650-35E cell | Remote - production screening by Samsung |
| Overcharge | Charger malfunction continues charging past 4.2V/cell | Remote - BMS independent of charger |
| Over-discharge | Deep discharge below 2.5V/cell causes dendrite growth on subsequent charge | Remote - BMS cutoff at 2.7V/cell |
| Mechanical crush | Physical damage to battery from impact/crush | Remote - enclosed in 4mm aluminum |
| External heat | Ambient temperature above 80C (thermal management failure) | Improbable - max operating 60C, derating 20C |

**Mitigation Measures:**

| # | Mitigation | Type | Effectiveness |
|---|-----------|------|---------------|
| M1 | BMS IC (TI BQ76940) with independent over-voltage, under-voltage, over-current, short-circuit, and over-temperature protection | Design (hardware) | High - independent safety IC |
| M2 | PTC fuse on each cell (internal to Samsung 35E) | Design (cell-level) | High - irreversible above 120C |
| M3 | Pack-level fuse (5A fast-blow) on battery output | Design (pack-level) | High - limits short-circuit current |
| M4 | UN 38.3 tested cells (Samsung INR18650-35E has certification) | Procurement | High - proven chemistry |
| M5 | Battery isolated from electronics by fire-retardant separator (ceramic fiber sheet) | Design (thermal barrier) | Medium - buys evacuation time |
| M6 | 4mm aluminum enclosure acts as fire containment | Design (containment) | Medium - contains small cell fire |
| M7 | Thermal fuse (95C) on battery pack disconnects before runaway | Design (thermal) | High - kills power before runaway temperature |
| M8 | BIT monitors battery temperature via BQ27441 fuel gauge; alarm at 55C | Software (warning) | Medium - operator warning |

**Residual Risk After Mitigation:**

| Parameter | Value |
|-----------|-------|
| Severity | II - Critical (unchanged - if thermal runaway occurs, consequence is critical) |
| Probability | E - Improbable (multiple independent protections; requires simultaneous failure of BMS + PTC + thermal fuse) |
| **Residual Risk** | **MEDIUM** - Acceptable with monitoring |

---

### 4.3 Hazard 2: Electrical Shock

| Parameter | Detail |
|-----------|--------|
| **Hazard ID** | HAZ-002 |
| **Hazard** | Electrical shock to operator or maintenance personnel |
| **Severity** | III - Marginal (all voltages <50V DC; cannot deliver lethal shock) |
| **Probability** | E - Improbable (no user-accessible voltages above SELV) |
| **Initial Risk** | LOW |
| **Related Requirements** | SAF-01, SAF-03 |

**Hazard Analysis:**

| Cause | Mechanism | Likelihood |
|-------|-----------|------------|
| Contact with battery terminals | Maintenance personnel contacts exposed 14.8V terminals | Improbable - battery in sealed compartment |
| Charger fault | External AC-DC adapter develops fault, passes mains to output | Improbable - adapter is IEC 62368-1 certified with double insulation |
| Wet conditions + low voltage | Wet hands contact 14.8V battery | Improbable - IP67 sealing; 14.8V is below 60V DC SELV threshold |

**Mitigation Measures:**

| # | Mitigation | Type | Effectiveness |
|---|-----------|------|---------------|
| M1 | Maximum system voltage = 14.8V DC (battery) / 28V DC (external) | Design | High - below 60V DC SELV limit per IEC 62368-1 |
| M2 | IP67 enclosure prevents user contact with any internal voltage | Design | High - no accessible live parts |
| M3 | External AC-DC adapter (IEC 62368-1 certified, Class II double insulation) | Procurement | High - no mains voltage at BSU |
| M4 | Battery door interlock (magnetic reed switch disconnects battery when door open) | Design | Medium - reduces risk during maintenance |
| M5 | Maintenance manual specifies battery disconnect before PCB service | Procedure | Medium - procedural control |

**Residual Risk After Mitigation:**

| Parameter | Value |
|-----------|-------|
| Severity | III - Marginal (unchanged) |
| Probability | E - Improbable (no credible shock path to user) |
| **Residual Risk** | **LOW** - Acceptable |

---

### 4.4 Hazard 3: Projectile Deflection by BSU

| Parameter | Detail |
|-----------|--------|
| **Hazard ID** | HAZ-003 |
| **Hazard** | BSU components deflect a projectile toward range personnel |
| **Severity** | I - Catastrophic (redirected projectile could cause fatality) |
| **Probability** | E - Improbable (sensor bar is below target; geometry prevents deflection toward personnel) |
| **Initial Risk** | MEDIUM |
| **Related Requirements** | SAF-02 |

**Hazard Analysis:**

| Cause | Mechanism | Likelihood |
|-------|-----------|------------|
| Direct hit on sensor bar | 7.62mm bullet strikes aluminum bar at 800+ m/s | Remote - sensor bar is at bottom of target frame, outside normal aim point |
| Direct hit on processing enclosure | Bullet strikes enclosure mounted behind/below frame | Improbable - enclosure is behind frame, shielded by target backing |
| Ricochet off angled surface | Bullet strikes angled aluminum surface and redirects | Improbable - 4mm Al at 90 degrees will be perforated, not deflected |

**Deflection Physics Analysis:**

| Parameter | Value |
|-----------|-------|
| Sensor bar material | Al 6063-T5, 3mm wall |
| 5.56mm NATO at 300m impact velocity | ~700 m/s |
| 5.56mm penetration of 3mm aluminum | Clean perforation (far exceeds yield strength) |
| Deflection probability on flat surface at ~90 degrees | <1% (clean penetration) |
| Deflection probability on angled impact (<15 degrees) | Possible but sensor bar is horizontal = 90-degree impact from horizontal fire |

**Mitigation Measures:**

| # | Mitigation | Type | Effectiveness |
|---|-----------|------|---------------|
| M1 | Sensor bar mounted at bottom of target frame (below silhouette) | Installation (geometry) | High - aimed shots are above sensor bar |
| M2 | Low-profile sensor bar (60mm x 40mm cross-section) | Design | High - minimal exposed area |
| M3 | Processing enclosure mounted behind or below target frame | Installation | High - shielded by frame structure |
| M4 | No angled deflection surfaces (all flat or perpendicular to firing line) | Design | Medium - reduces ricochet probability |
| M5 | Range safety procedures (BSU installation behind firing line prohibited) | Procedure | High - operational control |
| M6 | Optional ballistic backing plate (3mm AR500 steel) behind sensor bar for close-range installations (<100m) | Design (optional) | High - absorbs projectile energy |

**Residual Risk After Mitigation:**

| Parameter | Value |
|-----------|-------|
| Severity | I - Catastrophic (unchanged - any redirected projectile is potentially lethal) |
| Probability | E - Improbable (geometry + installation prevents any credible deflection path toward personnel) |
| **Residual Risk** | **MEDIUM** - Acceptable with range safety procedures |

---

### 4.5 Hazard 4: RF Interference with Range Communications

| Parameter | Detail |
|-----------|--------|
| **Hazard ID** | HAZ-004 |
| **Hazard** | BSU electromagnetic emissions interfere with range communication equipment (VHF radios, telephone, intercom) |
| **Severity** | III - Marginal (loss of range communication could delay cease-fire command) |
| **Probability** | D - Remote (MIL-STD-461G compliant design) |
| **Initial Risk** | MEDIUM |
| **Related Requirements** | SAF-05, SIG-01, SIG-02 |

**Hazard Analysis:**

| Cause | Mechanism | Likelihood |
|-------|-----------|------------|
| BSU radiated emissions on VHF band | FPGA/MCU clock harmonics in 136-174 MHz VHF range | Remote - aluminum enclosure provides >60 dB shielding |
| WiFi interference (802.11n, 2.4 GHz) | WiFi module in BSU interferes with 2.4 GHz range equipment | Occasional - if range uses 2.4 GHz equipment |
| Ethernet cable emissions | 50m Ethernet cable radiates as antenna | Remote - shielded CAT6 cable |

**Mitigation Measures:**

| # | Mitigation | Type | Effectiveness |
|---|-----------|------|---------------|
| M1 | MIL-STD-461G RE102 compliant design (aluminum enclosure Faraday cage) | Design | High - >60 dB shielding |
| M2 | WiFi channel management (avoid channels used by range comms) | Software/configuration | Medium - requires coordination |
| M3 | WiFi power management (minimum required transmit power) | Software | Medium - limits interference radius |
| M4 | Pre-installation EMC survey of range communications | Procedure | Medium - identifies potential conflicts |
| M5 | Shielded Ethernet cables (CAT6 STP) | Design | High - contains cable emissions |

**Residual Risk After Mitigation:**

| Parameter | Value |
|-----------|-------|
| Severity | III - Marginal (unchanged) |
| Probability | E - Improbable (MIL-STD-461G compliance + shielded enclosure) |
| **Residual Risk** | **LOW** - Acceptable |

---

### 4.6 Hazard 5: Fire from Battery or Electrical Fault

| Parameter | Detail |
|-----------|--------|
| **Hazard ID** | HAZ-005 |
| **Hazard** | Electrical fire from battery fault, wiring fault, or component failure igniting internal materials or surrounding vegetation |
| **Severity** | II - Critical (fire could spread to range vegetation, especially in dry season; equipment destroyed) |
| **Probability** | D - Remote (multiple protection layers) |
| **Initial Risk** | SERIOUS |
| **Related Requirements** | SAF-01, SAF-04, ENG-08 |

**Hazard Analysis:**

| Cause | Mechanism | Likelihood |
|-------|-----------|------------|
| Battery thermal runaway | See HAZ-001 - Li-ion cell fire | Remote (mitigated by HAZ-001 measures) |
| Wiring harness short circuit | Chafed wire contacts metal enclosure, draws overcurrent | Remote - all wires strain-relieved, sleeved |
| Component failure (resistor overheating) | PCB component fails short, dissipates excessive power | Remote - conservative derating (50% voltage, 75% current) |
| External fire (range fire reaches BSU) | Brush/grass fire contacts BSU during dry season | Occasional - Vietnamese dry season fire risk |

**Mitigation Measures:**

| # | Mitigation | Type | Effectiveness |
|---|-----------|------|---------------|
| M1 | All HAZ-001 battery mitigations apply | Design | High - prevents battery fire initiation |
| M2 | Pack-level fuse (5A fast-blow) on battery output | Design | High - limits fault current |
| M3 | Polyfuse (PTC) on each DC-DC converter output | Design | High - resets after fault clears |
| M4 | FR-4 Tg170 PCB substrate (UL94 V-0 rated, self-extinguishing) | Design | High - PCB will not sustain combustion |
| M5 | No flammable materials inside enclosure (no foam, no plastic housings) | Design | High - only Al, FR-4, EPDM, ceramic |
| M6 | Aluminum enclosure (non-flammable, contains internal fire) | Design | High - fire cannot escape sealed enclosure |
| M7 | Wire harness: PTFE-insulated wire with ETFE sleeving | Design | High - self-extinguishing insulation |
| M8 | BIT over-temperature alarm at 55C (battery) and 70C (enclosure internal) | Software | Medium - early warning |
| M9 | Installation: maintain 0.5m clearance from vegetation | Procedure | Medium - reduces vegetation fire risk |

**Residual Risk After Mitigation:**

| Parameter | Value |
|-----------|-------|
| Severity | II - Critical (unchanged - fire consequence is critical if it occurs) |
| Probability | E - Improbable (multiple fuse/thermal protections + non-flammable materials + sealed enclosure) |
| **Residual Risk** | **MEDIUM** - Acceptable with monitoring |

---

### 4.7 MIL-STD-882E Hazard Summary

| Hazard ID | Hazard | Severity | Initial Prob. | Initial Risk | Mitigations | Residual Prob. | Residual Risk |
|-----------|--------|----------|--------------|-------------|-------------|---------------|--------------|
| HAZ-001 | Battery thermal runaway | II - Critical | D - Remote | SERIOUS | 8 mitigations (BMS, fuses, thermal barriers) | E - Improbable | **MEDIUM** |
| HAZ-002 | Electrical shock | III - Marginal | E - Improbable | LOW | 5 mitigations (SELV, IP67, Class II adapter) | E - Improbable | **LOW** |
| HAZ-003 | Projectile deflection | I - Catastrophic | E - Improbable | MEDIUM | 6 mitigations (geometry, installation, optional ballistic plate) | E - Improbable | **MEDIUM** |
| HAZ-004 | RF interference | III - Marginal | D - Remote | MEDIUM | 5 mitigations (461G compliance, shielded cables) | E - Improbable | **LOW** |
| HAZ-005 | Fire (battery/electrical) | II - Critical | D - Remote | SERIOUS | 9 mitigations (fuses, V-0 materials, Al containment) | E - Improbable | **MEDIUM** |

**Overall Safety Assessment:** All hazards reduced to MEDIUM or LOW residual risk. No HIGH or SERIOUS residual risks remain. The design is **acceptable** for operational deployment per MIL-STD-882E risk acceptance criteria.

---

## 5. IEC 62368-1 / IEC 60529 / UN 38.3

### 5.1 IEC 62368-1 - Audio/Video/ICT Equipment Safety

| Clause | Requirement | BSU-V1 Compliance | Design Feature |
|--------|------------|-------------------|----------------|
| 5.2 | Energy source classification | ES1 (<=20V DC / <100VA) | Max voltage = 14.8V battery / 28V external input; power = 15W << 100VA |
| 5.3 | Safeguards (one for ES1) | Basic insulation | IP67 enclosure provides complete enclosure of all energy sources |
| 6.2 | Electric shock | SELV circuit (<60V DC) | All user-accessible circuits <= 28V DC |
| 6.4 | Protective earthing | Not required (Class III equipment) | Battery-powered; no mains connection at BSU; external adapter is Class II |
| 9.2 | Temperature of accessible parts | Accessible surface temp <=60C at max operating | Al enclosure: at 60C ambient + 15W internal, surface <=75C; IP67 prevents contact with internal hot spots |
| 10 | Mechanical hazards | No sharp edges, pinch points | All enclosure edges have 1mm chamfer; gasket-sealed interfaces |
| 14 | Components | All components to IEC 62368-1 or equivalent | DC-DC converters, ICs from compliant manufacturers (TI, Microchip, Lattice) |

**IEC 62368-1 Assessment:** BSU-V1 is a Class III (battery-powered) device with ES1 energy sources. The combination of low voltage (<28V DC), IP67 enclosure, and external Class II adapter results in a straightforward compliance path.

### 5.2 IEC 60529 - IP67 Ingress Protection

**IP67 Definition:** IP6X (dust-tight) + IPX7 (temporary immersion)

#### IP6X - Dust-Tight Test

| Parameter | Detail |
|-----------|--------|
| **Test Method** | IEC 60529 Clause 13.4 |
| **Condition** | Talcum powder (particle size <75um) at 2 kPa underpressure inside enclosure |
| **Duration** | 8 hours |
| **Pass Criteria** | No ingress of dust deposits that could interfere with satisfactory operation or impair safety |

#### IPX7 - Temporary Immersion Test

| Parameter | Detail |
|-----------|--------|
| **Test Method** | IEC 60529 Clause 14.2.7 |
| **Condition** | Immersion in water, enclosure bottom at 1m depth |
| **Duration** | 30 minutes |
| **Water Temperature** | Ambient (within 5C of test article temperature, to prevent thermal breathing) |
| **Pass Criteria** | No ingress of water in any quantity |

**BSU-V1 IP67 Design Features:**

| Feature | Detail |
|---------|--------|
| **Enclosure body** | CNC machined from solid Al 6061-T6 billet; no joints except lid interface |
| **Lid-body interface** | EPDM O-ring (AS568A), captured in machined groove; 8x M4 bolts at 2.5Nm provide uniform compression |
| **Connector penetrations** | 2x IP67 panel-mount connectors (Amphenol RJFTV for Ethernet, Souriau 8STA for power); factory-sealed bulkhead interface |
| **Sensor cable penetration** | IP67 circular connector (Amphenol) with rubber boot |
| **Battery door** | EPDM gasket + cam-latch with positive seal; captive gasket in groove |
| **Cable entry glands** | Not used (all entries via panel-mount connectors with factory sealing) |
| **Surface finish** | Hard anodize fills surface porosity of aluminum |
| **Assembly torque** | All lid bolts torqued to 2.5Nm with torque wrench; procedure documented |

**IP67 Verification Plan:**

| Step | Action |
|------|--------|
| 1 | Air pressure leak test at production (inflate enclosure to +10 kPa, hold 60s, leak rate <0.5 kPa/min) |
| 2 | Full IP67 immersion test on DV (Design Verification) units at test lab |
| 3 | Post-environmental (after MIL-STD-810H sequence) re-test IP67 to verify seal integrity |

### 5.3 UN 38.3 - Transport Testing of Lithium Batteries

The BSU-V1 battery pack (4S1P, 14.8V 10Ah, 148Wh) must pass all 8 UN 38.3 tests for air and ground transport.

**Battery Pack Specifications for UN 38.3:**

| Parameter | Value |
|-----------|-------|
| Cell type | Samsung INR18650-35E (lithium-ion, cylindrical) |
| Configuration | 4S1P (4 cells in series) |
| Nominal voltage | 14.8V (3.7V x 4) |
| Capacity | 10Ah (35E = 3,500mAh per cell, rounded to 10Ah for 3 parallel or using slightly higher-capacity binning) |
| Energy | 148 Wh |
| Classification | UN 38.3 Section 38.3.3 (rechargeable lithium-ion battery) |
| Watt-hour rating | >100 Wh (requires Class 9 dangerous goods labeling for air transport) |

**UN 38.3 Test Requirements (All 8 Tests):**

| Test | Title | Condition | Pass Criteria | BSU-V1 Design Feature |
|------|-------|-----------|---------------|----------------------|
| T.1 | Altitude Simulation | Pressure 11.6 kPa (equivalent to 15,000m altitude) for 6 hours | No mass loss, no venting, no fire, no explosion, no leakage; OCV change <5% | Sealed cylindrical cells (Samsung 35E UN 38.3 certified); BMS does not affect |
| T.2 | Thermal Test | 75C for 6h, then -40C for 6h; repeat 10 cycles | No mass loss, no venting, no fire, no explosion, no leakage | Cells rated -20C to +60C operating, -40C to +70C storage; BMS temperature monitoring |
| T.3 | Vibration | Sinusoidal 7 Hz to 200 Hz, 1 gn, 3 hours per axis | No mass loss, no venting, no fire, no explosion, no leakage | Spot-welded nickel strip connections (not soldered); pack structurally retained |
| T.4 | Shock | Half-sine 150g, 6ms, 3 shocks per direction per axis (18 total) | No mass loss, no venting, no fire, no explosion, no leakage | Cell retention via heat-shrink and structural frame; BMS board secured |
| T.5 | External Short Circuit | Short-circuit battery terminals through <0.1 ohm for 1 hour at 55C | External case temperature <170C; no fire, no explosion for 6 hours after test | Pack-level fuse (5A fast-blow) opens within milliseconds; BMS short-circuit protection (hardware) |
| T.6 | Impact/Crush | 9.1 kg mass dropped from 610mm onto cell placed on 15.8mm diameter bar | No fire, no explosion (cell level test) | Samsung INR18650-35E has existing UN 38.3 T.6 certification |
| T.7 | Overcharge | Charge at 2x rated current (2x 2A = 4A) or 2x rated voltage (2x 16.8V = 33.6V), whichever is less; 24 hours | No fire, no explosion for 7 days after test | BMS over-voltage cutoff at 4.25V/cell (17.0V pack); charge FET opens; secondary protection via cell PTC |
| T.8 | Forced Discharge | Discharge each cell at max rated current in series with 12V external source until Vcell = 0V | No fire, no explosion for 7 days after test | Samsung INR18650-35E has existing UN 38.3 T.8 certification at cell level |

**UN 38.3 Compliance Path:**

| Level | Approach | Status |
|-------|----------|--------|
| **Cell level** | Samsung INR18650-35E has existing UN 38.3 certification (available from Samsung SDI test reports) | **CERTIFIED** (use manufacturer certificate) |
| **Pack level** | BSU-V1 battery pack (4S1P + BMS) must be tested as a battery per UN 38.3 Section 38.3.3 | **TEST REQUIRED** |
| **Test lab** | UL, TUV, or SGS facility (Singapore or China) | Quote required |
| **Estimated cost** | $8,000-15,000 for complete UN 38.3 battery pack testing | |
| **Estimated duration** | 4-6 weeks (including thermal cycling) | |

---

## 6. TEST PLANNING

### 6.1 Test Article Requirements

| Designation | Quantity | Purpose | Configuration |
|-------------|----------|---------|---------------|
| **DV-1** (Design Verification #1) | 1 | Full environmental test sequence per MIL-STD-810H | Production-representative hardware |
| **DV-2** (Design Verification #2) | 1 | EMC testing per MIL-STD-461G; safety testing per IEC 62368-1 | Production-representative hardware |
| **PV-1** (Production Validation #1) | 1 | Repeat key environmental tests on production hardware | First-article production unit |
| **PV-2** (Production Validation #2) | 1 | Field trial unit (10-lane range installation) | First-article production unit |
| **Battery packs** | 3 | UN 38.3 testing (destructive; 3 packs consumed) | Production battery packs |
| **TOTAL** | **4 BSU units + 3 battery packs** | | |

### 6.2 Test Sequence (MIL-STD-810H Order)

Per MIL-STD-810H Part One, Section 3.1, the recommended test sequence minimizes the number of test articles and ensures cumulative stress effects are captured:

```
DV-1 TEST SEQUENCE (Environmental)
═══════════════════════════════════

Step 1: Baseline functional test (BIT + TDOA accuracy + IP67 pressure)
    │
Step 2: MIL-STD-810H 514.8 Vibration (Cat 4, 3 axes)
    │   Rationale: Vibration first to loosen any marginal connections
    │
Step 3: MIL-STD-810H 516.8 Shock (40g, 18 pulses)
    │   Rationale: Shock after vibration to compound mechanical stress
    │
Step 4: Functional test + internal inspection
    │
Step 5: MIL-STD-810H 501.7 High Temperature (60C, 7 days operating)
    │   Rationale: Thermal tests after mechanical
    │
Step 6: MIL-STD-810H 502.7 Low Temperature (-10C, 72 hours)
    │   Rationale: Low temp immediately after high temp = thermal cycling
    │
Step 7: Functional test
    │
Step 8: MIL-STD-810H 507.6 Humidity (95% RH, 10 cycles)
    │   Rationale: Humidity test after thermal cycling may reveal seal degradation
    │
Step 9: MIL-STD-810H 509.7 Salt Fog (48 hours)
    │   Rationale: Corrosion test after humidity test
    │
Step 10: MIL-STD-810H 510.7 Sand/Dust (Procedure I, 6 hours)
    │    Rationale: Dust test last (particles may affect subsequent tests)
    │
Step 11: Final functional test + IP67 re-test + detailed internal inspection
    │
Step 12: Tear-down inspection (destructive)
         Document all internal conditions, corrosion, component conditions
```

```
DV-2 TEST SEQUENCE (EMC + Safety)
══════════════════════════════════

Step 1: Baseline functional test
    │
Step 2: MIL-STD-461G RE102 (Radiated Emissions)
    │
Step 3: MIL-STD-461G CE102 (Conducted Emissions)
    │
Step 4: MIL-STD-461G RS103 (Radiated Susceptibility)
    │
Step 5: MIL-STD-461G CS101 (Conducted Susceptibility)
    │
Step 6: IEC 62368-1 Safety Tests (accessible touch temp, insulation, marking)
    │
Step 7: IEC 60529 IP67 Full Test (dust 8h + immersion 1m/30min)
    │
Step 8: Final functional test
```

```
BATTERY PACK TESTING (3 packs, destructive)
═══════════════════════════════════════════

Pack #1: UN 38.3 T.1 (Altitude) + T.2 (Thermal) + T.3 (Vibration) + T.4 (Shock)
Pack #2: UN 38.3 T.5 (External Short) + T.7 (Overcharge)
Pack #3: UN 38.3 T.8 (Forced Discharge) + reserve
    │
Note: T.6 (Impact/Crush) uses Samsung cell-level certification
```

### 6.3 Test Duration Estimate

| Test Phase | Tests | Duration | Parallel with |
|-----------|-------|----------|---------------|
| **DV-1 Environmental** | 810H full sequence | 8-10 weeks | — |
| **DV-2 EMC** | 461G RE/CE/RS/CS | 2-3 weeks | DV-1 (different unit) |
| **DV-2 Safety** | IEC 62368-1 + IP67 | 1-2 weeks | After EMC |
| **Battery UN 38.3** | All 8 tests (3 packs) | 4-6 weeks | DV-1 and DV-2 (different lab) |
| **PV-1 Environmental** | Key tests (vibration, shock, humidity, IP67) | 4-5 weeks | After DV complete |
| **PV-2 Field Trial** | 10-lane installation, 1000-shot test | 4 weeks | After PV-1 |
| **TOTAL (SERIAL)** | | **23-30 weeks** | |
| **TOTAL (PARALLEL)** | | **~16-20 weeks** | With 2 labs running DV simultaneously |

### 6.4 Test Equipment Required

| Equipment | Purpose | Available at Lab? | Notes |
|-----------|---------|-------------------|-------|
| Environmental chamber (temperature + humidity) | 501.7, 502.7, 507.6 | Yes (standard lab) | Range -70C to +180C, humidity control |
| Salt fog chamber | 509.7 | Yes (standard lab) | ASTM B117 capable |
| Sand/dust chamber | 510.7 | Yes (specialized lab) | Wind tunnel with particle injection |
| Electrodynamic shaker (vibration) | 514.8 | Yes (standard lab) | 5-2000 Hz, >10 kN force rating |
| Shock machine / drop table | 516.8 | Yes (standard lab) | 40g capability with half-sine pulse |
| EMC anechoic chamber (10m) | RE102, RS103 | Yes (EMC lab) | 10 kHz - 18 GHz capability |
| LISN (Line Impedance Stabilization Network) | CE102, CS101 | Yes (EMC lab) | MIL-STD-461G compliant |
| Water immersion tank | IP67 (IPX7) | Yes (standard lab) | 1m depth minimum |
| Dust chamber | IP67 (IP6X) | Yes (standard lab) | Talcum powder injection at underpressure |
| UN 38.3 battery test equipment | All 8 tests | Specialized battery lab | Altitude simulation, thermal chamber, crush test rig |
| Acoustic test fixture | TDOA accuracy verification | Custom build | Simulates shockwave at known positions |

### 6.5 External Test Lab Options

| Lab | Location | Capabilities | Estimated Cost | Lead Time |
|-----|----------|-------------|----------------|-----------|
| **QUATEST 3** | Ho Chi Minh City, Vietnam | Environmental (limited 810H), IP testing, basic EMC | $8,000-15,000 (partial) | 8-12 weeks |
| **VILAS-accredited labs** | Hanoi, Vietnam | Environmental testing, safety | $5,000-10,000 (partial) | 6-10 weeks |
| **TUV SUD** | Singapore | Full MIL-STD-810H, 461G, IEC 62368-1, UN 38.3 | $40,000-60,000 (complete) | 12-16 weeks |
| **SGS** | Singapore / China | Full environmental + EMC + safety | $35,000-55,000 (complete) | 12-16 weeks |
| **China National Accreditation (CNAS) labs** | Shenzhen / Guangzhou, China | Full 810H, 461G, UN 38.3 | $25,000-40,000 (complete) | 10-14 weeks |
| **Bureau Veritas** | Ho Chi Minh City / Singapore | Environmental + safety testing | $30,000-50,000 (complete) | 12-16 weeks |

**Recommended Approach:**

| Phase | Lab | Tests | Cost |
|-------|-----|-------|------|
| **DV-1 Environmental** | CNAS lab (Shenzhen) | MIL-STD-810H full sequence | $15,000-20,000 |
| **DV-2 EMC + Safety** | TUV SUD (Singapore) or CNAS lab | MIL-STD-461G + IEC 62368-1 + IP67 | $12,000-18,000 |
| **Battery UN 38.3** | SGS (Shenzhen) | Full UN 38.3 pack testing | $8,000-15,000 |
| **PV Environmental** | QUATEST 3 (HCMC) | Abbreviated repeat (vibration, humidity, IP67) | $5,000-8,000 |
| **TOTAL** | | | **$40,000-61,000** |

### 6.6 Test Budget Summary

| Item | Cost Estimate |
|------|---------------|
| Test articles (4x BSU @ $328 + 3x battery packs @ $35) | $1,417 |
| Test fixtures and custom equipment | $3,000-5,000 |
| External lab fees (all testing) | $40,000-61,000 |
| Travel and logistics (lab visits, shipping) | $5,000-8,000 |
| Test reports and documentation | $2,000-3,000 |
| **TOTAL TEST BUDGET** | **$51,417-78,417** |
| **Budget recommended (with 20% contingency)** | **$65,000-95,000** |

---

## 7. COMPLIANCE SUMMARY TABLE

### 7.1 Standards vs. Requirements vs. Compliance Status

| Standard | Clause/Method | BSU-V1 Requirement | Design Feature | Status | Verification |
|----------|--------------|-------------------|----------------|--------|-------------|
| **MIL-STD-810H** | 501.7 High Temp | OPR-01: -10C to +60C | Industrial ICs, FR-4 Tg170, Al heat sink | Designed | Test |
| | 502.7 Low Temp | OPR-01: -10C to +60C | Industrial ICs, Li-ion rated -20C | Designed | Test |
| | 507.6 Humidity | OPR-03: 95% RH, 40C | IP67, conformal coat IPC-CC-830C | Designed | Test |
| | 509.7 Salt Fog | OPR-06: 48h salt fog | SS316, hard anodize, EPDM, nylon washers | Designed | Test |
| | 510.7 Sand/Dust | OPR-05: Procedure I dust | IP67 (IP6X), no ventilation holes | Designed | Test |
| | 514.8 Vibration | FRC-04: Cat 4 wheeled | Rubber isolators, 4mm walls, no spans >80mm | Designed | Test |
| | 516.8 Shock | FRC-03: 40g, 11ms | Rubber standoffs, battery strap, 8x M4 lid | Designed | Test |
| | 521.4 Icing | OPR-01 (extended) | No moving parts, IP67, -10C rated | Designed | Analysis |
| **MIL-STD-461G** | RE102 | SAF-05 | Al Faraday cage, filtered I/O, spread-spectrum | Designed | Test |
| | CE102 | SAF-05 | Pi-filter, battery mode | Designed | Test |
| | RS103 | SAF-05 | Al enclosure >60 dB SE | Designed | Test |
| | CS101 | SAF-05 | DC-DC rejection, pi-filter | Designed | Test |
| **MIL-STD-882E** | HAZ-001 Battery | SAF-04 | BMS, fuses, thermal barrier, monitoring | Designed | Analysis + Test |
| | HAZ-002 Shock | SAF-01, SAF-03 | SELV (<50V), IP67, Class II adapter | Designed | Analysis |
| | HAZ-003 Projectile | SAF-02 | Low profile, geometry, optional ballistic plate | Designed | Analysis |
| | HAZ-004 RF | SAF-05 | 461G compliant, shielded cables | Designed | Test |
| | HAZ-005 Fire | SAF-01, SAF-04 | Fuses, V-0 materials, Al containment | Designed | Analysis + Test |
| **IEC 62368-1** | Clause 5-14 | SAF-01, SAF-03 | ES1, SELV, Class III, IP67 enclosure | Designed | Test |
| **IEC 60529** | IP6X | OPR-05, OPR-07 | Sealed Al enclosure, no ventilation | Designed | Test |
| | IPX7 | OPR-04, OPR-07 | EPDM O-ring, 8x M4 bolts, IP67 connectors | Designed | Test |
| **IPC-CC-830C** | Class 3 | MAT-03 | HumiSeal 1B31 acrylic conformal coat | Designed | Process Qual |
| **IPC-A-610** | Class 2 | PRD-03, PRD-05 | Vietnamese EMS capability, AOI inspection | Designed | Inspection |
| **MIL-A-8625F** | Type III | MAT-01 | Hard anodize 25um on Al 6061-T6 | Designed | Process Qual |
| **UN 38.3** | T.1-T.8 | ENG-04, TRN-04 | Samsung 35E cells (cell-level certified), pack-level BMS | Cell: Certified; Pack: **TEST REQUIRED** | Test |
| **FASIT** | v5.0 protocol | SIG-06 | TCP/IP Ethernet, FASIT message format | Designed | Demonstration |
| **TCVN 7447** | Electrical installation | SAF-01 | Low-voltage DC (<50V), double insulation | Designed | Inspection |
| **TCVN 6450** | EMC | SAF-05 | MIL-STD-461G exceeds TCVN 6450 Class A | Designed | Test (via 461G) |

### 7.2 Compliance Status Summary

| Status | Count | Percentage | Standards |
|--------|-------|------------|-----------|
| **Designed** (compliance designed-in, awaiting verification) | 28 of 30 line items | 93% | All standards |
| **Certified** (existing certification) | 1 of 30 | 3% | UN 38.3 cell-level |
| **Test Required** (new testing needed) | 1 of 30 | 3% | UN 38.3 pack-level |

### 7.3 Compliance Risk Assessment

| Risk | Standard | Issue | Mitigation |
|------|----------|-------|------------|
| HIGH | MIL-STD-461G RE102 | FPGA 480 MHz MCU clock harmonics could exceed limit at specific frequencies | Spread-spectrum clocking; conductive gasket at lid; pre-compliance scan before formal test |
| MEDIUM | MIL-STD-810H 507.6 | Humid cycling may reveal seal degradation after extended use | Test with post-cycling IP67 re-test; add desiccant pack as margin |
| MEDIUM | UN 38.3 T.4 (Shock) | Pack-level shock (150g) is more severe than operational shock (40g); BMS wire bonds vulnerable | Strain-relieve all BMS connections; use welded tabs not soldered |
| LOW | MIL-STD-810H 509.7 | Galvanic corrosion at Al/SS interface despite nylon washers | Nylon washers + sealant (Loctite 5900) at all dissimilar metal joints |
| LOW | IPC-A-610 Class 2 | Vietnamese EMS may have limited experience with Class 2 workmanship | Provide IPC-A-610 training to EMS; establish incoming inspection criteria |

---

## 8. VIETNAMESE NATIONAL STANDARDS COMPLIANCE

### 8.1 TCVN 7447 - Electrical Installation

| Clause | Requirement | BSU-V1 Compliance |
|--------|------------|-------------------|
| TCVN 7447-1 | Basic principles, safety | All circuits SELV (<50V DC); no mains connection at BSU |
| TCVN 7447-4-41 | Protection against electric shock | Double/reinforced insulation via IP67 enclosure + external Class II adapter |
| TCVN 7447-4-42 | Protection against thermal effects | Non-flammable enclosure (aluminum); V-0 rated PCB |
| TCVN 7447-4-43 | Protection against overcurrent | Pack fuse (5A), polyfuse on outputs, BMS over-current protection |
| TCVN 7447-5-52 | Wiring systems | Internal harness: PTFE/ETFE insulated, strain-relieved, fire-retardant |

### 8.2 TCVN 6450 - EMC

| Clause | Requirement | BSU-V1 Compliance |
|--------|------------|-------------------|
| TCVN 6450 Class A | Radiated emission limits (industrial) | MIL-STD-461G RE102 limits are more stringent; passing 461G exceeds TCVN 6450 |
| TCVN 6450 Class A | Conducted emission limits (industrial) | MIL-STD-461G CE102 limits are more stringent; passing 461G exceeds TCVN 6450 |
| TCVN 6450 | Immunity requirements | RS103 at 10 V/m exceeds TCVN immunity requirements (typically 3 V/m) |

**Assessment:** MIL-STD-461G compliance automatically satisfies TCVN 6450 Class A. A single test program covers both standards.

---

## 9. FASIT PROTOCOL COMPLIANCE

### 9.1 FASIT Overview

| Parameter | Detail |
|-----------|--------|
| **Full Name** | Future Army System of Integrated Targets |
| **Version** | FASIT v5.0 |
| **Origin** | US Army PEO STRI |
| **Purpose** | Standard communication protocol for range target systems |
| **Transport** | TCP/IP over Ethernet |
| **Port** | Configurable (default 4000) |

### 9.2 FASIT Message Types Relevant to BSU-V1

| Message | Direction | Content | BSU-V1 Implementation |
|---------|-----------|---------|----------------------|
| STATUS | BSU -> Control | Device status, health, configuration | BIT results mapped to FASIT status fields |
| HIT | BSU -> Control | X,Y coordinates, timestamp, shot ID | TDOA result converted to FASIT hit message |
| CONFIGURE | Control -> BSU | Lane ID, mode, detection zone | Parsed by MCU; stored in flash |
| RESET | Control -> BSU | Soft reset command | MCU performs warm restart |
| HEARTBEAT | Bidirectional | Keep-alive, connection monitoring | 1 Hz interval configurable |

### 9.3 FASIT Compliance Status

| Item | Status | Notes |
|------|--------|-------|
| FASIT specification access | **TBD-04 OPEN** | US Army controlled document; access requested |
| Protocol implementation | Designed (based on public FASIT documentation) | Will finalize when specification received |
| Interoperability test | Not yet possible | Requires access to FASIT-compliant equipment |
| Fallback | Proprietary VN-LOMAH protocol as primary | FASIT as secondary/export protocol layer |

---

## 10. META-LEARNING SKILL: REGULATORY MAPPING

### Skill Applied: Standards-to-Design Traceability

| Aspect | Insight |
|--------|---------|
| **Technique** | Map each standard clause to specific design features (not just "compliant by design") |
| **Key Learning** | Standards compliance is NOT an afterthought; every design decision in Phase 3 must reference the standard it satisfies |
| **Vietnamese Context** | TCVN standards generally harmonized with IEC; MIL-STD compliance exceeds TCVN requirements in all cases |
| **Cost Insight** | Test budget ($65-95K) is significant for a $377/unit product; amortized over 500 units = $130-190/unit test cost; must be factored into program NRE |
| **Risk Insight** | EMC (461G RE102) is the highest compliance risk due to high-speed clocks; pre-compliance testing strongly recommended before formal test |
| **Process Insight** | Test article quantity (4 units + 3 battery packs) must be planned in Phase 4 BOM alongside prototype articles |

### Application in Future Projects

1. **Start standards mapping in Phase 1** (requirements) -- this was done correctly for VN-TRN-001
2. **Allocate test budget early** -- $65-95K is 3-5% of first-year revenue (500 units x $377 = $188K); significant but necessary
3. **Use Vietnamese labs where possible** (QUATEST 3) for cost reduction; use Singapore/China for MIL-STD tests beyond Vietnamese lab capability
4. **Pre-compliance EMC testing** can be done with $2,000 near-field probe set before committing $15,000 to formal test
5. **Battery UN 38.3 certification** should be initiated in parallel with DV-1 environmental testing to avoid schedule impact

---

**Next Step:** [[OCP_O_optimization]] -- Optimize design for weight, cost, thermal, and manufacturability

---

*DECS-S Complete | 12 standards mapped | 30 compliance line items | 5 hazards analyzed | Test budget $65-95K | ~16-20 weeks test duration*
