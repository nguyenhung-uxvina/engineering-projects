---
project: RE-SkyWall100
type: benchmark_analysis
version: 1.0
created: 2026-02-05
status: complete
systems_compared: 8
---

# C-UAS SYSTEM BENCHMARK COMPARISON
## SkyWall 100 vs Competitive Systems

**Analysis Date:** 2026-02-05
**Systems Analyzed:** 8 Counter-UAS platforms
**Purpose:** Inform indigenous C-UAS development strategy

---

## 1. SYSTEM CLASSIFICATION

### 1.1 C-UAS Defeat Methods

```
C-UAS DEFEAT TAXONOMY
═══════════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────────────────┐
                    │              C-UAS DEFEAT METHODS                    │
                    └───────────────────────┬─────────────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────┐
        │                                   │                               │
        ▼                                   ▼                               ▼
┌───────────────┐               ┌───────────────────┐           ┌───────────────────┐
│   KINETIC     │               │    ELECTRONIC     │           │  DIRECTED ENERGY  │
│               │               │                   │           │                   │
├───────────────┤               ├───────────────────┤           ├───────────────────┤
│ • Net capture │◄─ SkyWall    │ • RF jamming      │◄─ DroneGun│ • Laser (HELWS)   │
│ • Projectile  │               │ • GPS spoofing    │           │ • HPM (microwave) │
│ • Interceptor │◄─ DroneHunter│ • Protocol attack │           │                   │
│   drone       │◄─ DroneCatcher│ • Cyber takeover │           │                   │
└───────────────┘               └───────────────────┘           └───────────────────┘

ADVANTAGES:
Kinetic: Forensic intact, works against hardened drones
Electronic: Long range, low collateral, multi-target
Directed Energy: Unlimited shots, speed-of-light engagement

DISADVANTAGES:
Kinetic: Single target, limited range, ammunition
Electronic: Ineffective vs autonomous drones, regulatory issues
Directed Energy: High cost, power hungry, weather dependent
```

### 1.2 Systems Analyzed

| #   | System                | Manufacturer          | Country     | Type            | Category            |
| --- | --------------------- | --------------------- | ----------- | --------------- | ------------------- |
| 1   | **SkyWall Patrol**    | OpenWorks Engineering | UK          | Man-portable    | Kinetic (Net)       |
| 2   | **DroneGun Tactical** | DroneShield           | Australia   | Man-portable    | Electronic (Jammer) |
| 3   | **DroneGun Mk4**      | DroneShield           | Australia   | Handheld        | Electronic (Jammer) |
| 4   | **DroneDefender**     | Battelle/Dedrone      | USA         | Man-portable    | Electronic (Jammer) |
| 5   | **Dronekiller**       | IXI EW                | USA         | Man-portable    | Electronic (Jammer) |
| 6   | **DroneCatcher**      | Delft Dynamics        | Netherlands | Interceptor UAV | Kinetic (Net)       |
| 7   | **DroneHunter F700**  | Fortem Technologies   | USA         | Interceptor UAV | Kinetic (Net)       |
| 8   | **Skylock Dome**      | Skylock               | Israel      | Fixed/Mobile    | Electronic (Jammer) |

---

## 2. SPECIFICATIONS COMPARISON

### 2.1 Man-Portable Systems (Kinetic vs Electronic)

| Parameter | SkyWall Patrol | DroneGun Tactical | DroneGun Mk4 | DroneDefender | Dronekiller |
|-----------|----------------|-------------------|--------------|---------------|-------------|
| **Type** | Net launcher | RF jammer | RF jammer | RF jammer | RF jammer |
| **Weight** | ~10 kg | 7.3 kg | 3.2 kg | <4.5 kg | 4.0 kg |
| **Range** | 100m | 1-2 km | ~1 km | 400m | 1 km |
| **Power** | Compressed air | Battery 14.4V | Battery | Battery | Battery |
| **Battery Life** | N/A (gas) | 8 hr | ~4 hr | 5 hr | 2-6 hr |
| **Reload Time** | 8-10 sec | N/A | N/A | N/A | N/A |
| **Form Factor** | Bazooka/tube | Rifle | Pistol | Rifle attachment | Rifle |
| **Target Result** | Captured intact | Land/RTH | Land/RTH | Land/RTH | Land/RTH |
| **Multi-target** | No (single shot) | Yes | Yes | Yes | Yes |
| **Price Est.** | $30,000+ | $30,000+ | ~$15,000 | $20,000+ | ~$25,000 |

### 2.2 Interceptor Drone Systems

| Parameter | DroneCatcher | DroneHunter F700 |
|-----------|--------------|------------------|
| **Type** | Net-gun drone | Autonomous interceptor |
| **Weight** | <6 kg | 18 kg |
| **Speed** | 20 m/s | High agility |
| **Range** | System-dependent | 5 km |
| **Net Range** | 20m from target | Close approach |
| **Capture Method** | Pneumatic net gun | NetGun/DrogueNet |
| **Autonomy** | Semi-autonomous | Fully autonomous |
| **Tether Option** | Yes (indefinite hover) | No |
| **Target Size** | Small-medium drones | Group 1-3 drones |
| **Success Rate** | Not published | 85% |
| **Price Est.** | $50,000+ | $100,000+ |

### 2.3 Fixed/Mobile Systems

| Parameter | Skylock Dome | Comments |
|-----------|--------------|----------|
| **Type** | Detection + Jamming | Integrated system |
| **Detection Range** | 5 km (airport) | 360° RF detection |
| **Defeat Range** | Up to 15 km | Directional jamming |
| **Detection Time** | <5 seconds | Real-time tracking |
| **Coverage** | 360° | Omnidirectional antennas |
| **Targets** | Multiple simultaneous | Swarm capable |
| **Mobility** | Fixed or mobile | Vehicle-mounted option |
| **Limitation** | Ineffective vs military hardened | Commercial drones only |
| **Price Est.** | $200,000+ | System price |

---

## 3. CAPABILITY MATRIX

### 3.1 Effectiveness by Threat Type

| System | Commercial Drone | FPV Racing | Military Hardened | Swarm | Autonomous |
|--------|------------------|------------|-------------------|-------|------------|
| SkyWall Patrol | ✅ High | ⚠️ Medium | ✅ High | ❌ Low | ✅ High |
| DroneGun Tactical | ✅ High | ✅ High | ❌ Low | ⚠️ Medium | ❌ Low |
| DroneDefender | ✅ High | ✅ High | ❌ Low | ⚠️ Medium | ❌ Low |
| Dronekiller | ✅ High | ✅ High | ❌ Low | ⚠️ Medium | ❌ Low |
| DroneCatcher | ✅ High | ⚠️ Medium | ✅ High | ❌ Low | ✅ High |
| DroneHunter F700 | ✅ High | ✅ High | ✅ High | ⚠️ Medium | ✅ High |
| Skylock Dome | ✅ High | ✅ High | ❌ Low | ✅ High | ❌ Low |

**Legend:** ✅ High effectiveness | ⚠️ Medium effectiveness | ❌ Low effectiveness

### 3.2 Operational Characteristics

| System | Training Time | Mobility | Covert Use | Legal (Civilian) | Evidence Preservation |
|--------|---------------|----------|------------|------------------|----------------------|
| SkyWall Patrol | 4 hours | ✅ Excellent | ⚠️ Visible | ✅ Yes | ✅ Intact |
| DroneGun Tactical | 2 hours | ✅ Good | ⚠️ Visible | ⚠️ Restricted | ❌ None |
| DroneDefender | 2 hours | ✅ Good | ⚠️ Visible | ❌ Fed only | ❌ None |
| Dronekiller | 2 hours | ✅ Good | ⚠️ Visible | ⚠️ Restricted | ❌ None |
| DroneCatcher | 8 hours | ⚠️ Medium | ❌ Obvious | ✅ Yes | ✅ Intact |
| DroneHunter F700 | 16+ hours | ⚠️ Medium | ❌ Obvious | ✅ Yes | ✅ Intact |
| Skylock Dome | 8 hours | ❌ Fixed | ✅ Covert | ⚠️ Restricted | ❌ None |

### 3.3 Cost-Effectiveness Analysis

| System | Unit Cost | Cost per Engagement | Reusability | TCO (5 yr) |
|--------|-----------|---------------------|-------------|------------|
| SkyWall Patrol | $30,000 | $200-500/projectile | Limited | $50,000 |
| DroneGun Tactical | $30,000 | ~$0 (battery) | Unlimited | $35,000 |
| DroneDefender | $20,000 | ~$0 (battery) | Unlimited | $25,000 |
| Dronekiller | $25,000 | ~$0 (battery) | Unlimited | $30,000 |
| DroneCatcher | $50,000 | $100/net | Nets reusable | $65,000 |
| DroneHunter F700 | $100,000 | $500/net | Nets disposable | $150,000 |
| Skylock Dome | $200,000 | ~$0 (electricity) | Unlimited | $250,000 |

---

## 4. FUNCTION COMPARISON

### 4.1 Parallel Function Structure

| Function | SkyWall | DroneGun | DroneCatcher | DroneHunter |
|----------|---------|----------|--------------|-------------|
| **F1: Acquire Target** | | | | |
| F1.1 Detect | Operator visual | Operator visual | Radar/RF/camera | Radar guided |
| F1.2 Range | Laser rangefinder | N/A | Laser rangefinder | Radar ranging |
| F1.3 Track | Video tracker | N/A | Camera + gimbal | AI tracking |
| F1.4 Identify | Operator | Operator | Operator | AI classification |
| **F2: Compute Solution** | | | | |
| F2.1 Calculate | Ballistic computer | N/A | Flight planning | Autonomous AI |
| F2.2 Lead angle | SmartScope | N/A | UAV maneuver | AI prediction |
| **F3: Authorize Fire** | | | | |
| F3.1 Arm | Manual switch | Manual switch | Remote command | Autonomous/manual |
| F3.2 Fire | Trigger pull | Trigger hold | Remote command | Autonomous |
| **F4: Defeat Target** | | | | |
| F4.1 Method | Net capture | RF disruption | Net capture | Net capture |
| F4.2 Mechanism | Pneumatic launch | EM transmission | Pneumatic net gun | NetGun/DrogueNet |
| **F5: Recover** | | | | |
| F5.1 Descent | Parachute | Uncontrolled | Carry or parachute | Parachute |
| F5.2 Evidence | ✅ Preserved | ❌ Lost | ✅ Preserved | ✅ Preserved |

### 4.2 Working Principle Comparison

| Subfunction | SkyWall WP | DroneGun WP | DroneCatcher WP | DroneHunter WP |
|-------------|------------|-------------|-----------------|----------------|
| Ranging | Pulsed LRF | — | Pulsed LRF | Radar |
| Tracking | Video correlation | — | Camera + gimbal | AI + radar |
| Propulsion | Compressed gas | — | Multicopter | Custom airframe |
| Defeat | Net entanglement | RF jamming | Net entanglement | Net entanglement |
| Recovery | Parachute | Drone RTH | UAV carry/release | Parachute |

---

## 5. STRENGTHS & WEAKNESSES

### 5.1 SkyWall Patrol

| Strengths | Weaknesses |
|-----------|------------|
| ✅ Captures drone intact (forensics) | ❌ Single shot (reload required) |
| ✅ Works against autonomous drones | ❌ Short range (100m) |
| ✅ No RF interference (legal) | ❌ Heavy (10 kg) |
| ✅ SmartScope aids accuracy | ❌ Requires operator skill |
| ✅ Works against hardened drones | ❌ High cost per engagement |
| ✅ No electronics to jam | ❌ Limited to visible targets |

### 5.2 Electronic Jammers (DroneGun, DroneDefender, Dronekiller)

| Strengths | Weaknesses |
|-----------|------------|
| ✅ Long range (400m - 2km) | ❌ Ineffective vs autonomous drones |
| ✅ Lightweight (3-7 kg) | ❌ Destroys forensic evidence |
| ✅ Multi-target capable | ❌ Legal restrictions (civilian) |
| ✅ Unlimited "shots" | ❌ Defeated by freq-hopping |
| ✅ Low cost per engagement | ❌ Collateral interference |
| ✅ Simple operation | ❌ Ineffective vs military drones |

### 5.3 Interceptor Drones (DroneCatcher, DroneHunter)

| Strengths | Weaknesses |
|-----------|------------|
| ✅ Long range (km scale) | ❌ High system cost |
| ✅ Works against all drone types | ❌ Complex operation |
| ✅ Preserves evidence | ❌ Weather dependent |
| ✅ Can pursue maneuvering targets | ❌ Long training time |
| ✅ Autonomous operation possible | ❌ Regulatory challenges |
| ✅ Multiple engagements | ❌ Maintenance intensive |

---

## 6. MARKET & STRATEGIC ANALYSIS

### 6.1 Price-Performance Positioning

```
C-UAS PRICE vs CAPABILITY MAP
═══════════════════════════════════════════════════════════════════════════

CAPABILITY
    ↑
High│                                    ┌─────────────────┐
    │                                    │ DroneHunter F700│
    │                    ┌───────────┐   │ $100K           │
    │                    │DroneCatcher│   │ Autonomous      │
    │                    │ $50K       │   └─────────────────┘
    │    ┌───────────┐   └───────────┘
    │    │ SkyWall   │
Med │    │ $30K      │   ┌────────────────────────────────┐
    │    │ Forensic+ │   │ DroneGun Tactical $30K         │
    │    └───────────┘   │ Long range, but limited vs     │
    │                    │ autonomous targets              │
    │                    └────────────────────────────────┘
    │    ┌───────────┐   ┌───────────┐
Low │    │ Indigenous│   │ Dronekiller│
    │    │ TARGET    │   │ $25K       │
    │    │ $5-8K     │◄──│            │
    │    └───────────┘   └───────────┘
    │
    └────────────────────────────────────────────────────────────→ COST
        Low              Medium                    High

═══════════════════════════════════════════════════════════════════════════
```

### 6.2 Technology Gap Analysis (for Indigenous Development)

| Capability | Best-in-Class | Gap vs SkyWall | Indigenous Feasibility |
|------------|---------------|----------------|------------------------|
| Detection range | DroneHunter (5km radar) | SkyWall 100m visual | Need radar/sensor integration |
| Defeat mechanism | SkyWall (net intact) | Equal | Net + parachute achievable |
| Autonomy | DroneHunter (AI) | SkyWall manual | Add AI tracking option |
| Multi-target | Jammers (unlimited) | SkyWall single-shot | Add magazine or multi-tube |
| Weight | DroneGun Mk4 (3.2kg) | SkyWall 10kg | Optimize structure |
| Cost | Indigenous target | SkyWall $30K | Target $5-8K |

### 6.3 Vietnamese Market Opportunity

| Application | Primary Need | Best Fit | Indigenous Opportunity |
|-------------|--------------|----------|------------------------|
| Airport security | Long range, 24/7 | Skylock Dome + SkyWall | High (complement imported) |
| Event security | Portable, quick deploy | SkyWall or DroneGun | High (cost-sensitive) |
| Military base | All-threat, autonomous | DroneHunter | Medium (license or develop) |
| VIP protection | Covert, reliable | DroneGun + SkyWall | High (multiple needed) |
| Border patrol | Long range, mobile | DroneHunter + jammers | Medium (complex) |

---

## 7. RECOMMENDATIONS

### 7.1 Indigenous Development Strategy

Based on benchmark analysis, recommend **hybrid approach**:

```
RECOMMENDED INDIGENOUS C-UAS PORTFOLIO
═══════════════════════════════════════════════════════════════════════════

TIER 1: MAN-PORTABLE NET LAUNCHER (SkyWall-inspired)
────────────────────────────────────────────────────
Target: $5,000-8,000 | Weight: <8 kg | Range: 80-100m
- Pneumatic launcher (local capability)
- Simplified SmartScope (LRF + manual tracking)
- Forensic-preserving net + parachute
- Vietnamese manufacturing: 70%+
USE CASE: Event security, VIP protection, military training

TIER 2: ELECTRONIC JAMMER (DroneGun-inspired)
─────────────────────────────────────────────
Target: $8,000-12,000 | Weight: <5 kg | Range: 500m-1km
- Multi-band RF jammer
- GPS disruption
- Compact rifle form factor
- Selective frequency bands
USE CASE: Quick response, multi-target scenarios

TIER 3: INTERCEPTOR DRONE (Future phase)
────────────────────────────────────────
Target: $30,000-50,000 | Range: 2-3 km
- Multicopter with net gun
- Semi-autonomous tracking
- Integrate with detection systems
USE CASE: Large area defense, autonomous patrol

═══════════════════════════════════════════════════════════════════════════
```

### 7.2 Priority Development Recommendation

| Priority | System | Rationale | Timeline |
|----------|--------|-----------|----------|
| **1** | Net Launcher (SkyWall-type) | Unique capability, forensic value, achievable | 12-18 months |
| **2** | RF Jammer | Simpler technology, complement net launcher | 18-24 months |
| **3** | Interceptor Drone | Complex, consider license or partnership | 24-36 months |

### 7.3 Key Differentiators for Indigenous System

| Feature | Import (SkyWall) | Indigenous Target | Advantage |
|---------|------------------|-------------------|-----------|
| Price | $30,000+ | $5,000-8,000 | 75% cost reduction |
| Local content | 0% | 70%+ | Self-reliance |
| Maintenance | Vendor-dependent | Local support | Availability |
| Customization | Fixed | Adaptable | Mission-specific |
| Integration | SkyLink only | Open architecture | Flexibility |

---

## 8. CONCLUSION

### 8.1 Key Findings

1. **SkyWall's unique value:** Only man-portable system that preserves forensic evidence and works against autonomous/hardened drones

2. **Electronic jammers' limitation:** Ineffective against the growing threat of autonomous drones (FPV, pre-programmed)

3. **Market gap:** No affordable (<$10K) man-portable net capture system exists

4. **Indigenous opportunity:** Vietnam can develop competitive C-UAS at 20-25% of import cost with 70% local content

### 8.2 Recommended Next Steps

1. ✅ **PROCEED** with indigenous net launcher development (VN-CUA-001)
2. Use SkyWall function structure as baseline
3. Simplify SmartScope to reduce cost
4. Target $5,000-8,000 price point
5. Design for 70%+ local content

---

## SOURCES

- [DroneShield Products](https://www.droneshield.com/products-dismounted)
- [Battelle DroneDefender](https://www.battelle.org/government-offerings/national-security/payloads-platforms-controls/counter-uas-technologies/dronedefender)
- [DroneCatcher](https://dronecatcher.nl/)
- [Fortem DroneHunter F700](https://fortemtech.com/products/dronehunter-f700/)
- [IXI Dronekiller](https://www.ixiew.com/products/dronekiller-2/)
- [Skylock C-UAS](https://www.skylock1.com/)
- [OpenWorks SkyWall Patrol](https://openworksengineering.com/skywall-patrol/)

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-05** | **Initial benchmark comparison. 8 systems analyzed across kinetic and electronic categories. Identified market gap for affordable net capture system. Recommended 3-tier indigenous development strategy with net launcher as priority.** |
