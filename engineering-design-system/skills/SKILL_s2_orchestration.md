# 🔀 S2 — MULTI-AGENT ORCHESTRATION PATTERNS

## Reusable Pattern Library for IRONMESH Product Family

**Skill ID:** SKILL_s2_orchestration
**Commands:** `/orchestrate`, `/pattern`, `/agents`, `/edges`

---

## ⌨️ SLASH COMMANDS

| Command | Aliases | Purpose |
|---------|---------|---------|
| `/orchestrate <product>` | `/orch` | Design full orchestration for a product |
| `/pattern <type>` | `/pat` | Apply a specific pattern (pipeline / statemachine / workflow) |
| `/agents <product>` | `/roles` | Define master + sub-agent roster |
| `/edges <product>` | `/routing` | Design conditional edges (retry / reroute / escalate / halt) |

---

## 🏗️ FOUNDATION: MASTER-CLONE FRAMEWORK

All 3 patterns share this foundation. Violating it is an anti-pattern.

```
WRONG: Rigid N-agent pipeline with pre-defined routing
RIGHT: Master Agent holds state, issues Task() calls dynamically,
       routes based on CURRENT results (not pre-planned sequence)

Sub-agents are STATELESS → receive task, return structured result
Master is ALWAYS the router → it has full context, sub-agents have none
Custom sub-agents with forced routing = ANTI-PATTERN
```

### Three Invariant Rules

1. **Consequence drives automation %** — consequence ↑ → automation ↓ → HITL required
2. **Fallbacks are first-class** — defined BEFORE implementation. No fallback = no automation.
3. **Gates are never automated** — accountability transfer moments are always 0% automated

---

## 📊 PATTERN SELECTION RULE

```
Is the process sequential, order-dependent, hours-to-days?
  → Pattern 1: LINEAR PIPELINE

Is the process cyclic, real-time, sensor-driven?
  → Pattern 2: STATE MACHINE

Is the process multi-project, multi-framework, with a learning loop?
  → Pattern 3: WORKFLOW ORCHESTRATION

Does the process coordinate parallel pipelines with shared resources?
  → Pattern 4: PARALLEL PIPELINE
```

---

## PATTERN 1: LINEAR PIPELINE

**Archetype:** VN-RANGE-001 Deployment
**Source:** `projects/IRONMESH/IRONMESH_Orchestration_Design_v1.0.md`

### When to Use

- Multi-step process that must complete in order
- Each phase produces deliverables that feed the next
- Human must sign off at gates between phases
- Time scale: hours to days per step

### Architecture

```
Master (Deployment Orchestrator)
  ├── A-SURVEY  — data collection (site survey, verification)
  ├── A-DOC     — document generation (BOM, contracts, reports)
  ├── A-CONFIG  — system configuration (equipment, software)
  ├── A-TEST    — automated testing (FAT, integration, calibration)
  ├── A-DEPLOY  — software deployment (fixed playbook, rollback)
  ├── A-TRAIN   — training delivery (content, dashboards)
  └── A-REPORT  — validation reporting (from test data)
```

### Key Properties

| Property | Value |
|----------|-------|
| Sub-agents | 5–8 (administrative / domain-scoped) |
| State | Session-bound (Master holds in memory) |
| HITL checkpoints | 10–15 (document review + physical verify + gates) |
| HITL time budget | 15–45 min per checkpoint |
| Retry logic | 2 retries → escalate to human |
| Reroute logic | Jump to root-cause step, not symptom step |
| Fallback | Escalate to KN (human available, not time-critical) |
| Gate design | Both parties sign, ≥24h between re-presentations |

### HITL Types (Pipeline)

| Type | Code | When | Information | Time |
|------|------|------|-------------|------|
| Review & Approve | R | After doc generation | ≤4 items, one question | 15–20 min |
| Physical Verify | P | On-site checks | Checklist + tolerance | 20–60 min |
| Expert Judgment | E | Calibration, testing | Data + physical ground truth | 30–45 min |
| Gate | G | Phase boundary | All prior results + risk | 30–45 min, both parties sign |

### Conditional Edge Template

```yaml
retry:   { max: 2, action: "re-issue Task() with corrected params", after_max: "escalate" }
reroute: { trigger: "gate rejected", target: "step where root cause lives" }
escalate: { after: "MAX_RETRY or safety violation", to: "KN" }
halt:     { trigger: "CRITICAL flag or safety", clearance: "KN only" }
```

---

## PATTERN 2: STATE MACHINE

**Archetype:** V-SMASH-LITE Engagement Controller
**Source:** `projects/V-SMASH-LITE/V-SMASH-LITE_Orchestration_Design_v1.0.md`

### When to Use

- Real-time cyclic process with operator in the loop
- Sensor-driven state transitions (not document-driven)
- Engagement window measured in seconds, not hours
- Human is the ACTOR (holds trigger), not the REVIEWER (reads document)

### Architecture

```
Master (Engagement Controller — state machine)
  ├── A-DETECT  — detection (<100ms, scanning)
  ├── A-TRACK   — tracking (<50ms, position + velocity)
  ├── A-IFF     — classification (<200ms, HOSTILE/NEUTRAL/UNKNOWN)
  ├── A-FC      — fire control (<50ms, solution quality + window)
  └── A-LOG     — data capture (background, continuous)
```

### State Diagram

```
STANDBY ──detect──→ ALERT ──IFF hostile──→ LOCKED ──trigger held──→ READY
   ↑                  ↑←──track lost──┘       ↑←──trigger released──┘  │
   │                  │                        │                        │
   │                  ├──IFF unknown──→ AMBER ──operator confirms──→ LOCKED
   │                  │                 │                               │
   │                  │                 └──operator lowers──→ ALERT     │
   │                  │                                                 │
   └──concluded──── CONCLUDED ←──threat gone── ASSESSING ←──shot── ENGAGED
                                                  │                    ↑
                                                  └──re-engage──→ LOCKED
```

### Key Properties

| Property | Value |
|----------|-------|
| Sub-agents | 4–6 (real-time inference, latency-bounded) |
| State | Ephemeral per engagement cycle |
| HITL checkpoints | 2–4 (one-glance signals, not documents) |
| HITL time budget | 1–5 seconds |
| Retry logic | NONE — no time for retry in real-time |
| Fallback | Instant → manual mode (operator takes over) |
| Safety override | IFF GREEN blocks gate (no override, ever) |

### HITL Types (State Machine)

| Type | When | Signal | Time |
|------|------|--------|------|
| IFF Confirm | ALERT → LOCKED | Reticle color (RED/AMBER/GREEN) | 1–3 sec |
| Fire Execute | READY → ENGAGED | Reticle pulse (window open) | 0–500ms |
| Conclude/Re-engage | ASSESSING | Hit/miss indicator + drone status | 2–5 sec |

**Critical rule:** Every HITL signal readable in ONE GLANCE under combat stress. Color + shape only. No sentences. No numbers except range.

### ACH Principle (AI-Compensates-Hardware)

```
Operator decides WHAT (intent: engage or not)
AI decides WHEN (precision: optimal fire moment within window)

Operator holds trigger = intention signal
AI gates the moment = quality > threshold AND window open AND trigger held
Three conditions, ALL must be true → shot released

Operator can ALWAYS abort by releasing trigger
AI can NEVER fire without operator holding trigger
```

### Safety Boundaries (Absolute — No Override)

```
IFF GREEN (friendly/civilian) → gate NEVER opens, regardless of trigger
Safe zone boundary exceeded   → gate NEVER opens, regardless of quality
Both enforced by Master — no sub-agent can override
```

---

## PATTERN 3: WORKFLOW ORCHESTRATION

**Archetype:** D-M-I-R × ODI × Engineering Design Framework
**Source:** `projects/IRONMESH/IRONMESH_Framework_Orchestration_Design_v1.1.md`

### When to Use

- Multiple projects at different phases simultaneously
- Multiple frameworks that must coordinate (ODI → Requirements → Design)
- Resource constraint (fixed hours/week) requires allocation decisions
- Learning loop: system reconfigures itself weekly based on reflection

### Architecture

```
Master (Design Orchestrator — reads state from files at session open)
  │
  ├── FRAMEWORK AGENTS (phase-sequenced per project)
  │   ├── A-ODI      — Phase 0a: /odi /jobs /outcomes /opp /seg
  │   ├── A-REQ      — Phase 1:  /req /validate /mil /stake
  │   ├── A-CONCEPT  — Phase 2:  /abs /fn /morpho /eval /vs
  │   ├── A-EMBODY   — Phase 3:  /layout /dfx /mat /tol /lc
  │   └── A-DETAIL   — Phase 4:  /bom /verify /cost
  │
  └── CROSS-CUTTING AGENTS (always-on infrastructure)
      ├── A-QC        — after EVERY output, no exceptions
      ├── A-DMIR      — weekly Friday, mandatory
      ├── A-PORTFOLIO  — gates every routing decision
      ├── A-SYSTEMS   — triggered on persistent constraints (≥2 weeks)
      └── A-SKILL     — tracks hours per skill vs budget
```

### Key Properties

| Property | Value |
|----------|-------|
| Sub-agents | 8–12 (5 framework + 3–5 cross-cutting) |
| State | **Externalized to files** (not session memory) |
| Session opening | Mandatory 5-file read protocol before any routing |
| HITL types | 3 distinct (gate review, strategic judgment, QC review) |
| Retry logic | N/A — rework at phase level, not step level |
| Fallback | Pause project, protect buffer, reroute capacity |
| Learning loop | D-M-I-R weekly → Master reconfigures allocation |

### Session-Opening Protocol (MANDATORY)

```
1. Read progress.md          → project phases + status
2. Read dmir_log.md (last 4) → current constraint
3. Read allocation_tracker   → budget remaining
4. Read freeze_order         → what's frozen
5. Read qc_gate calibration  → QC state
Only AFTER all 5 → Master has valid state → proceed with work
```

### Framework Dependency Enforcement

```
ODI report MUST exist before Phase 1 starts
Phase 1 gate MUST pass before Phase 2 starts
Phase 2 gate MUST pass before Phase 3 starts
...
Frozen project → BLOCK all routing (no "quick fix" exception)
Skill over-budget → BLOCK routing until next week or buffer approved
```

### HITL Types (Workflow)

| Type | When | Time | Decision Format |
|------|------|------|-----------------|
| Gate Review | Phase boundary | 30–60 min | A (approve) / B (revise) / C (pause) / D (cancel) |
| Strategic Judgment | Weekly Friday | 60 min | Name constraint → approve allocation delta |
| Quality Review | After QC flags | 2h/week batched | ACCEPT / REJECT per flag |

### D-M-I-R Feedback Loop

```
Week N work → A-QC gates → deliverables produced
                                    ↓
Friday: A-DMIR runs → {constraint, cause, intervention, allocation_delta}
                                    ↓
Master consumes → reconfigures routing for Week N+1
                                    ↓
If same constraint ≥2 weeks → trigger A-SYSTEMS archetype analysis
                                    ↓
Archetype feeds back into D-M-I-R model section
                                    ↓
Week N+1: routing changes, allocation changes, constraint addressed
```

---

## PATTERN 4: PARALLEL PIPELINE

**Archetype:** VN-12.7MM-SIM Product Family Coordination
**Source:** `projects/VN-12.7MM-SIM/VN-12.7MM-SIM_Family_Orchestration_Design_v1.0.md`

### When to Use

- Multiple products progressing through design phases in parallel
- Shared resources (developer, fab shop, engineering time) create conflicts
- Cross-product dependencies (one product must reach a milestone before another can start)
- Different timelines require scheduling decisions
- Common software/component base propagates changes across products

### Architecture

```
Master (Product Family Coordinator — meta-pattern)
  │
  ├── COORDINATION AGENTS (Pattern 4 layer)
  │   ├── A-SCHEDULE  — resource allocation, conflict detection, 25h cap enforcement
  │   ├── A-DEPEND    — dependency resolution, cross-product gate verification
  │   ├── A-SYNC      — shared artifact propagation, version tracking
  │   └── A-TRACK     — progress dashboard, family timeline, slip detection
  │
  └── PER-PRODUCT PATTERN 3 INSTANCES
      ├── Product A → [P0]→[P1]→[P2]→[P3]→[P4]  (independent)
      ├── Product B → [P0]→[P1]→[P2]→[P3]→[P4]  (independent)
      ├── Product C → [BLOCKED]→→→[P1]→...        (depends on A.Phase3)
      └── Product D → [BLOCKED]→→→→→[P1]→...      (depends on A + external)
```

### Key Properties

| Property | Value |
|----------|-------|
| Sub-agents | 4 coordination + 6 shared per-product (10 total unique) |
| State | **Externalized + cross-product** (family_state.md, dependency_map.md) |
| HITL types | 6 (SR, CA, DG, WR, AP, FM) — two-layer system |
| HITL time budget | ~65 min/week (coordination layer) + per-product Pattern 3 |
| Primary edge | Escalate → Halt (coordination errors are structural) |
| Fallback | Escalate to human for all priority/dependency decisions |
| Gate design | Dependency Gates (DG) — cross-product, 0% automated, evidence-based |
| Learning | D-M-I-R weekly + family rebalancing |

### HITL Types (Parallel Pipeline)

| Type | Code | When | Time |
|------|------|------|------|
| Session Routing | SR | Every session open | 5–10 min |
| Conflict Arbitration | CA | Resource conflict detected | 5–15 min |
| Dependency Gate | DG | Dependent product advances | 15–30 min |
| Weekly Rebalance | WR | Friday close | 15–20 min |
| Artifact Propagation | AP | Shared artifact changed | 10–20 min |
| Family Milestone | FM | Major milestone / quarterly | 30–60 min |

### Three Halt Conditions (Absolute)

```
HALT-1: Dependency file missing or corrupt → no product advances
HALT-2: Safety-critical shared parameter changed → all downstream frozen
HALT-3: Dependency product regressed → dependent product immediately paused
```

### What Makes Pattern 4 Distinct

Pattern 4 is a **meta-pattern** — it coordinates multiple Pattern 3 instances, not individual process steps. The key innovations:

1. **Dependency gates (DG)** — cross-product gates with evidence checklists
2. **Shared resource arbitration** — explicit conflict detection with standing priority + human override
3. **Artifact propagation control** — prevents silent SW divergence across products
4. **Two-layer HITL** — coordination checkpoints + per-product checkpoints
5. **Escalate-not-retry** — coordination errors are structural, not transient

---

## 📋 CROSS-PATTERN COMPARISON

| Aspect | Pipeline | State Machine | Workflow | **Parallel Pipeline** |
|--------|----------|---------------|----------|-----------------------|
| Time scale | Hours–days | Milliseconds–seconds | Weeks–months | **Months–years** |
| Structure | A → B → C | States ⇄ States | Dependency graph + loop | **Parallel graphs + shared resources** |
| Agents | 5–8 admin | 4–6 inference | 8–12 framework + cross-cut | **4 coordination + N×Pattern 3** |
| State | Session memory | Ephemeral per cycle | Externalized to files | **Externalized + cross-product** |
| HITL count | 10–15 | 2–4 | 3 types (varying frequency) | **6 types (2-layer)** |
| HITL info density | High (documents) | Low (one-glance signals) | Medium (checklists + reflection) | **Medium (dashboards + tradeoffs)** |
| HITL time | 15–45 min | 1–5 sec | 30–90 min | **5–30 min (coordination) + inherited** |
| Fallback | Retry 2× → escalate | Instant → manual mode | Pause → protect buffer → reroute | **Escalate → Halt** |
| Automation ceiling | 85% (admin) | 60% (inference) | 40% (frameworks) | **50% (coordination) + inherited** |
| Safety-critical | 0% (gates) | 0% (IFF GREEN) | 0% (all gates) | **0% (cross-product gates)** |
| Learning | Post-deployment review | Real-time adjustment | D-M-I-R weekly + archetype | **D-M-I-R + family rebalancing** |

---

## 🔧 REUSABLE YAML TEMPLATES

### Template: Task() Delegation

```yaml
task_delegation:
  format: "Master → Task(A-AGENT, 'action description')"
  agent_scope: "single domain only"
  output: "structured result — no free-form narrative"
  retry_limit: 2  # (0 for state machine — no time)
  escalation: "after MAX_RETRY or safety violation"
```

### Template: HITL Checkpoint

```yaml
hitl_checkpoint:
  id: "{{STEP}}-H"
  type: "R | P | E | G"  # Review / Physical / Expert / Gate
  authority: "{{role}}"
  time_budget: "{{minutes}}"
  information_package:
    max_items: 4
    format: "summary → anomalies → one clear question"
    never: "raw data dumps, ambiguous questions"
  decision_format: "{{structured options}}"
  master_behavior: "present → wait indefinitely → never auto-approve"
```

### Template: Conditional Edge

```yaml
conditional_edge:
  retry:    { max: 2, action: "re-issue with correction", after_max: "escalate" }
  reroute:  { trigger: "gate rejected [reason]", target: "root-cause step" }
  escalate: { trigger: "MAX_RETRY or CRITICAL", to: "human", wait: "indefinite" }
  halt:     { trigger: "safety violation", clearance: "KN only", never: "auto-resume" }
```

### Template: Consequence Map Row

```yaml
consequence_map_row:
  step: "{{step_name}}"
  what_AI_could_get_wrong: "{{failure mode}}"
  consequence: "{{impact description}}"
  severity: "CRITICAL | HIGH | MEDIUM | LOW"
  automation_pct: "{{0–100}}%"  # lower for higher severity
  hitl_required: "{{yes/no}}"
  fallback: "{{what happens if AI fails}}"
```

---

## 🎯 `/orchestrate` WORKFLOW

When invoked, follow this 5-step sequence:

### Step 1: Consequence Map
For each step in the process, ask: **"What fails if AI gets this wrong?"**

```
Step → Failure Mode → Consequence → Severity → Automation %
```

Rule: Consequence ↑ → Automation ↓. Start here, NOT with agent design.

### Step 2: Agent Roster
Assign one agent per domain. Define scope boundary.

```
Agent → Domain → Steps involved → Scope boundary → What it CANNOT do
```

Rule: Agents are stateless. Master holds all state. Agent scope = one domain.

### Step 3: Conditional Edges
For every automated step, define: retry / reroute / escalate / halt.

```
Trigger → Edge type → Action → After max attempts
```

Rule: If no fallback defined → step is NOT automated.

### Step 4: HITL Architecture
Place checkpoints where accountability transfers.

```
Checkpoint → Type → Authority → Information package → Decision format
```

Rule: Match HITL to time scale. Pipeline = documents. State machine = signals. Workflow = reflection. Parallel pipeline = dashboards + tradeoffs.

### Step 5: Pattern Documentation
Produce the orchestration design document with:
- Section 0: Procurement narrative (if defense)
- Section 1: Design principles (3 max)
- Section 2: Agent architecture (roster + scope)
- Section 3: Process graph (Task() delegation for all steps)
- Section 4: Conditional edges (retry/reroute/escalate/halt table)
- Section 5: HITL checkpoint register
- Section 6: Loop prevention rules
- Section 7: Reusable YAML template
- Section 8: Pattern library reference (which pattern, what was adapted)
- Section 9: Metrics (agents, checkpoints, automation %, human time)

---

## 📚 SOURCE DOCUMENTS

| Pattern | Document | Lines | Key Innovation |
|---------|----------|-------|---------------|
| Pipeline | `projects/IRONMESH/IRONMESH_Orchestration_Design_v1.0.md` | 409 | Consequence gradient + 14 HITL + reusable template |
| State Machine | `projects/V-SMASH-LITE/V-SMASH-LITE_Orchestration_Design_v1.0.md` | 497 | ACH principle + one-glance HITL + IFF safety boundaries |
| Workflow | `projects/IRONMESH/IRONMESH_Framework_Orchestration_Design_v1.1.md` | 759 | D-M-I-R feedback loop + externalized state + 3 HITL types |
| **Parallel Pipeline** | `projects/VN-12.7MM-SIM/VN-12.7MM-SIM_Family_Orchestration_Design_v1.0.md` | ~450 | **Meta-pattern + dependency gates + shared resource arbitration + 2-layer HITL** |

---

## CAPTURE PROTOCOL

```
Skill:     S2 — Multi-Agent Orchestration
Version:   2.0
Patterns:  4 documented (Pipeline / State Machine / Workflow / Parallel Pipeline)
Source:    4 project-specific orchestration designs
Evidence:  Same master-clone framework → 4 architecturally distinct designs
           depending on time scale, process structure, resource sharing, and human role
New:       Pattern 4 (Parallel Pipeline) is a META-PATTERN that coordinates
           multiple Pattern 3 instances with shared resources and dependency gates.
           Key innovations: DG gates, A-SYNC propagation, escalate-not-retry edges.
```
