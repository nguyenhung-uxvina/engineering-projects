# Engineering Design System - Unified Skills

**Version:** 2.4
**Updated:** 2026-02-20
**Total Skills:** 10 unified | **Total Commands:** 54+

---

## ⌨️ ALL SLASH COMMANDS

### 📁 Project Management (Core)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/open <code>` | `/o`, `/tieptuc` | Load project, show status |
| `/status [code]` | `/s` | Quick project status |
| `/new <name>` | `/taomoi` | Create new project |
| `/gate <phase>` | `/chuyenphase` | Phase transition |
| `/close` | — | Archive project |

### 🗂️ Portfolio (SKILL_portfolio_strategy)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/portfolio` | `/pf` | Portfolio dashboard |
| `/prioritize <Q>` | `/pri` | Prioritization matrix |
| `/allocate` | `/alloc` | Resource allocation |
| `/roadmap <domain>` | `/rm` | Technology roadmap |
| `/review <Q>` | `/qr` | Quarterly review |
| `/business-case` | `/bc` | Platform ROI analysis |

### 🎯 Phase 0: ODI (SKILL_odi_innovation)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/odi` | `/customer` | Run full ODI process |
| `/jobs` | `/jtbd` | Define job executor & map |
| `/outcomes` | `/dim` | Capture D-I-M outcomes |
| `/opportunity` | `/opp` | Calculate opportunity scores |
| `/segment` | `/seg` | Customer segmentation |

### 📝 Phase 1 (SKILL_task_clarification)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/requirements` | `/req`, `/taoreq` | Requirements list (16 cat) |
| `/validate` | `/check` | Completeness check |
| `/standards` | `/mil`, `/std` | MIL-STD mapping |
| `/stakeholders` | `/stake` | Stakeholder analysis |

### 🧠 Phase 2 (SKILL_conceptual_design)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/abstract` | `/abs` | 5-step abstraction |
| `/functions` | `/fn`, `/taofunction` | Function structure |
| `/morpho` | `/matrix`, `/taomorpho` | Morphological matrix |
| `/evaluate` | `/eval`, `/danhgia` | VDI 2225 evaluation |
| `/compare` | `/vs` | Concept comparison |

### 🔧 Phase 3 (SKILL_embodiment_design)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/layout` | `/thietke` | Layout design |
| `/dfx [type]` | `/dfm`, `/dfa` | DfX review |
| `/materials` | `/mat`, `/chonvatlieu` | Material selection |
| `/tolerances` | `/tol` | Tolerance analysis |
| `/local-content` | `/lc` | Local content % |

### 🔬 DfX Details (SKILL_dfx_guidelines)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/dfx-all` | `/dfx-12` | Review all 12 DfX categories |
| `/dfx-priority` | `/dfx-rank` | Prioritize DfX for product |
| `/corrosion` | `/dfc` | Design for Corrosion |
| `/thermal` | `/dft` | Design for Thermal |
| `/wear` | `/dfw` | Design for Wear |
| `/maintenance` | `/dfmaint` | Design for Maintenance |

### 🔀 S2 Orchestration (SKILL_s2_orchestration)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/orchestrate <product>` | `/orch` | Design full orchestration for a product |
| `/pattern <type>` | `/pat` | Apply specific pattern (pipeline/statemachine/workflow/parallel) |
| `/agents <product>` | `/roles` | Define master + sub-agent roster |
| `/edges <product>` | `/routing` | Design conditional edges |

### 🔄 Systems (SKILL_systems_thinking)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/cld` | `/causal` | Causal Loop Diagram |
| `/loops` | `/feedback` | Identify R/B loops |
| `/leverage` | `/lever` | Find leverage points |
| `/archetype` | `/pattern` | System archetypes |
| `/dynamics` | `/behavior` | Behavior over time |

### 📚 Learning (SKILL_dmir_learning)
| Command | Aliases | Purpose |
|---------|---------|---------|
| `/reflect` | `/weekly` | D-M-I-R reflection |
| `/mastery` | `/level` | Competency assessment |
| `/lessons` | `/ll` | Lessons learned |
| `/journal` | `/log` | Quick note |

### ⚡ Utilities
| Command | Purpose |
|---------|---------|
| `/help` | Show all commands |
| `/help <cmd>` | Command details |
| `/export <fmt>` | Export PDF/DOCX |
| `/template <name>` | Apply template |

---

## 📂 SKILL FILES (9 Unified) - All with Commands

```
skills/
├── SKILL_overview.md           ← Master index + /o, /s, /new, /gate, /close
│
├── SKILL_portfolio_strategy.md ← /pf, /pri, /alloc, /rm, /qr, /bc
├── SKILL_odi_innovation.md     ← /odi, /jobs, /outcomes, /opportunity, /segment
├── SKILL_systems_thinking.md   ← /cld, /loops, /leverage, /archetype, /dynamics
├── SKILL_s2_orchestration.md  ← /orchestrate, /pattern, /agents, /edges
│
├── SKILL_task_clarification.md ← /req, /validate, /mil, /stake
├── SKILL_conceptual_design.md  ← /abs, /fn, /morpho, /eval, /vs
├── SKILL_embodiment_design.md  ← /layout, /dfx, /mat, /tol, /lc
├── SKILL_dfx_guidelines.md     ← /dfx-all, /corrosion, /thermal, /wear, /maintenance
│
└── SKILL_dmir_learning.md      ← /reflect, /mastery, /ll, /log
```

---

## 🔄 WORKFLOW & SKILL LOADING

### Design Process Flow
```
┌─────────────────────────────────────────────────────────────┐
│  PORTFOLIO LEVEL                                             │
│  ─────────────────                                          │
│  /pf → /pri → /alloc                                        │
│  Load: SKILL_portfolio_strategy                             │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 0: CUSTOMER INSIGHT                                  │
│  ─────────────────────────                                  │
│  ODI process, Jobs-to-be-Done                               │
│  Load: SKILL_odi_innovation                                 │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: TASK CLARIFICATION                                │
│  ────────────────────────────                               │
│  /new → /req → /validate → /mil → /gate 2                   │
│  Load: SKILL_task_clarification + SKILL_systems_thinking    │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2: CONCEPTUAL DESIGN                                 │
│  ──────────────────────────                                 │
│  /abs → /fn → /morpho → /eval → /gate 3                     │
│  Load: SKILL_conceptual_design + SKILL_systems_thinking     │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3: EMBODIMENT DESIGN                                 │
│  ──────────────────────────                                 │
│  /layout → /dfx → /mat → /lc → /gate 4                      │
│  Load: SKILL_embodiment_design + SKILL_dfx_guidelines       │
└────────────────────────┬────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│  PHASE 4: DETAIL DESIGN                                     │
│  ──────────────────────                                     │
│  CAD drawings, BOM, production specs                        │
│  /close when complete                                       │
└─────────────────────────────────────────────────────────────┘
                         ↓
          /reflect → /lessons (throughout all phases)
          Load: SKILL_dmir_learning
```

### Loading Rules
1. **Load this file first** (SKILL_overview) for command reference
2. **Load 1-2 skills max** per task to conserve context
3. **Primary skill** = phase-specific (task_clarification, conceptual, embodiment)
4. **Support skill** = cross-cutting (systems_thinking, dfx_guidelines, dmir_learning)

---

## 📁 PROJECT COMMANDS (Detailed)

### /open <code> (aliases: /o, /tieptuc)

**Purpose**: Load project context, show status, suggest next action

**Output**:
```markdown
## Project: [CODE] - [NAME]

**Phase**: [N] - [Phase Name]
**Status**: 🟢 On Track | 🟡 At Risk | 🔴 Blocked

### Progress
- [x] Completed item
- [ ] **In Progress**: Current task
- [ ] Pending: Next task

### Suggested Next Action
> [Specific action with rationale]
```

---

### /status [code] (alias: /s)

**Purpose**: Quick status check

**Output**:
```markdown
Phase 2/4 | 🟢 On Track | Updated: [DATE]
Progress: ████████░░ 80%
Next Gate: [DATE] - Phase 2→3
```

---

### /new <name> (alias: /taomoi)

**Purpose**: Create new project with folder structure

**Creates**:
```
vault/projects/VN-XXX-NNN/
├── 00_project_brief.md
├── 01_requirements/
├── 02_conceptual/
├── 03_embodiment/
├── 04_detail/
└── PROJECT_STATUS.md
```

---

### /gate <phase> (alias: /chuyenphase)

**Purpose**: Verify gate checklist, transition phase

**Gate Checklists**:

| Phase 1→2 | Phase 2→3 | Phase 3→4 |
|-----------|-----------|-----------|
| 16 categories reviewed | Function structure ✓ | Layout finalized |
| ≥80% quantified | ≥3 concepts | DfX passed |
| No conflicts | VDI 2225 ≥70% | Local ≥60% |
| Stakeholder sign-off | Rationale documented | Cost on target |

---

### /close

**Purpose**: Archive completed/cancelled project

**Actions**:
1. Generate summary report
2. Extract lessons learned
3. Move to `vault/projects/_archive/`
4. Update PROJECT_INDEX.md

---

## 🇻🇳 VIETNAMESE CONTEXT

| Target | Value |
|--------|-------|
| Local Content | 60-75% |
| Cost vs Import | ≤70% |
| Standards | MIL-STD + TCVN |

---

## ⌨️ QUICK REFERENCE CARD

```
╔═══════════════════════════════════════════════════════════════╗
║           ENGINEERING DESIGN SYSTEM v2.2                      ║
╠═══════════════════════════════════════════════════════════════╣
║ PROJECT          │ PORTFOLIO        │ PHASE 1                 ║
║ /o    open       │ /pf   dashboard  │ /req  requirements      ║
║ /s    status     │ /pri  prioritize │ /check validate         ║
║ /new  create     │ /rm   roadmap    │ /mil  standards         ║
║ /gate transition │ /qr   review     │ /stake stakeholders     ║
╠═══════════════════════════════════════════════════════════════╣
║ PHASE 2          │ PHASE 3          │ LEARNING                ║
║ /abs  abstract   │ /layout design   │ /reflect weekly         ║
║ /fn   functions  │ /dfx   review    │ /mastery assess         ║
║ /morpho matrix   │ /mat   materials │ /ll     lessons         ║
║ /eval  evaluate  │ /tol   tolerance │ /log    quick note      ║
║ /vs    compare   │ /lc    local %   │                         ║
╠═══════════════════════════════════════════════════════════════╣
╠═══════════════════════════════════════════════════════════════╣
║ ORCHESTRATION    │ DFX              │ UTILITIES               ║
║ /orch  design    │ /dfx-all review  │ /help    commands        ║
║ /pat   pattern   │ /corrosion DfC   │ /export  PDF/DOCX        ║
║ /roles agents    │ /thermal   DfT   │ /template apply          ║
║ /routing edges   │ /wear      DfW   │                          ║
╠═══════════════════════════════════════════════════════════════╣
║ Type /help <command> for details    │ Bilingual: EN + VN      ║
╚═══════════════════════════════════════════════════════════════╝
```

---

*Engineering Design System v2.4 - Unified Skills Architecture*
