---
project: V-SMASH
phase: 0-2
type: reverse_engineering
version: 1.0
created: 2026-02-04
status: complete
foreign_system: SMASH 2000+
origin: Israel (Smart Shooter Ltd.)
---

# REVERSE ENGINEERING ANALYSIS
## SMASH 2000+ Fire Control System

**Document ID:** V-SMASH_RE_01
**Analysis Date:** 2026-02-04
**Reference:** [[SKILL_reverse_engineering]]
**Methodology:** D-M-I-R aligned RE process

---

## 1. SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Designation** | SMASH 2000 Plus |
| **Manufacturer** | Smart Shooter Ltd. |
| **Origin** | Israel |
| **Category** | AI-Enhanced Fire Control Optic |
| **Specimen Type** | Commercial documentation + field observation |
| **Analysis Completeness** | Level 1-2 (external + partial subsystem) |
| **Relevance** | Primary reference system for V-SMASH development |

### 1.1 System Context

```
SUPERSYSTEM: Infantry weapon platform (rifle/LMG)
     │
     ├── SYSTEM: SMASH 2000+ Fire Control
     │
     └── SIBLINGS:
         ├── TrackingPoint (USA) - Precision rifle
         ├── ARCAS (Israel) - AR/AI sight
         └── V-SMASH (Vietnam) - Indigenous development
```

### 1.2 Operational Context

| Parameter | Value |
|-----------|-------|
| **Primary Mission** | Counter-UAS, precision engagement |
| **Target Types** | Small drones, personnel, light vehicles |
| **Engagement Range** | 50-500m (caliber dependent) |
| **Environment** | Desert, temperate, maritime |
| **User** | Infantry, special operations |

---

## 2. EXTERNAL CHARACTERIZATION

### 2.1 Physical Parameters

| Parameter | Observed Value | Confidence | Method |
|-----------|----------------|------------|--------|
| Dimensions (L×W×H) | ~180 × 85 × 110 mm | High | Documentation |
| Mass (with battery) | ~1.1 kg | High | Documentation |
| Mass (without battery) | ~0.9 kg | Medium | Estimated |
| Mounting interface | Picatinny (MIL-STD-1913) | Confirmed | Visual |
| Operating voltage | 7.4V nominal (2S Li-ion) | Medium | Inferred |

### 2.2 External Features

```
┌─────────────────────────────────────────────────────────────┐
│                  SMASH 2000+ EXTERNAL VIEW                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  FRONT VIEW              TOP VIEW              SIDE VIEW     │
│  ┌─────────┐            ┌──────────────┐      ┌──────────┐  │
│  │ ◉ CMOS  │            │[PWR][MODE][0]│      │  ┌────┐  │  │
│  │         │            │              │      │  │USB │  │  │
│  ├─────────┤            │   SMASH      │      │  └────┘  │  │
│  │         │            │   2000+      │      │          │  │
│  │ OPTIC   │            │              │      │  ┌────┐  │  │
│  │ WINDOW  │            └──────────────┘      │  │TRIG│  │  │
│  │         │                                  │  └────┘  │  │
│  └─────────┘            BOTTOM VIEW           └──────────┘  │
│                         ══════════════                       │
│                         Picatinny clamp                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Interface Specifications

| Interface | Type | Purpose | Notes |
|-----------|------|---------|-------|
| Mounting | Picatinny rail | Weapon attachment | MIL-STD-1913 compliant |
| Power | Internal Li-ion | System power | Rechargeable, ~6-8 hrs |
| Data | USB-C | Configuration | Weapon profile setup |
| Trigger | Proprietary cable | Fire control | Connects to weapon trigger |
| Display | See-through optic | Aim point | Unlimited eye relief |

### 2.4 Markings & Labels

| Marking | Location | Intelligence Value |
|---------|----------|-------------------|
| "SMASH 2000+" | Housing top | Model identification |
| "Smart Shooter" | Housing side | Manufacturer confirmation |
| "Made in Israel" | Bottom plate | Origin country |
| Serial number | Bottom plate | Production tracking |
| CE marking | Side | EU compliance |
| FCC marking | Side | US RF compliance |
| Patent numbers | Documentation | IP landscape |

### 2.5 Environmental Ratings (Documented)

| Parameter | Rating | Standard |
|-----------|--------|----------|
| Operating temp | -20°C to +50°C | — |
| Storage temp | -40°C to +70°C | — |
| Sealing | IP67 (claimed) | IEC 60529 |
| Shock | Military grade (claimed) | MIL-STD-810 |
| Humidity | 95% RH | — |

---

## 3. SUBSYSTEM DECOMPOSITION

### 3.1 Major Assemblies

```
SMASH 2000+ SUBSYSTEM ARCHITECTURE
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│                    SMASH 2000+ SYSTEM                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │   SENSOR     │   │  PROCESSING  │   │   OPTICAL    │    │
│  │   MODULE     │   │    UNIT      │   │   MODULE     │    │
│  │              │   │              │   │              │    │
│  │ • CMOS cam   │──▶│ • SoC/FPGA   │──▶│ • See-thru   │    │
│  │ • IMU 6-axis │   │ • AI model   │   │   combiner   │    │
│  │ • Lens assy  │   │ • Tracker    │   │ • Reticle    │    │
│  │              │   │ • Ballistic  │   │ • LED illum  │    │
│  └──────────────┘   └──────┬───────┘   └──────────────┘    │
│         │                  │                                │
│         │           ┌──────▼───────┐                        │
│         │           │    FIRE      │                        │
│         │           │   CONTROL    │                        │
│         │           │              │                        │
│         │           │ • Trigger    │                        │
│         │           │   sensor     │                        │
│         │           │ • Gate logic │                        │
│         │           │ • Timing     │                        │
│         │           └──────┬───────┘                        │
│         │                  │                                │
│  ┌──────▼──────┐    ┌──────▼───────┐   ┌──────────────┐    │
│  │   POWER     │    │   WEAPON     │   │   USER       │    │
│  │   MODULE    │    │  INTERFACE   │   │  INTERFACE   │    │
│  │             │    │              │   │              │    │
│  │ • Li-ion    │───▶│ • Solenoid   │   │ • Buttons    │    │
│  │ • PMIC      │    │ • Cable      │   │ • Status LED │    │
│  │ • USB-C chg │    │ • Connector  │   │ • USB config │    │
│  └─────────────┘    └──────────────┘   └──────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Subsystem Specifications (Inferred)

| Subsystem | Key Components | Est. Mass | Est. Cost |
|-----------|---------------|-----------|-----------|
| Sensor Module | CMOS, IMU, lens | ~200g | $150-300 |
| Processing Unit | SoC, memory, PCB | ~100g | $200-400 |
| Optical Module | Combiner, LED, housing | ~150g | $300-500 |
| Fire Control | Trigger sensor, gate logic | ~50g | $50-100 |
| Power Module | Battery, PMIC, connector | ~200g | $50-100 |
| Weapon Interface | Solenoid, cable, mount | ~150g | $50-100 |
| Housing/Structure | Aluminum body, seals | ~250g | $200-300 |
| **TOTAL** | | **~1,100g** | **$1,000-1,800** |

*Note: Cost estimates are component cost, not retail price*

### 3.3 Energy/Material/Signal Flow

| Flow ID | Type | Source | Destination | Transformation |
|---------|------|--------|-------------|----------------|
| E1 | Electrical | Battery | PMIC | Store → Regulate |
| E2 | Electrical | PMIC | Processor | 5V/3.3V regulated |
| E3 | Electrical | PMIC | Sensor | Sensor power |
| E4 | Electrical | PMIC | Solenoid | Actuator power |
| E5 | Light | Scene | CMOS | Optical capture |
| E6 | Light | LED | Optic | Reticle illumination |
| S1 | Digital | CMOS | Processor | Image stream |
| S2 | Analog | IMU | Processor | Orientation data |
| S3 | Digital | AI model | Tracker | Detection coords |
| S4 | Digital | Tracker | Ballistic | Track state |
| S5 | Digital | Ballistic | Gate logic | Fire solution |
| S6 | Analog | Trigger sensor | Gate logic | Operator intent |
| S7 | Digital | Gate logic | Solenoid | Fire command |
| S8 | Digital | Processor | LED/optic | Display data |

---

## 4. FUNCTIONAL RECONSTRUCTION

### 4.1 Overall Function Statement

> **"Optimize weapon fire timing to maximize hit probability on moving targets while maintaining human decision authority"**

### 4.2 Function Structure Diagram

```
SMASH 2000+ FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════

OVERALL FUNCTION: Optimize fire timing for moving target engagement
                  with human-in-the-loop control

├── F1: ACQUIRE TARGET
│   ├── F1.1: Capture scene image ────────── [WP: CMOS rolling shutter]
│   ├── F1.2: Detect targets in scene ────── [WP: CNN object detection]
│   ├── F1.3: Classify target type ───────── [WP: Neural classifier]
│   └── F1.4: Estimate target range ──────── [WP: Size-based estimation]
│
├── F2: TRACK TARGET MOTION
│   ├── F2.1: Initialize track ───────────── [WP: Detection-to-track]
│   ├── F2.2: Update track state ─────────── [WP: Extended Kalman filter]
│   ├── F2.3: Predict future position ────── [WP: Motion extrapolation]
│   └── F2.4: Handle track loss ──────────── [WP: Re-acquisition logic]
│
├── F3: COMPUTE FIRE SOLUTION
│   ├── F3.1: Sense weapon orientation ───── [WP: MEMS IMU 6-axis]
│   ├── F3.2: Retrieve weapon profile ────── [WP: EEPROM lookup]
│   ├── F3.3: Calculate projectile path ──── [WP: Point-mass 3DOF model]
│   └── F3.4: Determine alignment error ──── [WP: Vector subtraction]
│
├── F4: CONTROL FIRE AUTHORIZATION
│   ├── F4.1: Sense trigger pressure ─────── [WP: Force/switch sensor]
│   ├── F4.2: Evaluate hit probability ───── [WP: Threshold comparison]
│   ├── F4.3: Gate fire authorization ────── [WP: Boolean AND logic]
│   └── F4.4: Time trigger release ───────── [WP: Precision timer <5ms]
│
├── F5: ACTUATE TRIGGER MECHANISM
│   ├── F5.1: Hold trigger (gate closed) ─── [WP: Solenoid energized]
│   ├── F5.2: Release trigger (gate open) ── [WP: Solenoid de-energized]
│   └── F5.3: Detect fire event ──────────── [WP: Recoil/acoustic sense]
│
├── F6: PROVIDE OPERATOR FEEDBACK
│   ├── F6.1: Display dynamic aim point ──── [WP: See-through reflex]
│   ├── F6.2: Indicate target lock ───────── [WP: Reticle color change]
│   ├── F6.3: Show fire readiness ────────── [WP: Symbol/color change]
│   └── F6.4: Display system status ──────── [WP: Status LEDs]
│
└── F_AUX: AUXILIARY FUNCTIONS
    ├── F_AUX.1: Manage power ────────────── [WP: PMIC + Li-ion]
    ├── F_AUX.2: Store weapon profiles ───── [WP: Non-volatile memory]
    ├── F_AUX.3: Enable configuration ────── [WP: USB + mobile app]
    ├── F_AUX.4: Update firmware ─────────── [WP: USB bootloader]
    └── F_AUX.5: Fail-safe to manual ─────── [WP: Mechanical bypass]
```

### 4.3 Working Principle Catalog

| ID | Subfunction | Physical Effect | Form Design | Working Principle |
|----|-------------|-----------------|-------------|-------------------|
| WP-01 | F1.1 Image capture | Photoelectric effect | CMOS pixel array | Rolling shutter sensor |
| WP-02 | F1.2 Target detection | Pattern matching | CNN weight matrix | YOLO-type inference |
| WP-03 | F1.3 Classification | Statistical learning | Softmax output | Neural network classifier |
| WP-04 | F1.4 Range estimation | Geometric similarity | Known target size | Size-distance relationship |
| WP-05 | F2.2 Track update | Recursive estimation | State-space model | Extended Kalman filter |
| WP-06 | F2.3 Position prediction | Linear/polynomial fit | Extrapolation | Constant velocity model |
| WP-07 | F3.1 Orientation sense | Coriolis + acceleration | MEMS structure | 6-axis IMU |
| WP-08 | F3.3 Trajectory calc | Newtonian mechanics | Numerical integration | Point-mass ballistic model |
| WP-09 | F4.1 Trigger sense | Resistive/piezo | Force transducer | Force-sensitive resistor |
| WP-10 | F4.4 Timing control | Digital counter | FPGA/timer IC | Precision timer |
| WP-11 | F5.1/5.2 Trigger actuation | Electromagnetic | Solenoid coil | Push-pull solenoid |
| WP-12 | F6.1 Aim display | Light reflection | Beam combiner | Reflex sight optics |

### 4.4 Subfunction Classification

| Type | Count | Examples |
|------|-------|----------|
| SENSE | 5 | F1.1, F3.1, F4.1, F5.3 |
| PROCESS | 10 | F1.2, F1.3, F2.2, F3.3, F4.2 |
| DECIDE | 3 | F2.4, F4.3 |
| ACTUATE | 2 | F5.1, F5.2 |
| CONVERT | 4 | F6.1, F6.2, F6.3, F6.4 |
| **TOTAL** | **24** | |

---

## 5. PERFORMANCE ESTIMATION

### 5.1 Derived Specifications

| Parameter | Estimated Value | Confidence | Derivation Method |
|-----------|----------------|------------|-------------------|
| Detection range (drone) | 300-500m | Medium | Marketing + physics |
| Detection range (person) | 500-800m | Medium | Marketing + physics |
| Detection accuracy | >90% | Medium | Industry benchmark |
| Tracking speed | Up to 50 m/s | Medium | Drone speed capability |
| Fire solution latency | <100ms | Medium | Real-time requirement |
| Trigger timing precision | <5ms | High | Critical for accuracy |
| Hit improvement | 3-5x | Medium | Marketing claims |
| First-round Pk | 50-70% @ 200m | Low | Estimated from claims |

### 5.2 Validation Requirements

| Specification | Validation Method | Priority |
|---------------|-------------------|----------|
| Detection accuracy | Field test with known targets | High |
| Tracking performance | High-speed moving target test | High |
| Trigger timing | High-speed camera measurement | High |
| Hit improvement | Controlled firing trial | Critical |
| Environmental rating | MIL-STD-810H chamber test | Medium |

---

## 6. DESIGN PHILOSOPHY ASSESSMENT

### 6.1 Paradigm Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| Safety margins | Human-in-loop mandatory, fail-safe | 5 | Safety paramount |
| Modularity | Integrated unit, limited field service | 2 | Factory service model |
| Material selection | Quality aluminum, premium finish | 4 | Performance priority |
| Redundancy | Fail-safe to manual, no sensor redundancy | 3 | Critical path protected |
| Manufacturing | Precision assembly, tight tolerances | 4 | Low-medium volume |
| Complexity | Sophisticated but focused | 4 | Single-purpose excellence |

### 6.2 Designer's Paradigm Statement

> **"Maximize hit probability through AI-assisted fire timing while ensuring absolute human control over lethal decisions and graceful degradation to manual operation if system fails."**

### 6.3 Trade-off Analysis

| Trade-off | Prioritized | Over | Evidence |
|-----------|-------------|------|----------|
| 1 | **Accuracy** | Weight | Complex optics, processing hardware |
| 2 | **Safety** | Speed | Mandatory human trigger initiation |
| 3 | **Reliability** | Cost | Quality components, IP67 sealing |
| 4 | **Simplicity** | Features | Single-purpose, focused design |
| 5 | **Performance** | Field service | Integrated design, factory calibration |

### 6.4 Paradigm Applicability Assessment

| Aspect | SMASH Paradigm | V-SMASH Context | Match | Action |
|--------|---------------|-----------------|-------|--------|
| Human-in-loop | Mandatory | Required by policy | ✅ | Adopt exactly |
| Fail-safe | To manual | Required | ✅ | Adopt exactly |
| Factory service | Acceptable (Israel) | Need field service | ⚠️ | Adapt design |
| Premium materials | Cost acceptable | Cost constrained | ⚠️ | Select alternatives |
| Single-purpose | Acceptable | Multi-platform desired | ⚠️ | Modular design |
| IP67 sealing | Standard | Required | ✅ | Adopt standard |

---

## 7. APPLICATION RECOMMENDATIONS

### 7.1 Replication Feasibility Assessment

| Function | SMASH Solution | Local Alternative | Feasibility | Notes |
|----------|---------------|-------------------|-------------|-------|
| F1.1 Image | Sony CMOS | Sony IMX290/462 | ✅ High | Available via distribution |
| F1.2 Detection | Proprietary CNN | YOLOv8-nano | ✅ High | Open-source, trainable |
| F2.2 Tracking | Kalman (presumed) | OpenCV Kalman | ✅ High | Standard algorithm |
| F3.1 IMU | Quality MEMS | BMI160/BMI270 | ✅ High | Available, adequate |
| F3.3 Ballistics | Proprietary | Point-mass model | ✅ High | Physics-based |
| F4.4 Timing | FPGA/ASIC | MCU timer | ✅ High | <5ms achievable |
| F5.1/5.2 Solenoid | Custom | Standard 12V | ✅ High | Available |
| F6.1 Optics | Custom design | **Local development** | ⚠️ Medium | Requires optical expertise |
| F_AUX.1 Power | Quality PMIC | TI/Analog Devices | ✅ High | Available |

**Overall Replication Feasibility: 85%**

### 7.2 Technology Insertion Candidates

| Priority | Technology | Source | Insert Into V-SMASH | Rationale |
|----------|------------|--------|---------------------|-----------|
| 1 | CNN detection (YOLO) | Open-source | ✅ Yes | Proven, adaptable |
| 2 | Kalman tracking | Standard algorithm | ✅ Yes | Well-documented |
| 3 | Point-mass ballistics | Physics | ✅ Yes | Validate locally |
| 4 | Human-in-loop paradigm | SMASH philosophy | ✅ Yes | Critical safety |
| 5 | Fail-safe mechanism | SMASH concept | ✅ Yes | Combat reliability |
| 6 | Reflex optic concept | SMASH form | ⚠️ Partial | Adapt for local mfg |

### 7.3 Counter-System Analysis

| SMASH Vulnerability | Counter Approach | Difficulty |
|---------------------|------------------|------------|
| Visual sensor (CMOS) | Smoke, obscurants, dazzle | Low |
| AI model limitations | Decoys, unusual profiles | Medium |
| Single sensor | Multi-spectral countermeasures | Medium |
| Electronic trigger | EMP/EMI attack | High |
| Battery dependency | Prolonged engagement exhaustion | Low |
| GPS (if used for ballistics) | GPS jamming | Medium |

### 7.4 Improvement Opportunities for V-SMASH

| Area | SMASH Limitation | V-SMASH Opportunity |
|------|------------------|---------------------|
| **Night capability** | CMOS only (poor low-light) | Add thermal sensor (PRO) |
| **Field service** | Factory return required | Design for field repair |
| **Cost** | ~$18,000 retail | Target $3,000-5,000 |
| **Local content** | 0% (import only) | 60-70% local |
| **Multi-platform** | Rifle-focused | Rifle + RCWS + vehicle |
| **Maneuvering targets** | Basic tracking | IMM filter for evasive |

---

## 8. LESSONS LEARNED

### 8.1 RE Process Observations

| Observation | Implication |
|-------------|-------------|
| Limited physical access | Much inferred from documentation |
| Proprietary components | Working principles identified, not exact parts |
| Marketing vs. reality | Performance claims need validation |
| Paradigm clarity | Design philosophy well-communicated |

### 8.2 Capability Gaps Identified

| Gap | Training/Development Need |
|-----|---------------------------|
| Optical design | Need expertise in reflex sight optics |
| AI model training | Need labeled dataset for Vietnamese context |
| Trigger mechanism | Need precision timing validation capability |
| Environmental testing | Need MIL-STD-810H test chamber access |

### 8.3 Process Improvements for Future RE

| Improvement | Action |
|-------------|--------|
| Physical specimen access | Seek procurement or captured sample |
| Component identification | Develop spectrometry/X-ray capability |
| Performance validation | Establish field test protocols |
| Documentation template | Use this report as template |

---

## 9. CROSS-REFERENCE TO V-SMASH

### 9.1 Function Structure Alignment

| SMASH Function | V-SMASH Equivalent | Status |
|----------------|-------------------|--------|
| F1: Acquire target | F1: Acquire target | ✅ Aligned |
| F2: Track target | F2: Track target | ✅ Aligned |
| F3: Compute fire solution | F3: Compute fire solution | ✅ Aligned |
| F4: Control fire auth | F4: Control fire auth | ✅ Aligned |
| F5: Actuate trigger | F5: Actuate trigger | ✅ Aligned |
| F6: Operator feedback | F6: Operator feedback | ✅ Aligned |
| F_AUX: Support | F_AUX: Support | ✅ Aligned |

**Conclusion:** V-SMASH function structure is validated by SMASH RE analysis.

### 9.2 Working Principle Comparison

| Function | SMASH WP | V-SMASH WP | Match |
|----------|----------|------------|-------|
| Detection | CNN (proprietary) | YOLOv8-nano | Equivalent |
| Tracking | Kalman (presumed) | Kalman/IMM | Enhanced |
| Ballistics | Point-mass | Point-mass 3DOF | Equivalent |
| Trigger | Solenoid | Solenoid | Equivalent |
| IMU | 6-axis MEMS | BMI160 6-axis | Equivalent |
| Optics | Custom reflex | Local design | Adapted |

### 9.3 V-SMASH Differentiation Summary

| Differentiator | SMASH | V-SMASH LITE | V-SMASH PRO |
|----------------|-------|--------------|-------------|
| Price | $18,000 | $3,000 | $5,000 |
| Night capability | None | NV clip-on | Integrated thermal |
| Local content | 0% | 70% | 31% |
| Field service | Factory | Field-level | Field-level |
| Tracking | Basic | Basic | IMM (3g maneuver) |
| Sealing | IP67 | IP65 | IP67 |

---

## 10. APPROVAL & DISTRIBUTION

### Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-04 | Design Team | Initial RE analysis |

### Distribution List

| Recipient | Purpose |
|-----------|---------|
| V-SMASH Design Team | Reference for design decisions |
| Program Office | Competitive analysis |
| Manufacturing | Local content planning |

---

## APPENDIX A: REFERENCE MATERIALS

### A.1 Source Documents

| Source | Type | Reliability |
|--------|------|-------------|
| Smart Shooter website | Marketing | Medium |
| Product brochures | Technical summary | Medium |
| Trade show observations | Physical examination | High |
| Patent filings | Technical detail | High |
| News articles | Context | Low |

### A.2 Related V-SMASH Documents

- [[V-SMASH_00_project_brief|Project Brief]]
- [[V-SMASH_P0_01_ODI_analysis|ODI Analysis]]
- [[V-SMASH_P2_01_function_structure|Function Structure]]
- [[V-SMASH_P2_04_conceptual_design_v1_1|Conceptual Design]]
- [[V-SMASH_P2_05_product_variants_spec|Product Variants Spec]]

### A.3 RE Methodology Reference

- [[SKILL_reverse_engineering|RE Skill]]
- [[Reverse Engineering Foreign Military Systems|RE Reference Guide]]

---

*This document was generated using the Engineering Design System reverse engineering methodology (D-M-I-R aligned). It serves as competitive intelligence and design validation for the V-SMASH indigenous fire control development program.*
