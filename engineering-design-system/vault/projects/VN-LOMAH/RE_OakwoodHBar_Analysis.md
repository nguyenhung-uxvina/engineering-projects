---
project: VN-LOMAN
type: reverse_engineering
version: 1.0
created: 2026-02-06
status: active
methodology: Reverse Engineering (4-Phase D-M-I-R)
foreign_system: H-Bar LOMAH
manufacturer: Oakwood Controls Corp
country: USA (UK distribution)
---

# REVERSE ENGINEERING ANALYSIS
## Oakwood Controls H-Bar LOMAH (USA/UK)
## Phan tich Ky thuat Dao nguoc - He thong Bia dien tu LOMAH

---

# SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| **Foreign Designation** | H-Bar LOMAH Electronic Target System |
| **Manufacturer** | Oakwood Controls Corp |
| **Headquarters** | Glen Rock, Pennsylvania, USA |
| **UK Distributor** | Militec Ltd (Mountain Ash, Wales) |
| **Founded** | 2009 |
| **Technology** | Acoustic LOMAH (Location Of Miss And Hit) |
| **Market Segment** | Military SOF, Law enforcement, Sport shooting |
| **Price Range** | Not publicly disclosed (military/institutional sales) |
| **Analysis Date** | 2026-02-06 |
| **Analysis Type** | Open Source (web, publications, spec sheets) |

---

# PART 1: PHASE 1 - DIAGNOSIS (RECONNAISSANCE)

## 1.1 System Overview

```
+===============================================================================+
|                       H-BAR LOMAH SYSTEM CONCEPT                               |
+===============================================================================+
|                                                                                |
|  SHOOTER                              TARGET                      DISPLAY     |
|  --------                             ------                      -------     |
|                                                                                |
|   +---+                          +------------------+           +---------+   |
|   |   |                          |                  |           |         |   |
|   | O |        Supersonic        |  +------------+  |  Radio    | TOUGH-  |   |
|   |/|\|  --------bullet--------> |  |   TARGET   |  |<--------> |  BOOK   |   |
|   | | |     shock wave           |  |    FACE    |  |  (5 km)   | TABLET  |   |
|   |/ \|                          |  +------------+  |           |         |   |
|   +---+                          |                  |           +---------+   |
|                                  |  o  o  o  o  o o | <- 6 Acoustic sensors   |
|   Range: up to 3,500 yards       |  (6 microphones) |                         |
|                                  +------------------+                         |
|                                          |                                    |
|                                          | Processing                         |
|                                          v                                    |
|                                  +------------------+                         |
|                                  |   ELECTRONICS    |                         |
|                                  | * Time capture   |                         |
|                                  | * TDOA calc      |                         |
|                                  | * Long-range RF  |                         |
|                                  | * Battery power  |                         |
|                                  +------------------+                         |
|                                                                                |
|  WEIGHT: <15 lbs    SETUP: <10 min    ACCURACY: +/-5mm    RANGE: 5 km radio  |
+===============================================================================+
```

## 1.2 Technical Specifications (Documented)

### 1.2.1 Detection System

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| **Sensor Type** | Acoustic sensors | 6 sensors per unit |
| **Detection Principle** | Acoustic supersonic shock wave | Time-of-arrival triangulation |
| **Accuracy** | +/- 5mm | Throughout entire scoring area |
| **Min Bullet Velocity** | 1,200 fps (365 m/s, Mach 1.07) | Lower threshold than TrueZero |
| **Caliber Range** | Wide (5.56mm to .50 BMG) | Military calibers focus |
| **Detection Window** | Large (size not specified) | Hits AND misses |
| **Firing Angle** | Up to 15 degrees from center | Or 90 degrees perpendicular |
| **Shot Detection** | Hits and misses | Beyond target window |
| **Temperature Sensors** | Integrated | For acoustic compensation |

### 1.2.2 Physical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Total Weight** | <15 lbs (<7 kg) | Full portable system |
| **Setup Time** | <10 minutes | Field deployment |
| **Target Frame** | Modular aluminum | Precision Box variant |
| **IP Rating** | Not specified | Ruggedized design |
| **Operating Temp** | Not specified | Field-proven outdoors |
| **Portability** | Fully portable | Designed for tactical use |

### 1.2.3 Power System

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Power Source** | Rechargeable batteries | Primary mode |
| **Alternative** | 12V DC cabling | Fixed installation |
| **Battery Life** | Not specified | Full day operation implied |
| **Charging** | Standard charger | Details not specified |

### 1.2.4 Communication

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Primary Link** | Long-range data radio | Proprietary protocol likely |
| **Communication Range** | Up to 5 km (3.1 miles) | Exceptional range |
| **Tested Range** | 3,500 yards (3.2 km) | Practical shooting limit |
| **Secondary** | Wi-Fi | Short-range option |
| **Encryption** | Not specified | Military-grade likely |

### 1.2.5 Software & Display

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Display Device** | Toughbook tablet | Ruggedized, touchscreen |
| **OS Platform** | Windows | Laptop or tablet |
| **Sunlight Readable** | Yes | Confirmed in field tests |
| **Response Time** | Split-second | Real-time feedback |
| **Measurement Units** | Inches, cm, MOA, MIL | Multiple formats |
| **Features** | Group size, center, shot-by-shot notes | Comprehensive analysis |
| **Data Storage** | Session storage | Multi-shooter comparison |

## 1.3 Product Variants

| Model | Application | Key Features | Target Market |
|-------|-------------|--------------|---------------|
| **H-Bar Standard** | Stationary targets | 15-degree impact angle | Military, competition |
| **H-Bar Hunting** | Long-range hunting | Realistic animal imagery | Hunters, enthusiasts |
| **Precision Box** | Fixed ranges | Modular aluminum frame, subsonic capable | Military ranges |
| **R&D System** | Ballistic testing | Ballistic coefficient measurement | Government labs |

## 1.4 Military & Government Customers

| Customer | Application | Date | Notes |
|----------|-------------|------|-------|
| **Naval Special Warfare Group Four** | SOF precision training | Contracted | Large system procurement |
| **US Army NVESD** | R&D (CACI $2.8M subcontract) | Active | Night vision/sensors |
| **USMC** | Machine gun accuracy validation | Jan 2021 | Refurbished weapons |
| **US Army** | Ammunition/weapons testing | May 2021 | Ballistic research |
| **US Special Operations** | Assault/sniper training | Jun 2022 | 12-month installation |
| **UK MoD** | Soldier/weapon performance | Apr 2022 | H-Bar testing |
| **French Special Forces** | Target systems | Mar 2021 | SOF training |

## 1.5 Competitive Position vs TrueZeroTarget

| Parameter | H-Bar (Oakwood) | TrueZeroTarget (Steinert) | VN-LOMAN Target |
|-----------|-----------------|---------------------------|-----------------|
| **Country** | USA | Norway | Vietnam |
| **Accuracy** | +/-5mm | +/-3mm (center) | +/-5mm |
| **Min Velocity** | 365 m/s (Mach 1.07) | 440 m/s (Mach 1.3) | 400 m/s |
| **Comm Range** | 5 km (radio) | 300m (Wi-Fi) | Target: 1 km |
| **Weight** | <7 kg (system) | 4 kg (unit only) | Target: <5 kg |
| **Sensors** | 6 | 4+ | 4-6 |
| **Display** | Windows Toughbook | Win/Android/iOS | Android focus |
| **Price** | Institutional (higher) | EUR 3,490 | $1,500-2,000 |
| **Focus** | Military SOF | Consumer/hunting | Military training |

---

# PART 2: PHASE 2 - MODELING (FUNCTIONAL RECONSTRUCTION)

## 2.1 Overall Function Statement

> **Detect and locate supersonic projectile impacts on/near a target at extended ranges and transmit precise position data via long-range radio to ruggedized field displays.**

Vietnamese: *Phat hien va dinh vi vi tri dan sieu am trung/gan bia o khoang cach xa va truyen du lieu vi tri chinh xac qua song radio tam xa den man hinh thuc dia.*

## 2.2 Function Structure Diagram

```
FUNCTION STRUCTURE: OAKWOOD H-BAR LOMAH
===============================================================================

OVERALL FUNCTION: Detect and locate supersonic projectile impacts
                  and display position via long-range radio

F1: DETECT PROJECTILE PASSAGE
+-- F1.1: Generate acoustic signature ------------ Bullet shock wave (external)
+-- F1.2: Capture shock wave --------------------- 6x Acoustic sensors
+-- F1.3: Convert acoustic to electrical --------- Piezoelectric/MEMS elements
+-- F1.4: Timestamp arrival at each sensor ------- High-speed sampling
+-- F1.5: Detect temperature (compensation) ------ Temperature sensor
+-- F1.6: Amplify and filter signals ------------- Analog front-end

F2: CALCULATE IMPACT POSITION
+-- F2.1: Measure time differences --------------- TDOA algorithm
+-- F2.2: Apply temperature correction ----------- Speed of sound adjustment
+-- F2.3: Triangulate position ------------------- 6-sensor geometry
+-- F2.4: Classify hit vs miss ------------------- Boundary detection
+-- F2.5: Calculate group statistics ------------- Running calculations
+-- F2.6: Format measurement units --------------- MOA, MIL, inches, cm

F3: COMMUNICATE RESULTS (Long-Range)
+-- F3.1: Encode data packet --------------------- Protocol formatting
+-- F3.2: Modulate RF signal --------------------- Long-range radio
+-- F3.3: Transmit data -------------------------- 5 km range capability
+-- F3.4: Handle acknowledgment ------------------ Two-way comm
+-- F3.5: Manage link (Wi-Fi fallback) ----------- Dual-mode option

F4: DISPLAY RESULTS (Toughbook)
+-- F4.1: Receive RF data ------------------------ Radio receiver
+-- F4.2: Decode position ------------------------ Protocol parsing
+-- F4.3: Render target image -------------------- Graphics overlay
+-- F4.4: Plot impact location ------------------- Coordinate mapping
+-- F4.5: Calculate statistics ------------------- Group size, center
+-- F4.6: Store shot history --------------------- Session management
+-- F4.7: Support multi-shooter ------------------ Data separation
+-- F4.8: Enable annotations --------------------- Shot-by-shot notes

F_AUX: SUPPORT FUNCTIONS
+-- F_AUX.1: Store electrical energy ------------- Rechargeable battery
+-- F_AUX.2: Accept 12V DC input ----------------- Fixed installation
+-- F_AUX.3: Regulate voltage -------------------- DC-DC converters
+-- F_AUX.4: Protect electronics ----------------- Ruggedized enclosure
+-- F_AUX.5: Mount target face ------------------- Aluminum frame
+-- F_AUX.6: Support/position system ------------- Tripod/stand

===============================================================================
TOTAL: 4 Main Functions + 1 Auxiliary = 5 Function Groups, 32 Subfunctions
===============================================================================
```

## 2.3 Working Principle Analysis

### 2.3.1 6-Sensor TDOA Array (Enhanced Accuracy)

```
6-SENSOR ARRAY CONFIGURATION (Estimated)
===============================================================================

TOP VIEW - H-Bar Sensor Arrangement:
-------------------------------------------------------------------------------

                              Bullet path
                                  |
                          - - - -+- - - - - - ->
                                  \
                                   \ Shock wave cone
                                    \
        S1 o-----------o S2-----------o S3
           |                           |
           |       TARGET FACE         |
           |           * Impact        |
           |         (x, y)            |
           |                           |
        S4 o-----------o S5-----------o S6

           <-------- baseline -------->

WHY 6 SENSORS vs 4?
-------------------------------------------------------------------------------
* Redundancy: Can lose 1-2 sensors and still calculate
* Accuracy: Over-determined system reduces error
* Miss detection: Wider coverage for near-misses
* Angle tolerance: Better performance at oblique angles

TDOA EQUATIONS (Overdetermined System):
-------------------------------------------------------------------------------
For N=6 sensors, we have 5 independent time differences:
  dt12 = t2 - t1 --> Hyperbola 1
  dt13 = t3 - t1 --> Hyperbola 2
  dt14 = t4 - t1 --> Hyperbola 3
  dt15 = t5 - t1 --> Hyperbola 4
  dt16 = t6 - t1 --> Hyperbola 5

With 5 hyperbolas and 2 unknowns (x, y), use least-squares fit
for optimal position estimate with error bounds.

===============================================================================
```

### 2.3.2 Long-Range Communication Architecture

```
COMMUNICATION SUBSYSTEM
===============================================================================

TARGET UNIT                                        SHOOTER STATION
+------------------+                              +------------------+
|                  |                              |                  |
| +------------+   |        5 km RANGE            |  +------------+  |
| |   MCU      |   |     (Line of Sight)          |  |  TOUGHBOOK |  |
| +-----+------+   |                              |  |   TABLET   |  |
|       |          |                              |  +-----+------+  |
| +-----v------+   |                              |        |         |
| | LONG-RANGE |   |     Sub-GHz Radio            |  +-----v------+  |
| |   RADIO    |<===============================>|  |   RADIO    |  |
| | (900 MHz?) |   |     (Likely 900 MHz ISM      |  |  RECEIVER  |  |
| +------------+   |      or licensed freq)       |  +------------+  |
|                  |                              |                  |
+------------------+                              +------------------+

PROTOCOL (Estimated):
-------------------------------------------------------------------------------
* Frequency: 900 MHz ISM or 400 MHz (military allocation)
* Modulation: FSK or LoRa (long-range, low power)
* Data rate: Low (position data is small, ~100 bytes/shot)
* Latency: <500 ms round-trip
* Error correction: Forward error correction (FEC)
* Acknowledgment: Two-way for reliability

RANGE ADVANTAGE vs Wi-Fi:
-------------------------------------------------------------------------------
| Parameter        | Wi-Fi (2.4 GHz)  | Long-Range Radio |
|------------------|------------------|------------------|
| Frequency        | 2.4 GHz          | 900 MHz (est.)   |
| Free-space loss  | Higher           | Lower (-6 dB)    |
| Obstacle penetration | Poor         | Good             |
| Typical range    | 100-300m         | 5+ km            |
| Power consumption| Moderate         | Low              |

===============================================================================
```

## 2.4 Subsystem Decomposition

### 2.4.1 Estimated System Architecture

```
H-BAR LOMAH SUBSYSTEM ARCHITECTURE (Estimated)
===============================================================================

+-------------------------------------------------------------------------+
|                              SENSOR HEAD                                 |
|  +-------+  +-------+  +-------+  +-------+  +-------+  +-------+       |
|  | MIC 1 |  | MIC 2 |  | MIC 3 |  | MIC 4 |  | MIC 5 |  | MIC 6 |       |
|  +---+---+  +---+---+  +---+---+  +---+---+  +---+---+  +---+---+       |
|      |          |          |          |          |          |           |
|      +----------+----------+----------+----------+----------+           |
|                            | (Analog signals)                           |
+----------------------------+--------------------------------------------+
                             |
+----------------------------+--------------------------------------------+
|                      ELECTRONICS MODULE                                  |
|                            |                                             |
|  +-------------------------v-------------------------------------------+ |
|  |                  ANALOG FRONT-END                                   | |
|  |  +--------+  +--------+  +--------+  +--------+  +--------+  +----+ | |
|  |  |Preamp 1|  |Preamp 2|  |Preamp 3|  |Preamp 4|  |Preamp 5|  |  6 | | |
|  |  +---+----+  +---+----+  +---+----+  +---+----+  +---+----+  +--+-+ | |
|  |      |           |           |           |           |         |    | |
|  |  +---v----+  +---v----+  +---v----+  +---v----+  +---v----+  +-v--+ | |
|  |  |Filter 1|  |Filter 2|  |Filter 3|  |Filter 4|  |Filter 5|  |  6 | | |
|  |  +---+----+  +---+----+  +---+----+  +---+----+  +---+----+  +-+--+ | |
|  |      +----------+------------+-----------+------------+-------+     | |
|  +-------------------------+-------------------------------------------+ |
|                            |                                             |
|  +-------------------------v-------------------------------------------+ |
|  |                  DIGITAL PROCESSING                                 | |
|  |                         |                                           | |
|  |  +----------------------v----------------------+                    | |
|  |  |        MULTI-CHANNEL ADC                   |   Temp             | |
|  |  |        (6 channels, high-speed)            |<--Sensor           | |
|  |  +----------------------+----------------------+                    | |
|  |                         |                                           | |
|  |  +----------------------v----------------------+                    | |
|  |  |        MAIN PROCESSOR                       |                    | |
|  |  |        (ARM Cortex or DSP)                  |                    | |
|  |  |        * 6-channel timestamp capture        |                    | |
|  |  |        * TDOA calculation (least-squares)   |                    | |
|  |  |        * Temperature compensation           |                    | |
|  |  |        * Hit/miss classification            |                    | |
|  |  +----------------------+----------------------+                    | |
|  |                         |                                           | |
|  +-------------------------+-------------------------------------------+ |
|                            |                                             |
|  +-------------------------v-------------------------------------------+ |
|  |                  COMMUNICATION                                      | |
|  |                         |                                           | |
|  |  +----------------------v----------------------+                    | |
|  |  |        LONG-RANGE RADIO MODULE              |                    | |
|  |  |        * Sub-GHz (900 MHz or 400 MHz)       |                    | |
|  |  |        * 5 km range                         |---------> ANTENNA  | |
|  |  |        * FEC encoding                       |                    | |
|  |  +---------------------------------------------+                    | |
|  |                                                                     | |
|  |  +---------------------------------------------+                    | |
|  |  |        Wi-Fi MODULE (Optional)              |                    | |
|  |  |        * Short-range backup                 |                    | |
|  |  +---------------------------------------------+                    | |
|  |                                                                     | |
|  +---------------------------------------------------------------------+ |
|                                                                          |
|  +---------------------------------------------------------------------+ |
|  |                  POWER SYSTEM                                       | |
|  |                                                                     | |
|  |  +----------+    +----------+    +------------------+               | |
|  |  | 12V DC   |--->| Charger  |--->| Rechargeable     |               | |
|  |  | Input    |    | Circuit  |    | Battery Pack     |               | |
|  |  +----------+    +----------+    +--------+---------+               | |
|  |                                           |                         | |
|  |                                    +------v------+                  | |
|  |                                    | DC-DC       |                  | |
|  |                                    | Converters  |                  | |
|  |                                    | 3.3V, 5V,12V|                  | |
|  |                                    +-------------+                  | |
|  |                                                                     | |
|  +---------------------------------------------------------------------+ |
|                                                                          |
+--------------------------------------------------------------------------+

+--------------------------------------------------------------------------+
|                       ENCLOSURE (Ruggedized)                              |
|  * Weather-resistant housing                                              |
|  * Modular aluminum frame (Precision Box variant)                         |
|  * Field-serviceable design                                               |
|  * Tactical finish                                                        |
+--------------------------------------------------------------------------+

===============================================================================
```

---

# PART 3: DESIGN PARADIGM ANALYSIS

## 3.1 Observed Indicators

| Indicator | Observation | Score (1-5) | Interpretation |
|-----------|-------------|-------------|----------------|
| **Safety margins** | Military-grade ruggedization, field-proven | 5 | SOF-grade reliability |
| **Modularity** | Modular frame, swappable components | 4 | Designed for maintainability |
| **Material selection** | Aluminum frame, Toughbook display | 5 | Premium, tactical-grade |
| **Redundancy** | 6 sensors (overdetermined), dual comm | 5 | High redundancy |
| **Manufacturing** | US production, military supply chain | 4 | Quality over cost |
| **Usability** | <10 min setup, touchscreen | 4 | Optimized for field use |
| **Communication** | 5 km range radio | 5 | Industry-leading range |
| **Accuracy** | +/-5mm (slightly below TrueZero) | 4 | Good, not best-in-class |

**Overall Paradigm Score: 4.5/5** (Military-grade, long-range focus, SOF optimized)

## 3.2 Designer's Paradigm Statement

> "Create a ruggedized, long-range electronic target system optimized for Special Operations Forces and military training environments, prioritizing extended communication range, field reliability, and rapid deployment over consumer accessibility or lowest cost."

## 3.3 Trade-off Analysis

| Trade-off | Choice Made | Alternative Forgone | Rationale |
|-----------|-------------|---------------------|-----------|
| **Range vs. Simplicity** | 5 km radio | Wi-Fi only (simpler) | Military ranges are large |
| **Accuracy vs. Cost** | +/-5mm (good) | +/-3mm (best) | Sufficient for training |
| **6 sensors vs. 4** | 6 (redundant) | 4 (simpler) | Reliability, miss detection |
| **Weight vs. Features** | <15 lbs (heavier) | <10 lbs (lighter) | Full capability prioritized |
| **Toughbook vs. Consumer** | Toughbook (rugged) | iPad/phone (cheaper) | Sunlight, durability |
| **Proprietary vs. Open** | Proprietary protocol | Open standards | Military security |

## 3.4 Strengths and Limitations

### Strengths
1. **Exceptional communication range** - 5 km radio enables use on any military range
2. **SOF-proven** - US Navy SEALs, US Army, USMC, UK MoD, French SF customers
3. **6-sensor redundancy** - Can operate with sensor failures
4. **Miss detection** - Locates shots that miss the target
5. **Rapid deployment** - <10 min setup, <15 lbs total
6. **Ruggedized display** - Toughbook with sunlight readability
7. **Comprehensive software** - MOA, MIL, statistics, multi-shooter
8. **Subsonic capability** - Precision Box variant for all projectiles

### Limitations
1. **Price** - Institutional/military pricing, not consumer accessible
2. **Windows only** - No mobile app for iOS/Android
3. **Accuracy** - +/-5mm is good but not best-in-class (+/-3mm)
4. **Weight** - <15 lbs is heavier than some competitors
5. **Proprietary** - Custom radio protocol limits interoperability
6. **US Export** - ITAR considerations for international sales

---

# PART 4: PHASE 3 - INTERVENTION (APPLICATION STRATEGY)

## 4.1 Key Differentiators vs TrueZeroTarget

| Feature | H-Bar Advantage | TrueZero Advantage | VN-LOMAN Strategy |
|---------|-----------------|--------------------|--------------------|
| **Comm Range** | 5 km radio | 300m Wi-Fi | Target 1 km (balance) |
| **Sensors** | 6 (redundant) | 4+ | 4-6 (configurable) |
| **Accuracy** | +/-5mm | +/-3mm | +/-5mm (acceptable) |
| **Platform** | Windows | Win/Android/iOS | Android focus |
| **Price** | High (military) | EUR 3,490 | $1,500-2,000 |
| **Miss Detection** | Large window | Limited | Important feature |

## 4.2 Technology Adoption for VN-LOMAN

### 4.2.1 Features to Adopt from H-Bar

| Feature | Rationale | Implementation |
|---------|-----------|----------------|
| **Extended radio range** | Vietnamese military ranges can be large | Add LoRa module (1-2 km) |
| **6-sensor option** | Redundancy for critical training | Design for 4-6 sensors |
| **Miss detection** | Valuable training feedback | Larger detection window |
| **Ruggedized display** | Outdoor use in Vietnam conditions | Android tablet with case |
| **Sub-10 min setup** | Rapid deployment requirement | Integrated design |

### 4.2.2 Features NOT to Adopt

| Feature | Reason | VN-LOMAN Approach |
|---------|--------|-------------------|
| **5 km radio** | Overkill for most ranges, adds cost | 1 km LoRa sufficient |
| **Toughbook display** | Too expensive | Ruggedized Android tablet |
| **Windows-only software** | Limited accessibility | Cross-platform (Android+Windows) |
| **Proprietary protocols** | Limits flexibility | Use open standards |
| **US military supply chain** | Not accessible | Local Vietnamese suppliers |

## 4.3 Updated VN-LOMAN Specifications

Based on analysis of BOTH TrueZeroTarget and H-Bar:

| Parameter | TrueZero | H-Bar | VN-LOMAN (Updated) |
|-----------|----------|-------|---------------------|
| **Accuracy** | +/-3mm | +/-5mm | +/-5mm (target) |
| **Min velocity** | 440 m/s | 365 m/s | 380 m/s (improved) |
| **Sensors** | 4+ | 6 | 4 standard, 6 optional |
| **Comm range** | 300m Wi-Fi | 5 km radio | 1 km LoRa + Wi-Fi |
| **Display** | Multi-platform | Windows | Android primary |
| **Weight** | 4 kg | 7 kg | <5 kg target |
| **Setup time** | <10 min | <10 min | <10 min |
| **Price** | EUR 3,490 | Military | $1,500-2,000 |
| **Local content** | 0% | 0% | 70%+ |

## 4.4 Communication Module Options

```
VN-LOMAN COMMUNICATION OPTIONS
===============================================================================

OPTION A: Wi-Fi Only (Like TrueZeroTarget)
+-----------------------------------------------------------------------+
| ESP32-S3 with integrated Wi-Fi                                         |
| Range: 200-300m (line of sight)                                        |
| Cost: $8 (module)                                                      |
| Pros: Simple, low cost, standard                                       |
| Cons: Limited range for large military ranges                          |
+-----------------------------------------------------------------------+

OPTION B: LoRa + Wi-Fi (Recommended for VN-LOMAN)
+-----------------------------------------------------------------------+
| ESP32-S3 + SX1276/SX1262 LoRa module                                   |
| Range: 1-2 km LoRa (outdoor), 200m Wi-Fi (indoor)                      |
| Cost: $15 (ESP32 + LoRa)                                               |
| Pros: Good range, low power, Vietnamese 915 MHz legal                  |
| Cons: Slightly more complex                                            |
+-----------------------------------------------------------------------+

OPTION C: Sub-GHz Radio (Like H-Bar)
+-----------------------------------------------------------------------+
| Custom radio module (400 MHz or 900 MHz)                               |
| Range: 3-5 km                                                          |
| Cost: $50+ (custom design)                                             |
| Pros: Maximum range                                                    |
| Cons: Higher cost, regulatory complexity, overkill                     |
+-----------------------------------------------------------------------+

RECOMMENDATION: OPTION B (LoRa + Wi-Fi)
* 1 km range sufficient for most Vietnamese military ranges
* $15 vs $50+ savings per unit
* Standard protocol (LoRaWAN compatible)
* Low power consumption
* Legal in Vietnam (915 MHz ISM band)

===============================================================================
```

---

# PART 5: PHASE 4 - REFLECTION

## 5.1 Key Insights from H-Bar Analysis

1. **Long-range communication is a key differentiator** - H-Bar's 5 km radio enables use on any range. VN-LOMAN should offer LoRa option for 1-2 km range.

2. **6 sensors provide redundancy** - Overdetermined system improves reliability and enables miss detection. Consider 6-sensor variant for VN-LOMAN.

3. **Military customers value ruggedness over cost** - H-Bar optimizes for SOF use. VN-LOMAN can target cost-conscious military buyers.

4. **Windows-only is a limitation** - Android/iOS support provides broader accessibility. VN-LOMAN should prioritize mobile platforms.

5. **+/-5mm accuracy is acceptable** - Both H-Bar and military standards accept +/-5mm. VN-LOMAN doesn't need to match TrueZero's +/-3mm.

6. **Setup time matters** - <10 minutes is the benchmark for portable systems.

## 5.2 Comparative Summary

```
LOMAH SYSTEM COMPARISON
===============================================================================

                    | TrueZero    | H-Bar       | VN-LOMAN (Target)
--------------------|-------------|-------------|-------------------
ORIGIN              | Norway      | USA         | Vietnam
MARKET              | Consumer    | Military    | Military/Training
ACCURACY            | +/-3mm      | +/-5mm      | +/-5mm
MIN VELOCITY        | 440 m/s     | 365 m/s     | 380 m/s
SENSORS             | 4+          | 6           | 4-6
COMM RANGE          | 300m        | 5 km        | 1 km
COMM TYPE           | Wi-Fi       | Radio       | LoRa + Wi-Fi
DISPLAY             | Multi       | Windows     | Android
WEIGHT              | 4 kg        | 7 kg        | <5 kg
SETUP               | <10 min     | <10 min     | <10 min
PRICE               | EUR 3,490   | High        | $1,500-2,000
LOCAL CONTENT       | 0%          | 0%          | 70%+

===============================================================================
```

## 5.3 Updated VN-LOMAN BOM Estimate

| Subsystem | Key Components | Est. Cost ($) | Notes |
|-----------|----------------|---------------|-------|
| Sensors | 4x MEMS mics (expandable to 6) | $20-30 | ICS-43434 or similar |
| Analog | 4-6 channel preamp/filter | $20 | Op-amp based |
| ADC | ADS131M04 or ADS131M08 | $25-40 | 4 or 8 channel |
| MCU | ESP32-S3-WROOM-1 | $8 | Wi-Fi integrated |
| LoRa | SX1262 module | $7 | 1-2 km range |
| Power | LiFePO4 10Ah + BMS | $80 | Full day operation |
| Enclosure | Aluminum + gaskets (IP65) | $100 | Local fabrication |
| PCB | Custom 4-layer | $30 | Local production |
| Mechanical | Frame, mounts | $50 | Local fabrication |
| Assembly | Labor, test, QC | $50 | Local |
| **TOTAL** | | **$390-415** | ~65% local |

**Selling Price:** $1,500-2,000 -> **Gross Margin: 60-74%**

## 5.4 Lessons Learned

| Aspect | Lesson | Application |
|--------|--------|-------------|
| **Market segmentation** | Consumer vs military are different markets | VN-LOMAN targets military training |
| **Communication** | Range is critical for military ranges | Include LoRa option |
| **Redundancy** | 6 sensors valuable for reliability | Design for expandability |
| **Platform** | Windows-only limits adoption | Prioritize Android |
| **Accuracy** | +/-5mm acceptable for training | Don't over-engineer |
| **Ruggedness** | Military needs field-proof design | IP65 minimum |

---

# APPENDIX A: SOURCES

## Web Sources
- [Oakwood Controls - Portable Electronic Target System](https://www.oakwoodcontrols.com/electronic-target-systems/portable-electronic-target-system/)
- [Oakwood Controls - Military Applications](https://www.oakwoodcontrols.com/electronic-target-systems/military-and-law-enforcement-applications/)
- [Oakwood Controls - Company News](https://www.oakwoodcontrols.com/about/company-news/)
- [Oakwood Controls - About](https://www.oakwoodcontrols.com/about/)
- [Small Arms Review - H-Bar LOMAH](https://smallarmsreview.com/oakwood-controls-h-bar-lomah-electronic-target-system/)
- [SSUSA - H-Bar LOMAH Review](https://www.ssusa.org/articles/2015/8/25/oakwood-controls-h-bar-lomah-electronic-target-system/)
- [Militec UK - Oakwood Distributor](https://www.militec.co.uk/oakwood.html)
- [ThinkingAfield - Oakwood Systems](https://thinkingafield.org/2016/02/oakwood-controls-electronic-target-systems.html)

## Related Documents
- [[RE_TrueZeroTarget_Analysis|TrueZeroTarget RE Analysis]]
- [[VN-LOMAN_Product_Spec|VN-LOMAN Product Specification]] (To Be Created)

---

# APPENDIX B: COMPANY PROFILE

## Oakwood Controls Corp

| Field | Value |
|-------|-------|
| **Founded** | 2009 |
| **Headquarters** | Glen Rock, Pennsylvania, USA |
| **Address** | 159 Industrial Road, Glen Rock, PA |
| **Specialization** | Electronic target systems, sensor integration |
| **Key Customers** | US Navy SEALs, US Army, USMC, UK MoD, French SF |
| **UK Distributor** | Militec Ltd |
| **Trade Shows** | SHOT Show, I/ITSEC, SOFIC, EUSOSS |

## Key Contracts
- Naval Special Warfare Group Four - Large portable target system
- CACI International - $2.8M subcontract for NVESD support
- UK MoD - H-Bar testing (2022)
- French Special Forces - Target systems (2021)

---

# REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| **1.0** | **2026-02-06** | **Initial RE analysis. Oakwood H-Bar LOMAH (USA/UK) fully documented. 6-sensor architecture, 5km radio range. Military SOF customer base confirmed. VN-LOMAN specs updated with LoRa communication option.** |

---

*This reverse engineering analysis follows the 4-Phase D-M-I-R methodology for systematic extraction of design knowledge from foreign military/commercial systems.*

**Analysis Status:** COMPLETE
