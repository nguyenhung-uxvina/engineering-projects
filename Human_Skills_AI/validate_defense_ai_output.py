"""
Defense AI Output Validator — Workshop X
=========================================
Skill 3: Critical Reasoning — Automated QC Layer

Automates Categories 1 (Physics) and 2 (Data Quality) from defense_ai_qc_checklist.md.
Categories 3-6 require human judgment and are listed as MANUAL reminders.

Usage:
    python validate_defense_ai_output.py --input output.json
    python validate_defense_ai_output.py --type scoring --range 800 --acoustic 7 --visual 6
    python validate_defense_ai_output.py --type ballistic --weapon hmg_127 --range 2800

Output:
    PASS   — All automated checks passed
    WARN   — Passed but with caveats (human should review flagged items)
    FAIL   — One or more automated checks failed
    EXIT 0 — pass/warn (pipeline can continue, subject to human HITL)
    EXIT 2 — fail (pipeline should halt, escalate to human)
"""

import sys
import argparse
import json
import math
from dataclasses import dataclass, field
from typing import Optional

# Windows UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# ─── Weapon Specifications (sourced from Workshop X product data)
WEAPON_SPECS = {
    "hmg_127": {
        "name": "12.7mm HMG",
        "effective_range_m": 2000,
        "muzzle_velocity_ms": 930,
        "bullet_mass_g": 46.7,
        "ballistic_coeff": 0.65,
    },
    "rifle_762": {
        "name": "7.62mm rifle",
        "effective_range_m": 600,
        "muzzle_velocity_ms": 830,
        "bullet_mass_g": 9.75,
        "ballistic_coeff": 0.41,
    },
    "rifle_556": {
        "name": "5.56mm rifle",
        "effective_range_m": 500,
        "muzzle_velocity_ms": 940,
        "bullet_mass_g": 4.0,
        "ballistic_coeff": 0.30,
    },
    "pistol_9mm": {
        "name": "9mm pistol",
        "effective_range_m": 50,
        "muzzle_velocity_ms": 370,
        "bullet_mass_g": 8.0,
        "ballistic_coeff": 0.15,
    },
}

# ─── Environmental constants for Vietnam coastal deployment
SPEED_OF_SOUND_MS = 340.0          # m/s at 20°C sea level
TEMP_CORRECTION_PER_C = 0.6        # m/s per degree C above 20°C
CONFIDENCE_THRESHOLD = 0.85
MARITIME_ACOUSTIC_RANGE_FACTOR = 0.70  # 30% degradation for water reflections
MAX_SENSOR_DELTA = 1               # Max allowed acoustic vs. visual count mismatch


@dataclass
class CheckResult:
    category: str
    check: str
    status: str           # PASS, WARN, FAIL
    detail: str
    automatable: bool = True


@dataclass
class ValidationReport:
    checks: list[CheckResult] = field(default_factory=list)
    weapon: Optional[str] = None
    range_m: Optional[float] = None

    def add(self, category, check, status, detail, automatable=True):
        self.checks.append(CheckResult(category, check, status, detail, automatable))

    @property
    def verdict(self) -> str:
        statuses = [c.status for c in self.checks if c.automatable]
        if "FAIL" in statuses:
            return "FAIL"
        if "WARN" in statuses:
            return "WARN"
        return "PASS"

    def print_report(self):
        print(f"\n{'='*65}")
        print("DEFENSE AI OUTPUT VALIDATION REPORT")
        print(f"{'='*65}")
        if self.weapon:
            print(f"Weapon:  {self.weapon}")
        if self.range_m:
            print(f"Range:   {self.range_m:.0f}m")
        print()

        current_cat = None
        for c in self.checks:
            if c.category != current_cat:
                current_cat = c.category
                auto = "(automated)" if c.automatable else "(MANUAL required)"
                print(f"\n[ {c.category} ] {auto}")
                print("─" * 60)

            icon = {"PASS": "OK ", "WARN": "!! ", "FAIL": "XX "}.get(c.status, "   ")
            print(f"  {icon} {c.check}")
            if c.status != "PASS":
                print(f"       → {c.detail}")

        print(f"\n{'='*65}")
        verdict = self.verdict
        icon = {"PASS": "PASS", "WARN": "PASS* (review warnings)", "FAIL": "FAIL — do not proceed"}.get(verdict, verdict)
        print(f"VERDICT: {icon}")
        print(f"{'='*65}\n")

        # Manual checklist reminder
        manual = [c for c in self.checks if not c.automatable]
        if manual:
            print("MANUAL CHECKS REQUIRED (human judgment — not automated):")
            for c in manual:
                print(f"  [ ] {c.category}: {c.check}")
            print()


# ─── Category 1: Physics Plausibility

def check_ballistics(report: ValidationReport, weapon_key: str, range_m: float,
                     ai_confidence: Optional[float] = None):
    """Validate ballistic plausibility for weapon at range."""
    spec = WEAPON_SPECS.get(weapon_key)
    if not spec:
        report.add("Cat 1: Physics", "Weapon specification lookup",
                   "WARN", f"Unknown weapon '{weapon_key}' — cannot validate ballistics")
        return

    report.weapon = spec["name"]
    report.range_m = range_m

    # Check 1.1: Effective range
    if range_m > spec["effective_range_m"]:
        report.add("Cat 1: Physics", "Range vs. effective range",
                   "FAIL",
                   f"{spec['name']} effective range is {spec['effective_range_m']}m. "
                   f"AI solution at {range_m:.0f}m exceeds this by "
                   f"{range_m - spec['effective_range_m']:.0f}m. "
                   f"(Classic VN-SMASH error: optimizes hit probability, ignores lethality threshold)")
    elif range_m > spec["effective_range_m"] * 0.85:
        report.add("Cat 1: Physics", "Range vs. effective range",
                   "WARN",
                   f"{range_m:.0f}m is within 15% of effective range limit ({spec['effective_range_m']}m). "
                   f"Verify terminal ballistics are sufficient for the target.")
    else:
        report.add("Cat 1: Physics", "Range vs. effective range", "PASS", "")

    # Check 1.2: Kinetic energy at range (simplified, no air drag integration)
    v0 = spec["muzzle_velocity_ms"]
    m_kg = spec["bullet_mass_g"] / 1000
    # Simplified velocity retention: v ≈ v0 * exp(-k * range) where k from BC
    k = 0.001 / spec["ballistic_coeff"]   # rough approximation
    v_at_range = v0 * math.exp(-k * range_m)
    ke_j = 0.5 * m_kg * v_at_range ** 2
    report.add("Cat 1: Physics", "Estimated KE at target",
               "PASS" if ke_j > 100 else "WARN",
               f"Estimated KE ≈ {ke_j:.0f}J at {range_m:.0f}m "
               f"({'sufficient' if ke_j > 100 else 'marginal — verify lethality requirement'})")

    # Check 1.3: AI confidence vs. range
    if ai_confidence is not None:
        if range_m > spec["effective_range_m"] and ai_confidence > 0.80:
            report.add("Cat 1: Physics", "Confidence calibration",
                       "FAIL",
                       f"AI confidence {ai_confidence:.0%} is HIGH despite range "
                       f"exceeding effective limit. Overconfident solution — reject.")
        else:
            report.add("Cat 1: Physics", "Confidence calibration", "PASS", "")


def check_acoustics(report: ValidationReport, range_m: float,
                    stated_acoustic_delay_s: Optional[float] = None,
                    ambient_temp_c: float = 30.0,
                    is_maritime: bool = True):
    """Validate acoustic physics for VN-LOMAH outputs."""
    # Corrected speed of sound for ambient temperature
    v_sound = SPEED_OF_SOUND_MS + TEMP_CORRECTION_PER_C * (ambient_temp_c - 20.0)
    expected_delay = range_m / v_sound

    if is_maritime:
        max_effective_range = range_m * MARITIME_ACOUSTIC_RANGE_FACTOR
        if range_m > 1500:
            report.add("Cat 1: Physics", "Maritime acoustic range",
                       "WARN",
                       f"Maritime environment reduces effective acoustic range by ~30%. "
                       f"At {range_m:.0f}m, SNR may be marginal. Verify LOMAH confidence ≥0.85.")
        else:
            report.add("Cat 1: Physics", "Maritime acoustic range", "PASS", "")

    if stated_acoustic_delay_s is not None:
        tolerance = 0.5  # seconds
        expected = expected_delay
        if abs(stated_acoustic_delay_s - expected) > tolerance:
            report.add("Cat 1: Physics", "Acoustic delay vs. range",
                       "FAIL",
                       f"Stated delay {stated_acoustic_delay_s:.2f}s inconsistent with "
                       f"range {range_m:.0f}m at {ambient_temp_c:.0f}°C "
                       f"(expected {expected:.2f}s ± {tolerance}s). "
                       f"Check range estimate or speed-of-sound correction.")
        else:
            report.add("Cat 1: Physics", "Acoustic delay vs. range",
                       "PASS", f"Delay {stated_acoustic_delay_s:.2f}s consistent with {range_m:.0f}m")


# ─── Category 2: Data Quality

def check_sensor_fusion(report: ValidationReport,
                        acoustic_count: int, visual_count: int,
                        ai_confidence: float):
    """Validate VN-LOMAH / VN-CAM fusion consistency."""
    delta = abs(acoustic_count - visual_count)

    # Count correlation (CORTEX FSM §4.2 logic)
    if delta == 0:
        report.add("Cat 2: Data Quality", "Sensor count correlation",
                   "PASS", f"Acoustic={acoustic_count}, Visual={visual_count} — exact match")
    elif delta == 1:
        report.add("Cat 2: Data Quality", "Sensor count correlation",
                   "WARN",
                   f"Acoustic={acoustic_count}, Visual={visual_count} — delta=1. "
                   f"Possible ricochet fragment. HITL review required (CORTEX S4).")
    else:
        report.add("Cat 2: Data Quality", "Sensor count correlation",
                   "FAIL",
                   f"Acoustic={acoustic_count}, Visual={visual_count} — delta={delta}. "
                   f"Large mismatch. DO NOT AUTO-SCORE. Manual recount required (CORTEX S5.2).")

    # Confidence threshold
    if ai_confidence < CONFIDENCE_THRESHOLD:
        report.add("Cat 2: Data Quality", "Confidence threshold",
                   "FAIL",
                   f"AI confidence {ai_confidence:.0%} below required {CONFIDENCE_THRESHOLD:.0%}. "
                   f"HITL pause required — do not auto-accept score.")
    else:
        report.add("Cat 2: Data Quality", "Confidence threshold",
                   "PASS", f"Confidence {ai_confidence:.0%} ≥ {CONFIDENCE_THRESHOLD:.0%}")

    # Out-of-distribution warning (heuristic)
    if ai_confidence > 0.95 and delta > 0:
        report.add("Cat 2: Data Quality", "Overconfidence check",
                   "WARN",
                   f"Confidence {ai_confidence:.0%} is very high despite count mismatch (delta={delta}). "
                   f"AI may be overconfident on ambiguous data. Verify manually.")
    else:
        report.add("Cat 2: Data Quality", "Overconfidence check", "PASS", "")


def check_qualification(report: ValidationReport,
                        score_pct: float,
                        ai_proposed_threshold: Optional[float] = None,
                        approved_threshold: float = 70.0):
    """Check qualification scoring against approved threshold."""
    # Critical: AI must NOT propose its own threshold
    if ai_proposed_threshold is not None and ai_proposed_threshold != approved_threshold:
        report.add("Cat 2: Data Quality", "Qualification threshold source",
                   "FAIL",
                   f"AI proposed threshold {ai_proposed_threshold:.0f}% differs from approved "
                   f"{approved_threshold:.0f}%. Always use approved threshold. "
                   f"AI must not set its own standards.")
    else:
        report.add("Cat 2: Data Quality", "Qualification threshold source", "PASS",
                   f"Using approved threshold {approved_threshold:.0f}%")

    # Score vs. threshold
    if score_pct >= approved_threshold:
        report.add("Cat 2: Data Quality", "Score vs. threshold",
                   "PASS", f"Score {score_pct:.1f}% ≥ threshold {approved_threshold:.0f}%")
    else:
        report.add("Cat 2: Data Quality", "Score vs. threshold",
                   "WARN",
                   f"Score {score_pct:.1f}% < threshold {approved_threshold:.0f}%. "
                   f"Unit does not qualify. Additional rounds or re-attempt required.")


# ─── Manual Reminders (Categories 3-6) — human judgment, cannot automate

def add_manual_reminders(report: ValidationReport):
    """Add non-automatable checks as reminders."""
    manual = [
        ("Cat 3: Safety", "Safety fan — all impacts within boundary?"),
        ("Cat 3: Safety", "Emergency stop tested within last 30 minutes?"),
        ("Cat 3: Safety", "RSO clearance obtained for this session?"),
        ("Cat 4: Compliance", "TCVN scoring standard applied (not AI-proposed variant)?"),
        ("Cat 4: Compliance", "Documentation bilingual (Vietnamese + English)?"),
        ("Cat 5: RoE", "IFF check completed before engagement solution accepted?"),
        ("Cat 5: RoE", "Target positively identified — NOT AI classification alone?"),
        ("Cat 5: RoE", "ROE section verified to exist and apply?"),
        ("Cat 6: Context", "System calibration current (within required interval)?"),
        ("Cat 6: Context", "Sea state within system rated envelope (≤Sea State 4)?"),
    ]
    for cat, check in manual:
        report.add(cat, check, "MANUAL", "Human judgment required", automatable=False)


# ─── CLI entry point

def main():
    parser = argparse.ArgumentParser(
        description="Defense AI Output Validator — Workshop X Skill 3 automation"
    )
    parser.add_argument("--type", choices=["scoring", "ballistic", "full"],
                        default="full", help="Validation type")
    parser.add_argument("--weapon", choices=list(WEAPON_SPECS.keys()),
                        help="Weapon key (e.g. hmg_127, rifle_762)")
    parser.add_argument("--range", type=float, dest="range_m",
                        help="Target range in meters")
    parser.add_argument("--acoustic", type=int,
                        help="Acoustic shot count (VN-LOMAH)")
    parser.add_argument("--visual", type=int,
                        help="Visual hit count (VN-CAM)")
    parser.add_argument("--confidence", type=float, default=0.90,
                        help="AI confidence score (0-1)")
    parser.add_argument("--score-pct", type=float,
                        help="Qualification score percentage")
    parser.add_argument("--acoustic-delay", type=float,
                        help="Stated acoustic delay in seconds")
    parser.add_argument("--temp", type=float, default=30.0,
                        help="Ambient temperature °C (default 30 for Vietnam)")
    parser.add_argument("--maritime", action="store_true", default=True,
                        help="Apply maritime acoustic corrections")
    parser.add_argument("--input", type=str,
                        help="JSON input file (alternative to CLI args)")
    args = parser.parse_args()

    # Load from JSON if provided
    if args.input:
        try:
            with open(args.input) as f:
                data = json.load(f)
            # Merge JSON fields into args
            for key, val in data.items():
                if not getattr(args, key.replace("-", "_"), None):
                    setattr(args, key.replace("-", "_"), val)
        except Exception as e:
            print(f"Error loading input file: {e}")
            sys.exit(2)

    report = ValidationReport()

    # Run relevant check categories
    if args.weapon and args.range_m:
        check_ballistics(report, args.weapon, args.range_m, args.confidence)

    if args.range_m:
        check_acoustics(report, args.range_m,
                        stated_acoustic_delay_s=args.acoustic_delay,
                        ambient_temp_c=args.temp,
                        is_maritime=args.maritime)

    if args.acoustic is not None and args.visual is not None:
        check_sensor_fusion(report, args.acoustic, args.visual, args.confidence)

    if args.score_pct is not None:
        check_qualification(report, args.score_pct)

    if not report.checks:
        print("No validation parameters provided. Use --help for usage.")
        sys.exit(2)

    add_manual_reminders(report)
    report.print_report()

    # Exit codes: 0 = pass/warn (pipeline may continue), 2 = fail (halt pipeline)
    sys.exit(0 if report.verdict in ("PASS", "WARN") else 2)


if __name__ == "__main__":
    main()
