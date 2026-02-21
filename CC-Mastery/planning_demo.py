"""planning_demo.py -- Analyze Claude Code session history for planning patterns.

Module 5 exercise: demonstrates plan-before-implement workflow.
Reads JSONL session files and reports on tool use patterns,
planning ratios, and exploration-vs-implementation sequences.
"""

import json
import sys
from pathlib import Path
from collections import Counter
from datetime import datetime
from dataclasses import dataclass, field

# ── Constants ──────────────────────────────────────────────────────

SESSION_DIR = Path(
    r"C:\Users\ADMIN\.claude\projects\d--UxV-engineering-projects-CC-Mastery"
)

EXPLORATION_TOOLS = {
    "Read", "Grep", "Glob", "Task", "Skill", "WebFetch",
    "WebSearch", "AskUserQuestion",
}
IMPLEMENTATION_TOOLS = {"Edit", "Write", "NotebookEdit"}
PLANNING_TOOLS = {"EnterPlanMode", "ExitPlanMode", "TodoWrite"}

# Bash commands containing these substrings are classified as implementation
BASH_WRITE_PATTERNS = [
    "mkdir", "touch", "rm ", "mv ", "cp ", "git add", "git commit",
    "git push", "npm install", "pip install", ">", ">>", "tee ",
]

BAR_WIDTH = 28
BAR_FILLED = "\u2588"
BAR_EMPTY = "\u2591"


# ── Data Classes ───────────────────────────────────────────────────

@dataclass
class ToolUse:
    name: str
    category: str       # exploration | implementation | planning
    timestamp: str
    request_id: str


@dataclass
class TokenUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_tokens: int = 0
    cache_read_tokens: int = 0
    total_input: int = 0


@dataclass
class SessionData:
    session_id: str
    filepath: Path
    entries_by_type: Counter = field(default_factory=Counter)
    human_message_count: int = 0
    assistant_turn_count: int = 0
    tool_uses: list = field(default_factory=list)
    timestamps: list = field(default_factory=list)
    token_usage_raw: list = field(default_factory=list)


@dataclass
class ToolAnalysis:
    exploration_count: int = 0
    implementation_count: int = 0
    planning_count: int = 0
    tool_counts: Counter = field(default_factory=Counter)


@dataclass
class SequenceAnalysis:
    first_exploration_idx: int | None = None
    first_implementation_idx: int | None = None
    pattern: str = "unknown"


# ── Parsers ────────────────────────────────────────────────────────

def discover_sessions(base_path: Path) -> list[Path]:
    """Find top-level .jsonl session files (skip subagent dirs)."""
    return sorted(base_path.glob("*.jsonl"))


def parse_entry(line: str, line_num: int, filepath: str) -> dict | None:
    """Parse a single JSONL line. Returns None on failure."""
    line = line.strip()
    if not line:
        return None
    try:
        return json.loads(line)
    except json.JSONDecodeError as e:
        print(f"  WARNING: Skipping line {line_num} in {filepath}: {e}",
              file=sys.stderr)
        return None


def classify_bash_command(command: str) -> str:
    """Classify a Bash command as exploration or implementation."""
    cmd_lower = command.lower()
    for pattern in BASH_WRITE_PATTERNS:
        if pattern in cmd_lower:
            return "implementation"
    return "exploration"


def classify_tool(name: str, input_data: dict) -> str:
    """Classify a tool use into exploration/implementation/planning."""
    if name in PLANNING_TOOLS:
        return "planning"
    if name in EXPLORATION_TOOLS:
        return "exploration"
    if name in IMPLEMENTATION_TOOLS:
        return "implementation"
    if name == "Bash":
        return classify_bash_command(input_data.get("command", ""))
    # MCP tools and unknowns default to exploration
    return "exploration"


def parse_session(filepath: Path) -> SessionData:
    """Parse a JSONL session file into structured data."""
    data = SessionData(session_id=filepath.stem, filepath=filepath)
    seen_request_ids = set()

    with open(filepath, encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            entry = parse_entry(line, line_num, str(filepath))
            if entry is None:
                continue

            entry_type = entry.get("type", "unknown")
            data.entries_by_type[entry_type] += 1

            # Collect timestamps
            ts = entry.get("timestamp")
            if ts:
                data.timestamps.append(ts)
            elif entry_type == "file-history-snapshot":
                nested_ts = entry.get("snapshot", {}).get("timestamp")
                if nested_ts:
                    data.timestamps.append(nested_ts)

            # Count human messages (string content = typed by user)
            if entry_type == "user":
                content = entry.get("message", {}).get("content")
                if isinstance(content, str):
                    data.human_message_count += 1

            # Process assistant entries
            if entry_type == "assistant":
                request_id = entry.get("requestId", "")
                if request_id and request_id not in seen_request_ids:
                    seen_request_ids.add(request_id)
                    data.assistant_turn_count += 1

                # Token usage (one per requestId to avoid inflation)
                usage = entry.get("message", {}).get("usage")
                if usage and request_id:
                    data.token_usage_raw.append((request_id, usage))

                # Extract tool uses from content blocks
                content_blocks = entry.get("message", {}).get("content", [])
                if not isinstance(content_blocks, list):
                    continue
                for block in content_blocks:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        tool_name = block.get("name", "unknown")
                        tool_input = block.get("input", {})
                        if not isinstance(tool_input, dict):
                            tool_input = {}
                        category = classify_tool(tool_name, tool_input)
                        data.tool_uses.append(ToolUse(
                            name=tool_name,
                            category=category,
                            timestamp=entry.get("timestamp", ""),
                            request_id=request_id,
                        ))

    return data


# ── Analyzers ──────────────────────────────────────────────────────

def analyze_tools(data: SessionData) -> ToolAnalysis:
    """Aggregate tool use counts by category and name."""
    analysis = ToolAnalysis()
    for tu in data.tool_uses:
        analysis.tool_counts[tu.name] += 1
        if tu.category == "exploration":
            analysis.exploration_count += 1
        elif tu.category == "implementation":
            analysis.implementation_count += 1
        elif tu.category == "planning":
            analysis.planning_count += 1
    return analysis


def analyze_sequence(data: SessionData) -> SequenceAnalysis:
    """Determine exploration-first vs implementation-first pattern."""
    seq = SequenceAnalysis()
    if not data.tool_uses:
        seq.pattern = "no-tools"
        return seq

    for i, tu in enumerate(data.tool_uses):
        if tu.category == "exploration" and seq.first_exploration_idx is None:
            seq.first_exploration_idx = i
        if tu.category == "implementation" and seq.first_implementation_idx is None:
            seq.first_implementation_idx = i

    has_exp = seq.first_exploration_idx is not None
    has_imp = seq.first_implementation_idx is not None

    if has_exp and not has_imp:
        seq.pattern = "exploration-only"
    elif not has_exp and has_imp:
        seq.pattern = "implementation-only"
    elif not has_exp and not has_imp:
        seq.pattern = "planning-only"
    elif seq.first_exploration_idx < seq.first_implementation_idx:
        seq.pattern = "exploration-first"
    else:
        seq.pattern = "implementation-first"

    return seq


def compute_token_usage(data: SessionData) -> TokenUsage:
    """Sum token usage, deduplicated by requestId."""
    last_per_request = {}
    for request_id, usage in data.token_usage_raw:
        last_per_request[request_id] = usage

    result = TokenUsage()
    for usage in last_per_request.values():
        result.input_tokens += usage.get("input_tokens", 0)
        result.output_tokens += usage.get("output_tokens", 0)
        result.cache_creation_tokens += usage.get("cache_creation_input_tokens", 0)
        result.cache_read_tokens += usage.get("cache_read_input_tokens", 0)

    result.total_input = (
        result.input_tokens + result.cache_creation_tokens + result.cache_read_tokens
    )
    return result


def compute_planning_ratio(tool_analysis: ToolAnalysis) -> float | None:
    """Exploration / (exploration + implementation). None if no tools."""
    total = tool_analysis.exploration_count + tool_analysis.implementation_count
    if total == 0:
        return None
    return tool_analysis.exploration_count / total


def get_date_range(timestamps: list[str]) -> tuple[str, str]:
    """Earliest and latest from ISO 8601 timestamp strings."""
    if not timestamps:
        return ("N/A", "N/A")
    parsed = []
    for ts in timestamps:
        try:
            parsed.append(datetime.fromisoformat(ts.replace("Z", "+00:00")))
        except (ValueError, TypeError):
            continue
    if not parsed:
        return ("N/A", "N/A")
    fmt = "%Y-%m-%d %H:%M"
    return (min(parsed).strftime(fmt), max(parsed).strftime(fmt))


# ── Report Formatter ───────────────────────────────────────────────

def make_bar(ratio: float) -> str:
    """Create a text bar chart segment."""
    filled = round(ratio * BAR_WIDTH)
    return BAR_FILLED * filled + BAR_EMPTY * (BAR_WIDTH - filled)


def format_report(results: list[dict]) -> str:
    """Build the full formatted report."""
    lines = []
    sep = "=" * 80
    thin_sep = "\u2500" * 80

    lines.append(sep)
    lines.append("       CLAUDE CODE SESSION ANALYSIS \u2014 Planning Patterns Report")
    lines.append(sep)
    lines.append("")

    for r in results:
        data: SessionData = r["data"]
        tools: ToolAnalysis = r["tools"]
        seq: SequenceAnalysis = r["sequence"]
        tokens: TokenUsage = r["tokens"]
        ratio = r["ratio"]
        date_start, date_end = r["date_range"]

        sid_short = data.session_id[:8] + "..."
        lines.append(f"SESSION: {data.session_id}")
        lines.append(f"  Date range    : {date_start} \u2014 {date_end}")

        total_entries = sum(data.entries_by_type.values())
        lines.append(f"  Total entries : {total_entries}")

        type_parts = [f"{k}: {v}" for k, v in data.entries_by_type.most_common()]
        lines.append(f"    {', '.join(type_parts)}")
        lines.append(f"  Human messages: {data.human_message_count}")
        lines.append(f"  Assistant turns: {data.assistant_turn_count}")
        lines.append("")

        # Tool use breakdown
        lines.append("  TOOL USE:")
        for name, count in tools.tool_counts.most_common():
            cat = "?"
            for tu in data.tool_uses:
                if tu.name == name:
                    cat = tu.category
                    break
            lines.append(f"    {name:<30s} : {count:>3d}  [{cat}]")

        lines.append(f"    {'':30s}   {'':3s}  \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500")
        lines.append(f"    {'Exploration':<30s} : {tools.exploration_count:>3d}")
        lines.append(f"    {'Implementation':<30s} : {tools.implementation_count:>3d}")
        lines.append(f"    {'Planning':<30s} : {tools.planning_count:>3d}")

        if ratio is not None:
            lines.append(f"    PLANNING RATIO: {ratio:.2f}  (higher = more exploration)")
        else:
            lines.append(f"    PLANNING RATIO: N/A  (no exploration/implementation tools)")
        lines.append("")

        # Sequence pattern
        lines.append(f"  SEQUENCE PATTERN: {seq.pattern}")
        if seq.first_exploration_idx is not None:
            first_exp_name = data.tool_uses[seq.first_exploration_idx].name
            lines.append(f"    First exploration at position {seq.first_exploration_idx} ({first_exp_name})")
        if seq.first_implementation_idx is not None:
            first_imp_name = data.tool_uses[seq.first_implementation_idx].name
            lines.append(f"    First implementation at position {seq.first_implementation_idx} ({first_imp_name})")
        lines.append("")

        # Token usage
        lines.append("  TOKEN USAGE:")
        lines.append(f"    Input tokens          : {tokens.input_tokens:>10,d}")
        lines.append(f"    Output tokens         : {tokens.output_tokens:>10,d}")
        lines.append(f"    Cache creation        : {tokens.cache_creation_tokens:>10,d}")
        lines.append(f"    Cache read            : {tokens.cache_read_tokens:>10,d}")
        lines.append(f"    Total input (w/cache) : {tokens.total_input:>10,d}")
        lines.append("")
        lines.append(thin_sep)
        lines.append("")

    # ── Aggregate Summary ──
    lines.append(sep)
    lines.append("                          AGGREGATE SUMMARY")
    lines.append(sep)
    lines.append("")
    lines.append(f"  Sessions analyzed: {len(results)}")
    lines.append("")
    lines.append("  PLANNING RATIOS:")

    for r in results:
        sid_short = r["data"].session_id[:8] + "..."
        ratio = r["ratio"]
        pattern = r["sequence"].pattern
        if ratio is not None:
            bar = make_bar(ratio)
            lines.append(f"    {sid_short:<14s} : {ratio:.2f}  {bar}  {pattern}")
        else:
            lines.append(f"    {sid_short:<14s} : N/A   {'':>{BAR_WIDTH}s}  {pattern}")

    ratios = [r["ratio"] for r in results if r["ratio"] is not None]
    if ratios:
        avg = sum(ratios) / len(ratios)
        lines.append(f"\n    Average planning ratio: {avg:.2f}")

    # Overall tool distribution
    lines.append("")
    lines.append("  OVERALL TOOL DISTRIBUTION:")
    total_tools = Counter()
    for r in results:
        total_tools += r["tools"].tool_counts
    max_count = max(total_tools.values()) if total_tools else 1
    for name, count in total_tools.most_common():
        bar = make_bar(count / max_count)
        lines.append(f"    {name:<30s} : {count:>3d}  {bar}")

    lines.append("")
    lines.append(sep)
    return "\n".join(lines)


# ── Main ───────────────────────────────────────────────────────────

def main():
    """Discover sessions, parse, analyze, and print report."""
    # Force UTF-8 output on Windows
    sys.stdout.reconfigure(encoding="utf-8")

    if not SESSION_DIR.is_dir():
        print(f"ERROR: Session directory not found: {SESSION_DIR}", file=sys.stderr)
        sys.exit(1)

    session_files = discover_sessions(SESSION_DIR)
    if not session_files:
        print("No session files found.", file=sys.stderr)
        sys.exit(1)

    results = []
    for filepath in session_files:
        data = parse_session(filepath)
        tool_analysis = analyze_tools(data)
        sequence = analyze_sequence(data)
        tokens = compute_token_usage(data)
        ratio = compute_planning_ratio(tool_analysis)
        date_range = get_date_range(data.timestamps)

        results.append({
            "data": data,
            "tools": tool_analysis,
            "sequence": sequence,
            "tokens": tokens,
            "ratio": ratio,
            "date_range": date_range,
        })

    print(format_report(results))


if __name__ == "__main__":
    main()
