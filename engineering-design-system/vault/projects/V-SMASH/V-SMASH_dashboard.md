---
project: V-SMASH
type: dashboard
version: 1.0
created: 2026-02-04
updated: 2026-02-04
status: active
---

# V-SMASH PROJECT DASHBOARD
## Vietnam Indigenous C-UAS Fire Control System

**Last Updated:** 2026-02-04

---

## 📊 PROJECT OVERVIEW

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                     V-SMASH FIRE CONTROL SYSTEM                            ║
║             Vietnamese AI-Powered Counter-UAS Platform Family              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  Mission: Single-shot-single-hit capability against moving aerial targets  ║
║  Status:  PHASE 2 - CONCEPTUAL DESIGN (Active)                            ║
║  Target:  9-Product Portfolio | $24.3M TAM (10-year)                       ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 🎯 KEY METRICS

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| **Requirements Quantified** | ≥80% | 85% | ✅ |
| **VDI 2225 Concept Score** | ≥70% | 81% (Concept A) | ✅ |
| **Local Content** | ≥60% | 65-75% (planned) | ✅ |
| **Cost vs Import** | ≤70% | 40-60% | ✅ |
| **RE Analyses Complete** | 10 | 10 | ✅ |
| **Products Defined** | 9 | 9 | ✅ |

---

## 📈 PHASE STATUS

```
PHASE 0 ████████████████████ 100% ✅ ODI Analysis Complete
PHASE 1 ████████████████████ 100% ✅ Requirements v1.5 (101 req)
PHASE 2 ████████████████████ 100% ✅ Product Variants v2.0
PHASE 3 ░░░░░░░░░░░░░░░░░░░░   0% ⏳ Awaiting Gate 2→3
PHASE 4 ░░░░░░░░░░░░░░░░░░░░   0% ⏳ Future
```

### Current Phase: 2 - Conceptual Design

| Deliverable | Status | Document |
|-------------|--------|----------|
| Abstraction | ✅ Complete | V-SMASH_P2_01 |
| Function Structure | ✅ v1.3 | [[V-SMASH_P2_01_function_structure]] |
| Morphological Matrix | ✅ v1.3 | [[V-SMASH_P2_02_morphological_matrix]] |
| Concept Evaluation | ✅ v1.4 (9 products) | [[V-SMASH_P2_03_concept_evaluation]] |
| Product Variants | ✅ v2.0 (9 products) | [[V-SMASH_P2_05_product_variants_spec]] |
| Product Portfolio | ✅ v3.0 | [[V-SMASH_P2_06_product_portfolio_v2]] |

---

## 🔍 REVERSE ENGINEERING SUMMARY

### 10 Systems Analyzed

| # | System | Type | Key Insight | Proposed Req |
|---|--------|------|-------------|--------------|
| 1 | SMASH 2000+ | Handheld FCS | Human-in-loop, fail-safe | R1-R45 |
| 2 | ARCAS | AR/Multi-tgt | Multi-target tracking | R46-R52 |
| 3 | ARBEL | C-UAS AI | Drone classification | R53-R61 |
| 4 | SMASH 3000 | Lightweight | 72h battery, mesh | R62-R68 |
| 5 | SMASH X4 | 4x Magnified | LRF, etched reticle | R69-R76 |
| 6 | SMASH Connect | Connectivity | MAGTAB, ATAK, HMG | R77-R91 |
| 7 | SMASH Hopper 5000 | Full RCWS | 15kg, 360° pan | R92-R99 |
| 8 | SMASH Hopper Light | Ultra-light RCWS | 10kg, single-soldier | R100-R107 |
| 9 | SMASH DOME | Integrated C-UAS | Detect-track-engage | R108-R115 |
| 10 | SMASH Dragon | Armed UAV | Airborne FCS | R116-R120 (Wishes) |

### RE Documents

- [[V-SMASH_RE_01_SMASH2000_analysis]]
- [[V-SMASH_RE_02_ARCAS_analysis]]
- [[V-SMASH_RE_03_ARBEL_analysis]]
- [[V-SMASH_RE_04_SMASH3000_analysis]]
- [[V-SMASH_RE_05_SMASHX4_analysis]]
- [[V-SMASH_RE_06_SMASH_connectivity_analysis]]
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis]]
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis]]
- [[V-SMASH_RE_09_SMASH_DOME_analysis]]
- [[V-SMASH_RE_03_SMASH_Dragon_analysis]]

---

## 📋 REQUIREMENTS SUMMARY

**Document:** [[V-SMASH_P1_01_requirements_list]] v1.5

| Category | Count | Type |
|----------|-------|------|
| **Total Requirements** | **101** | |
| Demands (D) | 77 | Mandatory |
| Wishes (W) | 24 | Desirable |

### By Category

| Category | Req Count | Examples |
|----------|-----------|----------|
| Performance | 12 | Hit prob ≥60%, range 800m |
| Environmental | 10 | -10° to +55°C, IP67 |
| Interface | 8 | Picatinny, HMG mount |
| Safety | 6 | Human-in-loop, fail-safe |
| Power | 5 | 8h operation, hot-swap |
| C4I/Network | 8 | CoT, ATAK, mesh |
| C-UAS Specific | 8 | Drone classification AI |
| RCWS | 8 | R92-R99: 15kg, 360° |
| RCWS-LITE | 8 | R100-R107: 10kg single-soldier |
| C-UAS System | 8 | R108-R115: DOME integrated |
| UAV Payload | 5 | R116-R120: Future (Wishes) |
| Other | 15 | Cost, local content, training |

---

## 🛒 PRODUCT PORTFOLIO

**Document:** [[V-SMASH_P2_06_product_portfolio_v2]] v3.0

### 9 Products | $24.3M TAM (10-year)

```
PRODUCT FAMILY ARCHITECTURE
═══════════════════════════════════════════════════════════════════════

    HANDHELD FCS                    PLATFORM-MOUNTED
    ────────────                    ────────────────
┌─────────────────┐           ┌─────────────────────────┐
│ V-SMASH LITE    │ $3,000    │ V-SMASH HMG             │ $6,000
│ V-SMASH PRO     │ $5,000    │ V-SMASH MARITIME        │ $6,500
│ V-SMASH PRO-X   │ $7,000    │ V-SMASH RCWS-LITE (NEW) │ $8,000
└─────────────────┘           │ V-SMASH RCWS            │ $12,000
                              └─────────────────────────┘
    SYSTEM                          ACCESSORY
    ──────                          ─────────
┌─────────────────┐           ┌─────────────────┐
│ V-SMASH DOME    │ $50,000   │ V-SMASH C4I HUB │ $2,000
│ (Integrated     │           │ (Squad coord)   │
│  C-UAS) (NEW)   │           └─────────────────┘
└─────────────────┘
```

### Market Summary

| Segment | Products | Price Range | 10-Year Volume | Revenue |
|---------|----------|-------------|----------------|---------|
| Handheld | 3 | $3K-$7K | 1,500 units | $7.0M |
| Platform | 4 | $6K-$12K | 800 units | $7.3M |
| System | 1 | $50K | 100 units | $5.0M |
| Accessory | 1 | $2K | 2,500 units | $5.0M |
| **TOTAL** | **9** | **$2K-$50K** | **4,900 units** | **$24.3M** |

### Development Investment

| Phase | Investment | Products |
|-------|------------|----------|
| Core Platform (Yr 1-2) | $400K | LITE, PRO, HMG |
| Extended Products (Yr 2-3) | $250K | PRO-X, MARITIME, RCWS |
| System Integration (Yr 3-4) | $100K | RCWS-LITE, DOME, C4I HUB |
| **TOTAL** | **$750K** | **9 products** |

---

## 🔧 FUNCTION STRUCTURE

**Document:** [[V-SMASH_P2_01_function_structure]] v1.3
**Morphological Matrix:** [[V-SMASH_P2_02_morphological_matrix]] v1.3

### 10 Function Groups | 40 Sub-functions | 25 Working Principles

| Group | Name | Sub-functions | Applies To |
|-------|------|---------------|------------|
| **F1** | Image Acquisition | 4 | All |
| **F2** | Target Detection & Tracking | 6 | All |
| **F3** | Ballistic Computation | 4 | All |
| **F4** | Fire Control Logic | 5 | All |
| **F5** | Power Management | 4 | All |
| **F6** | Operator Interface | 5 | All |
| **F7** | Data Management | 4 | All (optional) |
| **F8** | RCWS Platform Control | 8 | RCWS, RCWS-LITE |
| **F9** | Integrated C-UAS System | 8 | DOME |
| **F_AUX** | Environmental Protection | 4 | All |

### Signal Flows

- **Core flows:** S1-S17 (All products)
- **RCWS flows:** S18-S23 (Platform control)
- **DOME flows:** S24-S29 (C-UAS integration)

---

## 📅 DEVELOPMENT ROADMAP

```
2026 Q1-Q2: Complete Phase 2 Conceptual Design
            ├── Function structure finalization
            ├── Morphological matrix update (F8, F9)
            ├── Concept selection ratification
            └── Gate 2→3 review

2026 Q3-Q4: Phase 3 Embodiment Design
            ├── Layout design
            ├── DfX review (12 categories)
            ├── Material selection
            └── Local content verification

2027 Q1-Q2: Phase 4 Detail Design
            ├── CAD models
            ├── BOM creation
            └── Prototype build

2027 Q3-Q4: Prototype Testing
            ├── Environmental testing
            ├── Live fire testing
            └── User acceptance

2028+:      Production & Variants
            ├── Initial production (LITE, PRO, HMG)
            ├── Extended variants (PRO-X, MARITIME, RCWS)
            └── System integration (RCWS-LITE, DOME)
```

---

## 📝 NEXT ACTIONS

### Immediate (Gate 2→3 Review)

- [x] Update morphological matrix with F8/F9 working principles ✅ v1.3
- [x] Validate concept evaluation for new variants ✅ v1.4
- [x] Update product variants spec ✅ v2.0 (9 products)
- [ ] Prepare Gate 2→3 review package
- [ ] Stakeholder sign-off on 9-product portfolio

### Phase 3 Preparation

- [ ] Layout design methodology selection
- [ ] DfX priority ranking for defense products
- [ ] Material database for Vietnam suppliers
- [ ] Local content analysis framework

---

## 📁 DOCUMENT INDEX

### Phase 0: ODI
- [[V-SMASH_P0_01_ODI_analysis]] (v2.0 - Integrated)

### Phase 1: Requirements
- [[V-SMASH_P1_01_requirements_list]] (v1.5)

### Phase 2: Conceptual Design
- [[V-SMASH_P2_01_function_structure]] (v1.3)
- [[V-SMASH_P2_02_morphological_matrix]]
- [[V-SMASH_P2_03_concept_evaluation]]
- [[V-SMASH_P2_04_conceptual_design_v1_1]]
- [[V-SMASH_P2_05_product_variants_spec]]
- [[V-SMASH_P2_06_product_portfolio_v2]] (v3.0)

### Reverse Engineering
- [[V-SMASH_RE_01_SMASH2000_analysis]]
- [[V-SMASH_RE_02_ARCAS_analysis]]
- [[V-SMASH_RE_03_ARBEL_analysis]]
- [[V-SMASH_RE_04_SMASH3000_analysis]]
- [[V-SMASH_RE_05_SMASHX4_analysis]]
- [[V-SMASH_RE_06_SMASH_connectivity_analysis]]
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis]]
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis]]
- [[V-SMASH_RE_09_SMASH_DOME_analysis]]
- [[V-SMASH_RE_03_SMASH_Dragon_analysis]]

### Other
- [[V-SMASH_00_project_brief]]
- [[V-SMASH_SESSION_REPORT_2026-02-04]]

---

## 📊 QUICK STATS

```
╔═════════════════════════════════════════════════════════════╗
║                  V-SMASH PROJECT SUMMARY                     ║
╠═════════════════════════════════════════════════════════════╣
║  RE Analyses:      10 systems analyzed                       ║
║  Requirements:     101 total (77 Demands, 24 Wishes)         ║
║  Products:         9 variants ($3K - $50K)                   ║
║  Function Groups:  10 (40 sub-functions, 25 WPs)             ║
║  Signal Flows:     29 defined                                ║
║  TAM (10-year):    $24.3M                                    ║
║  Investment:       $750K total development                   ║
║  Local Content:    65-75% target                             ║
║  Current Phase:    2 - Conceptual Design (85% complete)      ║
╚═════════════════════════════════════════════════════════════╝
```

---

*Dashboard auto-generated from project documents*
*Use `/status` or `/s` for quick status check*
