#!/bin/bash
# =============================================================================
# Layer 1, Level 4: Session Chaining
# =============================================================================
# Each `claude -p` is independent by default — no shared memory.
# Session chaining lets you build multi-step workflows where
# Claude REMEMBERS what happened in previous steps.
#
# THREE MECHANISMS:
#   --continue (-c)    = resume the MOST RECENT session
#   --resume (-r) ID   = resume a SPECIFIC session by ID
#   --session-id UUID  = use exact session UUID
# =============================================================================

# --- 4A: Capture session ID from first step ---
echo "=== Step 1: Analyze ==="
session_id=$(claude -p "Read all Python files in sdk_demo/testbed/ and summarize what each one does." \
  --tools "Read,Glob" \
  --output-format json | python -c "import sys,json; print(json.load(sys.stdin)['session_id'])")

echo "Session ID: $session_id"

# --- 4B: Continue with context (Claude remembers Step 1) ---
echo ""
echo "=== Step 2: Deepen (using --resume) ==="
claude -p "Which of those files has the worst code quality? Explain why." \
  --resume "$session_id" \
  --tools "Read"
# Claude already knows the files from Step 1 — doesn't need to re-read them!

# --- 4C: Continue again ---
echo ""
echo "=== Step 3: Act (using --resume) ==="
claude -p "Write a brief code review summary for all three files as a markdown table." \
  --resume "$session_id" \
  --tools ""
# No tools needed — Claude generates from memory of Steps 1 & 2

# =============================================================================
# ALTERNATIVE: --continue (-c) for quick follow-ups
# =============================================================================

# First command (starts a new session)
claude -p "What design patterns does sdk_demo/testbed/models.py use?" --tools "Read"

# Follow-up (continues the MOST RECENT session, whatever it was)
claude -c -p "How would you improve it with dataclasses?"
# Simpler than capturing session_id, but only works for the latest session.

# =============================================================================
# PATTERN: Analysis Pipeline
# =============================================================================
#
#   Step 1: claude -p "Read and analyze" --tools "Read,Glob"    → capture session_id
#   Step 2: claude -p "Focus on X" --resume $id --tools "Read"  → deeper analysis
#   Step 3: claude -p "Generate report" --resume $id --tools "" → output (no tools)
#
# Each step adds to Claude's understanding WITHOUT re-reading everything.
# Cost efficient: files read once in Step 1, context carried forward.
#
# VERSUS without chaining:
#   Step 1: Read all files → $0.02
#   Step 2: Read all files AGAIN + analyze → $0.04  (wasteful!)
#   Step 3: Read all files AGAIN + generate → $0.06  (3x cost!)
#
# With chaining: $0.02 + $0.01 + $0.005 = ~$0.035 (much cheaper)
# =============================================================================
