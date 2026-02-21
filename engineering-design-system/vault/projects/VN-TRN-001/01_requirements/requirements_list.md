---
project: VN-TRN-001
phase: 1
type: requirements-list
version: 1.0
created: 2026-02-06
status: draft
---

# REQUIREMENTS LIST
## VN-TRN-001: Vietnamese LOMAH Electronic Scoring System
### Version: 1.0 | Date: 2026-02-06

---

## 1. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-06 | Engineering Team | Initial release from ODI analysis + 8 RE benchmarks |

---

## 2. PROJECT OVERVIEW

| Item | Detail |
|------|--------|
| **Product Name** | VN-LOMAH Electronic Scoring System |
| **Project Code** | VN-TRN-001 |
| **Customer** | Vietnamese Ministry of National Defense (MoND) / Ministry of Public Security (MoPS) |
| **End Users** | Range Officer/NCO, Instructor, Shooter, Maintenance Technician |
| **Target Cost** | ≤$500/lane (hardware), ≤$25,000/range (10-lane complete system) |
| **ODI Reference** | [[00_odi_analysis]] |
| **RE References** | 8 competitor analyses in [[VN-LOMAH]] folder |

---

## 3. REQUIREMENTS SUMMARY

| # | Category | MUST (D) | WISH (W) | Total | Quantified % |
|---|----------|----------|----------|-------|-------------|
| 1 | Geometry | 5 | 4 | 9 | 89% |
| 2 | Kinematics | 3 | 2 | 5 | 100% |
| 3 | Forces | 4 | 2 | 6 | 83% |
| 4 | Energy | 5 | 3 | 8 | 88% |
| 5 | Material | 4 | 3 | 7 | 86% |
| 6 | Signals | 7 | 4 | 11 | 91% |
| 7 | Safety | 5 | 1 | 6 | 83% |
| 8 | Ergonomics | 3 | 3 | 6 | 83% |
| 9 | Production | 4 | 2 | 6 | 83% |
| 10 | Quality | 5 | 2 | 7 | 86% |
| 11 | Assembly | 3 | 2 | 5 | 80% |
| 12 | Transport | 3 | 2 | 5 | 80% |
| 13 | Operation | 6 | 3 | 9 | 89% |
| 14 | Maintenance | 4 | 3 | 7 | 86% |
| 15 | Costs | 4 | 2 | 6 | 83% |
| 16 | Schedule | 3 | 1 | 4 | 75% |
| | **TOTAL** | **68** | **39** | **107** | **85%** |

---

## 4. DETAILED REQUIREMENTS

### 4.1 Geometry (Kích thước & Hình học)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| GEO-01 | Beam Sensor Unit (BSU) length | ≤1,300mm | D | I | Polytronic H-Bar (1200mm), Saab BSU | O-15 |
| GEO-02 | BSU height | ≤200mm | W(4) | I | Competitor average | O-15 |
| GEO-03 | BSU width/depth | ≤150mm | W(3) | I | Minimize target area obstruction | — |
| GEO-04 | BSU weight | ≤12kg (target 8kg) | D | I | Polytronic ~10kg; portability | O-15 |
| GEO-05 | Target Processor Unit (TPU) enclosure | ≤300×200×150mm | W(3) | I | Compact field unit | — |
| GEO-06 | TPU weight | ≤5kg | D | I | Field-portable requirement | O-15 |
| GEO-07 | Detection zone - infantry | ≥3.0m (H) × 2.5m (W) | D | T | NATO standard silhouette; InVeris/Saab benchmark | O-21 |
| GEO-08 | Detection zone - armor | ≥4.0m (H) × 3.0m (W) | W(4) | T | Extended config; InVeris Armor LOMAH | O-08 |
| GEO-09 | Sensor bar mounting compatibility | Standard NATO target frames + Vietnamese frames | D | D | Cross-platform requirement | O-09 |

### 4.2 Kinematics (Động học)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| KIN-01 | Minimum detectable projectile velocity | ≤Mach 1.3 (440 m/s at 20°C) | D | T | Saab/TTS benchmark; supersonic TDOA physics | O-08 |
| KIN-02 | Maximum detectable projectile velocity | ≥Mach 3.5 (~1,190 m/s) | D | T | 12.7mm AP muzzle velocity consideration | O-08 |
| KIN-03 | Detection azimuth angle | ≥±20° from perpendicular | D | T | Saab/TTS specification | O-19 |
| KIN-04 | Detection elevation angle | ≥±5° from perpendicular | D | T | Saab/TTS specification | O-19 |
| KIN-05 | Shot-to-display latency | ≤500ms (target ≤200ms) | W(4) | T | Real-time feedback; InVeris benchmark | O-22 |

### 4.3 Forces (Lực & Tải trọng)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| FRC-01 | Shockwave overpressure tolerance | ≥160 dB SPL without sensor damage | D | T | Supersonic shockwave N-wave peak pressure | O-30 |
| FRC-02 | Ballistic impact survival (BSU) | Withstand indirect hits from 5.56mm fragments at 300m | D | T | Range safety; InVeris/Saab ballistic protection | O-30 |
| FRC-03 | Mechanical shock (transport) | 40g, 11ms half-sine per MIL-STD-810H Method 516.8 | D | T | Military transport environment | O-46 |
| FRC-04 | Vibration (transport) | MIL-STD-810H Method 514.8, Cat. 4 (truck) | D | T | Wheeled vehicle transport | O-46 |
| FRC-05 | Wind load on BSU | Operational up to 72 km/h (20 m/s) wind | W(4) | T | Polytronic BRP benchmark | O-26 |
| FRC-06 | Drop height (TPU, packed) | 1.0m drop onto concrete without damage | W(3) | T | Field handling robustness | O-46 |

### 4.4 Energy (Năng lượng)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| ENG-01 | Primary power input | 12 VDC nominal (10.5-15V range) | D | T | Military vehicle battery standard; Saab/InVeris | — |
| ENG-02 | Mains power input | 110/230 VAC, 50/60 Hz (auto-switching) | D | T | Range infrastructure power; dual-voltage | — |
| ENG-03 | Battery operation runtime | ≥10 hours continuous at 25°C | D | T | InVeris Portable LOMAH benchmark; full training day | O-34 |
| ENG-04 | Battery type | Li-ion rechargeable, field-replaceable | D | I | Modern standard; InVeris 20V Li-ion reference | O-49 |
| ENG-05 | System power consumption (per lane) | ≤15W average | D | T | Battery life calculation basis | O-34 |
| ENG-06 | Solar charging input | 18-36 VDC solar panel compatible | W(4) | T | Remote range deployment; off-grid sites | O-52 |
| ENG-07 | Power-on to operational time | ≤60 seconds (target ≤30s) | W(4) | T | Quick deployment; ODI Step 3 | O-10 |
| ENG-08 | Brownout/surge protection | Survive 50V transient, 100ms | D | T | Military electrical environment | O-30 |

### 4.5 Material (Vật liệu)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| MAT-01 | BSU housing material | Aluminum alloy (6061-T6 or equiv.) or marine-grade polymer | D | I | Corrosion resistance + weight; tropical environment | O-51 |
| MAT-02 | Fasteners | Stainless steel 316 or equivalent | D | I | Salt spray / humidity resistance | O-51 |
| MAT-03 | PCB conformal coating | IPC-CC-830C Class 3 (acrylic or silicone) | D | I | Tropical humidity protection | O-51 |
| MAT-04 | Sealing gaskets | EPDM or silicone rubber, Vietnamese-sourced | D | I | IP67 sealing; local content | O-49, O-51 |
| MAT-05 | Cable assemblies | UV-resistant, oil-resistant jacket; MIL-DTL-17 or equiv. | W(4) | I | Outdoor durability | O-51 |
| MAT-06 | RoHS compliance | All materials RoHS 3 compliant | D | A | EU export potential; environmental | — |
| MAT-07 | Sensor acoustic coupling | Rubber dampener, Vietnamese natural rubber | W(3) | T | Local content; vibration isolation | O-49 |

### 4.6 Signals (Tín hiệu & Giao tiếp)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| SIG-01 | Primary communication | Ethernet 100BaseT (TCP/IP), CAT 5e/6 | D | T | FASIT standard; TTS/InVeris benchmark | O-35 |
| SIG-02 | Wireless communication | WiFi 802.11n, ≥300m LOS (target 2km with antenna) | D | T | Portable config; InVeris WiFi 2km | O-35 |
| SIG-03 | Scoring data output | X,Y coordinates (mm), timestamp, lane ID, shot ID | D | T | Standard scoring data format | O-21 |
| SIG-04 | Scoring accuracy | ±10mm at 300m range (target ±5mm) | D | T | Saab SASS-4/9 ±10mm; Polytronic ±5mm | O-21 |
| SIG-05 | ADC sampling rate | ≥500 kHz per channel (target 1 MHz) | D | A | TDOA timing resolution for ±10mm accuracy | O-21 |
| SIG-06 | FASIT protocol compatibility | FASIT message set over TCP/IP | W(4) | T | US Army interoperability; export potential | — |
| SIG-07 | Number of sensor channels | 4 minimum (expandable to 9) | D | I | SASS-4 baseline; SASS-9 expansion | O-21 |
| SIG-08 | Maximum lanes per control station | ≥10 lanes | D | T | Saab ROPU benchmark; standard range size | O-23 |
| SIG-09 | Display interface | Web-based HTML5 (any browser/device) | D | D | TrueZero-inspired; no proprietary software | O-50 |
| SIG-10 | Data export formats | CSV, PDF, JSON; USB + network | D | T | Training database integration | O-43 |
| SIG-11 | VHF radio backup | VHF 136-174 MHz, configurable frequency | W(3) | T | Extended range fallback; Saab/InVeris | O-35 |

### 4.7 Safety (An toàn)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| SAF-01 | Electrical safety | IEC 62368-1 compliant | D | T | Product safety standard | — |
| SAF-02 | No projectile deflection | BSU shall not deflect or redirect projectiles | D | T | Range safety critical | O-30 |
| SAF-03 | Low-voltage operation in field | ≤50V DC at all user-accessible points | D | I | Electrical safety in wet conditions | — |
| SAF-04 | Battery safety | UN 38.3 transport tested; BMS with over-discharge, over-charge, short-circuit protection | D | T | Li-ion battery safety | O-30 |
| SAF-05 | EMC emissions | MIL-STD-461G RE102, CE102 | D | T | No interference with range comms | — |
| SAF-06 | Fault indication | Audible/visual alarm on critical system fault | W(3) | D | Operator awareness | O-31 |

### 4.8 Ergonomics (Công thái học)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| ERG-01 | Operator training time | ≤8 hours for basic operation (target 4 hours) | D | D | Low-skill operators; ODI O-50 | O-50 |
| ERG-02 | Display readability | Sunlight-readable; min 500 nits OR anti-glare + sun hood | D | I | Outdoor use; Saab VDU-1 sun hood | O-44 |
| ERG-03 | UI language | Vietnamese primary; English secondary; switchable | D | D | Vietnamese military users | O-50 |
| ERG-04 | Setup without special tools | All field setup using max 1 multi-tool | W(4) | D | Minimize logistics burden | O-40 |
| ERG-05 | Single-person lane setup | One person can install BSU + TPU per lane | W(3) | D | Manpower efficiency | O-12 |
| ERG-06 | Color-coded connectors | Unique connector per cable type (no mis-mating) | W(3) | I | Prevent installation errors | O-13 |

### 4.9 Production (Sản xuất)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| PRD-01 | Local content by value | ≥60% (target 70%) | D | A | Vietnamese national policy | O-49, O-52 |
| PRD-02 | Initial production lot | 50 lane-sets (500 total over 5 years) | D | A | Vietnamese military range count estimate | — |
| PRD-03 | Production capability | Vietnamese machining, PCB assembly, integration | D | A | No specialized imported equipment | O-52 |
| PRD-04 | Component dual-sourcing | All critical components available from ≥2 suppliers | D | A | Supply chain resilience | O-49 |
| PRD-05 | PCB assembly | Designed for local SMT assembly (0402 min, TQFP max) | W(4) | A | Vietnamese PCB house capability | O-52 |
| PRD-06 | Test fixture standardization | One test fixture per subassembly for production QC | W(3) | D | Production quality | — |

### 4.10 Quality (Chất lượng & Độ tin cậy)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| QUA-01 | MTBF (system) | ≥5,000 hours (target 8,000h) | D | A | Saab 40-year longevity benchmark | O-30, O-48 |
| QUA-02 | MTTR (field) | ≤30 minutes for LRU replacement | D | D | Field maintainability | O-37 |
| QUA-03 | Scoring repeatability | ≤±3mm standard deviation over 100 shots | D | T | Measurement consistency | O-21, O-33 |
| QUA-04 | False positive rate | ≤0.1% (1 in 1,000 detections) | D | T | Scoring reliability | O-18 |
| QUA-05 | Missed detection rate | ≤0.5% (1 in 200 shots within zone) | D | T | Scoring completeness | O-19 |
| QUA-06 | Design life | ≥15 years (target 20 years) | W(4) | A | Saab 40-year reference; lifecycle cost | O-47 |
| QUA-07 | Firmware update capability | Field-updatable via USB or Ethernet | W(3) | D | Long-term supportability | O-52 |

### 4.11 Assembly (Lắp ráp)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| ASM-01 | Field assembly time per lane | ≤15 minutes (power-off to operational) | D | D | ODI O-10; combat readiness | O-10 |
| ASM-02 | Connector type | Quick-connect mil-spec (IP67 when mated) | D | I | Field conditions; water resistance | O-11 |
| ASM-03 | Sensor bar mounting | Tool-less quick-mount clamp system | D | D | Speed and simplicity | O-12 |
| ASM-04 | Cable count per lane | ≤3 cables (power, sensor, comm) | W(4) | I | Minimize field wiring | O-11 |
| ASM-05 | Modular LRU design | BSU, TPU, VDU as separate replaceable units | W(3) | I | Field swap capability | O-39 |

### 4.12 Transport (Vận chuyển)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| TRN-01 | Lane set packed weight | ≤25kg total (BSU + TPU + cables + battery) | D | I | 2-person carry; field deployment | O-45 |
| TRN-02 | Transport case | IP67 ruggedized case, stackable | D | I | Military logistics standard | O-46 |
| TRN-03 | Vehicle transport | Fit in standard military truck bed (≥10 lane-sets) | D | I | Vietnamese military vehicles | O-45 |
| TRN-04 | Airline transport (battery) | Li-ion batteries UN 38.3 certified for air transport | W(4) | A | Export/deployment logistics | — |
| TRN-05 | Pack-up time per lane | ≤10 minutes | W(3) | D | End-of-exercise teardown | O-45 |

### 4.13 Operation (Vận hành & Môi trường)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| OPR-01 | Operating temperature | -10°C to +60°C | D | T | Vietnamese climate (tropical); MIL-STD-810H 501/502 | O-27 |
| OPR-02 | Storage temperature | -40°C to +70°C | D | T | MIL-STD-810H warehouse storage | — |
| OPR-03 | Humidity | 95% RH at 40°C, non-condensing; condensing with IP67 | D | T | Tropical monsoon climate; MIL-STD-810H 507 | O-51 |
| OPR-04 | Rain operation | Operational in rain up to 100mm/hr | D | T | Monsoon conditions; IP67 | O-26 |
| OPR-05 | Dust/sand | MIL-STD-810H Method 510.7, Procedure I (dust) | D | T | Dry-season field conditions | O-51 |
| OPR-06 | Salt fog | MIL-STD-810H Method 509.7, 48-hour exposure | D | T | Coastal installations | O-51 |
| OPR-07 | IP rating (BSU, TPU) | IP67 minimum | D | T | Immersion-proof for field conditions | O-51 |
| OPR-08 | Calibration requirement | Calibration-free (zero calibration shots) | D | T | Expired Saab patent WO1991010876A1; ODI #1 opportunity | O-16, O-20 |
| OPR-09 | Ammunition compatibility (Phase 1) | 5.56×45mm, 7.62×39mm, 7.62×51mm, 12.7×99mm | D | T | Vietnamese military standard calibers | O-08 |

### 4.14 Maintenance (Bảo trì)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| MNT-01 | Preventive maintenance interval | ≥500 operating hours (6 months minimum) | D | A | Minimize maintenance burden | O-48 |
| MNT-02 | Built-In Test (BIT) | Auto-diagnostic at power-on; report: firmware, voltage, comm, errors, hit count | D | D | Saab BSU-4/9 BIT feature | O-14, O-31 |
| MNT-03 | LRU replacement | All field-replaceable units swappable with basic tools (Phillips + flat screwdriver) | D | D | Vietnamese maintenance capability | O-40 |
| MNT-04 | Spare parts domestic availability | ≥80% of spare parts sourced within Vietnam | D | A | Supply independence | O-49 |
| MNT-05 | Technical manual | Vietnamese-language O&M manual with troubleshooting flowcharts | W(4) | I | Operator/maintainer reference | O-50 |
| MNT-06 | No special test equipment | Field maintenance with standard multimeter only | W(3) | D | Minimize support equipment | O-40 |
| MNT-07 | Sensor replacement | Individual sensor replaceable without full BSU disassembly | W(3) | D | Reduce repair time & cost | O-37, O-39 |

### 4.15 Costs (Chi phí)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| CST-01 | Unit hardware cost per lane | ≤$500 (at lot size 50) | D | A | ≤70% of import; RE BOM estimates $120-510 | O-47 |
| CST-02 | Complete 10-lane range system | ≤$25,000 (hardware + software + installation) | D | A | Import equiv. ~$40,000-80,000 | O-47 |
| CST-03 | 10-year lifecycle cost per lane | ≤$1,500 (includes spares, maintenance) | D | A | TCO target; domestic support advantage | O-47 |
| CST-04 | Software development (NRE) | One-time; amortized over 500 lane-sets | D | A | Range control + display software | — |
| CST-05 | Import content cost | ≤40% of unit cost (sensors, ICs, connectors) | W(4) | A | Support PRD-01 local content target | O-49 |
| CST-06 | Export price competitiveness | ≤60% of European/US equivalent FOB | W(3) | A | ASEAN export market potential | — |

### 4.16 Schedule (Tiến độ)

| ID | Requirement | Value/Range | D/W | Verify | Source | ODI |
|----|-------------|-------------|-----|--------|--------|-----|
| SCH-01 | Phase 1 prototype (supersonic) | 12 months from Phase 2 start | D | D | First functional prototype | — |
| SCH-02 | Phase 1 field trial | 18 months from Phase 2 start | D | D | 10-lane trial at military range | — |
| SCH-03 | Phase 2 (subsonic Box Target) | 24 months from project start | W(4) | D | Second product variant | O-28 |
| SCH-04 | LRIP (Low-Rate Initial Production) | 30 months from project start | D | D | First 50 lane-sets delivered | — |

---

## 5. STANDARDS COMPLIANCE MATRIX

| Standard | Sections Applied | Requirements Mapped | Compliance Approach |
|----------|-----------------|---------------------|---------------------|
| **MIL-STD-810H** | 501 (High Temp), 502 (Low Temp), 507 (Humidity), 509 (Salt Fog), 510 (Sand/Dust), 514 (Vibration), 516 (Shock) | OPR-01 to OPR-07, FRC-03, FRC-04 | Full environmental test program |
| **MIL-STD-461G** | RE102 (Radiated Emissions), CE102 (Conducted Emissions), RS103 (Radiated Susceptibility) | SAF-05, SIG-01, SIG-02 | EMC shielded enclosure + test |
| **MIL-STD-882E** | Hazard Analysis (4.1-4.5) | SAF-01 to SAF-06 | FMEA + Fault Tree Analysis |
| **IEC 62368-1** | Electrical safety | SAF-01, SAF-03 | Design review + testing |
| **IPC-CC-830C** | Conformal coating, Class 3 | MAT-03 | Process qualification |
| **UN 38.3** | Li-ion battery transport test | ENG-04, TRN-04 | Battery certification |
| **IP67** | IEC 60529 ingress protection | OPR-07, ASM-02 | Enclosure design + test |
| **FASIT** | US Army target interface protocol | SIG-06 | Protocol implementation + interop test |
| **TCVN 7447** | Vietnamese electrical installation | SAF-01 | Design compliance |
| **TCVN 6450** | Vietnamese EMC standard | SAF-05 | Test to TCVN + MIL-STD-461G |

---

## 6. VERIFICATION PLAN SUMMARY

| Verification Type | Quantity | Key Tests | Est. Duration |
|-------------------|----------|-----------|---------------|
| **Analysis (A)** | 18 | MTBF prediction, cost analysis, local content calculation, thermal analysis | 4-6 weeks |
| **Inspection (I)** | 22 | Dimensional, material, workmanship, labeling | 2-3 weeks |
| **Test (T)** | 48 | Environmental (MIL-STD-810H), EMC (461G), accuracy, battery, IP67 | 12-16 weeks |
| **Demonstration (D)** | 19 | Field setup, operator training, maintainability, data export | 4-6 weeks |
| **TOTAL** | **107** | | **22-31 weeks** |

---

## 7. ODI TRACEABILITY MATRIX

| ODI Outcome (Top 10) | Opp Score | Requirements Mapped |
|----------------------|-----------|---------------------|
| O-52: Foreign support independence | 16.5 | PRD-01, PRD-03, PRD-04, MNT-04, CST-01 |
| O-49: Domestic spare parts | 16.0 | PRD-01, PRD-04, MNT-04, MAT-04, MAT-07 |
| O-16: Calibration-free | 15.0 | OPR-08, SIG-04, SIG-05, SIG-07 |
| O-28: Subsonic scoring | 15.0 | SCH-03 (Phase 2 scope) |
| O-47: 10-year TCO | 14.5 | CST-01, CST-02, CST-03, QUA-01, QUA-06 |
| O-21: Shot accuracy | 14.0 | SIG-04, SIG-05, SIG-07, QUA-03 |
| O-51: Tropical resistance | 14.0 | OPR-01 to OPR-07, MAT-01 to MAT-05 |
| O-26: Wind/rain effect | 13.0 | OPR-04, FRC-05, OPR-07 |
| O-27: Temperature effect | 13.0 | OPR-01, OPR-08 (implicit in calibration-free) |
| O-10: Setup time | 12.5 | ASM-01, ASM-03, ENG-07 |

---

## 8. OPEN ISSUES & TBD

| Issue ID | Description | Impact | Owner | Target Date | Status |
|----------|-------------|--------|-------|-------------|--------|
| TBD-01 | Exact MEMS microphone model selection (SPH0641LU4H vs ICS-40730 vs custom) | SIG-04, SIG-05 accuracy | Hardware team | Phase 2 | Open |
| TBD-02 | FPGA vs MCU-only for TDOA processing | SIG-05 timing, CST-01 cost | Hardware team | Phase 2 | Open |
| TBD-03 | Subsonic detection method for Phase 2 (Box Target vs radar) | SCH-03, O-28 | Systems team | Phase 2 | Open |
| TBD-04 | FASIT protocol specification access (US Army controlled) | SIG-06 compliance | Program mgmt | Phase 1 | Open |
| TBD-05 | Specific Vietnamese military caliber velocity data for algorithm tuning | KIN-01, KIN-02 | Test team | Phase 2 | Open |
| TBD-06 | Field survey for ODI validation (MoD access needed) | ODI scores | Program mgmt | Parallel | Open |
| TBD-07 | Export control classification for ASEAN sales | CST-06 | Legal | Phase 3 | Open |

---

## 9. CONFLICT ANALYSIS

| Conflict | Requirements | Resolution |
|----------|-------------|------------|
| Weight vs. IP67 protection | GEO-04 (≤12kg) vs OPR-07 (IP67 adds weight) | Use aluminum 6061-T6 (MAT-01) for strength-to-weight; polymer option if weight exceeds target |
| Cost vs. accuracy | CST-01 (≤$500) vs SIG-04 (±10mm target ±5mm) | ±10mm is MUST; ±5mm is stretch goal. 4-sensor config minimizes cost |
| Local content vs. sensor quality | PRD-01 (≥60% local) vs SIG-04 (precision sensors) | Accept sensors as imported (10% of BOM); maximize local content in housing, PCB, cables, software |
| Battery runtime vs. weight | ENG-03 (≥10h) vs GEO-04/TRN-01 (weight limits) | Li-ion energy density ~250 Wh/kg; 15W × 10h = 150Wh = ~0.6kg cells; achievable within weight budget |
| Setup speed vs. robustness | ASM-01 (≤15min) vs ASM-02 (mil-spec connectors) | Quick-connect mil-spec connectors exist (e.g., Amphenol RJFTV); slight cost premium acceptable |

**Resolution status**: All 5 identified conflicts have feasible resolutions. No showstoppers.

---

*Requirements List v1.0 | VN-TRN-001 | 107 requirements across 16 categories | 85% quantified*
