---
project: VN-TRN-001
phase: 0
type: project-brief
version: 1.0
created: 2026-02-06
status: active
---

# Project Brief: VN-TRN-001 - Vietnamese LOMAH Electronic Scoring System

## 1. Project Identity

| Item | Detail |
|------|--------|
| **Project Code** | VN-TRN-001 |
| **Project Name** | Vietnamese LOMAH (Location of Miss and Hit) Electronic Scoring System |
| **Domain** | Training & Simulation - Live Fire Range Equipment |
| **Classification** | UNCLASSIFIED |
| **Start Date** | 2026-02-06 |
| **Current Phase** | Phase 0 - ODI (Customer Insight) |

## 2. Project Objective

Design and develop an indigenous Vietnamese electronic scoring system for live-fire shooting ranges that detects supersonic (and later subsonic) projectile trajectories and determines precise hit/miss location on target planes.

## 3. Strategic Context

### Market Need
- Vietnamese military and police forces currently import LOMAH systems from foreign vendors (Saab, InVeris, Polytronic, TTS, etc.)
- Import costs: $2,500-5,000+ per lane (FOB) + installation + ongoing support
- Dependency on foreign supply chains for critical training infrastructure
- No indigenous Vietnamese capability exists

### Strategic Value
- **Self-sufficiency** in training equipment production
- **Cost reduction** vs. imported systems (target: ≤70% of import cost)
- **Local content** development (target: ≥60% by value)
- **Export potential** to regional markets (ASEAN, Africa)
- **Technology mastery** in acoustic signal processing, embedded systems, range management software

## 4. Competitive Landscape (8 RE Analyses Completed)

| # | Manufacturer | Country | Key Technology | Reference |
|---|-------------|---------|----------------|-----------|
| 1 | Zen Technologies | India | Acoustic TDOA, Ethernet | [[RE_zen_technologies_smart_electronic_target]] |
| 2 | Theissen Training Systems | Germany | Dual delta array, Box Target (subsonic) | [[RE_theissen_training_systems_lomah]] |
| 3 | InVeris (Meggitt) | USA | 3 variants, LSI, multi-comm, 80K+ fielded | [[RE_inveris_training_solutions_lomah]] |
| 4 | Polytronic International | Switzerland | H-Bar, T-Bar, Radar I-Bar (subsonic) | [[RE_polytronic_international_ag_lomah]] |
| 5 | SIUS AG | Switzerland | Electronic scoring | [[RE_SIUS_Analysis]] |
| 6 | Oakwood Controls | UK | H-Bar configuration | [[RE_OakwoodHBar_Analysis]] |
| 7 | TrueZero Target | USA | Advanced scoring | [[RE_TrueZeroTarget_Analysis]] |
| 8 | Saab T&S | Sweden | Calibration-free SASS-4/9, AVTI pixel model | [[RE_saab_lomah]] |

## 5. Key Technology Findings from RE

| Finding | Source | Impact |
|---------|--------|--------|
| Calibration-free acoustic scoring patent **EXPIRED** (WO1991010876A1) | Saab RE | Can legally implement without license |
| Temperature compensation implicit in calibration-free algorithm | Saab RE | Critical for tropical Vietnamese climate |
| FASIT protocol is industry standard (TCP/IP, Ethernet) | InVeris/TTS RE | Adopt for interoperability |
| Box Target (chambered LOMAH) enables subsonic scoring | TTS RE | Vietnamese rubber advantage |
| Radar-based subsonic detection possible | Polytronic RE | Higher tech risk, Phase 3+ |
| Pixel vulnerability model is software-only | Saab AVTI RE | Low-cost high-value differentiator |
| 4 MEMS microphones sufficient for ±10mm accuracy | All RE | Minimizes sensor cost |
| Per-lane BOM $120-510 depending on complexity | All RE | Strong cost advantage over imports |

## 6. Target Specifications (Preliminary)

| Parameter | Target | Basis |
|-----------|--------|-------|
| **Accuracy** | ±10mm at 300m (Phase 1) | Saab SASS-4/9 benchmark |
| **Min velocity** | Mach 1.3 (~440 m/s) Phase 1; subsonic Phase 2 | Industry standard |
| **Caliber range** | 5.56mm - 12.7mm (Phase 1) | Vietnamese military ammo |
| **Detection zone** | 3 × 2.5m (infantry target) | Standard NATO silhouette |
| **Calibration** | Calibration-free (target) | Saab patent expired |
| **Communication** | Ethernet (primary) + WiFi (portable) | FASIT-compatible |
| **Power** | 12 VDC + solar option | Field deployment |
| **IP rating** | IP67 minimum | Tropical environment |
| **Operating temp** | -10°C to +60°C | Vietnamese climate |
| **Local content** | ≥60% by value | National policy target |
| **Unit cost** | ≤$500 per lane (hardware) | ≤70% of import equivalent |

## 7. Phased Development Plan

| Phase | Scope | Key Deliverable |
|-------|-------|-----------------|
| **Phase 0** | ODI - Customer insight & outcome discovery | Job map, opportunity scores |
| **Phase 1** | Requirements - Formal spec from ODI outcomes | Requirements list (16 categories) |
| **Phase 2** | Conceptual Design - 3+ concepts, VDI 2225 evaluation | Selected concept with rationale |
| **Phase 3** | Embodiment Design - Layout, DfX, materials, local content | Production-ready design |
| **Phase 4** | Detail Design - CAD, BOM, prototype, testing | Prototype & test results |

## 8. Related Projects & References

| Reference | Location |
|-----------|----------|
| RE analyses (8 files) | `vault/projects/VN-LOMAH/` |
| LOMAH system reference | `vault/references/LOMAH-System.md` |
| Vietnamese defense context | CLAUDE.md |

---

*Project initiated: 2026-02-06 | Phase 0: ODI Customer Insight*
