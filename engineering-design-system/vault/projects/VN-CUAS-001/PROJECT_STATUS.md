---
project: VN-CUAS-001
name: Counter-Unmanned Aircraft System (C-UAS)
codename: TBD
phase: 2
status: active
created: 2026-02-11
updated: 2026-02-12
re_count: 10
phase1_requirements: 153
phase1_quantified: 92%
phase1_gate: APPROVED
phase1_gate_date: 2026-02-12
---

# VN-CUAS-001 - Counter-Unmanned Aircraft System (C-UAS)

## Status
Phase 2 | Active | Updated: 2026-02-12
Progress: ░░░░░░░░░░ 0% (Phase 2 starting)

## Phase Progress
- [x] Phase 0: ODI Customer Insight & Reverse Engineering - **APPROVED** (2026-02-11)
- [x] Phase 1: Task Clarification (Requirements) - **APPROVED** (2026-02-12)
- [ ] Phase 2: Conceptual Design - **ACTIVE**
- [ ] Phase 3: Embodiment Design
- [ ] Phase 4: Detail Design

## Current Phase: 1 - Task Clarification (Requirements)

### Phase 1 Deliverables
- [x] Stakeholder Analysis (12 stakeholders, RACI matrix, ODI segment mapping)
- [x] Requirements List (153 requirements, 92 MUST / 61 WISH, 92% quantified, 16/16 categories)
- [x] Standards Mapping (9 standard families, 947 lines, $226K qualification budget)
- [x] Requirements Validation (8/8 gate criteria PASS, 25/25 ODI coverage, 0 conflicts)

### Phase 1 Statistics
| Metric | Value |
|--------|-------|
| Total requirements | 153 |
| MUST requirements | 92 (60%) |
| WISH requirements | 61 (40%) |
| Quantified | 92% (target ≥80%) |
| Categories covered | 16/16 |
| ODI top 25 coverage | 25/25 FULL |
| Unresolved conflicts | 0 |
| Standards mapped | 11 |
| TBDs open | 12 |
| Gate result | **8/8 PASS** |

---

## Phase 0 (Complete) - ODI & Reverse Engineering

### Reverse Engineering Analyses
- [x] Squarehead Technology Discovair G2+ (Norway) — **Passive acoustic array, 128 MEMS mics, beamforming + ML, 8 kg**
- [x] BeephoniX M2 (Netherlands) — **Bio-inspired acoustic array, 151 MEMS mics, Doppler beamforming + ML, 950 g**
- [x] Fraunhofer IDMT (Germany) — **Research institute, acoustic fingerprint + ML, sensor wake-up architecture, 50-200m, NLOS**
- [x] DroneShield DroneSentry (Australia) — **Multi-sensor fusion (RF + radar + optical + AI), RFAI engine 150+ drone models, $200K-1M+/site**
- [x] Dedrone DroneTracker (Germany/USA) — **Software-centric C2 platform, DroneDNA 600+ models, RF sensors 1.6-5km, Axon subsidiary**
- [x] Mind Foundry SENTRY (United Kingdom) — **AI-first acoustic intelligence, Oxford ML spin-out, Bayesian ML + spectrograms, ATAK integration <30s, hardware-agnostic**
- [x] GA-EMS Fencepost (USA) — **Classical signal processing (eigenvector), acoustic+seismic, 5-7km Group 3, 100-4000Hz, networked nodes, MAFIA C2, AI planned**
- [x] Microflown AVISA SKYSENTRY (Netherlands) — **Acoustic Vector Sensor (particle velocity), CASTLE platform, firmware-defined multi-mission, 250m quad/1km FW/10km helo, <2W, combat-proven Mali**
- [x] Rafael FIRE WEAVER C2 (Israel) — **Geo-Pixel STS, AI fire allocation, BNET SDR, DRONE DOME C-UAS, C2 integration patterns for VN-CUAS**
- [x] Elbit Systems C4I Suite (Israel) — **TORCH-X family, E-CiX SOA architecture, E-LynX SDR, enterprise C2 architecture patterns**

### Pending
- [x] ODI Analysis
- [x] Competitive landscape analysis
- [x] Phase 0 synthesis

## Product Concept (Preliminary)
Counter-UAS passive acoustic detection system for Vietnamese defense applications:
- **Passive** acoustic detection (no RF emissions)
- **Drone detection & classification** (Class I/II UAVs)
- Potential **C-RAM** (Counter-Rocket, Artillery, Mortar) capability
- **Jamming-proof** and GPS-independent operation
- MIL-STD-810H environmental qualification
- Vietnamese local content optimization

## Key Reference Systems
| System | Country | Technology | Key Feature |
|--------|---------|------------|-------------|
| **Squarehead Discovair G2+** | Norway | 128-mic beamforming + ML | Passive, 8 kg, MIL-STD-810H |
| **BeephoniX M2** | Netherlands | 151-mic bio-inspired beamforming + ML | Passive, 950g, 1-2° accuracy |
| **Fraunhofer IDMT** | Germany | Acoustic fingerprint + ML (research) | NLOS, sensor wake-up, algorithm-centric |
| **DroneShield DroneSentry** | Australia | RF (RFAI) + radar + optical + AI | Multi-sensor fusion, 4000+ units, 40+ countries, $200K-1M+/site |
| **Dedrone DroneTracker** | Germany/USA | RF (DroneDNA) + camera + API | Software-centric C2, 600+ models, Axon subsidiary, $50K-500K+ |
| **Mind Foundry SENTRY** | United Kingdom | Bayesian ML on acoustic signatures | AI-first, Oxford spin-out, ATAK <30s deploy, hardware-agnostic, ~$44M funded |
| **GA-EMS Fencepost** | USA | Eigenvector acoustic + seismic | Classical signal processing, 5-7km Group 3, networked nodes, GA $3.2B parent |
| **Microflown AVISA SKYSENTRY** | Netherlands | Acoustic Vector Sensor (particle velocity) | AVS physics, CASTLE platform, firmware-defined multi-mission, combat-proven Mali, <2W |
| RADA MHR | Israel | AESA radar | Long range, active |
| Robin Radar Elvira | Netherlands | FMCW radar | Micro-drone optimized |

## Files

### Phase 0 — Reverse Engineering
- [[RE_squarehead_discovair_g2plus.md]] - **Squarehead Discovair G2+ (Norway): 128-mic passive acoustic array, beamforming + ML, C-UAS/C-RAM**
- [[RE_beephonix_m2.md]] - **BeephoniX M2 (Netherlands): 151-mic bio-inspired acoustic array, Doppler beamforming + ML, 950g ultra-light**
- [[RE_fraunhofer_idmt_acoustic_drone_detection.md]] - **Fraunhofer IDMT (Germany): Research institute, acoustic fingerprint + ML, sensor wake-up, NLOS detection, 50-200m**
- [[RE_droneshield_dronesentry.md]] - **DroneShield DroneSentry (Australia): Multi-sensor C-UAS (RF + radar + optical + AI), RFAI engine 150+ drones, 4000+ sold, ASX:DRO A$2.9B**
- [[RE_dedrone_dronetracker.md]] - **Dedrone DroneTracker (Germany/USA): Software-centric C2 platform, DroneDNA 600+ models, RF sensors 1.6-5km, acquired by Axon Oct 2024**
- [[RE_mind_foundry_sentry.md]] - **Mind Foundry SENTRY (UK): AI-first acoustic intelligence, Oxford ML spin-out, Bayesian ML + spectrograms → CV, ATAK <30s mobile deploy, hardware-agnostic, NIGHTINGALE ASW cross-domain**
- [[RE_ga_ems_fencepost.md]] - **GA-EMS Fencepost (USA): Classical signal processing (eigenvector), acoustic+seismic dual-modality, 5-7km Group 3 range, 100-4000Hz, networked nodes, MAFIA C2, GA $3.2B parent, AI planned**
- [[RE_microflown_avisa_skysentry.md]] - **Microflown AVISA SKYSENTRY (Netherlands): Acoustic Vector Sensor (particle velocity), CASTLE platform, 4 AMMS per post, firmware-defined multi-mission (7+ missions), 250m quad/1km FW/10km helo, <2W, combat-proven Mali MINUSMA, sole AVS manufacturer**
- [[RE_rafael_fire_weaver_c2.md]] - **Rafael FIRE WEAVER & C2 Ecosystem (Israel): Geo-Pixel GPS-independent STS, AI fire allocation, BNET SDR (100+ Mbps MANET), DRONE DOME C-UAS (radar+EO/IR+jammer+laser), Iron Beam $2/shot. C2 integration patterns for VN-CUAS sensor-to-C2 layer**
- [[RE_elbit_systems_c4i_c2_suite.md]] - **Elbit Systems C4I Suite (Israel): TORCH-X family (HQ/Mounted/Fires/Naval), E-CiX open SOA middleware, E-LynX SDR (MANET 35 Mbps), $6.8B revenue. Enterprise C2 architecture patterns for VN-CUAS integration layer**

### Phase 0 — Analysis
- [[odi_analysis.md]] - **ODI Rev B.0: 76 outcomes (52 primary + 20 consumption chain + 4 ES), 14 EXTREME, evidence-based scoring, weighted scorecard (VN-CUAS 6.8 #1), $20-65M SOM, 15-Q survey instrument. #1: detect RF-silent drones (Opp=18.5).**
- [[competitive_landscape_analysis.md]] - **Competitive landscape: 8 systems, 6 paradigms, 7 countries. White space at $2-5K ML-enhanced acoustic node. 10 strategic recommendations.**
- [[phase0_synthesis.md]] - **Phase 0 Synthesis: 11 deliverables, 8 RE analyses, 52 ODI outcomes, product concept v8.0, 10/10 gate criteria PASS. Recommends Phase 1 transition.**

### Phase 1 — Requirements
- [[01_requirements/stakeholder_analysis.md]] - **Stakeholder Analysis: 12 stakeholders (S1-S11), interest/influence map, RACI matrix, ODI segment mapping, communication plan, 12 risks identified**
- [[01_requirements/requirements_list.md]] - **Requirements List: 153 requirements (92 MUST / 61 WISH), 16 P&B categories, 92% quantified, all 14 EXTREME ODI outcomes traced, 7 conflicts resolved, 12 TBDs**
- [[01_requirements/standards_mapping.md]] - **Standards Mapping: 9 standard families (MIL-STD-810H, 461G, 882E, 217F, IP67, UN 38.3, NATO STANAG, TCVN, SW/Cyber), 947 lines, $226K qualification budget**
- [[01_requirements/requirements_validation.md]] - **Requirements Validation: 8/8 gate criteria PASS, 25/25 ODI coverage, 0 unresolved conflicts, Phase 1→2 gate review ready**
