---
project: V-SMASH
phase: 2
type: reverse-engineering
subject: SMASH Dragon Armed UAV Payload
version: 1.0
created: 2026-02-04
status: complete
methodology: D-M-I-R aligned
---

# V-SMASH RE-03: SMASH Dragon Armed UAV Analysis

## 1. System Identification

| Attribute | Value |
|-----------|-------|
| **Product** | SMASH Dragon |
| **Manufacturer** | Smart Shooter Ltd. (Israel) |
| **Category** | Armed UAV Weapon Payload |
| **Generation** | 1st Gen |
| **First Unveiled** | January 2022 |
| **Status** | Advanced Development (live-fire tested) |
| **Primary Mission** | Air-to-air C-UAS, Air-to-ground precision strike |

### Market Positioning

```
ARMED UAV MARKET SEGMENTATION:
┌─────────────────────────────────────────────────────────────────┐
│  LARGE ARMED UAV (MALE/HALE Class)                             │
│  ├── MQ-9 Reaper, Bayraktar TB2                                │
│  ├── Missiles, guided bombs                                     │
│  └── Strategic/operational level                                │
├─────────────────────────────────────────────────────────────────┤
│  MEDIUM ARMED UAV (Tactical)                                    │
│  ├── Loitering munitions (Switchblade, Harop)                  │
│  ├── One-way attack drones                                      │
│  └── Squad/platoon level                                        │
├─────────────────────────────────────────────────────────────────┤
│  SMALL ARMED UAV (Micro-tactical) ← SMASH DRAGON SEGMENT       │
│  ├── SMASH Dragon (reusable, rifle-armed)                      │
│  ├── Precision strike + C-UAS dual role                        │
│  └── Squad level, low cost per engagement                       │
└─────────────────────────────────────────────────────────────────┘
```

**Key Differentiator**: Reusable armed drone with FCS-enhanced precision (not expendable)

---

## 2. System Architecture

### 2.1 SMASH Dragon Concept

```
SMASH DRAGON SYSTEM ARCHITECTURE:

┌─────────────────────────────────────────────────────────────────┐
│                    SMASH DRAGON SYSTEM                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                   UAV PLATFORM                             │ │
│  │  (Hexacopter or other multi-rotor / fixed-wing)           │ │
│  │                                                            │ │
│  │  • Flight controller                                       │ │
│  │  • Navigation (GPS/INS)                                    │ │
│  │  • Datalink (C2 + video)                                   │ │
│  │  • Power system (battery)                                  │ │
│  └───────────────────────────────────────────────────────────┘ │
│                          │                                      │
│                          │ Payload interface                    │
│                          ▼                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              SMASH DRAGON PAYLOAD                          │ │
│  │                                                            │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐   │ │
│  │  │ STABILIZED  │  │   SMASH     │  │    WEAPON       │   │ │
│  │  │   GIMBAL    │──│    FCS      │──│   INTERFACE     │   │ │
│  │  │             │  │             │  │                 │   │ │
│  │  │ • 2/3-axis  │  │ • Computer  │  │ • Rifle mount   │   │ │
│  │  │ • Damping   │  │   vision    │  │ • Trigger mech  │   │ │
│  │  │ • Position  │  │ • Tracking  │  │ • Recoil mgmt   │   │ │
│  │  │   feedback  │  │ • Ballistic │  │                 │   │ │
│  │  └─────────────┘  └─────────────┘  └─────────────────┘   │ │
│  │                          │                                │ │
│  │                          ▼                                │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │              SENSOR PAYLOAD                          │ │ │
│  │  │  • Day camera (SMASH Dragon sight)                   │ │ │
│  │  │  • Optional thermal                                   │ │ │
│  │  │  • Target acquisition + tracking                      │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              GROUND CONTROL STATION                        │ │
│  │  • Remote operator                                         │ │
│  │  • Video feed display                                      │ │
│  │  • Target designation                                      │ │
│  │  • Fire authorization                                      │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Breakdown

| Component | Function | Key Feature |
|-----------|----------|-------------|
| **UAV Platform** | Flight, navigation | Hexacopter (prototype) |
| **Stabilized Gimbal** | Isolate weapon from platform motion | Unique stabilization concept |
| **SMASH FCS** | Target tracking, ballistics | Computer vision, AI |
| **SMASH Dragon Sight** | Target acquisition, video | Day/night capable |
| **Weapon Interface** | Mount, trigger, recoil | Multi-weapon compatible |
| **GCS** | Remote operation | Operator-in-loop |

### 2.3 Weapon Compatibility

| Weapon Type | Caliber | Application |
|-------------|---------|-------------|
| **Assault Rifle** | 5.56mm NATO | Anti-personnel, C-sUAS |
| **Battle Rifle** | 7.62mm NATO | Extended range, light vehicles |
| **Sniper Rifle** | 7.62mm+ | Precision strike |
| **Grenade Launcher** | 40mm | Area effect, fortifications |

---

## 3. External Characterization

### 3.1 Physical Specifications (Estimated)

| Parameter | Estimate | Basis |
|-----------|----------|-------|
| **Payload Weight** | 3-5 kg | "Extremely lightweight" emphasis |
| **Weapon Weight** | 3-4 kg | M4/rifle typical |
| **Total Armed** | 6-9 kg | Payload + weapon + ammo |
| **UAV MTOW** | 15-25 kg | Hexacopter class |

### 3.2 Performance Characteristics

| Parameter | Estimate | Notes |
|-----------|----------|-------|
| **Endurance** | 20-40 min | "Long mission endurance" |
| **Operating Altitude** | 50-300m AGL | Tactical engagement |
| **Engagement Range** | 100-300m | Air-to-ground |
| **C-UAS Range** | 50-200m | Air-to-air |
| **Hit Probability** | >80% | FCS-enhanced (estimate) |

### 3.3 Operational Modes

| Mode | Description | Target Type |
|------|-------------|-------------|
| **Air-to-Ground** | Precision strike from hover/orbit | Personnel, vehicles, positions |
| **Air-to-Air (C-UAS)** | Intercept hostile drones | Group 1-2 UAS |
| **Overwatch** | Loiter and observe, engage on command | Opportunity targets |
| **Escort** | Protect friendly forces/convoys | Threats to protected asset |

---

## 4. Functional Reconstruction

### 4.1 Primary Functions

```
F0: PROVIDE AIRBORNE PRECISION ENGAGEMENT
│
├── F1: FLY to engagement area
│   ├── F1.1: Navigate to coordinates
│   ├── F1.2: Maintain station (loiter)
│   └── F1.3: Maneuver for engagement
│
├── F2: ACQUIRE targets
│   ├── F2.1: Search area (sensor scan)
│   ├── F2.2: Detect potential targets
│   ├── F2.3: Classify target type
│   └── F2.4: Operator designation
│
├── F3: TRACK targets
│   ├── F3.1: Lock target (computer vision)
│   ├── F3.2: Predict target motion
│   ├── F3.3: Maintain track through maneuvers
│   └── F3.4: Handoff between targets
│
├── F4: STABILIZE weapon
│   ├── F4.1: Isolate from platform motion
│   ├── F4.2: Compensate for wind/turbulence
│   ├── F4.3: Point weapon at target
│   └── F4.4: Synchronize fire timing
│
├── F5: ENGAGE target
│   ├── F5.1: Compute ballistic solution
│   ├── F5.2: Verify engagement (operator)
│   ├── F5.3: Fire synchronized shot
│   └── F5.4: Assess hit (BDA)
│
└── F6: COMMUNICATE
    ├── F6.1: Transmit video to GCS
    ├── F6.2: Receive commands
    └── F6.3: Report status/ammunition
```

### 4.2 C-UAS Operating Concept

```
SMASH DRAGON C-UAS ENGAGEMENT:

     HOSTILE DRONE                    SMASH DRAGON
          │                                │
          │  Detected by ground sensors    │
          │  or visual acquisition         │
          ▼                                │
     ┌─────────┐                          │
     │ Target  │◄─────────────────────────┤ Intercept vector
     │ Drone   │                          │
     └─────────┘                          │
          │                                │
          │  ~100-200m engagement range   │
          │                                ▼
          │                          ┌─────────┐
          │◄─────── FCS tracking ────│  SMASH  │
          │                          │ DRAGON  │
          ▼                          └────┬────┘
     ┌─────────┐                          │
     │   HIT   │◄─────── Precision shot ──┘
     │ (KILL)  │
     └─────────┘

ADVANTAGE: Reusable interceptor (vs expendable loitering munition)
           Low cost per engagement (~$1-5 ammunition)
```

### 4.3 Air-to-Ground Operating Concept

```
PRECISION STRIKE MISSION:

                    ┌─────────────────┐
                    │  SMASH DRAGON   │
                    │  (Overwatch)    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
         [Target 1]    [Target 2]    [Target 3]
              │              │              │
              │   Operator selects target   │
              │              ▼              │
              │    ┌─────────────────┐     │
              │    │ FCS tracks and  │     │
              │    │ computes shot   │     │
              │    └────────┬────────┘     │
              │             │              │
              │             ▼              │
              │    ┌─────────────────┐     │
              │    │ Precision shot  │     │
              │    │ (stabilized)    │     │
              │    └─────────────────┘     │
              │                            │

BENEFIT: Multiple engagements from single platform
         Reduced collateral damage (precision)
         Persistent presence (vs one-shot loitering munition)
```

---

## 5. Technology Analysis

### 5.1 Key Technologies

| Technology | Implementation | Innovation Level |
|------------|----------------|------------------|
| **Stabilized Gimbal** | 2/3-axis mechanical + electronic | Incremental |
| **Computer Vision** | SMASH target tracking algorithms | Core competency |
| **Ballistic Computer** | Real-time solution with motion comp | Core competency |
| **Weapon Integration** | Universal rifle mount | Incremental |
| **Platform Agnostic** | Modular payload design | Architectural |

### 5.2 Technical Challenges

| Challenge | Difficulty | SMASH Solution |
|-----------|------------|----------------|
| **Platform Stability** | HIGH | Advanced gimbal + timing |
| **Recoil Management** | HIGH | Dampened mount, timing |
| **Weight Constraint** | MEDIUM | "Extremely lightweight" design |
| **Target Tracking (Air)** | HIGH | Computer vision AI |
| **Ballistics (Moving)** | HIGH | SMASH FCS algorithms |

### 5.3 Comparison: SMASH Dragon vs Alternatives

| System | Type | Cost/Engagement | Reusable | Precision |
|--------|------|-----------------|----------|-----------|
| **SMASH Dragon** | Armed drone | ~$1-5 | YES | HIGH (FCS) |
| **Switchblade 300** | Loitering munition | ~$6,000 | NO | HIGH |
| **Coyote** | Interceptor drone | ~$10-100K | NO | MEDIUM |
| **FPV Kamikaze** | Attack drone | ~$500-2K | NO | LOW-MED |
| **Armed Quadcopter** | Commercial armed | ~$1-10 | YES | LOW |

---

## 6. Design Philosophy Analysis

### 6.1 Core Design Principles

| Principle | Implementation | Rationale |
|-----------|----------------|-----------|
| **FCS-First** | Same SMASH technology | Core competency leverage |
| **Platform Agnostic** | Modular payload | Multiple UAV integration |
| **Lightweight** | Minimal structure | Endurance, cost |
| **Reusable** | Not expendable | Economics, sustainability |
| **Multi-Role** | C-UAS + strike | Platform utilization |
| **Operator-in-Loop** | Remote human control | ROE/IHL compliance |

### 6.2 Innovation Assessment

| Innovation | Type | Impact |
|------------|------|--------|
| **FCS on UAV** | Application | New capability category |
| **Airborne stabilization** | Functional | Enables precision |
| **Rifle-armed drone** | Architectural | Reusable economics |
| **C-UAS role** | Application | Dual-use value |
| **Platform agnostic** | Interface | Market flexibility |

### 6.3 SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
| Reusable (low cost/shot) | Limited payload capacity |
| FCS precision | Short range vs missiles |
| Multi-role capable | Weather dependent |
| Platform flexibility | Endurance limited |
| Low collateral damage | Single weapon |

| Opportunities | Threats |
|---------------|---------|
| Growing C-UAS market | Counter-drone systems |
| Squad-level armed UAV | Regulations/restrictions |
| Export potential | Competition from loitering munitions |
| Naval applications | EW/jamming vulnerabilities |

---

## 7. Technology Gap Analysis (vs V-SMASH)

### 7.1 V-SMASH UAV Application Concept

Based on SMASH Dragon analysis, V-SMASH could develop an armed UAV payload:

```
V-SMASH DRAGON CONCEPT:

┌─────────────────────────────────────────────────────────────────┐
│                  V-SMASH DRAGON PAYLOAD                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              V-SMASH PRO FCS CORE                        │   │
│  │  • Same sensor/processor as handheld                     │   │
│  │  • Computer vision tracking                              │   │
│  │  • Ballistic computation                                 │   │
│  │  • Day/night capability (with thermal option)            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │           LOCAL STABILIZATION SYSTEM                     │   │
│  │  • 2-axis gimbal (local manufacture)                     │   │
│  │  • Vibration isolation                                   │   │
│  │  • Position encoders                                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                          │                                      │
│                          ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              WEAPON INTERFACE                            │   │
│  │  • M16/Galil mount (VN standard)                        │   │
│  │  • Electronic trigger                                    │   │
│  │  • Recoil dampening                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Vietnam Advantages:                                            │
│  • Leverage existing V-SMASH FCS development                   │
│  • Local UAV industry growing                                   │
│  • Low-cost C-UAS capability                                    │
│  • Not dependent on expensive loitering munitions              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Development Priority Assessment

| Capability | Priority | Rationale |
|------------|----------|-----------|
| **Handheld FCS** | HIGHEST | Foundation for all products |
| **RCWS** | HIGH | Ground-based C-UAS primary |
| **Armed UAV** | MEDIUM | Future capability |
| **UAV Payload** | LOW (now) | After RCWS proven |

**Recommendation**: Armed UAV capability should follow successful RCWS development, as core FCS and stabilization technologies are shared.

### 7.3 Proposed Requirements (from Dragon Analysis)

| Req ID | Category | Requirement | D/W | Source |
|--------|----------|-------------|-----|--------|
| **R116** | UAV | FCS payload weight ≤5 kg | W | Dragon benchmark |
| **R117** | UAV | Stabilized gimbal for airborne use | W | Core technology |
| **R118** | UAV | Air-to-air tracking capability | W | C-UAS role |
| **R119** | UAV | Platform-agnostic interface | W | Flexibility |
| **R120** | UAV | Recoil management for airborne fire | W | Precision requirement |

*Note: UAV requirements marked as Wishes (W) - future development phase*

---

## 8. Application to V-SMASH

### 8.1 Product Roadmap Implications

```
V-SMASH DEVELOPMENT PHASES:

PHASE 1: HANDHELD FCS (Current Focus)
├── LITE, PRO, PRO-X
└── Core technology validation

PHASE 2: PLATFORM-MOUNTED (Near-term)
├── HMG, MARITIME
├── RCWS, RCWS-LITE
└── Stabilization technology

PHASE 3: INTEGRATED SYSTEMS (Medium-term)
├── C4I HUB
├── V-SMASH DOME
└── Network integration

PHASE 4: UAV APPLICATIONS (Future)          ← SMASH Dragon equivalent
├── V-SMASH DRAGON payload
├── Armed UAV integration
└── Airborne C-UAS capability
```

### 8.2 Technology Transfer Path

| Technology | Source Phase | Application to UAV |
|------------|--------------|-------------------|
| **FCS Core** | Phase 1 (Handheld) | Direct transfer |
| **Computer Vision** | Phase 1 (PRO) | Direct transfer |
| **Stabilization** | Phase 2 (RCWS) | Adapt for gimbal |
| **C2 Integration** | Phase 3 (C4I) | Datalink interface |
| **Airborne Mount** | Phase 4 (New) | New development |

### 8.3 Vietnam UAV Ecosystem Alignment

| Local Capability | Status | V-SMASH Integration |
|------------------|--------|---------------------|
| **Multi-rotor UAV** | Growing | Platform partners |
| **Fixed-wing UAV** | Emerging | Future platforms |
| **GCS/Datalink** | Available | Interface development |
| **Gimbal/Stabilization** | Limited | Technology gap |
| **FCS** | V-SMASH developing | Core product |

---

## 9. D-M-I-R Learning Alignment

### 9.1 **D**escribe - What We Learned

1. **FCS scales to airborne** - Same SMASH technology works on UAV
2. **Stabilization is critical** - Unique challenge for airborne weapons
3. **Reusable economics** - vs expendable loitering munitions
4. **Multi-role value** - C-UAS + strike from one platform
5. **Platform agnostic design** - Payload concept enables flexibility
6. **Weight is paramount** - Directly impacts endurance

### 9.2 **M**odel - Mental Models Updated

```
ARMED UAV DESIGN APPROACH:

Traditional: UAV first → Add weapon → Hope for accuracy
             (Platform-driven)

SMASH Dragon: FCS first → Stabilization → Any platform
              (Capability-driven)

V-SMASH:     FCS core → Ground validation → Airborne adaptation
             (Phased capability building)
```

### 9.3 **I**ntegrate - Design Decisions

| Decision | Rationale |
|----------|-----------|
| UAV as Phase 4 | After ground systems proven |
| Shared FCS core | Development efficiency |
| RCWS stabilization first | Technology stepping stone |
| Local UAV partnerships | Platform access |
| Rifle-based weapon | Ammunition logistics |

### 9.4 **R**eflect - Lessons for V-SMASH

1. **FCS is the product** - Platform is secondary
2. **Airborne is harder** - Stabilization technology key
3. **Ground first, air later** - De-risk with RCWS
4. **Reusable is smart** - Economic sustainability
5. **Vietnam UAV industry** - Partnership opportunity
6. **C-UAS driving demand** - Both ground and air needed

---

## 10. References

### Sources
- [Defense Update - SMASH Dragon Unveiling](https://defense-update.com/20220110_smash-dragon.html)
- [Army Recognition - SMASH Dragon Development](https://www.armyrecognition.com/focus-analysis-conflicts/army/defence-security-industry-technology/smart-shooter-from-israel-develops-smash-dragon-armed-drone-to-counter-other-uavs)
- [sUAS News - SMASH Dragon UAV Configuration](https://www.suasnews.com/2022/01/smart-shooters-smash-technology-now-also-in-uav-configuration-smash-dragon/)
- [Asia Pacific Defence Reporter - SMASH Dragon Launch](https://asiapacificdefencereporter.com/smart-shooters-launches-smash-dragon-uav/)
- [Unmanned Airspace - Counter-UAS Drone](https://www.unmannedairspace.info/counter-uas-systems-and-policies/drone-equipped-with-smart-shooter-counter-uas-technology-can-take-out-hostile-drones/)

### Related V-SMASH Documents
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis]] - Ground RCWS (shared tech)
- [[V-SMASH_RE_09_SMASH_DOME_analysis]] - C-UAS system integration
- [[V-SMASH_P2_06_product_portfolio_v2]] - Product family context

---

## Appendix A: Armed UAV Comparison Matrix

| System | Platform | Weapon | Reusable | Cost Est. | Precision |
|--------|----------|--------|----------|-----------|-----------|
| **SMASH Dragon** | Hexacopter | Rifle | YES | ~$50-100K | HIGH |
| **Switchblade 300** | Fixed-wing | Warhead | NO | ~$6K/shot | HIGH |
| **Switchblade 600** | Fixed-wing | Warhead | NO | ~$50K/shot | HIGH |
| **Coyote Block 2** | Fixed-wing | Warhead | NO | ~$10-100K | MED |
| **Hero-30** | Fixed-wing | Warhead | NO | ~$15K/shot | HIGH |
| **Commercial Armed** | Quadcopter | Various | YES | ~$5-20K | LOW |

---

## Appendix B: V-SMASH Product Family (10 Products - Future)

| Product | Type | Phase | Status |
|---------|------|-------|--------|
| **LITE** | Handheld FCS | 1 | Development |
| **PRO** | Handheld FCS | 1 | Development |
| **PRO-X** | Magnified FCS | 1 | Development |
| **HMG** | Heavy mount FCS | 2 | Planned |
| **MARITIME** | Naval FCS | 2 | Planned |
| **RCWS-LITE** | Ultra-light RCWS | 2 | Planned |
| **RCWS** | Full RCWS | 2 | Planned |
| **C4I HUB** | Network node | 3 | Planned |
| **DOME** | Integrated C-UAS | 3 | Planned |
| **DRAGON** | UAV payload | 4 | Future |

---

*Analysis complete. 5 new requirements proposed (R116-R120) for future V-SMASH UAV capability.*
