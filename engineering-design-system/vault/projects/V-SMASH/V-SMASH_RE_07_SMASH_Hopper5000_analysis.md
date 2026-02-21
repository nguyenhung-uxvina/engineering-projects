---
project: V-SMASH
phase: 2
type: reverse-engineering
subject: SMASH Hopper 5000 LRCWS
version: 1.0
created: 2026-02-04
status: complete
methodology: D-M-I-R aligned
---

# V-SMASH RE-07: SMASH Hopper 5000 LRCWS Analysis

## 1. System Identification

| Attribute | Value |
|-----------|-------|
| **Product** | SMASH Hopper 5000 |
| **Manufacturer** | Smart Shooter Ltd. (Israel) |
| **Category** | Light Remote Controlled Weapon Station (LRCWS) |
| **Generation** | 3rd Gen (Current flagship RCWS) |
| **First Unveiled** | 2020 (Eurosatory), Enhanced 2022-2025 |
| **Status** | Production, Combat-proven |
| **Primary Mission** | Force protection, C-UAS, Remote engagement |

### Market Positioning
```
RCWS Market Segment:
┌─────────────────────────────────────────────────────────────────┐
│  Heavy RCWS (50-500kg)                                          │
│  ├── Kongsberg CROWS (~200kg)                                   │
│  ├── Rafael Samson (~150kg)                                     │
│  └── 12.7mm/.50 cal primary                                     │
├─────────────────────────────────────────────────────────────────┤
│  Medium RCWS (25-50kg)                                          │
│  ├── FN deFNder                                                 │
│  └── 7.62mm primary                                             │
├─────────────────────────────────────────────────────────────────┤
│  SMASH Hopper 5000 (~15kg) ← ULTRA-LIGHT SEGMENT               │
│  ├── Unique: FCS-integrated LRCWS                               │
│  ├── 5.56-7.62mm NATO                                           │
│  └── Man-portable, UGV-mountable                                │
└─────────────────────────────────────────────────────────────────┘
```

**Key Differentiator**: Only LRCWS with integrated AI-based Fire Control System

---

## 2. External Characterization

### 2.1 Physical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **System Weight** | ~15 kg | Core LRCWS unit |
| **Total Weight** | ≤25 kg | With weapon + ammo |
| **Max Payload** | 40 kg | Balanced load capacity |
| **Form Factor** | Compact pan-tilt head | Rapid deployment |
| **Portability** | 2-person carry | Man-portable |

### 2.2 Motion Performance

| Parameter | Value | Significance |
|-----------|-------|--------------|
| **Slew Rate** | 0.01 - 40°/sec | Variable for precise/fast tracking |
| **Max Acceleration** | 100°/sec² | Rapid target acquisition |
| **Azimuth (Pan)** | 360° continuous | Adjustable limits available |
| **Elevation (Tilt)** | -30° to +70° | Drone engagement optimized |

### 2.3 Environmental Specifications

| Standard | Rating | Application |
|----------|--------|-------------|
| **MIL-STD-810G** | Full compliance | Shock, vibration, dust, humidity |
| **Operating Temp** | -30°C to +55°C | Extreme climate capable |
| **Power Input** | 24V - 36V DC | Vehicle/generator compatible |
| **Protection** | Ruggedized | Field deployable |

### 2.4 Weapon Compatibility

| Weapon | Caliber | Role |
|--------|---------|------|
| **M4/M4A1** | 5.56×45mm NATO | Anti-personnel, C-sUAS |
| **SR25** | 7.62×51mm NATO | Extended range, anti-materiel |

**Magazine Capacity**: Standard rifle magazines (30rd 5.56, 20rd 7.62)

---

## 3. Subsystem Decomposition

### 3.1 Functional Architecture

```
┌────────────────────────────────────────────────────────────────────┐
│                    SMASH HOPPER 5000 LRCWS                         │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐     │
│  │   SENSOR     │    │     FCS      │    │   EFFECTOR       │     │
│  │   PAYLOAD    │───▶│   COMPUTER   │───▶│   ASSEMBLY       │     │
│  │              │    │              │    │                  │     │
│  │ • Day camera │    │ • Target     │    │ • Weapon cradle  │     │
│  │ • Thermal    │    │   tracking   │    │ • Trigger mech   │     │
│  │   (optional) │    │ • Ballistic  │    │ • Recoil mgmt    │     │
│  │ • LRF        │    │   computer   │    │                  │     │
│  └──────────────┘    │ • AI/ML      │    └──────────────────┘     │
│                      └──────────────┘                              │
│         ▲                   │                     │                │
│         │                   ▼                     │                │
│  ┌──────────────┐    ┌──────────────┐            │                │
│  │   EXTERNAL   │    │  PAN-TILT    │────────────┘                │
│  │   SENSORS    │    │    HEAD      │                              │
│  │              │    │              │                              │
│  │ • Radar cue  │    │ • 2-axis     │                              │
│  │ • C2 handoff │    │   servo      │                              │
│  │ • ATAK data  │    │ • Position   │                              │
│  └──────────────┘    │   feedback   │                              │
│                      └──────────────┘                              │
│                            ▲                                       │
│                            │                                       │
│  ┌─────────────────────────┴───────────────────────────────────┐  │
│  │                    CONTROL INTERFACE                         │  │
│  │  • Remote Control Unit (RCU)                                 │  │
│  │  • Wired or Wireless connectivity                            │  │
│  │  • C2 system integration (ATAK, proprietary)                 │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### 3.2 Subsystem Details

#### A. Sensor Payload
| Component | Specification | Function |
|-----------|--------------|----------|
| **Day Camera** | HD CMOS | Target acquisition, tracking |
| **Thermal** | Optional LWIR | Night/obscured conditions |
| **LRF** | Integrated | Range measurement for ballistics |
| **FOV** | Standard/narrow | Configurable |

#### B. Fire Control System (FCS)
- **Core**: SMASH 2000 technology (same as handheld)
- **Processing**: Onboard computer with AI/ML
- **Functions**:
  - Automatic target detection
  - Real-time tracking (static + moving)
  - Ballistic solution computation
  - Fire synchronization ("smart trigger")
  - Multi-target prioritization

#### C. Pan-Tilt Head
| Axis | Range | Drive |
|------|-------|-------|
| **Pan (Azimuth)** | 360° | Servo motor |
| **Tilt (Elevation)** | -30° to +70° | Servo motor |
| **Accuracy** | <1 mrad | Encoder feedback |

#### D. Effector Assembly
- **Weapon Cradle**: Quick-change for M4/SR25
- **Trigger Mechanism**: Electronic solenoid
- **Recoil Management**: Damped mounting
- **Safe/Arm**: Electronic interlock

#### E. Control Interface
| Mode | Connection | Latency |
|------|------------|---------|
| **Wired** | Fiber/copper | <10ms |
| **Wireless** | Encrypted RF | <50ms |
| **C2 Integrated** | ATAK/proprietary | Network dependent |

---

## 4. Functional Reconstruction

### 4.1 Primary Functions

```
F0: PROVIDE REMOTE PRECISION ENGAGEMENT
├── F1: DETECT targets (ground/aerial)
│   ├── F1.1: Acquire EO/IR imagery
│   ├── F1.2: Process sensor data
│   └── F1.3: Classify target type
│
├── F2: TRACK targets continuously
│   ├── F2.1: Lock target designation
│   ├── F2.2: Predict target trajectory
│   └── F2.3: Maintain track through maneuvers
│
├── F3: COMPUTE firing solution
│   ├── F3.1: Measure range (LRF)
│   ├── F3.2: Calculate ballistics
│   └── F3.3: Compensate environmental factors
│
├── F4: POSITION weapon
│   ├── F4.1: Drive pan-tilt to solution
│   ├── F4.2: Synchronize with target motion
│   └── F4.3: Stabilize platform
│
├── F5: ENGAGE target (operator initiated)
│   ├── F5.1: Verify safe engagement
│   ├── F5.2: Time fire command
│   └── F5.3: Execute trigger release
│
└── F6: COMMUNICATE status
    ├── F6.1: Transmit video feed
    ├── F6.2: Report system state
    └── F6.3: Receive commands/cues
```

### 4.2 Operational Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Manual** | Operator drives pan-tilt, manual aim | Search, patrol |
| **Semi-Auto** | FCS tracks, operator authorizes fire | Standard engagement |
| **Auto-Track** | System tracks designated target | Continuous coverage |
| **Scan** | Automatic sector scanning | Perimeter security |
| **Cued** | External sensor handoff | C-UAS with radar |

### 4.3 C-UAS Operating Concept

```
SMASH DOME Integration (Layered C-UAS):

     ┌─────────────────────────────────────────┐
     │         DETECTION LAYER                 │
     │  ┌──────────┐    ┌──────────────────┐   │
     │  │  RF/EW   │    │  Radar (1-2km)   │   │
     │  │ Detector │    │  (DRS RPS-42)    │   │
     │  └────┬─────┘    └────────┬─────────┘   │
     │       │                   │             │
     │       └───────┬───────────┘             │
     │               ▼                         │
     │  ┌───────────────────────────────────┐  │
     │  │    C2 / Tracking System           │  │
     │  │  • Target fusion                  │  │
     │  │  • Track management               │  │
     │  │  • Handoff coordination           │  │
     │  └───────────────┬───────────────────┘  │
     │                  │                      │
     │                  ▼                      │
     │  ┌───────────────────────────────────┐  │
     │  │      SMASH HOPPER LRCWS           │  │
     │  │  • Receive track cue              │  │
     │  │  • FCS acquires + tracks          │  │
     │  │  • Operator confirms              │  │
     │  │  • Kinetic engagement             │  │
     │  └───────────────────────────────────┘  │
     │                                         │
     │  "Person-in-the-Loop" Design            │
     └─────────────────────────────────────────┘
```

---

## 5. Performance Estimation

### 5.1 Engagement Performance

| Metric | Estimate | Basis |
|--------|----------|-------|
| **Effective Range (Ground)** | 300-600m | 5.56mm ballistics |
| **Effective Range (Drone)** | 200-400m | Moving aerial target |
| **Hit Probability (Static)** | >95% | FCS-enhanced |
| **Hit Probability (Moving)** | >85% | <15 km/h ground target |
| **Hit Probability (Drone)** | ~90% | FCS tracking claim |
| **Engagement Time** | 2-5 sec | From cue to shot |
| **Rounds per Kill (Drone)** | 2-5 rds | Estimated |

### 5.2 Operational Performance

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Deployment Time** | <5 min | Tripod setup |
| **Redeployment** | <3 min | Already configured |
| **Endurance** | Vehicle power dependent | 24V-36V draw |
| **MTBF** | ~1000 hrs | Military electronics typical |

### 5.3 Comparison: Hopper vs Traditional RCWS

| Attribute | SMASH Hopper | Traditional RCWS |
|-----------|--------------|------------------|
| Weight | 15 kg | 50-200+ kg |
| Caliber | 5.56-7.62mm | 7.62-12.7mm |
| Accuracy | FCS-enhanced | Operator dependent |
| Setup | Minutes | Hours (integration) |
| Cost | ~$50-80K est. | $100-300K+ |
| UGV Compatible | ✓ | Limited |
| Drone Capable | ✓ Designed for | Add-on capability |

---

## 6. Design Philosophy Analysis

### 6.1 Core Design Principles

| Principle | Implementation | Rationale |
|-----------|----------------|-----------|
| **Ultra-Light** | 15 kg system | Man-portable, UGV mountable |
| **FCS-First** | Same tech as handheld SMASH | Core competency leverage |
| **Modularity** | Swap weapons, sensors | Platform flexibility |
| **Person-in-Loop** | Operator confirms all shots | ROE compliance, IHL |
| **Network-Centric** | C2/ATAK integration | Force multiplication |

### 6.2 Innovation Assessment

| Innovation | Type | Impact |
|------------|------|--------|
| **FCS-integrated RCWS** | Architectural | Market-defining |
| **15 kg weight class** | Parametric | New segment created |
| **UGV-native design** | Application | Autonomous integration |
| **Drone-optimized kinematics** | Functional | -30° to +70° elevation |
| **Dual connectivity** | Interface | Operational flexibility |

### 6.3 SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
| Lightest armed RCWS | Limited caliber (max 7.62) |
| Proven FCS technology | Magazine capacity constraint |
| Rapid deployment | Requires external power |
| C-UAS optimized | Limited armor penetration |
| UGV/vehicle agnostic | Sensor-to-shooter dependency |

| Opportunities | Threats |
|---------------|---------|
| Growing C-UAS market | Larger caliber C-UAS systems |
| UGV proliferation | Directed energy alternatives |
| Network warfare | Electronic warfare vulnerabilities |
| Low-cost platforms | Competition from drone interceptors |

---

## 7. Technology Gap Analysis (vs V-SMASH RCWS)

### 7.1 Capability Comparison

| Capability | SMASH Hopper | V-SMASH RCWS Target | Gap |
|------------|--------------|---------------------|-----|
| Weight | 15 kg | ≤15 kg | ✓ Match |
| Caliber | 5.56-7.62mm | 5.56-7.62mm | ✓ Match |
| FCS | Gen 3 AI | Equivalent | **Close gap** |
| Thermal | Optional | Standard | ✓ Better |
| Slew Rate | 40°/sec | ≥40°/sec | ✓ Match |
| Elevation | -30° to +70° | -30° to +70° | ✓ Match |
| C2 | Proprietary | Open (CoT) | ✓ Better |
| Local Content | 0% | ≥60% | **Key differentiator** |
| Cost | ~$50-80K | ≤$12K | **Major advantage** |

### 7.2 Critical Technologies to Develop

| Technology | Priority | Approach |
|------------|----------|----------|
| **Precision servo drives** | HIGH | Local manufacture |
| **Position encoders** | HIGH | Import initially |
| **Recoil management** | MEDIUM | Design for 7.62mm |
| **Wireless datalink** | HIGH | Encrypted, low-latency |
| **C2 integration (CoT)** | HIGH | Open standard |
| **Ruggedization** | MEDIUM | MIL-STD-810G target |

---

## 8. Application to V-SMASH

### 8.1 Proposed Requirements (from Hopper Analysis)

| Req ID | Category | Requirement | D/W | Source |
|--------|----------|-------------|-----|--------|
| **R92** | Platform | RCWS total weight ≤15 kg (excl. weapon) | D | Hopper benchmark |
| **R93** | Platform | Slew rate 0.1-40°/sec variable | D | Hopper spec |
| **R94** | Platform | Elevation range -30° to +70° | D | C-UAS optimization |
| **R95** | Platform | Azimuth 360° continuous | D | Full coverage |
| **R96** | Performance | Max acceleration ≥100°/sec² | D | Fast target acquisition |
| **R97** | Interface | Dual connectivity (wired + wireless) | D | Operational flexibility |
| **R98** | Integration | Radar/C2 cue acceptance | D | SMASH DOME concept |
| **R99** | Environment | Operating temp -10°C to +55°C | D | Vietnam adjusted |

### 8.2 V-SMASH RCWS Design Implications

```
V-SMASH RCWS Architecture (Informed by Hopper):

┌─────────────────────────────────────────────────────────────┐
│                    V-SMASH RCWS (~15 kg)                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ V-SMASH PRO │  │  PAN-TILT   │  │  WEAPON INTERFACE   │ │
│  │    FCS      │──│    HEAD     │──│  • M4/M16 (5.56)   │ │
│  │  (Core)     │  │  (Local)    │  │  • Galil (7.62)    │ │
│  │             │  │             │  │  • Quick-change    │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│                          │                                  │
│                          ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              CONTROL & COMMUNICATIONS                │  │
│  │  • Wired (fiber/CAT6)                                │  │
│  │  • Wireless (AES-256 encrypted)                      │  │
│  │  • CoT protocol (ATAK compatible)                    │  │
│  │  • External cue interface (radar, C2)                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  Vietnam Advantages:                                        │
│  • Open CoT vs proprietary SMASH networking                │
│  • Galil 7.62 compatibility (VN standard)                  │
│  • Local servo/mechanical manufacture                       │
│  • $12K target vs $50-80K Hopper                           │
└─────────────────────────────────────────────────────────────┘
```

### 8.3 Mounting Platform Concepts

| Platform | Application | Notes |
|----------|-------------|-------|
| **Tripod** | Forward positions, checkpoints | Rapid deploy |
| **Mast** | Fixed installations, FOBs | Elevated coverage |
| **Light Vehicle** | Toyota technical, pickup | Popular in VN |
| **Armored Vehicle** | M113, BTR variants | VN inventory |
| **UGV** | Roboteam-type platform | Future capability |
| **Naval** | Patrol boat, coastal | IP68 variant |

---

## 9. D-M-I-R Learning Alignment

### 9.1 **D**escribe - What We Learned

1. **Ultra-light RCWS is viable** - 15 kg creates new market segment
2. **FCS is the differentiator** - Same tech from handheld to RCWS
3. **C-UAS driving requirements** - Elevation, slew rate optimized for drones
4. **Person-in-loop mandatory** - All systems require operator confirmation
5. **Network-centric operations** - C2 integration essential
6. **UGV integration emerging** - Future growth vector

### 9.2 **M**odel - Mental Models Updated

```
RCWS Design Philosophy:
┌────────────────────────────────────────────────────────────┐
│  Traditional: Heavy platform → Add sensors → Add control   │
│                                                            │
│  SMASH Approach: FCS first → Minimal platform → Network   │
│                                                            │
│  V-SMASH Approach: FCS core → Open ecosystem → Local mfg  │
└────────────────────────────────────────────────────────────┘
```

### 9.3 **I**ntegrate - Design Decisions

| Decision | Rationale |
|----------|-----------|
| 15 kg weight target | Match benchmark, enable UGV |
| 360° × 100° coverage | Full hemisphere for C-UAS |
| Dual connectivity | Redundancy, flexibility |
| Open CoT protocol | vs proprietary SMASH networking |
| Local servo manufacture | Key cost reduction |

### 9.4 **R**eflect - Lessons for V-SMASH

1. **FCS-first approach validated** - Core technology drives product family
2. **Weight discipline critical** - Enables new platform options
3. **C-UAS is primary market** - Design for drone threats
4. **Open standards advantage** - Interoperability over lock-in
5. **Cost is competitive weapon** - $12K vs $80K = market capture

---

## 10. References

### Sources
- [Smart Shooter Official - SMASH Hopper 5000](https://www.smart-shooter.com/gun/smash-hopper-3/)
- [Army Recognition - SMASH Hopper LRCWS Launch](https://armyrecognition.com/archives/archives-land-defense/land-defense-2020/smart-shooter-launches-smash-hopper-lrcws-light-remote-controlled-weapon-station)
- [Military Leak - SMASH Hopper Specifications](https://militaryleak.com/2023/06/28/smartshooters-smash-hopper-light-remote-controlled-weapon-station/)
- [Unmanned Systems Technology - Roboteam UGV Integration](https://www.unmannedsystemstechnology.com/2022/06/roboteam-ugv-integrated-with-smartshooter-smash-technology/)
- [Defense Advancement - Tactical Ground Robot with SMASH](https://www.defenseadvancement.com/news/tactical-ground-robot-now-integrated-with-smash-technology/)
- [Unmanned Airspace - SMASH DOME C-UAS](https://www.unmannedairspace.info/counter-uas-systems-and-policies/smartshooter-develops-portable-layered-c-uas/)
- [EDR Magazine - SMASH DOME Layered C-UAS](https://www.edrmagazine.eu/smartshooter-unveils-smash-dome-a-layered-cuas-solution-for-area-defense-and-force-protection)

### Related V-SMASH Documents
- [[V-SMASH_RE_06_SMASH_connectivity_analysis]] - Ecosystem context
- [[V-SMASH_P2_06_product_portfolio_v2]] - V-SMASH RCWS positioning
- [[V-SMASH_P1_01_requirements_list]] - Requirements integration

---

## Appendix A: SMASH Product Family Summary

| Product | Type | Weight | Caliber | Key Feature |
|---------|------|--------|---------|-------------|
| SMASH 2000L | Clip-on FCS | 740g | Any rifle | Lightest |
| SMASH 3000 | Clip-on FCS | ~1 kg | Any rifle | Enhanced |
| SMASH X4 | Integrated scope | ~1.5 kg | Any rifle | 4× magnified |
| **SMASH Hopper** | LRCWS | 15 kg | 5.56-7.62 | Remote weapon |
| SMASH HMG | FCS for HMG | ~1.5 kg | 12.7mm | Heavy mount |
| SMASH DOME | C-UAS system | System | Various | Integrated defense |

---

*Analysis complete. 8 new requirements proposed (R92-R99) for V-SMASH RCWS variant.*
