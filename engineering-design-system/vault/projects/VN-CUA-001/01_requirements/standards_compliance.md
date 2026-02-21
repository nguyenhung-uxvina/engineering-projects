---
project: VN-CUA-001
designation: VDC-100
type: standards_compliance
phase: 1
version: 1.0
created: 2026-02-08
status: approved
methodology: Pahl & Beitz (VDI 2221) - Step 6
---

# VN-CUA-001: STANDARDS COMPLIANCE MATRIX
## Vietnamese Drone Catcher 100 (VDC-100)
## Ma trận Tuân thủ Tiêu chuẩn - Giai đoạn 1, Bước 6

**Project Code:** VN-CUA-001
**Phase:** 1 - Task Clarification (Step 6)
**Date:** 2026-02-08

---

# 1. APPLICABLE STANDARDS

| Standard | Title | Applicability | Status |
|----------|-------|---------------|--------|
| **MIL-STD-810H** | Environmental Engineering Considerations | Full — environmental qualification | Primary |
| **MIL-STD-461G** | EMI/EMC Requirements | Partial — LRF/display electronics only | Secondary |
| **MIL-STD-882E** | System Safety | Full — pneumatic pressure + projectile | Primary |
| **MIL-STD-1472G** | Human Engineering | Partial — ergonomics/controls | Secondary |
| **IEC 60825-1** | Laser Safety | Full — laser rangefinder | Primary |
| **DOT-3AL** | HPA Cylinder Certification | Full — pressure vessel | Primary |
| **TCVN 6153:1996** | Pressure Equipment (Vietnam) | Full — Vietnamese compliance | Required |
| **IP Code (IEC 60529)** | Ingress Protection | Partial — dust/rain resistance | Secondary |

---

# 2. MIL-STD-810H COMPLIANCE MATRIX

## 2.1 Environmental Test Methods

| Method | Test | Requirement ID | Condition | Procedure | Duration | Acceptance Criteria |
|--------|------|----------------|-----------|-----------|----------|---------------------|
| **501.7** | High Temperature | CUA-OPR-01 | 55°C operating | Procedure II (Cycling) | 7 cycles (168 hr) | Functional, no degradation |
| **502.7** | Low Temperature | CUA-OPR-01 | -10°C operating | Procedure II (Cycling) | 7 cycles (168 hr) | Functional, no degradation |
| **507.6** | Humidity | CUA-OPR-02 | 95% RH, 40°C | Procedure II (Aggravated) | 10 cycles (240 hr) | No corrosion, functional |
| **510.7** | Sand & Dust | CUA-OPR-04 | Blowing dust | Procedure I | 6 hr | Functional, seals intact |
| **514.8** | Vibration | — | Transport vibration | Procedure I (General) | Per curve | No damage, functional |
| **516.8** | Shock | CUA-FOR-05 | 1m drop, concrete | Procedure IV (Transit drop) | 26 drops (each axis) | Functional, no cracks |
| **506.6** | Rain | CUA-OPR-03 | Light rain ~10 mm/hr | Procedure I (Blowing rain) | 30 min per face | Electronics functional |
| **500.6** | Low Pressure | CUA-OPR-05 | 3,000m ASL equiv | Procedure II | 2 hr | Functional, seals hold |
| **509.7** | Salt Fog | — | Coastal deployment | Procedure I | 48 hr | No corrosion (Al anodized) |

## 2.2 Test Sequence (Recommended)

```
MIL-STD-810H TEST SEQUENCE
═══════════════════════════════════════════════════════════════════════════════

PHASE 1: INITIAL INSPECTION + FUNCTIONAL BASELINE
│
├─► HIGH TEMP (501.7) ──► FUNCTIONAL CHECK
│
├─► LOW TEMP (502.7) ──► FUNCTIONAL CHECK
│
├─► HUMIDITY (507.6) ──► FUNCTIONAL CHECK + VISUAL INSPECTION
│
├─► SAND/DUST (510.7) ──► FUNCTIONAL CHECK
│
├─► RAIN (506.6) ──► FUNCTIONAL CHECK
│
├─► VIBRATION (514.8) ──► FUNCTIONAL CHECK
│
├─► SHOCK/DROP (516.8) ──► FUNCTIONAL CHECK + VISUAL INSPECTION
│
├─► LOW PRESSURE (500.6) ──► FUNCTIONAL CHECK
│
└─► SALT FOG (509.7) ──► FINAL INSPECTION + FUNCTIONAL CHECK

TOTAL ESTIMATED DURATION: 6-8 weeks (2 units in parallel)
ESTIMATED COST: $15,000-25,000 (outsourced lab)
```

---

# 3. MIL-STD-882E SAFETY COMPLIANCE

## 3.1 Hazard Analysis Summary

| Hazard ID | Hazard Description | Severity | Probability | Risk Level | Req ID | Mitigation |
|-----------|-------------------|----------|-------------|------------|--------|------------|
| H-01 | Accidental discharge (misfire) | III - Critical | D - Remote | Medium | CUA-SAF-01 | Positive safety interlock (mechanical) |
| H-02 | Over-pressurization (cylinder burst) | I - Catastrophic | E - Improbable | Medium | CUA-SAF-02, CUA-FOR-04 | Relief valve @ 350 bar; DOT certified cylinder |
| H-03 | Muzzle obstruction detonation | II - Critical | D - Remote | Medium | CUA-SAF-03 | Obstruction detection; operator training |
| H-04 | Laser eye injury (LRF) | III - Marginal | C - Occasional | Medium | CUA-SAF-04 | Class 1 eye-safe LRF (IEC 60825) |
| H-05 | Projectile impact on person | II - Critical | D - Remote | Medium | — | ROE training; clear firing corridor |
| H-06 | Captured drone crash (parachute fail) | III - Marginal | C - Occasional | Low | CUA-SAF-05 | Drogue backup; descent rate control |
| H-07 | Gas leak (regulator failure) | III - Marginal | D - Remote | Low | CUA-SAF-02 | Pressure gauge monitoring; auto-shutoff |
| H-08 | Trigger jam under stress | III - Marginal | D - Remote | Low | CUA-FOR-01 | Simple mechanical linkage; redundant spring |
| H-09 | Recoil injury (improper shoulder) | IV - Negligible | C - Occasional | Low | CUA-FOR-02 | Butt pad; training on stance |
| H-10 | Battery thermal runaway (scope) | III - Marginal | E - Improbable | Low | CUA-ENE-04 | CR123A (stable chemistry); thermal cutoff |

## 3.2 Safety Risk Matrix

```
╔══════════════════════════════════════════════════════════════════╗
║  MIL-STD-882E RISK ASSESSMENT MATRIX                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  PROBABILITY    │ I Catastrophic │ II Critical │ III Marginal    ║
║  ──────────────│────────────────│─────────────│──────────────── ║
║  A Frequent     │    HIGH        │    HIGH     │    SERIOUS      ║
║  B Probable     │    HIGH        │    HIGH     │    MEDIUM       ║
║  C Occasional   │    HIGH        │    SERIOUS  │  ► H-04, H-06  ║
║                 │                │             │  ► H-09         ║
║  D Remote       │    SERIOUS     │  ► H-05     │  ► H-01, H-03  ║
║                 │                │             │  ► H-07, H-08   ║
║  E Improbable   │  ► H-02        │    LOW      │  ► H-10        ║
║                                                                  ║
║  RESULT: No HIGH risks. 1 SERIOUS (H-05: projectile impact)     ║
║          All mitigated to MEDIUM or LOW with design controls.    ║
╚══════════════════════════════════════════════════════════════════╝
```

## 3.3 Safety Requirements Traceability

| Safety Req | Hazard(s) | Design Solution | Verification |
|------------|-----------|-----------------|--------------|
| CUA-SAF-01 | H-01 | Positive mechanical arm/safe switch | D: Demonstrate 1000 arm/safe cycles |
| CUA-SAF-02 | H-02, H-07 | Auto-relief valve @ 350 bar | T: Pressure test to 1.5× working |
| CUA-SAF-03 | H-03 | Muzzle proximity sensor or physical interlock | T: Blocked barrel test (5 shots) |
| CUA-SAF-04 | H-04 | Class 1 LRF per IEC 60825 | I: Manufacturer certificate |
| CUA-SAF-05 | H-06 | Drogue parachute backup | T: 50 deployments, measure descent rate |

---

# 4. MIL-STD-461G EMC COMPLIANCE

## 4.1 Applicable EMC Tests

| Test | Description | Applicability | Equipment Affected | Limit |
|------|-------------|---------------|--------------------| ------|
| **RE102** | Radiated Emissions (10 kHz - 18 GHz) | Scope electronics, LRF | Display, LRF module | Class B (man-portable) |
| **RS103** | Radiated Susceptibility | All electronics | Scope, safety interlock | 10 V/m (field level) |
| **CE102** | Conducted Emissions | Battery-powered (limited) | Power circuits | Limited applicability |
| **CS101** | Conducted Susceptibility | Battery-powered (limited) | Power circuits | Limited applicability |

## 4.2 EMC Design Approach

| Strategy | Implementation | Affected Components |
|----------|---------------|---------------------|
| Shielded enclosure | Aluminum scope housing (natural shield) | LRF, display, processor |
| Filtered connectors | Ferrite beads on cable assemblies | Scope-to-body cable |
| Battery isolation | Isolated power supply in scope | Battery compartment |
| Low-emission design | Slow edge rates, proper grounding | PCB layout |

**EMC Test Estimate:** $5,000-8,000 (outsourced lab, 3-5 days)

---

# 5. MIL-STD-1472G HUMAN ENGINEERING

## 5.1 Applicable Requirements

| Clause | Topic | VDC-100 Requirement | Verification |
|--------|-------|---------------------|--------------|
| 5.6.1 | Control placement | All controls reachable from firing position | D: Operator assessment |
| 5.6.3 | Control force | Trigger 20-40 N (CUA-FOR-01) | T: Force gauge |
| 5.8.1 | Display legibility | ≥1000 nits sunlight readable (CUA-SIG-04) | T: Luminance meter |
| 5.8.5 | Warning indicators | Safety status LED (CUA-SIG-06) | D: Visual check |
| 5.9.1 | Anthropometry | Adjustable stock ±50 mm (CUA-ERG-02) | I: Measurement |
| 5.10.1 | Protective equipment | Gloved operation (CUA-ERG-04) | D: Winter glove test |

---

# 6. ADDITIONAL STANDARDS

## 6.1 IEC 60825-1 (Laser Safety)

| Parameter | Requirement | VDC-100 Design | Compliance |
|-----------|-------------|----------------|------------|
| Laser class | Class 1 (eye-safe) | COTS LRF module rated Class 1 | By design |
| Labeling | IEC 60825 warning label | Label on scope housing | I: Visual |
| Beam divergence | Per class limit | Module spec compliance | I: Datasheet |
| Aperture marking | Laser aperture identified | Marked on scope | I: Visual |

## 6.2 DOT-3AL / TCVN 6153 (Pressure Vessel)

| Parameter | Requirement | VDC-100 Design | Compliance |
|-----------|-------------|----------------|------------|
| Cylinder certification | DOT-3AL (US) or equivalent | Certified import cylinder | I: Cert review |
| Working pressure | Rated ≥300 bar | 300 bar cylinder | I: Marking |
| Hydrostatic test | Every 5 years | Per cylinder standard | D: Schedule |
| Transport marking | UN/DOT hazmat label | Applied per regulation | I: Visual |
| Vietnamese cert | TCVN 6153:1996 compliance | Registration with TCVN body | A: Documentation |

## 6.3 IP Rating (IEC 60529)

| Component | Target IP | Meaning | Verification |
|-----------|-----------|---------|--------------|
| Scope assembly | IP54 | Dust-protected, splash-proof | T: IP test |
| Barrel/breech | IP43 | Particle >1mm, rain-protected | T: IP test |
| Gas system | IP65 | Dust-tight, water jet (seals) | T: Pressure hold |
| Trigger group | IP43 | Basic dust/rain protection | T: Function after rain |

---

# 7. VERIFICATION PLAN SUMMARY

## 7.1 Verification Method Distribution

| Method | Code | Count | % of 89 Reqs | Estimated Cost | Duration |
|--------|------|-------|---------------|----------------|----------|
| **Analysis** (A) | A | 19 | 21% | $2,000 (eng. hours) | 2 weeks |
| **Inspection** (I) | I | 18 | 20% | $1,000 (measurement) | 1 week |
| **Test** (T) | T | 31 | 35% | $25,000-35,000 | 6-8 weeks |
| **Demonstration** (D) | D | 21 | 24% | $5,000 (field trials) | 2 weeks |
| **TOTAL** | | **89** | **100%** | **$33,000-43,000** | **~12 weeks** |

## 7.2 Test Program Breakdown

| Test Category | Methods | # Tests | Est. Cost | Facility |
|---------------|---------|---------|-----------|----------|
| Environmental (MIL-STD-810H) | 501,502,507,510,514,516,506,500,509 | 9 | $15,000-25,000 | External lab |
| Performance (ballistic) | Muzzle velocity, range, hit prob, reload | 8 | $5,000 | Internal range |
| Safety (MIL-STD-882E) | Pressure, drop, interlock, muzzle safety | 5 | $3,000 | Internal + lab |
| EMC (MIL-STD-461G) | RE102, RS103 | 2 | $5,000-8,000 | External lab |
| Human factors (MIL-STD-1472G) | Ergonomics assessment, training eval | 4 | $2,000 | Field |
| Ingress protection (IP) | IP54/IP43/IP65 | 3 | $3,000 | External lab |
| **TOTAL** | | **31** | **$33,000-43,000** | Mixed |

## 7.3 Test Facility Requirements

| Facility | Needed For | In-House? | External Option | Cost |
|----------|-----------|-----------|-----------------|------|
| Environmental chamber | Temp, humidity, alt | No | QUATEST or VIMCERT (Vietnam) | $15-25K |
| Ballistic range (outdoor) | Velocity, range, accuracy | Yes | Internal test area | $2K (setup) |
| EMC chamber | Emissions, susceptibility | No | EMC lab (Ho Chi Minh) | $5-8K |
| IP test rig | Dust, rain, water jet | No | QUATEST | $3K |
| Drop test fixture | MIL-STD-810 shock | No | QUATEST | Incl. in env. |

---

# 8. COMPLIANCE RISK ASSESSMENT

| Risk | Standard | Probability | Impact | Mitigation |
|------|----------|-------------|--------|------------|
| Humidity test fails (corrosion) | MIL-STD-810H 507 | Medium | High | Anodize all Al parts; seal electronics |
| EMC emissions exceed limit | MIL-STD-461G RE102 | Low | Medium | Shielded scope housing; ferrite beads |
| Drop test barrel deformation | MIL-STD-810H 516 | Low | High | Wall thickness margin; Al 6061-T6 |
| TCVN registration delayed | TCVN 6153 | Medium | Medium | Start registration early (Month 2) |
| Muzzle safety design complexity | MIL-STD-882E | Medium | Medium | Simple mechanical interlock preferred |
| IP54 scope seal leak | IEC 60529 | Low | Medium | O-ring + gasket design; test early |

---

# DOCUMENT LINKS

- [[01_requirements/requirements_list|Requirements List]]
- [[01_requirements/stakeholder_analysis|Stakeholder Analysis]]
- [[01_requirements/validation_report|Validation Report]]
- [[VN-CUA-001_product_spec|Master Product Specification]]

---

*This standards compliance matrix follows Pahl & Beitz Step 6, mapping all 89 requirements to applicable military and industry standards with verification methods.*
