---
project: CORTEX-C2
phase: 0
type: reverse-engineering
subject: Saab 9LV Combat Management System (Sweden)
version: 1.0
created: 2026-02-12
status: complete
---

# RE Analysis: Saab 9LV Combat Management System

## Executive Summary

Saab's 9LV is the world's most widely exported Western naval Combat Management System (CMS), with 250+ deliveries to 20+ navies across all continents. Originating in 1968 as a Swedish Navy fire control system, 9LV has evolved over five generations (Mk1 through Mk4/NextGen) into a full-spectrum C4I platform covering anti-air, anti-surface, anti-submarine, and mine warfare. The system's open architecture built on DDS middleware, proven integration with 50+ sensor/weapon types, and scalability from patrol boats to LHDs make it a formidable benchmark. However, 9LV's complexity, pricing ($5-50M+ per ship), and heavyweight integration requirements create a significant market gap below the corvette tier -- precisely where CORTEX NAVAL can compete.

---

## 1. Company Profile: Saab AB

### Overview

| Attribute | Detail |
|-----------|--------|
| **Legal name** | Saab AB (publ) |
| **Headquarters** | Stockholm / Linkoping, Sweden |
| **Founded** | 1937 (originally Svenska Aeroplan AB) |
| **Industry** | Aerospace & Defense |
| **Stock** | SAAB-B on Nasdaq OMX Stockholm |
| **CEO** | Micael Johansson |
| **Employees** | ~23,000 (2024) |
| **Revenue (2024)** | SEK 63.8B (~$5.98B USD) |
| **EBIT (2024)** | SEK 5.6B (8.9% margin) |
| **Order backlog** | SEK 187B (~$17.5B USD) -- record level |
| **Market cap** | ~SEK 500B+ (~$47B+ USD, Feb 2026) |
| **Ownership** | Public; FAM/Wallenberg family ~38.9% of shares, 47.7% of votes |

**NOTE**: Saab AB is entirely separate from Saab Automobile (which was sold to GM in 2000 and subsequently ceased operations). The defense company retained the Saab name and brand.

### Business Areas (2024 Structure)

| Business Area | Focus | Key Products |
|---------------|-------|--------------|
| **Aeronautics** | Military & civil aviation | Gripen E/F fighter, GlobalEye AEW&C, T-7A trainer components |
| **Dynamics** | Missiles, ground combat, training | Carl-Gustaf, AT4, NLAW, RBS-15, MSHORAD, training simulation |
| **Surveillance** | C2, radar, EW, naval combat systems | **9LV CMS**, Giraffe radars, ARTHUR, GlobalEye sensors, TactiCall, EW suites |
| **Kockums** | Submarines, surface ships | A26 Blekinge-class submarine, Visby-class corvette, CB90 combat boat |
| **Combitech** | Consulting & technology services | Systems engineering, cybersecurity, test & evaluation |

### Financial Performance (2024)

| Metric | 2024 | 2023 | Change |
|--------|------|------|--------|
| Revenue | SEK 63.8B | SEK 51.6B | +23.5% |
| Order intake | SEK 77.3B | SEK 62.6B | +24% |
| EBIT | SEK 5.6B | SEK 4.3B | +30% |
| EBIT margin | 8.9% | 8.3% | +0.6pp |
| Order backlog | SEK 187B | SEK 153B | +22% |
| Employees | ~23,000 | ~22,000 | +~1,000 |

The company is on a strong growth trajectory driven by the post-2022 European defense spending surge. Revenue growth has been double-digit for three consecutive years. The Surveillance business area (which houses 9LV) has been described as delivering "strong results" with "exceptional project completions" in recent quarters.

### 2025 Outlook
- Organic sales growth: 12-16%
- EBIT growth: higher than organic sales growth
- Major new contracts: Gripen E/F for Colombia (EUR 3.1B), Giraffe 1X for US Army ($46M), multiple Trackfire RWS orders

---

## 2. 9LV Combat Management System -- Architecture Deep Dive

### 2.1 Historical Evolution

| Generation | Period | Key Innovation | Technology Base |
|------------|--------|----------------|-----------------|
| **Mk1** | 1968-1977 | Analogue fire control + Ceros Ku-band radar | Analogue computers, hydraulic directors |
| **Mk2** | 1977-1983 | Digital processing, first software-based system | Fixed-program digital computers |
| **Mk2.5** | 1983-1987 | High-level language (RTL/2), new bus architecture | Upgraded processors, new busses |
| **Mk3** | 1987-2005 | Distributed architecture, Ada language, multi-function consoles | Ethernet LAN, OS-9 RTOS, "Base System 2000" |
| **Mk3E** | 1998-2008 | COTS migration, Windows NT | Intel cPCI, Windows NT, commercial HW |
| **Mk4** | 2008-present | Naval Open Architecture, DDS middleware, Java | DDS pub/sub, Java + Ada, virtualization |
| **NextGen** | ~2020-present | Containerization, virtualization, AI/ML elements | Cloud-native concepts, Future Operator Workspace |

### 2.2 Architecture Overview (Mk4 / NextGen)

The 9LV architecture is built on several foundational principles:

**Distributed Processing**
- Fully distributed system with no single point of failure
- Applications are location-independent across the ship's LAN
- Any operator can perform any task from any console position
- Automatic failover and graceful degradation

**Data Distribution Service (DDS)**
- OMG DDS middleware standard for publish-subscribe data sharing
- Enables loose coupling between modules
- Facilitates third-party integration without tight API dependencies
- Supports real-time data distribution with QoS policies

**Naval Open Architecture (NOA)**
- Compliant with US Navy NOA principles
- Layered software architecture separating infrastructure, services, and applications
- Standardized interfaces for sensor/weapon integration
- Designed for incremental upgrades without full system replacement

**Virtualization & Containerization (NextGen)**
- Server virtualization reduces hardware footprint
- Containerized applications for faster deployment
- Enables shore-based development and testing environments
- Supports CI/CD-like update cycles for defense software

### 2.3 Software Architecture

```
+-------------------------------------------------------+
|                 APPLICATION LAYER                       |
|  Tactical Picture | TEWA | Weapon Control | Navigation |
|  Track Management | Comms Mgmt | Mission Planning      |
+-------------------------------------------------------+
|              MIDDLEWARE / SERVICES LAYER                 |
|  DDS Pub/Sub | Secure SOA Suite | Data Fusion Engine   |
|  Track Correlation | Identity Management               |
+-------------------------------------------------------+
|              INFRASTRUCTURE LAYER                       |
|  OS (Windows/Linux) | Network (Ethernet/FC)            |
|  Hardware Abstraction | Security Services              |
+-------------------------------------------------------+
|              HARDWARE LAYER                              |
|  COTS Servers | Multi-Function Consoles | Network HW   |
|  Sensor Interfaces | Weapon Interfaces | Data Links    |
+-------------------------------------------------------+
```

**Programming Languages**: Ada (legacy core), Java (Mk4 applications), C/C++ (interfaces), Python (tooling)

**Operating System**: Migrated from OS-9 RTOS (Mk3) to Windows NT (Mk3E) to modern Windows/Linux variants (Mk4/NextGen)

**Middleware**: OMG Data Distribution Service (DDS) -- the same standard mandated by NATO STANAG 4754 (NGVA) for vehicle architectures

### 2.4 Hardware Components

| Component | Description |
|-----------|-------------|
| **Multi-Function Consoles (MFC)** | Ruggedized operator workstations with large displays, configurable for any role |
| **Future Operator Workspace** | Next-gen console concept (DSEI 2023) with immersive displays, reduced footprint, advanced HMI |
| **COTS Servers** | Standard Intel-based rack-mount servers in ruggedized enclosures |
| **Network Infrastructure** | Redundant Gigabit Ethernet backbone with fiber optic segments |
| **Interface Units** | Sensor and weapon interface modules for connecting to diverse equipment |
| **Data Link Processors** | Dedicated processors for Link-11, Link-16, Link-22, JREAP |
| **Display Processors** | GPU-equipped units for tactical picture rendering |

### 2.5 Sensor Integration

9LV has proven integration with an extensive range of sensors:

| Sensor Category | Integrated Systems |
|----------------|--------------------|
| **Surveillance Radar** | Sea Giraffe 4A (AESA), Sea Giraffe AMB, Sea Giraffe 1X, Thales SMART-S, various legacy radars |
| **Fire Control Radar** | Ceros 200 (Ku-band, Saab-made), third-party FCRs |
| **Electro-Optical** | EOS 500 (Saab), various third-party EO/IR systems |
| **ESM/ELINT** | Multiple ESM suites (Saab, Thales, others) |
| **Sonar** | Hull-mounted and towed-array sonars (various manufacturers) |
| **IFF** | NATO-compatible IFF systems, Mode 5 |
| **Navigation** | GPS, INS, ECDIS integration |
| **AIS** | Commercial AIS receivers |
| **Meteorological** | Weather sensors for fire control ballistics |

### 2.6 Weapon Integration

| Weapon Category | Integrated Systems |
|----------------|--------------------|
| **Anti-Ship Missiles** | RBS-15 Mk2/Mk3/Mk4, NSM, Harpoon, Gabriel |
| **Surface-to-Air Missiles** | ESSM (Evolved Sea Sparrow), Sea Ceptor (CAMM), RBS-70/RBS-90 |
| **Naval Guns** | Bofors 57mm Mk3, Oto Melara 76mm, various 20-40mm cannons |
| **CIWS** | Integration with close-in weapon systems |
| **Torpedoes** | Saab Lightweight Torpedo (SLWT/Tp47), heavyweight torpedoes |
| **Remote Weapon Stations** | Trackfire RWS (Saab), other third-party RWS |
| **Decoys** | Chaff, flare, and torpedo decoy launchers |
| **Mines** | Mine deployment management |

### 2.7 Track Management & Data Fusion

The **Track Data Fusion Engine (TDFE)** is a core 9LV component:

| Feature | Capability |
|---------|------------|
| **Multi-Sensor Tracker (MST)** | Correlates and fuses tracks from all connected sensors |
| **Track Correlation & Fusion Module (TCFM)** | Resolves track ambiguities, maintains system tracks |
| **Automatic Identity Evaluation** | Combines sensor data to assess target identity (friendly/hostile/unknown) |
| **Data Link Track Integration** | Merges external tracks from Link-16/22 participants |
| **Track Capacity** | Hundreds to thousands of simultaneous tracks |
| **Update Rate** | Sensor-dependent; radar tracks at scan rate, EO tracks in real-time |
| **Common Operating Picture** | Unified tactical display combining all sensor and link data |

The TDFE is not 9LV-exclusive -- it is also used in Saab's 9Airborne C2, 9Land BMS, and 9Maritime SOCS products, enabling multi-domain track sharing.

---

## 3. Broader Saab C2 Product Ecosystem

### 3.1 Product Family Overview

| Product | Domain | Function |
|---------|--------|----------|
| **9LV CMS** | Naval | Core combat management for surface ships & submarines |
| **9LV FCS** | Naval | Fire control subsystem (can be standalone or integrated) |
| **9LV Compact** | Naval | Scaled-down CMS for small patrol vessels |
| **AusCMS** | Naval | Australia-specific 9LV derivative (sovereign capability) |
| **9Airborne C2** | Air | Airborne command & control (GlobalEye, Erieye) |
| **9AIR TOCCS** | Air | Ground-based air C2 for air forces |
| **9Land BMS** | Land | Battle Management System for ground forces |
| **9Maritime SOCS** | Maritime | Ship Operations & Control System for coast guard/civilian |
| **TactiCall ICS** | Multi-domain | Integrated Communication System |
| **TactiCall MCI Naval** | Naval | Mobile Communication Infrastructure |
| **Secure SOA Suite** | Multi-domain | Service-Oriented Architecture enabling platform |
| **TDFE** | Multi-domain | Track Data Fusion Engine (shared component) |

### 3.2 Giraffe Radar Family

The Giraffe radars are Saab's primary sensor family and tightly integrated with 9LV:

| Radar | Type | Key Features |
|-------|------|-------------|
| **Sea Giraffe 4A** | Naval AESA, long-range | Multi-function (air surveillance + weapon locating), digital beamforming, 250+ km range |
| **Sea Giraffe 1X** | Naval 3D, short-medium range | Compact, drone detection, C-RAM sense & warn, GBAD quality data |
| **Sea Giraffe AMB** | Naval 3D, medium-range | Battle-proven, fast missile & small UAV detection in clutter |
| **Giraffe 4A** | Land AESA, long-range | Multi-mission (air surveillance + artillery locating), replaces separate ARTHUR in some configs |
| **Giraffe 1X** | Land 3D, short-medium range | Man-portable, C-UAS/C-RAM, recently ordered by US Army ($46M, 2025) |
| **Giraffe AMB** | Land 3D, medium-range | Ground-based air defense command post capability |

### 3.3 TactiCall Communications

TactiCall is Saab's integrated communications management system:
- Interconnects all communication technologies regardless of radio band, frequency, and hardware
- Automated communication management for mission planning and control
- Multi-level security (MLS) capability for coalition operations
- Deployed on French MCM vessels (SLAM-F program via Kership)
- Used by QinetiQ for naval research facilities
- Available in naval, aviation, maritime, energy, and civil variants

### 3.4 ARTHUR Weapon-Locating Radar

| Attribute | Detail |
|-----------|--------|
| **Type** | Counter-battery radar |
| **Function** | Locates hostile artillery, mortars, rockets |
| **Integration** | Data feeds into 9LV/9Land/9AIR C2 systems |
| **Evolution** | Capability being merged into Giraffe 4A multi-function radar |
| **Users** | Sweden, Norway, Czech Republic, Denmark, Greece, South Korea, others |

### 3.5 Gripen Data Link / Multi-Domain Integration

Saab's Gripen fighter uses proprietary and NATO-standard data links that can share tactical data with 9LV-equipped naval platforms via Link-16. The company's multi-domain vision connects:
- 9LV (naval) + 9Airborne C2 (airborne) + 9Land BMS (ground) + 9AIR TOCCS (air defense)
- All using the common TDFE for track fusion
- Secure SOA Suite as the network backbone

### 3.6 Ground-Based Air Defense C2

Saab's MSHORAD (Mobile Short-Range Air Defence) integrates:
- Giraffe 1X radar for detection
- C2 command and control communication platform
- RBS 70 NG Remote Weapon Station
- Recently ordered by Lithuania (2x orders, 2024-2025)
- The C2 element shares architecture concepts with 9LV

### 3.7 Submarine CMS

The A26 Blekinge-class (5th-generation submarine) uses:
- 9LV-based CMS for combat, navigation, and communication
- **Autonomous Ocean Core** -- an AI-based system of systems for autonomous operations
- Multi-Mission Portal for UUV deployment
- Integration with Saab Lightweight Torpedo, heavyweight torpedoes, and long-range strike missiles
- NATO interoperability for Multi-Domain Operations

The Gotland-class submarines (MLU) also use 9LV-based CMS with upgraded capabilities.

---

## 4. AI & Decision Support

### 4.1 Current AI/ML Capabilities

Saab's approach to AI in 9LV has been evolutionary rather than revolutionary:

| Capability | Description | AI Maturity |
|------------|-------------|-------------|
| **Threat Evaluation & Weapon Assignment (TEWA)** | Automated threat ranking and optimal weapon-target pairing | Rules-based + optimization algorithms (not ML) |
| **Air Defence Coordination (ADC)** | Performance-based planning and engagement function (beyond basic TEWA) | Advanced decision support with optimization |
| **Automatic Track Identity Evaluation** | Combines sensor data to assess target identity | Algorithmic fusion, some ML experimentation |
| **Track Correlation** | Resolves track ambiguities from multiple sensors | Statistical algorithms, Bayesian methods |
| **Sensor Management** | Automated sensor scheduling and resource allocation | Optimization-based |
| **Autonomous Ocean Core** | AI system of systems for submarine/UUV autonomy | Emerging AI/ML (A26 program) |
| **Future Operator Workspace** | Advanced HMI with cognitive load reduction | UI/UX innovation, some AI-assisted presentation |

### 4.2 TEWA Details

Saab's TEWA capability is marketed as **Air Defence Coordination (ADC)**, which Saab describes as "much more than a normal TEWA function." It includes:
- Performance-based engagement planning (not just threat ranking)
- Optimized weapon-target assignment considering engagement geometry, weapon inventory, and kill probability
- Multi-layer defense coordination (area defense, point defense, self-defense)
- Engagement scheduling across multiple weapons simultaneously

Research collaboration: Saab Electronic Defence Systems has partnered with academic researchers (documented in a doctoral dissertation on TEWA system performance evaluation), suggesting ongoing R&D in AI/ML-enhanced decision support.

### 4.3 Autonomous Ocean Core

The most advanced AI work in Saab's portfolio is the **Autonomous Ocean Core**, designed for:
- Uncrewed vessel operations (ISTAR, EW, MCM, assault, logistics)
- Vessel-agnostic control system with autonomous navigation
- AI/ML for decision support and mission planning
- Currently deployed on Autonomous Ocean Drone (LUUV)
- Key capability for A26 submarine operations via Multi-Mission Portal

### 4.4 AI Gap Assessment

| Area | Saab Status | State of the Art |
|------|-------------|-----------------|
| ML-based target classification | Experimental | Mature in commercial & some military systems |
| Reinforcement learning for TEWA | Research stage | Academic papers only |
| Natural language C2 interfaces | Not evident | Emerging (LLM-based) |
| Predictive maintenance via ML | Likely in development | Widespread in commercial aviation |
| Computer vision for EO/IR | Basic automatic tracking | Deep learning-based classification common |
| Generative AI for course of action | Not evident | Emerging in US programs |

**Key insight**: 9LV's AI capabilities are primarily algorithmic/optimization-based rather than modern ML/DL. This represents a significant competitive opportunity for AI-native C2 platforms like CORTEX NAVAL.

---

## 5. Naval Warfare Domain Coverage

### 5.1 Anti-Surface Warfare (ASuW)

| Feature | Capability |
|---------|------------|
| **SSM Fire Control** | Full engagement planning for RBS-15, NSM, Harpoon, Gabriel |
| **Surface Defence Coordination** | Counters high-speed surface craft attacks (swarm defense) |
| **Gun Fire Control** | Precision engagement with 57mm/76mm naval guns |
| **RWS Integration** | Trackfire and third-party remote weapon stations for asymmetric threats |
| **Surface Search** | Radar and EO/IR based surface picture compilation |

### 5.2 Anti-Air Warfare (AAW)

| Feature | Capability |
|---------|------------|
| **Air Defence Coordination (ADC)** | Multi-layer air defense management (area, point, self-defense) |
| **SAM Fire Control** | ESSM, Sea Ceptor/CAMM engagement management |
| **Gun-Based Air Defence** | 57mm 3P programmable ammunition for air targets |
| **Threat Evaluation** | Automated threat assessment and prioritization |
| **Engagement Planning** | Optimized weapon-target pairing and scheduling |
| **Missile Defence** | Anti-missile capability via ESSM and Sea Ceptor |

### 5.3 Anti-Submarine Warfare (ASW)

| Feature | Capability |
|---------|------------|
| **Sonar Integration** | Hull-mounted and towed-array sonar data processing |
| **Torpedo Fire Control** | Saab LWT (Tp47) and heavyweight torpedo engagement |
| **ASW Mission Planning** | Patrol planning, datum management, search patterns |
| **Submarine Track Management** | Underwater track maintenance and prediction |
| **Decoy Management** | Torpedo countermeasure deployment |

### 5.4 Mine Warfare

| Feature | Capability |
|---------|------------|
| **Mine Detection** | Integration with mine-hunting sonars |
| **Mine Avoidance** | Navigation with mine threat overlay |
| **Mine Deployment** | Mine-laying mission management |
| **MCM Coordination** | Mine countermeasures vessel coordination |

### 5.5 Naval Gunfire Support

| Feature | Capability |
|---------|------------|
| **Shore Bombardment** | Gun fire control for land targets |
| **Forward Observer Integration** | Data link connection to shore-based spotters |
| **Ballistic Computation** | Atmospheric and terrain-compensated fire solutions |

### 5.6 Integrated Navigation

| Feature | Capability |
|---------|------------|
| **ECDIS Integration** | Electronic chart display and information system |
| **Autopilot Interface** | Course and speed commands from CMS |
| **Navigation Radar** | Dual-use radar for navigation and surface search |
| **GPS/INS Fusion** | Multi-source position determination |

---

## 6. Architecture & Integration Standards

### 6.1 Open Architecture Approach

9LV Mk4/NextGen follows Naval Open Architecture (NOA) principles:

| Principle | Implementation |
|-----------|---------------|
| **Modular design** | Components can be added/removed/replaced independently |
| **Standard interfaces** | DDS-based APIs for sensor and weapon integration |
| **COTS hardware** | Intel-based servers, standard Ethernet networking |
| **Multi-vendor** | Proven integration with 50+ third-party systems |
| **Technology refresh** | Hardware can be upgraded without software rewrite |
| **Reusable software** | Common code base across ship classes ("system family" concept) |

### 6.2 Standards Compliance

| Standard | Coverage |
|----------|----------|
| **Link-11** | Legacy tactical data link |
| **Link-16** | Primary NATO tactical data link (MIDS terminal integration) |
| **Link-22** | Next-generation NATO tactical data link |
| **JREAP-A/B/C** | Joint Range Extension Application Protocol (satellite reach-back) |
| **VMF** | Variable Message Format (land forces interoperability) |
| **OTH-Gold** | Over-the-horizon targeting data |
| **DDS** | OMG Data Distribution Service middleware |
| **STANAG 4586** | UAV interoperability |
| **STANAG 5516** | Link-16 |
| **IFF Mode 5** | NATO identification friend or foe |
| **AIS** | Automatic Identification System |
| **NMEA** | Navigation data standard |

### 6.3 Secure SOA Enabling Product Suite

Saab's Secure SOA Suite provides:
- Network-enabling capability for multi-domain operations
- IT security framework meeting operational and commercial requirements
- Information exchange between 9LV and external C2 systems
- Coalition interoperability support
- Cross-domain guard functionality

### 6.4 Third-Party Integration Capability

9LV's integration track record includes:

| Integration Partner/System | Context |
|---------------------------|---------|
| **Lockheed Martin Canada CMS330** | Halifax-class (9LV as sub-system) |
| **CEA Technologies CEAFAR** | Anzac-class ASMD (phased array radar) |
| **Thales sensors** | Various radar and sonar systems |
| **MBDA Sea Ceptor** | Visby-class air defense upgrade |
| **Raytheon ESSM** | Multiple navies (Australia, Finland, Thailand) |
| **Bofors/BAE 57mm Mk3** | Standard naval gun on multiple classes |
| **Oto Melara 76mm** | Alternative gun integration |
| **Northrop Grumman DLP** | Data Link Processor for Anzac-class |
| **Kongsberg NSM** | Norwegian anti-ship missile |
| **IAI Gabriel** | Israeli anti-ship missile (Finnish Pohjanmaa-class) |

### 6.5 Shore-to-Ship Connectivity

- JREAP for satellite reach-back to shore C2
- Shore-based training and simulation environments
- Remote monitoring and diagnostics capability
- Virtual testing environments for software updates before deployment

---

## 7. Key Contracts & Deployments

### 7.1 Known 9LV Navy Users (20+ Countries)

| Country | Navy | Ship Class(es) | 9LV Variant | Status |
|---------|------|----------------|-------------|--------|
| **Australia** | RAN | Anzac-class frigates (8) | Mk3E / AusCMS | Operational, upgrading |
| **Australia** | RAN | Canberra-class LHD (2) | Mk3E | Operational |
| **Australia** | RAN | Supply-class AOR (2) | Mk4 | Delivered ~2021 |
| **Australia** | RAN | Arafura-class OPV (6 planned) | Mk4 (SAS) | Delivering |
| **Sweden** | Swedish Navy | Visby-class corvettes (5) | Mk3E (CETRIS) | Operational, Sea Ceptor upgrade ordered 2025 |
| **Sweden** | Swedish Navy | Goteborg-class corvettes | Mk3 | Decommissioning |
| **Sweden** | Swedish Navy | Stockholm-class corvettes | Mk3 | Decommissioned |
| **Sweden** | Swedish Navy | A26 Blekinge-class submarine (2) | NextGen | Under construction |
| **Sweden** | Swedish Navy | Gotland-class submarine (3) | Mk3E (MLU) | Upgraded |
| **Finland** | Finnish Navy | Hamina-class FAC (4) | Mk4 (MLU) | Operational |
| **Finland** | Finnish Navy | Rauma-class FAC (4) | Mk3 | Operational |
| **Finland** | Finnish Navy | Pohjanmaa-class corvettes (4) | Mk4 | Delivering (Squadron 2020) |
| **Canada** | RCN | Halifax-class frigates (12) | Mk3E/Mk4 (via LM Canada) | Operational (HCM/FELEX) |
| **Norway** | Coast Guard | Jan Mayen-class OPV (3) | Mk4 (FCS) | Delivering |
| **Germany** | German Navy | Brandenburg-class (F123) frigates (4) | Mk4 | MLU in progress (SEK 4.6B contract, 2021) |
| **Thailand** | RTN | Naresuan-class frigates (2) | Mk4 | Operational (ESSM firing 2015) |
| **Thailand** | RTN | Bhumibol Adulyadej-class frigates | Mk4 | Delivered |
| **Colombia** | ARC | PES-class frigate (1+) | Mk4 | Contracted Feb 2025 (via Damen Naval) |
| **Bahrain** | RBNF | 38m FPB | Compact | Operational (2009 contract) |
| **Peru** | MGP | Patrol boats (multiple) | Compact/FCS | 3rd contract signed Dec 2024 |
| **Brunei** | RBMN | Various patrol craft | 9LV variants | Reported user |
| **Pakistan** | PN | Various vessels | 9LV variants | Reported user |
| **Indonesia** | TNI-AL | Various vessels | 9LV variants | Reported user |
| **UAE** | UAE Navy | Various vessels | 9LV variants | Market presence confirmed |
| **New Zealand** | RNZN | Various vessels | 9LV variants | Reported user |
| **Singapore** | RSN | Various vessels | 9LV variants | Reported user |
| **Denmark** | RDN | Various vessels | Legacy 9LV | Historical user |
| **Malaysia** | RMN | Various vessels | 9LV variants | Reported user |

**Total installed base**: 250+ combat system deliveries (Saab official figure, 2019+)

### 7.2 Recent Major Contracts (2021-2025)

| Year | Customer | Ship/Program | Scope | Value |
|------|----------|-------------|-------|-------|
| **2025 Feb** | Colombia (via Damen) | PES-class frigate | 9LV CMS + FCS + Ceros 200 + EOS 500 + Sea Giraffe 4A | Undisclosed |
| **2025 Jan** | Sweden (FMV) | Visby-class corvettes | Sea Ceptor air defense integration with 9LV | Undisclosed |
| **2024 Dec** | Peru (SIMA) | Patrol boats | 3rd contract, knock-down kit + support | Undisclosed |
| **2024** | Australia (RAN) | AusCMS evolution | Enterprise Partnering Agreement continuation | Multi-year |
| **2022** | Australia (RAN) | Next-gen CMS (EPA) | 9LV-based sovereign CMS development | SEK multi-billion |
| **2021 Jul** | Germany (BAAINBw) | F123 Brandenburg-class MLU | 9LV CMS + Sea Giraffe 4A/1X + Ceros 200 | SEK 4.6B (~$728M) |
| **2019 Sep** | Finland (FDFLC) | Squadron 2020 (Pohjanmaa-class) | Full combat system with 9LV | EUR 412M |
| **2019** | Norway (Vard) | Jan Mayen-class | 9LV FCS + Ceros 200 | Undisclosed |

### 7.3 Combat / Operational Deployment History

While 9LV has been deployed on active warships for decades, publicly documented combat engagements are limited. Key operational milestones include:
- **ESSM live firing** from HTMS Naresuan (Thailand) during CARAT 2015 exercise
- **Anti-Ship Missile Defence (ASMD)** proven on Anzac-class with CEAFAR radar integration (Project of the Year, Australia 2012)
- Continuous operational deployment on Australian, Swedish, Finnish, Canadian, and Norwegian naval vessels
- Used in multinational exercises (RIMPAC, Trident Juncture, etc.)

---

## 8. Business Model & Pricing

### 8.1 Sales Model

Saab employs multiple go-to-market approaches:

| Model | Description | Example |
|-------|-------------|---------|
| **Full Combat System Prime** | Saab as prime contractor for entire combat system | Finland Squadron 2020, Colombia PES |
| **CMS + Sensors Package** | 9LV CMS with Saab radars and fire control | Germany F123 MLU |
| **CMS-Only Integration** | 9LV CMS integrated with third-party sensors/weapons | Various retrofit programs |
| **Fire Control Sub-system** | 9LV FCS standalone (Ceros 200 + EOS 500 + software) | Norway Jan Mayen |
| **Compact CMS for Small Ships** | 9LV Compact for patrol boats | Bahrain 38m FPB, Peru patrol boats |
| **Sub-Supplier** | 9LV components within another prime's system | Canada Halifax (via Lockheed Martin) |
| **Technology Transfer** | Local build with Saab support | Australia (AusCMS), Peru (knock-down kits) |

### 8.2 Estimated Pricing

Based on publicly available contract data:

| Ship Type | Estimated CMS Price (USD) | Scope |
|-----------|--------------------------|-------|
| **Major Frigate (full combat system)** | $100-180M per ship | Full 9LV CMS + Saab sensors + FCS + integration |
| **Corvette (full combat system)** | $50-100M per ship | 9LV CMS + sensors + FCS (Squadron 2020: EUR 412M / 4 ships = ~$103M each) |
| **Frigate MLU (CMS + sensors)** | $50-180M per ship | Germany F123: ~$182M per ship for CMS + radar + FCS |
| **OPV (situational awareness)** | $10-30M per ship | 9LV-based SAS, reduced sensor suite |
| **Patrol boat (compact CMS)** | $5-15M per ship | 9LV Compact + basic FCS |
| **Replenishment ship** | ~$15-25M per ship | SEK 226M / 2 ships for Australian Supply-class |
| **CMS software-only (retrofit)** | $5-20M per ship | Software + integration services |

**Lifecycle costs**: Saab offers in-service support contracts, typically 10-20% of initial system cost per year for sustainment, obsolescence management, and incremental upgrades.

### 8.3 Technology Transfer / Local Build

Saab has demonstrated willingness to transfer technology:
- **Australia**: Full technology transfer since 1988; AusCMS is developed locally as a sovereign capability by Saab Australia (800+ employees)
- **Peru**: Knock-down kits for patrol boats built at SIMA shipyard (3 contracts)
- **Finland**: Local integration and support partnerships
- **General approach**: Saab establishes local entities and trains local engineers; willing to create in-country CMS development capability

---

## 9. Strengths & Weaknesses

### 9.1 Technical Strengths

| # | Strength | Evidence |
|---|----------|----------|
| 1 | **Proven open architecture** | DDS-based NOA, 50+ third-party integrations, DDS is NATO STANAG 4754 standard |
| 2 | **Massive installed base** | 250+ deliveries, 20+ navies, every continent -- most widely exported Western CMS |
| 3 | **Full spectrum coverage** | AAW, ASuW, ASW, MCM, NGFS, navigation -- all in one system |
| 4 | **Scalable from patrol boat to LHD** | 9LV Compact for 38m FPBs to full CMS for 27,000t Canberra-class |
| 5 | **Integrated Saab ecosystem** | Sea Giraffe radars, Ceros 200/EOS 500 FCS, RBS-15, SLWT, Trackfire -- seamless integration |
| 6 | **Multi-domain C2 family** | 9LV (naval) + 9Airborne + 9Land + 9AIR TOCCS with shared TDFE |
| 7 | **Technology transfer model** | Australia sovereign capability, Peru knock-down, willing to localize |
| 8 | **NATO interoperability** | Link-11/16/22, JREAP, VMF, IFF Mode 5, full coalition C2 |
| 9 | **55+ years continuous development** | Unbroken evolution from 1968, no "clean sheet" risks |
| 10 | **Virtualization/containerization** | NextGen architecture supports modern deployment patterns |
| 11 | **Non-US / ITAR-friendly** | Swedish origin reduces ITAR restrictions, attractive to many nations |
| 12 | **Proven combat system integration** | Track record as prime contractor for complex frigate programs |

### 9.2 Weaknesses & Limitations

| # | Weakness | Impact |
|---|----------|--------|
| 1 | **High cost floor** | Even 9LV Compact is $5-15M; inaccessible for small navies with $1-5M budgets |
| 2 | **Heavyweight integration** | Requires significant shipboard infrastructure, engineering, and integration effort |
| 3 | **Legacy code burden** | 55 years of accumulated Ada/Java code creates technical debt |
| 4 | **Limited AI/ML capability** | TEWA is algorithmic/rules-based, not ML-native; behind state of the art |
| 5 | **Proprietary middleware dependency** | While DDS is standard, Saab's implementation layers are proprietary |
| 6 | **Long delivery timelines** | Complex integration programs take 2-5 years from contract to delivery |
| 7 | **Operator training burden** | Full CMS requires extensive operator training (weeks to months) |
| 8 | **Swedish export restrictions** | Swedish defense export policy can limit sales to some countries |
| 9 | **Not designed for autonomous/unmanned vessels** | 9LV assumes manned operations; Autonomous Ocean Core is separate |
| 10 | **Overkill for constabulary missions** | Fisheries protection, SAR, border patrol don't need full CMS |
| 11 | **AusCMS concerns** | Reports of development challenges with Australian sovereign derivative |
| 12 | **Limited market penetration in large-navy tier** | US Navy uses Aegis, UK chose TACTICOS, France uses Naval Group SETIS |

### 9.3 Competitive Position

| Competitor | Vendor | Strengths vs 9LV | Weaknesses vs 9LV |
|------------|--------|-------------------|--------------------|
| **Aegis / COMBATSS-21** | Lockheed Martin (USA) | Unmatched for BMD, massive US funding, SPY-6/7 integration | ITAR-heavy, US political dependencies, extremely expensive |
| **TACTICOS** | Thales (France/NL) | 200+ platforms, 20+ navies, UK Type 31 selection, strong EU position | Similar pricing tier, less sensor ecosystem than Saab |
| **SETIS** | Naval Group (France) | French Navy heritage, submarine CMS, FREMM integration | Narrower export base, French export policy constraints |
| **Atlas ANCS** | Thales Germany/Atlas | German Navy K130, Brazilian Tamandare, established in EU | Smaller installed base, less mature than 9LV |
| **Naval Shield** | Korea (domestic) | Korean Navy heritage, emerging export | Limited international track record |
| **IPMS/CMS** | Hanwha/Hyundai (Korea) | Price competitive, bundled with Korean-built ships | Unproven outside Korea |
| **OYQ-1** | Japan (domestic) | Japanese Navy (JMSDF) use | Not exported |

**Market positioning**: 9LV sits in the "Tier 2" CMS market -- below Aegis (Tier 1, for large-navy combatants) but competing head-to-head with TACTICOS for the global frigate/corvette market. Both 9LV and TACTICOS have ~200+ platform installed bases across ~20 navies.

---

## 10. Design Paradigm Comparison: Saab 9LV vs. CORTEX C2 NAVAL

### 10.1 Architecture Philosophy

| Dimension | Saab 9LV | CORTEX C2 NAVAL |
|-----------|----------|-----------------|
| **Design origin** | 1968 fire control, evolved over 55 years | Clean-sheet AI-native C2 (2025+) |
| **Architecture** | Distributed, DDS middleware, multi-layered | Cloud-native, microservices, API-first |
| **Primary language** | Ada + Java + C/C++ (mixed legacy) | Modern stack (Python/Rust/TypeScript) |
| **AI approach** | Algorithmic TEWA, rules-based decision support | ML-native: classification, prediction, NLP, RL-based TEWA |
| **Middleware** | DDS (OMG standard) | Message broker (MQTT/gRPC/DDS adapter) |
| **Update model** | Multi-year upgrade cycles, integration testing | Continuous deployment, OTA updates |
| **Hardware model** | Ruggedized COTS servers + custom consoles | COTS computing + edge AI accelerators |
| **Console paradigm** | Multi-Function Console (MFC), Future Operator Workspace | Tablet/laptop-based, web UI, optional large displays |

### 10.2 Sensor Integration Approach

| Dimension | Saab 9LV | CORTEX C2 NAVAL |
|-----------|----------|-----------------|
| **Sensor ecosystem** | 50+ proven integrations (Saab + third-party) | Workshop X ecosystem (cameras, RCWS, targets) + open API |
| **Integration method** | DDS-based adapters, months of integration per sensor | Plug-and-play API adapters, days to weeks per sensor |
| **Radar integration** | Deep integration (Sea Giraffe family, others) | Radar data consumer via ASTERIX/standard protocols |
| **EO/IR** | EOS 500, third-party via custom interfaces | Workshop X cameras, ONVIF/GigE Vision standard protocols |
| **Sensor fusion** | TDFE (proven, algorithmically mature) | AI-based multi-sensor fusion engine |

### 10.3 AI Capabilities

| AI Domain | Saab 9LV | CORTEX C2 NAVAL |
|-----------|----------|-----------------|
| **Threat evaluation** | Algorithmic (rules + optimization) | ML-based with explainable AI |
| **Weapon assignment** | Optimization-based (ADC) | RL-optimized with human-in-the-loop |
| **Target classification** | Basic automatic identity evaluation | Deep learning image/signal classification |
| **Anomaly detection** | Not evident | Behavioral analytics, pattern recognition |
| **Natural language** | Not available | LLM-based operator interface and log analysis |
| **Predictive analytics** | Limited | Equipment failure prediction, threat trajectory prediction |
| **Training/simulation** | Separate simulation system | Integrated digital twin with AI opponents |

### 10.4 Price Point Accessibility

| Dimension | Saab 9LV | CORTEX C2 NAVAL |
|-----------|----------|-----------------|
| **Minimum system cost** | ~$5M (Compact for small vessel) | Target: $80-200K |
| **Typical frigate cost** | $50-180M (full combat system) | Not competing at frigate tier |
| **Target market** | Medium-to-large navies, corvette-to-LHD | Small navies, coast guards, patrol vessels, unmanned |
| **Cost ratio** | Baseline (1.0x) | 0.01-0.04x of 9LV Compact |
| **Business model** | Capital expenditure, multi-year contracts | SaaS/subscription + hardware, rapid deployment |

### 10.5 Small Navy Suitability

| Criterion | Saab 9LV | CORTEX C2 NAVAL |
|-----------|----------|-----------------|
| **Budget fit (<$5M/ship)** | No (exceeds floor) | Yes (core target market) |
| **Operator training** | Weeks to months | Days (intuitive AI-assisted UI) |
| **Integration timeline** | Months to years | Weeks |
| **Maintenance complexity** | Requires Saab support or trained local staff | Self-maintaining with remote support |
| **Upgrade path** | Multi-year upgrade cycles | Continuous OTA updates |
| **Minimum crew** | Full warship complement assumed | Designed for reduced/minimal crew |
| **Unmanned vessel support** | Not designed for (Autonomous Ocean Core is separate) | Native unmanned vessel support |

### 10.6 Workshop X Product Integration

| Workshop X Product | 9LV Integration | CORTEX NAVAL Integration |
|-------------------|-----------------|--------------------------|
| **RCWS (Trackfire-like)** | 9LV integrates Trackfire (Saab's own RWS) | Native control, AI-assisted targeting |
| **Sea Targets (VN-TGT-SEA)** | Would need custom interface | Native integration, performance scoring |
| **EO/IR Cameras** | Via EOS 500 or custom adapter | Direct GigE Vision/ONVIF integration |
| **C-UAS Acoustic (VN-CUAS)** | Not available (different market) | Native sensor fusion input |
| **Training Range Systems** | Separate training simulation | Integrated live-virtual-constructive |

### 10.7 Market Segments Where CORTEX NAVAL Can Win

| Segment | Why 9LV Doesn't Serve It | CORTEX NAVAL Fit |
|---------|--------------------------|------------------|
| **Sub-50m patrol boats** | Too expensive, too complex | Core market: $80-200K CMS |
| **Unmanned surface vessels (USV)** | 9LV not designed for USVs | AI-native autonomous C2 |
| **Coast guard / constabulary** | Overkill for fisheries/SAR/EEZ patrol | Right-sized MDA + basic combat |
| **Developing nation navies** | Budget constraint ($1-5M total for electronics) | Affordable entry point |
| **Riverine / brown-water** | No Saab offering for riverine patrol | Lightweight deployable solution |
| **Private maritime security** | 9LV is military-only | Dual-use capable platform |
| **Rapid deployment forces** | 9LV needs shipboard installation | Portable, deploy-in-hours concept |
| **Training and exercise** | Separate simulation system | Integrated training mode |
| **Workshop X ecosystem customers** | Customers already buying Workshop X products (RCWS, targets, cameras) have no CMS | Natural up-sell to existing relationships |

---

## 11. Strategic Summary

### 11.1 Key Takeaways for CORTEX C2 NAVAL

1. **Do not compete head-to-head with 9LV**. Saab has 55 years of development, 250+ installations, and deep integration with 50+ sensor/weapon systems. Competing on features at the frigate/corvette tier is futile.

2. **Exploit the price gap**. The chasm between $5M (9LV Compact floor) and $0 (no CMS at all) is enormous. Most patrol boats, coast guard vessels, and small navy ships operate without any CMS. CORTEX NAVAL at $80-200K fills this gap.

3. **Lead with AI**. 9LV's AI capabilities are fundamentally algorithmic/rules-based, not ML-native. CORTEX NAVAL can offer genuinely superior AI capabilities (ML-based classification, predictive analytics, NLP interfaces) at a fraction of the cost because it starts from a clean-sheet AI-native architecture.

4. **Target the unmanned vessel market**. 9LV was designed for manned warships. Saab's Autonomous Ocean Core is separate and focused on submarines/LUUVs. The surface USV market for C2 is wide open.

5. **Leverage Workshop X ecosystem**. Existing customers of Workshop X products (RCWS, sea targets, cameras) are natural CORTEX NAVAL prospects. No other CMS vendor offers this kind of product-ecosystem integration at this price point.

6. **Adopt Saab's architectural strengths selectively**. DDS middleware, open architecture, and modular design are proven concepts. CORTEX should adopt DDS as an optional integration layer (NATO STANAG 4754 compliance) while using modern message brokers (MQTT, gRPC) as primary transport.

7. **Offer a "bridge to 9LV" story**. Small navies that start with CORTEX NAVAL can graduate to 9LV as their fleet grows. Position CORTEX as a stepping stone, not a competitor -- potentially even as a Saab-compatible data source.

### 11.2 Comparative Positioning Matrix

| Criterion | Saab 9LV | TACTICOS | Aegis | CORTEX NAVAL |
|-----------|----------|----------|-------|-------------|
| **Target ship size** | 50m-230m | 50m-200m | 100m-330m | 10m-80m |
| **Target budget/ship** | $5-180M | $5-150M | $100M-1B+ | $80-200K |
| **AI maturity** | Low-Medium | Low-Medium | Medium | High (native) |
| **Installed base** | 250+ | 200+ | 100+ | New entrant |
| **Time to deploy** | 1-5 years | 1-5 years | 2-7 years | Days-weeks |
| **Unmanned support** | No (separate) | No | No | Yes (native) |
| **ITAR risk** | Low (Swedish) | Low (EU) | High (US) | None (VN/commercial) |
| **Operator count** | 5-30+ per ship | 5-30+ | 20-50+ | 1-5 per ship |
| **Technology age** | 55 years evolved | 30+ years evolved | 40+ years evolved | Clean-sheet 2025+ |
| **Workshop X integration** | None | None | None | Native |

### 11.3 Recommended Intelligence Monitoring

| Topic | Source | Frequency |
|-------|--------|-----------|
| 9LV new contracts | Saab press releases, Janes, Naval News | Monthly |
| AusCMS development status | Australian Defence Magazine, parliamentary reports | Quarterly |
| Autonomous Ocean Core progress | Saab news, FMV publications | Quarterly |
| AI/ML investment signals | Saab annual report, conference presentations | Annually |
| 9LV NextGen architecture evolution | DSEI, Indo Pacific, naval industry events | Semi-annually |
| Competitor CMS wins (TACTICOS, ATLAS) | Thales/Naval Group press, procurement announcements | Monthly |
| Small navy CMS procurements | Janes, Shephard, country defense ministry announcements | Monthly |

---

## References

1. Saab AB. "9LV CMS." https://www.saab.com/products/9lv-cms
2. Saab AB. "9LV Combat System." https://www.saab.com/products/9lv-cs
3. Saab AB. "9LV Fire Control System." https://www.saab.com/products/9lv-fcs
4. Wikipedia. "9LV." https://en.wikipedia.org/wiki/9LV
5. Saab AB. "5 Quick Facts about 9LV." https://www.saab.com/newsroom/stories/2019/september/5-quick-facts-about-9lv
6. Saab AB. "9LV in Numbers." https://www.saab.com/newsroom/stories/2019/november/9lv-in-numbers
7. Saab AB. "Year-End Report 2024." https://www.saab.com/newsroom/press-releases/2025/saab-year-end-report-2024
8. Saab AB. "Annual and Sustainability Report 2024." https://www.saab.com/investors/reports-and-presentations/annual-and-sustainability-report-2024
9. Nordic Defence Review. "All-Time High Order Intake: Saab 2024." https://nordicdefencereview.com/all-time-high-order-intake-saab-sweden-2024-performance-review-and-growth-outlook/
10. Saab AB. "Combat System for Colombian Navy (Feb 2025)." https://www.saab.com/newsroom/press-releases/2025/saab-signs-contract-for-combat-system-for-the-colombian-navys-new-frigate
11. Saab AB. "F123 Modernisation Order (Jul 2021)." https://www.saab.com/newsroom/press-releases/2021/saab-receives-order-to-modernise-german-navys-f123-frigates
12. Saab AB. "Finnish Squadron 2020 Order (Sep 2019)." https://www.saab.com/newsroom/press-releases/2019/saab-receives-finnish-squadron-2020-order
13. Saab AB. "Future Operator Workspace." https://www.saab.com/products/future-operator-workspace
14. Saab AB. "Track Data Fusion Engine." https://www.saab.com/products/track-data-fusion-engine
15. Saab AB. "TactiCall Integrated Communication System." https://www.saab.com/products/tacticall-integrated-communication-system
16. Saab AB. "Secure SOA." https://www.saab.com/products/secure-soa
17. Saab AB. "Autonomous Ocean Core." https://www.saab.com/products/autonomous-ocean-core
18. Saab AB. "A26 5th Generation Submarine." https://www.saab.com/products/5th-generation-submarine
19. Janes. "Saab to base Australia's next-gen combat system on 9LV architecture." https://www.janes.com/osint-insights/defence-news/c4isr/saab-to-base-australias-next-gen-combat-system-on-9lv-architecture
20. Armada International. "Managing Maritime Combat at Speed (May 2024)." https://www.armadainternational.com/2024/05/managing-maritime-combat-at-speed/
21. Defence Connect. "Saab wins German Navy frigate contract." https://www.defenceconnect.com.au/maritime-antisub/8495-saab-wins-german-navy-frigate-contract
22. Australian Defence Magazine. "C4I: Saab connects with NATO." https://www.australiandefence.com.au/41ED6E5E-E948-11DE-98280050568C22C9
23. Global Insight Services. "Combat Management System Market." https://www.globalinsightservices.com/reports/combat-management-system-market/
24. ResearchGate. "Saab opens up 9LV Mk 4 system." https://www.researchgate.net/publication/291428505_Saab_opens_up_9LV_Mk_4_system
25. Diva Portal. "Evaluating Performance of TEWA Systems (Doctoral Thesis)." http://www.diva-portal.org/smash/get/diva2:354687/FULLTEXT02.pdf

---

*Analysis prepared for CORTEX-C2 project competitive intelligence. Data gathered from public sources including Saab AB corporate communications, defense media, parliamentary records, and market research reports. All pricing estimates are based on publicly disclosed contract values and should be treated as approximate.*
