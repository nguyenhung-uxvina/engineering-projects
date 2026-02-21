---
project: VN-CUA-001
designation: VDC-100
type: embodiment_RISM
phase: 3
steps: R-I-S-M
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz 15-Step RISM-PRAD-DECS-OCP
selected_concept: VDC-100 Enhanced (Concept B, 85.8%)
---

# VN-CUA-001: RISM — REQUIREMENTS & MATERIAL FOUNDATION
## Vietnamese Drone Catcher 100 (VDC-100 Enhanced)
## Nền tảng Yêu cầu & Vật liệu - Giai đoạn 3, Bước R-I-S-M

**Project Code:** VN-CUA-001
**Phase:** 3 - Embodiment Design (Steps R, I, S, M)
**Date:** 2026-02-08
**Input:** [[02_conceptual/concept_selection|Selected Concept B: VDC-100 Enhanced (85.8%)]]

---

# STEP R: REQUIREMENTS IDENTIFICATION

## R.1 Purpose

Extract and organize all embodiment-determining requirements from Phase 1 that constrain physical form, dimensions, materials, and manufacturing. These requirements drive every subsequent embodiment decision.

## R.2 Embodiment-Determining Requirements

### R.2.1 Geometric (Size & Space)

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-GEO-01 | System weight (loaded) | ≤8 kg | Hard limit | D | Operator patrol | Material density, wall thickness |
| CUA-GEO-02 | Overall length | ≤1200mm | ±20mm | D | Transport/handling | Barrel + stock proportioning |
| CUA-GEO-03 | Barrel bore diameter | 100mm | +0.5/-0mm | D | Projectile fit | Barrel machining tolerance |
| CUA-GEO-04 | Barrel outer diameter | ≤120mm | — | D | Grip, portability | Wall thickness → pressure rating |
| CUA-GEO-05 | Collapsed length | ≤800mm | — | W | Transport case | Folding stock design option |
| CUA-GEO-06 | Projectile length | ≤200mm | ±2mm | D | Net + chute volume | Projectile body design |

### R.2.2 Kinematic (Motion & Speed)

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-KIN-01 | Muzzle velocity | 50-70 m/s | ±5 m/s | D | Range achievement | Barrel length, pressure regulation |
| CUA-KIN-02 | Effective range | ≥80m | — | D | O-46: 13.5 | Projectile aerodynamics, fin design |
| CUA-KIN-04 | Net deployment reliability | ≥98% | — | D | O-43: 13.5 | Timer + barometric mechanism |
| CUA-KIN-06 | First-shot hit (stationary 50m) | ≥70% | — | D | O-48: 15.0 | Reticle calibration, barrel straightness |
| CUA-KIN-07 | First-shot hit (moving 10m/s 50m) | ≥50% | — | D | O-48: 15.0 | Lead marks, fin stabilization |

### R.2.3 Force & Load

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-FOR-01 | Trigger force | 20-40 N | ±5 N | D | Ergonomics | Trigger spring selection |
| CUA-FOR-02 | Recoil impulse | ≤15 Ns | — | D | Shoulder comfort | Recoil pad thickness, mass distribution |
| CUA-FOR-03 | Operating pressure | 100 bar (regulated) | ±5 bar | D | Propulsion | Regulator spec, seal design |
| CUA-FOR-04 | Storage pressure | 300 bar | — | D | Cylinder rating | DOT-3AL certified vessel |
| CUA-FOR-05 | Drop survival | 1m onto concrete | — | D | MIL-STD-810H 516 | Corner protection, material toughness |

### R.2.4 Environmental

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-OPR-01 | Operating temperature | -10°C to +55°C | — | D | MIL-STD-810H 501/502 | Material brittleness, seal swelling |
| CUA-OPR-02 | Humidity | 95% RH | — | D | MIL-STD-810H 507 | Corrosion protection, conformal coat |
| CUA-OPR-03 | Rain operation | Light rain (~10mm/hr) | — | D | MIL-STD-810H 506 | IP rating, sealing, drainage |
| CUA-OPR-04 | Sand/dust | Blowing dust | — | D | MIL-STD-810H 510 | Seal design, barrel protection |
| CUA-OPR-05 | Altitude | ≤3000m ASL | — | W | MIL-STD-810H 500 | Pressure vessel rating |
| CUA-TRA-01 | Storage temperature | -40°C to +70°C | — | D | Transport/storage | Material selection (no brittle failure) |

### R.2.5 Safety

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-SAF-01 | Arm/safe mechanism | Positive mechanical interlock | — | D | MIL-STD-882E | Safety lever, mechanical block |
| CUA-SAF-02 | Over-pressure protection | Relief valve @ 350 bar | — | D | DOT-3AL / TCVN 6153 | Relief valve in gas system |
| CUA-SAF-03 | Muzzle safety | Obstruction detection | — | D | MIL-STD-882E | Physical interlock or sensor |
| CUA-SAF-04 | Laser safety | Class 1 (IEC 60825) | — | D | Eye safety | COTS LRF module selection |
| CUA-SAF-05 | Drop safety | No discharge on drop | — | D | MIL-STD-882E | Inertia lock in trigger |

### R.2.6 Signal & Information

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-SIG-01 | Laser rangefinder range | 5-150m | — | D | O-12: 11.5 | LRF module selection |
| CUA-SIG-02 | Range accuracy | ±1m | — | D | O-48: 15.0 | LRF specification |
| CUA-SIG-03 | Ballistic reticle | Range marks 20/40/60/80/100m | — | D | O-48: 15.0 | Etched glass design |
| CUA-SIG-04 | Display brightness | ≥1000 nits | — | D | Sunlight readable | LCD module selection |
| CUA-SIG-06 | Safety status LED | Red=Armed, Green=Safe | — | D | MIL-STD-1472G | LED + circuit in scope |
| CUA-SIG-07 | Training mode indicator | Distinct visual/audible | — | W | Training safety | Mode switch design |

### R.2.7 Assembly & Maintenance

| Req ID | Requirement | Value | Tolerance | D/W | Source | Impact on Embodiment |
|--------|-------------|-------|-----------|-----|--------|---------------------|
| CUA-ASM-01 | Field strip without tools | — | — | D | Maintenance | Quick-release, captive fasteners |
| CUA-ASM-02 | Reload time | ≤8 sec | — | D | O-55: 12.5 | Breech design, ergonomics |
| CUA-ASM-04 | Total part count | ≤80 | — | W | Simplicity | Part consolidation |
| CUA-ASM-05 | Ready from standby | ≤5 sec | — | D | O-19: 12.5 | Safety toggle, arm sequence |
| CUA-MNT-01 | Standard tools only | Hex keys | — | D | Field maintenance | M4/M6 fasteners only |
| CUA-MNT-04 | Spare parts availability | 10-year guarantee | — | W | Lifecycle | Standard materials/parts |

## R.3 Requirements Summary

| Category | Count | Critical (D) | Wish (W) | Top ODI Outcome |
|----------|-------|--------------|----------|-----------------|
| Geometric | 6 | 5 | 1 | — |
| Kinematic | 5 | 5 | 0 | O-48: 15.0 |
| Force & Load | 5 | 5 | 0 | — |
| Environmental | 6 | 5 | 1 | — |
| Safety | 5 | 5 | 0 | — |
| Signal/Info | 6 | 5 | 1 | O-48: 15.0 |
| Assembly/Maintenance | 6 | 4 | 2 | O-55: 12.5 |
| **TOTAL** | **39** | **34 (87%)** | **5 (13%)** | |

**39 embodiment-determining requirements** extracted from 89 total Phase 1 requirements.

---

# STEP I: IDENTIFY CRITICAL REQUIREMENTS

## I.1 Purpose

Prioritize requirements by constraint strength and identify conflicts that must be resolved before layout design begins.

## I.2 Constraint Hierarchy

### Hard Constraints (MUST — Non-Negotiable)

| Priority | Requirement | Value | Rationale |
|----------|-------------|-------|-----------|
| **H1** | Weight ≤8 kg | CUA-GEO-01 | Operator cannot patrol with heavier system |
| **H2** | Operating pressure 100 bar | CUA-FOR-03 | Physics: required for 60 m/s muzzle velocity |
| **H3** | Storage pressure 300 bar | CUA-FOR-04 | DOT-3AL cylinder rating — certified vessel |
| **H4** | Safety interlock | CUA-SAF-01 | Regulatory / MIL-STD-882E mandatory |
| **H5** | Relief valve @ 350 bar | CUA-SAF-02 | Catastrophic failure prevention |
| **H6** | Bore diameter 100mm | CUA-GEO-03 | Projectile compatibility — defines barrel |
| **H7** | Class 1 laser | CUA-SAF-04 | Eye safety — non-negotiable |
| **H8** | Drop survival 1m | CUA-FOR-05 | Field use reality — will be dropped |

### Soft Constraints (WISH — Trade-off Space)

| Priority | Requirement | Value | Trade-off Available |
|----------|-------------|-------|---------------------|
| S1 | Part count ≤80 | CUA-ASM-04 | Can accept 85-90 if accuracy improves |
| S2 | Collapsed length ≤800mm | CUA-GEO-05 | Folding stock adds complexity |
| S3 | Training mode | CUA-SIG-07 | Can be firmware, not mechanical |
| S4 | Night vision compat | CUA-SIG-05 | Future upgrade path acceptable |
| S5 | Altitude 3000m | CUA-OPR-05 | Vietnam terrain mostly <1500m |

## I.3 Conflict Identification

| Conflict | Requirements | Nature | Resolution Strategy |
|----------|-------------|--------|---------------------|
| **CF-E1** | Weight ≤8 kg vs. Range ≥80m | Heavier barrel = better accuracy at range, but adds weight | Optimize barrel wall thickness (3× SF minimum), use Al 6061-T6 |
| **CF-E2** | Weight ≤8 kg vs. 5 shots/fill | Larger cylinder = more shots but heavier | 0.5L cylinder (1.2 kg) provides ≥5 shots with 100 bar regulation |
| **CF-E3** | Cost target vs. Fin stabilization | Fins add $15/projectile but improve accuracy | Justified by O-48 (15.0) — accuracy is #1 customer priority |
| **CF-E4** | Simplicity (72 parts) vs. Dual deploy | Barometric backup adds 3 components per projectile | Trade-off accepted — O-43 (13.5) and O-63 (13.0) justify complexity |
| **CF-E5** | Drop survival vs. Light weight | Thick walls survive drops but add weight | Corner bumpers (polymer) + optimized wall thickness |

## I.4 ODI-Weighted Priority Map

Mapping critical requirements to ODI outcomes for design priority:

```
ODI-WEIGHTED EMBODIMENT PRIORITIES
═══════════════════════════════════════════════════════════════════════════════

ODI Score    Requirement Group               Design Priority
─────────    ───────────────────────────     ──────────────────
O-48: 15.0   First-shot hit accuracy         ████████████████████ TOP
             → Barrel straightness, reticle
             → Fin stabilization, LRF

O-23: 14.6   Equipment reliability           ██████████████████  HIGH
             → Mechanical fire chain
             → Pressure regulation ±3%

O-46: 13.5   Effective range                 █████████████████   HIGH
             → Muzzle velocity 60 m/s
             → Barrel length 800mm

O-43: 13.5   Net deployment reliability      █████████████████   HIGH
             → Timer + barometric dual
             → Deploy mechanism design

O-63: 13.0   Evidence preservation           ████████████████    HIGH
             → Parachute + drogue
             → Descent rate ≤5 m/s

O-55: 12.5   Reload speed                    ███████████████     MEDIUM-HIGH
             → Breech design
             → Ergonomic chamber access

─────────    ─── DESIGN ATTENTION LINE ───   ──────────────────

O-24: 12.0   Weight/portability              ██████████████      MEDIUM
             → Material selection
             → Part consolidation

═══════════════════════════════════════════════════════════════════════════════
```

---

# STEP S: SELECT PRELIMINARY MATERIALS

## S.1 Purpose

Narrow material candidates early to guide form development. Screen by hard constraints (environmental, mechanical, manufacturing).

## S.2 Environmental Screening

Vietnam tropical environment imposes these constraints:

| Factor | Value | Severity | Material Implication |
|--------|-------|----------|---------------------|
| Temperature range | -10°C to +55°C operating | HIGH | No brittle materials at -10°C, no creep at 55°C |
| Storage temperature | -40°C to +70°C | MEDIUM | Polymers must survive -40°C without cracking |
| Humidity | 95% RH continuous | HIGH | Corrosion-resistant materials mandatory |
| Salt exposure | Coastal deployment | MEDIUM | Marine-grade or protected materials |
| UV exposure | Tropical sun | MEDIUM | UV-resistant polymers or coatings |
| Rain | Light rain operation | MEDIUM | Water-resistant finishes |

## S.3 Material Screening by Component

### Barrel — Screening

| Candidate | Yield (MPa) | Density (g/cm³) | Corrosion | Machinability | Local? | Pass? |
|-----------|-------------|-----------------|-----------|---------------|--------|-------|
| **Al 6061-T6** | 276 | 2.70 | Good (anodize) | Excellent | ✅ | **YES** |
| **Al 7075-T6** | 503 | 2.81 | Fair (needs coat) | Good | ⚠️ | **YES** |
| SS 304 | 205 | 8.00 | Excellent | Fair | ✅ | NO (too heavy) |
| SS 316 | 205 | 8.00 | Excellent | Fair | ✅ | NO (too heavy) |
| Carbon fiber tube | 600+ | 1.55 | Excellent | Special | ❌ | NO (cost, no local) |
| Ti-6Al-4V | 880 | 4.43 | Excellent | Poor | ❌ | NO (cost, no local) |

**Decision:** Al 6061-T6 (primary) and Al 7075-T6 (backup if higher strength needed).

**Barrel wall thickness check:**
- Bore pressure: 100 bar = 10 MPa
- Barrel ID: 100mm, Wall: 5mm → OD: 110mm
- Hoop stress: σ = P × r / t = 10 × 50 / 5 = 100 MPa
- Safety factor: 276 / 100 = **2.76×** (acceptable, >2.5× target)
- With 7075-T6: 503 / 100 = **5.03×** (over-designed, not needed)

### Receiver — Screening

| Candidate | Yield (MPa) | Density (g/cm³) | Corrosion | Machinability | Local? | Pass? |
|-----------|-------------|-----------------|-----------|---------------|--------|-------|
| **Al 6061-T6** | 276 | 2.70 | Good (anodize) | Excellent | ✅ | **YES** |
| PA66-GF30 | 80 (injection) | 1.35 | Excellent | N/A (molded) | ✅ | **YES** (if loads OK) |
| Al 7075-T6 | 503 | 2.81 | Fair | Good | ⚠️ | YES (overkill) |

**Decision:** Al 6061-T6 — receiver carries recoil and barrel loads; polymer may be insufficient for 15 Ns recoil impulse and 300-bar gas line connections.

### Stock — Screening

| Candidate | Yield (MPa) | Density (g/cm³) | Corrosion | Process | Local? | Pass? |
|-----------|-------------|-----------------|-----------|---------|--------|-------|
| **PA66-GF30** | 80 | 1.35 | Excellent | Injection mold | ✅ | **YES** |
| ABS | 40 | 1.05 | Excellent | Injection mold | ✅ | YES (weaker) |
| Al 6061-T6 | 276 | 2.70 | Good | CNC | ✅ | YES (heavy) |
| Wood (teak) | 50 | 0.65 | Fair | Carving | ✅ | NO (inconsistent) |

**Decision:** PA66-GF30 (glass-filled nylon) — optimal strength-to-weight, corrosion-proof, injection moldable locally.

### Trigger/Safety Mechanism — Screening

| Candidate | Hardness (HRC) | Corrosion | Fatigue Life | Local? | Pass? |
|-----------|----------------|-----------|-------------|--------|-------|
| **17-4 PH SS (H900)** | 44 | Excellent | Excellent | ✅ | **YES** |
| SS 316 | 25 (max) | Excellent | Good | ✅ | YES (soft) |
| 4140 alloy steel | 50+ | Poor | Excellent | ✅ | NO (corrosion) |

**Decision:** 17-4 PH stainless steel, H900 condition — hardness + corrosion resistance for 10,000+ cycle trigger mechanism.

### Seals — Screening

| Candidate | Temp Range | Chemical | Compression Set | Cost | Pass? |
|-----------|-----------|----------|-----------------|------|-------|
| NBR (Nitrile) | -30 to +100°C | Good | Fair | Low | YES (marginal cold) |
| **EPDM** | -50 to +150°C | Excellent | Good | Low | **YES** |
| FKM (Viton) | -20 to +200°C | Excellent | Excellent | High | NO (cost, cold limit) |
| Silicone | -60 to +200°C | Good | Poor | Medium | NO (poor compression) |

**Decision:** EPDM — widest operating range covering -40°C storage to +55°C operation, excellent water/humidity resistance.

### Fasteners — Screening

| Candidate | Corrosion | Strength | Local? | Pass? |
|-----------|-----------|----------|--------|-------|
| Zinc-plated carbon steel | Fair (will rust) | High | ✅ | NO (humidity) |
| **SS 316** | Excellent | Medium (A4-80) | ✅ | **YES** |
| SS 304 | Good | Medium (A2-70) | ✅ | YES (316 preferred) |
| Titanium | Excellent | High | ❌ | NO (cost, no local) |

**Decision:** SS 316 — excellent corrosion resistance in tropical humidity, locally available.

## S.4 Preliminary Material Short List

| Component Group | Primary Material | Backup Material | Spec |
|----------------|-----------------|-----------------|------|
| Barrel | Al 6061-T6 | Al 7075-T6 | AMS 4027 |
| Receiver | Al 6061-T6 | Al 7075-T6 | AMS 4027 |
| Stock | PA66-GF30 | PA6-GF30 | — |
| Trigger/safety parts | 17-4 PH SS (H900) | SS 316 | AMS 5643 |
| Springs | SS 302 | SS 316 | ASTM A313 |
| Fasteners | SS 316 | SS 304 | ASTM A193 B8M |
| Seals | EPDM 70A | NBR 70A | AS568 sizes |
| HPA cylinder | Al + CF wrap | Al (no wrap) | DOT-3AL |
| Projectile body | ABS or PP | PA66 | — |
| Net | UHMWPE (Dyneema) | Nylon 6 | — |
| Parachute | Ripstop nylon | Polyester | — |

---

# STEP M: MATERIAL ANALYSIS

## M.1 Purpose

Detailed analysis of short-listed materials: properties, cost, lifecycle, and Vietnamese supply chain.

## M.2 Primary Material: Al 6061-T6

### M.2.1 Property Sheet

| Property | Value | Unit | Test Standard |
|----------|-------|------|---------------|
| Tensile yield strength | 276 | MPa | ASTM B557 |
| Ultimate tensile strength | 310 | MPa | ASTM B557 |
| Elongation at break | 12 | % | ASTM B557 |
| Hardness | 95 | HB | ASTM E10 |
| Density | 2.70 | g/cm³ | — |
| Thermal conductivity | 167 | W/m·K | — |
| CTE | 23.6 | μm/m·°C | — |
| Fatigue limit (10⁷ cycles) | 96 | MPa | — |
| Elastic modulus | 68.9 | GPa | — |
| Poisson's ratio | 0.33 | — | — |
| Melting point | 582-652 | °C | — |

### M.2.2 Corrosion Performance

| Environment | Corrosion Rate | With Type III Anodize | With Type II + Powder Coat |
|-------------|---------------|----------------------|---------------------------|
| Urban (Vietnam, inland) | 5 μm/year | <0.1 μm/year | <0.1 μm/year |
| Coastal (salt spray) | 20 μm/year | <1 μm/year | <0.5 μm/year |
| Tropical humidity (95% RH) | 10 μm/year | <0.5 μm/year | <0.2 μm/year |

**Barrel protection:** Type III hard anodize (50μm) — wear-resistant + corrosion barrier
**Receiver protection:** Type II anodize (20μm) + powder coat — cosmetic + corrosion

### M.2.3 Vietnamese Supply

| Supplier | Grade Available | Form | Price ($/kg) | MOQ | Lead Time |
|----------|----------------|------|-------------|-----|-----------|
| Hòa Phát Aluminum | 6061-T6 | Plate, bar, tube | $4.50 | 100 kg | 2 weeks |
| VNALUMINIUM | 6061-T6 | Extrusion profiles | $5.00 | 50 kg | 3 weeks |
| Import (China) | 6061-T6 | All forms | $3.50 | 200 kg | 4-6 weeks |

### M.2.4 Cost per Component

| Component | Raw Mass (kg) | Finish Mass (kg) | Material Cost | Machining Cost | Total |
|-----------|---------------|-------------------|---------------|----------------|-------|
| Barrel | 3.2 | 1.8 | $14.40 | $80.00 | $94.40 |
| Receiver | 2.5 | 0.9 | $11.25 | $120.00 | $131.25 |
| Muzzle brake | 0.5 | 0.3 | $2.25 | $30.00 | $32.25 |
| Scope housing | 0.8 | 0.4 | $3.60 | $50.00 | $53.60 |
| **Subtotal** | **7.0** | **3.4** | **$31.50** | **$280.00** | **$311.50** |

**Material utilization:** 3.4 / 7.0 = 49% (typical for CNC machining; chips recyclable)

## M.3 Secondary Material: PA66-GF30

### M.3.1 Property Sheet

| Property | Value | Unit | Notes |
|----------|-------|------|-------|
| Tensile strength | 80 | MPa | Glass-fiber reinforced |
| Flexural modulus | 6,500 | MPa | Good stiffness |
| Impact strength (Charpy) | 12 | kJ/m² | Adequate |
| Density | 1.35 | g/cm³ | 50% lighter than aluminum |
| Heat deflection (1.8 MPa) | 250 | °C | Well above operating range |
| Water absorption (24h) | 0.6 | % | Low — acceptable |
| UV resistance | Good | — | With carbon black pigment |
| Mold shrinkage | 0.5 | % | Predictable, manageable |

### M.3.2 Injection Molding Parameters

| Parameter | Value |
|-----------|-------|
| Mold temperature | 80-90°C |
| Melt temperature | 275-290°C |
| Injection pressure | 80-120 MPa |
| Cycle time | 30-45 sec |
| Tooling cost (stock mold) | ~$8,000 |
| Amortization (100 units) | $80/unit |
| Amortization (500 units) | $16/unit |

## M.4 Tertiary Material: 17-4 PH SS (H900)

### M.4.1 Property Sheet

| Property | Value | Unit |
|----------|-------|------|
| Tensile yield strength | 1170 | MPa |
| Ultimate tensile strength | 1310 | MPa |
| Hardness | 44 | HRC |
| Density | 7.78 | g/cm³ |
| Fatigue limit (10⁷) | 520 | MPa |
| Corrosion resistance | Comparable to SS 304 | — |

### M.4.2 Application: Trigger Group

| Part | Mass (g) | Machining Time | Cost |
|------|----------|----------------|------|
| Trigger lever | 25 | 0.5 hr | $15 |
| Sear | 15 | 0.5 hr | $15 |
| Safety lever | 20 | 0.3 hr | $10 |
| Inertia block | 10 | 0.2 hr | $5 |
| **Total trigger group** | **70** | **1.5 hr** | **$45** |

**Lifecycle:** 10,000+ cycles at 20-40 N trigger force. Safety factor: 1170 / (40 × area factor) > 10×.

## M.5 Material Selection Summary Matrix

| Component | Material | Specification | Treatment | Supplier | $/unit | Local? |
|-----------|----------|---------------|-----------|----------|--------|--------|
| Barrel | Al 6061-T6 | AMS 4027 | Type III hard anodize 50μm | Hòa Phát | $94 | ✅ |
| Receiver | Al 6061-T6 | AMS 4027 | Type II anodize + powder coat | Hòa Phát | $131 | ✅ |
| Muzzle brake | Al 6061-T6 | AMS 4027 | Type III hard anodize | Hòa Phát | $32 | ✅ |
| Scope housing | Al 6061-T6 | AMS 4027 | Type II anodize | Hòa Phát | $54 | ✅ |
| Stock body | PA66-GF30 | — | Matte black, as-molded | Local molder | $80 | ✅ |
| Trigger group | 17-4 PH SS | AMS 5643 H900 | Passivated | Local CNC | $45 | ✅ |
| Fasteners | SS 316 | ASTM A193 B8M | Passivated | Local | $30 | ✅ |
| Springs | SS 302 | ASTM A313 | None needed | Import | $20 | ❌ |
| Seals (all) | EPDM 70A | AS568 standard | None needed | Local | $10 | ✅ |
| HPA cylinder | Al + CF | DOT-3AL | Factory | Import (TW) | $150 | ❌ |
| Regulator | Mixed | — | — | Import | $60 | ❌ |
| LRF module | — | COTS | — | Import (CN) | $250 | ❌ |

## M.6 Galvanic Compatibility Analysis

| Junction | Material A | Material B | ΔV (galvanic) | Risk | Mitigation |
|----------|-----------|-----------|---------------|------|------------|
| Fastener → Barrel | SS 316 | Al 6061 anodized | 0.50V | ⚠️ MEDIUM | Nylon washer isolator between SS and Al |
| Fastener → Receiver | SS 316 | Al 6061 anodized | 0.50V | ⚠️ MEDIUM | Nylon washer isolator |
| Barrel → Receiver | Al 6061 | Al 6061 | 0.00V | ✅ NONE | Same material |
| Trigger → Receiver | 17-4 PH | Al 6061 | 0.35V | ⚠️ LOW | Trigger housed in polymer insert |
| Spring → Housing | SS 302 | Al 6061 | 0.45V | ⚠️ LOW | Spring pockets anodized; no standing water |
| Cylinder → Mount | Al CF-wrap | Al 6061 | 0.00V | ✅ NONE | Same base material |

**Critical Rule:** All SS-to-Al junctions require nylon washer isolation per galvanic prevention design.

---

# STEP M — META-LEARNING SKILLS APPLIED

| Skill | Step | Application |
|-------|------|-------------|
| Categorization | R | Grouped 39 requirements into 7 embodiment categories |
| Prioritization | I | Ranked by Hard/Soft constraints + ODI scores |
| Constraint identification | I | Found 5 conflicts requiring trade-off resolution |
| Filtering | S | Screened 6-8 candidates per component down to 2 |
| Satisficing | S | Selected "good enough" materials vs. optimal-but-expensive |
| Multi-criteria decision | M | Weighted analysis across strength, cost, corrosion, local availability |

---

# DOCUMENT LINKS

- [[02_conceptual/concept_selection|Concept Selection (Phase 2 Input)]]
- [[01_requirements/requirements_list|Requirements List]]
- [[01_requirements/standards_compliance|Standards Compliance Matrix]]
- [[03_embodiment/PRAD_principles_architecture|PRAD: Principles & Architecture]] ← NEXT

---

*This RISM document follows Steps R-I-S-M of the 15-step RISM-PRAD-DECS-OCP embodiment design methodology, establishing the requirements and material foundation for VDC-100 Enhanced.*
