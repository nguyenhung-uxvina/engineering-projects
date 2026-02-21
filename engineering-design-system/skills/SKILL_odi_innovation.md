# SKILL: Outcome-Driven Innovation (ODI)
## Systematic Customer Insight for Defense Product Development

**Skill ID:** SKILL_odi_innovation
**Difficulty:** ⭐⭐⭐⭐ (Advanced)
**Time to Master:** 20-25 hours
**Prerequisites:** Basic understanding of customer requirements, product development process
**Integration:** Use BEFORE Task Clarification (Pahl & Beitz Phase 1)
**Commands:** `/odi`, `/jobs`, `/outcomes`, `/opportunity`, `/segment`

---

## ⌨️ SLASH COMMANDS

| Command | Aliases | Purpose |
|---------|---------|---------|
| `/odi` | `/customer` | Run full ODI process (10 steps) |
| `/jobs` | `/jtbd` | Define job executor and job map |
| `/outcomes` | `/dim` | Capture outcome statements (D-I-M format) |
| `/opportunity` | `/opp` | Calculate opportunity scores |
| `/segment` | `/seg` | Identify customer segments |

### Command Output Templates

**`/odi`** → Full ODI process kickoff:
```markdown
## ODI Analysis - [PROJECT]

### Step 1: Define Job Executor
- Primary executor: [Who performs the job]
- Job statement: [Verb + object + context]

### Step 2: Job Map (8 stages)
| Stage | Description | Outcomes to capture |
|-------|-------------|---------------------|
| Define | ... | ... |
| Locate | ... | ... |
```

**`/jobs`** → Job definition:
```markdown
## Job Definition

**Job Executor**: [Role, not buyer]
**Core Job**: [Verb] + [object] + [contextual clarifier]

### Job Map
1. Define → 2. Locate → 3. Prepare → 4. Confirm →
5. Execute → 6. Monitor → 7. Modify → 8. Conclude
```

**`/outcomes`** → D-I-M format outcomes:
```markdown
## Outcome Statements

| ID | Direction | Metric | Object |
|----|-----------|--------|--------|
| O-01 | Minimize | the time it takes to | acquire target |
| O-02 | Minimize | the likelihood of | false positive |
| O-03 | Increase | the accuracy of | range measurement |
```

**`/opportunity`** → Opportunity algorithm:
```markdown
## Opportunity Scores

Formula: Opportunity = Importance + max(Importance - Satisfaction, 0)

| Outcome | Importance | Satisfaction | Opportunity |
|---------|------------|--------------|-------------|
| O-01 | 9.2 | 4.1 | 14.3 🔴 |
| O-02 | 8.5 | 7.2 | 9.8 🟡 |
| O-03 | 7.1 | 8.0 | 7.1 🟢 |

🔴 >12 = High opportunity | 🟡 10-12 = Moderate | 🟢 <10 = Low
```

**`/segment`** → Outcome-based segmentation:
```markdown
## Customer Segments

| Segment | Size | Key Unmet Outcomes | Strategy |
|---------|------|-------------------|----------|
| Underserved | 40% | O-01, O-03, O-07 | Disruptive innovation |
| Overserved | 35% | None (all satisfied) | Cost reduction |
| Restricted | 25% | Budget constraints | Value offering |
```

---

## 🎯 WHAT IS ODI?

**Outcome-Driven Innovation (ODI)** is a systematic process for discovering what customers are trying to achieve (outcomes), measuring how well current solutions satisfy those outcomes, and identifying opportunities for innovation.

### The Core Insight

> **"Innovation failure is not a creativity problem—it's a knowledge problem. The constraint limiting innovation success is customer outcome knowledge, not engineering capability or budget."**

### Success Rate Comparison

| Approach | Success Rate | Why |
|----------|--------------|-----|
| **Traditional (ideas-first)** | 10-50% | Guessing what customers want |
| **ODI (outcomes-first)** | 70-86% | Systematically discovering unmet needs |

### The Math Behind ODI

With 15 unmet customer needs and 100 possible solutions per need:
- **Random approach:** 1 in 14 million chance of success
- **ODI approach:** First discover which needs are underserved, THEN generate targeted solutions

---

## 📋 WHEN TO USE THIS SKILL

### Use ODI When:
✅ Starting a new product development project
✅ Requirements are vague or conflicting
✅ Previous products had low customer acceptance
✅ Innovation success rate is below 60%
✅ Entering a new market or domain
✅ Customers say "we need X" but you suspect they need Y

### ODI Phase in Design Process

```
PROJECT START
     ↓
┌────────────────────────┐
│  ODI (Steps 1-7)       │ ← YOU ARE HERE (before requirements)
│  Discover outcomes     │
│  Identify opportunities│
└───────────┬────────────┘
            ↓
┌────────────────────────┐
│  Task Clarification    │ ← ODI outcomes become requirements
│  (Pahl & Beitz Phase 1)│
└───────────┬────────────┘
            ↓
┌────────────────────────┐
│  Conceptual Design     │ ← ODI Steps 8-10 (brainstorm on outcomes)
│  (Pahl & Beitz Phase 2)│
└────────────────────────┘
```

---

## 🔟 THE 10-STEP ODI PROCESS

### Overview Map

```
FOUNDATION (Steps 1-4)        RESEARCH (Steps 5-7)         STRATEGY (Steps 8-10)
┌────────────────────┐        ┌────────────────────┐       ┌────────────────────┐
│ 1. Define executor │        │ 5. Field survey    │       │ 8. Brainstorm on   │
│ 2. Define jobs     │───────▶│ 6. Opportunity     │──────▶│    outcomes        │
│ 3. Capture outcomes│        │    algorithm       │       │ 9. Scorecard eval  │
│ 4. Job map         │        │ 7. Segmentation    │       │ 10. Growth strategy│
└────────────────────┘        └────────────────────┘       └────────────────────┘
```

---

## 📖 STEP-BY-STEP GUIDE

### STEP 1: Define the Job Executor

**Purpose:** Identify WHO is trying to get the job done.

**Key Principle:** The job executor is NOT always the buyer or decision-maker.

#### Defense Context Examples

| Product | Job Executor | NOT the Executor |
|---------|--------------|------------------|
| **RCWS-127-NAVAL** | Naval gunner (operator) | Procurement officer, Ship captain |
| **V-SMASH Fire Control** | Infantry rifleman | Battalion commander |
| **MANPADS Trainer** | Air defense operator | Training coordinator |
| **Target USV** | Naval exercise coordinator | Fleet commander |
| **Training Grenade** | Infantry trainee | Instructor |

#### How to Identify

**Ask:** "Who physically performs the job of [achieving the goal]?"

**Example - RCWS-127-NAVAL:**
- ❌ Wrong: "Ship captain uses RCWS to defend the ship"
- ✅ Right: "Naval gunner uses RCWS to engage surface/air threats"

The gunner is the executor; the captain sets rules of engagement but doesn't operate the system.

#### Exercise 1.1
For the following products, identify the job executor:
1. Small Arms Marksmanship Trainer (V-SAMT-001)
2. UAV Catapult Launch System
3. LOMAH (Location of Miss and Hit) System

---

### STEP 2: Define Jobs-to-be-Done

**Purpose:** Identify WHAT the executor is trying to accomplish (the functional job).

**Key Principle:** Focus on the FUNCTIONAL job, not emotional or social jobs (though those exist).

#### The Universal Job Map (8 Steps)

Every job follows this universal structure:

| Job Step | Question | RCWS-127-NAVAL Example |
|----------|----------|------------------------|
| **1. DEFINE** | What must be defined before execution? | Define threat type, engagement parameters |
| **2. LOCATE** | What must be located/gathered? | Acquire target visually/electronically |
| **3. PREPARE** | What must be prepared? | Power up system, check ammunition |
| **4. CONFIRM** | What must be confirmed? | Verify friend-or-foe, check fire corridor |
| **5. EXECUTE** | The core task | Track and engage target |
| **6. MONITOR** | What must be monitored during execution? | Observe rounds, assess hits |
| **7. MODIFY** | What adjustments might be needed? | Adjust aim, change ammo type |
| **8. CONCLUDE** | What must happen after execution? | Return to ready state, report results |

#### Job Statement Format

**Template:** `[Verb] + [Object] + [Context/Clarifier]`

**Examples:**
- RCWS Gunner: "Engage surface and air threats from a moving naval platform"
- MANPADS Operator: "Engage hostile aircraft with shoulder-launched missile"
- Training Grenade User: "Practice grenade throwing with realistic feedback"

#### Exercise 2.1
Create a Universal Job Map for "MANPADS Operator engages hostile aircraft"

---

### STEP 3: Capture Customer Outcomes

**Purpose:** Discover the metrics customers use to measure job success.

#### Outcome Statement Structure: D-I-M

```
[DIRECTION] + [INDICATOR] + [MATTER]

Direction: Minimize, Maximize, Increase, Reduce, Optimize, Avoid
Indicator: Time, likelihood, number, frequency, amount, variability
Matter: What specifically is being measured
```

#### Outcome Statement Examples

| Product | Outcome Statement | D-I-M Breakdown |
|---------|------------------|-----------------|
| RCWS-127-NAVAL | **Minimize** time to acquire moving target | D: Minimize, I: Time, M: Acquire moving target |
| RCWS-127-NAVAL | **Maximize** accuracy of first round on target | D: Maximize, I: Accuracy, M: First round on target |
| MANPADS Trainer | **Minimize** likelihood of engaging friendly aircraft | D: Minimize, I: Likelihood, M: Engaging friendly |
| MANPADS Trainer | **Reduce** time to achieve seeker lock | D: Reduce, I: Time, M: Achieve seeker lock |
| Training Grenade | **Maximize** similarity to live grenade flight | D: Maximize, I: Similarity, M: Flight characteristics |
| Training Grenade | **Minimize** risk of injury during training | D: Minimize, I: Risk, M: Injury during training |

#### Outcome Validation Checklist

✅ **Good Outcome Statement:**
- [ ] Describes what customer wants to achieve (not a solution)
- [ ] Is measurable (can be quantified)
- [ ] Is stable over time (doesn't change with technology)
- [ ] Uses customer language (not engineering jargon)
- [ ] Contains only one idea (not compound)

❌ **Bad Outcome Statement Examples:**

| Bad Statement | Why Bad | Good Version |
|--------------|---------|--------------|
| "Need faster processor" | Solution, not outcome | "Minimize time to process target data" |
| "Want better display" | Vague, not measurable | "Maximize visibility of reticle in bright sunlight" |
| "Improve accuracy and reliability" | Compound statement | Split into 2: "Maximize hit probability" + "Minimize system failures" |

#### Outcome Capture Process

**Target:** 50-150 outcome statements per job-to-be-done

**Methods:**
1. **Interview executors** (10-15 people) - Ask "How do you measure success when [doing job]?"
2. **Observe jobs being performed** - Note what they check, measure, worry about
3. **Analyze complaints** - What do they wish was better?
4. **Review requirements docs** - Extract outcome-oriented statements

#### Exercise 3.1
For "MANPADS Operator engages hostile aircraft", write 10 outcome statements covering different job steps.

---

### STEP 4: Organize Outcomes into Universal Job Map

**Purpose:** Structure outcomes by job step for systematic analysis.

#### RCWS-127-NAVAL Outcome Map Example

```markdown
JOB: Engage surface and air threats from moving naval platform

STEP 1: DEFINE (Define engagement parameters)
├── Minimize time to classify threat type
├── Reduce likelihood of misidentifying threat
└── Maximize accuracy of threat assessment

STEP 2: LOCATE (Acquire target)
├── Minimize time to acquire target visually
├── Reduce time to acquire target electronically
├── Maximize probability of detecting low-signature targets
└── Minimize effort required to maintain visual contact

STEP 3: PREPARE (Power up, check ammunition)
├── Minimize time from standby to ready state
├── Reduce likelihood of ammunition feed jam
├── Maximize reliability of system power-up
└── Minimize time to verify system operational status

STEP 4: CONFIRM (Verify fire corridor)
├── Minimize likelihood of firing into restricted zone
├── Reduce time to confirm friend-or-foe status
├── Maximize confidence in safe-to-fire decision
└── Minimize likelihood of collateral damage

STEP 5: EXECUTE (Track and engage)
├── Maximize accuracy of first round on target
├── Minimize time to neutralize threat
├── Reduce ammunition expenditure per target
├── Maximize hit probability on moving target
└── Minimize effect of ship motion on accuracy

STEP 6: MONITOR (Observe engagement)
├── Minimize time to assess hit/miss
├── Maximize visibility of tracer rounds
├── Reduce uncertainty in battle damage assessment
└── Minimize delay in feedback to operator

STEP 7: MODIFY (Adjust engagement)
├── Minimize time to switch ammunition types
├── Reduce effort to re-engage missed target
├── Maximize speed of re-acquisition after jam
└── Minimize time to adjust aim for different range

STEP 8: CONCLUDE (Return to ready)
├── Minimize time to return to search mode
├── Reduce time to report engagement results
├── Maximize completeness of engagement data recorded
└── Minimize cleanup/reset time after engagement
```

**Total outcomes in this example:** 32 (typical jobs have 50-150)

---

### STEP 5: Field Quantitative Survey

**Purpose:** Measure importance and satisfaction for all outcomes.

#### Survey Structure

For EACH outcome statement, ask TWO questions:

**Question 1 - Importance:**
"When [performing job], how important is it to [outcome statement]?"
- Scale: 1 (Not at all important) to 5 (Extremely important)

**Question 2 - Satisfaction:**
"When using your current solution, how satisfied are you with your ability to [outcome statement]?"
- Scale: 1 (Not at all satisfied) to 5 (Completely satisfied)

#### Survey Example - RCWS-127-NAVAL

| Outcome Statement | Importance (1-5) | Satisfaction (1-5) |
|------------------|------------------|-------------------|
| Minimize time to acquire moving target | ☐1 ☐2 ☐3 ☐4 ☐5 | ☐1 ☐2 ☐3 ☐4 ☐5 |
| Maximize accuracy of first round | ☐1 ☐2 ☐3 ☐4 ☐5 | ☐1 ☐2 ☐3 ☐4 ☐5 |
| Minimize effect of ship motion on accuracy | ☐1 ☐2 ☐3 ☐4 ☐5 | ☐1 ☐2 ☐3 ☐4 ☐5 |
| ... (repeat for all 50-150 outcomes) | | |

#### Sample Size Requirements

| Population Size | Minimum Sample | Target Sample |
|----------------|----------------|---------------|
| <50 executors | 30-40 | All |
| 50-200 executors | 40-60 | 80-100 |
| 200-1000 executors | 60-100 | 180-300 |
| >1000 executors | 100-200 | 300-600 |

**Vietnamese Navy RCWS Example:**
- Population: ~500 naval gunners
- Target sample: 180-300 respondents
- Method: Mix of online survey + in-person interviews

---

### STEP 6: Calculate Opportunity Scores

**Purpose:** Identify which outcomes are underserved (high importance, low satisfaction).

#### The Opportunity Algorithm

```
Opportunity = Importance + MAX(Importance - Satisfaction, 0)
```

**Conversion from 5-point to 10-point scale:**
```
Score (10-point) = (% rating 4 or 5) × 10
```

#### Worked Example - RCWS-127-NAVAL

| Outcome | % Imp 4-5 | % Sat 4-5 | Imp (10pt) | Sat (10pt) | Opportunity | Category |
|---------|-----------|-----------|------------|------------|-------------|----------|
| Minimize time to acquire moving target | 92% | 45% | 9.2 | 4.5 | 9.2 + (9.2-4.5) = **13.9** | **HIGH** |
| Maximize accuracy of first round | 95% | 50% | 9.5 | 5.0 | 9.5 + (9.5-5.0) = **14.0** | **HIGH** |
| Minimize effect of ship motion | 88% | 35% | 8.8 | 3.5 | 8.8 + (8.8-3.5) = **14.1** | **HIGH** |
| Minimize time from standby to ready | 75% | 70% | 7.5 | 7.0 | 7.5 + (7.5-7.0) = **8.0** | Low |
| Maximize reliability of power-up | 85% | 80% | 8.5 | 8.0 | 8.5 + (8.5-8.0) = **9.0** | Low |

#### Opportunity Score Interpretation

| Score Range | Category | Action | Example |
|-------------|----------|--------|---------|
| **>15** | **EXTREME** | Immediate priority - accelerate development | Rare, highest value |
| **12-15** | **HIGH** | Strong priority - fund and resource | RCWS ship motion compensation |
| **10-12** | **MODERATE** | Second-tier - monitor and consider | Important but satisfied enough |
| **<10** | **LOW** | Potentially overserved - reduce/maintain | Current solution adequate |

#### Key Insight

**Overserved outcomes (satisfaction > importance)** indicate:
- Features customers don't value much
- Opportunities for cost reduction
- Potential for "disruptive" lower-cost solutions

---

### STEP 7: Identify Outcome-Based Segments

**Purpose:** Discover customer groups with different unmet needs.

**Key Principle:** Segment by outcome importance/satisfaction patterns, NOT demographics.

#### Segmentation Process

1. **Cluster customers** by their outcome ratings (not by age, rank, unit, etc.)
2. **Identify segments** with distinct opportunity profiles
3. **Size each segment** (% of population)
4. **Assess competitive position** in each segment

#### RCWS-127-NAVAL Segmentation Example

**Segment A: "Precision Seekers"** (35% of gunners)
- High importance: Accuracy outcomes (first-round hit, precision)
- Low satisfaction: Current system accuracy insufficient
- Underserved outcomes:
  - Maximize accuracy of first round (Opp: 16.2)
  - Minimize aiming error (Opp: 15.8)
  - Maximize hit probability at long range (Opp: 14.5)

**Segment B: "Fast Responders"** (45% of gunners)
- High importance: Speed outcomes (acquisition time, response time)
- Low satisfaction: Current system too slow
- Underserved outcomes:
  - Minimize time to acquire target (Opp: 15.1)
  - Reduce time from detect to engage (Opp: 14.9)
  - Minimize time to switch targets (Opp: 13.2)

**Segment C: "All-Weather Operators"** (20% of gunners)
- High importance: Reliability in harsh conditions
- Low satisfaction: Night/weather performance poor
- Underserved outcomes:
  - Maximize performance in low visibility (Opp: 16.8)
  - Minimize effect of sea spray on sensors (Opp: 15.5)
  - Reduce downtime in salt environment (Opp: 14.2)

#### Strategy Implications

| Segment | Product Strategy | RCWS Design Focus |
|---------|-----------------|-------------------|
| Precision Seekers | **Differentiated** - Premium accuracy | Advanced stabilization, precision optics |
| Fast Responders | **Dominant** - Best speed + reasonable cost | Fast servo motors, predictive targeting |
| All-Weather | **Differentiated** - Premium environmental | IP67 sealing, thermal/IR sensors, corrosion protection |

**Design Decision:** Can one RCWS serve all segments, or need variants?
- Option 1: Modular design with base + segment-specific upgrades
- Option 2: Single "dominant" design targeting largest segment (Fast Responders)
- Option 3: Three variants (high cost, high customization)

---

### STEP 8: Focused Brainstorming

**Purpose:** Generate solutions targeting specific underserved outcomes.

**Key Principle:** Brainstorm on OUTCOMES, not problems. "How can we help customers [achieve this outcome]?"

#### FOCUS-BREAKTHROUGH Method

1. **FOCUS** on top 3-5 underserved outcomes
2. **BREAKTHROUGH** thinking - aim for 10x improvement, not 10%
3. **CONSTRAIN** ideas to address the specific outcome
4. **ELIMINATE** ideas that don't move the opportunity score
5. **OPTIMIZE** remaining ideas for feasibility

#### Worked Example - RCWS-127-NAVAL

**Target Outcome:** "Minimize effect of ship motion on accuracy" (Opportunity: 14.1)

**Brainstorming Round 1 (Unconstrained):**
1. Active stabilization (gyro-stabilized platform)
2. Predictive aim compensation (AI-based)
3. Larger ammunition (less affected by movement) ❌ Changes weapon
4. Fire only when stable (wait for calm moment)
5. Hybrid: Stabilization + predictive compensation
6. Operator training to time shots ❌ Doesn't reduce effect, just mitigates
7. Shock-absorbing mount
8. Real-time ballistic adjustment based on IMU data
9. Fire multiple rounds, AI selects best moment ❌ Wastes ammo
10. Dual-axis gimbal with fast servo response

**Elimination (does it address the outcome?):**
- #3: Changes weapon (out of scope)
- #4: Doesn't reduce effect, just avoids it
- #6: Training doesn't change system performance
- #9: Wasteful, not acceptable for 12.7mm

**Optimization (feasibility analysis):**

| Idea | Technical Feasibility | Cost | Impact on Outcome | Priority |
|------|----------------------|------|-------------------|----------|
| 1. Gyro-stabilized platform | High (proven tech) | High ($40K-60K) | Very high (8→2 mil RMS) | **P1** |
| 2. Predictive AI compensation | Medium (needs development) | Medium ($10K-20K) | Medium (8→5 mil RMS) | P2 |
| 5. Hybrid (1+2) | Medium | Very high ($50K-80K) | Very high (8→1 mil RMS) | P1 (if budget allows) |
| 7. Shock-absorbing mount | High | Low ($2K-5K) | Low (8→7 mil RMS) | P3 (quick win) |
| 8. Real-time ballistic adjust | Medium | Medium ($15K-25K) | Medium-High (8→4 mil RMS) | P2 |
| 10. Dual-axis gimbal | High | High ($35K-50K) | High (8→3 mil RMS) | P1 |

**Decision:** Pursue Idea #10 (Dual-axis gimbal) as baseline, with Idea #8 (ballistic adjustment) as value-add.

---

### STEP 9: Customer Scorecard Evaluation

**Purpose:** Predict product success BEFORE building by scoring concepts against top outcomes.

#### Scorecard Structure

| Outcome (ranked by Opp) | Weight | Current | Concept A | Concept B | Concept C |
|-------------------------|--------|---------|-----------|-----------|-----------|
| [Outcome 1] (Opp: 15.2) | 0.25 | Score | Score | Score | Score |
| [Outcome 2] (Opp: 14.1) | 0.20 | Score | Score | Score | Score |
| [Outcome 3] (Opp: 13.5) | 0.15 | Score | Score | Score | Score |
| ... | ... | ... | ... | ... | ... |
| **WEIGHTED TOTAL** | 1.00 | | | | |

**Scoring Scale:** 1-10 (1 = doesn't achieve outcome, 10 = perfectly achieves outcome)

#### Worked Example - RCWS-127-NAVAL Concepts

**Concepts:**
- **Current:** Manual aim with basic optics
- **Concept A:** Stabilized platform + basic FCS
- **Concept B:** Stabilized platform + AI-enhanced FCS + thermal
- **Concept C:** Predictive software-only (no stabilization hardware)

| Outcome | Opp | Weight | Current | A | B | C |
|---------|-----|--------|---------|---|---|---|
| Minimize effect of ship motion | 14.1 | 0.30 | 3 | 8 | 9 | 5 |
| Maximize first-round accuracy | 14.0 | 0.25 | 4 | 7 | 9 | 6 |
| Minimize time to acquire target | 13.9 | 0.20 | 5 | 7 | 8 | 7 |
| Maximize low-visibility performance | 13.2 | 0.15 | 2 | 5 | 9 | 3 |
| Reduce ammunition per target | 12.5 | 0.10 | 4 | 7 | 8 | 6 |
| **WEIGHTED SCORE** | | **1.00** | **3.55** | **7.05** | **8.60** | **5.70** |

**Interpretation:**
- **Concept B scores 8.6/10** - High probability of success
- **Concept A scores 7.0/10** - Good, but B significantly better
- **Concept C scores 5.7/10** - Marginal improvement, risky

**Decision Rule:** Concepts scoring >8.0 on top outcomes have high success probability. → **Proceed with Concept B**

---

### STEP 10: Growth Strategy Selection

**Purpose:** Choose the right competitive strategy based on outcomes served and cost structure.

#### The Growth Strategy Matrix

```
                    OVERSERVED ◄────────────────► UNDERSERVED
                         │                              │
    ┌────────────────────┼──────────────────────────────┼────────────────────┐
    │                    │                              │                    │
    │   DISRUPTIVE       │                              │   DIFFERENTIATED   │
    │   STRATEGY         │                              │   STRATEGY         │
LOW │                    │                              │                    │
    │   Strip features   │                              │   Add premium      │
COST│   Lower price      │                              │   features         │
    │   Target non-      │                              │   Target demanding │
    │   consumers        │                              │   customers        │
    │                    │                              │                    │
    ├────────────────────┼──────────────────────────────┼────────────────────┤
    │                    │                              │                    │
    │   DISCRETE         │                              │   DOMINANT         │
    │   STRATEGY         │                              │   STRATEGY         │
HIGH│                    │                              │                    │
COST│   Cost reduction   │                              │   Best performance │
    │   focus            │                              │   + cost parity    │
    │   Commodity play   │                              │   Market leadership│
    │                    │                              │                    │
    └────────────────────┴──────────────────────────────┴────────────────────┘
```

#### Strategy Definitions

**1. DIFFERENTIATED Strategy (Underserved + Low Cost)**
- Address underserved outcomes
- Premium pricing justified
- Target: Customers who value those outcomes highly
- Example: RCWS-127-NAVAL with advanced stabilization for "All-Weather Operators" segment

**2. DOMINANT Strategy (Underserved + High Cost)**
- Best performance on underserved outcomes
- Competitive cost (not premium)
- Target: Market leadership
- Example: V-SMASH fire control (best accuracy + acceptable cost)

**3. DISRUPTIVE Strategy (Overserved + Low Cost)**
- Strip features customers don't value
- Lower price significantly
- Target: Non-consumers or overserved customers
- Example: Basic MANPADS trainer (no live missile, 1/10 cost)

**4. DISCRETE Strategy (Overserved + High Cost)**
- Commodity approach
- Compete on cost reduction
- Target: Mature markets
- Example: Standard target drones (low-tech, cost-driven)

#### Defense Portfolio Strategy Examples

| Product | Strategy | Rationale | Opportunity Evidence |
|---------|----------|-----------|---------------------|
| **RCWS-127-NAVAL** | **Differentiated** | Ship motion compensation highly underserved (Opp: 14+), premium justified | Survey shows 20% willing to pay 50% more for all-weather capability |
| **V-SMASH** | **Dominant** | Core product for infantry, aim for best + competitive cost | Multiple underserved outcomes (accuracy, speed), large market |
| **MANPADS Trainer** | **Differentiated** | Extreme outcomes (realism, safety), low volume justifies premium | Live training unsafe + expensive, simulator high value |
| **Training Grenade** | **Disruptive** | Live grenades overserve (too dangerous for basic training), strip to essentials | Basic training needs safety, not lethality |
| **Target UAV** | **Discrete** | Mature market, low differentiation, cost competition | Survey shows satisfaction high, price sensitivity high |

---

## 🔗 INTEGRATION WITH PAHL & BEITZ

### ODI Feeds Into Requirements List

```markdown
## Task Clarification (Phase 1) - Requirements List

| ID | Requirement | D/W | Value | Source |
|----|-------------|-----|-------|--------|
| R01 | Ship motion compensation accuracy | D | ±1 mil RMS | **ODI Outcome (Opp: 14.1)** |
| R02 | First-round hit probability | D | >70% @ 500m | **ODI Outcome (Opp: 14.0)** |
| R03 | Target acquisition time | W | <3 seconds | **ODI Outcome (Opp: 13.9)** |
| R04 | Night/thermal capability | W | 200m range | **ODI Outcome (Opp: 13.2)** |
| R05 | Operating temperature range | D | -20°C to +50°C | **MIL-STD + ODI validation** |
```

**Key Benefit:** Requirements are VALIDATED by customer data, not assumed.

### ODI Weights Concept Evaluation (VDI 2225)

```markdown
## Conceptual Design (Phase 2) - VDI 2225 Evaluation

| Criterion | Weight | Concept A | Concept B | Concept C |
|-----------|--------|-----------|-----------|-----------|
| Ship motion compensation | **0.30** | 3 | 4 | 2 |
| First-round accuracy | **0.25** | 3 | 4 | 3 |
| Acquisition speed | **0.20** | 4 | 3 | 4 |
| ... | ... | ... | ... | ... |

Weights derived from ODI opportunity scores (normalized)
```

**Key Benefit:** Objective criterion weighting based on customer importance, not subjective judgment.

---

## 🛠️ TOOLS & TEMPLATES

### Template 1: Outcome Statement Capture Sheet

```markdown
## Outcome Capture Session

**Product:** _____________
**Job Executor:** _____________
**Job-to-be-Done:** _____________
**Job Step:** ___ (1-8 from Universal Job Map)
**Interview Date:** _____________
**Respondent:** _____________

### Outcome Statements Captured

| # | Outcome Statement | Direction | Indicator | Matter | Valid? |
|---|------------------|-----------|-----------|--------|--------|
| 1 | | | | | ☐ |
| 2 | | | | | ☐ |
| 3 | | | | | ☐ |
...

### Validation Check (for each outcome)
- ☐ Describes outcome, not solution?
- ☐ Measurable?
- ☐ Technology-independent?
- ☐ Customer language?
- ☐ Single idea?
```

### Template 2: Opportunity Landscape

```markdown
## Opportunity Landscape: [Product Name]

**Survey Date:** _____________
**Respondents:** ___ (target: 180+)
**Response Rate:** ___%

### Top 10 Opportunities

| Rank | Outcome Statement | Opp Score | Category | Action |
|------|------------------|-----------|----------|--------|
| 1 | | | EXTREME/HIGH/MOD | |
| 2 | | | | |
| 3 | | | | |
...

### Opportunity Distribution

| Category | Count | % |
|----------|-------|---|
| EXTREME (>15) | | |
| HIGH (12-15) | | |
| MODERATE (10-12) | | |
| LOW (<10) | | |
| **TOTAL** | | 100% |

### Strategic Recommendations

**Immediate Priorities (EXTREME + HIGH):**
1. [Outcome + proposed solution direction]
2. [Outcome + proposed solution direction]
3. [Outcome + proposed solution direction]

**Monitor (MODERATE):**
- [Outcomes to track]

**Reduce/Maintain (LOW):**
- [Overserved outcomes - cost reduction opportunities]
```

### Template 3: Customer Scorecard

```markdown
## Customer Scorecard: [Product Concepts]

**Product:** _____________
**Date:** _____________
**Concepts Evaluated:** A, B, C, ...

| Outcome | Opp | Weight | Current | Concept A | Concept B | Concept C |
|---------|-----|--------|---------|-----------|-----------|-----------|
| [Top outcome 1] | | | | | | |
| [Top outcome 2] | | | | | | |
...
| **WEIGHTED SCORE** | | **1.00** | | | | |

### Decision Criteria
- **8.0+:** High success probability - Recommend proceed
- **7.0-7.9:** Good - Proceed with risk mitigation
- **6.0-6.9:** Marginal - Significant improvements needed
- **<6.0:** High risk - Reject or major redesign

### Selected Concept: ___________
**Justification:** _____________
```

---

## ⚠️ COMMON PITFALLS

### Pitfall 1: Job Too Narrow

**Wrong:** "Use RCWS to fire 12.7mm rounds"
**Right:** "Engage surface and air threats from moving platform"

**Why it matters:** Narrow job = miss opportunities for innovation outside current solution.

### Pitfall 2: Solutions Disguised as Outcomes

**Wrong:** "Need faster processor"
**Right:** "Minimize time to process target data"

**Why it matters:** Solutions constrain design space; outcomes enable creativity.

### Pitfall 3: Skipping the Survey

**Wrong:** "We already know what customers want from experience"
**Right:** Field the survey with 180+ respondents to get quantitative data

**Why it matters:** Intuition fails; data reveals surprises. Even experts are often wrong about importance vs. satisfaction.

### Pitfall 4: Demographic Segmentation

**Wrong:** Segment by "Young gunners vs. Experienced gunners"
**Right:** Segment by outcome patterns ("Precision Seekers" vs. "Fast Responders")

**Why it matters:** Demographics don't predict needs; outcome patterns do.

### Pitfall 5: Brainstorming Before Outcomes

**Wrong:** Start with "Let's brainstorm RCWS improvements"
**Right:** First identify underserved outcomes, THEN brainstorm solutions

**Why it matters:** Unfocused brainstorming = random walk. Outcome-focused brainstorming = targeted innovation.

---

## 🇻🇳 VIETNAMESE TERMINOLOGY

| English | Vietnamese | Notes |
|---------|------------|-------|
| **Outcome-Driven Innovation** | Đổi mới Hướng Kết quả | |
| **Job-to-be-Done** | Công việc Cần làm | |
| **Job Executor** | Người Thực hiện | |
| **Outcome** | Kết quả Mong muốn | |
| **Opportunity Score** | Điểm Cơ hội | |
| **Importance** | Mức độ Quan trọng | |
| **Satisfaction** | Mức độ Hài lòng | |
| **Universal Job Map** | Sơ đồ Công việc Phổ quát | |
| **Underserved** | Chưa được Đáp ứng | |
| **Overserved** | Đã được Đáp ứng Thừa | |
| **Growth Strategy** | Chiến lược Tăng trưởng | |
| **Differentiated** | Khác biệt hóa | |
| **Dominant** | Thống trị | |
| **Disruptive** | Đột phá | |

---

## 📚 FURTHER LEARNING

### Recommended Reading Order

1. **This skill file** (you are here) - 2-3 hours
2. **Apply to simple product** (Training Grenade) - 4-6 hours
3. **Apply to complex product** (RCWS-127-NAVAL) - 8-10 hours
4. **Integration with Task Clarification** - 2-3 hours
5. **Full ODI project** (real defense system) - 20-30 hours

### Practice Exercises

**Exercise Beginner:** For "Training Grenade":
1. Define job executor
2. Write job statement
3. Create Universal Job Map (8 steps)
4. Write 20 outcome statements (at least 2 per job step)

**Exercise Intermediate:** For "MANPADS Trainer":
1. Complete Steps 1-4 (foundation)
2. Design survey instrument
3. Simulate 10 responses (make realistic data)
4. Calculate opportunity scores

**Exercise Advanced:** For "Target USV":
1. Complete full ODI process (Steps 1-10)
2. Identify 3 segments
3. Select growth strategy for each
4. Create customer scorecard for top concept

---

## ✅ MASTERY CHECKLIST

### Level 1: Awareness (Can explain)
- [ ] Can explain ODI in 60 seconds
- [ ] Can distinguish job executor from decision-maker
- [ ] Can write outcome statement in D-I-M format
- [ ] Can explain opportunity algorithm

### Level 2: Application (Can do with guidance)
- [ ] Can define job executor for a defense product
- [ ] Can create Universal Job Map (8 steps)
- [ ] Can write 20+ outcome statements
- [ ] Can calculate opportunity scores from survey data

### Level 3: Proficiency (Can do independently)
- [ ] Can conduct complete ODI Steps 1-7 for a product
- [ ] Can design and field survey
- [ ] Can identify outcome-based segments
- [ ] Can integrate ODI with Pahl & Beitz requirements list

### Level 4: Expertise (Can teach and lead)
- [ ] Can facilitate ODI workshop with stakeholders
- [ ] Can complete Steps 1-10 for complex defense system
- [ ] Can defend growth strategy selection to management
- [ ] Can mentor others in ODI application

---

## 🔄 UPDATES & VERSION

**Version:** 1.0
**Created:** 2026-02-03
**Last Updated:** 2026-02-03
**Next Review:** 2026-05-03 (quarterly)

**Changelog:**
- v1.0: Initial creation with 10-step process, defense examples, integration with P&B

---

**Related Skills:**
- [[SKILL_task_clarification|Task Clarification]] - ODI feeds into requirements list
- [[SKILL_conceptual_design|Conceptual Design]] - ODI weights VDI 2225 criteria
- [[SKILL_systems_thinking|Systems Thinking]] - Understand why innovation fails
- [[SKILL_dmir_learning|D-M-I-R Learning]] - ODI as part of diagnosis phase

**Navigation:**
- ← Previous: [[SKILL_overview|Overview]]
- → Next: Apply ODI to your project, then proceed to [[SKILL_task_clarification|Task Clarification]]

---

*This skill is part of the Engineering Design System for Vietnamese defense product development, integrating Pahl & Beitz systematic design with Outcome-Driven Innovation methodology.*
