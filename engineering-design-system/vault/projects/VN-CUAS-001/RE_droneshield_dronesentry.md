---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: DroneShield DroneSentry (Australia)
version: 1.0
created: 2026-02-11
status: complete
---

# RE: DroneShield DroneSentry - Australia
## Reverse Engineering Analysis from Public Sources

> **KEY DISTINCTION:** DroneShield DroneSentry is a **multi-sensor fusion C-UAS system** — NOT a purely acoustic sensor like Squarehead, BeephoniX, or Fraunhofer IDMT. It integrates RF detection, radar, optical/thermal cameras, electronic warfare (jamming), and AI-driven software into a modular platform. This is the **market-leading integrated C-UAS solution** and represents the **system-of-systems architecture** that Vietnamese acoustic sensors would need to integrate into — or compete against.

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | DroneShield Limited |
| **HQ** | Sydney, NSW, Australia |
| **US Office** | Virginia, USA |
| **ASX Ticker** | DRO |
| **Founded** | 2014 (Virginia, USA) |
| **Founders** | Brian Hearing, John Franklin (defense industry researchers) |
| **CEO** | Oleg Vornik (joined 2015 as CFO, became CEO) |
| **CTO** | Angus Harris |
| **CPO** | Angus Bean |
| **CFO** | Carla Balanco |
| **CCO** | Louis Gamarra |
| **COO** | Michael Powell (appointed Feb 2026) |
| **Employees** | 100-200+ (exceeded 100 milestone Jan 2024; growing rapidly) |
| **Market Cap** | A$2.9B / US$1.9B (peak 2024) |
| **Revenue** | Record quarterly revenue Q3 2024; $61.6M single European contract (Jun 2025) |
| **IPO** | ASX listing 2016, raised A$7M at A$20M valuation |
| **Status** | Public (ASX:DRO); joined S&P/ASX 200 Index (Sep 2025) |
| **Countries** | Products deployed in 40+ countries |
| **Partners** | 70+ in-country partner nations |
| **Systems Sold** | 4,000+ (as of Sep 2025) |
| **Origin** | Acoustic detection for mosquito control → pivoted to counter-drone |
| **ITAR Status** | Mixed — US components likely ITAR; Australian-sovereign manufacturing |
| **Core IP** | RFAI (RF AI) engine, DroneOptID (computer vision), SensorFusionAI |

### Key Personnel

| Name | Role | Background |
|------|------|------------|
| **Oleg Vornik** | CEO & Managing Director | Joined 2015 as CFO; became CEO |
| **Angus Bean** | Chief Product Officer | Product strategy |
| **Angus Harris** | Chief Technology Officer | Technical leadership |
| **Carla Balanco** | CFO & Joint Company Secretary | Finance |
| **Louis Gamarra** | Chief Commercial Officer | Commercial strategy (appointed Jan 2026) |
| **Michael Powell** | Chief Operating Officer | Global expansion, operations (appointed Feb 2026) |
| **Nathan Vardanega** | Chief Delivery Officer | Program delivery |
| **Carl Norman** | VP Embedded Systems | Hardware engineering |
| **Tom Branstetter** | VP Business Development & Sales (USA) | US market |
| **Terry van Haren DSM** | VP Strategy | Strategic advisory |

### Board Advisors (US Advisory Board)

| Name | Background |
|------|------------|
| **General Mark D. Kelly (Ret.)** | U.S. Air Force (4-star general) |
| **Brig. Gen. Gwyn Armfield (Ret.)** | U.S. Air Force |
| **Anthony P. Reardon (Ret.)** | U.S. Air Force |
| **Lt. Jay Humphlett (Ret.)** | U.S. Navy |
| **Mary Monica Palmer** | Strategic advisor |
| **Christi Cox** | Strategic advisor |

### Historical Timeline

| Year | Event |
|------|-------|
| 2014 | Founded by Brian Hearing and John Franklin (Virginia, USA); acoustic drone detection from mosquito research |
| 2015 | Oleg Vornik joins as CFO |
| 2016 | IPO on ASX (A$7M raised, A$20M valuation); NATO Stock Numbers assigned |
| ~2017-2019 | Product evolution: acoustic → RF → multi-sensor fusion |
| 2020 | DroneShield + Squarehead Discovair integration (DroneSentry-C2) |
| 2021 | US DOD tests DroneShield + Squarehead combined C-UAS |
| 2023 (Jul) | $33M US Government contract; $9.9M DoD contract |
| 2023 (Oct) | DroneSentry-X Mk2 released; SensorFusionAI launched; RADA long-range radar added |
| 2023 (Oct) | Australia supplies DroneShield equipment to Ukraine |
| 2023 (Nov) | Lockheed Martin collaboration announced |
| 2024 (Jan) | Exceeded 100 employees; EFS Kit launched |
| 2024 (Mar) | Added to S&P/ASX All Ordinaries Index |
| 2024 (Oct) | $13.5M US Government contract |
| 2024 (Dec) | $8.2M European contract |
| 2025 (Jan) | $11.8M Asia-Pacific contracts (three contracts) |
| 2025 (Feb) | Joined AUKUS Export Framework |
| 2025 (Mar) | Avalon Airshow: significant upgrade announced; UAS Incident Platform launched |
| 2025 (Apr) | $32.2M Asia-Pacific contracts |
| 2025 (Jun) | **$61.6M European military contract** (all-time record) |
| 2025 (Jul) | LAND 156 LoE 3 initial contracts (Australian Defence) |
| 2025 (Aug) | SentryCiv launched; Ukrainian partnership expanded |
| 2025 (Sep) | **Joined S&P/ASX 200 Index**; surpassed 4,000 systems sold |
| 2025 (Sep) | Sentrycs (cyber takeover) integration |
| 2025 (Oct) | DroneSentry-C2 Enterprise launched; SAPIENT compatibility; South Australia R&D facility |
| 2025 (Oct) | **Platinum Innovators Award** for RFAI Technology |
| 2025 (Nov) | US Advisory Board named (4-star general, flag officers) |
| 2025 (Dec) | $49.6M European military contract; $8.2M Western military; $6.2M Asia-Pacific |
| 2026 (Jan) | Selected for LAND 156 LoE 3 Panel; Intelic European partnership |
| 2026 (Feb) | Michael Powell appointed COO |

### Financial Scale

| Metric | Value |
|--------|-------|
| **Market cap** | A$2.9B peak (2024); ~A$3.5-4B range (ASX 200 member) |
| **Largest single contract** | $61.6M (European military, Jun 2025) |
| **2025 contract total** | >$180M announced contracts |
| **Best-performing ASX 200 stock** | 2024 |
| **Systems sold** | 4,000+ units |
| **Global reach** | 40+ countries, 70+ partner nations |

---

## 2. PRODUCT FAMILY OVERVIEW

```
DroneShield Product Portfolio
│
├── DETECTION (Sensors)
│   ├── DroneSentry-X Mk2 — Core RF detect & defeat unit (46 kg, IP67)
│   │   ├── Detect Only variant (passive, non-emitting)
│   │   └── Detect & Defeat variant (RF jamming)
│   ├── RfPatrol Mk2 — Wearable body-worn RF detector (dismounted troops)
│   ├── SentryCiv — Compact civilian RF detection (critical infrastructure)
│   └── DroneOptID — AI computer vision (camera-agnostic drone identification)
│
├── INTEGRATED SYSTEMS
│   ├── DroneSentry — Fixed-site multi-sensor system (modular: RF + radar + optical)
│   │   ├── Close-range: Bosch MIC 7100i + Echodyne EchoGuard
│   │   ├── Medium-range: OpenWorks Vision Flex + Echodyne EchoShield
│   │   └── Long-range: FLIR HDC Ranger UC + RADA RPS-82
│   ├── EFS Kit — Expeditionary Fixed Site (DroneSentry-X Mk2 on tripod, ~70 kg)
│   └── Immediate Response Kit (IRK) — RfPatrol + DroneGun Mk4
│
├── DEFEAT (Effectors)
│   ├── DroneSentry-X Mk2 (Defeat) — Integrated RF jamming (ISM bands)
│   ├── DroneGun Mk4 — Handheld RF jammer (compact)
│   ├── DroneGun Tactical — Two-hand RF jammer (long range)
│   ├── DroneCannon — Fixed-site RF countermeasure
│   └── Integration: Epirus Leonidas (High-Power Microwave), Sentrycs (cyber takeover)
│
├── SOFTWARE / C2
│   ├── DroneSentry-C2 — Command-and-control platform (on-prem or cloud)
│   ├── DroneSentry-C2 Enterprise — National-scale multi-site monitoring
│   ├── DroneSentry-C2 Tactical — Rugged tablet-based C2 (1.26 kg)
│   ├── RfPatrol-Plugin — ATAK-CIV plugin for geospatial awareness
│   └── Access Portal — Lifecycle support, 3D planning, UAS incident database
│
└── AI / ML ENGINES
    ├── RFAI — RF AI detection engine (150+ drone models, known + unknown)
    ├── RFAI-ATK — ATAK-integrated RF AI
    ├── DroneOptID — Camera-agnostic AI computer vision for UAS ID
    ├── SensorFusionAI — 3D multi-sensor data fusion
    └── ThreatAI — Intelligent threat prioritization
```

### Product Evolution

| Generation | Period | Focus | Key Advance |
|-----------|--------|-------|-------------|
| Gen 1 | 2014-2016 | Acoustic detection | Drone sound signature matching |
| Gen 2 | 2016-2019 | RF detection | Radio frequency drone signal detection |
| Gen 3 | 2019-2023 | Multi-sensor fusion | RF + radar + optical + AI |
| **Gen 4** | **2023-present** | **Software-defined, AI-native** | **RFAI engine, SensorFusionAI, modular architecture** |

---

## 3. DRONESENTRY SYSTEM ARCHITECTURE

### 3.1 System Topology

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        DRONESENTRY SYSTEM                                  │
│                                                                          │
│  DETECTION LAYER                    IDENTIFICATION LAYER                  │
│  ┌──────────────────┐              ┌──────────────────────┐              │
│  │ DroneSentry-X Mk2│              │ DroneOptID (AI CV)    │              │
│  │ • RFAI engine     │              │ • Camera-agnostic     │              │
│  │ • 150+ drone DB   │              │ • Detect/verify/track │              │
│  │ • RF direction    │              │ • Real-time AI        │              │
│  │ • Hemispheric     │              └──────────────────────┘              │
│  └──────────────────┘                       │                             │
│           │                                 │                             │
│  ┌──────────────────┐              ┌──────────────────────┐              │
│  │ Radar             │              │ SensorFusionAI        │              │
│  │ • Echodyne Guard  │─────────────→│ • 3D data fusion      │              │
│  │ • Echodyne Shield │              │ • Multi-sensor corr.  │              │
│  │ • RADA RPS-82     │              │ • Track management    │              │
│  └──────────────────┘              └──────────────────────┘              │
│           │                                 │                             │
│  ┌──────────────────┐                       ▼                             │
│  │ Optical/Thermal   │              ┌──────────────────────┐              │
│  │ • Bosch MIC 7100i │              │ DroneSentry-C2        │              │
│  │ • OpenWorks Flex  │              │ • Unified UI          │              │
│  │ • FLIR HDC Ranger │              │ • ThreatAI priority   │              │
│  └──────────────────┘              │ • SAPIENT compatible  │              │
│                                    │ • MIL-STD-2525       │              │
│  DEFEAT LAYER                      │ • RESTful API         │              │
│  ┌──────────────────┐              │ • Cloud or on-prem    │              │
│  │ RF Jamming        │              └──────────────────────┘              │
│  │ • DroneSentry-X   │                       │                             │
│  │   (defeat mode)   │              ┌────────┴─────────┐                  │
│  │ • DroneCannon     │              │                  │                  │
│  │ • DroneGun Mk4    │              ▼                  ▼                  │
│  │ • DroneGun Tact.  │         C2 Enterprise    C2 Tactical              │
│  ├──────────────────┤         (multi-site,     (rugged tablet,            │
│  │ Cyber Takeover    │          national)       dismounted)               │
│  │ • Sentrycs        │                                                    │
│  ├──────────────────┤                                                    │
│  │ Kinetic / HPM     │                                                    │
│  │ • Epirus Leonidas │                                                    │
│  └──────────────────┘                                                    │
└──────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Sensor Layers — Layered Defense Approach

| Layer | Sensor | Range | Function | Partner/OEM |
|-------|--------|-------|----------|-------------|
| **RF Detection** | DroneSentry-X Mk2 (RFAI) | Several km (est. 3-8 km) | Passive RF scanning; detect drone comms | DroneShield proprietary |
| **Short-range radar** | Echodyne EchoGuard | ~1.5 km | MESA radar, small drone detection | Echodyne (USA) |
| **Medium-range radar** | Echodyne EchoShield | ~3-5 km | MESA radar, wider area | Echodyne (USA) |
| **Long-range radar** | RADA RPS-82 | 5-20 km | 4D AESA pulse-Doppler radar | RADA/Leonardo DRS (Israel) |
| **Close-range optical** | Bosch MIC IP Starlight 7100i | ~500 m | PTZ camera, visual verification | Bosch (Germany) |
| **Medium-range optical** | OpenWorks Vision Flex | ~2-3 km | EO/IR tracker | OpenWorks (UK) |
| **Long-range optical** | FLIR HDC Ranger UC | 5+ km | Long-range thermal/visible | Teledyne FLIR (USA) |
| **AI Computer Vision** | DroneOptID | Camera-agnostic | Drone detection from any camera feed | DroneShield proprietary |

### 3.3 Detection Principle: Multi-Modal RF + Radar + Optical

Unlike the acoustic-only systems previously analyzed, DroneShield's approach layers **three fundamentally different sensing modalities**:

**Layer 1: RF Detection (RFAI) — First Alert**
- Passively scans radio frequency spectrum for drone control signals
- RFAI engine identifies 150+ drone models using AI/ML
- Detects both known and unknown drones
- Provides drone + controller location (DroneLocator technology)
- Completely passive (no emissions)

**Layer 2: Radar — Track Confirmation**
- Active radar (AESA or MESA) provides 3D track data
- Speed, altitude, heading, range
- Works against RF-silent drones (autonomous, fiber-optic)
- Ranges from 1.5 km (EchoGuard) to 20 km (RADA RPS-82)

**Layer 3: Optical/Thermal — Visual ID**
- Camera (EO/IR) provides visual confirmation
- DroneOptID AI classifies drone type from camera feed
- Evidence capture for legal/forensic purposes
- Slew-to-cue from RF/radar bearing

**Fusion: SensorFusionAI**
- Correlates RF, radar, and optical data into unified 3D tracks
- Reduces false positives through multi-sensor confirmation
- Growing threat level as more data layers confirm detection

```
DRONESENTRY DETECTION TIMELINE:

Time ──────────────────────────────────────────────────────→

RF (RFAI)     ████████████████████████████████████████████████
              "Drone signal detected at bearing 045°"
              (passive, first alert, km-range)

Radar         ░░░░░████████████████████████████████████████
              "Confirmed: target at 2.3 km, alt 120m, heading 225°"
              (active, 3D track, confirms RF alert)

Optical       ░░░░░░░░░░░████████████████████████████████
              "Visual: DJI Mavic 3 identified at 1.1 km"
              (visual ID, AI classification, evidence)

SensorFusion  ░░░░░░░░░░░░░░████████████████████████████
              "HIGH CONFIDENCE THREAT — all three layers confirm"
              (correlated 3D track, automated response option)

Defeat        ░░░░░░░░░░░░░░░░░░██████████████████████
              "RF jamming engaged — drone RTH/land"
              (operator-authorized or automatic)
```

---

## 4. DETAILED COMPONENT SPECIFICATIONS

### 4.1 DroneSentry-X Mk2 (Core RF Unit)

| Parameter | Specification | Source |
|-----------|--------------|--------|
| **Function** | RF detection + optional RF disruption | Official |
| **Detection method** | RFAI (AI-powered RF scanning) | Official |
| **Drone database** | 150+ drone models (RFAI engine) | Official |
| **Unknown drone detection** | Yes (AI pattern recognition) | Official |
| **DroneLocator** | Drone + controller coordinates, altitude, velocity | Official |
| **Coverage** | Hemispheric (full hemisphere) | Official |
| **Bearing** | Directional (cardinal) bearing identification | Official |
| **Detection range** | Not disclosed (estimated 3-8 km for RF) | Estimated |
| **Disruption** | Software-defined RF jamming (ISM bands) | Official |
| **Dimensions** | 710 x 710 x 532 mm (antenna-mounted) | Official |
| **Weight** | **46 kg** (device only) | Official |
| **Operating temp** | -20°C to +50°C | Official |
| **IP rating** | **IP67** | Official |
| **Output** | Audio + visual alerts, JSON, gRPC, TAK compatible | Official |
| **Mounting** | Vehicle roof-rack, mast, tripod | Official |
| **Shock/vibration** | MIL-STD rated (ruggedized) | Official |
| **Warranty** | 12 months (extendable) | Official |

### 4.2 DroneSentry-C2 (Command & Control)

| Parameter | Specification |
|-----------|--------------|
| **Platform** | Web-based or desktop application |
| **Deployment** | Cloud-hosted or on-premises (air-gapped) |
| **On-prem server** | 2RU, Intel Xeon Silver 4510 x2, 32GB RAM, TAA compliant |
| **Server dimensions** | 87mm (H) x 482mm (W) x 772mm (D) |
| **Server weight** | 36.1 kg |
| **Sensor compatibility** | Bosch, Echodyne, Leonardo DRS, RADA, Teledyne FLIR, Sentrycs, ADS-B |
| **Map services** | MAXAR, Maptiler, Bing, Google Maps, Esri, Nearmap (optional) |
| **Protocols** | SAPIENT, MIL-STD-2525 iconography, MGRS, RESTful API, Cursor-on-Target |
| **Software updates** | Quarterly |
| **Digital Twin** | 3D planning tool for site deployment simulation |

### 4.3 DroneSentry-C2 Tactical (Rugged Tablet)

| Parameter | Specification |
|-----------|--------------|
| **Processor** | Intel i7 (10 core) |
| **Memory** | 32GB RAM |
| **Storage** | 1TB SSD |
| **OS** | Linux |
| **Dimensions** | 203 x 296 x 23.9 mm |
| **Weight** | 1.26 kg (excluding accessories) |
| **Compliance** | IP65, MIL-STD-461 (emissions) |
| **Networks** | Ethernet, wireless, mesh radio (Silvus, Persistent Systems), 4G |
| **Compatible** | RfPatrol Mk2, DroneSentry-X, DroneSentry-X Mk2 |

### 4.4 EFS Kit (Expeditionary Fixed Site)

| Parameter | Specification |
|-----------|--------------|
| **Total weight** | ~70 kg (DroneSentry-X Mk2 + bracket + tripod) |
| **Assembly** | Tool-less, <10 minutes, no specialized training |
| **Operating temp** | -20°C to +55°C |
| **IP rating** | IP67 (unit, cases, cables) |
| **UI** | Ruggedized tablet + DroneSentry-C2 Tactical |
| **Output** | JSON, gRPC, TAK, Cursor on Target |
| **Disruption** | Software-defined |

### 4.5 Third-Party Radar Options

| Radar | Type | Range | Manufacturer | Key Feature |
|-------|------|-------|-------------|-------------|
| **Echodyne EchoGuard** | MESA | ~1.5 km | Echodyne (USA) | Compact, metamaterial antenna |
| **Echodyne EchoShield** | MESA | ~3-5 km | Echodyne (USA) | Medium-range, wider FoV |
| **RADA RPS-82 (ieMHR)** | 4D AESA Pulse-Doppler | 5-20 km | Leonardo DRS RADA (Israel) | Long-range, multi-mission |

---

## 5. CORE TECHNOLOGY DEEP DIVE

### 5.1 RFAI (Radio Frequency Artificial Intelligence)

RFAI is DroneShield's **most important IP** — the AI engine that detects drone RF emissions:

| Feature | Detail |
|---------|--------|
| **Purpose** | Detect and identify drones via their RF control signals |
| **Database** | 150+ drone models recognized |
| **Unknown drones** | AI pattern recognition detects novel/unknown drones |
| **Encrypted signals** | RFAI can detect even encrypted drone communications |
| **Update cadence** | Continuous database updates as new drones appear |
| **Passive** | Non-emitting; cannot be detected |
| **Output** | Drone model, controller location, drone position, altitude, velocity |
| **Award** | Platinum Innovators Award (Military & Aerospace Electronics, 2025) |

### 5.2 DroneOptID (AI Computer Vision)

| Feature | Detail |
|---------|--------|
| **Purpose** | Detect, identify, and track UAS using cameras |
| **Camera dependency** | Camera-agnostic (works with any EO/IR camera) |
| **AI model** | Purpose-built for UAS detection (not general object detection) |
| **Origin** | Developed with UTS (University of Technology Sydney) under Defence Innovation Network grant |
| **Real-time** | Real-time drone tracking and classification |
| **Integration** | Works with DroneSentry-C2 and third-party systems |

### 5.3 SensorFusionAI

| Feature | Detail |
|---------|--------|
| **Purpose** | Fuse data from RF, radar, optical, and third-party sensors |
| **3D fusion** | Creates unified 3D operating picture |
| **Sensor-agnostic** | Works with any sensor data inputs |
| **Launched** | October 2023 |
| **Benefit** | Reduces false positives; increases detection confidence |

### 5.4 Electronic Warfare / Defeat

| Capability | Method | Detail |
|-----------|--------|--------|
| **RF Jamming** | Software-defined disruption | Disrupts drone control links on ISM frequencies |
| **GNSS denial** | GPS/GLONASS/Galileo jamming | Forces drone to lose navigation |
| **Anti-swarming** | Multiple simultaneous targets | Disables swarms within effective range |
| **Cyber takeover** | Protocol-level control (Sentrycs) | Controlled landing of captured drone |
| **High-Power Microwave** | Epirus Leonidas integration | Kinetic-effect electronic defeat |
| **Handheld defeat** | DroneGun Mk4 / Tactical | Man-portable RF jammer |

---

## 6. PATENTS & INTELLECTUAL PROPERTY

### 6.1 Granted Patents (DroneShield LLC — US)

| Patent | Title | Filed | Granted | Inventors |
|--------|-------|-------|---------|-----------|
| **US 10,032,464** | Drone detection and classification with compensation for background clutter | 2016-11-23 | 2018-07-24 | Franklin, Hearing |
| **US 9,858,947** | Drone detection and classification methods and apparatus | 2015-11-24 | 2018-01-02 | Hearing, Franklin |
| **US 9,704,508** | Drone detection and classification methods and apparatus | 2015-11-24 | 2017-07-11 | Hearing, Franklin |
| **US 9,697,850** | Drone detection and classification methods and apparatus | 2015-11-24 | 2017-07-04 | Hearing, Franklin |
| **US 9,275,645** | Drone detection and classification methods and apparatus | 2014-04-22 | 2016-03-01 | Hearing, Franklin |

### 6.2 Patent Analysis

All five patents cover **acoustic drone detection** — the company's original technology:

| Patent Claim | Method | VN-CUAS Relevance |
|-------------|--------|-------------------|
| Sound sample segmentation + frequency/PSD transform | Acoustic feature extraction | MEDIUM — similar to Fraunhofer fingerprint approach |
| Drone sound signature database matching | Template matching classification | MEDIUM — common technique |
| Background clutter compensation | Noise suppression for acoustic detection | HIGH — critical for real-world deployment |
| Broad spectrum matching for classification | Frequency spectrum comparison | MEDIUM — general audio ML |

**Key insight:** DroneShield's patents are all **acoustic detection** patents from the founding era (2014-2016). Their current core IP — RFAI, DroneOptID, SensorFusionAI — appears to be protected through **trade secrets** (AI model weights, training data, algorithms) rather than patents. This suggests:
1. The acoustic detection technology is not their current competitive advantage
2. The RF AI and computer vision technology is where the real value lies
3. Vietnamese acoustic detection development is unlikely to infringe DroneShield patents (different approach)

### 6.3 IP Freedom to Operate for VN-CUAS

| Technology | Status | Freedom to Operate |
|------------|--------|-------------------|
| Acoustic drone signature matching | Patented by DroneShield (general concept) | **DESIGN AROUND** — use different classification method |
| Background clutter compensation | Patented (US 10,032,464) | **CHECK** — specific method may be avoidable |
| RF drone signal detection | Not patented by DroneShield (trade secret) | **FREE** — general RF scanning is not patentable |
| AI computer vision for drones | Trade secret (DroneOptID) | **FREE** — train own model |
| Multi-sensor fusion | General concept not patentable | **FREE** |
| Beamforming (Squarehead) | Patented by Squarehead (array geometry) | **DESIGN AROUND** |
| MEMS microphone arrays (general) | Public domain | **FREE** |

---

## 7. KNOWN CONTRACTS & DEPLOYMENTS

### 7.1 Major Contracts (2023-2026)

| Date | Customer | Value | Detail |
|------|----------|-------|--------|
| Jul 2023 | **US Government** | **$33M** | Largest DoD contract at that time |
| Jul 2023 | US DoD | $9.9M | Separate DoD order |
| Oct 2024 | US Government | $13.5M | Follow-on US contract |
| Dec 2024 | European military | $8.2M | European NATO flank |
| Jan 2025 | Asia-Pacific (3x) | $11.8M | Three separate APAC military customers |
| Jan 2025 | Latin America | $9.7M | Latin American military |
| Apr 2025 | Asia-Pacific | $32.2M | New APAC contracts |
| **Jun 2025** | **European military** | **$61.6M** | **All-time record single contract** |
| Jul 2025 | Australia (LAND 156) | TBD | Australian Defence Force C-UAS program |
| Sep 2025 | Various | $7.9M | Pushed past 4,000 systems milestone |
| Dec 2025 | European military | $49.6M | Major European order |
| Dec 2025 | Western military | $8.2M | Handheld systems + software |
| Dec 2025 | Asia-Pacific | $6.2M | Via in-country reseller |

### 7.2 Strategic Agreements

| Partner | Type | Detail |
|---------|------|--------|
| **NATO NSPA** | Framework agreement | First-ever C-UAS procurement framework (3-year) |
| **AUKUS** | Export framework | Joined AUKUS Export Framework (Feb 2025) |
| **Lockheed Martin** | Collaboration | C-UAS technology integration (Nov 2023) |
| **Ukraine** | Operational deployment | Active frontline C-UAS support (since 2023) |
| **BT Group (UK)** | Distribution | UK market partnership |
| **Intelic** | European partner | Modular European C-UAS (Jan 2026) |
| **Sentrycs** | Technology integration | Cyber takeover capability |
| **Epirus** | Technology integration | High-Power Microwave effector |
| **Squarehead Technology** | Sensor integration | Discovair acoustic sensor in DroneSentry-C2 |

### 7.3 Market Reach

| Region | Presence |
|--------|----------|
| **Australia** | HQ, manufacturing, LAND 156 program |
| **USA** | Virginia office, DoD contracts, US Advisory Board |
| **Europe** | NATO flank deployments, €49.6M+ contracts |
| **Asia-Pacific** | Multiple military customers ($32M+) |
| **Latin America** | $9.7M+ contracts, dedicated regional director |
| **Ukraine** | Active operational deployment |
| **Middle East** | In-country partners |
| **UK** | BT Group distribution |

---

## 8. PERFORMANCE COMPARISON — Multi-Sensor C-UAS Systems

| Feature | DroneShield DroneSentry | Dedrone DroneTracker | Rafael Drone Dome | D-Fend EnforceAir |
|---------|------------------------|---------------------|-------------------|--------------------|
| **Country** | Australia | Germany/USA | Israel | Israel |
| **Detection: RF** | **RFAI (150+ models)** | RF analysis | RF scanning | RF analysis (cyber) |
| **Detection: Radar** | RADA, Echodyne (3rd party) | Optional | AESA radar | Optional |
| **Detection: Optical** | Multiple (AI DroneOptID) | Camera + acoustic | EO/IR | Optional |
| **Detection: Acoustic** | Via Squarehead Discovair | Proprietary | No | No |
| **Defeat: RF Jam** | **Yes** | No (detect only) | Yes | No |
| **Defeat: Cyber** | **Yes (Sentrycs)** | No | No | **Yes (primary)** |
| **Defeat: Kinetic/HPM** | **Yes (Epirus)** | No | **Yes (laser)** | No |
| **C2 Platform** | **DroneSentry-C2** | DedroneTracker | C4I | EnforceAir Console |
| **SAPIENT** | **Yes** | Unknown | Unknown | Unknown |
| **NATO integration** | **Framework agreement** | Unknown | Unknown | Unknown |
| **Systems sold** | **4,000+** | ~1,000+ (est.) | Unknown | Unknown |
| **Weight (core RF)** | 46 kg | ~5-10 kg (est.) | System-level | ~15 kg (est.) |
| **IP rating** | **IP67** | IP65 | MIL-STD | IP65 |
| **ASX/public** | **ASX:DRO** | Private | Part of Rafael | Private |
| **Market cap** | **A$2.9B** | N/A | N/A | N/A |

---

## 9. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 9.1 Overall Function

```
┌──────────────────────────────────────────────────────────────────────┐
│                        DRONESENTRY SYSTEM                              │
│                                                                      │
│  INPUT:                            OUTPUT:                           │
│  • RF signals (drone comms)        • Drone detection alerts          │
│  • Radar returns                   • Drone + controller positions    │
│  • Optical/thermal images          • Drone type classification       │
│  • Power (AC mains / battery)      • 3D fused track data             │
│  • Network connection              • Defeat commands (jamming)       │
│                                    • Unified C2 operating picture    │
│  FUNCTION:                         • After-action reports            │
│  "Detect, identify, track,                                           │
│   and defeat unauthorized                                            │
│   drones using multi-sensor                                          │
│   fusion and layered defense"                                        │
└──────────────────────────────────────────────────────────────────────┘
```

### 9.2 Sub-Function Structure

```
F0: Detect, Identify, Track & Defeat Unauthorized Drones
│
├── F1: RF SENSE (DroneSentry-X Mk2 / RFAI)
│   ├── F1.1: Passively scan RF spectrum for drone signals
│   ├── F1.2: Match signal to RFAI drone database (150+ models)
│   ├── F1.3: Detect unknown drones via AI pattern recognition
│   ├── F1.4: Determine drone bearing (hemispheric)
│   ├── F1.5: Locate drone + controller position (DroneLocator)
│   └── F1.6: Detect encrypted drone communications
│
├── F2: RADAR TRACK (Third-party radars)
│   ├── F2.1: Emit radar pulses and receive returns
│   ├── F2.2: Detect micro-Doppler signature of rotating propellers
│   ├── F2.3: Calculate 3D position (range, azimuth, elevation)
│   ├── F2.4: Track velocity, altitude, heading
│   └── F2.5: Detect RF-silent drones (autonomous, fiber-optic)
│
├── F3: OPTICAL IDENTIFY (Camera + DroneOptID)
│   ├── F3.1: Slew camera to RF/radar-cued bearing
│   ├── F3.2: Capture EO/IR imagery of target
│   ├── F3.3: Run DroneOptID AI classification
│   ├── F3.4: Visually confirm drone type and payload
│   └── F3.5: Capture forensic evidence imagery
│
├── F4: FUSE (SensorFusionAI)
│   ├── F4.1: Correlate RF, radar, optical tracks
│   ├── F4.2: Create unified 3D target track
│   ├── F4.3: Compute composite threat confidence
│   ├── F4.4: Manage multiple simultaneous tracks (swarm)
│   └── F4.5: Feed fused data to C2
│
├── F5: COMMAND (DroneSentry-C2)
│   ├── F5.1: Display unified operating picture
│   ├── F5.2: Provide threat prioritization (ThreatAI)
│   ├── F5.3: Enable operator decision-making
│   ├── F5.4: Interface with external C2 (SAPIENT, TAK)
│   ├── F5.5: Log detections for after-action review
│   └── F5.6: Multi-site monitoring (C2 Enterprise)
│
├── F6: DEFEAT (Electronic Warfare)
│   ├── F6.1: RF jamming of drone control links (ISM bands)
│   ├── F6.2: GNSS denial (GPS/GLONASS spoofing)
│   ├── F6.3: Cyber takeover and forced landing (Sentrycs)
│   ├── F6.4: High-power microwave (Epirus Leonidas)
│   ├── F6.5: Anti-swarm simultaneous multi-target jamming
│   └── F6.6: Automatic or manual engagement modes
│
└── F7: SUSTAIN (Lifecycle)
    ├── F7.1: Quarterly software/firmware updates
    ├── F7.2: RFAI database updates (new drone models)
    ├── F7.3: Remote diagnostics and support
    ├── F7.4: Training portal and documentation
    └── F7.5: 3D mission planning tool
```

---

## 10. BOM ESTIMATE (For Comparison — NOT Vietnamese Production Target)

### 10.1 DroneSentry System-Level Cost Estimate

DroneShield's DroneSentry is a **system integrator** product — it bundles proprietary RF hardware with third-party radars, cameras, and effectors. Estimated system costs:

| Configuration | Components | Est. Cost (USD) |
|--------------|-----------|-----------------|
| **Core RF (DroneSentry-X Mk2)** | RF sensor + RFAI engine + edge compute | $50K-100K (est.) |
| **Close-range package** | Mk2 + Bosch camera + EchoGuard radar + C2 | $100K-200K (est.) |
| **Medium-range package** | Mk2 + OpenWorks + EchoShield + C2 | $200K-400K (est.) |
| **Long-range package** | Mk2 + FLIR + RADA RPS-82 + C2 | $500K-1M+ (est.) |
| **Defeat add-on** | RF jamming module | $30K-80K (est.) |
| **C2 on-prem server** | Intel Xeon 2RU server + software | $30K-50K (est.) |
| **Handheld (DroneGun Mk4)** | Portable RF jammer | $30K-60K (est.) |

### 10.2 Cost Positioning vs Vietnamese Acoustic Sensor

| System | Est. Price/Unit | Detection Method | Range | Weight |
|--------|----------------|------------------|-------|--------|
| **DroneSentry (full system)** | $200K-1M+ | RF + radar + optical | 1-20 km | System-level |
| **DroneSentry-X Mk2 (RF only)** | $50K-100K | RF only | 3-8 km (est.) | 46 kg |
| **Squarehead G2+ (acoustic)** | $15K-50K | Acoustic beamforming | 0.3-1 km | 8 kg |
| **BeephoniX M2 (acoustic)** | $5K-15K | Acoustic bio-inspired | 0.2-0.9 km | 950 g |
| **VN-CUAS target (acoustic)** | **$2K-5K** | Acoustic + ML | 0.5-0.8 km | 1-2 kg |

**Key insight:** Vietnamese acoustic C-UAS at $2K-5K is **10-100x cheaper** than DroneSentry but covers a fundamentally different (shorter range, NLOS) detection niche. The two are **complementary, not competing** — acoustic is the low-cost, low-power first-alert layer that cues expensive RF/radar/optical systems.

---

## 11. DESIGN INSIGHTS FOR VN-CUAS

### 11.1 Key Lessons from DroneShield

1. **The C-UAS market demands multi-sensor fusion, not single-sensor solutions** — DroneShield's dominance comes from integrating RF + radar + optical + AI into one platform. No single sensor technology (acoustic, RF, radar, or camera) alone provides adequate C-UAS protection. Vietnamese acoustic sensors must be designed as **one layer in a multi-sensor architecture**.

2. **Software is the real product, hardware is the vessel** — DroneShield's core value is RFAI, DroneOptID, SensorFusionAI, and ThreatAI — all software/AI. The hardware is commodity or third-party (Echodyne, RADA, Bosch, FLIR). Vietnamese development should invest heavily in **AI/ML algorithms** (acoustic fingerprint, classification, fusion) rather than custom hardware.

3. **SAPIENT compatibility is essential for military customers** — DroneSentry-C2 supports SAPIENT (NATO standard for autonomous sensor integration). Vietnamese C-UAS must implement SAPIENT protocol to be interoperable with NATO/allied systems.

4. **Acoustic detection fills the NLOS gap that RF/radar/camera cannot** — DroneShield integrated Squarehead Discovair into DroneSentry specifically because acoustics "hears around corners" where RF/radar/camera have blind spots. This validates acoustic detection as a **high-value complementary layer** in Vietnamese defense architecture.

5. **DroneShield started with acoustics then pivoted** — Founded on acoustic drone detection (2014 patents), DroneShield evolved to RF-centric detection because RF offers longer range and more information (drone model, controller location). However, acoustic detection remains relevant for RF-silent threats (fiber-optic, autonomous drones). This pivot suggests Vietnamese development should plan for **acoustic-first, RF-addition later**.

6. **4,000+ systems sold proves market demand** — The C-UAS market is real and growing rapidly. DroneShield's $180M+ in 2025 contracts alone demonstrates massive demand. Even a small share of this market with affordable acoustic sensors could be significant for Vietnam.

7. **Quarterly software updates are the business model** — DroneShield delivers quarterly firmware/software updates to all customers. This SaaS-like approach ensures continuous improvement and recurring revenue. Vietnamese C-UAS should adopt similar continuous update architecture.

8. **RESTful API + TAK + SAPIENT = interoperability** — DroneSentry outputs data via JSON, gRPC, TAK (Cursor on Target), SAPIENT, and RESTful APIs. Vietnamese acoustic sensors must support at least TAK and SAPIENT for integration into existing military C2 infrastructure.

9. **IP67 is the environmental standard** — DroneSentry-X Mk2 is IP67 rated (submersible). This is higher than the IP65 typical of acoustic sensors. Vietnamese product should target IP67 for competitive environmental performance.

10. **The EFS Kit concept (tool-less <10 min assembly) defines deployability** — The Expeditionary Fixed Site Kit transforms DroneSentry-X Mk2 into a field-deployable system in under 10 minutes with no tools. Vietnamese acoustic system should target similar rapid deployment.

### 11.2 Vietnamese Acoustic Sensor Position in DroneShield-Type Architecture

```
INTEGRATED C-UAS ARCHITECTURE (Vietnamese Future)
│
├── LAYER 1: ACOUSTIC DETECTION (VN-CUAS — Vietnamese Indigenous)
│   • 128-256 MEMS array, <10W, battery/solar
│   • "Hears around corners" — NLOS detection
│   • 500-800m range, <5° bearing accuracy
│   • ML classification (acoustic fingerprint)
│   • Cost: $2K-5K per sensor
│   • Role: First alert, wake-up trigger, NLOS coverage
│   • Detects: RF-silent drones, fiber-optic, autonomous
│
├── LAYER 2: RF DETECTION (Import or Future Indigenous Development)
│   • Passive RF scanning for drone control signals
│   • Longer range (3-8 km)
│   • Drone + controller location
│   • Cost: $50K-100K per unit
│   • Role: Primary detection for RF-emitting drones
│
├── LAYER 3: RADAR (Import — RADA, Echodyne, or equivalent)
│   • Active radar for 3D tracking
│   • 1.5-20 km range (size-dependent)
│   • Cost: $50K-500K per unit
│   • Role: Track confirmation, RF-silent drone detection
│
├── LAYER 4: OPTICAL/THERMAL (Import or Local Integration)
│   • EO/IR camera with AI classification
│   • Visual ID and evidence capture
│   • Cost: $5K-100K per unit
│   • Role: Visual confirmation, slew-to-cue
│
├── FUSION: SENSOR FUSION SOFTWARE (Vietnamese Indigenous)
│   • Correlate acoustic + RF + radar + optical
│   • Unified 3D operating picture
│   • SAPIENT + TAK output
│   • Cost: Software development investment
│   • Role: Integrated situation awareness
│
└── DEFEAT (Import or Separate Program)
    • RF jamming, GNSS denial
    • Requires separate authorization/licensing
    • Cost: $30K-100K per system
    • Role: Active countermeasure
```

### 11.3 Updated VN-CUAS Product Concept v4.0

```
VN-CUAS Product Architecture v4.0
(Cumulative from Squarehead + BeephoniX + Fraunhofer + DroneShield insights)
│
├── SENSOR UNIT: Optimized Acoustic Array
│   • 128-256 MEMS digital microphones
│   • Weight: 1-2 kg
│   • Power: <10W (battery/solar)
│   • IP67 (upgraded from IP65 — match DroneShield standard)
│   • MIL-STD-810H target
│   • On-edge processing with ML
│   • ITAR-free components
│
├── ALGORITHMS: Three-Layer Processing Stack
│   ├── L1: Signal Enhancement (Fraunhofer-inspired)
│   ├── L2: Beamforming + Localization (Squarehead/BeephoniX-inspired)
│   └── L3: ML Classification (acoustic fingerprint + CNN + RNN)
│
├── INTEGRATION: Multi-Sensor Architecture (DroneShield-inspired)
│   • RESTful API for C2 integration
│   • SAPIENT protocol (NATO interoperability)
│   • TAK/ATAK compatible (Cursor on Target)
│   • JSON + gRPC output (match DroneSentry format)
│   • Designed as "acoustic layer" in layered defense
│   • Sensor wake-up trigger for RF/radar/camera (Fraunhofer concept)
│
├── DEPLOYMENT: Rapid Field Setup
│   • Tool-less assembly <10 minutes (match DroneShield EFS Kit)
│   • Tripod, mast, vehicle, building-mount options
│   • Body-worn display option (phone/tablet)
│   • Mesh networking for multi-sensor coverage
│
├── DETECTION TARGETS:
│   • FPV drones: 500-800m
│   • Commercial drones (DJI class): 200-400m
│   • Large UAVs (Shahed class): 1+ km
│   • NLOS detection: 50-150m (unique vs RF/radar/camera)
│   • RF-silent drones: Primary advantage over RF detection
│   • Direction accuracy: <5°
│   • Update rate: <0.5 seconds
│
├── ACOUSTIC FINGERPRINT DATABASE:
│   • Build Vietnamese drone signature library
│   • DJI series, FPV, military, Chinese commercial
│   • Environmental noise profiles (tropical, urban, border)
│
├── POWER: Tropical-Optimized
│   • Li-ion battery: 10+ hours @ <10W
│   • Solar: 50W panel for persistent deployment
│   • External 12-48 VDC for fixed sites
│   • Sensor wake-up: 95%+ power savings on secondary sensors
│
└── COST TARGET:
    • Single acoustic sensor: $2K-5K
    • 4-sensor perimeter kit: $10K-20K
    • Complementary to $200K+ multi-sensor C-UAS systems
    • Position: Affordable wide-area first-alert layer
```

---

## 12. INTELLIGENCE GAPS

| Gap | Impact | Workaround |
|-----|--------|-----------|
| DroneSentry-X Mk2 RF detection range (exact km) | High | Not disclosed; estimate 3-8 km from industry benchmarks |
| RFAI engine architecture and training methodology | High for RF development | Not relevant for acoustic sensor; proprietary AI |
| System pricing (exact per-unit costs) | Medium for business case | Estimate from contract values / system counts |
| DroneOptID model architecture | Low for acoustic project | Camera AI is separate domain |
| Specific ISM frequency bands for jamming | Medium | Standard ISM: 2.4 GHz, 5.8 GHz, 900 MHz, 1.2 GHz |
| Acoustic sensor integration details (Squarehead in DroneSentry) | High for integration planning | Likely API-based; design own integration layer |
| SensorFusionAI correlation algorithm | Medium | Implement standard multi-hypothesis tracking |
| SAPIENT protocol specification details | High for interoperability | Available through NATO channels |
| Export control restrictions to Vietnam | **Critical** | DroneShield products likely export-controlled; focus on indigenous development |
| DroneShield's acoustic detection patent enforceability in Vietnam | Low | Vietnamese patent jurisdiction different from US |

---

## 13. REFERENCES

### Public Sources Used

| # | Source | Type | Key Data |
|---|--------|------|----------|
| 1 | droneshield.com/c-uas-products/dronesentry | Product page | System architecture, layered defense configurations |
| 2 | droneshield.com/products-on-the-move | Product page | DroneSentry-X Mk2 specs: 46 kg, IP67, -20 to +50°C |
| 3 | droneshield.com/products-software | Product page | C2 platform specs, server details, compatibility |
| 4 | droneshield.com/about-droneshield | Corporate | Leadership team, company timeline, founding story |
| 5 | droneshield.com/capabilities | Technology | RFAI, DroneOptID, SensorFusionAI, EW capabilities |
| 6 | en.wikipedia.org/wiki/DroneShield | Encyclopedia | History, founding, market cap, deployments |
| 7 | patents.justia.com/assignee/droneshield-llc | Patents | 5 acoustic detection patents (US 9,275,645 through US 10,032,464) |
| 8 | cuashub.com/en/product/dronesentry | Industry database | Product overview, DroneCannon integration |
| 9 | dronelife.com | News | $6.2M Asia-Pacific contract details |
| 10 | army-technology.com | News | $8.2M Western military contract |
| 11 | asdnews.com | News | C2 Enterprise launch, SAPIENT, MIL-STD-2525 |
| 12 | janes.com | Defense intel | RADA RPS-82 integration, Avalon 2025 launch |
| 13 | everythingrf.com | Product database | DroneSentry-X Mk2 listing |
| 14 | fintechpulse.co.uk | Business analysis | RFAI as core IP, SaaS model, threat database |
| 15 | innovationaus.com | News | NATO framework agreement signed |

### Cross-References (VN-CUAS-001 Project)

| RE Analysis | Key Comparison Point |
|-------------|---------------------|
| [[RE_squarehead_discovair_g2plus]] | Acoustic sensor integrated INTO DroneShield DroneSentry-C2 |
| [[RE_beephonix_m2]] | Ultra-light acoustic competitor; complementary to RF-based systems |
| [[RE_fraunhofer_idmt_acoustic_drone_detection]] | Sensor wake-up architecture; algorithm-centric approach |

---

## 14. COMPARATIVE SUMMARY: ACOUSTIC vs MULTI-SENSOR C-UAS

| Dimension | VN-CUAS (Acoustic) | DroneShield DroneSentry (Multi-Sensor) | Relationship |
|-----------|--------------------|-----------------------------------------|-------------|
| **Detection method** | Acoustic beamforming + ML | RF + radar + optical + AI | **Complementary** |
| **Range** | 0.5-0.8 km | 1-20 km | Different coverage tiers |
| **NLOS capability** | **Yes** | No (requires LOS) | **Acoustic advantage** |
| **RF-silent drones** | **Yes** | Limited (radar only) | **Acoustic advantage** |
| **Drone identification** | Sound classification | RF model ID + visual | Different methods |
| **Controller location** | No | **Yes** (DroneLocator) | DroneShield advantage |
| **Defeat capability** | No | **Yes** (jamming, cyber, HPM) | Different roles |
| **Weight** | 1-2 kg | 46-70 kg | Acoustic much lighter |
| **Power** | <10W (battery) | AC mains or large battery | Acoustic much lower |
| **Cost** | **$2K-5K** | $200K-1M+ | **100x cost difference** |
| **Deployment density** | High (many cheap sensors) | Low (few expensive systems) | Different coverage models |
| **Integration** | As sensor layer in C2 | **As complete C2 system** | Acoustic feeds into DroneShield-type C2 |

---

*Analysis compiled from publicly available sources only. No classified, ITAR-controlled, or proprietary information included. All specifications are estimates based on published data, news articles, corporate websites, patent filings, and industry comparisons.*

*Created: 2026-02-11 | Project: VN-CUAS-001 | Phase: 0 (Reverse Engineering)*
