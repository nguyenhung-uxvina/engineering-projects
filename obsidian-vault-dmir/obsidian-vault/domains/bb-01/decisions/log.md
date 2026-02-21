# BB-01 Decision Log

> **Project**: VN-TARGET-BB01 LOMAH
> **Last Updated**: 2026-01-26

---

## Decision Index

| ID | Date | Decision | Status |
|----|------|----------|--------|
| DEC-001 | 2026-01-26 | Acoustic Sensor: ECM over MEMS | ✅ Approved |
| DEC-002 | 2026-01-26 | MTBF Improvement: Combined approach | ✅ Approved |

---

## DEC-001: Acoustic Sensor Selection

| Field | Value |
|-------|-------|
| **Date** | 2026-01-26 |
| **Status** | ✅ Approved |
| **Owner** | Design Lead |

### Context
BB-01 cần chọn microphone cho acoustic hit detection. Hai options: MEMS vs Electret (ECM).

### Decision
**Chọn ECM (Electret Condenser Microphone)**

### Rationale
1. IP67 marine protection dễ hơn (không cần membrane)
2. Local availability tại Việt Nam (Nhật Tảo)
3. Cost-effective ($1.50-2.80 vs MEMS + membrane)
4. 120 dB AOP đủ cho range 150-400m
5. Proven reliability trong outdoor/marine applications

### Recommended Part
**PUI Audio AOM-5024L-HD-F-R** ($2.50/unit)

### Related
- [[acoustic-sensor-research]] - Full D-M-I-R analysis
- [[acoustic-sensor-summary]] - Executive summary

---

## DEC-002: MTBF Improvement Approach

| Field | Value |
|-------|-------|
| **Date** | 2026-01-26 |
| **Status** | ✅ Approved |
| **Owner** | Design Lead |

### Context
DfX review phát hiện MTBF 365 hrs < 500 hrs requirement (MT.01). Cần improvement plan.

### Decision
**Combined approach (A+B+C+D)**

| Improvement | Impact | Cost |
|-------------|--------|------|
| A: IP68 gold connectors | -480 FIT | +$15 |
| B: Reduce to 5 connectors | -240 FIT | -$3 |
| C: Add backup mic (6th) | -100 FIT | +$2.50 |
| D: Conformal coating | -100 FIT | +$3 |
| **TOTAL** | **-920 FIT** | **+$16.50** |

### Result
- Before: 365 hrs
- After: 551 hrs ✅
- Margin: +51 hrs (10%)

### Rationale
1. Pareto: Connectors (44%) + Mics (37%) = 81% of failures
2. Combined approach đạt target với margin
3. Cost increase 15.7% justified by 51% reliability improvement

### Trade-offs Considered
- Option: Integrate mics to PCB (-50% connectors)
- Rejected: Bigger design change, longer timeline

### Related
- [[MTBF-Improvement-Plan]] - Full implementation plan
- [[DfX-Review-MCU-Box]] - Original analysis
- [[DfX-Dashboard]] - Issue tracking

---

*Decision log per Workshop X 3-Gate Quality System*
