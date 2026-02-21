---
type: session-checkpoint
created: 2026-02-19
context-at-save: ~80k / 200k (40%)
session: 9
module: 11 (GitHub Action)
---

# CC-Mastery Progress

## Completed

### Session 1 (2026-02-14): Modules 1-3
- Module 1: Audited parent CLAUDE.md, moved tables to vault/references/, added alternatives to all "Never" rules, v2.3 -> v2.4
- Module 2: Learned Document & Clear pattern, created checkpoint_session_01.md as exercise
- Module 3: Created /checkpoint and /catchup global slash commands

### Session 2 (2026-02-15): CLAUDE.md Refinement + /pr Command
- Rewrote CC-Mastery/CLAUDE.md from bare tracker to proper guardrails file (30 lines, practices Module 1 principles)
- Added Workflow Rules, Context Budget, and real Mistakes entries
- Created `/pr` global slash command — cleans code, stages, drafts PR, waits for approval
- Now at 3 global commands: /checkpoint, /catchup, /pr

### Session 3 (2026-02-15): Module 4 — Resume, Continue & History
- Explored session history structure: `.jsonl` files in `~/.claude/projects/<path>/`
- Entry types: user, assistant, progress, file-history-snapshot, queue-operation
- Analyzed 4 CC-Mastery sessions + 17 total project histories
- Discovered `engineering-projects` parent has 10 sessions / 54MB — richest mine for insights
- Initialized auto-memory (`MEMORY.md`) — was empty, now has project context + workflow patterns
- Key learning: auto-memory is the bridge between session history and CLAUDE.md

### Session 4 (2026-02-15): Module 5 — Planning Mode
- Learned planning mode concepts: Shift+Tab, --permission-mode plan, auto-detect
- Plan mode = read-only exploration (no Edit/Write/NotebookEdit) until plan approved
- Used planning mode end-to-end: EnterPlanMode → Explore → Plan → ExitPlanMode → Implement
- Built `planning_demo.py` — analyzes session JSONL files for planning patterns
- Key finding: planned session had 0.79 exploration ratio vs 0.26 for unplanned sessions
- Fixed Windows encoding issue: `sys.stdout.reconfigure(encoding="utf-8")`

### Session 5 (2026-02-15): Modules 6 & 7 — Hooks + Custom Subagents
**Module 6 — Hooks (initial):**
- Learned hook system: 14 event types, PreToolUse is the key one for blocking
- Exit codes: 0 = allow, 2 = block (stderr fed back to Claude), other = ignore
- Built `log_bash.py` (PreToolUse logging) and `block_commit.py` (PreToolUse blocking)
- Self-correction demo: hook blocked buggy commit, provided test output, agent fixed and retried

**Module 7 — Custom Subagents:**
- Core lesson: custom subagents are usually an anti-pattern (context gating + forced workflows)
- Better model: master-clone — main agent dynamically spawns Task()/Explore() as needed
- Formula: `(X + Y) * N + Z` — shared context in CLAUDE.md, dynamic delegation, task-specific prompts

### Session 6 (2026-02-17): Module 6 Retry — Expanded Hook Types
- Extended from 2 hooks (PreToolUse only) to **5 hooks across 4 event types**:
  1. `log_bash.py` — PreToolUse (Bash): logs all commands with timestamps
  2. `block_commit.py` — PreToolUse (Bash): blocks git commit unless pytest passes
  3. `track_file_changes.py` — **PostToolUse** (Write|Edit): logs file modifications
  4. `prompt_hints.py` — **UserPromptSubmit**: injects context hints for keywords/project IDs
  5. `stop_logger.py` — **Stop**: logs response completions, checks `stop_hook_active`
- All 5 hooks verified working with log evidence
- Key learnings per event type:
  - PostToolUse: receives `tool_response`, good for auditing, non-blocking
  - UserPromptSubmit: stdout = context injection Claude sees — most powerful hint mechanism
  - Stop: `stop_hook_active` flag critical to prevent infinite continue loops
- Created `.claude/hooks/README.md` documenting all hooks

### Session 7 (2026-02-17): Modules 8 & 9 — Skills + MCP

**Module 8 — Skills:**
- Learned skill architecture: SKILL.md + scripts/ + references/ + assets/
- Three progressive disclosure levels: metadata (always) → SKILL.md (on trigger) → resources (on demand)
- Invoked `example-skills:skill-creator` to study a real packaged skill
- Explored skill-creator internals: `init_skill.py`, `package_skill.py`, `quick_validate.py`
- **Conversion exercise**: Converted `SKILL_task_clarification.md` (369-line monolith) to official format:
  - SKILL.md: 82 lines (core workflow, commands, guardrails)
  - references/: 2 files (categories table, stakeholder template) — loaded on-demand
  - assets/: 1 file (requirements list template) — never in context, copied to projects
  - scripts/: 1 file (`validate_requirements.py`) — deterministic completeness checker
- Validated with `quick_validate.py` — passed after fixing YAML multi-line scalar bug
- Discovered: `quick_validate.py` doesn't handle YAML `>` folded scalars (naive regex)

**Module 9 — MCP:**
- Core thesis: MCP = secure gateway for stateful/sensitive ops, not general API wrapper
- Decision framework: stateful or security-gated → MCP; stateless → Skill + Script
- Audited existing MCP servers:
  - Hyperbrowser: legitimate MCP (stateful browser sessions) — keep
  - Brave Search: stateless (independent HTTP GETs) — migration candidate
- **Exercise A**: Migrated Brave Search MCP → Skill (`brave_search.py`, 80 lines, zero deps, stdlib only)
  - Tested with real API call — returns clean JSON results
  - Replaces entire npm package + Node runtime + MCP protocol framing
- **Exercise B**: Built minimal MCP server (`project_tracker.py`) with FastMCP
  - 3 tools: `get_projects()`, `update_phase()`, `run_gate_check()`
  - Maps to curriculum's three-tool pattern: read / controlled mutation / validation
  - In-memory state persists across tool calls (why it must be MCP, not script)
  - Phase enforcement: can't skip phases, can't go backward
  - All 3 tools tested and verified working
- Registered in `.mcp.json` (learned: MCP config goes in `.mcp.json`, not `settings.json`)
- Installed `mcp[cli]` Python package (FastMCP SDK)

### Session 8 (2026-02-19): Module 10 Deep Dive — Claude Agent SDK (all 3 layers)

**Layer 1 — CLI Headless (`claude -p`)** — 7 progressive levels:
1. Basics: `-p`, `--output-format json|text`, `--model`, `--tools ""`
2. Piping: `content | claude -p "instruction"`, chain pattern
3. Tool control: `--allowedTools`, `--disallowedTools`, `--tools`, `--permission-mode`
4. Session chaining: `--resume $id`, `--continue`, cost savings from context reuse
5. Structured extraction: `--json-schema '{...}'` + `--output-format json`
6. CI/CD patterns: smart_commit, review_pr, changelog, security_audit, batch parallel
7. System prompts: `--append-system-prompt` (add persona) vs `--system-prompt` (replace)

**Layer 2 — Python SDK** — 6 progressive levels:
1. `query()` basics: AsyncGenerator[Message], 4 message types, content blocks
2. Agent Observatory: execution traces, tool call logging, timing analysis
3. `ClaudeSDKClient`: multi-turn, `set_model()`, `interrupt()`, context persistence
4. SDK hooks: inline async Python callbacks (vs Module 6 file-based hooks)
5. Custom MCP tools: `@tool` decorator + `create_sdk_mcp_server()` — in-process, no server
6. Real patterns: fan-out/fan-in, writer/reviewer, sequential pipeline

**Layer 3 — TypeScript SDK** — 4 levels:
1. `query()` basics: `SDKMessage` discriminated union, `BetaMessage` content format
2. `AbortController` + Query control methods (`interrupt`, `setModel`, `supportedModels`)
3. Custom tools with Zod schemas + hooks as `HookCallback`
4. Python vs TS comparison (naming, types, schemas, cancellation, multi-turn)

**Key Technical Findings:**
- Installed `claude-agent-sdk` v0.1.37 (Python) + `@anthropic-ai/claude-agent-sdk` v0.2.47 (TS)
- Inspected actual SDK source types — `ClaudeAgentOptions` has 35+ fields, `Query` has 12+ control methods
- TS SDK passes type-checking (`tsc --noEmit` clean)
- Python `ClaudeSDKClient` = stable multi-turn; TS `unstable_v2_createSession` = alpha
- Zod v4 supported in TS SDK tool schemas

### Session 9 (2026-02-19): Module 11 — Claude Code GitHub Action

**Core concepts:**
- The Flywheel: GHA logs → pattern analysis → CLAUDE.md fixes → better agent → fewer bugs
- Interactive vs Automation mode: presence of `prompt` input determines mode
- PR-from-Anywhere: any alert system → GitHub issue → Claude GHA → branch → human PR
- Policy: AI-initiated PRs should require 2 human approvals (Tier 2/3)

**4 progressive workflow files:**
1. `01_interactive.yml` — Responds to @claude mentions (entry point)
2. `02_pr_review.yml` — Auto-reviews every PR on open/update (read-only tools)
3. `03_issue_to_pr.yml` — Issue → branch with implementation (write tools)
4. `04_scheduled_maintenance.yml` — Cron health checks + CI debug (structured output)

**Key technical findings:**
- Action: `anthropics/claude-code-action@v1` (GA since Aug 2025, name NOT renamed unlike SDK)
- `claude_args` is the power knob — accepts any Claude Code CLI argument
- `--allowedTools` in `claude_args` is the security boundary in GHA
- Structured output (`--json-schema` + `structured_output`) makes Claude a CI decision engine
- Claude creates branches, NOT PRs — human must create PR (safety by default)
- `additional_permissions` for CI log access (`actions: read`)
- OIDC supported for Bedrock/Vertex/Foundry (no API key storage needed)

**Log analysis script:**
- `analyze_gha_logs.py` — queries GHA runs via `gh` CLI, detects error patterns
- Detects: file_not_found, test_failure, tool_blocked, max_turns_hit, retries, etc.
- Generates CLAUDE.md improvement suggestions based on pattern frequency
- The "power move": pipe output to `claude -p` for automated CLAUDE.md fixes

**AI PR policy (3 tiers):**
- Tier 1 (human-prompted): standard review, 1 approval
- Tier 2 (event-triggered): 2 approvals, no auto-merge
- Tier 3 (fully autonomous): 2 approvals, CODEOWNERS, max-turns cap, audit trail

### Session 10 (2026-02-20): Module 12 — settings.json Tuning ✅ CURRICULUM COMPLETE

**Three-layer architecture learned:**
- Global: `~/.claude/settings.json` (all projects) — timeouts added
- Project shared: `.claude/settings.json` (committed, team) — hooks here
- Project local: `.claude/settings.local.json` (gitignored, personal) — permissions here

**Permissions audit — 25 rules reviewed:**
- 2 removed: `Bash(choco install:*)` (HIGH risk — silent software installs) + `WebFetch(domain:blog.sshh.io)` (stale, module-specific)
- 23 retained with documented risk classification in MODULE_12_NOTES.md
- Key insight: allow-list skips the prompt, but hooks still fire. `git commit` is safe because `block_commit.py` is the real security gate.

**Timeouts added to global settings.json:**
- `BASH_MAX_TIMEOUT_MS: 600000` (10 min — for SDK pipeline scripts)
- `MCP_TOOL_TIMEOUT: 120000` (2 min — for slow MCP servers)

**Enterprise pattern learned:** `apiKeyHelper` for centralized key management — relevant for IRONMESH multi-operator deployments.

**Mastery checklist: ALL 12 items complete** (see MODULE_12_NOTES.md §7)

## Current State
- **ALL 12 MODULES COMPLETE** ✅
- Mastery checklist: Beginner ✅ / Intermediate ✅ / Advanced ✅
- Curriculum flywheel active: GHA logs → CLAUDE.md → better agents → fewer bugs

## Files Created/Modified
| File | Action |
|------|--------|
| `gha_demo/01_interactive.yml` | Created — @claude mention responder |
| `gha_demo/02_pr_review.yml` | Created — automatic PR review |
| `gha_demo/03_issue_to_pr.yml` | Created — issue-to-branch worker |
| `gha_demo/04_scheduled_maintenance.yml` | Created — cron + CI debug |
| `gha_demo/analyze_gha_logs.py` | Created — log pattern analysis script |
| `gha_demo/MODULE_11_NOTES.md` | Created — comprehensive study notes |
| `gha_demo/AI_PR_POLICY.md` | Created — 3-tier AI PR policy |
| `CLAUDE.md` | Updated — Module 11 done, next is 12 |
| `progress.md` | Updated — Session 9 details |

## Files Created/Modified (Session 10)
| File | Action |
|------|--------|
| `MODULE_12_NOTES.md` | Created — full settings.json audit, enterprise patterns, mastery checklist |
| `.claude/settings.local.json` | Updated — removed `choco install` (HIGH risk) + stale blog domain |
| `~/.claude/settings.json` | Updated — added BASH_MAX_TIMEOUT_MS + MCP_TOOL_TIMEOUT |
| `CLAUDE.md` | Updated — Modules 1-12 complete |
| `progress.md` | Updated — Session 10 |

## Next Steps
1. Apply CC Mastery to VN-RANGE-001 pipeline (Human_Skills_AI workspace)
2. Run Phase 1 from standalone terminal: `unset CLAUDECODE && python sdk_pipeline_VN-RANGE-001.py --phase 1`
3. Consider deploying GHA workflows on real defense project repo

## Key Decisions Made
- CC-Mastery/CLAUDE.md practices what Module 1 teaches (guardrails, not manual)
- /pr command waits for approval before committing (safe by default)
- Staying under 5 slash commands per Module 3 guideline
- Auto-memory used for cross-session patterns, CLAUDE.md for guardrails (different purposes)
- Planning mode proven valuable: higher exploration ratio = more precise implementation
- Hooks use Python (not bash+jq) for Windows compatibility
- Block-at-submit is the primary hook pattern; avoid block-at-write (confuses agent mid-plan)
- Dynamic delegation (Task/Explore) beats rigid subagent routing — main agent is the best router
- UserPromptSubmit stdout injection is the best mechanism for hint/context hooks
- Skills > MCP for most use cases — raw env access beats API abstraction
- Skill description must be single-line (no YAML `>` scalar) — validator uses naive regex
- Monolith SKILL files should split into SKILL.md + references/ + assets/ + scripts/
- MCP only for stateful/security-gated ops; stateless tools → skill + script
- MCP server config goes in `.mcp.json`, not `settings.json`
- Three-tool MCP pattern: read + controlled mutation + validation
- SDK renamed to "Claude Agent SDK" — old package names deprecated
- SDK `setting_sources` defaults empty — must explicitly load CLAUDE.md/hooks/MCP
- SDK before framework — validate agentic ideas with 20-line script, then scale up
- `--allowedTools` prefix matching with trailing ` *` (space matters)
- `ClaudeSDKClient` for multi-turn; `query()` for one-shot
- TS SDK: Zod schemas give compile-time type inference on tool args (vs Python dict/Pydantic runtime-only)
- TS SDK: `Query` object has control methods directly (vs Python `ClaudeSDKClient` separate methods)
- TS `unstable_v2_createSession` is alpha — use `query()` with streaming input for now
- SDK hooks share in-memory state with your app (vs file-based hooks: subprocess overhead)
- GHA action name is `anthropics/claude-code-action@v1` — NOT renamed (unlike SDK)
- `claude_args` is the single power knob in GHA — all CLI flags go through it
- Claude creates branches, not PRs — human always creates the PR (safety default)
- Structured output (`--json-schema`) turns Claude into a CI decision engine
- AI-initiated PRs need tiered policy: human-prompted (1 review), event-triggered (2 reviews), autonomous (2 + CODEOWNERS)
