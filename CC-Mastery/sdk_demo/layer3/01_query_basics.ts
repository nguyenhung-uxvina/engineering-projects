/**
 * Layer 3, Level 1: query() Basics in TypeScript
 * =================================================
 * Run OUTSIDE Claude Code session:
 *     cd sdk_demo/layer3 && npx tsx 01_query_basics.ts
 *
 * KEY DIFFERENCES FROM PYTHON:
 *   Python: query() → AsyncGenerator[Message]
 *   TS:     query() → Query (AsyncGenerator<SDKMessage> + control methods)
 *
 *   Python messages: AssistantMessage, ResultMessage, SystemMessage, UserMessage
 *   TS messages: SDKAssistantMessage, SDKResultMessage, SDKSystemMessage, SDKUserMessage
 *
 *   Python content: TextBlock, ToolUseBlock
 *   TS content: msg.message.content[] (Anthropic BetaMessage format)
 */

import { query } from "@anthropic-ai/claude-agent-sdk";
import type {
  SDKMessage,
  SDKSystemMessage,
  SDKAssistantMessage,
  SDKUserMessage,
  SDKResultMessage,
  SDKResultSuccess,
  SDKResultError,
  Options,
} from "@anthropic-ai/claude-agent-sdk";
import path from "path";

const TESTBED = path.resolve(import.meta.dirname!, "..", "testbed");

async function main() {
  console.log("=".repeat(60));
  console.log("  TypeScript SDK: query() Basics");
  console.log("=".repeat(60));
  console.log(`Target: ${TESTBED}\n`);

  // ---------------------------------------------------------------
  // query() returns a Query object:
  //   - Implements AsyncGenerator<SDKMessage> (for await...of)
  //   - Has control methods: interrupt(), setModel(), etc.
  //
  // Options uses camelCase (not snake_case like Python):
  //   Python: allowed_tools, max_turns, setting_sources
  //   TS:     allowedTools,  maxTurns,  settingSources
  // ---------------------------------------------------------------
  const options: Options = {
    // Tools: read-only analysis
    tools: ["Read", "Glob"],

    // Budget caps
    maxTurns: 5,
    maxBudgetUsd: 0.10,

    // Model
    model: "sonnet",

    // Working directory
    cwd: TESTBED,

    // Isolated: no CLAUDE.md, no hooks
    settingSources: [],

    // Don't save to disk (ephemeral)
    persistSession: false,  // Python: --no-session-persistence
  };

  const msgCounts = { system: 0, assistant: 0, user: 0, result: 0 };

  // ---------------------------------------------------------------
  // Iterate the message stream
  // ---------------------------------------------------------------
  const q = query({
    prompt: `Read all Python files in ${TESTBED} and list the functions in each.`,
    options,
  });

  for await (const message of q) {
    // --- Type narrowing by message.type ---

    if (message.type === "system" && "subtype" in message) {
      const sys = message as SDKSystemMessage;
      if (sys.subtype === "init") {
        msgCounts.system++;
        console.log("─".repeat(60));
        console.log(`SYSTEM (init)`);
        console.log(`  session: ${sys.session_id}`);
        console.log(`  model:   ${sys.model}`);
        console.log(`  tools:   ${sys.tools.join(", ")}`);
      }
    }

    else if (message.type === "assistant") {
      const asst = message as SDKAssistantMessage;
      msgCounts.assistant++;
      console.log("─".repeat(60));
      console.log(`ASSISTANT (model=${asst.message.model})`);

      // Content blocks are Anthropic API format (BetaMessage.content)
      for (const block of asst.message.content) {
        if (block.type === "text") {
          const preview = block.text.length > 200
            ? block.text.slice(0, 200) + "..."
            : block.text;
          console.log(`  TEXT: ${preview}`);
        }
        else if (block.type === "thinking") {
          console.log(`  THINKING: ${block.thinking.slice(0, 100)}...`);
        }
        else if (block.type === "tool_use") {
          console.log(`  TOOL_USE: ${block.name}`);
          console.log(`    id: ${block.id}`);
          console.log(`    input: ${JSON.stringify(block.input).slice(0, 120)}`);
        }
        else if (block.type === "tool_result") {
          console.log(`  TOOL_RESULT: ${JSON.stringify(block).slice(0, 100)}`);
        }
      }
    }

    else if (message.type === "user") {
      msgCounts.user++;
      // UserMessage carries tool results back to the agent
      // Usually not interesting to display
    }

    else if (message.type === "result") {
      const result = message as SDKResultMessage;
      msgCounts.result++;
      console.log("─".repeat(60));
      console.log(`RESULT`);
      console.log(`  subtype:  ${result.subtype}`);
      console.log(`  is_error: ${result.is_error}`);
      console.log(`  turns:    ${result.num_turns}`);
      console.log(`  cost:     $${result.total_cost_usd.toFixed(4)}`);
      console.log(`  duration: ${result.duration_ms}ms`);

      if (result.subtype === "success") {
        const success = result as SDKResultSuccess;
        console.log(`  result:   ${success.result.slice(0, 300)}`);
      } else {
        const error = result as SDKResultError;
        console.log(`  errors:   ${error.errors.join(", ")}`);
      }
    }
  }

  // --- Summary ---
  console.log(`\n${"=".repeat(60)}`);
  console.log(`Message counts:`, msgCounts);
  console.log(`\nKEY DIFFERENCES FROM PYTHON:`);
  console.log(`  Python: isinstance(msg, AssistantMessage)`);
  console.log(`  TS:     msg.type === "assistant"`);
  console.log(`  Python: block.text (TextBlock attribute)`);
  console.log(`  TS:     block.text (object property, after type === "text" check)`);
  console.log(`  Python: ResultMessage.result`);
  console.log(`  TS:     (msg as SDKResultSuccess).result`);
}

main().catch(console.error);
