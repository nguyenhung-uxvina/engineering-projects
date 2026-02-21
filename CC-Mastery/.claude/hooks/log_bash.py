"""Hook: Log all Bash commands Claude executes.

Type: PreToolUse (matcher: Bash)
Purpose: Exercise 1 — Module 6 (Hooks)

Input: JSON on stdin with tool_input.command
Output: exit 0 (allow) — logging only, never blocks
"""

import json
import sys
import os
from datetime import datetime

def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
        command = data.get("tool_input", {}).get("command", "unknown")
    except Exception:
        command = "<parse-error>"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    log_file = os.path.join(project_dir, ".claude", "hooks", "bash_command_log.txt")

    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {command}\n")

    sys.exit(0)

if __name__ == "__main__":
    main()
