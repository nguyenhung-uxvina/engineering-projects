"""
Layer 2, Level 1: query() Basics + Message Flow
=================================================
Run OUTSIDE Claude Code session:
    python sdk_demo/layer2/01_query_basics.py

KEY CONCEPT:
    query() returns an AsyncGenerator that yields typed messages.
    You iterate over them to see EVERYTHING the agent does.

MESSAGE FLOW:
    SystemMessage (init)  →  session_id, tools, model
    AssistantMessage      →  agent thinking + tool calls
    UserMessage           →  tool results fed back to agent
    AssistantMessage      →  agent processes results, may call more tools
    UserMessage           →  more tool results...
    AssistantMessage      →  final text response
    ResultMessage         →  status, cost, structured_output
"""

import asyncio
import sys

sys.stdout.reconfigure(encoding="utf-8")  # Windows fix

from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    # --- 4 message types ---
    SystemMessage,    # Init: session_id, tools
    AssistantMessage, # Agent output: text, tool calls
    UserMessage,      # Tool results (auto-generated)
    ResultMessage,    # Final: status, cost, result
    # --- Content block types ---
    TextBlock,        # Agent's text output
    ThinkingBlock,    # Extended thinking (if enabled)
    ToolUseBlock,     # Agent calling a tool: name + input
    ToolResultBlock,  # Tool's response
)
from pathlib import Path

TESTBED = Path(__file__).resolve().parent.parent / "testbed"


async def main():
    print("=" * 60)
    print("  query() Message Flow Demo")
    print("=" * 60)
    print()

    msg_count = {"system": 0, "assistant": 0, "user": 0, "result": 0}

    # ---------------------------------------------------------------
    # query() signature:
    #   query(prompt: str, options: ClaudeAgentOptions) -> AsyncGenerator[Message]
    #
    # The generator yields messages as the agent works.
    # You MUST iterate it — otherwise the agent never runs.
    # ---------------------------------------------------------------
    async for message in query(
        prompt=f"Read {TESTBED / 'utils.py'} and list all function names.",
        options=ClaudeAgentOptions(
            # Minimum tools: read-only
            tools=["Read"],
            # Budget cap
            max_turns=3,
            max_budget_usd=0.10,
            # Model
            model="sonnet",
            # Isolated: no CLAUDE.md, no hooks
            setting_sources=[],
        ),
    ):
        # --- Dispatch on message type ---

        if isinstance(message, SystemMessage):
            msg_count["system"] += 1
            print(f"{'─'*60}")
            print(f"SYSTEM (subtype={message.subtype})")
            # data contains session_id, tools, model, cwd
            sid = message.data.get("session_id", "?")
            print(f"  session_id: {sid}")
            print(f"  data keys: {list(message.data.keys())}")

        elif isinstance(message, AssistantMessage):
            msg_count["assistant"] += 1
            print(f"{'─'*60}")
            print(f"ASSISTANT (model={message.model})")

            for block in message.content:
                if isinstance(block, TextBlock):
                    # The agent's text — reasoning or final answer
                    preview = block.text[:200]
                    if len(block.text) > 200:
                        preview += "..."
                    print(f"  TEXT: {preview}")

                elif isinstance(block, ThinkingBlock):
                    # Extended thinking (only with thinking enabled)
                    print(f"  THINKING: {block.thinking[:100]}...")

                elif isinstance(block, ToolUseBlock):
                    # Agent is calling a tool
                    print(f"  TOOL_USE: {block.name}")
                    print(f"    id: {block.id}")
                    print(f"    input: {_fmt(block.input)}")

                elif isinstance(block, ToolResultBlock):
                    # Tool result embedded in assistant message
                    content = str(block.content)[:100] if block.content else "(empty)"
                    print(f"  TOOL_RESULT: {content}")

        elif isinstance(message, UserMessage):
            msg_count["user"] += 1
            print(f"{'─'*60}")
            print(f"USER (auto-generated tool result)")
            # UserMessage carries tool results back to the agent.
            # You don't create these — the SDK does automatically.
            if message.tool_use_result:
                content = str(message.tool_use_result)[:150]
                print(f"  tool_result: {content}...")
            elif isinstance(message.content, list):
                for block in message.content:
                    if isinstance(block, ToolResultBlock):
                        snippet = str(block.content)[:150] if block.content else ""
                        print(f"  tool_result [{block.tool_use_id[:8]}]: {snippet}...")

        elif isinstance(message, ResultMessage):
            msg_count["result"] += 1
            print(f"{'─'*60}")
            print(f"RESULT")
            print(f"  subtype:   {message.subtype}")
            print(f"  is_error:  {message.is_error}")
            print(f"  turns:     {message.num_turns}")
            print(f"  cost:      ${message.total_cost_usd or 0:.4f}")
            print(f"  duration:  {message.duration_ms}ms")
            print(f"  session:   {message.session_id}")
            if message.result:
                print(f"  result:    {message.result[:300]}")

    # --- Summary ---
    print(f"\n{'='*60}")
    print(f"Message counts: {msg_count}")
    print(f"  Typical flow: 1 system + N*(assistant+user) + 1 result")


def _fmt(d: dict, max_len: int = 120) -> str:
    """Format dict for display, truncating long values."""
    parts = []
    for k, v in d.items():
        vs = str(v)
        if len(vs) > 60:
            vs = vs[:57] + "..."
        parts.append(f"{k}={vs}")
    out = ", ".join(parts)
    return out[:max_len]


if __name__ == "__main__":
    asyncio.run(main())
