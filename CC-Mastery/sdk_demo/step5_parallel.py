"""
Step 5: Parallel Fan-Out / Fan-In
===================================
Run OUTSIDE Claude Code session:
  python sdk_demo/step5_parallel.py

Demonstrates:
  - asyncio.Semaphore for bounded concurrency
  - Multiple query() calls in parallel
  - Fan-out (dispatch) → Fan-in (collect results)
  - Cost aggregation across parallel tasks

Key insight: Each query() spawns a separate Claude Code process.
The semaphore prevents overwhelming your machine / API limits.
"""

import asyncio
import time
from pathlib import Path

from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    ResultMessage,
)

TESTBED = Path(__file__).parent / "testbed"


# =============================================================================
# Fan-Out: Process one file
# =============================================================================

async def process_file(filepath: Path, semaphore: asyncio.Semaphore) -> dict:
    """Process a single file with bounded concurrency."""
    async with semaphore:  # Wait if too many concurrent tasks
        print(f"  [{filepath.name}] Starting...")
        start = time.time()

        result_data = {
            "file": filepath.name,
            "status": "error",
            "cost": 0.0,
            "duration": 0.0,
            "summary": "",
        }

        try:
            async for msg in query(
                prompt=(
                    f"Read {filepath} and add a module-level docstring "
                    f"explaining what the file contains. "
                    f"Don't change any existing code, just add the docstring at the top."
                ),
                options=ClaudeAgentOptions(
                    allowed_tools=["Read", "Edit"],
                    permission_mode="acceptEdits",
                    max_turns=3,
                    max_budget_usd=0.10,
                    model="sonnet",
                    cwd=str(filepath.parent),
                    setting_sources=[],
                ),
            ):
                if isinstance(msg, ResultMessage):
                    result_data["status"] = msg.subtype
                    result_data["cost"] = msg.total_cost_usd or 0.0
                    result_data["summary"] = (msg.result or "")[:100]

        except Exception as e:
            result_data["status"] = f"exception: {e}"

        result_data["duration"] = time.time() - start
        print(f"  [{filepath.name}] Done in {result_data['duration']:.1f}s "
              f"(${result_data['cost']:.4f})")
        return result_data


# =============================================================================
# Fan-In: Collect and summarize results
# =============================================================================

async def main():
    print("=== Parallel Processing Demo ===\n")

    files = sorted(TESTBED.glob("*.py"))
    print(f"Files to process: {[f.name for f in files]}")
    print()

    # --- KEY PATTERN: Bounded concurrency with Semaphore ---
    # Set to 2 to avoid overwhelming the API
    # In production, tune based on rate limits
    CONCURRENCY = 2
    semaphore = asyncio.Semaphore(CONCURRENCY)

    print(f"Concurrency: {CONCURRENCY} parallel tasks\n")

    # Fan-out: dispatch all tasks
    start_total = time.time()
    tasks = [process_file(f, semaphore) for f in files]

    # Fan-in: collect results (asyncio.gather runs them concurrently)
    results = await asyncio.gather(*tasks)

    total_time = time.time() - start_total
    total_cost = sum(r["cost"] for r in results)

    # --- Summary ---
    print(f"\n{'='*50}")
    print(f"RESULTS")
    print(f"{'='*50}")

    for r in results:
        status_icon = "ok" if r["status"] == "success" else "FAIL"
        print(f"  [{status_icon}] {r['file']:15s} "
              f"${r['cost']:.4f}  {r['duration']:.1f}s")

    print(f"\n  Total: ${total_cost:.4f} in {total_time:.1f}s")
    print(f"  Files: {len(results)} processed, "
          f"{sum(1 for r in results if r['status']=='success')} succeeded")

    # Sequential would take: sum of all durations
    seq_time = sum(r["duration"] for r in results)
    speedup = seq_time / total_time if total_time > 0 else 0
    print(f"  Speedup: {speedup:.1f}x vs sequential ({seq_time:.1f}s)")


if __name__ == "__main__":
    asyncio.run(main())
