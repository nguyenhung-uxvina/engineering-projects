---
project: VN-TRN-LOMAH
phase: 0
type: reverse-engineering
subject: InVeris Training Solutions LOMAH (USA)
version: 1.0
created: 2026-02-06
status: complete
---

# RE: InVeris Training Solutions LOMAH - USA
## Reverse Engineering Analysis from Public Sources

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | InVeris Training Solutions (formerly Meggitt Training Systems) |
| **HQ** | Suwanee, Georgia, USA (235,000 sq ft facility) |
| **Ownership** | Pine Island Capital Partners |
| **Legacy** | Caswell International (1926) + FATS + Meggitt PLC |
| **Rebranded** | October 2020 (Meggitt → InVeris) |
| **Employees** | 400+ across multiple countries |
| **Global presence** | USA, Australia, Canada, Netherlands, Singapore, UAE, UK |
| **Installed base** | 15,500+ live-fire ranges, 7,500+ virtual systems, 80,000+ target lifters |
| **Website** | https://www.inveristraining.com |

InVeris is the **global market leader** in integrated live-fire and virtual weapons training. Their installed base of 80,000+ target systems worldwide makes them the benchmark against which all competitors are measured.

---

## 2. PRODUCT FAMILY OVERVIEW

```
InVeris Training Solutions - Live Fire Portfolio
│
├── Electronic Scoring
│   ├── LOMAH (Standard) ←── Fixed, supersonic .22-.50 cal
│   ├── LOMAH (Armor) ←── 5.56mm-120mm, larger detection zone
│   └── Portable LOMAH ←── Battery + WiFi, field-deployable
│
├── Target Mechanisms (Host Platforms)
│   ├── SIT (Stationary Infantry Target) ←── 44,000+ fielded
│   ├── MF-SIT (Multi-Function SIT) ←── 33,000+ fielded, 360° rotation
│   ├── SAT (Stationary Armor Target)
│   ├── SP-MIT (Self-Propelled Moving Infantry Target)
│   ├── QuikTurn 360 ←── Portable turning, <0.5s expose
│   ├── QuikTurn 90
│   ├── DP29 Running Man Target
│   ├── XWT Wireless Target Carrier ←── Indoor, 360° turning
│   └── XWT Lite (no turning)
│
├── Range Control Software
│   ├── RangeMaster 9000 (RM9K) ←── Desktop control
│   ├── RangeMaster 10000 (RM10K) ←── Wireless tablet control
│   ├── Visual Shot
│   ├── TRACR
│   ├── FASIT compatible
│   └── RISCON-T compatible
│
├── Range Infrastructure
│   ├── GranTrap (rubber bullet trap, up to .50 BMG)
│   ├── Road Range (mobile/containerized range)
│   ├── SHOTT House (shoot house for tactical training)
│   ├── SafeZone shooting stalls
│   └── Ballistic protection (blocks, panels, walls)
│
└── Virtual Training
    ├── FATS AR (Augmented Reality)
    └── FATS VR (Virtual Reality)
```

---

## 3. LOMAH SYSTEM ARCHITECTURE

### 3.1 System Topology

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    InVeris LOMAH SYSTEM TOPOLOGY                         │
│                                                                          │
│  TARGET END (Per Lane)                                                   │
│  ┌─────────────────────────┐                                             │
│  │ Target Lifter            │                                            │
│  │ (SIT / MF-SIT / SAT)    │                                            │
│  │  ┌───────────────────┐  │    Ethernet 100BaseT                       │
│  │  │ Microphone Sensor │  │    (or VHF/UHF/WiFi/Fiber)                 │
│  │  │ Array             │  │◄─────────────────────┐                     │
│  │  │ (ballistic encl.) │  │                      │                     │
│  │  └───────────────────┘  │                      │                     │
│  │  ┌───────────────────┐  │                      │                     │
│  │  │ LOMAH Lane Shot   │  │                      │                     │
│  │  │ Initiator (LSI)   │  │                      │                     │
│  │  │ (multi-lane       │  │                      │                     │
│  │  │  discrimination)  │  │                      │                     │
│  │  └───────────────────┘  │                      │                     │
│  └─────────────────────────┘                      │                     │
│                                                    │                     │
│  FIRER'S END (Per Lane)                           │                     │
│  ┌─────────────────────────┐                      │                     │
│  │ Firing Point Computer   │                      │                     │
│  │ (FPC)                   │◄─────────────────────┤                     │
│  │ - Graphical hit plot    │                      │                     │
│  │ - 4X zoom of target     │                      │                     │
│  │ - Shot replay           │                      │                     │
│  │ - Sequential numbering  │                      │                     │
│  │ - Group size analysis   │                      │                     │
│  │ - Integrated sun shield │                      │                     │
│  └─────────────────────────┘                      │                     │
│                                                    │                     │
│  CONTROL CENTER                                    │                     │
│  ┌─────────────────────────────────────────────────┴──────────────┐     │
│  │ RangeMaster 9000 (RM9K) - Desktop                              │     │
│  │ - Target locations/presentations via color icons               │     │
│  │ - Distance in ft/yd/m increments                               │     │
│  │ - Controls targetry, security, ventilation, lighting           │     │
│  │ - Scenario authoring, storage, download to firing line         │     │
│  │ - Controls any/all/combination of target types                 │     │
│  ├────────────────────────────────────────────────────────────────┤     │
│  │ RangeMaster 10000 (RM10K) - Wireless Tablet                   │     │
│  │ - Touchscreen + wireless control                               │     │
│  │ - Same capabilities as RM9K                                    │     │
│  │ - Ruggedized tablet controller                                 │     │
│  │ - Range up to 2,000 meters                                     │     │
│  └────────────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Communication Protocol Options

InVeris is unique in supporting the **widest range of communication methods** in the industry:

```
┌──────────────────────────────────────────┐
│  Communication Options (Factory Config)   │
│                                           │
│  WIRED:                                   │
│  ├── Ethernet 100BaseT (standard)         │
│  ├── Serial                               │
│  └── Fiber optic                          │
│                                           │
│  WIRELESS:                                │
│  ├── VHF radio                            │
│  ├── UHF radio                            │
│  └── WiFi (up to 2,000 m range)           │
│                                           │
│  SOFTWARE COMPATIBILITY:                  │
│  ├── RangeMaster RM9K/RM10K               │
│  ├── Visual Shot                          │
│  ├── TRACR                                │
│  ├── FASIT                                │
│  └── RISCON-T                             │
└──────────────────────────────────────────┘
```

### 3.3 Unique Component: Lane Shot Initiator (LSI)

The **LSI** is an InVeris-specific innovation not found in competitors:

```
Multi-Position Range Problem:
    Shooter A ──────────────► Target Zone
    Shooter B ──────────────► (shared LOMAH detection window)
    Shooter C ──────────────►

Without LSI: Cannot tell which shooter fired which shot
With LSI:    LSI at each firing position detects muzzle blast timing
             → Correlates with LOMAH detection → Assigns shot to correct lane
```

This solves a critical problem for **multi-lane ranges** where detection zones overlap.

---

## 4. LOMAH VARIANTS - DETAILED SPECIFICATIONS

### 4.1 Standard LOMAH (Fixed Installation)

| Parameter | Specification |
|-----------|--------------|
| **Detection method** | Acoustic - supersonic shockwave (Mach cone) |
| **Sensor type** | Microphone sensor array |
| **Sensor mounting** | Below lifter height, ballistic enclosure |
| **Caliber range** | .22 to .50 caliber (NATO 5.56 to 12.7mm) |
| **Min projectile velocity** | 450 m/s (1,476 ft/s) at target |
| **Detection zone** | 3 x 2.5 m (10 x 8 ft) |
| **Max detection rate** | 1,200 rounds/minute |
| **Accuracy** | Average radial tolerance <5mm at target center within 150mm radius |
| **Wind tolerance** | <1.5 m/s for rated accuracy |
| **Operating temp** | -25°C to +70°C (-13°F to +158°F) |
| **Storage temp** | -40°C to +70°C (-40°F to +158°F) |
| **IP rating** | IP67 |
| **Power** | Integrated into SIT, or +12V enclosure, or PoE |
| **Communication** | Ethernet 100BaseT |
| **Output** | X,Y coordinate + graphical image on FPC |
| **Display features** | 4X zoom, shot replay, sequential numbering, group size |
| **Installation** | Retrofit kit or factory-integrated |

### 4.2 Armor LOMAH

| Parameter | Specification |
|-----------|--------------|
| **Caliber range** | 5.56mm to 120mm |
| **Detection zone** | 4 x 3 m (13 x 10 ft) - larger than standard |
| **Max detection rate** | 1,200 rounds/minute |
| **Accuracy** | Average radial tolerance <150mm in target area |
| **Wind tolerance** | <1.5 m/s |
| **Operating temp** | -25°C to +70°C |
| **Storage temp** | -40°C to +70°C |
| **IP rating** | IP67 |
| **Power** | +12V or PoE |
| **Communication** | Ethernet 100BaseT |
| **Integration** | Mounts on SAT (Stationary Armor Target) or MAT |

### 4.3 Portable LOMAH (Field-Deployable)

| Parameter | Specification |
|-----------|--------------|
| **Caliber range** | .22 to .50 caliber (NATO 5.56 to 12.7mm) |
| **Min projectile velocity** | 450 m/s (1,476 ft/s) |
| **Detection zone** | Adjustable, typical 3 x 2.5 m (10 x 8 ft) |
| **Max detection rate** | 1,200 rounds/minute |
| **Accuracy** | <5mm radial at center within 150mm radius |
| **Wind tolerance** | <1.5 m/s |
| **Operating temp** | -25°C to +70°C |
| **IP rating** | IP67 |
| **Primary power** | Removable 20V lithium-ion battery pack |
| **Battery life** | Up to 10 hours/charge (larger options available) |
| **Communication** | WiFi radio, range up to 2,000 m |
| **Base** | Adjustable base (no trench required) |
| **Key innovation** | Battery + WiFi = no infrastructure needed |
| **Optional** | Self-contained SIT lifter |

### 4.4 Comparison Table: Three LOMAH Variants

| Feature | Standard | Armor | Portable |
|---------|----------|-------|----------|
| **Caliber** | .22-.50 | 5.56-120mm | .22-.50 |
| **Detection zone** | 3x2.5m | 4x3m | 3x2.5m (adjustable) |
| **Accuracy** | <5mm | <150mm | <5mm |
| **Power** | 12V/PoE | 12V/PoE | 20V Li-ion battery |
| **Comms** | Ethernet | Ethernet | WiFi (2km) |
| **Infrastructure** | Wired range | Wired range | None needed |
| **Battery life** | N/A | N/A | 10+ hours |
| **Use case** | Fixed range | Tank/armor range | Field/expeditionary |

---

## 5. HOST TARGET PLATFORMS

### 5.1 Stationary Infantry Target (SIT) - Primary LOMAH Host

| Parameter | Specification |
|-----------|--------------|
| **Fielded quantity** | 44,000+ worldwide (80,000+ all target types) |
| **Communication** | VHF, UHF, Ethernet, Serial (factory configurable) |
| **Master/slave** | Up to 100 targets per group |
| **Hit sensing** | 600 hits/minute, remotely adjustable sensitivity |
| **Expose/conceal time** | <1 second |
| **Target weight** | Up to 10 lbs (4.5 kg) |
| **Unit weight** | 50 lb (22.6 kg) excl. battery |
| **Exposed dimensions** | 12"W x 18"L x 20"H (30x46x51 cm) |
| **Concealed dimensions** | 11"W x 18"L x 24"H (28x46x61 cm) |
| **Power** | 12VDC, 120VAC 60Hz, or 230/240VAC 50/60Hz |
| **Operating temp** | -29°C to +60°C (-20°F to +140°F) |
| **IP rating** | IP65 |
| **Wind rating** | 35 mph (56 kph) safe operation |
| **Target types** | US Army E, F, 3-D; NATO fig 11, 12, 15 |
| **Options** | Muzzle flash simulator, moonlight simulator, LOMAH |

### 5.2 Self-Propelled Moving Infantry Target (SP-MIT)

| Parameter | Specification |
|-----------|--------------|
| **Max speed** | 10 mph (16 kph), variable |
| **Track width** | 2 ft standard sections, 50-500 ft length |
| **Turning radius** | As tight as 25 ft (7m) |
| **Grade capability** | Up to 5% |
| **Carrier size** | 26"W x 33"L x 24"H (concealed) |
| **Target weight** | Up to 10 lbs (4.5 kg) |
| **Emplacement depth** | As shallow as 24" (0.60m) |
| **Hit detection** | 600 rounds/minute, adjustable |
| **Expose/conceal** | <1 second |
| **Power** | 24VDC on-board; AC, DC, DC Solar charging |
| **Communication** | VHF, UHF, Ethernet, WiFi, Fiber |
| **Operating temp** | -29°C to +60°C |
| **IP rating** | IP67 |
| **Wind rating** | 35 mph (56 kph) |
| **LOMAH** | Optional integration |
| **Other options** | Muzzle flash/moonlight simulator, MILES adaptor, thermal targets, dual lifters |

### 5.3 QuikTurn 360 Portable

| Parameter | Specification |
|-----------|--------------|
| **360° turn time** | <1 second |
| **90° expose/conceal** | <0.5 seconds |
| **Unit weight** | 30 lbs (13.6 kg) |
| **Max target weight** | 10 lbs (4.5 kg) |
| **Actuator dimensions** | 8.25" x 13.5" x 9" |
| **Hit sensing** | Up to 600 hits/minute (optional) |
| **LED indicators** | Red, blue, white (threat/no-threat) |
| **Power** | 20VDC rechargeable lithium, solar charging available |
| **Battery actuations** | 6,500+/charge (5AH battery) |
| **Communication** | WiFi up to 2,000 m |
| **Software** | RangeMaster 9K/10K compatible |
| **LOMAH** | Optional integration |

---

## 6. RANGE CONTROL SOFTWARE ECOSYSTEM

### 6.1 RangeMaster 9000 (RM9K) - Desktop

| Feature | Detail |
|---------|--------|
| **Target display** | All target locations, presentations via color-changing icons |
| **Distance units** | Feet, yards, or meters (selectable) |
| **Controls** | Targetry, security systems, ventilation, lighting |
| **Scenario authoring** | Write, store, download to individual firing line units |
| **Target compatibility** | Controls any, all, or combination of target types |
| **Infrastructure integration** | Range security + HVAC + lighting unified control |

### 6.2 RangeMaster 10000 (RM10K) - Wireless Tablet

| Feature | Detail |
|---------|--------|
| **Form factor** | Ruggedized wireless touchscreen tablet |
| **Full-size keyboard** | Detachable, backlit |
| **Wireless range** | Up to 2,000 meters |
| **Capabilities** | Same as RM9K + wireless mobility |
| **Use case** | Mobile instructor, field ranges |

### 6.3 Software Integration Matrix

| Software | Type | Description |
|----------|------|-------------|
| **RangeMaster RM9K** | Range control | Desktop target/range management |
| **RangeMaster RM10K** | Range control | Wireless tablet variant |
| **Visual Shot** | Scoring | Shot display and analysis |
| **TRACR** | Training record | Training records and reporting |
| **FASIT** | Standard | US Army interoperability protocol |
| **RISCON-T** | Standard | Additional military standard |

---

## 7. DETECTION PRINCIPLE - ENGINEERING ANALYSIS

### 7.1 Acoustic Shockwave Detection

```
    Supersonic bullet trajectory (V > 450 m/s)
    ════════════════════════════════════════════►
                    │
         Mach cone  │╲  θ = arcsin(V_sound / V_bullet)
                    │  ╲
                    │    ╲
    ────────────────┼──────╲───────────── Sensor array plane
                    │       ╲
    [Mic 1]  [Mic 2]  [Mic 3]  [Mic 4]
       │        │         │        │
       t₁       t₂        t₃       t₄

    TDOA method:
    Δt₁₂ = t₁ - t₂  →  Hyperbola 1
    Δt₁₃ = t₁ - t₃  →  Hyperbola 2
    Intersection → (X, Y) position of bullet passage
```

### 7.2 InVeris-Specific: "Triangulation of Sound Waves"

InVeris publicly states their method as **"Triangulation of sound waves for hit location"** which they describe as making their "offering unique in this market."

From their published materials:
1. Microphone sensor array mounted below lifter height
2. Ballistic protection enclosure around sensors
3. System measures **precise time** of shockwave passing over each sensor
4. **Triangulation** algorithm computes (X,Y) coordinate
5. Result transmitted to Firing Point Computer (FPC)
6. FPC displays graphical image + numerical coordinates

### 7.3 Signal Processing Chain (Estimated)

```
Supersonic shockwave
    │
    ▼
Microphone sensor array (ballistically protected)
    │
    ▼
Analog signal conditioning
├── Bandpass filter (shockwave frequency band)
├── Amplification (AGC)
└── Anti-aliasing filter
    │
    ▼
High-speed ADC (estimated 500 kHz - 2.8 MHz)
    │
    ▼
TDOA computation engine
├── Cross-correlation or threshold detection
├── Temperature compensation (V_sound = 331.3 + 0.606 × T)
└── Calibration transform application
    │
    ▼
Position calculator
├── Triangulation algorithm → (X, Y)
└── Score zone mapping
    │
    ▼
Communication interface
├── Ethernet 100BaseT (standard/armor)
└── WiFi (portable variant)
    │
    ▼
Firing Point Computer (FPC)
├── Graphical display with 4X zoom
├── Shot replay
├── Sequential shot numbering
└── Group size analysis
```

### 7.4 Accuracy Analysis

| Zone | Standard LOMAH | Armor LOMAH |
|------|---------------|-------------|
| **Center (r < 150mm)** | <5mm average radial | <150mm average radial |
| **Full detection zone** | Degrades toward edges | Degrades toward edges |
| **Detection zone size** | 3 x 2.5 m | 4 x 3 m |
| **Max fire rate** | 1,200 rpm | 1,200 rpm |

The <5mm accuracy at center is the **industry benchmark**. Accuracy degrades toward the edges of the detection zone due to:
- Mach cone angle variations at oblique passages
- Sensor geometry (farther from sensor centroid = less precise TDOA)
- Wind effects on shockwave propagation

---

## 8. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  OVERALL FUNCTION: "Detect, score and report projectile location         │
│                     for integrated live-fire training range"              │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  F1: Detect projectile         F2: Compute position                      │
│  ┌──────────────────────┐     ┌──────────────────────┐                  │
│  │ F1.1 Sense Mach cone  │     │ F2.1 Measure TDOA    │                  │
│  │      shockwave        │     │ F2.2 Temperature      │                  │
│  │ F1.2 Filter/amplify   │     │      compensation    │                  │
│  │ F1.3 Digitize (ADC)   │     │ F2.3 Triangulate     │                  │
│  │ F1.4 Discriminate lane│     │      (X,Y)           │                  │
│  │      (via LSI)        │     │ F2.4 Apply calibration│                  │
│  └──────────────────────┘     │      transform       │                  │
│                                └──────────────────────┘                  │
│                                                                          │
│  F3: Present target            F4: Control range                         │
│  ┌──────────────────────┐     ┌──────────────────────┐                  │
│  │ F3.1 Lift/lower       │     │ F4.1 RangeMaster     │                  │
│  │      (<1 sec)         │     │      RM9K/RM10K      │                  │
│  │ F3.2 Turn (360°       │     │ F4.2 Scenario author │                  │
│  │      for MF-SIT)      │     │ F4.3 Multi-target    │                  │
│  │ F3.3 Move (SP-MIT     │     │      coordination    │                  │
│  │      up to 10 mph)    │     │ F4.4 FASIT protocol  │                  │
│  │ F3.4 LED indicators   │     │ F4.5 Security/HVAC/  │                  │
│  │ F3.5 Muzzle flash sim │     │      lighting ctrl   │                  │
│  └──────────────────────┘     └──────────────────────┘                  │
│                                                                          │
│  F5: Report results            F6: Withstand environment                 │
│  ┌──────────────────────┐     ┌──────────────────────┐                  │
│  │ F5.1 FPC display      │     │ F6.1 -29°C to +60°C  │                  │
│  │      (4X zoom)        │     │ F6.2 IP65 (SIT)      │                  │
│  │ F5.2 Shot replay      │     │      IP67 (LOMAH/MIT)│                  │
│  │ F5.3 Group size calc  │     │ F6.3 35 mph wind safe│                  │
│  │ F5.4 Sequential number│     │ F6.4 Ballistic sensor│                  │
│  │ F5.5 TRACR logging    │     │      protection      │                  │
│  │ F5.6 Visual Shot      │     │ F6.5 .50 BMG bullet  │                  │
│  │      integration      │     │      trap (GranTrap) │                  │
│  └──────────────────────┘     └──────────────────────┘                  │
│                                                                          │
│  F7: Deploy flexibly (Portable LOMAH specific)                           │
│  ┌──────────────────────┐                                                │
│  │ F7.1 Battery power    │                                               │
│  │      (20V Li-ion, 10h)│                                               │
│  │ F7.2 WiFi comms       │                                               │
│  │      (2,000m range)   │                                               │
│  │ F7.3 No infrastructure│                                               │
│  │ F7.4 Solar charging   │                                               │
│  │      (optional)       │                                               │
│  └──────────────────────┘                                                │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 9. COMPETITIVE ADVANTAGES (What InVeris Does Better)

### 9.1 vs. Zen Technologies (India)

| Advantage | InVeris | Zen |
|-----------|---------|-----|
| Installed base | 80,000+ targets | Much smaller |
| Portable/wireless variant | Yes (WiFi 2km, battery 10h) | No |
| Armor LOMAH (120mm) | Yes | No published |
| Lane discrimination (LSI) | Yes | No published |
| FASIT compliance | Yes | No |
| Software ecosystem | RM9K/10K + Visual Shot + TRACR | MCS only |
| Multi-comm options | VHF/UHF/Ethernet/WiFi/Fiber/Serial | Ethernet |
| Display features | 4X zoom, replay, group analysis | Basic display |

### 9.2 vs. Theissen Training Systems (Germany)

| Advantage | InVeris | TTS |
|-----------|---------|-----|
| Portable/battery variant | Yes | No |
| WiFi range | 2,000 m | RF (range unspecified) |
| Armor LOMAH (120mm) | Yes, dedicated product | Yes, on SAT/MAT |
| Subsonic scoring | No | Yes (Box Target) |
| Installed base | 80,000+ | Smaller |
| Lane discrimination (LSI) | Yes | No published |
| Multi-comm factory config | 6 options | Ethernet + RF |
| Solar charging | Yes (SP-MIT, QuikTurn) | No |

### 9.3 InVeris Weaknesses

| Weakness | Implication |
|----------|-------------|
| **No subsonic scoring** | Cannot score 9mm, .22 LR, air weapons |
| **Supersonic only** | Requires V > 450 m/s at target |
| **Wind sensitive** | <1.5 m/s for rated accuracy (open-air) |
| **High cost** | Premium US pricing |
| **No Box Target equivalent** | No zero-wind enclosed option |
| **IP65 on SIT** (not IP67) | Lower protection than LOMAH unit itself |
| **Weight** | SIT at 50 lb vs lighter alternatives |

---

## 10. COMPARATIVE ANALYSIS: InVeris vs. TTS vs. Zen

| Parameter | InVeris (USA) | TTS (Germany) | Zen (India) |
|-----------|--------------|---------------|-------------|
| **Installed base** | 80,000+ targets | Not published | Not published |
| **LOMAH open-air** | Yes | Yes | Yes |
| **Subsonic scoring** | No | Yes (Box Target) | No |
| **Armor LOMAH** | Yes (5.56-120mm) | Yes | Not published |
| **Portable variant** | Yes (battery+WiFi) | No | No |
| **WiFi range** | 2,000 m | Not published | Not published |
| **Battery life** | 10+ hours (20V Li-ion) | N/A | N/A |
| **Solar charging** | Yes (SP-MIT, QuikTurn) | No | No |
| **Lane discrimination** | Yes (LSI) | Not published | Not published |
| **Min velocity** | 450 m/s | 440 m/s (Mach 1.3) | Supersonic |
| **Accuracy (std)** | <5mm radial | Not published | Est. +/-5mm |
| **Detection zone (std)** | 3x2.5m | Not published | ~3x2.5m |
| **Max fire rate** | 1,200 rpm | Not published | Not published |
| **Operating temp** | -25 to +70°C | -25 to +65°C | Est. MIL-STD |
| **IP rating (LOMAH)** | IP67 | Not published | Not published |
| **IP rating (lifter)** | IP65 | Not published | Not published |
| **Communication** | VHF/UHF/Eth/WiFi/Fiber/Serial | Ethernet/RF | Ethernet |
| **FASIT compliant** | Yes | Yes | No |
| **Software** | RM9K/10K+VisualShot+TRACR | TACF | MCS |
| **Max targets** | Not published | 1,024 | Not published |
| **FPC features** | 4X zoom, replay, grouping | Graphical+Cartesian | Basic |
| **Moving target w/LOMAH** | SP-MIT (10 mph) | MIT (rail/cable) | Not published |
| **Retrofit-capable** | Yes | Yes (any vendor) | Proprietary |

---

## 11. BILL OF MATERIALS ESTIMATE (Vietnamese Equivalent)

### 11.1 Per-Lane LOMAH Unit (Standard Variant)

| Component | Description | Sourcing (VN) | Est. Cost |
|-----------|-------------|---------------|-----------|
| MEMS microphones (x4-8) | High-SPL, wide bandwidth | Import (TDK/Knowles) | $10-30 |
| Temperature sensor | DS18B20 digital | Import (commodity) | $1-2 |
| MCU/DSP | STM32H7 or equivalent | Import | $10-25 |
| Analog frontend (multi-ch) | Op-amp, BPF, AGC | Mixed | $8-15 |
| Ethernet PHY + PoE | 100BaseT, 802.3af | Import | $5-10 |
| WiFi module (portable) | 802.11n/ac, 2km range | Import | $5-15 |
| Sensor frame | Aluminum extrusion | **Local** (Hoa Phat) | $20-40 |
| Ballistic enclosure | Steel/composite sensor housing | **Local** | $15-30 |
| Target lifter mechanism | 12V actuator + linkage | **Local** machining | $30-60 |
| PCB + IP67 enclosure | Custom PCB, sealed housing | **Local** PCB fab | $15-25 |
| Li-ion battery pack (portable) | 20V, 5Ah removable | Import/local assembly | $15-30 |
| FPC display unit | Tablet/screen + software | Mixed | $40-80 |
| Cabling + connectors | IP67, Ethernet | **Local**/import | $5-10 |
| **Subtotal per lane (standard)** | | | **$135-260** |
| **Subtotal per lane (portable)** | | | **$175-340** |

### 11.2 Local Content Analysis

| Category | Local Value | Import Value | Local % |
|----------|------------|-------------|---------|
| Mechanical (frame, lifter, enclosure) | $65-130 | $0 | **100%** |
| Electronics (PCB, passive) | $15-25 | $50-110 | ~20% |
| Battery assembly | $5-10 | $10-20 | ~35% |
| Software/firmware | $0 (labor) | $0 | **100%** |
| FPC display | $10-20 | $30-60 | ~25% |
| **Overall by value (standard)** | | | **~55-63%** |
| **Overall by value (portable)** | | | **~50-58%** |

---

## 12. KEY DESIGN INSIGHTS FOR INDIGENOUS DEVELOPMENT

### 12.1 Innovations to Adopt from InVeris

| Innovation | Engineering Value | Implementation Priority |
|-----------|------------------|------------------------|
| **Portable LOMAH concept** | Battery + WiFi = no infrastructure | HIGH - field deployment critical for VN |
| **Lane Shot Initiator (LSI)** | Multi-lane discrimination | MEDIUM - needed for multi-position ranges |
| **Multi-comm factory config** | VHF/UHF/Eth/WiFi/Fiber/Serial | HIGH - VN ranges have varied infrastructure |
| **FPC with 4X zoom + replay** | Superior training feedback | MEDIUM - software-only improvement |
| **Solar charging option** | Off-grid sustainability | HIGH - tropical field conditions |
| **IP67 on LOMAH** | Environmental hardening | HIGH - tropical climate |
| **FASIT protocol support** | Export market access | MEDIUM - study for future |
| **Retrofit kit design** | Sell into existing ranges | HIGH - market entry strategy |

### 12.2 InVeris Gaps = Vietnamese Opportunities

| Gap | Vietnamese Advantage |
|-----|---------------------|
| No subsonic scoring | Add **Box Target** (TTS concept) with VN rubber |
| No wind-immune option | Add **chambered design** for indoor/field ranges |
| High US production cost | **50-60% cost reduction** achievable |
| No 0-infrastructure portable | Already portable, but **improve**: lighter, cheaper |
| IP65 on SIT (not IP67) | Design **all components IP67** from start |
| 50 lb SIT weight | Target **<30 lb** with aluminum optimization |
| No thermal target standard | Add **IR signature** option for NVG training |

---

## 13. RECOMMENDED VIETNAMESE PRODUCT CONCEPT (Updated)

Combining lessons from all three competitors (InVeris + TTS + Zen):

```
VIETNAMESE "VN-SMART TARGET" CONCEPT
════════════════════════════════════

  ┌───────────────────────────────────────┐
  │  MODE 1: Open-Air LOMAH               │ Supersonic (5.56, 7.62, 12.7)
  │  - Dual delta sensor arrays            │ (adopt TTS approach)
  │  - Lane Shot Initiator                 │ (adopt InVeris approach)
  │  - <5mm accuracy                       │
  ├───────────────────────────────────────┤
  │  MODE 2: Chambered (Box) Target        │ Subsonic + Supersonic
  │  - Vietnamese natural rubber membrane  │ (adopt TTS approach)
  │  - Zero-wind interference              │ (9mm, .22, air weapons)
  ├───────────────────────────────────────┤
  │  VARIANTS:                             │
  │  A) Fixed (wired, Ethernet/PoE)        │ Standard range
  │  B) Portable (battery + WiFi 2km)      │ Field deployment
  │  C) Armor (larger zone, 5.56-30mm)     │ Armor training
  ├───────────────────────────────────────┤
  │  INNOVATIONS vs. ALL IMPORTS:          │
  │  + Dual-mode (open-air + chambered)    │ Only TTS has this
  │  + Wireless LoRa/WiFi (2km+)           │ Like InVeris portable
  │  + Solar + battery field power          │ Like InVeris SP-MIT
  │  + Aluminum frame (tropical)            │ Better than TTS wood
  │  + Vietnamese rubber consumables        │ VN = #3 producer
  │  + Multi-comm (Ethernet/WiFi/VHF)      │ Like InVeris
  │  + FASIT-compatible protocol            │ Like InVeris + TTS
  │  + IP67 all components                  │ Better than InVeris SIT
  │  + Lightweight (<30 lb lifter)          │ Better than InVeris 50 lb
  │  + IR/thermal target option             │ Unique for NVG training
  ├───────────────────────────────────────┤
  │  COST TARGET: <=70% of InVeris import  │
  │  LOCAL CONTENT: >=60% by value         │
  └───────────────────────────────────────┘
```

---

## 14. ASSESSMENT SUMMARY

### Strengths
- Undisputed global market leader (80,000+ targets, 15,500+ ranges)
- Most comprehensive product ecosystem in the industry
- Only vendor with truly portable/wireless LOMAH (battery + WiFi)
- Widest communication options (6 factory-configurable methods)
- Strongest software ecosystem (RM9K/10K + Visual Shot + TRACR)
- FASIT + RISCON-T compliant
- Lane Shot Initiator (LSI) solves multi-position range problem
- Best-published accuracy specifications (<5mm radial)
- Armor variant handles up to 120mm caliber

### Weaknesses
- No subsonic scoring capability
- No enclosed/chambered target option (wind-sensitive)
- Premium US pricing
- SIT weighs 50 lb (heavy for field deployment)
- SIT only IP65 (not IP67 like LOMAH unit)
- Requires supersonic ammunition (V > 450 m/s)

### Relevance to Vietnamese Development
- Portable LOMAH concept is directly relevant (VN needs field-deployable)
- LSI innovation should be studied for multi-lane ranges
- Multi-comm architecture essential for VN's varied range infrastructure
- FPC display features set the user experience standard
- RM9K/10K software architecture is the benchmark for range control
- Solar charging option critical for tropical/remote VN locations
- Total system cost reduction of 50-60% achievable with local production
- Combining InVeris portability + TTS chambered design = superior product

---

*Analysis based entirely on publicly available information (product pages, ARCAT listings, press releases, newsletters, brochures, competitor datasheets).*
*Detection principle (TDOA-based acoustic shockwave triangulation) is well-established physics.*
*InVeris publicly describes their method as "triangulation of sound waves for hit location."*
