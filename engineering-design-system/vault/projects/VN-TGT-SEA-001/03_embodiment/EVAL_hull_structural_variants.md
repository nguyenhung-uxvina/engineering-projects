---
project: VN-TGT-SEA-001
phase: 3
type: variant_evaluation
step: "Hull Structural Concept — VDI 2225 Evaluation"
version: 1.0
created: 2026-02-10
status: draft
---

# HDPE Hull Structural Concept Evaluation — VDI 2225

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Evaluate alternative structural concepts for the M1 HDPE hull platform using VDI 2225 weighted scoring. This evaluation goes beyond E10 Decision 1 (which compared fabrication methods) to assess fundamentally different hull **structural configurations**.
**Method:** VDI 2225 weighted evaluation (0–4 scoring, 8 criteria)
**Input:** [[PRAD_D8_design_structure.md]] (hydrostatic stability, wave loads), [[DECS_D9_detail_specification.md]] (hull specs), [[OCP_C14_cost_analysis.md]] (M1 BOM), [[OCP_P15_production_planning.md]] (suppliers, manufacturing)
**Context:** E10 Decision 1 selected **2-section bolted** fabrication over 1-piece rotomold and 2-section welded (85.0%). That decision fixed the **joining method**. This evaluation now assesses the **hull structural form** — what the cross-section looks like, how buoyancy is achieved, and how the hull resists loads.

---

## 1. Scope and Approach

### 1.1 Why Evaluate Hull Structure?

The hull is the largest subsystem (350 kg, 35.5% of displacement, $4,118 = 23% of M1–M8 material cost). The current design — a foam-filled ring pontoon — was inherited from Phase 2 Concept A without formal evaluation against structurally different alternatives. Before committing $9.2K to a hull prototype ([[PROTO_hull_platform_validation.md]]), it is prudent to confirm that the ring pontoon structural concept is optimal.

### 1.2 What This Evaluation Covers

| In Scope | Out of Scope |
|----------|-------------|
| Hull cross-section geometry (ring vs disc vs pipe) | Hull material (HDPE is fixed — M4 selected at 88.8%) |
| Buoyancy method (foam vs compartments vs sealed pipe) | Joining method (2-section bolted is fixed — E10 at 85.0%) |
| Hull depth (500 mm vs compact alternatives) | Frame design (M2 is fixed per D8/A7) |
| Impact on freeboard, stability, mass, cost | Reflector, mast, mooring design |

### 1.3 Constraints (Non-Negotiable)

All variants must satisfy these hard requirements:

| Constraint | Requirement | Source |
|-----------|-------------|--------|
| Platform diameter | 8.0 m | GEO-001 |
| Total system mass | ≤1,100 kg | GEO-007 |
| Transportable | ≤2.5 m width per section | TRA-002 |
| Survive SS 5–6 | 72 h anchored, Bft 6–7 | OPR-002 |
| Unsinkable (goal) | Float after hull breach | SAF-003 |
| Support 8 mast sockets | IF-03, at R = 3,200 mm | A7 architecture |
| Central mooring pad eye | IF-02, through-hull | A7 architecture |
| Freeboard | ≥300 mm (operational target) | OPR-005, D8 |

---

## 2. Variant Descriptions

### 2.1 Variant A: Foam-Filled Ring Pontoon, 500 mm Depth (CURRENT BASELINE)

```
CROSS-SECTION — Variant A: Foam-Filled Ring Pontoon
=====================================================

               SOLID HDPE DECK (self-draining, non-skid)
   +================================================================+
   |  ≥8 mm HDPE wall                                                |
   |  +----------------------------------------------------------+  |
   |  |                                                          |  |
   |  |   Closed-cell PU foam fill (40 kg/m³)                   |  |
   |  |   80% fill factor — unsinkable reserve                  |  |  500 mm
   |  |                                                          |  |  depth
   |  |                                                          |  |
   |  +----------------------------------------------------------+  |
   |  ≥8 mm HDPE wall                                                |
   +================================================================+

   |<------------- 500 mm ring width (pontoon section) ------------>|

   Hull outer diameter: 8,000 mm
   Hull inner diameter: ~7,000 mm
   Center: open deck (HDPE sheet or grating, self-draining via scuppers)
```

**Key characteristics:**
- Annular ring pontoon, 500 × 500 mm cross-section, ≥8 mm HDPE wall
- Closed-cell PU foam fill at 80% (provides unsinkable reserve buoyancy)
- Solid deck spanning center area (effective waterplane = full 50.27 m²)
- Hull shell mass: ~200 kg; foam: ~121 kg; accessories: ~29 kg → **Total M1: 350 kg**
- BOM: **$4,118** (C14)
- Draft: 19.1 mm → Freeboard: **481 mm**
- Reserve buoyancy: 96.2% (25,768 kg buoyancy at deck edge vs 986 kg displacement)
- Foam-only buoyancy: 2,975 kg >> 986 kg → **UNSINKABLE**
- 2-section bolted at diameter (IF-07: 24× M10 SS316, EPDM gasket, steel backing)

### 2.2 Variant B: Compartmented Ring Pontoon, 500 mm Depth (No Foam)

```
CROSS-SECTION — Variant B: Compartmented Ring (No Foam)
========================================================

               SOLID HDPE DECK
   +================================================================+
   |  ≥8 mm HDPE wall                                                |
   |  +--------+  +--------+  +--------+  +--------+  +--------+   |
   |  |        |  |        |  |        |  |        |  |        |   |
   |  |  AIR   |  |  AIR   |  |  AIR   |  |  AIR   |  |  AIR   |   |  500 mm
   |  |  (WTC) |  |  (WTC) |  |  (WTC) |  |  (WTC) |  |  (WTC) |   |  depth
   |  |        |  |        |  |        |  |        |  |        |   |
   |  +--------+  +--------+  +--------+  +--------+  +--------+   |
   |  ≥8 mm HDPE wall                                                |
   +================================================================+

   8× transverse HDPE bulkheads create 8 watertight compartments (WTC)
   Each bulkhead: 500 × 500 × 8 mm HDPE, perimeter-welded to hull wall
```

**Key characteristics:**
- Same ring geometry as Variant A (500 × 500 mm cross-section)
- 8× HDPE transverse bulkheads welded inside hull ring → 8 watertight compartments
- No foam fill — buoyancy from sealed air compartments
- Hull shell: ~200 kg; bulkheads (8× ~5 kg): ~40 kg; accessories: ~29 kg → **Total M1: 269 kg**
- Estimated BOM: **~$3,400** (saves foam $800, adds bulkhead welding $280)
- Draft: lighter hull → ~16 mm; Freeboard: **~484 mm** (slightly better)
- Reserve buoyancy: 96.2% (same hull geometry, less displacement)
- **NOT UNSINKABLE**: each compartment holds ~12.5% of hull buoyancy volume. 1 flooded → floats. 2 flooded → floats. **≥3 simultaneous → progressive flooding risk → may sink**
- Compartment integrity depends on 100% weld quality on 8 internal welds — difficult to inspect
- 2-section bolted same as A (2 bulkheads coincide with joint plane)

**Damage survival analysis:**
```
Ring pontoon volume: ~3.78 m³ (8 compartments × ~0.47 m³ each)

1 compartment flooded (12.5% loss):
  Lost buoyancy: 0.47 × 1,025 = 482 kg
  Remaining: 3,294 - 482 = 2,812 kg >> 986 kg → FLOATS (heel ~2°)

2 compartments flooded (25% loss):
  Lost buoyancy: 964 kg
  Remaining: 2,330 kg >> 986 kg → FLOATS (heel ~5°)

3 compartments flooded (37.5% loss):
  Lost buoyancy: 1,446 kg
  Remaining: 1,848 kg > 986 kg → FLOATS (heel ~10°, marginal)

4 compartments flooded (50% loss):
  Lost buoyancy: 1,928 kg
  Remaining: 1,366 kg > 986 kg → FLOATS but marginal (heel ~15°)

5+ compartments → SINKS (buoyancy < displacement)
```

### 2.3 Variant C: Foam-Filled Compact Ring, 300 mm Depth

```
CROSS-SECTION — Variant C: Compact Foam-Filled Ring (300 mm)
=============================================================

               SOLID HDPE DECK
   +================================================================+
   |  ≥8 mm HDPE wall                                                |
   |  +----------------------------------------------------------+  |
   |  |   Closed-cell PU foam fill (40 kg/m³)                   |  |
   |  |   80% fill factor                                       |  |  300 mm
   |  |                                                          |  |  depth
   |  +----------------------------------------------------------+  |
   |  ≥8 mm HDPE wall                                                |
   +================================================================+

   |<------------- 500 mm ring width (unchanged) ------------------>|

   Same 8,000 mm OD, 7,000 mm ID as Variant A
   Reduced depth: 300 mm (was 500 mm)
```

**Key characteristics:**
- Same ring OD/ID as A (8.0 m / 7.0 m), but **reduced depth: 300 mm** (−40%)
- Foam-filled at 80% → still unsinkable
- Lighter: Hull shell ~130 kg (−35%); foam ~73 kg (−40%); accessories ~22 kg → **Total M1: 225 kg**
- Estimated BOM: **~$2,850** (less HDPE, less foam)
- Draft: 19.1 mm (unchanged — same A_wp if solid center deck) → Freeboard: **281 mm**
- **CRITICAL: Freeboard 281 mm < 300 mm target → green water risk in SS 5–6**
- Reserve buoyancy: 93.4% (lower but still very high)

**Foam reserve buoyancy check:**
```
Internal volume (300 mm ring): 0.3/0.5 × 3.78 = 2.27 m³
Foam fill (80%): 1.81 m³ at 40 kg/m³ = 72.5 kg
Foam buoyancy (if hull completely lost):
  1.81 × (1,025 - 40) = 1.81 × 985 = 1,783 kg
  1,783 kg vs 886 kg displacement (lighter system) → ratio 2.01:1
  → UNSINKABLE (but margin reduced from 3.0× to 2.0×)
```

**Freeboard sensitivity:**
```
At 986 kg (full system): freeboard = 300 - 19 = 281 mm
At 1,100 kg (max allowable): freeboard = 300 - 21 = 279 mm
Green water onset: breaking wave crest = 0.6 × Hs = 0.6 × 5.0 = 3.0 m
  Wave orbital velocity at surface: v = π × Hs/Tp = 1.75 m/s
  Wave crest height above still waterline: ~0.6 × Hs/2 = 1.5 m (for deep water)
  At 8 m platform diameter, wave conforming: platform follows wave surface
  BUT deck edge submersion occurs when wave slope × radius > freeboard
  Wave slope at SS 6: θ = 2πHs/(g×Tp²) ≈ 0.039 rad = 2.2°
  Edge dip: 4.0 m × sin(2.2°) = 154 mm

At 281 mm freeboard: 281 - 154 = 127 mm margin → GREEN WATER MARGINAL
At 481 mm freeboard (Var A): 481 - 154 = 327 mm margin → SAFE
```

### 2.4 Variant D: COTS PE100 Pipe Ring Pontoon + Sheet Deck

```
CROSS-SECTION — Variant D: COTS Pipe Ring
===========================================

   TOP VIEW (octagonal):

            N
         ___+___
        /   |   \          8× straight DN315 PE100 pipe segments
       /    |    \         Each segment: ~3.14 m long
      / seg1|seg2 \        Joined at 22.5° mitre-welded elbows
     +------+------+       Flat HDPE sheet deck welded to pipe tops
     |      |      |
     + seg8 | seg3 +       Diameter: ~8.0 m across flats
     |      |      |
     +------+------+       Center: same open/solid deck as other variants
      \ seg7|seg4 /
       \    |    /
        \___|___/
          seg5,6

   CROSS-SECTION (through pipe):

            HDPE deck sheet (5 mm)
       ┌──────────────────────┐
       │    welded to pipe    │
       └─────┐        ┌──────┘
           ┌─┘        └─┐
          │   Foam fill   │     DN315 PE100 pipe
          │   in pipe     │     OD = 315 mm, wall = 7.7 mm (SDR 41)
          │   (optional)  │     Cross-section area: 74,400 mm²
           └─────────────┘

       Pipe provides structural ring beam + buoyancy volume
```

**Key characteristics:**
- 8× straight DN315 PE100 SDR 41 pipe segments arranged as octagonal ring
- OD 315 mm, wall 7.7 mm (SDR 41 = PN4, standard Vietnamese water pipe stock)
- Each segment ~3.14 m long (circumference/8). Joined at vertices by mitre-welded HDPE elbows (22.5°)
- Flat 5 mm HDPE sheet deck welded to pipe ring tops
- Pipes foam-filled and end-capped for unsinkability
- **Uses 100% COTS Vietnamese HDPE pipe** — Binh Minh, Tien Phong mass-produce this product

**Mass estimate:**
```
DN315 SDR 41 pipe: 7.4 kg/m × 25.1 m perimeter = 186 kg
HDPE deck sheet (5 mm, ring area ~11.8 m²): 11.8 × 5.0 × 0.95 = 56 kg
Mitre elbows (8× fabricated joints, ~2 kg each): 16 kg
Foam in pipes (V = 25.1 × π/4 × 0.300² × 0.80 × 40): 57 kg
End caps + fittings: 5 kg
Total M1 (hull): ~320 kg
```

**Hydrostatic analysis:**
```
Buoyancy comes from pipe ring only.
Pipe cross-section area: π/4 × 0.315² = 0.0779 m²
Pipe ring total volume: 0.0779 × 25.1 = 1.96 m³
Max buoyancy (fully submerged): 1.96 × 1,025 = 2,009 kg

Displacement: 986 kg → displaced volume = 0.962 m³
Fraction of pipe submerged: 0.962 / 1.96 = 49.1% → pipe ~half submerged

For circular pipe at 49.1% submersion:
  Waterline at pipe center (approximately)
  Draft below pipe center: 157.5 mm
  Hull bottom to waterline: 157.5 mm
  Pipe top above waterline: 157.5 mm
  Deck (on top of pipe): at 315 mm above pipe bottom
  Deck freeboard: 315 - 157.5 = 157.5 mm

  FREEBOARD = 158 mm — SEVERELY INADEQUATE
  (vs 481 mm for Variant A, 281 mm for Variant C)
```

**Cost estimate:**
```
DN315 SDR 41 PE100 pipe: ~$12/m × 25.1 m = $301
HDPE deck sheet (5 mm): ~$200
Mitre-welded elbows (8×, $60 each labor+material): $480
Foam fill (in pipes): $100
End caps + fittings: $80
Assembly labor (12 hrs × $25): $300
Total BOM: ~$1,461 — CHEAPEST OPTION
```

---

## 3. Evaluation Criteria

### 3.1 Criteria Definition

| # | Criterion | Weight | Rationale | Driving Requirement |
|---|-----------|--------|-----------|---------------------|
| C1 | **Unsinkability / damage survival** | 0.20 | Core safety for unattended sea target — must float even after hull breach. This is the defining feature that makes THANH TRI-H deployable without manned standby. | SAF-003 |
| C2 | **Freeboard & green water resistance** | 0.15 | Deck must remain above waves to protect frame, mast sockets, GPS beacon, and mooring hardware. Green water degrades reliability. | OPR-005, D8 Sec 5.1 |
| C3 | **Manufacturing feasibility (VN)** | 0.15 | Vietnamese supply chain maturity, process complexity, QC difficulty. Higher score = simpler to produce locally. | PRD-002 (≥60% local) |
| C4 | **Structural integrity (SS 6 loads)** | 0.10 | Resistance to wave slamming, bending, fatigue over 72 h at SS 6. | OPR-002, FOR-008 |
| C5 | **Mass budget impact** | 0.10 | Lighter hull = more margin for other subsystems within 1,100 kg limit. | GEO-007 |
| C6 | **Unit cost** | 0.10 | Lower hull cost supports $35.6K target. | CST-001 |
| C7 | **Transportability (2-section)** | 0.10 | 2-section splitting for ≤2.5 m road width; ease of splitting and re-joining. | TRA-002 |
| C8 | **Frame/equipment attachment (IF-01)** | 0.10 | Flat, rigid deck surface for M2 frame (84× M12 bolts), mast sockets, mooring pad eye. | IF-01, IF-02, IF-03 |
| | **Total** | **1.00** | | |

### 3.2 Scoring Scale (VDI 2225)

| Score | Meaning |
|-------|---------|
| 0 | Unacceptable — does not satisfy requirement |
| 1 | Barely adequate — just meets minimum, significant risk |
| 2 | Adequate — meets requirement with some concerns |
| 3 | Good — meets requirement well, minor concerns only |
| 4 | Very good — exceeds requirement, no concerns |

---

## 4. Scoring

### 4.1 C1: Unsinkability / Damage Survival (Weight 0.20)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **4** | Foam buoyancy alone provides 2,975 kg — **3.0× the displacement** (986 kg). If hull shell is completely destroyed, foam floats the platform. Verified in D8 Section 5.4: "Platform floats on foam alone even with total hull failure — UNSINKABLE." No failure mode that causes sinking. |
| **B: Compartmented** | **2** | Survives 1–2 compartments flooded (up to 25% loss). At 3–4 compartments flooded (37–50%), platform is marginal with severe heel. At 5+ flooded (>62%), it sinks. Each internal bulkhead weld is a potential single-point failure. In SS 6 wave impacts, multiple compartment breaches are plausible (debris strike, fatigue crack propagating along hull seam). Fundamentally **not unsinkable** — a matter of probability, not certainty. |
| **C: Foam Compact 300** | **3** | Foam buoyancy: 1,783 kg = 2.0× displacement. Still unsinkable, but margin halved vs Variant A. In a worst case (degraded foam + partial waterlogging over service life), reserve drops closer to 1.5×. Acceptable but less robust. |
| **D: Pipe Ring** | **3** | Foam-filled pipes provide segmented unsinkability. If one pipe segment is breached, 12.5% buoyancy lost — floats. Even 2 segments: floats. Pipe walls are thicker (7.7 mm) and pressure-rated, inherently more puncture-resistant than sheet-welded hull. However, 8 mitre-welded joints are vulnerability points. Overall unsinkability good but reliant on joint integrity. |

### 4.2 C2: Freeboard & Green Water Resistance (Weight 0.15)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **4** | Freeboard = 481 mm. Wave edge dip at SS 6 = 154 mm (D8 wave slope × platform radius). Margin: 481 − 154 = **327 mm** above worst-case wave dip. Deck stays dry in SS 5; only occasional spray in SS 6 peak. Self-draining scuppers (8× Ø100 mm) handle green water overtopping. |
| **B: Compartmented** | **4** | Same geometry as A. Lighter → draft ~16 mm → freeboard ~484 mm. Marginally better than A. Same 327+ mm margin. |
| **C: Foam Compact 300** | **2** | Freeboard = 281 mm. Margin: 281 − 154 = **127 mm**. In SS 5 (H_s = 3.5 m), edge dip ~108 mm → margin only 173 mm. In SS 6, green water reaches deck regularly — 20+ overtopping events per hour. Accelerates corrosion of frame, mast sockets, GPS. Mast base sockets fill with seawater despite drain holes. **Fails OPR-005 target (≥300 mm freeboard).** |
| **D: Pipe Ring** | **1** | Freeboard = 158 mm. Margin: 158 − 154 = **4 mm** (effectively zero). Deck is at or below wave surface during most of SS 5–6 exposure. Continuous green water immersion. Equipment permanently awash. Mooring hardware, GPS beacon, all IF-01 bolts permanently submerged. **Completely unacceptable for open ocean target.** |

### 4.3 C3: Manufacturing Feasibility in Vietnam (Weight 0.15)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **3** | Hot-plate welding of HDPE sheet is standard process. 4.0 m half-hulls are large but within capability of Binh Minh Plastics and Tan Dai Hung (confirmed tank/liner fabricators). Ring cross-section requires 3D forming (curved inner and outer walls) — more complex than flat panels but feasible with fixtures. Foam pour-in-place is simple (Dong A Chemical). 3 suppliers identified. |
| **B: Compartmented** | **2** | Same hull fabrication as A (baseline = 3). BUT adds 8 internal bulkheads welded inside the ring cross-section. Internal welding access is constrained: welder must work inside 500 × 500 mm ring void. Bulkhead perimeter weld must be 100% watertight — any leak defeats the concept. Testing requires pressure-testing each compartment individually before assembly (8 separate leak tests). QC burden is significantly higher. Net: manufacturing difficulty + QC complexity downgrades to 2. |
| **C: Foam Compact 300** | **3** | Same process as A but smaller cross-section. Slightly easier to fabricate (less material, smaller panels, lighter sections). Foam fill is simpler (less volume). Same suppliers. Score same as A — marginally easier but not enough to upgrade. |
| **D: Pipe Ring** | **4** | **Strongest manufacturing score.** DN315 PE100 pipe is a mass-produced Vietnamese product — millions of meters produced annually by Binh Minh Plastics, Tien Phong Plastics, Hoa Phat Pipe. Pipe cutting, mitre welding, and electrofusion joining are standard water infrastructure operations. Every Vietnamese pipe fabricator can do this. No custom tooling. No special forming. COTS material + standard techniques = highest feasibility. |

### 4.4 C4: Structural Integrity — SS 6 Loads (Weight 0.10)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **3** | D8 Section 5.2: wave slamming stress = 0.20 MPa vs 22 MPa yield → 0.9% utilization. Foam infill provides distributed support against local buckling — hull wall cannot collapse inward. Ring section modulus is enhanced by foam acting as elastic foundation. Joint (IF-07) at 2.4% bolt utilization. Adequate structural performance with large margins. |
| **B: Compartmented** | **2** | Hull wall geometry identical to A, but **no foam support**. Hollow ring wall under slamming: local plate buckling becomes governing failure mode. HDPE panel 500 × 500 × 8 mm with no backing can flex under 7,850 Pa slamming pressure. Elastic deflection: δ = P×a⁴/(384×E×I) where a = 500 mm unsupported span. With E_HDPE = 900 MPa, I = 42.7 mm⁴/mm width: δ ≈ 2.3 mm — acceptable but visible flexing. Over 40,000 cycles (LC6), HDPE fatigue is not well-characterized for flexural cycling. **Risk of fatigue crack initiation at bulkhead weld toes.** |
| **C: Foam Compact 300** | **3** | Same foam-supported wall as A. Smaller section but slamming pressure unchanged (depends on wave velocity, not hull depth). Wall still at 0.9% utilization. Ring bending stiffness reduced (proportional to depth³), but ring follows wave surface (D/L_p < 0.15) so bending loads are negligible. Score same as A. |
| **D: Pipe Ring** | **2** | Circular pipe cross-section is excellent for hydrostatic pressure (ideal shape). SDR 41 pipe rated for 4 bar (400 kPa) vs slamming 7.8 kPa → trivial. **However**, 8 mitre-welded joints at 22.5° angles create stress concentrations. Under cyclic wave loading, fatigue crack initiation at mitre weld toes is the governing concern. Also, octagonal geometry creates uneven wave loading — 8 flat faces hit waves at different angles, creating differential loads between adjacent segments. HDPE deck sheet welded to round pipe surface is a weak connection under in-plane shear (mast socket forces, mooring pull). |

### 4.5 C5: Mass Budget Impact (Weight 0.10)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **3** | M1 = 350 kg. Margin to 1,100 kg: 114 kg (10.4%). Adequate but hull is the largest single subsystem. |
| **B: Compartmented** | **4** | M1 = 269 kg. **Saves 81 kg** vs A. Margin to 1,100 kg: 195 kg (17.7%). Best mass performance. Extra margin could absorb growth in other subsystems (e.g., heavier mooring for deeper water). |
| **C: Foam Compact 300** | **4** | M1 = 225 kg. **Saves 125 kg** vs A. Margin to 1,100 kg: 239 kg (21.7%). Lightest option. |
| **D: Pipe Ring** | **3** | M1 = 320 kg. Saves 30 kg vs A. Moderate improvement. Pipe wall thickness (7.7 mm minimum for SDR 41) constrains further lightening. |

### 4.6 C6: Unit Cost (Weight 0.10)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **3** | $4,118 BOM (C14). Baseline cost. Foam adds $800 but provides critical unsinkability. |
| **B: Compartmented** | **3** | ~$3,400. Saves $718 (−17%). Foam savings ($800) partially offset by bulkhead fabrication ($280 material + labor). Net savings modest. |
| **C: Foam Compact 300** | **4** | ~$2,850. Saves $1,268 (−31%). Less HDPE material (−35%) and less foam (−40%). Cheapest foam-filled option. |
| **D: Pipe Ring** | **4** | ~$1,461. Saves $2,657 (−65%). **By far cheapest** due to COTS pipe pricing. No custom forming, no complex welding fixtures. |

### 4.7 C7: Transportability (Weight 0.10)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **4** | 2-section bolted (E10: 85.0%). Each half: ~4.0 × 4.0 × 0.5 m. Fits standard 40-ft flatbed. 175 kg per half (manageable). Field-joinable in ~2 hours. |
| **B: Compartmented** | **4** | Same 2-section geometry as A. Slightly lighter (135 kg per half). Joint at diameter coincides with 2 bulkhead positions — structural continuity maintained. |
| **C: Foam Compact 300** | **4** | Same 2-section split. Each half: 4.0 × 4.0 × **0.3 m** — thinner profile, easier to stack on transport. Only 113 kg per half. Slightly easier transport than A. |
| **D: Pipe Ring** | **3** | Can split octagon into 2 halves (4 segments each), each ~4.0 m wide. But re-joining requires HDPE mitre welding at 4 joint points — more complex than bolted flange. Alternatively, transport as 8 individual pipe segments + deck panels for on-site assembly — but assembly time increases to ~8 hours. No simple bolt-and-gasket joint like A/B/C. |

### 4.8 C8: Frame / Equipment Attachment (Weight 0.10)

| Variant | Score | Justification |
|---------|-------|---------------|
| **A: Foam Ring 500** | **4** | Flat HDPE deck provides continuous surface for frame attachment (IF-01: 84× M12 at 300 mm spacing). Fender washers distribute load on HDPE. Foam backing supports hull wall against bolt pull-through. Mast sockets bolt through deck and frame simultaneously. Mooring pad eye loads transfer through frame to hull. Proven, simple, robust attachment. |
| **B: Compartmented** | **3** | Same flat deck as A. But **no foam backing** behind hull wall at bolt locations — bolts compress unsupported HDPE wall. Higher creep risk than A (no elastic foundation). Fender washers alone must distribute all load. Internal bulkheads provide some stiffening at 8 discrete locations but not continuous support. |
| **C: Foam Compact 300** | **3** | Flat deck present. Foam backing present. But **300 mm depth reduces vertical contact area** between frame and hull. Frame perimeter ring sits on narrower hull deck edge. Less through-bolt engagement length available. Reduced bolt pull-through resistance for hull-to-frame connection. IF-07 joint flange is also shorter (300 vs 500 mm), reducing joint clamping area. |
| **D: Pipe Ring** | **1** | **Critical weakness.** Deck sheet is welded to the curved top of DN315 pipes — not a rigid flat surface. Under mast socket loads (142 N lateral wind + 15 kg vertical per mast), the deck sheet deflects between pipes. Frame perimeter ring cannot bolt to a round pipe surface without custom saddle clamps. Mooring pad eye (14,832 N peak) would require a dedicated load-spreading subframe welded to multiple pipe segments. Entire IF-01 architecture must be redesigned. This is not a minor adaptation — it is a fundamental incompatibility with the A7 architecture. |

---

## 5. Weighted Score Calculation

### 5.1 Score Matrix

| Criterion | Weight | A: Foam Ring 500 | B: Compartmented | C: Compact 300 | D: Pipe Ring |
|-----------|--------|:-:|:-:|:-:|:-:|
| C1: Unsinkability | 0.20 | 4 | 2 | 3 | 3 |
| C2: Freeboard | 0.15 | 4 | 4 | 2 | 1 |
| C3: Mfg feasibility | 0.15 | 3 | 2 | 3 | 4 |
| C4: Structural integrity | 0.10 | 3 | 2 | 3 | 2 |
| C5: Mass | 0.10 | 3 | 4 | 4 | 3 |
| C6: Cost | 0.10 | 3 | 3 | 4 | 4 |
| C7: Transport | 0.10 | 4 | 4 | 4 | 3 |
| C8: Frame attachment | 0.10 | 4 | 3 | 3 | 1 |

### 5.2 Weighted Scores

| Criterion | Wt | A: w×s | B: w×s | C: w×s | D: w×s |
|-----------|-----|--------|--------|--------|--------|
| C1 | 0.20 | 0.80 | 0.40 | 0.60 | 0.60 |
| C2 | 0.15 | 0.60 | 0.60 | 0.30 | 0.15 |
| C3 | 0.15 | 0.45 | 0.30 | 0.45 | 0.60 |
| C4 | 0.10 | 0.30 | 0.20 | 0.30 | 0.20 |
| C5 | 0.10 | 0.30 | 0.40 | 0.40 | 0.30 |
| C6 | 0.10 | 0.30 | 0.30 | 0.40 | 0.40 |
| C7 | 0.10 | 0.40 | 0.40 | 0.40 | 0.30 |
| C8 | 0.10 | 0.40 | 0.30 | 0.30 | 0.10 |
| **Σ** | **1.00** | **3.55** | **2.90** | **3.15** | **2.65** |
| **Score (%)** | | **88.8%** | **72.5%** | **78.8%** | **66.3%** |

### 5.3 Ranking

| Rank | Variant | Score | Verdict |
|------|---------|-------|---------|
| **1** | **A: Foam-Filled Ring 500 mm** | **88.8%** | **SELECTED — confirms baseline** |
| 2 | C: Foam-Filled Compact 300 mm | 78.8% | Viable but freeboard deficiency is disqualifying |
| 3 | B: Compartmented Ring 500 mm | 72.5% | Viable but sacrifices core unsinkability feature |
| 4 | D: COTS Pipe Ring | 66.3% | Cheapest but freeboard + frame attachment fatal flaws |

---

## 6. Sensitivity Analysis

### 6.1 What If Unsinkability Weight is Reduced?

If the customer accepts "survivable" (≤2 compartments flooded) instead of "unsinkable" (total hull loss), C1 weight drops from 0.20 to 0.10:

| Variant | Original Score | C1 = 0.10 (Mfg +0.10) | C1 = 0.10 (Cost +0.10) |
|---------|---------------|------------------------|------------------------|
| A | 88.8% | 86.3% | 83.8% |
| B | 72.5% | 75.0% | 75.0% |
| C | 78.8% | 78.8% | 81.3% |
| D | 66.3% | 70.0% | 72.5% |

**Result:** Variant A remains first in all sensitivity scenarios. Variant C approaches A only if both unsinkability AND freeboard are deprioritized — but deprioritizing freeboard for an open-ocean target is unjustifiable.

### 6.2 What If Pipe Diameter Increased to DN500?

Larger pipe would improve freeboard:
```
DN500 SDR 41 PE100: OD = 500 mm, wall = 12.2 mm, weight = 18.7 kg/m
Pipe ring mass: 18.7 × 25.1 = 469 kg (pipe alone)
+ deck + foam + elbows: ~560 kg total hull
System mass: 560 + 636 (non-hull) = 1,196 kg → EXCEEDS 1,100 kg LIMIT

DISQUALIFIED — cannot meet GEO-007 mass constraint.
```

DN400 SDR 41: OD = 400 mm, wall = 9.8 mm, weight = 11.9 kg/m
```
Pipe ring: 11.9 × 25.1 = 299 kg
+ deck + foam + elbows: ~400 kg total
System: 400 + 636 = 1,036 kg → within limit (64 kg margin, tight)
Freeboard: pipe half-submerged → ~200 mm deck freeboard
Still inadequate (200 mm < 300 mm target)
```

**Conclusion:** No practical PE100 pipe diameter simultaneously meets mass AND freeboard requirements for the 8.0 m platform. The pipe ring concept is fundamentally limited by circular cross-section efficiency.

### 6.3 Break-Even: How Much Depth Can Be Removed from Variant A?

```
Minimum freeboard target: 300 mm
Draft: ~19 mm (insensitive to hull depth, depends on waterplane area)
Minimum hull depth: 300 + 19 = 319 mm → round to 350 mm

At 350 mm depth:
  Hull shell: ~160 kg (−30%)
  Foam: ~85 kg (−30%)
  Total M1: ~274 kg (saves 76 kg vs baseline)
  Cost: ~$3,300 (saves $818)
  Freeboard: 350 − 19 = 331 mm → meets 300 mm target
  Foam buoyancy: 2,083 kg >> 986 kg → UNSINKABLE (2.1× ratio)

This represents the compact limit of Variant A.
Could be pursued as Phase 4 optimization (O13 continuation).
```

---

## 7. Decision

### 7.1 Selected: Variant A — Foam-Filled Ring Pontoon, 500 mm Depth (88.8%)

**Justification:**

The foam-filled ring pontoon at 500 mm depth is the clear winner across all criteria combinations. Its defining advantage is the **3.0× unsinkability margin** — the platform cannot sink under any hull damage scenario, including total shell failure. For an unattended expendable sea target deployed 72 h before a missile test in SS 5–6, this margin is the difference between a successful test and a lost target (with associated $1–5M test delay).

**Why alternatives fall short:**

| Variant | Fatal Weakness | Engineering Basis |
|---------|---------------|-------------------|
| B: Compartmented | Not unsinkable — ≥5 compartments flooded = sinks | Bulkhead weld quality is single-point failure; difficult to inspect internally; 72 h SS 6 exposure creates plausible multi-compartment breach scenario |
| C: Compact 300 mm | Freeboard 281 mm < 300 mm target | Wave edge dip at SS 6 = 154 mm; only 127 mm margin vs 327 mm for baseline; green water regularly reaches deck, accelerating corrosion and reducing reliability |
| D: COTS Pipe Ring | Freeboard 158 mm (inadequate) + frame attachment incompatible | Circular pipe cross-section is geometrically inefficient for pontoon application; cannot achieve adequate freeboard within 1,100 kg mass limit; IF-01 architecture requires complete redesign |

### 7.2 Optimization Opportunity Identified

The sensitivity analysis (Section 6.3) shows that **reducing hull depth from 500 to 350 mm** would save 76 kg and $818 while maintaining ≥300 mm freeboard and 2.1× unsinkability. This can be evaluated as a Phase 4 detail design optimization if mass/cost savings are needed.

### 7.3 Impact on Prototype Plan

This evaluation **confirms** the hull prototype plan ([[PROTO_hull_platform_validation.md]]) should proceed with the 500 mm depth foam-filled ring as specified. No design change required.

---

## 8. Summary Table

| Parameter | A: Foam Ring 500 | B: Compartmented | C: Compact 300 | D: Pipe Ring |
|-----------|:-:|:-:|:-:|:-:|
| **VDI 2225 Score** | **88.8%** | 72.5% | 78.8% | 66.3% |
| Hull mass (kg) | 350 | 269 | 225 | 320 |
| Hull cost ($) | 4,118 | 3,400 | 2,850 | 1,461 |
| Freeboard (mm) | **481** | 484 | 281 | 158 |
| Unsinkable? | **YES (3.0×)** | NO | YES (2.0×) | YES (segmented) |
| Mfg complexity | Medium | High (internal welds) | Medium | Low (COTS pipe) |
| Frame attachment | **Excellent** | Good | Adequate | **Incompatible** |
| **Verdict** | **SELECTED** | Reserve | Rejected (freeboard) | Rejected (freeboard + IF-01) |

---

## 9. Cross-References

- [[DECS_E10_variant_evaluation.md]] — E10 Decision 1: Hull **fabrication method** (2-section bolted at 85.0%)
- [[PRAD_D8_design_structure.md]] — Hydrostatic stability (Sec 5.1), wave slamming (Sec 5.2), joint analysis (Sec 5.3), reserve buoyancy (Sec 5.4)
- [[DECS_D9_detail_specification.md]] — Hull specifications (Sec 2.1–2.3)
- [[OCP_C14_cost_analysis.md]] — M1 hull BOM ($4,118)
- [[OCP_O13_design_optimization.md]] — Weight optimization W-1 (foam density)
- [[OCP_P15_production_planning.md]] — Hull manufacturing (Sec 1.2), suppliers (Sec 2.1)
- [[PROTO_hull_platform_validation.md]] — Hull prototype plan ($9.2K, 10 weeks)

---

*End of Hull Structural Concept Evaluation. Variant A "Foam-Filled Ring Pontoon, 500 mm Depth" confirmed at 88.8% VDI 2225 score. No design change from Phase 3 baseline. Hull depth reduction to 350 mm identified as Phase 4 optimization opportunity (−76 kg, −$818, freeboard 331 mm).*
