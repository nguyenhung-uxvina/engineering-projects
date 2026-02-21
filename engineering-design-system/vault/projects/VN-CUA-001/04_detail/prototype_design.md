---
project: VN-CUA-001
designation: VDC-33
type: prototype_design
phase: 4
version: 2.0
created: 2026-02-05
updated: 2026-02-08
status: complete
methodology: Pahl & Beitz Phase 4 - Detail Design
scale: "1:3 (bore diameter)"
total_3d_parts: 14
total_print_time: "~48 hours"
total_filament: "~790g"
---

# PHASE 4 — PROTOTYPE DESIGN (VDC-33)
## VDC-33 Scale Prototype Design Specifications

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Purpose:** Validate pneumatic system, safety interlocks, projectile stability
**Phase 3 Input:** [[03_embodiment/OCP_optimization_production|Gate 3 PASSED (15/15)]]

---

# 1. PROTOTYPE STRATEGY

## 1.1 Why Scale Prototype?

| Risk Area | What VDC-33 Validates | Full-Scale Risk if Skipped |
|-----------|----------------------|---------------------------|
| **Pneumatic performance** | V(P) curve, gas efficiency | Wrong barrel/valve sizing → redesign |
| **Safety architecture** | 3-level interlock logic | Safety failure → injury liability |
| **Projectile stability** | Fin geometry selection | Tumbling projectiles → zero accuracy |
| **Recoil management** | Impulse measurement + scaling | Excessive recoil → unusable in field |
| **Valve timing** | Optimal dwell time | Wasted gas or low velocity |
| **Manufacturing feasibility** | 3D print tolerances, assembly | Interference fits, bad tolerances |

**Cost justification:** $800 prototype vs. $15,000+ full-scale first article
**Schedule justification:** 6 weeks (prototype) vs. 16 weeks (full-scale tooling)

## 1.2 Scale Selection Rationale

```
SCALING APPROACH
═══════════════════════════════════════════════════════════════════════════════

                VDC-33                          VDC-100
                (Prototype)                     (Production)
                ──────────                      ──────────
Bore:           32mm ───── ×3.1 ─────────────── 100mm
Barrel:         260mm ──── ×3.1 ─────────────── 800mm
Projectile:     58g (tennis ball) ── ×7.8 ────── 450g (net + parachute)
Pressure:       60-100 bar ── ×1.0 ────────────── 100 bar
Velocity:       30-40 m/s ── ×1.0 ─────────────── 35-45 m/s
Energy:         ~35 J ───── ×10 ─────────────── ~360 J

KEY INSIGHT: Same pressure → similar velocity at any scale
             This allows direct pneumatic system validation

═══════════════════════════════════════════════════════════════════════════════
```

## 1.3 Design Decisions Captured in Prototype

| Design Aspect | VDC-33 Implementation | What It Validates | VDC-100 Impact |
|---------------|----------------------|-------------------|----------------|
| **Pneumatic architecture** | HPA → Regulator → Solenoid → Barrel | Pressure/velocity relationship | Valve sizing, chamber volume |
| **Valve type** | Fast-acting solenoid (PE/Dye) | Response time <15ms | Solenoid spec for production |
| **Safety interlocks** | 3-level (mech + electrical + SW) | Logic correctness, fail-safe | Safety architecture confirmed |
| **Projectile stabilization** | 3 fin configurations tested | Optimal fin geometry | Fin design for VDC-P40E |
| **Trigger mechanism** | Electronic (μswitch → Arduino → MOSFET) | Safety logic | Production trigger design |
| **Gas consumption** | Measured at multiple pressures | Shots per fill prediction | Cylinder sizing confirmation |

---

# 2. VDC-33 SPECIFICATIONS

## 2.1 System Parameters

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    VDC-33 SCALE PROTOTYPE SPECIFICATIONS                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  SCALE: 1:3 (Bore Diameter Ratio)                                            ║
║                                                                               ║
║  ┌─────────────────────────┬─────────────────┬─────────────────────────────┐ ║
║  │ Parameter               │ VDC-33          │ VDC-100 (Full Scale)        │ ║
║  ├─────────────────────────┼─────────────────┼─────────────────────────────┤ ║
║  │ Bore diameter           │ 32mm            │ 100mm                       │ ║
║  │ Barrel length           │ 260mm           │ 800mm                       │ ║
║  │ Projectile mass         │ ~58g            │ ~450g                       │ ║
║  │ Operating pressure      │ 60-100 bar      │ 100 bar                     │ ║
║  │ Target velocity         │ 30-40 m/s       │ 40 m/s                      │ ║
║  │ Muzzle energy           │ ~35 J           │ ~360 J                      │ ║
║  │ Projectile type         │ Tennis ball     │ Net + Parachute             │ ║
║  │ HPA tank                │ 48ci (0.8L)     │ 0.5L (300 bar)             │ ║
║  │ Weight (loaded)         │ ~2.5 kg         │ ≤8 kg                      │ ║
║  └─────────────────────────┴─────────────────┴─────────────────────────────┘ ║
║                                                                               ║
║  PURPOSE: Validate pneumatic system, safety interlocks, projectile stability ║
║  BUDGET:  ~$800 (basic) / ~$1,000 (with test equipment)                     ║
║  BUILD:   ~4-6 weeks including procurement                                   ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## 2.2 Subsystem Architecture

```
VDC-33 SYSTEM ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

                    ┌────────────────────────────────────────────────────────┐
                    │                    TARGETING (simplified)               │
                    │              Iron sights / optional red dot             │
                    └────────────────────────┬───────────────────────────────┘
                                             │
    ┌────────────────────────────────────────┴──────────────────────────────┐
    │                          LAUNCH ASSEMBLY                              │
    │                                                                       │
    │  ┌──────────┐  ┌──────────────────────┐  ┌────────────────────────┐  │
    │  │ MUZZLE   │  │ BARREL (PVC/Al)      │  │ BREECH ADAPTER (3D)   │  │
    │  │ CAP (3D) │  │ 32mm ID × 260mm      │  │ O-ring sealed         │  │
    │  └──────────┘  └──────────────────────┘  └────────────────────────┘  │
    │                                                                       │
    └────────────────────────────────────────┬──────────────────────────────┘
                                             │
    ┌────────────────────────────────────────┴──────────────────────────────┐
    │                       RECEIVER ASSEMBLY (3D printed)                   │
    │                                                                       │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────┐  │
    │  │ RECEIVER     │  │ VALVE MOUNT  │  │ RAIL MOUNT   │  │ GRIP +  │  │
    │  │ BODY (P01)   │  │ (P02)        │  │ (P06)        │  │TRIGGER  │  │
    │  └──────────────┘  └──────────────┘  └──────────────┘  │GUARD    │  │
    │                                                         └─────────┘  │
    └────────────────────────────────────────┬──────────────────────────────┘
                                             │
    ┌────────────────────────────────────────┴──────────────────────────────┐
    │                         GAS SYSTEM                                    │
    │                                                                       │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
    │  │ HPA TANK │→│REGULATOR │→│SOLENOID  │→│ BREECH   │            │
    │  │ 0.8L     │  │ Ninja    │  │ 12V NC   │  │ CHAMBER  │            │
    │  │ 207 bar  │  │ SLP      │  │ <10ms    │  │          │            │
    │  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
    │                                                                       │
    │  SAFETY: Relief valve (120 bar), pressure gauge (0-160 bar)          │
    │                                                                       │
    └────────────────────────────────────────┬──────────────────────────────┘
                                             │
    ┌────────────────────────────────────────┴──────────────────────────────┐
    │                     ELECTRONICS & SAFETY                              │
    │                                                                       │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
    │  │ BATTERY  │→│ ARDUINO  │→│ MOSFET   │→│SOLENOID  │            │
    │  │ 3S 18650 │  │ NANO     │  │ IRF520   │  │ DRIVE    │            │
    │  │ 11.1V    │  │          │  │          │  │          │            │
    │  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
    │                                                                       │
    │  INPUTS:  ARM switch │ SAFETY switch │ TRIGGER switch                │
    │  OUTPUTS: Red/Green LED │ Buzzer │ Voltmeter display                 │
    │                                                                       │
    └────────────────────────────────────────┬──────────────────────────────┘
                                             │
    ┌────────────────────────────────────────┴──────────────────────────────┐
    │                         STOCK ASSEMBLY                                │
    │                                                                       │
    │  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐   │
    │  │ STOCK BODY   │  │ TANK CLAMP   │  │ RECOIL PAD + ADJ RAIL   │   │
    │  │ (P09)        │  │ (P10)        │  │                          │   │
    │  └──────────────┘  └──────────────┘  └──────────────────────────┘   │
    │                                                                       │
    └───────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
```

---

# 3. 3D PRINTED COMPONENTS

## 3.1 Parts Summary

| Part # | Name | Material | Weight | Print Time | Infill | Priority |
|--------|------|----------|--------|------------|--------|----------|
| P01 | Receiver Body | PETG | 200g | 12h | 40% | HIGH |
| P02 | Valve Mount | PETG | 50g | 3h | 40% | HIGH |
| P03 | Breech Adapter | PETG | 40g | 2h | 60% | HIGH |
| P04 | Muzzle Cap | PETG | 20g | 1h | 30% | MEDIUM |
| P05 | Barrel Clamp (x2) | PETG | 40g | 2h | 50% | HIGH |
| P06 | Rail Mount | PETG | 30g | 2h | 40% | MEDIUM |
| P07 | Trigger Guard | PETG | 20g | 1h | 30% | MEDIUM |
| P08 | Grip | PETG | 60g | 4h | 30% | MEDIUM |
| P09 | Stock Body | PETG | 150g | 10h | 30% | HIGH |
| P10 | Tank Clamp | PETG | 80g | 5h | 40% | HIGH |
| P11 | Fin Set A (x4) | PLA | 20g | 1.5h | 100% | HIGH |
| P12 | Fin Set B (x4) | PLA | 20g | 1.5h | 100% | HIGH |
| P13 | Fin Set C (x4) | PLA | 20g | 1.5h | 100% | HIGH |
| P14 | Weighted Nose (x4) | PLA | 40g | 2h | 100% | MEDIUM |
| | **TOTAL** | | **~790g** | **~48h** | | |

## 3.2 Design Guidelines

```
3D PRINT DESIGN RULES
═══════════════════════════════════════════════════════════════════════════════

WALL THICKNESS:
• Minimum wall: 2.0mm (structural parts)
• Pressure-bearing: 4.0mm minimum
• Non-structural: 1.5mm acceptable

TOLERANCES:
• Hole diameters: +0.3mm (clearance fit)
• Shaft diameters: -0.2mm (clearance fit)
• Press-fit holes: +0.0mm (may need reaming)
• Mating surfaces: +/-0.2mm

OVERHANGS:
• Maximum unsupported: 45 degrees
• Use chamfers instead of fillets on bottom faces
• Add support blockers for internal features

FASTENER FEATURES:
• Heat-set inserts: Hole = insert OD + 0.2mm
• M4 insert: 5.6mm hole x 6mm deep
• M3 insert: 4.2mm hole x 5mm deep

ORIENTATION:
• Print with largest flat surface on bed
• Avoid supports on sealing surfaces
• Orient holes perpendicular to layers when possible

═══════════════════════════════════════════════════════════════════════════════
```

## 3.3 Print Settings

| Parameter | PETG (Structural) | PLA (Fins/Nose) |
|-----------|-------------------|-----------------|
| Nozzle temp | 240C | 210C |
| Bed temp | 80C | 60C |
| Layer height | 0.2mm | 0.2mm (fins: 0.15mm) |
| Infill | 25-60% (per part) | 100% (solid) |
| Perimeters | 4 | 3 |
| Top/bottom layers | 5 | 4 |
| Speed | 50mm/s | 60mm/s |
| Supports | As noted per part | None |
| Brim | 5mm | 3mm |

## 3.4 Critical Part Specifications

### P01: Receiver Body (Main Housing)

**Function:** Main structural housing for valve, trigger, barrel interface

```
P01 RECEIVER BODY - ORTHOGRAPHIC VIEWS
═══════════════════════════════════════════════════════════════════════════════

TOP VIEW
─────────────────────────────────────────────────────────────────────────────
                          120mm
        <--------------------------------------------->
        +---------------------------------------------+  ^
        |  O         RAIL SLOTS          O            |  |
        |  M4      +--------------+        M4         |  |
        |          |              |                    |  |  60mm
        |   O      |  O36 bore    |         O         |  |
        |          |     O        |                    |  |
        |          +--------------+                    |  |
        +---------------------------------------------+  v

SIDE VIEW (Section A-A)
─────────────────────────────────────────────────────────────────────────────
                          120mm
        <--------------------------------------------->
        +---------------------------------------------+  ^
        |  (top wall 8mm)                              |  |
        |   +-------------------------------------+    |  |
        |   |                                     |    |  |
        |   |         BARREL BORE                 |    |  |  70mm
        |   |           O36mm                     |    |  |
        |   |                                     |    |  |
        |   +-------------------------------------+    |  |
        |  (bottom wall 10mm)                          |  |
        +---------------------------------------------+  v
        |<-->|
         12mm (wall thickness)

FRONT VIEW (Breech face)
─────────────────────────────────────────────────────────────────────────────
                           60mm
              <----------------------------->
              +-----------------------------+  ^
              |                             |  |
              |     +---------------+       |  |
              |     |               |       |  |
              |     |   O36mm       |       |  |  70mm
              |     |     O bore    |       |  |
              |     |               |       |  |
              |     +---------------+       |  |
              |                             |  |
              |   O  GAS PORT O8  O         |  |
              +-----------------------------+  v

═══════════════════════════════════════════════════════════════════════════════
```

**P01 Critical Dimensions:**

| Feature | Dimension | Tolerance | Notes |
|---------|-----------|-----------|-------|
| Overall length | 120mm | +/-0.5mm | |
| Overall width | 60mm | +/-0.5mm | |
| Overall height | 70mm | +/-0.5mm | |
| Barrel bore | O36mm | +0.3/-0mm | Clearance for 32mm + clamp |
| Gas port | O8mm | +/-0.2mm | For 6mm push-fit + adapter |
| Valve cavity | 60x40x35mm | +/-0.5mm | Fits solenoid valve |
| M4 insert holes (6x) | O5.6mm x 6mm | +0.1mm | Heat-set inserts |
| M6 stock holes (2x) | O6.5mm thru | +0.2mm | Clearance for M6 bolt |
| Wall thickness | 12mm min | — | Structural requirement |
| Rail slot width | 21mm | +/-0.1mm | MIL-STD-1913 Picatinny |

**Print:** Bottom face (stock interface) on bed. Supports for valve cavity ceiling and gas channel. 40% infill, 4 perimeters. ~12h, ~200g PETG.

### P03: Breech Adapter (Pressure Seal)

**Function:** Seals barrel to receiver, contains O-ring groove

```
P03 BREECH ADAPTER - SECTION VIEW
═══════════════════════════════════════════════════════════════════════════════

                    FRONT (barrel side)         REAR (receiver side)
                           |                           |
                    +----------------------------------+
                    | (solid)                          |
                    |  +----------------------------+  |
                    |  |                            |  |
       O-RING -----+  |  +--+              +--+   |  |
       GROOVE       |  |  |OO|   BORE      |OO|   |  |
       (2 places)   |  |  |OO|   O32mm     |OO|   |  |
                    |  |  +--+              +--+   |  |
                    |  |                            |  |
                    |  +----------------------------+  |
                    | (solid)                          |
                    +----------------------------------+
                    |<----------- 50mm --------------->|
                    |<10>|                        |<10>|
                      flange                        flange

═══════════════════════════════════════════════════════════════════════════════
```

**P03 Critical Dimensions:**

| Feature | Dimension | Tolerance | Notes |
|---------|-----------|-----------|-------|
| Overall length | 50mm | +/-0.3mm | |
| Flange OD | O50mm | +/-0.3mm | |
| Bore ID | O32.3mm | +0.2/-0mm | Clearance for 32mm barrel |
| O-ring groove ID | 35mm | +/-0.1mm | For 40x3mm O-ring |
| O-ring groove width | 3.5mm | +/-0.1mm | Standard AS568 |
| O-ring groove depth | 2.5mm | +/-0.1mm | 20% compression |
| M4 holes (4x) | O4.3mm thru | +0.1mm | For attachment |

**Print:** Flange face down, no supports. 60% infill. Post-process O-ring groove with file if needed.

### P09: Stock Body

**Function:** Main stock structure with adjustment rail and tank space

**P09 Critical Dimensions:**

| Feature | Dimension | Tolerance |
|---------|-----------|-----------|
| Overall length | 200mm | +/-0.5mm |
| Overall width | 50mm | +/-0.3mm |
| Overall height | 60mm | +/-0.3mm |
| Rail slot | 20x100mm | +/-0.3mm |
| Tank cavity | 40x40x150mm | +/-0.5mm |
| M6 receiver holes (2x) | O6.5mm thru | +0.2mm |
| M4 pad mount holes (2x) | O5.6mm insert | +0.1mm |
| Wall thickness | 10mm | — |

**Print:** Longest flat face down. 30% infill. ~10h, ~150g PETG.

### P11-P13: Fin Sets (Stability Test Configurations)

```
FIN CONFIGURATIONS
═══════════════════════════════════════════════════════════════════════════════

P11: FIN SET A              P12: FIN SET B              P13: FIN SET C
4 fins, 15 deg cant         4 fins, 10 deg cant         6 fins, 0 deg (straight)

    END VIEW                    END VIEW                    END VIEW
       |                           |                       \ | /
       |                           |                        \|/
    ---+---                     ---+---                  ----+----
       |                           |                        /|\
       |                           |                       / | \

Max spin (~20 rps)          Med spin (~12 rps)          No spin (drag only)
High drag penalty           Moderate drag               Lowest drag
Best for stability          Balanced                    Baseline comparison

COMMON COLLAR DESIGN:
─────────────────────────────────────────────────────────────────────────────
Collar OD:    30mm (fits 32mm barrel with clearance)
Collar length: 40mm
Ball pocket:  O59mm x 30mm deep (holds tennis ball snugly)

═══════════════════════════════════════════════════════════════════════════════
```

| Feature | P11 (15 deg) | P12 (10 deg) | P13 (straight) |
|---------|--------------|--------------|----------------|
| Number of fins | 4 | 4 | 6 |
| Cant angle | 15 deg | 10 deg | 0 deg |
| Fin height | 25mm | 25mm | 20mm |
| Fin root chord | 15mm | 15mm | 12mm |
| Fin tip chord | 10mm | 10mm | 8mm |
| Fin thickness | 2mm | 2mm | 2mm |
| Total span | 70mm | 70mm | 60mm |

**Print:** PLA, 100% infill (solid), 0.15mm layer height. Fins vertical for strength.

### P14: Weighted Nose

**Function:** CG forward shift for stability, contains steel BB fill (~20g)

| Feature | Dimension |
|---------|-----------|
| Overall length | 50mm |
| Max diameter | 30mm |
| Ball socket | O58mm hemisphere |
| BB cavity | O15mm x 20mm deep |
| BB fill mass | ~20g (steel BBs) |
| Wall thickness | 3mm min |

**Assembly:** Print → Fill cavity with steel BBs → Seal with epoxy → Press tennis ball into socket.

---

# 4. HEAT-SET INSERT INSTALLATION

```
HEAT-SET INSERT GUIDE
═══════════════════════════════════════════════════════════════════════════════

TOOLS:
• Soldering iron with conical tip (or dedicated insert tip)
• Temperature: 220-240C for PETG
• M4 inserts: O5.6mm x 6mm brass
• M3 inserts: O4.2mm x 5mm brass

PROCEDURE:
    Step 1: Place insert     Step 2: Heat & press     Step 3: Result

         +---+                    +---+                    +---+
         |   | insert             |###| iron tip           |   |
         |   |                    |vvv|                    |   |
    -----+---+-----          ----+---+-----          -----+---+-----
    |    |   |    |          |   |   |    |          |    |###|    |
    |    |   |    |          |   |   |    |          |    |###|    |
    |    |   |    |          |   |   |    |          |    +---+    |
    |    +---+    |          |   +---+    |          |             |

    • Align insert           • 3-5 sec heat           • Flush with surface
    • Don't push yet         • Press slowly            • Let cool 30 sec

TIPS:
• Insert should be flush or 0.5mm below surface
• If crooked, reheat and adjust while warm
• Test thread with screw before final assembly

INSERT COUNT PER PART:
─────────────────────────────────────────────────────────────────────────────
P01 Receiver:     6x M4
P02 Valve Mount:  4x M4
P08 Grip:         2x M4
P09 Stock:        2x M4
P10 Tank Clamp:   4x M4
─────────────────────────────────────────────────────────────────────────────
TOTAL:           18x M4 inserts + spare

═══════════════════════════════════════════════════════════════════════════════
```

---

# 5. ASSEMBLY DRAWINGS

## 5.1 Receiver Assembly (Exploded View)

```
RECEIVER ASSEMBLY - EXPLODED VIEW
═══════════════════════════════════════════════════════════════════════════════

                              P06 RAIL MOUNT
                                   |
                         M4x12 (4x)|
                              v    v
                    +---------------------------+
                    |                           |
                    |    P01 RECEIVER BODY      |
                    |                           |
            +-------+---------------------------+-------+
            |       |                           |       |
    P05     |       |                           |       |     P05
    BARREL  |   <---+---------------------------+--->   |   BARREL
    CLAMP   |       |                           |       |   CLAMP
    (upper) |       |                           |       |   (lower)
            +-------+---------------------------+-------+
                    |    ^                      |
                    |    | M4x20 (4x)           |
                    |    |                      |
                    | P03 BREECH ADAPTER        |
                    |         |                 |
                    |         | O-rings (2x)    |
                    |         v                 |
                    |    +---------+            |
                    |    |         |            |
                    +----+ BARREL  +------------+
                         |  TUBE   |
                         | (PVC)   |
                         +---------+

                    |         |                 |
                    |    P02 VALVE MOUNT        |
                    |         |                 |
                    |    M4x12 (4x)             |
                    |         v                 |
                    |    +---------+            |
                    |    |SOLENOID |            |
                    |    |  VALVE  |            |
                    |    +---------+            |
                    |                           |
                    +---------------------------+
                              |
                              | M6x30 (2x)
                              v
                    +---------------------------+
                    |                           |
                    |    P09 STOCK BODY         |
                    |                           |
                    +---------------------------+

═══════════════════════════════════════════════════════════════════════════════
```

## 5.2 Projectile Assembly

```
PROJECTILE ASSEMBLY
═══════════════════════════════════════════════════════════════════════════════

         P14 WEIGHTED NOSE         TENNIS BALL          P11/P12/P13
         (with BB fill)              (58mm)              FIN COLLAR

              /\
             /  \                 +---------+
            / BB \               |         |        +---------------+
           / FILL \              |  TENNIS |        |               |
          / CAVITY \   press     |  BALL   |  snap  |   FIN COLLAR  |
         +----------+  fit  --> |         |  fit -->|   + FINS      |
         |  SOCKET  |           |         |        |               |
         +----------+           +---------+        +---------------+

         ASSEMBLED:
         ─────────────────────────────────────────────────────────────

              NOSE            BALL              FINS
               \               |                 |
                \    +---------+--------+--------+
                 \  / +---------+ +-------------+ \
                  \/  | * * *   | |    FINS     |  |
                  /\  | (BBs)   | |             |  |
                 /  \ +---------+ +-------------+ /
                /    +---------+--------+--------+
               /               |                 |

         <--- 50mm ---><-- 58mm --><--- 40mm --->

         TOTAL LENGTH: ~148mm
         TOTAL MASS: ~80g (with BBs)
         CG: Forward of center (stable flight)

═══════════════════════════════════════════════════════════════════════════════
```

---

# 6. ASSEMBLY SEQUENCE

## 6.1 Phase 1: Pneumatic System (Day 1-2)

```
PNEUMATIC ASSEMBLY
═══════════════════════════════════════════════════════════════════════════════

Step 1: Tank + Regulator
+-------------------+
|  HPA TANK         |
|  (PNE-001)        |---- Hand-tighten regulator (PNE-002)
+--------+----------+      Use PTFE tape on threads
         |
Step 2: Add Pressure Gauge
         |
    +----+----+
    |   TEE   |---- Install gauge (PNE-005) on branch
    |(PNE-007)|
    +----+----+
         |
Step 3: Add Relief Valve
    +----+----+
    |   TEE   |---- Install relief valve (PNE-012) on branch
    |(PNE-007)|
    +----+----+
         |
Step 4: Connect to Solenoid
    +----+----+
    |SOLENOID |---- Mount solenoid in receiver (RCV-002)
    |(PNE-006)|
    +----+----+
         |
Step 5: Connect to Breech
    +----+----+
    | BREECH  |---- Seal with O-ring (BAR-006)
    |(BAR-003)|
    +---------+

TEST: Pressurize to 50 bar, check all connections with soapy water
      No bubbles = good seal. Hold 5 min, no pressure drop.

═══════════════════════════════════════════════════════════════════════════════
```

## 6.2 Phase 2: Mechanical Assembly (Day 2-3)

| Step | Action | Tools | Check |
|------|--------|-------|-------|
| 1 | Install heat-set inserts into all 3D parts | Soldering iron 230C | Thread test each |
| 2 | Attach barrel clamps to receiver (P05→P01) | M4x20 SHCS | Barrel bore aligned |
| 3 | Insert barrel tube and secure | Hand-tighten clamps | Barrel straight, no wobble |
| 4 | Install breech adapter with O-rings | M4x12 SHCS | O-rings seated, no pinch |
| 5 | Mount valve assembly to receiver (P02→P01) | M4x12 SHCS | Gas ports aligned |
| 6 | Attach stock to receiver (P09→P01) | M6x30 bolts | Solid connection |
| 7 | Install tank clamp on stock (P10→P09) | M4x12 SHCS | Tank fits snugly |
| 8 | Install trigger guard and grip (P07+P08→P01) | M4x12 SHCS | Trigger pocket clear |
| 9 | Mount rail (P06→P01) | M4x12 SHCS | Picatinny aligned |

## 6.3 Phase 3: Electronics (Day 3-4)

```
WIRING DIAGRAM
═══════════════════════════════════════════════════════════════════════════════

                    +-----------------------------------------------+
                    |                 BATTERY PACK                   |
                    |           3S 18650 (11.1V nominal)             |
                    |                 with BMS                       |
                    +---------------------+-------------------------+
                                          |
                         +----------------+----------------+
                         |           12V BUS               |
                         |                                 |
              +----------+----------+          +-----------+---------+
              |     DC-DC 5V        |          |    VOLTMETER        |
              |     (ELE-011)       |          |    (ELE-014)        |
              +----------+----------+          +---------------------+
                         |
              +----------+----------+
              |     ARDUINO NANO    |
              |      (ELE-001)      |
              +----------+----------+
                         |
    +--------------------+--------------------+--------------------+
    |                    |                    |                    |
+---+---+           +----+----+          +----+----+          +----+----+
| ARM   |           | SAFETY  |          | TRIGGER |          |  LED    |
|SWITCH |           | SWITCH  |          | SWITCH  |          |(ELE-007)|
|(D2)   |           |  (D3)   |          |  (D4)   |          |(D5,D6)  |
+-------+           +---------+          +---------+          +---------+

                         | D7 output
              +----------+----------+
              |    MOSFET MODULE     |
              |      (ELE-003)      |
              +----------+----------+
                         | 12V switched
              +----------+----------+
              |   SOLENOID VALVE    |
              |      (PNE-006)      |
              +---------------------+

═══════════════════════════════════════════════════════════════════════════════
```

**Arduino Safety Logic (Pseudocode):**

```
SAFETY INTERLOCK LOGIC
═══════════════════════════════════════════════════════════════════════════════

INPUTS:
  ARM_SWITCH    → D2  (HIGH = armed)
  SAFETY_SWITCH → D3  (LOW = safety off / fire enabled)
  TRIGGER       → D4  (HIGH = pressed)
  BATTERY_V     → A0  (voltage divider)

OUTPUTS:
  MOSFET_GATE   → D7  (HIGH = solenoid open)
  LED_RED       → D5  (armed indication)
  LED_GREEN     → D6  (safe indication)
  BUZZER        → D8  (low battery warning)

LOGIC:
  IF battery_voltage < 9.5V:
    → Block all firing, buzzer ON
    → LED: FLASH RED

  IF ARM=ON AND SAFETY=OFF (fire position):
    → LED: RED (armed)
    → IF TRIGGER pressed:
      → Open solenoid for DWELL_MS (adjustable: 8-25ms)
      → Close solenoid
      → Wait for trigger release (anti-rapid-fire)

  ELSE:
    → LED: GREEN (safe)
    → Block solenoid regardless of trigger

FAIL-SAFE BEHAVIORS:
  Power loss     → Solenoid NC (closed) → No fire
  Arduino reset  → All outputs LOW → No fire
  Wire break     → Input reads LOW → Blocks fire
  MOSFET fail    → Fuse on 12V line → Limits current

═══════════════════════════════════════════════════════════════════════════════
```

## 6.4 Phase 4: Integration & Test (Day 4-5)

| Step | Action | Verification |
|------|--------|-------------|
| 1 | Connect all wiring per diagram | Continuity test each connection |
| 2 | Upload Arduino firmware | LED pattern confirms upload |
| 3 | Bench test: all 8 state permutations (no pressure) | Only S8 fires solenoid |
| 4 | Low-pressure test (30 bar, foam projectile) | Solenoid actuates, no leaks |
| 5 | Increase to 50 bar, verify safety blocks | SAFE position blocks fire |
| 6 | Increase to operating pressure (60-80 bar) | Stable pressure, consistent firing |
| 7 | First projectile test (tennis ball) | Projectile exits cleanly |
| 8 | Chronograph velocity check | Record baseline V @ standard P |

---

# 7. STL EXPORT & PRINT QUEUE

## 7.1 File Naming Convention

```
VDC33_P01_receiver_body_v1.stl
VDC33_P02_valve_mount_v1.stl
VDC33_P03_breech_adapter_v1.stl
VDC33_P04_muzzle_cap_v1.stl
VDC33_P05_barrel_clamp_v1.stl
VDC33_P06_rail_mount_v1.stl
VDC33_P07_trigger_guard_v1.stl
VDC33_P08_grip_v1.stl
VDC33_P09_stock_body_v1.stl
VDC33_P10_tank_clamp_v1.stl
VDC33_P11_fin_set_A_15deg_v1.stl
VDC33_P12_fin_set_B_10deg_v1.stl
VDC33_P13_fin_set_C_straight_v1.stl
VDC33_P14_weighted_nose_v1.stl
```

## 7.2 Print Queue (Optimized Batch Order)

```
RECOMMENDED PRINT ORDER
═══════════════════════════════════════════════════════════════════════════════

BATCH 1: Critical path (Day 1-2)                              ~16h
─────────────────────────────────────────────────────────────────────────────
  P01 Receiver Body      PETG    200g    12h    Start first (longest)
  P03 Breech Adapter     PETG     40g     2h    Critical for assembly
  P05 Barrel Clamps (x2) PETG     40g     2h    Critical for assembly

BATCH 2: Stock assembly (Day 2)                                ~15h
─────────────────────────────────────────────────────────────────────────────
  P09 Stock Body         PETG    150g    10h    Second longest
  P10 Tank Clamp         PETG     80g     5h

BATCH 3: Small parts (Day 3)                                   ~11h
─────────────────────────────────────────────────────────────────────────────
  P02 Valve Mount        PETG     50g     3h
  P06 Rail Mount         PETG     30g     2h
  P07 Trigger Guard      PETG     20g     1h
  P08 Grip               PETG     60g     4h
  P04 Muzzle Cap         PETG     20g     1h

BATCH 4: Projectiles (Day 4)                                   ~6.5h
─────────────────────────────────────────────────────────────────────────────
  P11 Fin Set A (x4)     PLA      20g    1.5h
  P12 Fin Set B (x4)     PLA      20g    1.5h
  P13 Fin Set C (x4)     PLA      20g    1.5h
  P14 Weighted Nose (x4) PLA      40g     2h

─────────────────────────────────────────────────────────────────────────────
TOTAL PRINT TIME:                        ~48 hours (4 days continuous)
TOTAL FILAMENT:                          ~790g (PETG: 690g, PLA: 100g)
FILAMENT COST:                           ~$20 (own printer) / $50-80 (service)

═══════════════════════════════════════════════════════════════════════════════
```

## 7.3 Pre-Print Checklist

```
PRE-PRINT VERIFICATION
═══════════════════════════════════════════════════════════════════════════════

PER STL FILE:
  [ ] STL file loads without errors in slicer
  [ ] Model is watertight (no holes in mesh)
  [ ] Correct orientation for printing
  [ ] Supports generated where needed
  [ ] Estimated print time acceptable
  [ ] Estimated filament usage acceptable
  [ ] Bed adhesion (brim/raft) configured
  [ ] Infill percentage matches spec table

GENERAL:
  [ ] PETG spool dry (dehumidifier or oven-dried)
  [ ] Bed leveled and clean
  [ ] First layer calibration verified
  [ ] Enough filament for batch

═══════════════════════════════════════════════════════════════════════════════
```

---

# 8. SAFETY WARNINGS

```
SAFETY REQUIREMENTS FOR PROTOTYPE TESTING
═══════════════════════════════════════════════════════════════════════════════

1. ALWAYS wear safety glasses during any pressurized testing
2. NEVER point at people, even with tennis ball projectiles
3. TEST outdoors or in adequately sized indoor space (>10m range)
4. ENSURE backstop can safely stop projectiles
5. VERIFY all fittings sealed before pressurizing
6. START with low pressure (30 bar), increase gradually
7. KEEP bystanders at minimum 5m distance during testing
8. STORE depressurized when not in use
9. INSPECT O-rings and seals before each session
10. DOCUMENT all tests for safety review

EMERGENCY: If leak detected, point muzzle safe direction,
           allow to depressurize naturally, then repair.

ENERGY NOTE: At 100 bar, 32mm bore = ~25 kgf (245N) on projectile
             Tennis ball at 40 m/s has 46 J kinetic energy
             Treat as projectile weapon — full safety protocols apply

═══════════════════════════════════════════════════════════════════════════════
```

---

# 9. DOCUMENT LINKS

## Phase 4 Documents
- [[04_detail/prototype_BOM_procurement|BOM & Procurement Guide]]
- [[04_detail/experiment_procedures|Experiment Procedures]]
- [[04_detail/scale_up_production|Scale-Up & Production Design]]
- [[04_detail/gate_review|Gate 4A/4B Review]]

## Phase 3 Reference
- [[03_embodiment/OCP_optimization_production|Phase 3: OCP + Gate 3]]
- [[03_embodiment/DECS_detail_evaluation|Phase 3: Layout & DfX]]
- [[03_embodiment/PRAD_principles_architecture|Phase 3: Architecture]]
- [[03_embodiment/RISM_requirements_materials|Phase 3: Materials]]

## Supporting Documents
- [[VN-CUA-001_product_spec|Product Specification v1.4]]
- [[VN-CUA-001_Systems_Analysis|Systems Analysis]]

---

# 10. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **2.0** | **2026-02-08** | **Restructured from monolithic P4 + 3D designs files. Consolidated prototype design specifications, 3D print specs (14 parts), assembly sequence, wiring diagram, safety logic into single comprehensive document.** |
| 1.0 | 2026-02-05 | Initial prototype design. |

---

*This prototype design follows Pahl & Beitz Phase 4 with risk-reduction prototyping before full-scale commitment.*

**Next:** [[04_detail/prototype_BOM_procurement|BOM & Procurement]] → [[04_detail/experiment_procedures|Experiments]] → [[04_detail/scale_up_production|Scale-Up]]
