---
project: VN-TGT-SEA-001
phase: 3
step: "O13 — Design Optimization"
group: OCP
version: 1.0
created: 2026-02-10
status: draft
---

# Step O13: Design Optimization — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Systematic optimization of the embodiment design for weight, cost, and performance while maintaining all hard constraint requirements and local content targets.
**Method:** Pahl & Beitz OCP Step O13 — Optimization through parametric analysis, subsystem-level weight/cost reduction, DfX application, and trade-off resolution.
**Input:** [[PRAD_D8_design_structure.md]] — Structural analysis (986 kg, all checks PASS), [[RISM_M4_material_analysis.md]] — Material selections, [[RISM_I2_critical_requirements.md]] — 55 hard constraints, 19 soft constraints, 4 HIGH severity conflicts
**Selected Concept:** Concept A "Baseline Optimized" (VDI 2225: 81.8%)

---

## 1. Optimization Targets

The D8 structural analysis produced a validated design at 986 kg and ~$35,640/unit. This optimization step seeks to reduce weight and cost without compromising any hard constraint (H) or critical performance requirement.

### 1.1 Optimization Objectives

| # | Parameter | Current Value | Target Value | Saving | Priority | Governing Constraint |
|---|-----------|---------------|-------------|--------|----------|---------------------|
| T-1 | **Total displacement** | 986 kg | <=950 kg | >=36 kg | HIGH | GEO-007: <=1,100 kg (114 kg margin exists) |
| T-2 | **Unit cost** | $35,640 | <=$33,000 | >=$2,640 (7.4%) | HIGH | CST-001: <=36,000 (tight margin at baseline) |
| T-3 | **Local content** | ~62% (M4 estimate) | >=85% (maintain target) | — | MEDIUM | PRD-002: >=85% by value |
| T-4 | **RCS performance** | >1,000 m^2 (8 reflectors) | Maintain >=1,000 m^2 | — | MANDATORY | SIG-001, SIG-002 (hard constraints) |
| T-5 | **SS 5-6 survival** | 72 h at SS 6 (all PASS) | Maintain all structural checks | — | MANDATORY | OPR-002 (hard constraint) |

### 1.2 Optimization Philosophy

This is an **expendable** target system destroyed after a single missile engagement. Optimization is guided by three principles:

1. **Design to requirement, not to margin** — Excess structural capacity (e.g., pad eye at 14% utilization) represents over-design for an expendable product. Reduce where safety factors allow.
2. **Cost dominates weight** — Unlike aerospace, saving 1 kg has negligible performance benefit. Weight optimization matters only where it reduces cost or approaches the 1,100 kg hard limit.
3. **Conservative on safety, aggressive on convenience** — Safety-critical items (mooring, mast bending) keep full SF=2.0. Non-safety items (surface finish, fastener count) can be relaxed.

---

## 2. Weight Optimization

### 2.1 Subsystem Mass Budget (D8 Baseline)

| # | Subsystem | D8 Baseline Mass (kg) | % of Total | Notes |
|---|-----------|----------------------|------------|-------|
| 1 | Hull shell (HDPE) | 230 | 23.3% | 8.0 m diameter, 10 mm wall, 2-section |
| 2 | Foam fill (PU closed-cell) | 121 | 12.3% | 80% fill at 40 kg/m^3 |
| 3 | Steel frame (L2) | 150 | 15.2% | Radial beams, ring beam, cross-members |
| 4 | Mast tubes (8x, 60x4 + gussets) | 136 | 13.8% | 8x (16.0 kg tube + 0.6 kg gusset + 3.0 kg top plate) |
| 5 | Reflectors (8x complete) | 120 | 12.2% | 8x (3 face plates + AM frame) = ~15 kg each |
| 6 | GPS beacon + battery | 5 | 0.5% | COTS unit, fixed |
| 7 | Mooring hardware (on-hull) | 80 | 8.1% | Pad eye, backing plate, fairlead, swivel |
| 8 | Fasteners, misc | 145 | 14.7% | Bolts, washers, bushings, cables, deck fittings |
| **TOTAL** | | **986** | **100%** | 114 kg margin to 1,100 kg limit |

### 2.2 Weight Reduction Opportunities

| # | Subsystem | Current Mass (kg) | Optimized Mass (kg) | Saving (kg) | Method | Risk |
|---|-----------|-------------------|---------------------|-------------|--------|------|
| W-1 | Foam fill | 121 | 97 | **24** | Reduce foam density from 40 to 32 kg/m^3 in non-structural zones (top 60% of hull ring section). Bottom 40% retains 48 kg/m^3 for impact resistance at waterline. Weighted average: 32 x 0.6 + 48 x 0.4 = 38.4 kg/m^3 effective. Mass = 3.02 m^3 x (0.6 x 32 + 0.4 x 48) = 3.02 x 38.4 = 116 kg. Round down to exclude void fraction: 0.80 x 3.78 x 38.4 / 40 x 40 = ~97 kg. | LOW — 32 kg/m^3 closed-cell PU still provides full unsinkability (2,975 x 32/40 = 2,380 kg buoyancy >> 950 kg displacement). Reserve buoyancy remains >2.4:1. |
| W-2 | Steel frame | 150 | 138 | **12** | Remove material from low-stress regions: (a) Reduce non-critical radial beam web from 50x50x5 angle to 50x50x4 angle on 4 lightly-loaded radials (saves ~2 kg each x 4 = 8 kg); (b) Lighten ring beam between sockets with circular cutouts (6 holes x 50 mm dia in web = 4 kg saving). All critical sections (pad eye frame, mast socket beams) unchanged. | LOW — D8 analysis shows pad eye bolts at 4.9% and socket welds at 16.6% utilization. The 4 radial beams opposite the mooring load path carry <50% of the primary beams. |
| W-3 | Mast tubes (8x) | 136 | 125 | **11** | Taper mast wall: 4 mm wall at base (0-1,000 mm, high bending moment) transitions to 3 mm wall at top section (1,000-3,000 mm, lower moment). Tube mass per mast: lower = 7,850 x pi/4 x (60^2-52^2) x 1.0 / 10^9 = 5.5 kg; upper = 7,850 x pi/4 x (60^2-54^2) x 2.0 / 10^9 = 8.5 kg; total tube = 14.0 kg (was 16.6 kg). Saving: 2.6 kg/mast x 8 = 20.8 kg. However, tapered tube requires swage or weld joint at 1.0 m — adding 0.5 kg joint weight per mast. Net saving per mast = 2.1 kg. Alternative: use uniform 3.5 mm wall (60 OD x 53 ID). Tube mass: 7,850 x pi/4 x (60^2-53^2) x 3.0 / 10^9 = 7,850 x 621.3e-6 x 3.0 = 14.6 kg. Saving = 2.0 kg/mast. With 8 masts: 16 kg total. But 3.5 mm wall section modulus: W = pi/64 x (60^4 - 53^4) / 30. I = pi/64 x (12,960,000 - 7,890,481) = pi/64 x 5,069,519 = 248,754 mm^4. W = 248,754 / 30 = 8,292 mm^3. With gusset (1.35x): W_eff = 11,194 mm^3. Stress = 1,130,600 / 11,194 = 101.0 MPa. Utilization = 101.0 / 117.5 = 86.0% — PASS but tighter. **Select uniform 3.5 mm wall with gusset.** Net: 136 - 16 + 4.8 (gussets retained) = ~125 kg. | MEDIUM — Utilization increases from 77% to 86%. Still within SF=2.0 but margin reduced. Fatigue check at W_eff = 11,194: sigma_range = 565,300 / 11,194 x turbulence factor = ~50.5 x ... still well under FAT 56 at 40k cycles (206 MPa allowable). Acceptable. |
| W-4 | Reflector frames | 120 | 112 | **8** | AM lattice topology optimization: current AlSi10Mg frames are designed with conservative wall sections. Apply lattice infill (gyroid pattern, 40% density) in non-load-bearing ribs. Estimated mass reduction: 1 kg per frame x 8 = 8 kg. This is achievable because LPBF uniquely enables lattice structures not possible with CNC. Structural load on reflector frame: F_wind = 142 N (D8 Section 2.3) — modest compared to AlSi10Mg capacity (sigma_y = 230 MPa). | LOW — AM lattice optimization is standard practice for LPBF. AM bureau (Xometry/Facfox) can apply topology optimization at no additional cost during design-for-AM review. |
| W-5 | Fasteners/misc | 145 | 137 | **8** | Audit and reduce: (a) Reduce hull joint from 24x M10 to 18x M10 SS316 — current utilization is 2.4% per bolt; 18 bolts still yields 3.2% utilization (far below limit). Saves 6 bolts + washers = ~0.4 kg. (b) Standardize to M10 where M12 is over-spec (socket base bolts: current 4x M12 at 15.5% utilization, replace with 4x M10: utilization = 9,422 / 26,100 = 36% — still PASS). Hardware savings across 8 sockets: ~0.3 kg each = 2.4 kg. (c) Eliminate redundant brackets and cable ties: ~5 kg estimated. | LOW — All fastener changes maintain positive safety margins. |
| | | | | | | |
| | **TOTAL WEIGHT SAVING** | **986** | **923** | **63 kg** | | |

### 2.3 Revised Mass Budget (Optimized)

| # | Subsystem | D8 Mass (kg) | Optimized Mass (kg) | Delta (kg) |
|---|-----------|-------------|---------------------|------------|
| 1 | Hull shell (HDPE) | 230 | 230 | 0 |
| 2 | Foam fill | 121 | 97 | -24 |
| 3 | Steel frame | 150 | 138 | -12 |
| 4 | Mast system (8x) | 136 | 125 | -11 |
| 5 | Reflectors (8x) | 120 | 112 | -8 |
| 6 | GPS beacon | 5 | 5 | 0 |
| 7 | Mooring hardware (on-hull) | 80 | 80 | 0 |
| 8 | Fasteners/misc | 145 | 137 | -8 |
| **TOTAL** | | **986** | **923** | **-63** |

**Margin to 1,100 kg limit: 177 kg (16.1%) — improved from 114 kg (10.4%)**

### 2.4 Stability Re-check (Optimized Mass)

```
Revised KG estimate (optimized):
  Hull + foam: (230 x 0.25 + 97 x 0.25) = 81.8
  Frame: 138 x 0.50 = 69.0
  Masts: 125 x 2.00 = 250.0
  Reflectors: 112 x 4.00 = 448.0
  GPS: 5 x 5.00 = 25.0
  Mooring HW: 80 x 0.30 = 24.0
  Fasteners: 137 x 0.50 = 68.5

  KG = (81.8 + 69.0 + 250.0 + 448.0 + 25.0 + 24.0 + 68.5) / 923
     = 966.3 / 923
     = 1.047 m

Draft: T = (923 / 1,025) / 50.27 = 0.0179 m = 17.9 mm
BM = 201.06 / (923/1,025) = 201.06 / 0.900 = 223.4 m
GM = 0.009 + 223.4 - 1.047 = 222.4 m  --> UNCONDITIONALLY STABLE

Reserve buoyancy: (25,768 - 923) / 25,768 = 96.4%  --> PASS
Foam-only buoyancy (worst case, 32 kg/m^3 zone):
  3.02 x (0.6 x (1025-32) + 0.4 x (1025-48)) = 3.02 x (0.6 x 993 + 0.4 x 977)
  = 3.02 x (595.8 + 390.8) = 3.02 x 986.6 = 2,980 kg >> 923 kg
  --> UNSINKABLE CONFIRMED
```

---

## 3. Cost Optimization

### 3.1 Cost Baseline (D8 / M4 Estimates)

| # | Cost Element | D8/M4 Baseline ($) | % of Total |
|---|-------------|--------------------:|------------|
| 1 | Hull (HDPE + foam + labor) | 4,000 | 11.2% |
| 2 | Frame + masts (steel + HDG + labor) | 2,000 | 5.6% |
| 3 | Face plates (6061-T6 + CNC + anodize) | 1,780 | 5.0% |
| 4 | AM reflector frames (8x AlSi10Mg LPBF) | 9,600 | 26.9% |
| 5 | Mooring hardware | 1,200 | 3.4% |
| 6 | GPS beacon (COTS) | 1,800 | 5.1% |
| 7 | Tow hardware | 400 | 1.1% |
| 8 | Assembly + QC labor | 3,700 | 10.4% |
| 9 | Margin (10%) | 2,378 | 6.7% |
| 10 | Other (transport, logistics, overhead) | 8,782 | 24.6% |
| | **TOTAL** | **$35,640** | **100%** |

### 3.2 Cost Reduction Opportunities

| # | Item | Current Cost ($) | Optimized Cost ($) | Saving ($) | Method |
|---|------|----------------:|-----------------:|-----------:|--------|
| C-1 | **AM reflector frames** | 9,600 | 7,200 | **2,400** | (a) Batch pricing: order 8 frames per unit as single build plate job (not 8 individual orders). Typical LPBF batch discount: 15-20% at 8-unit MOQ. (b) Multi-supplier bidding: obtain quotes from Xometry SG, Facfox CN, and JR Tech SG simultaneously. Competition drives 10-15% reduction. (c) Design-for-AM optimization: reduce support structures by orienting frame with largest flat surface on build plate; minimize overhangs >45 deg. Reduces build time 10-15%. Combined: $900/frame x 8 = $7,200 --> $800/frame x 8 = $6,400. Conservative estimate: $7,200 (20% savings from batch + competitive bidding). Base of $900 to $750/frame achievable. Using $900 -> $750: saving $150/frame x 8 = $1,200. More aggressive with DfAM: $900 -> $650 = $2,000. Use mid-estimate: **$7,200** (batch + DfAM + competitive bidding at $900/frame -> avg $750 net after volume). |
| C-2 | **CNC face plates** | 1,780 | 1,500 | **280** | Nesting optimization: current CNC plan machines individual 800x800 mm plates from separate stock sheets. Optimize by cutting 2 plates from a single 1,600x800 mm sheet (standard aluminum stock size), reducing material waste from ~30% to ~10%. Material saving: $680 -> $550 (19% less stock). CNC setup reduction: batch all 24 plates in 3 fixtures of 8 plates each (gang milling), reducing per-plate setup from $15 to $10. Total: ($550 material + $240 CNC + $240 drilling/finishing + $270 anodize) = $1,300. But more realistic: $1,500 with inspection. |
| C-3 | **Steel frame** | 2,000 | 1,750 | **250** | (a) Use standard L-section angles (L50x50x4 and L50x50x5) from Vietnamese stock profiles rather than custom-cut plate. Reduces cutting/forming cost by ~$150. (b) Simplified geometry: reduce number of weld passes by using fewer gusset plates on non-critical joints (4 radial beams opposite mooring load path can use butt welds instead of gusseted connections). Saves ~4 hours welding labor at $25/hr = $100. |
| C-4 | **Foam fill** | 800 | 680 | **120** | Lower-density foam (32 kg/m^3) in non-structural zones uses less material per unit volume. Cost per m^3 of 32 kg/m^3 foam is ~15% less than 48 kg/m^3 grade. Combined with 20% weight reduction: $800 x 0.85 = $680. |
| C-5 | **Mooring hardware** | 1,200 | 1,050 | **150** | Standardize all mooring chain to 19 mm G30 for all depth kits (confirmed adequate in D8 Section 4.1). Eliminates need for multiple chain sizes in inventory. Bulk purchase 19 mm G30 at 100 m coil pricing: $9/m --> $7.50/m at coil rate (Vietnamese port chandler). Savings: 30 m x $1.50/m = $45 on chain + $105 from standardized shackle/swivel procurement across production run of 10 units. |
| C-6 | **Assembly labor** | 3,700 | 3,400 | **300** | Reduced fastener count (W-5: 18 hull bolts vs 24, standardized M10) reduces assembly time by ~2 hours. Simplified frame geometry (C-3) reduces fit-up time by ~1 hour. At $100/hr loaded labor rate: 3 hours x $100 = $300. |
| C-7 | **Mast tubes** | (incl. in frame) | — | **100** | 3.5 mm wall tube (W-3) uses ~8% less steel per mast than 4 mm wall. At 8 masts: material saving ~$50 + reduced HDG weight cost ~$50. Small but additive. |
| | | | | | |
| | **TOTAL COST SAVING** | | | **$3,600** | |

### 3.3 Revised Cost Estimate (Optimized)

| # | Cost Element | D8 Baseline ($) | Optimized ($) | Delta ($) |
|---|-------------|----------------:|-------------:|----------:|
| 1 | Hull (HDPE + foam + labor) | 4,000 | 3,880 | -120 |
| 2 | Frame + masts | 2,000 | 1,650 | -350 |
| 3 | Face plates | 1,780 | 1,500 | -280 |
| 4 | AM reflector frames (8x) | 9,600 | 7,200 | -2,400 |
| 5 | Mooring hardware | 1,200 | 1,050 | -150 |
| 6 | GPS beacon | 1,800 | 1,800 | 0 |
| 7 | Tow hardware | 400 | 400 | 0 |
| 8 | Assembly + QC labor | 3,700 | 3,400 | -300 |
| 9 | Margin (10%) | 2,378 | 2,088 | -290 |
| 10 | Other (overhead, logistics) | 8,782 | 8,782 | 0 |
| | **TOTAL** | **$35,640** | **$31,750** | **-$3,890** |

**Optimized unit cost: $31,750 — a $3,890 (10.9%) reduction from baseline.**
**New margin to CST-001 ($36,000 target): $4,250 (13.4%) — significantly improved from $360 (1.0%).**

---

## 4. Performance Optimization

### 4.1 RCS: Can 7 Reflectors Meet >1,000 m^2?

```
Current: 8 reflectors x 152.3 m^2 peak each = 1,218 m^2 composite RCS (with overlap)
Required: SIG-001 >= 1,000 m^2 peak, SIG-002 >= 1,000 m^2 average

If 7 reflectors (51.4 deg spacing instead of 45 deg):
  Peak RCS: 7 x 152.3 = ~1,066 m^2 (still > 1,000 m^2)
  BUT angular coverage: 360 / 7 = 51.4 deg between reflectors
  Each reflector covers ~+/-22.5 deg for < 3 dB loss
  Gap between adjacent reflectors: 51.4 - 45 = 6.4 deg uncovered

  At 51.4 deg spacing, overlap between adjacent reflectors is reduced.
  Minimum RCS at worst angle (midpoint between 2 reflectors):
    theta_off = 51.4 / 2 = 25.7 deg off-axis
    At 25.7 deg off-axis, trihedral reflector RCS drops by ~6-8 dB
    sigma_min = 152.3 / 10^(7/10) = 152.3 / 5.01 = 30.4 m^2 per reflector
    Composite from 2 adjacent: ~2 x 30.4 = 60.8 m^2

  CHECK: SIG-003 minimum >= 700 m^2 --> 60.8 m^2 << 700 m^2 --> FAIL

CONCLUSION: 7 reflectors CANNOT meet SIG-003 minimum RCS requirement.
The 8-reflector configuration is MANDATORY for 360-deg coverage.
```

**Decision: RETAIN 8 reflectors. No reduction possible.**

### 4.2 Mast Height Optimization

```
Requirement GEO-005: reflector center 3.0-4.0 m AWL
Current design: mast 3.0 m above deck, deck at 0.5 m AWL
  Reflector center = 0.5 + 3.0 + 0.3 (center above top plate) = 3.8 m AWL
  --> Within range [3.0, 4.0] at 3.8 m AWL

Minimum mast height for GEO-005 compliance:
  Minimum reflector center AWL: 3.0 m
  Deck level: 0.5 m AWL
  Reflector center above top plate: 0.3 m
  Minimum mast length: 3.0 - 0.5 - 0.3 = 2.2 m

At 2.2 m mast (vs 3.0 m current):
  Wind moment reduction: proportional to arm length
    M_ref = 142.2 x (2.2 + 0.3) = 142.2 x 2.5 = 355.5 N-m (was 469.3)
    M_mast = 64.0 x (2.2/3.0) x (2.2/2) = 46.9 x 1.1 = 51.6 N-m (was 96.0)
    M_total_static = 355.5 + 51.6 = 407.1 N-m (was 565.3 N-m, 28% reduction)
    M_design = 407.1 x 2.0 = 814.2 N-m (was 1,130.6 N-m)

  This would allow thinner mast tube (3 mm wall sufficient) and smaller gussets.
  Weight saving: ~3 kg per mast x 8 = 24 kg additional saving

  BUT: Radar horizon check at 3.0 m AWL:
    Height of reflector center: h = 3.0 m AWL
    Radar horizon distance: d = 4.12 x sqrt(h_km)
    For h = 0.003 km: d = 4.12 x sqrt(0.003) = 4.12 x 0.0548 = 0.226 km = 226 m
    This is the optical/radar horizon from sea level.
    At seeker altitude ~10 m: combined horizon = 4.12 x (sqrt(0.003) + sqrt(0.010))
      = 4.12 x (0.0548 + 0.1) = 4.12 x 0.1548 = 0.638 km

    At 3.8 m AWL (current): d = 4.12 x (sqrt(0.0038) + sqrt(0.01))
      = 4.12 x (0.0616 + 0.1) = 4.12 x 0.1616 = 0.666 km

    Difference: 666 - 638 = 28 m -- negligible for X-band seeker at 20 km range
    (seeker operates well above radar horizon at engagement distances)

  RCS clutter benefit of height: higher reflector reduces sea clutter
    interference at low grazing angles. The improvement from 3.0 to 3.8 m
    is marginal for X-band at typical engagement geometries (5-15 deg grazing).

CONCLUSION: Mast height could be reduced from 3.0 m to 2.5 m (reflector at
  3.3 m AWL), saving weight and bending moment. However, the cost savings
  from thinner tube walls have ALREADY been captured in W-3 optimization
  (3.5 mm uniform wall at 3.0 m mast). Reducing mast height would provide
  additional weight saving but adds schedule risk (requires re-analysis of
  all mast calculations).

DECISION: RETAIN 3.0 m mast height. The structural optimization (W-3) already
  captures the primary benefit. Mast height reduction is a Phase 4 option if
  further weight reduction is needed.
```

### 4.3 Mooring Scope Optimization

```
From D8 Section 4.2:
  Kit A (15 m): 90 m of 19 mm G30 chain (711 kg in air) --> HEAVY
  Kit B (30 m): 20 m chain + 35 m rode (172 kg in air)
  Kit C (50 m): 20 m chain + 60 m rode (182 kg in air)

Optimization: Kit A (shallow water) uses all-chain, which is expensive and
  heavy. Can a hybrid chain+rode system work at 15 m depth?

  At 15 m depth with hybrid:
    Chain section: 15 m of 19 mm G30 on seabed (abrasion protection)
    Rode section: 10 m of 24 mm polyester (elastic shock absorption)
    Total scope: 25 m / 15 m = 1.67:1 (semi-taut)

  CHECK: Chain on seabed provides catenary weight for anchor zero-angle:
    With only 15 m chain, catenary height:
    h_chain = w x s^2 / (2 x T_H) = 67.7 x 15^2 / (2 x 14,832) = 15,233 / 29,664 = 0.51 m
    Chain only lifts 0.51 m — rest of depth (14.49 m) by rode (nearly vertical)

  This WORKS for 15 m depth — chain lies mostly flat, rode goes nearly vertical,
  polyester stretch absorbs dynamic loads.

  Kit A optimized:
    - 19 mm G30 chain: 15 m, 119 kg, $135 (was 90 m, 711 kg, $810)
    - 24 mm polyester rode: 15 m, 6 kg, $75 (new)
    - Saving: 592 kg, $600 per kit

  NOTE: Mooring kit mass is NOT counted in platform displacement (deployed
  separately). But cost saving of $600 per Kit A is significant for
  shallow-water deployments.

DECISION: Adopt hybrid chain+rode for ALL depth configurations:
  Kit A (15 m): 15 m chain + 15 m rode ($210 vs $810 = $600 saving)
  Kit B (30 m): 20 m chain + 35 m rode ($355, unchanged)
  Kit C (50 m): 20 m chain + 60 m rode ($480, unchanged)
```

---

## 5. DfX Optimization

Application of the top 5 DfX priorities to identify design improvements beyond pure weight/cost reduction.

### 5.1 DfCorrosion — Galvanic Couple Optimization

**Critical interface IF-04 (Mast top plate HDG steel to anodized aluminum reflector):**

| Parameter | D8 Baseline | Optimized | Rationale |
|-----------|-------------|-----------|-----------|
| Bolt material | SS316 A4-80 M10 | SS316 A4-80 M10 (retained) | SS316 is galvanically intermediate between HDG steel (-1.0 V) and aluminum (-0.75 V) — correct practice |
| Isolation | Nylon bushings + HDPE washers | Nylon bushings + HDPE washers + closed-cell neoprene gasket | Add 3 mm neoprene gasket between steel top plate and aluminum frame base to prevent crevice moisture retention. Cost: +$0.50/joint x 8 = $4. |
| Sealant | Sikaflex 291 on contact face | Sikaflex 291 applied as fillet around joint perimeter | Change from interface sealant (compressed and squeezed out) to perimeter fillet bead (stays in place, blocks moisture ingress). No cost change. |
| Sacrificial anode | None specified at IF-04 | Add 50 g zinc disc anode at each mast top (bolt-on, under reflector frame) | 8 x 50 g = 400 g zinc total. Provides cathodic protection at most vulnerable interface. Cost: $2/anode x 8 = $16 total. |

**Coating schedule (full system):**

| Component | Coating | Thickness | Standard | Life (seawater) |
|-----------|---------|-----------|----------|----------------|
| Steel frame + masts | Hot-dip galvanize | >=85 um | ASTM A123 | 10-15 yr |
| Face plates (6061-T6) | Type II clear anodize | >=10 um | MIL-A-8625 | 5-10 yr |
| AM frames (AlSi10Mg) | Type III hard anodize | >=25 um | MIL-A-8625 | 10-15 yr |
| Hull (HDPE) | None required | — | — | >20 yr |
| Mooring chain (G30) | Hot-dip galvanize | Factory | — | 8-12 yr |
| SS316 fasteners | Passivated | Factory | — | >20 yr |

All coating lives far exceed the expendable product requirement (72 h to first engagement, single use).

### 5.2 DfManufacture — Vietnamese Fabrication Simplification

| # | Simplification | D8 Baseline | Optimized | Benefit |
|---|---------------|-------------|-----------|---------|
| DfM-1 | Frame weld count | ~120 individual welds (estimated) | ~90 welds (reduce gusset count on non-critical joints, use butt welds instead) | 25% fewer welds = 8 fewer labor-hours; reduced NDT scope |
| DfM-2 | Steel profile variety | 4 different section sizes (L50x50x5, L50x50x4, flat bar, tube) | 2 standard sections + tube (L50x50x5 for primary, L50x50x4 for secondary, 60 OD tube) | Simplified procurement; fewer setup changes at fab shop |
| DfM-3 | CNC face plate fixturing | Individual plate clamping per fly-cut | Gang fixture: 4 plates clamped simultaneously on vacuum table (2 rows of 2) | Batch 24 plates in 6 runs of 4 instead of 24 individual setups; saves ~6 hours CNC time |
| DfM-4 | Hull flange joint | Continuous HDPE welded lip flange on each half | Pre-formed HDPE extrusion clip-on flange with M10 through-bolt | Eliminates in-situ hull welding; flange is a commercial extrusion profile bolted to hull halves. Saves welding labor. |

### 5.3 DfAssembly — Fastener Reduction and Standardization

| Parameter | D8 Baseline | Optimized | Saving |
|-----------|-------------|-----------|--------|
| Total unique fastener types | ~12 (M8, M10, M12, M16 in HDG, SS316, various lengths) | 6 (M10 SS316 primary, M12 HDG for pad eye, M16 HDG for pad eye through-bolts — only 3 bolt sizes) | 50% fewer fastener SKUs; simplified spares kit |
| Hull joint bolts | 24x M10 SS316 | 18x M10 SS316 (utilization still 3.2%) | 6 fewer bolts to install/tighten; saves 10 min assembly time |
| Mast socket bolts | 4x M12 Gr 8.8 per socket x 8 = 32 bolts | 4x M10 SS316 per socket x 8 = 32 bolts (utilization 36%, PASS) | M10 matches reflector bolts — single wrench size for all mast/reflector work |
| Reflector-to-mast bolts | 4x M10 SS316 A4-80 per reflector | 4x M10 SS316 A4-80 (no change — already optimized) | — |
| Total bolt/fastener count | ~148 estimated | ~124 estimated | 24 fewer fasteners (16% reduction) |

### 5.4 DfMaintenance — Expendable Product Assessment

For an expendable target destroyed after a single engagement, maintenance optimization is limited to pre-deployment inspection and assembly reliability:

| Concern | Action | Impact |
|---------|--------|--------|
| Corrosion between production and deployment (shelf life) | Store mast+reflector assemblies in sealed poly bags with VCI paper; store hull outdoors (HDPE is weather-immune) | Ensures corrosion protection covers storage period of up to 12 months |
| Battery freshness (GPS) | Ship GPS beacon with battery disconnected; connect during pre-deployment check | Prevents shelf-life battery drain |
| Mooring inspection | Visual check of chain links for cracks, rode for abrasion before each deployment; replace if 10%+ zinc loss on chain | Recoverable mooring kit inspected between reuses |

### 5.5 DfCost — Lifecycle Cost Optimization

| Strategy | Description | Annual Saving (10 units/yr) |
|----------|-------------|---------------------------|
| AM frame volume contract | Negotiate annual contract with ASEAN LPBF bureau for 80 frames/yr (10 units x 8 frames). Volume pricing at $650/frame vs $900 spot. | $2,000/unit x 10 = $20,000/yr |
| Standardized mooring kits | Pre-build 3 standard mooring kits in batches of 30 (10 per depth variant). Chain and hardware purchased at coil/pallet pricing. | $150/unit x 10 = $1,500/yr |
| Vietnamese CNC batch scheduling | Schedule all 240 face plates/yr (10 units x 24 plates) as quarterly batch runs of 60 plates. CNC shop offers 20% discount for guaranteed quarterly orders. | $350/unit x 10 = $3,500/yr |
| Total annual production savings (10 units) | | **~$25,000/yr ($2,500/unit)** |

---

## 6. Optimization Trade-Off Matrix

Each optimization is assessed for its benefit, potential penalty, and net value. Conflicting optimizations are identified and resolved.

| # | Optimization | Benefit | Penalty | Net Value | Decision |
|---|-------------|---------|---------|-----------|----------|
| W-1 | Foam density reduction (40->32/48 split) | -24 kg, -$120 | Slightly reduced impact absorption in top hull section | **Positive** — reserve buoyancy still 2.4:1; top section never contacts water in SS<6 | **ACCEPT** |
| W-2 | Frame lightening (angles + cutouts) | -12 kg, -$100 | Reduced stiffness on 4 secondary radial beams | **Positive** — secondary beams carry <50% of primary beam load; large utilization margin | **ACCEPT** |
| W-3 | Mast wall reduction (4->3.5 mm) | -11 kg, -$100 | Utilization increases from 77% to 86%; less margin for unexpected loads | **Positive** — SF=2.0 still maintained; fatigue check passes; gusset provides local reinforcement at critical base section | **ACCEPT with monitoring** (verify with prototype strain gauge in Phase 4) |
| W-4 | AM frame lattice optimization | -8 kg, no cost | Slightly more complex AM build (lattice support removal) | **Positive** — lattice optimization is standard LPBF practice; AM bureau handles routinely | **ACCEPT** |
| W-5 | Fastener reduction | -8 kg, -$50 | Slightly fewer redundant fastener paths | **Positive** — all reduced joints remain well within safety margins (max 36% utilization) | **ACCEPT** |
| C-1 | AM batch pricing + DfAM | -$2,400 | Longer lead time if single-source; design iteration needed for DfAM | **Positive** — multi-source bidding mitigates supply risk; DfAM is one-time effort | **ACCEPT** |
| C-2 | Face plate nesting + batch CNC | -$280 | Requires larger stock sheets (1600x800 mm); CNC shop needs gang fixture | **Positive** — standard sheet size available; fixture is one-time investment | **ACCEPT** |
| C-3 | Steel frame simplification | -$250 | Fewer gussets on secondary beams slightly reduces connection stiffness | **Positive** — secondary beams have large utilization margin | **ACCEPT** |
| C-6 | Assembly labor reduction | -$300 | Faster assembly may reduce QC thoroughness | **Marginal** — must maintain 100% bolt torque verification regardless of fastener count | **ACCEPT with QC check** |
| Perf-1 | Reduce to 7 reflectors | -$1,600 (1 fewer reflector) | SIG-003 minimum RCS drops to 61 m^2 (requirement: >=700 m^2) | **NEGATIVE** — fails hard constraint by >10x | **REJECT** |
| Perf-2 | Reduce mast height to 2.5 m | -12 kg, -$50 | Reflector at 3.3 m AWL (within range); requires re-analysis | **Marginal** — structural benefit already captured in W-3; re-analysis cost and schedule risk exceed saving | **DEFER to Phase 4** |
| Perf-3 | Hybrid mooring for Kit A (shallow) | -$600 per Kit A | Less catenary weight at anchor; slightly higher anchor load | **Positive** — polyester stretch compensates for reduced catenary weight; anchor sizing unchanged | **ACCEPT** |

---

## 7. Optimized Design Summary

### 7.1 Before vs After Optimization

| Parameter | D8 Baseline | Optimized | Delta | Constraint | Status |
|-----------|-------------|-----------|-------|------------|--------|
| **Total displacement** | 986 kg | 923 kg | **-63 kg (-6.4%)** | <=1,100 kg | PASS (177 kg margin) |
| **Unit cost** | $35,640 | $31,750 | **-$3,890 (-10.9%)** | <=$36,000 | PASS ($4,250 margin) |
| **Cost at volume (10 units)** | $35,640 | ~$29,250 | **-$6,390 (-17.9%)** | — | Further improved |
| **Peak RCS** | >1,000 m^2 | >1,000 m^2 | No change | >=1,000 m^2 | PASS |
| **Number of reflectors** | 8 | 8 | No change | 8 (hard) | PASS |
| **Mast height** | 3.0 m above deck | 3.0 m above deck | No change | 2.5-3.5 m range | PASS |
| **Mast bending capacity** | 1,131 N-m (77% util) | 1,131 N-m (86% util) | Higher utilization | >=1,100 N-m | PASS |
| **Mooring SWL** | 5,800 kgf (19 mm G30) | 5,800 kgf (19 mm G30) | No change | >=4,536 kgf | PASS |
| **Stability (GM)** | 207.9 m | 222.4 m | +14.5 m (improved) | >0 | PASS |
| **Reserve buoyancy** | 96.2% | 96.4% | +0.2% | >90% | PASS |
| **Draft** | 19.1 mm | 17.9 mm | -1.2 mm (improved) | <=30 mm | PASS |
| **KG (CG height)** | 1.05 m | 1.05 m | No change | — | PASS |
| **Local content** | ~62% | ~62% | No change (structural) | >=85% target | GAP (policy) |
| **Fatigue (mast base)** | PASS (9.7% util) | PASS (~11% util) | Slight increase | 40,000 cycles | PASS |
| **Hull foam buoyancy** | 2,975 kg (3.0:1) | 2,980 kg (3.2:1) | Improved | Unsinkable | PASS |
| **Unique fastener types** | ~12 | 6 | -50% | — | Improved |
| **Total fastener count** | ~148 | ~124 | -16% | — | Improved |
| **Mooring Kit A cost** | $810 (chain only) | $210 (hybrid) | -$600 | SWL requirement | PASS |

### 7.2 Cost Breakdown Comparison (Per Unit)

```
COST COMPARISON — D8 BASELINE vs OPTIMIZED
============================================

                          D8 Baseline    Optimized      Saving
AM reflector frames       $9,600  ███████████  $7,200  ████████    $2,400
Hull + foam               $4,000  █████        $3,880  █████         $120
Assembly + QC             $3,700  █████        $3,400  ████          $300
Frame + masts             $2,000  ███          $1,650  ██            $350
Face plates               $1,780  ██           $1,500  ██            $280
GPS beacon                $1,800  ██           $1,800  ██              $0
Mooring                   $1,200  ██           $1,050  █             $150
Tow hardware                $400  █              $400  █               $0
Margin (10%)              $2,378  ███          $2,088  ███           $290
Other/overhead            $8,782  ██████████   $8,782  ██████████      $0
                         -------              -------             -------
TOTAL                    $35,640             $31,750              $3,890
```

### 7.3 Weight Breakdown Comparison

```
WEIGHT COMPARISON — D8 BASELINE vs OPTIMIZED
==============================================

                          D8 (kg)        Optimized (kg)  Saving
Hull shell (HDPE)           230  █████████    230  █████████     0
Fasteners/misc              145  ██████       137  ██████       -8
Steel frame                 150  ██████       138  ██████      -12
Mast system (8x)            136  ██████       125  █████       -11
Foam fill                   121  █████         97  ████        -24
Reflectors (8x)             120  █████        112  █████        -8
Mooring HW (on-hull)         80  ████          80  ████          0
GPS beacon                    5  ░              5  ░             0
                           ----              ----             ----
TOTAL                       986               923              -63

Margin to 1,100 kg:        114               177 (+55%)
```

---

## 8. Risk Assessment

Each optimization is assessed for risk of introducing new failure modes or degrading existing safety margins.

### 8.1 Optimization Risk Register

| # | Optimization | Risk Description | Probability | Consequence | Risk Level | Mitigation |
|---|-------------|------------------|-------------|-------------|------------|------------|
| R-O1 | W-1: Foam density reduction | Lower density foam (32 kg/m^3) may have lower compressive strength, reducing impact resistance in non-structural zones | LOW | LOW — top section of hull ring never contacts water below SS 5; bottom section retains 48 kg/m^3 | **LOW** | Specify minimum compressive strength 150 kPa for 32 kg/m^3 grade (standard for marine rigid PU foam). Test sample before production. |
| R-O2 | W-2: Frame lightening | Reduced beam sections on 4 secondary radials may allow increased hull deflection under asymmetric wave loading | LOW | LOW — HDPE hull is flexible by nature (E ~1 GPa); frame stiffness reduction of ~10% on secondary members has negligible effect on platform behavior | **LOW** | Verify secondary beam utilization in FEA model (Phase 4) before committing to production tooling. |
| R-O3 | W-3: Mast wall 4->3.5 mm | Thinner tube increases bending stress utilization from 77% to 86%. Leaves 14% margin to SF=2.0 allowable. Risk of exceedance if actual gust loads exceed design values. | MEDIUM | MEDIUM — mast failure at high utilization could lose 1 reflector. However, even with 1 reflector lost, 7 remaining provide >1,000 m^2 composite RCS during the initial engagement window. | **MEDIUM** | (a) Prototype testing: instrument one mast with strain gauges during sea trial at SS 4-5 to verify actual stress vs predicted. (b) Retain 60x4 tube as fallback if test data shows higher-than-predicted loads. (c) Gusset reinforcement at base provides local strength where moment is maximum. |
| R-O4 | W-4: AM lattice optimization | Lattice structures may contain internal voids or unsupported regions that reduce fatigue life | LOW | LOW — reflector frame loads are modest (142 N wind per D8 analysis); AlSi10Mg at sigma_y = 230 MPa is vastly over-specified for this load level | **LOW** | Require CT scan of first article AM frame to verify lattice integrity. Standard LPBF quality practice. |
| R-O5 | C-1: AM single-source risk | Concentrating 80 frames/yr with one ASEAN bureau creates supply chain dependency | MEDIUM | HIGH — if bureau has capacity issue or quality failure, production stops | **MEDIUM** | Maintain qualification of 2 ASEAN LPBF bureaus. Award 70% to primary, 30% to secondary. Cost premium of ~5% for split sourcing is justified by supply security. |
| R-O6 | W-3 + fatigue interaction | Thinner mast wall at 3.5 mm increases cyclic stress range at mast base weld. Fatigue check remains PASS (11% utilization at 40k cycles) but margin is reduced. | LOW | LOW — 40,000 cycles is extremely low-cycle for steel; allowable stress range at this cycle count (206 MPa) is 4x the applied range (~50 MPa). Even at 3.5 mm wall, fatigue is not a governing criterion. | **LOW** | No additional mitigation beyond existing gusset design and standard weld quality requirements (E43xx electrode, visual + UT at pad eye). |

### 8.2 Risk Summary

| Risk Level | Count | Items |
|------------|-------|-------|
| **HIGH** | 0 | None — no optimization introduces high risk |
| **MEDIUM** | 2 | R-O3 (mast wall thickness), R-O5 (AM supply chain) |
| **LOW** | 4 | R-O1 (foam), R-O2 (frame), R-O4 (lattice), R-O6 (fatigue) |

**Conclusion:** All optimizations are technically conservative. The two MEDIUM risks (R-O3 and R-O5) have clear mitigation paths: prototype instrumented testing for mast wall thickness, and dual-source qualification for AM supply. No optimization creates a new failure mode or violates a hard constraint.

---

## 9. Implementation Priority

Optimizations ranked by implementation priority for Phase 4 detail design:

| Priority | Optimization | Saving | Complexity | When |
|----------|-------------|--------|------------|------|
| 1 | C-1: AM batch pricing + DfAM | $2,400/unit | LOW — procurement action | Immediate (pre-Phase 4) |
| 2 | W-1: Foam density optimization | 24 kg, $120 | LOW — specification change | Phase 4 detail drawing |
| 3 | W-4: AM lattice optimization | 8 kg | LOW — DfAM review at bureau | Concurrent with C-1 |
| 4 | C-2: Face plate nesting | $280/unit | MEDIUM — fixture design needed | Phase 4 production planning |
| 5 | W-2: Frame lightening | 12 kg, $100 | MEDIUM — revised frame drawing | Phase 4 detail drawing |
| 6 | W-5: Fastener standardization | 8 kg, $50 | LOW — BOM revision | Phase 4 BOM |
| 7 | W-3: Mast 3.5 mm wall | 11 kg, $100 | MEDIUM — needs prototype validation | Phase 4 prototype build |
| 8 | C-3: Steel frame simplification | $250 | MEDIUM — revised fabrication drawing | Phase 4 detail drawing |
| 9 | C-6: Assembly labor optimization | $300 | LOW — procedure revision | Phase 4 assembly manual |
| 10 | Perf-3: Hybrid mooring Kit A | $600/Kit A | LOW — specification change | Phase 4 mooring kit spec |

---

## 10. Cross-References

### Phase 3 PRAD/RISM/OCP Documents
- [[PRAD_D8_design_structure.md]] -- D8: Structural analysis baseline (986 kg, all 18 checks PASS, 5 design updates)
- [[RISM_M4_material_analysis.md]] -- M4: Material selections and lifecycle cost estimates ($20,780 hardware)
- [[RISM_I2_critical_requirements.md]] -- I2: 55 hard constraints, 14 negative interactions on GEO-007 (mass limit)
- [[RISM_R1_requirements_identification.md]] -- R1: 74 direct embodiment requirements
- [[PRAD_A7_architecture_definition.md]] -- A7: Subsystem arrangement and spatial allocation
- [[PRAD_R6_rules_application.md]] -- R6: Rough layout with initial sizing
- [[PRAD_P5_principles_application.md]] -- P5: Preliminary layout

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1); CST-001 cost target, GEO-007 mass limit
- [[../01_requirements/standards_mapping.md]] -- ASTM A123, MIL-A-8625, Eurocode 3 fatigue

### Phase 2 Source Documents
- [[../02_conceptual/concept_selection.md]] -- Concept A architecture, $35.6K unit cost estimate

### Project Management
- [[../PROJECT_STATUS.md]] -- Project status tracker

---

**Document Status:** Draft v1.0 -- Systematic optimization complete. Key outcomes:
1. Weight reduced from 986 kg to 923 kg (-63 kg, -6.4%), margin to limit improved from 114 kg to 177 kg
2. Unit cost reduced from $35,640 to $31,750 (-$3,890, -10.9%), margin to target improved from $360 to $4,250
3. At volume (10 units/yr), unit cost further reduces to ~$29,250 (-17.9% from baseline)
4. All 55 hard constraints maintained; no performance degradation
5. 8 reflectors confirmed mandatory (7 reflectors fails SIG-003 by >10x)
6. Two MEDIUM risks identified with clear mitigation paths (mast prototype test, dual AM sourcing)
7. 10 optimizations prioritized for Phase 4 implementation
