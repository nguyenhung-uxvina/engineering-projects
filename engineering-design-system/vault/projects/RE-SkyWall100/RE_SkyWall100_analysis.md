---
project: RE-SkyWall100
type: reverse_engineering
system: SkyWall 100 / SkyWall Patrol
origin: United Kingdom
manufacturer: OpenWorks Engineering
phase: reconnaissance
version: 1.0
created: 2026-02-05
status: in_progress
analyst: Engineering Team
---

# REVERSE ENGINEERING ANALYSIS
## SkyWall 100 / SkyWall Patrol Counter-Drone System

**System Designation:** SkyWall 100 (now SkyWall Patrol)
**Origin:** United Kingdom
**Manufacturer:** OpenWorks Engineering Ltd (Northumberland, UK)
**System Type:** Man-Portable Kinetic Counter-UAS (C-UAS)
**Analysis Date:** 2026-02-05

---

## 1. SYSTEM IDENTIFICATION

### 1.1 Basic Information

| Parameter | Value | Confidence |
|-----------|-------|------------|
| **Designation** | SkyWall 100 / SkyWall Patrol | High |
| **Manufacturer** | OpenWorks Engineering | High |
| **Country** | United Kingdom | High |
| **First Announced** | March 2016 | High |
| **System Category** | Kinetic C-UAS, Net Capture | High |
| **Operator** | Single soldier, shoulder-fired | High |

### 1.2 System Context

```
SUPERSYSTEM: Base/Site Defense System
            │
            ├── Detection Layer (Radar, RF sensors, cameras)
            │
            ├── Tracking & ID Layer (AI classification)
            │
            └── Defeat Layer ─────────────────────────────────
                    │
                    ├── Electronic (RF jamming, GPS spoofing)
                    │
                    └── KINETIC ◄──── SkyWall 100 (YOU ARE HERE)
                          │
                          ├── Directed Energy (laser)
                          ├── Projectile (shotgun, rifle)
                          └── Net Capture (SkyWall)

SIBLING SYSTEMS (Kinetic C-UAS):
├── DroneShield DroneGun
├── Battelle DroneDefender
├── SkyNet (Chinese net launcher)
├── DroneCatcher (Delft Dynamics)
└── Excipio (Theiss UAV Solutions)
```

### 1.3 Operational Deployment

| Deployment | Context | Users |
|------------|---------|-------|
| VIP Protection | US Presidential visits | Secret Service |
| Event Security | Major sporting events | UK Police |
| Critical Infrastructure | Airports, power plants | Security contractors |
| Military | Force protection | NATO forces |
| Mobile Patrol | Vehicle-mounted variant | Military/LEO |

---

## 2. PHASE 1: RECONNAISSANCE (DIAGNOSIS)

### 2.1 Level 1 - External Observation (OSINT)

#### 2.1.1 Physical Characteristics

| Parameter | Value | Source | Confidence |
|-----------|-------|--------|------------|
| **System Weight** | ~10 kg (22 lbs) | DSIAC, Engadget | High |
| **Configuration** | Shoulder-mounted launcher | Photos/video | High |
| **Length** | ~1.2-1.5m (estimated) | Photos | Medium |
| **Diameter** | ~100-120mm barrel | Photos | Medium |
| **Power Source** | Compressed gas cylinder | Manufacturer | High |
| **Operating Pressure** | ~200-300 bar (estimated) | Pneumatic analysis | Low |

#### 2.1.2 External Components Identified

```
SKYWALL 100 - EXTERNAL COMPONENT MAP
═══════════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────────────────┐
                    │                SMARTSCOPE UNIT                       │
                    │  ┌─────────┐ ┌─────────┐ ┌─────────────────────┐   │
                    │  │ LASER   │ │ DISPLAY │ │ CONTROL BUTTONS     │   │
                    │  │ RANGING │ │ OLED/LCD│ │ ARM/FIRE/SELECT     │   │
                    │  └─────────┘ └─────────┘ └─────────────────────┘   │
                    └──────────────────────┬──────────────────────────────┘
                                           │
    ┌──────────────────────────────────────┴──────────────────────────────┐
    │                         LAUNCH TUBE                                  │
    │  ┌─────────────┐  ┌───────────────────────────┐  ┌───────────────┐ │
    │  │ MUZZLE      │  │ BARREL ASSEMBLY           │  │ BREECH/       │ │
    │  │ (120mm dia) │  │ (Smoothbore, ~1m length)  │  │ CHAMBER       │ │
    │  └─────────────┘  └───────────────────────────┘  └───────────────┘ │
    └─────────────────────────────────────────────────────────────────────┘
                                           │
    ┌──────────────────────────────────────┴──────────────────────────────┐
    │                      LOWER RECEIVER                                  │
    │  ┌─────────────┐  ┌───────────────┐  ┌───────────────────────────┐ │
    │  │ GAS         │  │ PNEUMATIC     │  │ GRIP + TRIGGER            │ │
    │  │ CYLINDER    │  │ VALVE/REG     │  │ MECHANISM                 │ │
    │  │ (HPA tank)  │  │               │  │                           │ │
    │  └─────────────┘  └───────────────┘  └───────────────────────────┘ │
    └─────────────────────────────────────────────────────────────────────┘
                                           │
                              ┌────────────┴────────────┐
                              │     SHOULDER STOCK      │
                              │  (Adjustable, padded)   │
                              └─────────────────────────┘

═══════════════════════════════════════════════════════════════════════════
```

#### 2.1.3 Projectile Variants (SP Series)

| Model | Type | Contents | Application |
|-------|------|----------|-------------|
| **SP10** | Capture | Net only | Basic capture, forensic intact |
| **SP40** | Capture + Recovery | Net + Parachute | Controlled descent, evidence preservation |
| **SP90** | Capture + Payload | Net + Parachute + Payload | Future capability (marker, jammer?) |
| **TR10** | Training | Net only (reusable) | Operator training |
| **TR40** | Training | Net + Parachute (reusable) | Full sequence training |

#### 2.1.4 SmartScope System

| Feature | Description | Technology |
|---------|-------------|------------|
| **Laser Rangefinder** | Measures distance to target | Pulsed laser, Class 1/2 |
| **Target Tracking** | Locks onto moving target | Video + algorithm |
| **Ballistic Computer** | Calculates launch timing | Embedded processor |
| **Lead Angle Display** | Shows aim point to operator | OLED/LCD overlay |
| **Projectile Programming** | Sets net deploy distance | RF or optical link |
| **Integration Port** | SkyLink for external sensors | Digital interface |

### 2.2 Level 2 - Subsystem Decomposition

#### 2.2.1 Major Subsystems

| ID | Subsystem | Function | Est. Mass | Interface |
|----|-----------|----------|-----------|-----------|
| SS1 | Launch Tube Assembly | Propel projectile | 2.5 kg | Mechanical to SS2, SS3 |
| SS2 | Pneumatic System | Store/regulate gas | 3.0 kg | Gas line to SS1 |
| SS3 | SmartScope Unit | Target/compute/display | 1.5 kg | Electrical to SS4, RF to projectile |
| SS4 | Fire Control Electronics | Process/control/safety | 0.5 kg | Electrical to all |
| SS5 | Structural Frame | Support/ergonomics | 2.0 kg | Mechanical to all |
| SS6 | Projectile (SP40) | Net deployment | 0.5 kg | Pneumatic receive, RF receive |
| | **TOTAL** | | **~10 kg** | |

#### 2.2.2 Interface Matrix

| From \ To | SS1 Tube | SS2 Pneumatic | SS3 Scope | SS4 FCE | SS5 Frame | SS6 Proj |
|-----------|----------|---------------|-----------|---------|-----------|----------|
| SS1 Tube | — | Gas inlet | Mount | — | Mount | Propel |
| SS2 Pneumatic | Gas out | — | — | Trigger signal | Mount | — |
| SS3 Scope | — | — | — | Data | Mount | RF program |
| SS4 FCE | Fire cmd | Valve cmd | Data | — | Mount | — |
| SS5 Frame | Support | Support | Support | Support | — | — |
| SS6 Proj | Receive | — | RF receive | — | — | — |

### 2.3 Level 3 - Component Analysis (Estimated)

#### 2.3.1 Pneumatic System Components

| Component | Estimated Spec | Function | Material |
|-----------|----------------|----------|----------|
| Gas Cylinder | 0.5L, 300 bar, HPA | Store compressed air | Aluminum/CF wrapped |
| Regulator | 300→120 bar | Reduce pressure | Brass/SS |
| Dump Valve | Fast-acting solenoid | Release gas | Aluminum body |
| Gas Lines | 8mm OD, rated 150 bar | Conduct gas | Reinforced nylon |
| Fill Valve | Foster-style quick connect | Refill cylinder | Brass |

#### 2.3.2 SmartScope Components

| Component | Estimated Spec | Function | Technology |
|-----------|----------------|----------|------------|
| Laser Rangefinder | 1-200m, ±0.5m accuracy | Distance measurement | Pulsed 905nm |
| Camera | 720p, 60fps | Target tracking | CMOS sensor |
| Processor | ARM Cortex-M4 or similar | Ballistic computation | Embedded MCU |
| Display | 0.5" OLED, monochrome | Aim point overlay | Micro display |
| RF Transceiver | 2.4GHz or 5.8GHz | Projectile programming | Short-range digital |
| Battery | Li-ion, ~2000mAh | Power SmartScope | 7.4V pack |

#### 2.3.3 Projectile (SP40) Components

| Component | Estimated Spec | Function | Technology |
|-----------|----------------|----------|------------|
| Body | ~80mm dia × 150mm | Structure | Injection molded polymer |
| Net | 4m × 4m (~16m² deployed) | Capture drone | High-strength nylon |
| Parachute | ~1m dia | Controlled descent | Ripstop nylon |
| Deploy Mechanism | Pyrotechnic or spring | Eject net | Mechanical timer or RF trigger |
| RF Receiver | Short-range | Receive deploy command | 2.4/5.8GHz chip |
| Weights | 4× corner weights | Spread net | Metal or polymer |

---

## 3. PHASE 2: MODELING (Function Reconstruction)

### 3.1 Overall Function Statement

> **"Capture an airborne drone target using a net projectile launched from a shoulder-fired pneumatic system, with intelligent targeting assistance to maximize hit probability on moving targets"**

### 3.2 Energy/Material/Signal Flow Analysis

```
SKYWALL 100 - ENERGY/MATERIAL/SIGNAL FLOW
═══════════════════════════════════════════════════════════════════════════

INPUTS                          SYSTEM                          OUTPUTS
──────                          ──────                          ───────

E: Compressed Gas ─────────┐
   (300 bar HPA)           │
                           ▼
E: Battery Power ──────► ┌─────────────────────────────────┐
   (7.4V Li-ion)         │                                 │
                         │      SKYWALL 100 SYSTEM         │ ──► E: Kinetic Energy
S: Visual Scene ────────►│                                 │     (Projectile @~40 m/s)
   (Target drone)        │  Transform: Stored gas energy   │
                         │  → Projectile kinetic energy    │ ──► M: Captured Drone
S: Operator Trigger ────►│  with intelligent timing        │     (In net, parachute descent)
   (Intent to fire)      │                                 │
                         │                                 │ ──► S: Fire Confirmation
S: Target Data ─────────►│                                 │     (Audio/visual feedback)
   (From SkyLink, opt)   └─────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════

FLOW LEGEND:
E = Energy flow
M = Material flow
S = Signal/Information flow
```

### 3.3 Function Structure

```
SKYWALL 100 FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════════════════

OVERALL: Capture airborne drone using net projectile with intelligent targeting

F1: ACQUIRE TARGET INFORMATION
├── F1.1: Detect target visually ─────────── Operator eyes + scope magnification
├── F1.2: Measure target range ───────────── Laser rangefinder (LRF)
├── F1.3: Track target motion ────────────── Camera + tracking algorithm
├── F1.4: Predict target trajectory ──────── Ballistic computer extrapolation
└── F1.5: Receive external cues (opt) ────── SkyLink interface from radar/RF

F2: COMPUTE FIRE SOLUTION
├── F2.1: Calculate projectile trajectory ── Ballistic model (point-mass 3DOF)
├── F2.2: Determine lead angle ───────────── Vector geometry
├── F2.3: Calculate launch timing ────────── Intercept algorithm
├── F2.4: Program projectile ─────────────── RF command (deploy distance)
└── F2.5: Display aim point ──────────────── OLED overlay with lead indicator

F3: AUTHORIZE AND CONTROL FIRE
├── F3.1: Arm system ─────────────────────── Operator arm switch (safety)
├── F3.2: Verify safety conditions ───────── System self-check (BIT)
├── F3.3: Sense trigger pull ─────────────── Mechanical trigger sensor
├── F3.4: Confirm optimal timing ─────────── Computer "GO" indication
└── F3.5: Command pneumatic release ──────── Solenoid valve actuation

F4: PROPEL PROJECTILE
├── F4.1: Release compressed gas ─────────── Dump valve opens
├── F4.2: Accelerate projectile ──────────── Gas expansion in barrel
├── F4.3: Guide projectile exit ──────────── Smoothbore barrel alignment
└── F4.4: Confirm launch ─────────────────── Acoustic/mechanical sensor

F5: DEPLOY CAPTURE MECHANISM
├── F5.1: Travel to target vicinity ──────── Projectile ballistic flight
├── F5.2: Receive deploy command ─────────── RF signal from SmartScope
├── F5.3: Eject net assembly ─────────────── Pyrotechnic/spring mechanism
├── F5.4: Spread net ─────────────────────── Corner weights + aerodynamics
├── F5.5: Entangle target ────────────────── Net engulfs drone
└── F5.6: Deploy parachute ───────────────── Drogue extraction

F6: RECOVER CAPTURED TARGET
├── F6.1: Slow descent ───────────────────── Parachute drag
├── F6.2: Protect evidence ───────────────── Gentle landing, drone intact
└── F6.3: Mark location (optional) ───────── Visual marker or beacon

F_AUX: AUXILIARY FUNCTIONS
├── F_AUX.1: Store gas energy ────────────── HPA cylinder
├── F_AUX.2: Regulate gas pressure ───────── Pressure regulator
├── F_AUX.3: Provide electrical power ────── Li-ion battery
├── F_AUX.4: Support structural loads ────── Frame assembly
├── F_AUX.5: Interface with operator ─────── Ergonomic stock, grip
├── F_AUX.6: Enable reload ───────────────── Breech open mechanism
├── F_AUX.7: Indicate system status ──────── LED indicators, display
└── F_AUX.8: Integrate with C2 (opt) ─────── SkyLink module

═══════════════════════════════════════════════════════════════════════════
TOTAL: 6 Main Functions + 1 Auxiliary = 7 Function Groups, 35 Subfunctions
```

### 3.4 Working Principle Mapping

| ID | Subfunction | Physical Effect | Form Design | Working Principle |
|----|-------------|-----------------|-------------|-------------------|
| WP-01 | F1.2: Measure range | Time-of-flight | Laser + detector | Pulsed LRF |
| WP-02 | F1.3: Track motion | Image correlation | CMOS + algorithm | Video tracker |
| WP-03 | F2.1: Calculate trajectory | Newtonian mechanics | Embedded algorithm | Point-mass ballistics |
| WP-04 | F2.4: Program projectile | EM radiation | RF transceiver | Digital RF link |
| WP-05 | F3.5: Release gas | Electromagnetic actuation | Solenoid valve | Fast-acting dump valve |
| WP-06 | F4.2: Accelerate projectile | Gas expansion | Smoothbore barrel | Pneumatic propulsion |
| WP-07 | F5.3: Eject net | Stored mechanical energy | Spring or pyro | Spring ejector |
| WP-08 | F5.4: Spread net | Aerodynamic drag | Corner weights | Ballistic spreading |
| WP-09 | F5.6: Deploy parachute | Aerodynamic drag | Drogue extraction | Pilot chute deploy |
| WP-10 | F_AUX.1: Store gas | Elastic strain energy | Composite cylinder | HPA storage |

---

## 4. PHASE 3: DESIGN PARADIGM ANALYSIS

### 4.1 Paradigm Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **Safety margins** | Multiple interlocks, continuous monitoring | 5 | High safety priority (civilian use) |
| **Modularity** | Interchangeable projectiles, replaceable cylinder | 4 | Good maintainability |
| **Material selection** | Composite cylinder, polymer projectiles | 3 | Cost-conscious, adequate |
| **Redundancy** | Single-shot, no backup | 2 | Accepts single-point failure |
| **Manufacturing precision** | Moderate tolerances, injection molding | 3 | Volume production focused |
| **Automation level** | Semi-automatic (human in loop) | 4 | Balances safety and speed |

### 4.2 Inferred Design Philosophy

> **"Provide a reliable, safe, and cost-effective method for physically capturing drones that preserves forensic evidence, prioritizes operator safety over engagement speed, and enables integration into broader security systems."**

### 4.3 Trade-off Analysis

| Trade-off | Choice Made | Alternative | Rationale |
|-----------|-------------|-------------|-----------|
| **Range vs Weight** | ~100m range | Longer range = heavier | Balance portability |
| **Kinetic vs Electronic** | Kinetic (net) | RF jamming | Forensic preservation |
| **Autonomy vs Control** | Human-in-loop | Autonomous | Liability, safety |
| **Single vs Multi-shot** | Single-shot | Magazine feed | Simplicity, weight |
| **Explosive vs Pneumatic** | Pneumatic | Pyrotechnic launcher | Safety, regulations |
| **Precision vs Cost** | Moderate tolerance | Tight tolerance | Volume affordability |

### 4.4 Design Philosophy Comparison

| Aspect | SkyWall (UK) | Typical Military | Implication for Indigenous |
|--------|--------------|------------------|---------------------------|
| **Primary user** | Security/LEO | Military | Consider both markets |
| **Collateral damage** | Zero tolerance | Acceptable | Net capture is advantageous |
| **Evidence preservation** | High priority | Low priority | Differentiator |
| **Training level** | Minimal assumed | High | Keep system simple |
| **Cost sensitivity** | High | Moderate | Drive to lower cost |
| **Regulatory environment** | Strict civilian | Military exception | Design for civilian cert |

---

## 5. PERFORMANCE SPECIFICATIONS (Estimated)

### 5.1 Launcher Performance

| Parameter | Estimated Value | Confidence | Method |
|-----------|-----------------|------------|--------|
| Effective range | 100m | High | Published |
| Maximum range | 120-150m | Medium | Extrapolation |
| Muzzle velocity | 40-50 m/s | Medium | Pneumatic analysis |
| Reload time | 8-10 seconds | Medium | Video analysis |
| Shots per fill | 3-5 shots | Low | Cylinder size estimate |
| Weight (loaded) | 10 kg | High | Published |
| Weight (unloaded) | 8 kg | Medium | Calculated |

### 5.2 SmartScope Performance

| Parameter | Estimated Value | Confidence | Method |
|-----------|-----------------|------------|--------|
| LRF range | 5-200m | Medium | Component analysis |
| LRF accuracy | ±0.5m | Medium | Typical LRF spec |
| Tracking speed | <30 m/s targets | Low | Algorithm assumption |
| Display type | OLED, monocular | Medium | Photos |
| Battery life | 4-8 hours | Low | Typical |
| Boot time | <5 seconds | Low | Typical embedded |

### 5.3 Projectile Performance

| Parameter | Estimated Value | Confidence | Method |
|-----------|-----------------|------------|--------|
| Projectile mass | 400-600g | Medium | Photos/video |
| Net deployed area | 8-16 m² | Medium | Published (8 m²) |
| Parachute descent rate | 3-5 m/s | Medium | Typical drogue |
| Deploy distance | 10-20m from target | Low | Algorithm assumption |
| Target size range | 0.2-2m wingspan | Medium | Net size analysis |

---

## 6. TECHNOLOGY ASSESSMENT

### 6.1 Technology Readiness Level (TRL)

| Subsystem | TRL | Assessment |
|-----------|-----|------------|
| Pneumatic launcher | 9 | Mature, widespread |
| Laser rangefinder | 9 | COTS available |
| Video tracking | 8 | Requires integration |
| Ballistic computer | 8 | Algorithm development |
| Smart projectile | 7 | Novel, proprietary |
| Net deployment | 8 | Proven concept |
| Parachute recovery | 9 | Mature technology |
| System integration | 8 | Requires engineering |

### 6.2 Indigenous Replication Feasibility

| Subsystem | Feasibility | Vietnamese Capability | Gap |
|-----------|-------------|----------------------|-----|
| Pneumatic launcher | High | Paintball industry exists | Minor |
| Laser rangefinder | Medium | Import or license | COTS available |
| Video tracking | Medium | Software development | Algorithm |
| Ballistic computer | High | Embedded systems capable | None |
| Smart projectile | Medium | Injection molding OK | RF/timing |
| Net deployment | High | Textile industry strong | None |
| Parachute recovery | High | Parachute capability exists | None |
| **OVERALL** | **Medium-High** | | ~70% local |

### 6.3 Critical Technology Elements

| Element | Criticality | Source Option | Lead Time |
|---------|-------------|---------------|-----------|
| LRF module | High | Import (China) | 4 weeks |
| CMOS camera | Medium | Import (COTS) | 2 weeks |
| RF transceiver | Medium | Import (COTS) | 2 weeks |
| Composite cylinder | Medium | Import (Taiwan) | 6 weeks |
| High-strength net | High | Local development | 8 weeks |
| Embedded processor | Low | Import (COTS) | 2 weeks |

---

## 7. APPLICATION RECOMMENDATIONS

### 7.1 Strategy A: Indigenous Alternative Development

**Objective:** Develop Vietnamese C-UAS net launcher inspired by SkyWall

| Phase | Activity | Duration | Output |
|-------|----------|----------|--------|
| 1 | Function structure validation | 2 weeks | Confirmed requirements |
| 2 | Morphological matrix (local alternatives) | 3 weeks | Concept variants |
| 3 | VDI 2225 evaluation | 1 week | Selected concept |
| 4 | Prototype development | 12 weeks | Working prototype |
| 5 | Qualification testing | 8 weeks | Certified system |

**Estimated Cost:** $150,000-200,000 NRE
**Local Content Target:** 70%
**Unit Cost Target:** $5,000-8,000 (vs SkyWall ~$30,000+)

### 7.2 Strategy B: Counter-System Development

**Objective:** Develop countermeasures against SkyWall-type systems

| Countermeasure | Approach | Effectiveness |
|----------------|----------|---------------|
| Speed increase | >50 m/s drone | Exceeds intercept envelope |
| Evasive maneuver | Sudden direction change | Defeats prediction algorithm |
| Net entanglement resistance | Prop guards, smooth surfaces | Reduces capture reliability |
| Decoy deployment | Chaff/flare equivalent | Confuses tracking |
| Range exploitation | Operate >150m from threat | Outside effective range |

### 7.3 Strategy C: Technology Insertion Points

| Function | SkyWall Solution | Upgrade Opportunity |
|----------|------------------|---------------------|
| F1.3 Target tracking | Basic video tracker | AI-enhanced tracking |
| F1.5 External cues | SkyLink interface | Radar/RF integration |
| F2.4 Projectile program | RF link | Optical link (faster) |
| F5.6 Parachute | Passive | Steerable (precision landing) |
| — | Single shot | Multi-shot magazine |

---

## 8. LESSONS LEARNED

### 8.1 RE Process Insights

| Aspect | Observation | Improvement |
|--------|-------------|-------------|
| OSINT availability | Good for commercial systems | Less available for military |
| Specification estimation | Reasonable from photos/video | Physical specimen preferred |
| Function reconstruction | Straightforward for simple system | More complex systems need more time |
| Paradigm identification | Clear from design choices | Validated by use cases |

### 8.2 Capability Gaps Identified

| Gap | Description | Action |
|-----|-------------|--------|
| Smart projectile RF | No local experience | Partner with RF developer |
| Net material optimization | Strength vs weight trade-off | Material science R&D |
| Tracking algorithm | Need development | AI/ML team training |
| Pneumatic expertise | Limited local experience | Hire from paintball industry |

---

## 9. GATE REVIEW: RE PHASE 1 COMPLETE

### 9.1 Checklist

| Criterion | Status | Evidence |
|-----------|--------|----------|
| System identified and bounded | ✅ | Section 1 |
| External observation documented | ✅ | Section 2.1 |
| Subsystems decomposed | ✅ | Section 2.2 |
| Function structure reconstructed | ✅ | Section 3.3 |
| Working principles mapped | ✅ | Section 3.4 |
| Design paradigm assessed | ✅ | Section 4 |
| Performance estimated | ✅ | Section 5 |
| Replication feasibility assessed | ✅ | Section 6 |
| Application strategies defined | ✅ | Section 7 |

### 9.2 RE Phase 1 Status

**Status:** ✅ **COMPLETE** - Ready for Conceptual Design phase

---

## 10. NEXT STEPS

### 10.1 Immediate Actions

1. **Create project code:** Assign VN-CUA-001 or similar
2. **Stakeholder identification:** Military, police, airport security
3. **Requirements capture:** ODI process for Vietnamese C-UAS needs
4. **Morphological matrix:** Develop with SkyWall as one column

### 10.2 Decision Required

```
A) ✅ PROCEED - Start indigenous C-UAS development project
B) 🔬 DEEP DIVE - More detailed RE analysis (physical specimen needed)
C) 📊 COMPARE - Benchmark against other C-UAS systems first
D) ⏸️ PAUSE - Archive RE analysis for future use
```

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial RE analysis. OSINT-based reconnaissance complete. Function structure with 35 subfunctions, 10 working principles identified. Design paradigm: safety and evidence-focused. Replication feasibility: Medium-High (70% local). Recommended: Proceed to indigenous development.** |

---

## REFERENCES

1. OpenWorks Engineering website: https://openworksengineering.com/
2. DSIAC article on SkyWall100
3. Ars Technica coverage (March 2016)
4. TechCrunch coverage (March 2016)
5. Army Recognition DSEI 2021 coverage

---

*This reverse engineering analysis follows the methodology from SKILL_reverse_engineering.md, applying the D-M-I-R framework to understand the SkyWall 100 design intent and enable indigenous capability development.*
