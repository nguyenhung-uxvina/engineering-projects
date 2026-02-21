---
project: VN-RNG-001
phase: 0
type: project_brief
version: 1.0
created: 2026-02-08
status: draft
---

# Project Brief: VN-RNG-001 - LOMAH Acoustic Shooting Range System

## Product Vision

Vietnamese-designed and manufactured **LOMAH (Location of Miss and Hit)** system for military live-fire marksmanship training. Acoustic sensor technology providing real-time shot placement feedback to instructors and shooters via tablet displays.

## Problem Statement

Vietnamese military shooting ranges currently use **manual pit-based scoring** requiring 4-8 personnel per range day, 3+ days for qualification cycles, no real-time feedback, and paper-based records. This results in:
- 60%+ of training time wasted walking downrange
- Instructor can observe 4-8 lanes (not 16+)
- No data-driven coaching capability
- No cross-session performance tracking
- Full dependency on imported systems ($10,000-25,000/lane) with no local support

## Opportunity

ODI analysis identified **11 EXTREME opportunity outcomes** (score >15) and **14 HIGH opportunities** (12-15). The current manual baseline creates satisfaction scores of 1.5-3.0/10 on core outcomes, leaving massive room for improvement.

## Product Concept: Smart LOMAH (Concept B)

| Feature | Specification |
|---------|--------------|
| **Technology** | Acoustic MEMS microphone array (8x), GCC-PHAT algorithm |
| **Accuracy** | <5mm standard, <3mm precision variant |
| **Latency** | <100ms shot-to-display |
| **Lanes** | 1-32 (modular) |
| **Display** | Android tablets (COTS) + web dashboard |
| **Intelligence** | AI error pattern detection, auto sight adjustment, cross-session tracking |
| **Environment** | IP67, -10C to 50C continuous (70C peak), tropical hardened |
| **Power** | 12V DC / lithium battery (10h+) |
| **Distances** | 25-600m+ |
| **Calibers** | 5.56mm to 12.7mm (supersonic) |

## Target Markets

| Segment | Size | Product Variant | Price Target |
|---------|------|-----------------|-------------|
| Throughput Maximizers (45%) | 50-80 ranges | VN-RNG-A (Multi-Lane) | $5,000-8,000/lane |
| Precision Trainers (30%) | 20-30 systems | VN-RNG-B (Precision) | $8,000-12,000/lane |
| Field Deployers (25%) | 100-200 systems | VN-RNG-C (Portable) | $2,000-4,000/lane |

## Strategic Rationale

| Factor | Target |
|--------|--------|
| **Growth strategy** | DOMINANT - market leadership |
| **Cost vs import** | ≤50-60% of Western import |
| **Local content** | 60-75% by value |
| **Vendor independence** | 100% - zero proprietary lock-in |
| **Standards** | MIL-STD-810H (environmental) + TCVN |

## Key Differentiators vs Import

1. **Tropical-native design** - not adapted from cold-climate products
2. **Zero vendor lock-in** - COTS components, open firmware, standard connectors
3. **AI-enhanced coaching** - software intelligence beyond basic Western LOMAH
4. **Vietnamese support** - local repair, parts, and training
5. **50-60% cost advantage** - Vietnamese manufacturing economics

## ODI Customer Scorecard Result

| Concept | Score (1-10) | Recommendation |
|---------|-------------|----------------|
| Current (manual pit) | 2.43 | Replace |
| A: Basic LOMAH | 6.97 | Good but lacks depth |
| **B: Smart LOMAH** | **8.46** | **SELECTED - High success probability** |
| C: Import (InVeris) | 7.20 | Good but vendor-dependent |

## Phase 0 Deliverables
- [[00_odi/odi_analysis.md]] - Full ODI analysis (Steps 1-10)

## Next Steps
- Phase 1: Task Clarification - Requirements list (16 categories) driven by ODI outcomes
- Field survey: 60-100 Vietnamese military instructors to validate opportunity scores

## References
- [[LOMAH-System|LOMAH System Technical Research]] - Comprehensive technical reference
