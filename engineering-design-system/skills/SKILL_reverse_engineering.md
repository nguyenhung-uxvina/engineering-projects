# SKILL: Reverse Engineering Foreign Military Systems
## Systematic Methodology for Understanding Design Intent

**Skill ID:** SKILL_reverse_engineering
**Difficulty:** ⭐⭐⭐⭐⭐ (Expert)
**Time to Master:** 40-60 hours
**Prerequisites:** SKILL_conceptual_design, SKILL_systems_thinking
**Integration:** Feeds into Conceptual Design (Phase 2) via function structure
**Commands:** `/re`, `/recon`, `/decompose`, `/reconstruct`, `/paradigm`, `/compare-foreign`

---

## ⌨️ SLASH COMMANDS

| Command | Aliases | Purpose |
|---------|---------|---------|
| `/re` | `/reverse`, `/reverseeng` | Start reverse engineering workflow |
| `/recon` | `/reconnaissance` | Phase 1: System reconnaissance & documentation |
| `/decompose` | `/disassemble` | Phase 2: Subsystem decomposition |
| `/reconstruct` | `/functions` | Phase 3: Function structure reconstruction |
| `/paradigm` | `/philosophy` | Identify design paradigm & trade-offs |
| `/compare-foreign` | `/benchmark` | Compare foreign vs indigenous solutions |
| `/re-report` | `/rereport` | Generate RE analysis report |

### Command Output Templates

**`/re <system>`** → Full reverse engineering workflow:
```markdown
## REVERSE ENGINEERING ANALYSIS - [SYSTEM NAME]

### System Identification
- **Designation**: [Foreign designation]
- **Origin**: [Country/manufacturer]
- **Specimen**: [Condition, completeness]
- **Analysis Date**: [Date]

### Phase 1: Reconnaissance
[External documentation checklist]

### Phase 2: Decomposition
[Subsystem breakdown]

### Phase 3: Function Reconstruction
[Function structure diagram]

### Phase 4: Application
[Recommendations]
```

**`/recon`** → System reconnaissance template:
```markdown
## LEVEL 1: External Observation (Non-destructive)
- [ ] Overall dimensions (L×W×H): ___mm × ___mm × ___mm
- [ ] Mass: ___kg
- [ ] Mounting interfaces: [Describe]
- [ ] External connectors: [List type, count]
- [ ] Visible materials: [List]
- [ ] Surface treatments: [Anodize, paint, coating]
- [ ] Markings/labels: [CRITICAL - photograph all]
- [ ] Part numbers: [List]
- [ ] Operational controls: [List]

## LEVEL 2: Subsystem Decomposition
| Assembly | Interface | Fasteners | Notes |
|----------|-----------|-----------|-------|
| | | | |

## LEVEL 3: Component Analysis
| Component | Material | Manufacturing | Wear Pattern |
|-----------|----------|---------------|--------------|
| | | | |
```

**`/reconstruct`** → Function structure reconstruction:
```markdown
## FUNCTION STRUCTURE RECONSTRUCTION

### Energy/Material/Signal Flow Analysis
| Component | Input | Output | Transformation |
|-----------|-------|--------|----------------|
| | | | |

### Function Hierarchy
```
OVERALL FUNCTION: [Statement]
├── F1: [Main function 1]
│   ├── F1.1: [Subfunction] → [Working Principle]
│   └── F1.2: [Subfunction] → [Working Principle]
├── F2: [Main function 2]
│   └── ...
└── F_AUX: Support Functions
    └── ...
```

### Working Principle Mapping
| Subfunction | Physical Effect | Form Design | Working Principle |
|-------------|-----------------|-------------|-------------------|
| | | | |
```

**`/paradigm`** → Design philosophy assessment:
```markdown
## DESIGN PARADIGM ANALYSIS

### Observed Indicators
| Indicator | Observation | Reveals |
|-----------|-------------|---------|
| Safety margins | [High/Normal/Low] | Risk tolerance |
| Modularity | [High/Medium/Low] | Maintenance philosophy |
| Material selection | [Premium/Standard/Economy] | Cost vs performance |
| Redundancy | [Triple/Dual/None] | Mission criticality |
| Manufacturing | [Precision/Standard/Basic] | Production volume |

### Designer's Paradigm Statement
> "[Inferred design philosophy in one sentence]"

### Trade-off Pattern
[What was prioritized over what?]
```

**`/compare-foreign`** → Foreign vs indigenous comparison:
```markdown
## PARALLEL FUNCTION COMPARISON

| Function | Foreign Solution | Indigenous Option | Gap |
|----------|------------------|-------------------|-----|
| F1: | | | |
| F2: | | | |

### Technology Insertion Candidates
| Function | Foreign WP | Feasibility | Recommendation |
|----------|------------|-------------|----------------|
| | | | |
```

---

## 🎯 WHAT IS REVERSE ENGINEERING?

**Reverse engineering is NOT simply disassembly—it is reconstructing the design decisions that led to the physical manifestation.**

### Forward vs Reverse Engineering

```
FORWARD ENGINEERING:
Requirements → Functions → Working Principles → Structure → Physical Form

REVERSE ENGINEERING (Inverse):
Physical Form → Structure → Working Principles → Functions → Requirements
```

### The Key Question at Each Layer

| Layer | Forward Question | Reverse Question |
|-------|------------------|------------------|
| Physical Form | "How do we build this?" | "What exactly IS this?" |
| Structure | "How should we organize?" | "How is this organized?" |
| Working Principles | "What effect should we use?" | "Why does this work?" |
| Functions | "What must it do?" | "What does this accomplish?" |
| Requirements | "What problem to solve?" | "What problem was the designer solving?" |

---

## 📋 WHEN TO USE THIS SKILL

### Use Reverse Engineering When:
✅ Analyzing captured/procured foreign equipment
✅ Developing indigenous alternatives to imports
✅ Creating counter-system capabilities
✅ Benchmarking against foreign solutions
✅ Technology insertion from foreign designs
✅ Understanding competitor approaches

### RE Phase in Design Process

```
FOREIGN SYSTEM AVAILABLE
        ↓
┌────────────────────────┐
│  REVERSE ENGINEERING   │ ← YOU ARE HERE
│  (This Skill)          │
│  Extract functions     │
│  Identify principles   │
└───────────┬────────────┘
            ↓
┌────────────────────────┐
│  CONCEPTUAL DESIGN     │ ← Function structure feeds here
│  (Pahl & Beitz Phase 2)│
│  Morphological matrix  │
│  Alternative search    │
└───────────┬────────────┘
            ↓
┌────────────────────────┐
│  INDIGENOUS DESIGN     │ ← VDI 2225 evaluation
│  Own working principles│
└────────────────────────┘
```

---

## 🔟 THE 4-PHASE RE PROCESS (D-M-I-R Aligned)

### Overview Map

```
DIAGNOSIS (D)              MODELING (M)              INTERVENTION (I)         REFLECTION (R)
Phase 1: Recon             Phase 2: Decompose        Phase 3: Apply           Phase 4: Learn
┌──────────────────┐       ┌──────────────────┐      ┌──────────────────┐     ┌──────────────────┐
│ • System bounds  │       │ • Function       │      │ • Replication    │     │ • Documentation  │
│ • External doc   │──────▶│   structure      │─────▶│ • Counter-system │────▶│ • After-action   │
│ • Paradigm ID    │       │ • Working        │      │ • Tech insertion │     │ • Capability     │
│ • Multi-level    │       │   principles     │      │ • Alternatives   │     │   building       │
└──────────────────┘       └──────────────────┘      └──────────────────┘     └──────────────────┘
```

---

## 📖 PHASE 1: DIAGNOSIS — System Reconnaissance

### 1.1 Establish System Boundaries

Before any disassembly, define:

| Boundary Question | Example (RCWS) |
|-------------------|----------------|
| What is the system? | Remote Weapon Station |
| What is the supersystem? | Combat vehicle platform |
| What are sibling systems? | M151 Protector, CROWS, BPPU |
| What is the operational context? | Mounted patrol, convoy protection |

### 1.2 Multi-Level Documentation

**Level 1 — External Observation (Non-destructive)**
- Overall dimensions, mass, mounting interfaces
- External connectors (electrical, hydraulic, pneumatic)
- Visible materials and surface treatments
- **Markings, labels, part numbers** (CRITICAL intelligence)
- Operational controls and displays

**Level 2 — Subsystem Decomposition**
- Major assembly breakdown
- Interface documentation between assemblies
- Cable/harness routing
- Fastener types and torque markings
- Seal types and lubrication points

**Level 3 — Component Analysis**
- Individual part examination
- Material identification (spectrometry if available)
- Manufacturing process signatures
- Wear patterns indicating operating conditions
- Design features revealing performance intent

### 1.3 Pattern Recognition: Identify Design Paradigm

**Design Paradigm Indicators:**

| Indicator | What It Reveals |
|-----------|-----------------|
| **Safety margins** | Risk tolerance, reliability philosophy |
| **Modularity level** | Maintenance philosophy, upgrade intent |
| **Material selection** | Cost vs. performance priorities |
| **Manufacturing signatures** | Production volume, technological capability |
| **Redundancy patterns** | Mission criticality assessment |

---

## 📖 PHASE 2: MODELING — Functional Reconstruction

### 2.1 Energy/Material/Signal Flow Analysis

For each component, ask:
- What **energy** enters? What form? (Mechanical, electrical, thermal, chemical)
- What **material** passes through? (Solids, fluids, gases)
- What **signals** are processed? (Electrical, optical, acoustic)

### 2.2 Input-Output Transformation Mapping

| Component | Input | Output | Transformation |
|-----------|-------|--------|----------------|
| Gyroscope | Angular motion | Electrical signal | Sense angular rate |
| Servo motor | Electrical + command | Mechanical rotation | Convert & amplify |
| Barrel assembly | Propellant energy | Projectile KE | Channel & direct |

### 2.3 Construct Subfunction Hierarchy

Build from bottom up using **generally valid functions**:

| Function Type | Examples |
|---------------|----------|
| **Convert** | Energy type A → type B |
| **Store** | Accumulate over time |
| **Transmit** | Move through space |
| **Increase/Decrease** | Change magnitude |
| **Connect/Separate** | Material handling |
| **Channel** | Guide flow |
| **Sense** | Information acquisition |
| **Process** | Signal transformation |

### 2.4 Working Principle Identification

| Subfunction | Physical Effect | Form Design | Working Principle |
|-------------|-----------------|-------------|-------------------|
| Sense angular rate | Coriolis force | MEMS structure | MEMS gyroscope |
| Convert elec→mech | Electromagnetic induction | PM + stator | Brushless DC motor |
| Stabilize pointing | Feedback control | PID algorithm | Gyro-stabilized servo |

---

## 📖 PHASE 3: INTERVENTION — Knowledge Application

### 3.1 Leverage Point Analysis

Map discoveries to Meadows' Leverage Points:

| Leverage Level | Discovery Type | Action |
|----------------|---------------|--------|
| **L2: Paradigm** | Design philosophy | Evaluate if paradigm suits YOUR requirements |
| **L3: Goals** | Performance targets | Compare to your requirements |
| **L5: Rules** | Design rules, safety margins | Adopt or adapt |
| **L6: Information** | Sensor types, feedback signals | Key to matching performance |
| **L7: R-loops** | Self-improving features | Understand why system excels |
| **L8: B-loops** | Safety/limiting mechanisms | Critical for safe operation |
| **L10: Structure** | Physical architecture | Foundation for reproduction |

### 3.2 Application Strategies

**Strategy A: Functional Replication (Indigenous Alternative)**

1. Extract function structure (complete)
2. Identify working principles at each node
3. Search for alternative working principles achievable with local capability
4. Reconstruct using morphological matrix
5. Evaluate alternatives per VDI 2225

**Strategy B: Counter-System Development**

1. Identify critical feedback loops (B-loops that maintain performance)
2. Find ways to disrupt information flows (L6)
3. Identify structural vulnerabilities (L10)
4. Attack buffers/delays (L9, L11)

**Strategy C: Technology Insertion/Improvement**

1. Parallel function structure comparison (foreign vs. indigenous)
2. Identify functions where foreign solution has superior performance
3. Analyze working principle differences
4. Evaluate feasibility of adopting specific working principles

---

## 📖 PHASE 4: REFLECTION — Meta-Learning

### 4.1 RE Report Structure

```markdown
# FOREIGN SYSTEM ANALYSIS REPORT

## 1. SYSTEM IDENTIFICATION
- Designation, origin, variant
- Date of analysis, specimen condition
- Documentation completeness level

## 2. EXTERNAL CHARACTERIZATION
- Dimensional data
- Interface specifications
- Environmental ratings (observed/marked)

## 3. FUNCTIONAL RECONSTRUCTION
- Overall function statement
- Function structure diagram
- Energy/material/signal flow analysis

## 4. WORKING PRINCIPLE CATALOG
- Subfunction → Physical effect → Form design mapping
- Comparison with design catalogues
- Novel/unexpected solutions noted

## 5. PERFORMANCE ESTIMATION
- Derived specifications
- Confidence levels
- Validation requirements

## 6. DESIGN PHILOSOPHY ASSESSMENT
- Observed paradigms
- Trade-off patterns
- Quality/cost balance

## 7. APPLICATION RECOMMENDATIONS
- Replication feasibility
- Counter-system opportunities
- Technology insertion candidates

## 8. LESSONS LEARNED
- Process improvements
- Capability gaps identified
- Training needs
```

### 4.2 After-Action Review Questions

| Question | Purpose |
|----------|---------|
| What function structure elements were hardest to reconstruct? | Identify analytical gaps |
| Which working principles were unknown to our team? | Training needs |
| What manufacturing processes couldn't we identify? | Technology gaps |
| Where did our initial hypotheses prove wrong? | Mental model correction |
| What would we do differently next time? | Process improvement |

---

## 🔗 INTEGRATION WITH PAHL & BEITZ

### RE Feeds Into Conceptual Design

```markdown
## Phase 2 Morphological Matrix (with RE input)

| Subfunction | Foreign WP | Alt 1 (Local) | Alt 2 (Local) | Alt 3 |
|-------------|------------|---------------|---------------|-------|
| F1.1 Sense target | [From RE] | [Local option] | [Local option] | |
| F1.2 Track target | [From RE] | [Local option] | [Local option] | |
```

**Key Benefit:** RE provides proven working principles that can be used as one column in morphological matrix, while local alternatives are explored in parallel.

---

## 🛠️ TEMPLATES

### Template 1: System Reconnaissance Checklist

```markdown
## SYSTEM: _______________
## DATE: _______________
## ANALYST: _______________

### LEVEL 1: External (Non-destructive)
- [ ] Photographs (all sides, markings, labels)
- [ ] Dimensions: L___×W___×H___ mm
- [ ] Mass: ___ kg
- [ ] Mounting interface: _______________
- [ ] Connectors:
  - [ ] Electrical: _______________
  - [ ] Hydraulic: _______________
  - [ ] Pneumatic: _______________
- [ ] Materials visible: _______________
- [ ] Surface treatment: _______________
- [ ] Part numbers found: _______________
- [ ] Country of origin indicators: _______________

### LEVEL 2: Subsystem
| Assembly | Mass | Interface | Fasteners | Notes |
|----------|------|-----------|-----------|-------|
| | | | | |

### LEVEL 3: Component
| Component | Material | Mfg Process | Wear | Function Hypothesis |
|-----------|----------|-------------|------|---------------------|
| | | | | |
```

### Template 2: Function Structure Extraction

```markdown
## FUNCTION STRUCTURE: [SYSTEM NAME]

### Overall Function
> "[Verb] + [object] + [context]"

### Main Functions
F1: _______________
F2: _______________
F3: _______________
F_AUX: Support

### Subfunction Decomposition
| ID | Subfunction | Input | Output | Physical Effect | Component |
|----|-------------|-------|--------|-----------------|-----------|
| F1.1 | | | | | |
| F1.2 | | | | | |

### Function Structure Diagram
```
OVERALL: _______________
├── F1: _______________
│   ├── F1.1: ___________ → [WP: ___________]
│   └── F1.2: ___________ → [WP: ___________]
├── F2: _______________
│   └── ...
└── F_AUX: Support
    └── ...
```
```

### Template 3: Paradigm Assessment

```markdown
## DESIGN PARADIGM ASSESSMENT: [SYSTEM]

### Indicator Analysis
| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| Safety margins | | | |
| Modularity | | | |
| Material grade | | | |
| Redundancy | | | |
| Manufacturing precision | | | |

### Inferred Paradigm
**Primary Focus:** [ ] Performance [ ] Cost [ ] Reliability [ ] Maintainability
**Secondary Focus:** _______________

### Trade-off Statement
> "The designer prioritized ___ over ___ because ___"

### Applicability to Our Context
- [ ] Paradigm matches our requirements
- [ ] Partial match - adapt needed
- [ ] Paradigm mismatch - original design preferred
```

---

## ⚠️ COMMON PITFALLS

### Pitfall 1: Copying Without Understanding

**Wrong:** "Let's just copy the dimensions exactly"
**Right:** "Let's understand WHY these dimensions, then decide if they're right for us"

### Pitfall 2: Ignoring Paradigm Mismatch

**Wrong:** "Foreign system uses titanium, so should we"
**Right:** "Foreign system uses titanium because they prioritize weight over cost. Our requirements prioritize cost—aluminum may be acceptable."

### Pitfall 3: Missing Hidden Functions

**Wrong:** Documenting only obvious functions
**Right:** Looking for hidden functions (thermal management, EMI shielding, tamper evidence)

### Pitfall 4: Assuming Manufacturing Equivalence

**Wrong:** "We can make this part"
**Right:** "Can we achieve the same tolerances and material properties with available processes?"

---

## 🇻🇳 VIETNAMESE TERMINOLOGY

| English | Vietnamese | Notes |
|---------|------------|-------|
| Reverse Engineering | Kỹ thuật đảo ngược | |
| Function Structure | Cấu trúc chức năng | |
| Working Principle | Nguyên lý hoạt động | |
| Design Paradigm | Mô hình thiết kế | |
| Physical Effect | Hiệu ứng vật lý | |
| Subsystem | Hệ thống con | |
| Decomposition | Phân tách | |
| Reconnaissance | Trinh sát | Military term |
| Counter-system | Hệ thống đối kháng | |

---

## ✅ MASTERY CHECKLIST

### Level 1: Awareness (Can explain)
- [ ] Can explain difference between forward and reverse engineering
- [ ] Can describe 4-phase RE process
- [ ] Understands function structure concept
- [ ] Knows what working principles are

### Level 2: Application (Can do with guidance)
- [ ] Can complete Level 1 external documentation
- [ ] Can identify major subsystems
- [ ] Can hypothesize function structure
- [ ] Can identify obvious working principles

### Level 3: Proficiency (Can do independently)
- [ ] Can complete full 3-level documentation
- [ ] Can reconstruct complete function structure
- [ ] Can identify working principles with physical effects
- [ ] Can assess design paradigm

### Level 4: Expertise (Can teach and innovate)
- [ ] Can generate indigenous alternatives via morphological matrix
- [ ] Can identify counter-system opportunities
- [ ] Can recommend technology insertion points
- [ ] Can train others in RE methodology

---

## 📚 REFERENCE DOCUMENT

**Primary Reference:** [[Reverse Engineering Foreign Military Systems]]
- Location: `vault/references/Reverse Engineering Foreign Military Systems.md`
- Contains detailed D-M-I-R session with examples
- RCWS function structure example
- LOMAH practical exercise

---

## 🔄 UPDATES & VERSION

**Version:** 1.0
**Created:** 2026-02-04
**Last Updated:** 2026-02-04
**Next Review:** 2026-05-04 (quarterly)

**Changelog:**
- v1.0: Initial creation from reference document

---

**Related Skills:**
- [[SKILL_conceptual_design|Conceptual Design]] - RE function structure feeds into morphological matrix
- [[SKILL_systems_thinking|Systems Thinking]] - Leverage point analysis for counter-systems
- [[SKILL_task_clarification|Task Clarification]] - RE-derived requirements
- [[SKILL_dmir_learning|D-M-I-R Learning]] - RE as diagnosis phase

**Navigation:**
- ← Previous: [[SKILL_dfx_guidelines|DfX Guidelines]]
- → Next: Apply RE to foreign system, then proceed to [[SKILL_conceptual_design|Conceptual Design]]

---

*This skill is part of the Engineering Design System for Vietnamese defense product development, enabling systematic analysis of foreign military systems for indigenous capability development.*
