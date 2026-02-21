---
project: V-SMASH
phase: 1
type: requirements
version: 1.5
created: 2026-01-18
updated: 2026-02-04
status: revised
---

# V-SMASH REQUIREMENTS LIST
## 12.7mm C-UAS Fire Control System - Phase 1: Task Clarification

**Project Code**: V-SMASH
**Reference System**: SmartShooter SMASH (Israel)
**Applicable to**: MTB-20 RCWS, VN-CUAV, Small Arms Enhancement

---

## 1. MISSION STATEMENT

Develop an **indigenous Vietnamese AI-powered fire control system** that enables:
- Single-shot-single-hit capability against moving aerial and ground targets
- Integration with Vietnamese weapon platforms (MTB-20, rifles, vehicle weapons)
- Sustainable local production and maintenance
- Counter-UAS capability for national defense

---

## 2. DESIGN PHILOSOPHY

### Core Principles (Adopted from SMASH Analysis)

#### Principle 1: HUMAN-IN-THE-LOOP
**Vietnamese**: Con người trong vòng điều khiển

**Description**:
- AI assists, human decides
- Operator must initiate trigger action
- System only optimizes TIMING of fire
- No autonomous lethal decision-making

**Rationale**:
- Legal compliance (international humanitarian law)
- Ethical responsibility
- Operator confidence and trust

**Implementation**:
- Trigger gating requires human pressure first
- Clear "SAFE" and "AI-READY" states
- Manual override always available

#### Principle 2: MODULAR PLATFORM
**Vietnamese**: Nền tảng mô-đun

**Description**:
- Core processing module shared across variants
- Weapon-specific interface modules
- Software-configurable for different platforms
- Upgrade path built-in

**Rationale**:
- Reduce total development cost
- Faster time to multiple products
- Easier maintenance and logistics

**Implementation**:
- Common AI processing board
- Interchangeable sensor heads
- Standardized weapon interfaces
- USB/Ethernet configuration port

#### Principle 3: FAIL-SAFE TO MANUAL
**Vietnamese**: An toàn mặc định - chuyển sang thủ công

**Description**:
- If FCS fails, weapon operates normally
- No dependency on electronics for basic function
- Graceful degradation of capabilities
- Clear failure indicators

**Rationale**:
- Combat reliability
- Operator confidence
- Mission continuity

**Implementation**:
- Mechanical decoupling option
- Battery failure = normal trigger
- Visual/audio failure warnings
- Standard sights backup (V-SMASH-X4)

---

## 3. COMPLETE REQUIREMENTS LIST

### Verification Methods Legend

| Code | Method | Description |
|------|--------|-------------|
| **A** | Analysis | Calculation, simulation, modeling |
| **I** | Inspection | Visual examination, measurement |
| **D** | Demonstration | Functional operation under controlled conditions |
| **T** | Test | Formal testing per specified procedures |

### Requirements Table (D = Demand, W = Wish)

| ID | Category | Requirement | D/W | Value | Verification | Remarks |
|----|----------|-------------|-----|-------|--------------|---------|
| **FUNCTIONAL** | | | | | | |
| R01 | Performance | Detect aerial targets (drones) | D | 95% @ 300m | T | Day conditions, MIL-STD test setup |
| R02 | Performance | Detect ground targets (personnel) | D | 95% @ 500m | T | Day conditions |
| R03 | Performance | Track moving targets | D | Up to 50 m/s | T | Drone typical speed |
| R04 | Performance | Calculate fire solution | D | <100ms latency | T | Instrumented timing |
| R05 | Performance | Gate trigger at optimal moment | D | <5ms precision | T | High-speed camera verification |
| R06 | Performance | Night operation capability | **D** | 200m range | T | **UPGRADED from W** ← ODI S1-22 (Opp: 14.2) |
| R07 | Data | Record engagements | W | 720p video | D | For training/legal review |
| **PERFORMANCE** | | | | | | |
| R08 | Range | Effective range - drone engagement | D | 250m minimum | T | 5.56mm platform |
| R09 | Range | Effective range - HMG platform | W | 400m | T | 12.7mm platform |
| R10 | Effectiveness | Hit probability improvement | D | 3x baseline | T | Compared to iron sights |
| R11 | Effectiveness | First-shot hit probability | W | >70% | T | Moving target @ 200m |
| **ENVIRONMENTAL** | | | | | | |
| R12 | Temperature | Operating temperature range | D | -10°C to +55°C | T | MIL-STD-810H Method 501.7/502.7 |
| R13 | Humidity | Humidity resistance | D | 95% RH | T | MIL-STD-810H Method 507.6 |
| R14 | Sealing | Dust/water protection | D | **IP67** | T | **UPGRADED from IP65** ← ODI S1-19 (Opp: 13.2) |
| R15 | Shock | Shock resistance | D | Per MIL-STD-810H | T | Method 516.8 (functional shock) |
| R16 | Vibration | Vibration resistance | D | Per MIL-STD-810H | T | Method 514.8 Cat. 20 (ground vehicles) |
| R17 | Salt Fog | Corrosion resistance | W | Per MIL-STD-810H | T | Method 509.7 (for naval variant) |
| **PHYSICAL/GEOMETRY** | | | | | | |
| R18 | Mass | Handheld variant weight | D | <1.5 kg | I | Including battery |
| R19 | Mass | RCWS module weight | D | <3 kg | I | Vehicle integration |
| R20 | Dimensions | Handheld envelope | D | 200×100×120mm max | I | Picatinny-mounted clearances |
| R21 | Power | Power consumption average | D | <10W | T | Continuous operation |
| R22 | Power | Battery life | D | >6 hours | T | Full operational mode |
| **INTEGRATION/KINEMATICS** | | | | | | |
| R23 | Interface | Mounting interface | D | Picatinny rail | I | MIL-STD-1913 compliance |
| R24 | Compatibility | Compatible weapon platforms | D | AK/M16/Galil, PKM, NSV, DShK | D | VPA inventory coverage |
| R25 | Compatibility | MTB-20 RCWS integration | D | Full compatibility | D | Primary vehicle platform |
| R26 | Field of View | Optical FOV | D | ≥15° | I | Adequate target acquisition |
| **SIGNALS/DATA** | | | | | | |
| R27 | Interface | Configuration interface | D | USB-C | D | Field programmable |
| R28 | Interface | Video output (optional) | W | Composite/HDMI | D | For external display |
| R29 | Storage | Onboard storage | W | 32GB minimum | I | Engagement recording |
| R30 | Protocol | MTB-20 data interface | D | CAN bus | T | Vehicle integration |
| **SAFETY** | | | | | | |
| R31 | Safety | Human-in-the-loop enforcement | D | Trigger requires human initiation | A/D | Ethical/legal requirement |
| R32 | Safety | Fail-safe to manual operation | D | Weapon functional without FCS | D | Combat reliability |
| R33 | Safety | Clear mode indication | D | Visual + audio status | D | Operator awareness |
| R34 | Safety | No inadvertent discharge | D | Per MIL-STD-882E | A | System safety analysis |
| R35 | EMC | Electromagnetic compatibility | D | Per MIL-STD-461G | T | CE106, RS103, CS114 |
| **ERGONOMICS** | | | | | | |
| R36 | Human Factors | Eye relief | D | Unlimited (reflex style) | I | Rapid target acquisition |
| R37 | Human Factors | Reticle visibility | D | Visible in daylight | D | 50,000 lux ambient |
| R38 | Human Factors | Control accessibility | D | Single-hand operation | D | While holding weapon |
| **PRODUCTION** | | | | | | |
| R39 | Sourcing | Local content | D | >60% by value | A | Self-reliance target |
| R40 | Components | COTS component usage | D | Maximize where possible | A | Cost efficiency |
| R41 | Cost | Unit cost target (LITE) | W | <$5,000 USD | A | Export competitive |
| R42 | Complexity | Manufacturing complexity | W | Medium (local capability) | A | Vietnamese facilities |
| **ASSEMBLY** | | | | | | |
| R43 | Assembly | Assembly tools required | D | Standard hand tools only | I | No specialized tooling |
| R44 | Assembly | Assembly time | W | <4 hours per unit | D | Production efficiency |
| R45 | Assembly | Calibration requirement | D | Factory calibration only | D | No field adjustment |
| **MAINTENANCE/OPERATION** | | | | | | |
| R46 | Maintenance | Field-level repair capability | D | No special tools required | D | Soldier-level maintenance |
| R47 | Reliability | Mean Time Between Failures | D | >2,000 hours | A | MIL-HDBK-217F prediction |
| R48 | Maintenance | Software update method | D | Field flashable via USB | D | No depot return |
| R49 | Diagnostics | Built-in test capability | W | System status self-check | D | Operator-initiated |
| **TRANSPORT/STORAGE** | | | | | | |
| R50 | Storage | Storage temperature range | D | -40°C to +70°C | T | Warehouse conditions |
| R51 | Transport | Shipping protection | W | Pelican-style case compatible | I | Standard military logistics |
| **QUALITY CONTROL** | | | | | | |
| R52 | QC | Acceptance test procedure | D | Documented ATP | D | Per deliverable specification |
| R53 | QC | Inspection criteria | D | Workmanship per IPC-A-610 | I | Electronics assembly |
| **LEGAL/REGULATORY** | | | | | | |
| R54 | Compliance | Vietnamese military certification | D | Per MoD requirements | D | Type approval |
| R55 | Compliance | Export control classification | W | Non-ITAR design preferred | A | International sales |
| **RECYCLING/DISPOSAL** | | | | | | |
| R56 | Environment | Battery disposal compliance | D | Per Vietnamese regulations | A | Li-ion handling |
| R57 | Environment | RoHS compliance (civil variant) | W | RoHS 3 compliant | A | Dual-use potential |
| | | | | | | |
| | | **── NEW REQUIREMENTS (ODI Phase 0 v1.1) ──** | | | | |
| **R58** | **Performance** | **False positive rate (non-threat misidentification)** | **D** | **<5%** | **T** | **← ODI S1-16 (Opp: 13.5)** |
| **R59** | **Performance** | **Detection in varying light (dawn/dusk/shadow)** | **D** | **95% @ 1,000-50,000 lux** | **T** | **← ODI S1-17 (Opp: 12.8)** |
| **R60** | **Performance** | **Tracking maneuvering targets (evasive flight)** | **D** | **Maintain lock during 3g turn** | **T** | **← ODI S1-24 (Opp: 13.0)** |
| **R61** | **Sensor** | **Dynamic range (HDR capability)** | **D** | **≥80 dB** | **T** | **Supports S1-17 varying light** |
| **R62** | **Sensor** | **Thermal/IR sensor integration** | **D** | **LWIR 8-14μm, NETD <50mK** | **T** | **Supports S1-22 night ops** |
| **R63** | **Environmental** | **Lens anti-fog/condensation** | **D** | **Heater or hydrophobic coating** | **D** | **← ODI S1-19 (Opp: 13.2)** |
| **R64** | **Environmental** | **Lens protection (dust/rain)** | **W** | **Wiper or sacrificial cover** | **I** | **← ODI S1-19 (Opp: 13.2)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - ARCAS Analysis) ──** | | | | |
| **R65** | **Performance** | **Multi-target tracking capability** | **D** | **≥5 targets simultaneous** | **T** | **← ARCAS RE (swarm defense)** |
| **R66** | **Performance** | **Automatic threat prioritization** | **W** | **Rank by threat level (distance, speed, heading)** | **D** | **← ARCAS RE (PRO variant)** |
| **R67** | **Interface** | **Tactical data link for target sharing** | **W** | **Export target coords via C4I protocol** | **D** | **← ARCAS RE (PRO option)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - ARBEL Analysis) ──** | | | | |
| **R68** | **AI/Software** | **C-UAS specific AI training dataset** | **D** | **≥5,000 drone images (FPV, commercial, loitering)** | **A** | **← ARBEL RE (drone-optimized AI)** |
| **R69** | **Performance** | **Backup passive ranging (size-based)** | **W** | **±20% accuracy @ 100-300m** | **T** | **← ARBEL RE (LITE fallback)** |
| **R70** | **Sensor** | **Sensor fusion algorithm (day+thermal)** | **D** | **Weighted blend, auto-switching** | **T** | **← ARBEL RE (PRO only)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - SMASH Connectivity Analysis) ──** | | | | |
| **R90** | **Platform** | **12.7mm HMG mounting kit** | **D** | **Compatible with NSV, DShK, M2; recoil-tolerant** | **T** | **← SMASH Connectivity RE (primary V-SMASH mission)** |
| **R91** | **Security** | **Encrypted communications** | **D** | **AES-256 for all wireless data** | **T** | **← SMASH Connectivity RE (military requirement)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - SMASH Hopper 5000 Analysis) ──** | | | | |
| **R92** | **RCWS** | **RCWS total weight (excl. weapon)** | **D** | **≤15 kg** | **I** | **← Hopper 5000 RE (benchmark)** |
| **R93** | **RCWS** | **Slew rate variable** | **D** | **0.1-40°/sec** | **T** | **← Hopper 5000 RE (fast tracking)** |
| **R94** | **RCWS** | **Elevation range** | **D** | **-30° to +70°** | **T** | **← Hopper 5000 RE (C-UAS optimized)** |
| **R95** | **RCWS** | **Azimuth coverage** | **D** | **360° continuous** | **T** | **← Hopper 5000 RE (full coverage)** |
| **R96** | **RCWS** | **Max acceleration** | **D** | **≥100°/sec²** | **T** | **← Hopper 5000 RE (fast acquisition)** |
| **R97** | **RCWS** | **Dual connectivity** | **D** | **Wired + wireless options** | **D** | **← Hopper 5000 RE (operational flexibility)** |
| **R98** | **RCWS** | **External cue acceptance** | **D** | **Radar/C2 target handoff interface** | **D** | **← Hopper 5000 RE (SMASH DOME concept)** |
| **R99** | **RCWS** | **RCWS operating temperature** | **D** | **-10°C to +55°C** | **T** | **← Hopper 5000 RE (Vietnam adjusted)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - SMASH Hopper Light Analysis) ──** | | | | |
| **R100** | **RCWS-LITE** | **RCWS-LITE weight (excl. weapon)** | **D** | **≤10 kg** | **I** | **← Hopper Light RE (single-soldier)** |
| **R101** | **RCWS-LITE** | **Single-soldier operation** | **D** | **Carry, setup, operate by 1 person** | **D** | **← Hopper Light RE (key differentiator)** |
| **R102** | **RCWS-LITE** | **Setup time** | **D** | **<3 minutes** | **T** | **← Hopper Light RE (rapid deployment)** |
| **R103** | **RCWS-LITE** | **Transportability** | **D** | **Backpack/bag portable** | **D** | **← Hopper Light RE (infantry mobility)** |
| **R104** | **RCWS-LITE** | **RCWS-LITE slew rate** | **W** | **≥25°/sec** | **T** | **← Hopper Light RE (trade-off acceptable)** |
| **R105** | **RCWS-LITE** | **RCWS-LITE elevation** | **W** | **-20° to +60°** | **T** | **← Hopper Light RE (compact design)** |
| **R106** | **RCWS-LITE** | **Battery operation** | **D** | **≥2 hours standalone** | **T** | **← Hopper Light RE (dismounted ops)** |
| **R107** | **RCWS-LITE** | **Visual profile** | **W** | **Low-profile design for covert ops** | **I** | **← Hopper Light RE (tactical advantage)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - SMASH DOME Analysis) ──** | | | | |
| **R108** | **C-UAS** | **Integrated detect-track-engage** | **D** | **Layered C-UAS architecture** | **D** | **← SMASH DOME RE (system concept)** |
| **R109** | **C-UAS** | **Detection range (EO/IR)** | **D** | **≥1 km baseline** | **T** | **← SMASH DOME RE (portable requirement)** |
| **R110** | **C-UAS** | **Detect-to-kill time** | **D** | **≤15 seconds** | **T** | **← SMASH DOME RE (engagement timeline)** |
| **R111** | **C-UAS** | **Person-in-the-loop engagement** | **D** | **Operator confirms all shots** | **D** | **← SMASH DOME RE (IHL compliance)** |
| **R112** | **C-UAS** | **Simultaneous track management** | **D** | **≥3 targets** | **T** | **← SMASH DOME RE (swarm defense)** |
| **R113** | **C-UAS** | **External radar cue interface** | **W** | **Accept radar track handoff** | **D** | **← SMASH DOME RE (scalability)** |
| **R114** | **C-UAS** | **ATAK/CoT protocol integration** | **D** | **Open standard C2 interface** | **D** | **← SMASH DOME RE (interoperability)** |
| **R115** | **C-UAS** | **Cost per engagement** | **D** | **≤$10 (ammunition)** | **A** | **← SMASH DOME RE (sustainability)** |
| | | | | | | |
| | | **── NEW REQUIREMENTS (RE Phase - SMASH Dragon Analysis) ── FUTURE** | | | | |
| **R116** | **UAV** | **FCS payload weight** | **W** | **≤5 kg** | **I** | **← Dragon RE (Phase 4 - future)** |
| **R117** | **UAV** | **Stabilized gimbal for airborne** | **W** | **2/3-axis airborne stabilization** | **T** | **← Dragon RE (Phase 4 - future)** |
| **R118** | **UAV** | **Air-to-air tracking capability** | **W** | **Track aerial targets from UAV** | **T** | **← Dragon RE (Phase 4 - future)** |
| **R119** | **UAV** | **Platform-agnostic interface** | **W** | **Modular payload for multiple UAVs** | **D** | **← Dragon RE (Phase 4 - future)** |
| **R120** | **UAV** | **Recoil management for airborne** | **W** | **Dampened mount, fire timing sync** | **T** | **← Dragon RE (Phase 4 - future)** |

### Requirements Summary Statistics

| Category | Demands | Wishes | Total | Change |
|----------|---------|--------|-------|--------|
| Functional | 6 | 1 | 7 | R06: W→D |
| Performance | **7** | 4 | **11** | +R96 |
| Environmental | 7 | 2 | 9 | +R63, R64; R14 upgraded |
| Physical/Geometry | 5 | 0 | 5 | — |
| Integration/Kinematics | 4 | 0 | 4 | — |
| Signals/Data | 2 | 3 | 5 | +R67 |
| Safety | 5 | 0 | 5 | — |
| Ergonomics | 3 | 0 | 3 | — |
| Production | 2 | 2 | 4 | — |
| Assembly | 2 | 1 | 3 | — |
| Maintenance/Operation | 3 | 1 | 4 | — |
| Transport/Storage | 1 | 1 | 2 | — |
| Quality Control | 2 | 0 | 2 | — |
| Legal/Regulatory | 1 | 1 | 2 | — |
| Recycling/Disposal | 1 | 1 | 2 | — |
| Sensor | 3 | 0 | 3 | +R61, R62, R70 |
| AI/Software | 1 | 0 | 1 | +R68 |
| Platform | 1 | 0 | 1 | +R90 |
| Security | 1 | 0 | 1 | +R91 |
| **RCWS (NEW)** | **8** | **0** | **8** | **+R92-R99** |
| **RCWS-LITE (NEW)** | **5** | **3** | **8** | **+R100-R107** |
| **C-UAS (NEW)** | **7** | **1** | **8** | **+R108-R115** |
| **UAV (NEW - Future)** | **0** | **5** | **5** | **+R116-R120** |
| **TOTAL** | **77** | **24** | **101** | **+29 new (v1.5)** |

**Quantification Level**: 77/101 = **76.2%** Demands quantified (Target: ≥80%)
**Note**: UAV requirements (R116-R120) are Wishes for Phase 4 future development.

---

## 4. PROBLEM ABSTRACTION (Pahl & Beitz 5-Step Method)

### Purpose
Before creating the function structure, we abstract the requirements list to identify the **essential problem** in solution-neutral terms. This expands the design space and prevents premature solution fixation.

### Step 1: Eliminate Personal Preferences

**Review of requirements for solution bias:**

| Original Requirement | Assessment | Action |
|---------------------|------------|--------|
| "Use NVIDIA Jetson" (implicit in WP selection) | Solution bias - specifies technology | Reformulate: "Process video/AI inference in real-time with ≤10W power" |
| "YOLO-based detection" (implicit) | Solution bias - specifies algorithm | Reformulate: "Detect targets with ≥95% accuracy in operational conditions" |
| "Picatinny rail mount" (R23) | **Retained** - Customer mandate (VPA weapon standard) | Keep as essential constraint |
| "USB-C interface" (R27) | Minor solution preference | Accept - industry standard, minimal impact |

**Result**: Requirements list is reasonably solution-neutral. Key requirements express WHAT (function) not HOW (mechanism).

### Step 2: Omit Non-Essential Requirements

**Main Function Statement:**
> "Improve weapon hit probability against moving aerial/ground targets through optimized fire timing"

**Essential vs Non-Essential Classification:**

| Requirement Type | Essential (Retain) | Non-Essential (Omit for Abstraction) |
|------------------|-------------------|-------------------------------------|
| **Core Function** | R01-R05 (detection, tracking, fire solution, trigger timing) | R07 (video recording - auxiliary) |
| **Critical Constraints** | R31-R35 (safety), R12-R16 (environmental) | R17 (salt fog - variant-specific) |
| **Interface Mandates** | R23 (Picatinny - customer requirement), R25 (MTB-20) | R28 (video output - nice-to-have) |
| **Physical Limits** | R18-R22 (size, weight, power) | R51 (shipping case) |

**Retained for Essential Problem:** 28 requirements (core function + critical constraints + mandated interfaces)

### Step 3: Transform Quantitative → Qualitative

| Quantitative Specification | Qualitative Essence |
|---------------------------|---------------------|
| "95% detection @ 300m" | Reliable target acquisition at infantry engagement distances |
| "<100ms fire solution, <5ms trigger timing" | Real-time response enabling intercept of fast-moving targets |
| "Track up to 50 m/s" | Capability against small UAS threat spectrum |
| "3x hit probability improvement" | Significant effectiveness increase justifying system adoption |
| "-10°C to +55°C, IP65, MIL-STD-810H" | Function in harsh field conditions across Vietnamese operational environments |
| "<1.5 kg, <10W" | Soldier-portable without significant burden |
| "Human-in-the-loop, fail-safe to manual" | Ethical operation with combat reliability |

### Step 4: Generalize the Results

| Specific Formulation | Generalized Formulation | Assessment |
|---------------------|------------------------|------------|
| "AI-powered optic sight" | "Weapon aiming enhancement system" | Good - allows non-AI solutions |
| "Counter-drone capability" | "Engagement of small, fast, maneuvering aerial targets" | Good - doesn't limit to only drones |
| "Trigger gating mechanism" | "Fire timing optimization method" | Good - allows alternatives to solenoid |
| "NVIDIA Jetson processing" | "Edge computing with real-time inference" | Good - platform-neutral |

**Generalization Boundary**: We maintain specificity for:
- Infantry/vehicle weapon integration (not naval guns, artillery)
- Visual-band/thermal sensing (not radar-based)
- Direct fire weapons (not missiles, guided munitions)

### Step 5: Solution-Neutral Problem Formulation

**ESSENTIAL PROBLEM STATEMENT:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      V-SMASH ESSENTIAL PROBLEM                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  FUNCTION:                                                                   │
│  Enable high-probability weapon-target intercept against small, fast,       │
│  maneuvering aerial and ground targets within infantry/vehicle engagement   │
│  distances through optimized fire timing.                                   │
│                                                                              │
│  ESSENTIAL CONSTRAINTS:                                                      │
│  • Human must retain authorization decision (ethical/legal)                 │
│  • System must not prevent weapon operation if failed (combat reliability)  │
│  • Must operate in harsh field environments (MIL-STD-810H envelope)         │
│  • Must be soldier-portable (<1.5kg) or vehicle-integrable (<3kg)           │
│  • Must integrate with existing VPA weapon inventory (AK/M16/PKM/NSV/DShK)  │
│  • Must be producible primarily with Vietnamese capabilities (>60% local)   │
│                                                                              │
│  PROBLEM CLASS:                                                              │
│  "Augmented weapon effectiveness systems for emerging asymmetric threats"   │
│                                                                              │
│  SOLUTION SPACE ENABLED:                                                     │
│  1. Electro-optical + AI processing (SMASH-like)                            │
│  2. Laser designation + ballistic computer                                  │
│  3. Predictive reticle without trigger gating                               │
│  4. Acoustic/RF detection + simple lead indicator                           │
│  5. Hybrid sensor fusion approaches                                         │
│                                                                              │
│  SELECTED APPROACH: #1 (Electro-optical + AI) based on reference system     │
│  analysis and technology readiness assessment.                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Validation**: The abstracted problem enables at least 5 fundamentally different solution approaches while maintaining essential defense context. ✓

---

## 5. ODI → REQUIREMENTS TRACEABILITY (v1.1)

### 5.1 ODI Outcome to Requirement Mapping

| ODI ID | Outcome Statement | Opp | Requirement(s) | D/W | Value |
|--------|-------------------|-----|----------------|-----|-------|
| **EXTREME** | | | | | |
| S1-01 | Minimize time: acquisition → first shot | 17.2 | R04, R05 | D | <100ms, <5ms |
| S1-02 | Maximize tracking lock probability | 16.5 | R01, R03 | D | 95%, 50 m/s |
| **HIGH (Original)** | | | | | |
| S1-03 | Minimize ammo per kill | 13.8 | R10, R11 | D/W | 3x, >70% |
| S1-04 | Minimize time to locate drone | 13.6 | R26 | D | ≥15° FOV |
| S1-05 | Maximize first-round hit probability | 13.7 | R10, R11 | D/W | 3x, >70% |
| S1-06 | Minimize tracking jitter | 13.0 | R03 | D | 50 m/s track |
| **HIGH (NEW - Phase 2 Insights)** | | | | | |
| **S1-16** | **Minimize false positive rate** | **13.5** | **R58** | **D** | **<5%** |
| **S1-17** | **Maximize detection in varying light** | **12.8** | **R59, R61** | **D** | **95% @ 1k-50k lux, ≥80dB HDR** |
| **S1-19** | **Minimize environmental effects** | **13.2** | **R14↑, R63, R64** | **D/W** | **IP67↑, heater, wiper** |
| **S1-22** | **Maximize night/low-light capability** | **14.2** | **R06↑, R62** | **D** | **200m, LWIR sensor** |
| **S1-24** | **Maximize effectiveness vs. evasive maneuvers** | **13.0** | **R60** | **D** | **3g turn tracking** |

### 5.2 Requirements Changes Summary (v1.0 → v1.1)

| Change Type | Requirement | Before | After | ODI Source |
|-------------|-------------|--------|-------|------------|
| **UPGRADED** | R06 | W (optional) | **D (mandatory)** | S1-22 (Night ops) |
| **UPGRADED** | R14 | IP65 | **IP67** | S1-19 (Environmental) |
| **NEW** | R58 | — | False positive <5% | S1-16 |
| **NEW** | R59 | — | Varying light detection | S1-17 |
| **NEW** | R60 | — | Evasive maneuver tracking | S1-24 |
| **NEW** | R61 | — | HDR ≥80dB | S1-17 |
| **NEW** | R62 | — | Thermal sensor | S1-22 |
| **NEW** | R63 | — | Anti-fog lens | S1-19 |
| **NEW** | R64 | — | Lens wiper (W) | S1-19 |

### 5.3 Cost Impact Assessment (Preliminary)

| New Requirement | Est. Unit Cost Impact | Notes |
|-----------------|----------------------|-------|
| R62 (Thermal sensor) | +$800-1,500 | LWIR module (FLIR Lepton or similar) |
| R61 (HDR sensor) | +$50-100 | Sony IMX462 vs IMX290 |
| R14 (IP67 vs IP65) | +$30-50 | Better seals, gaskets |
| R63 (Lens heater) | +$20-40 | Resistive heater, controller |
| R60 (IMM filter) | +$0 (software) | Algorithm development |
| **Total Impact** | **+$900-1,690** | ~15-25% cost increase |

**Recommendation**: Thermal sensor (R62) is the largest cost driver. Consider:
- **V-SMASH-LITE**: CMOS only, night clip-on compatible (base price)
- **V-SMASH-PRO**: Integrated thermal (premium variant)

### 5.4 RE → Requirements Traceability (v1.3)

| RE Source | System | Finding | Requirement(s) | D/W | Variant |
|-----------|--------|---------|----------------|-----|---------|
| ARCAS RE | Elbit ARCAS | Multi-target tracking (10+) | **R65** | **D** | Both |
| ARCAS RE | Elbit ARCAS | Threat prioritization AI | **R66** | W | PRO |
| ARCAS RE | Elbit ARCAS | Built-in C4I integration | **R67** | W | PRO option |
| ARBEL RE | IWI ARBEL | C-UAS optimized AI training | **R68** | **D** | Both |
| ARBEL RE | IWI ARBEL | Passive ranging (backup) | **R69** | W | LITE |
| ARBEL RE | IWI ARBEL | Native sensor fusion | **R70** | **D** | PRO |
| **SMASH Conn RE** | **SMASH 2000+/3000** | **HMG platform integration** | **R90** | **D** | **Both** |
| **SMASH Conn RE** | **SMASH 2000+/3000** | **Encrypted tactical comms** | **R91** | **D** | **PRO** |
| **Hopper 5000 RE** | **SMASH Hopper 5000** | **RCWS weight/performance benchmarks** | **R92-R99** | **D** | **RCWS** |
| **Hopper Light RE** | **SMASH Hopper Light** | **Single-soldier ultra-light RCWS** | **R100-R107** | **D/W** | **RCWS-LITE** |
| **SMASH DOME RE** | **SMASH DOME** | **Integrated C-UAS system architecture** | **R108-R115** | **D/W** | **DOME** |
| **Dragon RE** | **SMASH Dragon** | **Armed UAV payload (future)** | **R116-R120** | **W** | **Phase 4** |

**RE Reference Documents:**
- [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+ RE Analysis]] - Fire control mechanism
- [[V-SMASH_RE_02_ARCAS_analysis|ARCAS RE Analysis]] - Multi-target, C4I networking
- [[V-SMASH_RE_03_SMASH_Dragon_analysis|SMASH Dragon RE Analysis]] - Armed UAV payload
- [[V-SMASH_RE_04_SMASH3000_analysis|SMASH 2000L/3000 RE Analysis]] - Latest generation FCS
- [[V-SMASH_RE_05_SMASHX4_analysis|SMASH X4 RE Analysis]] - Magnified FCS
- [[V-SMASH_RE_06_SMASH_connectivity_analysis|SMASH Connectivity RE Analysis]] - Networking, HMG, RCWS
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|SMASH Hopper 5000 RE Analysis]] - Full RCWS
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis|SMASH Hopper Light RE Analysis]] - Ultra-light RCWS
- [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME RE Analysis]] - Integrated C-UAS

---

## 6. GATE 1 CHECKLIST (Phase 1 → Phase 2 Transition)

- [x] All MUST requirements quantified (**77/77 Demands have values** ← updated v1.5)
- [x] Verification methods specified for all requirements
- [ ] Stakeholder sign-off obtained (PENDING)
- [x] No conflicts detected between requirements
- [x] Problem abstraction completed
- [x] **ODI traceability established** ← v1.1
- [x] **RE traceability established** ← v1.5 (10 RE analyses: SMASH family, ARCAS, ARBEL, Hopper, DOME, Dragon)

**Status**: ✅ **Ready for Phase 2 - Conceptual Design** (Revised v1.5)

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-18 | Initial requirements list (57 requirements, 43 Demands) |
| 1.1 | 2026-02-04 | ODI-driven revision: +7 requirements (R58-R64), R06 W→D, R14 IP65→IP67. Total: 64 requirements, 51 Demands. Added ODI traceability section (§5). Est. cost impact: +$900-1,690/unit. |
| 1.2 | 2026-02-04 | ARCAS RE-driven: +3 requirements (R65-R67). Multi-target tracking (D), threat prioritization (W), C4I link (W). Total: 67 requirements, 52 Demands. |
| 1.3 | 2026-02-04 | ARBEL RE-driven: +3 requirements (R68-R70). C-UAS AI training (D), passive ranging backup (W), sensor fusion (D). Total: 70 requirements, 54 Demands. Added ARBEL to RE traceability. |
| 1.4 | 2026-02-04 | SMASH Connectivity RE-driven: +2 requirements (R90-R91). 12.7mm HMG mounting kit (D), encrypted communications (D). Total: 72 requirements, 56 Demands. Added SMASH Connectivity to RE traceability. |
| **1.5** | **2026-02-04** | **Major RE expansion: +29 requirements (R92-R120) from 4 RE analyses. RCWS (R92-R99, 8D), RCWS-LITE (R100-R107, 5D/3W), C-UAS (R108-R115, 7D/1W), UAV future (R116-R120, 5W). Total: 101 requirements, 77 Demands, 24 Wishes. Added Hopper 5000, Hopper Light, SMASH DOME, Dragon to RE traceability.** |

---

*Next: [[V-SMASH_P2_01_function_structure|Function Structure]] - Phase 2*
*Back to: [[V-SMASH_00_project_brief|Project Brief]]*
*ODI Source: [[V-SMASH_P0_01_ODI_analysis|ODI Analysis v1.1]]*

**RE Sources (10 Analyses):**
- Handheld: [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+]] | [[V-SMASH_RE_04_SMASH3000_analysis|SMASH 3000]] | [[V-SMASH_RE_05_SMASHX4_analysis|SMASH X4]]
- Platform: [[V-SMASH_RE_02_ARCAS_analysis|ARCAS]] | [[V-SMASH_RE_06_SMASH_connectivity_analysis|Connectivity]] | [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|Hopper 5000]] | [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light]]
- System: [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME]] | [[V-SMASH_RE_03_SMASH_Dragon_analysis|SMASH Dragon]]
