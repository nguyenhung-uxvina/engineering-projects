---
project: VN-CUA-001
designation: VDC-33
type: procurement_guide
version: 1.0
created: 2026-02-05
status: active
total_budget: $800-1000
---

# VN-CUA-001: VDC-33 PROCUREMENT GUIDE
## Prototype Component Ordering Checklist

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Budget:** $800-1,000 USD
**Timeline:** 4 weeks to full assembly

---

## 1. PROCUREMENT PRIORITY MATRIX

```
PROCUREMENT TIMELINE
═══════════════════════════════════════════════════════════════════════════

WEEK 0 (NOW) ─────────────────────────────────────────────────────────────
│ ORDER IMMEDIATELY - Long lead time items (3-4 weeks shipping)
│
│ ☐ Ninja SLP Regulator (USA)
│ ☐ Solenoid Valve (USA/China)
│ ☐ Chronograph (AliExpress)
│ ☐ Heat-set inserts (AliExpress)
│
WEEK 1 ───────────────────────────────────────────────────────────────────
│ ORDER - Domestic items (1 week delivery)
│
│ ☐ HPA Tank (local paintball/SCUBA)
│ ☐ Pneumatic fittings (local)
│ ☐ Electronics (local)
│ ☐ Hardware (local)
│
WEEK 1-2 ─────────────────────────────────────────────────────────────────
│ ACTION - 3D Printing
│
│ ☐ Finalize CAD designs
│ ☐ Start printing (48h total)
│
WEEK 2-3 ─────────────────────────────────────────────────────────────────
│ RECEIVE - Import items arriving
│
│ ☐ Inventory check
│ ☐ Test components
│
WEEK 3-4 ─────────────────────────────────────────────────────────────────
│ ASSEMBLY & TEST
│
│ ☐ Assemble prototype
│ ☐ Begin experiments

═══════════════════════════════════════════════════════════════════════════
```

---

## 2. WEEK 0: IMMEDIATE ORDERS (Long Lead Time)

### 2.1 Ninja SLP Regulator

| Detail        | Value                                     |
| ------------- | ----------------------------------------- |
| **Item**      | Ninja Paintball SLP Regulator             |
| **Spec**      | Adjustable 450-800 psi (31-55 bar) output |
| **Price**     | $75-95 USD                                |
| **Lead Time** | 2-4 weeks                                 |
| **Priority**  | 🔴 CRITICAL                               |

**Supplier Options:**

| Supplier | URL | Notes |
|----------|-----|-------|
| ANS Gear | ansgear.com | Best selection, ships international |
| Paintball Gateway | pbgateway.com | Alternative |
| Amazon.com | amazon.com | Search "Ninja SLP regulator" |

**Search Terms:** "Ninja SLP regulator", "Ninja 4500 SLP tank regulator"

**Order Notes:**
- Get adjustable version (not fixed pressure)
- Confirm thread compatibility (standard paintball ASA)
- Consider ordering spare O-ring kit

```
☐ ORDERED    Date: ________    Order #: ________________
☐ SHIPPED    Tracking: ________________________________
☐ RECEIVED   Date: ________    Condition: ______________
```

---

### 2.2 Solenoid Valve

| Detail | Value |
|--------|-------|
| **Item** | Paintball marker solenoid valve |
| **Spec** | 12V, NC (normally closed), <10ms response |
| **Price** | $40-80 USD |
| **Lead Time** | 2-3 weeks |
| **Priority** | 🔴 CRITICAL |

**Supplier Options:**

| Supplier | Part Number | Price | Notes |
|----------|-------------|-------|-------|
| ANS Gear | Planet Eclipse solenoid | $60-80 | OEM quality |
| AliExpress | Generic paintball solenoid | $20-40 | Budget option |
| eBay | Used marker solenoid | $30-50 | Check condition |

**Search Terms:** "paintball solenoid valve 12V", "Planet Eclipse solenoid", "Dye solenoid"

**Order Notes:**
- Must be 12V (not 9V or 7.4V)
- Normally closed (NC) type required
- Get wiring diagram/pinout if available

```
☐ ORDERED    Date: ________    Order #: ________________
☐ SHIPPED    Tracking: ________________________________
☐ RECEIVED   Date: ________    Condition: ______________
```

---

### 2.3 Chronograph

| Detail | Value |
|--------|-------|
| **Item** | Airsoft/Paintball Chronograph |
| **Spec** | LCD display, measures fps/m/s |
| **Price** | $25-45 USD |
| **Lead Time** | 2-3 weeks |
| **Priority** | 🟡 HIGH |

**Supplier Options:**

| Supplier | Item | Price | Notes |
|----------|------|-------|-------|
| AliExpress | X3200 Chronograph | $25-35 | Popular, reliable |
| AliExpress | E9800 Chronograph | $30-40 | Larger display |
| Amazon | Acetech AC5000 | $40-50 | Better quality |

**Search Terms:** "airsoft chronograph", "paintball chronograph LCD"

**Order Notes:**
- Must display m/s (not just fps)
- Battery powered preferred
- Check sensor spacing fits 32mm projectile

```
☐ ORDERED    Date: ________    Order #: ________________
☐ SHIPPED    Tracking: ________________________________
☐ RECEIVED   Date: ________    Condition: ______________
```

---

### 2.4 Heat-Set Inserts

| Detail | Value |
|--------|-------|
| **Item** | Brass heat-set threaded inserts |
| **Spec** | M4×5.6mm×6mm (18pcs needed) |
| **Price** | $5-10 USD |
| **Lead Time** | 2-3 weeks |
| **Priority** | 🟡 HIGH |

**Supplier Options:**

| Supplier | Item | Price | Notes |
|----------|------|-------|-------|
| AliExpress | M4 brass inserts 100pcs | $5-8 | Best value |
| Amazon | McMaster-style inserts | $10-15 | Faster shipping |

**Search Terms:** "M4 heat set insert brass", "M4 threaded insert 3D printing"

**Order Notes:**
- Get M4 size (5.6mm OD × 6mm length)
- Order 50+ pcs (extras for mistakes)
- Also get M3 size if using smaller fasteners

```
☐ ORDERED    Date: ________    Order #: ________________
☐ SHIPPED    Tracking: ________________________________
☐ RECEIVED   Date: ________    Condition: ______________
```

---

### 2.5 Digital Pressure Gauge (Optional but Recommended)

| Detail | Value |
|--------|-------|
| **Item** | Digital pressure gauge |
| **Spec** | 0-250 bar, 0.1 bar resolution, 1/8" NPT |
| **Price** | $30-50 USD |
| **Lead Time** | 2-3 weeks |
| **Priority** | 🟢 MEDIUM |

**Supplier Options:**

| Supplier | Item | Price |
|----------|------|-------|
| AliExpress | Digital pressure gauge 250bar | $25-40 |
| Amazon | Winters digital gauge | $40-60 |

```
☐ ORDERED    Date: ________    Order #: ________________
☐ SHIPPED    Tracking: ________________________________
☐ RECEIVED   Date: ________    Condition: ______________
```

---

## 3. WEEK 1: DOMESTIC ORDERS

### 3.1 HPA Tank

| Detail | Value |
|--------|-------|
| **Item** | High Pressure Air tank |
| **Spec** | 48ci (0.8L) / 3000psi (207 bar), aluminum |
| **Price** | $40-60 USD |
| **Lead Time** | 1-3 days (local) |
| **Priority** | 🔴 CRITICAL |

**Supplier Options (Vietnam):**

| Supplier | Location | Contact |
|----------|----------|---------|
| Paintball Vietnam | TP.HCM | Facebook: "Paintball Vietnam" |
| SCUBA shops | Nationwide | Search "bình khí nén SCUBA" |
| Industrial gas suppliers | Hanoi/HCMC | May have paintball-compatible tanks |

**Alternative:** Order from AliExpress (2-3 week lead time)

**Order Notes:**
- Must be DOT/TC certified for HPA use
- Get with standard paintball ASA thread
- Hydro test date should be current (<5 years)

```
☐ ORDERED    Date: ________    Supplier: _______________
☐ RECEIVED   Date: ________    Hydro date: _____________
```

---

### 3.2 Pneumatic Fittings & Hose

| Item | Spec | Qty | Est. Price |
|------|------|-----|------------|
| Macro line | SS braided, 6mm OD, 1m | 1 | $15 |
| Quick disconnect | Foster style, 1/8" NPT | 2 sets | $10 |
| Pressure gauge (analog) | 0-160 bar, 1/8" NPT | 1 | $12 |
| Tee fitting | 1/8" NPT brass | 2 | $5 |
| Elbow fitting | 1/8" NPT 90° | 2 | $4 |
| Push-fit adapter | 1/8" NPT to 6mm | 4 | $8 |
| Relief valve | 120 bar preset | 1 | $18 |
| PTFE tape | Thread sealant | 2 | $2 |
| **SUBTOTAL** | | | **~$75** |

**Supplier Options (Vietnam):**

| Supplier | Location | Items |
|----------|----------|-------|
| Pneumatic supply shops | Industrial zones | Fittings, hose |
| Hydraulic shops | Nationwide | High-pressure fittings |
| Kim Tín / similar | Hanoi/HCMC | General pneumatics |

**Search Terms (Vietnamese):** "phụ kiện khí nén", "ống khí nén", "van khí nén"

```
☐ ORDERED    Date: ________    Supplier: _______________
☐ RECEIVED   Date: ________    All items: ☐ Complete
```

---

### 3.3 Electronics Package

| Item | Spec | Qty | Est. Price |
|------|------|-----|------------|
| Arduino Nano | ATmega328P, USB-C | 1 | $8 |
| MOSFET module | IRF520 | 1 | $3 |
| Toggle switch | SPST, panel mount | 1 | $2 |
| Slide switch | SPST | 1 | $2 |
| Microswitch | SPST-NO, lever | 1 | $2 |
| Bi-color LED | 5mm, common cathode | 2 | $2 |
| Green LED | 5mm | 2 | $1 |
| Piezo buzzer | 5V active | 1 | $2 |
| 18650 holder | 3S with leads | 1 | $3 |
| 18650 cells | Samsung/LG 2600mAh | 3 | $15 |
| BMS module | 3S 12.6V 10A | 1 | $5 |
| DC-DC converter | 12V→5V | 1 | $3 |
| Resistors | 10kΩ, 330Ω assorted | 20 | $2 |
| Wire | 18AWG silicone, 2m | 1 | $4 |
| Connectors | JST-XH assorted | 1 kit | $5 |
| Voltage display | 0.28" LED | 1 | $3 |
| **SUBTOTAL** | | | **~$62** |

**Supplier Options (Vietnam):**

| Supplier | Location | Notes |
|----------|----------|-------|
| Nhật Tảo Electronics | Q.10, HCMC | Large selection |
| Linh Kiện Điện Tử | Hanoi | Full range |
| Điện Tử Việt | Online | Ships nationwide |
| Lazada/Shopee | Online | Search by item |

**Search Terms (Vietnamese):** "Arduino Nano", "linh kiện điện tử", "pin 18650"

```
☐ ORDERED    Date: ________    Supplier: _______________
☐ RECEIVED   Date: ________    All items: ☐ Complete
```

---

### 3.4 Hardware

| Item | Spec | Qty | Est. Price |
|------|------|-----|------------|
| Socket head cap screw | M4×12 SS | 20 | $4 |
| Socket head cap screw | M4×20 SS | 10 | $3 |
| Socket head cap screw | M3×10 SS | 10 | $2 |
| Hex nut | M4 SS | 20 | $2 |
| Flat washer | M4 SS | 30 | $2 |
| Lock washer | M4 split SS | 20 | $2 |
| Nylon washer | M4 isolator | 10 | $2 |
| Cable ties | 100mm black | 100 | $3 |
| Heat shrink | Assorted | 100 | $5 |
| Hex key set | 1.5-5mm | 1 | $8 |
| **SUBTOTAL** | | | **~$33** |

**Supplier Options (Vietnam):**

| Supplier | Location |
|----------|----------|
| Hardware stores | Nationwide |
| Nguyễn Kim | Nationwide |
| Industrial supply | Hanoi/HCMC |

```
☐ ORDERED    Date: ________    Supplier: _______________
☐ RECEIVED   Date: ________    All items: ☐ Complete
```

---

### 3.5 Barrel & Projectile Materials

| Item | Spec | Qty | Est. Price |
|------|------|-----|------------|
| PVC pipe | 32mm ID × 300mm | 1 | $5 |
| Tennis balls | Standard 58mm | 12 | $10 |
| EVA foam sheet | 10mm × 500×500mm | 2 | $10 |
| Steel BBs | 6mm, for nose weight | 100 | $5 |
| Rubber pad | 80×40×15mm | 1 | $5 |
| Aluminum extrusion | 20×20mm × 150mm | 1 | $8 |
| **SUBTOTAL** | | | **~$43** |

**Supplier Options:**
- Hardware store: PVC, aluminum
- Sports store: Tennis balls
- Craft store: EVA foam
- Airsoft shop: Steel BBs

```
☐ ORDERED    Date: ________    Supplier: _______________
☐ RECEIVED   Date: ________    All items: ☐ Complete
```

---

## 4. 3D PRINTING

### Option A: Own Printer

| Item | Material | Weight | Time |
|------|----------|--------|------|
| All PETG parts | PETG | 690g | 42h |
| All PLA parts | PLA | 100g | 6h |
| **TOTAL** | | 790g | 48h |

**Filament Required:**
- PETG: 1kg spool (~$25)
- PLA: 250g from spool (~$5)

### Option B: Print Service (Vietnam)

| Service | Location | Est. Cost |
|---------|----------|-----------|
| In 3D Việt Nam | HCMC | ~$50-80 |
| 3D Printing Hanoi | Hanoi | ~$40-70 |
| FabLab Saigon | HCMC | Hourly rate |
| Shopee/Lazada | Online | Quote-based |

**Files to Send:**
- All STL files from 3D design specifications
- Specify: PETG for structural, PLA for fins
- Request: 40% infill structural, 100% infill fins

```
☐ PRINTED    Method: ☐ Own printer  ☐ Service
☐ COMPLETED  Date: ________
☐ POST-PROCESSED (heat-set inserts installed)
```

---

## 5. BUDGET SUMMARY

| Category | Estimated | Actual | Variance |
|----------|-----------|--------|----------|
| Week 0 imports | $200 | | |
| HPA tank | $50 | | |
| Pneumatic fittings | $75 | | |
| Electronics | $62 | | |
| Hardware | $33 | | |
| Barrel/projectile | $43 | | |
| 3D printing | $30-80 | | |
| Test equipment | $100 | | |
| **SUBTOTAL** | **$593-643** | | |
| Contingency (15%) | $97 | | |
| **TOTAL BUDGET** | **$690-740** | | |

**Notes:**
- Prices in USD
- Shipping costs may vary
- Some items may be cheaper locally
- Budget includes recommended test equipment

---

## 6. PROCUREMENT TRACKING SHEET

```
MASTER PROCUREMENT TRACKER
═══════════════════════════════════════════════════════════════════════════

WEEK 0 IMPORTS (Order by: ________)
─────────────────────────────────────────────────────────────────────────────
Item                    │ Ordered │ Shipped │ Received │ Cost   │ Notes
────────────────────────┼─────────┼─────────┼──────────┼────────┼──────────
Ninja SLP Regulator     │ ☐       │ ☐       │ ☐        │        │
Solenoid Valve          │ ☐       │ ☐       │ ☐        │        │
Chronograph             │ ☐       │ ☐       │ ☐        │        │
Heat-set Inserts        │ ☐       │ ☐       │ ☐        │        │
Digital Pressure Gauge  │ ☐       │ ☐       │ ☐        │        │

WEEK 1 DOMESTIC (Order by: ________)
─────────────────────────────────────────────────────────────────────────────
Item                    │ Ordered │ Shipped │ Received │ Cost   │ Notes
────────────────────────┼─────────┼─────────┼──────────┼────────┼──────────
HPA Tank                │ ☐       │ ☐       │ ☐        │        │
Pneumatic Fittings      │ ☐       │ ☐       │ ☐        │        │
Electronics Package     │ ☐       │ ☐       │ ☐        │        │
Hardware                │ ☐       │ ☐       │ ☐        │        │
Barrel/Projectile       │ ☐       │ ☐       │ ☐        │        │

3D PRINTING
─────────────────────────────────────────────────────────────────────────────
Item                    │ Started │ Complete│ Post-proc│ Notes
────────────────────────┼─────────┼─────────┼──────────┼──────────────────
Receiver Body (P01)     │ ☐       │ ☐       │ ☐        │ 12h print
Stock Body (P09)        │ ☐       │ ☐       │ ☐        │ 10h print
Other PETG parts        │ ☐       │ ☐       │ ☐        │
Fin sets (PLA)          │ ☐       │ ☐       │ ☐        │

═══════════════════════════════════════════════════════════════════════════

RUNNING TOTAL: $________ / $800 budget

NOTES:
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________

═══════════════════════════════════════════════════════════════════════════
```

---

## 7. ACTION ITEMS FOR TODAY

```
TODAY'S ACTIONS (Week 0)
═══════════════════════════════════════════════════════════════════════════

☐ 1. ORDER NINJA REGULATOR
      → Go to: ansgear.com
      → Search: "Ninja SLP regulator"
      → Select adjustable version
      → Add to cart, checkout with international shipping

☐ 2. ORDER SOLENOID VALVE
      → Go to: ansgear.com or AliExpress
      → Search: "paintball solenoid 12V"
      → Verify: 12V, NC type
      → Order

☐ 3. ORDER CHRONOGRAPH
      → Go to: AliExpress
      → Search: "airsoft chronograph X3200"
      → Order cheapest with good reviews

☐ 4. ORDER HEAT-SET INSERTS
      → Go to: AliExpress
      → Search: "M4 heat set insert brass 100pcs"
      → Order

☐ 5. LOCATE LOCAL HPA TANK SOURCE
      → Search Facebook: "Paintball Vietnam"
      → Contact for tank availability
      → OR search local SCUBA shops

☐ 6. START CAD DESIGN FINALIZATION
      → Review 3D print specifications
      → Begin modeling in CAD software
      → Prepare STL exports

═══════════════════════════════════════════════════════════════════════════
```

---

## 8. RISK MITIGATION

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Regulator delayed | Medium | High | Order backup from 2nd source |
| Solenoid incompatible | Low | High | Verify specs before ordering |
| Tank unavailable locally | Medium | Medium | Order from AliExpress (longer lead) |
| 3D print failures | Medium | Low | Order extra filament |
| Component DOA | Low | Medium | Test immediately upon receipt |

---

## 9. DOCUMENT LINKS

- [[VN-CUA-001_prototype_BOM|Full BOM]]
- [[VN-CUA-001_prototype_3D_designs|3D Print Specifications]]
- [[firmware/VDC33_wiring_guide|Wiring Guide]]

---

## 10. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial procurement guide. Supplier options, tracking sheets, action items.** |

---

*Start ordering Week 0 items immediately to minimize schedule risk.*
