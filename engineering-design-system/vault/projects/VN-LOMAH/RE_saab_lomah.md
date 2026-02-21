---
project: VN-LOMAH
phase: 0
type: reverse-engineering
subject: Saab Training & Simulation LOMAH (Sweden)
version: 1.0
created: 2026-02-06
status: complete
---

# RE: Saab Training & Simulation LOMAH - Sweden
## Reverse Engineering Analysis from Public Sources

---

## 1. COMPANY PROFILE

| Item | Detail |
|------|--------|
| **Company** | Saab Training Systems AB (operating as Saab Training & Simulation) |
| **HQ** | Stensholmsvagen 20, Stensholm, Huskvarna, Sweden |
| **Parent** | Saab AB (Stockholm: SAAB-B.ST), Business Area: Dynamics |
| **Acoustic scoring origin** | Air Target Sweden AB (Osterogatan 1, Kista, Sweden) |
| **Employees** | 900+ (T&S unit); 500+ outside Sweden |
| **Subsidiaries** | Czech Republic (~120), USA (Orlando, FL), UK, Germany, Norway, Finland, Netherlands, Canada |
| **Live fire installed base** | 30,000+ targets delivered to 25 countries |
| **Acoustic scoring reach** | 30+ countries since 1956 (Air Target Sweden) |
| **Heritage** | 60+ years ("targets delivered 40 years ago are still in operation") |
| **Key products** | LOMAH SASS-4/9, AVTI, BT46/BT47, GAMER CTC, EXCON, Target Lifters |

### Historical Lineage

| Year | Event |
|------|-------|
| 1935 | Svensk Flygtjanst AB founded by Tor Eliasson (military flying school) |
| 1956 | Acoustic scoring development begins at Vidsel Test Range (Ulf Sellman) |
| 1977 | Merged under Swedair; by 1978 delivered to 15 nations |
| 1989 | Swedair privatized → Air Target Sweden AB (Kista) |
| 1990s | Saab Training Systems AB established in Huskvarna; BT46 introduced |
| 1991 | Patent WO1991010876A1 filed: calibration-free acoustic scoring |
| 1999 | Saab AB acquired Celsius AB (Bofors parent), consolidating defense training |
| 2019 | "Beyond Live" concept announced at I/ITSEC |
| 2025 | AVTI unveiled at IT2EC Oslo; AI-based AAR announced |
| Present | Air Target Sweden AB operates as SOFF member, supplies acoustic scoring globally |

Saab has a **unique dual heritage**: Air Target Sweden AB (Kista) specializes in acoustic scoring technology since 1956, while Saab Training Systems AB (Huskvarna) provides the complete live fire training ecosystem. This gives Saab one of the longest pedigrees in electronic scoring worldwide.

---

## 2. PRODUCT FAMILY OVERVIEW

```
Saab Training & Simulation - Live Fire Portfolio
│
├── Electronic Scoring (LOMAH)
│   ├── SASS-4 (4 pressure transducers) ←── Standard config
│   ├── SASS-9 (9 pressure transducers) ←── Extended accuracy/coverage
│   └── Box Targets ←── Subsonic projectiles
│
├── AVTI (Advanced Vulnerability Target Interface)
│   ├── WDU (Wireless Detector Unit) ←── Laser, <1000m
│   ├── WRDU (Wireless Retro Reflector Unit) ←── Extended range, >1000m
│   ├── AVC (Advanced Vulnerability Computer) ←── GNSS, pixel model
│   └── Pixel vulnerability models ←── 1cm² infantry, 10cm² vehicle
│
├── Target Mechanisms (Host Platforms)
│   ├── SIT (Stationary Infantry Target) ←── Pop-up with LOMAH
│   ├── SAT (Stationary Armour Target) ←── Half/full-scale
│   ├── MIT (Moving Infantry Target) ←── Cable-driven
│   ├── MAT (Moving Armour Target) ←── Self-propelled/cable
│   └── Turning/Swivel Targets ←── Friend-or-foe training
│
├── Range Control Software
│   ├── EXCON / "Expert" ←── Exercise control, AAR
│   ├── AI-based AAR (announced Dec 2025)
│   ├── DAN (Distribution & Acquisition Network)
│   └── HoloLens Sandbox (3D tracking)
│
├── Laser Simulation (CTC)
│   ├── BT46 Mk III (Vehicle laser engagement)
│   ├── BT47 SAT (Infantry small arms transmitter)
│   ├── GAMER (Mobile Combat Training Centre)
│   └── TESS (Tactical Engagement Simulation System)
│
└── Display & Reporting
    ├── VDU-1 (Visual Display Unit at firing point)
    ├── ROPU (Range Office Presentation Unit, 10 lanes)
    └── AAR / Hit reports / Database / Printing
```

---

## 3. LOMAH SYSTEM ARCHITECTURE

### 3.1 System Topology

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAAB LOMAH SASS-4/9                           │
│                                                                 │
│  TARGET AREA                           FIRING POINT / RANGE OFF │
│  ┌──────────┐     cable    ┌────────┐    radio    ┌──────────┐  │
│  │ BSU-4/9  │─────────────→│ TPU-2  │────────────→│  VDU-1   │  │
│  │ (Beam    │              │(Target │             │ (Visual  │  │
│  │  Sensor  │              │ Proc.  │             │  Display │  │
│  │  Unit)   │              │ Unit)  │             │  Unit)   │  │
│  └──────────┘              └────────┘             └──────────┘  │
│       │                         │                      │        │
│  4 or 9 pressure           12 VDC                 Near gunner  │
│  transducers               battery                 Sun hood     │
│                                 │                                │
│                            radio link                           │
│                                 │                                │
│                            ┌────────┐                           │
│                            │  ROPU  │  (Range Office            │
│                            │ Up to  │   Presentation Unit)      │
│                            │10 lanes│                           │
│                            └────────┘                           │
│                                 │                                │
│                         ┌──────────────┐                        │
│                         │   EXCON /    │                        │
│                         │  "Expert"    │                        │
│                         │  Exercise    │                        │
│                         │  Management  │                        │
│                         └──────────────┘                        │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Detection Principle: Calibration-Free Acoustic Scoring

Saab's LOMAH uses the **SASS (Saab Acoustic Scoring System)** -- a patented calibration-free method:

**Step 1: Shockwave Generation**
A supersonic projectile (≥Mach 1.3, ~440 m/s) generates a conical shockwave (Mach cone). The cone half-angle:
```
μ = arcsin(1/Mp)    where Mp = Mach number of projectile
```

**Step 2: Pressure Detection**
4 (or 9) pressure transducers detect the shockwave arrival. The system uses Time-Difference-of-Arrival (TDOA) -- measuring the precise time the shockwave front reaches each transducer.

**Step 3: Triangulation**
Using known sensor spacing and computed arrival time differences, the system calculates directional vectors toward the projectile trajectory, determining X,Y coordinates relative to the target plane.

**Step 4: Calibration-Free Innovation (Key Differentiator)**
The patented design **eliminates the need for an extra reference measurement** to gauge the current speed of sound. Other systems require a calibration shot; SASS derives speed of sound from the measurements themselves using purely time-based calculations. This is protected by patent WO1991010876A1.

```
Physics of Calibration-Free Detection:

     Projectile (Mp ≥ 1.3)
         ●──────────────────→ V_projectile
        /│\
       / │ \ Mach cone
      /  │  \
     /   │   \  μ = arcsin(V_sound / V_projectile)
    /    │    \
───T1───T2───T3───T4──── Sensor Plane (BSU)
   ↓    ↓    ↓    ↓
   t1   t2   t3   t4    (arrival times)

   Δt12 = t2 - t1       (time differences)
   Δt13 = t3 - t1
   Δt14 = t4 - t1

   → System solves for (X, Y) using ONLY Δt values
   → No calibration shot needed
   → No speed-of-sound measurement required
   → Temperature compensation is IMPLICIT
```

### 3.3 SASS-4 vs SASS-9

| Parameter | SASS-4 | SASS-9 |
|-----------|--------|--------|
| **Transducer count** | 4 | 9 |
| **Typical use** | Standard infantry scoring | Extended coverage / enhanced accuracy |
| **Detection zone** | ~3×2.5m (infantry) | Larger zone, higher redundancy |
| **Cost** | Lower | Higher |
| **Applications** | Standard shooting ranges | Complex multi-target setups |

---

## 4. DETAILED COMPONENT SPECIFICATIONS

### 4.1 Beam Sensor Unit (BSU-4/9)

| Parameter | Specification |
|-----------|--------------|
| **Designations** | BSU-4 (4 transducers), BSU-9 (9 transducers) |
| **Sensor type** | Pressure transducers (microphones) |
| **Configuration** | Two delta arrays (per TTS-compatible documentation) |
| **Mounting** | Positioned below and in front of the target, on bar/frame structure |
| **Detection method** | Mach cone time-of-arrival measurement |
| **Detection zone** | 3×2.5m (infantry), 4×3m (armor) |
| **Detection azimuth** | ±20 degrees |
| **Detection elevation** | ±5 degrees |
| **Built-In Test (BIT)** | Displays: target type, firmware version, BIT status, comm details, supply voltage, error messages, hit count, holder position |
| **Enclosure** | Ballistic protection, weather-resistant |
| **Compatibility** | Retrofittable onto existing infantry/armor targetry; cross-vendor compatible |

### 4.2 Target Processor Unit (TPU-2)

| Parameter | Specification |
|-----------|--------------|
| **Designation** | TPU-2 |
| **Input** | Cable connection from BSU-4/9 |
| **Function** | Processes sensor timestamps, executes triangulation, computes (X,Y) position |
| **Power** | 12 VDC battery (field), 110/230 VAC (mains) |
| **Communication** | Radio link to VDU-1 and ROPU (real-time data transmission) |
| **Processing** | Decodes control signals, processes timestamps, performs scoring calculations |
| **Output data** | X,Y coordinates, hit/miss classification, shot statistics |
| **Environmental comp.** | Implicit in calibration-free algorithm |

### 4.3 Visual Display Unit (VDU-1)

| Parameter | Specification |
|-----------|--------------|
| **Designation** | VDU-1 |
| **Location** | Near gunner at firing point |
| **Features** | Sun protection hood included |
| **Display** | Color monitor, graphical X/Y coordinate display |
| **Data shown** | Salvo center, standard deviation, tabulated rounds, points, lane/target status, processor status |
| **Output** | Printable results, multiple target figure options (soldier silhouettes, ten-ring standards) |

### 4.4 Range Office Presentation Unit (ROPU)

| Parameter | Specification |
|-----------|--------------|
| **Scalability** | Up to 10 lanes with multiple SASS units per lane |
| **Function** | Centralized monitoring and control of all lanes |
| **Calculations** | Salvo center, mean miss distance, total scored rounds |
| **Output** | Tabular round-by-round results, printable reports, database storage |
| **Multi-target** | Control station can receive scoring data from up to 6 different targets (ATG variant) |

---

## 5. PERFORMANCE SPECIFICATIONS

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Accuracy** | ±10mm at ~1,200m | Calibration-free |
| **Minimum projectile velocity** | Mach 1.3 (~440 m/s) | Supersonic only |
| **Caliber range** | All supersonic (.22 to 120mm) | Infantry through armor |
| **Detection azimuth** | ±20° | |
| **Detection elevation** | ±5° | |
| **Calibration** | None required | Patented calibration-free technology |
| **Detection zone (infantry)** | 3 × 2.5m | BSU-4 standard |
| **Detection zone (armor)** | 4 × 3m | BSU-9 or extended config |
| **FASIT compliant** | Yes | US Army standard |
| **Operating temperature** | -25°C to +70°C | Estimated (military standard) |
| **IP rating** | IP67 (estimated) | Military-grade outdoor equipment |
| **Power** | 12 VDC (field) / 110-230 VAC (mains) | |
| **Operational longevity** | 40+ years demonstrated | "Targets from 40 years ago still in operation" |

### Accuracy Comparison with Competitors

| Manufacturer | Accuracy | Min Velocity | Calibration |
|-------------|----------|-------------|-------------|
| **Saab SASS-4/9** | **±10mm** | **Mach 1.3 (~440 m/s)** | **Calibration-free** |
| Polytronic H-Bar | ±5mm | 350 m/s | Required |
| InVeris LOMAH | <5mm | Supersonic | Required |
| TTS LOMAH | ±10mm | Mach 1.3 | Calibration-free (TTS variant) |
| Zen Technologies | ±5mm (est.) | Supersonic | Required |

Saab's key differentiator is the **calibration-free operation** -- no reference shot needed, critical for operational efficiency and reducing range downtime.

---

## 6. AVTI (ADVANCED VULNERABILITY TARGET INTERFACE)

Unveiled at **IT2EC 2025 in Oslo** (Janes Defence News).

### 6.1 System Components

| Component | Function |
|-----------|----------|
| **WDU (Wireless Detector Unit)** | Laser detectors matching Gamer TESS; engagements ≤1,000m |
| **WRDU (Wireless Retro Reflector Unit)** | Extended-range variant; engagements >1,000m |
| **AVC (Advanced Vulnerability Computer)** | Cable-connected to target; GNSS equipped; power + data |
| **Control Software** | Tablet-hosted interface |

### 6.2 FCC Registration (WDU24A)

| Parameter | Detail |
|-----------|--------|
| **FCC ID** | R4AWDU24A |
| **Applicant** | Saab Defense and Security USA LLC |
| **User Manual** | 50 pages, 120.11 KB PDF |
| **Created** | 2011-12-14 |
| **Detectors** | 1 detector + 1 strobe hit indicator per WDU |
| **Optional** | 2 reflectors per WDU |

### 6.3 Pixel-Based Vulnerability Model

| Target Type | Pixel Resolution | Application |
|-------------|-----------------|-------------|
| **Infantry** | 1 cm² | High-precision kill zone modeling |
| **Vehicle** | 10 cm² | Armor vulnerability mapping |

- Each pixel assigned individual vulnerability value
- Different vulnerability models configurable via AVC or system controller
- Enables **realistic target behavior** based on well-defined vulnerability zones
- Compatible with both live ammunition AND laser systems

### 6.4 AVTI Communication Architecture

```
[WDU/WRDU] ──wireless──→ [AVC (GNSS)] ──VHF + Bluetooth──→ [Tablet Software]
                              │
                         cable to target
                         (power + data)
```

### 6.5 Wireless Target System (WTS) Components (FCC Filing)

| Component | Function |
|-----------|----------|
| WDU | Wireless Detector Unit (with/without reflectors) |
| DAN antenna | Distribution and Acquisition Network antenna |
| MSA | GPS receiver |
| WCU | Wireless Control Unit |
| Battery | 1-cell / 2-cell options |
| Loudspeaker | Audio feedback |
| IBU/VAD | Interface/Visual Alert Device |
| WLN antenna + splitter | Wireless Local Network |
| Power/adapter cables | Interconnection |

**Key Innovation**: AVTI uses the **same laser detectors as Gamer TESS** (tactical engagement simulation system), enabling unified live fire + laser simulation on the same targets. This is a significant integration advantage.

---

## 7. TARGET LIFTER SYSTEMS

### 7.1 Stationary Infantry Target (SIT)

| Feature | Detail |
|---------|--------|
| **Type** | Remote-controlled pop-up target |
| **Silhouettes** | US Army and NATO standard |
| **LOMAH integration** | Can be equipped with SASS-4/9 sensors |
| **Variant** | SIT with Swivel target holder (turning/friend-or-foe) |
| **Scenarios** | Programmable exposure/conceal sequences |

### 7.2 Stationary Armour Target (SAT)

| Feature | Detail |
|---------|--------|
| **Variants** | Half-scale and full-scale tank flank/frontal silhouettes |
| **Target arms** | Adjustable elevation |
| **LOMAH** | BSU-9 or extended configuration for larger detection zone |

### 7.3 Moving Infantry Target (MIT)

| Feature | Detail |
|---------|--------|
| **Drive** | Cable-driven |
| **Speed** | Variable-speed movement |
| **Action** | Rapid conceal/expose capability |

### 7.4 Moving Armour Target (MAT)

| Feature | Detail |
|---------|--------|
| **Drive** | Self-propelled or cable-pulled |
| **Speed** | High-speed movement capability |
| **Design** | Modular and portable |
| **Trails** | Systems allowing curved movement paths |

### 7.5 Turning/Swivel Targets

| Feature | Detail |
|---------|--------|
| **Application** | Friend-or-foe close-combat training |
| **LOMAH** | Compatible with SASS sensor system |
| **Safety** | Optional ballistic shield for ricochet prevention |
| **Configuration** | Fixed and portable options |

---

## 8. RANGE CONTROL & EXERCISE MANAGEMENT

### 8.1 EXCON / "Expert" Software

| Capability | Detail |
|------------|--------|
| **Automated scenarios** | Programming target exposure sequences |
| **Target control** | Individual and group target management |
| **Real-time data** | Online status monitoring, hit presentation |
| **Hit reports** | Detailed scoring with X/Y coordinates |
| **AAR** | After-Action Review with playback |
| **Troubleshooting** | Range diagnostic tools |
| **AI AAR** | Announced Dec 2025; imports EXCON data, enriches with doctrine/geography/climate |
| **HoloLens Sandbox** | Real-time 3D tracking (announced 2019) |
| **3D terrain** | One World Terrain (Vricon) photo-realistic maps |

### 8.2 DAN (Distribution & Acquisition Network)

| Parameter | Detail |
|-----------|--------|
| **Function** | Communication backbone for training exercises |
| **Architecture** | Proprietary radio network with microwave backbone |
| **Data flow** | Target area → DAN → Exercise Control stations |
| **Components** | DAN antennas, Manpack 300 (portable control) |

### 8.3 BT46/BT47 Laser Simulation (Cross-Reference)

| System | Application |
|--------|-------------|
| **BT46 Mk III** | Vehicle laser engagement; ballistic computers + gyros; CBL for RWS; 20+ countries |
| **BT47 SAT** | Infantry small arms transmitter; adjusts to each weapon's firing conditions |
| **GAMER** | Mobile Combat Training Centre; TESS; NATO interoperable |

Integration note: AVTI bridges live fire (LOMAH) and laser simulation (BT46/BT47/GAMER) by using shared laser detector technology.

---

## 9. COMMUNICATION SYSTEMS

| Protocol | Application | Range/Detail |
|----------|-------------|-------------|
| **VHF Radio** | AVTI AVC ↔ tablet; DAN network; TPU ↔ VDU/ROPU | Primary C2 link |
| **Bluetooth** | AVTI AVC ↔ tablet control software | Short-range config |
| **Ethernet** | System backbone (100BaseT) | TCP/IP, IPv6 support |
| **DAN** | Proprietary training comm network | Microwave backbone |
| **Wi-Fi** | Display tablets, short-range data | 2-400m, extendable |
| **Radio link** | TPU ↔ VDU/ROPU scoring data | Real-time transmission |
| **FASIT** | US Army standard target communication | TCP/IP over Ethernet |

---

## 10. POWER SYSTEMS

| Option | Application | Detail |
|--------|-------------|--------|
| **12 VDC** | Primary field power (TPU, target area) | Battery-powered for deployment |
| **110 VAC** | Mains power (US standard) | Range infrastructure |
| **230 VAC** | Mains power (European standard) | Range infrastructure |
| **Lithium battery** | Portable systems | Up to 10 hours per charge |
| **Solar** | Remote installations | Solar charging for off-grid sites |
| **PDD batteries** | WTS system (WDU/WCU) | Per FCC documentation |

---

## 11. FUNCTIONAL DECOMPOSITION (Pahl & Beitz)

### 11.1 Overall Function

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAAB LOMAH SASS-4/9                           │
│                                                                 │
│  INPUT:                          OUTPUT:                        │
│  • Supersonic projectile         • X,Y impact coordinates       │
│    (≥ Mach 1.3)                  • Hit/miss classification      │
│  • Power (12VDC/110-230VAC)      • Shot statistics              │
│  • Control commands              • Real-time display            │
│                                  • Printed reports              │
│  FUNCTION:                       • AAR data                     │
│  "Detect supersonic projectile                                  │
│   trajectory and determine                                      │
│   impact location using                                         │
│   calibration-free acoustic                                     │
│   scoring"                                                      │
└─────────────────────────────────────────────────────────────────┘
```

### 11.2 Sub-Function Structure

```
F0: Detect & Score Supersonic Projectile (Calibration-Free)
│
├── F1: SENSE - Shockwave Detection
│   ├── F1.1: Receive acoustic shockwave (pressure transducers × 4/9)
│   ├── F1.2: Convert pressure to electrical signal
│   ├── F1.3: Filter & condition signal (bandpass, AGC)
│   └── F1.4: Detect shockwave arrival time (threshold/zero-crossing)
│
├── F2: PROCESS - TDOA Calculation (Calibration-Free)
│   ├── F2.1: Timestamp shockwave arrival at each transducer
│   ├── F2.2: Calculate time differences (Δt12, Δt13, Δt14...)
│   ├── F2.3: Solve calibration-free equations (time-only)
│   ├── F2.4: Compute X,Y coordinates in target plane
│   └── F2.5: Classify hit/miss against target silhouette
│
├── F3: COMMUNICATE - Data Transmission
│   ├── F3.1: Encode scoring data
│   ├── F3.2: Transmit via radio link to VDU-1
│   ├── F3.3: Transmit to ROPU (multi-lane aggregation)
│   └── F3.4: Interface with EXCON exercise management
│
├── F4: DISPLAY - Result Presentation
│   ├── F4.1: Show X,Y on color monitor (VDU-1)
│   ├── F4.2: Overlay on target silhouette graphic
│   ├── F4.3: Calculate salvo center & standard deviation
│   ├── F4.4: Tabulate individual rounds with scoring
│   └── F4.5: Generate printable reports
│
├── F5: POWER - Energy Management
│   ├── F5.1: Accept 12VDC / 110VAC / 230VAC
│   ├── F5.2: Regulate to component voltages
│   └── F5.3: Battery management (portable config)
│
├── F6: PROTECT - Environmental Survival
│   ├── F6.1: Ballistic protection for BSU
│   ├── F6.2: Weather sealing (IP67 estimated)
│   ├── F6.3: Wide temperature operation (-25°C to +70°C)
│   └── F6.4: Sun protection (VDU-1 hood)
│
├── F7: DIAGNOSE - Self-Test
│   ├── F7.1: Built-In Test (BIT) at BSU level
│   ├── F7.2: Report firmware version, supply voltage, comm status
│   └── F7.3: Error messaging and hit count tracking
│
└── F8: INTEGRATE - AVTI Interface (Optional)
    ├── F8.1: Accept WDU/WRDU laser detection data
    ├── F8.2: Apply pixel vulnerability model
    ├── F8.3: Merge live fire + laser scoring
    └── F8.4: Report via GNSS-tagged AVC
```

---

## 12. SIGNAL PROCESSING CHAIN (Estimated)

```
                    SAAB LOMAH SIGNAL PROCESSING CHAIN
                    ═══════════════════════════════════

PHYSICAL         TRANSDUCTION       CONDITIONING        DIGITAL
─────────        ────────────       ────────────        ───────
Shockwave ──→ Pressure ──→ Bandpass ──→ High-Speed ──→ TDOA
 (Mach cone)  Transducer    Filter      ADC            Engine
              ×4 or ×9     (AGC)       (≥500 kHz     (MCU/FPGA)
                                       sample rate)        │
                                                          ▼
                                                    Calibration-Free
                                                    (X,Y) Calculator
                                                          │
                                                          ▼
                                                    Hit/Miss
                                                    Classifier
                                                          │
                                                    ┌─────┴──────┐
                                                    ▼            ▼
                                               Radio Link    Storage
                                               to VDU/ROPU   (TPU-2)
```

### Estimated Component Architecture

| Stage | Component | Specification (Estimated) |
|-------|-----------|--------------------------|
| **Transducer** | Pressure microphone | High-SPL rated, >140 dB SPL tolerance |
| **Pre-amp** | Low-noise amp | Fast response, ~1 μs rise time |
| **Filter** | Bandpass | 1-100 kHz (shockwave spectrum) |
| **AGC** | Automatic Gain Control | Dynamic range management |
| **ADC** | High-speed converter | ≥500 kHz, 12-16 bit resolution |
| **Processor** | MCU or FPGA | TDOA computation, calibration-free algorithm |
| **Communication** | Radio transceiver | VHF, real-time data link |
| **Power** | DC-DC converter | From 12V battery/110-230V mains |

---

## 13. PATENTS & INTELLECTUAL PROPERTY

### 13.1 Core Acoustic Scoring Patents

| Patent | Title | Inventor | Year | Key Innovation |
|--------|-------|----------|------|----------------|
| **WO1991010876A1** | Acoustic projectile trajectory evaluation device | Lasse Karlsen | 1991 | 4 transducers, calibration-free, time-only measurement |
| **US5258962** | US equivalent of above | Lasse Karlsen | 1993 | Assignee: Techsonic Aerosystems AB |
| **EP0890075B1** | Method and device for projectile measurements | Appelgren, Kroling | 1997 | Extends to subsonic; 3 transducers/plane; 30-50 kHz ultrasonic |
| **US5920522A** | Acoustic hit indicator | Nadav Levanon | 1999 | 5+ sensors; iterative least-squares estimation |
| **RE32123** | Discriminatory hit detection in target apparatus | — | Reissue | Lomah Electronic Targetry Inc. |

### 13.2 Key Patent Details (WO1991010876A1)

This is the **foundational patent** for calibration-free acoustic scoring:

| Parameter | Detail |
|-----------|--------|
| **Transducers** | T1-T4, "not located in the same geometrical plane" |
| **Spacing** | 10-50 cm typical (plane wave approximation) |
| **Key claim** | "Time measurements only are required" |
| **No calibration** | No velocity of sound or projectile speed needed |
| **Status** | Ceased (expired -- free to practice) |

### 13.3 Saab-Assigned Patents

| Patent | Subject |
|--------|---------|
| US6887079 | Firing simulator alignment (Saab Training Systems AB) |
| Various | Laser scoring: "relationship of projectile to angular beam position" |
| Various | Piezoelectric sensor arrangement for projectile impact detection |

**Note**: The foundational calibration-free patent (WO1991010876A1 / US5258962) has **CEASED** status, meaning the technology is now in the public domain and free to practice without licensing.

---

## 14. KNOWN CONTRACTS & CUSTOMERS

### 14.1 Confirmed Contracts

| Country | Details | Value | Year |
|---------|---------|-------|------|
| **Norway** | Framework: fixed/portable lifters, MIT/MAT, control systems, LOMAH sensors; Rena CTC | SEK 141M (first order) + SEK 190M support | 2019-2027 |
| **Austria** | Infantry Target Systems (LOMAH), vehicle simulators, soldier kits | Not disclosed | End 2023 |
| **Sweden** | Framework with FMV for training & simulation including live fire | SEK 340M (~$32.2M) | 2022 |
| **Belgium** | GAMER mobile CTC with TESS, BT47, BT46 Mk III | SEK 160M (~$17M) | 2019 |
| **United Kingdom** | ILT-D Instrumented Live Training; deployed in FI/SE/EE/KE/OM/JO/CY/DE | GBP 60M (3-year, options to 2030) | 2024 |
| **USA (USMC)** | FoFTS-Next, MCTIS equipment, up to 10 battalion sets | Not disclosed | 2021-2026 |
| **Finland** | Combat Training Simulators, GCIDT at 21 locations (~20,000 conscripts/year) | Not disclosed | 2022 |
| **Poland** | Live training for mechanized battalion + 4 company centres; BT46 upgrade | Not disclosed | 2021-2026 |
| **Netherlands** | Combat Training Solutions, Royal Netherlands Army | Not disclosed | 2021 |
| **Estonia** | BT46 for CV9035, Carl-Gustaf, infantry simulators, Manpack 300 | Not disclosed | 2017 |
| **Germany** | GUZ Combat Training Centre (Saab-operated); BT46 for PAH-1A1 | Multiple contracts | 2000-ongoing |
| **Spain** | Individual Duel Simulation, infantry soldier systems, EXCON | Not disclosed | 2025 |
| **Kenya** | Army Combat Training Centre School of Infantry, Isiolo | Not disclosed | Recent |
| **Lithuania** | Pabrade Training Area, mobile lifters with LOMAH (joint LT-DE-NSPA) | Not disclosed | Recent |

### 14.2 Aggregate Customer Base

| Metric | Value |
|--------|-------|
| **Live fire targets delivered** | 30,000+ |
| **Countries (live fire)** | 25 |
| **Countries (acoustic scoring)** | 30+ (since 1956) |
| **BT46 delivered to** | 20+ countries |
| **Products sold to** | 100+ countries (all Saab) |
| **Operations in** | 30+ countries |

---

## 15. BOM ESTIMATE (Vietnamese Production)

### 15.1 Per-Lane Cost Estimate (SASS-4 Configuration)

| Subsystem | Components | Est. Cost (USD) | Local Content |
|-----------|-----------|-----------------|---------------|
| **BSU-4 Sensor Unit** | 4× pressure transducers, housing, mounting, cables | $45-75 | 40% (housing local, sensors import) |
| **Signal conditioning** | Pre-amps, bandpass filters, AGC circuits | $25-40 | 50% (PCB local, ICs import) |
| **ADC + Processing** | High-speed ADC, MCU/FPGA, firmware | $35-60 | 30% (PCB local, chips import) |
| **TPU-2 enclosure** | IP67 housing, connectors, power regulation | $25-40 | 70% (machined locally) |
| **Radio communication** | VHF transceiver, antenna | $20-35 | 30% (module import) |
| **VDU-1 Display** | Color monitor, sun hood, housing | $40-65 | 45% (enclosure local, display import) |
| **Power system** | 12V battery, DC-DC converters, mains adapter | $20-35 | 55% (battery local, converters import) |
| **Cables & connectors** | Inter-unit cables, mil-spec connectors | $15-25 | 60% (cables local, connectors import) |
| **Target lifter (SIT)** | Mechanism, actuator, frame, silhouette | $60-100 | 75% (structural local) |
| **Assembly & test** | Integration, calibration, QC | $20-35 | 90% (local labor) |
| **TOTAL per lane** | | **$305-510** | **~52-60%** |

### 15.2 Software & Infrastructure (Per Range)

| Item | Est. Cost (USD) | Notes |
|------|-----------------|-------|
| **Exercise management software** | $15,000-25,000 | EXCON equivalent; custom development |
| **ROPU hardware** | $2,000-4,000 | Server + monitors |
| **DAN communication infrastructure** | $5,000-10,000 | VHF backbone |
| **Installation & commissioning** | $8,000-15,000 | Per range |

### 15.3 Local Content Analysis

| Category | Import % | Local % | Vietnamese Advantage |
|----------|----------|---------|---------------------|
| **Pressure transducers** | 90% | 10% | Must import (specialized acoustic) |
| **Electronics (ICs, ADC, FPGA)** | 85% | 15% | China/Taiwan supply chain |
| **PCB fabrication** | 30% | 70% | Growing domestic PCB industry |
| **Mechanical housing** | 20% | 80% | Strong local machining capability |
| **Target lifter structure** | 15% | 85% | Steel from Hòa Phát / Nam Kim |
| **Cables & wiring** | 30% | 70% | Local cable manufacturing |
| **Battery systems** | 40% | 60% | Li-ion assembly local, cells import |
| **Rubber components** | 5% | 95% | Vietnam = #3 global rubber producer |
| **Software** | 0% | 100% | Domestic development team |
| **Assembly & integration** | 5% | 95% | Local labor |
| **Overall weighted** | **~42%** | **~58%** | Target: ≥60% with optimization |

### 15.4 Cost Comparison vs Import

| Scenario | Per-Lane Cost | Notes |
|----------|--------------|-------|
| **Saab import (estimated)** | $2,500-5,000 | FOB, excludes installation/support |
| **Vietnamese production** | $305-510 | Per-lane hardware only |
| **Vietnamese full range (10 lanes)** | $28,050-55,100 | Hardware + software + infrastructure |
| **Cost ratio** | **~12-20%** | Significant cost advantage |

---

## 16. COMPETITIVE COMPARISON

### 16.1 Saab vs Other LOMAH Manufacturers

| Feature | Saab SASS | InVeris | Polytronic | TTS | Zen |
|---------|-----------|---------|------------|-----|-----|
| **Accuracy** | ±10mm | <5mm | ±5mm | ±10mm | ±5mm (est.) |
| **Calibration** | **Free** | Required | Required | **Free** | Required |
| **Min velocity** | Mach 1.3 | Supersonic | 350 m/s | Mach 1.3 | Supersonic |
| **Subsonic** | No (acoustic only) | No | **Yes (radar I-Bar)** | **Yes (Box Target)** | No |
| **AVTI/Vuln model** | **Yes (pixel-based)** | No | No | No | No |
| **Laser integration** | **Yes (GAMER TESS)** | No | No | No | No |
| **Installed base** | 30,000+ targets | 80,000+ targets | Not disclosed | Not disclosed | Limited |
| **Countries** | 25+ | Worldwide | 40+ | 15+ | 10+ |
| **Heritage** | 1956 (acoustic) | 1926 (Caswell) | 1966 | ~2000s | ~2010s |

### 16.2 Saab Unique Advantages

1. **Calibration-free scoring** -- No reference shot needed; operational time savings
2. **AVTI pixel vulnerability model** -- Most advanced target realism in industry
3. **Live fire + laser simulation integration** -- Shared WDU detectors bridge LOMAH and GAMER
4. **60+ year acoustic heritage** -- Longest track record in electronic scoring
5. **40+ year operational longevity** -- Extreme durability demonstrated
6. **AI-based AAR** -- Next-generation exercise analysis (announced 2025)
7. **Combat Training Centre expertise** -- Full LVC integration capability

### 16.3 Saab Limitations

1. **No subsonic capability** -- Cannot score 9mm, .45 ACP, etc. (unlike Polytronic I-Bar)
2. **Accuracy** -- ±10mm is adequate but not best-in-class (Polytronic/InVeris achieve ±5mm)
3. **Proprietary DAN network** -- Lock-in risk for communication infrastructure
4. **Higher system complexity** -- AVTI adds cost and integration effort
5. **Nordic pricing** -- Swedish manufacturing cost base is high

---

## 17. DESIGN INSIGHTS FOR VIETNAMESE PRODUCT

### 17.1 Technologies to Adopt from Saab

| Technology | Rationale | Implementation Risk |
|------------|-----------|-------------------|
| **Calibration-free algorithm** | Operational efficiency; patent EXPIRED (free to practice) | LOW -- mathematics published |
| **Pixel vulnerability model** | Most advanced realism; differentiator for VN product | MEDIUM -- software development |
| **Multi-lane ROPU architecture** | Scalable range management | LOW -- standard networking |
| **Built-In Test (BIT)** | Reduces maintenance burden; critical for VN context | LOW -- firmware feature |
| **12VDC field power** | Simple, reliable, battery-compatible | LOW -- standard design |

### 17.2 Key Lessons from Saab

1. **Calibration-free is achievable with 4 transducers** -- The expired patent WO1991010876A1 provides the mathematical framework. Vietnamese team should study and implement this algorithm.

2. **Time-only measurement eliminates temperature calibration** -- Major advantage in tropical Vietnamese climate where temperature varies 15-40°C daily.

3. **AVTI-style vulnerability model is software, not hardware** -- Can be developed domestically at low cost but high differentiation value.

4. **60-year durability proves robust mechanical design** -- Vietnamese product should prioritize mechanical simplicity and corrosion resistance (tropical environment is harsher than Scandinavia).

5. **Laser + live fire integration is the future** -- Design Vietnamese system architecture to accommodate both from the start.

### 17.3 Vietnamese Product Concept (Cumulative from All RE Analyses)

```
VN-LOMAH Product Architecture (Phase 1 - Supersonic Acoustic)
│
├── Sensing: Calibration-free TDOA (4 transducers, Saab-inspired)
│   • Patent WO1991010876A1 expired -- free to practice
│   • Time-only measurement (no temp sensor needed)
│   • ±10mm accuracy target (matching Saab baseline)
│
├── Processing: FPGA + ARM MCU (hybrid, InVeris/Polytronic-inspired)
│   • FPGA for high-speed TDOA capture (≥500 kHz)
│   • ARM MCU for scoring calculation + communication
│   • BIT self-diagnostics (Saab-inspired)
│
├── Communication: Multi-mode (InVeris-inspired)
│   • Ethernet (FASIT-compatible) -- primary
│   • WiFi 802.11n -- portable config
│   • VHF radio -- extended range fallback
│
├── Display: Web-based (TrueZero-inspired)
│   • HTML5 dashboard -- any device
│   • Pixel vulnerability model (Saab AVTI-inspired)
│   • Real-time X/Y display with statistics
│
├── Target Lifter: Local steel fabrication
│   • SIT: pop-up infantry, 75%+ local content
│   • Turning target: friend-or-foe capability
│   • Vietnamese natural rubber dampers (#3 global producer)
│
├── Power: 12VDC + Solar (tropical optimized)
│   • Li-ion battery (10h runtime target)
│   • Solar charging option for remote ranges
│   • 110/230VAC mains adapter
│
├── Environmental: Tropical hardened
│   • IP67 minimum (Vietnamese humidity/monsoon)
│   • -10°C to +60°C operating range
│   • Conformal-coated PCBs
│   • Marine-grade connectors
│
└── Software: Indigenous development
    • Exercise management (EXCON-inspired)
    • AAR with playback
    • Vietnamese language UI
    • TCVN + MIL-STD compliance reporting
```

### 17.4 Phased Development Approach

| Phase | Scope | Timeline (est.) | Key Risk |
|-------|-------|-----------------|----------|
| **Phase 1** | Supersonic LOMAH (calibration-free, 4 transducers) | 12-18 months | Algorithm validation |
| **Phase 2** | Box Target / chambered LOMAH (TTS-inspired, subsonic) | 6-12 months add-on | Rubber membrane sourcing (local advantage) |
| **Phase 3** | AVTI-style vulnerability model (software) | 6-9 months parallel | UI/UX development |
| **Phase 4** | Radar subsonic LOMAH (Polytronic-inspired) | 18-24 months | Radar engineering expertise |
| **Phase 5** | Full CTC integration (laser + live fire) | 24-36 months | System-of-systems complexity |

---

## 18. INTELLIGENCE GAPS

The following information was **NOT found** in public sources:

| Gap | Impact | Workaround |
|-----|--------|-----------|
| Exact BSU-4/9 dimensions & weight | Mechanical design | Estimate from similar systems (~10-15 kg) |
| Confirmed IP rating | Environmental specification | Assume IP67 (military standard) |
| SASS-4 vs SASS-9 detailed algorithm differences | System architecture | Study expired patents for 4-transducer algorithm |
| DAN network protocol specifications | Communication design | Use standard VHF + Ethernet instead |
| Radio link frequency/protocol (TPU↔VDU) | Communication design | Design with configurable VHF/UHF |
| Firmware/software architecture of TPU-2 | Embedded design | Independent development from patents |
| PCB component identification | Electronics design | Standard MEMS mic + FPGA + ARM approach |
| Exact pricing per component | Business case | Use BOM estimate range |
| Air Target Sweden ↔ Saab T&S relationship | Supply chain | Treat as supplier/subsidiary |
| Signal conditioning chain details | Analog design | Standard acoustic processing chain |

---

## 19. REFERENCES

### Public Sources Used

| # | Source | Type | Key Data |
|---|--------|------|----------|
| 1 | saab.com/products/live-fire-training | Product page | System overview, capabilities |
| 2 | defence-industries.com | Product listing | SASS-4/9 specs, Air Target Sweden |
| 3 | airtarget.com | Corporate site | Company history, acoustic scoring heritage |
| 4 | Janes Defence News (IT2EC 2025) | News article | AVTI details, pixel vulnerability model |
| 5 | FCC ID R4AWDU24A | Regulatory filing | WDU24A specs, WTS system components |
| 6 | Google Patents WO1991010876A1 | Patent | Calibration-free algorithm, 4 transducers |
| 7 | Google Patents EP0890075B1 | Patent | Subsonic extension, ultrasonic sensing |
| 8 | EDR Magazine | Industry press | Employee count, contract details |
| 9 | Breaking Defense | News | AI-based AAR announcement (Dec 2025) |
| 10 | livefiringshow.com | Trade show | Saab exhibit details, target demos |
| 11 | army-technology.com | Defense portal | Contract announcements |
| 12 | SOFF (Swedish Security & Defence Industry) | Association | Member listing, company data |
| 13 | theissentraining.com | Competitor | TTS LOMAH specs (Saab-compatible technology) |

### Patent References

| Patent | Status | Relevance |
|--------|--------|-----------|
| WO1991010876A1 / US5258962 | **CEASED (expired)** | Foundational calibration-free 4-transducer scoring |
| EP0890075B1 | Active | Subsonic extension using aeroacoustic wake |
| US5920522A | Expired | 5+ sensor iterative least-squares approach |
| RE32123 | Expired | Early LOMAH discriminatory hit detection |
| US6887079 | Active | Saab firing simulator alignment |

---

*Analysis compiled from publicly available sources only. No classified, ITAR-controlled, or proprietary information included. All specifications are estimates based on published data, patent disclosures, trade show information, and industry comparisons.*

*Created: 2026-02-06 | Project: VN-LOMAH | Phase: 0 (Reverse Engineering)*
