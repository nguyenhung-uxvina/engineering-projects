---
project: VN-CUAS-001
phase: 1
type: standards_mapping
version: 1.0
created: 2026-02-11
status: draft
---

# Standards Mapping — Counter-UAS Passive Acoustic Detection
## VN-CUAS-001 Phase 1 Deliverable

> **Purpose:** Map all applicable military, international, and Vietnamese standards to VN-CUAS-001 requirements. Defines specific test methods, procedures, severities, and pass criteria for qualification.
>
> **Cross-reference:** [[requirements_list.md]] for detailed requirement definitions.
>
> **Classification:** UNCLASSIFIED

---

## 1. STANDARDS OVERVIEW

### 1.1 Applicable Standards Summary

| # | Standard | Title | Scope | Priority |
|---|----------|-------|-------|----------|
| 1 | **MIL-STD-810H** | Environmental Engineering Considerations | Environmental qualification (16 methods) | Critical |
| 2 | **MIL-STD-461G** | EMI/EMC Requirements | Electromagnetic compatibility (8 requirements) | Critical |
| 3 | **MIL-STD-882E** | System Safety | Hazard analysis and risk management | Critical |
| 4 | **MIL-HDBK-217F** | Reliability Prediction | MTBF calculation methodology | Important |
| 5 | **IEC 60529 (IP67)** | Ingress Protection | Dust and water protection | Critical |
| 6 | **UN 38.3** | Lithium Battery Transport | Battery safety for transport/logistics | Critical |
| 7 | **NATO STANAGs** | Interoperability Standards | C2 integration, track formats, IFF | Important |
| 8 | **TCVN** | Vietnamese National Standards | Local regulatory compliance | Important |
| 9 | **SW/Cyber Standards** | Software and Cybersecurity | Safety-critical SW, OTA security | Important |

### 1.2 Compliance Priority Matrix

| Priority | Definition | Standards |
|----------|-----------|-----------|
| **Critical** | Must comply for market entry; non-negotiable for Vietnamese military acceptance | MIL-STD-810H, MIL-STD-461G, MIL-STD-882E, IP67, UN 38.3 |
| **Important** | Required for credibility and interoperability; may use tailored compliance | MIL-HDBK-217F, NATO STANAGs, TCVN, SW/Cyber |
| **Optional** | Best practice; enhances product competitiveness | Additional NATO STANAGs, IEC 62443 advanced levels |

---

## 2. MIL-STD-810H — ENVIRONMENTAL ENGINEERING (PRIMARY)

### 2.1 Applicability Statement

MIL-STD-810H is the primary environmental qualification standard for VN-CUAS-001. The system must survive and operate in Vietnamese tropical conditions (northern highland, central coast, southern delta, and offshore maritime environments). The operational profile includes:

- **Ground Fixed (GF):** Static deployment at FOBs, checkpoints, border posts
- **Ground Mobile (GM):** Vehicle-transported, dismounted operation
- **Climate:** Tropical hot-humid (A2), tropical hot-dry (A1), highland (C1)
- **Lifecycle:** Storage, transport, field deployment, 24h+ continuous operation

### 2.2 Test Method Mapping

#### Method 500.6 — Low Pressure (Altitude)

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Storage/Transit) and Procedure II (Operation) |
| **Test Severity** | Altitude: 3,048 m (10,000 ft) — covers 0-3000 m operating requirement |
| **Duration** | Procedure I: 1 hour at altitude; Procedure II: 2 hours operational at altitude |
| **Temperature** | Combined with Method 501.7 high temp at reduced pressure |
| **Pass Criteria** | Full acoustic detection performance at altitude; no enclosure deformation; battery operation unaffected; all seals maintain integrity |
| **Applicable Requirements** | [[requirements_list.md#OPR-001]] (Operating altitude), [[requirements_list.md#OPR-003]] (Environmental range) |
| **Priority** | Important — highland border deployment (Sa Pa, Lao Cai at 1,500-3,000 m) |
| **VN-CUAS Notes** | Reduced air pressure affects acoustic propagation (lower air density = reduced sound pressure level). Must verify detection range is maintained at 3,000 m. Atmospheric absorption coefficient changes at altitude — recalibrate acoustic models. Battery capacity degrades ~2% per 1,000 m due to cooling effects on lithium cells. |

#### Method 501.7 — High Temperature

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Storage) and Procedure II (Operation) |
| **Test Severity** | Storage: +70C (Hot-Dry A1, per Table 501.7-I); Operation: +55C (Hot-Humid A2) |
| **Duration** | Procedure I: 7 cycles of 24 hours; Procedure II: 3 cycles of 24 hours operational |
| **Humidity** | Dry heat for Procedure I; combined with 507.6 for humid operation |
| **Pass Criteria** | Full detection performance at +55C; no material degradation; processor thermal throttling must not reduce classification accuracy below 80%; battery charge/discharge within spec; enclosure no permanent deformation |
| **Applicable Requirements** | [[requirements_list.md#OPR-002]] (Temperature range), [[requirements_list.md#MAT-001]] (Material thermal stability), [[requirements_list.md#ENR-001]] (Power at temperature extremes) |
| **Priority** | Critical — Vietnamese southern regions regularly exceed +40C; direct sun exposure on black enclosure can reach +70C |
| **VN-CUAS Notes** | MEMS microphone sensitivity drifts ~0.01 dB/C — at +55C this is ~0.5 dB from 25C baseline. Must compensate in DSP. Edge AI processor (Cortex-A/M class) thermal throttle point is typically 85-105C junction — must verify thermal design keeps junction below limit at +55C ambient. Lithium battery capacity loss ~20% at +55C; accelerated aging reduces cycle life. Acoustic window material must not soften or deform. |

#### Method 502.7 — Low Temperature

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Storage) and Procedure II (Operation) |
| **Test Severity** | Storage: -40C (Basic Cold C1); Operation: -10C (Mild Cold C2) |
| **Duration** | Procedure I: 4 hours at -40C (storage); Procedure II: 4 hours operational at -10C |
| **Pass Criteria** | Full detection performance at -10C; battery provides ≥80% of rated capacity; LCD/display readable; all mechanical latches and connectors operable with gloved hands; no cracking of seals or enclosure |
| **Applicable Requirements** | [[requirements_list.md#OPR-002]] (Temperature range), [[requirements_list.md#MAT-002]] (Low-temp material properties), [[requirements_list.md#ENR-002]] (Battery cold performance) |
| **Priority** | Important — Northern highlands (Ha Giang, Lao Cai) winter temperatures reach -5 to 0C; -10C provides margin |
| **VN-CUAS Notes** | Lithium-ion capacity drops 30-40% at -10C. Consider LiFePO4 chemistry or battery heater for cold deployments. MEMS microphone sensitivity shift at -10C is small (<0.3 dB) but verify. Rubber seals (EPDM, silicone) must remain elastic at -10C — avoid nitrile. Condensation risk when bringing cold unit into warm humid air — desiccant or conformal coating required. |

#### Method 503.7 — Temperature Shock

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Constant Extreme Temperature) |
| **Test Severity** | -10C to +55C transfer (operational range); 5-minute transfer time |
| **Cycles** | 3 cycles minimum |
| **Pass Criteria** | No cracking, delamination, or seal failure; full functionality after cycling; solder joints intact (visual + electrical); acoustic calibration within ±1 dB of baseline |
| **Applicable Requirements** | [[requirements_list.md#OPR-002]] (Temperature range), [[requirements_list.md#MAT-003]] (Thermal shock resistance) |
| **Priority** | Important — Simulates rapid temperature changes during helicopter transport or moving from air-conditioned storage to tropical field |
| **VN-CUAS Notes** | PCB CTE mismatch between FR4 and BGA packages is primary failure mode. 128-256 MEMS microphones represent 128-256 solder joints at risk — must use appropriate solder paste and pad design. Acoustic window bonding adhesive must accommodate differential thermal expansion. |

#### Method 504.2 — Contamination by Fluids

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (System Level) |
| **Test Severity** | JP-8 fuel, hydraulic fluid (MIL-PRF-83282), lubricating oil, insect repellent, cleaning solvents |
| **Duration** | 24-hour exposure per fluid |
| **Pass Criteria** | No material degradation; enclosure paint/finish intact; seals not swollen or degraded; labels legible; no functional degradation after cleaning |
| **Applicable Requirements** | [[requirements_list.md#MAT-004]] (Chemical resistance), [[requirements_list.md#OPR-005]] (Field contamination resistance) |
| **Priority** | Important — FOB deployment near fuel/vehicle maintenance areas |
| **VN-CUAS Notes** | Enclosure material selection critical: polycarbonate resists most fluids but is attacked by some solvents; aluminum with anodize is broadly resistant. Acoustic window must resist JP-8 — PTFE or silicone mesh preferred over polyurethane foam. |

#### Method 505.7 — Solar Radiation (Actinic)

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Cycling) |
| **Test Severity** | 1120 W/m2 (standard); 56 cycles of 24 hours (equivalent to ~2 years tropical exposure) |
| **Duration** | 56 days continuous |
| **Pass Criteria** | No material degradation (chalking, cracking, discoloration); UV-stabilized components intact; enclosure structural integrity maintained; no functional degradation |
| **Applicable Requirements** | [[requirements_list.md#MAT-005]] (UV resistance), [[requirements_list.md#OPR-006]] (Outdoor deployment life) |
| **Priority** | Important — Continuous outdoor deployment in Vietnamese tropical sun |
| **VN-CUAS Notes** | Polycarbonate yellows under UV without stabilizer — use UV-stabilized grades or add UV coating. Consider RAL 6031 (Bronze Green F9) or RAL 7013 (Brown Grey) paint per NATO STANAG 2338 for camouflage. Wind/acoustic screen material must be UV-resistant — avoid untreated polyurethane foam (degrades in 6-12 months tropical sun). |

#### Method 506.6 — Rain

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Rain and Blowing Rain) and Procedure III (Drip) |
| **Test Severity** | Procedure I: 100 mm/hr, 18 m/s wind, 40 minutes per face; Procedure III: drip rate per table |
| **Duration** | Procedure I: 30-minute rain then immediate function; Procedure III: 15 minutes |
| **Pass Criteria** | Full acoustic detection during rain (with rain-noise rejection algorithm active); no water ingress into electronics; connectors sealed; post-test inspection shows no internal water |
| **Applicable Requirements** | [[requirements_list.md#OPR-007]] (Rain operation), [[requirements_list.md#QUA-003]] (Detection in rain), [[requirements_list.md#MAT-006]] (Water resistance) |
| **Priority** | Critical — Vietnam monsoon season (May-November) produces sustained heavy rainfall; system must detect drones during rain |
| **VN-CUAS Notes** | Rain noise is the primary acoustic challenge. Rain on hard surfaces generates broadband noise 40-80 dB SPL that can mask drone signatures. Mitigation: (1) rain-noise spectral subtraction algorithm; (2) acoustic window design that minimizes rain impact noise; (3) multi-node fusion to exploit spatial diversity (some nodes may be sheltered). Rain operation acceptance threshold: Pd ≥70% at 200 m in moderate rain (25 mm/hr), degraded from ≥90% in clear conditions. |

#### Method 507.6 — Humidity

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure II (Aggravated Cycling) |
| **Test Severity** | 95% RH, +60C, 10 cycles of 24 hours |
| **Duration** | 10 days |
| **Pass Criteria** | No corrosion on PCBs or connectors; conformal coating intact; MEMS microphones functional (sensitivity within ±2 dB); no condensation-induced short circuits; fungus-resistant materials show no growth |
| **Applicable Requirements** | [[requirements_list.md#OPR-008]] (Humidity tolerance), [[requirements_list.md#MAT-007]] (Corrosion resistance), [[requirements_list.md#QUA-001]] (MTBF in tropical conditions) |
| **Priority** | Critical — Vietnamese baseline environment is tropical humid; 95% RH is normal during monsoon |
| **VN-CUAS Notes** | Humidity is the single most important environmental factor for VN-CUAS reliability. MEMS microphones can absorb moisture and shift sensitivity — select hermetically-sealed MEMS (e.g., Knowles SPH0645LM4H has a moisture-resistant port). PCBs require conformal coating (acrylic or silicone) on all surfaces. Connector contacts: gold-plated minimum. Internal desiccant recommended with humidity indicator. Battery contacts must be corrosion-resistant (nickel or gold plating). |

#### Method 508.7 — Fungus

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Material Analysis) preferred; Procedure II (Test) if non-fungus-resistant materials used |
| **Test Severity** | 28 days at 30C, 95% RH, with fungal spore inoculation (Aspergillus, Penicillium, Chaetomium, etc.) |
| **Duration** | 28 days |
| **Pass Criteria** | No fungal growth on functional surfaces; acoustic window not degraded; no performance loss from fungal contamination |
| **Applicable Requirements** | [[requirements_list.md#MAT-008]] (Fungus resistance), [[requirements_list.md#OPR-008]] (Tropical environment) |
| **Priority** | Important — Tropical jungle deployments; equipment stored in non-climate-controlled facilities |
| **VN-CUAS Notes** | Acoustic window/windscreen is the highest-risk component — open-cell foam is an excellent fungal substrate. Use closed-cell PTFE or metal mesh acoustic window. Avoid organic materials (natural rubber, cellulose, untreated cotton) in all external components. PCB conformal coating must be fungus-resistant (silicone-based preferred). Packaging materials for storage must be fungus-resistant. |

#### Method 509.7 — Salt Fog

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Metallic/Treated Materials) |
| **Test Severity** | 5% NaCl solution, 35C, 48-hour exposure followed by 48-hour drying; 2 cycles |
| **Duration** | 8 days total (2 x 96-hour cycles) |
| **Pass Criteria** | No corrosion on structural components; electrical contacts functional; enclosure fasteners not seized; acoustic window not degraded; full functionality after cleaning |
| **Applicable Requirements** | [[requirements_list.md#MAT-009]] (Salt corrosion resistance), [[requirements_list.md#OPR-009]] (Maritime/coastal operation) |
| **Priority** | Important — Vietnamese coastline is 3,444 km; maritime patrol and coastal defense are key deployment scenarios |
| **VN-CUAS Notes** | Aluminum enclosure requires hard anodize (Type III, 50 um minimum) or powder coat over chromate conversion. Stainless steel fasteners (A4/316 grade) mandatory for external hardware. Dissimilar metal joints require isolation (nylon washers, anti-seize compound). MEMS microphone port protection critical — salt crystallization in acoustic port can permanently block or damage the diaphragm. Consider a replaceable acoustic filter/membrane over MEMS ports. |

#### Method 510.7 — Sand and Dust

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Blowing Dust) and Procedure II (Blowing Sand) |
| **Test Severity** | Procedure I: <149 um particles, 1.5 m/s, 6 hours; Procedure II: 150-850 um particles, 18 m/s, 90 minutes |
| **Duration** | Procedure I: 6 hours; Procedure II: 90 minutes |
| **Pass Criteria** | No dust ingress into sealed electronics (IP6X verified); acoustic window not clogged; detection performance maintained after dust exposure; mechanical functions (latches, connectors) operable |
| **Applicable Requirements** | [[requirements_list.md#MAT-010]] (Dust resistance), [[requirements_list.md#OPR-010]] (Dusty environment operation) |
| **Priority** | Important — Central Vietnam (sandy soil), construction sites near FOBs, vehicle-convoy operations |
| **VN-CUAS Notes** | IP67 enclosure satisfies IP6X (dust-tight) requirement. Acoustic window is the vulnerability — must pass sound while blocking dust. Multi-layer design: outer metal mesh (>500 um particles) + inner hydrophobic fabric (>50 um) + optional PTFE membrane. Field-replaceable acoustic window recommended for dusty environments. |

#### Method 512.6 — Immersion

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Immersion per IP67) |
| **Test Severity** | 1 meter depth, 30 minutes |
| **Duration** | 30 minutes |
| **Pass Criteria** | No water ingress; full functionality after immersion; all seals intact; connectors dry internally |
| **Applicable Requirements** | [[requirements_list.md#MAT-006]] (Water resistance), [[requirements_list.md#OPR-011]] (Submersion survival) |
| **Priority** | Critical — Monsoon flooding, river crossings, accidental drops into water during deployment |
| **VN-CUAS Notes** | This directly supports the IP67 rating. Enclosure sealing: O-ring (EPDM or silicone) on all joints; IP68-rated connectors (MIL-DTL-38999 or equivalent); cable glands with double compression. Acoustic window is the critical challenge — must pass sound while being waterproof. Proven approach: hydrophobic PTFE membrane (Gore-Tex type) with 0.2 um pore size allows acoustic transmission while blocking water. Breathing vent with PTFE membrane for pressure equalization during immersion. |

#### Method 514.8 — Vibration

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (General Vibration: Category 4, Truck Transport) and Procedure II (Secured Cargo) |
| **Test Severity** | Category 4 (Truck — Common Carrier): composite wheeled vehicle profile per Annex C, Table 514.8C-I. Frequency range: 5-500 Hz. Duration: 60 minutes per axis (3 axes). |
| **Duration** | 3 hours total (60 min x 3 axes) for transport; 1 hour per axis for operational |
| **Pass Criteria** | No structural failure; all solder joints intact (128-256 MEMS mics); connectors tight; acoustic calibration within ±1 dB post-vibration; PCB no cracked traces; battery secure in mount |
| **Applicable Requirements** | [[requirements_list.md#FOR-001]] (Vibration resistance), [[requirements_list.md#TRN-001]] (Transport survivability) |
| **Priority** | Critical — System will be truck-transported over rough Vietnamese roads; vehicle-mounted operation possible |
| **VN-CUAS Notes** | The 128-256 MEMS microphone solder joints are the primary vibration concern. Use underfill on BGA packages; design PCB with strain relief. Battery must be mechanically secured against vibration-induced disconnection. All connectors must be locking type (bayonet, threaded, or push-pull with positive retention). Consider vibration isolators for the processor/DSP module to protect sensitive electronics. Vehicle-mounted operation adds operational vibration — reserve Method 514.8 Category 7 (Assembled Aircraft, Jet) profile for future vehicle-mount variant. |

#### Method 516.8 — Shock (Mechanical)

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Functional Shock) and Procedure IV (Transit Drop) |
| **Test Severity** | Procedure I: 40g, 11 ms half-sine, 3 shocks per axis per direction (18 total). Procedure IV: 122 cm free-fall onto 50 mm plywood over steel (per transit case weight). |
| **Duration** | 18 shocks (functional); 26 drops (transit per MIL-STD-810H Table 516.8-II) |
| **Pass Criteria** | Functional shock: full operation immediately after each shock; transit drop: functional after complete drop sequence; no cracked PCBs; battery mount secure; enclosure no cracks or permanent deformation |
| **Applicable Requirements** | [[requirements_list.md#FOR-002]] (Shock resistance), [[requirements_list.md#TRN-002]] (Drop survivability) |
| **Priority** | Critical — Field handling by soldiers; helicopter sling-load; truck transport on unimproved roads |
| **VN-CUAS Notes** | 40g functional shock is moderate — standard for ground-mobile electronics. Transit drop from 122 cm simulates rough handling during logistics. MEMS microphone die are fragile — PCB mounting must distribute shock loads. Battery must not disconnect under shock (locking connector or welded tabs). Consider internal shock mount for HDD/SSD if data logging is internal (or use flash storage which is inherently shock-resistant). |

#### Method 519.8 — Gunfire Shock

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure III (Functional — Exposed to Nearby Weapon Fire) |
| **Test Severity** | Per MIL-STD-810H Table 519.8-I: depends on weapon type and distance. For VN-CUAS co-located with small arms/light weapons: 12.7 mm HMG at 5 m distance — approximately 200g, 0.5 ms duration. |
| **Duration** | 10 rounds per weapon type, per axis (3 axes) |
| **Pass Criteria** | System continues detection operation during and after gunfire; no false alarms triggered by gunfire acoustic signature (or correct classification as gunfire if gunshot-localization firmware active); no structural damage |
| **Applicable Requirements** | [[requirements_list.md#FOR-003]] (Gunfire shock resistance), [[requirements_list.md#OPR-012]] (Co-located weapons operation) |
| **Priority** | Optional — Only required if VN-CUAS will be co-located with active weapon systems. May defer to Phase 2 variant. |
| **VN-CUAS Notes** | Gunfire shock is extremely severe (200g+). If VN-CUAS is deployed at weapons positions, internal shock isolation is mandatory. Alternative: define minimum standoff distance (e.g., 10 m from 12.7 mm weapon) to reduce shock requirement. Acoustic processing must distinguish gunfire from drone signatures — this is a feature opportunity (gunshot localization mission). Phase 1 decision needed: is gunfire shock a MUST or WISH requirement? |

#### Method 521.4 — Icing/Freezing Rain

| Parameter | Value |
|-----------|-------|
| **Procedure** | Procedure I (Icing on Static Equipment) |
| **Test Severity** | -10C, freezing rain (0.5 mm ice layer), 4 hours |
| **Duration** | 4 hours exposure + 2 hours operational at -10C |
| **Pass Criteria** | Acoustic window not blocked by ice; system operational after ice thaws (may accept degraded detection during icing); mechanical functions operable after de-icing; no structural damage from ice loading |
| **Applicable Requirements** | [[requirements_list.md#OPR-013]] (Icing conditions), [[requirements_list.md#MAT-011]] (Ice resistance) |
| **Priority** | Optional — Northern highland winter only (Ha Giang, Lao Cai); not typical for most Vietnamese deployments |
| **VN-CUAS Notes** | Ice on acoustic window will severely degrade detection performance. Accepted approach: system detects icing condition (temperature + humidity sensors) and alerts operator; degraded operation accepted during icing. If anti-icing is required, a small heater element (2-5W) in the acoustic window surround could prevent ice formation — adds power consumption and complexity. Defer detailed design to Phase 3 if requirement confirmed. |

### 2.3 MIL-STD-810H Test Program Summary

| Method | Test | Priority | Duration | Est. Cost (USD) | Phase |
|--------|------|----------|----------|-----------------|-------|
| 500.6 | Low Pressure | Important | 1 day | $2,000 | Qual |
| 501.7 | High Temperature | Critical | 10 days | $5,000 | Qual |
| 502.7 | Low Temperature | Important | 2 days | $3,000 | Qual |
| 503.7 | Temperature Shock | Important | 2 days | $3,000 | Qual |
| 504.2 | Contamination | Important | 7 days | $4,000 | Qual |
| 505.7 | Solar Radiation | Important | 56 days | $8,000 | Qual |
| 506.6 | Rain | Critical | 2 days | $3,000 | DV |
| 507.6 | Humidity | Critical | 10 days | $5,000 | Qual |
| 508.7 | Fungus | Important | 28 days | $4,000 | Qual |
| 509.7 | Salt Fog | Important | 8 days | $4,000 | Qual |
| 510.7 | Sand and Dust | Important | 2 days | $3,000 | Qual |
| 512.6 | Immersion | Critical | 1 day | $1,500 | DV |
| 514.8 | Vibration | Critical | 1 day | $5,000 | DV |
| 516.8 | Shock | Critical | 2 days | $4,000 | DV |
| 519.8 | Gunfire Shock | Optional | 1 day | $6,000 | Qual |
| 521.4 | Icing | Optional | 1 day | $3,000 | Qual |
| | **TOTAL** | | **~134 days** | **~$63,500** | |

> **DV** = Design Verification (Phase 3, prototype); **Qual** = Qualification (Phase 4, production representative)

---

## 3. MIL-STD-461G — EMC/EMI

### 3.1 Applicability Statement

VN-CUAS-001 is a **passive acoustic sensor** with embedded digital processing and a radio transceiver. EMC is uniquely critical for this system because:

1. **Self-interference:** DSP/processor clock harmonics and switching power supply noise can couple into the acoustic front-end, creating false signatures or masking real targets
2. **Radio-acoustic isolation:** The mesh radio module transmits at 0.1-1W; during transmit periods, RF energy can couple into the analog signal chain of the microphone array
3. **EMCON mode:** Operational requirement for zero RF emissions during electromagnetic silence conditions — the system must be verifiably quiet
4. **Co-location immunity:** VN-CUAS will be deployed near military radios (VHF/UHF 30-400 MHz), radars, jammers, and other high-power emitters

### 3.2 Equipment Class

Per MIL-STD-461G Table II:
- **Equipment class:** Ground, Army — Ground Benign (installed in permanent facility) and Ground Mobile (field deployed)
- **Applicable requirements:** Per Table III, Ground Army — all CE/CS/RE/RS requirements apply

### 3.3 Requirement Mapping

#### CE101 — Conducted Emissions, Power Leads, Low Frequency (30 Hz - 10 kHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | Power input leads of each subsystem (processor unit, radio module, sensor array power distribution) |
| **Frequency Range** | 30 Hz - 10 kHz |
| **Limit** | Per Figure CE101-1 (Ground, Army): 106 dBuA at 30 Hz, decreasing to 60 dBuA at 10 kHz |
| **Test Method** | Current probe on power leads; spectrum analyzer |
| **Applicable Requirements** | [[requirements_list.md#SIG-001]] (EMC compliance), [[requirements_list.md#ENR-003]] (Power quality) |
| **Priority** | Critical |
| **VN-CUAS Notes** | Primary concern: switching power supply (battery to 3.3V/1.8V/5V rails) conducted emissions. Use multi-stage LC filtering on all power outputs. Battery-powered operation simplifies compliance (no AC power line concerns) but DC-DC converter switching frequencies (typically 500 kHz - 2 MHz) and their harmonics must be filtered. |

#### CE102 — Conducted Emissions, Power Leads, High Frequency (10 kHz - 10 MHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | All power leads exceeding 2 m total length |
| **Frequency Range** | 10 kHz - 10 MHz |
| **Limit** | Per Figure CE102-1 (Ground, Army): ~60 dBuV at 10 kHz, decreasing to ~36 dBuV at 10 MHz |
| **Test Method** | LISN (Line Impedance Stabilization Network) on power leads; spectrum analyzer |
| **Applicable Requirements** | [[requirements_list.md#SIG-001]] (EMC compliance) |
| **Priority** | Critical |
| **VN-CUAS Notes** | DC-DC converter harmonics are the primary emission source. Multi-node systems with power cables between nodes must comply. If each node is self-powered (internal battery), inter-node cables carry only data — simplifies CE102. Recommend: each node fully self-contained with internal battery to minimize conducted emission paths. |

#### CS101 — Conducted Susceptibility, Power Leads (30 Hz - 150 kHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | All power input leads |
| **Frequency Range** | 30 Hz - 150 kHz |
| **Test Level** | Per Figure CS101-1: 6 Vrms from 30 Hz to 150 kHz (Ground, Army) |
| **Test Method** | Inject sine wave on power leads via coupling transformer; monitor performance |
| **Pass Criteria** | No degradation of acoustic detection performance; no false alarms; no processor reset; battery charging circuit unaffected |
| **Applicable Requirements** | [[requirements_list.md#SIG-002]] (EMI immunity), [[requirements_list.md#ENR-003]] (Power quality) |
| **Priority** | Important |
| **VN-CUAS Notes** | Power bus noise from co-located equipment (generators, vehicle electrical systems) can propagate to VN-CUAS power input when externally powered. Battery operation provides inherent isolation — but external charging port must be protected. Input power filter with common-mode choke recommended. |

#### CS114 — Conducted Susceptibility, Bulk Cable Injection (10 kHz - 200 MHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | All cables (power, signal, antenna) exceeding 2 m |
| **Frequency Range** | 10 kHz - 200 MHz |
| **Test Level** | Per Figure CS114-1 (Ground, Army): frequency-dependent, ~30 dBuA at 10 kHz to ~54 dBuA at 200 MHz |
| **Test Method** | Bulk current injection (BCI) probe on each cable; swept frequency |
| **Pass Criteria** | No false alarms; no data corruption on mesh network; no processor lockup |
| **Applicable Requirements** | [[requirements_list.md#SIG-002]] (EMI immunity), [[requirements_list.md#SIG-003]] (Cable immunity) |
| **Priority** | Important |
| **VN-CUAS Notes** | Most critical for the mesh radio antenna cable and any external sensor cables. Minimize cable count and length — self-contained node architecture reduces cable susceptibility. If external microphone array cable is used (sensor head separated from processor), shielded cable with ferrite chokes at both ends is required. |

#### RE101 — Radiated Emissions, Magnetic Field (30 Hz - 100 kHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | All equipment with power conversion or high-current switching |
| **Frequency Range** | 30 Hz - 100 kHz |
| **Limit** | Per Figure RE101-1: frequency-dependent, ~180 dBpT at 30 Hz decreasing to ~100 dBpT at 100 kHz |
| **Test Method** | Magnetic field loop antenna at 7 cm from equipment face |
| **Applicable Requirements** | [[requirements_list.md#SIG-001]] (EMC compliance) |
| **Priority** | Important |
| **VN-CUAS Notes** | Switching power supply magnetics (inductors, transformers) are the primary source. Use shielded inductors in DC-DC converters. Magnetic emissions are unlikely to affect acoustic sensing directly but may interfere with co-located magnetic sensors (compasses, magnetometers). |

#### RE102 — Radiated Emissions, Electric Field (10 kHz - 18 GHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | Entire system in operational configuration |
| **Frequency Range** | 10 kHz - 18 GHz |
| **Limit** | Per Figure RE102-1 (Ground, Army): frequency-dependent; strictest at communications bands |
| **Test Method** | EMI receiving antenna at 1 m; spectrum analyzer/EMI receiver; 3m or 10m anechoic chamber |
| **Applicable Requirements** | [[requirements_list.md#SIG-001]] (EMC compliance), [[requirements_list.md#OPR-014]] (EMCON mode) |
| **Priority** | Critical |
| **VN-CUAS Notes** | Two operational modes must be tested: (1) **Normal mode** — radio active, must meet RE102 limits; (2) **EMCON mode** — radio disabled, emissions must be below detection threshold for adversary SIGINT at tactical ranges. Processor clock frequencies (typically 100-1000 MHz) and their harmonics are the primary emission source. Enclosure must be EMI-shielded (conductive gasket on all joints, EMI-filtered connectors). Acoustic window is a potential EMI leakage path — consider conductive mesh backing behind acoustic-transparent membrane. |

#### RS101 — Radiated Susceptibility, Magnetic Field (30 Hz - 100 kHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | All equipment |
| **Frequency Range** | 30 Hz - 100 kHz |
| **Test Level** | Per Figure RS101-1 (Ground, Army): 180 dBpT at 30 Hz, decreasing |
| **Test Method** | Magnetic field radiating loop at 7 cm |
| **Pass Criteria** | No acoustic false detections; no data corruption; no processor upset |
| **Applicable Requirements** | [[requirements_list.md#SIG-002]] (EMI immunity) |
| **Priority** | Important |
| **VN-CUAS Notes** | Magnetic fields can induce currents in PCB traces, potentially creating noise in the analog microphone front-end. MEMS microphones are capacitive (not magnetic) sensors — inherently less susceptible than dynamic/electret microphones. However, the ADC input traces and reference voltage circuits are vulnerable. Use differential signaling from MEMS to ADC where possible. |

#### RS103 — Radiated Susceptibility, Electric Field (2 MHz - 40 GHz)

| Parameter | Value |
|-----------|-------|
| **Applicability** | Entire system in operational configuration |
| **Frequency Range** | 2 MHz - 40 GHz |
| **Test Level** | Per Table RS103-I (Ground, Army): 20 V/m from 2 MHz to 18 GHz; 50 V/m in selected bands (communications); spot frequencies at antenna resonances |
| **Test Method** | Radiated RF field in anechoic chamber; swept frequency |
| **Pass Criteria** | No acoustic false alarms during RF exposure; detection performance maintained; radio module recovers after exposure; processor does not reset or hang |
| **Applicable Requirements** | [[requirements_list.md#SIG-002]] (EMI immunity), [[requirements_list.md#OPR-015]] (Co-located EMI resistance) |
| **Priority** | Critical |
| **VN-CUAS Notes** | This is the most challenging EMC requirement for VN-CUAS. The system must operate near military radios (PRC-117G type, 30-2000 MHz, up to 20W) and radars (X-band, S-band). 20 V/m at 2 MHz-18 GHz requires good shielding effectiveness (SE ≥40 dB). Acoustic window must not be an RF entry point — conductive mesh or metallized membrane behind acoustic window. All cable entries must be filtered or shielded. MEMS microphone acoustic port is a potential RF entry — evaluate MEMS susceptibility to RF rectification (AM demodulation in the MEMS ASIC). |

### 3.4 MIL-STD-461G Test Program Summary

| Requirement | Type | Priority | Duration | Est. Cost (USD) |
|-------------|------|----------|----------|-----------------|
| CE101 | Emission | Critical | 0.5 day | $2,000 |
| CE102 | Emission | Critical | 0.5 day | $2,000 |
| CS101 | Susceptibility | Important | 0.5 day | $2,500 |
| CS114 | Susceptibility | Important | 1 day | $4,000 |
| RE101 | Emission | Important | 0.5 day | $2,500 |
| RE102 | Emission | Critical | 1 day | $5,000 |
| RS101 | Susceptibility | Important | 0.5 day | $2,500 |
| RS103 | Susceptibility | Critical | 2 days | $8,000 |
| | **TOTAL** | | **~6.5 days** | **~$28,500** |

> EMC testing requires access to a MIL-STD-461G accredited anechoic chamber. Nearest facilities: Singapore (ST Engineering), Australia (BAE Systems), South Korea (ADD). No accredited facility known in Vietnam — see TBD-006.

---

## 4. MIL-STD-882E — SYSTEM SAFETY

### 4.1 Applicability

MIL-STD-882E applies to VN-CUAS-001 as a military system with identified hazards. The system contains lithium batteries, RF transmitters, and AI-based classification that can influence engagement decisions.

### 4.2 Hazard Severity Categories

| Category | Description | VN-CUAS Relevance |
|----------|-------------|-------------------|
| **I — Catastrophic** | Death or system loss | Misclassification leading to friendly fire; battery explosion near personnel |
| **II — Critical** | Severe injury, major damage | Battery thermal runaway causing fire; cybersecurity breach enabling adversary control |
| **III — Marginal** | Minor injury, minor damage | RF exposure at close range; software crash during active threat scenario |
| **IV — Negligible** | Less than minor injury | Incorrect bearing display; nuisance false alarms |

### 4.3 Hazard Probability Levels

| Level | Description | VN-CUAS Application |
|-------|-------------|---------------------|
| **A — Frequent** | Likely to occur often in system life | False alarms in high-noise environments |
| **B — Probable** | Will occur several times | Software anomalies requiring restart |
| **C — Occasional** | Likely to occur sometime | Battery degradation requiring replacement |
| **D — Remote** | Unlikely but possible | Battery thermal event (with proper BMS) |
| **E — Improbable** | Very unlikely to occur | Catastrophic misclassification leading to friendly fire |
| **F — Eliminated** | Cannot occur (design prevents) | Target for all Severity I hazards through design |

### 4.4 VN-CUAS Hazard Identification

| Hazard ID | Hazard | Severity | Probability | Risk Level | Mitigation |
|-----------|--------|----------|-------------|------------|------------|
| **H-001** | Lithium battery thermal runaway | I (Catastrophic) | D (Remote) | Medium | BMS with independent thermal cutoff; cell-level fusing; fire-resistant enclosure partition; UN 38.3 compliant cells |
| **H-002** | Misclassification leading to friendly fire | I (Catastrophic) | E (Improbable) | Low | Dual classification (eigenvector + ML) with confidence scoring; operator-in-the-loop for engagement; never autonomous engagement |
| **H-003** | Cybersecurity breach via OTA update | II (Critical) | D (Remote) | Medium | Signed firmware images; encrypted OTA channel; hardware root-of-trust; rollback capability; air-gapped update option |
| **H-004** | RF exposure to personnel at close range | III (Marginal) | B (Probable) | Medium | RF power ≤1W; antenna placement away from operator position; warning labels; minimum standoff distance defined |
| **H-005** | Battery fire during transport | II (Critical) | D (Remote) | Medium | UN 38.3 qualified cells; SoC limited to 30% for transport; fire-resistant packaging |
| **H-006** | False negative during active threat | II (Critical) | C (Occasional) | Medium | Multi-node fusion reduces single-node miss; alert latency SLA; operator training on system limitations |
| **H-007** | Adversary spoofing of acoustic detection | III (Marginal) | D (Remote) | Low | ML model trained on spoofing signatures; multi-sensor fusion with external radar/RF cues; anomaly detection |
| **H-008** | Electrical shock from battery system | III (Marginal) | E (Improbable) | Low | Voltage ≤48V (SELV per IEC 60950-1); insulated battery compartment; polarity protection |

### 4.5 Required Safety Analyses

| Analysis | Standard Reference | Phase | Applicable Subsystems | Est. Cost (USD) |
|----------|-------------------|-------|----------------------|-----------------|
| **Preliminary Hazard Analysis (PHA)** | MIL-STD-882E Task 401 | Phase 1-2 | Entire system | $5,000 |
| **Subsystem Hazard Analysis (SSHA)** | MIL-STD-882E Task 402 | Phase 2-3 | Battery, radio, AI classification | $8,000 |
| **System Hazard Analysis (SHA)** | MIL-STD-882E Task 403 | Phase 3 | System-level integration | $6,000 |
| **FMEA** | MIL-STD-1629A | Phase 2-3 | All critical subsystems | $10,000 |
| **Fault Tree Analysis (FTA)** | MIL-STD-882E Task 405 | Phase 3 | H-001 (battery), H-002 (misclassification) | $8,000 |
| | **TOTAL** | | | **~$37,000** |

### 4.6 Safety Design Requirements

| Requirement | Description | Applicable Hazard |
|-------------|-------------|-------------------|
| **SDR-001** | Battery Management System (BMS) shall independently monitor cell temperature, voltage, and current with hardware shutdown capability | H-001, H-005 |
| **SDR-002** | Classification output shall always include confidence score; engagement recommendation shall require confidence ≥90% | H-002 |
| **SDR-003** | OTA firmware update shall use cryptographic signing (RSA-2048 or ECDSA P-256 minimum) with hardware root-of-trust | H-003 |
| **SDR-004** | RF transmit power shall not exceed 1W EIRP; antenna shall be positioned ≥30 cm from operator interface | H-004 |
| **SDR-005** | System shall provide degraded-mode operation (reduced detection range, increased false alarm rate) rather than complete failure when any single component fails | H-006 |

---

## 5. MIL-HDBK-217F — RELIABILITY PREDICTION

### 5.1 Applicability

MIL-HDBK-217F Notice 2 provides the methodology for predicting VN-CUAS-001 MTBF. While the handbook is older (1995), it remains the standard reference for military reliability prediction and is required by most defense procurement programs.

### 5.2 Environmental Factors

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Primary environment** | Ground Fixed (GF) | Static deployment at FOB/border post |
| **Secondary environment** | Ground Mobile (GM) | Vehicle-transported field deployment |
| **Temperature** | +40C ambient (MIL-HDBK-217F Table assumes) | Vietnamese tropical average operating |
| **Pi_E (Environmental factor)** | GF: 2.0; GM: 5.0 | Per MIL-HDBK-217F Table 5.1 |

### 5.3 MTBF Target and Allocation

| Subsystem | Component Count | Target MTBF (hrs) | Allocation Basis |
|-----------|----------------|-------------------|-----------------|
| Microphone array (128-256 MEMS) | 128-256 | 50,000 | Redundant — array degrades gracefully |
| ADC/signal conditioning | 4-8 | 40,000 | Commercial-grade multi-channel ADC |
| DSP/processor | 1-2 | 30,000 | Industrial-grade ARM processor |
| FPGA/co-processor | 1 | 40,000 | Industrial-grade FPGA |
| Radio module | 1 | 25,000 | Commercial mesh radio module |
| Power management (BMS + DC-DC) | 1 | 20,000 | Most stressed subsystem (thermal) |
| Battery pack | 1 | 10,000 | Consumable; 500-cycle life |
| Enclosure/mechanical | 1 | 100,000 | Passive; corrosion is primary failure |
| **System (series model)** | — | **≥5,000** | **Per [[requirements_list.md#QUA-001]]** |

> **Calculation note:** System MTBF = 1 / (sum of subsystem failure rates). Preliminary estimate: 1/(1/50000 + 1/40000 + 1/30000 + 1/40000 + 1/25000 + 1/20000 + 1/10000 + 1/100000) = ~4,500 hours. Power management and battery are the reliability bottleneck — must improve to ≥20,000 hrs (PM) and replace battery as maintenance item to achieve system MTBF ≥5,000 hrs.

### 5.4 Component Derating Requirements

| Component Type | Parameter | Maximum Rating Use | VN-CUAS Standard |
|----------------|-----------|-------------------|------------------|
| Semiconductor (IC) | Junction temperature | 70% of Tj_max | Tj ≤ 105C (at 55C ambient) |
| Capacitor (MLCC) | Voltage | 50% of rated voltage | Use 2x rated voltage minimum |
| Capacitor (electrolytic) | Voltage | 60% of rated voltage | Use 1.7x rated voltage minimum |
| Resistor | Power | 50% of rated power | Use 2x rated power minimum |
| Inductor | Current | 70% of saturation current | Use 1.4x rated current minimum |
| Connector | Mating cycles | 50% of rated cycles | Specify connectors rated 2x expected cycles |

### 5.5 Reliability Testing

| Test | Standard | Duration | Sample Size | Est. Cost (USD) |
|------|----------|----------|-------------|-----------------|
| HALT (Highly Accelerated Life Test) | — | 2 weeks | 3 units | $15,000 |
| HASS (Screening) | — | Per production lot | All units | $500/unit |
| Reliability Demonstration (MTBF) | MIL-HDBK-781 | Per test plan (est. 2,000 hrs) | 5 units | $25,000 |
| | **TOTAL (Development)** | | | **~$40,000** |

---

## 6. IEC 60529 — INGRESS PROTECTION (IP67)

### 6.1 Requirements

| Protection | Level | Requirement | Test |
|------------|-------|-------------|------|
| **First digit: 6 (Dust-tight)** | Complete protection against dust ingress | No dust shall enter enclosure after 8 hours in dust chamber at 2 kPa below ambient | IEC 60529 Clause 13.4: Dust chamber, talcum powder, 8 hours, vacuum 2 kPa |
| **Second digit: 7 (Temporary immersion)** | Protection against temporary immersion | No water ingress at 1 m depth for 30 minutes | IEC 60529 Clause 14.2.7: 1 m depth, 30 min, ambient temperature |

### 6.2 Design Implications for Acoustic Window

The acoustic window is the critical IP67 challenge. It must simultaneously:

| Requirement | Target | Design Approach |
|-------------|--------|----------------|
| Pass acoustic energy (50-20,000 Hz) | Insertion loss ≤3 dB | Hydrophobic PTFE membrane (Gore-Tex type) |
| Block dust (IP6X) | Zero dust ingress | PTFE membrane pore size 0.2-1.0 um |
| Block water (IPX7) | Withstand 1 m / 30 min | PTFE membrane water entry pressure >10 kPa |
| Resist UV degradation | ≥2 years outdoor | UV-stabilized PTFE or protected behind UV-opaque mesh |
| Field-replaceable | Tool-free or single-tool | Snap-fit or threaded cap over membrane |

### 6.3 Seal Design Requirements

| Seal Location | Type | Material | Specification |
|---------------|------|----------|---------------|
| Enclosure halves | O-ring (face seal) | EPDM or silicone | Hardness 50-70 Shore A; continuous groove |
| Connector interfaces | IP68 connector | Stainless steel body | MIL-DTL-38999 Series III or equivalent |
| Cable glands | Compression gland | Nickel-plated brass | IP68 rated; double-compression type |
| Battery compartment | O-ring (face seal) | Silicone | Separate from main electronics chamber |
| Acoustic window | Membrane seal | PTFE + adhesive bond | Bonded to enclosure with room-temp-cure silicone |
| Pressure vent | PTFE breather | PTFE membrane | Equalizes pressure during altitude/temperature changes |

### 6.4 Test Cost

| Test | Duration | Est. Cost (USD) |
|------|----------|-----------------|
| IP6X dust test | 1 day | $1,500 |
| IPX7 immersion test | 0.5 day | $1,000 |
| **TOTAL** | **1.5 days** | **$2,500** |

---

## 7. UN 38.3 — LITHIUM BATTERY SAFETY

### 7.1 Transport Safety Tests

| Test | Description | Requirement | Pass Criteria |
|------|-------------|-------------|---------------|
| **T.1** | Altitude simulation | Low pressure (11.6 kPa) at 75C for 6 hours | No mass loss, no fire, no rupture, no venting, voltage OCV ≥90% |
| **T.2** | Thermal test | Cycling between 75C and -40C; 10 cycles, 6h dwell per extreme | No mass loss, no fire, no rupture, no venting, voltage OCV ≥90% |
| **T.3** | Vibration | Sinusoidal sweep 7-200 Hz, 3 axes, 3 hours/axis | No mass loss, no fire, no rupture, no venting, voltage OCV ≥90% |
| **T.4** | Shock | Half-sine 150g, 6 ms, 3 axes, both directions (18 shocks total) | No mass loss, no fire, no rupture, no venting, voltage OCV ≥90% |
| **T.5** | External short circuit | 80 mOhm external resistance, 55C, 1 hour after removal | No fire, no rupture; case temp ≤170C |
| **T.6** | Impact/Crush | 9.1 kg bar dropped from 61 cm | No fire (for small cells); cell-specific |
| **T.7** | Overcharge | 2x recommended charge current to 2x recommended voltage for 24 hours | No fire, no rupture (for rechargeable cells) |
| **T.8** | Forced discharge | Forced discharge at max discharge current in series with 12V source | No fire, no rupture |

### 7.2 IATA Compliance

| Requirement | VN-CUAS Application |
|-------------|---------------------|
| **Section II (battery ≤100 Wh)** | If battery pack ≤100 Wh — likely for 10W x 24h = 240 Wh at cell level; system exceeds Section II limit |
| **Section IA (battery >100 Wh)** | Battery pack >100 Wh requires Section IA — Dangerous Goods declaration, UN-rated packaging, cargo aircraft only (not passenger) |
| **Packing Instruction** | PI 965 (standalone battery) or PI 966/967 (packed with/in equipment) |
| **Labeling** | Lithium battery handling label (Class 9 Miscellaneous Dangerous Goods), UN number UN3481 (lithium-ion packed with equipment) |
| **Documentation** | Shipper's Declaration for Dangerous Goods; MSDS; UN 38.3 test summary |

### 7.3 IEC 62133-2 Secondary Requirements

| Test | Description | Applicability |
|------|-------------|---------------|
| External short circuit | At 20C and 55C | Cell and pack level |
| Free fall | 1 m drop onto concrete | Pack level |
| Thermal abuse | 130C for 10 min (cells) | Cell level |
| Crushing | 13 kN force | Cell level |
| Overcharge protection | Verify BMS cutoff | Pack level — per SDR-001 |
| Forced internal short | Nail penetration or equivalent | Cell level (destructive) |

### 7.4 VN-CUAS Battery Design Requirements

| Requirement | Value | Rationale |
|-------------|-------|-----------|
| Cell chemistry | Lithium-ion (NMC or LFP) | NMC for energy density; LFP for safety and cold performance |
| Pack energy | ~240 Wh (10W x 24h) | Operational runtime requirement |
| Cell configuration | 3S or 4S (10.8-14.8V nominal) | Matches common DC-DC input range |
| BMS features | Cell balancing, over-voltage/under-voltage cutoff, over-temperature cutoff, short-circuit protection | Per H-001, SDR-001 |
| UN 38.3 certification | Required for all cells and pack | Transport compliance |
| Cell source | Certified manufacturer (Samsung SDI, LG Energy, CATL, EVE Energy) | Quality and traceability |
| **Estimated test cost** | **$8,000-12,000** | Per accredited battery test lab |

---

## 8. NATO STANAG REFERENCES

### 8.1 STANAG 4586 — UAV Control System Interfaces

| Parameter | Value |
|-----------|-------|
| **Relevance** | VN-CUAS detects UAVs — interoperability with UAV control systems enables correlation of detected acoustic tracks with known friendly UAV positions (IFF function) |
| **Applicable Levels** | Level 2 (Receive UAV sensor product data) — VN-CUAS receives friendly UAV position data to suppress friendly-fire alerts |
| **Implementation** | C2 interface ingests STANAG 4586 messages for friendly UAV position; correlates with acoustic detections; suppresses known-friendly tracks |
| **Applicable Requirements** | [[requirements_list.md#SIG-004]] (C2 integration), [[requirements_list.md#SAF-002]] (Friendly fire prevention) |
| **Priority** | Important — Phase 2-3 interface design |
| **VN-CUAS Notes** | Vietnamese forces may not currently use STANAG 4586. Implement as optional interface module. Internal IFF list (GPS coordinates of known-friendly UAVs) can serve same function without full STANAG 4586 compliance. |

### 8.2 STANAG 4607 — GMTI/Radar Track Format (NATO AEDP-7)

| Parameter | Value |
|-----------|-------|
| **Relevance** | VN-CUAS acoustic tracks must be translatable to common track formats for multi-sensor fusion with radar systems |
| **Implementation** | Export acoustic tracks in STANAG 4607-compatible format (target position, velocity, classification, confidence) for fusion with radar GMTI tracks |
| **Applicable Requirements** | [[requirements_list.md#SIG-005]] (Track format compatibility) |
| **Priority** | Optional — Only needed when integrating with NATO-compatible radar systems |
| **VN-CUAS Notes** | Vietnamese military primarily uses Russian-origin radar systems. Track format conversion may need to support both NATO (STANAG 4607) and Russian (proprietary) formats. Implement as a pluggable track formatter module. |

### 8.3 SAPIENT — Sensing for Asset Protection with Integrated Electronic Networked Technology

| Parameter | Value |
|-----------|-------|
| **Relevance** | SAPIENT is the emerging standard for autonomous sensor network management in C-UAS applications. DroneShield, Dedrone, and Mind Foundry all support SAPIENT. |
| **Version** | SAPIENT v7 (BSI Flex 335, published by DSTL/BSI) |
| **Implementation** | VN-CUAS node implements SAPIENT ASM (Autonomous Sensor Module) interface: reports detections, accepts tasking, provides status |
| **Key Messages** | Registration, SensorTask, Detection, Status, Alert |
| **Protocol** | Google Protocol Buffers over TCP/IP (SAPIENT v7) |
| **Applicable Requirements** | [[requirements_list.md#SIG-006]] (SAPIENT interface), [[requirements_list.md#SIG-004]] (C2 integration) |
| **Priority** | Critical — Table-stakes for international C-UAS market; validated by Mind Foundry SENTRY, DroneShield DroneSentry |
| **VN-CUAS Notes** | SAPIENT integration enables VN-CUAS to plug into any SAPIENT-compliant C2 system. Implement SAPIENT ASM as a software module with versioned protocol adapter. SAPIENT test tools available from DSTL for compliance validation. Estimated development: 4-6 weeks for basic SAPIENT ASM. |

### 8.4 ADatP-36 — Friendly Force Tracking

| Parameter | Value |
|-----------|-------|
| **Relevance** | VN-CUAS must distinguish friendly drones from hostile — Friendly Force Tracking (FFT) data enables IFF correlation |
| **Implementation** | Receive FFT data (blue force positions including friendly UAVs) and correlate with acoustic detections to reduce friendly-fire risk |
| **Applicable Requirements** | [[requirements_list.md#SAF-002]] (Friendly fire prevention), [[requirements_list.md#SIG-004]] (C2 integration) |
| **Priority** | Important — Becomes critical as Vietnamese forces increase UAV use |
| **VN-CUAS Notes** | Vietnamese BMS may not implement ADatP-36. Design IFF function to accept position data from any source (BMS, manual input, TAK, STANAG 4586) and correlate with acoustic tracks. Fusion logic: if acoustic track correlates with known-friendly position within tolerance (range <50 m, bearing <5 deg), classify as "FRIEND" and suppress alert. |

### 8.5 TAK (Team Awareness Kit) Integration

| Parameter | Value |
|-----------|-------|
| **Relevance** | TAK (formerly ATAK/WinTAK) is widely adopted by Vietnamese SOF and allied forces. Mind Foundry SENTRY demonstrated TAK integration in <30 seconds. |
| **Implementation** | TAK plugin (CoT — Cursor on Target messages over multicast or TAK Server) that displays VN-CUAS detections as map overlays |
| **Protocol** | CoT XML over UDP multicast (SA) or TAK Server API (RESTful) |
| **Applicable Requirements** | [[requirements_list.md#SIG-007]] (TAK integration) |
| **Priority** | Critical — Enables rapid adoption without dedicated C2 infrastructure |
| **VN-CUAS Notes** | TAK plugin development is well-documented. CoT message for VN-CUAS detection: type="a-h-A-M-H-Q" (hostile, air, military, helicopter/rotary — closest to drone). Include detection bearing, estimated range, classification, confidence as CoT detail fields. Estimated development: 2-4 weeks for basic TAK plugin. |

---

## 9. TCVN — VIETNAMESE NATIONAL STANDARDS

### 9.1 Applicable TCVN Standards

| TCVN | Title | IEC/ISO Equivalent | Applicability |
|------|-------|--------------------|--------------|
| **TCVN 4255:2008** | Degrees of protection by enclosures | IEC 60529 | IP67 testing — TCVN is direct adoption of IEC 60529 |
| **TCVN 7909-1:2008** | EMC — Generic emission | IEC 61000-6-3 | General EMC emission limits (civilian; military use MIL-STD-461G) |
| **TCVN 7909-2:2008** | EMC — Generic immunity | IEC 61000-6-1 | General EMC immunity limits (civilian baseline) |
| **TCVN 6480:2008** | IT equipment safety | IEC 60950-1 | Electrical safety of processing unit (replaced by IEC 62368-1) |
| **TCVN 8241** series | Environmental testing | IEC 60068 series | Environmental test methods (civilian equivalent of MIL-STD-810H subsets) |
| **TCVN 6612:2007** | Lithium battery safety | IEC 62133 (older) | Battery safety (supplements UN 38.3) |

### 9.2 Vietnamese Defense-Specific Standards

| Standard | Status | Notes |
|----------|--------|-------|
| QCVN (Vietnamese technical regulation) for military electronics | **TBD-002** | Vietnamese Ministry of National Defence may have internal standards. Must consult with MoND procurement authority. |
| Vietnamese military environmental test requirements | **TBD-002** | May specify Vietnamese-specific climate categories (A2 tropical humid as baseline). |
| Vietnamese cybersecurity requirements for defense systems | **TBD-002** | Cybersecurity Law 2018 (Luat An Ninh Mang) applies to defense systems. Specific technical requirements to be determined. |
| Vietnamese defense procurement QA requirements | **TBD-002** | May require ISO 9001 + additional defense QA procedures. |

### 9.3 TCVN Compliance Strategy

| Approach | Application |
|----------|-------------|
| **Direct equivalence** | Where TCVN directly adopts IEC/ISO (e.g., TCVN 4255 = IEC 60529), MIL-STD testing exceeds TCVN requirements. Provide MIL-STD test report with TCVN equivalence statement. |
| **Dual compliance** | Where TCVN has specific Vietnamese additions, perform additional TCVN-specific tests. |
| **Gap resolution** | Engage with Vietnamese MoND (Bo Quoc Phong) standards authority to clarify defense-specific requirements. Target resolution by end of Phase 2. |

---

## 10. SOFTWARE AND CYBERSECURITY STANDARDS

### 10.1 Safety-Critical Software (DO-178C Equivalence)

| Parameter | Value |
|-----------|-------|
| **Standard** | DO-178C / ED-12C (Software Considerations in Airborne Systems and Equipment Certification) — adapted for ground defense |
| **Applicability** | VN-CUAS classification output influences engagement decisions (H-002). Software criticality derived from MIL-STD-882E hazard severity. |
| **DAL (Design Assurance Level)** | DAL-C (Major) — misclassification could lead to incorrect engagement decisions. Not DAL-A/B because operator-in-the-loop prevents autonomous engagement. |
| **Key Requirements** | Requirements traceability, code coverage (statement + decision at DAL-C), configuration management, verification testing, independence of verification from development |
| **Applicable Requirements** | [[requirements_list.md#SAF-003]] (Software safety), [[requirements_list.md#QUA-004]] (Software quality) |
| **Priority** | Important — Full DO-178C certification is expensive ($200K+). Recommend DO-178C-like process with documentation but without formal DER certification for initial production. |
| **VN-CUAS Notes** | Partition software into safety-critical (classification engine, alert generation, BMS control) and non-safety-critical (UI, logging, diagnostics). Apply DO-178C rigor only to safety-critical partition. Use RTOS with time/space partitioning (e.g., FreeRTOS + MPU or Zephyr with separation) to enforce partitioning. |

### 10.2 NIST Cybersecurity Framework (OTA Update Security)

| Function | VN-CUAS Application |
|----------|---------------------|
| **Identify** | Asset inventory: firmware version, ML model version, crypto key status, configuration baseline |
| **Protect** | Cryptographic signing of firmware images (RSA-2048 or ECDSA P-256); encrypted OTA channel (TLS 1.3); hardware root-of-trust (TPM or secure element); boot-time signature verification (secure boot) |
| **Detect** | Integrity monitoring: firmware hash verification at boot; runtime anomaly detection; tamper detection on enclosure |
| **Respond** | Rollback to last-known-good firmware on verification failure; alert C2 on tamper or integrity violation; isolate compromised node from mesh network |
| **Recover** | Factory reset capability; re-keying procedure for compromised keys; replacement unit provisioning |

| Requirement | Specification | Applicable Requirement |
|-------------|--------------|----------------------|
| Firmware signing | RSA-2048 or ECDSA P-256 with hardware key storage | [[requirements_list.md#SIG-008]] (OTA security) |
| Secure boot | Chain-of-trust from hardware root to application | [[requirements_list.md#SIG-008]] |
| Encrypted comms | TLS 1.3 or DTLS 1.3 for mesh and C2 links | [[requirements_list.md#SIG-009]] (Encrypted communications) |
| Key management | Unique per-device key pair; key rotation support; revocation list | [[requirements_list.md#SIG-008]] |
| OTA rollback | Dual-bank firmware with automatic rollback on boot failure | [[requirements_list.md#SIG-008]] |

### 10.3 IEC 62443 — Industrial Cybersecurity

| Parameter | Value |
|-----------|-------|
| **Applicability** | VN-CUAS C2 interface connects to military networks. IEC 62443 provides security level (SL) framework. |
| **Target Security Level** | SL-2 (Protection against intentional violation using simple means with low resources, generic skills, and low motivation) — appropriate for tactical field system |
| **Key Requirements** | Network segmentation (VN-CUAS mesh isolated from command network); authentication (mutual TLS); access control (role-based); audit logging; availability (degraded mode on network loss) |
| **Applicable Requirements** | [[requirements_list.md#SIG-010]] (Network security), [[requirements_list.md#SAF-003]] (Software safety) |
| **Priority** | Important — Baseline cybersecurity for network-connected military system |

---

## 11. COMPLIANCE STRATEGY

### 11.1 Compliance Approach Matrix

| Standard | Full Test | Analysis | Similarity | Tailored |
|----------|-----------|----------|------------|----------|
| MIL-STD-810H (Critical methods) | X | | | |
| MIL-STD-810H (Important methods) | | X (some) | | X |
| MIL-STD-810H (Optional methods) | | X | | X |
| MIL-STD-461G | X | | | |
| MIL-STD-882E | | X | | |
| MIL-HDBK-217F | | X | | |
| IP67 (IEC 60529) | X | | | |
| UN 38.3 | X (cells) | | X (pack) | |
| NATO STANAGs | | | | X |
| TCVN | | | X (via MIL-STD) | |
| DO-178C | | | | X (DAL-C like) |
| NIST CSF | | X | | |
| IEC 62443 | | X | | X |

### 11.2 Compliance Methods

| Method | Definition | When Used |
|--------|-----------|-----------|
| **Full Test** | Complete test per standard procedure, in accredited laboratory | Critical requirements; market entry standards |
| **Analysis** | Engineering analysis (simulation, calculation, inspection) demonstrates compliance | Where testing is impractical or unnecessary |
| **Similarity** | Reference test data from similar qualified product (e.g., battery cells already UN 38.3 certified by manufacturer) | Component-level compliance; leveraging supplier certifications |
| **Tailored** | Modified test procedure or acceptance criteria, documented and justified | Where full standard is excessive for VN-CUAS operational profile |

---

## 12. COMPLIANCE SCHEDULE

### 12.1 Phase-by-Phase Standards Activities

| Phase | Standards Activity | Deliverable |
|-------|-------------------|-------------|
| **Phase 1** | Standards mapping (this document); PHA (MIL-STD-882E Task 401); identify test facilities | Standards mapping document; preliminary hazard list |
| **Phase 2** | FMEA for critical subsystems; EMC pre-compliance design review; battery chemistry selection per UN 38.3 | FMEA report; EMC design checklist; battery specification |
| **Phase 3** | Design Verification (DV) testing: rain, immersion, vibration, shock, EMC pre-scan; IP67 prototype verification | DV test reports; design changes based on test findings |
| **Phase 4** | Full qualification testing: MIL-STD-810H (all methods), MIL-STD-461G (all requirements), IP67, UN 38.3; HALT/HASS | Qualification test reports; type approval documentation |

### 12.2 Timeline Estimate

| Activity | Start | Duration | End | Dependencies |
|----------|-------|----------|-----|-------------|
| Standards mapping | Phase 1 | 2 weeks | Phase 1 gate | None |
| PHA | Phase 1 | 2 weeks | Phase 1 gate | Standards mapping |
| Test facility identification | Phase 1 | 4 weeks | Phase 1 gate | Standards mapping |
| FMEA | Phase 2 | 4 weeks | Phase 2 gate | PHA, concept selection |
| EMC design review | Phase 2 | 2 weeks | Phase 2 gate | Concept selection |
| DV test plan | Phase 3 | 2 weeks | Phase 3 start | FMEA |
| DV testing (environmental) | Phase 3 | 8 weeks | Phase 3 gate | Prototype available |
| DV testing (EMC pre-scan) | Phase 3 | 2 weeks | Phase 3 gate | Prototype available |
| Qualification test plan | Phase 4 | 4 weeks | Phase 4 Q1 | DV test results |
| Qualification testing | Phase 4 | 20 weeks | Phase 4 Q3 | Production-representative units |
| Certification documentation | Phase 4 | 4 weeks | Phase 4 Q4 | All qual tests complete |

---

## 13. COST ESTIMATES FOR QUALIFICATION TESTING

### 13.1 Total Test Cost Summary

| Standard | Est. Cost (USD) | Phase |
|----------|-----------------|-------|
| MIL-STD-810H (16 methods) | $63,500 | Phase 3-4 |
| MIL-STD-461G (8 requirements) | $28,500 | Phase 3-4 |
| MIL-STD-882E (safety analyses) | $37,000 | Phase 1-4 |
| MIL-HDBK-217F (reliability testing) | $40,000 | Phase 3-4 |
| IP67 (IEC 60529) | $2,500 | Phase 3 |
| UN 38.3 (battery) | $10,000 | Phase 3-4 |
| Software (DO-178C-like process) | $30,000 | Phase 2-4 |
| Cybersecurity (assessment) | $15,000 | Phase 3-4 |
| **TOTAL ESTIMATED** | **$226,500** | |

### 13.2 Cost Optimization Strategies

| Strategy | Savings | Approach |
|----------|---------|----------|
| **Combined testing** | 15-20% | Run MIL-STD-810H methods in optimized sequence (humidity before fungus, etc.) |
| **In-country DV testing** | 30-40% (DV phase) | Use Vietnamese test labs for rain, immersion, vibration, shock (DV only); reserve accredited international labs for qualification |
| **Supplier certifications** | $5,000-10,000 | Leverage battery cell manufacturer's UN 38.3 certification; avoid re-testing cells |
| **Phased qualification** | Cash flow | Test Critical methods first (Phase 3 DV); defer Optional methods to Phase 4 |
| **Reduced sample size** | 20-30% on units | Use minimum sample size per MIL-HDBK-781 test plan; accept longer test duration |

### 13.3 Realistic Budget Estimate

| Scenario | Total Cost | Notes |
|----------|-----------|-------|
| **Minimum viable** | $150,000 | Critical standards only; analysis/similarity for non-critical |
| **Recommended** | $226,500 | Full program per Section 13.1 |
| **Comprehensive** | $300,000 | Including HALT margin, re-test after design changes, extended MTBF demonstration |

---

## 14. CROSS-REFERENCE: REQUIREMENTS TO STANDARDS

### 14.1 Requirement-to-Standard Traceability Matrix

| Requirement ID | Requirement Description | Standard | Clause/Method | Test Method | Compliance Approach |
|----------------|------------------------|----------|---------------|-------------|---------------------|
| [[requirements_list.md#OPR-001]] | Operating altitude 0-3000 m | MIL-STD-810H | Method 500.6 | Procedure I, II | Test |
| [[requirements_list.md#OPR-002]] | Temperature -10C to +55C | MIL-STD-810H | Methods 501.7, 502.7 | Procedure II | Test |
| [[requirements_list.md#OPR-003]] | Environmental operating range | MIL-STD-810H | Multiple methods | Combined | Test + Analysis |
| [[requirements_list.md#OPR-005]] | Contamination resistance | MIL-STD-810H | Method 504.2 | Procedure I | Test |
| [[requirements_list.md#OPR-006]] | Outdoor deployment life ≥2 years | MIL-STD-810H | Method 505.7 | Procedure I | Test |
| [[requirements_list.md#OPR-007]] | Rain operation | MIL-STD-810H | Method 506.6 | Procedure I, III | Test |
| [[requirements_list.md#OPR-008]] | 95% RH tropical humidity | MIL-STD-810H | Methods 507.6, 508.7 | Procedure II | Test |
| [[requirements_list.md#OPR-009]] | Maritime/coastal operation | MIL-STD-810H | Method 509.7 | Procedure I | Test |
| [[requirements_list.md#OPR-010]] | Dusty environment | MIL-STD-810H | Method 510.7 | Procedure I, II | Test |
| [[requirements_list.md#OPR-011]] | Submersion survival (IP67) | MIL-STD-810H / IEC 60529 | Method 512.6 / Cl. 14.2.7 | Immersion | Test |
| [[requirements_list.md#OPR-012]] | Co-located weapons operation | MIL-STD-810H | Method 519.8 | Procedure III | Test (optional) |
| [[requirements_list.md#OPR-013]] | Icing conditions | MIL-STD-810H | Method 521.4 | Procedure I | Analysis + Test |
| [[requirements_list.md#OPR-014]] | EMCON mode (zero RF) | MIL-STD-461G | RE102 (EMCON limit) | Emission scan | Test |
| [[requirements_list.md#OPR-015]] | Co-located EMI resistance | MIL-STD-461G | RS103 | Radiated susceptibility | Test |
| [[requirements_list.md#FOR-001]] | Vibration resistance | MIL-STD-810H | Method 514.8 | Category 4, truck | Test |
| [[requirements_list.md#FOR-002]] | Shock resistance (40g) | MIL-STD-810H | Method 516.8 | Procedure I, IV | Test |
| [[requirements_list.md#FOR-003]] | Gunfire shock resistance | MIL-STD-810H | Method 519.8 | Procedure III | Test (optional) |
| [[requirements_list.md#MAT-001]] | Material thermal stability | MIL-STD-810H | Methods 501.7, 502.7, 503.7 | Combined | Test |
| [[requirements_list.md#MAT-004]] | Chemical resistance | MIL-STD-810H | Method 504.2 | Procedure I | Test |
| [[requirements_list.md#MAT-005]] | UV resistance | MIL-STD-810H | Method 505.7 | Procedure I | Test |
| [[requirements_list.md#MAT-006]] | Water resistance (IP67) | IEC 60529 | Clause 14.2.7 | IPX7 immersion | Test |
| [[requirements_list.md#MAT-007]] | Corrosion resistance | MIL-STD-810H | Methods 507.6, 509.7 | Combined | Test |
| [[requirements_list.md#MAT-008]] | Fungus resistance | MIL-STD-810H | Method 508.7 | Procedure I or II | Analysis preferred |
| [[requirements_list.md#MAT-009]] | Salt corrosion resistance | MIL-STD-810H | Method 509.7 | Procedure I | Test |
| [[requirements_list.md#MAT-010]] | Dust resistance | MIL-STD-810H / IEC 60529 | Method 510.7 / Cl. 13.4 | IP6X | Test |
| [[requirements_list.md#MAT-011]] | Ice resistance | MIL-STD-810H | Method 521.4 | Procedure I | Analysis (optional) |
| [[requirements_list.md#ENR-001]] | Power at temperature extremes | MIL-STD-810H | Methods 501.7, 502.7 | Combined | Test |
| [[requirements_list.md#ENR-002]] | Battery cold performance | MIL-STD-810H | Method 502.7 | Procedure II | Test |
| [[requirements_list.md#ENR-003]] | Power quality | MIL-STD-461G | CE101, CE102, CS101 | Combined | Test |
| [[requirements_list.md#SIG-001]] | EMC compliance (emissions) | MIL-STD-461G | CE101, CE102, RE101, RE102 | Per requirement | Test |
| [[requirements_list.md#SIG-002]] | EMI immunity | MIL-STD-461G | CS101, CS114, RS101, RS103 | Per requirement | Test |
| [[requirements_list.md#SIG-003]] | Cable immunity | MIL-STD-461G | CS114 | BCI | Test |
| [[requirements_list.md#SIG-004]] | C2 integration | STANAG 4586, SAPIENT, ADatP-36 | Various | Interface test | Test + Demo |
| [[requirements_list.md#SIG-005]] | Track format compatibility | STANAG 4607 | AEDP-7 | Format validation | Analysis + Demo |
| [[requirements_list.md#SIG-006]] | SAPIENT interface | BSI Flex 335 (SAPIENT v7) | ASM interface | Protocol test | Test + Demo |
| [[requirements_list.md#SIG-007]] | TAK integration | CoT standard | CoT XML | Plugin test | Demo |
| [[requirements_list.md#SIG-008]] | OTA update security | NIST CSF, IEC 62443 | Various | Penetration test | Test + Analysis |
| [[requirements_list.md#SIG-009]] | Encrypted communications | NIST CSF | TLS 1.3 / DTLS 1.3 | Protocol verification | Test |
| [[requirements_list.md#SIG-010]] | Network security | IEC 62443 | SL-2 | Security assessment | Analysis + Test |
| [[requirements_list.md#SAF-001]] | Battery safety | UN 38.3, IEC 62133-2, MIL-STD-882E | T.1-T.8, Hazard H-001 | Cell + pack test | Test |
| [[requirements_list.md#SAF-002]] | Friendly fire prevention | MIL-STD-882E, ADatP-36 | H-002 | FMEA, FTA | Analysis |
| [[requirements_list.md#SAF-003]] | Software safety | DO-178C (tailored), MIL-STD-882E | DAL-C equivalent | Coverage analysis | Analysis + Test |
| [[requirements_list.md#QUA-001]] | MTBF ≥5,000 hours | MIL-HDBK-217F | Prediction method | HALT, MTBF demo | Test + Analysis |
| [[requirements_list.md#QUA-003]] | Detection in rain | MIL-STD-810H | Method 506.6 | Functional rain test | Test |
| [[requirements_list.md#QUA-004]] | Software quality | DO-178C (tailored) | DAL-C | Code coverage + review | Analysis + Test |
| [[requirements_list.md#TRN-001]] | Transport survivability | MIL-STD-810H | Method 514.8 | Category 4 truck | Test |
| [[requirements_list.md#TRN-002]] | Drop survivability | MIL-STD-810H | Method 516.8 | Procedure IV | Test |

---

## 15. TBDs AND GAPS

### 15.1 Open TBDs

| TBD ID | Description | Owner | Target Resolution | Impact |
|--------|-------------|-------|-------------------|--------|
| **TBD-002** | TCVN defense-specific standards — Vietnamese MoND requirements not yet identified | Engineering + MoND liaison | Phase 2 start | May add additional test requirements |
| **TBD-006** | MIL-STD-810H/461G accredited test facility selection (Singapore, Australia, South Korea) | Programme Manager | Phase 2 | Affects qualification schedule and cost |
| **TBD-009** | Gunfire shock requirement (MUST or WISH?) — depends on co-location with weapon systems | Customer / User | Phase 1 gate | Affects enclosure design and cost |
| **TBD-010** | Vietnamese cybersecurity law (Luat An Ninh Mang) specific technical requirements for defense systems | Legal + Engineering | Phase 2 | May add cybersecurity certification requirement |
| **TBD-011** | DO-178C formal certification requirement vs. DO-178C-like process | Customer / MoND | Phase 2 | $200K+ cost difference |
| **TBD-012** | Battery chemistry selection (NMC vs LFP) — affects UN 38.3 test scope and cold performance | Engineering trade study | Phase 2 | Affects safety, performance, and certification |
| **TBD-013** | Vietnamese test lab capabilities for DV-phase environmental testing | Programme Manager | Phase 2 | Affects cost optimization strategy |
| **TBD-014** | STANAG 4586 / 4607 requirement (mandatory for Vietnamese procurement or optional?) | Customer / MoND | Phase 1 gate | Affects C2 interface design scope |

### 15.2 Standards Gaps

| Gap | Description | Risk | Mitigation |
|-----|-------------|------|------------|
| **No MIL-STD for acoustic sensor performance** | No military standard specifically for passive acoustic drone detection performance (Pd, Pfa, classification accuracy) | Medium — no recognized verification standard | Define internal test procedure based on Fraunhofer IDMT and GA-EMS Fencepost published test methodologies; propose to customer as the acceptance test procedure |
| **No TCVN for military EMC** | Vietnamese EMC standards (TCVN 7909) are civilian-level; no military equivalent to MIL-STD-461G identified | Low — MIL-STD-461G exceeds TCVN requirements | Use MIL-STD-461G as primary; declare TCVN equivalence |
| **No standard for ML model validation** | No accepted standard for validating ML-based classification models in military applications | High — customer may question ML reliability | Develop internal ML validation procedure: confusion matrix, per-class accuracy, adversarial robustness testing, operational test with live drones. Reference emerging standards (e.g., NIST AI 100-1, NATO STANREC 4811) |
| **Acoustic window lacks test standard** | No standard for testing acoustic windows that must simultaneously pass sound and block water/dust | Medium — critical design element has no standardized test | Develop internal test procedure: acoustic insertion loss measurement (anechoic chamber, 100-20,000 Hz) before and after IP67 testing |

---

## 16. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-11 | VN-CUAS Engineering Team | Initial release |

---

*This document will be updated as TBDs are resolved and standards requirements are refined through Phase 1-4.*
*Cross-reference: [[requirements_list.md]] for full requirement definitions.*
*Classification: UNCLASSIFIED*
