# AI-Initiated PR Policy

## The Problem

When Claude Code runs in GitHub Actions, it can create branches and suggest PRs
with **no human prompter** — especially in automation mode (scheduled, alert-triggered).
This creates a new class of code change that doesn't fit traditional review models.

## Policy Recommendations

### Tier 1: Human-Prompted (Low Risk)
**Trigger:** Developer @-mentions Claude in an issue or PR comment.

| Control | Requirement |
|---------|------------|
| Human in loop | Yes — the developer who triggered |
| Approvals | Standard (1 review per team policy) |
| Branch protection | Standard |
| Auto-merge | Allowed if CI passes + 1 approval |

### Tier 2: Event-Triggered (Medium Risk)
**Trigger:** PR opened/updated (auto-review), issue labeled, assignment.

| Control | Requirement |
|---------|------------|
| Human in loop | Indirect — someone created the PR/issue |
| Approvals | **2 human approvals** (author's recommendation) |
| Branch protection | Require up-to-date branch, CI pass |
| Auto-merge | **Not allowed** — human must click merge |
| Tool restrictions | Read-only for reviews; write-list for implementations |

### Tier 3: Fully Autonomous (High Risk)
**Trigger:** Scheduled cron, CloudWatch alert, repository_dispatch.

| Control | Requirement |
|---------|------------|
| Human in loop | No — triggered by automation |
| Approvals | **2 human approvals** (mandatory) |
| Branch protection | Require up-to-date, CI pass, CODEOWNERS review |
| Auto-merge | **Never** |
| Tool restrictions | Strict allowlist, no Bash without prefix |
| Max turns | Capped (e.g., --max-turns 15) |
| Audit | `display_report: true`, logs retained 90 days |
| Notification | Slack/email notification on branch creation |

## Implementation

### Branch Protection Rules

```
Settings > Branches > Branch protection rules
  Pattern: main (or master)
  ✅ Require pull request reviews before merging
    → Required approvals: 2
  ✅ Require status checks to pass
  ✅ Require branches to be up to date
  ✅ Require review from Code Owners
  ❌ Allow auto-merge (disabled for Tier 2+3)
```

### CODEOWNERS for AI Changes

```
# .github/CODEOWNERS
# Claude branches require team-lead review
claude/**  @team-leads
```

### Workflow-Level Controls

```yaml
# In your GHA workflow:
claude_args: |
  --max-turns 15                    # Cap computation
  --allowedTools "Read,Write,Edit"  # No arbitrary Bash
  --model claude-sonnet-4-6         # Cost-conscious model for automation

# Don't expose full output in public repos
show_full_output: false
```

### Labeling Convention

All AI-created PRs should be labeled for tracking:

| Label | When Applied |
|-------|-------------|
| `ai-generated` | All Claude-created branches |
| `needs-2-approvals` | Tier 2 and 3 |
| `autonomous` | Tier 3 only |
| `human-prompted` | Tier 1 only |

## Audit Trail

Every Claude GHA run produces:
1. **Step Summary** — formatted execution report (visible in Actions tab)
2. **Execution file** — full output (available as artifact)
3. **Session ID** — can resume the exact session for follow-up
4. **Git commits** — standard git history with `Co-Authored-By: Claude`

Retain logs for at least 90 days. The flywheel depends on being able to query
historical patterns.

## Review Checklist for AI-Generated PRs

Before approving any Claude-generated PR:

- [ ] Read the full diff — don't just skim
- [ ] Check for hallucinated imports or non-existent APIs
- [ ] Verify tests actually test the new behavior (not just pass)
- [ ] Look for hardcoded values that should be configurable
- [ ] Ensure no secrets or sensitive data in the diff
- [ ] Check that the change matches the issue/request intent
- [ ] Run the code locally if the change is non-trivial
