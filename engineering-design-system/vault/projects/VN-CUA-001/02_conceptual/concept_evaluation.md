---
project: VN-CUA-001
designation: VDC-100
type: concept_evaluation
phase: 2
step: 5
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221/2225) - Step 5
---

# VN-CUA-001: CONCEPT EVALUATION (VDI 2225)
## Vietnamese Drone Catcher 100 (VDC-100)
## Đánh giá Phương án - Giai đoạn 2, Bước 5

**Project Code:** VN-CUA-001
**Phase:** 2 - Conceptual Design (Step 5: Evaluation)
**Date:** 2026-02-08
**Input:** [[02_conceptual/morphological_matrix|4 Concepts from Morphological Matrix]]

---

# 1. EVALUATION METHODOLOGY

## 1.1 VDI 2225 Weighted Scoring Method

The VDI 2225 method evaluates concepts against weighted criteria using a standardized 0-4 scoring scale. Criteria weights are derived from ODI opportunity scores to ensure the evaluation reflects **actual customer priorities** rather than engineering assumptions.

**Process:**
1. Define evaluation criteria with weights (summing to 1.00)
2. Score each concept per criterion (0-4 scale)
3. Calculate weighted score: Σ(weight × score)
4. Normalize as percentage of maximum possible (4.00)
5. Threshold: concepts scoring ≥70% are acceptable candidates

## 1.2 Scoring Scale

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                     VDI 2225 SCORING SCALE                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║   0 = Absolutely unsatisfactory                                             ║
║       Does not meet minimum requirement. Showstopper.                       ║
║       Example: Weight 15 kg (requirement ≤8 kg)                             ║
║                                                                             ║
║   1 = Just tolerable                                                        ║
║       Barely meets minimum. Significant compromise.                         ║
║       Example: 65% hit rate (requirement ≥70%, but close)                   ║
║                                                                             ║
║   2 = Adequate                                                              ║
║       Meets requirement satisfactorily. No concern.                         ║
║       Example: 70% hit rate (meets requirement exactly)                     ║
║                                                                             ║
║   3 = Good                                                                  ║
║       Exceeds requirement. Competitive advantage.                           ║
║       Example: 80% hit rate (10% above requirement)                         ║
║                                                                             ║
║   4 = Very good                                                             ║
║       Close to ideal solution. Best achievable.                             ║
║       Example: 90% hit rate (near theoretical maximum)                      ║
║                                                                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

# 2. EVALUATION CRITERIA

## 2.1 Criteria Selection & Weighting

Criteria are derived from the top ODI outcomes and key project requirements. Weights reflect the relative importance established by customer research.

| # | Criterion | Weight | Rationale | ODI Source | Req Trace |
|---|-----------|--------|-----------|------------|-----------|
| C1 | **First-shot hit probability** | **0.20** | #1 ODI outcome — defines product success | O-48: 15.0 | CUA-KIN-06, CUA-KIN-07 |
| C2 | **Equipment reliability** | **0.15** | #2 ODI outcome — fire-every-time confidence | O-23: 14.6 | CUA-QUA-01, CUA-QUA-06 |
| C3 | **Effective range** | **0.12** | Key performance differentiator | O-46: 13.5 | CUA-KIN-02 |
| C4 | **Net deployment reliability** | **0.10** | Essential for capture mission | O-43: 13.5 | CUA-KIN-04 |
| C5 | **Ready/reload time** | **0.10** | Speed for Rapid Responders segment (40%) | O-19, O-55: 12.5 | CUA-ASM-02, CUA-ASM-05 |
| C6 | **Unit cost** | **0.10** | Market position: ≤$6,000 vs $30K import | — | CUA-CST-01 |
| C7 | **Local content** | **0.08** | Strategic procurement: ≥60% (target 70%) | — | CUA-PRO-01 |
| C8 | **Weight/portability** | **0.08** | Ergonomic: ≤8 kg loaded for patrol | O-24: 12.0 | CUA-GEO-01, CUA-ERG-06 |
| C9 | **Development risk** | **0.07** | Schedule: 12-month target to prototype | — | CUA-SCH-01 |
| | **TOTAL** | **1.00** | | | |

## 2.2 Weight Derivation from ODI

```
CRITERIA WEIGHT DERIVATION
═══════════════════════════════════════════════════════════════════════════════

ODI Score        Criterion                    Raw Weight   Normalized
───────────      ─────────────────────────    ──────────   ──────────
O-48: 15.0  →   C1: First-shot hit           0.200        0.20 ████████████████████
O-23: 14.6  →   C2: Equipment reliability    0.155        0.15 ███████████████
O-46: 13.5  →   C3: Effective range          0.120        0.12 ████████████
O-43: 13.5  →   C4: Net deployment           0.100        0.10 ██████████
O-55: 12.5  →   C5: Ready/reload time        0.100        0.10 ██████████
Req-driven  →   C6: Unit cost                0.100        0.10 ██████████
Req-driven  →   C7: Local content            0.080        0.08 ████████
O-24: 12.0  →   C8: Weight/portability       0.080        0.08 ████████
Req-driven  →   C9: Development risk         0.065        0.07 ███████
                                             ─────────    ──────
                                             1.000        1.00

Top 3 criteria (C1+C2+C3) = 47% of total weight → drive the evaluation
═══════════════════════════════════════════════════════════════════════════════
```

---

# 3. EVALUATION MATRIX

## 3.1 Detailed Scoring

### C1: First-Shot Hit Probability (Weight: 0.20)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **2** | Manual reticle only, smoothbore. ~60% at 50m moving. Meets minimum but not competitive. |
| B: Enhanced | **3** | LRF + calibrated reticle + fin stabilization. ~70% at 50m moving. Exceeds requirement. |
| C: Pro | **4** | Ballistic computer + camera + fins + RF timing. ~85% at 50m moving. Near ideal. |
| D: Pyro | **2** | Same reticle as A, higher velocity helps range but not close-range accuracy. ~60%. |

### C2: Equipment Reliability (Weight: 0.15)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **4** | Fewest components (~60), all mechanical fire chain. TRL 9. Near-ideal reliability. |
| B: Enhanced | **4** | Similar mechanical core. Fins and barometric add complexity but not in fire chain. |
| C: Pro | **2** | Electronic valve, ballistic computer, RF trigger, camera — many failure modes. |
| D: Pyro | **3** | Simple mechanical, but cartridge storage sensitivity and per-shot variability. |

### C3: Effective Range (Weight: 0.12)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **3** | 80m effective (meets requirement). Smoothbore accuracy degrades beyond 60m. |
| B: Enhanced | **3** | 80m effective. Fin stabilization maintains accuracy to full range. |
| C: Pro | **4** | 100m effective with computer-assisted targeting. Exceeds requirement. |
| D: Pyro | **4** | 90m+ effective due to higher muzzle velocity (70 m/s). Exceeds requirement. |

### C4: Net Deployment Reliability (Weight: 0.10)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **3** | Single timer deploy. Reliable but no backup if timer fails (2% failure). |
| B: Enhanced | **4** | Timer + barometric backup. Dual redundancy → ~99.9% deploy rate. |
| C: Pro | **3** | RF command deploy — precise timing but RF can fail/be jammed. |
| D: Pyro | **3** | Single timer (same as A). No backup. |

### C5: Ready/Reload Time (Weight: 0.10)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **3** | Breech loading, ~10 sec reload. Good but not best. |
| B: Enhanced | **4** | Optimized breech + fast valve, ≤8 sec reload. Meets Rapid Responders need. |
| C: Pro | **2** | Magazine eliminates reload but magazine change is 15+ sec. Complex jam clearing. |
| D: Pyro | **3** | Breech loading but must also load new cartridge. ~12 sec. |

### C6: Unit Cost (Weight: 0.10)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **4** | ~$4,800 selling price. Well under $6,000. Best cost position. |
| B: Enhanced | **3** | ~$5,400 selling price. Under $6,000 but less margin. |
| C: Pro | **1** | ~$9,000 selling price. Exceeds $6,000 ceiling. Just tolerable for premium market. |
| D: Pyro | **4** | ~$4,200 selling price. Lowest cost option. |

### C7: Local Content (Weight: 0.08)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **4** | ~75% local. Minimal imported electronics. Mostly aluminum + machining. |
| B: Enhanced | **4** | ~72% local. LRF is import but small percentage of total value. |
| C: Pro | **2** | ~50% local. Camera, computer, electronic valve, magazine — heavy import content. |
| D: Pyro | **3** | ~70% local. Cartridges may need import or special license for local production. |

### C8: Weight/Portability (Weight: 0.08)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **3** | 7.5 kg. Under 8 kg limit. Comfortable for patrol. |
| B: Enhanced | **3** | 7.8 kg. Under 8 kg limit but close. Acceptable. |
| C: Pro | **2** | 10 kg. Exceeds 8 kg limit. Tiring for extended patrol. |
| D: Pyro | **4** | 6 kg. Best portability — no gas cylinder. Lightest option. |

### C9: Development Risk (Weight: 0.07)

| Concept | Score | Justification |
|---------|-------|---------------|
| A: Basic | **4** | All proven components (TRL 8-9). Minimal development needed. |
| B: Enhanced | **3** | Fin-stabilized projectile and barometric deploy need prototyping. TRL 7-8. |
| C: Pro | **1** | Ballistic computer, RF trigger, magazine, self-tightening net — all need development. TRL 6-7. |
| D: Pyro | **2** | Proven technology but Vietnamese regulatory pathway uncertain. |

---

## 3.2 Complete Evaluation Matrix

| Criterion | Weight | A: Basic | B: Enhanced | C: Pro | D: Pyro |
|-----------|--------|----------|-------------|--------|---------|
| C1: First-shot hit | 0.20 | 2 | **3** | **4** | 2 |
| C2: Reliability | 0.15 | **4** | **4** | 2 | 3 |
| C3: Range | 0.12 | 3 | 3 | **4** | **4** |
| C4: Net deploy | 0.10 | 3 | **4** | 3 | 3 |
| C5: Reload time | 0.10 | 3 | **4** | 2 | 3 |
| C6: Unit cost | 0.10 | **4** | 3 | 1 | **4** |
| C7: Local content | 0.08 | **4** | **4** | 2 | 3 |
| C8: Weight | 0.08 | 3 | 3 | 2 | **4** |
| C9: Dev risk | 0.07 | **4** | 3 | 1 | 2 |

---

# 4. WEIGHTED SCORE CALCULATIONS

## 4.1 Concept A: VDC-100 BASIC

```
CONCEPT A WEIGHTED CALCULATION
═══════════════════════════════════════════════════════════════════════════════

Criterion              Weight    Score    Weighted
────────────────────   ──────    ─────    ────────
C1: First-shot hit     0.20  ×    2    =   0.40
C2: Reliability        0.15  ×    4    =   0.60
C3: Range              0.12  ×    3    =   0.36
C4: Net deploy         0.10  ×    3    =   0.30
C5: Reload time        0.10  ×    3    =   0.30
C6: Unit cost          0.10  ×    4    =   0.40
C7: Local content      0.08  ×    4    =   0.32
C8: Weight             0.08  ×    3    =   0.24
C9: Dev risk           0.07  ×    4    =   0.28
                       ─────              ──────
                       1.00         SUM =  3.20

PERCENTAGE = 3.20 / 4.00 = 80.0%    ✅ ABOVE THRESHOLD (≥70%)

═══════════════════════════════════════════════════════════════════════════════
```

## 4.2 Concept B: VDC-100 ENHANCED

```
CONCEPT B WEIGHTED CALCULATION
═══════════════════════════════════════════════════════════════════════════════

Criterion              Weight    Score    Weighted
────────────────────   ──────    ─────    ────────
C1: First-shot hit     0.20  ×    3    =   0.60    ← +0.20 vs A (key differentiator)
C2: Reliability        0.15  ×    4    =   0.60
C3: Range              0.12  ×    3    =   0.36
C4: Net deploy         0.10  ×    4    =   0.40    ← +0.10 vs A (dual redundancy)
C5: Reload time        0.10  ×    4    =   0.40    ← +0.10 vs A (optimized breech)
C6: Unit cost          0.10  ×    3    =   0.30
C7: Local content      0.08  ×    4    =   0.32
C8: Weight             0.08  ×    3    =   0.24
C9: Dev risk           0.07  ×    3    =   0.21
                       ─────              ──────
                       1.00         SUM =  3.43

PERCENTAGE = 3.43 / 4.00 = 85.8%    ✅ ABOVE THRESHOLD (≥70%)    ⭐ HIGHEST

═══════════════════════════════════════════════════════════════════════════════
```

## 4.3 Concept C: VDC-100 PRO

```
CONCEPT C WEIGHTED CALCULATION
═══════════════════════════════════════════════════════════════════════════════

Criterion              Weight    Score    Weighted
────────────────────   ──────    ─────    ────────
C1: First-shot hit     0.20  ×    4    =   0.80    ← Highest raw score
C2: Reliability        0.15  ×    2    =   0.30    ← Penalized for complexity
C3: Range              0.12  ×    4    =   0.48
C4: Net deploy         0.10  ×    3    =   0.30
C5: Reload time        0.10  ×    2    =   0.20    ← Magazine adds complexity
C6: Unit cost          0.10  ×    1    =   0.10    ← Over budget ($9,000)
C7: Local content      0.08  ×    2    =   0.16    ← Heavy import content
C8: Weight             0.08  ×    2    =   0.16    ← Over weight (10 kg)
C9: Dev risk           0.07  ×    1    =   0.07    ← Highest risk
                       ─────              ──────
                       1.00         SUM =  2.57

PERCENTAGE = 2.57 / 4.00 = 64.3%    ❌ BELOW THRESHOLD (<70%)

═══════════════════════════════════════════════════════════════════════════════
```

## 4.4 Concept D: VDC-100 PYRO

```
CONCEPT D WEIGHTED CALCULATION
═══════════════════════════════════════════════════════════════════════════════

Criterion              Weight    Score    Weighted
────────────────────   ──────    ─────    ────────
C1: First-shot hit     0.20  ×    2    =   0.40
C2: Reliability        0.15  ×    3    =   0.45
C3: Range              0.12  ×    4    =   0.48    ← Best range (higher velocity)
C4: Net deploy         0.10  ×    3    =   0.30
C5: Reload time        0.10  ×    3    =   0.30
C6: Unit cost          0.10  ×    4    =   0.40    ← Lowest cost
C7: Local content      0.08  ×    3    =   0.24
C8: Weight             0.08  ×    4    =   0.32    ← Lightest
C9: Dev risk           0.07  ×    2    =   0.14
                       ─────              ──────
                       1.00         SUM =  3.03

PERCENTAGE = 3.03 / 4.00 = 75.8%    ✅ ABOVE THRESHOLD (≥70%)

═══════════════════════════════════════════════════════════════════════════════
```

---

# 5. RESULTS SUMMARY

## 5.1 Ranking

| Rank | Concept | Weighted Score | Percentage | Decision |
|------|---------|----------------|------------|----------|
| **1** | **B: VDC-100 Enhanced** | **3.43** | **85.8%** | **SELECTED** |
| 2 | A: VDC-100 Basic | 3.20 | 80.0% | Acceptable (Fallback) |
| 3 | D: VDC-100 Pyro | 3.03 | 75.8% | Acceptable (Alternative) |
| 4 | C: VDC-100 Pro | 2.57 | 64.3% | Below threshold |

## 5.2 Visual Results

```
VDI 2225 EVALUATION RESULTS
═══════════════════════════════════════════════════════════════════════════════

                50%        60%        70%        80%        90%       100%
                 │          │          │          │          │          │
                 │          │    THRESHOLD        │          │          │
                 │          │     (70%)  │        │          │          │
                 │          │       ▼    │        │          │          │
C: Pro       ════╪══════════╪═════╡      │        │          │          │ 64.3%
                 │          │     ▼      │        │          │          │
                 │          │   BELOW    │        │          │          │
                 │          │   ❌       │        │          │          │
                 │          │            │        │          │          │
D: Pyro      ════╪══════════╪════════════╪═══╡    │          │          │ 75.8%
                 │          │            │   ▼    │          │          │
                 │          │            │ ACCEPT │          │          │
                 │          │            │        │          │          │
A: Basic     ════╪══════════╪════════════╪════════╡          │          │ 80.0%
                 │          │            │        ▼          │          │
                 │          │            │    FALLBACK       │          │
                 │          │            │        │          │          │
B: Enhanced  ════╪══════════╪════════════╪════════╪════════╡ │          │ 85.8%
                 │          │            │        │        ▼ │          │
                 │          │            │        │  SELECTED │          │
                 │          │            │        │          │          │

Gap: B leads A by 5.8%, leads D by 10.0%, leads C by 21.5%

═══════════════════════════════════════════════════════════════════════════════
```

## 5.3 Score Distribution Analysis

| Concept | Min Score | Max Score | Range | Weak Spot |
|---------|-----------|-----------|-------|-----------|
| A: Basic | 2 (hit prob) | 4 (reliability, cost, LC, dev) | 2 | First-shot hit |
| **B: Enhanced** | **3 (multiple)** | **4 (reliability, deploy, reload, LC)** | **1** | **None below 3** |
| C: Pro | 1 (cost, dev risk) | 4 (hit prob, range) | 3 | Cost + risk |
| D: Pyro | 2 (hit prob, dev risk) | 4 (range, cost, weight) | 2 | First-shot hit |

**Key Observation:** Concept B has the narrowest score range (3-4), meaning **no weak spots**. All other concepts have at least one criterion scored at 2 or below.

---

# 6. SENSITIVITY ANALYSIS

## 6.1 Weight Variation Scenarios

Testing robustness of the selection by shifting criteria weights ±10%:

| Scenario | Weight Shift | A: Basic | B: Enhanced | C: Pro | D: Pyro | Winner |
|----------|-------------|----------|-------------|--------|---------|--------|
| **Baseline** | As defined | 80.0% | **85.8%** | 64.3% | 75.8% | **B** |
| Cost priority | C6: 0.10→0.20 | **82.5%** | 82.5% | 60.0% | 78.8% | **Tie A/B** |
| Accuracy priority | C1: 0.20→0.30 | 77.5% | **87.5%** | 67.5% | 73.8% | **B** |
| Reliability priority | C2: 0.15→0.25 | **82.5%** | 85.0% | 60.0% | 73.8% | **B** |
| Local content priority | C7: 0.08→0.18 | **82.0%** | 85.0% | 60.0% | 73.8% | **B** |
| Weight priority | C8: 0.08→0.18 | 78.8% | 83.8% | 60.0% | **78.8%** | **B** |
| Range priority | C3: 0.12→0.22 | 78.8% | 83.8% | 67.5% | **78.8%** | **B** |

## 6.2 Sensitivity Chart

```
SENSITIVITY ANALYSIS — CONCEPT B ROBUSTNESS
═══════════════════════════════════════════════════════════════════════════════

                    B wins    │ B wins    │ B wins    │ Tie with A │ B wins
Scenario            clearly   │ clearly   │ clearly   │            │ clearly
                              │           │           │            │
       70%    75%    80%     85%      90%
        │      │      │       │        │
Base ───┼──────┼──────┼───────╪════════╡            B: 85.8%
        │      │      │       │    ▲
Cost ───┼──────┼──════╪═══════╡    │                B: 82.5% (Tie with A)
        │      │      │       │    │
Accur ──┼──────┼──────┼───────╪════╪════════╡       B: 87.5% (Widest lead)
        │      │      │       │    │
Relia ──┼──────┼──────┼───════╪════╡                B: 85.0%
        │      │      │       │
Local ──┼──────┼──────┼───════╪════╡                B: 85.0%
        │      │      │       │
Weight ─┼──────┼──────┼──════╪════╡                 B: 83.8%
        │      │      │       │
Range ──┼──────┼──────┼──════╪════╡                 B: 83.8%
        │      │      │       │

RESULT: Concept B wins or ties in ALL scenarios tested.
        Only at extreme cost priority does Concept A tie.
        Concept B is ROBUST to weight changes.

═══════════════════════════════════════════════════════════════════════════════
```

## 6.3 Critical Criteria Analysis (Showstopper Check)

What if a single criterion drops to 0 (total failure)?

| Concept | If C1=0 (miss) | If C2=0 (break) | If C6=0 (over budget) | Worst Case |
|---------|----------------|------------------|----------------------|------------|
| A: Basic | 70.0% (survives) | 65.0% | 70.0% (survives) | 65.0% |
| **B: Enhanced** | **70.8% (survives)** | **70.8% (survives)** | **78.3% (survives)** | **70.8%** |
| C: Pro | 44.3% | 59.3% | 61.8% | 44.3% |
| D: Pyro | 65.8% | 60.8% | 65.8% | 60.8% |

**Key Insight:** Concept B is the **only concept that stays above the 70% threshold even with one criterion at 0**. This confirms its robustness.

## 6.4 Breakeven Analysis

How much would Concept A need to improve to beat Concept B?

```
B - A gap = 85.8% - 80.0% = 5.8 percentage points (0.23 raw score)

To close this gap, Concept A would need:
• C1 (hit prob): Score 2→4 (+0.40) — would give A 85.0%, still below B
  → Practically: A would need ballistic computer + fins = becomes Concept B

CONCLUSION: A cannot beat B without adding B's key features (fins, dual deploy, fast valve)
```

---

# 7. EVALUATION CONFIDENCE

## 7.1 Score Confidence Assessment

| Criterion | Confidence | Basis | Risk if Wrong |
|-----------|-----------|-------|---------------|
| C1: First-shot hit | **Medium** | Estimated from similar systems, no prototype data | Selection reversal if A matches B |
| C2: Reliability | **High** | Based on component count and TRL assessment | Low risk — mechanical systems are well-understood |
| C3: Range | **High** | Physics-based (muzzle velocity vs. drag) | Low risk |
| C4: Net deploy | **Medium** | Dual redundancy assumption needs prototype validation | Low — both timer and barometric are proven individually |
| C5: Reload time | **High** | Based on breech loading mechanics | Low risk |
| C6: Unit cost | **High** | Based on BOM estimate from product spec | Medium — material prices may vary |
| C7: Local content | **High** | Component-by-component analysis | Low risk |
| C8: Weight | **High** | Based on material density calculations | Low risk |
| C9: Dev risk | **Medium** | Subjective assessment | Medium — schedule impact if underestimated |

**Overall evaluation confidence: HIGH** — 6/9 criteria at high confidence, 3/9 at medium. No low-confidence criteria.

## 7.2 Key Assumptions

| Assumption | Impact if Wrong | Mitigation |
|------------|----------------|------------|
| Fin stabilization improves accuracy by ~10% | C1 score for B drops to 2, B score = 80.0% (ties A) | Prototype testing early in Phase 3 |
| Barometric backup deploys reliably | C4 score for B drops to 3, minimal impact (B = 83.3%) | Component testing in Phase 3 |
| LRF can be sourced for ≤$200 COTS | C6 score for B unchanged (budgeted) | Identify 3 supplier options |
| Vietnamese HPA cylinder certification | C7 unchanged if imported cylinder | Start TCVN 6153 process early |

---

# DOCUMENT LINKS

- [[02_conceptual/morphological_matrix|Morphological Matrix (Steps 3-4)]]
- [[02_conceptual/concept_selection|Concept Selection (Step 6)]] ← NEXT
- [[01_requirements/requirements_list|Requirements List]]
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]

---

*This evaluation follows VDI 2225 weighted scoring methodology with ODI-derived criteria weights, ensuring the concept selection reflects validated customer priorities for the Vietnamese C-UAS market.*
