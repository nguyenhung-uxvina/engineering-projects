---
project: V-SMASH
product: LITE
designation: VSM-L
phase: 4
type: fru_specification
version: 1.0
created: 2026-02-05
status: approved
requirement: L-ASM-05
---

# V-SMASH LITE - FIELD REPLACEABLE UNIT (FRU) SPECIFICATION
## Modular Maintenance Architecture

**Document ID:** VSM-L-FRU-001
**Version:** 1.0
**Requirement:** L-ASM-05 (≥4 field-replaceable modules)

---

## 1. FRU ARCHITECTURE OVERVIEW

### 1.1 Design Philosophy

V-SMASH LITE is designed with **4 Field Replaceable Units (FRUs)** to enable:
- Soldier-level maintenance (no special tools)
- Rapid fault isolation and repair
- Reduced logistics footprint
- Mean Time To Repair (MTTR) ≤30 minutes

### 1.2 FRU Summary

```
V-SMASH LITE FRU ARCHITECTURE
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│                    FRU-1: OPTICS MODULE                      │
│    ┌─────────┐  ┌──────────────┐  ┌─────────────────────┐   │
│    │ CMOS    │  │ BEAM         │  │ SEE-THROUGH         │   │
│    │ SENSOR  │──│ SPLITTER     │──│ DISPLAY             │   │
│    │         │  │              │  │                     │   │
│    └─────────┘  └──────────────┘  └─────────────────────┘   │
│                        │ FPC Connector                       │
└────────────────────────┼────────────────────────────────────┘
                         │
┌────────────────────────┼────────────────────────────────────┐
│                    FRU-2: PROCESSING MODULE                  │
│    ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐    │
│    │ JETSON      │  │ CARRIER     │  │ IMU + SENSORS   │    │
│    │ NANO        │  │ BOARD       │  │ (BMI160, FSR)   │    │
│    │ 4GB         │  │             │  │                 │    │
│    └─────────────┘  └─────────────┘  └─────────────────┘    │
│                        │ Power + Trigger Connector           │
└────────────────────────┼────────────────────────────────────┘
                         │
┌────────────────────────┼────────────────────────────────────┐
│                    FRU-3: POWER MODULE                       │
│    ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐    │
│    │ BATTERY     │  │ PMIC        │  │ SOLENOID        │    │
│    │ 2x 18650    │  │ BOARD       │  │ DRIVER          │    │
│    │ 6800mAh     │  │             │  │                 │    │
│    └─────────────┘  └─────────────┘  └─────────────────┘    │
│                        │ Mechanical Interface                │
└────────────────────────┼────────────────────────────────────┘
                         │
┌────────────────────────┴────────────────────────────────────┐
│                    FRU-4: HOUSING MODULE                     │
│    ┌─────────────────────────────────────────────────────┐  │
│    │  MAIN HOUSING + PICATINNY MOUNT + GASKETS + COVERS  │  │
│    └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 FRU Quick Reference

| FRU | Name | Part Number | Weight | Replacement Time | Tools |
|-----|------|-------------|--------|------------------|-------|
| **FRU-1** | Optics Module | VSM-L-FRU-OPT | 180g | 10 min | Hex 2.5mm |
| **FRU-2** | Processing Module | VSM-L-FRU-PRC | 250g | 15 min | Hex 2.5mm |
| **FRU-3** | Power Module | VSM-L-FRU-PWR | 220g | 5 min | Tool-free |
| **FRU-4** | Housing Module | VSM-L-FRU-HSG | 350g | 20 min | Hex 2.5mm, 3mm |

---

## 2. FRU-1: OPTICS MODULE

### 2.1 Identification

| Field | Value |
|-------|-------|
| **FRU ID** | FRU-1 |
| **Part Number** | VSM-L-FRU-OPT |
| **Description** | Optics Module Assembly |
| **Weight** | 180g |
| **Dimensions** | 60×50×40mm |

### 2.2 Components Included

| Item | Part Number | Description | Qty |
|------|-------------|-------------|-----|
| 1 | VSM-L-SNS-001 | Sony IMX290 camera module | 1 |
| 2 | VSM-L-LNS-001 | Lens 4mm f/1.2 (mounted) | 1 |
| 3 | VSM-L-OPT-001 | Beam splitter prism | 1 |
| 4 | VSM-L-DSP-001 | See-through OLED display | 1 |
| 5 | VSM-L-OPT-002 | Reticle etched glass | 1 |
| 6 | VSM-L-OPT-003 | Protective window (AR coated) | 1 |
| 7 | VSM-L-CBL-001 | FPC cable (30-pin, 100mm) | 1 |
| 8 | VSM-L-MTG-001 | Optics mounting frame | 1 |

### 2.3 Interfaces

| Interface | Type | Location | Mating Connector |
|-----------|------|----------|------------------|
| **J1** | 30-pin FPC | Bottom | FRU-2 carrier board |
| **M1** | 4× M2.5 screws | Corners | FRU-4 housing |

### 2.4 Removal Procedure

**Tools Required:** 2.5mm hex key

**Steps:**
1. Power OFF system, remove battery (FRU-3)
2. Remove front protective cover (2× M2.5 screws)
3. Disconnect FPC cable J1 (lift locking tab, pull straight)
4. Remove 4× M2.5 mounting screws (corners)
5. Lift optics module straight up
6. Place in ESD bag

**Time:** 10 minutes

### 2.5 Installation Procedure

**Steps:**
1. Verify replacement module part number
2. Remove from ESD bag, inspect for damage
3. Align module with housing guides
4. Insert 4× M2.5 mounting screws (torque: 0.3 Nm)
5. Connect FPC cable J1 (push until click, close locking tab)
6. Reinstall front cover
7. Install battery, power ON
8. Run self-test: **Menu → Diagnostics → Optics Test**
9. Verify camera image, display function

### 2.6 Calibration After Replacement

| Calibration | Required | Procedure |
|-------------|----------|-----------|
| Boresight | **YES** | Factory or depot level |
| Focus | No | Pre-focused at factory |
| Display | No | Auto-calibrated |

**Note:** Optics module replacement requires boresight calibration. Field units should return to depot or use portable boresight tool (VSM-L-TOOL-001).

### 2.7 Fault Symptoms → FRU-1

| Symptom | Likely Cause | Action |
|---------|--------------|--------|
| No camera image | Sensor failure | Replace FRU-1 |
| Blurry image | Lens damage/misalignment | Replace FRU-1 |
| Display blank | OLED failure | Replace FRU-1 |
| Display flickering | FPC connection | Reseat J1, then replace |
| Reticle misaligned | Optics damage | Replace FRU-1 + recalibrate |

---

## 3. FRU-2: PROCESSING MODULE

### 3.1 Identification

| Field | Value |
|-------|-------|
| **FRU ID** | FRU-2 |
| **Part Number** | VSM-L-FRU-PRC |
| **Description** | Processing Module Assembly |
| **Weight** | 250g |
| **Dimensions** | 80×60×35mm |

### 3.2 Components Included

| Item | Part Number | Description | Qty |
|------|-------------|-------------|-----|
| 1 | VSM-L-CPU-001 | NVIDIA Jetson Nano 4GB | 1 |
| 2 | VSM-L-PCB-001 | Carrier board (custom) | 1 |
| 3 | VSM-L-IMU-001 | BMI160 6-axis IMU | 1 |
| 4 | VSM-L-SNS-002 | FSR402 force sensor | 1 |
| 5 | VSM-L-SNS-003 | Ambient light sensor | 1 |
| 6 | VSM-L-SNS-004 | Microphone (fire detect) | 1 |
| 7 | VSM-L-MEM-001 | SD card 32GB (with software) | 1 |
| 8 | VSM-L-THM-001 | Heat sink + fan assembly | 1 |
| 9 | VSM-L-MTG-002 | Processing mounting plate | 1 |

### 3.3 Interfaces

| Interface | Type | Location | Mating Connector |
|-----------|------|----------|------------------|
| **J1** | 30-pin FPC | Top | FRU-1 optics module |
| **J2** | 10-pin power | Bottom | FRU-3 power module |
| **J3** | 6-pin trigger | Bottom | FRU-3 solenoid driver |
| **J4** | USB-C | Side | External (config/charge) |
| **M2** | 4× M2.5 screws | Corners | FRU-4 housing |

### 3.4 Removal Procedure

**Tools Required:** 2.5mm hex key

**Steps:**
1. Power OFF system, remove battery (FRU-3)
2. Remove optics module (FRU-1) - see Section 2.4
3. Disconnect power connector J2 (squeeze tabs, pull)
4. Disconnect trigger connector J3 (squeeze tabs, pull)
5. Remove 4× M2.5 mounting screws
6. Lift processing module carefully (fan cable attached)
7. Note: USB-C is panel-mounted, stays with housing
8. Place in ESD bag

**Time:** 15 minutes (including FRU-1 removal)

### 3.5 Installation Procedure

**Steps:**
1. Verify replacement module part number
2. Verify SD card installed with correct software version
3. Remove from ESD bag, inspect for damage
4. Align module with housing standoffs
5. Insert 4× M2.5 mounting screws (torque: 0.3 Nm)
6. Connect trigger connector J3 (push until click)
7. Connect power connector J2 (push until click)
8. Reinstall optics module (FRU-1) - see Section 2.5
9. Install battery, power ON
10. Run self-test: **Menu → Diagnostics → Full Test**
11. Verify all functions

### 3.6 Calibration After Replacement

| Calibration | Required | Procedure |
|-------------|----------|-----------|
| IMU | **YES** | Auto-calibrate on power-up (30 sec) |
| Weapon Profile | No | Retained on SD card |
| AI Model | No | Pre-loaded on SD card |

### 3.7 Software Recovery

If SD card is corrupted or missing:

1. Obtain recovery SD card (VSM-L-MEM-002)
2. Insert into replacement module
3. Power ON - system will auto-configure
4. Re-enter weapon profile if needed

### 3.8 Fault Symptoms → FRU-2

| Symptom | Likely Cause | Action |
|---------|--------------|--------|
| No power-up | Processor failure | Replace FRU-2 |
| Boot loop | SD card corrupt | Replace SD card, then FRU-2 |
| No tracking | AI processing failure | Replace FRU-2 |
| IMU drift | IMU failure | Replace FRU-2 |
| Trigger not sensing | FSR failure | Replace FRU-2 |
| Overheating | Fan/heatsink failure | Replace FRU-2 |

---

## 4. FRU-3: POWER MODULE

### 4.1 Identification

| Field | Value |
|-------|-------|
| **FRU ID** | FRU-3 |
| **Part Number** | VSM-L-FRU-PWR |
| **Description** | Power Module Assembly |
| **Weight** | 220g |
| **Dimensions** | 70×50×30mm |

### 4.2 Components Included

| Item | Part Number | Description | Qty |
|------|-------------|-------------|-----|
| 1 | VSM-L-BAT-001 | 18650 Li-ion 3400mAh cell | 2 |
| 2 | VSM-L-PCB-002 | PMIC board (BMS + regulator) | 1 |
| 3 | VSM-L-DRV-001 | Solenoid MOSFET driver | 1 |
| 4 | VSM-L-SOL-001 | 12V push solenoid | 1 |
| 5 | VSM-L-CBL-002 | Internal power harness | 1 |
| 6 | VSM-L-CON-001 | USB-C connector (panel mount) | 1 |
| 7 | VSM-L-HSG-005 | Battery holder (PA66-GF30) | 1 |
| 8 | VSM-L-SPR-001 | Battery contacts (spring) | 4 |

### 4.3 Interfaces

| Interface | Type | Location | Mating Connector |
|-----------|------|----------|------------------|
| **J2** | 10-pin power | Top | FRU-2 carrier board |
| **J3** | 6-pin trigger | Top | FRU-2 carrier board |
| **BATT** | Battery door | Rear | Tool-free latch |
| **M3** | 4× M2.5 screws | Corners | FRU-4 housing |

### 4.4 Battery Removal (Tool-Free)

**Steps:**
1. Slide battery door latch (marked ◄)
2. Battery door swings open
3. Remove 2× 18650 cells (note polarity markings)
4. Insert fresh cells (+ toward front)
5. Close battery door until click

**Time:** 30 seconds

### 4.5 Full FRU-3 Removal Procedure

**Tools Required:** 2.5mm hex key

**Steps:**
1. Power OFF system, remove battery cells
2. Remove optics module (FRU-1)
3. Remove processing module (FRU-2)
4. Disconnect solenoid cable from trigger linkage
5. Remove 4× M2.5 mounting screws
6. Lift power module assembly
7. Note: USB-C panel connector disconnects

**Time:** 20 minutes (full disassembly required)

### 4.6 Installation Procedure

**Steps:**
1. Verify replacement module part number
2. Position module in housing
3. Connect USB-C panel connector
4. Insert 4× M2.5 mounting screws (torque: 0.3 Nm)
5. Route solenoid cable to trigger linkage
6. Reinstall FRU-2 and FRU-1
7. Insert battery cells
8. Power ON, verify charging LED
9. Run self-test: **Menu → Diagnostics → Power Test**

### 4.7 Calibration After Replacement

| Calibration | Required | Procedure |
|-------------|----------|-----------|
| None | — | Plug and play |

### 4.8 Fault Symptoms → FRU-3

| Symptom | Likely Cause | Action |
|---------|--------------|--------|
| No power | PMIC failure | Replace FRU-3 |
| Short runtime | Battery degraded | Replace batteries first |
| Not charging | BMS/USB failure | Replace FRU-3 |
| Trigger not firing | Solenoid failure | Replace FRU-3 |
| Trigger slow | Driver failure | Replace FRU-3 |
| Overheating battery | BMS failure | Replace FRU-3 immediately |

---

## 5. FRU-4: HOUSING MODULE

### 5.1 Identification

| Field | Value |
|-------|-------|
| **FRU ID** | FRU-4 |
| **Part Number** | VSM-L-FRU-HSG |
| **Description** | Housing Module Assembly |
| **Weight** | 350g (empty) |
| **Dimensions** | 150×80×100mm |

### 5.2 Components Included

| Item | Part Number | Description | Qty |
|------|-------------|-------------|-----|
| 1 | VSM-L-HSG-001 | Main housing (Al 6061-T6) | 1 |
| 2 | VSM-L-HSG-002 | Front cover (Al) | 1 |
| 3 | VSM-L-HSG-003 | Battery door (Al) | 1 |
| 4 | VSM-L-HSG-004 | Picatinny mount clamp | 1 |
| 5 | VSM-L-GSK-001 | Main gasket set (silicone) | 1 |
| 6 | VSM-L-GSK-002 | Battery door gasket | 1 |
| 7 | VSM-L-BTN-001 | Control buttons (3×) | 1 |
| 8 | VSM-L-LBL-001 | Labels and markings | 1 |
| 9 | VSM-L-HW-001 | Fastener kit (SS 304) | 1 |

### 5.3 Interfaces

| Interface | Type | Location | Notes |
|-----------|------|----------|-------|
| **Picatinny** | MIL-STD-1913 | Bottom | Clamp mechanism |
| **Front Cover** | 4× M3 screws | Front | Protects optics |
| **Battery Door** | Latch | Rear | Tool-free access |
| **USB Port** | Panel cutout | Left side | For USB-C |
| **Buttons** | 3× tactile | Top | Power, Mode, Select |

### 5.4 When to Replace FRU-4

- Housing cracked or damaged
- Picatinny mount bent or worn
- Gaskets degraded (IP65 compromised)
- Anodizing severely worn
- Threads stripped

### 5.5 Full System Disassembly

**Tools Required:** 2.5mm hex key, 3mm hex key

**Steps:**
1. Power OFF, remove battery
2. Remove FRU-1 (Optics)
3. Remove FRU-2 (Processing)
4. Remove FRU-3 (Power)
5. Transfer all modules to new housing
6. Reassemble in reverse order
7. Verify IP65 sealing

**Time:** 30-45 minutes (full rebuild)

### 5.6 Gasket Replacement (Maintenance)

**Part Number:** VSM-L-GSK-KIT (includes GSK-001, GSK-002)

**Steps:**
1. Disassemble to access gasket grooves
2. Remove old gaskets (pry gently)
3. Clean groove with IPA
4. Install new gaskets (ensure seated)
5. Reassemble, torque to spec
6. Perform IP65 verification if available

**Interval:** Every 3 years or after water exposure

### 5.7 Fault Symptoms → FRU-4

| Symptom | Likely Cause | Action |
|---------|--------------|--------|
| Water ingress | Gasket failure | Replace gaskets or FRU-4 |
| Dust inside | IP65 compromised | Replace gaskets or FRU-4 |
| Mount slipping | Clamp worn | Replace FRU-4 |
| Housing crack | Impact damage | Replace FRU-4 |
| Buttons stuck | Button failure | Replace FRU-4 |

---

## 6. SPARE PARTS LIST

### 6.1 FRU-Level Spares (Recommended Stock)

| Part Number | Description | Unit Cost | Stock Level |
|-------------|-------------|-----------|-------------|
| VSM-L-FRU-OPT | Optics Module | $175 | 1 per 10 units |
| VSM-L-FRU-PRC | Processing Module | $220 | 1 per 10 units |
| VSM-L-FRU-PWR | Power Module | $65 | 1 per 20 units |
| VSM-L-FRU-HSG | Housing Module | $150 | 1 per 50 units |
| VSM-L-BAT-001 | Battery 18650 (pair) | $8 | 1 per 2 units |

### 6.2 Consumables

| Part Number | Description | Unit Cost | Interval |
|-------------|-------------|-----------|----------|
| VSM-L-GSK-KIT | Gasket set | $15 | 3 years |
| VSM-L-MEM-001 | SD card 32GB | $10 | As needed |
| VSM-L-OPT-003 | Protective window | $15 | As needed |

### 6.3 Tools Required

| Tool | Description | Part Number | Notes |
|------|-------------|-------------|-------|
| Hex key 2.5mm | Module removal | Standard | Included in kit |
| Hex key 3mm | Housing screws | Standard | Included in kit |
| Torque driver | Precision torque | Optional | 0.3-0.5 Nm |
| ESD wrist strap | Static protection | Standard | Required |

---

## 7. TROUBLESHOOTING QUICK REFERENCE

### 7.1 Fault Isolation Matrix

| Symptom | Check First | Then Check | FRU to Replace |
|---------|-------------|------------|----------------|
| **Dead (no power)** | Battery charge | FRU-3 PMIC | FRU-3 |
| **No image** | FPC connection | Sensor/display | FRU-1 |
| **No tracking** | Camera image | AI processing | FRU-2 |
| **Trigger stuck** | Linkage | Solenoid | FRU-3 |
| **Drifting aim** | IMU cal | IMU sensor | FRU-2 |
| **Short battery** | Cell age | BMS | FRU-3 → Batteries |
| **Water damage** | Gaskets | Housing | FRU-4 |
| **Physical damage** | Mount/housing | — | FRU-4 |

### 7.2 Built-In Test (BIT) Codes

| Code | Meaning | FRU |
|------|---------|-----|
| E01 | Camera failure | FRU-1 |
| E02 | Display failure | FRU-1 |
| E03 | IMU failure | FRU-2 |
| E04 | AI processing error | FRU-2 |
| E05 | SD card error | FRU-2 (replace SD) |
| E06 | Battery low | Charge or FRU-3 |
| E07 | Solenoid failure | FRU-3 |
| E08 | Overtemperature | FRU-2 (fan) |
| E09 | Force sensor error | FRU-2 |

---

## 8. MAINTENANCE SCHEDULE

### 8.1 Operator Level (Daily/Weekly)

| Task | Frequency | Procedure |
|------|-----------|-----------|
| Visual inspection | Daily | Check for damage, clean lens |
| Battery check | Daily | Verify charge level |
| Function test | Weekly | Power on, verify tracking |
| Clean exterior | Weekly | Wipe with dry cloth |

### 8.2 Unit Level (Monthly/Quarterly)

| Task | Frequency | Procedure |
|------|-----------|-----------|
| Run full BIT | Monthly | Menu → Diagnostics → Full Test |
| Check fasteners | Quarterly | Verify torque, no loosening |
| Inspect gaskets | Quarterly | Check for wear, compression |
| Update software | As released | USB flash procedure |

### 8.3 Depot Level (Annual)

| Task | Frequency | Procedure |
|------|-----------|-----------|
| Full disassembly inspection | Annual | Check all components |
| Gasket replacement | 3 years | Replace GSK-KIT |
| Calibration verification | Annual | Boresight check |
| IP65 verification | Annual | Dust/water test |

---

## 9. DOCUMENT CONTROL

### 9.1 Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| Logistics | | | |
| Quality | | | |

### 9.2 Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-05 | Initial FRU specification. Defined 4 FRUs per L-ASM-05: Optics, Processing, Power, Housing. Includes part numbers, procedures, troubleshooting, spare parts list. |

---

*Requirements Source: [[V-SMASH_LITE_P1_requirements_list|LITE Requirements List v1.0]]*
*Product Spec: [[V-SMASH_LITE_product_spec|LITE Product Specification v1.1]]*
*Test Plan: [[V-SMASH_LITE_P4_test_plan|LITE Test Plan v1.0]]*
