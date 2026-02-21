---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Squarehead Technology Discovair G2+ (Norway)
version: 1.0
created: 2026-02-11
status: complete
---

# RE: Squarehead Technology Discovair G2+ - Norway
## Reverse Engineering Analysis from Public Sources

> **CRITICAL NOTE:** The Discovair G2+ is **NOT a LOMAH** (Location of Miss and Hit) shooting range scoring system. It is a **passive acoustic threat detection sensor** (C-UAS, C-RAM, sniper detection). However, its 128-microphone array beamforming technology represents a fundamentally different — and potentially superior — approach to acoustic sensing that has direct relevance to next-generation LOMAH design. This analysis evaluates the technology for cross-domain application.

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Squarehead Technology AS |
| **HQ** | Nydalsveien 28, 0484 Oslo, Norway |
| **Mailing** | PO Box 13, Nydalen, NO-0410 Oslo |
| **US Office** | Squarehead Technology LLC, 200 1st Ave NW, Suite 617, Hickory, NC 28601 |
| **Phone (NO)** | +47 21 66 63 37 |
| **Phone (US)** | +1 (571) 299-6971 |
| **Org Nr** | 987 307 749 (Norway) |
| **Founded** | 2004 |
| **Origin** | Three physics students, University of Oslo |
| **Employees** | ~45-67 (sources vary) |
| **Revenue** | ~$6M (2025 estimate) |
| **Status** | Private, independent |
| **Subsidiaries** | USA (Hickory, NC); teams in Canada, Denmark, Argentina |
| **Key products** | Discovair G2+ (acoustic array), AudioScope (legacy) |
| **ITAR status** | ITAR-free |

### Key Personnel

| Name | Role | Background |
|------|------|------------|
| **Vibeke Jahr** | Founder & COO | Co-founder, physics, University of Oslo |
| **Stig Oluf Nyvold** | CEO | Ex-Galleon Embedded Computing, Curtiss Wright Controls, VMETRO ASA |
| **Ines Hafizovic** | Head of Research | Co-founder, named inventor on core patents |
| **Morgan Kjølerbakken** | Co-founder | Physics, University of Oslo; named inventor on early patents |

Two of three original founders remain with the company.

### Historical Lineage

| Year | Event |
|------|-------|
| 2003-2004 | Three University of Oslo physics students (Kjølerbakken, Jahr, Hafizovic) explore underwater sound waves; conceive directional "super-microphone" |
| 2004 | Squarehead Technology AS founded in Oslo |
| 2006 | First patent filed (US 2008/0247567 — Directional Audio Capturing) |
| ~2008-2010 | AudioScope product for broadcasting/sports audio capture |
| ~2014-2016 | Pivot to defense/security; discover drone detection capability |
| 2016 | UAV Detection patent filed (US 10,557,916) |
| 2017 | Discovair G2 deployed at G20 Summit, Hamburg |
| 2019 | Discovair G2 presented at NATO NAAG meeting, Oslo |
| 2019 | Microphone Arrays patent filed (US 11,832,051) |
| 2020 | DroneShield partnership for integrated C-UAS (DroneSentry-C2) |
| 2021 | US DOD tests DroneShield + Discovair combined system |
| ~2023-2024 | Discovair G2+ launched (enhanced version with MIL-STD-810H, C-RAM capability) |
| 2024 | Idekapital leads NOK 50M funding round; Norselab equity investment |
| 2025 | Norwegian Defence contract (P5007 counter-battery acoustic sensors) |
| 2025 | OSL framework NOK 938M C-UAS at Ørland Air Station (Squarehead as sub-supplier) |
| 2025 | Joins E-CUAS (European Counter-UAS) EDF project |
| 2025 | PROTEAS EDF project — acoustic situational awareness |
| 2026 | NATO Fast-Track Defense Tech Challenge selection (150 firms) |

### Investors & Funding

| Investor | Detail |
|----------|--------|
| **Idekapital** | Led NOK 50M funding round |
| **Norselab** | Meaningful Equity I fund (NOK 500M across 16 companies) |
| **H4XLabs** | Investor |
| Latest round | $1.28M (December 2023) |

Squarehead is a **small, specialized company** — roughly 1/20th the size of a typical LOMAH manufacturer (Saab ~900 T&S employees, InVeris ~1,000+). Their strength is deep expertise in array acoustics and machine learning, not manufacturing scale.

---

## 2. PRODUCT FAMILY OVERVIEW

```
Squarehead Technology - Product Portfolio
│
├── Discovair G2+ (Current Flagship)
│   ├── C-UAS: Drone detection & classification (Class I/II)
│   ├── C-RAM: Rocket/Artillery/Mortar detection & source localization
│   ├── Sniper detection: Muzzle blast & shockwave localization
│   ├── Vehicle detection: Ground vehicle acoustic classification
│   └── Multi-purpose: Configurable via ML model selection
│
├── Discovair G2 (Previous Generation)
│   └── Drone detection focus (predecessor to G2+)
│
├── Discovair (Original, ~2014-2016)
│   └── First-generation acoustic drone detector
│
├── AudioScope (Legacy, ~2008-2012)
│   └── Broadcasting/sports audio capture & zoom
│   └── Stadium/arena directed audio pickup
│
└── Industrial Solutions
    ├── Pulp & paper: Machine condition monitoring
    ├── Metal industry: Acoustic quality control
    └── Autonomous vessels: Maritime acoustic sensing
```

### Product Evolution

| Generation | Period | Focus | Microphones | Key Advance |
|-----------|--------|-------|-------------|-------------|
| AudioScope | 2008-2014 | Broadcasting | Array (count unknown) | Acoustic zoom for sports |
| Discovair | 2014-2017 | Drone detection | Array | First passive acoustic drone detector |
| Discovair G2 | 2017-2023 | C-UAS | 128 | IP65, digital MEMS, improved ML |
| **Discovair G2+** | **2023-present** | **C-UAS + C-RAM** | **128** | **MIL-STD-810H, on-edge ML, camera, C-RAM** |

---

## 3. DISCOVAIR G2+ SYSTEM ARCHITECTURE

### 3.1 System Topology

```
┌──────────────────────────────────────────────────────────────────────┐
│                    DISCOVAIR G2+ SYSTEM                               │
│                                                                      │
│  SENSOR UNIT (Self-Contained)              COMMAND & CONTROL         │
│  ┌──────────────────────────┐              ┌───────────────────┐     │
│  │  128 MEMS Microphones    │   Ethernet   │  Browser-Based    │     │
│  │  (proprietary circular   │──────────────│  User Interface   │     │
│  │   array pattern)         │      or      │  (any device)     │     │
│  │                          │    API       │                   │     │
│  │  Integrated Camera       │              └───────────────────┘     │
│  │  (optical reference)     │                      │                 │
│  │                          │              ┌───────────────────┐     │
│  │  On-Edge Processor       │    API       │  C2 System        │     │
│  │  (beamforming + ML)      │──────────────│  • ATAK/WinTAK    │     │
│  │                          │              │  • NATO SAPIENT   │     │
│  │  24-48 VDC Power         │              │  • DroneSentry-C2 │     │
│  │  (~20W draw)             │              │  • Custom BMS     │     │
│  └──────────────────────────┘              └───────────────────┘     │
│       │                                                              │
│  Multiple sensors → networked protection grid                        │
│  (360° coverage from single sensor when horizontal)                  │
│  (105° FoV per sector when vertical)                                 │
└──────────────────────────────────────────────────────────────────────┘
```

### 3.2 Detection Principle: Beamforming (NOT TDOA)

**This is fundamentally different from all LOMAH systems reviewed.**

LOMAH systems use **TDOA (Time-Difference-of-Arrival)** with 4-8 microphones to triangulate a single supersonic projectile at a specific target plane. Discovair uses **digital beamforming** with 128 microphones to create steerable directional "acoustic beams" across a 105° field of view.

**Step 1: Sound Capture**
128 MEMS microphones capture sound simultaneously. The array's proprietary geometric arrangement determines directional resolution capability.

**Step 2: Digital Beamforming**
A beamforming algorithm combines all 128 microphone signals, applying phase delays to "steer" the array's sensitivity toward specific directions. This creates a directional supermicrophone that amplifies sound from a chosen direction while suppressing all other directions.

**Step 3: Multi-Beam Scanning**
The same array simultaneously forms beams in many directions across its 105° field of view. Each sector is continuously monitored for acoustic changes.

**Step 4: ML Classification**
When an acoustic change is detected, the beamformed signal is analyzed by a machine learning classifier trained on threat signatures (drone propeller sounds, muzzle blasts, rocket launches, etc.). The system classifies the sound and provides bearing/elevation.

```
Beamforming vs TDOA:

LOMAH (TDOA - 4 microphones):                 DISCOVAIR (Beamforming - 128 microphones):

   Projectile ●→→→→→→→→                          Sound source ●
        Mach cone                                     ↓ ↓ ↓
       /  |  \                                  ┌─────────────────┐
  ──T1──T2──T3──T4──                            │ ░░░░░░░░░░░░░░░ │
     Δt → triangulation                         │ ░128 MEMS mics░ │  Steerable
     → (X,Y) at target plane                    │ ░░░░░░░░░░░░░░░ │  beam pattern
                                                └─────────────────┘
  Accuracy: ±5-10mm at plane                    → bearing + elevation
  Range: ~3×2.5m target zone                    → 105° FoV, 300-1000m range
  Purpose: Bullet position                      → Threat classification + tracking
```

### 3.3 Beamforming vs TDOA — Technical Comparison

| Parameter | TDOA (LOMAH) | Beamforming (Discovair) |
|-----------|-------------|------------------------|
| **Microphones** | 4-8 | 128 |
| **Array size** | ~1-3m (target-mounted bar) | ~30-40cm (pizza-box) |
| **Principle** | Time difference → position | Phase delay → direction |
| **Output** | X,Y coordinates (mm) | Bearing, elevation (degrees) |
| **Accuracy** | ±5-10mm positional | <10° directional |
| **Detection range** | ~3×2.5m zone at target | 300-1000m |
| **Speed requirement** | Supersonic (≥Mach 1.3) | Any audible sound |
| **Calibration** | Required (most) or calibration-free | Not applicable |
| **Processing** | Deterministic triangulation | ML classification |
| **Multi-target** | 1 projectile per detection cycle | Multiple simultaneous targets |
| **Environmental** | Temperature-sensitive (speed of sound) | Robust (ML-adaptive) |

---

## 4. DETAILED COMPONENT SPECIFICATIONS

### 4.1 Sensor Unit (Discovair G2+)

| Parameter | Specification |
|-----------|--------------|
| **Microphone count** | 128 digital MEMS microphones |
| **Microphone type** | Digital MEMS (Micro-Electro-Mechanical Systems) |
| **Array geometry** | Proprietary circular/pattern arrangement (patented) |
| **Integrated camera** | Optical camera for visual reference and fused detection |
| **Processing** | On-edge (embedded — no external server required) |
| **Weight** | 8 kg |
| **Size** | "Pizza box" form factor (~30-40cm diameter estimated) |
| **IP rating** | IP65 (dust-tight, water jet resistant) |
| **MIL-STD** | MIL-STD-810H compliant |
| **Operating temperature** | -40°C to +70°C |
| **Power input** | 24-48 VDC |
| **Power draw** | ~20 W |
| **ITAR** | ITAR-free |
| **Moving parts** | None (fully solid-state) |
| **Jamming immunity** | Passive sensor — cannot be jammed |
| **GPS dependency** | None — operational in GPS-denied areas |

### 4.2 Detection Performance

| Parameter | Specification |
|-----------|--------------|
| **Detection range** | 300-500m typical; up to 1 km (source-dependent) |
| **Frequency range** | 200 Hz - 20 kHz |
| **Field of view** | 105° per sensor |
| **Direction accuracy** | <10° (azimuth and elevation) |
| **SNR** | <85 dB (system-level) |
| **360° coverage** | Yes, from single sensor (horizontal mount) |
| **Target classes** | Class I drones (<25 kg), Class II drones (25-150 kg) |
| **Other threats** | RAM (rockets, artillery, mortars), snipers, vehicles |
| **False positive rate** | "Close to zero" (ML suppresses non-target sounds) |
| **Unknown drone detection** | Yes — trained on propeller signatures, not specific models |

### 4.3 Deployment Modes

| Mode | Configuration | Use Case |
|------|---------------|----------|
| **Horizontal** | Flat-mounted (tripod, vehicle, roof) | Rapid deployment, 360° hemisphere |
| **Vertical** | Upright on pole/wall | Improved range, directional coverage |
| **Networked** | Multiple G2+ sensors linked | Perimeter/border protection grid |
| **Standalone** | Single sensor with local display | SOF, ad-hoc deployment |

### 4.4 Communication & Integration

| Interface | Protocol/Standard |
|-----------|-------------------|
| **Network** | Ethernet (implied by browser/API connectivity) |
| **User interface** | Browser-based (any network-connected device) |
| **Machine-to-machine** | Flexible API |
| **TAK integration** | ATAK (Android), WinTAK |
| **NATO standard** | SAPIENT (Sensing for Asset Protection with Integrated Electronic Networked Technology) |
| **DroneShield** | DroneSentry-C2 command-and-control |
| **Custom** | Open API for BMS/C2 integration |

---

## 5. PERFORMANCE COMPARISON

### 5.1 Discovair G2+ vs LOMAH Systems

| Feature | Discovair G2+ | Saab SASS-4 | Polytronic H-Bar | InVeris LOMAH |
|---------|--------------|-------------|-------------------|---------------|
| **Primary purpose** | Threat detection | Bullet scoring | Bullet scoring | Bullet scoring |
| **Microphones** | 128 MEMS | 4 pressure | 8 pressure (2×4) | 4-8 pressure |
| **Algorithm** | Beamforming + ML | TDOA (cal-free) | TDOA | TDOA |
| **Positional accuracy** | <10° bearing | ±10mm XY | ±5mm XY | <5mm XY |
| **Detection range** | 300-1000m | 3×2.5m zone | 3×3m zone | ~3×2.5m zone |
| **Min projectile speed** | Any (sound-based) | Mach 1.3 | Mach 1.3 | Supersonic |
| **Subsonic capability** | Yes (any sound) | No | No (acoustic) | No |
| **Weight** | 8 kg | ~10-15 kg (est.) | ~8-12 kg (est.) | ~10 kg (est.) |
| **Power** | 24-48V, 20W | 12V battery | 12V/24V | 12V/24V |
| **IP rating** | IP65 | IP67 (est.) | IP65+ | IP67 (est.) |
| **Temp range** | -40 to +70°C | -25 to +70°C | -20 to +55°C | -25 to +70°C |
| **MIL-STD** | 810H | Not confirmed | Not confirmed | 810H |
| **ML/AI** | Yes (classification) | No | No | No |
| **Camera** | Integrated | No | No | No |
| **Calibration** | Not applicable | Calibration-free | Required | Required |
| **ITAR** | ITAR-free | Unknown | Non-ITAR (Swiss) | ITAR (US) |

### 5.2 Key Differentiators

**Discovair G2+ advantages over traditional LOMAH:**
1. **128 vs 4-8 microphones** — massively more spatial information
2. **Beamforming** — steerable, multi-directional, not locked to one target plane
3. **ML classification** — can distinguish sound types, not just detect shockwaves
4. **Any sound speed** — no Mach 1.3 minimum (could detect subsonic projectiles)
5. **No calibration** — inherently calibration-free due to beamforming approach
6. **On-edge processing** — self-contained, no external processor needed
7. **Integrated camera** — visual confirmation capability
8. **MIL-STD-810H certified** — verified, not estimated
9. **ITAR-free** — no export restrictions

**Discovair G2+ limitations for LOMAH application:**
1. **No positional accuracy** — <10° bearing ≠ ±5mm XY position
2. **Not designed for scoring** — no X,Y coordinate output
3. **No target silhouette** — no hit/miss classification against target figure
4. **No range control integration** — no FASIT, no target lifter interface
5. **Different form factor** — pizza box vs target-mounted bar
6. **Higher cost** — likely $10K-30K+ vs $300-500 per LOMAH lane
7. **Overkill for bullet scoring** — 128 mics when 4-8 suffice for TDOA

---

## 6. PATENTS & INTELLECTUAL PROPERTY

### 6.1 Granted Patents

| Patent | Title | Filed | Granted | Key Inventors |
|--------|-------|-------|---------|---------------|
| **US 11,832,051** | Microphone Arrays | 2019-09-13 | 2023-11-28 | Hafizovic, Berg, Nyvold |
| **US 10,557,916** | UAV Detection | 2016-11-07 | 2020-02-11 | Hafizovic, Nyvold, Helgesen, Daleng, Olsen |

### 6.2 Patent Applications

| Application | Title | Filed | Status | Key Inventors |
|-------------|-------|-------|--------|---------------|
| **US 2015/0039314** | Speech Recognition Method Based on Sound Mapping | 2011-12-20 | Application | Kjølerbakken |
| **US 2010/0254543** | Conference Microphone System | 2010-02-02 | Application | Kjølerbakken |
| **US 2008/0247567** | Directional Audio Capturing | 2006-09-29 | Application | Kjølerbakken, Jahr, Hafizovic |

### 6.3 Key Patent Analysis

**US 11,832,051 — Microphone Arrays (Core Hardware Patent)**

| Parameter | Detail |
|-----------|--------|
| **Claim scope** | Circular microphone array with multiple simultaneous beamforming algorithms |
| **Key innovation** | Isolating different sound sources from different directions simultaneously |
| **Array geometry** | Circular arrangement (proprietary pattern — this is the "trippy pattern" mentioned on their website) |
| **Status** | **ACTIVE — granted 2023** |
| **Freedom to operate** | Must design around circular array geometry claims |

**US 10,557,916 — UAV Detection (Core Software Patent)**

| Parameter | Detail |
|-----------|--------|
| **Claim scope** | Spatial detection probability map fusing audio analysis score, audio intensity score, and video analysis score |
| **Key innovation** | Multi-modal fusion (acoustic + visual) for drone classification |
| **ML component** | Trained classifier on beamformed spatial audio |
| **Status** | **ACTIVE — granted 2020** |
| **LOMAH relevance** | LOW — specific to UAV detection, not projectile scoring |

**US 2008/0247567 — Directional Audio Capturing (Foundational)**

| Parameter | Detail |
|-----------|--------|
| **Claim scope** | Method for capturing directional audio using microphone array |
| **Key innovation** | Original beamforming approach |
| **Status** | Application (likely abandoned or incorporated into later patents) |
| **LOMAH relevance** | MEDIUM — general beamforming method could apply |

### 6.4 IP Landscape Assessment for VN-LOMAH

| Technology | Patent Status | Freedom to Operate |
|------------|--------------|-------------------|
| Beamforming (general) | Public domain (decades-old technique) | **FREE** |
| Circular array geometry | US 11,832,051 ACTIVE | **DESIGN AROUND** — use different geometry |
| UAV detection fusion | US 10,557,916 ACTIVE | **FREE** — not applicable to LOMAH |
| TDOA scoring (Saab) | WO1991010876A1 EXPIRED | **FREE** — calibration-free TDOA available |
| Digital MEMS microphones | Not patented by SQH | **FREE** — commodity components |
| ML sound classification | Trade secret (model weights) | **FREE** — train own model |

**Conclusion:** Squarehead's active patents cover their specific circular array geometry and UAV detection fusion method. Neither directly blocks a LOMAH implementation. The general beamforming technique and MEMS microphone array concept are freely practicable.

---

## 7. KNOWN CONTRACTS & CUSTOMERS

### 7.1 Confirmed Contracts

| Customer | Detail | Value | Year |
|----------|--------|-------|------|
| **Norwegian Armed Forces** | P5007 counter-battery acoustic sensors | Not disclosed | 2025 |
| **Norwegian Defence Materiel Agency** | Via OSL, C-UAS at Ørland Air Station | NOK 938M (framework, SQH as sub-supplier) | 2025 |
| **US DOD** | DroneShield + Discovair combined C-UAS evaluation | Not disclosed | 2021 |
| **USSOCOM** | Arctic conditions exercise testing in Norway | Not disclosed | ~2022 |
| **European Defense Fund** | E-CUAS project member | EU funded | 2025 |
| **European Defense Fund** | PROTEAS project — acoustic situational awareness | EU funded | 2025 |
| **NATO** | Fast-Track Defense Tech Challenge (selected) | N/A | 2026 |
| **G20 Summit** | Discovair deployed for event security, Hamburg | Not disclosed | 2017 |

### 7.2 Partners

| Partner | Relationship | Detail |
|---------|-------------|--------|
| **DroneShield** (ASX: DRO, Australia) | Technology integration | Discovair G2 integrated into DroneSentry-C2 (2020) |
| **OSL (Operational Solutions Ltd)** | Prime contractor | Squarehead as sub-supplier for Norwegian C-UAS |
| **Siphon** (Norway) | Distributor | Norwegian distribution |

### 7.3 Market Reach

| Metric | Value |
|--------|-------|
| **Countries served** | "Allied countries around the world" (specific count undisclosed) |
| **Combat deployment** | "Proven track record... with armed forces in active combat" |
| **Civilian deployments** | G20 Summit, marathons, motor sports events |
| **NATO alignment** | SAPIENT protocol compatible |

---

## 8. SIGNAL PROCESSING CHAIN

```
                DISCOVAIR G2+ SIGNAL PROCESSING CHAIN
                ═════════════════════════════════════

PHYSICAL            TRANSDUCTION         DIGITAL               INTELLIGENCE
────────            ────────────         ───────               ────────────
Sound wave ──→ 128 MEMS ──→ Digital ──→ Beamforming ──→ ML Classifier
 (any audible    Microphones   Streams    Engine            (on-edge)
  source)        (digital      (128 ch    (multi-beam,          │
                  output)       parallel)  steerable)           ▼
                                              │           Classification
                                              │           (drone/RAM/
                                              │            sniper/vehicle/
                                              │            unknown)
                                              ▼                │
                                         Acoustic              ▼
                                         Image Map        Alert + Bearing
                                         (spatial             │
                                          heatmap)            ▼
                                              │          ┌────────────┐
                                              └──────────│ API Output │
                                                         │ • Bearing  │
                                                         │ • Elevation│
                                                         │ • Class    │
                                                         │ • Conf.    │
                                                         │ • Camera   │
                                                         └────────────┘
                                                              │
                                                    ┌─────────┴──────────┐
                                                    ▼                    ▼
                                               Browser UI          C2 System
                                               (operator)     (TAK/SAPIENT/BMS)
```

### Estimated Component Architecture

| Stage | Component | Specification (Estimated) |
|-------|-----------|--------------------------|
| **Microphone** | Digital MEMS | ICS-43434 or similar, omnidirectional, SNR >65 dB, <1mm package |
| **Array PCB** | Multi-layer PCB | 128 MEMS in proprietary circular pattern, integrated digital bus |
| **ADC** | Integrated in MEMS | Digital output from each mic (PDM or I²S) |
| **FPGA/SoC** | Embedded processor | Likely Xilinx Zynq or similar (FPGA fabric + ARM cores) |
| **Beamforming** | FPGA accelerated | Real-time 128-channel beamforming, multiple simultaneous beams |
| **ML inference** | ARM/GPU | TensorFlow Lite or similar edge-optimized framework |
| **Camera** | CMOS sensor | Visible-light, medium resolution for visual reference |
| **Network** | Ethernet PHY | 100/1000BaseT for API/browser connectivity |
| **Power** | DC-DC converters | 24-48V input → internal rails (3.3V, 1.8V, 1.0V) |
| **Enclosure** | IP65 housing | Ruggedized, MIL-STD-810H, ~8 kg total |

---

## 9. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 9.1 Overall Function

```
┌──────────────────────────────────────────────────────────────────────┐
│                     DISCOVAIR G2+                                     │
│                                                                      │
│  INPUT:                            OUTPUT:                           │
│  • Sound waves (any audible)       • Threat bearing (azimuth)        │
│  • Visual scene (camera)           • Threat elevation                │
│  • 24-48 VDC power                 • Threat classification           │
│  • Network connection              • Confidence score                │
│                                    • Visual reference image          │
│  FUNCTION:                         • API data stream                 │
│  "Passively detect, localize,      • Browser display                 │
│   and classify acoustic threats                                      │
│   using beamforming array and                                        │
│   machine learning"                                                  │
└──────────────────────────────────────────────────────────────────────┘
```

### 9.2 Sub-Function Structure

```
F0: Detect, Localize & Classify Acoustic Threats (Passive)
│
├── F1: SENSE - Multi-Channel Sound Capture
│   ├── F1.1: Receive sound waves at 128 MEMS microphones
│   ├── F1.2: Convert acoustic pressure to digital signal (per mic)
│   ├── F1.3: Synchronize 128 digital streams (clock distribution)
│   └── F1.4: Monitor all sectors for acoustic changes (threshold)
│
├── F2: PROCESS - Digital Beamforming
│   ├── F2.1: Apply phase delays for beam steering
│   ├── F2.2: Form multiple simultaneous beams (spatial filter)
│   ├── F2.3: Scan 105° FoV across monitored sectors
│   ├── F2.4: Isolate sound from detected change direction
│   └── F2.5: Generate acoustic spatial heatmap
│
├── F3: CLASSIFY - Machine Learning Inference
│   ├── F3.1: Extract acoustic features from beamformed signal
│   ├── F3.2: Run ML classifier (drone/RAM/sniper/vehicle/other)
│   ├── F3.3: Compute classification confidence score
│   ├── F3.4: Suppress non-threat classifications (zero false positives)
│   └── F3.5: Track classified target over time
│
├── F4: FUSE - Multi-Modal Integration
│   ├── F4.1: Capture visual frame from integrated camera
│   ├── F4.2: Fuse acoustic bearing with camera field
│   ├── F4.3: Generate spatial detection probability map
│   └── F4.4: Slew-to-cue for visual confirmation
│
├── F5: COMMUNICATE - Data Output
│   ├── F5.1: Serve browser-based operator display
│   ├── F5.2: Stream API data (bearing, class, confidence)
│   ├── F5.3: Interface with TAK/SAPIENT/C2 systems
│   └── F5.4: Network with other Discovair units (multi-sensor grid)
│
├── F6: POWER - Energy Management
│   ├── F6.1: Accept 24-48 VDC input
│   ├── F6.2: Regulate to internal rails (3.3V, 1.8V, 1.0V)
│   └── F6.3: Power budget management (~20W total)
│
└── F7: SURVIVE - Environmental Protection
    ├── F7.1: IP65 sealing (dust-tight, water jet)
    ├── F7.2: MIL-STD-810H environmental qualification
    ├── F7.3: -40°C to +70°C operation
    └── F7.4: No moving parts (solid-state reliability)
```

---

## 10. POWER SYSTEMS

| Option | Application | Detail |
|--------|-------------|--------|
| **24 VDC** | Standard field power | Battery or vehicle power bus |
| **48 VDC** | PoE or infrastructure | Range/base installation |
| **~20 W** | Total power draw | Low SWaP (Size, Weight, and Power) |
| **Solar** | Possible with 24V solar panel | 50W panel sufficient with battery |
| **Battery** | Field deployment | ~10h on 200Wh battery (estimated) |

---

## 11. BOM ESTIMATE (Vietnamese Production Context)

### 11.1 Discovair G2+ Equivalent — Estimated BOM

| Subsystem | Components | Est. Cost (USD) | Local Content |
|-----------|-----------|-----------------|---------------|
| **128 MEMS microphones** | Digital MEMS (e.g., ICS-43434) at ~$1-2 each | $130-260 | 0% (import all) |
| **Array PCB** | Multi-layer PCB, proprietary geometry, connectors | $40-80 | 70% (PCB fab local) |
| **FPGA/SoC module** | Xilinx Zynq or Intel Cyclone (beamforming + ARM) | $80-200 | 10% (module import) |
| **Camera module** | CMOS camera + lens + interface | $15-30 | 20% (module import) |
| **Power supply** | DC-DC converters, protection, filtering | $20-40 | 50% (PCB local, ICs import) |
| **Enclosure** | IP65 aluminum/polymer housing, MIL-STD rated | $50-100 | 80% (machined locally) |
| **Connectors** | IP-rated power, Ethernet, mounting hardware | $20-40 | 40% (import mil-spec) |
| **Firmware/software** | Beamforming algorithms, ML models, API | $0 (embedded) | 100% (domestic dev) |
| **Assembly & test** | Integration, calibration, QC | $30-50 | 90% (local labor) |
| **TOTAL per unit** | | **$385-800** | **~45-55%** |

### 11.2 Key Insight: MEMS Array as LOMAH Alternative

A beamforming array using 128 MEMS microphones could potentially serve as a LOMAH sensor if:
1. Signal processing is optimized for supersonic shockwave detection (not drone propellers)
2. Beamforming resolution is sufficient for ±5-10mm positional accuracy at 1-3m range
3. Output is converted to X,Y coordinates rather than bearing/elevation

**Cost comparison:**
| Approach | Sensor Cost | Accuracy | Subsonic |
|----------|------------|----------|----------|
| Traditional LOMAH (4 mic TDOA) | $45-75 | ±5-10mm | No |
| Beamforming array (128 MEMS) | $250-500 | TBD (requires R&D) | Potentially yes |

The beamforming approach costs 3-7× more per sensor but could potentially offer subsonic detection capability and wider detection zones — significant advantages over traditional TDOA LOMAH.

---

## 12. COMPETITIVE COMPARISON — C-UAS Acoustic Sensors

| Feature | Discovair G2+ | Dedrone DroneTracker | RADA MHR | Robin Radar Elvira |
|---------|--------------|---------------------|----------|-------------------|
| **Type** | Acoustic array | RF + acoustic | Radar (AESA) | Radar (FMCW) |
| **Passive** | Yes | Partially | No | No |
| **Drone detection** | Yes | Yes | Yes | Yes |
| **C-RAM** | Yes | No | Yes | No |
| **Jammable** | No | Partially | Yes (ARMs) | Yes (ARMs) |
| **Weight** | 8 kg | ~5 kg | ~30 kg | ~20 kg |
| **Power** | 20W | ~15W | ~150W | ~80W |
| **Weather** | IP65, MIL-810H | IP65 | IP67 | IP65 |
| **Range** | 300-1000m | 500m (acoustic) | 5 km+ | 3 km+ |
| **ITAR** | Free | Unknown | ITAR | Non-ITAR |

Discovair G2+ is the **market leader in passive acoustic C-UAS** — the key differentiator is that it cannot be jammed, hacked, or detected (emits nothing).

---

## 13. DESIGN INSIGHTS FOR VIETNAMESE PRODUCT

### 13.1 Technology Transfer Relevance to VN-LOMAH

| Technology | Relevance | Adoption Risk | Priority |
|------------|-----------|---------------|----------|
| **Beamforming algorithms** | HIGH — could enable subsonic LOMAH | MEDIUM — needs R&D for projectile accuracy | Phase 2-3 |
| **128 MEMS microphone array** | MEDIUM — higher-res alternative to 4-mic TDOA | LOW — commodity components | Phase 2 |
| **Digital MEMS vs analog pressure transducers** | HIGH — lower cost, better availability | LOW — well-proven technology | **Phase 1** |
| **On-edge processing** | HIGH — self-contained, no external server | LOW — standard embedded design | **Phase 1** |
| **ML classification** | MEDIUM — could classify caliber, weapon type | MEDIUM — needs training data | Phase 3 |
| **IP65/MIL-STD-810H design** | HIGH — proven ruggedization approach | LOW — standard practices | **Phase 1** |
| **Browser-based UI** | HIGH — matches TrueZero-inspired web interface | LOW — standard web dev | **Phase 1** |
| **API-first architecture** | HIGH — enables C2/BMS integration | LOW — standard practice | **Phase 1** |
| **Camera integration** | LOW — not needed for LOMAH scoring | N/A | Not applicable |
| **ITAR-free design** | HIGH — eliminates export restrictions for VN | LOW — component selection | **Phase 1** |

### 13.2 Key Lessons from Squarehead

1. **Digital MEMS microphones are a viable alternative to pressure transducers** — At $1-2 each vs $10-20 for specialized acoustic pressure transducers, MEMS mics dramatically reduce sensor cost. Vietnamese LOMAH should evaluate MEMS for shockwave detection.

2. **On-edge processing is the modern standard** — Discovair processes everything locally on a single-board computer. No external processor box needed. VN-LOMAH should follow this architecture rather than the legacy BSU → TPU → VDU chain used by Saab/InVeris.

3. **Beamforming could solve the subsonic LOMAH problem** — Traditional TDOA requires supersonic projectiles (Mach 1.3+). Beamforming with 128 mics could potentially detect and locate subsonic rounds (9mm, .45 ACP) by their aerodynamic turbulence — a capability that only Polytronic achieves today (with radar, not acoustics). This is a high-value R&D direction for Phase 2-3.

4. **MIL-STD-810H is achievable at small scale** — Squarehead is a ~50-person company that achieved MIL-STD-810H certification. This proves it's accessible for a small Vietnamese team without major infrastructure.

5. **API-first + browser UI eliminates proprietary display hardware** — Saab's VDU-1 and ROPU are proprietary display units. Discovair's approach (browser UI + API) means any tablet or laptop can serve as the operator display. VN-LOMAH should adopt this.

6. **ITAR-free component selection enables unrestricted export** — By choosing ITAR-free components (European MEMS, non-US FPGAs like Lattice/Intel), VN-LOMAH can be exported without US State Department restrictions.

7. **ML-based sound classification is the future** — Beyond hit/miss scoring, ML could classify weapon type, caliber, and even detect unsafe conditions (ricochets, cross-fire). This is a Phase 3+ differentiator.

### 13.3 Hybrid Architecture Concept (TDOA + Beamforming)

Based on insights from both traditional LOMAH systems and Discovair G2+, the VN-LOMAH could pioneer a **hybrid approach**:

```
VN-LOMAH Hybrid Architecture Concept
│
├── TIER 1: TDOA Scoring (Supersonic) — Phase 1
│   • 4-8 MEMS microphones on target frame (Saab-inspired)
│   • Calibration-free TDOA algorithm (expired patent)
│   • ±10mm accuracy, Mach 1.3+ projectiles
│   • $45-75 per sensor unit
│
├── TIER 2: Beamforming Array (All Speeds) — Phase 2-3
│   • 32-64 MEMS microphones in planar array (Discovair-inspired)
│   • Beamforming + ML for subsonic projectile detection
│   • Potentially ±15-25mm accuracy (R&D needed)
│   • Enables 9mm, .45 ACP, .22LR scoring
│   • $150-350 per array unit
│
├── TIER 3: ML Classification — Phase 3
│   • Weapon type / caliber identification
│   • Ricochet / unsafe condition detection
│   • Anomaly flagging for range safety
│
└── COMMON: On-Edge Processor + Browser UI + API
    • Single SoC (FPGA + ARM) for both TDOA and beamforming
    • Browser-based display (any device)
    • API for range control integration
    • ITAR-free, TCVN + MIL-STD compliant
```

### 13.4 Updated Vietnamese Product Concept (Incorporating Discovair Insights)

| Feature | Previous Concept | Updated with Discovair Insights |
|---------|-----------------|-------------------------------|
| **Microphones** | Pressure transducers (import) | **MEMS digital** ($1-2 each, easier to source) |
| **Processing** | FPGA + ARM MCU (separate) | **SoC on-edge** (self-contained, no TPU box) |
| **Display** | Web-based | **Browser UI + flexible API** (TAK/SAPIENT-compatible) |
| **Subsonic** | Phase 4 (radar, Polytronic-inspired) | **Phase 2-3 (beamforming, Discovair-inspired)** |
| **Classification** | None | **ML caliber/weapon classification** (Phase 3) |
| **Environmental** | IP67 target | **MIL-STD-810H** (proven achievable at small scale) |
| **Export** | Unknown | **ITAR-free design** (deliberate component selection) |

---

## 14. INTELLIGENCE GAPS

| Gap | Impact | Workaround |
|-----|--------|-----------|
| Exact array geometry (microphone positions) | Critical for beamforming design | Develop own geometry; general principles published |
| ML model architecture and training data | High for classification | Train on own data; standard audio ML techniques |
| Specific MEMS microphone model used | Low | Use comparable digital MEMS (ICS-43434, SPH0645) |
| Internal SoC/FPGA selection | Medium | Select based on Vietnamese supply chain access |
| Beamforming algorithm specifics | Medium | Published literature covers delay-and-sum, MVDR, MUSIC |
| Detection range for projectile shockwaves | **Critical** | Requires R&D: can beamforming achieve ±10mm at 2m? |
| Pricing per unit | Medium for business case | Estimate $10K-30K based on similar defense sensors |
| Specific military customers | Low | Focus on capability, not customer list |
| Camera specifications | Low (not needed for LOMAH) | N/A |
| Long-term reliability data | Medium | MIL-STD-810H provides baseline confidence |

---

## 15. REFERENCES

### Public Sources Used

| # | Source | Type | Key Data |
|---|--------|------|----------|
| 1 | sqhead.com/defense | Product page | G2+ specs, features, deployment modes |
| 2 | sqhead.com/technology | Technology | Beamforming explanation, ML approach |
| 3 | sqhead.com/company/about-us | Corporate | Founding story, personnel |
| 4 | sqhead.com/drone-detection | Application | C-UAS capabilities, use cases |
| 5 | sqhead.com/c-ram | Application | C-RAM detection, multi-sensor approach |
| 6 | siphon.no/squarehead-discovair-g2 | Distributor | 128 mics, patented arrays, modular/scalable |
| 7 | cuashub.com/en/product/discovair-g2 | Product database | 105° FoV, 8 kg, 20W |
| 8 | patents.justia.com/assignee/squarehead-technology-as | Patents | 5 patents/applications listed |
| 9 | droneshield.com | Partner | DroneShield integration details |
| 10 | hstoday.us | News | DOD testing of DroneShield+Discovair |
| 11 | robinradar.com | Industry analysis | Pros/cons of acoustic detection |
| 12 | crunchbase.com/organization/squarehead-technology | Corporate | Funding, employees |
| 13 | robaid.com | News | AudioScope origin, founders |
| 14 | edfproteas.eu | EU project | PROTEAS acoustic situational awareness |

### Patent References

| Patent | Status | LOMAH Relevance |
|--------|--------|----------------|
| US 11,832,051 (Microphone Arrays) | **ACTIVE** (2023) | MEDIUM — array geometry claims |
| US 10,557,916 (UAV Detection) | **ACTIVE** (2020) | LOW — UAV-specific |
| US 2008/0247567 (Directional Audio) | Application | LOW — general beamforming |
| US 2015/0039314 (Speech Recognition) | Application | NONE |
| US 2010/0254543 (Conference Mic) | Application | NONE |

---

## 16. CROSS-REFERENCE TO OTHER VN-LOMAH RE ANALYSES

| Competitor | Key Technology | Discovair Comparison |
|-----------|---------------|---------------------|
| [[RE_saab_lomah]] | Calibration-free TDOA, 4/9 transducers | Different paradigm: beamforming vs TDOA |
| [[RE_polytronic_international_ag_lomah]] | Dual delta arrays, radar H-Bar for subsonic | Discovair beamforming could compete with radar for subsonic |
| [[RE_inveris_training_solutions_lomah]] | Portable LOMAH, FASIT, wireless | Discovair has better API architecture |
| [[RE_theissen_training_systems_lomah]] | US Army PEO STRI, BIT diagnostics | Discovair has superior self-diagnostics (ML-based) |
| [[RE_SIUS_Analysis]] | Swiss precision, electronic target | Different domain (electronic vs acoustic) |
| [[RE_zen_technologies_smart_electronic_target]] | Indian cost-effective LOMAH | Discovair is higher-cost, higher-capability |
| [[RE_OakwoodHBar_Analysis]] | H-Bar portable LOMAH | Same class as Polytronic/Saab |
| [[RE_TrueZeroTarget_Analysis]] | Low-cost web-based display | Discovair shares browser UI philosophy |

---

*Analysis compiled from publicly available sources only. No classified, ITAR-controlled, or proprietary information included. All specifications are estimates based on published data, patent disclosures, trade show information, and industry comparisons.*

*Note: Discovair G2+ is a C-UAS/C-RAM sensor, NOT a LOMAH system. This analysis evaluates cross-domain technology relevance for the VN-LOMAH acoustic scoring project.*

*Created: 2026-02-11 | Project: VN-CUAS-001 | Phase: 0 (Reverse Engineering)*
