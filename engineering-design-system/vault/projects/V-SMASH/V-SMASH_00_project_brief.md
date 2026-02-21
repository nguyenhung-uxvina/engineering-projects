---
project: V-SMASH
phase: 2
type: project_brief
version: 1.4
created: 2025-01-15
updated: 2026-02-04
status: active
strategy: two-tier (LITE + PRO)
---

# 📁 PROJECT BRIEF
## V-SMASH: 12.7mm C-UAS Fire Control System

---

## 1. PROJECT OVERVIEW

### 1.1 Product Identification
| Field | Value |
|-------|-------|
| **Project Code** | V-SMASH |
| **Product Name** | SMASH-style Fire Control System for 12.7mm |
| **Category** | C-UAS / Fire Control |
| **Classification** | Restricted |

### 1.2 Project Timeline
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Phase 1: Task Clarification | 2025-01 | ✅ Complete |
| Phase 2: Conceptual Design | 2025-03 | 🔄 In Progress |
| Phase 3: Embodiment Design | 2025-06 | ⬜ Pending |
| Phase 4: Detail Design | 2025-09 | ⬜ Pending |
| Prototype | 2025-12 | ⬜ Pending |

### 1.3 Budget Summary
| Category | Budget | Notes |
|----------|--------|-------|
| Development | $150,000 | Including prototypes |
| Testing | $50,000 | MIL-STD compliance |
| **Total** | $200,000 | |

### 1.4 Unit Cost Targets (Two-Tier Strategy)
| Variant | Target | vs. Import | Market |
|---------|--------|------------|--------|
| **V-SMASH-LITE** | **$3,000** | 17% of SMASH 2000+ | Volume |
| **V-SMASH-PRO** | **$4,500-5,000** | 25-28% of SMASH 2000+ | Premium |

*Import reference: SMASH 2000+ = $18,000*

---

## 2. PROBLEM STATEMENT

### 2.1 Current Situation
- Increasing drone threats to military installations
- Current 12.7mm HMG lacks precision against small, fast UAVs
- Imported systems (SMASH 2000+, etc.) cost $15,000-25,000/unit

### 2.2 Customer Need
Affordable fire control system to enable 12.7mm HMG engagement of:
- Small commercial drones (DJI class)
- FPV attack drones
- Loitering munitions

### 2.3 Existing Solutions
| Solution | Pros | Cons | Cost |
|----------|------|------|------|
| Smart Shooter SMASH 2000+ | Proven, compact | Import restricted, expensive | $18,000 |
| Manual engagement | Available now | Low Pk against small UAVs | $0 |
| Dedicated C-UAS systems | Higher Pk | Very expensive, overkill | $100,000+ |

### 2.4 Why This Project?
- **Strategic**: Indigenous C-UAS capability
- **Economic**: Target $8,000/unit (55% of import)
- **Tactical**: Retrofit existing 12.7mm inventory

---

## 3. CURRENT STATUS (Phase 2)

### 3.1 Completed Deliverables
- ✅ Requirements List v1.3 (**70 requirements** - incl. ODI + 3× RE analyses)
- ✅ Function Structure v1.1 (**7 functions, 31 subfunctions** - incl. multi-target)
- ✅ Morphological Matrix v1.1 (**22 subfunctions × 3-4 options** - incl. multi-target)
- ✅ 5 Concept variants → **2-tier strategy** (LITE + PRO)
- ✅ VDI 2225 evaluation v1.3 complete
- ✅ **Reverse Engineering**: SMASH 2000+, ARCAS, and **ARBEL** analyses

### 3.2 Concept Evaluation Summary (v1.3 - Multi-Target Updated)

**Original Evaluation:**
| Concept | Score | Decision |
|---------|-------|----------|
| V4: Phased Build | 85% | Selected |

**ODI + RE Re-evaluation (2026-02-04):**
| Variant | Requirements | Score | Price | Decision |
|---------|--------------|-------|-------|----------|
| **V-SMASH-LITE** | 54/70 (77%) | **88%** | $3,000 | ✅ Phase 1 deliverable |
| **V-SMASH-PRO** | 68/70 (97%) | **79%** | $4,500-5,000 | ✅ Phase 2 deliverable |

**Strategy:** ✅ **TWO-TIER PRODUCT APPROVED** (2026-02-04)
**Multi-Target:** ✅ **5 simultaneous tracks** (both variants)
**C-UAS AI:** ✅ **Drone-optimized training** (from ARBEL RE)

### 3.3 Product Variants

| Feature | LITE | PRO |
|---------|------|-----|
| **Sensor** | CMOS | CMOS + Thermal |
| **Night ops** | NV clip-on | Integrated 200m |
| **Sensor fusion** | **None** | **Weighted blend** |
| **Sealing** | IP65 | IP67 |
| **Tracking** | Kalman (1.5g) | IMM (3g) |
| **Multi-target tracks** | **5** | **5** |
| **Data association** | **Nearest-Neighbor** | **Hungarian** |
| **Threat prioritization** | **Distance-based** | **Multi-factor AI** |
| **C4I target sharing** | **None** | **CoT/UDP** |
| **C-UAS AI training** | **≥5,000 drone images** | **≥5,000 drone images** |
| **Target Market** | Training, daylight | 24/7 operational |

### 3.4 Next Actions
1. [x] ~~Complete stakeholder review package~~ → Two-tier strategy approved
2. [x] ~~Define LITE vs PRO specifications~~ → Product Variants Spec v1.1
3. [x] ~~Add multi-target capability~~ → R65-R67 from ARCAS RE
4. [x] ~~Add C-UAS AI and sensor fusion~~ → R68-R70 from ARBEL RE
5. [ ] **Begin Phase 3 preliminary layout (LITE first)**
6. [ ] Source thermal sensor for PRO evaluation
7. [ ] Validate multi-target algorithm performance (5 tracks)
8. [ ] **Collect C-UAS drone training dataset (≥5,000 images)**
9. [ ] **Develop sensor fusion algorithm (PRO)**

---

## 4. KEY DOCUMENTS

### 4.1 Design Documents
| Document | Status | Link |
|----------|--------|------|
| ODI Analysis | ✅ v1.1 | [[V-SMASH_P0_01_ODI_analysis]] |
| Requirements List | ✅ **v1.3** | [[V-SMASH_P1_01_requirements_list]] |
| Function Structure | ✅ **v1.1** | [[V-SMASH_P2_01_function_structure]] |
| Morphological Matrix | ✅ **v1.1** | [[V-SMASH_P2_02_morphological_matrix]] |
| Concept Evaluation | ✅ **v1.3** | [[V-SMASH_P2_03_concept_evaluation]] |
| Product Variants Spec | ✅ **v1.1** | [[V-SMASH_P2_05_product_variants_spec]] |
| Complete Design Doc | ✅ v1.1 | [[V-SMASH_P2_04_conceptual_design_v1_1]] |

### 4.2 Reverse Engineering Documents
| Document | Status | Key Contribution |
|----------|--------|------------------|
| SMASH 2000+ RE | ✅ v1.0 | Fire control mechanism, safety |
| ARCAS RE | ✅ v1.0 | Multi-target (10+), C4I networking |
| **ARBEL RE** | ✅ **v1.0** | **C-UAS AI, sensor fusion** |

| Link |
|------|
| [[V-SMASH_RE_01_SMASH2000_analysis]] |
| [[V-SMASH_RE_02_ARCAS_analysis]] |
| [[V-SMASH_RE_03_ARBEL_analysis]] |

### 4.3 Approvals
| Document | Status | Link |
|----------|--------|------|
| Stakeholder Review | ⏳ Pending | MoD approval for two-tier strategy |
| Session Report | ✅ v1.0 | [[V-SMASH_SESSION_REPORT_2026-02-04]] |

---

## 5. TEAM & STAKEHOLDERS

| Role | Name/Organization | Contact |
|------|-------------------|---------|
| Project Lead | KN Nguyen | |
| Customer | [Vietnamese Military Unit] | |
| Manufacturing | [TBD - Local contractor] | |

---

## 6. REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-15 | Initial project brief |
| 1.1 | 2026-02-03 | Phase 2 progress update |
| 1.2 | 2026-02-04 | Two-tier strategy (LITE + PRO), ODI integration |
| 1.3 | 2026-02-04 | ARCAS RE multi-target update: Added R65-R67, 5 simultaneous tracks, data association, threat prioritization, C4I sharing. |
| **1.4** | **2026-02-04** | **ARBEL RE update: Added R68-R70 (C-UAS AI training, passive ranging, sensor fusion). Total: 70 requirements. Added sensor fusion and AI training to variants. 3 RE analyses complete.** |

---

*Back to [[PROJECT_INDEX|Project Index]]*
