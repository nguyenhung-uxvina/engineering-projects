/**
 * Layer 3, Level 2: AbortController + Query Control Methods
 * ===========================================================
 * Run OUTSIDE Claude Code session:
 *     cd sdk_demo/layer3 && npx tsx 02_abort_and_control.ts
 *
 * KEY CONCEPT:
 *   The Query object returned by query() has CONTROL METHODS.
 *   These are TS-exclusive — Python SDK wraps them differently.
 *
 *   Query extends AsyncGenerator<SDKMessage> AND has:
 *     q.interrupt()          — Stop mid-execution
 *     q.setModel("opus")     — Switch model
 *     q.setPermissionMode()  — Change permissions
 *     q.rewindFiles(uuid)    — Restore files to checkpoint
 *     q.supportedCommands()  — List slash commands
 *     q.supportedModels()    — List available models
 *     q.mcpServerStatus()    — Check MCP servers
 *     q.accountInfo()        — Get account info
 *     q.close()              — Force-terminate
 *
 *   Plus native AbortController for timeout-based cancellation.
 */

import { query, AbortError } from "@anthropic-ai/claude-agent-sdk";
import type {
  SDKAssistantMessage,
  SDKResultMessage,
  SDKSystemMessage,
  Query,
} from "@anthropic-ai/claude-agent-sdk";
import path from "path";

const TESTBED = path.resolve(import.meta.dirname!, "..", "testbed");

// =============================================================================
// Demo A: AbortController — timeout-based cancellation
// =============================================================================

async function demoAbort() {
  console.log("=".repeat(60));
  console.log("  Demo A: AbortController (Timeout)");
  console.log("=".repeat(60));

  const controller = new AbortController();

  // Cancel after 15 seconds
  const timeout = setTimeout(() => {
    console.log("\n  >>> ABORT: Timeout reached <<<\n");
    controller.abort();
  }, 15_000);

  try {
    const q = query({
      prompt: "Do a comprehensive analysis of all files in this directory. "
        + "Read each one, analyze style, complexity, and patterns.",
      options: {
        tools: ["Read", "Glob", "Grep"],
        maxTurns: 20,
        model: "sonnet",
        cwd: TESTBED,
        settingSources: [],
        persistSession: false,
        abortController: controller,  // <-- Pass the controller
      },
    });

    let toolCalls = 0;
    for await (const msg of q) {
      if (msg.type === "assistant") {
        const asst = msg as SDKAssistantMessage;
        for (const block of asst.message.content) {
          if (block.type === "tool_use") {
            toolCalls++;
            console.log(`  [${toolCalls}] ${block.name}(${JSON.stringify(block.input).slice(0, 50)}...)`);
          }
        }
      } else if (msg.type === "result") {
        const result = msg as SDKResultMessage;
        console.log(`\n  Result: ${result.subtype}, cost: $${result.total_cost_usd.toFixed(4)}`);
      }
    }
  } catch (err) {
    if (err instanceof AbortError) {
      console.log("  Caught AbortError — agent was cleanly terminated.");
    } else {
      throw err;
    }
  } finally {
    clearTimeout(timeout);
  }
}

// =============================================================================
// Demo B: Query control methods — introspection
// =============================================================================

async function demoControlMethods() {
  console.log("\n" + "=".repeat(60));
  console.log("  Demo B: Query Control Methods");
  console.log("=".repeat(60));

  const q = query({
    prompt: "Read utils.py and suggest improvements.",
    options: {
      tools: ["Read"],
      maxTurns: 3,
      model: "sonnet",
      cwd: TESTBED,
      settingSources: [],
      persistSession: false,
    },
  });

  // --- Introspect the session WHILE it runs ---
  let initialized = false;

  for await (const msg of q) {
    // After init, query the session for info
    if (msg.type === "system" && !initialized) {
      initialized = true;

      // These methods talk to the running CLI subprocess
      try {
        const models = await q.supportedModels();
        console.log(`\n  Available models (${models.length}):`);
        for (const m of models.slice(0, 5)) {
          console.log(`    ${m.value}: ${m.displayName}`);
        }

        const commands = await q.supportedCommands();
        console.log(`\n  Slash commands (${commands.length}):`);
        for (const c of commands.slice(0, 5)) {
          console.log(`    /${c.name}: ${c.description.slice(0, 50)}`);
        }

        const account = await q.accountInfo();
        console.log(`\n  Account: ${account.email || "?"} (${account.subscriptionType || "?"})`);

        const mcp = await q.mcpServerStatus();
        console.log(`\n  MCP servers: ${mcp.length}`);
        for (const s of mcp) {
          console.log(`    ${s.name}: ${s.status}`);
        }
      } catch (err) {
        console.log(`  (some control methods failed — expected in some environments)`);
      }
    }

    else if (msg.type === "result") {
      const result = msg as SDKResultMessage;
      console.log(`\n  Result: ${result.subtype}, $${result.total_cost_usd.toFixed(4)}`);
    }
  }
}

// =============================================================================
// Demo C: Model switching mid-session
// =============================================================================

async function demoModelSwitch() {
  console.log("\n" + "=".repeat(60));
  console.log("  Demo C: Model Switching Mid-Session");
  console.log("=".repeat(60));

  // Use streaming input mode for multi-turn
  const userMessages = async function* () {
    // Turn 1: Quick scan with Sonnet
    yield {
      type: "user" as const,
      message: { role: "user" as const, content: `Read ${TESTBED}/utils.py briefly.` },
      parent_tool_use_id: null,
      session_id: "",
    };
  };

  const q = query({
    prompt: userMessages(),
    options: {
      tools: ["Read"],
      maxTurns: 3,
      model: "sonnet",
      cwd: TESTBED,
      settingSources: [],
      persistSession: false,
    },
  });

  let turnCount = 0;
  for await (const msg of q) {
    if (msg.type === "assistant") {
      turnCount++;
      const asst = msg as SDKAssistantMessage;
      for (const block of asst.message.content) {
        if (block.type === "text") {
          console.log(`  [turn ${turnCount}, model=${asst.message.model}] ${block.text.slice(0, 150)}...`);
        }
      }

      // After first turn, switch to Opus for deeper analysis
      if (turnCount === 1) {
        console.log("\n  >>> Switching model to Opus <<<\n");
        await q.setModel("opus");
      }
    }
    else if (msg.type === "result") {
      const result = msg as SDKResultMessage;
      console.log(`\n  Final: ${result.subtype}, $${result.total_cost_usd.toFixed(4)}`);
    }
  }
}

// =============================================================================
// Main
// =============================================================================

async function main() {
  await demoAbort();
  await demoControlMethods();
  // demoModelSwitch() uses streaming input which may need special setup
  // Uncomment when ready to test:
  // await demoModelSwitch();

  console.log(`
${"=".repeat(60)}
  TS-EXCLUSIVE FEATURES (not in Python SDK)
${"=".repeat(60)}
  1. AbortController — native JS pattern for cancellation
  2. Query.supportedModels() — list models during execution
  3. Query.supportedCommands() — list slash commands
  4. Query.accountInfo() — check auth status
  5. Query.mcpServerStatus() — inspect MCP connections
  6. Query.setMcpServers() — dynamically add/remove MCP servers
  7. Query.rewindFiles(uuid) — restore files to checkpoint
  8. Query.close() — force-terminate the subprocess

  Python equivalent: ClaudeSDKClient has similar methods but
  as separate awaitable methods, not on the generator itself.
`);
}

main().catch(console.error);
