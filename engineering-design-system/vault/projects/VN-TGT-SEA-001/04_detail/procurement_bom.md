---
project: VN-TGT-SEA-001
phase: 4
type: procurement
version: 1.0
created: 2026-02-11
status: draft
---

# Procurement BOM — VN-TGT-SEA-001

**Product:** Fixed Sea Target with Hyperganic Enhancement ("THANH TRI-H")
**Lot Size:** 10 units (first production lot)
**Purpose:** Production-ready procurement document defining every purchased item, approved suppliers, lead times, lot quantities (with overage), costs, and delivery schedule. This document is the master purchase order reference for Lot 1.
**Input:** [[../03_embodiment/OCP_C14_cost_analysis.md]] (BOM, labor, volume pricing), [[../03_embodiment/OCP_P15_production_planning.md]] (suppliers, lead times, make/buy, schedule), [[../03_embodiment/DECS_D9_detail_specification.md]] (material specifications, tolerances)
**General Notes:**
- All costs in USD unless noted. VND conversion at 25,000 VND/USD (2026 reference rate).
- Overage factor: 5% for standard items, 10% for AM frames and CNC face plates (QC reject allowance).
- Payment terms default: 30% advance on PO, 70% on delivery and inspection acceptance.

---

## 1. Procurement Summary

| Parameter | Value |
|-----------|-------|
| **Total line items** | 73 |
| **Total BOM cost (10-unit lot)** | $187,851 |
| **Per-unit BOM cost** | $18,785 |
| **C14 baseline per-unit BOM** | $17,862 |
| **Variance to C14** | +$923/unit (+5.2%) — overage for QC rejects |
| **Number of distinct suppliers** | 18 |
| **Number of import sources** | 7 |
| **Local content (material only)** | 62.5% by value |
| **Procurement timeline** | 16 weeks (Week -2 to Week 14) |
| **Long-lead items (>3 weeks)** | 4 items (Dyneema, GPS modules, Al sheet, AM frames) |
| **Assembly start target** | Week 7 (all materials converged for Unit 1) |

---

## 2. Procurement BOM by Module

### 2.1 M1: Hull Assembly

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1101 | HDPE pontoon shell, 8.0m dia x 0.5m depth, 12mm wall (2-section) | PE100 HDPE per ASTM D3350 Cell Class 345464C, carbon-black UV-stabilized, MFI <=0.4 g/10min, density 940-960 kg/m3 | 1 set | 11 sets (10% overage) | Binh Minh Plastics (BMP) | HCMC | 3 weeks | $2,800.00 | $30,800.00 | Buy | Local |
| VN-TGT-001-P-1102 | Closed-cell PU rigid foam, 35 kg/m3, 2-component pour-in-place | Marine-grade polyurethane per ASTM D1622, D2842 (water abs <=3%), compressive strength >=150 kPa per ASTM D1621 | 200 kg | 2,100 kg (5% overage) | Dong A Chemical | Binh Duong | 2 weeks | $4.00/kg | $8,400.00 | Make (pour) | Local |
| VN-TGT-001-P-1103 | Hull section joint flanges (IF-07), HDPE welded ribs | PE100 HDPE, integral to hull | 2 sets | 22 sets (10% overage) | Binh Minh Plastics (BMP) | HCMC | Incl. in hull | $120.00 | $2,640.00 | Buy | Local |
| VN-TGT-001-P-1104 | EPDM gasket strip, 5mm x 50mm, hull joint seal | EPDM rubber, Shore A 60 +/-5 | 6 m | 63 m (5% overage) | Local rubber supplier | HCMC | 1 week | $8.00/m | $504.00 | Buy | Local |
| VN-TGT-001-P-1105 | Marine sealant (Sikaflex 291), hull joint + frame interface | Polyurethane sealant, marine grade | 4 tubes | 42 tubes (5% overage) | Sika Vietnam (distributor) | HCMC | 1 week | $18.00 | $756.00 | Buy | Import |
| VN-TGT-001-P-1106 | Scupper drain fittings, 25mm flush-mount | HDPE | 8 ea | 84 ea (5% overage) | Binh Minh Plastics (BMP) | HCMC | 1 week | $6.00 | $504.00 | Buy | Local |
| VN-TGT-001-P-1107 | Deck non-skid coating (textured paint), grey | Marine deck paint, UV-stabilized | 3 L | 32 L (5% overage) | International Paint (distributor) | HCMC | 1 week | $25.00/L | $800.00 | Buy | Import |
| VN-TGT-001-P-1108 | Hull identification markings (stencil + paint) | Marine marking paint | 1 set | 11 sets (10% overage) | Local sign shop | Hai Phong | 1 week | $35.00 | $385.00 | Buy | Local |
| | **M1 Subtotal** | | | | | | | | **$44,789.00** | | |

### 2.2 M2: Structural Frame Assembly

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1201 | Perimeter angle ring, L50x50x5, ~25.1m circumference | S235JR per EN 10025-2, yield >=235 MPa | 60 kg | 630 kg (5% overage) | Hoa Phat Group | Hai Duong | 2 weeks | $1.30/kg | $819.00 | Buy | Local |
| VN-TGT-001-P-1202 | Radial cross members, C80x40x5 channel, 4 pcs x ~3.8m | S235JR per EN 10025-2 | 40 kg | 420 kg (5% overage) | Hoa Phat Group | Hai Duong | 2 weeks | $1.30/kg | $546.00 | Buy | Local |
| VN-TGT-001-P-1203 | Central mooring pad eye assembly (ring 25mm dia + base 200x200x14mm + backing 200x200x14mm) | S235JR HDG per ASTM A123, UT-inspected weld per AWS D1.1 | 1 set | 11 sets (10% overage) | Truong Hai Mechanical | Hai Phong | 3 weeks | $85.00 | $935.00 | Buy | Local |
| VN-TGT-001-P-1204 | Deck sockets, 116mm OD x 8mm wall x 150mm deep, 160x160x8mm top flange | S235JR HDG, bore reamed to 100mm ID, Ra <=12.5um | 8 ea | 88 ea (10% overage) | Truong Hai Mechanical | Hai Phong | 3 weeks | $22.00 | $1,936.00 | Buy | Local |
| VN-TGT-001-P-1205 | Tow padeyes (ring 20mm dia + base plate 150x150x10mm + backing) | S235JR HDG | 2 ea | 22 ea (10% overage) | Truong Hai Mechanical | Hai Phong | 3 weeks | $45.00 | $990.00 | Buy | Local |
| VN-TGT-001-P-1206 | Gusset plates and stiffeners (various) | S235JR | 20 kg | 210 kg (5% overage) | Hoa Phat Group | Hai Duong | 2 weeks | $1.30/kg | $273.00 | Buy | Local |
| VN-TGT-001-P-1207 | M16 x 60 Grade 8.8 HDG hex bolt (pad eye to frame) | Grade 8.8 HDG per ISO 898-1 | 4 ea | 44 ea (10% overage) | Bulong Viet | Hanoi | 2 weeks | $2.80 | $123.20 | Buy | Local |
| VN-TGT-001-P-1208 | M16 HDG flat washer | HDG steel per DIN 125 | 4 ea | 44 ea | Bulong Viet | Hanoi | 2 weeks | $0.40 | $17.60 | Buy | Local |
| VN-TGT-001-P-1209 | M16 HDG Nylock nut | HDG steel per DIN 985 | 4 ea | 44 ea | Bulong Viet | Hanoi | 2 weeks | $0.60 | $26.40 | Buy | Local |
| VN-TGT-001-P-1210 | M12 x 40 SS316 hex bolt (frame to hull, IF-01) | SS 316 A4-70 per ISO 3506-1 | 84 ea | 882 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $1.20 | $1,058.40 | Buy | Local |
| VN-TGT-001-P-1211 | M12 SS316 flat washer (frame side) | SS 316 per DIN 125 | 84 ea | 882 ea | Bulong Viet | Hanoi | 2 weeks | $0.25 | $220.50 | Buy | Local |
| VN-TGT-001-P-1212 | M12 SS316 fender washer, 50x50x5mm (HDPE side) | SS 316, laser-cut | 84 ea | 882 ea | Bulong Viet | Hanoi | 2 weeks | $1.50 | $1,323.00 | Buy | Local |
| VN-TGT-001-P-1213 | M12 SS316 Nylock nut | SS 316 A4-70 per DIN 985 | 84 ea | 882 ea | Bulong Viet | Hanoi | 2 weeks | $0.45 | $396.90 | Buy | Local |
| VN-TGT-001-P-1214 | M12 x 50 Grade 8.8 HDG hex bolt (tow padeye) | Grade 8.8 HDG | 8 ea | 84 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $1.80 | $151.20 | Buy | Local |
| VN-TGT-001-P-1215 | M12 HDG flat washer (tow padeye) | HDG steel | 8 ea | 84 ea | Bulong Viet | Hanoi | 2 weeks | $0.30 | $25.20 | Buy | Local |
| VN-TGT-001-P-1216 | M12 SS316 fender washer, 50x50x5mm (HDPE side, tow) | SS 316 | 8 ea | 84 ea | Bulong Viet | Hanoi | 2 weeks | $1.50 | $126.00 | Buy | Local |
| VN-TGT-001-P-1217 | M12 HDG Nylock nut (tow padeye) | HDG steel | 8 ea | 84 ea | Bulong Viet | Hanoi | 2 weeks | $0.45 | $37.80 | Buy | Local |
| VN-TGT-001-P-1218 | Sacrificial zinc anode, 1 kg block | Zinc per MIL-A-18001 | 1 ea | 11 ea (10% overage) | Vietnam Marine Equipment | Hai Phong | 1 week | $12.00 | $132.00 | Buy | Local |
| VN-TGT-001-P-1219 | Hot-dip galvanizing service, frame + sockets + padeyes (~150 kg/unit) | Zinc coating >=85um per ASTM A123 / ISO 1461, Sa 2.5 pre-blast | 150 kg | 1,575 kg (5% overage) | Vinh Thanh HDG | Hai Phong | 3-5 days | $0.90/kg | $1,417.50 | Buy | Local |
| | **M2 Subtotal** | | | | | | | | **$10,555.70** | | |

### 2.3 M3: Mast Assembly (x8 per unit)

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1301 | Steel tube, 60.3mm OD x 4mm wall x 3000mm, S235 | S235JR per EN 10219-2, seamless or ERW, yield >=235 MPa | 8 ea | 88 ea (10% overage) | Hoa Phat Tube Division | Hai Duong | 2 weeks | $14.50 | $1,276.00 | Buy | Local |
| VN-TGT-001-P-1302 | Mast base plate, 150x150x8mm, welded to tube | S235JR per EN 10025-2, 4x dia 14mm holes on 120mm BC | 8 ea | 88 ea | Truong Hai Mechanical | Hai Phong | 2 weeks | $3.50 | $308.00 | Buy | Local |
| VN-TGT-001-P-1303 | Mast top plate, 200x200x8mm, welded to tube | S235JR, 4x M10 tapped holes + 2x dia 8 H7 reamed on 160mm pattern | 8 ea | 88 ea | Truong Hai Mechanical | Hai Phong | 2 weeks | $2.80 | $246.40 | Buy | Local |
| VN-TGT-001-P-1304 | Mast base gussets, 6mm thick, 80x40mm triangle (4 per mast) | S235JR, 6mm fillet weld both sides | 32 ea | 336 ea (5% overage) | Truong Hai Mechanical | Hai Phong | Incl. in mast fab | $0.50 | $168.00 | Buy | Local |
| VN-TGT-001-P-1305 | M12 clevis pin, SS316, 12mm dia x 80mm (locking) | SS 316, spring ball-lock type with lanyard | 8 ea | 88 ea (10% overage) | Vietnam Marine Hardware | Hai Phong | 2 weeks | $4.50 | $396.00 | Buy | Local |
| VN-TGT-001-P-1306 | R-clip (spring pin) for clevis pin retention | SS 316 | 16 ea | 176 ea (10% overage) | Vietnam Marine Hardware | Hai Phong | 2 weeks | $0.80 | $140.80 | Buy | Local |
| VN-TGT-001-P-1307 | Safety wire, 0.8mm SS, for locking pin backup | SS 316 wire per MS20995-C32 | 5 m | 53 m (5% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $1.20/m | $63.60 | Buy | Local |
| VN-TGT-001-P-1308 | Hot-dip galvanizing service, 8 mast assemblies (~130 kg/unit) | Zinc coating >=85um per ASTM A123 | 130 kg | 1,365 kg (5% overage) | Vinh Thanh HDG | Hai Phong | 3-5 days | $0.90/kg | $1,228.50 | Buy | Local |
| VN-TGT-001-P-1309 | Tef-Gel anti-seize compound (socket bore, pins) | Marine anti-seize, titanium-based | 1 tube | 11 tubes (10% overage) | Tef-Gel Marine (import distributor) | Import | 2 weeks | $28.00 | $308.00 | Buy | Import |
| | **M3 Subtotal** | | | | | | | | **$4,135.30** | | |

### 2.4 M4: Reflector Assembly (x8 per unit)

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1401 | AM AlSi10Mg frame, LPBF printed, T5 heat treated, post-machined datums | AlSi10Mg per ASTM F3318; T5 (300C/2h + 160C/6h); orthogonality <=+/-0.05 deg per face pair; Type III hard anodize >=25um per MIL-A-8625F | 8 ea | 88 ea (10% overage) | Xometry Asia (primary); Facfox (backup 1); JR Tech Solutions (backup 2) | Singapore; Shenzhen; Bangkok | 3 weeks | $900.00 | $79,200.00 | Buy | ASEAN Import |
| VN-TGT-001-P-1402 | CNC face plate, 800x800x3mm, fly-cut Ra <=6.3um, flatness <0.1mm | 6061-T6 Al per ASTM B209; 4x dia 7mm + 2x dia 5 H7 reamed holes per plate; edge chamfer 0.5x45 deg | 24 ea | 264 ea (10% overage) | Hai Phong CNC (primary); Minh Phuc CNC (backup) | Hai Phong; Hanoi | 2 weeks | $38.00 | $10,032.00 | Buy | Local |
| VN-TGT-001-P-1403 | Type III hard anodize service, AM frames (8 pcs/unit) | >=25um per MIL-A-8625F Type III, Class 1, sealed | 8 ea | Incl. in P-1401 | Xometry Asia (bundled) | Singapore | Incl. in AM lead | $75.00 | (Incl. in P-1401) | Buy | ASEAN Import |
| VN-TGT-001-P-1404 | Type II anodize service, face plates (24 pcs/unit) | >=10um, <=25um per MIL-A-8625F Type II, Class 1 (clear/natural) | 24 ea | 264 ea | Saigon Anodizing (primary); An Phat Surface Treatment (backup) | HCMC; Binh Duong | 3-5 days | $12.50 | $3,300.00 | Buy | Local |
| VN-TGT-001-P-1405 | M6 x 20 SS316 socket head cap screw (face to frame) | SS 316 A4-80 per ISO 3506-1 | 96 ea | 1,008 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $0.35 | $352.80 | Buy | Local |
| VN-TGT-001-P-1406 | M6 SS316 flat washer | SS 316 per DIN 125 | 96 ea | 1,008 ea | Bulong Viet | Hanoi | 2 weeks | $0.10 | $100.80 | Buy | Local |
| VN-TGT-001-P-1407 | M6 SS316 Nylock nut | SS 316 A4-80 per DIN 985 | 96 ea | 1,008 ea | Bulong Viet | Hanoi | 2 weeks | $0.15 | $151.20 | Buy | Local |
| VN-TGT-001-P-1408 | Alignment dowel pin, dia 5mm m6 x 12mm, SS316 | SS 316, light press fit | 48 ea | 504 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $0.60 | $302.40 | Buy | Local |
| VN-TGT-001-P-1409 | Safety wire, 0.8mm SS, 2 loops per reflector | SS 316 wire per MS20995-C32 | 8 m | 84 m (5% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $1.20/m | $100.80 | Buy | Local |
| VN-TGT-001-P-1410 | Helicoil insert, M6 x 1.5D (AM frame bolt holes) | SS 304 per NASM33537 | 96 ea | 1,056 ea (10% overage) | Import (Heli-Coil / Recoil distributor) | Import (US/EU) | 3 weeks | $0.85 | $897.60 | Buy | Other Import |
| VN-TGT-001-P-1411 | 6061-T6 Al sheet stock, 1250x2500x3mm (raw material for face plates) | 6061-T6 per ASTM B209, mill cert required | 10 sheets/unit | 110 sheets (10% overage) | Novelis (Korea) via VN distributor | Import (Korea) | 4 weeks | $55.00/sheet | $6,050.00 | Buy | Other Import |
| | **M4 Subtotal** | | | | | | | | **$100,487.60** | | |

**Note on P-1401:** Unit cost of $900/frame includes LPBF printing, T5 heat treatment, CNC post-machining of datums, and Type III hard anodize. Frames ordered in batches of 40 (2 batches for 80 frames + 8 overage). Type III anodize cost (P-1403) is bundled into the per-frame price from the AM bureau.

**Note on P-1411:** Raw Al sheet is procured separately and issued to CNC shop (P-1402). The $38/plate CNC cost is machining labor only. Total face plate cost = sheet material ($55/10 plates = $5.50/plate) + CNC ($38/plate) + anodize ($12.50/plate) = $56.00/plate effective.

### 2.5 M5: Mast-Reflector Interface Hardware (IF-04, x8 per unit)

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1501 | M10 x 30 Grade 8.8 HDG hex bolt (mast top to reflector) | Grade 8.8 HDG per ISO 898-1 | 32 ea | 336 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $1.40 | $470.40 | Buy | Local |
| VN-TGT-001-P-1502 | Nordlock washer pair, M10, SS (anti-vibration) | SS 316 wedge-lock per DIN 25201 | 32 pr | 352 pr (10% overage) | Nordlock / Bossard Vietnam (distributor) | Import (Sweden via SG) | 3 weeks | $2.80 | $985.60 | Buy | Other Import |
| VN-TGT-001-P-1503 | M10 SS316 Nylock nut | SS 316 A4-80 | 32 ea | 336 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $0.55 | $184.80 | Buy | Local |
| VN-TGT-001-P-1504 | Helicoil insert, M10 x 1.5D (AM frame flange) | SS 304 per NASM33537 | 32 ea | 352 ea (10% overage) | Import (Heli-Coil / Recoil distributor) | Import (US/EU) | 3 weeks | $1.20 | $422.40 | Buy | Other Import |
| VN-TGT-001-P-1505 | Dowel pin, dia 8mm H7 x 20mm, SS316 | SS 316, m6 tolerance on diameter | 16 ea | 176 ea (10% overage) | Bulong Viet | Hanoi | 2 weeks | $1.80 | $316.80 | Buy | Local |
| VN-TGT-001-P-1506 | Nylon isolation bushing, M10 (11mm ID x 16mm OD x 8mm) | Nylon 6/6 per ASTM D4066 | 32 ea | 336 ea (5% overage) | Specialty plastics distributor | HCMC | 2 weeks | $0.45 | $151.20 | Buy | Local |
| VN-TGT-001-P-1507 | Nylon flat washer, 10mm ID x 20mm OD x 2mm (isolation) | Nylon 6/6 | 64 ea | 672 ea (5% overage) | Specialty plastics distributor | HCMC | 2 weeks | $0.20 | $134.40 | Buy | Local |
| VN-TGT-001-P-1508 | Nylon dowel pin sleeve, 8mm ID (galvanic isolation, Al side) | Nylon 6/6 | 16 ea | 176 ea (10% overage) | Specialty plastics distributor | HCMC | 2 weeks | $0.35 | $61.60 | Buy | Local |
| VN-TGT-001-P-1509 | Tef-Gel anti-seize, all IF-04 fasteners | Marine anti-seize, titanium-based | 1 tube | 11 tubes (10% overage) | Tef-Gel Marine (import distributor) | Import | 2 weeks | $28.00 | $308.00 | Buy | Import |
| VN-TGT-001-P-1510 | Safety wire, 0.8mm SS, 4 loops per unit (bolt pairs) | SS 316 wire per MS20995-C32 | 10 m | 105 m (5% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $1.20/m | $126.00 | Buy | Local |
| | **M5 Subtotal** | | | | | | | | **$3,161.20** | | |

### 2.6 M6: GPS Beacon Assembly

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1601 | GNSS module (u-blox ZED-F9P or equivalent), multi-constellation | COTS electronics, GPS+GLONASS+BeiDou, CEP <=5m | 1 ea | 12 ea (20% overage — ESD sensitive) | u-blox distributor (Mouser/Digikey Asia) | Import (Taiwan) | 4-6 weeks | $250.00 | $3,000.00 | Buy | Other Import |
| VN-TGT-001-P-1602 | Iridium SBD modem (RockBLOCK 9603N or equiv.) | COTS electronics, Iridium Short Burst Data | 1 ea | 12 ea (20% overage) | Rock Seven / Iridium distributor | Import (UK/US) | 4-6 weeks | $280.00 | $3,360.00 | Buy | Other Import |
| VN-TGT-001-P-1603 | GNSS active antenna, marine-grade, IP67 | COTS, wide-beam patch, 3.3V active | 1 ea | 12 ea (20% overage) | u-blox distributor | Import (Taiwan) | 4-6 weeks | $45.00 | $540.00 | Buy | Other Import |
| VN-TGT-001-P-1604 | Iridium patch antenna, marine-grade | COTS, 1616 MHz L-band patch | 1 ea | 12 ea (20% overage) | Iridium distributor | Import (US) | 4-6 weeks | $55.00 | $660.00 | Buy | Other Import |
| VN-TGT-001-P-1605 | Li-ion battery pack, 20 Wh (4x 18650, 3.7V 5400mAh) | Li-ion 18650 cells, UN38.3 certified | 1 pack | 12 packs (20% overage) | EVE Energy / Samsung SDI (distributor) | Import (China) | 3 weeks | $65.00 | $780.00 | Buy | Other Import |
| VN-TGT-001-P-1606 | Battery management PCB (charge/protect) | COTS PCB, 1S4P configuration, over-charge/discharge protection | 1 ea | 12 ea (20% overage) | Import (China electronics) | Import (China) | 3 weeks | $25.00 | $300.00 | Buy | Other Import |
| VN-TGT-001-P-1607 | IP67/68 waterproof enclosure, ABS/PC, 200x150x80mm | ABS/Polycarbonate blend per IEC 60529 IP68 | 1 ea | 12 ea (20% overage) | Bud Industries / Polycase (distributor) | Import (China/US) | 3 weeks | $55.00 | $660.00 | Buy | Other Import |
| VN-TGT-001-P-1608 | Waterproof cable glands, M16, IP68 | Nylon body, SS clamping ring | 3 ea | 33 ea (10% overage) | Local electrical supply | HCMC | 1 week | $8.00 | $264.00 | Buy | Local |
| VN-TGT-001-P-1609 | SS316 U-bolt clamp bracket (2x M8 U-bolts, saddle plate 80x40x5mm) | SS 316 per ASTM A240, passivated per ASTM A967 | 1 set | 11 sets (10% overage) | Local SS fabricator | Hai Phong | 2 weeks | $45.00 | $495.00 | Buy | Local |
| VN-TGT-001-P-1610 | L-bracket, 100x80x3mm SS316, for enclosure mounting | SS 316 | 1 ea | 11 ea (10% overage) | Local SS fabricator | Hai Phong | 2 weeks | $18.00 | $198.00 | Buy | Local |
| VN-TGT-001-P-1611 | M6 x 16 SS316 bolt (enclosure to bracket) | SS 316 A4-70 | 4 ea | 44 ea (10% overage) | Bulong Viet | Hanoi | 2 weeks | $0.35 | $15.40 | Buy | Local |
| VN-TGT-001-P-1612 | M8 SS316 Nylock nut (U-bolt) | SS 316 A4-70 | 4 ea | 44 ea (10% overage) | Bulong Viet | Hanoi | 2 weeks | $0.45 | $19.80 | Buy | Local |
| VN-TGT-001-P-1613 | Wiring harness + connectors (internal) | Marine-grade wire, JST/Molex connectors, UV-resistant jacket | 1 set | 11 sets (10% overage) | Local electronics assembler | HCMC | 2 weeks | $30.00 | $330.00 | Buy | Local |
| VN-TGT-001-P-1614 | Desiccant pack (enclosure moisture control) | Silica gel, indicating type | 2 ea | 22 ea (10% overage) | Local supply | HCMC | 1 week | $2.00 | $44.00 | Buy | Local |
| VN-TGT-001-P-1615 | Conformal coating for PCB (marine protection) | Urethane conformal coating per MIL-I-46058 Type UR | 1 can | 11 cans (10% overage) | HumiSeal / Dow (distributor) | Import | 2 weeks | $15.00 | $165.00 | Buy | Import |
| | **M6 Subtotal** | | | | | | | | **$10,831.20** | | |

### 2.7 M7: Mooring Kit (Medium Depth — 20-40m baseline)

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1701 | Danforth anchor, 50 kg, hot-dip galvanized | HDG cast steel per ASTM A123, holding >=1,500 kgf in medium sand | 1 ea | 11 ea (10% overage) | Vietnam Marine Equipment (primary); Tan Thanh Marine (backup) | Hai Phong; Da Nang | 3 weeks | $350.00 | $3,850.00 | Buy | Local |
| VN-TGT-001-P-1702 | G30 proof coil chain, 16mm HDG, bottom section | G30 per ASTM A413 / NACM, HDG >=85um, SWL >=4,200 kgf | 20 m | 210 m (5% overage) | Hai Phong Marine Chandler (primary); Vung Tau Marine Supply (backup) | Hai Phong | 1 week | $7.50/m | $1,575.00 | Buy | Local |
| VN-TGT-001-P-1703 | Polyester braided rode, 20mm, 3-strand, UV-stabilized | Marine polyester, SWL >=4,500 kgf at 24mm (per D9 upgrade) | 60 m | 630 m (5% overage) | Saigon Rope & Cordage (primary); Hai Phong Rope Factory (backup) | HCMC; Hai Phong | 2 weeks | $4.50/m | $2,835.00 | Buy | Local/ASEAN |
| VN-TGT-001-P-1704 | Swivel, rated 5,000 kgf, HDG (chain-to-rode) | HDG forged alloy steel, jaw-jaw type, free rotation under 1,500 kgf | 1 ea | 11 ea (10% overage) | Vietnam Marine Hardware (primary); Import via Hai Phong chandler | Hai Phong | 2 weeks | $85.00 | $935.00 | Buy | Import |
| VN-TGT-001-P-1705 | Bow shackle, 20mm pin, SWL 5,000 kgf, HDG (anchor to chain) | HDG forged alloy steel per Crosby G-2130 or equivalent | 1 ea | 11 ea (10% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $28.00 | $308.00 | Buy | Local |
| VN-TGT-001-P-1706 | Bow shackle, 20mm pin, SWL 5,000 kgf, HDG (chain to swivel) | HDG forged alloy steel | 1 ea | 11 ea | Vietnam Marine Hardware | Hai Phong | 1 week | $28.00 | $308.00 | Buy | Local |
| VN-TGT-001-P-1707 | Bow shackle, 20mm pin, SWL 5,000 kgf, HDG (rode to pad eye) | HDG forged alloy steel | 1 ea | 11 ea | Vietnam Marine Hardware | Hai Phong | 1 week | $28.00 | $308.00 | Buy | Local |
| VN-TGT-001-P-1708 | SS316 thimble, 20mm rope (rode eye termination) | SS 316, rated >=6,000 kgf | 2 ea | 22 ea (10% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $8.00 | $176.00 | Buy | Local |
| VN-TGT-001-P-1709 | Mousing wire, 1.0mm galv (for shackle pins) | Galvanized steel wire | 5 m | 53 m (5% overage) | Hai Phong Marine Chandler | Hai Phong | 1 week | $1.00/m | $53.00 | Buy | Local |
| VN-TGT-001-P-1710 | Trip line (polypropylene, 10mm, anchor recovery) | PP rope, buoyant | 50 m | 525 m (5% overage) | Saigon Rope & Cordage | HCMC | 1 week | $1.50/m | $787.50 | Buy | Local |
| VN-TGT-001-P-1711 | Surface buoy, 300mm dia, orange (trip line marker) | HDPE foam, high-visibility orange | 1 ea | 11 ea (10% overage) | Vietnam Marine Equipment | Hai Phong | 1 week | $25.00 | $275.00 | Buy | Local |
| | **M7 Subtotal** | | | | | | | | **$11,410.50** | | |

### 2.8 M8: Tow Kit

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1801 | Dyneema SK75 bridle rope, 16mm, 12-strand, 2 legs x 25m | UHMWPE (Dyneema) per ISO 2307, SWL >=8,000 kgf, UV cover braid | 50 m | 550 m (10% overage) | Marlow Ropes agent (primary); Samson Rope via SG distributor (backup) | Import (UK/NL) | 6 weeks | $8.50/m | $4,675.00 | Buy | Other Import |
| VN-TGT-001-P-1802 | Spliced soft eyes with SS316 thimble (bridle terminations) | SS 316 thimble rated >=6,000 kgf + professional splice (72x core tuck min) | 4 ea | 44 ea (10% overage) | Local marine rigger (Hai Phong) | Hai Phong | 1 week | $25.00 | $1,100.00 | Make | Local |
| VN-TGT-001-P-1803 | Trailing drogue, 600mm dia conical, canvas/nylon | UV-stabilized nylon 600D canvas, SS ring + swivel, 4-point bridle | 1 ea | 11 ea (10% overage) | Local canvas/sail maker (Hai Phong) | Hai Phong | 2 weeks | $120.00 | $1,320.00 | Buy | Local |
| VN-TGT-001-P-1804 | Bow shackle, 16mm pin, SWL 3,500 kgf, HDG (bridle to tow pad eye) | HDG forged alloy steel | 2 ea | 22 ea (10% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $22.00 | $484.00 | Buy | Local |
| VN-TGT-001-P-1805 | Bow shackle, 12mm pin, SWL 2,000 kgf, HDG (drogue attachment) | HDG forged alloy steel | 1 ea | 11 ea (10% overage) | Vietnam Marine Hardware | Hai Phong | 1 week | $15.00 | $165.00 | Buy | Local |
| VN-TGT-001-P-1806 | Mousing wire, 1.0mm galv (for shackle pins) | Galvanized steel wire | 3 m | 32 m (5% overage) | Hai Phong Marine Chandler | Hai Phong | 1 week | $1.00/m | $32.00 | Buy | Local |
| VN-TGT-001-P-1807 | Protective rope bag (storage + transport) | Heavy canvas, draw-string closure | 1 ea | 11 ea (10% overage) | Local canvas maker | Hai Phong | 1 week | $18.00 | $198.00 | Buy | Local |
| | **M8 Subtotal** | | | | | | | | **$7,974.00** | | |

### 2.9 Miscellaneous Hardware and Consumables

| Part # | Description | Material Specification | Qty/Unit | Qty @10 (incl. overage) | Approved Supplier(s) | Location | Lead Time | Unit Cost ($) | Extended @10 ($) | Make/Buy | Source |
|--------|-------------|----------------------|----------|------------------------|---------------------|----------|-----------|---------------|------------------|----------|--------|
| VN-TGT-001-P-1901 | M12 SS316 hex bolt spare kit (IF-01, IF-06 spares) | SS 316 A4-70 | 10 ea | 105 ea (5% overage) | Bulong Viet | Hanoi | 2 weeks | $1.20 | $126.00 | Buy | Local |
| VN-TGT-001-P-1902 | Spare M12 clevis pin + R-clip (mast spares) | SS 316 | 2 sets | 22 sets (10% overage) | Vietnam Marine Hardware | Hai Phong | 2 weeks | $5.30 | $116.60 | Buy | Local |
| VN-TGT-001-P-1903 | Spare M6 bolt/nut/washer sets (reflector spares) | SS 316 A4-80 | 12 sets | 126 sets (5% overage) | Bulong Viet | Hanoi | 2 weeks | $0.60 | $75.60 | Buy | Local |
| VN-TGT-001-P-1904 | Lifting slings, 2T WLL, polyester, 2m (handling) | Polyester webbing, color-coded per EN 1492-1 | 4 ea | 42 ea (5% overage) | Local rigging supply | Hai Phong | 1 week | $12.00 | $504.00 | Buy | Local |
| VN-TGT-001-P-1905 | Ratchet straps, 2T WLL, 5m (transport securing) | Polyester + steel ratchet per EN 12195-2 | 8 ea | 84 ea (5% overage) | Local rigging supply | Hai Phong | 1 week | $8.00 | $672.00 | Buy | Local |
| VN-TGT-001-P-1906 | Reflective tape, SOLAS grade (night visibility) | Retro-reflective per IMO SOLAS III/4 | 5 m | 53 m (5% overage) | 3M Marine (distributor) | Import | 2 weeks | $6.00/m | $318.00 | Buy | Import |
| VN-TGT-001-P-1907 | Identification plates, engraved SS (serial #, data plate) | SS 316, laser-engraved | 2 ea | 22 ea (10% overage) | Local engraver | Hai Phong | 1 week | $15.00 | $330.00 | Buy | Local |
| VN-TGT-001-P-1908 | Waterproof documentation pouch (deployment manual) | PVC/clear, zip-lock closure | 1 ea | 11 ea (10% overage) | Local supply | HCMC | 1 week | $8.00 | $88.00 | Buy | Local |
| | **Misc. Subtotal** | | | | | | | | **$2,230.20** | | |

---

## 3. BOM Summary by Module

| Module | Description | C14 Per-Unit ($) | Lot Qty (with overage) | Lot Extended ($) | % of Lot BOM |
|--------|-------------|------------------|------------------------|------------------|-------------|
| **M1** | Hull Assembly | $4,118.00 | 11 sets | $44,789.00 | 23.1% |
| **M2** | Structural Frame Assembly | $987.20 | 11 sets | $10,555.70 | 5.4% |
| **M3** | Mast Assembly (x8) | $366.20 | 88 masts | $4,135.30 | 2.1% |
| **M4** | Reflector Assembly (x8) | $9,189.60 | 88 reflectors | $100,487.60 | 51.7% |
| **M5** | Mast-Reflector Interface HW | $292.00 | 10 sets | $3,161.20 | 1.6% |
| **M6** | GPS Beacon Assembly | $914.20 | 12 beacons | $10,831.20 | 5.6% |
| **M7** | Mooring Kit | $1,060.00 | 11 kits | $11,410.50 | 5.9% |
| **M8** | Tow Kit | $725.00 | 11 kits | $7,974.00 | 4.1% |
| **Misc** | Spares, consumables, handling | $209.80 | 10 sets + spares | $2,230.20 | 1.2% |
| | | | | | |
| | **PROCUREMENT BOM TOTAL** | **$17,862.00** | | **$195,574.70** | **100%** |

**Per-unit procurement cost (including overage):** $195,574.70 / 10 = **$19,557/unit**

**Overage cost:** $195,574.70 - ($17,862 x 10) = $16,954.70 (8.7% overage on $178,620 baseline)

---

## 4. Long-Lead Item Schedule

Items with lead time >3 weeks, ordered by required delivery date. Assembly start is **Week 7**. All PO dates calculated working backwards from assembly start with 1-week receiving/inspection buffer.

| Priority | Part # | Description | Lead Time | Required at Assembly | Latest PO Date | Recommended PO Date | Qty (Lot) | Extended Cost ($) | Supplier |
|----------|--------|-------------|-----------|---------------------|----------------|--------------------|-----------|--------------------|----------|
| 1 | VN-TGT-001-P-1801 | Dyneema SK75 bridle rope, 16mm | 6 weeks | Week 7 | **Week -2** | **Week -2** | 550 m | $4,675.00 | Marlow Ropes (UK/NL) |
| 2 | VN-TGT-001-P-1601 | GNSS module (u-blox ZED-F9P) | 4-6 weeks | Week 7 | **Week -1** | **Week -2** | 12 ea | $3,000.00 | u-blox distributor (Taiwan) |
| 3 | VN-TGT-001-P-1602 | Iridium SBD modem (RockBLOCK 9603N) | 4-6 weeks | Week 7 | **Week -1** | **Week -2** | 12 ea | $3,360.00 | Rock Seven (UK/US) |
| 4 | VN-TGT-001-P-1603 | GNSS active antenna, marine IP67 | 4-6 weeks | Week 7 | **Week -1** | **Week -2** | 12 ea | $540.00 | u-blox distributor |
| 5 | VN-TGT-001-P-1604 | Iridium patch antenna, marine | 4-6 weeks | Week 7 | **Week -1** | **Week -2** | 12 ea | $660.00 | Iridium distributor |
| 6 | VN-TGT-001-P-1411 | 6061-T6 Al sheet, 1250x2500x3mm | 4 weeks | Week 4 (CNC start) | **Week 0** | **Week 0** | 110 sheets | $6,050.00 | Novelis (Korea) via VN distributor |
| 7 | VN-TGT-001-P-1401 | AM AlSi10Mg frames, LPBF (Batch 1: 44 frames) | 3 weeks | Week 4 | **Week 0** | **Week 0** | 44 ea | $39,600.00 | Xometry Asia (Singapore) |
| 8 | VN-TGT-001-P-1401 | AM AlSi10Mg frames, LPBF (Batch 2: 44 frames) | 3 weeks | Week 5 | **Week 1** | **Week 1** | 44 ea | $39,600.00 | Facfox (Shenzhen) |
| 9 | VN-TGT-001-P-1410 | Helicoil insert, M6 x 1.5D | 3 weeks | Week 5 | **Week 1** | **Week 1** | 1,056 ea | $897.60 | Heli-Coil distributor (US/EU) |
| 10 | VN-TGT-001-P-1504 | Helicoil insert, M10 x 1.5D | 3 weeks | Week 5 | **Week 1** | **Week 1** | 352 ea | $422.40 | Heli-Coil distributor (US/EU) |
| 11 | VN-TGT-001-P-1502 | Nordlock washer pair, M10, SS | 3 weeks | Week 6 | **Week 2** | **Week 1** | 352 pr | $985.60 | Nordlock / Bossard Vietnam |
| 12 | VN-TGT-001-P-1101 | HDPE pontoon shell (2-section) | 3 weeks | Week 4 (rolling) | **Week 1** | **Week 0** | 11 sets | $30,800.00 | Binh Minh Plastics (HCMC) |

**Total long-lead procurement value:** $130,590.60 (66.8% of total procurement BOM)

**Critical path:** Dyneema and GPS modules must be ordered at Week -2 (2 weeks before general procurement). AM frame batches and Al sheet at Week 0. All other items have <=2 week lead times and can be ordered at Week 0-1.

---

## 5. Supplier Summary

| # | Supplier | Location | Components Supplied | Part Numbers | Total Value ($) | % of Lot | Payment Terms | Qualification Status |
|---|----------|----------|---------------------|-------------|-----------------|----------|---------------|---------------------|
| 1 | **Xometry Asia** | Singapore | AM AlSi10Mg frames (Batch 1, incl. Type III anodize) | P-1401 (partial) | $39,600.00 | 20.2% | 30% advance, 70% on delivery + FAI pass | **TO QUALIFY** — first article required (OCP-P15-001) |
| 2 | **Facfox** | Shenzhen, China | AM AlSi10Mg frames (Batch 2, incl. Type III anodize) | P-1401 (partial) | $39,600.00 | 20.2% | 30% advance, 70% on delivery + FAI pass | **TO QUALIFY** — first article required (OCP-P15-001) |
| 3 | **Binh Minh Plastics (BMP)** | HCMC | HDPE hull shells, joint flanges, scupper fittings | P-1101, P-1103, P-1106 | $33,944.00 | 17.4% | 30% advance, 70% on delivery | Established (ISO 9001) |
| 4 | **Hai Phong CNC** | Hai Phong | CNC face plate machining (24/unit) | P-1402 | $10,032.00 | 5.1% | 30% advance, 70% on delivery | **TO QUALIFY** — Ra <=6.3um capability (OCP-P15-002) |
| 5 | **Novelis (Korea) via distributor** | Import (Korea) | 6061-T6 Al sheet stock | P-1411 | $6,050.00 | 3.1% | 100% on order (import prepay) | Established (ASTM B209 mill cert) |
| 6 | **Bulong Viet** | Hanoi | SS316 + HDG fasteners (all sizes) | P-1210 to P-1217, P-1405-1408, P-1501, P-1503, P-1505, P-1611-1612, P-1901, P-1903 | $5,025.30 | 2.6% | 30% advance, 70% on delivery | Established |
| 7 | **Marlow Ropes (via agent)** | Import (UK/NL) | Dyneema SK75 16mm bridle rope | P-1801 | $4,675.00 | 2.4% | 100% on order (import prepay) | Established (ISO 2307 cert) |
| 8 | **Hoa Phat Group** | Hai Duong / Dung Quat | S235 steel plate, angle, channel, tube | P-1201, P-1202, P-1206, P-1301 | $2,914.00 | 1.5% | 30% advance, 70% on delivery | Established (EN 10025-2 mill cert) |
| 9 | **Vietnam Marine Equipment** | Hai Phong | Danforth anchors, zinc anodes, surface buoys | P-1701, P-1218, P-1711 | $4,257.00 | 2.2% | 30% advance, 70% on delivery | Established |
| 10 | **Vietnam Marine Hardware** | Hai Phong | Shackles, thimbles, clevis pins, R-clips, safety wire, swivels | P-1305-1307, P-1409, P-1510, P-1704-P-1708, P-1804-P-1806, P-1902 | $3,955.40 | 2.0% | 30% advance, 70% on delivery | Established |
| 11 | **Truong Hai Mechanical** | Hai Phong | Steel frame fabrication, mast fabrication (M2+M3 welded assemblies) | P-1203, P-1204, P-1205, P-1302-P-1304 | $4,583.40 | 2.3% | 30% advance, 40% at mid-fab inspection, 30% on delivery | **TO QUALIFY** — AWS D1.1, UT capability |
| 12 | **Vinh Thanh HDG** | Hai Phong | Hot-dip galvanizing (frame, masts) | P-1219, P-1308 | $2,646.00 | 1.4% | 30% advance, 70% on delivery | Established (ASTM A123) |
| 13 | **Saigon Anodizing** | HCMC | Type II anodize (face plates) | P-1404 | $3,300.00 | 1.7% | 30% advance, 70% on delivery | Established (MIL-A-8625F) |
| 14 | **Dong A Chemical** | Binh Duong | PU rigid foam, 2-component | P-1102 | $8,400.00 | 4.3% | 30% advance, 70% on delivery | Established |
| 15 | **u-blox / Iridium distributors** | Import (Taiwan/UK/US) | GNSS module, Iridium modem, antennas | P-1601 to P-1604 | $7,560.00 | 3.9% | 100% on order (import prepay) | Established (COTS) |
| 16 | **Electronics import (China)** | Import (China) | Battery packs, BMS PCB, enclosures | P-1605, P-1606, P-1607 | $1,740.00 | 0.9% | 100% on order (import prepay) | Established (UN38.3 cert for batteries) |
| 17 | **Saigon Rope & Cordage** | HCMC | Polyester rode, PP trip line | P-1703, P-1710 | $3,622.50 | 1.9% | 30% advance, 70% on delivery | Established |
| 18 | **Heli-Coil / Nordlock distributors** | Import (US/EU/Sweden) | Helicoil inserts (M6, M10), Nordlock washers | P-1410, P-1504, P-1502 | $2,305.60 | 1.2% | 100% on order (import prepay) | Established |
| | **Various local minor** | HCMC / Hai Phong | Sealant, paint, cable glands, desiccant, nylon isolation hardware, slings, straps, misc | Multiple | ~$10,964.10 | 5.6% | Various | Established |
| | | | | | | | | |
| | **TOTAL** | | | | **$195,574.70** | **100%** | | |

---

## 6. Import Item Consolidation

### 6.1 Import Summary by Country of Origin

| Country / Region | Items | Part Numbers | Total Value ($) | % of Imports | Suggested Shipping Route | Transit Time |
|-----------------|-------|-------------|-----------------|-------------|-------------------------|-------------|
| **Singapore** | AM frames Batch 1 (44 ea) | P-1401 (partial) | $39,600.00 | 53.8% | Singapore -> HCMC via sea freight | 5 days |
| **China (Shenzhen)** | AM frames Batch 2 (44 ea) | P-1401 (partial) | $39,600.00 | Incl. in ASEAN | Shenzhen -> Hai Phong via sea freight | 3 days |
| **China (other)** | Battery packs, BMS PCB, enclosures | P-1605, P-1606, P-1607 | $1,740.00 | 2.4% | Shenzhen -> HCMC via sea freight (consolidate with AM Batch 2) | 3 days |
| **Korea** | 6061-T6 Al sheet stock (110 sheets) | P-1411 | $6,050.00 | 8.2% | Busan -> Hai Phong via sea freight | 5-7 days |
| **Taiwan** | GNSS modules, GNSS antennas | P-1601, P-1603 | $3,540.00 | 4.8% | Taipei -> HCMC via air freight (high value, low weight) | 2 days |
| **UK / Netherlands** | Dyneema SK75 rope (550 m) | P-1801 | $4,675.00 | 6.3% | Rotterdam -> HCMC via sea freight | 25-30 days |
| **UK / US** | Iridium modem, Iridium antenna | P-1602, P-1604 | $4,020.00 | 5.5% | US -> HCMC via air freight (high value, low weight) | 3 days |
| **US / EU** | Helicoil inserts (M6, M10) | P-1410, P-1504 | $1,320.00 | 1.8% | US -> HCMC via air freight (consolidate with Iridium) | 3 days |
| **Sweden (via SG)** | Nordlock washers | P-1502 | $985.60 | 1.3% | Sweden -> Singapore -> HCMC (consolidate with AM Batch 1) | 5 days (SG leg) |
| **Various** | Sealant (Sika), paint, Tef-Gel, conformal coat, SOLAS tape | P-1105, P-1107, P-1309, P-1509, P-1615, P-1906 | $2,955.00 | 4.0% | Distributed via local Vietnamese distributors (stock items) | N/A (local stock) |
| | | | | | | |
| | **TOTAL IMPORTS** | | **$104,485.60** | **100%** | | |

### 6.2 Consolidated Shipment Plan

| Shipment # | Origin | Destination | Contents | Value ($) | Weight (est.) | Mode | Order Week | Ship Week | Arrive Week |
|------------|--------|-------------|----------|-----------|---------------|------|------------|-----------|-------------|
| **SHIP-01** | Rotterdam, NL | HCMC | Dyneema SK75 rope (550 m, ~75 kg) | $4,675 | 100 kg | Sea freight (FCL share) | Wk -2 | Wk -1 | Wk 3 |
| **SHIP-02** | Taipei + US | HCMC | GNSS modules (12), Iridium modems (12), antennas (24), Helicoils (1,408 pcs), conformal coat | $12,480 | 15 kg | Air freight (consolidated) | Wk -2 | Wk -1 | Wk 0 |
| **SHIP-03** | Busan, Korea | Hai Phong | 6061-T6 Al sheet (110 sheets, ~600 kg) | $6,050 | 650 kg | Sea freight (LCL) | Wk 0 | Wk 1 | Wk 3 |
| **SHIP-04** | Singapore | HCMC / Hai Phong | AM frames Batch 1 (44 ea, ~375 kg) + Nordlock washers | $40,586 | 400 kg | Sea freight (LCL) | Wk 0 | Wk 2 | Wk 3 |
| **SHIP-05** | Shenzhen | Hai Phong | AM frames Batch 2 (44 ea, ~375 kg) + battery packs + BMS + enclosures | $41,340 | 420 kg | Sea freight (LCL) | Wk 1 | Wk 2 | Wk 3 |
| | | | **TOTAL** | **$105,131** | **~1,585 kg** | | | | |

**Estimated total import freight cost:** $3,500-5,000 (sea freight dominant; air freight for electronics only)
**Import duties (Vietnam MFN rate, est. 5-10% on electronics, 0-3% on industrial materials):** $3,000-6,000

---

## 7. Procurement Risk Register

| Risk ID | Risk Description | Probability | Impact | Cost Impact ($) | Affected Items | Mitigation Strategy |
|---------|-----------------|-------------|--------|----------------|----------------|---------------------|
| **PR-01** | **AM frame single-source delivery failure** — One AM bureau (Xometry or Facfox) fails quality on entire batch, requiring re-order from backup (JR Tech, Bangkok). | Medium (25%) | High | +$5,000-10,000 (expedite premium + 3-week delay) | P-1401 (44 frames per batch) | Split order across 2 bureaus (already planned). Third bureau (JR Tech, Bangkok) pre-qualified as hot standby. Maintain 8-frame (1-unit) buffer from first delivery. |
| **PR-02** | **AM frame orthogonality rejection rate >10%** — More than 9 of 88 frames fail +/-0.05 deg orthogonality at incoming inspection. | Medium (20%) | Medium | +$900/rejected frame (replacement) | P-1401 | 10% overage already included in lot quantity (88 vs 80 needed). Require AM bureau to provide CMM data per frame before shipment. Tighten AM bureau SOP with pre-ship inspection gate. |
| **PR-03** | **Dyneema import delay >8 weeks** — Shipping disruption (port congestion, customs hold) delays Dyneema rope delivery past Week 4. | Low (15%) | Medium | +$1,500 (air freight premium) or schedule slip 2 weeks | P-1801 | Order at Week -2 (4-week buffer to assembly start). If delayed, substitute 28mm polyester braided rope (locally available, SWL 8,500 kgf) per tow system fallback in P15. |
| **PR-04** | **GPS/Iridium module supply disruption** — Component shortage or export restriction delays GNSS or Iridium modules >8 weeks. | Low (10%) | High | +$2,000-5,000 (alternative module sourcing) or schedule slip | P-1601, P-1602 | 20% overage ordered (12 units for 10 needed). Qualify backup: Queclink GT300 integrated GPS/Iridium tracker ($350/unit, COTS alternative). Maintain 2-unit buffer stock. |
| **PR-05** | **6061-T6 Al sheet price increase >20%** — Global aluminum price spike due to LME volatility. | Medium (25%) | Low | +$1,210 for lot (20% on $6,050) | P-1411 | Lock in price at PO issuance (Week 0). Consider pre-purchasing 6-month Al sheet stock at current pricing. Impact is only 0.6% of lot BOM. |
| **PR-06** | **CNC face plate quality rejection rate >15%** — More than 40 of 264 plates fail flatness (<0.1 mm) or Ra (<=6.3 um) at incoming inspection. | Medium (20%) | Medium | +$1,520 (40 replacement plates at $38/plate) | P-1402 | 10% overage already included. Qualify CNC shop with 5-plate trial run before production order. Require CNC shop to provide Ra/flatness data per plate. Backup: Minh Phuc CNC (Hanoi). |
| **PR-07** | **VND/USD exchange rate adverse movement >10%** — VND appreciates against USD, increasing all local procurement costs when reported in USD. | Low (10%) | Medium | +$8,000-10,000 on local content portion | All local items | Low probability (VND historically stable/depreciating). Natural hedge: imported items become cheaper if VND appreciates. Net impact moderated. |
| **PR-08** | **HDPE hull fabrication capacity constraint** — Binh Minh Plastics unable to deliver 11 hulls in 10 weeks (1.1/week sustained rate). | Medium (20%) | Medium | +$3,000-5,000 (premium for parallel fabricator) | P-1101 | Qualify backup: Tien Phong Plastics (Hai Phong) or Tan Dai Hung (HCMC). Split order: 6 hulls to BMP, 5 to backup. Welding approach has more shop capacity than rotomolding. |

---

## 8. Budget Summary

### 8.1 Lot Cost Comparison

| Cost Element | C14 Baseline (10 units) | Procurement BOM (10 units) | Variance | Notes |
|-------------|------------------------|---------------------------|----------|-------|
| **Materials (BOM)** | $178,620 | $195,575 | +$16,955 (+9.5%) | Overage for QC rejects (5-10% per line) |
| **Manufacturing labor** | $27,260 | $27,260 | $0 | Per C14 Section 2; not in procurement BOM |
| **DIRECT COST** | **$205,880** | **$222,835** | **+$16,955** | |
| Tooling amortization | $25,000 | $25,000 | $0 | Rotomold, jigs, fixtures per C14 Section 4 |
| QC overhead | $8,500 | $8,500 | $0 | FAI, RCS test, material certs |
| PM / Engineering | $5,500 | $5,500 | $0 | Production engineering, documentation |
| Facility overhead (12%) | $24,710 | $26,740 | +$2,030 | 12% of higher direct cost |
| **OVERHEAD TOTAL** | **$63,710** | **$65,740** | **+$2,030** | |
| **SUBTOTAL** | **$269,590** | **$288,575** | **+$18,985** | |
| Margin (10%) | $26,959 | $28,858 | +$1,899 | |
| **LOT TOTAL (10 units)** | **$296,549** | **$317,433** | **+$20,884** | |
| | | | | |
| **Per-unit cost** | **$29,655** | **$31,743** | **+$2,088 (+7.0%)** | |

### 8.2 Variance Analysis

| Variance Source | Amount ($) | Explanation |
|----------------|-----------|-------------|
| AM frame overage (8 extra frames @ $900) | +$7,200 | 10% overage on 80 frames; highest-value item drives most of the variance |
| CNC face plate overage (24 extra @ $38) | +$912 | 10% overage on 240 plates |
| HDPE hull overage (1 extra hull @ $2,800) | +$2,800 | 10% overage — 1 spare hull shell |
| GPS electronics overage (2 extra @ $914) | +$1,828 | 20% overage on ESD-sensitive electronics |
| All other overage (fasteners, hardware, misc) | +$4,215 | 5-10% overage across remaining 60+ line items |
| **Total material overage** | **+$16,955** | 9.5% of C14 baseline BOM |
| Facility overhead increase (12% x $16,955) | +$2,030 | Overhead scales with direct cost |
| Margin increase (10% x $18,985) | +$1,899 | Margin scales with subtotal |
| **TOTAL VARIANCE** | **+$20,884** | 7.0% above C14 baseline lot cost |

### 8.3 Budget Recommendation

| Metric | Value |
|--------|-------|
| **C14 engineering estimate (per unit @10)** | $29,655 |
| **Procurement BOM estimate (per unit @10, with overage)** | $31,743 |
| **Phase 1 cost ceiling (CST-001)** | $36,000 |
| **Margin to ceiling** | $4,257 (11.8%) |
| **Recommendation** | Approve procurement at $31,743/unit. Margin to CST-001 ceiling provides contingency for first-unit learning, AM pricing uncertainty, and exchange rate fluctuation. Unused overage material (spare frames, plates, hulls) carries forward to Lot 2 as free-issue stock. |

### 8.4 Budget by Source Category

| Source | Lot Value ($) | % of Lot | Per Unit ($) |
|--------|-------------|----------|-------------|
| Vietnamese local procurement | $96,889.10 | 49.5% | $9,689 |
| ASEAN import (AM frames + anodize) | $79,200.00 | 40.5% | $7,920 |
| Other import (Al sheet, GPS, Dyneema, Helicoils, Nordlock, misc) | $19,485.60 | 10.0% | $1,949 |
| **TOTAL** | **$195,574.70** | **100%** | **$19,557** |

---

## 9. Procurement Execution Checklist

### 9.1 Pre-Procurement Actions (Before Week -2)

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| PRE-01 | Obtain budget approval for Lot 1 ($317,433 total) | Project Manager | Week -4 | PENDING |
| PRE-02 | Qualify Xometry Asia — submit 1-frame first article order, inspect on delivery | Procurement | Week -6 | PENDING (OCP-P15-001) |
| PRE-03 | Qualify Facfox — submit 1-frame first article order | Procurement | Week -6 | PENDING (OCP-P15-001) |
| PRE-04 | Qualify Hai Phong CNC — submit 5-plate trial order, verify Ra <=6.3um | Procurement | Week -4 | PENDING (OCP-P15-002) |
| PRE-05 | Qualify Truong Hai Mechanical — review AWS D1.1 certs, visit facility | Procurement | Week -4 | PENDING |
| PRE-06 | Confirm Dyneema distributor stock and lead time | Procurement | Week -3 | PENDING |
| PRE-07 | Confirm GPS/Iridium module availability and pricing | Procurement | Week -3 | PENDING |
| PRE-08 | Open Iridium SBD service account for GPS beacon testing | Engineering | Week -3 | PENDING |

### 9.2 PO Issuance Schedule

| Week | Purchase Orders to Issue | Total PO Value ($) |
|------|------------------------|---------------------|
| **Week -2** | P-1801 (Dyneema), P-1601-P-1604 (GPS/Iridium electronics) | $12,235 |
| **Week 0** | P-1401 Batch 1 (AM frames), P-1411 (Al sheet), P-1101 (HDPE hulls), all steel (P-1201-P-1206, P-1301), all fasteners (P-12xx, P-14xx, P-15xx), marine hardware (P-17xx), all local consumables | $145,340 |
| **Week 1** | P-1401 Batch 2 (AM frames), P-1410/P-1504 (Helicoils), P-1502 (Nordlock), P-1102 (PU foam), nylon isolation hardware | $42,000 |
| **Ongoing** | Galvanizing services (P-1219, P-1308), anodizing (P-1404), CNC machining (P-1402) — issued as materials arrive to sub-suppliers | — |

---

## 10. Cross-References

### Source Documents (Phase 3)
- [[../03_embodiment/OCP_C14_cost_analysis.md]] — Full BOM with unit costs, labor breakdown, volume pricing, overhead, cost risk analysis
- [[../03_embodiment/OCP_P15_production_planning.md]] — Supplier identification, lead times, make/buy decisions, production schedule, capacity analysis
- [[../03_embodiment/DECS_D9_detail_specification.md]] — Material specifications, tolerances, surface finishes, inspection criteria for all components

### Related Phase 4 Documents
- 04_detail/prototype_build_plan.md — Prototype fabrication plan (to be created)
- 04_detail/production_drawings/ — CAD drawing package (to be created)
- 04_detail/quality_plan.md — Incoming inspection and QC procedures (to be created)

### Requirements Traced
| Requirement | Description | How Addressed |
|-------------|-------------|---------------|
| CST-001 | Unit cost <=$36,000 @10 units | Procurement BOM $31,743/unit — PASS (11.8% margin) |
| PRD-001 | Production rate >=6 units/month | 18 suppliers identified; AM frames split across 2 bureaus with 3rd standby |
| PRD-002 | Local content >=60% | 62.5% local by material value (per C14 Section 6) — PASS |
| PRD-003 | >=2 qualified AM bureaus | 3 identified: Xometry (SG), Facfox (CN), JR Tech (TH) |
| PRD-005 | HDPE hull from VN supplier | Binh Minh Plastics (primary) + Tien Phong Plastics (backup) |
| PRD-007 | AM lead time <=3 weeks | Xometry: 2-3 wk; Facfox: 2-3 wk; JR Tech: 3-4 wk — PASS |

---

## 11. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Engineer | | | |
| Procurement Manager | | | |
| Quality Assurance | | | |
| Project Manager | | | |

---

*End of Procurement BOM — VN-TGT-SEA-001, Phase 4. This document defines all 73 procurement line items for a 10-unit first production lot of the THANH TRI-H fixed sea target. Total procurement value $195,575 (materials with overage). Combined with labor, overhead, and margin, the per-unit cost of $31,743 is within the Phase 1 ceiling of $36,000 (CST-001) with 11.8% contingency margin. Long-lead items (Dyneema, GPS modules) must be ordered at Week -2; AM frames and Al sheet at Week 0. All 18 suppliers identified with backup sources for critical items.*
