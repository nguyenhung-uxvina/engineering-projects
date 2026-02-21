---
project: VN-TRN-LOMAH
phase: 0
type: reverse-engineering
subject: Theissen Training Systems LOMAH (Germany)
version: 1.0
created: 2026-02-06
status: complete
---

# RE: Theissen Training Systems LOMAH - Germany
## Reverse Engineering Analysis from Public Sources

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | T.T.S. Theissen Training Systems GmbH |
| **HQ** | Dusseldorf, Germany |
| **Production** | Germany, Belgium, North America |
| **Core competency** | Targetry from sport air guns to tank/anti-tank ammunition |
| **Standards** | FASIT compliant (US Army standard) |
| **Key contracts** | US Army LTRaC MAC-3 (FASIT, JPMRC, STE-LTS, USMC) |
| **Contact** | +49 (211) 97504-0 / info@theissentraining.de |
| **Website** | https://theissentraining.com |

**Key differentiator vs. Zen Technologies:** TTS offers **two distinct scoring technologies** - open-air LOMAH (supersonic only) AND Box Target / Chambered LOMAH (supersonic + subsonic). This dual-mode capability is their primary competitive advantage.

---

## 2. PRODUCT FAMILY OVERVIEW

```
TTS Electronic Scoring Portfolio
│
├── LOMAH (Open-Air) ←── Supersonic only (≥ Mach 1.3)
│   ├── Infantry LOMAH (on SIT lifter)
│   ├── Armor LOMAH (on SAT mechanism)
│   └── Moving Target LOMAH (on rail/cable system)
│
├── Box Target (Chambered LOMAH) ←── Supersonic + Subsonic
│   └── AMS / Kammerziel variants
│
├── Range Control
│   ├── TACF (computerized control facility)
│   ├── Range Control Tablet (handheld)
│   ├── Shooter's Monitor (per-lane display)
│   └── Range Control Vehicle (mobile, 60+ hr autonomy)
│
└── Target Mechanisms (host platforms)
    ├── THEISSEN-Cube (SIT lifter/turner)
    ├── Known Distance Targets
    ├── Turning Targets (360°, <1 sec, up to 5 kg)
    └── Moving Infantry/Armor Targets (rail/cable/self-propelled)
```

---

## 3. SYSTEM ARCHITECTURE

### 3.1 Overall Range Architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│                     TTS RANGE SYSTEM TOPOLOGY                         │
│                                                                       │
│  TARGET END (×N Lanes)                                                │
│  ┌────────────────────────┐                                           │
│  │ Target Mechanism        │                                          │
│  │ (SIT/Turning/Moving)    │     Ethernet (CAT 5e/6)                  │
│  │  ┌──────────────────┐  │     TCP/IP (IPv4 + IPv6 ready)           │
│  │  │ LOMAH Sensor Bar  │  │◄──────────────────────┐                  │
│  │  │ (2× delta arrays) │  │                       │                  │
│  │  └──────────────────┘  │                       │                  │
│  │  ┌──────────────────┐  │                       │                  │
│  │  │ Target Controller │  │     FASIT Protocol    │                  │
│  │  │ (TC)              │──┤◄────────────────────┐│                  │
│  │  └──────────────────┘  │                     ││                  │
│  └────────────────────────┘                     ││                  │
│         OR                                       ││                  │
│  ┌────────────────────────┐                     ││                  │
│  │ Box Target              │                     ││                  │
│  │  ┌──────────────────┐  │                     ││                  │
│  │  │ 2× Delta Sensor  │  │                     ││                  │
│  │  │ Arrays in Chamber │  │◄────────────────────┘│                  │
│  │  └──────────────────┘  │                      │                  │
│  │  ┌──────────────────┐  │                      │                  │
│  │  │ Rubber Membrane  │  │                      │                  │
│  │  │ (self-sealing)    │  │                      │                  │
│  │  └──────────────────┘  │                      │                  │
│  └────────────────────────┘                      │                  │
│                                                   │                  │
│  CONTROL END                                      │                  │
│  ┌────────────────────────┐    ┌─────────────────┴───────────┐      │
│  │ Shooter's Monitor       │    │ TACF (Control Facility)      │      │
│  │ (per-lane display)      │◄───┤ - Dual screen               │      │
│  │ - X,Y coordinates       │    │ - Screen 1: Range layout     │      │
│  │ - Graphical hit plot    │    │ - Screen 2: Controls/flowchart│     │
│  │ - Score                 │    │ - Up to 1024 targets managed │      │
│  └────────────────────────┘    │ - Fire area editor           │      │
│                                │ - Personnel management       │      │
│  ┌────────────────────────┐    └──────────────────────────────┘      │
│  │ Range Control Tablet    │         OR                               │
│  │ (mobile/handheld)       │    ┌──────────────────────────────┐     │
│  │ - Backlit keyboard      │    │ Range Control Vehicle         │     │
│  │ - Long-range RF         │    │ - Detachable cabin            │     │
│  │ - Touchscreen GUI       │    │ - 60+ hours autonomous        │     │
│  └────────────────────────┘    │ - Same TACF software           │     │
│                                └──────────────────────────────┘      │
└───────────────────────────────────────────────────────────────────────┘
```

### 3.2 Communication Protocol Stack

```
┌───────────────────────────────┐
│  Application Layer             │
│  FASIT Protocol                │
│  (Target commands, scoring     │
│   data, status, diagnostics)   │
├───────────────────────────────┤
│  Transport Layer               │
│  TCP (reliable delivery)       │
├───────────────────────────────┤
│  Network Layer                 │
│  IPv4 / IPv6-ready             │
├───────────────────────────────┤
│  Data Link / Physical          │
│  Ethernet 100BaseT             │
│  CAT 5e/6 cabling              │
├───────────────────────────────┤
│  Alternative (field/mobile):   │
│  RF (VHF/UHF) or WiFi          │
└───────────────────────────────┘
```

**FASIT compliance** is critical - it is the US Army standard (Future Army System of Integrated Targets) that defines:
- Two-way communication between Target Controllers and TACF
- Standard command/response message formats
- Common benchmarks for function and conventions
- Interoperability with any FASIT-compliant range

---

## 4. LOMAH SENSOR BAR (Open-Air) - DETAILED ANALYSIS

### 4.1 Sensor Configuration

```
                    LOMAH SENSOR BAR (Top View)
    ┌──────────────────────────────────────────────────┐
    │                                                    │
    │   DELTA ARRAY A              DELTA ARRAY B         │
    │                                                    │
    │       [S1]                       [S4]              │
    │       / \                        / \               │
    │      /   \                      /   \              │
    │     /     \                    /     \             │
    │   [S2]───[S3]               [S5]───[S6]           │
    │                                                    │
    │   ◄── Set distance between arrays ──►             │
    │                                                    │
    │   4 sensors per array × 2 arrays = 8 sensors      │
    │   (source: "two delta arrays, each with            │
    │    four sensors")                                  │
    └──────────────────────────────────────────────────┘
                        │
                  Mounted on bar below target face
                  (below lifter height for ballistic protection)
```

**Key insight:** TTS uses **two separate delta arrays on a bar** rather than a single array. Each delta array has **4 sensors** (not 3). This dual-array approach provides:

1. **Redundancy** - Either array can independently estimate position
2. **Directional vectors** - Each array produces a bearing; intersection = position
3. **Velocity estimation** - Time difference between arrays gives projectile speed

### 4.2 Detection Principle (TTS-Specific)

```
    Bullet trajectory (supersonic, ≥ Mach 1.3)
    ════════════════════════════════════════════►
                    │
         Mach cone  │╲
                    │  ╲ θ = arcsin(c/v)
                    │    ╲
    ────────────────┼──────╲───────────────── Sensor bar plane
    [Delta A]       │       ╲   [Delta B]
    Records TDOA    │        ╲  Records TDOA
    → Direction A   │         ╲ → Direction B
                    │          ╲
    Intersection of directional vectors = (X, Y) position
```

**TTS method:** Each delta array records time differences → computes a **directional vector** toward the projectile path. The two vectors from Array A and Array B **intersect** to give the (X,Y) coordinate. This is more robust than single-array TDOA alone.

### 4.3 Specifications

| Parameter | TTS LOMAH | Notes |
|-----------|-----------|-------|
| **Sensor type** | Microphones (MEMS, likely) | Detects supersonic shockwave |
| **Min velocity** | Mach 1.3 (~440 m/s) | Higher threshold than some competitors |
| **Detection angle** | ±20° azimuth, ±5° elevation | Defines valid engagement cone |
| **Sensor config** | 2× delta arrays, 4 sensors each | 8 total sensors per bar |
| **Scoring display** | Graphical + Cartesian (X,Y) | Instant feedback |
| **Auto-fire handling** | Yes | Resolves overlapping rounds |
| **BIT (diagnostics)** | Built-in | Firmware, voltage, errors, maintenance |
| **FASIT compliant** | Yes | US Army interoperability |
| **Integration** | Infantry, armor, any vendor's lifter | Retrofit-capable |

---

## 5. BOX TARGET (Chambered LOMAH) - DETAILED ANALYSIS

This is TTS's **unique differentiator** - no equivalent in Zen Technologies' lineup.

### 5.1 Architecture

```
         CROSS-SECTION: TTS BOX TARGET

    ─────── Incoming projectile ──────►

    ┌──────────────────────────────────────────┐
    │  Self-sealing rubber membrane (front)     │ ← Bullet passes through
    ├──────────────────────────────────────────┤
    │                                          │
    │        ENCLOSED CHAMBER                  │
    │        (wooden frame)                    │
    │                                          │
    │   [Delta Array A]     [Delta Array B]    │ ← Pair of sensor arrays
    │       (3 sensors)         (3 sensors)    │    in delta format
    │                                          │
    │   ◄── set distance between arrays ──►   │
    │                                          │
    │   Shockwave reverberates inside chamber  │
    │   → Sensors detect arrival times         │
    │   → Calculate position                   │
    │                                          │
    ├──────────────────────────────────────────┤
    │  Self-sealing rubber membrane (rear)      │ ← Bullet exits
    └──────────────────────────────────────────┘

    Also known as: AMS, Chambered LOMAH, Kammerziel
```

### 5.2 How It Handles Subsonic Projectiles

| | Open-Air LOMAH | Box Target (Chambered) |
|---|---|---|
| **Detection source** | Mach cone shockwave in open air | Impact sound through rubber + shockwave inside chamber |
| **Works subsonic?** | NO (needs Mach >1.3) | YES |
| **Works supersonic?** | YES | YES |
| **Wind interference** | Significant (degrades accuracy) | **ZERO** (enclosed chamber) |
| **Mechanism** | Shockwave triangulation | Rubber impact + enclosed acoustic chamber |

**The rubber membrane serves three functions:**
1. **Acoustic trigger** - Bullet impact creates detectable sound even for subsonic rounds
2. **Wind isolation** - "Zero-wind interference detection"
3. **Self-sealing** - Minor tears close automatically; larger holes patchable with rubber patches or gaffer tape

### 5.3 Box Target Specifications

| Parameter | TTS Box Target |
|-----------|---------------|
| **Detection method** | Enclosed acoustic chamber + rubber membrane |
| **Sensor config** | 2× delta arrays (3 sensors each), set distance apart |
| **Supersonic** | Yes |
| **Subsonic** | Yes (.22 LR, 9mm, air weapons capable) |
| **Wind immunity** | Complete (enclosed) |
| **Operating temp** | -25°C to +65°C |
| **Environmental** | Waterproof, dustproof, extreme conditions |
| **Frame material** | Wood |
| **Membrane** | Self-sealing rubber |
| **Lift time** | 5-8 seconds (motorized, gearbox + chain) |
| **Scoring output** | Graphical + Cartesian (X,Y) |
| **Diagnostics** | Built-in self-test |
| **Maintenance** | Rubber patches / gaffer tape for membrane |

---

## 6. RANGE CONTROL SYSTEM (TACF)

### 6.1 Software Capabilities

| Feature | Specification |
|---------|--------------|
| **Max targets managed** | 1,024 systems |
| **Display** | Dual-screen (range layout + controls/flowchart) |
| **Fire area editor** | Custom fire zones on range map |
| **Personnel management** | Instructor/student database with history |
| **Exercise programming** | Pre-defined + custom flowcharts |
| **Scoring** | Real-time graphical + Cartesian |
| **Platforms** | Desktop PC, tablet (touchscreen), mobile vehicle |

### 6.2 Control Hierarchy

```
    TACF (Master)
      │
      ├──► Target Controller (TC) per lane ──► Target mechanism (lift/turn/move)
      │                                         └──► LOMAH sensor bar OR Box Target
      │
      ├──► Shooter's Monitor (per lane, display only)
      │
      └──► Range Control Tablet (instructor, mobile)
              └──► RF link for field operation
```

---

## 7. TARGET MECHANISM: THEISSEN-Cube

| Feature | Specification |
|---------|--------------|
| **Functions** | Lift, slash, turn infantry silhouettes |
| **Controller** | External Target Controller (TC) |
| **Communication** | TC <-> TACF (Ethernet/FASIT) or TC <-> RCU (Remote Control Unit) |
| **Target weight** | Up to 5 kg |
| **Rotation** | 360° independent |
| **Rotation speed** | < 1 second |
| **Hit sensor** | Contact-based, adjustable sensitivity |
| **Options** | Illumination (visible + IR), muzzle flash simulator, police light, ballistic shield |
| **Installation** | Ground or ceiling mount, portable or fixed |

---

## 8. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

```
┌─────────────────────────────────────────────────────────────────────┐
│  OVERALL FUNCTION: "Detect, score and report projectile impact      │
│                     for live-fire training range"                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  F1: Detect projectile        F2: Compute position                  │
│  ┌────────────────────┐      ┌────────────────────┐                │
│  │ F1.1a Open-air:     │      │ F2.1 TDOA from each│                │
│  │   Sense Mach cone   │      │      delta array   │                │
│  │ F1.1b Chambered:    │      │ F2.2 Directional   │                │
│  │   Sense rubber impact│      │      vector calc   │                │
│  │ F1.2 Filter/amplify │      │ F2.3 Vector inter- │                │
│  │ F1.3 Digitize (ADC) │      │      section -> X,Y│                │
│  └────────────────────┘      │ F2.4 Temp compensate│                │
│                               └────────────────────┘                │
│                                                                     │
│  F3: Present target           F4: Control range                     │
│  ┌────────────────────┐      ┌────────────────────┐                │
│  │ F3.1 Lift/lower     │      │ F4.1 FASIT protocol│                │
│  │ F3.2 Turn (360°)    │      │ F4.2 Up to 1024    │                │
│  │ F3.3 Move (rail/    │      │      targets       │                │
│  │      cable/self)    │      │ F4.3 Exercise prog  │                │
│  │ F3.4 Illuminate     │      │ F4.4 Fire area mgmt│                │
│  │ F3.5 Flash simulate │      │ F4.5 Personnel DB  │                │
│  └────────────────────┘      └────────────────────┘                │
│                                                                     │
│  F5: Report results           F6: Withstand environment             │
│  ┌────────────────────┐      ┌────────────────────┐                │
│  │ F5.1 Shooter monitor│      │ F6.1 -25°C to +65°C│                │
│  │ F5.2 TACF display   │      │ F6.2 IP-rated seal │                │
│  │ F5.3 Score/rate     │      │ F6.3 Ballistic prot│                │
│  │ F5.4 Log/record     │      │ F6.4 Self-sealing  │                │
│  │ F5.5 BIT diagnostics│      │      membrane      │                │
│  └────────────────────┘      └────────────────────┘                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 9. RELEVANT PATENT: US6109614A (Acoustic Projectile Sensing)

This public-domain patent reveals the mathematical core applicable to all LOMAH systems:

| Patent Detail | Specification |
|--------------|--------------|
| **Sensor geometry** | 5 sensors in diamond + 1 orthogonal (32" x 32" area) |
| **Sampling rate** | 2.765 MHz (360 ns resolution) |
| **Accuracy achieved** | 0.038" (~1mm) RMS within 6" radius |
| **Method** | Two planar-orthogonal channels for (X,Y) + one cross-orthogonal for velocity |
| **Signal analysis** | Rise-time, peak amplitude, FWHH, decay profile |
| **Calibration** | Non-linear multi-order correction transform matrix |
| **Communication** | RF 902-928 MHz (ISM band) |
| **Architecture** | Microcontroller at target + CDU at firing point |

**Key equations from patent:**
```
Position determination:
  - Horizontal TDOA → X coordinate
  - Vertical TDOA → Y coordinate
  - Cross-orthogonal TDOA → Velocity = sensor_spacing / Δt

Calibration transform:
  - Translation, rotation, scale extent corrections
  - Weighted off-field correction terms
  - Non-linear multi-order cross-detection field correction
```

---

## 10. COMPARATIVE ANALYSIS: TTS vs. ZEN vs. InVeris

| Parameter | TTS (Germany) | Zen (India) | InVeris (USA) |
|-----------|--------------|-------------|---------------|
| **LOMAH open-air** | Yes | Yes | Yes |
| **Subsonic scoring** | Yes (Box Target) | No | No (standard) |
| **Sensor config** | 2× delta (4 sensors each) | Single array on frame | Single bar array |
| **Min velocity** | Mach 1.3 (440 m/s) | Supersonic (~340+ m/s) | 450 m/s |
| **Wind immunity option** | Yes (Box Target) | No | No |
| **FASIT compliant** | Yes | No | Yes |
| **Max targets/range** | 1,024 | Not published | Not published |
| **Operating temp** | -25°C to +65°C | Est. MIL-STD | -25°C to +70°C |
| **Accuracy** | Not published | Est. +/-5mm | <5mm radial |
| **Armor targets** | Yes (SAT, MAT) | Yes | Yes |
| **Diagnostics (BIT)** | Yes | Not published | Yes |
| **Retrofit to other lifters** | Yes (any vendor) | Proprietary | Yes |
| **IPv6 ready** | Yes | Not published | Not published |
| **Autonomous mobile control** | 60+ hrs (vehicle) | MCS | Not published |
| **Production location** | DE, BE, US | India | USA |
| **Est. cost/lane** | High (EUR EUR EUR) | Medium ($$) | High ($$$) |

---

## 11. KEY DESIGN INSIGHTS FOR INDIGENOUS DEVELOPMENT

### 11.1 What TTS Does Better (Lessons to Adopt)

| Innovation | Engineering Principle | Benefit |
|-----------|----------------------|---------|
| **Dual delta arrays** | Redundancy + directional intersection | Better accuracy, fault tolerance |
| **Box Target (chambered)** | Enclosed acoustic chamber | Subsonic + wind immunity |
| **Self-sealing rubber** | Elastomeric material science | Low maintenance consumable |
| **FASIT compliance** | Standardized protocol | Export market access (US Army) |
| **BIT diagnostics** | Built-in test | Field maintainability |
| **1,024 target scalability** | Software architecture | Large range support |
| **Retrofit-compatible** | Open mechanical interface | Market flexibility |

### 11.2 TTS Vulnerabilities (Opportunities for Vietnamese Product)

| Weakness | Opportunity |
|----------|-------------|
| High European production cost | **Cost advantage** at <=70% |
| No LoRa/wireless scoring option | Add **wireless** (like ShotMarker) |
| Rubber membrane is consumable | Develop longer-life or **local rubber** (VN is #3 rubber producer globally) |
| Wood frame (rot, termite risk in tropics) | Use **aluminum or composite** |
| No published IP rating for LOMAH | Design for **IP67** from start |
| No solar/battery power option | Add **off-grid power** for field use |

---

## 12. BILL OF MATERIALS ESTIMATE (Vietnamese Box Target Variant)

### 12.1 Per-Lane Box Target Unit

| Component | Description | Sourcing (VN) | Est. Cost |
|-----------|-------------|---------------|-----------|
| MEMS microphones (x6) | High-SPL, 2 delta arrays | Import (TDK/Knowles) | $12-30 |
| Temperature sensor | DS18B20 digital | Import (commodity) | $1-2 |
| MCU/DSP | STM32H7 (2x ADC, timers) | Import | $10-25 |
| Analog frontend (x6 ch) | Op-amp, BPF, AGC per channel | Mixed | $8-15 |
| Ethernet PHY + PoE | 100BaseT, 802.3af | Import | $5-10 |
| **Rubber membrane** | **Natural rubber sheet** | **Local** (VN rubber) | **$5-10** |
| Chamber frame | Aluminum extrusion (not wood) | **Local** (Hoa Phat) | $25-45 |
| Sensor mounting brackets | CNC aluminum | **Local** machining | $10-20 |
| Lifting mechanism | 12V motor + gearbox + chain | **Local**/import | $30-60 |
| PCB + IP67 enclosure | Custom PCB, sealed housing | **Local** PCB fab | $15-25 |
| Cabling + connectors | CAT6 + IP67 connectors | **Local**/import | $5-10 |
| **Subtotal per lane** | | | **$125-250** |

### 12.2 Local Content Analysis

| Category | Local Value | Import Value | Local % |
|----------|------------|-------------|---------|
| Mechanical (frame, rubber, lifter, brackets) | $70-135 | $0 | **100%** |
| Electronics (PCB, passive) | $15-25 | $35-80 | ~25% |
| Rubber membrane (VN natural rubber) | $5-10 | $0 | **100%** |
| Software/firmware | $0 (labor) | $0 | **100%** |
| **Overall by value** | | | **~58-68%** |

Vietnam's position as the **world's #3 natural rubber producer** gives a unique advantage for the self-sealing membrane - a recurring consumable that generates aftermarket revenue.

---

## 13. ASSESSMENT SUMMARY

### Strengths
- Dual-mode scoring (supersonic + subsonic) is unique competitive advantage
- FASIT compliance opens US/NATO market
- Box Target eliminates wind interference completely
- Mature product ecosystem (10+ product types)
- Retrofit-compatible with any vendor's target mechanisms
- Proven in US Army service (LTRaC MAC-3 contract)
- Scalable software architecture (1,024 targets)

### Weaknesses
- High European cost structure
- Wood frame not optimal for tropical environments
- Rubber membrane is consumable (recurring cost to customer)
- No wireless/LoRa scoring option
- No published IP rating for open-air LOMAH
- No solar/off-grid power option

### Relevance to Vietnamese Development
- Box Target concept is highly relevant (VN has rubber supply chain advantage)
- FASIT protocol study essential for export potential
- Dual delta array design is superior to single-array (adopt this approach)
- Aluminum frame adaptation straightforward for Vietnamese manufacturers
- Software architecture (TACF) can be developed locally
- Total system cost reduction of 50-60% achievable with local production

---

## 14. RECOMMENDED DESIGN STRATEGY

Based on analyzing both Zen (India) and TTS (Germany):

```
RECOMMENDED VIETNAMESE PRODUCT CONCEPT
=======================================

  "Dual-Mode Smart Electronic Target"

  ┌─────────────────────────────────┐
  │  MODE 1: Open-Air LOMAH         │ <- Supersonic (5.56, 7.62)
  │  (Sensor bar, 2× delta arrays)  │
  ├─────────────────────────────────┤
  │  MODE 2: Chambered (Box) Target │ <- Subsonic + Supersonic
  │  (Vietnamese rubber membrane)    │    (9mm, .22, + all above)
  ├─────────────────────────────────┤
  │  INNOVATIONS vs. IMPORTS:        │
  │  + Wireless (LoRa) option        │
  │  + Solar/battery field power     │
  │  + Aluminum frame (tropical)     │
  │  + Vietnamese rubber consumables │
  │  + FASIT-compatible protocol     │
  │  + IP67 standard                 │
  └─────────────────────────────────┘

  Target: <=70% cost of TTS/InVeris import
  Local content: >=60%
```

---

*Analysis based entirely on publicly available information (product brochures, published specifications, academic papers, patents, competitor datasheets).*
*The detection principle (TDOA-based acoustic shockwave triangulation) is well-established physics, not proprietary.*
*Patent US6109614A referenced for mathematical framework (filed 2000).*
