---
project: CORTEX-C2
phase: 0
type: product-phase0-complete
subject: CORTEX RANGE "TRƯỜNG BẮN" — Complete Phase 0 (ODI → Product → Architecture)
version: 1.0
created: 2026-02-12
status: complete
edition: RANGE
price_range: $15-25K perpetual + $3-5K/yr
---

# CORTEX RANGE "TRƯỜNG BẮN" — COMPLETE PHASE 0
## From Customer Pain → Product Architecture → Build Plan
### The AI Brain for Every Shooting Range on Earth

---

## STEP 0: WHY RANGE FIRST?

### The Portfolio Prioritization (Musk Rule: Serialize)

```
CORTEX C2 has 5 editions. Building all 5 simultaneously = death.
Musk Rule: "Build 1 thing. Make it work. Then build the next."

PRIORITIZATION MATRIX:
╔══════════╦═══════╦══════════╦═════════╦══════════╦═════════╦═══════╗
║ Edition  ║ Risk  ║ Time to  ║ Data    ║ Revenue  ║ Gateway ║ SCORE ║
║          ║       ║ Revenue  ║ Flywheel║ Ceiling  ║ to Next ║       ║
╠══════════╬═══════╬══════════╬═════════╬══════════╬═════════╬═══════╣
║ RANGE    ║ LOW   ║ 3 months ║ HIGH    ║ Medium   ║ →BASE   ║ ★★★★★║
║ BASE     ║ MED   ║ 6 months ║ HIGH    ║ High     ║ →SHIELD ║ ★★★★ ║
║ SHIELD   ║ HIGH  ║ 9 months ║ MED     ║ V.High   ║ →ENTER. ║ ★★★  ║
║ NAVAL    ║ HIGH  ║ 12 months║ LOW     ║ V.High   ║ →ENTER. ║ ★★   ║
║ ENTERPRISE║V.HIGH║ 18 months║ V.HIGH  ║ Highest  ║ (final) ║ ★★   ║
╚══════════╩═══════╩══════════╩═════════╩══════════╩═════════╩═══════╝

RANGE wins because:
1. LOWEST RISK — Training has lowest classification; no lethal decisions
2. FASTEST REVENUE — Ranges exist today; deploy in <1 day
3. HIGHEST DATA VALUE — Every shot = training data for ALL AI engines
4. BEST GATEWAY — Range customer buys BASE next (same commander)
5. PROVEN HARDWARE — VN-LOMAH + VN-CAM already exist in Workshop X
```

---

## STEP 1: JOB EXECUTOR ANALYSIS (Who Is the Customer?)

### 1.1 Primary Job Executor: Training Officer (Sĩ Quan Huấn Luyện)

| Attribute | Detail |
|-----------|--------|
| **Role** | Plans, executes, and evaluates unit training programs |
| **Rank** | Captain to Lieutenant Colonel (Đại úy → Trung tá) |
| **Core Job** | "Ensure soldiers achieve combat readiness standards through systematic training" |
| **Frequency** | Weekly range sessions; monthly qualification; quarterly exercises |
| **Current Tools** | Paper scorecards, manual target inspection, Excel spreadsheets, verbal reports |
| **Pain Level** | EXTREME — spends 60%+ of time on admin, not coaching |
| **Budget Authority** | $5-50K (unit training budget); influences $50-500K (higher command) |

### 1.2 Secondary Job Executors

| Executor | Core Job | Interaction with RANGE | Key Outcome |
|----------|----------|----------------------|-------------|
| **Range NCO** (Quản lý trường bắn) | "Operate range safely and efficiently" | Daily user — operates scoring, safety, targets | T21: Min prep time |
| **Unit Commander** (Chỉ huy đơn vị) | "Know unit readiness at all times" | Weekly consumer — reads dashboards, reports | T03: Compare units |
| **Individual Soldier** (Binh sĩ) | "Improve my shooting to survive combat" | Per-session — sees scores, gets AI coaching | T04: Instant feedback |
| **Higher Command** (Chỉ huy cấp trên) | "Allocate resources to maximize readiness" | Monthly consumer — cross-unit analytics | T22: Cross-unit analysis |
| **Technical Operator** (Kỹ thuật viên) | "Keep training systems running 24/7" | Maintenance — system health, calibration | T19: Min expert dependency |
| **Instructor/Coach** (Huấn luyện viên) | "Teach soldiers to shoot better, faster" | Real-time — AI-augmented coaching insights | T12: AI error classification |

### 1.3 Job Map: Training Officer's Workflow

```
BEFORE RANGE DAY          DURING RANGE DAY          AFTER RANGE DAY
═══════════════           ════════════════           ═══════════════

1. PLAN                   5. EXECUTE                9. DEBRIEF
   • Select exercise         • Monitor firing          • Review scores
   • Assign lanes            • Observe technique       • Identify patterns
   • Set standards           • Ensure safety           • Coach individuals
   • Prepare targets         • Track ammunition        • Discuss lessons

2. PREPARE                6. SCORE                  10. REPORT
   • Setup range             • Count hits              • Compile results
   • Calibrate systems       • Record scores           • Write report
   • Brief soldiers          • Calculate quals          • Submit to command
   • Distribute ammo         • Verify manual count     • File records

3. BRIEF                  7. ADJUST                 11. ANALYZE
   • Safety brief            • Change drills           • Compare to last
   • Exercise overview       • Swap personnel          • Trend over time
   • Standards review        • Modify difficulty       • Identify at-risk

4. VERIFY                 8. DOCUMENT               12. PLAN NEXT
   • Range clear             • Write observations      • Based on data
   • Communications          • Note malfunctions       • Predict needs
   • Medical standby         • Record conditions       • Schedule training
                             (weather, visibility)

PAIN POINTS (marked with ⚡):
─────────────────────────────
⚡ Step 1: No data to plan with (gut feeling only)
⚡ Step 6: Manual scoring takes 30-60 min, error-prone
⚡ Step 8: Documentation is manual, incomplete, often skipped
⚡ Step 9: Debrief is delayed hours/days after event
⚡ Step 10: Report takes 1-3 days to compile manually
⚡ Step 11: No cross-session analysis capability
⚡ Step 12: Planning is reactive, not predictive
```

---

## STEP 2: ODI OUTCOME ANALYSIS (What Do They Need?)

### 2.1 All 25 Training Domain Outcomes with RANGE Product Mapping

| # | Outcome Statement | Imp | Sat | Score | Zone | RANGE Product | Priority |
|---|-------------------|-----|-----|-------|------|--------------|----------|
| T01 | Min time to consolidate multi-system training results | 9.5 | 1.5 | **17.5** | EXTREME | CR-D3 PULSE + CR-D1 CDM | P0 |
| T02 | Min subjective bias in marksmanship evaluation | 9.0 | 2.0 | **16.0** | EXTREME | CR-L1 SCOREBOARD | P0 |
| T03 | Max cross-unit comparison on same scale | 9.0 | 1.5 | **16.5** | EXTREME | CR-N3 CLOUD + CR-D3 PULSE | P2 |
| T04 | Min time from shooting to detailed feedback | 9.5 | 3.0 | **16.0** | EXTREME | CR-L1 SCOREBOARD + CR-D3 PULSE | P0 |
| T05 | Max performance metrics auto-captured per shot | 8.5 | 2.0 | **15.0** | HIGH | CR-L1 + CR-L2 + CR-L4 | P0 |
| T06 | Min time to plan training from actual data | 8.0 | 2.5 | **13.5** | HIGH | CR-C3 PROPHECY | P3 |
| T07 | Max first-time qualification rate via trend analysis | 8.5 | 3.0 | **14.0** | HIGH | CR-C3 PROPHECY | P3 |
| T08 | Min time to detect declining soldier performance | 8.0 | 2.0 | **14.0** | HIGH | CR-D2 DEBRIEF + CR-C3 PROPHECY | P2 |
| T09 | Max individual training history traceability | 8.5 | 1.5 | **15.5** | EXTREME | CR-D1 CDM (Soldier Profile) | P1 |
| T10 | Min effort to generate training reports for command | 8.0 | 2.0 | **14.0** | HIGH | CR-D2 DEBRIEF (LLM auto-report) | P1 |
| T11 | Min time to setup/calibrate LOMAH-to-CAM connection | 7.5 | 3.0 | **12.0** | MEDIUM | CR-N1 MESH (auto-discovery) | P1 |
| T12 | Max AI accuracy in classifying shooting technique errors | 9.0 | 2.5 | **15.5** | EXTREME | CR-L2 OVERWATCH (VisualAI) | P1 |
| T13 | Min time to integrate new training scenario | 7.0 | 3.5 | **10.5** | MEDIUM | CR-C2 SCENARIO FORGE | P2 |
| T14 | Max multi-angle video replay and analysis | 8.0 | 1.5 | **14.5** | HIGH | CR-L2 OVERWATCH + CR-V1 MIRROR | P1 |
| T15 | Min training data loss or sync failure rate | 8.5 | 3.0 | **14.0** | HIGH | CR-N2 EDGE (offline store) + CR-N3 CLOUD | P1 |
| T16 | Max before/after performance comparison | 8.0 | 2.0 | **14.0** | HIGH | CR-D1 CDM + CR-D3 PULSE | P1 |
| T17 | Min switchover time between individual/collective training | 6.5 | 4.0 | **9.0** | OK | CR-C2 SCENARIO FORGE | P3 |
| T18 | Max weapon systems managed on single platform | 9.0 | 1.0 | **17.0** | EXTREME | CR-L4 WEAPONS LINK + CR-D1 CDM | P1 |
| T19 | Min dependency on technical experts for daily ops | 7.5 | 3.0 | **12.0** | MEDIUM | CR-N1 MESH (auto-discovery) | P2 |
| T20 | Max LVC standards compatibility | 7.0 | 1.5 | **12.5** | MEDIUM | CR-D4 EXPORT (DIS/HLA/TAK) | P1 |
| T21 | Min range cold-to-ready preparation time | 8.0 | 3.5 | **12.5** | MEDIUM | CR-N1 MESH + CR-N2 EDGE | P1 |
| T22 | Max cross-unit training data analysis | 8.5 | 1.0 | **16.0** | EXTREME | CR-N3 CLOUD + CR-C3 PROPHECY | P2 |
| T23 | Min training operations cost per soldier-hour | 8.0 | 3.0 | **13.0** | HIGH | ALL (automation reduces cost) | P2 |
| T24 | Max transparency/verifiability of evaluation results | 9.0 | 2.0 | **16.0** | EXTREME | CR-L1 SCOREBOARD + CR-D1 CDM | P0 |
| T25 | Min time to auto-generate qualification certificates | 7.0 | 2.0 | **12.0** | MEDIUM | CR-D2 DEBRIEF | P2 |

### 2.2 Outcome Priority Distribution by Build Phase

```
                    PHASE 1          PHASE 2          PHASE 3          PHASE 4          PHASE 5
                   (Month 1-3)      (Month 3-6)      (Month 6-9)      (Month 9-12)     (Month 12-18)
                   SCOREBOARD+      OVERWATCH+        TRACKER+          VIRTUAL+          CLOUD+
                   PULSE+CDM        DEBRIEF           MESH+EDGE         CONSTRUCT.        PROPHECY
                   ═══════════      ═══════════       ═══════════       ═══════════       ═══════════

EXTREME (≥15.0):   T01 ★ (17.5)    T09 (15.5)        T03 (16.5)        T13 (10.5)        T22 ★(16.0)
                   T02 ★ (16.0)    T12 (15.5)        T22 (16.0)                          T07 (14.0)
                   T04 ★ (16.0)    T18 (17.0)
                   T24 ★ (16.0)    T14 (14.5)
                   T05 (15.0)

HIGH (12-14.9):                    T10 (14.0)        T08 (14.0)        T06 (13.5)
                                   T15 (14.0)        T19 (12.0)        T17 (9.0)
                                   T16 (14.0)        T23 (13.0)
                                   T20 (12.5)        T25 (12.0)
                                   T21 (12.5)
                                   T11 (12.0)

OUTCOMES/PHASE:    5 (5 EXTREME)   10                 7                  3                  2
CUM. COVERAGE:     5/25 (20%)      15/25 (60%)       22/25 (88%)       25/25 (100%)      25/25
ODI SCORE AVG:     16.1            14.4               13.6              11.0               15.0
```

**Phase 1 addresses all 5 highest-scoring outcomes.** This is the "iPhone moment."

---

## STEP 3: COMPETITIVE FEATURE MAP (Where Do We Win?)

### 3.1 Feature-by-Feature Comparison: CORTEX RANGE vs Cubic vs Manual

| Feature | Manual Range | Cubic CTC | **CORTEX RANGE** | Winner |
|---------|-------------|-----------|-----------------|--------|
| **Shot scoring method** | Paper target inspection | MILES laser (kill/no-kill) | Acoustic LOMAH (<5mm) | **CORTEX** |
| **Scoring latency** | 30-60 min (walk downrange) | Real-time (binary only) | **Real-time + precise** | **CORTEX** |
| **Miss distance** | Not measured | Not measured | **<5mm accuracy** | **CORTEX** |
| **Shot grouping analysis** | Manual (ruler on paper) | Not available | **AI auto-analysis** | **CORTEX** |
| **Shooter technique analysis** | Instructor observation | Not available | **AI video analysis** | **CORTEX** |
| **Multi-lane monitoring** | 1 instructor per 2-4 lanes | N/A (force-on-force) | **1 dashboard, 50 lanes** | **CORTEX** |
| **Individual soldier profile** | Paper records (if kept) | Not tracked | **Digital, career-long** | **CORTEX** |
| **Cross-unit benchmarking** | Impossible | Same CTC only | **Cloud, any range** | **CORTEX** |
| **AI coaching** | None | None | **Real-time AI feedback** | **CORTEX** |
| **Auto-report generation** | N/A (manual, days) | Manual from CATS Metrix | **LLM, instant** | **CORTEX** |
| **Deployment time** | N/A (permanent) | 6-12 months | **< 1 day** | **CORTEX** |
| **Cost per range** | ~$0 (no system) | $5-50M | **$15-25K** | **CORTEX** |
| **Force-on-force sim** | None | **Full MILES ecosystem** | Not in V1 (future) | Cubic |
| **Air combat training** | None | **P5CTS ACMI** | Not in scope | Cubic |
| **CTC-scale exercise** | None | **4000-5000 players** | Company-level max | Cubic |
| **LVC integration** | None | **Full DIS/HLA/TENA** | DIS + TAK (V1) | Cubic |

**CORTEX wins 11/16 features.** Cubic wins only on CTC-scale force-on-force (4 features) — their $500M+ fortress.

### 3.2 Price-Performance Map

```
                          ← LOWER ANALYTICS              HIGHER ANALYTICS →
                                │                              │
         ┌──────────────────────┼──────────────────────────────┤
         │                      │                              │
$50M+ ───┤                      │  ■ Cubic CTC                 │
         │                      │    (NTC/JRTC)                │
         │                      │                              │
$5-50M ──┤   ■ Cubic Range      │                              │
         │     (non-CTC)        │        ■ Cubic + SPEAR       │
         │                      │          (2027?)             │
$1-5M ───┤                      │                              │
         │                      │                              │
         │                      │                              │
$50-300K─┤                      │                              │
         │                      │                              │
$15-50K──┤                      │            ★ CORTEX RANGE    │
         │                      │              (2026)          │
         │                      │                              │
$0 ──────┤  ■ Paper targets     │                              │
         │    (Vietnamese       │                              │
         │     ranges today)    │                              │
         └──────────────────────┼──────────────────────────────┘
```

---

## STEP 4: PRODUCT ARCHITECTURE (What Do We Build?)

### 4.1 Complete Product Tree with ODI Traceability

```
CORTEX RANGE "TRƯỜNG BẮN"
│
├── LIVE LAYER ──────────────────────────────────────────────────
│   │
│   ├── CR-L1: SCOREBOARD ★ ─── "The iPhone Moment"
│   │   ├── Function: Real-time acoustic shot scoring
│   │   ├── Hardware: VN-LOMAH sensor array (existing Workshop X product)
│   │   ├── Data Out: Shot event {timestamp, lane, position_mm, miss_distance_mm,
│   │   │              velocity_mps, angle_deg, grouping_id}
│   │   ├── ODI Outcomes: T02 (16.0), T04 (16.0), T05 (15.0), T24 (16.0)
│   │   ├── Specs:
│   │   │   ├── Accuracy: <5mm miss distance measurement
│   │   │   ├── Latency: <50ms shot detection to display
│   │   │   ├── Capacity: 50 lanes simultaneous
│   │   │   ├── Environment: -10°C to +55°C, rain/wind operational
│   │   │   └── Calibration: Auto-calibrate on power-up (<60s)
│   │   ├── User Story: "As a range NCO, I see every shot scored on my tablet
│   │   │   in real-time, so I never have to walk downrange to check paper."
│   │   └── Build Phase: 1 (Month 1-3) ★ FIRST
│   │
│   ├── CR-L2: OVERWATCH ─── "The AI Coach's Eyes"
│   │   ├── Function: AI video analytics for shooter technique
│   │   ├── Hardware: VN-CAM-T1 cameras (existing Workshop X product)
│   │   ├── Data Out: Technique event {timestamp, soldier_id, posture_score,
│   │   │              grip_quality, breathing_pattern, flinch_detected,
│   │   │              trigger_pull_analysis, video_clip_url}
│   │   ├── ODI Outcomes: T12 (15.5), T14 (14.5), T02 (16.0)
│   │   ├── Specs:
│   │   │   ├── Detection: Muzzle flash, ejection, recoil pattern
│   │   │   ├── Analysis: 12 technique error categories
│   │   │   │   ├── Flinching / anticipation
│   │   │   │   ├── Trigger jerk (vs smooth press)
│   │   │   │   ├── Breathing hold failure
│   │   │   │   ├── Sight alignment drift
│   │   │   │   ├── Grip pressure inconsistency
│   │   │   │   ├── Stance instability
│   │   │   │   ├── Follow-through break
│   │   │   │   ├── Head position (cheek weld)
│   │   │   │   ├── Elbow position
│   │   │   │   ├── Shoulder pocket (stock placement)
│   │   │   │   ├── Rate of fire inconsistency
│   │   │   │   └── Magazine change technique
│   │   │   ├── Frame rate: 30 fps analysis; 120 fps for slow-motion replay
│   │   │   ├── Multi-camera: 2-4 angles per firing position
│   │   │   └── AI model: CNN trained on annotated shooting technique dataset
│   │   ├── User Story: "As an instructor, I see AI annotations on video
│   │   │   showing me EXACTLY what each soldier is doing wrong, so I can
│   │   │   coach the specific error instead of guessing."
│   │   └── Build Phase: 2 (Month 3-6)
│   │
│   ├── CR-L3: TRACKER ─── "Where Every Soldier Goes"
│   │   ├── Function: Position and movement analytics
│   │   ├── Hardware: GPS/BLE tracker units ($200-500 each, commodity)
│   │   ├── Data Out: Position event {timestamp, soldier_id, lat, lon, alt,
│   │   │              heading_deg, speed_mps, stance(prone/kneel/stand),
│   │   │              weapon_orientation_3d}
│   │   ├── ODI Outcomes: T05 (15.0), T14 (14.5), T23 (13.0)
│   │   ├── Specs:
│   │   │   ├── Outdoor accuracy: <1m (GPS + RTK correction)
│   │   │   ├── Update rate: 1 Hz position, 10 Hz IMU
│   │   │   ├── Battery: 12+ hours continuous
│   │   │   ├── Weight: <100g per tracker
│   │   │   └── Output: Heat maps, movement replays, time-in-cover analysis
│   │   ├── User Story: "As a commander, I see heat maps showing where my
│   │   │   soldiers actually move during exercises, so I can identify
│   │   │   who uses cover effectively and who doesn't."
│   │   └── Build Phase: 3 (Month 6-9)
│   │
│   └── CR-L4: WEAPONS LINK ─── "Every Weapon Talks"
│       ├── Function: Direct weapon system data integration
│       ├── Hardware: Software API to Workshop X weapons (no new hardware)
│       ├── Data Out: Weapon event {timestamp, weapon_id, weapon_type,
│       │              round_count, burst_length, aim_point_3d,
│       │              traverse_rate, elevation_rate, fire_mode}
│       ├── ODI Outcomes: T18 (17.0), T05 (15.0)
│       ├── Integrations:
│       │   ├── VN-SMASH: Aim point, trigger event, calculated hit
│       │   ├── RCWS: Traverse, elevation, burst, ammunition type/count
│       │   ├── VN-LOMAH: Acoustic shot data (already via SCOREBOARD)
│       │   ├── Grenade launcher: Range, angle, fuze setting
│       │   └── Future: Mortar fire control, AT weapons
│       ├── User Story: "As a training officer, I manage rifle, RCWS,
│       │   and smart sight training results on ONE platform instead of
│       │   3 separate systems with 3 separate reports."
│       └── Build Phase: 2 (Month 3-6)
│
├── VIRTUAL LAYER ───────────────────────────────────────────────
│   │
│   ├── CR-V1: MIRROR ─── "Your Range in 3D"
│   │   ├── Function: Digital twin of physical range
│   │   ├── Technology: Photogrammetry scan → 3D model → web viewer
│   │   ├── Data In: Live training data overlaid on 3D model
│   │   ├── ODI Outcomes: T14 (14.5), T13 (10.5)
│   │   ├── Features:
│   │   │   ├── 3D replay of live exercises from any viewpoint
│   │   │   ├── "What-if" analysis (change wind, change distance)
│   │   │   ├── Trajectory visualization (shot path in 3D)
│   │   │   ├── Share replay files across units (cloud)
│   │   │   └── Compare replay to "gold standard" execution
│   │   ├── User Story: "As an instructor, I show the squad their exercise
│   │   │   from a bird's-eye view in 3D, highlighting what went right
│   │   │   and wrong — 10x more impactful than talking about it."
│   │   └── Build Phase: 4 (Month 9-12)
│   │
│   ├── CR-V2: GHOST ─── "Virtual Enemies, Real Training"
│   │   ├── Function: Virtual threat injection into live training
│   │   ├── Technology: AR overlay on tablets/HUDs; DIS entity injection
│   │   ├── ODI Outcomes: T13 (10.5), T17 (9.0)
│   │   ├── Features:
│   │   │   ├── Virtual pop-up targets (no mechanical target needed)
│   │   │   ├── Virtual moving targets with AI-controlled behavior
│   │   │   ├── Virtual indirect fire effects (audio + visual)
│   │   │   ├── Stress inoculation (simulated chaos)
│   │   │   └── SITL: Synthetic Inject to Live (via DIS protocol)
│   │   ├── User Story: "As a range NCO, I add 'enemies' to my flat range
│   │   │   with a tablet instead of buying $50K pop-up target mechanisms."
│   │   └── Build Phase: 4 (Month 9-12)
│   │
│   └── CR-V3: DOJO ─── "Train Without Ammo"
│       ├── Function: Indoor dry-fire training with AI coaching
│       ├── Technology: Laser emitter + camera + AI analysis
│       ├── ODI Outcomes: T04 (16.0), T12 (15.5), T23 (13.0)
│       ├── Features:
│       │   ├── Laser-based indoor shot detection
│       │   ├── AI technique analysis (same models as OVERWATCH)
│       │   ├── Progressive difficulty (AI adapts to skill level)
│       │   ├── Same CORTEX CDM data model (seamless live↔virtual)
│       │   └── Practice unlimited reps with zero ammunition cost
│       ├── User Story: "As a soldier, I practice my shooting fundamentals
│       │   indoors with AI coaching, then my scores carry over to
│       │   the live range dashboard."
│       └── Build Phase: 4 (Month 9-12)
│
├── CONSTRUCTIVE LAYER ──────────────────────────────────────────
│   │
│   ├── CR-C1: ADVERSARY ─── "AI Enemies That Learn"
│   │   ├── Function: AI-generated opposing force behaviors
│   │   ├── Technology: Behavior trees + reinforcement learning
│   │   ├── ODI Outcomes: T13 (10.5), T17 (9.0)
│   │   ├── Features:
│   │   │   ├── Procedural enemy behavior (not scripted)
│   │   │   ├── Adaptive difficulty (harder for experts, easier for novices)
│   │   │   ├── Doctrine database (threat-specific behaviors)
│   │   │   └── Eliminates need for 5-10 OPFOR controllers
│   │   └── Build Phase: 4 (Month 9-12)
│   │
│   ├── CR-C2: SCENARIO FORGE ─── "Describe It, Build It"
│   │   ├── Function: LLM-powered scenario generation
│   │   ├── Technology: LLM + scenario template engine + CDM
│   │   ├── ODI Outcomes: T13 (10.5), T06 (13.5)
│   │   ├── Features:
│   │   │   ├── Natural language: "Create platoon defense scenario, 12 targets"
│   │   │   ├── Auto-populates: target positions, timing, scoring criteria
│   │   │   ├── 100+ template library (customizable)
│   │   │   └── Export to DIS for virtual/live integration
│   │   └── Build Phase: 4 (Month 9-12)
│   │
│   └── CR-C3: PROPHECY ─── "Predict Before They Fail"
│       ├── Function: Predictive readiness engine
│       ├── Technology: ML regression + time-series analysis + Bayesian
│       ├── ODI Outcomes: T07 (14.0), T08 (14.0), T06 (13.5), T22 (16.0)
│       ├── Features:
│       │   ├── Predicts unit readiness score from historical data
│       │   ├── Identifies "at risk" soldiers 2-4 weeks before qual failure
│       │   ├── Recommends specific training interventions
│       │   ├── Correlates training patterns with qualification outcomes
│       │   └── Cross-unit readiness comparison dashboard
│       ├── User Story: "As a commander, I see that 3rd Platoon's readiness
│       │   score is declining and PROPHECY recommends extra trigger control
│       │   drills — before they fail next month's qualification."
│       └── Build Phase: 5 (Month 12-18)
│
├── DATA LAYER ──────────────────────────────────────────────────
│   │
│   ├── CR-D1: CORTEX CDM ★ ─── "One Language for All Training Data"
│   │   ├── Function: Unified Common Data Model for training events
│   │   ├── Technology: JSON Schema, versioned, open specification
│   │   ├── ODI Outcomes: T01 (17.5), T15 (14.0), T18 (17.0)
│   │   ├── Schema Objects:
│   │   │   ├── ShotEvent {timestamp, lane_id, soldier_id, weapon_id,
│   │   │   │    position_mm, miss_distance_mm, velocity_mps, angle_deg,
│   │   │   │    grouping_id, environmental_conditions}
│   │   │   ├── TechniqueEvent {timestamp, soldier_id, camera_id,
│   │   │   │    error_type, confidence, video_clip_ref, ai_model_version}
│   │   │   ├── PositionEvent {timestamp, soldier_id, lat, lon, alt,
│   │   │   │    heading, speed, stance, weapon_orientation}
│   │   │   ├── WeaponEvent {timestamp, weapon_id, event_type,
│   │   │   │    round_count, aim_point, fire_mode}
│   │   │   ├── SoldierProfile {soldier_id, unit_id, rank, weapon_quals[],
│   │   │   │    training_history[], performance_trend, readiness_score}
│   │   │   ├── UnitProfile {unit_id, soldiers[], aggregate_stats,
│   │   │   │    readiness_score, comparison_percentile}
│   │   │   ├── SessionProfile {session_id, date, range_id, exercise_type,
│   │   │   │    weather, participants[], events[], ai_summary}
│   │   │   └── ScenarioProfile {scenario_id, type, targets[], timing[],
│   │   │        scoring_criteria[], difficulty_level}
│   │   ├── Key Design Decisions:
│   │   │   ├── JSON-based (not protobuf) — human readable, debuggable
│   │   │   ├── Open specification — published, anyone can implement
│   │   │   ├── Superset of DIS PDU data — can ingest DIS entities
│   │   │   ├── Acoustic extension — data Cubic/DIS cannot represent
│   │   │   └── AI annotation layer — model outputs attached to events
│   │   └── Build Phase: 1 (Month 1-3) ★ FIRST
│   │
│   ├── CR-D2: DEBRIEF ─── "AI Writes the Report"
│   │   ├── Function: Automated intelligent after-action review
│   │   ├── Technology: Time-series analysis + LLM narrative generation
│   │   ├── ODI Outcomes: T10 (14.0), T16 (14.0), T09 (15.5), T25 (12.0)
│   │   ├── Output Types:
│   │   │   ├── Instant Replay: Synchronized multi-source playback
│   │   │   ├── AI Highlights: Auto-detected key moments (best/worst/unusual)
│   │   │   ├── Performance Card: Per-soldier summary with trend arrows
│   │   │   ├── Narrative Report: LLM-generated text (Vietnamese/English)
│   │   │   ├── Qualification Certificate: Auto-generated with digital sig
│   │   │   └── Commander Brief: 1-page executive summary
│   │   └── Build Phase: 2 (Month 3-6)
│   │
│   ├── CR-D3: PULSE ★ ─── "See Everything, Right Now"
│   │   ├── Function: Real-time training monitoring dashboard
│   │   ├── Technology: Web app (React) + WebSocket real-time updates
│   │   ├── ODI Outcomes: T01 (17.5), T04 (16.0), T24 (16.0)
│   │   ├── Views:
│   │   │   ├── Range View: All lanes, live scores, active shooters
│   │   │   ├── Soldier View: Individual shot-by-shot, technique notes
│   │   │   ├── Unit View: Aggregate stats, qualification progress
│   │   │   ├── Safety View: Range fan overlay, cease-fire status, alerts
│   │   │   ├── Ammo View: Round count by lane/weapon/total
│   │   │   └── Commander View: Multi-range overview (cloud-connected)
│   │   ├── Platforms: Web browser (any device), ATAK plugin, mobile app
│   │   └── Build Phase: 1 (Month 1-3) ★ FIRST
│   │
│   └── CR-D4: EXPORT ─── "Your Data, Your Way"
│       ├── Function: Integration with external systems
│       ├── Technology: REST API + protocol adapters
│       ├── ODI Outcomes: T20 (12.5), T01 (17.5)
│       ├── Adapters:
│       │   ├── DIS (IEEE 1278): Publish CORTEX events as DIS PDUs
│       │   │   Implementation: Open-DIS library (Java/Python/C++)
│       │   │   Use case: Feed data to existing LVC systems
│       │   ├── TAK/CoT: Publish to ATAK/WinTAK cursor-on-target
│       │   │   Implementation: CoT XML over multicast/TCP
│       │   │   Use case: Training data on tactical map display
│       │   ├── HLA (IEEE 1516): Federate with simulation systems
│       │   │   Implementation: OpenRTI or Portico RTI
│       │   │   Use case: Connect virtual/constructive simulations
│       │   ├── REST API: JSON over HTTPS for third-party apps
│       │   │   Implementation: OpenAPI 3.0 specification
│       │   │   Use case: Custom dashboards, analytics tools
│       │   └── CSV/Excel: Flat file export for manual analysis
│       │       Use case: Commanders who love spreadsheets
│       └── Build Phase: 2-3 (DIS+TAK in Phase 2; HLA in Phase 3)
│
└── NETWORK LAYER ───────────────────────────────────────────────
    │
    ├── CR-N1: MESH ─── "Plug In, It Works"
    │   ├── Function: Self-organizing sensor network
    │   ├── Technology:
    │   │   ├── LoRa 868/915 MHz: Sensor data (low bandwidth, 1-5 km)
    │   │   ├── WiFi 6E: Video/high-bandwidth (short range, 100m)
    │   │   └── 4G/5G: Cloud backhaul (where cellular available)
    │   ├── ODI Outcomes: T11 (12.0), T21 (12.5), T19 (12.0)
    │   ├── Features:
    │   │   ├── Auto-discovery: New sensor appears on dashboard automatically
    │   │   ├── Self-healing: Route around failed nodes
    │   │   ├── Range: 1-5 km between nodes (LoRa)
    │   │   └── Setup: Power on → connected in <60 seconds
    │   └── Build Phase: 3 (Month 6-9)
    │
    ├── CR-N2: EDGE ─── "The Range Brain"
    │   ├── Function: Local AI processing and data storage
    │   ├── Hardware: ARM-based edge compute (NVIDIA Jetson Orin NX or AGX)
    │   ├── ODI Outcomes: T15 (14.0), T21 (12.5)
    │   ├── Specs:
    │   │   ├── Processing: 100 TOPS AI inference
    │   │   ├── Storage: 1TB NVMe (30 days offline data)
    │   │   ├── Power: 15-60W (solar/battery capable)
    │   │   ├── Environment: IP65, -20°C to +60°C
    │   │   ├── Models: ONNX Runtime for cross-framework inference
    │   │   └── Updates: OTA model + firmware updates
    │   ├── Comparison: Cubic DTECH Fusion eHPC = AMD EPYC 64-core,
    │   │   NVIDIA RTX 5000, 512GB RAM. Cost: ~$50-100K.
    │   │   CORTEX EDGE = Jetson Orin. Cost: ~$2-5K. 20-50x cheaper.
    │   └── Build Phase: 3 (Month 6-9)
    │
    └── CR-N3: CLOUD ─── "Every Range Connected"
        ├── Function: Multi-range sync, federated analytics, model training
        ├── Technology: Cloud backend (AWS/Azure or on-prem Kubernetes)
        ├── ODI Outcomes: T03 (16.5), T22 (16.0), T15 (14.0)
        ├── Features:
        │   ├── Range-to-cloud sync (daily/real-time configurable)
        │   ├── Cross-unit benchmarking dashboard
        │   ├── Federated ML model training (data stays local, models shared)
        │   ├── OTA model distribution to edge nodes
        │   └── Backup + disaster recovery
        ├── Security:
        │   ├── AES-256 encryption in transit and at rest
        │   ├── Air-gapped option (on-prem deployment)
        │   ├── Role-based access control (RBAC)
        │   └── Audit logging (all data access tracked)
        └── Build Phase: 5 (Month 12-18)
```

---

## STEP 5: DATA FLOW ARCHITECTURE

### 5.1 End-to-End Data Flow (Single Range)

```
PHYSICAL WORLD                    EDGE LAYER                      USER LAYER
═══════════════                   ═════════                       ═══════════

 Soldier fires  ──→  VN-LOMAH  ──→  CR-N2    ──→  CR-D1 CDM  ──→  CR-D3 PULSE
 a bullet           (acoustic)     EDGE NODE       (data store)    (dashboard)
                        │              │                │              │
                        ▼              ▼                ▼              ▼
                    ShotEvent      AI Inference     SoldierProfile  Range View
                    {miss: 23mm}   {grouping: 4.2}  {trend: ↑}     [live scores]
                                       │
 VN-CAM records ──→  VN-CAM-T1 ──→    │
 muzzle flash        (camera)         │
                        │              │
                        ▼              ▼
                    VideoFrame     TechniqueEvent
                    {30 fps}       {flinch: 0.87}
                                       │
                                       ▼
                                  CR-D2 DEBRIEF ──→ Commander
                                  (AI analysis)     (1-page report)
                                       │
                                       ▼
                                  CR-D4 EXPORT
                                  ├── DIS PDU → LVC systems
                                  ├── CoT XML → TAK/ATAK
                                  └── REST API → 3rd party
```

### 5.2 Multi-Range Data Flow (Cloud Connected)

```
RANGE A (Hanoi)          RANGE B (Da Nang)         RANGE C (HCMC)
═══════════════          ═════════════════          ═══════════════
CR-N2 EDGE              CR-N2 EDGE                CR-N2 EDGE
    │                        │                         │
    └────────────┐          │         ┌───────────────┘
                 ▼          ▼         ▼
              ┌──────────────────────────┐
              │      CR-N3 CLOUD          │
              │  ┌────────────────────┐   │
              │  │ Federated ML Train │   │
              │  │ Cross-unit Compare │   │
              │  │ Model Distribution │   │
              │  │ Readiness Predict  │   │
              │  └────────────────────┘   │
              └───────────┬──────────────┘
                          │
                          ▼
              ┌──────────────────────────┐
              │   HIGHER COMMAND PORTAL    │
              │  • National readiness map  │
              │  • Unit comparison         │
              │  • Resource allocation     │
              │  • Trend analysis          │
              └──────────────────────────┘
```

---

## STEP 6: SYSTEMS DYNAMICS (RANGE-Specific)

### 6.1 RANGE Data Flywheel

```
                    THE RANGE DATA FLYWHEEL
                    ═══════════════════════

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │   ① Sell VN-LOMAH hardware                         │
    │      (range gets SCOREBOARD free)                   │
    │              │                                      │
    │              ▼                                      │
    │   ② Range officers see real-time scores             │
    │      → "I can't go back to paper"                  │
    │              │                                      │
    │              ▼                                      │
    │   ③ Subscribe to RANGE STANDARD                    │
    │      (OVERWATCH + DEBRIEF + EXPORT)                │
    │              │                                      │
    │              ▼                                      │
    │   ④ Every shot generates training data              │
    │      → Acoustic + Video + Weapon → CORTEX CDM      │
    │              │                                      │
    │              ▼                                      │
    │   ⑤ AI models improve with more data                │
    │      → Better error detection                      │
    │      → Better readiness prediction                 │
    │      → Better coaching recommendations             │
    │              │                                      │
    │              ▼                                      │
    │   ⑥ Word spreads: "Range X has AI coaching"         │
    │      → Other units demand CORTEX                   │
    │              │                                      │
    │              ▼                                      │
    │   ⑦ More ranges deployed                           │
    │      → More data → Better AI → More demand → ...   │
    │                                                     │
    │   FLYWHEEL ACTIVATION: ~10-15 ranges (50K shots/mo) │
    │   ESCAPE VELOCITY: ~50+ ranges (500K shots/mo)      │
    │                                                     │
    └─────────────────────────────────────────────────────┘
```

### 6.2 RANGE-to-Platform Upsell Path

```
MONTH 1          MONTH 6          MONTH 12         MONTH 18
════════         ════════          ════════         ════════

VN-LOMAH    ──→  VN-CAM-T1   ──→  VN-CAM-B1   ──→  VN-LOMAH-AD
(range)          (range)           (perimeter)       (C-UAS)
    │                │                  │                │
    ▼                ▼                  ▼                ▼
CORTEX         CORTEX            CORTEX           CORTEX
RANGE FREE     RANGE STD         BASE             SHIELD
($0)           ($15K+$3K/yr)     ($35K+$8K/yr)    ($60K+$15K/yr)

CLV: $5K       CLV: $45K         CLV: $115K       CLV: $250K+

SAME CUSTOMER, SAME COMMANDER, EXPANDING USE CASE
```

---

## STEP 7: BUILD PLAN (Serial Execution)

### 7.1 Five-Phase Build Roadmap

| Phase | Month | Products | Team | Validation Gate | Revenue |
|-------|-------|----------|------|----------------|---------|
| **1** | 1-3 | SCOREBOARD + PULSE + CDM v1 | 2 devs | Range officers stop using paper | $0 (free) |
| **2** | 3-6 | OVERWATCH + DEBRIEF + WEAPONS LINK + EXPORT(DIS/TAK) | 3 devs | Officers share reports proudly | $15K × 5 |
| **3** | 6-9 | TRACKER + MESH + EDGE + CDM v1.2 | 3 devs | Units request for field exercises | $15K × 10 |
| **4** | 9-12 | MIRROR + GHOST + DOJO + ADVERSARY + SCENARIO FORGE | 4 devs | Scenarios created in <30 min | $25K × 5 |
| **5** | 12-18 | CLOUD + PROPHECY + EXPORT(HLA) + CDM v2 | 4 devs | General makes decisions from data | $50K × 3 |

### 7.2 Phase 1 Sprint Plan (SCOREBOARD + PULSE + CDM)

```
SPRINT 1 (Week 1-2): FOUNDATION
├── Define CORTEX CDM v1.0 schema (ShotEvent, SessionProfile)
├── Setup project: Python backend + React frontend + TimescaleDB
├── VN-LOMAH serial/UDP data parser (existing protocol)
└── Deliverable: Shot data flows from LOMAH → DB → console log

SPRINT 2 (Week 3-4): DASHBOARD MVP
├── PULSE web dashboard: Range view (lane grid + live scores)
├── WebSocket real-time updates (LOMAH → backend → browser)
├── Shot grouping calculation (mean radius, extreme spread)
└── Deliverable: See live shots on browser in <100ms

SPRINT 3 (Week 5-6): SCORING ENGINE
├── Qualification scoring rules (Vietnamese military standards)
├── Session management (start/stop/pause exercise)
├── Lane assignment (soldier → lane mapping)
└── Deliverable: Automatic pass/fail qualification scoring

SPRINT 4 (Week 7-8): SOLDIER PROFILES + POLISH
├── SoldierProfile in CDM (name, unit, weapon quals, history)
├── Session history (view past sessions, compare)
├── Basic trend visualization (improving / declining / stable)
├── Mobile-responsive design (works on tablet in the field)
└── Deliverable: RANGE officers at 1 Vietnamese range use it for real

SPRINT 5 (Week 9-10): HARDENING + DEPLOY
├── Error handling, offline resilience, auto-reconnect
├── User authentication (simple token-based for V1)
├── Installation documentation (1-page setup guide)
├── Performance testing (50 lanes × 10 shots/min = 500 events/min)
└── Deliverable: System runs for 8 hours without intervention

SPRINT 6 (Week 11-12): FIELD TRIAL + ITERATE
├── Deploy at 1-2 Vietnamese ranges
├── Observe range officers using the system
├── Collect feedback (what's missing? what's confusing?)
├── Fix top 5 issues
└── Deliverable: GO/NO-GO decision for Phase 2
```

---

## STEP 8: TECHNOLOGY STACK RECOMMENDATION

### 8.1 Stack Selection (First Principles)

| Layer | Technology | Why |
|-------|-----------|-----|
| **Frontend** | React + TypeScript + Leaflet/MapLibre | Web-based = works on any device; React ecosystem mature; maps for range layout |
| **Backend** | Python (FastAPI) | Fastest development; AI/ML ecosystem; async capable |
| **Database** | TimescaleDB (PostgreSQL extension) | Time-series optimized for shot events; SQL familiar; hypertable partitioning |
| **Real-time** | WebSocket (via FastAPI) | Sub-100ms dashboard updates |
| **AI/ML** | PyTorch → ONNX → ONNX Runtime | Train in PyTorch; deploy as ONNX for edge + cloud |
| **Edge compute** | NVIDIA Jetson Orin NX | 100 TOPS AI; $500-800; low power; ONNX Runtime native |
| **Sensor comms** | Serial/UDP (LOMAH) + RTSP (cameras) | Match existing VN-LOMAH + VN-CAM protocols |
| **Mesh network** | LoRa (Meshtastic) + WiFi 6E | Open-source mesh; commodity hardware |
| **Cloud** | Kubernetes (K3s for edge, K8s for cloud) | Same stack edge-to-cloud; on-prem or AWS/Azure |
| **Protocol adapters** | Open-DIS (Python) + CoT (XML) | Open-source DIS; simple CoT XML |
| **LLM (reports)** | Local LLM (Llama/Qwen) or API | Vietnamese language support; runs on edge GPU |

### 8.2 Why NOT These Alternatives

| Alternative | Why Not |
|-------------|---------|
| C++/Rust backend | Slower development; RANGE needs speed-to-market, not microsecond latency |
| MongoDB/NoSQL | Time-series queries are 10-100x slower than TimescaleDB for our workload |
| gRPC/Protobuf | Adds complexity; JSON+WebSocket is sufficient for RANGE data rates |
| TensorFlow | PyTorch dominates research; ONNX export handles deployment |
| Custom SDR mesh | Overkill; LoRa + WiFi covers RANGE network needs at 1/100th cost |
| Unity/Unreal (3D) | Too heavy for V1; Three.js sufficient for MIRROR digital twin |

---

## STEP 9: PRICING & BUSINESS MODEL

### 9.1 Edition Tiers with Feature Matrix

| Feature | FREE | STANDARD ($15K+$3K/yr) | PRO ($25K+$5K/yr) | ENTERPRISE ($50K+$10K/yr) |
|---------|------|----------------------|-------------------|--------------------------|
| CR-L1 SCOREBOARD | ✅ | ✅ | ✅ | ✅ |
| CR-D3 PULSE (basic) | ✅ | ✅ | ✅ | ✅ |
| CR-D1 CDM | ✅ | ✅ | ✅ | ✅ |
| CR-L2 OVERWATCH | — | ✅ | ✅ | ✅ |
| CR-D2 DEBRIEF | — | ✅ | ✅ | ✅ |
| CR-L4 WEAPONS LINK | — | ✅ | ✅ | ✅ |
| CR-D4 EXPORT (DIS/TAK) | — | ✅ | ✅ | ✅ |
| CR-L3 TRACKER | — | — | ✅ | ✅ |
| CR-N1 MESH | — | — | ✅ | ✅ |
| CR-N2 EDGE | — | — | ✅ | ✅ |
| CR-V1 MIRROR | — | — | ✅ | ✅ |
| CR-V2 GHOST | — | — | ✅ | ✅ |
| CR-V3 DOJO | — | — | ✅ | ✅ |
| CR-C1 ADVERSARY | — | — | ✅ | ✅ |
| CR-C2 SCENARIO FORGE | — | — | ✅ | ✅ |
| CR-D4 EXPORT (HLA) | — | — | — | ✅ |
| CR-N3 CLOUD | — | — | — | ✅ |
| CR-C3 PROPHECY | — | — | — | ✅ |
| Multi-range dashboard | — | — | — | ✅ |
| Cross-unit benchmarking | — | — | — | ✅ |
| Priority support | — | — | — | ✅ |

### 9.2 Revenue Model (3-Year Projection)

| Year | FREE Ranges | STD Ranges | PRO Ranges | ENT Ranges | Perpetual | Subscription | **Total** |
|------|------------|------------|------------|------------|-----------|-------------|-----------|
| Y1 | 15 | 8 | 2 | 0 | $160K | $34K | **$194K** |
| Y2 | 30 | 20 | 8 | 3 | $410K | $159K | **$569K** |
| Y3 | 50 | 35 | 15 | 8 | $575K | $371K | **$946K** |
| **Total** | | | | | **$1,145K** | **$564K** | **$1,709K** |

**Note:** RANGE revenue alone is modest ($1.7M/3yr). The strategic value is:
- Activating the data flywheel (50+ ranges = 5M shots/month)
- Creating the upgrade path to BASE ($35-60K) and SHIELD ($60-120K)
- Generating the 9x CLV multiplier ($18K → $163K per customer)

---

## STEP 10: RISK ANALYSIS (RANGE-Specific)

| # | Risk | Severity | Likelihood | Mitigation |
|---|------|----------|------------|------------|
| R1 | VN-LOMAH integration harder than expected | Medium | Medium | LOMAH protocol already documented; Workshop X team available |
| R2 | AI technique analysis insufficient accuracy | High | Medium | Start with rules-based; add ML when 10K+ annotated shots available |
| R3 | Range officers resist digital transition | Medium | High | FREE tier removes cost barrier; deploy alongside paper (not replace) |
| R4 | Vietnamese internet insufficient for cloud | Low | Medium | Edge-first architecture; works fully offline; sync when connected |
| R5 | Cybersecurity concerns delay military adoption | Medium | Medium | Air-gapped option; simple architecture; no classified data in V1 |
| R6 | Cubic responds with affordable offering | Low | Low | Market window 2-3 years; Cubic's cost structure prevents $15K product |
| R7 | Developer capacity insufficient | High | High | Phase 1 needs only 2 devs; Python/React = largest talent pool |
| R8 | CDM schema design flawed | Medium | Medium | Open-source early; community feedback; versioned schema |

---

## Cross-References

- [[CORTEX_C2_ODI_Analysis.md]] — 25 Training outcomes (T01-T25)
- [[CORTEX_RANGE_product_portfolio_musk.md]] — Musk first principles analysis
- [[RE_cubic_training_systems.md]] — Cubic competitive analysis
- [[RE_cubic_lvc_integration.md]] — Cubic LVC architecture deep dive
- [[00_project_brief.md]] — CORTEX C2 platform brief
- [[phase0_synthesis.md]] — Phase 0 gate review (all editions)
