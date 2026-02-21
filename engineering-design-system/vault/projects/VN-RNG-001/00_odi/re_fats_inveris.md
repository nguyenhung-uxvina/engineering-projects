---
project: VN-RNG-001
phase: 0
type: reverse-engineering
subject: FATS / Meggitt / InVeris Training Solutions - LOMAH System
version: 1.0
created: 2026-02-08
status: complete
---

# Reverse Engineering Report: FATS / Meggitt / InVeris Training Solutions

## 1. Executive Summary

InVeris Training Solutions (formerly FATS Inc. → Meggitt Training Systems) is the **dominant US-based integrated training solutions provider**, offering LOMAH as one component within a comprehensive live-fire and virtual training ecosystem. Unlike Saab (sensor technology specialist) or Polytronic (LOMAH inventor/pioneer), InVeris's competitive advantage lies in **ecosystem integration** — LOMAH is an accessory that deepens lock-in across their 15,500+ installed range base.

**Key Insight**: InVeris does NOT compete on LOMAH technology; they compete on total range solutions. Their LOMAH is technically comparable to Saab's but strategically positioned as a retrofit/add-on to their massive installed base of SIT/MF-SIT targets.

---

## 2. Company History & Corporate Evolution

| Year | Event |
|------|-------|
| 1926 | **Caswell International** founded — invents world's first target retrieval system |
| 1935 | Caswell invents world's first bullet trap |
| 1977 | Caswell develops first shoot/no-shoot situational training |
| 1982 | Caswell expands into US and foreign military markets |
| 1984 | **Firearms Training Systems (FATS) Inc.** established in Atlanta, GA — first interactive firearms simulation |
| 1985 | FATS produces first stand-alone firearm interacting with video scenario |
| 1989 | Caswell patents GranTrap (rubber bullet trap) |
| 1993 | FATS introduces first virtual lanes marksmanship with AAR |
| 2004 | FATS introduces BlueFire — world's first wireless weapon simulator |
| 2003 | Meggitt PLC acquires Caswell International |
| 2006 | Meggitt PLC acquires FATS (merger agreement Aug 29, 2006) |
| **2008** | **FATS + Caswell combined → Meggitt Training Systems** (HQ: Suwanee, GA) |
| 2014 | Wins US Army and USMC small-arms training contracts — **Program of Record** |
| 2019 | SIT with LOMAH showcased at AUSA; ATS III contract awards $15.8M+ |
| **2020 Jul** | **Pine Island Capital Partners acquires Meggitt Training Systems for $146M** |
| 2020 Oct | **Rebranded to InVeris Training Solutions** |
| 2021 | Debuts at IDEX/I-ITSEC with full virtual-to-live portfolio |

### Current Ownership
- **Pine Island Capital Partners** (private equity, defense-focused; includes former Sen. Saxby Chambliss)
- Headquarters: Suwanee, Georgia (235,000 sq ft facility)
- Global offices: USA, Australia, Canada, Netherlands, Singapore, UAE, UK
- ~400+ employees
- Retains FATS and Caswell legacy brands

### Scale
| Metric | Value |
|--------|-------|
| Countries served | 40+ |
| Live-fire ranges installed | 15,500+ |
| Virtual systems installed | 7,500+ |
| Infantry targets fielded | 44,000–80,000+ |
| Military bases with targets | 122+ |
| Total systems deployed | 90,000+ |

---

## 3. Product Line Overview

### 3.1 LOMAH Products

InVeris offers three LOMAH variants:

#### A. Standard LOMAH (TRCS — Target Range Control System)

Integrated into or retrofit onto SIT/MF-SIT infantry targets.

| Parameter | Specification |
|-----------|---------------|
| **Caliber** | .22 to .50 cal (NATO 5.56–12.7mm) |
| **Min projectile velocity** | 450 m/s (1,476 ft/s) at target |
| **Detection zone** | 3 x 2.5 m (10 x 8 ft), adjustable |
| **Detection rate** | 1,200 RPM maximum |
| **Accuracy** | <5mm avg radial tolerance at target center within 150mm radius circle, wind <1.5 m/s |
| **Power** | Integrated in SIT, or +12V separate, or POE |
| **Communications** | Ethernet 100BaseT; Wi-Fi option |
| **Operating temp** | -25°C to +70°C |
| **Storage temp** | -40°C to +70°C |
| **Enclosure** | IP67 |
| **Software** | RangeMaster, Visual Shot, TRACR, FASIT, RISCON-T |

#### B. Armor LOMAH

Larger detection zone for vehicle gunnery training.

| Parameter | Specification |
|-----------|---------------|
| **Caliber** | 5.56mm to 120mm |
| **Min projectile velocity** | 450 m/s at target |
| **Detection zone** | 4 x 3 m (13 x 10 ft), adjustable |
| **Detection rate** | 1,200 RPM maximum |
| **Accuracy** | <150mm in target area, wind <1.5 m/s |
| **Power** | +12V separate or POE |
| **Communications** | Ethernet 100BaseT |
| **Operating/storage temp** | Same as standard |
| **Enclosure** | IP67 |

#### C. Portable LOMAH

Standalone battery-powered field-deployable unit.

| Parameter | Specification |
|-----------|---------------|
| **Caliber** | .22 to .50 cal |
| **Communication range** | 2,000 m (Wi-Fi) |
| **Battery life** | 10 hours (standard Li-ion), larger options available |
| **Deployment** | Self-contained, any target lifter |
| **Use cases** | Field zeroing, mission rehearsal, austere locations |

### 3.2 Broader Ecosystem

LOMAH integrates within a much larger product portfolio:

**Live-Fire Targetry:**
- SIT — Stationary Infantry Target (44,000+ fielded)
- MF-SIT — Multi-Function SIT (360° rotation, friend/foe)
- SAT — Stationary Armor Target (up to 150 lbs silhouettes)
- MIT/MAT — Moving Infantry/Armor Targets
- SP-MIT — Self-Propelled Moving Infantry Target
- QuikTurn 360 — Turning target, <0.5s expose/conceal

**Range Control:**
- RangeMaster 9K — PC-based scenario programming & control
- RangeMaster 10K — Wireless tablet control, 2000m range
- XWT Lane Manager — Browser-based lane control

**Virtual Training:**
- FATS 100P/100MIL — Projection-based marksmanship/judgmental
- FATS AR — Augmented reality
- FATS VR — Virtual reality
- FATS LIVE — Hybrid live-fire-on-projected-scenarios (self-healing screen)
- BlueFire — Wireless weapon simulators with recoil

**Range Construction:**
- Turnkey range design, build, equip, maintain
- GranTrap bullet traps, LE5000 escalator traps
- Ballistic baffles, shooting stalls, ventilation

---

## 4. Technical Architecture Analysis

### 4.1 LOMAH Sensor System

**Sensing Principle**: Acoustic TDOA (same as Saab and Polytronic)
- Microphone sensor array detects supersonic shockwave
- Measures precise time of bullet's Mach cone passing over sensors
- Computes X, Y coordinate via triangulation
- Presents graphical shot location on Firing Point Computer (FPC)

**Key Design Decisions:**

| Feature | InVeris Approach | Notes |
|---------|-----------------|-------|
| Sensor type | Microphone array (modular) | Individual replacement modules |
| Mounting | Below lifter height, ballistic protection | Survives direct fire environment |
| Topology | Configurable modules | "Various topologies" — not locked to one geometry |
| Min velocity | 450 m/s (supersonic only) | Same limitation as Saab |
| Max rate | 1,200 RPM | Matches Saab; below Polytronic's 2,000 RPM |

### 4.2 Processing & Communication

| Subsystem | Technology |
|-----------|-----------|
| Processing | Embedded electronics (integrated in SIT or separate enclosure) |
| Primary comms | Ethernet 100BaseT (wired) |
| Secondary comms | Wi-Fi (optional, standard on Portable) |
| Power options | Integrated SIT power, +12V DC, Power-over-Ethernet (POE) |
| Display | Firing Point Computer (FPC) — adjustable brightness, 4X zoom, sun shield |

### 4.3 Firing Point Computer (FPC) Features

The FPC is a field-hardened display unit at the shooter's position:
- Real-time shot location display
- Target lifter control (when integrated with SIT)
- Adjustable brightness + sun shield
- 4X zoom of target view
- Shot replay (last shot)
- Sequential numbered shots
- Crossfire detection (when used with Lane Shot Initiator)
- Scoring information (hits on target)
- Group size and diameter calculation
- Integrated carry handle for portability

### 4.4 Lane Shot Initiator (LSI)

Optional accessory for multi-lane ranges:
- Differentiates between shooters on adjacent lanes
- Reports crossfire events
- Quickly added to existing LOMAH installations

### 4.5 Software Integration

InVeris LOMAH is compatible with multiple military-standard software platforms:

| Software | Description |
|----------|-------------|
| **RangeMaster** | InVeris proprietary range control & scenario management |
| **Visual Shot** | Shot display and analysis |
| **TRACR** | Training Range Automated Control & Reporting (US Army standard) |
| **FASIT** | Future Army System of Integrated Targets (US Army standard) |
| **RISCON-T** | Range Integrated System Controller - Targetry |

This multi-platform compatibility is a key differentiator — InVeris LOMAH works within existing military C2 infrastructure rather than requiring proprietary software.

---

## 5. Function Structure (Reconstructed)

### 5.1 Primary Functions

| ID | Function | Working Principle |
|----|----------|-------------------|
| F1 | Detect projectile passage | Acoustic microphone array captures shockwave |
| F2 | Compute shot location | TDOA triangulation → (X, Y) coordinate |
| F3 | Display results to shooter | FPC graphical display, real-time |
| F4 | Integrate with targetry | Embedded in SIT/MF-SIT or standalone |
| F5 | Communicate to range control | Ethernet 100BaseT / Wi-Fi |
| F6 | Discriminate lane/shooter | Lane Shot Initiator (LSI) |

### 5.2 Auxiliary Functions

| ID | Function | Working Principle |
|----|----------|-------------------|
| F_AUX.1 | Survive direct fire | Ballistic protection enclosure below lifter |
| F_AUX.2 | Operate in extreme temp | -25°C to +70°C rated components |
| F_AUX.3 | Resist weather | IP67 sealed enclosure |
| F_AUX.4 | Enable retrofit | Modular kit fits existing ranges |
| F_AUX.5 | Simplify maintenance | Individual sensor module replacement |
| F_AUX.6 | Support scoring | Group size, diameter, numbered shots |

---

## 6. Design Paradigm Analysis

### 6.1 Core Philosophy: "Ecosystem Lock-in Through Integration"

InVeris's LOMAH strategy is fundamentally different from Saab or Polytronic:

| Vendor | Strategy | LOMAH Role |
|--------|----------|------------|
| **Polytronic** | LOMAH pioneer, technology-first | Core product, technology differentiator |
| **Saab** | Defense systems integrator | Premium sensor product |
| **InVeris** | Total range solutions provider | Accessory/add-on to drive ecosystem value |

InVeris treats LOMAH as a **value multiplier** for their installed base:
- 15,500+ ranges × LOMAH retrofit = massive addressable market
- 44,000+ SITs × LOMAH upgrade = recurring revenue opportunity
- Combined with FATS virtual training = virtual-to-live training continuum

### 6.2 Strengths

1. **Largest installed base** — 15,500+ ranges, 44,000+ infantry targets
2. **Retrofit-first design** — LOMAH adds to existing ranges with minimal downtime
3. **Multi-software compatibility** — TRACR, FASIT, RISCON-T compliance
4. **Virtual-to-live continuum** — Only vendor with both FATS virtual AND LOMAH live-fire
5. **US DoD Program of Record** — Preferred vendor for US Army/USMC
6. **Turnkey capability** — Design, build, equip, maintain entire ranges
7. **Portable variant** — Battery-powered, Wi-Fi, field-deployable

### 6.3 Weaknesses

1. **LOMAH not core competency** — Acquired capability, not invented
2. **Accuracy matches competitors, doesn't exceed** — <5mm at center only within 150mm radius
3. **Supersonic only** — 450 m/s minimum (no subsonic detection like Polytronic's RADAR)
4. **Detection rate limited** — 1,200 RPM vs Polytronic's 2,000 RPM
5. **Accuracy degrades with distance from center** — Specified only within 150mm radius
6. **US-centric procurement** — Heavy reliance on US DoD programs
7. **Private equity ownership** — Potential cost-cutting pressure on R&D

---

## 7. Patent & IP Analysis

### 7.1 Published Patents

InVeris lists patents on their website. **Critically, NO LOMAH-specific patents are published:**

| Product Category | Patent | Relevance to LOMAH |
|-----------------|--------|-------------------|
| Steel bullet trap | "Apparatus and Method for Detecting a Shot Firing Event" (PENDING) | **Possibly LOMAH-related** — shot detection |
| IBOT | "Methods and Apparatus for Acquiring and Tracking a Projectile" (PENDING) | Optical tracking, NOT acoustic |
| GranTrap | US 6,027,120 — Granulate Backstop Assembly | None |
| BlueFire | US 7,306,462, US 7,291,014, US 7,197,973 | Virtual weapons, none |
| MF-SIT | US 8,047,546 — Multi-Target Clamping Assembly | Target mechanism, none |
| Coaching | US 10,012,475 — Automated Coaching of a Shooter | Software, none |

### 7.2 Freedom-to-Operate Assessment for VN-RNG-001

| Technology Area | Risk Level | Assessment |
|----------------|------------|------------|
| Acoustic TDOA triangulation | **NONE** | Published science (Knapp & Carter, 1976) |
| GCC-PHAT algorithm | **NONE** | Public domain algorithm |
| Microphone sensor array geometry | **LOW** | Standard triangulation arrays not patentable |
| Modular sensor replacement | **NONE** | Mechanical design, not novel |
| Shot detection apparatus | **LOW-MEDIUM** | Pending patent — monitor claims when published |
| FPC display concepts | **NONE** | Standard UI patterns |
| Range software integration | **NONE** | FASIT/TRACR are US Army standards (public) |
| Retrofit kit design | **NONE** | Mechanical packaging, not novel |

### 7.3 Foundational LOMAH Patents (Industry-Wide, Historical)

| Patent | Title | Filed/Granted | Assignee | Status |
|--------|-------|---------------|----------|--------|
| **US4350881A** | Projectile Position Detection Apparatus | 1980/1982 | Australasian Training Aids → LOMAH Electronic Targetry Inc. | **EXPIRED** — foundational acoustic LOMAH patent |
| **WO1997024575A1** | Projectile Location System | 1996 | International PCT | **EXPIRED** — cross-correlation triangulation method |

These foundational patents cover the core LOMAH principle (acoustic triangulation of supersonic shockwave using microphone arrays with cross-correlation for time-of-arrival). Both are **expired**, meaning the fundamental technology is in the **public domain**.

**Overall FTO Risk: LOW** — InVeris has minimal LOMAH-specific IP protection. Foundational LOMAH patents are expired. Their moat is ecosystem scale, not patents.

---

## 8. Military Contracts & Deployments

### 8.1 Key Contracts

| Contract | Value | Year | Scope |
|----------|-------|------|-------|
| US Army ATS III (IDIQ, 5-year) | >$15.8M (awarded by TACOM since May 2019) | 2019+ | Live-fire targetry systems |
| US Army ATS additional orders | $17.7M | 2018+ | Continued targetry delivery |
| US Army Program of Record | — | 2014 | Small-arms training systems |
| US Marine Corps Program of Record | — | 2014 | Small-arms training systems |
| Live-Fire Training & Target Systems | **$359.8M ceiling** | 2025 | Shared IDIQ: InVeris + Riptide + Shock Stream + Theissen |
| TRACR development | $43M | 2019 | Riptide Software Inc. (Oviedo, FL) — government-owned software |

### 8.2 Known LOMAH Installations

| Installation | Year | Details |
|-------------|------|---------|
| Fort Jackson, SC | 2000-2004 | Initial LOMAH deployment for Basic Training |
| Fort Benning (now Fort Moore), GA | 2000-2004, upgraded ~2012 | MRF with LOMAH; GAT testing site. 11/16 "hard luck cases" passed first attempt |
| Fort Knox, KY | 2000-2004 | Initial deployment |
| Fort Sill, OK | 2000-2004, new range 2025 | Second LOMAH range opening May 2025 (5+ year project) |
| Fort Leonard Wood, MO | 2000-2004, upgraded ~2012 | Automated Field Fire with LOMAH |
| Fort Eustis, VA | ~2013 | LOMAH demonstration for BG Lundy |
| Grafenwoehr, Germany | Ongoing | Largest European InVeris presence (7th Army Training Command) |

### 8.3 Deployment Scale

- **40+ countries** with equipment installed
- **15,500+ live-fire ranges** worldwide
- **250+ TRACR-equipped ranges** (US Army/USMC)
- Compatible with US Army's new marksmanship qualification program
- LOMAH training impact: **Pass rates improved from 40-45% to 86%+ in testing**

---

## 9. FASIT Standard & Government-Owned Software Model

### 9.1 FASIT (Future Army System of Integrated Targets)

The US Army's standard for live-fire training target systems, managing 659 ranges:
- **Managing org**: PEO STRI / PM TRADE / PdM TTS
- **Key document**: FASIT PD Interface Control Document (ICD)
- **Architecture**: Open modular — multiple vendors (InVeris, Theissen, Saab, Sius) must interoperate
- **Software**: Government-owned TRACR (Targetry Range Automated Control & Recording)
- **TRACR developer**: Riptide Software ($43M contract), fully SOA architecture, 250+ ranges

### 9.2 Government-Owned Software — Critical Lesson

The original LOMAH system (2000-2004) used **proprietary OEM software**. This created major problems:
- Each BRM doctrine change required costly contract modifications with OEM
- Software updates were "too costly and in some cases impossible"
- No flexibility to adapt to new weapons, sights, or ammunition

**Solution**: PM TRADE folded LOMAH into TRACR product line (government-owned):
- Army owns the source code, modifies freely
- Post-Deployment Software Support (PDSS) contract for centralized sustainment
- Eliminated vendor lock-in
- Pass rates improved from 40-45% to 86%+

**VN-RNG-001 Implication**: Design open-architecture software from day one. Avoid proprietary lock-in. Offer customer-modifiable training scenarios.

---

## 10. Comparative Analysis: InVeris vs Saab vs Polytronic

| Parameter | InVeris | Saab | Polytronic |
|-----------|---------|------|------------|
| **Accuracy (center)** | <5mm (within 150mm radius) | <5mm | ±3mm (box target) |
| **Accuracy specification** | Conditional (150mm zone, low wind) | Full scoring area | Zone-graded (A/B/C) |
| **Detection rate** | 1,200 RPM | 1,200 RPM | 2,000 RPM |
| **Min velocity** | 450 m/s (supersonic) | ~340 m/s (supersonic) | Supersonic + subsonic (RADAR) |
| **Caliber range** | .22–120mm | 5.56–12.7mm | 5.56mm–20mm |
| **Operating temp** | -25°C to +70°C | -32°C to +55°C | -30°C to +70°C |
| **IP rating** | IP67 | IP65 (typical) | IP67 |
| **Communications** | Ethernet + Wi-Fi | Ethernet + fiber | Ethernet |
| **Portable variant** | Yes (10h battery) | No standard | Yes |
| **Software platform** | RangeMaster + FASIT/TRACR | Proprietary | AROS |
| **Installed base** | 15,500+ ranges | ~1,000+ ranges | 1,000+ ranges |
| **Core competency** | Total range solutions | Defense systems | LOMAH technology |
| **LOMAH patents** | Minimal (pending) | Dual-delta array patent | 30+ patents |
| **Virtual training** | Yes (FATS AR/VR/LIVE) | Limited | No |

### 9.1 Key Competitive Dynamics

**InVeris wins when:**
- Customer wants one-stop-shop (virtual + live-fire + range construction)
- US DoD procurement (Program of Record advantage)
- Retrofit to existing InVeris ranges (captive market)
- Budget constraints favor known vendor

**InVeris loses when:**
- Pure LOMAH performance is primary evaluation criterion
- Subsonic detection required (Polytronic RADAR)
- High-RPM engagement (Polytronic 2,000 RPM)
- Customer is outside US DoD ecosystem

---

### 10.3 Additional Competitors Identified

| Company | Product | Country | Key Differentiator |
|---------|---------|---------|-------------------|
| **Theissen Training Systems (TTS)** | LOMAH | Germany/USA | Patented system eliminating extra reference measurement; FASIT ICD compliant |
| **Steinert Sensing Systems** | TrueZeroTarget | Germany | Indoor/outdoor; adjustable detection window |
| **Zen Technologies** | LOMAH Smart Electronic Target | India | Electro-mechanical, software-driven; outdoor ranges |
| **Sius AG** | Target systems | Switzerland | Primarily competition shooting targets |

---

## 11. Technology Insertion Opportunities for VN-RNG-001

### Priority 1 (Implement)

| Feature | Source | Rationale |
|---------|--------|-----------|
| **Retrofit kit design** | InVeris approach | Design LOMAH as add-on to existing targets — expands TAM |
| **Multi-power options** | InVeris (SIT/12V/POE) | Flexibility for different range infrastructure |
| **FPC shooter feedback** | InVeris FPC concept | 4X zoom, shot replay, group analysis — high training value |
| **Lane Shot Initiator** | InVeris LSI | Critical for multi-lane crossfire detection |

### Priority 2 (Consider)

| Feature | Source | Rationale |
|---------|--------|-----------|
| **FASIT/TRACR compatibility** | InVeris software | Required for US export market |
| **Portable variant** | InVeris Portable LOMAH | Field deployment use case for Vietnamese military |
| **Wi-Fi communication** | InVeris | Reduces cabling cost, enables tablet control |

### Priority 3 (Monitor)

| Feature | Source | Rationale |
|---------|--------|-----------|
| **Virtual-to-live training** | InVeris FATS LIVE | Future roadmap — hybrid training using projection screens |
| **Automated coaching** | InVeris patent US 10,012,475 | AI-driven marksmanship coaching from shot data |

---

## 12. Implications for VN-RNG-001 Design

### 11.1 Market Positioning

InVeris's weakness is VN-RNG-001's opportunity:
- InVeris is premium-priced, US-centric, ecosystem-locked
- VN-RNG-001 targets markets where InVeris ecosystem is NOT installed
- Focus on **standalone LOMAH excellence** (not ecosystem dependency)
- Target countries that cannot access US Program of Record

### 11.2 Technical Differentiation Strategy

| VN-RNG-001 Advantage | vs InVeris |
|----------------------|-----------|
| Higher detection rate target (>1,200 RPM) | Match or exceed InVeris 1,200 RPM |
| Full-area accuracy spec (not zone-limited) | InVeris specifies only 150mm center zone |
| AI-enhanced coaching (Concept B) | InVeris has pending patent but no fielded AI |
| Open software architecture | InVeris is RangeMaster-proprietary |
| Temperature compensation (real-time) | InVeris does not disclose compensation method |
| Lower cost (<50% of import) | InVeris is premium priced |

### 11.3 BOM Impact

InVeris LOMAH provides limited BOM insight (proprietary), but confirms:
- Microphone sensor array with ballistic protection
- Embedded processing electronics
- Ethernet + Wi-Fi communication
- IP67 enclosure rated -25°C to +70°C
- POE-capable power system

Estimated InVeris LOMAH unit cost (per lane):
- Standard LOMAH kit: $3,000–5,000 (component cost estimate)
- Selling price: $8,000–15,000/lane (including FPC and software)
- Portable LOMAH: $5,000–8,000 (with battery, Wi-Fi, FPC)

---

## 13. Summary Findings

### 12.1 Design Philosophy Comparison

| | Polytronic | Saab | InVeris |
|-|------------|------|---------|
| **Philosophy** | Technology pioneer | Premium defense | Ecosystem integrator |
| **LOMAH Role** | Core product | Key product | Accessory/add-on |
| **Moat** | 30+ patents, 60yr experience | Dual-delta patent, brand | 15,500 installed ranges |
| **Weakness** | Niche player | Premium cost | LOMAH not core focus |

### 12.2 Key Takeaways for VN-RNG-001

1. **InVeris has NO significant LOMAH patents** — FTO risk is minimal
2. **Their LOMAH accuracy spec is conservative** — <5mm only within 150mm center zone
3. **Detection rate (1,200 RPM) is beatable** — Polytronic already does 2,000 RPM
4. **Retrofit design philosophy is worth adopting** — expands addressable market
5. **FPC feature set is the benchmark** — zoom, replay, grouping, crossfire detection
6. **Multi-software compatibility is essential** for export markets
7. **Portable variant validates the use case** — Vietnamese military needs field deployment
8. **Virtual-to-live is future direction** — monitor but don't invest yet

---

## Cross-References

- [[re_saab_lomah.md]] — Saab Live Fire Precision Scoring RE analysis
- [[re_polytronic.md]] — Polytronic International LOMAH RE analysis
- [[odi_analysis.md]] — Phase 0 ODI customer insight analysis
- [[../00_project_brief.md]] — VN-RNG-001 project brief
