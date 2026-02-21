---
project: VN-TGT-SEA-001
phase: 3
type: prototype_validation
document: "PROTO — AM Reflector Prototype Build & RCS Validation"
version: 1.0
created: 2026-02-10
status: draft
---

# AM Reflector Prototype Build & RCS Validation — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Manufacture 1× hybrid AM/CNC corner reflector (0.8 m edge), verify dimensional accuracy (orthogonality ±0.10°), and measure RCS at X-band (9.4 GHz) to validate predicted 152.3 m² per reflector.
**Input:** [[DECS_D9_detail_specification.md]], [[DECS_S12_standards_compliance.md]], [[OCP_C14_cost_analysis.md]], [[RISM_M4_material_analysis.md]], [[OCP_O13_design_optimization.md]]
**Classification:** Development test — Phase 3 risk reduction, pre-production validation

---

## 1. Objective & Scope

### 1.1 Why This Test Matters

The hybrid AM/CNC corner reflector is the **core technology differentiator** of THANH TRI-H and the **highest-risk component**:

- **AM frames** (AlSi10Mg LPBF) have never been used for radar reflector structures in Vietnamese defense
- **RCS prediction** (152.3 m² per reflector) is based on theoretical calculation for an ideal trihedral — real-world performance depends on fabrication accuracy
- **Orthogonality tolerance** (±0.10° assembled) is the tightest specification in the entire product — must be validated before committing to production of 8 reflectors × 10+ units

### 1.2 Test Objectives

| # | Objective | Success Criterion | Traceability |
|---|-----------|-------------------|-------------|
| OBJ-1 | Validate AM frame manufacturability at ASEAN LPBF bureau | Frame delivered within spec, no critical defects | PRD-003, MAT-004 |
| OBJ-2 | Verify assembled orthogonality ±0.10° | CMM measurement: all 3 face pairs within 90.00° ±0.10° | SIG-009 |
| OBJ-3 | Measure single-reflector RCS at X-band (9.4 GHz) | Peak RCS ≥120 m² (≥80% of 152.3 m² theoretical) | SIG-001, SIG-002 |
| OBJ-4 | Characterize RCS angular pattern (±30° off-axis) | 3 dB beamwidth ≥22° per face pair | SIG-003 (minimum coverage) |
| OBJ-5 | Validate CNC face plate flatness and surface finish | Flatness <0.1 mm; Ra ≤6.3 μm | SIG-001 (reflectivity) |
| OBJ-6 | Confirm galvanic isolation approach at face-to-frame interface | No corrosion initiation after 72h salt fog (if combined with T-01) | MAT-008, OPR-009 |

### 1.3 Scope

**In scope:**
- 1× complete reflector assembly (1 AM frame + 3 CNC face plates + all fasteners)
- AM material qualification coupons (3 tensile, 3 hardness, 1 CT scan)
- CMM dimensional inspection (frame and assembled reflector)
- RCS measurement at 9.4 GHz (single reflector, turntable sweep)
- Optional: 72h salt fog exposure (combine with S12 Test T-01)

**Out of scope:**
- Mast assembly and mast-to-reflector interface (IF-04) — tested separately
- Full 8-reflector composite RCS — extrapolated from single-reflector data
- Sea trial — covered by S12 Test T-05

---

## 2. Prototype Reflector Specification

### 2.1 Assembly Overview

```
PROTOTYPE REFLECTOR ASSEMBLY — 1× UNIT
═══════════════════════════════════════

                    Face B (800×800×3)
                   ╱
                  ╱  90.00° ±0.10°
                 ╱
   Face A ──────╳────── Face C
  (800×800×3)   │     (800×800×3)
                │
           AM Frame
         (AlSi10Mg)
                │
        Base Flange
       (200×200×6)

Total mass: ~24 kg
  Frame:       8.5 kg
  3× faces:   15.5 kg (3 × 5.18 kg)
  Fasteners:   0.9 kg (12× M6 bolts, 6× dowel pins, safety wire)
```

### 2.2 Prototype Bill of Materials

| # | Item | Specification | Qty | Source | Unit Cost ($) | Extended ($) |
|---|------|---------------|-----|--------|---------------|-------------|
| P-01 | AM frame, AlSi10Mg LPBF, T5 aged | Per D9 Section 5.2 | 1 | ASEAN AM bureau | 900.00 | 900.00 |
| P-02 | CNC face plate, 6061-T6, 800×800×3 mm | Per D9 Section 5.1 | 3 | VN CNC shop | 38.00 | 114.00 |
| P-03 | Type III hard anodize, AM frame | ≥25 μm, MIL-A-8625F | 1 | ASEAN (at AM bureau) | 75.00 | 75.00 |
| P-04 | Type II clear anodize, face plates | ≥10 μm, MIL-A-8625F | 3 | VN local anodizer | 12.50 | 37.50 |
| P-05 | Helicoil insert, M6×1.5D, SS304 | Per D9 Section 5.2 | 12 | Import | 0.85 | 10.20 |
| P-06 | M6×20 A4-80 SHCS (face to frame) | SS316, socket head cap | 12 | Local | 0.35 | 4.20 |
| P-07 | M6 A4-80 Nylock nut | SS316 | 12 | Local | 0.15 | 1.80 |
| P-08 | M6 SS316 flat washer | SS316 | 12 | Local | 0.10 | 1.20 |
| P-09 | Dowel pin, Ø5 m6 × 12 mm, SS316 | Precision ground | 6 | Local | 0.60 | 3.60 |
| P-10 | Safety wire, MS20995-C32, 0.8 mm SS | Per D9 Section 5.3 | 2 | m | 1.20 | 2.40 |
| P-11 | Tef-Gel anti-seize compound | Marine grade | 1 | tube (shared) | 5.00 | 5.00 |
| P-12 | AM tensile test coupons (XY, XZ, ZX) | Per ASTM E8, co-printed | 3 | (incl. in P-01) | 0.00 | 0.00 |
| P-13 | AM hardness test blocks | Per ASTM E18 | 3 | (incl. in P-01) | 0.00 | 0.00 |
| | **PROTOTYPE BOM TOTAL** | | | | | **$1,154.90** |

### 2.3 Key Dimensional Requirements (Prototype)

| Parameter | Nominal | Tolerance | Tier | Inspection Method |
|-----------|---------|-----------|------|-------------------|
| **Frame orthogonality (3 face pairs)** | 90.00° | **±0.05°** (frame alone) | T1 | CMM — 3 surface scans per pair |
| **Assembled orthogonality (3 face pairs)** | 90.00° | **±0.10°** (frame + faces) | T1 | CMM — 3 surface scans per pair |
| Face plate flatness (each face) | Flat | <0.1 mm over 800 mm | T2 | CMM or granite flat + dial indicator |
| Face plate surface roughness | — | Ra ≤6.3 μm | T2 | Profilometer, 3 readings per plate |
| Face plate thickness | 3.0 mm | ±0.1 mm | T2 | Micrometer at 5 points per plate |
| Face plate edge dimension | 800 mm | ±0.5 mm | T2 | CMM or calibrated tape |
| AM frame mounting boss flatness | Flat | ≤0.05 mm per surface | T1 | CMM |
| Dowel hole position (frame) | Per drawing | ±0.05 mm | T1 | CMM |
| Dowel hole diameter (frame, H7) | Ø5 +0.000/+0.012 mm | H7 | T1 | Pin gauge |
| Overall envelope | ~800×800×800 mm | ±2 mm | T3 | CMM |

---

## 3. AM Frame Procurement

### 3.1 Supplier Selection

| Bureau | Location | Machine | Lead Time | Quote Basis |
|--------|----------|---------|-----------|-------------|
| **Xometry ASEAN** | Singapore | EOS M290 / SLM 280 | 2-3 weeks | Online instant quote |
| **Facfox** | Shenzhen, China | SLM 280 / BLT | 2-3 weeks | RFQ via platform |
| **JR Tech Solutions** | Bangkok | EOS M290 | 3-4 weeks | Direct RFQ |

**Recommendation:** Order from **2 bureaus** simultaneously (1 frame + coupons each). Total: 2 frames, select best for RCS test. Cost: 2 × $900 = $1,800 (budget for dual sourcing).

### 3.2 AM Build Specification (to be transmitted with CAD file)

| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Material | AlSi10Mg per ASTM F3318 | Powder CoA required |
| Powder PSD | D50: 30-45 μm | Per ASTM B937 |
| Recycled powder ratio | ≤30% | Documented in build report |
| Layer thickness | 30 μm | ±5 μm |
| Laser power | 370 W | ±10 W |
| Scan speed | 1,300 mm/s | ±50 mm/s |
| Atmosphere | Argon, O₂ <0.1% | Continuous monitor |
| Build orientation | Base flange DOWN (Z-axis vertical, mounting surfaces in XY plane) | Per DfAM review |
| Heat treatment | T5: 300°C / 2h / air cool (on build plate) | Before plate removal |
| Post-machining | All 3 mounting boss surfaces, base flange, 12× M6 Helicoil bores, 6× Ø5 H7 dowel holes, 4× Ø11 clearance holes, 2× Ø8 H7 dowel holes | CNC at AM bureau |
| Surface treatment | Type III hard anodize ≥25 μm per MIL-A-8625F | After machining |
| CT scan | 1× full-frame industrial CT (voxel ≤100 μm) | First article only |
| Tensile coupons | 3× co-printed, ASTM E8 dog-bone (XY, XZ, ZX orientations) | On same build plate |
| Hardness blocks | 3× co-printed, per ASTM E18 | On same build plate |

### 3.3 AM Acceptance Criteria (Frame Delivery)

| Check | Method | Accept | Reject |
|-------|--------|--------|--------|
| Visual | Unaided eye + 10× loupe | No cracks, delamination, unfused powder | Any visible defect on load-bearing surfaces |
| Orthogonality (raw frame) | CMM, 3 face-pair angles | All pairs 90.00° ±0.08° | Any pair >±0.10° |
| Mounting boss flatness | CMM | ≤0.05 mm per surface | >0.08 mm |
| Dowel hole diameter | Pin gauge (Ø5 H7) | +0.000/+0.012 mm | Outside H7 range |
| Dowel hole position | CMM | ±0.05 mm from nominal | >0.08 mm |
| Tensile coupon (XY) | ASTM E8 | σ_y ≥230 MPa, σ_UTS ≥330 MPa, ε ≥5% | Below any threshold |
| Tensile coupon (Z) | ASTM E8 | σ_y ≥210 MPa, σ_UTS ≥300 MPa, ε ≥3% | Below any threshold |
| Hardness | Rockwell B or Vickers | HRB 65-85 (HV 100-130) | Outside range |
| CT scan | Industrial X-ray CT | No internal voids ≥1.0 mm; no delamination | Any void ≥1.0 mm |
| Hard anodize thickness | Eddy current gauge | ≥25 μm | <20 μm |
| Mass | Scale | 7.5-9.5 kg (target 8.5 kg) | >10 kg or <6 kg |

---

## 4. CNC Face Plate Procurement

### 4.1 Material Specification

| Parameter | Value | Standard |
|-----------|-------|----------|
| Alloy | 6061-T6 | ASTM B209 |
| Stock size | 900 × 900 × 4 mm (oversized for clamping margin) | Mill certificate required |
| Temper verification | Brinell hardness 95 HB typical | Spot-check 1 per sheet |

### 4.2 CNC Process

| Step | Operation | Tool | Target |
|------|-----------|------|--------|
| 1 | Mount on vacuum fixture (800 mm table) | CNC 3-axis, Mazak/Haas equivalent | Secure 4 edges + center suction |
| 2 | Fly-cut reflective face to flatness <0.05 mm | Single-point carbide or PCD insert, 0.05 mm DOC finishing pass | Ra ≤6.3 μm, flatness <0.1 mm |
| 3 | Flip; machine back face to 3.0 mm thickness | Fly-cut to thickness | ±0.1 mm |
| 4 | Drill 4× Ø7 mm clearance holes (M6 bolt) | Carbide drill | Position ±0.1 mm from datum |
| 5 | Ream 2× Ø5 H7 dowel holes | H7 reamer | +0.000/+0.012 mm |
| 6 | Edge trim to 800 × 800 mm | End mill | ±0.5 mm |
| 7 | Chamfer all edges 0.5 mm × 45° | Chamfer tool | Deburr, no sharp edges |
| 8 | Clean, inspect, package (protective film on reflective face) | — | No scratches |

**Quantity:** 3 plates for prototype + 1 spare = **4 plates total**

### 4.3 Face Plate Acceptance

| Check | Method | Accept | Reject |
|-------|--------|--------|--------|
| Flatness (reflective face) | CMM or granite flat + dial indicator, 9-point grid | <0.1 mm over 800 mm | ≥0.15 mm |
| Surface roughness | Profilometer, 3 readings per plate | Ra ≤6.3 μm | Ra >8.0 μm |
| Thickness | Micrometer at 5 points | 3.0 ±0.1 mm | Outside range |
| Edge dimension | Calibrated tape or CMM | 800 ±0.5 mm | Outside range |
| Hole positions | CMM (bolt holes + dowel holes) | ±0.1 mm | >0.15 mm |
| Dowel hole diameter | Pin gauge Ø5 H7 | +0.000/+0.012 mm | Outside H7 |
| Anodize thickness (post-anodize) | Eddy current gauge | 10-25 μm | <8 μm or >30 μm |

---

## 5. Assembly Procedure

### 5.1 Assembly Environment

- **Clean, covered workspace** — no sand, grit, or metal filings
- **Temperature:** 18-28°C (standard workshop)
- **Tools required:** Torque wrench (M6 range: 2-12 N·m), pin press (Ø5 soft-jawed), safety wire pliers, Tef-Gel applicator, lint-free wipes, IPA cleaning solvent

### 5.2 Assembly Sequence

| Step | Action | Acceptance Check |
|------|--------|-----------------|
| A-01 | Verify all components against BOM (P-01 through P-11). Confirm AM frame CMM report available. | BOM complete, CMM data reviewed |
| A-02 | Clean AM frame mounting surfaces with IPA wipe. Remove any anodize debris from Helicoil bores. | Surfaces visually clean, bore gauge confirms thread engagement |
| A-03 | Clean face plates (reflective face) with IPA wipe. Verify flatness report per plate. | Flatness reports reviewed, Ra confirmed |
| A-04 | Trial-fit Face A to Frame Surface A (dry, no fasteners). Check seating — full contact, no rocking. | Visual: <0.1 mm gap at all 4 corners |
| A-05 | Apply thin film of Tef-Gel to 2× Ø5 dowel pins. Press-fit dowel pins into Frame Surface A H7 holes using soft-jawed pin press. Verify pins stand proud 6 mm (half of 12 mm pin length). | Pin gauge: pins seated flush to 6.0 ±0.5 mm proud |
| A-06 | Lower Face A onto Frame Surface A. Engage dowel pins through face H7 holes (slide fit). Seat face fully against frame mounting boss. | Visual: face seated, pins engaged, no gap |
| A-07 | Install 4× M6×20 A4-80 SHCS through face clearance holes into Helicoil inserts. Finger-tight first, then torque to **8 ±1 N·m** using calibrated torque wrench. Sequence: diagonal pattern (1-3-2-4). | Torque wrench click at 8 N·m on all 4 bolts |
| A-08 | Repeat A-04 through A-07 for Face B and Face C. | All 3 faces installed, 12 bolts torqued |
| A-09 | Install safety wire: MS20995-C32 through bolt heads in pairs (2 bolts per wire loop, 6 loops total). Twist wire clockwise, minimum 6 twists per inch, trim and tuck ends. | Visual: all 6 wire loops secure, no sharp ends |
| A-10 | Install 12× M6 Nylock nuts on bolt shanks (backup retention). Hand-tight only — Helicoil is primary thread; Nylock is vibration backup. | All 12 Nylocks finger-tight + 1/4 turn |
| A-11 | **HOLD POINT — CMM Inspection (Section 6).** Do not proceed until orthogonality verified. | CMM report: all 3 pairs ≤±0.10° |

### 5.3 Rework Protocol

If CMM inspection (Step A-11) shows any face pair exceeding ±0.10°:

1. Identify which face(s) contribute to the error (CMM data will show individual face tilt)
2. Disassemble affected face (remove bolts, extract dowel pins)
3. Investigate root cause:
   - **Frame datum surface out-of-spec** → Return to AM bureau for re-machining (if <±0.15°) or reject frame
   - **Dowel pin bore misalignment** → Re-ream H7 holes with jig bore (if correctable)
   - **Face plate warpage** → Re-fly-cut on vacuum fixture with stress relief cycle
   - **Contamination between surfaces** → Clean and reassemble
4. Reassemble and re-inspect

---

## 6. Dimensional Inspection Plan

### 6.1 Equipment Required

| Equipment | Specification | Purpose |
|-----------|---------------|---------|
| **CMM (coordinate measuring machine)** | Accuracy ≤5 μm, travel ≥1,000 mm XYZ | Frame and assembly orthogonality |
| Profilometer | Ra measurement ≤0.1 μm resolution | Face plate surface roughness |
| Eddy current gauge | Anodize thickness 0-100 μm range | Coating verification |
| Micrometer (0-25 mm) | Resolution 0.01 mm | Face plate thickness |
| Pin gauges | Ø5 H7 (GO: 5.000 mm, NO-GO: 5.012 mm) | Dowel hole verification |
| Pin gauges | Ø8 H7 (GO: 8.000 mm, NO-GO: 8.015 mm) | Base flange dowel holes |
| Torque wrench | 2-12 N·m range, ±4% accuracy | Bolt torque |
| Digital scale | 0-50 kg, ±0.01 kg | Mass verification |

### 6.2 Inspection Sequence

#### Stage 1: AM Frame (Bare, Before Assembly)

| # | Measurement | Points | Accept | Record |
|---|-------------|--------|--------|--------|
| I-01 | Face pair A-B angle | 3 scans per surface, least-squares plane fit | 90.00° ±0.05° | Deviation from 90° |
| I-02 | Face pair B-C angle | 3 scans per surface | 90.00° ±0.05° | Deviation from 90° |
| I-03 | Face pair A-C angle | 3 scans per surface | 90.00° ±0.05° | Deviation from 90° |
| I-04 | Mounting boss flatness (Surface A) | 9-point grid per surface | ≤0.05 mm | Max deviation from plane |
| I-05 | Mounting boss flatness (Surface B) | 9-point grid | ≤0.05 mm | Max deviation from plane |
| I-06 | Mounting boss flatness (Surface C) | 9-point grid | ≤0.05 mm | Max deviation from plane |
| I-07 | Dowel hole positions (6× Ø5 H7) | CMM probe each hole center | ±0.05 mm from nominal | Position error vector |
| I-08 | Bolt hole positions (12× Ø7) | CMM probe | ±0.2 mm | Position error |
| I-09 | Base flange flatness | 9-point grid | ≤0.1 mm | Max deviation |
| I-10 | Base flange dowel holes (2× Ø8 H7) | Pin gauge + CMM | H7 range, ±0.05 mm position | GO/NO-GO + position |
| I-11 | Overall envelope | CMM bounding box | 800×800×800 ±2 mm | XYZ dimensions |

#### Stage 2: Face Plates (Before Assembly)

| # | Measurement | Points | Accept | Record |
|---|-------------|--------|--------|--------|
| I-12 | Flatness (reflective face), each of 3 plates | 9-point grid on CMM | <0.1 mm | Max deviation from plane |
| I-13 | Thickness, each plate | Micrometer, 5 points per plate | 3.0 ±0.1 mm | Min/max/average |
| I-14 | Surface roughness (reflective face), each plate | Profilometer, 3 readings per plate | Ra ≤6.3 μm | Average Ra |
| I-15 | Edge dimensions | CMM or calibrated tape | 800 ±0.5 mm | L × W per plate |
| I-16 | Anodize thickness | Eddy current, 3 points per plate | 10-25 μm | Average |

#### Stage 3: Assembled Reflector (After Step A-11)

| # | Measurement | Points | Accept | Reject | Record |
|---|-------------|--------|--------|--------|--------|
| **I-17** | **Face pair A-B angle** | **3 scans per face surface, least-squares fit** | **90.00° ±0.10°** | **>±0.15°** | **Critical — deviation from 90°** |
| **I-18** | **Face pair B-C angle** | **3 scans per face surface** | **90.00° ±0.10°** | **>±0.15°** | **Critical** |
| **I-19** | **Face pair A-C angle** | **3 scans per face surface** | **90.00° ±0.10°** | **>±0.15°** | **Critical** |
| I-20 | Face-to-frame gap (all 3 faces) | Feeler gauge at 4 corners per face | ≤0.05 mm | >0.10 mm | Gap at each corner |
| I-21 | Assembled mass | Digital scale | 23-25 kg | >27 kg or <20 kg | Total mass |

### 6.3 Tolerance Stack-Up Analysis

```
ORTHOGONALITY TOLERANCE STACK-UP (per face pair)
═════════════════════════════════════════════════

Source                           Contribution    Budget
────────────────────────────────────────────────────────
AM frame datum surface angle     ±0.05°          T1 (AM post-machining)
Face plate flatness effect       ±0.007°         <0.1 mm / 800 mm ≈ 0.007°
Dowel pin position error         ±0.004°         0.05 mm / 800 mm ≈ 0.004°
Face plate warpage (residual)    ±0.01°          Stress-relieved + fly-cut
Bolt clamping distortion         ±0.005°         8 N·m on 3 mm plate — negligible
────────────────────────────────────────────────────────
RSS total:  sqrt(0.05² + 0.007² + 0.004² + 0.01² + 0.005²)
          = sqrt(0.002500 + 0.000049 + 0.000016 + 0.000100 + 0.000025)
          = sqrt(0.002690)
          = 0.0519°

MARGIN: ±0.10° budget — ±0.052° RSS = ±0.048° margin (48% of budget)

CONCLUSION: AM frame machining accuracy (±0.05°) dominates the stack-up.
If the frame is within ±0.05°, the assembled reflector will be within ±0.10°
with high confidence (>99% assuming normal distribution, 3σ coverage).
```

---

## 7. RCS Test Plan

### 7.1 Theoretical RCS Prediction

```
TRIHEDRAL CORNER REFLECTOR — THEORETICAL RCS
══════════════════════════════════════════════

Formula (exact, for square trihedral):
  σ = (4π / 3) × a⁴ / λ²

Where:
  a = face edge length = 0.800 m
  λ = wavelength at 9.4 GHz = c / f = 3.0×10⁸ / 9.4×10⁹ = 0.03191 m
  a⁴ = 0.800⁴ = 0.4096 m⁴
  λ² = 0.03191² = 0.001018 m²

  σ = (4π / 3) × 0.4096 / 0.001018
    = 4.189 × 402.36
    = 1,684.7 m²  ← This is the MAXIMUM for a perfect reflector

CORRECTION FACTORS:
  Truncated trihedral (AM frame occupies some aperture):
    Aperture efficiency η ≈ 0.85 (estimated 15% blockage by frame edges)
    σ_corrected = 1,684.7 × 0.85² = 1,684.7 × 0.7225 = 1,217.2 m²

WAIT — let me reconcile with the project's 152.3 m² figure.

The 152.3 m² value used throughout Phase 0-3 appears to use a DIFFERENT
formula or geometry. Let me verify:

For a TRIANGULAR trihedral (each face is an isoceles right triangle
with legs = a):
  σ = (4π / 3) × a⁴ / λ²  (same formula, but effective aperture is
  smaller because triangular faces have ~50% the area of square faces)

  Actually, the standard formula σ = (4π/3)(a⁴/λ²) applies to
  TRIANGULAR trihedrals where 'a' is the leg length.

  For SQUARE trihedrals: σ = (12π)(a⁴/λ²)

Let me recalculate with the triangular formula:
  σ_tri = (4π/3) × 0.800⁴ / 0.03191²
        = 4.189 × 402.4
        = 1,685 m²

Hmm, this still gives ~1,685 m². The 152.3 m² figure implies:
  152.3 = (4π/3) × a⁴ / λ²
  a⁴ = 152.3 × λ² × 3 / (4π)
     = 152.3 × 0.001018 × 3 / 12.566
     = 0.4651 / 12.566
     = 0.03701
  a = 0.03701^(1/4) = 0.4386 m

This suggests the 152.3 m² figure is for an EFFECTIVE aperture of ~0.44 m,
not 0.8 m. This may reflect the truncated trihedral geometry where the
AM frame structure reduces the effective reflective area.

RECONCILIATION:
The Phase 0 analysis likely used a PRACTICAL RCS value accounting for:
  - Truncated (not full-depth) trihedral geometry
  - Frame shadowing and edge diffraction losses
  - Manufacturing imperfection allowance
  - Conservative estimate for system design

For this prototype test, we measure ACTUAL RCS and compare to:
  PRIMARY target:  152.3 m² (project design value, per reflector)
  THEORETICAL max: ~1,685 m² (ideal triangular trihedral, 0.8 m legs)
  MINIMUM accept:  120 m² (≥80% of 152.3 m² — allows for real-world losses)
```

**Note:** The discrepancy between theoretical maximum (~1,685 m²) and the project design value (152.3 m²) should be investigated during this test. The actual measured RCS will establish the true per-reflector performance. The 8-reflector composite target (≥1,000 m²) requires ≥125 m² per reflector average to achieve with some angular loss margin.

### 7.2 Test Configuration

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Frequency** | 9.4 GHz (X-band, standard marine/military radar) | Fixed frequency, CW or pulsed |
| **Polarization** | HH (horizontal-horizontal) primary; VV secondary | Both polarizations measured |
| **Range type** | Option A: Anechoic chamber (indoor) or Option B: Outdoor far-field range | See Section 7.3 for facility options |
| **Far-field distance** | R_ff = 2D²/λ = 2×(1.13)²/0.032 = 80 m minimum | D = diagonal of 0.8 m reflector = 1.13 m |
| **Target mounting** | Reflector mounted on low-RCS pylon (foam or dielectric), boresight facing transmitter | Pylon RCS <0.1 m² at 9.4 GHz |
| **Rotation** | 360° azimuth sweep in 0.5° steps (720 data points) | Turntable or manual repositioning |
| **Elevation** | 0° (horizontal plane) primary; ±10° secondary | Simulate sea-level engagement geometry |
| **Calibration** | Known reference target (metal sphere, σ_sphere = π×r²) | Calibrate before and after DUT measurement |
| **Dynamic range** | ≥40 dB | Required to measure sidelobes |

### 7.3 Facility Options

| Option | Facility | Pros | Cons | Est. Cost | Lead Time |
|--------|----------|------|------|-----------|-----------|
| **A: Anechoic chamber** | Military radar lab (VPN/VNPT) or university (HUST, BKU) | Controlled environment, repeatable, no weather dependency | Limited chamber size (verify ≥80 m range or use compact range); access coordination | $3,000-5,000 | 4-6 weeks |
| **B: Outdoor range** | Military test range (open field or coastal) | True far-field, no chamber size limitation, representative environment | Weather-dependent; ground clutter; multipath | $2,000-3,000 | 2-4 weeks |
| **C: Compact range** | University EM lab with parabolic reflector | Simulates far-field in small chamber; high precision | Limited availability in Vietnam | $4,000-6,000 | 6-8 weeks |

**Recommendation:** Option A (anechoic chamber) preferred for first measurement — controlled conditions give most reliable data. If chamber range length is insufficient (<80 m), use compact range (Option C) or outdoor range (Option B) as fallback.

### 7.4 Test Procedure

| Step | Action | Duration |
|------|--------|----------|
| T-01 | Pre-test calibration: mount reference sphere (σ known), measure at 0° and ±45°, verify system accuracy ±0.5 dB | 1 hour |
| T-02 | Mount prototype reflector on pylon, boresight aligned to transmitter (Face A normal facing TX) | 30 min |
| T-03 | **Full azimuth sweep (HH pol):** Rotate reflector 360° in 0.5° steps. Record received power at each angle. | 2 hours |
| T-04 | **Full azimuth sweep (VV pol):** Repeat T-03 with VV polarization | 2 hours |
| T-05 | **Elevation sweep (HH pol):** At boresight azimuth (0°), sweep elevation from -10° to +10° in 1° steps | 30 min |
| T-06 | Post-test calibration: re-measure reference sphere, verify ±0.5 dB consistency | 30 min |
| T-07 | Background measurement: remove DUT, measure pylon + mount RCS alone | 30 min |
| T-08 | Data processing: subtract background, calibrate against reference, plot σ vs θ (azimuth and elevation) | 2 hours (post-test) |

**Total test time:** ~1 day setup + measurement, ~0.5 day data processing

### 7.5 Data Products

1. **RCS vs. azimuth plot** (0-360°, HH and VV polarizations)
2. **Peak RCS value** (maximum σ at boresight for each face pair)
3. **3 dB beamwidth** per face pair (angular width where σ ≥ σ_peak/2)
4. **Minimum RCS** at worst angle (midpoint between face pairs)
5. **Average RCS** over 360° (weighted by angular density)
6. **Comparison table:** measured vs. predicted (152.3 m²) with deviation
7. **8-reflector extrapolation:** composite RCS estimate using measured single-reflector pattern

---

## 8. Pass/Fail Criteria

### 8.1 Primary Acceptance Criteria

| # | Criterion | PASS | MARGINAL | FAIL |
|---|-----------|------|----------|------|
| **PC-01** | **Assembled orthogonality** | All 3 face pairs within **90.00° ±0.10°** | 1 pair at ±0.12° (others ≤±0.10°) | Any pair >±0.15° |
| **PC-02** | **Peak RCS at boresight** | ≥**120 m²** (≥80% of 152.3 m²) | 100-120 m² (65-80% of prediction) | <100 m² |
| **PC-03** | **3 dB beamwidth** | ≥**22°** per face pair | 18-22° | <18° |
| **PC-04** | **Minimum RCS at worst angle** | ≥**15 m²** (single reflector) | 10-15 m² | <10 m² |
| **PC-05** | **8-reflector composite (extrapolated)** | ≥**1,000 m²** average over 360° | 800-1,000 m² | <800 m² |
| **PC-06** | **AM material properties** | All coupons meet ASTM F3318 minimums | 1 coupon marginal (within 5% of threshold) | Any coupon below threshold by >5% |
| **PC-07** | **Face plate flatness** | All 3 plates <0.1 mm | 1 plate 0.1-0.15 mm | Any plate >0.15 mm |
| **PC-08** | **Face plate Ra** | All 3 plates Ra ≤6.3 μm | 1 plate Ra 6.3-8.0 μm | Any plate Ra >8.0 μm |

### 8.2 Decision Matrix

| Result | Action |
|--------|--------|
| **ALL PASS** | Proceed to full production (8 reflectors × 10 units). Use validated specs for Phase 4 detail design. |
| **PC-01 MARGINAL** | Accept with deviation. Tighten AM frame spec to ±0.04° for production. Add shimming procedure to assembly instructions. |
| **PC-02 MARGINAL (100-120 m²)** | Investigate cause: (a) if orthogonality-driven → tighten tolerances; (b) if surface-driven → improve face plate finish; (c) if geometry-driven → resize reflector edge to 0.85 m (+6% area). Re-test after correction. |
| **PC-02 FAIL (<100 m²)** | Root cause analysis. Options: (1) increase reflector size to 0.9 m edge (+27% RCS); (2) switch to square trihedral geometry; (3) add 9th reflector position. Re-design and re-test before production. |
| **PC-05 MARGINAL (800-1,000 m²)** | Consider adding 9th or 10th reflector position. Re-analyze deck layout for additional mast sockets. |
| **PC-06 FAIL** | Reject AM bureau. Requalify alternative supplier. Do not proceed to production until material properties confirmed. |

---

## 9. RCS Sensitivity Analysis

### 9.1 Effect of Orthogonality Error on RCS

```
RCS DEGRADATION vs ORTHOGONALITY ERROR
═══════════════════════════════════════

For a trihedral corner reflector, RCS degrades as the cube of the
angular error from perfect orthogonality. The 3 dB loss angle is:

  θ_3dB ≈ 0.4 × λ/a (radians) = 0.4 × 0.032/0.800 = 0.016 rad = 0.92°

This means the reflector loses 3 dB (50% RCS) when the INCIDENT beam
is 0.92° off boresight — NOT when the faces are misaligned by 0.92°.

For FABRICATION orthogonality error δ (face misalignment):
The effect is equivalent to a beam offset of 2δ (reflected beam
deflects by 2× the surface tilt).

  At δ = 0.10° → equivalent beam offset = 0.20° → loss ≈ 0.3 dB (7%)
  At δ = 0.20° → equivalent beam offset = 0.40° → loss ≈ 1.2 dB (24%)
  At δ = 0.50° → equivalent beam offset = 1.00° → loss ≈ 3.5 dB (55%)
  At δ = 1.00° → equivalent beam offset = 2.00° → loss ≈ 8 dB (84%)

SUMMARY TABLE:
  Orthogonality Error | RCS Loss | % of Ideal | Result
  ────────────────────┼──────────┼────────────┼────────
  ±0.05° (frame spec) | 0.08 dB  | 98%        | EXCELLENT
  ±0.10° (assy spec)  | 0.3 dB   | 93%        | PASS
  ±0.15° (reject)     | 0.7 dB   | 85%        | MARGINAL
  ±0.20°              | 1.2 dB   | 76%        | CONCERN
  ±0.50°              | 3.5 dB   | 45%        | FAIL
  ±1.00° (CNC-only)   | 8 dB     | 16%        | FAIL

CONCLUSION: The ±0.10° assembled tolerance allows ≤0.3 dB loss —
acceptable for the project. CNC-only fallback frames (Strategy B,
±0.3° typical) would lose ~2 dB (37% reduction), which may still
meet the 1,000 m² composite target if per-reflector RCS is higher
than the conservative 152.3 m² estimate.
```

### 9.2 Effect of Surface Roughness on Reflectivity

```
SURFACE ROUGHNESS vs RADAR REFLECTIVITY
════════════════════════════════════════

The Rayleigh roughness criterion determines when a surface appears
"smooth" to radar:

  h_Rayleigh = λ / (8 × cos θ)

At normal incidence (θ = 0°), 9.4 GHz:
  h_Rayleigh = 31.9 mm / 8 = 3.99 mm

Any surface roughness Ra << 4 mm appears perfectly smooth at X-band.

Our face plate specification:
  Ra ≤ 6.3 μm = 0.0063 mm

  Ra / h_Rayleigh = 0.0063 / 3.99 = 0.0016 = 0.16%

CONCLUSION: Surface roughness is COMPLETELY NEGLIGIBLE at X-band.
Even a Ra = 100 μm surface (coarse mill finish) would have
Ra/h_Rayleigh = 2.5% — still smooth. The tight Ra ≤ 6.3 μm spec
is driven by face plate flatness quality (fly-cutting achieves
both flatness and finish simultaneously), NOT by radar reflectivity.

Similarly, Type II anodize (10-25 μm) is RF-transparent at 9.4 GHz:
  Skin depth in aluminum at 9.4 GHz: δ_s = 0.82 μm
  Anodize is non-conductive Al₂O₃ — radar passes through to metal
  substrate. Zero reflectivity impact.
```

---

## 10. Budget & Schedule

### 10.1 Budget

| # | Item | Cost ($) | Notes |
|---|------|----------|-------|
| 1 | AM frame × 2 (dual-source qualification) | 1,800 | 2 bureaus × $900 |
| 2 | CNC face plates × 4 (3 + 1 spare) | 152 | 4 × $38 |
| 3 | Type III hard anodize (2 frames) | 150 | 2 × $75 |
| 4 | Type II clear anodize (4 plates) | 50 | 4 × $12.50 |
| 5 | Fasteners, dowels, consumables | 30 | Per BOM P-05 to P-11 |
| 6 | AM tensile testing (6 coupons, 2 bureaus) | 300 | $50/coupon |
| 7 | AM CT scan (2 frames) | 400 | $200/frame |
| 8 | CMM inspection — frame (2 frames) | 200 | $100/frame (2 hrs @ $50/hr) |
| 9 | CMM inspection — assembled reflector | 150 | 3 hrs @ $50/hr |
| 10 | Assembly labor (2 reflectors from 2 frames) | 60 | 2 × 2.5 hrs × $12/hr |
| 11 | RCS measurement (facility + personnel) | 4,000 | Anechoic chamber or outdoor range |
| 12 | Data processing + report writing | 500 | 20 hrs engineering @ $25/hr |
| 13 | Transport (frame shipping ASEAN → VN) | 200 | DHL/FedEx × 2 shipments |
| 14 | Contingency (10%) | 799 | — |
| | | | |
| | **TOTAL PROTOTYPE + RCS VALIDATION** | **$8,791** | Within Phase 3 prototype budget |

**Budget source:** Phase 3 prototype fabrication allocation ($55,000 per C14 Section 9). This prototype test uses $8,791 (16%) of that allocation.

### 10.2 Schedule

```
AM REFLECTOR PROTOTYPE + RCS VALIDATION SCHEDULE
═════════════════════════════════════════════════

Week 1:
  ├── [ORDER] AM frames from 2 ASEAN bureaus (CAD + build spec transmitted)
  ├── [ORDER] 6061-T6 stock for CNC face plates (VN supplier)
  └── [BOOK]  RCS measurement facility (4-6 week lead time)

Week 2:
  ├── [CNC]   Machine 4 face plates at VN CNC shop (2 days)
  ├── [QC]    Inspect face plates: flatness, Ra, dimensions (0.5 day)
  └── [ANOD]  Send face plates to local anodizer (Type II clear, 3 days)

Week 3:
  ├── [AM BUILD] In progress at 2 ASEAN bureaus
  ├── [RECEIVE] Anodized face plates returned
  └── [QC]      Final face plate inspection (anodize thickness)

Week 4:
  ├── [AM DELIVERY] Receive AM frames from Bureau 1 (fastest)
  ├── [QC]    AM incoming inspection: visual, CMM (frame orthogonality)
  ├── [QC]    AM coupons: tensile test, hardness (send to local lab)
  └── [CT]    CT scan of frame (if facility available, else defer)

Week 5:
  ├── [AM DELIVERY] Receive AM frame from Bureau 2
  ├── [QC]    Bureau 2 frame inspection
  ├── [ASSEMBLY] Assemble Reflector #1 (best frame + 3 face plates)
  ├── [CMM]   Assembled reflector orthogonality inspection
  └── HOLD POINT: CMM results — PASS/MARGINAL/FAIL?

Week 6:
  ├── [RCS TEST] Transport assembled reflector to test facility
  ├── [RCS TEST] Setup, calibration, 360° azimuth sweep, elevation sweep
  └── [RCS TEST] Data processing, preliminary results

Week 7:
  ├── [ANALYSIS] Full data analysis, comparison to prediction
  ├── [REPORT]   Write prototype validation report
  ├── [ASSEMBLY] If Frame #2 better, assemble Reflector #2 for comparison
  └── [DECISION] PASS → proceed to production spec
                 MARGINAL → root cause + corrective action plan
                 FAIL → redesign iteration

TOTAL: 7 WEEKS (parallel with other Phase 3 validation activities)
CRITICAL PATH: AM frame delivery (3 weeks) → CMM → RCS test (1 week)
```

### 10.3 Dependencies & Parallel Activities

| Activity | Depends On | Can Run Parallel With |
|----------|------------|----------------------|
| AM frame order | CAD file release (Week 1) | CNC face plate fabrication |
| CNC face plates | Stock material available (Week 1) | AM frame build |
| Face plate anodize | CNC complete | AM frame build |
| Assembly | AM frame + face plates both received | — |
| CMM inspection | Assembly complete | AM coupon testing |
| RCS test | CMM PASS + facility booked | S12 Test T-01 (salt fog) |
| Report | RCS data available | — |

---

## 11. Contingency Plans

### 11.1 If AM Frame Delivery Delayed (>4 Weeks)

- **Action:** Proceed with CNC-machined 6061-T6 frame as interim test article
- **CNC frame spec:** 3-piece brazed or bolted assembly; orthogonality ±0.2-0.3° (lower accuracy)
- **Purpose:** Validate RCS measurement setup and face plate quality; AM frame tested when delivered
- **Cost:** ~$300 for CNC frame (local machining)
- **Schedule impact:** None — CNC frame available in 1 week

### 11.2 If Orthogonality Fails (>±0.15°)

- **Root cause 1: AM frame datum machining** → Request re-machining from bureau (1-2 week turnaround)
- **Root cause 2: AM build distortion** → Request modified build orientation or support strategy; re-print
- **Root cause 3: Face plate warpage** → Re-fly-cut with slower feed rate and stress-relief cycle
- **Fallback:** Accept ±0.15° and evaluate RCS impact (expect ~0.7 dB loss = 85% of ideal)

### 11.3 If RCS Fails (<100 m² Peak)

| Root Cause | Corrective Action | Timeline |
|------------|-------------------|----------|
| Orthogonality error (>±0.2°) | Tighten AM spec to ±0.03°; add shimming | 3 weeks (re-machine + re-test) |
| Frame shadowing/blockage | Redesign frame with thinner ribs (lattice optimization W-4) | 4 weeks (AM re-print) |
| Face plate size too small | Increase edge from 0.8 m to 0.9 m (+27% RCS) | 2 weeks (new CNC plates + re-test) |
| Anodize causing unexpected loss | Test bare (un-anodized) plates for comparison | 1 week |
| Measurement error | Re-calibrate, re-measure; verify with second facility | 2 weeks |

### 11.4 If Budget Overrun

- **Primary risk:** RCS facility cost exceeds $4,000 → Cap at $6,000 by negotiating university rate
- **Mitigation:** Use outdoor range ($2,000) instead of anechoic chamber if budget constrained
- **Hard limit:** $12,000 total (2× initial estimate) — requires Phase 3 budget reallocation approval

---

## 12. Deliverables

| # | Deliverable | Format | Recipient |
|---|-------------|--------|-----------|
| D-01 | AM frame CMM inspection report (2 frames) | PDF + CSV data | Project file |
| D-02 | AM tensile test report (6 coupons) | PDF per ASTM E8 | Project file |
| D-03 | AM CT scan report (1 or 2 frames) | PDF + DICOM images | Project file |
| D-04 | Face plate inspection report (4 plates) | PDF + CSV data | Project file |
| D-05 | Assembled reflector CMM report (orthogonality) | PDF — **key deliverable** | Project file + S-04 (QC) |
| D-06 | RCS measurement report (360° azimuth + elevation) | PDF + raw data (.csv or .s1p) | Project file + S-01 (customer) |
| D-07 | RCS vs. prediction comparison analysis | PDF — **key deliverable** | Project file + Phase 3 gate |
| D-08 | 8-reflector composite RCS extrapolation | PDF | Phase 3 gate review |
| D-09 | Prototype validation summary & recommendation | PDF — **gate document** | Phase 3 gate review |
| D-10 | Lessons learned (AM procurement, CNC quality, test facility) | Markdown → project file | Engineering team |

---

## 13. Cross-References

### Phase 3 Source Documents
- [[DECS_D9_detail_specification.md]] — Section 5: Reflector specifications (face plates, AM frames, assembly, IF-04)
- [[DECS_S12_standards_compliance.md]] — Section 3: ASTM F3301 AM qualification; Section 6: Test T-03 (RCS) and T-07 (AM qualification)
- [[OCP_C14_cost_analysis.md]] — Section 1.4: M4 Reflector Assembly BOM ($9,190/unit)
- [[OCP_O13_design_optimization.md]] — Section 4.1: 7 vs 8 reflectors analysis; W-4: AM lattice optimization
- [[RISM_M4_material_analysis.md]] — Section 2.3: Reflector face plate selection (6061-T6, 87.5%); Section 2.4: AM frame selection (AlSi10Mg, 78.8%)
- [[RISM_S3_material_selection.md]] — AM bureau supply chain assessment
- [[PRAD_D8_design_structure.md]] — Mast bending analysis (reflector wind load 142.2 N)
- [[DECS_C11_requirements_verification.md]] — SIG-001 to SIG-009 verification status (PENDING-TEST)

### Phase 1 Requirements Traced
- **SIG-001:** Peak RCS ≥1,000 m² (360° composite) → extrapolated from single-reflector data
- **SIG-002:** Average RCS ≥1,000 m² → extrapolated
- **SIG-003:** Minimum RCS ≥700 m² at any azimuth → verified by angular pattern
- **SIG-009:** Reflector orthogonality ±0.10° → directly measured (CMM)
- **MAT-004:** AlSi10Mg LPBF per ASTM F3318 → coupon testing
- **PRD-003:** ≥2 qualified AM suppliers → dual-source procurement validates

### Standards
- ASTM F3301-18a — AM PBF-LB/M process qualification
- ASTM F3318-18 — AlSi10Mg mechanical properties
- ASTM B937-18 — AlSi10Mg powder specification
- ASTM E8 — Tensile testing (AM coupons)
- ASTM E18 — Hardness testing
- MIL-A-8625F — Anodize coating (Type II, Type III)
- ASTM B209 — 6061-T6 plate specification
- IEEE Std 149-2021 — Standard Test Procedures for Antennas (RCS measurement methodology)

---

**Document Status:** Draft v1.0 — Complete prototype build and RCS validation plan for 1× hybrid AM/CNC corner reflector. Key parameters:

1. **Budget:** $8,791 (16% of Phase 3 prototype allocation)
2. **Schedule:** 7 weeks (AM delivery is critical path at 3 weeks)
3. **Primary success criterion:** Assembled orthogonality ±0.10° AND peak RCS ≥120 m² at 9.4 GHz
4. **Dual AM sourcing:** 2 ASEAN bureaus qualified simultaneously (risk reduction)
5. **RCS prediction note:** The project's 152.3 m²/reflector figure needs reconciliation against theoretical maximum (~1,685 m² for 0.8 m square trihedral). The actual measured value will establish the true design basis.
6. **Contingency:** CNC-only frame fallback if AM delivery delayed; reflector upsizing to 0.9 m edge if RCS falls short
