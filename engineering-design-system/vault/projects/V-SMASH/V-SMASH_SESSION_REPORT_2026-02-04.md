# V-SMASH SESSION REPORT
## Phase 0 ODI Revision & Two-Tier Product Strategy

**Date:** 2026-02-04
**Session Type:** ODI Revision, Requirements Update, Strategy Decision
**Project:** V-SMASH (12.7mm C-UAS Fire Control System)
**Prepared By:** Engineering Design System

---

## EXECUTIVE SUMMARY

This session revised the V-SMASH Phase 0 ODI (Outcome-Driven Innovation) analysis based on insights gained during Phase 2 conceptual design. Five new HIGH-opportunity outcomes were identified, leading to seven new requirements. Re-evaluation of Concept C (V4: Phased Build) against expanded requirements resulted in approval of a **two-tier product strategy** with V-SMASH-LITE and V-SMASH-PRO variants.

### Key Decisions

| Decision | Outcome |
|----------|---------|
| ODI Revision | +5 outcomes from Phase 2 design challenges |
| Requirements Update | +7 requirements, 2 upgraded |
| Concept Re-evaluation | V4 score dropped 85% → 69% |
| Strategy Approval | **Two-tier product line (LITE + PRO)** |

### Business Impact

| Metric | Before | After |
|--------|--------|-------|
| Product Variants | 1 | **2** |
| Price Range | $3,000 | **$3,000 - $5,000** |
| Addressable Market | ~1,500 units | **~2,300 units** |
| 5-Year Revenue Potential | ~$4.5M | **~$8.5M** |

---

## 1. ODI ANALYSIS CHANGES

### 1.1 New Outcomes Added

Five new HIGH-opportunity outcomes were identified from Phase 2 design challenges:

| ID | Job Step | Outcome Statement | Imp | Sat | Opp | Priority |
|----|----------|-------------------|-----|-----|-----|----------|
| S1-22 | Locate | Maximize night/low-light acquisition capability | 9.0 | 3.8 | **14.2** | HIGH |
| S1-16 | Execute | Minimize false positive rate (non-threats as targets) | 8.5 | 3.5 | **13.5** | HIGH |
| S1-19 | Execute | Minimize effect of environmental conditions on tracking | 8.6 | 4.0 | **13.2** | HIGH |
| S1-24 | Execute | Maximize effectiveness against evasive maneuvers | 8.5 | 4.0 | **13.0** | HIGH |
| S1-17 | Execute | Maximize detection reliability in varying light | 8.4 | 4.0 | **12.8** | HIGH |

### 1.2 Updated Opportunity Landscape

```
OPPORTUNITY DISTRIBUTION (v1.1)
═══════════════════════════════════════════
Category          Before    After    Change
───────────────────────────────────────────
EXTREME (>15)        2         2        —
HIGH (12-15)         5        10       +5
MODERATE (10-12)     3         3        —
LOW (<10)            5         5        —
───────────────────────────────────────────
TOTAL               15        20       +5
```

### 1.3 Design Implications

| Outcome | Design Implication | Cost Impact |
|---------|-------------------|-------------|
| S1-22 (Night) | Thermal sensor required | +$800-1,500 |
| S1-16 (False Positive) | Enhanced AI training, confidence thresholds | +$0 (software) |
| S1-19 (Environmental) | IP67 sealing, lens heater | +$50-90 |
| S1-24 (Evasive) | IMM filter algorithm | +$0 (software) |
| S1-17 (Varying Light) | HDR sensor upgrade | +$50-100 |

---

## 2. REQUIREMENTS CHANGES

### 2.1 Summary Statistics

| Metric | v1.0 | v1.1 | Change |
|--------|------|------|--------|
| Total Requirements | 57 | 64 | +7 |
| Demands (D) | 43 | 51 | +8 |
| Wishes (W) | 14 | 13 | -1 |
| Quantification Level | 75.4% | 79.7% | +4.3% |

### 2.2 Requirements Modified

| ID | Requirement | Before | After | ODI Source |
|----|-------------|--------|-------|------------|
| R06 | Night operation capability | W (optional) | **D (mandatory)** | S1-22 |
| R14 | Dust/water protection | IP65 | **IP67** | S1-19 |

### 2.3 Requirements Added

| ID | Category | Requirement | D/W | Value | ODI Source |
|----|----------|-------------|-----|-------|------------|
| R58 | Performance | False positive rate | D | <5% | S1-16 |
| R59 | Performance | Detection in varying light | D | 95% @ 1k-50k lux | S1-17 |
| R60 | Performance | Evasive maneuver tracking | D | 3g turn | S1-24 |
| R61 | Sensor | HDR capability | D | ≥80 dB | S1-17 |
| R62 | Sensor | Thermal sensor | D | LWIR, NETD <50mK | S1-22 |
| R63 | Environmental | Lens anti-fog | D | Heater/coating | S1-19 |
| R64 | Environmental | Lens protection | W | Wiper/cover | S1-19 |

---

## 3. CONCEPT RE-EVALUATION

### 3.1 VDI 2225 Score Impact

Original V4 (Phased Build) was evaluated against 57 requirements and scored **85%**.

Re-evaluation against 64 requirements (including 7 new ODI-driven requirements):

| Criterion | Weight | Original | Revised | Impact |
|-----------|--------|----------|---------|--------|
| C1: Performance | 15% | 3 | 2 | Night/HDR gap |
| C2: Reliability | 10% | 3 | 3 | — |
| C3: Dev Cost | 15% | 4 | 3 | +$900-1,690/unit |
| C4: Prod Cost | 10% | 3 | 2 | Thermal cost |
| C5: Dev Time | 10% | 4 | 3 | Thermal complexity |
| C6: Supply Chain | 15% | 3 | 3 | — |
| C7: Local Match | 15% | 4 | 3 | Thermal is import |
| C8: Maintainability | 5% | 3 | 3 | — |
| C9: Interoperability | 5% | 3 | 3 | — |
| **TOTAL** | **100%** | **85%** | **69%** | **-16%** |

### 3.2 Gap Analysis

| Requirement | V4 Phase 1 | V4 Phase 2 | Gap Severity |
|-------------|------------|------------|--------------|
| R06 (Night) | ❌ | ✅ | **CRITICAL** |
| R14 (IP67) | ⚠️ IP65 | ✅ | Medium |
| R58 (False Pos) | ⚠️ ~10% | ✅ <5% | Medium |
| R59 (Vary Light) | ⚠️ ~85% | ✅ 95% | Medium |
| R60 (Evasive) | ❌ 1.5g | ✅ 3g | High |
| R61 (HDR) | ❌ 65dB | ✅ 80dB | Medium |
| R62 (Thermal) | ❌ | ✅ | **CRITICAL** |
| R63 (Anti-fog) | ❌ | ✅ | Low |

---

## 4. TWO-TIER PRODUCT STRATEGY

### 4.1 Decision Rationale

Original V4 score (69%) fell below the 70% acceptance threshold. Four options were considered:

| Option | Description | Outcome |
|--------|-------------|---------|
| A | Accept V4 with lower score | Rejected |
| B | Move thermal to Phase 1 | Rejected (cost/risk) |
| **C** | **Two-tier product strategy** | **APPROVED** |
| D | Re-evaluate alternatives | Rejected (schedule) |

### 4.2 Approved Product Variants

```
┌─────────────────────────────────────────────────────────────────────┐
│                    V-SMASH PRODUCT LINE                             │
├─────────────────────────────┬───────────────────────────────────────┤
│       V-SMASH-LITE          │           V-SMASH-PRO                 │
├─────────────────────────────┼───────────────────────────────────────┤
│ VDI Score: 88%              │ VDI Score: 79%                        │
│ Target Price: $3,000        │ Target Price: $4,500-5,000            │
│ Delivery: Month 12          │ Delivery: Month 24                    │
│ Unit Cost: $784             │ Unit Cost: $1,895                     │
├─────────────────────────────┼───────────────────────────────────────┤
│ SPECIFICATIONS              │ SPECIFICATIONS                        │
│ • CMOS sensor (65dB)        │ • CMOS HDR (85dB) + Thermal LWIR      │
│ • Daylight operation        │ • 24/7 operation (200m night)         │
│ • IP65 sealing              │ • IP67 sealing                        │
│ • Kalman tracking (1.5g)    │ • IMM tracking (3g)                   │
│ • False positive <10%       │ • False positive <5%                  │
│ • Weight <1.2 kg            │ • Weight <1.5 kg                      │
│ • Battery 8+ hours          │ • Battery 6+ hours                    │
│ • NV clip-on compatible     │ • Integrated thermal                  │
│ • Local content: 70%        │ • Local content: 31%*                 │
├─────────────────────────────┼───────────────────────────────────────┤
│ TARGET MARKET               │ TARGET MARKET                         │
│ • Training units            │ • Front-line infantry                 │
│ • Reserve forces            │ • Special operations                  │
│ • Cost-sensitive export     │ • Vehicle-mounted (MTB-20)            │
│ • Paramilitary/police       │ • Capability-driven export            │
├─────────────────────────────┼───────────────────────────────────────┤
│ Est. Volume (5-yr): 1,500   │ Est. Volume (5-yr): 800               │
│ Est. Revenue: $4.5M         │ Est. Revenue: $4.0M                   │
└─────────────────────────────┴───────────────────────────────────────┘
*Local content waiver requested for PRO due to thermal sensor import
```

### 4.3 Development Timeline

```
MONTH  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
       ├──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┼──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┤
LITE   ═══════════════════════════════════▶ DELIVERY (Month 12)
       │  Core Dev  │ Integration │  Test  │

PRO    ─────────────────────────────────────═══════════════════════════════▶
                                   │Thermal│  IMM  │Integration│Test│DELIVERY
                                                                    (Month 24)
```

---

## 5. COST ANALYSIS

### 5.1 Unit Cost Comparison

| Component | LITE | PRO | Delta |
|-----------|------|-----|-------|
| Processing (Jetson) | $200 | $200 | $0 |
| Sensors | $60 | $960 | +$900 |
| Optics | $115 | $155 | +$40 |
| Power | $30 | $45 | +$15 |
| Housing | $130 | $180 | +$50 |
| Other | $49 | $55 | +$6 |
| Labor + Test | $100 | $150 | +$50 |
| Software | $100 | $150 | +$50 |
| **UNIT COST** | **$784** | **$1,895** | **+$1,111** |

### 5.2 Pricing Strategy

| Variant | Unit Cost | Margin | Target Price | vs. Import |
|---------|-----------|--------|--------------|------------|
| LITE | $784 | 3.8x | $3,000 | 17% of SMASH |
| PRO | $1,895 | 2.5x | $4,500-5,000 | 25-28% of SMASH |

*Import reference: Smart Shooter SMASH 2000+ = $18,000*

### 5.3 Market Potential

| Metric | LITE | PRO | Combined |
|--------|------|-----|----------|
| Est. Units (5-year) | 1,500 | 800 | 2,300 |
| Revenue | $4.5M | $4.0M | **$8.5M** |
| Gross Margin | 60% | 55% | 58% |
| Gross Profit | $2.7M | $2.2M | **$4.9M** |

---

## 6. RISK REGISTER UPDATE

### 6.1 New Risks Identified

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Night/thermal capability gap | High | High | Add thermal in Phase 2 (PRO) |
| False positive in clutter | Medium | Medium | Expand negative training data |
| Evasive target track loss | Medium | High | Implement IMM filter |
| PRO local content below 60% | High | Medium | Request waiver; future local thermal |
| Thermal sensor supply risk | Low | High | Qualify multiple suppliers |

### 6.2 Mitigated Risks

| Risk | Original Status | New Status | Action Taken |
|------|-----------------|------------|--------------|
| Single product price point | Medium | **Low** | Two-tier pricing |
| Market segmentation gap | Medium | **Low** | LITE/PRO addresses both segments |

---

## 7. DOCUMENTS MODIFIED

### 7.1 Document Version Summary

| Document | Previous | Current | Key Changes |
|----------|----------|---------|-------------|
| Project Brief | v1.1 | **v1.2** | Two-tier strategy, pricing |
| ODI Analysis | v1.0 | **v1.1** | +5 outcomes, updated landscape |
| Requirements List | v1.0 | **v1.1** | +7 requirements, ODI traceability |
| Concept Evaluation | v1.1 | **v1.2** | Re-evaluation, two-tier approved |
| Product Variants Spec | — | **v1.0** | NEW: LITE vs PRO specifications |

### 7.2 Cross-Reference Matrix

| Document | References | Referenced By |
|----------|------------|---------------|
| ODI Analysis v1.1 | — | Requirements, Concept Eval, Variants |
| Requirements v1.1 | ODI Analysis | Concept Eval, Variants |
| Concept Eval v1.2 | ODI, Requirements | Project Brief, Variants |
| Variants Spec v1.0 | All above | Project Brief |
| Project Brief v1.2 | All above | — |

---

## 8. OPEN ITEMS

| Item | Owner | Due | Status |
|------|-------|-----|--------|
| MoD approval for two-tier strategy | Program Office | Week 2 | Pending |
| Local content waiver for PRO | Program Office | Week 3 | Pending |
| Thermal sensor procurement (eval units) | Procurement | Week 4 | Not started |
| Phase 3 kickoff (LITE) | Engineering | Week 2 | Ready |
| LITE preliminary layout | Mechanical Eng | Week 4 | Not started |

---

## 9. NEXT STEPS

### Immediate (Week 1-2)
1. Present two-tier strategy to MoD stakeholders
2. Initiate Phase 3 Embodiment Design for V-SMASH-LITE
3. Source FLIR Lepton 3.5 evaluation units

### Short-term (Week 3-4)
1. Obtain MoD approval
2. Complete LITE preliminary layout
3. Begin PRO thermal integration study

### Medium-term (Month 2-3)
1. LITE PDR (Preliminary Design Review)
2. PRO requirements finalization
3. Supplier qualification for LITE production

---

## 10. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Lead | | | |
| Technical Lead | | | |
| Program Manager | | | |

---

## APPENDIX A: ACRONYMS

| Acronym | Definition |
|---------|------------|
| C-UAS | Counter-Unmanned Aerial System |
| FCS | Fire Control System |
| HDR | High Dynamic Range |
| IMM | Interacting Multiple Model (filter) |
| LWIR | Long-Wave Infrared |
| NETD | Noise Equivalent Temperature Difference |
| NV | Night Vision |
| ODI | Outcome-Driven Innovation |
| VDI | Verein Deutscher Ingenieure (German Engineers Association) |

---

## APPENDIX B: FILE LOCATIONS

```
D:\UxV\engineering-projects\engineering-design-system\vault\projects\V-SMASH\
├── V-SMASH_00_project_brief.md              (v1.2)
├── V-SMASH_P0_01_ODI_analysis.md            (v1.1) ✏️
├── V-SMASH_P1_01_requirements_list.md       (v1.1) ✏️
├── V-SMASH_P2_01_function_structure.md      (v1.0)
├── V-SMASH_P2_02_morphological_matrix.md    (v1.0)
├── V-SMASH_P2_03_concept_evaluation.md      (v1.2) ✏️
├── V-SMASH_P2_04_conceptual_design_v1_1.md  (v1.1)
├── V-SMASH_P2_05_product_variants_spec.md   (v1.0) 🆕
└── V-SMASH_SESSION_REPORT_2026-02-04.md     (this file) 🆕

✏️ = Modified this session
🆕 = Created this session
```

---

**Report Generated:** 2026-02-04
**Session Duration:** Phase 0 Revision
**Framework:** Engineering Design System v2.3

---

*End of Report*
