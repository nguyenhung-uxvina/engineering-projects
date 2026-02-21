"""Hook: Log each time Claude finishes a response.

Type: Stop (no matcher)
Purpose: Module 6 retry — explore Stop event type

Stop fires when Claude finishes responding.
- Can BLOCK (force Claude to continue) or ALLOW (let it stop)
- Input: JSON with stop_hook_active (bool) to prevent infinite loops
- We just log — never block

Key detail: stop_hook_active=true means Claude is already continuing
from a previous Stop hook. Check this to avoid infinite loops!
"""

import json
import os
import sys
from datetime import datetime


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
    except Exception:
        sys.exit(0)

    # CRITICAL: check stop_hook_active to avoid infinite loops
    if data.get("stop_hook_active", False):
        sys.exit(0)  # Already in a stop-hook continuation, don't interfere

    session_id = data.get("session_id", "unknown")[:8]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = "d:/UxV/engineering-projects/CC-Mastery/.claude/hooks"
    log_file = os.path.join(log_dir, "session_activity_log.txt")

    os.makedirs(log_dir, exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | session:{session_id} | response completed\n")

    sys.exit(0)  # Allow stop


if __name__ == "__main__":
    main()
