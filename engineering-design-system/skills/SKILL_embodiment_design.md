# 🔧 PHASE 3: EMBODIMENT DESIGN
## Comprehensive Skill Guide - Transform Concept to Definitive Layout

**Skill ID:** SKILL_embodiment_design
**Difficulty:** ⭐⭐⭐⭐ (Advanced)
**Time to Master:** 30-40 hours
**Prerequisites:** SKILL_conceptual_design completed, selected concept validated
**Integration:** Works with SKILL_dfx_guidelines, SKILL_systems_thinking
**Commands:** `/layout`, `/dfx`, `/mat`, `/tol`, `/lc`

---

## ⌨️ SLASH COMMANDS

| Command | Aliases | Purpose |
|---------|---------|---------|
| `/layout` | `/thietke` | Design layout with basic rules |
| `/dfx [type]` | `/dfm`, `/dfa` | DfX review (M/A/T/S) |
| `/materials` | `/mat`, `/chonvatlieu` | Material selection matrix |
| `/tolerances` | `/tol` | Tolerance stack-up analysis |
| `/local-content` | `/lc` | Calculate local content % |

### Command Output Templates

**`/layout`** → Design rules compliance:
```markdown
| Rule | Status | Evidence |
|------|--------|----------|
| Clarity | ✅ | Single function per component |
| Simplicity | ✅ | Reduced to 8 parts |
| Safety | ⚠️ | Add pinch guard |
```

**`/dfx`** → DfX review summary:
```markdown
| Type | Score | Status |
|------|-------|--------|
| DfM | 85% | ✅ Pass |
| DfA | 72% | ⚠️ Needs work |
```

**`/materials`** → Selection matrix:
```markdown
| Material | Strength | Cost | Local | Score |
|----------|----------|------|-------|-------|
| SS 304 | 3 | 3 | ✅ | 2.95 |
| Al 6061 | 2 | 4 | ⚠️ | 2.80 |
```

**`/local-content`** → Local content analysis:
```markdown
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| By Cost | 58% | 60% | ⚠️ |
| By Count | 72% | 60% | ✅ |
```

---

## 🎯 PHASE 3 OBJECTIVES

Transform **Selected Concept** → **Definitive Layout** with:
- Dimensions and tolerances specified
- Materials selected and justified
- **12 DfX categories applied** (see SKILL_dfx_guidelines)
- Manufacturing methods defined
- Standards compliance verified
- Systems thinking applied (virtuous cycles strengthened)

**Duration**: 35-40% of total project
**Output**: Definitive Layout + Production Method Outline + DfX Documentation

---

## 📖 TWO APPROACHES TO EMBODIMENT DESIGN

### Approach 1: 7-Step Simplified (Original)
**Best for:** Small projects, simple products, tight timelines
**Coverage:** ~70% of embodiment design knowledge

### Approach 2: 15-Step RISM-PRAD-DECS-OCP (Comprehensive)
**Best for:** Complex defense systems, rigorous methodology required
**Coverage:** ~95% of embodiment design knowledge, includes meta-learning

**Choose based on project complexity and rigor requirements.**

---

## 🔷 APPROACH 1: 7-STEP SIMPLIFIED PROCESS

### Step 1: IDENTIFY EMBODIMENT-DETERMINING REQUIREMENTS

**Extract from Requirements List (Phase 1)**:
```
┌─────────────────────────────────────────────────────────┐
│ EMBODIMENT-DETERMINING REQUIREMENTS                     │
├─────────────────────────────────────────────────────────┤
│ SIZE & SPACE:                                           │
│   - Max envelope dimensions                             │
│   - Weight limits                                       │
│   - Mounting interfaces                                 │
│                                                         │
│ FORCES & LOADS:                                         │
│   - Operating loads (static, dynamic)                   │
│   - Shock & vibration (MIL-STD-810H)                    │
│   - Safety factors by criticality                       │
│                                                         │
│ ENVIRONMENTAL:                                          │
│   - Temperature range (-X to +Y °C)                     │
│   - Humidity, salt spray, dust                          │
│   - IP rating (IP65, IP67)                              │
│                                                         │
│ INTERFACES:                                             │
│   - Mechanical connections (bolts, welds)               │
│   - Electrical connectors (type, sealing)               │
│   - Fluid ports (if applicable)                         │
│                                                         │
│ PERFORMANCE CONSTRAINTS:                                │
│   - Accuracy/precision (tolerances)                     │
│   - Speed/response (latency, bandwidth)                 │
│   - Thermal management (max component temps)            │
└─────────────────────────────────────────────────────────┘
```

**Systems Thinking Integration:**
- Identify feedback-sensitive requirements (e.g., cooling affects performance)
- Note delays that could destabilize system (L9 leverage point)

---

### Step 2: APPLY BASIC RULES

**4 Fundamental Rules of Embodiment Design**:

```
┌─────────────────────────────────────────────────────────┐
│ RULE 1: CLARITY (Rõ ràng)                               │
│ ─────────────────────────────────────────               │
│ • Every function must be clear and unambiguous           │
│ • Avoid "hidden failures"                                │
│ • Load paths easy to trace                               │
│                                                         │
│ Example: Bearing mount - clearly shows radial vs        │
│ axial load paths. Design makes function explicit.       │
├─────────────────────────────────────────────────────────┤
│ RULE 2: SIMPLICITY (Đơn giản)                           │
│ ─────────────────────────────────────────               │
│ • Minimum number of parts (DfA principle)                │
│ • Reduce feature count                                   │
│ • Fewer interfaces = fewer failure modes                 │
│                                                         │
│ Example: One investment casting vs 5 machined parts     │
│ welded - evaluate part count reduction                  │
├─────────────────────────────────────────────────────────┤
│ RULE 3: SAFETY (An toàn)                                │
│ ─────────────────────────────────────────               │
│ • Fail-safe design (spring to safe position)            │
│ • Redundancy for critical functions                      │
│ • Clear indication of failures (BIT, indicators)         │
│                                                         │
│ Hierarchy: Safe-life → Fail-safe → Redundant            │
│ (See SKILL_dfx_guidelines DfX#11: Safety)                │
├─────────────────────────────────────────────────────────┤
│ RULE 4: ECONOMY (Kinh tế)                               │
│ ─────────────────────────────────────────               │
│ • Right material for function (not overkill)             │
│ • Consider full lifecycle cost (TCO)                     │
│ • Manufacturing method appropriate to volume             │
│                                                         │
│ Defense target: 60-70% of import equivalent cost        │
└─────────────────────────────────────────────────────────┘
```

---

### Step 3: APPLY DESIGN PRINCIPLES

**Key Principles for Defense Products**:

| Principle | Description | Application |
|-----------|-------------|-------------|
| **Task Division** | Each component has one clear function | Modularity for maintenance (DfX#9) |
| **Self-Help** | Parts self-centering, self-locking | Reduce assembly errors (DfX#8) |
| **Stability** | Preferred stable configurations | Resist vibration (DfX#1) |
| **Bi-stability** | Definite ON/OFF states | Safety interlocks (DfX#11) |
| **Force Transmission** | Short, direct load paths | Structural efficiency |
| **Matched Deformations** | Compatible deformation patterns | Prevent stress concentration |
| **Force Balance** | Minimize reaction forces | Reduce bearing loads (DfX#4 Wear) |
| **Fault-Free** | Design out failure modes | FMEA + Systems Thinking |

**Systems Thinking Connection:**
- Each principle creates balancing loops (self-correcting)
- Self-help = L8 (strengthen negative feedback)
- Bi-stability = L5 (rules that enforce states)

---

### Step 4: APPLY DfX GUIDELINES

**IMPORTANT:** This step now references comprehensive **SKILL_dfx_guidelines.md**

**Quick DfX Priority Selection:**

1. **Identify product type** (naval, infantry, training, UAV, etc.)
2. **Load SKILL_dfx_guidelines.md**
3. **Use priority matrix** to rank 12 DfX categories
4. **Apply top 5 priority categories** with full checklists

**12 DfX Categories** (see SKILL_dfx_guidelines for details):
```
DESIGN PHASE:
1. DfX#1: Durability (shock, vibration, environmental)
2. DfX#2: Thermal Management (heat dissipation)
3. DfX#3: Corrosion Resistance (marine/tropical)
4. DfX#4: Wear Resistance (moving parts)

PRODUCTION:
5. DfX#5: Ergonomics (human factors)
6. DfX#6: Aesthetics (professional appearance)
7. DfX#7: Production (manufacturing ease)
8. DfX#8: Assembly (assembly speed, mistake-proofing)

OPERATIONAL:
9. DfX#9: Maintenance (MTTR, accessibility)
10. DfX#10: Recycling (end-of-life)

CROSS-CUTTING:
11. DfX#11: Safety (hazard elimination)
12. DfX#12: Standards Compliance (MIL-STD, TCVN)
```

**Action:** For each priority category, complete the Phase 3 design review checklist from SKILL_dfx_guidelines.

---

### Step 5: DEVELOP LAYOUT VARIANTS

**Layout Development Process**:

```
Preliminary Layout (rough sketches)
       │
       ├─── Variant A: [Approach 1]
       ├─── Variant B: [Approach 2]
       └─── Variant C: [Approach 3]
              │
              ▼
       Evaluate variants
       (simplified VDI 2225 + Systems Thinking)
       - Leverage point analysis (which variant enables L6-L9?)
       - Feedback loop analysis (which creates virtuous cycles?)
              │
              ▼
       Selected Layout
              │
              ▼
       Definitive Layout
       (scale drawings, dimensions, tolerances)
```

**Layout Documentation Template:**
```markdown
## LAYOUT VARIANT [X]

### Overall Arrangement
[Description or drawing reference]

### Key Dimensions
- Overall: L × W × H = [values] mm
- Weight estimate: [kg]
- Envelope check vs requirements: [PASS/FAIL]

### Component Arrangement
1. [Component 1]: Location, orientation, mounting method
2. [Component 2]: Location, orientation, mounting method
[...]

### Interface Points
- Mechanical: [Bolt patterns, welds, fasteners]
- Electrical: [Connector types, locations, EMC considerations]
- Thermal: [Heat dissipation approach, airflow paths]

### DfX Assessment Summary
| Category | Status | Notes |
|----------|--------|-------|
| Durability | ✅/⚠️/❌ | |
| Thermal | ✅/⚠️/❌ | |
| Corrosion | ✅/⚠️/❌ | |
| [Priority categories] | | |

### Systems Analysis
- Feedback loops: [Identify any reinforcing or balancing loops]
- Leverage points: [What interventions does this layout enable?]

### Pros/Cons
+ [Advantage 1]
+ [Advantage 2]
- [Disadvantage 1]
- [Disadvantage 2]

### Estimated Cost: $[value]
```

---

### Step 6: MATERIAL SELECTION

**Material Selection Process** (integrates with DfX#1, #3, #4, #7):

```
1. Identify material requirements (DfX#1 Durability)
   - Strength, stiffness, fatigue
   - Environmental resistance (DfX#3 Corrosion)
   - Wear characteristics (DfX#4 Wear)

2. Screen available materials
   - Vietnamese suppliers (DfX#7 Production)
   - Standard vs special order
   - Lead times

3. Evaluate candidates
   - Material selection matrix (weighted scoring)
   - Cost analysis
   - Local content impact

4. Select and justify
   - Document rationale
   - Specify grade, form, heat treatment
```

**Material Selection Matrix**:

| Factor | Weight | Material A | Material B | Material C |
|--------|--------|------------|------------|------------|
| Strength/weight ratio | 0.20 | Score | Score | Score |
| Corrosion resistance | 0.15 | Score | Score | Score |
| Machinability (DfX#7) | 0.15 | Score | Score | Score |
| Local availability | 0.20 | Score | Score | Score |
| Cost | 0.20 | Score | Score | Score |
| Weldability | 0.10 | Score | Score | Score |
| **Weighted Score** | 1.00 | **Total** | **Total** | **Total** |

**Vietnamese Material Sources**:

| Material | Supplier | Grades | Notes |
|----------|----------|--------|-------|
| Structural steel | Nam Kim, Hòa Phát | A36, Q235 | Excellent availability |
| Aluminum alloy | Hòa Phát, imports | 6061, 7075 | Good availability |
| Stainless steel | Various | 304, 316, 316L | Marine-grade available |
| Engineering plastics | Import | Delrin, PEEK, UHMW-PE | For wear applications |
| Composites | Limited local | Carbon fiber, fiberglass | May need import for quality |

---

### Step 7: STANDARDS COMPLIANCE CHECK

**MIL-STD-810H Environmental Requirements**:

| Method | Test | Design Impact | DfX Reference |
|--------|------|---------------|--------------|
| 501 | High temp (+55°C+) | Material selection, ventilation | DfX#2 Thermal |
| 502 | Low temp (-40°C) | Cold-start, brittle fracture | DfX#1 Durability |
| 507 | Humidity (95% RH) | Sealing, coatings | DfX#3 Corrosion |
| 509 | Salt fog (marine) | Material, finish selection | DfX#3 Corrosion |
| 510 | Sand & dust | Sealing, filtration | DfX#1 Durability |
| 514 | Vibration | Mounting, natural frequency | DfX#1 Durability |
| 516 | Shock | Structural design, retention | DfX#1 Durability |

**MIL-STD-461G EMC Requirements** (if applicable):

| Requirement | Description | Design Impact | DfX Reference |
|-------------|-------------|---------------|--------------|
| RE102 | Radiated emissions | Shielding, filtering | DfX#12 Standards |
| RS103 | Radiated susceptibility | Shielding, grounding | DfX#12 Standards |
| CE106 | Conducted emissions | Filtering, isolation | DfX#12 Standards |

**Action:** For each applicable standard, document compliance approach and verification method.

---

## 🔶 APPROACH 2: 15-STEP RISM-PRAD-DECS-OCP PROCESS

**Comprehensive Embodiment Design Methodology**

This is the complete Pahl & Beitz Phase 7 process with meta-learning integration.

### Process Overview

```
RISM (Requirements & Material Foundation)
  R: Requirements identification
  I: Identify critical requirements
  S: Select preliminary materials
  M: Material analysis
          ↓
PRAD (Principles & Rules Application)
  P: Principles application
  R: Rules application
  A: Architecture definition
  D: Design structure
          ↓
DECS (Detail & Evaluation)
  D: Detail specification
  E: Evaluate variants
  C: Check against requirements
  S: Standards compliance
          ↓
OCP (Optimization & Production)
  O: Optimize design
  C: Cost analysis
  P: Production planning
```

---

### RISM: Requirements & Material Foundation

#### Step R: Requirements Identification

**Purpose:** Extract and organize all embodiment-determining requirements

**Process:**
1. Read Requirements List from Phase 1
2. Filter for embodiment-relevant requirements:
   - Geometric (size, shape, envelope)
   - Kinematic (motion, speed, positioning)
   - Force/load (static, dynamic, shock)
   - Material (strength, corrosion, weight)
   - Surface (finish, texture, appearance)
   - Safety (interlocks, fail-safe)

3. Organize by category (creates clarity)

**Output:** Embodiment Requirements Matrix

**Meta-Learning Skill Applied:** Categorization (mental model: hierarchical organization)

---

#### Step I: Identify Critical Requirements

**Purpose:** Prioritize requirements that most constrain the design

**Process:**
1. Rank requirements by constraint strength:
   - **Hard constraints:** MUST be met (safety, standards)
   - **Soft constraints:** WISH to meet (cost, weight goals)

2. Identify conflicting requirements:
   - Example: "Lightweight" vs "High durability"
   - Resolution approach: Trade-off analysis, leverage points

3. Map to ODI outcomes (if Phase 0 completed):
   - Link requirements to top customer outcomes
   - Weight by opportunity scores

**Output:** Prioritized Requirements List with conflicts identified

**Meta-Learning Skill Applied:** Prioritization + Constraint identification

**Systems Thinking Integration:**
- Conflicting requirements often indicate competing feedback loops
- Example: Cost reduction (R loop) vs Quality improvement (B loop)

---

#### Step S: Select Preliminary Materials

**Purpose:** Narrow material candidates early to guide form development

**Process:**
1. Screen by hard constraints:
   - Environmental (temp, corrosion, UV)
   - Mechanical (strength, stiffness, fatigue)
   - Manufacturing (weldability, machinability)

2. Screen by local availability (DfX#7):
   - Vietnamese suppliers inventory
   - Lead times, minimum order quantities

3. Create short list (3-5 candidates per component)

**Output:** Material Candidate Short List

**Meta-Learning Skill Applied:** Filtering + Satisficing

---

#### Step M: Material Analysis

**Purpose:** Detailed analysis of material candidates

**Process:**
1. **Property comparison:**
   - Mechanical properties (yield, ultimate, fatigue)
   - Physical properties (density, thermal conductivity)
   - Chemical properties (corrosion resistance)

2. **Cost analysis:**
   - Raw material cost ($/kg)
   - Processing cost (machining rates, welding)
   - Total cost per component

3. **Lifecycle analysis:**
   - Durability (DfX#1)
   - Maintenance (DfX#9)
   - Recycling (DfX#10)

**Output:** Material Selection Matrix (see Step 6 above for template)

**Meta-Learning Skill Applied:** Multi-criteria decision analysis

---

### PRAD: Principles & Rules Application

#### Step P: Principles Application

**Purpose:** Apply Pahl & Beitz design principles systematically

**Key Principles to Apply:**

1. **Force Flow Principle:**
   - Load paths short and direct
   - Minimize bending moments
   - Uniform stress distribution

2. **Division of Tasks:**
   - Each component has one clear function
   - Enables modularity (DfX#9)

3. **Self-Help:**
   - Self-centering (alignment features)
   - Self-locking (friction, detents)

4. **Stability:**
   - Preferred stable equilibrium
   - Avoid unstable balance points

5. **Direct vs Indirect Transmission:**
   - Direct: Simple, efficient
   - Indirect: Allows control, transformation

**Process:**
1. For each subsystem, identify applicable principles
2. Sketch preliminary layouts showing principle application
3. Document rationale

**Output:** Principle-Based Layout Sketches

**Meta-Learning Skill Applied:** Principle → Application transfer

---

#### Step R: Rules Application

**Purpose:** Apply the 4 Basic Rules systematically

**Process:**
1. **Clarity Check:**
   - Is every function explicitly visible in the design?
   - Can load paths be traced easily?
   - Are interfaces clearly defined?

2. **Simplicity Check:**
   - Part count justified? (Can parts be combined?)
   - Feature count minimized?
   - Interface count minimized?

3. **Safety Check:**
   - Fail-safe failure modes?
   - Redundancy where needed?
   - Clear failure indications?

4. **Economy Check:**
   - Overdesigned? (excessive safety factors?)
   - Manufacturing method optimal?
   - Lifecycle cost considered?

**Output:** Rules Compliance Matrix

**Meta-Learning Skill Applied:** Checklist-based verification

---

#### Step A: Architecture Definition

**Purpose:** Define overall system structure and subsystem breakdown

**Process:**
1. **Functional decomposition:**
   - Main functions (from Phase 2 function structure)
   - Sub-functions
   - Component-function mapping

2. **Physical architecture:**
   - Modules definition (mechanical, electrical, thermal)
   - Module interfaces (mechanical, electrical, thermal, data)
   - Assembly sequence (DfX#8)

3. **Information architecture:**
   - Sensor → Processor → Actuator flows
   - Data paths
   - Control loops (Systems Thinking: identify feedback)

**Output:** System Architecture Diagram + Interface Control Document (ICD)

**Meta-Learning Skill Applied:** Abstraction + Decomposition

**Systems Thinking Integration:**
- Architecture defines information flows (L6 leverage point)
- Module boundaries enable self-organization (L4 leverage point)

---

#### Step D: Design Structure

**Purpose:** Define detailed structural configuration

**Process:**
1. **Structural analysis:**
   - Load cases (static, dynamic, thermal)
   - Stress analysis (FEA if needed)
   - Deflection analysis
   - Natural frequency (vibration isolation)

2. **Form development:**
   - Shape optimization (reduce weight, increase stiffness)
   - Feature definition (ribs, gussets, lightening holes)
   - Fillet radii (stress concentration mitigation)

3. **Integration:**
   - How subsystems fit together
   - Routing (cables, fluids)
   - Access for assembly and maintenance

**Output:** Preliminary Structural Layout (dimensioned sketches)

**Meta-Learning Skill Applied:** Analysis → Synthesis

---

### DECS: Detail & Evaluation

#### Step D: Detail Specification

**Purpose:** Specify all dimensions, tolerances, and surface finishes

**Process:**
1. **Dimensional specification:**
   - Nominal dimensions
   - Tolerances (as loose as function allows)
   - Tolerance stack-up analysis (for critical chains)

2. **Surface specification:**
   - Roughness (Ra, Rz) - standard finishes preferred
   - Finish type (machined, polished, coated)
   - Special treatments (anodize, paint, plating)

3. **Interface specification:**
   - Mating part clearances/fits (H7/g6, etc.)
   - Fastener specifications (size, grade, torque)
   - Sealing specifications (O-rings, gaskets)

**Output:** Detailed Layout Drawing with Dimensions & Tolerances

**Meta-Learning Skill Applied:** Precision specification

**DfX Integration:**
- Loose tolerances → DfX#7 Production (lower cost)
- Standard finishes → DfX#7 Production (availability)
- Accessible fasteners → DfX#9 Maintenance

---

#### Step E: Evaluate Variants

**Purpose:** Systematically compare layout variants

**Process:**
1. **Develop 2-3 variants** (if not already done in Step 5)

2. **Evaluation criteria** (from requirements + DfX priorities):
   - Performance (meets requirements?)
   - DfX scores (top 5 priorities)
   - Cost estimate
   - Risk (technical, schedule, cost)
   - Local content %

3. **Scoring method:**
   - VDI 2225 weighted scoring
   - Weighted by ODI opportunity scores (if available)
   - Systems Thinking: Which variant enables higher leverage points?

**Output:** Variant Evaluation Matrix + Selected Layout

**Meta-Learning Skill Applied:** Multi-criteria evaluation

---

#### Step C: Check Against Requirements

**Purpose:** Verify selected layout satisfies all requirements

**Process:**
1. **Requirements traceability:**
   - For each requirement, identify design feature that satisfies it
   - For each design feature, identify requirement it addresses

2. **Gap analysis:**
   - Requirements not yet satisfied?
   - Design features not justified by requirements? (over-design)

3. **Verification method:**
   - Analysis (calculation, FEA)
   - Inspection (measurement, visual)
   - Demonstration (functional test)
   - Test (formal testing per procedure)

**Output:** Requirements Verification Matrix

**Meta-Learning Skill Applied:** Traceability + Verification

---

#### Step S: Standards Compliance

**Purpose:** Verify design meets all applicable standards

**Process:**
1. **Identify applicable standards** (from Phase 1):
   - MIL-STD-810H (environmental)
   - MIL-STD-461G (EMC)
   - MIL-STD-882E (safety)
   - MIL-STD-1472H (human factors)
   - TCVN (Vietnamese standards)

2. **Compliance mapping:**
   - For each standard section, identify design features that ensure compliance
   - Document compliance approach

3. **Test planning:**
   - Which tests required?
   - When to test? (prototype, production)
   - Pass/fail criteria

**Output:** Standards Compliance Matrix + Test Plan Outline

**Meta-Learning Skill Applied:** Regulatory mapping

**DfX Integration:** See SKILL_dfx_guidelines DfX#12: Standards Compliance

---

### OCP: Optimization & Production

#### Step O: Optimize Design

**Purpose:** Refine design for best performance/cost trade-off

**Process:**
1. **Performance optimization:**
   - Stress optimization (remove material where stress low)
   - Thermal optimization (improve cooling paths)
   - Weight optimization (material substitution, topology)

2. **Cost optimization:**
   - Part count reduction (consolidate parts)
   - Material optimization (cheaper alternative if adequate)
   - Manufacturing process optimization (casting vs machining)

3. **Leverage point optimization (Systems Thinking):**
   - Can we move from L12 (parameters) to L9 (delays)?
   - Can we strengthen feedback loops (L8)?
   - Can we add information flows (L6)?

**Output:** Optimized Layout + Optimization Rationale

**Meta-Learning Skill Applied:** Optimization heuristics

---

#### Step C: Cost Analysis

**Purpose:** Detailed cost estimation for production

**Process:**
1. **Material cost:**
   - Bill of Materials (BOM)
   - Raw material cost per item
   - Scrap rate

2. **Labor cost:**
   - Manufacturing hours (machining, welding, assembly)
   - Labor rate ($/hour)
   - Learning curve effect (quantity)

3. **Overhead:**
   - Tooling amortization
   - Quality control
   - Facility overhead

4. **Margin:**
   - Target margin %
   - Price to customer

**Output:** Detailed Cost Breakdown + Unit Cost Estimate

**Meta-Learning Skill Applied:** Cost modeling

---

#### Step P: Production Planning

**Purpose:** Define how product will be manufactured

**Process:**
1. **Manufacturing process selection:**
   - Machining, casting, welding, sheet metal, molding
   - Rationale for each choice

2. **Supplier identification:**
   - Local suppliers (DfX#7)
   - Import requirements
   - Lead times

3. **Quality control planning:**
   - Inspection points
   - Acceptance criteria
   - Workmanship standards (IPC-A-610 for electronics)

4. **Assembly sequence:**
   - Step-by-step assembly procedure
   - Tools required
   - Time estimate

**Output:** Production Plan + Supplier List + Assembly Instructions Draft

**Meta-Learning Skill Applied:** Process planning

---

## 📊 15-STEP META-LEARNING INTEGRATION

### 13 Meta-Learning Skills Applied in Embodiment Design

| Skill | Where Applied | Example |
|-------|--------------|---------|
| 1. Categorization | Step R: Requirements | Group by geometric, kinematic, force, material |
| 2. Prioritization | Step I: Critical Requirements | Rank by constraint strength |
| 3. Filtering | Step S: Material Selection | Screen by hard constraints |
| 4. Satisficing | Step S: Material Selection | "Good enough" > perfect |
| 5. Multi-criteria Decision | Step M: Material Analysis | Weighted scoring matrix |
| 6. Principle → Application | Step P: Principles | Force flow → direct load paths |
| 7. Checklist Verification | Step R: Rules Application | 4 basic rules compliance |
| 8. Abstraction | Step A: Architecture | Function → Module mapping |
| 9. Decomposition | Step A: Architecture | System → Subsystem → Component |
| 10. Analysis → Synthesis | Step D: Structure | FEA results → form optimization |
| 11. Precision Specification | Step D: Detail | Dimensions + tolerances |
| 12. Traceability | Step C: Check Requirements | Requirement ↔ Design feature |
| 13. Optimization Heuristics | Step O: Optimize | Remove material where stress low |

**Mastery Progression:**
- **Level 1 (Novice):** Apply skills with guidance (use checklists)
- **Level 2 (Apprentice):** Apply skills independently
- **Level 3 (Practitioner):** Adapt skills to novel situations
- **Level 4 (Expert):** Teach skills, create new heuristics

---

## 📋 LAYOUT DOCUMENTATION TEMPLATE

```markdown
# EMBODIMENT DESIGN - DEFINITIVE LAYOUT
## [Project Code]: [System Name]
### Version: [x.x] | Date: [YYYY-MM-DD]

---

## 1. LAYOUT OVERVIEW

### 1.1 Overall Dimensions
- Length: [mm] ± [tolerance]
- Width: [mm] ± [tolerance]
- Height: [mm] ± [tolerance]
- Weight: [kg] (target) / [kg] (current estimate)

### 1.2 Layout Drawing Reference
- Drawing number: [XXX-001]
- Scale: [1:X]
- Revision: [Rev]

### 1.3 Approach Used
- [ ] 7-Step Simplified (small/simple projects)
- [ ] 15-Step RISM-PRAD-DECS-OCP (complex/rigorous)

---

## 2. COMPONENT LIST (Preliminary BOM)

| Item | Description | Qty | Material | Source | Est. Cost |
|------|-------------|-----|----------|--------|-----------|
| 1 | | | | Local/Import | |
| 2 | | | | | |
[...]

### 2.1 Local Content Analysis
- Local components: [N] items, [X]% of cost
- Import components: [M] items, [Y]% of cost
- **Local content ratio: [Z]%** (target: 60-75%)

---

## 3. CRITICAL INTERFACES

### 3.1 Mechanical Interfaces
| Interface | Type | Specification | Drawing Ref |
|-----------|------|---------------|-------------|
| I-001 | Mounting | [Bolt pattern, load capacity] | |
| I-002 | Connection | [Type, size] | |

### 3.2 Electrical Interfaces
| Interface | Connector | Signals | Drawing Ref |
|-----------|-----------|---------|-------------|
| E-001 | MIL-DTL-38999 | Power, CAN | |

### 3.3 Thermal Interfaces
| Component | Heat Load | Dissipation Method | Max Temp |
|-----------|-----------|-------------------|----------|
| Processor | 15W | Heat sink + fan | 80°C |

---

## 4. DfX COMPLIANCE

**DfX Priorities for this Product:**
1. [Top priority category from SKILL_dfx_guidelines]
2. [Second priority]
3. [Third priority]
4. [Fourth priority]
5. [Fifth priority]

### 4.1 Top Priority DfX Category: [Name]
**Checklist Status:** [X/Y items completed]

| Criterion | Status | Notes |
|-----------|--------|-------|
| [Criterion 1] | ✅/⚠️/❌ | |
| [Criterion 2] | ✅/⚠️/❌ | |
[...]

[Repeat for each priority category]

**Action Items:**
- [ ] [Remaining DfX work item 1]
- [ ] [Remaining DfX work item 2]

---

## 5. SYSTEMS THINKING ANALYSIS

### 5.1 Feedback Loops Identified
| Loop | Type | Description | Impact on Design |
|------|------|-------------|------------------|
| R1 | Reinforcing | [Description] | [How design strengthens/weakens] |
| B1 | Balancing | [Description] | [How design utilizes] |

### 5.2 Leverage Points Applied
| Level | Intervention | Design Implementation |
|-------|-------------|----------------------|
| L6 | Information flow | [Added sensor feedback to operator] |
| L8 | Negative feedback | [Strengthened error correction loop] |
| L9 | Delay reduction | [Reduced sensor latency 100ms → 50ms] |

---

## 6. STANDARDS COMPLIANCE

### 6.1 MIL-STD-810H Compliance
| Method | Requirement | Design Feature | Verification | Status |
|--------|-------------|----------------|--------------|--------|
| 501/502 | -10 to +55°C | Material selection, thermal design | Analysis + Test | ⏳ |
| 509.7 | Salt fog 1000h | 316 SS, coatings | Test | ⏳ |
| 514.8 | Vibration | Mounting isolation | Test | ⏳ |
| 516.8 | Shock | Structural design | Analysis + Test | ⏳ |

### 6.2 Other Standards
| Standard | Section | Compliance Approach | Status |
|----------|---------|-------------------|--------|
| MIL-STD-461G | RE102 | Shielded enclosure | ⏳ |
| MIL-STD-882E | All | System safety analysis | ⏳ |

---

## 7. REQUIREMENTS VERIFICATION MATRIX

| Req ID | Requirement | Design Feature | Verification Method | Status |
|--------|-------------|----------------|-------------------|--------|
| R01 | [Requirement] | [Feature] | Analysis/Test/Inspection | ✅/⏳/❌ |
| R02 | | | | |
[...]

**Verification Summary:**
- Requirements verified: [X/Y] ([Z]%)
- Remaining: [List critical unverified requirements]

---

## 8. RISK ASSESSMENT

| Risk | Probability | Impact | Mitigation | Owner | Status |
|------|-------------|--------|------------|-------|--------|
| Thermal overheating | M | H | Add fan, oversized heat sink | [Name] | Open |
| Corrosion in testing | L | H | Multiple coating layers | [Name] | Closed |
[...]

---

## 9. COST ESTIMATE

### 9.1 Material Cost
| Item | Qty | Unit Cost | Total |
|------|-----|-----------|-------|
| [Material 1] | | | |
| **Subtotal** | | | **$[value]** |

### 9.2 Labor Cost
| Process | Hours | Rate | Total |
|---------|-------|------|-------|
| Machining | | $/hr | |
| Assembly | | $/hr | |
| **Subtotal** | | | **$[value]** |

### 9.3 Overhead & Margin
| Category | % | Amount |
|----------|---|--------|
| Overhead | 30% | |
| Margin | 20% | |

### 9.4 Unit Cost Summary
**Unit cost at lot size [N]:** $[value]
**Target cost:** $[value]
**Variance:** [+/-]%

---

## 10. APPROACH-SPECIFIC DOCUMENTATION

### If 7-Step Simplified:
**Simplifications Made:**
- [What was simplified or skipped]
- [Justification]

### If 15-Step RISM-PRAD-DECS-OCP:
**Meta-Learning Skills Applied:**
- Categorization: [Example]
- Prioritization: [Example]
- Multi-criteria Decision: [Example]
[...]

**Process Insights:**
- [What worked well]
- [What was challenging]
- [Improvements for next project]

---

## 11. GATE 3 CHECKLIST (Phase 3 → Phase 4 Transition)

**Must complete ALL items to proceed to Phase 4:**

- [ ] Definitive layout complete with dimensions
- [ ] All materials selected and justified
- [ ] Top 5 DfX priorities addressed (checklists complete)
- [ ] Standards compliance verified (analysis or test plan)
- [ ] Requirements verification matrix complete (≥80%)
- [ ] Preliminary cost estimate within target (+10% acceptable)
- [ ] Local content ≥60%
- [ ] All critical interfaces defined (ICDs created)
- [ ] Risks identified with mitigations
- [ ] Systems analysis complete (feedback loops, leverage points)
- [ ] Stakeholder review completed (design lead, manufacturing, quality)

**Gate 3 Status:** ⏳ In Progress / ✅ Ready for Phase 4

---

## 12. APPROVALS

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Design Lead | | | |
| Manufacturing Rep | | | |
| Quality Rep | | | |
| Systems Engineer | | | |

---

## 13. NEXT STEPS (Phase 4 Preview)

**Phase 4 Deliverables:**
- [ ] Complete production drawings (2D + 3D)
- [ ] Final BOM with part numbers
- [ ] Assembly instructions (step-by-step)
- [ ] Verification plan (detailed test procedures)
- [ ] Final cost analysis
- [ ] Production readiness review

**Estimated Phase 4 Duration:** [weeks/months]

---

*Embodiment Design determines HOW the product will be made. This is where concept becomes reality.*
```

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Ignoring manufacturing constraints** (DfX#7)
   - ❌ Design features that can't be made locally
   - ✅ Consult with manufacturers early in Step 7 or Step P

2. **Over-specifying tolerances**
   - ❌ ±0.01mm everywhere (expensive, unnecessary)
   - ✅ Tight tolerances ONLY where function requires

3. **Forgetting maintenance access** (DfX#9)
   - ❌ Battery buried behind 20 screws
   - ✅ High-service items easily accessible

4. **Thermal management neglected** (DfX#2)
   - ❌ Electronics packed tight without airflow
   - ✅ Thermal analysis for heat-generating components

5. **Interface mismatch**
   - ❌ Designing in isolation from mating parts
   - ✅ Define interfaces early, control with ICDs

6. **Skipping DfX priorities**
   - ❌ Applying generic DfX checklists
   - ✅ Use priority matrix from SKILL_dfx_guidelines

7. **Ignoring systems thinking**
   - ❌ Optimizing parameters (L12) when leverage points L6-L9 available
   - ✅ Map feedback loops, identify high-leverage interventions

---

## 🏁 PHASE 3 EXIT CRITERIA

**Gate 3 Checklist** - Must achieve ALL to proceed to Phase 4:

### Technical Completeness
- [ ] Definitive layout complete with dimensions and tolerances
- [ ] All materials selected and justified (Step M complete)
- [ ] Manufacturing methods defined (Step P complete)

### DfX Compliance
- [ ] Top 5 DfX priorities addressed (from SKILL_dfx_guidelines priority matrix)
- [ ] Each priority category checklist ≥80% complete
- [ ] Critical DfX gaps documented with mitigation plan

### Requirements & Standards
- [ ] Requirements verification matrix ≥80% complete
- [ ] Standards compliance verified (analysis or test plan defined)
- [ ] All embodiment-determining requirements satisfied

### Cost & Local Content
- [ ] Preliminary cost estimate within target (+10% variance acceptable)
- [ ] Local content ≥60% by value
- [ ] Critical import items identified with lead times

### Interfaces & Integration
- [ ] All critical interfaces defined (mechanical, electrical, thermal)
- [ ] Interface Control Documents (ICDs) created
- [ ] Assembly sequence defined (DfX#8)

### Systems & Risk
- [ ] Feedback loops identified (Systems Thinking)
- [ ] Leverage points applied where feasible (L6-L9 minimum)
- [ ] Risks identified with mitigations
- [ ] FMEA completed (critical functions)

### Documentation & Approvals
- [ ] Layout documentation complete (per template above)
- [ ] Stakeholder review completed (design, manufacturing, quality, systems)
- [ ] Gate 3 approval signatures obtained

**Gate 3 Status Determination:**
- **✅ PASS:** All critical items complete, <3 minor gaps with documented mitigation
- **⚠️ CONDITIONAL PASS:** <5 minor gaps, clear closure plan, approved by stakeholders
- **❌ FAIL:** >5 gaps or any critical item incomplete → Remediation required

---

## 🔗 RELATED SKILLS

**Prerequisite:**
- `SKILL_conceptual_design.md` - Selected concept from Phase 2

**Integrates With:**
- **`SKILL_dfx_guidelines.md`** - Comprehensive 12 DfX categories (ESSENTIAL for Step 4)
- **`SKILL_systems_thinking.md`** - Feedback loops, leverage points (use in Steps I, A, O)
- `SKILL_odi_innovation.md` - Weight VDI 2225 by opportunity scores (Step E)

**Next Phase:**
- `SKILL_detail_design.md` - Production documentation (Phase 4)

**Tools:**
- `scripts/vdi2225_calculator.py` - Variant evaluation (Step 5, Step E)
- `scripts/cost_calculator.py` - Cost estimation (Step 9, Step C)

---

## 📚 REFERENCE DOCUMENTS

**Internal:**
- **`SKILL_dfx_guidelines.md`** - 12 DfX categories with checklists
- `vault/references/material-selection-guide.md` - Material properties database
- `vault/references/vietnamese-suppliers.md` - Supplier contacts and capabilities
- `vault/references/mil-std-810h-summary.md` - Environmental testing quick reference

**External Standards:**
- MIL-STD-810H: Environmental Engineering Considerations
- MIL-STD-461G: EMC Requirements
- MIL-STD-882E: System Safety
- MIL-STD-1472H: Human Engineering
- Pahl & Beitz: "Engineering Design" (3rd Edition, Chapter 7)

---

## ✅ MASTERY CHECKLIST

### Level 1: Awareness (Can explain)
- [ ] Can explain difference between 7-step and 15-step approaches
- [ ] Can list 12 DfX categories
- [ ] Can identify embodiment-determining requirements
- [ ] Understands 4 basic rules

### Level 2: Application (Can do with guidance)
- [ ] Can complete 7-step process with checklist
- [ ] Can apply top 3 DfX priorities for a product
- [ ] Can create preliminary layout with dimensions
- [ ] Can perform material selection with weighted matrix

### Level 3: Proficiency (Can do independently)
- [ ] Can complete full 15-step RISM-PRAD-DECS-OCP process
- [ ] Can apply all 12 DfX categories systematically
- [ ] Can integrate Systems Thinking (feedback loops, leverage points)
- [ ] Can lead Gate 3 review
- [ ] Can optimize design for cost and performance

### Level 4: Expertise (Can teach and lead)
- [ ] Can mentor others in embodiment design
- [ ] Can adapt process for novel product types
- [ ] Can create custom DfX guidelines
- [ ] Can identify and apply meta-learning skills explicitly
- [ ] Can lead embodiment design for complex systems (>50 components)

---

*Phase 3 determines HOW the product will be made. This is where concept becomes reality.*
*"God is in the details" - Mies van der Rohe*
*"The devil is also in the details" - Defense Systems Engineer*

**Version:** 2.0 (Enhanced with 15-step process, DfX integration, Systems Thinking)
**Last Updated:** 2026-02-03
