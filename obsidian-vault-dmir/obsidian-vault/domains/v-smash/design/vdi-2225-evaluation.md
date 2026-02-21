# V-SMASH VDI 2225 Concept Evaluation

> **Document Type**: Conceptual Design - Concept Selection
> **Version**: 1.1
> **Method**: VDI 2225 Technical-Economic Evaluation

---

## 1. Evaluation Context

| Attribute | Value |
|-----------|-------|
| **Target Project** | V-SMASH Development Program |
| **Reference System** | SmartShooter SMASH (Israel) |
| **Evaluation Date** | 2026-01-18 |
| **Evaluator** | Design Team |
| **Strategy** | Technology Insertion with Local Adaptation |

---

## 2. Concepts Being Evaluated

| Concept | Description | Key Approach |
|---------|-------------|--------------|
| **V1: Direct Clone** | Full replication of SMASH design | Maximum capability, minimum local |
| **V2: Local-First** | Maximize local content, reduce scope | Maximum local, reduced capability |
| **V3: Hybrid Optimal** | Balance capability and local content | Optimal balance |
| **V4: Phased Build** | Start minimal, upgrade over time | Risk mitigation |

---

## 3. Criteria Weight Derivation

### Stakeholder Input Analysis

| Stakeholder | Role | Key Priorities |
|-------------|------|----------------|
| **Military End User** | Infantry/Vehicle crews | Reliability, effectiveness |
| **Procurement Office** | MoD acquisition | Value for money |
| **MoD Policy** | Strategic planning | Reduce foreign dependency |
| **Program Office** | Project management | Capability within timeline |
| **Maintenance Command** | Lifecycle support | Field maintainable |

### Pairwise Comparison Matrix (AHP Method)

Scale: 2 = much more important, 1 = slightly more important, 0.5 = equal, 0 = less

|    | C1:Perf | C2:Rel | C3:Dev$ | C4:Prod$ | C5:Time | C6:Supply | C7:Local | C8:Maint | C9:Interop |
|----|---------|--------|---------|----------|---------|-----------|----------|----------|------------|
| C1 | - | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 2 | 2 |
| C2 | 1 | - | 0.5 | 1 | 1 | 0.5 | 0.5 | 2 | 2 |
| C3 | 1 | 1.5 | - | 1 | 1 | 0.5 | 0.5 | 2 | 2 |
| C4 | 1 | 1 | 1 | - | 1 | 0.5 | 0.5 | 2 | 2 |
| C5 | 1 | 1 | 1 | 1 | - | 0.5 | 0.5 | 2 | 2 |
| C6 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | - | 1 | 2 | 2 |
| C7 | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 | 1 | - | 2 | 2 |
| C8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | 1 |
| C9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | - |

### Derived Weights

| ID | Criterion | Normalized | Rounded | Justification |
|----|-----------|------------|---------|---------------|
| C1 | Technical Performance | 13.6% | **15%** | End-user priority |
| C2 | Reliability | 12.9% | **10%** | Combat critical |
| C3 | Development Cost | 14.4% | **15%** | Procurement constraint |
| C4 | Production Cost | 13.6% | **10%** | Volume production |
| C5 | Development Time | 13.6% | **10%** | Operational urgency |
| C6 | Supply Chain Risk | 18.9% | **15%** | MoD policy priority |
| C7 | Local Capability Match | 18.9% | **15%** | MoD policy priority |
| C8 | Maintainability | 4.5% | **5%** | Secondary |
| C9 | Interoperability | 1.5% | **5%** | MTB-20 coverage |
| | **TOTAL** | 100% | **100%** | |

> **Note**: C6 and C7 elevated per MoD strategic directive on defense industry self-reliance

---

## 4. Scoring Scale

| Score | Definition | Example |
|-------|------------|---------|
| 0 | Completely inadequate | Fails mandatory requirements |
| 1 | Very poor | Major deficiencies, high risk |
| 2 | Poor | Significant gaps, substantial risk |
| 3 | Adequate | Meets minimum with concerns |
| 4 | Good | Solid performance, acceptable |

---

## 5. Evaluation Matrix

### Raw Scores (0-4 scale)

| Criterion | V1: Clone | V2: Local-First | V3: Hybrid | V4: Phased | Rationale |
|-----------|-----------|-----------------|------------|------------|-----------|
| C1: Performance | 4 | 2 | 3 | 3 | V1 proven; V2 reduced scope |
| C2: Reliability | 3 | 2 | 3 | 3 | V1 unproven local production |
| C3: Dev Cost | 1 | 3 | 3 | 4 | V1 high NRE; V4 spreads cost |
| C4: Prod Cost | 1 | 4 | 3 | 3 | V1 import-dependent |
| C5: Dev Time | 1 | 3 | 2 | 4 | V1 complex; V4 early deliverable |
| C6: Supply Chain | 1 | 4 | 3 | 3 | V1 foreign dependent |
| C7: Local Match | 1 | 4 | 3 | 4 | V4 builds capability progressively |
| C8: Maintain | 2 | 4 | 3 | 3 | V2 simplest design |
| C9: Interop | 3 | 2 | 3 | 3 | V1 proven interfaces |

### Weighted Scores

| Criterion | Weight | V1 | V2 | V3 | V4 |
|-----------|--------|----|----|----|----|
| C1 | 0.15 | 0.60 | 0.30 | 0.45 | 0.45 |
| C2 | 0.10 | 0.30 | 0.20 | 0.30 | 0.30 |
| C3 | 0.15 | 0.15 | 0.45 | 0.45 | 0.60 |
| C4 | 0.10 | 0.10 | 0.40 | 0.30 | 0.30 |
| C5 | 0.10 | 0.10 | 0.30 | 0.20 | 0.40 |
| C6 | 0.15 | 0.15 | 0.60 | 0.45 | 0.45 |
| C7 | 0.15 | 0.15 | 0.60 | 0.45 | 0.60 |
| C8 | 0.05 | 0.10 | 0.20 | 0.15 | 0.15 |
| C9 | 0.05 | 0.15 | 0.10 | 0.15 | 0.15 |
| **TOTAL** | **1.00** | **1.80** | **3.15** | **2.90** | **3.40** |

### Technical Value Calculation

| Concept | Weighted Score | Technical Value | Ranking |
|---------|----------------|-----------------|---------|
| V1: Clone | 1.80 | 45% | 4th |
| V2: Local-First | 3.15 | 79% | 2nd |
| V3: Hybrid | 2.90 | 73% | 3rd |
| **V4: Phased** | **3.40** | **85%** | **1st ✓** |

---

## 6. Sensitivity Analysis

### Test 1: Performance Weight +10%

If C1 (Performance) increases from 15% to 25% (C7 decreases to 5%):

| Concept | New Score | Change | New Rank |
|---------|-----------|--------|----------|
| V1 | 2.20 | +0.40 | 4th |
| V2 | 2.75 | -0.40 | 3rd |
| V3 | 2.90 | ±0.00 | 2nd |
| **V4** | **3.10** | -0.30 | **1st** |

**Result**: V4 still wins. Robust to performance priority increase.

### Test 2: Local Content Weight +10%

If C7 (Local Match) increases from 15% to 25% (C1 decreases to 5%):

| Concept | New Score | Change | New Rank |
|---------|-----------|--------|----------|
| V1 | 1.50 | -0.30 | 4th |
| **V2** | **3.55** | +0.40 | **1st** |
| V3 | 2.90 | ±0.00 | 3rd |
| V4 | 3.50 | +0.10 | 2nd |

**Result**: V2 wins if local content becomes dominant. V4 close second.

### Test 3: All V4 Scores -1 Point

| Concept | New Score | Rank |
|---------|-----------|------|
| V1 | 1.80 | 4th |
| **V2** | **3.15** | **1st** |
| V3 | 2.90 | 2nd |
| V4 | 2.40 | 3rd |

**Result**: V4 falls to 3rd if execution significantly worse than estimated.

### Sensitivity Conclusion

- **V4 is robust winner** under baseline and performance-priority scenarios
- **V2 could win** if local content becomes overwhelming priority OR V4 execution disappoints
- **Recommendation**: Proceed with V4, maintain V2 as fallback

---

## 7. Recommendation

### Selected Approach: V4 - Phased Development

**Technical Value: 85%** (Exceeds 80% threshold for "Good")

### Rationale

1. **Risk Mitigation**: Start with achievable scope, prove capabilities before committing to AI complexity
2. **Capability Growth**: Each phase adds performance while building team expertise
3. **Learning Integration**: Lessons from Phase 1 directly inform Phase 2 design decisions
4. **Budget Alignment**: Spread investment over time, demonstrate value before major spending
5. **Local Expertise Building**: Progressive capability development matches Vietnamese industry growth

### Phase 1 Approach (Months 1-12)

- Classical CV detection (HOG+SVM)
- Kalman filter tracking
- Point-mass ballistics
- Solenoid trigger gate
- **Goal**: Working prototype, collect training data

### Phase 2 Evolution (Months 13-24)

- Upgrade to YOLOv8-nano
- Add thermal option (PRO variant)
- Production preparation
- **Goal**: Production-ready design

### Fallback Plan

If V4 Phase 1 underperforms:
- Simplify to V2 (Local-First)
- Reduce AI complexity
- Focus on mechanical reliability

---

## 8. Approval Record

| Stakeholder | Approval | Date | Notes |
|-------------|----------|------|-------|
| Technical Lead | ☐ Pending | | |
| Program Manager | ☐ Pending | | |
| MoD Representative | ☐ Pending | | |

---

## Related Documents

- [[morphological-matrix]] - Concept variant definitions
- [[requirements/v1.1-summary]] - Requirements driving criteria
- [[decisions/log#DEC-004]] - Concept selection decision
- [[../README]] - Project overview

---

*Evaluation follows VDI 2225 Technical-Economic standard*
*Last updated: 2026-01-26*
