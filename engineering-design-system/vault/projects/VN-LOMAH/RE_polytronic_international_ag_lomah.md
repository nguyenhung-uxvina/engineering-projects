---
project: VN-LOMAH
phase: 0
type: reverse-engineering
subject: Polytronic International AG LOMAH (Switzerland)
version: 1.0
created: 2026-02-06
status: complete
---

# RE: Polytronic International AG LOMAH - Switzerland
## Reverse Engineering Analysis from Public Sources

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Polytronic International AG |
| **HQ** | Pilatusstrasse 12, 5630 Muri, Aargau, Switzerland |
| **Founded** | 1966 by Claude Thalmann (ETH/SIA physicist) |
| **Key milestone** | Invented the world's first automatic marking system (1969) |
| **Current CEO** | Markus Huwyler (since 2024) |
| **Owner** | Christoph Koch (since 2013) |
| **Subsidiary** | Polytronic UAE (est. 2016) |
| **Certifications** | ISO 9001, ISO 14001, ISO 45001 |
| **Website** | https://www.polytronic.ch |
| **Contact** | +41 56 675 99 11 / info@polytronic.ch |

**Key differentiator:** Polytronic is the **inventor of electronic scoring** (1966) and the **only manufacturer offering radar-based subsonic LOMAH** (I-Bar). Combined with their AROS software platform and semi-autonomous robotic targets, they represent the most technologically advanced product ecosystem in the market.

### Company Timeline

| Year | Milestone |
|------|-----------|
| 1966 | Founded in Zurich by Claude Thalmann |
| 1969 | World's first automatic marking system (patent filed) |
| 1976 | First international CISM competition use (Thun) |
| 1978 | Equipped 42nd Shooting World Cup (Seoul) |
| 1982 | Established Polytronic International AG |
| 1986 | Entered defense market with military targets |
| 1990 | Largest contract: Swiss Army |
| 1993 | Middle East market (sniper training) |
| 2002 | Acquired Australian Defence Industries IP |
| 2006 | European market via Norway live-fire range |
| 2007 | Released TG 6000 electronic scoring generation |
| 2016 | Launched AROS software; UAE subsidiary; biggest live-fire range project |
| 2021 | Semi-autonomous robotic targets introduced |
| 2024 | TG 6302 target system launched |

---

## 2. PRODUCT FAMILY OVERVIEW

```
Polytronic International AG - Complete Portfolio
│
├── LOMAH (Electronic Scoring)
│   ├── H-Bar LOMAH (TG 4020) ←── Supersonic, multi-angle capable
│   ├── T-Bar LOMAH ←── Supersonic, perpendicular fire only
│   ├── I-Bar LOMAH (Subsonic) ←── WORLD FIRST: Radar-based, 9mm capable
│   ├── TG 4040 Pistol LOMAH ←── Radar, zonal scoring, subsonic
│   └── TG 4002 Box Target ←── Enclosed sensor array, all-weather
│
├── Static Targets (TG 82 Series)
│   ├── TG 82-70 Single Pop-up ←── Supersonic + subsonic LOMAH
│   ├── TG 82-70 BRP (Mobile/pop-up) ←── 30 kg, IP67, Li-ion battery
│   ├── TG 82 Infantry (pop-up + rotary)
│   └── TG 82-40 Armour (up to full tank flank)
│
├── Portable Targets
│   ├── PITS (Portable Infantry Target System) ←── UHF + WiFi, battery
│   ├── Confined Space Target (rotary module)
│   ├── Bagman (fan-inflated, auto-deflate)
│   └── TG 82-70 Sniper Portable ←── Battery + supersonic LOMAH
│
├── Moving Targets
│   ├── Lateral Movers (adjustable speed/exposure)
│   ├── Oblique Moving Target (curved rail, self-driven)
│   ├── Moving Armour (diesel or battery)
│   └── TG 94 Retrievable Target System
│
├── Robotic Targets (Semi-Autonomous)
│   ├── RT-CQB ←── Compact, collapsible, indoor CQB
│   ├── RT-M ←── Flagship, LIDAR + GPS, semi-autonomous
│   └── RT-M6 ←── Extended platform, tracked option
│
├── Range Control
│   ├── AROS (Advanced Range Operating Software)
│   └── IVDU (Intelligent Visual Display Unit)
│
├── Sport & Hunting Scoring
│   ├── TG 3000 Electronic Scoring
│   ├── TG 6000 Electronic Scoring
│   └── TG 6302 (latest, 2024)
│
└── Accessories
    ├── Sound Simulator
    ├── Hostile Fire Simulator
    └── Target illumination (moonlight, IR)
```

---

## 3. LOMAH PRODUCT LINE - DETAILED ANALYSIS

### 3.1 LOMAH Variants Comparison

| Feature | H-Bar (TG 4020) | T-Bar | I-Bar (Subsonic) | TG 4040 Pistol | TG 4002 Box |
|---------|-----------------|-------|-------------------|----------------|-------------|
| **Detection** | Acoustic | Acoustic | **Radar** | **Radar** | Acoustic (enclosed) |
| **Supersonic** | Yes | Yes | No | No | Yes |
| **Subsonic** | No | No | **Yes (9mm)** | **Yes (9mm)** | Yes |
| **Multi-angle** | **Yes** | No (perpendicular only) | N/A | N/A | N/A |
| **Scoring type** | X,Y coordinate | X,Y coordinate | Shot location | **Zonal** | X,Y coordinate |
| **Moving targets** | Yes | No | N/A | Combined w/ H-Bar | No |
| **Enclosure** | Open-air | Open-air | N/A | N/A | **Sealed aluminium** |
| **Weather immune** | No | No | N/A | N/A | **Yes** |
| **Use case** | Primary military LOMAH | Basic marksmanship | Pistol/SMG training | Weapon transition drills | Indoor/outdoor |

### 3.2 H-Bar LOMAH (TG 4020) - Primary Product

```
                    H-BAR LOMAH SENSOR CONFIGURATION
    ┌──────────────────────────────────────────────────────┐
    │                                                        │
    │   H-shaped sensor array (more sensors than T-Bar)      │
    │                                                        │
    │   [S1]─────────────[S2]                                │
    │        │                                               │
    │        │  (vertical bar)                               │
    │        │                                               │
    │   [S3]─┼─────────[S4]                                  │
    │        │                                               │
    │        │  (vertical bar)                               │
    │        │                                               │
    │   [S5]─────────────[S6]                                │
    │                                                        │
    │   Multiple sensors on H-frame enable:                  │
    │   - Perpendicular fire detection                       │
    │   - Angled fire detection (±XX degrees)                │
    │   - Moving target engagement                           │
    └──────────────────────────────────────────────────────┘

    Dimensions: 1200mm x 450mm (L x W)
    Weight: ~10 kg
```

**Specifications (H-Bar / TG 4020):**

| Parameter | Specification |
|-----------|--------------|
| **Detection method** | Acoustic - supersonic shockwave |
| **Sensor config** | H-shaped array (more sensors than T-Bar) |
| **Accuracy** | +/- 5mm in center scoring area |
| **Min projectile velocity** | 350 m/s (1,150 fps) at target |
| **Dimensions** | 1200mm x 450mm (L x W) |
| **Weight** | ~10 kg |
| **Power** | Rechargeable battery (6+ hours runtime) |
| **Radio range** | Line of sight, >2,000 m |
| **Radio frequency** | 400-470 MHz (standard, from TG 82-70 spec) |
| **IP rating** | IP67 (from TG 82 platform spec) |
| **Fire angles** | Perpendicular + angled fire |
| **Moving targets** | Compatible |
| **Display** | IVDU + AROS |
| **Battery pack** | AC005v3 detachable, 12Vdc |
| **Integration** | M3200M Pop-Up mechanism; AC120 or AC114 frames |

**Key advantage over competitors:** The H-Bar's lower minimum velocity (350 m/s vs. InVeris 450 m/s and TTS 440 m/s) means it can detect bullets that have decelerated more, extending effective range for long-range marksmanship.

### 3.3 T-Bar LOMAH

| Parameter | Specification |
|-----------|--------------|
| **Detection method** | Acoustic - supersonic shockwave |
| **Sensor config** | T-shaped array (fewer sensors than H-Bar) |
| **Fire angle** | Perpendicular only |
| **Accuracy** | +/- 5mm (estimated, same technology) |
| **Min velocity** | 350 m/s (1,150 fps) |
| **Use case** | Fixed-distance ranges, basic marksmanship |
| **Limitation** | Cannot detect angled fire |

### 3.4 I-Bar LOMAH (Subsonic) - WORLD FIRST

```
┌──────────────────────────────────────────────────────────┐
│                                                            │
│    I-BAR LOMAH: RADAR-BASED SUBSONIC DETECTION             │
│                                                            │
│    Unlike ALL other LOMAH systems that rely on             │
│    acoustic shockwave (requires supersonic bullet),        │
│    the I-Bar uses RADAR TECHNOLOGY to detect               │
│    subsonic projectiles.                                   │
│                                                            │
│    ┌─────────────────┐                                     │
│    │  Radar Emitter/  │                                    │
│    │  Receiver Array  │                                    │
│    │                  │  Radar beam detects passing         │
│    │  ~~~~radar~~~~►  │  projectile regardless of speed     │
│    │                  │                                     │
│    │  Subsonic bullet │                                     │
│    │  (9mm, .45, etc) │  No shockwave needed!              │
│    │  ══════════════► │                                     │
│    └─────────────────┘                                     │
│                                                            │
│    Provides shot LOCATION for subsonic ammo including:     │
│    - 9mm pistol                                            │
│    - .45 ACP                                               │
│    - .22 LR subsonic                                       │
│    - Other subsonic rounds                                 │
│                                                            │
│    Can be combined with H-Bar or T-Bar for weapon          │
│    transition drills (rifle supersonic → pistol subsonic)  │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

| Parameter | Specification |
|-----------|--------------|
| **Detection method** | **Radar technology** (world first) |
| **Supersonic** | No (use H-Bar/T-Bar for that) |
| **Subsonic** | **Yes** - including 9mm |
| **Scoring type** | Shot location |
| **Combined use** | Pairs with H-Bar or T-Bar for weapon transition drills |
| **Innovation level** | Unique - no other LOMAH manufacturer offers radar-based subsonic |

### 3.5 TG 4040 Pistol LOMAH

| Parameter | Specification |
|-----------|--------------|
| **Detection method** | **Radar technology** |
| **Scoring type** | **Zonal scoring** (not full X,Y coordinate) |
| **Subsonic capable** | Yes (9mm pistol ammunition) |
| **Combined use** | Can couple with H-Bar for concurrent primary/secondary weapon drills |
| **Innovation** | World first pistol LOMAH with radar |

### 3.6 TG 4002 Box Target

| Parameter | Specification |
|-----------|--------------|
| **Construction** | Target box with enclosed sensor array |
| **Enclosure** | Sealed aluminium case |
| **Accuracy** | "Exceptional accuracy for small arms" |
| **Indoor/outdoor** | Both (sealed electronics) |
| **Weather immune** | Yes (enclosed sensors unaffected by weather) |
| **Subsonic** | Yes (enclosed chamber design) |
| **Supersonic** | Yes |
| **Integration** | AROS + IVDU |
| **Portable option** | Can be used as fixed or portable |
| **Comparison** | Similar concept to TTS Box Target / Chambered LOMAH |

---

## 4. SYSTEM ARCHITECTURE

### 4.1 Overall Range Topology

```
┌──────────────────────────────────────────────────────────────────────────┐
│                  POLYTRONIC RANGE SYSTEM TOPOLOGY                        │
│                                                                          │
│  TARGET END (Per Lane)                                                   │
│  ┌───────────────────────────┐                                           │
│  │ Target Mechanism           │                                          │
│  │ (TG 82-70 / TG 82-40)     │                                          │
│  │  ┌─────────────────────┐  │     Radio 400-470 MHz                    │
│  │  │ LOMAH Sensor         │  │     OR Wired/WiFi                        │
│  │  │ (H-Bar/T-Bar/I-Bar/ │  │◄────────────────────┐                   │
│  │  │  Box Target)         │  │                     │                   │
│  │  └─────────────────────┘  │                     │                   │
│  │  ┌─────────────────────┐  │                     │                   │
│  │  │ Contact Hit Sensor   │  │                     │                   │
│  │  │ (15-level sensitivity│  │                     │                   │
│  │  │  adjustable)         │  │                     │                   │
│  │  └─────────────────────┘  │                     │                   │
│  │  ┌─────────────────────┐  │                     │                   │
│  │  │ Illumination         │  │                     │                   │
│  │  │ (moonlight, hit,     │  │                     │                   │
│  │  │  retaliatory fire)   │  │                     │                   │
│  │  └─────────────────────┘  │                     │                   │
│  └───────────────────────────┘                     │                   │
│         AND/OR                                      │                   │
│  ┌───────────────────────────┐                     │                   │
│  │ Robotic Target (RT-M)      │                     │                   │
│  │ - LIDAR + GPS navigation   │                     │                   │
│  │ - Semi-autonomous          │                     │                   │
│  │ - Obstacle avoidance       │                     │                   │
│  │ - 7.62mm ballistic rated   │                     │                   │
│  │ - Zonal shot detection     │                     │                   │
│  └───────────────────────────┘                     │                   │
│                                                     │                   │
│  FIRER'S END (Per Lane)                             │                   │
│  ┌───────────────────────────┐                     │                   │
│  │ IVDU (Intelligent Visual   │                     │                   │
│  │ Display Unit)              │◄────────────────────┤                   │
│  │ - Non-glare LCD screen     │                     │                   │
│  │ - Toughened glass          │                     │                   │
│  │ - Tactile buttons          │                     │                   │
│  │ - Shot location display    │                     │                   │
│  │ - Sight adjustment info    │                     │                   │
│  │ - Scoring display          │                     │                   │
│  │ - Lane Initiator (built-in)│                     │                   │
│  └───────────────────────────┘                     │                   │
│                                                     │                   │
│  CONTROL CENTER                                     │                   │
│  ┌──────────────────────────────────────────────────┴──────────────┐   │
│  │ AROS (Advanced Range Operating Software)                         │   │
│  │ - Multi-lingual (instant language switching)                     │   │
│  │ - Scales from infantry section to Combined Arms exercises        │   │
│  │ - Interactive AAR (After Action Review) with force positions     │   │
│  │ - Drag-and-drop CQB range configuration                         │   │
│  │ - Seamless integration: static + portable + moving + robotic     │   │
│  │ - Third-party system integration via flexible comm layer         │   │
│  │ - Platforms: server, commercial tablet, Polytronic tablet        │   │
│  │ - Wired or wireless communication                                │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Communication Architecture

```
┌────────────────────────────────────────┐
│  Communication Options                  │
│                                         │
│  WIRELESS:                              │
│  ├── UHF Radio (400-470 MHz standard)   │
│  ├── WiFi (for portable/CQB targets)    │
│  └── Radio range: >2,000 m LOS          │
│                                         │
│  WIRED:                                 │
│  └── State-of-the-art (unspecified)     │
│                                         │
│  SOFTWARE:                              │
│  ├── AROS proprietary protocol          │
│  └── Third-party integration capable    │
│       (flexible communication layer)    │
└────────────────────────────────────────┘
```

---

## 5. TARGET MECHANISM: TG 82-70 BRP (Detailed Specs)

This is the primary host platform for LOMAH systems.

| Parameter | Specification |
|-----------|--------------|
| **Min protection height** | 330mm |
| **Weight** | 30 kg |
| **Max targets** | Up to 3 targets (500x1200mm each) |
| **Target weight** | 2.5 kg (single), 5 kg (double), 7 kg (triple) |
| **Reaction time** | <1 second (no wind); up to 3 sec with wind |
| **Hit detection** | 1,200 rounds/minute |
| **Hit sensor** | Contact Hit Sensor, 15-level adjustable sensitivity |
| **Wind resistance** | 72 km/h (single), 50 km/h (double), 40 km/h (triple) |
| **Battery** | 25.2 VDC / 4.4 Ah Li-Ion |
| **Battery life** | ~700 operations (max single target) |
| **IP rating** | **IP67** |
| **Operating temp** | -25°C to +50°C |
| **Radio frequency** | 400-470 MHz standard |
| **Radio reliability** | 98% |
| **Built-in lights** | Moonlight, hit on target, retaliatory fire simulation |
| **LOMAH** | Fits supersonic AND subsonic LOMAH |
| **Built to** | Military standards (MIL-STD) |

---

## 6. IVDU (Intelligent Visual Display Unit)

| Feature | Detail |
|---------|--------|
| **Screen** | Non-glare LCD |
| **Protection** | Toughened glass (against ejected casings) |
| **Controls** | Tactile buttons (operable in harsh conditions) |
| **Response time** | Displays fall of shot "within milliseconds" |
| **Features** | Sight adjustment info, shot location, scoring |
| **Lane Initiator** | Integrated (prevents cross-lane firing) |
| **Comparison** | Equivalent to InVeris FPC but with integrated Lane Initiator |

---

## 7. AROS (Advanced Range Operating Software)

| Feature | Specification |
|---------|--------------|
| **Launched** | 2016 |
| **Scalability** | From infantry section 100m drill to Combined Arms exercises |
| **Multi-lingual** | Instant language switching |
| **AAR** | Interactive After Action Review with blue/red force positions |
| **CQB support** | Drag-and-drop range configuration |
| **Target integration** | Static + portable + moving + robotic (seamless) |
| **Third-party** | Flexible communication layer for external systems |
| **Platforms** | High-performance server, commercial tablet, Polytronic tablet |
| **Communication** | Wired or wireless |
| **Simulation** | Environmental effects modeling |

---

## 8. ROBOTIC TARGETS (RT Series) - Advanced Capability

This is Polytronic's **most advanced capability** - no direct equivalent from Zen, TTS, or InVeris.

| Feature | RT-CQB | RT-M | RT-M6 |
|---------|--------|------|-------|
| **Application** | Indoor CQB | Flagship outdoor | Extended platform |
| **Ballistic rating** | 7.62mm NATO | 7.62mm NATO | 7.62mm NATO |
| **Shot detection** | Zonal | Zonal | Zonal + advanced LOMAH |
| **Navigation** | LIDAR + GPS | LIDAR + GPS | LIDAR + GPS |
| **Obstacle avoidance** | Dynamic | Dynamic | Dynamic |
| **Autonomy** | Semi-autonomous | Semi-autonomous | Semi-autonomous |
| **Behavior** | Tactical formations (up to 4 RTs) | Tactical formations | Specialized/tracked |
| **Collapsible** | Yes (confined spaces) | No | No |
| **CnC control** | Up to 4 RTs per controller | Up to 4 RTs | Up to 4 RTs |
| **AROS integration** | Yes | Yes | Yes |
| **3D mannequin** | Yes (hit lethality sensing) | Yes | Yes |
| **Day/night** | Yes | Yes | Yes |

---

## 9. DETECTION PRINCIPLE ANALYSIS

### 9.1 Supersonic LOMAH (H-Bar, T-Bar)

Standard acoustic TDOA approach, same physics as competitors:

```
Supersonic bullet (V > 350 m/s at target)
═══════════════════════════════════════════►
                │
     Mach cone  │╲  θ = arcsin(V_sound / V_bullet)
                │  ╲
────────────────┼────╲────────── H-Bar sensor array
                │     ╲
    [Sensors detect shockwave TDOA]
    → Algorithm → (X, Y) position
    → Relay to AROS + IVDU
```

**Polytronic advantage:** Lower min velocity (350 m/s vs 440-450 m/s competitors) = works at longer ranges where bullets decelerate.

### 9.2 Subsonic LOMAH (I-Bar, TG 4040) - RADAR TECHNOLOGY

```
┌──────────────────────────────────────────────────────────┐
│                                                            │
│    RADAR-BASED DETECTION (Polytronic World First)          │
│                                                            │
│    Unlike acoustic LOMAH which needs Mach cone:            │
│                                                            │
│    Radar emitter → Continuous RF beam across detection zone │
│                                                            │
│    Subsonic bullet (V < 340 m/s)                           │
│    ══════════════════════════════►                          │
│           │                                                │
│           │ Bullet enters radar field                      │
│           │ → Radar return signal detected                 │
│           │ → Doppler shift gives velocity                 │
│           │ → Time-of-flight gives position                │
│           │ → OR: multiple radar elements give             │
│           │      triangulated position                     │
│                                                            │
│    Result: Shot location even for 9mm, .45, .22 LR         │
│                                                            │
│    TG 4040 variant: ZONAL scoring (hit zones, not X,Y)     │
│    I-Bar variant: Full shot location                        │
│                                                            │
└──────────────────────────────────────────────────────────┘
```

**This is fundamentally different from TTS Box Target** which still uses acoustic detection (impact sound through rubber membrane). Polytronic's radar approach:
- Does NOT require physical contact with any membrane
- Does NOT require enclosed chamber
- Works in open air for subsonic rounds
- Is truly non-contact detection

### 9.3 TG 4002 Box Target (Enclosed Acoustic)

Similar to TTS Box Target concept:
- Sensor array inside sealed aluminium case
- Enclosed sensors = weather immune
- Detects both supersonic and subsonic ammunition
- "Exceptional accuracy for small arms"

---

## 10. COMPARATIVE ANALYSIS: Polytronic vs. Competitors

| Parameter | Polytronic (CH) | InVeris (USA) | TTS (Germany) | Zen (India) |
|-----------|----------------|---------------|---------------|-------------|
| **Founded** | **1966 (oldest)** | 1926 (Caswell) | N/A | N/A |
| **Invented e-scoring** | **Yes (1969)** | No | No | No |
| **Supersonic LOMAH** | Yes (H-Bar, T-Bar) | Yes | Yes | Yes |
| **Subsonic LOMAH** | **Yes (I-Bar radar)** | No | Yes (Box Target acoustic) | No |
| **Radar detection** | **Yes (world first)** | No | No | No |
| **Box Target** | Yes (TG 4002) | No | Yes | No |
| **Pistol LOMAH** | **Yes (TG 4040, zonal)** | No | No | No |
| **Multi-angle fire** | Yes (H-Bar) | Yes | Yes | Not published |
| **Min velocity** | **350 m/s (lowest)** | 450 m/s | 440 m/s | Supersonic |
| **Accuracy** | +/- 5mm | <5mm | Not published | ~5mm est. |
| **Robotic targets** | **Yes (LIDAR+GPS, semi-autonomous)** | No | No | No |
| **Range software** | AROS (AAR, multi-lingual) | RM9K/RM10K | TACF | MCS |
| **Lane Initiator** | Yes (in IVDU) | Yes (LSI) | Not published | Not published |
| **IP rating** | IP67 | IP67 (LOMAH), IP65 (SIT) | Not published | Not published |
| **Battery (target)** | 25.2V Li-Ion, 700 ops | 20V Li-ion, 10h | No battery | No battery |
| **Radio range** | >2,000 m | 2,000 m (WiFi) | Not published | Not published |
| **Radio frequency** | 400-470 MHz UHF | WiFi | Ethernet/RF | Ethernet |
| **FASIT compliant** | Not published | Yes | Yes | No |
| **Sport/civilian** | **Yes (TG 3000/6000/6302)** | No | No | No |
| **Operating temp** | -25°C to +50°C | -25°C to +70°C | -25°C to +65°C | Est. MIL-STD |
| **Wind resistance** | 72 km/h (single target) | 56 km/h | Not published | Not published |
| **Hit detection rate** | 1,200 rpm | 1,200 rpm | Not published | Not published |

---

## 11. KEY DESIGN INSIGHTS FOR INDIGENOUS DEVELOPMENT

### 11.1 Innovations to Adopt from Polytronic

| Innovation | Engineering Value | Priority |
|-----------|------------------|----------|
| **Radar-based subsonic LOMAH** | Detects 9mm without contact/chamber | HIGH - research radar approach |
| **Lower min velocity (350 m/s)** | Extended range scoring | MEDIUM - optimize sensor sensitivity |
| **15-level hit sensor sensitivity** | Adjustable contact detection | LOW - software feature |
| **Built-in illumination** | Moonlight/hit/retaliatory fire sim | MEDIUM - adds training value |
| **IVDU with integrated Lane Initiator** | Combined display + lane discrimination | HIGH - reduces component count |
| **AROS multi-lingual + AAR** | Interactive after action review | MEDIUM - software development |
| **Robotic targets with LIDAR+GPS** | Future capability roadmap | LOW - Phase 2 product |
| **25.2V Li-Ion, 700 operations** | Good battery life specification | HIGH - target for VN design |
| **72 km/h wind resistance** | Best-in-class wind tolerance | MEDIUM - mechanical design |
| **Swiss quality / ISO triple cert** | Quality benchmark | HIGH - adopt for VN certification |

### 11.2 Polytronic Vulnerabilities (Vietnamese Opportunities)

| Weakness | Opportunity |
|----------|-------------|
| Premium Swiss pricing | **Cost advantage** at <=70% |
| Operating temp max +50°C (lower than competitors) | Design for **+60-70°C** (tropical requirement) |
| 400-470 MHz radio (specific band) | Add **multi-band** (VHF/UHF/WiFi) like InVeris |
| No FASIT compliance published | Implement **FASIT** for export potential |
| Radar subsonic LOMAH likely expensive | Develop **lower-cost radar** or use TTS-style chamber as alternative |
| No published portable WiFi variant | Combine **InVeris portable concept** with Polytronic H-Bar |
| TG 4040 is zonal only (not X,Y) | Develop **full X,Y radar** for subsonic |
| Robotic targets are niche/expensive | Not needed for initial Vietnamese product |

---

## 12. BILL OF MATERIALS ESTIMATE (Vietnamese Equivalent)

### 12.1 Per-Lane H-Bar LOMAH Equivalent

| Component | Description | Sourcing (VN) | Est. Cost |
|-----------|-------------|---------------|-----------|
| MEMS microphones (x6-8) | High-SPL, H-configuration | Import (TDK/Knowles) | $12-30 |
| Temperature sensor | Digital compensation | Import (commodity) | $1-2 |
| MCU/DSP | STM32H7 or equivalent | Import | $10-25 |
| Analog frontend (multi-ch) | Op-amp, BPF, AGC | Mixed | $8-15 |
| Radio module (UHF 400-470MHz) | >2km range | Import | $10-20 |
| WiFi module (optional) | 802.11n/ac | Import | $5-15 |
| Sensor frame (H-bar) | Aluminum, 1200x450mm | **Local** (Hoa Phat) | $25-45 |
| Ballistic enclosure | Composite/steel | **Local** | $15-30 |
| Target lifter (TG 82 equiv) | 25.2V motor + gearbox | **Local** machining | $35-65 |
| Li-Ion battery pack | 25.2V / 4.4Ah | Import/local assembly | $15-25 |
| Contact hit sensor | 15-level sensitivity | Mixed | $5-10 |
| Illumination module | LED moonlight/flash/fire | **Local** | $5-10 |
| PCB + IP67 enclosure | Custom PCB, sealed housing | **Local** PCB fab | $15-25 |
| IVDU display unit | LCD + toughened glass | Mixed | $40-80 |
| Cabling + connectors | IP67 connectors | **Local**/import | $5-10 |
| **Subtotal per lane** | | | **$205-405** |

### 12.2 Radar Subsonic Add-on (R&D Item)

| Component | Description | Est. Cost |
|-----------|-------------|-----------|
| Radar module (24GHz or 77GHz) | FMCW radar for bullet detection | $30-80 |
| Radar signal processor | DSP/FPGA for Doppler + position | $20-40 |
| Radar antenna array | Patch or horn antenna | $15-30 |
| **Subtotal radar add-on** | | **$65-150** |

### 12.3 Local Content Analysis

| Category | Local Value | Import Value | Local % |
|----------|------------|-------------|---------|
| Mechanical (frame, lifter, enclosure, illumination) | $80-150 | $0 | **100%** |
| Electronics (PCB, passive, hit sensor) | $20-35 | $55-115 | ~25% |
| Battery assembly | $5-10 | $10-15 | ~40% |
| Display (IVDU) | $10-20 | $30-60 | ~25% |
| Software/firmware | $0 (labor) | $0 | **100%** |
| **Overall by value** | | | **~52-60%** |

---

## 13. TECHNOLOGY ROADMAP IMPLICATIONS

Polytronic's product evolution suggests a clear technology trajectory:

```
TECHNOLOGY EVOLUTION (Polytronic trajectory)
════════════════════════════════════════════

1966-2000: Acoustic scoring (sport → military)
    │
2000-2016: LOMAH variants (H-Bar, T-Bar, Box Target)
    │
2016-2020: AROS software platform + radar subsonic LOMAH
    │           (WORLD FIRST - key technology breakthrough)
    │
2021-2024: Robotic targets (LIDAR, GPS, semi-autonomous)
    │
2025+: AI-driven training? Fully autonomous targets?
         AR/VR integration with live-fire?

VIETNAMESE DEVELOPMENT SHOULD TARGET:
═════════════════════════════════════
Phase 1: Acoustic LOMAH (H-Bar equivalent) ← Proven technology
Phase 2: Box Target (enclosed, subsonic) ← Lower risk than radar
Phase 3: Radar subsonic LOMAH (R&D) ← Future differentiator
Phase 4: Robotic targets ← Long-term roadmap
```

---

## 14. ASSESSMENT SUMMARY

### Strengths
- **Inventor of electronic scoring** (1966) - deepest domain expertise
- **Only radar-based subsonic LOMAH** in the world (I-Bar)
- Lowest minimum velocity (350 m/s) - works at longest ranges
- Most advanced robotic targets (LIDAR + GPS, semi-autonomous)
- Best-in-class wind resistance (72 km/h)
- Comprehensive software platform (AROS with AAR, multi-lingual)
- Triple ISO certification (9001, 14001, 45001)
- Dual market presence (sport/hunting + military)
- Integrated Lane Initiator in IVDU
- IP67 rated, MIL-STD built

### Weaknesses
- Premium Swiss pricing (highest in market)
- Lower operating temperature (+50°C vs +60-70°C competitors)
- No published FASIT compliance
- Radar LOMAH likely very expensive
- TG 4040 only zonal scoring (not full X,Y for subsonic)
- No published portable WiFi variant like InVeris
- Proprietary communication protocol (AROS)

### Relevance to Vietnamese Development
- Radar subsonic LOMAH is the future technology direction - study for Phase 3
- Lower min velocity (350 m/s) is achievable with better analog frontend
- IVDU with integrated Lane Initiator reduces per-lane component count
- AROS-style software (multi-lingual, AAR) should be development target
- TG 82-70 specifications provide detailed mechanical design benchmark
- Box Target (TG 4002) provides simpler subsonic path than radar
- Robotic targets are long-term roadmap item, not Phase 1 priority
- Swiss quality standards (ISO triple) should be adopted for Vietnamese product

---

*Analysis based entirely on publicly available information (product pages, brochures, distributor sites, press releases, company history).*
*Polytronic's radar-based subsonic detection (I-Bar) represents a fundamentally different technology approach from acoustic-only competitors.*
*Patent landscape for radar-based bullet detection should be investigated before development.*
