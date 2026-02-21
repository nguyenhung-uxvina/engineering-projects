---
project: CORTEX-C2
phase: 0
type: project-brief
version: 1.0
created: 2026-02-12
status: draft
---

# PROJECT BRIEF
## CORTEX-C2: CORTEX C2 "THẦN TOÁN"
### AI-based Central Command & Control for Training, Combat & Base Defense

---

## 1. PROJECT IDENTITY

| Field | Value |
|-------|-------|
| **Project Code** | CORTEX-C2 |
| **Product Name** | CORTEX C2 "THẦN TOÁN" |
| **Product Type** | Software Platform (C2 System) |
| **Organization** | Workshop X |
| **Start Date** | 2026-02-12 |
| **Classification** | CONFIDENTIAL |

---

## 2. PROBLEM STATEMENT

Vietnamese military units operate training systems, combat systems, and base defense systems as **isolated silos** — each with separate data, separate interfaces, and no cross-domain intelligence. Commanders must mentally fuse information from multiple screens, multiple systems, and multiple reports to form a situational picture. This creates:

- **Decision lag** — minutes to hours synthesizing multi-system data
- **Information gaps** — no cross-sensor fusion or pattern recognition
- **Training inefficiency** — no data-driven readiness assessment across weapon systems
- **Counter-UAS blind spot** — no integrated detect-to-engage kill chain
- **Zero institutional memory** — no AI learning from accumulated operational data

---

## 3. PRODUCT VISION

> **CORTEX C2 "THẦN TOÁN"** is the AI brain that connects all Workshop X products into one intelligent platform. It transforms raw data from 13+ sensors and weapons into **actionable command decisions** — and gets smarter every day.

### Core Differentiators
| Differentiator | Description |
|---------------|-------------|
| **Platform, not product** | One system grows with customer, not 13 separate purchases |
| **AI that learns** | 6 AI engines improve from operational data (Data Flywheel R1) |
| **3-domain coverage** | Training + Combat + Base Defense on single interface |
| **Hardware-integrated** | Deep integration with Workshop X sensors/weapons (moat vs pure-SW competitors) |
| **Vietnamese-built** | Local development, local content, local support |

---

## 4. MISSION DOMAINS & EDITIONS

### 4.1 Three Mission Domains

| Domain | Core Job-to-be-Done | Key Pain Point |
|--------|---------------------|---------------|
| **Training** | Ensure soldiers achieve combat readiness standards | Multi-system results not integrated; assessment is subjective |
| **Combat** | Make accurate command decisions under time pressure | Sensor data scattered; no AI-assisted decision support |
| **Base Defense** | Detect and respond to threats as early as possible | Sensors not fused; counter-UAS gap; no automated response chain |

### 4.2 Five Product Editions

| Edition | Codename | Target | Entry Price |
|---------|----------|--------|-------------|
| **RANGE** | Trường Bắn | Training range operators, training officers | $15-25K |
| **BASE** | Căn Cứ | Base security officers, surveillance centers | $35-60K |
| **SHIELD** | Lá Chắn | Tactical commanders, C-UAS operators | $60-120K |
| **NAVAL** | Hải Quân | Naval combat centers, ship CIC | $80-200K |
| **ENTERPRISE** | Toàn Diện | Higher command, multi-site operations | $150-300K |

---

## 5. CUSTOMER SEGMENTS (ODI-Based)

| Segment | Market Share | Key Outcomes | Strategy |
|---------|-------------|-------------|----------|
| **A: Decision Dominance** | 30% | C01 (18.0), C02 (17.0), C07 (17.0) | Differentiation |
| **B: Sensor Fusion Seekers** | 25% | D17 (17.5), D09 (17.5), C04 (17.5) | Differentiation |
| **C: Training Analytics Champions** | 25% | T01 (17.5), T18 (17.0), T03 (16.5) | Gateway (entry point) |
| **D: Counter-UAS Urgency** | 20% | D21 (17.5), D22 (17.5), D09 (17.5) | Disruptive |

---

## 6. TECHNOLOGY ARCHITECTURE (Concept Level)

### 6.1 Five-Layer Platform

```
┌─────────────────────────────────────────────────┐
│  LAYER 5: DECISION                              │
│  AI-assisted command decisions, alerts, COP      │
├─────────────────────────────────────────────────┤
│  LAYER 4: AI ENGINES                            │
│  AcousticAI │ VisualAI │ FusionAI               │
│  ThreatAI │ TrainingAI │ BallisticAI             │
├─────────────────────────────────────────────────┤
│  LAYER 3: DATA                                  │
│  Time-series DB │ Event store │ ML model store   │
├─────────────────────────────────────────────────┤
│  LAYER 2: DEVICE INTEGRATION                    │
│  LOMAH │ CAM │ RCWS │ SMASH │ C-UAS │ Drone     │
├─────────────────────────────────────────────────┤
│  LAYER 1: CONNECTIVITY                          │
│  Mesh radio │ Ethernet │ Serial │ TAK │ SAPIENT  │
└─────────────────────────────────────────────────┘
```

### 6.2 Six AI Engines

| Engine | Function | Primary Domain | Data Source |
|--------|----------|---------------|-------------|
| **AcousticAI** | Acoustic detection & classification | Defense, Training | VN-LOMAH, VN-LOMAH-AD, VN-CUAS |
| **VisualAI** | Video analytics, object detection, tracking | All domains | VN-CAM-T1/B1/S1/M1/W1/D1 |
| **FusionAI** | Cross-sensor data fusion, COP generation | Combat, Defense | All sensors combined |
| **ThreatAI** | Threat classification, behavior prediction | Combat, Defense | Radar, acoustic, visual fused |
| **TrainingAI** | Performance analytics, readiness scoring | Training | LOMAH, CAM, scenario data |
| **BallisticAI** | Fire control, ballistic computation | Combat | RCWS, VN-SMASH, weapon systems |

---

## 7. BUSINESS MODEL

### Revenue Architecture
```
HARDWARE SALE → FREE C2 GATEWAY → SUBSCRIPTION REVENUE → UPSELL EDITIONS
     │                │                    │                    │
  VN-LOMAH          CORTEX              $3-60K/yr           RANGE→BASE
  $15K              RANGE               per site            →SHIELD
                    (free)                                   →NAVAL
                                                            →ENTERPRISE
```

### Revenue Targets
| Period | Revenue | Mix |
|--------|---------|-----|
| Year 1 | ~$780K | 80% perpetual / 20% subscription |
| Year 2 | ~$3.0M | 50% perpetual / 50% subscription |
| Year 3 | ~$5.0M | 30% perpetual / 70% subscription |
| **3-Year Total** | **~$8.8M** | Transitioning to platform model |

### Customer Lifetime Value
- Without CORTEX: ~$18K (one-time hardware sales)
- With CORTEX: ~$163K+ (**9x multiplier**)

---

## 8. KEY RISKS

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Engineering capacity insufficient for 5 editions | High | High | Serial development (RANGE → BASE → SHIELD); 80% shared code |
| AI engines underperform without sufficient training data | High | Medium | RANGE generates training data first; data flywheel activates |
| Customer adoption slow (military conservatism) | Medium | Medium | Bundle free RANGE with hardware purchases; demonstrate ROI |
| Competing C2 systems from larger defense primes | Medium | Low | Hardware integration moat; Vietnamese local content advantage |
| Cybersecurity vulnerabilities in networked C2 | High | Medium | Security-by-design; penetration testing; AES-256; air-gapped option |
| Talent shortage (AI + defense domain expertise) | High | High | International partnerships; AI frameworks (TensorFlow/PyTorch); phased hiring |

---

## 9. PHASE 0 → PHASE 1 TRANSITION

### Phase 0 Deliverables
| # | Deliverable | Status |
|---|-------------|--------|
| 1 | ODI Analysis (75 outcomes, 3 domains, 4 segments) | ✅ Complete |
| 2 | Strategic context (IRONMESH restructuring) | ✅ Complete |
| 3 | Competitive/market analysis | ✅ Complete |
| 4 | Systems thinking (loops, archetypes, leverage) | ✅ Complete |
| 5 | Phase 0 synthesis & gate review | ❌ Pending |

### Key Questions for Phase 1
| # | Question | Impact |
|---|----------|--------|
| 1 | Which edition to build FIRST? (RANGE recommended) | Development priority, resource allocation |
| 2 | What existing codebase/framework to build on? | Technology stack selection |
| 3 | What C2 standards must be followed? (SAPIENT, TAK, NATO STANAG?) | Interface requirements |
| 4 | What cybersecurity certification is required? | Security architecture |
| 5 | What is the deployment model? (On-premise, edge, cloud, hybrid?) | Infrastructure requirements |
| 6 | How many simultaneous sensor integrations in V1.0? | Scope control |
| 7 | What AI framework/inference engine? (TensorFlow, ONNX, custom?) | ML pipeline architecture |
| 8 | What is the target latency for real-time sensor display? | Performance requirements |

### TBDs Carried Forward
| TBD | Description | Resolution Owner | Phase |
|-----|-------------|-----------------|-------|
| TBD-001 | Technology stack selection (frontend, backend, DB, ML framework) | Software architect | Phase 1 |
| TBD-002 | Deployment model (on-premise vs edge vs hybrid) | Systems engineer | Phase 1 |
| TBD-003 | SAPIENT/TAK version compliance targets | Systems engineer | Phase 1 |
| TBD-004 | Cybersecurity framework and certification path | Security engineer | Phase 1 |
| TBD-005 | Hardware interface specifications for each Workshop X product | Integration engineer | Phase 1 |
| TBD-006 | AI model training data acquisition strategy | ML engineer | Phase 1 |
| TBD-007 | Subscription billing and license management system | Product manager | Phase 1 |

---

## Cross-References
- [[CORTEX_C2_ODI_Analysis.md]] — Phase 0 ODI analysis (75 outcomes)
- [[Workshop_X_Strategic_Restructuring_IRONMESH.md]] — Strategic context
- [[DroneShield_Musk_Analysis_Workshop_X.md]] — Competitive analysis
- [[Robotics_Startup_2026_Integrated_Analysis.md]] — Technology landscape
- [[Workshop_X_Elon_Musk_Strategy.md]] — Strategic principles
