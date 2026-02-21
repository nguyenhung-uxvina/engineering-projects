"""
Step 3: ClaudeSDKClient — Multi-Turn Demo
============================================
Run OUTSIDE Claude Code session:
  python sdk_demo/step3_multiturn_demo.py

Demonstrates:
  - ClaudeSDKClient context manager (async with)
  - Multi-turn: agent remembers previous exchanges
  - Interrupt support
  - Session persistence across turns
"""

import asyncio
import sys
from pathlib import Path

from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolUseBlock,
)

TESTBED = Path(__file__).parent / "testbed"


async def print_response(client: ClaudeSDKClient, label: str):
    """Helper: print all messages from a response."""
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")

    async for msg in client.receive_response():
        if isinstance(msg, SystemMessage):
            print(f"  [session: {msg.session_id}]")
        elif isinstance(msg, AssistantMessage):
            for block in msg.content:
                if isinstance(block, TextBlock):
                    print(f"  {block.text[:300]}")
                elif isinstance(block, ToolUseBlock):
                    print(f"  [tool: {block.name}]")
        elif isinstance(msg, ResultMessage):
            print(f"  [cost: ${msg.total_cost_usd:.4f}]")


async def main():
    print("=== Multi-Turn Demo ===")
    print(f"Working in: {TESTBED}\n")

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Glob", "Grep"],  # Read-only — safe
        permission_mode="default",
        max_turns=5,
        max_budget_usd=0.50,
        model="sonnet",
        cwd=str(TESTBED),
        setting_sources=[],
    )

    # ---------------------------------------------------------------
    # async with = context manager that manages the subprocess
    # The Claude Code CLI runs as a child process for the whole session
    # ---------------------------------------------------------------
    async with ClaudeSDKClient(options=options) as client:

        # --- Turn 1: Ask about files ---
        await client.query("What Python files are in this directory? List them.")
        await print_response(client, "Turn 1: List files")

        # --- Turn 2: Follow-up (Claude REMEMBERS Turn 1) ---
        await client.query(
            "Read utils.py and tell me which functions lack type hints."
        )
        await print_response(client, "Turn 2: Analyze utils.py")

        # --- Turn 3: Another follow-up (context preserved) ---
        await client.query(
            "Now read models.py. Compare the code style with utils.py — "
            "which file is more consistent?"
        )
        await print_response(client, "Turn 3: Compare files")

    # ClaudeSDKClient closes cleanly here (subprocess exits)
    print("\n=== Session ended ===")
    print("Key point: Claude remembered all 3 turns without --resume flags!")


if __name__ == "__main__":
    asyncio.run(main())
