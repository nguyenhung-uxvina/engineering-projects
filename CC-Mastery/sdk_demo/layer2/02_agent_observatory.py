"""
Layer 2, Level 2: Agent Observatory — Watch Everything
=======================================================
Run OUTSIDE Claude Code session:
    python sdk_demo/layer2/02_agent_observatory.py

KEY CONCEPT:
    The message stream lets you BUILD OBSERVABILITY into the agent.
    Log every tool call, measure timing, track costs per tool.
    This is how you debug agents and build dashboards.

OUTPUT:
    A structured log showing exactly what the agent did,
    how long each step took, and what it cost.
"""

import asyncio
import sys
import time
from dataclasses import dataclass, field

sys.stdout.reconfigure(encoding="utf-8")

from claude_agent_sdk import (
    query, ClaudeAgentOptions,
    SystemMessage, AssistantMessage, UserMessage, ResultMessage,
    TextBlock, ToolUseBlock, ToolResultBlock,
)
from pathlib import Path

TESTBED = Path(__file__).resolve().parent.parent / "testbed"


# =============================================================================
# The Observer: captures a structured execution trace
# =============================================================================

@dataclass
class ToolCall:
    name: str
    input_summary: str
    output_summary: str = ""
    timestamp: float = 0.0
    duration_ms: float = 0.0
    is_error: bool = False


@dataclass
class AgentTrace:
    """Full execution trace of an agent run."""
    session_id: str = ""
    model: str = ""
    start_time: float = 0.0
    tool_calls: list[ToolCall] = field(default_factory=list)
    text_outputs: list[str] = field(default_factory=list)
    total_cost_usd: float = 0.0
    total_turns: int = 0
    duration_ms: int = 0
    status: str = ""

    # Pending tool call (between ToolUseBlock and ToolResultBlock)
    _pending: ToolCall | None = field(default=None, repr=False)

    def on_tool_use(self, name: str, tool_input: dict):
        """Agent is calling a tool."""
        self._pending = ToolCall(
            name=name,
            input_summary=_summarize_input(name, tool_input),
            timestamp=time.time(),
        )

    def on_tool_result(self, content, is_error: bool = False):
        """Tool returned a result."""
        if self._pending:
            self._pending.duration_ms = (time.time() - self._pending.timestamp) * 1000
            self._pending.output_summary = _summarize_output(content)
            self._pending.is_error = is_error or False
            self.tool_calls.append(self._pending)
            self._pending = None

    def on_text(self, text: str):
        self.text_outputs.append(text)

    def report(self) -> str:
        """Generate a human-readable execution report."""
        lines = [
            f"{'='*60}",
            f"  AGENT EXECUTION TRACE",
            f"{'='*60}",
            f"  Session:  {self.session_id}",
            f"  Model:    {self.model}",
            f"  Status:   {self.status}",
            f"  Turns:    {self.total_turns}",
            f"  Cost:     ${self.total_cost_usd:.4f}",
            f"  Duration: {self.duration_ms}ms",
            f"",
            f"  TOOL CALLS ({len(self.tool_calls)}):",
        ]
        for i, tc in enumerate(self.tool_calls, 1):
            err = " ERROR" if tc.is_error else ""
            lines.append(f"    {i}. {tc.name}{err} ({tc.duration_ms:.0f}ms)")
            lines.append(f"       in:  {tc.input_summary}")
            lines.append(f"       out: {tc.output_summary}")

        if self.text_outputs:
            lines.append(f"")
            lines.append(f"  FINAL RESPONSE:")
            # Only show last text block (the actual answer)
            last_text = self.text_outputs[-1]
            for line in last_text.split("\n")[:15]:
                lines.append(f"    {line}")
            if last_text.count("\n") > 15:
                lines.append(f"    ... ({last_text.count(chr(10))} lines total)")

        lines.append(f"{'='*60}")
        return "\n".join(lines)


def _summarize_input(tool_name: str, tool_input: dict) -> str:
    if tool_name == "Read":
        return tool_input.get("file_path", "?")
    if tool_name == "Edit":
        fp = tool_input.get("file_path", "?")
        old = (tool_input.get("old_string", ""))[:40]
        return f"{fp} (replacing '{old}...')"
    if tool_name == "Write":
        return tool_input.get("file_path", "?")
    if tool_name == "Bash":
        return tool_input.get("command", "?")[:80]
    if tool_name in ("Glob", "Grep"):
        return tool_input.get("pattern", "?")
    return str(tool_input)[:80]


def _summarize_output(content) -> str:
    if content is None:
        return "(empty)"
    s = str(content)
    return s[:100] + "..." if len(s) > 100 else s


# =============================================================================
# Run the agent with full observation
# =============================================================================

async def main():
    trace = AgentTrace(start_time=time.time())

    print("Running agent with full observation...")
    print(f"Target: {TESTBED}\n")

    async for message in query(
        prompt=(
            f"Read all Python files in {TESTBED}. "
            "For each file, count the number of functions and whether they have type hints. "
            "Summarize as a table."
        ),
        options=ClaudeAgentOptions(
            tools=["Read", "Glob"],
            max_turns=10,
            max_budget_usd=0.20,
            model="sonnet",
            setting_sources=[],
        ),
    ):
        if isinstance(message, SystemMessage):
            trace.session_id = message.data.get("session_id", "?")
            trace.model = message.data.get("model", "?")

        elif isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock):
                    trace.on_tool_use(block.name, block.input)
                    # Real-time progress indicator
                    print(f"  -> {block.name}({_summarize_input(block.name, block.input)[:50]})")
                elif isinstance(block, TextBlock):
                    trace.on_text(block.text)

        elif isinstance(message, UserMessage):
            # UserMessage carries tool results
            if isinstance(message.content, list):
                for block in message.content:
                    if isinstance(block, ToolResultBlock):
                        trace.on_tool_result(block.content, block.is_error)
            elif message.tool_use_result:
                trace.on_tool_result(message.tool_use_result)

        elif isinstance(message, ResultMessage):
            trace.status = message.subtype
            trace.total_cost_usd = message.total_cost_usd or 0.0
            trace.total_turns = message.num_turns
            trace.duration_ms = message.duration_ms

    # Print the full trace report
    print()
    print(trace.report())

    # --- Bonus: tool call frequency ---
    print()
    from collections import Counter
    freq = Counter(tc.name for tc in trace.tool_calls)
    print("Tool frequency:", dict(freq))
    print(f"Avg time per tool call: {sum(tc.duration_ms for tc in trace.tool_calls) / max(len(trace.tool_calls), 1):.0f}ms")


if __name__ == "__main__":
    asyncio.run(main())
