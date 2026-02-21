"""
Step 2: Python SDK query() — One-Shot Demo
============================================
Run OUTSIDE Claude Code session:
  python sdk_demo/step2_query_demo.py

Demonstrates:
  - query() async generator
  - ClaudeAgentOptions with real field names
  - Message type handling (SystemMessage, AssistantMessage, ResultMessage)
  - Tool use visibility (see what the agent does)
  - Cost tracking
"""

import asyncio
import sys
from pathlib import Path

from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolUseBlock,
    ToolResultBlock,
)

# Target: add type hints to this file
TARGET = Path(__file__).parent / "testbed" / "utils.py"


async def main():
    print(f"=== SDK query() Demo ===")
    print(f"Target: {TARGET}")
    print(f"Exists: {TARGET.exists()}")
    print()

    # ---------------------------------------------------------------
    # query() returns an AsyncGenerator[Message]
    # Each message is one of: SystemMessage, AssistantMessage,
    #   UserMessage, ResultMessage
    # ---------------------------------------------------------------
    options = ClaudeAgentOptions(
        # TOOLS: only allow Read + Edit (least privilege)
        allowed_tools=["Read", "Edit"],

        # PERMISSIONS: auto-approve edits (headless, no human)
        permission_mode="acceptEdits",

        # BUDGET: cap iterations and cost
        max_turns=5,
        max_budget_usd=0.25,

        # MODEL: use Sonnet for cost efficiency on simple tasks
        model="sonnet",

        # WORKING DIRECTORY: where file paths resolve
        cwd=str(TARGET.parent),

        # SETTINGS: don't load CLAUDE.md or hooks (isolated task)
        setting_sources=[],
    )

    turn_count = 0

    async for message in query(
        prompt=(
            f"Add Python type hints to all functions in {TARGET.name}. "
            "Use standard library types. Don't change logic. "
            "For file I/O return types, use list[list[str]]."
        ),
        options=options,
    ):
        # --- System init message (session start) ---
        if isinstance(message, SystemMessage):
            print(f"[SYSTEM] Session: {message.session_id}")
            print(f"  Model: {getattr(message, 'model', '?')}")
            print(f"  Tools: {getattr(message, 'tools', '?')}")
            print()

        # --- Assistant turn (thinking + tool calls) ---
        elif isinstance(message, AssistantMessage):
            turn_count += 1
            print(f"[TURN {turn_count}]")
            for block in message.content:
                if isinstance(block, TextBlock):
                    # Agent's reasoning / response text
                    text = block.text[:200] + "..." if len(block.text) > 200 else block.text
                    print(f"  Text: {text}")
                elif isinstance(block, ToolUseBlock):
                    # Agent calling a tool
                    print(f"  Tool: {block.name}({_summarize_input(block.input)})")
                elif isinstance(block, ToolResultBlock):
                    # Tool result (usually in next message)
                    print(f"  Result: {str(block)[:100]}")
            print()

        # --- Final result ---
        elif isinstance(message, ResultMessage):
            print(f"[RESULT]")
            print(f"  Status: {message.subtype}")
            print(f"  Cost: ${message.total_cost_usd:.4f}")
            if message.result:
                print(f"  Summary: {message.result[:300]}")
            print()

    # --- Verify the file was modified ---
    print("=== Modified File ===")
    print(TARGET.read_text(encoding="utf-8"))


def _summarize_input(tool_input: dict) -> str:
    """Summarize tool input for display."""
    if "file_path" in tool_input:
        return f"file_path={tool_input['file_path']}"
    if "command" in tool_input:
        return f"command={tool_input['command'][:60]}"
    if "old_string" in tool_input:
        return f"old='{tool_input['old_string'][:40]}...' new='{tool_input['new_string'][:40]}...'"
    return str(tool_input)[:80]


if __name__ == "__main__":
    asyncio.run(main())
