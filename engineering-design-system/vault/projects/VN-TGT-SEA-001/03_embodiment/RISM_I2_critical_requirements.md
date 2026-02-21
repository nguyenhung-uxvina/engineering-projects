---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "I2 — Critical Requirements"
group: RISM
version: 1.0
created: 2026-02-10
status: draft
---

# Step I2: Critical Requirements — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Classify, rank, and prioritize the 74 direct embodiment requirements identified in Step R1 to focus Phase 3 design effort on the most constraining and conflict-prone requirements.
**Method:** Pahl & Beitz RISM Step I — Identify critical requirements through constraint classification, criticality scoring, conflict analysis, and ODI outcome mapping.
**Input:** [[RISM_R1_requirements_identification.md]] — 74 direct embodiment requirements mapped to Concept A subsystems
**Selected Concept:** Concept A "Baseline Optimized" (VDI 2225: 81.8%)

---

## 1. Constraint Classification

Each of the 74 direct embodiment requirements is classified as:

- **Hard Constraint (H):** Non-negotiable; failure to satisfy invalidates the design. Typically safety-critical, physics-driven, or contractually mandated.
- **Soft Constraint (S):** Desirable target that can be relaxed through trade-off. Typically performance margins, ergonomic preferences, or cost optimization targets.

### 1.1 Geometry Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| GEO-001 | Platform diameter | 8.0 m +/-0.1 m | **H** | Drives hull tooling, reflector spacing, stability (BM = 210.3 m); changing diameter cascades through all subsystems |
| GEO-002 | Hull depth | 0.5 m +/-0.05 m | **H** | Determines freeboard (0.48 m) and green water clearance; reducing depth risks deck flooding in SS 5 |
| GEO-003 | Reflector edge length | 0.8 m +/-0.005 m | **H** | Drives individual RCS (sigma = 152.3 m^2); any reduction fails SIG-001 |
| GEO-004 | Number of reflectors | 8 at 45 deg | **H** | 8 units required for 360 deg coverage with <=+/-2 dB variation; fewer creates coverage gaps |
| GEO-005 | Reflector height AWL | 3.0-4.0 m | **H** | Radar clutter rejection; below 3.0 m degrades seeker discrimination at low grazing angles |
| GEO-006 | GPS beacon height | >=4.5 m AWL | S | Can be relaxed to 4.0 m if mast design constrains; GPS antenna works at lower elevations |
| GEO-007 | Displacement limit | <=1,100 kg | **H** | Contractual limit; exceeding requires hull redesign (larger diameter or deeper section) |
| GEO-008 | Design draft | <=3 cm | S | Generous margin (actual 1.9 cm); can accept up to 5 cm without performance impact |
| GEO-009 | Reflector clearance | >=1.5 m between adj. | **H** | Prevents physical obstruction of adjacent reflector apertures; spacing is 2.01 m (33% margin) |
| GEO-010 | Mast structure | 8 masts, >=2.5 m, 45 deg | **H** | Required to achieve GEO-005 height; integral to Concept A architecture |

### 1.2 Kinematic Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| KIN-001 | Maximum roll | <=+/-7.5 deg SS 6 | **H** | Exceeding roll degrades RCS per SIG-005 (>1 dB loss above +/-7.5 deg) |
| KIN-003 | Weathervane | 360 deg unrestricted | **H** | SPM architecture; restricting rotation creates asymmetric mooring loads in storm |
| KIN-004 | Maximum heave | <=+/-3.0 m SS 6 | S | Platform follows wave surface; heave is physics-determined, not designable |
| KIN-005 | Tow speed | >=3.0 kn SS 5 | S | Can accept 2.5 kn with longer transit time; operational, not safety-critical |

### 1.3 Force/Load Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| FOR-001 | Steady wind force | 1,814 N (185 kgf) Bft 7 | **H** | Environmental load — determines mooring and mast design loads; physics-fixed |
| FOR-002 | Gust wind force | 3,557 N (363 kgf) peak | **H** | Peak dynamic load sizes mooring chain, mast section, and all connections |
| FOR-003 | Wave drift force | 3,765 N (384 kgf) SS 6 | **H** | Dominant mooring load component; physics-fixed for 8.0 m platform |
| FOR-004 | Steady mooring load | <=578 kgf | **H** | Sum of environmental forces; mooring must sustain continuously for 72 h |
| FOR-005 | Peak mooring load | <=1,512 kgf | **H** | Dynamic amplification of combined loads; chain/anchor must survive |
| FOR-006 | Mooring SWL | >=4,536 kgf (3:1) | **H** | Safety factor non-negotiable per marine engineering practice |
| FOR-007 | Anchor holding | >=1,500 kgf | **H** | Below this, anchor drags and target is lost; mission failure |
| FOR-008 | Tow line SWL | >=7,524 kgf | **H** | Safety factor on tow loads; failure = uncontrolled drift |
| FOR-009 | Green water on deck | 1,538 N (157 kgf) | S | Intermittent loading; mast bases can tolerate partial overload if socket design is robust |
| FOR-010 | Cyclic endurance | >=40,000 cycles +/-7 deg | **H** | Fatigue failure of mast base or reflector mount = loss of reflector = RCS degradation |
| FOR-011 | Mast bending capacity | >=1,100 N-m per mast | **H** | Below this, mast fails in gust; catastrophic loss of reflector |

### 1.4 Energy Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| ENR-001 | GPS battery life | >=72 h | **H** | Below 72 h, GPS dies before recovery; target becomes untrackable |
| ENR-002 | GPS transmit rate | >=1 Hz | S | 0.5 Hz acceptable for position tracking; 1 Hz is preferred |

### 1.5 Material Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| MAT-001 | Hull material | HDPE | **H** | Concept A architecture built around HDPE properties (UV, salt, impact, buoyancy) |
| MAT-002 | Flotation fill | Closed-cell foam | **H** | Without foam, hull breach = sinking; unsinkability is safety-critical |
| MAT-003 | Face plate material | 6061-T6 Al, 3 mm | **H** | RCS depends on flat, reflective aluminum surfaces; substitution changes RCS |
| MAT-004 | Frame material | AlSi10Mg LPBF | S | CNC-only fallback available at +/-0.3 deg tolerance; AM is preferred, not mandatory |
| MAT-005 | Frame steel | S235 HDG | S | Can substitute S275 or equivalent; galvanizing spec is the hard constraint |
| MAT-006 | Mooring chain | G30 HDG | **H** | Marine grade non-negotiable; underspec chain fails catastrophically |
| MAT-007 | Face plate finish | Ra <=10 um | S | Lambda = 32 mm >> Ra; finish up to Ra 25 um acceptable with <0.1 dB RCS loss |
| MAT-008 | Face plate protection | Type II anodize >=10 um | S | Can substitute marine paint or conversion coating if anodizing unavailable |
| MAT-009 | AM frame protection | Type III hard anodize >=25 um | **H** | AlSi10Mg corrodes rapidly in saltwater without hard coating; 72 h survival requires it |
| MAT-010 | Mast material | Galv. steel or marine Al | **H** | Must withstand 72 h salt spray + cyclic loading; unprotected steel fails in <72 h |

### 1.6 Signal/Performance Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| SIG-001 | Peak RCS >=1,000 m^2 | X-band | **H** | Core functional requirement; below 1,000 m^2 fails contract specification |
| SIG-002 | Average RCS >=1,000 m^2 | 360 deg | **H** | Contract specification; average must meet threshold from any azimuth |
| SIG-003 | Minimum RCS >=700 m^2 | Worst angle | **H** | Below 700 m^2, seeker acquisition probability drops below 99% at 20 km |
| SIG-004 | Angular variation | <=+/-2 dB | **H** | Larger variation causes inconsistent seeker behavior; test validity compromised |
| SIG-005 | RCS at +/-7 deg roll | <=1 dB loss | **H** | SS 6 roll must not degrade RCS below SIG-003 minimum threshold |
| SIG-009 | Orthogonality | <=+/-0.1 deg | S | +/-0.3 deg (CNC-only) still yields >120 m^2 per reflector; 0.1 deg is preferred |
| SIG-007 | GPS accuracy | <=+/-5 m CEP | S | Standard GNSS meets this by default; no design action required |

### 1.7 Safety Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| SAF-003 | Drift after mooring failure | Non-hazardous 24 h | **H** | Safety of navigation; GPS must continue transmitting |
| SAF-004 | Environmental debris | Non-toxic, recoverable | **H** | Regulatory compliance; HDPE + PU foam inherently meet this |
| SAF-005 | Tow bridle SWL | >=3x peak tow load | **H** | Safety factor for personnel protection during tow operations |
| SAF-006 | Reflector/mast retention | Safety wire + locking pins | **H** | 15 kg reflector falling from 3 m = 441 J impact; personnel hazard during deployment |
| SAF-007 | Positive GM all conditions | GM > 0 through SS 6 | **H** | Capsize = total loss; positive GM is physics-guaranteed at BM = 210 m |

### 1.8 Assembly Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| ASM-001 | Reflector assembly time | <=30 min per unit | S | Can accept 45 min if alignment procedure requires additional steps |
| ASM-003 | Field tools | Standard hand tools only | **H** | Deployment crew has no specialized equipment; constraint is operational |
| ASM-004 | Reflector-to-mast attachment | Bolted + Nylock + pins + wire | **H** | Redundant retention is safety-critical per SAF-006 |
| ASM-005 | Mooring pad eye | Through-bolted, 200x200x10 mm | **H** | Pad eye is primary load path; under-design = mooring failure = target loss |
| ASM-006 | Field mast erection | <=15 min (8 masts, 2-person) | S | Can accept 20-25 min; deployment time budget has margin (30 min total) |

### 1.9 Transport Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| TRA-001 | Container fit | >=1 per 40 ft | **H** | Logistics requirement; oversized platform cannot ship to remote bases |
| TRA-002 | Road width | <=2.5 m per section | **H** | Vietnamese road width limit; oversize permit is fallback but adds cost/schedule |
| TRA-003 | Tow configuration | 2-point bridle + drogue | S | Single-point tow acceptable at reduced speed; drogue improves yaw stability |
| TRA-004 | Tow line spec | 16 mm Dyneema >=8,000 kgf | **H** | Below SWL rating creates unsafe tow; non-negotiable |

### 1.10 Operational Requirements

| ID | Requirement | Value | H/S | Justification |
|----|-------------|-------|-----|---------------|
| OPR-002 | Survival SS 5-6 72 h | Anchored | **H** | Core differentiator (ODI O-57 EXTREME); cannot relax |
| OPR-003 | Survival Bft 6-7 | Gusts to 46 kn | **H** | Environmental loading basis; all structural sizing depends on this |
| OPR-005 | Water depth 10-80 m | Depth-dependent mooring | **H** | Operational requirement; mooring kits must cover full range |
| OPR-007 | Temperature -5 to +55 C | All materials | **H** | Material selection must cover range; HDPE embrittlement below -10 C |
| OPR-009 | Salt spray 72 h | Continuous | **H** | All materials must survive; corrosion protection is non-negotiable |
| OPR-010 | Missile compatibility | X-band active seeker | **H** | Product function; incompatibility = no market |

### 1.11 Classification Summary

| Classification | Count | Percentage |
|----------------|-------|------------|
| **Hard Constraint (H)** | **55** | **74%** |
| **Soft Constraint (S)** | **19** | **26%** |
| **Total Direct Embodiment** | **74** | **100%** |

**Interpretation:** The high ratio of hard constraints (74%) confirms that THANH TRI-H is a tightly constrained system. Most requirements are physics-driven (environmental loads, RCS equations, stability) or safety-mandated (mooring SWL, retention, positive GM), leaving limited trade-off space. The 19 soft constraints represent the primary design freedom available during embodiment.

---

## 2. Criticality Ranking

Each of the 74 direct embodiment requirements is scored across four impact dimensions (0-3 scale each):

| Score | Safety Impact | Performance Impact | Cost Impact | Schedule Impact |
|-------|--------------|-------------------|-------------|-----------------|
| **3** | Failure causes loss of life or total asset loss | Failure prevents primary function | >20% unit cost increase | >4 weeks delay |
| **2** | Failure creates hazardous condition | Significant performance degradation | 10-20% cost increase | 2-4 weeks delay |
| **1** | Minor safety concern | Minor performance reduction | 5-10% cost increase | 1-2 weeks delay |
| **0** | No safety impact | No performance impact | <5% cost impact | <1 week delay |

### 2.1 Top 25 Requirements by Criticality Score

| Rank | ID | Requirement | Safety | Perf. | Cost | Sched. | **Total** | Subsystem |
|------|-----|------------|--------|-------|------|--------|-----------|-----------|
| 1 | FOR-005 | Peak mooring load <=1,512 kgf | 3 | 3 | 2 | 2 | **10** | L0 Mooring |
| 2 | FOR-006 | Mooring SWL >=4,536 kgf | 3 | 3 | 2 | 1 | **9** | L0 Mooring |
| 3 | SIG-001 | Peak RCS >=1,000 m^2 | 0 | 3 | 3 | 3 | **9** | L3 Reflectors |
| 4 | FOR-010 | Cyclic endurance >=40,000 | 3 | 2 | 2 | 2 | **9** | L2.5 Masts |
| 5 | FOR-011 | Mast bending >=1,100 N-m | 3 | 2 | 2 | 2 | **9** | L2.5 Masts |
| 6 | OPR-002 | Survival SS 5-6 72 h | 2 | 3 | 2 | 2 | **9** | All structural |
| 7 | FOR-007 | Anchor holding >=1,500 kgf | 3 | 2 | 1 | 2 | **8** | L0 Mooring |
| 8 | GEO-001 | Platform 8.0 m diameter | 0 | 3 | 3 | 2 | **8** | L1 Hull |
| 9 | GEO-003 | Reflector edge 0.8 m | 0 | 3 | 2 | 3 | **8** | L3 Reflectors |
| 10 | SIG-002 | Average RCS >=1,000 m^2 | 0 | 3 | 2 | 3 | **8** | L3 Reflectors |
| 11 | MAT-001 | Hull HDPE | 2 | 2 | 2 | 2 | **8** | L1 Hull |
| 12 | SAF-006 | Reflector/mast retention | 3 | 1 | 1 | 2 | **7** | L2.5 Masts |
| 13 | ASM-005 | Mooring pad eye through-bolted | 3 | 2 | 1 | 1 | **7** | L2 Frame |
| 14 | GEO-005 | Reflector 3.0-4.0 m AWL | 0 | 3 | 2 | 2 | **7** | L2.5 Masts |
| 15 | GEO-007 | Displacement <=1,100 kg | 1 | 2 | 2 | 2 | **7** | All systems |
| 16 | MAT-002 | Closed-cell foam fill | 3 | 1 | 1 | 1 | **6** | L1 Hull |
| 17 | MAT-003 | 6061-T6 Al face plates | 0 | 3 | 2 | 1 | **6** | L3 Reflectors |
| 18 | SIG-003 | Min RCS >=700 m^2 | 0 | 3 | 1 | 2 | **6** | L3 Reflectors |
| 19 | SIG-004 | Angular variation <=+/-2 dB | 0 | 3 | 1 | 2 | **6** | L3 Reflectors |
| 20 | SIG-005 | RCS at +/-7 deg <=1 dB loss | 0 | 3 | 1 | 2 | **6** | L3 Reflectors |
| 21 | ENR-001 | GPS battery >=72 h | 2 | 2 | 1 | 1 | **6** | L5 GPS |
| 22 | KIN-001 | Roll <=+/-7.5 deg | 1 | 3 | 1 | 1 | **6** | L1 Hull |
| 23 | MAT-009 | AM frame hard anodize >=25 um | 1 | 2 | 1 | 2 | **6** | L3 Reflectors |
| 24 | TRA-001 | Container fit (40 ft) | 0 | 1 | 2 | 3 | **6** | L1 Hull |
| 25 | OPR-009 | Salt spray 72 h continuous | 1 | 2 | 2 | 1 | **6** | All exposed |

### 2.2 Criticality Distribution

| Score Range | Count | Description |
|-------------|-------|-------------|
| 9-10 (Critical) | 6 | Highest priority — design-driving, must resolve first |
| 7-8 (High) | 7 | High priority — constrain major design decisions |
| 5-6 (Medium) | 24 | Medium priority — influence detail design choices |
| 3-4 (Low) | 25 | Lower priority — resolved through standard practice |
| 0-2 (Minimal) | 12 | Minimal design impact — addressed by material/process selection |

---

## 3. Conflict Identification

These are **embodiment-level conflicts** — physical design trade-offs where satisfying one requirement makes satisfying another harder. These differ from the Phase 1 conflict register (which addressed specification-level conflicts between requirement values).

### 3.1 Embodiment Conflict Register

| CF# | Conflict Description | Req. A | Req. B | Severity | Resolution Approach |
|-----|---------------------|--------|--------|----------|---------------------|
| **CF-01** | **Mast height vs mast structural capacity** — Increasing reflector height (GEO-005: 3.0-4.0 m AWL) increases bending moment arm, requiring larger tube section, which increases mass and windage, which further increases bending moment. Self-reinforcing loop. | GEO-005 (3.0-4.0 m AWL) | FOR-011 (>=1,100 N-m), GEO-007 (<=1,100 kg) | **HIGH** | (a) Optimize mast height at lowest value in range (3.0 m AWL = 2.5 m above deck); (b) FEA to find minimum tube section; (c) Guyed mast fallback (P4.2) if free-standing margin <15% |
| **CF-02** | **Displacement budget vs corrosion protection** — Heavier galvanizing (FOR-010 fatigue, OPR-009 salt spray) adds mass to steel components (frame + 8 masts ~310 kg = 32% of total). Each 10 um additional HDG coating adds ~2 kg across all steel parts. | GEO-007 (<=1,100 kg) | OPR-009 (salt spray 72 h), MAT-010 (galvanized) | **MEDIUM** | Design to 85 um HDG minimum (ASTM A123); accept 980 kg baseline with 120 kg margin; do not over-specify coating thickness |
| **CF-03** | **Reflector precision vs AM cost and schedule** — Achieving +/-0.1 deg orthogonality (SIG-009) requires AM frames, which drive 48% of hardware cost ($16K of $33.4K). Relaxing to +/-0.3 deg (CNC-only) saves $8K/unit but reduces individual RCS by ~20%. | SIG-009 (<=+/-0.1 deg) | CST-001 (<=36K), PRD-007 (<=3 wk lead time) | **HIGH** | (a) Maintain AM as baseline with CNC fallback; (b) Prototype one reflector in Phase 3 to validate RCS at +/-0.1 deg; (c) If military rejects AM, CNC-only at 800-1,000 m^2 still meets SIG-001 with margin |
| **CF-04** | **Hull diameter vs transport** — 8.0 m hull (GEO-001) exceeds 2.5 m road width limit (TRA-002) and 12.2 m container length (TRA-001). Must either split hull into sections (adding interface IF-07 weight, sealing complexity, and cost) or accept oversize transport constraints. | GEO-001 (8.0 m) | TRA-001 (40 ft container), TRA-002 (<=2.5 m road) | **HIGH** | (a) 2-section hull design (2 x 4.0 m halves, bolted flange at midline); (b) Each half is 4.0 m wide — still oversize but manageable with escort; (c) Phase 3 trade study: 2-section weight/cost penalty vs oversize permit |
| **CF-05** | **Mooring depth range vs kit cost** — Covering 10-80 m depth (OPR-005) requires different chain/rode lengths per depth. A universal mooring kit would be oversized for shallow water (expensive, heavy) or undersized for deep water (unsafe). 3 variants needed. | OPR-005 (10-80 m) | CST-001 (<=36K per unit), GEO-007 (mass budget) | **MEDIUM** | (a) Define 3 standard mooring kits (shallow 10-20 m, medium 20-40 m, deep 40-60 m); (b) Kit cost: $1,200-$3,500 depending on depth; (c) Customer orders depth-specific kit; mooring kit is NOT included in platform displacement |
| **CF-06** | **Field assembly speed vs joint reliability** — Quick mast erection (ASM-006: 15 min for 8 masts) conflicts with robust retention (SAF-006: safety wire + locking pins, ASM-004: Nylock + pins + wire). Safety wire installation alone takes 2-3 min per mast. | ASM-006 (<=15 min) | SAF-006 (safety wire + locking pins), ASM-004 (Nylock + pins + wire) | **MEDIUM** | (a) Pre-assemble reflector-to-mast at factory (ASM-004 done in factory, not field); (b) Field operation is socket-insert + locking pin only (ASM-006); (c) Safety wire on mast locking pin: 1 min per mast x 8 = 8 min; leaves 7 min for insertion |
| **CF-07** | **Reflector surface protection vs RCS performance** — Anodizing (MAT-008: Type II >=10 um) changes surface reflectivity slightly. Hard anodize (MAT-009: Type III >=25 um) on AM frames has Ra ~3-5 um post-process but frame is not a reflecting surface. Risk: anodize on CNC face plates changes surface from bright Al to matte. | MAT-008 (anodize face plates) | SIG-001 (RCS >=1,000 m^2), MAT-007 (Ra <=10 um) | **LOW** | (a) Type II clear anodize has negligible RF effect at X-band (lambda = 32 mm >> coating thickness 10 um); (b) Verify with prototype RCS measurement; (c) Black anodize may absorb more — use clear only |
| **CF-08** | **HDPE hull stiffness vs mooring/mast load transfer** — HDPE is flexible (E ~1 GPa vs steel 200 GPa). Mooring pad eye (ASM-005: peak 1,512 kgf) and 8 mast sockets (FOR-011: 1,100 N-m each) concentrate loads on the HDPE hull. Without adequate steel frame, hull deforms locally. | MAT-001 (HDPE hull) | FOR-005 (peak 1,512 kgf), FOR-011 (1,100 N-m/mast) | **HIGH** | (a) Steel frame (L2) distributes all concentrated loads across hull; (b) Frame acts as structural backbone — hull is buoyancy shell only; (c) Pad eye + mast sockets welded to frame, not bolted to HDPE; (d) Frame-to-hull connection via multiple distributed bolts or continuous weld |

### 3.2 Conflict Severity Summary

| Severity | Count | Conflicts |
|----------|-------|-----------|
| HIGH | 4 | CF-01 (mast height/strength), CF-03 (precision/cost), CF-04 (hull/transport), CF-08 (HDPE/loads) |
| MEDIUM | 3 | CF-02 (mass/corrosion), CF-05 (depth/cost), CF-06 (speed/reliability) |
| LOW | 1 | CF-07 (anodize/RCS) |

**Key finding:** The 4 HIGH severity conflicts all involve the mast system (CF-01), reflector manufacturing (CF-03), hull logistics (CF-04), or structural load paths (CF-08). These must be resolved in the earliest Phase 3 embodiment decisions.

---

## 4. ODI Outcome Mapping

Maps the top 15 ODI outcomes (by opportunity score) to embodiment requirements, showing which physical design decisions satisfy which customer needs.

| ODI Outcome | Description | Opp. Score | Embodiment Requirements | Design Decision Affected |
|-------------|-------------|------------|------------------------|--------------------------|
| **O-57** | Minimize likelihood that environmental conditions cause target failure | **18.0 EXTREME** | OPR-002, OPR-003, FOR-005, FOR-006, FOR-010, FOR-011, MAT-010, OPR-009 | Mast section sizing (CF-01), mooring chain grade, HDG spec, foam fill — ALL structural sizing derives from SS 5-6 survival |
| **O-37** | Minimize likelihood that mooring anchor drags in storm | **15.0 EXTREME** | FOR-004, FOR-005, FOR-006, FOR-007, MAT-006, OPR-005, ASM-005 | Anchor type/weight, chain size (12 vs 16 mm), catenary scope, pad eye design, depth-dependent kit selection |
| **O-71** | Minimize total cost of ownership over 50 tests | **15.0 EXTREME** | GEO-007, MAT-001, MAT-005, PRD-002 (indirect) | Hull material (HDPE = 20+ yr life), local content optimization, expendable concept validation |
| **O-29** | Minimize likelihood that missile seeker fails to acquire target | **13.8 HIGH** | SIG-001, SIG-002, SIG-009, GEO-003, MAT-003, MAT-004 | Reflector edge length, face plate material/flatness, AM frame orthogonality — core RCS chain |
| **O-31** | Minimize variation in radar return across 360 deg | **14.0 HIGH** | SIG-004, GEO-004, GEO-005, GEO-009, GEO-010 | Number of reflectors (8), angular spacing (45 deg), mast height uniformity, reflector clearance |
| **O-62** | Minimize cost per valid test event | **14.9 HIGH** | GEO-007, MAT-001, MAT-005, SIG-001 | Unit cost drivers: HDPE hull ($8K), reflectors ($16K), steel frame ($3.5K); AM vs CNC trade-off (CF-03) |
| **O-36** | Minimize likelihood of platform capsize or instability | **14.0 HIGH** | KIN-001, SAF-007, GEO-001, GEO-002, GEO-007 | Hull diameter (8.0 m), depth (0.5 m), mass distribution (low CG); BM = 210 m is inherent in geometry |
| **O-33** | Minimize position drift from intended test location | **14.0 HIGH** | FOR-004, FOR-005, FOR-007, OPR-005, OPR-006, KIN-003 | Mooring catenary design, anchor selection, scope ratio per depth, weathervaning freedom |
| **O-40** | Maximize range at which missile seeker acquires target | **13.5 HIGH** | SIG-001, SIG-006, GEO-005 | RCS magnitude (>1,000 m^2 = 20+ km acquisition), reflector height (reduces sea clutter at range) |
| **O-42** | Minimize radar cross-section fades during engagement | **12.5 HIGH** | SIG-003, SIG-005, KIN-001, GEO-004 | Minimum RCS at worst angle (>=700 m^2), roll-induced RCS degradation, reflector count for overlap |
| **O-73** | Maximize indigenous/local content percentage | **14.0 HIGH** | MAT-001, MAT-003, MAT-005, MAT-006, MAT-010, PRD-002 | HDPE (local), CNC Al (local), steel (Hoa Phat/Nam Kim), chain (marine supply); AM frames are only import (ASEAN) |
| **O-46** | Minimize test failures attributable to target signature | **13.5 HIGH** | SIG-001, SIG-002, SIG-003, SIG-004, SIG-009, QUA-001, QUA-002 | Reflector QC (100% RCS measurement), orthogonality check (+/-0.1 deg), 360 deg pattern verification |
| **O-55** | Minimize likelihood of GPS position loss during deployment | **11.5 MOD** | ENR-001, ENR-002, SIG-007, GEO-006 | Battery capacity (>=72 h), mounting height (>=4.5 m AWL), waterproof enclosure (IP67/68) |
| **O-34** | Minimize time from anchor connection to target ready | **12.5 HIGH** | ASM-006, ASM-003, ASM-004, ERG-002, ERG-005 | Socket-insert mast design, tool-free connections, pre-assembled mast+reflector units (CF-06 resolution) |
| **O-26** | Minimize weight of heaviest component handled in field | **10.5 MOD** | ERG-003, ERG-004, ASM-006, GEO-007 | Mast+reflector unit ~31 kg (2-person lift); no component >150 kg in field; socket-insert = no crane |

### 4.1 Outcome Coverage Assessment

| Coverage Level | Count | Outcomes |
|----------------|-------|----------|
| Fully addressed by embodiment requirements | 12 | O-57, O-37, O-29, O-31, O-62, O-36, O-33, O-40, O-42, O-73, O-46, O-34 |
| Partially addressed (indirect influence) | 2 | O-71 (TCO depends on production + operations), O-55 (COTS GPS selection) |
| Addressed but limited design freedom | 1 | O-26 (mass is physics-constrained; already near minimum) |

**Key finding:** The top 3 EXTREME outcomes (O-57, O-37, O-71) are ALL addressed by the highest-criticality embodiment requirements (FOR-005, FOR-006, FOR-010, FOR-011, OPR-002). Environmental survivability drives the majority of structural sizing decisions.

---

## 5. Constraint Interaction Matrix

Shows interactions among the top 20 most constrained requirements. Interactions are classified as:

- **(+) Positive:** Satisfying requirement A helps satisfy requirement B
- **(-) Negative:** Satisfying requirement A makes requirement B harder
- **(0) Neutral:** No significant interaction

### 5.1 Interaction Matrix (Top 20 Requirements)

Requirements listed by criticality rank (Section 2):

```
         FOR  FOR  SIG  FOR  FOR  OPR  FOR  GEO  GEO  SIG  MAT  SAF  ASM  GEO  GEO  MAT  MAT  SIG  SIG  SIG
         005  006  001  010  011  002  007  001  003  002  001  006  005  005  007  002  003  003  004  005
FOR-005   .    +    0    +    +    +    +    -    0    0    0    0    +    -    -    0    0    0    0    0
FOR-006   +    .    0    0    0    +    +    0    0    0    0    0    +    0    -    0    0    0    0    0
SIG-001   0    0    .    0    0    0    0    +    +    +    0    0    0    +    -    0    +    +    +    +
FOR-010   +    0    0    .    +    +    0    0    0    0    0    +    0    -    -    0    0    0    0    0
FOR-011   +    0    0    +    .    +    0    0    0    0    0    +    0    -    -    0    0    0    0    +
OPR-002   +    +    0    +    +    .    +    0    0    0    +    +    +    0    -    +    0    0    0    0
FOR-007   +    +    0    0    0    +    .    0    0    0    0    0    +    0    0    0    0    0    0    0
GEO-001   -    0    +    0    0    0    0    .    0    +    +    0    0    0    -    0    0    0    +    0
GEO-003   0    0    +    0    0    0    0    0    .    +    0    0    0    0    -    0    +    0    0    0
SIG-002   0    0    +    0    0    0    0    +    +    .    0    0    0    +    -    0    +    +    +    +
MAT-001   0    0    0    0    0    +    0    +    0    0    .    0    -    0    +    +    0    0    0    0
SAF-006   0    0    0    +    +    +    0    0    0    0    0    .    0    0    -    0    0    0    0    0
ASM-005   +    +    0    0    0    +    +    0    0    0    -    0    .    0    -    0    0    0    0    0
GEO-005   -    0    +    -    -    0    0    0    0    +    0    0    0    .    -    0    0    0    0    +
GEO-007   -    -    -    -    -    -    0    -    -    -    +    -    -    -    .    0    -    0    0    0
MAT-002   0    0    0    0    0    +    0    0    0    0    +    0    0    0    0    .    0    0    0    0
MAT-003   0    0    +    0    0    0    0    0    +    +    0    0    0    0    -    0    .    +    0    0
SIG-003   0    0    +    0    0    0    0    0    0    +    0    0    0    0    0    0    +    .    +    +
SIG-004   0    0    +    0    0    0    0    +    0    +    0    0    0    0    0    0    0    +    .    0
SIG-005   0    0    +    0    +    0    0    0    0    +    0    0    0    +    0    0    0    +    0    .
```

### 5.2 Interaction Summary

| Interaction Type | Count | Key Pairs |
|------------------|-------|-----------|
| **Positive (+)** | 52 | FOR-005/FOR-006 (mooring loads reinforce chain sizing), SIG-001/SIG-002/SIG-003 (all RCS requirements mutually reinforcing), OPR-002/all structural (storm survival drives all load requirements) |
| **Negative (-)** | 28 | GEO-007 vs nearly all structural (mass limit opposes every structural strengthening), GEO-005 vs FOR-011/FOR-010 (mast height increases bending/fatigue loads), GEO-001 vs FOR-005 (larger platform = higher drift force = higher mooring load) |
| **Neutral (0)** | 120 | Most cross-domain pairs (e.g., SIG requirements vs MAT-002 foam) |

### 5.3 Most Constrained Requirements (by negative interaction count)

| Requirement | Negative Interactions | Description |
|-------------|----------------------|-------------|
| **GEO-007** (displacement <=1,100 kg) | **14 negatives** | Mass limit conflicts with every structural strengthening, larger reflectors, heavier corrosion protection, and deeper hull |
| **GEO-005** (reflector 3.0-4.0 m AWL) | **5 negatives** | Height increases mast loads (FOR-011, FOR-010), adds mass (GEO-007), increases mooring loads (FOR-005) |
| **FOR-005** (peak mooring 1,512 kgf) | **3 negatives** | Higher mooring load requires heavier chain/hardware (opposes GEO-007), larger pad eye (opposes mass) |

**Key finding:** GEO-007 (displacement limit) is the single most constraining requirement in the system, with 14 negative interactions. Every decision to increase strength, size, or protection conflicts with the mass budget. This makes mass management the central embodiment challenge.

---

## 6. Priority Requirements for Embodiment

The top 15 "design-driving" requirements that most constrain the physical design, ranked by combined criticality score and negative interaction count. These are the requirements that Phase 3 design teams must address first.

| Rank | ID | Requirement | Criticality | Neg. Int. | Subsystem Affected | Design Consequence |
|------|-----|------------|-------------|-----------|--------------------|--------------------|
| **1** | **GEO-007** | Displacement <=1,100 kg | 7 | 14 | **All systems** | Mass budget allocation is the primary design constraint. Every structural decision must be mass-checked. 120 kg margin (12%) is available but must be defended through embodiment. |
| **2** | **FOR-005** | Peak mooring load <=1,512 kgf | 10 | 3 | **L0 Mooring, L2 Frame** | Sizes mooring chain (12-16 mm G30), pad eye (200x200x10 mm backing plate), anchor (Danforth 50 kg), and all mooring hardware. Peak load is the single highest force in the system. |
| **3** | **FOR-011** | Mast bending >=1,100 N-m | 9 | 3 | **L2.5 Masts** | Sizes mast tube section (60 mm x 4 mm minimum), socket depth, base plate weld, and determines free-standing vs guyed configuration (TBD-011). Only 18% margin at baseline. |
| **4** | **SIG-001** | Peak RCS >=1,000 m^2 | 9 | 1 | **L3 Reflectors** | Locks reflector edge length (0.8 m), count (8), face plate material (6061-T6 Al), and orthogonality tolerance. Any deviation fails the core contract specification. |
| **5** | **FOR-010** | Cyclic endurance >=40,000 | 9 | 2 | **L2.5 Masts, L2 Frame** | Fatigue life of mast-socket weld, reflector mount bolts, and all cyclic connections. Requires fatigue analysis at detail category per Eurocode 3 or equivalent. |
| **6** | **OPR-002** | Survival SS 5-6 72 h | 9 | 1 | **All structural** | The overarching environmental requirement. All loads (FOR-001 through FOR-011) derive from SS 5-6 conditions. Storm survival is the core value proposition (ODI O-57: 18.0 EXTREME). |
| **7** | **GEO-005** | Reflector 3.0-4.0 m AWL | 7 | 5 | **L2.5 Masts** | Determines mast height, which cascades into mast bending (CF-01), mass (GEO-007), windage (FOR-001), and deployment procedure (ASM-006). Height must be optimized, not maximized. |
| **8** | **GEO-001** | Platform 8.0 m diameter | 8 | 2 | **L1 Hull** | Fixes hull tooling, drives transport conflict (CF-04), determines reflector spacing, and provides the waterplane area for stability. Cannot change without total system redesign. |
| **9** | **FOR-006** | Mooring SWL >=4,536 kgf | 9 | 1 | **L0 Mooring** | 3:1 safety factor on peak load. Sizes chain grade/diameter, shackle rating, swivel specification, and anchor specification. Marine safety standard — non-negotiable. |
| **10** | **MAT-001** | Hull HDPE | 8 | 1 | **L1 Hull** | Material selection locked by concept; drives fabrication method (TBD-007: rotomold vs welded), foam compatibility, UV resistance, and 20+ year service life. |
| **11** | **TRA-001** | Container fit (40 ft) | 6 | 1 | **L1 Hull** | Forces 2-section hull design (CF-04) or oversize transport. Interface IF-07 (hull section joint) is a critical embodiment decision with weight, sealing, and structural implications. |
| **12** | **FOR-007** | Anchor holding >=1,500 kgf | 8 | 0 | **L0 Mooring** | Anchor type (Danforth vs Bruce), weight (30-50 kg), and seabed compatibility. Requires proper setting protocol and may need pre-deployment verification pull test. |
| **13** | **SAF-006** | Reflector/mast retention | 7 | 1 | **L2.5 Masts, L3 Reflectors** | Safety-critical retention design: locking pins in sockets, safety wire on all bolted connections, redundant retention against vibration loosening. Drives fastener selection and assembly procedures. |
| **14** | **ASM-005** | Mooring pad eye through-bolted | 7 | 1 | **L2 Frame** | Primary structural interface between mooring and platform. Through-bolted with 200x200x10 mm backing plate, distributing 1,512 kgf peak load into steel frame. Weld sizing, bolt pattern, and frame stiffness all derive from this. |
| **15** | **SIG-009** | Orthogonality <=+/-0.1 deg | 5 | 0 | **L3 Reflectors** | Drives AM vs CNC decision (CF-03), manufacturing process, supplier selection, cost structure ($8K AM premium), and military acceptance risk (R-1). Soft constraint but high cost/schedule impact. |

### 6.1 Design Consequence Summary by Subsystem

| Subsystem | Design-Driving Requirements | Primary Consequence |
|-----------|----------------------------|---------------------|
| **L0: Mooring** | FOR-005, FOR-006, FOR-007, ASM-005 | Chain sizing, anchor selection, pad eye structural design, depth-dependent kit definition |
| **L1: Hull** | GEO-001, GEO-007, MAT-001, TRA-001 | 2-section hull design, HDPE fabrication method, foam fill procedure, mass budget enforcement |
| **L2: Frame** | ASM-005, FOR-005, GEO-007 | Frame section sizing, pad eye integration, mast socket welding, load distribution design |
| **L2.5: Masts** | FOR-011, FOR-010, GEO-005, SAF-006 | Tube section selection, socket design, fatigue analysis, free-standing vs guyed decision |
| **L3: Reflectors** | SIG-001, SIG-009, GEO-007 | Edge length lock, AM vs CNC decision, face plate material, anodizing specification |
| **L5: GPS** | ENR-001, GEO-006 | Battery pack sizing, mounting location on tallest mast, waterproof enclosure |
| **L6: Tow** | FOR-008, SAF-005 | Rope specification (16 mm Dyneema), bridle hardware, attachment point design |

---

## 7. Cross-References

### RISM Workflow

- [[RISM_R1_requirements_identification.md]] -- Step R1: 74 direct embodiment requirements identified and mapped to Concept A subsystems (input to this document)
- [[RISM_S3_material_selection.md]] -- Step S3: Material candidate screening (uses criticality ranking from this document to prioritize material decisions)
- [[RISM_M4_material_analysis.md]] -- Step M4: Material selection matrices using VDI 2225 weighted evaluation

### Phase 2 Source Documents

- [[../02_conceptual/concept_selection.md]] -- Concept A architecture, risk register (R-1 through R-5), Phase 3 entry recommendations
- [[../02_conceptual/function_structure.md]] -- Function-to-subsystem mapping (F1-F7, 21 sub-functions)
- [[../02_conceptual/concept_evaluation.md]] -- VDI 2225 evaluation scores and sensitivity analysis

### Phase 1 Source Documents

- [[../01_requirements/requirements_list.md]] -- 116 requirements (Rev B.1), 16 Pahl & Beitz categories, conflict register (C-01 through C-09)
- [[../01_requirements/requirements_validation.md]] -- Completeness check and gate criteria (12/12 PASS)
- [[../01_requirements/standards_mapping.md]] -- MIL-STD-810H, 882E, TCVN, ASTM F3301 compliance mapping

### Phase 0 Source Documents

- [[../00_odi/odi_analysis.md]] -- 73 ODI outcomes, opportunity scores (O-57: 18.0, O-37: 15.0, O-71: 15.0)

---

*Document generated as part of the RISM (Requirements-Identify-Select-Model) embodiment design process per Pahl & Beitz VDI 2221. This document feeds into Step S3 (Material Selection) and Step M4 (Material Analysis) by identifying which requirements are design-driving and where material trade-offs are most critical.*
