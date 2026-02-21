---
project: V-SMASH
phase: 2
type: reverse-engineering
subject: SMASH DOME Integrated C-UAS System
version: 1.0
created: 2026-02-04
status: complete
methodology: D-M-I-R aligned
---

# V-SMASH RE-09: SMASH DOME Integrated C-UAS Analysis

## 1. System Identification

| Attribute | Value |
|-----------|-------|
| **Product** | SMASH DOME |
| **Manufacturer** | Smart Shooter Ltd. (Israel) |
| **Category** | Integrated Counter-UAS System |
| **Generation** | 1st Gen (Unveiled Jan 2025) |
| **First Unveiled** | 28 January 2025 |
| **Status** | Production, Market Launch |
| **Primary Mission** | Layered area defense against UAS |

### Market Positioning

```
C-UAS MARKET SEGMENTATION:
┌─────────────────────────────────────────────────────────────────┐
│  STRATEGIC / FIXED SITE                                         │
│  ├── Rafael Drone Dome (laser + jammer)     ~$5-10M+           │
│  ├── Raytheon COYOTE (expendable interceptor)                   │
│  └── High-power directed energy systems                         │
├─────────────────────────────────────────────────────────────────┤
│  TACTICAL / MOBILE                                              │
│  ├── MADIS (USMC integrated system)                             │
│  ├── Various vehicle-mounted jammers                            │
│  └── Medium complexity/cost                                     │
├─────────────────────────────────────────────────────────────────┤
│  PORTABLE / SQUAD LEVEL ← SMASH DOME SEGMENT                   │
│  ├── SMASH DOME (detect + kinetic)          ~$100-300K est.    │
│  ├── Lightweight, man-portable                                  │
│  └── Low-cost kinetic (rifle ammunition)                        │
└─────────────────────────────────────────────────────────────────┘
```

**Key Differentiator**: Portable, integrated detect-track-engage C-UAS at squad/platoon level

---

## 2. System Architecture

### 2.1 SMASH DOME Concept

```
SMASH DOME LAYERED C-UAS ARCHITECTURE:

                    DETECTION LAYER (1-2 km)
     ┌──────────────────────────────────────────────────┐
     │                                                  │
     │   ┌─────────────┐       ┌─────────────────┐     │
     │   │  ACTIVE RF  │       │ PASSIVE OPTICAL │     │
     │   │   RADAR     │       │   EO/IR SENSOR  │     │
     │   │             │       │                 │     │
     │   │ • MHR/RPS-42│       │ • Day camera    │     │
     │   │   capable   │       │ • Thermal       │     │
     │   │ • 360° opt  │       │ • VMD/ATR       │     │
     │   └──────┬──────┘       └────────┬────────┘     │
     │          │                       │              │
     │          └───────────┬───────────┘              │
     │                      ▼                          │
     └──────────────────────────────────────────────────┘
                            │
                            │ Target data stream
                            ▼
     ┌──────────────────────────────────────────────────┐
     │              TRACKING LAYER                      │
     │                                                  │
     │   ┌────────────────────────────────────────┐    │
     │   │    SMARTSHOOTER PROPRIETARY            │    │
     │   │         TRACKING SYSTEM                │    │
     │   │                                        │    │
     │   │  • Continuous target monitoring        │    │
     │   │  • Classification (drone type)         │    │
     │   │  • Trajectory prediction               │    │
     │   │  • Threat prioritization               │    │
     │   │  • Handoff to effector                 │    │
     │   └────────────────────────────────────────┘    │
     │                      │                          │
     │                      │ C2 Integration           │
     │                      │ (ATAK compatible)        │
     │                      ▼                          │
     └──────────────────────────────────────────────────┘
                            │
                            │ Engagement command
                            ▼
     ┌──────────────────────────────────────────────────┐
     │              ENGAGEMENT LAYER                    │
     │                                                  │
     │   ┌────────────────────────────────────────┐    │
     │   │         SMASH HOPPER LRCWS             │    │
     │   │                                        │    │
     │   │  • Assault rifle (5.56/7.62mm)         │    │
     │   │  • SMASH Fire Control System           │    │
     │   │  • AI-assisted tracking                │    │
     │   │  • Ballistic solution computation      │    │
     │   │  • Person-in-the-loop trigger          │    │
     │   └────────────────────────────────────────┘    │
     │                                                  │
     │   ENGAGEMENT RANGE: 200-500m (kinetic)          │
     │                                                  │
     └──────────────────────────────────────────────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │  TARGET KILLED  │
                   │   (Hard-kill)   │
                   └─────────────────┘
```

### 2.2 Component Breakdown

| Layer | Component | Function | Specifications |
|-------|-----------|----------|----------------|
| **Detection** | RF Radar | Volume surveillance | Up to 2 km range |
| **Detection** | EO/IR Sensor | Visual/thermal detect | Up to 1-2 km |
| **Tracking** | Proprietary SW | Target management | Real-time processing |
| **C2** | ATAK Interface | Network integration | Standard protocols |
| **Effector** | SMASH Hopper | Kinetic engagement | ~15 kg LRCWS |

### 2.3 Radar Integration Options

| Radar | Type | Range | Coverage | Integration |
|-------|------|-------|----------|-------------|
| **DRS MHR (RPS-42)** | S-band AESA | 10 km (Group 1-2 UAS) | 90° per unit | Proven |
| **Generic radar** | Various | 1-5 km | Various | Open interface |
| **Passive only** | EO/IR | 1-2 km | Sector | Baseline |

---

## 3. Functional Reconstruction

### 3.1 Primary Functions

```
F0: PROVIDE AREA C-UAS DEFENSE
│
├── F1: DETECT UAS threats
│   ├── F1.1: Scan airspace (radar/optical)
│   ├── F1.2: Acquire contact
│   └── F1.3: Classify target (drone vs bird vs clutter)
│
├── F2: TRACK UAS continuously
│   ├── F2.1: Maintain track file
│   ├── F2.2: Predict trajectory
│   ├── F2.3: Estimate time-to-impact
│   └── F2.4: Prioritize multiple threats
│
├── F3: DECIDE engagement
│   ├── F3.1: Apply ROE (Rules of Engagement)
│   ├── F3.2: Verify target (person-in-loop)
│   ├── F3.3: Authorize engagement
│   └── F3.4: Select effector (if multiple)
│
├── F4: ENGAGE target
│   ├── F4.1: Slew weapon to target
│   ├── F4.2: Compute ballistic solution
│   ├── F4.3: Track target motion
│   ├── F4.4: Fire synchronized shot
│   └── F4.5: Assess kill (BDA)
│
└── F5: COMMUNICATE status
    ├── F5.1: Report to higher C2
    ├── F5.2: Share track data (network)
    └── F5.3: Log engagement data
```

### 3.2 Kill Chain Timeline

```
SMASH DOME ENGAGEMENT TIMELINE:

    DETECT        TRACK       DECIDE      ENGAGE       KILL
       │            │            │           │           │
       ▼            ▼            ▼           ▼           ▼
    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
    │ Radar│───▶│Track │───▶│Verify│───▶│ Fire │───▶│ BDA  │
    │ EO/IR│    │Manage│    │Target│    │ FCS  │    │      │
    └──────┘    └──────┘    └──────┘    └──────┘    └──────┘
       │            │            │           │           │
    0-5 sec     1-3 sec      1-2 sec     2-5 sec     1-2 sec
                                                         │
    TOTAL TIMELINE: ~5-15 seconds ◄──────────────────────┘
    (from detection to kill)
```

### 3.3 Operational Modes

| Mode | Description | Sensors Active | Automation |
|------|-------------|----------------|------------|
| **Standby** | Low-power monitoring | Radar only | Full auto detect |
| **Alert** | Threat detected | All sensors | Auto track |
| **Engage** | Target confirmed | All + FCS | Semi-auto (PITL) |
| **Manual** | Operator control | Operator select | None |

---

## 4. Performance Estimation

### 4.1 Detection Performance

| Target Type | RCS (m²) | Detection Range | Classification |
|-------------|----------|-----------------|----------------|
| **Group 1 UAS** (<20 lbs) | 0.001-0.01 | 1-3 km | High confidence |
| **Group 2 UAS** (20-55 lbs) | 0.01-0.1 | 2-5 km | High confidence |
| **FPV drone** | 0.001-0.005 | 0.5-2 km | Medium confidence |
| **Swarm (multiple)** | Various | Degraded | Requires prioritization |

### 4.2 Engagement Performance

| Metric | Value | Notes |
|--------|-------|-------|
| **Effective Range** | 200-500m | Kinetic (rifle) |
| **Pk (single shot)** | ~90% | FCS-enhanced |
| **Pk (burst)** | >95% | 3-5 round burst |
| **Engagement Time** | 5-15 sec | Detect to kill |
| **Rate of Fire** | 2-3 engagements/min | Magazine dependent |
| **Ammunition** | 5.56/7.62mm NATO | Low cost/round |

### 4.3 System Comparison

| System | Detection | Effector | Range | Cost/Kill | Portability |
|--------|-----------|----------|-------|-----------|-------------|
| **SMASH DOME** | Radar + EO | Rifle (kinetic) | 200-500m | ~$1-5 | Portable |
| **Drone Dome** | Radar + EO | Laser + Jammer | 1-3 km | ~$0 (laser) | Vehicle |
| **COYOTE** | KuRFS radar | Interceptor drone | 5+ km | ~$10-100K | Vehicle |
| **MADIS** | Radar | Mixed (missile/gun) | 1-5 km | Various | Vehicle |

### 4.4 Cost Analysis

| Component | Estimated Cost | Notes |
|-----------|----------------|-------|
| **SMASH Hopper** | $50-80K | Core effector |
| **Radar (MHR)** | $100-200K | Optional upgrade |
| **EO/IR sensor** | $20-50K | Baseline detection |
| **C2 software** | $20-30K | Proprietary |
| **Integration** | $20-50K | System integration |
| **TOTAL** | **~$150-400K** | Configuration dependent |

**Cost per engagement**: ~$1-5 (rifle ammunition)

---

## 5. Design Philosophy Analysis

### 5.1 Core Design Principles

| Principle | Implementation | Rationale |
|-----------|----------------|-----------|
| **Layered Defense** | Detect → Track → Engage | Redundancy |
| **Person-in-Loop** | Operator confirms all shots | IHL/ROE compliance |
| **Portable** | Lightweight components | Tactical mobility |
| **Low Cost/Kill** | Rifle ammunition | Sustainable ops |
| **Open Architecture** | ATAK/C2 integration | Interoperability |
| **Modular** | Scalable sensor suite | Mission tailoring |

### 5.2 Innovation Assessment

| Innovation | Type | Impact |
|------------|------|--------|
| **FCS-integrated C-UAS** | Architectural | Unique approach |
| **Portable layered defense** | Parametric | New market segment |
| **Low-cost kinetic** | Economic | Cost-per-kill advantage |
| **Squad-level C-UAS** | Application | Democratized defense |
| **Rifle-based effector** | Functional | Ammo logistics simple |

### 5.3 SWOT Analysis

| Strengths | Weaknesses |
|-----------|------------|
| Portable/lightweight | Limited range (500m) |
| Low cost per kill | Requires LOS |
| PITL (safe) | Weather dependent |
| Scalable sensors | Single effector |
| Combat-proven FCS | Magazine capacity |

| Opportunities | Threats |
|---------------|---------|
| Squad C-UAS gap | Swarm saturation |
| Growing drone threat | Faster/smaller drones |
| Complement to jammers | EW countermeasures |
| Export market | Directed energy systems |

---

## 6. Technology Gap Analysis (vs V-SMASH C-UAS)

### 6.1 V-SMASH C-UAS System Concept

Based on SMASH DOME analysis, V-SMASH should develop an integrated C-UAS capability:

```
V-SMASH C-UAS SYSTEM CONCEPT:

┌─────────────────────────────────────────────────────────────────┐
│                     V-SMASH DOME                                │
│            (Vietnam Indigenous C-UAS System)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  DETECTION LAYER                                                │
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │  RADAR OPTIONS  │    │  EO/IR SENSOR   │                    │
│  │                 │    │                 │                    │
│  │ • Import radar  │    │ • V-SMASH PRO   │ ← Local FCS       │
│  │   (initial)     │    │   sensor head   │                    │
│  │ • Local radar   │    │ • CMOS + LWIR   │                    │
│  │   (future)      │    │ • 1-2 km range  │                    │
│  └────────┬────────┘    └────────┬────────┘                    │
│           │                      │                              │
│           └──────────┬───────────┘                              │
│                      ▼                                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              V-SMASH C4I HUB                              │  │
│  │                                                          │  │
│  │  • CoT protocol (open standard)                          │  │
│  │  • ATAK compatible                                       │  │
│  │  • Track management                                      │  │
│  │  • Threat prioritization                                 │  │
│  │  • Local software development                            │  │
│  └────────────────────────┬─────────────────────────────────┘  │
│                           │                                     │
│                           ▼                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              V-SMASH RCWS / RCWS-LITE                    │  │
│  │                                                          │  │
│  │  • V-SMASH FCS core                                      │  │
│  │  • M16/Galil (5.56mm)                                    │  │
│  │  • Local pan-tilt manufacture                            │  │
│  │  • Person-in-the-loop                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Vietnam Advantages:                                            │
│  • Open CoT protocol (vs proprietary SMASH)                    │
│  • Local manufacturing (60%+ content)                           │
│  • $50-80K target (vs $150-400K SMASH DOME)                    │
│  • Scalable from squad to installation                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 V-SMASH DOME Configuration Options

| Configuration | Components | Target Cost | Application |
|---------------|------------|-------------|-------------|
| **Basic** | EO/IR + RCWS-LITE | ~$20K | Squad C-UAS |
| **Standard** | EO/IR + RCWS | ~$30K | Platoon C-UAS |
| **Enhanced** | Radar + EO/IR + RCWS | ~$80K | Company/FOB |
| **Networked** | Multiple RCWS + C4I HUB | ~$100K+ | Area defense |

### 6.3 Proposed Requirements (from SMASH DOME Analysis)

| Req ID | Category | Requirement | D/W | Source |
|--------|----------|-------------|-----|--------|
| **R108** | C-UAS | Integrated detect-track-engage capability | D | SMASH DOME concept |
| **R109** | C-UAS | Detection range ≥1 km (EO/IR baseline) | D | Portable requirement |
| **R110** | C-UAS | Detect-to-kill time ≤15 seconds | D | Engagement timeline |
| **R111** | C-UAS | Person-in-the-loop engagement | D | IHL compliance |
| **R112** | C-UAS | Track management for ≥3 simultaneous targets | D | Swarm defense |
| **R113** | C-UAS | External radar cue interface | W | Scalability |
| **R114** | C-UAS | ATAK/CoT protocol integration | D | Interoperability |
| **R115** | C-UAS | Cost per engagement ≤$10 | D | Sustainability |

---

## 7. Competitive Analysis

### 7.1 C-UAS Market Landscape

```
C-UAS EFFECTOR COMPARISON:

COST PER KILL
      │
$100K ├────────────────────────●  COYOTE interceptor
      │
 $10K ├──────────────●           Missile (Stinger-type)
      │
  $1K ├────●                     SMASH DOME (rifle)
      │
   $0 ├●                         Laser (Drone Dome)
      │    │    │    │    │    │
      └────┼────┼────┼────┼────┼──▶ RANGE (km)
          0.5   1    2    5   10

Trade-off: Range vs Cost per Kill
SMASH DOME optimizes for LOW COST at SHORT RANGE
```

### 7.2 Layered Defense Integration

```
TYPICAL LAYERED C-UAS DEPLOYMENT:

         LONG RANGE (5-10 km)
    ┌───────────────────────────────┐
    │     MISSILE / INTERCEPTOR    │
    │     (COYOTE, Stinger)        │
    │     High cost, limited shots │
    └───────────────┬───────────────┘
                    │
         MEDIUM RANGE (1-5 km)
    ┌───────────────────────────────┐
    │     DIRECTED ENERGY / EW     │
    │     (Laser, Jammer)          │
    │     Zero cost/shot, LOS req  │
    └───────────────┬───────────────┘
                    │
         SHORT RANGE (0.2-1 km)      ← SMASH DOME
    ┌───────────────────────────────┐
    │     KINETIC (GUN-BASED)      │
    │     Low cost, high Pk        │
    │     Last line of defense     │
    └───────────────────────────────┘

SMASH DOME = "Insurance policy" for when other layers fail
```

### 7.3 Vietnam C-UAS Requirements

| Threat | Current Defense | Gap | V-SMASH Solution |
|--------|-----------------|-----|------------------|
| **Commercial drones** | Small arms | Poor Pk | V-SMASH FCS |
| **FPV attack drones** | None | Critical | V-SMASH DOME |
| **Reconnaissance UAS** | Limited | Significant | Integrated C-UAS |
| **Swarm** | None | Critical | Networked RCWS |

---

## 8. Application to V-SMASH

### 8.1 Product Family Update (9 Products)

```
V-SMASH PRODUCT FAMILY (Complete):

HANDHELD FCS TIER:
├── V-SMASH LITE        $3K     Militia, reserve
├── V-SMASH PRO         $5K     Regular infantry
└── V-SMASH PRO-X       $7K     Designated marksman

PLATFORM-MOUNTED TIER:
├── V-SMASH HMG         $6K     12.7mm crews
├── V-SMASH MARITIME    $6.5K   Patrol boats
├── V-SMASH RCWS-LITE   $8K     Infantry squads
└── V-SMASH RCWS        $12K    Vehicles, UGV

SYSTEM TIER:
├── V-SMASH C4I HUB     $2K     Network node
└── V-SMASH DOME        $50-80K  Integrated C-UAS  ← NEW
```

### 8.2 V-SMASH DOME Specifications (Proposed)

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| **Detection Range** | ≥1 km (EO/IR) | Portable baseline |
| **Engagement Range** | 200-500m | Rifle ballistics |
| **Detect-to-Kill** | ≤15 sec | Benchmark |
| **Simultaneous Tracks** | ≥3 | Swarm defense |
| **Cost** | ≤$80K (enhanced) | vs $150-400K SMASH |
| **Weight** | ≤50 kg total | Portable |
| **Local Content** | ≥50% | Indigenous goal |

### 8.3 Development Roadmap

```
V-SMASH DOME DEVELOPMENT PHASES:

PHASE 1 (Year 1-2): BASIC C-UAS
┌─────────────────────────────────────────────────┐
│ • V-SMASH PRO sensor head (EO only)            │
│ • V-SMASH RCWS effector                         │
│ • Manual target designation                     │
│ • Basic track management                        │
│ • Target: $30K system cost                      │
└─────────────────────────────────────────────────┘
                    │
                    ▼
PHASE 2 (Year 2-3): STANDARD C-UAS
┌─────────────────────────────────────────────────┐
│ • Add thermal sensor (EO/IR)                    │
│ • Automated detection + classification          │
│ • V-SMASH C4I HUB integration                   │
│ • CoT/ATAK networking                           │
│ • Target: $50K system cost                      │
└─────────────────────────────────────────────────┘
                    │
                    ▼
PHASE 3 (Year 3-5): ENHANCED C-UAS
┌─────────────────────────────────────────────────┐
│ • Imported radar integration                    │
│ • Multi-target track management                 │
│ • Networked multi-RCWS engagement               │
│ • Future: Local radar development               │
│ • Target: $80K system cost                      │
└─────────────────────────────────────────────────┘
```

---

## 9. D-M-I-R Learning Alignment

### 9.1 **D**escribe - What We Learned

1. **Layered C-UAS architecture** - Detect → Track → Engage pipeline
2. **Person-in-the-loop essential** - IHL/ROE compliance non-negotiable
3. **Low cost per kill matters** - Rifle ammo vs missiles/interceptors
4. **Portable segment exists** - Squad/platoon level gap
5. **FCS is the differentiator** - Same SMASH tech enables C-UAS
6. **Open architecture wins** - ATAK/C2 integration critical

### 9.2 **M**odel - Mental Models Updated

```
C-UAS DESIGN PHILOSOPHY:

Traditional: Big radar → Big effector → Fixed site
             (Expensive, limited deployment)

SMASH DOME:  Scalable sensors → FCS-enhanced effector → Portable
             (Cost-effective, wide deployment)

V-SMASH:     Open sensors → Local FCS → Indigenous production
             (Affordable, sovereign capability)
```

### 9.3 **I**ntegrate - Design Decisions

| Decision | Rationale |
|----------|-----------|
| Add V-SMASH DOME product | Address critical C-UAS gap |
| Phased development | Manage complexity |
| Open CoT protocol | vs proprietary SMASH networking |
| EO/IR baseline | Lower cost entry point |
| Optional radar | Scalability without dependency |
| Rifle-based effector | Ammo logistics, low cost |

### 9.4 **R**eflect - Lessons for V-SMASH

1. **C-UAS is system, not product** - Integration is key value
2. **FCS technology scales** - Same core enables multiple missions
3. **Cost per kill is strategic** - Enables sustainable defense
4. **Open standards matter** - Interoperability over lock-in
5. **Phased approach wise** - Build capability incrementally
6. **Vietnam drone threat real** - Investment justified

---

## 10. References

### Sources
- [European Security & Defence - SMASH DOME Unveiling](https://euro-sd.com/2025/01/major-news/42297/smartshooter-smash-dome/)
- [UAS Weekly - SMASH DOME Advanced C-UAS](https://uasweekly.com/2025/01/28/smartshooter-unveils-smash-dome-advanced-cuas-solution-for-area-defense/)
- [Military Africa - SMASH DOME Layered C-UAS](https://www.military.africa/2025/01/smartshooter-unveils-smash-dome-layered-c-uas/)
- [Frag Out Magazine - Hopper + RPS-42 Integration](https://fragoutmag.com/smartshooter-smash-hopper-lrcws-integrated-rps-42-mhr-radar/)
- [Unmanned Airspace - Portable Layered C-UAS](https://www.unmannedairspace.info/counter-uas-systems-and-policies/smartshooter-develops-portable-layered-c-uas/)
- [Defence Industry EU - SMASH DOME Introduction](https://defence-industry.eu/smartshooter-introduces-smash-dome-a-new-solution-for-counter-drone-defence/)

### Related V-SMASH Documents
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis]] - Effector system
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis]] - Portable effector
- [[V-SMASH_RE_06_SMASH_connectivity_analysis]] - C2 integration
- [[V-SMASH_P2_06_product_portfolio_v2]] - Product family context

---

## Appendix A: Complete V-SMASH Product Family (9 Products)

| Product | Type | Weight | Cost | Primary Market |
|---------|------|--------|------|----------------|
| **LITE** | Handheld FCS | 400g | $3K | Militia, reserve |
| **PRO** | Handheld FCS | 800g | $5K | Regular infantry |
| **PRO-X** | Magnified FCS | 1.2kg | $7K | Designated marksman |
| **HMG** | Heavy mount FCS | 1.5kg | $6K | 12.7mm crews |
| **MARITIME** | Naval FCS | 1kg | $6.5K | Patrol boats |
| **RCWS-LITE** | Ultra-light RCWS | 10kg | $8K | Infantry squads |
| **RCWS** | Full RCWS | 15kg | $12K | Vehicles, UGV |
| **C4I HUB** | Network node | 500g | $2K | Squad leaders |
| **DOME** | Integrated C-UAS | ~50kg | $50-80K | Area defense |

---

## Appendix B: C-UAS Technology Comparison

| Technology | Pros | Cons | V-SMASH Relevance |
|------------|------|------|-------------------|
| **Kinetic (gun)** | Low cost, proven | Short range, LOS | PRIMARY |
| **Kinetic (missile)** | Long range | High cost | Not applicable |
| **Kinetic (interceptor)** | Effective | Very high cost | Not applicable |
| **Directed Energy** | Zero ammo cost | Expensive system | Future consideration |
| **EW/Jamming** | Non-kinetic | Counterable | Complement only |
| **Nets/Physical** | Simple | Very short range | Manual backup |

---

*Analysis complete. 8 new requirements proposed (R108-R115) for V-SMASH integrated C-UAS capability.*
