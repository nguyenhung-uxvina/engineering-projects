---
project: CORTEX-C2
phase: 0
type: reverse-engineering
subject: Saab AB Training & Simulation - GAMER System (Sweden)
version: 1.0
created: 2026-02-12
status: complete
---

# RE Analysis: Saab Training & Simulation / GAMER System

> **Classification:** OPEN SOURCE INTELLIGENCE (OSINT)
> **Analyst:** CORTEX C2 RANGE Team
> **Date:** 2026-02-12
> **Sources:** Saab corporate website, Janes Defence, Breaking Defense, Army Technology, Wikipedia, Shephard Media, press releases, annual reports, contract awards

---

## 1. Company Profile — Training & Simulation Division

### 1.1 Corporate Position

| Attribute | Detail |
|-----------|--------|
| **Parent Company** | Saab AB (OMX: SAAB-B) |
| **Business Area** | **Dynamics** (one of 4 BAs: Aeronautics, Dynamics, Surveillance, Kockums) |
| **Business Unit** | Training & Simulation (T&S) |
| **HQ Location** | Stensholmsv. 20, Huskvarna, Sweden |
| **Established** | Originally as Saab Training Systems AB; renamed Saab Training and Simulation |
| **Employees (T&S)** | **~1,200+** globally (per 2024 job posting; was ~400 historically, ~257 in 1999) |
| **Subsidiaries** | Czech Republic (~120 emp), USA (Saab Inc., Orlando FL), UK, Germany, Norway, Finland, Netherlands, Canada, Australia |
| **CAGE Code** | S7055 |
| **Export Ratio** | ~95% of revenue from exports |
| **Global Reach** | Products deployed in **30+ nations** |
| **Parent Revenue (2024)** | SEK 63B (~USD 5.98B) total Saab AB |
| **Dynamics BA Revenue** | ~SEK 16-18B (est. 2024; includes Ground Combat, Missile Systems, T&S) |
| **T&S Revenue (est.)** | **SEK 3-5B** (~USD 300-500M) — estimated 20-30% of Dynamics BA |
| **US Market Share** | **~25%** of US live training market (per Saab 2021 Annual Report) |

### 1.2 Organizational History

| Year | Event |
|------|-------|
| 1990s | BT46 laser technology introduced — first "true ballistic" simulation |
| 1995 | First US Army TESS systems fielded |
| 1999 | GAMER system delivered to US Forces; 257 employees |
| 2001 | DISE (Deployable Instrumented Training System - Europe) delivered to US 7th ATC |
| 2003 | Dutch MCTC (Mobile Combat Training Centre) delivered — world's largest mobile CTC |
| 2005 | Joint venture with EADS Deutschland (Friedrichshafen) for live training |
| 2007 | BT46 Mk II launched — new laser transceiver, improved target & recording |
| 2012 | US Army CVTESS IDIQ contract signed |
| 2016 | WE:Go individualized soldier AAR app introduced |
| 2016 | OSAG 2.0 interoperability upgrades for US 7th ATC DISE + CVTESS |
| 2017 | BT46 Mk III introduced at I/ITSEC — smartphone/tablet setup, dual laser codes |
| 2019 | **Sandbox** 3D mixed-reality AAR tool unveiled at I/ITSEC |
| 2021 | USMC FoFTS-Next contract awarded (USD 127.9M SATOC) |
| 2021 | Netherlands combat training: 1.4B SEK (10-year) |
| 2021 | Poland combat training: ~1B SEK |
| 2022 | FoFTS-Next contract modification: USD 122M additional |
| 2022 | Denmark framework agreement: 15+5 years |
| 2023 | Maritime Live Training (MLT) unveiled at IMDEX Singapore |
| 2024 | UK ILT-D contract: GBP 60M (3-year + extensions to 2030) |
| 2024 | UAV training capability revealed for GAMER |
| 2024 | Indirect fire simulation fully mature — first delivery to Netherlands |
| 2025 | Spain framework agreement: EUR 34M |
| 2025 | USMC additional MCTIS: USD 37M |
| 2025 | AR3 AI-assisted AAR platform MVP announced (release Q2 2026) |
| 2025 | Training Data Insights (TDI) AI analytics platform announced |

### 1.3 Key Leadership (as of 2024-2025)

| Role | Name |
|------|------|
| Head of BU Training & Simulation | Asa Thegstrom (2019); current TBD |
| VP Training & Simulation | Joakim Alhbin |
| Head of Business Development, T&S | Hans Lindgren |
| Director T&S (Land Systems, US) | James McArthur |
| Principal PM T&S (Land, US) | Ed Jezisek |

### 1.4 Key Sites

| Site | Function |
|------|----------|
| Huskvarna, Sweden | T&S HQ — R&D, production, program management |
| Czech Republic (E-COM) | ~120 employees — software development, electronics |
| Orlando, FL (USA) | Saab Inc. — US programs, FoFTS-Next, CVTESS, TaaS |
| UK | ILT-D program support, COS |
| Amersfoort, Netherlands | MCTC operations, Dutch CTC support |
| Germany (Friedrichshafen) | JV with EADS (legacy), GUZ support |
| Norway, Finland, Canada | In-country support offices |
| Australia | Saab Australia — training services, integration |

---

## 2. Live Training Products

### 2.1 BT46 Laser Engagement System

The BT46 is Saab's flagship laser simulator and the core engagement technology of the GAMER system. It is fundamentally different from conventional MILES in its use of **true ballistic simulation**.

| Attribute | BT46 Mk III (Current) |
|-----------|----------------------|
| **Technology** | Two-way eye-safe laser with true ballistic computation |
| **Simulation Fidelity** | Models weapon/ammo parameters, time of flight, velocity, trajectory, impact point |
| **Ballistic Model** | Gyro-stabilized laser with onboard computer — round behaves like real projectile (gravity, airspeed) |
| **Laser Codes** | Dual simultaneous codes — MILES Communication Code (MCC) + OSAG 2.0 |
| **Setup** | Smartphone/tablet-based alignment and configuration |
| **Platform Adaptability** | Configurable for different vehicle platforms; backwards-compatible with Mk II components |
| **Engagement Range** | Replicates real weapon range (up to 5,000m for tank guns) |
| **Weapons Simulated** | Small arms, machine guns, ATGMs, tank main guns, RWS, helicopter weapons |
| **Variants** | BT46 (vehicle), BT47 (infantry small arms), CBL (Compact Ballistic Laser for RWS) |
| **Data Output** | Every engagement recorded — firer ID, target ID, range, time of flight, hit/miss, ammo type |
| **Network** | Wireless radio network (DAN — Data Acquisition Network) |

### 2.2 BT46 vs. MILES Comparison

| Feature | Saab BT46 Mk III | US MILES XXI / IWS2 |
|---------|-------------------|---------------------|
| **Ballistic Simulation** | True ballistic — models trajectory, gravity, velocity | Simple line-of-sight laser beam |
| **Engagement Realism** | Round has realistic flight time and path | Instantaneous hit at speed of light |
| **Hit Determination** | Computer-calculated impact based on weapon/ammo physics | Sensor detects laser = hit |
| **Range Accuracy** | Proportional to real weapon effective range | Binary (in range or not) |
| **Dual Code** | OSAG 2.0 + MCC simultaneously | MCC only |
| **International Interop** | NATO-wide (30+ nations) | Primarily US/Five Eyes |
| **Setup** | Smartphone/tablet based | Manual alignment tools |
| **Platform Integration** | Modular, adaptable to any vehicle | Specific kits per platform |
| **Data Richness** | Full engagement telemetry + GPS tracking | Limited engagement data |
| **Provider** | Saab (Sweden) | Cubic/Lockheed Martin (US) |

### 2.3 CVTESS (Combat Vehicle Tactical Engagement Simulation System)

| Attribute | Detail |
|-----------|--------|
| **Full Name** | I-MILES CVTESS (Instrumentable MILES Combat Vehicle TESS) |
| **Customer** | US Army (NTC, JRTC, JMRC) |
| **Contract** | IDIQ signed 2012; multiple options exercised |
| **Value** | $32M (options 4+5 alone); total program significantly higher |
| **Platforms** | M1 Abrams, Bradley IFV, OPFOR vehicles |
| **Technology** | BT46-based laser engagement + MILES-compatible coding |
| **Interoperability** | OSAG 2.0 upgrade enables European interoperability |
| **Latest Order** | FY2025 — $1.2M replenishment order at NTC |
| **Significance** | Saab is the **primary vehicle TESS provider to the US Army** |

### 2.4 Personnel Detection Device (PDD)

| Attribute | Detail |
|-----------|--------|
| **Type** | Soldier-worn engagement simulation system |
| **Components** | Vest with speakers + radio antenna + GPS; helmet with laser detectors/reflectors |
| **Fidelity** | "Highest fidelity in simulating combat effects for dismounted soldier" |
| **Interfaces** | Multinational training interfaces per OSAG 2.0 |
| **Network** | DAN radio network for position + engagement data |
| **Audio** | Loudspeakers for hit notification and weapon effects |

### 2.5 Small Arms Transmitter (SAT / BT47)

| Attribute | Detail |
|-----------|--------|
| **Type** | Infantry weapon laser projector |
| **Alignment** | Pocket-sized alignment device, calibrates to weapon sights |
| **Use** | Attached to infantry weapons for force-on-force engagements |
| **Deployed** | Belgium (BT47), UK, Denmark, Spain, and 25+ other nations |

### 2.6 Area Weapons Effects / Indirect Fire Simulation

| Attribute | Detail |
|-----------|--------|
| **Capability** | Single- or multi-barrel mortar/artillery fire support simulation |
| **Method** | Geo-pairing + GPS-based area effects (not line-of-sight laser) |
| **Maturity** | Fully mature as of late 2024; first customer: Royal Netherlands Army |
| **Technology** | "Technology agnostic" — combines laser, geo-pairing, GPS |
| **Significance** | Enables combined arms training with indirect fire effects |

### 2.7 Position Tracking

| Technology | Application |
|------------|-------------|
| **GPS** | Standard position tracking for all GAMER participants |
| **DAN Radio Network** | Saab-proprietary data acquisition network — position + engagement data |
| **Tablet/Smartphone** | Commander and O/C situational awareness |
| **Geo-pairing** | Area weapons effects, indirect fire |

---

## 3. GAMER System — CRITICAL ANALYSIS

### 3.1 What is GAMER?

**GAMER** = **Gunnery And Manoeuvre Exercise and Review** (also referenced as Ground, Air, Maritime, Exercise and Review in some sources). It is Saab's integrated live training system that encompasses:

1. **Engagement Simulation** — BT46/BT47 laser TESS hardware
2. **Exercise Control (EXCON)** — Software suite called **"Expert"** (also ExPERT)
3. **Communications** — DAN (Data Acquisition Network)
4. **After-Action Review (AAR)** — 2D/3D replay, analytics, reporting
5. **Data Collection** — Automated capture of all training events

GAMER is **both an AAR system AND an exercise control system** — it is a complete end-to-end training infrastructure.

### 3.2 GAMER System Architecture

```
+------------------------------------------------------------------+
|                      GAMER SYSTEM ARCHITECTURE                    |
+------------------------------------------------------------------+
|                                                                    |
|  FIELD LAYER                                                       |
|  +-----------+  +-----------+  +-----------+  +----------+        |
|  | PDD       |  | BT46      |  | BT47/SAT  |  | UAV      |       |
|  | (Soldier) |  | (Vehicle) |  | (Infantry)|  | (Drone)  |       |
|  +-----+-----+  +-----+-----+  +-----+-----+  +----+-----+      |
|        |              |              |              |               |
|        +------+-------+------+-------+------+-------+              |
|               |              |              |                      |
|          DAN RADIO NETWORK (Proprietary Mesh)                      |
|               |                                                    |
|  EXCON LAYER  |                                                    |
|  +------------+--------------------------------------------------+ |
|  |  ExPERT Software Suite                                        | |
|  |  +------------------+  +------------------+  +-------------+  | |
|  |  | Exercise Planning|  | Real-Time        |  | Data        |  | |
|  |  | & Setup          |  | Monitoring       |  | Collection  |  | |
|  |  +------------------+  | (2D Map View)    |  | (All events)|  | |
|  |  +------------------+  +------------------+  +-------------+  | |
|  |  | O/C Tools        |  | Force Tracking   |  | Engagement  |  | |
|  |  | (WE:Observe app) |  | (GPS positions)  |  | Recording   |  | |
|  |  +------------------+  +------------------+  +-------------+  | |
|  +---------------------------------------------------------------+ |
|               |                                                    |
|  AAR LAYER    |                                                    |
|  +------------+--------------------------------------------------+ |
|  |  +------------------+  +------------------+  +-------------+  | |
|  |  | 2D Map Replay    |  | Sandbox (3D MR)  |  | WE:Go App   |  | |
|  |  | (Timeline-based) |  | (Mixed Reality)  |  | (Individual)|  | |
|  |  +------------------+  +------------------+  +-------------+  | |
|  |  +------------------+  +------------------+  +-------------+  | |
|  |  | Report Generator |  | Statistics &     |  | AR3 (AI AAR)|  | |
|  |  | (PDF/HTML)       |  | Scoring          |  | (MVP Q2'26) |  | |
|  |  +------------------+  +------------------+  +-------------+  | |
|  +---------------------------------------------------------------+ |
|                                                                    |
|  ANALYTICS LAYER (NEW — 2025+)                                     |
|  +---------------------------------------------------------------+ |
|  |  Training Data Insights (TDI)                                 | |
|  |  - AI-driven analysis of structured + unstructured data       | |
|  |  - Ingests: doctrine, battle plans, radio comms, video,       | |
|  |    C2 feeds, weather, biometrics, terrain, simulation data    | |
|  |  - Statistical + ML + Generative AI (customized LLMs)         | |
|  +---------------------------------------------------------------+ |
+------------------------------------------------------------------+
```

### 3.3 GAMER Components Detailed

| Component | Description | Status |
|-----------|-------------|--------|
| **BT46/BT47** | Laser engagement hardware (vehicle + infantry) | Production — Mk III current |
| **PDD** | Personnel Detection Device — soldier-worn sensors | Production |
| **DAN** | Data Acquisition Network — proprietary radio mesh | Production |
| **ExPERT** | EXCON software suite — planning, monitoring, control | Production |
| **WE:Observe** | O/C field data collection app — subjective observations | Production |
| **WE:Go** | Individual soldier AAR app — personalized debrief | Production (since 2016) |
| **Sandbox** | Mixed-reality 3D AAR tool using Vricon One World Terrain | Production (since 2019) |
| **Manpack** | Man-portable small unit EXCON — identical CTC functionality | Production |
| **ExTerm** | EXCON terminal | Production |
| **MTS** | Modular Target System — laser-based training targets | Production |
| **AR3** | AI-assisted AAR chatbot platform | MVP expected Q2 2026 |
| **TDI** | Training Data Insights — AI analytics platform | In development (2025+) |

### 3.4 GAMER Data Ingestion & Output

#### Data Collected

| Data Type | Source | Method |
|-----------|--------|--------|
| GPS positions (all participants) | PDD, BT46, vehicles | DAN radio network, continuous |
| Engagement events (every shot) | BT46/BT47 lasers | Automatic — firer, target, weapon, ammo, result |
| Casualty events | PDD/BT46 detectors | Automatic — who hit whom, when, where |
| Movement tracks | GPS | Continuous recording |
| O/C observations | WE:Observe app | Manual — subjective field observations |
| Radio communications | Radio intercept (TDI) | AI processing (new) |
| C2 data feeds | Integrated C2 systems | Digital ingest (TDI) |
| Video | Cameras, drones | AI processing (TDI) |
| Biometrics | Wearable sensors | Future integration (TDI) |
| Weather/terrain | External feeds | Contextual data for analysis |
| Doctrine/battle plans | Pre-loaded documents | AI analysis against actual performance (TDI) |

#### Data Output

| Output | Description |
|--------|-------------|
| **Real-time 2D map** | Live force tracking, engagement events on map |
| **2D replay** | Timeline-controlled playback of entire exercise |
| **3D Sandbox replay** | Mixed-reality 3D terrain with unit movements |
| **Individual soldier reports** | WE:Go app — personalized debrief per soldier |
| **Unit performance scoring** | Hit rates, casualty ratios, engagement statistics |
| **Mission success metrics** | Objective completion, task performance |
| **AI-generated insights** | AR3/TDI — natural language analysis of performance |
| **Hot debrief tools** | Rapid preliminary feedback for immediate AAR |
| **Comprehensive final AAR reports** | Detailed post-exercise analysis documents |

### 3.5 GAMER Scalability

| Echelon | Support Level |
|---------|---------------|
| **Individual soldier** | WE:Go app personal debrief |
| **Fire team / Squad** | Small unit AAR via Manpack |
| **Platoon** | Standard GAMER EXCON |
| **Company** | Full GAMER system |
| **Battalion** | MCTC / CTC level (Netherlands: "world's largest mobile CTC") |
| **Brigade Combat Team** | Full-scale CTC exercises |
| **Joint/Multinational** | Multi-brigade, multi-national exercises (e.g., Aurora 23) |

### 3.6 GAMER vs. Cubic CATS/Metrix Comparison

| Feature | Saab GAMER | Cubic CATS/Metrix |
|---------|------------|-------------------|
| **Engagement Simulation** | BT46 true ballistic | MILES line-of-sight |
| **Ballistic Fidelity** | Trajectory, gravity, flight time modeled | Binary hit/miss at light speed |
| **EXCON** | ExPERT software suite | CATS (Core Automated Tracking System) |
| **AAR** | 2D/3D replay, Sandbox MR, WE:Go, AR3 | Metrix analytics, HITS/IOS |
| **AI Analytics** | TDI + AR3 (in development, 2025-26) | Cubic AI/ML analytics (in development) |
| **Indirect Fire** | Geo-pairing area effects (mature 2024) | AWES (Area Weapons Effects System) |
| **Position Tracking** | GPS via DAN radio network | GPS + UWB (Indoor/Outdoor) |
| **O/C Tools** | WE:Observe app | O/C Toolkit |
| **Individual Debrief** | WE:Go soldier app | Limited |
| **Interoperability** | OSAG 2.0 + MCC dual-code | MCC (MILES Communication Code) |
| **NATO Standard** | OSAG 2.0 = de facto European standard | MILES = de facto US standard |
| **Scalability** | Individual to brigade+ | Squad to division |
| **Maritime Capability** | MLT (Maritime Live Training) — 2023 | Limited naval |
| **UAV Integration** | UAV training capability (2024) | Emerging |
| **3D AAR** | Sandbox (Vricon 3D terrain) | VBS/OneSAF integration |
| **Market Presence** | 30+ nations, dominant in Europe | NTC/JRTC (US), some international |
| **Business Model** | Equipment + TaaS (Training as a Service) | Equipment + O&M contracts |

---

## 4. Virtual & Constructive Training

### 4.1 Ground Combat Indoor Trainer (GCIT)

| Attribute | Detail |
|-----------|--------|
| **Type** | Virtual weapons trainer using replica weapons |
| **Weapons** | Carl-Gustaf M4, AT4 family, small arms, mortars |
| **Fidelity** | Faithful replica weapons + lifelike virtual environment |
| **Capacity** | Studio version: up to 10 soldiers simultaneously |
| **Customers** | Finland (first, 2019), Sweden, and growing international |
| **Pricing** | USD 37M for Finnish contract (2022) — includes hardware + installation |

### 4.2 Air Domain Training

| Product | Description |
|---------|-------------|
| **Air Defence Training Centre** | International aviation centre for air defence operations |
| **LVC Integration** | Live-Virtual-Constructive integration solutions |
| **BT46 Helicopter Firing System** | True ballistic simulation for helicopter weapons (PAH-1 A1, others) |
| **UAV Integration** | Drone as asset or threat during exercises (revealed 2024) |

### 4.3 Maritime Live Training (MLT)

| Attribute | Detail |
|-----------|--------|
| **Unveiled** | IMDEX 2023, Singapore |
| **Based On** | GAMER system adapted for naval domain |
| **Capabilities** | Naval gunnery simulation, coastal defence, maritime scenarios |
| **Subsystems** | Naval gunnery simulator, coastal defence simulator |
| **Similar To** | USMC FoFTS-Next maritime capabilities |
| **AAR** | Full GAMER EXCON/AAR capabilities for maritime |
| **Threats Simulated** | Drone swarms, improvised attack vessels, conventional threats |

### 4.4 LVC Integration

| Aspect | Detail |
|--------|--------|
| **Approach** | "Beyond Live Training" — combines live + virtual technologies |
| **Standards** | DIS, HLA (assumed, standard for LVC) |
| **Capability** | Non-line-of-sight effects (e.g., Fire & Observe missiles) |
| **Integration** | Virtual entities injected into live exercise environment |
| **Maturity** | Demonstrated capability; expanding |

---

## 5. Training Management & Analytics

### 5.1 Analytics Evolution

| Generation | Timeframe | Capability |
|------------|-----------|------------|
| **Gen 1** | 1990s-2015 | Basic data collection — GPS tracks, engagement logs |
| **Gen 2** | 2016-2023 | ExPERT suite, WE:Go individual app, WE:Observe O/C app, Sandbox 3D |
| **Gen 3** | 2024-2026+ | AI-driven: TDI analytics, AR3 AI AAR chatbot, generative AI insights |

### 5.2 Training Data Insights (TDI) — 2025+

| Attribute | Detail |
|-----------|--------|
| **Type** | Integrated end-to-end AI analytics platform |
| **Data Sources** | Structured (GPS, engagements) + Unstructured (doctrine, radio, video, C2, biometrics) |
| **AI Methods** | Statistical analysis + Machine Learning + Generative AI (customized LLMs) |
| **Key Feature** | Compares actual performance against doctrine and battle plans |
| **Visualization** | Interactive exercise site view — select data by location, unit, or parameter |
| **Benchmarking** | Compare attributes of different units, benchmark progress over time |
| **Doctrine Evaluation** | Measures adherence to doctrine; can evaluate doctrine effectiveness |
| **Exercise Planning** | Future: suggest exercise setups based on previous results |
| **Status** | In development / early deployment (announced Dec 2025) |

### 5.3 AR3 AI-Assisted AAR Platform

| Attribute | Detail |
|-----------|--------|
| **Name** | AR3 (After Action Review AI) |
| **Type** | AI chatbot for exercise debrief |
| **Interface** | Natural language — user asks "How did platoon X perform?" |
| **Data Source** | EXCON (Expert) software suite — sensors, GPS, engagement data |
| **AI Response** | Detailed answers on success/failure vs. pre-loaded goals/objectives |
| **MVP Release** | End of Q2 2026 |
| **Target Customers** | Existing EXCON users: UK, Poland, Denmark, others |
| **Key Quote** | "God's truth" — unbiased assessment based on objective data (Ed Jezisek, Saab) |

### 5.4 WE:Observe — O/C Data Collection

| Attribute | Detail |
|-----------|--------|
| **Type** | Mobile app for Observer/Controllers |
| **Purpose** | Primary subjective performance observations in the field |
| **Data** | Aggregated with objective GAMER data for holistic assessment |
| **Output** | Combined subjective + objective training performance measurement |

### 5.5 WE:Go — Individual Soldier AAR

| Attribute | Detail |
|-----------|--------|
| **Type** | Mobile app for individual soldiers |
| **Purpose** | Personalized debrief — each soldier sees own performance |
| **Introduced** | 2016 |
| **Innovation** | Moved from group AAR to individual feedback |
| **Data** | Personal shooting accuracy, movement, engagement timing |

### 5.6 Readiness Assessment

Saab does not currently offer a standalone **training management system** (TMS) or **readiness assessment** platform comparable to US Army DTMS. However:

- TDI provides **longitudinal benchmarking** (comparing units over time)
- TDI can measure unit **strengths and weaknesses at different echelons**
- Future TDI capability: compare across multiple exercises
- AR3 provides rapid readiness-relevant feedback

This is a **significant gap** that CORTEX RANGE could exploit.

---

## 6. Architecture & Integration

### 6.1 Interoperability Standards

| Standard | Saab Support |
|----------|-------------|
| **OSAG 2.0** | Primary international laser code standard — Saab is the author/owner |
| **MCC (MILES Communication Code)** | Supported via dual-code BT46 Mk III |
| **DIS (Distributed Interactive Simulation)** | Likely supported for LVC (not explicitly confirmed in open sources) |
| **HLA (High Level Architecture)** | Likely supported for LVC integration |
| **NATO STANAG** | OSAG 2.0 is de facto NATO standard for TESS interoperability |
| **SAPIENT** | Not mentioned — unlike CORTEX RANGE concept |
| **TAK/ATAK** | Not mentioned — unlike CORTEX RANGE concept |

### 6.2 OSAG 2.0 Standard

| Attribute | Detail |
|-----------|--------|
| **Full Name** | Open Systems Architecture for GAMER |
| **Origin** | Developed by Saab as international interoperability standard |
| **Purpose** | Standardize laser engagement codes across nations |
| **Variants** | OSAG 2.0 Basic (subset, used at GUZ), OSAG 2.0 Standard (full) |
| **Adoption** | Most European nations, Austria, Poland, UK, Denmark, Netherlands, etc. |
| **US Compatibility** | Dual-code with MCC — single system works in US or European exercises |
| **Significance** | Saab effectively **owns the interoperability standard** for European TESS |

### 6.3 Network Architecture

| Component | Detail |
|-----------|--------|
| **Field Network** | DAN (Data Acquisition Network) — Saab proprietary radio mesh |
| **EXCON Network** | Client-server architecture at EXCON site |
| **Mobile CTC** | Van-based MCTC — self-contained training center |
| **Manpack** | Man-portable EXCON for small unit training |
| **Connectivity** | Primarily tactical radio; some cellular/WiFi for rear areas |
| **Cloud** | Not mentioned — appears to be on-premise/tactical |

### 6.4 Integration with Operational C2

| Aspect | Detail |
|--------|--------|
| **Saab 9LV CMS** | Saab's own naval combat management system — potential integration path but not confirmed for GAMER |
| **TDI C2 Ingest** | TDI can ingest C2 data feeds for analysis (announced 2025) |
| **CBRN Integration** | Argon Electronics PlumeSIM integrated with GAMER |
| **Open Architecture** | "Technology agnostic" — laser + geo-pairing + GPS + other |

---

## 7. Key Contracts & Deployments

### 7.1 Major Contract Summary

| Customer | Program | Value | Year | Duration |
|----------|---------|-------|------|----------|
| **US Marine Corps** | FoFTS-Next (SATOC) | USD 127.9M (base) | 2021 | Multi-year |
| **US Marine Corps** | FoFTS-Next modification | USD 122M | 2022 | Ongoing |
| **US Marine Corps** | MCTIS additional equipment | USD 37M | 2025 | 2025-2027 |
| **US Army** | CVTESS IDIQ | $32M+ (options 4+5) | 2012+ | IDIQ |
| **US Army** | DISE OSAG 2.0 upgrades | Undisclosed | 2016 | - |
| **UK MoD** | ILT-D (Instrumented Live Training) | GBP 60M | 2024 | 3yr + ext to 2030 |
| **UK MoD** | DFWES support (predecessor) | GBP 60M | 2020 | 3yr + ext |
| **Netherlands** | Combat Training Solutions | SEK 1.4B (10yr) | 2021 | 10yr + 5yr opt |
| **Poland** | Complete live training + 4 CTCs | SEK ~1B | 2021 | Multi-year |
| **Denmark** | Framework agreement | Undisclosed | 2022 | 15yr + 5yr opt |
| **Finland** | Combat training simulators | USD 37M | 2022 | 2025-2027 |
| **Spain** | Framework agreement | EUR 34M (potential max) | 2025 | Multi-year |
| **Kenya** | Complete GAMER system | Undisclosed | 2022 | - |
| **Estonia** | BT46 training systems | Undisclosed | 2017+ | Ongoing since 2008 |
| **Austria** | OSAG 2.0 upgrade (DuSim) | Undisclosed | 2010 | - |
| **Belgium** | GAMER Mobile CTC | Undisclosed | Recent | - |
| **Germany** | GUZ training support | Undisclosed | Legacy | - |
| **France** | Laser simulators (helicopter) | Undisclosed | 2001 | - |
| **Chile** | BT46 for Leopard 2A4 | Undisclosed | 2024 | - |

### 7.2 USMC FoFTS-Next — Key Program

| Attribute | Detail |
|-----------|--------|
| **Program** | Force on Force Training Systems - Next |
| **Type** | Single Award Task Order Contract (SATOC) |
| **Scope** | Full turnkey live training system — laser TESS + EXCON + AAR |
| **Total Value** | USD 127.9M base + USD 122M modification + USD 37M (2025) = **~USD 287M+ cumulative** |
| **Significance** | Saab's largest single US training program; replaces legacy USMC MILES |
| **Features** | Open systems design, high fidelity, BT46-based |

### 7.3 Countries Using GAMER / Saab Live Training

Based on open sources, confirmed or likely GAMER users include:

| Region | Countries |
|--------|-----------|
| **Nordics** | Sweden, Denmark, Finland, Norway |
| **Western Europe** | UK, Netherlands, Belgium, Germany, France, Austria, Spain |
| **Eastern Europe** | Poland, Estonia, Czech Republic |
| **Americas** | USA (Army + USMC), Canada |
| **Africa** | Kenya, South Africa |
| **Asia-Pacific** | Australia, Singapore |
| **South America** | Chile |
| **Other** | ~10+ additional nations (totaling 30+) |

---

## 8. Business Model & Pricing

### 8.1 Sales Model

| Model | Description |
|-------|-------------|
| **Equipment Sale** | Hardware (BT46, PDD, BT47, EXCON) + software licenses |
| **Framework Agreements** | Long-term (10-20yr) with equipment + support (Netherlands, Denmark, Spain) |
| **IDIQ Contracts** | Indefinite delivery/indefinite quantity (US CVTESS) |
| **SATOC** | Single Award Task Order Contract (USMC FoFTS-Next) |
| **Through-Life Support** | COS (Contractor Operational Support) — embedded Saab staff worldwide |
| **CLS** | Contractor Logistic Support — spares, maintenance, repairs |
| **Training as a Service (TaaS)** | Saab provides complete training capability as a service — no customer ownership of hardware |

### 8.2 Pricing Estimates (from Contract Data)

| Scale | Estimated Cost | Basis |
|-------|---------------|-------|
| **Individual soldier kit (PDD + SAT)** | $3,000-8,000 per soldier | Estimated from system-level contracts |
| **Vehicle system (BT46 Mk III)** | $25,000-80,000 per vehicle | Estimated from CVTESS/FoFTS data |
| **Battalion-level CTC** | $30-100M | Netherlands SEK 1.4B for 10yr; Poland SEK 1B |
| **Complete national system** | $100-300M+ over lifecycle | Full equipment + 10-20yr support |
| **Through-life support** | $5-10M/year | Netherlands: SEK 66.9M/yr = ~USD 6.5M/yr |
| **TaaS (per exercise)** | $500K-2M per exercise (est.) | Based on Northern Strike 2024 deployment |

### 8.3 Training as a Service (TaaS) — New Model

| Attribute | Detail |
|-----------|--------|
| **Concept** | Saab provides complete training capability without customer hardware ownership |
| **Includes** | GAMER equipment, EXCON, personnel, AAR, logistics |
| **Target** | US National Guard, allied forces, "almost anywhere" |
| **Advantage** | Eliminates O&M tail; customer focuses on training, not equipment |
| **Demonstrated** | Michigan Northern Strike exercise (2024) |
| **Pricing** | Per-exercise or per-training-day basis (details TBD) |

### 8.4 Technology Transfer

| Aspect | Detail |
|--------|--------|
| **Joint Ventures** | EADS Deutschland JV (2005) — local production in Germany |
| **Local Production** | Czech Republic subsidiary (E-COM) — software/electronics |
| **In-Country Support** | Embedded staff in customer nations (UK, US, Netherlands, etc.) |
| **Offset/IC** | Offered where required; Australian Global Supply Chain participant |

---

## 9. Strengths & Weaknesses

### 9.1 Strengths

| # | Strength | Detail |
|---|----------|--------|
| S1 | **True ballistic simulation** | BT46 is unique — no other system models actual projectile physics at this fidelity |
| S2 | **30+ nation installed base** | Massive global footprint creates network effect and switching costs |
| S3 | **Owns OSAG 2.0 standard** | Saab wrote the European interoperability standard — immense lock-in |
| S4 | **Complete ecosystem** | End-to-end: engagement sim + EXCON + AAR + analytics + support |
| S5 | **Dual MILES/OSAG compatibility** | BT46 Mk III works in both US and European environments |
| S6 | **Scalability** | Individual soldier to multinational brigade-level exercises |
| S7 | **Expanding into maritime + air** | MLT (2023), helicopter firing, UAV integration (2024) |
| S8 | **AI/ML investment** | TDI and AR3 bring AI analytics to training (first mover in live training AI) |
| S9 | **TaaS business model** | Removes customer O&M burden; opens new markets |
| S10 | **Strong US position** | 25% US market share; USMC FoFTS-Next; Army CVTESS at NTC/JRTC |
| S11 | **Long-term contracts** | 10-20 year framework agreements (Denmark 15+5, Netherlands 10+5) |
| S12 | **Parent company strength** | Saab AB SEK 63B revenue; SEK 187B backlog; defense upswing |

### 9.2 Weaknesses

| # | Weakness | Detail |
|---|----------|--------|
| W1 | **No live-fire training analytics** | GAMER is force-on-force only — does not address live-fire scoring/analytics |
| W2 | **No acoustic sensing** | Cannot detect or analyze real gunshots — only simulated laser engagements |
| W3 | **Proprietary lock-in** | DAN radio, OSAG 2.0, ExPERT — customer dependent on Saab ecosystem |
| W4 | **High system cost** | $30-300M for national programs — prohibitive for developing nations |
| W5 | **No standalone analytics product** | TDI/AR3 are integrated into GAMER — cannot be sold independently (yet) |
| W6 | **No readiness management system** | No TMS equivalent for longitudinal readiness tracking |
| W7 | **AI features immature** | AR3 MVP not until Q2 2026; TDI still in development |
| W8 | **Heavy logistics tail (without TaaS)** | Traditional model requires significant O&M infrastructure |
| W9 | **Limited beyond force-on-force** | Does not address marksmanship training, qualification, live-fire ranges |
| W10 | **Cloud/edge not confirmed** | Appears on-premise only — no cloud-native or edge computing architecture |
| W11 | **No C-UAS training** | Despite UAV integration for F-o-F, no specific counter-drone training scoring |
| W12 | **Slow adoption of open standards** | TAK/ATAK, SAPIENT not mentioned; limited beyond OSAG/MILES codes |

---

## 10. Design Paradigm Comparison — Saab GAMER vs. CORTEX RANGE

### 10.1 Fundamental Philosophy

| Attribute | Saab GAMER | CORTEX RANGE |
|-----------|------------|--------------|
| **Primary Domain** | Force-on-force (simulated combat) | Live-fire training (real ammunition) |
| **Core Technology** | Laser engagement (BT46 true ballistic) | Acoustic sensing (LOMAH + AI analytics) |
| **What It Measures** | Simulated engagements between opposing forces | Real bullet impacts and shooting performance |
| **Training Type** | Tactical training — maneuver, C2, combined arms | Marksmanship, qualification, live-fire exercises |
| **Data Source** | Laser hits/misses + GPS tracking | Acoustic miss/hit detection + shooter analytics |
| **AI Role** | Emerging (TDI/AR3 in 2025-26) | Core — AI-driven analytics from day one |
| **User** | Brigade/battalion trainers, CTCs | Range operators, company/platoon trainers |
| **Scale** | National defense programs | Individual range systems |
| **Heritage** | 30+ years of laser TESS evolution | New entrant with modern AI-first design |

### 10.2 Feature Comparison

| Feature | Saab GAMER | CORTEX RANGE | Winner |
|---------|------------|--------------|--------|
| Force-on-force training | Comprehensive | Not applicable | GAMER |
| Live-fire accuracy scoring | Not available | Core capability | CORTEX |
| Real-time shot analysis | Laser engagement only | Acoustic + AI | CORTEX |
| Marksmanship improvement | Not available | AI coaching | CORTEX |
| Combined arms training | Full combined arms | Not applicable | GAMER |
| Exercise control (EXCON) | Full suite (ExPERT) | Lightweight | GAMER |
| After-action review | 2D/3D/AI AAR | AI-powered AAR | Tie (different domains) |
| Individual soldier feedback | WE:Go app | AI analytics per shooter | Tie |
| GPS force tracking | Core capability | Optional/limited | GAMER |
| Acoustic analysis | Not available | Core capability | CORTEX |
| AI/ML analytics | Emerging (2025-26) | Native/core design | CORTEX |
| Edge computing | Not confirmed | Edge-first architecture | CORTEX |
| Cloud connectivity | Not confirmed | Cloud-native design | CORTEX |
| Open standards (TAK/ATAK) | Not supported | Planned integration | CORTEX |
| Interoperability (NATO TESS) | OSAG 2.0 + MCC | Not applicable | GAMER |
| Scalability (echelon) | Squad to brigade+ | Individual to company | GAMER |
| Multi-national training | 30+ nation interop | Not applicable | GAMER |
| Deployment speed | Hours-days (CTC setup) | Minutes (acoustic sensors) | CORTEX |
| Training management | Partial (TDI future) | Integrated | CORTEX |
| Readiness assessment | Not available (gap) | Core capability | CORTEX |

### 10.3 Price Comparison

| Metric | Saab GAMER | CORTEX RANGE |
|--------|------------|--------------|
| **Per-lane/per-position** | $3,000-8,000+ (soldier kit) | $5,000-8,000 (acoustic lane) |
| **Battalion system** | $30-100M | N/A (not battalion F-o-F) |
| **Per range** | Not applicable (not live-fire) | $15,000-25,000 |
| **Annual support** | $5-10M/yr (national CTC) | $2,000-5,000/yr (per range est.) |
| **Total system lifecycle** | $100-300M+ (national) | $50K-500K (range network) |
| **Target customer budget** | National defense programs ($50M+) | Training commands ($15K-250K) |

### 10.4 Market Overlap Analysis

```
SAAB GAMER DOMAIN                    CORTEX RANGE DOMAIN
(Force-on-Force)                     (Live-Fire)
+-------------------+               +-------------------+
|                   |               |                   |
| Tactical training |               | Marksmanship      |
| Combined arms     |               | Qualification     |
| Maneuver          |   OVERLAP     | Live-fire scoring |
| C2 exercise       |   ZONE        | Range management  |
| Multi-national    +-----+-----+   | Shot analytics    |
| Brigade+ scale    |     |     |   | AI coaching       |
|                   | AAR |Data | |                   |
|                   |Analytics  |   |                   |
+-------------------+-----+-----+---+-------------------+
                          |
                    Both provide:
                    - Training data collection
                    - Performance analytics
                    - After-action review
                    - Individual feedback
                    BUT for different training types
```

### 10.5 Differentiation — Gaps CORTEX RANGE Exploits

| Gap in Saab GAMER | CORTEX RANGE Response |
|--------------------|-----------------------|
| **No live-fire capability** | Core mission — acoustic miss/hit detection for real ammunition |
| **No acoustic sensing** | Microphone arrays for shot detection and analysis |
| **No marksmanship analytics** | AI-driven shooting performance analysis and improvement coaching |
| **No range management** | Integrated range operations and safety management |
| **Massive system cost ($30M+)** | Affordable per-range system ($15-25K) |
| **Complex logistics** | Minimal footprint — edge sensors + cloud analytics |
| **No cloud/edge architecture** | Cloud-native, edge-first design |
| **AI is bolt-on (2025-26)** | AI is core architectural principle from inception |
| **No readiness tracking** | Longitudinal performance tracking and readiness assessment |
| **No open C2 integration** | TAK/ATAK/SAPIENT integration planned |
| **No qualification scoring** | Automated qualification scoring and certification |
| **Limited to TESS ecosystem** | Works with any weapon, any range, any ammunition |

### 10.6 Complementary Positioning

CORTEX RANGE and Saab GAMER are fundamentally **complementary, not competitive**:

| Training Phase | System |
|----------------|--------|
| **Individual marksmanship** | CORTEX RANGE |
| **Squad live-fire** | CORTEX RANGE |
| **Company qualification** | CORTEX RANGE |
| **Force-on-force platoon** | Saab GAMER |
| **Combined arms battalion** | Saab GAMER |
| **Multi-national brigade+** | Saab GAMER |
| **Range analytics (any level)** | CORTEX RANGE |
| **Exercise analytics (F-o-F)** | Saab GAMER |

**Strategic Implication:** CORTEX RANGE should position as the live-fire training analytics complement to GAMER, not a competitor. In the long term, data from CORTEX RANGE (live-fire performance) could feed into GAMER's TDI platform for holistic readiness assessment. A potential integration/partnership with Saab could be explored.

---

## 11. Key Intelligence Findings for CORTEX RANGE

### 11.1 Critical Takeaways

1. **Saab does NOT compete in live-fire training analytics** — GAMER is 100% force-on-force laser engagement. This is the #1 gap CORTEX RANGE exploits.

2. **Saab's AI is 2+ years behind CORTEX RANGE's design philosophy** — AR3 MVP not until Q2 2026; TDI still in development. CORTEX RANGE has AI as core architecture.

3. **Saab owns the European TESS interoperability standard (OSAG 2.0)** — Any CORTEX RANGE integration with force-on-force systems must account for OSAG 2.0.

4. **Saab's TaaS model is disruptive** — Training-as-a-Service removes equipment ownership burden. CORTEX RANGE should consider a similar SaaS/TaaS pricing model.

5. **30+ nation installed base** — Saab has relationships with virtually every NATO training command. CORTEX RANGE could leverage these same customers for complementary live-fire capability.

6. **No readiness management system exists at Saab** — This is a gap across the entire training industry. CORTEX RANGE's integrated readiness tracking is a unique differentiator.

7. **Price point is orders of magnitude different** — Saab sells $30-300M national programs; CORTEX RANGE sells $15-25K range systems. These serve completely different budget lines and procurement processes.

8. **Saab's data architecture is closed/proprietary** — DAN, ExPERT, OSAG 2.0 are all Saab-owned. CORTEX RANGE's open architecture (TAK, cloud, API-first) is a competitive advantage for integration.

### 11.2 Competitive Risk Assessment

| Risk | Level | Rationale |
|------|-------|-----------|
| Saab entering live-fire market | **LOW** | No acoustic technology; 30-year focus on laser TESS |
| Saab TDI/AR3 competing with CORTEX analytics | **MEDIUM** | TDI could eventually analyze any data source; but currently GAMER-only |
| Saab bundling analytics with GAMER as standard | **LOW** | TDI/AR3 are premium add-ons, not included in base GAMER |
| Saab acquiring acoustic/live-fire company | **LOW-MEDIUM** | Possible but not aligned with current strategy (Dynamics focus on weapons + TESS) |
| Customer expecting GAMER-level ecosystem from CORTEX | **MEDIUM** | Set expectations: CORTEX RANGE is live-fire, not force-on-force |

### 11.3 Partnership Opportunities

| Opportunity | Description |
|-------------|-------------|
| **Data Integration** | CORTEX RANGE live-fire data feeds into Saab TDI for holistic readiness |
| **Complementary Sales** | Saab GAMER customers need live-fire training — natural cross-sell |
| **TaaS Model** | CORTEX RANGE delivered as part of Saab TaaS offerings |
| **Technology Partnership** | CORTEX acoustic analytics + Saab EXCON/AAR infrastructure |
| **Standards Alignment** | CORTEX data formatted for OSAG/DIS/HLA interoperability |

---

## 12. Summary Assessment

| Dimension | Rating | Comment |
|-----------|--------|---------|
| **Technology Maturity** | 9/10 | 30+ years of BT46 evolution; GAMER is world-class |
| **Market Position** | 9/10 | Dominant in Europe; 25% US share; 30+ nations |
| **AI/Analytics** | 5/10 | TDI/AR3 promising but immature; MVP not until 2026 |
| **Live-Fire Capability** | 0/10 | **Does not exist** — entirely force-on-force |
| **Architecture Openness** | 4/10 | Proprietary DAN, ExPERT; OSAG 2.0 is open but Saab-controlled |
| **Price Accessibility** | 3/10 | National-scale programs; prohibitive for small customers |
| **Threat to CORTEX RANGE** | 2/10 | Different domain entirely; complementary positioning |
| **Partnership Potential** | 8/10 | Strong complementary fit; shared customer base |

**Bottom Line:** Saab GAMER is the world leader in force-on-force live training simulation but has **zero presence in live-fire training analytics**. CORTEX RANGE occupies a completely different market segment with no direct competition from Saab. The optimal strategy is **complementary positioning** — CORTEX RANGE for live-fire, GAMER for force-on-force — with potential data integration via TDI in the future.

---

## References

1. Saab AB. "Live Training." saab.com/products/live-training
2. Saab AB. "Training and Simulation | Land." saab.com/products/land/training-and-simulation
3. Saab AB. "Instant learning, long-term results." Dec 2025. saab.com/newsroom/stories/2025/december/instant-learning-long-term-results
4. Breaking Defense. "Saab developing minimally viable AI-assisted after-action review platform." Dec 2025.
5. Saab AB. "Saab Awarded U.S. Marine Corps Contract for FoFTS-Next." Jun 2021.
6. Saab AB. "Saab receives order for additional Live Training equipment from USMC." Jan 2025.
7. Saab AB. "British Army signs new contract for Saab ILT-D." Apr 2024.
8. Saab AB. "Saab to Deliver Combat Training Solutions to the Netherlands." Jun 2021.
9. Saab AB. "Saab to deliver combat training solutions to Poland." 2021.
10. Saab AB. "Denmark Selects Saab's Live Training Systems." 2022.
11. Saab AB. "Saab signs contract with Spanish Army for Live Training Systems." Dec 2025.
12. Saab AB. "Saab Receives Contract from Finland for Combat Training Simulators." 2022.
13. Janes. "Saab explores new markets for its live-training simulation." Dec 2024.
14. Janes. "Saab unveils new training simulation system for naval forces." May 2023.
15. Janes. "Saab launches AI-based training analysis." 2025.
16. Wikipedia. "Saab Training and Simulation." en.wikipedia.org
17. Wikipedia. "Multiple Integrated Laser Engagement System." en.wikipedia.org
18. Saab AB. "Potential for further growth in Training & Simulation." Annual Report 2021.
19. Saab AB. "Saab Unveils New Training Solutions" (Sandbox). Dec 2019.
20. Saab AB. "Training as a Service: The Future of US Armed Forces Training." 2023.
21. Saab AB. "Training for the new threat from above." Dec 2024.
22. Saab AB. "True ballistic training for true battle readiness." Apr 2024.
23. Saab AB. "Revolutionizing Naval Training." saab.com/markets/singapore
24. Saab AB. "Saab introduces BT 46 Mk III at I/ITSEC." Nov 2017.
25. Saab AB. "Saab Receives Upgrade Orders for US Army Training Systems." 2016.
26. Army Technology. "US Army to receive CVTESS trainers from Saab." 2012.
27. Army Technology. "Poland's AWL to use Saab BT46 to upgrade GAMER system." 2018.
28. Argon Electronics. "SAAB Gamer CBRN Live Training system." argonelectronics.com
29. Saab AB. Year-End Report 2024. Feb 2025.
30. Saab AB. Annual and Sustainability Report 2024.
