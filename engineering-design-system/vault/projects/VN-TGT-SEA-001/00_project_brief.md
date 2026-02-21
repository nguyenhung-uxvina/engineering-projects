---
project: VN-TGT-SEA-001
phase: 0
type: project_brief
version: 2.1
created: 2026-02-09
updated: 2026-02-10
status: active
revision: B.1
---

# Project Brief: VN-TGT-SEA-001

> **Rev B.1** — Updated for 8.0m platform, superstructure removed, IR/propane removed (radar-only), reflectors elevated to 3-4m on steel masts. See [[00_odi/phase0_final_revision.md]] for full analysis.

## 1. Product Identity

| Field | Value |
|-------|-------|
| **Code** | VN-TGT-SEA-001 |
| **Name** | Fixed Sea Target with Hyperganic Enhancement |
| **Codename** | "THANH TRI-H" (Fortress-Hyperganic) |
| **Category** | Naval test & evaluation equipment |
| **Type** | Anchored stationary missile acceptance target |
| **Base Product** | VN-AST-MSL-001 "THANH TRI" (Fortress) |
| **Enhancement** | Hybrid AM/CNC corner reflectors for precision RCS |

---

## 2. Problem Statement

### Essential Problem (Vietnamese)
> "Cung cap muc tieu co dinh co dac tinh radar tuong duong tau chien (>1.000 m² RCS), duoc neo tai vi tri xac dinh trong dieu kien bien dong (SS 5-6), cho phep ban ten lua nghiem thu ma khong can tau keo hien dien trong vung nguy hiem."

### Essential Problem (English)
> "Provide a STATIONARY target with frigate-class radar signature (>1,000 m² RCS), ANCHORED at designated position in rough sea conditions (SS 5-6), enabling warship missile acceptance firing WITHOUT any vessel in the danger zone."

### Why This Product
Vietnam's Navy requires regular anti-ship missile acceptance testing (C-802, Kh-35, Exocet). Current approaches:
- **SINKEX (decommissioned ships):** $1-5M per test, environmentally problematic, limited supply
- **USV targets (Hammerhead, HSMST):** $200-300K, insufficient RCS (10-100 m² vs required >1,000 m²), C2 vessel in danger zone
- **Towed targets (L-CATT):** $20-30K but tow vessel at 500m during firing = UNSAFE for missile tests
- **Ad-hoc target barges:** Unstandardized, no signature control, limited to fair weather

**Gap:** No standardized product combines FRIGATE-CLASS RCS (>1,000 m²) + STORM-SURVIVABLE deployment (SS 5-6) + LOW cost (<$40K) + HIGH safety (no vessel in danger zone). VN-TGT-SEA-001 fills this gap.

---

## 3. Key Innovation: Hyperganic Enhancement

The base product VN-AST-MSL-001 is a conventional anchored target. The Hyperganic enhancement adds additive manufacturing (AM) technology for the critical RCS subsystem:

### 3.1 AM Precision Corner Reflector Frames (Layer 3 — CORE INNOVATION)
- **Technology:** Hybrid CNC 6061-T6 face plates + AM AlSi10Mg LPBF mounting frames
- **What:** 8 trihedral reflectors (0.8m edge) with 90° ±0.1° tolerance (vs ±0.5° traditional)
- **Impact:** >1,000 m² frigate-class RCS, 360° omnidirectional, ±2 dB variation
- **Benefit:** Near-certain missile seeker acquisition, 1-2% test failure rate (vs 10-15%)

### 3.2 Removed Components (Rev B)
| Component | Status | Reason |
|-----------|--------|--------|
| ~~TPMS Voronoi/Gyroid flotation core~~ | **REMOVED** | User directive — expendable target, no ballistic survivability needed |
| ~~Schwarz P thermal distribution panels~~ | **REMOVED** | Rev B — radar-only target, no IR signature |
| ~~Superstructure (ship silhouette)~~ | **REMOVED** | Rev B — no visual profile needed |
| ~~Topology-optimized joints~~ | Merged into reflector AM frames | Simplified architecture |

---

## 4. Architecture (Rev B.1)

```
LAYER 3: SIGNATURE MODULE (Hybrid AM/CNC - Core Innovation)
  8× corner reflectors (0.8m edge, CNC faces + AM frames)
  Mounted on 8× galvanized steel masts (60mm×4mm, 3-4m AGL)
  1,000-1,200 m² RCS, 360°, ±2 dB variation
  Radar-only signature (no IR, no visual profile)

LAYER 2: STRUCTURAL FRAME (Traditional)
  Steel frame with reinforced mooring attachment (pad eye)
  Self-draining deck with scuppers
  8× mast deck sockets (welded flange plates)
  Nylock/safety wire on all bolts

LAYER 1: FLOTATION (Traditional)
  HDPE hull (8.0m diameter circular pontoon)
  Closed-cell marine foam fill
  >93% reserve buoyancy

LAYER 0: MOORING SYSTEM (Storm-Rated - Pre-Deployable)
  Danforth/Bruce anchor (30-50 kg)
  12-16mm G30 chain + polyester rode (depth-dependent)
  Pre-deployed in fair weather, target connected later
  72h+ GPS beacon on elevated mast (≥4.5m AGL)
```

---

## 5. Target Specifications (Rev B.1)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Platform diameter** | 8.0 m ±0.1 m (circular pontoon) | Rev B: increased from 6.0m for stability |
| **Height above water** | 3.0-4.0 m (reflector center on masts) | Rev B.1: elevated on steel masts |
| **Displacement** | 980 kg (loaded) | Rev B.1: includes mast system |
| **RCS (X-band)** | >1,000-1,200 m², 360° | 8 × 0.8m hybrid reflectors, 45° spacing |
| **RCS variation** | ≤ ±2 dB through 360° | AM precision mounting frames |
| **RCS minimum (any angle)** | ~770 m² | 5× above seeker threshold |
| **Signature type** | **Radar-only** | Rev B: no IR, no visual profile |
| **Position hold** | ±70-240 m (depth dependent) | Storm-rated mooring, single-point |
| **Sea state (deploy/tow)** | SS 4-5 | Tow in moderate-rough seas |
| **Sea state (survive)** | SS 5-6, Bft 6-7, 72h anchored | Environmental survivability |
| **Deployment time** | 30 min from mooring pickup | Pre-deployed mooring concept |
| **Crew required** | 3-4 personnel (tug crew) | No specialist required |
| **GPS beacon** | ±5m, 1 Hz, 72h+ battery | Elevated mount ≥4.5m AGL |
| **Missile compatibility** | C-802, Kh-35, Exocet, X/Ku-band seekers | Active radar guided |
| **Unit cost** | **$35,640 @ 10 units** | Rev B.1 (was $37,730 v1.0) |
| **Indigenous content** | 85-90% | GPS module + AM frames import |

---

## 6. Competitive Positioning (Rev B.1)

| Criterion | VN-TGT-SEA-001-H | SINKEX | USV Targets | Towed Targets |
|-----------|-------------------|--------|-------------|---------------|
| **RCS** | **1,000-1,200 m² 360°** | 1,000-10,000 m² | 10-100 m² | 20-50 m² |
| **Signature** | Radar-only | Full (uncontrolled) | Optional | Optional |
| **Sea state (survive)** | **SS 5-6 (72h)** | N/A | SS 4 | SS 3 |
| **Cost/engagement** | **$35.6K** | $1-5M | $200-300K | $20-30K |
| **Safety** | 5+ km clearance | 5+ km clearance | C2 at 2-3 km | Tow at 500m |
| **Indigenous** | 85-90% | N/A | ITAR/EAR | Import |
| **Test failure rate** | 1-2% | 2% | 15% | 20% |

**Unique value proposition:** The ONLY product combining >1,000 m² frigate-class RCS + SS 5-6 storm deployment + fully passive operation at $35.6K/unit. Previously only achievable by sinking a real ship ($1-5M per test).

---

## 7. Budget & Timeline

### Development Budget
| Phase | Budget | Key Deliverable | Timeline |
|-------|--------|-----------------|----------|
| Phase 0: ODI & Feasibility | $12,000 | Customer insight, competitive analysis | 2026 Q1 |
| Phase 1: Requirements | $55,000 | 116 requirements, basic prototype | 2026 Q1-Q2 |
| Phase 2: Conceptual Design | $35,000 | AM reflector validation, storm mooring trial | 2026 Q3 |
| Phase 3: Embodiment Design | $100,000 | Integrated prototype, sea trials, seeker test | 2026 Q4-2027 Q1 |
| Phase 4: Detail Design | $90,000 | Production readiness, pilot batch | 2027 Q2-Q3 |
| **TOTAL** | **$292,000** | | **15-18 months** |

### ROI Projection (3-year, 50 tests)
- **VN-TGT-SEA-001-H:** $2,692,000 total ($53,840/test)
- **Current baseline:** $5,400,000 total ($108,000/test)
- **Savings:** $2,708,000 (50% reduction)
- **ROI:** 928% vs current baseline

---

## 8. Technology Reuse (Cross-Portfolio)

| Technology | Reuse Target | Value |
|-----------|-------------|-------|
| AM corner reflector frames | Radar simulation, EW training, navigation buoys | HIGH |
| Hybrid CNC/AM precision assembly | Any precision reflector/antenna application | HIGH |
| Storm mooring system | Other anchored marine targets, buoys | MEDIUM |
| Pre-deploy mooring concept | All anchored marine equipment | MEDIUM |

---

## 9. Key Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AM reflector RCS mismatch | 15% | MEDIUM | Well-established physics; validate with prototype |
| Military rejects AM components | 50% | HIGH | Live-fire demo; cite GE Aviation AM adoption |
| Mooring fails in SS 6 | 20% | HIGH | Proper marine anchor, pre-deploy and verify |
| Reflector mount failure in waves | 15% | MEDIUM | Nylock bolts, safety wire, AM alignment pins |
| AM cost exceeds budget | 10% | LOW | Hybrid approach 60-70% cheaper than full AM |

---

## 10. Decision Gates (Revised)

| Gate | Criteria | Cost | No-Go Action |
|------|----------|------|--------------|
| **H1:** AM reflector RCS validation | RCS within ±1 dBsm of target | $15,000 | Adjust frame geometry; fallback to full CNC |
| **H2:** Storm mooring sea trial | Target holds anchor in SS 5 for 72h | $5,000 | Upgrade chain/rode; revise mooring design |
| **H3:** Production readiness | AM reflector library + assembly manual | $20,000 | Simplify to CNC-only variant |

---

## 11. Cross-References

- [[PROJECT_STATUS.md]] - Project status tracker
- [[00_odi/odi_analysis.md]] - ODI analysis (73 outcomes)
- [[00_odi/re_competitive_analysis.md]] - Competitive analysis (6 competitors)
- [[00_odi/hyperganic_feasibility.md]] - AM feasibility (retained as reference)
- [[00_odi/re_deep_analysis.md]] - Deep RE subsystem teardown
- [[00_odi/phase0_synthesis.md]] - Phase 0 synthesis (cost model)
- [[00_odi/environmental_survivability.md]] - Environmental survivability (SS 5-6)
- [[00_odi/phase0_final_revision.md]] - Final revision (>1,000 m² RCS)
- [[../../references/VN_Fixed_Sea_Target_Hyperganic_Enhancement.md]] - Hyperganic evaluation
- [[../../references/VN_FIXED_SEA_TARGET_Complete_Analysis.md]] - Complete sea target analysis
