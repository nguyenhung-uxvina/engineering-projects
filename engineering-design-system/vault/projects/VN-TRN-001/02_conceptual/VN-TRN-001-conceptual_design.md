---
project: VN-TRN-001
phase: 2
type: conceptual-design
version: 1.0
created: 2026-02-06
status: draft
---

# CONCEPTUAL DESIGN
## VN-TRN-001: Vietnamese LOMAH Electronic Scoring System
### Version: 1.0 | Date: 2026-02-06

---

## 1. ABSTRACTION (5-Step Process)

### Step 1: Eliminate Personal Preferences

| Original (with preferences) | Abstracted (preferences removed) |
|------------------------------|----------------------------------|
| "Use Saab-style calibration-free algorithm" | "Determine shot location without per-session calibration" |
| "Use FPGA for signal processing" | "Process sensor signals with sufficient timing resolution" |
| "Use WiFi for communication" | "Transmit scoring data wirelessly" |
| "Use web-based HTML5 display" | "Present scoring results to operator" |
| "Use Vietnamese natural rubber" | "Provide acoustic isolation and sealing" |

### Step 2: Omit Non-Essential Requirements

| Retained (Essential) | Omitted (Non-essential for concept phase) |
|----------------------|------------------------------------------|
| Detect projectile trajectory | Specific IP rating number |
| Determine X,Y impact location | Exact connector type |
| Operate without calibration | Color-coding scheme |
| Transmit results wirelessly | Specific export file format |
| Survive tropical environment | Specific battery chemistry |
| Producible in Vietnam | Certification details |

### Step 3: Transform Quantitative → Qualitative

| Quantitative | Qualitative |
|-------------|-------------|
| ±10mm accuracy | "Determine location with sufficient precision" |
| ≥10 hours battery | "Operate through a full training day" |
| ≤500ms latency | "Display results in near real-time" |
| ≥10 lanes | "Support multi-lane range operations" |
| ≤$500/lane | "Achieve cost significantly below imports" |

### Step 4: Generalize

| Specific | Generalized |
|----------|------------|
| "Detect acoustic shockwave from supersonic bullet" | "Sense projectile passage through detection plane" |
| "Calculate TDOA from 4 microphones" | "Determine trajectory from multi-point measurement" |
| "Transmit via Ethernet/WiFi/VHF" | "Communicate data between field and control station" |
| "Display on HTML5 web interface" | "Present information to operator" |

### Step 5: Solution-Neutral Problem Statement

> **"Sense the passage of a projectile through a defined detection plane, determine its location within that plane with sufficient precision for marksmanship assessment, and communicate the result to operators -- without requiring per-session calibration, surviving tropical field conditions, and producible with Vietnamese industrial capability."**

**Essence (Input → Output):**
```
INPUT:                              OUTPUT:
• Projectile passage (energy)  →    • Location coordinates (X,Y)
• Electrical power             →    • Hit/miss classification
• Operator commands            →    • Statistical reports
                                    • After-action data
```

---

## 2. FUNCTION STRUCTURE

### 2.1 Overall Function

```
╔═══════════════════════════════════════════════════════════════════╗
║          VN-LOMAH: OVERALL FUNCTION                               ║
║                                                                   ║
║   "Sense projectile passage and determine impact location         ║
║    in a defined detection plane"                                  ║
║                                                                   ║
║   INPUT                              OUTPUT                       ║
║   ─────                              ──────                       ║
║   E: Electrical power          →     E: (waste heat)              ║
║   M: Projectile (passes thru)  →     M: Projectile (unaffected)   ║
║   S: Operator commands         →     S: X,Y coordinates           ║
║                                      S: Hit/miss classification    ║
║                                      S: Statistical reports        ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 2.2 Sub-Function Breakdown

```
F0: Sense projectile & determine impact location
│
├── F1: SENSE projectile passage
│   ├── F1.1: Detect physical phenomenon (shockwave / radar echo / IR)
│   ├── F1.2: Convert physical signal to electrical signal
│   └── F1.3: Condition electrical signal (filter, amplify)
│
├── F2: MEASURE timing/parameters
│   ├── F2.1: Digitize conditioned signals (ADC)
│   ├── F2.2: Determine arrival times at each sensor
│   └── F2.3: Calculate time differences (TDOA or equivalent)
│
├── F3: COMPUTE location
│   ├── F3.1: Execute positioning algorithm
│   ├── F3.2: Compensate for environmental factors
│   └── F3.3: Classify hit vs miss against target silhouette
│
├── F4: COMMUNICATE results
│   ├── F4.1: Encode scoring data
│   ├── F4.2: Transmit to display/control station
│   └── F4.3: Receive operator commands
│
├── F5: PRESENT information
│   ├── F5.1: Display X,Y on target overlay
│   ├── F5.2: Compute and display statistics
│   └── F5.3: Generate/export reports
│
├── F6: SUPPLY power
│   ├── F6.1: Accept/convert power source
│   ├── F6.2: Regulate and distribute to subsystems
│   └── F6.3: Monitor power status
│
└── F7: PROTECT system
    ├── F7.1: Shield from environment (rain, dust, heat)
    ├── F7.2: Protect from ballistic damage
    └── F7.3: Self-diagnose faults (BIT)
```

### 2.3 Function Flow Diagram

```
                     OPERATOR COMMANDS (S)
                            │
                            ▼
POWER (E) ──→ [F6: SUPPLY] ──→ E to all subsystems
                            │
                            │
PROJECTILE (M) ─────────────┼──→ (passes through unaffected)
        │                   │
        ▼                   │
[F1: SENSE]                 │
  │ E: shockwave/radar/IR   │
  │ → electrical signal      │
  ▼                         │
[F2: MEASURE]               │
  │ S: timing data          │
  │                         │
  ▼                         │
[F3: COMPUTE]               │
  │ S: X,Y coordinates      │
  │ S: hit/miss             │
  ▼                         │
[F4: COMMUNICATE] ←─────────┘ (commands)
  │ S: scoring data
  │ (wired or wireless)
  ▼
[F5: PRESENT]
  │ S: display output
  │ S: reports
  ▼
OPERATOR (receives results)

[F7: PROTECT] ← surrounds F1-F6 (environment, ballistic, BIT)
```

### 2.4 Function Table

| ID | Function | Input | Output | Type | Key Requirement |
|----|----------|-------|--------|------|-----------------|
| F1 | Sense projectile passage | M: projectile energy (acoustic/EM) | E: raw electrical signal | Main | SIG-04, FRC-01 |
| F2 | Measure timing parameters | E: raw signal | S: digital timing data | Main | SIG-05, KIN-01 |
| F3 | Compute location | S: timing data | S: X,Y coordinates, hit/miss | Main | SIG-04, OPR-08 |
| F4 | Communicate results | S: scoring data + commands | S: transmitted data | Main | SIG-01, SIG-02 |
| F5 | Present information | S: scoring data | S: visual display, reports | Main | SIG-09, SIG-10 |
| F6 | Supply power | E: battery/mains | E: regulated DC | Support | ENG-01 to ENG-05 |
| F7 | Protect system | Environment threats | System integrity | Support | OPR-01 to OPR-07 |

---

## 3. MORPHOLOGICAL MATRIX

### 3.1 Working Principles per Sub-Function

| Sub-Function | P1 | P2 | P3 | P4 |
|-------------|-----|-----|-----|-----|
| **F1: Sense** | Acoustic microphones (MEMS) | Acoustic piezoelectric | Doppler radar | Infrared optical |
| **F2: Measure** | High-speed ADC + FPGA | High-speed ADC + MCU (DSP) | Time-to-Digital Converter (TDC) IC | Analog comparator + timer |
| **F3: Compute** | Calibration-free TDOA (Saab patent) | Standard TDOA + temp sensor | Correlation-based (matched filter) | Neural network (ML) |
| **F4: Communicate** | Ethernet (wired) | WiFi 802.11n | VHF radio | LoRa LPWAN |
| **F5: Present** | Web-based HTML5 (any device) | Dedicated display unit (VDU) | Mobile app (iOS/Android) | PC software (desktop) |
| **F6: Supply** | Li-ion battery + DC-DC | Lead-acid battery | Mains AC + UPS | Solar + supercap |
| **F7: Protect** | Aluminum IP67 enclosure | Polymer IP67 enclosure | Stainless steel enclosure | Composite (GRP) enclosure |

### 3.2 Working Principle Assessment

#### F1: Sense Projectile Passage

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: MEMS microphones** | 9 | Proven, low cost ($2-5/ea), small, 8 RE competitors use this | Supersonic only; wind/rain noise | Low | 20% (import sensor, local PCB) |
| **P2: Piezoelectric** | 8 | Robust, high SPL tolerance, simple | Lower sensitivity, needs more conditioning | Low | 30% (import element, local housing) |
| **P3: Doppler radar** | 6 | Works subsonic + supersonic; wind immune | Complex, higher cost, export control risk, lower accuracy | High | 15% (import radar module) |
| **P4: IR optical** | 5 | Non-acoustic; weather immune | Requires line-of-sight, expensive, alignment critical | Very High | 10% |

#### F2: Measure Timing

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: ADC + FPGA** | 9 | Highest timing resolution (<1μs), parallel channels, flexible | FPGA expertise needed, higher power, BOM $30-50 | Medium | 25% (import FPGA, local PCB) |
| **P2: ADC + MCU (DSP)** | 9 | Simpler firmware, proven ARM ecosystem, lower power | Lower parallel throughput, may limit accuracy at high rates | Low | 30% (import MCU, local PCB) |
| **P3: TDC IC** | 8 | Purpose-built for timing, very high resolution (ps) | Limited flexibility, niche supply chain | Medium | 20% |
| **P4: Analog comparator + timer** | 7 | Simplest, lowest cost, lowest power | Lowest accuracy, no waveform capture, limited diagnostics | Very Low | 40% |

#### F3: Compute Location

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: Calibration-free TDOA** | 9 | No calibration shots, patent EXPIRED, temp-independent | Requires 4+ sensors, specific geometry | Low | 90% (software, expired patent) |
| **P2: Standard TDOA + temp sensor** | 9 | Well-understood, simpler math | Needs temp sensor + calibration shot; less accurate in varying temp | Low | 85% (software) |
| **P3: Correlation-based** | 7 | Better noise rejection, works with degraded signals | Higher compute requirement, more complex firmware | Medium | 80% (software) |
| **P4: Neural network (ML)** | 4 | Self-calibrating potential, could learn environment | Training data needed, black-box, regulatory acceptance questionable | Medium | 70% (software) |

#### F4: Communicate

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: Ethernet** | 9 | Reliable, high bandwidth, FASIT standard, low latency | Requires cable runs (labor, fragile in field) | Low | 60% (local cable, import switch) |
| **P2: WiFi 802.11n** | 9 | No cables, fast deployment, 300m+ range | Interference risk, power consumption, range limits | Low | 40% (import module) |
| **P3: VHF radio** | 9 | Long range (2-10 km), robust, military standard | Lower bandwidth, latency, frequency coordination | Medium | 30% (import radio) |
| **P4: LoRa LPWAN** | 8 | Very long range (5-15 km), ultra-low power | Very low bandwidth, high latency (seconds), not real-time | Low | 35% |

#### F5: Present Information

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: Web-based HTML5** | 9 | Any device (phone/tablet/PC), no install, updatable, Vietnamese-easy | Needs WiFi/Ethernet to device, browser dependency | Very Low | 95% (domestic dev) |
| **P2: Dedicated VDU** | 9 | Purpose-built, ruggedized, sun-readable | Expensive per unit, single-purpose, supply chain | High | 40% |
| **P3: Mobile app** | 9 | Modern UX, offline capable, camera integration | Platform maintenance (iOS+Android), app store restrictions | Low | 90% (domestic dev) |
| **P4: PC desktop software** | 9 | Full-featured, database, large screen | Requires PC at range, less portable | Low | 90% (domestic dev) |

#### F6: Power Supply

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: Li-ion + DC-DC** | 9 | High energy density, rechargeable, light | Import cells, BMS needed, air transport regs | Medium | 55% (local pack assembly) |
| **P2: Lead-acid** | 9 | Cheap, locally available, no transport regs | Heavy, lower energy density, shorter life | Low | 80% (local sourcing) |
| **P3: Mains AC + UPS** | 9 | Unlimited runtime at fixed ranges | Not portable, infrastructure needed | Low | 70% |
| **P4: Solar + supercap** | 7 | Off-grid, no resupply, green | Weather dependent, expensive, large panel | High | 40% |

#### F7: Protect (Enclosure)

| Principle | TRL | Pros | Cons | Cost | Local Content |
|-----------|-----|------|------|------|---------------|
| **P1: Aluminum 6061-T6** | 9 | Strong, light, machinable, corrosion-resistant (anodized) | Higher cost than polymer, thermal conductor | Medium | 80% (local machining) |
| **P2: Polymer (ASA/ABS)** | 9 | Cheapest, lightest, injection moldable, no corrosion | Lower impact resistance, UV degradation, not ballistic | Low | 85% (local molding) |
| **P3: Stainless steel 316** | 9 | Highest strength, best corrosion, ballistic protection | Heavy, expensive, harder to machine | High | 75% (local machining) |
| **P4: GRP composite** | 8 | Light, strong, corrosion-proof, radar-transparent | Tooling cost for molds, harder to repair | Medium | 70% (local layup) |

---

## 4. CONCEPT GENERATION

### 4.1 Concept Paths Through Morphological Matrix

| Sub-Function | Concept A: "Baseline" | Concept B: "Field Portable" | Concept C: "Multi-Mode" | Concept D: "Ultra-Low-Cost" |
|-------------|----------------------|----------------------------|------------------------|---------------------------|
| F1: Sense | P1: MEMS microphones | P1: MEMS microphones | P1: MEMS mic + P3: Radar (dual) | P2: Piezoelectric |
| F2: Measure | P1: ADC + FPGA | P2: ADC + MCU | P1: ADC + FPGA | P4: Comparator + timer |
| F3: Compute | P1: Calibration-free TDOA | P1: Calibration-free TDOA | P1: Calibration-free TDOA | P2: Standard TDOA + temp |
| F4: Communicate | P1: Ethernet (primary) | P2: WiFi (primary) | P1: Ethernet + P2: WiFi | P1: Ethernet only |
| F5: Present | P1: Web-based HTML5 | P1: Web HTML5 + P3: Mobile app | P1: Web HTML5 + P4: PC software | P4: PC software only |
| F6: Power | P1: Li-ion + DC-DC | P1: Li-ion + DC-DC | P1: Li-ion + P3: Mains | P2: Lead-acid |
| F7: Protect | P1: Aluminum 6061-T6 | P2: Polymer (ASA) | P1: Aluminum + P4: GRP (radar window) | P2: Polymer (ABS) |

### 4.2 Concept Descriptions

---

#### CONCEPT A: "BASELINE" -- Fixed-Range Calibration-Free LOMAH

**Philosophy:** Proven technology, maximum reliability, Saab-inspired calibration-free with modern Vietnamese production.

```
CONCEPT A ARCHITECTURE
═══════════════════════

TARGET AREA                                    CONTROL STATION
┌──────────────────────┐                      ┌────────────────────┐
│  BSU (Aluminum IP67)  │     CAT 5e/6        │  Any device with   │
│  4× MEMS microphones  │═════════════════════│  web browser       │
│  FPGA timing capture  │     Ethernet         │  (tablet/laptop)   │
│  ARM MCU (cal-free    │     100BaseT         │                    │
│   TDOA algorithm)     │                      │  HTML5 Web UI      │
│  Li-ion battery       │                      │  Vietnamese lang   │
│  12V DC / Mains input │                      │  Statistics + AAR  │
│  BIT self-diagnostic  │                      │  Up to 10 lanes    │
└──────────────────────┘                      └────────────────────┘
```

**Key characteristics:**
- Wired Ethernet primary (reliability)
- FPGA for high-speed TDOA (±10mm accuracy)
- Calibration-free algorithm (expired Saab patent)
- Aluminum IP67 enclosure (tropical hardened)
- Web-based display (no proprietary hardware)
- Supersonic only (Phase 1 scope)

**Strengths:** Highest reliability, proven architecture, best accuracy, FASIT compatible
**Weaknesses:** Cable runs in field, not man-portable, fixed infrastructure needed
**Risk:** LOW -- all components proven, no new technology development
**Estimated cost:** $350-450/lane

---

#### CONCEPT B: "FIELD PORTABLE" -- Man-Portable Wireless LOMAH

**Philosophy:** Maximum deployability, inspired by InVeris Portable LOMAH. WiFi-first, lightweight polymer housing.

```
CONCEPT B ARCHITECTURE
═══════════════════════

TARGET AREA                                    FIRING POINT
┌──────────────────────┐                      ┌────────────────────┐
│  BSU (Polymer IP67)   │     WiFi 802.11n    │  Tablet / Phone    │
│  4× MEMS microphones  │ )))))))))))))))))) ))│  (any WiFi device) │
│  ARM MCU + DSP        │     300m-2km LOS     │                    │
│  (cal-free TDOA)      │                      │  HTML5 + Mobile    │
│  Li-ion battery       │                      │  App (offline OK)  │
│  (10h runtime)        │                      │                    │
│  Quick-mount clamps   │                      │  Portable range    │
│  Tool-less setup      │                      │  office in         │
│  <8 kg total          │                      │  ruggedized tablet │
└──────────────────────┘                      └────────────────────┘
```

**Key characteristics:**
- WiFi-first (no cables in field)
- MCU-only processing (lower power, simpler, cheaper)
- Polymer enclosure (lightest weight)
- Tool-less quick-mount sensor bar
- Mobile app + web UI (offline capable)
- Supersonic only

**Strengths:** Lightest, fastest setup (<10 min), lowest cable burden, field-deployable anywhere
**Weaknesses:** WiFi range/interference risk, MCU timing may limit accuracy to ±15mm, polymer less durable
**Risk:** MEDIUM -- MCU timing resolution needs validation for ±10mm accuracy
**Estimated cost:** $280-380/lane

---

#### CONCEPT C: "MULTI-MODE" -- Supersonic + Subsonic Dual-Sensor

**Philosophy:** Maximum capability, combines acoustic TDOA (supersonic) with radar module (subsonic). Premium product for full-spectrum training.

```
CONCEPT C ARCHITECTURE
═══════════════════════

TARGET AREA                                    CONTROL STATION
┌──────────────────────────┐                  ┌────────────────────┐
│  BSU (Aluminum + GRP     │   Ethernet +     │  Range PC/Server   │
│       radar window)      │   WiFi (dual)    │  + Tablet clients  │
│                          │═════════════════ │                    │
│  4× MEMS microphones     │                  │  Full Exercise     │
│  (supersonic acoustic)   │                  │  Management:       │
│  + Radar module          │                  │  - Web UI          │
│  (subsonic 9mm/.45)     │                  │  - PC software     │
│                          │                  │  - Target control  │
│  FPGA timing capture     │                  │  - Vuln model      │
│  ARM MCU (dual algorithm)│                  │  - AAR + reports   │
│  Li-ion + Mains option   │                  │  - FASIT interface │
│  BIT + radar self-test   │                  │  Up to 10+ lanes   │
└──────────────────────────┘                  └────────────────────┘
```

**Key characteristics:**
- Dual sensing: acoustic (supersonic) + radar (subsonic)
- FPGA processing (handles both sensor types)
- Ethernet + WiFi dual communication
- Aluminum + GRP composite (radar-transparent window)
- Full exercise management software (EXCON-level)
- Pixel vulnerability model (Saab AVTI-inspired)

**Strengths:** Full spectrum (all calibers), highest capability, export differentiator, addresses O-28 (subsonic)
**Weaknesses:** Highest complexity, highest cost, radar technology risk (TRL 6), longer development
**Risk:** HIGH -- radar subsonic detection requires R&D; export control risk on radar
**Estimated cost:** $550-750/lane

---

#### CONCEPT D: "ULTRA-LOW-COST" -- Minimum Viable LOMAH

**Philosophy:** Absolute minimum cost, maximum local content. Basic scoring for mass deployment to all Vietnamese ranges.

```
CONCEPT D ARCHITECTURE
═══════════════════════

TARGET AREA                                    RANGE OFFICE
┌──────────────────────┐                      ┌────────────────────┐
│  BSU (ABS plastic)    │     CAT 5e cable    │  Desktop PC        │
│  4× Piezo transducers │═════════════════════│  (any Windows PC)  │
│  Comparator + timer   │     Ethernet         │                    │
│  (basic MCU)          │                      │  PC Software       │
│  Standard TDOA        │                      │  (Vietnamese)      │
│  + temp sensor        │                      │  Basic scoring     │
│  Lead-acid battery    │                      │  display + print   │
│  or 12V vehicle power │                      │                    │
└──────────────────────┘                      └────────────────────┘
```

**Key characteristics:**
- Piezoelectric sensors (cheapest, most robust)
- Analog timing (comparator + timer MCU) -- simplest processing
- Standard TDOA with temperature sensor (calibration shot needed)
- Lead-acid battery (locally available, cheap)
- ABS plastic enclosure (injection moldable)
- PC desktop software only (no web/mobile)
- Ethernet wired only

**Strengths:** Lowest cost ($150-250), highest local content (~72%), simplest to produce, mass-deployable
**Weaknesses:** Requires calibration shot, lower accuracy (±20mm est.), no wireless, heavier, less portable
**Risk:** LOW -- all proven/simple technology, but accuracy may not meet SIG-04 (MUST: ±10mm)
**Estimated cost:** $150-250/lane

---

## 5. VDI 2225 CONCEPT EVALUATION

### 5.1 Evaluation Criteria (Derived from ODI + Requirements)

| # | Criterion | Weight | Rationale (ODI Outcome) |
|---|-----------|--------|------------------------|
| C1 | Scoring accuracy (±10mm MUST) | 0.18 | O-21 (Opp 14.0) + SIG-04 |
| C2 | Calibration-free operation | 0.14 | O-16 (Opp 15.0) + OPR-08 |
| C3 | Local content & supply independence | 0.14 | O-52 (16.5) + O-49 (16.0) + PRD-01 |
| C4 | Unit cost | 0.12 | O-47 (Opp 14.5) + CST-01 |
| C5 | Environmental robustness (tropical) | 0.10 | O-51 (Opp 14.0) + OPR-01 to OPR-07 |
| C6 | Setup speed & portability | 0.08 | O-10 (Opp 12.5) + ASM-01 |
| C7 | Subsonic capability (future-ready) | 0.06 | O-28 (Opp 15.0) -- future phased |
| C8 | Development risk & timeline | 0.08 | SCH-01, SCH-02 |
| C9 | Multi-lane scalability | 0.05 | O-23 + SIG-08 |
| C10 | Lifecycle cost (10-year TCO) | 0.05 | O-47, O-48 + CST-03 |
| | **TOTAL** | **1.00** | |

*Weights set BEFORE evaluation, based on ODI opportunity scores (normalized).*

### 5.2 Evaluation Matrix

**VDI 2225 Scale: 0=Unsatisfactory, 1=Tolerable, 2=Adequate, 3=Good, 4=Very Good**

| # | Criterion | Weight | Concept A "Baseline" | Concept B "Portable" | Concept C "Multi-Mode" | Concept D "Ultra-Low" |
|---|-----------|--------|---------------------|---------------------|----------------------|----------------------|
| C1 | Scoring accuracy | 0.18 | **4** (FPGA ±10mm) | **3** (MCU ±12-15mm risk) | **4** (FPGA ±10mm) | **1** (±20mm, fails MUST) |
| C2 | Calibration-free | 0.14 | **4** (expired patent) | **4** (same algorithm) | **4** (same algorithm) | **0** (needs calibration) |
| C3 | Local content | 0.14 | **3** (~62% local) | **3** (~60% local) | **2** (~52% local, radar import) | **4** (~72% local) |
| C4 | Unit cost | 0.12 | **3** ($350-450) | **4** ($280-380) | **1** ($550-750) | **4** ($150-250) |
| C5 | Environmental robustness | 0.10 | **4** (aluminum IP67) | **2** (polymer, adequate) | **4** (aluminum+GRP IP67) | **2** (ABS, basic) |
| C6 | Setup speed | 0.08 | **2** (cable runs) | **4** (wireless, tool-less) | **2** (cable + config) | **2** (cable runs) |
| C7 | Subsonic ready | 0.06 | **1** (not designed for) | **1** (not designed for) | **4** (radar integrated) | **0** (no path) |
| C8 | Dev risk & timeline | 0.08 | **4** (all proven, low risk) | **3** (MCU timing risk) | **1** (radar R&D, high risk) | **4** (simplest) |
| C9 | Multi-lane scalability | 0.05 | **4** (Ethernet, 10+ lanes) | **3** (WiFi, interference at scale) | **4** (Ethernet backbone) | **3** (Ethernet, basic SW) |
| C10 | Lifecycle cost | 0.05 | **3** (moderate spares) | **3** (battery replacement) | **2** (radar spares costly) | **3** (cheap parts, but cal cost) |

### 5.3 Weighted Scores

| Criterion | Weight | A×W | B×W | C×W | D×W |
|-----------|--------|-----|-----|-----|-----|
| C1: Accuracy | 0.18 | 0.72 | 0.54 | 0.72 | 0.18 |
| C2: Cal-free | 0.14 | 0.56 | 0.56 | 0.56 | 0.00 |
| C3: Local content | 0.14 | 0.42 | 0.42 | 0.28 | 0.56 |
| C4: Unit cost | 0.12 | 0.36 | 0.48 | 0.12 | 0.48 |
| C5: Environment | 0.10 | 0.40 | 0.20 | 0.40 | 0.20 |
| C6: Setup speed | 0.08 | 0.16 | 0.32 | 0.16 | 0.16 |
| C7: Subsonic | 0.06 | 0.06 | 0.06 | 0.24 | 0.00 |
| C8: Dev risk | 0.08 | 0.32 | 0.24 | 0.08 | 0.32 |
| C9: Scalability | 0.05 | 0.20 | 0.15 | 0.20 | 0.15 |
| C10: Lifecycle | 0.05 | 0.15 | 0.15 | 0.10 | 0.15 |
| **TOTAL** | **1.00** | **3.35** | **3.12** | **2.86** | **2.20** |
| **PERCENTAGE** | | **83.8%** | **78.0%** | **71.5%** | **55.0%** |
| **DECISION** | | **PROCEED** | **PROCEED** | **PROCEED** | **REJECT** |

### 5.4 Results Ranking

| Rank | Concept | Score | Decision | Key Strength |
|------|---------|-------|----------|-------------|
| **1** | **A: Baseline** | **83.8%** | **SELECTED** | Best accuracy + cal-free + reliability + low risk |
| 2 | B: Portable | 78.0% | FALLBACK | Best portability + lowest cost variant |
| 3 | C: Multi-Mode | 71.5% | FUTURE (Phase 2+) | Only subsonic-capable; high dev risk now |
| 4 | D: Ultra-Low-Cost | 55.0% | REJECTED | Fails accuracy MUST (C1=1), no cal-free (C2=0) |

### 5.5 Showstopper Analysis

| Concept | Any Score = 0? | Any MUST Criterion ≤ 1? | Showstopper? |
|---------|---------------|------------------------|-------------|
| A: Baseline | No | No | No |
| B: Portable | No | No (C1=3, adequate but risk) | No (monitor C1) |
| C: Multi-Mode | No | C8=1 (dev risk just tolerable) | No (but marginal) |
| **D: Ultra-Low** | **C2=0** | **C1=1 (fails ±10mm MUST)** | **YES -- REJECTED** |

### 5.6 Sensitivity Analysis

**What if we increase portability weight (C6) from 0.08 to 0.15?**

| Concept | Original | Revised | Change |
|---------|----------|---------|--------|
| A | 83.8% | 82.4% | -1.4% |
| **B** | 78.0% | **80.8%** | **+2.8%** |
| C | 71.5% | 70.4% | -1.1% |

Concept A still leads but B closes the gap. If portability becomes critical (e.g., special forces requirement), B becomes competitive.

**What if subsonic (C7) weight doubles from 0.06 to 0.12?**

| Concept | Original | Revised | Change |
|---------|----------|---------|--------|
| A | 83.8% | 82.1% | -1.7% |
| B | 78.0% | 76.3% | -1.7% |
| **C** | 71.5% | **74.8%** | **+3.3%** |

Concept C improves but A still leads. Subsonic is better addressed as Phase 2 add-on to Concept A.

---

## 6. SELECTED CONCEPT: A "BASELINE"

### 6.1 Selection Summary

```
╔═══════════════════════════════════════════════════════════════════╗
║  SELECTED CONCEPT: A -- "BASELINE"                                ║
║  VDI 2225 Score: 83.8% (PROCEED)                                 ║
║                                                                   ║
║  Calibration-free acoustic TDOA LOMAH with:                       ║
║  • 4× MEMS microphones on aluminum IP67 sensor bar               ║
║  • FPGA + ARM MCU hybrid processing                              ║
║  • Ethernet primary communication                                 ║
║  • Web-based HTML5 display (any device)                           ║
║  • Li-ion battery (10h) + 12V/mains input                        ║
║  • Calibration-free algorithm (expired Saab patent)               ║
║                                                                   ║
║  Fallback: Concept B (Portable) if portability becomes critical   ║
║  Future: Concept C (Multi-Mode) subsonic add-on in Phase 2+      ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 6.2 Key Advantages

1. **Highest accuracy** -- FPGA timing ensures ±10mm MUST requirement met
2. **Calibration-free** -- Expired patent, zero operational overhead
3. **Lowest development risk** -- All components proven (TRL 9)
4. **Good local content** -- ~62%, optimizable to ~65% in production
5. **Cost target met** -- $350-450/lane (≤$500 MUST)
6. **Ethernet reliability** -- Best for multi-lane fixed ranges
7. **Scalable architecture** -- Web-based SW supports future WiFi/mobile add-on

### 6.3 Main Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| FPGA development complexity | Medium | Medium | Use proven FPGA dev kit (Lattice iCE40 / Xilinx Artix-7); reference TDOA IP cores available |
| Calibration-free algorithm accuracy in tropical conditions | Low | High | Extensive field testing at Vietnamese ranges; algorithm is inherently temp-independent |
| MEMS sensor degradation in high humidity | Low | Medium | IP67 + conformal coating; accelerated life testing |
| Ethernet cable vulnerability in field | Medium | Low | Ruggedized CAT6 with mil-spec connectors; future WiFi add-on option |

### 6.4 Development Approach

```
PHASE 2 → PHASE 3 DEVELOPMENT PLAN FOR CONCEPT A

Month 1-3: PROTOTYPE HARDWARE
├── Select MEMS microphone (TBD-01 → evaluate SPH0641LU4H vs ICS-40730)
├── Select FPGA (Lattice iCE40UP5K or Xilinx Artix-7)
├── Design BSU PCB (4-channel analog front-end + FPGA + ARM)
├── Design power management board
└── Design aluminum enclosure (local machining)

Month 3-6: FIRMWARE DEVELOPMENT
├── Implement TDOA timing capture on FPGA
├── Implement calibration-free algorithm on ARM MCU
├── Implement BIT self-diagnostic
├── Implement Ethernet communication (TCP/IP)
└── Unit test each subsystem

Month 6-9: SOFTWARE DEVELOPMENT
├── HTML5 web dashboard (Vietnamese + English)
├── Multi-lane management (10 lanes)
├── Statistics engine (MPI, group size, salvo center)
├── Report generation (PDF export)
└── REST API for integration

Month 9-12: INTEGRATION & TEST
├── System integration (BSU + TPU + SW)
├── Accuracy validation (±10mm at 300m)
├── Environmental testing (MIL-STD-810H subset)
├── Field trial at Vietnamese military range
└── Design review → Phase 3 (Embodiment)
```

### 6.5 Preliminary Architecture (Concept A Detail)

```
BSU (Beam Sensor Unit) - IP67 Aluminum Enclosure
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  [MIC1]──→[AMP+BPF]──→┐                                   │
│                        │     ┌──────────┐   ┌──────────┐   │
│  [MIC2]──→[AMP+BPF]──→├────→│  FPGA    │──→│ ARM MCU  │   │
│                        │     │ 4ch ADC  │   │ Cal-Free │   │
│  [MIC3]──→[AMP+BPF]──→┤     │ Timestmp │   │ TDOA Alg │   │
│                        │     │ ≥1MHz/ch │   │ BIT      │   │
│  [MIC4]──→[AMP+BPF]──→┘     └──────────┘   └────┬─────┘   │
│                                                   │         │
│  [TEMP]  (for diagnostics only, not cal)          │         │
│  [ACCEL] (for vibration monitoring)               │         │
│                                                   │         │
│  ┌──────────┐    ┌──────────┐    ┌─────────┐     │         │
│  │ Li-ion   │───→│ DC-DC    │───→│ Power   │     │         │
│  │ Battery  │    │ Converter│    │ to all  │     │         │
│  │ 14.8V    │    │ 3.3V/5V  │    │ modules │     │         │
│  │ 10Ah     │    │ 12V in   │    │         │     │         │
│  └──────────┘    └──────────┘    └─────────┘     │         │
│                                                   │         │
│  ┌──────────────────────────────────────────┐     │         │
│  │ ETHERNET PHY + MAC                        │←───┘         │
│  │ 100BaseT, RJ45 (IP67 connector)          │              │
│  └──────────────────────────────────────────┘              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
         │
    CAT 5e/6 ruggedized cable
         │
    ┌────┴────────────────────────────────────────────┐
    │  RANGE SWITCH (standard PoE Ethernet switch)     │
    │  Up to 10 BSU units per switch                   │
    └────┬────────────────────────────────────────────┘
         │
    ┌────┴────────────────────────────────────────────┐
    │  CONTROL STATION (any device with web browser)   │
    │                                                  │
    │  ┌─────────────────────────────────────────┐    │
    │  │  VN-LOMAH Web Application (HTML5)        │    │
    │  │  ┌──────────┐ ┌──────────┐ ┌─────────┐ │    │
    │  │  │ Live     │ │ Lane     │ │ Reports │ │    │
    │  │  │ Scoring  │ │ Manager  │ │ & AAR   │ │    │
    │  │  │ Display  │ │ (10 ch)  │ │ Export  │ │    │
    │  │  └──────────┘ └──────────┘ └─────────┘ │    │
    │  │  ┌──────────┐ ┌──────────┐ ┌─────────┐ │    │
    │  │  │ Target   │ │ BIT      │ │ Config  │ │    │
    │  │  │ Silhouet │ │ Status   │ │ & Admin │ │    │
    │  │  │ Overlay  │ │ Monitor  │ │         │ │    │
    │  │  └──────────┘ └──────────┘ └─────────┘ │    │
    │  └─────────────────────────────────────────┘    │
    └─────────────────────────────────────────────────┘
```

### 6.6 Estimated BOM (Concept A)

| # | Component | Qty/Lane | Est. Unit Cost | Est. Total | Local % |
|---|-----------|----------|---------------|-----------|---------|
| 1 | MEMS microphone (SPH0641LU4H or equiv.) | 4 | $3 | $12 | 0% (import) |
| 2 | Analog front-end (op-amp, BPF, AGC) | 4 ch | $8 | $8 | 50% (PCB local) |
| 3 | FPGA (Lattice iCE40UP5K) | 1 | $8 | $8 | 0% (import) |
| 4 | ARM MCU (STM32H743 or equiv.) | 1 | $10 | $10 | 0% (import) |
| 5 | ADC (4-ch, 1 MSPS, 12-bit) | 1 | $6 | $6 | 0% (import) |
| 6 | Ethernet PHY + magnetics | 1 | $4 | $4 | 0% (import) |
| 7 | PCB (4-layer, 160×100mm) | 1 | $8 | $8 | 80% (local fab) |
| 8 | Li-ion battery (14.8V 10Ah) | 1 | $35 | $35 | 55% (local assembly) |
| 9 | DC-DC converters (3.3V, 5V) | 2 | $3 | $6 | 0% (import) |
| 10 | Aluminum enclosure (CNC machined) | 1 | $45 | $45 | 90% (local machining) |
| 11 | IP67 connectors (Amphenol or equiv.) | 3 | $8 | $24 | 0% (import) |
| 12 | Sensor bar (aluminum extrusion + clamps) | 1 | $30 | $30 | 85% (local fab) |
| 13 | Cable assemblies (CAT6 + power) | 1 set | $15 | $15 | 65% (local) |
| 14 | Gaskets, rubber mounts, hardware | 1 set | $8 | $8 | 90% (local rubber) |
| 15 | Assembly, test, QC labor | 1 | $25 | $25 | 100% (local) |
| 16 | Firmware/software (amortized over 500 units) | 1 | $30 | $30 | 100% (local dev) |
| 17 | Packaging (transport case) | 1 | $20 | $20 | 80% (local) |
| | **SUBTOTAL (per lane)** | | | **$294** | |
| | **Margin + contingency (25%)** | | | **$74** | |
| | **TOTAL per lane** | | | **$368** | **~63%** |

**Cost target: ≤$500 → $368 PASS (73.6% of budget)**
**Local content: ≥60% → ~63% PASS**

---

## 7. PHASE 2 GATE REVIEW

### Gate 2 Checklist

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| Function structure validated | Covers all requirements | 7 functions, all 107 req traced | PASS |
| ≥3 concepts evaluated | 3 minimum | **4 concepts** (A, B, C, D) | PASS |
| VDI 2225 ≥70% for selected | 70% | **83.8% (Concept A)** | PASS |
| No criterion score = 0 | No zeros | **No zeros for Concept A** | PASS |
| Selection rationale documented | Yes | Section 6.2-6.3 | PASS |
| Risks identified with mitigation | Yes | 4 risks with mitigations | PASS |
| Preliminary architecture | Yes | Section 6.5 | PASS |
| BOM estimate | Yes | $368/lane, 63% local | PASS |

**All gate criteria met.**

---

*Conceptual Design v1.0 | VN-TRN-001 | Selected: Concept A "Baseline" (83.8%) | Fallback: Concept B "Portable" (78.0%)*
