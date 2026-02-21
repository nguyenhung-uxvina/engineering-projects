# Python SDK vs TypeScript SDK — Side-by-Side

## Installation

```bash
# Python
pip install claude-agent-sdk

# TypeScript
npm install @anthropic-ai/claude-agent-sdk
```

## 1. Basic query()

```python
# PYTHON
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

async for msg in query(
    prompt="Fix the bug",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Edit"],
        permission_mode="acceptEdits",
        max_turns=5,
        setting_sources=[],
    ),
):
    if isinstance(msg, ResultMessage):
        print(msg.result, msg.total_cost_usd)
```

```typescript
// TYPESCRIPT
import { query } from "@anthropic-ai/claude-agent-sdk";
import type { SDKResultSuccess } from "@anthropic-ai/claude-agent-sdk";

for await (const msg of query({
  prompt: "Fix the bug",
  options: {
    allowedTools: ["Read", "Edit"],
    permissionMode: "acceptEdits",
    maxTurns: 5,
    settingSources: [],
  },
})) {
  if (msg.type === "result" && msg.subtype === "success") {
    const r = msg as SDKResultSuccess;
    console.log(r.result, r.total_cost_usd);
  }
}
```

## 2. Message Type Checking

```python
# PYTHON — isinstance() dispatch
if isinstance(msg, SystemMessage):     ...
if isinstance(msg, AssistantMessage):  ...
if isinstance(msg, UserMessage):       ...
if isinstance(msg, ResultMessage):     ...

# Content blocks — isinstance() again
for block in msg.content:
    if isinstance(block, TextBlock):      print(block.text)
    if isinstance(block, ToolUseBlock):   print(block.name, block.input)
```

```typescript
// TYPESCRIPT — discriminated union on msg.type
if (msg.type === "system")    { /* SDKSystemMessage */ }
if (msg.type === "assistant") { /* SDKAssistantMessage */ }
if (msg.type === "user")      { /* SDKUserMessage */ }
if (msg.type === "result")    { /* SDKResultMessage */ }

// Content blocks — Anthropic API BetaMessage format
for (const block of (msg as SDKAssistantMessage).message.content) {
  if (block.type === "text")     { console.log(block.text); }
  if (block.type === "tool_use") { console.log(block.name, block.input); }
}
```

## 3. Naming Convention

| Concept | Python (snake_case) | TypeScript (camelCase) |
|---------|--------------------|-----------------------|
| Options | `ClaudeAgentOptions` | `Options` |
| Allowed tools | `allowed_tools` | `allowedTools` |
| Max turns | `max_turns` | `maxTurns` |
| Setting sources | `setting_sources` | `settingSources` |
| Session persist | N/A (CLI flag) | `persistSession` |
| Max budget | `max_budget_usd` | `maxBudgetUsd` |
| Permission mode | `permission_mode` | `permissionMode` |
| System prompt | `system_prompt` | `systemPrompt` |
| Output format | `output_format` | `outputFormat` |
| MCP servers | `mcp_servers` | `mcpServers` |

## 4. Multi-Turn

```python
# PYTHON — ClaudeSDKClient context manager
async with ClaudeSDKClient(options=options) as client:
    await client.query("Read auth.py")
    async for msg in client.receive_response():
        ...
    await client.query("Now find callers")  # Remembers!
    async for msg in client.receive_response():
        ...
```

```typescript
// TYPESCRIPT — streaming input (AsyncIterable)
// OR use unstable v2 API:
import { unstable_v2_createSession } from "@anthropic-ai/claude-agent-sdk";

const session = unstable_v2_createSession({ model: "sonnet" });
await session.send({ type: "user", message: { role: "user", content: "Read auth.py" }, ... });
for await (const msg of session.stream()) { ... }
await session.send({ type: "user", message: { role: "user", content: "Find callers" }, ... });
for await (const msg of session.stream()) { ... }
session.close();
```

## 5. Custom Tools

```python
# PYTHON — dict schema
@tool("convert", "Convert units", {"value": float, "unit": str})
async def convert(args: dict) -> dict:
    return {"content": [{"type": "text", "text": f"{args['value']} converted"}]}

server = create_sdk_mcp_server("eng", tools=[convert])
```

```typescript
// TYPESCRIPT — Zod schema (type-safe!)
const convert = tool("convert", "Convert units", {
  value: z.number(),
  unit: z.string(),
}, async (args) => {  // args is typed as { value: number, unit: string }
  return { content: [{ type: "text", text: `${args.value} converted` }] };
});

const server = createSdkMcpServer({ name: "eng", tools: [convert] });
```

## 6. Hooks

```python
# PYTHON — typed hook input
async def my_hook(
    input_data: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext,
) -> SyncHookJSONOutput:
    return {}

options = ClaudeAgentOptions(
    hooks={"PreToolUse": [HookMatcher(hooks=[my_hook])]}
)
```

```typescript
// TYPESCRIPT — callback with signal
const myHook: HookCallback = async (input, toolUseId, { signal }) => {
  return {};
};

const options: Options = {
  hooks: { PreToolUse: [{ hooks: [myHook] }] }
};
```

## 7. Cancellation

```python
# PYTHON — client.interrupt()
async with ClaudeSDKClient(options=options) as client:
    await client.query("Long task...")
    await asyncio.sleep(5)
    await client.interrupt()
```

```typescript
// TYPESCRIPT — AbortController (native JS pattern)
const controller = new AbortController();
setTimeout(() => controller.abort(), 5000);

const q = query({
  prompt: "Long task...",
  options: { abortController: controller }
});
try {
  for await (const msg of q) { ... }
} catch (err) {
  if (err instanceof AbortError) { /* clean cancellation */ }
}
```

## 8. Structured Output

```python
# PYTHON — Pydantic
from pydantic import BaseModel
class Report(BaseModel):
    summary: str
    issues: list[str]

options = ClaudeAgentOptions(
    output_format={"type": "json_schema", "schema": Report.model_json_schema()}
)
```

```typescript
// TYPESCRIPT — Zod (or raw JSON schema)
import { z } from "zod";
const Report = z.object({
  summary: z.string(),
  issues: z.array(z.string()),
});

const options: Options = {
  outputFormat: { type: "json_schema", schema: z.toJSONSchema(Report) }
};
```

## Decision: When to Use Which

| Factor | Use Python | Use TypeScript |
|--------|-----------|---------------|
| **Your stack** | Python/data/ML apps | Node.js/web services |
| **Multi-turn** | `ClaudeSDKClient` (stable) | `unstable_v2_createSession` (alpha) |
| **Type safety** | Runtime only (Pydantic) | Compile-time (Zod + TS) |
| **Tool schemas** | Dict or Pydantic | Zod (auto-inferred types) |
| **Cancel** | `client.interrupt()` | `AbortController` (standard) |
| **Control methods** | On ClaudeSDKClient | On Query object directly |
| **Ecosystem** | Huge (data, science, ML) | Huge (web, serverless, edge) |
| **SDK maturity** | Stable | Stable (v2 API is alpha) |

**Bottom line**: Same capabilities, different ergonomics. Pick the one that matches your stack.
