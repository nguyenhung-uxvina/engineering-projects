---
project: VN-CUA-001
designation: VDC-100
type: requirements_list
phase: 1
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Steps 3/4/5
total_requirements: 89
demands: 70
wishes: 19
quantification_rate: 100%
odi_linked: 13
gate1: APPROVED
---

# VN-CUA-001: REQUIREMENTS LIST
## Vietnamese Drone Catcher 100 (VDC-100)
## Danh sách Yêu cầu Kỹ thuật - Giai đoạn 1

**Project Code:** VN-CUA-001
**Phase:** 1 - Task Clarification (Steps 3-5)
**Date:** 2026-02-08
**Source Documents:**
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]
- [[VN-CUA-001_product_spec|Product Specification v1.4]]
- [[VN-CUA-001_Systems_Analysis|Systems Analysis]]
- SkyWall 100 RE Analysis (baseline)

---

# 1. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-08 | Engineering | Extracted from product_spec v1.4; consolidated Steps 3-5 |

---

# 2. PROJECT OVERVIEW

| Field | Value |
|-------|-------|
| **Product Name** | Vietnamese Drone Catcher 100 (VDC-100) |
| **Codename** | Lưới Trời (Sky Net) |
| **Project Code** | VN-CUA-001 |
| **Customer** | Vietnamese security forces (Airport, Police, Military, CIP) |
| **End Users** | C-UAS operators (field security personnel) |
| **Target Cost** | ≤$6,000 selling / ≤$2,000 production |
| **Local Content** | ≥70% by value |
| **RE Baseline** | SkyWall 100 (OpenWorks Engineering, UK) |
| **ODI Strategy** | DOMINANT (best value in underserved market) |

---

# 3. REQUIREMENTS SUMMARY

| # | Category | Demands (D) | Wishes (W) | Total | ODI-Linked | Quantified |
|---|----------|-------------|------------|-------|------------|------------|
| 1 | Geometry | 3 | 2 | 5 | 0 | 100% |
| 2 | Kinematics | 5 | 2 | 7 | 4 | 100% |
| 3 | Forces | 5 | 0 | 5 | 0 | 100% |
| 4 | Energy | 4 | 1 | 5 | 0 | 100% |
| 5 | Material | 5 | 0 | 5 | 0 | 100% |
| 6 | Signals | 7 | 1 | 8 | 2 | 100% |
| 7 | Safety | 4 | 1 | 5 | 0 | 100% |
| 8 | Ergonomics | 6 | 1 | 7 | 1 | 100% |
| 9 | Production | 3 | 2 | 5 | 0 | 100% |
| 10 | Quality | 6 | 1 | 7 | 3 | 100% |
| 11 | Assembly | 4 | 1 | 5 | 2 | 100% |
| 12 | Transport | 3 | 1 | 4 | 0 | 100% |
| 13 | Operation | 2 | 3 | 5 | 0 | 100% |
| 14 | Maintenance | 3 | 1 | 4 | 0 | 100% |
| 15 | Costs | 5 | 2 | 7 | 1 | 100% |
| 16 | Schedule | 5 | 0 | 5 | 0 | 100% |
| **TOTAL** | | **70** | **19** | **89** | **13** | **100%** |

**Overall Quantification Rate:** 89/89 = **100%** (target ≥80%)

---

# 4. DETAILED REQUIREMENTS

## 4.1 GEOMETRY (Kích thước & Hình học) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-GEO-01 | System weight (loaded, with projectile) | **D** | ≤8 kg | Target 7 kg | I | Ergonomics study | — | Lighter than SkyWall (10 kg) |
| CUA-GEO-02 | Overall length (assembled) | **D** | ≤1200 mm | — | I | Portability req | — | Single-person carry |
| CUA-GEO-03 | Barrel inner diameter | **D** | 100 ±5 mm | ±5 mm | I | Projectile fit | — | Matches VDC-P40 projectile |
| CUA-GEO-04 | Barrel length | W(4) | 700-900 mm | ±50 mm | I | Ballistic perf. | — | Longer = higher velocity |
| CUA-GEO-05 | Collapsed length (if folding stock) | W(3) | ≤800 mm | — | I | Transport req | — | For vehicle/backpack carry |

---

## 4.2 KINEMATICS (Động học) — 7 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-KIN-01 | Muzzle velocity | **D** | 35-45 m/s | ±2 m/s | T | Range calc | — | Sufficient for 80m range |
| CUA-KIN-02 | Effective range (stationary target) | **D** | ≥80 m | — | T | RE baseline | **O-46: 13.5** | SkyWall ref: 100m |
| CUA-KIN-03 | Maximum range (ballistic) | W(3) | ≥120 m | — | T | Extended use | — | Reduced accuracy accepted |
| CUA-KIN-04 | Net deploy time after launch | **D** | 1.5-2.5 sec | ±0.3 sec | T | Intercept timing | **O-43: 13.5** | Timer/barometric trigger |
| CUA-KIN-05 | Parachute descent rate | **D** | 3-5 m/s | ±0.5 m/s | T | Soft landing | O-63: 13.0 | Evidence preservation |
| CUA-KIN-06 | First-shot hit prob. (stationary, 50m) | **D** | ≥70% | — | T | ODI O-48 | **O-48: 15.0** | Top ODI priority |
| CUA-KIN-07 | Hit prob. (moving 10 m/s, 50m) | **D** | ≥50% | — | T | ODI O-38 | **O-38: 14.5** | 2nd ODI priority |

---

## 4.3 FORCES (Lực & Tải trọng) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-FOR-01 | Trigger pull force | **D** | 20-40 N | ±5 N | T | MIL-STD-1472 | — | Comfortable + safe |
| CUA-FOR-02 | Recoil impulse | **D** | ≤15 Ns | — | T | Shoulder-fired | — | Manageable for all operators |
| CUA-FOR-03 | Operating pressure (regulated) | **D** | 100-150 bar | ±5 bar | I | Pneumatic design | — | Regulator output |
| CUA-FOR-04 | Storage pressure (cylinder) | **D** | 200-300 bar | ±10 bar | I | HPA cylinder spec | — | Standard HPA range |
| CUA-FOR-05 | Drop survival | **D** | 1 m onto concrete | — | T | Handling abuse | — | MIL-STD-810H Method 516 |

---

## 4.4 ENERGY (Năng lượng) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-ENE-01 | Gas cylinder capacity | **D** | 0.5 L @ 300 bar | ±0.05 L | I | Shot count calc | — | Stored energy source |
| CUA-ENE-02 | Shots per fill | **D** | ≥5 shots | — | T | Operational use | — | Better than SkyWall (3-5) |
| CUA-ENE-03 | Scope battery life | **D** | ≥8 hours continuous | — | T | Shift duration | — | Single shift coverage |
| CUA-ENE-04 | Scope battery type | **D** | CR123A or 18650 | — | I | Field availability | — | Common in Vietnam |
| CUA-ENE-05 | Cylinder refill time (field) | W(3) | ≤5 min | — | D | Quick turnaround | — | With portable pump |

---

## 4.5 MATERIAL (Vật liệu) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-MAT-01 | Barrel material | **D** | Al 6061-T6 or equiv | — | I | Strength/weight | — | Local CNC capable |
| CUA-MAT-02 | Receiver/housing material | **D** | Al alloy or glass-filled PA6 | — | I | Manufacturing | — | Local capability |
| CUA-MAT-03 | Net material | **D** | UHMWPE or Dyneema | ≥500 N break strength | I | Capture strength | — | Must hold 5 kg drone |
| CUA-MAT-04 | Parachute material | **D** | Ripstop nylon 40D | — | I | Standard recovery | — | Available locally |
| CUA-MAT-05 | Cylinder material | **D** | Al/CF wrapped, DOT-3AL | ≥300 bar rated | I | Pressure safety | — | Import (certified) |

---

## 4.6 SIGNALS (Tín hiệu & Giao tiếp) — 8 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-SIG-01 | LRF measurement range | **D** | 5-150 m | — | T | Targeting | O-12: 11.5 | COTS module |
| CUA-SIG-02 | LRF accuracy | **D** | ±1 m @ 100 m | — | T | Fire solution | O-12: 11.5 | Adequate for manual aim |
| CUA-SIG-03 | Ballistic reticle | **D** | Range marks 20/40/60/80/100 m + lead marks | — | D | ODI O-48, O-38 | **O-48: 15.0** | Key differentiator |
| CUA-SIG-04 | Display sunlight readability | **D** | ≥1000 nits, anti-glare coating | — | D | ODI O-76 | O-76: 12.0 | Vietnam tropical sun |
| CUA-SIG-05 | Projectile communication | W(2) | None (passive deploy) | — | A | Simplicity | — | Timer/barometric only |
| CUA-SIG-06 | Safety interlock indicator | **D** | Arm/safe switch with visual status | — | D | Safety system | — | Mechanical + LED |
| CUA-SIG-07 | Training mode indicator | **D** | Visual distinction (LED color) | — | D | ODI O-79 | O-79: 11.0 | Separate training mode |
| CUA-SIG-08 | Ready status display | **D** | Gas pressure + armed status | — | D | ODI O-27 | O-27: 10.5 | Operator confidence |

---

## 4.7 SAFETY (An toàn) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-SAF-01 | Arm/safe mechanism | **D** | Positive mechanical interlock | — | D | MIL-STD-882E | — | Prevents misfire |
| CUA-SAF-02 | Over-pressure relief | **D** | Auto-relief @ 350 bar | ±10 bar | T | Pressure safety | — | Fail-safe valve |
| CUA-SAF-03 | Muzzle obstruction safety | **D** | No fire if barrel blocked | — | T | Obstruction detect | — | Mechanical/proximity |
| CUA-SAF-04 | Laser eye safety | **D** | Class 1 (IEC 60825) | — | I | LRF safety | — | Eye-safe LRF |
| CUA-SAF-05 | Parachute backup (drogue) | W(3) | Drogue deploys if main fails | — | D | Recovery safety | — | Reduces evidence damage |

---

## 4.8 ERGONOMICS (Công thái học) — 7 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-ERG-01 | Shoulder-fired, single operator | **D** | One person operate + carry | — | D | Portability | — | No crew required |
| CUA-ERG-02 | Adjustable stock length | **D** | ±50 mm adjustment | ±5 mm | I | Operator fit | — | Fits 5th-95th percentile VN |
| CUA-ERG-03 | Ambidextrous controls | W(3) | Left/right operation | — | D | Flexibility | — | Mirror-image controls |
| CUA-ERG-04 | Gloved operation | **D** | Winter glove compatible | — | D | Field use | — | All controls accessible |
| CUA-ERG-05 | Training time to proficiency | **D** | ≤4 hours (70% hit rate) | — | D | ODI O-79 | O-79: 11.0 | Rapid deployment |
| CUA-ERG-06 | Carry fatigue (patrol weight) | **D** | ≤8 kg loaded system | — | D | ODI O-24 | **O-24: 12.0** | Extended patrol |
| CUA-ERG-07 | Carry-to-fire transition | **D** | ≤3 sec (sling to shoulder) | — | T | ODI O-28 | O-28: 11.5 | Rapid response |

---

## 4.9 PRODUCTION (Sản xuất) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-PRO-01 | Local content | **D** | ≥70% by value | — | A | Self-reliance policy | — | Vietnamese production |
| CUA-PRO-02 | Unit production cost | **D** | ≤$2,000 | — | A | Margin target | — | 67% gross margin |
| CUA-PRO-03 | Manufacturing complexity | **D** | Medium (local CNC + molding) | — | A | Feasibility | — | No exotic processes |
| CUA-PRO-04 | Production rate | W(4) | ≥20 units/month | — | A | Demand forecast | — | At steady state |
| CUA-PRO-05 | Special tooling investment | W(3) | ≤$20,000 | — | A | NRE budget | — | Molds + fixtures |

---

## 4.10 QUALITY (Chất lượng) — 7 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-QUA-01 | MTBF (launcher mechanism) | **D** | ≥2,000 cycles | — | A | Reliability | **O-23: 14.6** | 3rd ODI priority |
| CUA-QUA-02 | Design life | **D** | 10 years | — | A | Longevity | — | With scheduled maintenance |
| CUA-QUA-03 | Production defect rate | W(3) | ≤2% at final test | — | A | Quality program | — | Statistical QC |
| CUA-QUA-04 | Warranty period | **D** | 12 months | — | A | Customer commitment | — | Parts + labor |
| CUA-QUA-05 | Net deployment reliability | **D** | ≥98% success rate | — | T | ODI O-43 | **O-43: 13.5** | Mission critical |
| CUA-QUA-06 | Pneumatic system reliability | **D** | ≥99.5% fire-on-demand | — | T | ODI O-23 | **O-23: 14.6** | Must fire when needed |
| CUA-QUA-07 | Tropical climate reliability | **D** | No degradation 40°C/95%RH/1000h | — | T | ODI O-73 | O-73: 12.5 | Vietnam environment |

---

## 4.11 ASSEMBLY (Lắp ráp) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-ASM-01 | Field disassembly | **D** | Tool-free for cleaning | — | D | Maintenance ease | — | Strip/clean/reassemble |
| CUA-ASM-02 | Reload time (projectile) | **D** | ≤8 sec | — | T | ODI O-55 | **O-55: 12.5** | Breach loading |
| CUA-ASM-03 | Cylinder swap time | **D** | ≤30 sec (quick-release) | — | D | Gas refill | O-61: 11.0 | Field replacement |
| CUA-ASM-04 | Total component count | W(3) | ≤80 parts | — | A | Simplicity | — | Reduces failure modes |
| CUA-ASM-05 | Ready-from-standby time | **D** | ≤5 sec | — | T | ODI O-19 | **O-19: 12.5** | Always-ready mode |

---

## 4.12 TRANSPORT (Vận chuyển) — 4 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-TRA-01 | Storage temperature | **D** | -40 to +70°C | — | T | Warehouse storage | — | MIL-STD-810H |
| CUA-TRA-02 | Transport case | **D** | Hard case, ≤15 kg total | — | I | Logistics | — | System + 5 projectiles |
| CUA-TRA-03 | HPA cylinder transport | **D** | DOT/TC approved cylinder | — | I | Regulation | — | Hazmat compliance |
| CUA-TRA-04 | Vehicle mount compatibility | W(2) | Clamp-compatible rail | — | D | Mobile ops | — | Toyota Hilux/similar |

---

## 4.13 OPERATION (Vận hành) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-OPR-01 | Operating temperature | **D** | -10 to +55°C | — | T | Vietnam climate | — | MIL-STD-810H 501/502 |
| CUA-OPR-02 | Humidity | **D** | Up to 95% RH | — | T | Tropical | — | MIL-STD-810H 507 |
| CUA-OPR-03 | Rain operation | W(4) | Light rain (≤10 mm/hr) | — | D | Field use | — | IPX4 equivalent |
| CUA-OPR-04 | Dust/sand resistance | W(3) | Dust-resistant seals | — | T | Field use | — | MIL-STD-810H 510 |
| CUA-OPR-05 | Operating altitude | W(2) | 0-3,000 m ASL | — | T | Mountain operations | — | Pressure compensation |

---

## 4.14 MAINTENANCE (Bảo trì) — 4 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-MNT-01 | Field maintenance tools | **D** | Standard tools only (no special) | — | D | Accessibility | — | Metric Allen + wrench set |
| CUA-MNT-02 | Cleaning interval | **D** | Every 50 shots | — | D | Practicality | — | Operator-level |
| CUA-MNT-03 | Seal replacement interval | W(3) | Every 500 shots | — | D | Scheduled maint. | — | Depot-level |
| CUA-MNT-04 | Spare parts availability | **D** | 10 year commitment | — | A | Lifecycle support | — | Buffer inventory in-country |

---

## 4.15 COSTS (Chi phí) — 7 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-CST-01 | Unit selling price | **D** | ≤$6,000 | — | A | Market position | — | 80% less than SkyWall |
| CUA-CST-02 | Unit production cost | **D** | ≤$2,000 | — | A | Margin target | — | BOM est. $1,600 |
| CUA-CST-03 | Projectile unit cost | **D** | ≤$80/unit | — | A | ODI O-72 | **O-72: 12.0** | Consumable economics |
| CUA-CST-04 | NRE budget (total development) | W(3) | ≤$150,000 | — | A | Investment cap | — | Phases 1-4 |
| CUA-CST-05 | 5-year TCO per unit | W(3) | ≤$8,000 | — | A | Lifecycle cost | — | Incl. projectiles + maint. |
| CUA-CST-06 | Net reusability | W(3) | ≥3 uses per net | — | A | ODI O-66 | O-66: 10.5 | Reduce cost/engagement |
| CUA-CST-07 | Training projectile cost | W(3) | ≤$30/unit | — | A | ODI O-80 | O-80: 10.0 | Lower cost for training |

---

## 4.16 SCHEDULE (Tiến độ) — 5 Requirements

| ID | Requirement | D/W | Value/Range | Tolerance | Verify | Source | ODI | Notes |
|----|-------------|-----|-------------|-----------|--------|--------|-----|-------|
| CUA-SCH-01 | Preliminary Design Review | **D** | Month 3 | ±2 weeks | D | Milestone | — | Gate 1→2 |
| CUA-SCH-02 | Critical Design Review | **D** | Month 6 | ±2 weeks | D | Milestone | — | Gate 2→3 |
| CUA-SCH-03 | Prototype delivery (3 units) | **D** | Month 10 | ±4 weeks | D | Milestone | — | DV units |
| CUA-SCH-04 | Qualification testing complete | **D** | Month 14 | ±4 weeks | D | Milestone | — | Environmental + performance |
| CUA-SCH-05 | Production start | **D** | Month 16 | ±4 weeks | D | Milestone | — | Pilot 10 units |

---

# 5. ODI TRACEABILITY MATRIX

Requirements linked to high-opportunity ODI outcomes (Score ≥12):

| ODI ID | Outcome | Opp Score | Req IDs | Design Response |
|--------|---------|-----------|---------|-----------------|
| **O-48** | First-shot hit probability | **15.0** | CUA-KIN-06, CUA-SIG-03 | LRF + ballistic reticle |
| **O-38** | Hit moving target (10 m/s) | **14.5** | CUA-KIN-07, CUA-SIG-03 | Lead angle markings |
| **O-23** | Equipment reliability | **14.6** | CUA-QUA-01, CUA-QUA-06 | Robust pneumatic design |
| **O-46** | Effective range | **13.5** | CUA-KIN-02 | Optimize barrel/pressure |
| **O-43** | Net deployment reliability | **13.5** | CUA-KIN-04, CUA-QUA-05 | Timer + barometric backup |
| **O-63** | Evidence preservation | **13.0** | CUA-KIN-05 | Parachute soft landing |
| **O-55** | Reload time | **12.5** | CUA-ASM-02 | Breech loading ≤8 sec |
| **O-19** | Ready from standby | **12.5** | CUA-ASM-05 | Always-ready mode |
| **O-73** | Tropical reliability | **12.5** | CUA-QUA-07 | Environmental testing |
| **O-24** | Carry fatigue | **12.0** | CUA-ERG-06, CUA-GEO-01 | Weight ≤8 kg |
| **O-72** | Projectile cost | **12.0** | CUA-CST-03 | ≤$80/unit target |
| **O-76** | Sunlight visibility | **12.0** | CUA-SIG-04 | ≥1000 nits display |
| **O-33** | Lead angle accuracy | **12.0** | CUA-SIG-03 | Calibrated reticle |

**Coverage:** 13/13 high-opportunity outcomes mapped to requirements (100%)

---

# 6. PRELIMINARY BOM ESTIMATE

| Category | Key Items | Est. Cost | Local % | Source |
|----------|-----------|-----------|---------|--------|
| Barrel Assembly | Tube, chamber, muzzle brake | $150 | 100% | Local CNC |
| Gas System | Cylinder, regulator, valve, lines | $250 | 50% | Cylinder: import |
| Trigger/Receiver | Housing, trigger group, linkage | $200 | 100% | Local CNC/molding |
| Scope Assembly | LRF, display, battery, reticle | $400 | 20% | COTS import |
| Stock/Furniture | Stock, grip, butt pad, sling | $100 | 100% | Local |
| Projectile (×5) | Net, parachute, body, weights | $250 | 80% | Net material local |
| Miscellaneous | Fasteners, seals, case | $100 | 80% | Mixed |
| Assembly/Test | Labor, QC, packaging | $150 | 100% | Local |
| **TOTAL** | | **$1,600** | **~72%** | |

**Selling Price:** $6,000 | **Gross Margin:** 73% | **Local Content:** 72%

---

# 7. OPEN ISSUES & TBD

| Issue ID | Description | Owner | Target Date | Status |
|----------|-------------|-------|-------------|--------|
| TBD-001 | Validate LRF module selection (cost vs accuracy) | Optics Eng. | Month 2 | Open |
| TBD-002 | Net material sourcing (Dyneema vs UHMWPE local) | Materials Eng. | Month 2 | Open |
| TBD-003 | DOT/TC cylinder certification for Vietnam market | Regulatory | Month 3 | Open |
| TBD-004 | Training projectile design (reduced cost variant) | Projectile Eng. | Month 4 | Open |
| TBD-005 | Field survey validation of ODI scores (200+ operators) | Marketing | Month 6 | Open |

---

# DOCUMENT LINKS

- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]
- [[01_requirements/stakeholder_analysis|Stakeholder Analysis]]
- [[01_requirements/standards_compliance|Standards Compliance Matrix]]
- [[01_requirements/validation_report|Validation Report]]
- [[VN-CUA-001_product_spec|Master Product Specification]]

---

*This requirements list follows the Pahl & Beitz systematic design methodology (VDI 2221), Steps 3-5 of Phase 1 Task Clarification.*
