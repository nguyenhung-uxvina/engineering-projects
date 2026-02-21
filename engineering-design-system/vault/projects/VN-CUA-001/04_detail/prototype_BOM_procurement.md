---
project: VN-CUA-001
designation: VDC-33
type: prototype_bom_procurement
phase: 4
version: 2.0
created: 2026-02-05
updated: 2026-02-08
status: active
total_budget: "$800-1,000"
subsystems: 8
total_line_items: 55
---

# PHASE 4 — BOM & PROCUREMENT
## VDC-33 Bill of Materials & Procurement Plan

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Budget:** $800-1,000 USD
**Timeline:** 4 weeks to full assembly
**Design Input:** [[04_detail/prototype_design|Prototype Design Specifications]]

---

# 1. BILL OF MATERIALS

## 1.1 Pneumatic System ($282)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **PNE-001** | HPA Tank | 48ci (0.8L) / 3000psi (207 bar), aluminum | 1 | pc | Paintball shop | $50 |
| **PNE-002** | Tank Regulator | Adjustable 50-120 bar output, Ninja SLP | 1 | pc | Import (ANS Gear) | $85 |
| **PNE-003** | Macro Line | Stainless braided, 6mm OD, 1m length | 1 | m | Local pneumatic | $15 |
| **PNE-004** | Quick Disconnect | Foster style, 1/8" NPT, male+female pair | 2 | set | Local pneumatic | $10 |
| **PNE-005** | Pressure Gauge | 0-160 bar, 40mm dial, 1/8" NPT | 1 | pc | Local pneumatic | $12 |
| **PNE-006** | Solenoid Valve | 12V NC, 3-way, 8mm orifice, <10ms response | 1 | pc | Import (PE/Dye) | $65 |
| **PNE-007** | Fitting Tee | 1/8" NPT brass tee | 2 | pc | Local pneumatic | $5 |
| **PNE-008** | Fitting Elbow | 1/8" NPT brass 90 deg elbow | 2 | pc | Local pneumatic | $4 |
| **PNE-009** | Fitting Adapter | 1/8" NPT to 6mm push-fit | 4 | pc | Local pneumatic | $8 |
| **PNE-010** | O-ring Kit | NBR 70A, metric assortment | 1 | kit | Local hardware | $8 |
| **PNE-011** | PTFE Tape | Thread sealant, 12mm x 10m | 2 | roll | Local hardware | $2 |
| **PNE-012** | Relief Valve | 120 bar preset, 1/8" NPT | 1 | pc | Local pneumatic | $18 |
| | | | | | **Subtotal** | **$282** |

## 1.2 Barrel Assembly ($54)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **BAR-001** | Barrel Tube (PVC) | PVC Schedule 40, 32mm ID x 300mm | 1 | pc | Local hardware | $5 |
| **BAR-002** | Barrel Tube (Al) | Al 6061, 32mm ID x 35mm OD x 300mm (optional) | 1 | pc | Local machining | $35 |
| **BAR-003** | Breech Adapter | 3D printed PETG (P03) | 1 | pc | 3D print | $5 |
| **BAR-004** | Muzzle Cap | 3D printed PETG (P04) | 1 | pc | 3D print | $3 |
| **BAR-005** | Barrel Clamp | 3D printed PETG (P05), x2 | 2 | pc | 3D print | $4 |
| **BAR-006** | O-ring Breech | NBR 40mm ID x 3mm CS | 2 | pc | Local hardware | $2 |
| | | | | | **Subtotal** | **$54** |

## 1.3 Receiver Assembly - 3D Printed ($34)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **RCV-001** | Receiver Body | 3D printed PETG (P01), ~200g | 1 | pc | 3D print | $12 |
| **RCV-002** | Valve Mount | 3D printed PETG (P02), ~50g | 1 | pc | 3D print | $4 |
| **RCV-003** | Rail Mount | 3D printed PETG (P06), ~30g | 1 | pc | 3D print | $3 |
| **RCV-004** | Trigger Guard | 3D printed PETG (P07), ~20g | 1 | pc | 3D print | $2 |
| **RCV-005** | Grip | 3D printed PETG (P08), ~60g | 1 | pc | 3D print | $5 |
| **RCV-006** | Insert Nuts M4 | Brass heat-set inserts | 20 | pc | Import (AliExpress) | $5 |
| **RCV-007** | Insert Nuts M3 | Brass heat-set inserts | 10 | pc | Import (AliExpress) | $3 |
| | | | | | **Subtotal** | **$34** |

## 1.4 Stock Assembly ($32)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **STK-001** | Stock Body | 3D printed PETG (P09), ~150g | 1 | pc | 3D print | $10 |
| **STK-002** | Tank Clamp | 3D printed PETG (P10), ~80g | 1 | pc | 3D print | $6 |
| **STK-003** | Recoil Pad | Rubber, 80mm x 40mm x 15mm | 1 | pc | Local hardware | $5 |
| **STK-004** | Adjustment Rail | Aluminum extrusion 20x20, 150mm | 1 | pc | Local hardware | $8 |
| **STK-005** | Adjustment Knob | M6 knurled knob | 1 | pc | Local hardware | $3 |
| | | | | | **Subtotal** | **$32** |

## 1.5 Electronics & Safety ($62)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **ELE-001** | Arduino Nano | ATmega328P, USB-C | 1 | pc | Local electronics | $8 |
| **ELE-002** | Relay Module | 5V 1-channel, optocoupler isolated | 1 | pc | Local electronics | $3 |
| **ELE-003** | MOSFET Module | IRF520, 12V/5A | 1 | pc | Local electronics | $3 |
| **ELE-004** | Toggle Switch | SPST, panel mount, ARM switch | 1 | pc | Local electronics | $2 |
| **ELE-005** | Safety Switch | SPST, slide type, mechanical safety | 1 | pc | Local electronics | $2 |
| **ELE-006** | Trigger Switch | Microswitch, 5A, lever actuator | 1 | pc | Local electronics | $2 |
| **ELE-007** | LED Indicator | Bi-color (Red/Green), 5mm, panel mount | 2 | pc | Local electronics | $2 |
| **ELE-008** | Battery Holder | 3x 18650 holder with leads | 1 | pc | Local electronics | $3 |
| **ELE-009** | 18650 Cells | Li-ion 3.7V 2600mAh (Samsung/LG) | 3 | pc | Local electronics | $15 |
| **ELE-010** | BMS Module | 3S 12.6V 10A protection board | 1 | pc | Local electronics | $5 |
| **ELE-011** | DC-DC Converter | 12V to 5V, 1A, USB output | 1 | pc | Local electronics | $3 |
| **ELE-012** | Wiring | 18AWG silicone wire, red/black, 2m each | 1 | set | Local electronics | $4 |
| **ELE-013** | Connectors | JST-XH 2-pin, 3-pin assortment | 1 | kit | Local electronics | $5 |
| **ELE-014** | Voltage Display | Mini 0.28" LED voltmeter, 3-wire | 1 | pc | Local electronics | $3 |
| **ELE-015** | Buzzer | 5V active buzzer, panel mount | 1 | pc | Local electronics | $2 |
| | | | | | **Subtotal** | **$62** |

## 1.6 Projectile System ($54)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **PRJ-001** | Tennis Balls | Standard 58mm diameter | 12 | pc | Sports store | $10 |
| **PRJ-002** | Foam Sabots | EVA foam, 32mm OD x 30mm length | 12 | pc | DIY from sheet | $8 |
| **PRJ-003** | Fin Set A | 3D printed PLA (P11), 4-fin 15 deg cant | 4 | set | 3D print | $6 |
| **PRJ-004** | Fin Set B | 3D printed PLA (P12), 4-fin 10 deg cant | 4 | set | 3D print | $6 |
| **PRJ-005** | Fin Set C | 3D printed PLA (P13), 6-fin straight | 4 | set | 3D print | $6 |
| **PRJ-006** | Weighted Nose | 3D printed PLA (P14) + steel BB fill | 4 | pc | 3D print + BB | $8 |
| **PRJ-007** | EVA Foam Sheet | 10mm thick, 500x500mm | 2 | pc | Craft store | $10 |
| | | | | | **Subtotal** | **$54** |

## 1.7 Test Equipment ($140)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **TST-001** | Chronograph | Airsoft/paintball, LCD display | 1 | pc | Import (AliExpress) | $35 |
| **TST-002** | Digital Scale | 0.1g resolution, 500g capacity | 1 | pc | Local | $15 |
| **TST-003** | Pressure Gauge (Digital) | 0-250 bar, 0.1 bar resolution | 1 | pc | Import | $45 |
| **TST-004** | Multimeter | Basic DMM with frequency | 1 | pc | Local electronics | $20 |
| **TST-005** | Oscilloscope (Optional) | 2-ch, 50MHz, for valve timing | 1 | pc | Import/borrow | ($150) |
| **TST-006** | High-Speed Camera (Optional) | 240fps smartphone or GoPro | 1 | pc | Use existing | ($0) |
| **TST-007** | Safety Glasses | ANSI Z87.1 rated | 2 | pc | Local hardware | $10 |
| **TST-008** | Target Frame | PVC pipe + cardboard backing | 1 | set | Local hardware | $15 |
| | | | | | **Subtotal** | **$140** |
| | | | | | *(with optional)* | *($290)* |

## 1.8 Fasteners & Hardware ($33)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **HDW-001** | Socket Head Cap Screw | M4x12mm, SS A2 | 20 | pc | Local hardware | $4 |
| **HDW-002** | Socket Head Cap Screw | M4x20mm, SS A2 | 10 | pc | Local hardware | $3 |
| **HDW-003** | Socket Head Cap Screw | M3x10mm, SS A2 | 10 | pc | Local hardware | $2 |
| **HDW-004** | Hex Nut | M4, SS A2 | 20 | pc | Local hardware | $2 |
| **HDW-005** | Flat Washer | M4, SS A2 | 30 | pc | Local hardware | $2 |
| **HDW-006** | Lock Washer | M4 split, SS A2 | 20 | pc | Local hardware | $2 |
| **HDW-007** | Nylon Washer | M4 isolator | 10 | pc | Local hardware | $2 |
| **HDW-008** | Cable Ties | 100mm, black, 100pcs | 1 | bag | Local hardware | $3 |
| **HDW-009** | Heat Shrink | Assorted sizes, 100pcs | 1 | kit | Local electronics | $5 |
| **HDW-010** | Hex Key Set | 1.5, 2, 2.5, 3, 4, 5mm | 1 | set | Local hardware | $8 |
| | | | | | **Subtotal** | **$33** |

---

# 2. COST SUMMARY

## 2.1 Budget Breakdown

| Category | Cost (USD) | % of Total |
|----------|------------|------------|
| Pneumatic System | $282 | 40.8% |
| Barrel Assembly | $54 | 7.8% |
| Receiver Assembly (3D) | $34 | 4.9% |
| Stock Assembly | $32 | 4.6% |
| Electronics & Safety | $62 | 9.0% |
| Projectile System | $54 | 7.8% |
| Test Equipment (basic) | $140 | 20.3% |
| Fasteners & Hardware | $33 | 4.8% |
| **TOTAL (Basic)** | **$691** | **100%** |
| | | |
| Contingency (15%) | $104 | |
| **GRAND TOTAL** | **$795** | |
| | | |
| *Optional: Oscilloscope* | *+$150* | |
| *Optional: Al Barrel* | *+$30* | |
| **TOTAL (Full)** | **$975** | |

## 2.2 Cost by Source

| Source Type | Est. Cost | Lead Time |
|-------------|-----------|-----------|
| Import (USA) - Regulator, Solenoid | ~$150 | 3-4 weeks |
| Import (China/AliExpress) - Chrono, inserts, gauge | ~$100 | 2-3 weeks |
| Local electronics (Vietnam) | ~$62 | 1-3 days |
| Local hardware (Vietnam) | ~$100 | 1-3 days |
| Local pneumatic (Vietnam) | ~$75 | 1-3 days |
| 3D printing (own/service) | ~$50-80 | 4-5 days |
| Other local (sports, craft) | ~$40 | 1-3 days |

## 2.3 3D Printing Cost Detail

| Option | Cost | Notes |
|--------|------|-------|
| **Own printer** | ~$20 filament | PETG 700g @ $25/kg + PLA 100g @ $20/kg |
| **Print service** | $50-80 | Vietnamese 3D print shops |

---

# 3. PROCUREMENT PLAN

## 3.1 Procurement Timeline

```
PROCUREMENT TIMELINE
═══════════════════════════════════════════════════════════════════════════════

WEEK 0 (NOW) ─────────────────────────────────────────────────────────────
| ORDER IMMEDIATELY - Long lead time items (3-4 weeks shipping)
|
| [ ] PNE-002: Ninja SLP Regulator (ANS Gear, USA)      ~$85
| [ ] PNE-006: Solenoid Valve (PE/Dye, import)           ~$65
| [ ] TST-001: Chronograph (AliExpress)                  ~$35
| [ ] RCV-006/007: Heat-set inserts (AliExpress)         ~$8
| [ ] TST-003: Digital pressure gauge (AliExpress)       ~$45
|                                              SUBTOTAL: ~$238

WEEK 1 ───────────────────────────────────────────────────────────────────
| ORDER - Domestic items (1-3 day delivery)
|
| [ ] PNE-001: HPA Tank (local paintball/SCUBA)          ~$50
| [ ] PNE-003 to PNE-012: Pneumatic fittings (local)     ~$75
| [ ] ELE-001 to ELE-015: Electronics (local shops)      ~$62
| [ ] HDW-001 to HDW-010: Hardware (local)                ~$33
|                                              SUBTOTAL: ~$220

WEEK 1-2 ─────────────────────────────────────────────────────────────────
| ACTION - 3D Printing
|
| [ ] Finalize all CAD models (P01-P14)
| [ ] Start printing Batch 1 (critical path, ~16h)
| [ ] Continue Batch 2-4 (~32h remaining)
|                                              SUBTOTAL: ~$20-80

WEEK 2 ───────────────────────────────────────────────────────────────────
| ORDER - Remaining local items
|
| [ ] BAR-001: PVC barrel tube (local hardware)           ~$5
| [ ] PRJ-001: Tennis balls (sports store)                ~$10
| [ ] PRJ-007: EVA foam (craft store)                     ~$10
| [ ] STK-003: Recoil pad (local hardware)                ~$5
| [ ] STK-004: Aluminum extrusion (local hardware)        ~$8
|                                              SUBTOTAL: ~$38

WEEK 3-4 ─────────────────────────────────────────────────────────────────
| RECEIVE & INVENTORY
|
| [ ] Receive import items (verify condition)
| [ ] Inventory check (all line items accounted)
| [ ] Test key components (solenoid, regulator)
| [ ] Begin assembly

═══════════════════════════════════════════════════════════════════════════════
```

## 3.2 Critical Path Items

| Item | Why Critical | Earliest Available | Mitigation |
|------|-------------|-------------------|------------|
| **PNE-002** Ninja Regulator | Only source for adjustable HPA reg | Week 3-4 | Order from 2 sources |
| **PNE-006** Solenoid Valve | Core pneumatic component | Week 2-3 | AliExpress backup |
| **PNE-001** HPA Tank | Needed for all testing | Week 1 | Contact local paintball first |
| **TST-001** Chronograph | Required for EXP-1, EXP-2, EXP-4 | Week 2-3 | Can borrow from airsoft club |

---

# 4. SUPPLIER DIRECTORY

## 4.1 Import Suppliers (Paintball Equipment)

| Supplier | Website | Ships to VN | Items | Est. Shipping |
|----------|---------|-------------|-------|---------------|
| ANS Gear | ansgear.com | Yes | Ninja regulators, PE solenoids | ~$30 |
| Paintball Gateway | pbgateway.com | Yes | PE/Dye parts, spare parts | ~$25 |
| AliExpress | aliexpress.com | Free/cheap | Chronograph, inserts, gauges | Free-$5 |
| Amazon.com | amazon.com | Via forwarder | Backup for regulator | ~$40 |

## 4.2 Local Suppliers (Vietnam)

### Paintball/Airsoft

| Supplier | Location | Contact | Items |
|----------|----------|---------|-------|
| Paintball Vietnam | TP.HCM | Facebook: "Paintball Vietnam" | HPA tanks, masks |
| Airsoft Vietnam | Hanoi | airsoftvn.com | Tanks, accessories |
| Local SCUBA shop | Various | — | HPA fill service |

### Electronics

| Supplier | Location | Items | Notes |
|----------|----------|-------|-------|
| Nhat Tao Electronics | Q.10, HCMC | Arduino, components | Large selection |
| Linh Kien Dien Tu | Hanoi | Full range | Good prices |
| Dien Tu Viet | Online | Batteries, modules | Ships nationwide |
| Lazada/Shopee | Online | Search by item | Compare prices |

### Hardware & Pneumatics

| Supplier | Location | Items |
|----------|----------|-------|
| Local pneumatic shops | Industrial zones | Fittings, hoses, valves |
| Nguyen Kim | Nationwide | Tools, general hardware |
| Hardware stores | Nationwide | Fasteners, tube, extrusions |

### 3D Printing Services

| Supplier | Location | Material | Price |
|----------|----------|----------|-------|
| In 3D Viet Nam | HCMC | PETG, PLA | ~$0.10/g |
| 3D Printing Hanoi | Hanoi | PETG, PLA | ~$0.08/g |
| FabLab Saigon | HCMC | Various | Hourly rate |
| Shopee/Lazada | Online | Quote-based | Varies |

---

# 5. ITEM-BY-ITEM ORDERING GUIDE

## 5.1 Ninja SLP Regulator (PNE-002) — CRITICAL

| Detail | Value |
|--------|-------|
| **Item** | Ninja Paintball SLP Regulator |
| **Spec** | Adjustable 450-800 psi (31-55 bar) output |
| **Price** | $75-95 USD |
| **Lead Time** | 2-4 weeks |
| **Priority** | CRITICAL |

**Search Terms:** "Ninja SLP regulator", "Ninja 4500 SLP tank regulator"

**Order Notes:**
- Get **adjustable** version (not fixed pressure)
- Confirm thread compatibility (standard paintball ASA)
- Consider ordering spare O-ring kit
- Alternative: Guerrilla Air adjustable regulator ($60-80)

```
[ ] ORDERED    Date: ________    Order #: ________________
[ ] SHIPPED    Tracking: ________________________________
[ ] RECEIVED   Date: ________    Condition: ______________
```

## 5.2 Solenoid Valve (PNE-006) — CRITICAL

| Detail | Value |
|--------|-------|
| **Item** | Paintball marker solenoid valve |
| **Spec** | 12V, NC (normally closed), <10ms response |
| **Price** | $40-80 USD |
| **Lead Time** | 2-3 weeks |
| **Priority** | CRITICAL |

**Options:**

| Source | Part | Price | Notes |
|--------|------|-------|-------|
| ANS Gear | Planet Eclipse solenoid | $60-80 | OEM quality |
| AliExpress | Generic paintball solenoid | $20-40 | Budget option |
| eBay | Used marker solenoid | $30-50 | Check condition |

**Order Notes:**
- **Must be 12V** (not 9V or 7.4V)
- Normally closed (NC) type required
- Get wiring diagram/pinout if available

```
[ ] ORDERED    Date: ________    Order #: ________________
[ ] SHIPPED    Tracking: ________________________________
[ ] RECEIVED   Date: ________    Condition: ______________
```

## 5.3 HPA Tank (PNE-001) — CRITICAL

| Detail | Value |
|--------|-------|
| **Item** | High Pressure Air tank |
| **Spec** | 48ci (0.8L) / 3000psi (207 bar), aluminum |
| **Price** | $40-60 USD |
| **Lead Time** | 1-3 days (local) / 2-3 weeks (import) |
| **Priority** | CRITICAL |

**Order Notes:**
- Must be DOT/TC certified for HPA use
- Standard paintball ASA thread
- Hydro test date should be current (<5 years)
- Local paintball shops or SCUBA shops may stock

```
[ ] ORDERED    Date: ________    Supplier: _______________
[ ] RECEIVED   Date: ________    Hydro date: _____________
```

## 5.4 Chronograph (TST-001) — HIGH

| Detail | Value |
|--------|-------|
| **Item** | Airsoft/Paintball Chronograph |
| **Spec** | LCD display, measures fps/m/s |
| **Price** | $25-45 USD |
| **Lead Time** | 2-3 weeks |
| **Priority** | HIGH |

**Options:**

| Source | Item | Price |
|--------|------|-------|
| AliExpress | X3200 Chronograph | $25-35 |
| AliExpress | E9800 Chronograph | $30-40 |
| Amazon | Acetech AC5000 | $40-50 |

**Order Notes:**
- Must display **m/s** (not just fps)
- Battery powered preferred
- Check sensor spacing fits 32mm projectile

```
[ ] ORDERED    Date: ________    Order #: ________________
[ ] SHIPPED    Tracking: ________________________________
[ ] RECEIVED   Date: ________    Condition: ______________
```

---

# 6. PROCUREMENT TRACKING

```
MASTER PROCUREMENT TRACKER
═══════════════════════════════════════════════════════════════════════════════

WEEK 0 IMPORTS (Order by: ________)
─────────────────────────────────────────────────────────────────────────────
Item                    | Ordered | Shipped | Received | Cost   | Notes
------------------------+---------+---------+----------+--------+----------
Ninja SLP Regulator     | [ ]     | [ ]     | [ ]      |        |
Solenoid Valve          | [ ]     | [ ]     | [ ]      |        |
Chronograph             | [ ]     | [ ]     | [ ]      |        |
Heat-set Inserts        | [ ]     | [ ]     | [ ]      |        |
Digital Pressure Gauge  | [ ]     | [ ]     | [ ]      |        |

WEEK 1 DOMESTIC (Order by: ________)
─────────────────────────────────────────────────────────────────────────────
Item                    | Ordered | Shipped | Received | Cost   | Notes
------------------------+---------+---------+----------+--------+----------
HPA Tank                | [ ]     | [ ]     | [ ]      |        |
Pneumatic Fittings      | [ ]     | [ ]     | [ ]      |        |
Electronics Package     | [ ]     | [ ]     | [ ]      |        |
Hardware                | [ ]     | [ ]     | [ ]      |        |
Barrel/Projectile       | [ ]     | [ ]     | [ ]      |        |

3D PRINTING
─────────────────────────────────────────────────────────────────────────────
Item                    | Started | Complete| Post-proc| Notes
------------------------+---------+---------+----------+------------------
Batch 1 (P01,P03,P05)  | [ ]     | [ ]     | [ ]      | 16h, critical
Batch 2 (P09,P10)      | [ ]     | [ ]     | [ ]      | 15h
Batch 3 (P02,P04,P06-8)| [ ]     | [ ]     | [ ]      | 11h
Batch 4 (P11-P14)      | [ ]     | [ ]     | [ ]      | 6.5h

═══════════════════════════════════════════════════════════════════════════════

RUNNING TOTAL: $________ / $800 budget

═══════════════════════════════════════════════════════════════════════════════
```

---

# 7. RISK MITIGATION

| Risk | Prob. | Impact | Mitigation Strategy |
|------|-------|--------|---------------------|
| Regulator delayed >4 weeks | Medium | HIGH | Order from 2 sources simultaneously |
| Solenoid incompatible | Low | HIGH | Verify 12V/NC spec before ordering; get pinout |
| HPA tank unavailable locally | Medium | Medium | AliExpress backup order (longer lead time) |
| 3D print failures | Medium | Low | Extra filament, print critical parts first |
| Component DOA on arrival | Low | Medium | Test immediately on receipt, order spares |
| Chronograph sensor too narrow | Low | Medium | Verify 32mm+ clearance in listing |
| Budget overrun | Low | Medium | Contingency 15%, prioritize essentials |

---

# 8. ACTION ITEMS FOR DAY 1

```
TODAY'S ACTIONS (Week 0)
═══════════════════════════════════════════════════════════════════════════════

[ ] 1. ORDER NINJA REGULATOR
      -> Go to: ansgear.com
      -> Search: "Ninja SLP regulator"
      -> Select adjustable version
      -> Checkout with international shipping to Vietnam

[ ] 2. ORDER SOLENOID VALVE
      -> Go to: ansgear.com or AliExpress
      -> Search: "paintball solenoid 12V"
      -> Verify: 12V, NC type
      -> Order

[ ] 3. ORDER CHRONOGRAPH
      -> Go to: AliExpress
      -> Search: "airsoft chronograph X3200"
      -> Order cheapest with good reviews

[ ] 4. ORDER HEAT-SET INSERTS + PRESSURE GAUGE
      -> AliExpress: "M4 heat set insert brass 100pcs"
      -> AliExpress: "digital pressure gauge 250bar 1/8 NPT"
      -> Order both

[ ] 5. LOCATE LOCAL HPA TANK SOURCE
      -> Search Facebook: "Paintball Vietnam"
      -> Contact for tank availability
      -> OR visit local SCUBA shop

[ ] 6. START CAD DESIGN FINALIZATION
      -> Review 3D print specifications in prototype_design.md
      -> Begin modeling in CAD software
      -> Prepare STL exports

═══════════════════════════════════════════════════════════════════════════════
```

---

# 9. DOCUMENT LINKS

## Phase 4 Documents
- [[04_detail/prototype_design|Prototype Design Specifications]]
- [[04_detail/experiment_procedures|Experiment Procedures]]
- [[04_detail/scale_up_production|Scale-Up & Production Design]]
- [[04_detail/gate_review|Gate 4A/4B Review]]

## Phase 3 Reference
- [[03_embodiment/OCP_optimization_production|Phase 3: BOM & Production]]
- [[VN-CUA-001_product_spec|Product Specification v1.4]]

---

# 10. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **2.0** | **2026-02-08** | **Restructured: Merged prototype_BOM.md + procurement_guide.md into single comprehensive document. 8 subsystems, 55 line items, $795 budget, 4-week procurement timeline, supplier directory, tracking sheets.** |
| 1.0 | 2026-02-05 | Initial BOM and procurement guide (separate files). |

---

*Start ordering Week 0 items immediately to minimize schedule risk.*

**Next:** [[04_detail/experiment_procedures|Experiment Procedures]]
