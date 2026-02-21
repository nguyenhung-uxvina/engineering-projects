---
project: CORTEX-C2
phase: 0
type: reverse-engineering
target: Rafael FIRE WEAVER & Networked Warfare Suite
country: Israel
version: 1.0
created: 2026-02-12
status: complete
---

# REVERSE ENGINEERING ANALYSIS
## Rafael FIRE WEAVER & Networked Warfare Suite
### AI-Powered Sensor-to-Shooter Network

---

## 1. COMPANY OVERVIEW

| Field | Value |
|-------|-------|
| **Company** | Rafael Advanced Defense Systems Ltd. |
| **HQ** | Haifa, Israel |
| **Founded** | 1948 (as Israel's national weapons development authority) |
| **Ownership** | State-owned (Israeli Ministry of Defense) |
| **Revenue (2024)** | ~$4.9B (+27% YoY from ~$3.9B in 2023) |
| **New Orders (2024)** | $8.23B |
| **Order Backlog** | $17.76B (3.6 years of sales, +24% from 2023) |
| **Net Profit (2024)** | $257M (+64% from 2023) |
| **Employees** | ~8,000-9,000 |
| **Export** | ~50% of revenue; 40+ countries |
| **Core Competency** | Precision munitions, air defense, networked warfare, AI-driven fire control |

### Key Product Families (Relevant to C2)

| Product | Category | Revenue Significance |
|---------|----------|---------------------|
| **Iron Dome / C-DOME** | Air defense system + C2 | Flagship; combat-proven; multi-billion |
| **FIRE WEAVER** | Sensor-to-shooter network | Next-gen; IDF adopted; US Army evaluated |
| **DRONE DOME** | Counter-UAS system | Growing rapidly (post-Ukraine demand) |
| **BNET** | Broadband tactical radio | Networking backbone for all Rafael C2 |
| **SPIKE Family** | Precision missiles (NLOS, LR, ER) | Major revenue; integrated with FIRE WEAVER |
| **SPICE** | Precision guidance kit for bombs | Air force integration |
| **Iron Beam** | Laser air defense | Future; nearing deployment |

---

## 2. FIRE WEAVER — CORE ANALYSIS

### 2.1 Product Definition

> **FIRE WEAVER** is an AI-powered, GPS-independent, networked sensor-to-shooter system that connects any sensor to any shooter on the battlefield through a patented **Geo-Pixel** common visual language. It uses artificial intelligence to analyze the combat environment, prioritize targets, and allocate the optimal shooter to each target — closing sensor-to-shooter loops in **seconds** rather than minutes.

### 2.2 System Architecture

```
FIRE WEAVER SYSTEM ARCHITECTURE
═══════════════════════════════════════════════════════════════

LAYER 5: FIRE MANAGEMENT TERMINAL (Officer Control)
┌─────────────────────────────────────────────────────────┐
│  • Full control of autonomous behavior level             │
│  • Define safety zones and time limits                   │
│  • Approve/decline/reprogram fire solutions              │
│  • Multiple parallel sensor-to-shooter loops             │
│  • Override authority at all times                        │
└───────────────────────────┬─────────────────────────────┘
                            │
LAYER 4: AI ENGINE (Target Allocation & Optimization)
┌─────────────────────────────────────────────────────────┐
│  AI FIRE ALLOCATION:                                     │
│  • Analyze combat environment in real-time               │
│  • Prioritize targets by threat level                    │
│  • Calculate optimal shooter per target based on:        │
│    - Line-of-sight availability                          │
│    - Weapon type suitability                             │
│    - Ammunition status                                   │
│    - Engagement range                                    │
│    - Collateral damage estimate                          │
│    - Time-to-effect                                      │
│  • Deconflict simultaneous engagements                   │
│  • IFF (Identification Friend/Foe) enforcement           │
│  • Battle Damage Assessment (post-engagement)            │
└───────────────────────────┬─────────────────────────────┘
                            │
LAYER 3: GEO-PIXEL ENGINE (Common Visual Language)
┌─────────────────────────────────────────────────────────┐
│  PATENTED GEO-PIXEL TECHNOLOGY:                          │
│  • 3D model of terrain with pixel-level resolution       │
│  • GPS-INDEPENDENT target designation                    │
│  • Computer vision to present target location from       │
│    multiple viewing angles                               │
│  • Any sensor can designate using:                       │
│    - Geo-coordinates (GPS)                               │
│    - Laser designation                                   │
│    - Electro-optical pixel selection                     │
│  • Shooter sees target FROM THEIR OWN PERSPECTIVE        │
│    (Geo-Pixel translates sensor view → shooter view)     │
│  • Works in GPS-denied / GPS-jammed environments         │
└───────────────────────────┬─────────────────────────────┘
                            │
LAYER 2: SENSOR-SHOOTER NETWORK (Flat Architecture)
┌─────────────────────────────────────────────────────────┐
│                                                          │
│  SENSORS (Any-to-Any):         SHOOTERS (Any-to-Any):    │
│  ┌─────────┐ ┌─────────┐     ┌─────────┐ ┌─────────┐   │
│  │ UAV ISR │ │ Ground  │     │ Tank    │ │ RCWS    │   │
│  │ Camera  │ │ EO/IR   │     │ Gun     │ │ Station │   │
│  ├─────────┤ ├─────────┤     ├─────────┤ ├─────────┤   │
│  │ Radar   │ │ Soldier │     │ ATGM    │ │ Mortar  │   │
│  │         │ │ (Sight) │     │ (Spike) │ │         │   │
│  ├─────────┤ ├─────────┤     ├─────────┤ ├─────────┤   │
│  │ SIGINT/ │ │ Acoustic│     │ Artillery│ │ Air     │   │
│  │ ELINT   │ │ Sensor  │     │ (155mm) │ │ Support │   │
│  └─────────┘ └─────────┘     └─────────┘ └─────────┘   │
│       │           │               │           │          │
│       └───────────┼───────────────┼───────────┘          │
│                   │               │                      │
│              BNET RADIO (Broadband Mesh)                  │
│                                                          │
└─────────────────────────────────────────────────────────┘
                            │
LAYER 1: CONNECTIVITY (BNET Family)
┌─────────────────────────────────────────────────────────┐
│  BNET Broadband IP Radio:                                │
│  • Cognitive multi-frequency MANET                       │
│  • Simultaneous voice + data + video + sensor feeds      │
│  • Self-forming/self-healing mesh                        │
│  • Multi-hop routing                                     │
│  • Spectrum management (avoids jamming/interference)     │
│  • Data rates: up to 100+ Mbps aggregate                 │
│  • Range: 10-50 km (depending on terrain/power)          │
│  • Waveforms: Multiple simultaneous                      │
└─────────────────────────────────────────────────────────┘
```

### 2.3 Geo-Pixel Technology (Patented)

This is FIRE WEAVER's most distinctive innovation:

```
TRADITIONAL Target Designation:         GEO-PIXEL Target Designation:
═══════════════════════════════        ═══════════════════════════════

Sensor sees target                     Sensor sees target
    │                                      │
    ▼                                      ▼
Convert to GPS coordinate              Map to 3D terrain model pixel
    │                                      │
    ▼                                      ▼
Transmit coordinates to shooter        Geo-Pixel translates to
    │                                  SHOOTER'S own viewpoint
    ▼                                      │
Shooter must FIND target               Shooter sees EXACTLY what
using coordinates + map                to look for FROM THEIR angle
    │                                      │
    ▼                                      ▼
Prone to GPS jamming,                  Works GPS-denied
map errors, confusion                  Eliminates confusion
Time: MINUTES                          Time: SECONDS
```

**Key Properties:**
- **GPS-independent**: Uses computer vision + 3D terrain model, not satellite positioning
- **Multi-perspective**: Translates a sensor's view to any shooter's viewpoint automatically
- **Pixel-level precision**: Target designated at individual pixel in sensor image
- **3D awareness**: Handles elevation, defilade, building floors
- **Universal language**: Any sensor, any shooter, any platform — same visual format

### 2.4 AI Capabilities

| AI Feature | Description | Maturity |
|-----------|-------------|---------|
| **Target Prioritization** | AI ranks threats by urgency, capability, proximity | Operational (IDF) |
| **Shooter-Target Pairing** | AI selects optimal shooter per target (multi-criteria optimization) | Operational |
| **Deconfliction** | AI prevents fratricide, manages safety zones, deconflicts fires | Operational |
| **IFF Integration** | Automatic friend/foe/neutral tracking integrated into fire solution | Operational |
| **Battle Damage Assessment** | Post-engagement AI analysis of effectiveness | Operational |
| **Predictive Engagement** | AI predicts target movement for lead computation | In development |
| **Autonomous Engagement** | AI suggests fire solution — human approves/overrides | Operational (human-on-the-loop) |
| **Multi-Loop Parallel** | Manage multiple sensor-to-shooter loops simultaneously | Operational |

**Critical Insight**: FIRE WEAVER's AI is fundamentally a **real-time optimization engine** for fire allocation. It solves: "Given N targets and M shooters, what is the optimal assignment?" This is a combinatorial optimization problem — Rafael's edge is their combat-validated algorithms from Iron Dome experience.

### 2.5 Deployment & Operational Status

| Milestone | Date | Details |
|-----------|------|---------|
| IDF selection | Feb 2020 | Israeli Ministry of Defense selected FIRE WEAVER for IDF ground forces |
| IDF brigade fielding | 2021-2022 | First operational brigade equipped |
| US Army assessment | 2021 | AEWE (Army Expeditionary Warrior Experiment) operational assessment; platoon-level |
| Germany demonstration | 2024 | BNET + FIRE WEAVER demonstrated for Bundeswehr |
| NATO interest | 2024-2025 | Multiple NATO nations evaluating |
| Oracle cloud partnership | Sept 2024 | FIRE WEAVER + IMILITE available on Oracle cloud infrastructure |

### 2.6 Spike NMT (All-in-One STS Package)

Rafael now offers a complete **Spike NMT (NLOS Mission Taskforce)** that bundles FIRE WEAVER with:
- UAV platforms (ISR)
- Ground launch platform with multiple Spike NLOS missiles
- BNET radios (networking)
- FIRE WEAVER (C2 + AI fire allocation)

This is a "sensor-to-shooter in a box" — relevant because it shows Rafael packaging complete solutions, not just C2 software.

---

## 3. DRONE DOME (C-UAS)

| Feature | Detail |
|---------|--------|
| **Purpose** | Counter-UAS detection, tracking, and neutralization system |
| **Detection** | Radar (360°) + EO/IR (day/night) + RF detection/DF |
| **Tracking** | Multi-sensor fusion; simultaneous multiple drone tracking |
| **Neutralization** | RF jamming (CURT-S), GPS spoofing, laser (optional for hard-kill) |
| **C2** | Integrated command interface; manual + automated response modes |
| **Range** | Detection: 3-10 km (depends on drone size); jamming: 1-3 km |
| **Integration** | Can feed into FIRE WEAVER for integrated air/ground threat picture |
| **Deployment** | Fixed site, vehicle-mounted, rapid-deployable |
| **Pricing** | Estimated $1-5M per site (depends on configuration) |
| **Relevance** | Directly competes with CORTEX C2 SHIELD + VN-CUAS combination |

---

## 4. BNET COMMUNICATIONS

| Feature | Detail |
|---------|--------|
| **Type** | Broadband IP radio family (cognitive, multi-frequency) |
| **Architecture** | MANET (Mobile Ad-hoc Network) with spectral management |
| **Bandwidth** | Up to 100+ Mbps aggregate network throughput |
| **Range** | 10-50 km (terrain/power dependent) |
| **Nodes** | Supports large-scale networks (hundreds of nodes) |
| **Key Feature** | Patented cognitive spectrum management — avoids jamming |
| **Forms** | Manpack, vehicular, airborne (drone-mounted), naval |
| **Video** | Supports real-time video streaming from multiple sensors |
| **Role** | Backbone for FIRE WEAVER — enables high-bandwidth STS loops |

---

## 5. BUSINESS MODEL

### 5.1 Pricing (Estimated)

| Product | Estimated Price | Basis |
|---------|----------------|-------|
| **FIRE WEAVER** (brigade set) | $10-30M | Full brigade deployment with integration |
| **FIRE WEAVER** (company set) | $2-8M | Limited deployment |
| **Spike NMT** (complete STS kit) | $5-15M | UAV + missiles + BNET + FIRE WEAVER |
| **DRONE DOME** (per site) | $1-5M | Depending on sensor/effector config |
| **BNET radio** (per unit) | $20-80K | Broadband IP radio |
| **Annual support** | 10-15% of acquisition | Industry standard |

### 5.2 Revenue Model

```
RAFAEL NETWORKED WARFARE BUSINESS MODEL:
═════════════════════════════════════════

1. SELL WEAPONS (Spike missiles, Iron Dome interceptors)
   → High-margin consumables; recurring ammunition revenue

2. SELL NETWORKING (BNET radios)
   → Infrastructure backbone; enables all connected systems

3. SELL C2 BRAIN (FIRE WEAVER)
   → AI fire allocation; connects everything; highest strategic value

4. SELL COMPLETE PACKAGES (Spike NMT)
   → One procurement = sensor + shooter + C2 + comms

5. CLOUD DEPLOYMENT (Oracle partnership)
   → Lower barrier for evaluation/training; SaaS-like model emerging

KEY DIFFERENCE FROM ELBIT:
• Elbit sells C2 as PLATFORM (E-CiX is middleware)
• Rafael sells C2 as WEAPON SYSTEM (FIRE WEAVER enables kills)
• Rafael's value proposition: "Close the loop in SECONDS, not minutes"
```

### 5.3 Export Customers

| Customer | Products | Status |
|----------|----------|--------|
| **IDF (Israel)** | FIRE WEAVER, Iron Dome, DRONE DOME, BNET | Operational |
| **US Army** | FIRE WEAVER (AEWE evaluation), Iron Dome | Evaluation / partial procurement |
| **Germany** | BNET + FIRE WEAVER (demonstration 2024) | Evaluation |
| **NATO nations** | Multiple (classified) | Various stages |
| **India** | Iron Dome variant, Spike missiles | Operational |
| **South Korea** | Iron Dome technology | Procurement |
| **UAE** | Iron Dome variant (THAAD-class) | Reported |
| **40+ countries** | Spike missile family | Major export |

---

## 6. STRENGTHS & WEAKNESSES

### Strengths

| # | Strength | Impact on CORTEX C2 |
|---|----------|-------------------|
| 1 | **Geo-Pixel is breakthrough technology** — GPS-independent, intuitive, patented | CORTEX C2 must develop equivalent visual target language |
| 2 | **Combat-proven AI fire allocation** — Iron Dome algorithms adapted for ground | CORTEX C2 AI engines are unproven; must demonstrate reliability |
| 3 | **Sensor-to-shooter in seconds** — closed-loop speed is unmatched | CORTEX C2 must match latency requirements (QUA-005: ≤3s) |
| 4 | **IDF + US Army validation** — highest possible credibility | CORTEX C2 must build credibility through Vietnamese military pilots |
| 5 | **Complete ecosystem** — weapons + sensors + C2 + comms from one company | Workshop X has similar ecosystem advantage (13+ products) |
| 6 | **$17.76B backlog** — massive resources for continued development | CORTEX C2 cannot match R&D investment; must be smarter, not bigger |
| 7 | **Oracle cloud partnership** — enabling SaaS/cloud deployment model | CORTEX C2 should consider cloud option for training/export |

### Weaknesses

| # | Weakness | CORTEX C2 Opportunity |
|---|----------|---------------------|
| 1 | **Expensive** — $2-30M per deployment; out of reach for most armies | CORTEX C2 at $15-200K is 10-100x cheaper |
| 2 | **Combat-focused only** — no training domain; no base security analytics | CORTEX C2 RANGE and BASE editions fill these gaps |
| 3 | **Weapons-centric** — FIRE WEAVER is about KILLING, not SENSING or TRAINING | CORTEX C2 spans sense-decide-act across all 3 domains |
| 4 | **Israeli export restrictions** — political barriers in some markets | Vietnamese product has no such restrictions |
| 5 | **BNET dependency** — requires Rafael radio infrastructure | CORTEX C2 works with any IP network |
| 6 | **No acoustic integration** — no native acoustic sensor capability | CORTEX C2 AcousticAI is unique competitive advantage |
| 7 | **No training data analytics** — no readiness scoring, no personnel tracking | CORTEX C2 TrainingAI fills major market gap |
| 8 | **State-owned** — slower commercial agility than private company | Workshop X can move faster on product iterations |
| 9 | **No subscription model** — traditional defense procurement only | CORTEX C2 subscription model = better recurring revenue |

---

## 7. DESIGN PARADIGM ANALYSIS

### Paradigm: "AI FIRE ALLOCATOR"

| Dimension | Rafael FIRE WEAVER Approach |
|-----------|-----------------------------|
| **Philosophy** | AI optimizes the kill chain — right shooter, right target, right time |
| **Architecture** | Flat sensor-shooter network with centralized AI optimization |
| **AI Role** | **Core product** — AI IS the value (fire allocation algorithm) |
| **Key Innovation** | Geo-Pixel visual language eliminates GPS dependency |
| **Business Model** | Weapon system sale ($2-30M); ammunition consumables; support |
| **Pricing** | Premium-only; nation-state budget required |
| **Deployment** | Brigade-level; months of integration; Rafael engineers required |
| **Target Customer** | Advanced militaries (IDF, US, NATO); high-end only |
| **Competitive Moat** | Geo-Pixel patent + Iron Dome AI heritage + IDF combat validation |

### vs. CORTEX C2 "PLATFORM AI BRAIN" Paradigm

| Dimension | FIRE WEAVER | CORTEX C2 | CORTEX Advantage |
|-----------|-------------|-----------|------------------|
| **Scope** | Fire allocation only | Training + Combat + Defense | Broader value proposition |
| **AI Focus** | Kill chain optimization | Decision support across all domains | More applications for same AI investment |
| **Price** | $2-30M | $15-200K | 10-100x more accessible |
| **Training** | None | RANGE edition (core) | Entire uncontested domain |
| **Base Defense** | DRONE DOME (separate product) | BASE edition (integrated) | Single platform vs. separate procurement |
| **Acoustic** | None | AcousticAI engine (unique) | Novel sensing modality |
| **Data Flywheel** | Limited (combat data only) | Training + combat + defense data all feed AI | Richer, more diverse learning |
| **Gateway** | Spike missile purchase | VN-LOMAH purchase | Lower entry cost |
| **Subscription** | No | Yes ($3-60K/yr) | Better recurring revenue model |

---

## 8. KEY LESSONS FOR CORTEX C2

| # | Lesson | Application |
|---|--------|-------------|
| 1 | **Geo-Pixel concept is brilliant** — GPS-independent visual target language solves real problem | CORTEX C2 should develop equivalent "visual common language" for multi-sensor display; consider 3D terrain model with pixel-level target overlay |
| 2 | **AI fire allocation is the killer feature** — not just displaying data, but DECIDING what to do | CORTEX C2 AI engines must go beyond dashboard → must RECOMMEND actions (fire solutions, threat responses, training corrections) |
| 3 | **Seconds matter** — FIRE WEAVER's value is SPEED (minutes → seconds for STS loop) | CORTEX C2 must obsess over latency: sensor event → C2 display → recommended action in <3 seconds |
| 4 | **Human-on-the-loop, not human-in-the-loop** — AI recommends, human approves/overrides | CORTEX C2 should adopt same pattern: AI generates recommendations; commander approves with single button |
| 5 | **Complete packages sell better** — Spike NMT bundles everything into one procurement | CORTEX C2 Edition bundles (software + training + integration + support) are validated approach |
| 6 | **Oracle cloud partnership signals SaaS trend** — even traditional defense companies going cloud | CORTEX C2 should offer cloud/hybrid option for training analytics (non-classified) and export |
| 7 | **Patent your innovations** — Geo-Pixel is patented and creates strong competitive moat | Workshop X should patent key CORTEX C2 innovations (data flywheel algorithms, acoustic-visual fusion method, training analytics model) |
| 8 | **Training domain is Rafael's blind spot** — and Elbit's too | CORTEX C2 RANGE edition has NO competition from either Israeli giant; this is the safest entry point |

---

## 9. COMPETITIVE POSITIONING MAP

```
                    COMBAT FOCUS
                         │
    ┌────────────────────┼────────────────────┐
    │                    │                    │
    │   TORCH-X HQ       │   FIRE WEAVER      │
    │   (Elbit)          │   (Rafael)          │
    │   $5-20M           │   $2-30M            │
    │   BMS + COP        │   AI Fire Alloc     │
    │                    │                    │
HIGH├────────────────────┼────────────────────┤
COST│                    │                    │
    │   DRONE DOME       │   TORCH-X Naval    │
    │   (Rafael)         │   (Elbit)          │
    │   $1-5M            │   $10-50M          │
    │   C-UAS            │   Ship CMS         │
    │                    │                    │
    ├────────────────────┼────────────────────┤
LOW │                    │                    │
COST│  ★ CORTEX BASE    │  ★ CORTEX SHIELD   │
    │    $35-60K         │    $60-120K         │
    │    Base Defense    │    C-UAS + Combat   │
    │                    │                    │
    │  ★ CORTEX RANGE   │                    │
    │    $15-25K         │   (NO COMPETITOR)   │
    │    Training        │                    │
    │                    │                    │
    └────────────────────┼────────────────────┘
                         │
                    TRAINING FOCUS

★ = CORTEX C2 Editions (all in underserved low-cost quadrant)
```

---

## 10. SUMMARY TABLE

| Dimension | Rafael FIRE WEAVER | CORTEX C2 "THẦN TOÁN" |
|-----------|-------------------|----------------------|
| **Company** | Rafael ($4.9B, state-owned) | Workshop X (startup) |
| **Product Type** | AI fire allocator | Multi-domain C2 platform |
| **Domains** | Combat only | Training + Combat + Base Defense |
| **AI** | Fire allocation optimization (combat-proven) | 6 named engines (development stage) |
| **Key Innovation** | Geo-Pixel (GPS-independent visual language) | Data Flywheel (13+ products → AI learning) |
| **Price** | $2-30M per deployment | $15-200K per deployment |
| **Business Model** | Weapon system + support | Hardware gateway + subscription |
| **Training** | None | RANGE edition (core) |
| **Acoustic** | None | AcousticAI engine |
| **Export Reach** | 40+ countries (Israeli restrictions) | Vietnam + ASEAN (no restrictions) |
| **Maturity** | Operational (IDF, US Army tested) | Concept stage |
| **Threat Level** | Low (different price/market segment) | — |

---

*Reverse Engineering Analysis completed: 2026-02-12*
*Classification: UNCLASSIFIED — Based on publicly available information*
*Sources: Rafael corporate communications, defense publications (Jane's, Defense News, Asian Military Review, EDR Magazine), US Army AEWE reports, Oracle press release (Sept 2024), financial reports (2024)*
