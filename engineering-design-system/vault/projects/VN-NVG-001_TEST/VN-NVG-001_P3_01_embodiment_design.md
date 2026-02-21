---
project: VN-NVG-001-TEST
phase: 3
type: embodiment_design
version: 1.0
created: 2026-02-03
status: complete
---

# VN-NVG-001: EMBODIMENT DESIGN (PHASE 3)
## Handheld Thermal Viewer - Layout & DfX Application

**Test Validation:** SKILL_embodiment_design.md + SKILL_dfx_guidelines.md integration

**Previous Phase:** [[VN-NVG-001_P2_01_conceptual_design|Phase 2: Conceptual Design]]

---

## 1. SELECTED CONCEPT (From Phase 2)

**Concept C: "Balanced Performer"** (VDI 2225: 84.3%)
- SWIR InGaAs sensor (640×480)
- Germanium lens
- OLED microdisplay
- ARM microcontroller
- Li-ion 18650 battery
- IP67 sealed housing

---

## 2. EMBODIMENT APPROACH

**Chosen:** 7-Step Simplified (appropriate for small, proven-tech product)

**Rationale:**
- Simple product (12 functions, minimal interfaces)
- Proven components (TRL 8-9)
- 6-month schedule (tight timeline)

---

## 3. PRELIMINARY LAYOUT

### 3.1 Form Factor

```
┌─────────────────────────────────┐
│     TOP VIEW                    │
│                                 │
│   ┌─────────────────────┐       │
│   │   Eyepiece          │       │
│   │   (15mm eye relief) │       │
│   └─────────────────────┘       │
│            ││                    │
│   ┌────────▼▼────────────┐      │
│   │  Display Housing     │      │
│   │  (OLED + optics)     │      │
│   ├─────────────────────┬┘      │
│   │  Control Module     │       │
│   │  (3 buttons, MCU)   │       │
│   ├────────────────────┬┘       │
│   │  Sensor Module     │        │
│   │  (SWIR 640×480)    │        │
│   │  ┌──────┐          │        │
│   │  │ Lens │          │        │
│   └──┴──────┴──────────┘        │
│                                 │
│  Total Length: 210mm            │
│  Width: 75mm                    │
│  Height: 140mm                  │
└─────────────────────────────────┘
```

### 3.2 Module Breakdown (L10 Leverage Point)

**Module 1: Sensor Assembly**
- SWIR InGaAs sensor (640×480)
- Germanium lens (f=50mm, f/1.2)
- Lens mount (threaded, aluminum)
- Dimensions: 60×60×40mm
- Mass: 150g

**Module 2: Electronics & Display**
- OLED microdisplay (0.5" diagonal)
- ARM Cortex-M4 microcontroller
- Power management IC
- 12-bit ADC
- Dimensions: 75×50×30mm
- Mass: 100g

**Module 3: Housing & Battery**
- Polymer housing (PC+30% GF)
- Li-ion 18650 battery (3400mAh)
- 3-button control interface
- IP67 sealing (O-rings)
- Dimensions: 75×75×210mm (overall)
- Mass: 250g

**Total Mass:** 500g ✅ (Target: ≤600g, R104)

---

## 4. DfX PRIORITY MATRIX (Top 5 for Infantry Equipment)

**Product Type:** Handheld infantry equipment (field use)

| DfX Category | Priority | Rationale |
|--------------|----------|-----------|
| **DfX #11: Safety** | ⭐⭐⭐⭐⭐ | Weapon-adjacent equipment (critical) |
| **DfX #1: Durability** | ⭐⭐⭐⭐⭐ | Field operations (drops, impacts) |
| **DfX #3: Corrosion** | ⭐⭐⭐⭐ | Jungle environment (humidity, salt) |
| **DfX #9: Maintenance** | ⭐⭐⭐⭐ | Field maintainability (battery swap only) |
| **DfX #5: Ergonomics** | ⭐⭐⭐⭐ | Handheld use (30+ min continuously) |

---

## 5. DfX GUIDELINES APPLICATION

### DfX #11: SAFETY ⭐⭐⭐⭐⭐

**Design Decisions:**
- ✅ **Battery protection circuit** (prevent thermal runaway, R703)
- ✅ **Max case temperature ≤45°C** (prevent burns, R701)
- ✅ **Auto-dim display** (prevent eye strain, R702)
- ✅ **Rounded edges** (no sharp corners, prevent injury)

---

### DfX #1: DURABILITY ⭐⭐⭐⭐⭐

**Design Decisions:**
- ✅ **1.5m drop test** (MIL-STD-810 Method 516, R301)
- ✅ **Reinforced housing** (PC+30% glass fiber, R501)
- ✅ **Shock-mounted sensor** (isolate from impacts)
- ✅ **Scratch-resistant lens coating** (R503)

---

### DfX #3: CORROSION RESISTANCE ⭐⭐⭐⭐

**Design Decisions:**
- ✅ **IP67 sealing** (dust + water immersion 1m, R504)
- ✅ **Stainless steel fasteners** (316 SS, corrosion resistant)
- ✅ **Conformal coating** (PCB protection from humidity)
- ✅ **Drainage holes** (prevent water pooling, bottom of housing)

---

### DfX #9: MAINTENANCE ⭐⭐⭐⭐

**Design Decisions:**
- ✅ **Tool-free battery access** (twist-lock battery compartment, R1401)
- ✅ **No field calibration** (factory-calibrated, R1402)
- ✅ **External lens cleaning only** (no internal access needed, R1403)
- ✅ **MTBF ≥5,000 hours** (reliable components, R1001)

---

### DfX #5: ERGONOMICS ⭐⭐⭐⭐

**Design Decisions:**
- ✅ **Contoured grip** (fits hand naturally, R801)
- ✅ **Textured surface** (anti-slip, glove compatible)
- ✅ **Balanced weight distribution** (CoG at grip point)
- ✅ **15mm eye relief** (comfortable viewing, R802)
- ✅ **Tactile buttons** (operate without looking, 3-button interface, R607)

---

## 6. DEFINITIVE LAYOUT DIMENSIONS

```
FRONT VIEW                    SIDE VIEW

    ┌─────┐                      ┌──────────────┐
    │Lens │                      │   Eyepiece   │◄─ 15mm eye relief
    │ Ø50 │                      └──────┬───────┘
    └──┬──┘                             │ 40mm
       │                                │
  ┌────▼────┐                    ┌──────▼───────┐
  │ Sensor  │                    │   Display    │
  │ 60×60mm │                    │   Housing    │ 50mm
  └────┬────┘                    └──────┬───────┘
       │                                │
  ┌────▼────┐                    ┌──────▼───────┐
  │Controls │                    │   Controls   │
  │3-button │                    │   & MCU      │ 40mm
  └────┬────┘                    └──────┬───────┘
       │                                │
  ┌────▼────┐                    ┌──────▼───────┐
  │ Battery │                    │   Battery    │
  │ 18650   │                    │   Compart    │ 80mm
  └─────────┘                    └──────────────┘

  Width: 75mm                    Length: 210mm
```

**Mass Budget:**
- Sensor module: 150g
- Electronics: 100g
- Housing: 200g
- Battery: 50g
- **TOTAL:** 500g ✅ (Requirement: ≤600g)

---

## 7. MATERIAL SELECTION

| Component | Material | Rationale | Requirement Trace |
|-----------|----------|-----------|-------------------|
| Housing | PC+30% GF (Polycarbonate + Glass Fiber) | Impact resistant, lightweight | R501, R301 |
| Lens | Germanium | SWIR transparency, high refractive index | R502, R601 |
| Fasteners | 316 Stainless Steel | Corrosion resistant (marine grade) | DfX#3 |
| Seals | Viton (FKM) | Chemical/UV resistant | R504 |
| PCB Coating | Acrylic conformal coating | Humidity protection | DfX#3 |
| Grip Texture | Thermoplastic elastomer (TPE) overmold | Anti-slip, comfort | DfX#5 (R801) |

---

## 8. GATE 3 CHECKLIST (Phase 3 → Phase 4)

- [x] Definitive layout with dimensions (210×75×140mm)
- [x] Materials selected and justified (6 materials specified)
- [x] DfX review completed (5 priority categories addressed)
- [x] Mass budget verified (500g ≤ 600g target) ✅
- [x] Standards compliance planned (MIL-STD-810, IP67)
- [x] Modular architecture defined (3 LRUs)
- [x] Systems feedback integrated (L10 modular design)
- [x] Production feasibility confirmed (COTS components available)

**Status**: ✅ **100% Complete - Ready for Phase 4**

---

## 9. VALIDATION RESULTS

### Embodiment Design Validation

| Test | Target | Actual | Status |
|------|--------|--------|--------|
| Layout dimensions | Complete | 3-view drawing | ✅ PASS |
| Mass budget | ≤600g | 500g | ✅ PASS |
| DfX categories applied | ≥5 | 5 (top priority) | ✅ PASS |
| Material selection | All critical | 6 materials specified | ✅ PASS |
| Modular design | 3 LRUs | 3 modules defined | ✅ PASS |
| Gate 3 criteria | 8/8 | 8/8 | ✅ PASS |

**PHASE 3 VALIDATION:** ✅ **COMPLETE - ALL TESTS PASSED**

**Time to Complete Phase 3:** ~45 minutes (realistic: 2-3 months with prototyping)

---

**Previous Phase:** [[VN-NVG-001_P2_01_conceptual_design|Phase 2: Conceptual Design]]
**Next Phase:** [[VN-NVG-001_P4_01_detail_design|Phase 4: Detail Design]]

**Cross-Reference Test:** ✅ Wiki-links validated, traceability maintained
