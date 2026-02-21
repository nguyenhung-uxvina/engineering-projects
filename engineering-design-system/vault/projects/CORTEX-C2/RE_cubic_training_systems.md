---
project: CORTEX-C2
phase: 0
type: reverse-engineering
subject: Cubic Corporation Training Systems & C2 (USA)
version: 1.0
created: 2026-02-12
status: complete
---

# RE Analysis: Cubic Corporation Training Systems & C2

## Executive Summary

Cubic Corporation is the **undisputed global leader in military live training systems**, having fielded over 250,000 systems across 33 countries and 25+ fixed/mobile combat training ranges. Acquired by Veritas Capital and Evergreen Coast Capital (Elliott Management affiliate) in May 2021 for ~$3.0B, Cubic is now privately held and headquartered in San Diego, CA. Their product portfolio spans air combat maneuvering instrumentation (ACMI), ground force-on-force laser engagement (MILES/I-MILES), area weapons effects simulation (AWES/ILT-A), exercise control and after-action review (CATS Metrix), and the emerging SPEAR common data model for AI/ML-ready training analytics. Understanding Cubic's architecture, strengths, and gaps is critical for positioning CORTEX C2 RANGE edition as a next-generation training analytics platform.

---

## 1. Company Profile

### 1.1 Corporate Overview

| Attribute | Detail |
|-----------|--------|
| **Full Name** | Cubic Corporation |
| **Founded** | 1951 by Walter J. Zable (San Diego, CA) |
| **Headquarters** | 9233 Balboa Ave, Kearny Mesa, San Diego, CA |
| **Ownership** | Private (Veritas Capital + Evergreen Coast Capital / Elliott Management) |
| **Acquisition Date** | May 25, 2021 |
| **Acquisition Value** | ~$3.0B ($75/share including debt assumption) |
| **Employees** | ~6,000-6,200 globally (1,500+ at San Diego HQ) |
| **Last Public Revenue** | ~$1.46B (FY2020, ending Sep 30, 2020) |
| **Estimated Current Rev** | ~$1.5-1.8B (private, not publicly disclosed) |
| **Key Competitors** | CAE, Saab, Rheinmetall, Thales, BAE Systems, L3Harris, Lockheed Martin |

### 1.2 Business Divisions (Post-2020 Restructuring)

In August 2020, Cubic consolidated from three segments to two:

| Division | Focus | Former Segments |
|----------|-------|-----------------|
| **Cubic Mission & Performance Solutions (CMPS)** | Training systems, C4ISR, secure comms, defense electronics | Cubic Global Defense (CGD) + Cubic Mission Solutions (CMS) |
| **Cubic Transportation Systems (CTS)** | Automated fare collection, transit payment systems | Unchanged |

CMPS is the defense-relevant division for this RE analysis. It provides:
- Live, virtual, and constructive (LVC) training systems
- Air combat training instrumentation (P5CTS/ACMI)
- Ground combat training (MILES, AWES, TESS)
- Secure communications (DTECH family)
- C4ISR and intelligence solutions
- Edge computing platforms

### 1.3 Key Subsidiaries and Entities

| Subsidiary | Location | Role |
|------------|----------|------|
| **Cubic Defense** | San Diego, CA | Primary defense business unit |
| **Cubic Defence Australia** | Townsville, QLD | Australian CTC support, Asia-Pacific ops |
| **Cubic Defence New Zealand** | Auckland, NZ | Manufacturing of training/simulation systems |
| **Cubic Technologies Singapore** | Singapore | Asia-Pacific training support |
| **Cubic Defence UK** | UK | AWES/ILT-A, British Army training |
| **DTECH Labs** | USA | Edge computing, secure comms products |
| **GATR Technologies** | USA | Portable SATCOM terminals |
| **TeraLogics** | Ashburn, VA | Full Motion Video PED |

### 1.4 Market Position

| Metric | Value |
|--------|-------|
| **Live Training Market Share** | Dominant (#1 globally for NATO live training) |
| **Air Combat Training** | "World's foremost provider" (self-described, validated) |
| **P5CTS Installed Base** | 2,000+ pods, 22 countries, 30+ ACMI ranges |
| **P5CTS Flight Hours** | 2,000,000+ cumulative |
| **Ground Training Installed Base** | 250,000+ systems, 33 countries |
| **CTC Support Duration** | JRTC since 2001 (138+ BCTs, 1M+ soldiers trained) |
| **Global Training Market** | $14.49B (2024), CAGR 4.35% to 2033 |

---

## 2. Live Training Products

### 2.1 MILES / I-MILES Family (Ground Force-on-Force)

The Multiple Integrated Laser Engagement System (MILES) is the **gold standard** for ground force-on-force live training worldwide.

#### 2.1.1 System Architecture

```
MILES Ecosystem
├── Soldier-Worn (Manworn)
│   ├── I-MILES IWS 2 (Individual Warfighter System)
│   │   ├── Small Arms Transmitter (SAT) — weapon-mounted laser
│   │   ├── Body-worn sensors (detect laser "hits")
│   │   ├── GPS receiver for position tracking
│   │   └── Radio link for real-time data
│   └── Casualty Assessment — real-time hit/kill determination
├── Vehicle Systems
│   ├── I-MILES TVS (Tactical Vehicle System)
│   │   ├── Wireless MILES technology
│   │   ├── Vehicle-mounted laser transmitter
│   │   ├── Vehicle sensors (detect hits)
│   │   └── Real-time casualty assessment
│   └── I-MILES CVTESS (Combat Vehicle TESS)
│       └── Heavy platform integration (Saab partnership)
├── Crew-Served Weapons
│   ├── Machine gun simulators
│   └── Anti-tank weapon simulators (RPG, AT-4)
└── Range Instrumentation Integration
    ├── GPS position tracking
    ├── Radio telemetry to EXCON
    └── AAR data recording
```

#### 2.1.2 I-MILES Product Variants

| Variant | Type | Key Features | Status |
|---------|------|--------------|--------|
| **I-MILES IWS 2** | Soldier-worn | Lightweight, quick-attach SAT, open standards, upgradeable | Current production |
| **I-MILES TVS** | Vehicle (HMMWV, tactical) | Wireless MILES, direct-fire simulation | Current production |
| **I-MILES CVTESS** | Combat vehicle | Heavy platform integration | Fielded (Saab-partnered) |
| **I-MILES VTESS** | Vehicle TESS next-gen | STE-LTS compatible | In development |
| **Mortar TESS** | 60mm/81mm mortar | Indirect fire simulation | Rapid fielding (2025) |

#### 2.1.3 How MILES Works

1. **Weapon fires blank ammunition** (live blank round triggers the laser)
2. **Small Arms Transmitter (SAT)** emits coded, eye-safe laser pulse
3. **Body/vehicle sensors** detect the laser hit
4. **Casualty assessment logic** determines hit/kill/near-miss
5. **GPS + radio** reports position and engagement data to EXCON in real-time
6. **Kill indicator** activates on the hit soldier/vehicle (audible/visual)
7. **All data recorded** for After Action Review playback

#### 2.1.4 Key Technical Parameters (Estimated)

| Parameter | Soldier-Worn (IWS 2) | Vehicle (TVS) |
|-----------|----------------------|---------------|
| Weight (total kit) | ~3-5 kg | Vehicle-integrated |
| Laser type | Eye-safe, coded | Eye-safe, coded |
| Effective range | Matches weapon type | Matches weapon type |
| GPS accuracy | ~5-10m (outdoor) | ~5-10m (outdoor) |
| Battery life | 12-24h operational | Vehicle power |
| Wireless link | Proprietary radio | Proprietary radio |
| Interoperability | Open standards, non-proprietary interfaces | Same |
| Indoor tracking | UWB add-on (SAFTI City) | N/A |

### 2.2 Area Weapons Effects Simulation (AWES) / ILT-A

AWES simulates **indirect fire** effects (artillery, mortar, mines, air-delivered munitions, CBRN) on instrumented soldiers and vehicles during force-on-force exercises.

| Attribute | AWES (Legacy) | ILT-A (Next-Gen, 2025) |
|-----------|---------------|------------------------|
| **Customer** | UK MoD (since 1998) | UK MoD (2025 contract) |
| **Coverage** | 150 sq mi Salisbury Plain | Multiple training areas |
| **Capacity** | 1,400 soldiers + 250 vehicles | Expandable |
| **Contract Value** | $35M (2017 extension), further extensions | $39.6M (2yr) + $130M (5yr option) |
| **Features** | GPS tracking, area effects, casualty assessment | Laser + area effects + live-fire ranges + RPAS + synthetic environment |
| **Integration** | Standalone TES system | SCOPIC2 Virtual-in-Live synthetic environment |
| **Multi-domain** | Ground focus | Multi-spectrum, multi-domain threats |
| **AAR** | Data-informed review | Digital AAR with full reconstruction |

#### AWES/ILT-A Effects Simulated
- Artillery fire (105mm, 155mm)
- Mortar fire (60mm, 81mm, 120mm)
- Mines and IEDs
- Air-delivered munitions
- CBRN weapons effects
- Direct fire (integrated with MILES/TES)

### 2.3 Shoot-Back Systems (SAFTI City, Singapore)

Cubic delivered an advanced shoot-back system to Singapore's SAFTI City (launched March 2025), the world's largest urban training facility.

| Component | Quantity | Technology |
|-----------|----------|------------|
| Building-integrated anchors | 8,000 | Ultra-wideband (UWB) indoor tracking |
| Shoot-through-wall modules | 3,000 | Sensor modules |
| Total sensors | 11,000 | Integrated system |
| Target detection | Computer vision | Automatic target detection & recognition |
| Shoot-back | Laser-based | Autonomous return fire simulation |

### 2.4 I-TESS II (Marine Corps)

| Attribute | Detail |
|-----------|--------|
| **Customer** | USMC |
| **Location** | MCB Quantico, VA |
| **Components** | RPG/AT-4 simulators, man-worn/vehicle laser detection, C2 systems |
| **Tracking** | GPS + radio (outdoor), UWB-capable (indoor MOUT) |
| **Integration** | LVC capable (live + virtual + constructive) |
| **Training** | Urban operations (MOUT), combined arms, small unit |

### 2.5 Position/Location Tracking Technology

| Environment | Technology | Accuracy | Notes |
|-------------|-----------|----------|-------|
| **Outdoor** | GPS (standard) | ~5-10m | All MILES/TESS variants |
| **Outdoor enhanced** | Differential GPS | ~1-3m | P5CTS (sub-meter for air) |
| **Indoor** | UWB (ultra-wideband) | ~0.3-1m | SAFTI City, 8,000 anchors |
| **Transition** | GPS + UWB handoff | Seamless | Outdoor-to-indoor continuity |
| **Air** | P5CTS GPS + IMU | Sub-meter | 3D position + attitude |

---

## 3. Air Combat Training Systems

### 3.1 P5 Combat Training System (P5CTS / ACMI)

The P5CTS is Cubic's **world-leading Air Combat Maneuvering Instrumentation (ACMI)** system.

| Attribute | Detail |
|-----------|--------|
| **System type** | ACMI pod (external) or Internal Subsystem (IS) for F-35 |
| **Function** | Real-time weapon simulation, high-fidelity instrumentation data links, onboard data recording |
| **Deployed** | 2,000+ pods, 22 countries, 30+ ACMI ranges |
| **Flight hours** | 2,000,000+ cumulative |
| **Security** | NSA-approved encrypted waveform (SSU upgrade) |
| **4th/5th Gen** | Full interoperability (F-16, F-15, F/A-18, F-35, etc.) |
| **Cost advantage** | <1/10th cost of competitors' secure ACMI (per Cubic) |
| **Data output** | Time, Space, Position Information (TSPI) — encrypted |

#### 3.1.1 P5CTS Variants

| Variant | Platform | Status |
|---------|----------|--------|
| **P5CTS Pod** | 4th gen fighters (external pod) | 2,000+ fielded |
| **P5 Internal Subsystem (IS)** | F-35 (internal integration) | 1,000+ delivered (as of Aug 2022) |
| **P5 SSU** | Security upgrade for 4th gen pods | First production order Sep 2024 |
| **P5 Block 7** | Engineering upgrade + SSU + 102 new pods | Contract Aug 2025 |

#### 3.1.2 Ground Instrumentation Subsystem

Supports ACMI with land/ship-based equipment for:
- Setup, monitor, control of air combat training missions
- Secure environment for debrief
- Integration with SPEAR for analytics

#### 3.1.3 Recent Operational Milestone: Cope North 2025

Cubic participated in Cope North 25 (Guam, Feb 2025) with:
- First-ever fully operational tracking of three F-35 partner nations
- Three variants of 4th gen fighters from three US services
- F-35 P5 IS + ACMI pods + ground stations + SPEAR
- Encrypted TSPI for live monitoring and post-mission review

### 3.2 Key Air Training Contracts (2022-2025)

| Contract | Value | Scope | Date |
|----------|-------|-------|------|
| P5CTS SSU program | Undisclosed | Encrypt 4th gen pod fleet for USAF | 2022 |
| Encrypted ACMI production | Undisclosed | First production order, 4th gen SSU kits | Sep 2024 |
| P5CTS Logistics Support | $399M (potential) | FMS to 9 countries through Jun 2032 | 2025 |
| P5 Block 7 + 102 new pods | Undisclosed | SSU + Block 7 upgrades, through Mar 2028 | Aug 2025 |
| First encrypted ACMI delivery | Delivered | 4th gen aircraft, USAF | May 2025 |

---

## 4. Training Management & After-Action Review

### 4.1 CATS Metrix (Exercise Control & AAR)

CATS Metrix is Cubic's **latest Exercise Control (EXCON) and After Action Review (AAR)** software platform.

#### 4.1.1 Capabilities

| Function | Description |
|----------|-------------|
| **Exercise Planning** | Scenario design, force ORBAT setup, objective definition |
| **Exercise Control** | Real-time monitoring, scenario injection, event triggers |
| **Live Tracking** | GPS-based player positions on electronic map, aerial photo, or 3D |
| **Performance Evaluation** | Goal/doctrine/tactic assessment against defined criteria |
| **Recording** | Full exercise recording for playback |
| **Debrief/AAR** | Visual replay, performance feedback, deficiency/excellence identification |
| **CBRN Integration** | Argon Electronics simulator integration |
| **Display Modes** | 2D map, aerial imagery, 3D terrain |

#### 4.1.2 Architecture (CATS Metrix)

```
CATS Metrix Architecture
├── Planning Module
│   ├── Scenario editor
│   ├── Force ORBAT builder
│   └── Objective/criteria definition
├── EXCON Module
│   ├── Real-time map display (2D/3D)
│   ├── GPS player tracking
│   ├── Event injection/triggers
│   ├── Casualty monitoring
│   └── Scenario control
├── AAR Module
│   ├── Exercise replay (time-synchronized)
│   ├── Performance scoring
│   ├── Deficiency identification
│   └── Report generation
├── Data Layer
│   ├── GPS telemetry ingestion
│   ├── MILES engagement data
│   ├── AWES/ILT-A effects data
│   └── Exercise recording database
└── Integration
    ├── I-MILES data feed
    ├── AWES/ILT-A data feed
    ├── CBRN simulator data
    └── SCOPIC2 virtual environment
```

### 4.2 SPEAR Common Data Model (Next-Generation)

SPEAR (Simplified, Planning, Execution, Analysis, Reconstruction) is Cubic's **emerging AI/ML-ready** analytics platform.

| Attribute | Detail |
|-----------|--------|
| **Type** | Common Data Model (CDM) software tool |
| **Tech Stack** | Modern, DoD-approved |
| **Domains** | Multi-domain training and operations |
| **Data Sources** | LVC (Live + Virtual + Constructive), kinetic + non-kinetic |
| **Analytics** | Kill chain events, mission rehearsal, live monitoring, debrief |
| **AI/ML Ready** | Lossless data export supports AI/ML algorithms |
| **Key Feature** | "Speed to insight" — rapid data visualization and analysis |
| **Deployment** | Cope North 2025 (operational validation) |
| **Training** | SPEAR Academy launched (with RCG Inc.) |

#### 4.2.1 SPEAR Functional Capabilities

| Phase | Capability |
|-------|------------|
| **Planning** | Mission rehearsal, scenario design |
| **Execution** | Live monitoring, real-time data visualization |
| **Analysis** | Post-mission performance analytics, readiness assessment |
| **Reconstruction** | Complete "when, how, what" reconstruction |
| **Insight** | "Why" analysis — allows debrief to focus on root causes |
| **Export** | Lossless LVC data export for AI/ML pipelines |

#### 4.2.2 SPEAR vs CATS Metrix

| Feature | CATS Metrix | SPEAR |
|---------|------------|-------|
| **Generation** | Current (mature) | Next-generation (emerging) |
| **Focus** | Ground EXCON/AAR | Multi-domain CDM |
| **Data Model** | Proprietary/structured | Common Data Model (open) |
| **AI/ML Support** | Not explicit | Explicitly designed for AI/ML |
| **Domain** | Ground training | Air + Ground + Multi-domain |
| **Analytics** | Performance scoring | Kill chain analysis, readiness |
| **Visualization** | 2D map / 3D terrain | Optimized displays, reduced cognitive load |
| **Interop** | I-MILES, AWES | LVC-wide, lossless export |

### 4.3 Advanced Training Environment (ATE)

ATE combines:
- **Instrumentation** — MILES/TESS sensor data
- **Synthetic Inject to Live (SITL)** — virtual threats injected into live exercises
- **SPEAR CDM** — unified data model
- **Purpose**: Emulate complex peer fight scenarios, assess proficiency, test TTPs

---

## 5. Range Systems & Instrumentation

### 5.1 Range Solutions Portfolio

Cubic Range Design Solutions (CRDS) designs, constructs, and maintains shooting ranges and training facilities.

| Category | Offerings |
|----------|-----------|
| **Gallery ranges** | Pistol, rifle, machine gun — baffled designs |
| **Open ranges** | Field firing, long range |
| **Targetry** | Pop-up, turning, moving targets |
| **Scoring** | Electronic hit detection and scoring |
| **Control** | Range control systems, communications |
| **Safety** | Sound absorption, HVAC/HEPA, safety baffles |
| **Specialized** | MOUT/urban training facilities |
| **Certification** | Exceeds local safety, noise, air quality regulations |

### 5.2 Combat Training Center (CTC) Instrumentation

Cubic provides the instrumentation backbone for the US Army's major CTCs:

| CTC | Location | Cubic Role | Duration |
|-----|----------|------------|----------|
| **JRTC** | Fort Johnson, LA | Full instrumentation, EXCON, AAR | Since 2001 |
| **NTC** | Fort Irwin, CA | Instrumentation support | Ongoing |
| **JPMRC** | Hohenfels, Germany | Instrumentation systems | Via LTRaC |
| **FMS CTC** | Multiple international | Modernization support | 2023+ |

#### JRTC Key Metrics
- 138+ brigade combat teams trained
- 1,000,000+ soldiers trained
- Contract history: $42M, $52M, $61M successive awards
- Continuous support since 2001

### 5.3 Instrumentation System (IS) Capabilities

The IS family provides:

| Capability | Description |
|------------|-------------|
| **Real-time tracking** | GPS-based location of all battlefield entities |
| **Recording** | Complete exercise recording for playback |
| **Control** | Remote control of all entities, scenario management |
| **AAR support** | Data feed to CATS Metrix / SPEAR for debrief |
| **Scalability** | Individual soldier to brigade-level exercises |
| **Integration** | I-MILES, AWES, CBRN, virtual inject |

### 5.4 Integration with LOMAH-Type Systems

Cubic does not appear to manufacture dedicated LOMAH (Location of Miss and Hit) acoustic scoring systems. Their range scoring relies primarily on:
- **Laser-based engagement detection** (MILES family)
- **Electronic targetry** with hit sensors
- **GPS-based position tracking** for movement scoring
- **CATS Metrix** for integrated scoring and AAR

This represents a **gap** — Cubic's ground training ecosystem does not include dedicated acoustic marksmanship scoring at the bullet-impact level. LOMAH-type acoustic scoring (as in VN-RNG-001) addresses a different training need: individual/crew weapon proficiency on live-fire ranges, vs. Cubic's focus on force-on-force tactical engagement.

---

## 6. AI & Analytics

### 6.1 Current AI/ML Posture

| Aspect | Status | Detail |
|--------|--------|--------|
| **SPEAR AI/ML readiness** | Emerging | Lossless data export designed to feed AI/ML algorithms |
| **Computer vision** | Fielded (SAFTI City) | Automatic target detection, recognition, tracking |
| **Predictive readiness** | Aspirational | SPEAR data supports readiness assessments |
| **Automated coaching** | Not announced | No evidence of AI-driven coaching/feedback |
| **Pattern recognition** | Not announced | No explicit ML-based training pattern detection |
| **Performance analytics** | SPEAR-based | Kill chain analysis, performance scoring |
| **Edge AI** | DTECH platform | Edge computing for data processing, AI inference |

### 6.2 AI/ML Gap Analysis

| Capability | Cubic Status | Industry State-of-Art |
|------------|-------------|----------------------|
| **AI-driven AAR** | Manual + data-assisted | Fully automated AAR generation is emerging |
| **Predictive training needs** | Not present | C3 AI PANDA-type predictive analytics exist |
| **Adaptive scenario generation** | Not present | AI-controlled adversaries in VR/simulators exist |
| **Automated performance scoring** | Rules-based | ML-based scoring with pattern recognition emerging |
| **Natural language debrief** | Not present | LLM-powered debrief summaries are feasible |
| **Training recommendation engine** | Not present | Data-driven recommendations for next-best training |
| **Cross-exercise trend analysis** | Limited | Longitudinal analysis across units/time periods |
| **Real-time coaching** | Not present | AI coaching in AR overlays emerging |

### 6.3 DTECH Edge Computing Platform

| Attribute | Detail |
|-----------|--------|
| **Family** | DTECH Family of Systems |
| **Function** | Edge-to-cloud connectivity, AI-driven decision-making |
| **Security** | Zero-trust, quantum-ready (DTECH Fusion Trust) |
| **Environment** | DDIL (Denied, Degraded, Intermittent, Limited) operations |
| **Training relevance** | Could enable edge AI for training analytics in austere environments |

### 6.4 STE-LTS Computer Vision Initiative

PEO STRI is investing in **computer vision technology as a potential replacement for MILES lasers**:
- Uses CV to detect weapon engagement instead of laser transmitters
- Expected procurement: FY2025
- Expected fielding: Starting FY2026 at JRTC, then NTC, then JPMRC
- This could fundamentally change the training instrumentation paradigm

---

## 7. Architecture & Integration

### 7.1 Software Architecture

| Layer | Technology | Notes |
|-------|-----------|-------|
| **Data Model** | SPEAR CDM (emerging), proprietary (legacy) | DoD-approved tech stack |
| **EXCON/AAR** | CATS Metrix (PC-compatible) | Client-server architecture |
| **Visualization** | 2D map, aerial imagery, 3D terrain | Desktop application |
| **Data Storage** | Local/networked | Exercise recording database |
| **Edge Compute** | DTECH platform | For operational C2, potentially training |
| **Cloud** | Not explicitly announced for training | Likely on-premise focused |

### 7.2 Simulation Standards Compliance

| Standard | Cubic Compliance | Application |
|----------|-----------------|-------------|
| **IEEE 1516 (HLA)** | Supported | LVC federation, virtual-constructive integration |
| **DIS** | Supported | Distributed interactive simulation for live training |
| **TENA** | Supported (via STE-LTS) | Test and training architecture for live assets |
| **STANAG 4603** | HLA-based | NATO interoperability |
| **Open standards** | I-MILES uses open, non-proprietary interfaces | Upgradability, interoperability |

### 7.3 LVC Integration Architecture

```
Cubic LVC Integration
├── LIVE
│   ├── I-MILES (soldiers, vehicles)
│   ├── AWES/ILT-A (area weapons)
│   ├── P5CTS ACMI (air combat)
│   └── GPS/UWB tracking
├── VIRTUAL
│   ├── SCOPIC2 (Synthetic Wrap / Virtual-in-Live)
│   ├── Reconfigurable Vehicle Simulator (RVS)
│   └── Virtual inject (SITL — Synthetic Inject to Live)
├── CONSTRUCTIVE
│   ├── JCATS integration (LLNL-managed)
│   ├── Threat simulation
│   └── Scenario generation
├── DATA
│   ├── SPEAR CDM (common data model)
│   ├── CATS Metrix (EXCON/AAR)
│   └── Lossless LVC data export
└── NETWORK
    ├── DIS / HLA / TENA gateways
    ├── DTECH edge nodes
    └── TAK integration (TAKTICS)
```

### 7.4 Integration with Operational C2

| System | Integration Level | Notes |
|--------|------------------|-------|
| **TAK (Tactical Assault Kit)** | TAKTICS product | Regional/Edge nodes, AutoSync Maps, DDIL-capable |
| **Mission Command** | Indirect fire integration | Call for fire, JTAC, fires missions |
| **BMS** | Exercise-level | EXCON monitoring |
| **SAPIENT** | Not announced | Gap for autonomous sensor integration |

---

## 8. Key Contracts & Deployments (2022-2026)

### 8.1 US Contracts

| Contract | Value | Customer | Scope | Year |
|----------|-------|----------|-------|------|
| **P5CTS SSU** | Undisclosed | USAF | Encrypt 4th gen ACMI pod fleet | 2022 |
| **CTC Modernization (FMS)** | Undisclosed | US Army PEO STRI | Modernize CTC for FMS customer | 2023 |
| **AWES Extension** | Undisclosed | UK MoD | Continue AWES support | 2023 |
| **Encrypted ACMI Production** | Undisclosed | USAF | First production SSU kits | Sep 2024 |
| **BEST MAC IDIQ** | 10-year | US Army PEO STRI | TESS engineering, manufacturing, lifecycle | Mar 2025 |
| **LTRaC MAC Lot 3** | $379M ceiling | US Army PEO STRI | 8-year, CTCs + ranges + STE-LTS + JPMRC-IS | Apr 2025 |
| **Mortar TESS Rapid Fielding** | Undisclosed | US Army PEO STRI | 60mm/81mm mortar TESS for NTC/JRTC | Aug 2025 |
| **P5 Block 7 + 102 Pods** | Undisclosed | USAF | SSU + Block 7 engineering upgrades | Aug 2025 |
| **P5CTS Logistics (FMS)** | $399M (potential) | USAF | Support for 9 FMS countries through 2032 | 2025 |

### 8.2 International Contracts

| Contract | Value | Customer | Scope | Year |
|----------|-------|----------|-------|------|
| **Australian CTC-LIS** | AUD $319.8M | Australian Army | 14-year CTC support (Townsville) | 2021 |
| **SAFTI City Shoot-Back** | Undisclosed | Singapore SAF | 11,000 sensors, CV, laser shoot-back | 2025 |
| **UK Light Gun Simulation** | Undisclosed | UK MoD | 2-year RSA Larkhill training | Feb 2024 |
| **UK ILT-A** | $39.6M (base) / $130M (full) | UK MoD | Next-gen AWES successor, 2+3 years | Jul 2025 |

### 8.3 FMS Countries (P5CTS)

Australia, Egypt, Kuwait, Morocco, Oman, Poland, Qatar, Saudi Arabia, Singapore (plus additional undisclosed customers for ground training systems in 33 countries total).

### 8.4 Installed Base Summary

| System | Installed Base | Geography |
|--------|---------------|-----------|
| **P5CTS Pods** | 2,000+ | 22 countries, 30+ ACMI ranges |
| **P5 F-35 IS** | 1,000+ | F-35 partner nations |
| **I-MILES (all variants)** | 250,000+ units | 33 countries |
| **AWES/ILT-A** | 1 major installation | UK (Salisbury Plain) + expanding |
| **CTC instrumentation** | 3+ major CTCs (US) + Australia + FMS | USA, Australia, international |

---

## 9. Business Model & Pricing

### 9.1 Revenue Model

```
Cubic Training Revenue Streams
├── HARDWARE SALES
│   ├── I-MILES kits (soldier-worn, vehicle)
│   ├── P5CTS pods and internal subsystems
│   ├── AWES/ILT-A equipment
│   ├── Range design and construction
│   └── Sensors, transmitters, receivers
├── SOFTWARE LICENSES
│   ├── CATS Metrix EXCON/AAR
│   ├── SPEAR CDM
│   └── SCOPIC2 synthetic environment
├── SERVICES (Recurring)
│   ├── CTC operational support (JRTC, NTC, Australia)
│   ├── O&M contracts (multi-year)
│   ├── Field service representatives (FSRs)
│   ├── Logistics support (P5CTS $399M IDIQ)
│   └── Training and academy (SPEAR Academy)
├── MODERNIZATION
│   ├── System upgrades (SSU, Block 7)
│   ├── Technology refresh
│   └── Engineering studies
└── FMS (Foreign Military Sales)
    ├── Government-to-government sales
    ├── Direct commercial sales
    └── In-country partnerships
```

### 9.2 Estimated Pricing (Based on Public Contract Data)

| Product/Service | Estimated Unit/System Cost | Basis |
|----------------|---------------------------|-------|
| **I-MILES IWS 2 (soldier kit)** | $3,000-8,000 per kit | $10M orders for "thousands" of units |
| **I-MILES TVS (vehicle kit)** | $15,000-40,000 per vehicle | $4.1M for ~100-250 vehicle sets |
| **P5CTS Pod (4th gen)** | $150,000-300,000 per pod | $399M for logistics on 2,000+ pods |
| **P5 F-35 IS** | $200,000-500,000 per unit | 1,000+ delivered, part of F-35 program |
| **CATS Metrix software** | $500K-2M per installation | Included in CTC contracts |
| **CTC annual support** | $10-15M per year | $61M over 4+1 years (JRTC) |
| **AWES/ILT-A system** | $30-130M total program | UK ILT-A contract range |
| **Range design/build** | $5-50M per range | Varies by complexity |

### 9.3 Contract Vehicles

| Vehicle | Type | Duration | Ceiling |
|---------|------|----------|---------|
| **BEST MAC** | Multi-award IDIQ | 10 years | Not disclosed |
| **LTRaC MAC Lot 3** | Multi-award IDIQ | 8 years (5+3) | $379M |
| **P5CTS Logistics** | FFP IDIQ | Through 2032 | $399M |
| **CTC Support** | Firm-fixed-price | 1+4 option years | $42-61M per cycle |

### 9.4 Lifecycle Support Model

Cubic operates a **long-term embedded support** model:
- Field Service Representatives (FSRs) at CTCs full-time
- 35+ Australian employees at CTC-LIS Townsville (most ADF veterans)
- Continuous technology refresh under IDIQ contracts
- Training academies (SPEAR Academy)
- Spare parts and logistics pipeline

---

## 10. Strengths & Weaknesses

### 10.1 Technical Strengths

| # | Strength | Evidence |
|---|----------|----------|
| 1 | **Dominant installed base** | 250,000+ ground systems, 2,000+ ACMI pods, 33 countries |
| 2 | **Decades of operational data** | JRTC since 2001 (1M+ soldiers), P5CTS 2M+ flight hours |
| 3 | **End-to-end LVC integration** | Live (MILES) + Virtual (SCOPIC) + Constructive (JCATS) |
| 4 | **Air combat training monopoly** | World's #1 ACMI provider, F-35 integration |
| 5 | **Multi-domain convergence** | SPEAR CDM integrates air + ground training data |
| 6 | **Encryption leadership** | First encrypted ACMI for 4th-5th gen interop |
| 7 | **Long-term customer relationships** | 20+ years UK MoD, 20+ years JRTC, 18+ years Australia |
| 8 | **Indoor tracking innovation** | UWB at SAFTI City (11,000 sensors) |
| 9 | **Computer vision investment** | SAFTI City shoot-back, PEO STRI CV for MILES replacement |
| 10 | **Global subsidiary network** | Australia, NZ, Singapore, UK — local expertise |

### 10.2 Weaknesses & Limitations

| # | Weakness | Analysis |
|---|----------|----------|
| 1 | **Legacy technology debt** | MILES architecture dates to 1970s-80s; GPS tracking limited to ~5-10m accuracy; laser engagement requires line-of-sight |
| 2 | **Minimal AI/ML in training analytics** | SPEAR is AI/ML-"ready" but no announced deployed AI; rules-based scoring only; no predictive readiness, no automated coaching |
| 3 | **No acoustic scoring capability** | No LOMAH or bullet-tracking system; cannot assess marksmanship accuracy at the shot level on live-fire ranges |
| 4 | **Closed/proprietary data ecosystems** | Despite "open standards" claims, CATS Metrix and legacy systems use proprietary data formats; limited API access |
| 5 | **Post-acquisition talent erosion** | Employee reviews cite toxic culture post-Veritas acquisition; "lost most prospects after being purchased by VC firm"; unqualified management |
| 6 | **No real-time AI coaching** | All analysis is post-exercise or post-mission; no in-exercise AI-driven feedback to trainees |
| 7 | **High cost and complexity** | Full CTC instrumentation costs $10-15M/year to operate; MILES kits at $3-8K per soldier; prohibitive for smaller militaries |
| 8 | **Slow modernization pace** | MILES replacement (STE-LTS with CV) not expected until FY2026-2027; decades between major technology refreshes |
| 9 | **Limited cloud-native architecture** | Training systems appear on-premise; no announced cloud-native analytics dashboard or SaaS model |
| 10 | **No multi-weapon scoring integration** | MILES handles force-on-force laser engagement; no integration with acoustic scoring, optical scoring, or real ballistic tracking |
| 11 | **Ground-to-air AAR gap** | CATS Metrix (ground) and P5CTS debrief (air) are separate systems; SPEAR is emerging but not yet unified |
| 12 | **PE ownership risk** | Veritas Capital focus on financial returns may limit R&D investment; talent flight documented in reviews |

### 10.3 Customer Dissatisfaction Signals

| Source | Signal |
|--------|--------|
| Employee reviews (Indeed/Glassdoor) | "Cubic used to be a respected developer of training systems, but through bad management and poor business development has lost most of its prospects after being purchased by a VC firm" |
| Employee reviews | "Completely unqualified managers and senior leaders with unshakable confidence" |
| US Army modernization | Army investing in computer vision to **replace** MILES laser technology — implicit dissatisfaction with current approach |
| I-MILES replacement timeline | BEST MAC is a "bridge" contract — Army actively seeking next-gen replacement |
| STE-LTS program | Explicit program to modernize away from current MILES paradigm |
| GAO protest | Cubic Simulation Systems GAO protest (B-410006) indicates competitive tensions |

---

## 11. Design Paradigm Comparison: Cubic vs CORTEX C2 RANGE

### 11.1 Architectural Comparison

| Dimension | Cubic (Current) | CORTEX C2 RANGE (Target) |
|-----------|----------------|--------------------------|
| **Core paradigm** | Hardware-centric instrumentation + post-exercise AAR | AI-first analytics platform with multi-sensor fusion |
| **Data model** | Proprietary (CATS Metrix) + emerging CDM (SPEAR) | Open, API-first, cloud-native from day one |
| **AI integration** | "AI-ready" data export; no deployed AI | AI-native: ML scoring, predictive readiness, automated coaching |
| **Real-time analysis** | Real-time tracking display; analysis is post-exercise | Real-time performance scoring + AI coaching during exercise |
| **Scoring** | Laser engagement (force-on-force only) | Multi-modal: acoustic (LOMAH), optical, laser, video, AI |
| **Marksmanship** | Not addressed (no shot-level accuracy) | Core capability: individual shot scoring, grouping analysis |
| **Cost** | $3-8K per soldier kit; $10-15M/yr CTC ops | Target: 10-50x lower cost through software-centric approach |
| **Deployment** | Weeks-months for CTC setup; permanent installations | Hours-days; portable, self-configuring |
| **Cloud** | On-premise, no cloud analytics | Cloud-native dashboard, edge-to-cloud pipeline |
| **Multi-weapon** | MILES per weapon type; separate P5CTS for air | Unified platform: rifle, pistol, MG, mortar, AT, air defense |

### 11.2 Training Analytics Comparison

| Capability | Cubic | CORTEX RANGE |
|------------|-------|--------------|
| **Shot-level accuracy** | Not available | Core feature (LOMAH acoustic) |
| **Engagement reconstruction** | Yes (CATS Metrix replay) | Yes + AI-annotated with tactical assessment |
| **Performance trending** | Manual comparison across exercises | Automated ML trend detection across time |
| **Unit readiness scoring** | Manual assessment | Automated readiness algorithm (predictive) |
| **Individual proficiency** | Not tracked at individual level | Individual shooter profile + improvement tracking |
| **Training recommendations** | Instructor-driven | AI-generated next-best training recommendation |
| **Cross-unit benchmarking** | Limited (same CTC only) | Multi-unit, multi-range, longitudinal comparison |
| **Report generation** | Manual from CATS Metrix data | Automated report generation (NLP summaries) |
| **Data export/API** | Limited, proprietary formats | Open API, standard formats (JSON, CSV, STANAG) |
| **Cost per data point** | High (hardware + FSRs + infrastructure) | Low (software + existing sensors) |

### 11.3 Exploitable Gaps for CORTEX RANGE

| Gap # | Cubic Gap | CORTEX RANGE Opportunity |
|-------|-----------|--------------------------|
| **G1** | No acoustic/LOMAH scoring | Build LOMAH-based marksmanship scoring as core differentiation |
| **G2** | No AI-driven analytics | AI-native platform: predictive readiness, automated coaching |
| **G3** | No real-time coaching | Real-time AI feedback during live-fire and force-on-force |
| **G4** | Proprietary data | Open API, cloud-native, interoperable data platform |
| **G5** | Extremely high cost | 10-50x cost reduction through software-centric + local manufacturing |
| **G6** | No cloud dashboard | Web-based commander dashboard, mobile AAR |
| **G7** | No individual proficiency tracking | Individual shooter profiles with ML trend analysis |
| **G8** | Slow deployment | Rapid deployment: hours not weeks |
| **G9** | Ground-air AAR separation | Unified multi-domain analytics from day one |
| **G10** | No cross-exercise ML trends | Longitudinal ML analysis across exercises, units, time |
| **G11** | No NLP report generation | LLM-powered automated debrief and report generation |
| **G12** | No integration with acoustic scoring | Native LOMAH + force-on-force data fusion |

### 11.4 Where Cubic Remains Superior (Respect Points)

| # | Cubic Advantage | CORTEX RANGE Response |
|---|----------------|----------------------|
| 1 | Massive installed base (250K+ systems) | Cannot compete head-on; target underserved markets first |
| 2 | F-35 / ACMI integration | Not in scope for RANGE edition |
| 3 | CTC-level exercise control | Focus on range/company level first, scale up |
| 4 | NATO standardization | Adopt HLA/DIS/TENA from the start for interop |
| 5 | Decades of engagement data | Build data advantage through AI analytics on smaller datasets |
| 6 | Government procurement relationships | Partner with local integrators; use FMS-friendly pricing |
| 7 | UWB indoor tracking (SAFTI City) | Not in initial scope; address via partnerships |
| 8 | LVC integration maturity | Focus on Live first; add V+C integration later |

### 11.5 CORTEX RANGE Competitive Strategy

```
Cubic Dominance Zone (Avoid)          CORTEX RANGE Attack Zone
┌─────────────────────────────┐      ┌──────────────────────────────────┐
│ ■ CTC-scale exercises       │      │ ■ Live-fire range analytics      │
│ ■ Air combat ACMI           │      │ ■ Marksmanship scoring (LOMAH)   │
│ ■ Major NATO exercises      │      │ ■ AI-driven performance tracking │
│ ■ F-35 integration          │      │ ■ Real-time coaching             │
│ ■ US Army prime contracts   │      │ ■ Small/medium military markets  │
│                             │      │ ■ Cost-accessible training       │
│ Cubic advantage: 10x       │      │ ■ Cloud-native analytics         │
│                             │      │ ■ Rapid deployment               │
│                             │      │ ■ Multi-weapon integration       │
│                             │      │                                  │
│                             │      │ CORTEX advantage: 10x            │
└─────────────────────────────┘      └──────────────────────────────────┘
```

---

## 12. Strategic Summary

### 12.1 Key Findings

1. **Cubic is the undisputed king of military live training hardware** — 250,000+ ground systems, 2,000+ ACMI pods, 33 countries, decades of dominance. Competing head-on in CTC-scale force-on-force instrumentation would be futile.

2. **Their AI/ML capability is nascent** — SPEAR CDM is "AI-ready" but no deployed AI exists. Their analytics remain rules-based and post-exercise. This is the #1 strategic gap.

3. **No acoustic/LOMAH scoring** — Cubic does not address individual marksmanship scoring at the shot level. Their ecosystem is force-on-force engagement, not live-fire proficiency. This is the #2 strategic gap.

4. **Cost structure is prohibitive** — $3-8K per soldier kit, $10-15M/year CTC operations. This locks out smaller militaries and limits training frequency for larger ones.

5. **Post-acquisition culture decline** — Employee reviews consistently cite management problems, talent flight, and loss of innovation post-Veritas acquisition.

6. **STE-LTS modernization is slow** — The Army is actively seeking MILES replacement (computer vision), but fielding isn't expected until FY2026-2027. This creates a modernization window.

7. **SPEAR is the watch item** — If Cubic successfully deploys SPEAR with real AI/ML analytics, it could close the analytics gap. Current evidence suggests they are 2-3 years from meaningful AI deployment.

### 12.2 CORTEX C2 RANGE Positioning

```
Market Position Matrix
                        Low Analytics ────────────── High Analytics
                        │                                          │
High Cost ──────────────┤  ■ Cubic (current)                       │
                        │                                          │
                        │           ■ Cubic + SPEAR (2027?)        │
                        │                                          │
                        │                                          │
                        │                      ■ CORTEX RANGE      │
Low Cost ───────────────┤              (target position)           │
                        │                                          │
                        └──────────────────────────────────────────┘
```

**CORTEX C2 RANGE should position as:**
- High analytics / low cost quadrant
- AI-native from day one (not retrofitted)
- Acoustic scoring (LOMAH) + force-on-force fusion
- Cloud-native, API-first architecture
- Target: markets Cubic cannot serve cost-effectively

### 12.3 Timeline & Risk Assessment

| Factor | Assessment |
|--------|------------|
| **Cubic SPEAR maturity** | 2-3 years to meaningful AI deployment; current focus on data model, not AI |
| **STE-LTS replacement** | FY2026-2027 fielding; creates procurement uncertainty |
| **Market window** | 2026-2028 is optimal window before Cubic/competitors deploy AI |
| **Entry strategy** | Start with LOMAH-based range analytics (VN-RNG-001 technology) |
| **Scale-up path** | Range analytics -> company-level AAR -> battalion-level -> CTC integration |

---

## References & Sources

| # | Source | URL |
|---|--------|-----|
| 1 | Cubic Corporation Wikipedia | https://en.wikipedia.org/wiki/Cubic_Corporation |
| 2 | Cubic Training Solutions | https://www.cubic.com/industries/training |
| 3 | CATS Metrix EXCON/AAR | https://www.cubic.com/solutions/training/ground/excon-aar-analysis |
| 4 | Cubic ACMI Systems | https://www.cubic.com/industries/training/air-combat/acmi |
| 5 | Cubic Manworn Systems | https://www.cubic.com/solutions/training/ground/tactical-engagement-systems/manworn-systems |
| 6 | I-MILES Wikipedia | https://en.wikipedia.org/wiki/Multiple_integrated_laser_engagement_system |
| 7 | Veritas Acquisition Completion | https://www.businesswire.com/news/home/20210525005655/en/ |
| 8 | Cubic LTRaC IDIQ Award | https://www.accessnewswire.com/newsroom/en/aerospace-and-defense/cubic-awarded-the-live-training-ranges-and-combat-training-centers-ltrac-inde-1013491 |
| 9 | Cubic BEST MAC Award | https://www.newswire.com/news/cubic-awarded-bridge-to-enduring-synthetic-training-environment-ste-22544500 |
| 10 | P5CTS Logistics $399M | https://www.govconwire.com/articles/cubic-p5-combat-training-system-contract-award-air-force-fms |
| 11 | Cubic UK ILT-A Contract | https://www.newswire.com/news/cubic-awarded-uk-integrated-live-training-area-weapons-effects-system-ilt-a |
| 12 | SAFTI City Shoot-Back | https://www.newswire.com/news/cubic-delivers-cutting-edge-shoot-back-system-to-singapore-armed-22568944 |
| 13 | Australian CTC $319M | https://www.businesswire.com/news/home/20211214005868/en/ |
| 14 | Cubic Cope North 2025 | https://soldiersystems.net/2025/03/18/cubic-participates-in-cope-north-25-multi-domain-exercise/ |
| 15 | I/ITSEC 2024 SPEAR Showcase | https://www.newswire.com/news/cubic-defense-to-showcase-advanced-live-virtual-and-constructive-lvc-22469710 |
| 16 | Cubic AUSA 2025 | https://www.newswire.com/news/cubic-defense-to-showcase-edge-computing-secure-communications-digital |
| 17 | SPEAR Academy Launch | https://www.newswire.com/news/cubic-announces-the-inaugural-simplified-planning-execution-analysis-22553991 |
| 18 | Encrypted ACMI Delivery | https://www.asdnews.com/news/defense/2025/05/21/cubic-delivers-firstever-encrypted-air-combat-maneuvering-instrumentation-acmi-4th-gen-aircraft-usaf |
| 19 | P5 Block 7 + 102 Pods | https://www.newswire.com/news/cubic-awarded-contract-from-the-united-states-air-force-usaf-for-102-new-p5 |
| 20 | Mortar TESS Rapid Fielding | https://www.asdnews.com/news/defense/2025/08/18/cubic-awarded-us-army-peo-stri-ste-lts-mortars-rapid-fielding-contract |
| 21 | Army MILES Replacement | https://www.military.com/daily-news/2021/03/18/army-wants-finally-replace-decades-old-miles-gear-more-realistic-force-force-training.html |
| 22 | Cubic Employee Reviews | https://www.indeed.com/cmp/Cubic-Corporation/reviews |
| 23 | Cubic AWES UK Contract | https://www.businesswire.com/news/home/20230418005045/en/ |
| 24 | Cubic Singapore Airshow 2026 | https://www.newswire.com/news/cubic-defense-to-showcase-proven-air-and-ground-training-solutions-for-7445708 |
| 25 | JRTC $61M Contract | https://www.prnewswire.com/news-releases/cubic-awarded-61-million-contract-to-continue-support-of-us-armys-joint-readiness-training-center-300563391.html |

---

*Analysis completed 2026-02-12. This RE document supports CORTEX C2 Phase 0 (ODI) competitive landscape analysis for the RANGE edition.*
