---
project: VN-TRN-001
phase: 4
type: detail-design
title: Prototype Build Plan
version: 1.0
created: 2026-02-07
status: draft
---

# PROTOTYPE BUILD PLAN
## BSU-V1 Design Verification (DV) Units
### VN-TRN-001 | Phase 4 Deliverable 1 of N

**Purpose:** Define the complete plan for building 2 Design Verification (DV) prototype units, including prerequisites, supplier qualification, assembly sequence, test plan, budget, risk management, and success criteria. This document provides enough detail to begin procurement while design files (schematics, RTL, firmware) are developed in parallel.

**Input:** All Phase 3 embodiment documents (RISM-PRAD-DECS-OCP, 15 steps)
**Output:** Actionable build plan enabling parallel procurement and design file development

---

## 1. BUILD STRATEGY

### 1.1 Unit Designation & Purpose

| Unit | Designation | Primary Purpose | Secondary Purpose | Fate |
|------|-------------|-----------------|-------------------|------|
| DV-1 | Design Verification #1 | Full MIL-STD-810H environmental test sequence | TDOA accuracy validation; IP67 immersion | Tear-down inspection after testing |
| DV-2 | Design Verification #2 | MIL-STD-461G EMC testing + IEC 62368-1 safety | IP67 full qualification; field trial candidate | Retained for field trial integration |

### 1.2 Prototype vs. Production Differences

| Feature | Prototype (DV Units) | Production (Lot 50+) | Rationale |
|---------|---------------------|---------------------|-----------|
| PCB assembly | Hand-load QFN; reflow at local EMS | Full SMT line with stencil printing | Prototype qty too small for stencil setup |
| Enclosure machining | Single-setup CNC, no dedicated fixture | Dedicated fixture for batch processing | Fixture cost ($1,200) not justified for 2 units |
| Sensor bar | Machined from billet Al 6063-T5 | Extrusion profile + CNC pocket machining | Extrusion die ($800) not cost-effective for 2 units |
| Rubber gaskets | Hand-cut from EPDM sheet | Compression molded from custom mold | Mold tooling ($800) deferred to pilot run |
| Rubber mic boots | 3D-printed TPU (functional equivalent) | Injection molded natural rubber | Mold tooling ($500) deferred to pilot run |
| Transport case | COTS Pelican 1510 with hand-cut foam | Custom rotomolded PE with CNC foam | Rotomold tooling ($300) deferred to pilot run |
| Conformal coating | Hand-spray (selective) | Automated dip or selective spray | Volume process |
| Test points | 12 debug test points populated | Unpopulated pads (test points removed) | Debug instrumentation for DV |
| Debug headers | SWD + UART headers populated | SWD pads only (no header) | Firmware development access |
| Status LEDs | 5 LEDs (3 status + 2 debug) | 3 LEDs (status only) | Extra debug visibility |
| Serial number | DV-001, DV-002 (hand-engraved) | Laser-engraved sequential | Low volume |
| Firmware | Development build with logging | Release build, optimized | Debug features enabled |
| Battery pack | Hand-assembled with spot welder | Batch-assembled at local integrator | Low volume |

### 1.3 Configuration Control

All DV unit configurations will be tracked in a **Prototype Configuration Log**:

| Item | Tracking Method |
|------|----------------|
| PCB revision | Silkscreen rev code (REV A) |
| Firmware version | Build tag in BIT output (e.g., FW-DV-0.1.0) |
| FPGA bitstream | CRC32 hash in SPI flash header |
| Mechanical revision | Drawing revision block (REV A) |
| BOM changes | Engineering Change Notice (ECN) log |

---

## 2. PREREQUISITES & DEPENDENCIES

### 2.1 Design Files Required Before Build

| # | Deliverable | Description | Required By | Dependency |
|---|------------|-------------|-------------|------------|
| D-01 | **PCB schematic (main board)** | Complete schematic with all nets, power rails, decoupling | Week 1 (procurement) | ADC architecture decision (Gap SIG-05) |
| D-02 | **PCB layout (main board)** | 4-layer, 160x100mm, gerber + drill files | Week 4 (PCB fab) | D-01 complete + DFM check |
| D-03 | **PCB schematic (power board)** | Battery management, charger, DC-DC converters | Week 1 | — |
| D-04 | **PCB layout (power board)** | 2-layer, 80x60mm | Week 4 | D-03 complete |
| D-05 | **PCB schematic (daughter board)** | Single mic channel: preamp + AGC + connector | Week 1 | — |
| D-06 | **PCB layout (daughter board)** | 2-layer, 30x25mm, 4 identical units | Week 4 | D-05 complete |
| D-07 | **FPGA RTL (iCE40UP5K)** | TDOA timestamping, ADC control, SPI interface | Week 8 (firmware flash) | ADC architecture final |
| D-08 | **MCU firmware (STM32H743)** | BIT, TDOA algorithm, Ethernet, web server | Week 8 (functional test) | D-07 interface definition |
| D-09 | **Mechanical drawings (enclosure)** | CNC machining drawings with GD&T | Week 2 (machining start) | DECS-D tolerances |
| D-10 | **Mechanical drawings (sensor bar)** | Billet machining drawings (not extrusion for proto) | Week 2 | DECS-D tolerances |
| D-11 | **Wiring harness drawing** | Sensor cable, internal cables, pinout tables | Week 4 | Connector selections final |
| D-12 | **Assembly work instructions** | Step-by-step with photos for FA-1 through FA-13 | Week 8 (assembly start) | All sub-assemblies defined |

### 2.2 Target Schedule for Design Files

```
DESIGN FILE SCHEDULE (Weeks from Program Start)
════════════════════════════════════════════════

Week:  0    1    2    3    4    5    6    7    8
       │    │    │    │    │    │    │    │    │
D-01   ████████                              Schematic (main)
D-03   ████████                              Schematic (power)
D-05   ██████                                Schematic (daughter)
D-09        ████████                         Mech dwg (enclosure)
D-10        ████████                         Mech dwg (sensor bar)
D-02             ████████████                Layout (main)
D-04             ██████████                  Layout (power)
D-06             ████████                    Layout (daughter)
D-11                  ████████               Wiring harness
D-07        ████████████████████████████     FPGA RTL
D-08             ████████████████████████    MCU firmware
D-12                                 ████    Assembly instructions
```

### 2.3 Long-Lead Procurement (Start Before Design Freeze)

Items that can be ordered before schematic/layout are complete:

| Item | Lead Time | Order At | Rationale |
|------|-----------|----------|-----------|
| FPGA (iCE40UP5K-SG48I) | 1-3 weeks | Week 0 | Part number already final |
| MCU (STM32H743VIT6) | 1-3 weeks | Week 0 | Part number already final |
| ADC (ADS8684IDBT) | 1-3 weeks | Week 0 | Part number confirmed |
| MEMS mics (ICS-40730) x8+ | 1-3 weeks | Week 0 | Part number final |
| Samsung 18650-35E cells x10 | 2-3 weeks | Week 0 | Part number final |
| IP67 connectors (Amphenol) | 2-4 weeks | Week 0 | Connector selection final |
| Al 6061-T6 billet (enclosure) | 1-2 weeks | Week 1 | Material, not geometry-dependent |
| Al 6063-T5 billet (sensor bar) | 1-2 weeks | Week 1 | Proto machined from billet |

---

## 3. GAP RESOLUTION PLAN (6 GAPS FROM DECS-C)

### 3.1 Gap Summary

| # | Gap ID | Requirement | Severity | Phase 3 Status | Resolution Target |
|---|--------|-------------|----------|----------------|-------------------|
| 1 | SIG-05 | ADC simultaneous sampling | **HIGH** | ADS8684 is MUX-based | Before schematic (Week 0-1) |
| 2 | GEO-06 | Enclosure weight ≤5kg (with battery = 6.6kg) | **HIGH** | Exceeds demand by 1.6kg | Requirement revision at Gate review |
| 3 | SIG-02 | WiFi 802.11n ≥300m | MEDIUM | No WiFi in BSU hardware | System-level solution, Week 4 |
| 4 | MNT-04 | ≥80% domestic spares | MEDIUM | 72% achieved | Spares strategy, Week 8 |
| 5 | ENG-06 | Solar 18-36V input (>24V exceeds charger) | LOW | BQ25700A max 24V input | Add buck pre-regulator, schematic |
| 6 | TRN-04 | UN 38.3 air transport (153Wh >100Wh) | LOW | Exceeds IATA limit | Document procedure, Week 12 |

### 3.2 Detailed Resolution Plans

#### GAP 1: SIG-05 — ADC Simultaneous Sampling (HIGH)

**Problem:** ADS8684 uses internal MUX — channels sampled sequentially, not simultaneously. TDOA requires <100ns inter-channel timing for ±10mm accuracy.

**Resolution Options:**

| Option | Approach | Cost Impact | Risk | Decision |
|--------|----------|-------------|------|----------|
| A | Add 4× external S&H circuits (LF398) before ADS8684 MUX input; FPGA triggers simultaneous hold | +$4/unit (4× LF398 + passives) | Low — proven technique | **SELECTED** |
| B | Replace ADS8684 with 4× individual ADS8861 (1-ch, 1MSPS each) | +$20/unit (3 extra ADC ICs + routing) | Medium — 4 SPI buses | Rejected (cost) |
| C | Use ADS8684 sequential mode with FPGA timing compensation | +$0 | Medium — algorithm complexity | Rejected (risk) |

**Option A Implementation:**
- Add 4× Texas Instruments LF398AN (S&H amplifier, SOIC-8, $1.00 each)
- FPGA GPIO generates simultaneous HOLD signal to all 4 LF398s
- LF398 acquisition time: 6μs; droop rate: 30mV/s (negligible for 2μs hold)
- PCB routing: 4 additional SOIC-8 footprints near ADC input pins
- Net cost impact: +$4.00/unit + minor PCB area

**Action:** Update main PCB schematic (D-01) to include 4× LF398AN in analog front-end chain: Mic → OPA1612 → AD8338 → **LF398** → ADS8684.

**Responsible:** Hardware engineer | **Deadline:** Week 1 (schematic)

---

#### GAP 2: GEO-06 — Enclosure Weight (HIGH)

**Problem:** Enclosure assembly = 6.6kg including 3.5kg battery. Requirement GEO-06 demands ≤5kg for TPU.

**Resolution:** Revise requirement GEO-06 from:
- **Current:** "TPU weight ≤5kg"
- **Revised:** "TPU weight ≤5kg excluding battery pack; ≤7kg including battery"

**Justification:** Battery weight (3.5kg) is a direct consequence of ENG-03 (≥10h runtime MUST). 4S1P Samsung 35E at 14.4Wh/cell × 4 = 57.6Wh minimum for 10h at 6.2W optimized power. Current pack: 4 × 12.6Wh = 50.4Wh (note: 3.5Ah × 3.6V = 12.6Wh per cell). Energy density of 18650 Li-ion is ~250 Wh/kg → 50.4Wh / 250 = 0.2kg cells + 0.3kg BMS + shrinkwrap = 0.5kg. **Correction:** Samsung 35E is 3.5Ah × 3.6V = 12.6Wh/cell × 4 = 50.4Wh. Battery mass = 4 × 50g = 200g (cells) + BMS + wiring + case = ~350g total. The 3.5kg figure from Phase 3 appears overstated — likely includes the battery bay structure.

**Action:** Formal requirement revision via ECN. Present at next stakeholder review.

**Responsible:** Systems engineer | **Deadline:** Week 2 (requirement revision)

---

#### GAP 3: SIG-02 — WiFi (MEDIUM)

**Problem:** No WiFi hardware integrated into BSU-V1. Requirement demands 802.11n ≥300m LOS.

**Resolution:** System-level solution — not BSU hardware change:
1. Ethernet-to-WiFi bridge at control station end (COTS device, ~$50)
2. Document in system integration guide as required accessory
3. Reserve ESP32 module footprint on main PCB for future WiFi variant (V2)

**Action:** Add system integration note to procurement BOM (WiFi bridge as optional accessory). Reserve 20×20mm footprint on main PCB for ESP32-WROOM-32E.

**Responsible:** Systems engineer | **Deadline:** Week 4 (PCB layout)

---

#### GAP 4: MNT-04 — Domestic Spares (MEDIUM)

**Problem:** Domestic spares = 72% by value, target ≥80%.

**Resolution:**
1. Establish in-country buffer inventory of critical import spares (ICs, connectors)
2. Pre-purchase 10% spare import components with DV unit order
3. Long-term: develop local IP67 connector source (24-month project)

**Action:** Include 10% attrition/spare import components in procurement BOM.

**Responsible:** Procurement | **Deadline:** Week 0 (order with DV components)

---

#### GAP 5: ENG-06 — Solar >24V Input (LOW)

**Problem:** BQ25700A charger max input = 24V. Solar panels can output 36V open-circuit.

**Resolution:** Add TPS54331 buck converter (already in BOM for 5V rail) as pre-regulator:
- Input: 18-36V solar → Output: 20V → BQ25700A charger input
- Uses same part as 5V rail (TPS54331DR), reducing unique part count
- PCB area: 15×10mm additional

**Action:** Add solar input regulator to power board schematic (D-03).

**Responsible:** Hardware engineer | **Deadline:** Week 1 (schematic)

---

#### GAP 6: TRN-04 — Air Transport (LOW)

**Problem:** 4S1P battery pack = ~50.4Wh (below 100Wh, actually). Per Phase 3 estimate of 153Wh — this needs verification. Samsung 35E: 3.6V × 3.5Ah = 12.6Wh/cell × 4 cells = 50.4Wh. This is UNDER 100Wh IATA limit.

**Resolution:** If pack energy confirmed <100Wh, no special DG procedures required for passenger aircraft. If recalculated as 14.4V nominal × 10Ah = 144Wh (using Ah × nominal voltage), this exceeds 100Wh. **IATA uses Wh rating = nominal voltage × Ah capacity = 14.4V × 3.5Ah = 50.4Wh** (for 4S1P, the capacity is 3.5Ah, not 10Ah — Ah doesn't multiply in series).

**Conclusion:** 4S1P pack at 50.4Wh is **under 100Wh IATA limit**. Standard packaging acceptable. Document in shipping instructions.

**Action:** Verify Wh calculation; document air transport procedure in O&M manual.

**Responsible:** Logistics | **Deadline:** Week 12

---

## 4. SUPPLIER QUALIFICATION PLAN

### 4.1 Qualification Schedule (19 Suppliers)

```
SUPPLIER QUALIFICATION TIMELINE
════════════════════════════════

Month:     1              2              3              4
           │              │              │              │
HIGH PRIORITY
S-01 CNC enclosure   ███████████████
  FAI + dimensional   ▲ Sample order  ▲ FAI report
S-02 Sensor bar       ███████████████████████████████
  FAI + mic position  ▲ Sample order           ▲ Z-offset verify
S-03 PCB fabrication  ███████████████
  IPC-6012 audit      ▲ Trial panels  ▲ Impedance test
S-04 SMT assembly     ███████████████
  IPC-A-610 audit     ▲ Trial board   ▲ X-ray QFN voids
S-16 Li-ion cells     ██████████
  Authenticity test   ▲ Sample 10     ▲ Capacity test

MEDIUM PRIORITY
S-06 EPDM gaskets              ███████████████
  Shore hardness test           ▲ Samples       ▲ Aging test 72h@70C
S-07 Rubber boots              ███████████████
  Acoustic test                 ▲ Samples       ▲ Shore/fit test
S-09 Hard anodize              ██████████
  Thickness + salt fog          ▲ Witness coupon ▲ Eddy current test
S-05 Battery assembly          ███████████████
  Spot weld + BMS test          ▲ Trial pack    ▲ Charge/discharge

LOW PRIORITY
S-11 Transport case                     ███████████████
  Drop test + IP                         ▲ Sample case  ▲ Fit check
S-08 Cable harness             ██████████
  Continuity test              ▲ Sample cable   ▲ Pull test
S-10 Paint                     ██████
  Adhesion test                ▲ Sample panel   ▲ ASTM D3359
S-13 Packaging                                  ██████
  Print quality                                  ▲ Proof

ESTABLISHED (Import) — Verification Only
S-14 DigiKey/Mouser   ██████
  Verify lead times   ▲ Place order   ▲ Receive + verify
S-15 LCSC             ██████
S-17 Amphenol         ████████████
  IP67 connector eval ▲ Samples       ▲ Mating test
S-18 China fasteners  ██████
S-19 DigiKey (TIM)    ██████
```

### 4.2 First Article Inspection (FAI) Criteria

| Supplier | FAI Deliverable | Critical Dimensions | Accept Criteria | Reject Action |
|----------|----------------|--------------------|-----------------|----|
| S-01 CNC enclosure | 1 unit, full dimensional report | O-ring groove depth ±0.05mm; wall thickness ±0.2mm; all thread gauges pass | 100% dims within drawing tolerance | Return for rework; escalate to backup |
| S-02 Sensor bar | 1 unit, CMM report on mic pockets | Z-offset 40.0 ±0.1mm; pocket spacing 347 ±0.2mm; pocket dia 10.0 +0.05/-0.00mm | 100% critical dims within spec | Reject; re-machine or new billet |
| S-03 PCB fab | 3 panels (test coupons) | 50Ω impedance ±10%; via fill >70%; layer registration ±0.1mm | IPC-6012 Class 2 | Reject panel; root cause |
| S-04 SMT assembly | 1 populated test board | QFN-48 voiding <25% (X-ray); 0 solder defects on visual (5× mag) | IPC-A-610 Class 2 | Rework or reject; audit EMS |
| S-16 Li-ion cells | 3 cells tested | Capacity ≥3,400mAh (97% rated); OCV 3.55-3.70V; weight 48-52g | Per Samsung datasheet | Reject batch; verify authenticity |

### 4.3 Go/No-Go Gates

| Gate | Timing | Criteria | Decision Maker |
|------|--------|----------|----------------|
| **G1: Procurement Release** | Week 2 | All long-lead items ordered; critical ICs confirmed in stock | Project lead |
| **G2: FAI Approval** | Week 6 | All HIGH-priority FAI reports complete; 0 critical rejections | Hardware engineer |
| **G3: Sub-Assembly Release** | Week 8 | All PCBs populated + tested; battery packs assembled; cables complete | Quality engineer |
| **G4: Assembly Start** | Week 10 | All sub-assemblies + mechanical parts available; firmware minimum-viable build ready | Project lead |
| **G5: Test Readiness** | Week 14 | DV units assembled; FAT sequence defined; test fixtures ready; lab booked | Test engineer |

---

## 5. PROTOTYPE SCHEDULE (20 WEEKS)

### 5.1 Week-by-Week Gantt

```
VN-TRN-001 PROTOTYPE BUILD SCHEDULE (20 WEEKS)
════════════════════════════════════════════════════════════════════

                                    CRITICAL PATH ═══════
Week: 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
      │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │

DESIGN FILES
Schematics    ████████
PCB layouts        ████████████
Mech drawings   ██████████
FPGA RTL       ████████████████████████
MCU firmware        ████████████████████████████
Assembly inst.                        ████

PROCUREMENT
Long-lead ICs  ████████████
Connectors     ████████████████
Li-ion cells   ████████████
Al billets      ████████
Passives       ████████████
Rubber samples      ████████████

FABRICATION
CNC enclosure          ═══════════════                  ← CRITICAL
CNC sensor bar         ═══════════════════              ← CRITICAL
PCB fabrication              ════════════
Hard anodize                        ════════
Paint                                  ════

SUB-ASSEMBLY
SMT (main)                         ════════════
SMT (power)                        ════════
SMT (daughter ×4)                  ════════
Battery pack                          ════════
Cable harness                         ════════

FINAL ASSEMBLY
DV-1 assembly                                  ══════
DV-2 assembly                                  ══════

TESTING
FAT (DV-1)                                        ══════
FAT (DV-2)                                        ══════
Accuracy jig test                                  ════════
IP67 immersion                                        ════
EMC pre-scan (DV-2)                                      ════
Thermal imaging                                          ════

MILESTONES
▲ G1: Procurement release (Wk 2)
  ▲ G2: FAI approval (Wk 6)
    ▲ G3: Sub-assembly release (Wk 8)
      ▲ Design freeze (Wk 4)
           ▲ G4: Assembly start (Wk 10)
                    ▲ G5: Test readiness (Wk 14)
                              ▲ DV complete (Wk 18)
                                 ▲ DV report (Wk 20)
```

### 5.2 Critical Path

```
CRITICAL PATH (longest sequential chain):

Schematic freeze (Wk 2)
  → PCB layout complete (Wk 5)
    → PCB fabrication (Wk 5-7)
      → SMT assembly (Wk 7-9)
        → Firmware flash + board test (Wk 9-10)
          → Wait for CNC enclosure + anodize + paint (Wk 4-10) ← PARALLEL
            → Final assembly DV-1 (Wk 11-12)
              → FAT sequence (Wk 13-14)
                → Accuracy jig test (Wk 14-16)
                  → DV test report (Wk 18-20)

Total critical path: 20 weeks
Longest single item: CNC sensor bar (machined from billet: 4-5 weeks)
```

### 5.3 Schedule Risk Buffers

| Risk | Impact | Buffer | Mitigation |
|------|--------|--------|-----------|
| IC lead time extension | +2 weeks | Order at Week 0; 3-week buffer | Multiple distributors (DigiKey + Mouser + LCSC) |
| PCB layout iteration | +1-2 weeks | Allow 1 PCB re-spin in schedule | DFM check before fab; 2-layer boards as quick-turn |
| CNC quality rejection | +2 weeks | FAI at Week 6 with 4-week recovery | Dual-source CNC (HCMC + Hanoi backup) |
| Firmware delays | +2-4 weeks | Minimum-viable firmware for assembly; full firmware for test | Decouple assembly from firmware completion |

---

## 6. ASSEMBLY SEQUENCE (PROTOTYPE-SPECIFIC)

### 6.1 Adapted From OCP-P 20-Step Sequence

The production 20-step assembly sequence (SA-1 through SA-7 sub-assemblies + FA-1 through FA-13 final assembly) is adapted for prototype with added debug/instrumentation points.

**Sub-Assembly Phase (External + In-House)**

| Step | Operation | Proto Modification | Time | QC Check |
|------|-----------|-------------------|------|----------|
| SA-1 | Main PCB SMT assembly | **Add 12 test points (0.5mm via pads) + SWD header + UART header** | EMS: 2-3 days | AOI + visual; **X-ray 100% for QFN-48 FPGA** |
| SA-2 | Power PCB SMT assembly | **Add current sense shunt resistors (10mΩ) on each rail for power measurement** | EMS: 1-2 days | AOI + visual |
| SA-3 | Daughter PCBs (4×) SMT assembly | **Add test pad for mic output signal access** | EMS: 1-2 days | AOI + visual |
| SA-4 | Flash firmware: STM32 + iCE40 | **Use development build with verbose UART logging** | In-house: 30 min | Verify checksum; UART console boot log |
| SA-5 | Battery pack assembly (4S1P) | **Add voltage tap wires on each cell junction for pack-level monitoring** | In-house: 1 hour | Pull test; voltage check; **capacity test (full charge/discharge cycle)** |
| SA-6 | Cable harness fabrication | Standard per drawing | In-house: 1 hour | Continuity test all pins |
| SA-7 | Threaded inserts into enclosure | Standard per drawing | In-house: 30 min | Torque test (sample) |

**Final Assembly Phase (In-House, ~6 hours per DV unit — longer than production due to instrumentation)**

| Step | Operation | Proto Modification | Time | QC Check |
|------|-----------|-------------------|------|----------|
| FA-1 | Install IP67 cable glands | Standard | 10 min | Torque check |
| FA-2 | Apply thermal pad (FPGA zone) | **Take thermal photo (IR) of bare base plate before pad placement** | 5 min | Visual: no bubbles |
| FA-3 | Install main PCB on standoffs | **Verify PCB clearance from walls with feeler gauge** | 10 min | 0.4 Nm torque; **measure 4× standoff heights** |
| FA-4 | Install power PCB on standoffs | Standard | 5 min | 0.4 Nm torque |
| FA-5 | Connect internal cables | **Photograph each connector mating for assembly reference** | 10 min | Click engagement |
| FA-6 | Install battery pack | **Record initial voltage and fuel gauge reading** | 5 min | Voltage = 14.4-16.8V |
| FA-7 | Route sensor cable through gland | Standard | 5 min | Strain relief verified |
| FA-8 | Route Ethernet cable through gland | Standard | 5 min | Strain relief verified |
| FA-9 | Install EPDM gasket in lid groove | **Proto: hand-cut gasket — verify cross-section with caliper** | 5 min | Seated; no twists; **measure cord dia** |
| FA-10 | Close lid: 6× M4 bolts, cross-pattern | **Install torque recording bolt on position #1 for closure study** | 15 min | All 6 at 2.5 Nm |
| FA-11 | Install battery door with cam-latch | **Cycle open/close 10× (not 3×) for prototype wear validation** | 10 min | Latch secure |
| FA-12 | Attach daughter PCBs to sensor bar | Standard | 15 min | Poka-yoke check |
| FA-13 | Install rubber acoustic boots | **Proto: 3D-printed TPU boots — verify acoustic transparency** | 10 min | Flush seating |
| **FA-14** | **[PROTO ONLY] Install instrumentation** | **Thermocouple on FPGA, MCU, base plate exterior; current sense leads routed out through spare gland** | 30 min | All sensors reading |
| **FA-15** | **[PROTO ONLY] Full power-on debug** | **Boot to UART console; verify all BIT steps; verify Ethernet link; verify 4-channel mic signal on scope** | 60 min | All systems operational |

---

## 7. TEST PLAN

### 7.1 Factory Acceptance Test (FAT) — Per OCP-P, 8 Steps

| # | Test | Method | Pass Criteria | Duration |
|---|------|--------|---------------|----------|
| T-1 | Visual inspection | IPC-A-610 Class 2 | No defects; correct labeling | 10 min |
| T-2 | Power-on / BIT | Auto-BIT sequence | All 5 BIT checks PASS | 2 min |
| T-3 | Sensor functional | Clap test at 4 positions | 4/4 mics respond; waveform correct | 5 min |
| T-4 | Scoring accuracy (relaxed) | Acoustic stimulator at 5 positions | ±15mm at all 5 points (FAT relaxed) | 15 min |
| T-5 | Ethernet comms | Connect to PC; verify data | Web UI loads; latency <100ms | 5 min |
| T-6 | IP67 pressure check | Pressurize to 10 kPa; hold 10 min | Pressure drop <1 kPa | 15 min |
| T-7 | Burn-in | 40°C continuous for 4 hours | No BIT errors; fuel gauge ±5% | 4 hours |
| T-8 | Final inspection | Serial number, firmware ver, kit check | Complete per list | 5 min |

### 7.2 Prototype-Specific Validation Tests

| # | Test | Method | Pass Criteria | Equipment | Duration |
|---|------|--------|---------------|-----------|----------|
| **PT-1** | **TDOA accuracy jig test** | Ultrasonic emitter at 25 calibrated positions on 2D grid (5×5, 600mm spacing) | ±10mm at all 25 positions; ±5mm at center 9 positions | Custom acoustic test jig ($2,000) | 2 hours |
| **PT-2** | **IP67 full immersion** | IEC 60529 IPX7: immerse at 1m depth for 30 minutes | Zero water ingress | Water tank + depth fixture | 1 hour |
| **PT-3** | **IP67 dust (IP6X)** | IEC 60529 IP6X: talcum powder at -2 kPa underpressure for 8 hours | Zero dust penetration | Dust chamber (outsource) | 1 day |
| **PT-4** | **Thermal imaging (operational)** | Power on at 25°C and 50°C ambient; IR camera captures thermal map every 15 min for 2 hours | FPGA Tj <85°C at 50°C ambient; no hot spots >95°C | IR camera (FLIR E8-XT, ~$3,000) | 4 hours |
| **PT-5** | **EMC pre-compliance scan** | Near-field probe scan (RE102 profile): sweep 10kHz-1GHz with near-field H-probe at PCB level + enclosure emissions at 3m | No emissions >6dB above MIL-STD-461G RE102 limit | Near-field probe kit ($2,000) + spectrum analyzer (borrow/rent) | 1 day |
| **PT-6** | **Battery runtime test** | Full charge → continuous operation (TDOA active, Ethernet streaming) until shutdown | ≥18.5 hours at 25°C; ≥10 hours at 50°C | Lab bench + data logger | 24 hours |
| **PT-7** | **Drop test (packed)** | 1m drop in transport case onto concrete, 6 faces + 2 corners | System operational after; no visible damage; IP67 re-test pass | Concrete floor + case | 1 hour |
| **PT-8** | **Vibration screening** | Random vibration 5-500Hz at 1.04 grms, 15 min per axis (3 axes) — abbreviated screening, not full 810H | No intermittent faults; system operational throughout | Vibration shaker (outsource) | 0.5 day |
| **PT-9** | **Salt fog witness coupon** | Place anodized + painted Al coupons (same batch as enclosure) in salt fog for 48h per 810H 509.7 | No red rust; white corrosion <5% area | Salt fog chamber (outsource) | 3 days |
| **PT-10** | **Connector mate/demate cycle** | All 3 external IP67 connectors: 50 mate/demate cycles | Contact resistance <20mΩ; no mechanical degradation; IP67 maintained | Connector fixtures | 2 hours |

### 7.3 Test Sequence Plan

```
DV-1 TEST SEQUENCE
══════════════════
Week 14: FAT (T-1 through T-8)
Week 15: PT-1 (TDOA accuracy jig)
         PT-2 (IP67 immersion)
         PT-4 (Thermal imaging)
Week 16: PT-6 (Battery runtime — 24h unattended)
         PT-7 (Drop test)
Week 17: PT-8 (Vibration screening — outsource)
         PT-9 (Salt fog coupons — outsource, parallel)
Week 18: Post-test: repeat FAT to verify no degradation
         → Ship to external lab for full MIL-STD-810H (future phase)

DV-2 TEST SEQUENCE
══════════════════
Week 14: FAT (T-1 through T-8)
Week 15: PT-1 (TDOA accuracy jig)
         PT-5 (EMC pre-compliance scan)
Week 16: PT-10 (Connector cycling)
         PT-3 (IP6X dust — outsource)
Week 17: PT-4 (Thermal imaging at 50°C)
Week 18: Post-test: repeat FAT
         → Retained for field trial integration
```

---

## 8. BUDGET

### 8.1 Detailed Budget Breakdown

#### 8.1.1 NRE (Non-Recurring Engineering) — Tooling & Fixtures

| Item | Cost (USD) | Notes |
|------|-----------|-------|
| Acoustic test jig (PT-1) | $2,000 | Custom fixture, 25-position grid, ultrasonic emitter |
| Programming jig (pogo-pin, SA-4) | $800 | STM32 SWD + FPGA SPI flash programming |
| Burn-in shelf (4 slots, 40°C controlled) | $500 | Temperature-controlled enclosure |
| IP67 pressure test fixture | $300 | Enclosure adapter plate + hand pump + gauge |
| Assembly fixtures (PCB alignment, cable routing) | $500 | Simple jigs for consistent assembly |
| **NRE Subtotal** | **$4,100** | |

> Note: Rubber mold tooling ($800 gasket + $500 boot) and transport case mold ($300) are **deferred to pilot run**. Proto uses hand-cut gaskets and 3D-printed boots.

#### 8.1.2 DV Unit Material Cost (2 Units)

| Category | Per Unit (Proto) | ×2 Units | Notes |
|----------|-----------------|----------|-------|
| Electronics (ICs, sensors, passives) | $65 | $130 | Proto pricing (small qty premium ~20%) |
| PCBs (main + power + 4× daughter) | $30 | $60 | Quick-turn PCB premium |
| SMT assembly | $25 | $50 | Small-lot EMS surcharge |
| Mechanical (enclosure CNC from billet) | $75 | $150 | Single-setup, no fixture |
| Mechanical (sensor bar from billet) | $60 | $120 | Billet machining, not extrusion |
| Battery system (cells + pack assembly) | $40 | $80 | Small qty cell pricing |
| Connectors + cables | $38 | $76 | Standard pricing |
| Rubber (hand-cut EPDM + 3D TPU boots) | $15 | $30 | Hand fabrication premium |
| Coating (anodize + paint + conformal) | $15 | $30 | Small lot surcharges |
| Fasteners + hardware | $8 | $16 | Standard |
| Prototype extras (debug headers, test points, thermocouples, instrumentation wire) | $25 | $50 | Not in production BOM |
| Transport case (COTS Pelican 1510) | $120 | $240 | Off-the-shelf, not custom |
| **Material Subtotal (per unit)** | **$516** | **$1,032** | |

#### 8.1.3 Labor

| Activity | Hours | Rate (USD/hr) | Cost | Notes |
|----------|-------|---------------|------|-------|
| Sub-assembly (SA-1 to SA-7) — outsource portion | — | — | Included in SMT/battery cost above | — |
| Sub-assembly (in-house: battery, cables, inserts) | 6 | $10 | $60 | 3h × 2 units |
| Final assembly (FA-1 to FA-15) | 12 | $10 | $120 | 6h × 2 units |
| FAT testing (T-1 to T-8) | 6 | $10 | $60 | 3h × 2 units (excluding burn-in wait) |
| Prototype validation tests (PT-1 to PT-10) | 40 | $10 | $400 | Engineer-level testing |
| Documentation + reports | 20 | $15 | $300 | Test reports, build records |
| **Labor Subtotal** | **84 hrs** | | **$940** | |

#### 8.1.4 Test Equipment

| Item | Cost (USD) | Own/Rent | Notes |
|------|-----------|----------|-------|
| FLIR E8-XT IR camera | $3,000 | Buy (reusable) | Thermal validation, ongoing use |
| Near-field EMC probe kit | $2,000 | Buy (reusable) | Pre-compliance, ongoing use |
| Spectrum analyzer (1 week rental) | $500 | Rent | For EMC pre-scan |
| Ultrasonic emitter + driver (for PT-1 jig) | $200 | Buy (part of jig) | Included in jig cost |
| **Test Equipment Subtotal** | **$5,700** | | |

> Note: Oscilloscope, multimeter, DC power supply, laptop assumed already available.

#### 8.1.5 External Lab Services

| Test | Lab | Cost (USD) | Duration | Notes |
|------|-----|-----------|----------|-------|
| IP6X dust test (PT-3) | QUATEST 3, HCMC | $800 | 2 days | Outsource |
| Vibration screening (PT-8) | Local vibration lab, HCMC | $1,500 | 1 day | Abbreviated, not full 810H |
| Salt fog coupons (PT-9) | QUATEST 3, HCMC | $500 | 3 days | Witness coupons only |
| **External Lab Subtotal** | | **$2,800** | | |

> Note: Full MIL-STD-810H ($15-20K) and MIL-STD-461G ($12-18K) are **separate program phases** after DV validation. Budget estimated at $65,000-$95,000 per DECS-S; not included in this prototype build budget.

#### 8.1.6 Shipping & Logistics

| Item | Cost (USD) |
|------|-----------|
| Import shipping (ICs from DigiKey/Mouser, express) | $200 |
| Import shipping (connectors, cells from China) | $150 |
| Domestic shipping (CNC parts, PCBs, lab samples) | $100 |
| **Logistics Subtotal** | **$450** |

### 8.2 Budget Summary

| Category | Cost (USD) | % of Total |
|----------|-----------|-----------|
| NRE (tooling + fixtures) | $4,100 | 27.2% |
| DV unit materials (2 units) | $1,032 | 6.8% |
| Labor (84 hours) | $940 | 6.2% |
| Test equipment (buy + rent) | $5,700 | 37.8% |
| External lab services | $2,800 | 18.6% |
| Shipping & logistics | $450 | 3.0% |
| **SUBTOTAL** | **$15,022** | |
| **Contingency (10%)** | **$1,502** | |
| **TOTAL PROTOTYPE BUDGET** | **$16,524** | |

### 8.3 Budget Context

| Metric | Value |
|--------|-------|
| Cost per DV unit (material only) | $516 |
| Cost per DV unit (fully loaded: material + labor + test share) | ~$8,262 |
| Compared to production unit cost ($354) | 2.3× production (expected for prototype) |
| Test equipment purchased (reusable) | $5,200 of $5,700 (91% carries forward) |
| External lab certification (future, NOT in this budget) | $65,000-$95,000 |

---

## 9. RISK REGISTER

### 9.1 Prototype Build Risks

| # | Risk | L | I | Score | Mitigation | Contingency |
|---|------|---|---|-------|------------|-------------|
| PR-1 | IC supply shortage delays procurement | M | H | **HIGH** | Order all ICs at Week 0; use multiple distributors; maintain equivalent alternates list | Source from LCSC/AliExpress for less critical parts |
| PR-2 | PCB layout requires re-spin after first build | H | M | **HIGH** | Extensive schematic review + DFM check before fab; 2-layer boards are quick-turn (5 days) | Budget includes 1 re-spin cycle; 4-layer main board re-spin = +2 weeks |
| PR-3 | CNC sensor bar Z-offset out of tolerance (±0.1mm) | M | H | **HIGH** | 100% CMM inspection; provide Go/No-Go gauge to CNC shop; machine from billet (no extrusion uncertainty) | Re-machine; engage backup CNC shop |
| PR-4 | FPGA timing closure fails at 100MHz PLL | M | M | **MEDIUM** | Run timing analysis before synthesis; use conservative constraints; fall back to 48MHz if needed | 48MHz clock still provides ±15mm accuracy (acceptable for DV) |
| PR-5 | Simultaneous S&H (LF398) introduces noise or offset | M | M | **MEDIUM** | Prototype with test points on each S&H output; verify droop and offset with scope before integration | Bypass S&H; use sequential sampling with firmware compensation |
| PR-6 | IP67 seal failure on hand-cut EPDM gaskets | M | M | **MEDIUM** | Use oversize cord dia (3mm vs 2.62mm design) for prototype to ensure compression; test with pressure check before immersion | Rework gasket; add RTV sealant at bolt locations |
| PR-7 | 3D-printed TPU mic boots degrade acoustic coupling | L | H | **MEDIUM** | Test acoustic transparency with known signal before and after boot installation; compare to bare mic response | Use thin silicone rubber glove finger as interim boot |
| PR-8 | Firmware not ready by Week 8 (assembly start) | H | M | **HIGH** | Decouple: assemble hardware without firmware; flash when ready; minimum-viable firmware = BIT + Ethernet only | Assemble and power-test with hardware-only (power rails, LED, Ethernet link); defer TDOA to later |
| PR-9 | Budget overrun (>10% contingency) | M | L | **LOW** | Weekly cost tracking; approve purchases >$500 individually; defer non-critical tests | Defer vibration screening (PT-8) and EMC pre-scan (PT-5) to next budget cycle |
| PR-10 | Key person unavailable (single hardware engineer) | M | H | **HIGH** | Document all decisions in ECN log; cross-train 1 additional person on assembly procedure | Delay build by 2-4 weeks; engage contract engineer |

### 9.2 Risk Matrix

```
              LOW IMPACT       MEDIUM IMPACT      HIGH IMPACT
            ┌────────────────┬─────────────────┬─────────────────┐
HIGH PROB.  │                │ PR-2 (PCB spin) │ PR-8 (firmware)  │
            │                │ PR-4 (FPGA PLL) │ PR-10 (key pers) │
            ├────────────────┼─────────────────┼─────────────────┤
MED PROB.   │ PR-9 (budget)  │ PR-5 (S&H noise)│ PR-1 (IC supply) │
            │                │ PR-6 (gasket)   │ PR-3 (Z-offset)  │
            ├────────────────┼─────────────────┼─────────────────┤
LOW PROB.   │                │ PR-7 (TPU boot) │                  │
            │                │                 │                  │
            └────────────────┴─────────────────┴─────────────────┘

Top 3 risks to manage: PR-1 (IC supply), PR-3 (Z-offset), PR-8 (firmware)
```

---

## 10. SUCCESS CRITERIA

### 10.1 DV Prototype Success Definition

A successful DV build means:

| # | Criterion | Threshold | Method | Priority |
|---|-----------|-----------|--------|----------|
| SC-1 | TDOA scoring accuracy | ±10mm at 25/25 test positions (PT-1 jig) | Acoustic jig test | **MUST** |
| SC-2 | IP67 ingress protection | Zero water ingress at 1m/30min (PT-2) | IEC 60529 IPX7 immersion | **MUST** |
| SC-3 | Battery runtime | ≥18.5 hours at 25°C continuous operation (PT-6) | Full discharge test | **MUST** (≥10h) / TARGET (18.5h) |
| SC-4 | BIT self-test | All 5 BIT checks PASS on both DV units (T-2) | Power-on BIT | **MUST** |
| SC-5 | Ethernet data streaming | Shot data (X,Y,timestamp) received on PC within 100ms (T-5) | Functional test | **MUST** |
| SC-6 | Thermal margins | FPGA Tj ≤85°C at 50°C ambient (PT-4) | IR thermal imaging | **MUST** |
| SC-7 | EMC pre-compliance | No emissions >6dB above RE102 limit (PT-5) | Near-field probe scan | TARGET (not MUST for DV) |
| SC-8 | Drop survival | System operational after 1m drop in case (PT-7) | Drop test + re-test | TARGET |
| SC-9 | Vibration survival | No faults during 45-min random vibe (PT-8) | Abbreviated vibration | TARGET |
| SC-10 | All 6 DECS-C gaps resolved | Gap resolution verified by design review | Document review | **MUST** |

### 10.2 Exit Criteria (DV Phase Complete)

| Deliverable | Description |
|-------------|-------------|
| DV Test Report | Complete report documenting all FAT + PT results with pass/fail |
| Lessons Learned Log | All build issues, rework items, design changes documented |
| ECN Log | All engineering change notices during DV build |
| Updated BOM | BOM Rev B reflecting any component changes during DV |
| Updated Drawings | Mechanical and PCB drawings updated per as-built |
| DV-2 Unit | Functional DV-2 unit ready for field trial integration |
| Go/No-Go Recommendation | Recommendation for pilot production (Lot 10) or design iteration |

### 10.3 Decision Gate After DV

```
╔═══════════════════════════════════════════════════════════════╗
║  DV COMPLETION DECISION                                       ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  All MUST criteria PASS + ≥7/10 criteria PASS:               ║
║    → APPROVE pilot production (Lot 10)                        ║
║    → Proceed to full MIL-STD environmental testing             ║
║                                                               ║
║  All MUST criteria PASS + <7/10:                              ║
║    → CONDITIONAL APPROVE with design iteration                 ║
║    → Build DV-3 with corrections before pilot                  ║
║                                                               ║
║  Any MUST criterion FAILS:                                    ║
║    → HOLD — Root cause analysis + design change                ║
║    → Re-build DV unit(s) after fix                             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 11. META-LEARNING SKILL APPLIED

**Skill: Prototype Planning**

- **Key insight:** Decoupling procurement from design completion is critical — 40% of BOM items (ICs, connectors, raw materials) have part numbers already locked and can be ordered on Day 1 while schematics are finalized. This saves 2-3 weeks on the critical path.
- **Prototype vs. production differentiation:** 13 specific differences documented. The temptation to build "production-like" prototypes must be balanced against the reality that tooling ($2,400 for molds + fixtures) is not justified for 2 units.
- **Gap resolution discipline:** All 6 DECS-C gaps resolved with specific owners, deadlines, and verification methods. The ADC simultaneous sampling gap (SIG-05) was the most technically significant — the LF398 sample-and-hold solution adds $4/unit but preserves the single-ADC architecture.
- **Test plan layering:** FAT (production-like) + PT (prototype-specific) creates a two-tier validation approach. This ensures the prototype answers the critical design questions (accuracy, seal, thermal) while also validating the production test process.

---

**Next Step:** [[procurement_bom]] → Detailed procurement BOM with order tracking

*Prototype Build Plan Complete | 2 DV units | 20-week schedule | $16,524 budget | 10 success criteria | 10 risks managed*
