# Hooks Directory — Module 6

Hook scripts for CC-Mastery Module 6 exercises.

| Hook | Event | Purpose |
|------|-------|---------|
| `log_bash.py` | PreToolUse (Bash) | Logs all Bash commands with timestamps |
| `block_commit.py` | PreToolUse (Bash) | Blocks git commit unless pytest passes |
| `track_file_changes.py` | PostToolUse (Write/Edit) | Tracks which files are modified |
| `prompt_hints.py` | UserPromptSubmit | Injects context hints for keywords |
| `stop_logger.py` | Stop | Logs each time Claude finishes a response |
