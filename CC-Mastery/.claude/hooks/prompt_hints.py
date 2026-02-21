"""Hook: Inject context hints when user mentions project IDs or keywords.

Type: UserPromptSubmit (no matcher — fires on every prompt)
Purpose: Module 6 retry — explore UserPromptSubmit event type

UserPromptSubmit fires BEFORE Claude processes the user's message.
- Can BLOCK (exit 2) or ALLOW (exit 0)
- Can INJECT CONTEXT via stdout (plain text or JSON additionalContext)
- Input: JSON on stdin with "prompt" field containing user's message

This hook demonstrates the "hint" pattern:
- Detects keywords in the user's prompt
- Injects relevant context without blocking
"""

import json
import re
import sys


# Keyword → context hint mapping
HINTS = {
    r"VN-\d{3}-\d{3}": (
        "HINT: Project ID detected. Use /o <project-id> to open the project, "
        "or check vault/projects/ for existing project folders."
    ),
    r"(?i)\bhook": (
        "HINT: Hooks topic detected. Hook config is in .claude/settings.json. "
        "Existing hooks: log_bash.py, block_commit.py, track_file_changes.py, prompt_hints.py."
    ),
    r"(?i)\btest": (
        "HINT: Testing topic detected. Demo tests are in hooks_demo/test_calculator.py. "
        "Run with: python -m pytest hooks_demo/ -v"
    ),
}


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
        prompt = data.get("prompt", "")
    except Exception:
        sys.exit(0)

    # Collect all matching hints
    matched_hints = []
    for pattern, hint in HINTS.items():
        if re.search(pattern, prompt):
            matched_hints.append(hint)

    if matched_hints:
        # Output plain text — Claude sees this as additional context
        print("\n".join(matched_hints))

    sys.exit(0)  # Always allow


if __name__ == "__main__":
    main()
