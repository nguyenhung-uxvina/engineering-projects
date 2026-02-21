---
project: VN-RNG-001
phase: 1
type: requirements_validation
version: 1.0
created: 2026-02-09
status: draft
---

# Requirements Validation Report: VN-RNG-001

---

## 1. Validation Summary

| Check | Target | Actual | Status |
|-------|--------|--------|--------|
| Total requirements | 100-150 (full system) | **120** | PASS |
| MUST requirements | — | **70** (58%) | — |
| WISH requirements | — | **50** (42%) | — |
| Categories covered | 16/16 | **16/16** | PASS |
| MUST quantified % | >=80% | **94%** | PASS |
| Verification methods assigned | 100% of MUST | **100%** | PASS |
| Standards mapped | All applicable | **11 standards** | PASS |
| Unresolved conflicts | 0 | **0** | PASS |
| ODI top 25 coverage | 100% | **100% (21 full + 4 partial)** | PASS |
| Stakeholder review | Complete | **Complete** | PASS |

**Overall: PASS -- Ready for Gate 1 review**

---

## 2. Category Completeness Check

| # | Category | Count | MUST | WISH | Quant % | Verify 100% | Status | Notes |
|---|----------|-------|------|------|---------|-------------|--------|-------|
| 1 | Geometry | 9 | 5 | 4 | 100% | Yes | PASS | Detection zone, sensor count, array geometry fully specified |
| 2 | Kinematics | 7 | 4 | 3 | 100% | Yes | PASS | Velocity, rate, latency, angles all quantified |
| 3 | Forces | 5 | 3 | 2 | 100% | Yes | PASS | MIL-STD-810H shock/vibration, ballistic protection |
| 4 | Energy | 7 | 4 | 3 | 100% | Yes | PASS | 12V DC, battery 10h+, consumption <=8W |
| 5 | Material | 7 | 4 | 3 | 86% | Yes | PASS | MAT-006 (gasket material) is qualitative — acceptable for gasket spec |
| 6 | Signals | 11 | 7 | 4 | 91% | Yes | PASS | SIG-008 (lane discrimination) needs detailed algorithm spec in Phase 2 |
| 7 | Safety | 7 | 5 | 2 | 86% | Yes | PASS | SAF-004 (fail-safe) is qualitative but appropriate for safety principle |
| 8 | Ergonomics | 8 | 4 | 4 | 88% | Yes | PASS | ERG-008 (audio/visual alert) is qualitative — acceptable |
| 9 | Production | 7 | 4 | 3 | 86% | Yes | PASS | PRD-006 (skill level) references IPC standard — quantified via standard |
| 10 | Quality | 9 | 5 | 4 | 100% | Yes | PASS | Accuracy zone-graded (Polytronic lesson), detection rate, MTBF |
| 11 | Assembly | 6 | 3 | 3 | 83% | Yes | PASS | ASM-006 (cable lengths) is catalog spec — acceptable |
| 12 | Transport | 5 | 3 | 2 | 100% | Yes | PASS | Man-portable 25kg, transit case, vehicle transport |
| 13 | Operation | 10 | 6 | 4 | 100% | Yes | PASS | Full MIL-STD-810H environmental coverage |
| 14 | Maintenance | 8 | 4 | 4 | 88% | Yes | PASS | MTTR, BIT, calibration interval, remote diagnostics |
| 15 | Costs | 8 | 5 | 3 | 100% | Yes | PASS | Unit cost, BOM cost, LCC, development cost all quantified |
| 16 | Schedule | 6 | 4 | 2 | 100% | Yes | PASS | Prototype, pilot, production, variant timelines |

**All 16 categories: PASS**

---

## 3. Quantification Analysis

### Overall: 113/120 = 94% quantified (target >=80%)

| Quantification Level | Count | % | Examples |
|---------------------|-------|---|---------|
| **Fully quantified** (numeric with tolerance) | 95 | 79% | QUA-001: <=5mm radial; KIN-004: <=100ms; ENE-004: >=10h |
| **Quantified via standard reference** | 18 | 15% | FOR-001: MIL-STD-810H Method 514.8; SAF-002: UN 38.3 |
| **Qualitative but acceptable** | 7 | 6% | SAF-004: fail-safe principle; ERG-008: configurable alert |
| **Total quantified** | **113** | **94%** | |
| **Qualitative** | **7** | **6%** | All are WISH or safety principles — acceptable |

### Unquantified Requirements (7)

| ID | Requirement | Why Acceptable |
|----|-------------|---------------|
| MAT-006 | Gasket material (silicone/EPDM) | Material specification, not a numeric target |
| SAF-004 | Fail-safe operation | Safety design principle; FMEA (SAF-005) quantifies specific failure modes |
| SAF-007 | Warning labels bilingual | Label content specification, not numeric |
| ERG-008 | Audio/visual shot alert | UX feature; detailed in software spec |
| PRD-006 | Assembly skill level (IPC-A-610 Class 2) | Quantified via industry workmanship standard |
| ASM-006 | Cable length options | Catalog specification |
| MNT-007 | Remote diagnostics | Feature specification; detailed in software spec |

**Assessment: All 7 unquantified requirements are appropriately specified. No action needed.**

---

## 4. Verification Method Distribution

| Method | Count | % | Notes |
|--------|-------|---|-------|
| **Test (T)** | 58 | 48% | Environmental, accuracy, EMC, IP67, functional |
| **Inspection (I)** | 24 | 20% | Dimensions, materials, labels, workmanship |
| **Demonstration (D)** | 20 | 17% | Field trials, user operation, installation |
| **Analysis (A)** | 18 | 15% | Cost analysis, MTBF prediction, FMEA, FTO |
| **Total** | **120** | **100%** | |

### Verification Feasibility Check

| Concern | Requirements | Assessment | Mitigation |
|---------|-------------|------------|------------|
| MIL-STD-810H testing requires accredited lab | OPR-001 to OPR-006, FOR-001, FOR-002 | Medium cost ($20-30K) | Budget allocated in verification plan ($40K for test) |
| EMC testing (MIL-STD-461G) requires shielded chamber | SIG-011 | Specialized facility needed | Contract with Vietnamese or regional EMC test lab |
| Accuracy testing requires live-fire range access | QUA-001 to QUA-006, KIN-001 to KIN-005 | Requires VPA range access | Coordinate through customer stakeholder (S1) |
| MTBF prediction requires component data | QUA-007 | Analysis method (MIL-HDBK-217F) | Component datasheets available; standard prediction methodology |
| IP67 testing | OPR-004, OPR-005 | Standard test equipment | In-house or test lab; relatively low cost |

**Assessment: All verification methods are feasible. No blocking issues.**

---

## 5. Conflict Analysis

### Identified and Resolved Conflicts (5)

| # | Conflict | Requirements | Resolution | Validated? |
|---|----------|-------------|------------|-----------|
| 1 | Weight vs Ballistic Protection | GEO-004 (<=12kg) vs FOR-003 (ballistic survival) | Aluminum enclosure + AR500 plate only in direct-fire path; FEA analysis in Phase 2 to confirm | Yes — RE data shows Saab achieves ~10kg with steel; aluminum will be lighter |
| 2 | Battery Life vs Weight | ENE-004 (>=10h) vs TRP-001 (<=25kg total kit) | Design for 5W avg consumption; 100Wh battery (~0.6kg LiPo) gives 20h; total kit easily <25kg | Yes — power budget analysis confirms feasibility |
| 3 | Cost vs Accuracy | CST-004 (<=$900 BOM) vs QUA-001 (<=5mm) | COTS MEMS ($3-5 ea) + GCC-PHAT proven to achieve <5mm; ShotMarker achieves 1-3mm with COTS | Yes — RE analysis + firmware implementation confirm |
| 4 | Detection Rate vs Cost | KIN-002 (1200 RPM) vs KIN-003 (2000 RPM wish) vs CST-004 | 1200 RPM achievable on STM32H7 at current BOM; 2000 RPM is WISH requiring FPGA ($50-100 adder) | Yes — KIN-003 is WISH, not MUST; no conflict |
| 5 | Portability vs Multi-Lane | TRP-001 (man-portable) vs OPR-010 (16+ lanes) | Modular platform: each sensor bar independent; portable = 1-4 lanes; multi-lane = rack controller | Yes — platform architecture resolves |

**Unresolved conflicts: 0**

---

## 6. ODI Traceability Validation

### EXTREME Opportunities (Opp >15) — All 11 Covered

| # | Outcome | Opp Score | Requirements | Coverage |
|---|---------|-----------|-------------|----------|
| 1 | O-27: Shot-to-display latency | 17.1 | KIN-004, SIG-009 | FULL |
| 2 | O-28: Lanes per instructor | 17.0 | ERG-004, SIG-002, OPR-010 | FULL |
| 3 | O-26: Shot placement accuracy | 16.5 | QUA-001/002/003/006, SIG-005/006/007, GEO-007/008 | FULL |
| 4 | O-66: Vendor independence | 16.5 | PRD-001/004/005, SIG-004, MNT-005/008, ERG-003 | FULL |
| 5 | O-33: Error pattern identification | 16.4 | ERG-004 + software spec (TBD-004) | PARTIAL — software-heavy |
| 6 | O-43: Cross-session tracking | 16.1 | SIG-010 + software spec (TBD-004) | PARTIAL — software-heavy |
| 7 | O-42: Corrective feedback time | 16.0 | KIN-004, ERG-004/007/008 | FULL |
| 8 | O-34: Coaching effectiveness | 15.5 | ERG-004/007/008, KIN-004 + software spec | FULL (HW) + PARTIAL (SW) |
| 9 | O-29: Missed detection rate | 15.4 | QUA-004, GEO-007, KIN-001 | FULL |
| 10 | O-54: Record generation time | 15.0 | SIG-010 + software spec (TBD-004) | PARTIAL — software-heavy |
| 11 | O-68: Tropical heat reliability | 15.0 | OPR-001/006, MAT-001/004, ENE-005 | FULL |

### Gap: Software Requirements Specification Needed

4 of 11 EXTREME opportunities are **partially covered** because they are primarily software features:
- O-33: AI error pattern detection
- O-43: Cross-session database and tracking
- O-34: Coaching effectiveness analytics (software portion)
- O-54: Automated report generation

**Action: TBD-004 (Software Requirements Specification) should be completed before or during Phase 2 to fully cover these outcomes.**

This is acceptable for Phase 1 gate because:
1. Hardware requirements to support these features ARE specified (processing power, storage, connectivity)
2. Software specification is typically developed in parallel with conceptual design
3. All 11 EXTREME outcomes have at least partial hardware coverage

### HIGH Opportunities (Opp 12-15) — All 14 Covered

All 14 HIGH-priority outcomes are traced to specific requirements with FULL coverage. See ODI Traceability Matrix in requirements list Section 6.

---

## 7. Standards Compliance Validation

| Standard | Requirements Mapped | Gap? | Action |
|----------|---------------------|------|--------|
| MIL-STD-810H | OPR-001 to OPR-006, FOR-001, FOR-002, MAT-002 | No | Full test program budgeted |
| MIL-STD-461G | SIG-011 | No | EMC test lab identified |
| MIL-STD-882E | SAF-004, SAF-005 | No | FMEA in Phase 2 |
| IEC 60529 | OPR-004, OPR-005 | No | IP67 test straightforward |
| IEC 62368-1 | SAF-001 | No | Low-voltage design inherent |
| IEEE 802.3 | SIG-001, ENE-003 | No | Standard Ethernet PHY |
| IEEE 802.11 | SIG-002 | No | WiFi module certified |
| UN 38.3 | SAF-002, TRP-004 | No | Battery supplier provides cert |
| IPC-CC-830C | MAT-004 | No | Conformal coating process |
| IPC-A-610 | PRD-006 | No | Workmanship training |
| **TCVN** | **TBD** | **YES** | **TBD-002: Identify applicable TCVN standards by Q2 2026** |

**Gap: TCVN standards mapping is incomplete (TBD-002). This is acceptable for Phase 1 gate because:**
1. MIL-STD requirements provide conservative baseline
2. TCVN typically maps to IEC/ISO equivalents
3. TBD-002 has owner and target date assigned

---

## 8. Stakeholder Coverage Validation

| Stakeholder | Key Needs | Requirements Coverage | Status |
|------------|-----------|----------------------|--------|
| S1: Customer (Procurement) | Cost, local content, schedule | CST-001 to CST-005, PRD-001, SCH-001 to SCH-004 | FULL |
| S2: User (Instructor) | Latency, accuracy, multi-lane, training | KIN-004, QUA-001, ERG-004, ERG-001 | FULL |
| S2b: User (Shooter) | Display, readability, intuitive | ERG-005, SIG-009, GEO-009 | FULL |
| S3: Regulator | Safety, compliance | SAF-001 to SAF-007, standards matrix | FULL |
| S4: Maintainer | MTTR, diagnostics, spares | MNT-001 to MNT-008, ASM-004 | FULL |
| S5: Manufacturer | DFM, local content, tolerances | PRD-001 to PRD-007, MAT-001 | FULL |
| S6: Dev Team | Clear specs, test access | All quantified requirements; TBD-005 (range access) | FULL |
| S7: Standards Body | TCVN compliance | TBD-002 (pending) | PARTIAL |
| S8: Higher Command | Training effectiveness | QUA-009, SIG-010 | FULL |

---

## 9. Open Items Summary

| Priority | ID | Description | Owner | Target | Impact on Gate |
|----------|-----|-------------|-------|--------|---------------|
| HIGH | TBD-002 | TCVN standard mapping | Standards researcher | Q2 2026 | Non-blocking (MIL-STD baseline covers) |
| HIGH | TBD-004 | Software requirements specification | Software lead | Phase 1.5/2 | Non-blocking (HW reqs cover software needs) |
| MEDIUM | TBD-001 | Vietnamese target frame types for retrofit bracket | Field survey | Q2 2026 | Non-blocking (universal bracket designed in Phase 2) |
| MEDIUM | TBD-005 | ODI field survey validation (60-100 respondents) | Field survey | Q2 2026 | Non-blocking (estimates based on RE + expert judgment) |
| LOW | TBD-003 | MEMS microphone model selection | Hardware engineer | Phase 2 | Phase 2 decision |
| LOW | TBD-006 | FASIT export market compliance | Business dev | Phase 3+ | Future scope |
| LOW | TBD-007 | Armor LOMAH variant specifications | Engineering | Phase 3+ | Future scope |

---

## 10. Gate 1 Readiness Assessment

| Gate 1 Criterion | Target | Actual | Status |
|-----------------|--------|--------|--------|
| 16 categories reviewed | 16/16 | 16/16 | PASS |
| >=80% MUST quantified | 80% | 94% | PASS |
| 100% MUST have verification method | 100% | 100% | PASS |
| No unresolved conflicts | 0 | 0 | PASS |
| Standards compliance matrix | Complete | 11 standards (TCVN TBD) | PASS (conditional) |
| Stakeholder review | Complete | 10 stakeholders analyzed, RACI assigned | PASS |
| Document version controlled | Yes | v1.0 with frontmatter | PASS |
| ODI traceability | All EXTREME covered | 11/11 (4 partial - SW spec pending) | PASS |

### Recommendation

**GATE 1: READY FOR REVIEW**

All mandatory criteria met. Two conditional items (TCVN mapping, software spec) are tracked as TBDs with assigned owners and target dates. These do not block Phase 2 entry because:
1. MIL-STD baseline exceeds typical TCVN requirements
2. Hardware requirements fully support software features; software spec runs parallel to Phase 2

---

## Cross-References

- [[01_requirements/requirements_list.md]] - Requirements list v1.0
- [[01_requirements/stakeholder_analysis.md]] - Stakeholder analysis
- [[00_odi/odi_analysis.md]] - ODI analysis
