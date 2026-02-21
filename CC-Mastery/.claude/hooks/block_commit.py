"""Hook: Block git commit unless tests pass.

Type: PreToolUse (matcher: Bash)
Purpose: Exercise 2 — Module 6 (Hooks)

Pattern: "Block-at-Submit"
- Intercepts any Bash command containing "git commit"
- Runs pytest in the hooks_demo directory
- If tests fail: exit 2 (block) with stderr feedback
- If tests pass: exit 0 (allow)

This forces Claude into a test-fix loop until all tests are green.
"""

import json
import subprocess
import sys
import os


def main():
    # Parse hook input
    try:
        raw = sys.stdin.read()
        data = json.loads(raw)
        command = data.get("tool_input", {}).get("command", "")
    except Exception:
        sys.exit(0)  # Can't parse — don't block

    # Only intercept git commit commands
    if "git commit" not in command:
        sys.exit(0)

    # Run tests
    project_dir = os.environ.get(
        "CLAUDE_PROJECT_DIR",
        "d:/UxV/engineering-projects/CC-Mastery",
    )
    test_dir = os.path.join(project_dir, "hooks_demo")

    result = subprocess.run(
        ["python", "-m", "pytest", "test_calculator.py", "-v"],
        cwd=test_dir,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        # BLOCK the commit — exit 2 sends stderr to Claude as feedback
        print(
            f"COMMIT BLOCKED: Tests failed. Fix the failing tests before committing.\n\n"
            f"Test output:\n{result.stdout}\n{result.stderr}",
            file=sys.stderr,
        )
        sys.exit(2)

    # Tests passed — allow the commit
    sys.exit(0)


if __name__ == "__main__":
    main()
