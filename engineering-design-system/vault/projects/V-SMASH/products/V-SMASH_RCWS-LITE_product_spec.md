---
project: V-SMASH
product: RCWS-LITE
designation: VSM-RL
version: 1.0
created: 2026-02-04
status: approved
vdi_score: 83%
target_price: $8,000
---

# V-SMASH RCWS-LITE - PRODUCT SPECIFICATION
## Single-Soldier Portable Remote Weapon Station

**Product Code:** VSM-RL
**VDI 2225 Score:** 83% ✅
**Target Price:** $8,000
**Delivery:** Phase 2 (Month 26)

**Key Differentiator:** "Can be carried, assembled and operated by a single soldier"

---

## PHASE 1: REQUIREMENTS

### 1.1 Product-Specific Requirements

| Req ID | Category | Requirement | Value | Type | Source |
|--------|----------|-------------|-------|------|--------|
| **R100** | **Physical** | **System weight (excl. weapon)** | **≤10 kg** | **D** | **Hopper Light** |
| **R101** | **Weapon** | **Weapons supported** | **7.62-12.7mm** | **D** | **Versatility** |
| **R102** | **Setup** | **Setup personnel** | **1 person** | **D** | **Key diff** |
| **R103** | **Setup** | **Setup time** | **<60 seconds** | **D** | **Rapid deploy** |
| **R104** | **Deploy** | **Tripod type** | **Folding** | **D** | **Portable** |
| **R105** | **Control** | **RCU cable length** | **≥50m** | **D** | **Standoff** |
| **R106** | **Power** | **Operation time** | **≥4 hours** | **D** | **Mission** |
| **R107** | **Environ** | **Climate** | **Vietnam tropical** | **D** | **Local** |
| R08 | Platform | Pan range | ±120° | D | Limited |
| R09 | Platform | Tilt range | -20° to +45° | D | Limited |
| R10 | Platform | Slew rate | ≥20°/sec | D | Manual feel |
| R11 | Platform | Stabilization | Passive | D | Simplicity |
| R12 | Video | Resolution | 1080p | D | Standard |
| R13 | Video | Latency | <150ms | D | R97 |
| R14 | Environ | Sealing | IP65 | D | Field |
| R15 | Safety | Human-in-the-loop | Mandatory | D | Legal |

### 1.2 RCWS-LITE vs RCWS Comparison

| Feature | RCWS-LITE | RCWS | LITE Advantage |
|---------|-----------|------|----------------|
| Weight | ≤10 kg | ≤15 kg | Portable |
| Setup personnel | 1 | 2 | Single-soldier |
| Setup time | <60 sec | Pre-installed | Rapid deploy |
| Pan range | ±120° | 360° | Simpler drive |
| Stabilization | Passive | Gyro 2-axis | Lower cost |
| External cue | None | CoT | Standalone |
| Auto-scan | None | Sector scan | Manual control |
| Deployment | Folding tripod | Fixed mount | Expeditionary |
| Price | $8,000 | $12,000 | Lower cost |

---

## PHASE 2: CONCEPTUAL DESIGN

### 2.1 Function Structure (RCWS-LITE)

```
V-SMASH RCWS-LITE FUNCTION STRUCTURE
═══════════════════════════════════════════════════════════════

F1-F7: CORE FCS FUNCTIONS (Inherited from PRO)
├── F1: Acquire target information
├── F2: Track target motion
├── F3: Compute fire solution
├── F4: Control fire authorization
├── F5: Actuate trigger mechanism
├── F6: Provide operator feedback
└── F7: Coordinate multi-target

F8: RCWS PLATFORM CONTROL (LITE Version)
├── F8.1: Control pan axis ───────────── Brushless servo, ±120°
├── F8.2: Control tilt axis ──────────── Brushless servo, -20°/+45°
├── F8.3: Stabilize weapon ───────────── Passive (friction damped)
├── F8.4: Stream video remotely ──────── H.264, 1080p, <150ms
├── F8.5: Receive operator commands ──── Wired RCU (50m)
├── F8.6: Accept external cue ────────── NONE (standalone)
├── F8.7: Execute auto-scan ──────────── NONE (manual only)
└── F8.8: Provide portable deploy ────── Folding tripod system

F_DEPLOY: PORTABLE DEPLOYMENT (RCWS-LITE Unique)
├── F_DEPLOY.1: Carry system ─────────── Single-soldier carry
├── F_DEPLOY.2: Unfold tripod ────────── Tool-free, <30 sec
├── F_DEPLOY.3: Mount weapon ─────────── Quick-attach, <20 sec
├── F_DEPLOY.4: Connect RCU ──────────── Single cable, <10 sec
└── F_DEPLOY.5: Tear down ────────────── Reverse, <60 sec total
```

### 2.2 Working Principles Selected

| Function | Working Principle | Specification |
|----------|------------------|---------------|
| F8.1/8.2 | WP-014: BLDC Servo | Smaller motors, 20°/sec |
| F8.3 | Passive stabilization | Friction damped, no gyro |
| F8.4 | WP-016: H.264 IP | Wired only, <150ms |
| F8.5 | WP-017: Wired RCU | 50m cable, 5" display |
| F8.8 | WP-020: Folding tripod | 3 kg, 0.5-1.2m height |

---

## PHASE 3: EMBODIMENT DESIGN

### 3.1 System Layout

```
V-SMASH RCWS-LITE - SYSTEM COMPONENTS
═══════════════════════════════════════════════════════════════

COMPONENT 1: WEAPON PLATFORM (4 kg)
┌─────────────────────────────────────────────────────────────┐
│                    PAN/TILT HEAD                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ┌───────────┐  ┌───────────────────────────────┐  │    │
│  │  │ PAN MOTOR │  │ TILT MOTOR + WEAPON CRADLE    │  │    │
│  │  │ (±120°)   │  │ (-20° to +45°)                │  │    │
│  │  └───────────┘  └───────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  FCS MODULE (V-SMASH PRO core)                      │    │
│  │  • CMOS + Thermal  • Jetson Nano  • IMU            │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘

COMPONENT 2: FOLDING TRIPOD (3 kg)
┌─────────────────────────────────────────────────────────────┐
│  DEPLOYED                      FOLDED                        │
│                                                              │
│      ●────────●                    ╲                         │
│     /│\      /│\                    ╲╱                       │
│    / │ \    / │ \                   ╱╲                       │
│   /  │  \  /  │  \                 ╱  ╲                      │
│  ●───●───●───●───●                ╱────╲                     │
│                                  (collapsed)                 │
│  Height: 0.5-1.2m               Length: 0.6m                │
│  Footprint: 0.8m dia            Weight: 3 kg                │
└─────────────────────────────────────────────────────────────┘

COMPONENT 3: REMOTE CONTROL UNIT (1.5 kg)
┌─────────────────────────────────────────────────────────────┐
│  ┌─────────────────────────────────────────────────────┐    │
│  │                 5" LCD DISPLAY                       │    │
│  │                 (1080p video)                        │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐     │
│  │ PAN/TILT    │  │ TRIGGER     │  │ MODE            │     │
│  │ JOYSTICK    │  │ (safety)    │  │ SELECTOR        │     │
│  └─────────────┘  └─────────────┘  └─────────────────┘     │
│                    50m CABLE TO PLATFORM                    │
└─────────────────────────────────────────────────────────────┘

COMPONENT 4: BATTERY PACK (1.5 kg)
┌─────────────────────────────────────────────────────────────┐
│  BB-2590 Military Battery (28V)                             │
│  Runtime: >4 hours                                          │
│  Quick-change: Tool-free                                    │
└─────────────────────────────────────────────────────────────┘

TOTAL SYSTEM: 10 kg (meets R100)
```

### 3.2 Setup Sequence (<60 seconds)

| Step | Action | Time | Notes |
|------|--------|------|-------|
| 1 | Unfold tripod | 15 sec | Quick-lock legs |
| 2 | Level platform | 5 sec | Bubble level |
| 3 | Mount weapon | 15 sec | Quick-attach |
| 4 | Connect cable | 10 sec | Single connector |
| 5 | Power on + verify | 15 sec | Self-test |
| **TOTAL** | | **<60 sec** | Single soldier |

### 3.3 DfX Review

| DfX Category | Score | Notes |
|--------------|-------|-------|
| DfM | 8/10 | Simple design, fewer parts |
| DfA | 9/10 | Tool-free assembly |
| DfR | 8/10 | Fewer failure modes |
| DfT | 8/10 | Simple function test |
| DfC | 9/10 | Lower cost than RCWS |
| DfE | 7/10 | IP65, tropical rated |
| DfMaint | 9/10 | Field-replaceable modules |
| **OVERALL** | **8.3/10** | Excellent for production |

---

## PHASE 4: DETAIL DESIGN

### 4.1 Bill of Materials Summary

| Component | Cost | Weight |
|-----------|------|--------|
| FCS Module (PRO core) | $1,400 | 1.5 kg |
| Pan/Tilt drives | $400 | 1.5 kg |
| Weapon cradle | $150 | 0.5 kg |
| Platform housing | $200 | 0.5 kg |
| Folding tripod | $200 | 3.0 kg |
| Remote Control Unit | $300 | 1.0 kg |
| Cable (50m) | $100 | 0.5 kg |
| Battery (BB-2590) | $150 | 1.5 kg |
| **SUBTOTAL** | **$2,900** | **10 kg** |
| Labor + Test | $400 | |
| Software | $200 | |
| **TOTAL** | **$2,800** | |

### 4.2 Local Content Analysis

| Category | Local | Import |
|----------|-------|--------|
| FCS Module | $350 | $1,050 |
| Drives | $100 | $300 |
| Mechanical | $550 | $0 |
| RCU | $150 | $150 |
| Cable | $100 | $0 |
| Battery | $0 | $150 |
| Labor | $400 | $0 |
| Software | $200 | $0 |
| **TOTAL** | **$1,850** (66%) | **$1,650** (34%) |

**Local Content: 66%** ✅ Meets ≥60% target

### 4.3 Production Plan

| Phase | Activity | Timeline | Volume |
|-------|----------|----------|--------|
| Pilot | 5 units | M24-25 | 5 |
| LRIP | 20 units | M26-28 | 20 |
| FRP | 60/year | M29+ | 60/yr |

### 4.4 Target Markets

| Market | Volume Est. | Use Case |
|--------|-------------|----------|
| Infantry rapid deployment | 150 units | Forward positions |
| Expeditionary forces | 50 units | Deployed operations |
| Special operations | 30 units | Covert positions |
| Export | 70 units | ASEAN, Middle East |

---

## DOCUMENT LINKS

- [[V-SMASH_PRO_product_spec|PRO Specification]] (FCS core)
- [[V-SMASH_RCWS_product_spec|RCWS Specification]] (full version)
- [[V-SMASH_RE_08_SMASH_HopperLight_analysis|Hopper Light RE Analysis]]
- [[V-SMASH_P2_02_morphological_matrix|Morphological Matrix v1.3]]
