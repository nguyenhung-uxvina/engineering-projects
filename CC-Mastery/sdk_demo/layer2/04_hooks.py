"""
Layer 2, Level 4: Hooks as Python Callbacks
=============================================
Run OUTSIDE Claude Code session:
    python sdk_demo/layer2/04_hooks.py

KEY CONCEPT:
    In Module 6, hooks were EXTERNAL SCRIPTS (shell/Python files).
    In the SDK, hooks are INLINE PYTHON FUNCTIONS — same events, tighter integration.

    Hook callback signature:
        async def my_hook(
            input_data: PreToolUseHookInput | PostToolUseHookInput | ...,
            tool_use_id: str | None,
            context: HookContext,
        ) -> SyncHookJSONOutput:
            ...

    Return values:
        {}                              → Allow (do nothing)
        {"decision": "block",
         "reason": "..."}              → Block the tool call
        {"hookSpecificOutput": {...}}   → Event-specific behavior

COMPARISON WITH MODULE 6:
    Module 6 (file hooks):                SDK hooks:
    - .claude/settings.json config        - options.hooks dict
    - Separate .py script files           - Inline async functions
    - stdin/stdout JSON protocol          - Typed Python objects
    - Exit code 0=allow, 2=block          - Return dict: {} or {"decision":"block"}
    - Same machine, any language          - Python only, in-process
"""

import asyncio
import sys
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    HookMatcher,
    AssistantMessage, ResultMessage,
    TextBlock, ToolUseBlock,
)
from claude_agent_sdk.types import (
    PreToolUseHookInput,
    PostToolUseHookInput,
    HookContext,
    SyncHookJSONOutput,
)

TESTBED = Path(__file__).resolve().parent.parent / "testbed"

# =============================================================================
# Hook 1: Audit Logger — log every tool call
# =============================================================================
# Equivalent to Module 6's log_bash.py but covers ALL tools

audit_log: list[str] = []


async def audit_logger(
    input_data: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext,
) -> SyncHookJSONOutput:
    """Log every tool call with timestamp."""
    ts = datetime.now().strftime("%H:%M:%S")
    tool = input_data["tool_name"]
    tool_input = input_data["tool_input"]

    if tool == "Read":
        detail = tool_input.get("file_path", "?")
    elif tool == "Edit":
        detail = tool_input.get("file_path", "?")
    elif tool == "Bash":
        detail = tool_input.get("command", "?")[:60]
    else:
        detail = str(tool_input)[:60]

    entry = f"[{ts}] {tool}: {detail}"
    audit_log.append(entry)
    print(f"  HOOK(audit): {entry}")

    # Return empty dict = allow the tool call
    return {}


# =============================================================================
# Hook 2: Block Dangerous Operations
# =============================================================================
# Equivalent to Module 6's block_commit.py but more flexible

BLOCKED_PATTERNS = [
    "rm -rf",
    "git push",
    "git reset --hard",
    "DROP TABLE",
    "format C:",
]


async def safety_guard(
    input_data: PreToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext,
) -> SyncHookJSONOutput:
    """Block dangerous bash commands."""
    if input_data["tool_name"] != "Bash":
        return {}  # Only check Bash

    command = input_data["tool_input"].get("command", "")

    for pattern in BLOCKED_PATTERNS:
        if pattern.lower() in command.lower():
            reason = f"Blocked: '{pattern}' detected in command"
            print(f"  HOOK(safety): BLOCKED — {reason}")
            return {
                "decision": "block",
                "reason": reason,
            }

    return {}


# =============================================================================
# Hook 3: Post-Tool Auditor — track what was modified
# =============================================================================

modified_files: list[str] = []


async def file_change_tracker(
    input_data: PostToolUseHookInput,
    tool_use_id: str | None,
    context: HookContext,
) -> SyncHookJSONOutput:
    """Track which files were modified after Edit/Write calls."""
    tool = input_data["tool_name"]
    if tool in ("Edit", "Write"):
        fpath = input_data["tool_input"].get("file_path", "unknown")
        modified_files.append(fpath)
        print(f"  HOOK(tracker): Modified: {fpath}")

    return {}


# =============================================================================
# Wire hooks into the SDK
# =============================================================================

async def main():
    print("=" * 60)
    print("  SDK Hooks Demo")
    print("=" * 60)
    print()

    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Edit", "Glob", "Bash"],
        permission_mode="acceptEdits",
        max_turns=8,
        max_budget_usd=0.20,
        model="sonnet",
        cwd=str(TESTBED),
        setting_sources=[],
        # --- HOOKS: inline Python callbacks ---
        hooks={
            # PreToolUse: runs BEFORE each tool call
            "PreToolUse": [
                # matcher=None means ALL tools
                HookMatcher(matcher=None, hooks=[audit_logger, safety_guard]),
            ],
            # PostToolUse: runs AFTER each tool call
            "PostToolUse": [
                # matcher matches tool names — "Edit|Write" = regex-like
                HookMatcher(matcher="Edit|Write", hooks=[file_change_tracker]),
            ],
        },
    )

    # Use ClaudeSDKClient (required for hooks)
    async with ClaudeSDKClient(options=options) as client:
        await client.query(
            "Read utils.py and add a type hint to the 'add' function. "
            "Change 'def add(a, b):' to 'def add(a: int, b: int) -> int:'"
        )

        async for msg in client.receive_response():
            if isinstance(msg, AssistantMessage):
                for block in msg.content:
                    if isinstance(block, TextBlock):
                        print(f"\n  Agent: {block.text[:200]}")
                    elif isinstance(block, ToolUseBlock):
                        pass  # Hooks already print this
            elif isinstance(msg, ResultMessage):
                print(f"\n  [done: ${msg.total_cost_usd or 0:.4f}]")

    # --- Report ---
    print(f"\n{'='*60}")
    print(f"  HOOK REPORT")
    print(f"{'='*60}")
    print(f"\n  Audit log ({len(audit_log)} entries):")
    for entry in audit_log:
        print(f"    {entry}")

    print(f"\n  Modified files ({len(modified_files)}):")
    for f in modified_files:
        print(f"    {f}")

    print(f"""
{'='*60}
  KEY DIFFERENCES: File Hooks vs SDK Hooks
{'='*60}
  File hooks (Module 6):         SDK hooks (this demo):
  ─────────────────────          ──────────────────────
  settings.json config           options.hooks dict
  Separate .py files             Inline async functions
  JSON via stdin/stdout          Typed Python dicts
  exit(2) to block               {{"decision": "block"}}
  Any language (Python/bash)     Python only
  Runs as subprocess             Runs in-process (faster)
  Works in interactive CC        Works ONLY with SDK
  Shared state = files           Shared state = variables!

  The biggest win: SDK hooks share memory with your app.
  audit_log and modified_files are regular Python lists —
  no file I/O, no JSON parsing, no subprocess overhead.
""")


if __name__ == "__main__":
    asyncio.run(main())
