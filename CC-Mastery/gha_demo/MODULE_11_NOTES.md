# Module 11: Claude Code GitHub Action — Study Notes

## Core Concept

Run Claude Code in CI/CD. Full agent logs = auditable, **self-improving** system.

---

## The Flywheel

```
    ┌─────────────────────────────────────┐
    │                                     │
    ▼                                     │
  GHA Runs ──► Agent Logs ──► Pattern     │
    │            Analysis       │          │
    │                           ▼          │
    │                     CLAUDE.md        │
    │                     Improvements     │
    │                           │          │
    │                           ▼          │
    └───── Better Agent ◄── Fewer Bugs ───┘
              Behavior
```

**How it works:**
1. Claude Code runs in GHA → produces execution logs
2. `analyze_gha_logs.py` extracts error patterns from those logs
3. Patterns reveal what Claude gets wrong repeatedly
4. Fix those patterns in CLAUDE.md (guardrails, not manual)
5. Next GHA run uses improved CLAUDE.md → fewer mistakes
6. Repeat — the system improves itself

**The "power move"** closes the loop automatically:
```bash
python analyze_gha_logs.py --repo owner/repo --since 5d --analyze | \
  claude -p "Read these agent mistakes and fix CLAUDE.md. Put up a PR."
```

---

## PR-from-Anywhere Architecture

```
  ┌──────────┐   ┌──────────┐   ┌──────────────┐
  │  Slack   │   │   Jira   │   │  CloudWatch  │
  │  Alert   │   │  Ticket  │   │    Alarm     │
  └────┬─────┘   └────┬─────┘   └──────┬───────┘
       │              │                 │
       ▼              ▼                 ▼
  ┌──────────────────────────────────────────┐
  │         GitHub Issue (auto-created)       │
  │     Label: "claude" or @claude mention    │
  └─────────────────┬────────────────────────┘
                    │
                    ▼
  ┌──────────────────────────────────────────┐
  │     03_issue_to_pr.yml (GHA Workflow)     │
  │                                           │
  │  1. Claude reads issue                    │
  │  2. Creates branch: claude/issue-42-...   │
  │  3. Implements fix + runs tests           │
  │  4. Commits and pushes                    │
  │  5. Posts link for human to create PR     │
  └─────────────────┬────────────────────────┘
                    │
                    ▼
  ┌──────────────────────────────────────────┐
  │          Human Review (mandatory)         │
  │                                           │
  │  - Human clicks link → creates PR         │
  │  - 2 human approvals required (policy)    │
  │  - Merge only after review passes         │
  └──────────────────────────────────────────┘
```

**Integration patterns:**

| Source | How to create GitHub issue |
|--------|--------------------------|
| Slack | Slack workflow → `gh issue create` webhook |
| Jira | Jira automation → GitHub webhook |
| CloudWatch | SNS → Lambda → `gh issue create` |
| PagerDuty | Webhook → GitHub `repository_dispatch` |
| Manual | `workflow_dispatch` (button in GHA UI) |

---

## The 4 Workflow Levels

| File | Mode | Trigger | Use Case |
|------|------|---------|----------|
| `01_interactive.yml` | Interactive | @claude mentions | General assistant |
| `02_pr_review.yml` | Automation | PR open/update | Code review |
| `03_issue_to_pr.yml` | Automation | Issue label/assign | Feature implementation |
| `04_scheduled_maintenance.yml` | Automation | Cron + manual | Health checks + CI debug |

### Interactive vs Automation Mode

The action auto-detects based on whether `prompt` input is provided:
- **No `prompt`** → Interactive mode: waits for @claude, creates tracking comments
- **Has `prompt`** → Automation mode: runs immediately, no tracking by default

---

## Key Configuration

### Action: `anthropics/claude-code-action@v1`

**Critical inputs:**
- `anthropic_api_key` — stored in repo secrets, never hardcoded
- `prompt` — determines automation vs interactive mode
- `claude_args` — the power knob (model, tools, max-turns, system prompt)
- `label_trigger` / `assignee_trigger` — issue-based triggers
- `branch_prefix` — namespace for Claude's branches (default: `claude/`)
- `additional_permissions` — request extra GitHub token scopes

**Critical outputs:**
- `execution_file` — full execution log path
- `structured_output` — JSON from `--json-schema` (for downstream decisions)
- `session_id` — for `--resume` continuation
- `branch_name` — the branch Claude created

### Tool Safety via `--allowedTools`

```yaml
# Read-only review (safe)
claude_args: |
  --allowedTools "Read,Glob,Grep,Bash(gh pr diff:*)"

# Implementation (controlled write)
claude_args: |
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(git:*),Bash(npm test:*)"

# Full power (use with caution)
claude_args: |
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash"
```

---

## Security Model

| Layer | Protection |
|-------|-----------|
| **Trigger** | Only repo write-access users can trigger Claude |
| **Tools** | `--allowedTools` restricts what Claude can execute |
| **Branches** | Claude creates branches, NOT PRs (human creates PR) |
| **Tokens** | Short-lived, single-repo scope, auto-revoked after run |
| **Logs** | `show_full_output: false` by default (prevents secret leaks) |
| **Auth** | API key in secrets; OIDC supported for Bedrock/Vertex/Foundry |
| **Sanitization** | HTML comments, invisible chars, markdown tricks stripped |

---

## Structured Output Pattern

This is a killer feature for CI decision-making:

```yaml
claude_args: |
  --json-schema '{"type":"object","properties":{
    "is_flaky":{"type":"boolean"},
    "confidence":{"type":"number"},
    "summary":{"type":"string"}
  },"required":["is_flaky"]}'
```

Then in the next step:
```yaml
- if: fromJSON(steps.claude.outputs.structured_output).is_flaky == true
  run: gh workflow run CI  # retry if flaky
```

This turns Claude into a **decision engine** in your CI pipeline — not just a code writer.

---

## The Analysis Script

`analyze_gha_logs.py` closes the flywheel loop:

```
Usage:
  # Overview of recent runs
  python analyze_gha_logs.py --repo owner/repo --since 7d

  # Deep analysis with pattern detection
  python analyze_gha_logs.py --repo owner/repo --since 7d --analyze

  # JSON output for piping
  python analyze_gha_logs.py --repo owner/repo --since 7d --analyze --json

  # The ultimate power move
  python analyze_gha_logs.py --repo owner/repo --since 5d --analyze | \
    claude -p "Read these agent mistakes and fix CLAUDE.md. Put up a PR."
```

**What it detects:**
- Error frequency (file_not_found, test_failure, tool_blocked, max_turns_hit, etc.)
- Tool usage patterns (which tools does Claude use most?)
- Retry patterns (is Claude brute-forcing failures?)
- Duration analysis (are runs getting slower?)
- Failure details (which runs failed and why?)

**What it suggests:**
- CLAUDE.md rules to prevent recurring errors
- Tool allowlist adjustments
- Max-turns tuning
- Merge strategy improvements

---

## v1 Migration Notes (from beta)

The action was significantly restructured for GA (v1.0, Aug 2025):

| Beta (v0.x) | GA (v1.0) |
|---|---|
| `mode: "tag"` or `mode: "agent"` | Auto-detected (no `mode` input) |
| `direct_prompt` | `prompt` |
| `custom_instructions` | `claude_args: --append-system-prompt "..."` |
| `max_turns`, `model`, `allowed_tools` | All via `claude_args` |
| `@beta` tag | `@v1` tag |

Key change: everything that used to be a separate input now goes through `claude_args`,
which accepts any Claude Code CLI argument. This is simpler and more powerful.

---

## Key Learnings

1. **Interactive mode is the starting point** — just install and @claude works
2. **Automation mode unlocks the flywheel** — `prompt` input triggers immediate execution
3. **`--allowedTools` is the security boundary** — restrict Claude to what it needs
4. **Structured output makes Claude a CI decision engine** — not just a code writer
5. **Claude creates branches, not PRs** — human always in the loop
6. **The flywheel is the real value** — logs → analysis → CLAUDE.md → better behavior
7. **PR-from-Anywhere is orchestration** — any alert system can create issues that trigger Claude
