---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: OCP-P
title: Production Planning
version: 1.0
created: 2026-02-06
status: complete
---

# STEP P: PRODUCTION PLANNING
## Manufacturing Flow, Supplier Strategy & Quality Control
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 15 of 15

**Purpose:** Define the complete production flow for the BSU-V1 LOMAH scoring unit, from raw material procurement through final acceptance testing. Establish supplier base, quality gates, assembly sequence, and production capacity planning.

**Input:** [[OCP_O_optimization]] (Optimized design), [[OCP_C_cost_analysis]] (BOM & costs)
**Output:** Production-ready manufacturing plan for Phase 4 detail design

---

## 1. PRODUCTION FLOW OVERVIEW

### 1.1 Six-Phase Production Flow

```
PHASE 1          PHASE 2          PHASE 3          PHASE 4          PHASE 5          PHASE 6
PROCUREMENT      FABRICATION      SUB-ASSEMBLY     FINAL ASSEMBLY   TEST & QC        PACK & SHIP
(2-6 weeks)      (2-4 weeks)      (1-2 weeks)      (1 day)          (1 day)          (1 day)
    │                │                │                │                │                │
    ▼                ▼                ▼                ▼                ▼                ▼
┌────────┐    ┌────────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│Import   │    │CNC enclos. │    │PCB+SMT   │    │Wire      │    │Power-on  │    │Foam      │
│ICs,FPGA │    │CNC bar     │    │Battery   │    │Install   │    │BIT test  │    │insert    │
│ADC,MCU  │    │PCB fab     │    │pack      │    │PCBs      │    │Accuracy  │    │Case pack │
│Cells    │    │Anodize     │    │Cable     │    │Battery   │    │IP67 seal │    │Label     │
│Connect. │    │Paint       │    │harness   │    │Seal      │    │Burn-in   │    │Ship      │
│Passives │    │Rubber mold │    │Sensor    │    │Close lid │    │Final QC  │    │          │
│         │    │            │    │assembly  │    │          │    │          │    │          │
└────────┘    └────────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
                                                     │
                                              ~4 hours labor
```

### 1.2 Lead Time Summary

| Phase | Duration | Critical Path Item |
|-------|----------|-------------------|
| 1. Procurement | 2-6 weeks | Sensor bar extrusion (4-6 weeks first order) |
| 2. Fabrication | 2-4 weeks | CNC enclosure + anodize + paint (3 weeks) |
| 3. Sub-assembly | 1-2 weeks | PCB fabrication + SMT assembly (2 weeks) |
| 4. Final assembly | 4 hours | Labor-limited |
| 5. Test & QC | 2 hours + 4h burn-in | Burn-in station limited |
| 6. Pack & ship | 0.5 day | Standard |
| **Total (first batch)** | **8-12 weeks** | Procurement + fabrication overlap |
| **Repeat batches** | **4-6 weeks** | With stocked components |

---

## 2. SUPPLIER STRATEGY

### 2.1 Supplier Matrix

| # | Component / Service | Supplier(s) | Location | Lead Time | Qualification Status |
|---|---------------------|-------------|----------|-----------|---------------------|
| **LOCAL SUPPLIERS** | | | | | |
| S-01 | Al 6061-T6 CNC enclosure | Primary: Cơ Khí Chính Xác (HCMC); Backup: Hà Nội Precision | HCMC / Hanoi | 2-3 weeks | To qualify (Phase 4) |
| S-02 | Al 6063-T5 sensor bar (extrusion + CNC) | Primary: Nhôm Việt Nhật; Backup: Xingfa VN | HCMC / Binh Duong | 4-6 weeks (first); 2-3 weeks (repeat) | To qualify |
| S-03 | PCB fabrication (main + power + daughter) | Primary: Sài Gòn PCB; Backup: An Phát Circuit | HCMC | 1-2 weeks | To qualify |
| S-04 | SMT assembly | Primary: VN EMS (HCMC); Backup: Hanoi Electronics | HCMC / Hanoi | 1-2 weeks | To qualify |
| S-05 | Battery pack assembly (4S1P + BMS) | Local battery integrator (HCMC) | HCMC | 1-2 weeks | To qualify |
| S-06 | EPDM gaskets (custom profile) | Cao Su Bình Dương | Binh Duong | 2-3 weeks (tooling: 4 weeks) | To qualify |
| S-07 | Natural rubber acoustic boots | Cao Su Bình Phước | Binh Phuoc | 2-3 weeks (tooling: 4 weeks) | To qualify |
| S-08 | Cable + wiring harness (PUR jacket) | Dây Cáp Sài Gòn | HCMC | 1-2 weeks | To qualify |
| S-09 | Hard anodize Type III (MIL-A-8625F) | Mạ Anot Thủ Đức | HCMC | 1-2 weeks | To qualify |
| S-10 | Paint RAL 6031 (2K polyurethane) | Sơn Việt | HCMC | 1 week | To qualify |
| S-11 | Transport case (rotomolded PE) | Hộp Nhựa Hà Nội | Hanoi | 2-3 weeks (tooling: 6 weeks) | To qualify |
| S-12 | Final assembly + test labor | In-house (HCMC facility) | HCMC | On demand | In-house |
| S-13 | Packaging + labeling | In Ấn Sài Gòn | HCMC | 1 week | To qualify |
| **IMPORT SUPPLIERS** | | | | | |
| S-14 | ICs + sensors (FPGA, MCU, ADC, MEMS, analog) | DigiKey, Mouser | USA | 1-3 weeks | Established |
| S-15 | Passive components (resistors, caps, inductors) | DigiKey + LCSC | USA / China | 1-2 weeks | Established |
| S-16 | Li-ion cells (Samsung INR18650-35E) | China distributor (verified authentic) | China | 2-3 weeks | To verify |
| S-17 | IP67 connectors (Amphenol / alternative) | Amphenol / Chinese alternative | China / USA | 2-4 weeks | To evaluate |
| S-18 | SS 316 fasteners (M3-M6) | China fastener supplier | China | 1-2 weeks | Established |
| S-19 | Thermal pads, conformal coating | DigiKey | USA | 1-3 weeks | Established |

### 2.2 Supplier Qualification Plan

| Priority | Supplier(s) | Qualification Activity | Timeline |
|----------|-------------|----------------------|----------|
| HIGH | S-01, S-02 (CNC, extrusion) | First article inspection (FAI); dimensional check 100%; surface finish; material cert | Phase 4, Month 1-2 |
| HIGH | S-03, S-04 (PCB, SMT) | IPC-A-610 Class 2 audit; solder quality; BOM verification; DRC | Phase 4, Month 1-2 |
| HIGH | S-16 (Li-ion cells) | Authenticity verification; capacity test (3 cells per batch); datasheet match | Phase 4, Month 1 |
| MEDIUM | S-06, S-07 (rubber) | Shore hardness test; dimensional check; aging test (72h @ 70°C); material cert | Phase 4, Month 2-3 |
| MEDIUM | S-09 (anodize) | Thickness measurement (eddy current); hardness test; salt spray witness coupon | Phase 4, Month 2 |
| MEDIUM | S-05 (battery assembly) | Spot weld pull test; BMS function test; charge/discharge cycle; safety test | Phase 4, Month 2 |
| LOW | S-11 (transport case) | Drop test; IP rating; foam insert fit check | Phase 4, Month 3 |

### 2.3 Dual-Source Strategy

| Component | Primary | Backup | Switch Criteria |
|-----------|---------|--------|-----------------|
| CNC enclosure | HCMC shop | Hanoi shop | Lead time >4 weeks or quality rejection >5% |
| PCB fabrication | Sài Gòn PCB | An Phát Circuit | Lead time >3 weeks or yield <95% |
| SMT assembly | VN EMS HCMC | Hanoi Electronics | Capacity overflow or quality issue |
| Al extrusion | Nhôm Việt Nhật | Xingfa VN | Lead time >6 weeks |
| ICs | DigiKey | Mouser / LCSC | Stock-out or lead time >4 weeks |

---

## 3. ASSEMBLY SEQUENCE

### 3.1 Detailed Assembly Steps (20 Steps)

**Pre-Assembly (Sub-assemblies prepared in Phase 3)**

| Step | Operation | Station | Time | Tools | QC Check |
|------|-----------|---------|------|-------|----------|
| SA-1 | Populate + solder main PCB (SMT line) | SMT line | - | Reflow oven | AOI + visual IPC-A-610 |
| SA-2 | Populate + solder power PCB (SMT line) | SMT line | - | Reflow oven | AOI + visual |
| SA-3 | Populate + solder 4× daughter PCBs (SMT line) | SMT line | - | Reflow oven | AOI + visual |
| SA-4 | Flash firmware to STM32H743 + iCE40UP5K bitstream | Programming station | 5 min | ST-LINK V3 + FTDI | Verify checksum + version |
| SA-5 | Assemble battery pack: spot-weld 4S1P + BMS board + shrink wrap | Battery station | 15 min | Spot welder + heat gun | Pull test (>5 kgf); voltage check |
| SA-6 | Fabricate cable harness: sensor cable (500mm, 7-pin) + internal cables | Cable station | 20 min | Crimping tool + soldering | Continuity test all pins |
| SA-7 | Press-fit threaded inserts into enclosure (M3, M4 helicoils) | Mechanical bench | 10 min | Press-fit tool | Torque test (sample) |

**Final Assembly (In-house, ~4 hours per unit)**

| Step | Operation | Station | Time | Tools | QC Check |
|------|-----------|---------|------|-------|----------|
| FA-1 | Install 3× IP67 cable glands into enclosure front panel | Bench 1 | 10 min | Spanner wrench | Finger-tight + 1/4 turn |
| FA-2 | Apply thermal pad to enclosure base plate (FPGA zone) | Bench 1 | 2 min | Clean surface + placement | Visual: centered, no air bubbles |
| FA-3 | Install main PCB on 4× M3 standoffs | Bench 1 | 5 min | M3 hex driver, 0.4 Nm | Torque verified; no flex |
| FA-4 | Install power PCB on 2× M3 standoffs | Bench 1 | 3 min | M3 hex driver, 0.4 Nm | Torque verified |
| FA-5 | Connect internal cables: power→main, battery→BMS | Bench 1 | 5 min | Connector insertion | Click engagement confirmed |
| FA-6 | Install battery pack into battery bay | Bench 1 | 3 min | Slide-in + connector | Voltage reading on fuel gauge |
| FA-7 | Route sensor cable through gland; connect to main PCB | Bench 1 | 5 min | Cable threading | Gland tightened; strain relief |
| FA-8 | Route Ethernet cable through gland; connect to RJ45 jack | Bench 1 | 3 min | Cable threading | Gland tightened |
| FA-9 | Install EPDM O-ring gasket in lid groove | Bench 1 | 2 min | Manual placement | Seated fully in groove; no twists |
| FA-10 | Close lid: 6× M4 SS316 bolts, cross-pattern torque | Bench 1 | 8 min | M4 torque driver, 2.5 Nm | All 6 bolts torqued in sequence |
| FA-11 | Install battery door with cam-latch | Bench 1 | 3 min | Manual | Open/close 3× cycles; latch secure |
| FA-12 | Attach 4× daughter PCBs into sensor bar pockets | Bench 2 | 10 min | M2.5 screws, 0.3 Nm | Poka-yoke: M1 only fits pocket 1 |
| FA-13 | Install 4× rubber acoustic boots over mic pockets | Bench 2 | 5 min | Manual press-fit | Flush seating; no gaps |

### 3.2 Assembly Flow Diagram

```
                    ┌─────────────┐
                    │  INCOMING   │
                    │  INSPECTION │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │  SMT     │ │ MECH     │ │ CABLE    │
        │ ASSEMBLY │ │ PREP     │ │ HARNESS  │
        │ SA-1→SA-4│ │ SA-7     │ │ SA-6     │
        └────┬─────┘ └────┬─────┘ └────┬─────┘
             │            │            │
             ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐     │
        │ BATTERY  │ │ SURFACE  │     │
        │ PACK     │ │ FINISH   │     │
        │ SA-5     │ │(anodize+ │     │
        │          │ │ paint)   │     │
        └────┬─────┘ └────┬─────┘     │
             │            │            │
             └────────┬───┘────────────┘
                      ▼
               ┌──────────────┐
               │   FINAL      │
               │   ASSEMBLY   │
               │   FA-1→FA-13 │
               │   (~4 hours) │
               └──────┬───────┘
                      ▼
               ┌──────────────┐
               │   TEST & QC  │
               │   T-1→T-8    │
               └──────┬───────┘
                      ▼
               ┌──────────────┐
               │  PACK & SHIP │
               └──────────────┘
```

---

## 4. TEST & QUALITY CONTROL PLAN

### 4.1 Factory Acceptance Test (FAT) Sequence

| # | Test | Method | Pass Criteria | Duration | Equipment |
|---|------|--------|--------------|----------|-----------|
| T-1 | Visual inspection | IPC-A-610 Class 2 | No defects; correct labeling; cosmetic grade | 10 min | Magnifier + checklist |
| T-2 | Power-on / BIT | Apply power; auto-BIT runs | All 5 BIT checks PASS (sensors, FPGA, MCU, memory, battery) | 2 min | DC supply or battery |
| T-3 | Sensor functional | Clap test at 4 known positions | 4/4 mics respond; waveform shape correct on scope | 5 min | Oscilloscope + PC |
| T-4 | Scoring accuracy | Acoustic stimulator at 5 known positions on test jig | ±15mm at all 5 points (relaxed from ±10mm for FAT; ±10mm verified at DV) | 15 min | Acoustic test jig |
| T-5 | Ethernet comms | Connect to PC; verify data stream | Web UI loads; shot data displays; latency <100ms | 5 min | Laptop + CAT6 cable |
| T-6 | IP67 seal check | Pressurize enclosure to 10 kPa; hold 10 min | Pressure drop <1 kPa | 15 min | Pressure tester + gauge |
| T-7 | Burn-in | Power on continuous at 40°C for 4 hours | No errors in BIT log; battery fuel gauge within 5% | 4 hours | Burn-in chamber |
| T-8 | Final inspection | Verify serial number, firmware version, accessories | Complete kit per packing list | 5 min | Checklist |

**Total test time:** ~1 hour active + 4 hours burn-in (unattended)

### 4.2 Incoming Quality Control (IQC)

| Component | Inspection | Sample Size | Accept/Reject |
|-----------|-----------|-------------|---------------|
| CNC enclosure | Dimensional (CMM or caliper); surface finish (Ra); thread gauges | 100% first batch; 20% thereafter | Per drawing ±0.1mm; Ra ≤1.6μm |
| Sensor bar | Dimensional; mic pocket positions (±0.1mm Z-axis critical) | 100% always (accuracy-critical) | Per drawing; Z-offset 40.0 ±0.1mm |
| PCBs (bare) | Visual; impedance (50Ω traces); via fill; layer alignment | 10% per batch | IPC-6012 Class 2 |
| SMT assemblies | AOI 100%; X-ray (BGA/QFN) 10% sample; ICT or flying probe | 100% AOI; 10% X-ray | IPC-A-610 Class 2 |
| Li-ion cells | Capacity test (3 cells per batch of 100); OCV check all | 3% capacity; 100% OCV | ≥3,400 mAh; OCV 3.55-3.70V |
| EPDM gaskets | Shore hardness; dimensional; compression set (sample) | 5% per batch | Shore A 70 ±5; per drawing ±0.3mm |
| IP67 connectors | Mating cycle test (3 cycles); pin resistance | 100% first batch; 10% after | <20 mΩ contact resistance |

### 4.3 Quality Metrics & Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| First pass yield (FAT) | ≥95% | Units passing T-1 through T-8 without rework |
| Incoming reject rate | ≤3% | IQC rejections / total incoming lots |
| Field failure rate (Year 1) | ≤2% | Warranty returns / units shipped |
| MTBF (operational) | ≥5,000 hours | Per MIL-HDBK-217F prediction |
| Customer satisfaction | ≥4.0/5.0 | Post-deployment survey |

---

## 5. PRODUCTION CAPACITY PLANNING

### 5.1 Capacity by Phase

| Production Phase | Equipment/Resource | Capacity (units/month) | Bottleneck? |
|-----------------|-------------------|----------------------|-------------|
| SMT assembly | External EMS line | 200+ | No |
| CNC enclosure | 1 CNC machine, 1 operator | 50 (2 enclosures/day) | **Yes — primary** |
| Sensor bar | Extrusion batch + CNC pockets | 100 (batch process) | No |
| Battery pack | 1 assembly station | 100 | No |
| Final assembly | 1 bench, 1 technician | 40 (2 units/day × 20 days) | **Yes — secondary** |
| Test + burn-in | 4 burn-in slots | 80 (4 units × 20 days) | No |
| **System capacity** | | **40 units/month** | Limited by final assembly |

### 5.2 Scaling Strategy

| Volume | Strategy | Unit Cost Impact |
|--------|----------|-----------------|
| Prototype (2 units) | All processes at minimum batch; expect higher unit cost (~$500) | +41% |
| Pilot (10 units) | First production batch; validate process; $354/unit achievable | Baseline |
| Low rate (50 units/year) | Monthly batches of 5; steady-state supplier relationships | -5% ($336) |
| Full rate (200 units/year) | Weekly batches; dedicated CNC fixtures; 2nd assembly station | -12% ($312) |
| Export scale (500+ units/year) | Dedicated production cell; automated test station; volume pricing | -18% ($290) |

### 5.3 Production Timeline (First Batch: 10-Lane Range System)

```
WEEK:  1    2    3    4    5    6    7    8    9   10   11   12
       │    │    │    │    │    │    │    │    │    │    │    │
PROCURE ████████████████████
 Import ████████████████████
 Local  ████████████

FABRICATE      ████████████████
 CNC encl.     ██████████████
 CNC bar       ████████████████
 PCB fab       ████████
 Anodize            ██████
 Paint               ████
 Rubber mold   ████████████████ (tooling only for 1st)

SUB-ASSY                  ██████████
 SMT assembly             ████████
 Battery pack             ████████
 Cable harness            ██████

FINAL ASSY                          ████████
 10 units × 4h/unit                 ████████

TEST & QC                                ████████
 FAT + burn-in                           ████████

PACK & SHIP                                    ████
                                               ████
```

**First batch delivery: ~12 weeks from order**
**Repeat batch delivery: ~6 weeks (stocked components)**

---

## 6. PRODUCTION DOCUMENTATION (Phase 4 Deliverables)

| Document | Description | Status |
|----------|-------------|--------|
| Assembly work instructions | Step-by-step with photos for FA-1 through FA-13 | Phase 4 |
| Test procedure (FAT) | Detailed procedure for T-1 through T-8 with pass/fail forms | Phase 4 |
| IQC procedure | Incoming inspection checklists per component | Phase 4 |
| BOM (production) | Exact part numbers, alternates, minimum order quantities | Phase 4 |
| Firmware release package | Binary images + programming instructions + version control | Phase 4 |
| Supplier qualification records | FAI reports, material certs, audit results | Phase 4 |
| Packing list template | Standard kit contents per unit | Phase 4 |
| Training manual | Assembler training (Vietnamese language) | Phase 4 |

---

## 7. RISK MANAGEMENT (PRODUCTION)

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| PR-1 | IC supply shortage (global chip shortage) | Medium | High | Maintain 3-month safety stock of critical ICs (FPGA, MCU, ADC); qualify LCSC as alternate source |
| PR-2 | CNC quality inconsistency | Medium | Medium | 100% dimensional inspection (first batch); fixture design for repeatability |
| PR-3 | Li-ion cell counterfeit | Low | High | Source only from verified Samsung distributors; capacity test every batch |
| PR-4 | Sensor bar mic pocket position error | Low | High | 100% incoming inspection of Z-offset (40.0 ±0.1mm); Go/No-Go gauge |
| PR-5 | SMT solder quality (QFN voiding) | Medium | Medium | X-ray inspection 10% sample; qualify EMS partner IPC-A-610 Class 2 |
| PR-6 | Rubber mold degradation | Low | Low | Mold life 5,000+ cycles; inspect every 500 cycles |
| PR-7 | Key-person dependency (assembly) | Medium | Medium | Cross-train 2 technicians; documented work instructions |

---

## 8. PRODUCTION COST MODEL

### 8.1 Non-Recurring Engineering (NRE) Costs

| Item | Cost (USD) | Notes |
|------|-----------|-------|
| EPDM gasket tooling (2 molds) | $800 | One-time; amortized over 500+ units |
| Rubber boot tooling (1 mold) | $500 | One-time |
| Transport case foam insert tooling | $300 | CNC-cut EVA foam template |
| CNC fixture (enclosure + bar) | $1,200 | Improves repeatability and reduces cycle time |
| Acoustic test jig | $2,000 | Custom test fixture with 5 known positions |
| Burn-in chamber setup (4 slots) | $500 | Temperature-controlled enclosure |
| Programming jig (pogo-pin) | $800 | For production firmware flashing |
| **Total NRE** | **$6,100** | Amortized: $12.20/unit over 500 units |

### 8.2 Production Cost Summary

| Volume | Unit Material | Unit Labor | NRE Amortization | Unit Total |
|--------|-------------|-----------|------------------|-----------|
| 2 (prototype) | $308 | $45 | $3,050 | ~$3,400 |
| 10 (pilot) | $308 | $35 | $610 | ~$953 |
| 50 | $293 | $35 | $122 | ~$450 |
| 100 | $285 | $32 | $61 | ~$378 |
| 500 | $270 | $28 | $12 | ~$310 |
| 1,000 | $255 | $25 | $6 | ~$286 |

> **Baseline pricing at 100+ units: $354/lane** (includes 15% margin over $308 material cost)

---

## 9. SYSTEMS THINKING: PRODUCTION AS A SYSTEM

### 9.1 Production Feedback Loops

```
R1: Quality Learning Loop (REINFORCING)
   Quality data → Process improvement → Better yield → Lower cost → More investment → More data

B1: Capacity Constraint Loop (BALANCING)
   More orders → Assembly backlog → Longer lead time → Customer dissatisfaction → Fewer orders

R2: Supplier Partnership Loop (REINFORCING)
   Consistent orders → Supplier invests in capability → Better quality/price → More competitive product → More orders
```

### 9.2 Leverage Points

| Level | Intervention | Production Application |
|-------|-------------|----------------------|
| L4 | Self-organization | Cross-trained technicians; any station can produce any sub-assembly |
| L5 | Rules | "Never ship a unit that fails any FAT step" — zero-tolerance |
| L6 | Information flows | Real-time yield dashboard; shared with all suppliers quarterly |
| L8 | Negative feedback | Statistical process control on CNC dimensions; auto-flag if 3σ drift |
| L9 | Reduce delays | Safety stock on critical ICs; pre-staged kits for assembly |

---

## 10. META-LEARNING SKILL APPLIED

**Skill: Process Planning (Production-level)**

- Key insight: The **CNC enclosure is the production bottleneck** — 2 units/day limits monthly output to 40 units with a single machine. This drives the scaling strategy: fixture optimization first, then second machine if demand exceeds 50/month.
- The **sensor bar Z-offset tolerance (±0.1mm)** is the single most quality-critical dimension in production — it directly determines scoring accuracy. This mandates 100% incoming inspection with a dedicated gauge.
- NRE costs ($6,100) are modest relative to production value, making the BSU-V1 economically viable even at low volumes (break-even at ~20 units for tooling amortization).

---

**Next Step:** Gate 3 review → Phase 4 (Detail Design)

*OCP-P Complete | 6-phase production flow | 19 suppliers | 20-step assembly | FAT procedure | Capacity: 40 units/month*
