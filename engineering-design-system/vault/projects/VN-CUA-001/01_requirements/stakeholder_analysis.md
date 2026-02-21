---
project: VN-CUA-001
designation: VDC-100
type: stakeholder_analysis
phase: 1
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Step 2
---

# VN-CUA-001: STAKEHOLDER ANALYSIS
## Vietnamese Drone Catcher 100 (VDC-100)
## Phân tích Các bên Liên quan - Giai đoạn 1, Bước 2

**Project Code:** VN-CUA-001
**Phase:** 1 - Task Clarification (Step 2)
**Date:** 2026-02-08

---

# 1. STAKEHOLDER IDENTIFICATION

## 1.1 Stakeholder Registry

| # | Stakeholder | Role | Category | Influence | Interest | Priority |
|---|-------------|------|----------|-----------|----------|----------|
| S1 | **C-UAS Operator** | End user (fire launcher) | User | Medium | High | **PRIMARY** |
| S2 | **Security Team Leader** | Tactical coordinator | User | Medium | High | High |
| S3 | **Procurement Officer** | Purchase decision | Customer | **High** | **High** | **PRIMARY** |
| S4 | **Military Commander** | Sets ROE, approves use | Customer | **High** | Medium | High |
| S5 | **Maintenance Technician** | Maintains system readiness | Maintainer | Low | High | Medium |
| S6 | **Training Instructor** | Trains operators | Support | Medium | High | High |
| S7 | **Investigation Unit** | Uses captured drone evidence | Beneficiary | Low | Medium | Medium |
| S8 | **Logistics Officer** | Stores/transports equipment | Support | Low | Medium | Low |
| S9 | **Manufacturing Team** | Builds product | Manufacturer | Medium | Medium | Medium |
| S10 | **Quality Inspector** | Verifies product quality | Manufacturer | Medium | Medium | Medium |
| S11 | **Regulatory Body** | Certifies for use | Regulator | **High** | Low | High |
| S12 | **Vietnamese MOD** | Defense policy, standards | Regulator | **High** | Medium | High |
| S13 | **Airport Authority** | Site-specific requirements | Customer | Medium | High | Medium |
| S14 | **Local Suppliers** | Provide materials/components | Supply Chain | Low | Medium | Medium |

---

# 2. POWER-INTEREST MATRIX

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    POWER-INTEREST MATRIX: VN-CUA-001                          ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  HIGH ┌─────────────────────────────┬─────────────────────────────────────┐  ║
║       │                             │                                     │  ║
║       │  KEEP SATISFIED             │  MANAGE CLOSELY                     │  ║
║       │                             │                                     │  ║
║  P    │  S11 Regulatory Body        │  S3  Procurement Officer ⭐         │  ║
║  O    │  S12 Vietnamese MOD         │  S4  Military Commander             │  ║
║  W    │                             │                                     │  ║
║  E    │                             │                                     │  ║
║  R    ├─────────────────────────────┼─────────────────────────────────────┤  ║
║       │                             │                                     │  ║
║       │  MONITOR                    │  KEEP INFORMED                      │  ║
║       │                             │                                     │  ║
║       │  S14 Local Suppliers        │  S1  C-UAS Operator ⭐              │  ║
║       │                             │  S2  Security Team Leader           │  ║
║       │                             │  S5  Maintenance Technician         │  ║
║       │                             │  S6  Training Instructor            │  ║
║       │                             │  S7  Investigation Unit             │  ║
║       │                             │  S8  Logistics Officer              │  ║
║       │                             │  S9  Manufacturing Team             │  ║
║       │                             │  S10 Quality Inspector              │  ║
║  LOW  │                             │  S13 Airport Authority              │  ║
║       └─────────────────────────────┴─────────────────────────────────────┘  ║
║                        LOW                              HIGH                  ║
║                                    INTEREST                                   ║
║                                                                               ║
║  ⭐ = Primary design input source                                             ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

# 3. DETAILED STAKEHOLDER PROFILES

## 3.1 S1: C-UAS Operator (PRIMARY — Job Executor)

| Attribute | Detail |
|-----------|--------|
| **Vietnamese Title** | Nhân viên vận hành chống UAV |
| **Demographics** | Age 22-45, high school + military/security training |
| **Physical** | Good fitness, carry 8-10 kg extended periods |
| **Training Level** | 2-4 hours minimum with system |
| **Operating Context** | Outdoor (airport, event, military base), solo or 2-person team |
| **Weather Exposure** | Hot/humid, rain, bright sun (Vietnam tropical) |
| **Time Pressure** | Seconds to engage — drone moves 10-20 m/s |
| **Stakes** | VIP safety, public security, military asset protection |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| High first-shot hit probability | **CRITICAL** | CUA-KIN-06, CUA-KIN-07, CUA-SIG-03 |
| Equipment works when needed | **CRITICAL** | CUA-QUA-01, CUA-QUA-06 |
| Light enough for patrol | HIGH | CUA-GEO-01, CUA-ERG-06 |
| Fast to ready from carry | HIGH | CUA-ASM-05, CUA-ERG-07 |
| Quick reload after miss | HIGH | CUA-ASM-02 |
| Easy to learn | MEDIUM | CUA-ERG-05 |
| Works in rain/heat | MEDIUM | CUA-OPR-01, CUA-OPR-02, CUA-QUA-07 |

**Emotional Jobs:**
- Feel confident in ability to stop threat
- Avoid embarrassment of missing target in front of team
- Trust equipment to fire every time

**Social Jobs:**
- Be seen as capable protector
- Demonstrate professional competence to superiors

---

## 3.2 S3: Procurement Officer (PRIMARY — Decision Maker)

| Attribute | Detail |
|-----------|--------|
| **Vietnamese Title** | Cán bộ mua sắm quốc phòng |
| **Organization** | Military procurement, Police procurement, Airport authority |
| **Decision Authority** | Approves purchase, selects vendor |
| **Budget Cycle** | Annual (Vietnamese fiscal year) |
| **Evaluation Criteria** | Cost, compliance, local content, delivery, support |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| Price ≤70% of import | **CRITICAL** | CUA-CST-01 ($6,000 vs $30,000) |
| Local content ≥60% | **CRITICAL** | CUA-PRO-01 (≥70%) |
| MIL-STD compliance | HIGH | CUA-OPR-01 thru OPR-05, CUA-FOR-05 |
| Warranty & support | HIGH | CUA-QUA-04, CUA-MNT-04 |
| Delivery timeline | MEDIUM | CUA-SCH-01 thru SCH-05 |
| Demonstrated effectiveness | MEDIUM | CUA-KIN-06 (70% hit rate demo) |

**Decision Criteria (Weighted):**

| Criterion | Weight | VDC-100 Score | SkyWall Score |
|-----------|--------|---------------|---------------|
| Unit cost | 30% | 9/10 ($6K) | 3/10 ($30K) |
| Local content | 20% | 9/10 (72%) | 1/10 (0%) |
| Performance | 20% | 7/10 (80m range) | 9/10 (100m) |
| Support/logistics | 15% | 9/10 (local) | 3/10 (UK vendor) |
| Compliance | 15% | 7/10 (testing TBD) | 9/10 (proven) |
| **WEIGHTED** | **100%** | **8.3/10** | **4.5/10** |

---

## 3.3 S4: Military Commander

| Attribute | Detail |
|-----------|--------|
| **Concerns** | ROE compliance, operational effectiveness, troop safety |
| **Decision Role** | Approves fielding, sets deployment doctrine |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| Safety (no fratricide) | **CRITICAL** | CUA-SAF-01 thru SAF-04 |
| Reliable engagement | HIGH | CUA-QUA-05, CUA-QUA-06 |
| Evidence for prosecution | MEDIUM | CUA-KIN-05 (soft landing) |
| Multi-threat capability | MEDIUM | CUA-KIN-02 (range), CUA-KIN-07 (moving) |

---

## 3.4 S5: Maintenance Technician

| Attribute | Detail |
|-----------|--------|
| **Skill Level** | Trained technician, standard tools |
| **Environment** | Field workshop or depot |
| **Concern** | Ease of maintenance, spare parts availability |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| Field-strippable | HIGH | CUA-ASM-01 |
| Standard tools only | HIGH | CUA-MNT-01 |
| Clear maintenance schedule | MEDIUM | CUA-MNT-02, CUA-MNT-03 |
| 10-year spare parts | MEDIUM | CUA-MNT-04 |
| Low component count | LOW | CUA-ASM-04 (≤80 parts) |

---

## 3.5 S6: Training Instructor

| Attribute | Detail |
|-----------|--------|
| **Concern** | Training effectiveness, time to proficiency, cost per trainee |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| Fast operator proficiency | HIGH | CUA-ERG-05 (≤4 hours) |
| Training mode distinction | HIGH | CUA-SIG-07 (LED indicator) |
| Low training projectile cost | MEDIUM | CUA-CST-07 (≤$30) |
| Intuitive controls | MEDIUM | CUA-ERG-01, CUA-ERG-04 |

---

## 3.6 S7: Investigation Unit

| Attribute | Detail |
|-----------|--------|
| **Concern** | Drone captured intact, forensic evidence preserved |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| Drone captured intact | **CRITICAL** | CUA-KIN-05 (3-5 m/s descent) |
| Memory card readable | HIGH | Soft landing design |
| Chain of custody support | MEDIUM | Future: evidence bag + log |

**Systems Loop:** R3 (Evidence Preservation Flywheel) — key differentiator identified in Systems Analysis.

---

## 3.7 S11/S12: Regulatory Bodies (MOD, Standards)

| Attribute | Detail |
|-----------|--------|
| **Standards** | MIL-STD-810H, MIL-STD-461G, MIL-STD-882E, TCVN |
| **Concern** | Safety certification, environmental qualification, EMC |

**Needs & Requirements Mapping:**

| Need | Priority | Mapped Requirements |
|------|----------|---------------------|
| Environmental qualification | **CRITICAL** | CUA-OPR-01 thru OPR-05 |
| Safety analysis (FMEA) | **CRITICAL** | CUA-SAF-01 thru SAF-05 |
| Pressure vessel certification | HIGH | CUA-FOR-04, CUA-TRA-03 |
| Laser safety classification | HIGH | CUA-SAF-04 |

---

# 4. STAKEHOLDER COMMUNICATION PLAN

| Stakeholder | Communication | Frequency | Method | Owner |
|-------------|---------------|-----------|--------|-------|
| S1: Operator | User feedback, field testing | Per milestone | Field test + survey | Test Eng. |
| S3: Procurement | Progress reports, cost tracking | Monthly | Written report | PM |
| S4: Commander | Capability demonstrations | Per gate review | Live demo | PM + Sales |
| S5: Maintenance | Maintenance procedure review | Phase 3-4 | Workshop review | Mech. Eng. |
| S6: Instructor | Training program development | Phase 4 | Co-development | Training |
| S7: Investigation | Evidence preservation validation | Phase 3 | Capture test | Systems Eng. |
| S11/S12: Regulator | Standards compliance evidence | Per gate review | Test reports | QA |
| S14: Suppliers | Procurement specs, schedules | As needed | Purchase orders | Procurement |

---

# 5. REQUIREMENTS COVERAGE CHECK

| Stakeholder | # Direct Requirements | Coverage | Gaps |
|-------------|----------------------|----------|------|
| S1: Operator | 28 | Complete | None |
| S3: Procurement | 12 | Complete | None |
| S4: Commander | 9 | Complete | None |
| S5: Maintenance | 6 | Complete | None |
| S6: Instructor | 4 | Complete | None |
| S7: Investigation | 2 | Partial | Evidence bag/chain of custody TBD |
| S11/S12: Regulator | 15 | Complete | TCVN mapping TBD |
| S14: Suppliers | 5 | Complete | None |
| **TOTAL mapped** | **81/89** | **91%** | 8 reqs are internal/schedule |

---

# 6. STAKEHOLDER RISK REGISTER

| Risk | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| Operator rejects weight (too heavy) | S1 | Medium | High | Target 7 kg (below 8 kg MUST) |
| Procurement demands lower price | S3 | High | Medium | Show TCO advantage + local content |
| MOD requires additional standards | S12 | Medium | High | Engage early, build compliance buffer |
| Training time exceeds 4 hours | S6 | Low | Medium | Simplified controls, intuitive reticle |
| Evidence preservation insufficient | S7 | Low | Medium | Larger parachute option |
| Local supplier quality issues | S14 | Medium | Medium | Dual-source critical components |

---

# DOCUMENT LINKS

- [[01_requirements/requirements_list|Requirements List]]
- [[01_requirements/standards_compliance|Standards Compliance Matrix]]
- [[01_requirements/validation_report|Validation Report]]
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]

---

*This stakeholder analysis follows Pahl & Beitz Step 2 methodology, integrated with ODI customer segmentation data.*
