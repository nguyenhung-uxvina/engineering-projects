---
project: VN-CUA-001
designation: VDC-33
type: prototype_bom
version: 1.0
created: 2026-02-05
status: draft
purpose: Scale prototype for pneumatic validation
scale: 1:3 (bore diameter)
---

# VN-CUA-001: VDC-33 SCALE PROTOTYPE
## Bill of Materials & Procurement Plan

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Prototype:** VDC-33 (1:3 Scale Pneumatic Demonstrator)
**Purpose:** Validate pneumatic system, safety interlocks, projectile stability
**Date:** 2026-02-05

---

## 1. PROTOTYPE SPECIFICATIONS

| Parameter | VDC-33 Prototype | VDC-100 Full Scale | Scale Factor |
|-----------|------------------|--------------------| -------------|
| Bore diameter | 32mm | 100mm | 1:3.1 |
| Barrel length | 260mm | 800mm | 1:3.1 |
| Projectile mass | 58g (tennis ball) | 450g | 1:7.8 |
| Operating pressure | 60-100 bar | 100 bar | 1:1 |
| Target velocity | 30-40 m/s | 40 m/s | 1:1 |
| Energy | ~35 J | ~360 J | 1:10 |

---

## 2. BILL OF MATERIALS

### 2.1 PNEUMATIC SYSTEM

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **PNE-001** | HPA Tank | 48ci (0.8L) / 3000psi (207 bar), aluminum | 1 | pc | Paintball shop | $50 |
| **PNE-002** | Tank Regulator | Adjustable 50-120 bar output, Ninja SLP | 1 | pc | Import (ANS Gear) | $85 |
| **PNE-003** | Macro Line | Stainless braided, 6mm OD, 1m length | 1 | m | Local pneumatic | $15 |
| **PNE-004** | Quick Disconnect | Foster style, 1/8" NPT, male+female pair | 2 | set | Local pneumatic | $10 |
| **PNE-005** | Pressure Gauge | 0-160 bar, 40mm dial, 1/8" NPT | 1 | pc | Local pneumatic | $12 |
| **PNE-006** | Solenoid Valve | 12V NC, 3-way, 8mm orifice, <10ms response | 1 | pc | Import (PE/Dye) | $65 |
| **PNE-007** | Fitting Tee | 1/8" NPT brass tee | 2 | pc | Local pneumatic | $5 |
| **PNE-008** | Fitting Elbow | 1/8" NPT brass 90° elbow | 2 | pc | Local pneumatic | $4 |
| **PNE-009** | Fitting Adapter | 1/8" NPT to 6mm push-fit | 4 | pc | Local pneumatic | $8 |
| **PNE-010** | O-ring Kit | NBR 70A, metric assortment | 1 | kit | Local hardware | $8 |
| **PNE-011** | PTFE Tape | Thread sealant, 12mm × 10m | 2 | roll | Local hardware | $2 |
| **PNE-012** | Relief Valve | 120 bar preset, 1/8" NPT | 1 | pc | Local pneumatic | $18 |
| | | | | | **Subtotal** | **$282** |

### 2.2 BARREL ASSEMBLY

| Item        | Description      | Spec                                                  | Qty | Unit | Source          | Est. Cost |
| ----------- | ---------------- | ----------------------------------------------------- | --- | ---- | --------------- | --------- |
| **BAR-001** | Barrel Tube      | PVC Schedule 40, 32mm ID × 300mm                      | 1   | pc   | Local hardware  | $5        |
| **BAR-002** | Barrel Tube (Al) | Al 6061, 32mm ID × 35mm OD × 300mm (optional upgrade) | 1   | pc   | Local machining | $35       |
| **BAR-003** | Breech Adapter   | 3D printed PETG, barrel-to-receiver                   | 1   | pc   | 3D print        | $5        |
| **BAR-004** | Muzzle Cap       | 3D printed PETG, with vent holes                      | 1   | pc   | 3D print        | $3        |
| **BAR-005** | Barrel Clamp     | 3D printed PETG, receiver mount                       | 2   | pc   | 3D print        | $4        |
| **BAR-006** | O-ring Breech    | NBR 40mm ID × 3mm CS                                  | 2   | pc   | Local hardware  | $2        |
|             |                  |                                                       |     |      | **Subtotal**    | **$54**   |

### 2.3 RECEIVER ASSEMBLY (3D Printed)

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **RCV-001** | Receiver Body | 3D printed PETG, main housing | 1 | pc | 3D print (~200g) | $12 |
| **RCV-002** | Valve Mount | 3D printed PETG, solenoid holder | 1 | pc | 3D print (~50g) | $4 |
| **RCV-003** | Rail Mount | 3D printed PETG, Picatinny section | 1 | pc | 3D print (~30g) | $3 |
| **RCV-004** | Trigger Guard | 3D printed PETG | 1 | pc | 3D print (~20g) | $2 |
| **RCV-005** | Grip | 3D printed PETG, ergonomic | 1 | pc | 3D print (~60g) | $5 |
| **RCV-006** | Insert Nuts | M4 brass heat-set inserts | 20 | pc | Import (AliExpress) | $5 |
| **RCV-007** | Insert Nuts | M3 brass heat-set inserts | 10 | pc | Import (AliExpress) | $3 |
| | | | | | **Subtotal** | **$34** |

### 2.4 STOCK ASSEMBLY

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **STK-001** | Stock Body | 3D printed PETG, adjustable | 1 | pc | 3D print (~150g) | $10 |
| **STK-002** | Tank Clamp | 3D printed PETG, HPA tank mount | 1 | pc | 3D print (~80g) | $6 |
| **STK-003** | Recoil Pad | Rubber, 80mm × 40mm × 15mm | 1 | pc | Local hardware | $5 |
| **STK-004** | Adjustment Rail | Aluminum extrusion 20×20, 150mm | 1 | pc | Local hardware | $8 |
| **STK-005** | Adjustment Knob | M6 knurled knob | 1 | pc | Local hardware | $3 |
| | | | | | **Subtotal** | **$32** |

### 2.5 ELECTRONICS & SAFETY

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **ELE-001** | Arduino Nano | ATmega328P, USB-C | 1 | pc | Local electronics | $8 |
| **ELE-002** | Relay Module | 5V 1-channel, optocoupler isolated | 1 | pc | Local electronics | $3 |
| **ELE-003** | MOSFET Module | IRF520, 12V/5A | 1 | pc | Local electronics | $3 |
| **ELE-004** | Toggle Switch | SPST, panel mount, ARM switch | 1 | pc | Local electronics | $2 |
| **ELE-005** | Safety Switch | SPST, slide type, mechanical safety | 1 | pc | Local electronics | $2 |
| **ELE-006** | Trigger Switch | Microswitch, 5A, lever actuator | 1 | pc | Local electronics | $2 |
| **ELE-007** | LED Indicator | Bi-color (Red/Green), 5mm, panel mount | 2 | pc | Local electronics | $2 |
| **ELE-008** | Battery Holder | 3× 18650 holder with leads | 1 | pc | Local electronics | $3 |
| **ELE-009** | 18650 Cells | Li-ion 3.7V 2600mAh (Samsung/LG) | 3 | pc | Local electronics | $15 |
| **ELE-010** | BMS Module | 3S 12.6V 10A protection board | 1 | pc | Local electronics | $5 |
| **ELE-011** | DC-DC Converter | 12V→5V, 1A, USB output | 1 | pc | Local electronics | $3 |
| **ELE-012** | Wiring | 18AWG silicone wire, red/black, 2m each | 1 | set | Local electronics | $4 |
| **ELE-013** | Connectors | JST-XH 2-pin, 3-pin assortment | 1 | kit | Local electronics | $5 |
| **ELE-014** | Voltage Display | Mini 0.28" LED voltmeter, 3-wire | 1 | pc | Local electronics | $3 |
| **ELE-015** | Buzzer | 5V active buzzer, panel mount | 1 | pc | Local electronics | $2 |
| | | | | | **Subtotal** | **$62** |

### 2.6 PROJECTILE SYSTEM

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **PRJ-001** | Tennis Balls | Standard 58mm diameter | 12 | pc | Sports store | $10 |
| **PRJ-002** | Foam Sabots | EVA foam, 32mm OD × 30mm length | 12 | pc | DIY from sheet | $8 |
| **PRJ-003** | Fin Set (Test A) | 3D printed PLA, 4-fin, 15° cant | 4 | set | 3D print | $6 |
| **PRJ-004** | Fin Set (Test B) | 3D printed PLA, 4-fin, 10° cant | 4 | set | 3D print | $6 |
| **PRJ-005** | Fin Set (Test C) | 3D printed PLA, 6-fin, straight | 4 | set | 3D print | $6 |
| **PRJ-006** | Weighted Nose | 3D printed with steel BB fill, 20g | 4 | pc | 3D print + BB | $8 |
| **PRJ-007** | EVA Foam Sheet | 10mm thick, 500×500mm | 2 | pc | Craft store | $10 |
| | | | | | **Subtotal** | **$54** |

### 2.7 TEST EQUIPMENT

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
| | | | | | **(with optional)** | **($290)** |

### 2.8 FASTENERS & HARDWARE

| Item | Description | Spec | Qty | Unit | Source | Est. Cost |
|------|-------------|------|-----|------|--------|-----------|
| **HDW-001** | Socket Head Cap Screw | M4×12mm, SS A2 | 20 | pc | Local hardware | $4 |
| **HDW-002** | Socket Head Cap Screw | M4×20mm, SS A2 | 10 | pc | Local hardware | $3 |
| **HDW-003** | Socket Head Cap Screw | M3×10mm, SS A2 | 10 | pc | Local hardware | $2 |
| **HDW-004** | Hex Nut | M4, SS A2 | 20 | pc | Local hardware | $2 |
| **HDW-005** | Flat Washer | M4, SS A2 | 30 | pc | Local hardware | $2 |
| **HDW-006** | Lock Washer | M4 split, SS A2 | 20 | pc | Local hardware | $2 |
| **HDW-007** | Nylon Washer | M4 isolator | 10 | pc | Local hardware | $2 |
| **HDW-008** | Cable Ties | 100mm, black, 100pcs | 1 | bag | Local hardware | $3 |
| **HDW-009** | Heat Shrink | Assorted sizes, 100pcs | 1 | kit | Local electronics | $5 |
| **HDW-010** | Hex Key Set | 1.5, 2, 2.5, 3, 4, 5mm | 1 | set | Local hardware | $8 |
| | | | | | **Subtotal** | **$33** |

### 2.9 3D PRINTING SUMMARY

| Part | Material | Weight | Print Time | Infill | Notes |
|------|----------|--------|------------|--------|-------|
| Receiver Body | PETG | 200g | 12h | 40% | High strength needed |
| Valve Mount | PETG | 50g | 3h | 40% | Pressure-bearing |
| Breech Adapter | PETG | 40g | 2h | 60% | Seal surface critical |
| Muzzle Cap | PETG | 20g | 1h | 30% | |
| Barrel Clamps (×2) | PETG | 40g | 2h | 50% | |
| Rail Mount | PETG | 30g | 2h | 40% | |
| Trigger Guard | PETG | 20g | 1h | 30% | |
| Grip | PETG | 60g | 4h | 30% | |
| Stock Body | PETG | 150g | 10h | 30% | |
| Tank Clamp | PETG | 80g | 5h | 40% | |
| Fin Sets (×3) | PLA | 60g | 4h | 100% | Solid for strength |
| Weighted Nose (×4) | PLA | 40g | 2h | 100% | Fill with BBs |
| **TOTAL** | | **~800g** | **~48h** | | |

**3D Printing Cost Estimate:**
- PETG: 700g × $25/kg = $17.50
- PLA: 100g × $20/kg = $2.00
- **Total filament: ~$20**
- Local print service (if no printer): $50-80

---

## 3. COST SUMMARY

| Category | Cost (USD) |
|----------|------------|
| Pneumatic System | $282 |
| Barrel Assembly | $54 |
| Receiver Assembly | $34 |
| Stock Assembly | $32 |
| Electronics & Safety | $62 |
| Projectile System | $54 |
| Test Equipment (basic) | $140 |
| Fasteners & Hardware | $33 |
| **TOTAL (Basic)** | **$691** |
| | |
| Optional: Oscilloscope | +$150 |
| Optional: Al Barrel upgrade | +$30 |
| **TOTAL (Full)** | **$871** |

**Contingency (15%):** $104
**Grand Total Budget:** **$800 - $1,000**

---

## 4. PROCUREMENT PLAN

### 4.1 Source Categories

| Category | Lead Time | Source Type |
|----------|-----------|-------------|
| **Immediate (Local)** | 1-3 days | Hardware stores, electronics shops |
| **Short (Domestic)** | 3-7 days | Vietnamese online, specialized shops |
| **Medium (Import)** | 2-4 weeks | AliExpress, international paintball |
| **Long (Specialty)** | 4-6 weeks | ANS Gear, Paintball Gateway |

### 4.2 Procurement Schedule

```
PROCUREMENT TIMELINE
═══════════════════════════════════════════════════════════════════════════

WEEK 0: ORDER LONG-LEAD ITEMS
├── PNE-002: Ninja regulator (ANS Gear, USA) - 3-4 weeks
├── PNE-006: Solenoid valve (PE/Dye, import) - 2-3 weeks
├── TST-001: Chronograph (AliExpress) - 2-3 weeks
├── RCV-006/007: Insert nuts (AliExpress) - 2 weeks
└── Budget: ~$200

WEEK 1: ORDER DOMESTIC/LOCAL ITEMS
├── PNE-001: HPA tank (paintball shop HCMC/Hanoi)
├── PNE-003 to PNE-012: Pneumatic fittings (local)
├── ELE-001 to ELE-015: Electronics (Nhật Tảo, Hà Nội)
├── HDW-001 to HDW-010: Hardware (local)
└── Budget: ~$250

WEEK 1-2: 3D PRINTING
├── Design finalization (CAD)
├── Print receiver, stock, barrel parts
├── Print projectile components
└── Budget: ~$50 (or $80 if outsourced)

WEEK 2: ORDER REMAINING ITEMS
├── BAR-001/002: Barrel tube (local)
├── PRJ-001: Tennis balls (sports store)
├── PRJ-007: EVA foam (craft store)
├── STK-003: Recoil pad (local)
└── Budget: ~$50

WEEK 3-4: RECEIVE & INVENTORY
├── Receive import items
├── Inventory check
├── Identify any missing items
└── Begin assembly

═══════════════════════════════════════════════════════════════════════════
```

### 4.3 Supplier Directory

#### Paintball Equipment (Vietnam)

| Supplier          | Location | Contact       | Items              |
| ----------------- | -------- | ------------- | ------------------ |
| Paintball Vietnam | TP.HCM   | Facebook page | HPA tanks, masks   |
| Airsoft Vietnam   | Hanoi    | airsoftvn.com | Tanks, accessories |
| Local SCUBA shop  | Various  | —             | HPA fill service   |

#### Paintball Equipment (International)

| Supplier | Website | Shipping to VN | Items |
|----------|---------|----------------|-------|
| ANS Gear | ansgear.com | Yes (~$30) | Ninja regulators, solenoids |
| Paintball Gateway | pbgateway.com | Yes | PE/Dye parts |
| AliExpress | aliexpress.com | Free/cheap | Chronograph, inserts, misc |

#### Local Electronics (Vietnam)

| Supplier | Location | Items |
|----------|----------|-------|
| Nhật Tảo Electronics | Q.10, HCMC | Arduino, components |
| Linh Kiện Điện Tử | Hanoi | Full range |
| Điện Tử Việt | Online | Batteries, modules |

#### Local Hardware (Vietnam)

| Supplier | Location | Items |
|----------|----------|-------|
| Nguyễn Kim | Nationwide | Tools, hardware |
| Điện Máy Xanh | Nationwide | Tools |
| Local pneumatic shop | Industrial zones | Fittings, hoses |

#### 3D Printing Services (Vietnam)

| Supplier | Location | Material | Price |
|----------|----------|----------|-------|
| In 3D Việt Nam | HCMC | PETG, PLA | ~$0.10/g |
| 3D Printing Hanoi | Hanoi | PETG, PLA | ~$0.08/g |
| FabLab Saigon | HCMC | Various | Hourly rate |

---

## 5. ASSEMBLY SEQUENCE

### Phase 1: Pneumatic System (Day 1-2)

```
PNEUMATIC ASSEMBLY
═══════════════════════════════════════════════════════════════════════════

Step 1: Tank + Regulator
┌─────────────────┐
│  HPA TANK       │
│  (PNE-001)      │──── Hand-tighten regulator (PNE-002)
└────────┬────────┘      Use PTFE tape on threads
         │
Step 2: Add Pressure Gauge
         │
    ┌────┴────┐
    │   TEE   │──── Install gauge (PNE-005) on branch
    │(PNE-007)│
    └────┬────┘
         │
Step 3: Add Relief Valve
    ┌────┴────┐
    │   TEE   │──── Install relief valve (PNE-012) on branch
    │(PNE-007)│
    └────┬────┘
         │
Step 4: Connect to Solenoid
    ┌────┴────┐
    │SOLENOID │──── Mount solenoid in receiver (RCV-002)
    │(PNE-006)│
    └────┬────┘
         │
Step 5: Connect to Breech
    ┌────┴────┐
    │ BREECH  │──── Seal with O-ring (BAR-006)
    │(BAR-003)│
    └─────────┘

TEST: Pressurize to 50 bar, check all connections with soapy water
      No bubbles = good seal

═══════════════════════════════════════════════════════════════════════════
```

### Phase 2: Mechanical Assembly (Day 2-3)

1. Install heat-set inserts into 3D printed parts
2. Attach barrel clamps to receiver
3. Insert barrel tube and secure
4. Mount valve assembly to receiver
5. Attach stock to receiver
6. Install tank clamp on stock
7. Install trigger guard and grip

### Phase 3: Electronics (Day 3-4)

```
WIRING DIAGRAM
═══════════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────────────────┐
                    │                 BATTERY PACK                         │
                    │           3S 18650 (11.1V nominal)                   │
                    │                 with BMS                             │
                    └─────────────────────┬───────────────────────────────┘
                                          │
                         ┌────────────────┴────────────────┐
                         │           12V BUS               │
                         │                                 │
              ┌──────────┴──────────┐          ┌──────────┴──────────┐
              │     DC-DC 5V        │          │    VOLTMETER        │
              │     (ELE-011)       │          │    (ELE-014)        │
              └──────────┬──────────┘          └─────────────────────┘
                         │
              ┌──────────┴──────────┐
              │     ARDUINO NANO    │
              │      (ELE-001)      │
              └──────────┬──────────┘
                         │
    ┌────────────────────┼────────────────────┬────────────────────┐
    │                    │                    │                    │
┌───┴───┐           ┌────┴────┐          ┌────┴────┐          ┌────┴────┐
│ ARM   │           │ SAFETY  │          │ TRIGGER │          │  LED    │
│SWITCH │           │ SWITCH  │          │ SWITCH  │          │(ELE-007)│
│(D2)   │           │  (D3)   │          │  (D4)   │          │(D5,D6)  │
└───────┘           └─────────┘          └─────────┘          └─────────┘

                         │ D7 output
              ┌──────────┴──────────┐
              │    MOSFET MODULE    │
              │      (ELE-003)      │
              └──────────┬──────────┘
                         │ 12V switched
              ┌──────────┴──────────┐
              │   SOLENOID VALVE    │
              │      (PNE-006)      │
              └─────────────────────┘

═══════════════════════════════════════════════════════════════════════════
```

### Phase 4: Integration & Test (Day 4-5)

1. Connect all wiring
2. Load Arduino firmware (safety logic)
3. Bench test: verify all interlocks
4. Low-pressure test (30 bar)
5. Increase to operating pressure (60-80 bar)
6. First projectile test (tennis ball)

---

## 6. ARDUINO SAFETY CODE (Outline)

```cpp
// VDC-33 Safety Interlock Logic
// Pins
const int PIN_ARM = 2;      // ARM switch (active HIGH)
const int PIN_SAFE = 3;     // SAFETY switch (active LOW = safe)
const int PIN_TRIG = 4;     // TRIGGER switch (active HIGH)
const int PIN_LED_R = 5;    // Red LED (armed)
const int PIN_LED_G = 6;    // Green LED (safe)
const int PIN_VALVE = 7;    // MOSFET gate (solenoid)
const int PIN_BUZZER = 8;   // Buzzer

// Timing
const int DWELL_MS = 12;    // Valve open time (adjustable)
const int DEBOUNCE = 50;    // Switch debounce

void setup() {
  pinMode(PIN_ARM, INPUT_PULLDOWN);
  pinMode(PIN_SAFE, INPUT_PULLUP);
  pinMode(PIN_TRIG, INPUT_PULLDOWN);
  pinMode(PIN_LED_R, OUTPUT);
  pinMode(PIN_LED_G, OUTPUT);
  pinMode(PIN_VALVE, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);

  digitalWrite(PIN_VALVE, LOW);  // Ensure valve closed
  digitalWrite(PIN_LED_G, HIGH); // Safe state
}

void loop() {
  bool armed = digitalRead(PIN_ARM);
  bool safe = !digitalRead(PIN_SAFE);  // Inverted
  bool trigger = digitalRead(PIN_TRIG);

  // Update LEDs
  if (armed && !safe) {
    digitalWrite(PIN_LED_R, HIGH);
    digitalWrite(PIN_LED_G, LOW);
  } else {
    digitalWrite(PIN_LED_R, LOW);
    digitalWrite(PIN_LED_G, HIGH);
  }

  // Fire logic: ARM=on, SAFETY=off, TRIGGER=pressed
  if (armed && !safe && trigger) {
    fire();
  }
}

void fire() {
  digitalWrite(PIN_VALVE, HIGH);
  delay(DWELL_MS);
  digitalWrite(PIN_VALVE, LOW);

  // Prevent rapid fire - wait for trigger release
  while(digitalRead(PIN_TRIG)) {
    delay(10);
  }
  delay(DEBOUNCE);
}
```

---

## 7. SAFETY WARNINGS

```
⚠️ SAFETY REQUIREMENTS FOR PROTOTYPE TESTING
═══════════════════════════════════════════════════════════════════════════

1. ALWAYS wear safety glasses during any pressurized testing
2. NEVER point at people, even with tennis ball projectiles
3. TEST outdoors or in adequately sized indoor space (>10m range)
4. ENSURE backstop can safely stop projectiles
5. VERIFY all fittings sealed before pressurizing
6. START with low pressure (30 bar), increase gradually
7. KEEP bystanders at minimum 5m distance during testing
8. STORE depressurized when not in use
9. INSPECT O-rings and seals before each session
10. DOCUMENT all tests for safety review

EMERGENCY: If leak detected, point muzzle safe direction,
           allow to depressurize naturally, then repair.

═══════════════════════════════════════════════════════════════════════════
```

---

## 8. DOCUMENT LINKS

- [[VN-CUA-001_product_spec|Product Specification]]
- [[VN-CUA-001_P3_embodiment_design|Phase 3 Embodiment Design]]
- [[VN-CUA-001_prototype_experiments|Experiment Procedures]] (to be created)

---

## 9. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial prototype BOM. 8 subsystems, ~$800 budget, 4-week procurement timeline.** |

---

*This BOM supports rapid prototyping to validate VDC-100 pneumatic concepts before detail design commitment.*
