"""Hook: Track file modifications by Write/Edit tools.

Type: PostToolUse (matcher: Write|Edit)
Purpose: Module 6 retry — explore PostToolUse event type

PostToolUse fires AFTER a tool succeeds. It cannot block.
Input: JSON on stdin with tool_name, tool_input, tool_response
Output: exit 0 always (logging only)
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

    tool_name = data.get("tool_name", "unknown")
    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "unknown")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = "d:/UxV/engineering-projects/CC-Mastery/.claude/hooks"
    log_file = os.path.join(log_dir, "file_change_log.txt")

    os.makedirs(log_dir, exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {tool_name} | {file_path}\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
