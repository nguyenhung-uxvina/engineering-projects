# SDK Gotchas — Things That Trip Everyone Up

## 1. `setting_sources` Defaults to Empty

The SDK loads **NOTHING** from your filesystem by default. No CLAUDE.md, no hooks, no MCP servers.

```python
# DEFAULT: Claude has NO project context
options = ClaudeAgentOptions()  # setting_sources=None → loads nothing

# FIX: Explicitly opt in
options = ClaudeAgentOptions(
    setting_sources=["project"],  # Loads CLAUDE.md from cwd
)

# Or load everything:
options = ClaudeAgentOptions(
    setting_sources=["user", "project", "local"],
)
```

**Why**: Isolation. SDK scripts should be predictable regardless of what's in the user's CLAUDE.md. If you want those rules, opt in.

## 2. Can't Run Inside Claude Code Session

```bash
$ claude -p "hello"
Error: Claude Code cannot be launched inside another Claude Code session.
```

The `CLAUDECODE` env var blocks nesting. All SDK exercises must run from a normal terminal.

## 3. `--allowedTools` Prefix Matching

```bash
# CORRECT: space before * = only "git diff ..." commands
--allowedTools "Bash(git diff *)"

# WRONG: no space = also matches "git diff-index", "git diffstat"
--allowedTools "Bash(git diff*)"

# CORRECT: allow all git commands
--allowedTools "Bash(git *)"

# WRONG: allows git AND gitk AND gitflow...
--allowedTools "Bash(git*)"
```

## 4. Package Naming Confusion

| Old (Deprecated) | New (Use This) |
|-------------------|---------------|
| `claude-code-sdk` (Python) | `claude-agent-sdk` |
| `@anthropic-ai/claude-code` (npm) | `@anthropic-ai/claude-agent-sdk` |
| `import claude_code_sdk` | `import claude_agent_sdk` |

The old names still install but are deprecated.

## 5. `query()` vs `ClaudeSDKClient` — Wrong Tool for the Job

```python
# WRONG: Using query() for multi-turn (no context carried over!)
result1 = await query("Read auth.py", options)
result2 = await query("Now find callers", options)  # Claude doesn't know about auth.py!

# RIGHT: Use ClaudeSDKClient for multi-turn
async with ClaudeSDKClient(options=options) as client:
    await client.query("Read auth.py")
    await client.receive_response()
    await client.query("Now find callers")  # Context preserved!
    await client.receive_response()
```

## 6. Headless Mode Hangs on Permission Prompts

```bash
# WRONG: No permission mode → hangs waiting for human approval
claude -p "Edit utils.py" --allowedTools "Edit"

# RIGHT: Auto-approve edits
claude -p "Edit utils.py" --allowedTools "Edit" --permission-mode acceptEdits
```

In headless mode (`-p`), there's no human to click "approve." Always set `--permission-mode` or `--allowedTools` to auto-approve the tools the agent needs.

## 7. Session Disk Buildup in Batch Mode

```bash
# WRONG: 1000 batch jobs = 1000 saved sessions
for f in *.py; do
    claude -p "Lint $f"
done

# RIGHT: Ephemeral sessions
for f in *.py; do
    claude -p "Lint $f" --no-session-persistence
done
```

## 8. `output_format` Schema Must Be Top-Level Object

```python
# WRONG: Array at top level
output_format={"type": "json_schema", "schema": {"type": "array", "items": {"type": "string"}}}

# RIGHT: Object at top level (wrap arrays in an object)
output_format={"type": "json_schema", "schema": {
    "type": "object",
    "properties": {"items": {"type": "array", "items": {"type": "string"}}},
    "required": ["items"]
}}
```

## 9. Cost Tracking — `total_cost_usd` Can Be None

```python
# WRONG: Assumes cost is always a number
total += msg.total_cost_usd  # TypeError if None!

# RIGHT: Handle None
total += msg.total_cost_usd or 0.0
```

## 10. Windows-Specific: cp1252 Encoding

If your SDK output contains Unicode (emojis, special chars), Windows may crash:

```python
# FIX: Add to top of script
import sys
sys.stdout.reconfigure(encoding="utf-8")
```

Or set env: `PYTHONIOENCODING=utf-8`
