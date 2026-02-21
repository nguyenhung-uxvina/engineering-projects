"""
Exercise 2: Non-Coding Agent with Python SDK
=============================================================================
Module 10, CC-Mastery

PURPOSE: Build a research agent that:
  1. Takes a topic as input
  2. Uses Claude to research it (web search + analysis)
  3. Returns structured output (Pydantic model)
  4. Demonstrates multi-turn with ClaudeSDKClient

USAGE:
  pip install claude-agent-sdk pydantic
  python 02_research_agent.py "quantum computing 2025 breakthroughs"
  python 02_research_agent.py --multi-turn  # Interactive multi-turn demo

PREREQUISITES: claude CLI installed and authenticated
=============================================================================
"""

import asyncio
import sys
import json
from dataclasses import dataclass
from pathlib import Path

# --- Check dependencies ---
try:
    from pydantic import BaseModel
except ImportError:
    print("Install pydantic: pip install pydantic")
    sys.exit(1)

try:
    from claude_agent_sdk import (
        query,
        ClaudeAgentOptions,
        AssistantMessage,
        ResultMessage,
    )
    HAS_SDK = True
except ImportError:
    print("Install SDK: pip install claude-agent-sdk")
    print("Falling back to CLI mode (claude -p)...")
    HAS_SDK = False


# =============================================================================
# Structured Output Schema
# =============================================================================

class Finding(BaseModel):
    claim: str
    confidence: str  # "high", "medium", "low"
    source: str

class ResearchReport(BaseModel):
    topic: str
    summary: str
    key_findings: list[Finding]
    open_questions: list[str]
    recommended_next_steps: list[str]


# =============================================================================
# Pattern A: One-Shot with query() + Structured Output
# =============================================================================

async def research_oneshot(topic: str) -> ResearchReport | None:
    """Single-shot research agent with structured output."""
    print(f"\n=== One-Shot Research: '{topic}' ===\n")

    schema = ResearchReport.model_json_schema()

    result = None
    async for message in query(
        prompt=(
            f"Research the topic: '{topic}'\n\n"
            "Use web search to find recent information. "
            "Produce a research report with key findings, confidence levels, "
            "open questions, and recommended next steps. "
            "Each finding should cite its source."
        ),
        options=ClaudeAgentOptions(
            allowed_tools=["WebSearch", "WebFetch", "Read"],
            max_turns=8,
            max_budget_usd=0.50,
            model="sonnet",
            output_format={"type": "json_schema", "schema": schema},
        ),
    ):
        if isinstance(message, AssistantMessage):
            # Show progress
            for block in message.content:
                if hasattr(block, "text") and block.text:
                    print(f"  [thinking] {block.text[:120]}...")
                elif hasattr(block, "name"):
                    print(f"  [tool] {block.name}")

        elif isinstance(message, ResultMessage):
            print(f"\n  Cost: ${message.total_cost_usd:.4f}")
            if message.structured_output:
                result = ResearchReport.model_validate(message.structured_output)

    return result


# =============================================================================
# Pattern B: Multi-Turn with ClaudeSDKClient
# =============================================================================

async def research_multiturn():
    """Interactive multi-turn research session."""
    print("\n=== Multi-Turn Research Agent ===")
    print("Type your questions. 'quit' to exit.\n")

    try:
        from claude_agent_sdk import ClaudeSDKClient, TextBlock
    except ImportError:
        print("ClaudeSDKClient requires claude-agent-sdk. Install it first.")
        return

    options = ClaudeAgentOptions(
        allowed_tools=["WebSearch", "WebFetch", "Read", "Glob", "Grep"],
        max_turns=5,
        max_budget_usd=1.00,
        model="sonnet",
        system_prompt={
            "type": "preset",
            "preset": "claude_code",
            "append": (
                "You are a research assistant. Answer questions thoroughly, "
                "citing sources. Remember context from previous questions in "
                "this conversation."
            ),
        },
    )

    total_cost = 0.0

    async with ClaudeSDKClient(options=options) as client:
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ("quit", "exit", "q"):
                break
            if not user_input:
                continue

            await client.query(user_input)
            async for msg in client.receive_response():
                if isinstance(msg, AssistantMessage):
                    for block in msg.content:
                        if isinstance(block, TextBlock):
                            print(f"\nAgent: {block.text}")
                elif isinstance(msg, ResultMessage):
                    if msg.total_cost_usd:
                        total_cost += msg.total_cost_usd
                    print(f"\n  [turn cost: ${msg.total_cost_usd:.4f}, "
                          f"session total: ${total_cost:.4f}]")

    print(f"\nSession ended. Total cost: ${total_cost:.4f}")


# =============================================================================
# Pattern C: CLI Fallback (no SDK installed)
# =============================================================================

def research_cli_fallback(topic: str):
    """Fallback using subprocess + claude -p when SDK not installed."""
    import subprocess

    schema = json.dumps(ResearchReport.model_json_schema())

    print(f"\n=== CLI Fallback Research: '{topic}' ===\n")

    cmd = [
        "claude", "-p",
        f"Research '{topic}' using web search. Produce a report with "
        f"findings (with confidence and sources), open questions, and next steps.",
        "--output-format", "json",
        "--json-schema", schema,
        "--max-turns", "8",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None

    data = json.loads(result.stdout)
    if data.get("structured_output"):
        report = ResearchReport.model_validate(data["structured_output"])
        return report
    else:
        print(f"Raw result: {data.get('result', 'no result')}")
        return None


# =============================================================================
# Display
# =============================================================================

def display_report(report: ResearchReport):
    """Pretty-print a research report."""
    print(f"\n{'='*60}")
    print(f"RESEARCH REPORT: {report.topic}")
    print(f"{'='*60}")
    print(f"\nSummary:\n  {report.summary}")

    print(f"\nKey Findings ({len(report.key_findings)}):")
    for i, f in enumerate(report.key_findings, 1):
        print(f"  {i}. [{f.confidence.upper()}] {f.claim}")
        print(f"     Source: {f.source}")

    print(f"\nOpen Questions:")
    for q in report.open_questions:
        print(f"  - {q}")

    print(f"\nNext Steps:")
    for s in report.recommended_next_steps:
        print(f"  - {s}")

    print(f"\n{'='*60}")


# =============================================================================
# Main
# =============================================================================

async def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  python 02_research_agent.py "topic to research"')
        print("  python 02_research_agent.py --multi-turn")
        sys.exit(1)

    if sys.argv[1] == "--multi-turn":
        if HAS_SDK:
            await research_multiturn()
        else:
            print("Multi-turn requires claude-agent-sdk. Install it first.")
    else:
        topic = " ".join(sys.argv[1:])

        if HAS_SDK:
            report = await research_oneshot(topic)
        else:
            report = research_cli_fallback(topic)

        if report:
            display_report(report)
        else:
            print("No structured report produced.")


if __name__ == "__main__":
    asyncio.run(main())
