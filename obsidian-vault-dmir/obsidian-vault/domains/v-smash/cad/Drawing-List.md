# V-SMASH CAD Drawing List

> **Project**: V-SMASH Fire Control System
> **Subsystem**: Sensor Unit (Camera + IMU + Processor)
> **Status**: 🔄 READY TO MODEL (Phase 1)
> **Date**: 2026-01-29

---

## 1. Drawing List Summary

| Type | Count | Status |
|------|-------|--------|
| Part Drawings (chi tiết) | 10 | ⬜ To create |
| Assembly Drawings (lắp) | 2 | ⬜ To create |
| **TOTAL** | **12** | |

---

## 2. Part Drawings (Bản vẽ chi tiết)

### 2.1 Main Housing

| # | Part ID | Name (EN) | Name (VN) | Material | Dimensions | Priority |
|---|---------|-----------|-----------|----------|------------|----------|
| 1 | VS-DT-001 | Main Housing | Vỏ chính | Aluminum | 150×100×80 | P1 |
| 2 | VS-DT-002 | Front Cover | Nắp trước | Aluminum | 150×100×10 | P1 |
| 3 | VS-DT-003 | Rear Cover | Nắp sau | Aluminum | 150×100×10 | P1 |

### 2.2 Camera Mount

| # | Part ID | Name (EN) | Name (VN) | Material | Dimensions | Priority |
|---|---------|-----------|-----------|----------|------------|----------|
| 4 | VS-DT-004 | Camera Bracket | Giá đỡ camera | Aluminum | 60×40×30 | P1 |
| 5 | VS-DT-005 | Camera Window | Kính camera | Polycarbonate | Ø50×3 | P2 |
| 6 | VS-DT-006 | Camera Shade | Che nắng camera | ABS | 60×40×20 | P2 |

### 2.3 Internal Components

| # | Part ID | Name (EN) | Name (VN) | Material | Dimensions | Priority |
|---|---------|-----------|-----------|----------|------------|----------|
| 7 | VS-DT-007 | Jetson Mount | Giá Jetson | Aluminum | 100×80×10 | P1 |
| 8 | VS-DT-008 | IMU Mount | Giá IMU | Aluminum | 30×30×15 | P2 |
| 9 | VS-DT-009 | Heat Sink | Tản nhiệt | Aluminum | 80×60×20 | P1 |

### 2.4 Mounting

| # | Part ID | Name (EN) | Name (VN) | Material | Dimensions | Priority |
|---|---------|-----------|-----------|----------|------------|----------|
| 10 | VS-DT-010 | Tripod Adapter | Đế tripod | Aluminum | 80×80×15 | P2 |

---

## 3. Assembly Drawings (Bản vẽ lắp)

| # | Assy ID | Name (EN) | Name (VN) | Parts Included |
|---|---------|-----------|-----------|----------------|
| 1 | VS-LR-001 | Sensor Head | Đầu cảm biến | DT-001, DT-002, DT-003, DT-004, DT-005, DT-006 |
| 2 | VS-LR-002 | Complete Unit | Cụm hoàn chỉnh | LR-001, DT-007, DT-008, DT-009, DT-010 |

---

## 4. Modeling Order (Thứ tự vẽ)

```
PHASE 1: Main Housing (Week 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. VS-DT-001 Main Housing     ← START HERE
   - Rectangular enclosure
   - Internal rails for Jetson
   - Heat sink mounting
   - Open front and rear

2. VS-DT-002 Front Cover
   - Camera window cutout
   - LED indicator holes
   - Gasket groove

3. VS-DT-003 Rear Cover
   - Connector cutouts (power, data)
   - Fan vent
   - Gasket groove

PHASE 2: Camera System (Week 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4. VS-DT-004 Camera Bracket
   - Adjustable tilt ±15°
   - IMX290 mounting pattern

5. VS-DT-005 Camera Window
   - Optical quality polycarbonate
   - Anti-reflective coating

6. VS-DT-006 Camera Shade
   - Reduces glare
   - Snap-fit to front cover

7. VS-LR-001 Sensor Head Assembly

PHASE 3: Internal & Mounting (Week 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8. VS-DT-007 Jetson Mount
   - Xavier NX mounting pattern
   - Thermal pad interface

9. VS-DT-008 IMU Mount
   - BNO055 mounting
   - Vibration isolation

10. VS-DT-009 Heat Sink
    - Fins for passive cooling
    - Interface to Jetson

11. VS-DT-010 Tripod Adapter
    - 1/4"-20 thread
    - Dovetail option

12. VS-LR-002 Complete Assembly
```

---

## 5. FreeCAD Prompts

### VS-DT-001 Main Housing

```
Tạo chi tiết VS-DT-001 - Main Housing trong FreeCAD:
- Document name: "VS-DT-001-MainHousing"

Main body:
- Outer: 150 × 100 × 80 mm
- Wall thickness: 4mm
- Open front and rear (for covers)
- Corner radius: R3 external

Features:
- 2× internal rails for Jetson mount, 5mm wide × 3mm deep
  - Position: Y=20 and Y=80, full length
- 4× M4 threaded holes on bottom for tripod adapter
  - Pattern: 60×60mm square, centered
- Heat sink mounting surface: 80×60mm flat area on top
- 4× M3 holes for heat sink, pattern 70×50mm

Material: Aluminum 6061
Color: Dark gray
```

### VS-DT-004 Camera Bracket

```
Tạo chi tiết VS-DT-004 - Camera Bracket trong FreeCAD:
- Document name: "VS-DT-004-CameraBracket"

Main body:
- L-shaped bracket
- Base: 60 × 40 × 5 mm
- Upright: 40 × 30 × 5 mm

Features:
- 2× M3 clearance holes in base for mounting
- 2× M2 holes in upright for IMX290 camera module
  - Spacing: 25mm horizontal
- Slot for tilt adjustment: 10mm arc, Ø3.5mm

Material: Aluminum 6061
Color: Silver
```

### VS-DT-009 Heat Sink

```
Tạo chi tiết VS-DT-009 - Heat Sink trong FreeCAD:
- Document name: "VS-DT-009-HeatSink"

Main body:
- Base: 80 × 60 × 5 mm
- Fins: 12× fins, 2mm thick, 15mm tall, 3mm spacing

Features:
- 4× M3 clearance holes for mounting
  - Pattern: 70×50mm
- Bottom surface flat for thermal interface

Material: Aluminum 6063-T5
Color: Black anodized
```

---

## 6. Requirements Traceability

| Part ID | Requirements Covered |
|---------|---------------------|
| DT-001 | Environmental protection, thermal management |
| DT-002 | Camera window, IP rating |
| DT-003 | Connector access, cooling |
| DT-004 | Camera FOV adjustment |
| DT-005 | Optical path, weatherproofing |
| DT-007 | Jetson Xavier NX mounting |
| DT-008 | IMU stability, vibration isolation |
| DT-009 | Thermal management (10-15W dissipation) |
| DT-010 | Field deployment flexibility |

---

## 7. Thermal Analysis Requirements

```
THERMAL BUDGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Heat sources:
- Jetson Xavier NX:     15W (max)
- Camera module:         1W
- IMU:                  0.1W
- Total:               16.1W

Ambient:               50°C (max)
Max junction temp:     85°C (Jetson)
Budget ΔT:             35°C

Heat sink requirement:
- Rth < 35°C / 16W = 2.2 °C/W
- With fan: easily achievable
- Passive: marginal, need optimization
```

---

## 8. Export Checklist

| Part | FreeCAD | STEP | 2D Drawing | BOM Entry |
|------|---------|------|------------|-----------|
| DT-001 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-002 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-003 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-004 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-005 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-006 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-007 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-008 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-009 | ⬜ | ⬜ | ⬜ | ⬜ |
| DT-010 | ⬜ | ⬜ | ⬜ | ⬜ |
| LR-001 | ⬜ | ⬜ | ⬜ | - |
| LR-002 | ⬜ | ⬜ | ⬜ | - |

---

## 9. References

- [[Dev-Kit-Procurement]] - Jetson Xavier NX specs
- [[Phase-1-Schedule]] - Timeline
- [[Resource-Plan]] - Budget for machining
- [[cad-workflow]] - FreeCAD commands

---

*Drawing list ready for FreeCAD modeling*
