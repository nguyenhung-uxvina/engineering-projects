---
project: VN-CUA-001
designation: VDC-100
type: abstraction
phase: 2
step: 1
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Step 1
---

# VN-CUA-001: ABSTRACTION (5-Step Process)
## Vietnamese Drone Catcher 100 (VDC-100)
## Trừu tượng hóa - Giai đoạn 2, Bước 1

**Project Code:** VN-CUA-001
**Phase:** 2 - Conceptual Design (Step 1: Abstraction)
**Date:** 2026-02-08
**Input:** 89 ODI-validated requirements from [[01_requirements/requirements_list|Requirements List]]

---

# 1. PURPOSE

The 5-step abstraction process removes implementation bias from the problem definition. Starting from the specific (validated requirements, stakeholder preferences, existing solutions like SkyWall), we systematically strip away assumptions to arrive at a **solution-neutral problem statement** that opens the design space to ALL possible concepts.

**Why This Matters:**
- SkyWall 300 costs $30,000 — copying it defeats the cost objective
- Vietnamese procurement needs local production — imported designs don't transfer
- ODI data shows underserved outcomes that existing solutions don't address
- A fresh abstraction may reveal non-obvious solution paths

---

# 2. INPUT SUMMARY

## 2.1 From Phase 1 Requirements

| Category | Count | Key Constraints |
|----------|-------|----------------|
| Kinematics (KIN) | 9 | Range ≥80m, muzzle velocity 50-70 m/s, 70% hit rate |
| Geometry (GEO) | 6 | Barrel 800-1100mm, OD ≤120mm, weight ≤8 kg |
| Energy (ENE) | 5 | HPA 300 bar, ≥5 shots/fill, 18650 battery |
| Safety (SAF) | 5 | Mechanical interlock, relief valve, Class 1 LRF |
| Signal/Info (SIG) | 7 | LRF, reticle with lead marks, 1000 nit display |
| **TOTAL** | **89** | Across 16 Pahl & Beitz categories |

## 2.2 From ODI Customer Discovery

| Top Outcomes (Opportunity Score ≥12) | Score |
|--------------------------------------|-------|
| O-48: First-shot hit probability | **15.0** |
| O-23: Equipment reliability | 14.6 |
| O-46: Effective range | 13.5 |
| O-43: Net deployment reliability | 13.5 |
| O-55: Reload speed | 12.5 |
| O-63: Evidence preservation | 13.0 |

## 2.3 From Stakeholder Analysis

| Primary Stakeholders | Core Need |
|---------------------|-----------|
| S1: C-UAS Operator | High first-shot hit, light enough for patrol |
| S3: Procurement Officer | Price ≤70% of import, local content ≥60% |
| S4: Military Commander | Safety, ROE compliance, evidence for prosecution |
| S7: Investigation Unit | Drone captured intact for forensics |

---

# 3. FIVE-STEP ABSTRACTION PROCESS

## Step 1: Eliminate Personal Preferences

Remove all solution-biased language that assumes a specific implementation approach.

| # | Original Statement (Biased) | Preference Removed (Neutral) | Bias Eliminated |
|---|----------------------------|------------------------------|-----------------|
| 1 | "Use SkyWall-style pneumatic launcher" | "Launch projectile to capture drone" | Specific product reference |
| 2 | "Include SmartScope targeting" | "Provide target acquisition assistance" | Specific brand name |
| 3 | "Use Dyneema net" | "Employ capture mechanism" | Specific material |
| 4 | "Aluminum barrel" | "Propel projectile through tube" | Specific material |
| 5 | "Parachute recovery system" | "Control descent of captured target" | Specific mechanism |
| 6 | "Compressed air propulsion" | "Store and release propulsive energy" | Specific energy type |
| 7 | "Laser rangefinder scope" | "Determine distance to target" | Specific sensor |
| 8 | "Shoulder-fired weapon form factor" | "Portable system operable by one person" | Specific form factor |

**Rationale:** The customer brief and SkyWall benchmark heavily biased initial thinking toward "pneumatic shoulder-fired net launcher." By removing these preferences, we allow consideration of drones, ground-launched systems, handheld devices, or entirely novel approaches.

---

## Step 2: Omit Non-Essential Requirements

Separate MUST-have (essential) from WISH (nice-to-have) requirements to focus on the core problem.

### Essential Requirements (MUST — Define the Problem)

| # | Essential Requirement | Source | Why Essential |
|---|----------------------|--------|---------------|
| E1 | Capture airborne drone physically | CUA-KIN-01, O-43 | Core function — without this, no product |
| E2 | Preserve captured drone for evidence | CUA-KIN-05, O-63 | Key differentiator vs. RF jamming |
| E3 | Portable by single operator | CUA-GEO-01, CUA-ERG-06 | Deployment flexibility requirement |
| E4 | Effective against autonomous drones | CUA-KIN-07, O-48 | RF jamming doesn't work on autonomous |
| E5 | Cost ≤$6,000 per unit | CUA-CST-01 | Market positioning vs. $30K imports |
| E6 | Producible in Vietnam (≥70% local) | CUA-PRO-01 | Strategic procurement requirement |
| E7 | Safe for operator and bystanders | CUA-SAF-01 thru SAF-05 | Regulatory / commander requirement |

### Non-Essential Requirements (WISH — Design Space Flexibility)

| # | Non-Essential Requirement | Source | Why Non-Essential |
|---|--------------------------|--------|-------------------|
| N1 | Video tracking system | — | Operator eyes sufficient for basic function |
| N2 | Ballistic computer | CUA-SIG-03 (WISH) | Manual aiming is viable alternative |
| N3 | RF communication with projectile | — | Timer-based deploy works without RF |
| N4 | Modular barrel lengths | — | Single optimized barrel sufficient |
| N5 | Night vision compatibility | CUA-SIG-05 (WISH) | Most engagements are daytime |
| N6 | Magazine/multi-shot capability | — | Single shot with fast reload is viable |
| N7 | Self-tightening net closure | — | Standard net with weights sufficient |

**Rationale:** By identifying only 7 essential requirements, we dramatically simplify the problem space. Any concept that meets E1-E7 is a valid candidate, regardless of how it achieves them.

---

## Step 3: Transform Quantitative to Qualitative

Replace specific numbers with the underlying intent to avoid prematurely constraining the solution space.

| # | Quantitative Requirement | Qualitative Equivalent | Design Space Opened |
|---|-------------------------|----------------------|---------------------|
| Q1 | Range ≥80m | "Engage at tactically useful distance" | Could be 60m, 100m, or variable |
| Q2 | Weight ≤8 kg | "Portable by single operator for extended patrol" | Could be worn, carried, wheeled |
| Q3 | First-shot hit ≥70% | "Accurate enough for practical engagement" | Allows different accuracy strategies |
| Q4 | Price ≤$6,000 | "Affordable for widespread deployment" | Cost optimization flexibility |
| Q5 | Net deploy reliability ≥98% | "Highly reliable capture mechanism" | Mechanism can vary |
| Q6 | Reload ≤8 seconds | "Rapid follow-up engagement capability" | Could mean fast reload OR multi-shot |
| Q7 | Muzzle velocity 50-70 m/s | "Sufficient velocity for ballistic accuracy" | Allows different propulsion types |
| Q8 | Operating temp -10°C to +55°C | "Functional in extreme field conditions" | Multiple environmental strategies |
| Q9 | Capture area ≥3m × 3m | "Cover area sufficient to entangle small drone" | Net, bola, other mechanisms |
| Q10 | Descent rate ≤5 m/s | "Gentle enough to preserve drone evidence" | Parachute, drag, active systems |

**Rationale:** The quantitative requirements were validated in Phase 1, but at this stage they can over-constrain concept generation. "80m range" immediately suggests a pneumatic launcher — but "tactically useful distance" allows consideration of thrown nets (short range), drone-delivered nets (long range), or novel approaches.

---

## Step 4: Generalize Results

Replace domain-specific terminology with universal function descriptions.

| # | Specific (Domain) | Generalized (Universal) | New Possibilities |
|---|-------------------|------------------------|-------------------|
| G1 | "Capture drone with net" | "Physically entangle aerial target" | Bola, sticky, cage, grapple |
| G2 | "Pneumatic propulsion" | "Accelerate projectile to target" | Gas, spring, electromagnetic, chemical |
| G3 | "Parachute recovery" | "Control descent of captured object" | Drogue, autorotation, active thrust |
| G4 | "Laser rangefinder" | "Measure distance to target" | Radar, stadiametric, acoustic, AI |
| G5 | "Trigger mechanism" | "Operator-initiated energy release" | Trigger, button, gesture, voice |
| G6 | "Barrel assembly" | "Guide and direct projectile" | Tube, rail, track, open launch |
| G7 | "Safety interlock" | "Prevent unintended discharge" | Mechanical, electronic, biometric |
| G8 | "Shoulder-fired" | "Human-aimed portable system" | Shoulder, hip, mounted, remote |
| G9 | "Breech-loading" | "Insert projectile into launch system" | Breech, muzzle, magazine, automatic |
| G10 | "HPA cylinder" | "Portable energy storage" | Compressed gas, chemical, battery, spring |

**Rationale:** Generalization is the most powerful step — it transforms a "pneumatic net launcher" into an "aerial target entanglement system," which encompasses dramatically more solution concepts.

---

## Step 5: Solution-Neutral Problem Statement

Combine all abstraction steps into a single, unbiased problem definition.

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                       ABSTRACTED PROBLEM STATEMENT                           ║
║                    Tuyên bố Bài toán Trừu tượng hóa                         ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  TRANSFORM:                                                                  ║
║  • Input:  Hostile/unauthorized airborne vehicle (drone) at distance         ║
║  • Output: Captured, intact drone with controlled descent to ground          ║
║                                                                              ║
║  CONSTRAINTS:                                                                ║
║  C1: Single operator, man-portable system                                    ║
║  C2: Works against ALL drone types (including fully autonomous)              ║
║  C3: Preserves drone for forensic evidence                                   ║
║  C4: Affordable for widespread deployment                                    ║
║  C5: Producible locally (Vietnam, ≥60% content)                              ║
║  C6: Safe for operator, bystanders, and captured equipment                   ║
║                                                                              ║
║  ESSENTIAL FUNCTION:                                                         ║
║  "Intercept and physically capture small unmanned aerial vehicle             ║
║   at tactically useful range with single-operator portable system,           ║
║   ensuring intact recovery for forensic investigation"                       ║
║                                                                              ║
║  BOUNDARY CONDITIONS:                                                        ║
║  • Target mass: 0.5 - 25 kg (small commercial/military drones)              ║
║  • Target speed: 0 - 20 m/s (hover to fast transit)                         ║
║  • Engagement window: Seconds (high time pressure)                           ║
║  • Environment: Tropical (hot, humid, rain, dust)                            ║
║  • Operator skill: Military/security trained, non-specialist                 ║
║                                                                              ║
║  DIFFERENTIATOR vs. ALTERNATIVES:                                            ║
║  • vs. RF Jamming: Works on autonomous drones, preserves evidence            ║
║  • vs. Directed Energy: Affordable, portable, preserves evidence             ║
║  • vs. Kinetic Kill: Preserves drone (evidence + safety)                     ║
║                                                                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

# 4. DESIGN SPACE OPENED

The abstraction reveals solution categories beyond the initial "pneumatic net launcher" assumption:

| Solution Category | Examples | Feasibility | Meets C1-C6? |
|-------------------|----------|-------------|---------------|
| **Pneumatic net launcher** | SkyWall-type, custom HPA | High (TRL 8-9) | Yes |
| **Pyrotechnic net launcher** | Blank cartridge propulsion | High (TRL 9) | Partially (noise, regulation) |
| **Spring-powered launcher** | Mechanical spring/bungee | Medium (TRL 7) | Partially (limited range) |
| **Drone-interceptor** | Kamikaze drone with net | Medium (TRL 6-7) | No (not man-portable aim) |
| **Thrown/hand-deployed** | Weighted throwing net | Low (TRL 9) | No (range too short) |
| **Electromagnetic launcher** | Rail gun / coil gun | Low (TRL 3-4) | No (power, cost) |
| **Bola launcher** | Spinning weighted cords | Medium (TRL 7-8) | Partially (limited capture area) |
| **Directed energy** | HPM/laser to disable | Low (TRL 5) | No (doesn't preserve) |

**Conclusion:** Pneumatic, pyrotechnic, and bola-type launchers all warrant further exploration in the morphological matrix. The abstraction confirms the physical capture approach is correct (vs. electronic/energy) due to the evidence preservation differentiator.

---

# 5. ABSTRACTION QUALITY CHECK

| Quality Criterion | Status | Evidence |
|-------------------|--------|----------|
| All personal preferences removed? | ✅ | 8 biases eliminated (Step 1) |
| Essential vs non-essential separated? | ✅ | 7 essential, 7 non-essential (Step 2) |
| Quantitative → qualitative complete? | ✅ | 10 transformations (Step 3) |
| Domain terms generalized? | ✅ | 10 generalizations (Step 4) |
| Problem statement solution-neutral? | ✅ | No specific mechanism referenced (Step 5) |
| Design space wider than input? | ✅ | 8 solution categories identified (Section 4) |
| Essential constraints preserved? | ✅ | C1-C6 all traceable to Phase 1 MUST requirements |

---

# DOCUMENT LINKS

- [[01_requirements/requirements_list|Requirements List (Phase 1 Input)]]
- [[01_requirements/stakeholder_analysis|Stakeholder Analysis]]
- [[01_requirements/validation_report|Validation Report]]
- [[02_conceptual/function_structure|Function Structure (Step 2)]] ← NEXT
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]

---

*This abstraction follows Pahl & Beitz Step 1 of Conceptual Design (VDI 2221), systematically removing implementation bias from 89 validated requirements to define a solution-neutral design space.*
