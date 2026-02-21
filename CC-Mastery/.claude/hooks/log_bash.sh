#!/bin/bash
# Hook: Log all Bash commands Claude executes
# Type: PreToolUse (matcher: Bash)
# Purpose: Exercise 1 — Module 6 (Hooks)
#
# Input: JSON on stdin with tool_input.command
# Output: exit 0 (allow) — this is a logging hook, never blocks

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // "unknown"')
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
LOG_FILE="$CLAUDE_PROJECT_DIR/.claude/hooks/bash_command_log.txt"

echo "$TIMESTAMP | $COMMAND" >> "$LOG_FILE"

exit 0
