---
title: "Microflown AVISA SKYSENTRY - Comprehensive Reverse Engineering Analysis"
type: reference
category: competitive-intelligence
domain: acoustic-C-UAS
created: 2026-02-11
status: complete
classification: OPEN SOURCE INTELLIGENCE (OSINT)
---

# Microflown AVISA SKYSENTRY: Comprehensive Reverse Engineering Analysis

**Document Purpose:** Complete technical intelligence assessment of the Microflown AVISA SKYSENTRY acoustic counter-UAS system, compiled from open-source information for reverse engineering analysis.

**Date:** 2026-02-11

---

## Table of Contents

1. [Company Profile](#1-company-profile)
2. [Core Technology - Acoustic Vector Sensors](#2-core-technology---acoustic-vector-sensors-avs)
3. [SKYSENTRY Product Details](#3-skysentry-product-details)
4. [Other Microflown AVISA Products](#4-other-microflown-avisa-products)
5. [Military Deployments & Customers](#5-military-deployments--customers)
6. [Partnerships & Contracts](#6-partnerships--contracts)
7. [Competitive Landscape](#7-competitive-landscape)
8. [Academic & Scientific Basis](#8-academic--scientific-basis)
9. [Pricing Intelligence](#9-pricing-intelligence)
10. [Integration Capabilities](#10-integration-capabilities)
11. [Key Takeaways for Reverse Engineering](#11-key-takeaways-for-reverse-engineering)
12. [Sources](#12-sources)

---

## 1. Company Profile

### 1.1 Microflown AVISA B.V.

| Attribute | Detail |
|-----------|--------|
| **Legal Name** | Microflown AVISA B.V. |
| **Founded** | 2011 |
| **Headquarters** | Tivolilaan 205, 6824 BV Arnhem, The Netherlands |
| **Founder/Director** | Alex Koers (Co-founder and Director) |
| **KVK (Dutch Chamber)** | 51520109 |
| **Phone** | +31 880 010 880 |
| **Email** | avisa@microflown.com |
| **Website** | www.microflown-avisa.com |
| **Company Type** | Private SME (Small/Medium Enterprise) |
| **R&D Intensity** | ~70% of company efforts dedicated to R&D |
| **Staff** | Internationally staffed SME (estimated 15-25 employees based on sister company size) |
| **Focus** | Defense & security acoustic solutions |
| **Funding** | Raised funding over 1 round from 1 investor (per Tracxn) |
| **COVID State Aid** | Received EUR 28,383 under Dutch COVID Temporary Framework |

### 1.2 Relationship to Microflown Technologies

Microflown AVISA and Microflown Technologies are **sister companies**, both co-founded by **Alex Koers** and both headquartered in Arnhem, Netherlands. They share the same address (Tivolilaan 205, Arnhem).

| Entity | Focus | Founded |
|--------|-------|---------|
| **Microflown Technologies** | Commercial acoustic testing, automotive, aerospace | ~2001 (sensor commercialized 2003) |
| **Microflown AVISA** | Defense & security applications | 2011 |

- Microflown Technologies had ~20 FTE and EUR 1.3M turnover in 2010
- RocketReach estimates Microflown Technologies at ~$5M revenue, 17 employees
- The 2008 strategic decision to explore defense & security market preceded AVISA's 2011 founding
- Both companies leverage the same patented MEMS acoustic particle velocity sensor technology

### 1.3 UK Subsidiary

| Attribute | Detail |
|-----------|--------|
| **Name** | Microflown AVISA UK LTD |
| **Company Number** | 11896411 |
| **Registered** | 33 Colston Avenue, Bristol, BS1 4AU, UK |
| **Incorporated** | 21 March 2019 |
| **Status** | Active |
| **Classification** | Defence activities |

### 1.4 Leadership / Key Personnel

| Name | Role | Notes |
|------|------|-------|
| **Alex Koers** | Co-founder & Director | Background: McKinsey (Germany), Unilever, SCA Packaging. Broad European B2B experience |
| **Hans-Elias de Bree** | Inventor / Co-founder of Microflown Technologies | Invented the Microflown sensor at University of Twente (1994). Professor of Vehicle Acoustics at HAN University, Arnhem |
| **Michael Maassen** | Lead, Hardware Development | At AVISA since Feb 2015. Started as electrical/test engineer. Field testing integration |
| **Hugh Griffiths** | Referenced in DSEI context | (May be confused with Inzpire CEO in source) |

### 1.5 Self-Description

Microflown AVISA describes itself as **"NATO's unicorn in acoustic situational awareness"** (from their open day engineering presentation, April 2019).

---

## 2. Core Technology - Acoustic Vector Sensors (AVS)

### 2.1 What is an Acoustic Vector Sensor?

An Acoustic Vector Sensor (AVS) measures **both** the scalar sound pressure **and** the three-dimensional acoustic particle velocity vector at a single point in space. This is fundamentally different from conventional microphones, which measure only scalar sound pressure.

**Key distinction:**
- **Conventional microphone**: Measures sound **pressure** (scalar value, no directional information from a single sensor)
- **Acoustic Vector Sensor**: Measures both sound **pressure** AND **particle velocity** (vector value, inherently provides direction of arrival from a single point)

Because particle velocity is a **vector quantity**, a single AVS can determine the **direction of arrival (DOA)** of a sound source -- something that requires an **array of multiple microphones** when using conventional pressure-only sensors.

### 2.2 The Microflown Transducer - Operating Principle

The Microflown is a **MEMS (Micro-Electro-Mechanical Systems)** transducer that directly measures acoustic particle velocity. It is the **world's first and only commercially available** dedicated particle velocity sensor.

**Physical Principle - Thermal Anemometry:**

1. The sensor consists of **two parallel platinum micro-wires** (resistors), each approximately **400 times thinner than a human hair**
2. These wires are **heated to approximately 300 degrees C** by electrical current
3. When an acoustic wave passes across the two wires, it creates **asymmetrical heat transfer** -- the upstream wire cools more than the downstream wire
4. This temperature difference causes a **resistance differential** between the two wires
5. The resistance differential is measured as a voltage, which is **proportional to the acoustic particle velocity**

**Key specifications of the raw sensor:**
- Size: Approximately **5 x 5 x 5 mm** for a complete 3D AVS (3 orthogonal Microflown elements + 1 pressure microphone)
- Frequency range: **10 Hz to 10 kHz** (full audible spectrum, some sources cite up to 14 kHz)
- Directivity pattern: **Figure-of-eight** (inherent to each 1D element)
- Fabrication: Silicon wafers, clean room technology
- The particle velocity vector **points towards the acoustic source**, enabling direct DOA determination

### 2.3 How Direction and Sound Intensity Are Measured

**Direction of Arrival (DOA):**
- Three orthogonally placed Microflown sensors measure the X, Y, Z components of the particle velocity vector
- The vector sum directly indicates the direction from which sound is arriving
- This works from a **single point** -- no need for spatial separation of multiple microphones
- The company describes this as listening with an **"acoustic straw"** -- highly directional from a single compact unit

**Sound Intensity:**
- Sound intensity = sound pressure x particle velocity
- By combining the pressure microphone reading with the particle velocity vector, the full sound intensity vector is obtained
- The intensity vector points **away from** the acoustic source

**Advantages over conventional microphone arrays:**
- **Double spatial resolution** compared to conventional microphones (per Microflown claims)
- Works in the **near field** where particle velocity is much larger than sound pressure (near-field boost)
- Less affected by background noise and reflections compared to pressure microphones
- Extremely compact form factor (no baseline length required as with microphone arrays)
- Inherently broadband

### 2.4 Patent History and Intellectual Property

| Patent / Reference | Description |
|-------------------|-------------|
| **PCT/NL95/00220** | Original patent application for the Microflown device (1995) |
| **WO1999035470A1** | "Acoustic particle velocity sensor" -- International patent on improved sensor design |
| **US20140052406A1** | "Method of using microphones to measure particle velocity" (Google Patents) |
| **University of Twente** | Origin institution -- sensor invented in 1994 by Hans-Elias de Bree |

The Microflown is described consistently as **"worldwide unique and patented"** across all company literature. The patents cover the fundamental MEMS thermal anemometry approach to particle velocity measurement. The company **"manufactures unique and patented acoustic particle velocity sensors and exports them all over the world."**

### 2.5 Technology Timeline

| Year | Milestone |
|------|-----------|
| 1994 | Microflown sensor invented at University of Twente by Hans-Elias de Bree |
| 1995 | Patent application PCT/NL95/00220 filed |
| ~2001 | Industrialized product developed (de Bree, Koers) |
| 2003 | Broadband sensor element introduced; first commercial availability |
| 2004 | First applications scientifically proven; first arrays sold |
| 2005 | Rapid growth in automotive + aerospace industry |
| 2005 | De Bree appointed Professor, Vehicle Acoustics, HAN University Arnhem |
| 2006 | Monolithic 3D AVS chip incorporating all 3 velocity components + pressure on single chip |
| 2008 | Strategic decision to explore defense & security market |
| 2010 | 20 FTE company, EUR 1.3M turnover |
| 2011 | Microflown AVISA B.V. founded for defense/security focus |

### 2.6 Sensitivity Comparison

| Medium | Sensitivity Factor |
|--------|-------------------|
| Air | Baseline |
| Water (Hydroflown) | **3,200x higher** than air (due to density and specific heat differences) |

---

## 3. SKYSENTRY Product Details

### 3.1 System Overview

SKYSENTRY is Microflown AVISA's **counter-UAS firmware application** running on the CASTLE sensor post platform. It is marketed as **"the only acoustic sensor solution to provide reliable multi-platform drone detection in a single system."**

**Key Concept:** SKYSENTRY is **firmware** on the universal CASTLE hardware platform. The same CASTLE hardware can run different firmware for different missions (C-UAS, gunshot detection, counter-battery, etc.).

### 3.2 Architecture

```
SKYSENTRY SYSTEM ARCHITECTURE
==============================

                    ┌─────────────────────────┐
                    │   AVISA C2 Application   │
                    │   (or overarching C2)     │
                    └───────────┬─────────────┘
                                │ IP Network
                    ┌───────────┴─────────────┐
                    │      MANET Radio         │
                    │    Mesh Network           │
                    └───────────┬─────────────┘
                                │
           ┌────────────────────┼────────────────────┐
           │                    │                    │
    ┌──────┴──────┐     ┌──────┴──────┐     ┌──────┴──────┐
    │  CASTLE #1  │     │  CASTLE #2  │     │  CASTLE #N  │
    │ Sensor Post │     │ Sensor Post │     │ Sensor Post │
    └─────────────┘     └─────────────┘     └─────────────┘

    Each CASTLE contains:
    ┌──────────────────────────────────────────┐
    │  4x AMMS (Acoustic Multi Mission Sensor) │
    │  1x Acoustic Master (AMR) - DSP/compute  │
    │  1x Weather Station                      │
    │  2x Satellite Receivers (GPS)            │
    │  1x MANET Radio                          │
    │  1x Battery Box                          │
    │  SKYSENTRY Firmware                      │
    └──────────────────────────────────────────┘
```

### 3.3 How SKYSENTRY Works for C-UAS

1. **Hemispherical Coverage**: Each CASTLE sensor post "hears all around in a full hemispherical bubble" -- 360-degree azimuth, full upper hemisphere elevation
2. **Broadband Capture**: Captures frequencies across the entire audio spectrum
3. **Signal Processing**: SKYSENTRY firmware processes acoustic signals that vary in time and space
4. **Frequency Bin Analysis**: Divides the entire frequency spectrum into "frequency bins" and determines Direction of Arrival (DOA) for each frequency bin
5. **Source Separation**: Can separate the acoustic signature of a drone from other sound sources (critical in urban environments)
6. **Wide-band targets**: Tracks multi-copters, jet engines (broadband noise signatures)
7. **Tonal targets**: Tracks propeller aircraft, manned helicopters (tonal/harmonic signatures)
8. **Networking**: When CASTLEs are networked, SKYSENTRY firmware provides a "bubble in space and time" around the airborne threat -- improved accuracy through triangulation

### 3.4 Detection Performance

| Threat Type | Detection Range | Notes |
|-------------|----------------|-------|
| Small quadcopter (2 kg) | **250 m** | Initial test results |
| Small fixed-wing drone (2 kg) | **up to 1 km** | Initial test results |
| Small, low-noise drones | **400 m** | Per Unmanned Airspace directory |
| Manned helicopters | **up to 10 km** | Per official website |
| Propeller aircraft | Extended range | Tonal signature aids detection |
| Jet engine aircraft | Extended range | Broadband signature |

**Factors affecting range:**
- Weather conditions (wind speed, wind direction are primary factors)
- Target acoustic signature (louder = further detection)
- Background noise environment
- Number of networked sensor posts

### 3.5 Accuracy

| Configuration | Angular Accuracy | Notes |
|--------------|-----------------|-------|
| **Single CASTLE (standalone)** | ~1.5 degrees | Per MilTech Magazine 2015 |
| **Networked CASTLE array** | ~0.2 degrees | Per MilTech Magazine 2015 (for counter-battery context) |
| **Gunshot: shockwave only** | ~120 degrees | Initial warning only (ACLOGUS firmware) |
| **Gunshot: muzzle blast** | ~2 degrees, 10% range accuracy | After muzzle blast arrives (ACLOGUS firmware) |

### 3.6 Hardware Specifications (CASTLE Sensor Post)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **AMMS footprint** | 23-30 cm diameter | "Molehill shaped" per Soldier Mod interview |
| **AVS chip size** | 5 x 5 x 5 mm | Raw 3D acoustic vector sensor element |
| **AMMS components** | Directional Microflown sensors + DSP + wind cap | Per DPI profile |
| **CASTLE composition** | 4x AMMS + Acoustic Master + Weather Station + 2x GPS + MANET radio + Battery | Hardwired subarray |
| **Frequency range** | Full audible spectrum (~10 Hz - 10+ kHz) | Broadband by design |
| **Power** | Battery powered (battery box included) | Specific Wh/Ah not publicly disclosed |
| **Setup time** | < 10 minutes per sensor post | Single person can set up |
| **Environmental** | All-weather: temperature, dust, fog, rain, smoke | Day & night, no line-of-sight required |
| **Anti-jamming** | Anti-jamming and anti-spoofing GPS can be integrated upon request | Optional |
| **Connectivity** | IP-based MANET radios | Mesh networking between CASTLEs |
| **Processing** | On-board DSP in Acoustic Master | Edge processing at sensor post level |

**Vehicle-mounted variant (V-AMMS):**
- Extremely small and compact due to Microflown's unique sensor technology
- Does NOT limit 360-degree capability of RWS and EO systems
- Algorithms compensate for platform-induced noise and acoustic shadows/reflections from non-flat vehicle deck

### 3.7 Deployment Modes

| Mode | Description |
|------|-------------|
| **Fixed / Permanent** | Installed at sites for persistent surveillance (e.g., RAM-SCORE at artillery range) |
| **Mobile / Vehicle-mounted** | V-AMMS on military vehicles (recce vehicles to IFVs to tanks) |
| **Man-portable / Unattended** | Ground-based CASTLE sensor posts, setup in < 10 minutes |
| **UAV-mounted** | AMMS mounted on multicopters/UAVs for airborne ISR |
| **Perimeter** | CASTLEs used to fence a secured perimeter |
| **Area Coverage** | CASTLEs distributed to cover an area |
| **Networked / Distributed** | Multiple CASTLEs networked via MANET for enhanced performance |

### 3.8 Threat Detection Capabilities (Full AVISA Platform)

The CASTLE platform with different firmware can detect:

| Threat Category | Specific Threats |
|----------------|-----------------|
| **UAS / Drones** | Multi-copters, fixed-wing propeller UAVs, toy-shop drones to larger platforms |
| **Manned Aircraft** | Helicopters, propeller planes |
| **Small Arms Fire** | Sniper rifles, assault rifles (shockwave + muzzle blast) |
| **Indirect Fire** | Rockets, artillery, mortars (launch detection, 3D shockwave tracking) |
| **Ground Vehicles** | Heavy ground vehicles, tracked vehicles |
| **Projectiles** | Supersonic artillery rounds, rockets (3D shockwave detection) |

### 3.9 Key Design Features

1. **Firmware-defined capability**: Same CASTLE hardware, different firmware = different mission
2. **Passive sensing**: Completely passive, does not emit -- cannot be detected or jammed by RF means
3. **No line-of-sight required**: Works around corners, through foliage, in urban canyons
4. **Graceful degradation**: Distributed architecture means losing one node degrades but does not eliminate capability
5. **"Acoustic straw"**: Can listen directionally in any direction within its hemisphere simultaneously
6. **Multi-threat**: Single sensor post handles multiple threat types simultaneously

---

## 4. Other Microflown AVISA Products

All products are **firmware applications** on the same CASTLE hardware platform.

### 4.1 Product Portfolio

| Product | Acronym | Function |
|---------|---------|----------|
| **SKYSENTRY** | -- | Counter-UAS: detect, localize, track drones and aircraft |
| **ACLOGUS** | ACoustic LOcalization of GUnShots | Vehicle-based gunshot localization |
| **MSRA** | Mobile Sound Ranging Array | Counter-battery target acquisition and fire control |
| **ATILS** | Acoustic Target Impact Localization System | Localize rocket, artillery, mortar impacts |
| **ACCOPS** | ACoustic COllaborative Protection System | Collaborative vehicle formation protection against incoming fire |
| **ACOMPRIS** | ACoustic COMPound PRoteciton System | Fixed compound protection against gunshots and mortars (requires ~6 sensor posts) |
| **ACQUIT** | ACoustic QUantification of IncidenTs | Detect and localize hostile firing events, timestamped, identify weapon type and which side was firing |
| **RAM-SCORE** | -- | Training, testing, range safety for artillery |
| **V-AMMS** | Vehicle-mounted Acoustic Multi Mission Sensor | Vehicle-integrated gunshot localization |
| **VAUDEO** | -- | Acoustically cued video surveillance |

### 4.2 Counter-Battery Capability (MSRA)

- Network of vehicle-mounted CASTLEs
- Processes both Time of Arrival (TOA) and Direction of Arrival (DOA)
- Tracks 3D shockwaves from supersonic artillery rounds and rockets
- Provides trajectory information connecting point of origin to point of impact
- Can differentiate between howitzers and rockets
- Complementary to Weapon Locating Radar (WLR) -- works at close range and in poor weather

### 4.3 Hydroflown (Underwater Variant)

- MEMS-based underwater particle velocity sensor
- Expected sensitivity **3,200 times higher** in water vs air
- Novel calibration techniques developed for underwater use

---

## 5. Military Deployments & Customers

### 5.1 Known Deployments

| Country / Context | Product | Details |
|-------------------|---------|---------|
| **Netherlands** | V-AMMS | Netherlands Special Forces ground mobility vehicles, deployed to **Mali** |
| **Netherlands** | RAM-SCORE | Permanently installed at Artillery Shooting Range (ASK) 't Harde |
| **Netherlands** | Portable variant | Used at Bergen/Munster Sud training area, Germany |
| **Netherlands** | General | Dutch MoD formally commissioned Microflown AVISA for systems |
| **Denmark** | ACLOGUS | Won Danish tender for acoustic gunshot localization via partner PTD (2018). Denmark described as "foster parent country" |
| **Three European countries** | V-AMMS | Vehicle-based systems sold (Netherlands + 2 others) |
| **Asia (unnamed)** | UAV-based system | UAV-based acoustic systems sold to an Asian customer |
| **India** | Research contract | Research contracts from India referenced |
| **United States** | Research contract | Research contracts from US referenced; US Army Research Laboratory (ARL) report ARL-TR-7431 (Sep 2015) evaluating Microflown AVS |
| **Norway** | Exhibition | Camp Rena, Norwegian Army Technology Days (Aug 2023) via partner Equipnor |

### 5.2 Combat Proven Status

The V-AMMS system deployed on Netherlands Special Forces vehicles in Mali is described as making the AVS a **"combat proven technology"** (MilTech Magazine, October 2015). The systems were delivered to Mali in January (likely 2015), were in operational use for six months as part of a technology demonstrator project.

### 5.3 NATO Engagement

- NIDV (Netherlands Industry Defence) member
- Participates in NATO NAAG (Army Armament Group) meetings
- Exhibits at NATO-affiliated defense shows across Europe
- Self-described as "NATO's unicorn in acoustic situational awareness"
- Advises governmental agencies and NATO industry groups in acoustic situational awareness

---

## 6. Partnerships & Contracts

### 6.1 Distribution Partners

| Partner | Country | Role |
|---------|---------|------|
| **MSS Defence** | UK | Distributor of SKYSENTRY and V-AMMS |
| **Adams Engineering Projects Pvt Ltd** | India | Partner for Indian defense market |
| **Equipnor** | Norway | Norwegian partner for Norwegian Army |
| **PTD** | Denmark | Business partner, won Danish tender 2018 |
| **SPACELAB MX** | Mexico | Co-developed acoustic gunfire locator for armored vehicle with RWS |
| **MIL Sistemika** | Serbia | Distributor in Balkans region |

### 6.2 EU Projects

| Project | Role | Description |
|---------|------|-------------|
| **TeamAware** | WP6 Leader | EU project providing Acoustic Detection System (ADS) together with Greek partner CERTH. Designing lightweight AMMS (23 cm diameter) for multicopter mounting |

### 6.3 Defence Exhibition Presence

The company maintains an active exhibition schedule across major defense shows:
- **DSEI** (London) - Showcased in 2015 and subsequent years
- **DVD** (Defence Vehicle Dynamics, UK) - 2024
- **Future Artillery** conference
- **Armoured Vehicles Eastern Europe**
- **International Armoured Vehicles**
- **DALO Days** (Copenhagen, Denmark)
- **Norwegian Army Technology Days** (Camp Rena)
- Various Netherlands pavilion exhibitions

---

## 7. Competitive Landscape

### 7.1 Acoustic C-UAS Competitors

| System | Company | Country | Technology | Key Specs |
|--------|---------|---------|------------|-----------|
| **SKYSENTRY** | Microflown AVISA | Netherlands | Acoustic Vector Sensors (particle velocity) | 250m quadcopter, 1km fixed-wing, 10km helicopter. ~1.5 deg standalone, ~0.2 deg networked |
| **Discovair G2+** | Squarehead Technology | Norway | Microphone array (128 mics) + beamforming + camera | Passive, directional. Partnered with DroneShield. Man-portable "Sentry Post" variant. SOFWERX competition winner (with Dedrone, Echodyne, Battelle) |
| **SENTRY** | Mind Foundry | UK | AI/ML on standard acoustic sensors | "Acoustic tripwire". AI-powered classification. UK sovereign AI. Sensor fusion capabilities. SAPIENT-compatible |
| **Fencepost** | GA-EMS (General Atomics) | USA | Acoustic surveillance sensors (conventional microphone-based) | 6-sensor networked perimeter at 2017 US Army event. Detected Group 1-3 UAS at T-REX 25 (2025). Lightweight, covert |
| **BeephoniX M2** | BeephoniX | Netherlands (Eindhoven) | 151 MEMS microphones + AI + beamforming | 40 cm diameter array. Detects Class I-II drones. Based in Brainport Eindhoven |

### 7.2 Technology Comparison: AVS vs Microphone Arrays

| Feature | Microflown AVS (SKYSENTRY) | Conventional Microphone Array (Squarehead, GA-EMS) |
|---------|---------------------------|---------------------------------------------------|
| **Sensing element** | Particle velocity + pressure (vector) | Sound pressure only (scalar) |
| **DOA from single sensor** | YES -- inherent directionality | NO -- requires array + beamforming |
| **Minimum array size** | 1 sensor gives DOA | 4+ microphones minimum |
| **Form factor** | Very compact (5mm AVS chip, 23-30cm AMMS) | Larger (Discovair G2+: 128 mics, BeephoniX: 151 mics) |
| **Spatial resolution** | 2x conventional (claimed) | Baseline |
| **Near-field advantage** | Yes -- particle velocity boost | No |
| **Background noise rejection** | "Noise removed before transduction" | Post-processing beamforming |
| **Multi-threat** | Single sensor handles SAF, RAM, UAS, vehicles | Typically specialized |
| **Maturity** | Commercially available since ~2012 | Squarehead: since 2004, GA-EMS: 2017+ |
| **AI/ML** | Not prominently featured | Mind Foundry SENTRY: AI-first approach |

### 7.3 Competitive Advantages of SKYSENTRY

1. **Unique sensor physics**: Only commercial particle velocity sensor; competitors all use pressure microphones
2. **Compact form factor**: 5mm AVS chip enables miniaturization impossible with microphone arrays
3. **Multi-mission platform**: Same hardware, different firmware = C-UAS + gunshot + counter-battery + vehicle tracking
4. **Single-point DOA**: No need for spatially separated microphone array baseline
5. **Combat proven**: Deployed in Mali with Dutch Special Forces

### 7.4 Competitive Disadvantages / Limitations

1. **Detection range**: 250m for quadcopters is relatively modest (acoustic detection in general is short-range vs radar)
2. **Weather sensitivity**: Wind speed and direction significantly affect performance
3. **Small company**: SME with ~20 staff, may have scaling challenges vs GA-EMS, DroneShield
4. **Limited AI**: Does not prominently feature ML/AI classification unlike Mind Foundry SENTRY
5. **Acoustic-only**: Still requires fusion with radar/RF/EO for complete C-UAS solution

---

## 8. Academic & Scientific Basis

### 8.1 University Origins

The Microflown sensor was invented in **1994** at the **University of Twente** (Enschede, Netherlands) by **Hans-Elias de Bree** and colleagues (Peter Leussink, Twan Korthorst, Henri Jansen, Theo S.J. Lammerink, Miko Elwenspoek) in the MESA+ Institute for Nanotechnology.

### 8.2 Key Publications

| Year | Publication | Authors | Venue |
|------|-------------|---------|-------|
| 1995 | "The mu-flown: a novel device for measuring acoustic flows" | H.E. de Bree, P. Leussink, T. Korthorst, H. Jansen, T.S.J. Lammerink, M. Elwenspoek | Sensors & Actuators A, Vol. SNA054/1-3, pp. 552-557 |
| 2003 | "An Overview of Microflown Technologies" | H.E. de Bree | Acustica United with Acustica, Vol. 89, pp. 163-172 |
| 2003 | "The Microflown: An Acoustic Particle Velocity Sensor" | H.E. de Bree | Acoustics Australia, Vol. 31, No. 3 |
| 2009 | "The Microflown Particle Velocity Sensor" (Book Chapter) | F. Jacobsen, H.E. de Bree | Springer Handbook of Acoustics |
| 2009 | "The Microflown e-Book" | H.E. de Bree | Online publication |
| ~2012 | "The Acoustic Vector Sensor, a versatile battlefield acoustics sensor" | H.E. de Bree, J.W. Wind | SPIE conference (Microflown AVISA, Arnhem) |
| 2015 | ARL-TR-7431 | US Army Research Laboratory | US Army evaluation of acoustic vector sensors |
| -- | "Recent Advances in Battlefield Acoustic Sensors" | Multiple (incl. ARL) | Academic/military research |
| -- | "A Perspective on Acoustic Vector Sensors in Passive Surveillance" | -- | J. Aerospace Sciences and Technologies |

### 8.3 Key Academic Milestones

- 2005: de Bree appointed **Professor of Vehicle Acoustics** at HAN University, Arnhem School of Automotive Engineering
- Extensive publication list maintained at microflown.com/resources/publication-list
- Wikipedia article on "Particle velocity probe" cites Microflown as one of only two commercially available models

### 8.4 US Army Research Laboratory Evaluation

The **ARL-TR-7431** report (September 2015) from the US Army Research Laboratory evaluated Microflown's acoustic vector sensor technology. Key findings referenced the ability of Microflown elements to measure particle velocity in perpendicular directions, and the computation of sound intensity vectors for source localization. This represents independent US military validation of the underlying technology.

---

## 9. Pricing Intelligence

### 9.1 Direct Pricing

**No direct pricing is publicly available** for any Microflown AVISA defense products. The company operates on a defense procurement model with direct inquiry and quotation.

### 9.2 Indirect Price Indicators

| Indicator | Value | Source |
|-----------|-------|--------|
| Company turnover (2010, Microflown Technologies) | EUR 1.3M | Internoise 2012 presentation |
| Microflown Technologies revenue | ~$5M | RocketReach estimate |
| COVID state aid received | EUR 28,383 | NorthData/EU records |
| Funding | 1 round, 1 investor | Tracxn |

### 9.3 Cost Estimation Factors

For reverse engineering purposes, consider:
- MEMS sensor fabrication (silicon wafer, clean room) -- specialized but not inherently expensive at scale
- DSP/processing hardware (Acoustic Master) -- standard military-grade embedded computing
- MANET radio -- commercially available military radios
- GPS receivers (dual, with optional anti-jam/anti-spoof) -- moderate cost
- Weather station -- low cost
- Battery box -- moderate cost
- Enclosure/packaging -- moderate cost for mil-spec
- **Firmware / algorithms -- PRIMARY value and IP barrier**: The signal processing algorithms for DOA determination, source separation, and multi-threat classification represent the core intellectual property

### 9.4 Estimated Price Range

Based on comparable military acoustic systems:
- Individual AMMS unit: likely EUR 5,000-15,000
- Complete CASTLE sensor post (4 AMMS + Master + peripherals): likely EUR 50,000-150,000
- Full SKYSENTRY system (multiple CASTLEs + C2): likely EUR 200,000-1,000,000+
- **These are rough estimates only -- no public pricing confirmed**

---

## 10. Integration Capabilities

### 10.1 Command & Control

| System | Integration Status |
|--------|-------------------|
| **AVISA C2** | Microflown AVISA's own C2 application; displays real-time localization results |
| **Overarching C2** | "Hooking up with overarching systems is a rather straightforward task" (company quote) |
| **ATAK** | Referenced in SAPIENT/C2 integration literature as a target integration platform |
| **NCOP** | Referenced as integration target |
| **JChat** | Referenced as integration target |

### 10.2 SAPIENT Compatibility

**SAPIENT (Sensing for Asset Protection with Integrated Electronic Networked Technology)** is a UK Dstl-developed open standard for C-UAS sensor interoperability, now being adopted by NATO.

- SAPIENT "successfully facilitated more than 70 connections between C-UAS and C2 systems" at TIE21 (held in The Netherlands)
- NATO is adopting SAPIENT as the C-UAS interoperability standard
- While no explicit confirmation was found that SKYSENTRY is SAPIENT-compliant, the system's IP-based MANET networking and C2 integration capability makes SAPIENT integration architecturally feasible
- The company states an "interface available for integration with an overarching C2 system and other C-UAS frameworks" (per MSS Defence)

### 10.3 Networking

| Feature | Detail |
|---------|--------|
| **Inter-CASTLE networking** | IP-based MANET (Mobile Ad-hoc Network) radios |
| **Hardwired option** | Sensor posts can be hardwired "making the system entirely passive and impossible to jam" |
| **Data output** | Real-time localization results to C2 |
| **Camera cueing** | Can cue PTZ cameras to acoustic events of interest (VAUDEO capability) |
| **Sensor fusion** | Designed to complement radar, RF, EO/IR as part of layered defense |

### 10.4 Concept: Passive Acoustic Distributed Sensing (PADS)

Microflown AVISA promotes the concept of **PADS -- Passive Acoustic Distributed Sensing**, supported by MANET radios, as "an advanced contemporary approach supporting Mosaic Warfare." This positions the technology as a key enabler for distributed, resilient sensor networks in contested environments.

---

## 11. Key Takeaways for Reverse Engineering

### 11.1 Critical Technology Elements to Replicate

| Priority | Element | Difficulty | Notes |
|----------|---------|------------|-------|
| **1 - HIGHEST** | MEMS particle velocity sensor | **VERY HIGH** | Patented. Requires clean room fabrication. Two heated platinum micro-wires on silicon. Only 2 commercial sources exist worldwide |
| **2** | Signal processing algorithms (DOA, source separation) | **HIGH** | Firmware IP. Frequency bin analysis, multi-source separation in hemispherical space |
| **3** | AMMS packaging (sensor + DSP + wind cap) | **MEDIUM** | Integration engineering; wind cap critical for outdoor use |
| **4** | CASTLE architecture (4x AMMS + Master) | **MEDIUM** | System integration; Acoustic Master computing platform |
| **5** | Networking (MANET mesh) | **LOW-MEDIUM** | COTS MANET radios available |
| **6** | C2 software | **MEDIUM** | Display, tracking, alerting |

### 11.2 Alternative Approaches (Avoiding Patent)

If the patented Microflown sensor cannot be obtained or replicated:

1. **Conventional microphone array + beamforming** (Squarehead/BeephoniX approach): 128-151 MEMS microphones in a compact array. More microphones needed but avoids patent issues. Well-understood signal processing
2. **AI-enhanced acoustic classification** (Mind Foundry approach): Use standard microphones but apply ML/AI for drone signature recognition. Potentially better classification accuracy
3. **p-p probe approach**: Approximate particle velocity by measuring pressure gradient between two closely-spaced microphones (finite difference method). Less accurate but patent-free. Referenced in academic literature as alternative to Microflown
4. **Hybrid approach**: Combine a small microphone array with AI classification and networked distributed sensing

### 11.3 Key Performance Benchmarks

Any reverse-engineered system should target:

| Parameter | SKYSENTRY Benchmark | Minimum Acceptable |
|-----------|--------------------|--------------------|
| Quadcopter detection range | 250 m | 200 m |
| Fixed-wing UAV detection range | 1 km | 500 m |
| Low-noise drone detection | 400 m | 300 m |
| Helicopter detection | 10 km | 5 km |
| Angular accuracy (standalone) | 1.5 degrees | 3 degrees |
| Angular accuracy (networked) | 0.2 degrees | 1 degree |
| Setup time per sensor post | < 10 minutes | < 15 minutes |
| Coverage | Full hemisphere (360 x 180) | Full hemisphere |
| All-weather operation | Yes | Yes |
| 24/7 autonomous | Yes | Yes |

### 11.4 Vietnamese Production Considerations

For local production context:

| Component | Local Feasibility | Notes |
|-----------|-------------------|-------|
| MEMS particle velocity sensor | **NOT feasible locally** | Requires advanced MEMS fabrication. Import required |
| MEMS microphone array (alternative) | **Partially feasible** | MEMS microphones are commodity imports; array PCB can be locally produced |
| DSP / Embedded computing | **Import + local assembly** | ARM/DSP chips imported; PCB assembly local |
| MANET radios | **Import** | Military MANET radios are specialized imports |
| Mechanical packaging | **Local feasible** | CNC machining, enclosures |
| Battery system | **Local feasible** | Li-ion battery packs |
| Software / Firmware | **Local feasible** | Algorithm development, C2 software |
| GPS receivers | **Import** | Standard COTS components |
| Weather station | **Local feasible** | Temperature, wind speed, humidity sensors |

---

## 12. Sources

### Primary Sources (Microflown AVISA Official)
- [Microflown AVISA Homepage](https://www.microflown-avisa.com/)
- [SKYSENTRY Product Page](https://www.microflown-avisa.com/solutions/skysentry-1/skysentry-1-1)
- [Technology Page](https://www.microflown-avisa.com/technology)
- [About Us](https://www.microflown-avisa.com/about-us)
- [Solutions Overview](https://www.microflown-avisa.com/solutions)
- [ACLOGUS](https://www.microflown-avisa.com/solutions/vehicle-survivability/aclogus)
- [ACCOPS](https://www.microflown-avisa.com/solutions/vehicle-survivability/accops)
- [ACOMPRIS](https://www.microflown-avisa.com/solutions/others/acompris-1)
- [MSRA](https://www.microflown-avisa.com/solutions/counter-battery/msra)
- [SKYSENTRY Leaflet (Nov 2020)](https://www.microflown-avisa.com/assets/uploads/Product-Leaflets/Microflown_AVISA_Leaflet_SKYSENTRY_November_2020.pdf)

### Microflown Technologies (Sister Company)
- [Microflown Technologies Homepage](https://www.microflown.com/)
- [Particle Velocity Sensors](https://www.microflown.com/products/acoustic-particle-velocity-sensors)
- [About Microflown Technologies](https://www.microflown.com/about-us)
- [Publication List](https://www.microflown.com/resources/publication-list/publication-list-overview)
- [Open Day Engineers Presentation (2019)](https://www.microflown.com/assets/uploads/MICROFLOWNOPENDAYENGINEERS190411.pdf)

### Distribution Partners
- [MSS Defence - SKYSENTRY](https://mssdefence.com/product/microflown-avisa-skysentry/)
- [Adams Engineering - Microflown AVISA](https://www.adamsengg.com/microflown-avisa/)
- [Adams Engineering - SKYSENTRY](https://www.adamsengg.com/skysentry-2/)

### Defense Media / Analysis
- [MilTech Magazine - Microflown AVISA Creates Acoustic Awareness (Oct 2015)](http://www.miltechmag.com/2015/10/microflown-avisa-creates-acoustic.html)
- [Soldier Mod - Volume 32: Mobile Sound Ranging Array](https://www.soldiermod.com/volume-32/microflown-avisa)
- [Defence Blog - New Gunfire Locator](https://defence-blog.com/microflown-avisa-tests-new-gunfire-locator/)
- [Military Systems Tech - Dutch MoD Purchases RAM-SCORE](https://www.militarysystems-tech.com/articles/dutch-ministry-defence-purchases-first-ram-score-systems)
- [Unmanned Airspace - Microflown AVISA C-UAS](https://www.unmannedairspace.info/c-uas-search/microflown-avisa/)
- [UAS Vision - AVS on UAVs (2012)](https://www.uasvision.com/2012/01/27/microflown-avisa-mounts-acoustic-vector-sensors-on-board-unmanned-aircraft/)
- [Greatreporter - Sky Sentry Urban (2015)](https://greatreporter.com/2015/07/17/sky-sentry-acoustic-microdrone-localization-system-urban-environment/)
- [DPI Company Profile](https://www.defenceprocurementinternational.com/profile/microflown-avisa)

### Business Intelligence
- [Tracxn - Microflown AVISA](https://tracxn.com/d/companies/microflown-avisa/__D-Re10f579pyfhqI5LsShZ7ET1F-TAmWUCeq4U_FKOo)
- [Crunchbase - Microflown AVISA](https://www.crunchbase.com/organization/microflown-avisa)
- [PitchBook - Microflown AVISA](https://pitchbook.com/profiles/company/138325-96)
- [RocketReach - Microflown AVISA](https://rocketreach.co/microflown-avisa-profile_b5e40852f42e6470)
- [LinkedIn - Microflown AVISA](https://www.linkedin.com/company/microflown-avisa)
- [LinkedIn - Alex Koers](https://www.linkedin.com/in/alex-koers-3627406/)
- [UK Companies House - Microflown AVISA UK LTD](https://find-and-update.company-information.service.gov.uk/company/11896411)
- [NorthData - Microflown AVISA B.V.](https://www.northdata.com/Microflown%20AVISA%20B%C2%B7V%C2%B7,%20Arnhem/KVK%2051520109)
- [NIDV Industry Guide](https://www.nidv.eu/en/industry-guide/microflown-avisa-b-v/)
- [EPICOS](https://www.epicos.com/company/10779/microflown-avisa)
- [eTesters Catalog](https://www.etesters.com/catalog/8F3C368D-38B8-465B-8268-815EBFED2564/microflown-avisa-b-v/)
- [Bloomberg - Microflown AVISA](https://www.bloomberg.com/profile/company/0830302D:NA)

### EU Projects
- [TeamAware - Microflown AVISA](https://teamaware.eu/blogs/avisa.html)
- [SecurityDelta (Dutch)](https://securitydelta.nl/images/Microflown_Openbare_samenvatting_start_fase_2.pdf)

### Academic / Scientific
- [University of Twente - Research Publication](https://research.utwente.nl/en/publications/the-microflown-an-acoustic-particle-velocity-sensor/)
- [de Bree 2003 - Acoustics Australia Paper](https://www.acoustics.asn.au/journal/2003/2003_31_3_Bree.pdf)
- [Springer - Microflown Particle Velocity Sensor Chapter](https://link.springer.com/chapter/10.1007/978-0-387-30441-0_68)
- [ScienceDirect - Original mu-flown Paper](https://www.sciencedirect.com/science/article/abs/pii/S0924424797800131)
- [ResearchGate - AVS Battlefield Sensor](https://www.researchgate.net/publication/252406347_The_Acoustic_Vector_Sensor_a_versatile_battlefield_acoustics_sensor)
- [ResearchGate - Microflown Particle Velocity Sensor](https://www.researchgate.net/publication/226756123_The_Microflown_Particle_Velocity_Sensor)
- [JOAST - AVS Passive Surveillance Perspective](https://www.joast.org/index.php/joast/article/view/651)
- [Science.gov - Acoustic Vector Sensor Topics](https://www.science.gov/topicpages/a/acoustic+vector+sensor)
- [Wikipedia - Particle Velocity Probe](https://en.wikipedia.org/wiki/Particle_velocity_probe)
- [ARL-TR-7431 (US Army Research Lab, Sep 2015)](https://apps.dtic.mil/sti/pdfs/ADA621195.pdf)
- [Internoise 2012 - Microflown Presentation](https://www.slideshare.net/Microflown/internoise-2012-14116662)
- [Academia.edu - Hans-Elias de Bree](https://independent.academia.edu/HansEliasdeBree)

### Patents
- [WO1999035470A1 - Acoustic Particle Velocity Sensor (Google Patents)](https://patents.google.com/patent/WO1999035470A1/en)
- [US20140052406A1 - Method of Using Microphones to Measure Particle Velocity](https://patents.google.com/patent/US20140052406)

### Competitors
- [Squarehead Technology Homepage](https://www.sqhead.com/)
- [Squarehead Discovair G2+ Defense](https://www.sqhead.com/defense)
- [Squarehead Drone Detection](https://www.sqhead.com/drone-detection)
- [DroneShield + Squarehead Partnership](https://www.droneshield.com/media/press-releases/droneshield-and-squarehead-partner-in-the-c-uas-space)
- [Mind Foundry SENTRY C-UAS](https://www.mindfoundry.ai/defence/offerings/counter-uas-sentry)
- [TechUK - Mind Foundry AI Acoustic Intelligence](https://www.techuk.org/resource/ai-powered-acoustic-intelligence-the-future-of-counter-uas.html)
- [GA-EMS Fencepost at US Army Event](https://www.ga.com/general-atomics-acoustic-detection-system-successfully-performs-at-us-army-event)
- [GA-EMS Fencepost at AUSA 2025 / T-REX 25](https://www.ga.com/fencepost-sensor-tackles-low-signature-threats-in-complex-terrain)
- [BeephoniX Defense & Security](https://beephonix.com/defense-security/)
- [Brainport Eindhoven - BeephoniX](https://brainporteindhoven.com/en/in-depth/beephonix-bets-on-acoustic-intelligence-to-counter-drone-threats)

### C-UAS / SAPIENT Standards
- [UK Dstl - SAPIENT](https://www.gov.uk/guidance/sapient-autonomous-sensor-system)
- [NATO SAPIENT Adoption](https://www.janes.com/osint-insights/defence-news/defence/nato-to-adopt-sapient-as-c-uas-standard)
- [Flying Mag - NATO SAPIENT](https://www.flyingmag.com/nato-set-to-adopt-british-mod-standard-for-counter-drone-technology/)
- [SAPIENT C2 Integration Paper](https://www.sciencedirect.com/science/article/pii/S1877050922008821/pdf)
- [Counter-UAS Directory Oct 2022](https://www.unmannedairspace.info/wp-content/uploads/2023/02/Counter-UAS-directory-October-2022.v3.pdf)

### Defence Events
- [DefenceIQ - Armoured Vehicles Eastern Europe](https://www.defenceiq.com/events-armouredvehicleseasterneurope/sponsors/microflown-avisa-8)
- [DefenceIQ - Future Artillery](https://www.defenceiq.com/events-futureartillery/sponsors/microflown-avisa-2)
- [DefenceIQ - International Armoured Vehicles](https://www.defenceiq.com/events-internationalarmouredvehicles/sponsors/microflown-avisa)
- [Microflown AVISA - DVD 2024](https://www.microflown-avisa.com/news-and-events/defence-vehicle-dynamics-dvd-2024)

---

*End of document. All information sourced from publicly available open-source materials.*
