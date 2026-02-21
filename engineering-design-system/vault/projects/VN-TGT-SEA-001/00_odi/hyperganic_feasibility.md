---
project: VN-TGT-SEA-001
phase: 0
type: feasibility_study
version: 2.1
created: 2026-02-09
updated: 2026-02-10
revision: B.1
status: reference
---

# Hyperganic / Additive Manufacturing Feasibility Study

> **Rev B.1 STATUS:** This document is retained as **reference only**. Key changes:
> - **TPMS flotation core (Section 1):** REMOVED — user directive. Expendable target, no ballistic survivability.
> - **Schwarz P IR panels (Section 4):** REMOVED — Rev B (radar-only target, no IR signature).
> - **AM corner reflectors (Section 3):** ACTIVE but revised — now 0.8m edge, hybrid CNC faces + AM AlSi10Mg frames (not full AM monolith). See [[phase0_final_revision.md]].
> - **Phase H0 ballistic test (Section 6):** ELIMINATED — no TPMS to test.
> - **Platform:** 8.0m diameter (was 6.0m). Superstructure REMOVED. Reflectors at 3-4m on steel masts.

**Scope:** Technical feasibility of TPMS flotation core, AM corner reflectors, and Schwarz P IR panels
**Decision:** GO / NO-GO for $8K Phase H0 ballistic test

---

## 1. ~~TPMS Flotation Core~~ — REMOVED (Rev B)

> **REMOVED:** User directive — "no need Target survivability 7,200 hits to sink." Expendable target. HDPE hull with closed-cell foam fill provides adequate environmental buoyancy. See [[environmental_survivability.md]].

### 1.1 TPMS Geometry Selection

| TPMS Type | Cell Size | Wall Thickness | Porosity | Strength | Impact Resistance | Recommendation |
|-----------|----------|----------------|----------|----------|-------------------|----------------|
| **Gyroid** | 4-10 mm | 0.3-1.0 mm | 70-90% | Highest SEA (27.54 J/g) | Good | **PRIMARY — flotation core** |
| **Diamond** | 4-8 mm | 0.5-1.0 mm | 70-85% | Good | **Best under ballistic** | **SECONDARY — impact face** |
| **Schwarz P** | 4-8 mm | 0.5-1.0 mm | 71-82% | Moderate | Lower toughness | IR thermal channels only |
| **Voronoi** | 2-8 mm | 0.3-0.8 mm | 60-90% | Variable | Good (stochastic) | Alternative to Gyroid |

**Selected baseline for Phase H0 test block:**
- **Structure:** Gyroid TPMS
- **Cell size:** 8 mm (conservative, printable on all SLS machines)
- **Wall thickness:** 1.0 mm (conservative, ensures watertight cells)
- **Relative density:** 20% (balance of buoyancy + strength)
- **Block dimensions:** 500 x 300 x 300 mm (fits standard SLS build volume)

### 1.2 Material Selection for Flotation Core

| Material | Density (solid) | Eff. Density @ 20% RD | Buoyancy | Cost/cm³ | Marine Durability | **Verdict** |
|----------|----------------|----------------------|----------|---------|-------------------|-------------|
| **PA12 (SLS nylon)** | 1.03 g/cm³ | **0.21 g/cm³** | Excellent | $0.10-0.50 | Good (low water absorption 0.63%) | **BEST for flotation** |
| **AlSi10Mg (LPBF)** | 2.67 g/cm³ | **0.53 g/cm³** | Good | $3-8 | Moderate (needs anodize) | Backup — higher ballistic |
| **316L SS (LPBF)** | 8.00 g/cm³ | **1.60 g/cm³** | **SINKS** | $5-10 | Excellent | NOT suitable standalone |

**Decision: PA12 SLS for Phase H0 test.** Reasons:
1. Effective density 0.21 g/cm³ → massive buoyancy reserve (seawater = 1.025 g/cm³)
2. Cost 10-50x cheaper than metal LPBF → $500-2,500 per test block vs $13,500-36,000
3. Low water absorption (0.63% at 24h, 1.5% saturated) → suitable for marine
4. If PA12 survives ballistic test → cheapest path to production
5. If PA12 fails → upgrade to AlSi10Mg for ballistic face layer

### 1.3 Survivability Math — Refined

```
PA12 TPMS GYROID FLOTATION CORE
═══════════════════════════════════════════════════════

Block dimensions: 500 x 300 x 300 mm = 45,000 cm³
Cell size: 8 mm
Cells per cm³: ~2 (at 8mm cell size)
Total cells in block: ~90,000

12.7mm AP bullet damage zone:
  Entry: ~15mm diameter
  Through-block: ~20-25mm channel
  Cells intersected: ~8-12 per penetration

After 10 hits (12.7mm AP):
  Cells destroyed: 80-120
  Buoyancy loss: 120/90,000 = 0.13%
  Status: FLOATING (negligible loss)

After 50 hits:
  Cells destroyed: 400-600
  Buoyancy loss: 600/90,000 = 0.67%
  Status: FLOATING (trivial loss)

After 200 hits:
  Cells destroyed: 1,600-2,400
  Buoyancy loss: 2,400/90,000 = 2.67%
  Status: FLOATING (well within reserve)

Reserve buoyancy calculation:
  Block mass (PA12, 20% RD): 45,000 cm³ x 0.21 g/cm³ = 9,450 g = 9.45 kg
  Displaced seawater: 45,000 cm³ x 1.025 g/cm³ = 46,125 g = 46.1 kg
  Net buoyancy: 46.1 - 9.45 = 36.7 kg upward force
  Reserve buoyancy: 36.7/46.1 = 80%

  To sink (flood all cells): need >80% cells destroyed
  That requires: 0.80 x 90,000 / 10 cells/hit = ~7,200 hits

  VERDICT: PA12 TPMS block is practically unsinkable by small arms
```

### 1.4 Key Risk: Water Ingress Through Damaged Cells

**Concern:** Even sealed TPMS cells may allow water to wick between cells through cracks in thin walls.

**Mitigation strategies:**
1. **Thicker walls (1.0 mm vs 0.3 mm):** Reduces crack propagation between cells
2. **Hydrophobic coating:** Spray-on marine sealant on exterior surfaces
3. **Graded density:** Denser outer layer (30% RD, 0.8 mm walls) → lighter inner core (15% RD)
4. **Test protocol:** Weigh block before/after ballistic test + 24h soak to measure actual water ingress

**Phase H0 test will measure this directly.**

---

## 2. AM Process & Supply Chain

### 2.1 Process Selection

| Component | Recommended Process | Machine Class | Build Volume Required | Cost Estimate |
|-----------|-------------------|---------------|----------------------|--------------|
| **Flotation core (Phase H0 test)** | SLS (PA12 nylon) | HP MJF 5200 or EOS P396 | 500x300x300 mm | **$500-2,500** |
| **Flotation core (production)** | SLS (PA12) segmented | Same | 3-6 segments joined | $3,000-10,000 per full section |
| **Corner reflectors** | LPBF (AlSi10Mg) | EOS M290 or SLM 280 | 300x300x300 mm (each reflector) | **$800-1,500 each** |
| **Schwarz P IR panels** | LPBF (AlSi10Mg) | EOS M290 | 300x300x50 mm | **$2,000-4,000 each** |
| **Structural joints** | LPBF (AlSi10Mg) or WAAM (steel) | Various | <200mm each | $500-1,000 each |

### 2.2 Build Volume Strategy

**Problem:** Full-size flotation section (3m x 2m x 1m) vastly exceeds any AM machine build volume.

**Solution: Segmented printing + mechanical joining**

```
SEGMENTATION STRATEGY
═══════════════════════════════════════════

Full section: 3000 x 2000 x 1000 mm

Option A: 500 x 300 x 300 mm blocks (fits HP MJF 5200)
  Blocks needed: 6 x 7 x 3 = 126 blocks per section
  Join method: Epoxy bonding + mechanical clips
  Pro: Fits standard SLS machines; widely available
  Con: Many joints; assembly time

Option B: 400 x 400 x 400 mm blocks (fits EOS P770)
  Blocks needed: 8 x 5 x 3 = 120 blocks per section
  Join method: Epoxy bonding + mechanical clips
  Pro: Fewer joints; cubic shape easier to handle
  Con: Larger SLS machine needed

Option C: Larger segments via Eplus3D EP-M2050 (2050 x 2050 x 1100 mm)
  Segments needed: 2 x 1 x 1 = 2 halves per section
  Join method: Bolted flange
  Pro: Minimum joints
  Con: Only available from Eplus3D in China; EXTREMELY expensive in metal

RECOMMENDATION: Option A for Phase H0 (single 500x300x300 block)
               Option A or B for production (bonded block assembly)
```

### 2.3 ASEAN AM Service Bureau Options

| Bureau | Location | Capability | Lead Time | Cost Level | Notes |
|--------|----------|-----------|-----------|-----------|-------|
| **Xometry Asia** | Global/Asia sourcing | SLS, LPBF, all materials | 7-10 days standard | $$$ | Online quoting, traceable |
| **Additive3D Asia** | Singapore | Metal LPBF (AlSi10Mg, 316L) | 3-5 weeks | $$$ | ISO 9001 certified |
| **3D Matters** | Singapore | SLS, SLM, MJF | 3-5 weeks | $$$ | First SG AM company ISO certified |
| **Facfox** | China | LPBF up to 500x500x1000 mm | 2-4 weeks | $$ | Largest build volumes |
| **Eplus3D** | Hangzhou, China | EP-M650 (655x655x800 mm) | 2-4 weeks | $$ | 100+ super-meter machines |
| **JR Technology** | Shenzhen | 30+ industrial SLM machines | 2-3 weeks | $ | Cost-competitive |
| **ARRK Asia** | SG/TH/MY | Prototyping, 3D printing | 2-4 weeks | $$ | Multi-country presence |

**Phase H0 recommendation:** Xometry Asia or Chinese bureau (Facfox/JR Technology) for PA12 SLS block. Estimated $500-2,500 including shipping.

### 2.4 Cost Model

| Component | Qty | Unit Cost | Total | Process |
|-----------|-----|-----------|-------|---------|
| **Phase H0: Test block (PA12 SLS)** | 1 | $500-2,500 | **$500-2,500** | SLS |
| **Phase H1: AM reflectors (AlSi10Mg)** | 4 | $800-1,500 | **$3,200-6,000** | LPBF |
| **Phase H1: IR panel demo (AlSi10Mg)** | 1 | $2,000-4,000 | **$2,000-4,000** | LPBF |
| **Phase H2: Full flotation section segments** | 126 | $25-100 | **$3,150-12,600** | SLS |
| **Phase H2: Full reflector set (8 units)** | 8 | $800-1,500 | **$6,400-12,000** | LPBF |

**Total Hyperganic material cost (Phases H0-H2):** $15,250-37,100
**Budget allocated:** $48,000 (H0 $8K + H1 $15K + H2 $25K)
**Margin:** 23-69% → **Budget is feasible with comfortable margin**

---

## 3. AM Corner Reflectors — Technical Analysis (REVISED Rev B.1)

### 3.1 RCS Formulas & Design Targets

**Square trihedral corner reflector:**
```
sigma_max = (12 * pi * a^4) / lambda^2

At X-band (9.4 GHz, lambda = 0.032 m):

a = 0.3 m:  sigma = 3.0 m²   (4.8 dBsm)
a = 0.4 m:  sigma = 9.5 m²   (9.8 dBsm)
a = 0.5 m:  sigma = 23.2 m²  (13.7 dBsm)  ← BASELINE
a = 0.6 m:  sigma = 48.2 m²  (16.8 dBsm)
a = 0.8 m:  sigma = 152 m²   (21.8 dBsm)
```

**8 reflectors at 0.5m edge, 45 deg spacing:**
- Peak RCS per reflector: 23.2 m² (13.7 dBsm)
- Combined 360 deg: 250-350 m² (depending on overlap)
- Minimum between reflectors: ~10-15 m² (gap fill from adjacent reflectors)
- Variation through 360 deg: **<= +/- 2 dB** (with optimized angular offset)

> **Rev B.1:** Selected edge length increased to **a = 0.8 m** (152.3 m² per reflector, 8 reflectors = 1,218 m² peak). Manufacturing approach changed to **hybrid CNC face plates + AM mounting frames** (not full AM monolith). See [[phase0_final_revision.md]] Section 1.4.

### 3.2 Manufacturing Tolerance Impact

| Orthogonality Error | RCS Loss | AM Achievable? | Traditional Achievable? |
|---------------------|----------|----------------|------------------------|
| +/- 0.1 deg | < 0.5 dB | **YES** (LPBF) | Difficult |
| +/- 0.2 deg | 0.5-1.0 dB | YES | Very difficult |
| +/- 0.5 deg | 2-3 dB | YES | YES (good fabrication) |
| +/- 1.0 deg | 5-8 dB | N/A | YES (typical field) |
| +/- 2.0 deg | 10-15 dB | N/A | Common in ad-hoc targets |

**AM advantage:** LPBF aluminum achieves +/- 0.1 deg tolerance routinely, providing 5-15 dB improvement over traditional hand-fabricated reflectors. This translates directly to more reliable seeker acquisition.

> **Rev B.1:** At 0.8m edge, full AM monolith exceeds most LPBF build volumes. Hybrid approach: CNC 6061-T6 face plates (800×800×3mm) + AM AlSi10Mg mounting frame (~300×300×300mm, fits EOS M290). AM frame controls orthogonality (±0.1°). Cost: $1,200-2,000/reflector (vs $4,000-6,000 for full AM).

### 3.3 AM Reflector Design Features

| Feature | Traditional | AM-Printed | Benefit |
|---------|------------|-----------|---------|
| Plate angle | Hand-bent/welded | Printed as monolith | No assembly error |
| Mounting bracket | Separate, bolted | Integrated (printed) | No alignment drift |
| Weight (a=0.5m) | ~5 kg (solid Al) | ~3 kg (lattice backing) | 40% lighter |
| Surface finish | Ra 100+ um | Ra 6-15 um (LPBF) | Better reflectivity |
| Corrosion protection | Paint/galvanize | Anodize (Type III) | 5-10 year life |
| Modularity | Permanent installation | Bolt-on, field-swappable | Change RCS profile in 1 hour |

> **Rev B.1:** Weight per reflector increased to ~15 kg (3× CNC plates + AM frame). Reflectors mounted on 8× galvanized steel masts (60mm×4mm tube) at 3-4m above waterline for improved radar horizon and separation from sea clutter.

### 3.4 Reflector Material: AlSi10Mg (LPBF)

| Property | Value | Adequacy |
|----------|-------|----------|
| Yield strength | 230-345 MPa | Far exceeds structural needs |
| Density | 2.67 g/cm³ | Lightweight |
| Surface conductivity | Excellent (aluminum) | Required for RF reflection |
| Corrosion (seawater) | 0.1-0.3 mm/year unprotected | Needs anodize |
| Anodizing | Type III hard anodize, 10-50 um, 500+ HV | Excellent marine protection |
| LPBF surface quality | Ra 6-15 um | Adequate for X-band (lambda = 32mm) |
| LPBF vs cast corrosion | LPBF BETTER (finer Si particles) | Advantage over traditional |

---

## 4. ~~Schwarz P IR Thermal Panels~~ — REMOVED (Rev B)

> **REMOVED:** Rev B directive — radar-only target. No IR signature, no propane system. Entire IR subsystem eliminated.

### 4.1 Concept

Internal Schwarz P minimal surface channels distribute heat from a propane burner through an aluminum panel, creating a gradient temperature distribution that mimics a ship's exhaust pattern:
- Hot zone (funnel area): 200-250 deg C
- Warm zone (hull sides): 80-120 deg C
- Cool zone (waterline): 30-50 deg C

### 4.2 TRL Assessment

| Factor | Status | TRL |
|--------|--------|-----|
| Schwarz P geometry for heat exchange | Published academic research (extensive) | 5 |
| AM printing of Schwarz P in AlSi10Mg | Demonstrated in cooling applications | 5 |
| Application to IR signature simulation | **Novel — no published precedent** | **2-3** |
| Integration with propane burner | Straightforward engineering | 4 |
| IR band calibration (3-5 um MWIR) | Requires emissivity characterization | 3 |

### 4.3 Recommendation

**Defer to Phase H1.** The IR panel is the lowest-priority Hyperganic component:
- Base target already has propane burner providing 250 deg C IR signature
- Schwarz P enhancement improves REALISM but doesn't enable new capability
- Phase H0 and H1 should focus on TPMS survivability and RCS accuracy (the EXTREME opportunities)
- Schwarz P IR panel can be added as Phase H1 or H2 enhancement

---

## 5. Risk Matrix — Updated with Technical Data

| Risk | Probability | Impact | Mitigation | Data Source |
|------|-------------|--------|------------|-------------|
| PA12 TPMS block fails ballistic test (fragments, doesn't retain buoyancy) | **25%** (↓ from 30%) | HIGH | Test at 12.7mm first; thicker walls (1.0mm); if PA12 fails, try AlSi10Mg | Published: lattice structures localize damage; Gyroid SEA = 27.54 J/g |
| Water wicks through damaged cell walls | **35%** | MEDIUM | Hydrophobic coating; measure water ingress in test; graded density design | To be validated in Phase H0 |
| AM reflector RCS doesn't match simulation | **15%** (↓ from 20%) | MEDIUM | Published data confirms corner reflector RCS formula accuracy; AM tolerance achieves +/- 0.1 deg | Extensive published RCS measurement data |
| No SLS machine available for 500mm block | **10%** (↓ from 50%) | LOW | HP MJF 5200 (380mm) available at all major bureaus; Xometry, Facfox, Additive3D all offer SLS | Multiple verified ASEAN service bureaus |
| AM cost exceeds Phase H0 budget ($8K) | **15%** | LOW | PA12 SLS block estimated $500-2,500; leaves $5,500-7,500 for test + contingency | Cost data from service bureau pricing |
| Military customer rejects 3D-printed hardware | **50%** (unchanged) | HIGH | Live-fire demo video; cite GE Aviation, US Navy AM adoption; focus on PERFORMANCE DATA not process | Organizational, not technical risk |

**Overall technical risk: MODERATE-LOW.** Key risks have been reduced by research data.

> **Rev B.1:** TPMS risks (rows 1-2) ELIMINATED. AM reflector risk reduced (hybrid approach is lower-risk than full AM monolith). Military acceptance risk unchanged (50%). New risks: mast structural integrity in SS 5-6, reflector mount fatigue (37,000 wave cycles over 72h).

---

## 6. ~~Phase H0 Test Protocol~~ — ELIMINATED (Rev B)

> **ELIMINATED:** No TPMS = no ballistic test needed. Budget reallocated to storm mooring sea trial ($5K) and AM reflector RCS validation ($15K).

### 6.1 Test Article

| Parameter | Specification |
|-----------|--------------|
| Material | PA12 (SLS nylon) |
| Structure | Gyroid TPMS |
| Cell size | 8 mm |
| Wall thickness | 1.0 mm |
| Relative density | 20% |
| Dimensions | 500 x 300 x 300 mm |
| Weight (calculated) | 9.45 kg |
| Estimated cost | $500-2,500 (SLS printing) |

### 6.2 Test Sequence

| Step | Action | Measurement | Pass Criteria |
|------|--------|-------------|---------------|
| 1 | Weigh dry block | Mass (kg) | Record baseline |
| 2 | Submerge in tank, measure buoyancy | Buoyancy force (N) | > 300 N (calc: 360 N) |
| 3 | Fire 10 rounds 12.7mm AP at block | Count penetrations | All penetrate (expected) |
| 4 | Remove from water, photograph damage | Damage zone diameter per hit | Record |
| 5 | Re-submerge, measure buoyancy | Buoyancy force (N) | > 285 N (< 5% loss) |
| 6 | Soak 24 hours submerged | Weight gain (kg) | < 2 kg water absorption |
| 7 | Re-measure buoyancy after 24h soak | Buoyancy force (N) | > 250 N (< 15% loss) |
| 8 | Fire 10 more rounds (total 20) | Cumulative damage | Record |
| 9 | Final buoyancy test | Buoyancy force (N) | > 200 N (still floating) |
| 10 | Photograph, document, video entire process | All data | 4K video for demo |

### 6.3 Decision Gate

| Result | Decision |
|--------|----------|
| Block floats after 20 hits with <15% buoyancy loss | **GO Phase H1** — proceed with full reflector + flotation development |
| Block floats after 20 hits with 15-30% buoyancy loss | **CONDITIONAL GO** — redesign with thicker walls or hydrophobic coating |
| Block sinks after 20 hits | **REDESIGN** — try AlSi10Mg metal TPMS, or graded density, or hybrid design |
| Block shatters on first hit (catastrophic) | **PIVOT** — PA12 not suitable; evaluate metal-only approach |

### 6.4 Budget Breakdown (Phase H0: $8,000)

| Item | Cost | Notes |
|------|------|-------|
| nTop software license (1 year) | $2,000 | TPMS design tool |
| SLS printing (PA12, 500x300x300mm) | $500-2,500 | Xometry or Chinese bureau |
| Shipping (international) | $200-500 | Express courier |
| Range time (12.7mm, 20 rounds) | $500-1,000 | Ammunition + range fee |
| Buoyancy test equipment | $200 | Scale, tank, weights |
| Video documentation | $0 | Smartphone |
| Contingency | $1,300-4,600 | |
| **TOTAL** | **$4,700-6,200** | **Well within $8K budget** |

---

## 7. Feasibility Verdict

> **Rev B.1 Verdict Update:** TPMS and Schwarz P removed. Only AM corner reflectors remain as Hyperganic component. Technology confidence increased to **95%** (hybrid CNC/AM is proven manufacturing approach). Hyperganic budget reduced from $68K to ~$30K (-56%). See [[environmental_survivability.md]] and [[phase0_final_revision.md]].

```
╔═════════════════════════════════════════════════════════════╗
║                    FEASIBILITY ASSESSMENT                     ║
╠═════════════════════════════════════════════════════════════╣
║                                                               ║
║  TPMS Flotation Core (PA12 SLS):                              ║
║  ├── Physics: VALIDATED (density 0.21 g/cm³ << seawater)      ║
║  ├── Printability: VALIDATED (0.3mm walls achievable)          ║
║  ├── Ballistic: PROBABLE (published lattice damage data)      ║
║  ├── Cost: VALIDATED ($500-2,500 per test block)              ║
║  ├── Supply chain: VALIDATED (multiple ASEAN bureaus)         ║
║  └── Status: ████████░░ 80% confident → TEST to confirm      ║
║                                                               ║
║  AM Corner Reflectors (AlSi10Mg LPBF):                       ║
║  ├── Physics: VALIDATED (RCS formula well-established)        ║
║  ├── Tolerance: VALIDATED (±0.1° achievable via LPBF)         ║
║  ├── Cost: VALIDATED ($800-1,500 per reflector)               ║
║  ├── Marine: VALIDATED (anodize for seawater service)         ║
║  └── Status: █████████░ 90% confident                         ║
║                                                               ║
║  Schwarz P IR Panels (AlSi10Mg LPBF):                         ║
║  ├── Physics: PLAUSIBLE (thermal channel design proven)       ║
║  ├── Application: NOVEL (no precedent in targets)             ║
║  ├── Priority: LOW (base IR burner already adequate)          ║
║  └── Status: █████░░░░░ 50% confident → defer to Phase H1    ║
║                                                               ║
║  ══════════════════════════════════════════════════════════  ║
║                                                               ║
║  OVERALL: TECHNICALLY FEASIBLE                                ║
║  RECOMMENDATION: APPROVE Phase H0 ($8K ballistic test)        ║
║  Risk: $5-6K actual spend. Upside: validates "unsinkable"     ║
║  claim that underpins entire product value proposition.        ║
║                                                               ║
╚═════════════════════════════════════════════════════════════╝
```

---

## Cross-References

- [[odi_analysis.md]] - ODI analysis (opportunity scores driving this feasibility study)
- [[re_competitive_analysis.md]] - Competitive analysis
- [[re_deep_analysis.md]] - Deep RE analysis (competitor subsystem details)
- [[../00_project_brief.md]] - Project brief
