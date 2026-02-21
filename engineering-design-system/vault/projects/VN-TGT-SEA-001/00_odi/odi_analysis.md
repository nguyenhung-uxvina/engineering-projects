---
project: VN-TGT-SEA-001
phase: 0
type: odi_analysis
version: 2.1
created: 2026-02-09
updated: 2026-02-10
revision: B.1
status: draft
---

# ODI Analysis: VN-TGT-SEA-001 — Fixed Sea Target with Hyperganic Enhancement

> **Rev B.1** — O-57 reinterpreted (environmental survivability), O-37 upgraded (EXTREME). RCS outcomes well-satisfied at >1,000 m². IR outcomes removed (radar-only). Platform 8.0m, reflectors at 3-4m on masts.

**Framework:** Outcome-Driven Innovation (ODI) — 10-Step Process
**Cross-reference:** [[../00_project_brief.md]], Reference documents (see Section 11)

---

## Step 1: Define the Job Executor

### Primary Executor

| Field | Value |
|-------|-------|
| **Role** | Naval Test & Evaluation Director (Giam doc Thu nghiem) |
| **Organization** | Vietnamese People's Navy — Weapons Test & Acceptance Directorate |
| **Context** | Conducts anti-ship missile acceptance tests at designated sea ranges |
| **NOT the executor** | Fleet Commander (sets policy), Procurement Officer (buys), Missile Manufacturer (supplies) |

### Why This Executor

The Test Director physically plans and executes the entire acceptance test sequence:
- Selects target type and position
- Coordinates deployment vessel, safety zone, firing ship
- Commands deployment, anchor, withdrawal sequence
- Authorizes missile launch
- Evaluates hit/miss/scoring results
- Signs acceptance certificate

### Secondary Executors

| Role | Interaction with Target | Key Outcomes |
|------|------------------------|--------------|
| **Deployment Crew** (3-4 sailors) | Tow, anchor, activate target | Deploy speed, safety, simplicity |
| **Missile System Operator** | Fires missile at target | Seeker acquisition, lock-on confidence |
| **Scoring Officer** | Evaluates test results | Hit determination, miss distance measurement |
| **Safety Officer** | Manages exclusion zones | Vessel clearance, debris, environmental |

---

## Step 2: Define Jobs-to-be-Done

### Core Functional Job

> **"Validate anti-ship missile system performance by engaging a representative sea target at designated coordinates, confirming seeker acquisition, guidance, and terminal accuracy — while ensuring zero risk to support personnel."**

### Related Jobs

| Job Type | Statement |
|----------|-----------|
| **Core functional** | Validate missile system through live-fire against sea target |
| **Related functional** | Document test results for acceptance certification |
| **Related functional** | Train firing crews on engagement procedures |
| **Emotional** | Feel confident the test will succeed (no wasted missile = $500K) |
| **Emotional** | Feel safe that no support vessel is at risk |
| **Social** | Demonstrate national capability in missile acceptance testing |
| **Consumption chain** | Procure, store, transport, deploy, recover/dispose target |

### Universal Job Map

```
JOB: Validate anti-ship missile by engaging representative sea target

1. DEFINE ──► Define test parameters
   │           • Select missile type (C-802, Kh-35, Exocet)
   │           • Define target signature requirements (RCS, IR)
   │           • Specify engagement geometry (range, bearing, sea state)
   │           • Set success criteria (hit zone, seeker lock time)
   │
2. LOCATE ──► Locate and designate target area
   │           • Select sea range coordinates
   │           • Survey sea bottom for anchoring suitability
   │           • Verify range clearance (shipping, fishing, weather)
   │           • Confirm GPS positioning capability
   │
3. PREPARE ─► Prepare target and support systems
   │           • Assemble/configure target for specific missile type
   │           • Load target onto deployment vessel
   │           • Verify radar and IR signature systems
   │           • Pre-set timers (IR ignition, GPS beacon activation)
   │           • Brief deployment crew and safety procedures
   │
4. CONFIRM ─► Confirm readiness before firing
   │           • Verify target anchored at correct position (±50m)
   │           • Confirm radar signature active (RCS measurement)
   │           • Confirm IR signature active (thermal camera verify)
   │           • Verify deployment vessel has withdrawn (5+ km)
   │           • Confirm safety zone clear (radar, AIS, visual)
   │           • Receive "safe to fire" from Safety Officer
   │
5. EXECUTE ─► Execute missile engagement
   │           • Authorize missile launch from firing ship
   │           • Missile seeker acquires target (radar/IR lock)
   │           • Missile guides to target
   │           • Terminal engagement (hit or miss)
   │
6. MONITOR ─► Monitor engagement and results
   │           • Track missile trajectory (radar, telemetry)
   │           • Observe impact (radar, visual, camera)
   │           • Monitor GPS beacon status (stops = hit, continues = miss)
   │           • Record all sensor data for analysis
   │
7. MODIFY ──► Modify for follow-up tests (if applicable)
   │           • Assess target condition (still floating? still anchored?)
   │           • Deploy replacement target if destroyed
   │           • Adjust test parameters for next missile
   │           • Reconfigure signature for different seeker type
   │
8. CONCLUDE ► Conclude test and certify results
              • Recover debris / environmental cleanup
              • Analyze hit/miss data, miss distance
              • Generate acceptance test report
              • Sign missile batch acceptance certificate
              • Archive all sensor data and video
```

---

## Step 3: Capture Customer Outcomes (D-I-M Format)

### Outcome Database — 73 Outcomes across 8 Job Steps

#### STEP 1: DEFINE (9 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-01 | Minimize | the time it takes to | configure target for specific missile seeker type | Define |
| O-02 | Minimize | the number of | target variants needed to cover all missile types in inventory | Define |
| O-03 | Minimize | the likelihood that | target signature specification is incorrect for the missile type | Define |
| O-04 | Minimize | the uncertainty in | required RCS level for reliable seeker acquisition | Define |
| O-05 | Minimize | the uncertainty in | required IR signature level for IR-guided seekers | Define |
| O-06 | Maximize | the number of | missile types that can be tested with one target configuration | Define |
| O-07 | Minimize | the number of | external experts needed to define test parameters | Define |
| O-08 | Minimize | the time it takes to | determine if weather/sea conditions are suitable for test | Define |
| O-09 | Maximize | the confidence that | test results will be accepted by missile manufacturer | Define |

#### STEP 2: LOCATE (7 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-10 | Minimize | the constraints on | sea bottom type for target anchoring | Locate |
| O-11 | Minimize | the time it takes to | survey and approve a new test location | Locate |
| O-12 | Minimize | the minimum water depth | required for safe target deployment | Locate |
| O-13 | Maximize | the number of | suitable deployment locations along coastline | Locate |
| O-14 | Minimize | the interference from | commercial shipping on test schedule | Locate |
| O-15 | Minimize | the distance | deployment vessel must travel from shore to test site | Locate |
| O-16 | Maximize | the accuracy of | GPS position designation for the target | Locate |

#### STEP 3: PREPARE (12 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-17 | Minimize | the time it takes to | assemble target from stored components | Prepare |
| O-18 | Minimize | the number of | personnel required for target preparation | Prepare |
| O-19 | Minimize | the number of | specialized tools required for assembly | Prepare |
| O-20 | Minimize | the likelihood that | signature system fails to activate on schedule | Prepare |
| O-21 | Minimize | the skill level | required for deployment crew | Prepare |
| O-22 | Minimize | the storage space | required for target components at depot | Prepare |
| O-23 | Maximize | the shelf life of | stored target components before deployment | Prepare |
| O-24 | Minimize | the time it takes to | load target onto deployment vessel | Prepare |
| O-25 | Minimize | the likelihood that | deployment equipment fails during transport | Prepare |
| O-26 | Minimize | the weight of | largest single component requiring crane/hoist | Prepare |
| O-27 | Minimize | the time it takes to | verify all systems functional before departure | Prepare |
| O-28 | Minimize | the cost of | consumables required per deployment (batteries, tow equipment) | Prepare |

#### STEP 4: CONFIRM (11 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-29 | Minimize | the likelihood that | missile seeker fails to acquire the STATIONARY target | Confirm |
| O-30 | Maximize | the reliability of | target radar signature at fixed anchored position | Confirm |
| O-31 | Maximize | the consistency of | RCS from all approach angles (360 deg) | Confirm |
| O-32 | Maximize | the visibility of | signature from all approach angles (360 deg) | Confirm |
| O-33 | Minimize | the position drift | after anchoring in sea state 3 conditions | Confirm |
| O-34 | Minimize | the time from | anchor drop to target confirmed ready | Confirm |
| O-35 | Maximize | the safe distance | between deployment vessel and target at firing time | Confirm |
| O-36 | Minimize | the likelihood that | target capsizes or becomes unstable before firing | Confirm |
| O-37 | Maximize | the confidence that | anchor will hold during engagement | Confirm |
| O-38 | Minimize | the time it takes to | confirm target is emitting correct radar signature | Confirm |
| O-39 | Minimize | the time it takes to | confirm target is emitting correct radar signature from all angles | Confirm |

#### STEP 5: EXECUTE (8 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-40 | Maximize | the probability that | missile seeker acquires target at maximum range | Execute |
| O-41 | Maximize | the probability of | missile achieving terminal guidance lock | Execute |
| O-42 | Minimize | the likelihood that | target RCS fades cause seeker to break lock | Execute |
| O-43 | Minimize | the angular variation | in RCS as missile approaches (aspect changes) | Execute |
| O-44 | Maximize | the realism of | target signature compared to actual warship | Execute |
| O-45 | Maximize | the probability of | successful missile impact on target | Execute |
| O-46 | Minimize | the number of | test failures caused by inadequate target signature | Execute |
| O-47 | Maximize | the number of | missile types/seekers compatible with target | Execute |

#### STEP 6: MONITOR (9 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-48 | Maximize | the certainty of | hit/miss determination after engagement | Monitor |
| O-49 | Minimize | the time it takes to | determine if missile hit the target | Monitor |
| O-50 | Maximize | the accuracy of | miss distance measurement (if miss) | Monitor |
| O-51 | Maximize | the amount of | scoring/telemetry data captured during engagement | Monitor |
| O-52 | Minimize | the likelihood that | scoring sensor data is lost due to target destruction | Monitor |
| O-53 | Maximize | the quality of | video/photo documentation of impact | Monitor |
| O-54 | Minimize | the time it takes to | retrieve telemetry data after test | Monitor |
| O-55 | Maximize | the reliability of | GPS beacon signal during and after engagement | Monitor |
| O-56 | Minimize | the ambiguity in | interpreting test results (pass/fail determination) | Monitor |

#### STEP 7: MODIFY (8 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-57 | Maximize | the number of | engagements a single target can survive | Modify |
| O-58 | Minimize | the cost to | repair/replace target after partial damage | Modify |
| O-59 | Minimize | the time it takes to | reconfigure target for different missile type | Modify |
| O-60 | Minimize | the time it takes to | deploy a replacement target if first is destroyed | Modify |
| O-61 | Maximize | the ability to | change RCS profile without building new target | Modify |
| O-62 | Minimize | the cost per | individual acceptance test engagement | Modify |
| O-63 | Maximize | the ability to | upgrade target capabilities over time | Modify |
| O-64 | Minimize | the number of | spare targets needed in inventory for test campaign | Modify |

#### STEP 8: CONCLUDE (9 outcomes)

| ID | Direction | Indicator | Matter | Job Step |
|----|-----------|-----------|--------|----------|
| O-65 | Minimize | the time it takes to | generate acceptance test report | Conclude |
| O-66 | Minimize | the environmental impact | of target debris in the sea | Conclude |
| O-67 | Minimize | the cost of | debris recovery and environmental cleanup | Conclude |
| O-68 | Maximize | the completeness of | test documentation for audit trail | Conclude |
| O-69 | Minimize | the time from | test completion to acceptance certificate issued | Conclude |
| O-70 | Maximize | the credibility of | test results with missile manufacturer | Conclude |
| O-71 | Minimize | the total cost of ownership | for a complete test campaign (10+ tests) | Conclude |
| O-72 | Maximize | the exportability of | test services to allied ASEAN navies | Conclude |
| O-73 | Minimize | the dependency on | imported components or foreign expertise | Conclude |

### Outcome Validation Summary

| Check | Count | % |
|-------|-------|---|
| Total outcomes captured | 73 | 100% |
| D-I-M format compliant | 73 | 100% |
| Measurable | 73 | 100% |
| Technology-independent | 73 | 100% |
| Single idea per outcome | 73 | 100% |
| All 8 job steps covered | 8/8 | 100% |

---

## Step 4: Organize Outcomes into Universal Job Map

```
JOB MAP: Validate anti-ship missile via sea target engagement
════════════════════════════════════════════════════════════════

1. DEFINE (9 outcomes)
│  EXTREME: O-04 (RCS uncertainty), O-05 (IR uncertainty)
│  HIGH:    O-06 (multi-missile), O-09 (result acceptance)
│  MOD:     O-01 (config time), O-02 (variant count)
│  LOW:     O-03, O-07, O-08
│
2. LOCATE (7 outcomes)
│  HIGH:    O-10 (bottom type constraints)
│  MOD:     O-13 (location options), O-16 (GPS accuracy)
│  LOW:     O-11, O-12, O-14, O-15
│
3. PREPARE (12 outcomes)
│  HIGH:    O-20 (activation reliability), O-26 (component weight)
│  MOD:     O-17 (assembly time), O-18 (personnel)
│  LOW:     O-19, O-21-O-25, O-27, O-28
│
4. CONFIRM (11 outcomes)  ★★★ HIGHEST CONCENTRATION ★★★
│  EXTREME: O-29 (seeker acquisition), O-30 (RCS reliability),
│           O-31 (360 deg RCS), O-32 (360 deg IR)
│  HIGH:    O-33 (position drift), O-34 (deploy time),
│           O-35 (safe distance)
│  MOD:     O-36 (stability), O-37 (anchor hold)
│  LOW:     O-38, O-39
│
5. EXECUTE (8 outcomes)
│  EXTREME: O-40 (seeker acquisition at range), O-42 (RCS fades)
│  HIGH:    O-41 (terminal lock), O-44 (realism),
│           O-46 (test failure rate)
│  MOD:     O-43 (angular variation), O-45, O-47
│
6. MONITOR (9 outcomes)
│  HIGH:    O-48 (hit certainty), O-50 (miss distance)
│  MOD:     O-49, O-51-O-56
│
7. MODIFY (8 outcomes)  ★★★ HYPERGANIC SWEET SPOT ★★★
│  EXTREME: O-57 (target survivability!), O-62 (cost per test)
│  HIGH:    O-58 (repair cost), O-61 (RCS reconfigurability)
│  MOD:     O-59, O-60, O-63, O-64
│
8. CONCLUDE (9 outcomes)
│  HIGH:    O-71 (total cost of ownership), O-73 (indigenous)
│  MOD:     O-66 (environmental), O-72 (export)
│  LOW:     O-65, O-67-O-70
```

> **Rev B.1 Note:** O-37 (anchor hold) upgraded from MODERATE to EXTREME (Opp 15.0) due to SS 5-6 environmental survivability requirement. O-32 (360° IR) removed (radar-only). RCS outcomes (O-29, O-31, O-40) now well-satisfied at >1,000 m² — scores reduced per [[phase0_final_revision.md]].

**Key Insight:** The CONFIRM and MODIFY job steps contain the highest concentration of EXTREME/HIGH opportunities. This is where Hyperganic enhancement delivers maximum impact — RCS precision (CONFIRM) and target survivability/reusability (MODIFY).

---

## Step 5: Quantitative Assessment

### Methodology

Importance and satisfaction estimates derived from:
- Structured interviews with 3 Vietnamese Navy test range officers (real data, limited sample)
- Expert assessment based on reverse engineering of 5 competitor systems (Saab, QinetiQ, Metal Shark, InVeris, custom target barges)
- Analysis of 4 reference documents with operational data
- Cross-referencing with published US Navy SINKEX/target procedures (DA PAM 385-63)

**Note:** Full survey (TBD-001: 30-50 respondents from VPN weapons test community) planned for Q2 2026 to validate these estimates.

### Importance and Satisfaction Scores (10-point scale)

| ID | Outcome (abbreviated) | Job Step | Imp | Sat | Notes on Satisfaction |
|----|----------------------|----------|-----|-----|----------------------|
| O-29 | Seeker acquisition of STATIONARY target | Confirm | 9.8 | 4.0 | Current ad-hoc barges have inconsistent RCS |
| O-57 | Target survives multiple engagements | Modify | 10.0 | 2.0 | Current targets sink after 1-3 hits |
| O-30 | RCS reliability at fixed position | Confirm | 9.5 | 4.5 | Hand-made reflectors vary ±5 dBsm |
| O-31 | 360 deg RCS consistency | Confirm | 9.5 | 3.5 | Current targets only ~180 deg coverage |
| O-32 | 360 deg IR visibility | Confirm | 9.0 | 4.0 | Current IR = point source, not distributed |
| O-62 | Cost per test engagement | Modify | 9.2 | 3.5 | $50-100K per test (target + missile + ops) |
| O-40 | Seeker acquisition at maximum range | Execute | 9.5 | 4.0 | RCS insufficient for some seekers |
| O-42 | Minimize RCS fades during approach | Execute | 9.0 | 4.0 | Aspect-dependent RCS causes lock breaks |
| O-33 | Position drift after anchoring | Confirm | 9.0 | 5.0 | Swing circle 100m acceptable but improvable |
| O-34 | Time from anchor to ready | Confirm | 8.5 | 4.5 | Current: 60-90 min; want: 30 min |
| O-35 | Safe distance for deployment vessel | Confirm | 9.5 | 7.0 | Already good (5+ km), critical to maintain |
| O-71 | Total cost of ownership (10+ tests) | Conclude | 9.0 | 3.0 | $1M+ for 10 expendable targets |
| O-44 | Signature realism vs actual warship | Execute | 9.0 | 4.0 | RCS pattern doesn't match ship profile |
| O-48 | Hit/miss determination certainty | Monitor | 8.5 | 5.5 | GPS beacon helps but scoring limited |
| O-50 | Miss distance measurement accuracy | Monitor | 8.5 | 3.5 | No MDI system on current targets |
| O-58 | Cost to repair after partial damage | Modify | 8.0 | 3.0 | Total replacement needed (no repair) |
| O-61 | Change RCS without new target | Modify | 8.0 | 2.5 | Fixed reflectors, no reconfiguration |
| O-46 | Test failures from inadequate signature | Execute | 9.0 | 4.5 | 10-15% estimated test failure rate |
| O-73 | Indigenous content / self-reliance | Conclude | 8.5 | 3.0 | Current targets use imported reflectors |
| O-06 | Multi-missile compatibility | Define | 8.5 | 4.0 | Different seekers need different RCS/IR |
| O-20 | Signature activation reliability | Prepare | 8.0 | 5.0 | Timer ignition generally reliable |
| O-47 | Number of missile types compatible | Execute | 8.0 | 4.0 | Only tested with 1-2 types currently |
| O-66 | Environmental impact of debris | Conclude | 7.5 | 4.0 | Steel/foam debris in sea problematic |
| O-72 | Export test services to ASEAN | Conclude | 7.0 | 2.0 | No current export capability |
| O-10 | Sea bottom constraints | Locate | 7.0 | 5.0 | Concrete anchor works on most bottoms |

> **Rev B.1 Note:** Satisfaction scores for O-29, O-31, O-40, O-42 improved (Sat +1.5-2.0) due to >1,000 m² RCS exceeding threshold by 7×. O-37 satisfaction decreased (5.0→3.0) due to SS 6 anchor holding requirement. O-32 (IR) and O-05 (IR uncertainty) removed for radar-only variant. See [[phase0_final_revision.md]] for revised opportunity scores.

---

## Step 6: Calculate Opportunity Scores

### Formula: Opportunity = Importance + max(Importance - Satisfaction, 0)

### Top 25 Opportunities (Ranked)

| Rank | ID | Outcome | Imp | Sat | **Opp Score** | Category |
|------|-----|---------|-----|-----|--------------|----------|
| **1** | **O-57** | **Target survives multiple engagements** | **10.0** | **2.0** | **18.0** | **EXTREME** |
| **2** | **O-29** | **Seeker acquisition of stationary target** | **9.8** | **4.0** | **15.6** | **EXTREME** |
| **3** | **O-31** | **360 deg RCS consistency** | **9.5** | **3.5** | **15.5** | **EXTREME** |
| **4** | **O-62** | **Cost per test engagement** | **9.2** | **3.5** | **14.9** | **HIGH** |
| **5** | **O-30** | **RCS reliability at fixed position** | **9.5** | **4.5** | **14.5** | **HIGH** |
| **6** | **O-40** | **Seeker acquisition at max range** | **9.5** | **4.0** | **15.0** | **EXTREME** |
| **7** | **O-32** | **360 deg IR visibility** | **9.0** | **4.0** | **14.0** | **HIGH** |
| **8** | **O-42** | **Minimize RCS fades during approach** | **9.0** | **4.0** | **14.0** | **HIGH** |
| **9** | **O-71** | **Total cost of ownership** | **9.0** | **3.0** | **15.0** | **EXTREME** |
| **10** | **O-44** | **Signature realism vs warship** | **9.0** | **4.0** | **14.0** | **HIGH** |
| 11 | O-33 | Position drift after anchoring | 9.0 | 5.0 | 13.0 | HIGH |
| 12 | O-46 | Test failures from inadequate sig | 9.0 | 4.5 | 13.5 | HIGH |
| 13 | O-58 | Cost to repair partial damage | 8.0 | 3.0 | 13.0 | HIGH |
| 14 | O-61 | Change RCS without new target | 8.0 | 2.5 | 13.5 | HIGH |
| 15 | O-50 | Miss distance measurement | 8.5 | 3.5 | 13.5 | HIGH |
| 16 | O-73 | Indigenous content | 8.5 | 3.0 | 14.0 | HIGH |
| 17 | O-48 | Hit/miss determination | 8.5 | 5.5 | 11.5 | MOD |
| 18 | O-34 | Anchor to ready time | 8.5 | 4.5 | 12.5 | HIGH |
| 19 | O-06 | Multi-missile compatibility | 8.5 | 4.0 | 13.0 | HIGH |
| 20 | O-47 | Number of missile types | 8.0 | 4.0 | 12.0 | MOD |
| 21 | O-72 | Export capability | 7.0 | 2.0 | 12.0 | MOD |
| 22 | O-35 | Safe distance for deploy vessel | 9.5 | 7.0 | 12.0 | MOD |
| 23 | O-20 | Signature activation reliability | 8.0 | 5.0 | 11.0 | MOD |
| 24 | O-66 | Environmental impact | 7.5 | 4.0 | 11.0 | MOD |
| 25 | O-26 | Component weight | 7.5 | 4.5 | 10.5 | MOD |

> **Rev B.1 Revised EXTREME Outcomes:** O-57 (18.0, environmental), O-71 (15.0, TCO), O-37 (15.0, anchor holding). RCS outcomes O-29, O-31, O-40 downgraded to HIGH (well-satisfied). See [[phase0_final_revision.md]] for full revised scoring.

### Opportunity Distribution

| Category | Score Range | Count | % | Action |
|----------|-----------|-------|---|--------|
| **EXTREME** | >15 | **5** | 7% | Immediate priority — accelerate |
| **HIGH** | 12-15 | **14** | 19% | Strong priority — fund & resource |
| **MODERATE** | 10-12 | **8** | 11% | Monitor — second tier |
| **LOW** | <10 | **46** | 63% | Maintain — current solution adequate |
| **TOTAL** | | **73** | 100% | |

### Opportunity Landscape Visualization

```
OPPORTUNITY LANDSCAPE: VN-TGT-SEA-001
══════════════════════════════════════════════════════════════

   Imp
   10 │                                        ● O-57 (18.0!)
      │                               ● O-29  ●O-40
   9  │                     ● O-32  ●O-42  ● O-31  ● O-71
      │                   ●O-62  ●O-44 ●O-46   ●O-30
   8  │           ● O-20  ●O-06 ●O-48 ●O-61  ●O-58 ●O-73
      │                   ●O-47
   7  │    ● O-10       ●O-72  ●O-66
      │                ●O-26
   6  │
      └──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──
         1  2  3  4  5  6  7  8  9  10  Sat

                        ↑ UNDERSERVED ZONE (Imp > Sat)

   ● Above diagonal = OPPORTUNITY
   ● Below diagonal = OVERSERVED
   ● Far upper-left = EXTREME OPPORTUNITY
```

### EXTREME Opportunities — Deep Analysis

#### O-57: Target Survivability (Opp 18.0) — HIGHEST IN PORTFOLIO

This is a "hidden opportunity" — customers don't even ask for it because they assume it's impossible. Current satisfaction = 2.0 (targets sink after 1-3 hits).

**Hyperganic solution:** TPMS multi-compartment flotation core
- ~36,000 sealed air cells
- 1 hit = 5 cells destroyed = 0.014% buoyancy loss
- After 50 hits = 0.69% loss → >99% survivability
- **Paradigm shift:** Expendable (1 use) → Reusable (5-10 uses)

**Value creation:**
- Each survived test saves $32-45K (avoided target replacement)
- 10-test campaign: $320K expendable → $90K reusable = **$230K savings**
- ROI of TPMS investment: payback in 2 reuse cycles

#### O-29 & O-40: Seeker Acquisition (Opp 15.6, 15.0)

Missile seeker must reliably acquire the STATIONARY target. Key difference from moving target: Doppler shift = 0, so seeker relies entirely on RCS magnitude.

**Hyperganic solution:** AM precision corner reflectors (±0.1 deg vs ±0.5 deg traditional)
- RCS accuracy ±0.5 dBsm (vs ±5 dBsm handmade)
- Predictable, repeatable signature → fewer failed tests
- Modular swap → change RCS profile for different seekers

#### O-31: 360 deg RCS Consistency (Opp 15.5)

Anchored target rotates on anchor chain — missile may approach from ANY angle. Current targets have 2-4 reflectors with >10 dB gaps between coverage sectors.

**Hyperganic solution:** 8 AM reflectors at 45 deg spacing → ≤±2 dB variation through 360 deg

#### O-71: Total Cost of Ownership (Opp 15.0)

10-test campaign costs:
- Current (expendable): 10 targets x $50-100K = $500K-$1M
- VN-TGT-SEA-001 base: 10 targets x $32K = $320K
- VN-TGT-SEA-001-H (reusable): 2-3 targets x $45K + repairs = **$90-135K**

---

## Step 7: Identify Outcome-Based Segments

### Segmentation Analysis

Three distinct segments identified based on outcome priority patterns:

### Segment A: "Test Efficiency Maximizers" (45% of stakeholders)

| Characteristic | Description |
|---------------|-------------|
| **Who** | Test Directors, Procurement Officers, Budget Controllers |
| **Top outcomes** | O-62 (cost/test), O-71 (TCO), O-57 (survivability), O-17 (assembly time) |
| **Core need** | Minimize total test campaign cost and time |
| **Current pain** | $50-100K per test is unsustainable; only 2-4 tests/year budget allows |
| **What they'd pay for** | Reusable target that cuts cost/test by 50-80% |
| **Satisfaction gap** | Very large — current solutions are 5-10x too expensive |

**Strategy implication:** Lead with cost/reusability value proposition. TPMS survivability is the killer feature for this segment.

### Segment B: "Signature Accuracy Seekers" (35% of stakeholders)

| Characteristic | Description |
|---------------|-------------|
| **Who** | Missile System Engineers, Seeker Calibration Officers, Scoring Officers |
| **Top outcomes** | O-29 (seeker acquisition), O-31 (360 deg RCS), O-30 (RCS reliability), O-50 (miss distance) |
| **Core need** | Ensure missile seeker test results are valid and repeatable |
| **Current pain** | 10-15% test failure rate due to inadequate/inconsistent target signature |
| **What they'd pay for** | Precision RCS/IR with documented, repeatable specifications |
| **Satisfaction gap** | Large — current hand-made reflectors are imprecise |

**Strategy implication:** Lead with AM precision reflectors and documented RCS specifications. Digital twin capability for pre-test signature prediction.

### Segment C: "Operational Safety Advocates" (20% of stakeholders)

| Characteristic | Description |
|---------------|-------------|
| **Who** | Safety Officers, Fleet Commanders, Training Command |
| **Top outcomes** | O-35 (safe distance), O-66 (environmental), O-36 (stability), O-25 (fuel safety) |
| **Core need** | Zero risk to personnel and minimum environmental impact |
| **Current pain** | Towed targets require vessel at 500m during missile firing |
| **What they'd pay for** | Anchored target with full crew withdrawal before firing |
| **Satisfaction gap** | Moderate — anchored concept already addresses main safety concern |

**Strategy implication:** Anchored design inherently satisfies this segment. Environmental benefit of reusable target (less debris) is bonus.

### Segment Strategy Map

```
                    COST SENSITIVITY
            HIGH ◄─────────────────────► LOW

     HIGH  ┌─────────────────┬─────────────────┐
           │                 │                 │
  TECH     │  Segment A      │  Segment B      │
  NEEDS    │  "Efficiency"   │  "Accuracy"     │
           │  45%            │  35%            │
           │                 │                 │
           │  DOMINANT       │  DIFFERENTIATED │
           │  strategy       │  strategy       │
           │                 │                 │
     LOW   ├─────────────────┼─────────────────┤
           │                 │                 │
           │  Segment C      │  (empty)        │
           │  "Safety"       │                 │
           │  20%            │                 │
           │                 │                 │
           │  ALREADY SERVED │                 │
           │  by anchored    │                 │
           │  concept        │                 │
           └─────────────────┴─────────────────┘
```

---

## Step 8: Focused Brainstorming on Top Outcomes

### Focus: Top 5 EXTREME Outcomes

#### Outcome O-57: Target Survives Multiple Engagements (Opp 18.0)

| # | Solution Idea | Feasibility | Cost Impact | Outcome Impact | Priority |
|---|--------------|-------------|-------------|----------------|----------|
| 1 | TPMS Voronoi multi-compartment flotation core | HIGH (proven AM) | +$8-15K/unit | 10x improvement (1→50+ hits) | **P1** |
| 2 | Foam-filled hollow pontoons | HIGH | +$2K | 2x improvement (1→3 hits) | P3 |
| 3 | Self-sealing polymer coating | MEDIUM | +$5K | 3x improvement | P2 |
| 4 | Kevlar ballistic liner | LOW (expensive) | +$20K | 5x improvement | P4 |
| 5 | Modular replaceable sections (survive by replacing) | HIGH | +$3K | Effectively unlimited | **P1** |

**Decision:** Combine #1 (TPMS core) + #5 (modular sections). TPMS provides survivability at flotation level; modularity enables damaged superstructure/signature replacement.

> **Rev B.1:** O-57 reinterpreted as environmental survivability (SS 5-6, 72h anchored). TPMS removed. Survivability now achieved through storm-rated mooring + robust marine construction, not ballistic damage tolerance.

#### Outcome O-29/O-40: Seeker Acquisition (Opp 15.6/15.0)

| # | Solution Idea | Feasibility | Cost Impact | Outcome Impact | Priority |
|---|--------------|-------------|-------------|----------------|----------|
| 1 | AM corner reflectors ±0.1 deg tolerance | HIGH | +$8K (8 units) | RCS ±0.5 dBsm (10x better) | **P1** |
| 2 | Luneburg lens (omnidirectional) | HIGH | +$15K (2 units) | Perfect omni-RCS | P2 (cost) |
| 3 | Active radar transponder (amplifier) | MEDIUM | +$20K | Unlimited RCS boost | P3 (complexity) |
| 4 | Larger traditional reflectors (a=0.8m) | HIGH | +$4K | 4x RCS increase | P2 |
| 5 | Metamaterial surface tuning | LOW (R&D) | +$30K | Programmable RCS | P4 (future) |

**Decision:** #1 (AM reflectors) as primary. 8 units at 45 deg spacing provides guaranteed 360 deg coverage with documented ±0.5 dBsm accuracy. Option #4 as fallback if AM cost exceeds budget.

> **Rev B.1:** Reflector edge increased to 0.8m (from 0.5m) for >1,000 m² RCS. Hybrid CNC faces + AM frames approach selected. Reflectors elevated to 3-4m on steel masts.

#### Outcome O-31: 360 deg RCS Consistency (Opp 15.5)

| # | Solution Idea | Feasibility | Cost Impact | Outcome Impact | Priority |
|---|--------------|-------------|-------------|----------------|----------|
| 1 | 8 reflectors at 45 deg perimeter spacing | HIGH | Included in above | ≤±2 dB through 360 deg | **P1** |
| 2 | Circular reflector array on rotating turntable | LOW | +$10K | Perfect consistency | P4 |
| 3 | Calculated overlap geometry (optimized spacing) | HIGH | $0 (design effort) | ≤±1.5 dB | **P1** |
| 4 | Supplementary flat panels between reflectors | HIGH | +$2K | Fill coverage gaps | P2 |

**Decision:** #1 + #3. Optimize reflector spacing and orientation angle using RCS simulation (CST/FEKO) to achieve ≤±2 dB through full rotation.

#### Outcome O-71: Total Cost of Ownership (Opp 15.0)

| # | Solution Idea | Feasibility | Cost Impact | Outcome Impact | Priority |
|---|--------------|-------------|-------------|----------------|----------|
| 1 | Reusable flotation (TPMS) — survive, reuse | HIGH | +$10K unit, -$200K campaign | TCO -70% for 10 tests | **P1** |
| 2 | Modular replaceable superstructure | HIGH | +$3K unit | Replace damaged parts only | **P1** |
| 3 | Standardized reflector modules (bolt-on) | HIGH | +$1K | Swap in field, no factory | **P1** |
| 4 | Digital twin for pre-test validation | MEDIUM | +$15K (development) | Reduce physical tests needed | P2 |
| 5 | Shared target pool with ASEAN allies | LOW (political) | N/A | Amortize over more users | P3 |

**Decision:** #1 + #2 + #3 form the "modular reusable platform" concept. This is the core value proposition of VN-TGT-SEA-001-H.

#### Outcome O-62: Cost per Test (Opp 14.9)

Directly addressed by O-57 and O-71 solutions. Reusable target reduces cost/test from $50-100K → $10-20K (replace only damaged modules).

---

## Step 9: Customer Scorecard Evaluation

### Concepts Evaluated

| Concept | Description | Key Feature |
|---------|------------|-------------|
| **Current** | Ad-hoc target barge with bolted reflectors | Baseline (expendable, inconsistent) |
| **A: Base THANH TRI** | VN-AST-MSL-001 traditional manufacturing | HDPE pontoon, 8 hand-made reflectors, propane IR |
| **B: THANH TRI-H Phased** | VN-TGT-SEA-001-H phased Hyperganic | TPMS core, AM reflectors, Schwarz P IR, modular |
| **C: Full Premium** | Maximum AM, 3-point mooring, Luneburg lens | Everything AM, highest performance, highest cost |

### Scorecard (Top 10 Outcomes)

| Outcome | Opp | Weight | Current | A: Base | B: THANH TRI-H | C: Premium |
|---------|-----|--------|---------|---------|----------------|------------|
| O-57: Survivability (multiple hits) | 18.0 | 0.18 | 1 | 2 | **9** | 10 |
| O-29: Seeker acquisition (stationary) | 15.6 | 0.14 | 4 | 7 | **9** | 10 |
| O-31: 360 deg RCS consistency | 15.5 | 0.13 | 3 | 6 | **9** | 10 |
| O-71: Total cost of ownership | 15.0 | 0.12 | 2 | 5 | **8** | 4 |
| O-40: Seeker acquisition at range | 15.0 | 0.10 | 4 | 7 | **9** | 10 |
| O-62: Cost per test | 14.9 | 0.10 | 2 | 5 | **8** | 4 |
| O-30: RCS reliability | 14.5 | 0.08 | 4 | 7 | **9** | 10 |
| O-32: 360 deg IR visibility | 14.0 | 0.05 | 3 | 6 | **8** | 9 |
| O-42: RCS fades during approach | 14.0 | 0.05 | 3 | 6 | **8** | 9 |
| O-73: Indigenous content | 14.0 | 0.05 | 5 | 8 | **8** | 5 |
| **WEIGHTED SCORE** | | **1.00** | **2.78** | **5.40** | **8.56** | **7.60** |

> **Rev B.1:** Concept B now uses 8.0m platform, 0.8m hybrid reflectors (>1,000 m² RCS), no superstructure, no IR (radar-only), reflectors at 3-4m on masts. Unit cost $35,640. TPMS and Schwarz P removed.

### Scorecard Analysis

```
CONCEPT EVALUATION RESULT
══════════════════════════════════════════════════════════════

  Concept B: THANH TRI-H    ████████████████████ 8.56  ← WINNER
  Concept C: Premium         ███████████████████  7.60
  Concept A: Base THANH TRI  █████████████        5.40
  Current (ad-hoc barge)     ██████               2.78

  Decision threshold: 8.0+ = High success probability
  Concept B: 8.56 > 8.0 → RECOMMEND PROCEED
```

### Why Concept B Wins Over C

| Factor | B: THANH TRI-H | C: Premium |
|--------|----------------|------------|
| Survivability | 9 (TPMS, 50+ hits) | 10 (TPMS + armor) |
| RCS accuracy | 9 (AM ±0.1 deg) | 10 (Luneburg + AM) |
| TCO | **8** (reusable, $45K unit) | **4** ($55K unit, complex) |
| Cost/test | **8** ($10-20K) | **4** ($25-30K) |
| Indigenous | **8** (85-90%) | **5** (60%, Luneburg import) |
| Deployment complexity | **8** (single anchor) | **5** (3-point mooring) |

**Concept C** has marginally better technical scores but is penalized heavily on cost, TCO, and indigenous content — the outcomes most important to Segment A (45% of stakeholders).

### Decision

**SELECTED: Concept B — THANH TRI-H (Phased Hyperganic Enhancement)**
- Scorecard: **8.56/10** (exceeds 8.0 threshold)
- Addresses all 5 EXTREME opportunities
- Phased investment de-risks Hyperganic technology
- 85-90% indigenous content
- $318K total development (27% premium for 500%+ value increase)

---

## Step 10: Growth Strategy Selection

### Strategy Analysis

```
                    OVERSERVED ◄────────────────► UNDERSERVED
                         │                              │
    ┌────────────────────┼──────────────────────────────┼────────────────────┐
    │                    │                              │                    │
    │   DISRUPTIVE       │                              │   DIFFERENTIATED   │
    │                    │                              │                    │
LOW │   Not applicable:  │                              │   ★ VN-TGT-SEA-001│
    │   Market needs are │                              │   Unique "unsink-  │
COST│   deeply           │                              │   able" feature    │
    │   underserved      │                              │   at lower cost    │
    │                    │                              │   than alternatives│
    │                    │                              │                    │
    ├────────────────────┼──────────────────────────────┼────────────────────┤
    │                    │                              │                    │
    │   DISCRETE         │                              │   DOMINANT         │
    │                    │                              │                    │
HIGH│   SINKEX           │                              │   QinetiQ USV      │
    │   (declining,      │                              │   (best performance│
COST│    unsustainable)  │                              │    but $300K+)     │
    │                    │                              │                    │
    └────────────────────┴──────────────────────────────┴────────────────────┘
```

### Selected Strategy: DIFFERENTIATED

| Dimension | Decision | Rationale |
|-----------|----------|-----------|
| **Primary strategy** | DIFFERENTIATED | Unique capabilities (survivability, 360 deg precision RCS) that no competitor offers, at competitive cost |
| **Target segment** | Segment A (Efficiency) + Segment B (Accuracy) | Combined 80% of market; Segment C inherently served by anchored design |
| **Pricing** | $40-45K/unit (vs $32K base, vs $200-300K USV) | Premium over base justified by reusability ROI |
| **Differentiation basis** | "Unsinkable" TPMS core + precision AM reflectors | Protected by AM manufacturing knowledge barrier |
| **Competitive moat** | Design knowledge (TPMS parameters, RCS optimization) | Not patentable but requires significant expertise |

### Growth Roadmap

```
GROWTH STRATEGY: VN-TGT-SEA-001-H
══════════════════════════════════════════════════════════════

PHASE 1: DOMESTIC BEACHHEAD (2026-2027)
├── Vietnamese Navy missile acceptance testing
├── Target: 10-20 units, $400-900K revenue
├── Prove: Survivability, RCS accuracy, reusability
└── Build: AM manufacturing supply chain

PHASE 2: REGIONAL EXPANSION (2027-2028)
├── ASEAN navies: Indonesia, Malaysia, Philippines, Thailand
├── All operate anti-ship missiles requiring acceptance testing
├── Target: 50-100 units/year, $2-4M/year revenue
├── Advantage: Non-ITAR, non-EAR, competitive price
└── Marketing: Live-fire demo video as proof

PHASE 3: TECHNOLOGY PLATFORM (2028+)
├── Extend TPMS technology to Target USV, Towed Targets
├── AM reflector library for custom RCS profiles
├── Digital twin service (simulate before build)
├── Target: Technology licensing + product sales
└── Cross-portfolio value: $100-200K saved internally

MARKET SIZE ESTIMATE:
├── ASEAN missile acceptance tests: ~100-200/year
├── Addressable with VN-TGT-SEA-001: ~50-100 targets/year
├── Revenue potential: $2-5M/year at $40-45K/unit
└── TOTAL ADDRESSABLE: $50-100M (10-year lifecycle)
```

---

## Summary Dashboard

> **Rev B.1 updates applied.** Key changes: 8.0m platform, radar-only, >1,000 m² RCS, 3-4m mast-mounted reflectors, $35,640/unit, 980 kg displacement. See [[phase0_final_revision.md]] for consolidated revision.

### ODI Analysis Summary

| Metric | Value |
|--------|-------|
| Job Executor | Naval Test & Evaluation Director |
| Core Job | Validate anti-ship missile via sea target engagement |
| Outcomes captured | 73 (8 job steps covered) |
| EXTREME opportunities (>15) | 5 (O-57, O-29, O-31, O-40, O-71) |
| HIGH opportunities (12-15) | 14 |
| Customer segments | 3 (Efficiency 45%, Accuracy 35%, Safety 20%) |
| Selected concept | B: THANH TRI-H (Phased Hyperganic) |
| Customer scorecard | **8.56/10** (threshold 8.0) |
| Growth strategy | **DIFFERENTIATED** |
| Revenue potential | $2-5M/year (ASEAN market) |

### Hyperganic Impact on Top Outcomes

| Outcome | Before Hyperganic | After Hyperganic | Improvement |
|---------|-------------------|------------------|-------------|
| O-57: Survivability | 1-3 hits (sinks) | 50+ hits (floats) | **>10x** |
| O-29: Seeker acquisition | ±5 dBsm RCS accuracy | ±0.5 dBsm | **10x** |
| O-31: 360 deg RCS | 10+ dB gaps, ~180 deg | ≤2 dB variation, 360 deg | **5x** |
| O-62: Cost per test | $50-100K (expendable) | $10-20K (reusable) | **5x** |
| O-71: TCO 10 tests | $500K-$1M | $90-135K | **5-7x** |

### Open Items (TBDs)

| ID | Description | Owner | Target | Impact |
|----|-------------|-------|--------|--------|
| TBD-001 | ODI field survey validation (30-50 respondents) | Field survey team | Q2 2026 | Validate Imp/Sat estimates |
| TBD-002 | TPMS ballistic test (12.7mm, 10 rounds) | Engineering | Q1 2026 | Validate survivability claim |
| TBD-003 | AM reflector RCS measurement validation | Engineering + university | Q3 2026 | Validate ±0.5 dBsm claim |
| TBD-004 | ASEAN market size validation | Business development | Q3 2026 | Validate revenue potential |
| TBD-005 | AM service bureau selection (SG/TH/CN) | Procurement | Q1 2026 | Production feasibility |

---

## Cross-References

- [[../00_project_brief.md]] - Project brief
- [[../PROJECT_STATUS.md]] - Project status tracker
- [[../../../references/VN_Fixed_Sea_Target_Hyperganic_Enhancement.md]] - Hyperganic evaluation
- [[../../../references/VN_FIXED_SEA_TARGET_Complete_Analysis.md]] - Complete sea target analysis
- [[../../../references/Bia TL/VN_AST_MSL_001_Anchored_Target_Analysis.md]] - Anchored target UIEF analysis
- [[../../../references/Bia TL/VN_AST_MSL_001_Competitive_Comparison.md]] - Competitive comparison
