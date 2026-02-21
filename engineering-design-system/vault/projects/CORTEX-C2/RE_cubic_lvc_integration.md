---
project: CORTEX-C2
phase: 0
type: reverse-engineering
subject: Cubic Corporation LVC Integration Architecture (USA) - Deep Dive
version: 1.0
created: 2026-02-12
status: complete
---

# RE Analysis: Cubic Corporation LVC Integration Architecture

## Executive Summary

Cubic Corporation (now a subsidiary of Veritas Capital, acquired 2021 for $3B) is the **dominant global provider** of Live, Virtual, Constructive (LVC) training systems for military forces. Their architecture spans from individual soldier-worn laser engagement devices (I-MILES) through air combat maneuvering pods (P5CTS) to enterprise-scale exercise control and after-action review platforms (CATS Metrix, SPEAR). This analysis dissects the data flows, protocols, hardware, software, and integration patterns that connect their entire training ecosystem -- identifying critical integration standards for CORTEX RANGE and exploitable gaps in their architecture.

**Key Finding**: Cubic's architecture is **hardware-centric, protocol-heavy, and centralized** in its analytics approach. Their SPEAR Common Data Model is the critical integration layer, but it remains proprietary and expensive. CORTEX RANGE can position as an **AI-first, open-architecture analytics layer** that ingests standard training data (DIS/HLA/TENA) at a fraction of the cost, targeting the 90%+ of ranges that cannot afford Cubic's full CTC-scale solution.

---

## System Architecture Overview

```
+===========================================================================+
|                    CUBIC LVC INTEGRATION ARCHITECTURE                      |
+===========================================================================+
|                                                                            |
|  +-----------------+  +-----------------+  +------------------+            |
|  |   LIVE DOMAIN   |  | VIRTUAL DOMAIN  |  |CONSTRUCTIVE DOMAIN|           |
|  +-----------------+  +-----------------+  +------------------+            |
|  | I-MILES IWS 2   |  | SCOPIC2         |  | JCATS (LLNL)     |           |
|  | I-MILES TVS     |  | Synthetic Wrap  |  | JTLS             |           |
|  | CVTESS (Saab)   |  | RVS Simulator   |  | JSAF             |           |
|  | VTESS (LM/Saab) |  | SITL-LVC        |  | CGF Engines      |           |
|  | Mortar TESS     |  | Flight Sims     |  | Scenario Gen     |           |
|  | AWES (UK)       |  | (F/A-18, F-35)  |  | Threat Models    |           |
|  | ILT-A (UK)      |  |                 |  |                  |           |
|  | P5CTS ACMI      |  |                 |  |                  |           |
|  | SLATE LVC       |  |                 |  |                  |           |
|  +---------+-------+  +--------+--------+  +---------+--------+           |
|            |                   |                      |                    |
|            v                   v                      v                    |
|  +--------------------------------------------------------------+         |
|  |            INTEGRATION / GATEWAY LAYER                        |         |
|  |  +----------+ +-----------+ +----------+ +----------------+  |         |
|  |  | DIS 1278 | | HLA 1516  | |   TENA   | | SPEAR CDM      |  |         |
|  |  | Gateway  | | RTI/FOM   | | Gateway  | | (Proprietary)  |  |         |
|  |  +----------+ +-----------+ +----------+ +----------------+  |         |
|  +--------------------------------------------------------------+         |
|            |                   |                      |                    |
|            v                   v                      v                    |
|  +--------------------------------------------------------------+         |
|  |              NETWORK INFRASTRUCTURE                           |         |
|  |  +----------+ +-----------+ +----------+ +----------------+  |         |
|  |  | DTECH    | | NCTE      | | DMON     | | Tactical       |  |         |
|  |  | Edge     | | (Navy)    | | (USAF)   | | Radio Links    |  |         |
|  |  | Nodes    | |           | |          | | (L-band, UHF)  |  |         |
|  |  +----------+ +-----------+ +----------+ +----------------+  |         |
|  +--------------------------------------------------------------+         |
|            |                   |                      |                    |
|            v                   v                      v                    |
|  +--------------------------------------------------------------+         |
|  |              COMMAND & ANALYSIS LAYER                         |         |
|  |  +--------------+ +-------------+ +------------------------+ |         |
|  |  | CATS Metrix  | | ICADS       | | SPEAR Analytics        | |         |
|  |  | (Ground      | | (Air Combat | | (Multi-Domain          | |         |
|  |  |  EXCON/AAR)  | |  Debrief)   | |  Planning/Execution/   | |         |
|  |  |              | |             | |  Analysis/Reconstruct) | |         |
|  |  +--------------+ +-------------+ +------------------------+ |         |
|  +--------------------------------------------------------------+         |
|            |                   |                      |                    |
|            v                   v                      v                    |
|  +--------------------------------------------------------------+         |
|  |              OUTPUT / INTEGRATION                             |         |
|  |  +---------+ +----------+ +-----------+ +-----------------+  |         |
|  |  | TAKTICS | | Mission  | | Training  | | Data Export     |  |         |
|  |  | (TAK)   | | Command  | | Mgmt      | | (Proprietary)  |  |         |
|  |  +---------+ +----------+ +-----------+ +-----------------+  |         |
|  +--------------------------------------------------------------+         |
+===========================================================================+
```

---

## 1. LIVE TRAINING SYSTEMS (Deep Technical)

### 1.1 I-MILES Family

The **Instrumentable Multiple Integrated Laser Engagement System** (I-MILES) is Cubic's core ground-force live training product line. It uses coded infrared laser pulses to simulate weapons fire and determine engagement outcomes.

#### 1.1.1 I-MILES IWS 2 (Individual Weapon System)

| Parameter | Specification |
|-----------|--------------|
| **Manufacturer** | Cubic Corporation (San Diego, CA) |
| **Contract Holder** | PEO STRI (PM TRADE, PdM LTS) |
| **Laser Type** | Pulsed infrared, 905nm eye-safe |
| **Pulse Coding** | Digital code modulated on IR carrier; encodes Player ID + Weapon Type |
| **MILES Code Format** | Pulse-coded burst triggered by blank round; code includes weapon class identifier (e.g., Code 35 = controller override) |
| **Detection** | Halo (head-mounted) + H-harness (body) with multiple IR detectors |
| **Kill/Near-Miss Logic** | Probability-of-Kill (PK) lookup tables; weapon type vs. target type matrix |
| **HCU (Harness Control Unit)** | Stores event data, provides user menu, sends/receives IR data via Comms module |
| **Data Storage** | Events logged locally on HCU; transferred via IR link to SAT (Small Arms Transmitter) or via optical link to TDTD |
| **Weight** | < 3.5 lbs entire kit (halo + harness + SAT) |
| **Key Feature** | Wireless MILES technology for real-time casualty assessment |
| **Interoperability** | Compatible with CVTESS, VTESS, range instrumentation systems |
| **Export Customers** | Latvia, Romania, 20+ NATO nations |
| **Contract Values** | $44M+ in cumulative orders (2016-2020 period); $10M+ individual orders |

**MILES Laser Protocol (Critical for CORTEX integration)**:

```
MILES IR Pulse Format:
+-------+----------+----------+----------+
| SYNC  | PLAYER   | WEAPON   | CHECKSUM |
| PULSE | ID CODE  | TYPE CODE|          |
+-------+----------+----------+----------+
  |         |           |          |
  |   8-16 bit     8-bit code   CRC
  |   unique ID    weapon class
  |
  Trigger: Blank round fires -> acoustic sensor
           activates laser transmitter

Weapon Types (MILES Code Examples):
  Code 05: M16/M4 (5.56mm)
  Code 10: M240 (7.62mm MG)
  Code 15: M2 (.50 cal)
  Code 20: TOW missile
  Code 25: Tank main gun (120mm)
  Code 35: Controller override (manual kill)

PK Table Logic:
  Weapon Type + Range + Target Type = PK value (0.0-1.0)
  Random number compared against PK -> Kill/Near-Miss/Miss
  Result transmitted to target's receiver array
```

**Data Collection Flow**:

```
Blank Fired -> SAT Laser Burst (905nm IR) -> Target Detector Array
                                                     |
                                              HCU processes:
                                              - Weapon type decode
                                              - PK table lookup
                                              - Kill determination
                                              - Event timestamp
                                              - GPS position (if I-MILES)
                                                     |
                                              Local storage (HCU flash)
                                                     |
                                    +---------+------+---------+
                                    |                          |
                              IR Data Link              RF Data Link
                              (to controller            (to EXCON/AAR)
                               device/TDTD)             via range
                                                        instrumentation
```

#### 1.1.2 TVS (Tactical Vehicle System)

| Parameter | Specification |
|-----------|--------------|
| **Application** | Wheeled vehicles (HMMWV, Stryker, etc.) |
| **Detection Coverage** | 360-degree IR detector array on vehicle exterior |
| **Transmitter** | Vehicle-mounted laser aligned to weapon systems |
| **Wireless** | RF data link for real-time status to EXCON |
| **Integration** | Compatible with I-MILES IWS for dismounted troops |
| **Kill Logic** | Vehicle-specific PK tables (armor value vs weapon penetration) |

#### 1.1.3 CVTESS (Combat Vehicle Tactical Engagement Simulation System)

| Parameter | Specification |
|-----------|--------------|
| **Manufacturer** | **Saab Defense and Security** (NOT Cubic -- critical distinction) |
| **Application** | M1 Abrams, M2/M3 Bradley (heavy armor) |
| **Fielded** | 3,000+ vehicle systems to US Army |
| **Technology** | Laser AND radio frequency based |
| **Simulates** | Direct fire, armor penetration, vehicle kills |
| **OSAG 2.0** | Interoperability upgrade for CTC deployments |
| **Key Difference** | Saab is prime contractor, NOT Cubic |

#### 1.1.4 VTESS (Vehicle Tactical Engagement Simulation System)

| Parameter | Specification |
|-----------|--------------|
| **Manufacturer** | **Lockheed Martin / Saab** partnership |
| **Contract** | Awarded July 2017; $17.7M modernization change order 2018 |
| **Status** | Government Acceptance Test passed; first 160 base kits to Fort Polk (2021) |
| **Code Modernization** | Increases interoperability for force-on-force training |
| **Platforms** | M1A1/A2, Bradley, light vehicles |

**Important Note for CORTEX**: CVTESS and VTESS are Saab/Lockheed Martin products, NOT Cubic. Cubic provides I-MILES (manworn) and the EXCON/AAR infrastructure. At CTCs, these interoperate via common MILES protocols and range instrumentation networks.

#### 1.1.5 Mortar TESS

| Parameter | Specification |
|-----------|--------------|
| **Technology** | Laser-less, geo-pairing technology |
| **Design** | Reuses combat mortar bipod, baseplate, and sight |
| **Simulation** | Indirect fire effects computed by AWES system using trajectory + impact point |
| **Provider** | Ravenwood Solutions / Army A-TESS program |

#### 1.1.6 MILES Data Latency and Collection

| Parameter | Value |
|-----------|-------|
| **Laser Engagement** | Near-instantaneous (speed of light) |
| **Kill Determination** | < 100ms (local HCU processing) |
| **Position Update** | 1 Hz GPS (1 update/second) for instrumented systems |
| **Data Upload to EXCON** | Variable: RF real-time (seconds) or post-exercise IR dump |
| **AAR Data Availability** | Real-time (limited) or full post-exercise download |
| **GPS Accuracy** | 3-10m CEP (military GPS); improved with DGPS at CTCs |

### 1.2 AWES / ILT-A (Area Weapons Effects Simulation)

#### 1.2.1 AWES (British Army -- Cubic Defence UK)

| Parameter | Specification |
|-----------|--------------|
| **Originally Delivered** | Contract awarded 1998 |
| **Customer** | UK Ministry of Defence |
| **Contract Extensions** | Multiple; latest April 2023 |
| **Capacity** | Tracks 1,400+ individual soldiers and 250+ vehicles via GPS |
| **Simulates** | Direct fire, artillery, mortar fire, mines, air-delivered munitions, NBC weapons |
| **Mechanism** | GPS position of all players + impact point calculation = casualty determination |

**AWES Indirect Fire Simulation Flow**:

```
Fire Mission Initiated (Observer -> EXCON)
         |
         v
Trajectory Computed (ballistic model)
         |
         v
Impact Point Calculated (GPS coordinates)
         |
         v
Burst Radius Applied (weapon-specific)
         |
         v
All Players in Radius Queried:
  - GPS position vs impact point distance
  - Cover/concealment modifiers
  - Armor protection factors
  - Fragmentation density model
         |
         v
Casualty Assessment per Player:
  - KIA / WIA / Suppressed / No Effect
         |
         v
Result Transmitted to Player HCU:
  - MILES "kill code" sent via RF
  - Player's harness activates kill indicator
```

#### 1.2.2 ILT-A (Integrated Live Training - Area Weapons Effects)

| Parameter | Specification |
|-----------|--------------|
| **Awarded** | July 2025 (UK MoD sole-source contract) |
| **Provider** | Cubic Defence UK |
| **Capability** | Advanced laser + area-effects technology + live-fire range + RPAS integration |
| **Environment** | Multi-spectrum, multi-domain threat simulation |
| **Integration** | SCOPIC2 Virtual-in-Live synthetic environment |
| **Key Advance** | Combines laser engagement with area effects AND drone integration |

### 1.3 P5CTS ACMI (Air Combat Maneuvering Instrumentation)

The P5 Combat Training System is Cubic's flagship air domain training product.

#### 1.3.1 Pod Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form Factor** | External pod (wing/fuselage pylon mounted) or internal subsystem (F-35) |
| **Pod Appearance** | "Giant pencil" shaped housing |
| **GPS** | Embedded GPS receiver for self-positioning (replaced legacy triangulation) |
| **Data Link** | Type-1 encrypted L-band communications (1755-1850 MHz) |
| **Range** | > 100 km communication range |
| **Anti-Jam** | Spread-spectrum, low-probability-of-intercept modulation |
| **Recording** | Position, attitude (6DOF), weapons employment, IFF, radar modes |
| **Real-Time** | TSPI (Time, Space, Position Information) relayed between aircraft during sortie |
| **Post-Mission** | Full data download to ICADS ground station for debrief |

#### 1.3.2 Data Recorded

```
P5CTS Data Packet (per aircraft, per timestamp):
+------------------------------------------------------------------+
| TSPI Block:                                                       |
|   - Latitude, Longitude, Altitude (WGS-84)                       |
|   - Ground speed, True airspeed                                   |
|   - Heading, Pitch, Roll, Yaw rates                              |
|   - G-loading (Nx, Ny, Nz)                                       |
|   - Timestamp (GPS synchronized, sub-millisecond)                 |
+------------------------------------------------------------------+
| Weapons Employment:                                               |
|   - Weapon release event (type, time, target)                    |
|   - Simulated missile flyout (computed trajectory)                |
|   - Kill assessment (hit/miss/proximity)                          |
|   - Radar lock status                                             |
+------------------------------------------------------------------+
| System State:                                                     |
|   - IFF mode/code                                                 |
|   - Fuel state                                                    |
|   - Stores remaining                                              |
|   - Defensive systems status                                      |
+------------------------------------------------------------------+
| LVC Inject Data (SLATE-equipped):                                 |
|   - Synthetic entity positions                                    |
|   - Virtual threat parameters                                     |
|   - Guised entity data (friendly appearing as adversary)          |
+------------------------------------------------------------------+
```

#### 1.3.3 F-35 Internal Subsystem

| Parameter | Specification |
|-----------|--------------|
| **Integration** | Internal to F-35 avionics (no external pod) |
| **Components** | P5 internal instrumentation package + P5 planning software within JSFMSF |
| **Provider** | Leonardo DRS (ACMI Pods & Subsystems division) |
| **Contract** | 150+ P5CTS for F-35 across USAF, USN, international partners |
| **Key Capability** | Enables 5th-gen to 5th-gen + 5th-to-4th-gen interoperability in training |
| **Data Sensitivity** | Extremely high -- radar cross-section, sensor capabilities must be protected |

#### 1.3.4 SSU (System Security Upgrade) - Encryption

| Parameter | Specification |
|-----------|--------------|
| **Contract** | Awarded 2022 (firm-fixed-price) |
| **Purpose** | NSA Type-1 encryption of TSPI data for P5 pod fleet |
| **Delivery** | First encrypted ACMI kits delivered to USAF May 2025 |
| **Scope** | "Substantial percentage" of USAF P5 pod fleet |
| **Capability** | Fully interoperable encrypted TSPI between 4th-gen and F-35 platforms |
| **Follow-On** | 102 new P5CTS pods with SSU and Block 7 capabilities (Aug 2025 contract) |
| **Encryption** | Protects country-specific maneuvering data during multinational exercises |

#### 1.3.5 ACMI Deployment Scale

| Customer | Approximate Fleet |
|----------|------------------|
| US Air Force | 500+ pods (estimate) |
| US Navy | 200+ pods (estimate) |
| Royal Australian Air Force | 50+ (recent SPEAR contract) |
| NATO allies | 20+ nations |
| F-35 Partner Nations | Growing with each production lot |
| **Total Global** | **1,500+ ACMI pods/subsystems (estimate)** |

### 1.4 Position Tracking

#### 1.4.1 Ground Tracking

| Parameter | Specification |
|-----------|--------------|
| **Primary** | GPS (L1/L2 military, L1 civilian) |
| **Update Rate** | 1 Hz standard (1 position/second) |
| **Accuracy** | 3-10m CEP (open sky); degraded in urban/forested terrain |
| **CTC Enhanced** | DGPS corrections broadcast from fixed towers (sub-meter possible) |
| **Historical** | Pre-GPS: General Dynamics microwave transponder system at NTC (1980s) |

#### 1.4.2 Air Tracking

| Parameter | Specification |
|-----------|--------------|
| **Primary** | P5CTS pod embedded GPS (12-channel or better) |
| **Update Rate** | 5-10 Hz (higher than ground due to dynamics) |
| **Accuracy** | Sub-meter (military GPS + INS hybridized) |
| **Data Link** | Real-time TSPI relay via L-band encrypted link |

#### 1.4.3 Indoor/Urban Tracking (Limited)

Cubic does NOT have a strong UWB indoor tracking product. This is a gap.

| Current State | Notes |
|---------------|-------|
| GPS-denied environments | Degraded or no tracking |
| UWB capability | Not a core Cubic product |
| MOUT training | Relies on reduced GPS accuracy or manual position reporting |
| **Gap for CORTEX** | **Acoustic/UWB hybrid positioning in GPS-denied environments** |

---

## 2. VIRTUAL TRAINING SYSTEMS

### 2.1 SCOPIC2 (Synthetic Combined Operations Picture Integrated Capability)

| Parameter | Specification |
|-----------|--------------|
| **Full Name** | Synthetic Wrap / SCOPIC2 |
| **Customer** | British Army (primary) |
| **Contract** | $16M+ (4-year managed service), awarded 2020 |
| **Deployment Sites** | Salisbury Plain Training Area (UK), BATUS (Canada), BATUK (Kenya) |
| **Concept** | "Virtual-in-Live" -- expands instrumented live training with virtual/constructive entities |

**What SCOPIC2 Does**:

SCOPIC2 creates a **"Synthetic Wrap"** around the live training area. This means:

1. **Live players** operate in the real terrain with real MILES equipment
2. **Virtual entities** (UAVs, GBAD systems, STA sensors, artillery) are injected into the battlespace
3. **Both Red and Blue** forces can interact with synthetic entities using their actual equipment
4. Live players see synthetic entities on their tactical displays (via data injection)
5. Synthetic entities respond to live player actions (shoot-back, detect, etc.)

```
SCOPIC2 Architecture:

  +------------------+     +------------------+
  | LIVE BATTLESPACE | <-> | SYNTHETIC LAYER  |
  +------------------+     +------------------+
  | Real soldiers    |     | Virtual UAVs     |
  | Real vehicles    |     | Virtual GBAD     |
  | Real terrain     |     | Virtual artillery|
  | MILES engagement |     | Virtual threats  |
  +--------+---------+     +--------+---------+
           |                        |
           v                        v
  +----------------------------------------+
  | SCOPIC2 INTEGRATION ENGINE             |
  | - Entity state management              |
  | - Engagement resolution                |
  | - DIS/HLA protocol translation         |
  | - Position correlation                 |
  | - Effects adjudication                 |
  +----------------------------------------+
           |
           v
  +------------------+
  | CATS Metrix      |
  | EXCON/AAR        |
  +------------------+
```

**Standards Used**: DIS (IEEE 1278) for entity state PDUs; HLA (IEEE 1516) for federation management. The specific FOM (Federation Object Model) is likely RPR-FOM based with Cubic-specific extensions.

### 2.2 Reconfigurable Vehicle Simulator (RVS)

Limited public information on Cubic's dedicated ground vehicle simulator. Their virtual capability primarily comes through:

1. **Partnership with CAE** (NXTGEN8 initiative) for high-fidelity simulators
2. **F/A-18E/F simulators** connected via NCTE for naval aviation
3. **F-35 Effects Based Simulator** for 5th-gen integration
4. **Aegis Battle Force Tactical Trainers** for surface combatant crews

Virtual vehicle data merges with live MILES data through the **DIS/HLA gateway layer** -- both domains produce Entity State PDUs that the integration engine correlates into a single Common Operating Picture.

### 2.3 SITL (Synthetic Inject to Live)

| Parameter | Specification |
|-----------|--------------|
| **Full Name** | Synthetic Inject to Live - Live Virtual Constructive (SITL-LVC) |
| **Partners** | Cubic + Boeing (initial development) |
| **Validation** | 97+ sorties on operational USAF and USN fighter aircraft |
| **Unique Claim** | "Lone company to demonstrate ability to inject virtual and constructive synthetic entities into live fighter cockpit displays at LFE scale" |
| **Scale** | Large Force Employment (LFE) -- dozens of aircraft simultaneously |

**SITL Key Technical Capabilities**:

1. **Entity Guising**: Participants can be made to appear as different entity types across all Blue platform system displays (e.g., friendly F-18 appears as adversary Su-30 to training audience)
2. **Synthetic Threat Injection**: Computer-generated forces (CGF) appear on live cockpit displays as real radar contacts
3. **Real-Time Engagement**: Live pilots can engage synthetic targets; synthetic threats can "kill" live participants
4. **Multi-Level Security**: MILS architecture with NSA Type-1 encryption protects classified sensor/platform data

**Latency Requirements for SITL**:

| Data Type | Required Latency | Notes |
|-----------|-----------------|-------|
| TSPI (position) | < 100ms | Critical for realistic radar picture |
| Engagement events | < 200ms | Weapons employment correlation |
| Entity state updates | 5-10 Hz minimum | Smooth entity movement on displays |
| Display injection | < 50ms | Must feel "real" to pilot |

---

## 3. CONSTRUCTIVE TRAINING

### 3.1 JCATS (Joint Conflict and Tactical Simulation)

| Parameter | Specification |
|-----------|--------------|
| **Developer** | Lawrence Livermore National Laboratory (LLNL) Conflict Simulation Laboratory |
| **Type** | Discrete-event, entity-level constructive simulation |
| **Resolution** | Individual soldier and vehicle level |
| **Scale** | Handful of entities to hundreds of thousands (JTF-level) |
| **Use** | Training, analysis, mission planning, "what-if" scenarios |
| **Users** | US military services, DOE security forces, international allies |
| **Availability** | Since 1980s (evolved from JANUS) |

**JCATS Integration with LVC**:

```
JCATS Integration Architecture:

+------------------+     +------------------+
|     JCATS        | <-> | LVC-IA Gateway   |
| (Constructive)   |     |                  |
+------------------+     +------------------+
| Entity-level sim |     | Protocol         |
| Weapons models   |     | Translation:     |
| Terrain models   |     |  JCATS <-> DIS   |
| Sensor models    |     |  JCATS <-> HLA   |
| C2 simulation    |     |                  |
+------------------+     +--------+---------+
                                  |
                    +-------------+-------------+
                    |                           |
              +-----v------+            +-------v-------+
              | Live Domain|            | Virtual Domain |
              | (MILES,    |            | (Simulators,   |
              |  AWES,     |            |  SCOPIC2,      |
              |  P5CTS)    |            |  Flight Sims)  |
              +------------+            +---------------+
```

**JCATS Data Provided to LVC Network**:

| Data Type | Description |
|-----------|-------------|
| Entity State | Position, velocity, orientation of constructive entities |
| Fire Events | Weapons employment by CGF units |
| Detonation Events | Impact and effects of constructive fires |
| Electronic Warfare | Jamming, detection, SIGINT events |
| Logistics | Supply, maintenance, casualty events |
| C2 Messages | Orders, reports, intelligence updates |
| Sensor Detections | What constructive sensors "see" |

**JCATS-JTLS Federation**: JCATS integrates with Joint Theater Level Simulation (JTLS) to provide multi-echelon training from tactical to strategic level. This federation was established in 2008.

**JCATS-VBS Integration**: Canada completed VBS-to-JCATS integration using Calytrix Technologies' "LVC Game" gateway, enabling 100-150 personnel to participate in combined constructive-virtual exercises.

### 3.2 Scenario Generation

| Aspect | Current State |
|--------|--------------|
| **JCATS Scenarios** | Terrain databases, force structures, OPLANs defined by exercise planners |
| **SPEAR Planning** | SPEAR software includes mission planning tools for air exercises |
| **CATS Metrix** | Exercise definition including objectives, trigger events, evaluation criteria |
| **Automation** | Limited -- primarily manual scenario scripting with pre-defined event triggers |
| **Real-Time Adaptation** | JCATS allows operator intervention; CGF responds to player actions |
| **AI/ML Scenario** | NOT implemented by Cubic -- identified as emerging capability |
| **Gap for CORTEX** | **AI-driven adaptive scenario generation is a major opportunity** |

---

## 4. DATA ARCHITECTURE (Critical Section)

### 4.1 SPEAR CDM (Common Data Model)

**SPEAR** = **S**implified, **P**lanning, **E**xecution, **A**nalysis, **R**econstruction

| Parameter | Specification |
|-----------|--------------|
| **Introduced** | ~2019-2020 (first spec sheets); operational demonstrations 2022+ |
| **Type** | Common Data Model (CDM) and software platform |
| **Purpose** | Integrate, visualize, and analyze multi-domain, multi-environment data throughout entire mission cycle |
| **Phases Covered** | Planning -> Execution (real-time) -> Analysis (post-mission) -> Reconstruction (debrief) |
| **First Academy** | April 2025 (inaugural SPEAR Academy announced) |
| **Customers** | USAF (Cope North, Checkered Flag, Red Flag), USN (Valiant Shield 2024), RAAF (Tasman Shield, Cobra Warrior) |

**SPEAR Supported Data Formats** (confirmed from Cubic's website):

| Format | Type | Domain |
|--------|------|--------|
| ADSB | Automatic Dependent Surveillance - Broadcast | Air tracking |
| AIS | Automatic Identification System | Maritime tracking |
| ASTERIX | All Purpose Structured Eurocontrol Surveillance Information Exchange | Radar/surveillance |
| DAT | Cubic proprietary data format | Legacy P5 data |
| DIS | Distributed Interactive Simulation (IEEE 1278) | Simulation standard |
| DIS Audio | DIS Audio PDUs | Voice comms |
| EAG | Electronic Attack Group data | EW domain |
| Garmin | Garmin GPS track format | GPS tracks |
| Generic Tracks | Configurable track format | Multiple |
| GPS | Raw GPS data (NMEA or similar) | Position |
| GPX | GPS Exchange Format | Position tracks |
| JMPS | Joint Mission Planning System | Mission planning |
| KML | Keyhole Markup Language | Geospatial |
| Link 16 | Tactical data link (MIL-STD-6016) | Multi-domain C2 |
| P5 | Cubic P5CTS native format | ACMI data |
| P5e | P5 encrypted format | Encrypted ACMI |
| SoW | Statement of Work format (likely scenario definition) | Planning |
| TENA | Test and Training Enabling Architecture | Range integration |
| TLE | Two-Line Element (satellite orbital) | Space domain |

**SPEAR Architecture Analysis**:

```
SPEAR Common Data Model Architecture:

+------------------------------------------------------------------+
|                    DATA INGESTION LAYER                            |
|  +--------+ +------+ +-----+ +------+ +-------+ +-----+ +------+ |
|  | ADSB   | | AIS  | | DIS | | Link | | P5/   | | GPS | | TENA | |
|  |        | |      | |     | | 16   | | P5e   | |     | |      | |
|  +---+----+ +--+---+ +--+--+ +--+---+ +---+---+ +--+--+ +--+---+ |
|      |         |        |       |         |        |        |      |
+------+---------+--------+-------+---------+--------+--------+-----+
                          |
                          v
+------------------------------------------------------------------+
|              SPEAR NORMALIZATION ENGINE                            |
|  - Protocol-specific parsers                                      |
|  - Timestamp synchronization (GPS time reference)                 |
|  - Coordinate system normalization (WGS-84)                       |
|  - Entity correlation (same entity across sources)                |
|  - Event classification and tagging                               |
|  - Lossless data archival                                         |
+------------------------------------------------------------------+
                          |
                          v
+------------------------------------------------------------------+
|              SPEAR COMMON DATA MODEL (CDM)                        |
|  Unified representation of:                                       |
|  - Entity tracks (air, ground, surface, subsurface, space)        |
|  - Engagement events (fire, detonation, kill, damage)             |
|  - Sensor events (detection, track, classification)               |
|  - Communication events (voice, data, Link 16)                    |
|  - Environmental data (weather, terrain)                          |
|  - Kinetic AND non-kinetic effects                                |
|  - Objective AND subjective data                                  |
+------------------------------------------------------------------+
                          |
                 +--------+--------+
                 |                 |
                 v                 v
+------------------+  +------------------------+
| EXECUTION VIEW   |  | ANALYSIS / RECON VIEW  |
| (Real-Time)      |  | (Post-Mission)         |
| - Live COP       |  | - 2D/3D playback       |
| - Exercise ctrl  |  | - Event timeline       |
| - Player status  |  | - Performance metrics  |
| - Alert/notify   |  | - "Speed to insight"   |
+------------------+  | - 90-min debrief saved |
                      +------------------------+
```

**How SPEAR Differs from DIS/HLA PDUs**:

| Aspect | DIS/HLA | SPEAR CDM |
|--------|---------|-----------|
| **Scope** | Single protocol standard | Multi-protocol aggregation |
| **Data Model** | Entity State PDUs, Fire/Detonation PDUs | Unified event + entity + effects model |
| **Time** | Per-protocol timestamps | Synchronized cross-source timeline |
| **Analysis** | Not included (separate tools) | Built-in analytics and visualization |
| **AI/ML Ready** | Raw PDU streams | Normalized, tagged, queryable data |
| **Archival** | Not standardized | Lossless archival with metadata |
| **Openness** | Open standards | **Proprietary Cubic format** |

**AI/ML Readiness Claims**:
- SPEAR's architecture "allows the lossless export of LVC data, including kinetic and non-kinetic effects"
- "Enriched data supports performance analytics, readiness assessments, and AI/ML algorithms"
- However: No public documentation of actual AI/ML features implemented -- this appears to be **aspirational positioning** rather than deployed capability

**Is SPEAR Open or Proprietary?**
- **Proprietary**. SPEAR is a Cubic commercial product sold under license
- RAAF contract specifically includes "SPEAR software licenses and hardware"
- No open-source components, no published API, no third-party integration SDK
- **This is a critical vulnerability for CORTEX to exploit**

### 4.2 CATS Metrix (Command and Analysis Training System)

| Parameter | Specification |
|-----------|--------------|
| **Type** | PC-compatible EXCON/AAR software |
| **Primary Use** | Ground force-on-force training |
| **Deployed** | Swedish Land Warfare Centre (Exercise Aurora 2017, brigade-level), UK, multiple NATO nations |
| **Integration** | Works with AWES, I-MILES, GPS tracking systems |

**EXCON (Exercise Control) Capabilities**:

| Feature | Description |
|---------|-------------|
| Planning | Define exercise scenario, objectives, evaluation criteria, trigger events |
| Monitoring | Real-time 2D electronic map display of all AWES/MILES players |
| Control | Start/stop/pause exercise, inject events, override kill states |
| Communication | Controller-to-player messaging, role-play injection |
| CBRN Interface | Integrates with LCD3.3-SIM for chemical/biological threat simulation |

**AAR (After Action Review) Capabilities**:

| Feature | Description |
|---------|-------------|
| 2D Map Replay | Time-synchronized playback on electronic map/air photograph |
| 3D Replay | Three-dimensional terrain visualization with entity movement |
| Timeline | Event-driven timeline with engagement markers |
| Tracking | GPS track recording and playback for all instrumented players |
| Evaluation | Assessment against defined goals, doctrines, and tactics |
| Feedback | Identifies both deficiencies AND exceptional performance |
| Recording | Complete exercise data logging for archival |

**Real-Time vs Post-Exercise**:
- **Real-time monitoring**: YES -- live GPS tracking and event display during exercise
- **Post-exercise debrief**: Full playback, analysis, and performance scoring
- **Performance scoring**: Rule-based evaluation against pre-defined tactical criteria (NOT AI/ML)

### 4.3 ICADS (Individual Combat Aircrew Display System)

| Parameter | Specification |
|-----------|--------------|
| **Type** | Windows-based aircrew combat display and debrief system |
| **Deployment** | Amphitheater setting with movie theater-size screen |
| **Real-Time** | Monitor and control exercises in progress |
| **Post-Mission** | Full debrief playback |
| **Views** | 2D, 3D, alphanumeric, DATAS view |

**ICADS Key Features**:
- Communicate with pilots during exercise
- Control simulated threats
- Fire simulated weapons
- Mission Line Up (MLU) software with thousands of weapon/threat simulations
- Firewall between range communications and ICADS network
- Live Monitor (LM) computer equipment for real-time tracking

### 4.4 Data Export and Analytics

| Aspect | Current State |
|--------|--------------|
| **Export Formats** | Proprietary SPEAR format; DIS replay files; KML for geospatial |
| **Third-Party Access** | Extremely limited -- no published API |
| **External Analytics** | Not supported -- Cubic wants analytics done within their tools |
| **Data Retention** | Local storage on EXCON servers; no cloud architecture |
| **Storage** | Traditional file-based + database; NOT cloud-native |
| **Gap for CORTEX** | **Open API, cloud-native storage, third-party analytics integration** |

---

## 5. NETWORK AND INTEGRATION

### 5.1 DIS / HLA / TENA Gateways

#### 5.1.1 DIS (Distributed Interactive Simulation) -- IEEE 1278

| Parameter | Specification |
|-----------|--------------|
| **Standard** | IEEE 1278.1-2012 |
| **Transport** | UDP broadcast/multicast on IP networks |
| **Data Unit** | Protocol Data Unit (PDU) -- 28 types in base standard |
| **Key PDUs** | Entity State, Fire, Detonation, Signal, Transmitter, Receiver |
| **Update Rate** | Dead-reckoning threshold based (not fixed rate) |
| **Typical Use** | Real-time entity simulation, weapons effects |
| **Cubic Usage** | Primary protocol for live-to-EXCON data flow; SCOPIC2 entity injection |

**Key DIS PDU Structure**:

```
Entity State PDU (most common):
+---+---+---+---+---+---+---+---+---+---+---+---+
| Header (12 bytes)                               |
|  - Protocol Version, Exercise ID, PDU Type      |
+---+---+---+---+---+---+---+---+---+---+---+---+
| Entity ID (6 bytes)                             |
|  - Site, Application, Entity                    |
+---+---+---+---+---+---+---+---+---+---+---+---+
| Force ID, Entity Type                           |
|  - Kind, Domain, Country, Category, Subcategory |
+---+---+---+---+---+---+---+---+---+---+---+---+
| Entity Location (24 bytes)                      |
|  - X, Y, Z in geocentric coordinates            |
+---+---+---+---+---+---+---+---+---+---+---+---+
| Entity Orientation (12 bytes)                   |
|  - Psi, Theta, Phi (Euler angles)               |
+---+---+---+---+---+---+---+---+---+---+---+---+
| Dead Reckoning Parameters                       |
|  - Algorithm, linear velocity, acceleration     |
+---+---+---+---+---+---+---+---+---+---+---+---+
| Entity Appearance (4 bytes)                     |
|  - Damage state, smoking, flaming, etc.         |
+---+---+---+---+---+---+---+---+---+---+---+---+
```

#### 5.1.2 HLA (High Level Architecture) -- IEEE 1516

| Parameter | Specification |
|-----------|--------------|
| **Standard** | IEEE 1516-2010 (HLA Evolved); IEEE 1516-2025 (latest) |
| **NATO** | STANAG 4603 mandates HLA compliance for new simulation procurement |
| **Key Component** | RTI (Runtime Infrastructure) -- middleware for federate communication |
| **FOM** | RPR-FOM (Real-time Platform Reference FOM) for military simulations |
| **Cubic Usage** | Federation management for multi-domain exercises; SLATE LVC integration |
| **Key Difference from DIS** | Object-oriented, supports publish/subscribe, time management, ownership transfer |

#### 5.1.3 TENA (Test and Training Enabling Architecture)

| Parameter | Specification |
|-----------|--------------|
| **Developer** | TRMC (Test Resource Management Center), DoD |
| **Purpose** | Enable interoperability among ranges, facilities, and simulations |
| **Key Tools** | TENA Middleware, TENA-DIS Gateway, TENA Repository, TENA Archive |
| **Cubic Usage** | SPEAR explicitly supports TENA as a data source |
| **Advantage** | Purpose-built for test ranges; handles range-specific instrumentation data |

**TENA-DIS Gateway** is a critical bridging device:

```
DIS Network              TENA Network
+-----------+           +-----------+
| DIS PDUs  |           | TENA Objs |
| (UDP      | <-------> | (CORBA-   |
|  multicast|  TENA-DIS |  based    |
|  )        |  Gateway  |  publish/ |
|           |           |  subscribe|
+-----------+           +-----------+
```

#### 5.1.4 Protocol Usage Matrix

| Protocol | Live | Virtual | Constructive | AAR | SPEAR |
|----------|------|---------|-------------|-----|-------|
| DIS | Primary | Primary | Supported | Replay | Ingested |
| HLA | Federation mgmt | Primary | Primary | Supported | Ingested |
| TENA | Range instr. | Rare | Rare | Archive | Ingested |
| Link 16 | Air C2 | Simulated | Simulated | Recorded | Ingested |
| MILES IR | Engagement | N/A | N/A | Via EXCON | Via EXCON |
| P5 Native | ACMI | N/A | N/A | ICADS | Ingested |

### 5.2 DTECH Edge Nodes

#### 5.2.1 DTECH Family Overview

| Parameter | Specification |
|-----------|--------------|
| **Brand** | DTECH (Digital Technology) -- Cubic's edge compute product line |
| **Division** | Cubic DTECH Mission Solutions |
| **Purpose** | Edge-to-cloud compute and networking for DDIL environments |
| **Certification** | AWS IoT Greengrass certified |

#### 5.2.2 DTECH Fusion eHPC (Edge High-Performance Compute)

| Parameter | Specification |
|-----------|--------------|
| **Introduced** | May 2024 (SOF Week) |
| **CPU** | AMD EPYC 7003, 64-core |
| **GPU** | NVIDIA RTX 5000 Ada Generation (dedicated) |
| **RAM** | 512 GB |
| **Storage** | 8-slot removable SSD drives (NVMe via Broadcom 9560-16i) |
| **Networking** | Broadcom 4-port NetExtreme 25GB + 2-port Intel X55x 10GB |
| **Management** | IPMI, 2x USB 3.0 |
| **Form Factor** | Single ruggedized transit case |
| **Power** | Battery-backed power supply |
| **OS** | Red Hat Enterprise Linux certified |
| **Capabilities** | AI, ML, video analysis, disconnected tactical-cloud, hyper-converged infrastructure |

#### 5.2.3 DTECH M3-SE

| Parameter | Specification |
|-----------|--------------|
| **Type** | Enterprise Compute and Networking platform for tactical edge |
| **Scale** | Smaller/lighter than Fusion eHPC |
| **Purpose** | Networking hub + compute at squad/platoon level |

**Edge vs Centralized Processing**:

| Processing | Location | Use Case |
|-----------|----------|----------|
| Data collection | Edge (player devices) | MILES events, GPS, sensor data |
| Protocol translation | Edge (DTECH nodes) | DIS<->HLA, format conversion |
| AI/ML inference | Edge (Fusion eHPC) | Emerging -- video analysis, pattern recognition |
| Exercise control | Centralized (EXCON) | CATS Metrix, scenario management |
| Full AAR/debrief | Centralized (SPEAR servers) | Post-mission data fusion and analysis |
| Archival | Centralized (servers) | Long-term data storage |

### 5.3 TAK Integration (TAKTICS)

| Parameter | Specification |
|-----------|--------------|
| **Product** | TAKTICS -- Cubic Digital Intelligence platform |
| **Function** | Web-based geospatial data management for TAK ecosystem |
| **Components** | Regional Nodes, Edge Nodes, AutoSync Maps |
| **Key Feature** | Quickly locate, view, download geospatial data to mobile devices |
| **TAK Integration** | Delivers imagery and maps directly to ATAK/WinTAK devices in DDIL |
| **Intelligence Feeds** | HawkEye 360 RF data and analytics (integrated May 2025) |
| **Training Use** | Provides SA layer for training exercises; maps/imagery to TAK users |

**TAKTICS in Training Context**:

```
TAKTICS Architecture for Training:

+-------------------+     +-------------------+
| Geospatial Data   |     | Training System   |
| Sources           |     | Data              |
| - Imagery         |     | - Player positions|
| - Maps            |     | - Event markers   |
| - Terrain         |     | - Blue/Red tracks |
| - RF analytics    |     |                   |
+--------+----------+     +--------+----------+
         |                         |
         v                         v
+------------------------------------------+
|          TAKTICS Platform                 |
| - Regional Nodes (enterprise)            |
| - Edge Nodes (tactical)                  |
| - AutoSync Maps (offline capable)        |
| - Web-based interface                    |
+------------------------------------------+
         |
         v
+------------------------------------------+
|          TAK Devices                      |
| - ATAK (Android)                         |
| - WinTAK (Windows)                       |
| - TAK Server (enterprise)                |
| - CoT (Cursor on Target) protocol        |
+------------------------------------------+
```

**Key Insight for CORTEX**: TAK uses **CoT (Cursor on Target)** XML format for position and event data. This is a lightweight, well-documented protocol that CORTEX should natively support.

---

## 6. CTC (Combat Training Center) ARCHITECTURE

### 6.1 NTC (National Training Center, Fort Irwin, CA)

| Parameter | Specification |
|-----------|--------------|
| **Activated** | October 16, 1980 |
| **Size** | ~1,000 sq miles (size of Rhode Island) |
| **Type** | Army's premier heavy maneuver CTC |
| **Exercise Level** | Brigade Combat Team (BCT) rotations |
| **Rotations** | Multiple per year (~10-12 annually) |
| **OPFOR** | 11th Armored Cavalry Regiment (Blackhorse) |

**NTC Instrumentation Infrastructure**:

```
NTC INSTRUMENTATION NETWORK TOPOLOGY:

+=====================================================+
|                 NTC CONTROL CENTER                   |
|  (The "Star Wars" Building)                         |
|  +-------------+ +----------+ +------------------+  |
|  | EXCON       | | AAR      | | Data Archive     |  |
|  | Workstations| | Theater  | | Servers          |  |
|  +------+------+ +----+-----+ +--------+---------+  |
|         |              |                |            |
+=========|==============|================|============+
          |              |                |
          v              v                v
+=====================================================+
|              BACKBONE NETWORK                        |
|  (Fiber optic ring + microwave links)               |
|  - High-bandwidth fiber to key facilities            |
|  - Microwave relay towers across training area       |
|  - Redundant paths for reliability                   |
+====================+================================+
                     |
        +------------+-------------+
        |            |             |
        v            v             v
+----------+  +----------+  +----------+
| Tower 1  |  | Tower 2  |  | Tower N  |
| (Radio   |  | (Radio   |  | (Radio   |
|  relay + |  |  relay + |  |  relay + |
|  GPS ref)|  |  GPS ref)|  |  GPS ref)|
+----+-----+  +----+-----+  +----+-----+
     |              |              |
     v              v              v
+=====================================================+
|              WIRELESS DATA LINKS                     |
|  - UHF/VHF radio for MILES data collection           |
|  - GPS tracking data uplink                          |
|  - Controller communications                         |
|  - Real-time player status                           |
+=====================================================+
     |              |              |
     v              v              v
+---------+  +----------+  +----------+
| Soldier |  | Vehicle  |  | Aircraft |
| I-MILES |  | CVTESS/  |  | P5CTS   |
| IWS 2   |  | VTESS    |  | (if air  |
| + GPS   |  | + GPS    |  |  integrated)
+---------+  +----------+  +----------+
```

**NTC Key Infrastructure Numbers (Estimated)**:

| Component | Approximate Quantity |
|-----------|---------------------|
| Instrumentation towers | 40-60+ across training area |
| Radio relay sites | 15-20 |
| Fiber optic backbone | 100+ miles |
| Simultaneous tracked players | 4,000-5,000+ (soldiers + vehicles) |
| OPFOR vehicles | 200+ |
| Rotational unit size | 3,500-5,500 soldiers per BCT rotation |
| Observer/Controller-Trainers | 600+ per rotation |
| Exercise duration | 14 days continuous |

### 6.2 JRTC (Joint Readiness Training Center, Fort Johnson, LA)

| Parameter | Specification |
|-----------|--------------|
| **Focus** | Light/airborne infantry, special operations |
| **Size** | Smaller maneuver area than NTC |
| **Terrain** | Forested, swamp -- GPS challenged environments |
| **Exercise Level** | BCT-level rotations |
| **Instrumentation** | Similar to NTC but adapted for light force operations |

### 6.3 JPMRC (Joint Pacific Multinational Readiness Center)

| Parameter | Specification |
|-----------|--------------|
| **Locations** | Hawaii, Alaska, Pacific theater |
| **Focus** | Pacific-specific multi-national training |
| **Status** | Newer CTC; instrumentation still being developed |
| **Significance** | Indo-Pacific focus aligns with VN defense context |

### 6.4 Infrastructure Requirements Summary

| Requirement | Typical CTC Deployment |
|-------------|----------------------|
| **Towers** | 40-60 instrumentation/relay towers |
| **Fiber** | 100+ miles fiber optic backbone |
| **Wireless** | UHF/VHF radio network + cellular backup |
| **DGPS** | Reference stations for enhanced accuracy |
| **Power** | Generator-backed sites, solar in remote areas |
| **Servers** | EXCON server farm (50+ workstations) |
| **AAR Facility** | Dedicated theater-style building |
| **Cost** | **$500M-$1B+ infrastructure investment** |
| **Annual O&M** | **$50-100M+ annually** |

---

## 7. GAPS AND OPPORTUNITIES FOR CORTEX C2 RANGE

### 7.1 Data Gaps -- What Cubic Does NOT Capture

| Gap | Description | CORTEX Opportunity |
|-----|-------------|-------------------|
| **Acoustic Data** | Cubic has NO shot detection or LOMAH capability | CORTEX RANGE with LOMAH provides miss distance, MPI, shot group data that Cubic cannot |
| **Ballistic Performance** | MILES simulates weapon effects but records ZERO actual ballistic data | CORTEX can correlate actual impact data with engagement outcomes |
| **Environmental Correlation** | Weather, wind, temperature effects on training NOT captured | CORTEX can correlate environmental conditions with performance degradation |
| **Physiological Data** | Stress, fatigue, heart rate, sleep quality NOT captured | Wearable integration (future) provides biometric performance correlation |
| **Audio/Comms Content** | DIS Audio captures metadata but not typically content analysis | NLP analysis of tactical communications for decision quality scoring |
| **Weapon Maintenance State** | No correlation between weapon condition and training performance | Maintenance data integration shows readiness degradation patterns |
| **Individual Progression** | Limited longitudinal tracking across multiple exercises | CORTEX can build individual soldier performance profiles over time |

### 7.2 Analytics Gaps

| Gap | Cubic Current State | CORTEX Advantage |
|-----|-------------------|-----------------|
| **Real-Time AI Scoring** | Rule-based, pre-defined criteria only | ML models for real-time performance assessment |
| **Predictive Readiness** | Not available | Train ML models to predict unit readiness from training data patterns |
| **Cross-Exercise Trends** | Manual comparison only | Automated trend analysis across exercises, units, time periods |
| **Individual Progression** | Not tracked longitudinally | Individual learning curves, skill decay models, personalized training plans |
| **Unit Pattern Recognition** | Manual OC/T observation | Automated tactical pattern recognition (flanking execution, fire discipline, etc.) |
| **Adaptive Difficulty** | Static scenarios | AI-driven scenario difficulty adjustment based on unit performance |
| **Natural Language Debrief** | Not available | AI-generated narrative debriefs from quantitative data |
| **Anomaly Detection** | Not available | Identify unusual patterns (safety violations, equipment failures, exceptional performance) |

### 7.3 Architecture Gaps

| Gap | Cubic Current State | CORTEX Advantage |
|-----|-------------------|-----------------|
| **Cloud-Native** | Legacy client-server; on-premise only | Cloud-native architecture, SaaS delivery |
| **Edge AI** | DTECH Fusion eHPC exists but AI features are nascent | Purpose-built edge AI from day one |
| **Open API** | No published API; proprietary data access | RESTful API, GraphQL, webhook integrations |
| **Cost** | $50M+ for CTC-scale; SPEAR licenses expensive | $15-25K per range; accessible to non-CTC ranges |
| **Deployment Complexity** | Weeks/months for installation | Hours for deployment; plug-and-play sensors |
| **Third-Party Integration** | Closed ecosystem | Open standards, plugin architecture |
| **Mobile Access** | Desktop-centric | Mobile-first AAR and analytics |

### 7.4 Integration Opportunities

#### 7.4.1 Where CORTEX RANGE Plugs into the LVC Ecosystem

```
CORTEX RANGE Integration Points:

                    EXISTING CUBIC ECOSYSTEM
+-------------------------------------------------------+
|                                                         |
|  I-MILES  -->  DIS PDUs  -->  EXCON  -->  CATS Metrix  |
|  P5CTS   -->  P5 Data   -->  SPEAR  -->  ICADS        |
|  AWES    -->  GPS Data   -->  |                        |
|                               |                        |
+===============================|========================+
                                |
                                v
              +----------------------------------+
              |    CORTEX RANGE                   |
              |    INTEGRATION LAYER              |
              |                                   |
              | INPUTS (Standard Protocols):      |
              |  - DIS PDU listener (UDP)         |
              |  - CoT XML (TAK integration)      |
              |  - NMEA GPS streams               |
              |  - TENA object subscription       |
              |  - Acoustic sensor data (LOMAH)   |
              |  - Environmental sensors           |
              |  - Video feeds                     |
              |                                   |
              | OUTPUTS:                          |
              |  - Real-time AI performance scores|
              |  - Predictive readiness metrics   |
              |  - Interactive AAR dashboards     |
              |  - REST API for third-party tools |
              |  - DIS PDU injection (feedback)   |
              |  - CoT markers to TAK            |
              |  - Cloud data warehouse           |
              +----------------------------------+
```

#### 7.4.2 Standards CORTEX MUST Support

| Standard | Priority | Rationale |
|----------|----------|-----------|
| **DIS (IEEE 1278)** | CRITICAL | Universal language of military simulation; all Cubic live systems output DIS |
| **CoT XML** | CRITICAL | TAK ecosystem is ubiquitous; ATAK/WinTAK on every soldier's phone |
| **HLA RPR-FOM** | HIGH | Required for federated exercises with virtual/constructive systems |
| **TENA** | MEDIUM | DoD test ranges use TENA; important for range integration |
| **Link 16 (simulated)** | MEDIUM | Air domain exercises use Link 16 data |
| **NMEA 0183/2000** | HIGH | Standard GPS data format; sensor data ingestion |
| **ASTERIX** | LOW | European surveillance standard; future NATO interop |
| **KML/GPX** | HIGH | Geospatial data import/export for planning and replay |
| **ADSB/AIS** | LOW | Air/maritime tracking; future multi-domain |

#### 7.4.3 CORTEX as "Smart Analytics Layer"

The highest-value positioning for CORTEX RANGE is as a **"smart analytics layer" that sits on top of existing infrastructure** -- whether that's Cubic, Saab, or any other training system that outputs standard protocols.

```
Value Proposition:

EXISTING RANGE                    CORTEX RANGE
(Any vendor)                      (Analytics Layer)

+--------------+                  +------------------+
| MILES/TESS   |   DIS PDUs      | AI/ML Engine     |
| GPS Tracking | =============>  | - Performance     |
| Engagement   |   CoT XML       |   scoring         |
| Data         |   NMEA GPS      | - Pattern recog   |
|              |                  | - Predictive      |
+--------------+                  |   readiness       |
                                  | - Trend analysis  |
                                  | - Natural language|
                                  |   debrief         |
                                  +------------------+
                                         |
                                         v
                                  +------------------+
                                  | CORTEX Dashboard |
                                  | - Web/Mobile     |
                                  | - Real-time      |
                                  | - Historical     |
                                  | - API access     |
                                  +------------------+
```

#### 7.4.4 CORTEX DIS/HLA Adapter Design Concept

```
CORTEX Protocol Adapter Stack:

+-------------------------------------------+
|           CORTEX APPLICATION LAYER         |
|  (AI/ML Analytics, Dashboard, API)        |
+-------------------------------------------+
|           CORTEX DATA MODEL               |
|  (Normalized entity + event store)        |
+-------------------------------------------+
|           ADAPTER LAYER                   |
|  +--------+ +--------+ +--------+        |
|  |  DIS   | |  HLA   | |  CoT   |        |
|  | Adapter| | Adapter| | Adapter|        |
|  +--------+ +--------+ +--------+        |
|  +--------+ +--------+ +--------+        |
|  | TENA   | | NMEA   | | Custom |        |
|  | Adapter| | Adapter| | Plugin |        |
|  +--------+ +--------+ +--------+        |
+-------------------------------------------+
|           TRANSPORT LAYER                 |
|  UDP Multicast | TCP | WebSocket | MQTT   |
+-------------------------------------------+

DIS Adapter Implementation:
  - Listen on UDP port 3000 (default DIS)
  - Parse PDU headers (protocol version, PDU type)
  - Decode Entity State PDUs -> CORTEX Entity objects
  - Decode Fire/Detonation PDUs -> CORTEX Event objects
  - Convert geocentric coords -> WGS-84 lat/lon/alt
  - Apply dead-reckoning between updates
  - Timestamp synchronization with GPS reference

Estimated Development: 2-3 weeks for basic DIS adapter
Open-Source Options: Open-DIS (Java/C++/JavaScript/Python)
  - https://github.com/open-dis
  - IEEE binary and XML format support
  - Battle-tested in multiple military projects
```

---

## 8. DESIGN PARADIGM ANALYSIS

### 8.1 Cubic's Design Philosophy

| Principle | Description |
|-----------|-------------|
| **Hardware-First** | Products defined by physical systems (pods, harnesses, lasers, GPS units); software wraps hardware |
| **Protocol-Heavy** | Deep investment in DIS, HLA, TENA compliance; interoperability through standards bodies |
| **Centralized AAR** | All data flows to central EXCON facility; analysis happens post-mission in dedicated buildings |
| **Proprietary Lock-In** | SPEAR CDM, CATS Metrix, ICADS are all closed systems requiring Cubic licenses |
| **Government Contract** | Designed for large government programs ($50M+ contracts); not commercial-viable |
| **Managed Service** | Revenue from multi-year support contracts (SCOPIC2 = 4-year managed service) |
| **Encryption Priority** | Significant investment in Type-1 encryption (NSA-certified) for classified training data |
| **Multi-Domain Aspiration** | Moving from single-domain (ground OR air) to multi-domain integration |

### 8.2 CORTEX RANGE Design Philosophy

| Principle | Description |
|-----------|-------------|
| **AI-First** | Analytics engine is the core product; sensors are commoditized inputs |
| **Data-Native** | Born in the era of ML/cloud; data model designed for analytics from day one |
| **Real-Time Analytics** | Performance scoring happens DURING training, not just after |
| **Edge Processing** | AI inference at the range level; cloud for aggregation and long-term analytics |
| **Open Architecture** | REST API, standard protocols, plugin system for third-party integration |
| **Commercial-Viable** | $15-25K price point makes advanced analytics accessible to ANY range |
| **Acoustic Foundation** | LOMAH acoustic data provides ground truth that Cubic's laser-only systems cannot |
| **Rapid Deployment** | Hours, not months; no infrastructure construction required |

### 8.3 Where Philosophies Conflict

| Area | Cubic | CORTEX | Tension |
|------|-------|--------|---------|
| **Data Ownership** | Cubic controls data in proprietary formats | Open data, user-owned | Cubic will resist data export to CORTEX |
| **Analytics** | Post-mission, manual interpretation | Real-time, AI-driven | CORTEX shows results Cubic can't match |
| **Cost Model** | Large contracts, managed service | Product purchase, SaaS analytics | Threatens Cubic's recurring revenue |
| **Deployment** | CTC-scale infrastructure required | Plug-and-play at any range | CORTEX serves markets Cubic ignores |
| **Integration** | Closed ecosystem preference | Open integration | CORTEX can work with any vendor, Cubic can't easily reciprocate |

### 8.4 Where They Can Complement

| Area | How |
|------|-----|
| **Analytics Layer** | CORTEX ingests DIS data from Cubic-instrumented ranges, providing AI analytics that Cubic doesn't offer |
| **Non-CTC Ranges** | Cubic focuses on CTC; CORTEX serves home station ranges, allied nation ranges, and commercial shooting ranges |
| **Acoustic Gap** | CORTEX LOMAH provides miss-distance data that enhances Cubic's engagement simulation (complementary, not competitive) |
| **Cloud Archival** | CORTEX's cloud platform can archive training data that Cubic currently stores only locally |
| **Multinational** | CORTEX can bridge between Cubic-equipped forces and non-Cubic equipped forces in multinational exercises |

---

## 9. KEY COMPETITIVE INTELLIGENCE SUMMARY

### 9.1 Cubic's Revenue and Market Position

| Metric | Value |
|--------|-------|
| **Acquisition** | Veritas Capital + Evergreen Coast Capital, 2021, ~$3B |
| **Status** | Private (no longer NYSE: CUB) |
| **Training Revenue** | Estimated $800M-1B annually (across all training divisions) |
| **Market Position** | #1 globally in live training instrumentation; top 3 in ACMI |
| **Key Competitors** | Saab (CVTESS/VTESS), Leonardo DRS (F-35 P5), CAE (virtual), L3Harris, Raytheon |
| **Partnerships** | CAE (NXTGEN8), Boeing (SITL), Leonardo DRS (F-35 ACMI) |

### 9.2 Recent Strategic Moves (2024-2026)

| Date | Event | Significance |
|------|-------|-------------|
| May 2024 | DTECH Fusion eHPC launched | Edge AI capability for first time |
| Jul 2024 | Valiant Shield 2024 with ATE | Multi-domain LVC at exercise scale |
| Nov 2024 | I/ITSEC 2024 showcases | ATE, SPEAR, CTSS, LTS on display |
| Feb 2025 | Singapore Airshow 2026 | P5 SSU, CIL, SPEAR showcased |
| Mar 2025 | Cope North '25 | SPEAR CDM deployed with 4th/5th gen ACMI |
| Apr 2025 | SPEAR Academy launched | Formalizing SPEAR as training platform standard |
| May 2025 | First encrypted ACMI for 4th gen | SSU kits delivered to USAF |
| May 2025 | TAKTICS + HawkEye 360 | Intelligence feeds into TAK ecosystem |
| Jul 2025 | UK ILT-A contract won | SCOPIC2 + live fire + RPAS integration |
| Aug 2025 | 102 new P5CTS pods + SSU | Major USAF production order |

### 9.3 Technology Readiness Assessment

| Technology | TRL | Status |
|-----------|-----|--------|
| I-MILES IWS 2 | 9 | Fielded, production |
| P5CTS ACMI | 9 | Fielded, production |
| P5 SSU (encryption) | 8-9 | First deliveries 2025 |
| SLATE LVC | 7+ | Validated in operational aircraft |
| SPEAR CDM | 7-8 | Deployed at major exercises |
| SCOPIC2 | 9 | In-service with British Army |
| DTECH Fusion eHPC | 7 | AWS certified; field deployments |
| CATS Metrix | 9 | Fielded globally |
| AI/ML Analytics | 3-4 | **Aspirational; not deployed** |
| Cloud-Native | 2-3 | **Not implemented** |

---

## 10. CRITICAL INTEGRATION REQUIREMENTS FOR CORTEX RANGE

### 10.1 Minimum Viable Protocol Support (Phase 1)

| Protocol | Library/Tool | Effort | Priority |
|----------|-------------|--------|----------|
| DIS (IEEE 1278) | Open-DIS (open source) | 2-3 weeks | Must-have |
| CoT XML (TAK) | FreeTAKServer or custom parser | 1-2 weeks | Must-have |
| NMEA GPS | Standard serial parser | 1 week | Must-have |
| KML/GPX import | GDAL/OGR or custom | 1 week | Should-have |

### 10.2 Extended Protocol Support (Phase 2)

| Protocol | Library/Tool | Effort | Priority |
|----------|-------------|--------|----------|
| HLA RPR-FOM | Pitch RTI or MAK RTI (commercial) | 4-6 weeks | Should-have |
| TENA | TENA Middleware (gov't provided) | 3-4 weeks | Could-have |
| Link 16 (simulated) | Custom parser for SIMPLE/JREAP | 2-3 weeks | Could-have |
| ASTERIX | Open-source ASTERIX library | 2 weeks | Future |

### 10.3 Data Model Requirements

CORTEX RANGE's internal data model should be a **superset** of what DIS/HLA/SPEAR capture, with additions for:

```
CORTEX Data Model (Conceptual):

Entity {
  id: UUID
  type: EntityType (soldier, vehicle, aircraft, target)
  force: ForceID (blue, red, white, neutral)
  position: {
    lat: float64 (WGS-84)
    lon: float64
    alt: float64
    accuracy: float32 (CEP meters)
    source: PositionSource (GPS, UWB, acoustic, manual)
  }
  velocity: Vector3D
  orientation: EulerAngles
  status: EntityStatus (active, killed, wounded, disabled)
  equipment: [EquipmentState]
  timestamp: int64 (epoch nanoseconds, GPS synchronized)
  source_protocol: Protocol (DIS, CoT, NMEA, MILES, custom)
}

Engagement {
  id: UUID
  timestamp: int64
  shooter: EntityRef
  target: EntityRef
  weapon_type: WeaponType
  result: EngagementResult (kill, near_miss, miss, suppress)

  // CORTEX ADDITIONS (not in Cubic):
  acoustic_data: {
    shot_detected: bool
    miss_distance_m: float32      // From LOMAH
    mpi_offset: Vector2D          // Mean Point of Impact offset
    shot_group_size_moa: float32  // Group size
    muzzle_velocity_mps: float32  // If measured
    time_of_flight_ms: float32    // Acoustic TOF
  }
  environmental: {
    wind_speed_mps: float32
    wind_direction_deg: float32
    temperature_c: float32
    humidity_pct: float32
    pressure_hpa: float32
    visibility_m: float32
  }
  ai_assessment: {
    performance_score: float32    // 0-100 AI computed
    technique_quality: string     // AI classification
    improvement_suggestion: string // AI generated
    anomaly_flags: [string]       // Safety, equipment, etc.
  }
}

Exercise {
  id: UUID
  name: string
  type: ExerciseType (marksmanship, force_on_force, CQB, etc.)
  start_time: int64
  end_time: int64
  entities: [Entity]
  engagements: [Engagement]
  objectives: [Objective]

  // CORTEX ANALYTICS (not in Cubic):
  ai_summary: {
    unit_performance_score: float32
    readiness_assessment: ReadinessLevel
    key_findings: [string]
    improvement_priorities: [string]
    trend_vs_previous: TrendDirection
    predicted_readiness_30d: float32
  }
}
```

---

## 11. CONCLUSIONS AND STRATEGIC RECOMMENDATIONS

### 11.1 Key Takeaways

1. **Cubic dominates live training instrumentation** but their analytics are rule-based and post-mission. There is a massive gap for AI-driven, real-time analytics.

2. **SPEAR CDM is proprietary** and expensive. CORTEX should build an open equivalent that ingests the same standard protocols (DIS, HLA, TENA, CoT) but provides superior analytics.

3. **Acoustic data is Cubic's blind spot**. They simulate engagement outcomes with lasers but capture ZERO actual ballistic data. CORTEX RANGE's LOMAH capability provides ground truth data that fundamentally enhances training value.

4. **The CTC market is Cubic's fortress** (~$500M+ infrastructure investment, sole-source contracts). CORTEX should NOT compete at CTC scale but instead target the **vastly larger market of non-CTC ranges** (home station, allied nations, commercial).

5. **DIS (IEEE 1278) is the lingua franca** of military simulation. CORTEX MUST support DIS natively. Open-DIS provides a solid open-source foundation.

6. **TAK/CoT is the emerging common operating picture** for ground forces. CORTEX should integrate with TAK from day one.

7. **Cloud-native is Cubic's weakness**. Their architecture is on-premise, server-based. CORTEX's cloud-native approach enables capabilities (cross-exercise analytics, institutional learning, ML model training) that Cubic cannot match without a fundamental re-architecture.

8. **Edge AI is nascent at Cubic**. Their DTECH Fusion eHPC is AWS-certified but AI features are aspirational. CORTEX can deliver edge AI capabilities faster because it is built from scratch for this purpose.

### 11.2 CORTEX RANGE Development Priorities

| Priority | Action | Timeline |
|----------|--------|----------|
| **P0** | DIS adapter (Open-DIS based) | Sprint 1-2 |
| **P0** | CoT/TAK adapter | Sprint 1-2 |
| **P0** | CORTEX data model (superset of DIS+acoustic) | Sprint 1 |
| **P1** | LOMAH acoustic sensor integration | Sprint 2-4 |
| **P1** | Real-time performance scoring engine | Sprint 3-6 |
| **P1** | Web dashboard (React/map-based) | Sprint 2-6 |
| **P2** | AI/ML training data pipeline | Sprint 4-8 |
| **P2** | REST API for third-party integration | Sprint 4-6 |
| **P2** | Cross-exercise trend analytics | Sprint 6-10 |
| **P3** | HLA adapter | Sprint 8-12 |
| **P3** | Predictive readiness models | Sprint 10-16 |
| **P3** | Natural language debrief generation | Sprint 12-18 |

### 11.3 Competitive Positioning Statement

> **CORTEX RANGE delivers AI-driven training analytics at 1/1000th the cost of a Combat Training Center, providing real-time performance scoring, acoustic ground truth, and predictive readiness -- capabilities that even Cubic's $500M CTC installations cannot match.**

---

## Appendix A: Glossary

| Acronym | Full Name |
|---------|-----------|
| ACMI | Air Combat Maneuvering Instrumentation |
| ATAK | Android Team Awareness Kit |
| ATE | Advanced Training Environment |
| AWES | Area Weapons Effects Simulation |
| BCT | Brigade Combat Team |
| CATS | Combined Arms Training Simulation (also Command and Analysis Training System) |
| CDM | Common Data Model |
| CGF | Computer-Generated Forces |
| CoT | Cursor on Target |
| CTC | Combat Training Center |
| CVTESS | Combat Vehicle Tactical Engagement Simulation System |
| DDIL | Denied, Disrupted, Intermittent, Limited |
| DIS | Distributed Interactive Simulation |
| DMON | Distributed Missions Operations Network |
| DTECH | Digital Technology (Cubic brand) |
| eHPC | Edge High-Performance Compute |
| EXCON | Exercise Control |
| FOM | Federation Object Model |
| HCU | Harness Control Unit |
| HLA | High Level Architecture |
| I-MILES | Instrumentable Multiple Integrated Laser Engagement System |
| ICADS | Individual Combat Aircrew Display System |
| ILT-A | Integrated Live Training - Area Weapons Effects |
| JCATS | Joint Conflict and Tactical Simulation |
| JRTC | Joint Readiness Training Center |
| JTLS | Joint Theater Level Simulation |
| LFE | Large Force Employment |
| LLNL | Lawrence Livermore National Laboratory |
| LOMAH | Location of Miss and Hit |
| LVC | Live, Virtual, Constructive |
| MILS | Multiple Independent Levels of Security |
| MILES | Multiple Integrated Laser Engagement System |
| MLU | Mission Line Up |
| NCTE | Navy Continuous Training Environment |
| NTC | National Training Center |
| NXTGEN8 | Next Generation Advanced Training Environment (Cubic + CAE) |
| P5CTS | P5 Combat Training System |
| PDU | Protocol Data Unit |
| PK | Probability of Kill |
| RPR-FOM | Real-time Platform Reference Federation Object Model |
| RPAS | Remotely Piloted Air Systems |
| RTI | Runtime Infrastructure |
| SAT | Small Arms Transmitter |
| SCOPIC | Synthetic Combined Operations Picture Integrated Capability |
| SITL | Synthetic Inject to Live |
| SLATE | Secure LVC Advanced Training Environment |
| SPEAR | Simplified Planning Execution Analysis Reconstruction |
| SSU | System Security Upgrade |
| TAK | Team Awareness Kit / Tactical Assault Kit |
| TAKTICS | Cubic TAK integration platform |
| TDTD | (Tactical Data Transfer Device) |
| TENA | Test and Training Enabling Architecture |
| TSPI | Time Space Position Information |
| VTESS | Vehicle Tactical Engagement Simulation System |

## Appendix B: Key Sources

| Source | URL | Content |
|--------|-----|---------|
| Cubic LVC Overview | cubic.com/live-virtual-constructive-lvc | SLATE, SITL-LVC specifications |
| Cubic SPEAR | cubic.com/spear | SPEAR CDM data sources, features |
| Cubic EXCON/AAR | cubic.com/solutions/training/ground/excon-aar-analysis | CATS Metrix capabilities |
| Cubic ACMI | cubic.com/industries/training/air-combat/acmi | P5CTS system overview |
| Cubic LVC Whitepaper | cubic.com (2019 PDF) | Architecture, SLATE ATD, encryption |
| MILES Wikipedia | en.wikipedia.org | MILES protocol history, CVTESS by Saab |
| MILES IWS Operator Manual | TM 23-6920-706-10 Rev 9 | HCU operation, IR data, MILES codes |
| MILES IWS Performance Spec | PRF-PT-00434B / PRF-PT-00543B | PK tables, MILES code 35, display format |
| FAS MILES Overview | man.fas.org | MILES 2000 pulse format, player ID encoding |
| JCATS LLNL | csl.llnl.gov | JCATS capabilities, LVC-IA integration |
| Open-DIS Tutorial | open-dis.github.io | DIS protocol details, PDU structure |
| DIS Wikipedia | en.wikipedia.org | IEEE 1278, RPR-FOM, protocol comparison |
| TENA Overview | tena-sda.org | TENA architecture, gateway tools |
| Cubic DTECH Fusion eHPC | cubic.com datasheet | 64-core AMD, RTX 5000, specifications |
| Leonardo DRS P5CTS | leonardodrs.com | F-35 internal subsystem, 150+ deliveries |
| Cubic SSU Delivery | Multiple press releases (May 2025) | First encrypted 4th-gen ACMI to USAF |
| Cubic ILT-A Contract | Newswire (Jul 2025) | UK MoD, SCOPIC2 integration |
| Cubic SPEAR Academy | Newswire (Apr 2025) | Inaugural SPEAR training program |
| NTC Wikipedia | en.wikipedia.org | NTC history, instrumentation approach |
| NCTE Overview | navy.mil, defense.info | Navy LVC network, 1200+ nodes |

---

*Analysis prepared for CORTEX-C2 project, Phase 0 (Market Analysis and Architecture Definition). This document should be updated as new information becomes available from industry conferences (I/ITSEC 2026), contract announcements, and technical publications.*
