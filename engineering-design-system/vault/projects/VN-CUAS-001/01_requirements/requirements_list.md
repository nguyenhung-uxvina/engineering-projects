---
project: VN-CUAS-001
phase: 1
type: requirements
version: 1.0
created: 2026-02-11
status: draft
total_requirements: 153
must_count: 92
wish_count: 61
quantified_pct: 92%
---

# REQUIREMENTS LIST
## VN-CUAS-001: Counter-UAS Passive Acoustic Detection System
### Version: 1.0 | Date: 2026-02-11

---

## 1. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-11 | Engineering Design System | Initial release - derived from ODI Rev B.0 (76 outcomes, 14 EXTREME, 28 HIGH), 8 RE analyses, competitive landscape analysis, and phase0 synthesis |

---

## 2. PROJECT OVERVIEW

| Field | Value |
|-------|-------|
| **Product Name** | VN-CUAS Passive Acoustic Detection Node (Codename: TBD-001) |
| **Project Code** | VN-CUAS-001 |
| **Customer** | Vietnamese People's Army (VPA), Air Defense, Border Defense, Base Security, Critical Infrastructure Protection |
| **End Users** | Air defense / force protection operators (Trung si NCO level), tactical commanders, system deployers, maintenance technicians |
| **Development Period** | 2026 Q1 - 2028 Q2 |
| **Target Cost** | $2,000-5,000 per node (lot size 50+) |
| **Product Concept** | VN-CUAS v8.0: Affordable ML-enhanced passive acoustic C-UAS detection node |
| **Growth Strategy** | Disruptive innovation (Segment A: Forward Force Protection) + Dominant growth (Segment B: Fixed-Site) |
| **Innovation Target** | Occupy white space: low-cost ($2-5K) + acoustic + ML (no competitor) |

### Source Documents

- [[odi_analysis.md]] - Phase 0 ODI Rev B.0 (76 outcomes, 52 primary + 20 CC + 4 ES)
- [[phase0_synthesis.md]] - Phase 0 synthesis and gate review (10/10 PASS)
- [[competitive_landscape_analysis.md]] - 8-system competitive analysis, 6 paradigms
- [[RE_squarehead_discovair_g2plus.md]] - RE: Squarehead G2+ (128 MEMS, beamforming)
- [[RE_beephonix_m2.md]] - RE: BeephoniX M2 (151 MEMS, bio-inspired Doppler)
- [[RE_fraunhofer_idmt_acoustic_drone_detection.md]] - RE: Fraunhofer IDMT (algorithm-centric)
- [[RE_droneshield_dronesentry.md]] - RE: DroneShield DroneSentry (multi-sensor)
- [[RE_dedrone_dronetracker.md]] - RE: Dedrone DroneTracker (RF-centric, DroneDNA)
- [[RE_mind_foundry_sentry.md]] - RE: Mind Foundry SENTRY (AI-first, Bayesian)
- [[RE_ga_ems_fencepost.md]] - RE: GA-EMS Fencepost (eigenvector, seismic)
- [[RE_microflown_avisa_skysentry.md]] - RE: Microflown AVISA SKYSENTRY (AVS, multi-mission)

---

## 3. REQUIREMENTS SUMMARY

| # | Category | Prefix | MUST | WISH | Total | Quantified % |
|---|----------|--------|------|------|-------|-------------|
| 1 | Geometry | GEO | 6 | 5 | 11 | 100% |
| 2 | Kinematics | KIN | 4 | 4 | 8 | 100% |
| 3 | Forces | FOR | 4 | 2 | 6 | 100% |
| 4 | Energy | ENE | 6 | 5 | 11 | 91% |
| 5 | Material | MAT | 5 | 4 | 9 | 78% |
| 6 | Signals | SIG | 14 | 6 | 20 | 95% |
| 7 | Safety | SAF | 5 | 3 | 8 | 75% |
| 8 | Ergonomics | ERG | 5 | 5 | 10 | 90% |
| 9 | Production | PRD | 5 | 4 | 9 | 89% |
| 10 | Quality | QUA | 9 | 3 | 12 | 100% |
| 11 | Assembly | ASM | 3 | 4 | 7 | 86% |
| 12 | Transport | TRN | 3 | 3 | 6 | 100% |
| 13 | Operation | OPR | 9 | 3 | 12 | 100% |
| 14 | Maintenance | MNT | 5 | 5 | 10 | 90% |
| 15 | Costs | CST | 5 | 3 | 8 | 100% |
| 16 | Schedule | SCH | 4 | 2 | 6 | 100% |
| | **TOTAL** | | **92** | **61** | **153** | **92%** |

**Gate 1 Target: >=80% quantified -- ACHIEVED (92%)**

---

## 4. DETAILED REQUIREMENTS

### 4.1 Geometry (GEO)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| GEO-001 | Sensor array form factor | Cylindrical or hemispherical array assembly | MUST | I | O-34 | RE: Squarehead (cylindrical), Microflown (spherical AVS) | Hemispherical coverage requires 3D arrangement; cylindrical is simpler for planar array |
| GEO-002 | Array diameter | 200-400 mm | MUST | I | O-09, O-25 | RE: Squarehead (~350mm), BeephoniX (~250mm) | Larger aperture = better angular resolution; must balance with weight/portability |
| GEO-003 | Array height | 150-300 mm | MUST | I | O-08 | RE: Squarehead, Microflown AMMS (compact head) | Height affects elevation beamforming; cylindrical height sets vertical aperture |
| GEO-004 | MEMS microphone count | 128-256 microphones | MUST | I | O-22, O-25 | RE: Squarehead (128), BeephoniX (151) | 128 minimum for adequate spatial resolution; 256 wish for improved SNR and DoA |
| GEO-005 | Microphone inter-element spacing | 8-25 mm (optimized for 50-20,000 Hz) | MUST | I | O-25, O-30 | Published MEMS array literature; spatial Nyquist criterion | Spacing = c/(2*f_max) for alias-free beamforming; 8.5mm for 20 kHz |
| GEO-006 | Sensor head weight (array + enclosure + electronics) | <=2 kg | MUST | I | O-08 (12.5) | RE: BeephoniX (950g), Microflown AMMS (1.75 kg) | Critical for man-portable requirement; competitive with best-in-class |
| GEO-007 | Full node weight (sensor + battery + radio + GPS + cables) | <=5 kg | WISH (W=5) | I | O-08, O-07 | Phase0 synthesis v8.0 target | 1-person carry; includes all components for standalone operation |
| GEO-008 | Node enclosure external dimensions | <=450 x 450 x 400 mm (L x W x H) overall | WISH (W=4) | I | O-06 | Derived from transport case size constraints | Must fit in Pelican 1560 or equivalent transit case |
| GEO-009 | Mounting interface — tripod | Standard 1/4"-20 or 3/8"-16 thread + NATO accessory rail | WISH (W=4) | I | CC-06 | Standard camera/survey tripod compatibility | Enables use of COTS tripods; reduces proprietary hardware |
| GEO-010 | Mounting interface — mast/pole | Clamp mount for 25-75 mm diameter poles | WISH (W=3) | I | O-06 | Field deployment flexibility | Enables elevated mounting on existing infrastructure |
| GEO-011 | Mesh radio antenna dimensions | <=150 mm length (whip or stub antenna) | WISH (W=3) | I | SIG-013 | Derived from radio module integration | Integrated or removable; must not exceed node envelope significantly |

### 4.2 Kinematics (KIN)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| KIN-001 | Angular coverage per node | >=360 deg azimuth, >=0-90 deg elevation (hemispherical) | MUST | T | O-34, O-09 | RE: Microflown CASTLE (hemispherical with 4 AMMS); Squarehead (360 deg azimuth) | Full hemispherical is minimum for unattended node; no blind spots overhead |
| KIN-002 | Beamforming scan rate | >=10 full-sphere scans per second | MUST | T | O-24, O-39 | Derived from <=3s alert latency and multi-target tracking | Ensures detection of fast-moving targets within 1 scan cycle |
| KIN-003 | Target velocity range — detection | 0-250 km/h (hovering to fast fixed-wing) | MUST | T | O-22, O-23 | RE: Fencepost (Group 3 up to 250 km/h); DJI Mavic max 72 km/h; FPV up to 150 km/h | Must detect stationary hovering drone and high-speed dive attack |
| KIN-004 | Track update rate | >=2 Hz (2 updates/second per tracked target) | MUST | T | O-39, O-37 | Derived from operator display refresh and trajectory prediction needs | >=1 Hz minimum per ODI; 2 Hz enables meaningful trajectory prediction |
| KIN-005 | Pan/tilt motorized mount | Optional motorized pan/tilt for directional listening mode | WISH (W=2) | D | O-34 | Future capability; not required for V1.0 | Enables sector focus for reduced power or enhanced range in priority direction |
| KIN-006 | Vehicle-mounted vibration tolerance | Operate while vehicle stationary with engine running; degrade gracefully while moving | WISH (W=4) | T | O-06 | RE: Microflown (vehicle-mounted capability); operational scenario | Self-noise cancellation algorithm needed for vehicle mount |
| KIN-007 | Deployment positions | Ground (tripod), elevated (mast 2-5m), vehicle-mounted, rooftop | WISH (W=5) | D | O-06, O-10 | RE: SKYSENTRY (tripod, mast, vehicle); Squarehead (fixed, mobile) | Multiple deployment modes from single hardware |
| KIN-008 | Target altitude coverage | 0-500m AGL (within detection range) | WISH (W=4) | T | O-22, O-23 | Derived from Group 1-3 operational altitudes | Group 1: typically 0-150m; Group 2-3: 150-500m; elevation angle from array geometry |

### 4.3 Forces (FOR)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| FOR-001 | Wind loading — operational | Withstand sustained wind 70 mph (113 km/h) per MIL-STD-810H Method 510.7 on tripod mount | MUST | T | O-31 | MIL-STD-810H; RE: Squarehead (MIL-STD-810H certified) | Structural integrity + mounting stability; tropical typhoon exposure |
| FOR-002 | Shock resistance | Per MIL-STD-810H Method 516.8, Procedure I, 40g 11ms half-sine | MUST | T | O-30, O-31 | MIL-STD-810H | Handling and transit shock; drop during field deployment |
| FOR-003 | Vibration resistance | Per MIL-STD-810H Method 514.8, Category 4 (truck transport) and Category 24 (field use) | MUST | T | O-30 | MIL-STD-810H; RE: Squarehead (MIL-STD-810H) | Both transport and operational vibration environments |
| FOR-004 | Drop resistance | Survive 1.5m drop onto concrete without loss of function | MUST | T | CC-06, O-06 | Field handling requirement; RE: ruggedized military equipment standard | Critical for field deployment by NCO-level operators |
| FOR-005 | Tripod/mount wind loading stability | Tripod mount maintains sensor pointing within <=1 deg under 40 km/h sustained wind | WISH (W=4) | T | O-31, O-25 | Derived from DoA accuracy requirement under wind | Wind-induced vibration degrades DoA; damped mount recommended |
| FOR-006 | Ballistic protection | None required (passive sensor, not armor) | WISH (W=1) | A | — | System is not designed for direct fire exposure | Sensor is expendable at $2-5K; not cost-effective to armor |

### 4.4 Energy (ENE)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| ENE-001 | Sensor head power consumption | <=10W continuous average (target <=7W) | MUST | T | O-17 (12.0) | Phase0 v8.0 target; RE: Microflown (<2W), Squarehead (20W) | Target between AMMS and Squarehead; ARM+FPGA power budget |
| ENE-002 | Full node power consumption | <=15W continuous average (sensor + radio + GPS + processor) | MUST | T | O-17 | Derived from ENE-001 + radio (2-3W) + GPS (0.5W) + margin | Radio and GPS add ~3-5W to sensor head power |
| ENE-003 | Battery capacity | >=240 Wh (sufficient for >=24h at <=10W average) | MUST | T | O-17, phase0 v8.0 | Derived: 10W x 24h = 240 Wh; 15W x 24h = 360 Wh | Use 240 Wh minimum; recommend 300 Wh for margin |
| ENE-004 | Battery operating duration | >=24 hours continuous on battery (at 25 deg C, sensor + radio active) | MUST | T | O-17 | Phase0 v8.0 target; forward deployment requirement | 24h covers full day cycle; 48h wish for extended operations |
| ENE-005 | Battery type | Lithium-ion or lithium iron phosphate (LiFePO4), rechargeable | MUST | I | O-17 | Industry standard for military portable electronics | LiFePO4 preferred for safety and cycle life; Li-ion for energy density |
| ENE-006 | External power interface | 12-28V DC input (MIL-STD-1275E compatible for vehicle power) | MUST | T | O-17 | RE: standard military power bus | Enables vehicle power, generator, and solar panel input |
| ENE-007 | Battery field-swap time | <=2 minutes with gloves, no tools | WISH (W=5) | D | O-06, CC-12 | Operational continuity requirement | Quick-release battery module; maintains power during swap via capacitor/buffer |
| ENE-008 | Solar panel interface | Compatible with 12-28V DC solar panel input; >=20W panel for indefinite operation | WISH (W=4) | T | O-17 | Extended deployment (fixed-site, border) | 20W panel at 5h sun = 100 Wh/day; supplements 240 Wh battery |
| ENE-009 | Power management — sleep/wake mode | Sleep mode <=0.5W; wake on acoustic event or timer (configurable 1-60s cycle) | WISH (W=4) | T | O-17 | RE: Fraunhofer IDMT (sensor wake-up concept); Microflown (<2W) | Sensor wake-up extends battery to 72h+ for low-threat periods |
| ENE-010 | Battery weight | <=2.0 kg (included in GEO-007 5 kg node total) | WISH (W=4) | I | O-08 | Derived from 240 Wh / 160 Wh/kg (LiFePO4) = 1.5 kg | LiFePO4 at 90-120 Wh/kg = 2.0-2.7 kg; Li-ion at 150-200 Wh/kg = 1.2-1.6 kg |
| ENE-011 | Operating voltage range (internal bus) | 3.3V, 5V, 12V internal rails with >=90% efficiency DC-DC | WISH (W=3) | T | — | Standard embedded power architecture | FPGA (1.0-3.3V), processor (1.8-3.3V), radio (3.3V), ADC (3.3-5V) |

### 4.5 Material (MAT)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| MAT-001 | Enclosure material — sensor head | Aluminum alloy 6061-T6 (CNC machined) or glass-filled nylon (injection molded) | MUST | I | O-08, O-30 | RE: Squarehead (zinc-steel); design decision for weight reduction | Aluminum for prototype/low volume; nylon for high volume production |
| MAT-002 | IP67 sealing — gasket material | Silicone or EPDM rubber, rated -40 deg C to +200 deg C | MUST | I | O-30, O-31, O-32 | IP67 sealing requirement for tropical monsoon | Long-term UV and ozone resistance in tropical environment |
| MAT-003 | UV resistance | Enclosure survives >=5 years continuous tropical sun exposure without degradation | MUST | T | O-30 | MIL-STD-810H Method 505.7; tropical deployment | UV-stabilized coating (powder coat) or UV-resistant polymer |
| MAT-004 | Corrosion resistance — salt spray | >=500 hours per MIL-STD-810H Method 509.7 (5% NaCl salt fog) | MUST | T | O-30 | MIL-STD-810H; Vietnamese coastal installations (Da Nang, Cam Ranh, Phu Quoc) | Anodized aluminum + powder coat; or marine-grade polymer |
| MAT-005 | PCB conformal coating | IPC-CC-830C Type AR (acrylic) or UR (polyurethane) | MUST | I | O-30, O-32 | Tropical humidity protection; RE: all competitors in mil-spec products | Protects against humidity, salt, fungal growth |
| MAT-006 | Wind/rain protection for MEMS | Acoustic-transparent wind screen (open-cell foam) + rain cap (hydrophobic mesh) | WISH (W=5) | T | O-31, O-32 | RE: Microflown (wind protection); acoustic measurement practice | Wind noise reduction >=20 dB; rain impact noise attenuation; must not attenuate drone frequencies |
| MAT-007 | Cable materials | UV-resistant, abrasion-resistant jacket; shielded (EMI) | WISH (W=4) | I | O-30 | Field deployment durability | Outdoor-rated Cat6 for data; silicone or TPE for power cables |
| MAT-008 | Fastener material | Stainless steel 316 (marine-grade) for all external fasteners | WISH (W=4) | I | O-30, MAT-004 | Salt spray environment; RE: all competitors use SS fasteners | Critical for coastal and maritime deployments |
| MAT-009 | RoHS compliance | RoHS 3 (EU 2015/863) compliant | WISH (W=2) | I | — | Export market enablement | Enables European/international sales; not required for Vietnamese military |

### 4.6 Signals (SIG)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| SIG-001 | Microphone type | MEMS microphone (Knowles, InvenSense, or equivalent commodity) | MUST | I | O-22, GEO-004 | RE: Squarehead (128 MEMS), BeephoniX (151 MEMS) | Commodity MEMS ($0.50-2.00 each) for cost target; TBD-007 specific model |
| SIG-002 | Microphone frequency response | 50-20,000 Hz (usable bandwidth) | MUST | T | O-22, O-23 | RE: Fencepost (100-4000 Hz); broader range captures Group 1 harmonics (4-16 kHz) | Low end for Group 2-3 propulsion; high end for small quadcopter motor harmonics |
| SIG-003 | Microphone SNR | >=65 dB(A) (A-weighted signal-to-noise ratio) | MUST | T | O-22, O-30 | MEMS microphone specification; typical Knowles SPH0645LM4H = 65 dB | Higher SNR = better detection range; 65 dB is commodity floor |
| SIG-004 | ADC resolution | >=16-bit per channel | MUST | T | O-22, O-25 | Increased from 12-bit (VN-RNG) for wider dynamic range in C-UAS application | 96 dB dynamic range; captures both nearby (<50m) and distant (>300m) targets |
| SIG-005 | ADC sampling rate | >=48 kHz per channel (simultaneous sampling, 128-256 channels) | MUST | T | O-25, SIG-002 | Nyquist for 20 kHz bandwidth; RE: standard audio sampling rate | 48 kHz minimum; 96 kHz wish for oversampling benefit |
| SIG-006 | Direction of Arrival (DoA) algorithm | MUSIC/ESPRIT hybrid or equivalent high-resolution DoA | MUST | T | O-25 (13.0) | RE: Squarehead (beamforming), Fencepost (eigenvector), BeephoniX (Doppler) | MUSIC for broadband DoA; ESPRIT for frequency-specific; beamforming for spatial filtering |
| SIG-007 | DoA accuracy — standalone | <=3 deg azimuth, <=5 deg elevation (single node, reference conditions) | MUST | T | O-25 | Phase0 v8.0 target; RE: BeephoniX (1-2 deg), Squarehead (<10 deg) | Reference: target at 200m, wind <15 km/h, ambient <50 dB(A) |
| SIG-008 | DoA accuracy — networked | <=0.5 deg azimuth (>=3 nodes, triangulation) | WISH (W=5) | T | O-25, O-26 | Phase0 v8.0 target; RE: Microflown V-AMMS (0.2 deg) | Triangulation with >=3 nodes at >=100m baseline separation |
| SIG-009 | Range estimation method | Multi-node triangulation (>=3 nodes required); single-node range estimated via signal decay model | MUST | T | O-26 (14.0) | RE: Fencepost (6-node), Microflown (multi-CASTLE); physics of acoustic ranging | Single-node range accuracy: +/-50%; multi-node: +/-10% at <500m |
| SIG-010 | Classification output format | JSON: {type, confidence_pct, bearing_deg, elevation_deg, range_est_m, track_id, timestamp_utc, node_id} | MUST | D | CC-02 (16.0), O-27 | Design specification for C2 integration | Bayesian confidence percentage per classification; enables commander decision |
| SIG-011 | C2 interface — primary | TAK plugin (ATAK/WinTAK) + RESTful API (V1.0) | MUST | D | O-11 (13.0) | Phase0 v8.0; RE: Mind Foundry (ATAK), DroneShield (SAPIENT) | TAK is deployed across NATO/partner nations; REST API for custom integration |
| SIG-012 | C2 interface — SAPIENT | SAPIENT (Sensing for Asset Protection with Integrated Electronic Networked Technology) v3.0+ | WISH (W=5) | D | O-11 | RE: DroneShield, Dedrone (SAPIENT interface); NATO standard for autonomous sensors | V3.0 target; enables plug-and-play with NATO C-UAS architectures |
| SIG-013 | Mesh radio — frequency band | 900 MHz ISM (primary) or 2.4 GHz ISM (secondary) | MUST | T | O-12 | Design decision; 900 MHz for better range and penetration | 900 MHz preferred for range (forests, urban); 2.4 GHz for bandwidth; TBD in Phase 2 |
| SIG-014 | Mesh radio — range | >=500m line-of-sight between nodes (target 1000m) | MUST | T | O-12, O-46 | Phase0 v8.0; RE: Microflown (multi-node mesh) | Node spacing drives coverage; 500m minimum for practical deployment geometry |
| SIG-015 | Mesh radio — protocol | Self-forming, self-healing mesh; auto-discovery of new nodes | MUST | T | O-46, O-12 | RE: Fencepost (6-node), Microflown (multi-CASTLE) | Node failure must not collapse network; remaining nodes re-route automatically |
| SIG-016 | GPS/GNSS | Integrated GNSS receiver (GPS + GLONASS + BeiDou); position accuracy <=3m CEP | MUST | I | O-25, O-26 | Position stamping for all detections; triangulation baseline computation | BeiDou inclusion for Southeast Asian regional coverage |
| SIG-017 | Data interface — local | USB-C for configuration, firmware update, data download | WISH (W=4) | I | O-48, O-50 | Standard interface for field maintenance and data extraction | USB 2.0 minimum; USB 3.0 wish for large dataset download |
| SIG-018 | Edge processor | ARM Cortex-A class (quad-core >=1.5 GHz) for ML inference | WISH (W=5) | I | O-27, O-47 | RE: Mind Foundry (hardware-agnostic AI); spectrogram-to-CNN pipeline | Cortex-A53 or A72 class; runs TensorFlow Lite / ONNX inference engine |
| SIG-019 | DSP co-processor | FPGA (Xilinx/Lattice) or dedicated DSP for real-time beamforming | WISH (W=5) | I | O-25, SIG-006 | RE: Squarehead (FPGA beamforming); 128-256 ch x 48 kHz = high throughput | FPGA handles beamforming; ARM handles ML classification; parallel pipeline |
| SIG-020 | Data logging — on-node | SD card or eMMC storage; >=256 GB capacity; >=72h continuous spectrogram recording | WISH (W=4) | T | O-52 (15.0), O-48 | RE: operational need for ML training data; phase0 v8.0 | 72h at 128ch x 48kHz x 16bit = ~2.5 TB raw; compressed spectrograms = ~200 GB |

### 4.7 Safety (SAF)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| SAF-001 | EMC — passive mode emissions | Zero intentional RF emissions in passive/EMCON mode; unintentional emissions per MIL-STD-461G RE102 | MUST | T | O-35 (18.5) | #1 EXTREME ODI outcome; passive acoustic must not emit RF | EMCON mode: mesh radio OFF, GPS receiver only; zero RF signature |
| SAF-002 | Battery safety | UN 38.3 transport certification; BMS with overcharge, overdischarge, short-circuit, over-temperature protection | MUST | T | ENE-005 | Lithium battery safety standard; military transport requirement | Battery supplier must provide UN 38.3 test report |
| SAF-003 | Fail-safe — graceful degradation | Partial array failure (up to 25% microphones failed) = reduced performance, NOT system failure | MUST | T | O-21, O-19 | RE: array redundancy principle; MIL-STD-882E fail-safe | Degraded mode: reduced angular accuracy and detection range; alert operator |
| SAF-004 | Cybersecurity — communications | AES-256 encryption on all mesh radio communications | MUST | T | CC-03, O-35 | Military communications security requirement | Prevents adversary from spoofing, jamming, or intercepting detection data |
| SAF-005 | Secure boot and firmware signing | Cryptographic firmware verification at boot; reject unsigned/modified firmware | MUST | T | O-47, SAF-004 | Cybersecurity requirement; prevent adversary firmware manipulation | Hardware root of trust; signed OTA updates only |
| SAF-006 | Lightning protection | Transient voltage suppression on external interfaces (antenna, power, data) | WISH (W=4) | T | O-30 | Tropical thunderstorm environment; elevated mast mounting | MOV/TVS on all external connectors; grounding path to earth |
| SAF-007 | No hazardous materials | No asbestos, heavy metals (Pb, Hg, Cd, Cr6+) beyond RoHS limits | WISH (W=3) | I | MAT-009 | Environmental and safety compliance | Applies to enclosure, PCB, battery, cables |
| SAF-008 | FMEA completion | Failure Modes and Effects Analysis completed before prototype test | WISH (W=5) | A | — | MIL-STD-882E safety process | Identify single-point failures; design in redundancy for critical functions |

### 4.8 Ergonomics (ERG)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| ERG-001 | Operator training time — basic operation | <=8 hours for basic monitor + alert response (target <=4h) | MUST | D | O-16 (12.0), O-10 | Phase0 v8.0; operator is NCO-level (6-12 months MOS training) | Vietnamese military instructor can train operators in 1-day course |
| ERG-002 | Deployment by 1 person | Single operator can carry, emplace, power-on, and connect 1 node in <=15 minutes | MUST | D | O-06 (11.5), O-07 | Phase0 v8.0; RE: Microflown SKYSENTRY (<10 min) | Full sequence: unpack, mount on tripod, power on, verify operational |
| ERG-003 | Tool-free setup | No special tools required for field deployment; all connections tool-free or standard hex/Philips | MUST | D | CC-05, CC-06 | RE: military field deployment requirement | Quick-release mounts, push-lock connectors, tool-free battery swap |
| ERG-004 | Status indicators | LED indicators: green (operational), amber (degraded/warning), red (fault/alert); visible at 5m | MUST | I | O-19, O-41 | Standard military equipment status indication | IR-compatible mode (wish) for night operations |
| ERG-005 | Operator interface — C2 application | Ruggedized tablet or smartphone app; map-based display with alert overlay | MUST | D | O-41, CC-01, CC-04 | RE: Mind Foundry (ATAK); DroneShield (tablet C2) | Android-based; COTS ruggedized tablet ($300-800) |
| ERG-006 | Language — interface | Vietnamese primary + English secondary; user-switchable | WISH (W=5) | D | — | Vietnamese market requirement | All menus, alerts, status messages, and reports bilingual |
| ERG-007 | Night operation — IR-compatible LEDs | LED indicators switchable to IR mode (visible only with NVG) | WISH (W=4) | I | O-35 | Tactical night operations; maintain visual signature discipline | Toggle via button or software command |
| ERG-008 | Audio alert capability | Configurable audible alert (buzzer/speaker) for high-confidence detections | WISH (W=3) | D | CC-01, O-24 | Operator awareness when not watching screen | Adjustable volume; configurable threshold (e.g., only >80% confidence) |
| ERG-009 | Glove-operable controls | All buttons and connectors operable with standard military gloves | WISH (W=4) | D | O-06 | Field deployment in cold/tactical conditions | Minimum button size 15mm; no recessed switches |
| ERG-010 | Intuitive mounting orientation | Keyed connectors and fool-proof sensor head orientation indicator | WISH (W=3) | D | CC-06 | Minimize installation error by untrained personnel | Arrow or marking indicating "NORTH" alignment reference |

### 4.9 Production (PRD)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| PRD-001 | Vietnamese local content by value | >=60% of BOM (target 70%) | MUST | A | — | Vietnamese defense policy; CLAUDE.md requirement | Local: PCB fabrication, PCB assembly, enclosure machining, battery pack assembly, cables, final assembly, test |
| PRD-002 | Import content by value | <=40% of BOM | MUST | A | PRD-001 | Complement of local content | Import: MEMS microphones, FPGA/DSP, radio module, GPS module, ARM processor |
| PRD-003 | PCB assembly standard | IPC-A-610 Class 2 (Dedicated Service) minimum | MUST | I | — | Defense electronics production standard | Vietnamese PCB assembly houses can achieve Class 2; Class 3 wish for critical boards |
| PRD-004 | Production lot size — Phase 1 target | >=50 nodes for cost target achievement | MUST | A | — | Cost model assumes lot size 50+ for $2-5K unit cost | Smaller lots = higher unit cost; 50 is minimum economic quantity |
| PRD-005 | Assembly skill level | Technician-level assembly (not PhD engineer); <=2 weeks training | MUST | D | — | Vietnamese workforce availability | Assembly procedures documented; visual work instructions; go/no-go fixtures |
| PRD-006 | Production rate — Year 1 | >=10 nodes/month (120 nodes/year capacity) | WISH (W=4) | A | — | Derived from market demand estimate and ramp-up schedule | Hand assembly acceptable Year 1; semi-automated Year 2 |
| PRD-007 | First-pass yield target | >=95% at functional test | WISH (W=4) | A | — | Production quality target | Automated functional test at end-of-line; rework for remaining 5% |
| PRD-008 | Test automation — end-of-line | Automated functional test: self-test + simulated acoustic event + radio link + GPS lock | WISH (W=3) | D | — | Production efficiency; consistent quality | Test fixture with acoustic source at known angle; verify DoA within spec |
| PRD-009 | Design for automated assembly (DFA) | >=80% of PCB components placeable by pick-and-place machine | WISH (W=3) | A | — | Production scalability | Minimize through-hole components; use standard SMD packages (0402, 0603, QFP, BGA) |

### 4.10 Quality (QUA)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| QUA-001 | Probability of detection (Pd) — Group 1 | >=90% at >=300m for DJI Mavic 3 class quadcopter (reference conditions) | MUST | T | O-22 (18.0), O-29 (17.5) | #2 and #3 EXTREME ODI outcomes; phase0 v8.0 | Reference: wind <=15 km/h, ambient <=50 dB(A), no rain, target altitude 50-150m AGL |
| QUA-002 | Probability of detection (Pd) — Group 2-3 | >=90% at >=1 km for fixed-wing UAV (reference conditions) | MUST | T | O-23 (15.5) | Phase0 v8.0; RE: Fencepost (5-7 km Group 3) | Larger targets = louder; physics favors detection at longer range |
| QUA-003 | False alarm rate (Pfa) | <=1 false alarm per hour in operational conditions | MUST | T | O-28 (15.5), ES-04 | #7 EXTREME ODI; NATO operational acceptability threshold | Operational: wind <=40 km/h, rain <=moderate, typical background (birds, insects, vehicles) |
| QUA-004 | Classification accuracy | >=80% correct classification among >=3 drone types at <=300m (reference conditions) | MUST | T | O-27 (15.0), CC-02 (16.0) | #10 EXTREME ODI; phase0 v8.0 | Drone types: quadcopter, fixed-wing, multi-rotor (hexacopter+); reference conditions per QUA-001 |
| QUA-005 | Alert latency — detection to C2 display | <=3 seconds from target entering detection zone to alert on operator display | MUST | T | O-24 (15.0) | #9 EXTREME ODI; phase0 v8.0 | Includes: acoustic processing + classification + mesh transmission + C2 rendering |
| QUA-006 | Simultaneous target tracking | >=3 independent targets within coverage volume | MUST | T | O-33 (15.0), O-40 (14.0) | #11 EXTREME ODI; drone swarm scenario | Each target: separate bearing, range estimate, classification, track ID |
| QUA-007 | Track continuity | >=90% track continuity (no gap >3 seconds) for tracked target within detection range | MUST | T | O-37 (14.5), O-42 (15.0) | Track loss = loss of situational awareness; unacceptable for active threat | Track maintained through short acoustic shadow or maneuver; re-acquire within 3s |
| QUA-008 | Angular accuracy — standalone | <=3 deg azimuth, <=5 deg elevation RMS error (reference conditions) | MUST | T | O-25 (13.0) | Phase0 v8.0; RE: Squarehead (<10 deg), BeephoniX (1-2 deg) | Reference conditions per QUA-001; validated via known-position drone flight test |
| QUA-009 | Angular accuracy — networked | <=0.5 deg azimuth RMS (>=3 nodes, >=100m baseline) | WISH (W=5) | T | O-25, O-26 | Phase0 v8.0; RE: Microflown V-AMMS (0.2 deg) | Triangulation from multiple node bearings; requires accurate GPS positions |
| QUA-010 | Confidence calibration | Reported Bayesian confidence % correlates with actual accuracy >=80% of the time | WISH (W=5) | T | CC-02 (16.0) | Commander needs trustworthy confidence score for engagement decisions | If system reports 90% confidence, actual correct classification >=90% in >=80% of cases |
| QUA-011 | MTBF | >=5,000 hours continuous operation (target 8,000 hours) | WISH (W=4) | A | O-19, O-21 | MIL-HDBK-217F prediction methodology | ~2 years at 8h/day continuous; or ~7 months 24/7 unattended |
| QUA-012 | Reference conditions definition | Ambient <=50 dB(A), wind <=15 km/h, temp 15-35 deg C, humidity 30-80% RH, no precipitation, flat open terrain | MUST | A | QUA-001 through QUA-008 | Standardized test conditions for all performance claims | Published in product datasheet; operational degradation curves for non-reference conditions |

### 4.11 Assembly (ASM)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| ASM-001 | Tool-free sensor head mounting | Quick-release mechanism for sensor head to tripod/mast; <=30 seconds | MUST | D | O-06, CC-05, CC-06 | 1-person rapid deployment requirement | Twist-lock, bayonet, or lever clamp; keyed for orientation |
| ASM-002 | Weatherproof connectors | Mil-spec circular (MIL-DTL-38999) or M12 IP67 rated | MUST | I | MAT-002, O-30 | IP67 system requirement; field reliability | Push-pull or screw-lock; <=5 connector types across entire system |
| ASM-003 | Field-replaceable battery module | Battery module removable/insertable without tools; IP67 maintained when installed | MUST | D | ENE-007, CC-12 | Operational continuity; field maintenance | Sealed battery compartment with quick-release latch |
| ASM-004 | Cable length options | 2m, 5m, 10m pre-terminated power/data cables | WISH (W=4) | I | O-06 | Installation flexibility for different deployment scenarios | Standard connectors at both ends; field-terminable wish |
| ASM-005 | Tripod interface | Standard 1/4"-20 threaded insert + quick-release plate compatible with COTS survey/camera tripods | WISH (W=4) | I | GEO-009, O-06 | Minimize proprietary accessories; COTS tripod availability | Also accept NATO accessory rail for military mounts |
| ASM-006 | No field calibration required | System self-calibrates at power-on; no manual calibration at deployment site | WISH (W=5) | T | O-14, O-10 | Minimize deployment skill requirement; RE: goal of zero-config deployment | Internal temperature sensor for speed-of-sound correction; GNSS for position |
| ASM-007 | Modular radio replacement | Radio module field-replaceable in <=15 minutes with basic tools | WISH (W=3) | D | CC-11, CC-12 | Future radio upgrade path; field maintenance | Socketed radio module with standard interface |

### 4.12 Transport (TRN)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| TRN-001 | Man-portable — single node | Full node (sensor + battery + tripod + cables) <=5 kg; with transit case <=8 kg | MUST | I | O-08 (12.5), O-07 | Phase0 v8.0; 1-person carry | Backpackable by single soldier over 1 km |
| TRN-002 | Transit case | IP67 Pelican-style case; stackable; pressure equalization valve; for 1-4 nodes per case | MUST | I | O-06 | Military transport requirement; protects during vehicle/air transit | Foam insert custom-cut for node components |
| TRN-003 | Vehicle transport | Rated for transport on military truck (unpaved road per MIL-STD-810H Method 514.8) | MUST | T | FOR-003 | Vietnamese military vehicle fleet: UAZ, Ural, HMMWV-class | Secured in transit case on vehicle bed |
| TRN-004 | Vehicle-mounted operation | Mount bracket for HMMWV/M113/Vietnamese military vehicle roof or side rail | WISH (W=4) | D | KIN-006 | Mobile force protection; convoy C-UAS | Vehicle-specific mounting kits; vibration isolation mount |
| TRN-005 | Air transport | Battery meets IATA DG requirements; <=100 Wh per battery module or UN 38.3 certified >100 Wh | WISH (W=3) | I | SAF-002 | Expeditionary deployment via helicopter or transport aircraft | LiFePO4 preferred for air transport safety |
| TRN-006 | Packaging volume per node | <=0.05 m3 packed in transit case (target 0.03 m3) | WISH (W=3) | I | — | Storage and shipping efficiency | 20 nodes fit in standard 20ft container |

### 4.13 Operation (OPR)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| OPR-001 | Operating temperature | -10 deg C to +55 deg C continuous | MUST | T | O-30 | MIL-STD-810H Method 501.7 (High Temp) / 502.7 (Low Temp) | Vietnamese climate: 35-45 deg C common; +55 deg C peak sun-exposed metal |
| OPR-002 | Storage temperature | -40 deg C to +70 deg C | MUST | T | O-30 | MIL-STD-810H; non-climate-controlled warehouse storage in Vietnam | Battery may require separate storage temperature range |
| OPR-003 | Humidity | Operate at 95% RH at 40 deg C continuously per MIL-STD-810H Method 507.6 | MUST | T | O-30, O-32 | Vietnamese monsoon: 80-95% RH sustained for months | Conformal coating + IP67 sealing critical |
| OPR-004 | Rain resistance | Operate in rainfall up to 4 inches/hour (100 mm/hr) per MIL-STD-810H Method 506.6 | MUST | T | O-32 | Tropical monsoon operation; system cannot shut down for rain | Detection performance may degrade in heavy rain; degradation curve to be characterized |
| OPR-005 | Salt fog | Per MIL-STD-810H Method 509.7 (5% NaCl) | MUST | T | O-30, MAT-004 | Coastal military installations | Combined with MAT-004 corrosion resistance |
| OPR-006 | Sand and dust | Per MIL-STD-810H Method 510.7 (blowing dust, fine sand) | MUST | T | O-30 | Vietnamese terrain: sandy coastal, laterite inland | IP6X dust-tight rating; mesh wind screen must not clog |
| OPR-007 | Solar radiation | Per MIL-STD-810H Method 505.7, 1120 W/m2 | MUST | T | O-30, MAT-003 | Tropical direct sunlight; component derating | Internal temperature must remain within component limits |
| OPR-008 | Immersion | IP67: 1m depth for 30 minutes per IEC 60529 | MUST | T | O-32 | Monsoon flooding; accidental submersion during deployment | All seals, connectors, battery compartment must maintain seal |
| OPR-009 | Wind operation — full performance | Full detection performance at wind <=25 km/h | WISH (W=5) | T | O-31 | Moderate wind is common; must not degrade detection | Wind noise reduction via beamforming spatial filtering + wind screen |
| OPR-010 | Wind operation — degraded | Degraded but operational at wind 25-70 km/h; graceful performance reduction | WISH (W=4) | T | O-31 | High wind (tropical storm); system remains active with reduced range/accuracy | Publish degradation curve: range vs. wind speed |
| OPR-011 | Altitude | 0-3000m ASL operating | WISH (W=3) | T | O-30 | Vietnamese highland deployments (Central Highlands, border mountains up to ~2000m) | Speed of sound correction; air density affects acoustic propagation |
| OPR-012 | Boot time — power-on to operational | <=60 seconds from power-on to first detection capability | MUST | T | O-13 | Operational urgency; RE: rapid deployment scenario | Includes self-test, calibration, mesh network join, GPS fix |

### 4.14 Maintenance (MNT)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| MNT-001 | Mean Time To Repair (MTTR) | <=30 minutes for field-replaceable module swap | MUST | D | CC-12, CC-11 | Operational availability requirement | Swap: battery, radio module, GPS module, entire sensor head |
| MNT-002 | Built-in Test (BIT) | Automatic health check at power-on and periodic (every 1 hour during operation) | MUST | T | O-19, O-21, O-15 | RE: all competitors provide BIT | Check: microphone array health, processor, memory, radio link, GPS, battery, temperature |
| MNT-003 | Calibration interval | >=12 months between factory recalibrations | MUST | T | O-14 | Operational cost reduction; RE: minimize field calibration need | Auto-calibration (temperature, gain) on each power-on reduces drift impact |
| MNT-004 | Field-replaceable modules | Battery, radio module, GPS module, SD card; no soldering or special tools | MUST | D | CC-11, CC-12 | Vietnamese field maintenance capability (technician level) | Modular architecture with socketed/connectorized subassemblies |
| MNT-005 | No special test equipment for field maintenance | Standard multimeter and laptop sufficient for field-level diagnostics | MUST | D | CC-11 | Vietnamese military maintenance infrastructure | BIT provides diagnostic codes; laptop connects via USB-C for detailed logs |
| MNT-006 | Remote diagnostics via mesh network | Health status of all nodes visible from C2 application; alerts on degradation | WISH (W=5) | D | O-19, O-21, CC-09 | Reduces need to physically visit each node for health check | Dashboard: battery %, signal quality, microphone health, temperature, uptime |
| MNT-007 | Spare parts availability in Vietnam | Top 5 consumable parts stocked in-country; <=14-day lead time | WISH (W=4) | D | CC-11, PRD-001 | Reduce logistics dependency on foreign supply | Consumables: battery, wind screen, SD card, radio module, cable assemblies |
| MNT-008 | Firmware/ML model update — OTA | Over-the-air update via mesh network or direct WiFi; encrypted and signed | WISH (W=5) | D | O-47 (16.0), O-44 (15.5), SAF-005 | #5 and #8 EXTREME ODI outcomes; continuous ML improvement | Dual-bank firmware (A/B) for rollback safety; ML model hot-swap without reboot |
| MNT-009 | Environmental monitoring — internal sensors | Temperature, humidity, battery voltage/current/health; logged and reported via BIT | WISH (W=4) | T | O-19 | Predictive maintenance; tropical environment monitoring | Alerts when internal conditions approach limits (e.g., temp >60 deg C) |
| MNT-010 | Predictive maintenance — battery health | Battery state-of-health estimation; predict remaining useful life; alert at <=20% capacity | WISH (W=3) | T | O-19 | Avoid unexpected battery failure in field | Coulomb counting + impedance estimation; cycle count tracking |

### 4.15 Costs (CST)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| CST-001 | Unit cost per node — selling price | $2,000-5,000 per node at lot size 50+ | MUST | A | Phase0 v8.0, competitive landscape | White space: no competitor at this price point with acoustic + ML | BeephoniX ~$10K, Squarehead ~$15-50K, DroneShield $200K+ system |
| CST-002 | BOM cost per node | $500-1,500 per node at lot size 50+ | MUST | A | Phase0 cost structure estimate | 60-75% gross margin (defense standard) | Phase0 estimate: $309-1,392; target middle of range |
| CST-003 | Development cost (NRE) — to MVP prototype | <=$500,000 total (target $300,000) | MUST | A | — | Budget constraint; includes HW design, FW development, ML training, tooling | Prototype (10 nodes) + field test + documentation |
| CST-004 | MIL-STD-810H testing cost | Budget $50,000-100,000 for environmental qualification | MUST | A | — | Third-party test lab (Singapore, Australia, or US) | TBD-006 test partner selection |
| CST-005 | Cost vs import ratio | <=50% of nearest affordable competitor (BeephoniX ~$10K) | MUST | A | Phase0 competitive positioning | $5K VN-CUAS vs $10K BeephoniX = 50% | Cost advantage is primary competitive differentiator |
| CST-006 | 10-year lifecycle cost per node | <=$10,000 (acquisition + 10-year maintenance + ML subscription) | WISH (W=4) | A | — | Total cost of ownership competitiveness | Import system LCC: $30K-100K+ per node over 10 years |
| CST-007 | Vietnamese local content value | >=60% of BOM cost (=$300-900 per node) | WISH (W=5) | A | PRD-001 | Defense policy alignment; enables government procurement preference | Local: enclosure ($50-150), PCB+asm ($100-200), battery ($50-100), cables ($20-50), integration ($100-200) |
| CST-008 | Software/ML license revenue | $5,000-20,000/year per site (10-50 nodes) for ML model updates and C2 software | WISH (W=3) | A | O-47, O-44 | Recurring revenue model; funds continuous ML improvement | Optional for Vietnamese military; standard for export customers |

### 4.16 Schedule (SCH)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| SCH-001 | Phase 1-2 design completion | 6-9 months from Phase 1 start (Q3 2026) | MUST | A | — | Development plan | Requirements (3 mo) + Conceptual design (3-6 mo) |
| SCH-002 | MVP prototype | 12-15 months from Phase 1 start (Q1-Q2 2027) | MUST | A | — | Development plan | 10 functional nodes + C2 software + field test at Vietnamese military site |
| SCH-003 | V1.0 production qualification | 18-24 months from Phase 1 start (Q3 2027 - Q1 2028) | MUST | A | — | Development plan | MIL-STD-810H testing complete; production BOM finalized; supply chain qualified |
| SCH-004 | First batch delivery | 50 nodes within 6 months of production qualification | MUST | A | PRD-004 | Customer commitment timeline | First batch for Vietnamese military evaluation/deployment |
| SCH-005 | ML V2.0 — spectrogram-to-CNN classification | 24-30 months from Phase 1 start (Q1-Q3 2028) | WISH (W=4) | A | O-47, O-44 | ML development timeline; requires field training data from V1.0 deployments | V1.0 ships with eigenvector baseline; V2.0 adds CNN ML layer via OTA update |
| SCH-006 | Multi-mission firmware (C-RAM, gunshot) | 30-36 months from Phase 1 start (Q3 2028 - Q1 2029) | WISH (W=3) | A | — | Firmware-defined multi-mission roadmap | Same hardware; new signal processing firmware per mission type |

---

## 5. STANDARDS COMPLIANCE MATRIX

| Standard | Title | Applicable Sections | Requirements Mapped | Compliance Approach |
|----------|-------|---------------------|---------------------|---------------------|
| **MIL-STD-810H** | Environmental Engineering Considerations | 501.7 (High Temp), 502.7 (Low Temp), 505.7 (Solar Radiation), 506.6 (Rain), 507.6 (Humidity), 509.7 (Salt Fog), 510.7 (Sand/Dust), 514.8 (Vibration), 516.8 (Shock) | OPR-001 to OPR-008, FOR-001 to FOR-004, MAT-003, MAT-004 | Full test program per applicable methods; TBD-006 test partner |
| **MIL-STD-461G** | EMI/EMC Requirements | RE102 (Radiated Emissions) | SAF-001 | EMCON validation in passive mode; EMC shielding design |
| **MIL-STD-882E** | System Safety | Hazard analysis, risk assessment (4.1-4.5) | SAF-003, SAF-008 | FMEA + Fault Tree Analysis before prototype test |
| **MIL-STD-1275E** | Characteristics of 28V DC Input Power | Vehicle power compatibility | ENE-006 | Input power conditioning and protection |
| **IEC 60529** | Ingress Protection | IP67 (dust-tight + 1m immersion) | OPR-006, OPR-008 | Test per IEC 60529 procedures |
| **UN 38.3** | Lithium Battery Transport | T1-T8 tests | SAF-002, TRN-005 | Battery supplier certification required |
| **IPC-CC-830C** | Conformal Coating | Type AR or UR | MAT-005 | Coating process + inspection per IPC standard |
| **IPC-A-610** | Acceptability of Electronic Assemblies | Class 2 (Dedicated Service) | PRD-003 | Workmanship inspection at production |
| **SAPIENT** | Sensing for Asset Protection with Integrated Electronic Networked Technology | v3.0+ interface spec | SIG-012 | SAPIENT message format compliance; NATO interoperability |
| **TAK** | Team Awareness Kit | Plugin API specification | SIG-011 | ATAK/WinTAK plugin development; CoT message format |
| **TCVN** | Vietnamese National Standards | TBD-002: electrical, environmental, labeling, EMC | OPR-001, ENE-006, ERG-006 | Compliance review pending TCVN applicability mapping |

---

## 6. ODI TRACEABILITY MATRIX (Top 25 Opportunities)

| Rank | ODI Outcome | Opp Score | Category | Requirements Mapped | Coverage |
|------|------------|-----------|----------|---------------------|----------|
| 1 | O-35: Detect RF-silent/autonomous drones | 18.5 | EXTREME | SAF-001 (zero RF), SIG-001-006 (passive acoustic), QUA-001-002 (Pd) | Full |
| 2 | O-22: Detect Group 1 quadcopters | 18.0 | EXTREME | QUA-001, SIG-002-005, GEO-002-005 (array), KIN-001 | Full |
| 3 | O-29: Minimize missed detection rate | 17.5 | EXTREME | QUA-001, QUA-002, QUA-007, SAF-003 (graceful degradation) | Full |
| 4 | CC-02: Commander confidence in classification | 16.0 | EXTREME | QUA-004, QUA-010, SIG-010, ERG-005 | Full |
| 5 | O-47: Adapt to evolving drone tactics | 16.0 | EXTREME | MNT-008, SIG-018 (ML processor), SIG-020 (data logging), SCH-005 | Full |
| 6 | O-23: Detect Group 2-3 fixed-wing UAVs | 15.5 | EXTREME | QUA-002, SIG-002 (50-20k Hz), SIG-006 (DoA) | Full |
| 7 | O-28: Minimize false alarm rate | 15.5 | EXTREME | QUA-003, QUA-004, QUA-010 (confidence calibration) | Full |
| 8 | O-44: Add new drone signatures | 15.5 | EXTREME | MNT-008 (OTA update), SIG-020 (data capture), SIG-018 (ML edge) | Full |
| 9 | O-24: Minimize time to alert | 15.0 | EXTREME | QUA-005, SIG-019 (DSP), SIG-015 (mesh), OPR-012 (boot time) | Full |
| 10 | O-27: Classification accuracy | 15.0 | EXTREME | QUA-004, SIG-018, SIG-010, QUA-010 | Full |
| 11 | O-33: Multi-drone detection | 15.0 | EXTREME | QUA-006, SIG-006 (DoA multi-source), KIN-004 (track update) | Full |
| 12 | O-42: Minimize likelihood of losing track | 15.0 | EXTREME | QUA-007, KIN-004, SIG-015 (mesh handoff) | Full |
| 13 | O-52: Maximize data retention for ML training | 15.0 | EXTREME | SIG-020, SIG-017 (USB data download) | Full |
| 14 | CC-03: Minimize friendly drone engagement | 15.0 | EXTREME | QUA-004, QUA-010, SIG-010 (classification output) | Full |
| 15 | O-37: Track continuity | 14.5 | HIGH | QUA-007, KIN-004, SIG-015 (mesh) | Full |
| 16 | CC-15: Identify new drone types from recordings | 14.5 | HIGH | SIG-020 (recording), SIG-017 (data export) | Full |
| 17 | O-04: Update threat definitions easily | 14.0 | HIGH | MNT-008, SIG-018 (ML edge) | Full |
| 18 | O-09: Coverage area per node | 14.0 | HIGH | QUA-001-002 (range), KIN-001 (hemispheric), GEO-002 (aperture) | Full |
| 19 | O-26: Range estimation accuracy | 14.0 | HIGH | SIG-009 (triangulation), SIG-014 (mesh range), SIG-016 (GPS) | Full |
| 20 | O-30: Detection in high ambient noise | 14.0 | HIGH | SIG-003 (SNR), SIG-006 (beamforming), MAT-006 (wind screen) | Full |
| 21 | O-31: Detection in windy conditions | 14.0 | HIGH | MAT-006, OPR-009, OPR-010, FOR-005 | Full |
| 22 | O-40: Multi-track discrimination | 14.0 | HIGH | QUA-006, SIG-006, KIN-004 | Full |
| 23 | CC-18: Track format compatibility with other sensors | 14.0 | HIGH | SIG-010-012, SIG-016 (GPS position) | Full |
| 24 | CC-20: Acoustic as cue for other sensors | 14.0 | HIGH | SIG-010 (bearing + range output), SIG-011-012 (C2 integration) | Full |
| 25 | O-18: Confidence in full coverage | 13.5 | HIGH | MNT-002 (BIT), MNT-006 (remote diagnostics), KIN-001 (hemispheric) | Full |

**Coverage: 25/25 FULL — all top 25 ODI outcomes have corresponding hardware requirements.**

---

## 7. VERIFICATION PLAN SUMMARY

| Verification Type | Count | Estimated Cost | Duration | Notes |
|-------------------|-------|----------------|----------|-------|
| Analysis (A) | 24 | $15,000 | 3 weeks | BOM cost, MTBF prediction, local content, FMEA, thermal analysis |
| Inspection (I) | 35 | $5,000 | 2 weeks | Dimensions, weight, materials, connectors, labels, workmanship |
| Test (T) | 68 | $80,000 | 12 weeks | MIL-STD-810H environmental suite, IP67, EMC, acoustic performance, detection Pd/Pfa, classification accuracy |
| Demonstration (D) | 26 | $20,000 | 4 weeks | Field deployment trials, user operation, 1-person setup, maintenance procedures, C2 integration |
| **TOTAL** | **153** | **$120,000** | **21 weeks** | Parallel execution reduces calendar time to ~14 weeks; MIL-STD-810H is longest single-thread |

### Key Test Programs

| Test Program | Requirements | Estimated Cost | Duration | Facility |
|--------------|-------------|----------------|----------|----------|
| MIL-STD-810H environmental | FOR-001 to FOR-004, OPR-001 to OPR-008 | $50-100K | 6-8 weeks | TBD-006 external lab (Singapore/Australia/US) |
| Acoustic performance (Pd, Pfa, DoA, classification) | QUA-001 to QUA-010, SIG-006, SIG-007 | $15-20K | 4 weeks | Vietnamese military range + controlled test site |
| IP67 ingress protection | OPR-006, OPR-008, MAT-002 | $3-5K | 1 week | Local test facility or self-test |
| EMC (MIL-STD-461G RE102 passive mode) | SAF-001 | $5-10K | 1 week | EMC test chamber |
| Cybersecurity (encryption, secure boot) | SAF-004, SAF-005 | $5-10K | 2 weeks | Internal + external pen test |
| Field deployment trials | ERG-001-003, QUA-005, OPR-012 | $10-15K | 2 weeks | Vietnamese military site |

---

## 8. CONFLICT ANALYSIS

| Conflict | Requirements | Resolution |
|----------|-------------|------------|
| **Weight vs Battery Life** | GEO-006 (<=2 kg head), GEO-007 (<=5 kg node), ENE-003 (>=240 Wh) | At 160 Wh/kg (Li-ion), 240 Wh = 1.5 kg battery. Sensor head 2 kg + battery 1.5 kg + radio/GPS/cables 1 kg = 4.5 kg. Achievable at 5 kg total. LiFePO4 (90-120 Wh/kg) requires 2.0-2.7 kg -- tight but feasible at 5 kg. |
| **Array Size vs Weight** | GEO-004 (128-256 mics), GEO-006 (<=2 kg head) | 128 MEMS at ~0.5g each = 64g for sensors. PCB, enclosure, electronics dominate weight. 256 mics feasible if PCB area managed. BeephoniX achieves 151 mics at 950g. |
| **Cost vs Performance** | CST-002 ($500-1500 BOM) vs QUA-001 (>=90% Pd at 300m) vs QUA-004 (>=80% classification) | Commodity MEMS ($0.50-2 each) + COTS FPGA ($20-100) + ARM SoC ($10-30) = achievable. ML classification from software, not expensive hardware. Dual-classification (eigenvector + CNN) maximizes accuracy per dollar. |
| **Power vs ML Processing** | ENE-001 (<=10W) vs SIG-018 (ARM Cortex-A for ML) vs SIG-019 (FPGA for beamforming) | FPGA + ARM total ~5-8W typical. Cortex-A53 at 1.5 GHz ~2W; low-power FPGA (Lattice) ~1-3W; ADC/analog ~2W. 10W total achievable. Sleep/wake mode (ENE-009) reduces average further. |
| **Mesh Radio Range vs Power** | SIG-014 (>=500m LoS) vs ENE-002 (<=15W total) | 900 MHz ISM at 1W output = 500-1000m LoS; radio module consumes 2-3W active. Within 15W budget. Duty-cycle radio transmit for further power savings. |
| **Detection Range vs Array Size** | QUA-001 (>=300m Pd Group 1) vs GEO-002 (200-400mm diameter) | 300m detection range depends on: SNR, array gain (N_mics), beamforming gain, ambient noise. 128-element array provides ~21 dB array gain. With 65 dB SNR mics, effective SNR at 300m is sufficient for DJI Mavic class drone (72 dB at 1m source level). Physics analysis confirms feasibility. |
| **EMCON vs Mesh Networking** | SAF-001 (zero RF in EMCON) vs SIG-013-015 (mesh radio) | EMCON mode disables radio; node operates standalone with on-node classification and data logging. Alert stored and transmitted when EMCON lifted. Configurable per node. |

**Unresolved conflicts: NONE** — all conflicts have feasible engineering resolutions identified.

---

## 9. OPEN ISSUES & TBD

| Issue ID | Description | Owner | Target Date | Status | Impact |
|----------|-------------|-------|-------------|--------|--------|
| TBD-001 | Codename for VN-CUAS product | User decision | Phase 1 | Open | Marketing/identity; no technical impact |
| TBD-002 | TCVN (Vietnamese standards) applicability mapping | Standards researcher | Q2 2026 | Open | May add requirements to OPR, ENE, SAF categories |
| TBD-003 | Target production volume for first batch | Business decision | Q2 2026 | Open | Drives CST-001/002 cost targets and PRD-004 lot size |
| TBD-004 | Software requirements specification detail | Software lead | Phase 1.5 | Open | C2 app, ML pipeline, data management — large scope; separate SRS document needed |
| TBD-005 | ML training data acquisition strategy | ML engineer | Q2 2026 | Open | Critical path for QUA-004 classification accuracy; need drone recordings |
| TBD-006 | MIL-STD-810H testing partner selection | Programme manager | Q2 2026 | Open | Cost and schedule for CST-004; Singapore/Australia/US options |
| TBD-007 | Specific MEMS microphone selection | Hardware engineer | Phase 2 | Open | Knowles SPH0645LM4H, InvenSense ICS-40730, or equivalent; affects SIG-001-003 |
| TBD-008 | SAPIENT version and TAK plugin specification | Systems engineer | Phase 1.5 | Open | Interface definition for SIG-011, SIG-012 |
| TBD-009 | Vietnamese military operational scenario prioritization | Field survey | Q2 2026 | Open | FOB vs base vs border vs convoy — drives deployment configuration |
| TBD-010 | ODI field survey validation (>=40 Vietnamese military operators) | Field survey team | Q3 2026 | Open | Validates importance/satisfaction scores; 7 LOW-confidence outcomes need priority |
| TBD-011 | FPGA vs dedicated DSP trade study for beamforming | Hardware engineer | Phase 2 | Open | Affects SIG-019, ENE-001, CST-002 |
| TBD-012 | Mesh radio protocol selection (LoRa, Zigbee, custom 900 MHz) | RF engineer | Phase 2 | Open | Affects SIG-013-015, ENE-002, CST-002 |

---

## 10. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | Engineering Design System | -- | 2026-02-11 |
| Reviewer | -- | -- | -- |
| Approver | -- | -- | -- |

---

## Cross-References

- [[odi_analysis.md]] - Phase 0 ODI Rev B.0 (76 outcomes, 52 primary + 20 CC + 4 ES)
- [[phase0_synthesis.md]] - Phase 0 synthesis and gate review document
- [[competitive_landscape_analysis.md]] - 8-system competitive landscape analysis
- [[RE_squarehead_discovair_g2plus.md]] - RE: Squarehead G2+ (128 MEMS, MIL-STD-810H)
- [[RE_beephonix_m2.md]] - RE: BeephoniX M2 (151 MEMS, 950g, 1-2 deg accuracy)
- [[RE_fraunhofer_idmt_acoustic_drone_detection.md]] - RE: Fraunhofer IDMT (algorithm-centric, NLOS)
- [[RE_droneshield_dronesentry.md]] - RE: DroneShield DroneSentry (multi-sensor, $200K+)
- [[RE_dedrone_dronetracker.md]] - RE: Dedrone DroneTracker (RF-centric, DroneDNA 600+)
- [[RE_mind_foundry_sentry.md]] - RE: Mind Foundry SENTRY (AI-first, Bayesian, ATAK)
- [[RE_ga_ems_fencepost.md]] - RE: GA-EMS Fencepost (eigenvector, seismic, 5-7km)
- [[RE_microflown_avisa_skysentry.md]] - RE: Microflown AVISA SKYSENTRY (AVS, <2W, multi-mission)
- [[standards_mapping.md]] - Detailed standards compliance (to be created Phase 1)
- [[stakeholder_analysis.md]] - Stakeholder analysis (to be created Phase 1)
