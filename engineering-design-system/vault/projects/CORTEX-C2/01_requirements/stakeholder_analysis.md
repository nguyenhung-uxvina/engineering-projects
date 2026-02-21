---
project: CORTEX-C2
phase: 1
type: stakeholder_analysis
version: 1.0
created: 2026-02-12
status: draft
edition: RANGE STANDARD
scope: First CORTEX C2 edition — AI-driven live-fire training analytics platform
---

# Stakeholder Analysis: CORTEX RANGE STANDARD "TRƯỜNG BẮN"
## AI-Driven Live-Fire Training Analytics Platform

---

## 1. Stakeholder Map Overview

```
                        HIGH INFLUENCE
                             |
        +--------------------+--------------------+
        |                    |                    |
        |   S12: Regulator   |   S1: Customer     |
        |   (TCVN/MoD IT)    |   (Training Cmd)   |
        |                    |                    |
        |   S13: Cybersec    |   S4: Unit Cmdr    |
        |   (MoD InfoSec)    |   (Budget holder)  |
        |                    |                    |
        |                    |   S8: Higher Cmd   |
        |                    |   (Cục Huấn Luyện) |
 LOW ---+--------------------+--------------------+--- HIGH
INTEREST|                    |                    | INTEREST
        |   S11: Partners    |   S2: Trng Officer |
        |   (CAE, Saab,      |   (PRIMARY user)   |
        |    Cubic ecosystem)|                    |
        |                    |   S3: Range NCO    |
        |                    |   (Daily operator) |
        |                    |                    |
        |                    |   S5: Soldier      |
        |                    |   S6: Instructor   |
        |                    |   S7: IT/SysAdmin  |
        |                    |   S9: Dev Team     |
        |                    |   S10: LOMAH HW    |
        +--------------------+--------------------+
                             |
                        LOW INFLUENCE
```

**Quadrant Summary:**

| Quadrant | Strategy | Stakeholders |
|----------|----------|-------------|
| **Key Players** (High influence + High interest) | Engage closely, co-develop requirements | S1, S4, S8 |
| **Keep Satisfied** (High influence + Low interest) | Formal compliance, security audits, demos | S12, S13 |
| **Keep Informed** (Low influence + High interest) | Design reviews, training, sprint demos, field feedback | S2, S3, S5, S6, S7, S9, S10 |
| **Monitor** (Low influence + Low interest) | Interoperability specs, API documentation | S11 |

---

## 2. Detailed Stakeholder Profiles

### S1: Customer (Training Command / Procurement Authority)

| Field | Detail |
|-------|--------|
| **Who** | VPA Training Directorate (Cục Huấn Luyện), Military Region training departments, Military Academy training centers, individual unit commanders with training budget authority |
| **Role** | Budget holder, procurement decision maker, defines acquisition specifications and acceptance criteria for training systems |
| **Interest** | HIGH — Currently spending 60%+ of training admin time on manual processes; no digital training analytics capability exists in Vietnamese military inventory |
| **Influence** | HIGH — Approves procurement budget ($15-50K per range); sets evaluation criteria; authorizes pilot deployments; controls multi-year training modernization plans |
| **Primary Needs** | Cost-effective vs import alternatives ($15-25K vs $5-50M Cubic); local software development and support; proven training outcome improvement; data ownership (not cloud-dependent on foreign vendor); Vietnamese language throughout; integration with existing VN-LOMAH hardware |
| **Success Criteria** | Perpetual license ≤$25K per range; subscription ≤$5K/year; demonstrated ≥200% improvement in training data consolidation time (T01, score 17.5); Vietnamese-language UI and reports; data sovereignty (on-premise option); deployment ≤1 day per range |
| **Pain Points** | No domestic training analytics platform exists; import C2 systems cost $5-50M+ (Cubic CTC); foreign system dependency creates support risk; current training assessment is manual (paper scorecards, verbal reports); no cross-unit training comparison capability; slow procurement cycle for imported defense software |
| **Communication** | Formal procurement specifications, range demonstration events, pilot deployment results, quarterly program reviews, cost-benefit analyses |
| **Risk if Ignored** | Project unfunded; requirements misaligned with procurement criteria; budget diverted to imported training management systems; VN-LOMAH hardware sales lose software value multiplier |
| **Key Requirements Driven** | CST-001 (perpetual ≤$25K), CST-002 (subscription ≤$5K/yr), PRD-001 (Vietnamese language), PRD-002 (on-premise deployment option), STD-001 (TCVN compliance), SCH-001 (delivery schedule) |

**ODI Connection:** Customer represents procurement gateway for Segment C (Training Analytics Champions, 25% market value). T01 (17.5) and T18 (17.0) are the two highest-scoring training outcomes — both directly address the customer's core pain: fragmented, manual training data across multiple systems.

---

### S2: Primary User (Training Officer / Sĩ Quan Huấn Luyện)

| Field | Detail |
|-------|--------|
| **Who** | Training officers at company-to-regiment level — Sĩ quan huấn luyện — Captain to Lieutenant Colonel (Đại úy → Trung tá) |
| **Role** | **PRIMARY ODI job executor**: Plans, executes, and evaluates unit training programs. Spends 60%+ of time on admin, not coaching. This is the person CORTEX RANGE must liberate. |
| **Interest** | HIGH — Direct impact on their effectiveness and career; currently drowning in manual scorecards and Excel spreadsheets |
| **Influence** | MEDIUM — Field feedback determines product acceptance; recommends system to unit commander (S4); generates training reports that demonstrate (or fail to demonstrate) value |
| **Technical Level** | Medium — Military academy graduate; comfortable with tablets and basic software; NOT IT professionals; expect systems to work like consumer apps |
| **Primary Needs** | Consolidate multi-system results instantly (T01, Score 17.5); eliminate subjective scoring bias (T02, 16.0); instant feedback after shooting (T04, 16.0); transparent evaluation results (T24, 16.0); manage multiple weapon types on one platform (T18, 17.0); auto-generate reports for command (T10, 14.0) |
| **Success Criteria** | Training data consolidated from VN-LOMAH + VN-CAM + weapon systems in <30 seconds (vs current 30-60 min); zero manual data entry for shot scoring; training reports auto-generated in Vietnamese; accessible on tablet at firing line; individual soldier performance trends visible across sessions |
| **Pain Points** | Paper scorecards lose data and are error-prone; walking downrange to check targets wastes 30-60 min per session; Excel spreadsheets are fragmented per weapon type; no way to compare soldiers across sessions or units; debrief is delayed hours/days; report writing takes 1-3 days; no predictive capability ("who will fail next qualification?") |
| **Communication** | Field demonstrations at real ranges, hands-on training sessions, Vietnamese-language user manual, video tutorials, feedback forms during pilot deployment |
| **Risk if Ignored** | System perceived as "more admin work" instead of less; training officers bypass system and continue manual methods; low adoption kills word-of-mouth growth needed for flywheel |
| **Key Requirements Driven** | FUN-001 (real-time shot scoring display), FUN-002 (multi-system data consolidation <30s), FUN-003 (auto-report generation Vietnamese), FUN-004 (soldier performance trends), UXD-001 (tablet-optimized interface), UXD-002 (field-usable in sunlight/rain), DAT-001 (CORTEX CDM unified data model) |

**Persona (from [[CORTEX_RANGE_phase0_complete.md]]):**
> Đại úy Minh, 32, is a training officer at a regiment near Hanoi. He manages weekly range sessions for 200+ soldiers across rifle, pistol, and RCWS qualifications. His current workflow: paper scorecards → manual counting → Excel entry → Word report → email to commander. A single range day generates 3-5 hours of post-session admin. He wants to coach soldiers, not count holes in paper. He has a Samsung tablet and good cellular coverage at his range.

**ODI Segments Represented:**
- Segment C: Training Analytics Champions (25%) — PRIMARY target
- Addresses 5 EXTREME outcomes in Build Phase 1 (T01, T02, T04, T24, T05)

---

### S3: Range NCO (Quản Lý Trường Bắn)

| Field | Detail |
|-------|--------|
| **Who** | Senior NCOs assigned to operate and manage shooting ranges — Quản lý trường bắn — Sergeant to Master Sergeant |
| **Role** | **Daily operator**: physically operates the range, manages VN-LOMAH sensors, ensures safety, controls firing sequences. The person who touches the system every day. |
| **Interest** | HIGH — System directly affects daily workload; poor usability = system abandoned; good usability = "I can't go back to paper" |
| **Influence** | MEDIUM — Informal but powerful; range NCO opinion determines whether system gets used or becomes shelf-ware; provides ground-truth feedback to training officers (S2) |
| **Technical Level** | Medium-Low — Experienced with range operations but NOT tech-savvy; expects "push button, it works" simplicity; may be resistant to change if system adds complexity |
| **Primary Needs** | Minimize range cold-to-ready preparation time (T21, 12.5); minimize setup/calibration time for LOMAH-to-CAM connection (T11, 12.0); minimize dependency on technical experts for daily ops (T19, 12.0); auto-detect connected sensors and systems (CR-N1 MESH); simple session start/stop workflow |
| **Success Criteria** | System startup from power-on to operational ≤5 minutes; LOMAH/camera auto-discovered on network (no manual IP configuration); session start = 1 button press; live scores visible within 50ms of shot; system recovers automatically from sensor disconnection; range NCO training ≤4 hours |
| **Pain Points** | Current VN-LOMAH operates standalone — data trapped in each sensor; connecting cameras requires manual configuration; no single view of all lanes simultaneously; weather conditions (rain, wind) affect paper targets but not system visibility; fear of "computer systems" complicating simple range operations |
| **Communication** | Hands-on training at the range, Vietnamese-language pictorial quick-start guide (laminated), "day in the life" workflow testing during development, monthly feedback sessions during pilot |
| **Risk if Ignored** | Range NCO refuses to use system ("too complicated"); trains soldiers to bypass system; negative word-of-mouth to other ranges; system powered off and paper targets resume |
| **Key Requirements Driven** | UXD-003 (startup ≤5 min from power-on), UXD-004 (session start = 1 action), UXD-005 (auto-discovery of sensors), UXD-006 (auto-reconnect on sensor loss), UXD-007 (range NCO training ≤4h), NET-001 (plug-and-play sensor network) |

---

### S4: Unit Commander (Chỉ Huy Đơn Vị)

| Field | Detail |
|-------|--------|
| **Who** | Company, battalion, and regiment commanders — Đại đội trưởng, Tiểu đoàn trưởng, Trung đoàn trưởng — Major to Colonel |
| **Role** | **Budget holder and readiness authority**: approves training resource allocation, reads training reports, makes decisions about who needs more training and where to invest. Consumes CORTEX RANGE data to make command decisions. |
| **Interest** | HIGH — Training readiness directly reflects on command competence; currently relies on subjective reports; wants data-driven training decisions |
| **Influence** | HIGH — Controls unit training budget ($5-50K); decides to purchase/renew CORTEX RANGE subscription; recommends system to higher command (S8); can mandate system use across subordinate units |
| **Technical Level** | Low-Medium — Uses systems through dashboards and reports, NOT through detailed configuration; expects executive-level summaries; reads on laptop/tablet in office |
| **Primary Needs** | Cross-unit comparison on same scale (T03, 16.5); cross-unit training data analysis (T22, 16.0); before/after performance comparison (T16, 14.0); detect declining soldier performance early (T08, 14.0); auto-generated reports eliminate 1-3 day report writing delay (T10, 14.0) |
| **Success Criteria** | Commander dashboard shows unit readiness at a glance; compare any 2 units on same metrics; identify bottom 10% soldiers for remedial training; training reports auto-generated and ready for higher command; trend lines show training investment ROI; zero manual data compilation |
| **Pain Points** | Cannot compare units because each range uses different scoring methods; training reports arrive 1-3 days after range day (too late to act); no historical trend analysis — "are we getting better or worse?"; relies on training officer's subjective assessment; no way to predict who will fail next qualification |
| **Communication** | Monthly command-level dashboard demonstrations, executive summary reports, quarterly readiness briefings, pilot deployment result presentations |
| **Risk if Ignored** | Commander doesn't see value → doesn't renew subscription → kills revenue model; commander doesn't mandate use → adoption remains optional → flywheel doesn't spin; commander shares data with higher command → if data is wrong, trust is destroyed permanently |
| **Key Requirements Driven** | FUN-005 (commander dashboard — unit readiness overview), FUN-006 (cross-unit comparison), FUN-007 (soldier performance trend alerts), FUN-008 (auto-generated commander brief), FUN-009 (qualification tracking and prediction), DAT-002 (data integrity — audit trail for all scores) |

**ODI Connection:** Commander bridges Segment C (Training Analytics, 25%) and the upsell path to Segment B (Sensor Fusion, 25%). When a commander sees the value of data-driven training, they ask: "Can CORTEX do this for base security too?" → CORTEX BASE upsell.

---

### S5: Individual Soldier (Binh Sĩ)

| Field | Detail |
|-------|--------|
| **Who** | Soldiers of all ranks who train at the range — Binh sĩ — from private to senior NCO |
| **Role** | **End user**: fires weapons, receives scores and AI coaching feedback, views personal performance history. The person whose improvement CORTEX RANGE must measurably accelerate. |
| **Interest** | MEDIUM-HIGH — Wants to improve shooting skill; wants fair, transparent scoring; competitive motivation (see how they compare to peers) |
| **Influence** | LOW — Does not make procurement decisions; but mass adoption and positive experience creates grassroots demand |
| **Technical Level** | Low — 18-25 years old typically; smartphone-native but NOT tech professionals; expects app-like interface on shared tablet or personal phone |
| **Primary Needs** | Instant feedback after shooting (T04, 16.0); transparent evaluation results (T24, 16.0); individual training history traceability (T09, 15.5); auto-captured performance metrics per shot (T05, 15.0) |
| **Success Criteria** | See shot placement on screen within 1 second of firing; know pass/fail status in real-time (not after session); view personal history across multiple range sessions; receive specific AI coaching suggestions (e.g., "trigger jerk detected — practice smooth press"); compare to unit average (anonymized) |
| **Pain Points** | Never sees own shot placement in real-time; paper scoring is delayed and perceived as unfair; no feedback on technique errors (only "hit or miss"); no memory of past sessions — every range day starts from zero; no way to self-practice with data-driven goals |
| **Communication** | Kiosk/tablet display at firing line, personal QR-code performance card, Vietnamese-language coach tips, gamification elements (rank, badges, improvement streaks) |
| **Risk if Ignored** | Soldiers see system as "surveillance" rather than coaching tool; no individual buy-in → system used only for officer reporting, not skill improvement; miss the motivational/competitive element that drives adoption |
| **Key Requirements Driven** | FUN-010 (per-shot real-time display at firing position), FUN-011 (personal performance history), FUN-012 (AI coaching suggestions in Vietnamese), FUN-013 (improvement trend visualization), UXD-008 (kiosk mode — simplified soldier view) |

---

### S6: Instructor/Coach (Huấn Luyện Viên)

| Field | Detail |
|-------|--------|
| **Who** | Marksmanship instructors and coaching specialists — Huấn luyện viên bắn súng — typically experienced NCOs or officers with shooting expertise |
| **Role** | **AI-augmented coach**: Uses CORTEX RANGE OVERWATCH (Phase 2) to identify technique errors in real-time; receives AI annotations on video; coaches specific corrections. The person AI serves, not replaces. |
| **Interest** | HIGH — AI coaching multiplies their effectiveness; currently limited to observing 2-4 shooters simultaneously; OVERWATCH enables coaching 50 lanes from one display |
| **Influence** | LOW-MEDIUM — Respected subject-matter expert; instructor endorsement ("this AI actually helps me coach better") is the strongest social proof for adoption |
| **Technical Level** | Medium — Deep domain expertise in shooting technique; willing to learn new tools if they visibly improve coaching outcomes; NOT interested in technology for its own sake |
| **Primary Needs** | AI accuracy in classifying shooting technique errors (T12, 15.5); multi-angle video replay and analysis (T14, 14.5); minimize subjective bias in evaluation (T02, 16.0); first-time qualification rate improvement via trend analysis (T07, 14.0) |
| **Success Criteria** | AI correctly identifies ≥10/12 technique error categories; video replay available within 30 seconds of firing sequence; AI annotations highlight specific body mechanics (flinch, grip, breathing); instructor can override AI classification; coaching recommendations are actionable (not just "error detected") |
| **Pain Points** | Can only physically observe 2-4 shooters at a time (regiment has 50+ lanes); technique errors happen in milliseconds — impossible to catch with naked eye consistently; no video replay capability today; coaching is based on experience/intuition, not data; junior instructors lack the pattern recognition of senior coaches |
| **Communication** | Instructor-specific dashboard view, AI annotation overlay training, technique error library (12 categories with video examples), instructor feedback mechanism to improve AI models |
| **Risk if Ignored** | Instructors feel threatened by AI ("replacing us"); AI coaching suggestions conflict with instructor's teaching → instructor discredits system; AI technique analysis too generic → instructors dismiss it as useless |
| **Key Requirements Driven** | FUN-014 (AI technique error classification — 12 categories), FUN-015 (multi-angle video replay <30s), FUN-016 (instructor override of AI classification), FUN-017 (actionable coaching recommendations), FUN-018 (instructor dashboard — 50-lane overview with AI alerts) |

---

### S7: Technical Operator / IT Admin (Kỹ Thuật Viên / Quản Trị Hệ Thống)

| Field | Detail |
|-------|--------|
| **Who** | Signal/IT NCOs and technicians assigned to maintain CORTEX RANGE — Kỹ thuật viên thông tin — at battalion/regiment level |
| **Role** | **System administrator**: installs CORTEX RANGE, maintains edge server, manages user accounts, troubleshoots network/sensor issues, performs software updates, monitors system health |
| **Interest** | HIGH — System availability directly affects their workload and unit readiness reporting; responsible when system fails |
| **Influence** | LOW-MEDIUM — Technical gatekeeper; can delay deployment through "not ready yet" assessments; maintenance feedback influences design updates |
| **Technical Level** | Medium-High — Signal/comms training; familiar with networking, basic server administration; may have Linux experience; can follow technical documentation but NOT software developers |
| **Primary Needs** | Minimize dependency on technical experts for daily ops (T19, 12.0); minimize range cold-to-ready time (T21, 12.5); minimize data loss or sync failure rate (T15, 14.0); self-diagnostics for troubleshooting; remote monitoring capability |
| **Success Criteria** | Installation ≤2 hours from unbox to operational (1-page setup guide); automated system health monitoring with alerts; self-diagnostics identify ≥90% of issues to component level; software updates via single command (no multi-step manual process); system runs ≥8 hours without intervention; user management via simple web interface (add/remove soldiers/officers) |
| **Pain Points** | Imported defense systems require foreign technicians for any issue; current VN-LOMAH has no centralized management — each unit configured individually; network configuration is manual and error-prone; no remote monitoring — must physically visit range to check system; software updates are manual USB copy process |
| **Communication** | Vietnamese-language admin manual, system health dashboard, troubleshooting decision tree (laminated), 8-hour admin training course, remote support channel |
| **Risk if Ignored** | System downtime increases; IT admin blames system for any range issue; updates not applied → security vulnerabilities; system configuration drift across ranges → inconsistent behavior |
| **Key Requirements Driven** | OPS-001 (installation ≤2h), OPS-002 (system health monitoring + alerts), OPS-003 (self-diagnostics ≥90% fault isolation), OPS-004 (single-command software update), OPS-005 (RBAC user management), OPS-006 (≥8h unattended operation), OPS-007 (remote monitoring API), NET-002 (auto-configuration of network components) |

---

### S8: Higher Command (Cục Huấn Luyện / Chỉ Huy Cấp Trên)

| Field | Detail |
|-------|--------|
| **Who** | VPA Training Directorate (Cục Huấn Luyện), Military Region deputy commanders for training, Military Academy leadership — General/Senior Colonel level |
| **Role** | **Enterprise consumer**: views cross-unit, cross-region training analytics; allocates national training resources; sets training standards; evaluates training system investments |
| **Interest** | HIGH — National readiness visibility is a strategic imperative; no current capability to compare training outcomes across units or regions on same scale |
| **Influence** | HIGH — Approves enterprise-level procurement ($50K+ ENTERPRISE edition); mandates system use across entire military region; sets training standards that CORTEX RANGE must implement |
| **Technical Level** | Low — Exclusively dashboard and report consumers; staff officers prepare briefings from CORTEX data; needs 1-page summaries, not raw data |
| **Primary Needs** | Cross-unit training data analysis (T22, 16.0); cross-unit comparison on same scale (T03, 16.5); maximize first-time qualification rate via trend analysis (T07, 14.0); national readiness dashboard |
| **Success Criteria** | National readiness map showing all ranges on single dashboard; drill down from region → division → regiment → company → individual; trend lines: "Is the army getting better at shooting?"; automatic identification of lowest-performing units for intervention; one-click export of quarterly training summary for Ministry |
| **Pain Points** | Currently aggregates training data manually from paper reports — weeks of delay; no common standard — each unit reports differently; impossible to compare training investment effectiveness across regions; training readiness is the #1 question asked by Minister of Defense — answer is always subjective |
| **Communication** | Quarterly command briefings, national readiness dashboard (web portal), annual training effectiveness report, enterprise procurement business case |
| **Risk if Ignored** | CORTEX RANGE remains unit-level tool (no enterprise scale); miss the highest-value revenue tier ($50K+ ENTERPRISE); no mandate for adoption → growth limited to voluntary adopters; data aggregation challenges create inconsistency |
| **Key Requirements Driven** | FUN-019 (national readiness dashboard), FUN-020 (region → unit drill-down), FUN-021 (cross-unit benchmarking on standardized metrics), FUN-022 (quarterly automated readiness report), DAT-003 (data federation — multi-range sync), SEC-001 (classification-appropriate data handling) |

---

### S9: Workshop X Development Team

| Field | Detail |
|-------|--------|
| **Who** | Core engineering team: Full-stack developers (Python/React), AI/ML engineers, UX designers, QA engineers, DevOps |
| **Role** | Designs, develops, tests, and iterates CORTEX RANGE through all phases; bridges concept to production; establishes engineering standards and CI/CD infrastructure |
| **Interest** | HIGH — Core project team; career development on cutting-edge defense AI product; defines technical feasibility boundaries |
| **Influence** | MEDIUM — Technical decisions within design space; identifies what is feasible vs aspirational; flags risk to schedule and cost; recommends technology stack |
| **Primary Needs** | Clear quantified requirements with testable acceptance criteria; access to VN-LOMAH hardware for integration testing; military range access for field validation; development infrastructure (GPU for AI training, staging servers, CI/CD pipeline); VN-LOMAH protocol documentation; Vietnamese shooting technique dataset for OVERWATCH AI training |
| **Success Criteria** | Phase 1 MVP (SCOREBOARD + PULSE + CDM) deployed at 1-2 real ranges within 12 weeks; system handles 50 lanes × 10 shots/min (500 events/min) without degradation; WebSocket dashboard updates in <100ms; AI technique analysis ≥80% accuracy on top-5 error types; zero critical security vulnerabilities in penetration test |
| **Pain Points** | No prior defense training analytics product experience (new domain); limited military range access for field testing; no existing Vietnamese shooting technique dataset for ML training; VN-LOMAH serial/UDP protocol may have undocumented edge cases; 2-developer team in Phase 1 limits parallelism; AI model quality limited by training data quantity |
| **Communication** | Technical design reviews, bi-weekly sprint demos, internal wiki documentation, daily stand-ups, design review gates |
| **Risk if Ignored** | Requirements misinterpretation and rework; overly ambitious Phase 1 scope causing schedule slip; insufficient field testing yielding unvalidated performance claims; technical debt accumulation from rushing |
| **Key Requirements Driven** | ARC-001 (Python FastAPI backend), ARC-002 (React + TypeScript frontend), ARC-003 (TimescaleDB for time-series), ARC-004 (ONNX Runtime for AI inference), ARC-005 (WebSocket real-time <100ms), ARC-006 (CDM v1.0 JSON schema), ARC-007 (CI/CD pipeline), ARC-008 (API-first architecture) |

**Capability Gaps Identified:**

| Gap | Severity | Mitigation |
|-----|----------|-----------|
| VN-LOMAH integration experience | Medium | LOMAH protocol documented; Workshop X hardware team (S10) available; serial/UDP is standard |
| AI shooting technique classification | High | Start rules-based; build annotated dataset from pilot ranges; add CNN when 10K+ shots labeled |
| Military software security practices | Medium | Adopt OWASP Top 10; air-gap architecture option; penetration test before deployment |
| Real-time dashboard at scale (500 events/min) | Medium | TimescaleDB + WebSocket proven at this scale; load test in Phase 1 Sprint 5 |
| Vietnamese military training standards codification | High | Work with S2 (Training Officers) to codify qualification scoring rules per weapon type |

---

### S10: VN-LOMAH Hardware Team (Workshop X — Hardware Division)

| Field | Detail |
|-------|--------|
| **Who** | Workshop X hardware engineers who design and manufacture the VN-LOMAH acoustic scoring system, VN-CAM camera systems, and VN-TRN electronics |
| **Role** | Provides the sensor hardware that feeds CORTEX RANGE; defines hardware API/protocol; controls sensor firmware updates; manufactures hardware at scale |
| **Interest** | HIGH — CORTEX RANGE is the software that makes their hardware 10x more valuable; "VN-LOMAH + CORTEX RANGE" sells for $30-40K vs VN-LOMAH alone at $15K |
| **Influence** | MEDIUM — Controls hardware interface (serial/UDP protocol); sensor firmware changes can break CORTEX integration; production quality affects CORTEX reliability |
| **Primary Needs** | Stable, documented API contract between hardware and software; synchronized release schedule; clear hardware-software interface specification; CORTEX should NOT require hardware firmware changes; hardware sales credit for CORTEX-bundled deals |
| **Success Criteria** | Hardware-software integration works without firmware modification; CORTEX auto-detects VN-LOMAH sensor model and firmware version; new hardware sensor types (future VN-CAM models) can be added via plugin architecture; hardware team receives integration test results before every CORTEX release |
| **Pain Points** | Current VN-LOMAH data goes nowhere — wasted intelligence; hardware-only sales have thin margins; no standardized API — each LOMAH installation configured differently; firmware update coordination between hardware and software teams is manual |
| **Communication** | Weekly hardware-software sync meetings, API specification document (versioned), integration test suite, joint release planning, shared issue tracker |
| **Risk if Ignored** | Hardware-software integration breaks on firmware updates; VN-LOMAH protocol changes break CORTEX without notice; missed cross-selling opportunities; sensor data format inconsistencies across hardware versions |
| **Key Requirements Driven** | INT-001 (VN-LOMAH serial/UDP parser — all sensor models), INT-002 (VN-CAM-T1 RTSP video feed integration), INT-003 (sensor auto-discovery and model detection), INT-004 (hardware API versioning contract), INT-005 (plugin architecture for future sensor types) |

---

### S11: Partner Systems (CAE, Saab, Cubic Ecosystem)

| Field | Detail |
|-------|--------|
| **Who** | CAE Inc. (virtual/constructive training, Rise analytics), Saab Training (GAMER AAR/EXCON, BT46 laser), Rheinmetall (AGDUS/LEGATUS, GUZ CTC), existing DIS/HLA/TAK ecosystem users |
| **Role** | **Co-opetition ecosystem**: CORTEX RANGE provides the live-fire data layer that no partner currently captures; partners provide virtual/constructive/force-on-force layers that CORTEX doesn't |
| **Interest** | LOW-MEDIUM — Partners have no live-fire analytics; CORTEX data enriches their ecosystem; interoperability expands their market (bundled sales with CORTEX) |
| **Influence** | MEDIUM — Partner integration validates CORTEX; DIS/HLA/TAK compatibility is table stakes for military training systems; partner endorsement opens international markets |
| **Primary Needs** | Standard interoperability protocols (DIS IEEE 1278, CoT/TAK, HLA IEEE 1516); documented API for data exchange; CORTEX CDM export in partner-compatible formats; no vendor lock-in (open data, open standards) |
| **Success Criteria** | CORTEX publishes DIS PDUs that standard DIS receivers can consume; TAK plugin displays CORTEX training data on ATAK map; REST API documented with OpenAPI 3.0 specification; CDM export to CSV/JSON for import into CAE Rise or GAMER; partner integration demonstrated at defense trade show |
| **Pain Points** | No live-fire data source in standard formats today; live-fire scoring (acoustic/LOMAH) has no DIS PDU equivalent — custom extension needed; each partner has proprietary data formats (Cubic SPEAR CDM is closed); integration testing requires access to partner systems (expensive, slow) |
| **Communication** | API documentation (OpenAPI 3.0), protocol specification documents, interoperability demonstration events, annual partner review, joint trade show presence |
| **Risk if Ignored** | CORTEX operates as isolated silo — loses 80% of LVC integration value; DIS/TAK non-compliance blocks military procurement in allied nations; partners build competing live-fire layer (unlikely but possible in 3-5 years) |
| **Key Requirements Driven** | INT-006 (DIS IEEE 1278 PDU output — ShotEvent as custom PDU), INT-007 (CoT/TAK plugin for ATAK), INT-008 (REST API with OpenAPI 3.0), INT-009 (HLA IEEE 1516 federate — Phase 3), INT-010 (CDM export: CSV, JSON, XML), INT-011 (open CDM specification — published, versioned) |

**Co-opetition Strategy (from [[CORTEX_RANGE_product_portfolio_musk.md]] v2.0):**

| Partner | Their Gap | CORTEX Fills | They Fill | Revenue Model |
|---------|-----------|-------------|-----------|---------------|
| CAE | ZERO live-fire products | Live-fire data feed to Rise analytics | Virtual/constructive analytics | Data licensing |
| Saab | ZERO live-fire scoring (BT46 = laser only) | Acoustic scoring + AI analytics | Force-on-force AAR (GAMER) | Integration bundle |
| Rheinmetall | ZERO AI analytics, ZERO LOMAH | AI training analytics for their ranges | CTC-scale exercise management | OEM licensing |

---

### S12: Regulator / Standards Body

| Field | Detail |
|-------|--------|
| **Who** | VPA Quality Assurance directorate; Military IT/Communications Department (Cục Công nghệ Thông tin); STAMEQ (Vietnamese standards); Military training standards committees |
| **Role** | Approves software systems for military use; enforces cybersecurity, data protection, and software quality standards; certifies compliance; defines acceptance test protocols |
| **Interest** | MEDIUM — New software category (AI-driven training analytics); no existing TCVN standard applies directly; increasing focus on military cybersecurity post-2024 |
| **Influence** | HIGH — Can block procurement and deployment; certification is mandatory before fielding in military units; sets data classification and handling requirements |
| **Primary Needs** | Compliance with applicable TCVN software standards; cybersecurity assessment (penetration test, vulnerability scan); data classification compliance; software quality assurance evidence; AI model validation methodology (how to certify AI coaching accuracy?) |
| **Success Criteria** | Complete compliance dossier with test results; penetration test by accredited lab with zero critical/high findings; data classification assessment (training data = likely RESTRICTED, not SECRET); OWASP Top 10 compliance evidence; documented AI model validation methodology with statistical performance guarantees |
| **Pain Points** | No existing TCVN standard for AI-driven military training systems; unclear how to certify AI coaching recommendations; data classification for training performance data is ambiguous (is individual soldier data personally identifiable?); limited military cybersecurity assessment capability for modern web applications |
| **Communication** | Formal compliance documentation, security assessment reports, data classification request, certification review meetings, annual security audit |
| **Risk if Ignored** | Deployment blocked at all military units; procurement non-compliant; data breach creates liability; AI coaching recommendations questioned without validation methodology |
| **Key Requirements Driven** | SEC-002 (OWASP Top 10 compliance), SEC-003 (penetration test — zero critical findings), SEC-004 (data classification compliance), SEC-005 (AI model validation methodology), STD-002 (software quality assurance per TCVN), STD-003 (personal data protection compliance) |

---

### S13: Cybersecurity / Data Protection Officer

| Field | Detail |
|-------|--------|
| **Who** | Military cybersecurity officers, unit information security officers — Sĩ quan an toàn thông tin — at division/military region level |
| **Role** | Approves IT system deployment in military networks; defines security requirements; monitors for vulnerabilities; responds to security incidents; controls network access |
| **Interest** | MEDIUM — New web application on military network raises security concerns; AI system processing soldier performance data raises privacy concerns |
| **Influence** | HIGH — Can veto deployment on security grounds; controls network access policies; defines encryption and authentication requirements; incident response authority |
| **Primary Needs** | Air-gapped deployment option (no internet required); role-based access control (RBAC); data encryption at rest and in transit; audit logging for all data access; no telemetry or data exfiltration to external servers; authentication integration with existing military identity systems |
| **Success Criteria** | System operates fully air-gapped (zero internet dependency); AES-256 encryption for data at rest; TLS 1.3 for data in transit; RBAC with minimum 4 roles (admin, officer, NCO, viewer); complete audit log of all access with tamper detection; no third-party cloud dependencies in on-premise mode; password policy compliance |
| **Pain Points** | Web applications are perceived as security risks; cloud-connected systems are automatically suspect; AI/ML systems are "black boxes" — what data goes where?; soldier performance data is sensitive (can be used for career discrimination); previous military software deployments have had security incidents |
| **Communication** | Security architecture review, threat model document, penetration test report, data flow diagram (showing all data paths), deployment security checklist, annual security audit |
| **Risk if Ignored** | System banned from military networks; deployment delayed 6-12 months for security review; data breach destroys trust permanently; CORTEX labeled as "security risk" — reputation damage across all military customers |
| **Key Requirements Driven** | SEC-001 (data classification handling — RESTRICTED level), SEC-006 (air-gap deployment mode), SEC-007 (AES-256 at rest + TLS 1.3 in transit), SEC-008 (RBAC — 4 roles minimum), SEC-009 (tamper-evident audit logging), SEC-010 (zero external telemetry in on-premise mode), SEC-011 (data retention and deletion policy) |

---

## 3. RACI Matrix

### 3.1 RACI by Requirement Category (Adapted 16 Categories for Software)

| Requirement Category | S1 Customer | S2 Training Officer | S3 Range NCO | S4 Unit Cmdr | S5 Soldier | S6 Instructor | S7 IT Admin | S8 Higher Cmd | S9 Dev Team | S10 LOMAH HW | S11 Partners | S12 Regulator | S13 CyberSec |
|---------------------|-------------|-------------------|-------------|-------------|-----------|--------------|------------|-------------|------------|-------------|------------|-------------|-------------|
| UI/UX Layout (Geometry) | I | **C** | **C** | C | C | C | I | I | **R/A** | -- | -- | -- | -- |
| Data Flow (Kinematics) | I | C | -- | I | -- | -- | C | I | **R/A** | C | C | I | C |
| Processing Load (Forces) | -- | -- | -- | -- | -- | -- | C | -- | **R/A** | -- | -- | -- | -- |
| Power/Host Req (Energy) | I | -- | C | -- | -- | -- | **C** | -- | **R/A** | C | -- | -- | -- |
| Tech Stack (Material) | -- | -- | -- | -- | -- | -- | I | -- | **R/A** | -- | -- | -- | I |
| APIs/Protocols (Signals) | I | C | -- | -- | -- | -- | C | I | **R/A** | **C** | **C** | -- | C |
| Cybersecurity (Safety) | C | I | -- | I | -- | -- | C | I | **R** | -- | -- | **A** | **C** |
| User Experience (Ergonomics) | C | **C** | **C** | C | **C** | **C** | C | C | **R/A** | -- | -- | -- | -- |
| Deployment/DevOps (Production) | **A** | -- | -- | -- | -- | -- | C | I | **R** | C | I | I | C |
| Performance/Reliability (Quality) | **A** | C | C | I | I | I | C | I | **R** | C | -- | C | -- |
| Integration/Modularity (Assembly) | I | -- | -- | -- | -- | -- | C | -- | **R/A** | **C** | C | -- | -- |
| Distribution/Install (Transport) | I | -- | -- | I | -- | -- | **C** | -- | **R/A** | C | -- | -- | C |
| Runtime/Admin (Operation) | I | C | **C** | I | I | I | **C** | I | **R/A** | -- | -- | -- | C |
| Updates/Support (Maintenance) | I | I | -- | -- | -- | -- | **C** | -- | **R/A** | C | -- | -- | C |
| Licensing/Infra (Costs) | **A** | -- | -- | C | -- | -- | I | **A** | **R** | I | I | -- | -- |
| Release/Milestones (Schedule) | **A** | I | -- | I | -- | -- | I | I | **R** | C | -- | I | -- |

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

### 3.2 RACI by Key Activity

| Activity | S1 Cust | S2 TrnOff | S3 NCO | S4 Cmdr | S5 Soldier | S6 Instr | S7 IT | S8 HiCmd | S9 Dev | S10 HW | S11 Ptnr | S12 Reg | S13 Cyber |
|----------|---------|-----------|--------|---------|-----------|----------|-------|---------|--------|--------|---------|---------|-----------|
| **Define requirements** | **A** | C | C | C | I | C | C | C | **R** | C | I | C | C |
| **Design system** | I | C | C | I | I | C | C | I | **R/A** | C | I | I | C |
| **Develop software** | I | -- | -- | -- | -- | -- | -- | -- | **R/A** | C | -- | -- | -- |
| **Test at range** | I | **C** | **C** | I | C | C | C | -- | **R/A** | C | -- | -- | -- |
| **Security assessment** | I | -- | -- | -- | -- | -- | C | -- | **R** | -- | -- | **A** | **C** |
| **Deploy to range** | I | I | C | **A** | -- | -- | **R** | I | C | C | -- | I | C |
| **Operate daily** | -- | **R** | **R** | I | I | I | C | -- | I | -- | -- | -- | -- |
| **Maintain/update** | -- | -- | -- | -- | -- | -- | **R** | -- | **C** | C | -- | -- | I |
| **Update AI models** | -- | I | -- | I | -- | C | -- | -- | **R/A** | -- | -- | C | I |
| **Enterprise rollout** | **A** | I | -- | I | -- | -- | C | **A** | **R** | C | -- | C | C |

---

## 4. ODI Segment to Stakeholder Mapping

### 4.1 Segment Mapping Table

| ODI Segment | Market Share | Primary Stakeholders | Influencing Stakeholders | Key Outcomes Driven |
|-------------|-------------|---------------------|-------------------------|-------------------|
| **C: Training Analytics Champions** | 25% | S2 (Training Officer), S3 (Range NCO), S6 (Instructor) | S1 (Customer), S4 (Unit Commander), S8 (Higher Command) | T01 (17.5), T18 (17.0), T03 (16.5), T22 (16.0), T02 (16.0), T04 (16.0), T24 (16.0) |

**Note:** CORTEX RANGE STANDARD addresses Segment C exclusively. Segments A (Decision Dominance), B (Sensor Fusion), and D (Counter-UAS) are addressed by future editions (SHIELD, BASE, NAVAL).

### 4.2 Segment C Stakeholder Heat Map

```
                    Segment C: Training Analytics Champions
                    ═══════════════════════════════════════

Stakeholder              Involvement Level       Key Contribution
─────────────────────────────────────────────────────────────────
S1  Customer             ●●●  Primary           Budget, procurement specs
S2  Training Officer     ●●●  Primary           Workflow requirements, field testing
S3  Range NCO            ●●●  Primary           Usability, daily operations
S4  Unit Commander       ●●●  Primary           Dashboard, comparison, readiness
S5  Soldier              ●●   Significant        Feedback, individual tracking
S6  Instructor           ●●●  Primary           AI coaching, technique analysis
S7  IT Admin             ●●   Significant        Deployment, maintenance, security
S8  Higher Command       ●●●  Primary           Enterprise scale, national rollout
S9  Dev Team             ●●●  Primary           Design, develop, test, iterate
S10 LOMAH Hardware       ●●   Significant        Sensor integration, API stability
S11 Partners             ●    Peripheral          Interop protocols (DIS/TAK)
S12 Regulator            ●●   Significant        Compliance, certification
S13 Cybersecurity        ●●   Significant        Security approval, data protection

Legend: ●●● = Primary stakeholder
        ●●  = Significant involvement
        ●   = Peripheral involvement
```

### 4.3 Upsell Path — Stakeholder Transition Across Editions

| Phase | Edition | Primary Stakeholders | New Stakeholders Added |
|-------|---------|---------------------|----------------------|
| Month 1-6 | RANGE STANDARD | S1-S13 (this analysis) | — |
| Month 6-12 | BASE | S1-S13 + Base Security Officer, Perimeter Guard | Base defense operators, sensor fusion operators |
| Month 6-12 | SHIELD | S1-S13 + Combat Commander, C-UAS Operator | Air defense operators, engagement decision makers |
| Month 12-24 | NAVAL | S1-S13 + Naval CMS Operator, Ship Captain | Naval weapons officers, CIC operators |
| Month 12-24 | ENTERPRISE | S1-S13 + Ministry of Defense, Regional Commands | National-level staff, resource allocation officers |

**Key Insight:** S1 (Customer) and S4 (Unit Commander) are the gateway stakeholders. Their positive experience with RANGE directly drives upsell to BASE/SHIELD. The person who says "CORTEX made our range 10x better" is the same person who asks "Can it protect our base too?"

---

## 5. Stakeholder Communication Plan

### 5.1 Communication Matrix

| Stakeholder | Frequency | Format | Language | Owner | Key Deliverables |
|-------------|-----------|--------|----------|-------|-----------------|
| **S1: Customer** | Monthly + gate reviews | Formal report, range demo | Vietnamese | Program Manager | Progress reports, pilot results, cost-benefit analysis, procurement specs |
| **S2: Training Officer** | Bi-weekly during pilot | Field demonstration, hands-on | Vietnamese | Product Owner | User manual, training session, feedback forms, workflow validation |
| **S3: Range NCO** | Weekly during pilot | Range-side training, observation | Vietnamese | UX Designer | Quick-start guide (laminated), setup training, workflow videos |
| **S4: Unit Commander** | Monthly | Dashboard demo, command briefing | Vietnamese | Program Manager | Readiness dashboard, comparison reports, ROI analysis |
| **S5: Soldier** | Per-session during pilot | Kiosk/tablet interaction, QR card | Vietnamese | UX Designer | Performance card, AI coaching tips, gamification design |
| **S6: Instructor** | Bi-weekly during Phase 2 | Coaching dashboard demo, AI review | Vietnamese | ML Engineer | AI annotation training, technique library, feedback mechanism |
| **S7: IT Admin** | Phase 1 Sprint 5 onwards | Admin manual, deployment training | Vietnamese | DevOps Engineer | Admin manual, health dashboard, update procedures, support channel |
| **S8: Higher Command** | Quarterly | Command briefing, national dashboard | Vietnamese | Program Manager | National readiness demo, enterprise business case, scalability proof |
| **S9: Dev Team** | Daily/bi-weekly | Stand-up, sprint review | Vietnamese + English | Tech Lead | Requirements spec, design docs, sprint backlog, test plans |
| **S10: LOMAH HW** | Weekly | Integration sync, API review | Vietnamese | Integration Lead | API spec (versioned), integration test suite, release coordination |
| **S11: Partners** | Quarterly + trade shows | API docs, interop demo | English | Strategy Lead | OpenAPI spec, DIS/TAK demo, CDM specification, interop test results |
| **S12: Regulator** | Phase 1 gate + certification | Formal compliance dossier | Vietnamese | Quality Manager | Compliance matrix, test reports, AI validation methodology |
| **S13: Cybersecurity** | Pre-deployment + annual | Security assessment, threat model | Vietnamese | Security Lead | Pen test report, data flow diagram, RBAC config, audit log demo |

### 5.2 Gate Review Communication

| Phase Gate | Attendees | Format | Decision Required |
|------------|-----------|--------|------------------|
| Phase 1 to 2 | S1, S2, S3, S4, S7, S9, S12 | Formal review + range demo | Requirements approval; proceed to conceptual design |
| Phase 2 to 3 | S1, S2, S4, S7, S8, S9, S12, S13 | Formal review + architecture presentation | Architecture approval; proceed to detailed design |
| Phase 3 to 4 | S1, S2, S3, S4, S7, S8, S9, S10, S12, S13 | Formal review + MVP demo | Design freeze; proceed to implementation |
| Phase 4 to Pilot | All | Formal review + pilot deployment results | Production authorization; pilot expansion |

### 5.3 Escalation Path

```
Level 1: Dev Team (S9) resolves technical issues internally
    |
Level 2: Product Owner escalates to Customer (S1) / IT Admin (S7)
    |
Level 3: Program Manager escalates to Unit Commander (S4) / Regulator (S12)
    |
Level 4: Customer (S1) escalates to Higher Command (S8) for budget/scope
```

---

## 6. Key Requirements Driven by Each Stakeholder

### 6.1 Requirements Traceability Summary

| Stakeholder | Requirement IDs | Count | Primary Categories |
|-------------|----------------|-------|-------------------|
| **S1: Customer** | CST-001, CST-002, PRD-001, PRD-002, STD-001, SCH-001 | 6 | Cost, Deployment, Standards |
| **S2: Training Officer** | FUN-001 to FUN-004, UXD-001, UXD-002, DAT-001 | 7 | Functionality, UX, Data |
| **S3: Range NCO** | UXD-003 to UXD-007, NET-001 | 6 | UX, Network |
| **S4: Unit Commander** | FUN-005 to FUN-009, DAT-002 | 6 | Functionality, Data |
| **S5: Soldier** | FUN-010 to FUN-013, UXD-008 | 5 | Functionality, UX |
| **S6: Instructor** | FUN-014 to FUN-018 | 5 | Functionality (AI coaching) |
| **S7: IT Admin** | OPS-001 to OPS-007, NET-002 | 8 | Operations, Network |
| **S8: Higher Command** | FUN-019 to FUN-022, DAT-003, SEC-001 | 6 | Functionality, Data, Security |
| **S9: Dev Team** | ARC-001 to ARC-008 | 8 | Architecture |
| **S10: LOMAH HW** | INT-001 to INT-005 | 5 | Integration |
| **S11: Partners** | INT-006 to INT-011 | 6 | Integration (Interop) |
| **S12: Regulator** | SEC-002 to SEC-005, STD-002, STD-003 | 6 | Security, Standards |
| **S13: Cybersecurity** | SEC-001, SEC-006 to SEC-011 | 7 | Security |
| **TOTAL** | | **87** | |

### 6.2 Requirement ID Convention (Software Platform Adapted)

| Prefix | Category | Pahl & Beitz Equivalent | Examples |
|--------|----------|------------------------|---------|
| FUN-xxx | Functionality | Kinematics / Signals | Core features, scoring, dashboards, AI |
| UXD-xxx | User Experience | Ergonomics / Geometry | UI layout, usability, field operation |
| DAT-xxx | Data Management | Signals / Material | CDM schema, data integrity, federation |
| NET-xxx | Networking | Signals / Energy | Connectivity, auto-discovery, protocols |
| INT-xxx | Integration | Assembly / Signals | Hardware API, DIS/TAK, partner systems |
| OPS-xxx | Operations | Operation / Maintenance | Installation, admin, monitoring, updates |
| SEC-xxx | Security | Safety | Cybersecurity, encryption, access control |
| ARC-xxx | Architecture | Material / Assembly | Tech stack, framework, infrastructure |
| PRD-xxx | Deployment | Production / Transport | Localization, on-premise, distribution |
| CST-xxx | Cost | Cost | Licensing, infrastructure cost |
| STD-xxx | Standards | Standards | TCVN, compliance, certification |
| SCH-xxx | Schedule | Schedule | Milestones, delivery timeline |

### 6.3 Top 25 Requirements by Stakeholder Priority

| Rank | Req ID | Requirement | Target | Driven By | ODI Source |
|------|--------|------------|--------|-----------|-----------|
| 1 | FUN-001 | Real-time shot scoring display | <50ms latency | S2, S3 | T04 (16.0), T24 (16.0) |
| 2 | FUN-002 | Multi-system data consolidation | <30 seconds | S2 | T01 (17.5) |
| 3 | DAT-001 | CORTEX CDM unified data model | JSON schema v1.0 | S2, S9 | T01 (17.5), T18 (17.0) |
| 4 | FUN-005 | Commander dashboard — unit readiness | Single-view overview | S4, S8 | T03 (16.5), T22 (16.0) |
| 5 | FUN-003 | Auto-generated training reports | Vietnamese, <30s | S2, S4 | T10 (14.0) |
| 6 | SEC-006 | Air-gapped deployment mode | Zero internet dependency | S13 | Military requirement |
| 7 | SEC-007 | Data encryption | AES-256 rest, TLS 1.3 transit | S13 | Military requirement |
| 8 | FUN-014 | AI technique error classification | ≥10/12 categories | S6 | T12 (15.5) |
| 9 | FUN-010 | Per-shot real-time display at position | <1s after firing | S5 | T04 (16.0) |
| 10 | FUN-006 | Cross-unit comparison | Standardized metrics | S4, S8 | T03 (16.5) |
| 11 | INT-001 | VN-LOMAH integration | All sensor models | S10 | Hardware dependency |
| 12 | SEC-008 | Role-based access control | ≥4 roles | S13 | Military requirement |
| 13 | UXD-003 | System startup time | ≤5 min power-on to operational | S3 | T21 (12.5) |
| 14 | UXD-001 | Tablet-optimized interface | Responsive web, ≥10" | S2 | Field usability |
| 15 | OPS-001 | Installation time | ≤2 hours unbox to operational | S7 | T19 (12.0) |
| 16 | INT-006 | DIS IEEE 1278 output | Custom ShotEvent PDU | S11 | T20 (12.5) |
| 17 | FUN-004 | Soldier performance trends | Session-over-session | S2, S5 | T09 (15.5) |
| 18 | FUN-019 | National readiness dashboard | Multi-range aggregation | S8 | T22 (16.0) |
| 19 | ARC-005 | WebSocket real-time updates | <100ms dashboard | S9 | T04 (16.0) |
| 20 | CST-001 | Perpetual license cost | ≤$25K per range | S1 | Pricing target |
| 21 | PRD-001 | Vietnamese language throughout | UI, reports, coaching tips | S1, S2 | ERG requirement |
| 22 | FUN-011 | Personal performance history | Career-spanning | S5 | T09 (15.5) |
| 23 | INT-007 | CoT/TAK plugin for ATAK | Training data on tactical map | S11 | T20 (12.5) |
| 24 | OPS-004 | Software update mechanism | Single-command update | S7 | OPS requirement |
| 25 | SEC-009 | Tamper-evident audit logging | All data access logged | S13, S12 | Military requirement |

---

## 7. Stakeholder Risks & Mitigations

| # | Risk | Stakeholder | Probability | Impact | Mitigation |
|---|------|------------|-------------|--------|------------|
| R1 | Training officers resist digital transition ("paper works fine") | S2, S3 | High | High | FREE tier with VN-LOMAH purchase removes cost barrier; deploy alongside paper (not replace); demonstrate 60-min time savings on first range day |
| R2 | Range NCOs find system too complex for daily use | S3 | Medium | High | "1-button session start" design principle; 4-hour training maximum; laminated quick-start guide; automatic sensor discovery (zero manual config) |
| R3 | Unit commanders don't trust AI-generated analytics | S4 | Medium | High | Display raw data alongside AI insights; manual override capability; audit trail showing data source for every metric; pilot with skeptical commander first |
| R4 | Cybersecurity officer blocks deployment on military network | S13 | High | High | Air-gap mode designed from day 1 (zero internet); penetration test before first deployment; threat model document; data flow diagram showing no external connections |
| R5 | VN-LOMAH protocol has undocumented edge cases breaking integration | S10 | Medium | Medium | Dedicated integration sprint (Sprint 1); LOMAH hardware team co-located during integration; comprehensive protocol test suite; graceful degradation on unknown data |
| R6 | Soldiers perceive system as surveillance rather than coaching | S5 | Medium | Medium | Individual data visible only to soldier + their instructor; anonymized comparison to unit average; gamification (improvement badges, not absolute ranking); privacy-by-design |
| R7 | Higher command demands features beyond RANGE STANDARD scope | S8 | High | Medium | Clear edition roadmap showing BASE/SHIELD/ENTERPRISE timeline; RANGE STANDARD scope locked at Phase 1 gate; prioritize features by ODI score — if not >12.0, it waits |
| R8 | AI technique analysis (OVERWATCH) insufficiently accurate | S6, S9 | High | Medium | Rules-based classification first (Phase 2); ML model added when 10K+ annotated shots available; instructor override + feedback loop to improve AI; set accuracy expectation at ≥80% not 100% |
| R9 | DIS/TAK interoperability fails with real partner systems | S11 | Medium | Medium | Use open-source Open-DIS and ATAK SDK; test against reference implementations; defer HLA to Phase 3; focus on CoT/TAK (simpler) first |
| R10 | TCVN compliance pathway unclear for AI-based training software | S12 | Medium | Medium | Early engagement with STAMEQ; map existing software quality standards; propose AI validation methodology in Phase 1; no AI-driven lethal decisions in RANGE (training only = lower risk) |
| R11 | Developer capacity insufficient for 12-week Phase 1 | S9 | High | High | 2-developer team focused on SCOREBOARD + PULSE + CDM only; defer OVERWATCH to Phase 2; Python/React = largest talent pool in Vietnam; pre-built libraries (Open-DIS, FastAPI) reduce custom code |
| R12 | Data quality issues from VN-LOMAH sensors create false analytics | S2, S4 | Medium | High | Data validation layer in CDM (reject anomalous shots); sensor health monitoring; calibration verification before each session; flag low-confidence data to user |

---

## Cross-References

- [[CORTEX_C2_ODI_Analysis.md]] — ODI Rev A: 75 outcomes (25 Training T01-T25), 4 segments, 5 editions, revenue model
- [[CORTEX_RANGE_phase0_complete.md]] — Complete Phase 0: job executors, product tree (16 products), CDM schema, data flows, sprint plan, tech stack
- [[CORTEX_RANGE_product_portfolio_musk.md]] — Musk First Principles v2.0: Category Creator thesis, co-opetition ecosystem, real competitors, build sequence
- [[phase0_synthesis.md]] — Phase 0 gate review (10/10 PASS)
- [[RE_cubic_training_systems.md]] — Cubic competitive analysis (MILES, CATS Metrix, SPEAR CDM)
- [[RE_cubic_lvc_integration.md]] — LVC architecture (DIS/HLA/TENA protocols, integration spec)
- [[RE_cae_training_simulation.md]] — CAE co-opetition analysis (Rise analytics, ZERO live-fire)
- [[RE_saab_training_gamer.md]] — Saab GAMER analysis (TaaS validation, force-on-force only)
- [[RE_rheinmetall_training_sts.md]] — Rheinmetall analysis (ZERO AI, niche competitor identification)
- [[01_requirements/requirements_list.md]] — Requirements list (to be created, adapted 16 categories)
