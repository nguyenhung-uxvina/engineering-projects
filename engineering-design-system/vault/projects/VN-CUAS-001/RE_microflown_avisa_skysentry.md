---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Microflown AVISA SKYSENTRY (Netherlands)
version: 1.0
created: 2026-02-08
status: complete
---

# RE: Microflown AVISA SKYSENTRY - Netherlands
## Reverse Engineering Analysis from Public Sources

> **KEY DISTINCTION:** SKYSENTRY is built on a **fundamentally different sensing physics** from all other C-UAS acoustic systems analyzed. While Squarehead, BeephoniX, and GA-EMS Fencepost use conventional microphones (sound pressure sensors) in array configurations to achieve directionality, Microflown AVISA uses the world's first and only **Acoustic Vector Sensor (AVS)** — a MEMS transducer that directly measures **acoustic particle velocity** rather than sound pressure. This gives each sensor inherent **broadband directionality from a single point**, eliminating the need for large microphone arrays. The result is a remarkably compact, lightweight system: four small AMMS sensors on a CASTLE post provide **full hemispherical coverage** across the entire audio bandwidth. Detection ranges are **250m for a 2 kg quadcopter**, **1 km for a 2 kg fixed-wing drone**, and **10 km for manned helicopters** — all from a single CASTLE post deployed by one person in under 10 minutes. The same hardware platform runs different firmware for different missions: C-UAS (SKYSENTRY), counter-battery (MSRA), vehicle protection (ACLOGUS), and more — making CASTLE a true **firmware-defined multi-mission** acoustic platform. Combat-proven with Netherlands Special Forces in Mali (MINUSMA), sold to at least 3 European countries, and participating in the EDF-2023 WHATSUP C-UAS project, Microflown AVISA represents a **physics-first** approach to acoustic sensing: invent a better sensor, then build the system around it.

---

## 1. COMPANY PROFILE

### 1.1 Corporate Structure — Two Companies, One Technology

Microflown operates as two distinct entities sharing the same foundational MEMS sensor technology:

| Item | Microflown Technologies | Microflown AVISA |
|------|------------------------|------------------|
| **Founded** | 1998 | 2011 |
| **Founders** | Hans-Elias de Bree & Alex Koers | Alex Koers |
| **HQ** | Arnhem, Gelderland, Netherlands | Tivolilaan 205, 6824 BV Arnhem, Netherlands |
| **Focus** | Commercial acoustic testing & measurement | Defense & security applications |
| **Revenue** | N/A | ~$5M (estimated) |
| **Employees** | ~30 (estimated) | ~18 |
| **Products** | Acoustic probes, sensors, testing services (automotive, industrial) | CASTLE platform, SKYSENTRY, MSRA, V-AMMS, ACLOGUS |
| **Customers** | Major automotive OEMs (interior sound quality) | NATO militaries, European defense ministries |
| **Ownership** | Private | Private |

### 1.2 Key Personnel

| Name | Role | Significance |
|------|------|-------------|
| **Hans-Elias de Bree** | Co-Founder, Microflown Technologies | Invented the Microflown particle velocity sensor (1994) at University of Twente. PhD on the technology. The core scientific innovator. |
| **Alex Koers** | Co-Founder & Director, both companies | Business leader. Co-founded Microflown Technologies (1998), then spun off Microflown AVISA (2011) for defense markets. |
| **Martijn van Veldhuizen** | Business Development Manager, AVISA | Defense market development and partnerships |
| **Lisanne Wilbrink** | Controller, AVISA | Financial operations |

### 1.3 Historical Timeline

| Year | Event |
|------|-------|
| 1994 | **Hans-Elias de Bree invents the Microflown sensor** at University of Twente — world's first acoustic particle velocity sensor |
| 1994-2004 | Microflown sensor generates hundreds of scientific papers; hot topic in acoustics research |
| 1998 | **Microflown Technologies founded** by de Bree and Koers; commercialization begins |
| 2001-2002 | First assembled 3D Acoustic Vector Sensor (AVS) becomes available |
| ~2004 | Sensor becomes widely accepted, primarily in automotive industry |
| 2006 | **Monolithic AVS chip**: 3D particle velocity + sound pressure on single chip (5x5x5mm) |
| 2011 | **Microflown AVISA founded** as defense/security spin-off by Alex Koers |
| 2012 | Acoustic Vector Sensors mounted on unmanned aircraft (UAV-based acoustic ISR) |
| 2013 Jun | **ACHOFILO**: AVS tested on Dutch AS532U2 COUGAR Mk2 helicopter (live fire) |
| ~2014 | WHELAC project: V-AMMS developed for vehicle-mounted gunshot localization |
| 2014 | **NSS 2014**: Networked AMMS used for sniper protection at Nuclear Security Summit, Amsterdam Schiphol |
| 2015 Jan | **9 V-AMMS sets delivered to Netherlands Special Forces** for Mali (MINUSMA) deployment |
| 2015 | **Combat proven**: V-AMMS operational for 6 months on SOF vehicles in Mali |
| 2015 | MilTech article: "Microflown AVISA Creates Acoustic Awareness" — comprehensive technology showcase |
| 2015 Sep | **Miniaturised AMMS**: IP67 helmet-mounted sensor node first tested |
| 2015 | SKYSENTRY C-UAS capability demonstrations in "several Western countries" |
| 2015 | Sold to 3 European countries (V-AMMS); UAV-based systems sold to Asian customer |
| 2018 | **Danish tender won**: Acoustic gunshot localization for Oksbol artillery range via partner PTD |
| ~2020s | CASTLE platform matures; firmware-defined multi-mission capabilities expand |
| 2023 | **EDF WHATSUP**: Microflown AVISA seeks partners for European Defence Fund C-UAS project |
| 2024-2025 | Continued SKYSENTRY development; CASTLE platform product line expansion |

### 1.4 Business Model

| Aspect | Detail |
|--------|--------|
| **Core IP** | Patented MEMS particle velocity sensor — sole global manufacturer |
| **Revenue Model** | Hardware sales (CASTLE, AMMS units) + firmware licenses per capability |
| **Competitive Moat** | Only company in the world with acoustic particle velocity MEMS sensors — no direct competitors for the core transducer |
| **Market Position** | Niche, high-technology, low-volume defense supplier |
| **Channel** | Direct + sales offices (Germany, UK, USA) + distributors (MSS Defence, PTD Denmark, Adams Engineering India) |
| **Growth Strategy** | Platform expansion: same CASTLE hardware, new firmware-defined missions |
| **Funding** | Primarily Dutch MoD R&D contracts (WHELAC, ACHOFILO, FLACOUSE, Loose Track, Walking Ears) |

> **Business model insight:** Microflown AVISA has the deepest physics moat of any system analyzed — they invented and are the sole manufacturer of an entirely new class of acoustic sensor. Their competitive advantage is not in algorithms (Mind Foundry), arrays (Squarehead/BeephoniX), or institutional scale (GA-EMS) — it is in the **sensor physics itself**. No competitor can replicate the AVS without the Microflown transducer or equivalent IP. However, the company remains small (~$5M, 18 employees) and has not achieved the commercial scale of DroneShield (A$2.9B market cap) or institutional backing of GA-EMS ($3.2B parent). The firmware-defined multi-mission model is strategically sound — one hardware sale enables recurring firmware revenue.

---

## 2. PRODUCT FAMILY

### 2.1 Core Sensor — AMMS (Acoustic Multi Mission Sensor)

| Specification | Detail |
|---------------|--------|
| **Product** | AMMS (Acoustic Multi Mission Sensor) |
| **Core Sensing** | 2 orthogonal Microflown transducers + 1 microphone |
| **Diameter** | 30 cm (standard) or 23 cm (compact) |
| **Weight** | 1.75 kg (V-AMMS configuration) |
| **Power** | <2W |
| **Components** | Sensor node, electronics, DSP, sheet metal housing, open foam wind cap |
| **Directionality** | Inherent broadband, figure-of-eight pattern per Microflown transducer |
| **Frequency** | Full acoustic bandwidth (~20 Hz to 14 kHz) |
| **Key Feature** | Multi-mission: same hardware, different firmware defines capability |

### 2.2 Platform — CASTLE (Sensor Post)

| Specification | Detail |
|---------------|--------|
| **Product** | CASTLE (ground-based sensor post) |
| **Composition** | 4 hard-wired AMMSs + Acoustic Master (AMR) + weather station |
| **Navigation** | 2 satellite receivers (position + heading); anti-jamming/anti-spoofing optional |
| **Coverage** | Full hemispherical "field of view" (360° azimuth, 0-90° elevation) |
| **Processing** | High local signal processing; minimized network bandwidth |
| **Networking** | Radio networked and/or hard-wired between CASTLE posts |
| **Deployment** | <10 minutes by one person; covert shape |
| **Operation** | Passive, all-weather, no line-of-sight required, day/night, unattended |
| **Cannot be** | Jammed (passive acoustic — no RF emissions) |
| **Mounting** | Ground-based (tripod/stake) or vehicle-mounted |

### 2.3 SKYSENTRY (C-UAS Firmware)

| Specification | Detail |
|---------------|--------|
| **Product** | SKYSENTRY |
| **Type** | C-UAS detection, localization, and tracking |
| **Platform** | CASTLE sensor post |
| **Detection Range** | **250 m** (2 kg quadcopter) |
| | **1 km** (2 kg fixed-wing drone) |
| | **10 km** (manned helicopter) |
| **Coverage** | Full hemispherical acoustic "bubble" per CASTLE |
| **Processing** | Frequency bin analysis with DoA per frequency bin |
| **Networking** | Multiple CASTLEs create 3D spatial coverage |
| **Targets** | Multi-copters, fixed-wing propeller UAVs, helicopters, propeller aircraft |
| **Deployment** | <10 min per CASTLE post by one person |
| **Operation** | Passive, all-weather, NLOS, unattended |

### 2.4 Full Product Line (Firmware-Defined Missions)

| Product | Mission | Platform | Key Capability |
|---------|---------|----------|----------------|
| **SKYSENTRY** | Counter-UAS | CASTLE | Drone detection, localization, tracking |
| **MSRA** | Counter-battery (C-RAM) | CASTLE | Rocket, artillery, mortar detection (POI + POO) |
| **ATILS** | Target impact localization | CASTLE | Artillery range scoring |
| **ACLOGUS** | Vehicle survivability | V-AMMS | On-the-move gunshot localization |
| **V-AMMS** | Vehicle-mounted gunshot | Vehicle mount | Small arms fire detection, 120° sector + precise DoA |
| **ACHOFILO** | Helicopter hostile fire | Airborne | Hostile fire alert + shooter location for helicopters |
| **FLACOUSE / Acoustic Pointer** | UAV-mounted acoustic ISR | Fixed-wing UAV | <150g, <100mW, acoustic target acquisition + hear-and-avoid |
| **Perch and Listen** | Deployable ISR | Multicopter + AMMS | 5 kg, 21 min endurance, 7.5 km range, forward-deployed acoustic ISR |
| **Walking Ears** | Dismounted soldier | Helmet-mounted | IP67 miniaturized AMMS, squad/platoon situational awareness |
| **360° Mobile Force Protection** | Base/outpost protection | 5x AMMS + Toughbook C2 | Grid coordinates to BMS, cue other sensors/weapons |

> **Product strategy insight:** Microflown AVISA has the broadest product family of any acoustic C-UAS company analyzed — from helmet-mounted to UAV-mounted to vehicle-mounted to ground-based. All share the same AMMS core sensor with the AVS technology. SKYSENTRY is just one firmware application on the CASTLE platform. This "firmware-defined" approach is analogous to software-defined radio — one hardware investment, multiple missions. For VN-CUAS, this validates the concept of designing a flexible hardware platform with expandable mission firmware.

---

## 3. TECHNOLOGY DEEP DIVE

### 3.1 The Microflown Transducer — Core Physics

The Microflown sensor operates on fundamentally different physics from conventional microphones:

**Conventional Microphones (Sound Pressure):**
- Measure scalar sound pressure (amplitude only)
- Omnidirectional — cannot determine direction from a single sensor
- Require arrays of multiple microphones + beamforming algorithms to estimate direction
- Array size determines frequency-dependent directional resolution
- Narrowband directional capability (optimized for specific frequency ranges)

**Microflown Sensor (Acoustic Particle Velocity):**
- Measures vector acoustic particle velocity (amplitude + direction)
- Inherent figure-of-eight directionality from a single transducer
- Direction determined at the sensor level — no array needed for 2D direction
- Broadband directional capability across the entire acoustic bandwidth
- Complementary physical quantity to sound pressure (together = complete acoustic field)

```
MICROFLOWN SENSOR OPERATING PRINCIPLE
═══════════════════════════════════════

    Two platinum wires heated to ~200°C above ambient
    ┌──────────────────────────────┐
    │                              │
    │   Wire 1 (T₁)   Wire 2 (T₂)│
    │      ║              ║       │
    │      ║ ←─ 200μm ─→ ║       │
    │      ║              ║       │
    │      ║    Air flow  ║       │
    │      ║  ═══════════>║       │
    │      ║  (particle   ║       │
    │      ║   velocity)  ║       │
    │                              │
    └──────────────────────────────┘

    Air flows past → upstream wire cools more → temperature differential
    ΔT = T₁ - T₂ → proportional to acoustic particle velocity

    Sensitivity: figure-of-eight pattern (cos θ)
    Bandwidth: 20 Hz to 14 kHz (broadband)
    Size: two wires of ~200 μm length, ~1 μm diameter
```

### 3.2 Acoustic Vector Sensor (AVS) — Complete Direction Finding

```
3D ACOUSTIC VECTOR SENSOR (AVS) ASSEMBLY
═════════════════════════════════════════

    3 orthogonal Microflown transducers + 1 pressure microphone
    = complete acoustic field measurement at a single point

         Z (velocity)
         │  ╱ Y (velocity)
         │ ╱
         │╱_________ X (velocity)
         │
    + Pressure microphone (P)

    Monolithic chip: 5 × 5 × 5 mm

    Outputs per frequency bin:
    • Vx, Vy, Vz (3D particle velocity vector → source direction)
    • P (sound pressure → source strength / distance)
    • DoA = arctan(Vy/Vx), elevation = arctan(Vz/√(Vx²+Vy²))

    KEY ADVANTAGE vs. microphone arrays:
    ┌─────────────────────────┬───────────────────────────┐
    │ Microphone Array        │ Acoustic Vector Sensor    │
    ├─────────────────────────┼───────────────────────────┤
    │ 128-256 MEMS mics       │ 3 Microflowns + 1 mic    │
    │ Array aperture ~30cm+   │ Single point 5×5×5mm      │
    │ Narrowband directional  │ Broadband directional     │
    │ Frequency-dependent     │ Frequency-independent     │
    │ Complex beamforming     │ Simple vector arithmetic  │
    │ Many channels = complex │ 4 channels = simple       │
    │ Large → more expensive  │ Compact → cheaper/lighter │
    └─────────────────────────┴───────────────────────────┘
```

### 3.3 AMMS Signal Processing Architecture

```
AMMS SIGNAL PROCESSING PIPELINE
════════════════════════════════

ACOUSTIC INPUT → AVS FRONT-END → LOCAL DSP → NETWORK → FUSION → C2 OUTPUT
      │               │              │           │          │          │
  2x Microflown   Amplification   Frequency   Compressed  Multi-    BMS /
  + 1 microphone  + digitization  bin         data via    CASTLE    Toughbook
  per AMMS                        decompose   radio or    triangul. display
                                  + DoA per   hard-wire   3D track
                                  bin                     generation

DETAILED PROCESSING FLOW:

Stage 1: Sensor Capture
├── 2 orthogonal Microflown transducers → Vx, Vy (in-plane velocity)
├── 1 microphone → P (sound pressure)
└── Weather station → wind speed/direction, temperature (for correction)

Stage 2: Local DSP (per AMMS)
├── FFT → decompose signal into frequency bins
├── Per frequency bin: compute DoA from velocity vector ratios
├── Background noise characterization and subtraction
├── Self-noise recognition (platform noise: doors slamming, rattling, engine)
└── Wind noise compensation (using weather data + foam wind cap)

Stage 3: CASTLE-Level Fusion (per post)
├── 4 AMMSs fused for hemispherical coverage
├── Spatial filtering using 4-sensor geometry
├── Improved angular accuracy through redundant measurements
└── Local classification: drone vs bird vs helicopter vs SAF vs RAM

Stage 4: Network-Level Fusion (multi-CASTLE)
├── Multi-post triangulation → range estimation
├── 3D track generation
├── Spatial "bubble" coverage map
└── Bandwidth-minimized data exchange (processed features, not raw audio)

Stage 5: C2 Output
├── Grid coordinates on digital map
├── Target classification + bearing + range
├── Cueing data for other sensors (radar, camera, RCWS)
└── BMS integration (Battlefield Management System)
```

### 3.4 Microflown vs. Conventional Arrays — Performance Comparison

| Parameter | Microflown AVS (AMMS) | Microphone Array (Squarehead 128-mic) | Microphone Array (BeephoniX 151-mic) |
|-----------|----------------------|---------------------------------------|--------------------------------------|
| **Sensors per unit** | 2 Microflown + 1 mic (per AMMS) | 128 MEMS microphones | 151 MEMS microphones |
| **Array size** | 30 cm (or 23 cm) | ~30-50 cm | ~30 cm |
| **Directionality** | Inherent broadband | Frequency-dependent beamforming | Bio-inspired Doppler beamforming |
| **Angular accuracy** | ~1.5° (standalone); **0.2°** (networked) | 1-3° (estimated) | 1-2° |
| **Frequency range** | Full acoustic bandwidth (20 Hz - 14 kHz) | ~50-20 kHz | Broadband |
| **Weight** | 1.75 kg (V-AMMS) | ~8 kg (G2+) | ~950 g (M2) |
| **Power** | <2W | ~10-30W (estimated) | ~5-10W (estimated) |
| **Coverage per unit** | Hemispherical (4 AMMSs on CASTLE) | Sector (needs rotation or multiples) | Hemispherical |
| **Multi-mission** | Yes (firmware-defined) | C-UAS/C-RAM primary | C-UAS primary |
| **Unique advantage** | Physics-level broadband directionality | Large array, high gain | Ultra-light, bio-inspired |
| **Limitation** | Lower detection range vs. large arrays | Heavy, sector-limited | Early-stage company |

> **Technology insight:** The Microflown AVS solves the directionality problem at the physics level — the sensor itself is directional across all frequencies. Conventional microphone arrays solve it at the algorithm level — beamforming computes directional information from many omnidirectional sensors. The AVS approach is more elegant (fewer sensors, smaller, broader bandwidth) but generates weaker signals than a large coherent array (less spatial gain). This is why SKYSENTRY's quadcopter detection range (250m) is shorter than Squarehead's claimed range (300-1000m) — the 128-microphone array has more spatial gain. However, the AVS excels in broadband multi-mission capability and SWaP.

---

## 4. KEY DEPLOYMENTS AND COMBAT RECORD

### 4.1 Combat Deployment — Mali MINUSMA (2015)

| Item | Detail |
|------|--------|
| **Operation** | MINUSMA (UN Multidimensional Integrated Stabilisation Mission in Mali) |
| **User** | Netherlands Army Special Forces Regiment |
| **Platform** | Mercedes Benz G280CDI wheeled offroad vehicles |
| **System** | V-AMMS (Vehicle-mounted Acoustic Multi Mission Sensor) |
| **Quantity** | 9 sets procured |
| **Delivery** | January 2015 |
| **Duration** | 6 months operational use (by mid-2015) |
| **Mission** | Small arms fire localization while on patrol |
| **Performance** | Bullet shockwave detection → 120° sector alert; muzzle blast → precise shooter location |
| **Angular accuracy** | <3° (direction), ~10% (range) |
| **Miss distance** | 500m CPA (static); 150m CPA (moving at up to 60 km/h) |
| **Self-noise rejection** | Ignores outgoing fire (7.62mm, 12.7mm), door slams, equipment rattle |
| **False alarm rate** | "Reduced to zero" (quoted) |
| **Status** | **COMBAT PROVEN** |

> **Combat record insight:** Microflown AVISA is the **only** C-UAS acoustic company in our analysis with a confirmed combat deployment record (Mali 2015). While this was for gunshot localization (not C-UAS), it validates the core AVS technology, the AMMS hardware platform, the DSP processing, and the ruggedization for real-world military conditions. Squarehead, BeephoniX, Mind Foundry, and GA-EMS Fencepost have only demonstrated at trials or exercises, not in active combat operations.

### 4.2 Other Known Deployments

| Deployment | Year | System | Mission | Detail |
|-----------|------|--------|---------|--------|
| **Netherlands artillery range** | ~2014+ | RAM-SCORE (networked AMMS) | Counter-battery training | Point of impact & point of origin for live fire |
| **Bergen/Munster Süd** | ~2014+ | Portable AMMS variant | Training area monitoring | Germany; heavy-use training area |
| **DISCUS** | ~2010-2014 | Networked AMMS | Compound protection | Afghanistan (Tarin Kowt, Uruzgan); also NSS 2014 |
| **NSS 2014** | 2014 | Networked AMMS | Sniper protection | Nuclear Security Summit, Amsterdam Schiphol airport |
| **Denmark (Oksbol)** | 2018 | ATILS | Artillery range scoring | Won Danish tender via partner PTD |
| **Asian customer** | ~2015 | UAV-based system | Acoustic ISR from UAV | Specific country not disclosed |
| **3 European countries** | ~2015 | V-AMMS | Vehicle gunshot localization | Including Netherlands; other 2 not disclosed |

### 4.3 R&D Programmes (Dutch MoD-Funded)

| Programme | Description | Status |
|-----------|-------------|--------|
| **WHELAC** | V-AMMS on wheeled vehicles (SOF) | Completed → Mali deployment |
| **ACHOFILO** | Acoustic Hostile Fire Locator on helicopter (AS532U2 COUGAR) | Tested with live fire (Jun 2013) |
| **FLACOUSE** | Flying Acoustic Seeker — UAV-mounted Acoustic Pointer | Developed; autonomous + networked variants |
| **Perch and Listen** | Multicopter-deployed AMMS for forward ISR | Developed; 5 kg, 21 min endurance |
| **Loose Track** | V-AMMS on armoured vehicles (VECTOR, BOXER, FENNEK, BUSHMASTER, CV90, Eagle IV/V) | In development |
| **Walking Ears** | Helmet/rifle/throwable miniature AMMS for dismounted soldiers | Tested Sep 2015; IP67 |
| **SKYSENTRY** | C-UAS capability on CASTLE platform | Ongoing; demos in "several Western countries" (2015) |
| **TeamAware** | EU Horizon 2020 project (grant 101019808) — multi-sensor awareness | Participated |
| **EDF WHATSUP** | "Wise Heterogeneous Arrays of Terrestrial Sensors with Upward and Panoramic views" — EDF-2023 C-UAS | Proposal submitted (2023); status unconfirmed |

### 4.4 Patent Portfolio

| Patent | Title | Year | Status |
|--------|-------|------|--------|
| **PCT/NL95/00220** | "Use of a fluid flow-measuring device as a microphone" | 1995 | Foundational patent by de Bree. **Likely expired ~2015** (20-year term) |
| **WO1999035470A1** | "Acoustic particle velocity sensor" / U-U method | 1999 | Filed by Alex Koers, Microflown Technologies. **Likely expired ~2019** |
| **EP1649591A2** | "Acoustic vector sensor" (assembled AVS) | 2003/2004 | European patent application |
| **US20050034519A1** | "Acoustic vector sensor" (US counterpart) | 2005 | US application |
| **US20230131772** | "Acoustic Vector Sensor" (new filing) | 2023 | **Active** — recent US patent application |

> **IP insight:** The foundational Microflown patents (1995, 1999) have likely expired, meaning the core sensor concept is no longer patent-protected. However, Microflown retains competitive advantage through: (1) **manufacturing know-how** — MEMS fabrication of the transducer requires specialized cleanroom processes, (2) newer patents (2023 application), and (3) decades of application engineering. For VN-CUAS, the patent expiry means that AVS-style particle velocity sensors could theoretically be replicated — but the manufacturing capability gap remains enormous. The commodity MEMS microphone array approach remains more practical.

### 4.5 European Competitive Landscape — EDF E-CUAS

A significant competitive development: the major **EDF-2023 C-UAS** project selected for funding is **E-CUAS** (European Counter-UAS), receiving **EUR 71 million**, led by **Leonardo** with 35 entities from 13 countries. Key consortium members include:

| Company | Country | Role |
|---------|---------|------|
| **Leonardo** | Italy | Coordinator |
| **Thales** | France | Key partner |
| **Diehl Defence** | Germany | Effector/sensor |
| **Kongsberg** | Norway | Sensor |
| **SAAB** | Sweden | Sensor |
| **Squarehead Technology** | Norway | **Passive acoustic detection** |
| **Delft Dynamics** | Netherlands | Counter-drone |
| **Hensoldt, Indra, CNIT** | Various | Various |

> **Competitive insight:** Squarehead Technology (a direct Microflown competitor) was selected for E-CUAS, while Microflown AVISA's WHATSUP proposal status is unconfirmed. This means Squarehead may gain significant EUR 71M backing and European integration opportunities, while Microflown AVISA remains a smaller independent player. For VN-CUAS, this validates Squarehead-style microphone arrays as the European institutional preference for C-UAS acoustic detection, and confirms that Microflown's AVS approach, while technologically elegant, has not achieved broad institutional adoption.

---

## 5. SYSTEM ARCHITECTURE — SKYSENTRY C-UAS

### 5.1 SKYSENTRY Network Architecture

```
SKYSENTRY C-UAS DEPLOYMENT (typical)
═══════════════════════════════════════

                        Coverage "Bubble"
                      ┌─────────────────┐
                      │   Hemispherical  │
                      │   acoustic field │
                      │   per CASTLE     │
                      └────────┬────────┘
                               │
     [CASTLE 1]───radio───[CASTLE 2]───radio───[CASTLE 3]
         │                     │                     │
    4x AMMS + AMR         4x AMMS + AMR         4x AMMS + AMR
    + weather stn         + weather stn         + weather stn
         │                     │                     │
         └─────────┬───────────┘─────────────────────┘
                   │
             ┌─────┴─────┐
             │ COMMAND    │
             │ POST       │
             │ (Toughbook │
             │  display)  │
             │            │
             │ • Grid map │
             │ • Tracks   │
             │ • Alerts   │
             │ • Cue data │
             └─────┬─────┘
                   │
            ┌──────┴──────┐
            │ BMS / C2    │
            │ Integration │
            │ (optional)  │
            └─────────────┘

DETECTION RANGES (per CASTLE):
• 2 kg quadcopter:  ~250 m
• 2 kg fixed-wing:  ~1 km
• Manned helicopter: ~10 km

NETWORKING BENEFIT:
• Single CASTLE: DoA only (direction + elevation)
• 2+ CASTLEs: Triangulation → range + 3D position
• 3+ CASTLEs: Redundant 3D tracking + spatial "bubble"
```

### 5.2 Detection Physics — Range vs. Target Type

```
DETECTION RANGE MODEL (estimated from public data)
═══════════════════════════════════════════════════

Detection range depends on:
1. Target acoustic signature strength (source level in dB)
2. Propagation loss (spherical spreading + atmospheric absorption)
3. Background noise level
4. Sensor sensitivity (Microflown transducer noise floor)

Target Type          Acoustic Source Level    Detection Range
─────────────────────────────────────────────────────────────
Small quadcopter     Low (~60-70 dB @ 1m)     ~250 m
(2 kg, electric)     High frequency dominance

Fixed-wing UAV       Medium (~70-80 dB @ 1m)  ~1 km
(2 kg, propeller)    Strong blade-passing freq

Large UAV            Higher (~80-90 dB @ 1m)  ~2-5 km (est.)
(Group 2-3, engine)  Broad spectrum

Manned helicopter    Very high (~100+ dB @ 1m) ~10 km
(turbine + rotors)   Dominant low-freq rotors

Small arms fire      Very high (impulse)       ~500 m CPA (V-AMMS)
(gunshot)            Broadband impulse

Artillery/mortar     Extremely high             Multi-km (MSRA mode)
(RAM)                Low-freq blast wave

NOTE: Range for networked configuration likely exceeds single-CASTLE
figures due to coherent processing gain across multiple posts.
```

---

## 6. FUNCTIONAL DECOMPOSITION (Reverse-Engineered)

### 6.1 SKYSENTRY Function Structure

```
F0: DETECT, LOCATE, AND TRACK AERIAL THREATS (SKYSENTRY)
├── F1: Sense acoustic field (per AMMS)
│   ├── F1.1: Measure 2D particle velocity vector (2 orthogonal Microflowns)
│   ├── F1.2: Measure sound pressure (microphone)
│   ├── F1.3: Protect sensors from wind/weather (foam wind cap)
│   └── F1.4: Compensate for environmental conditions (weather station)
├── F2: Process signals locally (per AMMS DSP)
│   ├── F2.1: Digitise and filter raw sensor signals
│   ├── F2.2: Decompose into frequency bins (FFT)
│   ├── F2.3: Compute Direction of Arrival per frequency bin
│   ├── F2.4: Subtract background noise profile
│   ├── F2.5: Reject self-noise (platform motion, mechanical noise)
│   └── F2.6: Compress processed data for network transmission
├── F3: Fuse sensor data (per CASTLE — Acoustic Master)
│   ├── F3.1: Combine data from 4 AMMSs for hemispherical coverage
│   ├── F3.2: Apply spatial filtering across 4-sensor geometry
│   ├── F3.3: Refine angular estimates through sensor redundancy
│   └── F3.4: Maintain local situation picture
├── F4: Classify targets
│   ├── F4.1: Match spectral signature against threat database
│   ├── F4.2: Discriminate drones from birds, aircraft, ground vehicles
│   ├── F4.3: Estimate target type (quadcopter, fixed-wing, helicopter)
│   └── F4.4: Assign threat priority
├── F5: Track and localise targets (multi-CASTLE fusion)
│   ├── F5.1: Correlate detections across networked CASTLEs
│   ├── F5.2: Triangulate position from multi-post DoA estimates
│   ├── F5.3: Generate 3D track (azimuth, elevation, range)
│   ├── F5.4: Maintain tracks on multiple simultaneous targets
│   └── F5.5: Predict target trajectory
└── F6: Alert and integrate with C2
    ├── F6.1: Display threats on digital map (grid coordinates)
    ├── F6.2: Generate alert with target classification and bearing
    ├── F6.3: Provide cueing data for other sensors (radar, camera, RCWS)
    └── F6.4: Feed data to BMS (Battlefield Management System)
```

---

## 7. BOM ESTIMATE (Reverse-Engineered)

### 7.1 AMMS Unit — Estimated BOM

| Component | Estimated Specification | Est. Cost |
|-----------|------------------------|-----------|
| Microflown transducers (x2) | Proprietary MEMS particle velocity sensors, orthogonal | $200-1,000 |
| Pressure microphone (x1) | MEMS or condenser, co-located | $5-50 |
| DSP processor | Embedded ARM/DSP for local FFT + DoA computation | $20-100 |
| ADC | Multi-channel, high-resolution | $10-50 |
| Foam wind cap | Open-cell foam, weatherproof | $5-20 |
| Sheet metal housing | 30 cm or 23 cm diameter, rugged | $20-80 |
| PCB & assembly | Multi-layer, conformal coated | $30-100 |
| Connector | Weatherproof, hard-wired to CASTLE | $10-30 |
| **Total BOM per AMMS** | | **$300-1,430** |

### 7.2 CASTLE Post — Estimated BOM

| Component | Specification | Est. Cost |
|-----------|---------------|-----------|
| 4x AMMS units | As above | $1,200-5,720 |
| Acoustic Master (AMR) | Embedded computer for CASTLE-level fusion | $200-800 |
| Weather station | Wind speed/direction, temperature, humidity | $100-500 |
| 2x GNSS receivers | Position + heading; anti-jam/spoof optional | $100-1,000 |
| Radio module | Mesh networking for multi-CASTLE | $100-500 |
| Power supply | Battery or external power | $50-200 |
| Mounting hardware | Tripod/stake, cables between AMMSs | $50-200 |
| Enclosure / structure | CASTLE post assembly, ruggedized | $100-500 |
| Firmware license | SKYSENTRY (or MSRA, ATILS, etc.) | $1,000-5,000 |
| **Total BOM per CASTLE** | | **$2,900-14,420** |
| **Est. Unit Price** | (with margins, integration, support) | **$15,000-50,000 est.** |

### 7.3 SKYSENTRY System (3-CASTLE Configuration) — Estimated

| Component | Specification | Est. Cost |
|-----------|---------------|-----------|
| 3x CASTLE posts | As above | $8,700-43,260 |
| Command post | Toughbook/Durabook display + software | $3,000-8,000 |
| Networking infrastructure | Radio repeaters, cables | $500-2,000 |
| Carrying cases | Transit and deployment kits | $500-1,500 |
| **Total 3-CASTLE System** | | **$12,700-54,760** |
| **Est. System Price** | (with margins, training, support) | **$50,000-150,000 est.** |

> **Cost insight:** Microflown AVISA's pricing is driven by the proprietary Microflown transducers — these are not commodity MEMS parts and cannot be sourced from third parties. The transducer cost is the key unknown: if each costs $100-200 (high-volume MEMS), the AMMS BOM is very competitive; if $500-1,000 (low-volume specialty MEMS), the cost advantage vs. microphone arrays narrows. For VN-CUAS, the key lesson is that commodity MEMS microphones ($0.50-2 each) in arrays of 128-256 provide lower per-sensor cost but require more complex beamforming DSP. The AVS approach trades sensor cost for algorithmic simplicity.

---

## 8. DESIGN INSIGHTS FOR VN-CUAS

### 8.1 Key Lessons from Microflown AVISA SKYSENTRY

1. **AVS physics is elegant but proprietary:** The Acoustic Vector Sensor solves directionality at the sensor level — 3 tiny transducers replace 128-256 microphones. However, this technology is patented and manufactured only by Microflown. VN-CUAS cannot use AVS technology and must use conventional MEMS microphone arrays with beamforming. This is not a disadvantage — large arrays offer higher spatial gain and longer detection range for the same target.

2. **Firmware-defined multi-mission is strategically brilliant:** CASTLE's approach of same hardware + different firmware for different missions (C-UAS, C-RAM, vehicle protection, etc.) is a business model VN-CUAS should adopt. Design the hardware platform for the broadest acoustic sensing capability, then define missions in software/firmware.

3. **250m quadcopter range is honest and realistic:** SKYSENTRY's claimed 250m for a 2 kg quadcopter is the most conservative and likely most accurate drone detection range claim of all systems analyzed. This suggests that acoustic-only C-UAS detection of small electric quadcopters is fundamentally limited to a few hundred meters. VN-CUAS should be honest about this physics limitation and position accordingly.

4. **Hemispherical coverage from a single post is achievable:** CASTLE achieves full hemispherical coverage from 4 small sensors (not 128). VN-CUAS can achieve similar coverage with a well-designed MEMS array geometry (spherical or semi-spherical arrangement of microphones).

5. **<2W power is achievable for acoustic sensing:** V-AMMS at <2W proves extremely low-power acoustic sensing is feasible. VN-CUAS's <10W target has significant margin. However, <2W is for a simple 2-transducer AMMS; a 128-256 mic array with beamforming DSP will consume more power.

6. **Combat-proven in Mali validates real-world ruggedization:** The 6-month Mali deployment proves that compact acoustic sensors survive and function in harsh field conditions (desert heat, dust, vibration, gunfire). VN-CUAS should target equivalent or higher environmental qualification for tropical conditions (humidity, salt spray, monsoon rain).

7. **Networked sensors provide the real capability:** A single CASTLE gives direction only; multiple networked CASTLEs give 3D position. Similarly, VN-CUAS should design for single-node direction capability with multi-node position/tracking — validating the mesh network architecture from the Fencepost analysis.

8. **Multi-mission potential de-risks the business case:** Microflown AVISA started with gunshot localization (V-AMMS), expanded to C-RAM (MSRA), then C-UAS (SKYSENTRY). VN-CUAS should consider a similar trajectory: start with the mission that has clearest demand (C-UAS), then expand firmware to gunshot localization, counter-battery, etc.

### 8.2 VN-CUAS Positioning vs SKYSENTRY

| Scenario | Positioning |
|----------|-------------|
| **Longer range** | VN-CUAS 128-256 mic array has higher spatial gain → likely exceeds SKYSENTRY's 250m quadcopter range |
| **Lower cost** | VN-CUAS uses commodity MEMS mics ($0.50-2 each) vs proprietary Microflown transducers ($200-1000 est.) |
| **ML-enhanced** | VN-CUAS with spectrogram→CV classification adds ML capability SKYSENTRY lacks |
| **Array advantage** | 128-256 coherent microphones provide more spatial gain than 2 Microflown transducers per AMMS |
| **AVS disadvantage** | VN-CUAS cannot match AVS's broadband directionality from a single point — needs larger array |
| **Multi-mission** | VN-CUAS should adopt SKYSENTRY's firmware-defined multi-mission model |
| **Export market** | VN-CUAS for markets where Microflown's small scale limits availability |

### 8.3 Updated VN-CUAS Product Concept (v8.0)

Building on insights from all 8 RE analyses (Squarehead, BeephoniX, Fraunhofer, DroneShield, Dedrone, Mind Foundry, GA-EMS Fencepost, Microflown AVISA SKYSENTRY):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Array** | 128-256 MEMS microphones | Squarehead (128), BeephoniX (151) benchmarks; higher spatial gain than AVS approach |
| **Weight** | 1-2 kg (sensor head); 3-5 kg (full node) | BeephoniX (950g), V-AMMS (1.75 kg) prove ultra-light feasible |
| **Power** | <10W (sensor); <15W (full node with comms) | V-AMMS (<2W) sets floor; array + DSP needs more |
| **Detection Range** | 300-500m (Group 1 quadcopter); 1-3 km (Group 2-3) | SKYSENTRY 250m baseline + array gain advantage; Fencepost 5-7km for large targets |
| **Frequency** | **50-20000 Hz** | Broader than Fencepost (100-4000 Hz); matches Microflown broadband philosophy |
| **Accuracy** | ≤3° azimuth (standalone); ≤0.5° (networked) | V-AMMS 1.5°/0.2° benchmark; array beamforming can match |
| **Coverage** | Hemispherical per node | CASTLE achieves this with 4 AMMSs; VN-CUAS with array geometry |
| **Target Price** | $2K-5K per node | Commodity MEMS vs proprietary Microflown = cost advantage |
| **Environmental** | IP67, MIL-STD-810H | V-AMMS combat-proven in Mali; SKYSENTRY all-weather |
| **Classification** | **Dual: eigenvector baseline + spectrogram→CV ML** | Fencepost classical + Mind Foundry AI: best of both |
| **DoA Method** | **Beamforming + MUSIC/ESPRIT hybrid** | Array beamforming (Squarehead) + eigenvector (Fencepost) |
| **Integration** | SAPIENT + RESTful API + TAK plugin + BMS | Dedrone/DroneShield (SAPIENT) + Mind Foundry (ATAK) + Microflown (BMS) |
| **Seismic Option** | Optional geophone/accelerometer per node | Fencepost dual-modality concept |
| **Mesh Network** | Multi-node distributed detection | Fencepost + SKYSENTRY: networked nodes are essential for 3D |
| **Edge AI** | Edge-first, cloud-optional | Mind Foundry edge concept |
| **Multi-Mission Firmware** | C-UAS → C-RAM → gunshot → vehicle protection | **Microflown AVISA's firmware-defined multi-mission model** |
| **Local Content** | ≥60% by value | Vietnamese defense requirement |
| **Cross-Domain** | Drone → mortar → artillery → border → ground vehicles | Fencepost + Mind Foundry + Microflown multi-mission |
| **Deployment** | <15 min per node by one person | SKYSENTRY <10 min benchmark |

### 8.4 C-UAS Ecosystem Map (After 8 RE Analyses)

```
MARKET LANDSCAPE (2025-2026) — UPDATED v8
═══════════════════════════════════════════════════════════════════

HIGH COST ($100K-1M+)    ┌───────────────────────────────────────┐
Multi-Sensor Systems      │  DroneShield DroneSentry               │
                          │  Dedrone Full System                    │
                          │  (Complete DTI-M kill chain)            │
                          └───────────────────────────────────────┘

MID COST ($20K-100K)      ┌───────────────────────────────────────┐
Specialized Sensors       │  Squarehead Discovair G2+               │
                          │  Dedrone RF-360 sensor                  │
                          │  Mind Foundry SENTRY (est.)             │
                          │  GA-EMS Fencepost system (est.)         │
                          │  Microflown AVISA SKYSENTRY (est.)      │
                          │  (Single modality / AI layer)           │
                          └───────────────────────────────────────┘

LOW COST ($2K-20K)        ┌───────────────────────────────────────┐
Entry/Complementary       │  BeephoniX M2                           │
                          │  GA-EMS Fencepost per-node (est.)       │
                          │  Microflown AMMS per-unit (est.)        │
                          │  ★ VN-CUAS (TARGET) ★                   │
                          │  (Affordable acoustic detection nodes)  │
                          └───────────────────────────────────────┘

RESEARCH/ALGORITHM        ┌───────────────────────────────────────┐
Technology Provider       │  Fraunhofer IDMT                        │
                          │  Mind Foundry (AI engine licensing)      │
                          │  (Algorithms + consulting)              │
                          └───────────────────────────────────────┘

PARADIGMS IDENTIFIED (8 systems):
• BEAMFORMING: Squarehead (128 MEMS), BeephoniX (151 dynamic MEMS)
• RF-CENTRIC: Dedrone (DroneDNA), DroneShield (RFAI)
• AI/ML-FIRST: Mind Foundry (Bayesian ML + CV)
• CLASSICAL SIGNAL PROCESSING: GA-EMS Fencepost (eigenvector)
• ACOUSTIC VECTOR SENSING: Microflown AVISA (particle velocity AVS)
• ALGORITHM-CENTRIC: Fraunhofer IDMT
• VN-CUAS: Hybrid beamforming + eigenvector + ML (commodity MEMS)
═══════════════════════════════════════════════════════════════════
```

---

## 9. INTELLIGENCE GAPS

| ID | Gap | Priority | Impact on VN-CUAS |
|----|-----|----------|-------------------|
| IG-01 | Microflown transducer manufacturing cost at volume | **High** | Cost comparison with MEMS mic arrays |
| IG-02 | SKYSENTRY classification algorithms (ML or rule-based?) | **High** | ML approach selection |
| IG-03 | CASTLE environmental ratings (IP, MIL-STD, temperature range) | **High** | Environmental design specification |
| IG-04 | Networked SKYSENTRY detection range improvement vs single CASTLE | **High** | Network architecture sizing |
| IG-05 | SKYSENTRY pricing (per CASTLE and per system) | Medium | Competitive positioning |
| IG-06 | EDF WHATSUP project status and partners (2024-2025) | Medium | European market dynamics |
| IG-07 | False alarm rate for SKYSENTRY in cluttered urban environments | Medium | Performance specification |
| IG-08 | CASTLE battery life and power consumption (full system) | Medium | Power budget and deployment planning |
| IG-09 | Microflown patent portfolio — scope and expiry dates | Medium | Freedom-to-operate for AVS approach |
| IG-10 | SKYSENTRY performance in tropical/high-humidity environments | Medium | Vietnam deployment suitability |
| IG-11 | Total units sold and current production rate | Low | Market size assessment |
| IG-12 | Acoustic Pointer / Perch-and-Listen current status | Low | UAV-mounted acoustic ISR roadmap |

---

## 10. REFERENCES

1. Microflown AVISA: SKYSENTRY product page — https://www.microflown-avisa.com/solutions/skysentry-1/skysentry-1-1
2. Microflown AVISA: Technology page — https://www.microflown-avisa.com/technology
3. Microflown AVISA: About us — https://www.microflown-avisa.com/about-us
4. Military Technology (MilTech): "Microflown AVISA Creates Acoustic Awareness" (Oct 2015) — http://www.miltechmag.com/2015/10/microflown-avisa-creates-acoustic.html
5. Microflown Technologies: About us — https://www.microflown.com/about-us
6. Microflown: Particle Velocity Sensors — https://www.microflown.com/products/acoustic-particle-velocity-sensors
7. MSS Defence: Microflown AVISA SKYSENTRY — https://mssdefence.com/product/microflown-avisa-skysentry/
8. de Bree, H-E.: "The Microflown: An acoustic particle velocity sensor" (2003) — https://www.acoustics.asn.au/journal/2003/2003_31_3_Bree.pdf
9. ResearchGate: "The Acoustic Vector Sensor, a versatile battlefield acoustics sensor" — https://www.researchgate.net/publication/252406347
10. EPICOS: Microflown AVISA company profile — https://www.epicos.com/company/10779/microflown-avisa
11. UAS Vision: "Microflown Avisa Mounts Acoustic Vector Sensors On Board Unmanned Aircraft" (2012) — https://www.uasvision.com/2012/01/27/microflown-avisa-mounts-acoustic-vector-sensors-on-board-unmanned-aircraft/
12. Unmanned Airspace: Microflown AVISA C-UAS — https://www.unmannedairspace.info/c-uas-search/microflown-avisa/
13. Tracxn: Microflown AVISA company profile — https://tracxn.com/d/companies/microflown-avisa/
14. JOAST: "A Perspective on Acoustic Vector Sensors in Passive Surveillance" — https://www.joast.org/index.php/joast/article/view/651

---

## 11. COMPARATIVE SUMMARY TABLE

| Dimension | Squarehead G2+ | BeephoniX M2 | Fraunhofer IDMT | DroneShield | Dedrone | Mind Foundry SENTRY | GA-EMS Fencepost | **Microflown SKYSENTRY** | VN-CUAS Target |
|-----------|---------------|-------------|-----------------|-------------|---------|---------------------|-----------------|------------------------|---------------|
| **Country** | Norway | Netherlands | Germany | Australia | Germany/USA | UK | USA | **Netherlands** | Vietnam |
| **Type** | Acoustic sensor | Acoustic sensor | Research | Multi-sensor | Software C2 | Acoustic AI | Acoustic/seismic | **Acoustic vector** | Acoustic + ML |
| **Founded** | 2000 | 2022 | 2008 | 2014 | 2014 | 2016 | 1955 (GA) | **1998/2011** | 2026 |
| **Ownership** | Private | Private | Institute | ASX:DRO | Axon | Private | Private (Blue) | **Private** | State |
| **Sensing** | 128 MEMS mics | 151 MEMS mics | Microphones | RF+radar+optical | RF+camera | Any microphone | Mic+geophone | **AVS (velocity)** | 128-256 MEMS |
| **Signal Processing** | Beamforming | Bio-Doppler | ML fingerprint | Multi-sensor AI | RF protocol | Bayesian ML+CV | Eigenvector | **Vector arithmetic** | Hybrid |
| **AI/ML** | ML layer | ML layer | Core | Yes | DroneDNA | Core Bayesian | Planned | **TBD** | Core |
| **Drone Range** | 300-1000m | 200-900m | 50-200m | 1-8 km | 1.6-5 km | ~200m-1km | 5-7 km (Grp3) | **250m (quad)** | 300-500m |
| **Frequency** | ~50-20kHz | Broadband | Broadband | N/A (RF) | N/A (RF) | Broadband | 100-4000 Hz | **20Hz-14kHz** | 50-20kHz |
| **Weight** | ~8 kg | ~950 g | N/A | Heavy | N/A | N/A | TBD | **1.75 kg (AMMS)** | 1-2 kg |
| **Power** | ~10-30W | ~5-10W | N/A | High | N/A | N/A | TBD | **<2W (AMMS)** | <10W |
| **Coverage** | Sector | Hemispherical | Point | 360° multi-sensor | 360° RF | Omnidirectional | Perimeter | **Hemispherical** | Hemispherical |
| **Multi-mission** | C-UAS/C-RAM | C-UAS | C-UAS | Multi | Multi | C-UAS/ASW | C-UAS/seismic | **7+ missions** | Multi (target) |
| **Combat proven** | No | No | No | In use | In use | No | No | **Yes (Mali)** | No |
| **Unique** | Large array gain | Bio-inspired | NLOS | RF library | SW platform | ATAK deploy | Seismic dual | **AVS physics** | Cost + ML |
| **Maturity** | Commercial | Field demo | Research | Production | Production | Pre-production | Demo (TRL 6-7) | **Production** | Concept |
| **Price/Node** | $50-150K | $20-50K | License | $200K+/site | $50K+ | $20-100K est. | $5-20K est. | **$15-50K est.** | $2-5K |
