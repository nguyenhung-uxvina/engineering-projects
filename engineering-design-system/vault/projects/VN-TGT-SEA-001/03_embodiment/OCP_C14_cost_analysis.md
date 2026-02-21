---
project: VN-TGT-SEA-001
phase: 3
step: "C14 — Cost Analysis"
group: OCP
version: 1.0
created: 2026-02-10
status: draft
---

# Step C14: Cost Analysis — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Purpose:** Bottom-up cost verification against Phase 1 estimate ($35,640 @10 units). Detailed BOM, labor, volume pricing, overhead, and cost risk analysis.
**Method:** Pahl & Beitz Embodiment Design, OCP Step C14 — Cost Analysis
**Input:** [[PRAD_A7_architecture_definition.md]] (8 modules, 7 interfaces), [[RISM_M4_material_analysis.md]] (5 material selections), [[../01_requirements/requirements_list.md]] (Section 11 cost targets)
**Cost Targets:** CST-001 ($36,000 @10), CST-002 ($27,000 @50), CST-004 ($280,000 dev budget), CST-007 (<=50% of SINKEX $1,610K)

---

## 1. Bill of Materials (BOM) — Single Unit

### 1.1 M1: Hull Assembly

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.1.01 | HDPE pontoon shell, 8.0m dia x 0.5m depth, 12mm wall (2-section) | PE100 HDPE, carbon-black stabilized | 1 | set | 2,800.00 | 2,800.00 | Local (rotomold/weld) |
| 1.1.02 | Closed-cell PU rigid foam fill, 35 kg/m3, pour-in-place | Marine-grade polyurethane | 200 | kg | 4.00 | 800.00 | Local |
| 1.1.03 | Hull section joint flanges (IF-07), HDPE welded ribs | PE100 HDPE | 2 | set | 120.00 | 240.00 | Local |
| 1.1.04 | EPDM gasket strip, 5mm x 50mm, hull joint seal | EPDM rubber | 6 | m | 8.00 | 48.00 | Local |
| 1.1.05 | Marine sealant (Sikaflex 291), hull joint + frame interface | Polyurethane sealant | 4 | tube | 18.00 | 72.00 | Import |
| 1.1.06 | Scupper drain fittings, 25mm flush-mount | HDPE | 8 | ea | 6.00 | 48.00 | Local |
| 1.1.07 | Deck non-skid coating (textured paint), grey | Marine deck paint | 3 | L | 25.00 | 75.00 | Import |
| 1.1.08 | Hull identification markings (stencil + paint) | Marine marking paint | 1 | set | 35.00 | 35.00 | Local |
| | **M1 Subtotal** | | | | | **4,118.00** | |

### 1.2 M2: Structural Frame Assembly

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.2.01 | Perimeter angle ring, L50x50x5, ~25.1m circumference | S235 HDG steel | 60 | kg | 1.30 | 78.00 | Local (Hoa Phat) |
| 1.2.02 | Radial cross members, C80x40x5 channel, 4 pcs x ~3.8m | S235 HDG steel | 40 | kg | 1.30 | 52.00 | Local (Hoa Phat) |
| 1.2.03 | Central mooring pad eye assembly (ring 25mm dia + base plate 200x200x10mm + backing plate 200x200x10mm) | S235 HDG steel | 1 | set | 85.00 | 85.00 | Local |
| 1.2.04 | Deck sockets, 65mm OD x 4mm wall x 200mm deep, welded tube with 160x160x8mm top flange | S235 HDG steel | 8 | ea | 22.00 | 176.00 | Local |
| 1.2.05 | Tow padeyes (ring 20mm dia + base plate 150x150x10mm + backing plate) | S235 HDG steel | 2 | ea | 45.00 | 90.00 | Local |
| 1.2.06 | Gusset plates and stiffeners (various) | S235 HDG steel | 20 | kg | 1.30 | 26.00 | Local |
| 1.2.07 | M16 x 60 Grade 8.8 HDG hex bolt (pad eye to frame) | Grade 8.8 HDG | 4 | ea | 2.80 | 11.20 | Local |
| 1.2.08 | M16 HDG flat washer | HDG steel | 4 | ea | 0.40 | 1.60 | Local |
| 1.2.09 | M16 HDG Nylock nut | HDG steel | 4 | ea | 0.60 | 2.40 | Local |
| 1.2.10 | M12 x 40 SS316 hex bolt (frame to hull, IF-01) | SS 316 | 84 | ea | 1.20 | 100.80 | Local |
| 1.2.11 | M12 SS316 flat washer (frame side) | SS 316 | 84 | ea | 0.25 | 21.00 | Local |
| 1.2.12 | M12 SS316 fender washer, 50x50x5mm (HDPE side) | SS 316 | 84 | ea | 1.50 | 126.00 | Local |
| 1.2.13 | M12 SS316 Nylock nut | SS 316 | 84 | ea | 0.45 | 37.80 | Local |
| 1.2.14 | M12 x 50 Grade 8.8 HDG hex bolt (tow padeye to frame) | Grade 8.8 HDG | 8 | ea | 1.80 | 14.40 | Local |
| 1.2.15 | M12 HDG flat washer (tow padeye) | HDG steel | 8 | ea | 0.30 | 2.40 | Local |
| 1.2.16 | M12 SS316 fender washer, 50x50x5mm (HDPE side, tow) | SS 316 | 8 | ea | 1.50 | 12.00 | Local |
| 1.2.17 | M12 HDG Nylock nut (tow padeye) | HDG steel | 8 | ea | 0.45 | 3.60 | Local |
| 1.2.18 | Sacrificial zinc anode, 1 kg block (mooring pad eye) | Zinc | 1 | ea | 12.00 | 12.00 | Local |
| 1.2.19 | Hot-dip galvanizing, frame + sockets + padeyes (~150 kg) | Zinc coating >=85um | 150 | kg | 0.90 | 135.00 | Local |
| | **M2 Subtotal** | | | | | **987.20** | |

### 1.3 M3: Mast Assembly (x8)

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.3.01 | Steel tube, 60mm OD x 4mm wall x 3000mm | S235 galv steel | 8 | ea | 14.50 | 116.00 | Local (Hoa Phat) |
| 1.3.02 | Base plate, 150x150x8mm, welded to tube | S235 steel | 8 | ea | 3.50 | 28.00 | Local |
| 1.3.03 | Top plate, 120x120x8mm, welded to tube | S235 steel | 8 | ea | 2.80 | 22.40 | Local |
| 1.3.04 | M12 clevis pin, SS316, 12mm dia x 80mm (locking) | SS 316 | 8 | ea | 4.50 | 36.00 | Local |
| 1.3.05 | R-clip (spring pin) for clevis pin retention | SS 316 | 16 | ea | 0.80 | 12.80 | Local |
| 1.3.06 | Safety wire, 0.8mm SS, for locking pin backup | SS 316 wire | 5 | m | 1.20 | 6.00 | Local |
| 1.3.07 | Hot-dip galvanizing, 8 mast assemblies (~130 kg) | Zinc coating >=85um | 130 | kg | 0.90 | 117.00 | Local |
| 1.3.08 | Tef-Gel anti-seize compound (socket bore, pins) | Marine anti-seize | 1 | tube | 28.00 | 28.00 | Import |
| | **M3 Subtotal (8 masts)** | | | | | **366.20** | |

### 1.4 M4: Reflector Assembly (x8)

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.4.01 | AM AlSi10Mg frame, LPBF printed, T5 heat treated, post-machined datums | AlSi10Mg (ASTM F3318) | 8 | ea | 900.00 | 7,200.00 | Import (ASEAN AM bureau) |
| 1.4.02 | CNC face plate, 800x800x3mm, fly-cut Ra<=10um | 6061-T6 Al (ASTM B209) | 24 | ea | 38.00 | 912.00 | Local (VN CNC shop) |
| 1.4.03 | Type III hard anodize, >=25um, AM frames (8 pcs) | Hard anodize coating | 8 | ea | 75.00 | 600.00 | ASEAN |
| 1.4.04 | Type II anodize, >=10um, face plates (24 pcs, batch) | Clear anodize coating | 24 | ea | 12.50 | 300.00 | Local |
| 1.4.05 | M6 x 20 SS316 hex bolt (face to frame) | SS 316 A4-80 | 96 | ea | 0.35 | 33.60 | Local |
| 1.4.06 | M6 SS316 flat washer | SS 316 | 96 | ea | 0.10 | 9.60 | Local |
| 1.4.07 | M6 SS316 Nylock nut | SS 316 | 96 | ea | 0.15 | 14.40 | Local |
| 1.4.08 | Alignment dowel pin, dia 5mm x 10mm, SS316 | SS 316 | 48 | ea | 0.60 | 28.80 | Local |
| 1.4.09 | Safety wire, 0.8mm SS, 2 loops per reflector | SS 316 wire | 8 | m | 1.20 | 9.60 | Local |
| 1.4.10 | Helicoil insert, M6 x 1.5D (AM frame bolt holes) | SS 304 | 96 | ea | 0.85 | 81.60 | Import |
| | **M4 Subtotal (8 reflectors)** | | | | | **9,189.60** | |

### 1.5 M5: Mast-Reflector Unit Interface (IF-04 hardware, x8)

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.5.01 | M10 x 30 Grade 8.8 HDG hex bolt (mast top to reflector) | Grade 8.8 HDG | 32 | ea | 1.40 | 44.80 | Local |
| 1.5.02 | Nordlock washer pair, M10, SS (anti-vibration) | SS 316 | 32 | pr | 2.80 | 89.60 | Import |
| 1.5.03 | M10 Nylock nut | SS 316 | 32 | ea | 0.55 | 17.60 | Local |
| 1.5.04 | Helicoil insert, M10 x 1.5D (AM frame flange) | SS 304 | 32 | ea | 1.20 | 38.40 | Import |
| 1.5.05 | Dowel pin, dia 8mm H7 x 20mm, SS316 | SS 316 | 16 | ea | 1.80 | 28.80 | Local |
| 1.5.06 | Nylon isolation bushing, M10, 2mm wall (galvanic isolation) | Nylon 6/6 | 32 | ea | 0.45 | 14.40 | Local |
| 1.5.07 | Nylon flat washer, 10mm ID x 20mm OD x 2mm (isolation) | Nylon 6/6 | 64 | ea | 0.20 | 12.80 | Local |
| 1.5.08 | Nylon dowel pin sleeve, 8mm ID (galvanic isolation, Al side) | Nylon 6/6 | 16 | ea | 0.35 | 5.60 | Local |
| 1.5.09 | Tef-Gel anti-seize, all IF-04 fasteners | Marine anti-seize | 1 | tube | 28.00 | 28.00 | Import |
| 1.5.10 | Safety wire, 0.8mm SS, 4 loops per unit (bolt pairs) | SS 316 wire | 10 | m | 1.20 | 12.00 | Local |
| | **M5 IF-04 Subtotal** | | | | | **292.00** | |

### 1.6 M6: GPS Beacon Assembly

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.6.01 | GNSS module (u-blox ZED-F9P or equivalent) | COTS electronics | 1 | ea | 250.00 | 250.00 | Import (China/Taiwan) |
| 1.6.02 | Iridium SBD modem (RockBLOCK 9603N or equiv.) | COTS electronics | 1 | ea | 280.00 | 280.00 | Import |
| 1.6.03 | GNSS active antenna, marine-grade, IP67 | COTS | 1 | ea | 45.00 | 45.00 | Import |
| 1.6.04 | Iridium patch antenna, marine-grade | COTS | 1 | ea | 55.00 | 55.00 | Import |
| 1.6.05 | Li-ion battery pack, 20 Wh (4x 18650, 3.7V 5400mAh) | Li-ion 18650 cells | 1 | pack | 65.00 | 65.00 | Import |
| 1.6.06 | Battery management PCB (charge/protect) | COTS PCB | 1 | ea | 25.00 | 25.00 | Import |
| 1.6.07 | IP67/68 waterproof enclosure, ABS/PC, 200x150x80mm | ABS/Polycarbonate | 1 | ea | 55.00 | 55.00 | Import |
| 1.6.08 | Waterproof cable glands, M16, IP68 | Nylon/SS | 3 | ea | 8.00 | 24.00 | Local |
| 1.6.09 | SS316 U-bolt clamp bracket (2x M8 U-bolts, saddle plate) | SS 316 | 1 | set | 45.00 | 45.00 | Local |
| 1.6.10 | L-bracket, 100x80x3mm SS316, for enclosure mounting | SS 316 | 1 | ea | 18.00 | 18.00 | Local |
| 1.6.11 | M6 x 16 SS316 bolt (enclosure to bracket) | SS 316 | 4 | ea | 0.35 | 1.40 | Local |
| 1.6.12 | M8 SS316 Nylock nut (U-bolt) | SS 316 | 4 | ea | 0.45 | 1.80 | Local |
| 1.6.13 | Wiring harness + connectors (internal) | Marine wire/connectors | 1 | set | 30.00 | 30.00 | Local |
| 1.6.14 | Desiccant pack (enclosure moisture control) | Silica gel | 2 | ea | 2.00 | 4.00 | Local |
| 1.6.15 | Conformal coating for PCB (marine protection) | Urethane coating | 1 | can | 15.00 | 15.00 | Import |
| | **M6 Subtotal** | | | | | **914.20** | |

### 1.7 M7: Mooring Kit (Medium Depth — 20-40m baseline)

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.7.01 | Danforth anchor, 50 kg, hot-dip galvanized | HDG cast steel | 1 | ea | 350.00 | 350.00 | Local |
| 1.7.02 | G30 proof coil chain, 16mm HDG, bottom section | G30 HDG steel | 20 | m | 7.50 | 150.00 | Local |
| 1.7.03 | Polyester braided rode, 20mm, 3-strand | Marine polyester | 60 | m | 4.50 | 270.00 | Local/ASEAN |
| 1.7.04 | Swivel, rated 5,000 kgf, HDG (chain-to-rode connection) | HDG forged steel | 1 | ea | 85.00 | 85.00 | Import |
| 1.7.05 | Bow shackle, 20mm pin, SWL 5,000 kgf, HDG (anchor to chain) | HDG forged steel | 1 | ea | 28.00 | 28.00 | Local |
| 1.7.06 | Bow shackle, 20mm pin, SWL 5,000 kgf, HDG (chain to swivel) | HDG forged steel | 1 | ea | 28.00 | 28.00 | Local |
| 1.7.07 | Bow shackle, 20mm pin, SWL 5,000 kgf, HDG (rode to pad eye) | HDG forged steel | 1 | ea | 28.00 | 28.00 | Local |
| 1.7.08 | SS316 thimble, 20mm rope (rode eye termination) | SS 316 | 2 | ea | 8.00 | 16.00 | Local |
| 1.7.09 | Mousing wire, 1.0mm galv, for shackle pins | Galvanized wire | 5 | m | 1.00 | 5.00 | Local |
| 1.7.10 | Trip line (polypropylene, 10mm, for anchor recovery) | PP rope | 50 | m | 1.50 | 75.00 | Local |
| 1.7.11 | Surface buoy, 300mm dia, orange, for trip line marker | HDPE foam | 1 | ea | 25.00 | 25.00 | Local |
| | **M7 Subtotal** | | | | | **1,060.00** | |

### 1.8 M8: Tow Kit

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.8.01 | Dyneema SK75 bridle rope, 16mm, 12-strand, 2 legs x 25m | UHMWPE (Dyneema) | 50 | m | 8.50 | 425.00 | Import |
| 1.8.02 | Spliced soft eyes with SS316 thimble (bridle terminations) | SS 316 thimble + splice | 4 | ea | 25.00 | 100.00 | Local (rigger) |
| 1.8.03 | Trailing drogue, 600mm dia conical, canvas/nylon | Heavy canvas/nylon | 1 | ea | 120.00 | 120.00 | Local |
| 1.8.04 | Bow shackle, 16mm pin, SWL 3,500 kgf, HDG (bridle to tow pad eye) | HDG forged steel | 2 | ea | 22.00 | 44.00 | Local |
| 1.8.05 | Bow shackle, 12mm pin, SWL 2,000 kgf, HDG (drogue attachment) | HDG forged steel | 1 | ea | 15.00 | 15.00 | Local |
| 1.8.06 | Mousing wire, 1.0mm galv, for shackle pins | Galvanized wire | 3 | m | 1.00 | 3.00 | Local |
| 1.8.07 | Protective rope bag (storage + transport) | Canvas | 1 | ea | 18.00 | 18.00 | Local |
| | **M8 Subtotal** | | | | | **725.00** | |

### 1.9 Miscellaneous Hardware & Consumables

| Item # | Description | Material | Qty | Unit | Unit Cost ($) | Extended ($) | Source |
|--------|-------------|----------|-----|------|---------------|-------------|--------|
| 1.9.01 | M12 SS316 hex bolt spare kit (IF-01, IF-06 spares) | SS 316 | 10 | ea | 1.20 | 12.00 | Local |
| 1.9.02 | Spare M12 clevis pin + R-clip (mast spares) | SS 316 | 2 | set | 5.30 | 10.60 | Local |
| 1.9.03 | Spare M6 bolt/nut/washer sets (reflector spares) | SS 316 | 12 | set | 0.60 | 7.20 | Local |
| 1.9.04 | Lifting slings, 2T WLL, polyester, 2m (handling) | Polyester webbing | 4 | ea | 12.00 | 48.00 | Local |
| 1.9.05 | Ratchet straps, 2T WLL, 5m (transport securing) | Polyester + steel | 8 | ea | 8.00 | 64.00 | Local |
| 1.9.06 | Reflective tape, SOLAS grade, for night visibility | Retro-reflective | 5 | m | 6.00 | 30.00 | Import |
| 1.9.07 | Identification plates, engraved SS (serial #, data plate) | SS 316 | 2 | ea | 15.00 | 30.00 | Local |
| 1.9.08 | Waterproof documentation pouch (deployment manual) | PVC/clear | 1 | ea | 8.00 | 8.00 | Local |
| | **Misc. Subtotal** | | | | | **209.80** | |

### 1.10 BOM Summary

| Module | Description | Subtotal ($) | % of BOM |
|--------|-------------|-------------|----------|
| **M1** | Hull Assembly | 4,118.00 | 23.2% |
| **M2** | Structural Frame Assembly | 987.20 | 5.6% |
| **M3** | Mast Assembly (x8) | 366.20 | 2.1% |
| **M4** | Reflector Assembly (x8) | 9,189.60 | 51.8% |
| **M5** | Mast-Reflector Interface HW | 292.00 | 1.6% |
| **M6** | GPS Beacon Assembly | 914.20 | 5.2% |
| **M7** | Mooring Kit (medium depth) | 1,060.00 | 6.0% |
| **M8** | Tow Kit | 725.00 | 4.1% |
| **Misc** | Spares, consumables, handling | 209.80 | 1.2% |
| | | | |
| | **BOM TOTAL** | **$17,862.00** | **100%** |

---

## 2. Labor Cost — Manufacturing Labor by Process

### 2.1 Labor Rate Basis (Vietnamese Manufacturing, 2026)

| Skill Category | Rate ($/hr) | Basis |
|----------------|-------------|-------|
| Welding (MIG/MAG, certified) | $10.00 | Hanoi/HCMC steel fabrication shops |
| CNC machining (3-axis, operator) | $12.00 | Vietnamese CNC job shops |
| Assembly, general (semi-skilled) | $8.00 | Factory assembly workers |
| Assembly, precision (reflector alignment) | $12.00 | Trained technicians, clean room |
| Quality control / inspection | $14.00 | QC engineers, CMM operators |
| Rotomolding / HDPE processing | $9.00 | Plastics manufacturing operators |
| Rigging / marine hardware | $8.00 | Marine riggers |
| Electronics assembly / test | $10.00 | Electronics technicians |
| Project engineering / supervision | $18.00 | Process engineering support |

### 2.2 Labor Breakdown by Process

| Process | Description | Hours | Rate ($/hr) | Cost ($) |
|---------|-------------|-------|-------------|----------|
| **HDPE hull fabrication** | Rotomold setup + cycle (2-section hull), foam pour + cure, scupper install, surface prep, section joining (IF-07 bolted flange) | 48 | $9.00 | $432.00 |
| **Steel frame fabrication** | CNC plasma cut angle, channel, plates; form perimeter ring; weld frame assembly, deck sockets (8x), pad eye, tow padeyes, gussets; deburr + clean | 40 | $10.00 | $400.00 |
| **Hot-dip galvanizing prep** | Transport frame + masts to galvanizer, masking, inspection on return | 4 | $8.00 | $32.00 |
| **Mast fabrication** | Cut 8 tubes to length, weld base plates (8x), weld top plates (8x), drill locking pin holes (8x), deburr all | 16 | $10.00 | $160.00 |
| **CNC face plate machining** | Setup vacuum fixture; fly-cut 24 plates (800x800x3mm) to Ra<=10um; drill 4x mounting holes + 2x dowel holes per plate; edge chamfer + deburr. Estimated 1.5 hr/plate including setup amortization | 36 | $12.00 | $432.00 |
| **Reflector assembly** | Install helicoils in 8 AM frames (96x M6 + 32x M10); bolt 24 face plates to 8 frames with alignment pins, torque + safety wire; CMM verify orthogonality per reflector. 2.5 hr/reflector | 20 | $12.00 | $240.00 |
| **Mast-reflector pre-assembly (IF-04)** | Mate 8 reflectors to 8 masts: install isolation bushings, dowel pins, bolt + torque + Nordlock + Nylock, safety wire. 1.0 hr/unit | 8 | $12.00 | $96.00 |
| **Frame-to-hull installation (IF-01)** | Lower frame into hull; align bolt holes; install 84x M12 SS bolts with fender washers; torque all to 40 N-m; apply Sikaflex sealant | 6 | $10.00 | $60.00 |
| **Pad eye + tow padeye install** | Install mooring pad eye (4x M16, torque 190 N-m), tow padeyes (2x 4x M12, torque 80 N-m); zinc anode attachment | 3 | $10.00 | $30.00 |
| **GPS beacon assembly** | Solder/connect GNSS + Iridium modules to PCB, install battery pack with BMS, conformal coat PCB, install in enclosure with cable glands, seal test; mount to U-bolt bracket; functional test (GPS fix + Iridium link) | 8 | $10.00 | $80.00 |
| **Mooring kit assembly** | Cut chain to length; splice rode eyes (2x) with thimbles; assemble shackle/swivel/chain/rode; rig trip line with buoy; label kit per depth variant | 4 | $8.00 | $32.00 |
| **Tow kit assembly** | Splice Dyneema bridle legs (4 eyes); install thimbles; assemble drogue; fit shackles; label and bag | 4 | $8.00 | $32.00 |
| **Final assembly** | Install mast-reflector units into deck sockets (trial fit, verify all 8 lock); mount GPS beacon on designated mast; connect all loose hardware; trial deployment sequence; pack for delivery | 8 | $8.00 | $64.00 |
| **Quality control — dimensional** | Verify hull diameter (8.0m +/-0.1m); frame socket positions (8x at 45deg +/-0.5deg); pad eye alignment; mast straightness; face plate flatness | 6 | $14.00 | $84.00 |
| **Quality control — CMM reflector** | CMM verification of orthogonality on 8 reflector assemblies (<=+/-0.1deg per face pair). 1.5 hr/reflector including setup | 12 | $14.00 | $168.00 |
| **Quality control — GPS endurance** | 72-hour battery endurance test on GPS beacon; verify position accuracy and Iridium connectivity at 1-hour intervals | 4 | $14.00 | $56.00 |
| **Quality control — surface finish** | Ra measurement on all 24 face plates (profilometer spot check); anodize thickness gauge on plates and frames; galvanize thickness on frame + masts | 4 | $14.00 | $56.00 |
| **Quality control — mooring proof load** | Pad eye proof load test at 1.5x SWL (6,804 kgf); shackle visual + cert review; chain sample link test | 4 | $14.00 | $56.00 |
| **Project engineering / documentation** | Process planning, work instructions, inspection reports, as-built documentation, shipping paperwork, deployment manual | 12 | $18.00 | $216.00 |
| | | | | |
| | **TOTAL LABOR** | **247 hr** | | **$2,726.00** |

### 2.3 Labor Summary by Category

| Category | Hours | Cost ($) | % of Labor |
|----------|-------|----------|------------|
| Fabrication (hull, frame, mast) | 108 | $1,024.00 | 37.6% |
| CNC machining (face plates) | 36 | $432.00 | 15.8% |
| Assembly (reflector, mast-refl, final) | 49 | $502.00 | 18.4% |
| Quality control (all categories) | 30 | $420.00 | 15.4% |
| Rigging (mooring, tow) | 8 | $64.00 | 2.3% |
| Electronics (GPS beacon) | 8 | $80.00 | 2.9% |
| Engineering / supervision | 12 | $216.00 | 7.9% |
| **TOTAL** | **247** | **$2,726.00** | **100%** |

---

## 3. Volume Pricing Analysis

### 3.1 Learning Curve Methodology

- **Manual processes** (welding, assembly, QC): 85% learning curve applied. Each doubling of cumulative production reduces unit labor by 15%.
- **Machine processes** (CNC, rotomold): 95% learning curve. Machine-paced, minimal learning effect.
- **AM frames**: Volume discount based on LPBF bureau batch pricing. 8 frames/unit; at 50 units = 400 frames in a batch order.
- **Purchased materials**: Bulk discount 5-15% at 50+ units; 10-20% at 100+ units.

### 3.2 Cost by Volume

| Item | @10 units | @50 units | @100 units | Notes |
|------|-----------|-----------|------------|-------|
| **M1: Hull Assembly** | | | | |
| HDPE shell (rotomold/weld) | $2,800 | $2,200 | $1,900 | Tooling amortized; cycle efficiency at volume |
| PU foam fill | $800 | $720 | $680 | Bulk foam pricing |
| Hull accessories + joint | $518 | $460 | $430 | Minor volume effect |
| *M1 subtotal* | *$4,118* | *$3,380* | *$3,010* | |
| **M2: Structural Frame** | | | | |
| Steel raw material | $507 | $450 | $420 | Bulk steel order discount 10-15% |
| Galvanizing | $135 | $120 | $110 | Batch galvanize efficiency |
| Fasteners (IF-01, IF-02, IF-06) | $345 | $295 | $265 | Bulk fastener pricing |
| *M2 subtotal* | *$987* | *$865* | *$795* | |
| **M3: Mast Assembly (x8)** | | | | |
| Steel tube + plates | $166 | $145 | $130 | Bulk tube purchase |
| Hardware (pins, clips, wire) | $55 | $48 | $44 | Minor volume effect |
| Galvanizing | $117 | $105 | $95 | Batch galvanize |
| Anti-seize | $28 | $24 | $20 | Bulk purchase |
| *M3 subtotal* | *$366* | *$322* | *$289* | |
| **M4: Reflector Assembly (x8)** | | | | |
| AM AlSi10Mg frames (8 pcs) | $7,200 | $4,800 | $3,600 | **KEY DRIVER**: batch LPBF pricing. 80 frames @50 units = $600/ea; 800 frames @100 = $450/ea |
| T5 heat treatment (incl. in AM) | (incl.) | (incl.) | (incl.) | Included in AM bureau pricing |
| Post-machining datums (incl. in AM) | (incl.) | (incl.) | (incl.) | CNC post-processing at AM bureau |
| CNC face plates (24 pcs) | $912 | $768 | $672 | Nesting 2-4 plates/setup at volume; $32/plate @50, $28/plate @100 |
| Type III hard anodize (8 frames) | $600 | $480 | $400 | Batch processing discount |
| Type II anodize (24 plates) | $300 | $240 | $192 | Batch processing discount |
| Fasteners + dowels + helicoils | $177 | $155 | $140 | Bulk fastener pricing |
| *M4 subtotal* | *$9,189* | *$6,443* | *$5,004* | |
| **M5: IF-04 Hardware** | | | | |
| Bolts, Nordlock, nuts, dowels | $220 | $190 | $170 | Bulk pricing |
| Isolation hardware (nylon) | $33 | $28 | $24 | Minor |
| Anti-seize + safety wire | $40 | $34 | $30 | Minor |
| *M5 subtotal* | *$292* | *$252* | *$224* | |
| **M6: GPS Beacon** | | | | |
| GNSS + Iridium modules | $530 | $470 | $420 | Volume discount from distributors |
| Antennas | $100 | $85 | $75 | Volume discount |
| Battery + BMS | $90 | $78 | $70 | Bulk cell pricing |
| Enclosure + hardware | $130 | $110 | $95 | Bulk enclosure order |
| Wiring + consumables | $64 | $55 | $48 | Minor |
| *M6 subtotal* | *$914* | *$798* | *$708* | |
| **M7: Mooring Kit** | | | | |
| Anchor | $350 | $300 | $270 | Bulk foundry order |
| Chain (20m G30 16mm) | $150 | $130 | $115 | Bulk chain purchase |
| Rode (60m polyester 20mm) | $270 | $235 | $210 | Bulk rope order |
| Swivel + shackles + accessories | $290 | $255 | $230 | Volume from chandler |
| *M7 subtotal* | *$1,060* | *$920* | *$825* | |
| **M8: Tow Kit** | | | | |
| Dyneema bridle (50m) | $425 | $370 | $330 | Bulk rope order |
| Splicing + thimbles | $100 | $80 | $65 | Learning curve on splicing |
| Drogue + shackles | $200 | $175 | $155 | Volume pricing |
| *M8 subtotal* | *$725* | *$625* | *$550* | |
| **Misc. Hardware** | $210 | $180 | $160 | Minor volume effect |
| | | | | |
| **BOM TOTAL** | **$17,862** | **$13,785** | **$11,565** | |
| | | | | |
| **Labor (with learning curve)** | | | | |
| Fabrication | $1,024 | $870 | $780 | 85% learning curve |
| CNC machining | $432 | $410 | $395 | 95% learning (machine-paced) |
| Assembly | $502 | $427 | $382 | 85% learning curve |
| Quality control | $420 | $357 | $320 | 85% learning; sampling at volume |
| Rigging | $64 | $54 | $49 | 85% learning |
| Electronics | $80 | $68 | $61 | 85% learning |
| Engineering | $216 | $130 | $80 | Amortizes at volume; WI established |
| **Labor subtotal** | **$2,726** (247 hr) | **$2,316** (216 hr) | **$2,067** (195 hr) | |
| | | | | |
| **DIRECT COST (BOM + Labor)** | **$20,588** | **$16,101** | **$13,632** | |

### 3.3 Volume Pricing Summary Chart

```
UNIT DIRECT COST BY VOLUME
═══════════════════════════════════════════════════════════
@10 units:   $20,588   ████████████████████████████████████
@50 units:   $16,101   ████████████████████████████
@100 units:  $13,632   ████████████████████████

Reduction @50 vs @10:   -$4,487 (-21.8%)
Reduction @100 vs @10:  -$6,956 (-33.8%)
Reduction @100 vs @50:  -$2,469 (-15.3%)

Key volume drivers:
  AM frames:  $7,200 → $4,800 → $3,600  (50% reduction @100 vs @10)
  Hull:       $4,118 → $3,380 → $3,010  (27% reduction)
  Labor:      $2,726 → $2,316 → $2,067  (24% reduction)
```

---

## 4. Overhead & Margin

### 4.1 Overhead Structure

| Overhead Category | @10 units | @50 units | @100 units | Basis |
|-------------------|-----------|-----------|------------|-------|
| **Tooling amortization** | | | | |
| Rotomold tooling ($15,000 mold) | $1,500 | $300 | $150 | /$N units |
| Frame welding jigs ($3,000) | $300 | $60 | $30 | /$N units |
| Mast welding fixture ($1,500) | $150 | $30 | $15 | /$N units |
| CNC vacuum fixture for face plates ($2,000) | $200 | $40 | $20 | /$N units |
| Reflector assembly alignment jig ($2,500) | $250 | $50 | $25 | /$N units |
| CMM fixture for reflector inspection ($1,000) | $100 | $20 | $10 | /$N units |
| *Tooling subtotal* | *$2,500* | *$500* | *$250* | |
| | | | | |
| **Quality control overhead** | | | | |
| First article inspection (detailed, 1st unit) | $500 | $100 | $50 | Amortized over run |
| RCS spot-check equipment rental | $200 | $40 | $20 | Per run, amortized |
| Material certifications (certs per batch) | $150 | $50 | $30 | Batch certs at volume |
| *QC overhead subtotal* | *$850* | *$190* | *$100* | |
| | | | | |
| **Project management / engineering** | | | | |
| Production engineering support (per unit) | $400 | $200 | $120 | Decreases with maturity |
| Documentation (as-built, test reports) | $150 | $80 | $50 | Template reuse at volume |
| *PM/Eng subtotal* | *$550* | *$280* | *$170* | |
| | | | | |
| **Facility overhead** | | | | |
| Factory floor rent, utilities, insurance (12% of direct cost) | $2,471 | $1,932 | $1,636 | 12% of direct cost |
| *Facility subtotal* | *$2,471* | *$1,932* | *$1,636* | |
| | | | | |
| **TOTAL OVERHEAD** | **$6,371** | **$2,902** | **$2,156** | |

### 4.2 Margin

| Item | @10 units | @50 units | @100 units | Basis |
|------|-----------|-----------|------------|-------|
| Subtotal (Direct + Overhead) | $26,959 | $19,003 | $15,788 | |
| Margin (10%) | $2,696 | $1,900 | $1,579 | Standard 10% margin |

### 4.3 Total Unit Cost

| Element | @10 units | @50 units | @100 units |
|---------|-----------|-----------|------------|
| BOM (materials) | $17,862 | $13,785 | $11,565 |
| Labor (manufacturing) | $2,726 | $2,316 | $2,067 |
| **Direct cost** | **$20,588** | **$16,101** | **$13,632** |
| Tooling amortization | $2,500 | $500 | $250 |
| QC overhead | $850 | $190 | $100 |
| PM / Engineering | $550 | $280 | $170 |
| Facility overhead (12%) | $2,471 | $1,932 | $1,636 |
| **Overhead total** | **$6,371** | **$2,902** | **$2,156** |
| **Subtotal** | **$26,959** | **$19,003** | **$15,788** |
| Margin (10%) | $2,696 | $1,900 | $1,579 |
| | | | |
| **UNIT COST** | **$29,655** | **$20,903** | **$17,367** |

---

## 5. Cost vs Target Analysis

### 5.1 Comparison to Phase 1 Estimate and Requirements

| Metric | Target (Phase 1) | C14 Bottom-Up | Variance | Status |
|--------|-------------------|---------------|----------|--------|
| Unit cost @10 units | $36,000 (CST-001) | **$29,655** | -$6,345 (-17.6%) | **PASS** — under target |
| Unit cost @50 units | $27,000 (CST-002) | **$20,903** | -$6,097 (-22.6%) | **PASS** — under target |
| Unit cost @100 units | ~$21,500 (estimate) | **$17,367** | -$4,133 (-19.2%) | **PASS** — under target |
| Development budget | $280,000 (CST-004) | See Note 1 | N/A | TBD — separate tracking |
| Cost vs SINKEX import | <=50% of $1,610,000 | **$29,655** = **1.8%** | -$775,345 | **PASS** — 98.2% savings |
| Cost per test (risk-adjusted) | <=$ 46,000 (CST-005) | ~$34,655 (unit + 1% missile loss ~$5K) | -$11,345 | **PASS** |

**Note 1:** Development budget ($280K) is tracked separately and includes prototyping, sea trials, RCS testing, and engineering labor across Phases 0-4. Not included in unit cost.

### 5.2 Phase 1 vs C14 Reconciliation

The C14 bottom-up estimate ($29,655 @10) is $5,985 lower than the Phase 1 top-down estimate ($35,640 @10). The difference is explained by:

| Factor | Phase 1 Estimate | C14 Actual | Difference | Explanation |
|--------|-----------------|------------|------------|-------------|
| HDPE pontoon | $7,000 | $4,118 | -$2,882 | Phase 1 included rotomold tooling in unit cost; C14 separates tooling into overhead and uses more detailed fabrication costing |
| Steel frame + mast sockets | $1,800 | $987 | -$813 | Phase 1 estimate was conservative; C14 detailed BOM shows lighter frame |
| Reflector masts (8x) | $800 | $366 | -$434 | Phase 1 estimate was higher; actual galv steel tube + plates cheaper |
| CNC face plates (24x) | $4,000 | $912 | -$3,088 | Phase 1 included significant contingency; C14 uses realistic VN CNC shop rates ($38/plate) |
| AM frames (8x) | $8,000 | $7,200 | -$800 | Slightly lower per-frame cost with batch of 8 |
| Assembly + QC (reflectors) | $1,000 | (in labor) | -$1,000 | Moved to labor section |
| Storm mooring | $1,700 | $1,060 | -$640 | Phase 1 was conservative on mooring kit cost |
| GPS beacon | $1,800 | $914 | -$886 | Detailed BOM shows lower COTS component costs |
| Tow equipment | $400 | $725 | +$325 | Phase 1 underestimated Dyneema bridle cost |
| Assembly + QC | $4,700 | $2,726 | -$1,974 | Phase 1 assembly estimate included contingency |
| Margin (10%) | $3,240 | $2,696 | -$544 | Lower base = lower margin |
| Foam fill | (in hull) | $800 | — | Phase 1 included in hull |
| Overhead | (in assembly) | $6,371 | — | Phase 1 bundled overhead into assembly |

**Conclusion:** Phase 1 estimate of $35,640 included significant contingency and conservative assumptions appropriate for early-stage estimation. The C14 bottom-up analysis confirms the product is feasible well within cost targets. The Phase 1 estimate provides **$5,985 contingency margin (17%)** which is appropriate for this development stage.

**Recommendation:** Maintain the Phase 1 target of $36,000 as the official cost ceiling for budgeting purposes. The C14 bottom-up cost of $29,655 is the engineering estimate. The delta provides contingency for:
- AM frame pricing uncertainty (see Section 7)
- HDPE hull fabrication method resolution (TBD-007)
- Exchange rate fluctuation (VND/USD)
- First-unit learning inefficiency

---

## 6. Local Content by Value

### 6.1 Component-Level Local Content

| Component | Value ($) | Source | Local? | Local Value ($) |
|-----------|-----------|--------|--------|-----------------|
| HDPE hull shell (rotomold/weld) | $2,800 | Vietnam (Binh Minh, Tan Dai Hung) | YES | $2,800 |
| PU foam fill | $800 | Vietnam (local PU supplier) | YES | $800 |
| Hull accessories (gasket, scupper, markings) | $518 | Mostly local | 80% | $414 |
| Steel frame raw material | $507 | Vietnam (Hoa Phat, Nam Kim) | YES | $507 |
| Frame fasteners (SS316, Grade 8.8) | $345 | Vietnam (marine hardware) | YES | $345 |
| Frame galvanizing | $135 | Vietnam (local HDG plant) | YES | $135 |
| Steel mast tubes + plates | $166 | Vietnam (Hoa Phat tube) | YES | $166 |
| Mast hardware (pins, clips, wire) | $83 | Local + import anti-seize | 70% | $58 |
| Mast galvanizing | $117 | Vietnam (local HDG plant) | YES | $117 |
| AM AlSi10Mg frames (8 pcs) | $7,200 | ASEAN AM bureau (Singapore/China) | NO | $0 |
| Type III hard anodize (8 frames) | $600 | ASEAN (at AM bureau) | NO | $0 |
| CNC face plates (24 pcs, material) | $912 | Material import (Korea/China); machining local | 60% | $547 |
| Type II anodize (24 plates) | $300 | Vietnam (local anodizer) | YES | $300 |
| Reflector fasteners + helicoils | $177 | Local hardware + import helicoils | 60% | $106 |
| IF-04 hardware (bolts, Nordlock, isolation) | $292 | Local + import Nordlock washers | 65% | $190 |
| GPS GNSS + Iridium modules | $530 | Import (China/Taiwan) | NO | $0 |
| GPS antennas | $100 | Import | NO | $0 |
| GPS battery + BMS | $90 | Import (China) | NO | $0 |
| GPS enclosure + hardware | $194 | Enclosure import; bracket local | 40% | $78 |
| Danforth anchor | $350 | Vietnam (local foundry) | YES | $350 |
| G30 HDG chain | $150 | Vietnam (marine chandler) | YES | $150 |
| Polyester rode | $270 | Vietnam/ASEAN | 60% | $162 |
| Mooring accessories (swivel, shackles, thimbles) | $290 | Local + import swivel | 60% | $174 |
| Dyneema bridle rope | $425 | Import (Dyneema is Dutch/EU) | NO | $0 |
| Tow splicing + thimbles | $100 | Local (rigger) | YES | $100 |
| Tow drogue + shackles | $200 | Local fabrication | YES | $200 |
| Misc. hardware (spares, slings, straps) | $210 | Mostly local | 80% | $168 |
| **All manufacturing labor** | **$2,726** | **Vietnam (all processes)** | **YES** | **$2,726** |
| **All overhead (facility, PM, QC)** | **$6,371** | **Vietnam** | **YES** | **$6,371** |
| **Margin** | **$2,696** | **Vietnam entity** | **YES** | **$2,696** |
| | | | | |
| **TOTAL** | **$29,655** | | | **$19,160** |

### 6.2 Local Content Summary

| Category | Value ($) | Local ($) | Local % |
|----------|-----------|-----------|---------|
| Vietnamese materials + fabrication | $7,685 | $7,185 | 93.5% |
| Vietnamese manufacturing labor | $2,726 | $2,726 | 100% |
| Vietnamese overhead + margin | $9,067 | $9,067 | 100% |
| ASEAN AM frames + processing | $7,800 | $0 | 0% |
| Imported components (GPS, Dyneema, helicoils, Nordlock) | $1,498 | $0 | 0% |
| Mixed source (partial local) | $879 | $582 | 66% |
| | | | |
| **TOTAL** | **$29,655** | **$19,160** | **64.6%** |

### 6.3 Local Content Breakdown

```
LOCAL CONTENT ANALYSIS — VN-TGT-SEA-001-H
══════════════════════════════════════════════════════════

100% VIETNAMESE (Total: $19,578):
  Hull fabrication + foam         $3,600  ████████████████████  100%
  Steel frame material + HDG     $  642  ████████████████████  100%
  Steel mast material + HDG      $  283  ████████████████████  100%
  CNC face plate machining       $  547  ████████████████████  100%
  Type II anodize (plates)       $  300  ████████████████████  100%
  Anchor                         $  350  ████████████████████  100%
  Chain                          $  150  ████████████████████  100%
  Tow splicing + drogue          $  300  ████████████████████  100%
  All manufacturing labor        $2,726  ████████████████████  100%
  Overhead + margin              $9,067  ████████████████████  100%

PARTIAL LOCAL (Total: $1,282 local of $1,879):
  Hull accessories               $  414  ████████████████      80%
  Mast hardware                  $   58  ██████████████        70%
  Reflector fasteners            $  106  ████████████          60%
  IF-04 hardware                 $  190  █████████████         65%
  GPS bracket/enclosure          $   78  ████████              40%
  Rode + mooring accessories     $  336  ████████████          60%
  Misc hardware                  $  168  ████████████████      80%

IMPORTED / ASEAN (Total: $0 local of $9,298):
  AM AlSi10Mg frames             $7,200  ░░░░░░░░░░░░░░░░░░░  0%
  Type III hard anodize          $  600  ░░░░░░░░░░░░░░░░░░░  0%
  GPS electronics                $  720  ░░░░░░░░░░░░░░░░░░░  0%
  Dyneema rope                   $  425  ░░░░░░░░░░░░░░░░░░░  0%
  Nordlock, helicoils, misc      $  353  ░░░░░░░░░░░░░░░░░░░  0%

RESULT: $19,160 / $29,655 = 64.6% LOCAL CONTENT
TARGET: >=85% (PRD-002)      STATUS: GAP of 20.4 percentage points
```

### 6.4 Path to Higher Local Content

| Strategy | Impact | Local % After | Feasibility |
|----------|--------|---------------|-------------|
| **Current baseline** | — | **64.6%** | Current state |
| **A: Classify ASEAN AM as "regional-local"** | +$7,800 local | **90.9%** | Policy decision — ASEAN defense procurement framework |
| **B: Switch to CNC-only frames (6061-T6)** | AM frames $7,200 -> local CNC frames $3,600 + material $800 import | **76.8%** | High — proven technology, VN CNC capable. +-0.3deg accuracy tradeoff |
| **C: Develop VN LPBF AM capability** | +$7,800 local (long term) | **90.9%** | Low — 2-3 year timeline, no current VN LPBF quality |
| **D: Source Dyneema from VN/ASEAN distributor** | +$425 local | **66.1%** | Medium — limited local distribution |
| **B+D combined** | CNC frames + local Dyneema | **78.2%** | High — both achievable |

**Recommendation:** Pursue Strategy A (ASEAN regional classification) as primary path. Maintain Strategy B (CNC fallback) as contingency if ASEAN classification is not accepted. Even at 64.6%, the THANH TRI-H represents a massive improvement over 0% local content with imported systems.

---

## 7. Cost Risk Assessment

### 7.1 Risk Register

| Risk ID | Risk Factor | Impact | Probability | Cost Impact | Mitigation |
|---------|-------------|--------|-------------|-------------|------------|
| CR-01 | **AM frame pricing +20%** | AM frames increase from $7,200 to $8,640 per unit | Medium (30%) | +$1,440/unit | Qualified 2+ AM bureaus (PRD-003) for competitive pricing; CNC fallback option |
| CR-02 | **AM frame pricing -20%** | AM frames decrease from $7,200 to $5,760 per unit (batch optimization) | Medium (40%) | -$1,440/unit | Opportunity — negotiate batch contracts at 50+ units |
| CR-03 | **HDPE hull method: rotomold vs weld** | Rotomold requires $15K tooling; welded hull may cost +$800/unit but no tooling | Medium (50%) | +$800/unit (weld) or -$1,300/unit @50+ (rotomold) | Resolve TBD-007 with supplier visits; prototype both methods |
| CR-04 | **VND/USD exchange rate +10%** | All local costs denominated in VND; 10% VND depreciation reduces USD-equivalent labor/overhead costs | Medium (25%) | -$900/unit (favorable) | Natural hedge — reduces unit cost in USD |
| CR-05 | **VND/USD exchange rate -10%** | VND appreciation increases local costs in USD | Low (15%) | +$900/unit (unfavorable) | Small risk — VND historically stable or slightly depreciating |
| CR-06 | **Steel price +25%** | Global steel price increase affects frame and masts | Medium (20%) | +$170/unit | Small impact — steel is only 3% of unit cost; local supply provides buffer |
| CR-07 | **Aluminum 6061-T6 price +30%** | Global Al price increase affects face plates | Low (15%) | +$270/unit | Lock in pricing with Korean/Chinese supplier at order time |
| CR-08 | **CNC shop capacity constraint** | Vietnamese CNC shops fully booked; lead time increases | Medium (25%) | +$200/unit (expedite premium) | Qualify 2-3 CNC shops; schedule orders 4-6 weeks ahead |
| CR-09 | **GPS COTS component obsolescence** | GNSS or Iridium module discontinued | Low (10%) | +$100-300/unit (redesign) | Use widely-stocked modules with long availability |
| CR-10 | **First-unit learning loss** | First 2-3 units significantly more expensive than estimate | High (70%) | +$3,000 for first unit | Expected — 85% learning curve accounts for this; budget at Phase 1 ceiling ($36K) |

### 7.2 Monte Carlo Summary (Simplified)

```
COST RISK DISTRIBUTION (@10 units)
═══════════════════════════════════════════════════════

Baseline (C14):           $29,655
P10 (optimistic):         $27,200   (favorable AM + FX)
P50 (expected):           $30,400   (baseline + minor risks)
P90 (pessimistic):        $34,800   (AM +20% + weld hull + FX unfavorable)
Phase 1 ceiling:          $36,000   ← CST-001 requirement

         P10     P50              P90     Ceiling
          │       │                │       │
  $27K ───┤───────┤────────────────┤───────┤──── $36K
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
          │←── 80% confidence ────→│
                                           │← 6% contingency

CONCLUSION: Even at P90, unit cost ($34,800) is below the $36,000 ceiling.
Phase 1 target provides adequate contingency margin.
```

### 7.3 Sensitivity Analysis — Top 3 Cost Drivers

| Rank | Cost Driver | % of Unit Cost | Sensitivity | Control |
|------|-------------|----------------|-------------|---------|
| 1 | AM AlSi10Mg frames | 24.3% ($7,200) | +-$1,440 per +-20% | Low — external ASEAN pricing |
| 2 | HDPE hull assembly | 13.9% ($4,118) | +-$1,000 per method | Medium — resolve TBD-007 |
| 3 | Manufacturing labor | 9.2% ($2,726) | +-$400 per +-15% rate | High — Vietnamese labor rates stable |

---

## 8. Cost Reduction Roadmap

### 8.1 Cost Trajectory: @10 to @100 Units

```
COST REDUCTION ROADMAP — VN-TGT-SEA-001-H
═══════════════════════════════════════════════════════════════

Unit Cost ($)
$35K ┤
     │  Phase 1 ceiling: $36,000
$30K ┤  ■ @10 units: $29,655
     │    │
$25K ┤    │ ─── Lever 1: AM batch pricing (80→400 frames)
     │    ▼        saves $2,400/unit
$20K ┤  ■ @50 units: $20,903
     │    │
     │    │ ─── Lever 2: Tooling fully amortized
$17K ┤    │        saves $500/unit
     │    │ ─── Lever 3: Labor learning curve (195 hr vs 247 hr)
$15K ┤    ▼        saves $659/unit
     │  ■ @100 units: $17,367
     │    │
$13K ┤    │ ─── Lever 4: Vietnamese AM capability (future)
     │    ▼        potential $2,000-3,000/unit savings
$12K ┤  ■ @100+VN-AM: ~$14,000-15,000 (projected)
     │
     └──┬─────────┬─────────┬─────────┬───────────
       10        50       100       200  units
```

### 8.2 Key Cost Reduction Levers

| Lever | Trigger | Savings/Unit | Cumulative |
|-------|---------|-------------|------------|
| **L1: AM batch pricing** | 50+ units (400+ frames) | $2,400 | $2,400 |
| **L2: Tooling amortization** | 50+ units | $2,000 | $4,400 |
| **L3: Labor learning curve** | 50+ units (85% curve) | $410 | $4,810 |
| **L4: Material volume discounts** | 50+ units | $1,677 | $6,487 |
| **L5: Overhead efficiency** | 50+ units (established processes) | $1,369 | $7,856 |
| **L6: CNC nesting optimization** | 100+ units (4 plates/setup) | $240 | $8,096 |
| **L7: Vietnamese LPBF AM** | 200+ units (2-3 year timeline) | $2,000-3,000 | $10,000-11,000 |

### 8.3 Lever Details

**L1 — AM Batch Pricing** (Largest single lever)
- At 10 units: 80 frames ordered = $900/frame
- At 50 units: 400 frames ordered = $600/frame (batch LPBF nesting, continuous build plate utilization, powder bulk pricing)
- At 100 units: 800 frames = $450/frame (dedicated build plate schedule, negotiated contract pricing)
- Mechanism: LPBF cost is dominated by machine time; batching frames on large build plates (4-6 per plate) reduces per-part machine time and setup overhead

**L2 — Tooling Amortization**
- Rotomold ($15K), frame jigs ($3K), mast fixture ($1.5K), CNC fixture ($2K), alignment jig ($2.5K), CMM fixture ($1K) = $25K total tooling
- At 10 units: $2,500/unit
- At 50 units: $500/unit
- At 100 units: $250/unit

**L3 — Labor Learning Curve**
- Manual processes follow 85% learning curve: each doubling of cumulative units reduces unit labor time by 15%
- From unit 1 to unit 10: significant learning on hull fabrication, frame welding, reflector assembly
- From unit 10 to unit 50: learning continues; work instructions refined; operator proficiency stabilizes
- Machine-paced processes (CNC) follow 95% curve — minimal learning effect but setup time amortization

**L4 — Material Volume Discounts**
- Steel: 10-15% discount on bulk Hoa Phat orders (1,500+ kg vs 300 kg)
- HDPE: PE100 resin pricing improves at ton quantities
- Fasteners: 20-30% discount on bulk SS316 hardware from marine suppliers
- Rope/chain: 10-15% discount on bulk marine hardware

**L5 — Overhead Efficiency**
- Production engineering: work instructions established after first 10 units; PM overhead drops from $550/unit to $170/unit
- QC: statistical sampling replaces 100% inspection after process capability proven (Cpk > 1.33)
- Facility: fixed overhead amortized over more units

**L7 — Vietnamese LPBF AM (Future)**
- If a Vietnamese LPBF service bureau is established or qualifies for AlSi10Mg printing:
  - Eliminates ASEAN import cost (shipping, duties, lead time)
  - Reduces per-frame cost to $500-600 (lower labor rates than Singapore)
  - Increases local content to >85% immediately
  - Timeline: 2-3 years for quality establishment

### 8.4 Cost Reduction Target Milestones

| Milestone | Volume | Unit Cost | Savings vs @10 | % Reduction |
|-----------|--------|-----------|----------------|-------------|
| Production start | 10 units | $29,655 | — | Baseline |
| Series production | 50 units | $20,903 | $8,752 | 29.5% |
| Mature production | 100 units | $17,367 | $12,288 | 41.4% |
| VN AM capability | 100+ units | ~$14,500 | ~$15,155 | ~51.1% |

---

## 9. Development Budget Allocation (Reference)

Per CST-004, the total development budget is $280,000. Approximate allocation:

| Phase | Activity | Budget ($) | Status |
|-------|----------|-----------|--------|
| Phase 0 | ODI analysis, stakeholder survey | $10,000 | Complete |
| Phase 1 | Requirements, standards mapping | $8,000 | Complete |
| Phase 2 | Conceptual design, concept evaluation | $12,000 | Complete |
| Phase 3 | Embodiment design, material selection, layout | $25,000 | In progress |
| Phase 3 | Prototype fabrication (1 unit, hull + reflectors + mooring) | $55,000 | Pending |
| Phase 3 | AM frame first article (8 frames, initial order) | $12,000 | Pending |
| Phase 3 | RCS measurement (anechoic chamber or outdoor range) | $15,000 | Pending |
| Phase 3 | Sea trial (SS 5 deployment, 72h endurance) | $30,000 | Pending |
| Phase 3 | Structural test (mast fatigue, pad eye proof load) | $10,000 | Pending |
| Phase 4 | Detail design, CAD, production drawings | $20,000 | Pending |
| Phase 4 | Pilot batch (3 units, pre-production) | $75,000 | Pending |
| Phase 4 | Live-fire demonstration | $25,000 | Pending |
| | Contingency (10%) | $28,000 | Reserved |
| | **TOTAL** | **$325,000** | Over budget by $45K |

**Note:** The development budget at $280K is tight. The prototype + pilot batch alone consumes $130K. Options to stay within budget:
1. Reduce pilot batch from 3 to 2 units (saves $25K)
2. Combine RCS measurement with sea trial (saves $10K)
3. Use outdoor RCS range instead of anechoic chamber (saves $5K)
4. Defer live-fire demo to operational funding (saves $25K)

With options 1+2+3, revised development budget = $285K (within 2% of target).

---

## 10. Cross-References

### Phase 3 Documents
- [[PRAD_A7_architecture_definition.md]] — Module decomposition (M1-M8), interface specifications (IF-01 to IF-07), mass budget, containment hierarchy
- [[RISM_M4_material_analysis.md]] — Material selection matrices (5 component groups), lifecycle cost estimates, local content analysis, galvanic compatibility
- [[RISM_R1_requirements_identification.md]] — 74 embodiment-determining requirements
- [[RISM_I2_critical_requirements.md]] — Critical requirements prioritization
- [[RISM_S3_material_selection.md]] — Material candidate screening
- [[PRAD_D8_design_structure.md]] — Structural sizing details

### Phase 1 Source Documents
- [[../01_requirements/requirements_list.md]] — Section 11: Cost estimates (Rev B.1), CST-001 through CST-007

### Phase 2 Source Documents
- [[../02_conceptual/concept_selection.md]] — Concept A cost baseline ($35,640 @10 units)

### Downstream Documents
- OCP_C15_production_plan.md — Production planning (to be created)
- Phase 4: Detailed procurement BOM, supplier contracts, tooling orders

---

*End of Step C14: Cost Analysis. Bottom-up verification confirms unit cost of $29,655 @10 units, well within the Phase 1 target of $36,000 (CST-001). AM reflector frames remain the dominant cost element at 24.3% of unit cost. Volume pricing to 50-100 units achieves 30-41% cost reduction driven primarily by AM batch pricing and tooling amortization. Local content at 64.6% falls short of 85% target due to ASEAN-sourced AM frames -- resolution path depends on procurement policy classification of ASEAN sources.*
