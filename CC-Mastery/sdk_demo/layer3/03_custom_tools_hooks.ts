/**
 * Layer 3, Level 3: Custom MCP Tools + Hooks in TypeScript
 * ==========================================================
 * Run OUTSIDE Claude Code session:
 *     cd sdk_demo/layer3 && npx tsx 03_custom_tools_hooks.ts
 *
 * KEY CONCEPT:
 *   TS uses Zod schemas for tool inputs (Python uses dict/Pydantic).
 *   The tool() function + createSdkMcpServer() work the same way,
 *   but with TypeScript's type inference.
 *
 *   Hooks are also inline functions, but match the TS callback signature.
 */

import {
  query,
  tool,
  createSdkMcpServer,
} from "@anthropic-ai/claude-agent-sdk";
import type {
  SDKAssistantMessage,
  SDKResultMessage,
  SDKResultSuccess,
  HookCallback,
  HookCallbackMatcher,
  PreToolUseHookInput,
  PostToolUseHookInput,
  SyncHookJSONOutput,
  Options,
} from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

// =============================================================================
// Custom Tool 1: Unit Converter (Zod schema)
// =============================================================================

const convertUnits = tool(
  "convert_units",
  "Convert between engineering units (length, weight, pressure, temperature)",
  // Zod schema — TS infers the types automatically!
  {
    value: z.number().describe("Numeric value to convert"),
    fromUnit: z.string().describe("Source unit (mm, cm, m, km, in, ft, psi, bar, c, f, k)"),
    toUnit: z.string().describe("Target unit"),
  },
  async (args) => {
    const { value, fromUnit, toUnit } = args;
    const from = fromUnit.toLowerCase();
    const to = toUnit.toLowerCase();

    // Simple conversion table to SI
    const TO_SI: Record<string, number> = {
      mm: 0.001, cm: 0.01, m: 1.0, km: 1000.0,
      "in": 0.0254, ft: 0.3048, yd: 0.9144,
      g: 0.001, kg: 1.0, lb: 0.453592,
      pa: 1.0, kpa: 1000.0, mpa: 1e6, psi: 6894.76, bar: 1e5, atm: 101325.0,
    };

    let result: number;

    // Temperature is special
    if (["c", "f", "k"].includes(from) && ["c", "f", "k"].includes(to)) {
      let celsius = from === "f" ? (value - 32) * 5 / 9
                  : from === "k" ? value - 273.15
                  : value;
      result = to === "f" ? celsius * 9 / 5 + 32
             : to === "k" ? celsius + 273.15
             : celsius;
    } else if (from in TO_SI && to in TO_SI) {
      result = (value * TO_SI[from]!) / TO_SI[to]!;
    } else {
      return { content: [{ type: "text" as const, text: `Unknown units: ${from} → ${to}` }] };
    }

    return {
      content: [{ type: "text" as const, text: `${value} ${from} = ${result.toFixed(4)} ${to}` }],
    };
  }
);

// =============================================================================
// Custom Tool 2: Stateful Notebook (demonstrates state across calls)
// =============================================================================

const entries: Array<{ id: number; category: string; content: string }> = [];

const notebookAdd = tool(
  "notebook_add",
  "Add a note to the engineering notebook",
  {
    category: z.enum(["calculation", "decision", "note"]),
    content: z.string(),
  },
  async (args) => {
    entries.push({ id: entries.length + 1, category: args.category, content: args.content });
    return { content: [{ type: "text" as const, text: `Entry #${entries.length} recorded.` }] };
  }
);

const notebookRead = tool(
  "notebook_read",
  "Read all notebook entries",
  {
    category: z.enum(["all", "calculation", "decision", "note"]),
  },
  async (args) => {
    const filtered = args.category === "all" ? entries
      : entries.filter(e => e.category === args.category);
    if (filtered.length === 0) {
      return { content: [{ type: "text" as const, text: "Notebook is empty." }] };
    }
    const text = filtered.map(e => `#${e.id} [${e.category}] ${e.content}`).join("\n");
    return { content: [{ type: "text" as const, text }] };
  }
);

// =============================================================================
// Bundle into MCP server
// =============================================================================

const engServer = createSdkMcpServer({
  name: "engineering",
  version: "1.0.0",
  tools: [convertUnits, notebookAdd, notebookRead],
});

// =============================================================================
// Hooks: Audit + Safety Guard
// =============================================================================

const auditLog: string[] = [];

const auditHook: HookCallback = async (input, toolUseId, { signal }) => {
  if (input.hook_event_name === "PreToolUse") {
    const pre = input as PreToolUseHookInput;
    const entry = `${pre.tool_name}: ${JSON.stringify(pre.tool_input).slice(0, 60)}`;
    auditLog.push(entry);
    console.log(`  HOOK(audit): ${entry}`);
  }
  return {};
};

const safetyHook: HookCallback = async (input, toolUseId, { signal }) => {
  if (input.hook_event_name === "PreToolUse") {
    const pre = input as PreToolUseHookInput;
    if (pre.tool_name === "Bash") {
      const cmd = (pre.tool_input as any)?.command || "";
      if (cmd.includes("rm -rf") || cmd.includes("format")) {
        console.log(`  HOOK(safety): BLOCKED — dangerous command`);
        return {
          decision: "block" as const,
          reason: "Dangerous command blocked by safety hook",
        };
      }
    }
  }
  return {};
};

// =============================================================================
// Run the agent
// =============================================================================

async function main() {
  console.log("=".repeat(60));
  console.log("  TypeScript: Custom Tools + Hooks");
  console.log("=".repeat(60));
  console.log();

  const options: Options = {
    mcpServers: { engineering: engServer },
    allowedTools: [
      "mcp__engineering__convert_units",
      "mcp__engineering__notebook_add",
      "mcp__engineering__notebook_read",
      "Read",
    ],
    maxTurns: 15,
    maxBudgetUsd: 0.20,
    model: "sonnet",
    settingSources: [],
    persistSession: false,
    hooks: {
      PreToolUse: [
        { hooks: [auditHook, safetyHook] },  // matcher omitted = all tools
      ],
    },
  };

  const q = query({
    prompt:
      "You have engineering tools. Do the following:\n" +
      "1. Convert 200 PSI to MPa\n" +
      "2. Convert 30°C to Fahrenheit\n" +
      "3. Convert 1000mm to feet\n" +
      "4. Record each result in the notebook as a 'calculation'\n" +
      "5. Add a 'decision': 'System pressure rated at 1.5 MPa — margins OK'\n" +
      "6. Read back all notebook entries",
    options,
  });

  for await (const msg of q) {
    if (msg.type === "assistant") {
      const asst = msg as SDKAssistantMessage;
      for (const block of asst.message.content) {
        if (block.type === "text") {
          console.log(`\n  ${block.text.slice(0, 400)}`);
        } else if (block.type === "tool_use") {
          // Hooks already print tool calls
        }
      }
    } else if (msg.type === "result") {
      const result = msg as SDKResultMessage;
      console.log(`\n  [done: $${result.total_cost_usd.toFixed(4)}, turns: ${result.num_turns}]`);
    }
  }

  // Report
  console.log(`\n${"=".repeat(60)}`);
  console.log("  IN-MEMORY STATE");
  console.log("=".repeat(60));
  for (const e of entries) {
    console.log(`  #${e.id} [${e.category}] ${e.content}`);
  }

  console.log(`\n  Audit log (${auditLog.length} entries):`);
  for (const entry of auditLog) {
    console.log(`    ${entry}`);
  }

  console.log(`
${"=".repeat(60)}
  PYTHON vs TYPESCRIPT TOOL DEFINITION
${"=".repeat(60)}
  Python:                              TypeScript:
  ─────────                            ──────────
  @tool("name", "desc", {              tool("name", "desc", {
    "value": float,                      value: z.number(),
    "unit": str                          unit: z.string()
  })                                   }, async (args) => {
  async def handler(args):               // args is typed!
    ...                                   ...
                                       });

  Python: dict schema → runtime only   TS: Zod schema → compile-time types
  Python: create_sdk_mcp_server()      TS: createSdkMcpServer()
  Python: HookMatcher(matcher, hooks)  TS: { matcher, hooks } object literal
`);
}

main().catch(console.error);
