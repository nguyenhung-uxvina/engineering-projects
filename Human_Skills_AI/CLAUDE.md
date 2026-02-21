# CLAUDE.md — Human_Skills_AI Workspace

**Version:** 1.0
**Created:** 2026-02-20
**Purpose:** Mastery of Agentic AI skills (ALCPE framework) applied to Workshop X defense products

---

## 🎯 Workspace Purpose

This workspace is for learning and applying the **5 Agentic Skills** that remain high-value alongside AI:

| Skill | Code | Current Score | Target | Evidence |
|-------|------|--------------|--------|----------|
| AI Literacy & Delegation | A | 8/10 | 10/10 | — |
| Multi-Agent Orchestration | L | 9/10 | 10/10 | `cortex_state_machine.md` — formal FSM spec |
| Critical Reasoning | C | 9/10 | 9/10 | `defense_ai_qc_checklist.md` + `validate_defense_ai_output.py` + wired into SDK pipeline |
| Process Automation Design | P | 7/10 | 8/10 | `skill4_automation_gradient_template.md`, `pipeline_VN-RANGE-001.md` |
| Ethics & Conflict Mitigation | E | 9/10 | 9/10 | `governance_framework_VN-RANGE-001.md` — audit trail, TCVN mapping, ROE system, accountability chain + wired into SDK pipeline |

**Primary product for live pipeline work:** VN-RANGE-001 (IRONMESH RANGE)

---

## 📁 Key Files

```
Human_Skills_AI/
├── CLAUDE.md                           ← This file
├── progress.md                         ← Session checkpoint (resume from here)
├── agentic_ai_skills_analysis.md       ← ALCPE framework analysis + Workshop X mapping
├── Claude_Code_Mastery_System.md       ← 30-day CC mastery plan (Modules 1-11 done)
├── pipeline_VN-RANGE-001.md            ← Master-clone pipeline architecture doc
├── sdk_pipeline_VN-RANGE-001.py        ← SDK implementation (5-phase, run OUTSIDE CC)
├── skill4_automation_gradient_template.md ← Skill 4 reusable template
├── cortex_state_machine.md             ← CORTEX FSM formal spec (Skill 2 evidence)
├── defense_ai_qc_checklist.md          ← Skill 3 QC checklist (6 categories, 40+ checks)
├── validate_defense_ai_output.py       ← Automated physics + data quality validator (exit 0/2)
└── governance_framework_VN-RANGE-001.md ← Skill 5 governance: audit trail, TCVN, ROE, accountability
```

---

## ⚙️ SDK / Python Environment

### Correct Imports (verified 2026-02-20)
```python
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,   # NOT ClaudeCodeOptions
    AssistantMessage,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolUseBlock,
)
```

### Required ClaudeAgentOptions fields
```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write"],   # or None for unrestricted
    max_turns=15,
    permission_mode="acceptEdits",     # headless: no approval prompts
    system_prompt="...",
    cwd=str(Path.cwd()),
    setting_sources=[],                # [] = isolated; omit = load parent CLAUDE.md
)
```

---

## 🚫 Mistakes Not To Repeat

### SDK — Nested Session (2026-02-20)
- **Cannot run SDK scripts inside an active Claude Code session.**
  Error: `Claude Code cannot be launched inside another Claude Code session.`
  Fix: Unset `CLAUDECODE` env var before running:
  ```bash
  unset CLAUDECODE && python sdk_pipeline_VN-RANGE-001.py --phase 1
  # Windows CMD: set CLAUDECODE=  then run python ...
  ```

### SDK — Wrong import names (2026-02-20)
- Package: `claude_agent_sdk` (NOT `claude_code_sdk`)
- Options class: `ClaudeAgentOptions` (NOT `ClaudeCodeOptions`)
- Installed as: `pip install claude-agent-sdk` (hyphen), imported as `claude_agent_sdk` (underscore)

### Windows — UTF-8 Encoding (Module 4 lesson)
- Always add at script top for Windows compatibility:
  ```python
  if sys.platform == "win32":
      sys.stdout.reconfigure(encoding="utf-8")
  ```
- Place BEFORE any emoji or non-ASCII print statements

### Pipeline Design — Anti-Patterns (2026-02-20)
- **Never design rigid 3-agent pipelines for defense** — edge cases break pre-defined routing.
  Use master-clone: main agent holds state and decides routing dynamically.
- **Skill 4 starts with consequence mapping, not automation tools** — ask "what fails if AI gets
  this wrong?" BEFORE deciding automation %. Automation gradient: consequence ↑ → automation % ↓.
- **HITL checkpoints are architectural decisions** — not UX polish. Place at every gate where
  accountability transfers. Gate decisions → always 0% automated.
- **Custom subagents with forced routing = anti-pattern** — use Task() delegation from master agent.
  Master agent is the best router because it has full context.
- **SDK pipeline fallbacks are first-class design** — every automated step needs explicit fallback.
  If no fallback defined → do NOT automate that step.

---

## 🔄 Automation Gradient (Skill 4 Core Rule)

```
Automation % DECREASES as consequence increases.

NEGLIGIBLE  → 95-100%  (no harm if wrong)
LOW         → 80-95%   (reversible, cheap to fix)
MEDIUM      → 60-80%   (significant rework if wrong)
HIGH        → 30-60%   (safety/trust/legal impact)
CRITICAL    → 0-20%    (life/mission impact)
ABSOLUTE    → 0%       (gate decisions, military sign-off — always human)
```

---

## 🏗️ VN-RANGE-001 Pipeline — Quick Reference

**Run outside CC session** (`unset CLAUDECODE` first):

```bash
python sdk_pipeline_VN-RANGE-001.py --phase 1   # Requirements (90% auto, no HITL)
python sdk_pipeline_VN-RANGE-001.py --phase 2   # Architecture review (70% auto, HITL)
python sdk_pipeline_VN-RANGE-001.py --phase 3   # Integration design (75% auto, HITL)
python sdk_pipeline_VN-RANGE-001.py --phase 4   # DfX gate review (50% auto, HITL)
python sdk_pipeline_VN-RANGE-001.py --phase 5   # Safety validation (0% auto, human-led)
```

Phase prerequisites: each phase requires the prior phase's output file to exist.
Audit log: `pipeline_audit_log.jsonl` (created automatically on first HITL decision).

---

## 📋 Session Resume Protocol

1. Read `progress.md` for current state and next steps
2. Check which pipeline phases have output files (`requirements_VN-RANGE-001.md`, etc.)
3. Continue from the first incomplete phase

---

## 🎓 CC-Mastery Status (as of 2026-02-20)

Modules 1-11 complete. Module 12 (settings.json Tuning) remaining.
Full details: `d:/UxV/engineering-projects/CC-Mastery/progress.md`

Key patterns confirmed working:
- Hooks: 5 hooks across 4 event types (PreToolUse, PostToolUse, UserPromptSubmit, Stop)
- MCP: `project_tracker.py` with FastMCP (3-tool pattern: read/mutate/validate)
- Skills: official format (SKILL.md + references/ + assets/ + scripts/)
- GHA: 4 workflow patterns (interactive, PR review, issue-to-PR, scheduled)
- SDK: `query()` one-shot + `ClaudeSDKClient` multi-turn, Python + TypeScript
