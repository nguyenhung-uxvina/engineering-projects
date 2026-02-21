---
project: V-SMASH
product: LITE
designation: VSM-L
phase: 4
type: procurement_plan
version: 1.0
created: 2026-02-05
status: draft
prototype_qty: 3
prototype_date: M9
---

# V-SMASH LITE - PROTOTYPE PROCUREMENT PLAN
## Phase 4: Detail Design - Procurement Strategy

**Document ID:** VSM-L-PROC-001
**Version:** 1.0
**Prototype Quantity:** 3 units (DV-01, DV-02, DV-03)
**Target Delivery:** Month 9

---

## 1. PROCUREMENT OVERVIEW

### 1.1 Prototype Build Plan

| Unit | Purpose | Configuration | Delivery |
|------|---------|---------------|----------|
| **DV-01** | Environmental qualification | Full production equivalent | M9 W1 |
| **DV-02** | Functional + accuracy testing | Full production equivalent | M9 W1 |
| **DV-03** | Recoil endurance | Instrumented | M9 W2 |

### 1.2 Budget Summary

| Category | Unit Cost | × 3 Units | Margin (20%) | Total |
|----------|-----------|-----------|--------------|-------|
| Processing | $200 | $600 | $120 | $720 |
| Sensors | $60 | $180 | $36 | $216 |
| Optics | $115 | $345 | $69 | $414 |
| Power | $30 | $90 | $18 | $108 |
| Actuation | $15 | $45 | $9 | $54 |
| Housing | $130 | $390 | $78 | $468 |
| Misc | $34 | $102 | $20 | $122 |
| Labor/Test | $100 | $300 | $60 | $360 |
| Software | $100 | $300 | $60 | $360 |
| **Subtotal** | **$784** | **$2,352** | **$470** | **$2,822** |
| Tooling (one-time) | — | — | — | $5,000 |
| Contingency | — | — | — | $1,178 |
| **TOTAL PROTOTYPE BUDGET** | | | | **$9,000** |

---

## 2. CRITICAL PATH ANALYSIS

### 2.1 Long-Lead Items (>4 weeks)

```
PROCUREMENT TIMELINE (Weeks from Order)
═══════════════════════════════════════════════════════════════════════

Item                        W1  W2  W3  W4  W5  W6  W7  W8
────────────────────────────────────────────────────────────────────────
Jetson Nano 4GB             ████████████████████████████░░░░  6 weeks
Sony IMX290 Module          ████████████████████░░░░░░░░░░░░  5 weeks
Custom Carrier PCB          ████████████████████████░░░░░░░░  6 weeks
See-through OLED Display    ████████████████████████████░░░░  6 weeks
Beam Splitter Prism         ████████████████░░░░░░░░░░░░░░░░  4 weeks
CNC Housing (Machining)     ░░░░░░░░████████████████░░░░░░░░  4 weeks*
Anodizing                   ░░░░░░░░░░░░░░░░████████░░░░░░░░  2 weeks*

█ = Lead time    ░ = Waiting/Sequential    * = After design release

CRITICAL PATH: Custom Carrier PCB (6 weeks) + Assembly (2 weeks) = 8 weeks
ORDER DEADLINE: Month 7 Week 1 for M9 delivery
```

### 2.2 Critical Items Risk Assessment

| Item | Lead Time | Risk | Mitigation |
|------|-----------|------|------------|
| **Jetson Nano 4GB** | 6 weeks | High (availability) | Order immediately, keep buffer stock |
| **Custom Carrier PCB** | 6 weeks | High (design dependent) | Finalize design M5, order M5 W4 |
| **See-through OLED** | 6 weeks | Medium (specialty) | Identify backup supplier |
| **Sony IMX290** | 5 weeks | Low (common part) | Standard distribution |
| **Housing machining** | 4 weeks | Low (local) | Multiple local vendors |

---

## 3. DETAILED PROCUREMENT LIST

### 3.1 Processing Components

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 1 | VSM-L-CPU-001 | NVIDIA Jetson Nano 4GB | 4 | $150 | $600 | 6 wk | Arrow/Digi-Key | ⬜ Quote |
| 2 | VSM-L-PCB-001 | Carrier board (custom) | 5 | $35 | $175 | 6 wk | Local PCB fab | ⬜ Design |
| 3 | VSM-L-MEM-001 | SD card 32GB industrial | 5 | $10 | $50 | 1 wk | Local | ⬜ |
| 4 | VSM-L-THM-001 | Heat sink + fan | 4 | $5 | $20 | 2 wk | AliExpress | ⬜ |

### 3.2 Sensor Components

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 5 | VSM-L-SNS-001 | Sony IMX290 module | 4 | $25 | $100 | 5 wk | Leopard Imaging | ⬜ Quote |
| 6 | VSM-L-LNS-001 | Lens 4mm f/1.2 M12 | 4 | $15 | $60 | 3 wk | Arducam | ⬜ |
| 7 | VSM-L-IMU-001 | BMI160 6-axis IMU | 5 | $5 | $25 | 2 wk | Digi-Key | ⬜ |
| 8 | VSM-L-SNS-002 | FSR402 force sensor | 5 | $8 | $40 | 2 wk | Interlink | ⬜ |
| 9 | VSM-L-SNS-003 | Ambient light sensor | 5 | $2 | $10 | 2 wk | Digi-Key | ⬜ |
| 10 | VSM-L-SNS-004 | MEMS microphone | 5 | $5 | $25 | 2 wk | Digi-Key | ⬜ |

### 3.3 Optical Components

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 11 | VSM-L-OPT-001 | Beam splitter prism 50/50 | 4 | $30 | $120 | 4 wk | Edmund Optics | ⬜ Quote |
| 12 | VSM-L-DSP-001 | See-through OLED display | 4 | $50 | $200 | 6 wk | Lumus/Vuzix | ⬜ Quote |
| 13 | VSM-L-OPT-003 | Protective window AR | 4 | $15 | $60 | 3 wk | Edmund Optics | ⬜ |
| 14 | VSM-L-OPT-002 | Reticle etched glass | 4 | $20 | $80 | 4 wk | Custom optics | ⬜ Design |

### 3.4 Power Components

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 15 | VSM-L-BAT-001 | 18650 Samsung 35E | 10 | $4 | $40 | 2 wk | Samsung SDI | ⬜ |
| 16 | VSM-L-PCB-002 | PMIC board (custom) | 5 | $12 | $60 | 4 wk | Local PCB | ⬜ Design |
| 17 | VSM-L-CON-001 | USB-C connector panel | 5 | $2 | $10 | 2 wk | Digi-Key | ⬜ |
| 18 | — | Power cables/harness | 5 | $3 | $15 | 1 wk | Local | ⬜ |
| 19 | — | Battery contacts spring | 15 | $2.50 | $38 | 2 wk | Local | ⬜ |

### 3.5 Actuation Components

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 20 | VSM-L-SOL-001 | 12V push solenoid | 5 | $5 | $25 | 3 wk | Takaha/Aliexpress | ⬜ |
| 21 | VSM-L-DRV-001 | MOSFET driver board | 5 | $3 | $15 | 2 wk | Local PCB | ⬜ |
| 22 | — | Trigger linkage mech | 4 | $7 | $28 | 3 wk | Local machine | ⬜ Design |

### 3.6 Housing Components

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 23 | VSM-L-HSG-001 | Main housing Al 6061 | 4 | $60 | $240 | 4 wk | Local CNC | ⬜ Design |
| 24 | VSM-L-HSG-002 | Front cover Al | 4 | $20 | $80 | 4 wk | Local CNC | ⬜ Design |
| 25 | VSM-L-HSG-003 | Battery door Al | 4 | $10 | $40 | 4 wk | Local CNC | ⬜ Design |
| 26 | VSM-L-HSG-004 | Picatinny mount clamp | 4 | $15 | $60 | 4 wk | Local CNC | ⬜ Design |
| 27 | VSM-L-GSK-001 | Gasket set silicone | 5 | $10 | $50 | 2 wk | Local | ⬜ Design |
| 28 | VSM-L-HW-001 | Fastener kit SS304 | 5 | $5 | $25 | 1 wk | Local | ⬜ |
| 29 | — | Anodizing (Type III) | 4 | $10 | $40 | 2 wk | Local | ⬜ |

### 3.7 Miscellaneous

| Item | Part Number | Description | Qty | Unit $ | Ext $ | Lead | Supplier | Status |
|------|-------------|-------------|-----|--------|-------|------|----------|--------|
| 30 | — | Internal cables/FPC | 5 | $8 | $40 | 3 wk | Local | ⬜ Design |
| 31 | — | Connectors assorted | 5 | $6 | $30 | 2 wk | Digi-Key | ⬜ |
| 32 | — | Labels/markings | 5 | $5 | $25 | 1 wk | Local | ⬜ |
| 33 | — | Packaging prototype | 3 | $10 | $30 | 2 wk | Local | ⬜ |

---

## 4. SUPPLIER DIRECTORY

### 4.1 International Suppliers

| Supplier | Items | Contact | Payment | Notes |
|----------|-------|---------|---------|-------|
| **Arrow Electronics** | Jetson Nano, ICs | arrow.com | Net 30 | Primary distro |
| **Digi-Key** | Sensors, connectors | digikey.com | Credit card | Fast shipping |
| **Leopard Imaging** | IMX290 module | leopardimaging.com | Wire | Jetson compatible |
| **Edmund Optics** | Beam splitter, window | edmundoptics.com | Net 30 | Precision optics |
| **Lumus** | See-through display | lumusvision.com | Wire | AR display |
| **Samsung SDI** | 18650 cells | — | Distributor | Via local agent |

### 4.2 Local Suppliers (Vietnam)

| Supplier | Items | Location | Capability | Notes |
|----------|-------|----------|------------|-------|
| **PCB Vendor A** | Carrier PCB, PMIC | HCMC | 4-layer, SMT | Qualified |
| **CNC Vendor A** | Housing, mount | Hanoi | Al 6061, ±0.05mm | Qualified |
| **CNC Vendor B** | Housing backup | HCMC | Al 6061 | Backup |
| **Anodize Vendor** | Type III anodize | HCMC | MIL-A-8625 | Qualified |
| **Gasket Vendor** | Silicone gaskets | Local | Custom profiles | — |
| **Cable Assembly** | Harnesses, FPC | HCMC | Custom cables | — |

---

## 5. PROCUREMENT SCHEDULE

### 5.1 Master Schedule

```
PROCUREMENT TIMELINE (Month 4 - Month 9)
═══════════════════════════════════════════════════════════════════════════════

                        M4      M5      M6      M7      M8      M9
Activity               W1234   W1234   W1234   W1234   W1234   W1234
─────────────────────────────────────────────────────────────────────────────────
DESIGN PHASE
  Carrier PCB design    ████████████
  Housing CAD           ████████████████
  Optics design             ████████████
  Design release                    ▼CDR

LONG-LEAD ORDERS
  Jetson Nano               ████████████████████████░░░░░░░░    Order M5W1
  See-through OLED              ████████████████████████░░░░    Order M5W2
  Custom PCB fabricate              ░░░░████████████████████    Order M5W4
  IMX290 module                 ████████████████████░░░░░░░░    Order M5W1
  Beam splitter                     ████████████████░░░░░░░░    Order M5W3

SHORT-LEAD ORDERS
  All other components                      ████████████████    Order M7W1

MECHANICAL
  Housing CNC                                   ████████████████    Start M7W2
  Anodizing                                             ████████    M8W3

ASSEMBLY
  PCB assembly                                          ████████    M8W3
  Unit assembly                                             ████████    M9W1

DELIVERY
  DV-01, DV-02                                                  ▼    M9W1
  DV-03 (instrumented)                                            ▼  M9W2

█ = Activity duration    ░ = Lead time waiting    ▼ = Milestone
```

### 5.2 Key Milestones

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| **CDR** | M6 W4 | Design release for procurement |
| **Long-lead order** | M5 W1 | Jetson, IMX290, OLED ordered |
| **PCB order** | M5 W4 | Carrier PCB to fabrication |
| **Mechanical release** | M7 W1 | Housing drawings to CNC |
| **All materials in** | M8 W4 | Ready for assembly |
| **DV-01/02 delivery** | M9 W1 | Prototypes complete |
| **DV-03 delivery** | M9 W2 | Instrumented unit complete |

---

## 6. PROCUREMENT ACTIONS

### 6.1 Immediate Actions (This Week)

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | Request quote: Jetson Nano 4GB (qty 4) | Procurement | Day 3 |
| 2 | Request quote: Sony IMX290 module | Procurement | Day 3 |
| 3 | Request quote: See-through OLED display | Procurement | Day 5 |
| 4 | Request quote: Beam splitter prism | Procurement | Day 5 |
| 5 | Confirm local CNC vendor availability | Procurement | Day 5 |
| 6 | Confirm local PCB vendor capability | Procurement | Day 5 |

### 6.2 Design-Dependent Actions (After CDR)

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 7 | Release carrier PCB Gerber files | Engineering | M5 W4 |
| 8 | Release housing CAD for CNC | Engineering | M6 W4 |
| 9 | Release PMIC PCB Gerber files | Engineering | M5 W4 |
| 10 | Release gasket drawings | Engineering | M6 W4 |
| 11 | Release FPC cable drawings | Engineering | M6 W4 |

### 6.3 Pre-Order Actions (M5)

| # | Action | Owner | Due |
|---|--------|-------|-----|
| 12 | Place Jetson Nano order | Procurement | M5 W1 |
| 13 | Place IMX290 order | Procurement | M5 W1 |
| 14 | Place OLED display order | Procurement | M5 W2 |
| 15 | Place beam splitter order | Procurement | M5 W3 |
| 16 | Place carrier PCB order | Procurement | M5 W4 |

---

## 7. RISK REGISTER

### 7.1 Procurement Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| **Jetson Nano shortage** | Medium | High | Order early, maintain 1 buffer unit | Procurement |
| **OLED supplier delay** | Medium | High | Identify backup supplier (Vuzix) | Procurement |
| **PCB quality issue** | Low | Medium | Use qualified vendor, first article inspection | QA |
| **Housing tolerance issue** | Low | Medium | First article inspection, fixture check | QA |
| **Customs delay (imports)** | Medium | Medium | Use DDP shipping, allow 1 week buffer | Logistics |
| **Component EOL** | Low | High | Monitor PCN notices, stock critical parts | Engineering |

### 7.2 Contingency Plan

| Scenario | Trigger | Action |
|----------|---------|--------|
| Jetson unavailable | >8 week lead time | Use Jetson Xavier NX (pin compatible) |
| OLED unavailable | >8 week lead time | Use micro-display + optics alternative |
| Local CNC overloaded | >6 week lead time | Use backup CNC vendor |
| Budget overrun >20% | Actual > $10,800 | Scope reduction (2 prototypes) |

---

## 8. RECEIVING & INSPECTION

### 8.1 Incoming Inspection Requirements

| Item | Inspection Level | Criteria |
|------|------------------|----------|
| Jetson Nano | Visual + power-on | Boot to desktop, no defects |
| IMX290 module | Visual + function | Image capture, focus check |
| OLED display | Visual + function | All pixels, brightness |
| Carrier PCB | Visual + electrical | No shorts, continuity |
| Housing | Dimensional | Per drawing ±0.1mm |
| Optics | Visual | No scratches, chips |
| Batteries | OCV + visual | 3.6-4.0V, no dents |

### 8.2 Receiving Log Template

| Date | Item | PO# | Qty | Supplier | Inspection | Status |
|------|------|-----|-----|----------|------------|--------|
| | | | | | | |

---

## 9. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| Procurement | | | |
| Engineering | | | |
| Program Manager | | | |

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-05 | Initial prototype procurement plan. 3 units, $9K budget, 8-week critical path. Long-lead items identified: Jetson, OLED, carrier PCB. Order deadline M5W1 for M9 delivery. |

---

*Product Spec: [[V-SMASH_LITE_product_spec|LITE Product Specification v1.1]]*
*Test Plan: [[V-SMASH_LITE_P4_test_plan|LITE Test Plan v1.0]]*
*FRU Specification: [[V-SMASH_LITE_FRU_specification|FRU Specification v1.0]]*
