"""
Layer 2, Level 3: ClaudeSDKClient — Multi-Turn Conversations
==============================================================
Run OUTSIDE Claude Code session:
    python sdk_demo/layer2/03_multiturn.py

KEY CONCEPT:
    ClaudeSDKClient manages a PERSISTENT Claude Code subprocess.
    Each query() call shares the same conversation context.
    Claude remembers everything from previous turns.

    LIFECYCLE:
        async with ClaudeSDKClient(options) as client:
            await client.query("Turn 1")         # Sends prompt
            async for msg in client.receive_response():  # Reads response
                ...
            await client.query("Turn 2")         # Sends follow-up
            async for msg in client.receive_response():  # Claude remembers Turn 1!
                ...

    BONUS METHODS:
        client.interrupt()         — Stop the agent mid-execution
        client.set_model("opus")   — Switch model between turns
        client.set_permission_mode("acceptEdits")  — Change permissions
        client.rewind_files(uuid)  — Restore files to a checkpoint
"""

import asyncio
import sys

sys.stdout.reconfigure(encoding="utf-8")

from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage, ResultMessage, SystemMessage,
    TextBlock, ToolUseBlock,
)
from pathlib import Path

TESTBED = Path(__file__).resolve().parent.parent / "testbed"


async def collect_response(client: ClaudeSDKClient, label: str) -> str:
    """Collect full text response from a turn. Returns the text."""
    print(f"\n{'━'*60}")
    print(f"  {label}")
    print(f"{'━'*60}")

    full_text = []
    cost = 0.0

    async for msg in client.receive_response():
        if isinstance(msg, SystemMessage):
            print(f"  [session: {msg.data.get('session_id', '?')[:12]}...]")

        elif isinstance(msg, AssistantMessage):
            for block in msg.content:
                if isinstance(block, TextBlock):
                    full_text.append(block.text)
                    # Print, but truncate long responses
                    preview = block.text[:400]
                    if len(block.text) > 400:
                        preview += f"\n  ... ({len(block.text)} chars total)"
                    print(f"  {preview}")
                elif isinstance(block, ToolUseBlock):
                    print(f"  [tool: {block.name}]")

        elif isinstance(msg, ResultMessage):
            cost = msg.total_cost_usd or 0.0
            print(f"  [cost: ${cost:.4f}, turns: {msg.num_turns}]")

    return "\n".join(full_text)


async def demo_basic_multiturn():
    """Demo 1: Basic multi-turn conversation."""
    print("=" * 60)
    print("  DEMO 1: Basic Multi-Turn")
    print("=" * 60)

    options = ClaudeAgentOptions(
        tools=["Read", "Glob"],   # Read-only
        max_turns=5,
        max_budget_usd=0.30,
        model="sonnet",
        cwd=str(TESTBED),
        setting_sources=[],
    )

    async with ClaudeSDKClient(options=options) as client:
        # Turn 1: Ask about files
        await client.query("List all Python files in this directory.")
        await collect_response(client, "Turn 1: What files exist?")

        # Turn 2: Claude remembers the file list from Turn 1
        await client.query(
            "Read utils.py and tell me how many functions it has."
        )
        await collect_response(client, "Turn 2: Analyze utils.py")

        # Turn 3: Claude remembers BOTH previous turns
        await client.query(
            "Based on what you've seen so far, which file would benefit "
            "most from refactoring? Explain why."
        )
        text = await collect_response(client, "Turn 3: Recommendation (from memory)")

        # KEY POINT: Turn 3 uses context from Turn 1 AND Turn 2
        # without re-reading any files. That's the power of multi-turn.


async def demo_model_switching():
    """Demo 2: Switch models between turns."""
    print("\n" + "=" * 60)
    print("  DEMO 2: Model Switching")
    print("=" * 60)

    options = ClaudeAgentOptions(
        tools=["Read"],
        max_turns=3,
        max_budget_usd=0.30,
        model="sonnet",          # Start cheap
        cwd=str(TESTBED),
        setting_sources=[],
    )

    async with ClaudeSDKClient(options=options) as client:
        # Turn 1: Quick scan with Sonnet (cheap)
        await client.query(f"Read {TESTBED / 'models.py'} quickly.")
        await collect_response(client, "Turn 1 (Sonnet): Quick read")

        # Switch to Opus for the hard thinking
        await client.set_model("opus")
        print("\n  >>> Switched model to Opus <<<\n")

        # Turn 2: Deep analysis with Opus (smart)
        await client.query(
            "Now analyze the design patterns in that file. "
            "What's the most significant architectural improvement you'd suggest?"
        )
        await collect_response(client, "Turn 2 (Opus): Deep analysis")

    # Pattern: Sonnet for data gathering, Opus for reasoning
    # Saves ~80% cost on the reading turns.


async def demo_interrupt():
    """Demo 3: Interrupt a running agent."""
    print("\n" + "=" * 60)
    print("  DEMO 3: Interrupt")
    print("=" * 60)

    options = ClaudeAgentOptions(
        tools=["Read", "Glob", "Grep"],
        max_turns=20,            # High limit — we'll interrupt before this
        model="sonnet",
        cwd=str(TESTBED),
        setting_sources=[],
    )

    async with ClaudeSDKClient(options=options) as client:
        # Start a potentially long task
        await client.query(
            "Do a comprehensive analysis of every function in every file. "
            "Check naming conventions, complexity, and documentation."
        )

        # Read first few messages, then interrupt
        count = 0
        async for msg in client.receive_response():
            count += 1
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, ToolUseBlock):
                        print(f"  [msg {count}] tool: {block.name}")
                    elif isinstance(block, TextBlock):
                        print(f"  [msg {count}] text: {block.text[:80]}...")

            # After seeing 3 messages, interrupt
            if count >= 3:
                print("\n  >>> INTERRUPTING AGENT <<<\n")
                await client.interrupt()
                break

        # We can still continue the conversation after interrupt!
        await client.query("Just give me a one-sentence summary of what you found so far.")
        await collect_response(client, "After interrupt: Summary")


async def main():
    await demo_basic_multiturn()
    await demo_model_switching()
    await demo_interrupt()

    print("\n" + "=" * 60)
    print("  KEY TAKEAWAYS")
    print("=" * 60)
    print("""
    1. ClaudeSDKClient = one persistent subprocess, shared context
    2. Each query() + receive_response() = one conversation turn
    3. Claude remembers ALL previous turns (no --resume needed)
    4. set_model() lets you switch cheap/smart between turns
    5. interrupt() stops execution but keeps the session alive
    6. async with = automatic cleanup (subprocess killed on exit)
    """)


if __name__ == "__main__":
    asyncio.run(main())
