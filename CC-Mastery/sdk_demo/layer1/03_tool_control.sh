#!/bin/bash
# =============================================================================
# Layer 1, Level 3: Tool Restriction Patterns
# =============================================================================
# THE SECURITY MODEL:
#   --tools          = whitelist (ONLY these tools exist)
#   --allowedTools   = auto-approve (these don't need human confirmation)
#   --disallowedTools = blacklist (remove from model's awareness)
#
# PERMISSION MODES:
#   default        = ask human for each tool use
#   acceptEdits    = auto-approve Read/Edit/Write
#   bypassPermissions = auto-approve EVERYTHING (dangerous!)
#   plan           = read-only exploration
# =============================================================================

# --- 3A: Read-Only Analysis (safest) ---
# Agent can read and search, but CANNOT modify anything
claude -p "Find all TODO comments in this project" \
  --tools "Read,Glob,Grep"
# No Bash, no Edit, no Write → zero risk of modification

# --- 3B: Controlled Edit (most common for automation) ---
# Agent can read + edit existing files, but NOT create new ones or run commands
claude -p "Add type hints to sdk_demo/testbed/utils.py" \
  --allowedTools "Read" "Edit" \
  --permission-mode acceptEdits
# Note: --allowedTools takes separate quoted strings, NOT comma-separated

# --- 3C: Specific Bash Commands Only ---
# Allow git operations but nothing else
claude -p "Show me the last 5 commits with their diffs" \
  --allowedTools "Bash(git log *)" "Bash(git diff *)" "Bash(git show *)"
# Prefix matching: "Bash(git log *)" matches:
#   git log --oneline -5    ✓
#   git log --all --graph   ✓
#   git loggerhead          ✗ (no space after "log")

# --- 3D: Test Runner Pattern ---
# Allow running tests + reading files, but no edits
claude -p "Run the test suite and explain any failures" \
  --allowedTools "Bash(pytest *)" "Bash(python -m pytest *)" "Read" "Glob"
# Agent can diagnose but not fix — human decides what to change

# --- 3E: Fix-and-Test Pattern ---
# Allow edit + specific test command only
claude -p "Fix the failing test in test_utils.py, then verify it passes" \
  --allowedTools "Read" "Edit" "Bash(pytest *)" \
  --permission-mode acceptEdits \
  --max-turns 8
# Agent reads → fixes → runs tests → checks result → iterates if needed

# --- 3F: Blacklist Dangerous Commands ---
# Allow everything EXCEPT destructive operations
claude -p "Clean up the project structure" \
  --disallowedTools "Bash(rm *)" "Bash(git push *)" "Bash(git reset *)"
# Agent has full toolbox minus the dangerous ones

# --- 3G: Pure Q&A — No Tools At All ---
claude -p "Explain dependency injection in 3 sentences" --tools ""
# Zero tool calls, single API roundtrip, cheapest possible invocation

# =============================================================================
# DECISION MATRIX: Which pattern to use?
# =============================================================================
#
# | Scenario               | Pattern                | Risk Level |
# |------------------------|------------------------|------------|
# | Code review            | --tools "Read,Glob,Grep" | None     |
# | Auto-fix bugs          | --allowedTools Read Edit + acceptEdits | Low |
# | Run tests              | --allowedTools Bash(pytest) Read | Low |
# | Fix + test loop        | Read Edit Bash(pytest) + acceptEdits | Medium |
# | Full automation (CI)   | bypassPermissions | High |
# | Pure Q&A               | --tools "" | None |
#
# Rule of thumb: give the MINIMUM tools needed for the task.
# =============================================================================
