# Engineering Design System

An AI-powered systematic engineering design platform for Vietnamese defense and security product development. Built on **Pahl & Beitz** methodology (VDI 2221/2225), **Outcome-Driven Innovation (ODI)**, and **Systems Thinking** — orchestrated through Claude Code with Obsidian as the knowledge vault.

## Architecture

```
┌─────────────────────┐         ┌──────────────────────────┐
│    CLAUDE CODE      │◄───────►│     OBSIDIAN VAULT       │
│    (AI Engine)      │  read/  │   (Knowledge Store)      │
│                     │  write  │                          │
│  • Design phases    │         │  • Projects (VN-XXX)     │
│  • ODI analysis     │         │  • Skills (11 modules)   │
│  • Systems thinking │         │  • Templates             │
│  • DfX review       │         │  • Learning journal      │
└─────────────────────┘         └──────────────────────────┘
```

## Repository Structure

```
├── engineering-design-system/     # Core system
│   ├── skills/                    # 11 skill modules (50+ commands)
│   └── vault/
│       ├── projects/              # Active project files
│       ├── templates/             # Reusable document templates
│       └── references/            # Standards, suppliers, commands
├── Engineering Design Knowledge/  # Pahl & Beitz study notes (100+ analyses)
├── 5 Skills AI/                   # Agentic AI skill development
├── CC-Mastery/                    # Claude Code mastery curriculum
├── Human_Skills_AI/               # AI governance & QC frameworks
├── VN-Projects/                   # Additional project workspace
├── vault/                         # Shared references
├── CLAUDE.md                      # System instructions for Claude Code
└── SETUP_GUIDE.md                 # Installation & setup guide (Vietnamese)
```

## Active Projects

| Code | Product | Phase | Status |
|------|---------|-------|--------|
| **VN-TGT-SEA-001** | Fixed Sea Target "THANH TRI-H" | 4 - Detail | 6 deliverables complete |
| **VN-TRN-001** | Training Range System | 4 - Detail | Prototype build plan ready |
| **CORTEX-C2** | AI C2 Platform "THAN TOAN" | 1 - Requirements | Gate review pending |
| **VN-CUAS-001** | C-UAS Acoustic Detection | 2 - Conceptual | Concept selected (VDI 75%) |
| **VN-RNG-001** | LOMAH Shooting Range | 1 - Requirements | Gate review pending |
| **V-SMASH** | 12.7mm C-UAS Fire Control | 2 - Conceptual | Stakeholder review |

## Design Methodology

The system follows a gated phase workflow:

```
Phase 0 (ODI)  →  Phase 1 (Requirements)  →  Phase 2 (Conceptual)
                                                      ↓
Phase 4 (Detail)  ←  Phase 3 (Embodiment)  ←─────────┘
```

Each phase gate requires explicit approval with deliverable checklists before proceeding.

### Skill Modules

| Skill | Purpose |
|-------|---------|
| Overview | Project management, gates, status |
| Portfolio Strategy | Prioritization, roadmaps, resource allocation |
| ODI Innovation | Jobs-to-be-Done, outcomes, opportunity scoring |
| Systems Thinking | Causal loops, leverage points, archetypes |
| Task Clarification | Requirements, standards, stakeholders (Phase 1) |
| Conceptual Design | Abstraction, morphology, VDI 2225 evaluation (Phase 2) |
| Embodiment Design | Layout, materials, tolerances, local content (Phase 3) |
| DfX Guidelines | Design for corrosion, thermal, wear, production, etc. |
| Reverse Engineering | Competitor analysis and benchmarking |
| D-M-I-R Learning | Weekly reflections, mastery tracking, lessons learned |

## Design Targets

| Metric | Target |
|--------|--------|
| Local content | 60-75% by value |
| Cost vs import | ≤70% of equivalent |
| Requirements quantified | ≥80% |
| VDI 2225 concept score | ≥70% |
| Standards | MIL-STD + TCVN |

## Getting Started

1. Install [Claude Code](https://claude.ai/claude-code) (CLI)
2. Install [Obsidian](https://obsidian.md/) and open the vault directory
3. See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions (Vietnamese)

## Tech Stack

- **AI Engine**: Claude Code (Claude Opus 4.6)
- **Knowledge Vault**: Obsidian (Markdown + wiki-links)
- **Scripts**: Python (VDI 2225 calculator, validation tools)
- **Methodology**: Pahl & Beitz (VDI 2221), ODI (Strategyn), D-M-I-R

## License

Proprietary. All rights reserved.
