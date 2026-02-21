---
project: VN-RNG-001
name: LOMAH Acoustic Shooting Range System
phase: 1
status: active
created: 2026-02-08
updated: 2026-02-09
---

# VN-RNG-001 - LOMAH Acoustic Shooting Range System

## Status
Phase 1/4 | Active | Updated: 2026-02-09
Progress: ███░░░░░░░ 25%

## Phase Progress
- [x] Phase 0: ODI Customer Insight - **COMPLETE** (Gate Approved 2026-02-09)
- [x] Phase 1: Task Clarification (Requirements) - **IN PROGRESS**
- [ ] Phase 2: Conceptual Design
- [ ] Phase 3: Embodiment Design
- [ ] Phase 4: Detail Design

## Phase 0 Deliverables (Complete)
- [x] ODI Steps 1-10 (73 outcomes, 3 segments, DOMINANT strategy)
- [x] Customer Scorecard: Concept B Smart LOMAH = 8.46/10
- [x] RE: Saab Live Fire Precision Scoring
- [x] RE: Polytronic International (TG series)
- [x] RE: FATS/Meggitt/InVeris Training Solutions
- [x] GCC-PHAT firmware (algorithm + tests)
- [x] Phase 0 Gate Review: **APPROVED**

## Current Phase: 1 - Task Clarification (Requirements)
- [x] Requirements list (16 categories) - **120 requirements, 94% quantified**
- [x] Standards mapping (MIL-STD + TCVN) - **11 standards mapped**
- [x] Stakeholder analysis - **10 stakeholders, RACI matrix, engagement strategy**
- [x] Requirements validation - **ALL GATE 1 CRITERIA PASSED**
- [ ] Phase 1 Gate Review

## Key Metrics
- Target unit cost: $5,000-15,000/lane (vs import $10,000-25,000)
- Target local content: 60-75%
- Target cost vs import: ≤50-60%
- Accuracy target: <5mm radial

## RE Summary (FTO Clear)
- Foundational LOMAH patents EXPIRED (US4350881A, WO1997024575A1)
- Saab dual-delta patent: avoid (use temp sensor alternative)
- InVeris: NO LOMAH-specific patents
- Polytronic: avoid subsonic RADAR patents
- GCC-PHAT algorithm: public domain (Knapp & Carter, 1976)

## Files
### Phase 0
- [[00_odi/odi_analysis.md]] - Phase 0 ODI full analysis (Steps 1-10)
- [[00_odi/re_saab_lomah.md]] - RE: Saab LOMAH system
- [[00_odi/re_polytronic.md]] - RE: Polytronic LOMAH system
- [[00_odi/re_fats_inveris.md]] - RE: FATS/Meggitt/InVeris LOMAH system
- [[00_project_brief.md]] - Project brief

### Firmware
- [[firmware/inc/gcc_phat.h]] - GCC-PHAT API header
- [[firmware/src/gcc_phat.c]] - GCC-PHAT implementation
- [[firmware/test/test_gcc_phat.c]] - GCC-PHAT unit tests

### Phase 1 (In Progress)
- [[01_requirements/requirements_list.md]] - Requirements list v1.0 (120 requirements, 16 categories)
- [[01_requirements/stakeholder_analysis.md]] - Stakeholder analysis (10 stakeholders, RACI)
- [[01_requirements/requirements_validation.md]] - Validation report (all gate criteria passed)
