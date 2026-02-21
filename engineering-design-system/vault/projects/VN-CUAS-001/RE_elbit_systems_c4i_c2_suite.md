---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Elbit Systems C4I/C2 Product Suite (Israel)
version: 1.0
created: 2026-02-12
status: complete
---

# RE: Elbit Systems C4I / Command & Control Product Suite - Israel
## Reverse Engineering Analysis from Public Sources

> **KEY DISTINCTION:** Elbit Systems is NOT a single-product company -- it is a **defense system-of-systems integrator** with the most comprehensive C4I product family in the non-US defense market. The Torch-X family serves as the **software backbone** connecting sensors, effectors, communications, autonomous platforms, and AI decision support across land, air, sea, and cyber domains. This analysis is critical for understanding how an Israeli defense prime structures **enterprise-grade C2 architecture** that VN-CUAS-001 acoustic sensors would need to integrate into -- or whose architectural patterns we should study for our own C2 layer.

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Elbit Systems Ltd. |
| **HQ** | Haifa, Israel |
| **NASDAQ Ticker** | ESLT |
| **TASE Ticker** | ESLT (Tel Aviv Stock Exchange) |
| **Founded** | 1966 (as Elbit Computers; defense focus from 1990s via mergers) |
| **CEO** | Bezhalel (Butzi) Machlis |
| **Employees** | 19,712 (FY2024); ~20,000+ (2025 est.) |
| **Revenue (FY2024)** | $6.83 billion (+14.3% YoY from $5.97B in 2023) |
| **Revenue (LTM Q3 2025)** | ~$7.5B annualized run-rate (+19% YoY) |
| **Q2 2025 Revenue** | $2.0 billion (single quarter) |
| **Q3 2025 Revenue** | $1.9 billion (single quarter) |
| **Net Income (FY2024)** | $321M GAAP (+49.3% YoY) |
| **Order Backlog** | $25.2 billion (Q3 2025) -- up from $22.6B (FY2024 end) |
| **Operating Cash Flow** | $461M (9mo 2025) vs $82.5M (9mo 2024) |
| **Stock Price** | ~$300-380 range (2025) |
| **Market Cap** | ~$17-18 billion (2025) |
| **Subsidiaries** | 80+ worldwide |
| **Countries of Operation** | Dozens of countries across 5 continents |
| **ITAR Status** | Israeli company; products generally NOT ITAR-controlled (advantage over US competitors); some US-subsidiary products may be ITAR |
| **Core Competency** | System-of-systems integration across C4ISR, EW, autonomous platforms, EO/IR, communications |

### Revenue by Business Segment (FY2024 / LTM Q3 2025)

| Segment | FY2024 Growth | LTM Revenue Share | Operating Margin | Key Products |
|---------|---------------|-------------------|------------------|--------------|
| **Land** | +29% | ~26% | 9.0% ($150.7M) | Ammunition, munitions, armored vehicle upgrades, Iron Fist APS |
| **Aerospace** | +9% | ~26% | -- | UAS (Hermes 900/450), PGM, aerostructures |
| **Elbit Systems of America (ESA)** | +8% | ~20% | -- | Night vision, medical, US border security |
| **ISTAR & EW** | +12% | ~17% | 7.3% ($96.1M) | EO/IR, electronic warfare, SIGINT, lasers |
| **C4I & Cyber** | +11% (FY24); +21% (Q2 2025) | ~11% | 7.8% ($62.0M) | Torch-X, E-LynX radios, BMS, cyber, autonomous systems |

> **NOTE:** C4I & Cyber at ~11% of revenue ($750M+) may seem modest, but this is the **integration layer** -- it pulls through sales across ALL other segments. The Torch-X platform is the connective tissue.

### Geographic Revenue Distribution (FY2024)

| Region | Approx. Share | Key Drivers |
|--------|---------------|-------------|
| **Israel** | ~35-40% | IDF Digital Army Program (Tzayad), Iron Fist, ammunition surge, border defense |
| **Europe** | ~30-35% | Sweden LSS Mark, artillery C4I, UK programs, multiple NATO armies |
| **North America** | ~15-20% | US Army night vision, border security, JADC2 competition |
| **Asia-Pacific** | ~10-15% | Australia, India, South Korea, unnamed APAC countries |
| **Rest of World** | ~5% | Brazil, Africa, others |

### Key Global Subsidiaries

| Subsidiary | Location | Focus | Employees |
|------------|----------|-------|-----------|
| **Elbit Systems of America (ESA)** | Fort Worth, TX, USA | Night vision, C4I, border security, medical | ~3,675 |
| **Elbit Systems UK** | 16 sites across UK | C4ISR, Torch-X BMA, DIRCM | ~680+ |
| **Elbit Systems Deutschland** | Germany | Communications (E-LynX), NVG, C2, EW | -- |
| **Elbit Systems Sweden** | Sweden | LSS Mark digitization, C2, comms | Est. 2020; growing |
| **Elbit Systems Switzerland** | Switzerland | E-LynX SDR (Swiss Army TASYS program) | -- |
| **Elbit Systems Australia (ELSA)** | Australia | Land 200 BMS, training, sovereign capability | -- |
| **AEL Sistemas (Brazil)** | Brazil | E-LynX airborne, EW, homeland security | -- |
| **Halbit (India)** | India | JV for Indian defense market | -- |
| **GeoSpectrum Technologies** | Canada | Acoustic/ASW sensors | -- |
| **SESA (South Korea)** | South Korea | Localized defense solutions | -- |

### Historical Timeline (C4I Focus)

| Year | Event |
|------|-------|
| 1966 | Founded as Elbit Computers |
| 1996 | Merged with El-Op (electro-optics) |
| 2000 | Acquired Elisra (EW systems) |
| 2000s | Absorbed dozens of companies; became system-of-systems integrator |
| 2004-2006 | TORC2H deployed as IDF's primary C4I system (Digital Army Program) |
| 2008 | Won Australian LAND 200 BGC3 ($331M) with Torch-based BMS |
| 2011 | Australian Torch BMS deployed to 7 Brigade |
| 2015 | IDF launches next-gen C4I network (TORC2H upgrade) |
| 2019 | DOMINATOR warrior suite expanded with SmartEye, SmartSight, SmartNVG, SmartWristView |
| 2021 | Torch-X BMA deployed in NATO CWIX 2021 exercise (28 nations) |
| 2023 | $170M Swedish Army LSS Mark digitization contract |
| 2023 | $200M European artillery C4I + hostile fire counter-attack contract |
| 2024 | European artillery Torch-X Fires + E-LynX upgrade contract |
| 2024 | FY revenue $6.83B; backlog $22.6B |
| Feb 2025 | Dominion-X autonomous management OS unveiled (TRL-9) |
| Feb 2025 | $100M+ IDF contracts for Tzayad (5th-gen Digital Ground Army) + MARS border defense |
| Aug 2025 | **$1.635 BILLION** European country contract -- largest single contract in company history |
| Sep 2025 | Frontier AI-based border surveillance system unveiled at DSEI 2025 |
| Q3 2025 | Revenue $1.9B; backlog reaches $25.2B |

---

## 2. C4I PRODUCT SUITE ARCHITECTURE

### 2.1 Product Family Overview

Elbit's C4I ecosystem is structured in concentric layers:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    STRATEGIC / NATIONAL LEVEL                       │
│                    Torch-X HQ (Division → Joint)                   │
├─────────────────────────────────────────────────────────────────────┤
│                    OPERATIONAL LEVEL                                │
│        TORC2H (Army-wide) / Torch-X Fires (Artillery)             │
│        Torch-X Borders (Border Defense)                            │
├─────────────────────────────────────────────────────────────────────┤
│                    TACTICAL LEVEL                                   │
│    Torch-X Mounted (Vehicles) │ Torch-X Dismounted (Infantry)     │
│    WinBMS (Armored Combat)    │ DOMINATOR Suite (Soldier)          │
│    HattoriX (Fire Support)    │ Torch-X Dismounted-Joint Fires    │
├─────────────────────────────────────────────────────────────────────┤
│                    AUTONOMOUS LAYER                                 │
│    Dominion-X (Drone/UGV Management OS) │ THOR (VTOL mini-UAS)    │
│    PROBOT (UGV) │ Hermes 900/450 (MALE/TUAS)                      │
├─────────────────────────────────────────────────────────────────────┤
│                    COMMUNICATIONS LAYER                             │
│    E-LynX Family (HH/MP/VD/AR/SR SDR Radios)                     │
│    GRX-8000 (Secure Microwave) │ SATCOM │ Tactical Data Links     │
├─────────────────────────────────────────────────────────────────────┤
│                    AI / DECISION SUPPORT LAYER                      │
│    AI Array (GenAI Reasoner) │ Frontier (AI Surveillance)         │
│    ARCAS (AI Rifle Computer) │ CyberShield HQ (Cyber Defense)     │
├─────────────────────────────────────────────────────────────────────┤
│                    FRAMEWORK LAYER                                  │
│              E-CIX (Open Architecture Middleware)                   │
│    ┌─────────────────────────────────────────────────────────┐     │
│    │ • Modular, open architecture development environment    │     │
│    │ • Third-party application accommodation                 │     │
│    │ • Multi-source data exploitation & prioritization       │     │
│    │ • Service-oriented architecture (SOA)                   │     │
│    │ • Cloud-enabled, open standards                         │     │
│    └─────────────────────────────────────────────────────────┘     │
├─────────────────────────────────────────────────────────────────────┤
│                    SELF-PROTECTION LAYER                            │
│    MUSIC / C-MUSIC / J-MUSIC / Mini-MUSIC (DIRCM)                 │
│    Iron Fist (APS) │ EW Systems                                    │
├─────────────────────────────────────────────────────────────────────┤
│                    ISTAR / SENSOR LAYER                             │
│    EO/IR Payloads │ Radar │ SIGINT/COMINT │ Acoustic              │
│    LiDAR │ Multi-spectral │ Ground Sensors                        │
├─────────────────────────────────────────────────────────────────────┤
│                    TRAINING LAYER                                   │
│    EHUD (Air AACMI) │ LVC │ Simulators                            │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 E-CIX: The Core Framework

| Attribute | Detail |
|-----------|--------|
| **Full Name** | E-CIX (Elbit Common Integration eXchange) |
| **Type** | Open architecture middleware / development framework |
| **Design Pattern** | Service-Oriented Architecture (SOA), cloud-enabled |
| **Modularity** | Plug-and-play modular design; third-party apps can be hosted |
| **Standards** | Open standards-based; cloud-enabled |
| **Data Handling** | Multi-source data exploitation; prioritized data extraction from complex info environments |
| **Extensibility** | Accommodates third-party applications for future growth |
| **Deployment** | Underpins ALL Torch-X variants and TORC2H |
| **Key Capability** | Allows ANY Torch-X application to interoperate with ANY other; provides common data model, common services, common UI framework |

> **ARCHITECTURAL INSIGHT:** E-CIX is Elbit's competitive moat. By building ALL products on a common middleware, they achieve:
> 1. **Rapid product derivation** -- new Torch-X variants are essentially new application bundles on E-CIX
> 2. **Cross-domain integration** -- Land, Air, Naval, Border all share data natively
> 3. **Third-party lock-in** -- once a customer adopts E-CIX, switching costs are enormous
> 4. **Ecosystem growth** -- partner/customer applications can run on E-CIX (like an app store for C2)

### 2.3 Product Integration Map

```
                    ┌──────────────┐
                    │  Torch-X HQ  │ Strategic/Operational
                    │  (Division+) │ C5ISR
                    └──────┬───────┘
                           │ E-CIX Data Exchange
            ┌──────────────┼──────────────┐
            │              │              │
    ┌───────▼───────┐ ┌───▼────────┐ ┌───▼──────────┐
    │ Torch-X Fires │ │  TORC2H    │ │ Torch-X      │
    │ (Artillery)   │ │ (Maneuver) │ │ Borders      │
    └───────┬───────┘ └───┬────────┘ └───┬──────────┘
            │             │              │
    ┌───────▼───────┐ ┌───▼────────┐ ┌───▼──────────┐
    │ Fire Units    │ │ Torch-X    │ │ Sensor Nodes │
    │ (155mm, MLRS) │ │ Mounted    │ │ (EO/Radar/   │
    │ + E-LynX SDR  │ │ (Vehicles) │ │  Acoustic)   │
    └───────────────┘ └───┬────────┘ └──────────────┘
                          │
              ┌───────────┼───────────┐
              │           │           │
      ┌───────▼──┐ ┌─────▼────┐ ┌───▼──────────┐
      │ WinBMS   │ │ Torch-X  │ │ Dominion-X   │
      │ (Armor)  │ │ Dismount │ │ (Autonomous) │
      └──────────┘ └─────┬────┘ └───┬──────────┘
                         │          │
                  ┌──────▼──┐  ┌───▼─────┐
                  │DOMINATOR│  │THOR UAS │
                  │(Soldier)│  │PROBOT   │
                  └─────────┘  │UGV      │
                               └─────────┘
```

**ALL connected via E-LynX SDR radio network + E-CIX middleware**

---

## 3. TORCH-X SYSTEM FAMILY (DETAILED)

### 3.1 Torch-X HQ

| Attribute | Detail |
|-----------|--------|
| **Purpose** | C5ISR for tactical, operational, and strategic headquarters |
| **Echelons** | Battle Group / Task Force (tactical) through Division/Joint Command (strategic) |
| **Domains** | Multi-domain: Land, Air, Sea, Space, Cyber |
| **COP** | Real-time Common Operational Picture with automatic, secure, location- and COI-based dissemination |
| **Planning** | Intelligence Preparation of the Battlefield (IPB), Course of Action (COA) analysis, orders distribution |
| **Decision Support** | AI-based tools to reduce cognitive load; optimal decision-making and planning |
| **Communications** | Real-time data, advanced voice services, live video streaming |
| **Tempo** | Generates superior tempo relative to adversary; shortens decision-action cycle |
| **Effects** | Coordinates kinetic and non-kinetic effects in battlespace |
| **Architecture** | E-CIX modular open framework |
| **Interoperability** | NATO/Five-Eyes tested (CWIX 2021); legacy system integration via E-CIX adapters |
| **Deployment** | Shelter-based (Tactical Armored C2 Shelter) or software-deployed at existing HQ infrastructure |

### 3.2 TORC2H

| Attribute | Detail |
|-----------|--------|
| **Full Name** | TORCH All-in-One Command & Control + Communication + Computing + HQ |
| **Purpose** | Complete operative-level C4I system built from ground up |
| **Status** | **Only C4I system fully deployed and operational in a major military (IDF)** |
| **Heritage** | IDF Digital Army Program (DAP) primary C2 system |
| **Coverage** | All army branches and echelons |
| **Key Capability** | Universal situational awareness + in-depth collaborative mission planning + real-time COP |
| **Sensors** | Vehicular mounted + dismounted units; continuous monitoring via sensor images |
| **Functions** | Target identification, location, verification; unit deployment visualization; rapid messaging of commands/reports/SITREPs |
| **Border Use** | Deployed along Israel-Palestinian Authority separation lines for border C2 |
| **Platforms** | Vehicular mounted, dismounted, command post variants |
| **Export** | Deployed in Land, Sea & Air military organizations worldwide, including NATO and Five-Eyes countries |

### 3.3 Torch-X Mounted (Vehicle BMS)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Battle Management System for combat vehicles and armored platforms |
| **UI Paradigm** | **Centralized user interface combining ALL mounted and detachable sensors and effectors** |
| **Sensor Integration** | Unified situational awareness from on-board sensors (EO, thermal, radar, weapon sights) |
| **Connectivity** | Multi-interface control and connectivity with advanced tactical communications (E-LynX) |
| **Control** | Multi-interface control of sensors AND weapons from single display |
| **COP** | Real-time common operational picture shared across formation |
| **Network** | Every platform becomes a networked sensor AND shooter (WinBMS concept) |
| **Weapons** | Weapons can be slaved by remote users to remote sensors (distributed lethality) |
| **Closed-Hatch** | Effective closed-hatches combat capability via sensor fusion |
| **Architecture** | E-CIX open framework; integrates navigation, communications, sensors, weapons |

### 3.4 Torch-X Dismounted

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Advanced networked solution for dismounted close combatants |
| **Composition** | Integrated hardware components + C4I applications + Load Carriage System |
| **Soldier System** | Complete warrior suite improving lethality and survivability |
| **Network Integration** | Integrates soldiers' sensors and effectors to the tactical network |
| **Variants** | Standard dismounted + Dismounted-Joint Fires (for FST/JTAC/TACP) |
| **Joint Fires** | Multi-domain non-kinetic and kinetic indirect fire coordination |
| **Architecture** | Open architecture, integrated digital solution |

### 3.5 Torch-X Fires (Artillery C4I)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Multi-layer digitalized indirect fire solution |
| **Architecture** | Based on E-CIX open framework with advanced artillery ballistics calculation |
| **Weapon Types** | Any weapon type and class, any ammunition type, all doctrines |
| **Effectors** | Integrates kinetic AND non-kinetic effectors; synergistic multi-effector operation |
| **Sensor-to-Shooter** | Effective cross-force coordination; quick and precise planning and execution |
| **Components** | Computing terminals + radio communications (E-LynX) + platform control + sensors + cyber protection |
| **Companion Comms** | E-LynX SDR radios + GRX-8000 secure microwave (high-speed data) |
| **Simulation** | Built-in simulation and training for mission planning, rehearsal, execution |
| **Autonomy** | All levels of autonomy (from fully manual to highly automated fire control) |
| **Contracts** | $200M European artillery + $100M+ additional European orders (2023-2025) |

### 3.6 Torch-X Borders

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Unified networked C2 for border protection and homeland security |
| **Operations** | 24/7, all terrain, all weather border surveillance and interdiction |
| **Sensors Fused** | EO cameras, radars, acoustic sensors, SIGINT, ELINT, autonomous aerial vehicles, autonomous ground vehicles |
| **Decision Support** | Recommends tasks to decision makers based on all available data + ROE |
| **Cognitive Load** | Imagery and data from all sensors fused and enriched to reduce operator cognitive load |
| **Key Functions** | Real-time regional surveillance, early warning, mission management, interception, incident control, rapid response |
| **US Deployment** | Elbit America integrated AI + sensor technology into US border wall via Torch C2 center |

### 3.7 Torch-X Artillery

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Modular, flexible indirect fire control & management system |
| **Scope** | Comprehensive digital artillery solutions for any weapon type/class |
| **Autonomy Levels** | All levels of autonomy |
| **Ballistics** | Advanced artillery ballistics calculation capabilities |
| **Integration** | Computing terminals, radio communications, platform control systems, broad range of sensors, cyber protection |
| **Framework** | E-CIX open architecture |

---

## 4. DOMINATOR SYSTEM (DETAILED)

### 4.1 DOMINATOR Integrated Infantry Combat System (IICS)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Integrated warrior combat suite to enhance dismounted soldier effectiveness |
| **Echelons** | Infantry battalion down to individual soldier |
| **Core Software** | TORC2H-D battle management C2 application (dismounted variant) |
| **COP** | Up-to-the-minute Common Operational Picture (friendly + enemy) on personal displays |
| **Live Video** | Send/receive from external or on-body sensors; transmit back to CP and colleagues |
| **Fratricide Prevention** | Blue Force Tracking (BFT) integrated; safety zones displayed |
| **Sensor-to-Shooter** | Dramatically shortens the sensor-to-shooter loop |
| **Radio Integration** | Seamless integration with Tadiran PNR-1000 UHF personal network radio and other E-LynX radios |

### 4.2 DOMINATOR Component Devices

| Device | Type | Function |
|--------|------|----------|
| **SmartEye** | Head-mounted C2 display | See-through AR symbology for commander SA |
| **SmartNVG** | NVG add-on (monocular) | Augmented reality symbology overlaid on NVG imagery; C2 data visible in night ops |
| **SmartSight** | Weapon sight add-on | See-through AR on weapon sights; target acquisition + C2 interoperability via radio; safety zones + BFT + enemy tracks displayed |
| **SmartWristView** | Wrist-strapped C2 display | Quick-glance SA and messaging for soldiers |
| **Raptor** | Rugged wearable computer | All-in-one computing platform running TORC2H-D |

### 4.3 DOMINATOR-LD (Light Dismounted)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Soldier-centric C2 for infantry squads and Special Forces |
| **Design** | Compact, lighter equipment vs full DOMINATOR IICS |
| **Computer** | Raptor rugged wearable computer |
| **Software** | Subset of TORC2H-D battle management C2 application |
| **Radio** | Tadiran PNR-1000 UHF encrypted personal network radio |
| **Target Users** | Tactical dismounted infantry + Special Forces |

---

## 5. COMMUNICATIONS: E-LynX SDR FAMILY

### 5.1 E-LynX Family Overview

| Attribute | Detail |
|-----------|--------|
| **Type** | Software Defined Radio (SDR) family |
| **Architecture** | Open architecture SDR platform |
| **Design Philosophy** | Multi-band, multi-waveform, multi-channel |
| **Heritage** | Combat-proven in IDF and multiple export customers |
| **Export Customers** | Switzerland (TASYS), Sweden, Spain, Brazil, Israel, and others |
| **Significance** | Preferred SDR choice for several countries' multi-domain digital transformation |

### 5.2 E-LynX Variants

| Variant | Form Factor | Frequency | Key Feature |
|---------|-------------|-----------|-------------|
| **E-LynX HH** | Handheld | VHF/UHF (30-512 MHz) | Infantry platoon to battalion; dismounted segment network connection |
| **E-LynX MP** | Manpack | VHF/UHF (30-512 MHz) | Extended range (higher power, longer antennas); infantry/battalion |
| **E-LynX MP-D** | Dual-channel manpack | VHF/UHF/L-Band (30 MHz - 1.8 GHz) | Simultaneous dual-channel operation |
| **E-LynX VD-55M** | Vehicular | VHF/UHF/L-Band | Backbone of wide mobile communication network |
| **E-LynX VD-15M** | Vehicular dual-channel | VHF/UHF/L-Band | Dual-channel vehicular |
| **E-LynX AR** | Airborne | VHF/UHF/L-Band | Simultaneous wideband + narrowband waveforms; full MANET |
| **E-LynX SR** | Small form factor | VHF/UHF | Compact for integration into platforms/systems |

### 5.3 Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| **Frequency Coverage** | 30 MHz - 512 MHz (HH/MP); 30 MHz - 1.8 GHz (dual-channel/vehicular) |
| **NATO Coverage** | Complete NATO mobile frequency bands |
| **Bands** | VHF, UHF, optional L-Band |
| **Waveforms** | Multiple narrowband + wideband; Elbit proprietary + European + NATO waveforms |
| **Third-Party Waveforms** | Open architecture enables porting of third-party waveforms |
| **Cognitive Waveforms** | Spectrum sensing for adaptive frequency management |
| **MANET** | Combat-proven Mobile Ad-hoc Networking with automatic self-forming, self-healing, routing, relay |
| **MIMO** | Multi-Input Multi-Output for enhanced throughput |
| **Multi-Hop** | Unique multi-hop concurrent flooding for network resilience |
| **IP Connectivity** | Continuous IP connectivity across network |
| **Full Duplex** | Full-duplex capability (recent enhancement) |
| **Multi-Channel** | Multi-channel operation (recent enhancement) |
| **Data Types** | Simultaneous voice, data, and video |
| **Synchronization** | GPS-independent synchronization |
| **Security** | Encrypted communications (military-grade) |
| **Legacy Support** | Supports legacy systems; porting of other waveforms |

### 5.4 E-LynX Deployment Examples

| Customer | Program | Details |
|----------|---------|---------|
| **Switzerland** | TASYS | National tactical communication system |
| **Sweden** | LSS Mark | Army digitization program integration |
| **Spain** | -- | Adopted for digital transformation |
| **Brazil** | F-5M integration | Airborne SDR connectivity flight tests completed on F-5M fighters |
| **European Country** | Artillery C4I | E-LynX paired with Torch-X Fires for 155mm howitzer battalions |
| **Israel** | IDF Digital Army | Backbone tactical communications |

---

## 6. AUTONOMOUS SYSTEMS LAYER

### 6.1 Dominion-X

| Attribute | Detail |
|-----------|--------|
| **Type** | Autonomous Management Operating System for unmanned platforms |
| **Announced** | February 18, 2025 |
| **TRL** | TRL-9 (operational maturity) |
| **Platforms Managed** | UAS (drones) + UGV; multi-domain |
| **Key Innovation** | Distributed Decision Management System (DMS) -- each platform has autonomous decision-making |
| **Human-Swarm Teaming** | Seamless interaction, influence, behavioral inference between human operators and robot swarms |
| **Sensing** | Large-scale distributed sensing with advanced information fusion and distillation |
| **Navigation** | Real-time terrain mapping + obstacle avoidance using EO and LiDAR algorithms |
| **Cognitive Load** | Significantly reduces human operator workload via automation |
| **Integration** | Managed via TORCH-X RAS C2 application |

### 6.2 THOR VTOL Mini-UAS

| Attribute | Detail |
|-----------|--------|
| **Type** | VTOL tactical mini-UAS |
| **Deployment** | Foldable, stored in backpack; deploys in <2 minutes |
| **Payload** | Up to 10 kg |
| **Missions** | Reconnaissance, ISR, tactical mule |
| **Integration** | Operates in swarms managed by Dominion-X; coordinated with PROBOT UGVs via TORCH-X RAS |
| **Autonomy Kit** | Equipped with Autonomy Kits + EO payloads |

### 6.3 AI Array Platform

| Attribute | Detail |
|-----------|--------|
| **Type** | Real-time data fusion, decision support, and mission planning platform |
| **Companion** | Works alongside Dominion-X to define "Agentic Operation Age" |
| **GenAI Reasoner** | Cognitive, situationally aware Generative AI that tracks events, interprets context, correlates historical data, provides actionable decision support |
| **Automation Level** | AI performs thousands of routine actions -- identifying anomalies to recommending responses |
| **Philosophy** | "5th generation of C2" -- rethinking the traditional decision loop |

---

## 7. SELF-PROTECTION: MUSIC DIRCM FAMILY

### 7.1 MUSIC Family Overview

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Directed Infrared Countermeasure (DIRCM) against heat-seeking MANPADS |
| **Technology** | Advanced laser + high frame-rate thermal camera + dynamic mirror turret |
| **Threat Coverage** | 1st, 2nd, and 3rd generation IR MANPADS |
| **Jam Codes** | Generic NATO jam codes |
| **Mechanism** | Optically breaks missile's IR tracking lock on target aircraft |

### 7.2 MUSIC Variants

| Variant | Platform | Key Spec |
|---------|----------|----------|
| **MUSIC** | Military transport/utility aircraft | Full-size DIRCM |
| **C-MUSIC** | Commercial/large transport aircraft | World's first DIRCM on commercial aircraft in regular service |
| **J-MUSIC** | Jet aircraft | Optimized for fast jets; market-leading DIRCM |
| **Mini-MUSIC** | Helicopters | 19 kg, 271x316x449 mm, <1000W; compact/lightweight |

> **NOTE:** MUSIC is NOT a C-UAS system. It is an aircraft self-protection system against ground-launched IR missiles. The name similarity to C-UAS should not cause confusion. However, the sensor fusion and tracking algorithms have potential crossover relevance.

---

## 8. TRAINING SYSTEMS

### 8.1 EHUD Air Combat Training System

| Attribute | Detail |
|-----------|--------|
| **Full Name** | EHUD Rangeless Air Combat Maneuvering Instrumentation (AACMI) |
| **Purpose** | Advanced air-to-air and air-to-ground combat training |
| **Key Innovation** | "Rangeless" -- no fixed infrastructure needed; fully autonomous |
| **Data Link** | Patented data link protocol supporting unlimited live participants |
| **Training Modes** | Live-Virtual-Constructive (LVC) and Virtual-Constructive (VC) |
| **Operational Since** | 1994 |
| **Deployments** | 17+ air forces, 4 continents |
| **Flight Hours** | 1,000,000+ logged |
| **Equipment** | 500+ airborne pods, 100+ ground debriefing/real-time monitoring stations |
| **Capabilities** | Advanced instrumentation + debriefing for optimal flight hour utilization |

### 8.2 Land Training & Simulation

| Attribute | Detail |
|-----------|--------|
| **Scope** | Full spectrum of simulators for land forces |
| **Environment** | Comprehensive, realistic training environments |
| **Integration** | LVC training capabilities integrated with BMS systems |
| **Types** | Vehicle crew trainers, gunnery simulators, tactical engagement simulation |

### 8.3 Training System Notes

> The search did not surface a specific product called "GEMS" in Elbit's public portfolio. This may be an internal/codename product, a sub-component of the land training suite, or possibly confused with another company's product. Further investigation recommended via direct Elbit engagement or defense trade publications.

---

## 9. AI / ML CAPABILITIES

### 9.1 AI Strategy Overview

Elbit positions itself at the forefront of military AI with what it calls the **"Agentic Operation Age"** -- defined by two pillars:

| Pillar | System | Function |
|--------|--------|----------|
| **Autonomous Platform Management** | Dominion-X | Orchestrates fleets of drones, UAVs, UGVs with distributed autonomous decision-making |
| **AI Decision Support** | AI Array | Real-time data fusion, GenAI Reasoner, mission planning, decision support |

### 9.2 AI Capabilities Across Products

| Product | AI/ML Feature |
|---------|---------------|
| **Torch-X Family** | AI-based decision support tools at all echelons; reduces cognitive load; optimal decision-making and planning |
| **AI Array** | Generative AI Reasoner -- tracks events, interprets context, correlates historical data, provides actionable decision support |
| **Frontier** | Adaptive learning for anomaly detection; autonomous threat classification; continuous sector learning of topography and operational routines |
| **Torch-X Borders** | Sensor fusion enrichment; task recommendations based on data + ROE; cognitive load reduction |
| **ARCAS** | AI-powered computerized rifle scope (assault rifle); target acquisition, friend-or-foe, ballistic calculation |
| **HattoriX** | Automatic fusion of GIS + pre-loaded targets + visual feed + C2 data; passive CAT-1 target acquisition |
| **Dominion-X DMS** | Distributed Decision Management -- each autonomous platform makes independent decisions |
| **CyberShield HQ** | AI-based endpoint detection and response (EDR) for isolated military networks |
| **SmartSight** | AI-enhanced target acquisition via weapon sight with C2 interoperability |

### 9.3 IDF "Tzayad" 5th-Gen Digital Ground Army (2025)

| Attribute | Detail |
|-----------|--------|
| **Contract** | $100M+ from Israel MoD (Feb 2025) |
| **Program** | 5th generation of IDF Digital Ground Army ("Tzayad") |
| **AI Features** | AI-enabled support for operational and tactical decision-making |
| **Sensor-to-Shooter** | Accelerated multi-service sensor-to-shooter operational loops |
| **Network** | Increased tactical network capacity down to frontline combat units |
| **Open Ecosystem** | Open digital ecosystem for rapid integration of diverse platforms and sensors |
| **Companion** | MARS (Multi-Sensor Border Defense System) for managing large sensor/effector arrays |

### 9.4 JADC2 Competition (US)

Elbit Systems of America was selected by the U.S. Air Force to compete for Joint All Domain Command and Control (JADC2) task orders, positioning the company in the US military's next-generation multi-domain C2 architecture.

---

## 10. TECHNOLOGY ARCHITECTURE & STANDARDS

### 10.1 Software Architecture Patterns

| Pattern | Implementation |
|---------|---------------|
| **Service-Oriented Architecture (SOA)** | E-CIX framework; modular services for each C2 function |
| **Open Architecture** | E-CIX designed for third-party application hosting; customer/partner apps |
| **Cloud-Enabled** | Cloud-capable architecture for scalable deployment |
| **Open Standards** | Standards-based interfaces for interoperability |
| **Modular Design** | All Torch-X variants are modular applications on E-CIX base |
| **Evergreen Upgradable** | Architecture designed for continuous upgrades without full system replacement |
| **Multi-Domain** | Single framework spanning Land, Air, Sea, Space, Cyber |

### 10.2 Standards Compliance

| Standard | Application |
|----------|-------------|
| **NATO STANAG 4586** | UAS interoperability (confirmed for Hermes 900) |
| **NATO CWIX** | Interoperability validation (Torch-X BMA tested at CWIX 2021, 28 nations, 10,000+ tests) |
| **NATO FMN** | Federated Mission Networking alignment (E-CIX enables connectivity to NATO datalinks) |
| **MIL-STD** | Multiple MIL-STDs for environmental, EMC, safety (product-specific; not detailed in public sources for C4I software) |
| **Legacy Interop** | E-CIX adapters for legacy C2 systems, existing tactical datalinks (demonstrated in Canadian Air Coordination project) |
| **Five-Eyes** | TORC2H deployed in Five-Eyes coalition environments |
| **Generic NATO Jam Codes** | MUSIC DIRCM uses NATO-standard countermeasure protocols |

### 10.3 Cybersecurity

| Solution | Function |
|----------|----------|
| **CyberShield HQ** | Endpoint Detection & Response (EDR) for sensitive, isolated military networks; operates in "assume breach" mindset |
| **Intelligence 360** | Multi-source data collection, fusion, analysis, investigation management platform |
| **Cyber Defense Suite** | Multi-layered, scalable cyber protection including cyber intelligence analysis, SIGINT, cyber defense |
| **Network Security** | Full range of military-wide secured network communication for all branches/echelons |
| **Embedded Cyber** | Torch-X Artillery specifically mentions integrated cyber protection |

### 10.4 Integration Approach

Elbit's integration philosophy can be characterized as:

1. **Common Middleware (E-CIX):** All products share a common software framework, enabling native data exchange
2. **SDR Communications Backbone (E-LynX):** Unified radio family provides the physical network layer
3. **Sensor Agnostic:** Torch-X Borders demonstrates fusion of EO, radar, acoustic, SIGINT, ELINT -- any sensor type
4. **Effector Agnostic:** Torch-X Fires integrates any weapon type, any ammunition, kinetic + non-kinetic
5. **Platform Agnostic:** Same E-CIX framework deploys on shelter, vehicle, dismounted, airborne platforms
6. **Autonomous Integration:** Dominion-X manages heterogeneous drone/UGV fleets within the C2 ecosystem
7. **Legacy Bridging:** E-CIX provides adapters for existing systems (proven in Canada, Australia, NATO exercises)
8. **Distributed Architecture:** Every platform is simultaneously a sensor AND a shooter on the network (WinBMS concept)

---

## 11. BUSINESS MODEL & MARKET POSITION

### 11.1 Pricing (Inferred from Contracts)

| Contract | Value | Scope | Implied Unit Economics |
|----------|-------|-------|----------------------|
| Australia LAND 200 BGC3 | $331M | Army-wide BMS (7 Brigade initial) | System-of-systems; $100M+ per brigade-equivalent |
| Sweden LSS Mark | $170M | 10-year integration partnership; tens of thousands of platforms | ~$5-10K per platform (very rough) + services |
| European Artillery C4I | $200M | Multiple 155mm battalions + hostile fire counter-attack | ~$50-100M per battalion-set |
| European Artillery Upgrade | ~$100M | Additional 155mm howitzer battalions with Torch-X Fires + E-LynX | -- |
| IDF Tzayad + MARS | $100M+ | 5th-gen Digital Ground Army + border sensor management | R&D + initial fielding |
| European Mega-Contract | $1.635B | Full military digitalization + ISTAR + UAS + munitions + upgrades (5 years) | C4I is major component alongside weapons systems |
| Israel MoD Communications | $130M | Advanced communication systems | E-LynX radios at scale |
| APAC Helicopter EW/DIRCM | $275M | EW + DIRCM for helicopter platform | Not C4I but shows deal sizes |
| Israel Tank Upgrades | $210M | Tank upgrade packages | Includes BMS integration |

> **PRICING MODEL:** Elbit does NOT publish unit prices. Based on contract values, the C4I business operates on:
> - **System-of-systems deals:** $100M-$1.6B+ for army-wide digitization
> - **Battalion-level packages:** $50-200M for C4I + communications
> - **Long-term integration partnerships:** 5-10 year contracts with upgrade/maintenance revenue
> - **Services annuity:** Ongoing support, training, software updates (estimated 15-25% of initial contract value per year)

### 11.2 Market Position

| Metric | Detail |
|--------|--------|
| **Global C2 Market Size** | $40-50B+ (growing 5-7% CAGR) |
| **Key Competitors** | Lockheed Martin, Northrop Grumman, BAE Systems, Thales, L3Harris, Rafael, IAI, Rheinmetall, Kongsberg, Saab |
| **Top 3 by Market Share** | Northrop Grumman, Lockheed Martin, BAE Systems (~23.1% combined) |
| **Elbit Position** | Top 10 globally; #1 Israeli C4I company; dominant in dismounted/tactical BMS segment |
| **Competitive Advantage** | Non-ITAR (vs US competitors); full stack from radio to HQ C2; IDF combat-proven heritage; E-CIX ecosystem lock-in |
| **Differentiation** | Only company with TORC2H fully deployed in a major military; E-LynX SDR + Torch-X C4I as integrated package |

### 11.3 Export Customers (Confirmed/Implied)

| Customer | Products | Contract Value | Year |
|----------|----------|---------------|------|
| **Israel (IDF)** | TORC2H, Torch-X, E-LynX, DOMINATOR, WinBMS, Dominion-X | Billions (cumulative) | Ongoing |
| **Australia** | Torch-based BGC3 (LAND 200) | $331M initial; $2B+ total program | 2008-present |
| **Sweden** | LSS Mark (Torch-X + E-LynX) | $170M | 2023 |
| **Switzerland** | E-LynX TASYS program | Multi-hundred $M | -- |
| **Canada** | Torch-X BMA (Airspace Coordination Centre Modernisation) | -- | 2021+ |
| **United Kingdom** | Torch-X BMA, DIRCM | Multi-program | Ongoing |
| **Brazil** | E-LynX (airborne, F-5M) | -- | -- |
| **Spain** | E-LynX SDR | -- | -- |
| **European Country (unnamed)** | Artillery C4I + hostile fire counter-attack | $200M | 2023-2026 |
| **European Country (unnamed)** | Full military digitalization mega-deal | $1.635B | 2025 |
| **European Countries (8)** | HattoriX demonstrations | -- | 2021 |
| **APAC Country (unnamed)** | Helicopter EW + DIRCM | $275M | 2025 |
| **India** | Halbit JV; various programs | -- | -- |
| **USA** | Night vision, border security, JADC2 competition | Multi-hundred $M | Ongoing |
| **Netherlands** | RAS concept development (drone swarm demonstrations) | -- | -- |

---

## 12. FIRE SUPPORT & TARGET ACQUISITION

### 12.1 HattoriX

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Next-gen fire support and intelligence for dismounted forces |
| **Innovation** | **Fully passive** target acquisition -- NO laser emitter (undetectable) |
| **Technology** | Automatic fusion of GIS database + pre-loaded targets + visual feed + C2 information |
| **Accuracy** | CAT-1 targets (Target Location Error of a few meters) |
| **Operation** | 3 touches on screen: (1) acquire target, (2) generate precise coordinates, (3) send to fire support |
| **Users** | Forward Observers, FAC, JTAC, reconnaissance, field intelligence, Special Forces |
| **Variants** | Lightweight (10 kg tripod, <5 km targets) + Heavy (30 kg, ~10 km targets) |
| **Status** | AI-enabled; demonstrated in 8 European countries |

### 12.2 WinBMS (Weapon-Integrated BMS)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Networked integrated battle management for armored combat platforms |
| **Key Concept** | Every platform = networked sensor + shooter; weapons slaved to remote sensors |
| **Capabilities** | Accelerated mission planning; common language across combat elements; auto-distribute intelligence, targets, alerts |
| **Integration** | Built-in navigation + communications + sensors + weapons; fully integrated with platform |
| **Doctrine** | Distributed dispersed firepower without fratricide risk |
| **Combat Mode** | Effective closed-hatches combat via sensor fusion |
| **Deployment** | Integral part of IDF Digital Army Programme |

---

## 13. RECENT CONTRACTS & DEPLOYMENTS (2023-2025)

| Date | Contract | Value | Customer | Details |
|------|----------|-------|----------|---------|
| Oct 2023 | Swedish Army LSS Mark | $170M | Sweden | 10-year C2 digitization integration partnership |
| 2023 | Artillery C4I + hostile fire counter-attack | $200M | European country | Torch-X Fires + E-LynX for 155mm battalions; options for extensions through 2026 |
| Mar 2024 | European Artillery Upgrade | ~$100M+ | European country | Torch-X Fires + E-LynX for additional 155mm howitzer battalions |
| 2024 | Israel MoD Communications | $130M | Israel | Advanced communication systems (E-LynX) |
| 2024 | Tank Upgrades | $210M | Israel MoD | Tank upgrade packages (includes BMS) |
| Feb 2025 | Tzayad + MARS | $100M+ | Israel MoD | 5th-gen Digital Ground Army + Multi-Sensor Border Defense |
| 2025 | APAC Helicopter EW/DIRCM | $275M | APAC country | EW + DIRCM self-protection |
| Aug 2025 | Full Military Digitalization | **$1.635B** | European country | Largest-ever contract: C4ISR + UAS + munitions + ISTAR + EW + vehicle upgrades (5 years) |
| Q3 2025 | Various | Multiple | Various | Backlog reaches $25.2B |

---

## 14. ARCHITECTURAL ANALYSIS: DESIGN PATTERNS FOR VN-CUAS RELEVANCE

### 14.1 Key Architectural Lessons from Elbit C4I

| Pattern | Elbit Implementation | VN-CUAS Relevance |
|---------|---------------------|-------------------|
| **Common Middleware** | E-CIX enables all products to share data natively | VN-CUAS should design sensor node with standardized middleware interface from day 1 |
| **SDR as Backbone** | E-LynX provides unified comms layer | Consider SDR integration path (even if initial deployment uses commercial radios) |
| **Sensor-Agnostic Fusion** | Torch-X Borders fuses EO + radar + acoustic + SIGINT | VN-CUAS acoustic data should be formatted for C2 fusion (not proprietary format) |
| **Edge AI + Cloud AI** | Frontier: smart edge computing + centralized AI | VN-CUAS dual architecture (edge classification + network-level fusion) aligns |
| **Open Architecture** | E-CIX allows third-party apps | Design for SAPIENT/TAK integration = our equivalent of open architecture |
| **Distributed Sensing** | Every platform = sensor node on network | VN-CUAS mesh network of acoustic nodes follows same pattern |
| **Autonomous Management** | Dominion-X manages heterogeneous swarms | Long-term: VN-CUAS sensors could be managed by autonomous C2 layer |
| **Cognitive Load Reduction** | AI tools across all echelons | VN-CUAS must minimize operator burden (classification confidence, auto-alert) |
| **Evergreen Upgrade** | E-CIX designed for continuous upgrade | Firmware-defined multi-mission approach (our concept) parallels this |

### 14.2 Integration Standards for VN-CUAS

Based on Elbit's integration approach, VN-CUAS acoustic sensors should support:

| Interface | Standard | Purpose |
|-----------|----------|---------|
| **C2 Data Exchange** | SAPIENT (NATO STANAG draft) | Autonomous sensor integration into C2 |
| **Tactical Display** | TAK/ATAK | Android-based tactical display (open source) |
| **Situational Awareness** | NATO APP-6 symbology | Standard military map symbols |
| **Radio Interface** | IP-based (UDP/TCP) | Compatible with SDR MANET networks |
| **Sensor Reporting** | NIEM / JSON-based | Structured detection reports |
| **Track Data** | STANAG 5516 / Link 16 (aspirational) | Interoperable track exchange |

### 14.3 Competitive Implications

| Factor | Elbit Approach | VN-CUAS Opportunity |
|--------|---------------|---------------------|
| **System Lock-in** | E-CIX creates ecosystem dependency | VN-CUAS should be C2-agnostic (works with ANY C2, not just one vendor) |
| **Price Point** | $100M+ for battalion-level C4I | VN-CUAS at $2-5K/node is complementary, not competitive (sensor layer, not C2 layer) |
| **Non-ITAR** | Elbit leverages non-ITAR for exports | VN-CUAS similarly benefits from non-ITAR/non-restricted status |
| **IDF Heritage** | Combat-proven credibility | Must build credibility via pilot deployments and rigorous testing |
| **Full Stack** | Radio → sensor → C2 → weapons | VN-CUAS is niche (acoustic sensing); must integrate into others' full stacks |

---

## 15. CRITICAL INTELLIGENCE GAPS

| Gap | Significance | Recommended Action |
|-----|-------------|-------------------|
| **E-CIX API specification** | Understanding the integration protocol would enable direct sensor-to-C2 design | Monitor NATO CWIX exercise documentation; request through defense cooperation channels |
| **Torch-X licensing model** | Per-seat, per-platform, or enterprise? Affects TCO comparison | Analyze SEC 20-F filing in detail |
| **E-LynX waveform specifications** | Data rates, latency, error correction for sensor data | Review Elbit SDR brochures (PDF available at elbitsystems.com) |
| **AI Array architecture** | GenAI Reasoner details -- training data, inference model, edge/cloud split | Monitor academic publications from Elbit R&D |
| **GEMS product** | Mentioned in user query but not found in public Elbit portfolio | May be internal codename or confused with another company |
| **NATO suspension** | Dec 2025 report of Elbit suspension from NATO procurement (corruption allegations) | Monitor developments; may affect competitive landscape |
| **Acoustic sensor integration** | How Torch-X Borders specifically handles acoustic sensor data | Critical for VN-CUAS integration design |
| **Unit pricing** | No public pricing for C4I software licenses or E-LynX radios | Engage defense trade shows; use FMS pricing databases |

---

## 16. SUMMARY ASSESSMENT

### Company Strengths
1. **Full-stack integration:** Only Israeli company offering radio-to-HQ C2 in a single ecosystem
2. **IDF combat-proven:** TORC2H is the ONLY C4I system fully deployed in a major military
3. **Massive backlog:** $25.2B provides 3+ years of revenue visibility
4. **Non-ITAR advantage:** Can export to countries restricted from US systems
5. **AI investment:** Dominion-X (TRL-9), AI Array (GenAI Reasoner), Frontier -- leading military AI
6. **E-CIX ecosystem:** Open architecture creates customer lock-in while appearing open
7. **Scale:** $6.8B revenue, 20K employees, 80+ subsidiaries, decades of defense experience

### Company Vulnerabilities
1. **NATO suspension risk:** Dec 2025 corruption allegations could disrupt European business
2. **Australian LAND 200 withdrawal:** BMS withdrawn from service; reasons unclear -- credibility issue
3. **Geopolitical sensitivity:** Israeli origin creates procurement barriers in some markets
4. **Complexity:** 80+ subsidiaries and sprawling product line = integration challenges
5. **Margin pressure:** C4I & Cyber at 7.8% operating margin is thin for software-heavy business
6. **Dependency on IDF:** ~35-40% revenue from single customer (Israel MoD)

### Relevance to VN-CUAS-001
- Elbit's Torch-X Borders explicitly fuses acoustic sensor data into C2 -- **direct precedent for our integration approach**
- E-CIX open architecture philosophy validates our SAPIENT/TAK integration strategy
- Edge AI + centralized fusion architecture (Frontier) parallels our dual-classification concept
- VN-CUAS operates at the **sensor layer** (not C2 layer) -- we complement, not compete with, systems like Torch-X
- Understanding Elbit's integration protocols helps us design sensor outputs that C2 platforms expect

---

## SOURCES

### Primary Corporate Sources
- [Elbit Systems Official Website](https://www.elbitsystems.com/)
- [Torch-X Family Product Page](https://www.elbitsystems.com/networked-warfare/network-warfare-systems/torch-x-family)
- [Torch-X Mounted Product Page](https://www.elbitsystems.com/networked-warfare/joint-land/battle-management-systems/torch-x-mounted)
- [Torch-X HQ Product Page](https://www.elbitsystems.com/networked-warfare/joint-land/hq-solutions/torch-x-hq)
- [Torch-X Fires Product Page](https://www.elbitsystems.com/networked-warfare/joint-land/artillery-command-control/torch-x-fires)
- [Torch-X Dismounted Product Page](https://www.elbitsystems.com/networked-warfare/joint-land/soldier-systems/torch-x-dismounted)
- [Torch-X Borders Product Page](https://www.elbitsystems.com/homeland-security/integrated-solutions/border-defence-systems/torch-x-borders)
- [E-LynX Mobile SDR Family](https://www.elbitsystems.com/networked-warfare/secured-communication/e-lynx-mobile-sdr-family)
- [E-LynX Family Brochure (PDF)](https://www.elbitsystems.com/sites/default/files/2025-02/e-lynx-family_brochure_0.pdf)
- [E-LynX HH Brochure (PDF)](https://www.elbitsystems.com/sites/default/files/2025-03/e_lynx_hh_2024_25.pdf)
- [Battle Management Systems](http://elbitsystems.com/c4i-systems-battle-management-systems-bms/)
- [C4I & Cyber Segment](https://elbitsystems.com/product/c4i-cyber/)
- [Segments Overview](https://www.elbitsystems.com/segments)
- [EHUD Training System](https://www.elbitsystems.com/air-space/training-simulation/embedded-virtual-training/ehud)
- [MUSIC DIRCM](https://www.elbitsystems.com/air-space/airborne-self-protection/dircm-systems/music)
- [C-MUSIC DIRCM](https://www.elbitsystems.com/air-space/airborne-self-protection/dircm-systems/c-music)
- [Mini-MUSIC DIRCM](https://www.elbitsystems.com/air-space/airborne-self-protection/dircm-systems/mini-music)
- [HattoriX Product Page](https://www.elbitsystems.com/land/land-c4isr/imaging-night-vision/hattorix)
- [Dominion-X Product Page](https://www.elbitsystems.com/networked-warfare/robotic-and-autonomous-solutions/autonomous-missions-management-system/dominion-x)
- [Cyber Security](https://www.elbitsystems.com/commercial/cyber-security)
- [Global Presence](https://www.elbitsystems.com/global-presence)
- [THOR Brochure (PDF)](https://www.elbitsystems.com/sites/default/files/2025-03/thor_2025_7.pdf)

### Financial & Corporate
- [Elbit FY2024 Results](https://www.elbitsystems.com/news/elbit-systems-reports-fourth-quarter-and-full-year-2024-results)
- [Elbit Q2 2025 Results](https://www.elbitsystems.com/news/elbit-systems-reports-second-quarter-2025-results)
- [Elbit Q3 2025 Results](https://www.elbitsystems.com/news/elbit-systems-reports-third-quarter-2025-results)
- [Elbit Revenue History (MacroTrends)](https://www.macrotrends.net/stocks/charts/ESLT/elbit-systems/revenue)
- [Elbit Employee Count (MacroTrends)](https://www.macrotrends.net/stocks/charts/ESLT/elbit-systems/number-of-employees)
- [Elbit ESLT Stock Analysis](https://stockanalysis.com/stocks/eslt/)
- [SEC Form 20-F (FY2024)](https://www.sec.gov/Archives/edgar/data/1027664/000162828025013971/eslt-20241231.htm)

### Contract Announcements
- [Elbit $1.635B European Contract](https://www.elbitsystems.com/news/elbit-systems-awarded-1635-billion-contract-deliver-range-defense-solutions-european-country)
- [Elbit $200M European Artillery C4I](https://www.elbitsystems.com/news/elbit-systems-awarded-two-contracts-aggregate-amount-200-million-supply-artillery-c4i-solution)
- [Elbit $170M Swedish Army LSS Mark](https://www.prnewswire.com/news-releases/elbit-systems-awarded-approximately-170-million-contract-to-become-the-integration-partner-for-swedish-army-lss-mark-digitization-program-301966857.html)
- [Elbit European Artillery Upgrade (2024)](https://www.elbitsystems.com/news/elbit-systems-advanced-c4i-solution-selected-european-artilery-upgrade)
- [Elbit $100M+ IDF Digital Army Contracts](https://www.calcalistech.com/ctechnews/article/s1ds11fdp11x)
- [Elbit $275M APAC Helicopter EW/DIRCM](https://www.elbitsystems.com/news/elbit-systems-secures-275-million-contracts-equip-asia-pacific-country-helicopter-platform)
- [Elbit $210M Israel Tank Upgrades](https://www.elbitsystems.com/news/elbit-systems-awarded-contracts-aggregate-amount-210-million-israel-ministry-defense-tank)
- [Elbit $130M Israel Communications](https://www.elbitsystems.com/news/israel-mod-procures-advanced-communication-systems-elbit-systems-approximately-130m)

### Technical & Trade Press
- [Elbit Torch-X NATO CWIX 2021 Exercise](https://www.elbitsystems.com/news/elbit-systems-torch-x-based-battle-management-application-deployed-natos-recent-multi-national)
- [Elbit Dominion-X Announcement](https://www.elbitsystems.com/news/elbit-systems-unveils-dominion-x-advanced-autonomous-management-operating-system-unmanned)
- [Elbit Frontier AI System (DSEI 2025)](https://www.elbitsystems.com/news/elbit-systems-launches-frontier-next-generation-ai-based-system-tackle-evolving-border-defense)
- [Elbit AI Defense Landscape Blog](https://www.elbitsystems.com/blog/how-ai-changing-defense-landscape)
- [Elbit Border Defense Blog](https://www.elbitsystems.com/blog/beyond-fences-building-smart-aware-borders)
- [Elbit "Battle Data Wins" Blog](https://www.elbitsystems.com/blog/battle-data-wins)
- [HattoriX European Demonstrations](https://www.elbitsystems.com/news/hattorix-ai-enabled-target-acquisition-system-concluded-demonstrations-eight-countries-across)
- [DOMINATOR Wearable Technologies](https://www.elbitsystems.com/news/elbit-systems-unveils-new-wearable-technologies-infantry-commanders-and-soldiers)
- [SPS MAI: Elbit C4I Overview](https://www.spsmai.com/military/?id=3291&q=Elbit-Systems-develops-digitised-battlefield-C4I)
- [Defense Update: WinBMS](https://defense-update.com/20051105_winbms.html)
- [Defense Update: Dominator LD](https://defense-update.com/20121018_dominator_ld.html)
- [Army Guide: DOMINATOR](http://www.army-guide.com/eng/product4267.html)
- [Australian Defence Magazine: LAND 200](https://www.australiandefence.com.au/news/land-warfare-army-s-new-battle-management-system-a-winner-adm-nov-2010)
- [APDR: Elbit BMS Withdrawn (Australia)](https://asiapacificdefencereporter.com/land-200-elbit-bms-withdrawn-from-service-but-the-reasons-remain-unclear/)
- [C2 Systems Market (Fortune Business Insights)](https://www.fortunebusinessinsights.com/command-and-control-system-market-108118)
- [C2 Systems Market (Mordor Intelligence)](https://www.mordorintelligence.com/industry-reports/command-and-control-systems-market)
- [Vanguard Canada: Elbit Networked Combat Solutions](https://vanguardcanada.com/pioneering-networked-combat-solutions-for-multi-domain-operations/)
- [Elbit JADC2 Competition](https://www.elbitamerica.com/news/elbit-systems-of-america-selected-by-u.s.-air-force-to-compete-for-joint-all-domain-command-and-control-task-orders)
- [Elbit E-LynX Brazil F-5M](https://www.edrmagazine.eu/elbit-systems-e-lynx-airborne-software-defined-radio-completes-connectivity-flight-tests-onboard-f-5m-aircraft-of-the-brazilian-air-force)
- [Elbit Systems UK: Command & Control](https://www.elbitsystems-uk.com/what-we-do/land/c4isr/command-control)
- [DOMINATOR UK Suite (PDF)](https://elbitsystems-uk.com/what-we-do/land/c4isr/soldier-equipment/dominatortm.pdf)
- [Elbit Wikipedia](https://en.wikipedia.org/wiki/Elbit_Systems)
- [Elbit Sweden Blog](https://www.elbitsystems.com/blog/sweden-midst-huge-buildup)
- [TORC2H Product Page (Elbit America)](https://www.elbitamerica.com/torc2h-product)
- [Soldier Modernisation: Land Training](https://www.soldiermod.com/volume-5/elbit-systems.html)
- [Elbit Simulating Future Ground Forces Blog](https://www.elbitsystems.com/blog/simulating-the-future)
- [E-LynX Germany](https://elbitsystems-de.com/en/products-and-solutions/communication/vhf-uhf-e-lynx/)
- [E-LynX Switzerland](https://elbitsystems-ch.com/what-we-do/new-generation-of-tactical-radio-e-lynx/)
