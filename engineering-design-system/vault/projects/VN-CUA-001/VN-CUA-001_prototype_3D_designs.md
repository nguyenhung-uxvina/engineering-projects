---
project: VN-CUA-001
designation: VDC-33
type: 3d_print_specifications
version: 1.0
created: 2026-02-05
status: draft
cad_software: Fusion 360 / FreeCAD / SolidWorks
total_parts: 12
total_print_time: ~48 hours
total_filament: ~800g
---

# VN-CUA-001: VDC-33 3D PRINT DESIGN SPECIFICATIONS
## CAD Models for Scale Prototype Components

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Date:** 2026-02-05

---

## 1. DESIGN OVERVIEW

### 1.1 Parts List

| Part # | Name | Material | Weight | Print Time | Priority |
|--------|------|----------|--------|------------|----------|
| P01 | Receiver Body | PETG | 200g | 12h | HIGH |
| P02 | Valve Mount | PETG | 50g | 3h | HIGH |
| P03 | Breech Adapter | PETG | 40g | 2h | HIGH |
| P04 | Muzzle Cap | PETG | 20g | 1h | MEDIUM |
| P05 | Barrel Clamp (×2) | PETG | 40g | 2h | HIGH |
| P06 | Rail Mount | PETG | 30g | 2h | MEDIUM |
| P07 | Trigger Guard | PETG | 20g | 1h | MEDIUM |
| P08 | Grip | PETG | 60g | 4h | MEDIUM |
| P09 | Stock Body | PETG | 150g | 10h | HIGH |
| P10 | Tank Clamp | PETG | 80g | 5h | HIGH |
| P11 | Fin Set A (×4) | PLA | 20g | 1.5h | HIGH |
| P12 | Fin Set B (×4) | PLA | 20g | 1.5h | HIGH |
| P13 | Fin Set C (×4) | PLA | 20g | 1.5h | HIGH |
| P14 | Weighted Nose (×4) | PLA | 40g | 2h | MEDIUM |
| | **TOTAL** | | **~790g** | **~48h** | |

### 1.2 General Design Rules

```
3D PRINT DESIGN GUIDELINES
═══════════════════════════════════════════════════════════════════════════

WALL THICKNESS:
• Minimum wall: 2.0mm (structural parts)
• Pressure-bearing: 4.0mm minimum
• Non-structural: 1.5mm acceptable

TOLERANCES:
• Hole diameters: +0.3mm (for clearance fit)
• Shaft diameters: -0.2mm (for clearance fit)
• Press-fit holes: +0.0mm (will need reaming)
• Mating surfaces: ±0.2mm

OVERHANGS:
• Maximum unsupported: 45°
• Use chamfers instead of fillets on bottom faces
• Add support blockers for internal features

FASTENER FEATURES:
• Heat-set inserts: Hole = insert OD + 0.2mm
• M4 insert: Ø5.6mm hole × 6mm deep
• M3 insert: Ø4.2mm hole × 5mm deep

ORIENTATION:
• Print with largest flat surface on bed
• Avoid supports on sealing surfaces
• Orient holes perpendicular to layers when possible

═══════════════════════════════════════════════════════════════════════════
```

### 1.3 Print Settings

| Parameter | PETG | PLA |
|-----------|------|-----|
| Nozzle temp | 240°C | 210°C |
| Bed temp | 80°C | 60°C |
| Layer height | 0.2mm | 0.2mm |
| Infill (structural) | 40% | 100% (fins) |
| Infill (non-structural) | 25% | 30% |
| Perimeters | 4 | 3 |
| Top/bottom layers | 5 | 4 |
| Speed | 50mm/s | 60mm/s |
| Supports | As noted | None |
| Brim | 5mm | 3mm |

---

## 2. PART SPECIFICATIONS

---

### P01: RECEIVER BODY

**Function:** Main structural housing for valve, trigger, and barrel interface

```
P01 RECEIVER BODY - ISOMETRIC VIEW
═══════════════════════════════════════════════════════════════════════════

                         RAIL MOUNT INTERFACE
                              (top)
                    ┌─────────────────────────┐
                   ╱│                         │╲
                  ╱ │    M4 insert holes (4×) │ ╲
                 ╱  │         ○   ○           │  ╲
                ╱   │         ○   ○           │   ╲
               ╱    └─────────────────────────┘    ╲
              ╱                                      ╲
             ╱     ┌─────────────────────────────┐    ╲
            ╱      │                             │     ╲
           ╱       │      BARREL BORE            │      ╲
          │        │        Ø36mm                │       │
          │        │         ○                   │       │
          │        │                             │       │
  BREECH  │        │      VALVE CAVITY           │       │ TRIGGER
  FACE    │        │       60×40×35mm            │       │ POCKET
          │        │      ┌─────────┐            │       │
          │        │      │         │            │       │
          │        │      │  ○      │            │       │
          │        │      │ valve   │            │       │
          │        └──────┴─────────┴────────────┘       │
          │                                              │
           ╲       GAS CHANNEL Ø8mm                     ╱
            ╲           ───────                       ╱
             ╲                                       ╱
              ╲    ┌─────────────────────────┐     ╱
               ╲   │   STOCK INTERFACE       │   ╱
                ╲  │   M6 holes (2×)         │  ╱
                 ╲ │      ○         ○        │ ╱
                  ╲└─────────────────────────┘╱
                   ╲                         ╱
                    ╲───────────────────────╱
                           (bottom)

═══════════════════════════════════════════════════════════════════════════
```

**P01 DIMENSIONS:**

```
P01 RECEIVER BODY - ORTHOGRAPHIC VIEWS
═══════════════════════════════════════════════════════════════════════════

TOP VIEW
─────────────────────────────────────────────────────────────────────────────
                          120mm
        ←─────────────────────────────────────────→
        ┌─────────────────────────────────────────┐  ↑
        │  ○         RAIL SLOTS          ○       │  │
        │  M4      ┌────────────┐        M4      │  │
        │          │            │                │  │  60mm
        │   ○      │  Ø36 bore  │         ○      │  │
        │          │     ○      │                │  │
        │          └────────────┘                │  │
        └─────────────────────────────────────────┘  ↓

SIDE VIEW (Section A-A)
─────────────────────────────────────────────────────────────────────────────
                          120mm
        ←─────────────────────────────────────────→
        ┌─────────────────────────────────────────┐  ↑
        │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ 8mm (top wall)
        ├─────────────────────────────────────────┤  │
        │                                         │  │
        │   ┌─────────────────────────────────┐   │  │
        │   │                                 │   │  │
        │   │         BARREL BORE             │   │  │  70mm
        │   │           Ø36mm                 │   │  │  total
        │   │                                 │   │  │
        │   └─────────────────────────────────┘   │  │
        │                                         │  │
        │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ 10mm (bottom)
        └─────────────────────────────────────────┘  ↓
        │←─────→│
          12mm
        (wall thickness)

FRONT VIEW (Breech face)
─────────────────────────────────────────────────────────────────────────────
                           60mm
              ←───────────────────────→
              ┌───────────────────────┐  ↑
              │                       │  │
              │     ┌───────────┐     │  │
              │     │           │     │  │
              │     │   Ø36mm   │     │  │  70mm
              │     │     ○     │     │  │
              │     │   bore    │     │  │
              │     └───────────┘     │  │
              │                       │  │
              │   ○  GAS PORT Ø8  ○   │  │
              └───────────────────────┘  ↓

═══════════════════════════════════════════════════════════════════════════
```

**P01 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance | Notes |
|---------|-----------|-----------|-------|
| Overall length | 120mm | ±0.5mm | |
| Overall width | 60mm | ±0.5mm | |
| Overall height | 70mm | ±0.5mm | |
| Barrel bore | Ø36mm | +0.3/-0mm | Clearance for 32mm + clamp |
| Gas port | Ø8mm | ±0.2mm | For 6mm push-fit + adapter |
| Valve cavity | 60×40×35mm | ±0.5mm | Fits solenoid valve |
| M4 insert holes (6×) | Ø5.6mm × 6mm | +0.1mm | Heat-set inserts |
| M6 stock holes (2×) | Ø6.5mm thru | +0.2mm | Clearance for M6 bolt |
| Wall thickness | 12mm min | — | Structural requirement |
| Rail slot width | 21mm | ±0.1mm | MIL-STD-1913 Picatinny |

**P01 PRINT ORIENTATION:**

```
RECOMMENDED PRINT ORIENTATION
═══════════════════════════════════════════════════════════════════════════

                    ▲ Z (build direction)
                    │
                    │     ┌─────────────────┐
                    │     │   TOP SURFACE   │
                    │     │   (rail mount)  │
                    │     │                 │
                    │     │   RECEIVER      │
                    │     │   BODY          │
                    │     │                 │
                    │     │                 │
        ────────────┼─────┴─────────────────┴───────── Build plate
                    │
                    │

Print with BOTTOM face (stock interface) on build plate
• Barrel bore horizontal (perpendicular to Z)
• Rail surface at top (best surface finish)
• Supports needed for: valve cavity ceiling, gas channel

═══════════════════════════════════════════════════════════════════════════
```

**P01 PRINT SETTINGS:**
- Material: PETG
- Infill: 40%
- Perimeters: 4
- Supports: Yes (for valve cavity)
- Estimated time: 12 hours
- Estimated weight: 200g

---

### P02: VALVE MOUNT

**Function:** Secures solenoid valve in receiver cavity

```
P02 VALVE MOUNT - VIEWS
═══════════════════════════════════════════════════════════════════════════

TOP VIEW                              SIDE VIEW
─────────────────────────────        ─────────────────────────────
      55mm                                  55mm
←─────────────────→                  ←─────────────────→
┌─────────────────┐  ↑               ┌─────────────────┐  ↑
│ ○             ○ │  │               │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ 5mm
│                 │  │               ├─────────────────┤  │
│  ┌───────────┐  │  │ 35mm          │   ┌───────┐     │  │
│  │  VALVE    │  │  │               │   │ VALVE │     │  │ 30mm
│  │  POCKET   │  │  │               │   │POCKET │     │  │
│  │  Ø25×25   │  │  │               │   └───────┘     │  │
│  └───────────┘  │  │               │                 │  │
│ ○             ○ │  │               └─────────────────┘  ↓
└─────────────────┘  ↓

                                     FEATURES:
                                     • 4× M4 insert holes (corners)
                                     • Ø25mm × 25mm deep valve pocket
                                     • Ø8mm gas ports (in/out)
                                     • Cable routing slot

═══════════════════════════════════════════════════════════════════════════
```

**P02 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance |
|---------|-----------|-----------|
| Overall | 55×35×30mm | ±0.3mm |
| Valve pocket | Ø25mm × 25mm deep | +0.3mm |
| M4 insert holes (4×) | Ø5.6mm × 6mm | +0.1mm |
| Gas port in | Ø8mm | ±0.2mm |
| Gas port out | Ø8mm | ±0.2mm |
| Cable slot | 10×5mm | ±0.5mm |

---

### P03: BREECH ADAPTER

**Function:** Seals barrel to receiver, contains O-ring groove

```
P03 BREECH ADAPTER - SECTION VIEW
═══════════════════════════════════════════════════════════════════════════

                    FRONT (barrel side)         REAR (receiver side)
                           ↓                           ↓
                    ┌──────────────────────────────────┐
                    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                    │▓▓┌────────────────────────────┐▓▓│
                    │▓▓│                            │▓▓│
       O-RING ──────│▓▓│  ┌──┐              ┌──┐   │▓▓│
       GROOVE       │▓▓│  │OO│   BORE       │OO│   │▓▓│
       (2 places)   │▓▓│  │OO│   Ø32mm      │OO│   │▓▓│
                    │▓▓│  └──┘              └──┘   │▓▓│
                    │▓▓│                            │▓▓│
                    │▓▓└────────────────────────────┘▓▓│
                    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                    └──────────────────────────────────┘
                    │←─────────── 50mm ───────────────→│

                    │←10→│                        │←10→│
                      flange                        flange

DIMENSIONS:
─────────────────────────────────────────────────────────────────────────────
Overall length:     50mm
Overall diameter:   Ø50mm (flange)
Bore diameter:      Ø32.3mm (+0.3mm for barrel clearance)
Flange thickness:   10mm each end
O-ring groove:      ID 35mm, width 3.5mm, depth 2.5mm (for Ø40×3mm O-ring)

═══════════════════════════════════════════════════════════════════════════
```

**P03 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance | Notes |
|---------|-----------|-----------|-------|
| Overall length | 50mm | ±0.3mm | |
| Flange OD | Ø50mm | ±0.3mm | |
| Bore ID | Ø32.3mm | +0.2/-0mm | Clearance for 32mm barrel |
| O-ring groove ID | 35mm | ±0.1mm | For 40×3mm O-ring |
| O-ring groove width | 3.5mm | ±0.1mm | Standard AS568 |
| O-ring groove depth | 2.5mm | ±0.1mm | 20% compression |
| M4 holes (4×) | Ø4.3mm thru | +0.1mm | For attachment |

**P03 PRINT NOTES:**
- Print with flange face down
- No supports needed
- 60% infill for pressure resistance
- Post-process O-ring groove with file if needed

---

### P05: BARREL CLAMP (×2)

**Function:** Secures barrel tube to receiver

```
P05 BARREL CLAMP - VIEWS
═══════════════════════════════════════════════════════════════════════════

TOP VIEW                              FRONT VIEW
─────────────────────────────        ─────────────────────────────
      40mm                                  40mm
←─────────────────→                  ←─────────────────→
┌─────────────────┐  ↑               ┌─────────────────┐  ↑
│ ○             ○ │  │               │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │
│                 │  │               │▓▓            ▓▓│  │
│    ╭───────╮    │  │ 30mm          │▓▓  ╭─────╮  ▓▓│  │ 25mm
│    │ Ø35   │    │  │               │▓▓  │ Ø35 │  ▓▓│  │
│    │ half  │    │  │               │▓▓  │     │  ▓▓│  │
│    ╰───────╯    │  │               │▓▓  ╰─────╯  ▓▓│  │
│                 │  │               │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │
│ ○             ○ │  │               └─────────────────┘  ↓
└─────────────────┘  ↓

ASSEMBLY: Two clamps sandwich barrel, bolt through to receiver

═══════════════════════════════════════════════════════════════════════════
```

**P05 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance |
|---------|-----------|-----------|
| Overall | 40×30×25mm | ±0.3mm |
| Half-bore radius | R17.5mm | +0.2mm |
| M4 thru holes (4×) | Ø4.5mm | +0.2mm |
| Clamping surface | Smooth | — |

---

### P08: GRIP

**Function:** Ergonomic pistol grip with trigger pocket

```
P08 GRIP - VIEWS
═══════════════════════════════════════════════════════════════════════════

SIDE VIEW                             FRONT VIEW
─────────────────────────────        ─────────────────────────────
         50mm                               30mm
    ←───────────→                     ←───────────→
    ┌─────────────┐  ↑                ┌───────────┐  ↑
    │▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ 15mm          │▓▓▓▓▓▓▓▓▓▓▓│  │
    │  MOUNT FACE │  │ (mount)       │▓▓▓▓▓▓▓▓▓▓▓│  │
    ├─────────────┤  │                ├───────────┤  │
    │             │  │                │           │  │
    │   TRIGGER   │  │                │           │  │
    │   GUARD     │  │                │           │  │
   ╱│   POCKET    │  │ 80mm          │           │  │ 80mm
  ╱ │             │  │               │           │  │
 │  │             │  │               │           │  │
 │  │             │  │               │           │  │
 │   ╲            │  │                ╲          │  │
  ╲   ╲───────────┘  ↓                 ╲─────────┘  ↓
   ╲
    ╲ 15° angle

FEATURES:
• Top face mounts to receiver (M4 inserts)
• Trigger pocket: 25×15×40mm
• 15° grip angle for ergonomics
• Textured surface (print texture OK)
• Wire channel for trigger switch

═══════════════════════════════════════════════════════════════════════════
```

**P08 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance |
|---------|-----------|-----------|
| Overall height | 80mm | ±0.5mm |
| Overall width | 30mm | ±0.3mm |
| Overall depth | 50mm | ±0.3mm |
| Mount face | 50×30mm | ±0.3mm |
| Grip angle | 15° | ±2° |
| Trigger pocket | 25×15×40mm | ±0.5mm |
| M4 insert holes (2×) | Ø5.6×6mm | +0.1mm |
| Wire channel | Ø6mm | ±0.3mm |

---

### P09: STOCK BODY

**Function:** Main stock structure with adjustment rail

```
P09 STOCK BODY - VIEWS
═══════════════════════════════════════════════════════════════════════════

SIDE VIEW
─────────────────────────────────────────────────────────────────────────────
                              200mm
        ←─────────────────────────────────────────────────→
        ┌─────────────────────────────────────────────────┐  ↑
        │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │
        │  ┌────────────────────────────────────────────┐ │  │
        │  │          ADJUSTMENT RAIL SLOT              │ │  │ 60mm
        │  │          (20mm wide × 100mm long)          │ │  │
        │  └────────────────────────────────────────────┘ │  │
        │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │
        └─────────────────────────────────────────────────┘  ↓
        │←───→│                                     │←───→│
         40mm                                         30mm
       (receiver                                     (pad
        interface)                                   mount)

TOP VIEW
─────────────────────────────────────────────────────────────────────────────
                              200mm
        ←─────────────────────────────────────────────────→
        ┌─────────────────────────────────────────────────┐  ↑
        │  ○                                          ○   │  │
        │  M6                                         M4  │  │
        │                                                 │  │ 50mm
        │  ○                                          ○   │  │
        │  M6                                         M4  │  │
        └─────────────────────────────────────────────────┘  ↓

CROSS SECTION (A-A)
─────────────────────────────────────────────────────────────────────────────
              50mm
        ←───────────→
        ┌───────────┐  ↑
        │▓▓▓▓▓▓▓▓▓▓▓│  │ 10mm
        ├───────────┤  │
        │           │  │
        │  ┌─────┐  │  │ 60mm
        │  │TANK │  │  │
        │  │SPACE│  │  │
        │  └─────┘  │  │
        │           │  │
        │▓▓▓▓▓▓▓▓▓▓▓│  │ 10mm
        └───────────┘  ↓

═══════════════════════════════════════════════════════════════════════════
```

**P09 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance |
|---------|-----------|-----------|
| Overall length | 200mm | ±0.5mm |
| Overall width | 50mm | ±0.3mm |
| Overall height | 60mm | ±0.3mm |
| Rail slot | 20×100mm | ±0.3mm |
| Tank cavity | 40×40×150mm | ±0.5mm |
| M6 receiver holes (2×) | Ø6.5mm thru | +0.2mm |
| M4 pad mount holes (2×) | Ø5.6mm insert | +0.1mm |
| Wall thickness | 10mm | — |

---

### P10: TANK CLAMP

**Function:** Secures HPA tank to stock, quick-release design

```
P10 TANK CLAMP - VIEWS
═══════════════════════════════════════════════════════════════════════════

TOP VIEW                              SIDE VIEW
─────────────────────────────        ─────────────────────────────
      80mm                                  80mm
←─────────────────→                  ←─────────────────→
┌─────────────────┐  ↑               ┌─────────────────┐  ↑
│ ○             ○ │  │               │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ 10mm
│   ╭─────────╮   │  │               ├─────────────────┤  │
│   │         │   │  │ 60mm          │   ╭─────────╮   │  │
│   │  Ø60    │   │  │               │   │  TANK   │   │  │ 50mm
│   │  tank   │   │  │               │   │  Ø60    │   │  │
│   │  bore   │   │  │               │   ╰─────────╯   │  │
│   ╰─────────╯   │  │               │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│  │ 10mm
│ ○             ○ │  │               └─────────────────┘  ↓
└─────────────────┘  ↓

STRAP SLOT                           QUICK-RELEASE MECHANISM
─────────────────                    ─────────────────────────
│     ┌───┐     │                    • Velcro strap through slots
│     │   │     │                    • Or: cam lever clamp
│     │ S │     │                    • Must hold 1.2kg tank
│     │ L │     │                    • Easy one-hand release
│     │ O │     │
│     │ T │     │
│     └───┘     │

═══════════════════════════════════════════════════════════════════════════
```

**P10 CRITICAL DIMENSIONS:**

| Feature | Dimension | Tolerance |
|---------|-----------|-----------|
| Overall | 80×60×70mm | ±0.3mm |
| Tank bore | Ø60mm | +0.5mm |
| Strap slots (2×) | 30×5mm | ±0.3mm |
| M4 mount holes (4×) | Ø5.6mm insert | +0.1mm |

---

### P11-P13: FIN SETS

**Function:** Stabilize projectile in flight, induce spin

```
FIN CONFIGURATIONS
═══════════════════════════════════════════════════════════════════════════

P11: FIN SET A - 4 fins, 15° cant
─────────────────────────────────────────────────────────────────────────────

    END VIEW                          SIDE VIEW (single fin)
    ─────────                         ─────────────────────
         │                                    ╱│
         │                                   ╱ │
    ─────┼─────                             ╱  │ 25mm
         │                                 ╱   │
         │                                ╱    │
                                         ╱─────┘
    4 fins at 90° spacing                  15mm
    15° cant angle                        (root)


P12: FIN SET B - 4 fins, 10° cant
─────────────────────────────────────────────────────────────────────────────

    END VIEW                          SIDE VIEW (single fin)
    ─────────                         ─────────────────────
         │                                   ╱│
         │                                  ╱ │
    ─────┼─────                            ╱  │ 25mm
         │                                ╱   │
         │                               ╱    │
                                        ╱─────┘
    4 fins at 90° spacing                 15mm
    10° cant angle                       (root)


P13: FIN SET C - 6 fins, 0° (straight)
─────────────────────────────────────────────────────────────────────────────

    END VIEW                          SIDE VIEW (single fin)
    ─────────                         ─────────────────────
       ╲ │ ╱                                  │
        ╲│╱                                   │
    ─────┼─────                               │ 20mm
        ╱│╲                                   │
       ╱ │ ╲                                  │
                                         ─────┘
    6 fins at 60° spacing                 12mm
    0° cant (straight)                   (root)

═══════════════════════════════════════════════════════════════════════════
```

**FIN COLLAR DESIGN (Common to all):**

```
FIN COLLAR - SECTION VIEW
═══════════════════════════════════════════════════════════════════════════

                    ┌───────────────────────────────────┐
                    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                    │▓▓┌─────────────────────────────┐▓▓│
                    │▓▓│                             │▓▓│
                    │▓▓│     TENNIS BALL POCKET      │▓▓│
                    │▓▓│         Ø59mm               │▓▓│ ← Snug fit
                    │▓▓│                             │▓▓│
                    │▓▓└─────────────────────────────┘▓▓│
                    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                    └───────────────────────────────────┘
                    │←─────────── 70mm ───────────────→│
                                (fin span)

DIMENSIONS:
─────────────────────────────────────────────────────────────────────────────
Collar OD:          30mm (fits in 32mm barrel with clearance)
Collar length:      40mm
Ball pocket:        Ø59mm × 30mm deep (holds tennis ball)
Fin span:           70mm tip-to-tip (P11/P12), 60mm (P13)
Fin height:         25mm (P11/P12), 20mm (P13)
Fin thickness:      2mm

═══════════════════════════════════════════════════════════════════════════
```

**FIN SET DIMENSIONS:**

| Feature | P11 (15° cant) | P12 (10° cant) | P13 (straight) |
|---------|----------------|----------------|----------------|
| Number of fins | 4 | 4 | 6 |
| Cant angle | 15° | 10° | 0° |
| Fin height | 25mm | 25mm | 20mm |
| Fin root chord | 15mm | 15mm | 12mm |
| Fin tip chord | 10mm | 10mm | 8mm |
| Fin thickness | 2mm | 2mm | 2mm |
| Collar OD | 30mm | 30mm | 30mm |
| Total span | 70mm | 70mm | 60mm |

**FIN PRINT SETTINGS:**
- Material: PLA (stronger for thin features)
- Infill: 100% (solid)
- Layer height: 0.15mm (fine detail)
- Orientation: Fins vertical for strength
- No supports needed

---

### P14: WEIGHTED NOSE

**Function:** Shifts CG forward for stability, contains BB fill

```
P14 WEIGHTED NOSE - SECTION VIEW
═══════════════════════════════════════════════════════════════════════════

                         ╱╲
                        ╱  ╲
                       ╱    ╲
                      ╱      ╲
                     ╱        ╲
                    ╱   BB     ╲
                   ╱   FILL     ╲
                  ╱    CAVITY    ╲
                 ╱    (Ø15×20)    ╲
                ╱                  ╲
               ╱▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╲
              │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
              │▓▓┌──────────────┐▓▓▓▓│
              │▓▓│  BALL SOCKET │▓▓▓▓│
              │▓▓│    Ø58mm     │▓▓▓▓│
              │▓▓└──────────────┘▓▓▓▓│
              └──────────────────────┘
                    │← 30mm →│

DIMENSIONS:
─────────────────────────────────────────────────────────────────────────────
Overall length:     50mm
Max diameter:       30mm
Ball socket:        Ø58mm hemisphere (receives tennis ball)
BB cavity:          Ø15mm × 20mm deep
BB fill mass:       ~20g (steel BBs)
Wall thickness:     3mm minimum

ASSEMBLY:
1. Print nose cone
2. Fill cavity with steel BBs
3. Seal with hot glue or epoxy
4. Press tennis ball into socket

═══════════════════════════════════════════════════════════════════════════
```

---

## 3. ASSEMBLY DRAWINGS

### 3.1 Receiver Assembly

```
RECEIVER ASSEMBLY - EXPLODED VIEW
═══════════════════════════════════════════════════════════════════════════

                              P06 RAIL MOUNT
                                   │
                         M4×12 (4×)│
                              ↓    ↓
                    ┌─────────────────────────┐
                    │                         │
                    │    P01 RECEIVER BODY    │
                    │                         │
            ┌───────┼─────────────────────────┼───────┐
            │       │                         │       │
    P05     │       │                         │       │     P05
    BARREL  │   ←───┼─────────────────────────┼───→   │   BARREL
    CLAMP   │       │                         │       │   CLAMP
    (upper) │       │                         │       │   (lower)
            └───────┼─────────────────────────┼───────┘
                    │    ↑                    │
                    │    │ M4×20 (4×)         │
                    │    │                    │
                    │ P03 BREECH ADAPTER      │
                    │         │               │
                    │         │ O-rings (2×)  │
                    │         ↓               │
                    │    ┌─────────┐          │
                    │    │         │          │
                    └────┤ BARREL  ├──────────┘
                         │  TUBE   │
                         │ (PVC)   │
                         └─────────┘

                    │         │               │
                    │    P02 VALVE MOUNT      │
                    │         │               │
                    │    M4×12 (4×)           │
                    │         ↓               │
                    │    ┌─────────┐          │
                    │    │SOLENOID │          │
                    │    │  VALVE  │          │
                    │    └─────────┘          │
                    │                         │
                    └─────────────────────────┘
                              │
                              │ M6×30 (2×)
                              ↓
                    ┌─────────────────────────┐
                    │                         │
                    │    P09 STOCK BODY       │
                    │                         │
                    └─────────────────────────┘

═══════════════════════════════════════════════════════════════════════════
```

### 3.2 Projectile Assembly

```
PROJECTILE ASSEMBLY - EXPLODED VIEW
═══════════════════════════════════════════════════════════════════════════

                         P14 WEIGHTED NOSE
                         (with BB fill)
                              │
                              │ press fit
                              ↓
                         ┌─────────┐
                         │         │
                         │ TENNIS  │
                         │  BALL   │
                         │  58mm   │
                         │         │
                         └─────────┘
                              │
                              │ friction fit
                              ↓
                    ┌─────────────────────┐
                    │                     │
                    │   P11/P12/P13       │
                    │   FIN COLLAR        │
                    │   (with fins)       │
                    │                     │
                    └─────────────────────┘


ASSEMBLED PROJECTILE:
─────────────────────────────────────────────────────────────────────────────

              NOSE                    BALL              FINS
               ╲                       │                 │
                ╲     ┌────────────────┼────────────────┐│
                 ╲   ╱                 │                 ╲│
                  ╲ ╱   ┌─────────┐    │    ┌───────────┐╲
                   ╳    │  ● ● ●  │    │    │           │ ╲
                  ╱ ╲   │  (BBs)  │    │    │   FINS    │  │
                 ╱   ╲  └─────────┘    │    │           │  │
                ╱     ╲                │    └───────────┘ ╱
               ╱       ╲───────────────┼────────────────╱│
              ╱                        │                 │

             ←───── 50mm ────→←── 58mm ──→←─── 40mm ───→

             TOTAL LENGTH: ~148mm
             TOTAL MASS: ~80g (with BBs)
             CG: Forward of center (stable)

═══════════════════════════════════════════════════════════════════════════
```

---

## 4. HEAT-SET INSERT INSTALLATION

```
HEAT-SET INSERT GUIDE
═══════════════════════════════════════════════════════════════════════════

TOOLS NEEDED:
• Soldering iron with conical tip (or insert tip)
• Heat-set inserts (M3: Ø4.0×5mm, M4: Ø5.6×6mm)
• Temperature: 220-240°C for PETG

PROCEDURE:
─────────────────────────────────────────────────────────────────────────────

    Step 1: Place insert          Step 2: Heat & press      Step 3: Result

         ┌───┐                         ┌───┐                    ┌───┐
         │   │ insert                  │███│ iron tip           │   │
         │   │                         │▼▼▼│                    │   │
    ─────┼───┼─────               ─────┼───┼─────          ─────┼───┼─────
    │▓▓▓▓│   │▓▓▓▓│               │▓▓▓▓│░░░│▓▓▓▓│          │▓▓▓▓│▓▓▓│▓▓▓▓│
    │▓▓▓▓│   │▓▓▓▓│               │▓▓▓▓│░░░│▓▓▓▓│          │▓▓▓▓│▓▓▓│▓▓▓▓│
    │▓▓▓▓│   │▓▓▓▓│               │▓▓▓▓│░░░│▓▓▓▓│          │▓▓▓▓└───┘▓▓▓▓│
    │▓▓▓▓│   │▓▓▓▓│               │▓▓▓▓│   │▓▓▓▓│          │▓▓▓▓▓▓▓▓▓▓▓▓▓│
    │▓▓▓▓└───┘▓▓▓▓│               │▓▓▓▓└───┘▓▓▓▓│          │▓▓▓▓▓▓▓▓▓▓▓▓▓│

    • Align insert               • Apply heat 3-5 sec      • Flush with
    • Don't push yet             • Press slowly             surface
                                 • Don't overheat          • Let cool

TIPS:
• Insert should be flush or 0.5mm below surface
• Don't overheat - plastic becomes too soft
• If crooked, reheat and adjust while warm
• Test thread with screw before assembly

INSERT COUNT PER PART:
─────────────────────────────────────────────────────────────────────────────
P01 Receiver:     6× M4
P02 Valve Mount:  4× M4
P08 Grip:         2× M4
P09 Stock:        2× M4
P10 Tank Clamp:   4× M4
─────────────────────────────────────────────────────────────────────────────
TOTAL:           18× M4 inserts

═══════════════════════════════════════════════════════════════════════════
```

---

## 5. STL EXPORT CHECKLIST

```
STL EXPORT SETTINGS
═══════════════════════════════════════════════════════════════════════════

CAD SOFTWARE SETTINGS:
─────────────────────────────────────────────────────────────────────────────
Format:             STL Binary
Units:              Millimeters
Resolution:         High (chord deviation <0.01mm)
Angular tolerance:  1°
Mesh check:         Watertight, no inverted normals

FILE NAMING CONVENTION:
─────────────────────────────────────────────────────────────────────────────
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

PRE-PRINT CHECKLIST:
─────────────────────────────────────────────────────────────────────────────
☐ STL file loads without errors in slicer
☐ Model is watertight (no holes)
☐ Correct orientation for printing
☐ Supports generated where needed
☐ Estimated print time acceptable
☐ Estimated filament usage acceptable
☐ Bed adhesion (brim/raft) configured

═══════════════════════════════════════════════════════════════════════════
```

---

## 6. PRINT QUEUE

```
RECOMMENDED PRINT ORDER
═══════════════════════════════════════════════════════════════════════════

BATCH 1: Critical path (Day 1-2)
─────────────────────────────────────────────────────────────────────────────
☐ P01 Receiver Body      PETG    200g    12h    Start first (longest)
☐ P03 Breech Adapter     PETG     40g     2h    Critical for assembly
☐ P05 Barrel Clamps (×2) PETG     40g     2h    Critical for assembly

BATCH 2: Stock assembly (Day 2)
─────────────────────────────────────────────────────────────────────────────
☐ P09 Stock Body         PETG    150g    10h    Second longest
☐ P10 Tank Clamp         PETG     80g     5h

BATCH 3: Small parts (Day 3)
─────────────────────────────────────────────────────────────────────────────
☐ P02 Valve Mount        PETG     50g     3h
☐ P06 Rail Mount         PETG     30g     2h
☐ P07 Trigger Guard      PETG     20g     1h
☐ P08 Grip               PETG     60g     4h
☐ P04 Muzzle Cap         PETG     20g     1h

BATCH 4: Projectiles (Day 4)
─────────────────────────────────────────────────────────────────────────────
☐ P11 Fin Set A (×4)     PLA      20g    1.5h
☐ P12 Fin Set B (×4)     PLA      20g    1.5h
☐ P13 Fin Set C (×4)     PLA      20g    1.5h
☐ P14 Weighted Nose (×4) PLA      40g     2h

─────────────────────────────────────────────────────────────────────────────
TOTAL PRINT TIME:                        ~48 hours
TOTAL FILAMENT:                          ~790g

═══════════════════════════════════════════════════════════════════════════
```

---

## 7. DOCUMENT LINKS

- [[VN-CUA-001_prototype_BOM|Prototype Bill of Materials]]
- [[VN-CUA-001_prototype_experiments|Experiment Procedures]]
- [[VN-CUA-001_P3_embodiment_design|Phase 3 Embodiment Design]]

---

## 8. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial 3D print specifications. 14 parts, ~790g filament, ~48h print time. Detailed dimensions for all components.** |

---

*These specifications enable fabrication of VDC-33 prototype using standard FDM 3D printing.*
