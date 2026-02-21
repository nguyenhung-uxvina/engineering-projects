---
project: CORTEX-C2
phase: 0
type: reverse-engineering
subject: Rheinmetall AG Training & Shooting Training Systems (Germany)
version: 1.0
created: 2026-02-12
status: complete
---

# RE Analysis: Rheinmetall AG Training & Simulation Division

> **Classification:** CORTEX C2 RANGE -- Competitive Intelligence
> **Analyst Priority:** CRITICAL -- #1 direct competitor for live-fire range analytics
> **Ticker:** XETRA: RHM | OTC: RNMBY

---

## Table of Contents

1. [Company Profile](#1-company-profile)
2. [Shooting Training Systems (STS)](#2-shooting-training-systems-sts)
3. [Simulation & Virtual Training](#3-simulation--virtual-training)
4. [Training Management Systems](#4-training-management-systems)
5. [AI & Analytics](#5-ai--analytics)
6. [Architecture & Integration](#6-architecture--integration)
7. [Key Contracts & Deployments](#7-key-contracts--deployments)
8. [Business Model & Pricing](#8-business-model--pricing)
9. [Strengths & Weaknesses](#9-strengths--weaknesses)
10. [Design Paradigm Comparison with CORTEX RANGE](#10-design-paradigm-comparison-with-cortex-range)

---

## 1. Company Profile

### 1.1 Corporate Overview

| Attribute | Value |
|-----------|-------|
| **Full Name** | Rheinmetall AG |
| **Founded** | 1889 (Dusseldorf, Germany) |
| **Headquarters** | Dusseldorf, North Rhine-Westphalia, Germany |
| **CEO** | Armin Papperger |
| **Ticker** | XETRA: RHM / OTC: RNMBY |
| **Market Cap** | ~EUR 73B (Feb 2026) |
| **Revenue (FY2024)** | EUR 9.75B (~50% YoY growth) |
| **Employees** | ~33,000 (2025) |
| **Order Backlog** | EUR 55B (Dec 2024), EUR 63B (H1 2025) |
| **Divisions** | Vehicle Systems, Weapon & Ammunition, Electronic Solutions, Power Systems |
| **Revenue Target 2030** | EUR 50B |

### 1.2 Defence Division Structure

```
Rheinmetall AG
 |
 +-- Vehicle Systems Division
 |    +-- Leopard 2, Lynx IFV, Boxer, KF51 Panther
 |    +-- American Rheinmetall (Loc Performance, acquired 2024, $950M)
 |
 +-- Weapon and Ammunition Division
 |    +-- Large/medium caliber weapons & ammunition
 |    +-- Rheinmetall Expal Munitions (acquired 2023, EUR 1.2B)
 |    +-- Rheinmetall NIOA Munitions (Australia JV)
 |
 +-- Electronic Solutions Division  <-- TRAINING LIVES HERE
 |    +-- Air Defence (Skynex, Skyranger)
 |    +-- Soldier Systems (GLADIUS 2.0, IdZ-ES)
 |    +-- Sensors & Networking
 |    +-- Simulation & Training (BU) <-- PRIMARY FOCUS
 |         +-- Rheinmetall Electronics GmbH (Bremen)
 |         +-- Rheinmetall Simulation Australia
 |         +-- Rheinmetall Arabia Simulation & Training (RAST, JV)
 |         +-- RH Mexico Simulation and Training S.A.
 |         +-- Rheinmetall Communication & Simulation Technology Pte Ltd (Singapore)
 |
 +-- Power Systems Division
      +-- Civilian automotive (declining, being divested)
```

### 1.3 Electronic Solutions Division -- Financial Context

| Metric | FY2024 | H1 2025 |
|--------|--------|---------|
| **Division Sales** | ~EUR 1.3B est. (13.5% of group) | EUR 944M (+46% YoY) |
| **Nomination (New Orders)** | EUR 5,065M (record) | EUR 9.98B (+231%) |
| **Simulation & Training Share** | ~15-20% of division est. | Growing |
| **Estimated S&T Revenue** | EUR 200-260M | Accelerating |

**Note:** Rheinmetall does not break out Simulation & Training revenue separately. The EUR 200-260M estimate is derived from division percentage analysis and contract value tracking.

### 1.4 Recent Acquisitions Relevant to Training

| Year | Target | Value | Relevance to Training |
|------|--------|-------|----------------------|
| 2023 | Expal Systems (Spain) | EUR 1.2B | Ammunition -- training munitions production |
| 2024 | Loc Performance (USA) | $950M | Vehicle hulls -- simulator physical mockups |
| 2024 | Hologate partnership | Strategic | XR/VR simulation driving simulators |
| 2025 | Varjo partnership | Strategic | MR headsets (XR-4) for vehicle sim |
| 2025 | BISim partnership | Strategic | VBS4/Blue IG integration for gunnery sims |
| 2025 | Muni Berka (Germany) | Undisclosed | Ammunition -- training rounds |

### 1.5 Key Subsidiaries for Training

| Subsidiary | Location | Focus |
|------------|----------|-------|
| **Rheinmetall Electronics GmbH** | Bremen, Germany | Simulation & Training HQ; LEGATUS, AGDUS, OSIRIS |
| **Rheinmetall Simulation Australia** | Adelaide, Australia | Boxer/Lynx ITT simulators; ADF programs |
| **Rheinmetall Soldier Electronics GmbH** | Stockach, Germany | Laser modules, VTAL, fire control; LES hardware |
| **Rheinmetall Arabia S&T (RAST)** | Riyadh, Saudi Arabia | JV with AVC Defense; Middle East training |
| **RH Mexico S&T** | Mexico | Latin America training |
| **Rheinmetall Comm & Sim Technology** | Singapore | APAC naval/army training |
| **Blackned GmbH** | Germany | Tactical Core software (5G networking for ranges) |

---

## 2. Shooting Training Systems (STS) -- CRITICAL SECTION

### 2.1 Critical Finding: Rheinmetall Does NOT Make LOMAH-Type Acoustic Scoring Systems

**This is the single most important finding in this RE analysis for CORTEX RANGE.**

After extensive research, Rheinmetall's training division focuses on:
- **Laser-based engagement simulation** (AGDUS/LEGATUS) -- simulated weapons effects, NO live rounds fired
- **Virtual gunnery simulators** (TacSi-based) -- computer simulation
- **Constructive simulation** (OSIRIS) -- staff training wargames
- **Vehicle simulators** (driver/gunnery) -- VR/MR based

Rheinmetall does **NOT** appear to manufacture or sell:
- Acoustic LOMAH scoring systems
- Electronic target scoring systems for live-fire ranges
- Pop-up infantry target mechanisms (HET/PHET)
- Automatic bullet impact scoring devices
- Live-fire range instrumentation for small arms

**Rheinmetall's training philosophy is fundamentally simulation-based, NOT live-fire range-based.** Their flagship GUZ Combat Training Centre at Letzlingen explicitly states: "During exercises at the GUZ -- conducted on a permanent basis -- live rounds are never fired."

### 2.2 What Rheinmetall DOES Offer for "Shooting Training"

Rheinmetall's "shooting training" capability is entirely virtual/simulated:

| System | Type | Live Rounds? | Detection Method |
|--------|------|-------------|-----------------|
| **AGDUS HdWa** | Laser engagement sim for small arms | NO | Laser + optical sensors |
| **AGDUS Passive Vehicles** | Laser engagement sim for vehicles | NO | Laser sensors on hull |
| **LEGATUS** | Complete live simulation ecosystem | NO | Laser + GPS + radio |
| **TacSi Gunnery Trainers** | Virtual gunnery simulation | NO | Computer simulation |
| **Immersive Tactical Trainer** | VR vehicle crew trainer | NO | VR/MR headset + haptics |

### 2.3 AGDUS (Ausbildungsgerat Duellsimulator) -- Training Device, Duel Simulator

**AGDUS is Rheinmetall's core live training hardware and their closest product to "shooting training."**

| Feature | Detail |
|---------|--------|
| **Full Name** | Ausbildungsgerat Duellsimulator (Training Device, Duel Simulator) |
| **Type** | Laser-based weapons effect simulator (similar to US MILES) |
| **Primary Customer** | Bundeswehr (German Army) |
| **Location** | GUZ Combat Training Centre, Letzlingen, Germany |
| **How It Works** | Laser transmitter attached to real weapon; laser sensors on target soldiers/vehicles detect "hits" |
| **Wireless** | Yes -- new generation uses wireless data transmission |
| **Weapons Supported** | Pistols, assault rifles, G28/G82 sniper rifles, MP7, MG4/MG5, AG40 grenade launcher, hand grenade simulators |
| **Vehicle Weapons** | Puma IFV: 30mm cannon, co-axial MG, Spike-LR ATGM simulation |
| **Networking** | All participants networked in real-time for AAR |
| **After Action Review** | Yes -- detailed playback of all engagements |

#### AGDUS Variants

| Variant | Description | Contract Details |
|---------|-------------|-----------------|
| **AGDUS HdWa (Small Arms)** | Laser transmitter units for infantry weapons | EUR ~20M for 2,000+ transmitters + 1,500 soldier sensor sets |
| **AGDUS Passive Soldier** | Wearable laser sensor harness for individual soldiers | Part of HdWa contract |
| **AGDUS Passive Vehicle** | Laser sensor arrays mounted on combat vehicles | Upper single-digit million EUR for 440 systems |
| **AGDUS Puma IFV** | Dedicated AGDUS for Puma Infantry Fighting Vehicle | Simulates 30mm, MG, Spike-LR, TSWA, self-defense |

### 2.4 LEGATUS Live Training System -- The "STS" Equivalent

LEGATUS is Rheinmetall's flagship live training platform -- essentially a comprehensive instrumented training system, but for **simulated** (laser) engagement, not live fire.

| Feature | Detail |
|---------|--------|
| **Product Family** | Modular live training system family |
| **Scale** | Individual soldier up to reinforced brigade level |
| **Core Technology** | Laser engagement + GPS tracking + radio networking |
| **Environment** | Open terrain AND urban (MOUT) |
| **Tracking** | Real-time position tracking of all players (soldiers, civilians, vehicles) indoors and outdoors |
| **Weapons Simulation** | Any real weapon type via laser transmitter calibration |
| **Building Penetration** | Vulnerability of buildings and people inside can be simulated |
| **Exercise Control** | Real-time monitoring from central EXCON |
| **AAR** | Comprehensive after-action review with full replay |
| **Integration** | Designed for GLADIUS 2.0 soldier system integration |
| **Mobile Deployment** | Mobile Combat Training Center (MCTC) variant in containerized modules |
| **Remote Operations** | "Reachback" capability -- connect to GUZ from Lithuania via network |

#### LEGATUS Architecture

```
LEGATUS System Architecture
 |
 +-- Laser Engagement Subsystem
 |    +-- Weapon-mounted laser transmitters (all calibers)
 |    +-- Body-worn laser sensors (AGDUS Passive Soldier)
 |    +-- Vehicle-mounted laser sensors (AGDUS Passive Vehicle)
 |    +-- Building-integrated sensors (MOUT)
 |
 +-- Positioning & Tracking
 |    +-- GPS/GNSS outdoor tracking
 |    +-- Indoor tracking system (for MOUT buildings)
 |    +-- Real-time position reporting
 |
 +-- Communications Network
 |    +-- Wireless data link (soldier-to-EXCON)
 |    +-- 5G infrastructure (new Blackned Tactical Core)
 |    +-- Long-range WAN (for reachback to GUZ)
 |
 +-- Exercise Control (EXCON)
 |    +-- Scenario definition & management
 |    +-- Real-time monitoring (2D/3D map display)
 |    +-- Casualty assessment & status
 |    +-- Instructor tools
 |
 +-- After Action Review (AAR)
      +-- Full exercise replay
      +-- Individual engagement analysis
      +-- Movement track visualization
      +-- Performance metrics
```

### 2.5 Comparison: AGDUS/LEGATUS vs. Live-Fire LOMAH Scoring

| Attribute | Rheinmetall AGDUS/LEGATUS | LOMAH Acoustic Scoring (e.g., Zen, Polytronic) |
|-----------|--------------------------|------------------------------------------------|
| **Rounds Fired** | NONE (laser only) | LIVE ammunition |
| **Hit Detection** | Laser sensor on target body/vehicle | Acoustic microphone array at target |
| **Accuracy** | ~1m engagement zone | +/- 5mm bullet position |
| **What It Measures** | Who shot whom, when, where | Exact bullet impact location on/near target |
| **Scoring** | Binary (hit/miss) + engagement parameters | Precise X,Y coordinates, score rings |
| **Group Analysis** | No (no real bullets) | Yes -- shot group size, mean point of impact |
| **Marksmanship Training** | NOT designed for this | PRIMARY purpose |
| **Tactical Training** | PRIMARY purpose | NOT designed for this |
| **Cost** | EUR 10K-50K+ per participant set | $2K-15K per lane |
| **Infrastructure** | Training area + EXCON | Firing range + target frames |
| **Complementary?** | YES -- different training domains | YES -- different training domains |

**Key Insight:** AGDUS/LEGATUS and LOMAH/CORTEX RANGE serve **completely different training needs**. They are complementary, not directly competitive for the same use case. AGDUS trains tactical behavior; LOMAH/CORTEX trains marksmanship accuracy.

### 2.6 Live-Fire Range Products -- Gap in Rheinmetall Portfolio

Rheinmetall does **NOT** appear to offer the following products that competitors provide:

| Product Category | Rheinmetall | Competitors Who Offer It |
|-----------------|-------------|-------------------------|
| Acoustic LOMAH scoring | NO | Zen Technologies, Polytronic, Steinert, Oakwood |
| Electronic target scoring | NO | Theissen (TTS), INTARSO, SIUS, ShotMarker |
| Pop-up infantry targets (HET) | NO | Theissen, InVeris (formerly Meggitt), Action Target |
| Moving target trolleys | NO | Marathon Targets, Theissen, InVeris |
| Bullet trap systems | NO | InVeris, Range Systems, Action Target |
| Range control systems | NO | InVeris (SmartRange), Zen (MCS), Action Target |
| Target retrieval systems | NO | Super Target Systems, Range Systems |
| Live-fire shoot houses | NO | InVeris, Action Target, SRT |

**This is a critical gap in Rheinmetall's portfolio that CORTEX RANGE can exploit.**

---

## 3. Simulation & Virtual Training

### 3.1 Product Portfolio Overview

Rheinmetall's simulation training portfolio spans all three LVC (Live, Virtual, Constructive) domains:

| Domain | Products | Description |
|--------|----------|-------------|
| **Live (L)** | LEGATUS, AGDUS | Laser engagement, GPS tracking, real equipment |
| **Virtual (V)** | TacSi gunnery trainers, ITT, DTS | Computer-generated environments, crew stations |
| **Constructive (C)** | OSIRIS | Command & staff training, wargaming |
| **LVC Integration** | Planned | Connecting all three domains |

### 3.2 TacSi -- Tactical Simulation Engine

TacSi is Rheinmetall's proprietary high-end scenario generator for virtual training.

| Feature | Detail |
|---------|--------|
| **Name** | TacSi (Tactical Simulation) |
| **Type** | Core simulation engine / scenario generator |
| **Visual Engine** | Game-based visual system technology |
| **Ballistics** | Sophisticated ballistics simulation model |
| **CGF** | Computer Generated Forces for automated combat control |
| **Fidelity** | Configurable -- from desktop trainer to full mission simulator |
| **Networking** | Intrinsic networking for multi-station exercises |
| **Scale** | Single gunnery trainer to company-level network |
| **Vehicle Types** | Leopard 2, Puma, Boxer, Lynx, various patrol vehicles |

### 3.3 Combat & Gunnery Skills Training Systems

| System | Platform | Status |
|--------|----------|--------|
| **Leopard Gunnery Skills Trainer (LGST)** | Leopard 2A4/A6/A7 | Delivered to Indonesia, Poland, Germany |
| **Leopard Driver Training Simulator (DTS)** | Leopard 2 | Delivered to Indonesia, Poland |
| **Puma IFV Gunnery Trainer** | Puma IFV | Approved by Bundeswehr Sep 2025 |
| **Boxer Immersive Tactical Trainer (ITT)** | Boxer CRV | AU$40M contract for ADF (Land 400 Phase 2) |
| **Lynx ITT** | Lynx IFV | Commander, gunner, driver stations |
| **Heavy Weapons Carrier Sim** | New platform | BISim VBS4/Blue IG integration (2025) |
| **XR Driving Simulator** | Generic military vehicles | Hologate partnership (2024), Varjo XR-4 (2025) |

### 3.4 OSIRIS -- Constructive Command & Staff Trainer

| Feature | Detail |
|---------|--------|
| **Name** | OSIRIS |
| **Type** | Constructive simulation for command & staff training |
| **Scale** | Battalion to joint forces command HQ |
| **Domains** | Land, sea, air -- all three branches |
| **Automation** | Unique automation enables tactical AND operational scenarios |
| **Scenarios** | Disaster relief to national defense to peacekeeping |
| **UI** | Optimized user interface reduces training time and operator errors |
| **Architecture** | Modern, customer-specific IT infrastructure |
| **BMS Integration** | Connects to battle management systems |
| **Key Customer** | Swiss Army (General Staff School, Kriens) |
| **Scalability** | Single laptop to full brigade-level system |

### 3.5 Naval Training Solutions

| System | Description |
|--------|-------------|
| **VTAM** | Distributed Naval Training Architecture -- first-of-kind for German Navy (2024 contract, mid-double-digit million EUR) |
| **ANS6000** | Ship handling and navigation simulation (commercial maritime) |
| **HLS7** | Heavy lift simulator for cargo operations |
| **Sensor & Weapon Training** | Sonar, radar, electro-optics simulation |
| **Naval Mission Training Center** | "Total ship training" exported to undisclosed customer (2023) |
| **Damage Control Training** | Shipboard damage response simulation |

### 3.6 XR/MR Technology Partnerships (2024-2025)

| Partner | Technology | Application | Date |
|---------|-----------|-------------|------|
| **Varjo** | XR-4 Series mixed reality headsets | Vehicle driving/gunnery simulation; physical hardware + virtual terrain | Nov 2025 |
| **Hologate** | XR/VR motion platforms | Military driver training VR simulator | Dec 2024 |
| **BISim (BAE)** | VBS4 + Blue IG | Gunnery & combat simulators for Heavy Weapons Carrier | Jan 2025 |

---

## 4. Training Management Systems

### 4.1 Integrated Training Management

Rheinmetall does not appear to market a standalone "Training Management System" (TMS) software product. Instead, training management functionality is embedded within their larger systems:

| Capability | Where It Lives | Details |
|-----------|---------------|---------|
| **Exercise Planning** | LEGATUS EXCON | Scenario definition, OOB setup, terrain selection |
| **Real-time Monitoring** | LEGATUS EXCON | 2D/3D tracking of all exercise participants |
| **Casualty Assessment** | LEGATUS / AGDUS | Automatic hit determination, damage assessment |
| **After Action Review** | LEGATUS AAR module | Full replay, engagement analysis, movement tracks |
| **Performance Evaluation** | Embedded in simulators | TacSi-based scoring for gunnery qualification |
| **e-Learning** | CBT modules | Computer-based training for vehicle familiarization |
| **Course Management** | Contract-specific | Custom LMS implementations per customer |

### 4.2 After Action Review (AAR) Capabilities

Rheinmetall's AAR capability is primarily tied to the LEGATUS live simulation system:

| AAR Feature | Detail |
|-------------|--------|
| **Playback** | Full 2D/3D replay of exercise from any perspective |
| **Engagement Analysis** | Who shot whom, when, with what weapon, at what range |
| **Movement Tracking** | GPS tracks of all participants (soldiers + vehicles) |
| **Indoor Tracking** | Building-interior position tracking for MOUT |
| **Instructor Tools** | Annotate, bookmark, slow-motion, multi-angle |
| **Export** | Exercise reports for documentation |
| **AI-Driven Analysis** | NOT currently available (manual instructor analysis) |

### 4.3 Comparison with CORTEX RANGE Training Analytics

| Feature | Rheinmetall AAR | CORTEX RANGE (Target) |
|---------|----------------|----------------------|
| **Data Source** | Laser engagement simulation | Live-fire acoustic LOMAH scoring |
| **Marksmanship Analytics** | None (no bullet data) | Shot group analysis, MPI, score trends |
| **Tactical Analytics** | Movement, engagement timing, positioning | Limited (range-focused) |
| **AI/ML Analytics** | None currently | Core differentiator |
| **Predictive Readiness** | None | Planned ML feature |
| **Standalone Software** | No (embedded in LEGATUS) | Yes (cloud/edge platform) |
| **Price Point** | Part of multi-million EUR system | $15-25K per unit |
| **Retrofit to Existing Ranges** | No | Yes -- primary use case |

---

## 5. AI & Analytics

### 5.1 Current AI/ML Capabilities in Training

Rheinmetall's AI efforts in training are **nascent and primarily aspirational** as of early 2026.

| Area | Status | Details |
|------|--------|---------|
| **Training AI/ML Analytics** | NOT DEPLOYED | No AI-driven performance assessment in LEGATUS or AGDUS |
| **CGF Automation** | DEPLOYED | Computer Generated Forces in TacSi (rule-based, not ML) |
| **Scenario Generation** | RESEARCH | Automated scenario generation explored but not productized |
| **Predictive Readiness** | NOT AVAILABLE | No equivalent to CORTEX RANGE's planned ML readiness scoring |
| **Computer Vision Scoring** | NOT AVAILABLE | Not applicable (laser systems, not visual scoring) |
| **Digital Twin for Training** | EARLY STAGE | Vehicle digital twins for maintenance, not training analytics |

### 5.2 AI Strategy -- Broader Rheinmetall (Non-Training)

Rheinmetall's AI investments are primarily focused on operational systems, not training:

| AI Application | Division | Maturity |
|---------------|----------|----------|
| **IRIS Suite** | Logistics | Deployed -- predictive maintenance for vehicle fleets |
| **Autonomous Vehicles** | Vehicle Systems | R&D -- Mission Master UGV |
| **Air Defense AI** | Electronic Solutions | R&D -- Skynex/Skyranger target classification |
| **Digital Twin** | Air Defence | Deployed -- 3D digital twin for change impact analysis (Spread.ai) |
| **Geo Data Analysis** | C4I | R&D -- AI position analysis for mission planning |

### 5.3 Key Gap: No AI-Native Training Analytics

**Rheinmetall has NOT developed AI-native training analytics.** This is a significant gap:

- No machine learning models for marksmanship performance prediction
- No automated coaching recommendations
- No longitudinal skill progression tracking with ML
- No anomaly detection for training degradation
- No natural language AAR summaries
- CGF in TacSi uses rule-based behavior, not learned behavior

**This is CORTEX RANGE's primary competitive advantage vector against Rheinmetall.**

---

## 6. Architecture & Integration

### 6.1 Standards Compliance

| Standard | Rheinmetall Usage |
|----------|------------------|
| **HLA (IEEE 1516)** | Used in constructive simulation (OSIRIS) for federation |
| **DIS (IEEE 1278)** | Supported for real-time entity-level interoperability |
| **STANAG 4603** | NATO standard for HLA -- Rheinmetall compliant |
| **STANAG 4586** | UAV control -- related to Luna NG integration |
| **D-LBO** | Digitalisation of Land-based Operations (Bundeswehr) -- core integration target |
| **SAPIENT** | Not mentioned -- CORTEX RANGE advantage |

### 6.2 Network Architecture

```
Rheinmetall Training Network Architecture
 |
 +-- Strategic Level (WAN)
 |    +-- GUZ Letzlingen <---> Lithuania (Reachback via military WAN)
 |    +-- Naval bases (6 locations for VTAM)
 |
 +-- Tactical Level (LAN/Radio)
 |    +-- 5G Blackned Tactical Core (new, being integrated 2025-2028)
 |    +-- Legacy radio infrastructure (being upgraded at GUZ)
 |    +-- Wireless AGDUS data links
 |    +-- GPS/GNSS positioning
 |
 +-- Simulation Level
 |    +-- TacSi scenario engine (central server)
 |    +-- BMS integration (D-LBO battle management)
 |    +-- HLA/DIS federation for LVC
 |
 +-- Hardware Level
      +-- Laser transmitters (weapon-mounted)
      +-- Laser sensors (body/vehicle-mounted)
      +-- Indoor positioning nodes (MOUT buildings)
      +-- EXCON workstations
```

### 6.3 Interoperability with C2 Systems

| System | Integration Status |
|--------|-------------------|
| **Bundeswehr BMS** | Integrated via D-LBO project |
| **GLADIUS 2.0** | Native integration -- LEGATUS designed for GLADIUS |
| **NATO STANAG** | HLA/DIS compliant for multinational exercises |
| **Third-party Ranges** | NOT interoperable -- Rheinmetall is a closed ecosystem |
| **ATAK/TAK** | Not mentioned |
| **SAPIENT** | Not mentioned |

---

## 7. Key Contracts & Deployments

### 7.1 Major Training Contracts (2020-2025)

| Year | Customer | Program | Value | Details |
|------|----------|---------|-------|---------|
| 2025 | Bundeswehr | GUZ Modernization (D-LBO) | EUR 61M | 5G infrastructure, digital radio, Tactical Core; complete 2028 |
| 2025 | Bundeswehr | Puma IFV Training System | Undisclosed | Approved Sep 2025; gunnery & combat simulation |
| 2025 | Bundeswehr | IdZ-ES Soldier System | EUR 3.2B (framework) | Includes LEGATUS training integration |
| 2024 | German Navy | VTAM Naval Training | Mid-double-digit million EUR | 6 naval bases; first distributed naval training for Germany |
| 2024 | Bundeswehr | MCTC Legatus Lithuania | Part of GUZ contract | Reachback containerized training tested Dec 2024 |
| 2023 | Undisclosed export | Naval Mission Training Center | Undisclosed | "Total ship training" -- first export of this type |
| 2023 | ADF (Australia) | Boxer CRV Simulators | AU$40M (EUR 25M) | Immersive Tactical Trainers for Land 400 Phase 2 |
| 2022 | UK MoD | CTTP (Omnia Training team) | Bid phase | Consortium with Raytheon UK, Capita, Cervus, Improbable |
| 2022 | Canadian Army | LVCTS (FORC3 team) | Bid phase | Consortium with Lockheed Martin, Calian |
| 2021 | Bundeswehr | AGDUS Passive Vehicle | Upper single-digit million EUR | 440 systems for GUZ Combat Training Centre |
| 2020 | Bundeswehr | AGDUS Puma IFV | Undisclosed | Laser duel simulators for Puma fleet |
| 2019 | Swiss Army | OSIRIS Command Simulator | Undisclosed | General Staff School, Kriens |
| 2016 | Bundeswehr | AGDUS HdWa (Small Arms) | ~EUR 20M | 2,000+ laser transmitters + 1,500 soldier sensor sets |
| Pre-2014 | Russian Army | Combat Training Centre | Undisclosed | GUZ-type facility (pre-Crimea sanctions) |

### 7.2 Installed Base

| Region | Training Installations |
|--------|----------------------|
| **Germany** | GUZ Combat Training Centre (Letzlingen) -- anchor installation; 6 naval bases (VTAM); multiple Bundeswehr schools |
| **Australia** | Boxer CRV simulators at Military Vehicle Centre of Excellence (Adelaide); Leopard simulation legacy |
| **Indonesia** | Leopard 2A4 RI gunnery & driver simulators (acceptance tests passed) |
| **Poland** | Leopard gunnery & driver simulators (modernized) |
| **Switzerland** | OSIRIS command simulator (General Staff School) |
| **Saudi Arabia** | Via RAST JV -- details classified |
| **Singapore** | Via Rheinmetall Comm & Sim Technology -- naval/army |
| **Lithuania** | MCTC Legatus (container-based, reachback to GUZ) |
| **Russia** | Pre-sanctions combat training centre (likely dormant) |
| **UK** | Bid phase for CTTP (Omnia Training consortium) |
| **Canada** | Bid phase for LVCTS (FORC3 consortium) |

**Estimated Total Installations:** 15-25 active training system deployments globally (not counting individual simulator units).

### 7.3 Bundeswehr GUZ -- The Flagship

The Gefechtsübungszentrum Heer (GUZ, Army Combat Training Centre) in Letzlingen, Saxony-Anhalt is Rheinmetall's most important reference installation.

| Feature | Detail |
|---------|--------|
| **Operational Since** | 2001 |
| **Operator** | Rheinmetall (contracted by Bundeswehr) |
| **Location** | Altmark district, Saxony-Anhalt |
| **Size** | One of Europe's largest instrumented training areas |
| **Live Rounds** | NEVER fired -- all laser engagement |
| **Scale** | Up to reinforced brigade-level exercises |
| **Participants** | Individual soldiers, all vehicle types, buildings |
| **Infrastructure** | Permanent EXCON, sensor networks, MOUT village |
| **Modernization** | EUR 61M contract (2025) for D-LBO/5G integration |
| **Multinational** | Used for NATO exercises; reachback to Lithuania tested |

---

## 8. Business Model & Pricing

### 8.1 Sales Model

Rheinmetall's training business uses multiple sales models:

| Model | Description | Example |
|-------|-------------|---------|
| **Turnkey Training Centre** | Design, build, equip, commission complete training facility | GUZ Letzlingen |
| **System Sale** | Sell simulator hardware + software + installation | Boxer ITT to ADF (AU$40M) |
| **Upgrade/Modernization** | Upgrade existing Rheinmetall installations | GUZ D-LBO integration (EUR 61M) |
| **Through-Life Support** | Ongoing O&M, spares, software updates | GUZ operations support |
| **Consortium Bid** | Joint bid with partners for large programs | CTTP (UK), LVCTS (Canada) |
| **JV Operations** | Joint venture for local presence | RAST (Saudi Arabia) |
| **Technology Partnership** | Strategic partnership for component supply | BISim, Varjo, Hologate |

### 8.2 Estimated Pricing

| Product / Service | Estimated Price Range | Basis |
|-------------------|----------------------|-------|
| **AGDUS HdWa complete set** | EUR 8K-12K per soldier | EUR 20M / ~2,000 units |
| **AGDUS Passive Vehicle set** | EUR 15K-25K per vehicle | Upper single-digit million / 440 sets |
| **LEGATUS per participant** | EUR 20K-50K per equipped entity | System complexity |
| **Full LEGATUS for battalion** | EUR 5M-15M | Estimated from contract patterns |
| **MCTC (container-based)** | EUR 10M-30M | Containerized brigade-level |
| **GUZ-type Training Centre** | EUR 100M-500M+ | Full turnkey including infrastructure |
| **Vehicle Simulator (ITT)** | EUR 2M-5M per station | AU$40M for ~10 Boxer ITTs |
| **OSIRIS system** | EUR 5M-15M | Command & staff trainer |
| **VTAM Naval Training** | EUR 30M-70M | Mid-double-digit million contract |
| **GUZ Modernization** | EUR 61M | Actual contract value (2025) |
| **Annual O&M (GUZ)** | EUR 10M-30M est. | Ongoing operations support |

### 8.3 O&M and Lifecycle Support

| Aspect | Model |
|--------|-------|
| **Hardware Maintenance** | Rheinmetall-provided spares + technicians |
| **Software Updates** | Periodic upgrades (e.g., new vehicle models, terrain DBs) |
| **Scenario Development** | Customer or Rheinmetall service |
| **Training of Trainers** | Included in delivery, ongoing available |
| **Technology Refresh** | Modernization contracts (e.g., GUZ D-LBO every 5-10 years) |
| **Proprietary Lock-in** | HIGH -- all systems are proprietary Rheinmetall |

---

## 9. Strengths & Weaknesses

### 9.1 Strengths

| # | Strength | Impact |
|---|----------|--------|
| S1 | **135+ years of defense industry credibility** | Trusted by Bundeswehr, NATO allies, and export customers; Rheinmetall brand carries extreme weight in procurement decisions |
| S2 | **End-to-end system integrator** | Makes the vehicles (Leopard, Puma, Boxer, Lynx), the weapons, AND the training systems -- unmatched vertical integration |
| S3 | **GUZ Combat Training Centre as flagship reference** | Operational since 2001; "gold standard" for instrumented live training in Europe |
| S4 | **LEGATUS proven at brigade scale** | Scalable from individual to brigade+; tested in multinational context (Lithuania reachback) |
| S5 | **40+ years in simulation & training** | Deep institutional knowledge; thousands of person-years of simulation engineering |
| S6 | **EUR 9.75B group revenue provides financial depth** | Can cross-subsidize training bids with vehicle/ammunition revenue; bundling leverage |
| S7 | **EUR 55B+ order backlog** | Financial stability and growth momentum attract best engineering talent |
| S8 | **Global subsidiary network** | Australia, Singapore, Saudi Arabia, Mexico, Canada -- local presence in key markets |
| S9 | **GLADIUS 2.0 / IdZ-ES soldier system integration** | LEGATUS natively integrated with soldier system sold to same customers |
| S10 | **Strategic partnerships with best-in-class technology providers** | BISim (VBS4), Varjo (XR-4), Hologate (VR), Blackned (5G) -- assembles latest tech |
| S11 | **NATO/Bundeswehr incumbent advantage** | Deeply embedded in German/NATO procurement culture; long-term framework agreements |
| S12 | **LVC coverage** | Live (LEGATUS), Virtual (TacSi), Constructive (OSIRIS) -- full spectrum |

### 9.2 Weaknesses

| # | Weakness | Opportunity for CORTEX RANGE |
|---|----------|------------------------------|
| W1 | **NO live-fire range scoring capability** | Rheinmetall cannot compete for LOMAH/acoustic scoring systems; CORTEX RANGE has zero competition from them in this domain |
| W2 | **No AI/ML in training analytics** | CGF is rule-based; no predictive readiness, no automated coaching; CORTEX RANGE's AI-native approach is a generation ahead |
| W3 | **Extremely high price point** | Minimum EUR 5M-15M for meaningful training capability; CORTEX RANGE at $15-25K is 200-600x cheaper per unit |
| W4 | **Long procurement cycles** | Turnkey training centres take 3-5 years from contract to operational; CORTEX RANGE deploys in hours |
| W5 | **Proprietary closed ecosystem** | Lock-in by design; does not interoperate with non-Rheinmetall systems; CORTEX RANGE is designed as open platform |
| W6 | **No marksmanship training capability** | AGDUS/LEGATUS trains tactics, NOT shooting accuracy; fundamental gap for individual skill development |
| W7 | **European-centric customer base** | Heavily dependent on Bundeswehr; limited penetration in APAC, Middle East, Africa, Latin America; CORTEX targets these markets |
| W8 | **No software-only product** | Every offering requires substantial hardware; no SaaS/software-as-a-service model; CORTEX RANGE is software-first |
| W9 | **Cannot retrofit to existing ranges** | Requires purpose-built training areas with installed infrastructure; CORTEX RANGE overlays on any existing range |
| W10 | **No cloud/edge architecture** | On-premises only; no remote access to training data; CORTEX RANGE is cloud-native |
| W11 | **AAR is manual/instructor-dependent** | No automated performance assessment; requires experienced observers; CORTEX RANGE automates this |
| W12 | **No small arms marksmanship data analytics** | Cannot track individual shooter progression over time; CORTEX RANGE's core feature |

### 9.3 Why Customers Might Prefer CORTEX RANGE

| Scenario | Why CORTEX RANGE Wins |
|----------|----------------------|
| **"We need to improve marksmanship"** | Rheinmetall has nothing for this; CORTEX RANGE is purpose-built |
| **"We have existing ranges"** | Rheinmetall requires new infrastructure; CORTEX overlays on existing |
| **"Our budget is <$100K"** | Rheinmetall's minimum is EUR 5M+; CORTEX starts at $15K |
| **"We want AI-driven analytics"** | Rheinmetall has no AI in training; CORTEX is AI-native |
| **"We need it deployed this month"** | Rheinmetall takes years; CORTEX deploys in hours/days |
| **"We want to track skill progression"** | Rheinmetall has no longitudinal analytics; CORTEX's core value proposition |
| **"We want a software platform"** | Rheinmetall sells hardware systems; CORTEX is software-first |
| **"We need ITAR-free"** | Rheinmetall is German export-controlled; CORTEX is ITAR-free |

---

## 10. Design Paradigm Comparison with CORTEX RANGE

### 10.1 Philosophy Comparison

| Dimension | Rheinmetall Training | CORTEX RANGE |
|-----------|---------------------|--------------|
| **Core Philosophy** | Hardware-centric, turnkey training infrastructure | Software-first, AI-native analytics platform |
| **Design Approach** | German systems engineering; build complete training environments | Lean startup; modular overlay on existing infrastructure |
| **Primary Domain** | Tactical force-on-force simulation | Live-fire marksmanship scoring and analytics |
| **Detection Method** | Laser engagement simulation | Acoustic LOMAH (microphone array) |
| **AI Strategy** | Nascent; rule-based CGF; partnerships for tech | AI-native from day one; ML-driven analytics core |
| **Customer Model** | Government prime contract (multi-year, multi-million) | Direct sale/SaaS to range operators ($15-25K) |
| **Deployment Model** | Purpose-built facility + years of integration | Install on existing range in hours |
| **Data Architecture** | On-premises, proprietary, closed | Cloud/edge, open APIs, interoperable |
| **Upgrade Path** | Major modernization contracts every 5-10 years | Continuous OTA software updates |
| **Scalability** | Scale up = more hardware = more cost | Scale up = more software licenses |
| **Integration** | Proprietary ecosystem only | Designed for open integration (SAPIENT, TAK, BMS) |

### 10.2 Feature Comparison Table

| Feature | Rheinmetall (LEGATUS/AGDUS) | CORTEX RANGE | Winner |
|---------|----------------------------|--------------|--------|
| **Hit Detection Method** | Laser sensor (binary hit/miss) | Acoustic LOMAH (precise X,Y) | CORTEX (precision) |
| **Scoring Accuracy** | ~1m zone | +/- 5mm | CORTEX |
| **Live Rounds** | No | Yes | CORTEX (realism) |
| **Shot Group Analysis** | N/A | Yes (MPI, spread, trend) | CORTEX |
| **Tactical Behavior Tracking** | Yes (GPS + laser) | No | Rheinmetall |
| **Force-on-Force** | Yes (brigade scale) | No | Rheinmetall |
| **MOUT/Urban Training** | Yes (building-integrated) | No | Rheinmetall |
| **Vehicle Engagement Sim** | Yes (all vehicles) | No (small arms only) | Rheinmetall |
| **AI/ML Analytics** | None | Core feature | CORTEX |
| **Predictive Readiness** | None | Planned | CORTEX |
| **Automated AAR** | Partial (replay, no AI) | Yes (AI-generated insights) | CORTEX |
| **Longitudinal Tracking** | None | Core feature | CORTEX |
| **Cloud Connectivity** | None | Yes (cloud-native) | CORTEX |
| **Mobile/Tablet Interface** | None | Yes | CORTEX |
| **Retrofit to Existing Range** | No | Yes | CORTEX |
| **Deployment Time** | Months to years | Hours to days | CORTEX |
| **Standards (DIS/HLA)** | Yes | Planned | Rheinmetall |
| **Integration with BMS** | Yes (D-LBO) | Planned (SAPIENT/TAK) | Rheinmetall |

### 10.3 Price Comparison

| Capability | Rheinmetall Cost | CORTEX RANGE Cost | Ratio |
|-----------|-----------------|-------------------|-------|
| **Single soldier training set** | EUR 8K-12K (AGDUS HdWa) | N/A (different product) | N/A |
| **Single lane scoring** | NOT AVAILABLE | $15-25K | Rheinmetall cannot compete |
| **10-lane instrumented range** | EUR 1M+ (if they offered it) | $150-250K | 4-7x cheaper |
| **Battalion training system** | EUR 5-15M (LEGATUS) | $200-500K (range analytics) | 10-75x cheaper |
| **Full training centre** | EUR 100-500M+ (GUZ-type) | Not comparable | Different markets |
| **Annual O&M per lane** | N/A | $2-5K (SaaS) | Rheinmetall cannot compete |

### 10.4 Market Segment Analysis

| Market Segment | Rheinmetall Position | CORTEX RANGE Position | Who Wins? |
|---------------|---------------------|----------------------|-----------|
| **NATO Tier 1 (US, UK, DE, FR)** | Strong -- incumbent supplier | Weak -- no presence yet | Rheinmetall (but different products) |
| **NATO Tier 2 (PL, NO, NL, ES)** | Moderate -- via vehicle programs | Opportunity -- cost-conscious | CORTEX (for marksmanship) |
| **APAC (AU, SG, ID, VN)** | Moderate -- Australia strong | Strong opportunity | CORTEX (cost, speed, ITAR-free) |
| **Middle East (SA, AE, QA)** | Moderate -- via RAST JV | Opportunity | Split (different needs) |
| **Africa** | Weak | Opportunity -- cost sensitive | CORTEX |
| **Latin America** | Weak (Mexico only) | Opportunity | CORTEX |
| **Police/Law Enforcement** | Very weak | Strong opportunity | CORTEX |
| **Existing ranges needing upgrade** | Cannot serve this market | PRIMARY market | CORTEX |
| **Budget-constrained militaries** | Cannot serve (<$1M budgets) | PRIMARY target | CORTEX |

### 10.5 Specific Gaps CORTEX RANGE Can Exploit

| Gap | Detail | CORTEX RANGE Approach |
|-----|--------|----------------------|
| **G1: No live-fire scoring** | Rheinmetall literally cannot score live bullets | CORTEX RANGE's core acoustic LOMAH capability |
| **G2: No marksmanship analytics** | Cannot measure shot placement accuracy | AI-driven grouping analysis, MPI tracking, qualification scoring |
| **G3: No shooter progression tracking** | Cannot track individual improvement over time | Longitudinal ML models for every shooter |
| **G4: No automated coaching** | Instructor must manually review every engagement | AI-generated coaching recommendations |
| **G5: No range retrofit capability** | Requires purpose-built infrastructure | Bolt-on to any existing military range |
| **G6: Price floor of EUR 5M+** | Cannot address sub-million budgets | Starting at $15K per lane |
| **G7: No software-only sale** | Every product requires hardware delivery and integration | Software + COTS acoustic sensor hardware |
| **G8: No SaaS model** | One-time sale + O&M contract | Monthly/annual SaaS pricing option |
| **G9: No cloud analytics** | All data stays on-premises | Cloud dashboards for centralized command visibility |
| **G10: No cross-range benchmarking** | Each installation is isolated | Network effect -- compare units, bases, cohorts |

### 10.6 Competitive Strategy Against Rheinmetall

**Rheinmetall is NOT a direct competitor -- they are a potential PARTNER or ADJACENT player.**

The correct competitive strategy is:

1. **Avoid head-to-head** -- Never position CORTEX RANGE as a replacement for LEGATUS/AGDUS. They serve fundamentally different training domains.

2. **Complement, then expand** -- Position CORTEX RANGE as the "marksmanship layer" that complements Rheinmetall's "tactical layer." Offer integration.

3. **Target the gaps** -- Focus on the markets and use cases where Rheinmetall literally cannot compete: live-fire scoring, small arms qualification, range analytics, AI coaching.

4. **Undercut on price** -- For customers who cannot afford EUR 5M+ Rheinmetall systems, CORTEX RANGE at $15-25K is the only option.

5. **Speed to deploy** -- For urgent training needs (e.g., Ukraine, NATO readiness push), CORTEX RANGE's hours-to-deploy vs. Rheinmetall's years-to-deploy is decisive.

6. **Software moat** -- Build AI/ML capabilities that Rheinmetall cannot replicate with their hardware-first DNA. By the time they pivot to software, CORTEX RANGE will have years of training data and model refinement.

7. **Potential partnership** -- In the long term, Rheinmetall may seek to add marksmanship analytics to their training portfolio. CORTEX RANGE could be acquired by or partnered with Rheinmetall to fill their live-fire gap.

---

## Appendix A: Rheinmetall Training Technology Timeline

| Year | Event |
|------|-------|
| ~1985 | Rheinmetall enters simulation & training market |
| 2001 | GUZ Combat Training Centre operational at Letzlingen |
| ~2005 | First-generation AGDUS deployed to Bundeswehr |
| 2011 | Russian training centre contract (pre-sanctions) |
| 2016 | Second-generation AGDUS HdWa (small arms) contract |
| 2017 | LEGATUS unveiled at DSEI and I/ITSEC |
| 2019 | OSIRIS to Swiss Army |
| 2020 | AGDUS for Puma IFV; LVCTS bid (Canada) with Lockheed Martin |
| 2021 | AGDUS Passive Vehicle (440 systems) to Bundeswehr |
| 2022 | CTTP bid (UK) with Raytheon UK consortium |
| 2023 | Boxer CRV simulators (AU$40M) to ADF; Naval Mission Training Center exported |
| 2024 | VTAM naval training contract; Hologate VR partnership; MCTC Lithuania test |
| 2025 | BISim partnership; Varjo XR-4 partnership; GUZ modernization (EUR 61M); Puma training system approved |

## Appendix B: Rheinmetall vs. Actual LOMAH/Range Competitors

Since Rheinmetall does not compete in the live-fire range scoring space, CORTEX RANGE's actual direct competitors are:

| Competitor | Country | Key Product | Detection Method | Estimated Price/Lane |
|-----------|---------|-------------|-----------------|---------------------|
| **Zen Technologies** | India | LOMAH Smart Target | Acoustic | $5-15K |
| **Polytronic International** | Switzerland | Various LOMAH systems | Acoustic | $10-30K |
| **Steinert Sensing** | USA | TrueZeroTarget | Acoustic LOMAH | $5-15K |
| **Oakwood Controls** | UK | Portable Electronic Target | Acoustic | $5-15K |
| **Theissen Training (TTS)** | Germany | Electronic Scoring Targets | Acoustic/optical | $10-25K |
| **InVeris (ex-Meggitt)** | USA | SmartRange, SIT targets | Electrical/mechanical | $20-50K |
| **Action Target** | USA | AutoTargets, SmartRange SW | Electrical/mechanical | $15-40K |
| **INTARSO** | Poland | TrueScore10 | Optical (high-speed camera) | $5-15K |
| **ShotMarker** | USA | Acoustic target system | Acoustic (MEMS mics) | $500-1K (consumer) |

**None of these competitors offer AI-driven training analytics -- this is CORTEX RANGE's unique moat.**

## Appendix C: Key Sources

- Rheinmetall AG FY2024 Annual Report (March 2025)
- Rheinmetall AG H1 2025 Results (August 2025)
- Rheinmetall.com product pages: Simulation & Training, Army Training, LEGATUS, Gunnery & Combat, Tactical/Constructive
- Rheinmetall press releases: AGDUS (Dec 2021), GUZ Modernization (Nov 2025), VTAM Navy (Feb 2025), BISim (Jan 2025), Varjo (Nov 2025), Hologate (Dec 2024)
- Defense industry media: Army Technology, Defence Blog, EDR Magazine, SPARTANAT, Joint Forces News, Defence Industry Europe
- Market research: MarketsandMarkets Simulator Market, Fortune Business Insights, Visiongain Military Simulation Reports
- Analyst reports: CNBC (Mar 2025), Yahoo Finance earnings transcripts

---

## Summary Verdict

### Threat Level to CORTEX RANGE: LOW-MEDIUM (Indirect)

**Rheinmetall is the world's premier provider of instrumented tactical training systems (live simulation), but they DO NOT compete in live-fire range scoring or marksmanship analytics.**

| Threat Dimension | Level | Rationale |
|-----------------|-------|-----------|
| **Direct product competition** | NONE | Rheinmetall has no LOMAH, no acoustic scoring, no live-fire range products |
| **Market overlap** | LOW | Different training domains (tactical vs. marksmanship) |
| **Customer overlap** | MEDIUM | Same defense customers, but different budget lines and procurement offices |
| **Acquisition threat** | MEDIUM-HIGH | Rheinmetall could acquire a LOMAH company to fill their gap |
| **Partnership opportunity** | HIGH | CORTEX RANGE could complement LEGATUS for comprehensive training |
| **Technology threat** | LOW | Rheinmetall's AI/ML in training is years behind; hardware DNA limits pivot speed |
| **Pricing threat** | NONE | Rheinmetall's EUR 5M+ minimum vs. CORTEX $15K makes them non-competitive in CORTEX's segment |

**Bottom Line:** Rheinmetall is not the threat -- they are the opportunity. CORTEX RANGE fills a gap that Rheinmetall cannot address. The real competitors are Zen Technologies, Polytronic, InVeris, and Theissen Training Systems. Rheinmetall should be approached as a potential integration partner, not a competitor.

---

*Document version 1.0 | Created 2026-02-12 | CORTEX C2 RANGE Edition -- Competitive Intelligence*
