---
project: VN-TGT-SEA-001
phase: 0
type: synthesis
version: 2.1
created: 2026-02-10
updated: 2026-02-10
revision: B.1
status: draft
---

# Phase 0 Synthesis: Refined Analysis & Cost-Budget Model

> **Rev B.1 NOTE:** This synthesis document is partially superseded by [[environmental_survivability.md]] (SS 5-6 analysis) and [[phase0_final_revision.md]] (>1,000 m² RCS, final specs). Key changes since this document: 8.0m platform (was 6.0m), superstructure REMOVED, IR/propane REMOVED (radar-only), 0.8m reflectors at 3-4m on steel masts, 980 kg displacement, $35,640/unit @ 10, $292K development budget.

**Purpose:** Consolidate and refine all Phase 0 analyses into a single decision-quality document
**Covers:** ODI outcome refinement, competitive deepening, feasibility extension, cost/budget model
**Revision from:** Gate Review B (all four areas selected for revision)

---

## 1. ODI Outcome Refinement

### 1.1 Cross-Validation of Top 5 EXTREME Outcomes

Each EXTREME outcome has been cross-validated against RE data, feasibility study, and reference documents.

| ID   | Outcome                 | Original Opp | Validated Opp        | Change       | Validation Source                                                |
| ---- | ----------------------- | ------------ | -------------------- | ------------ | ---------------------------------------------------------------- |
| O-57 | Target survivability    | 18.0         | **18.0** (confirmed) | No change    | Feasibility study: PA12 TPMS needs ~7,200 hits to sink           |
| O-29 | Seeker acquisition      | 15.6         | **15.8** (↑)         | Imp 9.8→10.0 | Deep RE: 10-15% test failure rate confirmed by competitor data   |
| O-31 | 360 deg RCS consistency | 15.5         | **15.5** (confirmed) | No change    | Deep RE: 8 reflectors at 45 deg = ≤±2 dB verified by RCS formula |
| O-40 | Seeker at max range     | 15.0         | **15.0** (confirmed) | No change    | RCS 250-350 m² >> 150 m² seeker threshold                        |
| O-71 | Total cost of ownership | 15.0         | **15.5** (↑)         | Sat 3.0→2.5  | Cost model: current TCO worse than estimated ($1.2M vs $1M)      |

### 1.2 Sensitivity Analysis — What If Estimates Are Wrong?

| Scenario | Impact on EXTREME Count | Action |
|----------|------------------------|--------|
| Imp scores 1 point lower across board | 5 EXTREME → 3 EXTREME + 2 HIGH | O-57 still EXTREME (16.0), core thesis holds |
| Sat scores 2 points higher (current solution better than we think) | 5 EXTREME → 2 EXTREME + 3 HIGH | O-57 still EXTREME (14.0), survivability is real gap |
| Both Imp lower AND Sat higher | 5 EXTREME → 1 EXTREME + 4 HIGH | Only O-57 survives — project still viable on survivability alone |
| Field survey invalidates segment sizes | Segments shift ±15% | Strategy unchanged (Efficiency + Accuracy = >60% in all scenarios) |

**Conclusion:** O-57 (survivability) is robust under all sensitivity scenarios. Even pessimistic estimates keep it as the #1 opportunity. This validates TPMS flotation as the project's core innovation.

### 1.3 Outcome Dependency Map

```
OUTCOME DEPENDENCY CHAIN
═══════════════════════════════════════════════════════

O-57 Target survivability ──┐
                            ├──► O-62 Cost per test ──► O-71 TCO
O-58 Repair cost ───────────┘                          ↑
                                                       │
O-29 Seeker acquisition ──┐                            │
                          ├──► O-46 Test failure rate ──┘
O-31 360 deg RCS ─────────┤
                          │
O-40 Max range acquisition┘

TPMS flotation ──► O-57, O-58, O-62, O-71 (cost chain)
AM reflectors ──► O-29, O-31, O-40, O-42, O-46 (signature chain)

TWO TECHNOLOGY PILLARS:
1. TPMS → Survivability → Cost reduction (4 outcomes)
2. AM reflectors → Signature quality → Test success (5 outcomes)
```

### 1.4 Outcomes NOT Addressed by VN-TGT-SEA-001

| ID | Outcome | Opp | Why Not Addressed | Risk |
|----|---------|-----|-------------------|------|
| O-50 | Miss distance measurement | 13.5 | Requires LOMAH-type scoring system (separate product VN-RNG-001) | LOW — can add MDI as Phase 4 option |
| O-51 | Telemetry data capture | 11.0 | Passive target has no telemetry | LOW — GPS beacon provides basic data |
| O-44 | Signature realism | 14.0 | AM reflectors improve but don't replicate ship RCS pattern | MEDIUM — future digital twin could model |
| O-14 | Shipping interference | 8.0 | Operational, not design | N/A |

---

## 2. Competitive Positioning — Extended

### 2.1 Sixth Competitor: QinetiQ HSITT MkII (Towed Inflatable)

| Parameter | HSITT MkII | VN-TGT-SEA-001 Comparison |
|-----------|-----------|---------------------------|
| Type | High-Speed Inflatable Towed Target | Anchored stationary |
| Dimensions | 3.0 m x 1.5 m | 6.0 m diameter |
| Weight | ~50 kg | 800 kg |
| Speed | 50 knots (towed) | 0 knots |
| RCS | 5-20 m² (patches) | 250-350 m² |
| Cost | $5-10K per unit | $32-45K per unit |
| Reusability | 3-10 uses (gunnery) | 1x base, 5-10x (H variant) |
| Safety | LOW (tow vessel at 500m) | HIGH (withdraw 5+ km) |

**Assessment:** HSITT is the cheapest competitor but designed exclusively for gunnery (not missiles). RCS of 5-20 m² is ~25x too low for missile seeker acquisition. Not a competitor for VN-TGT-SEA-001's job.

### 2.2 Quantitative RCS Comparison

```
RCS COMPARISON AT X-BAND (9.4 GHz)
═══════════════════════════════════════════════════════

Missile seeker acquisition threshold: 150 m² (typical X-band active radar)

VN-TGT-SEA-001-H  ████████████████████████████████████  250-350 m²  PASS
SINKEX (frigate)   ██████████████████████████████████████████████████  1,000-10,000 m²  PASS (overkill)
HSMST (augmented)  █████████████                          20-100 m²  FAIL
Hammerhead (aug.)  ███████                                10-50 m²   FAIL
L-CATT (enhanced)  ███████                                20-50 m²   FAIL
HSITT MkII         ██                                     5-20 m²    FAIL
Current VN barge   ████████████████                       80-200 m²  MARGINAL

                   0    50   100   150   200   250   300   350   400  m²
                                    ↑
                           Seeker threshold (150 m²)

ONLY VN-TGT-SEA-001 and SINKEX reliably exceed the 150 m² threshold.
SINKEX costs $1-5M per test. VN-TGT-SEA-001 costs $32-45K.
```

> **Rev B.1:** VN-TGT-SEA-001 RCS upgraded to **1,000-1,200 m²** (0.8m reflectors). Now MATCHES SINKEX frigate-class. See [[phase0_final_revision.md]] Section 1.

### 2.3 Refined TCO Model — 10-Test, 20-Test, 50-Test Campaigns

| Solution | 10 Tests | 20 Tests | 50 Tests | Cost/Test (50) |
|----------|----------|----------|----------|----------------|
| **VN-TGT-SEA-001 Base** (expendable) | $790K | $1,430K | $3,350K | **$67K** |
| **VN-TGT-SEA-001-H** (reusable, 5 uses/unit) | $555K | $730K | $1,350K | **$27K** |
| SINKEX | $16,100K | $32,200K | $80,500K | $1,610K |
| USV + missile mode (Hammerhead) | $788K | $1,015K | $1,700K | $34K |
| L-CATT + radar | $310K | $460K | $910K | $18K |

**TCO breakdown for VN-TGT-SEA-001-H (50 tests):**
```
ITEM                           COST        NOTES
────────────────────────────────────────────────────────
Development (one-time)         $318,000    Including Hyperganic $68K
Target units (10 @ $45K)       $450,000    Each used 5 times = 50 tests
Operations (50 tests)
  Tow vessel (50 @ $5K)        $250,000    Charter + fuel + crew
  Propane (50 @ $100)          $5,000      2 kg per test
  GPS beacon (50 @ $50)        $2,500      Battery replacement
  Test failure risk (5% @ $25K)$62,500     Missile cost × failure rate
Module replacement (10 sets)
  Superstructure (10 @ $800)   $8,000      Replaced after each hit
  Reflectors (20 @ $1,500)     $30,000     Replace damaged reflectors
  TPMS core inspection (5)     $5,000      Check buoyancy annually
Debris recovery               $50,000     Environmental compliance
────────────────────────────────────────────────────────
AM Enhancement Savings         ($180,000)  Credit: 40 targets NOT purchased
────────────────────────────────────────────────────────
NET TCO (50 tests)             $1,001,000
Cost per test                  $20,020

Comparison:
  Without Hyperganic (50 expendable targets): $3,350,000 → $67K/test
  With Hyperganic (10 reusable targets):      $1,001,000 → $20K/test
  SAVINGS: $2,349,000 (70% reduction)
```

**Critical insight:** L-CATT appears cheaper ($18K/test) but FAILS on RCS (20-50 m² vs 150+ m² required) and safety. When factoring in test failure cost (missile = $500K), L-CATT's true cost rises to $118K/test due to 20% failure rate. VN-TGT-SEA-001-H at $20K/test with 3-5% failure rate is the true lowest-cost solution that WORKS.

> **Rev B.1:** VN-TGT-SEA-001-H is now expendable (TPMS removed). Unit cost $35,640. TCO for 50 tests: $2,692,000 ($53,840/test). Still 50% cheaper than baseline due to reduced missile loss (1-2% failure at >1,000 m² vs 10% baseline). See [[phase0_final_revision.md]] Section 5.

### 2.4 Risk-Adjusted TCO

| Solution | Base Cost/Test | Failure Rate | Missile Loss Risk ($500K) | **True Cost/Test** |
|----------|---------------|-------------|--------------------------|-------------------|
| **VN-TGT-SEA-001-H** | $20K | 3-5% | $15-25K | **$35-45K** |
| VN-TGT-SEA-001 Base | $67K | 5-8% | $25-40K | **$92-107K** |
| SINKEX | $1,610K | 2% | $10K | **$1,620K** |
| Hammerhead + missile | $34K | 15% | $75K | **$109K** |
| L-CATT + radar | $18K | 20% | $100K | **$118K** |

**VN-TGT-SEA-001-H has the lowest risk-adjusted cost per test of ANY solution that meets RCS requirements.**

---

## 3. Feasibility Extension — Production Scale

### 3.1 Production Volume Economics

| Parameter | Prototype (1 unit) | Small batch (10) | Medium (50) | Full rate (100) |
|-----------|-------------------|------------------|-------------|-----------------|
| **Base target (traditional)** | | | | |
| HDPE pontoon | $6,000 | $5,000 | $4,000 | $3,500 |
| Steel frame + superstructure | $3,500 | $2,500 | $2,000 | $1,800 |
| Traditional reflectors (8x) | $12,000 | $9,100 | $7,000 | $5,500 |
| Propane IR system | $3,000 | $2,600 | $2,200 | $2,000 |
| Anchor + chain | $1,000 | $950 | $800 | $700 |
| GPS beacon | $1,500 | $1,500 | $1,300 | $1,200 |
| Assembly + QC | $8,000 | $6,500 | $4,500 | $3,500 |
| Margin (10%) | $3,500 | $2,815 | $2,180 | $1,820 |
| **Subtotal base** | **$38,500** | **$31,000** | **$24,000** | **$20,000** |
| | | | | |
| **Hyperganic enhancement (add-on)** | | | | |
| AM reflectors (8x AlSi10Mg) | $12,000 | $10,000 | $7,500 | $6,000 |
| TPMS flotation core (PA12 SLS) | $10,000 | $7,000 | $4,500 | $3,500 |
| Schwarz P IR panels (optional) | $4,000 | $3,500 | $2,500 | $2,000 |
| Integration + testing | $3,000 | $2,000 | $1,500 | $1,000 |
| **Subtotal Hyperganic** | **$29,000** | **$22,500** | **$16,000** | **$12,500** |
| | | | | |
| **TOTAL (H variant)** | **$67,500** | **$53,500** | **$40,000** | **$32,500** |

**Key finding:** At 50+ units, the H variant approaches the base target price at 10 units ($40K vs $31K). The AM cost reduction comes from:
- AM service bureau volume discounts (30-40% at 50+ units)
- Learning curve on TPMS segmentation (fewer rejects)
- Batch processing efficiency (full build plates)

> **Rev B.1:** Hyperganic enhancement simplified to AM reflector frames only. TPMS flotation and Schwarz P IR panels removed. Unit cost @ 10 units: $35,640 (was $53,500 in this table). Platform increased to 8.0m diameter.

### 3.2 AM Supply Chain Timeline

```
AM COMPONENT SUPPLY CHAIN (PRODUCTION)
═══════════════════════════════════════════════════════

CORNER REFLECTORS (AlSi10Mg LPBF):
Week 1-2:  Design file preparation + nTop TPMS design
Week 3-5:  AM printing (4 reflectors per build plate, 2 builds)
Week 6:    Post-processing (support removal, heat treatment)
Week 7:    Anodize (Type III hard anodize, outsource)
Week 8:    QC (RCS measurement on each reflector)
Week 9:    Ship to assembly
─────────────────────────────────────────────────────
LEAD TIME: 9 weeks (order to delivery)
PARALLEL: 2 sets per build cycle (enough for 1 complete target)

TPMS FLOTATION BLOCKS (PA12 SLS):
Week 1:    Design file (nTop, slice for segmentation)
Week 2-4:  AM printing (126 blocks per section, ~10 builds)
Week 5:    Post-processing (powder removal, inspection)
Week 6:    Assembly (epoxy bonding + mechanical clips)
Week 7:    Waterproofing (hydrophobic spray coating)
Week 8:    QC (buoyancy test, weight verification)
Week 9:    Ship to assembly
─────────────────────────────────────────────────────
LEAD TIME: 9 weeks (order to delivery)
PARALLEL: 1 complete flotation section per cycle

CRITICAL PATH: AM components (9 weeks) vs traditional (4 weeks)
MITIGATION: Start AM 5 weeks before traditional fabrication
BUFFER: 2 weeks contingency for AM rejects/reprints
TOTAL PRODUCTION TIME: 11-13 weeks per unit (AM-limited)
```

### 3.3 Risk-Adjusted Production Schedule

| Milestone | Nominal | Risk-Adjusted | Risk Factor |
|-----------|---------|---------------|-------------|
| Phase H0 ballistic test | Week 0+8 | Week 0+10 | AM delivery delay (30%) |
| Phase H1 reflector RCS validation | Week 10+12 | Week 10+15 | RCS mismatch (15%), iteration |
| Phase H2 full-size flotation | Week 22+16 | Week 25+20 | Assembly challenges (40%) |
| Phase H3 production readiness | Week 38+12 | Week 45+14 | Supply chain setup (50%) |
| **First production unit** | **Week 50** | **Week 59** | |
| **10-unit batch complete** | **Week 62** | **Week 75** | |

**Nominal:** 15 months to first production unit
**Risk-adjusted:** 18 months to first production unit (within 18-24 month project window)

---

## 4. Cost/Budget Model — Complete

### 4.1 Development Budget (Detailed Phasing)

```
DEVELOPMENT BUDGET: VN-TGT-SEA-001-H
═══════════════════════════════════════════════════════

PHASE 0: ODI & FEASIBILITY                         $15,000
├── Customer interviews (travel + per diem)          $3,000
├── Phase H0 ballistic test                         $6,200
│   ├── nTop license (1 year)                       $2,000
│   ├── PA12 SLS block (500x300x300mm)              $1,500
│   ├── Shipping                                    $300
│   ├── Range time + ammunition                     $800
│   ├── Buoyancy test equipment                     $200
│   └── Contingency                                 $1,400
├── Reference document procurement                   $2,000
└── Phase 0 engineering labor (200 hr @ $20/hr)      $4,000
    Subtotal Phase 0: $15,200

PHASE 1: REQUIREMENTS & BASIC TARGET PROTOTYPE      $58,000
├── Requirements engineering (400 hr)               $8,000
├── Basic target prototype (traditional, no AM)      $38,500
│   ├── HDPE pontoon (6m circular)                  $6,000
│   ├── Steel frame + superstructure                $3,500
│   ├── Traditional reflectors (8x, hand-fab)       $12,000
│   ├── Propane IR system                           $3,000
│   ├── Anchor + chain (50m)                        $1,000
│   ├── GPS beacon                                  $1,500
│   ├── Assembly + QC                               $8,000
│   └── Margin (10%)                                $3,500
├── Sea trial (tow, anchor, float, RCS measure)      $5,000
├── Phase H0 test (if not done in Phase 0)           $0
└── Engineering labor (300 hr)                       $6,000
    Subtotal Phase 1: $57,500

PHASE 2: ENHANCED SIGNATURE (AM COMPONENTS)          $45,000
├── AM reflectors (4x prototype, AlSi10Mg LPBF)     $6,000
├── AM reflector RCS measurement + validation        $3,000
├── Schwarz P IR panel (1x prototype)               $4,000
├── IR panel thermal testing                         $2,000
├── Integration with basic prototype                 $5,000
├── Full system RCS/IR measurement                   $5,000
├── Engineering labor (500 hr)                      $10,000
├── AM service bureau management                     $5,000
└── Contingency (15%)                               $5,000
    Subtotal Phase 2: $45,000

PHASE 3: FULL INTEGRATION (TPMS FLOTATION)           $125,000
├── Full-size TPMS flotation section
│   ├── PA12 SLS printing (126 blocks)              $25,000
│   ├── Assembly + bonding                          $5,000
│   ├── Waterproofing                               $2,000
│   ├── Buoyancy verification                       $1,000
│   └── Subtotal TPMS                               $33,000
├── Live-fire ballistic test (full-size section)
│   ├── Range time (12.7mm, 50 rounds)              $3,000
│   ├── Target preparation                          $2,000
│   ├── Video documentation (4K)                    $1,000
│   └── Subtotal ballistic test                     $6,000
├── Complete integrated prototype
│   ├── New pontoon with TPMS core                  $15,000
│   ├── Full AM reflector set (8x)                  $10,000
│   ├── IR system with Schwarz P                    $5,000
│   ├── Integration + assembly                      $8,000
│   └── Subtotal integrated prototype               $38,000
├── Sea trial (full system)                          $8,000
├── Seeker compatibility test (with VPN)             $15,000
├── Engineering labor (800 hr)                      $16,000
└── Contingency (10%)                               $9,000
    Subtotal Phase 3: $125,000

PHASE 4: PRODUCTION READINESS                        $90,000
├── Production drawings + assembly manual            $10,000
├── Modular component library (nTop)                 $5,000
├── Jigs + fixtures for assembly                     $8,000
├── AM supplier qualification (audit + samples)      $5,000
├── Pilot production batch (3 units)
│   ├── 3 × $45,000                                 $135,000
│   └── Less: production revenue (3 × $45K sold)    ($135,000)
│   └── Net cost of pilot batch                     $0
├── QC procedures + test protocols                   $5,000
├── Packaging + logistics design                     $3,000
├── Marketing materials (demo video, datasheet)      $4,000
├── Engineering labor (1,000 hr)                    $20,000
├── Program management                              $15,000
└── Contingency (15%)                               $15,000
    Subtotal Phase 4: $90,000

═══════════════════════════════════════════════════════
TOTAL DEVELOPMENT: $332,700 (within $318K budget + 5% contingency)
═══════════════════════════════════════════════════════
```

> **Rev B.1:** Total development budget revised to **$292,000** (was $332,700). TPMS phases eliminated (-$39K). Storm mooring and mast system added (+$4K). See [[phase0_final_revision.md]] Section 5.3.

### 4.2 Cash Flow Projection (Monthly)

```
CASH FLOW: VN-TGT-SEA-001-H DEVELOPMENT
═══════════════════════════════════════════════════════

MONTH   PHASE    SPEND     CUMULATIVE   KEY MILESTONE
──────────────────────────────────────────────────────
M1      P0       $5,000    $5,000       ODI field survey
M2      P0       $6,200    $11,200      H0 ballistic test
M3      P0       $4,000    $15,200      Phase 0 gate
M4      P1       $15,000   $30,200      Start basic prototype
M5      P1       $20,000   $50,200      Pontoon + reflectors
M6      P1       $15,000   $65,200      Assembly + sea trial
M7      P1       $7,300    $72,500      Phase 1 gate
M8      P2       $12,000   $84,500      AM reflectors ordered
M9      P2       $10,000   $94,500      AM delivery + test
M10     P2       $12,000   $106,500     RCS validation
M11     P2       $11,000   $117,500     Phase 2 gate
M12     P3       $20,000   $137,500     TPMS printing start
M13     P3       $15,000   $152,500     TPMS assembly
M14     P3       $20,000   $172,500     Ballistic test (full)
M15     P3       $25,000   $197,500     Integrated prototype
M16     P3       $20,000   $217,500     Sea trial (full)
M17     P3       $25,000   $242,500     Seeker compat. test
M18     P4       $20,000   $262,500     Production setup
M19     P4       $20,000   $282,500     Pilot batch start
M20     P4       $20,000   $302,500     Pilot batch complete
M21     P4       $15,000   $317,500     Documentation
M22     P4       $15,200   $332,700     Program close
──────────────────────────────────────────────────────
PEAK MONTHLY: $25,000 (M15, M17)
AVERAGE MONTHLY: $15,100
```

### 4.3 ROI Analysis

```
ROI ANALYSIS: HYPERGANIC ENHANCEMENT INVESTMENT
═══════════════════════════════════════════════════════

INVESTMENT:
  Hyperganic enhancement (development):    $68,000
  Additional unit cost (AM vs traditional): $13,000/unit × 10 units = $130,000
  TOTAL HYPERGANIC INVESTMENT:              $198,000

RETURNS (over 3-year period, 50 tests):
  Targets saved (40 @ $32K each):          $1,280,000
  Less: AM module replacement:             ($38,000)
  Less: TPMS inspection/maintenance:       ($5,000)
  NET SAVINGS:                             $1,237,000

ROI:
  Net return / Investment × 100
  = $1,237,000 / $198,000 × 100
  = 625% ROI over 3 years

PAYBACK:
  Investment per unit: $13,000 (AM premium)
  Savings per reuse: $32,000 (avoided replacement)
  PAYBACK: 1 reuse cycle (0.4 units worth of savings)
  After 2nd reuse: $51,000 net positive per unit

BREAKEVEN:
  Total Hyperganic investment: $198,000
  Savings per avoided target: $32,000
  Targets saved before breakeven: 198,000 / 32,000 = 6.2 targets
  At 10 tests/year with 5 reuses each: breakeven in ~3 targets = YEAR 1
```

> **Rev B.1:** ROI recalculated as **928%** vs baseline (3-year, 50 tests). Primary savings from reduced missile loss ($2.25M over 50 tests at 1% vs 10% failure rate). TPMS reuse savings no longer applicable. See [[phase0_final_revision.md]] Section 5.4.

### 4.4 Unit Cost Sensitivity

| Variable | Base Case | Optimistic | Pessimistic | Impact on Unit Cost |
|----------|-----------|-----------|-------------|-------------------|
| PA12 SLS price | $0.25/cm³ | $0.10/cm³ | $0.50/cm³ | $45K → $42K / $51K |
| AlSi10Mg LPBF price | $1,000/reflector | $600 | $1,500 | $45K → $42K / $49K |
| TPMS cell size | 8mm | 6mm (more cells) | 10mm (fewer cells) | $45K → $48K / $42K |
| HDPE pontoon | $5,000 | $4,000 | $7,000 | $45K → $44K / $47K |
| Labor rate | $20/hr | $15/hr | $25/hr | $45K → $43K / $47K |
| AM service bureau | China/SG | Vietnam (future) | Europe | $45K → $45K / $55K |
| **Worst case (all pessimistic)** | | | | **$62,000** |
| **Best case (all optimistic)** | | | | **$35,000** |

**Even worst-case unit cost ($62K) is <50% of Hammerhead ($300K) and <4% of SINKEX ($1.6M/test).**

---

## 5. Integrated Decision Matrix

### 5.1 Go/No-Go Criteria Assessment

| # | Criterion | Threshold | Actual | Status |
|---|-----------|-----------|--------|--------|
| 1 | Market need validated (ODI) | ≥3 EXTREME outcomes | 5 EXTREME | PASS |
| 2 | Customer scorecard | ≥8.0/10 | 8.56/10 | PASS |
| 3 | Competitive differentiation | #1 in weighted scoring | 3.85/5 (#1) | PASS |
| 4 | FTO clear | No blocking patents | CLEAR | PASS |
| 5 | Technology feasibility | ≥70% confidence | 80-90% | PASS |
| 6 | Unit cost within target | ≤$50K (H variant) | $40-45K (base case) | PASS |
| 7 | Development budget feasible | ≤$350K | $333K | PASS |
| 8 | Local content ≥60% | ≥60% | 85-90% | PASS |
| 9 | Timeline ≤24 months | ≤24 months | 18-22 months (risk-adj.) | PASS |
| 10 | ROI positive | >100% 3-year ROI | 625% | PASS |

**Result: 10/10 PASS — All criteria met.**

> **Rev B.1:** All 10 criteria still PASS. Technology feasibility increased to 95% (hybrid CNC/AM is proven). Unit cost $35,640 (within $50K). Budget $292K (within $350K). ROI 928%.

### 5.2 Top Risks Entering Phase 1

| Risk | Probability | Impact | Mitigation | Gate |
|------|-------------|--------|------------|------|
| PA12 TPMS fails ballistic test | 25% | HIGH | Phase H0 test ($6.2K) before major spend | H0 |
| AM cost exceeds budget | 15% | MEDIUM | Chinese bureaus at $$ vs $$$ Singapore; worst case $62K still competitive | H1 |
| Military rejects 3D-printed hardware | 50% | HIGH | Live-fire demo video; GE Aviation citation; focus on DATA not process | H0 |
| No local AM service bureau | 10% | LOW | Multiple ASEAN options (Xometry, Facfox, Additive3D, JR Technology) | H1 |
| RCS doesn't match simulation | 15% | MEDIUM | Well-established corner reflector physics; AM tolerance ±0.1 deg proven | H1 |
| Water wicks through damaged TPMS cells | 35% | MEDIUM | Hydrophobic coating; thicker walls (1.0mm); Phase H0 measures this | H0 |

### 5.3 Phase 1 Entry Conditions

To enter Phase 1 (Task Clarification / Requirements), the following are confirmed ready:

| Condition | Status |
|-----------|--------|
| Job executor and core job defined | READY |
| 73 outcomes captured and prioritized | READY |
| Growth strategy selected (DIFFERENTIATED) | READY |
| Competitive positioning established | READY |
| Technology feasibility assessed | READY |
| Budget and schedule baselined | READY |
| Design directives from RE (10 total) | READY |
| Phase H0 test protocol defined | READY (can execute in parallel with Phase 1) |

---

## 6. Phase 1 Recommended Scope

### 6.1 Requirements Categories (Pahl-Beitz 16 Categories)

Based on Phase 0 findings, the following categories will require special attention:

| Category | Priority | Source from Phase 0 |
|----------|----------|-------------------|
| Performance (RCS, IR) | CRITICAL | O-29, O-31, O-40 — 250-350 m², ≤±2 dB, 360 deg |
| Survivability | CRITICAL | O-57 — 50+ hits, TPMS core specification |
| Cost | HIGH | O-62, O-71 — $40-45K unit, $20K/test TCO |
| Safety | HIGH | O-35 — 5+ km withdrawal, passive operation |
| Environmental | HIGH | O-10, O-66 — any seabed, minimal debris |
| Manufacturing | HIGH | DFM directives from C-Target 3 RE |
| Maintenance | MEDIUM | Modular replacement, AM component swap |
| Deployment/logistics | MEDIUM | 30 min deploy, 2-3 per container |
| Standards (MIL-STD) | MEDIUM | MIL-STD-810H, TCVN mapping |
| Signature (electromagnetic) | HIGH | RCS formula validation, RCS measurement protocol |

### 6.2 Phase H0 Test — Execute in Parallel

Phase H0 ballistic test can run in parallel with Phase 1 requirements engineering:

```
PARALLEL EXECUTION
═══════════════════════════════════════════════════════

PHASE 1 (Requirements):                   PHASE H0 (Test):
Week 1: Requirements kickoff              Week 1: Order PA12 block
Week 2: Stakeholder analysis              Week 2: (waiting for print)
Week 3: Performance requirements          Week 3: (waiting for print)
Week 4: Survivability requirements        Week 4: Block delivered
Week 5: Cost/DFM requirements             Week 5: Ballistic test!
Week 6: Standards mapping                 Week 6: Data analysis
Week 7: Validation                        Week 7: Report
Week 8: Phase 1 gate review               Week 8: H0 gate decision

BENEFIT: 8 weeks saved vs sequential execution
RISK: If H0 fails, Phase 1 requirements may need revision (survivability spec)
MITIGATION: Phase 1 requirements written with fallback (base + H variant specs)
```

---

## Cross-References

- [[odi_analysis.md]] - Full ODI analysis (73 outcomes, 10 steps)
- [[re_competitive_analysis.md]] - Competitive positioning (5 competitors)
- [[re_deep_analysis.md]] - Deep RE subsystem teardown
- [[hyperganic_feasibility.md]] - AM/TPMS feasibility study
- [[../00_project_brief.md]] - Project brief
- [[../PROJECT_STATUS.md]] - Status tracker
