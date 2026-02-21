---
project: VN-CUA-001
designation: VDC-100
type: scale_up_production
phase: 4
version: 2.0
created: 2026-02-08
status: pending_prototype_data
methodology: Pahl & Beitz Phase 4 - Detail Design
production_target: "$1,700/unit"
local_content_target: "61% current, 78% roadmap"
---

# PHASE 4 — SCALE-UP & PRODUCTION DESIGN
## VDC-100 Full-Scale Production Documentation

**Project:** VN-CUA-001 (VDC-100 Vietnamese Drone Catcher)
**Status:** Awaiting VDC-33 prototype test data before finalizing
**Phase 3 Input:** [[03_embodiment/OCP_optimization_production|Gate 3 (15/15 PASSED)]]
**Prototype Input:** [[04_detail/experiment_procedures|VDC-33 Experiments]]

---

# 1. SCALING LAWS

## 1.1 Dimensional Scaling

| Parameter | Scaling Law | VDC-33 → VDC-100 | Multiplier | Notes |
|-----------|-------------|-------------------|------------|-------|
| Bore diameter | Linear (L) | 32mm → 100mm | x3.1 | Defines scale |
| Barrel length | Linear (L) | 260mm → 800mm | x3.1 | Maintains L/D ratio |
| Bore area | L^2 | 804 → 7,854 mm^2 | x9.77 | Affects force on projectile |
| Barrel volume | L^3 | ~210 → 6,280 cm^3 | x30 | Affects gas requirement |
| Projectile mass | Designed | 58g → 450g | x7.8 | Heavier for net payload |
| System mass | Designed | ~2.5 kg → ≤8 kg | x3.2 | Structural scaling |

## 1.2 Performance Scaling

| Parameter | Scaling Law | VDC-33 | VDC-100 Predicted | Requirement |
|-----------|-------------|--------|-------------------|-------------|
| Muzzle velocity | ~sqrt(P/rho) | 30-40 m/s | 35-45 m/s | 35-45 m/s |
| Operating pressure | Same | 60-100 bar | 100 bar | 100 bar max |
| Kinetic energy | 0.5*m*v^2 | ~35 J | ~360 J | — |
| Recoil impulse | m*v | ~2 Ns | ~18 Ns | ≤15 Ns |
| Gas per shot | ~A*L | ~2 bar drop | ~20 bar drop | — |
| Shots per fill | P_range/gas_per_shot | ~60 | ~9 | ≥5 |

**Critical scaling concern:** Recoil impulse scales with projectile momentum.
- VDC-33: 0.058 kg * 35 m/s = 2.0 Ns (comfortable)
- VDC-100: 0.45 kg * 40 m/s = 18 Ns (exceeds 15 Ns requirement)
- **Mitigation:** Recoil buffer in stock, muzzle brake, or reduce velocity to 33 m/s (impulse = 14.9 Ns)

## 1.3 Scale-Up Calculation Template

*To be completed after VDC-33 testing:*

| Parameter | VDC-33 Measured | Scale Factor | VDC-100 Predicted | Requirement | Status |
|-----------|-----------------|--------------|-------------------|-------------|--------|
| Muzzle velocity @ ___ bar | ___ m/s | ~1.0x | ___ m/s | 35-45 m/s | |
| Optimal pressure | ___ bar | 1.0x | ___ bar | ≤100 bar | |
| Optimal dwell | ___ ms | ~1.5x | ___ ms | TBD | |
| Shots per fill | ___ shots | /~3x | ___ shots | ≥5 | |
| Recoil impulse | ___ Ns | x7.8 | ___ Ns | ≤15 Ns | |
| Best fin config | Set ___ | — | Scale geometry | Stable flight | |

---

# 2. VDC-100 PRODUCTION DRAWINGS

## 2.1 Drawing Package Index

| Dwg # | Title | Status | Notes |
|-------|-------|--------|-------|
| VDC100-001 | System Assembly | PENDING | After prototype validation |
| VDC100-002 | Barrel Assembly | PENDING | Al 6061-T6, 100mm bore |
| VDC100-003 | Receiver Assembly | PENDING | Al 6061-T6 or PA66-GF30 |
| VDC100-004 | Gas System Assembly | PENDING | HPA + regulator + valve |
| VDC100-005 | Stock Assembly | PENDING | PA66-GF30, adjustable |
| VDC100-006 | Trigger Mechanism | PENDING | Electronic trigger |
| VDC100-007 | Scope Mount | PENDING | MIL-STD-1913 rail |
| VDC100-010 | VDC-P40E Projectile | PENDING | Net + parachute |
| VDC100-011 | Net Assembly | PENDING | UHMWPE, 3m x 3m |
| VDC100-012 | Parachute Assembly | PENDING | Ripstop nylon, 0.8m |

## 2.2 Key Assembly Drawing (Preliminary)

```
VDC-100 SYSTEM ASSEMBLY — SIDE VIEW
═══════════════════════════════════════════════════════════════════════════════

                     SCOPE (MIL-STD-1913)
                         +--------+
                         | LRF +  |
                         |RETICLE |
                         +---+----+
                             |
    MUZZLE                   | RAIL
    +---+  +─────────────────+────────────────────────+
    |   |  |                 BARREL                     |
    | O |==| ======================================== |=== 100mm bore
    |   |  |              Al 6061-T6                    |      800mm
    +---+  +─────────────────+────────────────────────+
                             |
                    +--------+--------+
                    |    RECEIVER     |
                    |  (Al or PA66)   |
                    +--+----+----+---+
                       |    |    |
              +--------+  +-+-+  +--------+
              | GRIP   |  |TRG|  | GAS    |
              |(PA66)  |  |   |  | SYSTEM |
              +--------+  +---+  +---+----+
                                     |
                              +------+------+
                              | SOLENOID    |
                              | VALVE       |
                              +------+------+
                                     |
                              +------+------+
                              | REGULATOR   |
                              | 300→100 bar |
                              +------+------+
                                     |
                              +------+------+
                              | HPA CYLINDER|
                              | 0.5L 300bar |
                              +------+------+
                                     |
                              +------+------+
                              |   STOCK     |
                              | (Adjustable)|
                              |  + RECOIL   |
                              |    PAD      |
                              +-------------+

    OVERALL: ~1100mm length, ≤8 kg loaded

═══════════════════════════════════════════════════════════════════════════════
```

## 2.3 Critical Interface Dimensions

| Interface | Dimension | Tolerance | Standard |
|-----------|-----------|-----------|----------|
| Barrel bore | 100mm ID | H7 (+0.035/0) | — |
| Barrel OD | 110mm | h9 (-0.087/0) | — |
| Projectile fit | 98mm OD | ±0.5mm | Clearance 2mm |
| Scope rail | 21mm slot | ±0.1mm | MIL-STD-1913 |
| Stock interface | M8 x 2 holes | ±0.1mm | — |
| Gas thread | G1/4 BSP | Per standard | ISO 228-1 |
| Cylinder thread | M18x1.5 | Per standard | DIN 477 |
| Trigger pull | 20-40N | ±5N | CUA-FOR-01 |

---

# 3. FINAL BILL OF MATERIALS (VDC-100)

## 3.1 Production BOM (from Phase 3 OCP optimization)

### Launcher Assembly — $1,192

| # | Component | Material | Process | Qty | Unit Cost | Total | Source |
|---|-----------|----------|---------|-----|-----------|-------|--------|
| 1 | Barrel tube | Al 6061-T6 | CNC turn + bore | 1 | $85 | $85 | Local CNC |
| 2 | Barrel liner (optional) | SS 304 | Honed tube | 1 | $45 | $45 | Import |
| 3 | Receiver body | Al 6061-T6 | CNC mill | 1 | $120 | $120 | Local CNC |
| 4 | Receiver cover | Al 6061-T6 | CNC mill | 1 | $40 | $40 | Local CNC |
| 5 | Stock body | PA66-GF30 | Injection mold | 1 | $25 | $25 | Local mold |
| 6 | Stock pad | Rubber | Molded | 1 | $8 | $8 | Local |
| 7 | Grip | PA66-GF30 | Injection mold | 1 | $15 | $15 | Local mold |
| 8 | Trigger assembly | Mixed | Machined + assembled | 1 | $35 | $35 | Local |
| 9 | Safety mechanism | SS 17-4 PH | CNC + heat treat | 1 | $25 | $25 | Local CNC |
| 10 | HPA cylinder | Al/CF | Purchased | 1 | $120 | $120 | Import |
| 11 | Regulator | Brass/SS | Purchased (Ninja/equiv) | 1 | $85 | $85 | Import |
| 12 | Solenoid valve | Mixed | Purchased (PE/equiv) | 1 | $65 | $65 | Import |
| 13 | Pressure gauge | SS | Purchased | 1 | $15 | $15 | Import |
| 14 | Scope mount rail | Al 6061-T6 | CNC mill | 1 | $20 | $20 | Local CNC |
| 15 | LRF module | COTS | Purchased | 1 | $200 | $200 | Import |
| 16 | Electronics PCB | FR4 | Assembled | 1 | $35 | $35 | Local |
| 17 | Battery (Li-ion) | 18650 cells | Purchased | 1 | $20 | $20 | Import |
| 18 | Pneumatic fittings | Brass | Purchased | 1 set | $30 | $30 | Local |
| 19 | Seals & O-rings | NBR/FKM | Purchased | 1 set | $15 | $15 | Local |
| 20 | Fasteners | SS A2/A4 | Purchased | 1 set | $25 | $25 | Local |
| 21 | Sling & mounts | Nylon/SS | Purchased | 1 | $12 | $12 | Local |
| 22 | Carry case | HDPE | Blow mold | 1 | $45 | $45 | Local |
| 23 | Misc (wire, labels) | Various | — | 1 set | $12 | $12 | Local |
| | | | | | **Subtotal** | **$1,117** | |
| | Assembly labor | — | 2 hrs @ $15/hr | — | $30 | $30 | Local |
| | QC/Test | — | 1 hr @ $25/hr | — | $25 | $25 | Local |
| | Packaging | — | — | — | $20 | $20 | Local |
| | | | | | **Launcher Total** | **$1,192** | |

### Projectile Pack (5x VDC-P40E) — $301

| # | Component | Material | Process | Qty | Unit Cost | Total |
|---|-----------|----------|---------|-----|-----------|-------|
| 1 | Projectile body | Al/PA66 | CNC/mold | 5 | $15 | $75 |
| 2 | Net (UHMWPE 3x3m) | UHMWPE | Knotted | 5 | $18 | $90 |
| 3 | Corner weights | SS 304 | CNC turn | 20 | $2 | $40 |
| 4 | Parachute (0.8m) | Ripstop nylon | Sewn | 5 | $10 | $50 |
| 5 | Timer/deploy mech | Electronic | PCB + assembly | 5 | $8 | $40 |
| 6 | Fin assembly | PA66-GF30 | Injection mold | 5 | $5 | $25 |
| | Assembly labor | — | 0.5 hr each | 5 | | |
| | | | | | **Subtotal** | **$320** |
| | *Price per projectile* | | | | *$64* | |

### Accessories — $60

| Item | Cost |
|------|------|
| Cleaning kit | $15 |
| Spare O-ring set | $10 |
| User manual (printed) | $5 |
| Training projectiles (2x inert) | $20 |
| Hex key set | $10 |
| **Subtotal** | **$60** |

## 3.2 Unit Cost Summary

| Category | Cost | % |
|----------|------|---|
| Launcher assembly | $1,192 | 70.1% |
| Projectile pack (5x) | $320 | 18.8% |
| Accessories | $60 | 3.5% |
| Overhead (7.5%) | $118 | 6.9% |
| Warranty reserve (2%) | $34 | 2.0% |
| **Unit Production Cost** | **$1,700** | **100%** |
| | | |
| **Selling Price** | **$5,400** | |
| **Gross Margin** | **$3,700 (68.5%)** | |

## 3.3 Local Content Analysis

| Source | Cost | % of Total |
|--------|------|------------|
| **Local manufacture** (CNC, mold, assembly) | $530 | 31.2% |
| **Local purchase** (fittings, seals, hardware) | $175 | 10.3% |
| **Local labor** (assembly, QC, packaging) | $75 | 4.4% |
| **Local materials** (PA66, rubber, nylon) | $260 | 15.3% |
| **Subtotal Local** | **$1,040** | **61.2%** |
| **Import** (cylinder, LRF, regulator, solenoid, etc.) | $660 | 38.8% |

**Current local content: 61%** (exceeds 60% MUST)

**Roadmap to 78%:**

| Import Item | Cost | Localization Path | Timeline |
|-------------|------|-------------------|----------|
| LRF module | $200 | Develop with local optics partner | 12-18 months |
| HPA cylinder | $120 | Vietnamese CF winding capability | 18-24 months |
| Regulator | $85 | Local precision machining | 12 months |
| Solenoid | $65 | Local solenoid manufacturer | 6-12 months |

---

# 4. MANUFACTURING PROCESS PLAN

## 4.1 Process Selection

| Component | Process | Equipment | Local Capability | Notes |
|-----------|---------|-----------|-----------------|-------|
| Barrel | CNC turning + boring | CNC lathe | YES - job shops | Critical bore tolerance H7 |
| Receiver | CNC 3+2 axis milling | CNC mill | YES - job shops | Complex geometry |
| Stock/Grip | Injection molding | Mold press | YES - mold shops | Tooling $8-12K |
| Safety parts | CNC + heat treat | CNC + furnace | YES | 17-4 PH H900 condition |
| PCB | SMD assembly | Pick & place | YES - PCB houses | Local assembly |
| Net | Knotting/weaving | Manual/semi-auto | YES - textile shops | UHMWPE handling |
| Parachute | Pattern cutting + sewing | Industrial sewing | YES | Standard skill |
| Projectile body | CNC turning | CNC lathe | YES | Aluminum or nylon |
| Final assembly | Manual | Assembly jig | YES | Trained technicians |

## 4.2 Manufacturing Flow

```
VDC-100 MANUFACTURING FLOW
═══════════════════════════════════════════════════════════════════════════════

INCOMING MATERIAL & COMPONENTS
        |
        v
+-------------------+     +-------------------+     +-------------------+
| MACHINING CELL    |     | MOLDING CELL      |     | ELECTRONICS CELL  |
|                   |     |                   |     |                   |
| • Barrel (CNC)    |     | • Stock (inject)  |     | • PCB assembly    |
| • Receiver (CNC)  |     | • Grip (inject)   |     | • Wiring harness  |
| • Safety (CNC)    |     | • Proj body (CNC  |     | • LRF integration |
| • Scope rail (CNC)|     |   or inject)      |     | • Battery pack    |
|                   |     |                   |     |                   |
| QC: Dimensional   |     | QC: Visual +      |     | QC: Functional    |
|     inspection    |     |     dimensional    |     |     test          |
+--------+----------+     +--------+----------+     +--------+----------+
         |                          |                          |
         v                          v                          v
+------------------------------------------------------------------------+
| SURFACE TREATMENT                                                       |
| • Barrel: Hard anodize Type III (MIL-A-8625)                           |
| • Receiver: Anodize Type II + Cerakote                                 |
| • Steel parts: Passivation (MIL-DTL-5002)                             |
| • Polymer: As-molded (UV stabilized resin)                            |
+--------+---------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------------+
| ASSEMBLY LINE (10-step sequence, ~2 hours)                             |
|                                                                         |
| Step 1: Receiver + barrel                                              |
| Step 2: Gas system (regulator + valve + fittings)                      |
| Step 3: Trigger mechanism + safety                                     |
| Step 4: Electronics + wiring                                           |
| Step 5: Stock + grip attachment                                        |
| Step 6: Scope rail + LRF mounting                                     |
| Step 7: Pneumatic pressure test (150 bar, 10 min hold)                |
| Step 8: Electronic function test (all interlocks)                      |
| Step 9: Live fire test (3 shots @ 100 bar)                            |
| Step 10: Final inspection + packaging                                  |
|                                                                         |
+--------+---------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------------+
| PROJECTILE ASSEMBLY (parallel line)                                     |
|                                                                         |
| Step P1: Net folding + weight attachment                               |
| Step P2: Parachute packing                                             |
| Step P3: Timer mechanism insertion                                     |
| Step P4: Body assembly (net + chute + timer)                           |
| Step P5: Fin attachment                                                |
| Step P6: Functional test (deploy mechanism)                            |
| Step P7: Packaging (5-pack)                                            |
|                                                                         |
+--------+---------------------------------------------------------------+
         |
         v
+------------------------------------------------------------------------+
| FINAL PACKAGING & SHIPPING                                              |
|                                                                         |
| • Launcher in carry case                                               |
| • 5x projectiles                                                       |
| • Accessories kit                                                      |
| • User manual + quick start guide                                      |
| • Certificate of conformance                                           |
+------------------------------------------------------------------------+

═══════════════════════════════════════════════════════════════════════════════
```

## 4.3 Production Capacity

| Metric | Value | Notes |
|--------|-------|-------|
| Assembly time per unit | ~2 hours | 2 technicians |
| Daily capacity | 3-4 units | Single shift, 8 hours |
| Monthly capacity | 60-80 units | 20 working days |
| Ramp-up time | 3 months | First 2 months: 20 units/month |
| Tooling investment | ~$20,000 | Injection molds + assembly jigs |

## 4.4 Supplier Strategy

| Component Type | Strategy | Number of Suppliers |
|----------------|----------|-------------------|
| **Critical** (barrel, receiver) | Dual source, local CNC | 2 |
| **Imported** (LRF, cylinder) | Single source + approved backup | 1+1 |
| **Commodity** (fasteners, seals) | Multiple local sources | 3+ |
| **Specialized** (net, parachute) | Develop 1 local, 1 backup | 1+1 |

---

# 5. QUALITY CONTROL PLAN

## 5.1 Incoming Inspection

| Material/Component | Inspection | Accept Criteria | Frequency |
|--------------------|------------|-----------------|-----------|
| Al 6061-T6 bar stock | Mill cert review, hardness | UTS ≥290 MPa, HB ≥95 | Every lot |
| PA66-GF30 resin | Lot cert, moisture | MFI per spec, moisture <0.2% | Every lot |
| HPA cylinder | Hydro cert, visual | Current hydro, no damage | 100% |
| Regulator | Function test | Output ±5% of setting | 100% |
| Solenoid | Response time | <15ms, NC verified | 100% |
| LRF module | Range accuracy | ±1m @ 100m | 100% |
| O-rings (NBR/FKM) | Visual, durometer | Shore A 70±5, no defects | Sample |

## 5.2 In-Process Inspection

| Operation | Check | Tool | Accept | Frequency |
|-----------|-------|------|--------|-----------|
| Barrel bore | Diameter H7 | Bore gauge | 100.000-100.035mm | 100% |
| Barrel straightness | TIR | V-block + DTI | ≤0.05mm/100mm | 100% |
| Receiver CNC | Critical dims | CMM or calipers | Per drawing | 100% |
| Anodize thickness | Coating | Eddy current | 25-50 μm (Type III) | Sample |
| Mold parts | Flash, fill | Visual + dims | No flash, dims ±0.3mm | First article + sample |
| PCB assembly | Solder quality | Visual + AOI | IPC-A-610 Class 2 | 100% |

## 5.3 Final Assembly Test

| Test | Procedure | Accept Criteria | Record |
|------|-----------|-----------------|--------|
| **Pressure test** | 150 bar, 10 min hold | Zero leaks (soapy water) | Certificate |
| **Safety interlock** | All 8 states (per EXP-3) | 8/8 correct | Certificate |
| **Trigger pull** | Force gauge | 20-40N | Certificate |
| **Live fire** | 3 shots @ 100 bar | All fire, V within ±10% | Certificate |
| **LRF accuracy** | Range 3 known targets | ±1m | Certificate |
| **Visual** | Full inspection | No cosmetic defects | Certificate |
| **Weight** | Scale | ≤8.0 kg loaded | Certificate |

## 5.4 Acceptance Test Procedure (ATP)

Each production unit receives a Certificate of Conformance including:
- Serial number
- Build date
- Pressure test result
- Safety test result (8/8)
- Live fire velocity (3 shots, mean ± SD)
- LRF calibration check
- Weight
- Inspector signature

---

# 6. DOCUMENTATION PACKAGE

## 6.1 Operator Manual (Outline)

| Chapter | Content | Status |
|---------|---------|--------|
| 1 | System Overview | PENDING |
| 2 | Safety Warnings & Handling | PENDING |
| 3 | Assembly & Setup | PENDING |
| 4 | Loading & Firing | PENDING |
| 5 | Targeting (Reticle Use) | PENDING |
| 6 | Reloading & Gas Refill | PENDING |
| 7 | Storage & Transport | PENDING |
| 8 | Troubleshooting | PENDING |
| A | Specifications Table | PENDING |
| B | Parts List | PENDING |

## 6.2 Maintenance Manual (Outline)

| Chapter | Content | Status |
|---------|---------|--------|
| 1 | Preventive Maintenance Schedule | PENDING |
| 2 | Field Cleaning (every 50 shots) | PENDING |
| 3 | Seal Replacement (every 500 shots) | PENDING |
| 4 | Barrel Inspection | PENDING |
| 5 | Electronics Diagnostics | PENDING |
| 6 | Spare Parts List | PENDING |
| 7 | Depot-Level Maintenance | PENDING |

## 6.3 Test Procedures (Qualification)

| Test | Standard | Duration | Est. Cost |
|------|----------|----------|-----------|
| Environmental (temp, humidity) | MIL-STD-810H Methods 501-502 | 4 weeks | $8,000 |
| Vibration | MIL-STD-810H Method 514 | 1 week | $3,000 |
| Drop (1m, 6 faces) | MIL-STD-810H Method 516 | 1 week | $2,000 |
| Salt fog (corrosion) | MIL-STD-810H Method 509 | 2 weeks | $3,000 |
| EMC | MIL-STD-461G | 2 weeks | $5,000 |
| Safety (FMEA + HAZOP) | MIL-STD-882E | Analysis | $3,000 |
| Endurance (2,000 cycles) | Custom | 4 weeks | $5,000 |
| Accuracy (CEP @ ranges) | Custom | 1 week | $2,000 |
| Reliability (MTBF demo) | MIL-HDBK-781A | 2 weeks | $4,000 |
| **TOTAL** | | **~12 weeks** | **$35,000-46,000** |

---

# 7. COST SENSITIVITY & VOLUME PRICING

## 7.1 Volume Pricing Projection

| Volume (units) | Unit Cost | Selling Price | Gross Margin |
|----------------|-----------|---------------|-------------|
| 1-10 (prototype) | $2,200 | $6,000 | 63.3% |
| 11-50 (pilot) | $1,900 | $5,800 | 67.2% |
| 51-100 (initial) | $1,700 | $5,400 | 68.5% |
| 101-500 (production) | $1,400 | $4,800 | 70.8% |
| 500+ (mature) | $1,200 | $4,200 | 71.4% |

**Cost reduction drivers:**
- Injection mold amortization (spread over more units)
- Volume discounts on imported components
- Learning curve on assembly (2h → 1.5h)
- Local content increase (import substitution)

## 7.2 Worst-Case Cost Scenario

| Risk | Impact | Probability | Cost Delta |
|------|--------|-------------|------------|
| Al price +30% | +$35 | Medium | +2.1% |
| Import shipping +50% | +$25 | Low | +1.5% |
| LRF module +20% | +$40 | Medium | +2.4% |
| Labor +25% | +$19 | Low | +1.1% |
| Scrap rate 5% | +$12 | Medium | +0.7% |
| **Total worst case** | **+$131** | | **+7.7%** |

**Worst case unit cost: $1,831** — still well under $2,000 target.

---

# 8. SUPPLY CHAIN & LEAD TIMES

## 8.1 Critical Path (First Lot)

```
SUPPLY CHAIN TIMELINE — FIRST PRODUCTION LOT (50 units)
═══════════════════════════════════════════════════════════════════════════════

WEEK 0 ──────────────────────────────────────────────────────────────────
| Order all materials and components
|
| LONG LEAD (8 weeks):
|   • HPA cylinders (50x) — Import
|   • LRF modules (50x) — Import
|   • Injection mold tooling — Local ($20K)
|
| MEDIUM LEAD (4 weeks):
|   • Al 6061-T6 bar stock — Local
|   • PA66-GF30 resin — Import/local
|   • Regulators (50x) — Import
|   • Solenoid valves (50x) — Import
|
| SHORT LEAD (1-2 weeks):
|   • Fasteners, seals, hardware — Local
|   • PCB components — Local/import
|   • Net material (UHMWPE) — Import

WEEK 4 ──────────────────────────────────────────────────────────────────
| Start CNC machining (barrels, receivers)
| Start PCB assembly
| Start net fabrication

WEEK 6 ──────────────────────────────────────────────────────────────────
| Injection mold trials (stock, grip)
| Anodize first batch of machined parts
| Receive medium-lead imports

WEEK 8 ──────────────────────────────────────────────────────────────────
| Receive long-lead imports (cylinders, LRF)
| Start final assembly line
| Start projectile assembly (parallel)

WEEK 10-12 ──────────────────────────────────────────────────────────────
| Assembly and testing (3-4 units/day)
| QC and packaging
| First units ship

WEEK 16 ──────────────────────────────────────────────────────────────────
| Lot complete (50 units)
| Lessons learned for next lot

═══════════════════════════════════════════════════════════════════════════════

ESTABLISHED SUPPLY: After first lot, reorder lead = 8 weeks
                    Assembly lead = 2-3 weeks per batch of 20

═══════════════════════════════════════════════════════════════════════════════
```

## 8.2 Inventory Strategy

| Component Type | Strategy | Buffer Stock |
|----------------|----------|-------------|
| Imported critical (LRF, cylinder) | Order 10% extra | 2 months |
| Local machined (barrel, receiver) | Just-in-time | 2 weeks |
| Commodity (fasteners, seals) | Kanban | 1 month |
| Projectile materials | Batch order per lot | 1 lot ahead |

---

# 9. DOCUMENT LINKS

## Phase 4 Documents
- [[04_detail/prototype_design|Prototype Design Specifications]]
- [[04_detail/prototype_BOM_procurement|BOM & Procurement]]
- [[04_detail/experiment_procedures|Experiment Procedures]]
- [[04_detail/gate_review|Gate 4A/4B Review]]

## Phase 3 Reference
- [[03_embodiment/OCP_optimization_production|Phase 3: OCP Optimization]]
- [[03_embodiment/RISM_requirements_materials|Phase 3: Materials Selection]]

---

# 10. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **2.0** | **2026-02-08** | **New comprehensive document. Scaling laws, production BOM ($1,700/unit), manufacturing flow, QC plan, qualification test plan ($35-46K), volume pricing, supply chain timeline. Pending prototype data for final parameters.** |

---

*Production design parameters will be finalized after VDC-33 prototype testing. Scale-up calculations provide preliminary values; actual test data will confirm or adjust.*

**Status:** Awaiting [[04_detail/experiment_procedures|Prototype Test Results]] → [[04_detail/gate_review|Gate 4A Review]]
