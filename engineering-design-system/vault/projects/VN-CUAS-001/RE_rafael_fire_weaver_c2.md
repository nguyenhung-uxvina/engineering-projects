---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Rafael Advanced Defense Systems - FIRE WEAVER & C2/Networked Warfare Products (Israel)
version: 1.0
created: 2026-02-12
status: complete
---

# RE: Rafael FIRE WEAVER & C2/Networked Warfare Ecosystem - Israel
## Reverse Engineering Analysis from Public Sources

> **SCOPE:** This analysis covers Rafael's FIRE WEAVER sensor-to-shooter system, DRONE DOME C-UAS, BNET SDR communications, and the broader C2 ecosystem (Iron Dome / C-DOME / Iron Beam). While FIRE WEAVER is a fire control/sensor-to-effector C2 system (not a passive acoustic detector), its AI-driven target allocation, IFF/deconfliction, and open architecture represent the **state-of-the-art in network-centric warfare C2** directly relevant to VN-CUAS-001's command, control, and integration layer.

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Rafael Advanced Defense Systems Ltd. (Hebrew: rafa'el maarakhot lekhima mitqadmot) |
| **HQ** | P.O. Box 2250, Haifa 3102102, Israel |
| **Phone** | +972-73-335-4444 |
| **Website** | www.rafael.co.il |
| **Founded** | 1948 (as Israel's National R&D Defense Laboratory) |
| **Incorporated** | 2002 (converted from MoD lab to government-owned business corporation) |
| **Ownership** | 100% Israeli Government (Ministry of Defense) |
| **Employees** | ~8,500 (2024); largest employer in Northern Israel |
| **Revenue (FY2024)** | $4.8 billion (27% increase from $3.8B in FY2023) |
| **Net Profit (FY2024)** | $257 million (64% increase from FY2023) |
| **New Orders (FY2024)** | $8.23 billion |
| **Order Backlog** | $17.76 billion (record; 24% increase YoY) |
| **R&D Investment** | ~7% of sales |
| **International Sales** | ~50% of total revenue (FY2024) |
| **Valuation (est.)** | ~$10 billion (2025, pre-privatization discussions) |
| **S&P Rating** | Investment grade |
| **Subsidiaries** | Rafael Systems Global Sustainment (RSGS, USA); Rafael UK; Astra Rafael Comsys (India JV); mPrest (50% owned); numerous others |

### Key Leadership

| Name | Role |
|------|------|
| **Dr. Yuval Steinitz** | Chairman of the Board |
| **Yoav Tourgeman** | President & CEO |
| **Yoav Wermuth** | VP & Head, C3I Directorate |
| **Lt Gen (Ret) Joe Anderson** | Team Lead, RSGS (US subsidiary) |

### Market Position

Rafael is Israel's **second-largest state-owned defense company** (after IAI, $6.1B revenue) and **third-largest overall** (after Elbit Systems, $6.8B). Together with IAI and the now-merged IMI Systems, Rafael accounts for >70% of Israel's defense production.

### Revenue Growth Trajectory

| Year | Revenue | Backlog | Net Profit |
|------|---------|---------|------------|
| 2011 | $1.98B | $3.5B | $111M |
| 2016 | ~$2.5B | — | $123M |
| 2021 | $3.1B | $7.1B | $133M |
| 2023 | $3.8B | $14.3B | $157M |
| **2024** | **$4.8B** | **$17.76B** | **$257M** |

### Divisions / Product Domains

| Domain | Key Products |
|--------|-------------|
| **Air & Missile Defense** | Iron Dome, David's Sling (Stunner interceptor), Iron Beam (HEL), C-DOME (naval) |
| **Precision-Guided Munitions** | SPICE (250/1000/2000), SPIKE missile family (SR, MR, LR, ER, NLOS, Firefly) |
| **C3I / Networked Warfare** | FIRE WEAVER, BNET SDR, mPrest BMC, IMILITE (IMINT AI) |
| **Active Protection** | Trophy APS (tanks), Windbreaker |
| **C-UAS** | DRONE DOME, Iron Dome (dual-use), Lite Beam (10 kW laser) |
| **RCWS** | SAMSON family (7.62mm to 30mm), Typhoon naval RCWS |
| **Naval** | C-DOME, Typhoon, naval SPIKE |
| **Directed Energy** | Iron Beam (100 kW class), Lite Beam (10 kW), DRONE DOME laser |
| **Cyber & Intelligence** | IMILITE (IMINT/GEOINT AI), cyber defense systems |

### Privatization

Israel announced plans (2024-2025) to partially privatize Rafael and IAI via public share offerings. With an $18B backlog, Rafael's estimated valuation is ~$10 billion. This remains subject to national security review.

---

## 2. FIRE WEAVER - NETWORKED SENSOR-TO-SHOOTER SYSTEM

### 2.1 System Overview

| Attribute | Detail |
|-----------|--------|
| **Full Name** | FIRE WEAVER Networked Sensor-to-Shooter System |
| **IDF Service Name** | "Smart Trigger" (Hedek Khakham) |
| **Category** | Multi-domain networked fire control / battle management overlay |
| **Developer** | Rafael, jointly with IDF Ground Forces Command and DDR&D (MAFAT) |
| **First Shown** | Eurosatory 2018 |
| **IDF Contract** | February 2020 (Israeli MoD acquisition) |
| **Operational Target** | First brigade operational by 2022 |
| **Combat Use** | Confirmed used by IDF in Gaza (2023-2024 conflict) |
| **Architecture** | Open, modular software application |

### 2.2 Core Concept

FIRE WEAVER is fundamentally a **software layer** that sits between networked sensors, C2 systems, and effectors. It creates a real-time **"fires exchange"** -- an operational marketplace where:

1. Units in contact with the enemy **"publish a tender"** (call for fire) specifying exact target location
2. Fire elements submit **"bids"** based on their readiness, position, ammunition, effectiveness
3. The AI engine selects the **optimal shooter** based on multiple parameters
4. Target information is transferred using **Geo-Pixel spatial language** (3D, GPS-independent)
5. The engagement is completed in **seconds rather than minutes**

This is described as an **"operational internet"** that brings to the battlefield what the internet brought to civilian commerce.

### 2.3 Key Technical Architecture

#### Geo-Pixel Common Visual Language (Core Innovation)

| Feature | Detail |
|---------|--------|
| **Technology** | GPS-independent geo-pixel-based 3D spatial referencing |
| **Function** | Creates a common visual language for ALL sensors and shooters |
| **How it Works** | Designates a location on a 3D model; uses computer vision to present that location viewed from different angles |
| **Target Transfer** | Transfers target geo-pixel + metadata (NOT images/video/speech) |
| **Bandwidth** | LOW -- only geo-pixel coordinates and metadata, much less than video-based systems |
| **Presentation** | Augmented reality overlay on weapon sights, binoculars, BMSs |
| **GPS Denied** | Fully functional without GPS |

The Geo-Pixel system means each shooter sees the same target from **their specific line of sight**, even though targets were designated from a different vantage point.

#### AI / Machine Learning Engine

| Capability | Detail |
|------------|--------|
| **Target Allocation** | AI algorithms continuously calculate optimal shooter for each target |
| **Parameters Considered** | Location, line-of-sight, weapon effectiveness, ammunition status, time to engage, cost per engagement |
| **Collateral Damage** | Minimization algorithms factor in proximity of friendly forces, civilians, sensitive locations |
| **Fratricide Prevention** | Real-time IFF, blue force tracking, keep-out zones, safety limits |
| **Rules of Engagement** | Automatically processes ROE, legal constraints, time windows |
| **Multiple Simultaneous Loops** | Handles multiple sensor-to-shooter loops in parallel |
| **Fire Prioritization** | Automated priority assignment based on threat severity |
| **Decision Aid** | Suggests fire solutions; commander can approve, decline, or reprogram at any time |
| **Learning** | Leverages AI from SPICE program (scene-matching algorithms) |

#### Fire Management Terminal (FMT)

| Feature | Detail |
|---------|--------|
| **Purpose** | Commander control station for the entire Fire Weaver system |
| **Control Level** | Sets level of autonomous behavior |
| **Safety Zones** | Define keep-out areas, exclusion zones |
| **Time Windows** | Set operational time limits for engagements |
| **Override** | Commander can approve, decline, or reprogram any fire solution at any time |
| **Multiple Loops** | Manages cases of multiple sensor-to-shooter loops in parallel |
| **Human in the Loop** | ALWAYS -- lethal decisions require human approval |

#### System Architecture

| Layer | Detail |
|-------|--------|
| **Integration** | Software application layer overlaying existing C4I systems |
| **Complementary** | Works WITH (not replaces) existing BMSs (e.g., IDF's Elbit Digital Army Program / TORC2H) |
| **Edge Elements** | Embedded in binoculars, target acquisition devices, weapon sights |
| **Open Architecture** | Integrates with various BMSs, radios, sensors, weapon systems |
| **Level** | Battalion level and below (combat echelon), vs. C4I systems that serve HQ/command level |
| **Safety Standard** | MIL-STD 882 compliant |
| **3D Terrain** | Uses high-resolution 3D terrain data for LoS calculations |

### 2.4 Sensors and Weapons Integrated

#### Sensors Connected to Fire Weaver

| Sensor Type | Examples |
|-------------|---------|
| **Target Locators** | Safran MOSKITO TI (MoU 2021, full agreement 2022); all Safran target locators (integration ongoing) |
| **UAVs** | Aeronautics Pegasus drone; Orbiter 3 UAV |
| **EO/IR Systems** | Various electro-optical and thermal imaging systems |
| **Binoculars** | Embedded edge elements in observation devices |
| **Radar** | Can receive feeds from ground surveillance radars |
| **Trophy APS** | Rafael planning Trophy-to-Fire Weaver link (trophy detects launch, Fire Weaver coordinates response) |
| **IMILITE** | Rafael's AI-based IMINT/GEOINT intelligence system (Oracle Cloud integration) |

#### Effectors / Weapons Connected

| Weapon Type | Examples |
|-------------|---------|
| **ATGM** | SPIKE SR (shoulder-fired precision strike); SPIKE NLOS (6th gen) |
| **Loitering Munitions** | SPIKE Firefly (miniature LM) |
| **RCWS** | SAMSON 30mm integrated RWS; SAMSON family |
| **Mortars** | Mortar fire control integration |
| **Tanks / AFV** | Merkava (via Trophy APS linkage); Carmel program concept demonstrator |
| **Attack Helicopters** | Apache AH-64E (shown in integration concepts) |
| **Artillery** | Fire support element integration |
| **Naval Weapons** | Potential integration (open architecture supports) |

#### Spike NMT (NLOS Mission Taskforce) -- Integrated Package

| Component | Detail |
|-----------|--------|
| **Concept** | All-in-one sensor-to-shooter package |
| **ISR** | UAV platforms (Orbiter 3) for detection and reconnaissance |
| **Effector** | Ground launch platform with multiple SPIKE NLOS missiles |
| **Networking** | BNET SDR radios |
| **C2** | Fire Weaver sensor-to-shooter system |
| **Platform** | 4x4 or armored vehicles |
| **Customer** | Hellenic Army (Greece) -- NMT deal confirmed (DEFEA 2023) |
| **Capability** | Organic detection, attack, and fire control for small mobile units |

### 2.5 Deployment Model

| Configuration | Detail |
|---------------|--------|
| **Vehicle-Mounted** | Armored vehicles, 4x4 tactical vehicles, Carmel demonstrator |
| **Dismounted** | Infantry units with handheld devices, binoculars, weapon sights |
| **Command Post** | Fire Management Terminal at battalion/brigade HQ |
| **UAV Integration** | Drone-to-ground via BNET data link |
| **Scalability** | Brigade-level deployment; designed for all IDF ground divisions |

### 2.6 Demonstrations and Trials

| Date | Customer | Event | Detail |
|------|----------|-------|--------|
| 2018 | IDF | Battalion exercise | First live demo at battalion level |
| Dec 2019 | Germany (BAAINBw) | Transparent Battlefield Phase 1 | Selected for "Glass Battlefield" (ErzUntGlas) study |
| Feb 2020 | IDF | Contract award | Acquired for IDF ground force divisions |
| Nov 2020 | Germany (Bundeswehr) | Transparent Battlefield Phase 2 | Demo at Paderborn with BNET + Pegasus drone; Dutch forces present |
| Jan 2021 | US Army | AEWE 21, Fort Benning | Operational assessment; soldiers trained in half a day |
| 2021 | Netherlands | Demonstration | Dutch SOF and Marine Corps |
| 2021-2022 | Asia (unnamed) | Demonstrations | Multiple nations in Asia |
| Jan 2022 | US Army | AEWE 22 | Follow-on demonstrations |
| 2022 | US Army | MFIX + Project Convergence 22 | Maneuver Fires Integration Experiment |
| 2023-2024 | IDF | Gaza operations | Combat use confirmed (Jerusalem Post) |

### 2.7 Partners and MoUs

| Partner | Nature | Date |
|---------|--------|------|
| **Atos GmbH** | Germany -- Transparent Battlefield study integration | 2019 |
| **Safran Vectronix** | MoU for MOSKITO TI integration; full agreement 2022 | 2021/2022 |
| **Oracle** | Cloud-based AI (FIRE WEAVER + IMILITE on OCI) | Sep 2024 |
| **Lockheed Martin** | SPICE marketing; broader US defense collaboration | 2019+ |
| **Aeronautics** | Orbiter 3 UAV + SPIKE NLOS + Fire Weaver (Greece NMT) | 2023 |

---

## 3. BNET -- BROADBAND TACTICAL MANET SDR

### 3.1 System Overview

| Attribute | Detail |
|-----------|--------|
| **Full Name** | BNET Broadband IP Software Defined Radio |
| **Category** | Tactical IP MANET (Mobile Ad-hoc Network) SDR |
| **Standard** | SCA 2.2.2 compliant |
| **Core Technology** | Multi-Channel Reception (MCR) -- patented |
| **Key Feature** | Ultra-high capacity, low delay, high scalability |
| **Scalability** | 1,000+ users in single network |
| **Domains** | Land, sea, and air units on single seamless network |
| **ECCM** | Electronic counter-countermeasures capability |
| **Non-GPS** | Operates in GPS-denied environments |

### 3.2 BNET Family Variants

| Variant | Form Factor | Application |
|---------|-------------|-------------|
| **BNET-HH** | Handheld | Dismounted soldier; modular multiband SDR |
| **BNET-MP** | Man-pack | Dismounted with higher power |
| **BNET-V** | Vehicular | Armored and tactical vehicles |
| **BNET-AR** | Airborne | Fixed-wing and rotary-wing aircraft |
| **BNET Nano** | Ultra-lightweight | UAS, small platforms |

### 3.3 Capabilities

| Feature | Detail |
|---------|--------|
| **Data** | High-speed broadband data transfer |
| **Video** | Live video streaming on the move |
| **Voice** | Secure voice communications |
| **Network** | Single flat MANET connecting all domain users |
| **Spectrum** | Cognitive spectrum management; optimized utilization |
| **Waveform** | Multi-channel reception MANET waveform |
| **Architecture** | F/TDMA; 80+ nodes, 80 time slots per channel |
| **Multi-Band** | Supports multiple frequency bands |
| **IP Protocol** | Native IP routing |

### 3.4 BNET + Fire Weaver Integration

BNET serves as the **data transport layer** for Fire Weaver. The combination provides:
- Live traffic from UAVs carried over BNET to Fire Weaver
- Common visual language distributed across entire network
- Single "flat" network connecting sensors and shooters across domains
- Demonstrated together for German Bundeswehr (Transparent Battlefield study)

### 3.5 International Customers

| Customer | Variant | Status |
|----------|---------|--------|
| **IDF** | All variants | In service |
| **Germany (Bundeswehr)** | Vehicle + Handheld | Evaluated (Transparent Battlefield) |
| **India** | BNET-MANAS V/UHF | User trials completed (Astra Rafael Comsys JV, 2025) |
| **South Korea** | Evaluated | DX Korea 2018 display |
| **Multiple NATO** | Various | Marketing/demos ongoing |

---

## 4. DRONE DOME -- C-UAS SYSTEM

### 4.1 System Overview

| Attribute | Detail |
|-----------|--------|
| **Full Name** | DRONE DOME Counter-Unmanned Aircraft System |
| **Category** | Modular, end-to-end C-UAS; all-weather 360-degree defense |
| **Developer** | Rafael Advanced Defense Systems |
| **First Displayed** | 2016 |
| **Architecture** | Modular, open; configurable sensor + effector combinations |
| **Coverage** | 360-degree, all-weather |
| **Deployment** | Stationary (site defense), vehicle-mounted, naval |
| **Threat Targets** | Micro and mini UAVs (Groups 1-2) |

### 4.2 Sensor Suite

| Sensor | Supplier | Specification |
|--------|----------|---------------|
| **Radar** | RADA Electronic Industries RPS-42 (now RPS-82 variant) | Multi-mission hemispheric radar; 3.5 km typical detection; up to 10-16 km for larger objects |
| **EO/IR** | CONTROP Precision Technologies | Electro-optical/infrared camera suite for tracking and identification |
| **SIGINT/RF** | Built-in RF detection | Radio frequency signal detection of drone and operator communications |
| **CRFS RFeye** | CRFS (UK) | Enhanced RF direction-finding (added as integration partner) |
| **Sentrycs** | Sentrycs (Israel) | Cyber-over-RF for protocol-level drone identification (2025 integration) |

### 4.3 Effectors

| Effector | Type | Detail |
|----------|------|--------|
| **Reactive Jammer** | Soft-kill | Blocks drone communication channels including GNSS; reactive (not broadband) to minimize interference |
| **High-Energy Laser** | Hard-kill | Locks, tracks, and destroys target in seconds; focused beam minimizes collateral; used for hard-kill at short range |
| **Lite Beam** | Hard-kill laser | 10 kW high-energy laser system (newer integration option) |
| **SAMSON RCWS** | Kinetic hard-kill | 30mm remotely controlled weapon station (newer vehicle-mounted C-UAS variant) |

### 4.4 Kill Chain

1. **Detection**: RPS-42/82 radar provides 360-degree hemispheric surveillance; detects micro/mini UAVs at 3.5+ km
2. **Classification**: RF sensors identify drone type and operator location; EO/IR provides visual classification
3. **Identification**: C4I processes sensor data; AI algorithms classify threat level
4. **Tracking**: EO/IR turret locks and tracks target continuously
5. **Decision**: C4I performs positive identification; presents engagement options
6. **Engagement (Soft-Kill)**: Reactive jammer disrupts drone/operator communication and GNSS
7. **Engagement (Hard-Kill)**: Laser effector locks, tracks, and destroys target within seconds; OR kinetic engagement via RCWS

### 4.5 C4I / Command Center

| Feature | Detail |
|---------|--------|
| **Architecture** | Centralized C2 center with operator stations |
| **Multi-Sensor Fusion** | Fuses radar, SIGINT/RF, and EO/IR data |
| **AI Algorithms** | Automated threat classification and prioritization |
| **Target Allocation** | System allocates targets to appropriate effector (jammer or laser) |
| **Rules of Engagement** | Configurable ROE; operator confirms engagement |
| **Multi-Target** | Handles multiple simultaneous drone threats |
| **External Integration** | Open architecture enables integration with other C2 systems and external sensors |

### 4.6 Specifications Summary

| Parameter | Value |
|-----------|-------|
| **Radar Detection Range** | 3.5 km (micro UAV); up to 10-16 km (larger targets) |
| **Coverage** | 360 degrees, hemispheric |
| **Laser Type** | High-focusing directional laser |
| **Laser Kill Time** | Seconds after lock-on |
| **Jammer Type** | Reactive (targeted frequency disruption) |
| **GNSS Denial** | Yes, included in jammer capability |
| **Weather** | All-weather operation |
| **Modularity** | Sensors and effectors configurable per customer requirement |

### 4.7 Variants (2025 Expansion)

At DSEI 2025, Rafael unveiled new C-UAS variants:

| Product | Description |
|---------|-------------|
| **Hunter Eagle** | Vehicle-mounted C-UAS for light tactical vehicles; integrated radar + EO/IR + effectors on single turret; on-the-move engagement |
| **Ghost Hunter** | Man-portable / small platform C-UAS |
| **Drone Dome (Classic)** | Stationary site defense configuration |

### 4.8 Contracts and Customers

| Customer | Value | Date | Detail |
|----------|-------|------|--------|
| **UK MoD** | $20M (6 systems) | Aug 2018 | Urgent capability requirement; launch customer |
| **UK MoD** | GBP 7.6M ($9.97M) follow-on | 2018 | Additional systems/support |
| **UK (G7)** | — | Jun 2021 | Deployed to secure G7 Summit in Cornwall |
| **US DoD** | — | Nov 2022 | Won Pentagon certification / recommended status |
| **Israel (IDF)** | Undisclosed | Operational | In-service with IDF |
| **Multiple Export** | Undisclosed | Various | "Globally deployed" per Rafael |

### 4.9 US Pentagon Status

Rafael's Drone Dome advanced in the Pentagon's Joint Counter-Small Unmanned Aircraft Systems Office (JCO) certification process in 2022, receiving a formal recommendation. This positions it for US government procurement and FMS.

---

## 5. IRON DOME / C-DOME / IRON BEAM -- AIR DEFENSE C2 ECOSYSTEM

### 5.1 Iron Dome System Architecture

| Component | Supplier | Function |
|-----------|----------|----------|
| **EL/M-2084 Radar** | IAI Elta Systems | Multi-mission radar; detection 4-70 km; tracks projectile trajectory |
| **Battle Management & Weapon Control (BMC)** | mPrest Systems (50% Rafael-owned) | Command and control center; evaluates trajectory; decides intercept necessity |
| **Tamir Interceptor** | Rafael (produced also by R2S JV in USA) | Active radar/EO guided missile; 20 missiles per launcher |
| **Missile Firing Unit (MFU)** | Rafael | 3 launchers per battery; 20 ready-to-fire canisters per launcher |

#### BMC (mPrest) Capabilities -- DIRECTLY RELEVANT TO VN-CUAS-001

| Feature | Detail |
|---------|--------|
| **Threat Discrimination** | Distinguishes threats hitting defended areas vs. falling in open areas |
| **Selective Engagement** | Only intercepts projectiles threatening populated/defended areas (saves interceptors) |
| **Multi-Threat** | Handles multiple simultaneous incoming threats |
| **Automated Decision** | Advanced algorithms assess intercept necessity and priority |
| **Real-Time** | Sub-second threat evaluation and launch authorization |
| **Dual Guidance** | Supports both radar-guided and EO-guided Tamir variants |
| **Open Architecture** | Integrates with US IBCS (Integrated Battle Command System) and IFPC framework |

### 5.2 C-DOME (Naval Iron Dome)

| Attribute | Detail |
|-----------|--------|
| **Platform** | Sa'ar 6 "Magen" class corvettes (Israeli Navy) |
| **Architecture** | Modular; no hull penetration required for integration |
| **Fire Control Radar** | Uses ship's own surveillance radar (no dedicated FCR needed) |
| **C2 Integration** | Weapon system C2 integrated with ship's combat management system |
| **Interceptors** | Maintenance-free, stored in sea-proof canisters below deck |
| **Open Architecture** | Compatible with any ship's sensors and CMS |
| **First Live Fire** | February 2022 (successful intercepts from Sa'ar 6) |
| **First Combat** | April 2024 (operational intercepts during Gaza conflict) |
| **Prime Contractor** | Rafael |
| **Radar** | IAI Elta Systems |
| **C2 Software** | mPrest |

### 5.3 Iron Beam (High-Energy Laser)

| Attribute | Detail |
|-----------|--------|
| **Type** | 100 kW class high-energy laser air defense system |
| **Components** | Air defense radar + C2 unit + 2 HEL systems per battery |
| **Targets** | Rockets, mortars, UAVs |
| **First Delivery** | December 2025 (first operational system to IDF) |
| **First Combat Use** | October 2024 (prototype intercepted 40 Hezbollah UAVs during Gaza War) |
| **Cost per Shot** | ~$2 vs. $50,000+ per Tamir interceptor |
| **Designation** | "Or Eitan" in IDF service |

### 5.4 UK Sky Sabre -- Rafael BMC4I Export

Rafael won the UK MoD contract for the **Battle Management C4I (BMC4I)** element of the UK Sky Sabre ground-based air defense (GBAD) system. This demonstrates the exportability of Rafael's C2 technology beyond its Israeli systems.

---

## 6. SPICE GUIDANCE KITS -- AI/ML PRECEDENT

| Variant | Weight Class | Range | Key Technology |
|---------|-------------|-------|----------------|
| **SPICE 250** | 250 lb (113 kg) | 100 km | EO scene-matching + AI target recognition |
| **SPICE 1000** | 1000 lb (453 kg) | 100 km | CCD/IIR dual seeker; GPS-independent |
| **SPICE 2000** | 2000 lb (907 kg) | 60-100 km | Scene-matching + INS + optional GPS |

### AI Relevance to Fire Weaver

Rafael's SPICE bombs pioneered **scene-matching AI algorithms** for terminal guidance:
- Can store 100 potential targets per sortie
- CCD/IIR dual seeker provides GPS-independent navigation
- CEP < 3m (circular error probable)
- **AI from SPICE directly informs Fire Weaver's computer vision** and Geo-Pixel technology

### Partners

| Partner | Role |
|---------|------|
| **Lockheed Martin** | US marketing and production (teaming agreement 2019; SPICE 250 joint development) |
| **Diehl Defence + Hensoldt** | German Eurofighter EK integration (2023) |

---

## 7. TECHNOLOGY ARCHITECTURE ANALYSIS

### 7.1 Network-Centric Warfare Approach

Rafael's architecture follows a **"flat network"** philosophy:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   SENSORS   │     │ FIRE WEAVER │     │  EFFECTORS  │
│             │     │  (Software  │     │             │
│ • UAVs      │────▶│   Layer)    │────▶│ • SPIKE     │
│ • EO/IR     │     │             │     │ • RCWS      │
│ • Radars    │     │ • AI Engine │     │ • Mortars   │
│ • Binoculars│     │ • Geo-Pixel │     │ • Artillery │
│ • Trophy APS│     │ • FMT       │     │ • Helicopters│
│ • IMILITE   │     │ • ROE Proc  │     │ • LMs       │
└─────────────┘     └─────────────┘     └─────────────┘
        │                  │                    │
        └──────────────────┼────────────────────┘
                           │
                    ┌──────┴──────┐
                    │  BNET SDR   │
                    │  (Transport │
                    │   Layer)    │
                    │ IP MANET    │
                    │ 1000+ users │
                    └─────────────┘
                           │
                    ┌──────┴──────┐
                    │ EXISTING    │
                    │ C4I / BMS   │
                    │ (Elbit DAP, │
                    │  TORC2H,    │
                    │  NATO BMSs) │
                    └─────────────┘
```

### 7.2 Key Architectural Principles

| Principle | Implementation |
|-----------|---------------|
| **Open Architecture** | Integrates with ANY existing BMS/C4I; not a replacement |
| **Software-Defined** | Software layer, not hardware-dependent |
| **Flat Network** | All participants (sensors, shooters, commanders) on equal footing |
| **GPS-Independent** | Geo-Pixel spatial referencing works without GPS |
| **Low Bandwidth** | Transfers metadata, not video/images (critical for congested RF environments) |
| **Edge Computing** | Processing at sensor/weapon edge elements, not centralized |
| **Human in the Loop** | AI recommends, human approves lethal action |
| **Autonomous Levels** | Commander sets level of autonomy per operational context |
| **Multi-Domain** | Ground, air, naval, unmanned systems on same network |

### 7.3 Sensor Fusion Approach

Fire Weaver does NOT perform raw sensor fusion in the traditional sense. Instead, it:
1. Receives **classified targets** (post-processing) from connected sensors
2. Associates targets with **3D geo-pixel locations** on terrain models
3. Calculates **optimal engagement** parameters across all connected effectors
4. Presents **augmented reality** overlay showing targets, friendlies, keep-out zones

This is more accurately described as **"fire control fusion"** or **"engagement fusion"** rather than raw data-level sensor fusion.

### 7.4 IFF and Deconfliction

| Feature | Detail |
|---------|--------|
| **Blue Force Tracking** | Real-time position of all friendly elements displayed on every sight |
| **Augmented Reality IFF** | Friendly/hostile/unknown markers overlaid on weapon sights |
| **Keep-Out Zones** | Commander-defined exclusion areas where fire is prohibited |
| **Safety Limits** | Automatic safety calculations prevent friendly fire |
| **Sensitive Locations** | Mark and protect hospitals, mosques, civilian infrastructure |
| **Legal Processing** | ROE and international law constraints processed in real-time |
| **MIL-STD 882** | Full compliance with system safety standard |

---

## 8. STANDARDS AND INTEROPERABILITY

### 8.1 Known Standards Compliance

| Standard | System | Detail |
|----------|--------|--------|
| **MIL-STD 882** | Fire Weaver | System safety standard; full compliance |
| **SCA 2.2.2** | BNET | Software Communications Architecture for SDR |
| **IP Protocol** | BNET | Native IP networking |
| **NATO C4I Requirements** | MOSKITO TI (Safran) | Target locator meets NATO C4I interop |
| **Open Architecture** | Fire Weaver + C-DOME | Explicit open architecture design philosophy |
| **IBCS Compatible** | Iron Dome | Integration with US Army Integrated Battle Command System |

### 8.2 NATO Interoperability

Rafael has demonstrated clear NATO interoperability intent:

- **Germany**: Transparent Battlefield study explicitly aims to provide "common visual language among different types of units, not only from the Bundeswehr, but also from allied forces"
- **Netherlands**: Dutch SOF and Marine Corps participated in demonstrations
- **Safran Partnership**: MOSKITO TI (widely used by NATO infantry) integrating Fire Weaver
- **US Army**: AEWE and Project Convergence demonstrations
- **UK**: Sky Sabre BMC4I; Drone Dome
- **Greece**: NMT package with SPIKE NLOS + Fire Weaver

No specific STANAG numbers have been publicly attributed to Fire Weaver itself, but the system's open architecture and demonstrated multi-national interoperability suggest compliance with relevant NATO data exchange and C2 standards.

---

## 9. BUSINESS MODEL AND PRICING

### 9.1 Contract Values

| Contract | Customer | Value | Date |
|----------|----------|-------|------|
| **Fire Weaver IDF** | Israeli MoD | Undisclosed (est. $100-500M for brigade-level rollout) | Feb 2020 |
| **Drone Dome UK** | UK MoD | $20M (6 systems) | Aug 2018 |
| **Drone Dome UK** | UK MoD | GBP 7.6M follow-on | 2018 |
| **Sky Sabre BMC4I** | UK MoD | Undisclosed | — |
| **Tamir Production** | US (R2S JV) | $1.25 billion | Nov 2025 |
| **Iron Beam** | Israeli MoD | Undisclosed (est. $500M+) | Oct 2024 |
| **NMT (SPIKE + FW)** | Hellenic Army | Undisclosed | 2023 |
| **BNET India** | Indian Army | Undisclosed (Astra Rafael Comsys JV) | 2025 |
| **FIRE WEAVER (Oracle)** | Cloud deployment | Partnership (no contract value disclosed) | Sep 2024 |

### 9.2 Pricing Model (Estimated)

| System | Estimated Unit/System Cost |
|--------|---------------------------|
| **Drone Dome (full system)** | ~$3-5M per system (based on $20M/6 units to UK) |
| **Fire Weaver (per brigade)** | Estimated $50-150M per brigade deployment (software + edge elements + training) |
| **BNET radio (individual)** | Estimated $30-100K per radio unit (based on comparable SDR market) |
| **Tamir interceptor** | ~$50,000 per missile (publicly known) |
| **SPICE 250 kit** | Estimated $100-200K per unit |
| **Iron Beam shot** | ~$2 per laser engagement (operational cost, not system cost) |

### 9.3 Market Positioning

Rafael positions itself as a **full-spectrum defense provider** for network-centric warfare:

1. **Sensors** (IMILITE, CONTROP EO/IR, Trophy radar)
2. **C2 Layer** (Fire Weaver, mPrest BMC)
3. **Communications** (BNET SDR)
4. **Effectors** (SPIKE family, SPICE, Iron Dome, Iron Beam, SAMSON RCWS)
5. **Integration** (open architecture connecting everything)

This "system of systems" approach creates significant **vendor lock-in** while offering genuine interoperability through open architecture.

---

## 10. RECENT DEVELOPMENTS (2024-2025)

### 10.1 Record Financial Performance

- FY2024 revenue: $4.8B (+27% YoY)
- Order backlog: $17.76B (record)
- Net profit: $257M (+64% YoY)
- International sales: ~50% of total

### 10.2 Iron Beam Delivery

- First operational Iron Beam laser system delivered to IDF (December 2025)
- Combat prototype tested in October 2024 (40 Hezbollah UAV interceptions)
- World's first operational high-energy laser interceptor

### 10.3 Fire Weaver in Combat

- Confirmed used by IDF in Gaza operations (2023-2024) -- Jerusalem Post report
- IDF service name "Smart Trigger" operational with ground forces
- Trophy APS and Fire Weaver integration planned for Merkava tanks

### 10.4 Oracle Cloud Partnership (September 2024)

- FIRE WEAVER and IMILITE available on Oracle Cloud Infrastructure (OCI)
- Enables cloud-based AI processing for deployed forces
- Available on Oracle Government Cloud, National Security Regions, Isolated Regions, and Roving Edge Infrastructure

### 10.5 US Market Expansion

- RSGS (US subsidiary) positioned for IFPC Inc 2 air defense interceptor program (Feb 2026)
- R2S joint venture (Raytheon-Rafael) awarded $1.25B Tamir production contract (Nov 2025)
- Fire Weaver assessed at AEWE 21, 22 and Project Convergence
- Drone Dome won Pentagon certification (2022)

### 10.6 Privatization Discussions

- Israel considering partial privatization via public share sale
- Estimated valuation ~$10 billion
- $18B backlog supports premium valuation

### 10.7 C-UAS Evolution (DSEI 2025)

- Hunter Eagle: Vehicle-mounted integrated C-UAS for light tactical vehicles
- Ghost Hunter: Man-portable C-UAS
- Sentrycs cyber-over-RF integrated with Drone Dome (2025)
- Lite Beam 10 kW laser added as Drone Dome effector option

---

## 11. RELEVANCE TO VN-CUAS-001

### 11.1 Direct Relevance -- C2/Integration Architecture

| Rafael Concept | VN-CUAS Applicability | Priority |
|----------------|----------------------|----------|
| **Open architecture software layer** | VN-CUAS needs a C2 layer that integrates with existing BMS/TAK | HIGH |
| **Geo-Pixel common visual language** | GPS-independent target referencing critical for VN context | MEDIUM |
| **AI-driven target allocation** | Autonomous threat prioritization for C-UAS nodes | HIGH |
| **Low-bandwidth metadata transfer** | Critical for contested RF environments | HIGH |
| **Flat network topology** | Distributed acoustic nodes need peer-to-peer networking | HIGH |
| **Edge computing** | Classification at sensor node, not centralized | HIGH |
| **Human in the loop with adjustable autonomy** | ROE compliance critical for VN defense | HIGH |
| **MIL-STD 882 safety compliance** | System safety standard applicable to VN-CUAS | MEDIUM |

### 11.2 Drone Dome Architecture Lessons

| Drone Dome Feature | VN-CUAS Applicability | Notes |
|--------------------|----------------------|-------|
| **Modular sensor architecture** | Acoustic array + optional radar/EO/IR | Core concept for VN-CUAS |
| **Reactive jamming (not broadband)** | Minimize interference in dense RF | Relevant for urban VN deployment |
| **Multi-effector C2** | Coordinate soft-kill + hard-kill options | Future VN-CUAS growth path |
| **360-degree hemispheric coverage** | Acoustic arrays inherently provide this | VN-CUAS advantage over radar-only |
| **AI classification algorithms** | Dual classification (eigenvector + spectrogram-to-CV) | Aligns with VN-CUAS v8.0 concept |

### 11.3 What VN-CUAS Can Learn

1. **Software-first architecture**: Fire Weaver is fundamentally software. This validates VN-CUAS approach of firmware-defined multi-mission capability.

2. **Metadata, not video**: Fire Weaver's low-bandwidth Geo-Pixel approach (transferring coordinates + metadata, not images/video) is directly applicable to VN-CUAS acoustic detection output -- bearing, elevation, classification, confidence -- not raw audio streams.

3. **Open architecture for export**: Rafael's success in demonstrating to Germany, US, Netherlands, Greece, UK all comes from open architecture. VN-CUAS must design for SAPIENT/TAK/BMS integration from day one.

4. **Edge elements embedded in existing equipment**: Fire Weaver embeds in binoculars, weapon sights, existing BMSs. VN-CUAS acoustic nodes should output to existing C2 screens, not require dedicated displays.

5. **"Fires exchange" marketplace model**: The concept of "publish tender, receive bids, execute optimal" is directly applicable to multi-node acoustic detection where multiple nodes detect the same threat and the system must allocate tracking/engagement.

6. **Adjustable autonomy**: Commander sets the level. This is the correct approach for VN defense context where ROE varies by operational scenario.

### 11.4 What VN-CUAS CANNOT Replicate

| Capability | Barrier | Alternative |
|------------|---------|-------------|
| **Geo-Pixel 3D terrain matching** | Requires high-res 3D terrain data of entire operational area | Use standard GPS/grid coordinates with acoustic bearing overlay |
| **BNET SDR network** | Proprietary, ITAR-controlled | Use standard IP/MANET radios; SAPIENT over existing comms |
| **AI from decades of SPICE/Iron Dome data** | Training data from combat engagements not available | Build acoustic ML models from ground-truth test data |
| **$4.8B R&D ecosystem** | VN-CUAS budget is $2-5K per node | Focus on open-source ML frameworks (TensorFlow Lite, ONNX) |

---

## 12. TECHNOLOGY ASSESSMENT SUMMARY

### 12.1 Rafael C2 Ecosystem Maturity

| Technology | TRL | Combat Proven | Export Success |
|------------|-----|---------------|----------------|
| **Iron Dome BMC** | 9 | Yes (thousands of intercepts) | Yes (US IFPC, UK Sky Sabre) |
| **Fire Weaver** | 8-9 | Yes (Gaza 2023-24) | Limited (demonstrations to 5+ nations) |
| **BNET SDR** | 9 | Yes (IDF service) | Yes (India, evaluations worldwide) |
| **Drone Dome** | 9 | Yes (IDF, UK G7) | Yes (UK, US Pentagon cert) |
| **C-DOME** | 9 | Yes (2024 combat intercepts) | Limited to Sa'ar 6 |
| **Iron Beam** | 8 | Yes (Oct 2024 prototypes) | Not yet exported |
| **SPICE AI** | 9 | Yes (extensive IDF use) | Yes (multiple nations) |

### 12.2 Key Differentiators

1. **Combat-proven ecosystem**: Unlike most competitors, Rafael's C2 systems have been validated in high-intensity combat (Gaza 2023-2024)
2. **System-of-systems integration**: FIRE WEAVER + BNET + SPIKE + Trophy + Iron Dome form a coherent ecosystem
3. **AI pedigree**: Scene-matching AI from SPICE, trajectory prediction from Iron Dome BMC, and engagement optimization from Fire Weaver represent deep AI/ML expertise
4. **Government backing**: 100% Israeli MoD ownership ensures sustained R&D investment
5. **Scalable**: From single-node (DRONE DOME) to multi-brigade (FIRE WEAVER) to national defense (Iron Dome)

---

## 13. SOURCES

| # | Source | URL | Accessed |
|---|--------|-----|----------|
| 1 | Defense Update: IDF Brigade to Field AI-Empowered Networked Fires | defense-update.com/20200203_fireweaver.html | 2026-02-12 |
| 2 | European Security & Defence: Tightening the Sensor-to-Shooter Loop | euro-sd.com/2025/02/articles/42517 | 2026-02-12 |
| 3 | Global Defence Technology: AI on the Battlefield (May 2021) | defence.nridigital.com/global_defence_technology_may21 | 2026-02-12 |
| 4 | Army Technology: IDF acquires Fire Weaver | army-technology.com/news/idf-rafael-weaver | 2026-02-12 |
| 5 | EDR Magazine: IDF chooses FIRE WEAVER | edrmagazine.eu (multiple articles) | 2026-02-12 |
| 6 | EDR Magazine: US Army AEWE Assessment | edrmagazine.eu (AEWE article) | 2026-02-12 |
| 7 | Safran: FIRE WEAVER + MOSKITO TI MoU | safran-group.com/pressroom | 2026-02-12 |
| 8 | Oracle: Cloud-Based AI Solutions with Rafael | oracle.com/news/announcement/ocw24 | 2026-02-12 |
| 9 | Breaking Defense: Rafael Record Sales 2024 | breakingdefense.com/2025/03 | 2026-02-12 |
| 10 | Israel Defense: Rafael FY2024 Results | israeldefense.co.il/en/node/64755 | 2026-02-12 |
| 11 | Arabian Defence: Rafael 2024 Financial Results | arabiandefence.com/2025/03/26 | 2026-02-12 |
| 12 | Wikipedia: Rafael Advanced Defense Systems | en.wikipedia.org | 2026-02-12 |
| 13 | Wikipedia: Drone Dome | en.wikipedia.org | 2026-02-12 |
| 14 | Wikipedia: Iron Dome | en.wikipedia.org | 2026-02-12 |
| 15 | Rafael UK: Drone Dome Brochure (PDF) | rafael-uk.com/wp-content/uploads/2022/10/Drone-Dome.pdf | 2026-02-12 |
| 16 | Rafael: BNET-HH SDR Brochure (PDF) | rafael.co.il/wp-content/uploads/2024/09 | 2026-02-12 |
| 17 | Jerusalem Post: New Weapon Systems in Gaza | jpost.com/arab-israeli-conflict/gaza-news/article-776000 | 2026-02-12 |
| 18 | Defense News: Weapons for Gaza Ground Campaign | defensenews.com (Oct 2023) | 2026-02-12 |
| 19 | JNS: Tank Protection System & Fire Weaver | jns.org | 2026-02-12 |
| 20 | C4ISRNet: Israel finds AI system for urban combat | c4isrnet.com (Feb 2020) | 2026-02-12 |
| 21 | C4ISRNet: Germany hires Rafael/Atos for Glass Battlefield | c4isrnet.com (Dec 2019) | 2026-02-12 |
| 22 | EDR Magazine: DEFEA 2023 NMT deal with Hellenic Army | edrmagazine.eu | 2026-02-12 |
| 23 | Globes: Rafael sells 6 Drone Domes to UK for $20M | en.globes.co.il | 2026-02-12 |
| 24 | Globes: Drone Dome secured G7 Summit | en.globes.co.il | 2026-02-12 |
| 25 | Times of Israel: Privatization of IAI and Rafael | timesofisrael.com | 2026-02-12 |
| 26 | mPrest Systems: Defense C2 | mprest.com/industries/defense | 2026-02-12 |
| 27 | EDR Magazine: Rafael 2024 Q4 Financial Summary (PDF) | edrmagazine.eu/wp-content/uploads/2025/03 | 2026-02-12 |
| 28 | Joint Forces News: Multiple Fire Weaver articles | joint-forces.com | 2026-02-12 |
| 29 | Janes: IAV 2022 Fire Weaver demo plans | janes.com | 2026-02-12 |
| 30 | Army Recognition: DEFEA 2025 Hunter Eagle C-UAS | armyrecognition.com | 2026-02-12 |
| 31 | CAAT: Rafael company profile | caat.org.uk/data/companies/rafael | 2026-02-12 |
| 32 | Asian Military Review: IDF chooses Fire Weaver | asianmilitaryreview.com (Feb 2020) | 2026-02-12 |
| 33 | Lockheed Martin: SPICE 250 Partnership | news.lockheedmartin.com | 2026-02-12 |
| 34 | RTX: R2S $1.25B Tamir Contract | rtx.com/news/news-center/2025/11/21 | 2026-02-12 |
| 35 | UAS Weekly: Sentrycs + Drone Dome Integration | uasweekly.com/2025/07/03 | 2026-02-12 |
| 36 | EDR Magazine: Rafael DSEI 2025 Hunter Eagle & Ghost Hunter | edrmagazine.eu | 2026-02-12 |

---

*Analysis complete. This RE document covers Rafael's C2/networked warfare ecosystem with focus on FIRE WEAVER sensor-to-shooter, DRONE DOME C-UAS, BNET SDR, and the Iron Dome/C-DOME/Iron Beam air defense C2 architecture. Key findings inform VN-CUAS-001 C2 layer design, particularly the software-first open architecture, low-bandwidth metadata transfer, edge computing, and adjustable autonomy concepts.*
