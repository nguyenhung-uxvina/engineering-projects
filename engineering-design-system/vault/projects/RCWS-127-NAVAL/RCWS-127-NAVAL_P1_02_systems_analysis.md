---
project: RCWS-127-NAVAL
phase: 1
type: systems_analysis
version: 1.0
created: 2026-02-03
updated: 2026-02-03
status: active
---

# RCWS-127-NAVAL: SYSTEMS THINKING ANALYSIS
## Feedback Loops, Leverage Points, and System Dynamics

**Purpose:** Apply systems thinking to identify feedback loops, leverage points, and system dynamics that will inform design decisions for the Naval RCWS.

**Integration:** This analysis complements the ODI analysis and requirements list, providing deeper insight into system behavior and high-leverage intervention points.

---

## 1. SYSTEM BOUNDARY DEFINITION

### 1.1 System Scope

**System Name:** Naval RCWS Combat Engagement System

**Boundary:**
- **INSIDE:** RCWS hardware, operator, ship platform, fire control integration, maintenance crew, training
- **OUTSIDE:** Threat environment (external), ship navigation systems (input only), higher-level command (external), ammunition supply chain

**Time Horizon:**
- Operational: Minutes to hours (single engagement)
- Strategic: 10 years (system lifecycle)

### 1.2 Key Variables

**Stock Variables** (accumulate over time):
- Operator skill level
- System reliability (degradation over time)
- Maintenance backlog
- Fleet combat readiness
- Operational data/lessons learned

**Flow Variables** (rates of change):
- Training rate (operators/month)
- Failure rate (MTBF)
- Repair rate (MTTR)
- Skill decay rate (if not practiced)
- Ammunition consumption rate

**External Variables:**
- Threat intensity (South China Sea tensions)
- Budget availability
- Technology advancement (sensors, stabilization)
- Environmental severity (corrosion, sea state)

---

## 2. CAUSAL LOOP DIAGRAMS (CLDs)

### 2.1 CLD #1: Accuracy Performance Loop

```
                    ┌──────────────────────────────────────┐
                    │                                      │
                    │         R1: VIRTUOUS CYCLE           │
                    │         (Reinforcing Loop)           │
                    │                                      │
    ┌───────────────▼────────────┐              ┌─────────┴──────────┐
    │  Ship Motion               │              │  First-Round        │
    │  Compensation              │              │  Hit Probability    │
    │  Quality                   │              │                     │
    └────────────┬───────────────┘              └──────────┬──────────┘
                 │                                         │
                 │ (+)                                (+)  │
                 │                                         │
    ┌────────────▼───────────────┐              ┌─────────▼──────────┐
    │  Operator                  │              │  Operator           │
    │  Confidence                │◄─────(+)─────┤  Training           │
    │  in System                 │              │  Effectiveness      │
    └────────────┬───────────────┘              └──────────┬──────────┘
                 │                                         │
                 │ (+)                                (+)  │
                 │                                         │
    ┌────────────▼───────────────┐              ┌─────────▼──────────┐
    │  Usage Rate                │──────(+)────►│  Data Collection   │
    │  (Engagements/Month)       │              │  & Learning        │
    └────────────────────────────┘              └────────────────────┘

LOOP TYPE: Reinforcing (R1)
DIRECTION: Virtuous cycle if started positively

BEHAVIOR:
- Better stabilization → Higher hit rate → Operator confidence increases
- Higher confidence → More engagement practice → More training data
- More data → Better understanding of system → Improved operator skill
- Improved skill → Better use of stabilization features → Even higher hit rate

LEVERAGE POINT: L6 (Information Flows)
- Implementing real-time feedback on hit/miss immediately after engagement
- This accelerates the learning loop dramatically
```

---

### 2.2 CLD #2: Maintenance Reliability Loop

```
                    ┌──────────────────────────────────────┐
                    │                                      │
                    │         B1: BALANCING LOOP           │
                    │    (Maintenance Stabilizing)         │
                    │                                      │
    ┌───────────────▼────────────┐              ┌─────────┴──────────┐
    │  System                    │              │  Failure            │
    │  Failures                  │◄─────(+)─────┤  Rate               │
    │  (Accumulated)             │              │  (per month)        │
    └────────────┬───────────────┘              └──────────┬──────────┘
                 │                                         │
                 │ (+)                                (−)  │
                 │                                         │
    ┌────────────▼───────────────┐              ┌─────────▼──────────┐
    │  Maintenance               │              │  System             │
    │  Workload                  │              │  Reliability        │
    │                            │              │  (MTBF)             │
    └────────────┬───────────────┘              └────────────────────┘
                 │                                         ▲
                 │ (+)                                     │
                 │                                    (−)  │
    ┌────────────▼───────────────┐                        │
    │  Repair                    │────────────────────────┘
    │  Actions                   │
    │  (Corrective)              │
    └────────────┬───────────────┘
                 │
                 │ (−)
                 │
    ┌────────────▼───────────────┐
    │  Maintenance               │
    │  Backlog                   │
    │  (Hours)                   │
    └────────────────────────────┘

LOOP TYPE: Balancing (B1)
BEHAVIOR:
- System failures accumulate → Maintenance workload increases
- More repair actions taken → Backlog reduced
- Lower backlog → Better system reliability
- Higher reliability → Fewer failures

DELAY: Critical 2-4 week delay between failure and parts availability
(This delay can cause oscillation if not managed)

LEVERAGE POINT: L9 (Delays)
- Reducing spare parts procurement delay from 4 weeks to 1 week
- Shifts system from oscillating to stable
- Recommendation: Pre-position critical spares at naval bases
```

---

### 2.3 CLD #3: Corrosion vs. Maintenance Trade-off

```
                    ┌──────────────────────────────────────┐
                    │                                      │
                    │         R2: VICIOUS CYCLE            │
                    │    (Corrosion Reinforcing)           │
                    │                                      │
    ┌───────────────▼────────────┐              ┌─────────┴──────────┐
    │  Corrosion                 │              │  Maintenance        │
    │  Damage                    │──────(+)────►│  Cost               │
    │  (Accumulated)             │              │  (Per Year)         │
    └────────────┬───────────────┘              └──────────┬──────────┘
                 ▲                                         │
                 │                                         │
                 │ (+)                                (−)  │
                 │                                         │
    ┌────────────┴───────────────┐              ┌─────────▼──────────┐
    │  Salt Exposure             │              │  Budget for         │
    │  Time                      │              │  Preventive         │
    │  (Hours at Sea)            │              │  Maintenance        │
    └────────────────────────────┘              └──────────┬──────────┘
                                                           │
                                                           │ (−)
                                                           │
                                               ┌───────────▼──────────┐
                                               │  Corrosion           │
                                               │  Protection          │
                                               │  Quality             │
                                               └──────────────────────┘

LOOP TYPE: Reinforcing (R2) - Vicious if not interrupted
BEHAVIOR:
- Salt exposure → Corrosion accumulates
- Corrosion → Higher maintenance costs
- Higher costs → Less budget for prevention
- Less prevention → More corrosion vulnerability

INTERVENTION POINT: L4 (Self-Organization)
- Design system to be "self-protecting" via material selection
- Marine-grade aluminum 5083 + proper coatings
- Eliminates dependency on maintenance budget for basic protection

DESIGN IMPLICATION:
- CRITICAL: Get corrosion resistance right in Phase 3 (Embodiment Design)
- Cannot rely on maintenance to compensate for poor material selection
- This is a L4 intervention (changing system structure)
```

---

### 2.4 CLD #4: Training vs. Automation Trade-off

```
    ┌──────────────────────┐              ┌──────────────────────┐
    │  Automation          │              │  Operator            │
    │  Level               │──────(−)────►│  Skill Required      │
    │  (AI, FCS)           │              │  (Training Hours)    │
    └──────────┬───────────┘              └──────────┬───────────┘
               │                                     │
               │ (+)                            (−)  │
               │                                     │
    ┌──────────▼───────────┐              ┌─────────▼───────────┐
    │  System Cost         │              │  Training Cost       │
    │  (Development +      │              │  (Per Operator)      │
    │   Production)        │              │                      │
    └──────────────────────┘              └─────────────────────┘
               │                                     │
               │                                     │
               └──────────────┬──────────────────────┘
                              │
                              │ (+)
                              │
                   ┌──────────▼───────────┐
                   │  Total Lifecycle     │
                   │  Cost                │
                   │  (TCO)               │
                   └──────────────────────┘

TRADE-OFF ANALYSIS:
Option A: High Automation (AI fire control, auto-tracking)
- Development cost: HIGH ($$$)
- Training cost: LOW ($)
- Operator dependency: LOW (good for conscript navy)
- Technology risk: HIGH (AI maturity for defense?)

Option B: Medium Automation (Stabilization + operator skill)
- Development cost: MEDIUM ($$)
- Training cost: MEDIUM ($$)
- Operator dependency: MEDIUM
- Technology risk: LOW (proven stabilization tech)

Option C: Low Automation (Manual + training)
- Development cost: LOW ($)
- Training cost: HIGH ($$$)
- Operator dependency: HIGH (skill degradation risk)
- Technology risk: NONE

RECOMMENDATION: Option B (Medium Automation)
RATIONALE:
- Balances cost with performance
- Vietnamese Navy has competent gunners (not conscripts)
- Stabilization tech proven and available (Korea, China)
- Avoids AI development risk (budget/schedule constraints)

LEVERAGE POINT: L5 (Rules of the System)
- Decision: Where to draw the automation boundary?
- This is a rules decision that cascades through entire system
```

---

## 3. SYSTEM ARCHETYPES IDENTIFIED

### 3.1 Archetype: "Fixes That Fail" (Corrosion Management)

**Pattern:**
```
Quick Fix                         Unintended
(Frequent Repainting)            Consequence
        │                              │
        │ (+)                     (−)  │
        ▼                              ▼
    ┌────────────┐   Delay    ┌────────────┐
    │  Problem   │◄───────────│  Deeper    │
    │  Symptom   │            │  Problem   │
    │ (Visible   │            │ (Substrate │
    │  Rust)     │            │  Corrosion)│
    └────────────┘            └────────────┘
         ▲                          │
         │                          │
         └──────────(+)─────────────┘
            Problem Returns
```

**Situation:**
- Quick fix: Sand and repaint corroded areas
- Problem symptom: Visible rust temporarily disappears
- Deeper problem: Substrate corrosion continues underneath
- Delay: 6-12 months before rust reappears
- Unintended consequence: Each repaint adds weight, hides structural damage

**Escape Strategy:**
- Fundamental solution: Proper marinization in Phase 3 (L4 intervention)
- Design out the corrosion problem via material selection
- Marine-grade aluminum 5083 (not steel)
- Proper drainage design (no water pooling)
- Galvanic isolation (no dissimilar metal contact)

---

### 3.2 Archetype: "Success to the Successful" (Accuracy vs. Speed Trade-off)

**Pattern:**
```
    Resources → Accuracy Features → Success → More Resources
         ↓                                          ↑
         │                                          │
         └────────────────(−)───────────────────────┘
                           │
                           ▼
                    Speed Features
                    (Starved)
```

**Situation:**
- Early design success with stabilization (accuracy) attracts attention/resources
- Speed features (rapid target switching, slew rate) get less focus
- BUT: ODI shows OUT-22 "Minimize engagement time" is Opp 13.5 (HIGH priority)
- Risk: Over-optimize accuracy at expense of speed

**Escape Strategy:**
- Use ODI opportunity scores to balance resource allocation
- OUT-25 (Motion comp): 14.9 → Allocate 35% resources
- OUT-21 (Accuracy): 14.2 → Allocate 30% resources
- OUT-22 (Speed): 13.5 → Allocate 25% resources (don't neglect!)
- Remaining 10% for other outcomes

**Leverage Point:** L3 (Goals of the System)
- Explicitly define success as "balanced scorecard" (not single metric)
- Prevents resource starvation of important-but-not-flashy features

---

### 3.3 Archetype: "Shifting the Burden" (Automation vs. Training)

**Pattern:**
```
                Problem
           (Engagement Quality)
                 ▲    ▲
                 │    │
       ┌─────────┘    └──────────┐
       │                         │
  Quick Fix               Fundamental
  (Add Automation)        (Training)
       │                         │
       │ (+)                (+)  │
       │                         │
       ▼                         ▼
  Side Effect:            Effort
  Skill Atrophy           Required
       │                         │
       │ (−)                (−)  │
       └─────────────────────────┘
```

**Situation:**
- Problem: Operators struggle with ship motion compensation
- Quick fix: Add more automation (auto-tracking, AI)
- Fundamental solution: Train operators in manual compensation techniques
- Side effect: Operators become dependent on automation
- When automation fails (combat damage, EMI), no fallback capability

**Escape Strategy:**
- Design for "graduated automation" (L10: Material Flow Structure)
- Mode 1: Full auto (AI tracking + stabilization)
- Mode 2: Semi-auto (Stabilization only, manual tracking)
- Mode 3: Manual (Backup mode, stabilization failed)
- Operators trained on Mode 2 & 3, default to Mode 1

**Leverage Point:** L10 (Structure of Material Flows)
- Build system architecture that REQUIRES operator skill at multiple levels
- Prevents complete dependency on automation

---

## 4. LEVERAGE POINTS ANALYSIS

### 4.1 L12-L9: Low Leverage (Numerical Adjustments)

**L12: Constants, Parameters**
- Examples: Slew rate (60°/s → 80°/s), weight limit (200kg → 180kg)
- Impact: Marginal improvement, doesn't change system behavior
- Recommendation: Optimize these LAST, after structure is set

**L11: Buffer Sizes**
- Examples: Ammunition capacity (100 rds → 200 rds), power reserve
- Impact: Reduces oscillation, adds resilience
- Recommendation: Size buffers for 2× average demand (safety margin)

**L10: Material Flow Structure**
- Examples: Modular architecture (base + upgrade kits), ammunition feed path
- Impact: Medium - enables flexibility and maintenance
- Recommendation: ✅ APPLY in Phase 3 - design for modularity

**L9: Delays**
- Examples: Spare parts delivery (4 weeks → 1 week), sensor lag (100ms → 20ms)
- Impact: Critical for stability - reduces oscillation
- Recommendation: ✅ CRITICAL - minimize sensor/control delays (R204, R205)

---

### 4.2 L8-L6: MEDIUM-HIGH LEVERAGE (Feedback Loops)

**L8: Negative Feedback Loops (Self-Correcting)**
- Examples: Stabilization feedback (gyro → actuator → weapon pointing)
- Current design: 2-axis gyro with 10 Hz bandwidth (R205)
- Impact: High - determines tracking accuracy
- Recommendation: ✅ HIGH PRIORITY - this is the core function

**L7: Positive Feedback Loops (Self-Amplifying)**
- Examples: Corrosion → Maintenance cost → Budget cuts → More corrosion (CLD #3)
- Intervention: INTERRUPT this loop via L4 (material selection)
- Recommendation: ✅ CRITICAL - design breaks vicious cycle

**L6: Information Flows** ⭐ HIGHEST IMPACT FOR THIS PROJECT
- Examples:
  1. **Real-time hit/miss feedback** (accelerates CLD #1 learning loop)
  2. **Ship motion data feed** (from navigation system to FCS)
  3. **Engagement data recording** (for after-action review)
- Impact: Very High - information enables rapid learning
- Recommendation: ✅ HIGHEST PRIORITY
  - Add requirement: Real-time impact assessment (camera + AI detection)
  - Add requirement: CAN bus integration with ship IMU/GPS
  - Add requirement: Engagement data logger (1000 engagements storage)

**New Requirements Generated:**
- **R-NEW-01:** System shall provide real-time hit/miss indication within 2 seconds (D)
- **R-NEW-02:** System shall record engagement data for post-mission analysis (W)
- **R-NEW-03:** System shall integrate with ship IMU for predictive stabilization (W)

---

### 4.3 L5-L1: HIGHEST LEVERAGE (System Structure & Paradigms)

**L5: Rules of the System**
- Example: "Where to draw automation boundary?" (CLD #4)
- Decision: Semi-automation (stabilization + manual tracking) NOT full AI
- Impact: Defines entire system architecture
- Recommendation: ✅ DECIDED - validate with stakeholders

**L4: Self-Organization**
- Example: Design system to be "self-protecting" via material selection
- Instead of relying on maintenance (external input), material resists corrosion
- Impact: Breaks CLD #3 vicious cycle at the source
- Recommendation: ✅ APPLY in Phase 3 - marine-grade materials (R501-R506)

**L3: Goals of the System**
- Current goal: "Accurate fire from moving platform"
- Proposed addition: "... while maintaining operator skill"
- Impact: Prevents "Shifting the Burden" to automation (Archetype 3.3)
- Recommendation: ✅ UPDATE mission statement in project brief

**L2: Paradigm (Mental Model)**
- OLD paradigm: "RCWS is a weapon system"
- NEW paradigm: "RCWS is a learning system that happens to fire a weapon"
- Shift: Focus on information flows (L6) and operator learning (CLD #1)
- Impact: Changes design priorities (sensors + data logging as important as gun)
- Recommendation: ⚠️ EVALUATE - may be too radical for conservative customer

**L1: Transcending Paradigms**
- Not applicable to this project (too abstract for engineering design)

---

## 5. INTEGRATION WITH ODI OUTCOMES

### 5.1 Mapping Leverage Points to ODI Outcomes

| Leverage Point | ODI Outcome | Opportunity | Design Intervention |
|----------------|-------------|-------------|---------------------|
| **L6 (Info Flows)** | OUT-25: Minimize ship motion effect | 14.9 | Ship IMU data feed to FCS (R-NEW-03) |
| **L6 (Info Flows)** | OUT-29: Minimize time to assess hit | 11.0 | Real-time impact detection (R-NEW-01) |
| **L8 (Neg Feedback)** | OUT-21: Maximize first-round accuracy | 14.2 | 2-axis stabilization loop (R204) |
| **L9 (Delays)** | OUT-22: Minimize engagement time | 13.5 | Low-latency sensors <50ms (R205) |
| **L4 (Self-Org)** | OUT-1005: Salt fog resistance | - | Marine materials (R501-R506) |
| **L5 (Rules)** | OUT-24: Hit probability moving target | 13.1 | Semi-auto (human in loop) |

### 5.2 Prioritization Matrix

```
                          HIGH LEVERAGE
                                │
                                │
    Quadrant 2              │  Quadrant 1
    (Low Opp, High Lev)     │  (HIGH PRIORITY)
                                │  • Ship IMU feed (L6 + Opp 14.9)
    • Paradigm shift?       │  • Real-time feedback (L6 + Opp 11.0)
                                │  • Stabilization (L8 + Opp 14.2)
    ────────────────────────┼──────────────────────────
                                │
    Quadrant 3              │  Quadrant 4
    (Low Opp, Low Lev)      │  (High Opp, Low Lev)
                                │
    • Parameter tweaks      │  • Weight optimization
    • Aesthetic details     │  • Slew rate increase
                                │
                          LOW LEVERAGE
```

**Design Focus:**
1. **Quadrant 1 (Both High):** 80% of design effort
2. **Quadrant 4 (High Opp):** 15% of design effort
3. **Quadrants 2 & 3:** 5% of design effort (only if time permits)

---

## 6. FEEDBACK LOOP DESIGN RECOMMENDATIONS

### 6.1 R1: Virtuous Accuracy Loop (STRENGTHEN)

**Goal:** Accelerate the learning loop (CLD #1)

**Design Interventions:**
1. **Real-time feedback** (L6):
   - Requirement: Camera-based impact detection
   - Specification: Display hit/miss within 2 seconds of engagement
   - Benefit: Immediate operator learning (vs. waiting for after-action review)

2. **Engagement data logging** (L6):
   - Requirement: Record all engagements (time, conditions, outcome)
   - Specification: 1000 engagement storage, USB export
   - Benefit: Post-mission analysis, identify patterns

3. **Simplified controls** (reduce barrier):
   - Requirement: Intuitive joystick (R802)
   - Specification: <4 hours operator qualification (R804)
   - Benefit: Lower barrier to practice → more iterations → faster learning

**Expected Outcome:**
- Operator proficiency time: 40 hours → 20 hours (50% reduction)
- Fleet combat readiness: Faster ramp-up with new operators

---

### 6.2 B1: Maintenance Balance Loop (STABILIZE)

**Goal:** Prevent oscillation between failure and backlog

**Design Interventions:**
1. **Reduce delay** (L9):
   - Strategy: Pre-position critical spares at 3 naval bases
   - Specification: 90% of failures repairable with on-site spares
   - Benefit: Repair delay 4 weeks → 1 week

2. **Predictive maintenance** (L6):
   - Requirement: Built-in diagnostics (R1405)
   - Specification: Predict failures 200 hours in advance (vibration monitoring)
   - Benefit: Shift from reactive to proactive maintenance

3. **Modular design** (L10):
   - Requirement: LRUs (Line Replaceable Units) for major subsystems
   - Specification: Sensor module, drive module, FCS module
   - Benefit: MTTR <2 hours (R1401)

**Expected Outcome:**
- System availability: 85% → 95%
- Maintenance cost: Reduced by 30% (preventive vs. corrective)

---

### 6.3 R2: Corrosion Vicious Cycle (BREAK)

**Goal:** Interrupt vicious cycle via design (not maintenance)

**Design Interventions:**
1. **Self-protecting materials** (L4):
   - Current: R501-R506 (marine-grade aluminum, 316 SS fasteners)
   - Enhancement: Add requirement for drainage design
   - Specification: No horizontal surfaces (water pooling), 5° min slope

2. **Eliminate galvanic couples** (L4):
   - Requirement: Isolate dissimilar metals (plastic washers)
   - Specification: Al-to-steel contact prohibited without insulation
   - Benefit: Eliminate accelerated corrosion

3. **Sacrificial anodes** (L4):
   - Requirement: Zinc anodes at critical joints
   - Specification: Replaceable every 2 years (PM interval)
   - Benefit: Protect structure, predictable maintenance cost

**Expected Outcome:**
- Corrosion-related failures: 40% → 5% of total failures
- Coating life: 5 years → 10 years (before major repaint)

---

## 7. SYSTEM BEHAVIOR PREDICTION

### 7.1 Scenario: Successful Deployment (Virtuous Cycle)

**Timeline:**
```
Month 0-6:   Prototype testing, operator training begins
             └─► R1 loop starts: Good stabilization → Early successes

Month 6-12:  Sea trials, data collection
             └─► R1 loop accelerates: More practice → Better operators

Month 12-24: Fleet retrofit (20 ships)
             └─► R1 loop at full strength: Training data shared fleet-wide

Month 24+:   Sustained high performance
             └─► B1 loop stable: Low failure rate, manageable maintenance
```

**Indicators of Success:**
- Operator qualification time: <30 hours (target: 20)
- First-round hit rate: >60% @ 500m sea state 4 (target: 50%)
- System availability: >92% (target: 90%)

---

### 7.2 Scenario: Design Failure (Vicious Cycles)

**Failure Mode 1: Corrosion Overwhelms Maintenance (R2 loop)**
```
Month 0-12:  Initial operation, minor corrosion noted
Month 12-18: Corrosion accelerates (poor material selection)
             └─► R2 vicious cycle begins
Month 18-30: Maintenance costs spiral, budget diverted from training
             └─► R1 virtuous cycle breaks (no practice time)
Month 30+:   System retired early, project failure
```

**Prevention:**
- ✅ Requirements R501-R506 already address this
- ✅ Phase 3: Rigorous DfX#3 (Corrosion) review mandatory

---

**Failure Mode 2: Over-Automation Dependency**
```
Month 0-12:  AI tracking works well, operators rely on it
Month 12-24: Manual skills atrophy (no practice)
             └─► "Shifting the Burden" archetype
Month 24:    Combat situation, EMI disables AI tracking
             └─► Operators cannot revert to manual mode effectively
Result:      Mission failure, loss of confidence
```

**Prevention:**
- ✅ Design decision: Semi-automation (L5 intervention)
- ✅ Training requirement: All operators qualified in manual mode

---

## 8. PHASE 2 PREPARATION: SYSTEMS-INFORMED CONCEPT EVALUATION

### 8.1 Enhanced VDI 2225 Criteria (Systems Thinking + ODI)

**Proposed Weighting:**

| Criterion | ODI Opp | Systems Leverage | Combined Weight |
|-----------|---------|------------------|-----------------|
| Ship motion compensation (OUT-25) | 14.9 | L8 (Neg feedback loop) | **0.30** |
| First-round accuracy (OUT-21) | 14.2 | L6 (Info flows) | **0.20** |
| Engagement speed (OUT-22) | 13.5 | L9 (Delays) | **0.15** |
| Real-time feedback (OUT-29) | 11.0 | L6 (Info flows) | **0.10** |
| Corrosion resistance (R1005) | - | L4 (Self-org) | **0.10** |
| Maintainability (R1401) | - | L10 (Flow structure) | **0.08** |
| Cost (R1501) | - | - | **0.07** |
| **TOTAL** | | | **1.00** |

**Justification:**
- Weights combine ODI opportunity scores (customer importance) with systems leverage
- High-leverage interventions weighted higher even if ODI score moderate
- Example: Corrosion (no direct ODI outcome but L4 intervention prevents vicious cycle)

---

### 8.2 Concept Evaluation Template

**Concepts to Evaluate in Phase 2:**
1. **Concept A:** 2-axis stabilization + basic FCS (baseline)
2. **Concept B:** 2-axis + AI FCS + thermal + real-time feedback (recommended)
3. **Concept C:** 3-axis stabilization + premium sensors
4. **Concept D:** 1-axis stabilization + extensive operator training

**Evaluation Matrix:**

| Criterion | Weight | A | B | C | D |
|-----------|--------|---|---|---|---|
| Motion compensation (L8) | 0.30 | 7 | 8 | 9 | 5 |
| First-round accuracy (L6) | 0.20 | 6 | 9 | 8 | 6 |
| Engagement speed (L9) | 0.15 | 7 | 8 | 7 | 6 |
| Real-time feedback (L6) | 0.10 | 4 | 9 | 6 | 4 |
| Corrosion resistance (L4) | 0.10 | 7 | 7 | 7 | 7 |
| Maintainability (L10) | 0.08 | 8 | 7 | 6 | 8 |
| Cost | 0.07 | 8 | 6 | 4 | 9 |
| **WEIGHTED SCORE** | 1.00 | **6.7** | **7.9** | **7.3** | **6.0** |

**Recommendation:** Concept B (7.9/10) confirmed as best balance

---

## 9. SUMMARY & NEXT ACTIONS

### 9.1 Key Systems Insights

**Feedback Loops Identified:**
1. **R1 (Virtuous):** Accuracy → Confidence → Practice → More accuracy ✅ STRENGTHEN
2. **B1 (Balancing):** Failures → Maintenance → Reliability ✅ STABILIZE
3. **R2 (Vicious):** Corrosion → Cost → Less protection → More corrosion ✅ BREAK
4. **Trade-off:** Automation vs. Training (Shifting Burden) ✅ AVOID

**High-Leverage Interventions:**
- **L6 (Info Flows):** Real-time feedback, ship IMU integration ⭐ HIGHEST PRIORITY
- **L8 (Neg Feedback):** Stabilization loop design (already in requirements)
- **L9 (Delays):** Minimize sensor lag, spare parts delay
- **L4 (Self-Org):** Material selection breaks corrosion cycle

---

### 9.2 New Requirements Generated

**Add to requirements list:**

| ID | Category | Requirement | D/W | Value | Verification | Leverage Point |
|----|----------|-------------|-----|-------|--------------|----------------|
| R-NEW-01 | Signals | Real-time hit indication | D | <2 s after impact | T | L6 |
| R-NEW-02 | Signals | Engagement data logging | W | 1000 engagements | I | L6 |
| R-NEW-03 | Signals | Ship IMU integration | W | CAN bus, 100 Hz | T | L6 |
| R-NEW-04 | Material | Drainage design | D | No horizontal surfaces, 5° min slope | I | L4 |
| R-NEW-05 | Material | Galvanic isolation | D | Dissimilar metals isolated | I | L4 |
| R-NEW-06 | Maintenance | Modular LRUs | D | 3 major modules (sensor, drive, FCS) | D | L10 |

---

### 9.3 Phase 2 Preparation Checklist

**Ready for Phase 2 Transition:**
- [x] ODI analysis complete (42 outcomes, opportunity scores)
- [x] Systems thinking analysis complete (4 CLDs, leverage points)
- [x] Requirements list complete (93 + 6 new = 99 requirements)
- [x] VDI 2225 criteria weighted (ODI + Systems)
- [ ] **Stakeholder review** (schedule this week)
- [ ] **Gate 1 approval** (after stakeholder sign-off)

**Phase 2 Readiness:**
- Concept B already selected (8.7/10 ODI, 7.9/10 systems-weighted)
- Function structure can begin immediately after Gate 1
- Morphological matrix will focus on high-leverage subsystems (stabilization, FCS, materials)

---

### 9.4 Integration Diagram: ODI + Systems + P&B

```
┌────────────────────────────────────────────────────────────────┐
│  PHASE 0: ODI                                                  │
│  ────────────────────────────────────────────────────────────  │
│  Outcomes captured (42)   →   Opportunity scores calculated    │
│  Segments identified      →   Top outcomes: 14.9, 14.2, 13.5   │
└────────────────┬───────────────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────────────┐
│  SYSTEMS THINKING (This Document)                              │
│  ────────────────────────────────────────────────────────────  │
│  CLDs drawn               →   Feedback loops identified        │
│  Leverage points found    →   L6, L8, L9, L4 prioritized       │
│  Archetypes recognized    →   Vicious cycles to break          │
└────────────────┬───────────────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────────────┐
│  PHASE 1: TASK CLARIFICATION (Pahl & Beitz)                    │
│  ────────────────────────────────────────────────────────────  │
│  Requirements (93 → 99)   →   ODI outcomes mapped              │
│  Weighted by Opp + Lev    →   Demands vs. Wishes prioritized   │
│  Gate 1 criteria          →   Systems resilience verified      │
└────────────────┬───────────────────────────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────────────────────────┐
│  PHASE 2: CONCEPTUAL DESIGN (Next)                             │
│  ────────────────────────────────────────────────────────────  │
│  VDI 2225 weighted by:    →   30% ODI + 70% Systems leverage   │
│  Morphological matrix     →   Focus on high-leverage subsys    │
│  Concept evaluation       →   Customer scorecard (Concept B)   │
└────────────────────────────────────────────────────────────────┘
```

---

## 10. LESSONS LEARNED (D-M-I-R Reflection)

### Diagnosis
**What was the real problem?**
- Initial framing: "Need marinized RCWS" (solution-focused)
- Deeper diagnosis (ODI): "Gunners can't compensate for ship motion" (outcome-focused)
- Systems lens: "Training loop too slow, corrosion cycle too fast" (dynamic behavior)

### Modeling
**How does the system work?**
- Four key feedback loops identified (2 reinforcing, 1 balancing, 1 trade-off)
- Critical delays: Spare parts (4 weeks), sensor lag (100ms), learning (hours)
- Leverage points: Information flows (L6) most impactful for this system

### Intervention
**Where to intervene?**
- **Highest leverage:** L6 (real-time feedback) + L8 (stabilization) + L4 (materials)
- **Medium leverage:** L9 (reduce delays), L10 (modular architecture)
- **Low leverage:** Parameter tweaks (optimize last)

### Reflection
**What did we learn?**
- Systems thinking revealed 6 new requirements that weren't obvious from ODI alone
- Combining ODI opportunity scores with leverage points creates better prioritization
- Archetype recognition (Fixes That Fail, Shifting Burden) prevents common design traps

---

**Status:** ✅ Ready for stakeholder review and Gate 1 transition
**Next:** Update requirements list with 6 new requirements, then proceed to Phase 2

---

*This systems analysis integrates with [[RCWS-127-NAVAL_P0_01_ODI_analysis|ODI Analysis]] and [[RCWS-127-NAVAL_P1_01_requirements_list|Requirements List]] to provide a complete Phase 1 package.*
