---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: BeephoniX M2 (Netherlands)
version: 1.0
created: 2026-02-11
status: complete
---

# RE: BeephoniX M2 - Netherlands
## Reverse Engineering Analysis from Public Sources

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | BeephoniX B.V. |
| **HQ** | Utrecht, Netherlands (originally Nijmegen) |
| **Phone** | +31 (0)6 5189 6954 |
| **Email** | hello@beephonix.com |
| **Founded** | 2022 |
| **Origin** | Spin-off from Radboud University Department of Biophysics |
| **Employees** | ~9 (as of late 2025) |
| **Revenue** | €1.2-1.5M projected (2025, from 10-15 projects) |
| **Status** | Private, early-stage startup |
| **Funding** | NWO Take-off 2 loan €250K + €190K additional; seeking €5M Series A |
| **Key products** | M1 (Dynamic Microphone — hearing aid), **M2 (C-UAS acoustic sensor)** |
| **ITAR status** | Non-ITAR (Dutch/EU) |
| **Core IP** | Patented biomimetic dynamic microphone inspired by bee antenna mechanics |

### Key Personnel

| Name | Role | Background |
|------|------|------------|
| **Klaas-Jan Kakebeeke** | CEO | Radboud University; NWO Venture Challenge 2nd place |
| **Martijn Agterberg** | CSO (Chief Science Officer) | Associate Professor, Radboud University Dept. of Biophysics; audiologist; 20+ years hearing research |
| **Patrick Wijnings** | CTO | Technical engineer, Radboud University; developed the dynamic microphone prototype |
| **Marc van Dorth** | Founding team | Early team member |

### Historical Lineage

| Year | Event |
|------|-------|
| ~2000s | Radboud University Dept. of Biophysics becomes leading lab in directional hearing research |
| ~2020 | Martijn Agterberg attends beekeeper lecture; conceives biomimetic microphone based on bee antenna mechanics |
| 2022 | BeephoniX B.V. founded as Radboud University spin-off; NWO Venture Challenge 2nd place |
| 2022-2023 | NWO Take-off 2 loan (€250K) + additional €190K funding |
| 2023 | "Beepod" prototype demonstrated; Dutch Ministry of Defence expresses interest |
| 2023-2024 | Pivot to dual-use: hearing aids + defense C-UAS; M1 (hearing) and M2 (defense) product lines |
| 2024 | BeephoniX M2 development commissioned by Dutch Ministry of Defence |
| 2025 (Jun) | M2 demonstrated to Dutch military; FPV drones detected at 600-900m |
| 2025 (Sep) | Public reveal of M2 at Blue Magic Netherlands event, Eindhoven |
| 2025 (Nov) | BeephoniX presents at Blue Magic Netherlands defense event |
| 2025 | Port of Amsterdam pilot announced (radar + camera + acoustic integration) |
| 2025 | 10-15 projects in pipeline; €1.2-1.5M early revenue |
| 2026 | Plans to double headcount (~18 staff); seeking €5M investment |

### Founding Story

The core technology originated when Prof. Martijn Agterberg (Radboud University audiologist and biophysicist) attended a beekeeper's lecture and learned that **bees use their antennae as moveable ears** to trace sound sources. This bio-inspired insight led to the development of a **dynamic (physically rotating) microphone** that exploits the **Doppler effect** for sound source localization — a fundamentally different approach from conventional static beamforming arrays.

The original mission was solving the **"Cocktail Party Problem"** for hearing-impaired people: distinguishing a single voice from background noise. When the Dutch Ministry of Defence recognized the technology's potential for passive drone detection, BeephoniX created the M2 defense product line alongside the M1 hearing aid microphone.

### Partnerships & Collaborations

| Partner | Type | Detail |
|---------|------|--------|
| **Radboud University** | Academic origin | Dept. of Biophysics, hearing science research |
| **Dutch Ministry of Defence** | Customer/sponsor | Commissioned M2 development; field demonstrations |
| **NWO (Netherlands Organisation for Scientific Research)** | Funder | Take-off 2 loan, Venture Challenge |
| **Radboudumc** | Clinical partner | Hearing implant user experience research |
| **Absolute Audio Labs** (Hilversum) | Technology partner | DSP software for hearing system (EU grant) |
| **Port of Amsterdam** | Pilot customer | Drone detection over water/industrial sites |
| **Briskr** | Startup accelerator | Business angel introductions, workshops |
| **Mercator Launch** | Incubator | Early-stage support |

---

## 2. PRODUCT FAMILY OVERVIEW

```
BeephoniX Product Portfolio
│
├── M1 — Dynamic Microphone (Hearing)
│   ├── Target: Hearing aids, cochlear implants, bone-conduction implants
│   ├── Technology: Biomimetic rotating microphone (Doppler-based localization)
│   ├── Purpose: Solve "Cocktail Party Problem" for hearing-impaired
│   └── Status: Prototype ("Beepod"), pre-clinical
│
├── M2 — Counter-UAS Acoustic Sensor (Defense)
│   ├── 151 MEMS microphones per unit
│   ├── AI/ML classification of drone types
│   ├── Passive, fully solid-state (no emissions)
│   ├── Bio-inspired beamforming algorithms
│   └── Status: Field-demonstrated, early production
│
└── Future Products (Announced)
    ├── Compact M2 variant (~20 cm) for Special Forces
    ├── Vehicle-mounted detection (with engine noise filtering)
    └── Artillery/gunshot detection (low-frequency extension)
```

### Key Innovation: Biomimetic Dynamic Microphone

BeephoniX's **core differentiator** is a fundamentally different sensing approach:

| Approach | How It Works | Used By |
|----------|-------------|---------|
| **Static TDOA** | Fixed microphones measure time difference of arrival | LOMAH systems (Saab, Polytronic, InVeris) |
| **Static beamforming** | Fixed array with digital phase steering | Squarehead Discovair G2+ |
| **Dynamic biomimetic** | Physically moving/rotating microphone creates Doppler effect | **BeephoniX (unique)** |

The Doppler-based approach:
1. A microphone element **physically oscillates or rotates**
2. Sound arriving from the direction of movement experiences a **Doppler shift**
3. Sound from other directions shows **no Doppler shift**
4. By measuring Doppler strength across rotation, the system **localizes the sound source**
5. This mimics how **bee antennae vibrate** to determine sound direction

This is analogous to how a rotating radar antenna creates directional sensitivity, but applied to passive acoustic sensing.

---

## 3. BEEPHONIX M2 SYSTEM ARCHITECTURE

### 3.1 System Topology

```
┌────────────────────────────────────────────────────────────────────┐
│                    BEEPHONIX M2 SYSTEM                              │
│                                                                    │
│  SENSOR UNIT (Ultra-Lightweight)                                   │
│  ┌───────────────────────────┐                                     │
│  │  151 MEMS Microphones     │         COMMAND & CONTROL           │
│  │  (circular array, ~35cm)  │         ┌──────────────────┐        │
│  │                           │  API    │  C2 System       │        │
│  │  On-Edge AI Processor     │────────→│  • SAPIENT (NATO)│        │
│  │  (ML classification)      │         │  • Custom BMS    │        │
│  │                           │         │  • Phone display │        │
│  │  Power: Battery/Solar/Ext │         │    (body-worn)   │        │
│  │  Weight: 950 g            │         └──────────────────┘        │
│  └───────────────────────────┘                                     │
│       │                                                            │
│  NETWORKED MODE                                                    │
│  ┌──────┐    ┌──────┐    ┌──────┐                                  │
│  │ M2-A │    │ M2-B │    │ M2-C │    → Triangulated 3D position    │
│  │(az/el)│   │(az/el)│   │(az/el)│   → "Acoustic dome" coverage    │
│  └──────┘    └──────┘    └──────┘                                  │
│     ↓            ↓            ↓                                    │
│  ┌─────────────────────────────────────┐                           │
│  │  Server / Fusion Node               │                           │
│  │  • Cross-bearing triangulation      │                           │
│  │  • 3D target position calculation   │                           │
│  │  • Track management                 │                           │
│  │  • Alert generation                 │                           │
│  └─────────────────────────────────────┘                           │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Detection Principle: Bio-Inspired Beamforming + ML

**Stage 1: Acoustic Capture**
151 MEMS microphones arranged in a circular array capture omnidirectional sound. The array geometry (35-40 cm diameter) determines spatial resolution.

**Stage 2: Beamforming**
Bio-inspired beamforming algorithms (derived from bee antenna mechanics and Doppler-based directional sensing) process the 151-channel audio to create directional acoustic beams. This provides azimuth and elevation to sound sources.

**Stage 3: AI Classification**
Machine learning algorithms (likely CNN/RNN-based) analyze the beamformed signal to:
- Distinguish drone sounds from environmental noise
- Classify drone type (FPV, multirotor, fixed-wing)
- Track targets over time
- Suppress false positives ("close to zero" false alarm rate claimed)

**Stage 4: Networked Triangulation (Multi-Sensor)**
When multiple M2 units are deployed, cross-bearing intersections calculate 3D target positions. The 1-2° direction accuracy per sensor becomes precise 3D localization in a mesh network.

```
Bio-Inspired Detection Principle:

   BEE ANTENNA (Natural)              BEEPHONIX M2 (Engineered)
   ┌─────────────────────┐            ┌─────────────────────────┐
   │  Antenna vibrates    │            │  151 MEMS mics in       │
   │  in sound field      │            │  circular array          │
   │       ↓              │            │       ↓                  │
   │  Doppler shift =     │            │  Beamforming =           │
   │  direction cue       │            │  directional sensitivity │
   │       ↓              │            │       ↓                  │
   │  Neural processing   │            │  ML classification       │
   │  → "food source      │            │  → "drone at bearing     │
   │     is THAT way"     │            │     045°, elevation 15°" │
   └─────────────────────┘            └─────────────────────────┘
```

### 3.3 Beamforming Comparison: BeephoniX vs Squarehead vs LOMAH

| Parameter | BeephoniX M2 | Squarehead G2+ | Traditional LOMAH |
|-----------|-------------|----------------|-------------------|
| **Microphones** | 151 MEMS | 128 MEMS | 4-8 pressure transducers |
| **Array diameter** | ~35-40 cm | ~30-40 cm | ~1-3 m (bar/frame) |
| **Weight** | **950 g** | 8 kg | 10-15 kg |
| **Algorithm** | Bio-inspired beamforming + Doppler | Digital beamforming | TDOA triangulation |
| **Direction accuracy** | **1-2°** | <10° | N/A (gives X,Y mm) |
| **Positional accuracy** | Via mesh triangulation | Via mesh triangulation | ±5-10 mm direct |
| **Detection range** | 200-900 m | 300-1000 m | 3×2.5 m zone |
| **Power** | Battery/solar (~W) | 24-48V, 20W | 12V battery |
| **IP rating** | TBD (field-capable) | IP65 | IP65-67 |
| **MIL-STD** | TBD (not yet certified) | MIL-STD-810H | Varies |
| **ML/AI** | Yes | Yes | No |
| **Unique feature** | **Ultra-light, bio-inspired** | Established, certified | Proven mm-accuracy |

---

## 4. DETAILED COMPONENT SPECIFICATIONS

### 4.1 Sensor Unit (BeephoniX M2)

| Parameter | Specification | Source |
|-----------|--------------|--------|
| **Microphone count** | 151 digital MEMS per unit | Official |
| **Microphone type** | MEMS (Micro-Electro-Mechanical Systems) | Official |
| **Array geometry** | Circular, ~35-40 cm diameter | Pravda: "35 cm diameter"; Brainport: "40 cm" |
| **Weight** | **950 grams** | Pravda |
| **Processing** | On-edge AI (embedded ML inference) | Official |
| **Camera** | Optional integrated optical module | Official |
| **Power** | Battery, solar, or external source | Pravda |
| **Power draw** | Not disclosed (estimated 5-15W based on MEMS + SoC) | Estimated |
| **IP rating** | Not disclosed (field-demonstrated) | TBD |
| **MIL-STD** | Not yet certified | TBD |
| **Operating temperature** | Not disclosed | TBD |
| **ITAR** | Non-ITAR (Dutch/EU origin) | Implied |

### 4.2 Detection Performance

| Parameter | Value | Notes |
|-----------|-------|-------|
| **FPV drone detection** | **600-900 m** | Dutch military demo (single sensor, no LOS) |
| **Commercial drone (DJI Mavic 4)** | **200-300 m** | Single sensor |
| **Shahed-type (large UAV)** | **~1.5 km** (modelled) | Early modelling, not field-verified |
| **General detection range** | Up to 200 m (conservative) | Pravda report |
| **Direction accuracy** | **1-2°** (azimuth/elevation) | Brainport article |
| **Drone classes** | Class I (<25 kg), Class II (25-150 kg) | Official |
| **Coverage per sensor** | Hemispherical (implied by flat-mount) | Estimated |
| **False positive rate** | Near-zero (ML suppression claimed) | Brainport article |
| **3D localization** | Yes, via multi-sensor mesh network | Official |

### 4.3 Networked Configuration

| Mode | Detail |
|------|--------|
| **Single sensor** | Bearing + elevation only; 2D direction |
| **Multi-sensor mesh** | Cross-bearing triangulation → 3D position |
| **"Acoustic dome"** | Multiple M2 units create coverage dome over area |
| **SOF deployment** | Body-worn phone display; multiple units for hemispheric coverage |
| **Perimeter** | Linear array along border/fence |

### 4.4 Integration

| Interface | Protocol/Standard |
|-----------|-------------------|
| **NATO SAPIENT** | Planned (announced by CEO) |
| **Custom APIs** | Additional APIs for C2 integration |
| **Display** | Phone/tablet (body-worn capable) |
| **Multi-sensor** | Network-linked mesh |
| **Sensor fusion** | Complement to radar, RF, EO/IR systems |

---

## 5. PERFORMANCE COMPARISON — Acoustic C-UAS Sensors

| Feature | BeephoniX M2 | Squarehead G2+ | Dedrone DroneTracker | Fraunhofer IDMT |
|---------|-------------|----------------|---------------------|-----------------|
| **Country** | Netherlands | Norway | Germany/USA | Germany |
| **Microphones** | **151 MEMS** | 128 MEMS | Unknown | Array |
| **Weight** | **950 g** | 8 kg | ~5 kg | Unknown |
| **Direction accuracy** | **1-2°** | <10° | Unknown | Unknown |
| **FPV range** | **600-900 m** | Not specified | Not specified | 50-200 m |
| **Commercial drone** | 200-300 m | 300-500 m | 500 m | 50-200 m |
| **Large UAV** | ~1.5 km (modelled) | Up to 1 km | Unknown | Unknown |
| **MIL-STD** | TBD | **810H** | Unknown | Unknown |
| **IP rating** | TBD | **IP65** | IP65 | Unknown |
| **Camera** | Optional | Integrated | Integrated | No |
| **SAPIENT** | Planned | Supported | Unknown | Unknown |
| **Maturity** | **Early-stage startup** | **Established product** | **Established** | **Research** |
| **Price (est.)** | $5K-15K (est.) | $15K-50K (est.) | $10K-30K (est.) | N/A |

### Key Competitive Position

**BeephoniX M2 advantages:**
1. **Ultra-lightweight (950g)** — 8.4× lighter than Squarehead G2+ (8 kg); ideal for SOF/dismounted
2. **Superior direction accuracy (1-2°)** — 5-10× better than Squarehead (<10°)
3. **151 vs 128 microphones** — marginal array advantage
4. **FPV detection at 600-900m** — first published field result for acoustic FPV detection at this range
5. **Bio-inspired algorithms** — novel Doppler-based approach from 20+ years of hearing research
6. **Low power** — battery/solar capable for forward deployment
7. **Non-ITAR** — Dutch/EU origin, no US export restrictions
8. **Lower cost potential** — startup pricing vs. established defense contractor margins

**BeephoniX M2 limitations:**
1. **No MIL-STD certification yet** — not ruggedized/qualified
2. **No confirmed IP rating** — field-capable but not IP65/67 rated
3. **Early-stage company (9 people)** — production scale risk
4. **No C-RAM capability demonstrated** — only drone detection shown
5. **Limited installed base** — no combat-proven deployments
6. **No DroneShield-type integration** — early API stage
7. **Detection range variance** — 200m (conservative) to 900m (demo) is wide spread

---

## 6. CORE TECHNOLOGY DEEP DIVE

### 6.1 Biomimetic Microphone Technology (Patented)

The foundational technology comes from studying how **insects (specifically bees) use mechanically vibrating antennae** to determine sound direction:

| Biological Model | Engineering Translation |
|-----------------|----------------------|
| Bee antenna vibrates in sound field | MEMS microphone element oscillates |
| Vibration creates frequency shift (Doppler) | Physical motion modulates incoming signal |
| Neural processing extracts direction | DSP algorithm measures Doppler strength vs direction |
| Bee navigates toward food source | System outputs bearing to sound source |

**Key paper:** Agterberg et al. (Radboud University) — 20+ years of research in directional hearing, hearing implants, and biophysics of auditory localization.

### 6.2 Dynamic vs Static Microphone Arrays

| Feature | Dynamic (BeephoniX) | Static (Squarehead, conventional) |
|---------|--------------------|---------------------------------|
| **Sensing element** | Physically moving microphone | Fixed microphone array |
| **Directional mechanism** | Doppler effect from motion | Phase delay between elements |
| **Minimum array size** | Potentially single element | Multiple elements required |
| **Frequency response** | Enhanced by motion (Doppler amplification) | Limited by element spacing (spatial aliasing) |
| **Novelty** | **Unique, patented** | Well-established (decades old) |
| **Risk** | Higher (new technology, less proven) | Lower (proven in many applications) |

### 6.3 Signal Processing Chain (Estimated)

```
                BEEPHONIX M2 SIGNAL PROCESSING CHAIN
                ═════════════════════════════════════

PHYSICAL            TRANSDUCTION         DIGITAL               INTELLIGENCE
────────            ────────────         ───────               ────────────
Sound wave ──→ 151 MEMS ──→ Digital ──→ Bio-Inspired ──→ ML Classifier
 (drone rotor,   Microphones   Streams    Beamforming      (CNN/RNN/LSTM)
  wind, etc.)    (digital      (151 ch    (Doppler-           │
                  MEMS)         parallel)  enhanced)           ▼
                                              │          Classification
                                              │          (drone type,
                                              │           class I/II,
                                              │           FPV/multirotor)
                                              ▼                │
                                         Bearing +             ▼
                                         Elevation        Alert + Track
                                         (1-2° acc.)          │
                                              │               ▼
                                              │        ┌────────────┐
                                              └───────→│ API Output │
                                                       │ • Bearing  │
                                                       │ • Elevation│
                                                       │ • Class    │
                                                       │ • Conf.    │
                                                       │ • Track ID │
                                                       └────────────┘
                                                            │
                                                  ┌─────────┴──────────┐
                                                  ▼                    ▼
                                             Phone/Tablet         C2 System
                                             (body-worn)      (SAPIENT/BMS)
```

### 6.4 ML Classification Approach

Based on DSIAC primer and industry practices, BeephoniX likely uses:

| ML Component | Purpose | Detail |
|-------------|---------|--------|
| **Feature extraction** | Convert audio to ML-friendly format | Mel-spectrograms, MFCCs from beamformed signal |
| **CNN** | Drone signature recognition | Trained on rotor/motor acoustic patterns |
| **RNN/LSTM** | Temporal tracking | Predict trajectory from past acoustic patterns |
| **Training data** | Model accuracy | Field recordings of FPV, DJI, military drones + noise |
| **Inference** | Edge deployment | On-sensor ML (embedded SoC) |

---

## 7. PATENTS & INTELLECTUAL PROPERTY

### 7.1 Known IP

| Type | Detail |
|------|--------|
| **Patent** | "Patented dynamic microphone technology" (stated on website) |
| **Patent scope** | Biomimetic microphone based on insect antenna mechanics |
| **Specific patent number** | Not publicly disclosed in sources found |
| **Academic basis** | 20+ years of Radboud University biophysics/hearing research |
| **Trade secrets** | ML models, training datasets, beamforming algorithms |

### 7.2 IP Landscape Assessment for VN-CUAS

| Technology | Status | Freedom to Operate |
|------------|--------|-------------------|
| Biomimetic dynamic microphone | **Patented by BeephoniX** | **BLOCKED** — must license or design around |
| Static beamforming (general) | Public domain | **FREE** |
| MEMS microphone arrays (general) | Not patented by BeephoniX | **FREE** |
| ML drone classification | Trade secret (model weights) | **FREE** — train own model |
| Doppler-based localization (general concept) | Broad concept not patentable | **FREE** (specific implementation may be patented) |
| Circular array geometry | Patented by Squarehead (US 11,832,051) | **DESIGN AROUND** Squarehead's claims |

**Key insight:** BeephoniX's patent covers the *specific* dynamic/rotating microphone mechanism. The broader concept of using MEMS arrays with beamforming for drone detection is **not blocked** — Vietnamese development can use standard static beamforming with a custom array geometry.

---

## 8. KNOWN CONTRACTS & DEPLOYMENTS

### 8.1 Confirmed

| Customer/Event | Detail | Date |
|---------------|--------|------|
| **Dutch Ministry of Defence** | Commissioned M2 development; field demonstrations with military | 2024-2025 |
| **Dutch military demo** | FPV drones detected at 600-900m; DJI Mavic 4 at 200-300m | Jun 2025 |
| **Blue Magic Netherlands** | Presented to State Secretary for Defence Gijs Tuinman | Nov 2025 |
| **Port of Amsterdam** | Pilot: drone detection over water/industrial sites (complement radar/camera) | 2025 (planned) |
| **Land Air Defense Command Vredepeel** | Lt. Col. Arjen Nijkamp — "virtually undetectable to enemy" endorsement | 2025 |
| **Special Forces interest** | Request for 20-cm compact version | 2025 |

### 8.2 Pipeline

| Item | Detail |
|------|--------|
| **10-15 projects** | €1.2-1.5M early revenue for 2025 |
| **Vehicle-mounted** | Requires engine noise training data |
| **Artillery/gunshot detection** | Low-frequency extension (future) |

### 8.3 Market Status

BeephoniX is an **early-stage startup** (founded 2022, ~9 employees, pre-Series A). Compare to Squarehead (founded 2004, ~50 employees, established Norwegian military contracts). BeephoniX has **higher technology risk but potentially disruptive innovation** in the ultra-lightweight passive acoustic C-UAS segment.

---

## 9. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 9.1 Overall Function

```
┌──────────────────────────────────────────────────────────────────────┐
│                      BEEPHONIX M2                                     │
│                                                                      │
│  INPUT:                             OUTPUT:                          │
│  • Sound waves (drone rotors,       • Drone bearing (1-2° accuracy)  │
│    environmental noise)             • Drone elevation                │
│  • Power (battery/solar/external)   • Drone classification (type)    │
│  • Network connection               • Confidence score               │
│                                     • Track data (time series)       │
│  FUNCTION:                          • API data stream                │
│  "Passively detect, localize,                                        │
│   track, and classify drones                                         │
│   using bio-inspired acoustic                                        │
│   beamforming and ML"                                                │
└──────────────────────────────────────────────────────────────────────┘
```

### 9.2 Sub-Function Structure

```
F0: Detect, Localize, Track & Classify Drones (Passive, Bio-Inspired)
│
├── F1: SENSE - 151-Channel Acoustic Capture
│   ├── F1.1: Receive sound waves at 151 MEMS microphones
│   ├── F1.2: Convert acoustic pressure to digital signal (per mic)
│   ├── F1.3: Synchronize 151 digital streams
│   └── F1.4: Continuous sector monitoring for acoustic changes
│
├── F2: PROCESS - Bio-Inspired Beamforming
│   ├── F2.1: Apply Doppler-enhanced beamforming algorithm
│   ├── F2.2: Form directional beams across coverage area
│   ├── F2.3: Determine azimuth and elevation to sound source
│   ├── F2.4: Achieve 1-2° angular resolution
│   └── F2.5: Generate acoustic spatial map
│
├── F3: CLASSIFY - AI/ML Inference
│   ├── F3.1: Extract acoustic features (spectrograms, MFCCs)
│   ├── F3.2: Run ML classifier (FPV/multirotor/fixed-wing/non-drone)
│   ├── F3.3: Compute classification confidence score
│   ├── F3.4: Suppress false positives (near-zero false alarm)
│   └── F3.5: Distinguish enemy drone from friendly/civilian
│
├── F4: TRACK - Target Management
│   ├── F4.1: Assign track ID to new detections
│   ├── F4.2: Update bearing/elevation over time
│   ├── F4.3: Estimate speed and direction of travel
│   └── F4.4: Alert on new/lost tracks
│
├── F5: NETWORK - Multi-Sensor Fusion
│   ├── F5.1: Share bearing/elevation data with other M2 units
│   ├── F5.2: Cross-bearing triangulation → 3D position
│   ├── F5.3: Create "acoustic dome" coverage map
│   └── F5.4: Feed data to C2/BMS via SAPIENT/API
│
├── F6: DISPLAY - Operator Interface
│   ├── F6.1: Show drone bearing/class on phone/tablet
│   ├── F6.2: Body-worn display for SOF operators
│   └── F6.3: Generate alerts for new threats
│
└── F7: POWER - Energy Management
    ├── F7.1: Accept battery power (field deployment)
    ├── F7.2: Accept solar power (persistent surveillance)
    ├── F7.3: Accept external power (fixed installation)
    └── F7.4: Low-power operation (~5-15W estimated)
```

---

## 10. BOM ESTIMATE (Vietnamese Production Context)

### 10.1 BeephoniX M2 Equivalent — Estimated BOM

| Subsystem | Components | Est. Cost (USD) | Local Content |
|-----------|-----------|-----------------|---------------|
| **151 MEMS microphones** | Digital MEMS (e.g., ICS-43434) at ~$1-2 each | $150-300 | 0% (import all) |
| **Array PCB** | Multi-layer circular PCB, digital bus | $30-60 | 70% (PCB fab local) |
| **SoC/Processor** | Embedded ML-capable SoC (e.g., NVIDIA Jetson Nano, Xilinx Zynq) | $60-150 | 10% (module import) |
| **Camera module** (optional) | CMOS camera + lens | $10-25 | 20% (import) |
| **Power management** | Battery charger, DC-DC, solar MPPT | $15-30 | 50% (PCB local) |
| **Battery** | Li-ion cells, ~20-50Wh | $15-30 | 60% (cells import, pack local) |
| **Enclosure** | Weatherproof housing, ~35cm circular, <1 kg | $20-40 | 85% (plastic injection local) |
| **Connectors & cables** | Ethernet, power, antenna | $10-20 | 50% |
| **Firmware/software** | Beamforming + ML algorithms | $0 (embedded) | 100% (domestic dev) |
| **Assembly & test** | Integration, calibration, QC | $15-25 | 90% (local labor) |
| **TOTAL per unit** | | **$325-680** | **~50-60%** |

### 10.2 Ultra-Light Form Factor Advantage

At 950g and ~$500 estimated BOM, the M2-class sensor is **the most portable and affordable** acoustic C-UAS concept in the market. A Vietnamese production could target:

| Configuration | Units | Est. Unit Cost | Total |
|--------------|-------|---------------|-------|
| **Single sensor** | 1 | $500-1,000 | $500-1,000 |
| **SOF kit (4 sensors + hub)** | 4+1 | $400/sensor + $300 hub | $1,900-2,500 |
| **Perimeter (12 sensors + server)** | 12+1 | $350/sensor + $2,000 server | $6,200-8,000 |
| **Base protection (24 sensors + C2)** | 24+1 | $300/sensor + $5,000 C2 | $12,200-15,000 |

---

## 11. DESIGN INSIGHTS FOR VN-CUAS

### 11.1 Key Lessons from BeephoniX

1. **Ultra-lightweight is achievable** — 951g for 151 MEMS mics proves that acoustic C-UAS does not need to be heavy. MEMS digital microphones at $1-2 each and lightweight plastic enclosures enable sub-1kg sensors.

2. **151 MEMS is better than 128** — More microphones = better spatial resolution and SNR. Vietnamese design should target 128-256 MEMS elements for optimal cost/performance.

3. **1-2° accuracy from a single sensor** — This is a breakthrough claim. If validated, it means far fewer sensors needed for 3D coverage. Vietnamese R&D should verify this with a prototype.

4. **FPV drone detection at 600-900m is the benchmark** — This is the most operationally relevant metric for current warfare (Ukraine/drone warfare context). Vietnamese product must match or exceed this.

5. **Bio-inspired algorithms are a real differentiator** — The Doppler-enhanced beamforming from hearing research gives BeephoniX a signal processing advantage. Vietnamese team should study Radboud University published research for algorithm inspiration.

6. **Hearing aid → C-UAS pivot is valid** — The "Cocktail Party Problem" (isolating one voice from noise) is exactly analogous to "isolate one drone from environmental clutter." Vietnamese hearing/audio researchers may be valuable for C-UAS development.

7. **SOF use case drives form factor** — Special forces want sub-1kg, body-worn, phone-display, no emissions. This is a premium market segment.

8. **Multi-sensor mesh is essential for 3D** — A single acoustic sensor gives direction only. Multiple sensors + triangulation give position. Vietnamese system architecture must be mesh-native.

9. **Battery/solar power enables forward deployment** — Unlike Squarehead (20W, 24-48V), BeephoniX targets battery operation. Vietnamese tropical conditions favor solar-augmented battery power.

10. **MIL-STD and IP certification is still needed** — BeephoniX's main weakness is lack of environmental qualification. Vietnamese product should pursue MIL-STD-810H from the start.

### 11.2 Technology Comparison Matrix for VN-CUAS Design

| Feature | Adopt from BeephoniX | Adopt from Squarehead | Own R&D |
|---------|---------------------|----------------------|---------|
| **Form factor** | Ultra-light (<1 kg) | — | Target 1-2 kg |
| **Microphones** | 151 MEMS (or more) | — | 128-256 MEMS |
| **Beamforming** | Study Doppler approach | Digital beamforming | Hybrid approach |
| **ML/AI** | CNN/RNN classification | ML classification | Train on local drone data |
| **Environmental** | — | IP65, MIL-STD-810H | IP65+ from start |
| **Integration** | SAPIENT (NATO) | TAK + SAPIENT | SAPIENT + local C2 |
| **Power** | Battery/solar (<15W) | 24-48V, 20W | Battery/solar (<10W target) |
| **Camera** | Optional | Integrated | Optional (EO/IR future) |
| **Display** | Phone (body-worn) | Browser | Phone + browser |

### 11.3 Updated VN-CUAS Product Concept

```
VN-CUAS Product Architecture (Cumulative from Squarehead + BeephoniX RE)
│
├── SENSOR UNIT: Ultra-Light Acoustic Array
│   • 128-256 MEMS digital microphones (ICS-43434 or similar)
│   • Target weight: 1-2 kg (between BeephoniX 950g and Squarehead 8 kg)
│   • Target power: <15W (battery/solar capable)
│   • Circular array, ~35-40cm diameter
│   • IP65 minimum, MIL-STD-810H target
│   • On-edge processing (SoC with ML capability)
│   • ITAR-free components throughout
│
├── ALGORITHMS: Hybrid Beamforming + ML
│   • Digital beamforming (phase delay, established technique)
│   • Study Doppler-enhanced approach (BeephoniX-inspired, if non-infringing)
│   • ML classification: CNN for drone detection, RNN for tracking
│   • Train on Vietnamese acoustic environment + known drone signatures
│   • "Cocktail Party" noise suppression algorithms
│
├── NETWORKING: Mesh C2
│   • Multi-sensor cross-bearing triangulation for 3D position
│   • NATO SAPIENT protocol for allied interoperability
│   • Local C2 integration API
│   • Body-worn phone display for SOF
│
├── DETECTION TARGETS:
│   • FPV drones: 500-800m range (match BeephoniX benchmark)
│   • Commercial drones (DJI class): 200-400m
│   • Large UAVs (Shahed class): 1+ km
│   • Direction accuracy: <5° (between BeephoniX 1-2° and Squarehead <10°)
│
├── POWER: Tropical-Optimized
│   • Li-ion battery: 10+ hours runtime target
│   • Solar charging: 50W panel for persistent deployment
│   • External 12-48 VDC for fixed installations
│
└── FUTURE EXTENSIONS:
    • C-RAM detection (artillery/mortar muzzle blast localization)
    • Sniper detection
    • Gunshot localization
    • Subsonic projectile LOMAH scoring (cross-domain application)
```

---

## 12. INTELLIGENCE GAPS

| Gap | Impact | Workaround |
|-----|--------|-----------|
| Specific patent claims (not disclosed) | Critical for FTO analysis | File patent search in Netherlands/EPO; assume Doppler mechanism patented |
| Exact MEMS microphone model used | Low | Use comparable digital MEMS |
| Internal SoC/processor selection | Medium | Select based on ML requirements and VN supply chain |
| Beamforming algorithm details | High for performance matching | Published Radboud University papers may provide foundation |
| IP rating and environmental performance | Medium | Design to IP65/MIL-STD-810H regardless |
| Actual false positive rate in field conditions | Medium | Own testing required |
| Production cost at scale | Medium for business case | Estimate from BOM analysis |
| Power consumption detail | Low | Design for <15W budget |
| Long-term reliability data | High | New product, no field data yet |
| Accuracy validation (1-2° claim) | **Critical** | Must be independently verified |

---

## 13. REFERENCES

### Public Sources Used

| # | Source | Type | Key Data |
|---|--------|------|----------|
| 1 | beephonix.com/defense-security | Product page | M2 specs, strategic advantages |
| 2 | beephonix.com | Corporate | Founding team, M1/M2 products, history |
| 3 | brainporteindhoven.com | In-depth article | 151 mics, 40cm, 600-900m FPV, 1-2° accuracy, €5M raise, 9 staff |
| 4 | news-pravda.com | News | 35cm diameter, 950g weight, battery/solar, 200m range |
| 5 | briskr.nl | Startup profile | Founding story, Doppler mechanism, NWO funding, "Beepod" prototype |
| 6 | nwo.nl/en/projects/20547 | Grant project | Biomimetic microphone, hearing implant origin, NWO Take-off 2 |
| 7 | ru.nl (Radboud University) | Academic | Bee antenna inspiration, NWO grant, beekeeper lecture origin |
| 8 | radboudumc.nl | Medical | EU grant for hearing system with Absolute Audio Labs |
| 9 | lifesciencesatwork.nl | Startup directory | Biomimetic microphone development |
| 10 | tracxn.com | Corporate data | Founders, company profile |
| 11 | dsiac.dtic.mil | Technical primer | Acoustic drone detection: CNNs, RNNs, LSTMs, signal processing |
| 12 | raillynews.com | News (Turkish) | Dutch military endorsement, Lt. Col. Nijkamp quote |

### Cross-References (VN-CUAS-001 Project)

| RE Analysis | Key Comparison Point |
|-------------|---------------------|
| [[RE_squarehead_discovair_g2plus]] | Established competitor: 128 mics, 8 kg, IP65, MIL-STD-810H, $15K-50K |
| (Future) Additional C-UAS competitors | DroneShield, Dedrone, RADA, Robin Radar, Fraunhofer IDMT |

---

## 14. COMPARATIVE SUMMARY: BEEPHONIX vs SQUAREHEAD

| Dimension | BeephoniX M2 | Squarehead G2+ | VN-CUAS Target |
|-----------|-------------|----------------|----------------|
| **Weight** | **950 g** | 8 kg | 1-2 kg |
| **Microphones** | **151** | 128 | 128-256 |
| **Direction accuracy** | **1-2°** | <10° | <5° |
| **FPV range** | **600-900 m** | Not specified | 500-800 m |
| **MIL-STD** | TBD | **810H** | 810H |
| **IP rating** | TBD | **IP65** | IP65 |
| **Power** | **Battery/solar** | 24-48V, 20W | Battery/solar, <15W |
| **C-RAM** | No | **Yes** | Future |
| **Camera** | Optional | **Integrated** | Optional |
| **SAPIENT** | Planned | **Supported** | Required |
| **Maturity** | Early startup | **Established** | New development |
| **Price (est.)** | **$5K-15K** | $15K-50K | **$2K-5K** |

---

*Analysis compiled from publicly available sources only. No classified, ITAR-controlled, or proprietary information included. All specifications are estimates based on published data, news articles, corporate websites, and industry comparisons.*

*Created: 2026-02-11 | Project: VN-CUAS-001 | Phase: 0 (Reverse Engineering)*
