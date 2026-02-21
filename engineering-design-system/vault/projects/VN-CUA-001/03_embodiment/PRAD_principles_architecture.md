---
project: VN-CUA-001
designation: VDC-100
type: embodiment_PRAD
phase: 3
steps: P-R-A-D
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz 15-Step RISM-PRAD-DECS-OCP
selected_concept: VDC-100 Enhanced (Concept B, 85.8%)
---

# VN-CUA-001: PRAD — PRINCIPLES & ARCHITECTURE
## Vietnamese Drone Catcher 100 (VDC-100 Enhanced)
## Nguyên lý & Kiến trúc - Giai đoạn 3, Bước P-R-A-D

**Project Code:** VN-CUA-001
**Phase:** 3 - Embodiment Design (Steps P, R, A, D)
**Date:** 2026-02-08
**Input:** [[03_embodiment/RISM_requirements_materials|RISM: Requirements & Materials]]

---

# STEP P: PRINCIPLES APPLICATION

## P.1 Purpose

Apply Pahl & Beitz design principles systematically to each subsystem, creating principle-based layouts that maximize structural efficiency and reliability.

## P.2 Force Flow Principle

**Rule:** Load paths must be short, direct, and clearly traceable.

### P.2.1 Primary Load Paths

```
VDC-100 FORCE FLOW ANALYSIS
═══════════════════════════════════════════════════════════════════════════════

LOAD CASE 1: FIRING (100 bar gas pressure, 15 Ns recoil)
───────────────────────────────────────────────────────────────────────────

   GAS PRESSURE (100 bar) ──────────────────────────────────────►
   ┌────────────────────────────────────────────────────────────────────┐
   │  BARREL (hoop stress: 100 MPa)                                    │
   │  ═══════════════════════════════════════════════════════►         │
   │                                                    PROJECTILE     │
   └────────────────────────────────────────────────────────────────────┘
                                                        ◄──────────────
   RECOIL (15 Ns impulse)          ◄──────────────────────────────────
   ┌────────────────────────────────────────────────────────────────────┐
   │  BARREL ──► RECEIVER ──► STOCK ──► SHOULDER PAD ──► OPERATOR     │
   │  (direct axial line — no bending moments in recoil path)         │
   └────────────────────────────────────────────────────────────────────┘

LOAD CASE 2: DROP IMPACT (1m, ~150g shock)
───────────────────────────────────────────────────────────────────────────

   Impact point (corner/edge)
          │
          ▼
   ┌──────────────┐    ┌────────────────────┐    ┌──────────────────┐
   │ POLYMER       │──►│ ALUMINUM STRUCTURE  │──►│ INTERNAL         │
   │ BUMPER/STOCK  │    │ (absorbs load)      │    │ COMPONENTS       │
   │ (absorbs peak)│    │                    │    │ (protected)      │
   └──────────────┘    └────────────────────┘    └──────────────────┘

LOAD CASE 3: CARRYING (7.8 kg, sling points)
───────────────────────────────────────────────────────────────────────────

   Sling point (front) ─────────────────────── Sling point (rear)
          │                                           │
          ▼                                           ▼
   ┌──────────────────────────────────────────────────────────────┐
   │  Balanced load distribution: CG at ~55% from muzzle         │
   │  Sling attachment: 4mm SS through-holes in Al structure      │
   └──────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
```

### P.2.2 Force Flow Design Decisions

| Subsystem | Load Path | Design Feature | Principle Applied |
|-----------|-----------|----------------|-------------------|
| Barrel → Receiver | Axial recoil | Thread + shoulder (M100×1.5) | Short, direct axial transmission |
| Receiver → Stock | Axial recoil | 2× M6 bolts (direct tension) | Force balance (symmetric) |
| Scope → Receiver | Cross-bolt shear | Picatinny rail, 2× cross-bolts | Direct shear (no bending) |
| Cylinder → Stock | Radial clamp | Quick-release band clamp | Self-centering, friction lock |
| Trigger → Valve | Mechanical link | Direct pushrod (no cable) | Short path, minimal lost motion |

## P.3 Division of Tasks Principle

**Rule:** Each component performs one clear, unambiguous function.

| Component | Primary Function | Secondary Function | Allowed? |
|-----------|-----------------|-------------------|----------|
| Barrel | Accelerate projectile | — | ✅ Single function |
| Receiver | House trigger + valve + regulator | Structural backbone | ✅ Acceptable (structural is inherent) |
| Scope | Target acquisition + ranging | Status display | ⚠️ Monitor — display could be separate |
| Stock | Support operator interface | House cylinder | ⚠️ Monitor — cylinder mount is secondary |
| Safety lever | Block trigger | Indicate armed status | ✅ Indication is inherent to position |
| Trigger | Release valve | — | ✅ Single function |
| Regulator | Reduce 300→100 bar | — | ✅ Single function |

**Action Items:** Scope and stock carry secondary functions — acceptable because secondary functions are physically inseparable from primary.

## P.4 Self-Help Principle

**Rule:** Components should be self-centering, self-aligning, and self-locking where possible.

| Feature | Self-Help Type | Implementation |
|---------|---------------|----------------|
| Projectile loading | Self-centering | Tapered breech chamber guides projectile to center |
| Scope mounting | Self-aligning | Picatinny rail V-groove forces consistent alignment |
| Cylinder mounting | Self-locking | Quick-release clamp with positive detent |
| Breech closure | Self-locking | Spring-loaded latch with over-center lock |
| Safety lever | Bi-stable | Detent positions at ARM and SAFE (no middle state) |
| Stock adjustment | Self-locking | Detent pins at 10mm increments |

## P.5 Stability Principle

**Rule:** Design should prefer stable equilibrium configurations.

| Configuration | Stability Type | Design Implementation |
|---------------|---------------|----------------------|
| System on surface | Stable rest | Flat bottom surface on receiver, stock, and barrel |
| Shoulder firing position | Stable aim | CG aligned with shoulder contact, balanced weight |
| Breech open | Stable open | Spring detent holds breech open for loading |
| Breech closed | Stable closed | Over-center latch locks until deliberate release |
| Safety engaged | Default stable | Spring biases to SAFE position |

---

# STEP R: RULES APPLICATION (4 Basic Rules)

## R.1 Rule 1: CLARITY (Rõ ràng)

| Criterion | Requirement | VDC-100 Implementation | Status |
|-----------|-------------|------------------------|--------|
| Load paths traceable | Every structural path identifiable | Barrel → receiver → stock (direct line) | ✅ |
| Function separation | One function per component | 7 main components, each with primary function | ✅ |
| Interfaces defined | All connections standardized | M4/M6 fasteners, O-ring seals, Picatinny rail | ✅ |
| Status indication | Unambiguous system state | Armed/Safe LED (red/green), pressure gauge, breech indicator | ✅ |
| Failure modes predictable | Every failure identified | FMEA: valve fails closed (safe), trigger jams (no fire) | ✅ |
| Assembly sequence clear | Only one correct way | Keyed connectors, asymmetric mounting holes | ✅ |

**Clarity Score: 6/6 = 100%** ✅

## R.2 Rule 2: SIMPLICITY (Đơn giản)

| Metric | Target | VDC-100 Design | Status |
|--------|--------|----------------|--------|
| Total part count | ≤80 | **72 parts** | ✅ |
| Fastener types | ≤3 | **2 types** (M4×0.7, M6×1.0) | ✅ |
| Tool types for assembly | ≤3 | **2 tools** (3mm hex, 5mm hex) | ✅ |
| Unique/custom components | Minimize | **8 custom** (rest COTS/standard) | ✅ |
| Assembly steps | Minimize | **18 steps** (barrel+receiver+scope+stock+cylinder) | ✅ |
| Subfunctions vs SkyWall | 35% fewer | **23 vs ~35** estimated | ✅ |

### Part Count Breakdown

| Assembly | Custom Parts | Standard Parts | COTS Parts | Total |
|----------|-------------|----------------|------------|-------|
| Barrel assembly | 3 (barrel, muzzle, front sight) | 8 (fasteners, O-rings) | 0 | 11 |
| Receiver assembly | 2 (housing, side panel) | 6 (fasteners) | 0 | 8 |
| Trigger group | 4 (trigger, sear, safety, inertia) | 6 (springs, pins) | 0 | 10 |
| Gas system | 0 | 4 (fittings, lines) | 3 (regulator, valve, relief) | 7 |
| Scope assembly | 1 (housing) | 4 (fasteners, glass) | 3 (LRF, LCD, PCB) | 8 |
| Stock assembly | 1 (stock body) | 6 (adjust mechanism) | 1 (pad) | 8 |
| Cylinder assembly | 0 | 2 (mount, clamp) | 1 (cylinder) | 3 |
| Projectile (×1) | 2 (body, fins) | 5 (net, weights, chute, timer, baro) | 0 | 7 |
| Misc hardware | 0 | 10 (sling, screws, pins) | 0 | 10 |
| **TOTAL** | **13** | **51** | **8** | **72** |

**Simplicity Score: 6/6 = 100%** ✅

## R.3 Rule 3: SAFETY (An toàn)

### Safety Architecture (3-Level)

```
VDC-100 SAFETY ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

LEVEL 1: MECHANICAL (always active, no power needed)
├── Manual safety lever (blocks trigger linkage mechanically)
│   └── Positive engagement: detent at SAFE, must lift to move to ARM
├── Inertia lock (drop safety — blocks sear if acceleration >50g)
│   └── Proof: mass on spring, threshold calibrated to 50g
├── Spring-return valve (fail-safe: spring closes if mechanism fails)
│   └── Valve cannot stay open without continuous trigger pressure
└── Breech interlock (cannot fire if breech not fully closed)
    └── Mechanical pin engagement confirms closed state

LEVEL 2: ELECTRICAL (requires battery)
├── Arm switch (enables solenoid power circuit)
│   └── Located left side, thumb-operated, separate from safety
├── Low battery cutoff (prevents partial valve opening)
│   └── Below 3.2V → solenoid disabled → cannot fire
└── LRF safety (laser enable only when scope powered)
    └── Class 1 eye-safe by design; additional enable switch

LEVEL 3: INDICATION (operator awareness)
├── Armed LED: RED = armed (dangerous), GREEN = safe
│   └── Visible from firing position, top of scope
├── Pressure gauge: analog, 0-350 bar
│   └── Visible from firing position, rear of receiver
├── Breech indicator: visual tab (red = open, flush = closed)
│   └── Tactile check possible with gloves
└── Ready indicator: scope display shows "READY" when all conditions met
    └── Requires: breech closed + pressure OK + armed + battery OK

FAIL-SAFE BEHAVIORS:
═══════════════════════════════════════════════════════════════════════════════
• Power loss       → Solenoid de-energizes → Valve spring-closes → CANNOT FIRE
• Safety engaged   → Trigger blocked mechanically → CANNOT FIRE
• Breech open      → Interlock pin disengaged → CANNOT FIRE
• Drop event       → Inertia lock engages → CANNOT FIRE
• Low battery      → Solenoid circuit open → CANNOT FIRE
• All failures     → System defaults to SAFE state (fail-safe design)
═══════════════════════════════════════════════════════════════════════════════
```

### MIL-STD-882E Risk Assessment

| Hazard | Severity | Probability | Risk Level | Mitigation | Residual Risk |
|--------|----------|-------------|------------|------------|---------------|
| Accidental discharge | III Critical | E Improbable | **LOW** | 3-level safety (mech+elec+indication) | Acceptable |
| Pneumatic rupture | I Catastrophic | E Improbable | **MEDIUM** | Relief valve @ 350 bar, 3× SF | Acceptable |
| Muzzle obstruction | II Critical | D Remote | **MEDIUM** | Physical interlock, operator training | Acceptable |
| Laser eye injury | III Marginal | E Improbable | **LOW** | Class 1 COTS module | Acceptable |
| Drop-induced fire | III Critical | E Improbable | **LOW** | Inertia lock + mechanical safety | Acceptable |
| Pinch/crush | IV Negligible | C Occasional | **LOW** | Smooth contours, recessed mechanisms | Acceptable |

**No HIGH or SERIOUS risks remain after mitigation.**

**Safety Score: 6/6 criteria met = 100%** ✅

## R.4 Rule 4: ECONOMY (Kinh tế)

| Factor | Target | VDC-100 Design | Status |
|--------|--------|----------------|--------|
| Unit production cost | ≤$2,000 | **$1,750** estimated | ✅ |
| Cost vs import (SkyWall) | ≤20% | **5.8%** ($1,750 / $30,000) | ✅ |
| Selling price | ≤$6,000 | **~$5,400** (3× markup) | ✅ |
| Local content | ≥70% | **72%** by value | ✅ |
| Tooling investment | ≤$20,000 | **$15,000** (mold + fixtures) | ✅ |
| Material cost ratio | <30% of production | **26%** ($460 / $1,750) | ✅ |
| No exotic materials | Standard, available | Al 6061, PA66, SS 316 — all standard | ✅ |

**Economy Score: 7/7 = 100%** ✅

## R.5 Basic Rules Summary

| Rule | Criteria Met | Score | Status |
|------|-------------|-------|--------|
| Clarity | 6/6 | 100% | ✅ |
| Simplicity | 6/6 | 100% | ✅ |
| Safety | 6/6 | 100% | ✅ |
| Economy | 7/7 | 100% | ✅ |
| **Overall** | **25/25** | **100%** | **PASS** |

---

# STEP A: ARCHITECTURE DEFINITION

## A.1 Purpose

Define overall system structure, module boundaries, and interfaces.

## A.2 Module Architecture

```
VDC-100 MODULAR ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│                        VDC-100 SYSTEM (7.8 kg)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  MODULE 1: SCOPE ASSEMBLY (FRU — Field Replaceable Unit)                    │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ LRF Module │ Reticle (glass) │ LCD Display │ PCB │ Battery │ LED     │ │
│  │ (COTS)     │ (etched)        │ (COTS)      │     │ (18650) │ (status)│ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│     Interface I-01: Picatinny rail mount (4× M4 cross-bolts)               │
│     ↕ Electrical: None to main system (self-contained)                     │
│                                                                             │
│  MODULE 2: BARREL ASSEMBLY (Semi-permanent — depot swap)                    │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ Barrel Tube │ Muzzle Brake │ Front Sight │ Breech Chamber │ Latch    │ │
│  │ (Al 6061)   │ (Al 6061)    │ (Al 6061)   │ (Al 6061)      │ (SS)    │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│     Interface I-02: Thread + shoulder to receiver (M100×1.5)                │
│     Interface I-03: Gas port from valve to breech (6mm OD tube)             │
│                                                                             │
│  MODULE 3: RECEIVER ASSEMBLY (Core — not field-replaceable)                 │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ Housing    │ Trigger │ Safety │ Sear │ Inertia │ Valve │ Regulator   │ │
│  │ (Al 6061)  │ (17-4PH)│ (17-4PH)│(17-4PH)│(17-4PH)│(COTS) │ (COTS)  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│     Interface I-04: 2× M6 bolts to stock                                   │
│     Interface I-05: Gas line from cylinder (8mm OD, AN fitting)             │
│                                                                             │
│  MODULE 4: STOCK ASSEMBLY (FRU — Field Replaceable Unit)                    │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ Stock Body (PA66-GF30) │ Adjustment Mechanism │ Recoil Pad (rubber)   │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│     Interface I-04: 2× M6 bolts to receiver                                │
│                                                                             │
│  MODULE 5: GAS SYSTEM (FRU — Quick-swap cylinder)                           │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ HPA Cylinder (0.5L, 300 bar) │ Fill Valve │ Gauge │ Quick-Release     │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│     Interface I-05: AN fitting to receiver regulator                        │
│     Interface I-06: Quick-release clamp to stock                            │
│                                                                             │
│  MODULE 6: PROJECTILE (Consumable)                                          │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │ Body │ Fins │ Net + Weights │ Timer │ Baro │ Parachute │ Drogue      │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│     Interface I-07: Drop-in breech chamber (100mm bore, clearance fit)      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
```

## A.3 Interface Control Document (ICD)

| Interface | Between | Type | Specification | Critical Param | Drawing Ref |
|-----------|---------|------|---------------|----------------|-------------|
| **I-01** | Scope ↔ Receiver | Mechanical | MIL-STD-1913 Picatinny, 4× M4×12 cross-bolts | Parallelism ≤0.5 mrad to bore | DWG-001 |
| **I-02** | Barrel ↔ Receiver | Mechanical | M100×1.5 thread + 110mm shoulder face | Concentricity ≤0.1mm to bore | DWG-002 |
| **I-03** | Valve ↔ Barrel | Pneumatic | 6mm OD SS tube, AN-4 fitting, 150 bar rated | Leak-free @ 150 bar | DWG-003 |
| **I-04** | Receiver ↔ Stock | Mechanical | 2× M6×20 hex socket bolts, locating pins | Align ±0.5mm | DWG-004 |
| **I-05** | Cylinder ↔ Receiver | Pneumatic | 8mm OD SS tube, AN-6 fitting, 350 bar rated | Leak-free @ 350 bar | DWG-005 |
| **I-06** | Cylinder ↔ Stock | Mechanical | Quick-release band clamp, 60mm OD | Release force 10-20 N | DWG-006 |
| **I-07** | Projectile ↔ Barrel | Clearance fit | 98.0±0.3mm OD into 100.0+0.5/-0mm bore | Clearance 1.7-2.8mm | DWG-007 |

## A.4 Assembly Sequence (DfX#8)

```
VDC-100 ASSEMBLY SEQUENCE
═══════════════════════════════════════════════════════════════════════════════

FACTORY ASSEMBLY (18 steps, ~2 hours)
─────────────────────────────────────

Step 1-4:  RECEIVER SUB-ASSEMBLY
├── 1. Install trigger group into receiver housing (4× pins)
├── 2. Install safety mechanism (2× pins + spring)
├── 3. Install valve assembly (thread-in + O-ring seal)
└── 4. Install regulator (thread-in + O-ring seal)

Step 5-7:  BARREL SUB-ASSEMBLY
├── 5. Press-fit front sight onto barrel
├── 6. Thread muzzle brake onto barrel
└── 7. Install breech latch mechanism (2× pins + spring)

Step 8-9:  BARREL-RECEIVER INTEGRATION
├── 8. Thread barrel into receiver (M100×1.5 + shoulder)
└── 9. Torque to 50 Nm, verify bore alignment

Step 10-12: STOCK INTEGRATION
├── 10. Install adjustment mechanism into stock body
├── 11. Attach recoil pad (adhesive + 2× screws)
└── 12. Bolt stock to receiver (2× M6 + locating pins)

Step 13-15: SCOPE SUB-ASSEMBLY
├── 13. Install LRF module into scope housing
├── 14. Install reticle glass + LCD display
└── 15. Install PCB + battery holder + LED

Step 16-17: FINAL INTEGRATION
├── 16. Mount scope onto Picatinny rail (4× M4 cross-bolts)
└── 17. Connect gas line from cylinder mount to regulator

Step 18:   FINAL QC
└── 18. Function test: pressure, trigger, safety, scope, bore alignment

FIELD ASSEMBLY (Operator level)
───────────────────────────────
• Attach cylinder: Quick-release clamp (30 sec)
• Load projectile: Open breech → drop in → close (8 sec)
• Power scope: Press ON button (1 sec)

═══════════════════════════════════════════════════════════════════════════════
```

## A.5 Information Flow Architecture

```
VDC-100 INFORMATION FLOW
═══════════════════════════════════════════════════════════════════════════════

OPERATOR INPUT                    SYSTEM STATE                    OPERATOR OUTPUT
──────────────                    ────────────                    ───────────────

Eyes (detect drone) ═══►  ┌─────────────────────┐
                          │ SCOPE ASSEMBLY       │  ═══► Reticle view
LRF button (thumb) ═══►  │ ├─ LRF → Range      │  ═══► Range display
                          │ ├─ Reticle → Aim     │  ═══► Aim solution
                          │ └─ LCD → Status      │  ═══► Ready/not ready
                          └─────────────────────┘

Safety lever (thumb) ═══► ┌─────────────────────┐
                          │ TRIGGER GROUP        │  ═══► Armed LED (red/green)
Trigger (finger) ════════►│ ├─ Safety → Block   │
                          │ ├─ Trigger → Sear    │
                          │ └─ Sear → Valve      │  ═══► FIRE (gas release)
                          └─────────────────────┘

                          ┌─────────────────────┐
                          │ GAS SYSTEM           │  ═══► Pressure gauge
                          │ ├─ Cylinder (300 bar)│
                          │ ├─ Regulator (100 bar)│
                          │ └─ Relief (350 bar)  │  ═══► Audible vent (if over-pressure)
                          └─────────────────────┘

Breech handle (hand) ═══► ┌─────────────────────┐
                          │ BARREL/BREECH        │  ═══► Breech indicator (red tab)
                          │ └─ Latch → Lock      │
                          └─────────────────────┘

FEEDBACK LOOPS (Systems Thinking):
• R1: Success → Confidence → Better aim → More success (reinforcing)
• B1: Low pressure → Reduced velocity → Miss → Check gauge → Refill (balancing)
• B2: Recoil → Flinch → Miss → Training corrects stance (balancing)

═══════════════════════════════════════════════════════════════════════════════
```

---

# STEP D: DESIGN STRUCTURE

## D.1 Purpose

Define detailed structural configuration with load analysis, form optimization, and integration.

## D.2 Structural Analysis

### D.2.1 Barrel — Pressure Vessel Analysis

```
BARREL STRESS ANALYSIS
═══════════════════════════════════════════════════════════════════════════════

                    ┌────────────────────────────────────┐
                    │         BARREL CROSS-SECTION        │
                    │                                    │
                    │    ┌──────────────────────────┐    │
                    │    │                          │    │
                    │    │    BORE (ID = 100mm)      │    │
                    │    │                          │    │
                    │    │    P = 100 bar = 10 MPa  │    │
                    │    │                          │    │
                    │    └──────────────────────────┘    │
                    │                                    │
                    │    WALL: t = 5mm                   │
                    │    OD = 110mm                      │
                    │                                    │
                    └────────────────────────────────────┘

Hoop Stress (thin-wall approximation):
  σ_hoop = P × r_inner / t
  σ_hoop = 10 MPa × 50mm / 5mm = 100 MPa

Axial Stress (closed-end):
  σ_axial = P × r_inner / (2 × t)
  σ_axial = 10 MPa × 50mm / (2 × 5mm) = 50 MPa

Von Mises Equivalent:
  σ_vm = √(σ_h² - σ_h×σ_a + σ_a²) = √(100² - 100×50 + 50²) = 86.6 MPa

Safety Factor:
  SF = σ_yield / σ_vm = 276 / 86.6 = 3.19×

Result: SF = 3.19× > 2.5× (target)  ✅ PASS

Peak transient (150 bar, 0.05 sec):
  σ_vm_peak = 86.6 × 1.5 = 130 MPa
  SF_peak = 276 / 130 = 2.12×  > 2.0× (dynamic)  ✅ PASS

═══════════════════════════════════════════════════════════════════════════════
```

### D.2.2 Receiver — Recoil Load Analysis

| Load Case | Force/Moment | Duration | Stress | Material Allowable | SF |
|-----------|-------------|----------|--------|-------------------|-----|
| Recoil (axial) | 750 N (15 Ns / 0.02s) | 20 ms | 12 MPa (at barrel thread) | 276 MPa | 23× |
| Drop impact (muzzle) | 1200 N (150g × 0.8 kg) | 5 ms | 45 MPa (at barrel junction) | 276 MPa | 6.1× |
| Drop impact (corner) | 1500 N (150g × 1.0 kg) | 5 ms | 55 MPa (at stock junction) | 276 MPa | 5.0× |
| Sling load (static) | 78 N (7.8 kg × g) | Continuous | 5 MPa (at sling point) | 276 MPa | 55× |

**All load cases pass with SF > 2.0×.** Receiver is over-designed for static loads — this is intentional for drop impact and fatigue margins.

### D.2.3 Weight Budget (Detailed)

| Assembly | Component | Material | Mass (g) | % Total |
|----------|-----------|----------|----------|---------|
| **Barrel** | Barrel tube (800mm, 100ID/110OD) | Al 6061-T6 | 1,400 | 17.9% |
| | Muzzle brake | Al 6061-T6 | 200 | 2.6% |
| | Front sight | Al 6061-T6 | 50 | 0.6% |
| | Breech chamber + latch | Al + SS | 300 | 3.8% |
| | Picatinny rail | Al 6061-T6 | 150 | 1.9% |
| | **Barrel subtotal** | | **2,100** | **26.9%** |
| **Receiver** | Housing | Al 6061-T6 | 600 | 7.7% |
| | Side panel | Al 6061-T6 | 100 | 1.3% |
| | Trigger group (4 parts) | 17-4 PH SS | 70 | 0.9% |
| | Springs + pins | SS 302/316 | 30 | 0.4% |
| | Fast-acting valve | COTS | 120 | 1.5% |
| | Regulator | COTS | 200 | 2.6% |
| | Fittings + lines | SS | 80 | 1.0% |
| | **Receiver subtotal** | | **1,200** | **15.4%** |
| **Scope** | Housing | Al 6061-T6 | 200 | 2.6% |
| | LRF module | COTS | 120 | 1.5% |
| | Reticle glass | Glass | 30 | 0.4% |
| | LCD display | COTS | 40 | 0.5% |
| | PCB + electronics | Mixed | 30 | 0.4% |
| | Battery (18650) | Li-ion | 50 | 0.6% |
| | Lens caps, LED, misc | Mixed | 30 | 0.4% |
| | **Scope subtotal** | | **500** | **6.4%** |
| **Stock** | Stock body | PA66-GF30 | 400 | 5.1% |
| | Adjustment mechanism | Steel | 80 | 1.0% |
| | Recoil pad | Rubber | 60 | 0.8% |
| | Sling swivel (rear) | SS 316 | 20 | 0.3% |
| | **Stock subtotal** | | **560** | **7.2%** |
| **Gas system** | HPA cylinder (0.5L, full) | Al + CF + air | 1,200 | 15.4% |
| | Fill valve | Brass | 30 | 0.4% |
| | Pressure gauge | COTS | 50 | 0.6% |
| | Quick-release mount | Al | 80 | 1.0% |
| | **Gas subtotal** | | **1,360** | **17.4%** |
| **Projectile** | VDC-P40E (loaded) | Mixed | 450 | 5.8% |
| **Hardware** | Fasteners (all) | SS 316 | 120 | 1.5% |
| | O-rings (all) | EPDM | 10 | 0.1% |
| | Sling + strap | Nylon | 60 | 0.8% |
| | Sling swivel (front) | SS 316 | 20 | 0.3% |
| | Relief valve | COTS | 50 | 0.6% |
| | **Hardware subtotal** | | **260** | **3.3%** |
| | | | | |
| | **TOTAL (loaded)** | | **6,430** | **82.4%** |
| | **Margin (10%)** | | **643** | **8.2%** |
| | **Contingency (5%)** | | **322** | **4.1%** |
| | **TARGET** | | **≤7,800** | **100%** |
| | **PROJECTED** | | **7,395** | **94.8%** |

**Status:** Projected weight 7,395g with 15% margin = well within 8,000g MUST. ✅

## D.3 Form Development Features

| Feature | Purpose | Implementation |
|---------|---------|----------------|
| Barrel ribs | Stiffness without weight | 4 longitudinal ribs, 2mm high, on barrel OD |
| Receiver web | Reduce mass | Internal web structure, 3mm walls with ribs |
| Scope housing ribs | Dust/rain deflection | External ribs direct water away from lenses |
| Trigger guard | Gloved operation | Oversized guard (CUA-ERG-04), 25mm clearance |
| Drainage holes | Water evacuation | 3× Ø4mm at receiver low points |
| Cable routing | Protection | Internal channels in receiver for gas lines |

---

# STEP D — META-LEARNING SKILLS APPLIED

| Skill | Step | Application |
|-------|------|-------------|
| Principle → Application | P | Force flow → direct axial recoil path; Self-help → tapered breech |
| Checklist verification | R | 4 basic rules with 25 criteria systematically checked |
| Abstraction + Decomposition | A | System → 6 modules → 72 parts with defined interfaces |
| Analysis → Synthesis | D | Stress analysis → optimized wall thickness; mass budget → form features |

---

# DOCUMENT LINKS

- [[03_embodiment/RISM_requirements_materials|RISM: Requirements & Materials]]
- [[03_embodiment/DECS_detail_evaluation|DECS: Detail & Evaluation]] ← NEXT
- [[02_conceptual/function_structure|Function Structure (Phase 2)]]
- [[01_requirements/requirements_list|Requirements List]]

---

*This PRAD document follows Steps P-R-A-D of the 15-step RISM-PRAD-DECS-OCP embodiment design methodology, establishing design principles, basic rules compliance, system architecture, and structural configuration for VDC-100 Enhanced.*
