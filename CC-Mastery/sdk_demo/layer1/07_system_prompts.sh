#!/bin/bash
# =============================================================================
# Layer 1, Level 7: System Prompt Control
# =============================================================================
# TWO MODES:
#   --append-system-prompt  = ADD to Claude Code's default prompt (safe)
#   --system-prompt         = REPLACE Claude Code's default prompt (risky)
#
# When to use which:
#   append → You want Claude Code's tools + your extra rules
#   replace → You want a completely custom agent persona
# =============================================================================

# --- 7A: Append — Add constraints while keeping defaults ---
# Claude still has all tools, CLAUDE.md, etc. — PLUS your rules.
claude -p "Review sdk_demo/testbed/utils.py" \
  --append-system-prompt "You are a senior Python developer who follows PEP 8 strictly. \
    Always mention specific PEP 8 rules by number when flagging issues." \
  --tools "Read"

# --- 7B: Append from file — For longer instructions ---
# Create a reviewer persona file:
cat > /tmp/reviewer_persona.md << 'EOF'
You are a defense systems code reviewer specializing in:
- Safety-critical software (DO-178C / MIL-STD-498)
- Real-time embedded systems
- Vietnamese defense standards (TCVN)

When reviewing code, always check:
1. Is every error path handled?
2. Are there any unbounded loops or allocations?
3. Is the code deterministic (no random, no time-dependent logic)?
4. Could this run on an embedded target (no heap allocation in hot paths)?

Format: table with columns [File, Line, Severity, MIL-STD Ref, Issue]
EOF

claude -p "Review the code in sdk_demo/testbed/" \
  --append-system-prompt-file /tmp/reviewer_persona.md \
  --tools "Read,Glob,Grep"

# --- 7C: Replace — Completely custom agent ---
# WARNING: This REMOVES all Claude Code defaults.
# No CLAUDE.md loading, no default tool instructions.
# Use when you want a pure, minimal agent.
claude -p "What are the OWASP Top 10 for 2025?" \
  --system-prompt "You are a cybersecurity expert. \
    Answer concisely with specific CVE references where applicable. \
    Never suggest tools or code changes — only analyze." \
  --tools ""

# --- 7D: Combining persona + structured output ---
# Security auditor that returns structured findings
claude -p "Audit sdk_demo/testbed/ for security issues" \
  --append-system-prompt "You are a penetration tester. \
    Rate all findings using CVSS v3.1 scores. \
    Be paranoid — flag anything suspicious." \
  --tools "Read,Glob,Grep" \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "findings": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "file": {"type": "string"},
            "issue": {"type": "string"},
            "cvss_score": {"type": "number"},
            "recommendation": {"type": "string"}
          },
          "required": ["file", "issue", "cvss_score", "recommendation"]
        }
      }
    },
    "required": ["findings"]
  }'

# =============================================================================
# INSIGHT: --append-system-prompt is the MOST USEFUL flag
#
# It lets you create specialized "modes" without losing Claude Code's
# built-in capabilities. Think of it as "personality injection":
#
#   Base Claude Code + "You are a security reviewer"  → Security agent
#   Base Claude Code + "You are a tech writer"        → Docs agent
#   Base Claude Code + "You follow MIL-STD-498"       → Defense agent
#   Base Claude Code + "You only speak Vietnamese"    → VN agent
#
# Same tool, different persona, same session.
# =============================================================================
