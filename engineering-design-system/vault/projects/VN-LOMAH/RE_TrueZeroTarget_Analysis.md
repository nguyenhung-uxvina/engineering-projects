---
project: VN-LOMAN
type: reverse_engineering
version: 1.0
created: 2026-02-06
status: active
methodology: Reverse Engineering (4-Phase D-M-I-R)
foreign_system: TrueZeroTarget
manufacturer: Steinert Sensing Systems
country: Norway
---

# REVERSE ENGINEERING ANALYSIS
## Steinert Sensing Systems TrueZeroTarget (Norway)
## Phân tích Kỹ thuật Đảo ngược - Hệ thống Bia điện tử LOMAH

---

# SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Foreign Designation** | TrueZeroTarget® Electronic Target System |
| **Manufacturer** | Steinert Sensing Systems |
| **Origin** | Norway (Oslo) |
| **Technology** | Acoustic LOMAH (Location Of Miss And Hit) |
| **Market Segment** | Military training, Law enforcement, Sport shooting, Hunting |
| **Price Range** | €3,490 (Individual) - €10,000+ (Range/OEM) |
| **Analysis Date** | 2026-02-06 |
| **Analysis Type** | Open Source (datasheets, web, publications) |

---

# PART 1: PHASE 1 - DIAGNOSIS (RECONNAISSANCE)

## 1.1 System Overview

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    TRUEZEROTARGET SYSTEM CONCEPT                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  SHOOTER                           TARGET                      DISPLAY       ║
║  ───────                           ──────                      ───────       ║
║                                                                               ║
║   ┌───┐                       ┌─────────────────┐            ┌─────────┐     ║
║   │   │                       │                 │            │         │     ║
║   │ O │        Supersonic     │  ┌───────────┐  │   Wi-Fi    │  TABLET │     ║
║   │/│\│  ───────bullet───────▶│  │   TARGET  │  │◄──────────▶│    or   │     ║
║   │ │ │    shock wave         │  │   FACE    │  │ (802.11)   │  PHONE  │     ║
║   │/ \│                       │  └───────────┘  │            │         │     ║
║   └───┘                       │                 │            └─────────┘     ║
║                               │  ○   ○   ○   ○  │ ← Acoustic sensors         ║
║                               │  (4+ microphones)│                            ║
║                               └─────────────────┘                            ║
║                                       │                                       ║
║                                       │ Processing                            ║
║                                       ▼                                       ║
║                               ┌─────────────────┐                            ║
║                               │   ELECTRONICS   │                            ║
║                               │ • Time capture  │                            ║
║                               │ • Position calc │                            ║
║                               │ • Wi-Fi xmit    │                            ║
║                               │ • LiFePO4 batt  │                            ║
║                               └─────────────────┘                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

## 1.2 Technical Specifications (Documented)

### 1.2.1 Detection System

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Sensor Type** | Ultrasonic transducers (microphones) | 4+ sensors per unit |
| **Detection Principle** | Acoustic supersonic shock wave | Time-of-arrival triangulation |
| **Accuracy (Center)** | ±3mm | At target center |
| **Accuracy (Edge)** | ±9mm | At 60cm target edges |
| **Min Bullet Velocity** | 440 m/s (Mach 1.3) | Supersonic requirement |
| **Caliber Range** | 4.3mm (.17) to 84mm | Wide compatibility |
| **Detection Window** | 600×600mm (standard) | Scalable to 4000×3000mm |
| **Shooting Angle** | Azimuth ±16°, Elevation ±5° | Limited angle acceptance |
| **Min Shot Interval** | 100ms | 600 rpm equivalent |
| **Built-in Chronograph** | Yes, 1% accuracy | Velocity measurement |
| **Temperature Compensation** | Yes | For acoustic velocity |

### 1.2.2 Physical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Dimensions** | 700×120×106mm | For 60cm sensor spacing |
| **Weight** | 4.0 kg | Portable |
| **Target Material** | Corrugated plastic 5mm or cardboard | User-replaceable |
| **IP Rating** | IP66 | Dust-tight, water jets |
| **Operating Temp** | -30°C to +70°C | Wide range |
| **Startup Time** | <10 seconds | Fast deployment |

### 1.2.3 Power System

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Battery Type** | LiFePO4 | Long life, safe chemistry |
| **Battery Capacity** | 3.2V × 12,000mAh | ~38.4 Wh |
| **Runtime** | Up to 16 hours | Continuous operation |
| **External Power** | 100-230VAC 50-60Hz | Via adapter |
| **Charging** | Included charger | Details not specified |

### 1.2.4 Connectivity

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Wi-Fi Standard** | IEEE 802.11 b/g | 2.4 GHz |
| **Wi-Fi Range** | Up to 300m | Line-of-sight |
| **Encryption** | WPA2 | Standard security |
| **Operating Modes** | AP mode (Individual), Infrastructure (Range) | Flexible deployment |
| **Extended Range** | Unlimited with access points | Network repeaters |

### 1.2.5 Software & Display

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Platforms** | Windows 7-10, Android, iOS | Cross-platform |
| **Response Time** | <1 second | Shot to display |
| **Display** | PC screen, tablet, smartphone | Flexible viewing |

## 1.3 Model Variants

| Model | Sensor Spacing | Target Size | Application | Price (€) |
|-------|----------------|-------------|-------------|-----------|
| **Individual 60cm** | 60cm | 60×60cm | Personal/hunting | 3,490 |
| **Individual 100cm** | 100cm | 100×100cm | Personal/hunting | TBD |
| **Range 60cm** | 60cm | 60×60cm | Multi-lane ranges | TBD |
| **Range 100cm** | 100cm | 100×100cm | Multi-lane ranges | TBD |
| **OEM** | Custom | Custom | Integration | Custom |

## 1.4 Competitive Landscape

| Manufacturer | System | Technology | Price Range | Notes |
|--------------|--------|------------|-------------|-------|
| **Steinert (Norway)** | TrueZeroTarget | Acoustic LOMAH | €3,490+ | Subject of this RE |
| **SIUS (Switzerland)** | HS10, HS15 | Acoustic | $2,000-5,000 | ISSF certified, 2mm accuracy |
| **Kongsberg (Norway)** | Various | Acoustic | $12,000+ | High-end military |
| **Oakwood (USA)** | H-Bar LOMAH | Acoustic | TBD | Long-range (5km radio) |
| **Zen Technologies (India)** | LOMAH Smart | Acoustic | TBD | Military training |
| **Hexta (Australia)** | Various | Optical | ~$1,300 AUD | Different technology |
| **Megalink (Norway)** | ML02/ML10 | Acoustic | ~$2,000 | Sport shooting |
| **NOPTEL (Finland)** | Various | Optical/Laser | TBD | Training systems |

---

# PART 2: PHASE 2 - MODELING (FUNCTIONAL RECONSTRUCTION)

## 2.1 Overall Function Statement

> **Detect and locate supersonic projectile impacts on/near a target and transmit precise position data wirelessly to a remote display device.**

Vietnamese: *Phát hiện và định vị vị trí đạn siêu âm trúng/gần bia và truyền không dây dữ liệu vị trí chính xác đến thiết bị hiển thị từ xa.*

## 2.2 Function Structure Diagram

```
FUNCTION STRUCTURE: TRUEZEROTARGET
═══════════════════════════════════════════════════════════════════════════════

OVERALL FUNCTION: Detect and locate supersonic projectile impacts
                  and display position wirelessly

F1: DETECT PROJECTILE PASSAGE
├── F1.1: Generate acoustic signature ────────── Bullet shock wave (external)
├── F1.2: Capture shock wave ─────────────────── Ultrasonic microphones
├── F1.3: Convert acoustic to electrical ─────── Piezoelectric transducers
├── F1.4: Timestamp arrival at each sensor ───── High-speed ADC + MCU
└── F1.5: Detect temperature (compensation) ──── Temperature sensor

F2: CALCULATE IMPACT POSITION
├── F2.1: Measure time differences ───────────── TDOA algorithm
├── F2.2: Apply temperature correction ────────── Speed of sound adjustment
├── F2.3: Triangulate position ───────────────── Geometric calculation
├── F2.4: Calculate velocity (optional) ──────── Time-of-flight
└── F2.5: Validate hit (in-bounds check) ─────── Software logic

F3: COMMUNICATE RESULTS
├── F3.1: Format data packet ─────────────────── Protocol encoding
├── F3.2: Establish Wi-Fi link ───────────────── 802.11 b/g radio
├── F3.3: Transmit data ──────────────────────── Wi-Fi transmission
├── F3.4: Handle connection (AP/Infra) ────────── Network management
└── F3.5: Encrypt data ───────────────────────── WPA2 encryption

F4: DISPLAY RESULTS (Client Device)
├── F4.1: Receive data ───────────────────────── Wi-Fi reception
├── F4.2: Decode position ────────────────────── Protocol decoding
├── F4.3: Render target image ────────────────── Graphics rendering
├── F4.4: Plot impact location ───────────────── Coordinate mapping
├── F4.5: Calculate group statistics ─────────── Statistical analysis
└── F4.6: Store shot history ─────────────────── Data logging

F_AUX: SUPPORT FUNCTIONS
├── F_AUX.1: Store electrical energy ─────────── LiFePO4 battery
├── F_AUX.2: Convert AC to DC ────────────────── Power adapter
├── F_AUX.3: Regulate voltage ────────────────── DC-DC converters
├── F_AUX.4: Protect electronics ─────────────── Conformal coating, IP66
├── F_AUX.5: Mount target face ───────────────── Target frame
└── F_AUX.6: Support/position system ─────────── Tripod/stand

═══════════════════════════════════════════════════════════════════════════════
TOTAL: 4 Main Functions + 1 Auxiliary = 5 Function Groups, 27 Subfunctions
═══════════════════════════════════════════════════════════════════════════════
```

## 2.3 Working Principle Analysis

### 2.3.1 Core Detection Principle: Time Difference of Arrival (TDOA)

```
TDOA TRIANGULATION PRINCIPLE
═══════════════════════════════════════════════════════════════════════════════

SENSOR ARRAY (Top view):
─────────────────────────────────────────────────────────────────────────────
                         Bullet path
                            ↓
                    ─ ─ ─ ─●─ ─ ─ ─ ─ ─ →
                            ╲
                             ╲ Shock wave cone
                              ╲
        S1 ○─────────────────────────────○ S2
           │                             │
           │      TARGET FACE            │
           │         ● Impact            │
           │      (x, y)                 │
           │                             │
        S3 ○─────────────────────────────○ S4

           ←─────── d (baseline) ────────→

TIMING DIAGRAM:
─────────────────────────────────────────────────────────────────────────────
        t1                 t2               t3                t4
         │                  │                │                  │
    S1 ──┼──                │                │                  │
         │ shock arrives    │                │                  │
         │                  │                │                  │
    S2 ──┼──────────────────┼──              │                  │
         │                  │ shock arrives  │                  │
         │                  │                │                  │
    S3 ──┼──────────────────┼────────────────┼──                │
         │                  │                │ shock arrives    │
         │                  │                │                  │
    S4 ──┼──────────────────┼────────────────┼──────────────────┼──
         │                  │                │                  │ shock arrives

Time differences: Δt12 = t2 - t1, Δt13 = t3 - t1, Δt14 = t4 - t1

CALCULATION:
─────────────────────────────────────────────────────────────────────────────
Distance difference: Δd = Δt × v_sound

For each sensor pair:
  d1 - d2 = Δt12 × v_sound(T)   ← Hyperbola 1
  d1 - d3 = Δt13 × v_sound(T)   ← Hyperbola 2

Impact point (x, y) = Intersection of hyperbolas

Speed of sound: v_sound(T) = 331.3 × √(1 + T/273.15) m/s
At 20°C: v_sound = 343 m/s

═══════════════════════════════════════════════════════════════════════════════
```

### 2.3.2 Working Principle Mapping

| Subfunction | Physical Effect | Form Design | Working Principle |
|-------------|-----------------|-------------|-------------------|
| F1.2 Capture shock wave | Acoustic pressure wave | Ultrasonic transducer | Piezoelectric microphone |
| F1.3 Convert acoustic→electrical | Piezoelectric effect | PZT or PVDF element | Direct piezoelectric conversion |
| F1.4 Timestamp arrival | Analog-to-digital conversion | High-speed ADC + MCU | Digital sampling (>1 MHz) |
| F1.5 Measure temperature | Thermal resistance change | NTC thermistor | Thermistor bridge |
| F2.3 Triangulate position | Geometric intersection | Algorithm | TDOA hyperbolic positioning |
| F3.2 Establish Wi-Fi | Electromagnetic radiation | 2.4 GHz radio + antenna | IEEE 802.11 protocol |
| F_AUX.1 Store energy | Electrochemical potential | LiFePO4 cells | Lithium iron phosphate battery |
| F_AUX.4 Protect electronics | Polymer barrier | Conformal coating + seals | IP66 encapsulation |

## 2.4 Energy/Material/Signal Flow

```
ENERGY-MATERIAL-SIGNAL FLOW DIAGRAM
═══════════════════════════════════════════════════════════════════════════════

                              EXTERNAL INPUTS
                                    │
            ┌───────────────────────┼───────────────────────┐
            │                       │                       │
            ▼                       ▼                       ▼
    ┌───────────────┐      ┌───────────────┐       ┌───────────────┐
    │  Bullet       │      │  AC Power     │       │  Temperature  │
    │  (kinetic)    │      │  (100-230V)   │       │  (ambient)    │
    └───────┬───────┘      └───────┬───────┘       └───────┬───────┘
            │                      │                       │
    [Shock wave]           [AC-DC convert]          [Temp sense]
            │                      │                       │
            ▼                      ▼                       ▼
    ┌───────────────┐      ┌───────────────┐       ┌───────────────┐
    │  Acoustic     │      │  DC Power     │       │  Temp Data    │
    │  Signal       │      │  (battery)    │       │  (digital)    │
    └───────┬───────┘      └───────┬───────┘       └───────┬───────┘
            │                      │                       │
    [Piezo convert]        [Regulate]              [Compensate]
            │                      │                       │
            ▼                      ▼                       ▼
    ┌───────────────┐      ┌───────────────┐       ┌───────────────┐
    │  Electrical   │◄─────│  Regulated    │──────►│  Corrected    │
    │  Signal       │      │  3.3V/5V      │       │  v_sound      │
    └───────┬───────┘      └───────────────┘       └───────┬───────┘
            │                                              │
    [ADC sample]                                    [Algorithm]
            │                                              │
            ▼                                              │
    ┌───────────────┐                                      │
    │  Digital      │◄─────────────────────────────────────┘
    │  Timestamps   │
    └───────┬───────┘
            │
    [TDOA calc]
            │
            ▼
    ┌───────────────┐
    │  Position     │
    │  (X, Y)       │
    └───────┬───────┘
            │
    [Wi-Fi transmit]
            │
            ▼
    ┌───────────────┐
    │  Display      │  ← OUTPUT
    │  (visual)     │
    └───────────────┘

═══════════════════════════════════════════════════════════════════════════════
```

## 2.5 Subsystem Decomposition

### 2.5.1 Estimated Subsystem Architecture

```
TRUEZEROTARGET SUBSYSTEM ARCHITECTURE (Estimated)
═══════════════════════════════════════════════════════════════════════════════

┌───────────────────────────────────────────────────────────────────────────┐
│                              SENSOR HEAD                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ MIC 1       │  │ MIC 2       │  │ MIC 3       │  │ MIC 4       │      │
│  │ (Piezo)     │  │ (Piezo)     │  │ (Piezo)     │  │ (Piezo)     │      │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘      │
│         │                │                │                │              │
│         └────────────────┴────────────────┴────────────────┘              │
│                                   │ (Analog signals)                      │
└───────────────────────────────────┼───────────────────────────────────────┘
                                    │
┌───────────────────────────────────┼───────────────────────────────────────┐
│                          ELECTRONICS MODULE                                │
│                                   │                                        │
│  ┌────────────────────────────────┼────────────────────────────────────┐  │
│  │            ANALOG FRONT-END                                          │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │  │
│  │  │ Preamp 1 │  │ Preamp 2 │  │ Preamp 3 │  │ Preamp 4 │            │  │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘            │  │
│  │       │             │             │             │                   │  │
│  │  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐            │  │
│  │  │ Filter 1 │  │ Filter 2 │  │ Filter 3 │  │ Filter 4 │            │  │
│  │  └────┬─────┘  └────┴─────┘  └────┬─────┘  └────┴─────┘            │  │
│  │       └────────────┬────────────────┴────────────┘                  │  │
│  └────────────────────┼────────────────────────────────────────────────┘  │
│                       │                                                    │
│  ┌────────────────────┼────────────────────────────────────────────────┐  │
│  │            DIGITAL PROCESSING                                        │  │
│  │                    │                                                 │  │
│  │  ┌─────────────────┴─────────────────┐                              │  │
│  │  │     MULTI-CHANNEL ADC            │   Temp                        │  │
│  │  │     (4+ channels, 1 MHz+)        │◄──Sensor                      │  │
│  │  └─────────────────┬─────────────────┘                              │  │
│  │                    │                                                 │  │
│  │  ┌─────────────────┴─────────────────┐                              │  │
│  │  │     MAIN MCU                      │                              │  │
│  │  │     (ARM Cortex-M or similar)     │                              │  │
│  │  │     • Timestamp capture           │                              │  │
│  │  │     • TDOA calculation            │                              │  │
│  │  │     • Temperature compensation    │                              │  │
│  │  │     • Protocol handling           │                              │  │
│  │  └─────────────────┬─────────────────┘                              │  │
│  │                    │                                                 │  │
│  └────────────────────┼────────────────────────────────────────────────┘  │
│                       │                                                    │
│  ┌────────────────────┼────────────────────────────────────────────────┐  │
│  │            COMMUNICATION                                             │  │
│  │                    │                                                 │  │
│  │  ┌─────────────────┴─────────────────┐                              │  │
│  │  │     Wi-Fi MODULE                  │                              │  │
│  │  │     (ESP32 or similar)            │                              │  │
│  │  │     • 802.11 b/g                  │                              │  │
│  │  │     • AP + Infrastructure mode    │                              │  │
│  │  │     • WPA2 encryption             │────────────────────────→ ANT │  │
│  │  └───────────────────────────────────┘                              │  │
│  │                                                                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │            POWER SYSTEM                                               │  │
│  │                                                                       │  │
│  │  ┌────────────┐    ┌────────────┐    ┌────────────┐                 │  │
│  │  │  AC/DC     │───▶│  CHARGER   │───▶│  LiFePO4   │                 │  │
│  │  │  Adapter   │    │  (BMS)     │    │  Battery   │                 │  │
│  │  │  (Ext)     │    │            │    │  12Ah      │                 │  │
│  │  └────────────┘    └────────────┘    └─────┬──────┘                 │  │
│  │                                            │                         │  │
│  │                                     ┌──────┴──────┐                  │  │
│  │                                     │  DC-DC      │                  │  │
│  │                                     │  Converters │                  │  │
│  │                                     │  3.3V, 5V   │                  │  │
│  │                                     └─────────────┘                  │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                           ENCLOSURE (IP66)                                  │
│  • Aluminum or reinforced plastic housing                                   │
│  • Conformal coating on electronics                                         │
│  • Sealed cable glands for sensors                                          │
│  • Operating: -30°C to +70°C                                               │
└────────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
```

---

# PART 3: DESIGN PARADIGM ANALYSIS

## 3.1 Observed Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **Safety margins** | LiFePO4 battery (safest Li chemistry), wide temp range | 4 | Conservative, reliability-focused |
| **Modularity** | Separate target face (replaceable), modular software | 4 | Designed for field service |
| **Material selection** | IP66 enclosure, mil-spec connectors likely | 4 | Premium, outdoor-focused |
| **Redundancy** | 4+ sensors (min 3 needed), no dual processors noted | 3 | Moderate redundancy |
| **Manufacturing** | Norwegian production, precision acoustic sensors | 4 | High-precision, low volume |
| **Usability** | Wi-Fi plug-and-play, multi-platform app | 5 | Consumer-grade UX |
| **Accuracy** | ±3mm at center | 5 | Very high precision |

**Overall Paradigm Score: 4.1/5** (Premium quality, field-rugged, user-friendly)

## 3.2 Designer's Paradigm Statement

> "Create a professional-grade acoustic target system that delivers military LOMAH accuracy in a plug-and-play package accessible to hunters and sport shooters, prioritizing ease of use and field reliability over cost."

## 3.3 Trade-off Analysis

| Trade-off | Choice Made | Alternative Forgone | Rationale |
|-----------|-------------|---------------------|-----------|
| **Accuracy vs. Cost** | High accuracy (±3mm) | Lower cost | Premium market positioning |
| **Wi-Fi vs. Wired** | Wi-Fi only | Wired option | Simplicity, no infrastructure |
| **Battery vs. AC** | Large battery (16h) | Smaller/lighter | Field independence |
| **Supersonic only** | Mach 1.3+ required | Subsonic capability | Simpler algorithm, higher accuracy |
| **2.4 GHz vs. 5 GHz** | 2.4 GHz only | 5 GHz option | Range over bandwidth |

## 3.4 Strengths and Limitations

### Strengths
1. **Plug-and-play simplicity** - No wiring, pit, or infrastructure required
2. **High accuracy** - ±3mm rivals professional range systems
3. **Wide environmental range** - -30°C to +70°C, IP66
4. **Long battery life** - 16 hours enables full-day use
5. **Cross-platform software** - Windows, Android, iOS
6. **Built-in chronograph** - Added value for load development
7. **ITAR-free** - Easy export, no restrictions

### Limitations
1. **Supersonic only** - Cannot track subsonic ammunition
2. **Limited angle** - ±16° azimuth, ±5° elevation
3. **Price** - €3,490 is premium segment
4. **Wi-Fi range** - 300m may limit long-range use
5. **No miss location beyond target** - LOMAH window limited

---

# PART 4: PHASE 3 - INTERVENTION (APPLICATION STRATEGY)

## 4.1 Indigenous Development Opportunity

### 4.1.1 Market Opportunity (Vietnam)

| Segment | Potential Users | Units (5-yr Est.) | Notes |
|---------|-----------------|-------------------|-------|
| **Military Ranges** | Army, Navy, Air Force | 200-500 | Basic rifle marksmanship |
| **Police Training** | Public Security, Mobile Police | 100-200 | Qualification ranges |
| **Sport Shooting** | Clubs, national team | 50-100 | Competition training |
| **Border Guards** | Border Defense Force | 50-100 | Remote post training |
| **Private Ranges** | Commercial, hunting clubs | 20-50 | Emerging market |
| **TOTAL** | | **420-950 units** | |

**Total Addressable Market (5-year):** 500-1,000 units × $2,000-3,000 = **$1-3M**

### 4.1.2 Competitive Position

| Factor | Import (TrueZero) | Indigenous (VN-LOMAN) | Advantage |
|--------|-------------------|----------------------|-----------|
| Price | €3,490 (~$3,800) | Target: $1,500-2,000 | 50% savings |
| Lead time | 4-8 weeks | 2-4 weeks | Faster |
| Support | Remote (Norway) | Local | Better |
| Customization | Limited | Full | Flexible |
| Local content | 0% | 70%+ | Self-reliance |
| Integration | Standard | Custom (Vietnamese app) | Language, features |

## 4.2 Technology Insertion Candidates

### 4.2.1 Subsystem-Level Analysis

| Subsystem | Foreign Solution | Local Feasibility | Recommendation |
|-----------|------------------|-------------------|----------------|
| **Acoustic sensors** | Piezoelectric mics | HIGH - COTS available | Use MEMS microphones |
| **Analog front-end** | Custom preamp/filter | HIGH - Standard design | Design in-house |
| **ADC** | Multi-channel high-speed | HIGH - Available ICs | Use ADS131M04 or similar |
| **MCU** | ARM Cortex-M | HIGH - Standard | Use STM32 or ESP32 |
| **Wi-Fi module** | Integrated | HIGH - ESP32 excellent | Use ESP32-S3 |
| **Battery** | LiFePO4 12Ah | HIGH - Available | Source from China |
| **Enclosure** | IP66 aluminum | HIGH - Local capability | Local fabrication |
| **Software** | Proprietary | MEDIUM - Custom dev | Develop Vietnamese app |

### 4.2.2 Critical Technology Gaps

| Gap | Description | Mitigation |
|-----|-------------|------------|
| **TDOA Algorithm** | Precision timing and calculation | Implement in MCU firmware, test extensively |
| **Temperature Compensation** | Acoustic velocity correction | Characterize across temp range |
| **Calibration Procedure** | Sensor position accuracy | Develop factory calibration jig |
| **App Development** | Cross-platform software | Use Flutter or React Native |

## 4.3 Proposed Indigenous System: VN-LOMAN

### 4.3.1 System Concept

```
VN-LOMAN CONCEPT
═══════════════════════════════════════════════════════════════════════════════

                    ┌──────────────────────────────────────────────────────┐
                    │              VN-LOMAN-100                             │
                    │         (60×60cm Detection Window)                    │
                    ├──────────────────────────────────────────────────────┤
                    │                                                       │
                    │  ┌─────────────────────────────────────────────────┐ │
                    │  │                TARGET FACE                       │ │
                    │  │           (Replaceable cardboard)               │ │
                    │  │                                                  │ │
                    │  │              ┌───────────┐                       │ │
                    │  │              │   ●       │                       │ │
                    │  │              │  Impact   │                       │ │
                    │  │              │  display  │                       │ │
                    │  │              └───────────┘                       │ │
                    │  │                                                  │ │
                    │  └─────────────────────────────────────────────────┘ │
                    │                                                       │
                    │  ○────────────────────────────────────────────────○  │
                    │  S1               SENSOR BAR                      S2 │
                    │                                                       │
                    │  ┌─────────────────────────────────────────────────┐ │
                    │  │              ELECTRONICS BOX                     │ │
                    │  │  • ESP32-S3 (MCU + Wi-Fi)                       │ │
                    │  │  • 4-ch ADC (ADS131M04)                         │ │
                    │  │  • LiFePO4 10Ah battery                         │ │
                    │  │  • USB-C charging                               │ │
                    │  │  • Status LEDs                                  │ │
                    │  └─────────────────────────────────────────────────┘ │
                    │                                                       │
                    │  ○────────────────────────────────────────────────○  │
                    │  S3               SENSOR BAR                      S4 │
                    │                                                       │
                    └──────────────────────────────────────────────────────┘
                                          │
                                          │ Tripod mount
                                          ▼
                                     ┌─────────┐
                                     │ Tripod  │
                                     └─────────┘

═══════════════════════════════════════════════════════════════════════════════
```

### 4.3.2 Preliminary Specifications (VN-LOMAN-100)

| Parameter | Target | Notes |
|-----------|--------|-------|
| Detection window | 60×60cm | Match TrueZero |
| Accuracy | ±5mm center, ±15mm edge | Slightly relaxed for cost |
| Min bullet velocity | 400 m/s (Mach 1.2) | Slightly lower threshold |
| Caliber range | 5.56mm to 12.7mm | Focus on military calibers |
| Weight | ≤5 kg | Portable |
| Battery life | ≥12 hours | Sufficient for training day |
| Wi-Fi range | ≥200m | Adequate for ranges |
| Operating temp | -10°C to +55°C | Vietnam conditions |
| IP rating | IP65 | Splashproof |
| Price target | $1,500-2,000 | 50% of import |
| Local content | ≥70% | Self-reliance target |

### 4.3.3 Preliminary BOM Estimate

| Subsystem | Key Components | Est. Cost ($) | Local % |
|-----------|----------------|---------------|---------|
| Sensors | 4× MEMS microphones (ICS-43434) | $20 | 0% (import) |
| Analog | Preamps, filters (op-amps) | $15 | 50% |
| ADC | ADS131M04 (4-ch, 24-bit) | $25 | 0% (import) |
| MCU | ESP32-S3-WROOM-1 | $8 | 0% (import) |
| Wi-Fi | Integrated in ESP32 | $0 | - |
| Power | LiFePO4 10Ah + BMS + charger | $80 | 30% |
| Enclosure | Aluminum + gaskets | $100 | 100% |
| PCB | Custom 4-layer | $30 | 100% |
| Mechanical | Frame, sensor mounts | $50 | 100% |
| Assembly/Test | Labor, QC | $50 | 100% |
| **TOTAL** | | **$378** | ~65% |

**Selling Price:** $1,500-2,000 → **Gross Margin: 60-75%**

---

# PART 5: PHASE 4 - REFLECTION

## 5.1 Key Insights from RE Analysis

1. **TDOA is the core technology** - All competitive systems use similar acoustic detection. The differentiation is in implementation quality, software UX, and form factor.

2. **±3mm accuracy is achievable** - With good sensor placement, fast ADC, and temperature compensation, ±5mm is realistic for indigenous development.

3. **ESP32 is ideal platform** - Combines MCU and Wi-Fi in one chip, reducing complexity and cost.

4. **Temperature compensation is critical** - Speed of sound varies ~0.6 m/s per °C. Must implement real-time correction.

5. **Software is the differentiator** - Hardware is increasingly commoditized. Vietnamese-language app with local features adds value.

6. **LiFePO4 is the right choice** - Safe, long-lasting, wide temperature range. Worth the slight cost premium.

## 5.2 Recommended Next Steps

```
VN-LOMAN DEVELOPMENT ROADMAP
═══════════════════════════════════════════════════════════════════════════════

PHASE 1: PROOF OF CONCEPT (Month 1-3)
─────────────────────────────────────────────────────────────────────────────
☐ Build breadboard prototype with ESP32 + 4 MEMS mics
☐ Implement basic TDOA algorithm
☐ Validate ±10mm accuracy in lab
☐ Develop minimal viable app (Android)
☐ Budget: $2,000

PHASE 2: ENGINEERING PROTOTYPE (Month 4-6)
─────────────────────────────────────────────────────────────────────────────
☐ Design custom PCB
☐ Develop IP65 enclosure
☐ Implement temperature compensation
☐ Add LiFePO4 power system
☐ Field testing at live range
☐ Validate ±5mm accuracy
☐ Budget: $10,000

PHASE 3: PILOT PRODUCTION (Month 7-9)
─────────────────────────────────────────────────────────────────────────────
☐ DfM review with local manufacturers
☐ Build 10 pilot units
☐ Field trials with Army/Police
☐ Refine software based on feedback
☐ Cost optimization
☐ Budget: $30,000

PHASE 4: PRODUCTION (Month 10+)
─────────────────────────────────────────────────────────────────────────────
☐ Establish production line
☐ Supplier agreements
☐ Quality control procedures
☐ Marketing and sales
☐ First customer deliveries

TOTAL NRE BUDGET: ~$50,000
TIME TO MARKET: 10-12 months

═══════════════════════════════════════════════════════════════════════════════
```

## 5.3 Lessons Learned

| Aspect | Lesson | Application |
|--------|--------|-------------|
| **Market position** | Premium import leaves room for value alternative | Target 50% price point |
| **Technology** | Core TDOA principle is well-documented, not proprietary | Can develop independently |
| **Components** | All key components are COTS, no exotic parts | Low technical risk |
| **Differentiation** | Software UX and local support are key differentiators | Invest in app development |
| **Standards** | No mandatory certifications beyond CE | Low regulatory barrier |

---

# APPENDIX A: SOURCES

## Web Sources
- [Steinert Sensing Systems - TrueZeroTarget Product Page](https://www.steinertsensingsystems.com/product-details/truezerotarget/)
- [Steinert Sensing Systems - Products](https://www.steinertsensingsystems.com/products/)
- [U.S. Army - New LOMAH Range System](https://www.army.mil/article/93978/new_range_system_passes_test)
- [Inveris Training - LOMAH System](https://www.inveristraining.com/live-fire-training/military/lomah-location-of-miss-and-hit/)
- [SIUS AG - Electronic Target Systems](https://www.sius.com/en)
- [Zen Technologies - LOMAH Smart Target](https://www.zentechnologies.com/lomah-smart-electronic-target-system.php)
- [Oakwood Controls - H-Bar LOMAH](https://www.ssusa.org/content/oakwood-controls-h-bar-lomah-electronic-target-system/)

## Technical References
- Time Difference of Arrival (TDOA) positioning algorithms
- Speed of sound temperature dependence
- MEMS microphone datasheets (InvenSense ICS-43434)
- ESP32-S3 technical reference manual
- ADS131M04 datasheet (Texas Instruments)

---

# APPENDIX B: DOCUMENT LINKS

## Project Documents (To Be Created)
- [[VN-LOMAN_Product_Spec|VN-LOMAN Product Specification]]
- [[VN-LOMAN_Requirements|VN-LOMAN Requirements List]]
- [[VN-LOMAN_Prototype_BOM|VN-LOMAN Prototype BOM]]

## Reference Documents
- [[SKILL_reverse_engineering|Reverse Engineering Skill]]
- [[SKILL_conceptual_design|Conceptual Design Skill]]

---

# REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-06** | **Initial RE analysis. TrueZeroTarget (Steinert, Norway) fully documented. Function structure with 27 subfunctions. TDOA working principle analyzed. VN-LOMAN indigenous system proposed at $1,500-2,000 (50% of import). 10-12 month development timeline, $50,000 NRE.** |

---

*This reverse engineering analysis follows the 4-Phase D-M-I-R methodology for systematic extraction of design knowledge from foreign military/commercial systems.*

**Analysis Status:** 🟢 **COMPLETE**
