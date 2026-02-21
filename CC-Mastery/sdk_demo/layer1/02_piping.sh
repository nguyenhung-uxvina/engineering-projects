#!/bin/bash
# =============================================================================
# Layer 1, Level 2: Piping Content Into claude -p
# =============================================================================
# The pipe pattern: CONTENT | claude -p "INSTRUCTION"
# Claude sees stdin as context, then follows the instruction.
# This is the most powerful one-liner pattern.
# =============================================================================

# --- 2A: Pipe a file for analysis ---
cat sdk_demo/testbed/utils.py | claude -p "List all functions and their parameters."

# --- 2B: Pipe git diff for code review ---
git diff HEAD~1 | claude -p "Review this diff. Flag any bugs or style issues."

# --- 2C: Pipe error logs for diagnosis ---
# (simulate with echo)
echo "ERROR 2026-02-17 14:32:01 ConnectionRefusedError: [Errno 111] Connection refused
ERROR 2026-02-17 14:32:02 Retry attempt 1/3 failed
ERROR 2026-02-17 14:32:05 Retry attempt 2/3 failed
ERROR 2026-02-17 14:32:10 Retry attempt 3/3 failed
CRITICAL 2026-02-17 14:32:10 Service unavailable: database backend" | \
  claude -p "Diagnose this error. What is the root cause and how to fix it?"

# --- 2D: Pipe command output for summarization ---
pip list 2>/dev/null | claude -p "Group these Python packages by category (web, data, testing, etc.)"

# --- 2E: Pipe multiple files using process substitution ---
# Combine two files into one stdin stream
(echo "=== utils.py ===" && cat sdk_demo/testbed/utils.py && \
 echo "=== models.py ===" && cat sdk_demo/testbed/models.py) | \
  claude -p "Compare the code style of these two files. Which is more Pythonic?"

# --- 2F: Pipe JSON data for transformation ---
echo '[{"name":"Alice","age":30},{"name":"Bob","age":25}]' | \
  claude -p "Convert this JSON to a markdown table." --tools ""

# --- 2G: Chain: generate → pipe → refine ---
# First call generates code, second call reviews it
claude -p "Write a Python function to validate email addresses" --tools "" | \
  claude -p "Review this code for edge cases and security issues" --tools ""

# KEY INSIGHT:
# The pipe pattern lets you use Claude as a UNIX filter.
# It fits naturally into shell pipelines:
#   generate | filter | transform | output
# Each step can be Claude or a traditional tool.
