---
title: Claude Code Mastery Curriculum
source: https://blog.sshh.io/p/how-i-use-every-claude-code-feature
author: Shrivu Shankar
created: 2026-02-14
status: active
---

# Claude Code Mastery Curriculum

> Based on "How I Use Every Claude Code Feature" by Shrivu Shankar
> Philosophy: "Shoot and forget" - delegate, set context, judge by final PR.

---

## Learning Path Overview

| # | Module | Difficulty | Status |
|---|--------|-----------|--------|
| 1 | CLAUDE.md Mastery | Beginner | [ ] |
| 2 | Context Management | Beginner | [ ] |
| 3 | Custom Slash Commands | Beginner | [ ] |
| 4 | Resume, Continue & History | Beginner | [ ] |
| 5 | Planning Mode | Intermediate | [ ] |
| 6 | Hooks | Intermediate | [ ] |
| 7 | Custom Subagents | Intermediate | [ ] |
| 8 | Skills | Advanced | [ ] |
| 9 | MCP (Model Context Protocol) | Advanced | [ ] |
| 10 | Claude Code SDK | Advanced | [ ] |
| 11 | Claude Code GitHub Action | Advanced | [ ] |
| 12 | settings.json Tuning | Advanced | [ ] |

---

## Module 1: CLAUDE.md Mastery

### Key Idea
CLAUDE.md is the agent's "constitution" - not a manual, but a curated set of guardrails addressing actual agent mistakes.

### Principles
1. **Start with Guardrails, Not a Manual** - Document rules born from real mistakes, not hypothetical ones
2. **Don't @-File Docs** - Mention paths, don't embed content. Say "For FooBarError see path/to/docs.md"
3. **Don't Just Say "Never"** - Always provide alternatives: "Never X, prefer Y"
4. **Use as a Forcing Function** - If your CLAUDE.md is bloated, simplify your tooling

### Anti-Patterns
- Embedding entire API docs (bloats context on every run)
- Negative-only constraints without alternatives
- Creating comprehensive manuals instead of targeted rules

### Structure Template
```markdown
# Project Name

## Mistakes Not To Repeat
<!-- Born from real corrections -->

## Code Style
- Always ...
- Never X, prefer Y

## Tools
- Test with <command>
- For <complex usage> see path/to/docs.md

## Build & Deploy
- ...
```

### Exercise
1. Review your current CLAUDE.md - is it guardrails or a manual?
2. Delete anything that isn't born from a real mistake or critical workflow
3. For every "Never", add a "prefer Y" alternative
4. Move detailed docs to separate files, reference by path only

---

## Module 2: Context Management (Compact, Context & Clear)

### Key Idea
The 200k token window is finite. Fresh session = ~20k baseline, leaving ~180k for work. Managing this is critical.

### Three Workflows (Ranked)

| Workflow | When | How |
|----------|------|-----|
| `/clear` + `/catchup` | Simple restart | Clears state, re-reads changed files in git branch |
| Document & Clear | Complex multi-step work | Dump progress to `.md` file, `/clear`, resume from doc |
| `/compact` | **Avoid** | Opaque, lossy, error-prone |

### Why /compact Is Dangerous
- You can't see what was lost in compression
- Critical context may silently disappear
- Errors compound as the agent loses track of prior decisions

### The "Document & Clear" Pattern
```
1. Ask Claude to dump current progress/decisions to a .md file
2. /clear
3. Resume: "Read progress.md and continue from where we left off"
```
This creates **durable external memory** that survives context resets.

### Exercise
1. Run `/context` mid-session to see your token usage
2. Practice the Document & Clear workflow on a multi-step task
3. Compare results: `/compact` vs `/clear` + `/catchup`

---

## Module 3: Custom Slash Commands

### Key Idea
Simple shortcuts for frequently used prompts. Keep them minimal.

### Author's Setup (Just 2!)
- `/catchup` - Reads all changed files in current git branch
- `/pr` - Cleans code, stages, prepares pull request

### Anti-Pattern
Long lists of complex slash commands that force rigid workflows. The whole point of an agent is flexibility.

### How to Create
Place `.md` files in `.claude/commands/`:
```
.claude/commands/
  catchup.md    -> "Read all files changed in the current git branch..."
  pr.md         -> "Clean up code, stage changes, prepare PR..."
```

### Exercise
1. Identify your 2-3 most repeated prompts
2. Create slash command files for them
3. Resist adding more than 5 - if you need more, improve your CLAUDE.md

---

## Module 4: Resume, Continue & History

### Key Idea
Sessions are persistent and searchable - use them for meta-learning.

### Commands
| Command | Purpose |
|---------|---------|
| `claude --continue` | Resume last session |
| `claude --resume` | Pick from session history |

### Hidden Power: Session History
- Stored in `~/.claude/projects/`
- Analyze past sessions for patterns
- Find how the agent overcame specific errors
- Feed insights back into CLAUDE.md

### Exercise
1. Try `claude --continue` after closing a session
2. Use `claude --resume` to browse past conversations
3. Review a past session - find one thing to add to CLAUDE.md

---

## Module 5: Planning Mode

### Key Idea
Always plan before implementing complex changes. Align on approach before writing code.

### When to Use
- Any "large" feature change
- Multi-file refactors
- Architectural decisions
- Anything where the wrong approach wastes significant tokens

### Benefits
- Aligns human and agent on strategy
- Builds intuition for minimal context requirements
- Catches misunderstandings before costly implementation

### Professional Pattern
Build custom planning tools (via SDK) that:
- Align with your team's technical design format
- Enforce internal best practices (code structure, security, privacy)
- Let engineers "vibe plan" like a senior architect

### Exercise
1. On your next complex task, force yourself to use planning mode first
2. Compare: planned implementation vs. "just start coding"
3. Note how planning reduces wasted iterations

---

## Module 6: Hooks

### Key Idea
Hooks = deterministic "must-do" rules. CLAUDE.md = "should-do" suggestions.
Use hooks for things that MUST happen, not things that should happen.

### Two Types

#### 1. Block-at-Submit (Primary)
Wraps `Bash(git commit)` with validation:
```
PreToolUse hook on Bash(git commit):
  -> Check /tmp/agent-pre-commit-pass exists
  -> If not: block commit, force test-and-fix loop
  -> Only pass when all tests green
```
Forces the agent into a test-fix loop until the build passes.

#### 2. Hint Hooks (Secondary)
Non-blocking feedback for suboptimal patterns. Gentle nudges, not hard blocks.

### Anti-Pattern
**Block-at-Write hooks** - blocking Edit/Write confuses the agent mid-plan. Let it finish work, then validate at commit time.

### Exercise
1. Create a simple PreToolUse hook that logs all Bash commands
2. Build a block-at-commit hook that requires tests to pass
3. Observe how the agent self-corrects when blocked

---

## Module 7: Custom Subagents

### Key Idea
Let the main agent manage its own delegation. Don't force rigid specialist hierarchies.

### The Problem with Custom Subagents
1. **Context Gating** - Hidden context prevents holistic reasoning
2. **Forced Workflows** - Rigid delegation patterns break when reality is messy

### Better Alternative: Master-Clone Model
```
Main Agent (has full CLAUDE.md context)
  └── Spawns Task(...) / Explore(...) clones as needed
      └── Clones inherit context, main agent decides when/how
```

### Key Insight
Instead of `(X + Y + Z) * N` subagents, use `(X + Y) * N + Z` - put context in CLAUDE.md and let the main agent dynamically delegate via built-in Task/Explore.

### Anti-Pattern
Pre-defined specialist agents (PythonTests, SecurityReviewer, etc.) that fragment context and force unnatural workflows.

### Exercise
1. Try a complex task using only Task(...) for delegation
2. Compare: rigid subagent routing vs. letting Claude self-delegate
3. Note when dynamic delegation produces better results

---

## Module 8: Skills

### Key Idea
Skills > MCP for most use cases. They formalize the "scripting" model - giving agents raw environment access (binaries, scripts, docs) instead of rigid API abstractions.

### Agent Autonomy Evolution
```
Stage 1: Single massive prompt (brittle)
Stage 2: Tool calling / APIs (better, but creates abstractions)
Stage 3: Scripting / Skills (raw environment access - most powerful)
```

### Why Skills Beat MCP
- More robust and flexible
- SKILL.md organizes and exposes CLIs/scripts
- Agent uses raw tools like a human developer would
- No brittle API abstraction layer

### Skill Types
1. **Single Prompt** - Simple instruction set
2. **Tool Calling** - Skills that invoke tools
3. **Scripting** - Skills that run scripts on-the-fly against the environment

### Exercise
1. Identify a workflow you currently do manually with CLI tools
2. Create a SKILL.md that exposes those tools to Claude
3. Compare: MCP approach vs. Skills approach for the same task

---

## Module 9: MCP (Model Context Protocol)

### Key Idea
MCP's new role: **secure gateway** for sensitive operations. Not API abstraction.

### Recommended Design (Minimal)
```
download_raw_data(filters...)        # Data access
take_sensitive_gated_action(args...) # Controlled mutations
execute_code_in_environment(code...) # Sandboxed execution
```

### When to Use MCP
- Stateful environments (e.g., Playwright for browser automation)
- Sensitive operations requiring auth/security gating
- When the agent needs a secure entry point for scripting

### When NOT to Use MCP
- Stateless tools (Jira, AWS, GitHub) - migrate to simple CLIs instead
- Read-only data access - use Skills/scripts
- Anything where a CLI wrapper would suffice

### Author's Practice
Only uses Playwright MCP (stateful). Migrated all stateless tools to CLIs.

### Exercise
1. Audit your current MCP servers - which are truly stateful?
2. Migrate one stateless MCP to a CLI wrapper
3. Build one MCP as a "secure gateway" with 2-3 high-level tools

---

## Module 10: Claude Code SDK

### Key Idea
Claude Code is both a CLI and a powerful SDK for building new agents - coding and non-coding.

### Three Use Patterns

#### 1. Massive Parallel Scripting
```bash
# Run across many files/repos in parallel
claude -p "in /pathA change all refs from foo to bar"
claude -p "in /pathB change all refs from foo to bar"
# More scalable than interactive delegation
```

#### 2. Internal Chat Tools
Wrap complex processes for non-technical users. Build "v0-at-home" style tools.

#### 3. Rapid Agent Prototyping
Test agentic ideas before building full deployment scaffolding. Use SDK before reaching for LangChain/CrewAI.

### Exercise
1. Try `claude -p "..."` for a batch refactor across multiple files
2. Prototype a simple non-coding agent using the SDK
3. Compare SDK vs. a framework (LangChain) for the same task

---

## Module 11: Claude Code GitHub Action

### Key Idea
Run Claude Code in CI/CD. Full agent logs = auditable, self-improving system.

### The Flywheel
```
Bugs in GHA logs
  -> Improved CLAUDE.md / CLIs
    -> Better Agent behavior
      -> Fewer bugs in GHA logs
```

### Power Move
```bash
# Query recent agent logs, find patterns, auto-fix
$ query-claude-gha-logs --since 5d | claude -p "see what the other claudes
  were getting stuck on and fix it, then put up a PR"
```

### Advanced: PR-from-Anywhere
Users trigger fixes from Slack, Jira, CloudWatch alerts -> GHA runs Claude -> Returns tested PRs.

### Policy Question
AI-initiated PRs with no human prompter: author recommends 2 human approvals.

### Exercise
1. Set up Claude Code GHA on a test repo
2. Review agent logs for common mistakes
3. Feed findings back into CLAUDE.md

---

## Module 12: settings.json Tuning

### Key Idea
Fine-grained control over Claude Code's behavior, networking, and permissions.

### Key Settings

| Setting | Purpose |
|---------|---------|
| `HTTPS_PROXY` / `HTTP_PROXY` | Debug raw traffic, network sandboxing |
| `MCP_TOOL_TIMEOUT` | Increase for slow MCP operations |
| `BASH_MAX_TIMEOUT_MS` | Increase for long-running commands |
| `ANTHROPIC_API_KEY` via `apiKeyHelper` | Enterprise key management |
| `"permissions"` | Self-audit allowed auto-run commands |

### Enterprise Pattern: apiKeyHelper
- Eliminates per-seat licensing
- Shifts to usage-based pricing (accounts for high variance)
- Engineers can tinker with non-CC LLM scripts under single account

### Exercise
1. Review your current settings.json
2. Audit your `permissions` - are you auto-allowing too much?
3. Set appropriate timeouts for your workflow

---

## Mastery Checklist

### Beginner (Modules 1-4)
- [ ] CLAUDE.md is guardrails, not a manual
- [ ] Using Document & Clear for complex sessions
- [ ] Have 2-3 personal slash commands
- [ ] Can resume/continue sessions effectively

### Intermediate (Modules 5-7)
- [ ] Always plan before complex changes
- [ ] Have block-at-commit hooks enforcing tests
- [ ] Using Task(...) for dynamic delegation, not rigid subagents

### Advanced (Modules 8-12)
- [ ] Skills replace most MCPs in workflow
- [ ] MCPs used only as secure gateways
- [ ] SDK used for batch operations and prototyping
- [ ] GHA creating a self-improving feedback loop
- [ ] settings.json tuned for team/enterprise needs

---

## Core Philosophy (Shrivu's Principles)

1. **"Shoot and forget"** - Delegate, set context, judge by final PR
2. **Guardrails > Manuals** - CLAUDE.md should be born from real mistakes
3. **Skills > MCP** - Raw environment access beats rigid APIs
4. **Dynamic > Rigid** - Let agents self-delegate, don't pre-define hierarchies
5. **Plan > Code** - Always align on strategy before implementation
6. **Validate at commit, not at write** - Let agents complete work, then check
7. **The Flywheel** - Bugs -> Better CLAUDE.md -> Better Agent -> Fewer Bugs
