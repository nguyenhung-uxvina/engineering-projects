# Module 12: settings.json Tuning
## CC-Mastery Final Module — Study Notes

**Date:** 2026-02-20
**Module:** 12 / 12 (final)
**Curriculum source:** CC_mastery_curriculum.md §Module 12

---

## 1. THE THREE-LAYER SETTINGS ARCHITECTURE

Claude Code uses **three overlapping settings files** at different scopes:

```
SCOPE           FILE                                    GIT STATUS
─────────────   ─────────────────────────────────────   ──────────────
Global user     ~/.claude/settings.json                 Never committed
Global local    ~/.claude/settings.local.json           Never committed
Project shared  <project>/.claude/settings.json         Committed (team shared)
Project local   <project>/.claude/settings.local.json   Gitignored (personal)
```

**Merge order (later overrides earlier):**
```
~/.claude/settings.json
    → ~/.claude/settings.local.json
        → <project>/.claude/settings.json
            → <project>/.claude/settings.local.json
```

**Key rule:** Hooks and permissions defined at project level apply only to that project.
Global hooks apply to ALL projects — use with caution.

---

## 2. CURRENT STATE AUDIT (CC-Mastery)

### 2.1 Global: ~/.claude/settings.json
```json
{
  "enabledPlugins": {
    "example-skills@anthropic-agent-skills": true
  }
}
```
**Assessment:** Minimal. Only plugin registration. No timeouts, no global hooks.

### 2.2 Project Shared: CC-Mastery/.claude/settings.json
Contains all 5 hooks (from Module 6):
- `PreToolUse/Bash` → `log_bash.py` + `block_commit.py`
- `PostToolUse/Write|Edit` → `track_file_changes.py`
- `UserPromptSubmit` → `prompt_hints.py`
- `Stop` → `stop_logger.py`

**Assessment:** Correct placement — hooks are project-specific, committed, shared.

### 2.3 Project Local: CC-Mastery/.claude/settings.local.json
25 auto-allow permission rules (personal convenience settings — not committed).

---

## 3. PERMISSIONS DEEP AUDIT

### 3.1 Security Risk Classification

```
Rule                                  │ Risk  │ Rationale                    │ Decision
──────────────────────────────────────┼───────┼──────────────────────────────┼──────────
mcp__hyperbrowser__scrape_webpage     │ LOW   │ Read-only web scraping        │ KEEP
WebFetch(domain:blog.sshh.io)         │ ZERO  │ STALE — Shrivu's blog only   │ REMOVE
Bash(wc:*)                            │ ZERO  │ Word count, read-only         │ KEEP
Bash(python:*) / python3:* / py:*     │ MED   │ Runs any Python — broad but   │ KEEP + note
                                      │       │ needed for curriculum scripts  │
Bash(grep:*)                          │ ZERO  │ Read-only search              │ KEEP
Bash(echo:*)                          │ ZERO  │ Print to stdout               │ KEEP
Bash(choco install:*)                 │ HIGH  │ Installs any software silently│ REMOVE ⚠️
Bash(pip install:*)                   │ MED   │ Installs Python packages      │ KEEP + note
Bash(git init:*)                      │ LOW   │ Creates repos                 │ KEEP
Bash(git add:*)                       │ LOW   │ Stages files                  │ KEEP
Bash(git commit:*)                    │ MED   │ Safe: block_commit.py is gate │ KEEP
Bash(find:*)                          │ ZERO  │ File search, read-only        │ KEEP
Bash(node:*)                          │ MED   │ Runs any JS file              │ KEEP (curriculum)
Bash(npm --version:*)                 │ ZERO  │ Read-only version check       │ KEEP
Bash(npm install:*)                   │ MED   │ Installs packages             │ KEEP (curriculum)
Bash(npx tsx:*)                       │ MED   │ Runs any TypeScript file      │ KEEP (curriculum)
Bash(npx tsc:*)                       │ LOW   │ Compilation only              │ KEEP
Bash(ls:*)                            │ ZERO  │ Directory listing, read-only  │ KEEP
Bash(gh api:*)                        │ MED   │ GitHub API (read + write)     │ KEEP (curriculum)
WebFetch(domain:raw.githubusercontent.com)│ LOW │ Fetches public GitHub files  │ KEEP
```

### 3.2 Key Finding: git commit is safe despite being auto-allowed

`block_commit.py` (PreToolUse hook) blocks the commit if pytest fails — regardless of
whether the `git commit` command is in the allow list. The allow list only removes the
*human approval prompt*. Hooks still fire. The security gate is intact.

```
Allow list: skips the "Allow this?" dialog for git commit
Hook:       still runs block_commit.py → blocks if tests fail

Result: No interruption + no quality bypass = correct design
```

### 3.3 Removed Items Rationale

**`Bash(choco install:*)`** — Installing system-level software has irreversible effects and
a large blast radius. Even in a learning context, software installation should require human
confirmation. This is the Module 6 principle: "hooks/permissions for things that MUST happen,
not convenience." Software installation is not a curriculum necessity — it was added once and
never revisited.

**`WebFetch(domain:blog.sshh.io)`** — Added during Module 1 to auto-fetch Shrivu's blog.
Modules 1-12 are complete. Keeping stale allow-rules is the settings.json equivalent of
dead code — it expands the attack surface without benefit.

---

## 4. KEY SETTINGS REFERENCE

### 4.1 Timeout Settings (Environment Variables in settings.json)

```json
{
  "env": {
    "BASH_MAX_TIMEOUT_MS": "600000",
    "MCP_TOOL_TIMEOUT": "120000"
  }
}
```

**When to adjust:**
- `BASH_MAX_TIMEOUT_MS` — Default: 120,000ms (2 min). Increase for:
  - Long-running Python scripts (ML training, data processing)
  - SDK pipeline scripts (sdk_pipeline_VN-RANGE-001.py could run 5-10 min)
  - Build processes, compilation
- `MCP_TOOL_TIMEOUT` — Default: 60,000ms (1 min). Increase for:
  - Slow MCP servers (network latency, rate limiting)
  - Heavy scraping operations (Hyperbrowser)

### 4.2 Proxy Settings (for traffic debugging)

```json
{
  "env": {
    "HTTPS_PROXY": "http://localhost:8080",
    "HTTP_PROXY": "http://localhost:8080"
  }
}
```

**Use case:** Route Claude Code traffic through mitmproxy or Charles Proxy to inspect:
- What tools are called (tool use telemetry)
- MCP server communication
- Raw API request/response pairs

**Defense use case:** Audit what IRONMESH agents actually send to the API — verify no
PII or classified design details leave the system in unexpected ways.

### 4.3 apiKeyHelper (Enterprise Pattern)

```json
{
  "apiKeyHelper": "/path/to/key-fetcher.sh"
}
```

**How it works:** Instead of storing `ANTHROPIC_API_KEY` directly, CC calls this script
to fetch the key at runtime. The script can:
- Fetch from AWS Secrets Manager / Azure Key Vault / HashiCorp Vault
- Rotate keys automatically
- Apply usage-based billing per team/project

**Why it matters for Workshop X:** When training Vietnamese military operators to use
IRONMESH's AI components, a shared key via `apiKeyHelper` means:
- Single key managed centrally (no per-seat licenses)
- Usage tracked per session (attribution for billing)
- Key rotation without touching individual workstations

### 4.4 Permissions Format

```json
{
  "permissions": {
    "allow": ["Bash(command:*)", "WebFetch(domain:example.com)"],
    "deny":  ["Bash(rm:*)", "Bash(curl:*) "]
  }
}
```

**Allow vs. Deny semantics:**
- `allow` → skip the "Allow this?" prompt automatically
- `deny` → block permanently, no override possible
- No entry → show the "Allow this?" prompt (default behavior)

**Best practice:** Use `deny` for truly dangerous commands (rm, curl to external, etc.)
rather than relying on prompts. Prompts can be bypassed by impatient operators.

---

## 5. WORKSHOP X DEFENSE SETTINGS TEMPLATE

For future IRONMESH development projects, this settings.json template applies defense-appropriate
controls:

```json
// <project>/.claude/settings.json — committed, team shared
{
  "env": {
    "BASH_MAX_TIMEOUT_MS": "600000",
    "MCP_TOOL_TIMEOUT": "120000"
  },
  "permissions": {
    "deny": [
      "Bash(rm:*)",
      "Bash(rmdir:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(choco install:*)",
      "Bash(apt install:*)",
      "Bash(pip install:*)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "python .claude/hooks/log_bash.py",
          "statusMessage": "Audit logging..."
        }]
      }
    ]
  }
}
```

```json
// <project>/.claude/settings.local.json — gitignored, personal approvals
{
  "permissions": {
    "allow": [
      "Bash(python:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(ls:*)",
      "Bash(grep:*)"
    ]
  }
}
```

**Design rationale:**
- Deny list in shared settings = team-wide safety baseline (no one bypasses)
- Allow list in local settings = personal workflow convenience (doesn't leak via git)
- Audit hook in shared settings = all Bash commands logged across team
- Timeouts in shared settings = consistent behavior across environments

---

## 6. MODULE 12 EXERCISE RESULTS

### Exercise 1: Reviewed settings.json ✅
Three files audited: global (minimal), project shared (hooks only), project local (permissions).
Full audit documented in §3 above.

### Exercise 2: Audited permissions ✅
25 rules reviewed. 2 removed (choco install — HIGH risk, blog.sshh.io — stale).
23 rules retained with risk classification documented.

### Exercise 3: Set appropriate timeouts ✅
Added `BASH_MAX_TIMEOUT_MS: 600000` and `MCP_TOOL_TIMEOUT: 120000` to global settings.json.
Rationale: SDK pipeline scripts for VN-RANGE-001 can exceed the default 2-minute timeout.

---

## 7. MASTERY CHECKLIST — FINAL STATUS

### Beginner (Modules 1-4) ✅
- [x] CLAUDE.md is guardrails, not a manual (CC-Mastery + Engineering CLAUDE.md)
- [x] Using Document & Clear (progress.md + /checkpoint command)
- [x] Have 2-3 personal slash commands (/checkpoint, /catchup, /pr)
- [x] Can resume/continue sessions effectively (--resume, --continue, /catchup)

### Intermediate (Modules 5-7) ✅
- [x] Always plan before complex changes (planning_demo.py verified higher exploration ratio)
- [x] Block-at-commit hooks enforcing tests (block_commit.py)
- [x] Using Task(...) for dynamic delegation, not rigid subagents (master-clone confirmed)

### Advanced (Modules 8-12) ✅
- [x] Skills replace most MCPs (brave_search → skill, task-clarification skill converted)
- [x] MCPs used only as secure gateways (project_tracker.py with FastMCP)
- [x] SDK used for batch operations and prototyping (VN-RANGE-001 pipeline script)
- [x] GHA creating a self-improving feedback loop (analyze_gha_logs.py → CLAUDE.md)
- [x] settings.json tuned for team/enterprise needs (this module)

---

**ALL 12 MODULES COMPLETE.**

*The Flywheel is running: GHA logs → CLAUDE.md improvements → better agents → fewer bugs.*
