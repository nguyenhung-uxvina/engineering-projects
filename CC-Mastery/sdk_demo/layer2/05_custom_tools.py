"""
Layer 2, Level 5: Custom In-Process MCP Tools
===============================================
Run OUTSIDE Claude Code session:
    python sdk_demo/layer2/05_custom_tools.py

KEY CONCEPT:
    In Module 9, MCP tools required a SEPARATE SERVER PROCESS.
    With the SDK, you define tools as DECORATED PYTHON FUNCTIONS.
    Claude calls them directly — no protocol overhead, no subprocess.

    PATTERN:
        @tool("name", "description", InputSchema)
        async def my_tool(args: dict) -> dict:
            return {"content": [{"type": "text", "text": "result"}]}

    Then bundle into a server:
        server = create_sdk_mcp_server("server-name", tools=[my_tool])

    And pass to options:
        options = ClaudeAgentOptions(
            mcp_servers={"my-server": server},
            allowed_tools=["mcp__my-server__name"],
        )

    Tool naming convention: mcp__<server>__<tool>

COMPARISON WITH MODULE 9:
    Module 9 (standalone MCP):             SDK in-process tools:
    ─────────────────────────              ─────────────────────
    Separate .py file                      Decorated function
    FastMCP server framework               @tool decorator
    .mcp.json registration                 options.mcp_servers
    Runs as subprocess (stdio)             Runs in-process
    State persists in server memory        State = Python variables
    Reusable across sessions               Scoped to this SDK run
    Can use from interactive CC            SDK only
"""

import asyncio
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

sys.stdout.reconfigure(encoding="utf-8")

from claude_agent_sdk import (
    query, ClaudeAgentOptions,
    tool, create_sdk_mcp_server,
    AssistantMessage, ResultMessage, SystemMessage,
    TextBlock, ToolUseBlock,
)


# =============================================================================
# Tool 1: Simple stateless tool — unit converter
# =============================================================================

@tool(
    "convert_units",
    "Convert between engineering units (length, weight, temperature, pressure)",
    {
        "value": float,
        "from_unit": str,
        "to_unit": str,
    },
)
async def convert_units(args: dict[str, Any]) -> dict:
    """Stateless conversion — pure function."""
    value = args["value"]
    from_u = args["from_unit"].lower()
    to_u = args["to_unit"].lower()

    # Conversion factors to SI base units
    TO_SI = {
        # Length → meters
        "mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
        "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34,
        # Weight → kg
        "g": 0.001, "kg": 1.0, "lb": 0.453592, "oz": 0.0283495,
        # Pressure → Pa
        "pa": 1.0, "kpa": 1000.0, "mpa": 1e6, "psi": 6894.76, "bar": 1e5, "atm": 101325.0,
    }

    # Temperature is special
    if from_u in ("c", "f", "k") and to_u in ("c", "f", "k"):
        # Convert to Celsius first
        if from_u == "f":
            celsius = (value - 32) * 5 / 9
        elif from_u == "k":
            celsius = value - 273.15
        else:
            celsius = value
        # Convert from Celsius to target
        if to_u == "f":
            result = celsius * 9 / 5 + 32
        elif to_u == "k":
            result = celsius + 273.15
        else:
            result = celsius
    elif from_u in TO_SI and to_u in TO_SI:
        si_value = value * TO_SI[from_u]
        result = si_value / TO_SI[to_u]
    else:
        return {"content": [{"type": "text", "text": f"Unknown units: {from_u} -> {to_u}"}]}

    return {
        "content": [{
            "type": "text",
            "text": f"{value} {from_u} = {result:.4f} {to_u}",
        }]
    }


# =============================================================================
# Tool 2: Stateful tool — engineering notebook
# =============================================================================
# This is why it needs MCP (not a script): STATE persists across calls.

notebook_entries: list[dict] = []


@tool(
    "notebook_add",
    "Add a calculation or note to the engineering notebook",
    {
        "category": str,   # "calculation", "decision", "note"
        "content": str,
    },
)
async def notebook_add(args: dict[str, Any]) -> dict:
    entry = {
        "id": len(notebook_entries) + 1,
        "timestamp": datetime.now().isoformat(),
        "category": args["category"],
        "content": args["content"],
    }
    notebook_entries.append(entry)
    return {
        "content": [{"type": "text", "text": f"Entry #{entry['id']} recorded."}]
    }


@tool(
    "notebook_read",
    "Read all entries from the engineering notebook, optionally filtered by category",
    {
        "category": str,  # "all", "calculation", "decision", "note"
    },
)
async def notebook_read(args: dict[str, Any]) -> dict:
    cat = args.get("category", "all")
    entries = notebook_entries if cat == "all" else [
        e for e in notebook_entries if e["category"] == cat
    ]
    if not entries:
        return {"content": [{"type": "text", "text": "Notebook is empty."}]}

    lines = []
    for e in entries:
        lines.append(f"#{e['id']} [{e['category']}] {e['content']}")
    return {
        "content": [{"type": "text", "text": "\n".join(lines)}]
    }


# =============================================================================
# Bundle tools into an in-process MCP server
# =============================================================================

eng_server = create_sdk_mcp_server(
    name="engineering",
    version="1.0.0",
    tools=[convert_units, notebook_add, notebook_read],
)


# =============================================================================
# Run the agent with custom tools
# =============================================================================

async def main():
    print("=" * 60)
    print("  Custom In-Process MCP Tools Demo")
    print("=" * 60)
    print()

    async for message in query(
        prompt=(
            "You have access to an engineering toolkit. Do the following:\n\n"
            "1. Convert 150 PSI to MPa (pressure for a hydraulic system)\n"
            "2. Convert 25 degrees Celsius to Fahrenheit\n"
            "3. Convert 500mm to inches\n"
            "4. Record each conversion result in the notebook as a 'calculation'\n"
            "5. Add a 'decision' note: 'Hydraulic system rated for 1.5 MPa — sufficient'\n"
            "6. Read back all notebook entries\n\n"
            "Show the results clearly."
        ),
        options=ClaudeAgentOptions(
            # Our custom MCP server
            mcp_servers={"engineering": eng_server},
            # Allow the custom tools + Read (for general use)
            allowed_tools=[
                "mcp__engineering__convert_units",
                "mcp__engineering__notebook_add",
                "mcp__engineering__notebook_read",
                "Read",
            ],
            max_turns=15,
            max_budget_usd=0.20,
            model="sonnet",
            setting_sources=[],
        ),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(f"\n  {block.text[:500]}")
                elif isinstance(block, ToolUseBlock):
                    print(f"  [tool: {block.name}({block.input})]")

        elif isinstance(message, ResultMessage):
            print(f"\n  [done: ${message.total_cost_usd or 0:.4f}, "
                  f"turns: {message.num_turns}]")

    # Show the in-memory state
    print(f"\n{'='*60}")
    print(f"  IN-MEMORY STATE (notebook_entries)")
    print(f"{'='*60}")
    for entry in notebook_entries:
        print(f"  #{entry['id']} [{entry['category']}] {entry['content']}")

    print(f"""
{'='*60}
  WHY THIS MATTERS
{'='*60}
  1. Tools are regular Python functions — debug with print(), test with pytest
  2. State is regular Python variables — no serialization, no persistence layer
  3. Tool naming: mcp__<server>__<tool> (predictable, auto-approved with --allowedTools)
  4. Zero infrastructure: no .mcp.json, no subprocess, no FastMCP framework
  5. Claude discovers tools automatically — just list them in allowed_tools

  MODULE 9 MCP (standalone)  →  Long-lived servers, shared across sessions
  SDK MCP (in-process)       →  Ephemeral tools, scoped to one script run

  Use standalone MCP when: tool needs to persist state across sessions
  Use SDK MCP when: tool is specific to this automation script
""")


if __name__ == "__main__":
    asyncio.run(main())
