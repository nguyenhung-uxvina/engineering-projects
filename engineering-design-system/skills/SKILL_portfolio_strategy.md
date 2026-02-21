# SKILL: PORTFOLIO STRATEGY
## Multi-Project Resource Allocation & Technology Roadmapping for Defense Products

**Version:** 1.1
**Created:** 2026-02-03
**Updated:** 2026-02-04
**Status:** Active
**Commands:** `/pf`, `/pri`, `/alloc`, `/rm`, `/qr`, `/bc`

---

## ⌨️ SLASH COMMANDS

| Command | Aliases | Purpose |
|---------|---------|---------|
| `/portfolio` | `/pf` | Display portfolio dashboard |
| `/prioritize <quarter>` | `/pri Q1-2026` | Run prioritization matrix |
| `/allocate <projects>` | `/alloc` | Calculate resource allocation |
| `/roadmap <domain>` | `/rm` | Create technology roadmap |
| `/review <quarter>` | `/qr Q1` | Quarterly gate review |
| `/business-case <tech>` | `/bc` | Platform business case analysis |

### Command Output Templates

**`/portfolio`** → Dashboard:
```markdown
| Code | Project | Phase | Status | Priority | Next Action |
|------|---------|-------|--------|----------|-------------|
| VN-001 | UAV | 2 | 🟢 | High | Complete morpho |
```

**`/prioritize`** → Ranking (6 criteria, weighted):
```markdown
| Rank | Project | Score | Recommendation |
|------|---------|-------|----------------|
| 1 | VN-001 | 8.2 | Continue - Full resources |
| 2 | VN-003 | 5.4 | Hold - Resolve risks |
```

**`/allocate`** → Resource matrix:
```markdown
| Resource | VN-001 | VN-002 | Total | Capacity | Util% |
|----------|--------|--------|-------|----------|-------|
| Mech Eng | 80h | 40h | 120h | 160h | 🟢 75% |
```

**`/roadmap`** → Technology evolution:
```
2026 → 2027 → 2028 → 2029
Gen1    Gen2    Gen3    Gen4
```

**`/business-case`** → ROI analysis:
```markdown
| Metric | Value |
|--------|-------|
| Payback | 18 months |
| 5Y NPV | $500K |
| IRR | 35% |
```

---

## 📋 OVERVIEW

### What This Skill Provides

This skill enables **portfolio-level strategic decision making** across multiple concurrent defense product development projects. While individual project skills (ODI, Systems Thinking, P&B) optimize single projects, this skill optimizes the **entire portfolio** for:

- **Resource allocation** across competing projects
- **Technology roadmapping** to maximize reuse and minimize risk
- **Strategic alignment** with organizational capabilities and market needs
- **Risk balancing** across the portfolio (not all high-risk projects)
- **Phased investment** to manage cash flow and reduce exposure

### When to Use This Skill

**Use this skill when:**
- Managing 5+ concurrent projects (resource conflicts inevitable)
- Making go/no-go decisions (which projects to start/continue/kill)
- Planning technology investments (sensors, FCS, materials, etc.)
- Balancing portfolio risk (high-risk innovation vs. low-risk incremental)
- Setting organizational priorities (Phase 2 project vs. Phase 1 project?)

**Don't use this skill for:**
- Single project optimization (use individual project skills)
- Operational execution (use project management tools)
- Financial accounting (use enterprise systems)

---

## 🎯 PORTFOLIO STRATEGY FRAMEWORK

### Three-Horizon Model

```
┌──────────────────────────────────────────────────────────────┐
│  HORIZON 1: CORE BUSINESS (Defend & Extend)                  │
│  ───────────────────────────────────────────────────────────│
│  Timeline:   0-12 months                                     │
│  Focus:      Incremental improvements to existing products   │
│  Risk:       Low (proven tech, known customers)              │
│  Resources:  70% of portfolio budget                         │
│  Examples:   Retrofits, upgrades, variants                   │
│                                                              │
│  Current Portfolio:                                          │
│  • VN-TARGET-BB01 (marine target detection upgrade)          │
│  • VN-RESCUE-DRONE-001 (proven UAV + flotation)             │
│  • BMT-01-HN (training equipment improvement)                │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  HORIZON 2: EMERGING OPPORTUNITIES (Build & Scale)           │
│  ───────────────────────────────────────────────────────────│
│  Timeline:   12-36 months                                    │
│  Focus:      New products leveraging existing capabilities   │
│  Risk:       Medium (new applications, proven tech)          │
│  Resources:  20% of portfolio budget                         │
│  Examples:   Platform extensions, new market segments        │
│                                                              │
│  Current Portfolio:                                          │
│  • RCWS-127-NAVAL (naval adaptation of MTB-20)               │
│  • V-SMASH (C-UAS fire control, new mission)                 │
│  • VN-RC-TX-001-D (defense radio, new product line)          │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  HORIZON 3: FUTURE BETS (Create & Disrupt)                   │
│  ───────────────────────────────────────────────────────────│
│  Timeline:   36+ months                                      │
│  Focus:      Breakthrough innovations, new capabilities      │
│  Risk:       High (unproven tech, uncertain market)          │
│  Resources:  10% of portfolio budget                         │
│  Examples:   AI systems, autonomous platforms, novel sensors │
│                                                              │
│  Current Portfolio:                                          │
│  • VN-TUAV-DEMO-001 (tactical UAV with autonomy)             │
│  • VN-MANPADS-TRAINER (IR seeker simulation, new tech)       │
└──────────────────────────────────────────────────────────────┘

PORTFOLIO BALANCE TARGET: 70% / 20% / 10% (H1 / H2 / H3)
```

---

## 📊 PORTFOLIO ANALYSIS TOOLS

### Tool 1: Project Prioritization Matrix

**Dimensions:**
- **Strategic Value** (alignment with organizational goals)
- **Technical Feasibility** (can we actually build this?)

```
                        HIGH FEASIBILITY
                              │
                              │
        DO LATER          │  DO NOW
        (Medium priority)     │  (HIGH PRIORITY)
        • VN-ARTY-FOS     │  • RCWS-127-NAVAL
        • VN-MORTAR-SIM   │  • V-SMASH
                              │  • VN-TARGET-BB01
    ──────────────────────────┼──────────────────────────
                              │
        AVOID             │  INVESTIGATE
        (Low priority)        │  (High potential, high risk)
        • [None current]  │  • VN-TUAV-DEMO
                              │  • VN-MANPADS-TRAINER
                              │
                        LOW FEASIBILITY

STRATEGIC VALUE SCORING (0-10):
- Market size (0-3): How many units can we sell?
- Strategic importance (0-3): National security impact?
- Competitive advantage (0-2): Can we differentiate?
- Local content (0-2): Supports self-reliance?

TECHNICAL FEASIBILITY SCORING (0-10):
- Technology readiness (0-4): TRL 1-9 mapped to score
- Team capability (0-3): Do we have the skills?
- Supply chain access (0-2): Can we source components?
- Budget adequacy (0-1): Sufficient funding?
```

---

### Tool 2: Resource Allocation Model

**Scarce Resources to Allocate:**
1. **Engineering hours** (500 hrs/month team capacity)
2. **Budget** ($2M annual R&D budget)
3. **Test facilities** (environmental chamber, RF lab, etc.)
4. **Key personnel** (e.g., 1 stabilization expert, 1 AI engineer)

**Allocation Methods:**

#### Method A: Phase-Weighted Allocation
```
Phase 1 (Task Clarification):     10-15% of project budget
Phase 2 (Conceptual Design):      15-20% of project budget
Phase 3 (Embodiment Design):      35-40% of project budget
Phase 4 (Detail Design):          30-35% of project budget

Portfolio Rule: No more than 30% of resources in Phase 1 simultaneously
Rationale: Phase 1 is discovery; too many = diluted focus
```

#### Method B: Strategic Allocation
```
                Hours/Month   Budget/Year   Justification
H1 Projects:    350 (70%)     $1.4M (70%)   Core revenue, low risk
H2 Projects:    100 (20%)     $400K (20%)   Growth engine
H3 Projects:     50 (10%)     $200K (10%)   Future options

Within H2:
- RCWS-127-NAVAL:  60 hrs/month   (Phase 1→2 transition)
- V-SMASH:         30 hrs/month   (Phase 2 active)
- VN-RC-TX-001-D:  10 hrs/month   (Phase 1 holding)
```

#### Method C: Opportunity Cost Analysis
```
When choosing between projects, calculate:

Opportunity Score = (Strategic Value × Technical Feasibility × ODI Success Prob) / Resource Cost

Example:
RCWS-127-NAVAL: (8.5 × 7.0 × 0.85) / 500 hrs = 0.101
V-SMASH:        (7.0 × 8.0 × 0.75) / 300 hrs = 0.140  ← HIGHER priority

Decision: Prioritize V-SMASH if resources constrained
```

---

### Tool 3: Technology Roadmap

**Purpose:** Identify common technology needs across projects to maximize reuse and minimize redundant development.

**Technology Domains:**
1. Stabilization & Motion Control
2. Sensors (EO/IR, Thermal, Radar)
3. Fire Control Systems (FCS)
4. Communications & Networking
5. Materials & Structures
6. Power Systems

**Roadmap Structure:**

```
DOMAIN: STABILIZATION & MOTION CONTROL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Technology        2026        2027        2028        2029
Generation        Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3 Q4 Q1 Q2 Q3
────────────────────────────────────────────────────────────────
Gen 1:            ████████████
2-axis Gyro       └─► RCWS-127-NAVAL
(Import COTS)         V-SMASH

Gen 2:                        ████████████████
2-axis + Inertial             └─► VN-TUAV-DEMO
Fusion (Hybrid)                   Naval Variant 2

Gen 3:                                        ████████████████
3-axis + AI                                   └─► Next-gen RCWS
Predictive                                        Autonomous UAV

────────────────────────────────────────────────────────────────
INVESTMENT DECISION POINTS:
├─ 2026-Q2: Source Gen 1 supplier (Korea/China)
├─ 2027-Q1: Develop Gen 2 (local IP, competitive advantage)
└─ 2028-Q3: Evaluate Gen 3 AI maturity (TRL 6+ required)

REUSE OPPORTUNITIES:
• Gen 1 platform → 3 projects (RCWS, V-SMASH, VN-NAVAL-GUNNERY)
• Cost saving: $150K NRE avoided (develop once, use 3×)
• Risk reduction: Proven tech reduces integration risk
```

**Technology Roadmap Template:**

| Technology | Current State | Target State (2027) | Projects Benefiting | Investment Required | Decision Date |
|------------|---------------|---------------------|---------------------|---------------------|---------------|
| 2-axis Stabilization | Import COTS | Local integration capability | RCWS-127, V-SMASH, VN-NAVAL-GUNNERY | $80K (1 engineer × 12 months) | 2026-Q2 |
| Thermal Imaging | Import sensors | Sensor fusion algorithms | RCWS-127, VN-TARGET-BB01, V-SMASH | $120K (AI engineer) | 2026-Q3 |
| AI Fire Control | Research | TRL 5 prototype | V-SMASH, RCWS-127 Gen 2 | $200K (external research) | 2027-Q1 |
| LiPo Battery Tech | COTS (Tattu) | Local assembly + BMS | All UAV projects (3+) | $60K (electronics) | 2026-Q4 |

**PORTFOLIO SYNERGY SCORE:**
- Standalone development: 5 projects × $100K = $500K
- Shared technology development: $460K (8% savings)
- Risk reduction: 5 separate failures → 1 technology risk
- **Recommendation:** Invest in shared tech platforms

---

### Tool 4: Phase Gate Portfolio Review

**Purpose:** Review all projects at their phase gates simultaneously to make comparative decisions.

**Review Cadence:** Quarterly (align with fiscal quarters)

**Review Structure:**

```
┌─────────────────────────────────────────────────────────────┐
│  Q2 2026 PORTFOLIO GATE REVIEW                              │
└─────────────────────────────────────────────────────────────┘

GATE 1 → PHASE 2 (Task Clarification → Conceptual Design)
─────────────────────────────────────────────────────────────
Project               Req Score   Conflicts   ODI Score   DECISION
RCWS-127-NAVAL        95% ✅      Resolved    8.7/10      → APPROVE (HIGH)
VN-TARGET-BB01        88% ✅      1 pending   7.2/10      → APPROVE (MEDIUM)
VN-RESCUE-DRONE-001   82% ✅      None        6.8/10      → APPROVE (MEDIUM)
VN-RC-TX-001-D        75% ⚠️      2 conflicts 6.5/10      → HOLD (resolve conflicts)

GATE 2 → PHASE 3 (Conceptual Design → Embodiment)
─────────────────────────────────────────────────────────────
Project               VDI 2225    Concepts    Tech Risk   DECISION
V-SMASH               74% ✅      5 evaluated Low         → APPROVE

GATE 3 → PHASE 4 (Embodiment → Detail)
─────────────────────────────────────────────────────────────
[None at Gate 3 this quarter]

RESOURCE ALLOCATION DECISION:
├─ HIGH priority (60% resources):  RCWS-127-NAVAL, V-SMASH
├─ MEDIUM priority (30% resources): VN-TARGET-BB01, VN-RESCUE-DRONE
└─ HOLD (10% resources):           VN-RC-TX-001-D (finalize requirements)

STRATEGIC DECISIONS:
• Accelerate RCWS-127-NAVAL (high ODI score, strategic importance)
• V-SMASH moves to Phase 3 (no blockers, resources available)
• VN-RC-TX-001-D delayed 1 quarter (resolve requirement conflicts first)
```

---

## 🎲 RISK PORTFOLIO BALANCING

### Risk Dimensions

**Technical Risk:**
- TRL 1-3: Research (high risk)
- TRL 4-6: Development (medium risk)
- TRL 7-9: Production (low risk)

**Market Risk:**
- New customer segment: High
- Existing customer, new product: Medium
- Existing customer, upgrade: Low

**Execution Risk:**
- Phase 1: Low (just requirements)
- Phase 2: Medium (concept risk)
- Phase 3-4: High (committed resources)

### Portfolio Risk Matrix

```
                        TECHNICAL RISK
                    Low    Medium    High
                    │       │        │
        High    │  AVOID  │ LIMIT  │ SINGLE BET
MARKET          │         │        │ (Max 1 project)
RISK   Medium   │  CORE   │ GROWTH │ OPTION
                │ (70%)   │ (20%)  │ (10%)
        Low     │  SAFE   │ SAFE   │ INVESTIGATE
                │         │        │
```

**Current Portfolio Risk Analysis:**

| Project | Tech Risk | Market Risk | Quadrant | % of Budget |
|---------|-----------|-------------|----------|-------------|
| VN-TARGET-BB01 | Low | Low | SAFE | 15% |
| VN-RESCUE-DRONE-001 | Low | Medium | CORE | 12% |
| RCWS-127-NAVAL | Medium | Low | CORE | 20% ⭐ |
| V-SMASH | Medium | Medium | GROWTH | 18% |
| VN-RC-TX-001-D | Medium | High | OPTION | 5% |
| VN-TUAV-DEMO | High | High | SINGLE BET | 8% |
| Others (8 projects) | Varies | Varies | Mixed | 22% |

**Portfolio Risk Health Check:**
- ✅ SAFE + CORE = 47% (target: 60-70%) → Slightly aggressive
- ✅ GROWTH = 18% (target: 20-25%) → On target
- ⚠️ SINGLE BET = 8% (target: <10%) → On edge
- ⚠️ AVOID quadrant = 0% → Good (no projects to kill)

**Rebalancing Recommendation:**
- Reduce SINGLE BET exposure: VN-TUAV-DEMO to 5% (de-risk or descope)
- Increase CORE: Move 3% to VN-TARGET-BB01 (accelerate low-risk revenue)

---

## 🗺️ STRATEGIC ROADMAPPING

### Product Line Strategy

**Three Product Lines Identified:**

```
┌───────────────────────────────────────────────────────────┐
│  PRODUCT LINE 1: WEAPON STATIONS & FIRE CONTROL           │
│  ────────────────────────────────────────────────────────│
│  Vision: Complete range of remote weapon stations         │
│  Timeline: 2026-2029                                      │
│                                                           │
│  2026    2027    2028    2029                             │
│  ├───────┼───────┼───────┼───────                         │
│  │       │       │       │                                │
│  MTB-20  RCWS-127 V-SMASH  30mm RCWS                      │
│  (Ground) NAVAL  (C-UAS)  (Naval)                         │
│          │       │       │                                │
│          └───────┴───────┴─► Fire Control Platform (FCP)  │
│                              Common core, multiple weapons│
│                                                           │
│  STRATEGIC GOAL: 60% market share in VN defense RCWS      │
│  KEY TECHNOLOGY: Stabilization, FCS, AI tracking          │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│  PRODUCT LINE 2: TRAINING & SIMULATION                    │
│  ────────────────────────────────────────────────────────│
│  Vision: Digital twin training for all weapon systems     │
│  Timeline: 2026-2028                                      │
│                                                           │
│  2026         2027         2028                           │
│  ├─────────────┼───────────┼───────                       │
│  │             │           │                              │
│  VN-B41SIM    VN-ARTY-FOS  VN-NAVAL-GUNNERY              │
│  VN-MANPADS   VN-MORTAR    Training Platform 2.0         │
│  VN-ADTS      │           │                              │
│               └───────────┴─► Common Simulation Engine    │
│                                                           │
│  STRATEGIC GOAL: 40% cost vs. live fire training          │
│  KEY TECHNOLOGY: VR/AR, ballistic models, AAR analytics   │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│  PRODUCT LINE 3: AUTONOMOUS SYSTEMS                       │
│  ────────────────────────────────────────────────────────│
│  Vision: Low-cost autonomous platforms (air, sea, ground) │
│  Timeline: 2027-2030 (FUTURE BET)                         │
│                                                           │
│  2027         2028         2029         2030              │
│  ├─────────────┼───────────┼───────────┼───────           │
│  │             │           │           │                  │
│  VN-TUAV      VN-RESCUE   TARGET      LOITERING          │
│  (Demo)       DRONE 2.0   DRONE       MUNITION           │
│               │           (Swarm)     (Kamikaze)         │
│               └───────────┴───────────┴─► Autonomy Stack  │
│                                                           │
│  STRATEGIC GOAL: Technology leadership in region          │
│  KEY TECHNOLOGY: AI navigation, swarm coordination        │
└───────────────────────────────────────────────────────────┘
```

---

### Technology Evolution Strategy

**Make vs. Buy Decision Framework:**

| Technology | Strategic Importance | Vietnamese Capability | Decision | Timeline |
|------------|---------------------|----------------------|----------|----------|
| **Stabilization (2-axis)** | HIGH (competitive advantage) | Medium (can develop) | MAKE (local IP) | 2027-Q1 |
| **Thermal sensors** | Medium | Low (import only) | BUY (COTS) | Ongoing |
| **AI fire control** | HIGH (future differentiator) | Medium (research capability) | PARTNER (university + vendor) | 2026-Q3 |
| **Marine coatings** | Low (commodity) | High (local suppliers) | BUY (local) | Ongoing |
| **Gyroscopes (MEMS)** | Medium | None (import restricted) | BUY (China/Korea) | 2026-Q2 |
| **LiPo battery packs** | Low | Medium (assembly capability) | MAKE (assembly, BUY cells) | 2026-Q4 |

**Investment Priority:**
1. **HIGH priority (invest now):** Stabilization, AI FCS → competitive moat
2. **MEDIUM priority (monitor):** Battery tech → cost optimization
3. **LOW priority (buy forever):** Sensors, gyros → commodity, not strategic

---

## 📈 PORTFOLIO METRICS & DASHBOARDS

### Key Performance Indicators (KPIs)

**Portfolio Health Metrics:**

| Metric | Target | Current | Trend | Action |
|--------|--------|---------|-------|--------|
| **Phase Distribution Balance** | 40/30/20/10 | 50/35/15/0 | ⚠️ Top-heavy | Move 2 projects to Phase 2 |
| **Innovation Success Rate** | 70%+ (with ODI) | TBD | - | Track from Q3 2026 |
| **Resource Utilization** | 85-95% | 78% | ⚠️ Low | Reassign idle hours |
| **Portfolio Risk Score** | 3-5 (1-10 scale) | 4.2 | ✅ Balanced | Maintain |
| **Technology Reuse %** | >40% | 32% | ⚠️ Low | Prioritize platform development |
| **Local Content (Avg)** | >65% | 61% | ✅ On track | Continue |
| **Gate Review Cycle Time** | <2 weeks | 3.5 weeks | ⚠️ Slow | Streamline process |

---

### Portfolio Dashboard Template

```
┌─────────────────────────────────────────────────────────────┐
│  DEFENSE PRODUCT PORTFOLIO DASHBOARD - Q2 2026             │
└─────────────────────────────────────────────────────────────┘

PORTFOLIO VALUE
─────────────────────────────────────────────────────────────
Total Projects:              14
Active (Funded):             13
On Hold:                      1
Total Budget:            $2.0M/year
Committed (YTD):         $0.8M (40%)
Forecast (EOY):          $1.9M (95% utilization ✅)

PHASE DISTRIBUTION
─────────────────────────────────────────────────────────────
Phase 1 (Task Clarification):   █████████████░░  13 projects (93%)
Phase 2 (Conceptual Design):    █░░░░░░░░░░░░░░   1 project  (7%)
Phase 3 (Embodiment Design):    ░░░░░░░░░░░░░░░   0 projects (0%)
Phase 4 (Detail Design):        ░░░░░░░░░░░░░░░   0 projects (0%)
                                ⚠️ IMBALANCE: Too many in Phase 1

HORIZON DISTRIBUTION (Budget %)
─────────────────────────────────────────────────────────────
H1 (Core):     ███████████████████░░░░░  65%  (Target: 70%)
H2 (Growth):   ██████░░░░░░░░░░░░░░░░░░  25%  (Target: 20%) ⚠️
H3 (Future):   ███░░░░░░░░░░░░░░░░░░░░░  10%  (Target: 10%) ✅

RISK BALANCE
─────────────────────────────────────────────────────────────
Low Risk:      ████████░░░░░░░░  40%
Medium Risk:   ████████████░░░░  55%
High Risk:     █░░░░░░░░░░░░░░░   5%
               ✅ BALANCED

TOP 5 PROJECTS (by Strategic Score)
─────────────────────────────────────────────────────────────
1. RCWS-127-NAVAL       Phase 1→2    Score: 8.7/10  ⭐⭐⭐⭐⭐
2. V-SMASH              Phase 2      Score: 7.8/10  ⭐⭐⭐⭐
3. VN-TARGET-BB01       Phase 1      Score: 7.2/10  ⭐⭐⭐⭐
4. VN-RESCUE-DRONE-001  Phase 1      Score: 6.8/10  ⭐⭐⭐
5. VN-RC-TX-001-D       Phase 1      Score: 6.5/10  ⭐⭐⭐

BOTTLENECKS & CONSTRAINTS
─────────────────────────────────────────────────────────────
⚠️ Stabilization expertise (1 engineer, 3 projects need)
⚠️ Environmental test chamber (2 projects waiting)
✅ Budget: 5% headroom available
✅ Team capacity: 22% idle (can take more work)

TECHNOLOGY READINESS
─────────────────────────────────────────────────────────────
Stabilization (2-axis):    TRL 7  ✅ (COTS available)
AI Fire Control:           TRL 4  ⚠️ (Research phase)
Thermal Sensors:           TRL 9  ✅ (Production ready)
Swarm Coordination:        TRL 3  ⚠️ (Early research)

NEXT QUARTER PRIORITIES
─────────────────────────────────────────────────────────────
1. Move RCWS-127-NAVAL to Phase 2 (Gate 1 approval)
2. Move V-SMASH to Phase 3 (Gate 2 approval)
3. Consolidate 4 training projects → common platform
4. Source stabilization supplier (Korea/China)
5. Hire AI engineer (support V-SMASH + future projects)
```

---

## 🔄 PORTFOLIO OPTIMIZATION WORKFLOWS

### Workflow 1: Quarterly Portfolio Review

**Cadence:** Every 3 months (aligned with fiscal quarters)

**Participants:**
- Portfolio Manager (decision authority)
- Technical Lead (feasibility assessment)
- Finance (budget allocation)
- Project Leads (project status)

**Agenda (4-hour session):**

```
PART 1: PORTFOLIO HEALTH (60 min)
├─ Review portfolio metrics dashboard
├─ Identify bottlenecks and constraints
├─ Assess resource utilization (engineers, budget, facilities)
└─ Technology readiness review

PART 2: PROJECT GATE REVIEWS (90 min)
├─ Gate 1 reviews (5 projects × 10 min each)
├─ Gate 2 reviews (1 project × 20 min)
├─ Gate 3 reviews (0 projects)
└─ Gate 4 reviews (0 projects)

BREAK (15 min)

PART 3: STRATEGIC DECISIONS (60 min)
├─ Go/No-Go decisions (which projects to approve/kill)
├─ Resource reallocation (where to shift engineering hours)
├─ Technology investment decisions (make vs. buy)
└─ Horizon rebalancing (shift budget between H1/H2/H3)

PART 4: NEXT QUARTER PLANNING (15 min)
├─ Set priorities for next 3 months
├─ Assign action items
└─ Schedule next review
```

**Decision Rules:**

| Decision | Approval Threshold | Veto Power |
|----------|-------------------|------------|
| Gate 1 → Phase 2 | 80% requirements quantified + stakeholder sign-off | Portfolio Manager |
| Gate 2 → Phase 3 | VDI 2225 ≥70% + tech risk acceptable | Technical Lead + Finance |
| Gate 3 → Phase 4 | DfX review complete + cost within budget | Finance + Portfolio Manager |
| Gate 4 → Production | All tests passed + production plan | Portfolio Manager (final) |
| **Kill Project** | 3 consecutive gate failures OR strategic misalignment | Portfolio Manager (unanimous) |

---

### Workflow 2: Technology Platform Decision

**Trigger:** Multiple projects need the same technology

**Example:** Stabilization needed by RCWS-127-NAVAL, V-SMASH, VN-NAVAL-GUNNERY

**Decision Process:**

```
STEP 1: IDENTIFY COMMONALITY
─────────────────────────────────────────────────────────────
Technology:       2-axis gyro stabilization
Projects needing: RCWS-127-NAVAL (2026-Q2)
                  V-SMASH (2026-Q3)
                  VN-NAVAL-GUNNERY (2027-Q1)
Total demand:     3 projects × $80K standalone = $240K

STEP 2: EVALUATE OPTIONS
─────────────────────────────────────────────────────────────
Option A: Each project sources independently
  Cost:      $240K (3 × $80K)
  Time:      3 × 6 months (sequential)
  Risk:      3 integration risks (3× chance of failure)
  Control:   Low (vendor-dependent)

Option B: Develop common platform (RECOMMENDED)
  Cost:      $150K (1× development + 3× $10K integration)
  Time:      9 months (parallel integration)
  Risk:      1 development risk (but reused 3×)
  Control:   High (local IP)

Option C: Partner with university
  Cost:      $100K (government grant + $50K internal)
  Time:      18 months (research pace)
  Risk:      Medium (academic uncertainty)
  Control:   Medium (shared IP)

STEP 3: DECISION CRITERIA
─────────────────────────────────────────────────────────────
Strategic Importance:  HIGH (competitive advantage)
Time Sensitivity:      MEDIUM (RCWS-127 needs by 2026-Q4)
Budget Available:      $150K (within portfolio budget)
Risk Tolerance:        MEDIUM (not mission-critical yet)

STEP 4: DECISION
─────────────────────────────────────────────────────────────
✅ SELECT OPTION B: Develop common platform

RATIONALE:
- Cost savings: $90K (38% reduction)
- Strategic IP: Own stabilization technology (competitive moat)
- Risk acceptable: If platform fails, fall back to Option A
- Timeline fits: 9 months → ready for V-SMASH (2026-Q3)

ACTION ITEMS:
[ ] Allocate $150K from portfolio budget (2026-Q2)
[ ] Assign lead engineer (stabilization expert)
[ ] Define platform requirements (input from 3 projects)
[ ] Source gyro hardware (Korea/China, COTS)
[ ] Develop integration software (local IP)
[ ] Validate with RCWS-127 (first customer)
[ ] Reuse for V-SMASH and VN-NAVAL-GUNNERY
```

---

### Workflow 3: Resource Conflict Resolution

**Trigger:** Two projects need the same scarce resource

**Example:** Stabilization engineer needed by both RCWS-127-NAVAL (Phase 2) and V-SMASH (Phase 3)

**Resolution Process:**

```
STEP 1: QUANTIFY CONFLICT
─────────────────────────────────────────────────────────────
Resource:         Senior Stabilization Engineer (1 person)
RCWS-127 needs:   80 hrs/month (Phase 2 conceptual design)
V-SMASH needs:    120 hrs/month (Phase 3 embodiment design)
Total demand:     200 hrs/month
Available:        160 hrs/month (1 FTE)
SHORTFALL:        40 hrs/month ⚠️

STEP 2: PRIORITIZATION
─────────────────────────────────────────────────────────────
Project         Phase   Strategic Score   ODI Score   Urgency
RCWS-127-NAVAL  2       8.7/10           8.7/10      HIGH (customer waiting)
V-SMASH         3       7.8/10           7.5/10      MEDIUM (Phase 3 can slip)

Priority: RCWS-127-NAVAL (higher score + higher urgency)

STEP 3: RESOLUTION OPTIONS
─────────────────────────────────────────────────────────────
Option A: Sequential (finish RCWS, then V-SMASH)
  RCWS impact:  None (gets full 80 hrs)
  V-SMASH impact: Delayed 2 months ⚠️
  Cost:         $0
  Risk:         V-SMASH customer dissatisfaction

Option B: Split resource (50/50)
  RCWS impact:  Slower progress (80 hrs → 80 hrs, supplemented elsewhere)
  V-SMASH impact: Slower progress (120 hrs → 80 hrs)
  Cost:         $0
  Risk:         Both projects delayed ⚠️⚠️

Option C: Hire contractor (3 months)
  RCWS impact:  None (keeps 80 hrs)
  V-SMASH impact: None (contractor provides 40 hrs, engineer 80 hrs)
  Cost:         $30K (contractor for 3 months)
  Risk:         Low (covers shortfall exactly)

Option D: Descope V-SMASH temporarily
  RCWS impact:  None
  V-SMASH impact: Delayed 1 month (reduce scope to 80 hrs/month)
  Cost:         $0
  Risk:         Low (scope can be added later)

STEP 4: DECISION
─────────────────────────────────────────────────────────────
✅ SELECT OPTION C: Hire contractor

RATIONALE:
- Both projects stay on schedule (portfolio value maximized)
- Cost ($30K) < revenue impact of delays (>$100K)
- Risk low (3-month commitment, contractor is supplement, not lead)
- Sustainable (contractor can train junior engineer)

ACTION ITEMS:
[ ] Approve $30K budget from portfolio reserve
[ ] Post contractor role (stabilization engineer, 3-month contract)
[ ] Assign contractor to V-SMASH (under senior engineer supervision)
[ ] Senior engineer allocates: 80 hrs RCWS + 80 hrs V-SMASH (lead only)
[ ] Contractor provides: 40 hrs V-SMASH (execution, supervised)
[ ] Re-evaluate after 3 months (hire full-time if portfolio grows)
```

---

## 🎯 STRATEGIC ALIGNMENT TOOLS

### Tool 1: Organizational Capability Assessment

**Purpose:** Ensure projects match organizational strengths and growth direction.

**Capability Dimensions:**

| Capability | Current Level | Target (2027) | Gap | Investment |
|------------|---------------|---------------|-----|------------|
| **Mechanical Design** | 8/10 (Strong) | 9/10 | Small | $20K (CAD training) |
| **Stabilization & Control** | 4/10 (Weak) | 7/10 | **LARGE** | $150K (hire + tech dev) ⭐ |
| **AI & Machine Learning** | 3/10 (Weak) | 6/10 | **LARGE** | $200K (hire + research) ⭐ |
| **Marine Engineering** | 5/10 (Medium) | 7/10 | Medium | $60K (corrosion expert) |
| **Systems Integration** | 7/10 (Strong) | 8/10 | Small | $10K (training) |
| **Testing & Validation** | 6/10 (Medium) | 8/10 | Medium | $100K (test facilities) |
| **Supply Chain (Defense)** | 7/10 (Strong) | 8/10 | Small | $15K (supplier dev) |

**Strategic Implications:**

```
PROJECTS ALIGNED WITH STRENGTHS (Low Risk):
✅ VN-TARGET-BB01 (uses Mechanical Design strength)
✅ VN-RESCUE-DRONE-001 (uses Systems Integration strength)
✅ BMT-01-HN (uses Mechanical + Testing strength)

PROJECTS REQUIRING CAPABILITY BUILDING (Medium Risk):
⚠️ RCWS-127-NAVAL (needs Marine Engineering + Stabilization)
   → Invest in capabilities BEFORE Phase 2
   → Mitigate: Hire corrosion expert, develop stabilization platform

⚠️ V-SMASH (needs AI & Machine Learning)
   → Invest in capabilities DURING Phase 2
   → Mitigate: Partner with university, hire AI engineer

PROJECTS BEYOND CURRENT CAPABILITY (High Risk):
🔴 VN-TUAV-DEMO (needs AI + Autonomous Systems, not developed yet)
   → OPTIONS: (1) Delay until 2027, (2) Partner with specialist, (3) Kill
   → DECISION: Delay to 2027, monitor AI capability development
```

---

### Tool 2: Market-Technology Matrix

**Purpose:** Ensure portfolio covers both existing markets (low risk) and new markets (growth).

```
                        TECHNOLOGY
                Existing    Related     New
                    │         │          │
        ┌───────────┼─────────┼──────────┼───────────┐
        │           │         │          │           │
Existing│  DEFEND   │ EXTEND  │ INNOVATE │           │
        │  (40%)    │ (30%)   │  (10%)   │           │
MARKET  │  ────────────────────────────  │           │
        │  VN-TARGET│ RCWS-127│ V-SMASH  │           │
        │  BB01     │ NAVAL   │ (C-UAS)  │           │
        ├───────────┼─────────┼──────────┼───────────┤
        │           │         │          │           │
New     │  EXPAND   │ BUILD   │ CREATE   │           │
        │  (10%)    │ (5%)    │  (5%)    │           │
        │  ────────────────────────────  │           │
        │  VN-RC-TX │ VN-TUAV │ [Future] │           │
        │  (New     │ DEMO    │          │           │
        │   segment)│         │          │           │
        └───────────┴─────────┴──────────┴───────────┘

PORTFOLIO BALANCE CHECK:
- Defend + Extend = 70% ✅ (target: 60-80%) CORE BUSINESS
- Innovate + Build = 15% ⚠️ (target: 15-25%) GROWTH ENGINE (low end)
- Expand + Create = 15% ✅ (target: 10-15%) FUTURE OPTIONS

REBALANCING RECOMMENDATION:
- Increase INNOVATE: Accelerate V-SMASH (proven market, new tech)
- Add to BUILD: Fast-track VN-TUAV-DEMO if AI capability ready
```

---

## 📊 CASE STUDY: RCWS-127-NAVAL PORTFOLIO IMPACT

### Scenario: Portfolio-Level Decision for RCWS-127-NAVAL

**Context:** RCWS-127-NAVAL has completed Phase 1 with excellent results (ODI 8.7/10, Requirements 95% quantified, Systems analysis complete). Portfolio Manager must decide:

1. **Go/No-Go for Phase 2?**
2. **Resource allocation level?** (High, Medium, Low priority)
3. **Technology platform investment?** (Stabilization platform development)

---

### Decision Analysis

#### **STEP 1: Project-Level Assessment**

**Strengths:**
- ✅ ODI score 8.7/10 (top outcome: ship motion compensation, Opp 14.9)
- ✅ Customer segment clear (50% Fast Responders, Vietnamese Navy)
- ✅ Requirements 95% quantified (exceeds 80% target)
- ✅ Systems analysis complete (4 CLDs, leverage points identified)
- ✅ Technical feasibility HIGH (2-axis gyro is TRL 7, available COTS)

**Weaknesses:**
- ⚠️ Cost target aggressive ($250K vs $600K imports, 42% of competitor)
- ⚠️ Stabilization expertise gap (need to hire or develop)
- ⚠️ Marine engineering capability gap (corrosion risk if not done right)
- ⚠️ Gyro export control risk (ITAR restrictions)

**Individual Project Recommendation:** ✅ GO (strong fundamentals)

---

#### **STEP 2: Portfolio-Level Assessment**

**Portfolio Context:**
- 13 active projects, 93% in Phase 1 (bottleneck!)
- Only 1 project in Phase 2 (V-SMASH)
- 0 projects in Phase 3-4 (no revenue yet)
- **Portfolio imbalance:** Too many Phase 1, need to advance some to Phase 2-3

**Resource Availability:**
- Engineering hours: 78% utilized (22% idle capacity)
- Budget: $200K unallocated (10% of annual budget)
- Stabilization engineer: 40 hrs/month available (after V-SMASH allocation)

**Strategic Fit:**
- Product Line 1 (Weapon Stations): Strategic priority ⭐⭐⭐⭐⭐
- Horizon 2 (Growth): Naval RCWS is new product line, proven tech
- Risk Profile: Medium (tech proven, market validated, execution risk only)
- Market-Technology: EXTEND quadrant (existing market, related technology)

**Portfolio Synergy:**
- Technology reuse: Stabilization platform → benefits V-SMASH, VN-NAVAL-GUNNERY (3 projects)
- Customer: Vietnamese Navy (also customer for VN-TARGET-BB01, VN-NAVAL-GUNNERY)
- Supplier: MTB-20 base → 40% reuse (reduces development cost/risk)

**Portfolio-Level Recommendation:** ✅ GO + HIGH PRIORITY

---

#### **STEP 3: Resource Allocation Decision**

**Option A: Low Priority (50 hrs/month, $50K)**
- Slow progress (Phase 2 takes 9 months instead of 6)
- Saves resources for other projects
- Risk: Customer loses interest (Navy has budget now, may evaporate)

**Option B: Medium Priority (100 hrs/month, $100K)** ← BASELINE
- Normal progress (Phase 2 in 6 months)
- Balanced resource use
- Risk: Stabilization platform not developed (must buy COTS)

**Option C: High Priority (150 hrs/month, $200K)** ← **RECOMMENDED**
- Fast progress (Phase 2 in 4 months)
- Includes stabilization platform development ($150K)
- Benefits portfolio (V-SMASH and VN-NAVAL-GUNNERY reuse platform)
- Risk: Ties up resources (but 22% idle capacity available)

**DECISION:** ✅ Option C (High Priority)

**Rationale:**
1. **Portfolio bottleneck:** 93% projects in Phase 1, need to advance leaders
2. **Idle capacity:** 22% idle → can absorb 150 hrs/month
3. **Technology platform ROI:**
   - Standalone: $240K (3 projects × $80K each)
   - Platform: $150K + 3× $10K integration = $180K
   - **Savings: $60K (25% reduction)**
   - **Strategic IP:** Own stabilization tech (competitive moat)
4. **Customer urgency:** Navy budget approved for 2026-2027, must deliver prototype by 2027-Q2
5. **Market leadership:** First-mover advantage in Vietnamese naval RCWS market

---

#### **STEP 4: Technology Platform Decision**

**Should we develop a common stabilization platform?**

**Benefits:**
- Cost savings: $60K across 3 projects
- Competitive advantage: Local IP, not vendor-dependent
- Capability building: Grow stabilization expertise (currently 4/10 → 7/10)
- Portfolio acceleration: V-SMASH and VN-NAVAL-GUNNERY faster when platform ready

**Risks:**
- Development risk: Platform may not work (fall back to COTS)
- Time risk: 9 months development (but RCWS-127 is first customer, validates platform)
- Resource risk: Ties up stabilization engineer (but this IS the priority)

**DECISION:** ✅ Develop stabilization platform

**Implementation:**
- Budget: $150K allocated from portfolio (10% of annual budget)
- Team: 1 senior engineer + 1 contractor (3 months)
- Timeline: 2026-Q2 → 2026-Q4 (9 months)
- First customer: RCWS-127-NAVAL (validates platform)
- Subsequent customers: V-SMASH (2026-Q4), VN-NAVAL-GUNNERY (2027-Q1)

---

### Decision Summary

```
┌─────────────────────────────────────────────────────────────┐
│  PORTFOLIO DECISION: RCWS-127-NAVAL                         │
└─────────────────────────────────────────────────────────────┘

GATE 1 APPROVAL:          ✅ APPROVED (Phase 1 → Phase 2)
RESOURCE PRIORITY:        ⭐⭐⭐ HIGH (150 hrs/month, $200K)
TECHNOLOGY PLATFORM:      ✅ DEVELOP (stabilization platform, $150K)

RATIONALE:
• Top strategic priority (Product Line 1: Weapon Stations)
• Strong fundamentals (ODI 8.7/10, Requirements 95% quantified)
• Portfolio synergy (technology reuse across 3 projects, $60K savings)
• Idle capacity available (22% → absorb 150 hrs/month)
• Customer urgency (Navy budget window 2026-2027)
• First-mover advantage (Vietnamese naval RCWS market leadership)

RISKS & MITIGATIONS:
⚠️ Cost target aggressive → Mitigate: Reuse MTB-20 (40%), local fab
⚠️ Stabilization expertise gap → Mitigate: Hire + develop platform
⚠️ Gyro export control → Mitigate: Source from Korea/China (non-ITAR)

PORTFOLIO IMPACT:
• Advances 1 project from Phase 1 → Phase 2 (reduces bottleneck)
• Creates reusable tech platform (benefits 2 more projects)
• Builds organizational capability (Stabilization 4/10 → 7/10)
• Revenue potential: 20 units × $250K = $5M (2-year pipeline)

NEXT ACTIONS:
[ ] Allocate $200K budget (2026-Q2)
[ ] Assign lead engineer + hire contractor
[ ] Schedule Phase 2 kickoff (function structure development)
[ ] Initiate stabilization platform development (parallel track)
[ ] Source gyro hardware (Korea/China, COTS)
[ ] Stakeholder briefing (Navy, MTB-20 supplier)

STATUS: ✅ APPROVED - PROCEED TO PHASE 2
```

---

## 📚 PORTFOLIO STRATEGY TEMPLATES

### Template 1: Quarterly Portfolio Review Agenda

```markdown
# PORTFOLIO REVIEW - [QUARTER YEAR]
**Date:** [Date]
**Participants:** [Names]

## 1. PORTFOLIO HEALTH (60 min)

### 1.1 Metrics Dashboard
- [ ] Review KPIs (phase distribution, resource utilization, risk balance)
- [ ] Identify trends (improving/declining metrics)
- [ ] Flag red alerts (>10% deviation from targets)

### 1.2 Resource Status
- [ ] Engineering hours: Utilized ___%, Idle ___%, Overbooked ____%
- [ ] Budget: Spent ___% YTD, Forecast ___% EOY
- [ ] Facilities: Environmental chamber queue, RF lab queue
- [ ] Key personnel: Bottlenecks identified

### 1.3 Technology Readiness
- [ ] Stabilization: TRL ___, Status: ___
- [ ] AI FCS: TRL ___, Status: ___
- [ ] [Other critical techs]

---

## 2. PROJECT GATE REVIEWS (90 min)

### Gate 1 Reviews (Phase 1 → Phase 2)
| Project | Req Score | Conflicts | ODI | Decision |
|---------|-----------|-----------|-----|----------|
| [Name]  | ___%      | [Status]  | ___ | GO/HOLD/KILL |

### Gate 2 Reviews (Phase 2 → Phase 3)
| Project | VDI 2225 | Concepts | Tech Risk | Decision |
|---------|----------|----------|-----------|----------|
| [Name]  | ___%     | [Count]  | [L/M/H]   | GO/HOLD/KILL |

### Gate 3 Reviews (Phase 3 → Phase 4)
[Similar table]

### Gate 4 Reviews (Phase 4 → Production)
[Similar table]

---

## 3. STRATEGIC DECISIONS (60 min)

### 3.1 Go/No-Go Decisions
- [ ] [Project Name]: GO / HOLD / KILL - Rationale: ___

### 3.2 Resource Reallocation
- [ ] Move ___ hrs from [Project A] to [Project B]
- [ ] Allocate $___ from reserve to [Project C]

### 3.3 Technology Investments
- [ ] [Technology]: MAKE / BUY / PARTNER - Budget: $___, Timeline: ___

### 3.4 Horizon Rebalancing
- [ ] Current: H1 ___%, H2 ___%, H3 ___%
- [ ] Target: H1 70%, H2 20%, H3 10%
- [ ] Actions: ___

---

## 4. NEXT QUARTER PRIORITIES (15 min)

1. ___
2. ___
3. ___

**Action Items:**
| Action | Owner | Due Date |
|--------|-------|----------|
| ___    | ___   | ___      |

**Next Review:** [Date]
```

---

### Template 2: Technology Platform Business Case

```markdown
# TECHNOLOGY PLATFORM BUSINESS CASE: [TECHNOLOGY NAME]

## EXECUTIVE SUMMARY
**Technology:** [Name]
**Projects Benefiting:** [Count] projects ([Names])
**Investment Required:** $[Amount]
**Decision Required By:** [Date]
**Recommendation:** MAKE / BUY / PARTNER

---

## 1. COMMONALITY ANALYSIS

### Projects Needing This Technology
| Project | Phase | Timeline | Standalone Cost | Critical? |
|---------|-------|----------|-----------------|-----------|
| [Name]  | [N]   | [Date]   | $[Amount]       | YES/NO    |

**Total Standalone Cost:** $[Amount]
**Total Demand:** [N] projects

---

## 2. OPTIONS ANALYSIS

### Option A: Standalone Development (Each Project)
- **Cost:** $[Amount] (sum of standalone costs)
- **Time:** [Duration] (sequential)
- **Risk:** [N] integration risks (independent failures)
- **Control:** Low (vendor-dependent)
- **Pros:** ___
- **Cons:** ___

### Option B: Common Platform Development (RECOMMENDED)
- **Cost:** $[Amount] (1× dev + N× integration)
- **Time:** [Duration] (parallel integration)
- **Risk:** 1 development risk (but reused N×)
- **Control:** High (local IP)
- **Pros:** ___
- **Cons:** ___

### Option C: Partner (University/Vendor)
- **Cost:** $[Amount]
- **Time:** [Duration]
- **Risk:** [Level]
- **Control:** Medium (shared IP)
- **Pros:** ___
- **Cons:** ___

---

## 3. DECISION CRITERIA

**Strategic Importance:** LOW / MEDIUM / HIGH
- Rationale: ___

**Time Sensitivity:** LOW / MEDIUM / HIGH
- First project needs by: [Date]

**Budget Available:** $[Amount]
- Source: [Portfolio reserve / Reallocate from / New funding]

**Risk Tolerance:** LOW / MEDIUM / HIGH
- Fallback plan: ___

---

## 4. RECOMMENDATION

✅ **SELECT: [Option]**

**Rationale:**
1. ___
2. ___
3. ___

**ROI Calculation:**
- Investment: $[Amount]
- Savings: $[Amount] ([%]% reduction vs standalone)
- Payback: [Duration]
- Strategic value: ___

---

## 5. IMPLEMENTATION PLAN

**Budget:** $[Amount] from [Source]
**Team:** [N] engineers ([Names/Roles])
**Timeline:** [Start] → [End] ([Duration])

**Milestones:**
- [ ] [Milestone 1]: [Date]
- [ ] [Milestone 2]: [Date]
- [ ] [Milestone 3]: [Date]

**First Customer:** [Project Name] (validates platform)
**Subsequent Customers:** [Projects] ([Dates])

---

## 6. RISKS & MITIGATIONS

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| ___  | L/M/H       | L/M/H  | ___        |

---

**Prepared By:** [Name], [Date]
**Approved By:** ________ (Portfolio Manager), [Date]
```

---

## 🎯 INTEGRATION WITH EXISTING SKILLS

### How Portfolio Strategy Connects to Other Skills

```
┌─────────────────────────────────────────────────────────────┐
│  PORTFOLIO STRATEGY (This Skill)                            │
│  ────────────────────────────────────────────────────────── │
│  • Multi-project resource allocation                        │
│  • Technology roadmapping                                   │
│  • Strategic prioritization                                 │
│  • Risk portfolio balancing                                 │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ├─► ODI (Phase 0)
                 │   Use: Portfolio-level customer segmentation
                 │   Output: Identify cross-project customer overlaps
                 │   Example: Navy as customer for 4 projects → bundle offering
                 │
                 ├─► Systems Thinking (Phase 1)
                 │   Use: Portfolio-level feedback loops
                 │   Output: Identify inter-project dependencies
                 │   Example: V-SMASH FCS reuse in RCWS-127-NAVAL Gen 2
                 │
                 ├─► Pahl & Beitz (Phases 1-4)
                 │   Use: Phase gate reviews across all projects
                 │   Output: Comparative gate decisions (approve/hold/kill)
                 │   Example: RCWS-127 (95% reqs) vs VN-RC-TX (75% reqs)
                 │
                 ├─► DfX Guidelines (Phase 3)
                 │   Use: Common DfX platforms (e.g., marine coatings)
                 │   Output: Reusable design guidelines across projects
                 │   Example: All naval projects use same corrosion strategy
                 │
                 └─► D-M-I-R Learning (Meta)
                     Use: Portfolio-level lessons learned
                     Output: Cross-project knowledge transfer
                     Example: RCWS-127 stabilization learnings → V-SMASH
```

---

### Portfolio-Enhanced Workflows

**Example 1: ODI at Portfolio Level**

Traditional ODI: Survey customers for 1 project
Portfolio ODI: Survey customers across ALL projects, identify:
- **Customer overlap:** Navy needs RCWS + Gunnery Trainer + Target Detection
- **Outcome overlap:** "Minimize maintenance downtime" appears in 8 projects
- **Bundling opportunity:** Sell integrated solution (RCWS + training + support)

**Example 2: Systems Thinking at Portfolio Level**

Traditional Systems: Analyze feedback loops within 1 project
Portfolio Systems: Analyze feedback loops ACROSS projects:
- **Technology pipeline:** RCWS-127 develops stabilization → V-SMASH reuses → Gen 2 products faster
- **Resource allocation loop:** Success breeds resources, failure breeds cuts (Success to Successful archetype)
- **Learning loop:** Each project adds to organizational capability → future projects easier

**Example 3: Phase Gates at Portfolio Level**

Traditional Gates: Approve/reject each project independently
Portfolio Gates: **Comparative gate reviews** (rank projects, allocate resources proportionally):
- Gate 1: 5 projects ready, but only 3 have sufficient priority → 2 held
- Gate 2: 1 project ready, resources available → approved
- Gate 3: 0 projects ready → no action

---

## 📖 FURTHER READING & RESOURCES

### Recommended Books

1. **"The Innovator's Dilemma"** - Clayton Christensen
   - Horizon 1/2/3 framework
   - Disruptive vs. sustaining innovation
   - When to invest in risky new technologies

2. **"Discovery-Driven Growth"** - Rita McGrath & Ian MacMillan
   - Portfolio approach to innovation
   - Managing uncertainty through staged investment
   - Relevant for Horizon 3 (future bets)

3. **"Portfolio Management for New Products"** - Robert Cooper et al.
   - Gate review processes
   - Risk balancing across portfolios
   - Resource allocation methods

4. **"Technology Roadmapping"** - Robert Phaal (Cambridge)
   - Technology evolution planning
   - Make vs. buy decisions
   - Platform strategies

### Internal Resources

- `SKILL_odi_innovation.md` - Customer-driven prioritization
- `SKILL_systems_thinking.md` - Feedback loops & leverage points
- `SKILL_conceptual_design.md` - VDI 2225 evaluation (adaptable to portfolio scoring)
- `PROJECT_INDEX.md` - Current portfolio status (update quarterly)

---

## 🔧 PRACTICAL USAGE GUIDE

### Quick Commands for Portfolio Management

| User Intent | Command | Action |
|-------------|---------|--------|
| **Portfolio overview** | "Portfolio status" | Display dashboard with all projects |
| **Prioritization** | "Prioritize projects Q2 2026" | Run prioritization matrix, output ranked list |
| **Resource allocation** | "Allocate resources for [project]" | Calculate optimal allocation using methods A/B/C |
| **Technology roadmap** | "Technology roadmap for [domain]" | Create roadmap showing evolution & reuse |
| **Gate review** | "Quarterly gate review [quarter]" | Prepare gate review package for all projects |
| **Platform decision** | "Should we develop [tech] platform?" | Run business case analysis (Template 2) |
| **Risk balance** | "Portfolio risk analysis" | Calculate risk portfolio, check balance |

---

## ⚠️ CRITICAL PORTFOLIO RULES

### Portfolio Management Principles

1. **70-20-10 Rule (Horizons):**
   - ALWAYS maintain 70% H1 (core), 20% H2 (growth), 10% H3 (future)
   - Violating this creates either stagnation (too much H1) or chaos (too much H3)

2. **Phase Distribution Rule:**
   - NO more than 30% of resources in Phase 1 simultaneously
   - Rationale: Phase 1 is discovery, too many = diluted focus, "analysis paralysis"

3. **Resource Bottleneck Rule:**
   - If >2 projects need the same scarce resource, develop PLATFORM
   - Rationale: Platform ROI > standalone development after N=2

4. **Kill Fast Rule:**
   - 3 consecutive gate failures → automatic portfolio review for kill decision
   - Rationale: Sunk cost fallacy kills portfolios (don't throw good money after bad)

5. **Technology Debt Rule:**
   - Strategic technologies (competitive advantage) → MAKE
   - Commodity technologies (no differentiation) → BUY
   - Uncertain technologies (research phase) → PARTNER (university)

6. **Risk Balance Rule:**
   - NO more than 10% budget in high-risk/high-uncertainty projects (Horizon 3)
   - Rationale: Portfolio needs predictable revenue stream, not lottery tickets

---

## 📝 D-M-I-R REFLECTION (Portfolio Strategy)

### Diagnosis
**What problem does portfolio strategy solve?**
- Without portfolio view: Projects compete destructively, no technology reuse, resource conflicts unresolved
- With portfolio view: Strategic resource allocation, technology platforms, risk balancing
- Real problem: Optimizing the **system of projects**, not individual projects

### Modeling
**How does a portfolio behave?**
- **Reinforcing loop:** Successful projects get more resources → more success (Success to Successful archetype)
- **Balancing loop:** Limited resources constrain portfolio growth
- **Leverage point:** Technology platforms (L10: Material flow structure) enable reuse, break resource constraint

### Intervention
**Where to intervene in a portfolio?**
- **L6 (Info flows):** Cross-project learning, quarterly reviews, dashboards
- **L10 (Flow structure):** Technology platforms, shared capabilities
- **L5 (Rules):** Gate criteria, resource allocation formulas, kill decisions

### Reflection
**What makes portfolio strategy effective?**
- Integration with project-level skills (ODI, Systems, P&B)
- Comparative decision-making (rank projects, allocate proportionally)
- Strategic technology investments (platforms > standalone)
- Risk balancing (70-20-10 Horizon rule)

---

**Status:** ✅ Skill Complete - Ready for Use

**Next Steps:**
1. Apply to current portfolio (14 projects)
2. Run Quarterly Portfolio Review (Q2 2026)
3. Create technology roadmap for stabilization domain
4. Decide on platform investments (stabilization, AI FCS)

---

*This skill integrates with the complete Engineering Design System to provide portfolio-level strategic decision-making for defense product development.*

*Related Skills:*
- [[SKILL_odi_innovation|ODI]] (customer priorities)
- [[SKILL_systems_thinking|Systems Thinking]] (feedback loops)
- [[SKILL_conceptual_design|P&B Conceptual Design]] (VDI 2225)
- [[SKILL_dmir_learning|D-M-I-R Learning]] (meta-cognition)
