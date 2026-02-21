---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "M4 — Material Analysis"
group: RISM
version: 1.0
created: 2026-02-10
status: draft
---

# Step M4: Material Analysis — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Perform rigorous weighted material selection for all 5 major component groups using systematic scoring matrices. Compare candidate materials on engineering properties, corrosion performance, cost, and Vietnamese supply chain availability.
**Method:** Weighted scoring matrix (VDI 2225-compatible), 0-4 scale, criteria derived from Phase 1 requirements and product priority ranking.
**Input:** [[RISM_R1_requirements_identification.md]] — 74 direct embodiment requirements; [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1); [[../02_conceptual/concept_selection.md]] — Concept A architecture (81.8% VDI 2225)

---

## 1. Analysis Method

### 1.1 Weighted Material Selection Matrix Approach

Each component group is evaluated using a weighted scoring matrix per Pahl & Beitz methodology. The process:

1. **Identify evaluation criteria** — 6-8 criteria per component group derived from the embodiment-determining requirements in R1
2. **Assign weighting factors** — Weights sum to 1.00 and reflect the relative importance of each criterion for the specific component. Weights are derived from product priority ranking (Section 1.2)
3. **Score candidates** — Each material candidate receives a score from 0 to 4 on each criterion
4. **Calculate weighted sum** — Sum of (weight x score) for each candidate; maximum possible = 4.00
5. **Convert to percentage** — (weighted sum / 4.00) x 100% for comparison
6. **Select winner** — Highest percentage score, with rationale review for any close results

### 1.2 Scoring Scale

| Score | Meaning | Description |
|-------|---------|-------------|
| 0 | Unacceptable | Fails to meet minimum requirement; eliminates candidate |
| 1 | Poor | Marginally meets requirement; significant compromise |
| 2 | Adequate | Meets requirement with some limitations |
| 3 | Good | Meets requirement well; minor advantages |
| 4 | Excellent | Exceeds requirement; best-in-class for this criterion |

### 1.3 Product Priority Ranking

The following priority ranking governs weighting factor allocation across all component groups. This ranking is derived from the ODI analysis (3 EXTREME opportunity scores: O-57 environmental survivability, O-37 anchor holds in SS 6, O-71 total cost of ownership) and the requirements density map from R1:

| Priority | Factor | Rationale | Key Requirements |
|----------|--------|-----------|-----------------|
| **1** | **Corrosion resistance in seawater** | 72h continuous salt spray/immersion (OPR-009); marine environment is the dominant failure mode for all exposed components | OPR-009, OPR-007, MAT-008, MAT-009 |
| **2** | **Structural strength** | SS 5-6 survival loads (FOR-001 to FOR-011); must withstand 1,512 kgf peak mooring load, 1,100 N-m mast bending | FOR-005, FOR-006, FOR-010, FOR-011 |
| **3** | **Cost (material + processing)** | Unit cost target $35.6K (CST-001); expendable product — lifecycle cost is single-use cost | CST-001, CST-002, CST-007 |
| **4** | **Local availability (Vietnam/ASEAN)** | 85% local content target (PRD-002); Vietnamese defense procurement preference | PRD-002, PRD-004, PRD-005 |
| **5** | **Manufacturability** | Production rate 6 units/month (PRD-001); local CNC, welding, rotomolding capability | PRD-001, PRD-006, PRD-008 |
| **6** | **Weight** | Displacement limit 1,100 kg (GEO-007); 980 kg design target with 120 kg margin | GEO-007 |

---

## 2. Material Selection Matrices

### 2.1 Hull Material

**Component:** L1 — Flotation Hull (8.0 m diameter circular pontoon, 0.5 m depth)
**Requirements:** GEO-001, GEO-002, GEO-007, MAT-001, MAT-002, SAF-004, SAF-007, TRA-001
**Mass target:** 350 kg (hull shell + foam fill)
**Candidates:** HDPE (rotomolded/welded), GRP (glass-reinforced polyester), marine plywood (epoxy-sealed), PE foam composite (structural foam)

| # | Criterion | Weight | HDPE | Score | GRP | Score | Marine Plywood | Score | PE Foam Composite | Score |
|---|-----------|--------|------|-------|-----|-------|----------------|-------|-------------------|-------|
| 1 | UV resistance (20+ year marine life) | 0.15 | Inherent UV-stable, carbon black stabilized | **4** | Gelcoat degrades 5-10 yr, re-coating needed | **2** | UV degrades unless fully sealed; 5-10 yr | **1** | PE inherently UV-stable | **3** |
| 2 | Impact resistance (green water, debris) | 0.15 | Excellent — flexible, absorbs impact without fracture | **4** | Brittle — cracks under point impact, delaminates | **2** | Splits along grain under impact | **1** | Good — energy absorption in foam core | **3** |
| 3 | Seawater corrosion resistance | 0.20 | Immune to seawater corrosion; chemically inert | **4** | Good — gelcoat barrier; osmotic blistering after years | **3** | Poor — requires continuous epoxy seal; any breach causes rot | **1** | Good — PE skin immune; foam core must be sealed | **3** |
| 4 | Density / buoyancy contribution | 0.10 | 940-960 kg/m³ (near neutral; foam fill provides buoyancy) | **2** | 1,500-1,800 kg/m³ (negative; needs foam fill) | **2** | 500-600 kg/m³ (positive; naturally buoyant) | **3** | 30-60 kg/m³ (excellent buoyancy) | **4** |
| 5 | Rotomoldability / formability | 0.10 | Excellent — standard rotomold material; 8.0m may need 2-section | **4** | Not rotomoldable; requires layup or infusion — labor intensive | **2** | Sheet material; cannot form complex 3D hull | **1** | Can be CNC-cut and assembled; no molding | **2** |
| 6 | Cost (material + processing @ 10 units) | 0.15 | $7,000-8,000 per hull (rotomold or welded sections) | **3** | $10,000-14,000 per hull (hand layup labor intensive) | **2** | $3,000-5,000 per hull (cheap material, labor to seal) | **4** | $8,000-12,000 (CNC cutting + assembly + sealing) | **2** |
| 7 | Local availability (Vietnam) | 0.10 | Multiple VN suppliers (Tan Dai Hung, Binh Minh Plastics) | **4** | VN boat builders available (Nha Trang, Vung Tau yards) | **3** | Marine plywood from VN forestry (limited marine grade) | **2** | Limited — import from ASEAN (Thailand, Malaysia) | **1** |
| 8 | Environmental safety (non-toxic debris) | 0.05 | Non-toxic, recyclable, no leachates | **4** | Fiberglass dust hazardous; styrene in production | **2** | Non-toxic but decomposes to debris | **3** | Non-toxic PE | **4** |
| | **WEIGHTED SUM** | **1.00** | | **3.55** | | **2.35** | | **1.70** | | **2.70** |
| | **PERCENTAGE** | | | **88.8%** | | **58.8%** | | **42.5%** | | **67.5%** |

**WINNER: HDPE — 88.8%**

**Rationale:** HDPE dominates due to its unmatched combination of seawater immunity, UV stability, impact resistance, and rotomoldability. It is the standard material for marine buoys, pontoons, and aquaculture floats worldwide. Multiple Vietnamese suppliers can provide rotomolding or HDPE welding services. The only disadvantage (density near 950 kg/m³) is mitigated by closed-cell PU foam fill that provides >98% reserve buoyancy. Aligns with MAT-001 (HDPE mandated) and SAF-004 (non-toxic debris).

---

### 2.2 Structural Frame & Mast Material

**Component:** L2 — Structural Frame + L2.5 — Mast System (8 masts, 60 mm OD x 4 mm wall min)
**Requirements:** MAT-005, MAT-010, FOR-009, FOR-010, FOR-011, GEO-007, OPR-009, ASM-006
**Mass target:** Frame 150 kg + Masts 130 kg = 280 kg total
**Candidates:** S235 HDG mild steel, SS316 stainless steel, 6061-T6 aluminum, 5083-H116 marine aluminum

| # | Criterion | Weight | S235 HDG Steel | Score | SS316 Stainless | Score | 6061-T6 Al | Score | 5083-H116 Al | Score |
|---|-----------|--------|----------------|-------|-----------------|-------|------------|-------|--------------|-------|
| 1 | Strength-to-weight ratio (σ_y/ρ) | 0.15 | 235 MPa / 7,850 = 30 kPa·m³/kg | **2** | 205 MPa / 8,000 = 25.6 | **2** | 276 MPa / 2,700 = 102 | **4** | 228 MPa / 2,660 = 85.7 | **4** |
| 2 | Corrosion resistance in seawater | 0.25 | Requires HDG (85 µm min); zinc sacrificial — 10-15 yr life | **3** | Excellent inherent resistance; pitting possible in crevices | **4** | Poor without protection; rapid pitting in saltwater | **1** | Good marine alloy; resistant but needs passivation | **3** |
| 3 | Weldability (field repair + factory) | 0.15 | Excellent — standard MIG/MAG, any VN welding shop | **4** | Good — requires purge gas, austenitic filler, skilled welder | **3** | Requires TIG + 4043/5356 filler; heat-affected zone softens T6 | **2** | Good — TIG weld, non-heat-treatable so no HAZ softening | **3** |
| 4 | Cost (material + HDG/processing) | 0.15 | Steel $0.8-1.0/kg + HDG $0.3/kg = ~$1.1-1.3/kg | **4** | $4.0-5.0/kg — 4x steel cost | **1** | $3.5-4.5/kg + anodize/paint $0.5/kg | **2** | $4.0-5.0/kg + treatment | **1** |
| 5 | Local availability (Vietnam) | 0.10 | Excellent — Hoa Phat, Nam Kim produce S235 equivalent; HDG widely available | **4** | Limited VN production; mostly import (China, Japan) | **2** | Hoa Phat produces some Al; mostly import for marine grade | **2** | Import only (Korea, Japan, Australia) | **1** |
| 6 | Fatigue endurance (40,000 cycles at ±7°) | 0.10 | Good fatigue properties; HDG improves by reducing notch effects | **3** | Good — but sensitization risk at welds reduces fatigue | **3** | Poor — no definite endurance limit; 6061-T6 fatigues at ~97 MPa | **2** | Better than 6061 — endurance ~110 MPa at 10^7 cycles | **3** |
| 7 | Weight penalty (mass budget impact) | 0.10 | Heavy — 280 kg for frame+masts (within budget but uses 28% of total) | **2** | Heavier — ~290 kg (slightly more dense than mild steel) | **1** | Light — ~95 kg for equivalent stiffness sections | **4** | Light — ~100 kg | **4** |

| | **WEIGHTED SUM** | **1.00** | | **3.05** | | **2.50** | | **2.20** | | **2.60** |
| | **PERCENTAGE** | | | **76.3%** | | **62.5%** | | **55.0%** | | **65.0%** |

**WINNER: S235 HDG Mild Steel — 76.3%**

**Rationale:** S235 galvanized steel wins decisively on cost, weldability, and local availability — the three factors that matter most for a Vietnamese-manufactured expendable product. The corrosion protection from hot-dip galvanizing (85+ µm per ASTM A123) provides 10-15 years of service life, far exceeding the expendable target's single-deployment requirement. The weight penalty (280 kg vs ~100 kg for aluminum alternatives) is acceptable because the platform has 120 kg mass margin and the hull's extreme waterplane area (50.3 m²) easily supports the additional mass. Aluminum alternatives (6061-T6, 5083-H116) offer superior strength-to-weight but at 3-4x the cost with significantly less Vietnamese supply chain depth. SS316 is eliminated on cost ($4-5/kg vs $1.1-1.3/kg for HDG steel). Aligns with MAT-005 (S235 HDG specified), MAT-010 (galvanized steel tube for masts).

---

### 2.3 Reflector Face Plates

**Component:** L3 — Corner Reflector Face Plates (3 plates per reflector x 8 reflectors = 24 plates, each 800 x 800 x 3 mm)
**Requirements:** MAT-003, MAT-007, MAT-008, SIG-001, SIG-005, SIG-009, GEO-003
**Mass target:** ~2.1 kg per plate x 24 = ~50 kg total (within 120 kg reflector budget)
**Candidates:** 6061-T6 aluminum, 5052-H32 aluminum, SS304 stainless steel, C26000 brass (cartridge brass)

| # | Criterion | Weight | 6061-T6 Al | Score | 5052-H32 Al | Score | SS304 | Score | C26000 Brass | Score |
|---|-----------|--------|------------|-------|-------------|-------|-------|-------|--------------|-------|
| 1 | Achievable flatness (CNC fly-cut, target <0.1 mm) | 0.20 | Excellent — machines flat with standard CNC; low residual stress in T6 | **4** | Good — slightly more springback than T6; can achieve <0.1 mm | **3** | Good — but harder to machine; tool deflection on thin 3 mm plate | **3** | Good machinability; slightly soft — may distort under clamping | **3** |
| 2 | X-band reflectivity (9.4 GHz, σ_max) | 0.20 | Excellent conductor (σ = 25 MS/m); skin depth ~0.8 µm at 9.4 GHz; >99.9% reflection | **4** | Excellent conductor (σ = 20 MS/m); >99.9% reflection | **4** | Good conductor (σ = 1.4 MS/m); >99.5% reflection | **3** | Good conductor (σ = 15.9 MS/m); >99.8% reflection | **4** |
| 3 | CNC machinability (fly-cutting, drilling) | 0.15 | Excellent — one of best CNC materials; chips well, good finish | **4** | Good — slightly gummy compared to 6061; still machines well | **3** | Difficult — work-hardens; requires carbide/ceramic tooling, slow | **1** | Excellent — free-cutting; best machinability of group | **4** |
| 4 | Corrosion resistance in seawater | 0.20 | Good with Type II anodize (10+ µm); bare 6061 pits in saltwater | **3** | Better bare corrosion than 6061; anodize improves further | **4** | Excellent inherent resistance; no coating needed for 72h deployment | **4** | Poor — dezincification in seawater; green patina, structural loss | **1** |
| 5 | Cost (raw material + CNC + surface treatment) | 0.15 | Sheet ~$4.5/kg; CNC fly-cut ~$15/plate; anodize ~$5/plate | **3** | Sheet ~$4.0/kg; CNC ~$18/plate (gummier); anodize ~$5/plate | **3** | Sheet ~$5.5/kg; CNC ~$30/plate (hard material); no coating needed | **2** | Sheet ~$6.0/kg; CNC ~$12/plate; coating required | **2** |
| 6 | Weight (density impact on reflector mass) | 0.10 | 2,700 kg/m³ → 5.18 kg per plate (3 mm) | **3** | 2,680 kg/m³ → 5.14 kg per plate | **3** | 8,000 kg/m³ → 15.36 kg per plate — HEAVY | **1** | 8,530 kg/m³ → 16.4 kg per plate — HEAVIEST | **0** |

| | **WEIGHTED SUM** | **1.00** | | **3.50** | | **3.35** | | **2.55** | | **2.25** |
| | **PERCENTAGE** | | | **87.5%** | | **83.8%** | | **63.8%** | | **56.3%** |

**WINNER: 6061-T6 Aluminum — 87.5%**

**Rationale:** 6061-T6 is the clear winner with the best combination of machinability, flatness achievability, and X-band reflectivity. Its only weakness is bare corrosion in seawater, which is fully mitigated by Type II anodize (MAT-008). At 5.18 kg per plate, the 24-plate set weighs ~124 kg — but with 3 plates per reflector sharing the AM frame mount, the reflector-level mass is manageable. 5052-H32 is a strong runner-up (83.8%) with marginally better bare corrosion resistance, but its slightly gummy machining characteristics make fly-cutting to <0.1 mm flatness less reliable. SS304 is eliminated on weight (3x heavier) and machinability (work-hardening makes thin plate CNC difficult). Brass is eliminated on seawater corrosion (dezincification) and weight. Aligns with MAT-003 (6061-T6 Al, 3 mm specified).

---

### 2.4 Reflector Frame (AM/CNC Structure)

**Component:** L3 — Corner Reflector Structural Frame (1 frame per reflector x 8 = 8 frames, holding 3 face plates at 90.0 +/- 0.1 deg)
**Requirements:** MAT-004, MAT-009, SIG-009, PRD-003, PRD-007, ASM-001
**Mass target:** ~10 kg per frame (within 15 kg per reflector budget, with 3 x ~1.7 kg face plates)
**Candidates:** AlSi10Mg LPBF (laser powder bed fusion), 6061-T6 CNC machined, SS316L LPBF, PA12 Nylon SLS

| # | Criterion | Weight | AlSi10Mg LPBF | Score | 6061-T6 CNC | Score | SS316L LPBF | Score | PA12 Nylon SLS | Score |
|---|-----------|--------|---------------|-------|-------------|-------|-------------|-------|----------------|-------|
| 1 | Dimensional accuracy (±0.1° orthogonality) | 0.25 | Excellent — LPBF achieves ±0.05° with alignment features printed in; post-machined datum surfaces | **4** | Good — multi-part assembly with dowel pins; accumulates tolerance across joints (±0.15-0.3°) | **2** | Excellent — same LPBF precision as AlSi10Mg | **4** | Good — SLS accuracy ±0.1 mm linear but warpage risk on large parts | **2** |
| 2 | Structural strength (wind + wave loads on 0.8 m reflector) | 0.15 | Good — σ_y ~230 MPa (T5), σ_UTS ~350 MPa; adequate for reflector loads | **3** | Excellent — σ_y 276 MPa, σ_UTS 310 MPa; overqualified for this application | **4** | Excellent — σ_y ~500 MPa (AM), σ_UTS ~600 MPa; vastly over-spec | **4** | Poor — σ_y ~50 MPa; inadequate for structural loads at marine conditions | **1** |
| 3 | Corrosion resistance in seawater | 0.15 | Requires Type III hard anodize (25+ µm); bare AlSi10Mg corrodes rapidly | **2** | Requires anodize or paint; same as face plates | **2** | Excellent inherent resistance; no coating needed | **4** | Excellent — PA12 is chemically inert in seawater | **4** |
| 4 | AM/manufacturing availability (ASEAN region) | 0.20 | Good — Xometry (SG), Facfox (CN), JR Tech (SG), several ASEAN LPBF bureaus; AlSi10Mg is most common LPBF alloy | **4** | Excellent — any Vietnamese CNC shop can machine; no AM required | **4** | Limited — SS316L LPBF less common; fewer bureaus, longer lead times | **2** | Good — SLS is widely available; many ASEAN bureaus | **3** |
| 5 | Cost per frame (material + AM/CNC + post-processing) | 0.15 | $800-1,200 per frame ($100-150/kg at 8 kg; economy of scale at 8 units) | **2** | $400-600 per frame (multi-part CNC assembly + dowel pins) | **4** | $1,500-2,500 per frame (SS316L LPBF 2-3x cost of AlSi10Mg) | **1** | $300-500 per frame (SLS is cheapest AM process) | **4** |
| 6 | Weight (contribution to reflector mass budget) | 0.10 | ~8-10 kg per frame at lattice-optimized design | **3** | ~6-8 kg per frame (solid sections, machined pockets) | **3** | ~20-25 kg per frame — HEAVY (8,000 kg/m³) | **1** | ~4-6 kg per frame — lightest option | **4** |

| | **WEIGHTED SUM** | **1.00** | | **3.15** | | **3.05** | | **2.55** | | **2.75** |
| | **PERCENTAGE** | | | **78.8%** | | **76.3%** | | **63.8%** | | **68.8%** |

**WINNER: AlSi10Mg LPBF — 78.8%**

**Rationale:** AlSi10Mg LPBF wins primarily on dimensional accuracy — the critical requirement for corner reflector orthogonality (SIG-009: ±0.1°). The monolithic LPBF frame prints alignment datum surfaces, face plate mounting bosses, and structural ribs as a single part, eliminating the tolerance stack-up inherent in multi-part CNC assemblies (6061-T6 CNC scored only 2/4 on accuracy due to 4-6 piece assembly with accumulated joint tolerance of ±0.15-0.3°). The 6061-T6 CNC option is the designated fallback (Concept A-CNC variant at $28.6K) if military AM acceptance (Risk R-1) is not achieved. SS316L LPBF is eliminated on cost (2-3x AlSi10Mg) and weight (2.5x). PA12 Nylon SLS is eliminated on structural strength — inadequate σ_y (~50 MPa) for the sustained wind and wave loads on a 0.8 m reflector in SS 5-6. Aligns with MAT-004 (AlSi10Mg LPBF specified), MAT-009 (Type III hard anodize required).

---

### 2.5 Mooring Hardware

**Component:** L0 — Storm Mooring System (chain segment: 30-50 m length per deployment depth)
**Requirements:** MAT-006, FOR-004, FOR-005, FOR-006, FOR-007, OPR-005, OPR-009
**SWL target:** ≥4,536 kgf (3:1 on 1,512 kgf peak dynamic load)
**Candidates:** G30 HDG proof coil chain, G43 HDG high-test chain, SS316 chain, Dyneema (HMPE) rope

| # | Criterion | Weight | G30 HDG Chain | Score | G43 HDG Chain | Score | SS316 Chain | Score | Dyneema Rope | Score |
|---|-----------|--------|---------------|-------|---------------|-------|-------------|-------|--------------|-------|
| 1 | Strength (SWL ≥4,536 kgf at selected size) | 0.20 | 16 mm G30: SWL ~4,200 kgf (marginal); 19 mm: ~5,800 kgf (meets) | **3** | 13 mm G43: SWL ~4,800 kgf (meets); smaller, lighter | **4** | 16 mm SS316: SWL ~3,200 kgf (insufficient); 19 mm: ~4,500 kgf (marginal) | **2** | 12 mm Dyneema: SWL ~8,000 kgf (far exceeds); best strength/weight | **4** |
| 2 | Corrosion resistance in seawater | 0.25 | HDG zinc layer provides 8-15 year life; sacrificial protection | **3** | HDG zinc layer similar to G30; same galvanizing process | **3** | Excellent — inherent corrosion resistance; 20+ year marine life | **4** | Excellent — HMPE is chemically inert; no corrosion | **4** |
| 3 | Cost (per meter, including hardware) | 0.15 | 16 mm: ~$3-4/m; 50 m = $150-200; cheapest option | **4** | 13 mm: ~$5-7/m; 50 m = $250-350 | **3** | 16 mm: ~$15-20/m; 50 m = $750-1,000 | **1** | 12 mm: ~$8-12/m; 50 m = $400-600 | **2** |
| 4 | Local availability (Vietnam) | 0.15 | Widely available — marine supply stores in all Vietnamese ports | **4** | Available — less common than G30 but stocked by marine suppliers | **3** | Limited — import from Japan/Europe; not stocked locally | **1** | Available — imported but stocked by fishing/marine suppliers | **3** |
| 5 | Weight in water (affects catenary performance) | 0.10 | 16 mm: ~4.0 kg/m in air; heavy catenary provides good shock absorption | **3** | 13 mm: ~2.8 kg/m; lighter but still provides catenary action | **3** | 16 mm: ~4.3 kg/m; similar to G30 HDG | **3** | 12 mm: ~0.01 kg/m in water (near neutral); NO catenary effect | **1** |
| 6 | Fatigue/abrasion resistance (seabed contact) | 0.15 | Good — HDG zinc protects against abrasion-corrosion; chain links robust | **3** | Good — same HDG protection; slightly harder alloy resists wear better | **3** | Good — corrosion-resistant but scratches remove passive layer | **3** | Poor — Dyneema abraded by coral/rock seabed; needs chain leader | **1** |

| | **WEIGHTED SUM** | **1.00** | | **3.30** | | **3.15** | | **2.30** | | **2.60** |
| | **PERCENTAGE** | | | **82.5%** | | **78.8%** | | **57.5%** | | **65.0%** |

**WINNER: G30 HDG Proof Coil Chain — 82.5%**

**Rationale:** G30 HDG chain wins on the combination of cost, local availability, and adequate performance. At 16 mm diameter, SWL is ~4,200 kgf — marginally below the 4,536 kgf target. This will be resolved by specifying 19 mm G30 (SWL ~5,800 kgf, 28% margin) OR using a hybrid chain+rode system where the bottom 15-20 m is chain (catenary weight) and the upper section is 20 mm polyester rode (lighter, elastic shock absorption). G43 high-test chain (78.8%) is the runner-up — it achieves the required SWL at a smaller 13 mm size, saving weight, but costs 1.5-2x more per meter and is less readily available in Vietnamese ports. The cost-weight tradeoff may favor G43 in the detailed mooring design (Phase 3 catenary analysis — TBD-010). SS316 chain is eliminated on cost (5x G30) and local availability. Dyneema rope has excellent strength-to-weight but is eliminated because it provides zero catenary shock absorption (near-neutral buoyancy) and is vulnerable to seabed abrasion — both critical failure modes for a storm mooring system. Aligns with MAT-006 (G30 proof coil HDG specified).

**Note:** Final chain size selection (16 mm vs 19 mm G30, or 13 mm G43 alternative) will be determined by the catenary analysis in the detailed mooring design step (TBD-010/TBD-011).

---

## 3. Property Comparison Tables

### 3.1 Hull — HDPE vs GRP (Top 2)

| Property | HDPE (PE100 grade) | GRP (E-glass/polyester) | Unit | Test Standard |
|----------|--------------------|-------------------------|------|---------------|
| Yield strength (tensile) | 22-26 | 80-150 (fiber direction) | MPa | ASTM D638 / D3039 |
| Ultimate tensile strength | 26-33 | 100-200 | MPa | ASTM D638 / D3039 |
| Elongation at break | 600-1,000 | 1.5-3.0 | % | ASTM D638 |
| Density | 940-960 | 1,500-1,800 | kg/m³ | ASTM D792 |
| Elastic modulus | 0.8-1.2 | 8-15 | GPa | ASTM D638 |
| Thermal expansion | 100-200 | 15-25 | µm/m·°C | ASTM D696 |
| Corrosion rate in seawater | 0 (immune) | ~0 (gelcoat intact) | mm/yr | — |
| UV degradation (outdoor) | >20 yr (stabilized) | 5-10 yr (gelcoat) | years | — |
| Fatigue endurance (10^6 cycles) | ~10 MPa (low) | ~40 MPa | MPa | — |
| Cost in Vietnam | $1.5-2.0 | $3.0-4.5 | $/kg | Market 2026 |

### 3.2 Frame/Mast — S235 HDG Steel vs 5083-H116 Al (Top 2)

| Property | S235 HDG Mild Steel | 5083-H116 Marine Al | Unit | Test Standard |
|----------|---------------------|---------------------|------|---------------|
| Yield strength | 235 | 228 | MPa | EN 10025 / ASTM B928 |
| Ultimate tensile strength | 360-510 | 317 | MPa | EN 10025 / ASTM B928 |
| Elongation at break | 26 | 10 | % | EN 10025 |
| Density | 7,850 | 2,660 | kg/m³ | — |
| Elastic modulus | 210 | 70.3 | GPa | — |
| Thermal expansion | 12 | 23.8 | µm/m·°C | — |
| Corrosion rate in seawater (bare) | 0.1-0.3 | 0.01-0.05 | mm/yr | — |
| Corrosion rate (protected) | <0.01 (HDG, 85 µm Zn) | <0.01 (anodized) | mm/yr | ASTM A123 |
| Fatigue endurance (10^7 cycles) | ~160 (definite limit) | ~110 (no limit; at 10^7) | MPa | — |
| Galvanic compatibility | Anodic to most metals; needs isolation from Al/Cu | Anodic to steel; galvanic couple risk | — | — |
| Weld strength (% of base) | 95-100% | 65-75% (HAZ softening in 5083) | % | — |
| Cost in Vietnam (processed) | $1.1-1.3 (incl. HDG) | $4.0-5.0 (import + treatment) | $/kg | Market 2026 |

### 3.3 Face Plates — 6061-T6 Al vs 5052-H32 Al (Top 2)

| Property | 6061-T6 Aluminum | 5052-H32 Aluminum | Unit | Test Standard |
|----------|-----------------|-------------------|------|---------------|
| Yield strength | 276 | 193 | MPa | ASTM B209 |
| Ultimate tensile strength | 310 | 228 | MPa | ASTM B209 |
| Elongation at break | 12 | 12 | % | ASTM B209 |
| Density | 2,700 | 2,680 | kg/m³ | — |
| Elastic modulus | 68.9 | 70.3 | GPa | — |
| Thermal expansion | 23.6 | 23.8 | µm/m·°C | — |
| Electrical conductivity | 25 | 20 | MS/m | — |
| Skin depth at 9.4 GHz | 0.82 | 0.92 | µm | Calculated |
| Reflectivity at X-band | >99.99% | >99.98% | % | EM theory |
| Corrosion rate (bare, seawater) | 0.05-0.15 | 0.01-0.03 | mm/yr | — |
| Corrosion rate (Type II anodize) | <0.005 | <0.005 | mm/yr | MIL-A-8625 |
| CNC machinability rating | 90 (excellent) | 70 (good, slightly gummy) | Relative | — |
| Surface finish achievable (fly-cut) | Ra 0.4-1.6 µm | Ra 0.8-3.2 µm | µm | — |
| Flatness achievable (800x800x3 mm) | <0.05 mm (vacuum fixture) | <0.08 mm (vacuum fixture) | mm | — |
| Cost in Vietnam (sheet, 3 mm) | $4.5-5.5 | $3.5-4.5 | $/kg | Market 2026 |

### 3.4 Reflector Frame — AlSi10Mg LPBF vs 6061-T6 CNC (Top 2)

| Property | AlSi10Mg LPBF (T5 heat treated) | 6061-T6 CNC Machined | Unit | Test Standard |
|----------|----------------------------------|---------------------|------|---------------|
| Yield strength | 230 (XY) / 210 (Z) | 276 | MPa | ASTM F3318 / B209 |
| Ultimate tensile strength | 350 (XY) / 330 (Z) | 310 | MPa | ASTM F3318 |
| Elongation at break | 5-8 (XY) / 3-5 (Z) | 12 | % | ASTM F3318 |
| Density | 2,670 | 2,700 | kg/m³ | — |
| Elastic modulus | 70 | 68.9 | GPa | — |
| Thermal expansion | 21 | 23.6 | µm/m·°C | — |
| Surface roughness (as-printed) | Ra 8-15 µm | Ra 0.8-3.2 µm (machined) | µm | — |
| Surface roughness (post-machined datums) | Ra 1.6-3.2 µm | Ra 0.8-3.2 µm | µm | — |
| Dimensional accuracy (as-printed) | ±0.1-0.2 mm (LPBF) | ±0.02-0.05 mm (CNC) | mm | — |
| Achievable orthogonality (single-part) | ±0.05° (monolithic) | ±0.15-0.3° (multi-part assembly) | degrees | — |
| Corrosion rate (bare, seawater) | 0.1-0.3 (rapid pitting due to Si phases) | 0.05-0.15 | mm/yr | — |
| Corrosion rate (Type III hard anodize) | <0.01 | <0.005 (Type II adequate) | mm/yr | MIL-A-8625 |
| Fatigue endurance (10^7 cycles) | 80-100 (T5) | 97 | MPa | — |
| Cost per frame (ASEAN bureau) | $800-1,200 | $400-600 (VN CNC shop) | $/frame | Market 2026 |
| Lead time (8-frame batch) | 2-3 weeks (ASEAN LPBF) | 1-2 weeks (VN CNC) | weeks | — |

### 3.5 Mooring — G30 HDG Chain vs G43 HDG Chain (Top 2)

| Property | G30 HDG (19 mm) | G43 HDG (13 mm) | Unit | Test Standard |
|----------|-----------------|-----------------|------|---------------|
| Working load limit (SWL) | 5,800 | 4,800 | kgf | ASTM A413 |
| Breaking load | 17,400 | 14,400 | kgf | ASTM A413 |
| Safety factor (on 1,512 kgf peak) | 3.8:1 | 3.2:1 | — | — |
| Weight in air | 7.9 | 3.8 | kg/m | — |
| Weight in water | 6.9 | 3.3 | kg/m | — |
| Submerged weight per 50 m | 345 | 165 | kg | — |
| Zinc coating thickness (HDG) | 85+ | 85+ | µm | ASTM A123 |
| Corrosion rate (HDG, seawater) | <0.02 (zinc sacrificial) | <0.02 | mm/yr | — |
| Estimated zinc life (immersed) | 8-12 | 8-12 | years | — |
| Catenary restoring force at 50 m scope | Higher (heavier chain) | Lower (lighter chain) | — | — |
| Cost per meter (Vietnam) | $8-10 | $10-14 | $/m | Market 2026 |
| Cost per 50 m length | $400-500 | $500-700 | $ | — |
| Local availability | Excellent — all port chandlers | Good — specialized marine suppliers | — | — |

---

## 4. Lifecycle Cost Analysis

For an expendable target system, "lifecycle" is dominated by a single deployment (build, deploy, engage/destroy). The analysis below estimates total material and processing cost per component for one unit.

### 4.1 Hull (HDPE)

| Cost Element | Value | Notes |
|-------------|-------|-------|
| HDPE raw material (PE100, ~350 kg shell) | $700 | ~$2.0/kg x 350 kg; local VN supply |
| Rotomolding tooling (amortized @ 50 units) | $300 | $15,000 mold ÷ 50 units |
| Rotomolding labor + energy per hull | $1,500 | 2-section hull, Vietnamese rotomolder |
| Closed-cell PU foam fill (200 kg @ $4/kg) | $800 | Pour-in-place rigid PU foam |
| HDPE welding (if 2-section assembly) | $500 | Joining 2 half-hulls at mid-plane |
| Surface preparation + marking | $200 | Deck non-skid, identification markings |
| **Hull subtotal** | **$4,000** | |
| Expected service life (marine, immersed) | 20+ years | Far exceeds expendable use |
| Replacement frequency | N/A (expendable) | Destroyed by missile impact |
| **Hull lifecycle cost per unit** | **$4,000** | Single-use |

### 4.2 Structural Frame + Masts (S235 HDG Steel)

| Cost Element | Value | Notes |
|-------------|-------|-------|
| Steel raw material (frame 150 kg + masts 130 kg) | $350 | ~280 kg x $1.25/kg; Hoa Phat/Nam Kim supply |
| Cutting + forming (CNC plasma, bending) | $400 | Local VN fabrication shop |
| Welding (frame assembly, mast sockets, pad eyes) | $800 | MIG/MAG, Vietnamese welder; ~40 hr labor |
| Hot-dip galvanizing (280 kg steel) | $250 | ~$0.9/kg HDG; local VN galvanizing plant |
| Quality inspection (NDT on critical welds) | $200 | UT on mooring pad eye weld, mast socket welds |
| **Frame + mast subtotal** | **$2,000** | |
| HDG service life (immersed seawater) | 10-15 years | 85 µm zinc at ~6-10 µm/yr loss rate |
| Replacement frequency | N/A (expendable) | |
| **Frame + mast lifecycle cost per unit** | **$2,000** | Single-use |

### 4.3 Reflector Face Plates (6061-T6 Al)

| Cost Element | Value | Notes |
|-------------|-------|-------|
| 6061-T6 sheet stock (24 plates, ~124 kg total) | $680 | $5.5/kg x 124 kg; import (Korea/Japan/China) |
| CNC fly-cutting (24 plates x $15/plate) | $360 | Local VN CNC shop (3-axis mill, vacuum fixture) |
| Drilling + edge finishing (24 plates) | $240 | Mounting holes, deburr, edge chamfer |
| Type II anodize (24 plates, batch processing) | $300 | Local VN anodizer; 10+ µm clear anodize |
| Dimensional inspection (flatness, orthogonality) | $200 | CMM or granite flat + dial indicator; 100% check |
| **Face plate subtotal** | **$1,780** | |
| Anodize service life (marine environment) | 5-10 years | Type II anodize, 10+ µm, no maintenance |
| Replacement frequency | N/A (expendable) | |
| **Face plate lifecycle cost per unit** | **$1,780** | Single-use; 24 plates for 8 reflectors |

### 4.4 Reflector Frames (AlSi10Mg LPBF)

| Cost Element | Value | Notes |
|-------------|-------|-------|
| AM raw material + build (8 frames x $900 avg) | $7,200 | AlSi10Mg LPBF; ASEAN bureau (Xometry/Facfox) |
| T5 heat treatment (8 frames, batch) | $400 | Stress relief + age hardening per ASTM F3318 |
| Post-machining (datum surfaces, bolt holes) | $800 | CNC post-processing at AM bureau; 8 frames |
| Type III hard anodize (8 frames) | $600 | 25+ µm hard anodize; ASEAN anodizer |
| Shipping (ASEAN to Vietnam) | $200 | Air freight for 8 frames (~80 kg total) |
| Incoming QC (dimensional, orthogonality check) | $400 | CMM verification of all 8 frames; 100% inspection |
| **Frame subtotal** | **$9,600** | |
| Hard anodize service life (marine) | 10-15 years | Type III, 25+ µm; no maintenance |
| Replacement frequency | N/A (expendable) | |
| **Frame lifecycle cost per unit** | **$9,600** | Largest single cost element |

### 4.5 Mooring Hardware (G30 HDG Chain + Accessories)

| Cost Element | Value | Notes |
|-------------|-------|-------|
| G30 HDG chain (19 mm, 30 m typical) | $270 | $9/m x 30 m; VN marine chandler |
| Polyester braided rode (20 mm, 50 m) | $250 | $5/m x 50 m; VN marine supply |
| Danforth anchor (50 kg, HDG) | $350 | Local VN marine supply |
| Swivel (SWL 5,000 kgf, HDG) | $150 | Import (China/ASEAN) |
| Shackles (4x, SWL 5,000 kgf, HDG) | $120 | 4x $30 each; VN marine chandler |
| Thimbles, links, connecting hardware | $60 | Standard marine fittings |
| **Mooring subtotal** | **$1,200** | For 30 m depth deployment |
| HDG chain service life (seawater) | 8-12 years | Zinc sacrificial; chain reusable |
| Replacement frequency | Recoverable and reusable | Mooring pre-deployed and recovered after test |
| **Mooring lifecycle cost per unit** | **$1,200** | But mooring is recoverable — actual cost amortized over multiple uses |

### 4.6 Lifecycle Cost Summary

| Component Group | Material Cost | Processing Cost | Protection Cost | Total Per Unit | % of Hardware |
|-----------------|--------------|-----------------|-----------------|----------------|---------------|
| Hull (HDPE) | $1,500 | $2,200 | $200 | $4,000 | 21.2% |
| Frame + Masts (S235 HDG) | $350 | $1,400 | $250 | $2,000 | 10.6% |
| Face Plates (6061-T6) | $680 | $600 | $500 | $1,780 | 9.4% |
| Reflector Frames (AlSi10Mg) | $7,200 | $1,200 | $1,200 | $9,600 | 50.8% |
| Mooring (G30 HDG) | $870 | $0 | $0 | $1,200 | 6.3% |
| GPS Beacon (COTS) | $1,800 | $0 | $0 | $1,800 | 9.5% |
| Tow hardware | $400 | $0 | $0 | $400 | 2.1% |
| **TOTAL HARDWARE** | **$12,800** | **$5,400** | **$2,150** | **$20,780** | **100%** |

**Notes:**
- Total hardware cost $20,780 aligns with concept estimate (~$20,000 hardware + $13,000 labor/assembly/QC/margin = ~$33,400 hardware loaded → $35,640 fully loaded @ 10 units)
- AM reflector frames are the dominant cost element (50.8%) — confirms that Concept A-CNC fallback ($400-600/frame vs $900/frame) would reduce unit cost by ~$4,000
- Mooring system is recoverable — actual per-test mooring cost is $1,200 ÷ N reuses (expected 5-10 reuses = $120-240/test)

---

## 5. Local Content Assessment

### 5.1 Component-Level Local Content Analysis

| Component | Material Source | Fabrication Location | Assembly Location | Material Value ($) | Local Value ($) | Local % |
|-----------|----------------|---------------------|-------------------|-------------------|-----------------|---------|
| **HDPE hull shell** | **Vietnam** (Binh Minh Plastics, Tan Dai Hung) | **Vietnam** (VN rotomolder) | **Vietnam** | $700 | $700 | **100%** |
| **PU foam fill** | **Vietnam** (local polyurethane suppliers) | **Vietnam** (pour-in-place at hull) | **Vietnam** | $800 | $800 | **100%** |
| **Hull assembly labor** | — | — | **Vietnam** | $2,500 | $2,500 | **100%** |
| **Steel frame** | **Vietnam** (Hoa Phat S235 equiv.) | **Vietnam** (local fab shop) | **Vietnam** | $350 | $350 | **100%** |
| **Steel masts (8x)** | **Vietnam** (Hoa Phat/Nam Kim tube) | **Vietnam** (cut, weld base plates) | **Vietnam** | $200 | $200 | **100%** |
| **Hot-dip galvanizing** | **Vietnam** (local HDG plant) | **Vietnam** | — | $250 | $250 | **100%** |
| **Frame/mast welding labor** | — | — | **Vietnam** | $800 | $800 | **100%** |
| **6061-T6 Al sheet** | **Import** (Korea/Japan/China) | — | — | $680 | $0 | **0%** |
| **CNC face plate machining** | — | **Vietnam** (local CNC shop) | — | $600 | $600 | **100%** |
| **Type II anodize (face plates)** | — | **Vietnam** (local anodizer) | — | $300 | $300 | **100%** |
| **AlSi10Mg LPBF frames** | **ASEAN** (Singapore/China AM bureau) | **ASEAN** | — | $7,600 | $0 | **0%** |
| **Type III hard anodize (frames)** | — | **ASEAN** (at AM bureau location) | — | $600 | $0 | **0%** |
| **Reflector assembly labor** | — | — | **Vietnam** | $1,000 | $1,000 | **100%** |
| **G30 HDG chain** | **Vietnam/ASEAN** (VN port chandler stocks imported chain) | — | — | $270 | $135 | **50%** |
| **Polyester rode** | **Vietnam/ASEAN** | — | — | $250 | $125 | **50%** |
| **Danforth anchor** | **Vietnam** (VN marine hardware) | **Vietnam** (local foundry) | — | $350 | $350 | **100%** |
| **Mooring accessories** | **Import/ASEAN** (swivels, shackles) | — | — | $330 | $100 | **30%** |
| **GPS beacon** | **Import** (COTS, China/Taiwan) | — | — | $1,800 | $0 | **0%** |
| **Tow hardware** | **Vietnam/Import** (bridle, drogue) | — | — | $400 | $200 | **50%** |
| **Final assembly + QC** | — | — | **Vietnam** | $3,700 | $3,700 | **100%** |
| **Margin (10%)** | — | — | — | $2,378 | $2,378 | **100%** |

### 5.2 Local Content Summary

| Category | Total Value ($) | Local Value ($) | Local Content (%) |
|----------|----------------|-----------------|-------------------|
| **Vietnamese-sourced materials** | $3,080 | $3,080 | 100% |
| **Vietnamese fabrication + processing** | $5,450 | $5,450 | 100% |
| **Vietnamese assembly + QC** | $8,000 | $8,000 | 100% |
| **ASEAN-sourced (AM frames + processing)** | $8,200 | $0 | 0% |
| **Imported materials (Al sheet, GPS, mooring HW)** | $3,140 | $0 | 0% |
| **Partially local (mooring chain/rode, tow gear)** | $1,250 | $560 | 45% |
| **Margin** | $2,378 | $2,378 | 100% |
| | | | |
| **TOTAL** | **$31,498** | **$19,468** | **61.8%** |

### 5.3 Local Content by Value Category

```
LOCAL CONTENT BREAKDOWN — VN-TGT-SEA-001-H (Material Selections)
=================================================================

Vietnamese sources (100% local):
  Hull (HDPE + foam + labor)        $4,000   ████████████████████  100%
  Steel frame + masts (material)    $  550   ████████████████████  100%
  Steel processing (HDG, welding)   $1,050   ████████████████████  100%
  CNC face plate machining          $  600   ████████████████████  100%
  Anodize (face plates)             $  300   ████████████████████  100%
  Reflector assembly labor          $1,000   ████████████████████  100%
  Danforth anchor                   $  350   ████████████████████  100%
  Final assembly + QC               $3,700   ████████████████████  100%
  Margin                            $2,378   ████████████████████  100%

Partially local (30-50% local):
  Mooring chain/rode/accessories    $  850   ██████████            ~43%
  Tow hardware                      $  400   ██████████            50%

Import / ASEAN (0% local):
  6061-T6 Al sheet                  $  680   ░░░░░░░░░░░░░░░░░░░░  0%
  AlSi10Mg LPBF frames             $7,600   ░░░░░░░░░░░░░░░░░░░░  0%
  AM frame post-processing          $1,200   ░░░░░░░░░░░░░░░░░░░░  0%
  GPS beacon (COTS)                 $1,800   ░░░░░░░░░░░░░░░░░░░░  0%

TOTAL LOCAL CONTENT:  $19,468 / $31,498 = 61.8%
```

### 5.4 Path to 85-90% Local Content Target

The current 61.8% local content falls short of the 85-90% target (PRD-002: ≥85%). The gap is driven primarily by the AM reflector frames ($8,800 imported from ASEAN = 28% of total value). Strategies to close the gap:

| Strategy | Local Content Gain | Feasibility | Timeline |
|----------|-------------------|-------------|----------|
| **A: Develop Vietnamese LPBF capability** | +$8,800 → pushes local to ~90% | LOW — no Vietnamese LPBF bureau for AlSi10Mg at required quality | 2-3 years |
| **B: Switch to Concept A-CNC (6061-T6 CNC frames)** | +$4,800 (frames made locally) → local ~78% | HIGH — proven CNC technology, VN shops capable | Immediate |
| **C: Classify ASEAN AM as "regional local"** | +$8,800 → local ~90% if ASEAN = local | MEDIUM — depends on procurement policy interpretation | Policy decision |
| **D: Increase Vietnamese value-add on imported materials** | +$500-1,000 from local Al sheet processing | MEDIUM — find VN aluminum distributor/processor | 6-12 months |

**Recommendation:** Pursue Strategy B (CNC fallback) as baseline to ensure ≥78% local content meets a relaxed threshold, while simultaneously pursuing Strategy C (ASEAN classification as regional-local). If ASEAN AM is classified as regional-local under Vietnamese defense procurement rules (similar to ASEAN trade agreements for defense offset), the 85-90% target is met. This is a procurement policy question to be resolved with Stakeholder S-06 (Procurement).

**Note:** Even at 61.8% local content, the THANH TRI-H represents a massive improvement over the alternative (importing complete target systems at 0% local content). The 61.8% figure may satisfy the PRD-002 requirement if the procurement authority accepts ASEAN-sourced AM as a transitional step toward full Vietnamese AM capability.

---

## 6. Final Material Selections

### 6.1 Consolidated Selection Table

| # | Component Group | Selected Material | Grade / Specification | Source | Processing | Protection | Cost/Unit | Req. Traceability |
|---|-----------------|-------------------|-----------------------|--------|-----------|------------|-----------|-------------------|
| 1 | **Hull** | HDPE | PE100, carbon-black stabilized, 8-12 mm wall | Vietnam (Binh Minh, Tan Dai Hung) | Rotomolding or thermoplastic welding (2-section) | None required (inherent UV/salt resistance) | $4,000 | MAT-001, GEO-001, GEO-002, SAF-004 |
| 2 | **Foam fill** | Closed-cell PU rigid foam | 32-48 kg/m³, marine grade, pour-in-place | Vietnam (local polyurethane supplier) | Pour-in-place into hull cavity | Sealed within hull; no external exposure | $800 | MAT-002, SAF-007 |
| 3 | **Structural frame** | Mild steel, HDG | S235JR per EN 10025 (or Q235B equivalent) | Vietnam (Hoa Phat, Nam Kim) | Cut, form, MIG/MAG weld, then HDG | Hot-dip galvanize ≥85 µm per ASTM A123 | $1,200 | MAT-005, FOR-009, ASM-005 |
| 4 | **Mast tubes (8x)** | Mild steel tube, HDG | 60 mm OD x 4 mm wall, S235JR | Vietnam (Hoa Phat seamless/welded tube) | Cut to length, weld base plates/top plates | Hot-dip galvanize ≥85 µm per ASTM A123 | $800 | MAT-010, FOR-011, GEO-010 |
| 5 | **Reflector face plates (24x)** | Aluminum alloy | 6061-T6, 3 mm sheet per ASTM B209 | Import (Korea/Japan/China) | CNC fly-cut, drill, deburr at VN CNC shop | Type II anodize ≥10 µm per MIL-A-8625 | $1,780 | MAT-003, MAT-007, MAT-008, SIG-001 |
| 6 | **Reflector frames (8x)** | Aluminum alloy (AM) | AlSi10Mg, LPBF + T5 per ASTM F3318 | ASEAN AM bureau (Xometry SG, Facfox CN) | LPBF print → T5 heat treat → CNC datum surfaces | Type III hard anodize ≥25 µm per MIL-A-8625 | $9,600 | MAT-004, MAT-009, SIG-009 |
| 7 | **Mooring chain** | G30 proof coil, HDG | 19 mm (or 16 mm G30 per catenary analysis) | Vietnam (marine chandler, port supply) | As-supplied; cut to length on site | Hot-dip galvanize (factory applied) | $270 | MAT-006, FOR-006, OPR-005 |
| 8 | **Mooring rode** | Polyester braided rope | 20 mm, 3-strand or double-braid | Vietnam/ASEAN (marine rope supplier) | As-supplied; splice eyes on site | UV-stabilized (factory treated) | $250 | FOR-006, OPR-005 |
| 9 | **Anchor** | Danforth type, HDG steel | 50 kg, galvanized, marine grade | Vietnam (marine hardware supplier/foundry) | Cast + HDG (factory) | Hot-dip galvanize | $350 | FOR-007 |
| 10 | **Tow line** | Dyneema (HMPE) | 16 mm, 12-strand, SWL ≥8,000 kgf | Import/ASEAN (specialized marine rope) | As-supplied; soft eye + thimble termination | UV cover braid (factory applied) | $400 | FOR-008, TRA-004 |
| 11 | **GPS beacon** | COTS GNSS + Iridium | IP67/68, 72h Li-ion battery | Import (China/Taiwan/Japan) | As-supplied; battery swap before deployment | Waterproof enclosure (factory) | $1,800 | ENR-001, ENR-002, SIG-007 |

### 6.2 Material Compatibility Assessment

Galvanic corrosion risk at dissimilar metal interfaces:

| Interface | Material Pair | Galvanic Potential Difference | Risk Level | Mitigation |
|-----------|--------------|-------------------------------|------------|------------|
| IF-01: Hull ↔ Frame | HDPE ↔ HDG Steel | N/A (HDPE is non-conductive) | **NONE** | No isolation needed |
| IF-02: Frame ↔ Mooring | HDG Steel ↔ HDG Steel | 0 mV (same material) | **NONE** | Same HDG coating system |
| IF-03: Frame ↔ Masts | HDG Steel ↔ HDG Steel | 0 mV (same material) | **NONE** | Same HDG coating system |
| IF-04: Mast ↔ Reflector | HDG Steel ↔ Anodized Al | ~500-800 mV (Al anodic to steel) | **HIGH** | Nylon/HDPE isolation bushings at bolt holes; stainless steel fasteners with nylon washers; apply marine sealant (Sikaflex) at joint |
| IF-05: Face plates ↔ AM frame | 6061-T6 anodized ↔ AlSi10Mg anodized | ~50-100 mV (both Al alloys, similar potential) | **LOW** | Both anodized; minimal galvanic risk; use SS316 bolts with nylon isolation if needed |
| IF-06: Mooring ↔ Anchor | HDG chain ↔ HDG anchor | 0 mV | **NONE** | Same material system |

**Critical interface IF-04 (Mast ↔ Reflector):** The HDG steel to anodized aluminum junction requires explicit galvanic isolation. Specify:
- Nylon isolation bushings on all 4 mounting bolts
- HDPE or nylon flat washers under bolt heads and nuts
- Marine-grade polysulfide or polyurethane sealant (Sikaflex 291) at the steel-aluminum contact face
- SS316 A4-80 mounting bolts (passive in seawater, between the two metals galvanically)
- Inspection requirement: check isolation integrity at pre-deployment inspection (MNT-003)

---

## 7. Cross-References

### Phase 3 RISM Documents
- [[RISM_R1_requirements_identification.md]] — Step R1: 74 direct embodiment requirements extracted from 116 Phase 1 requirements
- [[RISM_I2_critical_requirements.md]] — Step I2: Critical requirements prioritization and sizing drivers
- [[RISM_S3_material_selection.md]] — Step S3: Material candidate screening (pre-screening for this M4 analysis)

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1), material requirements MAT-001 through MAT-010
- [[../01_requirements/standards_mapping.md]] — MIL-STD-810H (salt fog), MIL-A-8625 (anodize), ASTM A123 (HDG), ASTM F3318 (AM)

### Phase 2 Source Documents
- [[../02_conceptual/concept_selection.md]] — Concept A architecture, material assignments per subsystem layer, cost estimates
- [[../02_conceptual/morphological_matrix.md]] — Working principles with material candidates per function

### Project Management
- [[../PROJECT_STATUS.md]] — Project status tracker

---

**Document Status:** Draft v1.0 — Material selection matrices complete for all 5 component groups. Pending review items:
1. Final mooring chain size (16 mm vs 19 mm G30) — depends on catenary analysis (TBD-010/TBD-011)
2. Local content gap resolution strategy — requires S-06 Procurement input on ASEAN classification
3. Galvanic isolation detail at IF-04 (mast-reflector) — requires detailed interface drawing in layout step
