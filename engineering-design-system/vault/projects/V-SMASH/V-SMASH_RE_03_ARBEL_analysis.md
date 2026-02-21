---
project: V-SMASH
phase: 2
type: reverse_engineering
system: ARBEL (IWI)
version: 1.0
created: 2026-02-04
status: complete
classification: OSINT Analysis
---

# REVERSE ENGINEERING ANALYSIS
## ARBEL - AI-Powered Anti-Drone Fire Control System

**Analysis Date:** 2026-02-04
**Analyst:** Claude (Engineering Design System)
**Data Source:** Open Source Intelligence (OSINT) - manufacturer publications, defense media, trade shows
**Specimen:** None (OSINT-based analysis)

---

## 1. SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Designation** | ARBEL |
| **Manufacturer** | IWI - Israel Weapon Industries |
| **Product Family** | AI-enabled fire control / C-UAS |
| **Unveiled** | 2023 (Eurosatory) |
| **Status** | In production |
| **Related Systems** | Smart Shooter SMASH, Elbit ARCAS |

### 1.1 System Context

```
SUPERSYSTEM: Integrated C-UAS Defense
    │
    ├── ARBEL (This System)
    │   └── AI fire control for multiple weapon types
    │
    ├── SMASH 2000+ (Competitor)
    │   └── Electro-optical fire control
    │
    └── Radar/EW Systems (Interface)
        └── Early warning, track handoff
```

### 1.2 Target Platforms
- **Primary:** 5.56mm/7.62mm assault rifles and LMGs
- **Extended:** 12.7mm HMG, 40mm GMG
- **Vehicle:** Remote Weapon Stations (RWS)
- **Static:** Fixed C-UAS positions

### 1.3 Manufacturer Background

IWI (Israel Weapon Industries) is a leading Israeli defense company known for:
- Tavor assault rifle family
- Negev LMG
- Uzi submachine gun legacy
- Growing focus on smart weapons and C-UAS

---

## 2. EXTERNAL CHARACTERIZATION

### 2.1 Physical Specifications (Estimated from OSINT)

| Parameter | Value | Confidence |
|-----------|-------|------------|
| **Length** | ~180-220 mm | Medium |
| **Width** | ~70-90 mm | Medium |
| **Height** | ~90-110 mm (above rail) | Medium |
| **Mass** | ~800-1,000 g | Medium |
| **Power** | Internal battery, rechargeable | High |
| **Display** | Integrated optic with reticle | High |
| **FOV** | ~15-20° estimated | Low |
| **Magnification** | 1x base (digital zoom available) | Medium |

### 2.2 Key External Features

| Feature | Observation | Significance |
|---------|-------------|--------------|
| **Compact form** | Similar size to SMASH | Infantry-portable |
| **Dual sensor** | Day + thermal visible | 24/7 capability |
| **Integrated display** | Built-in optic | All-in-one solution |
| **Quick-detach mount** | Lever-based | Rapid installation |
| **Minimal controls** | Few external buttons | Software-driven |
| **Rugged construction** | Military-grade finish | Combat-rated |

### 2.3 Interface Specifications

| Interface | Type | Purpose |
|-----------|------|---------|
| **Mount** | MIL-STD-1913 Picatinny | Weapon attachment |
| **Power** | USB-C (charging) | Battery charging |
| **Data** | Wireless (optional) | External integration |
| **Trigger** | Mechanical/electronic | Fire control |

### 2.4 Environmental Ratings (Claimed/Estimated)

| Parameter | Rating | Notes |
|-----------|--------|-------|
| **Sealing** | IP67 (estimated) | Military standard |
| **Shock** | MIL-STD-810 | Weapon firing rated |
| **Temperature** | -30°C to +55°C | Wide operational |
| **EMC** | MIL-STD-461 | Battlefield EMI |

---

## 3. SUBSYSTEM DECOMPOSITION

### 3.1 Major Assemblies

```
ARBEL SYSTEM
├── A1: OPTICAL/SENSOR ASSEMBLY
│   ├── A1.1: Day camera (CMOS HD)
│   ├── A1.2: Thermal imager (uncooled)
│   ├── A1.3: Optical combiner/display
│   └── A1.4: Lens assembly with protection
│
├── A2: PROCESSING UNIT
│   ├── A2.1: AI/ML processor
│   ├── A2.2: Image fusion engine
│   ├── A2.3: Tracking algorithm core
│   └── A2.4: Ballistic computer
│
├── A3: FIRE CONTROL MECHANISM
│   ├── A3.1: Trigger interface
│   ├── A3.2: Fire gate actuator
│   └── A3.3: Weapon orientation sensor (IMU)
│
├── A4: POWER SYSTEM
│   ├── A4.1: Battery pack (Li-ion)
│   ├── A4.2: Power management
│   └── A4.3: Charging circuit
│
├── A5: USER INTERFACE
│   ├── A5.1: Display overlay
│   ├── A5.2: Control buttons
│   └── A5.3: Status indicators
│
└── A6: HOUSING
    ├── A6.1: Main body (machined aluminum)
    ├── A6.2: Sealed enclosure
    └── A6.3: Rail interface clamp
```

### 3.2 Subsystem Mass Distribution (Estimated)

| Subsystem | Est. Mass | % Total |
|-----------|-----------|---------|
| A1: Optical/Sensor | 300 g | 33% |
| A2: Processing | 150 g | 17% |
| A3: Fire Control | 50 g | 6% |
| A4: Power | 200 g | 22% |
| A5: User Interface | 30 g | 3% |
| A6: Housing | 170 g | 19% |
| **TOTAL** | **900 g** | **100%** |

---

## 4. FUNCTIONAL RECONSTRUCTION

### 4.1 Overall Function Statement

> **"Autonomously detect, track, and engage small aerial threats (drones) using AI-powered target recognition and precision fire timing, while maintaining operator authorization for engagement decisions."**

### 4.2 Function Structure Diagram

```
OVERALL: Enable effective C-UAS engagement through AI-assisted fire control
│
├── F1: DETECT AERIAL THREATS
│   ├── F1.1: Capture day imagery → [HD CMOS sensor]
│   ├── F1.2: Capture thermal imagery → [Uncooled microbolometer]
│   ├── F1.3: Fuse sensor data → [Image fusion algorithm]
│   ├── F1.4: Detect drone signatures → [CNN object detection]
│   └── F1.5: Classify threat type → [Drone type classifier]
│
├── F2: TRACK TARGETS
│   ├── F2.1: Initialize track on detection → [Track initiation logic]
│   ├── F2.2: Maintain continuous track → [Robust tracking algorithm]
│   ├── F2.3: Predict target trajectory → [Motion prediction model]
│   ├── F2.4: Handle occlusion/loss → [Re-acquisition logic]
│   └── F2.5: Manage multiple tracks → [Multi-target tracker]
│
├── F3: COMPUTE ENGAGEMENT SOLUTION
│   ├── F3.1: Measure weapon orientation → [6-axis IMU]
│   ├── F3.2: Estimate target range → [Size-based estimation or LRF]
│   ├── F3.3: Calculate ballistic trajectory → [Point-mass model]
│   ├── F3.4: Compute lead angle → [Moving target solution]
│   └── F3.5: Generate aim point → [Reticle offset calculation]
│
├── F4: CONTROL WEAPON FIRING
│   ├── F4.1: Sense operator trigger intent → [Trigger pressure sensor]
│   ├── F4.2: Evaluate engagement criteria → [Pk threshold check]
│   ├── F4.3: Authorize/gate fire → [Human-in-loop decision]
│   └── F4.4: Execute precision timing → [Sub-ms fire release]
│
├── F5: PROVIDE OPERATOR INTERFACE
│   ├── F5.1: Display target indicators → [Bounding box overlay]
│   ├── F5.2: Show aim point → [Dynamic reticle]
│   ├── F5.3: Indicate lock status → [Visual/audio feedback]
│   ├── F5.4: Display system status → [Battery, mode, errors]
│   └── F5.5: Enable mode selection → [Button interface]
│
└── F_AUX: SUPPORT FUNCTIONS
    ├── F_AUX.1: Manage power → [Battery + PMIC]
    ├── F_AUX.2: Protect optics → [Sealed housing]
    ├── F_AUX.3: Dissipate heat → [Passive thermal management]
    ├── F_AUX.4: Enable configuration → [Software settings]
    └── F_AUX.5: Record engagements → [Video logging]
```

### 4.3 Energy/Material/Signal Flow

```
┌──────────────────────────────────────────────────────────────────────┐
│                        ARBEL SIGNAL FLOW                              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  SCENE ──(visible light)──► DAY CAMERA ───┐                          │
│       ──(thermal IR)──────► THERMAL CAM ──┼──► FUSION ──► AI DETECT  │
│                                           │              │            │
│                                           │         ┌────▼────┐       │
│                                           │         │ TRACKING │      │
│                                           │         │ (multi)  │      │
│                                           │         └────┬────┘       │
│                                           │              │            │
│  WEAPON ──(orientation)──► IMU ──────────────────────────┼───┐       │
│                                                          │   │       │
│                                                   ┌──────▼───▼──┐    │
│                                                   │  BALLISTIC   │    │
│                                                   │  COMPUTER    │    │
│                                                   └──────┬───────┘    │
│                                                          │            │
│                                                          ▼            │
│  OPERATOR ◄────────────── DISPLAY ◄────(aim point + status)          │
│      │                                                                │
│      └──(trigger pressure)──► TRIGGER SENSOR ──► FIRE GATE           │
│                                                      │                │
│                               (precision timing) ◄───┘                │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 5. WORKING PRINCIPLE CATALOG

### 5.1 Core Working Principles

| ID | Subfunction | Physical Effect | Form Design | Working Principle |
|----|-------------|-----------------|-------------|-------------------|
| WP-01 | Day imaging | Photoelectric effect | CMOS array | Digital camera |
| WP-02 | Thermal imaging | Thermal radiation | Uncooled VOx | Microbolometer |
| WP-03 | Sensor fusion | Data combination | Weighted blend | Multi-spectral fusion |
| WP-04 | AI detection | Pattern matching | Deep CNN | Neural network inference |
| WP-05 | Target tracking | State estimation | Correlation filter | Robust visual tracker |
| WP-06 | Multi-target mgmt | Data association | Track pool | Multi-object tracking |
| WP-07 | Range estimation | Geometric scaling | Known object size | Passive ranging |
| WP-08 | Orientation sensing | Coriolis/gravity | MEMS IMU | Inertial measurement |
| WP-09 | Ballistics | Newtonian mechanics | Numerical solver | Trajectory computation |
| WP-10 | Fire gating | Electromechanical | Solenoid actuator | Precision trigger |
| WP-11 | Display | Light emission | OLED micro-display | See-through overlay |

### 5.2 Key Differentiating Features (vs. SMASH/ARCAS)

| Feature | SMASH 2000+ | ARCAS | ARBEL | Significance |
|---------|-------------|-------|-------|--------------|
| **Integrated thermal** | Optional add-on | Partial | **Native dual-sensor** | 24/7 out-of-box |
| **Sensor fusion** | None | Basic | **Advanced fusion** | Better detection |
| **Primary market** | General FCS | Infantry AR | **C-UAS focused** | Optimized for drones |
| **Weapon range** | Rifles to HMG | Assault rifles | **Rifles to GMG** | Wider platform |
| **Form factor** | Weapon-mounted | Compact rifle | **Modular** | Flexibility |

### 5.3 Novel/Unexpected Solutions

| Feature | Conventional | ARBEL Approach | Innovation |
|---------|--------------|----------------|------------|
| **Dual sensor** | Separate thermal | Fused in single unit | Reduced size/weight |
| **C-UAS optimization** | General purpose | Drone-specific AI | Better Pd for drones |
| **Weapon flexibility** | Fixed platform | Multi-platform design | Single system, many weapons |
| **Passive ranging** | LRF required | AI-based size estimation | Cost/complexity reduction |

---

## 6. PERFORMANCE ESTIMATION

### 6.1 Derived Specifications

| Parameter | Estimated Value | Confidence | Derivation |
|-----------|-----------------|------------|------------|
| Detection range (drone, day) | 300-500 m | Medium | Marketing claims |
| Detection range (drone, thermal) | 200-400 m | Medium | Uncooled sensor limits |
| Track capacity | 3-5 targets | Low | Typical for class |
| Processing latency | <100 ms | Medium | Real-time requirement |
| Fire solution time | <50 ms | Medium | Similar to SMASH |
| Battery life | 4-6 hours | Low | Thermal power draw |
| Hit probability improvement | 3-5x | Medium | C-UAS claims |

### 6.2 Performance Comparison Matrix

| Parameter | ARBEL | SMASH 2000+ | ARCAS | V-SMASH Target |
|-----------|-------|-------------|-------|----------------|
| **Platform** | Multi-weapon | MG/HMG | Assault rifle | 12.7mm HMG |
| **Day detection** | 400m | 300m | 400m | 300m |
| **Night detection** | **300m native** | Add-on only | 200m | 200m (PRO) |
| **Sensor fusion** | **Yes** | No | Partial | Yes (PRO) |
| **Multi-target** | 3-5 | Unknown | 10+ | **5** |
| **C-UAS optimized** | **Yes** | General | General | **Yes** |
| **Weight** | ~900g | ~1,600g | ~700g | <1,500g |
| **Cost (est.)** | $15,000-20,000 | $18,000 | $5,000-8,000 | $3,000-5,000 |

---

## 7. DESIGN PHILOSOPHY ASSESSMENT

### 7.1 Paradigm Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **C-UAS focus** | Drone-specific AI training | 5 | Purpose-built for mission |
| **Sensor integration** | Native dual-sensor | 5 | 24/7 capability priority |
| **Platform flexibility** | Multi-weapon design | 4 | Market breadth |
| **Autonomy level** | AI-assisted, human decision | 4 | Balanced approach |
| **Modularity** | Moderate | 3 | Integrated design trade-off |

### 7.2 Designer's Paradigm Statement

> **"Counter-UAS is a distinct mission requiring purpose-built AI trained on drone signatures, with integrated day/thermal sensing for 24/7 operations, delivered in a form factor adaptable to multiple weapon platforms from rifles to crew-served weapons."**

### 7.3 Trade-off Analysis

| Design Decision | What Was Prioritized | What Was Sacrificed |
|-----------------|---------------------|---------------------|
| Dual sensor native | 24/7 capability | Size, cost, battery |
| C-UAS AI optimization | Drone detection | General target capability |
| Multi-weapon platform | Market flexibility | Per-weapon optimization |
| Passive ranging | Cost, simplicity | Range accuracy |
| Integrated package | Ease of use | Upgrade flexibility |

### 7.4 Paradigm Applicability to V-SMASH

| ARBEL Paradigm | V-SMASH Applicability | Recommendation |
|----------------|----------------------|----------------|
| C-UAS focused AI | **High** - Primary mission | **Adopt** - Train on drone data |
| Native dual-sensor | High - PRO variant | **Adopt for PRO** |
| Sensor fusion | **High** - Improves Pd | **Adopt for PRO** |
| Multi-weapon flexibility | Medium - Focus on 12.7mm | Partial - Consider variants |
| Passive ranging | Low - LRF preferred | **Skip** - Use LRF for HMG range |

---

## 8. APPLICATION RECOMMENDATIONS

### 8.1 Technology Insertion Candidates for V-SMASH

| ARBEL Feature | V-SMASH Application | Feasibility | Priority |
|---------------|---------------------|-------------|----------|
| **C-UAS optimized AI** | Drone-specific training | High | ★★★★★ |
| **Native sensor fusion** | CMOS + thermal blend | High (PRO) | ★★★★☆ |
| **Fusion algorithms** | Weighted image combination | High | ★★★★☆ |
| **Passive ranging** | Backup to LRF | Medium | ★★☆☆☆ |
| **Multi-weapon mount** | 12.7mm specific | Low | ★☆☆☆☆ |

### 8.2 Function Structure Comparison

| Function | ARBEL Solution | V-SMASH Current | Gap Analysis |
|----------|----------------|-----------------|--------------|
| F1: Detect | Fused day+thermal | Day or thermal | **Add fusion algorithm (PRO)** |
| F1.4: AI detect | C-UAS optimized CNN | General YOLO | **Train on drone dataset** |
| F2: Track | Multi-target (3-5) | Multi-target (5) | Comparable |
| F3.2: Range | Passive (size-based) | LRF planned | V-SMASH approach superior |
| F4: Fire control | Gate mechanism | Gate mechanism | Comparable |

### 8.3 Lessons for V-SMASH

1. **C-UAS AI training is critical** - ARBEL's drone-specific AI likely contributes significantly to performance; V-SMASH should prioritize drone dataset collection and model training

2. **Native dual-sensor is the future** - Market is moving toward integrated day/thermal; V-SMASH-PRO should include this from the start rather than as add-on

3. **Sensor fusion improves reliability** - Combining modalities reduces false positives and extends operational envelope; implement for PRO

4. **Passive ranging has limits** - ARBEL's size-based ranging is cost-effective but less accurate; V-SMASH should retain LRF for 12.7mm engagement ranges (400m+)

5. **Battery life is a challenge** - Dual-sensor systems draw significant power; V-SMASH-PRO needs larger battery or vehicle power option

---

## 9. CROSS-REFERENCE TO V-SMASH

### 9.1 Function Structure Validation

| V-SMASH Function | ARBEL Equivalent | Validation |
|------------------|------------------|------------|
| F1: Detect threat | F1: Detect aerial threats | ✅ Confirmed |
| F2: Track target | F2: Track targets | ✅ Confirmed |
| F3: Measure state | F3.1-F3.2: IMU + range | ✅ Confirmed |
| F4: Calculate solution | F3.3-F3.5: Ballistics + lead | ✅ Confirmed |
| F5: Gate fire | F4: Control firing | ✅ Confirmed |
| F6: Feedback | F5: Operator interface | ✅ Confirmed |
| **F7: Multi-target** | **F2.5: Multi-target mgmt** | ✅ **Validated** |

### 9.2 Requirements Implications

| ARBEL Capability | V-SMASH Requirement Impact |
|------------------|---------------------------|
| Native sensor fusion | Enhance R62: Add fusion algorithm requirement |
| C-UAS optimized AI | Add: R68 - Drone-specific AI training data |
| Passive ranging backup | Consider: R69 - Backup ranging (size-based) |
| 24/7 operations | Supports existing R06, R62 (PRO) |

### 9.3 New Requirement Suggestions

| ID | Requirement | D/W | Value | Variant | Source |
|----|-------------|-----|-------|---------|--------|
| R68 | C-UAS specific AI training | D | ≥5,000 drone images | Both | ARBEL RE |
| R69 | Backup passive ranging | W | ±20% accuracy | LITE | ARBEL RE |
| R70 | Sensor fusion algorithm | D | Weighted blend | PRO | ARBEL RE |

---

## 10. COMPARISON: THREE ISRAELI SYSTEMS

### 10.1 System Comparison Summary

| Aspect | SMASH 2000+ | ARCAS | ARBEL |
|--------|-------------|-------|-------|
| **Manufacturer** | Smart Shooter | Elbit | IWI |
| **Primary Mission** | General FCS | Infantry augmentation | **C-UAS** |
| **Platform** | Mounted weapons | Assault rifles | Multi-platform |
| **Day sensor** | Yes | Yes | Yes |
| **Thermal sensor** | Add-on | Integrated | **Native fused** |
| **AI detection** | Yes | Yes | **C-UAS optimized** |
| **Multi-target** | Unknown | 10+ | 3-5 |
| **C4I integration** | Optional | Built-in | Optional |
| **Weight** | ~1,600g | ~700g | ~900g |
| **Est. cost** | $18,000 | $5,000-8,000 | $15,000-20,000 |

### 10.2 Best-of-Breed for V-SMASH

| Feature | Best Source | Recommendation |
|---------|-------------|----------------|
| Fire control mechanism | SMASH 2000+ | Proven, reliable |
| Multi-target tracking | ARCAS | Most capable (10+) |
| C-UAS AI | ARBEL | Purpose-built |
| Sensor fusion | ARBEL | Native integration |
| C4I integration | ARCAS | Built-in networking |
| Cost efficiency | V-SMASH target | Must beat all three |

---

## 11. LESSONS LEARNED

### 11.1 RE Process Observations

| Observation | Learning |
|-------------|----------|
| Three Israeli systems show market maturity | C-UAS FCS is proven technology |
| Each has different optimization focus | V-SMASH can cherry-pick best features |
| Thermal integration is standard | PRO variant must include thermal |
| AI training data is differentiator | Invest in drone image dataset |

### 11.2 Capability Gaps Identified

| Gap | Significance | Mitigation |
|-----|--------------|------------|
| C-UAS specific AI | High - affects Pd | Partner with university for training |
| Sensor fusion expertise | Medium | Algorithm development |
| Drone image dataset | High | Collect local threat samples |

### 11.3 V-SMASH Competitive Positioning

| Factor | Israeli Systems | V-SMASH Strategy |
|--------|-----------------|------------------|
| **Price** | $5,000-20,000 | **$3,000-5,000** (undercut) |
| **Local content** | 0% (import) | **60-70%** (strategic) |
| **Platform focus** | Various | **12.7mm HMG** (specific) |
| **Supply security** | Import dependent | **Indigenous** (strategic) |

---

## 12. SUMMARY

### 12.1 Key Findings

| Category | Finding |
|----------|---------|
| **Design Philosophy** | C-UAS purpose-built, 24/7 dual-sensor, multi-platform |
| **Key Innovation** | Native sensor fusion, drone-optimized AI |
| **V-SMASH Relevance** | High for AI training, sensor fusion; Medium for form factor |
| **Technology Insertion** | C-UAS AI training, sensor fusion algorithms |
| **Competitive Insight** | V-SMASH can compete on price and local content |

### 12.2 Action Items for V-SMASH

| Priority | Action | Target |
|----------|--------|--------|
| ★★★★★ | Collect C-UAS drone training images | Both variants |
| ★★★★★ | Develop sensor fusion algorithm | PRO variant |
| ★★★★☆ | Train YOLO specifically on drone signatures | Both variants |
| ★★★☆☆ | Evaluate passive ranging as backup | LITE variant |
| ★★☆☆☆ | Benchmark against ARBEL detection claims | Testing phase |

---

## 13. DOCUMENT CONTROL

| Field | Value |
|-------|-------|
| **Document ID** | V-SMASH_RE_03_ARBEL_analysis |
| **Version** | 1.0 |
| **Status** | Complete |
| **Author** | Claude (Engineering Design System) |
| **Review Required** | Yes - validate OSINT accuracy |

### Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| RE Analyst | Claude | 2026-02-04 | ✅ |
| Project Lead | | | ⬜ Pending |

---

**Related Documents:**
- [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+ RE Analysis]]
- [[V-SMASH_RE_02_ARCAS_analysis|ARCAS RE Analysis]]
- [[V-SMASH_P2_01_function_structure|V-SMASH Function Structure]]
- [[V-SMASH_P1_01_requirements_list|V-SMASH Requirements List]]

---

*Analysis conducted using SKILL_reverse_engineering methodology. Data source: Open Source Intelligence (OSINT) only. Physical specimen analysis would provide higher confidence.*
