#!/usr/bin/env python3
"""
Requirements Completeness Validator

Parses a requirements list markdown file and checks:
- Category coverage (16 Pahl & Beitz categories)
- Quantification percentage (target: 80%)
- Verification method assignment (A/I/T/D)
- MUST vs WISH classification

Usage:
    python validate_requirements.py <path-to-requirements.md>

Output:
    Completeness report with pass/fail status per check.
"""

import re
import sys
from pathlib import Path

CATEGORIES = [
    "Geometry", "Kinematics", "Forces", "Energy",
    "Material", "Signals", "Safety", "Ergonomics",
    "Production", "Quality", "Assembly", "Transport",
    "Operation", "Maintenance", "Costs", "Schedule",
]

VERIFY_METHODS = {"A", "I", "T", "D"}

# Matches table rows like: | GEO-001 | some req | 15 kg | MUST | T | MIL-STD | note |
ROW_PATTERN = re.compile(
    r"^\|\s*([A-Z]{3}-\d{3})\s*\|"   # ID
    r"\s*(.*?)\s*\|"                   # Requirement
    r"\s*(.*?)\s*\|"                   # Value/Range
    r"\s*(.*?)\s*\|"                   # Type (MUST/WISH)
    r"\s*(.*?)\s*\|"                   # Verify (A/I/T/D)
    r"\s*(.*?)\s*\|"                   # Source
    r"\s*(.*?)\s*\|",                  # Notes
    re.IGNORECASE,
)


def parse_requirements(filepath):
    """Parse a requirements markdown file and extract requirement rows."""
    text = Path(filepath).read_text(encoding="utf-8")
    requirements = []

    for line in text.splitlines():
        m = ROW_PATTERN.match(line)
        if m:
            req_id, desc, value, req_type, verify, source, notes = m.groups()
            if desc.strip():  # skip empty template rows
                requirements.append({
                    "id": req_id.strip(),
                    "description": desc.strip(),
                    "value": value.strip(),
                    "type": req_type.strip().upper(),
                    "verify": verify.strip().upper(),
                    "source": source.strip(),
                })

    return requirements


def validate(requirements):
    """Run validation checks and return results."""
    results = []
    total = len(requirements)

    if total == 0:
        print("No requirements found in file.")
        return []

    # 1. Category coverage
    found_prefixes = {r["id"][:3] for r in requirements}
    prefix_map = {
        "GEO": "Geometry", "KIN": "Kinematics", "FRC": "Forces",
        "NRG": "Energy", "MAT": "Material", "SIG": "Signals",
        "SAF": "Safety", "ERG": "Ergonomics", "PRD": "Production",
        "QUA": "Quality", "ASM": "Assembly", "TRN": "Transport",
        "OPR": "Operation", "MNT": "Maintenance", "CST": "Costs",
        "SCH": "Schedule",
    }
    covered = sum(1 for p in prefix_map if p in found_prefixes)
    missing = [name for pfx, name in prefix_map.items() if pfx not in found_prefixes]
    results.append({
        "check": "Category coverage",
        "status": "PASS" if covered == 16 else "FAIL",
        "detail": f"{covered}/16 categories",
        "missing": missing,
    })

    # 2. Quantification
    has_number = re.compile(r"\d")
    quantified = sum(1 for r in requirements if has_number.search(r["value"]))
    pct = round(quantified / total * 100)
    results.append({
        "check": "Quantified",
        "status": "PASS" if pct >= 80 else "FAIL",
        "detail": f"{pct}% ({quantified}/{total}, target >= 80%)",
    })

    # 3. Verification methods
    has_verify = sum(1 for r in requirements if r["verify"] in VERIFY_METHODS)
    missing_verify = total - has_verify
    results.append({
        "check": "Verification methods",
        "status": "PASS" if missing_verify == 0 else "FAIL",
        "detail": f"{missing_verify} missing",
    })

    # 4. MUST/WISH classification
    classified = sum(1 for r in requirements if r["type"] in ("MUST", "WISH"))
    unclassified = total - classified
    results.append({
        "check": "MUST/WISH classified",
        "status": "PASS" if unclassified == 0 else "FAIL",
        "detail": f"{unclassified} unclassified",
    })

    # 5. Counts
    musts = sum(1 for r in requirements if r["type"] == "MUST")
    wishes = sum(1 for r in requirements if r["type"] == "WISH")
    results.append({
        "check": "Requirement counts",
        "status": "INFO",
        "detail": f"{total} total ({musts} MUST, {wishes} WISH)",
    })

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_requirements.py <path-to-requirements.md>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not Path(filepath).exists():
        print(f"File not found: {filepath}")
        sys.exit(1)

    requirements = parse_requirements(filepath)
    results = validate(requirements)

    if not results:
        sys.exit(1)

    # Print report
    print(f"\n{'='*60}")
    print(f"  REQUIREMENTS VALIDATION REPORT")
    print(f"  File: {filepath}")
    print(f"{'='*60}\n")

    all_pass = True
    for r in results:
        icon = {"PASS": "[PASS]", "FAIL": "[FAIL]", "INFO": "[INFO]"}[r["status"]]
        print(f"  {icon} {r['check']}: {r['detail']}")
        if r.get("missing"):
            print(f"         Missing: {', '.join(r['missing'])}")
        if r["status"] == "FAIL":
            all_pass = False

    print(f"\n{'='*60}")
    if all_pass:
        print("  RESULT: PASS - Ready for Gate 1 review")
    else:
        print("  RESULT: FAIL - Address issues before Gate 1")
    print(f"{'='*60}\n")

    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
