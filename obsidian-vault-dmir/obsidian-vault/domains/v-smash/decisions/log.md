# V-SMASH Decision Log

> **Project**: V-SMASH Fire Control System
> **Last Updated**: 2026-01-26

---

## Decision Index

| ID | Date | Title | Status | Impact |
|----|------|-------|--------|--------|
| DEC-001 | 2026-01-18 | Design Philosophy Adoption | ✅ Approved | High |
| DEC-002 | 2026-01-18 | Detection Approach | ✅ Approved | High |
| DEC-003 | 2026-01-18 | Processing Platform Selection | ⚠️ Superseded by DEC-005 | High |
| DEC-004 | 2026-01-18 | Concept Selection (V4) | ✅ Approved | Critical |
| **DEC-005** | **2026-01-26** | **Processing Platform Revision** | **✅ Approved** | **High** |

---

## DEC-001: Design Philosophy Adoption

**Date**: 2026-01-18 | **Status**: ✅ Approved

**Decision**: Adopt SMASH 2000+ design philosophy as reference architecture.

**Key Principles**:
1. Human-in-the-loop (AI assists, human decides)
2. Modular platform (common core, weapon-specific modules)
3. Fail-safe to manual (weapon functional without electronics)

**Rationale**: SMASH is proven in combat (10,000+ units deployed). Philosophy aligns with Vietnamese doctrine requirements.

---

## DEC-002: Detection Approach

**Date**: 2026-01-18 | **Status**: ✅ Approved

**Decision**: Phased detection strategy - HOG+SVM (Phase 1) → YOLOv8-nano (Phase 2)

**Options Considered**:
- A: Template matching only
- B: HOG+SVM only
- **C: Phased HOG→YOLO** ✓
- D: YOLO from start

**Rationale**: 
- Phase 1 (HOG+SVM): No training data needed, faster time-to-prototype
- Phase 2 (YOLO): Superior accuracy, dataset collected during Phase 1
- Risk reduction over starting with YOLO directly

---

## DEC-003: Processing Platform Selection (SUPERSEDED)

**Date**: 2026-01-18 | **Status**: ⚠️ Superseded by DEC-005

**Original Decision**: Jetson Nano for Phase 1, Xavier NX upgrade for Phase 2

**Why Superseded**: Analysis in DEC-005 shows this path is MORE expensive and riskier than starting with Xavier NX.

---

## DEC-004: Concept Selection

**Date**: 2026-01-18 | **Status**: ✅ Approved

**Decision**: Select V4 (Phased Development) approach

**VDI 2225 Results**:
| Concept | Technical Value | Rank |
|---------|-----------------|------|
| V1: Clone | 45% | 4th |
| V2: Local-First | 79% | 2nd |
| V3: Hybrid | 73% | 3rd |
| **V4: Phased** | **85%** | **1st** |

**Rationale**: Best balance of risk mitigation, capability growth, and local expertise building. Sensitivity analysis confirms robustness.

---

## DEC-005: Processing Platform Revision ⭐ NEW

**Date**: 2026-01-26 | **Status**: 🔄 Proposed

**Decision**: Use Jetson Xavier NX ($400) from Phase 1, eliminating Jetson Nano path

**Key Finding**: 
- Jetson Nano achieves only **6-16 FPS for YOLOv8n** (below 30 FPS requirement)
- Xavier NX achieves **66 FPS** (exceeds requirement)
- Total cost of ownership is LOWER with Xavier NX due to eliminated upgrade costs

**Cost Comparison**:
| Path | Phase 1 | Phase 2 Upgrade | Engineering | Total |
|------|---------|-----------------|-------------|-------|
| Nano→Xavier | $150 | $400 + $100 | $2,000 | **$2,650** |
| Xavier Direct | $400 | $0 | $0 | **$400** |

**Impact**:
- BOM increases from $644 to $894 per unit
- Eliminates Phase 2 hardware risk
- Simplifies carrier board design

**Pending Approval**: Technical Lead, Program Manager, Budget Authority

**Full Analysis**: [[decisions/DEC-005-processing-platform]]

---

## Pending Decisions

| Topic | Priority | Target Date | Owner |
|-------|----------|-------------|-------|
| Carrier board vendor selection | Medium | 2026-02 | HW Lead |
| Training data collection strategy | Medium | 2026-02 | AI Lead |
| Optic supplier selection | Low | 2026-03 | Mech Lead |

---

## Related Documents

- [[../README]] - Project overview
- [[../requirements/v1.1-summary]] - Requirements driving decisions
- [[../design/vdi-2225-evaluation]] - Concept evaluation details
- [[../design/morphological-matrix]] - Solution space exploration

---

*Decision log follows systematic engineering decision documentation practice*
