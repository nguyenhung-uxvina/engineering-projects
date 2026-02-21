---
project: VN-RNG-001
phase: 1
type: requirements
version: 1.0
created: 2026-02-09
status: draft
---

# REQUIREMENTS LIST
## VN-RNG-001: LOMAH Acoustic Shooting Range System
### Version: 1.0 | Date: 2026-02-09

---

## 1. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-09 | Engineering Design System | Initial release - derived from ODI analysis (73 outcomes) and 3 RE reports |

---

## 2. PROJECT OVERVIEW

| Field | Value |
|-------|-------|
| **Product Name** | Smart LOMAH Acoustic Scoring System (Concept B) |
| **Project Code** | VN-RNG-001 |
| **Customer** | Vietnamese People's Army (VPA), Border Defense, Coast Guard, Police |
| **End Users** | Marksmanship instructors, Range NCOICs, individual shooters |
| **Development Period** | 2026 Q1 - 2027 Q2 |
| **Target Cost** | $5,000-8,000/lane (Variant A, lot size 50+) |
| **Selected Concept** | Concept B: Smart LOMAH (ODI scorecard 8.46/10) |
| **Growth Strategy** | DOMINANT - market leadership through performance + cost |

### Source Documents

- [[00_odi/odi_analysis.md]] - Phase 0 ODI analysis (73 outcomes, 3 segments)
- [[00_project_brief.md]] - Project brief
- [[00_odi/re_saab_lomah.md]] - RE: Saab LOMAH
- [[00_odi/re_polytronic.md]] - RE: Polytronic LOMAH
- [[00_odi/re_fats_inveris.md]] - RE: InVeris LOMAH

---

## 3. REQUIREMENTS SUMMARY

| # | Category | MUST | WISH | Total | Quantified % |
|---|----------|------|------|-------|-------------|
| 1 | Geometry | 5 | 4 | 9 | 100% |
| 2 | Kinematics | 4 | 3 | 7 | 100% |
| 3 | Forces | 3 | 2 | 5 | 100% |
| 4 | Energy | 4 | 3 | 7 | 100% |
| 5 | Material | 4 | 3 | 7 | 86% |
| 6 | Signals | 7 | 4 | 11 | 91% |
| 7 | Safety | 5 | 2 | 7 | 86% |
| 8 | Ergonomics | 4 | 4 | 8 | 88% |
| 9 | Production | 4 | 3 | 7 | 86% |
| 10 | Quality | 5 | 4 | 9 | 100% |
| 11 | Assembly | 3 | 3 | 6 | 83% |
| 12 | Transport | 3 | 2 | 5 | 100% |
| 13 | Operation | 6 | 4 | 10 | 100% |
| 14 | Maintenance | 4 | 4 | 8 | 88% |
| 15 | Costs | 5 | 3 | 8 | 100% |
| 16 | Schedule | 4 | 2 | 6 | 100% |
| | **TOTAL** | **70** | **50** | **120** | **94%** |

**Gate 1 Target: >=80% quantified -- ACHIEVED (94%)**

---

## 4. DETAILED REQUIREMENTS

### 4.1 Geometry (GEO)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| GEO-001 | Sensor bar length | 1000-1300 mm | MUST | I | O-41 | RE: Saab (~1200mm), Polytronic (~1200mm) | Must cover detection zone width; mounting compatibility |
| GEO-002 | Sensor bar width (depth) | <=450 mm | MUST | I | O-20 | RE: Saab, Polytronic (450mm) | Fits behind standard target frames |
| GEO-003 | Sensor bar height | <=250 mm | MUST | I | O-20 | RE: Polytronic (215mm portable) | Below target silhouette for ballistic protection |
| GEO-004 | Sensor bar mass | <=12 kg (target 10 kg) | WISH (W=4) | I | O-20 | RE: Saab (~10 kg), Polytronic (~12 kg) | Field-portable by 1 person |
| GEO-005 | Detection zone - infantry | >=3.0 x 2.5 m (W x H) | MUST | T | O-41, O-39 | RE: InVeris (3x2.5m), Polytronic (double Fig 11) | Full torso silhouette + near-miss detection |
| GEO-006 | Detection zone - adjustable | Configurable via software | WISH (W=3) | D | O-50 | RE: InVeris (adjustable) | For different target types |
| GEO-007 | Sensor count | 8 MEMS microphones | MUST | I | O-26, O-29 | RE: Saab (8 dual-delta), GCC-PHAT design | 5 redundant beyond minimum 3 for reliability |
| GEO-008 | Sensor spacing geometry | Delta array configuration, inter-sensor distance 100-300 mm | MUST | I | O-26 | RE: Saab delta array, published TDOA literature | Optimized for multilateration accuracy |
| GEO-009 | Firing Point Display size | 8-12 inch tablet screen | WISH (W=3) | I | O-32 | COTS Android tablet | Sunlight-readable option preferred |

### 4.2 Kinematics (KIN)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| KIN-001 | Minimum detectable projectile velocity | <=450 m/s at target (Mach ~1.3) | MUST | T | O-05, O-26 | RE: InVeris (450 m/s), Saab (440-450 m/s) | Supersonic only; covers 5.56mm NATO at 600m |
| KIN-002 | Maximum detection rate | >=1,200 RPM | MUST | T | O-38, O-40 | RE: InVeris (1200), Saab (1200) | Automatic/burst fire capability |
| KIN-003 | Stretch detection rate | >=2,000 RPM | WISH (W=3) | T | O-38 | RE: Polytronic (2000 RPM) | Competitive advantage if achievable |
| KIN-004 | Shot-to-display latency | <=100 ms (target <=50 ms) | MUST | T | O-27 (Opp 17.1 EXTREME) | ODI Step 8, project brief | #2 EXTREME opportunity; ARM SoC + WiFi direct |
| KIN-005 | Shooting angle - azimuth | >=+/-15 degrees from perpendicular | MUST | T | O-39 | RE: Saab, Polytronic, InVeris (all +/-15 deg) | Industry standard for range safety angles |
| KIN-006 | Shooting angle - elevation | >=+/-5 degrees | WISH (W=4) | T | O-39 | RE: Polytronic (+/-3 to +/-5) | Covers elevated/depressed firing positions |
| KIN-007 | Engagement distances | 25 m to 300 m (standard), 600 m+ (precision variant) | WISH (W=5) | T | O-39 (Opp 11.0) | ODI Segment B, project brief | Segment A: 25-300m; Segment B: 600m+ |

### 4.3 Forces (FOR)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| FOR-001 | Vibration resistance | Per MIL-STD-810H Method 514.8, Cat 4 (truck transport) | MUST | T | O-68 | MIL-STD-810H | Field transport on military vehicles |
| FOR-002 | Shock resistance | Per MIL-STD-810H Method 516.8, Procedure I (functional shock, 40g 11ms) | MUST | T | O-68, O-65 | MIL-STD-810H | Drop and handling during field deployment |
| FOR-003 | Ballistic protection | Sensor bar survives direct-fire environment without damage to sensors | MUST | T | O-65 | RE: All competitors (sensors below target plane) | Steel/composite enclosure; sensors below target face |
| FOR-004 | Wind load on sensor bar | Operational at sustained wind <=15 m/s (55 km/h) | WISH (W=3) | T | O-08 | Structural requirement | Mounting must withstand without misalignment |
| FOR-005 | Target frame mounting load | Support <=20 kg sensor bar + bracket without deformation | WISH (W=4) | A | GEO-004 | Compatibility with Vietnamese target frames | Retrofit kit for existing range infrastructure |

### 4.4 Energy (ENE)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| ENE-001 | Primary power input | 12V DC nominal (10-16V range) | MUST | T | O-72 | RE: All competitors (12V DC) | Compatible with vehicle power, solar, battery |
| ENE-002 | Mains power option | 220V AC 50Hz via external PSU to 12V DC | MUST | T | O-72 | Vietnamese grid standard | Vietnamese military power standard |
| ENE-003 | Power-over-Ethernet (POE) | IEEE 802.3af/at (15.4W/25.5W) | WISH (W=4) | T | O-16 | RE: InVeris (POE option) | Reduces cabling; single Ethernet cable for power+data |
| ENE-004 | Battery operation duration | >=10 hours continuous at 25C (target 12h) | MUST | T | O-18 (Opp 13.0 HIGH) | RE: InVeris (10h), project brief (10h+) | Lithium-ion removable battery pack |
| ENE-005 | Sensor bar power consumption | <=8W average (target <=5W) | MUST | T | ENE-004 | Derived: 10h from reasonable battery size (~100Wh) | Enables compact battery; passive cooling |
| ENE-006 | Battery charge time | <=4 hours 0-100% | WISH (W=3) | T | O-18 | Operational need | Overnight charge for next-day use |
| ENE-007 | Battery hot-swap | Field-swappable without power-down | WISH (W=4) | D | O-18 | RE: Saab (quick-fit bayonet connector) | Continuous operation with spare battery |

### 4.5 Material (MAT)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| MAT-001 | Enclosure material | Aluminum alloy 6061-T6 or equivalent | MUST | I | O-65, O-70 | RE: Saab (zinc-steel), design decision (aluminum = lighter, corrosion-resistant) | Anodized + powder coated; locally CNC machined |
| MAT-002 | Corrosion resistance - salt spray | >=500 hours per MIL-STD-810H Method 509.7 (salt fog) | MUST | T | O-70 (Opp 12.0 HIGH) | MIL-STD-810H | Coastal installation requirement (Da Nang, Cam Ranh) |
| MAT-003 | UV resistance | >=10 years outdoor exposure without degradation (ASTM G154) | MUST | T | O-65, O-73 | Tropical outdoor environment | UV-stabilized enclosure coating/material |
| MAT-004 | PCB protection | Conformal coating (IPC-CC-830C, Type AR or UR) | MUST | I | O-71 | RE: Saab design decision, tropical requirement | Protects against humidity, salt, fungus |
| MAT-005 | Fastener material | Stainless steel 316 (marine-grade) | WISH (W=5) | I | O-70 | RE: Saab (SS fixings), Polytronic (SS fixings) | Critical for coastal salt spray environments |
| MAT-006 | Gasket material | Silicone or EPDM, rated -40C to +200C | WISH (W=4) | I | O-65 | IP67 sealing requirement | Long-term UV and ozone resistance |
| MAT-007 | RoHS compliance | RoHS 3 (EU 2015/863) compliant | WISH (W=3) | I | — | Export market requirement | Enables European/international sales |

### 4.6 Signals (SIG)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| SIG-001 | Primary communication | Ethernet 100BaseT (IEEE 802.3) | MUST | T | O-19 | RE: All competitors (Ethernet backbone) | Wired backbone for reliability |
| SIG-002 | Wireless communication | WiFi IEEE 802.11n/ac, 2.4 GHz + 5 GHz dual-band | MUST | T | O-17, O-19 | RE: InVeris (WiFi), project brief | Tablet connectivity; reduces field cabling |
| SIG-003 | Wireless range | >=500 m line-of-sight (target 1000 m) | MUST | T | O-39 | RE: InVeris (2000m RF) | Range firing point to sensor bar at 300m+ distances |
| SIG-004 | Data protocol | JSON over MQTT (primary), REST API (secondary) | MUST | D | O-66, O-58 | Design decision: open standard vs proprietary XML | Zero vendor lock-in; modern, lightweight protocol |
| SIG-005 | Sensor sampling rate | >=1 MHz per channel (8 channels simultaneous) | MUST | T | O-26 | GCC-PHAT requirement, firmware design | Sub-microsecond TDOA resolution |
| SIG-006 | ADC resolution | >=12-bit | MUST | I | O-26 | STM32H7 (12-bit 3.6 MSPS), firmware design | Adequate dynamic range for shockwave detection |
| SIG-007 | Temperature sensor | Accuracy <=+/-0.5C in range -10C to +70C | MUST | T | O-09 | Alternative to Saab dual-delta patent | Real-time speed-of-sound correction: c(T) = 331.3 + 0.606*T |
| SIG-008 | Lane discrimination | Distinguish shots from >=2 adjacent lanes | WISH (W=5) | T | O-31, O-28 | RE: InVeris (Lane Shot Initiator), Saab (LNR) | Firing angle filtering + optional LSI accessory |
| SIG-009 | Display refresh rate | >=30 fps on shooter tablet | WISH (W=3) | T | O-27 | UX requirement | Smooth real-time shot overlay animation |
| SIG-010 | Data export format | CSV, JSON, PDF report | WISH (W=4) | D | O-55, O-58 | O-58: export to military records | Interoperability with existing Vietnamese records systems |
| SIG-011 | EMC compliance | Per MIL-STD-461G (RE102, RS103 minimum) | MUST | T | — | Defense standard requirement | No interference with range communication systems |

### 4.7 Safety (SAF)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| SAF-001 | Electrical safety | IEC 62368-1 or equivalent; <=42V DC max | MUST | T | — | Electrical safety standard | Low-voltage design inherent (12V DC) |
| SAF-002 | Battery safety | UN 38.3 transport certification; BMS with overcharge/overdischarge/short-circuit protection | MUST | T | ENE-004 | Lithium battery safety | Critical for military transport and storage |
| SAF-003 | Ballistic safety | No sensor components above target face plane; sensor bar fully below target silhouette | MUST | I | FOR-003 | RE: All competitors (sensors below target) | Personnel safety - sensors in line of fire |
| SAF-004 | Fail-safe operation | System failure does NOT create range safety hazard; graceful degradation | MUST | D | O-24 | MIL-STD-882E principle | Loss of scoring does not affect range safety |
| SAF-005 | Hazard analysis | Per MIL-STD-882E; FMEA completed before prototype test | MUST | A | — | MIL-STD-882E | Identify and mitigate all safety risks |
| SAF-006 | Grounding | Single-point ground; chassis bonded to earth/vehicle ground | WISH (W=4) | I | — | EMC/safety best practice | Lightning and ESD protection |
| SAF-007 | Warning labels | Vietnamese + English bilingual safety labels on all accessible panels | WISH (W=3) | I | — | Vietnamese regulation | High voltage, pinch points, battery warnings |

### 4.8 Ergonomics (ERG)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| ERG-001 | Operator training time | <=8 hours for basic operation (target 4h) | MUST | D | O-06, O-28 | Pahl & Beitz: training requirement | Vietnamese military instructor can operate after 1-day course |
| ERG-002 | Maintenance training time | <=16 hours for Level 1 maintenance | MUST | D | O-62, O-64 | Operational need | Vietnamese technician can diagnose and replace modules |
| ERG-003 | User interface language | Vietnamese primary, English secondary, switchable | MUST | D | O-66 | Vietnamese market requirement | All menus, alerts, reports in Vietnamese |
| ERG-004 | Instructor multi-lane view | Display >=16 lanes simultaneously on single screen | MUST | D | O-28 (Opp 17.0 EXTREME) | #1 EXTREME opportunity; RE: Saab MCS (16 lanes) | Color-coded alert system (green/yellow/red per lane) |
| ERG-005 | Sunlight readability | Display readable at >=5000 lux ambient | WISH (W=5) | T | O-32 (Opp 13.0 HIGH) | RE: InVeris FPC (sun shield, adj. brightness) | COTS sunlight-readable tablet or anti-glare film |
| ERG-006 | Setup by single operator | 1 person can install and configure <=4 lanes in <=30 minutes | WISH (W=4) | D | O-16 (Opp 11.5) | ODI outcome | Reduces personnel requirement from 4-8 to 1-2 |
| ERG-007 | View switching time | Single-shooter to multi-lane view in <=1 tap / <=0.5 seconds | WISH (W=3) | T | O-35 | UX requirement | Instructor rapid navigation |
| ERG-008 | Audio/visual shot alert | Configurable audible beep + visual flash on new shot | WISH (W=3) | D | O-42 | Coaching effectiveness | Instructor immediately aware of shot event |

### 4.9 Production (PRD)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| PRD-001 | Local content by value | >=60% (target 70%) | MUST | A | O-66 (Opp 16.5 EXTREME) | Vietnamese defense policy, CLAUDE.md | Enclosure, PCB, assembly, brackets, cabling, testing = local |
| PRD-002 | Production volume (Year 1) | 32 lanes (2 pilot installations x 16 lanes) | MUST | A | — | ODI Step 10 revenue model | Pilot production; hand-assembly acceptable |
| PRD-003 | Production volume (Year 2+) | 160+ lanes/year | WISH (W=5) | A | — | ODI Step 10: scaling target | Design for batch production; jigs and fixtures |
| PRD-004 | PCB manufacturing | Vietnamese PCB fabrication (4-layer FR4 minimum) | MUST | I | O-66, PRD-001 | Local content requirement | Multiple Vietnamese PCB fab suppliers available |
| PRD-005 | CNC machining | Vietnamese CNC shops for enclosure + brackets | WISH (W=5) | I | PRD-001 | Local content: enclosure is largest cost item | 6061-T6 aluminum CNC + anodize locally |
| PRD-006 | Assembly skill level | Assembly by technician with IPC-A-610 Class 2 workmanship | WISH (W=4) | I | — | Production quality requirement | Achievable with 2-week training program |
| PRD-007 | Test automation | Automated end-of-line test (self-test + simulated shot) | WISH (W=3) | D | — | Production efficiency | Reduces test time from hours to minutes |

### 4.10 Quality (QUA)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| QUA-001 | Shot placement accuracy (center zone) | <=5 mm average radial error within 150 mm radius of center, wind <1.5 m/s | MUST | T | O-26 (Opp 16.5 EXTREME) | RE: InVeris (<5mm), Saab (<5mm), Polytronic (<=10mm avg) | #3 EXTREME opportunity; credibility threshold |
| QUA-002 | Shot placement accuracy (Zone B) | <=10 mm average radial error, 150-500 mm from center | MUST | T | O-26 | RE: Polytronic zone-graded approach (<=14mm Zone B) | Honest zone-graded specification per Polytronic lesson |
| QUA-003 | Shot placement accuracy (Zone C) | <=15 mm average radial error, 500-1000 mm from center | WISH (W=5) | T | O-26 | RE: Polytronic (<=16mm Zone C) | Edge accuracy acceptable at reduced precision |
| QUA-004 | Detection rate (hit detection) | >=99.5% at <=600 RPM, >=98% at 1200 RPM | MUST | T | O-29 (Opp 15.4 EXTREME) | #7 EXTREME opportunity | Missed shots unacceptable for qualification scoring |
| QUA-005 | False positive rate | <=0.1% (1 false per 1000 shots) | MUST | T | O-30 | Scoring integrity requirement | False hits worse than missed detections for trust |
| QUA-006 | Accuracy repeatability | Standard deviation <=2 mm across 100-shot test at center | WISH (W=5) | T | O-26, O-48 | Qualification scoring reliability | Consistent results session-to-session |
| QUA-007 | MTBF (sensor bar) | >=5,000 hours (target 8,000 hours) | MUST | A | O-65, O-24 | MIL-HDBK-217F prediction | ~2 years continuous operation at 8h/day |
| QUA-008 | Group size calculation accuracy | <=1 mm error vs manual measurement | WISH (W=4) | T | O-36 | Statistical computation accuracy | Extreme spread and CEP calculation |
| QUA-009 | Qualification scoring accuracy | 100% agreement with manual scoring for pass/fail | MUST | T | O-48 (Opp 14.0 HIGH) | Scoring integrity — must match doctrine | Zero tolerance for incorrect pass/fail |

### 4.11 Assembly (ASM)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| ASM-001 | Field installation time | <=2 hours per lane (first install); <=30 minutes per lane (repeat) | MUST | D | O-16 | Operational deployment requirement | Includes mounting, cabling, power, commissioning |
| ASM-002 | Tools required for installation | Standard hand tools only (no special tools) | MUST | I | O-16, O-66 | Vendor independence | M6/M8 hex, screwdriver, wire stripper only |
| ASM-003 | Retrofit compatibility | Mountable on existing Vietnamese target frames (TBD specific types) | MUST | D | — | RE: InVeris retrofit philosophy | Universal bracket kit for common frame types |
| ASM-004 | Modular sensor replacement | Individual MEMS sensor replaceable in field in <=15 minutes | WISH (W=5) | D | O-62 (Opp 13.0 HIGH) | RE: InVeris (individual sensor module replacement) | Plug-and-play sensor modules; auto-recalibrate |
| ASM-005 | Connector type | Standard M12 waterproof (IP67) connectors | WISH (W=4) | I | O-61 | Reliability + field serviceability | No proprietary connectors |
| ASM-006 | Cable length options | 5m, 10m, 25m, 50m pre-terminated Ethernet cables | WISH (W=3) | I | — | Installation flexibility | Standard shielded Cat6 outdoor-rated |

### 4.12 Transport (TRP)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| TRP-001 | Portable system weight (complete 1-lane kit) | <=25 kg total (sensor bar + battery + tablet + cables + case) | MUST | I | O-20 (Opp 12.0 HIGH) | ODI Segment C (Field Deployers) | Man-portable by 1 person with backpack/case |
| TRP-002 | Transport case | MIL-STD-810H rated transit case (Pelican or equiv) | MUST | I | FOR-001, FOR-002 | Military transport requirement | Stackable, with foam inserts, carry handles |
| TRP-003 | Vehicle transport | Rated for military truck transport (MIL-STD-810H Method 514.8) | MUST | T | FOR-001 | Field deployment by vehicle | Unpaved road vibration profile |
| TRP-004 | Air transport | Battery meets IATA DG lithium battery requirements | WISH (W=4) | I | SAF-002 | Expeditionary deployment | UN 38.3 + <=100 Wh per battery module |
| TRP-005 | Packaging volume per lane | <=0.1 m3 packed (target 0.06 m3) | WISH (W=3) | I | — | Storage and shipping efficiency | 10-lane system fits in single pallet |

### 4.13 Operation (OPR)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| OPR-001 | Operating temperature | -10C to +55C continuous | MUST | T | O-68 (Opp 15.0 EXTREME) | Vietnamese climate: 35-45C common, +55C peak sun-exposed | MIL-STD-810H Method 501.7/502.7 |
| OPR-002 | Storage temperature | -20C to +70C | MUST | T | O-73 | MIL-STD-810H | Non-climate-controlled warehouse storage |
| OPR-003 | Humidity | >=95% RH non-condensing, continuous operation | MUST | T | O-71, O-12 (Opp 13.5 HIGH) | Vietnamese monsoon: 80-95% RH for months | MIL-STD-810H Method 507.6 |
| OPR-004 | Rain resistance | IP67 (immersion 1m / 30min) | MUST | T | O-69, O-12 | Tropical monsoon operation | IEC 60529 test |
| OPR-005 | Dust resistance | IP6X (dust-tight) | MUST | T | O-68 | Field deployment | IEC 60529 test |
| OPR-006 | Solar radiation | Per MIL-STD-810H Method 505.7, 1120 W/m2 | MUST | T | O-68 | Tropical direct sunlight | Component derating + thermal design |
| OPR-007 | Power-up to operational | <=60 seconds from power-on to first shot detection | WISH (W=5) | T | O-13, O-14 | ODI: minimize startup time | Auto-calibration during boot |
| OPR-008 | Caliber range | 5.56mm NATO to 12.7mm (.50 cal) | WISH (W=5) | T | O-05 | RE: InVeris (.22-.50), Saab (5.56-12.7) | Vietnamese standard: 7.62x39, 5.56x45, 12.7x108 |
| OPR-009 | Wind accuracy limit | Accuracy spec maintained at wind <=1.5 m/s at sensor bar | MUST | T | QUA-001 | RE: All competitors (~1.5 m/s limit) | Specify wind limit honestly; optional rubber baffling |
| OPR-010 | Simultaneous lanes per controller | >=16 lanes (target 32) | WISH (W=5) | T | O-10, O-28 | ODI Segment A (Throughput, 16-32 lanes) | Software scalability; each sensor bar independent |

### 4.14 Maintenance (MNT)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| MNT-001 | Mean Time To Repair (MTTR) | <=30 minutes for module-level replacement | MUST | D | O-25, O-64 | Operational availability requirement | Swap sensor bar or module; resume training |
| MNT-002 | Maintenance levels | 2-level: Field (module swap) + Depot (board-level repair) | MUST | A | O-62 | Vietnamese military maintenance doctrine | Field: 1-2 trained technicians; Depot: electronics bench |
| MNT-003 | Calibration interval | >=12 months between professional recalibrations | MUST | T | O-67 | Operational cost reduction | Auto-calibration on power-up reduces manual calibration need |
| MNT-004 | Self-diagnostics (BIT) | Auto-detect >=90% of common faults; display fault code + recommended action | MUST | T | O-23, O-24, O-64 | RE: All competitors (BIT on power-up) | Sensor health, comms status, battery level, temperature |
| MNT-005 | Spare parts availability | All replacement modules available within 7 days in-country | WISH (W=5) | D | O-63, O-66 | Vendor independence | Vietnamese-stocked spares: sensor module, battery, PCB, cables |
| MNT-006 | Spare parts cost | Annual spares cost <=5% of system unit cost | WISH (W=4) | A | O-63 (Opp 14.0 HIGH) | Lifecycle cost control | COTS components minimize spares cost |
| MNT-007 | Remote diagnostics | WiFi/Ethernet remote health monitoring from range control station | WISH (W=3) | D | O-64 | Reduces need to walk to target line for diagnostics | Dashboard shows all sensor bar statuses |
| MNT-008 | Firmware update | Over-the-air (OTA) firmware update via WiFi | WISH (W=4) | D | O-66 | Vietnamese firmware team can push updates | Secure boot + signed firmware images |

### 4.15 Costs (CST)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| CST-001 | Unit cost per lane - Variant A (Multi-Lane) | <=$8,000 at lot size 50 (target $5,000) | MUST | A | O-66, ODI pricing | Project brief: $5,000-8,000/lane | Segment A: Throughput Maximizers |
| CST-002 | Unit cost per lane - Variant C (Portable) | <=$4,000 at lot size 100 (target $2,500) | MUST | A | — | Project brief: $2,000-4,000/lane | Segment C: Field Deployers |
| CST-003 | Cost vs import ratio | <=60% of equivalent InVeris import cost | MUST | A | O-66 | Project brief: <=50-60% of import | InVeris est. $15,000-30,000/lane import |
| CST-004 | Sensor bar BOM cost | <=$900 per unit at lot size 50 (target $500) | MUST | A | — | RE: Saab BOM estimate ($362-662 + 30% margin) | COTS MEMS ($3-5 ea), ARM SoC ($15-30), PCB ($30-50), enclosure ($150-300) |
| CST-005 | 10-year lifecycle cost per lane | <=$12,000 (acquisition + 10yr maintenance) | MUST | A | O-63 | Lifecycle cost competitiveness | Import LCC est. $25,000-50,000 per lane |
| CST-006 | Development cost (NRE) | <=$200,000 total (target $150,000) | WISH (W=4) | A | — | Budget constraint | Includes prototypes, tooling, testing, firmware |
| CST-007 | Annual maintenance cost per lane | <=$400 (target $250) | WISH (W=4) | A | O-63, MNT-006 | Operational cost target | <5% of acquisition cost per year |
| CST-008 | Tablet cost (COTS) | <=$300 per firing point display | WISH (W=3) | I | — | Android tablet COTS | Sunlight-readable option may cost more |

### 4.16 Schedule (SCH)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Source | Notes |
|----|-------------|-------------|------|--------|-----------|--------|-------|
| SCH-001 | Prototype completion | Q3 2026 (1 functional sensor bar + software demo) | MUST | D | — | Development plan | Proof of accuracy <5mm on test range |
| SCH-002 | Pilot installation | Q4 2026 (2 ranges x 16 lanes) | MUST | D | — | ODI Year 1 target (32 lanes) | Real-world validation at Vietnamese military range |
| SCH-003 | Production readiness | Q1 2027 | MUST | D | — | Development plan | BOM finalized, jigs ready, supply chain qualified |
| SCH-004 | Year 2 production | 160 lanes delivered by Q4 2027 | MUST | A | — | ODI Year 2 revenue model | Batch production capability |
| SCH-005 | Precision variant (Variant B) | Q2 2027 design start | WISH (W=3) | A | — | Segment B roadmap | After Variant A proven in field |
| SCH-006 | Portable variant (Variant C) | Q3 2027 design start | WISH (W=3) | A | — | Segment C roadmap | Ruggedized variant for field deployment |

---

## 5. STANDARDS COMPLIANCE MATRIX

| Standard | Title | Applicable Sections | Requirements Mapped | Compliance Approach |
|----------|-------|---------------------|---------------------|---------------------|
| **MIL-STD-810H** | Environmental Engineering Considerations | 501.7 (High Temp), 502.7 (Low Temp), 505.7 (Solar Radiation), 507.6 (Humidity), 509.7 (Salt Fog), 510.7 (Sand/Dust), 514.8 (Vibration), 516.8 (Shock) | OPR-001 to OPR-006, FOR-001 to FOR-003, MAT-002 | Full test program per applicable methods |
| **MIL-STD-461G** | EMI/EMC Requirements | RE102 (Radiated Emissions), RS103 (Radiated Susceptibility), CE102 (Conducted Emissions) | SIG-011 | EMC shielding + full test |
| **MIL-STD-882E** | System Safety | Hazard analysis, risk assessment (4.1-4.5) | SAF-004, SAF-005 | FMEA + Fault Tree Analysis |
| **IEC 60529** | Ingress Protection | IP67 (dust-tight + 1m immersion) | OPR-004, OPR-005 | Test per IEC 60529 procedures |
| **IEC 62368-1** | Audio/Video/IT Equipment Safety | Electrical safety clauses | SAF-001 | Test + declaration of conformity |
| **IEEE 802.3** | Ethernet | 100BaseT, 802.3af/at POE | SIG-001, ENE-003 | Standard Ethernet PHY compliance |
| **IEEE 802.11** | WiFi | 802.11n/ac dual-band | SIG-002 | WiFi module certification (FCC/CE equiv) |
| **UN 38.3** | Lithium Battery Transport | T1-T8 tests | SAF-002, TRP-004 | Battery supplier certification |
| **IPC-CC-830C** | Conformal Coating | Type AR or UR | MAT-004 | Coating process + inspection |
| **IPC-A-610** | Acceptability of Electronic Assemblies | Class 2 (Dedicated Service) | PRD-006 | Workmanship inspection |
| **TCVN** | Vietnamese National Standards | TBD: electrical, environmental, labeling | OPR-001, SAF-007, ENE-002 | Compliance review pending TCVN mapping |

---

## 6. ODI TRACEABILITY MATRIX (Top 25 Opportunities)

| Rank | ODI Outcome | Opp Score | Category | Requirements Mapped | Coverage |
|------|------------|-----------|----------|---------------------|----------|
| 1 | O-28: Maximize lanes per instructor | 17.0 | EXTREME | ERG-004, SIG-002, OPR-010 | Full |
| 2 | O-27: Minimize shot-to-display latency | 17.1 | EXTREME | KIN-004, SIG-009 | Full |
| 3 | O-26: Maximize shot placement accuracy | 16.5 | EXTREME | QUA-001, QUA-002, QUA-003, QUA-006, SIG-005, SIG-006, SIG-007, GEO-007, GEO-008 | Full |
| 4 | O-33: Minimize error pattern ID effort | 16.4 | EXTREME | ERG-004, SIG-010 (software req) | Partial (software-heavy, detailed in SW spec) |
| 5 | O-66: Minimize foreign vendor dependency | 16.5 | EXTREME | PRD-001, PRD-004, PRD-005, SIG-004, MNT-005, MNT-008, ERG-003 | Full |
| 6 | O-34: Maximize coaching effectiveness | 15.5 | EXTREME | ERG-004, ERG-007, ERG-008, KIN-004 | Full |
| 7 | O-29: Minimize missed detection rate | 15.4 | EXTREME | QUA-004, GEO-007, KIN-001 | Full |
| 8 | O-42: Minimize corrective feedback time | 16.0 | EXTREME | KIN-004, ERG-004, ERG-007, ERG-008 | Full |
| 9 | O-43: Maximize cross-session tracking | 16.1 | EXTREME | SIG-010 (software req, database) | Partial (software spec) |
| 10 | O-54: Minimize record generation time | 15.0 | EXTREME | SIG-010 (PDF/CSV export, auto-report) | Partial (software spec) |
| 11 | O-68: Maximize tropical heat reliability | 15.0 | EXTREME | OPR-001, OPR-006, MAT-001, MAT-004, ENE-005 | Full |
| 12 | O-65: Maximize tropical lifespan | 14.6 | HIGH | MAT-001, MAT-002, MAT-003, MAT-004, MAT-005, QUA-007 | Full |
| 13 | O-10: Maximize simultaneous shooters | 13.5 | HIGH | OPR-010, ERG-004 | Full |
| 14 | O-63: Minimize spare parts cost | 14.0 | HIGH | MNT-006, CST-007, ASM-005 | Full |
| 15 | O-48: Maximize qualification scoring accuracy | 14.0 | HIGH | QUA-009, QUA-001 | Full |
| 16 | O-12: Minimize rain/humidity impact | 13.5 | HIGH | OPR-003, OPR-004, MAT-004 | Full |
| 17 | O-71: Minimize humidity on electronics | 13.5 | HIGH | OPR-003, MAT-004 | Full |
| 18 | O-18: Maximize battery duration | 13.0 | HIGH | ENE-004, ENE-005, ENE-006, ENE-007 | Full |
| 19 | O-32: Maximize sunlight display visibility | 13.0 | HIGH | ERG-005 | Full |
| 20 | O-55: Maximize report completeness | 13.5 | HIGH | SIG-010 | Partial (software spec) |
| 21 | O-62: Maximize field replaceability | 13.0 | HIGH | ASM-004, MNT-001, MNT-002 | Full |
| 22 | O-70: Maximize salt spray resistance | 12.0 | HIGH | MAT-002, MAT-005 | Full |
| 23 | O-16: Minimize setup personnel | 11.5 | MODERATE | ERG-006, ASM-001, ASM-002 | Full |
| 24 | O-39: Maximize distance range | 11.0 | MODERATE | KIN-007, SIG-003 | Full |
| 25 | O-56: Minimize data loss likelihood | 12.0 | HIGH | SIG-010 (local storage + backup) | Partial (software spec) |

**Coverage: 21/25 FULL, 4/25 PARTIAL (software-specific outcomes deferred to software requirements spec)**

---

## 7. VERIFICATION PLAN SUMMARY

| Verification Type | Count | Estimated Cost | Duration | Notes |
|-------------------|-------|----------------|----------|-------|
| Analysis (A) | 18 | $5,000 | 2 weeks | BOM cost, MTBF prediction, FTO, FMEA |
| Inspection (I) | 24 | $2,000 | 1 week | Dimensions, materials, labels, workmanship |
| Test (T) | 58 | $40,000 | 8 weeks | Environmental (MIL-STD-810H), EMC, accuracy, rate, IP67 |
| Demonstration (D) | 20 | $8,000 | 3 weeks | Field trials, user operation, installation, maintenance |
| **TOTAL** | **120** | **$55,000** | **14 weeks** | Parallel execution reduces calendar time |

---

## 8. CONFLICT ANALYSIS

| Conflict | Requirements | Resolution |
|----------|-------------|------------|
| Weight vs Ballistic Protection | GEO-004 (<=12kg) vs FOR-003 (ballistic survival) | Use aluminum enclosure (lighter than steel) + AR500 steel plate only in direct-fire path. Target: 10kg with protection. |
| Battery Life vs Weight | ENE-004 (>=10h) vs TRP-001 (<=25kg total kit) | Design for 5W avg consumption; 100Wh battery (~0.6kg) gives 20h. Total kit weight target achievable. |
| Cost vs Accuracy | CST-004 (<=$900 BOM) vs QUA-001 (<=5mm) | COTS MEMS ($3-5 ea) proven to achieve <5mm with GCC-PHAT. No premium sensors needed. RE confirms this. |
| Detection Rate vs Cost | KIN-003 (2000 RPM wish) vs CST-004 (BOM constraint) | 1200 RPM achievable with STM32H7 at current BOM. 2000 RPM may require FPGA ($50-100 adder). Keep as WISH. |
| Portability vs Multi-Lane | TRP-001 (man-portable) vs OPR-010 (16+ lanes) | Resolved by modular platform: each sensor bar is independent. Portable variant = 1-4 lanes. Multi-lane = rack controller. |

**Unresolved conflicts: NONE**

---

## 9. OPEN ISSUES & TBD

| Issue ID | Description | Owner | Target Date | Status |
|----------|-------------|-------|-------------|--------|
| TBD-001 | Specific Vietnamese target frame types for retrofit bracket design (ASM-003) | Field survey team | Q2 2026 | Open |
| TBD-002 | TCVN standard numbers for electrical safety, environmental, labeling | Standards researcher | Q2 2026 | Open |
| TBD-003 | Specific MEMS microphone model selection (ICS-40730 vs SPH0645LM4H vs others) | Hardware engineer | Phase 2 | Open |
| TBD-004 | Software requirements specification (AI coaching, database, reporting, web dashboard) | Software lead | Phase 1.5 | Open |
| TBD-005 | ODI field survey validation (60-100 respondents) to confirm opportunity scores | Field survey team | Q2 2026 | Open |
| TBD-006 | Export market standards (FASIT compliance for potential US/NATO market) | Business development | Phase 3+ | Open |
| TBD-007 | Armor LOMAH variant specifications (detection zone 4x3m, up to 120mm caliber) | Engineering | Phase 3+ | Open |

---

## 10. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | Engineering Design System | — | 2026-02-09 |
| Reviewer | — | — | — |
| Approver | — | — | — |

---

## Cross-References

- [[00_odi/odi_analysis.md]] - Phase 0 ODI analysis (73 outcomes)
- [[00_project_brief.md]] - Project brief
- [[00_odi/re_saab_lomah.md]] - RE: Saab LOMAH
- [[00_odi/re_polytronic.md]] - RE: Polytronic LOMAH
- [[00_odi/re_fats_inveris.md]] - RE: InVeris LOMAH
- [[firmware/inc/gcc_phat.h]] - GCC-PHAT API (informs SIG-005, SIG-006)
