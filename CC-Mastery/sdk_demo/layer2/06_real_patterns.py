"""
Layer 2, Level 6: Real Workflow Patterns
==========================================
Run OUTSIDE Claude Code session:
    python sdk_demo/layer2/06_real_patterns.py [pattern]

    Patterns:
        fanout    — Parallel file processing with bounded concurrency
        reviewer  — Writer/Reviewer two-agent pattern
        pipeline  — Sequential analysis pipeline

KEY CONCEPT:
    The SDK primitives (query, ClaudeSDKClient, hooks, custom tools)
    combine into reusable workflow patterns. These are the patterns
    you'll use daily.
"""

import asyncio
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from claude_agent_sdk import (
    query, ClaudeAgentOptions, ClaudeSDKClient,
    AssistantMessage, ResultMessage, TextBlock, ToolUseBlock,
)

TESTBED = Path(__file__).resolve().parent.parent / "testbed"


# =============================================================================
# PATTERN A: Fan-Out / Fan-In
# =============================================================================
# Process multiple files in parallel with bounded concurrency.
# Each file gets its own independent query() — separate processes.
#
# USE WHEN: Same operation on many files (lint, type hints, docs, migration)

async def fanout_pattern():
    """Process files in parallel with bounded concurrency."""
    print("=" * 60)
    print("  PATTERN A: Fan-Out / Fan-In")
    print("=" * 60)

    files = sorted(TESTBED.glob("*.py"))
    CONCURRENCY = 2
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async def process_one(filepath: Path) -> dict:
        async with semaphore:
            print(f"  [{filepath.name}] starting...")
            start = time.time()
            result_text = ""
            cost = 0.0

            async for msg in query(
                prompt=(
                    f"Read {filepath} and write a one-line summary of what it does. "
                    "Return ONLY the summary, nothing else."
                ),
                options=ClaudeAgentOptions(
                    tools=["Read"],
                    max_turns=2,
                    max_budget_usd=0.05,
                    model="sonnet",
                    setting_sources=[],
                ),
            ):
                if isinstance(msg, ResultMessage):
                    result_text = msg.result or ""
                    cost = msg.total_cost_usd or 0.0

            elapsed = time.time() - start
            print(f"  [{filepath.name}] done ({elapsed:.1f}s, ${cost:.4f})")
            return {"file": filepath.name, "summary": result_text, "cost": cost}

    # Fan-out: dispatch all tasks
    start_total = time.time()
    results = await asyncio.gather(*[process_one(f) for f in files])
    total_time = time.time() - start_total
    total_cost = sum(r["cost"] for r in results)

    # Fan-in: collect results
    print(f"\n  Results ({total_time:.1f}s total, ${total_cost:.4f}):")
    for r in results:
        print(f"    {r['file']:15s} {r['summary'][:60]}")


# =============================================================================
# PATTERN B: Writer / Reviewer (Two-Agent)
# =============================================================================
# Agent 1 writes code. Agent 2 reviews it (fresh context, no bias).
# If review finds issues, loop back to writer with feedback.
#
# USE WHEN: Quality-critical tasks (production code, security-sensitive)

async def reviewer_pattern():
    """Two-agent writer/reviewer loop."""
    print("\n" + "=" * 60)
    print("  PATTERN B: Writer / Reviewer")
    print("=" * 60)

    target = TESTBED / "utils.py"
    max_rounds = 2

    for round_num in range(1, max_rounds + 1):
        print(f"\n  --- Round {round_num} ---")

        # WRITER: modify the file
        print(f"  [Writer] Working...")
        writer_result = ""
        async for msg in query(
            prompt=(
                f"Read {target} and add type hints to ALL functions. "
                "Use standard library types. Don't change logic."
            ),
            options=ClaudeAgentOptions(
                allowed_tools=["Read", "Edit"],
                permission_mode="acceptEdits",
                max_turns=5,
                max_budget_usd=0.10,
                model="sonnet",
                setting_sources=[],
            ),
        ):
            if isinstance(msg, ResultMessage):
                writer_result = msg.result or ""
                print(f"  [Writer] Done (${msg.total_cost_usd or 0:.4f})")

        # REVIEWER: analyze the result (READ-ONLY, fresh context)
        print(f"  [Reviewer] Reviewing...")
        review_text = ""
        async for msg in query(
            prompt=(
                f"Read {target} and review the type hints. Check:\n"
                "1. Are all functions annotated?\n"
                "2. Are the types correct?\n"
                "3. Any missing imports?\n\n"
                "If everything is correct, say 'APPROVED'.\n"
                "If there are issues, list them specifically."
            ),
            options=ClaudeAgentOptions(
                tools=["Read"],  # Read-only — reviewer can't modify
                max_turns=2,
                max_budget_usd=0.05,
                model="sonnet",
                setting_sources=[],
            ),
        ):
            if isinstance(msg, ResultMessage):
                review_text = msg.result or ""
                print(f"  [Reviewer] Done (${msg.total_cost_usd or 0:.4f})")

        print(f"  [Review]: {review_text[:200]}")

        if "APPROVED" in review_text.upper():
            print(f"\n  Review PASSED on round {round_num}")
            break
        else:
            print(f"  Issues found — will iterate...")

    else:
        print(f"\n  Max rounds ({max_rounds}) reached.")


# =============================================================================
# PATTERN C: Sequential Pipeline
# =============================================================================
# Multi-step analysis where each step builds on the previous.
# Uses ClaudeSDKClient for shared context (cheaper than re-reading).
#
# USE WHEN: Deep analysis, investigation, multi-step reasoning

async def pipeline_pattern():
    """Sequential analysis with shared context."""
    print("\n" + "=" * 60)
    print("  PATTERN C: Sequential Pipeline")
    print("=" * 60)

    options = ClaudeAgentOptions(
        tools=["Read", "Glob", "Grep"],  # Read-only
        max_turns=5,
        max_budget_usd=0.30,
        model="sonnet",
        cwd=str(TESTBED),
        setting_sources=[],
    )

    total_cost = 0.0

    async with ClaudeSDKClient(options=options) as client:
        steps = [
            ("SCAN", "List all Python files and their sizes."),
            ("ANALYZE", "Read each file. What patterns and libraries do they use?"),
            ("ASSESS", "Based on your analysis, rank the files by code quality (1=best). Explain your ranking."),
            ("RECOMMEND", "Give 3 specific, prioritized recommendations to improve this codebase."),
        ]

        for step_name, prompt in steps:
            print(f"\n  [{step_name}]")
            await client.query(prompt)

            async for msg in client.receive_response():
                if isinstance(msg, AssistantMessage):
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            # Show first 300 chars of response
                            preview = block.text[:300]
                            if len(block.text) > 300:
                                preview += "..."
                            print(f"    {preview}")
                        elif isinstance(block, ToolUseBlock):
                            print(f"    [tool: {block.name}]")
                elif isinstance(msg, ResultMessage):
                    step_cost = msg.total_cost_usd or 0.0
                    total_cost += step_cost
                    print(f"    [${step_cost:.4f}]")

    print(f"\n  Pipeline total cost: ${total_cost:.4f}")
    print(f"  (Context reuse saved ~50% vs independent queries)")


# =============================================================================
# Main: run selected pattern
# =============================================================================

async def main():
    pattern = sys.argv[1] if len(sys.argv) > 1 else "all"

    if pattern in ("fanout", "all"):
        await fanout_pattern()
    if pattern in ("reviewer", "all"):
        await reviewer_pattern()
    if pattern in ("pipeline", "all"):
        await pipeline_pattern()

    if pattern not in ("fanout", "reviewer", "pipeline", "all"):
        print("Usage: python 06_real_patterns.py [fanout|reviewer|pipeline|all]")

    print(f"""
{'='*60}
  PATTERN DECISION MATRIX
{'='*60}
  | Pattern    | When                    | SDK Feature Used       |
  |------------|-------------------------|------------------------|
  | Fan-out    | Same op, many files     | query() + Semaphore    |
  | Reviewer   | Quality-critical writes  | query() x2 (separate)  |
  | Pipeline   | Deep multi-step analysis | ClaudeSDKClient        |

  RULE OF THUMB:
    Independent tasks → Fan-out with query()
    Dependent steps   → Pipeline with ClaudeSDKClient
    Need fresh eyes   → Separate query() instances
""")


if __name__ == "__main__":
    asyncio.run(main())
