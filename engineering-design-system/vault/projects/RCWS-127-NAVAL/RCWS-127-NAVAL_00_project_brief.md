---
project: RCWS-127-NAVAL
phase: 1
type: project_brief
version: 1.0
created: 2026-02-03
updated: 2026-02-03
status: active
---

# 📁 PROJECT BRIEF
## RCWS-127-NAVAL: 12.7mm Naval RCWS System

**Version**: 1.0 | **Created**: 2026-02-03 | **Updated**: 2026-02-03

---

## 1. PROJECT OVERVIEW

### 1.1 Product Identification
| Field | Value |
|-------|-------|
| **Project Code** | RCWS-127-NAVAL |
| **Product Name** | 12.7mm Naval Remote Controlled Weapon Station |
| **Category** | Naval Weapon Systems / RCWS |
| **Classification** | Restricted |
| **Base Platform** | MTB-20 RCWS (ground vehicle variant) |

### 1.2 Project Timeline
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Phase 1: Task Clarification | 2026-Q2 | 🔄 In Progress |
| Phase 2: Conceptual Design | 2026-Q3 | ⬜ Not Started |
| Phase 3: Embodiment Design | 2026-Q4 | ⬜ Not Started |
| Phase 4: Detail Design | 2027-Q1 | ⬜ Not Started |
| Prototype Testing | 2027-Q2 | ⬜ Not Started |
| Production Start | 2027-Q3 | ⬜ Not Started |

### 1.3 Budget Summary
| Category | Budget | Notes |
|----------|--------|-------|
| Development | $250,000 | Naval adaptation engineering |
| Prototyping | $150,000 | 2 prototype units |
| Testing | $100,000 | Sea trials, environmental testing |
| **Total** | **$500,000** | Plus production tooling |

---

## 2. PROBLEM STATEMENT

### 2.1 Current Situation
- Vietnamese Navy patrol boats lack modern RCWS capability
- Existing manually-operated 12.7mm mounts expose crew to danger
- Current MTB-20 RCWS designed for ground vehicles, not marinized
- No integration with ship fire control systems
- Increasing asymmetric threats in South China Sea (fast attack craft, drones)

### 2.2 Customer Need
**Vietnamese Navy requires**:
- Remote-controlled 12.7mm weapon station for patrol boats
- Protection against fast surface threats and UAVs
- Corrosion-resistant design for harsh marine environment
- Integration with existing naval vessels (retrofit capability)
- Reduced crew exposure during surface engagement

**Key Requirements**:
- All-weather operation (sea state 4+)
- Salt spray resistance (MIL-STD-810 Method 509)
- Stabilization for moving platform
- Day/night target acquisition
- Local content >60%

### 2.3 Existing Solutions
| Solution | Pros | Cons | Cost |
|----------|------|------|------|
| Kongsberg Sea Protector | Proven, excellent performance | Import-restricted, very expensive, no local support | $800,000+/unit |
| Rafael Typhoon | Combat-proven, stabilized | Export control issues, high cost | $600,000+/unit |
| MTB-20 (ground variant) | Available, local production | Not marinized, no stabilization | $120,000/unit |
| Manual 12.7mm mount | Available now, low cost | Crew exposure, poor accuracy on moving platform | $5,000/unit |

### 2.4 Why This Project?
- **Strategic**: Reduce foreign dependency for naval systems, critical for sovereignty
- **Economic**: Target $250,000/unit (30-40% of import equivalent)
- **Tactical**: Retrofit existing patrol boat fleet (20+ vessels)
- **Capability**: Fill gap in naval asymmetric warfare capability
- **Industrial**: Develop Vietnamese maritime defense industry

---

## 3. STAKEHOLDER ANALYSIS

### 3.1 Customer (Người mua)
| Attribute | Description |
|-----------|-------------|
| **Organization** | Vietnamese Navy - Coastal Defense Command |
| **Decision maker** | Naval Procurement Directorate |
| **Budget authority** | Ministry of Defense |
| **Key concerns** | Corrosion resistance, reliability at sea, cost |

### 3.2 End Users (Người dùng cuối)
| Attribute | Description |
|-----------|-------------|
| **User organization** | Patrol boat crews (20-30 personnel/vessel) |
| **Operator profile** | Navy gunners, technical level: intermediate |
| **Technical level** | Basic electronics, weapon system operators |
| **Operating environment** | Coastal/offshore patrol, tropical maritime, 24/7 ops |

### 3.3 Maintainers
| Attribute | Description |
|-----------|-------------|
| **Maintenance organization** | Naval shipyard maintenance teams |
| **Skill level available** | Mechanical technicians, basic electronics |
| **Tools/facilities** | Naval shipyard workshops, corrosion treatment facilities |

### 3.4 Other Stakeholders
| Stakeholder | Role | Interest |
|-------------|------|----------|
| Vietnam Shipbuilding Industry | Integration partner | Retrofit installation contracts |
| Hòa Phát | Material supplier | Marine-grade aluminum/steel |
| MoD Standards Office | Regulator | Safety certification, standards compliance |
| Existing MTB-20 supplier | Base platform | Maintain compatibility, supply chain |

---

## 4. TECHNICAL CONTEXT

### 4.1 Applicable Standards
| Standard | Sections | Applicability |
|----------|----------|---------------|
| **MIL-STD-810H** | Method 509.7 (Salt Fog), 506.6 (Rain) | Marinization |
| **MIL-STD-461G** | RE102, RS103 | EMC for naval systems |
| **MIL-STD-882E** | All | System safety (weapon safety critical) |
| **MIL-STD-167** | Type I/II | Mechanical vibration (shipboard) |
| **ISO 12217** | Part 1-3 | Small craft stability (for weight/balance) |
| **TCVN 9294** | All | Vietnamese maritime equipment standards |

### 4.2 Related Systems/Interfaces
| System | Interface Type | Notes |
|--------|---------------|-------|
| MTB-20 RCWS (base) | Mechanical/electrical | Weapon, drive, control modules reused |
| Patrol boat fire control | Electrical (RS-232/CAN) | Target designation from ship radar |
| Ship power system | Electrical (24V/110V DC) | Naval power standards |
| Gyro-stabilized platform | Mechanical/data | Vessel motion compensation |
| V-SMASH fire control | Software/hardware | Potential future integration for C-UAS |

### 4.3 Technology Constraints
**Available locally**:
- Marine-grade aluminum fabrication (Hòa Phát, shipyards)
- Stainless steel machining
- Basic electrical/electronics assembly
- Corrosion-resistant coatings (epoxy, zinc)

**Requires import**:
- Precision gyroscopic stabilization system (Israel/US)
- Marine-grade servo drives (Japan/Europe)
- Sealed optical sensors (FLIR, day camera)
- High-reliability slip rings

**Export control concerns**:
- Gyro-stabilization tech (ITAR/Wassenaar Arrangement)
- Advanced EO/IR sensors
- Fire control software (if AI-based)

---

## 5. SUCCESS CRITERIA

### 5.1 Technical Success
- [ ] Stabilization enables accurate fire in sea state 4 (1.25-2.5m waves)
- [ ] Salt fog exposure 1000 hours (MIL-STD-810 Method 509.7)
- [ ] Hit probability >50% @ 500m vs surface target (moving platform)
- [ ] MTBF >500 hours in marine environment
- [ ] Integration with existing patrol boat fire control systems

### 5.2 Commercial Success
- [ ] Unit cost <$250,000 (production qty 20+)
- [ ] Local content ≥60% by value
- [ ] Development complete within 18 months
- [ ] Retrofit compatibility with 3+ patrol boat classes

### 5.3 Strategic Success
- [ ] Naval asymmetric warfare capability established
- [ ] Foundation for future naval RCWS variants (30mm, missiles)
- [ ] Knowledge transfer to Vietnamese shipbuilding industry
- [ ] Export potential to regional navies

---

## 6. RISKS AND CONSTRAINTS

### 6.1 Known Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Stabilization tech export control | High | High | Source from non-ITAR suppliers (Korea, China) |
| Corrosion failure in testing | Medium | High | Aggressive marinization design, multiple coating layers |
| Cost overrun (import components) | Medium | Medium | Fix cost early via supplier contracts |
| Integration complexity with ships | Medium | Medium | Early shipyard engagement, interface control docs |
| Schedule slip (prototype testing) | Low | Medium | Fixed-scope Phase 1, phased sea trials |

### 6.2 Constraints
| Constraint | Description | Impact on Design |
|------------|-------------|------------------|
| **Budget** | $500K total development | Reuse MTB-20 modules, limit new development |
| **Schedule** | 18 months to production | Parallel engineering, off-the-shelf stabilization |
| **Technology** | Export control on stabilization | Source from accessible suppliers early |
| **Regulatory** | Naval certification requirements | Early engagement with MoD Standards Office |
| **Physical** | Patrol boat deck space limited | Compact footprint, minimize above-deck mass |

---

## 7. KEY DIFFERENCES FROM MTB-20 BASE

### 7.1 New Requirements (Naval-Specific)
| Requirement | MTB-20 Ground | MTB-20 Naval | Rationale |
|-------------|---------------|--------------|-----------|
| **Corrosion resistance** | Standard | Marine-grade (5000 hrs salt fog) | Sea environment |
| **Stabilization** | None | 2-axis gyro-stabilized | Moving platform accuracy |
| **Sealing** | IP54 | IP67 minimum | Water spray, immersion risk |
| **Power input** | 12V/24V vehicle | 24V/110V DC naval | Ship power systems |
| **Fire control interface** | Standalone | CAN bus ship integration | Tactical coordination |
| **Weight** | <150 kg | <200 kg | Deck loading, stability |

### 7.2 Retained from MTB-20
- Weapon mount mechanism (12.7mm NSV/DShK)
- Azimuth/elevation drive motors (with marinized seals)
- Operator control unit (software upgraded)
- Ammunition feed system
- Safety interlocks

### 7.3 Major New Subsystems
1. **Gyro-stabilized platform** (import)
2. **Marinized housing** (local fabrication)
3. **Ship interface unit** (local electronics)
4. **Environmental sealing system** (local design)

---

## 8. PROJECT DELIVERABLES

### Phase 1: Task Clarification (Current)
- [ ] `01_requirements_list.md` - Complete naval requirements specification
- [ ] Interface Control Document with MTB-20
- [ ] Stakeholder review completed
- [ ] Gate 1 approval

### Phase 2: Conceptual Design
- [ ] `02_function_structure.md` - Function breakdown (naval adaptations)
- [ ] `03_morphological_matrix.md` - Stabilization & marinization solutions
- [ ] `04_concept_evaluation.md` - VDI 2225 evaluation
- [ ] Gate 2 approval

### Phase 3: Embodiment Design
- [ ] `05_embodiment_layout.md` - Definitive layout with marinization
- [ ] DfM review for shipyard fabrication
- [ ] Preliminary BOM (local vs import)
- [ ] Gate 3 approval

### Phase 4: Detail Design
- [ ] `06_detail_drawings/` - Production drawings
- [ ] `07_verification_plan.md` - Sea trial test plan
- [ ] `08_cost_analysis.md` - Final cost estimate (unit + retrofit)
- [ ] Installation manual (shipyard)
- [ ] Gate 4 approval

### Prototype & Testing
- [ ] 2 prototype units fabricated
- [ ] Shipyard integration (1 patrol boat)
- [ ] Sea trials (500 hours operational)
- [ ] MIL-STD-810 environmental testing

### Project Closure
- [ ] `99_lessons_learned.md` - D-M-I-R reflection
- [ ] Production release package

---

## 9. NEXT IMMEDIATE ACTIONS

**This Week**:
1. Load Phase 1 skill: [[../../skills/SKILL_task_clarification|Task Clarification Guide]]
2. Begin requirements development (16 P&B categories)
3. Schedule stakeholder kickoff meeting

**Next 2 Weeks**:
1. Visit shipyard to measure patrol boat installation constraints
2. Contact stabilization suppliers (Korea, China, Israel)
3. Review MTB-20 design package for reuse analysis

---

## 10. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-03 | Design Team | Initial project brief |

---

## 11. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Lead | | ☐ Pending | |
| Technical Review | | ☐ Pending | |
| Customer Rep (Navy) | | ☐ Pending | |

---

*This project follows Pahl & Beitz systematic design methodology with D-M-I-R integration for naval defense product development.*

*Related: [[../../V-SMASH/00_project_brief|V-SMASH Project]] (potential future integration)*
