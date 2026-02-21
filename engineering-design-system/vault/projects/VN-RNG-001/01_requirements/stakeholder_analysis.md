---
project: VN-RNG-001
phase: 1
type: stakeholder_analysis
version: 1.0
created: 2026-02-09
status: draft
---

# Stakeholder Analysis: VN-RNG-001 - LOMAH Acoustic Shooting Range System

---

## 1. Stakeholder Map Overview

```
                        HIGH INFLUENCE
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        │   S3: Regulator    │   S1: Customer     │
        │   (VPA QA/Safety)  │   (Procurement)    │
        │                    │                    │
        │   S7: Standards    │   S2: User         │
        │   Body (TCVN)      │   (Instructor)     │
        │                    │                    │
 LOW ───┼────────────────────┼────────────────────┼─── HIGH
INTEREST│                    │                    │ INTEREST
        │   S9: Competitor   │   S4: Maintainer   │
        │   (InVeris/Saab)   │   (Range Tech)     │
        │                    │                    │
        │   S10: Export      │   S5: Manufacturer │
        │   Customer (ASEAN) │   (Production)     │
        │                    │                    │
        │                    │   S6: Development  │
        │                    │   Team (Firmware/HW)│
        └────────────────────┼────────────────────┘
                             │
                        LOW INFLUENCE
```

---

## 2. Detailed Stakeholder Profiles

### S1: Customer (Procurement Authority)

| Field | Detail |
|-------|--------|
| **Who** | VPA Equipment Department (Cục Quân giới), Border Defense Command, Coast Guard Command, Police Training Bureau |
| **Role** | Budget holder, purchase decision maker |
| **Interest** | HIGH - Replacing manual ranges with electronic scoring |
| **Influence** | HIGH - Approves procurement, sets budget |
| **Primary Needs** | Cost competitiveness vs import, local content compliance, vendor independence, lifecycle affordability |
| **Success Criteria** | <=60% of import cost (CST-003); >=60% local content (PRD-001); proven accuracy (QUA-001); Vietnamese language documentation |
| **Pain Points** | Import systems cost $15K-30K/lane; foreign vendor dependency; no local support; slow procurement cycle for imported defense equipment |
| **Communication** | Formal reports, procurement specifications, demonstration events |
| **Risk if Ignored** | Project unfunded; requirements misaligned with procurement criteria |

**Key Requirements Driven:**
- CST-001 to CST-005 (cost targets)
- PRD-001 (local content >=60%)
- ERG-003 (Vietnamese language)
- SCH-001 to SCH-004 (delivery schedule)

---

### S2: User (Primary) - Marksmanship Instructor / Range NCOIC

| Field | Detail |
|-------|--------|
| **Who** | Huấn luyện viên xạ kích, NCO phụ trách bãi bắn — across VPA infantry, special forces, border defense, coast guard, police |
| **Role** | Primary job executor (ODI analysis); operates system daily during training |
| **Interest** | HIGH - Direct impact on their daily work and training effectiveness |
| **Influence** | HIGH - Field feedback determines product success; influences repeat orders |
| **Technical Level** | Medium - comfortable with Android tablets and basic electronics; NOT trained programmers or technicians |
| **Primary Needs** | Multi-lane monitoring (O-28), real-time feedback (O-27), accuracy they can trust (O-26), minimal setup effort (O-16), coaching data (O-33, O-34) |
| **Success Criteria** | Monitor 16+ lanes simultaneously; <100ms shot display; <5mm accuracy; <=8h training to operate; Vietnamese interface |
| **Pain Points** | Currently walks downrange to check paper targets; can only observe 4-8 shooters; no data-driven coaching; 60% of training time wasted |
| **Communication** | Field demonstrations, hands-on training, Vietnamese-language user manual |
| **Risk if Ignored** | Poor adoption; system not used; negative field reports kill procurement expansion |

**Key Requirements Driven (11 EXTREME opportunities):**
- KIN-004 (<=100ms latency) -- O-27
- ERG-004 (16-lane view) -- O-28
- QUA-001 (<=5mm accuracy) -- O-26
- ERG-001 (<=8h training) -- O-06
- ERG-006 (1-person setup) -- O-16

**ODI Segments Represented:**
- Segment A: Throughput Maximizers (45%) -- infantry OSUT, recruit training
- Segment B: Precision Trainers (30%) -- sniper schools, SF, competition
- Segment C: Field Deployers (25%) -- mobile teams, border defense, coast guard

---

### S2b: User (Secondary) - Individual Shooter (Trainee)

| Field | Detail |
|-------|--------|
| **Who** | Chiến sĩ, sĩ quan huấn luyện bắn — conscripts, NCOs, officers in marksmanship training |
| **Role** | Secondary job executor; receives shot feedback on individual tablet |
| **Interest** | MEDIUM - Wants to see shot placement and improve scores |
| **Influence** | LOW-MEDIUM - Doesn't choose system, but satisfaction drives perceived value |
| **Technical Level** | LOW - Many are 18-20 year-old conscripts; must be intuitive |
| **Primary Needs** | See where shot landed immediately (O-27); understand grouping (O-36); get sight adjustment recommendation (O-37); simple interface |
| **Success Criteria** | Shot visible on tablet within 100ms; clear graphical display; readable in sunlight |
| **Pain Points** | Currently has zero feedback until instructor walks downrange |
| **Communication** | Tablet interface (self-explanatory); brief verbal instruction |
| **Risk if Ignored** | Confusing interface reduces training value; system perceived as "for instructors only" |

**Key Requirements Driven:**
- ERG-005 (sunlight readability)
- ERG-007 (fast view switching)
- GEO-009 (tablet size 8-12 inch)
- SIG-009 (>=30 fps display)

---

### S3: Regulator (Safety & Quality Authority)

| Field | Detail |
|-------|--------|
| **Who** | VPA Quality Assurance directorate; Military Safety Board; TCVN standards body |
| **Role** | Approves equipment for military use; enforces safety and quality standards |
| **Interest** | MEDIUM - New equipment category requires certification pathway |
| **Influence** | HIGH - Can block deployment; sets mandatory requirements |
| **Primary Needs** | Compliance with Vietnamese military standards, safety assurance (no range safety hazards), electrical safety, environmental durability proof |
| **Success Criteria** | TCVN compliance; MIL-STD-882E safety analysis complete; no safety incidents during pilot |
| **Pain Points** | No existing Vietnamese standard for electronic LOMAH systems; must adapt from international standards |
| **Communication** | Formal compliance documentation, test reports, safety analysis reports |
| **Risk if Ignored** | Certification blocked; deployment delayed; liability exposure |

**Key Requirements Driven:**
- SAF-001 to SAF-007 (all safety requirements)
- SIG-011 (EMC MIL-STD-461G)
- Standards compliance matrix (Section 5 of requirements list)
- TBD-002 (TCVN mapping pending)

---

### S4: Maintainer (Range Technical Staff)

| Field | Detail |
|-------|--------|
| **Who** | Nhân viên kỹ thuật bãi bắn — range maintenance NCOs/technicians at battalion/regiment level |
| **Role** | Maintains, troubleshoots, repairs the system in the field |
| **Interest** | HIGH - System reliability directly affects their workload |
| **Influence** | MEDIUM - Maintenance feedback influences design updates and procurement decisions |
| **Technical Level** | Medium - electronics repair skills (soldering, multimeter); NOT software engineers |
| **Available Tools** | Basic hand tools, multimeter, soldering station (at depot level) |
| **Primary Needs** | Easy fault diagnosis (O-64), fast module swap (O-62), cheap spare parts (O-63), minimal professional recalibration (O-67), clear maintenance manual |
| **Success Criteria** | MTTR <=30 min (MNT-001); self-diagnostics detect >=90% faults (MNT-004); spare parts available in 7 days (MNT-005); 12-month calibration interval (MNT-003) |
| **Pain Points** | Imported systems require foreign technicians for any repair; spare parts take months; no local knowledge of proprietary systems |
| **Communication** | Vietnamese-language maintenance manual; fault code reference card; 16-hour training course |
| **Risk if Ignored** | System downtime increases; units stop using system; negative reputation |

**Key Requirements Driven:**
- MNT-001 to MNT-008 (all maintenance requirements)
- ASM-004 (modular sensor replacement <=15 min)
- ASM-005 (standard M12 connectors)
- ERG-002 (<=16h maintenance training)

---

### S5: Manufacturer (Production Team)

| Field | Detail |
|-------|--------|
| **Who** | Vietnamese manufacturing partners: PCB fabricators, CNC machining shops, electronics assemblers, test technicians |
| **Role** | Produces the hardware; determines local content % and cost structure |
| **Interest** | HIGH - Revenue opportunity; capability building |
| **Influence** | MEDIUM - Manufacturing capability constrains design choices |
| **Capabilities** | PCB: 4-layer FR4, solder paste + reflow; CNC: 3-axis aluminum; Assembly: IPC-A-610 Class 2 achievable with training |
| **Primary Needs** | Clear manufacturing drawings, realistic tolerances, available materials, reasonable batch sizes, design-for-manufacture |
| **Success Criteria** | >=60% local content achieved (PRD-001); consistent quality at volume; profitable margins |
| **Pain Points** | Limited experience with precision acoustic instruments; need training on conformal coating and IP67 sealing; import lead times for MEMS and ICs |
| **Communication** | Manufacturing specification packages, supplier qualification audits, DFM reviews |
| **Risk if Ignored** | Poor yield rates; inconsistent quality; local content target not met; cost overruns |

**Key Requirements Driven:**
- PRD-001 to PRD-007 (all production requirements)
- MAT-001 (6061-T6 aluminum -- locally available)
- CST-004 (sensor bar BOM <=$900)

**Key Suppliers (from CLAUDE.md):**
| Material | Potential Suppliers |
|----------|-------------------|
| Aluminum enclosure | Local CNC shops (Hoa Phat aluminum stock) |
| PCB fabrication | Vietnamese PCB fabs (4-layer FR4) |
| Conformal coating | Local coating specialists |
| MEMS microphones | Import: TDK, Knowles, InvenSense (China/US) |
| ARM SoC (STM32H7) | Import: STMicroelectronics (China distribution) |
| Connectors (M12) | Import: Amphenol, TE Connectivity (China) |
| Stainless fasteners | Local or import |

---

### S6: Development Team (Engineering)

| Field | Detail |
|-------|--------|
| **Who** | Firmware engineers (GCC-PHAT, embedded), hardware engineers (PCB, enclosure), software developers (web dashboard, Android app) |
| **Role** | Designs and develops the product through all phases |
| **Interest** | HIGH - Core project team |
| **Influence** | MEDIUM - Technical decisions within design space |
| **Primary Needs** | Clear requirements with quantified targets, access to test equipment (oscilloscope, acoustic chamber), military range access for field testing |
| **Success Criteria** | Prototype meets all MUST requirements; accuracy validated on live range; firmware passes unit tests |
| **Pain Points** | No prior LOMAH development experience; limited access to military ranges for testing; need acoustic signal processing training |
| **Communication** | Technical reviews, sprint demos, design reviews |
| **Risk if Ignored** | Requirements misinterpretation; scope creep; unrealistic schedule |

**Key Requirements Driven:**
- SIG-005, SIG-006 (sensor sampling, ADC resolution -- firmware architecture)
- KIN-004 (latency budget allocation across firmware pipeline)
- QUA-001 (accuracy target drives algorithm optimization effort)

**Capability Gaps Identified (from RE analysis):**
| Gap | Action |
|-----|--------|
| High-speed acoustic DSP | GCC-PHAT already implemented; training on optimization |
| IP67 enclosure design | Partner with experienced CNC shop; sealing test equipment needed |
| MIL-STD testing | Contract with accredited test lab |
| Field validation | Coordinate range access with VPA customer (S1) |

---

### S7: Standards Body

| Field | Detail |
|-------|--------|
| **Who** | Vietnamese Directorate for Standards, Metrology and Quality (STAMEQ); VPA technical standards office |
| **Role** | Defines applicable TCVN standards; certifies compliance |
| **Interest** | LOW-MEDIUM - New product category, no existing LOMAH standard |
| **Influence** | HIGH - Compliance is mandatory for military procurement |
| **Primary Needs** | Product meets applicable TCVN requirements; test reports from accredited labs |
| **Communication** | Formal compliance dossier; test certificates |
| **Risk if Ignored** | Procurement blocked without TCVN compliance certification |

**Key Requirements Driven:**
- TBD-002 (TCVN standard numbers pending)
- SAF-007 (bilingual labels per Vietnamese regulation)
- ENE-002 (220V 50Hz Vietnamese power standard)

---

### S8: Higher Command (Decision Influencer)

| Field | Detail |
|-------|--------|
| **Who** | Battalion/regiment commanders, training directorate, VPA General Staff training department |
| **Role** | Sets training requirements; allocates range time and budget; evaluates training effectiveness |
| **Interest** | MEDIUM - Cares about training outcomes (qualification pass rates), not system details |
| **Influence** | HIGH - Decides to procure (or not) based on training effectiveness demonstration |
| **Primary Needs** | Improved qualification pass rates (proven: InVeris 40-45% -> 86%); reduced training time per cycle; data-driven training reports for command oversight |
| **Success Criteria** | Measurable improvement in qualification rates; reduced training days per cycle; comprehensive training reports |
| **Communication** | Executive summary reports, demonstration events, pilot installation results |
| **Risk if Ignored** | No command buy-in; procurement not prioritized; budget diverted elsewhere |

**Key Requirements Driven:**
- QUA-009 (qualification scoring accuracy 100%)
- SIG-010 (CSV/JSON/PDF report export)
- O-48 (qualification scoring), O-54 (record generation), O-55 (report completeness)

---

### S9: Competitors (Indirect Stakeholder)

| Field | Detail |
|-------|--------|
| **Who** | InVeris (US), Saab (Sweden), Polytronic (Switzerland), Zen Technologies (India) |
| **Role** | Alternative solutions; benchmark for performance and pricing |
| **Interest** | LOW - VN-RNG-001 targets markets they are weak in (Vietnamese, cost-sensitive) |
| **Influence** | MEDIUM - Set customer expectations on performance specs |
| **Impact on Design** | Accuracy, detection rate, and environmental specs benchmarked against competitor products |

**Competitive Positioning (from RE reports):**
| Factor | VN-RNG-001 | InVeris | Saab | Polytronic |
|--------|-----------|---------|------|------------|
| Cost/lane | $5-8K | $15-30K | $15-30K | $20-50K |
| Accuracy | <5mm | <5mm (150mm zone) | <5mm | <=10mm avg |
| Tropical design | Native | Adapted | Cold-climate | UAE+Swiss |
| Local content | 60-75% | 0% | 0% | 0% |
| Vendor independence | Full | None | None | None |

---

### S10: Export Customer (Future Stakeholder)

| Field | Detail |
|-------|--------|
| **Who** | ASEAN military/police training organizations (Laos, Cambodia, Myanmar, Philippines, Indonesia) |
| **Role** | Future market expansion (Year 4-5 per ODI roadmap) |
| **Interest** | LOW (current) - Becomes HIGH when product is proven |
| **Influence** | LOW (current) - Does not drive Phase 1 requirements |
| **Primary Needs** | Affordable LOMAH alternative to Western imports; regional support; non-US-export-controlled |
| **Impact on Design** | English language option (ERG-003); RoHS compliance (MAT-007); potential FASIT compatibility (TBD-006) |

---

## 3. Stakeholder Influence-Interest Matrix

| | Low Interest | High Interest |
|---|-------------|--------------|
| **High Influence** | S3: Regulator (Manage Closely) | S1: Customer (Key Player) |
| | S7: Standards Body (Manage Closely) | S2: User/Instructor (Key Player) |
| | S8: Higher Command (Keep Satisfied) | |
| **Low Influence** | S9: Competitors (Monitor) | S4: Maintainer (Keep Informed) |
| | S10: Export Customer (Monitor) | S5: Manufacturer (Keep Informed) |
| | | S6: Dev Team (Keep Informed) |

### Engagement Strategy

| Strategy | Stakeholders | Actions |
|----------|-------------|---------|
| **Key Players** (High influence + High interest) | S1: Customer, S2: User | Regular demos, pilot involvement, feedback loops, Vietnamese-language deliverables |
| **Keep Satisfied** (High influence + Low interest) | S3: Regulator, S7: Standards, S8: Command | Formal compliance documentation, executive summaries, demonstration events |
| **Keep Informed** (Low influence + High interest) | S4: Maintainer, S5: Manufacturer, S6: Dev Team | Design reviews, DFM sessions, maintenance manual drafts, training courses |
| **Monitor** (Low influence + Low interest) | S9: Competitors, S10: Export | Market intelligence, competitive benchmarking, export readiness checklist |

---

## 4. Requirements Responsibility Matrix (RACI)

| Requirement Category | S1 Customer | S2 User | S3 Regulator | S4 Maintainer | S5 Manufacturer | S6 Dev Team |
|---------------------|-------------|---------|-------------|--------------|-----------------|-------------|
| Geometry | I | C | — | I | C | **R/A** |
| Kinematics | I | C | — | — | — | **R/A** |
| Forces | — | — | C | — | C | **R/A** |
| Energy | I | C | — | C | C | **R/A** |
| Material | — | — | C | C | **C** | **R/A** |
| Signals | I | C | C | C | — | **R/A** |
| Safety | C | I | **A** | I | I | **R** |
| Ergonomics | C | **C** | — | C | — | **R/A** |
| Production | **A** | — | I | — | **C** | **R** |
| Quality | **A** | C | C | I | C | **R** |
| Assembly | — | C | — | **C** | C | **R/A** |
| Transport | I | C | — | C | C | **R/A** |
| Operation | I | **C** | C | C | — | **R/A** |
| Maintenance | I | I | — | **C** | C | **R/A** |
| Costs | **A** | — | — | — | C | **R** |
| Schedule | **A** | I | I | — | C | **R** |

**R** = Responsible, **A** = Accountable, **C** = Consulted, **I** = Informed

---

## 5. Stakeholder Risks & Mitigations

| Risk | Stakeholder | Probability | Impact | Mitigation |
|------|------------|-------------|--------|------------|
| Customer rejects due to unproven accuracy | S1, S8 | Medium | High | Prototype demonstration at military range with documented accuracy test (QUA-001) |
| Instructors resist new technology adoption | S2 | Medium | High | <=8h training requirement (ERG-001); Vietnamese interface (ERG-003); hands-on pilot phase |
| TCVN compliance pathway unclear | S3, S7 | Medium | Medium | Early engagement with STAMEQ; map to MIL-STD equivalents; TBD-002 resolution by Q2 2026 |
| Local manufacturer quality inconsistent | S5 | Medium | Medium | Supplier qualification audit; IPC-A-610 training; end-of-line automated test (PRD-007) |
| Development team lacks acoustic DSP expertise | S6 | Low | Medium | GCC-PHAT already implemented and tested; bring in DSP consultant for optimization if needed |
| Competitor price reduction in response | S9 | Low | Low | Vietnamese cost structure advantage is structural, not marginal; competitors cannot match 60-75% local content |
| Higher command diverts budget to other priorities | S8 | Medium | High | Quantify training effectiveness improvement (pass rate data); low pilot cost ($200K) reduces risk perception |

---

## Cross-References

- [[01_requirements/requirements_list.md]] - Requirements list (120 requirements)
- [[00_odi/odi_analysis.md]] - ODI analysis (73 outcomes, 3 segments)
- [[00_project_brief.md]] - Project brief
