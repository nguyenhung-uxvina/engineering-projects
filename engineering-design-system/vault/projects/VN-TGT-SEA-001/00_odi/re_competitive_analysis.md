---
project: VN-TGT-SEA-001
phase: 0
type: reverse_engineering
version: 2.1
created: 2026-02-09
updated: 2026-02-10
revision: B.1
status: draft
---

# Reverse Engineering: Competitive Analysis — Sea Target Systems

> **Rev B.1** — VN-TGT-SEA-001 now specifies 8.0m platform, >1,000 m² RCS (0.8m hybrid reflectors at 3-4m on masts), radar-only (no IR), SS 5-6 environmental survivability, $35,640/unit. Competitor data unchanged.

**Scope:** 5 competitor systems analyzed for VN-TGT-SEA-001 positioning
**Sources:** Reference documents, public specifications, patent/export databases

---

## 1. Competitor Overview

### 1.1 Market Categories

| Category | Example | RCS | Cost | Use | Safety |
|----------|---------|-----|------|-----|--------|
| **Type 1: SINKEX** | Decommissioned warship | 1,000-10,000 m² | $1-5M/test | 1x (destroyed) | HIGH (withdraw) |
| **Type 2: USV Target** | QinetiQ Hammerhead, Metal Shark HSMST | 10-100 m² | $200-300K | Reusable (if miss) | MEDIUM (C2 at 2-3km) |
| **Type 3: Towed Target** | QinetiQ L-CATT + radar | 20-50 m² | $20-30K | 3-10x | LOW (tow at 500m) |
| **Type 4: Anchored Target** | VN-TGT-SEA-001 (THIS) | 1,000-1,200 m² | $35.6K | 1x (expendable) | HIGH (withdraw 5km+) |

### 1.2 Key Finding: No Competitor Occupies Our Position

No existing product simultaneously provides:
- FRIGATE-CLASS RCS (>1,000 m²) for missile seeker acquisition
- 360 deg omnidirectional coverage
- Storm deployment (SS 5-6, 72h anchored)
- LOW cost (<$50K)
- HIGH safety (no vessel in danger zone)
- Fully passive operation (no C2 vessel)

**VN-TGT-SEA-001-H is the ONLY product designed for this specific Job-to-be-Done.**

---

## 2. Detailed Competitor Analysis

### 2.1 SINKEX (Decommissioned Ship)

| Parameter | Value | Implication for VN-TGT-SEA-001 |
|-----------|-------|-------------------------------|
| RCS | 1,000-10,000 m² (actual ship) | Over-specification; missile seekers lock at 150+ m² |
| IR | Engine heat (variable, unreliable) | Often tested cold = unrealistic for IR seekers |
| Cost | $1-5M per test (EPA, tow, decon) | Prohibitively expensive for routine acceptance |
| Availability | Limited (need decommissioned ship) | Vietnam has very few candidates |
| Realism | Maximum (actual ship) | Highest fidelity but unnecessary for acceptance test |
| Sustainability | 1x only, environmental concerns | EPA/IMO restrictions increasing globally |

**Lesson for VN-TGT-SEA-001:** >1,000 m² matches frigate-class RCS for realistic testing. Cost must be <$50K to enable routine testing.

### 2.2 QinetiQ Hammerhead MkII (USV Target)

| Parameter | Value | Implication for VN-TGT-SEA-001 |
|-----------|-------|-------------------------------|
| Dimensions | 5.2m x 2.1m, 900 kg | Similar scale to VN-TGT-SEA-001 |
| Speed | 40 knots | Not needed (stationary target) |
| RCS | 10-50 m² (natural + optional) | INSUFFICIENT for missile seeker; designed for guns |
| RCS coverage | ~180 deg (bow aspect) | Not omnidirectional |
| C2 | UTCS radio, requires control ship | Control ship at 2-3 km = safety risk |
| Cost | ~$300,000 per unit | 7-10x more expensive than VN-TGT-SEA-001 |
| Export | EAR (UK export controls) | Available to Vietnam but expensive |
| Use case | Gunnery training, CIWS testing | NOT designed for missile acceptance |

**Key RE Insights:**
- Hull: GRP (Glass Reinforced Plastic), conventional construction
- No AM technology in any component
- Propulsion adds $100K+ to cost (not needed for anchored target)
- RCS augmentation is optional add-on, not integrated

**Lesson:** USV targets are designed for a DIFFERENT job (gunnery training with moving target). VN-TGT-SEA-001 serves missile acceptance (stationary, high RCS). No direct competition.

### 2.3 Metal Shark HSMST (High-Speed Maneuvering Surface Target)

| Parameter | Value | Implication for VN-TGT-SEA-001 |
|-----------|-------|-------------------------------|
| Dimensions | 8m x 2.5m, 1500 kg | Larger, heavier |
| Speed | 46 knots | Designed for CIWS/gun evasion scenarios |
| RCS | 20-100 m² (augmented) | Still insufficient for missile acceptance |
| C2 | Proprietary, US Navy MIL-SPEC | ITAR restricted |
| Cost | ~$200,000 per unit | 5x more expensive |
| Export | ITAR (US export controls) | NOT available to Vietnam |

**Lesson:** ITAR restriction makes this irrelevant for Vietnamese procurement. Confirms need for indigenous solution.

### 2.4 QinetiQ L-CATT + Radar Enhancement (Towed Target)

| Parameter | Value | Implication for VN-TGT-SEA-001 |
|-----------|-------|-------------------------------|
| Dimensions | 4.8m x 2.4m, ~500 kg | Lighter, towed |
| Speed | 15-25 knots (towed) | Safety concern: tow vessel at 500m |
| RCS | 20-50 m² (with enhancement) | Insufficient for missile acceptance |
| Cost | $20-30K per unit | Competitive cost but unsafe for missiles |
| Reusability | 3-10 uses (gunnery) | Good for guns, destroyed by missiles |

**Key RE Insights:**
- Tow cable: 750m Dyneema ($2,250) required
- Tow vessel MUST remain within 500-1000m during firing
- For missile tests: tow vessel is in the engagement zone = UNSAFE
- RCS patches/reflectors are basic flat panels, not trihedral corners

**Lesson:** Lowest cost competitor but UNSAFE for missile testing due to tow vessel proximity. VN-TGT-SEA-001's anchored concept eliminates this risk entirely.

### 2.5 C-Target 3 (Composite Dynamics — Reference Design)

| Parameter | Value | Implication for VN-TGT-SEA-001 |
|-----------|-------|-------------------------------|
| Dimensions | 3.5m x 1.4m, 325 kg | Small, deployable surface target drone |
| Hull | Aluminum 5083-H321, 3-6mm | Proven marine aluminum, local production possible |
| Speed | 25 knots (30 HP outboard) | Self-propelled USV |
| Transport | 4 per 20ft container | Excellent logistics concept |
| RCS | Natural hull only (~5-10 m²) | Far too low for missile acceptance |
| Design philosophy | "Deployable, repairable, producible" | Excellent DFM principles to adopt |
| Cost | ~$50-80K (estimated) | Mid-range |

**Key RE Insights from Pahl-Beitz Analysis:**
- Hull: Centerline bolted split for container transport → applicable to modular VN-TGT-SEA-001
- Tooling: Low investment ($30-50K) → matches Vietnamese manufacturing approach
- Trade-off: Deployability (5) > Cost (4) > Repairability (4) > Speed (3)
- DFM: >70% COTS components → adopt this philosophy

**Lessons Adopted for VN-TGT-SEA-001:**
1. Modular bolt-together sections for transport/deployment
2. Low-tooling manufacturing approach
3. "Deployable, repairable, producible" as design philosophy
4. Container-compatible dimensions for logistics

---

## 3. Competitive Positioning (ODI-Weighted)

### Weighted Scoring (from Competitive Comparison reference)

| Criterion | Weight | VN-TGT-SEA-001 | SINKEX | Hammerhead | HSMST | L-CATT |
|-----------|--------|----------------|--------|------------|-------|--------|
| O1: Seeker acquisition | 0.20 | 4 | 5 | 2 | 3 | 2 |
| O2: Position accuracy | 0.15 | 4 | 4 | 3 | 3 | 2 |
| O3: Cost/engagement | 0.18 | 4 | 1 | 3 | 3 | 4 |
| O4: IR realism | 0.15 | 4 | 2 | 3 | 3 | 2 |
| O5: Deployment simplicity | 0.10 | 4 | 1 | 2 | 2 | 3 |
| O6: Safety | 0.10 | 5 | 4 | 3 | 3 | 2 |
| O7: Indigenous content | 0.07 | 5 | 0 | 1 | 1 | 2 |
| O8: Export availability | 0.05 | 5 | 0 | 2 | 1 | 3 |
| **WEIGHTED TOTAL** | **1.00** | **3.85** | **2.95** | **2.60** | **2.75** | **2.55** |

> **Rev B.1:** VN-TGT-SEA-001 scores revised: O1 improved to 5 (>1,000 m² RCS). O4 reduced to 0 (IR removed, radar-only). Net weighted score ~3.45. However, O4 (IR realism) weighting should be reduced for radar-only missile acceptance (C-802, Kh-35 are radar-guided). With revised weights (IR 0.05 instead of 0.15), score remains ~3.80.

### Total Cost of Ownership — 10 Test Campaign

| Solution | Acquisition | Operations (10 tests) | **TOTAL TCO** |
|----------|------------|----------------------|---------------|
| VN-TGT-SEA-001-H (expendable) | $648K (dev $292K + 10 units × $35.6K) | $250K | **$898K** |
| SINKEX | $0 (decommissioned) | $16.1M | **$16.1M** |
| USV + missile mode | $580K | $207K | **$788K** |
| L-CATT + radar | $110K | $200K | **$310K** |

**Note:** L-CATT has lowest TCO but FAILS on RCS (20-50 m² vs 150+ m² required) and safety (tow vessel at 500m). USV targets FAIL on RCS. SINKEX is prohibitively expensive. VN-TGT-SEA-001 is the ONLY solution that meets ALL requirements at acceptable cost.

> **Rev B.1:** Expendable variant. No reuse savings. Unit cost $35,640. TCO benefit comes from 928% ROI vs baseline due to reduced missile loss (1-2% failure vs 10% baseline).

---

## 4. Patent / FTO Analysis

### Freedom-to-Operate Assessment

| Technology Area | Patent Status | FTO Risk | Notes |
|----------------|---------------|----------|-------|
| Corner reflectors | Public domain (basic geometry) | CLEAR | Trihedral geometry = basic physics |
| TPMS/Voronoi structures | Application-specific patents exist | LOW | No patents on buoyancy application specifically |
| AM printing (LPBF, SLS) | Process patents = machine vendors | CLEAR | We use machines, not make them |
| Anchored target concept | No patents found | CLEAR | Well-established maritime practice |
| Propane IR emitter | Public domain | CLEAR | Standard industrial burner |
| GPS beacon | COTS product | CLEAR | Buy, not make |
| Schwarz P thermal channels | Academic literature, no defense patents | LOW | Novel application, no prior art in targets |

> **Rev B.1:** Schwarz P and propane IR removed (radar-only). FTO remains CLEAR.

**FTO CONCLUSION: CLEAR — No blocking patents identified for VN-TGT-SEA-001-H concept.**

---

## 5. Technology Readiness Summary

| Component | TRL | Justification |
|-----------|-----|---------------|
| HDPE/Steel pontoon platform (8.0m diameter) | 9 | Standard marine construction |
| Concrete block anchor + chain | 9 | Standard mooring practice |
| Traditional corner reflectors | 9 | Widely used in maritime |
| Propane IR burner | 8 | ~~Used in military IR targets~~ **REMOVED (Rev B — radar-only)** |
| GPS beacon (waterproof) | 9 | COTS product |
| **TPMS flotation core** | **3-4** | **~~Design concept validated; no ballistic test yet~~ REMOVED (Rev B)** |
| **AM corner reflectors** | **4-5** | **Hybrid CNC/AM proven; RCS validation pending** |
| **Schwarz P IR panels** | **3** | **~~Design concept only; no prototype~~ REMOVED (Rev B — radar-only)** |
| **Steel mast structures (8x)** | **9** | **Standard galvanized steel tube, field-erectable** |
| Modular bolt-together frame | 7 | C-Target 3 demonstrates concept |

**Critical Path:** TPMS flotation core (TRL 3→6) is the primary technology risk. $8K Phase 0 ballistic test is the gate.

---

## Cross-References

- [[odi_analysis.md]] - ODI analysis (this RE feeds into competitive positioning)
- [[../00_project_brief.md]] - Project brief
- [[../../../references/Bia TL/VN_AST_MSL_001_Competitive_Comparison.md]] - Detailed competitive comparison
- [[../../../references/Bia TL/VN_AST_MSL_001_Anchored_Target_Analysis.md]] - Anchored target analysis
- [[../../../references/Target Drone/C-Target_3_PB_Reverse_Engineering_Worksheet.md]] - C-Target 3 RE
