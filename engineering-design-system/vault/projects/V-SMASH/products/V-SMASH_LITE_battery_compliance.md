---
project: V-SMASH
product: LITE
designation: VSM-L
phase: 4
type: compliance
version: 1.0
created: 2026-02-05
status: pending_verification
requirements: L-SAF-07, L-TRA-05
---

# V-SMASH LITE - BATTERY COMPLIANCE SPECIFICATION
## UN38.3 & IATA Transport Requirements

**Document ID:** VSM-L-BAT-COMP-001
**Version:** 1.0
**Requirements:** L-SAF-07, L-TRA-05

---

## 1. BATTERY SPECIFICATION

### 1.1 Cell Identification

| Parameter | Specification |
|-----------|---------------|
| **Part Number** | VSM-L-BAT-001 |
| **Cell Type** | 18650 cylindrical Li-ion |
| **Quantity per Unit** | 2 cells (series configuration) |
| **Chemistry** | Lithium Cobalt Oxide (LCO) / NMC |

### 1.2 Electrical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Nominal Voltage | 3.7V per cell | 7.4V pack |
| Capacity | 3,400 mAh per cell | 6,800 mAh pack |
| Energy | 12.58 Wh per cell | **25.16 Wh pack** |
| Max Charge Voltage | 4.2V per cell | 8.4V pack |
| Discharge Cut-off | 2.5V per cell | BMS protected |
| Max Continuous Discharge | 10A | 5C rate |
| Max Charge Current | 3.4A | 1C rate |

### 1.3 Physical Specifications

| Parameter | Value |
|-----------|-------|
| Cell Dimensions | 18.6mm × 65.2mm |
| Cell Weight | 48g (typical) |
| Pack Weight | 96g (2 cells) |
| Operating Temperature | -10°C to +55°C |
| Storage Temperature | -20°C to +45°C |

---

## 2. UN38.3 CERTIFICATION REQUIREMENTS

### 2.1 UN38.3 Overview

UN38.3 is the United Nations' standard for testing lithium batteries to ensure safe transport. All lithium batteries must pass these tests before international transport.

### 2.2 Required Tests (UN Manual of Tests and Criteria, Part III, Section 38.3)

| Test | Description | Pass Criteria |
|------|-------------|---------------|
| **T.1** | Altitude Simulation | No leakage, venting, disassembly, rupture, fire; OCV ≥90% |
| **T.2** | Thermal Test | No leakage, venting, disassembly, rupture, fire |
| **T.3** | Vibration | No leakage, venting, disassembly, rupture, fire; OCV ≥90% |
| **T.4** | Shock | No leakage, venting, disassembly, rupture, fire; OCV ≥90% |
| **T.5** | External Short Circuit | Case temp <170°C; no disassembly, rupture, fire |
| **T.6** | Impact/Crush | No fire (temp <170°C acceptable) |
| **T.7** | Overcharge | No disassembly, fire (cells >500g: no fire for 7 days) |
| **T.8** | Forced Discharge | No disassembly, fire |

### 2.3 Certification Documentation Required

| Document | Description | Status |
|----------|-------------|--------|
| **UN38.3 Test Summary** | Summary of all test results | ⬜ Required |
| **Test Report** | Detailed test data from accredited lab | ⬜ Required |
| **Cell Manufacturer CoC** | Certificate of Conformance | ⬜ Required |
| **MSDS/SDS** | Material Safety Data Sheet | ⬜ Required |

---

## 3. APPROVED BATTERY SUPPLIERS

### 3.1 Supplier Evaluation Criteria

| Criterion | Requirement | Weight |
|-----------|-------------|--------|
| UN38.3 Certified | Mandatory | Pass/Fail |
| Capacity ≥3,400 mAh | Mandatory | Pass/Fail |
| Quality consistency | ≤5% capacity variance | 30% |
| Price | ≤$4/cell | 25% |
| Lead time | ≤4 weeks | 20% |
| MOQ | ≤500 cells | 15% |
| Warranty | ≥1 year | 10% |

### 3.2 Evaluated Suppliers

| Supplier | Model | Capacity | UN38.3 | Price | Status |
|----------|-------|----------|--------|-------|--------|
| **Samsung SDI** | INR18650-35E | 3,500 mAh | ✅ Yes | $3.50 | ✅ **APPROVED** |
| **LG Chem** | INR18650-MJ1 | 3,500 mAh | ✅ Yes | $3.80 | ✅ **APPROVED** |
| **Panasonic** | NCR18650GA | 3,450 mAh | ✅ Yes | $4.20 | ✅ **APPROVED** |
| **Sony/Murata** | VTC6A | 3,000 mAh | ✅ Yes | $4.50 | ⚠️ Capacity low |
| **EVE Energy** | INR18650-35V | 3,500 mAh | ✅ Yes | $2.80 | ✅ **APPROVED** |
| Generic China | Various | 3,400 mAh | ❌ No cert | $1.50 | ❌ **REJECTED** |

### 3.3 Primary Supplier Selection

| Field | Value |
|-------|-------|
| **Primary Supplier** | Samsung SDI |
| **Model** | INR18650-35E |
| **Alternate 1** | LG Chem INR18650-MJ1 |
| **Alternate 2** | EVE Energy INR18650-35V |

---

## 4. UN38.3 VERIFICATION CHECKLIST

### 4.1 Documentation Verification

| Item | Document | Supplier | Received | Verified |
|------|----------|----------|----------|----------|
| 1 | UN38.3 Test Summary | Samsung SDI | ⬜ | ⬜ |
| 2 | Full Test Report | Samsung SDI | ⬜ | ⬜ |
| 3 | Certificate of Conformance | Samsung SDI | ⬜ | ⬜ |
| 4 | Material Safety Data Sheet | Samsung SDI | ⬜ | ⬜ |
| 5 | Cell specification datasheet | Samsung SDI | ⬜ | ⬜ |

### 4.2 Test Summary Requirements

The UN38.3 Test Summary must include:

- [ ] Name and address of test facility
- [ ] Name and address of applicant
- [ ] Unique test report identification
- [ ] Date of test report
- [ ] Description of cell/battery
- [ ] List of tests conducted
- [ ] Results of tests (pass/fail)
- [ ] Reference to assembled battery (if applicable)
- [ ] Signature of responsible party

### 4.3 Verification Actions

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Request UN38.3 docs from Samsung SDI | Procurement | Week 4 | ⬜ |
| Review test summary for completeness | QA | Week 5 | ⬜ |
| Verify test lab accreditation | QA | Week 5 | ⬜ |
| File certificates in QMS | QA | Week 5 | ⬜ |
| Update approved supplier list | Procurement | Week 5 | ⬜ |

---

## 5. IATA TRANSPORT COMPLIANCE

### 5.1 Classification

| Parameter | Value |
|-----------|-------|
| **UN Number** | UN3481 |
| **Proper Shipping Name** | Lithium ion batteries packed with equipment |
| **Class** | 9 (Miscellaneous dangerous goods) |
| **Packing Instruction** | PI 967, Section II |

### 5.2 PI 967 Section II Requirements

Section II applies because:
- Watt-hour rating: 25.16 Wh (≤100 Wh per battery) ✅
- Cells: 12.58 Wh each (≤20 Wh per cell) ✅
- Packed with equipment (not installed in) ✅

| Requirement | V-SMASH LITE Compliance |
|-------------|------------------------|
| Wh rating ≤100 Wh (battery) | ✅ 25.16 Wh |
| Wh rating ≤20 Wh (cell) | ✅ 12.58 Wh |
| State of charge ≤30% | ✅ Ship at 30% SoC |
| Protected against short circuit | ✅ Cells in holder, terminals covered |
| Strong outer packaging | ✅ Corrugated box |
| UN38.3 tested | ⬜ Pending verification |
| Quantity limits | ✅ 5 kg net per package |

### 5.3 Packaging Requirements

```
PACKAGING CONFIGURATION (PI 967 Section II)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│  OUTER PACKAGING (Corrugated Cardboard Box)                  │
│  UN Specification: 4G/4GV                                    │
│  Min. Dimensions: 250×150×150mm                              │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  INNER PACKAGING                                     │    │
│  │  ┌───────────────────────────────────────────────┐  │    │
│  │  │  V-SMASH LITE UNIT                            │  │    │
│  │  │  (in protective foam insert)                  │  │    │
│  │  └───────────────────────────────────────────────┘  │    │
│  │                                                      │    │
│  │  ┌───────────────┐  ┌───────────────┐               │    │
│  │  │ BATTERY       │  │ BATTERY       │               │    │
│  │  │ CELL #1       │  │ CELL #2       │               │    │
│  │  │ (in sleeve,   │  │ (in sleeve,   │               │    │
│  │  │ terminals     │  │ terminals     │               │    │
│  │  │ covered)      │  │ covered)      │               │    │
│  │  └───────────────┘  └───────────────┘               │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  LITHIUM BATTERY HANDLING LABEL (min. 120×110mm)            │
│  ┌──────────────────────────────────────┐                   │
│  │  [LITHIUM BATTERY SYMBOL]            │                   │
│  │  LITHIUM ION BATTERY                 │                   │
│  │  UN3481                              │                   │
│  │  FOR HANDLING INFORMATION            │                   │
│  │  CALL: [Emergency Phone]             │                   │
│  └──────────────────────────────────────┘                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5.4 Labeling Requirements

| Label | Size | Location | Required |
|-------|------|----------|----------|
| **Lithium Battery Handling Label** | 120×110mm min | Two opposite sides | ✅ Yes |
| **UN3481** | Within handling label | — | ✅ Yes |
| **Class 9 Label** | Not required (Sec II) | — | ❌ No |
| **Cargo Aircraft Only** | Not required (Sec II) | — | ❌ No |

### 5.5 Shipping Documentation

| Document | Required | Notes |
|----------|----------|-------|
| Air Waybill | ✅ Yes | "Lithium ion batteries in compliance with Section II of PI 967" |
| Shipper's Declaration | ❌ No | Not required for Section II |
| MSDS | ✅ Yes | Available upon request |

---

## 6. MARKING REQUIREMENTS

### 6.1 Product Marking (On V-SMASH LITE Unit)

| Marking | Location | Content |
|---------|----------|---------|
| Battery warning | Near battery door | ⚠️ LITHIUM-ION BATTERY |
| Watt-hour rating | Near battery door | 25.16 Wh |
| Polarity marking | Inside battery compartment | + / - symbols |
| Replacement part | Inside battery door | VSM-L-BAT-001 |

### 6.2 Battery Cell Marking

Cells must have manufacturer markings:
- [ ] Manufacturer name/logo
- [ ] Model number
- [ ] Nominal voltage (3.7V)
- [ ] Capacity (3400mAh / 3500mAh)
- [ ] Positive terminal identification

### 6.3 Packaging Marking

| Marking | Format | Example |
|---------|--------|---------|
| UN Number | UN + 4 digits | UN3481 |
| Proper Shipping Name | Text | LITHIUM ION BATTERIES PACKED WITH EQUIPMENT |
| Net quantity | kg | Net: 0.5 kg |
| Shipper info | Name, address | [Company details] |
| Emergency contact | Phone number | +84-XXX-XXX-XXXX |

---

## 7. BMS SAFETY REQUIREMENTS

### 7.1 Battery Management System Features

The V-SMASH LITE PMIC board (FRU-3) includes BMS with:

| Protection | Specification | Implementation |
|------------|---------------|----------------|
| **Overcharge** | Cutoff at 4.25V/cell | IC monitored |
| **Overdischarge** | Cutoff at 2.5V/cell | IC monitored |
| **Overcurrent** | Limit 10A | MOSFET + fuse |
| **Short Circuit** | <100μs response | MOSFET cutoff |
| **Overtemperature** | Cutoff at 60°C | NTC thermistor |
| **Cell Balancing** | Passive balancing | Resistor bleed |

### 7.2 Safety Certifications

| Certification | Standard | Status |
|---------------|----------|--------|
| UN38.3 | Transport safety | ⬜ Pending (cells) |
| IEC 62133 | Cell safety | ✅ Samsung certified |
| UL 2054 | Battery pack safety | ⬜ Optional |

---

## 8. PROCUREMENT SPECIFICATION

### 8.1 Purchase Specification

```
BATTERY CELL PROCUREMENT SPECIFICATION
Document: VSM-L-PROC-BAT-001

1. CELL REQUIREMENTS
   - Type: 18650 cylindrical lithium-ion
   - Chemistry: NMC or NCA
   - Capacity: ≥3,400 mAh (rated at 0.2C, 25°C)
   - Voltage: 3.6-3.7V nominal
   - Max discharge: ≥10A continuous

2. CERTIFICATION REQUIREMENTS
   - UN38.3 test summary: MANDATORY
   - UN38.3 full test report: Available on request
   - IEC 62133 certification: MANDATORY
   - RoHS compliance: MANDATORY (for export variants)

3. QUALITY REQUIREMENTS
   - Capacity variance: ≤5% within lot
   - Internal resistance: ≤25mΩ (1kHz AC)
   - Self-discharge: ≤3%/month at 25°C
   - Cycle life: ≥500 cycles to 80% capacity

4. DOCUMENTATION REQUIRED WITH SHIPMENT
   - Certificate of Conformance
   - Lot/batch number
   - Date of manufacture
   - UN38.3 test summary reference

5. PACKAGING
   - Individual cell sleeves
   - Positive terminal protection
   - Inner packaging preventing movement
   - Outer packaging per IATA PI 965

6. APPROVED MANUFACTURERS
   - Samsung SDI (Primary)
   - LG Chem (Alternate)
   - EVE Energy (Alternate)
```

### 8.2 Incoming Inspection

| Check | Method | Accept Criteria |
|-------|--------|-----------------|
| Visual | Inspect | No dents, leaks, rust |
| OCV | Multimeter | 3.6-4.1V |
| Capacity (sample) | Discharge test | ≥3,400 mAh |
| Documentation | Review | All certs present |

---

## 9. COMPLIANCE SUMMARY

### 9.1 Requirements Traceability

| Requirement | Specification | Compliance | Evidence |
|-------------|---------------|------------|----------|
| **L-SAF-07** | UN38.3 certified cells | ⬜ Pending | Supplier certificate |
| **L-TRA-05** | IATA PI967 compliant | ⬜ Pending | Packaging spec |
| **L-ENE-07** | 18650 Li-ion, replaceable | ✅ Verified | Design spec |
| **L-MNT-05** | Tool-free, <30 sec | ✅ Verified | FRU spec |

### 9.2 Verification Status

| Item | Status | Action Required |
|------|--------|-----------------|
| Cell supplier selected | ✅ Samsung SDI | None |
| UN38.3 certificate obtained | ⬜ Pending | Request from supplier |
| IATA packaging designed | ✅ Complete | None |
| Labeling designed | ✅ Complete | None |
| BMS safety verified | ✅ Design complete | Test at qualification |
| Documentation filed | ⬜ Pending | File when received |

---

## 10. ACTION ITEMS

| # | Action | Owner | Due | Status |
|---|--------|-------|-----|--------|
| 1 | Contact Samsung SDI for UN38.3 documentation | Procurement | Week 4 | ⬜ |
| 2 | Request test summary and CoC | Procurement | Week 4 | ⬜ |
| 3 | Verify test lab accreditation | QA | Week 5 | ⬜ |
| 4 | Order sample cells for incoming inspection | Procurement | Week 4 | ⬜ |
| 5 | Design and order lithium battery labels | Packaging | Week 6 | ⬜ |
| 6 | Update shipping procedures | Logistics | Week 6 | ⬜ |
| 7 | File all certificates in QMS | QA | Week 6 | ⬜ |
| 8 | Brief shipping team on IATA requirements | Logistics | Week 7 | ⬜ |

---

## 11. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| Procurement | | | |
| Quality | | | |
| Safety | | | |

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-05 | Initial battery compliance specification. Defined UN38.3 requirements, selected Samsung SDI as primary supplier, documented IATA PI967 Section II packaging requirements, created verification checklist. |

---

## APPENDIX A: LITHIUM BATTERY HANDLING LABEL

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│      ████████████████████████████████████████████          │
│      █                                          █          │
│      █     ┌────────────────────────────┐      █          │
│      █     │    ⚡ CAUTION ⚡           │      █          │
│      █     │                            │      █          │
│      █     │   LITHIUM ION BATTERY      │      █          │
│      █     │                            │      █          │
│      █     │   UN3481                   │      █          │
│      █     │                            │      █          │
│      █     └────────────────────────────┘      █          │
│      █                                          █          │
│      █   For handling information, contact:     █          │
│      █   [Company Name]                         █          │
│      █   Tel: +84-XXX-XXX-XXXX                  █          │
│      █                                          █          │
│      ████████████████████████████████████████████          │
│                                                            │
│   Minimum size: 120mm × 110mm                              │
│   Border: Red hatched (alternating red/white)              │
│   Symbol: Black on white background                        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

*Requirements Source: [[V-SMASH_LITE_P1_requirements_list|LITE Requirements List v1.0]]*
*FRU Specification: [[V-SMASH_LITE_FRU_specification|FRU Specification v1.0]]*
