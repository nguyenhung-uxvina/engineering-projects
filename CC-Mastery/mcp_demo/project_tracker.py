"""
Project Phase Tracker — MCP Server Demo

A minimal MCP server that manages engineering project state.
Demonstrates why MCP is needed: stateful phase transitions with validation.

Three tools mapping to the curriculum's three-tool pattern:
  1. get_projects()       → download_raw_data (read current state)
  2. update_phase()       → take_sensitive_gated_action (controlled mutation)
  3. run_gate_check()     → execute_code_in_environment (validation logic)

Usage:
  Register in Claude Code settings as an MCP server (stdio transport).
"""

from mcp.server.fastmcp import FastMCP

# --- Server ---
mcp = FastMCP(
    "project-tracker",
    instructions=(
        "Engineering project phase tracker. Use get_projects to see current state, "
        "run_gate_check before advancing phases, update_phase to transition."
    ),
)

# --- In-memory state (this is why it's an MCP, not a script) ---
VALID_PHASES = ["Phase 0: ODI", "Phase 1: Clarification", "Phase 2: Conceptual",
                "Phase 3: Embodiment", "Phase 4: Detail", "Closed"]

PROJECTS: dict[str, dict] = {
    "VN-UAS-001": {
        "name": "Reconnaissance UAV Gimbal",
        "phase": "Phase 1: Clarification",
        "requirements_count": 45,
        "quantified_pct": 62,
        "local_content_pct": 0,
        "notes": "Initial requirements gathering in progress",
    },
    "VN-RWS-002": {
        "name": "Remote Weapon Station",
        "phase": "Phase 2: Conceptual",
        "requirements_count": 128,
        "quantified_pct": 85,
        "local_content_pct": 55,
        "notes": "3 concepts under evaluation via VDI 2225",
    },
}


# --- Tool 1: Read (stateless-looking, but reads session state) ---
@mcp.tool()
def get_projects(project_id: str | None = None) -> str:
    """Get current project status. Returns all projects if no ID given, or a specific project by ID."""
    if project_id:
        proj = PROJECTS.get(project_id)
        if not proj:
            return f"Project {project_id} not found. Known projects: {', '.join(PROJECTS.keys())}"
        return _format_project(project_id, proj)

    if not PROJECTS:
        return "No projects tracked. Use update_phase to add a project."

    lines = [f"## Tracked Projects ({len(PROJECTS)})\n"]
    for pid, proj in PROJECTS.items():
        lines.append(_format_project(pid, proj))
    return "\n---\n".join(lines)


# --- Tool 2: Controlled Mutation (the security gate) ---
@mcp.tool()
def update_phase(project_id: str, target_phase: str, notes: str = "") -> str:
    """Advance a project to the next phase. Enforces sequential phase transitions — cannot skip phases.
    Use run_gate_check first to verify readiness."""
    if target_phase not in VALID_PHASES:
        return f"Invalid phase '{target_phase}'. Valid phases: {', '.join(VALID_PHASES)}"

    proj = PROJECTS.get(project_id)
    if not proj:
        return f"Project {project_id} not found. Known projects: {', '.join(PROJECTS.keys())}"

    current_idx = VALID_PHASES.index(proj["phase"])
    target_idx = VALID_PHASES.index(target_phase)

    # Enforce sequential progression
    if target_idx != current_idx + 1:
        if target_idx <= current_idx:
            return f"Cannot move backward. Current: {proj['phase']}, requested: {target_phase}"
        skipped = VALID_PHASES[current_idx + 1:target_idx]
        return f"Cannot skip phases. Current: {proj['phase']}. Must pass through: {', '.join(skipped)}"

    # Apply transition
    old_phase = proj["phase"]
    proj["phase"] = target_phase
    if notes:
        proj["notes"] = notes

    return f"Project {project_id} transitioned: {old_phase} -> {target_phase}"


# --- Tool 3: Validation Logic (execute against current state) ---
@mcp.tool()
def run_gate_check(project_id: str) -> str:
    """Run gate review checks for a project's current phase. Reports pass/fail for each criterion."""
    proj = PROJECTS.get(project_id)
    if not proj:
        return f"Project {project_id} not found. Known projects: {', '.join(PROJECTS.keys())}"

    phase = proj["phase"]
    checks = []

    if phase == "Phase 1: Clarification":
        checks = [
            ("Requirements >= 50", proj["requirements_count"] >= 50),
            ("Quantified >= 80%", proj["quantified_pct"] >= 80),
            ("No unresolved conflicts", True),  # simplified
        ]
    elif phase == "Phase 2: Conceptual":
        checks = [
            ("Requirements >= 100", proj["requirements_count"] >= 100),
            ("Quantified >= 80%", proj["quantified_pct"] >= 80),
            ("Local content >= 60%", proj["local_content_pct"] >= 60),
            ("VDI 2225 score >= 70%", True),  # simplified
        ]
    elif phase == "Phase 3: Embodiment":
        checks = [
            ("Layout finalized", True),  # simplified
            ("DfX review passed", True),
            ("Local content >= 60%", proj["local_content_pct"] >= 60),
            ("Cost on target", True),
        ]
    else:
        return f"No gate check defined for {phase}."

    lines = [f"## Gate Check: {project_id} ({phase})\n"]
    all_pass = True
    for name, passed in checks:
        status = "[PASS]" if passed else "[FAIL]"
        if not passed:
            all_pass = False
        lines.append(f"  {status} {name}")

    lines.append(f"\n**Result: {'READY to advance' if all_pass else 'NOT READY — fix failures before advancing'}**")
    return "\n".join(lines)


def _format_project(pid: str, proj: dict) -> str:
    return (
        f"**{pid}**: {proj['name']}\n"
        f"  Phase: {proj['phase']}\n"
        f"  Requirements: {proj['requirements_count']} ({proj['quantified_pct']}% quantified)\n"
        f"  Local content: {proj['local_content_pct']}%\n"
        f"  Notes: {proj['notes']}"
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
