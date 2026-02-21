---
project: VN-SMH-LITE
designation: V-SMASH LITE
type: quality_control_plan
version: 1.0
created: 2026-02-05
status: active
standard: IPC-A-610 Class 2
---

# V-SMASH LITE QUALITY CONTROL PLAN
## Production Quality Assurance

**Project:** VN-SMH-LITE (V-SMASH LITE)
**Document:** Quality Control Plan
**Version:** 1.0
**Date:** 2026-02-05
**Standard:** IPC-A-610 Class 2

---

## 1. QUALITY OBJECTIVES

### 1.1 Key Quality Metrics

| Metric | Target | Measurement | Frequency |
|--------|--------|-------------|-----------|
| **Production Defect Rate** | ≤2% | Defective units / Total produced | Per batch |
| **First Pass Yield (FPY)** | ≥95% | Units passing first inspection | Per batch |
| **Design Life** | 10 years | MTBF analysis + accelerated testing | Per design |
| **Software Defect Rate** | ≤1 critical/1000 LOC | Static analysis + testing | Per release |
| **Customer Returns** | ≤1% | Returns / Units shipped | Monthly |
| **Field Failure Rate** | ≤0.5%/year | Field failures / Deployed units | Annually |

### 1.2 Quality Standards

| Standard | Scope | Application |
|----------|-------|-------------|
| **IPC-A-610 Class 2** | Electronics assembly | PCB inspection, soldering |
| **IPC-J-STD-001 Class 2** | Soldering requirements | Process qualification |
| **MIL-STD-810H** | Environmental testing | Qualification testing |
| **MIL-STD-882E** | Safety analysis | Hazard assessment |
| **ISO 9001:2015** | Quality management | Overall QMS |

---

## 2. PRODUCTION DEFECT RATE CONTROL

### 2.1 Defect Categories

```
DEFECT CLASSIFICATION
═══════════════════════════════════════════════════════════════════════════

CATEGORY A: CRITICAL (Immediate rejection)
───────────────────────────────────────────────────────────────────────────
• Safety-related defects
• Functional failure
• Missing critical components
• Structural integrity issues

CATEGORY B: MAJOR (Rework required)
───────────────────────────────────────────────────────────────────────────
• Dimensional out of tolerance
• Cosmetic defects affecting function
• Incorrect component values
• Insufficient solder joints

CATEGORY C: MINOR (Accept with deviation)
───────────────────────────────────────────────────────────────────────────
• Minor cosmetic issues
• Non-critical dimensional variation
• Documentation errors
• Packaging defects

═══════════════════════════════════════════════════════════════════════════
```

### 2.2 Defect Rate Calculation

```
DEFECT RATE FORMULA
═══════════════════════════════════════════════════════════════════════════

                    Number of Defective Units
Defect Rate (%) = ─────────────────────────── × 100
                    Total Units Inspected

TARGET: ≤2%

EXAMPLE:
If 100 units inspected, maximum 2 defective units allowed

BREAKDOWN BY CATEGORY:
• Category A defects: 0 allowed (reject batch if any)
• Category B defects: ≤1% (1 per 100 units)
• Category C defects: ≤1% (1 per 100 units)

═══════════════════════════════════════════════════════════════════════════
```

### 2.3 Statistical Process Control (SPC)

| Parameter | Control Limit | Action |
|-----------|---------------|--------|
| Defect rate | >2% | Stop production, investigate |
| FPY | <95% | Process review |
| Trend (3 batches) | Rising | Root cause analysis |
| Single critical defect | Any | Quarantine batch |

---

## 3. DESIGN LIFE SPECIFICATION

### 3.1 Design Life Requirements

```
DESIGN LIFE: 10 YEARS
═══════════════════════════════════════════════════════════════════════════

OPERATING CONDITIONS:
───────────────────────────────────────────────────────────────────────────
• Temperature: -10 to +55°C operating
• Storage: -40 to +70°C
• Humidity: Up to 95% RH non-condensing
• Vibration: Per MIL-STD-810H Method 514
• Shock: Per MIL-STD-810H Method 516 (1m drop)

USAGE PROFILE:
───────────────────────────────────────────────────────────────────────────
• Operating hours: 500 hours/year
• Total design life: 5,000 operating hours
• Firing cycles: 2,000 lifetime
• Power cycles: 10,000 lifetime

RELIABILITY TARGETS:
───────────────────────────────────────────────────────────────────────────
• MTBF: ≥2,000 hours (mean time between failures)
• MTTR: ≤30 minutes (mean time to repair)
• Availability: ≥98%

═══════════════════════════════════════════════════════════════════════════
```

### 3.2 Life Testing Requirements

| Test | Duration | Sample Size | Pass Criteria |
|------|----------|-------------|---------------|
| Accelerated life | 1,000 hours @ 70°C | 3 units | No failures |
| Vibration endurance | 500 hours | 3 units | No degradation |
| Cycle testing | 5,000 cycles | 3 units | <5% drift |
| Storage aging | 6 months @ 70°C | 3 units | Full function |

### 3.3 Component Derating

| Component Type | Derating Factor | Notes |
|----------------|-----------------|-------|
| Resistors | 50% power | Extend life |
| Capacitors | 80% voltage | Electrolytic especially |
| Semiconductors | 70% junction temp | Add thermal margin |
| Connectors | 50% current | Reduce contact wear |
| Batteries | 80% capacity | Account for aging |

---

## 4. SOFTWARE DEFECT RATE CONTROL

### 4.1 Software Quality Metrics

```
SOFTWARE DEFECT RATE TARGET
═══════════════════════════════════════════════════════════════════════════

TARGET: ≤1 critical defect per 1,000 lines of code (LOC)

DEFECT SEVERITY:
───────────────────────────────────────────────────────────────────────────
CRITICAL: Safety impact, system crash, data loss
          Target: ≤1 per 1,000 LOC
          Allowed in production: 0

MAJOR:    Feature not working, significant workaround needed
          Target: ≤3 per 1,000 LOC

MINOR:    Cosmetic, minor inconvenience
          Target: ≤10 per 1,000 LOC

MEASUREMENT:
───────────────────────────────────────────────────────────────────────────
Defect Density = Total Defects Found / KLOC (thousands of lines of code)

═══════════════════════════════════════════════════════════════════════════
```

### 4.2 Software Quality Gates

| Gate | Requirement | Tool/Method |
|------|-------------|-------------|
| **Code Review** | 100% of changes reviewed | Peer review |
| **Static Analysis** | 0 critical warnings | SonarQube, Coverity |
| **Unit Test Coverage** | ≥80% | pytest, gtest |
| **Integration Test** | 100% requirements covered | Test matrix |
| **System Test** | All use cases passed | Test procedures |
| **Security Scan** | 0 high/critical vulnerabilities | OWASP, Bandit |

### 4.3 Software Testing Requirements

```
SOFTWARE TEST MATRIX
═══════════════════════════════════════════════════════════════════════════

TEST LEVEL          COVERAGE TARGET    EXECUTION
───────────────────────────────────────────────────────────────────────────
Unit Testing        ≥80% code          Every commit
Integration Testing 100% interfaces    Every build
System Testing      100% requirements  Every release
Regression Testing  100% prior tests   Every release
Performance Testing Response times     Major releases
Security Testing    OWASP Top 10       Major releases

ACCEPTANCE CRITERIA:
───────────────────────────────────────────────────────────────────────────
• All critical tests: PASS
• Major tests: ≥95% PASS
• Minor tests: ≥90% PASS
• No known critical defects in production

═══════════════════════════════════════════════════════════════════════════
```

---

## 5. IPC-A-610 CLASS 2 INSPECTION CRITERIA

### 5.1 Solder Joint Inspection

```
SOLDER JOINT CRITERIA (IPC-A-610 Class 2)
═══════════════════════════════════════════════════════════════════════════

ACCEPTABLE:
───────────────────────────────────────────────────────────────────────────
• Smooth, shiny or satin finish
• Wetting to both pad and lead
• Fillet visible on both sides
• No voids >25% of joint area
• Lead visible through solder (through-hole)

     ┌─────────────────┐
     │    GOOD JOINT   │
     │    ╱╲    ╱╲     │
     │   ╱  ╲  ╱  ╲    │  ← Smooth fillet
     │  ╱    ╲╱    ╲   │
     │ ╱      │      ╲ │
     └────────┴────────┘
            Lead

DEFECT (REJECT):
───────────────────────────────────────────────────────────────────────────
• Cold solder (dull, grainy)
• Insufficient solder (no fillet)
• Excess solder (bridging)
• Solder balls
• Cracked joints
• No wetting (dewetting)

     ┌─────────────────┐
     │   COLD JOINT    │
     │    ▓▓▓▓▓▓▓▓     │
     │   ▓▓▓▓▓▓▓▓▓▓    │  ← Dull, grainy
     │  ▓▓▓▓▓▓▓▓▓▓▓▓   │
     └─────────────────┘

═══════════════════════════════════════════════════════════════════════════
```

### 5.2 Component Placement

| Criteria | Class 2 Requirement | Inspection Method |
|----------|---------------------|-------------------|
| Offset (chip) | ≤50% of width | Visual / microscope |
| Rotation | ≤5° | Visual |
| Tombstone | Not allowed | Visual |
| Missing | Not allowed | Visual / AOI |
| Wrong value | Not allowed | LCR meter |
| Polarity | Correct orientation | Visual |

### 5.3 PCB Inspection Checklist

```
PCB INSPECTION CHECKLIST (IPC-A-610 Class 2)
═══════════════════════════════════════════════════════════════════════════

VISUAL INSPECTION:
───────────────────────────────────────────────────────────────────────────
☐ Board identification correct
☐ No physical damage (cracks, chips)
☐ Solder mask intact
☐ All components present
☐ Component orientation correct
☐ No foreign material (flux residue, debris)

SOLDER JOINTS:
───────────────────────────────────────────────────────────────────────────
☐ All joints wetted properly
☐ No cold solder joints
☐ No bridges between pads
☐ No solder balls
☐ Through-hole leads visible
☐ SMT joints have proper fillets

COMPONENT PLACEMENT:
───────────────────────────────────────────────────────────────────────────
☐ Components within placement tolerance
☐ No lifted leads
☐ No tombstoned components
☐ Connectors seated fully
☐ Heat sinks properly attached

MECHANICAL:
───────────────────────────────────────────────────────────────────────────
☐ Mounting holes clear
☐ Edge connectors clean
☐ No bent pins on connectors
☐ Conformal coating (if applicable) complete

═══════════════════════════════════════════════════════════════════════════
```

---

## 6. INSPECTION PROCEDURES

### 6.1 Incoming Inspection

```
INCOMING MATERIAL INSPECTION
═══════════════════════════════════════════════════════════════════════════

SAMPLING PLAN: AQL 1.0 (Acceptable Quality Level)
───────────────────────────────────────────────────────────────────────────
Lot Size        Sample Size     Accept      Reject
2-8             2               0           1
9-15            3               0           1
16-25           5               0           1
26-50           8               0           1
51-90           13              1           2
91-150          20              1           2
151-280         32              2           3
281-500         50              3           4

INSPECTION CRITERIA:
───────────────────────────────────────────────────────────────────────────
☐ Quantity matches packing list
☐ Part numbers correct
☐ Date codes acceptable (not expired)
☐ No physical damage
☐ Certificates of conformance (CoC) present
☐ Critical parameters verified (for key components)

═══════════════════════════════════════════════════════════════════════════
```

### 6.2 In-Process Inspection

| Stage | Inspection Point | Method | Record |
|-------|------------------|--------|--------|
| SMT Paste | Stencil alignment, volume | SPI | Auto log |
| SMT Placement | Component presence, orientation | AOI | Auto log |
| Reflow | Profile compliance | Profiler | Chart |
| Through-hole | Component placement | Visual | Checklist |
| Wave/Hand solder | Joint quality | Visual | Checklist |
| Assembly | Mechanical assembly | Checklist | Form |

### 6.3 Final Inspection

```
FINAL INSPECTION CHECKLIST
═══════════════════════════════════════════════════════════════════════════

UNIT SERIAL NUMBER: ____________________

VISUAL INSPECTION:
───────────────────────────────────────────────────────────────────────────
☐ Exterior clean, no damage
☐ All labels present and correct
☐ All fasteners torqued
☐ All covers/panels secure
☐ Serial number matches documentation

FUNCTIONAL TEST:
───────────────────────────────────────────────────────────────────────────
☐ Power-on sequence correct
☐ Self-test passes (no error codes)
☐ All indicators function
☐ Safety interlock verified
☐ Communication verified (if applicable)
☐ Calibration verified (if applicable)

ELECTRICAL TEST:
───────────────────────────────────────────────────────────────────────────
☐ Input voltage range tested
☐ Current consumption within spec
☐ Output signals verified
☐ Insulation resistance (if applicable)
☐ Hi-pot test (if applicable)

DOCUMENTATION:
───────────────────────────────────────────────────────────────────────────
☐ Test data recorded
☐ Calibration certificate (if applicable)
☐ User manual included
☐ Warranty card included

RESULT:        ☐ PASS    ☐ FAIL    ☐ REWORK

Inspector: _________________ Date: _____________ Signature: _____________

═══════════════════════════════════════════════════════════════════════════
```

---

## 7. NON-CONFORMANCE MANAGEMENT

### 7.1 Non-Conformance Reporting (NCR)

```
NON-CONFORMANCE REPORT (NCR)
═══════════════════════════════════════════════════════════════════════════

NCR Number: NCR-________    Date: ____________

IDENTIFICATION:
───────────────────────────────────────────────────────────────────────────
Product: ________________________    Serial/Lot: ________________________
Stage detected: ☐ Incoming  ☐ In-process  ☐ Final  ☐ Field

DESCRIPTION OF NON-CONFORMANCE:
───────────────────────────────────────────────────────────────────────────
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________

Defect Category: ☐ Critical (A)  ☐ Major (B)  ☐ Minor (C)

DISPOSITION:
───────────────────────────────────────────────────────────────────────────
☐ Use As-Is (MRB approval required for Cat A/B)
☐ Rework (procedure attached)
☐ Repair (procedure attached)
☐ Scrap
☐ Return to Supplier

ROOT CAUSE ANALYSIS:
───────────────────────────────────────────────────────────────────────────
________________________________________________________________________
________________________________________________________________________

CORRECTIVE ACTION:
───────────────────────────────────────────────────────────────────────────
________________________________________________________________________
________________________________________________________________________

VERIFICATION OF CORRECTIVE ACTION:
───────────────────────────────────────────────────────────────────────────
Date: ____________  Verified by: ________________  Effective: ☐ Yes  ☐ No

═══════════════════════════════════════════════════════════════════════════
```

### 7.2 Material Review Board (MRB)

| NCR Category | MRB Required | Approval Authority |
|--------------|--------------|-------------------|
| Critical (A) | Yes | Engineering + QA Manager |
| Major (B) - Use As-Is | Yes | QA Manager |
| Major (B) - Rework | No | QA Inspector |
| Minor (C) | No | QA Inspector |

---

## 8. QUALITY RECORDS

### 8.1 Required Records

| Record Type | Retention | Format |
|-------------|-----------|--------|
| Incoming inspection | 5 years | Paper/Electronic |
| In-process inspection | 5 years | Electronic |
| Final test data | Product life + 5 years | Electronic |
| Calibration records | 5 years | Paper/Electronic |
| Non-conformance reports | 5 years | Paper/Electronic |
| Corrective actions | 5 years | Paper/Electronic |
| Training records | Employment + 5 years | Paper |

### 8.2 Traceability

```
TRACEABILITY REQUIREMENTS
═══════════════════════════════════════════════════════════════════════════

UNIT LEVEL:
───────────────────────────────────────────────────────────────────────────
• Unique serial number per unit
• Build date recorded
• Test data linked to serial number
• Configuration (hardware/software revision) recorded

LOT LEVEL:
───────────────────────────────────────────────────────────────────────────
• Component lot codes recorded
• Supplier lot traceability
• Process batch traceability

MINIMUM TRACEABLE INFORMATION:
───────────────────────────────────────────────────────────────────────────
Serial Number → Build Date → PCB Lot → Critical Component Lots
                          → Software Version
                          → Test Data
                          → Inspector ID

═══════════════════════════════════════════════════════════════════════════
```

---

## 9. CONTINUOUS IMPROVEMENT

### 9.1 Quality Metrics Dashboard

```
MONTHLY QUALITY DASHBOARD
═══════════════════════════════════════════════════════════════════════════

METRIC                  TARGET      ACTUAL      STATUS
───────────────────────────────────────────────────────────────────────────
Production Defect Rate  ≤2.0%       ____%       ☐ PASS  ☐ FAIL
First Pass Yield        ≥95%        ____%       ☐ PASS  ☐ FAIL
Customer Returns        ≤1.0%       ____%       ☐ PASS  ☐ FAIL
Supplier Quality        ≤1.0% rej   ____%       ☐ PASS  ☐ FAIL
NCRs Open >30 days      0           ____        ☐ PASS  ☐ FAIL
Corrective Actions      100% on time ____%      ☐ PASS  ☐ FAIL

TREND:
───────────────────────────────────────────────────────────────────────────
Defect Rate (last 6 months):
  ____% → ____% → ____% → ____% → ____% → ____%
         (improving ↓ / stable → / worsening ↑)

TOP 3 DEFECT TYPES THIS MONTH:
───────────────────────────────────────────────────────────────────────────
1. _________________________________ (____%)
2. _________________________________ (____%)
3. _________________________________ (____%)

═══════════════════════════════════════════════════════════════════════════
```

### 9.2 Corrective Action Process

```
CORRECTIVE ACTION FLOW
═══════════════════════════════════════════════════════════════════════════

    ┌─────────────────┐
    │ Issue Identified│
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Containment     │ ← Immediate action to stop defects
    │ (24 hours)      │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Root Cause      │ ← 5-Why analysis, fishbone diagram
    │ Analysis        │
    │ (7 days)        │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Corrective      │ ← Address root cause
    │ Action          │
    │ (14 days)       │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Verification    │ ← Confirm effectiveness
    │ (30 days)       │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Close & Document│
    └─────────────────┘

═══════════════════════════════════════════════════════════════════════════
```

---

## 10. DOCUMENT CONTROL

### 10.1 Document Approval

| Role | Responsibility |
|------|----------------|
| QA Manager | Approve QC plan, procedures |
| Engineering | Technical review |
| Production | Process feasibility |
| Management | Resource allocation |

### 10.2 Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| **1.0** | **2026-02-05** | **Initial release. Added defect rate (≤2%), design life (10 years), software defect rate (≤1/KLOC), IPC-A-610 Class 2.** | |

---

## 11. APPENDICES

### Appendix A: Defect Code List

| Code | Description | Category |
|------|-------------|----------|
| D001 | Cold solder joint | B |
| D002 | Solder bridge | B |
| D003 | Missing component | A |
| D004 | Wrong component | A |
| D005 | Component reversed | A |
| D006 | Insufficient solder | B |
| D007 | Solder ball | C |
| D008 | Damaged component | B |
| D009 | Misaligned component | B/C |
| D010 | Foreign material | C |
| D011 | Cracked PCB | A |
| D012 | Scratched surface | C |
| D013 | Label defect | C |
| D014 | Functional failure | A |
| D015 | Calibration out of spec | B |

### Appendix B: Equipment Calibration Schedule

| Equipment | Calibration Interval | Standard |
|-----------|---------------------|----------|
| Multimeter | 12 months | NIST traceable |
| Oscilloscope | 12 months | NIST traceable |
| Power supply | 12 months | NIST traceable |
| Soldering station | 6 months | Internal |
| Torque wrench | 12 months | NIST traceable |
| Microscope | 24 months | Internal |
| AOI machine | 6 months | Internal |

---

*V-SMASH LITE Quality Control Plan - Ensuring ≤2% defect rate and 10-year design life*
