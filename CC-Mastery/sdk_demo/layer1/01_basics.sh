#!/bin/bash
# =============================================================================
# Layer 1, Level 1: Basic claude -p Invocations
# =============================================================================
# Run each block separately to see the output.
# These are building blocks — every later pattern uses these.
# =============================================================================

# --- 1A: Simplest form — question in, answer out ---
claude -p "What is the difference between TCP and UDP? Answer in 3 bullets."

# --- 1B: Text output (default) vs JSON output ---
# Text: just the answer string
claude -p "What is 2+2?" --output-format text

# JSON: full metadata envelope
claude -p "What is 2+2?" --output-format json
# Returns: {"type":"result","subtype":"success","result":"4","session_id":"...","total_cost_usd":0.003,...}

# --- 1C: Extract specific fields with Python (jq alternative for Windows) ---
claude -p "What is 2+2?" --output-format json | \
  python -c "import sys,json; d=json.load(sys.stdin); print(f'Answer: {d[\"result\"]}  Cost: \${d[\"total_cost_usd\"]}')"

# --- 1D: Choose your model ---
claude -p "Explain quicksort" --model sonnet      # Fast, cheap (~$0.003)
claude -p "Explain quicksort" --model opus         # Smart, expensive (~$0.03)

# --- 1E: Disable ALL tools (pure Q&A, no file access, no bash) ---
claude -p "Explain the CAP theorem" --tools ""
# Claude can ONLY generate text — can't read files, search, or run commands.
# Cheapest possible: 1 API call, no tool loops.
