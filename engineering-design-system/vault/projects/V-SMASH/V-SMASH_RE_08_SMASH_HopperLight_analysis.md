---
project: V-SMASH
phase: 2
type: reverse-engineering
subject: SMASH Hopper Light Ultra-Light RCWS
version: 1.0
created: 2026-02-04
status: complete
methodology: D-M-I-R aligned
---

# V-SMASH RE-08: SMASH Hopper Light Analysis

## 1. System Identification

| Attribute | Value |
|-----------|-------|
| **Product** | SMASH Hopper Light |
| **Manufacturer** | Smart Shooter Ltd. (Israel) |
| **Category** | Ultra-Light RCWS (Single-Soldier) |
| **Generation** | Latest (AUSA 2025) |
| **First Unveiled** | 2020 (concept), Enhanced 2025 |
| **Status** | Production |
| **Primary Mission** | Covert ops, ambush, temporary perimeters |

### Market Positioning: Hopper Family

```
SMASH Hopper Product Line:
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  SMASH HOPPER 5000 (~15 kg)                                    │
│  ├── 2-person portable                                          │
│  ├── Full-featured LRCWS                                        │
│  ├── Enhanced Night Vision option                               │
│  └── Vehicle/UGV primary platform                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SMASH HOPPER LIGHT (~8-10 kg est.) ← THIS ANALYSIS            │
│  ├── SINGLE-SOLDIER portable                                    │
│  ├── Smaller, lower profile                                     │
│  ├── Covert operations optimized                                │
│  └── Dismounted squad primary platform                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Differentiator**: Only RCWS designed for single-soldier carry, assembly, and operation

---

## 2. External Characterization

### 2.1 Physical Specifications (Estimated)

| Parameter | Hopper Light | Hopper 5000 | Basis |
|-----------|--------------|-------------|-------|
| **System Weight** | ~8-10 kg | ~15 kg | Single-soldier requirement |
| **Total Weight** | ≤15 kg | ≤25 kg | With weapon + ammo |
| **Form Factor** | Compact, low-profile | Standard pan-tilt | Covert ops design |
| **Portability** | **1-person** | 2-person | Key differentiator |
| **Setup** | Single operator | Crew served | Mission flexibility |

### 2.2 Operational Concept

```
SINGLE-SOLDIER DEPLOYMENT CYCLE:

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  CARRY                ASSEMBLE              OPERATE          │
│  ┌────────┐          ┌────────┐           ┌────────┐        │
│  │Backpack│    →     │ <3 min │     →     │ Remote │        │
│  │or carry│          │ setup  │           │ engage │        │
│  │  bag   │          │        │           │        │        │
│  └────────┘          └────────┘           └────────┘        │
│                                                              │
│  Single soldier throughout entire cycle                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 2.3 Design Philosophy: Covert Operations

| Feature | Implementation | Tactical Benefit |
|---------|----------------|------------------|
| **Low Profile** | Reduced height/signature | Concealment |
| **Compact** | Smaller pan-tilt head | Hidden positions |
| **Silent Setup** | Quick-release mounts | No assembly noise |
| **Single Op** | One-man system | Smaller footprint |

### 2.4 Weapon Compatibility

| Weapon | Caliber | Suitability |
|--------|---------|-------------|
| **M4/M4A1** | 5.56×45mm NATO | Primary (lighter) |
| **SR25** | 7.62×51mm NATO | Extended range |
| **Any AR-style** | 5.56-7.62mm | Platform agnostic |

---

## 3. Subsystem Decomposition

### 3.1 Functional Architecture (Simplified vs Hopper 5000)

```
┌────────────────────────────────────────────────────────────────┐
│                  SMASH HOPPER LIGHT                            │
│              (Optimized for Single Soldier)                    │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────┐    ┌──────────────┐    ┌────────────────┐   │
│  │   SENSOR     │    │     FCS      │    │   EFFECTOR     │   │
│  │  (Compact)   │───▶│  (Same as    │───▶│  (Lightweight) │   │
│  │              │    │   Hopper)    │    │                │   │
│  │ • Day camera │    │ • SMASH core │    │ • Light cradle │   │
│  │ • (No thermal│    │ • AI/ML      │    │ • M4 optimized │   │
│  │   standard)  │    │ • Tracking   │    │                │   │
│  └──────────────┘    └──────────────┘    └────────────────┘   │
│                             │                                  │
│                             ▼                                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              COMPACT PAN-TILT HEAD                        │ │
│  │  • Reduced range of motion (trade-off)                    │ │
│  │  • Lighter servo motors                                   │ │
│  │  • Lower profile design                                   │ │
│  └──────────────────────────────────────────────────────────┘ │
│                             │                                  │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              PORTABLE CONTROL UNIT                        │ │
│  │  • Handheld RCU                                          │ │
│  │  • Wired primary (weight savings)                        │ │
│  │  • Wireless optional                                      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 3.2 Weight Reduction Analysis

| Subsystem | Hopper 5000 | Hopper Light Est. | Reduction Method |
|-----------|-------------|-------------------|------------------|
| **Pan-Tilt** | ~5 kg | ~3 kg | Smaller servos |
| **Structure** | ~4 kg | ~2.5 kg | Aluminum/composite |
| **FCS Unit** | ~2 kg | ~2 kg | Same core |
| **Sensors** | ~2 kg | ~1 kg | Day-only standard |
| **Control** | ~2 kg | ~1.5 kg | Simplified RCU |
| **TOTAL** | ~15 kg | ~10 kg | -33% reduction |

### 3.3 Capability Trade-offs

| Capability | Hopper 5000 | Hopper Light | Trade-off Rationale |
|------------|-------------|--------------|---------------------|
| **Night Vision** | Enhanced option | Day-only std | Weight reduction |
| **Slew Rate** | 40°/sec | ~30°/sec est. | Smaller motors |
| **Elevation** | -30° to +70° | -20° to +60° est. | Compact design |
| **Azimuth** | 360° | 270-300° est. | Low-profile head |
| **Endurance** | Vehicle power | Battery capable | Portability |
| **C2 Integration** | Full | Basic | Simplified |

---

## 4. Operational Scenarios

### 4.1 Primary Use Cases

```
SCENARIO 1: SQUAD AMBUSH POSITION
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [Squad Leader] ──────────────────────┐                     │
│       │                                │                     │
│       │  "Set up overwatch"            │                     │
│       ▼                                ▼                     │
│  [Hopper Light]                   [Squad positions]          │
│       │                                                      │
│       │  • Soldier carries to position                       │
│       │  • Assembles in <3 min                               │
│       │  • Operates remotely from cover                      │
│       │  • Provides precision fire support                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘

SCENARIO 2: TEMPORARY DEFENSIVE PERIMETER
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│         [Hopper Light]                                       │
│              │                                               │
│              │  Auto-scan sector                             │
│              ▼                                               │
│    ┌─────────────────────┐                                  │
│    │                     │                                  │
│    │   [Resting Squad]   │  ← Single soldier on watch       │
│    │                     │    operates Hopper remotely      │
│    └─────────────────────┘                                  │
│                                                              │
│  Benefit: One soldier provides security for entire squad    │
│                                                              │
└──────────────────────────────────────────────────────────────┘

SCENARIO 3: COVERT OBSERVATION POST
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [Low-profile Hopper Light]                                 │
│           │                                                  │
│           │  Concealed position                              │
│           │  • Reduced visual signature                      │
│           │  • Silent operation                              │
│           │  • Rapid displacement                            │
│           ▼                                                  │
│  [Operator in cover] ←── 50-100m standoff                   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 4.2 Deployment Flexibility

| Platform | Hopper 5000 | Hopper Light |
|----------|-------------|--------------|
| **Tripod (ground)** | ✓ | ✓ Primary |
| **Vehicle mount** | ✓ Primary | ✓ Capable |
| **Fixed mast** | ✓ | Limited |
| **UGV** | ✓ | ✓ Ideal (weight) |
| **Backpack carry** | ✗ | ✓ Designed for |
| **Covert positions** | Limited | ✓ Optimized |

---

## 5. Performance Estimation

### 5.1 Engagement Performance (Estimated)

| Metric | Hopper Light Est. | Hopper 5000 | Notes |
|--------|-------------------|-------------|-------|
| **Effective Range** | 300-500m | 300-600m | Same FCS |
| **Hit Probability** | >90% | >95% | Slightly reduced stability |
| **Drone Engagement** | 150-300m | 200-400m | Reduced elevation |
| **Engagement Time** | 3-6 sec | 2-5 sec | Slower slew |
| **Magazine** | 30 rd (5.56) | Same | M4 standard |

### 5.2 Portability Performance

| Metric | Hopper Light | Hopper 5000 |
|--------|--------------|-------------|
| **Carry Distance** | 5+ km | 1-2 km |
| **Setup Time** | <3 min | <5 min |
| **Pack Size** | Backpack | Duffel/case |
| **Crew Required** | 1 | 2 |
| **Displacement** | <2 min | >3 min |

### 5.3 Comparison Matrix

```
                    PORTABILITY
                         ▲
                         │
           Hopper Light  │
                 ●       │
                         │
                         │
    ─────────────────────┼─────────────────────▶ CAPABILITY
                         │
                         │        ● Hopper 5000
                         │
                         │              ● Traditional RCWS
                         │

    Trade-off: Hopper Light optimizes for PORTABILITY
               over maximum CAPABILITY
```

---

## 6. Design Philosophy Analysis

### 6.1 Core Design Principles

| Principle | Hopper 5000 | Hopper Light |
|-----------|-------------|--------------|
| **Primary Goal** | Maximum capability | Maximum portability |
| **Crew Concept** | Crew-served | Single-soldier |
| **Platform Focus** | Vehicle/UGV | Dismounted infantry |
| **Ops Tempo** | Sustained | Rapid, transient |
| **Signature** | Standard | Minimized |

### 6.2 Innovation Assessment

| Innovation | Impact | V-SMASH Relevance |
|------------|--------|-------------------|
| **Single-soldier RCWS** | New category | HIGH - squad level |
| **Backpack portable** | Tactical flexibility | HIGH - VN terrain |
| **Covert-optimized** | Mission expansion | MEDIUM - ambush |
| **Same FCS core** | Platform commonality | HIGH - product family |
| **Weight <10 kg** | Deployment barrier removal | HIGH - infantry use |

### 6.3 SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
| Single-soldier portable | Reduced capability vs 5000 |
| Rapid deployment | Day-only standard |
| Covert operations | Limited arc coverage |
| Same FCS accuracy | Battery endurance |
| Low cost (simpler) | Not vehicle-optimized |

| Opportunities | Threats |
|---------------|---------|
| Infantry C-UAS gap | Drone swarm tactics |
| Jungle/mountain terrain | Heavier RCWS competition |
| Special operations | RF jamming |
| Border patrol units | Thermal-equipped threats |

---

## 7. Technology Gap Analysis (vs V-SMASH RCWS-LITE)

### 7.1 V-SMASH RCWS Variant Concept

Based on Hopper Light analysis, V-SMASH should consider a **RCWS-LITE** variant:

```
V-SMASH PRODUCT FAMILY (Updated):
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Handheld FCS Tier:                                            │
│  ├── V-SMASH LITE (~$3K)                                       │
│  ├── V-SMASH PRO (~$5K)                                        │
│  └── V-SMASH PRO-X (~$7K)                                      │
│                                                                 │
│  Platform-Mounted Tier:                                         │
│  ├── V-SMASH HMG (~$6K)           ← 12.7mm                     │
│  ├── V-SMASH MARITIME (~$6.5K)    ← IP68 naval                 │
│  ├── V-SMASH RCWS-LITE (~$8K) ← NEW (Single-soldier)          │
│  ├── V-SMASH RCWS (~$12K)         ← Full-featured              │
│  └── V-SMASH C4I HUB (~$2K)       ← Network node               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 V-SMASH RCWS-LITE Specifications (Proposed)

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| **Weight** | ≤10 kg | Single-soldier carry |
| **Setup Time** | <3 min | Rapid deployment |
| **Weapon** | M16/Galil (5.56mm) | VN standard |
| **Slew Rate** | ≥25°/sec | Acceptable trade-off |
| **Elevation** | -20° to +60° | Ground/low drone |
| **Azimuth** | 270° | Frontal arc |
| **Power** | Battery (2hr) + vehicle | Hybrid |
| **Control** | Wired primary | Weight/reliability |
| **Cost** | ≤$8,000 | vs $50K Hopper Light |

### 7.3 Proposed Requirements (from Hopper Light Analysis)

| Req ID | Category | Requirement | D/W | Source |
|--------|----------|-------------|-----|--------|
| **R100** | Platform | RCWS-LITE weight ≤10 kg (excl. weapon) | D | Single-soldier req |
| **R101** | Platform | Single-soldier carry/setup/operate | D | Hopper Light concept |
| **R102** | Platform | Setup time <3 minutes | D | Rapid deployment |
| **R103** | Platform | Backpack/bag transportable | D | Infantry mobility |
| **R104** | Performance | Slew rate ≥25°/sec | W | Trade-off acceptable |
| **R105** | Performance | Elevation -20° to +60° | W | Compact design |
| **R106** | Power | Battery operation ≥2 hours | D | Standalone ops |
| **R107** | Design | Low visual profile | W | Covert ops |

---

## 8. Application to V-SMASH

### 8.1 Vietnam-Specific Advantages of RCWS-LITE

| Factor | Relevance |
|--------|-----------|
| **Jungle terrain** | Vehicle access limited, infantry carries |
| **Mountain border** | Helicopter resupply, light loads critical |
| **Island defense** | Small boat delivery, patrol positions |
| **Budget constraints** | $8K vs $50K enables wider deployment |
| **Squad-level C-UAS** | Drone threat at lowest echelon |

### 8.2 Tactical Employment (Vietnam Context)

```
SCENARIO: BORDER PATROL (Northern Mountains)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [Patrol Base] ──── 5km patrol route ──── [OP Position]     │
│                                                              │
│  Single soldier carries V-SMASH RCWS-LITE in backpack       │
│  Sets up at observation post                                 │
│  Provides overwatch while squad rests                        │
│  Can engage drones or ground threats                         │
│  Rapid displacement if detected                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘

SCENARIO: COASTAL/ISLAND DEFENSE (Spratly)
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  [Small patrol boat] → [Island outpost]                     │
│                                                              │
│  Limited resupply capability                                 │
│  V-SMASH RCWS-LITE: 10 kg vs 50 kg for full RCWS           │
│  Single soldier operates security system                     │
│  Solar + battery power (no vehicle)                          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 8.3 V-SMASH RCWS-LITE Architecture

```
V-SMASH RCWS-LITE (~10 kg, ~$8K):

┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ V-SMASH     │  │  COMPACT    │  │  WEAPON INTERFACE   │ │
│  │ LITE FCS    │──│  PAN-TILT   │──│  • M16A2 (5.56)    │ │
│  │  (Core)     │  │  (~3 kg)    │  │  • Galil (5.56)    │ │
│  │             │  │             │  │  • Quick-release   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│        │                │                                   │
│        │                ▼                                   │
│        │    ┌─────────────────────────────────────────┐    │
│        │    │         LIGHTWEIGHT STRUCTURE            │    │
│        │    │  • Aluminum/composite frame              │    │
│        │    │  • Folding tripod legs                   │    │
│        │    │  • Low-profile design                    │    │
│        └───▶│  • Weight: ~2.5 kg                       │    │
│             └─────────────────────────────────────────┘    │
│                          │                                  │
│  ┌───────────────────────┴────────────────────────────────┐│
│  │              PORTABLE CONTROL SYSTEM                    ││
│  │  • Handheld controller (~500g)                         ││
│  │  • 50m tether (wired primary)                          ││
│  │  • Optional wireless upgrade                            ││
│  │  • Battery pack: LiFePO4 (~1 kg, 2hr)                  ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  Vietnam Advantages:                                        │
│  • M16A2 compatibility (VN inventory)                      │
│  • $8K target vs $50K Hopper Light                         │
│  • Infantry-portable for jungle/mountain                    │
│  • Local aluminum/composite manufacturing                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. D-M-I-R Learning Alignment

### 9.1 **D**escribe - What We Learned

1. **Single-soldier RCWS is achievable** - ~10 kg threshold
2. **Same FCS, different platform** - Core technology scales down
3. **Trade-offs are acceptable** - Reduced arc/speed for portability
4. **Covert ops niche** - Not just smaller, different mission
5. **Infantry-level C-UAS** - Drone defense at squad level
6. **Battery operation viable** - 2+ hours standalone

### 9.2 **M**odel - Mental Models Updated

```
RCWS Weight-Capability Trade-off:

  CAPABILITY
       │
   100%├────────────●  Traditional RCWS (50-200 kg)
       │
    85%├───────●       Hopper 5000 (15 kg)
       │
    70%├──●            Hopper Light / V-SMASH RCWS-LITE (10 kg)
       │
       └───┬───┬───┬───┬───┬───▶ WEIGHT
          10  15  25  50  100    (kg)

Key insight: 70% capability at 10 kg enables entirely new
             deployment scenarios (infantry portable)
```

### 9.3 **I**ntegrate - Design Decisions

| Decision | Rationale |
|----------|-----------|
| Add RCWS-LITE variant | Address infantry C-UAS gap |
| 10 kg target | Single-soldier threshold |
| 5.56mm primary | Weight optimization, VN M16 stock |
| Wired control primary | Simplicity, weight, reliability |
| Battery + vehicle power | Hybrid flexibility |
| Same FCS core | Platform commonality |

### 9.4 **R**eflect - Lessons for V-SMASH

1. **Product family depth** - Need both RCWS and RCWS-LITE
2. **Weight is a feature** - Not just cost, enables new missions
3. **Trade-offs are strategic** - Accept reduced capability for portability
4. **Vietnam terrain advantage** - Jungle/mountain favors lightweight
5. **Cost leverage** - $8K RCWS-LITE vs $50K Hopper Light = 6× units

---

## 10. Hopper Family Complete Summary

### 10.1 Smart Shooter RCWS Portfolio

| Product | Weight | Crew | Primary Platform | Est. Cost |
|---------|--------|------|------------------|-----------|
| **Hopper 5000** | ~15 kg | 2 | Vehicle, UGV | ~$50-80K |
| **Hopper Light** | ~10 kg | 1 | Dismounted infantry | ~$40-60K |

### 10.2 V-SMASH RCWS Portfolio (Proposed)

| Product | Weight | Crew | Primary Platform | Target Cost |
|---------|--------|------|------------------|-------------|
| **V-SMASH RCWS** | ≤15 kg | 2 | Vehicle, UGV | ~$12K |
| **V-SMASH RCWS-LITE** | ≤10 kg | 1 | Dismounted infantry | ~$8K |

**Cost Advantage**: 5-6× more units deployable for same budget

---

## 11. References

### Sources
- [Smart Shooter Official - SMASH Hopper 5000](https://www.smart-shooter.com/gun/smash-hopper-3/)
- [Army Recognition - SMASH Hopper Launch](https://armyrecognition.com/archives/archives-land-defense/land-defense-2020/smart-shooter-launches-smash-hopper-lrcws-light-remote-controlled-weapon-station)
- [Popular Airsoft - Hopper Light Details](https://www.popularairsoft.com/smart-shooters-smash-hopper-light-remote-controlled-weapon-system)
- [Overt Defense - Hopper Unveiling](https://www.overtdefense.com/2020/07/31/smart-shooter-unveils-smash-hopper-remote-controlled-weapon-station/)
- [Soldier Systems Daily - AUSA 2024 Coverage](https://soldiersystems.net/2024/10/02/ausa-smartshooter-combat-proven-smash-fire-control-systems-turn-dismounted-soldiers-into-effective-drone-eliminator/)

### Related V-SMASH Documents
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis]] - Full-size RCWS
- [[V-SMASH_P2_06_product_portfolio_v2]] - Product family update
- [[V-SMASH_P1_01_requirements_list]] - Requirements integration

---

## Appendix A: V-SMASH Product Family (Complete - 8 Products)

| Product | Type | Weight | Target Cost | Primary Market |
|---------|------|--------|-------------|----------------|
| **LITE** | Handheld FCS | 400g | $3K | Militia, reserve |
| **PRO** | Handheld FCS | 800g | $5K | Regular infantry |
| **PRO-X** | Magnified FCS | 1.2kg | $7K | Designated marksman |
| **HMG** | Heavy mount FCS | 1.5kg | $6K | 12.7mm crews |
| **MARITIME** | Naval FCS | 1kg | $6.5K | Patrol boats |
| **RCWS-LITE** | Ultra-light RCWS | 10kg | $8K | Infantry squads |
| **RCWS** | Full RCWS | 15kg | $12K | Vehicles, UGV |
| **C4I HUB** | Network node | 500g | $2K | Squad leaders |

---

*Analysis complete. 8 new requirements proposed (R100-R107) for V-SMASH RCWS-LITE variant.*
