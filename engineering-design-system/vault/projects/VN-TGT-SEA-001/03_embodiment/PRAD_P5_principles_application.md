---
project: VN-TGT-SEA-001
phase: 3
type: embodiment_design
step: "P5 — Principles Application"
group: PRAD
version: 1.0
created: 2026-02-10
status: draft
---

# Step P5: Principles Application — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Systematically apply 8 Pahl & Beitz design principles to all 7 subsystems of Concept A "Baseline Optimized", verifying that the embodiment design follows proven mechanical design guidelines and identifying where targeted improvements are needed.
**Method:** Pahl & Beitz Embodiment Design Principles (VDI 2221, Chapter 7)
**Input:** [[RISM_R1_requirements_identification.md]] — 74 direct embodiment requirements; [[RISM_M4_material_analysis.md]] — Material selections; [[../02_conceptual/concept_selection.md]] — Selected concept architecture (81.8%)

---

## 1. Design Principles Overview

The 8 Pahl & Beitz embodiment design principles are applied to each of the 7 subsystems (L0 Mooring, L1 Hull, L2 Frame, L2.5 Masts, L3 Reflectors, L5 GPS Beacon, L6 Tow System). Each principle is evaluated for applicability and compliance, producing a 7x8 compliance matrix.

| # | Principle | Core Question |
|---|-----------|---------------|
| P1 | Force Flow | Are load paths short, direct, and free of unnecessary bending? |
| P2 | Division of Tasks | Does each component have ONE clear primary function? |
| P3 | Self-Help | Are features self-centering, self-aligning, or self-locking? |
| P4 | Stability | Are equilibrium configurations stable under perturbation? |
| P5 | Direct vs Indirect Force Transmission | Are forces transmitted directly wherever possible? |
| P6 | Matched Deformations | Are deformation patterns compatible at all interfaces? |
| P7 | Force Balance | Are reaction forces and moments minimized by symmetry? |
| P8 | Fault-Free Design | Are dominant failure modes designed out proactively? |

---

## 2. Principle 1: Force Flow

**Rule:** Load paths must be short, direct, and carry loads in tension or compression rather than bending wherever possible.

### 2.1 Primary Load Path Diagrams

**Load Path A — Mooring (dominant operational load):**

```
WAVE DRIFT + WIND  ──►  HULL (distributed pressure on HDPE pontoon)
                              │
                              ▼
                        STEEL FRAME (continuous ring, distributes to center)
                              │
                              ▼
                        CENTRAL PAD EYE (200x200x10 mm backing plate)
                              │
                              ▼  TENSION (direct)
                        SWIVEL + SHACKLE
                              │
                              ▼  TENSION (direct, catenary)
                        G30 CHAIN (19 mm HDG, catenary curve)
                              │
                              ▼  TENSION → friction/suction
                        ANCHOR (Danforth/Bruce 50 kg, seabed)
```

**Analysis:** This path is efficient. Wave/wind loads distribute across the hull waterplane, concentrate through the steel frame radial members into the central pad eye, then transmit as pure tension through the mooring line. The only bending in this path occurs at the frame-to-pad-eye junction and is minimized by the 200x200x10 mm backing plate (ASM-005) which distributes the concentrated pad eye reaction over a large hull area.

**Load Path B — Wind on reflectors (secondary operational load):**

```
WIND (Bft 7, gust 46 kn)  ──►  REFLECTOR FACES (3x 0.8m plates, drag)
                                       │
                                       ▼  BOLT + PIN (shear + tension)
                                 AM FRAME (AlSi10Mg, distributes to mount)
                                       │
                                       ▼  4x M10 BOLTS (shear)
                                 MAST TOP PLATE (welded to tube)
                                       │
                                       ▼  BENDING (cantilever)
                                 MAST TUBE (60x4 mm, 3.0 m span)
                                       │
                                       ▼  BENDING → SHEAR + COMPRESSION
                                 DECK SOCKET (welded to frame)
                                       │
                                       ▼  SHEAR + COMPRESSION
                                 STEEL FRAME (ring structure)
                                       │
                                       ▼
                                 HULL + MOORING (as Load Path A)
```

**Analysis:** This path has one unavoidable bending segment — the mast tube acts as a cantilever. Bending is the least efficient force transmission mode. Mitigation: the 60x4 mm tube provides 1,303 N-m capacity vs 1,100 N-m required (18% margin, FOR-011). The cantilever is a design necessity (reflector must be elevated above hull for radar line-of-sight). Guyed mast fallback (R-2 mitigation) would convert bending to tension if margin proves insufficient.

### 2.2 Force Flow Assessment Per Subsystem

| Subsystem | Primary Load Mode | Bending Present? | Efficiency | Improvement Possible? |
|-----------|-------------------|-------------------|------------|----------------------|
| L0: Mooring | Tension (catenary) | No | HIGH | No — optimal tension chain |
| L1: Hull | Hydrostatic pressure (distributed) | Minimal (hull flex) | HIGH | No — large waterplane distributes loads |
| L2: Frame | Compression + shear (ring) | At pad eye junction | GOOD | Backing plate already mitigates |
| L2.5: Masts | **Bending (cantilever)** | **Yes — primary mode** | **MODERATE** | Guyed mast fallback reduces bending |
| L3: Reflectors | Shear at bolted joint | Minimal (rigid AM frame) | HIGH | Monolithic AM frame is optimal |
| L5: GPS Beacon | Negligible loads | N/A | N/A | Lightweight clamp mount sufficient |
| L6: Tow System | Tension (bridle + line) | No | HIGH | Dyneema bridle is optimal tension member |

**Key finding:** The mast cantilever (L2.5) is the only significant bending-mode load path. All other paths are predominantly tension/compression, which is ideal per the force flow principle.

---

## 3. Principle 2: Division of Tasks

**Rule:** Each component should have ONE clear primary function. Multi-function components increase complexity and coupling.

### 3.1 Component-Function Mapping

| Component | Primary Function | Secondary Functions | Multi-Function Risk |
|-----------|-----------------|---------------------|---------------------|
| HDPE hull (L1) | Provide buoyancy | Deck surface, rain/wave drainage | LOW — secondary functions are inherent |
| PU foam fill | Ensure unsinkability | Thermal insulation (incidental) | NONE — single function |
| Steel frame (L2) | Distribute mooring loads | Support deck sockets, tow points | MEDIUM — load distribution is unified purpose |
| Central pad eye | Mooring attachment | None | NONE — single function |
| Mast tube (L2.5) | Elevate reflector to 3m AWL | Support GPS beacon (1 mast only) | LOW — GPS is lightweight addition |
| Deck socket | Receive and fix mast base | None | NONE — single function |
| AM frame (L3) | Maintain 90.0 +/-0.1 deg orthogonality | Structural load transfer to mount | LOW — alignment IS the function |
| CNC face plates (L3) | Provide X-band radar reflection | None | NONE — single function |
| Mooring chain (L0) | Transmit anchor load + catenary weight | Shock absorption via catenary sag | LOW — catenary is inherent physics |
| Anchor (L0) | Hold seabed position | None | NONE — single function |
| Swivel (L0) | Allow 360 deg weathervane rotation | None | NONE — single function |
| GPS beacon (L5) | Transmit position (GNSS + Iridium) | None | NONE — COTS single-function device |
| Tow bridle (L6) | Distribute tow load to 2 hull points | None | NONE — single function |
| Drogue (L6) | Provide yaw stability under tow | None | NONE — single function |

**Assessment:** No component carries conflicting dual functions. The steel frame (L2) is the most multi-functional element (mooring distribution + mast socket hosting + tow point), but these are all structural load-distribution tasks — a unified purpose. The GPS mast extension adds minimal coupling to one mast. Division of tasks is well implemented.

---

## 4. Principle 3: Self-Help

**Rule:** Design features that are self-centering, self-aligning, self-locking, or self-reinforcing. Reduces dependence on assembly skill and maintains function under vibration/fatigue.

### 4.1 Self-Help Features Per Subsystem

| Subsystem | Feature | Self-Help Type | Mechanism | Requirement |
|-----------|---------|----------------|-----------|-------------|
| L0: Mooring | Danforth anchor fluke design | **Self-setting** | Flukes rotate and dig into seabed under load; harder you pull, deeper it sets | FOR-007 |
| L0: Mooring | SPM catenary | **Self-restoring** | Catenary weight increases restoring force as displacement increases (nonlinear stiffness) | KIN-003 |
| L0: Mooring | Swivel bearing | **Self-aligning** | Platform weathervanes to minimum-drag heading automatically | KIN-003 |
| L1: Hull | Waterplane area (50.3 m2) | **Self-righting** | BM = 210.3 m; any roll generates enormous righting moment | SAF-007, KIN-001 |
| L1: Hull | Scupper drainage | **Self-draining** | Deck perimeter scuppers drain green water by gravity | FOR-009 |
| L2: Frame | Through-bolted pad eye with backing plate | **Self-distributing** | Load spreads over 200x200 mm area; prevents local punch-through | ASM-005 |
| L2.5: Masts | Socket-insert with taper | **Self-centering** | Conical taper at socket mouth guides mast tube into correct alignment during field erection | ASM-006 |
| L2.5: Masts | Locking pin through socket + mast | **Self-retaining** | Pin captures mast against uplift; gravity + bolt preload hold against vibration | SAF-006 |
| L3: Reflectors | 2x dowel alignment pins | **Self-aligning** | Pins enforce reflector-to-mast alignment to <0.1 deg without manual adjustment | SIG-009, ASM-004 |
| L3: Reflectors | Nylock nuts on mounting bolts | **Self-locking** | Nylon insert in nut resists vibration loosening without need for re-torque | SAF-006 |
| L3: Reflectors | Safety wire on critical bolts | **Self-retaining** | Wire prevents bolt loss even if Nylock fails; redundant retention | SAF-006 |
| L5: GPS Beacon | IP67/68 sealed enclosure | **Self-sealing** | O-ring seals maintain waterproofing without active intervention | ENR-001 |
| L6: Tow | 60 deg bridle spread | **Self-centering** | Bridle geometry centers tow load on hull axis; self-corrects yaw | TRA-003 |
| L6: Tow | Trailing drogue | **Self-stabilizing** | Drag at stern prevents yaw oscillation; passive stabilization | TRA-003 |

**Assessment:** Strong self-help implementation across all subsystems. The three most critical self-help features are: (1) mast socket self-centering taper for rapid field assembly, (2) dowel pin self-alignment for reflector orthogonality, and (3) anchor self-setting for reliable mooring in varied seabed conditions.

---

## 5. Principle 4: Stability

**Rule:** Prefer stable equilibrium configurations where perturbations generate restoring forces. Avoid indifferent or unstable equilibria.

### 5.1 Stability Assessment

| Subsystem | Equilibrium Type | Stability Class | Analysis |
|-----------|-----------------|-----------------|----------|
| L0: Mooring (catenary) | Displacement from equilibrium increases chain lift-off, increasing restoring force | **STABLE** (nonlinear spring) | Catenary stiffness increases with displacement — self-limiting; scope ratio 5:1-7:1 ensures no chain-taut condition in SS 6 |
| L0: Anchor | Flukes engage deeper with horizontal pull | **STABLE** (positive feedback to holding) | Properly set anchor has increasing holding power with increasing load — up to breakout threshold |
| L1: Hull (roll/pitch) | BM = 210.3 m; any angular displacement generates righting moment proportional to sin(theta) | **EXTREMELY STABLE** | GM >> 0 for all loading conditions; impossible to capsize. Hull follows wave surface (D/Lp < 0.15) |
| L1: Hull (heave) | Waterplane area 50.3 m2; 1 cm immersion = 503 N restoring force | **STABLE** (linear spring) | Heave natural period ~1-2 s; follows wave surface passively |
| L2.5: Mast base (compression) | Gravity (mast + reflector ~31 kg) + bolt preload compresses socket; wind uplift must exceed total compression to unseat | **STABLE** (provided preload maintained) | Locking pin provides redundant retention (SAF-006) |
| L2.5: Mast (lateral) | Cantilever deflection generates elastic restoring force; 60x4 steel tube returns to vertical after gust | **STABLE** (elastic spring) | Max tip deflection ~45 mm at gust load; within elastic range |
| L3: Reflector (on mast) | Reflector CG is above mount point; statically unstable about mount IF free to rotate | **STABLE** (via bolted constraint) | 4-bolt + 2-pin mount prevents rotation; bolted joint converts unstable free-body to rigidly constrained stable system |
| L5: GPS (on mast) | Clamped to mast; follows mast motion | **STABLE** (constrained) | Clamp preload exceeds wind + vibration loads |
| L6: Tow (under tow) | Bridle + drogue provide yaw stability; tow point forward of hull center of lateral resistance | **STABLE** (directional stability) | Forward tow point + aft drogue = weather-helm equivalent; self-correcting yaw |

**Key finding:** All subsystems operate in stable equilibrium. The hull (L1) has extraordinary stability (BM = 210.3 m) — this is inherent to the circular pontoon geometry and cannot be lost. The mast reflector CG is above the mount, but the bolted constraint eliminates the tipping instability.

---

## 6. Principle 5: Direct vs Indirect Force Transmission

**Rule:** Prefer direct force transmission (fewest intermediary components) over indirect paths with multiple joints and compliant members.

### 6.1 Force Transmission Assessment

| Force Path | Type | Components in Path | Efficiency | Notes |
|-----------|------|-------------------|------------|-------|
| Pad eye → shackle → chain | **DIRECT** | 2 (shackle, chain) | HIGH | Pin-loaded shackle is simplest possible marine connection |
| Chain → anchor | **DIRECT** | 1 (anchor shank) | HIGH | Chain shackled directly to anchor crown ring |
| Reflector → mast (bolt+pin) | **DIRECT** | 3 (bolt, pin, plate) | HIGH | 4 bolts + 2 pins = direct shear transfer; no intermediate brackets |
| Mast → deck socket | **DIRECT** | 1 (socket) | HIGH | Mast tube inserts directly into welded socket — tube-in-tube |
| Deck socket → frame | **DIRECT** | 0 (welded integral) | HIGHEST | Socket is fillet-welded to frame ring; monolithic joint |
| Frame → hull | **INDIRECT** | 2 (frame flange, bolts, hull shell) | MODERATE | Steel frame bolted to HDPE hull through flange; HDPE is compliant |
| Hull → water (buoyancy) | **DIRECT** | 0 | HIGHEST | Hull shell is the buoyancy surface; no intermediaries |
| Wind → reflector face | **DIRECT** | 0 | HIGHEST | Wind acts directly on face plate surface |
| Tow → bridle → hull padeyes | **DIRECT** | 2 (thimble, shackle) | HIGH | Standard marine termination; minimal intermediaries |

**Key finding:** The frame-to-hull interface (IF-01) is the only indirect path with a compliant intermediary (HDPE). This is addressed in Principle 6 (Matched Deformations) with steel-through-HDPE bolted flanges and backing plates. All other force paths are direct, with 0-3 intermediary components.

---

## 7. Principle 6: Matched Deformations

**Rule:** At interfaces between components of different stiffness, ensure deformation patterns are compatible. Prevent stress concentrations at stiff-to-flexible transitions.

### 7.1 Critical Interface Deformation Analysis

| Interface | Stiff Member | Compliant Member | Mismatch Risk | Mitigation Design Feature |
|-----------|-------------|------------------|---------------|--------------------------|
| **IF-01: Frame ↔ Hull** | S235 steel (E=210 GPa) | HDPE (E=0.8-1.2 GPa) | **HIGH** — 175:1 modulus ratio; steel frame impresses point loads into soft HDPE hull | (a) Wide steel flange (60 mm min) distributes bolt loads over large HDPE area; (b) HDPE backing washers (50 mm dia) under bolt heads; (c) Bolt torque limited to prevent HDPE creep; (d) Through-bolts (not self-tapping) span full hull thickness |
| **IF-02: Pad eye ↔ Frame** | Pad eye plate (10 mm S235) | Frame ring (6-8 mm S235) | **LOW** — same material, matched stiffness | 200x200x10 mm backing plate welded to frame underside distributes concentrated pin load across frame |
| **IF-03: Mast socket ↔ Frame** | Mast tube (60x4 steel) | Socket (steel, welded to frame) | **LOW** — same material system | Fillet weld all around; socket wall >=5 mm for matched stiffness with 4 mm mast tube |
| **IF-04: Reflector ↔ Mast** | AlSi10Mg AM frame (E=70 GPa) | HDG steel mast top plate (E=210 GPa) | **MEDIUM** — 3:1 modulus ratio (Al softer); also galvanic isolation layer adds compliance | (a) Nylon isolation bushings at bolts add controlled compliance; (b) 4-bolt pattern spreads load; (c) Bolt preload maintains contact face friction; (d) Sealant (Sikaflex) fills minor surface irregularities |
| **IF-05: Face plate ↔ AM frame** | 6061-T6 face (E=69 GPa, 3 mm) | AlSi10Mg frame (E=70 GPa) | **NONE** — near-identical modulus (Al-Al) | Matched aluminum alloys; thermal expansion coefficients within 12% (23.6 vs 21 um/m-degC); minimal differential thermal stress |
| **IF-07: Hull sections** (if 2-section) | HDPE half-hull A | HDPE half-hull B | **LOW** — same material | Bolted flange with continuous gasket; both sections deform identically under wave loading |

**Key finding:** IF-01 (steel frame to HDPE hull) is the most critical deformation-mismatch interface. The 175:1 modulus ratio means steel frame members will indent into the HDPE hull unless loads are distributed over large areas. The design addresses this with wide flanges, backing washers, and controlled bolt torque. IF-04 (reflector to mast) has a secondary mismatch mitigated by the nylon isolation layer that doubles as a compliant shim.

---

## 8. Principle 7: Force Balance

**Rule:** Minimize reaction forces and moments through symmetric arrangements. Balanced forces reduce structural demands and improve fatigue life.

### 8.1 Force Balance Assessment

| System | Balance Arrangement | Balance Effectiveness | Residual Imbalance |
|--------|---------------------|----------------------|--------------------|
| **8 reflectors at 45 deg** | Octagonal symmetry; any wind direction loads 2-3 reflectors on windward side, balanced by leeward hull drag | **GOOD** — worst-case asymmetry is wind at 22.5 deg (between 2 reflectors), giving ~15% higher load on one mast vs neighbor | Residual: ±15% mast load variation with wind direction; within 18% structural margin |
| **SPM weathervaning** | Platform rotates to align minimum-drag heading into wind/current; eliminates fixed asymmetric loading | **EXCELLENT** — wind always approaches from bow direction after weathervaning settles (~5 min response) | Residual: transient asymmetric loads during weathervane response; damped by hull rotational inertia |
| **Central pad eye** | Single mooring point at geometric center of hull | **EXCELLENT** — all mooring forces pass through center; no yaw moment from mooring | Residual: none; single-point = zero yaw moment by definition |
| **2-point tow bridle** | Symmetric V-bridle at ±30 deg from centerline | **GOOD** — equal-length legs balance tow force about centerline | Residual: tow yaw if legs slightly unequal length; drogue corrects |
| **Hull buoyancy** | Circular hull = axially symmetric waterplane | **EXCELLENT** — righting moment is identical in all directions; no preferred heel axis | Residual: none; perfect circular symmetry |
| **Mast gravity loads** | 8 masts at 45 deg, equal mass (~31 kg each) | **EXCELLENT** — CG of mast system is at hull center if all masts installed | Residual: ±1 kg mass tolerance per mast gives <0.5 mm CG shift; negligible |

**Key finding:** Force balance is inherently strong due to the circular hull geometry (axial symmetry) and 8-fold reflector arrangement. The SPM weathervaning further improves balance by aligning the platform with the dominant environmental force direction. No design changes needed.

---

## 9. Principle 8: Fault-Free Design

**Rule:** Identify dominant failure modes and design them out proactively. This is a mini-FMEA (Failure Mode and Effects Analysis) applied through the lens of design principles.

### 9.1 Fault-Free Design Per Subsystem

#### L0: Storm Mooring

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Anchor drag in storm | HIGH | (a) 3:1 SWL margin (FOR-006); (b) anchor pre-set under controlled load at deployment; (c) catenary weight increases holding as load increases (self-help) | Self-help + force flow |
| Chain fatigue fracture | HIGH | (a) G30 HDG chain rated >100,000 cycles at SWL; (b) zinc coating prevents corrosion-accelerated fatigue; (c) swivel prevents chain twist | Fault-free (overdesign at fatigue) |
| Swivel seizure (no weathervane) | MEDIUM | (a) Marine-grade swivel rated for continuous immersion; (b) SPM system still functions without swivel — chain can twist ±2 turns safely; (c) visual inspection at deployment | Redundancy + self-help |

#### L1: HDPE Hull

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Hull puncture (collision/debris) | MEDIUM | (a) HDPE is impact-resistant (600-1000% elongation); (b) closed-cell foam fill ensures buoyancy even with hull breach; (c) >93% reserve buoyancy = hull remains afloat even fully flooded | Fault-free (damage tolerance) |
| Capsize | HIGH | (a) BM = 210.3 m — physically cannot capsize; (b) roll angle <=7.5 deg even in SS 6; (c) foam fill lowers CG further | Stability (inherent) |
| UV degradation | LOW | (a) HDPE with carbon black stabilizer: 20+ year UV life; (b) expendable product — deployed for hours to days, not years | Material selection |

#### L2: Steel Frame

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Pad eye weld failure | CRITICAL | (a) Full-penetration weld with UT inspection (QUA); (b) 200x200x10 backing plate distributes load; (c) 3:1 SWL margin on pad eye capacity | Force flow + direct transmission |
| Corrosion of frame under HDG | LOW | (a) HDG 85+ um zinc per ASTM A123; (b) zinc life 10-15 years immersed — far exceeds expendable mission; (c) sacrificial zinc protects base steel even if coating scratched | Fault-free (protective coating) |
| Frame-to-hull bolt pull-through | MEDIUM | (a) Large backing washers on HDPE side; (b) bolt torque controlled to prevent HDPE cold flow; (c) through-bolts (not blind fasteners) span full hull thickness | Matched deformations |

#### L2.5: Mast System

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Mast base weld fatigue (40K cycles) | HIGH | (a) 60x4 tube provides 18% margin over required bending; (b) fillet weld toe ground smooth to improve fatigue detail category; (c) if insufficient, upsizing to 76x5 tube adds 70% capacity at +3 kg/mast | Force flow + fault-free |
| Mast pulled from socket by wave uplift | MEDIUM | (a) Locking pin through socket and mast prevents withdrawal; (b) gravity + bolt preload exceed worst-case uplift; (c) safety lanyard as tertiary retention | Self-help (self-locking) |
| Reflector falls from mast top | HIGH | (a) 4x M10 bolts with Nylock nuts; (b) 2x dowel alignment pins share shear load; (c) safety wire on all 4 bolts prevents loss even if nuts loosen; (d) >=31 kg total — cannot be dislodged by wind alone | Self-help + redundancy |

#### L3: Reflectors

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Orthogonality loss (>0.1 deg) | HIGH | (a) Monolithic AM frame prints all 3 face-plate datums as single part — no tolerance stack-up; (b) 2 dowel alignment pins fix reflector-to-mast geometry; (c) bolt preload maintains contact face friction | Self-help (self-aligning) |
| Face plate corrosion (RCS loss) | MEDIUM | (a) Type II anodize >=10 um per MIL-A-8625; (b) 6061-T6 has good base corrosion resistance; (c) expendable use = hours to days exposure, not years | Fault-free (protective coating) |
| AM frame pitting corrosion | MEDIUM | (a) Type III hard anodize >=25 um; (b) Si-phase boundaries in AlSi10Mg are vulnerable — hard anodize seals surface; (c) nylon isolation at steel mast interface prevents galvanic acceleration | Matched deformations + fault-free |

#### L5: GPS Beacon

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Water ingress (battery short) | HIGH | (a) IP67/68 COTS enclosure with O-ring seals; (b) mounted at highest point (>=4.5 m AWL) — least wave exposure; (c) cable glands sealed | Self-help (self-sealing) |
| Battery depletion before 72h | MEDIUM | (a) Battery sized for 72h at 1 Hz fix rate with 20% margin; (b) pre-deployment battery check in SOP; (c) low-power GNSS module selected | Fault-free (margin) |

#### L6: Tow System

| Failure Mode | Severity | Design-Out Feature | Principle Applied |
|-------------|----------|-------------------|-------------------|
| Tow line failure under load | HIGH | (a) 16 mm Dyneema SWL 8,000 kgf vs peak tow load ~2,500 kgf = 3.2:1 margin; (b) Dyneema has no fatigue limit in tension; (c) soft eye + thimble prevents abrasion at termination | Force flow + fault-free |
| Yaw instability under tow | MEDIUM | (a) Trailing drogue provides directional stability; (b) 60 deg bridle spread centers tow force; (c) hull circular geometry has no preferred yaw coupling | Force balance + self-help |

---

## 10. Consolidated Design Principles Compliance Summary

Each cell is rated: **PASS** = fully compliant, **PARTIAL** = partially addressed (improvement identified), **N/A** = principle not applicable to this subsystem.

| Subsystem | P1 Force Flow | P2 Division of Tasks | P3 Self-Help | P4 Stability | P5 Direct/Indirect | P6 Matched Deform. | P7 Force Balance | P8 Fault-Free |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **L0: Mooring** | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS |
| **L1: Hull** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| **L2: Frame** | PASS | PASS | PASS | N/A | PASS | PARTIAL | PASS | PASS |
| **L2.5: Masts** | PARTIAL | PASS | PASS | PASS | PASS | N/A | PASS | PARTIAL |
| **L3: Reflectors** | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| **L5: GPS Beacon** | N/A | PASS | PASS | PASS | N/A | N/A | N/A | PASS |
| **L6: Tow System** | PASS | PASS | PASS | PASS | PASS | N/A | PASS | PASS |

### 10.1 Summary Statistics

| Rating | Count | Percentage |
|--------|-------|-----------|
| **PASS** | 43 | 76.8% |
| **PARTIAL** | 3 | 5.4% |
| **N/A** | 10 | 17.9% |
| **FAIL** | 0 | 0.0% |
| **Total** | **56** | **100%** |

### 10.2 PARTIAL Items Requiring Attention

| # | Subsystem | Principle | Issue | Required Action | Priority |
|---|-----------|-----------|-------|-----------------|----------|
| 1 | L2: Frame | P6 Matched Deformations | Steel-to-HDPE interface (IF-01) has 175:1 modulus ratio; bolt pull-through and HDPE creep under sustained load are risks | Validate flange width (>=60 mm), backing washer size (>=50 mm dia), and bolt torque limit through prototype testing or HDPE creep analysis | HIGH |
| 2 | L2.5: Masts | P1 Force Flow | Cantilever bending is unavoidable but only 18% margin; fatigue at weld toe unverified for 40,000 cycles | Complete FEA and fatigue analysis per Phase 3 Task 1; if margin <1.5x, upsize to 76x5 tube or add guy wires | HIGH |
| 3 | L2.5: Masts | P8 Fault-Free | Mast weld fatigue life not yet verified; 40,000 cycles at +-7 deg roll in SS 6 is demanding for a fillet weld detail | Specify weld toe grinding (improves fatigue category by ~30%); verify by S-N curve analysis or prototype cyclic test | HIGH |

---

## 11. Design Actions Summary

Actions derived from principles application, to be resolved in subsequent PRAD steps (R6 Layout, A7 Tolerance Analysis, D8 Detail Design):

| # | Action | Source Principle | Subsystem | Target Step | Requirement |
|---|--------|-----------------|-----------|-------------|-------------|
| DA-01 | Verify IF-01 flange width and bolt torque for HDPE creep resistance | P6 Matched Deformations | L2 Frame | R6 Layout | FOR-009, ASM-005 |
| DA-02 | Complete mast FEA: bending, fatigue (40K cycles), dynamic amplification | P1 Force Flow, P8 Fault-Free | L2.5 Masts | D8 Detail | FOR-010, FOR-011 |
| DA-03 | Specify weld toe grinding at mast-socket fillet weld | P8 Fault-Free | L2.5 Masts | D8 Detail | FOR-010 |
| DA-04 | Confirm galvanic isolation detail at IF-04 (nylon bushings, Sikaflex) | P6 Matched Deformations, P8 Fault-Free | L3/L2.5 | A7 Tolerance | MAT-008, MAT-009, OPR-009 |
| DA-05 | Define mast socket taper geometry for self-centering (cone angle, tolerance) | P3 Self-Help | L2.5 Masts | D8 Detail | ASM-006 |
| DA-06 | Specify Nylock nut grade and safety wire routing for 8 reflectors | P3 Self-Help, P8 Fault-Free | L3 Reflectors | D8 Detail | SAF-006, ASM-004 |

---

## 12. Cross-References

### Phase 3 RISM/PRAD Documents
- [[RISM_R1_requirements_identification.md]] — R1: 74 direct embodiment requirements; load values, interface definitions
- [[RISM_I2_critical_requirements.md]] — I2: Critical requirements prioritization; sizing drivers
- [[RISM_S3_material_selection.md]] — S3: Material candidate screening
- [[RISM_M4_material_analysis.md]] — M4: Material selection matrices; galvanic compatibility assessment (Section 6.2)
- PRAD_R6_layout.md — R6: Layout design (pending; receives DA-01, DA-04, DA-05)
- PRAD_A7_tolerance_analysis.md — A7: Tolerance analysis (pending; receives DA-04, DA-06)
- PRAD_D8_detail_design.md — D8: Detail design (pending; receives DA-02, DA-03, DA-05, DA-06)

### Phase 2 Source Documents
- [[../02_conceptual/concept_selection.md]] — Concept A architecture, risk register (R-1 through R-5), load path descriptions

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] — 116 requirements (Rev B.1); structural loads FOR-001 through FOR-011
- [[../01_requirements/standards_mapping.md]] — MIL-STD, ASTM, TCVN standards for materials and testing

---

**Document Status:** Draft v1.0 — All 8 Pahl & Beitz design principles applied to 7 subsystems (56 cells evaluated). 43 PASS, 3 PARTIAL, 10 N/A, 0 FAIL. Three PARTIAL items identified for resolution in subsequent PRAD steps (mast FEA/fatigue and frame-hull interface validation).
