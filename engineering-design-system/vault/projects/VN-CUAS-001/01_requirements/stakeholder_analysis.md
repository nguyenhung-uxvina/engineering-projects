---
project: VN-CUAS-001
phase: 1
type: stakeholder_analysis
version: 1.0
created: 2026-02-11
status: draft
---

# Stakeholder Analysis: VN-CUAS-001 -- Counter-UAS Passive Acoustic Detection System

---

## 1. Stakeholder Map Overview

```
                        HIGH INFLUENCE
                             |
        +--------------------+--------------------+
        |                    |                    |
        |   S7: Regulator    |   S1: Customer     |
        |   (TCVN/MoD Test)  |   (VPA Procure)    |
        |                    |                    |
        |   S11: Intl Partner|   S2: Primary User |
        |   (MIL-STD Labs)   |   (AD/FP Operator) |
        |                    |                    |
        |                    |   S2b: Tac. Cmdr   |
 LOW ---+--------------------+--------------------+--- HIGH
INTEREST|                    |                    | INTEREST
        |   S10: Competitors |   S3: Sys Deployer |
        |   (Squarehead,     |                    |
        |    DroneShield)    |   S4: Maint Tech   |
        |                    |                    |
        |                    |   S5: Intel Analyst |
        |                    |                    |
        |                    |   S6: Fusion Op    |
        |                    |                    |
        |                    |   S8: Manufacturer |
        |                    |                    |
        |                    |   S9: Dev Team     |
        +--------------------+--------------------+
                             |
                        LOW INFLUENCE
```

**Quadrant Summary:**

| Quadrant | Strategy | Stakeholders |
|----------|----------|-------------|
| **Key Players** (High influence + High interest) | Engage closely, co-develop requirements | S1, S2, S2b |
| **Keep Satisfied** (High influence + Low interest) | Formal compliance, demos, reports | S7, S11 |
| **Keep Informed** (Low influence + High interest) | Design reviews, training, DFM sessions | S3, S4, S5, S6, S8, S9 |
| **Monitor** (Low influence + Low interest) | Market intelligence, competitive benchmarking | S10 |

---

## 2. Detailed Stakeholder Profiles

### S1: Customer (Procurement Authority)

| Field | Detail |
|-------|--------|
| **Who** | VPA Equipment Department (Cuc Quan gioi), Border Defense Command (Bo Tu lenh Bien phong), Air Defense Command (Bo Tu lenh Phong khong - Khong quan), Military Region Commands |
| **Role** | Budget holder, procurement decision maker, defines procurement specifications and evaluation criteria |
| **Interest** | HIGH -- Urgent C-UAS gap exposed by global drone proliferation (Ukraine 2022-2026); no affordable passive detection system in Vietnamese inventory |
| **Influence** | HIGH -- Approves procurement budget, sets evaluation criteria, authorizes pilot deployments, controls multi-year acquisition plan |
| **Primary Needs** | Cost competitiveness vs import ($2-5K vs $15-200K); local content compliance (>=60%); proven detection capability; vendor independence; lifecycle affordability; TCVN compliance |
| **Success Criteria** | Unit cost <=$5K/node; >=60% local content; demonstrated Pd >=80% for Group 1 at 300m; Vietnamese documentation; 10-year lifecycle support plan; no ITAR-controlled components |
| **Pain Points** | Import C-UAS systems cost $50K-1M+/site (DroneShield, Dedrone); no local vendor for acoustic detection; foreign system dependency creates supply chain risk under sanctions; current "drone detection" = visual observation; slow procurement cycle for imported defense equipment |
| **Communication** | Formal procurement specifications, demonstration events at military ranges, pilot deployment results, cost-benefit analyses, quarterly program reviews |
| **Risk if Ignored** | Project unfunded; requirements misaligned with procurement criteria; budget diverted to imported multi-sensor systems |
| **Key Requirements Driven** | CST-001 (unit cost <=$5K/node), CST-002 (BOM <=$1.5K), PRD-001 (local content >=60%), ERG-001 (Vietnamese language UI), STD-001 (MIL-STD-810H), STD-002 (TCVN compliance), SCH-001 (delivery schedule) |

**ODI Connection:** Customer represents the procurement gateway for all 4 segments identified in [[odi_analysis.md]] -- Segment A (Forward Force Protection, 40%), Segment B (Fixed-Site Security, 30%), Segment C (Intelligence, 20%), Segment D (Tropical Environment, 10%).

---

### S2: Primary User (Air Defense / Force Protection Operator)

| Field | Detail |
|-------|--------|
| **Who** | Trac thu phong khong / Nhan vien bao ve luc luong -- Air defense trackers and force protection operators across VPA, Border Defense, and Coast Guard |
| **Role** | **Primary ODI job executor**: physically monitors the system, interprets alerts, initiates response actions on 8-hour shifts. Persona: "Trung si Nguyen" from [[odi_analysis.md]] |
| **Interest** | HIGH -- Direct impact on their survival and mission success; currently has zero passive acoustic capability |
| **Influence** | HIGH -- Field feedback determines product acceptance; poor usability = system abandoned; influences repeat orders through operational reports |
| **Technical Level** | Medium -- Military technical school graduate, 6-12 months MOS training; comfortable with ruggedized electronics; NOT software engineers |
| **Primary Needs** | Detect RF-silent drones (O-35, Opp=18.5); detect Group 1 quadcopters (O-22, Opp=18.0); low missed detection rate (O-29, Opp=17.5); low false alarm rate (O-28, Opp=15.5); alert latency <=3s (O-24, Opp=15.0); classification accuracy (O-27, Opp=15.0); multi-drone detection (O-33, Opp=15.0) |
| **Success Criteria** | Pd >=80% for Group 1 at 300m; Pfa <=1/hour; alert latency <=3s; classification accuracy >=75% across 4+ drone types; <=8h operator training; Vietnamese interface; intuitive alert display readable in sunlight and darkness |
| **Pain Points** | Current detection = visual observation and listening (zero capability at night or in fog); no prior C-UAS training or equipment; tropical heat 30-40C, monsoon rain, high humidity; 8-hour shifts create fatigue requiring low cognitive workload interface |
| **Communication** | Field demonstrations, hands-on training, Vietnamese-language operator manual, pictorial quick-reference card, annual refresher training |
| **Risk if Ignored** | Poor adoption; system abandoned; "alarm fatigue" from false positives; negative field reports kill procurement expansion |
| **Key Requirements Driven** | SIG-001 (Pd >=80% Group 1 at 300m), SIG-002 (Pfa <=1/hour), SIG-003 (alert latency <=3s), SIG-004 (classification accuracy >=75%), SIG-005 (multi-target >=3 simultaneous), ERG-002 (operator training <=8h), ERG-003 (sunlight-readable display), OPR-001 (continuous 24/7 operation) |

**Persona (from [[odi_analysis.md]]):**
> Trung si Nguyen, 24, operates air defense equipment at a forward operating base near the northern border. He monitors systems on 8-hour shifts, often at night. He has basic electronics training but is not an engineer. He operates in tropical heat (30-40C), monsoon rain, and high humidity. His unit budget is limited; equipment must be simple, rugged, and require minimal maintenance. He has never used a C-UAS system before -- his current "drone detection" method is visual observation and listening.

**ODI Segments Represented:**
- Segment A: Forward Force Protection (40%) -- PRIMARY target, northern border, coastal defense
- Segment D: Tropical Environment (10%) -- monsoon, jungle, high humidity operations

---

### S2b: Secondary User (Tactical Commander)

| Field | Detail |
|-------|--------|
| **Who** | Company/battalion commanders, air defense platoon leaders, force protection officers -- Dai doi truong, Tieu doan truong, Sy quan phong khong |
| **Role** | **ODI Consumption Chain CC-1**: receives detection alerts, decides response (engage/evade/report), accountable for engagement decisions under ROE |
| **Interest** | HIGH -- Acoustic detection directly feeds engagement decisions; wrong classification = fratricidal engagement or missed threat |
| **Influence** | HIGH -- Decides to trust (or not trust) the system; recommends procurement to higher command; sets operational procedures; can override system |
| **Primary Needs** | Confidence in classification before ordering response (CC-02, Opp=16.0); minimize friendly drone engagement risk (CC-03, Opp=15.0); rapid threat situation understanding (CC-01, Opp=14.5); clear track history for decision-making (CC-04, Opp=10.5) |
| **Success Criteria** | Classification confidence percentage displayed with each alert; IFF/correlation with friendly drone schedules; <=5 seconds from alert to situational understanding; audit trail for engagement decisions |
| **Pain Points** | No passive detection layer in current defense architecture; forced to make engagement decisions based on visual confirmation only (too late for fast FPV drones at 100+ km/h); ROE compliance risk if classification is wrong; no recorded evidence for after-action review |
| **Communication** | Command-level dashboard (summary view, not raw sensor data), Vietnamese-language alert protocols, tactical SOP integration, demonstration events, command briefings |
| **Risk if Ignored** | Commander distrust leads to system override and disuse; engagement decision delays negate detection advantage; ROE violations from insufficient classification confidence; system becomes shelf-ware |
| **Key Requirements Driven** | SIG-006 (classification confidence score with every alert), SIG-007 (IFF correlation capability), ERG-004 (alert-to-understanding <=5s), OPR-002 (engagement audit trail), OPR-003 (ROE-compatible alert levels) |

---

### S3: System Deployer

| Field | Detail |
|-------|--------|
| **Who** | Signal/engineering NCOs assigned to deploy and configure the system -- Tieu doi truong thong tin / Nhan vien ky thuat |
| **Role** | **ODI Consumption Chain CC-2**: carries equipment to deployment positions, installs sensor nodes, establishes mesh network, verifies operational coverage before handing off to operator |
| **Interest** | HIGH -- System weight, setup complexity, and deployment time directly impact their physical workload and tactical timeline |
| **Influence** | LOW-MEDIUM -- Does not make procurement decisions, but deployment difficulty creates field resistance and negative feedback |
| **Technical Level** | Medium -- signal/comms training; understands antennas, cabling, and basic RF; NOT software specialists |
| **Primary Needs** | Minimize weight (O-08, Opp=12.5); minimize deployment time (O-06, Opp=11.5); minimize tools for installation (CC-05, Opp=8.5); prevent incorrect orientation (CC-06, Opp=11.0); verify correct installation (CC-07, Opp=9.5); minimize training for new installers (CC-08, Opp=11.0) |
| **Success Criteria** | Full node <=5 kg (one-person carry); deploy single node in <=15 min; 3-node network operational in <=30 min; no specialized tools; visual/audible setup confirmation; deployer training <=4 hours |
| **Pain Points** | Every kilogram matters in dismounted operations; complex setup causes errors under time pressure; need to relocate quickly for tactical mobility; limited understanding of acoustic theory means "black box" feel if setup is not intuitive |
| **Communication** | Pictorial setup guide (laminated, Vietnamese), quick-start card, audible/visual deployment confirmation feedback from the system, setup training module |
| **Risk if Ignored** | Nodes positioned incorrectly degrading coverage; deployment takes too long for rapid operations; system too heavy and left behind; deployer blames system for poor performance caused by setup errors |
| **Key Requirements Driven** | GEO-001 (sensor head <=2 kg), GEO-002 (full node <=5 kg), OPR-004 (single-node deploy <=15 min), OPR-005 (network deploy <=30 min), ERG-005 (tool-less installation), ERG-006 (self-leveling or orientation indicator), ASM-001 (M12/bayonet connectors, IP67) |

---

### S4: Maintenance Technician

| Field | Detail |
|-------|--------|
| **Who** | Unit-level and depot-level maintenance technicians -- Nhan vien ky thuat bao tri -- at battalion/regiment level |
| **Role** | **ODI Consumption Chain CC-3**: keeps system operational, diagnoses faults, replaces modules, performs field repairs between deployments and on failure |
| **Interest** | HIGH -- System reliability and maintainability directly determine their workload and unit readiness reporting |
| **Influence** | LOW-MEDIUM -- Maintenance feedback influences design updates; high failure rate generates negative reports to command |
| **Technical Level** | Medium -- electronics repair skills (soldering, multimeter, oscilloscope at depot level); NOT software engineers or ML specialists |
| **Available Tools** | Basic hand tools, multimeter, soldering station (depot level), limited spare parts inventory |
| **Primary Needs** | Fast fault identification (CC-09, Opp=11.0); field repair capability (CC-11, Opp=13.0); fast node replacement (CC-12, Opp=10.0); minimum spare parts types (CC-10, Opp=9.5) |
| **Success Criteria** | MTTR <=30 min for module replacement; self-diagnostics identify >=90% of faults to LRU level; field repair without factory support; <=10 unique spare part types; 12-month calibration interval; Vietnamese maintenance manual with fault-code reference |
| **Pain Points** | Imported defense systems require foreign technicians for any repair; spare parts take months via import; no local knowledge of proprietary acoustic systems; tropical humidity accelerates corrosion and connector degradation; conformal coating complicates rework |
| **Communication** | Vietnamese-language maintenance manual, fault code reference card (laminated), 16-hour maintenance training course, remote diagnostic capability via mesh network |
| **Risk if Ignored** | System downtime increases; units stop using system; negative readiness reports; procurement not expanded |
| **Key Requirements Driven** | MNT-001 (MTTR <=30 min), MNT-002 (MTBF >=5,000 hours), MNT-003 (self-diagnostics >=90% fault isolation), MNT-004 (<=10 unique spare part types), MNT-005 (12-month calibration interval), MNT-006 (hot-swap node replacement), ASM-002 (modular LRU architecture), MAT-001 (conformal coating for tropical protection) |

---

### S5: Intelligence Analyst

| Field | Detail |
|-------|--------|
| **Who** | Military intelligence officers and NCOs at brigade/division level -- Sy quan trinh sat / Nhan vien tinh bao |
| **Role** | **ODI Consumption Chain CC-4**: processes accumulated detection data, identifies patterns in adversary drone activity, builds threat picture, updates threat library with newly identified drone signatures |
| **Interest** | HIGH -- Acoustic detection data is a new intelligence source; enables pattern-of-life analysis for adversary drone operations |
| **Influence** | LOW-MEDIUM -- Does not make procurement decisions, but intelligence value justifies system expansion and drives ML training data requirements |
| **Technical Level** | High -- Analytical skills, database queries, GIS tools; may have basic programming ability |
| **Primary Needs** | Accessible historical data (CC-13, Opp=13.0); correlate acoustic with other intel (CC-14, Opp=12.0); identify new drone types from recordings (CC-15, Opp=14.5); update threat database quickly (CC-16, Opp=13.0); retain acoustic data for ML training (O-52, Opp=15.0) |
| **Success Criteria** | Queryable database of all detection events (timestamp, bearing, range, classification, confidence, raw audio); export formats: CSV, JSON, KML; acoustic signature library with spectrogram visualization; correlation API for existing intel systems; >=90 days online storage |
| **Pain Points** | Currently zero acoustic intelligence on adversary drone activity; no systematic way to identify new drone types entering theater; intelligence reports are purely visual observation-based; no labeled acoustic dataset for Vietnamese environment |
| **Communication** | Analyst workstation interface (web-based), API documentation, data export format specifications, Vietnamese + English interface option |
| **Risk if Ignored** | System becomes "detect and forget" -- loses long-term intelligence value; ML training data not captured; new drone types not identified proactively |
| **Key Requirements Driven** | SIG-008 (searchable detection event database >=90 days), SIG-009 (raw acoustic data retention >=30 days for ML), SIG-010 (data export CSV/JSON/KML), SIG-011 (REST API for external correlation), SIG-012 (spectrogram capture for new-signature identification), SIG-013 (signature-to-library pipeline) |

---

### S6: Multi-Sensor Fusion Operator

| Field | Detail |
|-------|--------|
| **Who** | C2 center operators at brigade/division air defense -- Nhan vien dieu hanh tac chien phong khong |
| **Role** | **ODI Consumption Chain CC-5**: integrates acoustic tracks into Common Operational Picture (COP) alongside radar, RF, EO/IR, and visual data for layered defense |
| **Interest** | HIGH -- Acoustic fills the autonomous/RF-silent drone gap in multi-sensor COP; cues expensive active sensors to conserve their resources |
| **Influence** | LOW-MEDIUM -- Does not drive procurement, but fusion compatibility determines tactical utility and justifies acoustic as a layer |
| **Technical Level** | High -- C2 system operators; familiar with radar track formats, COP management, BMS interfaces |
| **Primary Needs** | Low acoustic track latency in COP (CC-17, Opp=12.5); track format compatibility with radar/EO/RF (CC-18, Opp=14.0); easy track de-confliction (CC-19, Opp=12.0); acoustic as cue for other sensors (CC-20, Opp=14.0); C2/BMS integration ease (O-11, Opp=13.0) |
| **Success Criteria** | Acoustic tracks appear in COP within <=2s of detection; SAPIENT-compliant track format; automatic correlation with radar/RF tracks within 5m/5s tolerance; acoustic-cued camera/radar slew capability |
| **Pain Points** | Current COP has no acoustic layer; acoustic tracks are a new data type requiring integration; lower precision than radar creates display challenges; no SAPIENT infrastructure in Vietnamese military yet |
| **Communication** | SAPIENT interface specification, TAK plugin documentation, REST API reference, integration test procedures, interoperability demonstrations |
| **Risk if Ignored** | Acoustic system operates as stand-alone silo -- loses 80% of value; no sensor cueing; operator must monitor separate display (unacceptable cognitive workload) |
| **Key Requirements Driven** | SIG-014 (SAPIENT-compliant track output, BSI Flex 335), SIG-015 (TAK plugin for mobile COP), SIG-016 (sensor cueing output for camera/radar slew), SIG-017 (track-to-COP latency <=2s), SIG-018 (track de-confliction metadata), SIG-019 (REST API for custom C2) |

---

### S7: Regulator / Standards Body

| Field | Detail |
|-------|--------|
| **Who** | VPA Quality Assurance directorate; Military Testing and Evaluation Center; Vietnamese Directorate for Standards, Metrology and Quality (STAMEQ); TCVN standards committees |
| **Role** | Approves equipment for military use; enforces safety, quality, and environmental standards; certifies compliance; defines test protocols |
| **Interest** | MEDIUM -- New equipment category (passive acoustic C-UAS); no existing Vietnamese standard to apply directly |
| **Influence** | HIGH -- Can block procurement indefinitely; certification is mandatory before deployment; sets acceptance test protocols |
| **Primary Needs** | Compliance with applicable TCVN standards; MIL-STD-810H environmental qualification evidence; MIL-STD-461G EMC compliance; MIL-STD-882E safety analysis; electrical safety certification; ML validation methodology |
| **Success Criteria** | Complete compliance dossier with accredited test lab results; FMECA + fault tree analysis; demonstrated environmental qualification across all MIL-STD-810H methods; no safety incidents during pilot deployment |
| **Pain Points** | No existing TCVN standard for passive acoustic C-UAS systems; must adapt from international military standards; limited experience evaluating ML-based classification systems; unclear how to certify Pd/Pfa claims from ML algorithms |
| **Communication** | Formal compliance documentation, accredited test lab reports, safety analysis dossier, certification review meetings |
| **Risk if Ignored** | Certification blocked; deployment delayed indefinitely; product cannot enter Vietnamese military inventory; liability exposure if fielded without proper qualification |
| **Key Requirements Driven** | STD-001 (MIL-STD-810H Methods 501-516 environmental), STD-002 (MIL-STD-461G RE102/RS103/CE102/CS101 EMC), STD-003 (MIL-STD-882E safety analysis), STD-004 (TCVN electrical safety), SAF-001 (IP67 environmental protection), SAF-002 (ML classification validation methodology) |

---

### S8: Manufacturer (Vietnamese Production Partners)

| Field | Detail |
|-------|--------|
| **Who** | Vietnamese manufacturing partners: PCB fabricators, CNC machining shops (aluminum enclosures), electronics assembly houses, cable/harness manufacturers, conformal coating specialists |
| **Role** | Produces the hardware; determines local content percentage and unit cost; scales production from prototype to volume |
| **Interest** | HIGH -- Revenue opportunity; defense manufacturing capability building; government incentives for local defense industry content |
| **Influence** | MEDIUM -- Manufacturing capability constrains design choices; yield rates affect cost; quality affects field reliability |
| **Capabilities** | PCB: 4-6 layer FR4, solder paste + reflow; CNC: 3-axis aluminum (5-axis limited); Assembly: IPC-A-610 Class 2 achievable with training; Conformal coating: available but limited military-grade experience |
| **Primary Needs** | Clear manufacturing drawings with realistic tolerances; locally available materials; reasonable batch sizes (>=100 units/lot); DFM-friendly design; standard component packages (no BGA if possible for rework); training on military-grade assembly |
| **Success Criteria** | >=60% local content by value; >=95% first-pass yield; consistent quality at 500+/year volume; profitable margins on defense contract |
| **Pain Points** | Limited experience with MEMS microphone array assembly (128-256 mics per board); conformal coating for IP67 + tropical humidity is challenging; import lead times for MEMS and ICs (8-16 weeks from China/US); limited MIL-grade component experience |
| **Communication** | Manufacturing specification packages, DFM review sessions, supplier qualification audits, IPC-A-610 training programs, pilot production reviews |
| **Risk if Ignored** | Poor yield rates and cost overruns; inconsistent quality and field failures; local content target not met; procurement non-compliance |
| **Key Requirements Driven** | PRD-001 (local content >=60%), PRD-002 (DFM: >=0.3mm trace/space, standard SMD, no BGA on critical boards), PRD-003 (IPC-A-610 Class 2 minimum), PRD-004 (100% end-of-line functional test + AOI), MAT-002 (6061-T6 aluminum locally available), MAT-003 (FR4 PCB locally fabricated) |

**Key Suppliers (Vietnamese Defense Context):**

| Material | Potential Suppliers | Local/Import |
|----------|-------------------|-------------|
| Aluminum enclosure (6061-T6) | Local CNC shops (Hoa Phat stock) | Local |
| PCB fabrication (4-6 layer) | Vietnamese PCB fabs | Local |
| PCB assembly (SMT + THT) | Vietnamese EMS houses | Local |
| Conformal coating (acrylic) | Local coating specialists | Local |
| Cable assemblies / harnesses | Local harness manufacturers | Local |
| Gaskets / seals (EPDM) | Local rubber manufacturers | Local |
| Fasteners (stainless) | Local or import | Local |
| MEMS microphones (128-256x) | Import: TDK InvenSense, Knowles | Import (China/US) |
| FPGA / SoC (Xilinx/AMD) | Import: AMD/Xilinx distribution | Import (China) |
| ARM MCU (STM32H7 class) | Import: STMicroelectronics | Import (China) |
| IP67 connectors (M12) | Import: Amphenol, TE Connectivity | Import (China) |
| Radio module (mesh network) | Import: Digi, Rajant, or similar | Import |
| GPS/GNSS module | Import: u-blox or similar | Import |

---

### S9: Development Team (DSP/ML/Firmware/Hardware Engineering)

| Field | Detail |
|-------|--------|
| **Who** | Core engineering team: DSP/embedded firmware engineers, ML engineers (acoustic classification), hardware engineers (PCB, FPGA, enclosure), software developers (C2 interface, TAK plugin, web dashboard) |
| **Role** | Designs, develops, tests, and iterates the product through all phases; bridges R&D to production; establishes engineering methods and test infrastructure |
| **Interest** | HIGH -- Core project team; career development on cutting-edge defense ML/DSP product |
| **Influence** | MEDIUM -- Technical decisions within design space; identifies what is feasible vs aspirational; flags risk to schedule and cost |
| **Primary Needs** | Clear quantified requirements with testable acceptance criteria; access to drone acoustic recordings for ML training; military test range access for field validation; development hardware (FPGA dev kits, microphone arrays, GPU for ML training); published acoustic propagation models for Vietnamese terrain/climate |
| **Success Criteria** | Prototype meets all MUST requirements; Pd/Pfa validated on live range with real drone targets; ML model achieves >=75% classification accuracy on 4+ drone types; firmware passes 72h continuous stress test; SAPIENT interface tested against reference implementation |
| **Pain Points** | No prior C-UAS acoustic development experience (learning curve); limited Vietnamese military range access for field testing; no labeled acoustic drone dataset for Vietnamese environment; ML training requires GPU infrastructure; 128-256 channel MEMS array DSP is computationally intensive |
| **Communication** | Technical design reviews, sprint demos, weekly stand-ups, design review gates, internal documentation wiki |
| **Risk if Ignored** | Requirements misinterpretation and rework; overly ambitious requirements causing schedule slip; insufficient test access yielding unvalidated performance claims |
| **Key Requirements Driven** | SIG-020 (beamforming architecture: SRP-PHAT + MUSIC/ESPRIT), SIG-021 (dual classification: eigenvector + CNN), SIG-022 (ML pipeline: audio to mel-spectrogram to CNN to classification), SIG-023 (OTA firmware + ML model update), ENE-001 (power budget <=10W sensor, <=15W full node), GEO-003 (128-256 MEMS array geometry) |

**Capability Gaps Identified (from 8 RE analyses in Phase 0):**

| Gap | Severity | Mitigation |
|-----|----------|-----------|
| MEMS array DSP (beamforming, DoA) | High | Study Squarehead/BeephoniX architectures from [[RE_squarehead_discovair_g2plus.md]] and [[RE_beephonix_m2.md]]; start with SRP-PHAT on FPGA |
| Acoustic ML classification | High | Study Mind Foundry spectrogram-to-CV pipeline from [[RE_mind_foundry_sentry.md]]; build training dataset |
| IP67 enclosure for tropical environment | Medium | Partner with experienced CNC shop; test IP67 sealing + conformal coating per MIL-STD-810H |
| MIL-STD-810H/461G qualification testing | Medium | Contract with accredited test lab (S11) |
| SAPIENT/TAK integration | Medium | Open-source TAK SDK available; SAPIENT spec published by UK DSTL (BSI Flex 335) |
| Multi-node mesh networking | Medium | Study Fencepost MAFIA architecture from [[RE_ga_ems_fencepost.md]]; evaluate commercial mesh radio modules |

---

### S10: Competitors (Reference / Indirect Stakeholder)

| Field | Detail |
|-------|--------|
| **Who** | Squarehead Technology (Norway), BeephoniX (Netherlands), Mind Foundry (UK), DroneShield (Australia), Microflown AVISA (Netherlands), GA-EMS Fencepost (USA), Dedrone (Germany/USA), Fraunhofer IDMT (Germany) |
| **Role** | Alternative solutions; benchmark for performance and pricing; set customer expectations; potential competitive response to VN-CUAS market entry |
| **Interest** | LOW -- VN-CUAS targets the $2-5K price point where no competitor operates; Vietnamese market is not a primary target for Western vendors |
| **Influence** | MEDIUM -- Set customer expectations on detection performance, environmental qualification, and feature set; competitor specs become de facto requirements benchmarks |
| **Impact on Design** | Detection range, Pd/Pfa, classification accuracy, and environmental specs benchmarked against competitor products from [[competitive_landscape_analysis.md]] |

**Competitive Positioning (from Phase 0 RE analyses):**

| Factor | VN-CUAS | Squarehead G2+ | BeephoniX M2 | Mind Foundry | DroneShield |
|--------|---------|---------------|-------------|-------------|-------------|
| Cost/node | $2-5K | $15-50K | $5-15K | SW license | $100K+ (system) |
| Detection paradigm | Acoustic + ML | Acoustic (beamforming) | Acoustic (Doppler) | AI-first (any sensor) | Multi-sensor |
| Array type | 128-256 MEMS | 128 MEMS | 151 MEMS | Hardware-agnostic | Multi-modal |
| ML classification | Dual (eigenvector + CNN) | Optional ML layer | Bio-inspired | Spectrogram-to-CV | RFAI + optional |
| Weight (sensor) | <=2 kg | ~3 kg | 0.95 kg | N/A (SW) | >10 kg (system) |
| Tropical design | Native (designed-in) | Adapted (MIL-STD) | Temperate origin | N/A | Desert/temperate |
| Local content | >=60% | 0% | 0% | 0% | 0% |
| Vendor independence | Full | None | None | None | None |
| Multi-mission | Firmware-defined (C-UAS, C-RAM, gunshot, vehicle) | C-UAS only | C-UAS only | Software-defined | Multi-sensor C-UAS |

**Key Competitive Threats:**

| Threat | Source | Mitigation |
|--------|--------|-----------|
| BeephoniX drops to $5K | BeephoniX | Vietnamese cost structure advantage is structural; ML differentiation; multi-mission value |
| Mind Foundry matures hardware-agnostic AI | Mind Foundry | Control hardware quality; offer complete integrated solution; local support/manufacturing |
| Chinese competitor enters at $1-2K | Unknown | ML quality; MIL-STD certification; non-Chinese supply chain trust; multi-mission firmware |
| DroneShield bundles acoustic at lower price | DroneShield | Position VN-CUAS as affordable complementary layer; SAPIENT interoperability with any C2 |

---

### S11: International Partners (University / Test Laboratory)

| Field | Detail |
|-------|--------|
| **Who** | International university partners (acoustic/ML research: NTU Singapore, KAIST South Korea, UNSW Australia); accredited MIL-STD test laboratories (Singapore, South Korea, Australia); NATO research institutions (UK DSTL, TNO Netherlands, Fraunhofer Germany) |
| **Role** | Provides capabilities not available domestically: MIL-STD environmental testing, ML research collaboration, acoustic dataset sharing, SAPIENT conformance testing, acoustic propagation modeling |
| **Interest** | MEDIUM -- Academic publication opportunities; defense research funding; regional security cooperation; technology transfer programs |
| **Influence** | HIGH -- MIL-STD test certification is mandatory for procurement (S7 requirement); ML research partnership accelerates development timeline; SAPIENT conformance enables international interoperability |
| **Primary Needs** | Clear collaboration scope; IP protection framework; publication rights agreement; research funding; data sharing agreements; export control compliance |
| **Success Criteria** | MIL-STD-810H test campaign completed within 6 months; ML model trained on >=10 drone types with >=1000 recordings per type; SAPIENT conformance tested against UK DSTL reference implementation; joint publications |
| **Pain Points** | Export control restrictions on some defense technologies; IP ownership negotiations; long lead times for test facility scheduling (6-12 months); language barriers in technical documentation |
| **Communication** | Formal collaboration agreements (MoU/MoA), technical exchange visits, joint publications, quarterly progress reports |
| **Risk if Ignored** | Cannot achieve MIL-STD certification (equipment not available in Vietnam); ML performance lags without international research collaboration; SAPIENT interoperability not validated; longer development timeline |
| **Key Requirements Driven** | STD-001 (MIL-STD-810H testing), STD-002 (MIL-STD-461G testing), SIG-021 (ML dataset >=10 drone types), SIG-014 (SAPIENT BSI Flex 335 conformance testing), SAF-003 (acoustic propagation modeling for tropical terrain) |

---

## 3. RACI Matrix

### 3.1 RACI by Requirement Category (Pahl & Beitz 16 Categories)

| Requirement Category | S1 Customer | S2 User | S2b Commander | S3 Deployer | S4 Maintainer | S5 Intel | S6 Fusion | S7 Regulator | S8 Manufacturer | S9 Dev Team | S10 Competitors | S11 Intl Partner |
|---------------------|-------------|---------|-------------|-------------|--------------|----------|-----------|-------------|----------------|-------------|-----------------|-----------------|
| Geometry (enclosure, array) | I | C | -- | C | I | -- | -- | -- | C | **R/A** | -- | -- |
| Kinematics (tracking, DoA) | I | C | C | -- | -- | C | C | -- | -- | **R/A** | -- | C |
| Forces (mounting, wind load) | -- | -- | -- | C | C | -- | -- | C | C | **R/A** | -- | -- |
| Energy (power, battery) | I | C | -- | C | C | -- | -- | -- | C | **R/A** | -- | -- |
| Material (enclosure, PCB) | -- | -- | -- | -- | C | -- | -- | C | **C** | **R/A** | -- | -- |
| Signals (acoustic, ML, comms) | I | **C** | C | -- | I | C | **C** | C | -- | **R/A** | -- | C |
| Safety (electrical, ML risk) | C | I | I | I | I | -- | -- | **A** | I | **R** | -- | C |
| Ergonomics (UI, display, HMI) | C | **C** | C | C | C | C | C | -- | -- | **R/A** | -- | -- |
| Production (local content, DFM) | **A** | -- | -- | -- | -- | -- | -- | I | **C** | **R** | -- | I |
| Quality (Pd, Pfa, accuracy) | **A** | C | C | -- | I | C | C | C | C | **R** | -- | C |
| Assembly (modular, LRU) | -- | -- | -- | C | **C** | -- | -- | -- | C | **R/A** | -- | -- |
| Transport (carry, vehicle) | I | C | I | **C** | C | -- | -- | -- | C | **R/A** | -- | -- |
| Operation (continuous, shift) | I | **C** | C | I | I | C | C | C | -- | **R/A** | -- | -- |
| Maintenance (MTTR, MTBF) | I | I | -- | -- | **C** | -- | -- | -- | C | **R/A** | -- | -- |
| Costs (unit, lifecycle, BOM) | **A** | -- | -- | -- | -- | -- | -- | -- | C | **R** | -- | I |
| Schedule (delivery, milestones) | **A** | I | I | -- | -- | -- | -- | I | C | **R** | -- | C |

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

### 3.2 RACI by Key Activity

| Activity | S1 Customer | S2 User | S2b Commander | S3 Deployer | S4 Maintainer | S5 Intel | S6 Fusion | S7 Regulator | S8 Manufacturer | S9 Dev Team | S10 Competitors | S11 Intl Partner |
|----------|-------------|---------|-------------|-------------|--------------|----------|-----------|-------------|----------------|-------------|-----------------|-----------------|
| **Define requirements** | **A** | C | C | C | C | C | C | C | I | **R** | -- | I |
| **Design system** | I | C | C | C | C | I | C | I | C | **R/A** | -- | C |
| **Procure components** | I | -- | -- | -- | -- | -- | -- | -- | **R** | **A** | -- | I |
| **Build prototype** | I | -- | -- | -- | -- | -- | -- | -- | C | **R/A** | -- | -- |
| **Test/qualify** | I | C | I | C | -- | -- | I | **A** | -- | **R** | -- | **C** |
| **Deploy** | I | **R** | A | **R** | I | -- | I | -- | -- | C | -- | -- |
| **Maintain** | I | I | -- | -- | **R** | -- | -- | -- | C | C | -- | -- |
| **Update ML models** | -- | I | I | -- | -- | C | -- | -- | -- | **R/A** | -- | C |

---

## 4. ODI Segment to Stakeholder Mapping

This section maps the 4 customer segments identified in [[odi_analysis.md]] to the stakeholders who represent, influence, or constrain each segment.

### 4.1 Segment Mapping Table

| ODI Segment | Size | Primary Stakeholders | Influencing Stakeholders | Key Outcomes Driven |
|-------------|------|---------------------|-------------------------|-------------------|
| **A: Forward Force Protection** | 40% | S2 (Primary User), S3 (Deployer) | S1 (Customer), S2b (Commander) | O-35 (18.5), O-22 (18.0), O-29 (17.5), O-24 (15.0), O-08 (12.5), O-06 (11.5) |
| **B: Fixed-Site Security** | 30% | S2 (Primary User), S6 (Fusion Op) | S1 (Customer), S2b (Commander), S4 (Maintainer) | O-33 (15.0), O-42 (15.0), O-28 (15.5), O-37 (14.5), O-09 (14.0), CC-02 (16.0) |
| **C: Intelligence & Adaptation** | 20% | S5 (Intel Analyst), S9 (Dev Team) | S2b (Commander), S11 (Intl Partner) | O-47 (16.0), O-44 (15.5), O-52 (15.0), CC-15 (14.5), CC-16 (13.0) |
| **D: Tropical Environment** | 10% | S2 (Primary User), S7 (Regulator) | S8 (Manufacturer), S11 (Intl Partner) | O-30 (14.0), O-31 (14.0), O-32 (13.5), O-17 (12.0) |

### 4.2 Segment-Stakeholder Heat Map

```
                    Seg A       Seg B       Seg C       Seg D
                   Forward    Fixed-Site    Intel     Tropical
Stakeholder       (40%)       (30%)        (20%)      (10%)
-----------------------------------------------------------
S1  Customer       ●●●         ●●●          ●●         ●●
S2  Primary User   ●●●         ●●●          ●          ●●●
S2b Commander      ●●●         ●●●          ●●         ●
S3  Deployer       ●●●         ●            ●          ●●
S4  Maintainer     ●●          ●●●          ●          ●●
S5  Intel Analyst  ●           ●            ●●●        ●
S6  Fusion Op      ●           ●●●          ●          ●
S7  Regulator      ●●          ●●           ●          ●●●
S8  Manufacturer   ●●          ●●           ●          ●●●
S9  Dev Team       ●●●         ●●●          ●●●        ●●●
S10 Competitors    ●●          ●●           ●●         ●
S11 Intl Partner   ●           ●●           ●●●        ●●

Legend: ●●● = Primary stakeholder for this segment
        ●●  = Significant involvement
        ●   = Peripheral involvement
```

### 4.3 Segment Strategy Implications

| Segment | Entry Strategy | Stakeholder Engagement Priority |
|---------|---------------|-------------------------------|
| **A: Forward** (PRIMARY, Year 1) | Disruptive innovation -- $2-5K/node creates new market where none existed | S2 (operator feedback drives usability), S3 (deployment simplicity is critical), S2b (trust in alerts determines adoption) |
| **B: Fixed-Site** (Year 1-2) | Dominant growth -- mesh of 10-50 nodes for perimeter protection | S6 (SAPIENT/TAK integration is table stakes), S4 (24/7 operation demands high reliability), S2b (multi-target tracking for engagement decisions) |
| **C: Intelligence** (Year 2-3) | Differentiated -- ML platform creates unique intelligence value | S5 (analyst workflow drives data/API requirements), S11 (ML research partnership accelerates capability), S9 (ML pipeline architecture) |
| **D: Tropical** (Concurrent) | Niche -- designed-in from day one; no competitor addresses this | S7 (tropical MIL-STD-810H qualification), S8 (tropical-grade manufacturing), S11 (test lab for environmental qualification) |

---

## 5. Stakeholder Communication Plan

### 5.1 Communication Matrix

| Stakeholder | Frequency | Format | Language | Owner | Key Deliverables |
|-------------|-----------|--------|----------|-------|-----------------|
| **S1: Customer** | Monthly + gate reviews | Formal report, demo event | Vietnamese | Program Manager | Progress reports, cost updates, pilot results, procurement specifications |
| **S2: Primary User** | Bi-weekly during test phases | Field demonstration, hands-on training | Vietnamese | Systems Engineer | Operator manual, quick-reference card, training curriculum, feedback forms |
| **S2b: Commander** | Monthly + gate reviews | Command briefing, dashboard demo | Vietnamese | Program Manager | Executive summary, alert protocol SOP, engagement decision workflow |
| **S3: Deployer** | Phase 2-3 (design for deployment) | DFM review, setup training | Vietnamese | Hardware Engineer | Setup guide (pictorial), training module, confirmation feedback spec |
| **S4: Maintainer** | Phase 3-4 (design for maintenance) | Maintenance manual review, training | Vietnamese | Reliability Engineer | Maintenance manual, fault-code card, spare parts list, training course |
| **S5: Intel Analyst** | Quarterly | API documentation, interface demo | Vietnamese + English | SW Lead | API docs, data export specs, analyst workstation UI, query guide |
| **S6: Fusion Op** | Phase 2-3 (integration design) | SAPIENT/TAK integration test | Vietnamese + English | SW Lead | SAPIENT interface spec, TAK plugin, REST API docs, interop test results |
| **S7: Regulator** | Quarterly + certification gates | Formal compliance dossier | Vietnamese | Quality Manager | Test reports, safety analysis, compliance matrix, certification application |
| **S8: Manufacturer** | Bi-weekly during Phase 3-4 | DFM review, supplier audit | Vietnamese | Manufacturing Engineer | Manufacturing drawings, DFM checklist, BOM, assembly procedures, test specs |
| **S9: Dev Team** | Weekly (sprint cadence) | Stand-up, design review, sprint demo | Vietnamese + English | Tech Lead | Requirements spec, design docs, test plans, sprint backlog |
| **S10: Competitors** | Quarterly (market monitoring) | Competitive intelligence brief | English | Strategy Lead | Competitive landscape update, pricing intelligence, new product analysis |
| **S11: Intl Partner** | Monthly during active collaboration | Technical exchange, progress report | English | Program Manager | MoU/MoA, test plans, research proposals, joint publication drafts |

### 5.2 Gate Review Communication

| Phase Gate | Attendees | Format | Decision Required |
|------------|-----------|--------|------------------|
| Phase 1 to 2 | S1, S2, S2b, S7, S9 | Formal review + demo | Requirements approval; proceed to conceptual design |
| Phase 2 to 3 | S1, S2, S2b, S7, S8, S9 | Formal review + concept presentation | Concept selection; proceed to embodiment design |
| Phase 3 to 4 | S1, S2, S2b, S4, S7, S8, S9, S11 | Formal review + prototype demo | Design freeze; proceed to detail design and prototype build |
| Phase 4 to Production | All | Formal review + pilot deployment results | Production authorization; procurement contract |

### 5.3 Escalation Path

```
Level 1: Dev Team (S9) resolves technical issues internally
    |
Level 2: Program Manager escalates to Customer (S1) / Regulator (S7)
    |
Level 3: Customer (S1) escalates to higher command for budget/schedule/scope decisions
```

---

## 6. Key Requirements Driven by Each Stakeholder

This section consolidates all requirement IDs driven by each stakeholder for traceability to [[01_requirements/requirements_list.md]].

### 6.1 Requirements Traceability Summary

| Stakeholder | Requirement IDs | Count | Primary Categories |
|-------------|----------------|-------|-------------------|
| **S1: Customer** | CST-001, CST-002, PRD-001, ERG-001, STD-001, STD-002, SCH-001 | 7 | Cost, Production, Standards |
| **S2: Primary User** | SIG-001 to SIG-005, ERG-002, ERG-003, OPR-001 | 8 | Signals, Ergonomics, Operation |
| **S2b: Commander** | SIG-006, SIG-007, ERG-004, OPR-002, OPR-003 | 5 | Signals, Ergonomics, Operation |
| **S3: Deployer** | GEO-001, GEO-002, OPR-004, OPR-005, ERG-005, ERG-006, ASM-001 | 7 | Geometry, Operation, Ergonomics, Assembly |
| **S4: Maintainer** | MNT-001 to MNT-006, ASM-002, MAT-001 | 8 | Maintenance, Assembly, Material |
| **S5: Intel Analyst** | SIG-008 to SIG-013 | 6 | Signals |
| **S6: Fusion Op** | SIG-014 to SIG-019 | 6 | Signals |
| **S7: Regulator** | STD-001 to STD-004, SAF-001, SAF-002 | 6 | Standards, Safety |
| **S8: Manufacturer** | PRD-001 to PRD-004, MAT-002, MAT-003 | 6 | Production, Material |
| **S9: Dev Team** | SIG-020 to SIG-023, ENE-001, GEO-003 | 6 | Signals, Energy, Geometry |
| **S10: Competitors** | (benchmarks, not direct requirements) | -- | -- |
| **S11: Intl Partner** | STD-001, STD-002, SIG-021, SIG-014, SAF-003 | 5 | Standards, Signals, Safety |

### 6.2 Requirement ID Convention

| Prefix | Category | Examples |
|--------|----------|---------|
| GEO-xxx | Geometry | Dimensions, weight, form factor |
| SIG-xxx | Signals | Detection, classification, data, interfaces |
| ENE-xxx | Energy | Power consumption, battery life |
| MAT-xxx | Material | Materials selection, corrosion protection |
| SAF-xxx | Safety | Electrical safety, ML risk, environmental protection |
| ERG-xxx | Ergonomics | User interface, training, display |
| PRD-xxx | Production | Local content, DFM, quality control |
| ASM-xxx | Assembly | Modularity, connectors, LRU |
| OPR-xxx | Operation | Deployment, continuous operation, procedures |
| MNT-xxx | Maintenance | MTTR, MTBF, spare parts, diagnostics |
| CST-xxx | Cost | Unit cost, BOM cost, lifecycle cost |
| STD-xxx | Standards | MIL-STD, TCVN, SAPIENT compliance |
| SCH-xxx | Schedule | Delivery milestones, program timeline |

### 6.3 Top 20 Requirements by Stakeholder Priority

| Rank | Req ID | Requirement | Target | Driven By | ODI Source |
|------|--------|------------|--------|-----------|-----------|
| 1 | SIG-001 | Pd for Group 1 quadcopter at 300m | >=80% | S2, S1 | O-22 (18.0), O-29 (17.5) |
| 2 | SIG-002 | False alarm rate | <=1/hour | S2, S2b | O-28 (15.5) |
| 3 | SIG-003 | Alert latency (detection to alert) | <=3 seconds | S2, S2b | O-24 (15.0) |
| 4 | SIG-004 | Classification accuracy (4+ drone types) | >=75% | S2, S5 | O-27 (15.0) |
| 5 | SIG-005 | Simultaneous target tracking | >=3 targets | S2, S6 | O-33 (15.0) |
| 6 | SIG-006 | Classification confidence score | Percentage with each alert | S2b | CC-02 (16.0) |
| 7 | SIG-014 | SAPIENT-compliant track output | BSI Flex 335 | S6 | CC-18 (14.0) |
| 8 | SIG-023 | OTA ML model update | Firmware + model | S2, S9 | O-47 (16.0), O-44 (15.5) |
| 9 | CST-001 | Unit cost per node | <=$5,000 | S1 | Cost target |
| 10 | PRD-001 | Local content by value | >=60% | S1, S8 | Vietnamese defense policy |
| 11 | GEO-001 | Sensor head weight | <=2 kg | S3 | O-08 (12.5) |
| 12 | GEO-002 | Full node weight (incl. battery, radio) | <=5 kg | S3 | O-08 (12.5) |
| 13 | ENE-001 | Power consumption (sensor) | <=10W | S9 | O-17 (12.0) |
| 14 | OPR-004 | Single-node deployment time | <=15 min, 1 person | S3 | O-06 (11.5) |
| 15 | MNT-001 | Mean Time to Repair (module swap) | <=30 min | S4 | CC-11 (13.0) |
| 16 | MNT-002 | Mean Time Between Failures | >=5,000 hours | S4 | Reliability |
| 17 | STD-001 | MIL-STD-810H environmental qualification | Full compliance | S7, S11 | MIL-STD |
| 18 | SAF-001 | Environmental protection | IP67 | S7, S8 | Tropical requirement |
| 19 | SIG-008 | Detection event database | >=90 days online | S5 | CC-13 (13.0) |
| 20 | ERG-002 | Operator training time | <=8 hours | S2 | O-16 (12.0) |

---

## 7. Stakeholder Risks & Mitigations

| # | Risk | Stakeholder | Probability | Impact | Mitigation |
|---|------|------------|-------------|--------|------------|
| R1 | Customer rejects due to unproven detection performance (no combat record) | S1, S2b | High | High | Pilot deployment at operational unit with documented Pd/Pfa metrics; phased procurement starting with 10-node pilot ($20-50K); benchmark against visual observation baseline |
| R2 | Operators experience alarm fatigue from tropical false positives (insects, rain, birds) | S2 | High | High | Dual classification (eigenvector + ML) reduces Pfa; Bayesian confidence scoring; adaptive wind/rain noise floor thresholds; target Pfa <=1/hour per O-28 |
| R3 | Tactical commander does not trust ML classification for engagement decisions | S2b | Medium | High | Display confidence percentage with every alert; require >=90% confidence before "high-threat" classification; manual override capability; audit trail for after-action review |
| R4 | TCVN/MIL-STD certification pathway unclear for ML-based classification system | S7 | Medium | High | Early engagement with STAMEQ; map MIL-STD requirements in Phase 1; contract accredited test lab (S11) by Phase 2; develop ML validation methodology (statistical Pd/Pfa test protocol) |
| R5 | Local manufacturer cannot achieve MEMS array assembly quality (128-256 mics) | S8 | Medium | Medium | DFM review in Phase 3; avoid BGA packages; IPC-A-610 training; AOI inspection; pilot production run (10 units) before volume |
| R6 | Development team lacks acoustic ML/DSP expertise for C-UAS application | S9 | Medium | Medium | Study Mind Foundry spectrogram-to-CV pipeline; partner with university for ML research (S11); start with eigenvector classifier (GA-EMS approach) and add ML as training data accumulates |
| R7 | International partner collaboration delayed by export control or MoU negotiations | S11 | Medium | Medium | Identify multiple potential partners (Singapore, South Korea, Australia); begin MoU process in Phase 1; use non-controlled components only (ITAR-free design) |
| R8 | No labeled acoustic drone dataset exists for Vietnamese tropical environment | S9, S11 | High | High | Build dataset from Phase 1: record commercial drones (DJI Mavic, FPV) at Vietnamese field sites; augment with published datasets (DCASE, IDMT); transfer learning from pre-trained models |
| R9 | SAPIENT/TAK integration not tested with Vietnamese C2 systems | S6 | Medium | Medium | Use open-source ATAK for initial integration; SAPIENT test harness from UK DSTL; design REST API as universal fallback for any C2 system |
| R10 | Competitor (BeephoniX, Mind Foundry) enters $2-5K price point before VN-CUAS launch | S10 | Low | Medium | Vietnamese cost structure advantage is structural; speed to market with local manufacturing; firmware-defined multi-mission creates switching cost and broader value proposition |
| R11 | Monsoon/tropical conditions degrade acoustic detection more than expected | S2, S1 | High | Medium | O-32 is LOW-confidence outcome; prioritize tropical field testing in Phase 2; wind/rain noise cancellation algorithms; "degraded mode" with honest performance indication to operator |
| R12 | Insufficient DSP/ML engineering talent available in Vietnam | S9 | High | High | Partner with international university (S11); hire diaspora engineers; use established ML frameworks (TensorFlow Lite, ONNX); leverage open-source acoustic processing libraries |

---

## Cross-References

- [[odi_analysis.md]] -- ODI Rev B.0: 76 outcomes, 4 segments, opportunity scoring, consumption chain analysis
- [[competitive_landscape_analysis.md]] -- 8 systems, 6 paradigms, competitive positioning matrix
- [[phase0_synthesis.md]] -- Phase 0 gate review, product concept VN-CUAS v8.0
- [[01_requirements/requirements_list.md]] -- Requirements list (to be created, 16 Pahl & Beitz categories)
- [[RE_squarehead_discovair_g2plus.md]] -- Squarehead Discovair G2+ RE analysis
- [[RE_beephonix_m2.md]] -- BeephoniX M2 RE analysis
- [[RE_mind_foundry_sentry.md]] -- Mind Foundry SENTRY RE analysis
- [[RE_ga_ems_fencepost.md]] -- GA-EMS Fencepost RE analysis
- [[RE_microflown_avisa_skysentry.md]] -- Microflown AVISA SKYSENTRY RE analysis
- [[RE_droneshield_dronesentry.md]] -- DroneShield DroneSentry RE analysis
- [[RE_dedrone_dronetracker.md]] -- Dedrone DroneTracker RE analysis
- [[RE_fraunhofer_idmt_acoustic_drone_detection.md]] -- Fraunhofer IDMT RE analysis
