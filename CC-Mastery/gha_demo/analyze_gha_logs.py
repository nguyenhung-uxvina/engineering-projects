"""
analyze_gha_logs.py — The "Power Move" from Module 11
=====================================================

Queries recent Claude Code GitHub Action runs, extracts patterns from
agent behavior, and suggests CLAUDE.md improvements.

Usage:
    # List recent Claude runs (last 5 days)
    python analyze_gha_logs.py --repo owner/repo --since 5d

    # Analyze and suggest CLAUDE.md fixes
    python analyze_gha_logs.py --repo owner/repo --since 5d --analyze

    # Pipe to Claude for auto-fix (the ultimate power move)
    python analyze_gha_logs.py --repo owner/repo --since 5d --analyze | \
        claude -p "Read these agent mistakes and fix CLAUDE.md to prevent them. Put up a PR."

Requirements:
    - gh CLI installed and authenticated
    - Python 3.10+
"""

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone


@dataclass
class RunSummary:
    """Summary of a single GHA run."""
    run_id: int
    status: str
    conclusion: str
    created_at: str
    duration_seconds: int
    trigger_event: str
    trigger_actor: str
    branch: str
    url: str
    errors: list[str] = field(default_factory=list)
    tool_calls: list[str] = field(default_factory=list)
    retries: int = 0


def parse_since(since_str: str) -> datetime:
    """Parse '5d', '12h', '1w' into a datetime."""
    unit = since_str[-1]
    value = int(since_str[:-1])
    now = datetime.now(timezone.utc)
    if unit == 'd':
        return now - timedelta(days=value)
    elif unit == 'h':
        return now - timedelta(hours=value)
    elif unit == 'w':
        return now - timedelta(weeks=value)
    else:
        raise ValueError(f"Unknown time unit: {unit}. Use d/h/w.")


def gh_api(endpoint: str) -> dict | list:
    """Call GitHub API via gh CLI."""
    result = subprocess.run(
        ["gh", "api", endpoint, "--paginate"],
        capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        print(f"Error calling gh api {endpoint}: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def get_claude_runs(repo: str, since: datetime) -> list[dict]:
    """Fetch Claude Code Action workflow runs since a given date."""
    since_iso = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    # List workflows to find Claude ones
    workflows = gh_api(f"/repos/{repo}/actions/workflows")
    claude_workflow_ids = []
    for wf in workflows.get("workflows", []):
        name_lower = wf["name"].lower()
        if "claude" in name_lower:
            claude_workflow_ids.append(wf["id"])

    if not claude_workflow_ids:
        print("No Claude Code workflows found in this repo.", file=sys.stderr)
        print("Tip: Ensure your workflow name contains 'claude'.", file=sys.stderr)
        return []

    all_runs = []
    for wf_id in claude_workflow_ids:
        data = gh_api(
            f"/repos/{repo}/actions/workflows/{wf_id}/runs"
            f"?created=%3E{since_iso}&per_page=100"
        )
        all_runs.extend(data.get("workflow_runs", []))

    return sorted(all_runs, key=lambda r: r["created_at"], reverse=True)


def get_job_logs(repo: str, run_id: int) -> str:
    """Download logs for a specific run's jobs."""
    jobs_data = gh_api(f"/repos/{repo}/actions/runs/{run_id}/jobs")
    logs = []
    for job in jobs_data.get("jobs", []):
        job_id = job["id"]
        result = subprocess.run(
            ["gh", "api", f"/repos/{repo}/actions/jobs/{job_id}/logs"],
            capture_output=True, text=True, encoding="utf-8"
        )
        if result.returncode == 0:
            logs.append(result.stdout)
    return "\n".join(logs)


# ── Pattern Detection ───────────────────────────────────────────────────

ERROR_PATTERNS = [
    (r"(?i)error:?\s+(.+)", "error"),
    (r"(?i)permission denied", "permission_denied"),
    (r"(?i)tool .+ not allowed", "tool_blocked"),
    (r"(?i)max.?turns? (?:reached|exceeded|limit)", "max_turns_hit"),
    (r"(?i)rate limit", "rate_limited"),
    (r"(?i)timeout", "timeout"),
    (r"(?i)ENOENT|file not found|No such file", "file_not_found"),
    (r"(?i)command failed|exit code [1-9]", "command_failed"),
    (r"(?i)merge conflict", "merge_conflict"),
    (r"(?i)tests? fail", "test_failure"),
]

TOOL_PATTERN = re.compile(r"Tool(?:Use|Call):\s*(\w+)")
RETRY_PATTERN = re.compile(r"(?i)retr(?:y|ying|ied)")


def analyze_log(log_text: str) -> tuple[list[str], list[str], int]:
    """Extract errors, tool calls, and retry count from log text."""
    errors = []
    for pattern, label in ERROR_PATTERNS:
        matches = re.findall(pattern, log_text)
        if matches:
            if isinstance(matches[0], tuple):
                errors.extend(f"{label}: {m[0][:100]}" for m in matches[:3])
            else:
                errors.append(label)

    tools = TOOL_PATTERN.findall(log_text)
    retries = len(RETRY_PATTERN.findall(log_text))

    return errors, tools, retries


def summarize_runs(repo: str, runs: list[dict], fetch_logs: bool = False) -> list[RunSummary]:
    """Build summaries for each run, optionally fetching logs."""
    summaries = []
    for run in runs:
        created = datetime.fromisoformat(run["created_at"].replace("Z", "+00:00"))
        updated = datetime.fromisoformat(run["updated_at"].replace("Z", "+00:00"))
        duration = int((updated - created).total_seconds())

        summary = RunSummary(
            run_id=run["id"],
            status=run["status"],
            conclusion=run.get("conclusion", "in_progress"),
            created_at=run["created_at"],
            duration_seconds=duration,
            trigger_event=run["event"],
            trigger_actor=run.get("triggering_actor", {}).get("login", "unknown"),
            branch=run.get("head_branch", "unknown"),
            url=run["html_url"],
        )

        if fetch_logs and run["status"] == "completed":
            log_text = get_job_logs(repo, run["id"])
            summary.errors, summary.tool_calls, summary.retries = analyze_log(log_text)

        summaries.append(summary)

    return summaries


# ── Report Generation ───────────────────────────────────────────────────

def print_overview(summaries: list[RunSummary]) -> None:
    """Print run overview table."""
    print(f"\n{'='*80}")
    print(f"  Claude Code GHA Runs ({len(summaries)} total)")
    print(f"{'='*80}\n")

    conclusions = Counter(s.conclusion for s in summaries)
    print(f"  Success: {conclusions.get('success', 0)}  "
          f"Failure: {conclusions.get('failure', 0)}  "
          f"Cancelled: {conclusions.get('cancelled', 0)}  "
          f"In-progress: {conclusions.get('in_progress', 0)}")
    print()

    print(f"  {'Run ID':<12} {'Status':<12} {'Duration':<10} {'Event':<18} {'Actor':<15}")
    print(f"  {'-'*12} {'-'*12} {'-'*10} {'-'*18} {'-'*15}")
    for s in summaries:
        mins = s.duration_seconds // 60
        secs = s.duration_seconds % 60
        print(f"  {s.run_id:<12} {s.conclusion:<12} {mins:>2}m {secs:02d}s     "
              f"{s.trigger_event:<18} {s.trigger_actor:<15}")


def print_analysis(summaries: list[RunSummary]) -> None:
    """Print detailed analysis with pattern detection."""
    print(f"\n{'='*80}")
    print(f"  Pattern Analysis")
    print(f"{'='*80}\n")

    # Error frequency
    all_errors = []
    for s in summaries:
        all_errors.extend(s.errors)
    error_counts = Counter(e.split(":")[0] for e in all_errors)

    if error_counts:
        print("  Top Error Patterns:")
        for err, count in error_counts.most_common(10):
            bar = "#" * min(count, 30)
            print(f"    {err:<25} {count:>3}x  {bar}")
    else:
        print("  No errors detected in analyzed runs.")

    # Tool usage
    all_tools = []
    for s in summaries:
        all_tools.extend(s.tool_calls)
    tool_counts = Counter(all_tools)

    if tool_counts:
        print(f"\n  Top Tool Usage:")
        for tool, count in tool_counts.most_common(10):
            bar = "#" * min(count, 30)
            print(f"    {tool:<25} {count:>3}x  {bar}")

    # Retry analysis
    retry_runs = [s for s in summaries if s.retries > 0]
    if retry_runs:
        print(f"\n  Runs with retries: {len(retry_runs)}/{len(summaries)}")
        for s in retry_runs:
            print(f"    Run {s.run_id}: {s.retries} retries — {s.url}")

    # Duration analysis
    completed = [s for s in summaries if s.conclusion == "success"]
    if completed:
        durations = [s.duration_seconds for s in completed]
        avg = sum(durations) / len(durations)
        print(f"\n  Duration (successful runs):")
        print(f"    Average: {avg/60:.1f}min  "
              f"Min: {min(durations)/60:.1f}min  "
              f"Max: {max(durations)/60:.1f}min")

    # Failure details
    failed = [s for s in summaries if s.conclusion == "failure"]
    if failed:
        print(f"\n  Failed Runs ({len(failed)}):")
        for s in failed:
            print(f"    Run {s.run_id} ({s.trigger_event} by {s.trigger_actor})")
            for err in s.errors[:3]:
                print(f"      - {err}")
            print(f"      URL: {s.url}")


def suggest_claude_md_fixes(summaries: list[RunSummary]) -> None:
    """Generate CLAUDE.md improvement suggestions based on patterns."""
    print(f"\n{'='*80}")
    print(f"  Suggested CLAUDE.md Improvements")
    print(f"{'='*80}\n")

    all_errors = []
    for s in summaries:
        all_errors.extend(s.errors)
    error_types = Counter(e.split(":")[0] for e in all_errors)

    suggestions = []

    if error_types.get("file_not_found", 0) > 2:
        suggestions.append(
            "Add file path conventions to CLAUDE.md:\n"
            '  "Source files are in src/, tests in tests/. '
            'Always verify paths with Glob before editing."'
        )

    if error_types.get("test_failure", 0) > 2:
        suggestions.append(
            "Add testing protocol to CLAUDE.md:\n"
            '  "Always run tests before committing. Command: npm test (or pytest).\n'
            '   If tests fail, fix the issue before retrying the commit."'
        )

    if error_types.get("tool_blocked", 0) > 2:
        suggestions.append(
            "Review --allowedTools in your workflow. Blocked tools mean Claude tried "
            "something it shouldn't. Either:\n"
            "  a) Expand the allowlist if the tool is safe\n"
            "  b) Add to CLAUDE.md: 'Do not use <tool> for <reason>'"
        )

    if error_types.get("max_turns_hit", 0) > 1:
        suggestions.append(
            "Claude is hitting --max-turns too often. Either:\n"
            "  a) Increase max-turns for complex tasks\n"
            "  b) Add to CLAUDE.md: 'Break large changes into smaller PRs.\n"
            "     If a task needs >15 turns, create an issue for the remaining work.'"
        )

    if error_types.get("merge_conflict", 0) > 1:
        suggestions.append(
            "Add merge strategy to CLAUDE.md:\n"
            '  "Before starting work, pull the latest base branch.\n'
            '   If merge conflicts occur, resolve them conservatively — prefer the base branch."'
        )

    retry_count = sum(s.retries for s in summaries)
    if retry_count > 5:
        suggestions.append(
            "High retry count suggests Claude is brute-forcing failures.\n"
            "Add to CLAUDE.md:\n"
            '  "If an approach fails twice, stop and try a different strategy.\n'
            '   Do not retry the same action more than once."'
        )

    if not suggestions:
        suggestions.append("No recurring patterns detected. Your CLAUDE.md is working well!")

    for i, s in enumerate(suggestions, 1):
        print(f"  {i}. {s}\n")


# ── Main ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Analyze Claude Code GitHub Action runs for patterns"
    )
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument("--since", default="7d", help="Time window: 5d, 12h, 1w (default: 7d)")
    parser.add_argument("--analyze", action="store_true", help="Fetch logs and analyze patterns")
    parser.add_argument("--json", action="store_true", help="Output as JSON (for piping)")

    args = parser.parse_args()
    since = parse_since(args.since)

    print(f"Fetching Claude runs for {args.repo} since {since.strftime('%Y-%m-%d %H:%M UTC')}...")
    runs = get_claude_runs(args.repo, since)

    if not runs:
        print("No Claude Code runs found in the specified time window.")
        return

    summaries = summarize_runs(args.repo, runs, fetch_logs=args.analyze)

    if args.json:
        output = {
            "repo": args.repo,
            "since": since.isoformat(),
            "total_runs": len(summaries),
            "runs": [
                {
                    "run_id": s.run_id,
                    "conclusion": s.conclusion,
                    "duration_seconds": s.duration_seconds,
                    "trigger_event": s.trigger_event,
                    "trigger_actor": s.trigger_actor,
                    "errors": s.errors,
                    "retries": s.retries,
                    "url": s.url,
                }
                for s in summaries
            ],
        }
        print(json.dumps(output, indent=2))
        return

    print_overview(summaries)

    if args.analyze:
        print_analysis(summaries)
        suggest_claude_md_fixes(summaries)
        print(f"\n  {'='*80}")
        print(f"  The Ultimate Power Move:")
        print(f"  {'='*80}")
        print(f"  python analyze_gha_logs.py --repo {args.repo} --since {args.since} --analyze | \\")
        print(f'    claude -p "Read these agent mistakes and fix CLAUDE.md. Put up a PR."')
        print()


if __name__ == "__main__":
    main()
