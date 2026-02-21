# =============================================================================
# AICC_MAKER_VolumeStudy_v1.0.py
# VN-AICC-001 Phase 3 — Component Volume Study
# Individual bounding boxes for volume comparison (NOT assembled layout)
#
# Document ref: VN_AICC_001_Component_Volume_Study.md v1.0
# Created: 2026-02-20
# Status: CHECKPOINT APPROVED
#
# HOW TO USE:
#   1. Open FreeCAD
#   2. Macro > Macros > Execute this file
#   3. Each component appears as a labeled solid in a 4-column grid
#   4. Use Model Tree to show/hide individual components
#   5. Select any component → Properties → Volume (in mm³)
#
# NOTE: This file shows individual volumes only.
#       For the enclosure spatial layout see: AICC_MAKER_Layout_v1.py
# =============================================================================

import FreeCAD as App
import Part

# --- Document ---
doc = App.newDocument("AICC_VolumeStudy")

# --- Grid layout parameters ---
# Components arranged in a 4-column grid for comparison
# Each cell: COL_W wide × ROW_H deep, 10mm gap between rows
COL_W = 200   # mm between column origins
ROW_H = 130   # mm between row origins

def place_offset(col, row):
    """Return placement base vector for grid cell (col, row)."""
    return App.Vector(col * COL_W, row * ROW_H, 0)

def add_box(name, label, L, W, H, col, row, color=(0.5, 0.5, 0.5)):
    """Create a box bounding volume at grid position."""
    shape = Part.makeBox(L, W, H)
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape
    obj.Placement.Base = place_offset(col, row)
    obj.Label = label
    try:
        obj.ViewObject.ShapeColor = color
        obj.ViewObject.Transparency = 20
        obj.ViewObject.DisplayMode = "Shaded"
    except Exception:
        pass
    return obj, L * W * H  # return (obj, volume_mm3)

def add_cyl(name, label, radius, H, col, row, color=(0.5, 0.5, 0.5)):
    """Create a cylindrical bounding volume at grid position."""
    import math
    shape = Part.makeCylinder(radius, H)
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape
    obj.Placement.Base = place_offset(col, row)
    obj.Label = label
    try:
        obj.ViewObject.ShapeColor = color
        obj.ViewObject.Transparency = 20
        obj.ViewObject.DisplayMode = "Shaded"
    except Exception:
        pass
    vol = math.pi * radius**2 * H
    return obj, vol

# =============================================================================
# ROW 0 — Compute & Carrier Boards (GREEN tones)
# =============================================================================

# A1: CM4 IO Board PCB only (just the board, no connectors)
_, v_a1 = add_box(
    "A1_CM4_IO_Board_PCB",
    "A1: CM4 IO Board PCB  160×90×1.6mm",
    160.0, 90.0, 1.6,
    col=0, row=0,
    color=(0.20, 0.65, 0.20)
)

# A2: CM4 IO Board full envelope including tallest connector (RJ45 = 13.5mm)
# Height = 1.6 PCB + 13.5 RJ45 = 15.1mm. Bounding box wraps entire board.
_, v_a2 = add_box(
    "A2_CM4_IO_Board_Envelope",
    "A2: CM4 IO Board Envelope  160×90×15.1mm  [PCB + tallest connector]",
    160.0, 90.0, 15.1,
    col=1, row=0,
    color=(0.30, 0.80, 0.30)
)

# A3: CM4 Module bounding box — measured from IO Board carrier PCB top surface
# Z height = 3.0mm Hirose mated gap + 1.0mm CM4 PCB + 2.4mm top components = 6.4mm
# CORRECTION from Spatial Layout v1.2 (was 4.7mm, corrected to 6.4mm)
_, v_a3 = add_box(
    "A3_CM4_Module_Envelope",
    "A3: CM4 Module Envelope  55×40×6.4mm  [CORRECTED: was 4.7mm]",
    55.0, 40.0, 6.4,
    col=2, row=0,
    color=(0.10, 0.45, 0.85)
)

# A4: Custom I/O Carrier PCB — REVISED to 80×55mm (was 80×50mm)
# Component fill factor: 80×55 = 4400mm² at 102% fill (×2.5 routing factor)
_, v_a4 = add_box(
    "A4_IO_Carrier_PCB",
    "A4: Custom I/O Carrier PCB  80×55×1.6mm  [REVISED: was 80×50mm]",
    80.0, 55.0, 1.6,
    col=3, row=0,
    color=(0.20, 0.65, 0.65)
)

# =============================================================================
# ROW 1 — Display & User Interface (ORANGE/PURPLE tones)
# =============================================================================

# B1: Waveshare 3.5" HDMI LCD (Standard, RECOMMENDED)
# Dimensions: ~86×57×9mm [VERIFY: download 3D_Drawing.zip from Waveshare wiki]
# $35.99 USD, 480×320 IPS, resistive touch, HDMI interface
_, v_b1 = add_box(
    "B1_Display_35_HDMI_Standard",
    "B1: Waveshare 3.5in HDMI LCD (Standard)  86×57×9mm  [$35.99] [VERIFY dims]",
    86.0, 57.0, 9.0,
    col=0, row=1,
    color=(0.85, 0.42, 0.10)
)

# B1_alt: Waveshare 3.5" HDMI LCD (E) — Alt model for comparison
# 76.6×63.6×9mm, 640×480 capacitive, $43.99
_, v_b1e = add_box(
    "B1_alt_Display_35_HDMI_E",
    "B1-alt: Waveshare 3.5in HDMI LCD (E)  76.6×63.6×9mm  [$43.99] [not recommended]",
    76.6, 63.6, 9.0,
    col=1, row=1,
    color=(0.60, 0.30, 0.10)
)

# B2: OLED 1.3" SPI (SH1106 128×64)
_, v_b2 = add_box(
    "B2_OLED_13_SPI",
    "B2: OLED 1.3in SPI SH1106  35×18×3.5mm",
    35.0, 18.0, 3.5,
    col=2, row=1,
    color=(0.85, 0.65, 0.10)
)

# B3: Tactile button 12mm (panel-mount, body behind panel)
_, v_b3 = add_box(
    "B3_Tactile_Button_12mm",
    "B3: Tactile Button 12mm  12×12×12mm  [×6 in design]",
    12.0, 12.0, 12.0,
    col=3, row=1,
    color=(0.60, 0.20, 0.65)
)

# =============================================================================
# ROW 2 — Controls & Electromechanical (RED/GREY tones)
# =============================================================================

# C1: E-stop 16mm NC mushroom
# Bounding cylinder: Ø40mm (head) × 35mm depth
# (Body Ø16mm, mounting nut depth ~7mm, contact block ~15mm, total ~35mm)
_, v_c1 = add_cyl(
    "C1_Estop_16mm_NC",
    "C1: E-stop 16mm NC  Cyl Ø40×35mm  [head Ø40, body Ø16]",
    radius=20.0, H=35.0,
    col=0, row=2,
    color=(0.85, 0.10, 0.10)
)

# C2: RGB LED WS2812B 5×5mm
_, v_c2 = add_box(
    "C2_WS2812B_LED",
    "C2: WS2812B RGB LED  5×5×1.7mm  [×4 in design]",
    5.0, 5.0, 1.7,
    col=1, row=2,
    color=(0.10, 0.85, 0.10)
)

# =============================================================================
# ROW 3 — Thermal, Audio & Power (GREY/YELLOW/BLUE tones)
# =============================================================================

# D1: CM4 Heatsink 40×40×10mm Al 6063-T5
_, v_d1 = add_box(
    "D1_Heatsink_40x40x10",
    "D1: Heatsink Al 6063-T5  40×40×10mm",
    40.0, 40.0, 10.0,
    col=0, row=3,
    color=(0.75, 0.75, 0.75)
)

# D2: Speaker 28mm 8Ω 1W (cylinder)
_, v_d2 = add_cyl(
    "D2_Speaker_28mm",
    "D2: Speaker 28mm 8Ohm 1W  Cyl Ø28×12mm",
    radius=14.0, H=12.0,
    col=1, row=3,
    color=(0.35, 0.35, 0.35)
)

# D3: PAM8403 audio amplifier module (small PCB)
_, v_d3 = add_box(
    "D3_PAM8403_AmpModule",
    "D3: PAM8403 Audio Amp Module  20×18×6mm",
    20.0, 18.0, 6.0,
    col=2, row=3,
    color=(0.55, 0.55, 0.20)
)

# D4: Power supply module (mini buck converter + LDO)
_, v_d4 = add_box(
    "D4_PowerSupply_Module",
    "D4: Power Supply Module (Buck+LDO)  30×20×10mm  [VERIFY: measure actual]",
    30.0, 20.0, 10.0,
    col=3, row=3,
    color=(0.40, 0.40, 0.85)
)

# =============================================================================
# RECOMPUTE & FIT VIEW
# =============================================================================

doc.recompute()

try:
    App.Gui.ActiveDocument.ActiveView.fitAll()
    App.Gui.ActiveDocument.ActiveView.viewIsometric()
except Exception:
    pass

# =============================================================================
# VOLUME REPORT
# =============================================================================

volumes = {
    "A1  CM4 IO Board PCB (160×90×1.6)":                        v_a1,
    "A2  CM4 IO Board Envelope (160×90×15.1) incl. connectors": v_a2,
    "A3  CM4 Module Envelope (55×40×6.4) CORRECTED":            v_a3,
    "A4  Custom I/O Carrier PCB (80×55×1.6) REVISED":           v_a4,
    "B1  Display 3.5in HDMI Standard (~86×57×9) VERIFY":        v_b1,
    "B1e Display 3.5in HDMI (E) (76.6×63.6×9) [not rec]":       v_b1e,
    "B2  OLED 1.3in SPI (35×18×3.5)":                           v_b2,
    "B3  Tactile Button 12mm (12×12×12) ×6":                    v_b3,
    "C1  E-stop 16mm NC (Ø40 cyl ×35mm)":                       v_c1,
    "C2  WS2812B LED (5×5×1.7) ×4":                             v_c2,
    "D1  Heatsink Al 6063 (40×40×10)":                          v_d1,
    "D2  Speaker 28mm (Ø28 cyl ×12)":                           v_d2,
    "D3  PAM8403 Audio Amp (20×18×6)":                          v_d3,
    "D4  Power Supply Module (30×20×10) VERIFY":                 v_d4,
}

print()
print("=" * 70)
print("  VN-AICC-001  COMPONENT VOLUME STUDY  v1.0")
print("  AICC MAKER — Individual Bounding Box Volumes")
print("=" * 70)
print(f"  {'Component':<52} {'Vol (cm³)':>9}  {'Vol (mm³)':>12}")
print("  " + "-" * 66)

total_component_vol_mm3 = 0
for label, vol in volumes.items():
    vol_cm3 = vol / 1000.0
    print(f"  {label:<52} {vol_cm3:>9.2f}  {vol:>12,.0f}")
    if not label.startswith("B1e"):  # exclude alt display from total
        total_component_vol_mm3 += vol

enclosure_vol_mm3 = 180 * 115 * 75          # 1,552,500 mm³
enclosure_internal_mm3 = 174 * 109 * 72      # 174×109×72 internal (3mm walls)

print("  " + "-" * 66)
print(f"  {'TOTAL component volume (excl. alt display)':<52} {total_component_vol_mm3/1000:>9.2f}  {total_component_vol_mm3:>12,.0f}")
print()
print(f"  Enclosure envelope (180×115×75):               {enclosure_vol_mm3/1000:>9.2f} cm³ = {enclosure_vol_mm3:>10,} mm³")
print(f"  Enclosure internal  (174×109×72, 3mm walls):   {enclosure_internal_mm3/1000:>9.2f} cm³ = {enclosure_internal_mm3:>10,} mm³")
print(f"  Component fill ratio (vs internal):            {total_component_vol_mm3/enclosure_internal_mm3*100:>9.1f}%")
print()
print("  NOTES:")
print("  [CORRECTED] CM4 Module Z=6.4mm (was 4.7mm). Hirose DF40HC(3.0) spec.")
print("  [REVISED]   I/O Carrier PCB 80×55mm (was 80×50mm). 102% fill @ ×2.5 routing.")
print("  [VERIFY]    Display dims: download 3.5inch_HDMI_LCD_3D_Drawing.zip from Waveshare wiki.")
print("  [VERIFY]    Power supply module: measure actual unit before PCB layout.")
print()
print("  Layout file (assembled position): AICC_MAKER_Layout_v1.py")
print("  Volume Study doc: VN_AICC_001_Component_Volume_Study.md")
print("=" * 70)

# =============================================================================
# Z-STACK CORRECTION SUMMARY
# =============================================================================
print()
print("  Z-STACK CORRECTION (vs Spatial Layout v1.2):")
print("  " + "-" * 50)
print(f"  CM4 module height above IO Board:  4.7mm → 6.4mm  (+1.7mm)")
print(f"  Heatsink base Z:                  20.9mm → 22.6mm (+1.7mm)")
print(f"  Heatsink top Z:                   30.9mm → 32.6mm (+1.7mm)")
print(f"  Air gap (heatsink top↔display):   31.6mm → 29.9mm (-1.7mm)  ✅ ample")
print(f"  Enclosure height (75mm):          UNCHANGED")
print("=" * 70)
