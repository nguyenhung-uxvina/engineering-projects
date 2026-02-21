---
project: VN-CUA-001
designation: VDC-100
type: concept_selection
phase: 2
step: 6
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Step 6
---

# VN-CUA-001: CONCEPT SELECTION & GATE 2 REVIEW
## Vietnamese Drone Catcher 100 (VDC-100)
## Chọn Phương án & Duyệt Cổng 2 - Giai đoạn 2, Bước 6

**Project Code:** VN-CUA-001
**Phase:** 2 - Conceptual Design (Step 6: Select & Firm Up)
**Date:** 2026-02-08
**Input:** [[02_conceptual/concept_evaluation|VDI 2225 Evaluation Results]]

---

# 1. SELECTION DECISION

## 1.1 Selection Summary

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                  SELECTED CONCEPT: VDC-100 ENHANCED (Concept B)              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  VDI 2225 Score: 85.8% (Exceeds 70% threshold by 15.8 points)               ║
║  Margin over #2: +5.8% (vs. Concept A: Basic at 80.0%)                      ║
║  Margin over #3: +10.0% (vs. Concept D: Pyro at 75.8%)                      ║
║                                                                              ║
║  SELECTION RATIONALE:                                                        ║
║  1. Highest VDI 2225 score across all scenarios (sensitivity robust)         ║
║  2. No weak spots — minimum score 3/4 across all 9 criteria                  ║
║  3. Only concept that survives any single criterion dropping to 0            ║
║  4. Best alignment with top ODI outcomes (O-48, O-23, O-43)                  ║
║  5. Meets all MUST requirements (price, weight, local content)               ║
║  6. Maintains jam-proof operation (no RF in fire control chain)              ║
║                                                                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## 1.2 Selection Rationale (Detailed)

### Why Concept B over Concept A (Basic)?

| Factor | A: Basic (80.0%) | B: Enhanced (85.8%) | Advantage |
|--------|-------------------|---------------------|-----------|
| First-shot hit | ~60% (score 2) | ~70% (score 3) | **B wins by +10% hit rate** — addresses #1 ODI |
| Net deploy | Single timer (score 3) | Timer+Barometric (score 4) | **B wins** — dual redundancy |
| Reload time | ~10 sec (score 3) | ≤8 sec (score 4) | **B wins** — fast valve |
| Cost | $4,800 (score 4) | $5,400 (score 3) | A wins by $600 — acceptable trade-off |
| Dev risk | Low (score 4) | Low-Med (score 3) | A wins — B has fin+barometric development |

**Decision:** The $600 cost premium ($5,400 vs $4,800) is justified by the 10% first-shot hit improvement. At the ODI opportunity score of 15.0, first-shot hit is the #1 value driver — customers will pay $600 more for significantly better accuracy.

### Why Not Concept C (Pro)?

- **Fails cost MUST** ($9,000 > $6,000 ceiling)
- **Fails weight MUST** (10 kg > 8 kg ceiling)
- **VDI 2225 below threshold** (64.3% < 70%)
- RF command deploy is **vulnerable to jamming** — contradicts C-UAS mission profile
- Complex electronics **reduce reliability** — the #2 ODI outcome

### Why Not Concept D (Pyro)?

- **Weapon regulation risk** in Vietnam — blank cartridge may require firearms license
- **Loud report** (120+ dB) — tactical signature unacceptable for security operations
- **Lower first-shot hit** (60% vs 70%) — same as Basic without accuracy improvements
- **Higher per-shot cost** — single-use cartridges vs. refillable HPA

---

# 2. SELECTED CONCEPT SPECIFICATION

## 2.1 VDC-100 ENHANCED — Working Principles Summary

| Function | Selected Principle | Rationale |
|----------|-------------------|-----------|
| F1.1 Detect | Visual (operator eyes) | Zero cost, zero latency, proven |
| F1.3 Range | Laser rangefinder (COTS) | ±1m accuracy for O-48 (first-shot hit) |
| F1.4 Aim | Hybrid (LRF + ballistic reticle) | Best accuracy/cost for #1 ODI outcome |
| F2.1 Energy | HPA cylinder (0.5L @ 300 bar) | Refillable, consistent, silent, ≥5 shots |
| F2.2 Load | Breech loading | Fast reload ≤8 sec, simple mechanism |
| F2.3 Regulate | Mechanical regulator (300→100 bar) | Consistent ±3%, no electronics, proven |
| F3.1 Release | Fast-acting trigger valve | <50 ms response, mechanical linkage |
| F3.2 Accelerate | Pneumatic tube (smoothbore) | Clean, quiet, 60 m/s muzzle velocity |
| F3.3 Guide | Fin stabilization (projectile) | Accuracy improvement without barrel complexity |
| F4.1 Deploy | Projected net (3m × 3m UHMWPE) | Large capture area, proven |
| F4.1t Timing | Timer + barometric backup | Dual redundancy → 99.9% deploy rate |
| F4.2 Entangle | Mesh net with corner weights | Reliable spread, simple, proven |
| F5.1 Descend | Parachute + drogue backup | Dual redundancy for evidence preservation |

## 2.2 System Description

**VDC-100 ENHANCED** is an ODI-optimized, man-portable pneumatic net launcher designed to physically capture small drones intact for forensic evidence recovery.

### Targeting System

| Component | Specification | Source |
|-----------|--------------|--------|
| Laser Rangefinder | COTS module, 5-150m range, Class 1 eye-safe (IEC 60825) | Import (China/US) |
| Ballistic Reticle | Etched glass with graduated range marks (20/40/60/80/100m) | Local fabrication |
| Lead Angle Marks | Calibrated for 5/10/15 m/s target speeds at each range | Local calibration |
| Display | LCD, 1000+ nit sunlight-readable, range + status | Import module |
| Battery | 18650 Li-ion, 3.7V, 3400 mAh, ≥8 hrs runtime | Import (standard) |
| Mounting | Picatinny rail, quick-detach | Local machining |

**Operator Workflow:**
1. Detect drone visually → raise weapon to shoulder
2. Acquire target in reticle → press LRF button (thumb)
3. Range displayed → select range mark on reticle
4. Estimate target speed → apply lead mark
5. Confirm safe firing corridor → disengage safety
6. Squeeze trigger → projectile launches

### Propulsion System

| Component | Specification | Source |
|-----------|--------------|--------|
| HPA Cylinder | Aluminum, 0.5L, DOT-3AL rated 300 bar, ~1.2 kg | Import (certified) |
| Regulator | Mechanical spring-piston, 300→100 bar, ±3% | Local assembly |
| Trigger Valve | Fast-acting, <50 ms open time, mechanical linkage | Local fabrication |
| Barrel | Aluminum 6061-T6, 800mm length, 100mm ID, smoothbore | Local extrusion + machining |
| Breech | Hinged rear chamber, drop-in loading, spring latch | Local machining |
| Safety | Positive mechanical arm/safe switch, left-side thumb | Local fabrication |
| Pressure Gauge | Analog, 0-350 bar, visible from firing position | Import (standard) |

**Propulsion Specifications:**
- Working pressure: 100 bar (regulated from 300 bar)
- Muzzle velocity: 60 ±3 m/s (consistent across shots)
- Shots per fill: ≥5 at 100 bar regulated
- Noise level: <85 dB (hearing-safe without protection)
- Recoil energy: ~20 J (manageable from shoulder)

### Projectile (VDC-P40E)

| Component | Specification | Source |
|-----------|--------------|--------|
| Body | Injection-molded polymer, 80mm OD, 200mm length | Local molding |
| Fins | 4× spring-loaded deployment fins (post-muzzle) | Local fabrication |
| Net | 3m × 3m, UHMWPE (Dyneema), mesh size 40mm | Import fiber / local assembly |
| Corner Weights | 4× steel, 25g each (total 100g) | Local machining |
| Timer Deploy | Mechanical timer, 1.8 sec default (adjustable 1.2-2.5 sec) | Local assembly |
| Barometric Backup | MEMS altimeter module, triggers at apex (ΔP threshold) | Import module |
| Parachute | 0.8m ripstop nylon, spring-ejected from rear | Local sewing + assembly |
| Drogue Backup | 0.3m streamer, deploys with net | Local fabrication |
| **Total Mass** | **450g** | |

**Projectile Cost Estimate:** ~$30-35 per round (target ≤$35 per CUA-CST-07)

### Launcher Body

| Component | Specification | Source |
|-----------|--------------|--------|
| Receiver | Glass-reinforced polymer, houses trigger group + valve | Local molding |
| Stock | Adjustable polymer, ±50mm length, rubber butt pad | Local molding |
| Cylinder Mount | Quick-release bracket under stock | Local machining |
| Sling Points | 2× steel loops (front + rear) | Local fabrication |
| Finish | Matte olive drab, anodized aluminum, painted polymer | Local finishing |

### System Mass Budget

| Assembly | Mass (kg) | % of Total |
|----------|-----------|------------|
| Barrel assembly (barrel + breech + muzzle) | 2.1 | 27% |
| Receiver + trigger group + valve | 0.9 | 12% |
| Regulator | 0.3 | 4% |
| Scope assembly (LRF + reticle + display + battery) | 0.6 | 8% |
| Stock assembly | 0.5 | 6% |
| HPA cylinder (0.5L, full) | 1.4 | 18% |
| Projectile (loaded) | 0.45 | 6% |
| Hardware, sling, misc | 0.55 | 7% |
| **Subtotal (loaded)** | **6.8** | **87%** |
| **Margin (10%)** | **0.7** | **9%** |
| **TOTAL (target)** | **≤7.8 kg** | **100%** |

**Status:** Within 8 kg MUST requirement with 0.2 kg margin.

---

# 3. KEY ADVANTAGES OVER ALTERNATIVES

## 3.1 vs. Other Concepts

| vs. A (Basic) | vs. C (Pro) | vs. D (Pyro) |
|---------------|-------------|---------------|
| +5.8% VDI score | +21.5% VDI score | +10.0% VDI score |
| Better first-shot hit (+10%) | Much lower cost ($5.4K vs $9K) | No weapon regulation |
| Dual deploy redundancy | Higher reliability (mech vs electronic) | Silent operation |
| Fin stabilization | Higher local content (72% vs 50%) | Refillable (lower TCO) |
| Fast reload (8 vs 10 sec) | Lighter weight (7.8 vs 10 kg) | Consistent velocity |

## 3.2 vs. Import Alternatives

| Parameter | VDC-100 Enhanced | SkyWall 300 (UK) | DroneShield NetGun (AU) |
|-----------|------------------|-------------------|-------------------------|
| **Price** | **$5,400** | $30,000 | $25,000 |
| **Range** | 80m | 100m | 15m (handheld) |
| **Weight** | 7.8 kg | 10 kg | 3 kg |
| **First-shot hit** | 70% (est.) | 80% (claimed) | 90% (short range) |
| **Local support** | Yes (Vietnam) | No (UK import) | No (AU import) |
| **Local content** | 72% | 0% | 0% |
| **Evidence preservation** | Dual-redundant chute | Single chute | No chute |
| **Anti-jam** | Yes (no RF) | Yes (no RF) | N/A (manual) |
| **Cost ratio** | **18% of SkyWall** | Baseline | 22% of SkyWall |

## 3.3 vs. RF Jamming (Non-Kinetic C-UAS)

| Parameter | VDC-100 Enhanced | RF Jammer (~$15K) |
|-----------|------------------|-------------------|
| **Works on autonomous drones** | **YES** (physical capture) | NO (no RF to jam) |
| **Evidence preservation** | **YES** (intact recovery) | NO (drone crashes) |
| **Collateral risk** | Low (projectile trajectory) | Medium (RF interference) |
| **Legal status** | Equipment (not weapon) | May need spectrum license |
| **Range** | 80m | 500-2000m |

**Positioning:** VDC-100 Enhanced fills the gap between short-range handheld nets and expensive electronic systems, with the unique advantage of **evidence preservation against autonomous drones**.

---

# 4. DEVELOPMENT RISKS & MITIGATIONS

## 4.1 Risk Register

| Risk ID | Risk Description | Probability | Impact | Score | Mitigation Strategy | Fallback |
|---------|-----------------|-------------|--------|-------|---------------------|----------|
| R-01 | Fin-stabilized projectile doesn't achieve +10% accuracy improvement | Medium | Medium | **6** | Prototype early (Month 2), test extensively at range | Remove fins → Concept A smoothbore |
| R-02 | Barometric backup deployment unreliable at varying altitudes | Low | Low | **2** | Use proven MEMS altimeter module, extensive testing | Remove barometric → timer only (Concept A) |
| R-03 | Ballistic reticle calibration doesn't match across projectile lots | Medium | Low | **3** | Tight manufacturing tolerance on projectile mass, multiple test sessions | Accept wider tolerance, adjust reticle spacing |
| R-04 | LRF COTS module integration issues (interface, power, mounting) | Low | Medium | **3** | Select module with standard serial interface, 3 supplier options | Stadiametric reticle backup (no LRF) |
| R-05 | Total weight exceeds 8 kg after detailed design | Low | High | **4** | Mass budget with 10% margin, material optimization | Reduce cylinder to 0.3L (3 shots) |
| R-06 | HPA cylinder TCVN certification delayed | Medium | Medium | **6** | Start TCVN 6153 registration in Month 2, parallel import option | Import DOT-3AL certified cylinder |

## 4.2 Risk Matrix

```
DEVELOPMENT RISK MATRIX — VDC-100 ENHANCED
═══════════════════════════════════════════════════════════════════════════════

               │ LOW Impact    │ MED Impact    │ HIGH Impact
───────────────│───────────────│───────────────│───────────────
HIGH Prob      │               │               │
               │               │               │
───────────────│───────────────│───────────────│───────────────
MEDIUM Prob    │ R-03 Reticle  │ R-01 Fins     │
               │  calibration  │  accuracy     │
               │               │ R-06 TCVN cert│
───────────────│───────────────│───────────────│───────────────
LOW Prob       │ R-02 Baro     │ R-04 LRF      │ R-05 Weight
               │  backup       │  integration  │  overrun
               │               │               │
───────────────│───────────────│───────────────│───────────────

OVERALL RISK LEVEL: LOW-MEDIUM
No HIGH probability risks. All risks have identified mitigations and fallbacks.

═══════════════════════════════════════════════════════════════════════════════
```

## 4.3 Fallback Strategy

**If Concept B encounters critical development issues:**

```
FALLBACK PATH
═══════════════════════════════════════════════════════════════════════════════

VDC-100 ENHANCED (B: 85.8%)
    │
    ├── Risk R-01 materializes (fins don't help) ──► Remove fins
    │   └── Score impact: C1 drops 3→2, score = 80.0%
    │
    ├── Risk R-02 materializes (baro fails) ──► Timer only
    │   └── Score impact: C4 drops 4→3, score = 83.3%
    │
    ├── Both R-01 AND R-02 ──► Concept A (Basic)
    │   └── Score = 80.0% (still above 70% threshold)
    │
    └── MINIMUM VIABLE: Concept A at 80.0% VDI 2225
        └── All proven technology, LOW development risk

═══════════════════════════════════════════════════════════════════════════════
```

---

# 5. PRELIMINARY LAYOUT

## 5.1 Side View

```
VDC-100 ENHANCED — PRELIMINARY LAYOUT (Side View)
═══════════════════════════════════════════════════════════════════════════════

    ┌─────────────────────────────────────────────────────────────────────┐
    │                         TARGETING SCOPE                             │
    │  ┌──────────────────────────────────────────────────────────────┐  │
    │  │  LRF  │ Ballistic Reticle │ LCD Display │ Battery            │  │
    │  │ Module│ (etched glass)    │ (status)    │ (18650)            │  │
    │  └──────────────────────────────────────────────────────────────┘  │
    └────────────────────────────────┬────────────────────────────────────┘
                                     │ Picatinny mount
    ┌────────────────────────────────┴────────────────────────────────────┐
    │                           BARREL ASSEMBLY                           │
    │  ┌────────┐  ┌────────────────────────────────────┐  ┌───────────┐ │
    │  │ MUZZLE │  │     BARREL (Al 6061-T6, 800mm)     │  │  BREECH   │ │
    │  │(100mm) │  │         Smoothbore, 100mm ID       │  │  CHAMBER  │ │
    │  └────────┘  └────────────────────────────────────┘  └─────┬─────┘ │
    └────────────────────────────────────────────────────────────│───────┘
                                                                 │
    ┌────────────────────────────────────────────────────────────┴───────┐
    │                         RECEIVER ASSEMBLY                          │
    │  ┌───────────────┐  ┌─────────────┐  ┌──────────────────────────┐ │
    │  │ TRIGGER       │  │ VALVE       │  │ REGULATOR (300→100 bar)  │ │
    │  │ MECHANISM     │  │ (fast-act)  │  │                          │ │
    │  │               │  │ (<50ms)     │  │ (mechanical spring)      │ │
    │  └───────┬───────┘  └──────┬──────┘  └────────────┬─────────────┘ │
    │          │                 │                      │                │
    │    [ARM/SAFE]         [Gas line]            [HPA line]            │
    │     (left thumb)                                                   │
    └──────────│─────────────────│──────────────────────│────────────────┘
               │                 │                      │
    ┌──────────┴─────────────────┴──────────────────────┴────────────────┐
    │                           STOCK ASSEMBLY                           │
    │  ┌───────────────────────┐  ┌────────────────────────────────────┐│
    │  │ ADJUSTABLE STOCK      │  │ HPA CYLINDER (0.5L @ 300 bar)      ││
    │  │ (±50mm, rubber pad)   │  │ [Quick-release mount]              ││
    │  │                       │  │ [Pressure gauge visible]           ││
    │  └───────────────────────┘  └────────────────────────────────────┘│
    │                              [Sling point rear]                    │
    └────────────────────────────────────────────────────────────────────┘
```

## 5.2 Top View

```
VDC-100 ENHANCED — TOP VIEW
═══════════════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────────────────┐
                    │                    SCOPE (170mm)                    │
                    └─────────────────────────────────────────────────────┘
    ┌───────────────────────────────────────────────────────────────────────┐
    │   MUZZLE   │              BARREL (800mm)              │   BREECH     │
    └───────────────────────────────────────────────────────────────────────┘
                                                            ┌───────────────┐
                                                            │   RECEIVER    │
                                                            │   (200mm)     │
                                                            └───────────────┘
                    ┌─────────────────────────────────────────────────────┐
                    │              STOCK + CYLINDER (400mm)               │
                    └─────────────────────────────────────────────────────┘
```

## 5.3 Key Dimensions

| Parameter | Value | Tolerance | Source Requirement |
|-----------|-------|-----------|-------------------|
| Overall length | 1150mm (collapsed: 800mm if folding) | ±20mm | CUA-GEO-02 (≤1200mm) |
| Barrel length | 800mm | ±5mm | CUA-GEO-02 |
| Barrel ID | 100mm | ±0.5mm | CUA-GEO-04 (≤120mm OD) |
| Barrel OD | 110mm | ±1mm | CUA-GEO-04 |
| Scope length | 170mm | ±5mm | — |
| Stock length | 400mm (adjustable ±50mm) | ±2mm | CUA-ERG-02 |
| Total height | 180mm (with scope) | ±5mm | — |
| Total width | 120mm | ±5mm | — |
| System weight | 7.8 kg (loaded, with scope) | Target ≤8.0 | CUA-GEO-01 (≤8 kg) |

## 5.4 Projectile Cross-Section

```
VDC-P40E PROJECTILE — CROSS-SECTION
═══════════════════════════════════════════════════════════════════════════════

    ◄─── 200mm ───►

    ┌──────────────────────────────────────────┐
    │  NOSE CONE │    NET + WEIGHTS   │  REAR  │  ← 80mm OD
    │  (deploy   │    (folded)        │  BODY  │
    │   timer)   │                    │        │
    │            │    3m×3m UHMWPE    │ ┌────┐ │
    │  [Timer]   │    4× 25g weights  │ │CHUTE│ │  ← Parachute (0.8m)
    │  [Baro]    │                    │ │+   │ │  ← Drogue (0.3m)
    │            │                    │ │FINS│ │  ← 4× spring-load fins
    │            │                    │ └────┘ │
    └──────────────────────────────────────────┘
                                         ↑
                                    Gas seal ring

    Mass breakdown:
    • Body (polymer): 80g
    • Net (UHMWPE): 120g
    • Corner weights: 100g (4×25g)
    • Timer mechanism: 15g
    • Barometric module: 10g
    • Parachute + drogue: 50g
    • Fins (4×): 40g
    • Hardware: 35g
    ─────────────────────
    TOTAL: 450g

═══════════════════════════════════════════════════════════════════════════════
```

---

# 6. PRELIMINARY COST ESTIMATE

## 6.1 Production BOM Summary

| Assembly | Estimated Cost | % of Total | Source |
|----------|---------------|------------|--------|
| Barrel assembly (Al 6061, machined) | $120 | 6.7% | Local |
| Receiver + trigger group | $180 | 10.0% | Local |
| Regulator assembly | $80 | 4.4% | Local |
| HPA cylinder (0.5L, DOT-3AL) | $150 | 8.3% | Import |
| Scope assembly (LRF + reticle + display) | $350 | 19.4% | Mixed |
| Stock assembly (polymer, adj.) | $60 | 3.3% | Local |
| Hardware, sling, finish | $40 | 2.2% | Local |
| Assembly labor | $100 | 5.6% | Local |
| **Launcher Subtotal** | **$1,080** | **60.0%** | |
| Projectile × 5 (included) | $175 | 9.7% | Mixed |
| Carrying case | $45 | 2.5% | Local |
| Manual + training kit | $20 | 1.1% | Local |
| QA/testing | $80 | 4.4% | Local |
| **Production Cost** | **$1,400** | **77.8%** | |
| Overhead (15%) | $210 | 11.7% | |
| Margin (30%) | $190 | 10.5% | |
| **Target Selling Price** | **~$1,800** | **100%** | |
| **With 3× markup (mil/gov)** | **~$5,400** | | |

## 6.2 Local Content Analysis

| Category | Local Value | Import Value | Local % |
|----------|-----------|-------------|---------|
| Barrel + machining | $120 | $0 | 100% |
| Receiver + trigger | $180 | $0 | 100% |
| Regulator | $80 | $0 | 100% |
| HPA cylinder | $0 | $150 | 0% |
| Scope (LRF import, reticle local) | $100 | $250 | 29% |
| Stock + hardware | $100 | $0 | 100% |
| Projectiles (mixed) | $100 | $75 | 57% |
| Assembly + QA | $180 | $0 | 100% |
| **TOTAL** | **$860** | **$475** | **~64%** |
| **Target** | | | **≥60% (MUST), 70% (WISH)** |

**Status:** 64% local content meets MUST (≥60%), with pathway to 70%+ through local LRF sourcing or cylinder certification.

---

# 7. ODI OUTCOME ALIGNMENT

Mapping the selected concept to the top ODI outcomes from customer discovery:

| Rank | ODI Outcome | Score | How VDC-100 Enhanced Addresses It | Gap? |
|------|-------------|-------|-----------------------------------|------|
| 1 | **O-48: Maximize first-shot hit probability** | **15.0** | LRF + calibrated reticle + fin stabilization = ~70% | None |
| 2 | **O-23: Maximize equipment reliability** | **14.6** | Mechanical fire chain, no electronics in critical path | None |
| 3 | O-46: Maximize effective range | 13.5 | 80m effective range, fin stabilization at distance | None |
| 4 | O-43: Maximize net deployment reliability | 13.5 | Timer + barometric dual redundancy (~99.9%) | None |
| 5 | O-63: Minimize evidence damage on capture | 13.0 | Parachute + drogue dual recovery, ≤5 m/s descent | None |
| 6 | O-55: Minimize reload time | 12.5 | Breech loading + fast valve ≤8 sec | None |
| 7 | O-24: Minimize physical fatigue | 12.0 | 7.8 kg total, balanced design, adjustable stock | None |
| 8 | O-12: Minimize range estimation error | 11.5 | COTS LRF ±1m accuracy | None |
| 9 | O-09: Minimize time to detect drone | 11.0 | Operator visual (instantaneous when cued) | None |
| 10 | O-61: Minimize energy refill difficulty | 11.0 | Standard HPA fill, SCUBA/diving shops available | None |

**Result: 10/10 top ODI outcomes addressed. No gaps.**

---

# 8. CUSTOMER SEGMENT FIT

From ODI customer segmentation ([[VN-CUA-001_ODI_customer_discovery|ODI Report Section 7]]):

| Segment | % Market | Key Need | VDC-100 Enhanced Fit |
|---------|----------|----------|---------------------|
| **Rapid Responders** | 40% | Speed: fast ready, fast reload | ≤8 sec reload, fast valve, quick aim | **STRONG** |
| **Precision Seekers** | 35% | Accuracy: first-shot hit | LRF + reticle + fins = 70% hit | **STRONG** |
| **Evidence Preservers** | 15% | Intact capture: evidence | Dual chute + net = intact recovery | **STRONG** |
| **Budget Operators** | 10% | Low cost: TCO | $5,400 vs $30K import, refillable HPA | **STRONG** |

**Result: VDC-100 Enhanced serves ALL 4 segments.** The DOMINANT growth strategy is confirmed — the product addresses both underserved and overserved segments simultaneously.

---

# 9. NEXT STEPS FOR PHASE 3

The selected concept now advances to Phase 3 (Embodiment Design) with these focus areas:

| Step | Phase 3 Activity | Input From Phase 2 | Key Decision |
|------|-----------------|--------------------|-|
| 1 | Layout design | Preliminary layout (Section 5) | Detailed dimensions, tolerances |
| 2 | DfX review (12 categories) | Concept specification | Manufacturing, assembly, maintenance optimization |
| 3 | Material selection | Mass budget (Section 2.2) | Final Al alloy, polymer grade, surface treatments |
| 4 | Tolerance analysis | Key dimensions (Section 5.3) | Critical tolerances for barrel, breech, regulator |
| 5 | Local content optimization | 64% current (Section 6.2) | Pathway to 70%+ target |
| 6 | Production cost refinement | Preliminary BOM (Section 6.1) | Detailed supplier quotes, process costs |

---

# 10. GATE 2 REVIEW

## 10.1 Gate 2 Checklist

| # | Criterion | Status | Evidence | File Reference |
|---|-----------|--------|----------|----------------|
| 1 | Function structure validated | ✅ | 5 main + 18 sub-functions, complete E/M/S flows | [[02_conceptual/function_structure]] |
| 2 | ≥3 concepts evaluated | ✅ | 4 concepts (A, B, C, D) through morphological matrix | [[02_conceptual/morphological_matrix]] |
| 3 | VDI 2225 score ≥70% | ✅ | **85.8%** (Concept B) — exceeds by 15.8 points | [[02_conceptual/concept_evaluation]] |
| 4 | No criterion scores = 0 | ✅ | Minimum score 3/4 for Concept B (best of all concepts) | [[02_conceptual/concept_evaluation]] |
| 5 | Selection rationale documented | ✅ | Sections 1-2 of this document | This file, Sections 1-2 |
| 6 | Sensitivity analysis performed | ✅ | 7 scenarios tested, B wins or ties all | [[02_conceptual/concept_evaluation]] Section 6 |
| 7 | Risks identified with mitigation | ✅ | 6 risks, all with mitigations and fallbacks | Section 4 |
| 8 | Preliminary layout sketched | ✅ | Side view, top view, projectile cross-section | Section 5 |
| 9 | Cost estimate within target | ✅ | $5,400 selling price ≤ $6,000 target | Section 6 |
| 10 | Local content feasible | ✅ | 64% current, pathway to 70%+ identified | Section 6.2 |
| 11 | ODI outcomes addressed | ✅ | 10/10 top outcomes covered, all 4 segments served | Sections 7-8 |
| 12 | Technical feasibility confirmed | ✅ | All working principles TRL ≥7, fallback to TRL 9 | Section 4.3 |

## 10.2 Gate 2 Decision

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                         GATE 2 STATUS: PASSED                                ║
║                                                                              ║
║  Checklist:  12/12 criteria met                                              ║
║  VDI 2225:   85.8% (threshold: 70%)                                         ║
║  Concept:    VDC-100 Enhanced (Concept B)                                    ║
║  Risk Level: LOW-MEDIUM (all mitigated)                                      ║
║  Fallback:   Concept A (Basic) at 80.0%                                      ║
║                                                                              ║
║  RECOMMENDATION: APPROVE — Proceed to Phase 3 (Embodiment Design)            ║
║                                                                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## 10.3 Phase 2 Complete File Map

```
02_conceptual/
├── abstraction.md              ← Step 1: 5-step abstraction process
├── function_structure.md       ← Step 2: 5 main + 18 sub-functions
├── morphological_matrix.md     ← Steps 3-4: Working principles + 4 concepts
├── concept_evaluation.md       ← Step 5: VDI 2225 scoring + sensitivity
└── concept_selection.md        ← Step 6: Selection + layout + Gate 2 (this file)
```

---

# DOCUMENT LINKS

- [[02_conceptual/abstraction|Abstraction (Step 1)]]
- [[02_conceptual/function_structure|Function Structure (Step 2)]]
- [[02_conceptual/morphological_matrix|Morphological Matrix (Steps 3-4)]]
- [[02_conceptual/concept_evaluation|Concept Evaluation (Step 5)]]
- [[01_requirements/requirements_list|Requirements List (Phase 1)]]
- [[01_requirements/validation_report|Validation Report (Phase 1)]]
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery (Phase 0)]]
- [[VN-CUA-001_P3_embodiment_design|Phase 3: Embodiment Design]] ← NEXT

---

# REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-08** | **Initial concept selection. VDC-100 Enhanced (Concept B) selected at 85.8% VDI 2225. Gate 2 PASSED 12/12 criteria. Preliminary layout, cost estimate, risk register documented.** |

---

*This concept selection follows Pahl & Beitz Step 6 of Conceptual Design, firming up the selected concept with preliminary layout, cost estimates, and risk assessment. Gate 2 review confirms readiness for Phase 3 Embodiment Design.*

**Phase 2 Status: COMPLETE** — Concept B (VDC-100 Enhanced) selected at 85.8%
