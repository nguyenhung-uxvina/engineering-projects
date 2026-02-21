---
project: VN-TRN-001
phase: 3
type: embodiment-design
step: PRAD-A
title: Architecture Definition
version: 1.0
created: 2026-02-06
status: complete
---

# STEP A: ARCHITECTURE DEFINITION
## System, Physical, Information & Interface Architecture for BSU-V1
### VN-TRN-001 | RISM-PRAD-DECS-OCP Step 7 of 15

**Purpose:** Define the complete architecture of the BSU-V1 (Beam Sensor Unit - Vietnamese Mark 1) at three levels: functional decomposition mapped to physical components, physical module structure with interfaces, and information/data flow architecture. This document serves as the **architectural reference** for all subsequent embodiment design steps.

**Input:** [[PRAD_R_rules]] (Rules compliance, optimized design), [[PRAD_P_principles]] (Principle-based decisions), [[RISM_I_critical_requirements]] (Design drivers)
**Output:** Architecture definition with ICD (Interface Control Document), ready for [[PRAD_D_structure]] (Design Structure)

**Selected Concept:** A "Baseline" (VDI 2225: 83.8%)
**Architecture Type:** Calibration-free acoustic TDOA, 4x MEMS microphones, FPGA+MCU hybrid processing

---

## 1. FUNCTIONAL DECOMPOSITION

### 1.1 Phase 2 Function-to-Component Mapping

The Phase 2 function structure (F1-F7) is mapped to specific physical components selected during RISM material screening and PRAD principles/rules application.

| Function | Sub-Function | Physical Component(s) | Part Number / Spec | Location |
|----------|-------------|----------------------|-------------------|----------|
| **F1: SENSE** | F1.1: Detect shockwave | 4x TDK ICS-40730 MEMS microphones | ICS-40730 (analog, 164 dB SPL max) | Sensor Bar, Daughter PCBs |
| | F1.2: Convert to electrical | Integrated in MEMS mic (capacitive transducer) | -- | Sensor Bar |
| | F1.3a: Pre-amplify | 4x TI OPA1612 low-noise op-amps | OPA1612AID (SOIC-8) | Daughter PCBs |
| | F1.3b: Bandpass filter | 4x 2nd-order Butterworth BPF (1 kHz - 100 kHz) | Passive R-C-R + OPA1612 stages | Daughter PCBs |
| | F1.3c: Auto-gain control | 4x Analog Devices AD8338 VGA | AD8338ACPZ (LFCSP-16) | Daughter PCBs |
| **F2: MEASURE** | F2.1: Digitize signals | TI ADS8688 8-ch ADC (500 kSPS, 16-bit, SPI) | ADS8688IDBT (TSSOP-38) | Main PCB |
| | F2.2: Timestamp arrivals | Lattice iCE40UP5K FPGA | iCE40UP5K-SG48I (QFN-48) | Main PCB |
| | F2.3: Calculate time diffs | FPGA hardware comparators + timestamp registers | FPGA gateware (RTL) | Main PCB |
| **F3: COMPUTE** | F3.1: Execute TDOA algorithm | STM32H743 MCU (Cortex-M7, 480 MHz) | STM32H743VIT6 (LQFP-100) | Main PCB |
| | F3.2: Env. compensation | Temperature-implicit in calibration-free algorithm | Firmware (no external sensor needed) | Main PCB |
| | F3.3: Classify hit/miss | MCU firmware (target silhouette overlay) | Firmware module | Main PCB |
| **F4: COMMUNICATE** | F4.1: Encode scoring data | MCU Ethernet stack (lwIP TCP/IP) | Firmware module | Main PCB |
| | F4.2: Transmit to station | Microchip LAN8720A Ethernet PHY + Pulse H1102NL | LAN8720A-CP (QFN-24) + H1102NL | Main PCB |
| | F4.3: Receive commands | Same Ethernet path (bidirectional TCP/IP) | RJ45 IP67 connector (Amphenol RJFTV) | Enclosure panel |
| **F5: PRESENT** | F5.1: Display X,Y | External HTML5 web application | Software (browser-based) | Control Station (not BSU) |
| | F5.2: Compute statistics | External web application | Software | Control Station |
| | F5.3: Generate reports | External web application | Software | Control Station |
| **F6: SUPPLY** | F6.1: Store energy | Samsung INR18650-35E 4S1P (14.8V, 10Ah, 148 Wh) | INR18650-35E x4 | Power Module |
| | F6.2a: Battery management | TI BQ76940 BMS IC | BQ76940DBTR (TSSOP-44) | Power PCB |
| | F6.2b: Charge control | TI BQ25700A multi-cell charger | BQ25700ARSNR (QFN-32) | Power PCB |
| | F6.2c: Regulate 5V | TI TPS54331 buck converter (3A, 5V) | TPS54331DR (SOIC-8) | Power PCB |
| | F6.2d: Regulate 3.3V | TI TPS62160 ultra-low-noise buck (1A, 3.3V) | TPS62160DSGR (SOT-6) | Power PCB |
| | F6.3: Monitor power | TI BQ27441 fuel gauge (I2C to MCU) | BQ27441DRZR (SON-12) | Power PCB |
| **F7: PROTECT** | F7.1a: Structural | Al 6061-T6 enclosure (250x180x120mm, 4mm wall) | CNC machined billet, MIL-A-8625F Type III | Enclosure Module |
| | F7.1b: Seal environment | EPDM O-ring gaskets (AS568A) | 70 Shore A EPDM, Vietnamese rubber | Enclosure Module |
| | F7.1c: Chemical protect | HumiSeal 1B31 acrylic conformal coating | IPC-CC-830C Class 3 | Applied to all PCBs |
| | F7.2: Ballistic protect | Low-profile sensor bar below target plane | Design geometry (SAF-02) | Sensor Bar |
| | F7.3: Self-diagnose | BIT firmware (power, sensor, FPGA, comm, temp) | Firmware module on MCU | Main PCB |

### 1.2 Function-to-Component Traceability Matrix

This matrix traces every Phase 2 function to its physical realization and the requirement it satisfies.

```
FUNCTION          COMPONENT                   KEY REQUIREMENT
--------          ---------                   ---------------
F1.1 Detect       ICS-40730 MEMS mic          FRC-01 (164 dB SPL)
F1.2 Convert      ICS-40730 (integrated)      SIG-04 (accuracy)
F1.3a Preamp      OPA1612                     SIG-05 (500 kSPS)
F1.3b BPF         Butterworth 1-100 kHz       KIN-01/02 (Mach 1.3-3.5)
F1.3c AGC         AD8338                      FRC-01 (dynamic range)
F2.1 Digitize     ADS8688 ADC                 SIG-05 (16-bit, 500 kSPS)
F2.2 Timestamp    iCE40UP5K FPGA              SIG-04 (timing <2ns jitter)
F2.3 Time diff    FPGA gateware               OPR-08 (calibration-free)
F3.1 TDOA algo    STM32H743 MCU               SIG-04, OPR-08
F3.2 Compensation Firmware (implicit)          OPR-01 (-10 to +60 deg C)
F3.3 Classify     Firmware                    SIG-03 (X,Y + hit/miss)
F4.1 Encode       lwIP TCP/IP stack           SIG-01 (100BaseT)
F4.2 Transmit     LAN8720A + H1102NL          SIG-01, SIG-08 (10 lanes)
F4.3 Receive      Same Ethernet               SIG-06 (FASIT)
F5.x Present      External web app            SIG-09, SIG-10, ERG-03
F6.1 Store        INR18650-35E 4S1P           ENG-03 (10h runtime)
F6.2a BMS         BQ76940                     SAF-04 (battery safety)
F6.2b Charge      BQ25700A                    ENG-01/02/06 (10.5-28V)
F6.2c 5V rail     TPS54331                    ENG-05 (15W budget)
F6.2d 3.3V rail   TPS62160                    ENG-05
F6.3 Monitor      BQ27441                     MNT-02 (BIT)
F7.1a Structure   Al 6061-T6 enclosure        OPR-07 (IP67), FRC-02/03
F7.1b Seal        EPDM O-rings                OPR-04/05 (rain, dust)
F7.1c Chemical    HumiSeal 1B31               MAT-03 (conformal)
F7.2 Ballistic    Geometry (bar below target)  SAF-02
F7.3 BIT          MCU firmware                MNT-02
```

### 1.3 Physical Location Map

```
BSU-V1 PHYSICAL LOCATION MAP
==============================

         TARGET FRAME (NATO / Vietnamese)
         ================================
         |                              |
         |      DETECTION ZONE          |
         |      3000 x 2500 mm          |
         |                              |
         |    [Target Silhouette]        |
         |                              |
         |                              |
         |==============================| <-- Sensor bar mounted here
         |  M1    M2    M3    M4        |
         ==========|=====================
                   |
            500mm shielded cable (I-006)
                   |
         ==========================================
         |        PROCESSING ENCLOSURE             |
         |        250 x 180 x 120 mm               |
         |                                          |
         |  ZONE A: Main Processing                 |
         |  +-------------------------------+       |
         |  | Main PCB (160 x 100 mm)       |       |
         |  | [FPGA] [MCU] [ADC] [PHY]      |       |
         |  | [Flash] [Temp] [Accel]         |       |
         |  +-------------------------------+       |
         |                                          |
         |  ZONE B: Power Management                |
         |  +-------------------+  +----------+     |
         |  | Power PCB         |  | Battery  |     |
         |  | (80 x 60 mm)     |  | Pack     |     |
         |  | [BMS] [Charger]  |  | 4S1P     |     |
         |  | [5V] [3.3V]     |  | 14.8V    |     |
         |  +-------------------+  | 10Ah    |     |
         |                         +----------+     |
         |                                          |
         |  ZONE C: Connectors (panel-mount)        |
         |  [RJ45-IP67]  [4-pin PWR-IP67]  [LEDs]  |
         |                                          |
         ==========================================
              |                    |
              | Ethernet           | DC Power
              | CAT5e/6            | (optional)
              | (50-100m)          | (10.5-28V)
              |                    |
         ==========================================
         |     CONTROL STATION (any device)         |
         |     Web browser -> HTML5 application     |
         ==========================================
```

**Zone Allocation Rationale:**
- **Zone A (Main PCB):** Positioned against 6mm aluminum base plate for thermal conduction. FPGA and MCU thermal pads aligned with base plate standoffs.
- **Zone B (Power):** Battery pack at enclosure base for low center of gravity (P4: Stability). Power PCB adjacent for short power traces. Battery accessible via battery door without disturbing Zone A.
- **Zone C (Connectors):** All external connectors on one face (south wall) for cable routing simplicity. LED window on same face for status visibility.

---

## 2. PHYSICAL ARCHITECTURE

### 2.1 Module Definition

The BSU-V1 is decomposed into 5 modules, each designed as either a Line Replaceable Unit (LRU) or a maintenance-replaceable component.

```
BSU-V1 MODULE BREAKDOWN
=========================

MODULE 1: SENSOR BAR ASSEMBLY (LRU)
+--------------------------------------------------+
|  Al 6063-T5 C-channel extrusion (1040mm)          |
|  +--------+  +--------+  +--------+  +--------+  |
|  | Daugh. |  | Daugh. |  | Daugh. |  | Daugh. |  |
|  | PCB #1 |  | PCB #2 |  | PCB #3 |  | PCB #4 |  |
|  | ICS-   |  | ICS-   |  | ICS-   |  | ICS-   |  |
|  | 40730  |  | 40730  |  | 40730  |  | 40730  |  |
|  | OPA1612|  | OPA1612|  | OPA1612|  | OPA1612|  |
|  | AD8338 |  | AD8338 |  | AD8338 |  | AD8338 |  |
|  | BPF    |  | BPF    |  | BPF    |  | BPF    |  |
|  +--------+  +--------+  +--------+  +--------+  |
|  [Rubber Boot x4]  [Cam Clamp x2]                |
|  [500mm shielded cable + IP67 circular connector] |
+--------------------------------------------------+

MODULE 2: MAIN PROCESSING MODULE (LRU)
+--------------------------------------------------+
|  Main PCB (160 x 100 mm, 4-layer FR-4 Tg170)     |
|                                                    |
|  [iCE40UP5K FPGA]  [STM32H743 MCU]               |
|  [ADS8688 ADC]     [LAN8720A PHY]                |
|  [H1102NL magnetics] [W25Q128 Flash]              |
|  [TMP117 Temp]     [LIS2DH12 Accel]              |
|  [3x Status LEDs]  [SWD Debug Header]             |
|  [4-pin sensor input header]                       |
|  [Power input header from Power PCB]               |
+--------------------------------------------------+

MODULE 3: POWER MODULE (LRU)
+--------------------------------------------------+
|  Power PCB (80 x 60 mm, 2-layer FR-4)             |
|  [BQ76940 BMS]    [BQ25700A Charger]              |
|  [TPS54331 5V]    [TPS62160 3.3V]                |
|  [BQ27441 Fuel Gauge] [SMAJ58A TVS]              |
|  [Reverse polarity MOSFET]                         |
|                                                    |
|  Battery Pack (4S1P, 14.8V 10Ah)                  |
|  [Samsung INR18650-35E x4]                         |
|  [BMS protection board]                            |
|  [NTC thermistor]                                  |
|  [Heat-shrink housing with label]                  |
+--------------------------------------------------+

MODULE 4: ENCLOSURE MODULE (non-LRU, structural)
+--------------------------------------------------+
|  Enclosure Body (Al 6061-T6, CNC machined)         |
|  - Body shell (top half)                           |
|  - Base plate (bottom, 6mm, heat sink function)    |
|  - O-ring groove (EPDM gasket, captive)            |
|  - 4x M3 standoffs for Main PCB (rubber grommets) |
|  - 4x M3 standoffs for Power PCB                  |
|  - Battery cradle with Velcro strap               |
|  - Cable gland #1: IP67 RJ45 (Amphenol RJFTV)    |
|  - Cable gland #2: IP67 4-pin power connector     |
|  - Cable gland #3: IP67 circular for sensor bar   |
|  - LED window (integrated into lid)                |
|  - Battery door (cam-latch, IP67 sub-gasket)       |
|  - 6x M4 lid bolts (SS 316 + nylon washers)       |
|  - 4x M6 threaded inserts (VESA 100x100 mount)    |
|  - 2x Dowel pins (lid-body alignment)              |
|  - Hard anodize Type III (25 um) + RAL 6031 paint |
+--------------------------------------------------+

MODULE 5: CABLE ASSEMBLY (field-replaceable)
+--------------------------------------------------+
|  Cable 5A: Ethernet Cable                          |
|  - CAT5e/6 outdoor-rated (PE-HDPE or PUR jacket)  |
|  - 50m standard / 100m option                      |
|  - IP67 RJ45 connectors both ends                  |
|  - Gel-filled for moisture protection               |
|                                                    |
|  Cable 5B: Sensor Bar Cable (integrated with M1)   |
|  - 500mm 4-pair shielded (overall braid + foil)    |
|  - IP67 circular connector (enclosure end)          |
|  - Permanently attached to sensor bar              |
|                                                    |
|  Cable 5C: External DC Power Cable (optional)      |
|  - 2-conductor 18AWG with IP67 4-pin connector     |
|  - 5m standard length                              |
|  - Compatible with 12V vehicle / 24V mil systems   |
+--------------------------------------------------+
```

### 2.2 Module Detail Specifications

#### Module 1: Sensor Bar Assembly

| Parameter | Specification |
|-----------|--------------|
| **Dimensions** | 1040 x 60 x 40 mm (L x W x H) |
| **Weight** | 1.2 kg |
| **Material** | Al 6063-T5 extrusion, C-channel, 3mm wall |
| **Sensors** | 4x TDK ICS-40730 on individual daughter PCBs (30 x 25 mm, 2-layer) |
| **Signal conditioning** | Per channel: OPA1612 preamp + Butterworth BPF (1-100 kHz) + AD8338 AGC |
| **Acoustic coupling** | Vietnamese natural rubber boots (40 Shore A), press-fit into machined pockets |
| **Sensor geometry** | Non-coplanar: M1/M3 at z=0, M2/M4 at z=30mm offset (per expired patent WO1991010876A1) |
| **Sensor spacing** | 347mm equidistant (3 spans across 1040mm bar) |
| **Mounting** | 2x cam-lever clamps at L/3 positions (347mm from each end) |
| **Cable** | 500mm 4-pair shielded, IP67 circular connector |
| **Finish** | Anodize Type III + RAL 6031 paint |
| **LRU status** | **YES** -- Field-replaceable in <10 minutes |
| **Assembly method** | Clamp to target frame (tool-less cam levers), connect circular connector to enclosure |
| **Disassembly method** | Disconnect circular connector, release 2 cam levers, lift off |

**Interfaces:**
- **To Module 2 (Main PCB):** I-001 -- 4x analog signals via shielded cable through I-006 connector
- **To Module 4 (Enclosure):** I-006 -- 500mm cable with IP67 circular connector
- **To Target Frame:** I-007 -- 2x cam-lever clamps, VESA-compatible mounting

#### Module 2: Main Processing Module

| Parameter | Specification |
|-----------|--------------|
| **PCB size** | 160 x 100 mm, 4-layer, FR-4 Tg170, 1.6mm |
| **Weight** | 0.12 kg (populated PCB) |
| **FPGA** | Lattice iCE40UP5K-SG48I (5,280 LUT, 1 Mbit SPRAM) |
| **MCU** | STM32H743VIT6 (Cortex-M7, 480 MHz, 1 MB RAM, 2 MB Flash) |
| **ADC** | TI ADS8688 (8-ch, 500 kSPS/ch, 16-bit, SPI) |
| **Ethernet PHY** | Microchip LAN8720A (100 Mbps, RMII) |
| **Magnetics** | Pulse H1102NL (integrated transformer) |
| **Flash** | W25Q128 (16 MB SPI, dual-image boot) |
| **Temp sensor** | TI TMP117 (diagnostics, NOT calibration) |
| **Accelerometer** | ST LIS2DH12 (vibration/transport detection) |
| **Clock** | 48 MHz crystal oscillator (20 ppm, no PLL) |
| **Conformal coating** | HumiSeal 1B31 acrylic, IPC-CC-830C Class 3 |
| **LRU status** | **YES** -- Depot-replaceable in <20 minutes |
| **Assembly method** | 4x M3 brass standoffs with EPDM rubber grommets to base plate |
| **Disassembly method** | Open enclosure lid (6x M4), disconnect 3 internal headers, unscrew 4x M3 |

**Interfaces:**
- **To Module 1 (Sensor Bar):** I-001 -- 4x analog signals via 4-pin internal header
- **To Module 3 (Power):** I-002 -- 5V, 3.3V, GND, I2C (fuel gauge) via board-to-board connector
- **To Module 4 (Enclosure):** Mechanical mounting (4x M3 standoffs); thermal pad to base plate
- **To External (Ethernet):** I-003 -- RJ45 IP67 panel-mount connector

#### Module 3: Power Module

| Parameter | Specification |
|-----------|--------------|
| **Power PCB size** | 80 x 60 mm, 2-layer, FR-4 |
| **Power PCB weight** | 0.04 kg |
| **Battery pack** | 4S1P Samsung INR18650-35E, 14.8V nominal, 10Ah, 148 Wh |
| **Battery weight** | 3.5 kg (cells + BMS + housing) |
| **BMS** | TI BQ76940 (4-10 cell, OV/UV/OC/OT/balance) |
| **Charger** | TI BQ25700A (12-28V input, 2A charge, NVDC power path) |
| **5V rail** | TI TPS54331 (3A buck, 90%+ efficiency) |
| **3.3V rail** | TI TPS62160 (1A buck, ultra-low-noise for analog) |
| **Fuel gauge** | TI BQ27441 (state-of-charge, I2C to MCU) |
| **Input protection** | SMAJ58A TVS + reverse polarity P-MOSFET + 3A polymer fuse |
| **Input range** | 10.5 - 28V DC (12V vehicle, 24V military, 18-36V solar via BQ25700A) |
| **Runtime** | 11.4 hours at 13W average (14.8V x 10Ah / 13W) |
| **LRU status** | **YES** -- Battery field-replaceable in <2 minutes (battery door); Power PCB depot-replaceable |
| **Assembly method** | Power PCB: 4x M3 standoffs. Battery: insert into cradle, secure Velcro strap |
| **Disassembly method** | Battery: open battery door (cam latch), pull battery tab. PCB: open lid, disconnect headers, unscrew |

**Interfaces:**
- **To Module 2 (Main PCB):** I-002 -- 5V, 3.3V, GND, I2C via board-to-board connector
- **To Battery Pack:** I-004 -- 14.8V, BMS data lines, NTC thermistor via JST-PH 6-pin
- **To External Power:** I-005 -- 10.5-28V DC via IP67 4-pin panel connector
- **To Module 4 (Enclosure):** Battery cradle mechanical interface; Power PCB standoffs

#### Module 4: Enclosure Module

| Parameter | Specification |
|-----------|--------------|
| **Material** | Al 6061-T6 (body + lid) |
| **External dims** | 250 x 180 x 120 mm |
| **Wall thickness** | 4mm (body), 6mm (base plate / heat sink) |
| **Weight** | 1.8 kg (enclosure only, empty) |
| **Manufacturing** | CNC machined from billet, 3-axis (Vietnamese job shop) |
| **Sealing** | EPDM O-ring (captive in groove), IP67 per IEC 60529 |
| **Lid closure** | 6x M4 SS316 bolts (from 8, reduced per PRAD-R Rule 2: Simplicity) |
| **Alignment** | 2x dowel pins (lid-body registration) |
| **Battery door** | Cam-latch with IP67 sub-gasket, spring-loaded default-closed |
| **Cable glands** | 3x IP67 panel-mount (RJ45, 4-pin power, circular sensor) |
| **LED window** | Integrated into lid (3x LEDs: Power/Ready/Error) |
| **Surface finish** | Type III hard anodize (25 um, MIL-A-8625F) + RAL 6031 Bronze Green paint |
| **Mounting** | 4x M6 threaded inserts (Helicoil), VESA 100x100 pattern |
| **External cam clamps** | 2x for VESA mount + 2x cam-lever quick-attach |
| **LRU status** | **NO** -- Structural element; replaced only at depot overhaul |
| **Assembly** | All modules install into enclosure; close lid with 6x M4 bolts |
| **Disassembly** | Remove 6x M4 lid bolts; lift lid; access all internal modules |

**Interfaces:**
- **To all internal modules:** Mechanical mounting (standoffs, cradle, cable gland passthroughs)
- **To external:** I-003 (RJ45), I-005 (DC power), I-006 (sensor bar cable), I-007 (target frame mount)
- **Thermal interface:** Base plate to FPGA/MCU via thermal pads through standoffs

#### Module 5: Cable Assembly

| Cable | Specification |
|-------|--------------|
| **5A: Ethernet** | CAT5e/6 outdoor, PE-HDPE jacket, gel-filled, IP67 RJ45 both ends, 50m std / 100m option |
| **5B: Sensor Bar** | 4-pair individually shielded + overall braid, 500mm, IP67 circular connector (enclosure end), permanent to sensor bar |
| **5C: DC Power** | 2-conductor 18 AWG, PUR jacket, IP67 4-pin connector, 5m standard |
| **LRU status** | **YES** (5A and 5C are field-replaceable; 5B is integral to Module 1) |
| **Assembly** | 5A: Plug Ethernet into BSU and switch. 5C: Plug into BSU and power source. Tool-less. |
| **Disassembly** | Unplug connectors (bayonet quarter-turn release for 5A; threaded for 5C) |

### 2.3 Physical Architecture Diagram

```
BSU-V1 PHYSICAL ARCHITECTURE -- EXPLODED VIEW
=================================================

                    TARGET FRAME
                    ============
                         |
                         | I-007: VESA 100x100 + Cam Clamps
                         |
    +====================|====================+
    |          MODULE 1: SENSOR BAR           |
    |  [M1]-[M2]-[M3]-[M4] Non-coplanar      |
    |  4x Daughter PCBs in rubber boots       |
    |  2x Cam-lever clamps                    |
    +=========================================+
                         |
                         | I-006: 500mm shielded cable
                         | (IP67 circular connector)
                         |
    +=========================================+
    |          MODULE 4: ENCLOSURE            |
    |  +-----------------------------------+  |
    |  |        LID (Al 6061-T6)           |  |
    |  |  [LED Window] [6x M4 bolts]       |  |
    |  |  [2x Dowel Pins] [O-ring groove]  |  |
    |  +---------+-----------+-------------+  |
    |            |           |                |
    |  +---------+-+  +-----+-------+         |
    |  | MODULE 2: |  | MODULE 3:   |         |
    |  | MAIN PCB  |  | POWER PCB   |         |
    |  | FPGA+MCU  |  | BMS+DC-DC   |         |
    |  | ADC+PHY   |  |             |         |
    |  |           |  | +---------+ |         |
    |  |     I-002 |<>| | BATTERY | |         |
    |  |           |  | | 4S1P    | |         |
    |  +-----------+  | | 14.8V   | |         |
    |       |         | +---------+ |         |
    |       |         +------+------+         |
    |       |                |                |
    |  +----+---+  +--------+--+  +---------+ |
    |  |I-003   |  |I-005      |  |I-006    | |
    |  |RJ45    |  |4-pin PWR  |  |Circular | |
    |  |IP67    |  |IP67       |  |IP67     | |
    |  +--------+  +-----------+  +---------+ |
    |                                          |
    |  +---BASE PLATE (6mm, heat sink)------+  |
    |  |  [4x M6 VESA threaded inserts]     |  |
    |  +------------------------------------+  |
    +==========================================+
         |              |              |
         | Cable 5A     | Cable 5C     | Cable 5B
         | Ethernet     | DC Power     | (integral
         | 50-100m      | 5m           |  to M1)
         |              | (optional)   |
    +----+----+    +----+----+
    | Ethernet |    | 12/24V  |
    | Switch   |    | Source  |
    +----+-----+    +---------+
         |
    +----+----+
    | Control  |
    | Station  |
    | (Web UI) |
    +----------+
```

### 2.4 Module Interaction Matrix

| | M1: Sensor Bar | M2: Main PCB | M3: Power | M4: Enclosure | M5: Cables |
|---|---|---|---|---|---|
| **M1: Sensor Bar** | -- | I-001 (analog) | -- | I-006 (mech), I-007 (frame) | 5B (integral) |
| **M2: Main PCB** | I-001 (analog) | -- | I-002 (power + I2C) | Mech (standoffs), Thermal (pad) | I-003 (Ethernet) |
| **M3: Power** | -- | I-002 (power + I2C) | -- | Mech (standoffs + cradle) | I-005 (DC power) |
| **M4: Enclosure** | I-006, I-007 | Mech, Thermal | Mech | -- | Glands (all cables) |
| **M5: Cables** | 5B | I-003 (5A) | I-005 (5C) | Glands | -- |

**Interface Types:**
- **Mechanical:** Physical mounting, load transfer, alignment
- **Electrical:** Power distribution, analog signals, digital data
- **Thermal:** Heat conduction path from ICs to ambient
- **Data:** Digital information flow (SPI, I2C, RMII, TCP/IP)

---

## 3. INFORMATION ARCHITECTURE

### 3.1 Sensor Signal Path

The primary data flow from acoustic event to operator display:

```
SENSOR SIGNAL PATH (Shot Detection → Display)
==============================================

STAGE 1: ACOUSTIC CAPTURE (Module 1: Sensor Bar)
+--------+    +--------+    +--------+    +--------+
|  MIC 1 |    |  MIC 2 |    |  MIC 3 |    |  MIC 4 |
| ICS-   |    | ICS-   |    | ICS-   |    | ICS-   |
| 40730  |    | 40730  |    | 40730  |    | 40730  |
+---+----+    +---+----+    +---+----+    +---+----+
    |             |             |             |
    v             v             v             v
+---+----+    +---+----+    +---+----+    +---+----+
| PREAMP |    | PREAMP |    | PREAMP |    | PREAMP |
| OPA1612|    | OPA1612|    | OPA1612|    | OPA1612|
| G = 20 |    | G = 20 |    | G = 20 |    | G = 20 |
+---+----+    +---+----+    +---+----+    +---+----+
    |             |             |             |
    v             v             v             v
+---+----+    +---+----+    +---+----+    +---+----+
|  BPF   |    |  BPF   |    |  BPF   |    |  BPF   |
| 1-100  |    | 1-100  |    | 1-100  |    | 1-100  |
| kHz    |    | kHz    |    | kHz    |    | kHz    |
+---+----+    +---+----+    +---+----+    +---+----+
    |             |             |             |
    v             v             v             v
+---+----+    +---+----+    +---+----+    +---+----+
|  AGC   |    |  AGC   |    |  AGC   |    |  AGC   |
| AD8338 |    | AD8338 |    | AD8338 |    | AD8338 |
| 0-80dB |    | 0-80dB |    | 0-80dB |    | 0-80dB |
+---+----+    +---+----+    +---+----+    +---+----+
    |             |             |             |
    +=============+=============+=============+
                  | I-001: 4x analog
                  | (shielded cable, 500mm)
                  |
STAGE 2: DIGITIZATION (Module 2: Main PCB)
                  |
                  v
        +---------+---------+
        |    ADS8688 ADC    |
        |  8-ch, 500 kSPS   |
        |  16-bit, SPI      |
        |  V_ref = 4.096V   |
        +---------+---------+
                  |
                  | SPI bus (20 MHz)
                  |
STAGE 3: TIMESTAMPING (Module 2: Main PCB)
                  |
                  v
        +---------+---------+
        |   iCE40UP5K FPGA  |
        |                   |
        |  4x threshold     |
        |  comparators      |
        |  (programmable)   |
        |                   |
        |  48 MHz counter   |
        |  = 20.83 ns       |
        |  resolution       |
        |                   |
        |  Timestamp regs   |
        |  t1, t2, t3, t4  |
        |                   |
        |  Delta-T calc:    |
        |  dt12, dt13, dt14 |
        |  dt23, dt24, dt34 |
        +---------+---------+
                  |
                  | SPI bus (register read)
                  |
STAGE 4: COMPUTATION (Module 2: Main PCB)
                  |
                  v
        +---------+---------+
        |   STM32H743 MCU   |
        |   Cortex-M7       |
        |   480 MHz         |
        |                   |
        |  Calibration-Free |
        |  TDOA Algorithm:  |
        |  - 6 delta-T vals |
        |  - Geometry matrix|
        |  - Least-squares  |
        |    solver         |
        |  - X,Y output     |
        |  - Hit/miss class.|
        |                   |
        |  Processing time: |
        |  ~0.5 ms          |
        +---------+---------+
                  |
                  | RMII interface
                  |
STAGE 5: TRANSMISSION (Module 2 → External)
                  |
                  v
        +---------+---------+
        | LAN8720A Ethernet |
        | PHY (100BaseT)    |
        +----+----+---------+
             |
             v
        +----+----+
        | H1102NL |
        | Magnetics|
        +----+----+
             |
             | I-003: IP67 RJ45
             | 100BaseT Ethernet
             | TCP/IP packet:
             |   {lane_id, shot_id,
             |    X_mm, Y_mm,
             |    timestamp_us,
             |    hit_miss,
             |    confidence}
             |
             | Cable 5A (50-100m)
             |
STAGE 6: DISPLAY (External Control Station)
             |
             v
        +----+----+
        | Ethernet |
        | Switch   |
        +----+----+
             |
             v
        +----+----------+
        | Control       |
        | Station       |
        | (any browser) |
        |               |
        | HTML5 Web App |
        | - Target plot |
        | - Statistics  |
        | - AAR reports |
        +---------------+
```

### 3.2 Data Rate and Latency Budget

| Stage | Data Type | Data Rate | Latency | Cumulative Latency |
|-------|-----------|-----------|---------|-------------------|
| **1. Acoustic → Mic** | Pressure wave (N-wave) | N/A (physics) | ~3 us (speed of sound across bar) | 3 us |
| **2. Mic → Preamp → BPF → AGC** | Analog voltage | Bandwidth: 1-100 kHz | 10 us (filter group delay) | 13 us |
| **3. Analog → ADC** | 4x analog channels | 500 kSPS x 16-bit x 4 ch = 32 Mbit/s | 2 us (conversion time) | 15 us |
| **4. ADC → FPGA** | SPI digital stream | 20 MHz SPI clock | 4 us (4-channel DMA transfer) | 19 us |
| **5. FPGA timestamp** | 4x timestamps + 6x delta-T | Internal registers | 1 us (combinational logic) | 20 us |
| **6. FPGA → MCU** | 6x 32-bit delta-T values | SPI register read | 5 us | 25 us |
| **7. MCU TDOA algorithm** | Matrix computation | N/A (internal) | 500 us (least-squares solver) | 525 us |
| **8. MCU → Ethernet PHY** | TCP/IP packet (~128 bytes) | 100 Mbps | 10 us (MAC/PHY latency) | 535 us |
| **9. Ethernet cable** | 100BaseT signals | 100 Mbps | 500 ns per 100m cable | 536 us |
| **10. Switch + network** | TCP/IP routing | 100 Mbps | 1 ms (switch forwarding) | 1.5 ms |
| **11. Web app rendering** | HTTP/WebSocket update | ~1 kB per shot | 5-50 ms (browser render) | 7-52 ms |
| **TOTAL end-to-end** | | | | **<55 ms** |

**Latency budget compliance:**
- KIN-05 requirement: <=500 ms (MUST), target <=200 ms
- Actual: ~7-55 ms (depending on browser) -- **well within budget**
- Dominant latency: web browser rendering (not hardware)

### 3.3 Control Path

```
CONTROL PATH (Operator → BSU Configuration)
=============================================

OPERATOR                    CONTROL STATION             BSU-V1
(human)                     (web browser)               (embedded)
                                |
[Click "Configure"]  ------>   |
                               |
    HTTP POST request  ------> | ----> TCP/IP packet
    {command: "set_mode",      |       over Ethernet
     params: {                 |
       mode: "live_fire",      |       I-003
       lanes: [1,2,3],        |       (RJ45)
       target: "E-type"       |          |
     }}                        |          v
                               |   +------+------+
                               |   | STM32H743   |
                               |   | MCU          |
                               |   | Parse JSON   |
                               |   | Validate     |
                               |   | Apply config |
                               |   +------+------+
                               |          |
                               |   +------+------+
                               |   | iCE40UP5K   |
                               |   | FPGA         |
                               |   | Update       |
                               |   | thresholds   |
                               |   | & trigger    |
                               |   | parameters   |
                               |   +-------------+
                               |          |
    HTTP 200 OK + status  <--- | <--- TCP/IP response
    {status: "configured",     |     {mode: "live_fire",
     fpga_ver: "1.2.0",       |      bit_status: "PASS",
     battery: "87%"}           |      ready: true}
```

**Command Set (MCU firmware):**

| Command | Direction | Protocol | Payload | Response |
|---------|-----------|----------|---------|----------|
| SET_MODE | Station -> BSU | TCP/IP JSON | mode, target_type, threshold | ACK + status |
| GET_STATUS | Station -> BSU | TCP/IP JSON | (none) | BIT result, battery %, shot count |
| SHOT_EVENT | BSU -> Station | TCP/IP JSON | X, Y, timestamp, hit_miss, lane_id | (none, push) |
| RESET | Station -> BSU | TCP/IP JSON | (none) | ACK + reboot |
| FIRMWARE_UPDATE | Station -> BSU | TCP/IP binary | Firmware image + CRC32 | ACK + progress % |
| GET_LOG | Station -> BSU | TCP/IP JSON | date range | Shot log entries |
| SET_THRESHOLD | Station -> BSU | TCP/IP JSON | Channel, level (mV) | ACK |
| CALIBRATE_AGC | Station -> BSU | TCP/IP JSON | (none) | AGC levels per channel |

### 3.4 BIT (Built-In Test) Path

```
BIT SEQUENCE (Power-On Self-Test)
==================================

POWER ON
    |
    v
[1] VOLTAGE CHECK (2s)
    +---> 5V rail: 4.75-5.25V?     --> PASS/FAIL
    +---> 3.3V rail: 3.14-3.46V?   --> PASS/FAIL
    +---> Battery: 12.0-16.8V?     --> PASS/FAIL (+ SOC %)
    +---> Input (if ext): 10.5-28V? --> PASS/FAIL
    |
    v
[2] FPGA CONFIG (3s)
    +---> Load bitstream from W25Q128 (application image)
    +---> CRC32 check             --> PASS/FAIL
    +---> If FAIL: load golden image --> PASS (degraded)
    +---> FPGA heartbeat to MCU    --> PASS/FAIL
    |
    v
[3] SENSOR TEST (5s)
    +---> Enable AGC on all 4 channels
    +---> Read noise floor per channel
    +---> Noise floor < threshold?  --> PASS/FAIL per channel
    +---> Channel-to-channel match  --> PASS/FAIL (>20dB diff = FAIL)
    +---> Report: CH1=OK, CH2=OK, CH3=OK, CH4=OK (or individual FAIL)
    |
    v
[4] FPGA TIMING TEST (2s)
    +---> Generate internal test pulse
    +---> Verify 4x timestamps captured
    +---> Timestamp jitter < 50ns?  --> PASS/FAIL
    +---> Counter rollover test     --> PASS/FAIL
    |
    v
[5] COMMUNICATION TEST (3s)
    +---> Ethernet PHY link status  --> UP/DOWN
    +---> Send test packet to control station --> ACK/TIMEOUT
    +---> If Ethernet DOWN: log locally, retry every 10s
    |
    v
[6] ENVIRONMENTAL CHECK (1s)
    +---> TMP117 temperature reading
    +---> Range: -10 to +60 deg C?  --> PASS/WARNING
    +---> LIS2DH12 accelerometer baseline
    +---> Vibration level < threshold? --> PASS/WARNING
    |
    v
[7] BIT SUMMARY (immediate)
    +---> Aggregate all results
    +---> ALL PASS: Green LED solid     --> READY
    +---> WARNING:  Green LED blink      --> OPERATIONAL (degraded)
    +---> ANY FAIL: Red LED solid       --> FAULT (not operational)
    +---> Report to Control Station via Ethernet
    +---> Log to W25Q128 flash
    |
    v
READY FOR OPERATION (total boot: <20s typical, <30s worst case)
```

**BIT coverage analysis:**

| Subsystem | BIT Test | Fault Detected | Coverage |
|-----------|----------|---------------|----------|
| Power (5V, 3.3V) | Voltage monitor | Over/under voltage, regulator failure | 100% |
| Battery | Fuel gauge + BMS | Low charge, cell imbalance, temperature | 100% |
| FPGA | Config CRC + heartbeat | Bitstream corruption, FPGA failure | 100% |
| ADC | Noise floor check | ADC failure, input stuck | 90% |
| Sensors (4 ch) | Noise floor + cross-check | Mic failure, cable open/short, preamp failure | 95% |
| Ethernet | Link + echo | PHY failure, cable, magnetics | 100% |
| Temperature | Range check | Sensor failure, environmental alarm | 100% |
| Firmware | CRC + watchdog | Flash corruption, hang | 100% |
| **Overall BIT coverage** | | | **~97%** |

### 3.5 Information Flow Diagram

```
COMPLETE INFORMATION FLOW -- BSU-V1
=====================================

                    ACOUSTIC DOMAIN          ANALOG DOMAIN
                    (air)                    (electrical)

Shockwave ------> [M1][M2][M3][M4] ------> [PREAMP x4]
(N-wave)          MEMS mics                 OPA1612
                  ICS-40730                      |
                                                 v
                                            [BPF x4]
                                            1-100 kHz
                                                 |
                                                 v
                                            [AGC x4]
                                            AD8338
                                                 |
                  I-001 (shielded cable)         |
                  ============================== |
                                                 |
                  DIGITAL DOMAIN                 v
                                            [ADS8688]
                                            16-bit ADC
                                            500 kSPS x 4
                                                 |
                                            SPI (20 MHz)
                                                 |
                                                 v
                                            [iCE40UP5K]
                                            FPGA
                                            - Threshold detect
                                            - Timestamp (48MHz)
                                            - Delta-T compute
                                                 |
                                            SPI registers
                                                 |
                                                 v
                                            [STM32H743]
                                            MCU
                                            - TDOA algorithm
                                            - Hit/miss classify
                                            - BIT management
                                            - TCP/IP stack
                                                 |
                   NETWORK DOMAIN               |
                                            RMII
                                                 |
                                                 v
                                            [LAN8720A]
                                            Ethernet PHY
                                                 |
                                            [H1102NL]
                                            Magnetics
                                                 |
                   I-003 (RJ45 IP67)            |
                   ============================= |
                                                 |
                                                 v
                                            [Ethernet Switch]
                                            100BaseT
                                                 |
                                                 v
                                            [Control Station]
                                            HTML5 Web App

    POWER DOMAIN                MONITORING DOMAIN

    [Battery] --> [BMS] ------> [BQ27441] --I2C--> [MCU]
       |           |                                  |
       v           v                                  v
    [Charger] --> [5V]          [TMP117] --I2C----> [MCU]
                    |                                 |
                    v           [LIS2DH12] -I2C---> [MCU]
                  [3.3V]                              |
                    |                           [BIT Results]
                    v                                 |
              All subsystems                     [Ethernet]
                                                     |
                                                [Web Dashboard]
```

---

## 4. INTERFACE CONTROL DOCUMENT (ICD)

### 4.1 Interface Register

| ICD # | Interface Name | Modules | Type | Criticality |
|-------|---------------|---------|------|-------------|
| I-001 | Sensor Bar to Main PCB | M1 <-> M2 | Analog electrical | HIGH (signal integrity) |
| I-002 | Main PCB to Power PCB | M2 <-> M3 | Power + digital | HIGH (power quality) |
| I-003 | Main PCB to External Ethernet | M2 <-> External | Data (network) | HIGH (primary comm) |
| I-004 | Power PCB to Battery Pack | M3 internal | Power + monitoring | HIGH (safety critical) |
| I-005 | Power PCB to External Power | M3 <-> External | Power input | MEDIUM |
| I-006 | Enclosure to Sensor Bar | M4 <-> M1 | Mech + electrical passthrough | HIGH (structural + signal) |
| I-007 | Enclosure to Target Frame | M4 <-> External | Mechanical | HIGH (positioning accuracy) |

### 4.2 I-001: Sensor Bar <-> Main PCB

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Convey 4 conditioned analog shockwave signals from sensor bar daughter PCBs to Main PCB ADC |
| **Signal count** | 4 analog channels + 4 analog grounds (8 conductors total) |
| **Signal characteristics** | 0 - 3.3V analog, bandwidth DC to 100 kHz, impedance 50 ohm |
| **Cable type** | 4-pair individually shielded (foil per pair) + overall braid shield |
| **Cable length** | 500 mm (fixed, integral to Module 1) |
| **Shielding** | Each pair: aluminum foil + drain wire. Overall: tinned copper braid (85% coverage) |
| **Connector (sensor bar end)** | Permanently terminated to sensor bar PCB headers |
| **Connector (enclosure end)** | IP67 circular connector, 12-pin (4 signal + 4 ground + 4 shield drain) |
| **Mating cycles** | >=500 cycles (IP67 circular rated for 1000+) |
| **Signal integrity** | Crosstalk: < -60 dB between any two channels at 100 kHz |
| **EMI** | Cable routed inside sensor bar C-channel (shielded by aluminum bar) |
| **Strain relief** | Molded boot at sensor bar entry; cable gland at enclosure entry |
| **Test method** | Signal injection: 1 kHz, 10 kHz, 100 kHz sine wave; verify amplitude and phase match across all 4 channels |

```
I-001 PIN ASSIGNMENT
=====================
Pin 1:  CH1_SIG  (Mic 1 conditioned analog)
Pin 2:  CH1_GND  (Mic 1 analog ground)
Pin 3:  CH2_SIG  (Mic 2 conditioned analog)
Pin 4:  CH2_GND  (Mic 2 analog ground)
Pin 5:  CH3_SIG  (Mic 3 conditioned analog)
Pin 6:  CH3_GND  (Mic 3 analog ground)
Pin 7:  CH4_SIG  (Mic 4 conditioned analog)
Pin 8:  CH4_GND  (Mic 4 analog ground)
Pin 9:  SHIELD_1 (Pair 1 drain wire)
Pin 10: SHIELD_2 (Pair 2 drain wire)
Pin 11: SHIELD_3 (Pair 3 drain wire)
Pin 12: SHIELD_4 (Pair 4 drain wire)
Shell:  OVERALL BRAID -> enclosure chassis ground
```

### 4.3 I-002: Main PCB <-> Power PCB

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Supply regulated power from Power Module to Main Processing Module; return fuel gauge data to MCU |
| **Connector type** | Board-to-board header, 2.54mm pitch, 10-pin (Molex KK 254 or equivalent) |
| **Power signals** | 5V (3A max), 3.3V (1A max), GND (2 pins for current return), VBAT_SENSE (battery voltage monitor) |
| **Digital signals** | I2C_SDA (fuel gauge BQ27441), I2C_SCL (100 kHz), POWER_GOOD (3.3V logic) |
| **Mechanical** | Positive retention latch; keyed (cannot insert reversed) |
| **Wire gauge** | 22 AWG for power pins (5V, GND); 26 AWG for signals |
| **Cable length** | 80 mm internal harness (per PRAD-R simplification: single internal harness) |
| **Decoupling** | 100 uF bulk + 10 uF MLCC at Main PCB power input |
| **Protection** | Power PCB provides POWER_GOOD signal; Main PCB will not boot until POWER_GOOD = HIGH |

```
I-002 PIN ASSIGNMENT
=====================
Pin 1:  +5V_REG     (5V regulated, 3A max)
Pin 2:  +5V_REG     (5V regulated, parallel for current capacity)
Pin 3:  +3V3_REG    (3.3V regulated, 1A max)
Pin 4:  GND         (Power ground return)
Pin 5:  GND         (Power ground return, parallel)
Pin 6:  VBAT_SENSE  (Battery voltage divided /4, for MCU ADC monitoring)
Pin 7:  I2C_SDA     (Fuel gauge data, 3.3V logic)
Pin 8:  I2C_SCL     (Fuel gauge clock, 100 kHz)
Pin 9:  POWER_GOOD  (Active HIGH when all rails stable)
Pin 10: RESERVED    (Future use: charge status or solar sense)
```

### 4.4 I-003: Main PCB <-> External Ethernet

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Bidirectional data communication between BSU and Control Station network |
| **Standard** | IEEE 802.3 100BASE-TX (Fast Ethernet) |
| **Protocol** | TCP/IP v4 (lwIP stack on MCU); HTTP/WebSocket for application layer |
| **Connector (BSU side)** | Amphenol RJFTV series, IP67 panel-mount RJ45, bayonet lock |
| **Connector (cable side)** | Matching Amphenol RJFTV field-install plug, IP67 when mated |
| **Cable** | CAT5e minimum, outdoor-rated, PE-HDPE jacket, gel-filled |
| **Max cable length** | 100m (per IEEE 802.3 spec) |
| **Data rate** | 100 Mbps (full duplex) |
| **Bandwidth required** | ~10 kbps per lane (128 bytes per shot at 10 shots/s max) |
| **Auto-MDIX** | Supported by LAN8720A (straight or crossover cable) |
| **IP addressing** | Static IP (configurable via web UI); default 192.168.1.x/24 |
| **PoE compatibility** | Passive PoE input accepted (12-48V on spare pairs); NOT IEEE 802.3af |
| **Isolation** | 1500 Vrms (H1102NL magnetics provide galvanic isolation) |
| **ESD protection** | TVS array on RJ45 connector pins (ESD rating: +-8 kV contact) |
| **LED indicators** | Link (green) and Activity (amber) on PHY; visible through enclosure LED window |

```
I-003 PIN ASSIGNMENT (RJ45 / T-568B)
======================================
Pin 1:  TX+    (Transmit data +)
Pin 2:  TX-    (Transmit data -)
Pin 3:  RX+    (Receive data +)
Pin 4:  NC     (or Passive PoE V+, optional)
Pin 5:  NC     (or Passive PoE V+, optional)
Pin 6:  RX-    (Receive data -)
Pin 7:  NC     (or Passive PoE V-, optional)
Pin 8:  NC     (or Passive PoE V-, optional)
Shell:  Chassis ground (via RJ45 metal body to enclosure)
```

### 4.5 I-004: Power PCB <-> Battery Pack

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Connect battery pack to BMS for monitoring, protection, and power delivery |
| **Connector type** | JST-PH 6-pin (2.0mm pitch), latched |
| **Voltage range** | 12.0V (cutoff) to 16.8V (fully charged) |
| **Max current** | 3A continuous, 8A peak (BMS OCP limit) |
| **Signals** | VBAT+ (battery positive), VBAT- (battery negative/ground), NTC (thermistor, 10K NTC), BALANCE_1, BALANCE_2, BALANCE_3 (cell tap points for BMS balancing) |
| **Wire gauge** | 20 AWG for VBAT+/VBAT- (power); 26 AWG for NTC and balance |
| **Cable length** | 150 mm (internal, battery cradle to Power PCB) |
| **Protection** | 3A polymer resettable fuse in-line on VBAT+ |
| **Temperature monitoring** | 10K NTC thermistor bonded to cell surface; BMS OTP at 60 deg C |
| **Mating cycles** | >=200 (battery replacement every ~3 years, ~10 cycles/year) |
| **Keying** | JST-PH is polarized (cannot reverse-insert) |

```
I-004 PIN ASSIGNMENT
=====================
Pin 1:  VBAT+      (Battery positive, 14.8V nom, 3A continuous max)
Pin 2:  BALANCE_1  (Cell 1-2 junction, 3.7V nominal)
Pin 3:  BALANCE_2  (Cell 2-3 junction, 7.4V nominal)
Pin 4:  BALANCE_3  (Cell 3-4 junction, 11.1V nominal)
Pin 5:  NTC        (10K NTC thermistor, bonded to cell pack)
Pin 6:  VBAT-      (Battery negative / ground)
```

### 4.6 I-005: Power PCB <-> External DC Power

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Accept external DC power for operation and battery charging |
| **Connector (BSU side)** | IP67 4-pin panel-mount circular connector (Amphenol or equivalent) |
| **Connector (cable side)** | Mating IP67 4-pin plug with strain relief |
| **Input voltage range** | 10.5 - 28V DC (compatible with 12V vehicle, 24V military, 18-36V solar via BQ25700A NVDC) |
| **Input current** | 3A maximum (fused at 5A slow-blow) |
| **Conductor** | 18 AWG x 2 (V+ and GND) + 2 spare pins |
| **Cable length** | 5m standard (Cable 5C) |
| **Protection** | TVS (SMAJ58A, 58V clamp), reverse polarity P-MOSFET, 5A fuse |
| **Hot-plug** | Yes -- BQ25700A NVDC power path supports insertion/removal while operating on battery |
| **Color coding** | Green connector body (distinct from blue Ethernet) |
| **Mating cycles** | >=1000 |

```
I-005 PIN ASSIGNMENT
=====================
Pin 1:  V_EXT+     (External DC positive, 10.5-28V)
Pin 2:  GND_EXT    (External DC ground)
Pin 3:  RESERVED   (Future: solar panel sense or RS-485)
Pin 4:  RESERVED   (Future: remote ON/OFF or charge enable)
Shell:  Chassis ground
```

### 4.7 I-006: Enclosure <-> Sensor Bar

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Route 4 analog sensor signals from external sensor bar through IP67 enclosure wall to Main PCB |
| **Connector (enclosure side)** | IP67 circular panel-mount, 12-pin, nickel-plated brass body |
| **Connector (cable side)** | Mating IP67 circular plug (permanently attached to sensor bar cable) |
| **Cable** | 500mm, 4-pair individually shielded + overall braid (see I-001 for signal details) |
| **Mechanical** | Bayonet-lock coupling (quarter-turn); pull force >50N when mated |
| **Sealing** | IP67 when mated; IP67 with dust cap when unmated |
| **EMI** | Cable shield terminated to connector shell at both ends (360-degree ground) |
| **Strain relief** | Cable gland with PG9/M16 thread; PUR strain relief boot |
| **Environmental** | -40 to +85 deg C; salt fog 500h; 500 mating cycles |
| **Pin assignment** | Same as I-001 (12-pin: 4 signal, 4 ground, 4 shield drain) |

### 4.8 I-007: Enclosure <-> Target Frame

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Mechanically mount BSU processing enclosure to target frame structure |
| **Mounting pattern** | VESA MIS-D 100x100 (100mm x 100mm, 4x M6 threaded holes) |
| **Fasteners** | 4x M6 x 16mm hex-socket cap screw (SS 316) with nylon washers |
| **Quick-mount option** | 2x cam-lever clamps (over-center, spring-loaded) on VESA adapter plate |
| **Load capacity** | 20 kg static (2.5x safety factor for 7.8 kg BSU system) |
| **Vibration** | MIL-STD-810H 514.8 Cat 4 compliant (rubber isolator pads between adapter plate and frame) |
| **Alignment** | Adapter plate with 2x alignment dowels for repeatable positioning |
| **Material** | Adapter plate: Al 6061-T6, 6mm thick; cam clamps: zinc-alloy die-cast (commercial) |
| **Tool required** | Tool-less for cam-lever clamps; 5mm hex key for VESA bolts (permanent installation) |
| **Compatibility** | NATO STANAG 4569 target frame rail profile + Vietnamese wooden/steel frames via adapter |

```
I-007 MOUNTING GEOMETRY
========================

     100 mm
  |<--------->|
  +-----+-----+  ---
  | M6  |  M6 |   |
  |  O  |  O  |   | 100 mm
  |     |     |   |
  | M6  |  M6 |   |
  |  O  |  O  |   |
  +-----+-----+  ---

  4x M6 threaded inserts (Helicoil)
  in enclosure base plate (6mm Al)

  Optional: 2x cam-lever clamps on
  adapter plate for tool-less mounting
```

### 4.9 Interface Summary Diagram

```
INTERFACE CONTROL DIAGRAM -- ALL INTERFACES
=============================================

                            [TARGET FRAME]
                                 |
                            I-007 (VESA 100x100
                                  + cam clamps)
                                 |
+===============================+|+================================+
|        MODULE 1               ||         MODULE 4                |
|     SENSOR BAR                ||       ENCLOSURE                 |
|                               ||                                 |
| [M1][M2][M3][M4]             || +----+   +----+   +--------+   |
|  Daughter PCBs               || |I-003|   |I-005|  |I-006   |   |
|  Rubber boots                || |RJ45 |   |4pin |  |12pin   |   |
|  Cam clamps                  || |IP67 |   |IP67 |  |circ    |   |
|                               || +--+-+   +--+-+  |IP67    |   |
+==============+================+|    |        |     +---+----+   |
               |                 |    |        |         |        |
          I-006|                 |    |        |         |        |
        (500mm |                 |    |        |         |        |
       shielded|  ===============|====|========|=========|========|
       cable)  |  |              |    |        |                  |
               |  |  MODULE 2    |    |        |                  |
               +---->MAIN PCB    |    |        |                  |
               |  |  FPGA+MCU   <----+  I-003 |                  |
          I-001|  |  ADC+PHY    |             |                  |
               |  |             |             |                  |
               |  |      I-002  |             |                  |
               |  |        |    |  MODULE 3   |                  |
               |  |        +--->  POWER PCB  <--- I-005          |
               |  |             |  BMS+DC-DC  |                  |
               |  |             |      |      |                  |
               |  |             |  I-004      |                  |
               |  |             |      |      |                  |
               |  |             |  [BATTERY]  |                  |
               |  |             |  4S1P       |                  |
               |  ==============|=============|==================|
               |                |             |
               |           Cable 5A      Cable 5C
               |           Ethernet      DC Power
               |           (50-100m)     (5m, optional)
               |                |             |
               |           [Ethernet     [12/24V
               |            Switch]       Source]
               |                |
               |           [Control Station]
               |           [HTML5 Web App]
```

---

## 5. SYSTEMS THINKING INTEGRATION

### 5.1 Architecture as Leverage Points

The architecture defines the system's structure, which in Systems Thinking is one of the highest-leverage intervention points (Meadows Level 4-5: system structure and rules).

| Leverage Level | Architecture Decision | Feedback Loop Created | Impact |
|----------------|----------------------|----------------------|--------|
| **L4: Self-organization** | Modular 5-module structure with defined interfaces | Modules can evolve independently; sensor bar can be upgraded without changing processing | Enables technology insertion without system redesign |
| **L5: System rules** | ICD defines all interface contracts | Changes within a module are unconstrained as long as interface contract is maintained | Reduces integration risk; enables parallel development |
| **L6: Information flow** | BIT diagnostic chain covers 97% of critical functions | Failure information flows from any subsystem to operator within 20s (BIT at boot) + continuous monitoring | Operator always knows system state; no hidden failures |
| **L8: Negative feedback** | Watchdog (MCU), BMS protection, power sequencing | Each creates a balancing loop that contains failures before they cascade | System self-corrects from transient faults |
| **L9: Reduce delays** | <55 ms shot-to-display latency; <30 s boot time | Faster feedback to shooter and operator; reduces "waiting for system" frustration loop | Increases operational tempo; better training outcomes |

### 5.2 Feedback Loops in Architecture

```
REINFORCING LOOPS (R) -- Positive Feedback
===========================================

R1: ACCURACY -> TRUST -> ADOPTION
    Calibration-free algorithm (F3)
         |
         v
    Consistent ±10mm accuracy
         |
         v
    User trusts scoring results
         |
         v
    More units deployed (adoption)
         |
         v
    More data for algorithm refinement
         |
         v
    [Back to: Improved accuracy]

R2: MODULARITY -> AVAILABILITY -> TRAINING HOURS
    LRU design (5 modules, defined interfaces)
         |
         v
    Fast field repair (MTTR <30 min)
         |
         v
    High system availability (>95%)
         |
         v
    More training hours per unit
         |
         v
    Greater operational value
         |
         v
    Budget for spares/upgrades
         |
         v
    [Back to: Better LRU inventory]


BALANCING LOOPS (B) -- Negative Feedback
==========================================

B1: THERMAL -> THROTTLE -> STABLE
    FPGA/MCU power dissipation (~5W)
         |
         v
    Temperature rise in sealed enclosure
         |
         v
    TMP117 sensor detects high temp
         |
         v
    MCU reduces ADC sample rate (if >70 deg C)
         |
         v
    Power dissipation decreases
         |
         v
    Temperature stabilizes
         |
         v
    [Back to: Normal operation restored]

B2: BATTERY -> SOC -> WARNING -> ACTION
    Battery energy consumption (13W avg)
         |
         v
    State-of-charge decreases
         |
         v
    BQ27441 fuel gauge reports to MCU
         |
         v
    MCU sends warning at 10% SOC
         |
         v
    Operator connects external power or replaces battery
         |
         v
    SOC restored
         |
         v
    [Back to: Normal operation]

B3: BMS PROTECTION -> SAFE STATE
    Cell voltage approaches limit (16.8V max, 12.0V min)
         |
         v
    BQ76940 BMS detects out-of-range
         |
         v
    BMS disconnects battery (protection MOSFET)
         |
         v
    System enters safe shutdown (saves state to flash)
         |
         v
    No further damage to cells
         |
         v
    [Stable safe state until operator intervention]
```

### 5.3 Architecture Vulnerability Analysis (Archetype: Fixes That Fail)

| Potential Failure | Architecture Response | Archetype Risk | Mitigation |
|-------------------|----------------------|----------------|-----------|
| Single Ethernet cable is SPOF for data | W25Q128 flash buffers ~500K shots locally | Low: buffer may fill if disconnect is prolonged | Auto-sync when reconnected; large flash capacity |
| Single FPGA is SPOF for timing | FPGA dual-boot image (golden + application) | Low: golden image provides fallback | Automatic CRC-verified fallback; manual reflash via SWD |
| Battery is single energy source | External DC input provides redundant power | Low: external power eliminates battery dependency | Power path auto-switch (BQ25700A NVDC) |
| Sensor bar cable is single pathway for analog signals | Cable is integral to Module 1 (no field-disconnectable joint in cable run) | Low: cable failure rate very low (no moving parts) | Replace entire Module 1 (sensor bar assembly) as LRU |

---

## 6. ARCHITECTURE DECISION LOG

| Decision # | Decision | Rationale | Alternatives Considered | Principle Applied |
|-----------|----------|-----------|------------------------|-------------------|
| AD-001 | FPGA + MCU hybrid (not MCU-only) | FPGA provides deterministic <2ns timing jitter for TDOA; MCU handles non-deterministic tasks | MCU-only (Concept B, lower accuracy risk), FPGA-only (more complex) | P2: Division of Tasks |
| AD-002 | 5-module decomposition | Matches LRU field maintenance model; each module independently replaceable | Monolithic (fewer interfaces, harder to maintain), 3-module (less granularity) | P2: Division of Tasks + P8: Fault-Free |
| AD-003 | Single internal harness (per PRAD-R RC-2) | Reduces part count from 3 cables to 1 harness; cleaner routing | 3 separate internal cables (original design) | Rule 2: Simplicity |
| AD-004 | Non-coplanar sensor geometry (z=0, z=30mm) | Enables calibration-free 3D TDOA per expired patent WO1991010876A1 | Coplanar array (requires calibration) | OPR-08 (MUST requirement) |
| AD-005 | Ethernet as primary (not WiFi) | Highest reliability, lowest latency, FASIT compatible, no interference risk | WiFi primary (Concept B), dual Ethernet+WiFi (Concept C) | Rule 3: Safety, SIG-01 |
| AD-006 | Battery at enclosure base | Low center of gravity for stability; gravity-assisted retention; accessible via battery door | Battery beside PCBs (higher CG), external battery (more cables) | P4: Stability |
| AD-007 | All connectors on one face | Simplifies cable routing; single-side installation; easier IP67 sealing of fewer penetrations | Distributed connectors (shorter internal routes, but multiple seal faces) | Rule 2: Simplicity + P1: Force Flow |
| AD-008 | VESA 100x100 mounting pattern | Industry standard; compatible with commercial mounts; cam-lever adapters available | Custom mounting (lock-in), NATO STANAG rail (limited to NATO frames) | Rule 4: Economy + GEO-09 |
| AD-009 | LED window integrated into lid | Reduces part count by 1 (from PRAD-R RC-3); simpler enclosure | Separate LED window assembly (original design) | Rule 2: Simplicity |
| AD-010 | 6x M4 lid bolts (from 8) | Maintains IP67 with hexagonal bolt pattern; saves 2 parts + 30s assembly (PRAD-R RC-1) | 8x M4 (original, redundant) | Rule 2: Simplicity |

---

## 7. ARCHITECTURE VERIFICATION

### 7.1 Requirements Trace

| Requirement | Architecture Element | Satisfied? |
|-------------|---------------------|-----------|
| OPR-08: Calibration-free | Non-coplanar sensor geometry (AD-004) + FPGA timestamping + MCU TDOA algorithm | YES |
| SIG-04: ±10mm accuracy | FPGA <2ns jitter + ADS8688 16-bit ADC + 347mm sensor spacing | YES (by analysis) |
| OPR-07: IP67 | Al 6061-T6 enclosure + EPDM gaskets + IP67 connectors on all penetrations | YES |
| ENG-03: >=10h runtime | 4S1P 10Ah battery (148 Wh) at 13W average = 11.4h | YES |
| SIG-01: Ethernet 100BaseT | LAN8720A PHY + H1102NL + IP67 RJ45 (I-003) | YES |
| ASM-01: <=15 min setup | Cam-lever clamps (tool-less) + IP67 quick-connect + <30s boot | YES |
| MNT-02: BIT | 7-step BIT sequence, 97% coverage, <30s total | YES |
| QUA-02: MTTR <=30 min | 5 LRU modules with defined interfaces; battery <2 min, sensor bar <10 min | YES |
| GEO-04: <=12 kg | Total system: 7.8 kg (sensor bar 1.2 + enclosure 1.8 + PCBs 0.16 + battery 3.5 + hardware 1.14) | YES |
| CST-01: <=$500 | BOM $328 + 15% margin = $377 per lane | YES |
| PRD-01: >=60% local | 66.2% local content by value | YES |

### 7.2 Architecture Completeness Check

| Check | Status | Evidence |
|-------|--------|----------|
| All 7 functions (F1-F7) mapped to physical components | PASS | Section 1.1 table |
| All modules have defined interfaces | PASS | Section 4 (7 ICDs) |
| All interfaces have pin assignments | PASS | Sections 4.2-4.8 |
| Data flow from sensor to display fully defined | PASS | Section 3.1 |
| Latency budget within KIN-05 | PASS | <55 ms vs 500 ms MUST |
| BIT covers all critical functions | PASS | 97% coverage (Section 3.4) |
| All feedback loops identified | PASS | 2 reinforcing + 3 balancing (Section 5.2) |
| No single-point-of-failure for data loss | PASS | Ethernet + W25Q128 dual storage |
| Power redundancy defined | PASS | Battery + external DC (I-004, I-005) |
| Mechanical mounting fully specified | PASS | I-007 with VESA pattern |

---

## 8. META-LEARNING SKILL APPLIED

**Skill: Abstraction + Decomposition**

This architecture definition exercise applied two complementary cognitive skills:

### 8.1 Abstraction (Bottom-Up)
- Started from 107 individual requirements and 30+ physical components
- Abstracted into 7 functions (Phase 2), then into 5 physical modules
- Each module represents a coherent set of functions with minimal inter-module coupling
- The Interface Control Document captures ALL coupling between modules, making it explicit

### 8.2 Decomposition (Top-Down)
- Decomposed the overall BSU-V1 system into 3 architecture views:
  1. **Functional** -- What does each part do? (Section 1)
  2. **Physical** -- Where is each part located? How do they connect mechanically? (Section 2)
  3. **Information** -- How does data flow? At what rate and latency? (Section 3)
- Each view reveals different aspects of the same system
- The ICD (Section 4) ties all three views together at their intersection points

### 8.3 Key Insight
The most important architectural decision is the **module boundary placement**. By placing boundaries at I-001 (sensor-to-processing) and I-002 (processing-to-power), we create three independently-replaceable LRUs that align with the three most common field failure modes: sensor damage (Module 1), electronics failure (Module 2), and battery depletion (Module 3). This alignment between failure modes and LRU boundaries maximizes maintainability (QUA-02: MTTR <= 30 min) while minimizing the logistic footprint (fewer unique spare types).

### 8.4 Systems Thinking Reflection
The architecture IS the system's structure -- and structure determines behavior (Meadows). By defining clear module boundaries with explicit interfaces, we create a system that:
- **Self-organizes** around failures (LRU swap restores function)
- **Flows information** transparently (BIT chain makes all states visible)
- **Balances** automatically (thermal, power, protection loops)
- **Reinforces** positive outcomes (accuracy -> trust -> adoption)

This is the deepest leverage available in embodiment design: getting the architecture right determines 80% of the system's lifecycle behavior.

---

**Next Step:** [[PRAD_D_structure]] --> Design structure (detailed component layout, PCB placement, thermal paths, tolerance chains)

*PRAD-A Complete | 3 architecture views + 7 ICDs | 5 modules defined | 10 architecture decisions logged | 97% BIT coverage | <55 ms end-to-end latency | All requirements traced*
