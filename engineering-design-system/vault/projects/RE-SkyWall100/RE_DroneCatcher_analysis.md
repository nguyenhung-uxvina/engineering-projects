---
project: RE-SkyWall100
type: reverse_engineering
system: DroneCatcher
origin: Netherlands
manufacturer: Delft Dynamics B.V.
phase: reconnaissance
version: 1.0
created: 2026-02-05
status: complete
analyst: Engineering Team
---

# REVERSE ENGINEERING ANALYSIS
## DroneCatcher Interceptor Drone System

**System Designation:** DroneCatcher
**Origin:** Netherlands
**Manufacturer:** Delft Dynamics B.V. (Delft, Netherlands)
**System Type:** Interceptor UAV with Net Gun (C-UAS)
**Analysis Date:** 2026-02-05

---

## 1. SYSTEM IDENTIFICATION

### 1.1 Basic Information

| Parameter | Value | Confidence |
|-----------|-------|------------|
| **Designation** | DroneCatcher | High |
| **Manufacturer** | Delft Dynamics B.V. | High |
| **Country** | Netherlands | High |
| **Founded** | February 2006 | High |
| **System Category** | Interceptor UAV, Kinetic C-UAS | High |
| **Operator** | Ground control station, 1-2 operators | High |

### 1.2 Manufacturer Background

| Parameter | Details |
|-----------|---------|
| **Company** | Delft Dynamics B.V. |
| **Founded** | February 2006 |
| **Founders** | 4 MSc graduates from TU Delft Aerospace Engineering |
| **Experience** | 19+ years in drone R&D |
| **Specialization** | UAS development, C-UAS systems, tethered drones |
| **Other Products** | RH2 'Stern', RH3 'Swift', RH4 'Spyder', U-drone |
| **R&D Projects** | iMUGS2, ORIGAMI, E-CUAS, Combat C-UAS, DeterMine |

### 1.3 System Context

```
DRONECATCHER OPERATIONAL CONTEXT
═══════════════════════════════════════════════════════════════════════════

SUPERSYSTEM: Integrated Air Defense / Site Protection
            │
            ├── DETECTION LAYER
            │   ├── Radar (primary)
            │   ├── RF detection
            │   ├── Acoustic sensors
            │   └── Optical/camera
            │
            ├── TRACKING & ID LAYER
            │   └── C2 system integration
            │
            └── DEFEAT LAYER
                │
                ├── Electronic (jammers)
                │
                └── KINETIC ◄──── DroneCatcher (YOU ARE HERE)
                      │
                      ├── Ground-launched (SkyWall)
                      └── AIR-LAUNCHED (DroneCatcher) ◄──
                            │
                            ├── Tethered standby mode
                            └── Free-flight intercept mode

SIBLING SYSTEMS (Interceptor UAV):
├── Fortem DroneHunter F700 (USA)
├── Anduril Anvil (USA)
├── Skywall Auto (UK) - ground-based auto turret
└── Various national programs

═══════════════════════════════════════════════════════════════════════════
```

---

## 2. PHASE 1: RECONNAISSANCE (DIAGNOSIS)

### 2.1 Level 1 - External Observation (OSINT)

#### 2.1.1 Physical Characteristics

| Parameter | Value | Source | Confidence |
|-----------|-------|--------|------------|
| **System Weight** | <6 kg (13 lb) | NewAtlas, manufacturer | High |
| **Configuration** | Quadcopter/multicopter | Photos/video | High |
| **Propeller Arms** | Folding carbon fiber | NewAtlas | High |
| **Max Speed** | 20 m/s (72 km/h) | NewAtlas | High |
| **Battery Endurance** | 30 minutes | NewAtlas | High |
| **Tethered Endurance** | Indefinite (hours) | Multiple sources | High |
| **Net Gun Range** | Up to 20m (66 ft) | Multiple sources | High |

#### 2.1.2 System Components

```
DRONECATCHER SYSTEM COMPONENTS
═══════════════════════════════════════════════════════════════════════════

COMPLETE SYSTEM INCLUDES:
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    DRONECATCHER UAV                               │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │   │
│  │  │ AIRFRAME    │  │ NET GUN     │  │ SENSORS     │               │   │
│  │  │ • Carbon    │  │ • Pneumatic │  │ • Camera    │               │   │
│  │  │   fiber arms│  │ • Net +     │  │   (gimbal)  │               │   │
│  │  │ • <6 kg     │  │   cable     │  │ • LRF       │               │   │
│  │  │ • Foldable  │  │ • 20m range │  │ • Tracker   │               │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │   │
│  │  │ PROPULSION  │  │ AVIONICS    │  │ POWER       │               │   │
│  │  │ • 4+ motors │  │ • Flight    │  │ • Battery   │               │   │
│  │  │ • ESCs      │  │   controller│  │   (30 min)  │               │   │
│  │  │ • Props     │  │ • Autopilot │  │ • OR tether │               │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    GROUND SEGMENT                                 │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │   │
│  │  │ GROUND      │  │ POWER       │  │ TRANSPORT   │               │   │
│  │  │ CONTROL     │  │ TETHER      │  │ CASES       │               │   │
│  │  │ STATION     │  │ SYSTEM      │  │             │               │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    CONSUMABLES                                    │   │
│  │  ┌─────────────┐  ┌─────────────┐                                │   │
│  │  │ NET         │  │ GAS         │                                │   │
│  │  │ CARTRIDGES  │  │ CARTRIDGES  │                                │   │
│  │  │ (reusable)  │  │ (CO2/HPA)   │                                │   │
│  │  └─────────────┘  └─────────────┘                                │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    SUPPORT                                        │   │
│  │  • Training program                                               │   │
│  │  • Manuals                                                        │   │
│  │  • Spare parts                                                    │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════
```

### 2.2 Level 2 - Subsystem Decomposition

#### 2.2.1 Major Subsystems

| ID | Subsystem | Function | Est. Mass | Key Components |
|----|-----------|----------|-----------|----------------|
| SS1 | Airframe Assembly | Structure, aerodynamics | 1.5 kg | CF arms, body, landing gear |
| SS2 | Propulsion System | Flight power | 1.0 kg | Motors, ESCs, propellers |
| SS3 | Net Gun System | Target capture | 1.2 kg | Pneumatic launcher, net, cable |
| SS4 | Sensor Suite | Target acquisition | 0.8 kg | Camera, gimbal, LRF, tracker |
| SS5 | Avionics/Flight Control | Navigation, autopilot | 0.5 kg | FC, GPS, IMU, comms |
| SS6 | Power System | Energy storage/delivery | 1.0 kg | Battery OR tether interface |
| | **TOTAL** | | **<6 kg** | |

#### 2.2.2 Operating Modes

| Mode | Description | Advantages | Limitations |
|------|-------------|------------|-------------|
| **Tethered Standby** | Connected to ground power, hovering at altitude | Indefinite endurance, always ready | Limited mobility, tether management |
| **Free-Flight Pursuit** | Tether released, battery-powered chase | Full mobility, 20 m/s speed | 30 min endurance, single mission |
| **Carry & Release** | Captures drone, carries to safe location | Evidence preservation | Weight-limited payload |
| **Parachute Descent** | Releases heavy target with controlled fall | Handles heavier targets | Less precise landing |

### 2.3 Level 3 - Component Analysis

#### 2.3.1 Net Gun System (Key Differentiator)

| Component | Estimated Spec | Function | Technology |
|-----------|----------------|----------|------------|
| Launcher | Pneumatic, single shot | Propel net | CO2 or compressed air |
| Net | ~3-4m diameter deployed | Entangle target | High-strength nylon/Dyneema |
| Cable | 10-15m, high tensile | Connect net to UAV | Spectra/Dyneema cord |
| Release Mechanism | Electromechanical | Drop heavy targets | Servo or solenoid |
| Cartridge | Replaceable, reusable nets | Quick reload | Modular design |

#### 2.3.2 Sensor Suite

| Component | Estimated Spec | Function | Technology |
|-----------|----------------|----------|------------|
| Camera | 1080p or 4K, stabilized | Target tracking | CMOS, 3-axis gimbal |
| Laser Rangefinder | 1-100m range | Distance to target | Pulsed laser, Class 1 |
| Tracking Algorithm | Real-time | Lock-on, lead calculation | Computer vision AI |
| Downlink | HD video | Operator awareness | Digital radio |

#### 2.3.3 Tether System (Unique Feature)

| Component | Estimated Spec | Function | Technology |
|-----------|----------------|----------|------------|
| Power Cable | Multi-conductor, 50-100m | Deliver ground power | Lightweight, flexible |
| Tether Reel | Motorized, auto-tension | Cable management | Slip ring, tension control |
| Quick Release | Electromechanical | Instant disconnect | Solenoid or servo latch |
| Ground Power | 48V DC or similar | Supply UAV | AC/DC converter |

---

## 3. PHASE 2: MODELING (Function Reconstruction)

### 3.1 Overall Function Statement

> **"Intercept and capture airborne drone targets using a net-gun equipped UAV that can loiter indefinitely on tether and pursue targets in free flight, then recover or safely descend the captured drone"**

### 3.2 Energy/Material/Signal Flow Analysis

```
DRONECATCHER - ENERGY/MATERIAL/SIGNAL FLOW
═══════════════════════════════════════════════════════════════════════════

INPUTS                          SYSTEM                          OUTPUTS
──────                          ──────                          ───────

E: Ground Power ───────────┐
   (AC mains → DC tether)  │
                           │
E: Battery Power ──────────┤
   (LiPo, ~22V)            │
                           ▼
E: Compressed Gas ──────► ┌─────────────────────────────────┐
   (CO2/HPA cartridge)    │                                 │
                          │      DRONECATCHER SYSTEM        │ ──► E: Kinetic Energy
S: External Detection ───►│                                 │     (Interceptor flight)
   (Radar, RF, acoustic)  │  Transform: Tethered standby   │
                          │  → Pursuit flight              │ ──► M: Captured Drone
S: Operator Commands ────►│  → Net deployment              │     (Carried or parachuted)
   (GCS inputs)           │  → Target recovery             │
                          │                                 │ ──► S: Status/Video
S: Target Visual ─────────┤                                 │     (Telemetry downlink)
   (Onboard camera)       └─────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════

OPERATIONAL SEQUENCE:
1. STANDBY: Tethered hover, indefinite, monitoring
2. ALERT: External system detects threat, cues DroneCatcher
3. RELEASE: Tether disconnects, UAV switches to battery
4. PURSUIT: 20 m/s flight toward target
5. ACQUIRE: Camera + LRF lock on target
6. ENGAGE: Close to 20m, fire net
7. CAPTURE: Net entangles target
8. RECOVER: Carry to safe spot OR release with parachute descent
9. RTB: Return to base, reload, reconnect tether
```

### 3.3 Function Structure

```
DRONECATCHER FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════════════════

OVERALL: Intercept and capture airborne drones using net-equipped UAV

F1: MAINTAIN STANDBY READINESS
├── F1.1: Connect to tether ──────────────── Quick-connect interface
├── F1.2: Receive ground power ───────────── DC power from tether
├── F1.3: Hover at altitude ──────────────── Autopilot station-keeping
├── F1.4: Monitor threat data ────────────── External sensor feed (C2)
└── F1.5: Indicate ready status ──────────── GCS display

F2: TRANSITION TO PURSUIT
├── F2.1: Receive engagement command ─────── Operator or auto trigger
├── F2.2: Release tether ─────────────────── Quick-release mechanism
├── F2.3: Switch to battery power ────────── Seamless power transfer
├── F2.4: Fly to threat vicinity ─────────── Autopilot waypoint
└── F2.5: Estimate intercept point ───────── Flight computer prediction

F3: ACQUIRE TARGET
├── F3.1: Search area visually ───────────── Gimbal camera scan
├── F3.2: Detect target ──────────────────── Computer vision algorithm
├── F3.3: Lock on target ─────────────────── Tracking algorithm
├── F3.4: Measure target range ───────────── Laser rangefinder
├── F3.5: Track target motion ────────────── Continuous CV tracking
└── F3.6: Display to operator ────────────── Video downlink

F4: PURSUE AND CLOSE
├── F4.1: Calculate intercept course ─────── Flight computer
├── F4.2: Navigate to intercept ──────────── Autopilot pursuit mode
├── F4.3: Match target velocity ──────────── Relative velocity control
├── F4.4: Close to engagement range ──────── 20m standoff
└── F4.5: Align net gun ──────────────────── Gimbal + aircraft attitude

F5: DEPLOY CAPTURE MECHANISM
├── F5.1: Verify firing solution ─────────── Algorithm GO/NO-GO
├── F5.2: Arm net gun ────────────────────── Safety unlock
├── F5.3: Fire pneumatic launcher ────────── Solenoid valve release
├── F5.4: Propel net to target ───────────── Gas expansion
├── F5.5: Spread net over target ─────────── Weighted net deployment
└── F5.6: Entangle target rotors ─────────── Net mesh captures drone

F6: RECOVER CAPTURED TARGET
├── F6.1: Assess captured weight ─────────── Strain/load sensor
├── F6.2A: CARRY MODE
│   ├── F6.2A.1: Arrest descent ──────────── Increase thrust
│   ├── F6.2A.2: Fly to safe zone ────────── Navigate with load
│   └── F6.2A.3: Lower target gently ─────── Controlled descent
├── F6.2B: RELEASE MODE (heavy target)
│   ├── F6.2B.1: Release cable ───────────── Electromechanical release
│   └── F6.2B.2: Parachute descent ───────── DroneCatcher as drogue
└── F6.3: Mark landing location ──────────── GPS coordinates to GCS

F7: RETURN TO BASE
├── F7.1: Navigate to base ───────────────── Autopilot RTB
├── F7.2: Land safely ────────────────────── Auto-land sequence
├── F7.3: Reload net cartridge ───────────── Manual or auto
└── F7.4: Reconnect tether ───────────────── Prepare for next mission

F_AUX: AUXILIARY FUNCTIONS
├── F_AUX.1: Store electrical energy ─────── LiPo battery pack
├── F_AUX.2: Store pneumatic energy ──────── CO2/HPA cartridge
├── F_AUX.3: Provide flight control ──────── Autopilot system
├── F_AUX.4: Communicate with GCS ────────── Telemetry + video
├── F_AUX.5: Navigate ────────────────────── GPS + INS
├── F_AUX.6: Manage tether ───────────────── Reel + tension control
├── F_AUX.7: Self-diagnose ───────────────── BIT functions
└── F_AUX.8: Integrate with C2 ───────────── External sensor cueing

═══════════════════════════════════════════════════════════════════════════
TOTAL: 7 Main Functions + 1 Auxiliary = 8 Function Groups, 42 Subfunctions
```

### 3.4 Working Principle Mapping

| ID | Subfunction | Physical Effect | Form Design | Working Principle |
|----|-------------|-----------------|-------------|-------------------|
| WP-01 | F1.3: Hover | Aerodynamic lift | Multicopter | Quad/hexacopter lift |
| WP-02 | F2.2: Release tether | Mechanical unlatch | Quick-release | Electromechanical latch |
| WP-03 | F3.3: Lock on target | Image correlation | Gimbal camera | AI visual tracking |
| WP-04 | F3.4: Measure range | Time-of-flight | Laser + detector | Pulsed LRF |
| WP-05 | F4.2: Navigate | Waypoint following | Autopilot | GPS + INS guidance |
| WP-06 | F5.3: Fire launcher | Gas expansion | Pneumatic | CO2/HPA propulsion |
| WP-07 | F5.5: Spread net | Aerodynamic drag | Weighted corners | Ballistic spreading |
| WP-08 | F6.2A.1: Arrest descent | Thrust > weight | Increased motor RPM | Powered lift recovery |
| WP-09 | F6.2B.2: Parachute | Aerodynamic drag | UAV as drogue | Controlled drag descent |
| WP-10 | F_AUX.6: Tether power | Electrical conduction | Power cable | Tethered power delivery |

---

## 4. PHASE 3: DESIGN PARADIGM ANALYSIS

### 4.1 Paradigm Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **Safety margins** | Tethered standby, controlled descent | 4 | Good safety focus |
| **Modularity** | Replaceable nets, battery/tether dual mode | 5 | High modularity |
| **Material selection** | Carbon fiber, aerospace-grade | 4 | Performance-focused |
| **Redundancy** | Dual power source (tether/battery) | 4 | Good redundancy |
| **Manufacturing precision** | Custom aerospace | 4 | Quality-focused |
| **Automation level** | Semi-autonomous with operator oversight | 4 | Balanced autonomy |

### 4.2 Inferred Design Philosophy

> **"Provide a persistent, rapidly-deployable aerial intercept capability that can loiter indefinitely and engage drone threats with kinetic capture while preserving evidence and minimizing collateral risk through controlled recovery options."**

### 4.3 Trade-off Analysis

| Trade-off | Choice Made | Alternative | Rationale |
|-----------|-------------|-------------|-----------|
| **Tethered vs Battery** | Both (hybrid) | One or other | Indefinite standby + mobile pursuit |
| **Net vs Jammer** | Net capture | RF jamming | Forensic evidence, works on autonomous |
| **Drone vs Ground** | Drone intercept | Ground launcher | 3D mobility, pursuit capability |
| **Carry vs Release** | Both options | One or other | Flexible target weight handling |
| **AI vs Manual** | Semi-autonomous | Full manual or auto | Balance control + reaction speed |
| **Single vs Multi-shot** | Single shot | Magazine | Weight, complexity trade-off |

### 4.4 Comparison: DroneCatcher vs SkyWall

| Aspect | DroneCatcher | SkyWall 100 |
|--------|--------------|-------------|
| **Platform** | UAV (aerial) | Man-portable (ground) |
| **Operator** | GCS, remote | Shoulder-fired, co-located |
| **Range** | km (flight) + 20m (net) | 100m (projectile) |
| **Endurance** | Indefinite (tethered) | Gas cylinder shots |
| **Pursuit** | Yes, 20 m/s | No, stationary shooter |
| **Engagement Volume** | 3D, large area | Limited by sight line |
| **Complexity** | High | Medium |
| **Cost** | $50,000+ | $30,000+ |
| **Training** | 8+ hours | 4 hours |
| **Weather** | Wind limited | Less sensitive |
| **Stealth** | Audible drone | Quiet until fire |

---

## 5. PERFORMANCE SPECIFICATIONS (Estimated)

### 5.1 Flight Performance

| Parameter | Estimated Value | Confidence | Notes |
|-----------|-----------------|------------|-------|
| Max speed | 20 m/s (72 km/h) | High | Published |
| Battery endurance | 30 minutes | High | Published |
| Tethered endurance | Hours (indefinite) | High | Published |
| Service ceiling | ~400m AGL | Medium | Typical for class |
| Wind tolerance | 10-15 m/s | Medium | Estimate |
| Weight (w/ net) | <6 kg | High | Published |
| Payload capacity | ~2 kg (carry mode) | Low | Estimate |

### 5.2 Net Gun Performance

| Parameter | Estimated Value | Confidence | Notes |
|-----------|-----------------|------------|-------|
| Net gun range | 20m (66 ft) | High | Published |
| Net deployed area | ~12 m² | Medium | Estimate |
| Net velocity | ~15-20 m/s | Low | Pneumatic typical |
| Reload time | 1-2 minutes | Low | Ground reload |
| Shots per cartridge | 1 (single shot) | High | Design |

### 5.3 Sensor Performance

| Parameter | Estimated Value | Confidence | Notes |
|-----------|-----------------|------------|-------|
| Camera resolution | 1080p-4K | Medium | Modern standard |
| LRF range | 1-100m | Medium | Estimate |
| Tracking speed | <20 m/s targets | Medium | Must match UAV speed |
| Gimbal stabilization | 3-axis | Medium | Typical |

---

## 6. TECHNOLOGY ASSESSMENT

### 6.1 Technology Readiness Level (TRL)

| Subsystem | TRL | Assessment |
|-----------|-----|------------|
| Multicopter airframe | 9 | Mature, commercial available |
| Flight controller | 9 | COTS (Pixhawk, DJI, etc.) |
| Pneumatic net gun | 7-8 | Proven, integration needed |
| Tracking gimbal | 8-9 | COTS available |
| Laser rangefinder | 9 | COTS available |
| Tether power system | 7-8 | Specialized, proven concept |
| AI tracking | 7-8 | Active development area |
| System integration | 7 | Custom engineering |

### 6.2 Indigenous Replication Feasibility

| Subsystem | Feasibility | Vietnamese Capability | Gap |
|-----------|-------------|----------------------|-----|
| Multicopter airframe | High | Local drone industry exists | Minor |
| Flight controller | High | COTS or local (VietDrone) | None |
| Pneumatic net gun | Medium | Paintball/pneumatics OK | Integration |
| Tracking gimbal | Medium | Import (China) or develop | Moderate |
| Laser rangefinder | Medium | Import (China COTS) | Minor |
| Tether power system | Medium | Electrical engineering OK | Design |
| AI tracking | Medium | Software development | Algorithm |
| **OVERALL** | **Medium-High** | | ~65% local |

### 6.3 Comparison with SkyWall Replication

| Factor | DroneCatcher | SkyWall | Implication |
|--------|--------------|---------|-------------|
| Core technology | UAV + net gun | Pneumatic launcher | UAV more complex |
| Development time | 18-24 months | 12-18 months | SkyWall faster |
| Development cost | $200-300K | $150-200K | SkyWall cheaper |
| Local content | 65% | 70% | Similar |
| Operational advantage | Pursuit, 3D | Simpler, lighter | Complementary |

---

## 7. APPLICATION RECOMMENDATIONS

### 7.1 DroneCatcher in Indigenous Portfolio

```
UPDATED INDIGENOUS C-UAS PORTFOLIO
═══════════════════════════════════════════════════════════════════════════

TIER 1: MAN-PORTABLE NET LAUNCHER (SkyWall-inspired) ← PRIORITY 1
────────────────────────────────────────────────────────────────────
Target: $5,000-8,000 | Timeline: 12-18 months
USE CASE: Event security, VIP protection, mobile response

TIER 2: INTERCEPTOR DRONE (DroneCatcher-inspired) ← PRIORITY 2 (NEW)
─────────────────────────────────────────────────────────────────────
Target: $15,000-25,000 | Timeline: 18-24 months
KEY FEATURES:
• Simplified design (no tether initially)
• 15-20 min endurance (battery only)
• Net gun 15-20m range
• Semi-autonomous tracking
• Local multicopter platform
USE CASE: Fixed site defense, airport, critical infrastructure

TIER 3: TETHERED INTERCEPTOR (DroneCatcher full capability)
────────────────────────────────────────────────────────────
Target: $30,000-40,000 | Timeline: 24-30 months
KEY FEATURES:
• Add tethered power option
• Extended endurance
• Integration with detection systems
USE CASE: Continuous coverage, high-value sites

═══════════════════════════════════════════════════════════════════════════
```

### 7.2 Technology Insertion from DroneCatcher

| Technology | From DroneCatcher | Application |
|------------|-------------------|-------------|
| Tethered power | Indefinite hover concept | Future V-SMASH integration (targeting UAV) |
| AI tracking gimbal | Target lock-on | Enhance SkyWall SmartScope |
| Net + cable recovery | Controlled descent | Improve SkyWall projectile design |
| Modular net cartridge | Quick reload | Design for rapid re-engagement |

### 7.3 Counter-System Opportunities

| Countermeasure | Against DroneCatcher | Effectiveness |
|----------------|---------------------|---------------|
| Speed >20 m/s | Exceeds pursuit speed | High |
| Tether attack | Cut power cable | High (if tethered) |
| Decoys | Confuse tracking | Medium |
| Swarm tactics | Overwhelm single interceptor | High |
| Low altitude/obstacles | Limit pursuit | Medium |

---

## 8. KEY INSIGHTS

### 8.1 DroneCatcher Unique Contributions

1. **Tethered standby concept:** Indefinite loiter solves "reaction time vs endurance" trade-off
2. **Dual recovery modes:** Carry light targets, parachute heavy ones
3. **3D pursuit capability:** Can chase maneuvering targets, unlike ground systems
4. **Modular approach:** Interchangeable net cartridges for quick turnaround

### 8.2 Limitations Identified

1. **Weather dependency:** Wind limits operations more than ground systems
2. **Single-shot:** Must RTB to reload (unlike jammers)
3. **Complexity:** More failure modes than ground launcher
4. **Audible signature:** Drone noise alerts target

### 8.3 Synergy with SkyWall-type System

| Scenario | Best System | Reason |
|----------|-------------|--------|
| VIP close protection | SkyWall | Portable, quiet, immediate |
| Fixed site perimeter | DroneCatcher | Persistent coverage, pursuit |
| Mobile patrol | SkyWall | Fits in vehicle, dismountable |
| Airport | Both | Layered defense |
| Remote site | DroneCatcher | Autonomous coverage |

---

## 9. CONCLUSION

### 9.1 DroneCatcher vs SkyWall Summary

| Factor | Winner | Notes |
|--------|--------|-------|
| Cost to develop | SkyWall | Simpler system |
| Operational flexibility | DroneCatcher | 3D pursuit |
| Ease of use | SkyWall | Point-and-shoot |
| Coverage area | DroneCatcher | Tethered + pursuit |
| Evidence preservation | Tie | Both capture intact |
| Indigenous feasibility | SkyWall (slightly) | Less complex integration |

### 9.2 Recommendation

**Proceed with SkyWall-type (Tier 1) as priority**, but incorporate DroneCatcher technologies:
- Modular net cartridge design
- AI-assisted tracking (future SmartScope upgrade)
- Plan for Tier 2 interceptor drone (phase 2 development)

---

## SOURCES

- [DroneCatcher Official](https://dronecatcher.nl/)
- [Delft Dynamics](https://www.delftdynamics.nl/)
- [NewAtlas - DroneCatcher Upgrade](https://newatlas.com/dronecatcher/55056/)
- [Electronic Specifier](https://www.electronicspecifier.com/industries/robotics/unleashing-the-dronecatcher-for-controlled-interception/)
- [Army Recognition DSEI 2017](https://www.armyrecognition.com/news/army-news/2017/dronecatcher-counter-drone-system-delft-dynamics-dsei-2017-london-uk)

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial RE analysis. DroneCatcher interceptor drone, 42 subfunctions, 10 working principles. Key insight: tethered standby + pursuit hybrid concept. Recommended as Tier 2 after SkyWall-type ground launcher.** |
