---
title: "V-SMASH Project Overview"
title_vi: "Tổng quan dự án V-SMASH"
project: v-smash
type: overview
created: 2026-01-25
updated: 2026-01-29
status: active
phase: concept
gate: G1
tags: [fire-control, ai, counter-uas, jetson, computer-vision]
entities:
  - type: product
    name: V-SMASH
  - type: reference
    name: SmartShooter-SMASH
  - type: platform
    name: Jetson-Xavier-NX
  - type: application
    name: Counter-UAS
metrics:
  gate_status: ready
  vdi_score: 85
  budget_vnd: 50000000
links:
  children:
    - "[[requirements/v1.1-summary]]"
    - "[[design/function-structure]]"
    - "[[quality/Gate-1-Ready]]"
---

# V-SMASH: Vietnamese AI Fire Control System

> **Project Code**: V-SMASH-001
> **Status**: Conceptual Design Complete ✅
> **Reference**: SmartShooter SMASH (Israel)

---

## 🎯 Mission Statement

Develop an **indigenous Vietnamese AI-powered fire control system** that enables:
- Single-shot-single-hit capability against moving aerial and ground targets
- Integration with Vietnamese weapon platforms (MTB-20, rifles, vehicle weapons)
- Sustainable local production and maintenance
- Counter-UAS capability for national defense

---

## 📊 Project Summary

| Attribute | Value |
|-----------|-------|
| **Selected Concept** | V4: Phased Development |
| **VDI 2225 Score** | 85% (Highest) |
| **Unit Cost Target** | <$3,000 USD |
| **Local Content** | 63% (>60% requirement) |
| **Development Timeline** | 24 months (Phase 1+2) |
| **Key Platforms** | AK/M16/Galil, PKM, NSV, DShK, MTB-20 |

---

## 🏗️ Product Family

```
V-SMASH CORE MODULE
├── V-SMASH-LITE (Rifle-mounted)
│   ├── Weight: <1.2kg
│   ├── Range: 250m
│   └── Cost: <$3,000
├── V-SMASH-PRO (Extended range)
│   ├── Weight: <1.8kg
│   ├── Range: 500m
│   └── Thermal option
└── V-SMASH-RWS (MTB-20 integration)
    ├── Weight: <3kg
    ├── Range: 600m
    └── Vehicle power
```

---

## 🛠️ Key Technical Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Processing Platform | NVIDIA Jetson Nano | Edge AI, local availability |
| AI Detection | YOLOv8-nano | Best accuracy/speed tradeoff |
| Tracking | Kalman Filter | Proven, local expertise |
| Ballistics | Point-mass 3DOF | Sufficient accuracy, fast |
| Trigger Mechanism | Solenoid | Simple, reliable, cheap |
| Optic Style | See-through reflex | Unlimited eye relief |

---

## 📁 Project Structure

```
v-smash/
├── README.md (this file)
├── requirements/
│   └── v1.1-summary.md
├── design/
│   ├── function-structure.md
│   ├── morphological-matrix.md
│   ├── working-principles.md
│   └── system-architecture.md
├── decisions/
│   └── log.md
├── quality/
│   └── vdi-2225-evaluation.md
└── research/
    └── smash-analysis.md
```

---

## 📋 Key Requirements Summary

### Critical (Must Have)
- R01: 95% detection @ 300m (drones)
- R03: Track up to 50 m/s targets
- R04: <100ms fire solution latency
- R31: Human-in-the-loop enforcement
- R32: Fail-safe to manual operation
- R18: <1.5kg weight (LITE variant)

### Performance Targets
| Metric | Target |
|--------|--------|
| Detection (drone) | 95% @ 300m |
| Detection (person) | 95% @ 500m |
| Hit improvement | 3x baseline |
| Processing latency | <50ms end-to-end |

---

## 🗓️ Development Roadmap

### Phase 1: Foundation (Months 1-12)
**Q1 (Months 1-3): Research & Setup**
- [ ] Procure Jetson Nano dev kits (5 units)
- [ ] Set up development environment
- [ ] Camera integration and basic capture
- [ ] Classical CV detection prototype (HOG+SVM)

**Q2 (Months 4-6): Core Algorithms**
- [ ] Kalman filter implementation
- [ ] Ballistic computer development
- [ ] Integration demo

**Q3 (Months 7-9): Hardware Prototype**
- [ ] Mechanical design (CAD)
- [ ] Carrier board design
- [ ] First prototype assembly
- [ ] PDR (Preliminary Design Review)

**Q4 (Months 10-12): Integration & Test**
- [ ] Mount on weapon, range test
- [ ] Drone imagery dataset (1000+ images)
- [ ] CDR (Critical Design Review)

### Phase 2: AI Integration (Months 13-24)
- Q5: YOLO model training
- Q6: Trigger mechanism integration
- Q7: System integration & field testing
- Q8: Production preparation

---

## ⚠️ Key Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AI accuracy insufficient | Medium | High | Classical CV fallback |
| Real-time performance | Low | High | Upgrade to Xavier NX |
| Import restrictions | Medium | Medium | Increase local content |

---

## 🔗 Related Projects

- [[domains/bb-01/README]] - BB-01 LOMAH (shares acoustic detection learnings)
- MTB-20 RCWS - Primary vehicle integration platform

---

## 📝 Quick Links

- [[requirements/v1.1-summary]] - Full requirements list
- [[decisions/log]] - Decision history
- [[design/function-structure]] - Function decomposition
- [[quality/vdi-2225-evaluation]] - Concept evaluation

---

*Last updated: 2026-01-26*
*Design Phase: Conceptual Design Complete*
