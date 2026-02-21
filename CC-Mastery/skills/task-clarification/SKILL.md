---
name: task-clarification
description: Phase 1 requirements engineering for defense products using Pahl and Beitz methodology. This skill should be used when starting a new design project, eliciting requirements, mapping standards (MIL-STD/TCVN), performing stakeholder analysis, or validating requirements completeness.
---

# Phase 1: Task Clarification

Generate complete, quantified, conflict-free requirements lists for Vietnamese defense products
using Pahl & Beitz systematic design (16 requirement categories).

## Commands

| Command | Aliases | Action |
|---------|---------|--------|
| `/requirements` | `/req`, `/taoreq` | Generate requirements list across 16 categories |
| `/validate` | `/check` | Check completeness score and flag conflicts |
| `/standards` | `/mil`, `/std` | Map MIL-STD/TCVN standards to requirements |
| `/stakeholders` | `/stake` | Perform stakeholder analysis using mapping template |

## Workflow (7 Steps)

To complete Phase 1, follow these steps in order:

1. **Gather inputs** - Collect customer brief, RFP, applicable standards, competitive analysis, field reports
2. **Map stakeholders** - Identify Customer/User/Maintainer/Regulator/Manufacturer using template in `references/stakeholder_mapping.md`
3. **Categorize requirements** - Assign to 16 Pahl & Beitz categories (see `references/pahl_beitz_categories.md` for the full table with defense-specific questions)
4. **Classify MUST vs WISH** - MUST = failure if not met (safety, regulations, physics). WISH = weighted 1-5, tradeable
5. **Quantify** - Every requirement gets a number. Run `scripts/validate_requirements.py` to check percentage
6. **Assign verification method** - Each requirement gets A (Analysis), I (Inspection), T (Test), or D (Demonstration)
7. **Check conflicts & completeness** - Run `/validate` to score. Target: 80%+ quantified, 16/16 categories covered, zero unresolved conflicts

## Output

`/requirements` produces a requirements list file. Copy the template from `assets/requirements_list_template.md` into the project folder, then populate it.

`/validate` produces a completeness report:
```
Completeness Score: [XX]%
| Check              | Status | Details          |
|--------------------|--------|------------------|
| All 16 categories  | Y/N    | [count]/16       |
| Quantified         | Y/N    | [pct]% (min 80%) |
| Verification methods| Y/N   | [count] missing  |
| Conflicts          | Y/N    | [count] open     |
```

## Quantification Rules

| Vague (reject)    | Quantified (accept)                    |
|-------------------|----------------------------------------|
| "lightweight"     | mass <= 15 kg (target 12 kg)           |
| "fast"            | acquisition time <= 3 s                |
| "reliable"        | MTBF >= 5000 h                         |
| "affordable"      | unit cost <= $15,000 at lot size 50    |
| "easy to use"     | operator training <= 8 h               |

Always push back on vague requirements. Ask "what number?" or propose a range.

## Common Mistakes

1. **Solution-first** - "Use motor XYZ" instead of "Thrust >= 50N, efficiency >= 80%"
2. **Missing verification** - Every requirement needs an A/I/T/D method
3. **Unresolved conflicts** - "Mass < 10kg" AND "armor plating required" must be explicitly traded off
4. **Incomplete categories** - All 16 Pahl & Beitz categories must have at least one requirement

## Phase 1 Exit Criteria (Gate 1)

- [ ] >= 80% MUST requirements quantified with tolerance
- [ ] 100% MUST requirements have verification method
- [ ] Standards compliance matrix complete
- [ ] No unresolved conflicts
- [ ] Stakeholder review completed
- [ ] Document version controlled

Minimum requirement counts: Simple component 50-80, Subsystem 100-150, Full system 200-300+.

## Related Resources

- `references/pahl_beitz_categories.md` - 16 categories with defense-specific questions
- `references/stakeholder_mapping.md` - Stakeholder identification template
- `assets/requirements_list_template.md` - Full requirements document template
- `scripts/validate_requirements.py` - Automated completeness checker
