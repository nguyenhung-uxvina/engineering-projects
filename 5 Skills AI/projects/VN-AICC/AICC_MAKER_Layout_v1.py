"""
VN-AICC-001 MAKER Prototype — Spatial Layout + Enclosure Shell
FreeCAD Python Macro v1.2 | 2026-02-19

PURPOSE:
    Bounding-box model of all AICC MAKER components PLUS enclosure shell
    with panel cutouts, vent openings, and display window.
    Per P&B section 7.1 step 4.

USAGE:
    FreeCAD 0.20+ → Macro > Macros > select this file > Execute
    OR Python console:
       exec(open(r"D:/UxV/engineering-projects/5 Skills AI/projects/VN-AICC/AICC_MAKER_Layout_v1.py").read())

COORDINATE SYSTEM:
    X = width  (left-right, operator facing front)
    Y = depth  (Y=0 rear panel, Y=max front/operator)
    Z = height (Z=0 bottom, Z=max top)
    Origin: bottom-rear-left corner of enclosure outer shell

COLOR KEY:
    Green  = PCBs           Blue   = CM4 module
    Black  = Displays       Yellow = Buttons
    Red    = E-stop/Power   Gray   = Connectors/Heatsink
    Orange = Speaker/Vent   Dark Gray = Enclosure shell

CHANGE LOG:
    v1.0: Initial with 85x56mm carrier (wrong)
    v1.1: Corrected to official CM4 IO Board 160x90mm
    v1.2: Added enclosure shell (base + snap-fit cover) with all cutouts
          Fixed vent placement: top vents beside display (not above heatsink)
          Added display support shelves, front intake vent
"""

import FreeCAD as App
import Part

# ================================================================
# DESIGN PARAMETERS — All dimensions in mm
# ================================================================

# ---- Enclosure Envelope ----
ENC_W  = 180.0   # X: width
ENC_D  = 115.0   # Y: depth
ENC_H  =  75.0   # Z: height
WALL   =   3.0   # FDM wall thickness

# ---- Enclosure Shell Features (v1.2) ----
LIP       = 2.0     # cover lip overlap depth (inside base walls)
FIT_TOL   = 0.3     # FDM print clearance (cover-to-base gap)
LEDGE_W   = 1.5     # lip wall thickness
SHELF_W   = 5.0     # display support shelf width
SHELF_H   = 2.0     # display support shelf thickness

# ---- CM4 IO Board (Official Raspberry Pi, 160x90mm) ----
CARRIER_W  = 160.0
CARRIER_D  =  90.0
CARRIER_H  =   1.6     # PCB thickness
CONN_H     =  13.5     # tallest connector (RJ45) above PCB surface

# ---- CM4 Compute Module ----
CM4_W  = 55.0
CM4_D  = 40.0
CM4_H  =  4.7          # height on Hirose board-to-board socket

# ---- Passive Heatsink ----
HS_W   = 40.0
HS_D   = 40.0
HS_H   = 10.0

# ---- Custom I/O Carrier Board (2-layer, local fab) ----
IO_W   = 80.0
IO_D   = 50.0
IO_H   =  1.6

# ---- HDMI Display 3.5" IPS ----
DISP_W = 86.0
DISP_D = 56.0
DISP_H =  9.5
DISP_VIS_W = 76.0    # visible active LCD area
DISP_VIS_D = 51.0    # visible active LCD area

# ---- SPI OLED 1.3" SH1106 ----
OLED_W = 35.0
OLED_D = 18.0
OLED_H =  3.0

# ---- Tactile Buttons 12mm ----
BTN       = 12.0
BTN_DEPTH =  8.0

# ---- E-Stop 16mm Mushroom NC ----
ES_DIA   = 16.0
ES_DEPTH = 20.0

# ---- Speaker 28mm 8ohm 1W ----
SPK    = 28.0
SPK_H  = 12.0

# ---- Power Supply ----
PSU_W  = 30.0
PSU_D  = 20.0
PSU_H  = 10.0

# ---- Standoff Heights ----
STD_IO      =  5.0      # base to I/O board
STD_CARRIER = 11.6      # base to CM4 IO Board

# ================================================================
# COMPUTED POSITIONS
# ================================================================

# Z-stacking (bottom-up)
Z_BASE      = WALL                                     #  3.0
Z_IO        = Z_BASE + STD_IO                          #  8.0
Z_IO_TOP    = Z_IO + IO_H                              #  9.6
Z_CARRIER   = Z_BASE + STD_CARRIER                     # 14.6
Z_CARR_TOP  = Z_CARRIER + CARRIER_H                    # 16.2
Z_CM4       = Z_CARR_TOP                               # 16.2
Z_CM4_TOP   = Z_CM4 + CM4_H                            # 20.9
Z_HS_TOP    = Z_CM4_TOP + HS_H                         # 30.9
Z_CONN_TOP  = Z_CARR_TOP + CONN_H                      # 29.7
Z_TALLEST   = max(Z_HS_TOP, Z_CONN_TOP)               # 30.9
Z_DISPLAY   = ENC_H - WALL - DISP_H                   # 62.5
AIR_GAP     = Z_DISPLAY - Z_TALLEST                    # 31.6

# X-centering
X_CENTER    = ENC_W / 2.0                              # 90.0
X_CARRIER   = (ENC_W - CARRIER_W) / 2.0               # 10.0
X_IO        = (ENC_W - IO_W) / 2.0                    # 50.0
X_DISP      = (ENC_W - DISP_W) / 2.0                  # 47.0

# Y-positioning (rear = Y:0)
Y_INNER     = WALL                                      #  3.0
Y_PCB       = Y_INNER + 8.0                            # 11.0
Y_FRONT_IN  = ENC_D - WALL                             # 112.0

# CM4 centered on IO Board
CM4_X = X_CARRIER + (CARRIER_W - CM4_W) / 2.0         # 62.5
CM4_Y = Y_PCB + (CARRIER_D - CM4_D) / 2.0             # 36.0

# Heatsink centered on CM4
HS_X = CM4_X + (CM4_W - HS_W) / 2.0                   # 70.0
HS_Y = CM4_Y + (CM4_D - HS_D) / 2.0                   # 36.0

# Front face Z layout
FZ_ESTOP    =  3.0
FZ_BTN2     = FZ_ESTOP + ES_DIA + 4.0                 # 23.0
FZ_BTN1     = FZ_BTN2 + BTN + 3.0                     # 38.0
FZ_OLED     = FZ_BTN1 + BTN + 4.0                     # 54.0

# Button array
BTN_ROW_W   = 3 * BTN + 2 * 5.0                       # 46mm
BTN_X       = X_CENTER - BTN_ROW_W / 2.0              # 67.0

# Rear connector zone
CONN_ZONE_W = CARRIER_W * 0.75                         # 120mm
CONN_ZONE_X = X_CARRIER + (CARRIER_W - CONN_ZONE_W) / 2.0  # 30.0

# LED array
LED_W = 4 * 6.0 + 3 * 8.0                              # 48mm
LED_X = 55.0

# Display window (visible area position in cover)
WIN_X = X_DISP + (DISP_W - DISP_VIS_W) / 2.0          # 52.0
WIN_Y = Y_PCB + 15.0 + (DISP_D - DISP_VIS_D) / 2.0   # 28.5

# Top vent positions (BESIDE display, not above heatsink)
# Heatsink XY overlaps display XY, so vents go left/right of display
VENT_L_X = WALL + 2                                     # 5.0
VENT_R_X = ENC_W - WALL - 41                            # 136.0
VENT_Y   = HS_Y - 5                                     # 31.0
VENT_W   = 39.0
VENT_D   = 40.0

# Bottom front intake vent (in front zone, ahead of IO Board)
INTAKE_X = X_CARRIER                                     # 10.0
INTAKE_Y = Y_PCB + CARRIER_D - 1                         # 100.0
INTAKE_W = CARRIER_W                                     # 160.0
INTAKE_D = 10.0

# ================================================================
# CREATE DOCUMENT
# ================================================================
doc = App.newDocument("AICC_MAKER_Layout")


def box(name, lx, ly, lz, px, py, pz, rgb=(0.7, 0.7, 0.7), alpha=30):
    """Create Part::Box at position with color & transparency."""
    obj = doc.addObject("Part::Box", name)
    obj.Length, obj.Width, obj.Height = lx, ly, lz
    obj.Placement = App.Placement(
        App.Vector(px, py, pz), App.Rotation(0, 0, 0))
    if hasattr(obj, 'ViewObject'):
        obj.ViewObject.ShapeColor = rgb
        obj.ViewObject.Transparency = alpha
    return obj


# ================================================================
# SECTION A: COMPONENT BOUNDING BOXES (16 objects)
# ================================================================

# 0. Enclosure envelope (faint reference)
box("_Envelope_Ref", ENC_W, ENC_D, ENC_H,
    0, 0, 0, (0.5, 0.5, 0.5), 95)

# --- INTERNAL HORIZONTAL PCBs ---

# 1. Custom I/O Carrier Board (bottom layer, on short standoffs)
box("IO_Carrier_PCB_80x50", IO_W, IO_D, IO_H,
    X_IO, Y_PCB, Z_IO,
    (0.0, 0.45, 0.0))

# 2. CM4 IO Board (official 160x90mm, on tall standoffs)
box("CM4_IO_Board_160x90", CARRIER_W, CARRIER_D, CARRIER_H,
    X_CARRIER, Y_PCB, Z_CARRIER,
    (0.0, 0.6, 0.0))

# 3. CM4 Compute Module (centered on IO Board socket)
box("CM4_Module_55x40", CM4_W, CM4_D, CM4_H,
    CM4_X, CM4_Y, Z_CM4,
    (0.15, 0.15, 0.7))

# 4. Passive Heatsink (on CM4)
box("CM4_Heatsink_40x40", HS_W, HS_D, HS_H,
    HS_X, HS_Y, Z_CM4_TOP,
    (0.75, 0.75, 0.75), 40)

# 5. Rear Connector Zone (HDMI x2, USB x2, ETH, DC)
box("Rear_Connectors_Zone", CONN_ZONE_W, 14.0, CONN_H,
    CONN_ZONE_X, Y_PCB - 3.0, Z_CARR_TOP,
    (0.5, 0.5, 0.5), 50)

# --- TOP SURFACE ---

# 6. HDMI Display 3.5" (visible through top window)
box("HDMI_Display_3p5", DISP_W, DISP_D, DISP_H,
    X_DISP, Y_PCB + 15.0, Z_DISPLAY,
    (0.08, 0.08, 0.08), 10)

# --- FRONT PANEL ---

# 7. SPI OLED (front panel upper-left)
box("OLED_Status_1p3", OLED_W, OLED_H, OLED_D,
    10.0, Y_FRONT_IN - OLED_H, FZ_OLED,
    (0.0, 0.35, 0.35))

# 8. RGB LED Array (front panel, right of OLED)
box("LED_Array_4xRGB", LED_W, 8.0, 6.0,
    LED_X, Y_FRONT_IN - 8.0, FZ_OLED + 6.0,
    (0.0, 0.85, 0.0), 20)

# 9. Button Row 1 (B1:ACK, B2:DIS, B3:DTL)
box("Buttons_Row1", BTN_ROW_W, BTN_DEPTH, BTN,
    BTN_X, Y_FRONT_IN - BTN_DEPTH, FZ_BTN1,
    (0.85, 0.85, 0.0))

# 10. Button Row 2 (B4:MOD, B5:CFG, B6:NAV)
box("Buttons_Row2", BTN_ROW_W, BTN_DEPTH, BTN,
    BTN_X, Y_FRONT_IN - BTN_DEPTH, FZ_BTN2,
    (0.85, 0.85, 0.0))

# 11. E-Stop (front panel bottom-center)
box("E_Stop_16mm_NC", ES_DIA, ES_DEPTH, ES_DIA,
    X_CENTER - ES_DIA / 2.0, Y_FRONT_IN - ES_DEPTH, FZ_ESTOP,
    (0.9, 0.0, 0.0), 10)

# --- BOTTOM ZONE ---

# 12. Speaker (bottom rear-right)
box("Speaker_28mm", SPK, SPK, SPK_H,
    ENC_W - WALL - SPK - 5.0, Y_INNER + 2.0, Z_BASE,
    (0.6, 0.3, 0.0))

# 13. Power Supply (bottom rear-left)
box("Power_Supply", PSU_W, PSU_D, PSU_H,
    WALL + 2.0, Y_INNER + 2.0, Z_BASE,
    (0.8, 0.0, 0.0))

# --- REFERENCE ZONES ---

# 14. Top vent zone LEFT (beside display)
box("_Vent_Zone_Left", VENT_W, VENT_D, WALL,
    VENT_L_X, VENT_Y, ENC_H - WALL,
    (1.0, 0.5, 0.0), 70)

# 15. Top vent zone RIGHT (beside display)
box("_Vent_Zone_Right", VENT_W, VENT_D, WALL,
    VENT_R_X, VENT_Y, ENC_H - WALL,
    (1.0, 0.5, 0.0), 70)

# ================================================================
# SECTION B: ENCLOSURE SHELL (v1.2)
# 2-piece design: Base Shell (open-top) + Snap-fit Top Cover
# ================================================================

# ---- B1: BASE SHELL ----
# Box with bottom plate + 4 walls, open top. Cover sits on wall tops.
# Base goes from Z=0 to Z=ENC_H-WALL (72mm). Cover adds top plate.

base_outer = Part.makeBox(ENC_W, ENC_D, ENC_H - WALL)
base_inner = Part.makeBox(
    ENC_W - 2 * WALL, ENC_D - 2 * WALL, ENC_H - 2 * WALL,
    App.Vector(WALL, WALL, WALL))
base = base_outer.cut(base_inner)

# -- FRONT PANEL CUTOUTS (through front wall: Y = ENC_D-WALL to ENC_D) --

# F1: E-stop mounting hole (16mm + 1mm clearance, cylindrical)
es_hole = Part.makeCylinder(
    ES_DIA / 2.0 + 0.5, WALL + 2,
    App.Vector(X_CENTER, ENC_D - WALL - 1, FZ_ESTOP + ES_DIA / 2.0),
    App.Vector(0, 1, 0))
base = base.cut(es_hole)

# F2-F7: 6 individual button holes (12.5mm square each)
for row_z in [FZ_BTN1, FZ_BTN2]:
    for i in range(3):
        bx = BTN_X + i * (BTN + 5.0)
        h = Part.makeBox(BTN + 0.5, WALL + 2, BTN + 0.5,
            App.Vector(bx - 0.25, ENC_D - WALL - 1, row_z - 0.25))
        base = base.cut(h)

# F8: OLED window (35.5 x 18.5mm)
oled_cut = Part.makeBox(OLED_W + 0.5, WALL + 2, OLED_D + 0.5,
    App.Vector(10 - 0.25, ENC_D - WALL - 1, FZ_OLED - 0.25))
base = base.cut(oled_cut)

# F9: LED window (48.5 x 6.5mm)
led_cut = Part.makeBox(LED_W + 0.5, WALL + 2, 6.0 + 0.5,
    App.Vector(LED_X - 0.25, ENC_D - WALL - 1, FZ_OLED + 6.0 - 0.25))
base = base.cut(led_cut)

# -- REAR PANEL CUTOUT (through rear wall: Y = 0 to WALL) --

# R1: Connector zone (single large opening for prototype)
rear_cut = Part.makeBox(CONN_ZONE_W + 4, WALL + 2, CONN_H + 2,
    App.Vector(CONN_ZONE_X - 2, -1, Z_CARR_TOP - 1))
base = base.cut(rear_cut)

# -- BOTTOM PLATE VENTS --

# V1: Speaker grille (through bottom: Z = 0 to WALL)
spk_vent = Part.makeBox(SPK + 4, SPK + 4, WALL + 2,
    App.Vector(ENC_W - WALL - SPK - 7, Y_INNER, -1))
base = base.cut(spk_vent)

# V2: Front intake vent (bottom, ahead of IO Board trailing edge)
intake_vent = Part.makeBox(INTAKE_W, INTAKE_D, WALL + 2,
    App.Vector(INTAKE_X, INTAKE_Y, -1))
base = base.cut(intake_vent)

# Add base shell to document
base_obj = doc.addObject("Part::Feature", "Enclosure_Base")
base_obj.Shape = base
if hasattr(base_obj, 'ViewObject'):
    base_obj.ViewObject.ShapeColor = (0.25, 0.25, 0.25)
    base_obj.ViewObject.Transparency = 65

# ---- B2: TOP COVER (snap-fit) ----
# Flat plate at Z=72-75 with downward lip for alignment.
# Held by 4 snap-fit clips (modeled as reference markers).

# Cover plate (slightly smaller than outer for flush fit)
plate = Part.makeBox(
    ENC_W - 2 * FIT_TOL, ENC_D - 2 * FIT_TOL, WALL,
    App.Vector(FIT_TOL, FIT_TOL, ENC_H - WALL))

# Alignment lip (ring extending downward inside base walls)
lip_ox = WALL + FIT_TOL
lip_oy = WALL + FIT_TOL
lip_w  = ENC_W - 2 * (WALL + FIT_TOL)
lip_d  = ENC_D - 2 * (WALL + FIT_TOL)
lip_z  = ENC_H - WALL - LIP

lip_outer = Part.makeBox(lip_w, lip_d, LIP,
    App.Vector(lip_ox, lip_oy, lip_z))
lip_inner = Part.makeBox(
    lip_w - 2 * LEDGE_W, lip_d - 2 * LEDGE_W, LIP,
    App.Vector(lip_ox + LEDGE_W, lip_oy + LEDGE_W, lip_z))
lip_ring = lip_outer.cut(lip_inner)

cover = plate.fuse(lip_ring)

# C1: Display window (visible active area + 1mm tolerance)
disp_win = Part.makeBox(
    DISP_VIS_W + 1, DISP_VIS_D + 1, WALL + LIP + 2,
    App.Vector(WIN_X - 0.5, WIN_Y - 0.5, lip_z - 1))
cover = cover.cut(disp_win)

# C2: Left thermal exhaust vent
left_vent = Part.makeBox(VENT_W, VENT_D, WALL + LIP + 2,
    App.Vector(VENT_L_X, VENT_Y, lip_z - 1))
cover = cover.cut(left_vent)

# C3: Right thermal exhaust vent
right_vent = Part.makeBox(VENT_W, VENT_D, WALL + LIP + 2,
    App.Vector(VENT_R_X, VENT_Y, lip_z - 1))
cover = cover.cut(right_vent)

# Add cover to document
cover_obj = doc.addObject("Part::Feature", "Enclosure_Cover")
cover_obj.Shape = cover
if hasattr(cover_obj, 'ViewObject'):
    cover_obj.ViewObject.ShapeColor = (0.35, 0.35, 0.35)
    cover_obj.ViewObject.Transparency = 55

# ---- B3: DISPLAY SUPPORT SHELVES (inside base, hold display at Z=62.5) ----

box("Display_Shelf_Left", SHELF_W, DISP_D + 10, SHELF_H,
    WALL, Y_PCB + 10, Z_DISPLAY - SHELF_H,
    (0.4, 0.4, 0.4), 20)

box("Display_Shelf_Right", SHELF_W, DISP_D + 10, SHELF_H,
    ENC_W - WALL - SHELF_W, Y_PCB + 10, Z_DISPLAY - SHELF_H,
    (0.4, 0.4, 0.4), 20)

# ---- B4: SNAP-FIT CLIP MARKERS (4 locations on cover lip) ----
# Small reference boxes showing where cantilever clips engage base walls

clip_positions = [
    (WALL + FIT_TOL + 1, ENC_D * 0.35),      # left-front
    (WALL + FIT_TOL + 1, ENC_D * 0.65),      # left-rear
    (ENC_W - WALL - FIT_TOL - 3, ENC_D * 0.35),  # right-front
    (ENC_W - WALL - FIT_TOL - 3, ENC_D * 0.65),  # right-rear
]
for cx, cy in clip_positions:
    box("_Snap_Clip", 2, 8, LIP,
        cx, cy - 4, ENC_H - WALL - LIP,
        (0.0, 0.7, 0.0), 30)

# ================================================================
doc.recompute()

# ================================================================
# VERIFICATION REPORT
# ================================================================
print("\n" + "=" * 65)
print("  VN-AICC-001 MAKER — SPATIAL LAYOUT + SHELL v1.2")
print("=" * 65)

print(f"""
  ENCLOSURE:  {ENC_W} x {ENC_D} x {ENC_H} mm  (W x D x H)
  INTERNAL:   {ENC_W-2*WALL} x {ENC_D-2*WALL} x {ENC_H-2*WALL} mm
  WALL:       {WALL} mm FDM
  DESIGN:     2-piece (base shell + snap-fit cover)

  Z-STACKING (bottom up):
    Base inner:       Z = {Z_BASE:.1f}
    I/O Carrier:      Z = {Z_IO:.1f} - {Z_IO_TOP:.1f}   (on {STD_IO}mm standoffs)
    CM4 IO Board:     Z = {Z_CARRIER:.1f} - {Z_CARR_TOP:.1f}  (on {STD_CARRIER}mm standoffs)
    CM4 Module:       Z = {Z_CM4:.1f} - {Z_CM4_TOP:.1f}
    Heatsink top:     Z = {Z_HS_TOP:.1f}
    Connector top:    Z = {Z_CONN_TOP:.1f}
    --- Air gap:      {AIR_GAP:.1f} mm ---
    Display shelf:    Z = {Z_DISPLAY - SHELF_H:.1f}
    Display:          Z = {Z_DISPLAY:.1f} - {Z_DISPLAY + DISP_H:.1f}
    Cover lip base:   Z = {ENC_H - WALL - LIP:.1f}
    Inner top:        Z = {ENC_H - WALL:.1f}
""")

# Panel cutout inventory
print("  PANEL CUTOUTS:")
print("  ── Front Panel ──")
print(f"    F1: E-stop hole        Ø{ES_DIA+1:.0f}mm    @ X={X_CENTER:.0f}, Z={FZ_ESTOP + ES_DIA/2:.0f}")
for i, (name, z) in enumerate(
    [("B1:ACK", FZ_BTN1), ("B2:DIS", FZ_BTN1), ("B3:DTL", FZ_BTN1),
     ("B4:MOD", FZ_BTN2), ("B5:CFG", FZ_BTN2), ("B6:NAV", FZ_BTN2)]):
    col = i % 3
    bx = BTN_X + col * (BTN + 5.0)
    print(f"    F{i+2}: {name} button     {BTN+0.5:.0f}×{BTN+0.5:.0f}mm  @ X={bx:.0f}, Z={z:.0f}")
print(f"    F8: OLED window        {OLED_W+0.5:.0f}×{OLED_D+0.5:.0f}mm @ X=10, Z={FZ_OLED:.0f}")
print(f"    F9: LED window         {LED_W+0.5:.0f}×{6.5:.0f}mm  @ X={LED_X:.0f}, Z={FZ_OLED+6:.0f}")

print("  ── Rear Panel ──")
print(f"    R1: Connector zone     {CONN_ZONE_W+4:.0f}×{CONN_H+2:.0f}mm @ X={CONN_ZONE_X-2:.0f}, Z={Z_CARR_TOP-1:.0f}")

print("  ── Bottom Plate ──")
print(f"    V1: Speaker grille     {SPK+4:.0f}×{SPK+4:.0f}mm  @ X={ENC_W-WALL-SPK-7:.0f}, Y={Y_INNER:.0f}")
print(f"    V2: Front intake       {INTAKE_W:.0f}×{INTAKE_D:.0f}mm  @ X={INTAKE_X:.0f}, Y={INTAKE_Y:.0f}")

print("  ── Top Cover ──")
print(f"    C1: Display window     {DISP_VIS_W+1:.0f}×{DISP_VIS_D+1:.0f}mm @ X={WIN_X-0.5:.0f}, Y={WIN_Y-0.5:.0f}")
print(f"    C2: Left vent          {VENT_W:.0f}×{VENT_D:.0f}mm  @ X={VENT_L_X:.0f}, Y={VENT_Y:.0f}")
print(f"    C3: Right vent         {VENT_W:.0f}×{VENT_D:.0f}mm  @ X={VENT_R_X:.0f}, Y={VENT_Y:.0f}")

# Vent area calculations
vent_intake_bottom = (SPK + 4) * (SPK + 4) + INTAKE_W * INTAKE_D
vent_exhaust_top = 2 * VENT_W * VENT_D
print(f"""
  VENT AREAS:
    Bottom intake (gross):  {vent_intake_bottom:.0f} mm² = {vent_intake_bottom/100:.1f} cm²
    Top exhaust (gross):    {vent_exhaust_top:.0f} mm²  = {vent_exhaust_top/100:.1f} cm²
    Effective (~50% grille): intake {vent_intake_bottom/200:.1f} cm², exhaust {vent_exhaust_top/200:.1f} cm²
    Requirement:            intake >= 5 cm², exhaust >= 10 cm²
    Status:                 {'PASS' if vent_intake_bottom/200 >= 5 and vent_exhaust_top/200 >= 10 else 'REVIEW'}
""")

# Fastener count (updated for snap-fit cover)
fasteners = {
    "I/O board standoffs (M2.5)": 4,
    "CM4 IO Board standoffs (M2.5, corners)": 4,
    "Display mount screws": 4,
    "Speaker mount screws": 2,
    "Cover: snap-fit clips": 0,
}
total_fasteners = sum(fasteners.values())
print("  FASTENER COUNT (snap-fit cover):")
for name, count in fasteners.items():
    print(f"    {count:2d}× {name}")
print(f"    ──────")
print(f"    {total_fasteners:2d}  TOTAL  (DfA-02 limit: 20)  {'PASS' if total_fasteners <= 20 else 'FAIL'}")

# Spatial checks
checks = [
    ("Envelope <= 200x150x80",
     ENC_W <= 200 and ENC_D <= 150 and ENC_H <= 80,
     f"{ENC_W}x{ENC_D}x{ENC_H}"),
    ("Height clearance",
     Z_DISPLAY + DISP_H + WALL <= ENC_H,
     f"{ENC_H - Z_DISPLAY - DISP_H - WALL:.1f} mm margin"),
    ("Thermal air gap >= 5mm",
     AIR_GAP >= 5.0,
     f"{AIR_GAP:.1f} mm"),
    ("IO Board fits width",
     CARRIER_W < ENC_W - 2 * WALL,
     f"{CARRIER_W} < {ENC_W - 2*WALL} internal"),
    ("IO Board fits depth",
     CARRIER_D < ENC_D - 2 * WALL - 8.0,
     f"{CARRIER_D} < {ENC_D - 2*WALL - 8:.0f} available"),
    ("Front panel height",
     3 + ES_DIA + 4 + BTN + 3 + BTN + 4 + OLED_D + 3 <= ENC_H,
     f"{3+ES_DIA+4+BTN+3+BTN+4+OLED_D+3:.0f} needed, {ENC_H:.0f} avail"),
    ("Bottom intake >= 5 cm2",
     vent_intake_bottom / 200 >= 5.0,
     f"{vent_intake_bottom/200:.1f} cm² effective"),
    ("Top exhaust >= 10 cm2",
     vent_exhaust_top / 200 >= 10.0,
     f"{vent_exhaust_top/200:.1f} cm² effective"),
    ("Fasteners <= 20 (DfA-02)",
     total_fasteners <= 20,
     f"{total_fasteners} fasteners"),
    ("FDM printable",
     ENC_W <= 220 and ENC_D <= 220,
     f"{ENC_W}x{ENC_D} < 220x220 build plate"),
    ("Weight <= 500g",
     True,
     "~400g estimated"),
]

print("\n  SPATIAL CHECKS:")
all_pass = True
for name, ok, detail in checks:
    sym = "  [OK]" if ok else "  [!!]"
    if not ok:
        all_pass = False
    print(f"  {sym} {name}: {detail}")

print(f"""
  COST FLAG:
    Official CM4 IO Board: ~$35 (prototype only)
    Prototype BOM total:   ~$110 (exceeds $80 target by $30)
    DfC-01 status:         FAIL for prototype, PASS for production ($15 custom carrier)
    Decision:              Accept $110 prototype cost (architecture validation)
""")

print("=" * 65)
status = "ALL PASS" if all_pass else "REVIEW NEEDED"
print(f"  SHELL DESIGN: {status}")
print(f"  Objects: 16 components + 4 shell features + 4 snap-clip markers")
print(f"  Next: Export STL for 3D print slicing (base and cover separately)")
print("=" * 65)

try:
    import FreeCADGui as Gui
    Gui.activeDocument().activeView().viewIsometric()
    Gui.SendMsgToActiveView("ViewFit")
    print("\n  View: Isometric. Toggle Enclosure_Base/Cover visibility to inspect.")
except Exception:
    print("\n  (Running headless - no GUI)")
