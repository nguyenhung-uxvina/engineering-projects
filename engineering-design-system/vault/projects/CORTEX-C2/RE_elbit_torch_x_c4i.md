---
project: CORTEX-C2
phase: 0
type: reverse-engineering
target: Elbit Systems TORCH-X C4ISR Suite
country: Israel
version: 1.0
created: 2026-02-12
status: complete
---

# REVERSE ENGINEERING ANALYSIS
## Elbit Systems TORCH-X C4ISR Suite
### Multi-Domain Command & Control Platform

---

## 1. COMPANY OVERVIEW

| Field | Value |
|-------|-------|
| **Company** | Elbit Systems Ltd. |
| **HQ** | Haifa, Israel |
| **Founded** | 1966 |
| **Ownership** | Public (NASDAQ: ESLT, TASE: ESLT) |
| **Revenue (2024)** | $6.828B (+14% YoY) |
| **Employees** | ~20,000+ |
| **Market Cap** | ~$12-14B (2025) |
| **Key Division** | C4I & Cyber (+7% growth in 2024) |
| **Export** | 30+ countries; ~70% of revenue from international customers |
| **Core Competency** | Multi-domain networked warfare, sensor integration, SDR communications |

### Division Structure (Relevant to C2)
| Division | Revenue Contribution | Products |
|----------|---------------------|----------|
| **C4I & Cyber** | ~$1.2B (est.) | TORCH-X, E-LynX, SafeCity, RAPTOR |
| **ISTAR & EW** | ~$1.5B (est.) | ISR sensors, EW systems, SIGINT |
| **Land** | ~$1.8B (est.) | DOMINATOR, RCWS, Sabrah |
| **Aerospace** | ~$2.3B (est.) | UAVs, avionics, HMDs |

---

## 2. TORCH-X PRODUCT FAMILY

### 2.1 Architecture Overview

TORCH-X is Elbit's flagship C4ISR platform family, built on the **E-CiX (Elbit Common infrastructure)** open architecture framework.

```
TORCH-X PRODUCT FAMILY
═══════════════════════════════════════════════════════════════

LAYER 5: APPLICATIONS (Edition-specific)
┌─────────────┬─────────────┬──────────────┬──────────────┐
│ TORCH-X HQ  │ TORCH-X     │ TORCH-X      │ TORCH-X      │
│ (Brigade+   │ Mounted     │ Fires        │ Naval CMS    │
│  Command)   │ (Platform)  │ (Artillery)  │ (Maritime)   │
├─────────────┴─────────────┴──────────────┴──────────────┤
│ SafeCity (HLS)│ RAPTOR (Tactical)│ DFNDR (C-UAS)       │
└─────────────────────────────────────────────────────────┘
         │                    │                    │
LAYER 4: AI & ANALYTICS
┌─────────────────────────────────────────────────────────┐
│  AI Decision Support │ Sensor Fusion │ Threat Assessment │
│  Predictive Analytics│ Pattern Recog │ Resource Optimize  │
└─────────────────────────────────────────────────────────┘
         │
LAYER 3: DATA & KNOWLEDGE BASE
┌─────────────────────────────────────────────────────────┐
│  Real-time Tactical DB │ Historical Data │ GIS Engine    │
│  Force Tracking │ Logistics DB │ Battle Damage Assess.   │
└─────────────────────────────────────────────────────────┘
         │
LAYER 2: E-CiX OPEN ARCHITECTURE FRAMEWORK
┌─────────────────────────────────────────────────────────┐
│  Service-Oriented Architecture (SOA)                     │
│  • Third-party app integration environment               │
│  • Modular plugin architecture                           │
│  • Cross-domain data exchange (land/air/sea/cyber)       │
│  • Multi-classification security boundaries              │
│  • NATO STANAG / MIL-STD compliance layer                │
└─────────────────────────────────────────────────────────┘
         │
LAYER 1: CONNECTIVITY
┌─────────────────────────────────────────────────────────┐
│  E-LynX SDR  │ SATCOM │ IP networks │ Legacy radios    │
│  (VHF/UHF/L-band, voice/data/video simultaneous)       │
│  Waveforms: MANET, HF ALE, VHF FM, SATCOM              │
└─────────────────────────────────────────────────────────┘
```

### 2.2 E-CiX Open Architecture

E-CiX is Elbit's foundational middleware framework. Key properties:

| Feature | Description |
|---------|-------------|
| **Architecture** | Service-Oriented Architecture (SOA) with microservices |
| **Third-party apps** | Open development environment for customer/partner applications |
| **Modularity** | Plugin architecture — add/remove capabilities without core changes |
| **Multi-domain** | Land, air, sea, cyber data exchange on single framework |
| **Security** | Multi-classification data handling; cross-domain guards |
| **Standards** | NATO STANAG 4559 (ISR), STANAG 5516 (Link-16), NFFI, MIP, OTH-G |
| **Scalability** | From single vehicle to theater-level command |
| **Deployment** | On-premise (ruggedized servers), vehicle-mounted, deployed HQ |

### 2.3 TORCH-X Product Variants

#### TORCH-X HQ (Brigade+ Command)

| Feature | Detail |
|---------|--------|
| **Purpose** | Multi-echelon headquarters command & control |
| **Users** | Brigade, division, corps commanders and staff |
| **COP** | Real-time Common Operational Picture with AI-prioritized information |
| **AI** | AI-based decision support, course-of-action analysis, threat prediction |
| **Video** | Live video streaming from UAVs, ground sensors, body cameras |
| **Comms** | Secure cross-platform voice, data, video synchronization |
| **Degraded ops** | Continues operating under network disruption/degradation |
| **Deployment** | Command post shelter, container, or building installation |

#### TORCH-X Mounted (Platform-Level BMS)

| Feature | Detail |
|---------|--------|
| **Purpose** | Single-platform battle management for AFVs, MBTs, APCs |
| **Key Feature** | Centralized UI combining ALL platform sensors and effectors |
| **Integration** | Any sensor, any effector on any platform type |
| **Crew Interface** | Single display for situational awareness + sensor/weapon operation |
| **Knowledge Base** | Extensive library enables rapid integration with new platforms |
| **Scalability** | From individual vehicle to combined arms combat team |
| **Architecture** | Modular — adapts to specific platform configuration |

#### TORCH-X Fires (Artillery/Fire Coordination)

| Feature | Detail |
|---------|--------|
| **Purpose** | Cross-force fire coordination, sensor-to-shooter |
| **Key Feature** | Quick and precise planning + execution with cross-force coordination |
| **Integration** | 155mm howitzers, MLRS, mortars, air support, naval fires |
| **Combined with** | E-LynX SDR for secure fire mission data transmission |
| **Capabilities** | Digital fire requests, automated fire plans, BDA, deconfliction |
| **Export** | Selected by European country for 155mm howitzer battalion upgrade (2024) |
| **Architecture** | Multi-layer fires application within TORCH-X framework |

#### TORCH-X Naval CMS (Combat Management System)

| Feature | Detail |
|---------|--------|
| **Purpose** | Naval combat management — coastal to EEZ operations |
| **Key Feature** | Open architecture, scalable from patrol boat to frigate |
| **Integration** | Radar, EO/IR, sonar, ESM, weapons (guns, missiles, torpedoes) |
| **AI** | Automated response options, threat evaluation, weapon assignment |
| **COP** | Real-time processed tactical picture with automated response |
| **Standards** | NATO STANAG maritime standards |

#### SafeCity (Homeland Security)

| Feature | Detail |
|---------|--------|
| **Purpose** | Urban/national security C2 for bases, cities, borders, critical infrastructure |
| **Architecture** | Fixed C2 centers + FRONTS-C2 mobile C4I for on-scene forces |
| **Integration** | CCTV, access control, radar, fence sensors, acoustic, drones |
| **AI** | Video analytics, anomaly detection, automated alerts |
| **Deployment** | Multi-site, multi-echelon (local/regional/national) |

#### RAPTOR (Tactical C2)

| Feature | Detail |
|---------|--------|
| **Purpose** | Company/platoon-level tactical C2 |
| **Form Factor** | Ruggedized tablet/smartphone application |
| **Key Feature** | Lightweight, man-portable, dismounted infantry C2 |
| **Integration** | Blue force tracking, messaging, sensor feeds, fire requests |

#### DFNDR (Counter-Drone)

| Feature | Detail |
|---------|--------|
| **Purpose** | Counter-UAS / counter-swarm C2 and effector |
| **Architecture** | Decentralized drone swarm defense — no single point of failure |
| **Effectors** | Jamming, laser, kinetic intercept, net capture |
| **AI** | Automated drone detection, classification, threat prioritization |
| **Integration** | Works within TORCH-X ecosystem for unified air picture |

---

## 3. E-LynX COMMUNICATIONS

| Feature | Detail |
|---------|--------|
| **Type** | Software-Defined Radio (SDR) family |
| **Bands** | VHF (30-88 MHz), UHF (225-512 MHz), L-band (1.2-1.4 GHz) |
| **Waveforms** | MANET (mobile ad-hoc), HF ALE, VHF FM, SATCOM, custom |
| **Capability** | Simultaneous voice + data + video on single radio |
| **MANET** | Self-forming/self-healing mesh network; 1000+ nodes |
| **Data rate** | Up to 35 Mbps (broadband MANET) |
| **Encryption** | Military-grade; NATO/national crypto suites |
| **Form Factors** | Manpack, vehicular, airborne, maritime, base station |
| **Key Advantage** | Enables TORCH-X connectivity layer without external infrastructure |

---

## 4. AI/ML CAPABILITIES

| Capability | Description | CORTEX C2 Comparison |
|-----------|-------------|---------------------|
| **AI Decision Support** | Course-of-action analysis; threat prediction; resource optimization | Directly competes with CORTEX SHIELD edition |
| **Sensor Fusion** | Multi-source data fusion for COP generation | Equivalent to FusionAI engine concept |
| **Pattern Recognition** | Historical pattern analysis for threat assessment | Equivalent to ThreatAI engine |
| **Video Analytics** | Object detection, tracking, anomaly detection (SafeCity) | Equivalent to VisualAI engine |
| **Predictive Analytics** | Trend analysis, readiness assessment | Partially overlaps with TrainingAI |
| **Natural Language** | Not publicly disclosed | CORTEX C2 potential advantage |
| **Autonomous Fires** | AI-suggested fire solutions (human-approved) | TORCH-X Fires capability |

**Key Insight**: Elbit's AI is embedded throughout TORCH-X as an enhancement layer, not as standalone "AI engines" with separate branding. The AI capabilities are presented as integrated features, not marketable modules. CORTEX C2's approach of **named, distinct AI engines** (AcousticAI, FusionAI, etc.) is a stronger branding and monetization strategy.

---

## 5. BUSINESS MODEL

### 5.1 Pricing (Estimated from Contract Data)

| Product | Estimated Price Range | Basis |
|---------|----------------------|-------|
| **TORCH-X HQ** (brigade set) | $5-20M | Large system procurement + integration |
| **TORCH-X Mounted** (per vehicle) | $50-200K | Vehicle BMS kit |
| **TORCH-X Fires** (battalion set) | $5-15M | European artillery contract (2024) |
| **TORCH-X Naval CMS** | $10-50M | Per vessel, depends on size |
| **E-LynX radio** (per unit) | $15-50K | SDR radio unit |
| **SafeCity** (per site) | $1-10M | Depends on sensor count and area |
| **Annual support/maintenance** | 10-15% of acquisition cost | Industry standard |

### 5.2 Export Customers

| Region | Known Customers | Products |
|--------|----------------|----------|
| **Europe** | Multiple NATO nations (classified) | TORCH-X Fires, E-LynX, BMS |
| **Asia-Pacific** | Australia, Singapore, Philippines, Thailand | Various C4I, E-LynX |
| **Latin America** | Brazil, Chile, Colombia | C4I, radios |
| **Africa** | Multiple countries | SafeCity, C4I |
| **North America** | US (limited, competitive market) | E-LynX, components |

### 5.3 Business Model Pattern

```
ELBIT C4I BUSINESS MODEL:
═════════════════════════
1. WIN RADIO CONTRACT (E-LynX SDR)
   → Establishes comms backbone

2. UPSELL C4I (TORCH-X application layer)
   → Adds value on top of radio network

3. INTEGRATE SENSORS (Elbit ISR products)
   → Locks customer into Elbit sensor ecosystem

4. PLATFORM LOCK-IN (E-CiX framework)
   → Third-party apps built on E-CiX are sticky

5. LONG-TERM SUPPORT (10-15% annual)
   → Recurring revenue for 15-25 year lifecycle

SIMILARITY TO CORTEX C2:
• Radio → Hardware = Entry point
• C4I → Software = Value capture
• Sensor integration → AI engines = Lock-in
• Annual support → Subscription = Recurring
```

---

## 6. STRENGTHS & WEAKNESSES

### Strengths
| # | Strength | Impact on CORTEX C2 |
|---|----------|-------------------|
| 1 | **Combat-proven at scale** — IDF operational use; multiple export armies | CORTEX C2 must prove reliability before competing |
| 2 | **Full-stack offering** — radio + C4I + sensors + weapons in one company | CORTEX C2 has similar advantage (Workshop X product ecosystem) |
| 3 | **E-CiX open architecture** — third-party app development environment | CORTEX C2 should match with open API/plugin architecture |
| 4 | **E-LynX radio moat** — once installed, TORCH-X is natural upsell | CORTEX C2 uses hardware products as gateway (same pattern) |
| 5 | **NATO interoperability** — STANAG compliance enables alliance sales | CORTEX C2 needs STANAG compliance for export |
| 6 | **$6.8B revenue** — massive R&D budget and staying power | CORTEX C2 cannot compete head-to-head; must find niche |

### Weaknesses
| # | Weakness | CORTEX C2 Opportunity |
|---|----------|---------------------|
| 1 | **Expensive** — brigade C4I = $5-20M; out of reach for most VN units | CORTEX C2 at $15-200K is 10-100x cheaper |
| 2 | **Heavyweight integration** — months to deploy, requires Elbit engineers | CORTEX C2 targets <1 week deployment with Edition templates |
| 3 | **Generalist platform** — E-CiX serves all domains but specializes in none | CORTEX C2 Editions specialize per domain (RANGE, SHIELD, etc.) |
| 4 | **Israeli export restrictions** — some countries cannot buy Israeli defense | CORTEX C2 as Vietnamese product has no such restrictions |
| 5 | **No training analytics focus** — TORCH-X is combat/ops C2; training is secondary | CORTEX C2 RANGE edition fills this gap |
| 6 | **AI not branded/monetized** — AI features buried in product, not sold separately | CORTEX C2 named AI engines (6 engines) are marketable assets |
| 7 | **Proprietary radio dependency** — E-LynX lock-in may deter some customers | CORTEX C2 is radio-agnostic (works with any IP network) |
| 8 | **No acoustic integration** — no native acoustic sensor (LOMAH, C-UAS acoustic) support | CORTEX C2 has deep acoustic integration (AcousticAI engine) |

---

## 7. DESIGN PARADIGM ANALYSIS

### Paradigm: "FULL-STACK DEFENSE INTEGRATOR"

| Dimension | Elbit TORCH-X Approach |
|-----------|----------------------|
| **Philosophy** | Provide everything from radio to C2 to sensors to weapons |
| **Architecture** | SOA middleware (E-CiX) with pluggable applications |
| **AI Role** | Enhancement layer — AI improves existing C2 workflows |
| **Business Model** | Radio entry → C4I upsell → sensor lock-in → lifecycle support |
| **Pricing** | Premium ($5-50M per deployment); high-value customers only |
| **Deployment** | Heavy integration; Elbit engineers on-site for months |
| **Target Customer** | National army (brigade+); large budget; long procurement cycle |
| **Competitive Moat** | E-CiX platform lock-in + E-LynX radio infrastructure |

### vs. CORTEX C2 "PLATFORM AI BRAIN" Paradigm

| Dimension | CORTEX C2 Approach | Advantage |
|-----------|-------------------|-----------|
| **Philosophy** | AI brain connecting existing products | Lower barrier — no radio replacement needed |
| **Architecture** | 5-layer platform with 6 named AI engines | More modular and transparent |
| **AI Role** | Core value proposition — AI IS the product | Stronger AI narrative; subscription-worthy |
| **Business Model** | Hardware gateway → free RANGE → subscription | Lower entry cost; faster adoption |
| **Pricing** | $15-200K (10-100x cheaper than TORCH-X) | Accessible to battalion/company level |
| **Deployment** | Edition templates → <1 week deployment target | Orders of magnitude faster |
| **Target Customer** | Vietnamese military (all echelons); regional export | Underserved market segment |
| **Competitive Moat** | Data flywheel (13+ products feeding AI) | Unique cross-domain data advantage |

---

## 8. KEY LESSONS FOR CORTEX C2

| # | Lesson | Application |
|---|--------|-------------|
| 1 | **Open architecture wins** — E-CiX's third-party app support drives adoption | CORTEX C2 must have open API/SDK for customer/partner apps from V1.0 |
| 2 | **Radio/comms is the entry wedge** — E-LynX creates infrastructure lock-in | CORTEX C2 uses hardware products (VN-LOMAH) as entry wedge — same pattern |
| 3 | **Sensor fusion is table stakes** — every modern C2 must fuse multi-sensor data | FusionAI engine must be core capability, not nice-to-have |
| 4 | **Edition/variant strategy works** — TORCH-X has HQ/Mounted/Fires/Naval/SafeCity | CORTEX C2 5-edition strategy (RANGE/BASE/SHIELD/NAVAL/ENTERPRISE) is validated |
| 5 | **NATO STANAG enables export** — TORCH-X sells globally because of standards compliance | CORTEX C2 should target STANAG 4559/5516 and SAPIENT compliance early |
| 6 | **Degraded mode is critical** — TORCH-X HQ continues under network disruption | CORTEX C2 must work standalone when mesh/network fails |
| 7 | **Annual support is revenue** — 10-15% recurring on large installed base | CORTEX C2 subscription model is even better (higher % recurring) |
| 8 | **Don't compete head-to-head** — $6.8B company with combat-proven products | CORTEX C2 competes on: price (10-100x cheaper), domain specialization (training), acoustic integration (unique), deployment speed |

---

## 9. COMPETITIVE POSITIONING

```
PRICE COMPARISON (per deployment):
                    $10K   $100K   $1M    $10M    $50M
                     │       │      │       │       │
CORTEX RANGE         ██      │      │       │       │     $15-25K
CORTEX BASE          │  ████ │      │       │       │     $35-60K
CORTEX SHIELD        │    ██████    │       │       │     $60-120K
CORTEX NAVAL         │      ████████│       │       │     $80-200K
                     │       │      │       │       │
TORCH-X Mounted      │       ██████ │       │       │     $50-200K/veh
TORCH-X Fires        │       │      │ ██████████    │     $5-15M/bn
TORCH-X HQ           │       │      │   ████████████│     $5-20M/bde
TORCH-X Naval        │       │      │     ██████████████  $10-50M/ship
                     │       │      │       │       │

CORTEX C2 occupies the AFFORDABLE segment that TORCH-X does not serve.
```

---

*Reverse Engineering Analysis completed: 2026-02-12*
*Classification: UNCLASSIFIED — Based on publicly available information*
*Sources: Elbit Systems corporate website, defense publications (Jane's, Defense News, C4ISRNET), press releases, financial filings (NASDAQ: ESLT)*
