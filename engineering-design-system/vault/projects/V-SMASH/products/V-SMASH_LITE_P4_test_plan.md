---
project: V-SMASH
product: LITE
designation: VSM-L
phase: 4
type: test_plan
version: 1.0
created: 2026-02-05
status: draft
---

# V-SMASH LITE - QUALIFICATION TEST PLAN
## Entry-Level AI Fire Control System

**Document ID:** VSM-L-TP-001
**Version:** 1.0
**Classification:** Restricted

---

## 1. TEST PLAN OVERVIEW

### 1.1 Purpose

This document defines the qualification test program for V-SMASH LITE (VSM-L) to verify compliance with 133 requirements specified in `V-SMASH_LITE_P1_requirements_list.md`.

### 1.2 Test Philosophy

| Principle | Description |
|-----------|-------------|
| **Test-to-Pass** | Demonstrate compliance under nominal conditions |
| **Design Margin** | Test at specification limits + 10% margin where applicable |
| **Early Testing** | Environmental screening before functional tests |
| **Witness Points** | Customer witness at key milestones |

### 1.3 Test Articles

| Article | Quantity | Configuration | Purpose |
|---------|----------|---------------|---------|
| DV-01 | 1 | Full production equivalent | Environmental qualification |
| DV-02 | 1 | Full production equivalent | Functional + accuracy |
| DV-03 | 1 | Instrumented | Recoil endurance |

### 1.4 Test Schedule

| Phase | Activity | Duration | Timeline |
|-------|----------|----------|----------|
| Pre-Test | Article preparation, calibration | 1 week | M9 W1 |
| Environmental | MIL-STD-810H tests | 3 weeks | M9 W2-4 |
| Functional | Performance verification | 2 weeks | M10 W1-2 |
| Endurance | Recoil, lifecycle | 2 weeks | M10 W3-4 |
| Accuracy | Range firing trials | 1 week | M11 W1 |
| Report | Data analysis, documentation | 1 week | M11 W2 |

---

## 2. ENVIRONMENTAL QUALIFICATION TESTS

### 2.1 Temperature Tests (MIL-STD-810H)

#### 2.1.1 High Temperature Operating (Method 501.7)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-OPR-01: -10°C to +55°C operating |
| **Test Temperature** | +55°C (+60°C with margin) |
| **Duration** | 4 hours at temperature |
| **Procedure** | Procedure I (Storage) + Procedure II (Operation) |

**Pass Criteria:**
- [ ] System powers on within 30 seconds
- [ ] Detection accuracy ≥95% at +55°C
- [ ] Fire solution latency ≤100ms
- [ ] No physical damage or deformation

#### 2.1.2 Low Temperature Operating (Method 502.7)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-OPR-01: -10°C to +55°C operating |
| **Test Temperature** | -10°C (-15°C with margin) |
| **Duration** | 4 hours at temperature |
| **Procedure** | Procedure I (Storage) + Procedure II (Operation) |

**Pass Criteria:**
- [ ] System powers on within 60 seconds
- [ ] Battery provides ≥4 hours operation at -10°C
- [ ] Display remains readable
- [ ] No condensation on optics after warm-up

#### 2.1.3 Storage Temperature (Method 501.7/502.7)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-TRA-01: -40°C to +70°C storage |
| **Test Temperatures** | -40°C and +70°C |
| **Duration** | 24 hours each extreme |

**Pass Criteria:**
- [ ] No physical damage after storage
- [ ] Full functionality restored after 2-hour stabilization

### 2.2 Humidity Test (Method 507.6)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-OPR-02: 95% RH non-condensing |
| **Test Condition** | 95% RH at +40°C |
| **Duration** | 10 cycles (24 hours each) |
| **Procedure** | Procedure II (Aggravated) |

**Pass Criteria:**
- [ ] No corrosion on electrical contacts
- [ ] IP65 sealing maintained
- [ ] All functions operational post-test

### 2.3 Dust/Water Ingress (IP65 Verification)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-OPR-03: IP65 rating |
| **Dust Test** | IEC 60529 - Dust tight (6) |
| **Water Test** | IEC 60529 - Water jets (5) |

#### 2.3.1 Dust Test (IP6X)

| Parameter | Value |
|-----------|-------|
| **Dust Type** | Talcum powder or cement |
| **Duration** | 8 hours in dust chamber |
| **Pressure** | 20 mbar below atmospheric |

**Pass Criteria:**
- [ ] No dust penetration to internal components
- [ ] Optics remain clear
- [ ] All seals intact

#### 2.3.2 Water Jet Test (IPX5)

| Parameter | Value |
|-----------|-------|
| **Nozzle** | 6.3mm diameter |
| **Flow Rate** | 12.5 L/min |
| **Distance** | 2.5-3m |
| **Duration** | 3 minutes all surfaces |

**Pass Criteria:**
- [ ] No water ingress to electronics
- [ ] Display remains functional
- [ ] Battery compartment dry

### 2.4 Shock Test (Method 516.8)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-OPR-04, L-FOR-04 |
| **Procedure** | Procedure I (Functional Shock) |
| **Peak Acceleration** | 40g |
| **Pulse Duration** | 11ms (half-sine) |
| **Axes** | 3 axes, both directions (6 total) |
| **Shocks per Axis** | 3 |

**Pass Criteria:**
- [ ] No structural damage
- [ ] Optical alignment within ±1 mrad
- [ ] All functions operational post-shock

#### 2.4.1 Drop Test

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-FOR-04: 1.5m drop onto concrete |
| **Height** | 1.5m |
| **Surface** | Concrete slab (50mm min) |
| **Orientations** | 6 faces + 4 corners (10 drops) |

**Pass Criteria:**
- [ ] Housing intact (minor cosmetic damage acceptable)
- [ ] Optics uncracked
- [ ] Full functionality after drop sequence

### 2.5 Vibration Test (Method 514.8)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-OPR-05, L-TRA-04 |
| **Category** | Category 20 (Ground vehicle) |
| **Procedure** | Procedure I (General) |

| Frequency Range | Level |
|-----------------|-------|
| 5-15 Hz | 0.04 g²/Hz |
| 15-100 Hz | +3 dB/octave to 0.04 g²/Hz |
| 100-500 Hz | -3 dB/octave |

| Parameter | Value |
|-----------|-------|
| **Duration** | 1 hour per axis (3 axes) |
| **Fixture** | Picatinny rail mounted |

**Pass Criteria:**
- [ ] No loosening of fasteners
- [ ] No resonance-induced failures
- [ ] Optical alignment maintained ±0.5 mrad
- [ ] All functions operational during vibration

---

## 3. RECOIL ENDURANCE TESTS (NEW)

### 3.1 Purpose

Verify V-SMASH LITE maintains full functionality after extended exposure to weapon recoil forces typical of supported calibers.

### 3.2 Test Configuration

| Parameter | Value |
|-----------|-------|
| **Test Article** | DV-03 (instrumented unit) |
| **Instrumentation** | Tri-axial accelerometer (100g range) |
| **Data Acquisition** | 50 kHz sample rate |
| **Mounting** | Production Picatinny clamp at 3.5 Nm |

### 3.3 5.56×45mm NATO Recoil Endurance (L-FOR-01)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-FOR-01: Functional after 10,000 rounds |
| **Test Weapon** | M16A4 or equivalent |
| **Ammunition** | M855 Ball (standard issue) |
| **Total Rounds** | 10,000 |
| **Firing Rate** | Semi-auto, 10 rounds/minute |
| **Inspection Intervals** | Every 2,000 rounds |

#### 3.3.1 Expected Recoil Profile

| Parameter | Value |
|-----------|-------|
| **Peak Acceleration** | 15-25g |
| **Pulse Duration** | 5-8ms |
| **Direction** | Primarily rearward (X-axis) |

#### 3.3.2 Inspection Protocol (Every 2,000 rounds)

| Check | Method | Pass Criteria |
|-------|--------|---------------|
| Visual inspection | Examine housing, mounts | No cracks, loose parts |
| Optical alignment | Boresight target | Within ±1 mrad |
| Fastener torque | Torque wrench | 3.5 Nm ±10% |
| Functional test | Power cycle + track | All functions nominal |
| Zero verification | 25m zero target | POI within 2 MOA |

#### 3.3.3 Pass Criteria (10,000 rounds)

- [ ] No structural failures (housing, mount, fasteners)
- [ ] Optical alignment drift ≤2 mrad cumulative
- [ ] All electronic functions operational
- [ ] Battery contacts intact
- [ ] Sensor (IMU, camera) functional
- [ ] Solenoid response <5ms maintained

### 3.4 7.62×39mm / 7.62×51mm Recoil Endurance (L-FOR-02)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-FOR-02: Functional after 5,000 rounds |
| **Test Weapon** | AK-47 (7.62×39) or M240 (7.62×51) |
| **Ammunition** | Standard ball |
| **Total Rounds** | 5,000 |
| **Firing Rate** | Semi-auto, 10 rounds/minute |
| **Inspection Intervals** | Every 1,000 rounds |

#### 3.4.1 Expected Recoil Profile

| Parameter | 7.62×39mm | 7.62×51mm |
|-----------|-----------|-----------|
| **Peak Acceleration** | 25-35g | 30-45g |
| **Pulse Duration** | 6-10ms | 8-12ms |

#### 3.4.2 Pass Criteria (5,000 rounds)

- [ ] No structural failures
- [ ] Optical alignment drift ≤3 mrad cumulative
- [ ] All electronic functions operational
- [ ] Mount clamp secure (no slippage)

### 3.5 Accelerated Life Test (Optional)

| Parameter | Value |
|-----------|-------|
| **Method** | Shaker table simulation |
| **Profile** | Synthesized recoil waveform |
| **Repetitions** | 50,000 equivalent cycles |
| **Duration** | ~8 hours |

**Note:** Accelerated testing may be used to supplement live-fire testing if range time is limited.

---

## 4. TRIGGER MECHANISM TESTS (NEW)

### 4.1 Solenoid Force Verification (L-FOR-05)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-FOR-05: 5-15N output force |
| **Test Method** | Force gauge measurement |
| **Measurement Points** | At 0mm, 2mm, 4mm stroke |

#### 4.1.1 Test Procedure

1. Mount unit in fixture with trigger linkage attached
2. Attach calibrated force gauge to trigger interface
3. Command solenoid actuation
4. Record peak force at each stroke position
5. Repeat 10 times, calculate mean and std dev

#### 4.1.2 Pass Criteria

| Stroke Position | Min Force | Max Force |
|-----------------|-----------|-----------|
| 0mm (initial) | 8N | 15N |
| 2mm (mid) | 6N | 12N |
| 4mm (full) | 5N | 10N |

- [ ] Force within 5-15N range at all positions
- [ ] Response time <5ms (command to motion)
- [ ] Consistent force (σ <10% of mean)

### 4.2 Trigger Timing Precision (L-FCS-02)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-FCS-02: ≤5ms trigger precision |
| **Test Method** | High-speed camera (1000 fps) |
| **Measurement** | Command-to-actuation delay |

#### 4.2.1 Test Procedure

1. Generate known fire command signal
2. Record solenoid motion with high-speed camera
3. Measure delay from command to solenoid motion start
4. Repeat 100 times across temperature range

#### 4.2.2 Pass Criteria

| Condition | Max Delay | Max Jitter (σ) |
|-----------|-----------|----------------|
| +25°C (ambient) | 4ms | 0.5ms |
| +55°C (hot) | 5ms | 1.0ms |
| -10°C (cold) | 5ms | 1.0ms |

- [ ] Mean delay ≤4ms at ambient
- [ ] Worst-case delay ≤5ms across temperature range
- [ ] Jitter (standard deviation) ≤1ms

### 4.3 Solenoid Endurance Test

| Parameter | Value |
|-----------|-------|
| **Cycles** | 100,000 actuations |
| **Duty Cycle** | 1 Hz (1 second on/off) |
| **Duration** | ~28 hours |

**Pass Criteria:**
- [ ] Force degradation <10% from initial
- [ ] Response time degradation <20%
- [ ] No mechanical failure

---

## 5. MOUNTING INTERFACE TESTS (NEW)

### 5.1 Mounting Torque Verification (L-FOR-03)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-FOR-03: 2-5 Nm torque on rail clamp |
| **Test Method** | Torque wrench + slip test |

#### 5.1.1 Test Procedure

1. Mount unit on MIL-STD-1913 test rail
2. Torque clamp to specified value (2, 3, 4, 5 Nm)
3. Apply lateral force until slip occurs
4. Record slip force for each torque setting

#### 5.1.2 Pass Criteria

| Clamp Torque | Min Lateral Slip Force |
|--------------|------------------------|
| 2 Nm | 50N |
| 3 Nm | 75N |
| 4 Nm | 100N |
| 5 Nm | 125N |

- [ ] Unit secure (no slip) at ≥3 Nm under recoil
- [ ] Unit removable without damage at ≤5 Nm
- [ ] Rail interface undamaged after 100 mount/dismount cycles

### 5.2 Optical Axis Alignment (Post-Mount)

| Parameter | Value |
|-----------|-------|
| **Requirement** | Tolerance analysis: ±0.5 mrad |
| **Test Method** | Collimator + boresight |

**Pass Criteria:**
- [ ] Optical axis parallel to bore within ±0.5 mrad
- [ ] Repeatability after remount: ±0.3 mrad

---

## 6. FUNCTIONAL PERFORMANCE TESTS

### 6.1 Detection Performance

| Test | Requirement | Method | Pass Criteria |
|------|-------------|--------|---------------|
| Drone detection range | L-DET-01: ≥300m | Range trial | Detect DJI Mavic at 300m |
| Detection accuracy | L-DET-03: ≥95% | Test dataset | ≥95% TP on 1000 images |
| False positive rate | L-DET-04: ≤10% | Test dataset | ≤10% FP on 1000 images |
| Detection latency | L-DET-07: ≤30ms | Instrumented | Mean <30ms per frame |
| Classification | L-DET-06: 3 class | Test dataset | Drone/Person/Vehicle |

### 6.2 Tracking Performance

| Test | Requirement | Method | Pass Criteria |
|------|-------------|--------|---------------|
| Track lock probability | L-TRK-01: ≥90% | Moving target | ≥90% lock on 100 attempts |
| Track maintenance | L-TRK-02: ≥95% | 60s track | ≥95% continuous track |
| Multi-target | L-TRK-05: ≥5 | Simulated | Track 5 simultaneous |
| Tracking jitter | L-TRK-04: ≤2 mrad | Stationary target | RMS jitter ≤2 mrad |

### 6.3 Fire Control Performance

| Test | Requirement | Method | Pass Criteria |
|------|-------------|--------|---------------|
| Fire solution latency | L-FCS-01: ≤100ms | Instrumented | End-to-end <100ms |
| Trigger precision | L-FCS-02: ≤5ms | High-speed camera | Jitter <5ms |
| Engagement time | L-FCS-05: ≤5s | Stopwatch | Acquisition to shot <5s |

### 6.4 Accuracy Trials (Range)

| Test | Requirement | Method | Pass Criteria |
|------|-------------|--------|---------------|
| Hit improvement | L-FCS-03: ≥3x | Comparative | 3x vs iron sights |
| First-round Pk @ 200m | L-FCS-04: ≥60% | Moving target | ≥60% hits |

#### 6.4.1 Range Trial Protocol

| Parameter | Value |
|-----------|-------|
| **Target** | Drone surrogate (0.3m wingspan) |
| **Motion** | 10 m/s crossing, random pattern |
| **Range** | 200m |
| **Rounds** | 50 engagements |
| **Shooter** | Trained operator (4-hour course) |
| **Weapon** | M16A4, 5.56mm |

**Pass Criteria:**
- [ ] ≥30/50 first-round hits (60% Pk)
- [ ] Mean rounds per kill ≤2 (with AI)
- [ ] Mean rounds per kill baseline ≥6 (iron sights)

---

## 7. EMC TESTS (MIL-STD-461G)

### 7.1 Radiated Emissions (RE102)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-SAF-05 |
| **Frequency Range** | 10 kHz - 18 GHz |
| **Limit** | Per MIL-STD-461G Figure RE102-2 |

**Pass Criteria:**
- [ ] Emissions below limit at all frequencies
- [ ] No narrowband spikes >6 dB above limit

### 7.2 Radiated Susceptibility (RS103)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-SAF-05 |
| **Frequency Range** | 2 MHz - 18 GHz |
| **Field Strength** | 20 V/m (ground) |

**Pass Criteria:**
- [ ] No malfunction during exposure
- [ ] No false triggers or detections
- [ ] Display readable throughout

---

## 8. SAFETY TESTS

### 8.1 Human-in-the-Loop Verification (L-SAF-01)

| Test | Method | Pass Criteria |
|------|--------|---------------|
| No autonomous fire | Remove trigger pressure | No fire without human input |
| Trigger required | Software analysis | HITL enforced in code |
| Override available | Functional test | Manual mode accessible |

### 8.2 Fail-Safe Verification (L-SAF-02)

| Test | Method | Pass Criteria |
|------|--------|---------------|
| Power loss | Remove battery | Trigger mechanically free |
| Software crash | Force exception | Solenoid releases |
| Processor hang | Watchdog timeout | Safe state achieved |

### 8.3 Battery Safety (L-SAF-07)

| Test | Requirement | Pass Criteria |
|------|-------------|---------------|
| UN38.3 certification | L-SAF-07 | Certificate on file |
| Overcharge protection | Safety | BMS prevents overcharge |
| Short circuit protection | Safety | Fuse/PTC limits current |

---

## 9. RELIABILITY ASSESSMENT

### 9.1 MTBF Verification (L-QUA-01)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-QUA-01: ≥1,500 hours MTBF |
| **Method** | MIL-HDBK-217F parts count |
| **Environment** | Ground, mobile (GM) |

**Pass Criteria:**
- [ ] Predicted MTBF ≥1,500 hours
- [ ] No failures during 200-hour burn-in (3 units)

### 9.2 Design Life (L-QUA-04)

| Parameter | Value |
|-----------|-------|
| **Requirement** | L-QUA-04: 10 years |
| **Method** | Analysis + accelerated aging |

**Pass Criteria:**
- [ ] Component derating adequate for 10-year life
- [ ] No life-limited components <10 years (except battery)

---

## 10. TEST MATRIX SUMMARY

| Test Category | Tests | Duration | Articles | Cost Est. |
|---------------|-------|----------|----------|-----------|
| Environmental | 8 | 3 weeks | DV-01 | $8,000 |
| Recoil Endurance | 3 | 2 weeks | DV-03 | $5,000 |
| Trigger/Mount | 4 | 1 week | DV-02 | $2,000 |
| Functional | 12 | 1 week | DV-02 | $3,000 |
| Accuracy (Range) | 2 | 1 week | DV-02 | $5,000 |
| EMC | 2 | 1 week | DV-01 | $4,000 |
| Safety | 6 | 3 days | DV-02 | $1,000 |
| Reliability | 2 | Analysis | — | $2,000 |
| **TOTAL** | **39** | **~10 weeks** | **3 units** | **$30,000** |

---

## 11. TEST REPORTS

### 11.1 Deliverables

| Report | Content | Delivery |
|--------|---------|----------|
| Environmental Test Report | MIL-STD-810H results | M10 W1 |
| Recoil Endurance Report | Round counts, inspections | M10 W4 |
| Functional Test Report | Performance data | M10 W3 |
| Accuracy Trial Report | Range results, Pk data | M11 W1 |
| EMC Test Report | MIL-STD-461G results | M10 W2 |
| **Qualification Summary** | All results, compliance | M11 W2 |

### 11.2 Non-Conformance Handling

| Severity | Definition | Action |
|----------|------------|--------|
| Critical | Safety or core function failure | Stop test, root cause, redesign |
| Major | Requirement not met | Document, engineering review |
| Minor | Marginal compliance | Document, accept with waiver |

---

## 12. APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Author | | | |
| Test Lead | | | |
| Program Manager | | | |
| Customer Rep | | | |

---

## REVISION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-05 | Initial test plan. Added recoil endurance tests (L-FOR-01, L-FOR-02), trigger force verification (L-FOR-05), mounting torque tests (L-FOR-03). Total 39 tests, 10-week schedule, $30K budget. |

---

*Requirements Source: [[V-SMASH_LITE_P1_requirements_list|LITE Requirements List v1.0]]*
*Product Spec: [[V-SMASH_LITE_product_spec|LITE Product Specification v1.1]]*
