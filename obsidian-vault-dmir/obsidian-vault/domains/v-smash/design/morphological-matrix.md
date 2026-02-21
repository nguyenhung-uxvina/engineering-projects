# V-SMASH Morphological Matrix

> **Document Type**: Conceptual Design - Solution Space Exploration
> **Version**: 1.1
> **Method**: Zwicky Morphological Analysis

---

## 1. Matrix Overview

| Subfunction | Option A | Option B | Option C | 
|-------------|----------|----------|----------|
| **F1.1 Image Capture** | CCD sensor | **CMOS sensor** ✓ | Thermal (LWIR) |
| **F1.2 Target Detection** | Template matching | Classical CV (HOG+SVM) | **Deep Learning (YOLO)** ✓ |
| **F1.3 Classification** | Rule-based | Random Forest | **Lightweight CNN** ✓ |
| **F1.4 Range Finding** | **Passive (size estimate)** ✓ | Laser Rangefinder | Stereo vision |
| **F2.2 Tracking** | Centroid tracking | **Kalman Filter** ✓ | Deep SORT |
| **F2.3 Prediction** | Linear extrapolation | Polynomial fit | **CV Kalman** ✓ |
| **F3.1 Orientation Sense** | Gyroscope only | **Gyro + Accel (6-axis)** ✓ | Full IMU (9-axis) |
| **F3.3 Ballistics** | Lookup table | **Point-mass 3DOF** ✓ | 6DOF model |
| **F4.1 Trigger Sense** | Limit switch | **Force sensor** ✓ | Optical gate |
| **F5.1/5.2 Trigger Gate** | Mechanical block | **Solenoid** ✓ | Servo motor |
| **F6.1 Aim Display** | Projected reticle | LCD overlay | **See-through optic** ✓ |
| **F6.3 Fire Indicator** | LED only | Audio only | **LED + Audio** ✓ |
| **F_AUX.1 Power** | AA batteries | **Rechargeable Li-ion** ✓ | External power |
| **F_AUX.2 Recording** | Internal memory | **SD card** ✓ | Cloud upload |
| **F_AUX.5 Fail-safe** | Manual bypass switch | Auto-detect failure | **Auto + Manual** ✓ |

**Legend**: ✓ = Selected for V4 (Phased Development)

---

## 2. Concept Variant Paths

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        MORPHOLOGICAL MATRIX - CONCEPT PATHS                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  SUBFUNCTION        │ Option A        │ Option B        │ Option C              │
│  ═══════════════════╪═════════════════╪═════════════════╪═════════════════════  │
│  F1.1 Image Capture │ CCD ────────────│ CMOS ───────────│ Thermal              │
│                     │   │             │   │      │      │     │                 │
│  F1.2 Detection     │ Template ───────│ HOG+SVM ────────│ YOLO-nano            │
│                     │   │             │   │      │      │     │                 │
│  F1.3 Classify      │ Rule-based ─────│ Random Forest ──│ CNN                  │
│                     │   │             │   │      │      │     │                 │
│  F2.2 Tracking      │ Centroid ───────│ Kalman ─────────│ Deep SORT            │
│                     │   │             │   │      │      │     │                 │
│  F3.3 Ballistics    │ Table ──────────│ Point-mass ─────│ 6DOF                 │
│                     │   │             │   │      │      │     │                 │
│  F5.1 Trigger Gate  │ Mech block ─────│ Solenoid ───────│ E-trigger            │
│                     │   │             │   │             │     │                 │
│                     │   ▼             │   ▼             │     ▼                 │
│                     │                 │                 │                       │
│  CONCEPT PATHS:     │                 │                 │                       │
│                     │                 │                 │                       │
│  V1 (CLONE)        ═══A═══════════════A═══════════════A═════════════════       │
│  • All Option A    │ CCD→Template→Rule→Centroid→Table→Mech                     │
│  • Foreign replica │ Minimum tech risk, maximum foreign dependency             │
│                                                                                  │
│  V2 (LOCAL-FIRST)  ═══B═══════════════B═══════════════B═════════════════       │
│  • All Option B    │ CMOS→HOG+SVM→RF→Kalman→PM→Solenoid                        │
│  • Maximum local   │ Proven tech, local capability match                        │
│                                                                                  │
│  V3 (HYBRID)       ═══B═══════════════C═══════════════B═════════════════       │
│  • Mix B + C       │ CMOS→YOLO→CNN→Kalman→PM→Solenoid                          │
│  • Balanced        │ AI capability with local production                        │
│                                                                                  │
│  V4 (PHASED) ✓     ═══B═══════════════B→C═════════════B═════════════════       │
│  • Start B, evolve │ CMOS→(HOG→YOLO)→(RF→CNN)→Kalman→PM→Solenoid              │
│  • SELECTED        │ Risk-managed evolution, learning integration              │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

Legend: ═══ Connection path    → Evolution path    ✓ Selected concept
```

---

## 3. Working Principle Selection Rationale

### F1.1 Image Capture: CMOS Sensor

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| CCD | Higher sensitivity | More expensive, power hungry | 2 |
| **CMOS** ✓ | Cost-effective, low power, widely available | Rolling shutter artifacts | **4** |
| Thermal | Night capability | Very expensive, export restricted | 2 |

**Selected**: CMOS - Best balance of cost, performance, availability

### F1.2 Detection: HOG+SVM → YOLO (Phased)

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| Template | Simple | Poor generalization | 1 |
| HOG+SVM | No training data needed, fast dev | Lower accuracy | 3 |
| **YOLO** ✓ | Best accuracy, real-time capable | Needs training data, expertise | **4** |

**Selected**: Start with HOG+SVM (Phase 1), transition to YOLO (Phase 2)
- Reduces initial risk
- Allows dataset collection during Phase 1
- University partnership for ML expertise

### F2.2 Tracking: Kalman Filter

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| Centroid | Simple | No motion model, loses track easily | 2 |
| **Kalman** ✓ | Proven, handles occlusion, predicts | Assumes linear motion | **4** |
| Deep SORT | Best for multi-target | Heavy computation, overkill | 2 |

**Selected**: Kalman Filter - Proven, well-documented, local expertise available

### F3.3 Ballistics: Point-Mass 3DOF

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| Lookup table | Simple, fast | Inaccurate for varied conditions | 2 |
| **Point-mass** ✓ | Good accuracy, handles wind/air | More computation | **4** |
| 6DOF | Most accurate | Overkill for small arms, slow | 2 |

**Selected**: Point-mass 3DOF - Sufficient accuracy for 400m range, real-time capable

### F5.1/5.2 Trigger Gate: Solenoid

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| Mechanical block | Simple, reliable | Slow response, bulky | 2 |
| **Solenoid** ✓ | Fast (<5ms), proven | Needs power, driver circuit | **4** |
| E-trigger | Clean integration | Only for electronic trigger weapons | 3 |

**Selected**: Solenoid - Universal compatibility, fast response, proven technology

---

## 4. Compatibility Matrix

Check which WP combinations are compatible:

| | CMOS | Kalman | Point-mass | Solenoid | See-through |
|---|:---:|:---:|:---:|:---:|:---:|
| **YOLO** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **HOG+SVM** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **6-axis IMU** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Force sensor** | ✅ | ✅ | ✅ | ✅ | ✅ |

**Result**: All selected WPs are mutually compatible ✅

---

## 5. Innovation Opportunities

### Wild Card Options (for future variants)

| Function | Wild Card | Potential |
|----------|-----------|-----------|
| F1.2 Detection | Event camera + SNN | Ultra-fast, low power |
| F1.4 Range | Radar ranging | All-weather, accurate |
| F2.2 Tracking | Transformer-based | Better long-term prediction |
| F3.3 Ballistics | ML-learned model | Adapts to actual performance |
| F6.1 Display | AR overlay | Rich information display |

### Cross-Domain Inspiration

| Domain | Technique | Applicable Function |
|--------|-----------|---------------------|
| Automotive | Lane-keeping vision | F1.2 - Edge detection |
| Gaming | Aim assist algorithms | F4.2 - Hit probability |
| Drone racing | FPV tracking | F2.2 - Fast tracking |
| Sports | Ball trajectory analysis | F3.3 - Prediction |

---

## 6. Related Documents

- [[function-structure]] - Functions being solved
- [[working-principles]] - Detailed WP specifications
- [[decisions/log#DEC-002]] - Detection approach decision
- [[quality/vdi-2225-evaluation]] - Concept evaluation

---

*Document follows Zwicky Morphological Analysis methodology*
*Last updated: 2026-01-26*
