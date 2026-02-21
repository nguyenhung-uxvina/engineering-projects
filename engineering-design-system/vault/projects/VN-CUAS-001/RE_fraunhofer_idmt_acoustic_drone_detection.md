---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Fraunhofer IDMT Acoustic Drone Detection (Germany)
version: 1.0
created: 2026-02-11
status: complete
---

# RE: Fraunhofer IDMT Acoustic Drone Detection - Germany
## Reverse Engineering Analysis from Public Sources

> **KEY DISTINCTION:** Fraunhofer IDMT is a **government-funded applied research institute**, NOT a product company. Unlike Squarehead Technology (commercial product) or BeephoniX (startup product), Fraunhofer IDMT offers **licensable algorithms and technology building blocks** for acoustic drone detection. This makes it a potential **technology partner** rather than a competitor for Vietnamese C-UAS development — or a source of publicly-funded research insights that can inform indigenous design.

---

## 1. ORGANIZATION PROFILE

| Item | Detail |
|------|--------|
| **Organization** | Fraunhofer Institute for Digital Media Technology (Fraunhofer IDMT) |
| **Branch** | Oldenburg Branch for Hearing, Speech and Audio Technology (HSA) |
| **Address** | Marie-Curie-Straße 2, 26129 Oldenburg, Germany |
| **Phone** | +49 441 80097-400 |
| **Fax** | +49 441 8009759-400 |
| **IDMT HQ** | Ilmenau, Thuringia, Germany |
| **HSA Branch Founded** | 2008 |
| **Parent Organization** | Fraunhofer-Gesellschaft (Europe's largest applied research org) |
| **Fraunhofer Scale** | 76 institutes, ~30,000 employees, €3.4B annual budget |
| **Type** | Government-funded applied research institute (NOT commercial product company) |
| **Business Model** | Technology licensing, contract R&D, algorithm integration, system prototypes |
| **Key Offering** | Integrable algorithms for UAS detection/localization + complete system solutions |
| **ITAR Status** | Non-ITAR (German/EU) |
| **Core Competency** | Audio signal processing, ML-based acoustic event detection, hearing technology |

### Key Personnel (HSA Branch)

| Name | Role | Background |
|------|------|------------|
| **Prof. Dr. Dr. Birger Kollmeier** | Director, Oldenburg Branch HSA | Co-founder HSA (2008); dual doctorate (rer. nat. + med.); Professor at University of Oldenburg |
| **Dr. Jens-E. Appell** | Head of Department, HSA | Co-founder HSA (2008); Dr. rer. nat.; department-level management |
| **Christian Rollwage** | Head of Audio Signal Enhancement | Lead for drone detection technology; primary spokesperson for C-UAS work |
| **Danilo Hollosi** | Head of Acoustic Event Detection | Acoustic monitoring, machine listening for smart decisions |
| **Menno Müller** | Head of Audio System Technology | Hardware design, demonstrators, acoustic end-of-line inspection |
| **Alexander Schwarz** | Head of Intelligent Audio Interaction | Speech recognition for products and processes |
| **Prof. Dr. Jan Rennies-Hochmuth** | Head of Personalized Hearing Systems | Sound quality, speech intelligibility |
| **Dr.-Ing. Insa Wolf** | Head of Mobile Neurotechnologies | Brain-computer interfaces, mobile neuro systems |
| **Laura Tuschen** | Head of Assistive Speech and Language Analysis | Digital speech processing for assistive tech |
| **Christian Colmer** | Head of Marketing & Communication | Oldenburg Branch marketing |

### Organizational Structure (HSA Branch — Drone Detection Context)

```
Fraunhofer-Gesellschaft (76 institutes)
│
├── Fraunhofer IDMT (HQ: Ilmenau, Germany)
│   │
│   └── Oldenburg Branch: HSA (Hearing, Speech and Audio Technology)
│       ├── Founded: 2008 by Kollmeier & Appell
│       │
│       ├── Research Groups:
│       │   ├── Personalized Hearing Systems (Rennies-Hochmuth)
│       │   ├── Mobile Neurotechnologies (Wolf)
│       │   ├── Intelligent Audio Interaction (Schwarz)
│       │   ├── Audio System Technology (Müller)
│       │   ├── Acoustic Event Detection (Hollosi)  ←── Drone classification
│       │   ├── Audio Signal Enhancement (Rollwage)  ←── Drone detection lead
│       │   ├── Assistive Speech and Language Analysis (Tuschen)
│       │   └── Evaluation and User Studies
│       │
│       └── Key Projects:
│           ├── AMBOS (BMBF) — Drone detection (since 2016)
│           ├── ALADDIN (H2020) — European drone detection
│           ├── "The Hearing Car" — Acoustic sensors for vehicles
│           ├── Connected Health — Networked healthcare
│           └── HSN4Production — Industrial acoustic monitoring
│
└── (75 other Fraunhofer institutes)
```

### Academic Partnerships

| Partner | Relationship |
|---------|-------------|
| **Carl von Ossietzky University of Oldenburg** | Primary academic partner; shared campus and faculty |
| **Jade University of Applied Sciences** | Scientific cooperation |
| **University of Applied Sciences Emden/Leer** | Scientific cooperation |
| **"Hearing4all" Cluster of Excellence** | Partner (DFG-funded excellence initiative) |
| **Collaborative Research Centre "Hearing Acoustics"** | Partner |

### Historical Lineage (Drone Detection)

| Year | Event |
|------|-------|
| 2008 | Oldenburg Branch HSA founded by Prof. Kollmeier and Dr. Appell |
| ~2010-2015 | HSA develops expertise in acoustic event detection, MEMS arrays, ML classification |
| 2016 | AMBOS project launched (BMBF-funded, 12 partners, led by Fraunhofer FKIE) — first drone detection R&D |
| 2016-2020 | ALADDIN project (H2020, 18 partners, 9 EU countries, led by CS Group) — European-scale drone detection |
| 2020-2024 | Continued internal R&D; algorithm refinement through multiple internal projects |
| 2025 (Jun) | "The Hearing Car" acoustic sensor test drive for autonomous vehicles |
| 2025 (Sep) | IAA Mobility 2025: "The Hearing Car" demonstration |
| 2025 (Nov) | Public announcement of integrated acoustic drone detection system (press release) |
| 2025 (Nov) | Multiple industry publications cover Fraunhofer IDMT drone detection |
| 2026 (Jan) | NAMM 2026: "Speech Intelligibility Meter" and sound optimization (audio expertise showcase) |

---

## 2. PRODUCT / TECHNOLOGY PORTFOLIO

> **Critical distinction:** Fraunhofer IDMT does NOT sell off-the-shelf "products" like Squarehead or BeephoniX. It offers **technology building blocks** — algorithms, prototypes, and integration services — that customers embed into their own systems.

```
Fraunhofer IDMT HSA — Technology Portfolio (Drone Detection Context)
│
├── LICENSABLE ALGORITHMS
│   ├── Acoustic drone detection (ML-based classification)
│   ├── Acoustic drone localization (beamforming + TDOA)
│   ├── Acoustic fingerprint database and matching
│   ├── Multi-channel noise suppression
│   ├── Beamforming algorithms (MEMS arrays)
│   └── Acoustic event detection (general-purpose)
│
├── COMPLETE SYSTEM SOLUTIONS
│   ├── Integrated acoustic drone sensor prototype
│   ├── 360° coverage sensor unit
│   ├── 8-microphone mobile airport sensor (demonstrated)
│   └── Custom sensor arrays (contract R&D)
│
├── SENSOR DATA FUSION INTEGRATION
│   ├── Acoustic + radar fusion
│   ├── Acoustic + camera fusion
│   ├── Acoustic + LiDAR fusion
│   └── Wake-up trigger for secondary sensors
│
├── ADJACENT TECHNOLOGIES (Same Core Competency)
│   ├── "The Hearing Car" — Vehicle acoustic environment sensing
│   ├── Industrial acoustic monitoring (machine condition)
│   ├── Speech recognition (edge and cloud)
│   ├── Acoustic end-of-line inspection (manufacturing QC)
│   ├── Meadow bird detection (nature conservation)
│   └── Hearing aid / cochlear implant signal processing
│
└── FUTURE EXTENSIONS (Announced)
    ├── Vehicle detection (acoustic classification)
    ├── Gunshot detection and localization
    └── Extended range through sensor networking
```

### Business Model Comparison

| Aspect | Squarehead | BeephoniX | **Fraunhofer IDMT** |
|--------|-----------|-----------|-------------------|
| **Type** | Product company | Startup product company | **Research institute** |
| **Offering** | Discovair G2+ (packaged product) | M2 (packaged sensor) | **Algorithms + prototypes + integration** |
| **Customer gets** | Complete sensor unit | Complete sensor unit | **Technology building blocks to embed** |
| **Revenue model** | Product sales | Product sales | **Licensing fees, contract R&D, grants** |
| **Production** | In-house manufacturing | In-house manufacturing | **No volume manufacturing** |
| **Maturity** | TRL 8-9 (fielded product) | TRL 6-7 (demonstrated) | **TRL 4-6 (prototype/demo)** |
| **Price** | $15K-50K/unit (est.) | $5K-15K/unit (est.) | **Contract-dependent (R&D pricing)** |
| **Vietnamese relevance** | Benchmark competitor | Innovation reference | **Potential technology partner** |

---

## 3. ACOUSTIC DRONE DETECTION SYSTEM ARCHITECTURE

### 3.1 System Topology

```
┌──────────────────────────────────────────────────────────────────────┐
│             FRAUNHOFER IDMT ACOUSTIC DRONE DETECTION SYSTEM           │
│                                                                      │
│  ACOUSTIC SENSOR UNIT                          SENSOR FUSION          │
│  ┌───────────────────────────┐                ┌──────────────────┐   │
│  │  MEMS Microphone Array     │   Data Feed    │  Fusion Node      │   │
│  │  (digital MEMS, count TBD) │───────────────→│  • Acoustic data  │   │
│  │                            │                │  + Radar data     │   │
│  │  On-Edge ML Processor      │                │  + Camera data    │   │
│  │  (classification + loc.)   │                │  + LiDAR data     │   │
│  │                            │                └──────────────────┘   │
│  │  Power: Battery-operable   │                        │              │
│  │  (low energy)              │                        ▼              │
│  └───────────────────────────┘                ┌──────────────────┐   │
│       │                                       │  C2 / Alert       │   │
│  DEPLOYMENT MODES                              │  System           │   │
│  ┌──────┐    ┌──────┐    ┌──────┐             │  • Threat alerts  │   │
│  │ Sn-A │    │ Sn-B │    │ Sn-C │             │  • Position data  │   │
│  │(360°)│    │(360°)│    │(360°)│             │  • Classification │   │
│  └──────┘    └──────┘    └──────┘             └──────────────────┘   │
│     ↓            ↓            ↓                                      │
│  ┌─────────────────────────────────────┐                             │
│  │  Networked Coverage                  │                             │
│  │  • Multiple sensors = wider area     │                             │
│  │  • "Hears around corners"           │                             │
│  │  • Triggers wake-up of other sensors │                             │
│  └─────────────────────────────────────┘                             │
└──────────────────────────────────────────────────────────────────────┘
```

### 3.2 Detection Principle: Acoustic Fingerprint + ML Classification

The Fraunhofer IDMT approach is distinctly **algorithm-centric** rather than hardware-centric:

**Stage 1: Acoustic Capture**
MEMS microphone array captures omnidirectional sound. The exact microphone count is not publicly fixed — Fraunhofer has demonstrated configurations from 8 microphones (mobile airport sensor) to larger arrays. The emphasis is on the algorithms, not a specific hardware configuration.

**Stage 2: Signal Enhancement**
Multi-channel noise suppression algorithms (the core expertise of the "Audio Signal Enhancement" group under Rollwage) clean the signal, separating drone acoustic signatures from environmental noise (wind, traffic, machinery, birds).

**Stage 3: Acoustic Fingerprint Matching**
Each drone type produces a unique acoustic signature — its "acoustic fingerprint" — determined by rotor speed, motor type, propeller geometry, and frame vibration. The ML system matches incoming signals against a database of known fingerprints.

**Stage 4: ML Classification**
Machine learning algorithms classify the detected sound:
- Drone vs. non-drone (detection)
- Drone type (classification)
- Direction of arrival (localization via beamforming/TDOA)

**Stage 5: Sensor Wake-Up (Unique Feature)**
Upon acoustic detection, the system can **trigger activation of secondary sensors** (radar, camera, LiDAR). This is a key architectural innovation — the low-power acoustic sensor serves as a "first alert" that cues higher-power, higher-resolution sensors only when needed, saving energy and reducing false alarms on expensive systems.

```
FRAUNHOFER IDMT DETECTION PIPELINE:
═══════════════════════════════════

SOUND CAPTURE      ENHANCEMENT        FINGERPRINT         CLASSIFICATION
──────────────    ─────────────      ────────────        ──────────────
MEMS Array ──→ Multi-Channel ──→ Acoustic ──→ ML Classifier
 (digital      Noise             Fingerprint    (drone type,
  MEMS mics)   Suppression       Matching       direction,
               (Rollwage group)  (database)     confidence)
                    │                                │
                    │                                ▼
                    │                          ┌──────────┐
                    │                          │ ALERT     │
                    │                          │ • Drone   │
                    │                          │   detected│
                    │                          │ • Type    │
                    │                          │ • Bearing │
                    │                          └──────────┘
                    │                               │
                    │                    ┌───────────┴──────────┐
                    │                    ▼                      ▼
                    │              Direct Alert          WAKE-UP TRIGGER
                    │              to C2 system          → Activate radar
                    │                                    → Activate camera
                    │                                    → Activate LiDAR
                    │                                    (save power on
                    │                                     expensive sensors)
                    │
                    └──→ "Hears around corners"
                         (works in built-up, forested areas
                          where LOS sensors fail)
```

### 3.3 Approach Comparison: Fraunhofer vs Squarehead vs BeephoniX

| Parameter | Fraunhofer IDMT | Squarehead G2+ | BeephoniX M2 |
|-----------|----------------|----------------|-------------|
| **Approach** | **Algorithm-centric** | Hardware product | Hardware product |
| **Microphones** | Flexible (8+, MEMS) | 128 MEMS (fixed) | 151 MEMS (fixed) |
| **Key innovation** | Acoustic fingerprint + ML | Beamforming array geometry | Bio-inspired Doppler |
| **Detection method** | ML pattern recognition | Digital beamforming + ML | Doppler beamforming + ML |
| **Localization** | Beamforming + TDOA | Beamforming | Bio-inspired beamforming |
| **Detection range** | 50-200 m | 300-1000 m | 200-900 m |
| **Temporal resolution** | 1 second | Real-time | Real-time |
| **Coverage** | 360° | 105° (or 360° horiz.) | Hemispherical |
| **Power** | **Battery-operable** (low energy) | 24-48V, 20W | Battery/solar |
| **Unique feature** | **Sensor wake-up trigger** | Established, MIL-certified | Ultra-light (950g) |
| **TRL** | 4-6 (prototype) | 8-9 (fielded) | 6-7 (demonstrated) |

---

## 4. DETAILED SPECIFICATIONS

### 4.1 Sensor System (Prototype Level)

| Parameter | Specification | Source |
|-----------|--------------|--------|
| **Microphone type** | Digital MEMS | Official (microphone arrays page) |
| **Microphone count** | Flexible; 8-mic mobile demonstrated | Press release, interview |
| **Array geometry** | Configurable (not fixed product form factor) | Implied by algorithm-centric approach |
| **Processing** | On-edge ML inference | Official |
| **Power** | Low energy, battery-operable | Official press release |
| **Power draw** | Not disclosed (estimated 3-10W based on MEMS + edge SoC) | Estimated |
| **Weight** | Not disclosed (prototype, not fixed product) | N/A |
| **IP rating** | Not disclosed (prototype) | N/A |
| **MIL-STD** | Not pursued (research institute) | N/A |
| **Operating temperature** | Not disclosed | N/A |
| **ITAR** | Non-ITAR (German/EU) | Implied |

### 4.2 Detection Performance

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Detection range** | **50-200 m** | Environment-dependent; lower in noisy environments |
| **Temporal resolution** | **1 second** | Update rate for detection/classification |
| **Coverage** | **360°** | Per sensor unit |
| **Localization** | Bearing (beamforming/TDOA) | Azimuth + elevation |
| **Classification** | Drone type identification | ML-based acoustic fingerprint |
| **False positive rate** | Not specified (ML-suppressed) | Algorithm-dependent |
| **Drone classes** | Not explicitly stated | Implied: small commercial + FPV |
| **Other detectable events** | Vehicles, gunshots (announced) | Future extension |
| **NLOS capability** | **Yes — "hears around corners"** | Key differentiator vs radar/camera |

### 4.3 Sensor Fusion Integration

| Fusion Partner | Role | Advantage |
|---------------|------|-----------|
| **Radar** | Long-range tracking, velocity measurement | Acoustic provides NLOS initial detection |
| **Camera (EO/IR)** | Visual identification, evidence capture | Acoustic provides bearing cue for slew-to-target |
| **LiDAR** | 3D mapping, precise range | Acoustic provides initial alert in cluttered environments |
| **RF scanner** | Drone communication interception | Acoustic detects fiber-optic/autonomous drones that RF cannot |

### 4.4 MEMS Microphone Technology (From Fraunhofer IDMT Microphone Arrays Page)

| Feature | MEMS (Digital) | Electret (Analog) |
|---------|---------------|-------------------|
| **Output** | Digital (direct to DSP) | Analog (requires ADC) |
| **Cost** | ~$1-2 each | ~$5-10 each |
| **Size** | <4mm package | ~6-10mm |
| **Power** | <1mW each | ~0.5-2mW each |
| **SNR** | >65 dB typical | >58 dB typical |
| **Consistency** | Factory-calibrated (matched) | Requires matching |
| **Complexity** | Lower (digital bus) | Higher (per-channel ADC) |
| **Fraunhofer preference** | **Recommended for arrays** | Legacy |

Fraunhofer IDMT explicitly notes that digital MEMS microphones can be connected **directly to signal processors**, reducing technical complexity. This aligns with their philosophy of minimizing hardware complexity and maximizing algorithmic performance.

---

## 5. RESEARCH PROJECTS (Publicly Funded)

### 5.1 AMBOS (BMBF)

| Item | Detail |
|------|--------|
| **Full name** | Not fully disclosed in English sources |
| **Funder** | BMBF (German Federal Ministry of Education and Research) |
| **Start** | 2016 |
| **Lead** | Fraunhofer FKIE (Institute for Communication, Information Processing and Ergonomics) |
| **Partners** | 12 organizations |
| **Fraunhofer IDMT role** | Acoustic detection algorithms and sensor development |
| **Focus** | Drone detection for security-critical areas |
| **Output** | Foundation algorithms for acoustic drone detection |

### 5.2 ALADDIN (H2020)

| Item | Detail |
|------|--------|
| **Full name** | Not fully disclosed in English sources |
| **Funder** | EU Horizon 2020 |
| **Lead** | CS Group (France) |
| **Partners** | 18 organizations from 9 European countries |
| **Fraunhofer IDMT role** | Acoustic detection algorithms |
| **Focus** | European-scale drone detection and countermeasures |
| **Scale** | Multi-national, multi-sensor approach |
| **Output** | Refined algorithms, international validation |

### 5.3 Adjacent Projects (Same Technology Base)

| Project | Domain | Relevance to C-UAS |
|---------|--------|-------------------|
| **"The Hearing Car"** | Autonomous vehicles | Acoustic environment sensing; MEMS array + ML on mobile platform |
| **HSN4Production** | Industrial monitoring | Acoustic anomaly detection; ML classification methods |
| **Connected Health** | Healthcare | Signal processing for noisy environments (hearing aids) |
| **Meadow Bird Detection** | Nature conservation | Acoustic species classification — directly analogous to drone type classification |

---

## 6. PERFORMANCE COMPARISON — Acoustic C-UAS Systems

| Feature | Fraunhofer IDMT | Squarehead G2+ | BeephoniX M2 | Dedrone DroneTracker |
|---------|----------------|----------------|-------------|---------------------|
| **Country** | Germany | Norway | Netherlands | Germany/USA |
| **Type** | **Research institute** | Product company | Startup | Product company |
| **Microphones** | Flexible (8+) | 128 MEMS | 151 MEMS | Unknown |
| **Detection range** | **50-200 m** | 300-1000 m | 200-900 m | ~500 m |
| **Direction accuracy** | Not specified | <10° | 1-2° | Unknown |
| **Coverage** | 360° | 105° (or 360°) | Hemispherical | Hemispherical |
| **Power** | Battery (low) | 24-48V, 20W | Battery/solar | ~15W |
| **MIL-STD** | No (research) | **810H** | TBD | Unknown |
| **IP rating** | No (prototype) | **IP65** | TBD | IP65 |
| **NLOS detection** | **Yes** | No | No | Partial |
| **Sensor wake-up** | **Yes** | No | No | No |
| **Camera** | No | Integrated | Optional | Integrated |
| **TRL** | 4-6 | **8-9** | 6-7 | 8-9 |
| **Price** | Contract R&D | $15K-50K est. | $5K-15K est. | $10K-30K est. |
| **Maturity** | **Research** | **Established** | **Early startup** | **Established** |

### Key Observations

**Fraunhofer IDMT advantages:**
1. **"Hears around corners"** — NLOS detection in urban/forested areas where radar/camera fail
2. **Sensor wake-up architecture** — Low-power acoustic acts as first-alert trigger for expensive sensors
3. **Algorithm-centric** — Technology can be embedded in any hardware platform
4. **Battery-operable** — Lowest power consumption of all reviewed systems
5. **Flexible microphone count** — Not locked to specific hardware configuration
6. **EU-funded research** — Publicly funded algorithms may be more accessible for licensing
7. **Broad acoustic expertise** — 8 research groups covering hearing, speech, audio, industrial monitoring
8. **Non-ITAR** — German/EU origin, no US export restrictions
9. **Extensible** — Same platform can detect vehicles, gunshots (announced)

**Fraunhofer IDMT limitations:**
1. **Shortest detection range (50-200m)** — 2-5x shorter than Squarehead and BeephoniX
2. **No MIL-STD certification** — Research prototype, not ruggedized product
3. **No fixed product form factor** — Must be productized by integrator/licensee
4. **No direction accuracy specification** — Key metric not published
5. **TRL 4-6** — Not field-proven at scale
6. **No volume manufacturing** — Research institute, not production facility
7. **Government funding dependency** — R&D timelines driven by grant cycles, not market demand
8. **1-second temporal resolution** — May be slower than real-time needs for fast FPV drones

---

## 7. CORE TECHNOLOGY DEEP DIVE

### 7.1 Acoustic Fingerprint Concept

The "acoustic fingerprint" is Fraunhofer IDMT's central metaphor and technical approach:

| Concept | Human Analogy | Drone Application |
|---------|--------------|-------------------|
| **Fingerprint** | Unique biometric identifier | Unique acoustic signature per drone model |
| **Database** | Fingerprint database (FBI/Interpol) | Drone acoustic signature library |
| **Matching** | Pattern comparison | ML feature matching |
| **Unknown prints** | "No match found" | Unknown drone detected (anomaly) |

Each drone type produces a characteristic acoustic profile based on:

| Sound Source | Acoustic Feature | Discriminating Power |
|-------------|-----------------|---------------------|
| **Rotor/propeller** | Blade pass frequency (BPF), harmonics | HIGH — unique per prop geometry |
| **Motor** | RPM, electromagnetic noise, commutation | MEDIUM — varies with model |
| **Frame vibration** | Resonant modes, structural harmonics | LOW — subtle, varies with payload |
| **Aerodynamic turbulence** | Broadband noise, vortex shedding | LOW — contributes to overall signature |

### 7.2 Signal Processing Chain (Estimated)

```
            FRAUNHOFER IDMT SIGNAL PROCESSING CHAIN
            ═══════════════════════════════════════

CAPTURE           ENHANCE              CLASSIFY            ACT
───────           ───────              ────────            ───
MEMS ──→ Multi-Channel ──→ Feature ──→ ML Model ──→ Alert
Array      Noise              Extraction   (CNN/RNN)     Generation
           Suppression        • Mel-spectrogram            │
           • Adaptive         • MFCCs                      ▼
             filtering        • BPF harmonics        ┌──────────┐
           • Spatial          • Temporal              │ OUTPUTS   │
             filtering          patterns              │ • Drone   │
           • Wind noise                               │   type    │
             cancellation                             │ • Bearing │
                                                      │ • Conf.   │
                    LOCALIZATION                       │ • Alert   │
                    ────────────                       └──────────┘
                    Beamforming                             │
                    + TDOA ──→ Direction ─────────────→     │
                    (azimuth,                              ▼
                     elevation)                      SENSOR WAKE-UP
                                                    → Activate radar
                                                    → Activate camera
                                                    → Activate LiDAR
```

### 7.3 ML Classification Approach

Based on Fraunhofer IDMT's published capabilities and the AMBOS/ALADDIN project scope:

| ML Component | Purpose | Fraunhofer Expertise |
|-------------|---------|---------------------|
| **Feature extraction** | Convert audio to ML-friendly representation | Mel-spectrograms, MFCCs (core HSA competency) |
| **Classification** | Drone vs. non-drone; drone type | CNN for spectral patterns (Acoustic Event Detection group) |
| **Temporal tracking** | Track across time windows | RNN/LSTM for trajectory patterns |
| **Noise robustness** | Operate in adverse conditions | Multi-channel noise suppression (Audio Signal Enhancement group) |
| **Anomaly detection** | Detect unknown drone types | Unsupervised/semi-supervised learning |
| **Edge inference** | Deploy on low-power hardware | Optimized models for embedded SoCs |

### 7.4 "Hearing Around Corners" — NLOS Detection

This is Fraunhofer IDMT's most distinctive capability claim:

```
SCENARIO: Urban C-UAS Detection

     Line-of-Sight Sensors (Radar, Camera, LiDAR):
     ┌─────────┐         BUILDING
     │  Radar  │────X────┌───────┐
     │  Camera │         │       │    ●  Drone
     │  LiDAR  │         │       │    (hidden behind
     └─────────┘         └───────┘     building)

     BLOCKED — Cannot detect drone behind building

     ─────────────────────────────────────────────

     Acoustic Sensor (Fraunhofer IDMT):
     ┌─────────┐         BUILDING
     │ Acoustic│←~~~~~←──┌───────┐
     │ Sensor  │  sound   │       │    ●  Drone
     │         │  diffracts│       │    (sound travels
     └─────────┘  around  └───────┘     around building)

     DETECTED — Sound diffracts around obstacles
```

Sound waves diffract around buildings, through forests, and over terrain features. This means acoustic sensors can detect drones in environments where radar, camera, and LiDAR have blind spots. Fraunhofer positions this as the primary value proposition for their acoustic technology.

### 7.5 Sensor Wake-Up Architecture

```
CONVENTIONAL APPROACH (All Sensors Always On):
┌──────────┐   ┌──────────┐   ┌──────────┐
│  Radar   │   │  Camera  │   │  LiDAR   │    Total: ~200-300W
│  (150W)  │   │  (50W)   │   │  (80W)   │    Always running
│  ON 24/7 │   │  ON 24/7 │   │  ON 24/7 │    High energy cost
└──────────┘   └──────────┘   └──────────┘

═══════════════════════════════════════════════════

FRAUNHOFER WAKE-UP APPROACH:
┌──────────┐                                       Total: ~5-10W
│ Acoustic │   STANDBY        STANDBY      STANDBY  (standby)
│  Sensor  │   ┌──────┐      ┌──────┐     ┌──────┐
│  (5-10W) │   │Radar │      │Camera│     │LiDAR │
│  ON 24/7 │   │(OFF) │      │(OFF) │     │(OFF) │
└──────────┘   └──────┘      └──────┘     └──────┘
     │              ↑              ↑            ↑
     │              │              │            │
     └──── DRONE DETECTED! ───────┤            │
           "Wake up!"  ───────────┤            │
                       ───────────┘            │
                       ────────────────────────┘
                                                Total: ~280-340W
                                                (only when threat detected)
```

This architecture:
1. **Reduces average power by 95%+** during quiet periods
2. **Extends battery life** for remote/off-grid deployments
3. **Reduces false alarm costs** on expensive sensors
4. **Provides true 24/7 coverage** with minimal energy budget

---

## 8. PATENTS & INTELLECTUAL PROPERTY

### 8.1 IP Assessment

| Type | Detail |
|------|--------|
| **Patent portfolio** | Not specifically identified for drone detection (Fraunhofer holds thousands of patents across 76 institutes) |
| **Likely IP** | Acoustic fingerprint matching algorithms, multi-channel noise suppression, sensor wake-up method |
| **Licensing model** | Fraunhofer is known for technology licensing (e.g., MP3, AAC, Fraunhofer FDK) |
| **Academic publications** | Extensive from AMBOS and ALADDIN projects (publicly accessible) |
| **Trade secrets** | ML model weights, training datasets, specific algorithm optimizations |

### 8.2 IP Landscape for VN-CUAS

| Technology | Status | Freedom to Operate |
|------------|--------|-------------------|
| Acoustic fingerprint concept (general) | Not patentable (general concept) | **FREE** |
| Specific ML models/weights | Trade secret (not accessible) | **FREE** — train own models |
| MEMS microphone arrays (general) | Public domain | **FREE** |
| Beamforming algorithms (general) | Public domain (decades old) | **FREE** |
| Multi-channel noise suppression (general) | Well-published in literature | **FREE** — implement from literature |
| Sensor wake-up concept | May be patented by Fraunhofer | **CHECK** — concept is obvious but implementation may be patented |
| Specific Fraunhofer implementations | Possibly patented | **DESIGN AROUND** — implement independently from published principles |

**Key insight:** Because Fraunhofer is a research institute with extensive publications, much of their fundamental approach is documented in academic papers. The specific optimizations and trained models are proprietary, but the underlying methods are accessible through published research.

---

## 9. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 9.1 Overall Function

```
┌──────────────────────────────────────────────────────────────────────┐
│               FRAUNHOFER IDMT ACOUSTIC DRONE DETECTION                │
│                                                                      │
│  INPUT:                            OUTPUT:                           │
│  • Sound waves (drone rotors,      • Drone detection alert           │
│    environmental noise)            • Drone type classification       │
│  • Power (battery/external)        • Direction (bearing)             │
│  • Configuration parameters        • Confidence score                │
│                                    • Wake-up trigger for other       │
│  FUNCTION:                           sensors                         │
│  "Passively detect, classify,      • Sensor data feed for fusion     │
│   and localize drones using                                          │
│   acoustic fingerprinting and                                        │
│   ML, even in NLOS conditions,                                       │
│   and trigger secondary sensors"                                     │
└──────────────────────────────────────────────────────────────────────┘
```

### 9.2 Sub-Function Structure

```
F0: Detect, Classify & Localize Drones (Passive, NLOS-Capable)
│
├── F1: SENSE - Multi-Channel Acoustic Capture
│   ├── F1.1: Receive sound waves at MEMS microphone array
│   ├── F1.2: Convert acoustic pressure to digital signal (per mic)
│   ├── F1.3: Synchronize multi-channel digital streams
│   └── F1.4: Continuous 360° monitoring for acoustic changes
│
├── F2: ENHANCE - Signal Conditioning
│   ├── F2.1: Multi-channel noise suppression
│   ├── F2.2: Wind noise cancellation
│   ├── F2.3: Adaptive filtering for environment-specific noise
│   ├── F2.4: Spatial filtering (beam-domain noise suppression)
│   └── F2.5: Signal-to-noise enhancement for weak drone signatures
│
├── F3: LOCALIZE - Direction Finding
│   ├── F3.1: Apply beamforming for direction of arrival
│   ├── F3.2: TDOA-based cross-channel triangulation
│   ├── F3.3: Determine azimuth (and elevation if array supports)
│   └── F3.4: Track bearing over time (motion estimation)
│
├── F4: CLASSIFY - ML Inference
│   ├── F4.1: Extract acoustic features (Mel-spectrograms, MFCCs)
│   ├── F4.2: Match against acoustic fingerprint database
│   ├── F4.3: Run ML classifier (drone type, confidence)
│   ├── F4.4: Detect unknown/novel drone types (anomaly detection)
│   └── F4.5: Suppress false positives (environmental events)
│
├── F5: ALERT - Threat Notification
│   ├── F5.1: Generate detection alert with classification
│   ├── F5.2: Provide bearing and confidence to fusion node
│   ├── F5.3: Update track data at 1-second intervals
│   └── F5.4: Interface with C2 system
│
├── F6: TRIGGER - Secondary Sensor Wake-Up
│   ├── F6.1: Evaluate detection confidence threshold
│   ├── F6.2: Send wake-up command to radar
│   ├── F6.3: Send slew-to-cue bearing to camera
│   ├── F6.4: Activate LiDAR scanning in detection direction
│   └── F6.5: Coordinate multi-sensor response
│
└── F7: POWER - Ultra-Low Energy Management
    ├── F7.1: Accept battery power (field/remote deployment)
    ├── F7.2: Accept external power (fixed installation)
    ├── F7.3: Ultra-low power operation (estimated 3-10W)
    └── F7.4: Standby power management for secondary sensors
```

---

## 10. BOM ESTIMATE (Vietnamese Production Context)

### 10.1 Fraunhofer-Class Acoustic Sensor — Estimated BOM

Since Fraunhofer IDMT provides algorithms rather than a fixed hardware product, this BOM estimates a Vietnamese-produced sensor using Fraunhofer-class technology:

| Subsystem | Components | Est. Cost (USD) | Local Content |
|-----------|-----------|-----------------|---------------|
| **MEMS microphones (32-64)** | Digital MEMS (e.g., ICS-43434) at ~$1-2 each | $32-128 | 0% (import all) |
| **Array PCB** | Multi-layer PCB, digital bus | $20-40 | 70% (PCB fab local) |
| **SoC/Processor** | Edge ML SoC (e.g., Cortex-A53/A72 + NPU, or NVIDIA Jetson Nano) | $40-100 | 10% (module import) |
| **Power management** | DC-DC, battery charger, solar MPPT | $10-20 | 50% (PCB local) |
| **Battery** | Li-ion cells, ~20-40Wh (10+ hours @ 5W) | $10-25 | 60% (cells import, pack local) |
| **Enclosure** | Weatherproof housing, IP65 | $15-30 | 85% (injection molding local) |
| **Connectors & cables** | Ethernet, power, antenna | $8-15 | 50% |
| **Software/firmware** | Detection algorithms + ML model | $0 (embedded) | 100% (domestic dev) |
| **Assembly & test** | Integration, calibration, QC | $10-20 | 90% (local labor) |
| **TOTAL per unit** | | **$145-378** | **~55-65%** |

### 10.2 Cost Comparison with Other Acoustic C-UAS Approaches

| Approach | Est. Sensor BOM | Detection Range | Maturity |
|----------|----------------|-----------------|----------|
| **Fraunhofer-class (32-64 MEMS)** | **$145-378** | 50-200 m | TRL 4-6 |
| BeephoniX-class (151 MEMS) | $325-680 | 200-900 m | TRL 6-7 |
| Squarehead-class (128 MEMS) | $385-800 | 300-1000 m | TRL 8-9 |
| Vietnamese CUAS target (128-256 MEMS) | $250-600 | 500-800 m (target) | TRL 1-2 |

### 10.3 Algorithm-First vs Hardware-First Trade-Off

Fraunhofer's approach suggests an important architectural decision for VN-CUAS:

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| **Algorithm-first** (Fraunhofer-style) | Invest in ML/DSP algorithms; keep hardware simple | Lower BOM; faster iteration; IP in software | Limited by physics (50-200m range); smaller array = less SNR |
| **Hardware-first** (Squarehead/BeephoniX-style) | Invest in large microphone array (128-256) | Higher SNR; longer range; better angular resolution | Higher BOM; more complex hardware; longer development |
| **Hybrid** (Recommended for VN-CUAS) | 128-256 MEMS array + strong algorithms | Best of both; competitive range AND smart classification | Highest development effort; needs both HW and SW teams |

---

## 11. DESIGN INSIGHTS FOR VN-CUAS

### 11.1 Key Lessons from Fraunhofer IDMT

1. **Algorithm sophistication compensates for hardware simplicity** — Fraunhofer achieves useful detection with as few as 8 microphones by relying on advanced ML and signal processing. Vietnamese development should invest heavily in algorithm quality, not just microphone quantity.

2. **"Acoustic fingerprint" database is a strategic asset** — The value is not just in the sensor but in the **database of drone signatures** used for classification. Vietnam should begin building a drone acoustic fingerprint database immediately, recording signatures of DJI Mavic, Phantom, FPV racing drones, military drones, and local Vietnamese commercial drones.

3. **Sensor wake-up architecture is brilliant for power-constrained deployments** — Using a low-power acoustic sensor to trigger expensive radar/camera/LiDAR saves 95%+ power during quiet periods. This is especially valuable for forward-deployed or border surveillance where power is limited. VN-CUAS should adopt this architecture.

4. **"Hears around corners" is the acoustic sensor's unique selling point** — No radar, camera, or LiDAR can detect a drone behind a building. Acoustic detection can. This should be a primary marketing message for Vietnamese C-UAS.

5. **Noise suppression is as important as detection** — Fraunhofer's Audio Signal Enhancement group (Rollwage) is the lead for drone detection — not the Acoustic Event Detection group. This means **cleaning the signal** (removing wind, traffic, birds) is the harder problem than classifying a clean drone sound. Vietnamese development should prioritize noise suppression algorithms.

6. **50-200m range is the honest floor for acoustic detection** — While Squarehead claims 300-1000m and BeephoniX claims 600-900m, Fraunhofer's research-grade assessment is more conservative: 50-200m depending on environment. Vietnamese product specifications should be realistic about acoustic range limitations.

7. **Research institute = accessible publications** — Unlike Squarehead and BeephoniX (commercial companies with trade secrets), Fraunhofer publishes extensively. AMBOS and ALADDIN project papers are likely publicly available and should be studied as primary references for Vietnamese algorithm development.

8. **Hearing technology → C-UAS is a proven technology transfer path** — Like BeephoniX (hearing aid → C-UAS), Fraunhofer IDMT's core competency is hearing/audio technology. Vietnamese hearing/audio researchers at universities (Hanoi University of Technology, HCMC University of Technology) may be valuable recruits for C-UAS development.

9. **Fraunhofer as potential technology partner** — Unlike product companies (Squarehead, BeephoniX), Fraunhofer's business model is technology licensing and contract R&D. A Vietnamese organization could potentially contract Fraunhofer for algorithm development, training data methodology, or system architecture consulting.

10. **1-second temporal resolution may be insufficient for fast FPV drones** — FPV racing drones travel at 100-160 km/h. At 1-second update rate, a drone moves 28-44 meters between updates. For effective tracking and effector cueing, Vietnamese system should target <0.5s temporal resolution.

### 11.2 Technology Adoption Matrix for VN-CUAS Design

| Feature | Adopt from Fraunhofer | Adopt from Squarehead | Adopt from BeephoniX | Own R&D |
|---------|----------------------|----------------------|---------------------|---------|
| **Detection principle** | Acoustic fingerprint + ML | — | — | Combine approaches |
| **Sensor wake-up** | **Yes — adopt this architecture** | — | — | Implement for VN C2 |
| **Noise suppression** | Study publications | — | — | Develop for VN environment |
| **Microphone count** | Study min. viable (8-32) | 128 reference | 151 reference | 128-256 target |
| **ML classification** | Feature extraction methods | Classification methods | Bio-inspired methods | Train on local data |
| **Localization** | Beamforming + TDOA | Beamforming | Doppler beamforming | Standard beamforming |
| **Environmental** | — | IP65, MIL-STD-810H | — | IP65+ from start |
| **Power** | Battery-operable (<10W) | 24-48V, 20W | Battery/solar (<15W) | Battery/solar (<10W) |
| **Form factor** | Flexible (algorithm-centric) | 8 kg pizza box | 950g disc | 1-2 kg target |
| **Integration** | Sensor fusion philosophy | TAK + SAPIENT | SAPIENT (planned) | SAPIENT + local C2 |

### 11.3 Updated VN-CUAS Product Concept (Cumulative from 3 RE Analyses)

```
VN-CUAS Product Architecture v3.0
(Incorporating Squarehead + BeephoniX + Fraunhofer IDMT insights)
│
├── SENSOR UNIT: Optimized Acoustic Array
│   • 128-256 MEMS digital microphones (ICS-43434 or similar)
│   • Target weight: 1-2 kg
│   • Target power: <10W (battery/solar capable)
│   • Circular array, ~35-40cm diameter
│   • IP65 minimum, MIL-STD-810H target
│   • On-edge processing (SoC with ML + DSP capability)
│   • ITAR-free components throughout
│
├── ALGORITHMS: Three-Layer Processing Stack
│   │
│   ├── Layer 1: Signal Enhancement (Fraunhofer-inspired)
│   │   • Multi-channel noise suppression (critical for VN tropical environment)
│   │   • Wind noise cancellation (monsoon conditions)
│   │   • Adaptive environmental noise filtering
│   │   • SNR enhancement for weak/distant drone signatures
│   │
│   ├── Layer 2: Beamforming + Localization (Squarehead/BeephoniX-inspired)
│   │   • Digital beamforming (phase delay, 128-256 channels)
│   │   • Azimuth + elevation determination
│   │   • Multi-sensor cross-bearing triangulation for 3D
│   │
│   └── Layer 3: ML Classification (All three references)
│       • Acoustic fingerprint database (build for Vietnamese drone landscape)
│       • CNN for drone type classification
│       • RNN for temporal tracking
│       • Anomaly detection for unknown drone types
│       • "Cocktail Party" noise suppression (BeephoniX heritage)
│
├── SENSOR FUSION: Wake-Up Architecture (Fraunhofer-inspired)
│   • Acoustic sensor as low-power first-alert layer
│   • Wake-up trigger for radar/camera/LiDAR
│   • Bearing cue for slew-to-target
│   • Dramatic power savings for remote deployments
│
├── NETWORKING: Mesh C2
│   • Multi-sensor cross-bearing triangulation for 3D position
│   • NATO SAPIENT protocol for allied interoperability
│   • Local C2 integration API
│   • Body-worn phone display for SOF
│
├── DETECTION TARGETS:
│   • FPV drones: 500-800m range
│   • Commercial drones (DJI class): 200-400m
│   • Large UAVs (Shahed class): 1+ km
│   • NLOS detection in urban/forested areas: 50-150m (Fraunhofer benchmark)
│   • Direction accuracy: <5°
│   • Update rate: <0.5 seconds (faster than Fraunhofer's 1s)
│
├── ACOUSTIC FINGERPRINT DATABASE (New — Fraunhofer-inspired):
│   • DJI Mavic series (all variants)
│   • DJI Phantom series
│   • FPV racing drones (5" props, various motors)
│   • Chinese commercial drones (FIMI, Autel)
│   • Military reconnaissance drones (known types)
│   • Shahed-class loitering munitions (if acoustic data available)
│   • Vietnamese environmental noise profiles
│
├── POWER: Tropical-Optimized
│   • Li-ion battery: 10+ hours runtime target @ <10W
│   • Solar charging: 50W panel for persistent deployment
│   • External 12-48 VDC for fixed installations
│   • Sensor wake-up: 95%+ power savings on secondary sensors
│
└── FUTURE EXTENSIONS:
    • Gunshot detection and localization (Fraunhofer announced)
    • Vehicle classification
    • C-RAM detection (muzzle blast from artillery/mortar)
    • Sniper detection
    • Cross-domain LOMAH scoring (subsonic projectile detection)
```

---

## 12. INTELLIGENCE GAPS

| Gap | Impact | Workaround |
|-----|--------|-----------|
| Specific microphone count in prototype | Low | Design-independent; algorithm works with variable count |
| Direction accuracy specification | High | Not published; assume >10° for small arrays |
| Detection range vs. microphone count trade-off | **Critical** | Must be determined through own testing |
| AMBOS/ALADDIN publication list | Medium | Search EU CORDIS database and academic databases |
| Specific ML model architecture | Medium | Implement standard audio ML (CNN on Mel-spectrograms) |
| Fraunhofer licensing terms/costs | Medium for partnership | Direct inquiry to Fraunhofer IDMT |
| Comparison at same microphone count (e.g., 128 mics) | High | Fraunhofer's 50-200m with few mics vs Squarehead's 300-1000m with 128 mics |
| Sensor wake-up protocol/interface | Medium | Design own; concept is straightforward |
| Environmental performance data | Medium | Research prototype; no field qualification data |
| Training dataset composition | High for ML accuracy | Build own dataset from scratch |
| 1-second update rate — hardware or algorithm limited? | Medium | Likely algorithm-limited; faster hardware could reduce |

---

## 13. REFERENCES

### Public Sources Used

| # | Source | Type | Key Data |
|---|--------|------|----------|
| 1 | idmt.fraunhofer.de/en/Press_and_Media/press_releases/2025/acoustic-drone-detection.html | Press release | System overview, 50-200m range, 360° coverage, 1-sec updates |
| 2 | idmt.fraunhofer.de/en/institute/projects-products/drone-detection.html | Product page | AMBOS project reference, detection + localization, ML methods |
| 3 | idmt.fraunhofer.de/en/institute/projects-products/microphonearrays.html | Technology page | MEMS vs electret, beamforming, digital arrays |
| 4 | idmt.fraunhofer.de/en/hsa.html | Branch overview | HSA structure, 8 research groups, management, founded 2008 |
| 5 | aerospace-and-defence.com | Industry article | Full technical overview; AMBOS/ALADDIN details; Christian Rollwage quote |
| 6 | electronicspecifier.com | Industry article | Target customers; Rollwage quote; sensor fusion description |
| 7 | stratpost.com | Defense news | System summary; "hears around corners" capability |
| 8 | securityworldmarket.com | Security news | AMBOS (12 partners, FKIE lead); ALADDIN (18 partners, 9 countries, CS Group lead) |
| 9 | airportsinternational.com | Aviation news | Airport security application; 8-mic mobile sensor |
| 10 | eenewseurope.com | Electronics news | Integrated acoustic sensor solution announcement |

### Cross-References (VN-CUAS-001 Project)

| RE Analysis | Key Comparison Point |
|-------------|---------------------|
| [[RE_squarehead_discovair_g2plus]] | Established competitor: 128 mics, 8 kg, 300-1000m, IP65, MIL-STD-810H |
| [[RE_beephonix_m2]] | Ultra-light competitor: 151 mics, 950g, 200-900m, bio-inspired |
| (Future) Additional C-UAS systems | DroneShield DroneSentry, Dedrone DroneTracker, RADA MHR, Robin Radar Elvira |

---

## 14. COMPARATIVE SUMMARY: THREE ACOUSTIC C-UAS APPROACHES

| Dimension | Squarehead G2+ | BeephoniX M2 | Fraunhofer IDMT | VN-CUAS Target |
|-----------|----------------|-------------|----------------|----------------|
| **Type** | **Product** | **Product** | **Research/license** | Product |
| **Country** | Norway | Netherlands | Germany | Vietnam |
| **Microphones** | 128 | **151** | Flexible (8+) | 128-256 |
| **Weight** | 8 kg | **950 g** | N/A (prototype) | 1-2 kg |
| **Detection range** | **300-1000 m** | 200-900 m | 50-200 m | 500-800 m |
| **Direction accuracy** | <10° | **1-2°** | Not specified | <5° |
| **Coverage** | 105° (360° horiz.) | Hemispherical | **360°** | 360° |
| **NLOS detection** | No | No | **Yes** | Yes (acoustic) |
| **Sensor wake-up** | No | No | **Yes** | Yes |
| **Power** | 24-48V, 20W | Battery/solar | **Battery (lowest)** | Battery/solar, <10W |
| **MIL-STD** | **810H** | TBD | No | 810H |
| **IP rating** | **IP65** | TBD | No | IP65 |
| **Camera** | **Integrated** | Optional | No | Optional |
| **SAPIENT** | **Supported** | Planned | No | Required |
| **ML/AI** | Yes | Yes | **Yes (core strength)** | Yes |
| **C-RAM** | **Yes** | No | No | Future |
| **TRL** | **8-9** | 6-7 | 4-6 | Target 8-9 |
| **Price (est.)** | $15K-50K | $5K-15K | Contract R&D | **$2K-5K** |
| **Key strength** | Established, certified | Ultra-light, accurate | **Algorithms, NLOS, wake-up** | Cost-effective |

---

*Analysis compiled from publicly available sources only. No classified, ITAR-controlled, or proprietary information included. All specifications are estimates based on published data, press releases, news articles, and industry comparisons.*

*Created: 2026-02-11 | Project: VN-CUAS-001 | Phase: 0 (Reverse Engineering)*
