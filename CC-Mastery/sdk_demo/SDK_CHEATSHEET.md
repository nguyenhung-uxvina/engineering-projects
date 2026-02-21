# Claude Agent SDK — Cheat Sheet

## CLI Headless (`claude -p`)

```bash
# Basic one-shot
claude -p "Explain this codebase"

# Pipe content in
cat error.log | claude -p "What went wrong?"

# JSON output (get session_id, cost, result)
claude -p "List all TODOs" --output-format json | jq '.result'

# Structured output with schema validation
claude -p "Extract API endpoints" --output-format json \
  --json-schema '{"type":"object","properties":{"endpoints":{"type":"array","items":{"type":"string"}}}}'

# Stream tokens
claude -p "Write a poem" --output-format stream-json --verbose --include-partial-messages

# Continue last session
claude -c -p "Now fix those issues"

# Resume specific session
claude -r "session-id" "Continue the review"
```

## Permission & Tool Control

```bash
# Allow specific tools only
claude -p "Fix the bug" --allowedTools "Read" "Edit" "Bash(pytest *)"

# Read-only mode (analysis only)
claude -p "Review for security issues" --tools "Read,Glob,Grep"

# Full auto (sandboxed environments only!)
claude -p "Run tests and fix" --dangerously-skip-permissions

# Prefix matching: "Bash(git *)" matches git log, git diff, etc.
# The space before * matters: "Bash(git diff *)" won't match "git diff-index"
```

## Budget & Model Control

```bash
claude -p "..." --model sonnet                 # Use Sonnet (cheaper)
claude -p "..." --model opus                   # Use Opus (smartest)
claude -p "..." --max-turns 5                  # Cap iterations
claude -p "..." --max-budget-usd 0.50          # Cost ceiling
claude -p "..." --fallback-model sonnet        # Fallback if overloaded
claude -p "..." --no-session-persistence       # Ephemeral (no disk save)
```

## System Prompt

```bash
# Append to defaults (safest — keeps CLAUDE.md, tools, etc.)
claude --append-system-prompt "Always use TypeScript"

# Replace entirely (specialized agent)
claude --system-prompt "You are a security auditor. Never modify files."

# From file
claude --append-system-prompt-file ./agent-instructions.md
```

## Custom Subagents via CLI

```bash
claude --agents '{
  "reviewer": {
    "description": "Code reviewer. Use after changes.",
    "prompt": "Review code for quality and security.",
    "tools": ["Read", "Grep", "Glob"],
    "model": "sonnet"
  }
}'
```

## Python SDK

```python
# --- One-shot ---
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async for msg in query(
    prompt="Add type hints to utils.py",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Edit"],
        permission_mode="acceptEdits",
        max_turns=5,
    ),
):
    if isinstance(msg, ResultMessage):
        print(msg.result, msg.total_cost_usd)

# --- Multi-turn ---
from claude_agent_sdk import ClaudeSDKClient

async with ClaudeSDKClient(options=options) as client:
    await client.query("Read auth.py")
    async for msg in client.receive_response():
        print(msg)
    await client.query("Now find all callers")  # Remembers context!
    async for msg in client.receive_response():
        print(msg)

# --- Structured output (Pydantic) ---
from pydantic import BaseModel

class Report(BaseModel):
    summary: str
    issues: list[str]

options = ClaudeAgentOptions(
    output_format={"type": "json_schema", "schema": Report.model_json_schema()}
)
```

## TypeScript SDK

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const msg of query({
  prompt: "Fix the failing tests",
  options: {
    allowedTools: ["Read", "Edit", "Bash"],
    permissionMode: "acceptEdits",
    maxTurns: 10,
  }
})) {
  if (msg.type === "result") {
    console.log(msg.result, msg.total_cost_usd);
  }
}
```

## Parallel Patterns

```bash
# Background jobs (bash)
for f in src/*.py; do
  claude -p "Add type hints to $f" --allowedTools "Read" "Edit" \
    --permission-mode acceptEdits --no-session-persistence &
done
wait

# GNU parallel
find src -name "*.py" | parallel -j 4 \
  'claude -p "Lint {}" --allowedTools "Read" "Edit" --no-session-persistence'

# Python fan-out
semaphore = asyncio.Semaphore(4)
results = await asyncio.gather(*[bounded_process(f) for f in files])
```

## Session Chaining

```bash
# Capture session ID
sid=$(claude -p "Analyze codebase" --output-format json | jq -r '.session_id')

# Resume with context
claude -p "Focus on database layer" --resume "$sid"
claude -p "Write summary" --resume "$sid"
```

## Key Gotcha: setting_sources

The SDK loads **NO settings by default** — no CLAUDE.md, no hooks, no MCP.
To load project settings:

```python
options = ClaudeAgentOptions(
    setting_sources=["project"],  # Loads CLAUDE.md
    system_prompt={"type": "preset", "preset": "claude_code"},
)
```

```typescript
options: { settingSources: ['project'] }
```
