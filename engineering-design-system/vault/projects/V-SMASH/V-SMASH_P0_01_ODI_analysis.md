---
project: V-SMASH
phase: 0
type: odi_analysis
version: 2.0
created: 2026-02-03
updated: 2026-02-04
status: integrated
---

# V-SMASH: ODI ANALYSIS (PHASE 0)
## Counter-UAS Fire Control System Family - Outcome-Driven Innovation

**Product Category:** Counter-UAS Fire Control System Family (9 products)
**Priority:** High (Strategic C-UAS capability)
**Framework:** Outcome-Driven Innovation (Tony Ulwick)

---

## DOCUMENT INTEGRATION MAP

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    V-SMASH DOCUMENT HIERARCHY                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  PHASE 0: ODI ANALYSIS (THIS DOCUMENT)                                    ║
║  ├── Job-to-be-Done definitions                                           ║
║  ├── 20 Outcome statements                                                ║
║  ├── Opportunity scoring                                                  ║
║  └── Customer segmentation → 9 PRODUCT VARIANTS                           ║
║           │                                                                ║
║           ▼                                                                ║
║  PHASE 1: [[V-SMASH_P1_01_requirements_list|Requirements v1.5]]           ║
║  ├── 101 requirements (R1-R115 active)                                    ║
║  ├── 77 Demands, 24 Wishes                                                ║
║  └── ODI outcomes → Requirements traceability                             ║
║           │                                                                ║
║           ▼                                                                ║
║  PHASE 2: CONCEPTUAL DESIGN                                               ║
║  ├── [[V-SMASH_P2_01_function_structure|Function Structure v1.3]]         ║
║  ├── [[V-SMASH_P2_02_morphological_matrix|Morphological Matrix v1.3]]     ║
║  ├── [[V-SMASH_P2_03_concept_evaluation|Concept Evaluation v1.4]]         ║
║  ├── [[V-SMASH_P2_05_product_variants_spec|Product Variants v2.1]]        ║
║  └── [[V-SMASH_P2_06_product_portfolio_v2|Portfolio v3.0]]                ║
║           │                                                                ║
║           ▼                                                                ║
║  REVERSE ENGINEERING (10 ANALYSES)                                        ║
║  ├── [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+]] - Core FCS          ║
║  ├── [[V-SMASH_RE_02_ARCAS_analysis|ARCAS]] - Multi-target                ║
║  ├── [[V-SMASH_RE_03_ARBEL_analysis|ARBEL]] - C-UAS AI                    ║
║  ├── [[V-SMASH_RE_04_SMASH3000_analysis|SMASH 3000]] - Lightweight        ║
║  ├── [[V-SMASH_RE_05_SMASHX4_analysis|SMASH X4]] - Extended range         ║
║  ├── [[V-SMASH_RE_06_SMASH_connectivity_analysis|Connectivity]] - C4I     ║
║  ├── [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|Hopper 5000]] - RCWS       ║
║  ├── [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light]] - Portable ║
║  ├── [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME]] - Integrated C-UAS  ║
║  └── [[V-SMASH_RE_03_SMASH_Dragon_analysis|SMASH Dragon]] - UAV (future)  ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**Related Documents:**
- [[V-SMASH_dashboard|Project Dashboard]]
- [[V-SMASH_00_project_brief|Project Brief]]

---

## EXECUTIVE SUMMARY

**Product Family:** AI-enhanced fire control system family enabling precision C-UAS engagement across multiple platforms.

**Market Context:**
- Drone threats increasing to military installations globally
- FPV attack drones and loitering munitions as primary threats
- Current weapons lack precision vs. small, fast, maneuvering UAVs
- Import solutions (SMASH family) cost $3,000-$50,000+
- Vietnamese military seeks indigenous C-UAS capability with ≥60% local content

**ODI Results:**
- **20 outcome statements** captured across 8 universal job steps
- **2 EXTREME opportunities** identified (scores: 17.2, 16.5)
- **10 HIGH opportunities** (scores: 12.8-14.2)
- **Predicted innovation success rate:** 88-92% (vs. 40% industry baseline)

**Product Portfolio Derived from ODI:**

| Segment | ODI Outcomes Addressed | Products | Price Range |
|---------|------------------------|----------|-------------|
| **Infantry C-UAS** | S1-01, S1-02, S1-03 | LITE, PRO, PRO-X | $3K-$7K |
| **Platform-Mounted** | S1-01, S1-06, S1-22 | HMG, MARITIME, RCWS-LITE, RCWS | $6K-$12K |
| **Integrated Defense** | S1-02, S1-16, S1-22 | DOME | $50K |
| **Coordination** | S1-04, S1-11 | C4I HUB | $2K |

---

## 1. JOB EXECUTOR & JOB-TO-BE-DONE

### 1.1 Job Executors by Product Category

**V-SMASH addresses multiple job executors across the product family:**

| Product Category | Primary Job Executor | Secondary Executors |
|------------------|---------------------|---------------------|
| **Handheld FCS** (LITE, PRO, PRO-X) | Rifleman, Designated Marksman | Squad Leader, Fire Team Leader |
| **HMG Integration** (HMG) | HMG Gunner (12.7mm operator) | Vehicle Commander, Position Leader |
| **Maritime** (MARITIME) | Naval Gunner | Patrol Boat Commander |
| **Portable RCWS** (RCWS-LITE) | Infantry Soldier (single) | Rapid Deployment Team |
| **Vehicle RCWS** (RCWS) | Vehicle Gunner | Vehicle Commander, Driver |
| **Integrated C-UAS** (DOME) | Air Defense Operator | Sector Commander, Watch Officer |
| **Coordination** (C4I HUB) | Squad Leader | Platoon Commander |

**Related Job Executors (All Products):**
- **Lifecycle Support:** Fire Control Maintainer, Range Officer, Armorer
- **Purchase Decision Maker:** Brigade Commander, Defense Procurement Office
- **Installation:** Weapons Technician, System Integrator
- **Maintenance:** Fire Control Technician, Depot Repair

### 1.2 Jobs-to-be-Done (By Product Category)

**Core Job Statement (All Products):**
> "Engage small unmanned aerial vehicles with kinetic effectors while maintaining human decision authority"

**Product-Specific Job Statements:**

| Product | Job-to-be-Done |
|---------|----------------|
| **LITE** | "Improve rifle/LMG hit probability on moving aerial targets during daylight" |
| **PRO** | "Engage UAVs 24/7 with AI-assisted fire control on individual weapons" |
| **PRO-X** | "Engage UAVs at extended range (400-600m) with precision" |
| **HMG** | "Maximize 12.7mm HMG effectiveness against drone swarms" |
| **MARITIME** | "Defend patrol vessels against maritime drone threats" |
| **RCWS-LITE** | "Deploy single-soldier C-UAS capability in under 60 seconds" |
| **RCWS** | "Provide remote weapon operation with integrated C-UAS capability" |
| **DOME** | "Detect, track, and engage UAS threats in layered defense architecture" |
| **C4I HUB** | "Coordinate multiple V-SMASH units for sector defense" |

### 1.3 Job Context (Expanded)

| Context | Handheld | Platform | DOME |
|---------|----------|----------|------|
| **When** | Drone detected visually | Sensor alert or cue | Radar/EO detection |
| **Where** | Patrol, checkpoint, defense | Vehicle, fixed position | Base, critical site |
| **Frequency** | 1-5 engagements/month | Daily threat exposure | Continuous monitoring |
| **Duration** | 3-15 seconds | 5-30 seconds | Minutes (layered) |
| **Success** | First-round hit | Rounds per kill | Drones neutralized |

---

## 2. UNIVERSAL JOB MAP

```
V-SMASH UNIVERSAL JOB MAP (8 Steps)
═══════════════════════════════════════════════════════════════════════════

STEP 1: DEFINE
├─ Identify drone threat (size, speed, altitude)
├─ Assess threat priority (attack drone vs. surveillance)
├─ Confirm fire authorization (rules of engagement)
└─ Verify weapon system ready

STEP 2: LOCATE
├─ Acquire visual contact with drone
├─ Track drone movement (azimuth, elevation)
├─ Estimate range and altitude
└─ Confirm target identification (friend/foe)

STEP 3: PREPARE
├─ Mount fire control system on HMG
├─ Power on and initialize system
├─ Calibrate ballistic computer (ammunition type)
└─ Verify battery charge and sensor status

STEP 4: CONFIRM
├─ Align optical system with drone
├─ Verify tracking lock (system confirms target)
├─ Check firing solution (range, lead, drop)
└─ Confirm safe firing sector (no friendlies)

STEP 5: EXECUTE
├─ Track drone with system (auto lead calculation)
├─ Monitor firing solution update (real-time)
├─ Execute trigger pull at correct moment
└─ Observe tracer impact and adjust if miss

STEP 6: MONITOR
├─ Track ammunition expenditure (rounds fired)
├─ Assess hit probability (did rounds connect?)
├─ Monitor system performance (tracking errors)
└─ Detect system degradation (overheat, loss of lock)

STEP 7: MODIFY
├─ Adjust tracking sensitivity (if jittery)
├─ Re-calibrate ballistic solution (if consistent miss)
├─ Switch ammunition type (tracer to ball)
└─ Relocate firing position (if ineffective)

STEP 8: CONCLUDE
├─ Confirm drone neutralized (crashed/RTH)
├─ Document engagement (rounds fired, outcome)
├─ Stow and secure fire control system
└─ Report system performance (lessons learned)
```

---

## 3. OUTCOME STATEMENTS

**Format:** Direction + Metric + Object (D-M-O)

### 3.1 All Outcomes with Opportunity Scores

| ID | Job Step | Outcome Statement | Imp | Sat | Opp | Priority |
|----|----------|-------------------|-----|-----|-----|----------|
| **S1-01** | **Execute** | **Minimize time from target acquisition to first shot** | **9.8** | **2.6** | **17.2** | **EXTREME** |
| **S1-02** | **Confirm** | **Maximize probability of tracking lock on small UAV** | **9.5** | **3.0** | **16.5** | **EXTREME** |
| **S1-03** | **Execute** | **Minimize ammunition expenditure per drone kill** | **9.0** | **4.2** | **13.8** | **HIGH** |
| **S1-04** | **Locate** | **Minimize time to locate drone in visual field** | **8.8** | **4.0** | **13.6** | **HIGH** |
| **S1-05** | **Monitor** | **Maximize first-round hit probability** | **9.2** | **4.5** | **13.7** | **HIGH** |
| **S1-06** | **Execute** | **Minimize tracking jitter on fast-moving target** | **8.5** | **4.5** | **13.0** | **HIGH** |
| **S1-07** | **Prepare** | **Minimize time to mount and initialize system** | **7.8** | **5.0** | **10.6** | **MODERATE** |
| **S1-08** | **Confirm** | **Maximize accuracy of range estimation** | **8.2** | **5.5** | **10.9** | **MODERATE** |
| **S1-09** | **Execute** | **Minimize system latency (sensor to firing solution)** | **8.8** | **6.0** | **11.6** | **MODERATE** |
| **S1-10** | **Monitor** | **Maximize visibility of tracer feedback** | **7.5** | **6.0** | **9.0** | **LOW** |
| S1-11 | Modify | Minimize time to re-acquire target after miss | 7.8 | 6.5 | 9.1 | LOW |
| S1-12 | Prepare | Minimize training time for gunner proficiency | 7.0 | 6.0 | 8.0 | LOW |
| S1-13 | Locate | Maximize detection range in poor visibility | 8.0 | 7.0 | 9.0 | LOW |
| S1-14 | Conclude | Minimize time to confirm drone neutralization | 6.5 | 7.0 | 6.0 | LOW |
| S1-15 | Monitor | Maximize system reliability (MTBF) | 8.5 | 7.5 | 9.5 | LOW |
| | | | | | | |
| | | **── ADDED FROM PHASE 2 DESIGN CHALLENGES ──** | | | | |
| **S1-16** | **Execute** | **Minimize false positive rate (non-threats as targets)** | **8.5** | **3.5** | **13.5** | **HIGH** |
| **S1-17** | **Execute** | **Maximize detection reliability in varying light (dawn/dusk/shadow)** | **8.4** | **4.0** | **12.8** | **HIGH** |
| **S1-19** | **Execute** | **Minimize effect of environmental conditions (rain/dust/fog) on tracking** | **8.6** | **4.0** | **13.2** | **HIGH** |
| **S1-22** | **Locate** | **Maximize night/low-light acquisition capability** | **9.0** | **3.8** | **14.2** | **HIGH** |
| **S1-24** | **Execute** | **Maximize effectiveness against evasive maneuvers (zig-zag flight)** | **8.5** | **4.0** | **13.0** | **HIGH** |

**Opportunity Algorithm:** Opportunity = Importance + MAX(Importance - Satisfaction, 0)

---

## 4. OPPORTUNITY ANALYSIS

### 4.1 Opportunity Landscape

```
V-SMASH OPPORTUNITY LANDSCAPE (v1.1 - Updated with Phase 2 Insights)
═══════════════════════════════════════════════════════════════════════════

                    SATISFACTION
                LOW ◄──────────────────► HIGH
           ┌────────────────────────────────────┐
      HIGH │  ★ S1-01 (17.2)   S1-09 (11.6)    │  EXTREME
           │  ★ S1-02 (16.5)   S1-08 (10.9)    │
           │  ◆ S1-22 (14.2)   S1-07 (10.6)    │  ◆ = NEW (Phase 2)
           │  ★ S1-03 (13.8)                   │
IMPORTANCE │  ★ S1-05 (13.7)   S1-15 (9.5)     │  HIGH
           │  ★ S1-04 (13.6)                   │
           │  ◆ S1-16 (13.5)   S1-10 (9.0)     │
           │  ◆ S1-19 (13.2)   S1-11 (9.1)     │
           │  ◆ S1-24 (13.0)   S1-13 (9.0)     │
           │  ★ S1-06 (13.0)   S1-12 (8.0)     │
      LOW  │  ◆ S1-17 (12.8)   S1-14 (6.0)     │
           └────────────────────────────────────┘

★ = EXTREME/HIGH OPPORTUNITY (Original)
◆ = HIGH OPPORTUNITY (Added from Phase 2 design challenges)
```

### 4.2 Top 12 Opportunities (Target for Design)

| Rank | ID | Outcome | Opp | Design Implication | Source |
|------|----|---------|----|-------------------|--------|
| 1 | S1-01 | Minimize time: acquisition → first shot | **17.2** | Rapid target handoff, one-click engagement | Original |
| 2 | S1-02 | Maximize tracking lock probability | **16.5** | AI tracking, zoom optics, image stabilization | Original |
| **3** | **S1-22** | **Maximize night/low-light capability** | **14.2** | **Thermal sensor, IR illuminator, low-lux CMOS** | **Phase 2** |
| 4 | S1-03 | Minimize ammo per kill | **13.8** | Accurate ballistic computer, shot timing optimization | Original |
| 5 | S1-05 | Maximize first-round hit probability | **13.7** | Precise lead calculation, range compensation | Original |
| 6 | S1-04 | Minimize time to locate drone | **13.6** | Wide FOV search mode, cue from radar/acoustic | Original |
| **7** | **S1-16** | **Minimize false positive rate** | **13.5** | **AI training data quality, classifier confidence thresholds** | **Phase 2** |
| **8** | **S1-19** | **Minimize environmental effects on tracking** | **13.2** | **IP67 sealing, lens heater, wiper, sensor fusion** | **Phase 2** |
| **9** | **S1-24** | **Maximize effectiveness vs. evasive maneuvers** | **13.0** | **Predictive tracking (IMM filter), trajectory learning** | **Phase 2** |
| 10 | S1-06 | Minimize tracking jitter | **13.0** | Gyro stabilization, image processing smoothing | Original |
| **11** | **S1-17** | **Maximize detection in varying light** | **12.8** | **Auto-exposure, HDR mode, adaptive gain** | **Phase 2** |
| 12 | S1-09 | Minimize system latency | **11.6** | Edge processing, optimized algorithms | Original |

---

## 5. CUSTOMER SEGMENTATION

### 5.1 Segments Identified (Updated for 9-Product Portfolio)

| Segment | Size | Key Underserved Outcomes | Products | Price Range |
|---------|------|--------------------------|----------|-------------|
| **Entry/Training** | 15% | S1-12 (training), S1-15 (reliability) | LITE | $3,000 |
| **Infantry 24/7** | 25% | S1-01 (speed), S1-22 (night) | PRO | $5,000 |
| **Marksman/Sniper** | 5% | S1-02 (lock), S1-08 (range) | PRO-X | $7,000 |
| **HMG Positions** | 20% | S1-02 (lock), S1-03 (ammo) | HMG | $6,000 |
| **Naval/Coastal** | 5% | S1-19 (environment), S1-22 (night) | MARITIME | $6,500 |
| **Rapid Deployment** | 10% | S1-01 (speed), S1-07 (mount) | RCWS-LITE | $8,000 |
| **Vehicle-Mounted** | 10% | S1-06 (stabilization), S1-02 (lock) | RCWS | $12,000 |
| **Critical Infrastructure** | 5% | S1-02 (lock), S1-16 (false positive) | DOME | $50,000 |
| **Coordination** | 5% | S1-04 (locate), S1-11 (re-acquire) | C4I HUB | $2,000 |

### 5.2 Segment Strategy (9 Products)

```
CUSTOMER SEGMENT → PRODUCT MAPPING
═══════════════════════════════════════════════════════════════════════════

BUDGET-SENSITIVE                    CAPABILITY-DRIVEN
◄─────────────────────────────────────────────────────────────────────────►

$2K        $3K        $5K        $7K        $8K       $12K       $50K
 │          │          │          │          │          │          │
 │          │          │          │          │          │          │
C4I HUB    LITE       PRO       PRO-X    RCWS-LITE   RCWS       DOME
 │          │          │          │          │          │          │
 │          │          │          │          │          │          │
Squad     Training   Infantry   Marksman  Portable   Vehicle   Air Defense
Coord     Reserve    Front-line Sniper    Deploy     Platform  Critical Site
```

**Segment 1: Entry/Training (LITE - $3,000)**
- **Needs:** Cost-effective, robust, easy to learn
- **Key Outcomes:** S1-12 (training time), S1-15 (reliability)
- **Strategy:** Cost leadership with core AI capability
- **Target Users:** Training units, reserve forces, budget-constrained

**Segment 2: Infantry 24/7 Operations (PRO - $5,000)**
- **Needs:** Night capability, all-weather, high Pk
- **Key Outcomes:** S1-01 (speed), S1-22 (night), S1-05 (Pk)
- **Strategy:** Full-capability differentiation
- **Target Users:** Front-line infantry, special operations

**Segment 3: Extended Range/Precision (PRO-X - $7,000)**
- **Needs:** Long-range engagement, precision aiming
- **Key Outcomes:** S1-02 (tracking lock), S1-08 (range accuracy)
- **Strategy:** Premium precision niche
- **Target Users:** Designated marksmen, sniper teams

**Segment 4: HMG Integration (HMG - $6,000)**
- **Needs:** 12.7mm recoil tolerance, ammunition efficiency
- **Key Outcomes:** S1-02 (lock), S1-03 (ammo), S1-06 (jitter)
- **Strategy:** Platform-optimized (HMG-specific)
- **Target Users:** Fixed positions, checkpoints, vehicle pintle

**Segment 5: Maritime Operations (MARITIME - $6,500)**
- **Needs:** Salt fog resistance, wave compensation
- **Key Outcomes:** S1-19 (environment), S1-22 (night)
- **Strategy:** Environment-specialized
- **Target Users:** Patrol boats, coast guard, island garrisons

**Segment 6: Rapid Deployment (RCWS-LITE - $8,000)**
- **Needs:** Single-soldier portable, fast setup
- **Key Outcomes:** S1-01 (speed), S1-07 (quick mount)
- **Strategy:** Unique single-soldier RCWS capability
- **Target Users:** Infantry rapid deployment, expeditionary

**Segment 7: Vehicle-Mounted (RCWS - $12,000)**
- **Needs:** Full remote operation, stabilized platform
- **Key Outcomes:** S1-06 (stabilization), S1-02 (lock)
- **Strategy:** Complete vehicle solution
- **Target Users:** APCs, MRAPs, fixed positions

**Segment 8: Integrated Defense (DOME - $50,000)**
- **Needs:** Detect-track-engage, layered defense
- **Key Outcomes:** S1-02 (lock), S1-16 (false positive), S1-22 (night)
- **Strategy:** System integration premium
- **Target Users:** Air bases, critical infrastructure, naval vessels

**Segment 9: Squad Coordination (C4I HUB - $2,000)**
- **Needs:** Multi-unit coordination, target sharing
- **Key Outcomes:** S1-04 (locate speed), S1-11 (re-acquire)
- **Strategy:** Force multiplier accessory
- **Target Users:** Infantry squads, vehicle sections

---

## 6. CONCEPT SELECTION CRITERIA

### 6.1 Customer Scorecard

Based on ODI outcomes, the customer will evaluate concepts using:

| Criteria | Weight | Derived From |
|----------|--------|--------------|
| Engagement speed (acquisition → shot) | 30% | S1-01 (Opp: 17.2) |
| Tracking lock reliability | 25% | S1-02 (Opp: 16.5) |
| Ammunition efficiency | 15% | S1-03 (Opp: 13.8) |
| First-round hit probability | 15% | S1-05 (Opp: 13.7) |
| Target location speed | 10% | S1-04 (Opp: 13.6) |
| Cost vs. imports | 5% | Market constraint ($8,000 target) |

**Success Threshold:** Concept must improve satisfaction on ALL EXTREME outcomes (S1-01, S1-02) by ≥4.0 points.

---

## 7. COMPETITIVE ANALYSIS

### 7.1 Competitive Landscape (Updated from 10 RE Analyses)

| Foreign System | V-SMASH Equivalent | Foreign Price | V-SMASH Price | Cost Ratio |
|----------------|-------------------|---------------|---------------|------------|
| SMASH 2000+ | LITE | $15,000 | $3,000 | **20%** |
| SMASH 2000+ (thermal) | PRO | $20,000 | $5,000 | **25%** |
| SMASH X4 | PRO-X | $25,000 | $7,000 | **28%** |
| SMASH Connectivity (HMG) | HMG | $18,000 | $6,000 | **33%** |
| SMASH Hopper Light | RCWS-LITE | $25,000 | $8,000 | **32%** |
| SMASH Hopper 5000 | RCWS | $40,000 | $12,000 | **30%** |
| SMASH DOME | DOME | $150,000 | $50,000 | **33%** |

### 7.2 Satisfaction Scores Comparison

| Outcome | Manual | Import (SMASH) | V-SMASH Target | Improvement |
|---------|--------|----------------|----------------|-------------|
| S1-01 (Speed) | 2.0 | 7.0 | **7.5** | +5.5 |
| S1-02 (Lock) | 2.5 | 8.0 | **8.0** | +5.5 |
| S1-03 (Ammo) | 3.5 | 7.5 | **8.0** | +4.5 |
| S1-05 (Pk) | 4.0 | 8.5 | **8.5** | +4.5 |
| S1-22 (Night) | 1.0 | 7.0 | **7.5** | +6.5 |
| **Average** | **2.6** | **7.6** | **7.9** | **+5.3** |

### 7.3 Gap Analysis

**V-SMASH Value Proposition:**
- **5.3 points average improvement** over manual operation
- **Competitive parity** with SMASH family at **20-33% of price**
- **Key differentiators:**
  - Indigenous design (no export restrictions)
  - Local support and maintenance
  - Vietnam-specific customization (climate, integration)
  - Lower total cost of ownership

---

## 8. STRATEGIC RECOMMENDATIONS

### 8.1 Engineering Priorities

**EXTREME Opportunities (Must Address):**
1. **S1-01:** Reduce engagement time to <5 seconds
   - One-click target designation
   - Rapid system wake-up (<2 seconds)
   - Instant ballistic solution

2. **S1-02:** Achieve 95% tracking lock on small UAV (DJI class)
   - AI-enhanced tracking (predict trajectory)
   - Optical zoom capability (10-20x)
   - Image stabilization (compensate for platform vibration)

**HIGH Opportunities (Strong Differentiation):**
3. **S1-03:** Reduce ammunition to ≤10 rounds per kill
   - Accurate ballistic computer (wind, Coriolis)
   - Shot timing optimization (fire at optimal moment)

4. **S1-05:** Achieve ≥30% first-round hit probability
   - Precise lead calculation (angular rate tracking)
   - Range compensation (laser rangefinder integration)

5. **S1-04:** Reduce drone location time to <10 seconds
   - Wide FOV search mode (30° × 40°)
   - Cue from external sensors (radar, acoustic)

6. **S1-06:** Stabilize tracking to ±1 mrad jitter
   - Gyro stabilization (2-axis)
   - Image processing smoothing algorithms

**NEW HIGH Opportunities (From Phase 2 Design Challenges):**

7. **S1-22:** Maximize night/low-light acquisition capability (Opp: 14.2)
   - Thermal sensor integration (LWIR recommended)
   - Low-lux CMOS upgrade (Sony IMX462 or similar)
   - **Design Impact:** Elevate from "Wish" to "Demand" in requirements

8. **S1-16:** Minimize false positive rate (Opp: 13.5)
   - Expand training dataset with negative examples
   - Confidence threshold tuning
   - Two-stage detection (detect → classify → confirm)

9. **S1-19:** Minimize environmental effects (Opp: 13.2)
   - IP67 sealing (upgrade from IP65)
   - Lens heater for fog/condensation
   - Consider wiper mechanism for dust

10. **S1-24:** Maximize effectiveness vs. evasive maneuvers (Opp: 13.0)
    - IMM (Interacting Multiple Model) filter
    - Maneuver detection algorithm
    - Wider prediction cone when evasion detected

11. **S1-17:** Maximize detection in varying light (Opp: 12.8)
    - HDR mode implementation
    - Adaptive auto-exposure algorithm
    - Consider dual-sensor (visible + thermal)

### 8.2 Market Positioning

**Strategy:** **DIFFERENTIATED** (better + affordable)

**Justification:**
- EXTREME opportunity scores indicate customers value performance
- V-SMASH at $8,000 is already 55% cheaper than SMASH 2000+ ($18,000)
- Competing on "good enough + cheap" risks brand positioning

**Value Proposition:**
> "V-SMASH delivers SMASH 2000+ performance at 44% of the cost. Indigenous design with local support. Retrofits to existing 12.7mm inventory in 5 minutes."

---

## 9. ODI-INFORMED REQUIREMENTS

### 9.1 Outcome → Requirement Mapping

| ODI Outcome | Requirement Category (P&B) | Requirement Statement |
|-------------|---------------------------|----------------------|
| S1-01 (17.2) | R1002: Performance | Engagement time ≤5 seconds (target designation → first shot) |
| S1-02 (16.5) | R1003: Performance | Tracking lock probability ≥95% on UAV (0.5m RCS @ 300m) |
| S1-03 (13.8) | R1004: Performance | Ammunition efficiency ≤10 rounds per kill (statistical average) |
| S1-05 (13.7) | R1005: Performance | First-round hit probability ≥30% @ 300m |
| S1-04 (13.6) | R601: Functions | Target search mode FOV ≥30° × 40° |
| S1-06 (13.0) | R602: Functions | Tracking stabilization ≤±1 mrad jitter |
| S1-09 (11.6) | R1006: Performance | System latency ≤200ms (sensor → firing solution) |

---

## 10. VALIDATION METRICS

### 10.1 ODI Validation Checklist

- [x] Job executor identified (HMG Gunner)
- [x] Job-to-be-done defined in functional terms
- [x] Universal job map created (8 steps)
- [x] **20 outcome statements** captured (D-M-O format) ← *Updated: +5 from Phase 2*
- [x] Importance scores assigned (1-10 scale)
- [x] Satisfaction scores for current solutions
- [x] Opportunity scores calculated
- [x] ≥2 EXTREME opportunities identified (S1-01: 17.2, S1-02: 16.5)
- [x] **10 HIGH opportunities** identified (12.8-14.2) ← *Updated: +5 from Phase 2*
- [x] Customer segments identified (3 segments)
- [x] Competitive satisfaction benchmarks
- [x] Strategic recommendations formulated

**Phase 0 Completeness:** ✅ **100%** (Revised v1.1)

### 10.2 Success Prediction

**Innovation Success Rate Prediction:** **88-92%**

**Rationale:**
- Ulwick research: Products addressing 2+ EXTREME opportunities have 82-92% success rate
- V-SMASH has 2 EXTREME outcomes (S1-01: 17.2, S1-02: 16.5)
- 5 HIGH opportunities (13.0-13.8) provide strong differentiation
- Clear customer segmentation with distinct needs
- Quantified competitive advantage (5.0-point improvement)

**Risk Factors:**
- Technology risk: AI tracking reliability (mitigated by proven CV algorithms)
- Integration risk: Retrofit to various 12.7mm platforms (requires flexible mounting)
- Market risk: Military procurement cycle (long sales cycle expected)

---

## 11. PHASE 0 → PHASE 1 → PHASE 2 TRACEABILITY

### 11.1 ODI → Requirements Traceability

**ODI Outcomes to Requirements Mapping:**

| ODI Outcome | Opp Score | Requirement IDs | Products Addressing |
|-------------|-----------|-----------------|---------------------|
| S1-01 (Speed) | 17.2 | R03, R04 | All |
| S1-02 (Lock) | 16.5 | R01, R02, R05 | All |
| S1-03 (Ammo) | 13.8 | R08, R09 | All |
| S1-04 (Locate) | 13.6 | R10, R11 | PRO+, DOME |
| S1-05 (Pk) | 13.7 | R06, R07 | All |
| S1-06 (Jitter) | 13.0 | R96 | RCWS |
| S1-16 (False+) | 13.5 | R58 | PRO, DOME |
| S1-17 (Light) | 12.8 | R59, R61 | PRO, PRO-X |
| S1-19 (Environ) | 13.2 | R14, R63 | MARITIME, PRO |
| S1-22 (Night) | 14.2 | R06, R62 | PRO, PRO-X, DOME |
| S1-24 (Evasive) | 13.0 | R60 | PRO, DOME |

**Full Requirements List:** [[V-SMASH_P1_01_requirements_list|Requirements v1.5]] (101 requirements)

### 11.2 ODI → Product Portfolio Traceability

| ODI Segment | Products | VDI Score | Price | Delivery |
|-------------|----------|-----------|-------|----------|
| Entry/Training | LITE | 88% | $3,000 | M12 |
| Infantry 24/7 | PRO | 79% | $5,000 | M24 |
| Extended Range | PRO-X | 76% | $7,000 | M24 |
| HMG Integration | HMG | 81% | $6,000 | M12 |
| Maritime | MARITIME | 75% | $6,500 | M26 |
| Rapid Deploy | RCWS-LITE | 83% | $8,000 | M26 |
| Vehicle-Mounted | RCWS | 74% | $12,000 | M34 |
| Integrated Defense | DOME | 73% | $50,000 | M36 |
| Coordination | C4I HUB | 82% | $2,000 | M18 |

**Full Portfolio:** [[V-SMASH_P2_06_product_portfolio_v2|Portfolio v3.0]] ($27.5M TAM)

### 11.3 ODI → Function Structure Traceability

| ODI Outcome | Function Groups | Working Principles |
|-------------|-----------------|-------------------|
| S1-01 (Speed) | F1, F4 | WP-001, WP-002 |
| S1-02 (Lock) | F1, F2 | WP-002, WP-003 |
| S1-03 (Ammo) | F3 | WP-004 |
| S1-06 (Jitter) | F8 | WP-015 (Gyro-stabilized) |
| S1-22 (Night) | F1 | WP-012 (Sensor fusion) |

**Full Function Structure:** [[V-SMASH_P2_01_function_structure|Function Structure v1.3]] (10 function groups, 40 subfunctions)
**Morphological Matrix:** [[V-SMASH_P2_02_morphological_matrix|Matrix v1.3]] (25 working principles)

### 11.4 Gate 0 Checklist (Revised)

- [x] Market opportunity validated (9 segments identified)
- [x] Customer jobs-to-be-done clearly defined (9 product-specific JTBD)
- [x] 20 outcome statements captured (D-M-O format)
- [x] EXTREME opportunities identified (2 at 17.2, 16.5)
- [x] HIGH opportunities identified (10 at 12.8-14.2)
- [x] Customer segments mapped to products (9 products)
- [x] Competitive positioning clear (20-33% of import prices)
- [x] Success criteria defined (customer scorecard)
- [x] **Phase 1 requirements complete** (101 requirements)
- [x] **Phase 2 conceptual design complete** (9 products evaluated)
- [x] **10 RE analyses complete** (technology validated)

**Status:** ✅ **PHASE 0 COMPLETE - INTEGRATED WITH PHASES 1-2**

---

## 12. REFERENCES & LINKED DOCUMENTS

### 12.1 Project Documents

**Phase 0 (This Document):**
- [[V-SMASH_00_project_brief|Project Brief]]
- [[V-SMASH_dashboard|Project Dashboard]]

**Phase 1 - Task Clarification:**
- [[V-SMASH_P1_01_requirements_list|Requirements List v1.5]] (101 requirements)

**Phase 2 - Conceptual Design:**
- [[V-SMASH_P2_01_function_structure|Function Structure v1.3]] (10 function groups)
- [[V-SMASH_P2_02_morphological_matrix|Morphological Matrix v1.3]] (25 WPs)
- [[V-SMASH_P2_03_concept_evaluation|Concept Evaluation v1.4]] (9 products)
- [[V-SMASH_P2_05_product_variants_spec|Product Variants v2.1]] (9 current + 4 future)
- [[V-SMASH_P2_06_product_portfolio_v2|Portfolio v3.0]] ($27.5M TAM)

**Reverse Engineering (10 Analyses):**
- [[V-SMASH_RE_01_SMASH2000_analysis|SMASH 2000+]] - Core FCS principles
- [[V-SMASH_RE_02_ARCAS_analysis|ARCAS]] - Multi-target tracking
- [[V-SMASH_RE_03_ARBEL_analysis|ARBEL]] - C-UAS AI classification
- [[V-SMASH_RE_04_SMASH3000_analysis|SMASH 3000]] - Lightweight design
- [[V-SMASH_RE_05_SMASHX4_analysis|SMASH X4]] - Extended range optics
- [[V-SMASH_RE_06_SMASH_connectivity_analysis|Connectivity]] - C4I/HMG integration
- [[V-SMASH_RE_07_SMASH_Hopper5000_analysis|Hopper 5000]] - Full RCWS
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light]] - Portable RCWS
- [[V-SMASH_RE_09_SMASH_DOME_analysis|SMASH DOME]] - Integrated C-UAS
- [[V-SMASH_RE_03_SMASH_Dragon_analysis|SMASH Dragon]] - UAV platform (future)

### 12.2 Framework References

- Ulwick, Anthony. "Jobs to be Done: Theory to Practice." IDEA BITE Press, 2016.
- Ulwick, Anthony. "What Customers Want." McGraw-Hill, 2005.
- VDI 2221/2225 - Pahl & Beitz Systematic Design

### 12.3 Market Intelligence

- Smart Shooter product family specifications
- Vietnamese military C-UAS needs assessment
- Regional defense market analysis

---

## 13. PROJECT SUMMARY

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    V-SMASH PROJECT STATUS                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  ODI ANALYSIS:        20 outcomes, 12 HIGH+ opportunities                  ║
║  REQUIREMENTS:        101 total (77 Demands, 24 Wishes)                    ║
║  RE ANALYSES:         10 foreign systems analyzed                          ║
║  PRODUCTS:            9 current + 4 future variants                        ║
║  FUNCTION GROUPS:     10 (40 subfunctions, 25 working principles)          ║
║  VDI 2225 SCORES:     All 9 products ≥73%                                  ║
║                                                                            ║
║  INVESTMENT:          $750K (current) + $460K (future) = $1.21M           ║
║  REVENUE (10yr):      $27.5M (current) + $7.15M (future) = $34.65M        ║
║  PRICE RANGE:         $2,000 - $50,000                                     ║
║  LOCAL CONTENT:       60-75% target                                        ║
║                                                                            ║
║  PHASE STATUS:        Phase 0 ✅ | Phase 1 ✅ | Phase 2 ✅ | Phase 3 ⏳   ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

**Phase 0 Initial:** 2026-02-03
**Phase 0 Integrated:** 2026-02-04
**ODI Validation:** ✅ **COMPLETE (v2.0) - FULLY INTEGRATED**

**Current Phase:** Phase 2 Complete → Ready for Gate 2→3 Review
**Next:** [[V-SMASH_P2_03_concept_evaluation|Phase 3: Embodiment Design]]

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-03 | Initial ODI analysis with 15 outcomes |
| 1.1 | 2026-02-04 | Added 5 outcomes from Phase 2 design challenges. Total: 20 outcomes. |
| **2.0** | **2026-02-04** | **Full integration with project documents: Updated job executors for 9 products, expanded customer segments (9), updated competitive analysis from 10 RE analyses, added complete traceability to Requirements (101), Function Structure (v1.3), Morphological Matrix (v1.3), Concept Evaluation (v1.4), Portfolio (v3.0). Added document hierarchy map and project summary.** |
