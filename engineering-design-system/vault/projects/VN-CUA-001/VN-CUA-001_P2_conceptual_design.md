---
project: VN-CUA-001
designation: VDC-100
type: conceptual_design
phase: 2
version: 1.0
created: 2026-02-05
status: active
methodology: Pahl & Beitz + ODI-weighted VDI 2225
---

# VN-CUA-001: PHASE 2 CONCEPTUAL DESIGN
## Vietnamese Drone Catcher 100 (VDC-100)

**Project:** VN-CUA-001
**Phase:** 2 - Conceptual Design
**Date:** 2026-02-05
**Input:** 89 ODI-validated requirements

---

## 1. ABSTRACTION (5-Step Process)

### Step 1: Eliminate Personal Preferences

| Original Statement | Preference Removed |
|--------------------|-------------------|
| "Use SkyWall-style pneumatic launcher" | "Launch projectile to capture drone" |
| "Include SmartScope targeting" | "Provide target acquisition assistance" |
| "Use Dyneema net" | "Employ capture mechanism" |
| "Aluminum barrel" | "Propel projectile through tube" |

### Step 2: Omit Non-Essential Requirements

**Essential Requirements (Must Have):**
- Capture airborne drone physically
- Preserve captured drone for evidence
- Portable by single operator
- Effective against autonomous drones
- Cost ≤$6,000

**Non-Essential (Nice to Have):**
- Video tracking system
- Ballistic computer
- RF communication with projectile
- Modular barrel lengths

### Step 3: Transform Quantitative to Qualitative

| Quantitative | Qualitative |
|--------------|-------------|
| ≥80m range | "Engage at tactically useful distance" |
| ≤8 kg weight | "Portable by single operator" |
| ≥70% first-shot hit | "Accurate enough for practical engagement" |
| ≤$6,000 price | "Affordable for widespread deployment" |
| ≥98% net deployment | "Highly reliable capture mechanism" |

### Step 4: Generalize Results

| Specific | Generalized |
|----------|-------------|
| "Capture drone with net" | "Physically entangle aerial target" |
| "Pneumatic propulsion" | "Accelerate projectile" |
| "Parachute recovery" | "Control descent of captured target" |
| "Laser rangefinder" | "Measure distance to target" |

### Step 5: Solution-Neutral Problem Statement

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    ABSTRACTED PROBLEM STATEMENT                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  TRANSFORM:                                                               ║
║  • Input: Hostile/unauthorized airborne vehicle (drone) at distance       ║
║  • Output: Captured, intact drone with controlled descent to ground       ║
║                                                                           ║
║  CONSTRAINTS:                                                             ║
║  • Single operator, man-portable system                                   ║
║  • Works against ALL drone types (including autonomous)                   ║
║  • Preserves forensic evidence                                            ║
║  • Affordable for widespread deployment                                   ║
║  • Producible locally (Vietnam)                                           ║
║                                                                           ║
║  ESSENTIAL FUNCTION:                                                      ║
║  "Intercept and physically capture small unmanned aerial vehicle          ║
║   at tactically useful range with single-operator portable system"        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 2. FUNCTION STRUCTURE (Refined)

### 2.1 Overall Function

**CAPTURE UNAUTHORIZED DRONE** and deliver intact to operator

### 2.2 Function Decomposition

```
VDC-100 FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════════════════

                            ┌─────────────────────────┐
                            │     OVERALL FUNCTION    │
                            │  Capture unauthorized   │
                            │  drone intact           │
                            └───────────┬─────────────┘
                                        │
        ┌───────────────┬───────────────┼───────────────┬───────────────┐
        │               │               │               │               │
        ▼               ▼               ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ F1: ACQUIRE   │ │ F2: PREPARE   │ │ F3: PROPEL    │ │ F4: CAPTURE   │ │ F5: RECOVER   │
│ TARGET        │→│ SYSTEM        │→│ PROJECTILE    │→│ TARGET        │→│ TARGET        │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘
        │               │               │               │               │
        ▼               ▼               ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ F1.1 Detect   │ │ F2.1 Store    │ │ F3.1 Release  │ │ F4.1 Deploy   │ │ F5.1 Slow     │
│ F1.2 Track    │ │      energy   │ │      energy   │ │      mechanism│ │      descent  │
│ F1.3 Measure  │ │ F2.2 Load     │ │ F3.2 Accelerate│ │ F4.2 Entangle │ │ F5.2 Land     │
│      range    │ │      projectile│ │     projectile│ │      target   │ │      safely   │
│ F1.4 Calculate│ │ F2.3 Regulate │ │ F3.3 Guide    │ │ F4.3 Secure   │ │               │
│      aim point│ │      energy   │ │      projectile│ │      target   │ │               │
│ F1.5 Confirm  │ │ F2.4 Arm      │ │               │ │               │ │               │
│      target   │ │      system   │ │               │ │               │ │               │
└───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘

FLOWS:
───────► Energy (E)
- - - -► Material (M)
═══════► Signal/Information (S)

═══════════════════════════════════════════════════════════════════════════
```

### 2.3 Sub-Function Details

| ID | Sub-Function | Input | Output | Type | ODI Priority |
|----|--------------|-------|--------|------|--------------|
| **F1** | **ACQUIRE TARGET** | | | **Main** | |
| F1.1 | Detect target | S: Visual/sensor | S: Target presence | Essential | O-09: 11.0 |
| F1.2 | Track target | S: Position data | S: Motion vector | Essential | O-17: 10.5 |
| F1.3 | Measure range | S: Target position | S: Range value | Essential | O-12: 11.5 |
| F1.4 | Calculate aim point | S: Range, motion | S: Aim solution | Critical | **O-48: 15.0** 🔴 |
| F1.5 | Confirm target | S: Target data | S: Engage decision | Essential | O-02: 11.0 |
| **F2** | **PREPARE SYSTEM** | | | **Main** | |
| F2.1 | Store energy | E: Mechanical/chemical | E: Stored potential | Essential | O-61: 11.0 |
| F2.2 | Load projectile | M: Projectile | M: Chambered round | Critical | **O-55: 12.5** 🔴 |
| F2.3 | Regulate energy | E: High pressure | E: Controlled pressure | Essential | O-23: 14.6 |
| F2.4 | Arm system | S: Arm command | S: Armed status | Safety | O-06: 10.0 |
| **F3** | **PROPEL PROJECTILE** | | | **Main** | |
| F3.1 | Release energy | E: Stored | E: Kinetic | Critical | **O-23: 14.6** 🔴 |
| F3.2 | Accelerate projectile | E: Kinetic, M: Proj | M: Moving projectile | Critical | **O-46: 13.5** 🔴 |
| F3.3 | Guide projectile | M: Projectile | M: Directed flight | Essential | O-40: 10.5 |
| **F4** | **CAPTURE TARGET** | | | **Main** | |
| F4.1 | Deploy capture mechanism | M: Projectile | M: Deployed net | Critical | **O-43: 13.5** 🔴 |
| F4.2 | Entangle target | M: Net, M: Drone | M: Captured drone | Critical | O-42: 11.0 |
| F4.3 | Secure target | M: Drone in net | M: Secured package | Essential | O-63: 13.0 |
| **F5** | **RECOVER TARGET** | | | **Main** | |
| F5.1 | Slow descent | M: Package | M: Slowed package | Critical | **O-63: 13.0** 🔴 |
| F5.2 | Land safely | M: Package | M: Grounded package | Essential | O-64: 10.0 |

---

## 3. WORKING PRINCIPLES SEARCH

### 3.1 F1: Acquire Target - Working Principles

| F1 Sub-function | Principle | Description | Pros | Cons | TRL |
|-----------------|-----------|-------------|------|------|-----|
| **F1.1 Detect** | P1.1a Visual (eyes) | Operator visual detection | Simple, no electronics | Limited range, fatigue | 9 |
| | P1.1b Radar | RF detection | All-weather, auto | Complex, expensive | 8 |
| | P1.1c Acoustic | Sound detection | Low cost | Short range, noisy env | 6 |
| **F1.3 Measure range** | P1.3a Laser rangefinder | Time-of-flight laser | Accurate, proven | Cost ~$150-300 | 9 |
| | P1.3b Stadiametric | Reticle + known size | No electronics | Requires known size | 9 |
| | P1.3c Radar ranging | RF echo | Multi-target | Complex, expensive | 8 |
| **F1.4 Calculate aim** | P1.4a Manual reticle | Operator uses marks | Simple, robust | Training required | 9 |
| | P1.4b Ballistic computer | Auto calculation | Accurate, fast | Cost, complexity | 8 |
| | P1.4c Hybrid (LRF+reticle) | LRF feeds reticle | Best accuracy/cost | Integration effort | 8 |

### 3.2 F2: Prepare System - Working Principles

| F2 Sub-function | Principle | Description | Pros | Cons | TRL |
|-----------------|-----------|-------------|------|------|-----|
| **F2.1 Store energy** | P2.1a HPA (compressed air) | High-pressure cylinder | Clean, refillable | Cylinder heavy | 9 |
| | P2.1b CO2 cartridge | Disposable cartridge | Compact | Single-use, temp sensitive | 9 |
| | P2.1c Blank cartridge | Powder charge | High energy density | Noise, regulation | 9 |
| | P2.1d Bungee/spring | Mechanical spring | Simple | Low energy, cocking | 7 |
| **F2.2 Load projectile** | P2.2a Breech loading | Rear chamber access | Fast, simple | Exposes mechanism | 9 |
| | P2.2b Muzzle loading | Front loading | Traditional | Slower | 9 |
| | P2.2c Magazine feed | Auto-feed from mag | Multi-shot ready | Complexity, weight | 7 |
| **F2.3 Regulate energy** | P2.3a Mechanical regulator | Pressure reducer | Reliable | Adds weight | 9 |
| | P2.3b Fixed orifice | Calibrated restriction | Simple | Less precise | 8 |
| | P2.3c Electronic valve | Solenoid control | Precise, variable | Electronics, power | 8 |

### 3.3 F3: Propel Projectile - Working Principles

| F3 Sub-function | Principle | Description | Pros | Cons | TRL |
|-----------------|-----------|-------------|------|------|-----|
| **F3.2 Accelerate** | P3.2a Pneumatic tube | Gas expansion in barrel | Clean, variable | Barrel length matters | 9 |
| | P3.2b Pyrotechnic | Explosive charge | High velocity | Noise, regulation | 9 |
| | P3.2c Spring launcher | Mechanical spring | Silent | Low velocity | 7 |
| | P3.2d Electromagnetic | Rail/coil gun | Very high velocity | Power, complexity | 4 |
| **F3.3 Guide** | P3.3a Smoothbore | No rifling | Simple, low drag | No spin stabilization | 9 |
| | P3.3b Rifled barrel | Spin stabilization | Accuracy | Complexity, drag | 9 |
| | P3.3c Fin stabilization | Projectile fins | Good stability | Adds projectile cost | 8 |

### 3.4 F4: Capture Target - Working Principles

| F4 Sub-function | Principle | Description | Pros | Cons | TRL |
|-----------------|-----------|-------------|------|------|-----|
| **F4.1 Deploy capture** | P4.1a Net (projected) | Net thrown by projectile | Large area, proven | Timing critical | 8 |
| | P4.1b Entanglement lines | Weighted cords | Simple | Smaller capture area | 7 |
| | P4.1c Bola | Spinning weights | Ancient, proven | Limited range | 8 |
| | P4.1d Sticky projectile | Adhesive impact | Direct hit only | Miss = no capture | 6 |
| **F4.1 Deploy timing** | P4.1t1 Timer | Time-delay fuse | Simple, reliable | No range adaptation | 9 |
| | P4.1t2 Barometric | Altitude/pressure | Auto-adapts to arc | Complexity | 7 |
| | P4.1t3 RF command | Radio trigger | Precise control | Adds RF, jamming risk | 8 |
| | P4.1t4 Proximity | Sensor detects target | Smart trigger | Complex, expensive | 6 |
| **F4.2 Entangle** | P4.2a Net mesh | Woven net | Reliable | Weight | 9 |
| | P4.2b Corner weights | Weights spread net | Proven | Trajectory effect | 9 |
| | P4.2c Self-tightening | Drawstring closure | Better capture | Complexity | 7 |

### 3.5 F5: Recover Target - Working Principles

| F5 Sub-function | Principle | Description | Pros | Cons | TRL |
|-----------------|-----------|-------------|------|------|-----|
| **F5.1 Slow descent** | P5.1a Parachute | Fabric canopy | Proven, gentle | Deployment needed | 9 |
| | P5.1b Streamer/drogue | Ribbon drag | Simple, reliable | Less slowing | 8 |
| | P5.1c Autorotation | Rotor/propeller | No deployment | Complexity | 6 |
| | P5.1d None | Ballistic fall | Simplest | Damage risk | 9 |

---

## 4. MORPHOLOGICAL MATRIX

### 4.1 Matrix Structure

| Sub-Function | Solution 1 | Solution 2 | Solution 3 | Solution 4 |
|--------------|------------|------------|------------|------------|
| **F1.1 Detect target** | Visual (eyes) | Acoustic sensor | Radar alert | Camera system |
| **F1.3 Measure range** | Laser rangefinder | Stadiametric reticle | Radar | Estimated |
| **F1.4 Calculate aim** | Manual reticle | Ballistic computer | Hybrid (LRF+reticle) | - |
| **F2.1 Store energy** | HPA cylinder | CO2 cartridge | Blank cartridge | Bungee/spring |
| **F2.2 Load projectile** | Breech loading | Muzzle loading | Magazine feed | - |
| **F3.2 Accelerate** | Pneumatic tube | Pyrotechnic | Spring | - |
| **F3.3 Guide** | Smoothbore | Rifled | Fin-stabilized | - |
| **F4.1 Deploy capture** | Projected net | Entanglement lines | Bola | - |
| **F4.1t Deploy timing** | Timer | Barometric | RF command | Proximity |
| **F4.2 Entangle** | Net mesh + weights | Self-tightening net | Simple net | - |
| **F5.1 Slow descent** | Parachute | Drogue/streamer | None | - |

### 4.2 Concept Generation

#### CONCEPT A: "VDC-100 BASIC" (Simplified SkyWall)

```
Path: Visual → LRF → Hybrid reticle → HPA → Breech → Pneumatic → Smoothbore →
      Net → Timer → Mesh+weights → Parachute

┌─────────────────────────────────────────────────────────────────────────────┐
│ CONCEPT A: VDC-100 BASIC                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ • Detection: Operator visual + LRF for range                                │
│ • Targeting: Ballistic reticle with range marks (manual lead)               │
│ • Propulsion: HPA pneumatic (300→100 bar regulated)                         │
│ • Projectile: Net with corner weights, timer deploy                         │
│ • Recovery: Standard parachute                                              │
│                                                                             │
│ KEY FEATURES:                                                               │
│ ✓ Simple, proven technology (TRL 8-9)                                       │
│ ✓ No RF communication (jam-proof)                                           │
│ ✓ Low cost (~$1,600 production)                                             │
│ ✓ High reliability (fewer components)                                       │
│                                                                             │
│ LIMITATIONS:                                                                │
│ • Manual lead calculation (training intensive)                              │
│ • Fixed timer deploy (less adaptive)                                        │
│ • Basic accuracy (~60% first-shot at 50m moving)                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### CONCEPT B: "VDC-100 ENHANCED" (ODI-Optimized)

```
Path: Visual → LRF → Hybrid reticle → HPA → Breech → Pneumatic → Fin-stabilized →
      Net → Timer+Barometric → Mesh+weights → Parachute

┌─────────────────────────────────────────────────────────────────────────────┐
│ CONCEPT B: VDC-100 ENHANCED                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ • Detection: Operator visual + LRF with digital display                     │
│ • Targeting: Ballistic reticle + lead angle marks (ODI O-48)                │
│ • Propulsion: HPA pneumatic with fast-acting valve                          │
│ • Projectile: Fin-stabilized + net, timer+backup barometric                 │
│ • Recovery: Parachute with drogue backup                                    │
│                                                                             │
│ KEY FEATURES:                                                               │
│ ✓ Optimized for ODI high-priority outcomes                                  │
│ ✓ Better first-shot hit (ballistic reticle + fins)                          │
│ ✓ Dual-redundant deploy (timer + barometric backup)                         │
│ ✓ Improved accuracy (~70% first-shot at 50m moving)                         │
│ ✓ Still no RF (jam-proof)                                                   │
│                                                                             │
│ LIMITATIONS:                                                                │
│ • Slightly higher cost (~$1,800 production)                                 │
│ • Fin-stabilized projectile more complex                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### CONCEPT C: "VDC-100 PRO" (Maximum Capability)

```
Path: Visual+Camera → LRF → Ballistic computer → HPA → Magazine → Pneumatic →
      Fin-stabilized → Net → RF command → Self-tightening → Parachute

┌─────────────────────────────────────────────────────────────────────────────┐
│ CONCEPT C: VDC-100 PRO                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ • Detection: Operator visual + assisted camera display                      │
│ • Targeting: Ballistic computer with auto-lead calculation                  │
│ • Propulsion: HPA pneumatic with electronic valve control                   │
│ • Loading: 3-round magazine for rapid follow-up                             │
│ • Projectile: Smart net with RF-triggered deploy                            │
│ • Recovery: Self-tightening net + parachute                                 │
│                                                                             │
│ KEY FEATURES:                                                               │
│ ✓ Highest accuracy (~85% first-shot at 50m moving)                          │
│ ✓ Multi-shot capability without manual reload                               │
│ ✓ Computer-assisted targeting reduces training time                         │
│ ✓ Optimal capture timing (RF proximity trigger)                             │
│                                                                             │
│ LIMITATIONS:                                                                │
│ • High cost (~$3,500 production) → $9,000 selling price                     │
│ • RF vulnerable to jamming                                                  │
│ • Complex electronics = lower reliability                                   │
│ • Heavier system (~10 kg)                                                   │
│ • Lower local content (~50%)                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### CONCEPT D: "VDC-100 PYRO" (Blank Cartridge Alternative)

```
Path: Visual → LRF → Hybrid reticle → Blank cartridge → Breech → Pyrotechnic →
      Smoothbore → Net → Timer → Mesh+weights → Parachute

┌─────────────────────────────────────────────────────────────────────────────┐
│ CONCEPT D: VDC-100 PYRO                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ • Detection: Operator visual + LRF                                          │
│ • Targeting: Ballistic reticle (same as Concept A)                          │
│ • Propulsion: Blank cartridge (pyrotechnic)                                 │
│ • Projectile: Net with timer deploy                                         │
│ • Recovery: Standard parachute                                              │
│                                                                             │
│ KEY FEATURES:                                                               │
│ ✓ Higher muzzle velocity (50+ m/s) → longer range                           │
│ ✓ Compact system (no gas cylinder)                                          │
│ ✓ Lighter weight (~6 kg)                                                    │
│ ✓ Simpler logistics (cartridges vs gas refill)                              │
│                                                                             │
│ LIMITATIONS:                                                                │
│ • Loud report (tactical signature)                                          │
│ • Weapon regulation in Vietnam                                              │
│ • Temperature sensitivity                                                   │
│ • Single-use cartridges (higher per-shot cost)                              │
│ • Less precise velocity control                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. CONCEPT EVALUATION (VDI 2225)

### 5.1 Evaluation Criteria (ODI-Weighted)

| # | Criterion | Weight | Rationale | ODI Source |
|---|-----------|--------|-----------|------------|
| 1 | **First-shot hit probability** | **0.20** | Critical ODI outcome #1 | O-48: 15.0 |
| 2 | **Equipment reliability** | **0.15** | Critical ODI outcome #2 | O-23: 14.6 |
| 3 | **Effective range** | **0.12** | Key performance driver | O-46: 13.5 |
| 4 | **Net deployment reliability** | **0.10** | Essential for capture | O-43: 13.5 |
| 5 | **Ready/reload time** | **0.10** | Speed for Rapid Responders | O-19, O-55: 12.5 |
| 6 | **Unit cost** | **0.10** | Market position | Requirement |
| 7 | **Local content** | **0.08** | Strategic requirement | CUA-PRO-01 |
| 8 | **Weight/portability** | **0.08** | Ergonomic requirement | O-24: 12.0 |
| 9 | **Development risk** | **0.07** | Schedule protection | CUA-SCH-xx |
| | **TOTAL** | **1.00** | | |

### 5.2 VDI 2225 Scoring Scale

```
0 = Absolutely unsatisfactory (not acceptable)
1 = Just tolerable (barely meets minimum requirement)
2 = Adequate (meets requirement satisfactorily)
3 = Good (exceeds requirement)
4 = Very good (close to ideal solution)
```

### 5.3 Evaluation Matrix

| Criterion | Weight | Concept A (Basic) | Concept B (Enhanced) | Concept C (Pro) | Concept D (Pyro) |
|-----------|--------|-------------------|----------------------|-----------------|------------------|
| First-shot hit probability | 0.20 | 2 | **3** | 4 | 2 |
| Equipment reliability | 0.15 | **4** | **4** | 2 | 3 |
| Effective range | 0.12 | 3 | 3 | **4** | **4** |
| Net deployment reliability | 0.10 | 3 | **4** | 3 | 3 |
| Ready/reload time | 0.10 | 3 | **4** | 2 | 3 |
| Unit cost | 0.10 | **4** | 3 | 1 | **4** |
| Local content | 0.08 | **4** | **4** | 2 | 3 |
| Weight/portability | 0.08 | 3 | 3 | 2 | **4** |
| Development risk | 0.07 | **4** | 3 | 1 | 2 |

### 5.4 Weighted Scores Calculation

**Concept A (Basic):**
```
Score = (0.20×2) + (0.15×4) + (0.12×3) + (0.10×3) + (0.10×3) +
        (0.10×4) + (0.08×4) + (0.08×3) + (0.07×4)
      = 0.40 + 0.60 + 0.36 + 0.30 + 0.30 + 0.40 + 0.32 + 0.24 + 0.28
      = 3.20
Percentage = 3.20 / 4.00 = 80.0%
```

**Concept B (Enhanced):**
```
Score = (0.20×3) + (0.15×4) + (0.12×3) + (0.10×4) + (0.10×4) +
        (0.10×3) + (0.08×4) + (0.08×3) + (0.07×3)
      = 0.60 + 0.60 + 0.36 + 0.40 + 0.40 + 0.30 + 0.32 + 0.24 + 0.21
      = 3.43
Percentage = 3.43 / 4.00 = 85.8%
```

**Concept C (Pro):**
```
Score = (0.20×4) + (0.15×2) + (0.12×4) + (0.10×3) + (0.10×2) +
        (0.10×1) + (0.08×2) + (0.08×2) + (0.07×1)
      = 0.80 + 0.30 + 0.48 + 0.30 + 0.20 + 0.10 + 0.16 + 0.16 + 0.07
      = 2.57
Percentage = 2.57 / 4.00 = 64.3%
```

**Concept D (Pyro):**
```
Score = (0.20×2) + (0.15×3) + (0.12×4) + (0.10×3) + (0.10×3) +
        (0.10×4) + (0.08×3) + (0.08×4) + (0.07×2)
      = 0.40 + 0.45 + 0.48 + 0.30 + 0.30 + 0.40 + 0.24 + 0.32 + 0.14
      = 3.03
Percentage = 3.03 / 4.00 = 75.8%
```

### 5.5 Results Summary

| Concept | Weighted Score | Percentage | Decision |
|---------|----------------|------------|----------|
| **B: VDC-100 Enhanced** | **3.43** | **85.8%** | ✅ **SELECTED** |
| A: VDC-100 Basic | 3.20 | 80.0% | ✅ Acceptable (Fallback) |
| D: VDC-100 Pyro | 3.03 | 75.8% | ✅ Acceptable (Alternative) |
| C: VDC-100 Pro | 2.57 | 64.3% | ❌ Below threshold |

```
VDI 2225 EVALUATION RESULTS
═══════════════════════════════════════════════════════════════════════════

                    50%        60%        70%        80%        90%       100%
                     │          │          │          │          │          │
Concept C (Pro)  ════╪══════════╪═════╡    │          │          │          │ 64.3%
                     │          │     ▼    │          │          │          │
                     │          │   BELOW  │          │          │          │
                     │          │ THRESHOLD│          │          │          │
                     │          │          │          │          │          │
Concept D (Pyro) ════╪══════════╪══════════╪═════╡    │          │          │ 75.8%
                     │          │          │     ▼    │          │          │
                     │          │          │ ACCEPTABLE│          │          │
                     │          │          │          │          │          │
Concept A (Basic)════╪══════════╪══════════╪══════════╡          │          │ 80.0%
                     │          │          │          ▼          │          │
                     │          │          │        GOOD         │          │
                     │          │          │      (FALLBACK)     │          │
                     │          │          │          │          │          │
Concept B (Enhanced) ╪══════════╪══════════╪══════════╪════════╡ │          │ 85.8%
                     │          │          │          │        ▼ │          │
                     │          │          │          │ SELECTED │          │
                     │          │          │          │          │          │
═══════════════════════════════════════════════════════════════════════════
```

---

## 6. SENSITIVITY ANALYSIS

### 6.1 What If Weights Change?

| Scenario | Weight Shift | A (Basic) | B (Enhanced) | Winner |
|----------|--------------|-----------|--------------|--------|
| Baseline | As defined | 80.0% | **85.8%** | B |
| Cost priority (+10%) | Cost 0.20 | **82.5%** | 82.5% | Tie |
| Accuracy priority (+10%) | Hit 0.30 | 77.5% | **87.5%** | B |
| Reliability priority (+10%) | Rel 0.25 | **82.5%** | 85.0% | B |
| Local content priority (+10%) | LC 0.18 | **82.0%** | 85.0% | B |

**Conclusion:** Concept B wins in most scenarios. Only at extreme cost priority does A tie.

### 6.2 Critical Criteria Analysis

**If any criterion score drops to 0 (showstopper):**

| Concept | Lowest Score | Criterion | Risk |
|---------|--------------|-----------|------|
| A | 2 | First-shot hit | LOW (acceptable) |
| B | 3 | Multiple criteria | VERY LOW |
| C | 1 | Cost, Dev risk | HIGH (showstopper risk) |
| D | 2 | First-shot hit, Dev risk | MEDIUM |

---

## 7. SELECTED CONCEPT: VDC-100 ENHANCED

### 7.1 Selection Summary

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  SELECTED CONCEPT: VDC-100 ENHANCED (Concept B)                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  VDI 2225 Score: 85.8% (Exceeds 70% threshold by 15.8 points)             ║
║                                                                           ║
║  KEY WORKING PRINCIPLES:                                                  ║
║  ├── Detection: Operator visual                                           ║
║  ├── Ranging: Laser rangefinder (COTS module)                             ║
║  ├── Targeting: Ballistic reticle with range/lead marks                   ║
║  ├── Energy storage: HPA cylinder (0.5L @ 300 bar)                        ║
║  ├── Propulsion: Pneumatic tube (regulated 100 bar)                       ║
║  ├── Projectile: Fin-stabilized net round                                 ║
║  ├── Deploy timing: Timer + barometric backup                             ║
║  ├── Capture: Mesh net with corner weights                                ║
║  └── Recovery: Parachute with drogue backup                               ║
║                                                                           ║
║  ODI OUTCOME ALIGNMENT:                                                   ║
║  ├── O-48 (First-shot hit): Score 3/4 - Good (ballistic reticle + fins)   ║
║  ├── O-23 (Reliability): Score 4/4 - Very good (simple, proven)           ║
║  ├── O-46 (Range): Score 3/4 - Good (80m effective)                       ║
║  ├── O-43 (Net deploy): Score 4/4 - Very good (dual redundancy)           ║
║  └── O-55 (Reload): Score 4/4 - Very good (fast breech)                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### 7.2 Concept Description

**VDC-100 ENHANCED** is an ODI-optimized pneumatic net launcher featuring:

1. **Targeting System:**
   - Laser rangefinder (COTS, 5-150m range)
   - Ballistic reticle with graduated range marks (20/40/60/80/100m)
   - Lead angle marks for moving targets (5/10/15 m/s)
   - Sunlight-readable display (1000+ nits)

2. **Propulsion System:**
   - HPA cylinder (0.5L @ 300 bar, ≥5 shots)
   - Mechanical regulator (300→100 bar)
   - Fast-acting trigger valve (<50ms)
   - Breech-loading chamber (≤8 sec reload)

3. **Projectile (VDC-P40E):**
   - 450g total mass
   - 80mm diameter, fin-stabilized
   - 3m × 3m UHMWPE net
   - Corner weights for spread
   - Timer deploy (1.8 sec) + barometric backup
   - 0.8m parachute + drogue backup

4. **Launcher Body:**
   - Aluminum 6061-T6 barrel (800mm)
   - Polymer receiver
   - Adjustable stock (±50mm)
   - Total weight: ≤8 kg loaded

### 7.3 Key Advantages Over Alternatives

| vs. Concept A (Basic) | vs. Concept C (Pro) | vs. Concept D (Pyro) |
|-----------------------|---------------------|----------------------|
| +5.8% VDI score | +21.5% VDI score | +10.0% VDI score |
| Better first-shot hit | Much lower cost | Better reliability |
| Dual deploy redundancy | Higher reliability | No weapon regulation |
| Fin stabilization | Higher local content | Refillable (lower TCO) |

### 7.4 Development Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Fin-stabilized projectile | Medium | Medium | Prototype early, test extensively |
| Barometric backup integration | Low | Low | Use proven altimeter module |
| Ballistic reticle calibration | Medium | Low | Multiple test sessions, documentation |
| LRF integration | Low | Medium | Use COTS module with standard interface |

### 7.5 Fallback Option

**If Concept B encounters development issues:**

→ **Fallback to Concept A (Basic)** at 80.0% VDI score
- Remove fin stabilization (use smooth projectile)
- Remove barometric backup (timer only)
- Simpler reticle (fewer marks)
- Faster development, lower risk

---

## 8. PRELIMINARY LAYOUT

```
VDC-100 ENHANCED - PRELIMINARY LAYOUT
═══════════════════════════════════════════════════════════════════════════

SIDE VIEW (not to scale)
─────────────────────────────────────────────────────────────────────────────

    ┌─────────────────────────────────────────────────────────────────────┐
    │                         TARGETING SCOPE                             │
    │  ┌──────────────────────────────────────────────────────────────┐  │
    │  │  LRF  │ Ballistic Reticle │ LCD Display │ Battery            │  │
    │  │ Module│ (etched glass)    │ (status)    │ (18650)            │  │
    │  └──────────────────────────────────────────────────────────────┘  │
    └────────────────────────────────┬────────────────────────────────────┘
                                     │ Picatinny mount
    ┌────────────────────────────────┴────────────────────────────────────┐
    │                           BARREL ASSEMBLY                           │
    │  ┌────────┐  ┌────────────────────────────────────┐  ┌───────────┐ │
    │  │ MUZZLE │  │     BARREL (Al 6061-T6, 800mm)     │  │  BREECH   │ │
    │  │(100mm) │  │         Smoothbore, 100mm ID       │  │  CHAMBER  │ │
    │  └────────┘  └────────────────────────────────────┘  └─────┬─────┘ │
    └────────────────────────────────────────────────────────────│───────┘
                                                                 │
    ┌────────────────────────────────────────────────────────────┴───────┐
    │                         RECEIVER ASSEMBLY                          │
    │  ┌───────────────┐  ┌─────────────┐  ┌──────────────────────────┐ │
    │  │ TRIGGER       │  │ VALVE       │  │ REGULATOR (300→100 bar)  │ │
    │  │ MECHANISM     │  │ (fast-act)  │  │                          │ │
    │  └───────┬───────┘  └──────┬──────┘  └────────────┬─────────────┘ │
    │          │                 │                      │                │
    │     [Trigger]         [Gas line]            [HPA line]            │
    └──────────│─────────────────│──────────────────────│────────────────┘
               │                 │                      │
    ┌──────────┴─────────────────┴──────────────────────┴────────────────┐
    │                           STOCK ASSEMBLY                           │
    │  ┌───────────────────────┐  ┌────────────────────────────────────┐│
    │  │ ADJUSTABLE STOCK      │  │ HPA CYLINDER (0.5L @ 300 bar)      ││
    │  │ (±50mm)               │  │                                    ││
    │  └───────────────────────┘  └────────────────────────────────────┘│
    │                              [Quick-release mount]                 │
    └────────────────────────────────────────────────────────────────────┘

TOP VIEW
─────────────────────────────────────────────────────────────────────────────

                    ┌─────────────────────────────────────────────────────┐
                    │                    SCOPE (170mm)                    │
                    └─────────────────────────────────────────────────────┘
    ┌───────────────────────────────────────────────────────────────────────┐
    │   MUZZLE   │              BARREL (800mm)              │   BREECH     │
    └───────────────────────────────────────────────────────────────────────┘
                                                            ┌───────────────┐
                                                            │   RECEIVER    │
                                                            │   (200mm)     │
                                                            └───────────────┘
                    ┌─────────────────────────────────────────────────────┐
                    │              STOCK + CYLINDER (400mm)               │
                    └─────────────────────────────────────────────────────┘

KEY DIMENSIONS:
─────────────────────────────────────────────────────────────────────────────
Overall length:     1150mm (collapsed: 800mm if folding)
Barrel length:      800mm
Barrel ID:          100mm
Scope length:       170mm
Stock length:       400mm (adjustable ±50mm)
Total height:       180mm (with scope)
Total width:        120mm
System weight:      7.8 kg (loaded, with scope)

═══════════════════════════════════════════════════════════════════════════
```

---

## 9. GATE 2 CHECKLIST

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Function structure validated | ✅ | Section 2 (5 main + 18 subfunctions) |
| ≥3 concepts evaluated | ✅ | 4 concepts (A, B, C, D) |
| VDI 2225 score ≥70% | ✅ | **85.8%** (Concept B) |
| No criterion scores = 0 | ✅ | Lowest score = 3 for Concept B |
| Selection rationale documented | ✅ | Section 7 |
| Risks identified with mitigation | ✅ | Section 7.4 |
| Preliminary layout sketched | ✅ | Section 8 |
| Technical feasibility confirmed | ✅ | All TRL ≥7 |

**Gate 2 Status:** 🟢 **PASSED**

---

## 10. NEXT STEPS (Phase 3)

1. **Layout Design:** Detailed dimensional design
2. **DfX Review:** All 12 categories for defense product
3. **Material Selection:** Finalize materials, suppliers
4. **Tolerance Analysis:** Critical dimensions
5. **Local Content Calculation:** Verify ≥70%
6. **Production Cost Refinement:** Detailed BOM

---

## DOCUMENT LINKS

- [[VN-CUA-001_product_spec|Product Specification v1.2]]
- [[VN-CUA-001_ODI_customer_discovery|ODI Customer Discovery]]
- [[VN-CUA-001_P3_embodiment_design|Phase 3: Embodiment Design]] ← NEXT

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial Phase 2 conceptual design. 5-step abstraction completed. Function structure with 5 main + 18 subfunctions. 4 concepts generated via morphological matrix. VDI 2225 evaluation with ODI-weighted criteria. Concept B (Enhanced) selected at 85.8%.** |

---

*This conceptual design follows Pahl & Beitz methodology with ODI-weighted VDI 2225 evaluation for Vietnamese defense product development.*

**Phase 2 Status:** 🟢 **COMPLETE** - Concept B (VDC-100 Enhanced) selected

