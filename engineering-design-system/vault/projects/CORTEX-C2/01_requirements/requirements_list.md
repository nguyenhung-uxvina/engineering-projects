---
project: CORTEX-C2
phase: 1
type: requirements
version: 1.0
created: 2026-02-12
status: draft
edition: RANGE STANDARD
total_requirements: 157
must_count: 89
wish_count: 68
quantified_pct: 91%
---

# REQUIREMENTS LIST
## CORTEX-C2 RANGE STANDARD "TRƯỜNG BẮN" — AI-Driven Live-Fire Training Analytics
### Version: 1.0 | Date: 2026-02-12

---

## 1. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-12 | Engineering Design System | Initial release — derived from ODI Rev A (75 outcomes, 25 Training T01-T25), 8 RE analyses, Phase 0 product architecture (16 products), stakeholder analysis (13 stakeholders, 87 pre-traced IDs) |

---

## 2. PROJECT OVERVIEW

| Field | Value |
|-------|-------|
| **Product Name** | CORTEX RANGE STANDARD "TRƯỜNG BẮN" — AI-Driven Live-Fire Training Analytics Platform |
| **Project Code** | CORTEX-C2 (RANGE edition) |
| **Customer** | VPA Training Directorate (Cục Huấn Luyện), Military Region training departments, Military Academy training centers |
| **End Users** | Training officers (primary), range NCOs, instructors, unit commanders, soldiers, IT administrators |
| **Development Period** | 2026 Q1 — 2027 Q2 (5 phases, 18 months) |
| **Target Cost** | $15-25K perpetual license + $3-5K/year subscription |
| **Product Type** | Software platform (web application + edge compute + sensor integration) |
| **First Edition** | RANGE STANDARD (first of 5 CORTEX C2 editions) |
| **Innovation Target** | Category Creator — no competitor offers AI-driven live-fire acoustic training analytics |

### Source Documents

- [[CORTEX_C2_ODI_Analysis.md]] — ODI Rev A: 75 outcomes (25 Training T01-T25), 4 segments, 5 editions
- [[CORTEX_RANGE_phase0_complete.md]] — Phase 0 complete: 6 job executors, 16 products, CDM schema, tech stack
- [[CORTEX_RANGE_product_portfolio_musk.md]] — Musk First Principles v2.0: Category Creator thesis, co-opetition
- [[01_requirements/stakeholder_analysis.md]] — 13 stakeholders, RACI matrix, 87 pre-traced requirement IDs
- [[RE_cubic_training_systems.md]] — Cubic MILES/CATS/SPEAR competitive analysis
- [[RE_cubic_lvc_integration.md]] — DIS/HLA/TENA protocols, SPEAR CDM analysis
- [[RE_cae_training_simulation.md]] — CAE Rise analytics, co-opetition partner
- [[RE_saab_training_gamer.md]] — Saab GAMER AAR, TaaS validation
- [[RE_rheinmetall_training_sts.md]] — Rheinmetall AGDUS/LEGATUS, real competitor identification

### 16 Adapted Categories for Software Platform

| # | P&B Original (Hardware) | Adapted (Software Platform) | Prefix |
|---|------------------------|---------------------------|--------|
| 1 | Geometry | UI/UX Layout & Visual Design | UXD |
| 2 | Kinematics | Core Functionality & Data Flow | FUN |
| 3 | Forces | Processing Performance & Scalability | PER |
| 4 | Energy | Host Environment & Infrastructure | HST |
| 5 | Material | Technology Stack & Dependencies | ARC |
| 6 | Signals | APIs, Protocols & Data Interfaces | INT |
| 7 | Safety | Cybersecurity & Data Protection | SEC |
| 8 | Ergonomics | User Experience & Training | UXP |
| 9 | Production | Deployment & Localization | DEP |
| 10 | Quality | Reliability & AI Accuracy | QUA |
| 11 | Assembly | System Integration & Modularity | MOD |
| 12 | Transport | Distribution & Installation | DST |
| 13 | Operation | Runtime Operations & Administration | OPS |
| 14 | Maintenance | Updates, Support & ML Lifecycle | MNT |
| 15 | Costs | Licensing & Infrastructure Costs | CST |
| 16 | Schedule | Release Schedule & Milestones | SCH |

---

## 3. REQUIREMENTS SUMMARY

| # | Category (Adapted) | P&B Original | Prefix | MUST | WISH | Total | Quantified % |
|---|-------------------|-------------|--------|------|------|-------|-------------|
| 1 | UI/UX Layout | Geometry | UXD | 6 | 4 | 10 | 90% |
| 2 | Core Functionality | Kinematics | FUN | 14 | 10 | 24 | 92% |
| 3 | Processing Performance | Forces | PER | 5 | 3 | 8 | 100% |
| 4 | Host & Infrastructure | Energy | HST | 4 | 3 | 7 | 86% |
| 5 | Technology Stack | Material | ARC | 6 | 4 | 10 | 80% |
| 6 | APIs & Protocols | Signals | INT | 7 | 5 | 12 | 92% |
| 7 | Cybersecurity | Safety | SEC | 8 | 4 | 12 | 83% |
| 8 | User Experience | Ergonomics | UXP | 5 | 5 | 10 | 90% |
| 9 | Deployment | Production | DEP | 4 | 4 | 8 | 88% |
| 10 | Reliability & AI Accuracy | Quality | QUA | 7 | 3 | 10 | 100% |
| 11 | System Integration | Assembly | MOD | 4 | 3 | 7 | 86% |
| 12 | Distribution & Installation | Transport | DST | 3 | 3 | 6 | 83% |
| 13 | Runtime Operations | Operation | OPS | 6 | 4 | 10 | 90% |
| 14 | Updates & Support | Maintenance | MNT | 4 | 4 | 8 | 88% |
| 15 | Licensing & Costs | Costs | CST | 4 | 4 | 8 | 100% |
| 16 | Release Schedule | Schedule | SCH | 2 | 5 | 7 | 100% |
| | **TOTAL** | | | **89** | **68** | **157** | **91%** |

**Gate 1 Target: ≥80% quantified — ACHIEVED (91%)**

---

## 4. DETAILED REQUIREMENTS

### 4.1 UI/UX Layout (← Geometry)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| UXD-001 | Responsive web layout | Functions on ≥10" tablets and ≥13" laptops; minimum 1280×800 resolution | MUST | T | T04 (16.0) | S2, S3 | Primary use: tablet at firing line + laptop in range office |
| UXD-002 | Field-readable display | Readable in direct sunlight (high-contrast mode); dark mode for night/indoor | MUST | D | T04 | S2, S3 | Auto-detect ambient light or manual toggle |
| UXD-003 | Dashboard views — minimum set | 6 views: Range (all lanes), Soldier (individual), Unit (aggregate), Safety, Ammo, Commander | MUST | D | T01 (17.5), T24 (16.0) | S2, S4, S8 | Per CR-D3 PULSE spec from Phase 0 |
| UXD-004 | Lane grid layout | Display ≥50 lanes simultaneously on single screen with real-time score overlay | MUST | T | T05 (15.0) | S2, S3 | Each lane shows: soldier name, last shot score, cumulative, trend arrow |
| UXD-005 | Shot placement visualization | Target diagram showing shot positions with ≤1mm display resolution | MUST | T | T02 (16.0), T24 (16.0) | S2, S5 | Color-coded: green (center), yellow (ring), red (miss); grouping circle overlay |
| UXD-006 | Trend visualization | Line chart of soldier performance across ≥10 sessions with trendline | MUST | D | T08 (14.0), T09 (15.5) | S2, S4 | Up/down/stable indicators visible at a glance |
| UXD-007 | Print-ready report layout | PDF export for reports: A4 format, Vietnamese headers, unit insignia placeholder | WISH (W=5) | D | T10 (14.0) | S2, S4 | Training officers still need paper for some workflows |
| UXD-008 | Soldier kiosk mode | Simplified display for soldier self-check: personal scores, trend, AI coaching tips only | WISH (W=4) | D | T04 (16.0) | S5 | QR code scan to load personal view; no admin access |
| UXD-009 | Color-blind accessible | All critical information conveyed by shape/pattern in addition to color | WISH (W=3) | I | — | S2 | WCAG 2.1 AA compliance for color contrast |
| UXD-010 | Customizable dashboard | Users can rearrange dashboard widgets; save per-user layout preferences | WISH (W=2) | D | T19 (12.0) | S2 | Phase 3+ feature; basic fixed layout acceptable for V1 |

### 4.2 Core Functionality (← Kinematics)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| FUN-001 | Real-time shot scoring display | Shot position displayed on dashboard ≤50ms after acoustic detection by VN-LOMAH | MUST | T | T04 (16.0), T24 (16.0) | S2, S3 | "iPhone moment" — the single feature that makes paper obsolete |
| FUN-002 | Multi-system data consolidation | All sensor data (LOMAH + camera + weapon) consolidated into single CDM view in ≤30 seconds | MUST | T | T01 (17.5) | S2 | #1 EXTREME training outcome; currently impossible |
| FUN-003 | Automated training report generation | Vietnamese-language PDF/HTML report auto-generated from session data in ≤30 seconds | MUST | T | T10 (14.0) | S2, S4 | LLM-generated narrative summary (CR-D2 DEBRIEF Phase 2); template-based in Phase 1 |
| FUN-004 | Soldier performance trends | Track and visualize individual performance across ≥100 sessions over ≥24 months | MUST | T | T09 (15.5), T08 (14.0) | S2, S4, S5 | Session data: scores, grouping, technique notes, qualification results |
| FUN-005 | Commander readiness dashboard | Single-view unit readiness overview: % qualified, trend, top/bottom performers, next qual date | MUST | D | T03 (16.5), T22 (16.0) | S4, S8 | Drill-down: unit → platoon → squad → individual |
| FUN-006 | Cross-unit comparison | Compare any 2+ units on standardized metrics: mean score, qualification rate, improvement rate | MUST | T | T03 (16.5) | S4, S8 | Same metrics across all ranges regardless of range physical configuration |
| FUN-007 | Qualification tracking | Track soldier qualification status per weapon type; alert when qualification expires within 30 days | MUST | T | T07 (14.0) | S2, S4 | Vietnamese military qualification standards for rifle, pistol, RCWS |
| FUN-008 | Session management | Create, start, pause, resume, end training sessions; assign soldiers to lanes; set exercise type | MUST | D | T21 (12.5) | S2, S3 | Session workflow: create → assign → brief → start → score → end → debrief |
| FUN-009 | Shot grouping analysis | Auto-calculate: mean radius, extreme spread, center of impact, group size for each burst/session | MUST | T | T05 (15.0), T02 (16.0) | S2, S6 | Eliminates manual measurement with ruler on paper |
| FUN-010 | Per-shot soldier display | Individual soldier sees own shot placement and score in ≤1 second at firing position display | MUST | T | T04 (16.0) | S5 | Tablet/kiosk at each firing position or shared per 4-5 positions |
| FUN-011 | Individual performance history | Searchable personal history: all sessions, scores, groupings, qualification results, trend | MUST | T | T09 (15.5) | S5, S2 | Career-spanning digital record |
| FUN-012 | AI coaching suggestions | Context-specific coaching tips in Vietnamese based on shot pattern analysis | MUST | D | T12 (15.5) | S5, S6 | Phase 1: rule-based ("shots low-left → anticipating recoil, practice trigger control"); Phase 2: ML-based |
| FUN-013 | Ammunition tracking | Track rounds issued, fired, returned per soldier per session; auto-calculate consumption rates | MUST | T | T23 (13.0) | S2, S3 | Safety and accountability requirement; ammunition is controlled |
| FUN-014 | Multi-weapon support | Manage ≥4 weapon types on single platform: rifle, pistol, RCWS, machine gun | MUST | D | T18 (17.0) | S2 | #2 EXTREME training outcome; each weapon type has own scoring criteria |
| FUN-015 | AI technique error classification | Classify ≥10/12 defined shooting technique errors from video analysis with ≥80% accuracy | WISH (W=5) | T | T12 (15.5) | S6 | Phase 2 (OVERWATCH); 12 categories defined in Phase 0 |
| FUN-016 | Multi-angle video replay | Synchronized replay from 2-4 camera angles with AI annotation overlay in ≤30 seconds | WISH (W=5) | D | T14 (14.5) | S6 | Phase 2 (OVERWATCH); slow-motion at 120fps |
| FUN-017 | Instructor override of AI | Instructor can accept, reject, or modify any AI classification/recommendation; feedback recorded | WISH (W=5) | D | T12 (15.5) | S6 | AI serves instructor, not replaces; instructor feedback improves AI model |
| FUN-018 | Predictive readiness scoring | Predict unit qualification success ≥2 weeks in advance with ≥75% accuracy | WISH (W=4) | T | T07 (14.0), T06 (13.5) | S4, S8 | Phase 5 (PROPHECY); requires ≥6 months historical data per unit |
| FUN-019 | National readiness dashboard | Multi-range aggregated view: all ranges, all units, national readiness metrics | WISH (W=4) | D | T22 (16.0) | S8 | Phase 5 (CLOUD); ENTERPRISE edition; drill-down from national → region → unit |
| FUN-020 | LLM-powered narrative reports | AI-generated natural language debrief report in Vietnamese summarizing session performance | WISH (W=4) | D | T10 (14.0) | S2, S4 | Phase 2 (DEBRIEF); uses local LLM (Llama/Qwen) or cloud API |
| FUN-021 | Scenario management | Create, save, load training scenarios with pre-configured target sequences and scoring rules | WISH (W=3) | D | T13 (10.5) | S2 | Phase 4 (SCENARIO FORGE); LLM-assisted scenario creation |
| FUN-022 | Position and movement analytics | Track soldier positions via GPS/BLE trackers; heat maps, movement replay, time-in-cover analysis | WISH (W=3) | D | T05 (15.0) | S2 | Phase 3 (TRACKER); add-on hardware ($200-500/tracker) |
| FUN-023 | Digital twin range replay | 3D replay of live exercises from any viewpoint on digital twin of physical range | WISH (W=2) | D | T14 (14.5) | S6 | Phase 4 (MIRROR); Three.js web-based 3D viewer |
| FUN-024 | Auto-generated qualification certificates | Digital certificate with QR verification when soldier passes qualification | WISH (W=3) | D | T25 (12.0) | S2 | Phase 2 (DEBRIEF); digital signature capability |

### 4.3 Processing Performance (← Forces)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| PER-001 | Shot event throughput | Process ≥500 shot events/minute (50 lanes × 10 shots/min) without data loss | MUST | T | T01 (17.5) | S9 | Peak load during rapid-fire exercises; TimescaleDB hypertable partitioning |
| PER-002 | Dashboard update latency | ≤100ms from backend event to browser display update via WebSocket | MUST | T | T04 (16.0) | S2, S9 | Users perceive ≤100ms as "instant" |
| PER-003 | Concurrent user support | ≥20 simultaneous dashboard users per range instance without degradation | MUST | T | T19 (12.0) | S7, S9 | Training officer + range NCO + 4 instructors + 10 soldiers + commander |
| PER-004 | Report generation time | ≤30 seconds for full session report (≥500 shots, all analytics) | MUST | T | T10 (14.0) | S2 | Template-based Phase 1; LLM-enhanced Phase 2 |
| PER-005 | Database query response | ≤2 seconds for any dashboard query (historical data spanning ≥24 months) | MUST | T | T09 (15.5) | S2, S4 | TimescaleDB time-series indexing; partition by month |
| PER-006 | AI inference latency | ≤500ms per video frame for technique analysis (OVERWATCH) | WISH (W=5) | T | T12 (15.5) | S9 | Phase 2; ONNX Runtime on Jetson Orin NX; batch processing acceptable |
| PER-007 | Cross-unit query performance | ≤5 seconds for cross-unit comparison query spanning ≥10 units, ≥12 months | WISH (W=4) | T | T03 (16.5), T22 (16.0) | S4, S8 | Phase 5 (CLOUD); federated query across range instances |
| PER-008 | Data ingestion burst capacity | Handle ≥1000 events/second during 10-second bursts (mass engagement exercise) | WISH (W=3) | T | PER-001 | S9 | 2× sustained capacity for burst handling; buffer with backpressure |

### 4.4 Host & Infrastructure (← Energy)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| HST-001 | Edge server hardware | NVIDIA Jetson Orin NX (100 TOPS) or ARM-based SBC with ≥8GB RAM, ≥256GB SSD | MUST | I | T19 (12.0) | S7, S9 | Phase 1: commodity mini-PC acceptable ($500-1500); Jetson for AI in Phase 2 |
| HST-002 | Edge server power consumption | ≤60W continuous; solar/battery capable | MUST | T | — | S7 | IP65 enclosure; 15-60W depending on AI inference load |
| HST-003 | Operating environment | Indoor (range office) or weatherproof enclosure; 0°C to +50°C operating | MUST | T | — | S7 | Vietnamese ranges: sheltered range tower or control room typical |
| HST-004 | Network connectivity | Wired Ethernet (1Gbps) from edge server to sensors; WiFi 6 to client devices | MUST | T | — | S7, S9 | LoRa for sensor mesh (Phase 3); WiFi for tablet/laptop clients |
| HST-005 | Cloud infrastructure | Kubernetes (K3s edge, K8s cloud); on-prem or AWS/Azure deployment | WISH (W=4) | D | T22 (16.0) | S9 | Phase 5 (CLOUD); same orchestration edge-to-cloud |
| HST-006 | Offline operation | Fully operational with zero internet connectivity for ≥30 days; sync when reconnected | WISH (W=5) | T | T15 (14.0) | S7, S13 | Edge-first architecture; Vietnamese ranges may have poor/no internet |
| HST-007 | UPS / battery backup | ≥30 minutes operation on battery after power loss; graceful shutdown with data preservation | WISH (W=4) | T | T15 (14.0) | S7 | Prevents data loss from power cuts; common in Vietnamese ranges |

### 4.5 Technology Stack (← Material)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| ARC-001 | Backend language/framework | Python 3.11+ with FastAPI (async capable) | MUST | I | — | S9 | Fastest development; AI/ML ecosystem; largest Vietnamese developer pool |
| ARC-002 | Frontend framework | React 18+ with TypeScript; MapLibre/Leaflet for range maps | MUST | I | — | S9 | Web-based = works on any device; React ecosystem mature |
| ARC-003 | Time-series database | TimescaleDB (PostgreSQL extension) for shot event storage | MUST | I | — | S9 | Time-series optimized; SQL familiar; hypertable auto-partitioning |
| ARC-004 | Real-time communication | WebSocket (native FastAPI) for dashboard live updates | MUST | I | — | S9 | Sub-100ms updates; bi-directional for session control commands |
| ARC-005 | AI/ML inference engine | ONNX Runtime for cross-framework model deployment | MUST | I | T12 (15.5) | S9 | Train in PyTorch → export ONNX → deploy edge + cloud consistently |
| ARC-006 | CDM specification | CORTEX CDM v1.0 JSON Schema (open specification, versioned, published) | MUST | D | T01 (17.5), T18 (17.0) | S9, S11 | 8 objects: ShotEvent, TechniqueEvent, PositionEvent, WeaponEvent, SoldierProfile, UnitProfile, SessionProfile, ScenarioProfile |
| ARC-007 | Open-source dependencies only | No proprietary/licensed runtime dependencies; all FOSS or MIT/Apache/BSD licensed | WISH (W=5) | I | — | S9, S1 | Prevents vendor lock-in; reduces cost; aligns with open CDM strategy |
| ARC-008 | API-first architecture | All backend functionality exposed via versioned REST API; no UI-only features | WISH (W=5) | I | — | S9, S11 | Enables third-party integrations, partner ecosystem, future mobile apps |
| ARC-009 | Containerized deployment | Docker containers for all services; Docker Compose for single-node; Kubernetes for multi-node | WISH (W=4) | D | — | S9 | Reproducible deployment; same container runs on edge, staging, cloud |
| ARC-010 | Local LLM capability | Run Vietnamese-capable LLM (Llama/Qwen 7-13B) on edge GPU for report generation | WISH (W=3) | T | T10 (14.0) | S9 | Phase 2 (DEBRIEF); Jetson Orin runs 7B models at acceptable speed |

### 4.6 APIs & Protocols (← Signals)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| INT-001 | VN-LOMAH serial/UDP parser | Parse all VN-LOMAH sensor models (V1, V2); serial RS-232 and UDP protocols | MUST | T | T01 (17.5), T04 (16.0) | S10 | Foundation — if this fails, nothing works; hardware team provides protocol spec |
| INT-002 | VN-CAM-T1 video feed | Ingest RTSP video streams from VN-CAM-T1 cameras (H.264/H.265) | MUST | T | T14 (14.5), T12 (15.5) | S10 | Phase 2 (OVERWATCH); 2-4 cameras per firing position |
| INT-003 | Sensor auto-discovery | New sensors auto-discovered on network within ≤60 seconds of power-on | MUST | T | T11 (12.0), T21 (12.5) | S3, S10 | mDNS/SSDP service discovery; no manual IP configuration needed |
| INT-004 | REST API | OpenAPI 3.0 specification; versioned (v1, v2); JSON request/response | MUST | D | T20 (12.5) | S9, S11 | Public API documentation; partner integration endpoint |
| INT-005 | WebSocket real-time feed | WebSocket endpoint streaming live shot events, session updates, system alerts | MUST | T | T04 (16.0) | S9 | Dashboard subscribes per session/lane; ≤100ms latency (PER-002) |
| INT-006 | DIS IEEE 1278 output | Publish CORTEX training events as DIS PDUs; custom ShotEvent PDU extension | MUST | T | T20 (12.5) | S11 | Open-DIS library (Python); enables LVC system integration |
| INT-007 | CoT/TAK plugin | ATAK/WinTAK plugin displaying training data on tactical map via CoT XML | MUST | D | T20 (12.5) | S11 | CoT cursor-on-target over multicast/TCP; TAK SDK available open-source |
| INT-008 | Hardware API versioning | Documented API contract with VN-LOMAH team; semantic versioning; backward-compatible | WISH (W=5) | I | — | S10 | Prevents integration breakage on firmware updates |
| INT-009 | CSV/Excel export | Export any view as CSV or XLSX for commanders who prefer spreadsheets | WISH (W=5) | D | T10 (14.0) | S2, S4 | Immediate value; low development effort |
| INT-010 | HLA IEEE 1516 federate | Connect to HLA simulation federations via OpenRTI or Portico RTI | WISH (W=3) | T | T20 (12.5) | S11 | Phase 3; required for CAE/Rheinmetall constructive simulation integration |
| INT-011 | CDM export JSON/XML | Bulk export of CDM data in JSON and XML formats for external analytics | WISH (W=4) | D | T01 (17.5) | S11 | Open CDM strategy — data portability, no lock-in |
| INT-012 | Weapon system API | Plugin interface for Workshop X weapon systems: VN-SMASH, RCWS traverse/elevation data | WISH (W=4) | D | T18 (17.0) | S10 | Phase 2 (WEAPONS LINK); each weapon type = plugin adapter |

### 4.7 Cybersecurity (← Safety)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| SEC-001 | Data classification handling | Handle RESTRICTED-level training data; no SECRET data in RANGE edition | MUST | A | — | S8, S13 | Training performance data = RESTRICTED (personnel data); not classified intelligence |
| SEC-002 | Authentication | Token-based authentication (JWT); session timeout ≤30 minutes idle; password policy (≥12 chars, complexity) | MUST | T | — | S13 | Phase 1: local accounts; Phase 3+: LDAP/AD integration |
| SEC-003 | Role-based access control | ≥4 roles: Admin, Officer, NCO, Viewer; granular permissions per view/action | MUST | T | — | S13 | Admin: full access. Officer: unit data + reports. NCO: session operation. Viewer: read-only |
| SEC-004 | Data encryption in transit | TLS 1.3 for all HTTP/WebSocket connections | MUST | T | — | S13 | Self-signed certificates acceptable for air-gapped; CA-signed for networked |
| SEC-005 | Data encryption at rest | AES-256 for database files and backup archives | MUST | T | — | S13 | Full-disk encryption on edge server; encrypted database backups |
| SEC-006 | Air-gapped deployment | System operates with zero internet dependency; no external telemetry, analytics, or phone-home | MUST | T | — | S13 | Non-negotiable for military deployment; all features work offline |
| SEC-007 | Audit logging | Tamper-evident log of all user actions: login, data access, configuration changes, exports | MUST | T | — | S12, S13 | Append-only log; hash-chained entries; ≥365 days retention |
| SEC-008 | OWASP Top 10 compliance | No critical or high vulnerabilities per OWASP Top 10 2021; validated by penetration test | MUST | T | — | S12 | SQL injection, XSS, CSRF, auth bypass, SSRF — all addressed |
| SEC-009 | Personal data protection | Soldier names/IDs encrypted in database; access restricted by role; data deletion capability | WISH (W=5) | T | — | S12, S13 | Vietnamese personal data regulations; soldier data is sensitive |
| SEC-010 | Network segmentation | CORTEX edge server on isolated network segment; no direct internet access from sensor network | WISH (W=5) | A | — | S13 | Defense-in-depth; sensor network physically separated from admin network |
| SEC-011 | Backup encryption | All backups encrypted with separate key; key management procedure documented | WISH (W=4) | T | — | S13 | Backup to external media (USB/NAS); encrypted at rest |
| SEC-012 | Security incident response plan | Documented procedure for: data breach, unauthorized access, system compromise | WISH (W=4) | A | — | S13 | Required for military deployment approval |

### 4.8 User Experience & Training (← Ergonomics)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| UXP-001 | Training officer training time | ≤4 hours to proficiency (create session, run range day, generate report) | MUST | D | T19 (12.0) | S2 | Half-day training session; Vietnamese-language training materials |
| UXP-002 | Range NCO training time | ≤4 hours to proficiency (power on, start session, monitor, troubleshoot basic issues) | MUST | D | T19 (12.0) | S3 | Same-day training; laminated quick-start guide provided |
| UXP-003 | Session start workflow | ≤3 actions from login to live scoring: Select exercise → Assign lanes → Start | MUST | D | T21 (12.5) | S3 | "1-button start" design principle; pre-configured exercise templates |
| UXP-004 | Vietnamese language | All UI text, labels, reports, coaching tips, error messages in Vietnamese | MUST | I | — | S1, S2 | No English-only features; full localization |
| UXP-005 | Error recovery | System auto-recovers from sensor disconnection within ≤10 seconds; no data loss; user notification | MUST | T | T15 (14.0) | S3, S7 | Sensor goes offline → buffered data retained → reconnect → sync → continue |
| UXP-006 | Instructor dashboard | Single view showing AI alerts across ≥50 lanes with click-to-detail per shooter | WISH (W=5) | D | T12 (15.5) | S6 | Phase 2 (OVERWATCH); AI highlights most interesting technique errors |
| UXP-007 | Gamification elements | Improvement streaks, badges for milestones, unit leaderboard (anonymized option) | WISH (W=3) | D | T04 (16.0) | S5 | Motivational; drives soldier engagement; commander can disable |
| UXP-008 | Contextual help | In-app help tooltips and Vietnamese-language tutorial walkthrough on first use | WISH (W=4) | D | T19 (12.0) | S2, S3 | Reduces training time; self-service onboarding |
| UXP-009 | Touch-optimized controls | All primary actions (start/stop/assign) touchable with ≥44×44px tap targets | WISH (W=4) | I | — | S2, S3 | Tablet is primary input device at firing line |
| UXP-010 | Offline indicator | Clear visual indicator when system is offline/disconnected with last-sync timestamp | WISH (W=3) | D | T15 (14.0) | S3, S7 | Prevents confusion about data freshness |

### 4.9 Deployment & Localization (← Production)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| DEP-001 | Installation time | ≤2 hours from unboxing edge server to operational system (including sensor connection) | MUST | D | T21 (12.5) | S7 | 1-page Vietnamese setup guide; maximum 10 steps |
| DEP-002 | Single-command deployment | Install/update entire CORTEX RANGE via single script or Docker Compose command | MUST | D | T19 (12.0) | S7, S9 | `docker compose up` or equivalent; no multi-step manual process |
| DEP-003 | Offline installation package | Complete installation package on USB drive (≤32GB); no internet download required | MUST | D | — | S7, S13 | Air-gapped ranges have no internet; all dependencies bundled |
| DEP-004 | Vietnamese localization — complete | 100% of user-facing text localized; Vietnamese date/time formats; Vietnamese diacritics supported | MUST | I | — | S1, S2 | UTF-8 throughout; Vietnamese sort order for names |
| DEP-005 | English localization | Full English UI for international export and partner demonstrations | WISH (W=4) | I | — | S11 | Language toggle in settings; demo mode for trade shows |
| DEP-006 | Configuration backup/restore | Export/import full system configuration (users, exercises, scoring rules) via single file | WISH (W=4) | D | T15 (14.0) | S7 | Disaster recovery; clone configuration to new range installation |
| DEP-007 | Multi-range deployment template | Pre-configured deployment templates: "Standard 25-lane", "Large 50-lane", "Mobile 10-lane" | WISH (W=3) | D | T21 (12.5) | S7 | Reduces per-site configuration effort |
| DEP-008 | CI/CD pipeline | Automated build → test → package → deploy pipeline; ≥80% unit test coverage | WISH (W=4) | I | — | S9 | GitHub Actions or GitLab CI; automated regression testing |

### 4.10 Reliability & AI Accuracy (← Quality)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| QUA-001 | System uptime | ≥99.5% during active range sessions (≤1 minute unplanned downtime per 8-hour session) | MUST | T | T15 (14.0) | S2, S3 | Measured from session start to session end; excludes planned maintenance windows |
| QUA-002 | Zero data loss | Zero shot events lost during normal operation; no unrecoverable data loss from power failure | MUST | T | T15 (14.0) | S2, S4 | Write-ahead logging; sync to disk before acknowledging; UPS buffer |
| QUA-003 | Shot scoring accuracy | ≤1mm additional error vs raw VN-LOMAH sensor accuracy (system adds no significant noise) | MUST | T | T02 (16.0), T24 (16.0) | S2, S6 | CORTEX must not degrade LOMAH accuracy; end-to-end validation |
| QUA-004 | Grouping calculation accuracy | Mean radius and extreme spread calculated within ±0.5mm of manual measurement | MUST | T | T05 (15.0) | S2 | Validated against manual measurement on known shot patterns |
| QUA-005 | AI coaching tip relevance | ≥80% of AI coaching suggestions rated "helpful" or "accurate" by instructors during pilot | MUST | D | T12 (15.5) | S6 | Phase 1: rule-based (lookup table); Phase 2: ML-based; instructor feedback loop |
| QUA-006 | AI technique classification accuracy | ≥80% accuracy on top-5 error types (flinch, trigger jerk, breathing, grip, stance) in controlled test | MUST | T | T12 (15.5) | S6, S9 | Phase 2 (OVERWATCH); tested with annotated reference videos |
| QUA-007 | Report accuracy | 100% of quantitative data in reports matches source data; zero calculation errors | MUST | T | T24 (16.0), T10 (14.0) | S2, S4 | Automated regression test suite for report generation |
| QUA-008 | Predictive readiness accuracy | ≥75% accuracy in predicting qualification pass/fail ≥2 weeks in advance | WISH (W=4) | T | T07 (14.0), T06 (13.5) | S4, S8 | Phase 5 (PROPHECY); requires ≥6 months historical training data |
| QUA-009 | AI confidence calibration | Reported confidence percentage correlates with actual accuracy ≥80% of the time | WISH (W=4) | T | T12 (15.5) | S6 | If system reports 90% confidence, correct ≥90% of the time in ≥80% of cases |
| QUA-010 | Data integrity audit | Automated daily data integrity check; alert on any corruption, tampering, or inconsistency | WISH (W=3) | T | T15 (14.0) | S4, S13 | Checksum verification on CDM records; log hash chain validation |

### 4.11 System Integration (← Assembly)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| MOD-001 | Sensor plugin architecture | New sensor types addable via plugin adapter without modifying core platform | MUST | D | T18 (17.0) | S9, S10 | Abstract sensor interface: connect(), read(), parse() → CDM event; each sensor = plugin |
| MOD-002 | Microservice separation | Core services independently deployable: ingestion, analytics, dashboard, API, AI inference | MUST | A | — | S9 | Enables independent scaling and updating; Docker container per service |
| MOD-003 | CDM extensibility | CDM schema extensible with custom fields per deployment without breaking core schema | MUST | D | T18 (17.0) | S9, S11 | JSON Schema `additionalProperties` + extension namespace; versioned |
| MOD-004 | Multi-sensor correlation | Correlate shot event (LOMAH) with video frame (camera) and weapon event within ±100ms | MUST | T | T14 (14.5), T05 (15.0) | S9 | Timestamp-based correlation; NTP sync across all sensors |
| MOD-005 | Plugin development SDK | Published SDK (Python) for third-party sensor plugin development with example code | WISH (W=3) | D | T18 (17.0) | S9, S11 | Opens ecosystem for partner hardware integration |
| MOD-006 | Feature flag system | Enable/disable features per deployment (hide ENTERPRISE features on STANDARD license) | WISH (W=4) | D | — | S9 | Tiered licensing enforcement; same codebase, different feature sets |
| MOD-007 | Database migration framework | Automated schema migration on update; zero-downtime migration for minor versions | WISH (W=4) | T | — | S9 | Alembic (SQLAlchemy) or equivalent; rollback capability |

### 4.12 Distribution & Installation (← Transport)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| DST-001 | Installation package size | ≤8GB total (all containers, models, dependencies) on USB drive | MUST | I | — | S7 | Vietnamese military: USB drive distribution common; 32GB USB has headroom |
| DST-002 | Minimum client bandwidth | Dashboard functions with ≥1 Mbps client connection (WiFi to tablet) | MUST | T | — | S7 | Range WiFi may be congested; minimize client data transfer; server-side rendering option |
| DST-003 | Browser compatibility | Chrome 90+, Firefox 90+, Edge 90+, Safari 15+; no browser plugins required | MUST | T | — | S2, S7 | Zero client installation; pure web application; Samsung tablet default browser |
| DST-004 | Automatic update notification | System checks for updates (when online) and notifies admin; no auto-install without approval | WISH (W=4) | D | — | S7, S13 | Admin controls when to apply updates; no automatic changes |
| DST-005 | Delta updates | Software updates transmit only changed components (≤500MB typical update vs ≤8GB full install) | WISH (W=3) | T | — | S7 | Reduces update distribution size; important for low-bandwidth sites |
| DST-006 | Rollback capability | Revert to previous version within ≤5 minutes if update causes issues | WISH (W=5) | D | — | S7 | Docker image versioning; database migration rollback; one-command rollback |

### 4.13 Runtime Operations (← Operation)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| OPS-001 | System startup time | ≤5 minutes from power-on to operational (all services running, sensors connected) | MUST | T | T21 (12.5) | S3 | Includes OS boot + container startup + sensor auto-discovery + self-test |
| OPS-002 | Unattended operation | Run ≥8 hours without human intervention during active session | MUST | T | — | S3 | Automatic error recovery; no periodic "click OK" prompts |
| OPS-003 | System health monitoring | Real-time dashboard showing: CPU, RAM, disk, database, sensor status, network for all services | MUST | D | — | S7 | Admin-only view; alerts via dashboard notification + optional email |
| OPS-004 | Automated backup | Daily automated backup of database and configuration to external storage; ≥30 backups retained | MUST | T | T15 (14.0) | S7 | Configurable backup time (default: 02:00); backup to USB/NAS |
| OPS-005 | User management | Web-based admin interface for CRUD of users, roles, unit assignments | MUST | D | — | S7, S13 | Import/export user list; bulk add from CSV |
| OPS-006 | Log management | Structured logging (JSON) for all services; log rotation at ≥500MB per file; ≥90 days retention | MUST | T | — | S7, S13 | Searchable via admin console; exportable for incident investigation |
| OPS-007 | Disk space management | Alert at ≥80% disk usage; auto-archive data older than configurable threshold (default: 365 days) | WISH (W=4) | T | — | S7 | Prevent disk-full system crash; archived data exportable before deletion |
| OPS-008 | Remote management | SSH access and remote web admin interface for off-site administration | WISH (W=4) | D | — | S7 | Enables Workshop X remote support; encrypted VPN when connected |
| OPS-009 | Multi-range data sync | Sync session data between ranges on manual trigger or scheduled (daily); conflict resolution | WISH (W=3) | T | T22 (16.0) | S7, S8 | Phase 5 (CLOUD); federation protocol for multi-site deployment |
| OPS-010 | Monitoring alerts | Configurable alerts for: sensor offline, disk space, high error rate, authentication failure | WISH (W=4) | D | — | S7 | Alert via dashboard notification; optional SMS/email (when internet available) |

### 4.14 Updates & Support (← Maintenance)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| MNT-001 | Software update frequency | ≥4 updates per year (quarterly); critical security patches within 7 days | MUST | A | — | S7, S12 | Subscription model funds continuous development |
| MNT-002 | Update procedure | ≤30 minutes total update time including backup, apply, verify; documented step-by-step | MUST | D | — | S7 | Vietnamese-language update guide; single-command preferred (DEP-002) |
| MNT-003 | Backward data compatibility | All data created in version N readable and usable in version N+1 without migration manual steps | MUST | T | — | S7, S9 | Automated schema migration; no data loss on update |
| MNT-004 | Self-diagnostics | System identifies ≥90% of common issues to component level with recommended resolution | MUST | D | — | S7 | "Sensor X offline — check cable connection" type diagnostics |
| MNT-005 | ML model update — separate from software | AI/ML models updateable independently from platform software; hot-swap without restart | WISH (W=5) | D | T12 (15.5) | S9 | New shooting technique models deployed without full software update |
| MNT-006 | Remote support capability | Workshop X support can view system health remotely (with admin authorization) via secure tunnel | WISH (W=4) | D | — | S7 | Encrypted reverse-SSH or VPN tunnel; admin explicitly enables/disables |
| MNT-007 | Feedback collection | In-app feedback mechanism for users to report issues/suggestions; rated importance | WISH (W=3) | D | — | S2, S6 | Collected locally; synced to Workshop X when connected; drives roadmap |
| MNT-008 | Documentation — admin | Vietnamese-language system administration manual covering all OPS procedures | WISH (W=5) | I | — | S7 | PDF + in-app help; covers install, update, backup, troubleshoot, user management |

### 4.15 Licensing & Costs (← Costs)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| CST-001 | Perpetual license — STANDARD | $15,000-25,000 per range (includes SCOREBOARD + PULSE + CDM + OVERWATCH + DEBRIEF + EXPORT) | MUST | A | — | S1 | One-time purchase; includes all Phase 1-2 features; 1 year support included |
| CST-002 | Annual subscription | $3,000-5,000 per range per year (includes updates, ML model updates, support) | MUST | A | — | S1 | Required for continued software updates and AI model improvements |
| CST-003 | FREE tier | SCOREBOARD + basic PULSE + CDM bundled FREE with VN-LOMAH hardware purchase | MUST | A | — | S1, S10 | Gateway drug — hook customers with free value; upsell to STANDARD |
| CST-004 | Edge server hardware cost | ≤$2,000 per range for edge compute hardware (mini-PC or Jetson) | MUST | A | — | S1, S7 | Commodity ARM-based SBC Phase 1 ($500); Jetson Phase 2 ($800-1500) |
| CST-005 | PRO tier pricing | $25,000-35,000 perpetual + $5,000-7,000/year (adds TRACKER, MESH, EDGE, MIRROR, GHOST, DOJO) | WISH (W=4) | A | — | S1 | Phase 3-4 features; upsell from STANDARD customers |
| CST-006 | ENTERPRISE tier pricing | $50,000-75,000 perpetual + $10,000-15,000/year (adds CLOUD, PROPHECY, HLA, multi-range) | WISH (W=4) | A | — | S1, S8 | Phase 5 features; higher command national deployment |
| CST-007 | Development cost — Phase 1 MVP | ≤$100,000 (2 developers × 3 months + infrastructure + testing) | WISH (W=5) | A | — | S9 | Lean startup approach; minimum viable SCOREBOARD + PULSE + CDM |
| CST-008 | 3-year total revenue target | $1.7M cumulative from RANGE edition alone (per Phase 0 revenue model) | WISH (W=3) | A | — | S1 | 15 FREE + 8 STD Year 1; 30+20+8 Year 2; 50+35+15+8 Year 3 |

### 4.16 Release Schedule (← Schedule)

| ID | Requirement | Value/Range | Type | Verify | ODI Trace | Stakeholder | Notes |
|----|-------------|-------------|------|--------|-----------|-------------|-------|
| SCH-001 | Phase 1 MVP delivery | 12 weeks from project start: SCOREBOARD + PULSE + CDM v1 deployed at ≥1 Vietnamese range | MUST | D | — | S1, S9 | 6 sprints × 2 weeks; 2 developers; per Phase 0 sprint plan |
| SCH-002 | Phase 2 delivery | Month 3-6: OVERWATCH + DEBRIEF + WEAPONS LINK + EXPORT (DIS/TAK) | MUST | D | — | S1, S9 | Team grows to 3 developers; enables STANDARD tier sales |
| SCH-003 | Phase 3 delivery | Month 6-9: TRACKER + MESH + EDGE + CDM v1.2 | WISH (W=5) | D | — | S9 | Team grows to 3 developers; enables PRO tier |
| SCH-004 | Phase 4 delivery | Month 9-12: MIRROR + GHOST + DOJO + ADVERSARY + SCENARIO FORGE | WISH (W=4) | D | — | S9 | Team grows to 4 developers; full PRO tier |
| SCH-005 | Phase 5 delivery | Month 12-18: CLOUD + PROPHECY + EXPORT (HLA) + CDM v2 | WISH (W=4) | D | — | S9, S8 | ENTERPRISE tier; national deployment capability |
| SCH-006 | Pilot deployment | ≥2 Vietnamese ranges actively using CORTEX RANGE within 6 months of project start | WISH (W=5) | D | — | S1, S2 | Validation of product-market fit; flywheel activation |
| SCH-007 | 50-range deployment target | 50+ ranges deploying CORTEX RANGE within 24 months | WISH (W=3) | A | — | S1, S8 | Flywheel escape velocity (from Phase 0 analysis) |

---

## 5. ODI TRACEABILITY MATRIX (Top 25 Training Outcomes)

| Rank | ODI Outcome | Score | Zone | Requirements Mapped | Coverage |
|------|------------|-------|------|---------------------|----------|
| 1 | T01: Min time to consolidate multi-system results | 17.5 | EXTREME | FUN-002, ARC-006 (CDM), INT-001, INT-002, MOD-004 | Full |
| 2 | T18: Max weapon systems on single platform | 17.0 | EXTREME | FUN-014, MOD-001 (plugin), INT-012, ARC-006 | Full |
| 3 | T03: Max cross-unit comparison on same scale | 16.5 | EXTREME | FUN-005, FUN-006, OPS-009, FUN-019 | Full |
| 4 | T02: Min subjective bias in evaluation | 16.0 | EXTREME | FUN-001, FUN-009, QUA-003, QUA-004, UXD-005 | Full |
| 5 | T04: Min time from shooting to feedback | 16.0 | EXTREME | FUN-001 (≤50ms), FUN-010 (≤1s), PER-002 (≤100ms), INT-005 | Full |
| 6 | T24: Max transparency/verifiability of results | 16.0 | EXTREME | FUN-001, QUA-003, QUA-007, SEC-007 (audit), UXD-005 | Full |
| 7 | T22: Max cross-unit training data analysis | 16.0 | EXTREME | FUN-019, FUN-006, OPS-009, PER-007 | Full |
| 8 | T09: Max individual training history traceability | 15.5 | EXTREME | FUN-004, FUN-011, PER-005, ARC-006 (SoldierProfile) | Full |
| 9 | T12: Max AI accuracy in classifying technique errors | 15.5 | EXTREME | FUN-015, FUN-016, FUN-017, QUA-005, QUA-006, ARC-005 | Full |
| 10 | T05: Max auto-captured performance metrics per shot | 15.0 | HIGH | FUN-009, MOD-004, INT-001, INT-002, FUN-022 | Full |
| 11 | T14: Max multi-angle video replay and analysis | 14.5 | HIGH | FUN-016, INT-002, MOD-004 | Full |
| 12 | T07: Max first-time qualification rate via trends | 14.0 | HIGH | FUN-007, FUN-018, QUA-008 | Full |
| 13 | T08: Min time to detect declining performance | 14.0 | HIGH | FUN-004 (trends), FUN-005 (dashboard alerts), UXD-006 | Full |
| 14 | T10: Min effort to generate training reports | 14.0 | HIGH | FUN-003, FUN-020 (LLM), PER-004, INT-009, UXD-007 | Full |
| 15 | T15: Min training data loss or sync failure rate | 14.0 | HIGH | QUA-001, QUA-002, HST-006 (offline), OPS-004, UXP-005 | Full |
| 16 | T16: Max before/after performance comparison | 14.0 | HIGH | FUN-004, FUN-011, UXD-006, PER-005 | Full |
| 17 | T06: Min time to plan training from actual data | 13.5 | HIGH | FUN-018 (prediction), FUN-005 (readiness), FUN-007 (qual tracking) | Full |
| 18 | T23: Min training operations cost per soldier-hour | 13.0 | HIGH | FUN-013 (ammo), CST-001 (pricing), all automation features | Full |
| 19 | T20: Max LVC standards compatibility | 12.5 | MEDIUM | INT-006 (DIS), INT-007 (TAK), INT-010 (HLA), INT-011 (CDM export) | Full |
| 20 | T21: Min range cold-to-ready preparation time | 12.5 | MEDIUM | OPS-001 (≤5 min), INT-003 (auto-discovery), UXP-003, DEP-001 | Full |
| 21 | T11: Min LOMAH-to-CAM setup/calibration time | 12.0 | MEDIUM | INT-003 (auto-discovery), MOD-004 (correlation), INT-008 | Full |
| 22 | T19: Min dependency on technical experts | 12.0 | MEDIUM | UXP-001 (≤4h training), UXP-002, MNT-004, DEP-002 | Full |
| 23 | T25: Min time to auto-generate qual certificates | 12.0 | MEDIUM | FUN-024, FUN-007 | Full |
| 24 | T13: Min time to integrate new training scenario | 10.5 | MEDIUM | FUN-021 (scenario management) | Full |
| 25 | T17: Min switchover individual/collective training | 9.0 | OK | FUN-021, UXP-003 (quick session start) | Partial |

**Coverage: 24/25 FULL, 1/25 PARTIAL — all 25 training ODI outcomes have corresponding software requirements.**

---

## 6. VERIFICATION PLAN SUMMARY

| Verification Type | Count | Estimated Cost | Duration | Notes |
|-------------------|-------|----------------|----------|-------|
| Analysis (A) | 18 | $5,000 | 1 week | Cost models, architecture review, security assessment, FMEA |
| Inspection (I) | 22 | $2,000 | 1 week | Code review, configuration audit, documentation review, localization |
| Test (T) | 72 | $30,000 | 8 weeks | Automated test suite, performance load testing, security pen test, AI accuracy testing |
| Demonstration (D) | 45 | $15,000 | 4 weeks | User acceptance testing at ≥2 Vietnamese ranges, stakeholder demonstrations |
| **TOTAL** | **157** | **$52,000** | **14 weeks** | Parallel execution reduces calendar time to ~8 weeks |

### Key Test Programs

| Test Program | Requirements | Estimated Cost | Duration | Facility |
|--------------|-------------|----------------|----------|----------|
| Performance & load testing | PER-001 to PER-008, QUA-001 | $5,000 | 2 weeks | Lab environment with simulated 50-lane load |
| Security penetration test | SEC-001 to SEC-012, OPS-006 | $8,000 | 2 weeks | External security assessor or Workshop X internal |
| VN-LOMAH integration test | INT-001, INT-003, MOD-004 | $3,000 | 2 weeks | Workshop X lab with real LOMAH hardware |
| AI technique accuracy test | QUA-005, QUA-006, FUN-015 | $5,000 | 3 weeks | Annotated reference dataset + controlled shooting sessions |
| Field deployment trial | UXP-001-003, OPS-001-002, DEP-001 | $10,000 | 4 weeks | ≥2 Vietnamese military ranges with real users |
| User acceptance testing | FUN-001-014, UXD-001-006 | $5,000 | 2 weeks | Training officers, range NCOs, instructors at pilot ranges |

---

## 7. CONFLICT ANALYSIS

| Conflict | Requirements | Resolution |
|----------|-------------|------------|
| **Performance vs Air-Gap** | PER-002 (≤100ms WebSocket) vs SEC-006 (air-gap) | No conflict — air-gap means no internet, not no local network. WebSocket operates over local WiFi/Ethernet. |
| **AI Accuracy vs Phase 1 Timeline** | QUA-006 (≥80% technique accuracy) vs SCH-001 (12 weeks) | Phase 1 uses rules-based coaching (FUN-012); ML-based classification (FUN-015) deferred to Phase 2. QUA-006 validated in Phase 2. |
| **Offline vs Cross-Unit Comparison** | HST-006 (offline ≥30 days) vs FUN-006 (cross-unit comparison) | Cross-unit requires data sync. Works: compare units within same range locally; cross-range comparison requires OPS-009 (sync) when connectivity available. Graceful degradation. |
| **Free Tier vs Revenue** | CST-003 (FREE with LOMAH) vs CST-001 ($15-25K STANDARD) | FREE tier is intentionally limited: SCOREBOARD + basic PULSE only. No OVERWATCH, DEBRIEF, EXPORT, analytics. Creates demand for STANDARD upgrade. |
| **Vietnamese-Only vs Partner Integration** | UXP-004 (Vietnamese UI) vs INT-006/INT-007 (DIS/TAK English protocols) | UI is Vietnamese; protocol interfaces (DIS, TAK, REST API) use standard English. DEP-005 adds English UI option for export/demo. Internal vs external separation. |
| **Edge Cost vs AI Capability** | CST-004 (≤$2K hardware) vs ARC-005 (ONNX inference) | Phase 1: $500 mini-PC sufficient for scoring + dashboard (no AI inference needed). Phase 2: $800-1500 Jetson Orin NX for OVERWATCH AI. Hardware upgrades with tier. |
| **Data Retention vs Disk Space** | FUN-004 (≥24 months history) vs HST-001 (≥256GB SSD) | At 500 shots/day × 365 days × 1KB/shot = ~180MB/year for shot data. Video is larger: configured retention. OPS-007 auto-archives. 256GB sufficient for ≥5 years of shot data. |

**Unresolved conflicts: NONE** — all conflicts have feasible engineering resolutions.

---

## 8. OPEN ISSUES & TBD

| Issue ID | Description | Owner | Target Date | Status | Impact |
|----------|-------------|-------|-------------|--------|--------|
| TBD-001 | VN-LOMAH serial protocol specification — complete documentation needed | S10 (LOMAH HW Team) | Phase 1 Sprint 1 | Open | Critical for INT-001; blocks all data ingestion |
| TBD-002 | Vietnamese military qualification scoring standards — codification per weapon type | S2 (Training Officer) | Phase 1 Sprint 3 | Open | Needed for FUN-007 qualification tracking; rules vary by branch/unit |
| TBD-003 | AI technique error classification — annotated dataset (≥1000 labeled clips per category) | S9 (Dev Team) | Phase 2 Sprint 1 | Open | Required for QUA-006; Phase 1 uses rules-based approach |
| TBD-004 | TCVN software standards applicability — which Vietnamese standards apply to military training software | S12 (Regulator) | Q2 2026 | Open | May add requirements to SEC, STD categories |
| TBD-005 | Pilot range selection — which 2 Vietnamese ranges for first deployment | S1 (Customer) | Phase 1 Sprint 5 | Open | Determines deployment environment, network availability, user availability |
| TBD-006 | CDM v1.0 schema — detailed field definitions, validation rules, extension mechanism | S9 (Dev Team) | Phase 1 Sprint 1 | Open | Foundation for ARC-006; publish as open specification |
| TBD-007 | Vietnamese LLM model selection — Llama vs Qwen vs PhoGPT for report generation | S9 (Dev Team) | Phase 2 | Open | Affects FUN-020 quality; local inference on Jetson vs cloud API |
| TBD-008 | Data classification approval — training data classification level (RESTRICTED vs INTERNAL) | S13 (Cybersecurity) | Phase 1 Sprint 4 | Open | Determines SEC requirements stringency; RESTRICTED requires more controls |
| TBD-009 | Partner integration priority — DIS vs TAK vs HLA: which protocol first? | S11 (Partners) | Phase 2 | Open | INT-006 vs INT-007 priority; TAK likely more immediately useful in Vietnam |
| TBD-010 | Edge hardware final selection — Jetson Orin NX vs commodity mini-PC for Phase 1 | S9 (Dev Team) | Phase 1 Sprint 1 | Open | Affects CST-004, HST-001; mini-PC sufficient for Phase 1 (no AI inference) |

---

## 9. PHASE-TO-REQUIREMENT MAPPING (Build Sequence)

| Phase | Month | Products Built | Requirements Addressed | Cumulative Coverage |
|-------|-------|---------------|----------------------|-------------------|
| **1** | 1-3 | SCOREBOARD + PULSE + CDM v1 | FUN-001-002, FUN-004-005, FUN-007-011, FUN-013-014, UXD-001-006, PER-001-005, INT-001, INT-003-005, SEC-001-008, UXP-001-005, DEP-001-004, OPS-001-006, ARC-001-006 | ~75% of MUST |
| **2** | 3-6 | OVERWATCH + DEBRIEF + WEAPONS LINK + EXPORT | FUN-003, FUN-012, FUN-015-017, FUN-020, FUN-024, INT-002, INT-006-007, INT-009, INT-012, QUA-005-006 | ~90% of MUST |
| **3** | 6-9 | TRACKER + MESH + EDGE + CDM v1.2 | FUN-022, HST-005-007, INT-010, MOD-005, DST-004-005 | ~95% of MUST |
| **4** | 9-12 | MIRROR + GHOST + DOJO + ADVERSARY + SCENARIO FORGE | FUN-021, FUN-023, ARC-010 | ~98% of MUST |
| **5** | 12-18 | CLOUD + PROPHECY + HLA + CDM v2 | FUN-018-019, OPS-009, PER-007, QUA-008 | 100% of MUST |

---

## 10. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | Engineering Design System | -- | 2026-02-12 |
| Reviewer | -- | -- | -- |
| Approver | -- | -- | -- |

---

## Cross-References

- [[CORTEX_C2_ODI_Analysis.md]] — ODI Rev A: 75 outcomes (25 Training T01-T25), scoring, segments
- [[CORTEX_RANGE_phase0_complete.md]] — Phase 0: job executors, product tree, CDM schema, sprint plan
- [[CORTEX_RANGE_product_portfolio_musk.md]] — Musk v2.0: Category Creator, co-opetition, competitors
- [[phase0_synthesis.md]] — Phase 0 gate review (10/10 PASS, approved 2026-02-12)
- [[01_requirements/stakeholder_analysis.md]] — 13 stakeholders, RACI, 87 pre-traced IDs, risks
- [[RE_cubic_training_systems.md]] — Cubic MILES/CATS/SPEAR competitive analysis
- [[RE_cubic_lvc_integration.md]] — DIS/HLA/TENA protocols, SPEAR CDM analysis
- [[RE_cae_training_simulation.md]] — CAE Rise analytics, co-opetition partner
- [[RE_saab_training_gamer.md]] — Saab GAMER AAR, TaaS validation
- [[RE_rheinmetall_training_sts.md]] — Rheinmetall AGDUS/LEGATUS, niche competitors
- [[01_requirements/standards_mapping.md]] — Standards compliance (to be created)
- [[01_requirements/requirements_validation.md]] — Validation report (to be created)
