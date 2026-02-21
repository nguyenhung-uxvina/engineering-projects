---
project: VN-CUAS-001
phase: 0
type: reverse-engineering
subject: Mind Foundry SENTRY (United Kingdom)
version: 1.0
created: 2026-02-08
status: complete
---

# RE: Mind Foundry SENTRY - United Kingdom
## Reverse Engineering Analysis from Public Sources

> **KEY DISTINCTION:** Mind Foundry is an **AI/ML-first company**, NOT a sensor manufacturer — fundamentally different from all other systems analysed in this project. Spun out of the University of Oxford's Machine Learning Research Group (2016) by two world-leading professors of machine learning, Mind Foundry applies **Bayesian inference, advanced signal processing, and computer vision** to acoustic data to create what it calls **"acoustic intelligence"** — transforming raw sound into actionable threat information. SENTRY C-UAS is an "acoustic tripwire" that detects, tracks, and classifies drones (including fibre-optic and autonomous types invisible to RF) using their acoustic signatures. The system integrates seamlessly with **ATAK** on chest-mounted devices, creating a mobile detection network in **<30 seconds**. Mind Foundry's approach is **software-defined and hardware-agnostic** — it makes existing microphones and sensor infrastructure smarter through AI, rather than selling proprietary sensor hardware. This represents the **algorithm-centric C-UAS architecture** and validates the role of **UK Sovereign AI** in acoustic intelligence.

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Mind Foundry Ltd |
| **HQ** | Oxford, Oxfordshire, United Kingdom |
| **Founded** | 2016 |
| **Origin** | Spin-out from University of Oxford, Machine Learning Research Group, Dept. of Engineering Science |
| **Founders** | Prof Stephen Roberts, Prof Michael Osborne |
| **CEO (2019-2025)** | Brian Mullins (former DAQRI founder, 100+ US patents) |
| **Chairman & Interim CEO (Jun 2025+)** | Jiro Okochi (founder of Reval, 35 yrs tech/banking) |
| **Employees** | 75-100 (2023) |
| **Total Funding** | ~$44M across seed + Series A + Series B |
| **Valuation** | ~£103M (Nov 2022, Tracxn) |
| **Sectors** | Insurance, Infrastructure, Defence & National Security |
| **Key Products** | SENTRY C-UAS, SENTRY Sensor Fusion, NIGHTINGALE (ASW) |
| **ITAR Status** | Non-ITAR (UK sovereign AI company) |
| **Core IP** | Bayesian inference, signal processing, acoustic ML classification |
| **Positioning** | "AI for high-stakes applications" |

### 1.1 Founders — Academic Heritage

| Name | Role | Background |
|------|------|------------|
| **Prof Stephen Roberts** | Co-Founder, Chief Scientific Advisor | Royal Academy of Engineering / Man Group Professor of Machine Learning, University of Oxford. Pioneer in signal processing, Bayesian inference, sensor networks. Research spans astronomy, biology, healthcare, finance, engineering, and control systems. |
| **Prof Michael Osborne** | Co-Founder, Chief Scientific Advisor | Professor of Machine Learning, Official Fellow of Exeter College, Oxford. Co-Director of Oxford Martin AI Governance Initiative. Pioneer in Bayesian optimisation, probabilistic numerics. Co-author of influential 2013 study on automation of jobs. |

> **Academic DNA insight:** Mind Foundry's technical approach is rooted in Oxford's Machine Learning Research Group — one of the world's top ML laboratories. Roberts and Osborne are not just academics; they are **field-defining researchers** whose contributions to Bayesian inference and signal processing ARE the theoretical foundation of modern acoustic intelligence. This academic pedigree gives Mind Foundry access to Oxford's PhD pipeline, IP, and research partnerships — a competitive moat that cannot be replicated by pure commercial startups.

### 1.2 Key Leadership

| Name | Role | Background |
|------|------|------------|
| **Brian Mullins** | CEO (2019-~2025) | Founded DAQRI (enterprise AR company). Awarded 100+ US patents. Testified before US Senate on AR. CNBC Disruptor 50, Goldman Sachs "100 Most Intriguing Entrepreneurs". Edison Award for Industrial Design. US Merchant Marine Academy BSc Engineering. Former DOT and SPAWAR (Space and Naval Warfare Systems Command). |
| **Jiro Okochi** | Chairman & Interim CEO (Jun 2025+) | Founded Reval (treasury & risk management, 650+ corporate/bank clients in 20 countries), sold to ION Group (2016). UC Berkeley BSc Genetics. 35 years tech & banking leadership (WestLB, Deutsche Bank, BofA, Kidder Peabody). |
| **Lindsay Chadwick** | Leadership team | Current senior leadership |
| **Al Bowman** | Leadership team | Current senior leadership; author on AI at the Edge for defence |
| **Syreeta Cummings** | Product Manager, Defence & Security | Key spokesperson for SENTRY C-UAS; authored techUK article on acoustic intelligence |

### 1.3 Funding & Investment History

| Year | Event | Amount | Investors |
|------|-------|--------|-----------|
| 2016 | **Seed Round** | Undisclosed | Oxford Science Enterprises (formerly OSI), Parkwalk Advisors |
| 2019 | **CEO appointment** | — | Brian Mullins joins as CEO |
| 2020 | **Series A** | $13.6M | **Aioi Nissay Dowa Insurance (ANDI)** (lead), Parkwalk Advisors, Oxford Sciences Innovation, University of Oxford, Oxford Technology & Innovations EIS Fund |
| 2023 Feb | **Aioi R&D Lab Oxford** | — | Joint R&D laboratory with ANDI in Oxford |
| 2023 Oct | **Series B** | $22M | University of Oxford, Aioi Nissay Dowa, Parkwalk Advisors |
| **Total** | | **~$44M** | 7+ investors across multiple rounds |

> **Strategic investor insight:** Aioi Nissay Dowa Insurance (part of MS&AD Insurance Group, Japan's largest insurance holding) is the anchor strategic investor — leading the Series A and participating in Series B. This reflects Mind Foundry's dual-use business model: insurance AI provides steady revenue while defence AI provides high-growth potential. The Aioi R&D Lab in Oxford (launched Feb 2023) is a joint commercial research facility. The University of Oxford itself is an investor — unusual and reflects the strength of the academic spin-out relationship.

### 1.4 Historical Timeline

| Year | Event |
|------|-------|
| 2016 | Mind Foundry founded as University of Oxford spin-out by Profs Roberts and Osborne |
| 2016 | Seed funding from Oxford Science Enterprises and Parkwalk Advisors |
| 2019 | Brian Mullins (DAQRI founder) appointed CEO |
| 2020 | Series A ($13.6M) led by Aioi Nissay Dowa Insurance |
| 2023 Feb | Aioi R&D Lab Oxford launched (joint insurance AI research) |
| 2023 Oct | Series B ($22M); total funding reaches ~$44M |
| 2023 Nov | British Business Awards — UK-Japan Partnership (with Aioi) |
| 2024 | SENTRY C-UAS product developed and positioned for defence market |
| 2024 | Saab UK awarded LookOut Phase 3 contract in collaboration with Mind Foundry (DASA-funded) |
| 2025 Jan | The Times Tech 100 — ranked #11 (UK fastest-growing private tech) |
| 2025 Jun | Jiro Okochi becomes Chairman & Interim CEO |
| 2025 Jul | Syreeta Cummings publishes techUK article on acoustic intelligence for C-UAS |
| 2025 | SENTRY C-UAS, SENTRY Sensor Fusion, and NIGHTINGALE products actively marketed |

### 1.5 Partnerships & Collaborations

| Partner | Type | Detail |
|---------|------|--------|
| **University of Oxford** | Academic origin & investor | Machine Learning Research Group; PhD pipeline; IP licensing |
| **Saab UK** | Defence partner | LookOut Phase 3 — Royal Navy maritime early warning (DASA/DSTL funded) |
| **Aioi Nissay Dowa Insurance** | Strategic investor & customer | Lead Series A investor; joint Aioi R&D Lab Oxford; insurance AI applications |
| **SEA (Systems Engineering & Assessment)** | Hardware partner | KraitSense hardware integration for NIGHTINGALE ASW product |
| **DASA (Defence & Security Accelerator)** | UK MOD innovation funder | LookOut Phase 3 programme funding |
| **DSTL (Defence Science & Technology Laboratory)** | UK MOD research | Collaboration through Saab UK LookOut programme |
| **Royal Navy** | End customer | LookOut maritime early warning requirement owner |
| **Parkwalk Advisors** | Investor | Oxford-focused deep-tech venture capital |
| **Oxford Science Enterprises** | Investor | University of Oxford technology transfer fund |

---

## 2. PRODUCT FAMILY

### 2.1 Product Overview

| Product | Type | Function | Key Feature |
|---------|------|----------|-------------|
| **SENTRY C-UAS** | AI software (acoustic) | Drone detection, tracking, classification | Acoustic tripwire; ATAK integration; <30s mobile network |
| **SENTRY Sensor Fusion** | AI software (multi-sensor) | Multi-sensor data fusion | Fuses acoustic, radar, EO/IR, RF into single picture |
| **NIGHTINGALE** | AI software (sonar/acoustic) | Anti-submarine warfare tonal analysis | Automated tonal analysis; SEA KraitSense integration |
| **Mind Foundry Core** | AI/ML platform | General-purpose AI deployment | Responsible AI tooling for high-stakes applications |

### 2.2 SENTRY C-UAS — Core Product

**The AI is the product.** Unlike Squarehead (hardware-centric acoustic sensor) or Dedrone (software-centric RF platform), Mind Foundry's primary value is **ML algorithms that transform acoustic data into intelligence**. SENTRY does not include proprietary microphone hardware — it makes existing microphones and infrastructure smarter.

#### Concept: "Acoustic Tripwire"
SENTRY creates an invisible acoustic perimeter around protected areas. When a drone enters the acoustic detection zone, SENTRY:
1. **Detects** the acoustic signature (motor hum, propeller buzz)
2. **Filters** environmental noise using advanced signal processing
3. **Classifies** the threat by comparing against known acoustic signatures
4. **Tracks** position and movement using acoustic triangulation
5. **Alerts** operators through ATAK integration on existing devices

#### Deployment Modes

| Mode | Description | Setup Time |
|------|-------------|------------|
| **Mobile** | ATAK on chest-mounted end-user devices; every soldier becomes a sensor | **<30 seconds** |
| **Static** | Leverages existing sensor networks; fixed microphone installations | Minutes-hours |
| **Layered** | Combination of mobile and static sensors feeding unified picture | Varies |

#### Key Capabilities
- Real-time acoustic detection, tracking, and classification
- **Fibre-optic drone detection** — critical capability that RF sensors cannot provide
- **Autonomous drone detection** — drones without RF links still produce sound
- Multi-drone simultaneous tracking in unpredictable environments
- Environmental noise filtering and isolation of drone-specific sounds
- Acoustic signature converted to spectrograms for computer vision analysis
- Continuous ML model improvement — new drone types fed back into system
- Seamless ATAK integration — no additional hardware for mobile deployment
- Reduces operator cognitive load through AI-processed intelligence
- Edge-deployable AI inference

#### Three Core Challenges Addressed (per techUK article)

| Challenge | Description | SENTRY AI Solution |
|-----------|-------------|--------------------|
| **Environmental Complexity** | Sounds vary in intensity, propagate non-linearly, affected by weather, temperature, terrain. Signals are combinations of many sources. | Advanced signal processing + AI algorithms filter environmental noise, isolate drone-specific sounds from multiple drones simultaneously |
| **Cognitive Load** | High-stress environments require rapid decisions. Massive data volumes with varying relevance can overload operators. | AI reduces raw data to actionable intelligence; spectrograms enable visual pattern recognition; operator focuses on decisions, not data |
| **Evolving Threats** | ~100+ drone types in Ukraine alone. Increasingly sophisticated, varied, and numerous. Airspace more congested and unpredictable. | Continuous ML learning — new drone encounters fed back to improve detection. System adapts as threats evolve. |

### 2.3 SENTRY Sensor Fusion

SENTRY Sensor Fusion extends beyond acoustic-only detection to fuse data from multiple sensor types:

| Capability | Detail |
|------------|--------|
| **Data Sources** | Acoustic, radar, EO/IR, RF, and other sensor types |
| **Output** | Single evolving operational picture |
| **Deployment** | Static (existing sensors) and mobile (end-user devices) |
| **Function** | Clarity, continuity, and actionable insights for faster decisions |
| **Integration** | Makes existing hardware and C2 software smarter |
| **Signal Types** | Sonar, radar, cyber, acoustic — complex signal processing engine |

> **Key insight:** SENTRY Sensor Fusion is not a competing product to SENTRY C-UAS — it's an **extension**. It takes the acoustic intelligence from SENTRY C-UAS and fuses it with radar, camera, and RF data from other sensors (e.g., from DroneShield, Dedrone, or military radar) to create a unified threat picture. This positions Mind Foundry as a **fusion layer** on top of existing C-UAS infrastructure.

### 2.4 NIGHTINGALE — Anti-Submarine Warfare (ASW)

| Specification | Detail |
|---------------|--------|
| **Domain** | Anti-submarine warfare acoustic intelligence |
| **Function** | Automated full tonal analysis of sonar data |
| **Core Capability** | Accelerates tonal analysis and prioritisation of threat signatures |
| **Hardware Partner** | SEA's KraitSense hardware (autonomous detection + classification) |
| **Operator Impact** | Expert sonar operators typically require 14 years of training. NIGHTINGALE accelerates both novice and expert performance. |
| **Integration** | Machine-speed decision support into existing ASW systems |
| **Cognitive Load** | Reduces cognitive burden; enhances decision speed and trust in outputs |

> **Cross-domain insight:** NIGHTINGALE proves that Mind Foundry's acoustic intelligence engine is **domain-agnostic** — the same core ML algorithms that detect drones in air also detect submarines in water. The underlying signal processing (spectrograms → pattern recognition → classification) is fundamentally the same. This cross-domain capability is a significant competitive advantage and validates the generality of their technology stack.

---

## 3. SYSTEM ARCHITECTURE

### 3.1 Algorithm-Centric Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                 MIND FOUNDRY AI ENGINE                        │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│  │  Signal       │  │  ML/AI       │  │  Sensor Fusion  │   │
│  │  Processing   │  │  Classification│  │  Engine         │   │
│  │  (Bayesian)   │  │  (Spectrogram │  │  (Multi-modal)  │   │
│  │              │  │   → CV)       │  │                 │   │
│  └──────┬───────┘  └──────┬───────┘  └────────┬────────┘   │
│         └─────────────────┼───────────────────┘             │
│                           │                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │            Integration Layer                            │ │
│  │  ATAK Plugin │ REST API │ C2 Interface │ Edge Runtime  │ │
│  └────────────────────────────────────────────────────────┘ │
└───────────┬────────────────┬────────────────┬───────────────┘
            │                │                │
  ┌─────────┴─────┐  ┌──────┴──────┐  ┌──────┴──────┐
  │ ACOUSTIC      │  │ 3RD PARTY   │  │ OPERATOR    │
  │ SENSORS       │  │ SENSORS     │  │ DEVICES     │
  │               │  │             │  │             │
  │ Microphones   │  │ Radar       │  │ ATAK on     │
  │ (any type)    │  │ Camera      │  │ chest-mount │
  │ Sonar arrays  │  │ RF sensors  │  │ Tablets     │
  │ (KraitSense)  │  │ EO/IR       │  │ C2 screens  │
  └───────────────┘  └─────────────┘  └─────────────┘
```

### 3.2 AI/ML Pipeline — Acoustic Intelligence

Mind Foundry's core technical approach transforms raw acoustic data into intelligence through a multi-stage ML pipeline:

```
RAW AUDIO → SIGNAL PROCESSING → SPECTROGRAM → COMPUTER VISION → CLASSIFICATION → INTELLIGENCE
     │              │                │                │                │              │
     │         Bayesian        Time-frequency    CNN/pattern      Acoustic DB    Threat alert
     │         filtering       representation   recognition      matching       via ATAK
     │         Noise removal                    Feature           Confidence
     │         Source                            extraction        scoring
     │         separation
     │
  Microphone
  input (any)
```

**Stage 1: Signal Acquisition**
- Hardware-agnostic — accepts input from any microphone or microphone array
- Mobile: uses smartphone/device microphones (ATAK on chest-mount)
- Static: uses installed microphone arrays or existing infrastructure

**Stage 2: Signal Processing (Bayesian)**
- Advanced Bayesian signal processing (Roberts/Osborne core expertise)
- Environmental noise filtering — weather, wind, terrain effects modelled
- Source separation — isolates individual drone signatures from multi-source acoustic environment
- Non-linear sound propagation modelling (sound affected by temperature gradients, terrain, obstacles)

**Stage 3: Spectrogram Generation**
- Time-frequency representation of acoustic signals
- Converts 1D audio waveform into 2D visual representation
- Preserves temporal and frequency information for pattern recognition

**Stage 4: Computer Vision Classification**
- Spectrograms treated as images → computer vision ML models identify patterns
- Compares against database of known drone acoustic signatures
- Identifies drone type, size, and motor characteristics
- Confidence scoring on classification output

**Stage 5: Tracking & Localisation**
- Multi-sensor acoustic triangulation for position estimation
- Track correlation across multiple microphone sources
- Movement prediction and trajectory estimation

**Stage 6: Intelligence Output**
- Actionable threat information delivered to ATAK interface
- Drone type, location, heading, confidence level
- Alert generation with priority ranking
- Reduced cognitive load — operator sees intelligence, not raw data

### 3.3 Detection Method — Acoustic Intelligence vs RF Detection

| Aspect | Mind Foundry SENTRY (Acoustic AI) | Dedrone/DroneShield (RF) |
|--------|-----------------------------------|--------------------------|
| **Core Technology** | ML on acoustic signatures | RF protocol pattern matching |
| **Sensing** | Sound waves via microphones | Radio frequency via SDR |
| **Range** | ~200m-1km (acoustic physics limited) | 1.6-8 km |
| **Fibre-optic Drones** | **YES — detects** (motors still produce sound) | **NO — cannot detect** (no RF) |
| **Autonomous Drones** | **YES — detects** (motors still produce sound) | **NO — cannot detect** (no RF) |
| **Pilot Location** | No | Yes (RF triangulation) |
| **Weather Impact** | Moderate (wind, rain degrade) | Minimal |
| **NLOS Detection** | Yes (sound diffracts) | Yes (RF penetrates) |
| **Hardware Required** | Any microphone (even smartphone) | Specialised SDR/antenna |
| **Mobile Deployment** | <30 seconds (ATAK on phone) | Minutes-hours (sensor setup) |
| **Cost** | Software license (HW-agnostic) | $10K-50K per sensor + software |
| **Continuous Learning** | Yes — new drones fed back to ML model | Yes — cloud-updated DB |

### 3.4 ATAK Integration — "Every Soldier a Sensor"

Mind Foundry's ATAK (Android Tactical Assault Kit) integration is a key differentiator:

| Feature | Detail |
|---------|--------|
| **Device** | Standard chest-mounted ATAK end-user device |
| **Additional Hardware** | None required — uses device microphone |
| **Setup Time** | <30 seconds to create mobile network |
| **Network** | Mesh of ATAK devices creates distributed acoustic sensor array |
| **Coverage** | Scales with number of personnel — each soldier extends detection area |
| **Weight Penalty** | Zero additional weight to individual soldier |
| **Interface** | Threat overlaid on ATAK tactical map |
| **Edge Processing** | ML inference runs on edge device |

> **Tactical significance:** This is the most **rapidly deployable** acoustic C-UAS system identified in any RE analysis. No other system achieves <30 second deployment. By making every soldier a sensor with zero additional weight, Mind Foundry creates a distributed acoustic mesh that scales linearly with unit size. A platoon of 30 soldiers = 30 acoustic nodes = wide-area coverage.

---

## 4. TECHNOLOGY DEEP DIVE

### 4.1 Academic Foundations

Mind Foundry's technology is built on decades of academic research from Oxford's Machine Learning Research Group. Key theoretical foundations:

| Domain | Description | Application in SENTRY |
|--------|-------------|-----------------------|
| **Bayesian Inference** | Probabilistic reasoning under uncertainty; updating beliefs with new evidence | Acoustic classification with confidence scoring; handling noisy/uncertain data |
| **Bayesian Optimisation** | Efficient optimisation of expensive-to-evaluate functions | Hyperparameter tuning; sensor placement optimisation |
| **Probabilistic Numerics** | Treating numerical computation as inference | Robust computation on edge devices with limited precision |
| **Signal Processing** | Time-frequency analysis, source separation, filtering | Acoustic noise filtering, drone signature extraction |
| **Computer Vision** | Pattern recognition in visual representations | Spectrogram analysis for drone classification |
| **Gaussian Processes** | Non-parametric Bayesian models for regression/classification | Acoustic propagation modelling; environmental adaptation |

### 4.2 Key Academic Papers (Founders)

The founders' academic publications form the theoretical backbone:

- **Roberts:** Machine learning theory for large-scale real-world problems with noise and uncertainty. Applications across astronomy, biology, healthcare, finance, engineering, control, and sensor networks.
- **Osborne:** Co-author of the influential 2013 study "The Future of Employment: How Susceptible Are Jobs to Computerisation?" (>20,000 citations). Pioneer in Bayesian optimisation and probabilistic numerics.
- **Combined:** The Roberts-Osborne research programme at Oxford has produced fundamental advances in probabilistic ML that directly apply to acoustic signal processing in noisy environments — exactly the core challenge of drone acoustic detection.

### 4.3 AI at the Edge

Mind Foundry emphasises edge-deployable AI — critical for defence applications:

| Aspect | Detail |
|--------|--------|
| **Edge Inference** | ML models run on local devices (ATAK devices, embedded systems) |
| **Connectivity** | Can operate disconnected from cloud |
| **Latency** | Real-time processing required for threat detection |
| **Model Updates** | New acoustic signatures can be pushed to edge devices |
| **Compute Constraints** | Models optimised for mobile device processors |
| **AI in the Loop** | Human operator makes final decision; AI provides intelligence |

### 4.4 Continuous Learning Architecture

A critical design principle — the system improves over time:

1. **Encounter new drone type** → acoustic signature captured
2. **Signature analysed** → ML model identifies new patterns
3. **Model updated** → new drone type added to classification database
4. **Update deployed** → pushed to edge devices across fleet
5. **System improves** → detection accuracy increases with each new encounter

This mirrors Dedrone's DroneDNA quarterly cloud updates but applies to acoustic rather than RF signatures.

---

## 5. NIGHTINGALE — CROSS-DOMAIN VALIDATION

### 5.1 Anti-Submarine Warfare Application

NIGHTINGALE applies the same acoustic intelligence engine to underwater sonar data:

| Aspect | SENTRY (Air) | NIGHTINGALE (Underwater) |
|--------|-------------|--------------------------|
| **Medium** | Air (sound waves) | Water (sonar signals) |
| **Targets** | Drones, aircraft | Submarines, underwater vehicles |
| **Sensors** | Microphones (any) | Sonar arrays (SEA KraitSense) |
| **Core ML** | Same engine — spectrogram → CV → classification | Same engine — tonal analysis → CV → classification |
| **Operator** | Frontline soldier via ATAK | Warfare specialist at sonar console |
| **Training Gap** | Hours (ATAK deployment) | 14 years to become expert sonar operator |

### 5.2 SEA KraitSense Partnership

| Item | Detail |
|------|--------|
| **Partner** | SEA (Systems Engineering & Assessment Ltd) |
| **Product** | KraitSense — autonomous underwater acoustic sensor |
| **Integration** | Mind Foundry AI + SEA hardware = autonomous detection + classification |
| **Significance** | Validates Mind Foundry's hardware-agnostic model — partners for hardware, provides AI |

### 5.3 Cross-Domain Significance for VN-CUAS

NIGHTINGALE proves that Mind Foundry's acoustic ML engine is **generalizable**:
- Same signal processing pipeline (spectrogram → pattern recognition)
- Same Bayesian inference approach
- Same continuous learning architecture
- Different physical medium (air vs water) and targets (drones vs submarines)

This validates that a well-designed acoustic ML engine can be adapted across domains — a principle VN-CUAS should embrace.

---

## 6. KEY DEPLOYMENTS & CUSTOMERS

### 6.1 Known Deployments

| Customer / Programme | Application | Status |
|---------------------|-------------|--------|
| **UK Royal Navy (via Saab UK LookOut Phase 3)** | Maritime early warning — potential Crowsnest successor | DASA-funded contract awarded |
| **UK MOD (via DASA/DSTL)** | Defence innovation programme | Active collaboration |
| **Aioi Nissay Dowa Insurance** | Insurance AI (telematics, claims, underwriting) | Commercial deployment |
| **Infrastructure operators** | Asset monitoring, predictive maintenance | Commercial deployment |

### 6.2 Saab UK LookOut Phase 3 — Key Defence Contract

| Item | Detail |
|------|--------|
| **Programme** | LookOut — Maritime Early Warning Innovations |
| **Funder** | DASA (Defence & Security Accelerator) on behalf of Royal Navy |
| **Prime Contractor** | Saab UK |
| **AI Partner** | Mind Foundry Ltd |
| **Research Partner** | DSTL (Defence Science & Technology Laboratory) |
| **Objective** | Mature and de-risk technologies for future maritime early warning solutions |
| **Context** | Potential successor to Crowsnest (out-of-service date 2029) |
| **Significance** | Validates Mind Foundry's AI for sovereign UK defence programmes |

> **Contract significance:** The Saab-Mind Foundry partnership for LookOut Phase 3 is Mind Foundry's most visible defence contract. Saab is a Tier 1 defence contractor — this partnership validates Mind Foundry as a credible defence AI supplier. The programme sits within the Royal Navy's future maritime surveillance architecture, suggesting Mind Foundry's sensor fusion capabilities are being evaluated at the strategic level.

---

## 7. AWARDS & RECOGNITION

| Award | Year | Significance |
|-------|------|-------------|
| **The Times Tech 100** | 2025 | Ranked #11 — Britain's fastest-growing private tech companies |
| **British Business Awards (UK-Japan Partnership)** | 2023 | With Aioi Nissay Dowa Insurance; British Chamber of Commerce in Japan |
| **Bloomberg coverage** | 2023 | AI startup profile — insurer cognitive decline detection |
| **Times Tech 100 listing** | 2025 | Validates commercial growth trajectory |

---

## 8. PERFORMANCE COMPARISON

### 8.1 Mind Foundry SENTRY vs Other Acoustic C-UAS Systems

| Parameter | Mind Foundry SENTRY | Squarehead Discovair G2+ | BeephoniX M2 | Fraunhofer IDMT | VN-CUAS (Target) |
|-----------|--------------------|--------------------------|--------------|--------------------|-------------------|
| **Architecture** | AI software (HW-agnostic) | Hardware sensor | Hardware sensor | Research algorithms | Hardware sensor + ML |
| **Primary Technology** | Bayesian ML on acoustics | Beamforming + ML | Bio-inspired Doppler + ML | Acoustic fingerprint + ML | Beamforming + ML |
| **Microphone Hardware** | Any (including phone mic) | 128 proprietary MEMS | 151 proprietary dynamic MEMS | Standard microphone array | 128-256 MEMS (target) |
| **Detection Range** | ~200m-1km (est.) | 300-1000m | 200-900m | 50-200m | 500-800m |
| **Mobile Deployment** | **<30 seconds** (ATAK) | Minutes (man-portable) | Minutes (lightweight) | Lab setup | <10 min (target) |
| **Weight** | Zero additional (uses phone) | 8 kg | 950g | Research prototype | 1-2 kg (target) |
| **Fibre-optic Drones** | **Yes** | Yes | Yes | Yes | Yes |
| **ATAK Integration** | **Native** | No | No | No | Target yes |
| **Sensor Fusion** | Yes (multi-modal) | Limited | Limited | No | SAPIENT target |
| **ASW Capability** | **Yes (NIGHTINGALE)** | No | No | No | No |
| **Edge AI** | Yes | Limited | Limited | No | Target yes |
| **Continuous Learning** | Yes | Limited | Limited | Yes (research) | Target yes |
| **Est. System Price** | Software license model (est. $20K-100K+) | $50K-150K | $20K-50K est. | Research licensing | $2K-5K target |
| **Country** | UK | Norway | Netherlands | Germany | Vietnam |

### 8.2 Mind Foundry vs AI/Software C-UAS Competitors

| Aspect | Mind Foundry | Dedrone (Axon) | DroneShield |
|--------|-------------|----------------|-------------|
| **Core Approach** | Acoustic AI | RF software C2 | Multi-sensor hardware |
| **Sensor Type** | Acoustic (any mic) | RF (proprietary SDR) | RF + radar + optical + acoustic |
| **IP Foundation** | Oxford ML Research Group | Kassel RF engineering | Australian defence engineering |
| **Business Model** | AI software license | SaaS + sensor sales | Product sales + contracts |
| **Acoustic Capability** | **Primary modality** | Third-party integration | Via Squarehead partnership |
| **Hardware** | None (HW-agnostic) | RF-160, RF-360 sensors | DroneSentry, RfOne, etc. |
| **Autonomous Drones** | **Detects** | Cannot detect | Partial (radar) |
| **ATAK Integration** | **Native** | No | No |
| **Mobile in <30s** | **Yes** | No | No |
| **SAPIENT** | Not confirmed | Yes | Yes |
| **Parent** | Independent (Oxford spin-out) | Axon (NASDAQ: AXON) | ASX:DRO (A$2.9B) |
| **Funding** | ~$44M | ~$130M + Axon backing | Public (A$2.9B mkt cap) |

---

## 9. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 9.1 Overall Function

**Detect, classify, track, and alert on unauthorized small UAS in protected airspace through AI-enabled acoustic intelligence, deployable in <30 seconds on standard soldier equipment.**

### 9.2 Function Structure

```
OVERALL: Acoustic Intelligence for Airspace Protection
├── F1: Acquire acoustic data (hardware-agnostic)
│   ├── F1.1: Capture sound via device microphone (mobile ATAK)
│   ├── F1.2: Capture sound via installed microphone array (static)
│   ├── F1.3: Mesh multiple acoustic sources into network
│   └── F1.4: Provide continuous real-time audio stream
├── F2: Process acoustic signals (Bayesian signal processing)
│   ├── F2.1: Filter environmental noise (wind, rain, traffic, animals)
│   ├── F2.2: Model non-linear sound propagation (terrain, temperature)
│   ├── F2.3: Separate individual sound sources from mixture
│   └── F2.4: Generate time-frequency spectrograms
├── F3: Classify acoustic threats (ML classification)
│   ├── F3.1: Apply computer vision to spectrograms
│   ├── F3.2: Match patterns against acoustic signature database
│   ├── F3.3: Identify drone type, size, motor characteristics
│   ├── F3.4: Score classification confidence
│   └── F3.5: Discriminate drones from birds, vehicles, aircraft
├── F4: Track and localise targets (acoustic triangulation)
│   ├── F4.1: Estimate direction of arrival from multiple nodes
│   ├── F4.2: Triangulate position using distributed sensors
│   ├── F4.3: Predict trajectory and movement
│   └── F4.4: Maintain track continuity across sensor handoffs
├── F5: Fuse multi-sensor data (sensor fusion engine)
│   ├── F5.1: Correlate acoustic detections with radar/camera/RF data
│   ├── F5.2: Resolve conflicting sensor reports
│   ├── F5.3: Generate common operating picture
│   └── F5.4: Prioritise threats by severity and confidence
├── F6: Present intelligence to operator (ATAK integration)
│   ├── F6.1: Display threat on tactical map
│   ├── F6.2: Generate prioritised alerts
│   ├── F6.3: Reduce cognitive load through AI-processed output
│   └── F6.4: Support human-in-the-loop decision making
└── F7: Learn and adapt (continuous improvement)
    ├── F7.1: Capture new drone acoustic signatures from field encounters
    ├── F7.2: Retrain ML models with new data
    ├── F7.3: Deploy updated models to edge devices
    └── F7.4: Maintain acoustic signature database
```

---

## 10. BOM ESTIMATE (Reverse-Engineered)

### 10.1 Mind Foundry SENTRY — Software-Only Model

Since SENTRY is software-only (hardware-agnostic), the "BOM" is fundamentally different from hardware-based systems:

| Component | Type | Est. Cost |
|-----------|------|-----------|
| **ML Model Development** | R&D (one-time) | $2M-5M+ (core AI engine) |
| **Signal Processing Algorithms** | R&D (one-time) | $1M-3M (Bayesian framework) |
| **ATAK Plugin Development** | Software (one-time) | $200K-500K |
| **Acoustic Signature Database** | Data asset (ongoing) | $100K-500K/year maintenance |
| **Edge Inference Runtime** | Software (one-time) | $200K-500K |
| **Sensor Fusion Engine** | Software (one-time) | $500K-1M |
| **Testing & Validation** | QA (ongoing) | $200K-500K/year |
| **Total Development** | | **$4M-10M+** |
| **Marginal Cost per Deployment** | Software license | **Near-zero** |

### 10.2 SENTRY Mobile Deployment — End-User Hardware

| Component | Type | Est. Cost |
|-----------|------|-----------|
| ATAK-capable device | Standard military smartphone/tablet | $500-2,000 (government issue) |
| Chest mount | Standard MOLLE-compatible mount | $50-100 |
| SENTRY software license | Per-device or per-unit license | $5K-20K est. (annual) |
| **Total per Soldier** | | **$5.5K-22K (first year)** |

### 10.3 SENTRY Static Deployment — Estimated Hardware

| Component | Specification | Est. Cost |
|-----------|---------------|-----------|
| External microphone array | COTS microphone array (4-16 mics) | $500-5,000 |
| Edge compute unit | Ruggedised mini-PC or SBC | $500-2,000 |
| Networking | WiFi/LTE/mesh radio | $200-500 |
| Power supply | Solar/battery/mains | $100-500 |
| Enclosure | IP67 weatherproof | $200-500 |
| Mounting hardware | Pole/wall mount | $100-200 |
| SENTRY software license | Per-node annual license | $5K-20K est. |
| **Total per Static Node** | | **$6.6K-28.7K** |

> **Business model insight:** Mind Foundry's software-only approach means near-zero marginal cost per deployment — the dominant cost is the software license, not hardware. This is the opposite of Squarehead (hardware margin) or DroneShield (product sales). For VN-CUAS, this suggests a hybrid model: manufacture low-cost Vietnamese hardware + develop indigenous acoustic ML software = maximum local content and margin.

---

## 11. DESIGN INSIGHTS FOR VN-CUAS

### 11.1 Key Lessons from Mind Foundry

1. **AI is the moat, not hardware:** Mind Foundry proves that acoustic C-UAS value lies in the AI/ML algorithms, not the microphones. VN-CUAS should invest proportionally: 60% in ML/software, 40% in hardware.

2. **Hardware-agnostic is powerful:** SENTRY works with any microphone — even smartphone mics. VN-CUAS should design software that is not locked to proprietary hardware, enabling flexible deployment across different Vietnamese military equipment.

3. **ATAK integration is a force multiplier:** The <30 second mobile deployment using existing soldier equipment is a breakthrough concept. VN-CUAS should target TAK (Android Team Awareness Kit) or equivalent Vietnamese C2 integration from day one.

4. **Spectrograms + computer vision is the state of the art:** Converting acoustic signals to spectrograms and applying CV is Mind Foundry's core approach. This is a well-validated ML pipeline that VN-CUAS should adopt — existing CV model architectures (CNNs, Vision Transformers) can be leveraged.

5. **Cross-domain validates the algorithm:** NIGHTINGALE (ASW) using the same engine as SENTRY (C-UAS) proves the acoustic ML pipeline is generalizable. VN-CUAS should design the acoustic engine as a reusable platform (drones today, potentially mortar/artillery detection, border surveillance, etc.).

6. **Bayesian approach handles uncertainty well:** Military acoustic environments are inherently noisy and uncertain. Bayesian methods provide confidence scoring alongside classifications — critical for military decision-making. VN-CUAS should adopt Bayesian or probabilistic ML frameworks.

7. **Continuous learning is essential:** Mind Foundry's system improves with each new drone encounter. VN-CUAS must design a feedback loop from field deployment to model retraining from the start.

8. **Edge deployment is critical:** AI inference must run on edge devices (no guaranteed cloud connectivity in military operations). VN-CUAS should design for edge-first, cloud-optional architecture.

### 11.2 VN-CUAS Positioning vs Mind Foundry

| Scenario | Positioning |
|----------|-------------|
| **Hardware complement** | VN-CUAS provides low-cost Vietnamese-manufactured acoustic hardware that Mind Foundry (or similar) AI can run on |
| **Indigenous alternative** | VN-CUAS develops its own acoustic ML engine — lower capability but 100% sovereign |
| **Hybrid approach** | VN-CUAS hardware + licensed/adapted ML from academic partnerships (Vietnamese universities) |
| **Low-cost mass deployment** | VN-CUAS at $2K-5K vs Mind Foundry's est. $20K+ per node — 4-10x cost advantage for saturation deployment |
| **ASEAN market** | VN-CUAS as affordable acoustic C-UAS for ASEAN nations that cannot access UK/Western AI |

### 11.3 Updated VN-CUAS Product Concept (v6.0)

Building on insights from all 6 RE analyses (Squarehead, BeephoniX, Fraunhofer, DroneShield, Dedrone, Mind Foundry):

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Array** | 128-256 MEMS microphones | Squarehead (128), BeephoniX (151) benchmarks |
| **Weight** | 1-2 kg | BeephoniX (950g) proves ultra-light is feasible |
| **Power** | <10W | Fraunhofer sensor wake-up; solar/battery viability |
| **Detection Range** | 500-800m | Acoustic physics limit; extended via mesh network |
| **Accuracy** | ≤5° azimuth, ≤10° elevation | BeephoniX (1-2°) benchmark |
| **Target Price** | $2K-5K per node | 10-100x cheaper than Western alternatives |
| **Environmental** | IP67, MIL-STD-810H | DroneShield (IP67) + Dedrone OTM (MIL-STD-810H) standard |
| **Classification** | Acoustic fingerprint DB (cloud-updatable) | Modeled on DroneDNA + SENTRY continuous learning |
| **ML Pipeline** | **Spectrogram → Computer Vision → Classification** | Mind Foundry validated approach — use CNN/ViT on spectrograms |
| **Integration** | SAPIENT + RESTful API + **TAK plugin** | Dedrone/DroneShield (SAPIENT) + Mind Foundry (ATAK) |
| **Mobile Mode** | **TAK app on soldier device** (secondary) | Mind Foundry <30s concept adapted for VN forces |
| **Deployment** | Tool-less <10 min; magnetic/clamp mount (hardware node) | DroneShield rapid deployment model |
| **Autonomous Detection** | YES — does not require RF emissions | Key differentiator vs Dedrone/DroneShield RF |
| **Software** | **Edge-first, cloud-optional** acoustic ML engine | Mind Foundry edge AI + Fraunhofer processing stack |
| **Bayesian Framework** | Probabilistic classification with confidence scoring | Mind Foundry Bayesian approach for uncertain environments |
| **Local Content** | ≥60% by value | Vietnamese defense requirement |
| **Cross-Domain Potential** | Drone → mortar → artillery → border surveillance | Mind Foundry NIGHTINGALE proves cross-domain viability |

### 11.4 C-UAS Ecosystem Map (After 6 RE Analyses)

```
MARKET LANDSCAPE (2025-2026) — UPDATED
═══════════════════════════════════════════════════════════════

HIGH COST ($100K-1M+)    ┌──────────────────────────────────┐
Multi-Sensor Systems      │  DroneShield DroneSentry          │
                          │  Dedrone Full System               │
                          │  (Complete DTI-M kill chain)       │
                          └──────────────────────────────────┘

MID COST ($20K-100K)      ┌──────────────────────────────────┐
Specialized Sensors       │  Squarehead Discovair G2+          │
                          │  Dedrone RF-360 sensor             │
                          │  Mind Foundry SENTRY (est.)        │
                          │  (Single modality / AI layer)      │
                          └──────────────────────────────────┘

LOW COST ($2K-20K)        ┌──────────────────────────────────┐
Entry/Complementary       │  BeephoniX M2                      │
                          │  ★ VN-CUAS (TARGET) ★              │
                          │  (Affordable acoustic detection)   │
                          └──────────────────────────────────┘

RESEARCH/ALGORITHM        ┌──────────────────────────────────┐
Technology Provider       │  Fraunhofer IDMT                   │
                          │  Mind Foundry (AI engine licensing) │
                          │  (Algorithms + consulting)         │
                          └──────────────────────────────────┘

PARADIGMS IDENTIFIED:
• HARDWARE-CENTRIC: Squarehead, BeephoniX, DroneShield
• SOFTWARE-CENTRIC: Dedrone (RF), Mind Foundry (Acoustic AI)
• ALGORITHM-CENTRIC: Fraunhofer IDMT
• VN-CUAS APPROACH: Hardware + Indigenous ML (hybrid)
═══════════════════════════════════════════════════════════════
```

---

## 12. INTELLIGENCE GAPS

| ID | Gap | Priority | Impact on VN-CUAS |
|----|-----|----------|-------------------|
| IG-01 | SENTRY exact detection range and accuracy specifications | **High** | Performance benchmarking |
| IG-02 | ML model architecture details (CNN type, model size, inference time) | **High** | VN-CUAS ML architecture design |
| IG-03 | SENTRY pricing model (per-device, per-site, annual license) | Medium | VN-CUAS competitive positioning |
| IG-04 | Acoustic signature database size (how many drone models?) | **High** | VN-CUAS database strategy |
| IG-05 | Edge hardware requirements (minimum compute specs) | Medium | VN-CUAS hardware design |
| IG-06 | ATAK plugin architecture and API documentation | Medium | VN-CUAS TAK integration design |
| IG-07 | Field deployment results (detection rate, false positive rate) | **High** | VN-CUAS performance targets |
| IG-08 | SAPIENT compliance status | Medium | VN-CUAS interoperability planning |
| IG-09 | Mind Foundry patent portfolio (specific acoustic ML patents) | Medium | VN-CUAS IP freedom-to-operate |
| IG-10 | NIGHTINGALE field deployment results and customer list | Low | Cross-domain architecture validation |
| IG-11 | Post-Mullins strategic direction under Okochi leadership | Medium | Market trajectory assessment |
| IG-12 | Performance in tropical/high-humidity environments | Medium | Vietnam deployment suitability |

---

## 13. REFERENCES

1. Mind Foundry Official Website — https://www.mindfoundry.ai/
2. Mind Foundry SENTRY C-UAS — https://www.mindfoundry.ai/defence/offerings/counter-uas-sentry
3. Mind Foundry SENTRY Sensor Fusion — https://www.mindfoundry.ai/sentry-sensor-fusion
4. Mind Foundry NIGHTINGALE ASW — https://www.mindfoundry.ai/nightingale
5. Mind Foundry Leadership — https://www.mindfoundry.ai/about-us/leadership
6. Mind Foundry About Us — https://www.mindfoundry.ai/about-us
7. Wikipedia: Mind Foundry — https://en.wikipedia.org/wiki/Mind_Foundry
8. techUK: AI-powered Acoustic Intelligence: The Future of Counter-UAS (Syreeta Cummings, Jul 2025) — https://www.techuk.org/resource/ai-powered-acoustic-intelligence-the-future-of-counter-uas.html
9. Saab UK: LookOut Phase 3 Contract — https://www.saab.com/markets/united-kingdom/stories/saab-uk-awarded-lookout-phase-3-contract
10. GOV.UK: Look Out! Maritime Early Warning (DASA) — https://www.gov.uk/government/publications/competition-look-out-maritime-early-warning-innovations
11. Wikipedia: Stephen Roberts — https://en.wikipedia.org/wiki/Stephen_Roberts_(academic)
12. Mind Foundry blog: Acoustic Intelligence for Counter-UAS — https://www.mindfoundry.ai/blog/acoustic-intelligence-for-counter-uas
13. Mind Foundry blog: Acoustic Intelligence for ASW — https://www.mindfoundry.ai/blog/acoustic-intelligence-for-anti-submarine-warfare
14. Mind Foundry blog: AI at the Edge — https://www.mindfoundry.ai/blog/ai-at-the-edge-transforming-defence-operations
15. Analytics Insight: Mind Foundry Company Profile — https://www.analyticsinsight.net/company-profile/mind-foundry
16. UK Tech News: Mind Foundry Series A — https://www.uktechnews.info/2020/11/09/mind-foundry-secures-10-4-million-series-a-investment-led-by-aioi-nissay-dowa-insurance/
17. AI Magazine: 5 Minutes with Brian Mullins — https://aimagazine.com/ai-applications/5-minutes-with-brian-mullins-ceo-at-mind-foundry
18. Tracxn: Mind Foundry profile — https://tracxn.com/d/companies/mind-foundry/
19. YouTube: Mind Foundry SENTRY demo — https://www.youtube.com/watch?v=CEMZdSTbePY

---

## 14. COMPARATIVE SUMMARY TABLE

| Dimension | Squarehead G2+ | BeephoniX M2 | Fraunhofer IDMT | DroneShield DroneSentry | Dedrone DroneTracker | **Mind Foundry SENTRY** | VN-CUAS Target |
|-----------|---------------|-------------|-----------------|------------------------|---------------------|------------------------|---------------|
| **Country** | Norway | Netherlands | Germany | Australia | Germany/USA | **United Kingdom** | Vietnam |
| **Type** | Acoustic sensor | Acoustic sensor | Research/algorithms | Multi-sensor system | Software C2 platform | **Acoustic AI software** | Acoustic sensor + ML |
| **Founded** | 2000 | 2022 | 2008 (HSA) | 2014 | 2014 | **2016** | 2026 |
| **Ownership** | Private | Private | Public institute | ASX:DRO | Axon (NASDAQ: AXON) | **Private (Oxford spin-out)** | State enterprise |
| **Primary Sensor** | 128 MEMS | 151 MEMS | Microphone array | RF + radar + optical | RF (SDR-based) | **Any microphone (AI)** | 128-256 MEMS |
| **Core Technology** | Beamforming | Bio-inspired Doppler | Acoustic fingerprint | Multi-sensor fusion | RF protocol matching | **Bayesian ML + CV** | Beamforming + ML |
| **Detection Range** | 300-1000m | 200-900m | 50-200m | 1-8 km | 1.6-5 km | **~200m-1km (est.)** | 500-800m |
| **Weight** | 8 kg | 950g | Research prototype | 46 kg (X Mk2) | ~5-8 kg/sensor | **0 kg (uses phone)** | 1-2 kg |
| **Mobile Deploy** | Minutes | Minutes | Lab | Minutes-hours | Minutes-hours | **<30 seconds** | <10 min |
| **Classification** | Type/class | Type/class | ML fingerprint | 150+ models (RFAI) | 600+ models (DroneDNA) | **ML acoustic DB** | Type/class + DB |
| **Autonomous Detect** | Yes | Yes | Yes | Partial | No (needs RF) | **Yes** | Yes |
| **ATAK Integration** | No | No | No | No | No | **Native** | Target yes |
| **Sensor Fusion** | Limited | Limited | No | DroneSentry-C2 | DedroneTracker.AI | **SENTRY Sensor Fusion** | SAPIENT client |
| **Cross-Domain** | No | No | Industrial | No | No | **Yes (ASW via NIGHTINGALE)** | Potential |
| **Defeat** | No | No | No | Yes (jamming) | Yes (Defender 2) | **No** | No |
| **Funding** | Undisclosed | ~€0.5M | Government institute | A$2.9B mkt cap | ~$130M + Axon | **~$44M** | Government |
| **Est. Price/Node** | $50K-150K | $20K-50K | Research license | $200K-1M+/site | $50K-500K+ | **$20K-100K+ (est.)** | $2K-5K |
