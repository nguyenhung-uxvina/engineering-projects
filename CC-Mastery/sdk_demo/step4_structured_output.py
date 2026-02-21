"""
Step 4: Structured Output with Pydantic
=========================================
Run OUTSIDE Claude Code session:
  python sdk_demo/step4_structured_output.py

Demonstrates:
  - Pydantic model → JSON Schema → SDK output_format
  - Validated, typed results from Claude
  - Error handling for schema validation failures

Key insight: Claude generates VALID JSON matching your schema,
or returns error_max_structured_output_retries as subtype.
"""

import asyncio
import json
import sys
from pathlib import Path

from pydantic import BaseModel, Field
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    ResultMessage,
    AssistantMessage,
    ToolUseBlock,
)


# =============================================================================
# Step 1: Define your output schema with Pydantic
# =============================================================================

class FunctionInfo(BaseModel):
    name: str = Field(description="Function or method name")
    params: list[str] = Field(description="Parameter names (excluding self)")
    has_type_hints: bool = Field(description="Whether it has type annotations")
    return_type: str = Field(description="Return type if annotated, else 'unknown'")
    complexity: str = Field(description="'simple' (1-3 lines), 'medium' (4-10), 'complex' (10+)")


class FileAnalysis(BaseModel):
    filename: str
    total_functions: int
    typed_functions: int
    untyped_functions: int
    functions: list[FunctionInfo]
    type_hint_coverage: float = Field(description="Percentage 0-100")
    recommendations: list[str] = Field(description="Improvement suggestions")


# =============================================================================
# Step 2: Generate JSON Schema from Pydantic model
# =============================================================================

def get_schema():
    """Convert Pydantic model to JSON Schema for the SDK."""
    schema = FileAnalysis.model_json_schema()
    # The SDK needs a top-level object schema
    print("Generated JSON Schema:")
    print(json.dumps(schema, indent=2)[:500])
    print("...\n")
    return schema


# =============================================================================
# Step 3: Query with structured output
# =============================================================================

TESTBED = Path(__file__).parent / "testbed"


async def analyze_file(filepath: Path) -> FileAnalysis | None:
    """Analyze a Python file and return structured results."""
    schema = FileAnalysis.model_json_schema()

    async for msg in query(
        prompt=(
            f"Analyze the Python file at {filepath}. "
            "Examine every function and method. "
            "Determine type hint coverage and suggest improvements."
        ),
        options=ClaudeAgentOptions(
            allowed_tools=["Read"],
            max_turns=3,
            max_budget_usd=0.15,
            model="sonnet",
            cwd=str(filepath.parent),
            setting_sources=[],
            # THIS IS THE KEY: output_format with json_schema
            output_format={
                "type": "json_schema",
                "schema": schema,
            },
        ),
    ):
        if isinstance(msg, AssistantMessage):
            for block in msg.content:
                if isinstance(block, ToolUseBlock):
                    print(f"  [tool: {block.name}]")

        elif isinstance(msg, ResultMessage):
            print(f"  [status: {msg.subtype}, cost: ${msg.total_cost_usd:.4f}]")

            if msg.subtype == "success" and msg.structured_output:
                # Validate with Pydantic
                return FileAnalysis.model_validate(msg.structured_output)
            elif msg.subtype == "error_max_structured_output_retries":
                print("  ERROR: Claude couldn't produce valid JSON for this schema")
                return None

    return None


# =============================================================================
# Step 4: Run analysis on all testbed files
# =============================================================================

async def main():
    print("=== Structured Output Demo ===\n")

    # Show the schema we're using
    get_schema()

    # Analyze each file
    results: list[FileAnalysis] = []
    for pyfile in sorted(TESTBED.glob("*.py")):
        print(f"Analyzing: {pyfile.name}")
        analysis = await analyze_file(pyfile)
        if analysis:
            results.append(analysis)
        print()

    # Display results
    if not results:
        print("No results. Run from outside a Claude Code session.")
        return

    print("=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)

    for r in results:
        print(f"\n--- {r.filename} ---")
        print(f"  Functions: {r.total_functions} total, "
              f"{r.typed_functions} typed, {r.untyped_functions} untyped")
        print(f"  Coverage: {r.type_hint_coverage:.0f}%")
        print(f"  Details:")
        for f in r.functions:
            hint_icon = "+" if f.has_type_hints else "-"
            print(f"    [{hint_icon}] {f.name}({', '.join(f.params)}) "
                  f"-> {f.return_type} [{f.complexity}]")
        print(f"  Recommendations:")
        for rec in r.recommendations:
            print(f"    - {rec}")

    # Summary
    total_funcs = sum(r.total_functions for r in results)
    typed_funcs = sum(r.typed_functions for r in results)
    coverage = (typed_funcs / total_funcs * 100) if total_funcs else 0
    print(f"\n{'='*60}")
    print(f"TOTAL: {typed_funcs}/{total_funcs} functions typed ({coverage:.0f}%)")


if __name__ == "__main__":
    asyncio.run(main())
