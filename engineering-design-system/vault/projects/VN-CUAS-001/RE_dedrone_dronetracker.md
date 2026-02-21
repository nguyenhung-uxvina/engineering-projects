---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Dedrone DroneTracker (Germany/USA)
version: 1.0
created: 2026-02-11
status: complete
---

# RE: Dedrone DroneTracker - Germany/USA
## Reverse Engineering Analysis from Public Sources

> **KEY DISTINCTION:** Dedrone is a **software-centric C-UAS platform** — fundamentally different from the hardware-centric approaches of DroneShield, Squarehead, or BeephoniX. Its core value proposition is the **DedroneTracker.AI command-and-control software** combined with proprietary **DroneDNA** classification engine (600+ drone models, 200+ RF protocols). Dedrone manufactures RF sensors but integrates third-party radars, cameras, and effectors via an open API. Acquired by **Axon Enterprise** (NASDAQ: AXON) in October 2024 for an estimated $300M+, Dedrone is now part of the world's largest public safety technology company. This represents the **software-defined C-UAS architecture** and the dominant approach in corrections, enterprise, and critical infrastructure markets.

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Dedrone Holdings, Inc. (now Axon subsidiary) |
| **Original HQ** | Kassel, Germany (2014); relocated to San Francisco, CA (2016) |
| **Current HQ** | Sterling, Virginia, USA (45662 Terminal Dr, Suite 110) |
| **Germany Office** | Kassel, Germany (R&D and production) |
| **UK Office** | London, England |
| **Other Offices** | Columbus, Ohio, USA |
| **Founded** | February 2014 |
| **Founders** | Jörg Lamprecht, Ingo Seebach, René Seeber |
| **CEO** | Aaditya Devarakonda (since 2020) |
| **Executive Chairman** | Jörg Lamprecht (co-founder) |
| **COO** | Ingo Seebach (co-founder) |
| **CTO** | René Seeber (co-founder) |
| **Parent Company** | Axon Enterprise, Inc. (NASDAQ: AXON) — acquired Oct 2024 |
| **Axon CEO** | Rick Smith (founder of Axon/TASER) |
| **Total Funding** | ~$130M across all rounds |
| **Last Valuation** | ~$300M (pre-acquisition) |
| **Axon Market Cap** | ~$50B+ (AXON is a Fortune 500 company) |
| **Axon Revenue** | $2.1B (FY2024, +33% YoY) |
| **Employees** | 200-300 estimated (Dedrone division) |
| **Status** | Wholly-owned subsidiary of Axon Enterprise |
| **ITAR Status** | German-origin R&D; US-headquartered — mixed ITAR/EAR considerations |
| **Certifications** | UK CPNI certified, US DHS SAFETY Act designated, Veracode verified, SAPIENT compliant |

### 1.1 Founding Team

| Name | Role | Background |
|------|------|------------|
| **Jörg Lamprecht** | Executive Chairman & Co-Founder | Serial entrepreneur; previously co-founded Aibotix (industrial drones, acquired by Hexagon) |
| **Ingo Seebach** | COO & Co-Founder | Serial entrepreneur; operational leadership |
| **René Seeber** | CTO & Co-Founder | Previously CTO & Co-Founder of JouleX (energy management, acquired by Cisco) |

> **Founder DNA insight:** The founding team has a track record of building and exiting deep-tech companies (Aibotix → Hexagon, JouleX → Cisco). All three founders are from the Kassel, Germany technology ecosystem. The Cisco connection is significant — John Chambers (former Cisco CEO) was an early personal investor in Dedrone and Dedrone won the 2016 Cisco Innovation Award.

### 1.2 Key Leadership

| Name | Role | Notes |
|------|------|-------|
| **Aaditya Devarakonda** | CEO | Appointed 2020 as founders stepped back |
| **Henning Heine Tam** | SVP, Chief of Staff & Head of Corporate Development | Key spokesperson; business operations leadership |
| **Russ Haugan** | GM of Aerial Armor division | CEO of acquired company Aerial Armor |
| **Matt Altman** | CTO of Aerial Armor division | CTO of acquired company Aerial Armor |

### 1.3 Funding & Acquisition History

| Year | Event | Amount | Investors |
|------|-------|--------|-----------|
| 2015 Apr | Seed Round | $3M | Target Partners |
| 2016 May | Series A | $10M | Menlo Ventures (lead), Felicis Ventures |
| 2017 May | Series B | $15M | Existing investors |
| 2021 | Series C | ~$30M | Axon (co-lead) |
| 2022 Jul | Series C-1 | $30.5M | Axon (co-lead), Felicis, Menlo |
| 2023 Jan | **Acquired Aerial Armor** | — | C-UAS systems integrator (New Mexico) |
| 2024 May | **Axon acquisition announced** | ~$300M+ est. | Definitive agreement |
| 2024 Oct | **Axon acquisition completed** | — | Dedrone now Axon subsidiary |

> **Strategic significance:** Axon (TASER, body cameras, Axon Evidence) acquiring Dedrone signals convergence of **public safety** and **airspace security**. Axon's Drone as First Responder (DFR) programs need both friendly-drone management AND counter-drone protection — Dedrone provides the latter. The combined platform is the only end-to-end solution from the same vendor.

### 1.4 Historical Timeline

| Year | Event |
|------|-------|
| 2014 | Founded in Kassel, Germany by Lamprecht, Seebach, and Seeber |
| 2015 Jan | First product launched: "Multi-Sensor Drone Warning System" + DroneTracker software |
| 2015 | 52 unauthorized drones detected in 26 days over US military facilities near Washington, D.C. |
| 2016 | HQ relocated from Kassel to San Francisco; won Cisco Innovation Award |
| 2016 | Provided anti-drone security for World Economic Forum in Davos |
| 2017 | Series B funding; expanded US government sales |
| 2019 | First C-UAS company to receive UK CPNI (Centre for Protection of National Infrastructure) certification |
| 2019 | RF-160 sensor launched (upgraded from RF-100) |
| 2020 | CEO transition: Aaditya Devarakonda replaces founders in day-to-day leadership |
| 2022 | Axis Communications camera integration; Series C-1 with Axon co-lead |
| 2022 Nov | DedroneTracker 5.1 — first true C-UAS C2 system |
| 2023 Jan | Acquired Aerial Armor (multi-sensor C-UAS integrator) |
| 2023 | Named TIME Best Inventions, CNBC Disruptor 50, AI Excellence Award |
| 2024 | Fast Company Most Innovative; US DHS SAFETY Act designation |
| 2024 Oct | Axon completes acquisition |
| 2025 | RF-360 sensor launched; DedroneOTM (On The Move) vehicle-mounted system |
| 2025 Oct | Tactical Extended Kit (radar + camera) for Group 3 drones at AUSA 2025 |
| 2025 | Partnership with Tytan Technologies (German AI interceptor drone for Shahed-class threats) |
| 2025 | Partnership with Thales Australia for OTM C-UAS |

---

## 2. PRODUCT FAMILY

### 2.1 Product Overview

| Product | Type | Function | Key Spec |
|---------|------|----------|----------|
| **DedroneTracker.AI** | C2 Software | Detection, classification, C2, forensics | 600+ drone models, 200+ protocols |
| **RF-160** | RF Sensor | Detection & classification | 1.6 km avg, up to 5 km |
| **RF-360** | RF Sensor | Detection, classification, & localization | Up to 5 km, ±5° direction finding |
| **RF-310** | RF Sensor | OTM-optimized detection | MIL-STD-810H rated |
| **DedroneOTM** | Vehicle System | Mobile DTI-M | 2x RF-310, MIL-STD-810H, 360° |
| **DedroneDefender 2** | Handheld Jammer | Precision RF defeat | Smart narrowband, AI-driven |
| **DedroneTactical Extended** | Kit | Fixed-site RF + radar + camera | Group 1-3 threats |

### 2.2 DedroneTracker.AI — Core C2 Platform

**The software is the product.** Unlike DroneShield (hardware-centric) or Squarehead (sensor-centric), Dedrone's primary competitive advantage is its software platform.

#### Architecture
- **Deployment:** Cloud-hosted OR on-premise server
- **Interface:** Web-based UI
- **Updates:** Quarterly DroneDNA cloud updates
- **API:** Open API for third-party sensor/effector integration
- **Standards:** SAPIENT compliant (NATO autonomous sensor integration)
- **Security:** Veracode certified code

#### DroneDNA Classification Engine
- **Database:** 600+ individual drone models from 150+ manufacturers
- **Protocols:** 200+ drone RF protocols (including FPV, DIY, battlefield drones)
- **Method:** RF protocol recognition — identifies drones by their specific radio frequency communication patterns without decoding telemetry data
- **ML Training:** Millions of data points; continuously updated via cloud
- **Discrimination:** Can distinguish drones from birds, planes, and other moving objects
- **Model ID:** Identifies specific drone manufacturer and model
- **Updates:** Cloud-delivered quarterly; dedicated SIGINT team adds emerging battlefield drone protocols
- **Coverage:** Commercial (DJI entire lineup), hobbyist, homebrew, FPV racing, military/modified drones

#### Key Software Features
- Real-time drone detection with flight path visualization on map
- Drone AND pilot localization (with RF-360 or multi-sensor)
- Automated alerts: text, email, TCP/IP, SNMP, smartphone push, UI
- Forensic evidence recording: drone model, time, duration, video evidence
- Automated summary reporting
- Multi-sensor fusion (RF + radar + camera + acoustic inputs)
- Machine learning video analytics (camera-based drone detection)
- Trigger passive and active countermeasures via API
- Multi-site management from single interface
- Air-gapped and connected deployment options

### 2.3 RF-160 Sensor

| Specification | Value |
|---------------|-------|
| **Type** | Passive omnidirectional RF sensor |
| **Function** | Detection & classification |
| **Detection Range** | 1.6 km average; up to 5 km (drone-dependent) |
| **Extended Range** | Multiple RF-160s networked increase coverage |
| **Connectivity** | Integrated LTE; cloud-connected to DroneTracker |
| **Server Required** | No (cloud-ready) |
| **Drones Detected** | Commercial, hobbyist, homebrew, entire DJI lineup |
| **Output** | Drone count, model, manufacturer, protocol |
| **Predecessor** | RF-100 |
| **Installation** | Fast deployment; LTE eliminates complex network setup |

### 2.4 RF-360 Sensor

| Specification | Value |
|---------------|-------|
| **Type** | Passive omnidirectional RF sensor with direction finding |
| **Function** | Detection, classification, localization (geolocation) |
| **Detection Range** | Up to 5 km |
| **Direction Finding** | Up to 1.0 km (0.65 mi); up to 1.5 km in ideal conditions |
| **DF Accuracy** | ±5° (mean error) |
| **Geolocation** | Requires 2+ RF-360 sensors; also via WiFi signals |
| **Connectivity** | Integrated LTE and GPS |
| **Optimization** | Optimized for RF-noisy environments |
| **Predecessor** | RF-300 (up to 1 mile detection) |
| **Legal** | No authorization required (passive listening) |

### 2.5 DedroneOTM (On The Move)

| Specification | Value |
|---------------|-------|
| **Type** | Vehicle-mounted C-UAS DTI-M system |
| **RF Sensors** | 2x RF-310 (passive detection) |
| **Compute** | Ruggedized on-vehicle tablet + Mobile Compute Unit |
| **Power** | MIL-STD-1275 compatible vehicle power |
| **Environmental** | MIL-STD-810H (weather, vibration, shock) |
| **Awareness** | 360° airspace coverage |
| **Targeting Accuracy** | 2.5° (kinetic kill viable) |
| **Protocols** | DedroneDNA: 200+ protocols, FPV, DIY, battlefield drones |
| **Navigation** | Integrated GNSS Compass |
| **Jammer** | DedroneDefender 2 (optional, connected handheld) |
| **Deployment** | Air-gapped or connected |
| **Vehicle Compatibility** | Any military/tactical vehicle |
| **Mast** | Optional telescopic mast for RF sensors |
| **Threats** | Group 1-3 UAS |
| **Partners** | Thales Australia (integration), ARX Robotics (UGV mount) |

### 2.6 DedroneDefender 2 — Smart Handheld Jammer

| Specification | Value |
|---------------|-------|
| **Type** | Handheld smart jammer |
| **Control** | AI-driven autonomous precision jamming |
| **Targeting** | Precision targeting display |
| **Jamming** | Narrowband — minimizes collateral to friendly communications |
| **Swarm** | Effective against drone swarms |
| **Connectivity** | Cloud-enabled; works with DedroneTracker.AI |
| **GNSS Spoofing** | Can block/spoof GNSS signals |
| **Ruggedization** | MIL-STD rated |
| **Mount** | Compatible with vehicle pan-tilt unit for OTM |
| **Range** | Several hundred meters (estimated from ARX Robotics reporting) |

### 2.7 DedroneTactical Extended Kit

Displayed at AUSA 2025 (October 2025):
- Adds **radar and camera capabilities** to baseline RF detect & defeat
- Extends detection from Group 1-2 to **Group 3** UAS (Shahed-class)
- Partnership with **Tytan Technologies** (German firm) — AI-powered interceptor drone
- End-to-end kill chain: detect → track → identify → defeat (kinetic or electronic)
- Open architecture; SAPIENT compliant
- Third-party EO/IR cameras and radars integrated while Dedrone provides RF

---

## 3. SYSTEM ARCHITECTURE

### 3.1 Software-Defined Architecture

```
┌─────────────────────────────────────────────────────┐
│              DedroneTracker.AI (C2 Software)         │
│    ┌───────────┐  ┌───────────┐  ┌───────────────┐  │
│    │ DroneDNA  │  │ ML Video  │  │ Sensor Fusion │  │
│    │ RF Class. │  │ Analytics │  │    Engine     │  │
│    └─────┬─────┘  └─────┬─────┘  └───────┬───────┘  │
│          └──────────────┼────────────────┘           │
│                         │                             │
│    ┌─────────────────────────────────────────────┐   │
│    │           Open API Layer                     │   │
│    │  SAPIENT │ REST API │ TCP/IP │ SNMP         │   │
│    └─────────────────────────────────────────────┘   │
└─────────┬──────────────┬──────────────┬──────────────┘
          │              │              │
    ┌─────┴─────┐  ┌─────┴─────┐  ┌────┴─────┐
    │ DEDRONE   │  │ 3RD PARTY │  │ EFFECTOR │
    │ RF SENSORS│  │ SENSORS   │  │ LAYER    │
    │           │  │           │  │          │
    │ RF-160    │  │ Radar     │  │ Jammer   │
    │ RF-360    │  │ Camera    │  │ (Defender │
    │ RF-310    │  │ Acoustic  │  │  2, etc) │
    │           │  │ EO/IR     │  │ Fog      │
    │           │  │ LiDAR     │  │ Blinds   │
    └───────────┘  └───────────┘  └──────────┘
```

### 3.2 Detection Method — RF Protocol Recognition

Dedrone's core detection modality is **RF-based** — fundamentally different from acoustic detection:

| Aspect | Dedrone RF Approach | Acoustic Approach (VN-CUAS) |
|--------|--------------------|-----------------------------|
| **Sensing** | Radio frequency signals (2.4/5.8 GHz, etc.) | Sound waves (50 Hz - 20 kHz) |
| **Method** | RF protocol pattern matching | Beamforming + acoustic fingerprint |
| **Range** | 1.6-5 km | 0.2-1 km |
| **Speed** | Near-instantaneous | ~1 second |
| **ID Granularity** | Specific model + protocol | Drone type/class |
| **Pilot Location** | Yes (via RF triangulation) | No |
| **Autonomous Drones** | Cannot detect (no RF emissions) | CAN detect (motors still produce sound) |
| **Modified Drones** | Partially (protocol may be changed) | CAN detect (acoustic signature persists) |
| **Urban Performance** | RF penetrates buildings (good) | Sound reflects/attenuates (moderate) |
| **Weather** | Unaffected | Moderate degradation (wind, rain) |
| **NLOS Detection** | Yes (RF penetrates structures) | Yes (sound diffracts around obstacles) |
| **Passive/Active** | Passive (listening only) | Passive (listening only) |
| **Power** | ~10-50W per sensor (estimated) | <10W per node |
| **Cost** | $10K-50K per sensor (estimated) | $2K-5K per node (VN target) |

> **Critical Gap for Dedrone:** RF detection CANNOT detect autonomous pre-programmed drones that fly without radio links — the exact scenario growing in military threats. **Acoustic detection fills this gap** — this is the primary justification for VN-CUAS as a complementary sensor layer.

### 3.3 Multi-Sensor Fusion Philosophy

Dedrone's approach is "RF-first, multi-sensor optional":

1. **Layer 1 — RF Detection (Dedrone-native):** RF-160/RF-360 sensors detect RF-emitting drones at 1-5 km
2. **Layer 2 — Camera AI:** ML-based video analytics distinguish drones from birds/planes; visual identification
3. **Layer 3 — Radar:** Third-party radar extends range and detects non-RF drones
4. **Layer 4 — Acoustic:** Third-party acoustic sensors for supplementary NLOS detection
5. **Layer 5 — Defeat:** DedroneDefender jamming, GNSS spoofing; third-party effectors via API

All sensor data fuses in DedroneTracker.AI to create single common operating picture.

---

## 4. PATENTS & INTELLECTUAL PROPERTY

### 4.1 US Patents — DroneDefender Product

| Patent Number | Type | Country |
|---------------|------|---------|
| D873,368 | Design | US |
| D872,820 | Design | US |
| D873,367 | Design | US |
| D872,819 | Design | US |
| D855,731 | Design | US |
| D855,730 | Design | US |
| D879,902 | Design | US |
| 10,574,384 | Utility | US |
| 10,020,909 | Utility | US |
| 10,103,835 | Utility | US |
| 10,237,012 | Utility | US |
| 10,567,107 | Utility | US |
| 2018101673 | — | AU |
| 2018101672 | — | AU |
| 10-1980499 | — | KR |
| 20180367237 | Application | US |
| 2,997,443 | — | CA |
| 16785276.3 | — | EP |

### 4.2 US Patents — DedroneTracker Product

| Patent Number | Type | Country |
|---------------|------|---------|
| 9,805,273 | Utility | US |
| 10,229,329 | Utility | US |
| 10,317,506 | Utility | US |
| 10,025,991 | Utility | US |
| 10,025,993 | Utility | US |
| 10,621,443 | Utility | US |

### 4.3 Patent Analysis

**Total known patents:** 24 granted + applications across 6 jurisdictions (US, AU, KR, CA, EP, plus US applications)

**IP Focus Areas:**
- **DroneDefender:** 7 design patents (physical form factor) + 5 utility patents (jammer technology, RF disruption methods) — strong protection of defeat capability
- **DedroneTracker:** 6 utility patents — RF-based detection, classification, multi-sensor fusion algorithms
- **Geographic coverage:** US, Australia, South Korea, Canada, Europe — commercial markets globally

**IP Strategy Insight:**
- Patent portfolio focuses on **detection algorithms** and **jammer technology** — NOT on sensor hardware
- This reinforces the software-centric business model
- Axon acquisition adds Axon's substantial patent portfolio in cameras, AI, evidence management
- Aerial Armor acquisition may have added integration/systems-level IP

> **VN-CUAS IP Gap:** Dedrone's patents are entirely in RF detection and RF jamming domains. There is **zero patent overlap** with acoustic detection technology. VN-CUAS acoustic detection system would not infringe any known Dedrone patents.

---

## 5. KEY DEPLOYMENTS & CUSTOMERS

### 5.1 Government & Military

| Customer | Application | Notes |
|----------|-------------|-------|
| **US Department of Defense** | Military base protection | Ongoing deployment |
| **US Department of Homeland Security** | Border protection | Fixed-site RF + jamming |
| **Ukraine Ministry of Defense** | Active combat C-UAS | Battlefield deployment |
| **6 of 7 G7 nations** | Various defense applications | Through partners and direct |

### 5.2 Law Enforcement & Public Safety

| Customer | Location |
|----------|----------|
| New Jersey State Police | USA |
| Virginia State Police | USA |
| South Carolina Law Enforcement Division (SLED) | USA |
| Campbell Police Department | USA |
| Tulsa County Sheriff's Office | USA |
| Oakland County Sheriff's Office | Michigan, USA |
| St. Petersburg Police Department | Florida, USA |
| Cobb County Sheriff's Office | Georgia, USA |
| Catalonian Police | Barcelona, Spain |
| Vienna Police Department | Austria |
| Latvia State Police | Latvia |
| Australian Police | Australia |
| Swiss Police | Davos (WEF), Switzerland |

### 5.3 Correctional Facilities

| Customer | Location |
|----------|----------|
| Fulton County Jail | Georgia, USA |
| Maine Department of Corrections | USA |
| South Carolina Department of Corrections | USA |
| JVA Halle Prison | Germany |

### 5.4 Critical Infrastructure & Events

| Customer/Event | Application |
|----------------|-------------|
| **World Economic Forum (Davos)** | VIP protection (2016+) |
| **US Presidential Debates** | Airspace security |
| **NASCAR** | Event protection |
| **PGA Tour Phoenix Open** | Event protection |
| **Marine Corps Marathon** | Event protection |
| **Preakness Stakes** | Event protection |
| **SOF Week 2024** | Military event protection |
| Chicago Department of Aviation | Airport protection |
| Newcastle International Airport | Airport protection |
| Consolidated Edison (ConEd) | Utility infrastructure |
| Korean Power Exchange (KPX) | Utility infrastructure |
| Volke Automotive | Industrial espionage prevention |

### 5.5 Key Partnerships

| Partner | Collaboration |
|---------|---------------|
| **Axon Enterprise** | Parent company; DFR integration, body camera ecosystem |
| **General Dynamics** | Expeditionary C-UAS kit for US military |
| **Thales Australia** | Vehicle-mounted OTM C-UAS delivery |
| **Tytan Technologies** | AI-powered interceptor drone (Group 3 defeat) |
| **ARX Robotics** | UGV-mounted counter-drone (Gereon + Defender 2) |
| **Airbus** | Anti-drone solution partnership |
| **Axis Communications** | PTZ camera integration (since 2022) |
| **Aerial Armor** | Acquired Jan 2023; multi-sensor integration |

---

## 6. AWARDS & CERTIFICATIONS

| Award/Certification | Year | Significance |
|---------------------|------|-------------|
| **UK CPNI Certified** | 2019 | First-ever C-UAS technology approved by UK Centre for Protection of National Infrastructure |
| **US DHS SAFETY Act Designated** | 2024 | Only C-UAS company acknowledged under DHS SAFETY Act |
| **Veracode Certified** | — | Code security verification |
| **SAPIENT Compliant** | — | NATO standard for autonomous sensor integration |
| **Cisco Innovation Award** | 2016 | Recognized by Cisco |
| **CNBC Disruptor 50** | 2023 | Top 50 disruptive companies |
| **TIME Best Inventions** | 2023 | Innovation recognition |
| **AI Excellence Award** | 2023 | Best product in AI category |
| **Fast Company Most Innovative** | 2024 | Innovation recognition |
| **Inc. 5000** | 2024 | Fastest-growing US companies |

---

## 7. PERFORMANCE COMPARISON

### 7.1 Dedrone vs Other C-UAS Systems

| Parameter | Dedrone DroneTracker | DroneShield DroneSentry | Squarehead Discovair G2+ | BeephoniX M2 | VN-CUAS (Target) |
|-----------|---------------------|------------------------|-------------------------|-------------|-------------------|
| **Architecture** | Software-centric C2 | Hardware-centric multi-sensor | Acoustic sensor | Acoustic sensor | Acoustic sensor |
| **Primary Sensor** | RF | RF + radar + optical | Acoustic (128 MEMS) | Acoustic (151 MEMS) | Acoustic (128-256 MEMS) |
| **Detection Range** | 1.6-5 km (RF) | 1-8 km (multi-sensor) | 0.3-1 km | 0.2-0.9 km | 0.5-0.8 km |
| **Autonomous Drones** | No (needs RF) | Partial (radar yes) | Yes | Yes | Yes |
| **Pilot Location** | Yes | Yes | No | No | No |
| **Classification** | 600+ models | 150+ models | Type/class | Type/class | Type/class |
| **Weight** | Sensor ~5-8 kg | Sensor ~46 kg | Array 8 kg | Array 0.95 kg | Target 1-2 kg |
| **Power** | ~20-50W/sensor | ~100-200W/system | ~20-40W | ~5-10W | <10W |
| **Environmental** | IP rated sensors | MIL-STD-810H/IP67 | IP65/MIL-STD | IP65 | IP67 target |
| **Defeat** | Yes (Defender 2) | Yes (jamming) | No | No | No |
| **C2 Software** | DedroneTracker.AI | DroneSentry-C2 | Limited | Limited | TBD |
| **SAPIENT** | Yes | Yes | No | No | Target yes |
| **Drone DB** | DroneDNA (600+) | RFAI (150+) | None | None | Acoustic DB (TBD) |
| **Est. System Price** | $50K-500K+ | $200K-1M+ | $50K-150K | $20K-50K est. | $2K-5K target |
| **Country** | Germany/USA (Axon) | Australia/USA | Norway | Netherlands | Vietnam |

### 7.2 Dedrone vs DroneShield — Detailed Comparison

| Aspect | Dedrone | DroneShield |
|--------|--------|-------------|
| **Business Model** | Software-as-a-Service + sensors | Hardware + software platform |
| **Revenue Model** | SaaS subscriptions + sensor sales | Product sales + contracts |
| **Core IP** | DroneDNA algorithm, RF classification | RFAI engine, DroneOptID, SensorFusionAI |
| **Sensor Manufacturing** | In-house RF sensors only; integrates 3rd-party | In-house RF/EW; integrates 3rd-party radar/optical |
| **Market Focus** | Enterprise, corrections, critical infrastructure, public safety | Military, defense, government |
| **Parent Company** | Axon (NASDAQ: AXON, ~$50B) | Independent (ASX:DRO, A$2.9B) |
| **Geographic Strength** | US domestic, Europe | AUKUS nations, NATO, Middle East |
| **Software Updates** | Quarterly DroneDNA via cloud | Quarterly software updates |
| **Group 3 Drones** | Expanding (Tytan partnership) | Expanding (radar integration) |
| **Acoustic Integration** | Third-party via API | Squarehead Discovair via DroneSentry-C2 |

---

## 8. CORE TECHNOLOGY DEEP DIVE

### 8.1 DroneDNA — The Classification Engine

DroneDNA is Dedrone's primary competitive moat:

**How it works:**
1. RF sensors passively scan radio spectrum
2. DroneDNA identifies specific **RF protocol patterns** — each drone model has unique communication characteristics
3. ML algorithms match observed RF patterns against database of 600+ models
4. Classification output: drone make, model, manufacturer, protocol type
5. Does NOT decode telemetry data (avoids legal/regulatory issues)

**Training pipeline:**
- Millions of RF signal data points collected from global sensor network
- Dedicated Signals Intelligence (SIGINT) team adds emerging protocols
- Quarterly cloud updates push new signatures to all deployed sensors
- Continuous learning from 1.2M+ drone violations tracked in global database

**Drone Violations Database:**
- Dedrone maintains a publicly visible counter of drone violations detected globally
- As of 2025: 1.2M+ violations tracked
- Provides market intelligence and validates detection accuracy

### 8.2 Machine Learning Video Analytics

- Camera-agnostic: works with off-the-shelf surveillance cameras
- ML image recognition classifies drones vs birds vs planes
- Cloud-updated classification library
- Records video evidence automatically
- Provides visual confirmation of RF-detected threats

### 8.3 Multi-Sensor Fusion

DedroneTracker.AI fuses data from multiple sensor types:
- **RF:** Primary detection, classification, pilot location
- **Radar:** Range extension, tracking, non-RF drone detection
- **Camera:** Visual confirmation, forensic evidence
- **Acoustic:** Supplementary detection layer (via third-party integration)
- **Output:** Single common operating picture with threat assessment

### 8.4 Open Architecture Philosophy

Key design principle: **sensor-agnostic platform**
- DroneTracker API integrates any compatible sensor or effector
- No vendor lock-in for secondary sensors
- Enables customers to select best-of-breed components
- SAPIENT compliance ensures NATO interoperability
- This approach is fundamentally different from DroneShield's more integrated hardware approach

---

## 9. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 9.1 Overall Function

**Detect, classify, locate, and enable defeat of unauthorized small UAS (sUAS) in protected airspace through software-centric multi-sensor fusion.**

### 9.2 Function Structure

```
OVERALL: Protect Airspace from Unauthorized sUAS
├── F1: Detect RF-emitting drones (RF-160/RF-360)
│   ├── F1.1: Passively scan radio spectrum
│   ├── F1.2: Identify drone RF protocol patterns
│   ├── F1.3: Count number of drones in airspace
│   └── F1.4: Provide early warning alert
├── F2: Classify drone threats (DroneDNA)
│   ├── F2.1: Match RF signature to drone database
│   ├── F2.2: Identify manufacturer and model
│   ├── F2.3: Assess threat level
│   └── F2.4: Update classification library (cloud)
├── F3: Locate drone and pilot (RF-360 + fusion)
│   ├── F3.1: Direction-find from multiple sensors
│   ├── F3.2: Triangulate drone position
│   ├── F3.3: Triangulate pilot/operator position
│   └── F3.4: Track flight path in real-time
├── F4: Fuse multi-sensor data (DedroneTracker.AI)
│   ├── F4.1: Correlate RF + radar + camera + acoustic data
│   ├── F4.2: Resolve conflicting sensor reports
│   ├── F4.3: Generate common operating picture
│   └── F4.4: Provide targeting data for effectors
├── F5: Visualize and alert (UI + notifications)
│   ├── F5.1: Display real-time map with drone/pilot positions
│   ├── F5.2: Trigger automated alerts (multi-channel)
│   ├── F5.3: Record forensic evidence
│   └── F5.4: Generate automated reports
└── F6: Defeat unauthorized drones (DedroneDefender 2)
    ├── F6.1: Jam drone control link (narrowband)
    ├── F6.2: Spoof GNSS signals
    ├── F6.3: Force drone to land/return-to-home
    └── F6.4: Engage kinetic effectors (via API)
```

---

## 10. BOM ESTIMATE (Reverse-Engineered)

### 10.1 RF-360 Sensor — Estimated BOM

| Component | Estimated Specification | Est. Cost |
|-----------|----------------------|-----------|
| Software-Defined Radios (SDRs) | Multiple integrated SDRs, wideband | $500-1,500 |
| RF Front-End | Low-noise amplifiers, filters, antenna elements | $200-500 |
| Direction Finding Array | Multi-element antenna array (DF capability) | $300-800 |
| Embedded Processor | ARM/x86 SoC with ML inference capability | $100-300 |
| LTE Module | Integrated cellular connectivity | $50-100 |
| GPS Module | Position and timing | $20-50 |
| Power Supply | PoE or 12/24V DC | $30-80 |
| Enclosure | IP-rated outdoor housing | $100-200 |
| Connectors & Cables | Weatherproof RF/data connectors | $30-50 |
| PCB & Assembly | Multi-layer RF PCBs | $100-200 |
| **Total BOM** | | **$1,430-3,780** |
| **Est. Retail** | (4-8x BOM for software-heavy product) | **$10,000-30,000** |

### 10.2 DedroneOTM System — Estimated BOM

| Component | Specification | Est. Cost |
|-----------|--------------|-----------|
| 2x RF-310 Sensors | MIL-STD-810H ruggedized RF sensors | $5,000-15,000 |
| Mobile Compute Unit | Ruggedized server (computing, networking, power) | $3,000-8,000 |
| Ruggedized Tablet | On-vehicle display/control | $2,000-5,000 |
| DedroneDefender 2 | Smart handheld jammer (optional) | $15,000-30,000 est. |
| Mounting Hardware | Vehicle-specific brackets, mast, cables | $1,000-3,000 |
| GNSS Compass | Navigation/orientation | $500-1,500 |
| MIL-STD-1275 Power | Vehicle power interface | $500-1,000 |
| Software License | DedroneTracker.AI + DroneDNA | $10,000-50,000/yr |
| **Total System** | | **$37,000-113,500** |
| **Est. Retail** | (with margins and integration) | **$100,000-300,000+** |

---

## 11. DESIGN INSIGHTS FOR VN-CUAS

### 11.1 Key Lessons from Dedrone

1. **Software is the moat:** Dedrone proves that a software-centric approach with cloud-updated databases can dominate the market. VN-CUAS should invest heavily in ML/classification software, not just hardware.

2. **Database is the asset:** DroneDNA's 600+ model database is Dedrone's most defensible competitive advantage. VN-CUAS should build an **acoustic signature database** (equivalent to DroneDNA) from day one.

3. **Open architecture wins:** Dedrone's API-first approach allows integration with any sensor or effector. VN-CUAS should design for SAPIENT compliance and RESTful API integration from the start.

4. **RF detection gap = acoustic opportunity:** Dedrone CANNOT detect autonomous pre-programmed drones (no RF emissions). This is the exact market gap that VN-CUAS acoustic detection fills. Position VN-CUAS as a **complementary Layer 4 sensor** that integrates into Dedrone (or DroneShield) via API.

5. **Cloud updates enable rapid evolution:** Quarterly DroneDNA updates keep pace with new drones. VN-CUAS should implement cloud-updatable acoustic fingerprint databases.

6. **Corrections market is validated:** Dedrone has proven strong demand from prisons for contraband drone detection. This is a potential VN-CUAS market (cheaper alternative to full Dedrone system for basic detection).

7. **SAPIENT compliance is table stakes:** Both Dedrone and DroneShield are SAPIENT compliant. VN-CUAS must implement SAPIENT to be considered for military/NATO market.

### 11.2 VN-CUAS Positioning vs Dedrone

| Scenario | Positioning |
|----------|-------------|
| **Complementary sensor** | VN-CUAS as acoustic Layer 4 integrated into DedroneTracker.AI via API — fills autonomous drone gap |
| **Low-cost standalone** | VN-CUAS as $2K-5K basic detection for corrections/perimeter where $50K+ Dedrone is overkill |
| **Sensor wake-up** | VN-CUAS triggers Dedrone RF sensors (power saving in persistent surveillance) |
| **Export market** | VN-CUAS for countries that cannot access Western C-UAS (sanctions, ITAR restrictions) |
| **Mesh network** | Multiple VN-CUAS nodes provide wide-area acoustic coverage feeding into Dedrone C2 |

### 11.3 Updated VN-CUAS Product Concept (v5.0)

Building on insights from all 5 RE analyses (Squarehead, BeephoniX, Fraunhofer, DroneShield, Dedrone):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Array** | 128-256 MEMS microphones | Squarehead (128), BeephoniX (151) benchmarks |
| **Weight** | 1-2 kg | BeephoniX (950g) proves ultra-light is feasible |
| **Power** | <10W | Fraunhofer sensor wake-up; solar/battery viability |
| **Detection Range** | 500-800m | Acoustic physics limit; extended via mesh network |
| **Accuracy** | ≤5° azimuth, ≤10° elevation | BeephoniX (1-2°), Dedrone RF-360 (±5°) benchmarks |
| **Target Price** | $2K-5K per node | 10-100x cheaper than Dedrone RF-360 or DroneShield |
| **Environmental** | IP67, MIL-STD-810H | DroneShield (IP67) + Dedrone OTM (MIL-STD-810H) standard |
| **Classification** | Acoustic fingerprint DB (cloud-updatable) | Modeled on DroneDNA concept — but for sound |
| **Integration** | SAPIENT + RESTful API + TAK plugin | Both Dedrone and DroneShield are SAPIENT compliant |
| **Deployment** | Tool-less <10 min; magnetic/clamp mount | DroneShield rapid deployment model |
| **Autonomous Detection** | YES — does not require RF emissions | Key differentiator vs Dedrone and DroneShield RF |
| **Software** | Cloud-updatable acoustic DB + edge ML inference | Fraunhofer processing stack + Dedrone cloud model |
| **Local Content** | ≥60% by value | Vietnamese defense requirement |
| **Mesh Network** | Multi-node distributed detection | Extends effective range to km-scale with $2K nodes |

### 11.4 C-UAS Ecosystem Map (After 5 RE Analyses)

```
MARKET LANDSCAPE (2025-2026)
═══════════════════════════════════════════════════════════

HIGH COST ($100K-1M+)    ┌──────────────────────────┐
Multi-Sensor Systems      │  DroneShield DroneSentry  │
                          │  Dedrone Full System      │
                          │  (Complete DTI-M)         │
                          └──────────────────────────┘

MID COST ($20K-100K)      ┌──────────────────────────┐
Specialized Sensors       │  Squarehead Discovair G2+ │
                          │  Dedrone RF-360 sensor    │
                          │  (Single modality)        │
                          └──────────────────────────┘

LOW COST ($2K-20K)        ┌──────────────────────────┐
Entry/Complementary       │  BeephoniX M2             │
                          │  ★ VN-CUAS (TARGET) ★     │
                          │  (Acoustic detection)     │
                          └──────────────────────────┘

RESEARCH/ALGORITHM        ┌──────────────────────────┐
Technology Provider       │  Fraunhofer IDMT          │
                          │  (Algorithms + licensing) │
                          └──────────────────────────┘

VN-CUAS SWEET SPOT: Low-cost acoustic sensor that
integrates into ANY higher-tier system via SAPIENT/API
═══════════════════════════════════════════════════════════
```

---

## 12. INTELLIGENCE GAPS

| ID | Gap | Priority | Impact on VN-CUAS |
|----|-----|----------|-------------------|
| IG-01 | Dedrone RF-360 exact internal architecture (SDR chipset, FPGA) | Medium | Component benchmarking |
| IG-02 | DroneDNA database update latency for new drone models | Medium | Acoustic DB update strategy |
| IG-03 | DedroneTracker.AI API documentation (sensor integration protocol) | **High** | VN-CUAS integration design |
| IG-04 | Exact pricing for Dedrone sensors and OTM system | Medium | VN-CUAS competitive pricing |
| IG-05 | Dedrone acoustic sensor integration partners (who provides Layer 4?) | **High** | VN-CUAS partnership opportunity |
| IG-06 | Axon post-acquisition product roadmap for Dedrone | Medium | Market trajectory |
| IG-07 | DedroneTracker.AI edge deployment specs (hardware requirements) | Medium | VN-CUAS compute design |
| IG-08 | Dedrone performance in tropical/high-humidity environments | Medium | Vietnam deployment suitability |

---

## 13. REFERENCES

1. Dedrone Official Website — https://www.dedrone.com/
2. Dedrone Legal/Patents — https://www.dedrone.com/legal/overview
3. Dedrone OTM Solution — https://www.dedrone.com/solutions/dedrone-on-the-move
4. Wikipedia: Dedrone Holdings — https://en.wikipedia.org/wiki/Dedrone_Holdings
5. NWS: Dedrone DroneTracker — https://nwsnext.com/tech/dedrone-dronetracker/
6. NWS: Dedrone RF Sensors — https://nwsnext.com/tech/dedrone-rf-sensors/
7. Janes: Dedrone Tactical Extended Kit (AUSA 2025) — https://www.janes.com/
8. Axon acquisition press release — https://investor.axon.com/2024-05-06
9. Axon Q3 2024 earnings (Dedrone close) — https://investor.axon.com/2024-11-07
10. CNBC: Axon acquiring Dedrone — https://www.cnbc.com/2024/05/06/
11. Menlo Ventures: Dedrone acquisition — https://menlovc.com/perspective/
12. Tracxn: Dedrone profile — https://tracxn.com/d/companies/dedrone/
13. Army Recognition: AUSA 2025 Dedrone/Tytan — https://www.armyrecognition.com/
14. Army Recognition: ARX Gereon + Dedrone Defender 2 — https://www.armyrecognition.com/
15. Inside Unmanned Systems: Dedrone + Thales Australia — https://insideunmannedsystems.com/
16. Unmanned Airspace: Dedrone + Aerial Armor — https://www.unmannedairspace.info/
17. PRNewswire: RF-160 launch — https://www.prnewswire.com/
18. SecurityInfoWatch: RF-360 — https://www.securityinfowatch.com/
19. ManualsLib: RF-360 installation manual — https://www.manualslib.com/

---

## 14. COMPARATIVE SUMMARY TABLE

| Dimension | Squarehead G2+ | BeephoniX M2 | Fraunhofer IDMT | DroneShield DroneSentry | **Dedrone DroneTracker** | VN-CUAS Target |
|-----------|---------------|-------------|-----------------|------------------------|------------------------|---------------|
| **Country** | Norway | Netherlands | Germany | Australia | **Germany/USA** | Vietnam |
| **Type** | Acoustic sensor | Acoustic sensor | Research/algorithms | Multi-sensor system | **Software C2 platform** | Acoustic sensor |
| **Founded** | 2000 | 2022 | 2008 (HSA) | 2014 | **2014** | 2026 |
| **Ownership** | Private | Private | Public institute | ASX:DRO | **Axon (NASDAQ: AXON)** | State enterprise |
| **Primary Sensor** | 128 MEMS | 151 MEMS | Microphone array | RF + radar + optical | **RF (SDR-based)** | 128-256 MEMS |
| **Detection Range** | 300-1000m | 200-900m | 50-200m | 1-8 km | **1.6-5 km** | 500-800m |
| **Weight** | 8 kg | 950g | Research prototype | 46 kg (X Mk2) | **~5-8 kg/sensor** | 1-2 kg |
| **Classification** | Type/class | Type/class | ML fingerprint | 150+ models (RFAI) | **600+ models (DroneDNA)** | Type/class + DB |
| **Autonomous Detect** | Yes | Yes | Yes | Partial | **No (needs RF)** | Yes |
| **C2 Platform** | Limited | Limited | None | DroneSentry-C2 | **DedroneTracker.AI** | SAPIENT client |
| **Defeat** | No | No | No | Yes (jamming + kinetic) | **Yes (Defender 2)** | No |
| **SAPIENT** | No | No | No | Yes | **Yes** | Target yes |
| **Est. Price** | $50-150K | $20-50K | N/A (licensing) | $200K-1M+ | **$50K-500K+** | $2K-5K |

---

*Document generated: 2026-02-11*
*RE Methodology: Pahl & Beitz 4-phase reverse engineering from public sources*
*Classification: UNCLASSIFIED — All data from open sources*
