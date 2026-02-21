"""
VN-RANGE-001 Deployment Pipeline — SDK Implementation
======================================================
Framework:  Skill 4 (Process Automation Design) × Module 10 (Claude Agent SDK)
Pattern:    Master-Clone (Module 7) with Automation Gradient
Product:    IRONMESH RANGE Smart Range System

Usage:
    python sdk_pipeline_VN-RANGE-001.py --phase 1
    python sdk_pipeline_VN-RANGE-001.py --phase 2 --input requirements_VN-RANGE-001.md
    python sdk_pipeline_VN-RANGE-001.py --phase 3 --input architecture_review_VN-RANGE-001.md

Architecture:
    Master orchestrator (this script) runs in main process.
    Low-consequence tasks → delegated to query() calls (Task equivalent).
    High-consequence steps → human HITL, no AI delegation.
    Safety-critical → 0% automation, logs only.
"""

import asyncio
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Windows UTF-8 fix (Module 4 lesson: sys.stdout.reconfigure for Windows encoding)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolUseBlock,
)

# ─── Automation Gradient: Phase → consequence level → automation %
PHASE_CONFIG = {
    1: {
        "name": "Requirements Generation",
        "consequence": "LOW",
        "automation_pct": 90,
        "hitl_required": False,  # AI drafts, human reviews at end
        "output_file": "requirements_VN-RANGE-001.md",
        "allowed_tools": ["Read", "Write", "Glob"],
    },
    2: {
        "name": "Architecture Review",
        "consequence": "MEDIUM",
        "automation_pct": 70,
        "hitl_required": True,   # Always pause for Gate 2 review
        "output_file": "architecture_review_VN-RANGE-001.md",
        "allowed_tools": ["Read", "Write"],
    },
    3: {
        "name": "Integration Design",
        "consequence": "MEDIUM",
        "automation_pct": 75,
        "hitl_required": True,   # RSO sign-off required
        "output_file": "integration_design_VN-RANGE-001.md",
        "allowed_tools": ["Read", "Write"],
    },
    4: {
        "name": "DfX Gate Review",
        "consequence": "HIGH",
        "automation_pct": 50,
        "hitl_required": True,   # Intensive human review
        "output_file": "dfx_gate_review_VN-RANGE-001.md",
        "allowed_tools": ["Read", "Write"],
    },
    5: {
        "name": "Safety Validation",
        "consequence": "CRITICAL",
        "automation_pct": 0,     # 0% — human-led only
        "hitl_required": True,
        "output_file": "safety_validation_VN-RANGE-001.md",
        "allowed_tools": [],     # No tools — logging only
    },
}

# ─── Task prompts per phase (scoped, no context bloat)
PHASE_PROMPTS = {
    1: """
You are a defense systems requirements writer for IRONMESH RANGE (VN-RANGE-001).

Generate a quantified requirements specification covering:
1. Functional requirements (acoustic sensing, vision scoring, training analytics, data fusion)
2. Performance requirements (detection accuracy ≥95%, latency <100ms, availability ≥99%)
3. Environmental requirements (IP67, maritime salt spray, temperature -10°C to +55°C)
4. Integration requirements (existing range infrastructure, Vietnamese power grid 220V/50Hz)
5. Safety requirements (TCVN compliance, fail-safe modes, RSO override capability)
6. Local content requirements (≥60% by value, Vietnamese supplier preference)

FORMAT: Numbered requirements, each QUANTIFIED with measurable target.
Vague requirements are NOT acceptable. Ask "what number?" for anything unmeasured.

Write the output to: requirements_VN-RANGE-001.md
""",

    2: """
You are a defense systems architect reviewing IRONMESH RANGE (VN-RANGE-001).

Read: requirements_VN-RANGE-001.md

Validate the requirements against:
- DfX Corrosion: maritime environment, salt spray, humidity
- DfX Thermal: temperature cycling, heat dissipation
- DfX Maintainability: field service by Vietnamese technicians, spare parts availability
- DfX Reliability: MTBF targets, redundancy requirements
- Gate 2 checklist: ≥80% requirements quantified, no conflicts, stakeholder coverage

For each check: ✅ (pass) or ❌ (fail with specific issue and recommended fix)

Calculate readiness score: (passed items / total items) × 100
IF readiness < 70: Stop and output HALT recommendation with specific gaps.

Write to: architecture_review_VN-RANGE-001.md
""",

    3: """
You are an integration engineer designing IRONMESH RANGE commissioning for VN-RANGE-001.

Read: requirements_VN-RANGE-001.md AND architecture_review_VN-RANGE-001.md

Design:
1. Physical integration map (sensor placement, cable routing, power distribution) — ASCII diagram
2. Software integration sequence: CORTEX → VN-LOMAH → VN-CAM → VN-TRN (step by step)
3. Data flow diagram showing multi-agent orchestration (ASCII)
4. Commissioning sequence table: Step | Who | Automation | Consequence | Fallback
5. Fallback protocols for each component failure mode

AUTOMATION GRADIENT — label each commissioning step:
  [AI-ASSIST]: consequence LOW → 90% automated
  [SEMI-AUTO]: consequence MEDIUM → AI prepares, human confirms
  [HUMAN-LED]: consequence HIGH → human primary, AI supports
  [HUMAN-ONLY]: consequence CRITICAL → AI observes/logs only, no delegation

Write to: integration_design_VN-RANGE-001.md
""",

    4: """
You are a DfX reviewer for VN-RANGE-001 Gate 3 (Embodiment → Detail Design transition).

Read ALL prior outputs:
- requirements_VN-RANGE-001.md
- architecture_review_VN-RANGE-001.md
- integration_design_VN-RANGE-001.md

Conduct DfX Gate Review across all 12 categories:
1. DfM (Manufacturability) — Can Workshop X produce this locally?
2. DfA (Assembly) — Assembly sequence feasible with Vietnamese labor?
3. DfT (Testing) — Test procedures defined for all subsystems?
4. DfR (Reliability) — MTBF meets military requirements?
5. DfMaint (Maintainability) — Field service by Vietnamese technicians?
6. DfCorrosion — Marine environment protection adequate?
7. DfThermal — Temperature management for Vietnam's climate?
8. DfLogistics — Supply chain for all components in Vietnam?
9. DfDisposal — End-of-life handling compliant with regulations?
10. DfHuman — Interface suitable for Vietnamese military operators?
11. DfSafety — All safety interlocks designed and documented?
12. DfCost — ≤70% of import equivalent on target?

For each: Score 1-5, Rationale, Action Required (if score <4)

Overall Gate Score: (sum of scores / 60) × 100
IF overall score < 70: REJECT with specific remediation plan.

Write to: dfx_gate_review_VN-RANGE-001.md
""",
}


async def run_phase(phase: int, input_file: str | None = None) -> bool:
    """
    Master orchestrator: runs one pipeline phase.
    Returns True if phase completes successfully, False if HALT or failure.
    """
    config = PHASE_CONFIG[phase]
    print(f"\n{'='*60}")
    print(f"PHASE {phase}: {config['name']}")
    print(f"Consequence: {config['consequence']} | Automation: {config['automation_pct']}%")
    print(f"{'='*60}")

    # ─── Safety: Phase 5 is always 0% automated
    if config["automation_pct"] == 0:
        print("\n⚠️  SAFETY VALIDATION (Phase 5)")
        print("This phase is 0% automated. Human-led only.")
        print("AI role: Documentation and record-keeping only.")
        print(f"\nPlease complete safety validation manually and document in:")
        print(f"  {config['output_file']}")
        return True

    # ─── Check preconditions
    if input_file and not Path(input_file).exists():
        print(f"\n❌ INPUT FILE NOT FOUND: {input_file}")
        print("Cannot proceed without prior phase output.")
        return False

    # ─── Inject input file context into prompt if provided
    prompt = PHASE_PROMPTS[phase]
    if input_file:
        prompt = f"Prior phase input file: {input_file}\n\n" + prompt

    # ─── Run the delegated Task (master-clone pattern)
    print(f"\n🤖 Running AI delegation ({config['automation_pct']}% automated)...")
    print(f"   Output: {config['output_file']}")
    print(f"   Tools: {config['allowed_tools'] or 'None (human-led)'}\n")

    options = ClaudeAgentOptions(
        allowed_tools=config["allowed_tools"] if config["allowed_tools"] else None,
        max_turns=15,  # Prevent runaway — defense tasks are bounded
        permission_mode="acceptEdits",
        system_prompt=f"""
You are operating within the VN-RANGE-001 deployment pipeline, Phase {phase}.
Consequence level: {config['consequence']}
Automation target: {config['automation_pct']}%

CRITICAL RULES:
1. Never proceed if safety-critical issue detected — output HALT recommendation
2. Quantify everything — vague outputs are not acceptable
3. Use TCVN standards for Vietnamese military compliance
4. Flag Vietnamese supplier gaps immediately (local content ≥60%)
5. Output ONLY to the specified file, no other files
""",
        cwd=str(Path.cwd()),
        setting_sources=[],  # Isolated task — don't load project CLAUDE.md hooks
    )

    output_lines = []
    turn_count = 0
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, SystemMessage):
            print(f"   [Session: {message.session_id[:8]}...]")
        elif isinstance(message, AssistantMessage):
            turn_count += 1
            print(f"   [Turn {turn_count}]", end=" ")
            for block in message.content:
                if isinstance(block, TextBlock):
                    # Show just the first line as progress indicator
                    first_line = block.text.strip().split('\n')[0][:80]
                    print(first_line)
                    output_lines.append(block.text)
                elif isinstance(block, ToolUseBlock):
                    print(f"→ {block.name}({getattr(block, 'input', {}).get('file_path', getattr(block, 'input', {}).get('path', '...')[:40])})")
        elif isinstance(message, ResultMessage):
            print(f"\n   Cost: ${message.cost_usd:.4f} | Turns: {message.num_turns}")

    print("✅ AI delegation complete.")

    # ─── Skill 3 QC Validation (automated checks before HITL)
    qc_verdict, qc_detail = validate_phase_output(phase, config["output_file"])
    qc_icons = {"PASS": "OK ", "WARN": "!! ", "FAIL": "XX ", "SKIP": "-- "}
    print(f"\n   [QC] {qc_icons.get(qc_verdict, '   ')} {qc_verdict}: {qc_detail}")
    if qc_verdict == "FAIL":
        print("   [QC] FAIL blocks APPROVE — you must REVISE or CANCEL")
    # Collect evidence files for audit trail (this phase output + any input)
    evidence_files = [config["output_file"]]
    if input_file and Path(input_file).exists():
        evidence_files.append(input_file)

    log_decision(phase, f"QC_{qc_verdict}", config, rationale=qc_detail,
                 evidence_files=evidence_files)

    # ─── HITL Checkpoint (always if hitl_required)
    if config["hitl_required"] or qc_verdict in ("FAIL", "WARN"):
        print(f"\n{'─'*60}")
        print(f"HITL CHECKPOINT — Phase {phase} Complete")
        print(f"   Output:     {config['output_file']}")
        print(f"   QC Verdict: {qc_verdict} — {qc_detail}")
        print(f"   Authority:  {PHASE_AUTHORITY.get(phase, 'OPERATIONAL')}")
        print(f"\n   Please review the output, then choose:")
        if qc_verdict == "FAIL":
            print("   A) ✅ APPROVE — NOT AVAILABLE (QC FAIL must be resolved first)")
        else:
            print("   A) ✅ APPROVE — Proceed to next phase")
        print("   B) 🔄 REVISE — Re-run this phase with adjustments")
        print("   C) ⏸️  PAUSE — Stop here, resume later")
        print("   D) ❌ CANCEL — Halt pipeline")
        print(f"{'─'*60}")

        decision = input("\nYour decision (A/B/C/D): ").strip().upper()

        # Governance §6: reject empty approvals — require rationale
        rationale = ""
        if decision in ("A", "B", "D"):
            rationale = input("Rationale (required — why this decision?): ").strip()
            if not rationale:
                print("⚠️  Empty rationale not accepted (governance §6). Please provide reason.")
                rationale = input("Rationale: ").strip()

        if decision == "A":
            if qc_verdict == "FAIL":
                print("Cannot APPROVE — QC validation failed. Choose B (Revise) or D (Cancel).")
                decision = input("Your decision (B/C/D): ").strip().upper()
                if decision == "B":
                    log_decision(phase, "REVISE_AFTER_QC_FAIL", config,
                                 rationale=rationale, evidence_files=evidence_files)
                    return False
                log_decision(phase, "CANCELLED_AFTER_QC_FAIL", config,
                             rationale=rationale, evidence_files=evidence_files)
                sys.exit(1)
            print("✅ Approved. Phase complete.")
            log_decision(phase, "APPROVED", config,
                         rationale=rationale, evidence_files=evidence_files)
            return True
        elif decision == "B":
            print("🔄 Revision requested. Re-run with adjusted parameters.")
            log_decision(phase, "REVISE", config,
                         rationale=rationale, evidence_files=evidence_files)
            return False
        elif decision == "C":
            print("⏸️  Pipeline paused. Resume with --phase to continue.")
            log_decision(phase, "PAUSED", config, evidence_files=evidence_files)
            sys.exit(0)
        elif decision == "D":
            print("❌ Pipeline cancelled.")
            log_decision(phase, "CANCELLED", config,
                         rationale=rationale, evidence_files=evidence_files)
            sys.exit(1)
        else:
            print("⚠️  Invalid input. Treating as PAUSE.")
            sys.exit(0)

    return True


def _last_record_hash(log_path: Path) -> str:
    """Read the last line of the audit log and return its SHA-256 hash for chain integrity."""
    if not log_path.exists():
        return "GENESIS"
    lines = log_path.read_text(encoding="utf-8").strip().splitlines()
    if not lines:
        return "GENESIS"
    return hashlib.sha256(lines[-1].encode("utf-8")).hexdigest()


def _file_hash(filepath: str) -> str | None:
    """SHA-256 of a file for evidence hashing. Returns None if file doesn't exist."""
    p = Path(filepath)
    if not p.exists():
        return None
    return hashlib.sha256(p.read_bytes()).hexdigest()


# Authority mapping per phase — from governance_framework §4.2
PHASE_AUTHORITY = {
    1: "OPERATIONAL",   # KN authority
    2: "OPERATIONAL",   # KN authority
    3: "OPERATIONAL",   # KN + RO
    4: "SAFETY",        # RO authority (gate review)
    5: "COMMAND",       # RSO authority (safety validation)
}


def log_decision(phase: int, decision: str, config: dict,
                 rationale: str = "", evidence_files: list[str] | None = None):
    """
    Enriched audit trail — governance_framework_VN-RANGE-001.md §1.2 schema.
    Hash-chained for tamper evidence (§1.3).
    """
    log_path = Path("pipeline_audit_log.jsonl")
    prior_hash = _last_record_hash(log_path)

    evidence = []
    for f in (evidence_files or [config["output_file"]]):
        h = _file_hash(f)
        if h:
            evidence.append({"file": f, "hash_sha256": h})

    log_entry = {
        "record_id": f"AUD-{datetime.now().strftime('%Y-%m%d-%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "context": {
            "system": "VN-RANGE-001",
            "phase": phase,
            "phase_name": config["name"],
            "consequence_level": config["consequence"],
            "automation_pct": config["automation_pct"],
        },
        "actor": {
            "role": "KN" if phase <= 3 else ("RO" if phase == 4 else "RSO"),
            "authority_level": PHASE_AUTHORITY.get(phase, "OPERATIONAL"),
        },
        "evidence_reviewed": evidence,
        "decision": {
            "action": decision,
            "rationale": rationale,
        },
        "integrity": {
            "prior_record_hash": prior_hash,
        },
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(f"   [Audit: {log_entry['record_id']} → {log_path}]")


def validate_phase_output(phase: int, output_file: str) -> tuple[str, str]:
    """
    Run Skill 3 QC validation on a completed phase output.
    Returns (verdict, detail) where verdict is PASS / WARN / FAIL / SKIP.

    Automated checks per phase:
      Phase 1: output file exists + substantial content + no HALT keyword
      Phase 2: readiness score ≥70 extracted from output
      Phase 3: automation gradient labels present ([AI-ASSIST], [HUMAN-LED], etc.)
      Phase 4: DfX gate score ≥70 extracted from output
      Phase 5: always SKIP (0% automated — human-led)
    """
    path = Path(output_file)

    # Phase 5: no automated validation
    if phase == 5:
        return "SKIP", "Phase 5 is 0% automated — no automated QC applies"

    # All phases: check output file exists and has content
    if not path.exists():
        return "FAIL", f"Output file not created: {output_file}"
    content = path.read_text(encoding="utf-8", errors="replace")
    if len(content) < 300:
        return "FAIL", f"Output file too short ({len(content)} chars) — AI may not have completed task"

    # Check for HALT keyword — AI detected a safety issue
    if "HALT" in content.upper() and phase in (1, 2, 3):
        return "FAIL", "AI output contains HALT recommendation — safety issue detected, do not proceed"

    # Phase-specific checks
    if phase == 2:
        # Extract readiness score: "readiness score: 82" or "Score: 75/100"
        match = re.search(r'readiness\s+score[:\s]+(\d+)', content, re.IGNORECASE)
        if match:
            score = int(match.group(1))
            if score < 70:
                return "FAIL", f"Architecture readiness score {score}/100 < required 70. Gate 2 NOT met."
            elif score < 80:
                return "WARN", f"Architecture readiness score {score}/100 — marginal (target ≥80)"
            else:
                return "PASS", f"Architecture readiness score {score}/100"
        else:
            return "WARN", "Could not extract readiness score from output — review manually"

    if phase == 3:
        # Check automation gradient labels are present
        labels = ["[AI-ASSIST]", "[SEMI-AUTO]", "[HUMAN-LED]", "[HUMAN-ONLY]"]
        found = [l for l in labels if l in content]
        if len(found) < 2:
            return "WARN", f"Only {len(found)}/4 automation gradient labels found — gradient may not be fully applied"
        # Check fallback protocols section
        if "fallback" not in content.lower():
            return "WARN", "No fallback protocols section found — required by Skill 4 framework"
        return "PASS", f"Gradient labels present ({', '.join(found)}), fallback protocols documented"

    if phase == 4:
        # Extract DfX gate score
        match = re.search(r'(?:gate\s+score|overall)[:\s]+(\d+)', content, re.IGNORECASE)
        if match:
            score = int(match.group(1))
            if score < 70:
                return "FAIL", f"DfX gate score {score}/100 < required 70. Gate 3 NOT met."
            elif score < 80:
                return "WARN", f"DfX gate score {score}/100 — passed but marginal (target ≥80)"
            else:
                return "PASS", f"DfX gate score {score}/100"
        else:
            return "WARN", "Could not extract DfX gate score — review manually"

    # Phase 1 and fallthrough: content checks passed
    req_count = len(re.findall(r'^\d+\.', content, re.MULTILINE))
    if phase == 1 and req_count < 10:
        return "WARN", f"Only {req_count} numbered requirements found — target is ≥15 across 6 categories"
    return "PASS", f"Output validated ({len(content)} chars{f', {req_count} requirements' if phase == 1 else ''})"


def check_prerequisites(phase: int) -> tuple[bool, str | None]:
    """Check that required prior phase outputs exist."""
    prerequisites = {
        1: None,  # No prereq for Phase 1
        2: "requirements_VN-RANGE-001.md",
        3: "architecture_review_VN-RANGE-001.md",
        4: "integration_design_VN-RANGE-001.md",
        5: "dfx_gate_review_VN-RANGE-001.md",
    }
    prereq = prerequisites.get(phase)
    if prereq and not Path(prereq).exists():
        return False, prereq
    return True, prereq


async def main():
    parser = argparse.ArgumentParser(description="VN-RANGE-001 Deployment Pipeline")
    parser.add_argument("--phase", type=int, required=True, choices=[1, 2, 3, 4, 5],
                        help="Pipeline phase to run (1-5)")
    parser.add_argument("--input", type=str, help="Input file from prior phase (optional override)")
    args = parser.parse_args()

    print(f"\nVN-RANGE-001 DEPLOYMENT PIPELINE")
    print(f"IRONMESH RANGE Smart Range System")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    # Check prerequisites
    ok, prereq = check_prerequisites(args.phase)
    if not ok:
        print(f"\n❌ PREREQUISITE MISSING: {prereq}")
        print(f"   Run Phase {args.phase - 1} first and obtain approval before proceeding.")
        sys.exit(1)

    input_file = args.input or prereq
    success = await run_phase(args.phase, input_file)

    if success:
        config = PHASE_CONFIG[args.phase]
        print(f"\n✅ Phase {args.phase} ({config['name']}) complete.")
        if args.phase < 5:
            next_phase = args.phase + 1
            next_config = PHASE_CONFIG[next_phase]
            print(f"\nNext: Phase {next_phase} ({next_config['name']})")
            print(f"      python sdk_pipeline_VN-RANGE-001.py --phase {next_phase}")
    else:
        print(f"\n⚠️  Phase {args.phase} requires revision. Re-run after adjustments.")


if __name__ == "__main__":
    asyncio.run(main())
