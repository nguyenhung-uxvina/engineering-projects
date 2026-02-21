#!/bin/bash
# =============================================================================
# STEP 2 EXERCISE: Batch Type Hints with claude -p
# =============================================================================
# Run from Git Bash: ./sdk_demo/run_batch_typehints.sh
#
# What this demonstrates:
#   - claude -p (headless mode)
#   - --allowedTools (restrict what agent can do)
#   - --permission-mode acceptEdits (auto-approve file edits)
#   - --max-turns 3 (prevent runaway — type hints need 1-2 turns max)
#   - --no-session-persistence (ephemeral, no disk buildup)
#   - --output-format json (machine-readable result)
# =============================================================================

set -euo pipefail

TESTBED="$(cd "$(dirname "$0")/testbed" && pwd)"
echo "=== Batch Type Hint Addition ==="
echo "Target: $TESTBED"
echo ""

# --- Sequential mode (safe, debuggable) ---
for file in "$TESTBED"/*.py; do
    filename=$(basename "$file")
    echo "[$filename] Processing..."

    # ANATOMY OF THIS COMMAND:
    #
    # claude -p "..."                     ← headless mode, prompt as string
    #   --allowedTools "Read" "Edit"      ← can ONLY read and edit files
    #                                       (no Bash, no Write, no Glob)
    #   --permission-mode acceptEdits     ← auto-approve Edit tool calls
    #   --max-turns 3                     ← safety: stop after 3 tool uses
    #   --no-session-persistence          ← don't save to disk
    #   --output-format json              ← get structured result

    result=$(claude -p \
        "Add Python type hints to all functions and methods in $file. \
         Only add type annotations — do NOT change any logic. \
         Use standard library types (list, dict, str, int, float, bool). \
         For unknown types, use Any from typing." \
        --allowedTools "Read" "Edit" \
        --permission-mode acceptEdits \
        --max-turns 3 \
        --no-session-persistence \
        --output-format json)

    # Extract cost from JSON result
    cost=$(echo "$result" | python -c "import sys,json; print(json.load(sys.stdin).get('total_cost_usd','?'))")
    echo "[$filename] Done — cost: \$$cost"
    echo ""
done

echo "=== Results ==="
echo "Check the files in $TESTBED — they should now have type hints."
echo ""

# Show diff if in a git repo
if git rev-parse --git-dir > /dev/null 2>&1; then
    echo "=== Git Diff ==="
    git diff "$TESTBED"
fi
