---
project: VN-CUA-001
designation: VDC-100
type: function_structure
phase: 2
step: 2
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Step 2
---

# VN-CUA-001: FUNCTION STRUCTURE
## Vietnamese Drone Catcher 100 (VDC-100)
## Cấu trúc Chức năng - Giai đoạn 2, Bước 2

**Project Code:** VN-CUA-001
**Phase:** 2 - Conceptual Design (Step 2: Function Structure)
**Date:** 2026-02-08
**Input:** [[02_conceptual/abstraction|Abstracted Problem Statement]]

---

# 1. OVERALL FUNCTION

## 1.1 Black Box Definition

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           OVERALL FUNCTION (Black Box)                       ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  INPUTS                    ┌────────────────────┐              OUTPUTS       ║
║                            │                    │                            ║
║  ───Energy (E)──────────►  │   CAPTURE          │  ──►  Captured drone       ║
║    (stored energy)         │   UNAUTHORIZED     │       (intact, on ground)  ║
║                            │   DRONE            │                            ║
║  ───Material (M)────────►  │                    │  ──►  Spent projectile     ║
║    (projectile/ammo)       │   INTACT           │       (recoverable)        ║
║                            │                    │                            ║
║  ───Signal (S)──────────►  │                    │  ──►  Engagement data      ║
║    (target info,           │                    │       (range, hit/miss)     ║
║     operator command)      └────────────────────┘                            ║
║                                                                              ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## 1.2 Energy / Material / Signal Flow Summary

| Flow Type | Input | Through System | Output |
|-----------|-------|----------------|--------|
| **Energy (E)** | Stored potential (gas/spring/chemical) | Converted to kinetic → projectile flight | Heat (barrel friction), recoil |
| **Material (M)** | Projectile assembly (net + weights + chute) | Loaded → accelerated → deployed | Captured drone + spent round |
| **Signal (S)** | Target visual, range data, operator intent | Processed → aim solution → fire command | Hit/miss feedback, status display |

---

# 2. FUNCTION DECOMPOSITION

## 2.1 Main Functions (Level 1)

The overall function decomposes into **5 sequential main functions** representing the engagement timeline:

```
VDC-100 FUNCTION STRUCTURE — MAIN FUNCTIONS
═══════════════════════════════════════════════════════════════════════════════

              TIME ──────────────────────────────────────────────────►

                            ┌─────────────────────────┐
                            │     OVERALL FUNCTION    │
                            │  "Capture unauthorized  │
                            │   drone intact"         │
                            └───────────┬─────────────┘
                                        │
        ┌───────────────┬───────────────┼───────────────┬───────────────┐
        │               │               │               │               │
        ▼               ▼               ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ F1: ACQUIRE   │ │ F2: PREPARE   │ │ F3: PROPEL    │ │ F4: CAPTURE   │ │ F5: RECOVER   │
│ TARGET        │→│ SYSTEM        │→│ PROJECTILE    │→│ TARGET        │→│ TARGET        │
│               │ │               │ │               │ │               │ │               │
│ "Find & aim"  │ │ "Ready to     │ │ "Launch       │ │ "Entangle     │ │ "Bring to     │
│               │ │  fire"        │ │  projectile"  │ │  drone"       │ │  ground"      │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘
   ~5-15 sec         ~3-8 sec         ~0.05 sec         ~1-3 sec         ~5-30 sec

TOTAL ENGAGEMENT TIMELINE: ~15-60 seconds from detection to recovery

═══════════════════════════════════════════════════════════════════════════════
```

| Function | Duration | Critical ODI Outcome | Priority |
|----------|----------|---------------------|----------|
| F1: Acquire Target | 5-15 sec | O-48: First-shot hit (15.0) | **CRITICAL** |
| F2: Prepare System | 3-8 sec | O-55: Ready/reload speed (12.5) | HIGH |
| F3: Propel Projectile | ~50 ms | O-23: Reliability (14.6) | **CRITICAL** |
| F4: Capture Target | 1-3 sec | O-43: Net deployment (13.5) | **CRITICAL** |
| F5: Recover Target | 5-30 sec | O-63: Evidence preservation (13.0) | HIGH |

---

## 2.2 Sub-Functions (Level 2)

### F1: ACQUIRE TARGET — Sub-Function Decomposition

```
F1: ACQUIRE TARGET
├── F1.1 DETECT target        (S: visual/sensor → S: target presence)
│   └── Operator sees drone or receives external alert
├── F1.2 TRACK target         (S: position → S: motion vector)
│   └── Follow target movement, estimate speed and direction
├── F1.3 MEASURE range        (S: target position → S: range value)
│   └── Determine distance to target (critical for aim point)
├── F1.4 CALCULATE aim point  (S: range + motion → S: aim solution)
│   └── Combine range, speed, lead angle into single aim point
└── F1.5 CONFIRM target       (S: target data → S: engage/no-go)
    └── Verify target identity, check safe firing corridor
```

| Sub-Function | Input Flow | Output Flow | Type | ODI Outcome | Score |
|--------------|-----------|-------------|------|-------------|-------|
| F1.1 Detect target | S: Visual/sensor cue | S: Target presence confirmed | Signal | O-09: Minimize detection time | 11.0 |
| F1.2 Track target | S: Position data (continuous) | S: Motion vector (speed, heading) | Signal | O-17: Minimize tracking loss | 10.5 |
| F1.3 Measure range | S: Target position | S: Range value (meters) | Signal | O-12: Minimize range error | 11.5 |
| F1.4 Calculate aim point | S: Range + motion + ballistics | S: Aim solution (elevation, lead) | Signal | **O-48: Maximize first-shot hit** | **15.0** |
| F1.5 Confirm target | S: Target identity data | S: Engage decision (go/no-go) | Signal | O-02: Minimize ID error | 11.0 |

**Design Insight:** F1.4 (Calculate aim point) addresses the #1 ODI outcome (O-48: 15.0). This sub-function deserves the most design attention — any solution that automates or simplifies aim calculation will score highest.

---

### F2: PREPARE SYSTEM — Sub-Function Decomposition

```
F2: PREPARE SYSTEM
├── F2.1 STORE energy         (E: external source → E: stored potential)
│   └── Energy available for multiple shots
├── F2.2 LOAD projectile      (M: projectile → M: chambered round)
│   └── Insert projectile into firing position
├── F2.3 REGULATE energy      (E: high pressure → E: controlled pressure)
│   └── Deliver consistent, repeatable energy to projectile
└── F2.4 ARM system           (S: operator command → S: armed status)
    └── Remove safety, enable firing circuit
```

| Sub-Function | Input Flow | Output Flow | Type | ODI Outcome | Score |
|--------------|-----------|-------------|------|-------------|-------|
| F2.1 Store energy | E: External charge/fill | E: Stored potential energy | Energy | O-61: Minimize refill difficulty | 11.0 |
| F2.2 Load projectile | M: Projectile assembly | M: Chambered, ready to fire | Material | **O-55: Minimize reload time** | **12.5** |
| F2.3 Regulate energy | E: Raw stored energy | E: Metered, controlled energy | Energy | **O-23: Maximize consistency** | **14.6** |
| F2.4 Arm system | S: Operator arm command | S: System armed, ready to fire | Signal | O-06: Minimize arming time | 10.0 |

**Design Insight:** F2.3 (Regulate energy) is critical for shot-to-shot consistency — the #2 ODI outcome (O-23: 14.6). The regulator directly affects whether each shot hits the same point.

---

### F3: PROPEL PROJECTILE — Sub-Function Decomposition

```
F3: PROPEL PROJECTILE
├── F3.1 RELEASE energy       (E: stored → E: kinetic, via operator trigger)
│   └── Convert stored energy to projectile motion
├── F3.2 ACCELERATE projectile (E: kinetic + M: projectile → M: moving projectile)
│   └── Accelerate to target velocity within barrel/launch guide
└── F3.3 GUIDE projectile     (M: projectile in barrel → M: directed flight)
    └── Impart directional stability for accurate flight
```

| Sub-Function | Input Flow | Output Flow | Type | ODI Outcome | Score |
|--------------|-----------|-------------|------|-------------|-------|
| F3.1 Release energy | E: Stored potential, S: Trigger command | E: Kinetic energy | Energy | **O-23: Maximize reliability** | **14.6** |
| F3.2 Accelerate projectile | E: Kinetic, M: Projectile | M: Moving projectile at Vmuzzle | Material+Energy | **O-46: Maximize effective range** | **13.5** |
| F3.3 Guide projectile | M: Accelerated projectile | M: Stabilized projectile in flight | Material | O-40: Minimize dispersion | 10.5 |

**Design Insight:** F3.2 determines muzzle velocity which directly sets maximum range (O-46: 13.5). The acceleration mechanism is the core "engine" of the system.

---

### F4: CAPTURE TARGET — Sub-Function Decomposition

```
F4: CAPTURE TARGET
├── F4.1 DEPLOY capture mechanism  (M: projectile → M: deployed mechanism)
│   └── Open/expand capture device at correct time and location
├── F4.2 ENTANGLE target      (M: mechanism + M: drone → M: captured drone)
│   └── Physically wrap around and immobilize drone
└── F4.3 SECURE target        (M: loose capture → M: secured package)
    └── Prevent drone from escaping capture
```

| Sub-Function | Input Flow | Output Flow | Type | ODI Outcome | Score |
|--------------|-----------|-------------|------|-------------|-------|
| F4.1 Deploy mechanism | M: Compact projectile | M: Expanded capture device | Material | **O-43: Maximize deployment reliability** | **13.5** |
| F4.2 Entangle target | M: Deployed device + drone | M: Drone wrapped in mechanism | Material | O-42: Maximize entanglement | 11.0 |
| F4.3 Secure target | M: Entangled drone | M: Secured package (cannot escape) | Material | **O-63: Minimize evidence damage** | **13.0** |

**Design Insight:** F4.1 timing is critical — deploy too early and the net/mechanism is fully open before reaching the target (drag slows it); deploy too late and it hasn't opened enough. This is a key engineering challenge.

---

### F5: RECOVER TARGET — Sub-Function Decomposition

```
F5: RECOVER TARGET
├── F5.1 SLOW descent         (M: falling package → M: slowed package)
│   └── Reduce vertical velocity to safe landing speed
└── F5.2 LAND safely          (M: slowed package → M: grounded package)
    └── Impact at ≤5 m/s descent rate preserving drone integrity
```

| Sub-Function | Input Flow | Output Flow | Type | ODI Outcome | Score |
|--------------|-----------|-------------|------|-------------|-------|
| F5.1 Slow descent | M: Captured drone + mechanism (falling) | M: Slowed descent package | Material | **O-63: Minimize evidence damage** | **13.0** |
| F5.2 Land safely | M: Slowed package approaching ground | M: Drone on ground, intact | Material | O-64: Minimize landing damage | 10.0 |

**Design Insight:** F5 is the differentiator vs. RF jamming and kinetic kill approaches. If the drone is not recoverable intact, the entire evidence preservation value proposition collapses (Systems Analysis R3 loop).

---

# 3. COMPLETE FUNCTION FLOW DIAGRAM

```
VDC-100 COMPLETE FUNCTION STRUCTURE WITH FLOWS
═══════════════════════════════════════════════════════════════════════════════

LEGEND:  ──────► Energy (E)     - - - -► Material (M)     ═══════► Signal (S)

                                                 ═══S: Target═══
                                                 ║  detected    ║
                                                 ▼              ║
                ┌──────────────────────────────────────────┐    ║
     S: Visual  │              F1: ACQUIRE TARGET           │    ║
   ═══════════►│                                          │    ║
                │  F1.1 Detect ══► F1.2 Track ══► F1.3 Range│    ║
                │       ║              ║              ║      │    ║
     S: Range   │       ╚══════════════╩══════► F1.4 Aim ═══╩═══╗
   ◄═══════════│                              ║      │    ║   ║
                │                        F1.5 Confirm  │    ║   ║
                └──────────────────────────────────────────┘    ║
                                                                 ║
                                                    S: Aim solution
                                                                 ║
                ┌──────────────────────────────────────────┐    ║
     E: Fill    │              F2: PREPARE SYSTEM           │    ║
   ──────────►│                                          │    ║
                │  F2.1 Store ──► F2.3 Regulate            │    ║
     M: Proj    │       E           E                      │    ║
   - - - - - -►│  F2.2 Load                               │    ║
                │       M     F2.4 Arm ◄════════════════════╩════╝
                │              S: Armed                     │
                └──────────────────────────────────────────┘
                        │E              │M
                        ▼               ▼
                ┌──────────────────────────────────────────┐
     S: Trigger │              F3: PROPEL PROJECTILE        │
   ═══════════►│                                          │
                │  F3.1 Release ──► F3.2 Accelerate        │
                │       E──►E           E+M                │
                │                    F3.3 Guide ─ ─ ─►     │
                │                       M: Projectile      │
                └──────────────────────────────────────────┘
                                        │M (projectile in flight)
                                        ▼
                ┌──────────────────────────────────────────┐
                │              F4: CAPTURE TARGET           │
                │                                          │
                │  F4.1 Deploy - - -► F4.2 Entangle        │
                │       M                  M: drone+net    │
                │                    F4.3 Secure ─ ─ ─►    │
                │                       M: package         │
                └──────────────────────────────────────────┘
                                        │M (drone + mechanism falling)
                                        ▼
                ┌──────────────────────────────────────────┐
                │              F5: RECOVER TARGET           │
                │                                          │
                │  F5.1 Slow descent - -► F5.2 Land safely │
                │       M                      M           │
                │                                          │
                └──────────────────────────────────────────┘
                                        │M
                                        ▼
                              ┌──────────────────┐
                              │ OUTPUT: Captured  │
                              │ drone on ground,  │
                              │ intact, evidence  │
                              │ preserved         │
                              └──────────────────┘

═══════════════════════════════════════════════════════════════════════════════
```

---

# 4. SUB-FUNCTION SUMMARY TABLE

| ID | Sub-Function | Input | Output | Flow Type | ODI Score | Priority |
|----|-------------|-------|--------|-----------|-----------|----------|
| **F1** | **ACQUIRE TARGET** | | | | | |
| F1.1 | Detect target | S: Visual/sensor cue | S: Target presence | Signal | 11.0 | Essential |
| F1.2 | Track target | S: Position data | S: Motion vector | Signal | 10.5 | Essential |
| F1.3 | Measure range | S: Target position | S: Range value | Signal | 11.5 | Essential |
| F1.4 | Calculate aim point | S: Range, motion, ballistics | S: Aim solution | Signal | **15.0** | **CRITICAL** |
| F1.5 | Confirm target | S: Target data | S: Engage decision | Signal | 11.0 | Essential |
| **F2** | **PREPARE SYSTEM** | | | | | |
| F2.1 | Store energy | E: External charge | E: Stored potential | Energy | 11.0 | Essential |
| F2.2 | Load projectile | M: Projectile assembly | M: Chambered round | Material | **12.5** | Critical |
| F2.3 | Regulate energy | E: Raw stored energy | E: Metered energy | Energy | **14.6** | **CRITICAL** |
| F2.4 | Arm system | S: Arm command | S: Armed status | Signal | 10.0 | Safety |
| **F3** | **PROPEL PROJECTILE** | | | | | |
| F3.1 | Release energy | E: Stored, S: Trigger | E: Kinetic | Energy | **14.6** | **CRITICAL** |
| F3.2 | Accelerate projectile | E: Kinetic, M: Projectile | M: Moving projectile | Material+Energy | **13.5** | **CRITICAL** |
| F3.3 | Guide projectile | M: Accelerated projectile | M: Stabilized flight | Material | 10.5 | Essential |
| **F4** | **CAPTURE TARGET** | | | | | |
| F4.1 | Deploy capture mechanism | M: Compact projectile | M: Deployed mechanism | Material | **13.5** | **CRITICAL** |
| F4.2 | Entangle target | M: Mechanism + drone | M: Captured drone | Material | 11.0 | Essential |
| F4.3 | Secure target | M: Entangled drone | M: Secured package | Material | **13.0** | Critical |
| **F5** | **RECOVER TARGET** | | | | | |
| F5.1 | Slow descent | M: Falling package | M: Slowed package | Material | **13.0** | Critical |
| F5.2 | Land safely | M: Slowed package | M: Grounded drone | Material | 10.0 | Essential |

**Total: 5 main functions + 18 sub-functions = 23 function elements**

---

# 5. ODI PRIORITY MAPPING

Ranking sub-functions by ODI opportunity score to focus design effort:

```
ODI PRIORITY RANKING — SUB-FUNCTIONS
═══════════════════════════════════════════════════════════════════════════════

SCORE   SUB-FUNCTION                           DESIGN FOCUS
─────   ──────────────────────────────────────  ────────────────────────────
15.0    F1.4 Calculate aim point       ████████████████████████████  TOP PRIORITY
14.6    F2.3 Regulate energy           ███████████████████████████   HIGH — consistency
14.6    F3.1 Release energy            ███████████████████████████   HIGH — reliability
13.5    F3.2 Accelerate projectile     ██████████████████████████    HIGH — range
13.5    F4.1 Deploy capture mechanism  ██████████████████████████    HIGH — net open
13.0    F4.3 Secure target             █████████████████████████     MEDIUM-HIGH
13.0    F5.1 Slow descent              █████████████████████████     MEDIUM-HIGH
12.5    F2.2 Load projectile           ████████████████████████      MEDIUM-HIGH
─────   ────────────────── THRESHOLD ─────────────────────────────────────
11.5    F1.3 Measure range             ██████████████████████        MEDIUM
11.0    F1.1 Detect target             █████████████████████         MEDIUM
11.0    F1.5 Confirm target            █████████████████████         MEDIUM
11.0    F2.1 Store energy              █████████████████████         MEDIUM
11.0    F4.2 Entangle target           █████████████████████         MEDIUM
10.5    F1.2 Track target              ████████████████████          STANDARD
10.5    F3.3 Guide projectile          ████████████████████          STANDARD
10.0    F2.4 Arm system                ███████████████████           STANDARD
10.0    F5.2 Land safely               ███████████████████           STANDARD

═══════════════════════════════════════════════════════════════════════════════

TOP 8 sub-functions (score ≥12.5) = 44% of functions, drive ~80% of customer value
```

---

# 6. INTERFACE DEFINITIONS

Key interfaces between main functions that constrain concept generation:

| Interface | Between | Flow | Critical Parameter | Constraint |
|-----------|---------|------|-------------------|------------|
| **I-01** | F1→F2 | S: Aim solution | Range value accuracy | ±2m at 80m required |
| **I-02** | F2→F3 | E: Regulated pressure | Consistent energy delivery | ±5% shot-to-shot |
| **I-03** | F2→F3 | M: Chambered projectile | Projectile position | Centered, no tilt |
| **I-04** | F3→F4 | M: Flying projectile | Velocity at deploy point | ≥20 m/s for net spread |
| **I-05** | F3→F4 | S: Time-of-flight | Deploy timing signal | ±0.1 sec accuracy |
| **I-06** | F4→F5 | M: Drone+net package | Package mass | 1-26 kg (drone dependent) |
| **I-07** | F4→F5 | E: Kinetic (falling) | Descent initiation | Chute must deploy within 0.5 sec |

**Design Rule:** Interfaces I-02 (pressure consistency) and I-05 (deploy timing) are the most critical — they directly affect the two highest ODI outcomes.

---

# 7. FUNCTION STRUCTURE VALIDATION

| Validation Criterion | Status | Evidence |
|---------------------|--------|----------|
| All essential requirements covered? | ✅ | 7 essential reqs from abstraction mapped to functions |
| Complete E/M/S flow through system? | ✅ | Energy: E→F2→F3. Material: M→F2→F3→F4→F5. Signal: S→F1→F2→F3 |
| No missing sub-functions? | ✅ | 18 sub-functions cover complete engagement cycle |
| No orphan functions (unconnected)? | ✅ | All functions have input and output connections |
| ODI outcomes traceable? | ✅ | All 10 top-scoring ODI outcomes mapped to sub-functions |
| Interfaces defined? | ✅ | 7 critical interfaces identified with parameters |

---

# DOCUMENT LINKS

- [[02_conceptual/abstraction|Abstraction (Step 1)]]
- [[02_conceptual/morphological_matrix|Morphological Matrix (Steps 3-4)]] ← NEXT
- [[01_requirements/requirements_list|Requirements List]]
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]
- [[VN-CUA-001_Systems_Analysis|Systems Analysis]]

---

*This function structure follows Pahl & Beitz Step 2 of Conceptual Design, decomposing the overall function into 5 main + 18 sub-functions with complete energy/material/signal flow analysis and ODI priority mapping.*
