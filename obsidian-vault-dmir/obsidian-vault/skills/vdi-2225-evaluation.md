# Skill: VDI 2225 Concept Evaluation

> **Use When**: Comparing design concepts systematically
> **Output**: Ranked concept list with technical value scores

---

## 🎯 Purpose

Apply VDI 2225 methodology to:
1. Define evaluation criteria from requirements
2. Weight criteria by stakeholder importance
3. Score concepts objectively
4. Select best concept with documented rationale

---

## 🔄 VDI 2225 Process

```
┌─────────────────────────────────────────────────────────┐
│                  VDI 2225 EVALUATION                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. DEFINE CRITERIA ──────► From requirements            │
│       │                                                  │
│       ▼                                                  │
│  2. WEIGHT CRITERIA ──────► Stakeholder priorities       │
│       │                     (AHP or pairwise comparison) │
│       ▼                                                  │
│  3. DEFINE SCALE ─────────► 0-4 scoring definitions      │
│       │                                                  │
│       ▼                                                  │
│  4. SCORE CONCEPTS ───────► Each concept × each criterion│
│       │                                                  │
│       ▼                                                  │
│  5. CALCULATE VALUE ──────► Technical Value = Σ(w×s)/max │
│       │                                                  │
│       ▼                                                  │
│  6. SENSITIVITY TEST ─────► Check robustness             │
│       │                                                  │
│       ▼                                                  │
│  7. DECIDE ───────────────► Select concept ≥70%          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 VDI 2225 Evaluation Template

```markdown
# VDI 2225 Evaluation: [Project Name]

**Date**: YYYY-MM-DD
**Evaluator(s)**: [Names]
**Number of Concepts**: [N]

---

## 1. Concepts Being Evaluated

| ID | Concept | Description | Origin |
|----|---------|-------------|--------|
| V1 | [Name] | [Brief description] | [Source] |
| V2 | [Name] | [Brief description] | [Source] |
| V3 | [Name] | [Brief description] | [Source] |

---

## 2. Evaluation Criteria

### Criteria Definition
| ID | Criterion | Source Requirement | Rationale |
|----|-----------|-------------------|-----------|
| C1 | [Criterion name] | R[XX] | [Why important] |
| C2 | [Criterion name] | R[XX] | [Why important] |
| ... | | | |

### Weight Derivation (AHP Method)

**Pairwise Comparison Matrix**
Scale: 2 = much more important, 1 = slightly more, 0.5 = equal, 0 = less

|    | C1 | C2 | C3 | C4 | Sum |
|----|----|----|----|----|-----|
| C1 | -  |    |    |    |     |
| C2 |    | -  |    |    |     |
| C3 |    |    | -  |    |     |
| C4 |    |    |    | -  |     |

**Derived Weights**
| Criterion | Raw Score | Weight | Rounded |
|-----------|-----------|--------|---------|
| C1 | | | % |
| C2 | | | % |
| ... | | | |
| **Total** | | | **100%** |

---

## 3. Scoring Scale Definition

| Score | Definition | Example |
|-------|------------|---------|
| 0 | Completely inadequate | Fails requirement |
| 1 | Very poor | Major gaps |
| 2 | Poor | Significant issues |
| 3 | Adequate | Meets minimum |
| 4 | Good | Solid performance |

---

## 4. Evaluation Matrix

### Raw Scores (0-4)

| Criterion | Weight | V1 | V2 | V3 | Scoring Rationale |
|-----------|--------|----|----|----|--------------------|
| C1 | | | | | [Why these scores] |
| C2 | | | | | [Why these scores] |
| ... | | | | | |

### Weighted Scores

| Criterion | Weight | V1 | V2 | V3 |
|-----------|--------|----|----|-----|
| C1 | w1 | w1×s1 | w1×s1 | w1×s1 |
| C2 | w2 | w2×s2 | w2×s2 | w2×s2 |
| ... | | | | |
| **TOTAL** | **1.00** | **Σ** | **Σ** | **Σ** |

### Technical Value Calculation

| Concept | Weighted Score | Technical Value (÷4×100) | Rank |
|---------|----------------|--------------------------|------|
| V1 | | % | |
| V2 | | % | |
| V3 | | % | |

---

## 5. Sensitivity Analysis

### Test 1: [Criterion X] Weight +10%
| Concept | New Score | Change | New Rank |
|---------|-----------|--------|----------|
| V1 | | | |
| V2 | | | |
| V3 | | | |

**Result**: [Is winner still winner?]

### Test 2: All [Winner] Scores -1
| Concept | New Score | New Rank |
|---------|-----------|----------|
| V1 | | |
| V2 | | |
| V3 | | |

**Result**: [How robust is the selection?]

---

## 6. Recommendation

### Selected Concept: [V#]

**Technical Value**: [X]%
**Threshold**: ≥70% = Good, ≥80% = Very Good

### Rationale
1. [Primary reason for selection]
2. [Secondary reason]
3. [Tertiary reason]

### Risks of Selected Concept
| Risk | Mitigation |
|------|------------|
| | |

### Fallback Concept: [V#]
If selected concept fails during development, fall back to [V#] because [reason].

---

## 7. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Technical Lead | | | |
| Program Manager | | | |

---

*Evaluation follows VDI 2225 standard*
```

---

## ⚡ Quick Evaluation (3 concepts, 5 criteria)

```markdown
# Quick VDI 2225: [Project]

## Concepts
- V1: [Name]
- V2: [Name]  
- V3: [Name]

## Criteria & Weights
| Criterion | Weight |
|-----------|--------|
| Performance | 25% |
| Cost | 20% |
| Local Content | 20% |
| Development Risk | 20% |
| Schedule | 15% |

## Scores (0-4)
| Criterion | V1 | V2 | V3 |
|-----------|----|----|-----|
| Performance | | | |
| Cost | | | |
| Local Content | | | |
| Dev Risk | | | |
| Schedule | | | |

## Result
| Concept | Score | Value | Rank |
|---------|-------|-------|------|
| V1 | | % | |
| V2 | | % | |
| V3 | | % | |

**Selected**: V[#] at [X]%
```

---

## 💡 VDI 2225 Tips

1. **Criteria from requirements** - Don't invent criteria, derive from requirements list
2. **Weight before scoring** - Prevents bias toward favorite concept
3. **Score independently** - Multiple evaluators, then compare
4. **Document rationale** - Why each score, not just the number
5. **Sensitivity test** - Check if winner is robust to weight changes
6. **Threshold = 70%** - Below this, reconsider all concepts

---

## 📊 Common Evaluation Criteria

### Technical Criteria
- Performance (meets specs)
- Reliability (MTBF, robustness)
- Technology readiness
- Integration complexity

### Economic Criteria
- Development cost
- Production cost
- Operating cost
- Investment required

### Strategic Criteria
- Local content
- Supply chain risk
- IP/export considerations
- Future extensibility

### Schedule Criteria
- Development time
- Time to market
- Risk to schedule

---

## 🔗 Integration with Pahl & Beitz

VDI 2225 fits into systematic design:

```
Requirements List ──► Function Structure ──► Morphological Matrix
                                                    │
                                                    ▼
                                            Concept Variants
                                                    │
                                                    ▼
                                          ┌─────────────────┐
                                          │  VDI 2225       │
                                          │  Evaluation     │
                                          └────────┬────────┘
                                                   │
                                                   ▼
                                          Selected Concept ──► Embodiment
```

---

*Skill Version: 1.0*
*Based on VDI 2225 Technical-Economic Evaluation*
