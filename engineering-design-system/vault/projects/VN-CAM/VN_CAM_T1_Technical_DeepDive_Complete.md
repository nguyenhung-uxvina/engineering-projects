# VN-CAM-T1 "HUẤN LUYỆN VIÊN"
## AI TRAINING CAMERA - TECHNICAL DEEP-DIVE
### Complete Engineering & Product Specification

**Document Version:** 1.0  
**Classification:** CONFIDENTIAL  
**Framework:** D-M-I-R × ODI × Pahl-Beitz × Systems Thinking

---

## EXECUTIVE SUMMARY

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     VN-CAM-T1 "HUẤN LUYỆN VIÊN" - AI TRAINING CAMERA                        ║
║                                                                               ║
║     "Phát hiện lỗi kỹ thuật mà mắt huấn luyện viên không thể thấy"          ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║     PRIMARY JOB-TO-BE-DONE:                                                   ║
║     "Phát triển kỹ năng bắn súng thông qua phản hồi AI thời gian thực"       ║
║                                                                               ║
║     CORE DIFFERENTIATOR:                                                      ║
║     Detect and correct shooter errors BEFORE trigger pull,                    ║
║     not just report WHERE the shot landed                                     ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Product Overview

| Parameter | VN-CAM-T1-STD | VN-CAM-T1-PRO | VN-CAM-T1-MAX |
|-----------|---------------|---------------|---------------|
| **Price** | $2,200 | $2,700 | $3,200 |
| **Pose Detection** | 17-point | 17-point | 25-point |
| **Frame Rate** | 30 fps | 60 fps | 120 fps |
| **Feedback Latency** | <150ms | <100ms | <50ms |
| **Simultaneous Shooters** | 2 | 4 | 8 |
| **Flinch Detection** | Basic | Advanced | Premium + Custom |
| **LOMAH Integration** | Optional | Included | Included + Sync |
| **AAR System** | Basic | Advanced | Enterprise |

---

## PHẦN 1: SYSTEM ARCHITECTURE

### 1.1 Hardware Block Diagram

```
VN-CAM-T1 HARDWARE ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│                           VN-CAM-T1 UNIT                                     │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        SENSOR MODULE                                 │   │
│  │   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐         │   │
│  │   │  EO SENSOR   │    │   IR ARRAY   │    │     IMU      │         │   │
│  │   │  Sony IMX462 │    │  (Optional)  │    │   BMI270     │         │   │
│  │   │ 1920×1080    │    │  8×8 pixels  │    │  6-axis      │         │   │
│  │   │ 120fps max   │    │  Presence    │    │  Vibration   │         │   │
│  │   │ 0.001 lux    │    │  Detection   │    │  Monitoring  │         │   │
│  │   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘         │   │
│  │          └───────────────────┼───────────────────┘                  │   │
│  └──────────────────────────────┼──────────────────────────────────────┘   │
│                                 │                                           │
│                                 ▼                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      COMPUTE MODULE                                  │   │
│  │   ┌──────────────────────────────────────────────────────────────┐  │   │
│  │   │              NVIDIA JETSON ORIN NX (16GB)                    │  │   │
│  │   │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │   │
│  │   │  │ CPU         │  │ GPU         │  │ DLA         │          │  │   │
│  │   │  │ 8-core ARM  │  │ 1024 CUDA   │  │ 2× DLA      │          │  │   │
│  │   │  │ Cortex-A78  │  │ Ampere      │  │ AI Accel    │          │  │   │
│  │   │  │ 2.0 GHz     │  │ cores       │  │ 100 TOPS    │          │  │   │
│  │   │  └─────────────┘  └─────────────┘  └─────────────┘          │  │   │
│  │   │  Memory: 16GB LPDDR5 | Storage: 256GB NVMe | Power: 25W     │  │   │
│  │   └──────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  CONNECTIVITY: GbE + PoE | WiFi 6E (Option) | USB 3.2 Type-C       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  HOUSING: IP65 Polycarbonate | Dimensions: 180×120×80mm | Weight: 850g    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Software Stack

```
VN-CAM-T1 SOFTWARE ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│                        APPLICATION LAYER                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │   POSE      │  │   FLINCH    │  │   SAFETY    │  │    AAR      │       │
│  │  ANALYZER   │  │  DETECTOR   │  │   MONITOR   │  │  GENERATOR  │       │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘       │
├─────────────────────────────────────────────────────────────────────────────┤
│                           AI MODEL LAYER                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  POSE ESTIMATION: MoveNet Thunder (TensorRT FP16)                   │   │
│  │  FLINCH DETECTION: LSTM-based temporal analysis                     │   │
│  │  BEHAVIOR ANALYSIS: Stability, breathing, trigger anticipation      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────────────────┤
│                         FRAMEWORK LAYER                                      │
│  DeepStream 6.3 | TensorRT 8.6 | GStreamer 1.22 | OpenCV 4.8              │
├─────────────────────────────────────────────────────────────────────────────┤
│                         RUNTIME LAYER                                        │
│  JetPack 6.0 | CUDA 12.2 | cuDNN 8.9 | Ubuntu 22.04 LTS                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PHẦN 2: AI POSE ESTIMATION

### 2.1 17-Point Pose Model (COCO Format)

```
KEYPOINT MAPPING FOR MARKSMANSHIP ANALYSIS
═══════════════════════════════════════════════════════════════════════════════

                              ┌───┐
                              │ 0 │ Nose (Head position)
                              └─┬─┘
                    ┌───┐       │       ┌───┐
             L Eye │ 1 │───────┼───────│ 2 │ R Eye
                    └───┘       │       └───┘
                    ┌───┐       │       ┌───┐
             L Ear │ 3 │       │       │ 4 │ R Ear
                    └───┘       │       └───┘
                                │
                    ┌───┐     ┌─┴─┐     ┌───┐
          L Shoulder│ 5 │─────│   │─────│ 6 │ R Shoulder ← STANCE
                    └─┬─┘     └───┘     └─┬─┘
                      │                   │
                    ┌─┴─┐               ┌─┴─┐
            L Elbow │ 7 │               │ 8 │ R Elbow ← SUPPORT
                    └─┬─┘               └─┬─┘
                      │                   │
                    ┌─┴─┐               ┌─┴─┐
            L Wrist │ 9 │               │10 │ R Wrist ← TRIGGER HAND
                    └───┘               └───┘
                                │
                    ┌───┐     ┌─┴─┐     ┌───┐
              L Hip │11 │─────│   │─────│12 │ R Hip ← BALANCE
                    └─┬─┘     └───┘     └─┬─┘
                      │                   │
                    ┌─┴─┐               ┌─┴─┐
             L Knee │13 │               │14 │ R Knee
                    └─┬─┘               └─┬─┘
                      │                   │
                    ┌─┴─┐               ┌─┴─┐
            L Ankle │15 │               │16 │ R Ankle
                    └───┘               └───┘

CRITICAL KEYPOINTS FOR MARKSMANSHIP:
├── Shoulders (5, 6): Stance alignment, shoulder dip detection
├── Elbows (7, 8): Support arm position, proper platform
├── Wrists (9, 10): Trigger discipline, grip stability, FLINCH DETECTION
├── Hips (11, 12): Weight distribution, balance
├── Chest midpoint: Breathing pattern analysis
└── Nose (0): Head position, cheek weld consistency

═══════════════════════════════════════════════════════════════════════════════
```

### 2.2 Flinch Detection Algorithm

```
FLINCH DETECTION - LSTM TEMPORAL ANALYSIS
═══════════════════════════════════════════════════════════════════════════════

DEFINITION:
Flinch = Involuntary movement in anticipation of recoil

DETECTION APPROACH: LSTM-based Temporal Pattern Recognition

INPUT: 30-frame sequence (500ms @ 60fps)
├── 17 keypoints × 3 values (x, y, confidence) = 51 features
├── Derived features: velocity, acceleration = 8 features
└── Total: 59 dimensions per frame

LSTM ARCHITECTURE:
┌─────────────────────────────────────────────────────────────────────────────┐
│  Input: [batch, 30, 59]                                                     │
│     ↓                                                                       │
│  LSTM Layer 1: 128 units, return_sequences=True                            │
│  Dropout: 0.2                                                               │
│     ↓                                                                       │
│  LSTM Layer 2: 64 units, return_sequences=False                            │
│  Dropout: 0.2                                                               │
│     ↓                                                                       │
│  Dense: 32 units, ReLU                                                      │
│     ↓                                                                       │
│  Output: 3 units, Softmax                                                   │
│          [no_flinch, mild_flinch, severe_flinch]                           │
│                                                                             │
│  Model size: ~200KB (TensorRT optimized)                                   │
│  Inference: <5ms on Jetson Orin NX                                         │
└─────────────────────────────────────────────────────────────────────────────┘

DETECTION THRESHOLDS:
| Output | Probability | Action |
|--------|-------------|--------|
| No flinch | P > 0.7 | Green indicator, continue |
| Mild flinch | 0.3 < P < 0.7 | Yellow, coaching tip |
| Severe flinch | P > 0.7 | Red, immediate feedback |

ACCURACY TARGETS:
├── True Positive Rate (Sensitivity): ≥90%
├── True Negative Rate (Specificity): ≥95%
├── False Positive Rate: ≤5%
└── F1 Score: ≥0.92

═══════════════════════════════════════════════════════════════════════════════
```

### 2.3 AI Processing Pipeline

```
VN-CAM-T1 AI PIPELINE (Total latency: 40-75ms)
═══════════════════════════════════════════════════════════════════════════════

STAGE 1: VIDEO CAPTURE (0-5ms)
├── Sensor: IMX462 → V4L2 → GStreamer
└── Format: 1080p @ 60fps, NV12

STAGE 2: PREPROCESSING (5-10ms)
├── Color: NV12 → RGBA
├── Resize: 1920×1080 → 640×480 (inference)
└── Normalize: [0,255] → [0,1]

STAGE 3: POSE INFERENCE (15-25ms)
├── Model: MoveNet Thunder (TensorRT FP16)
├── Input: 640×480×3
├── Output: 17×3 (x, y, confidence)
└── Throughput: 60+ fps

STAGE 4: TRACKING (5-10ms)
├── Algorithm: DeepSORT
├── Association: IoU + appearance
└── ID persistence: >95%

STAGE 5: BEHAVIOR ANALYSIS (10-15ms)
├── Stability: Rolling variance
├── Flinch: LSTM temporal
├── Breathing: FFT of chest Y
└── Trigger: Wrist acceleration

STAGE 6: FEEDBACK GENERATION (5-10ms)
├── Visual: Skeleton overlay + alerts
├── Audio: Vietnamese coaching cues
└── Data: JSON event stream

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 3: LOMAH INTEGRATION

### 3.1 Integration Architecture

```
T1 + LOMAH/RAMS CORRELATION
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
│   VN-CAM-T1     │          │  NETWORK SWITCH │          │     LOMAH       │
│                 │          │                 │          │                 │
│  Pose Data      │◄────────►│  PTP Grand-     │◄────────►│  Impact Data    │
│  Timestamp: T1  │   GbE    │  master Clock   │   GbE    │  Timestamp: T2  │
└─────────────────┘          └─────────────────┘          └─────────────────┘
        │                                                         │
        └────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CORRELATION ENGINE                                   │
│                                                                             │
│   Match shot events by timestamp (<1ms PTP accuracy)                        │
│   Correlate pre-shot pose with impact location                              │
│   Build shooter-specific error model                                        │
│                                                                             │
│   OUTPUT: Combined report                                                   │
│   "Flinch detected (85% probability) → Impact: -5cm, -3cm low-left"        │
│   "Recommendation: Drill #3 - Trigger control exercise"                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

KEY INSIGHT:
Traditional: "WHERE did the shot land?" (impact only)
VN-CAM-T1: "WHY did the shot miss?" (pose + impact correlation)

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 4: ODI OPPORTUNITY ANALYSIS

### 4.1 Top Opportunities

```
VN-CAM-T1 OPPORTUNITY SCORES
═══════════════════════════════════════════════════════════════════════════════

Formula: Opportunity = Importance + MAX(Importance - Satisfaction, 0)

| ID | Outcome Statement | Imp | Sat | Opp | Priority |
|----|-------------------|-----|-----|-----|----------|
| T1-01 | Minimize delay between error and feedback | 9.5 | 3.0 | **16.0** | EXTREME ★ |
| T1-02 | Maximize flinch detection accuracy | 9.2 | 4.2 | **14.2** | HIGH |
| T1-03 | Minimize time to identify degrading technique | 8.8 | 3.5 | **14.1** | HIGH |
| T1-04 | Maximize pose-shot correlation | 9.0 | 4.5 | **13.5** | HIGH |
| T1-05 | Minimize false positive rate | 9.3 | 5.0 | **13.6** | HIGH |
| T1-13 | Maximize breathing pattern detection | 8.0 | 3.5 | **12.5** | HIGH |
| T1-14 | Minimize missed trigger anticipation | 8.5 | 4.0 | **13.0** | HIGH |

STRATEGIC INSIGHT:
├── T1-01 (16.0) = EXTREME opportunity → Sub-100ms latency as key differentiator
├── Cluster T1-02,03,04,13,14 = AI-powered technique analysis
└── No competitor offers pre-shot feedback → Blue ocean

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 5: COMPETITIVE POSITIONING

```
T1 vs COMPETITORS
═══════════════════════════════════════════════════════════════════════════════

| Feature | VN-CAM-T1-PRO | FATS 300S | Meggitt XWT | EST Range |
|---------|---------------|-----------|-------------|-----------|
| **Price** | $2,700 | $15,000+ | $12,000+ | $8,000+ |
| **AI Pose Analysis** | ✓ 17-point | ✗ | ✗ | ✗ |
| **Real-time Flinch** | ✓ <100ms | ✗ | ✗ | ✗ |
| **Breathing Analysis** | ✓ | ✗ | ✗ | ✗ |
| **Multi-shooter** | 4 | 1 | 1 | 2 |
| **Vietnamese Support** | ✓ Native | ✗ | ✗ | ✗ |
| **Local Service** | ✓ | ✗ | ✗ | ✗ |

COMPETITIVE MOAT:
1. AI Pose Analysis - Competitors don't have
2. Edge Processing - No cloud dependency
3. Indigenous Software - Vietnamese localization
4. Cost Structure - 60-80% lower price

POSITIONING: DOMINANT STRATEGY (Better AND Cheaper)

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 6: BILL OF MATERIALS

```
VN-CAM-T1-PRO BOM SUMMARY
═══════════════════════════════════════════════════════════════════════════════

| Category | Cost | % | Indigenous |
|----------|------|---|------------|
| Compute Module (Jetson Orin NX) | $450 | 30% | ✗ |
| Image Sensor (IMX462) | $120 | 8% | ✗ |
| PCB Assembly | $180 | 12% | ✓ |
| Housing | $80 | 5% | ✓ |
| Power Components | $60 | 4% | ✓ |
| Connectivity | $45 | 3% | ✓ |
| Optics (Lens) | $65 | 4% | ✗ |
| Mechanical Parts | $50 | 3% | ✓ |
| Cables & Connectors | $35 | 2% | ✓ |
| Software License | $200 | 13% | ✓ |
| Assembly & Test | $100 | 7% | ✓ |
| Packaging | $25 | 2% | ✓ |
| Contingency (5%) | $70 | 5% | - |
|**TOTAL BOM** | **$1,480** | 100% | **70%** |
| Selling Price | $2,700 | | |
| **Gross Margin** | **$1,220** | **45%** | |

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 7: REQUIREMENTS LIST (PAHL-BEITZ)

```
VN-CAM-T1 KEY REQUIREMENTS (D = Demand, W = Wish)
═══════════════════════════════════════════════════════════════════════════════

PERFORMANCE
├── D: Pose detection accuracy ≥95% all keypoints
├── D: Flinch detection accuracy ≥90%
├── D: False positive rate ≤5%
├── D: System latency ≤150ms (STD), ≤100ms (PRO)
├── D: Frame rate ≥30fps continuous
└── W: Frame rate ≥60fps (PRO/MAX)

GEOMETRY
├── D: Dimensions ≤200×150×100mm
├── D: Weight ≤1.5kg
├── D: FOV ≥90° horizontal
└── D: Operating range 2-10m

SIGNALS/CONTROL
├── D: Gigabit Ethernet (RJ45)
├── D: RTSP video streaming
├── D: MQTT for telemetry
├── D: PTP (IEEE 1588) for LOMAH sync
└── D: RESTful API

SAFETY
├── D: No active emissions interfering with range
├── D: Safety zone monitoring <500ms alert
└── D: IEC 62368-1 electrical safety

ENVIRONMENT
├── D: Operating temperature 0°C to 50°C
├── D: Humidity 10-90% RH non-condensing
├── D: IP65 ingress protection
└── D: MTBF ≥20,000 hours

COSTS
├── D: BOM ≤$1,500 (PRO)
├── D: 10-year TCO ≤50% of imports
└── W: Gross margin ≥40%

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 8: FEEDBACK LOOPS (SYSTEMS THINKING)

```
T1 SYSTEM DYNAMICS
═══════════════════════════════════════════════════════════════════════════════

REINFORCING LOOP R1: SKILL ACCELERATION
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│    Accurate AI Feedback → Faster Skill Development → Higher Training Value │
│           ↑                                                    ↓            │
│           │                                                    │            │
│    Better AI Algorithms ← More Training Data ← Increased Usage             │
│                                                                             │
│    VIRTUOUS CYCLE: More use → More data → Better AI → More value           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

BALANCING LOOP B1: COMPLEXITY BARRIER
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│    Advanced AI → Complex Setup → Operator Frustration → Reduced Adoption   │
│                                                                             │
│    SOLUTION: Auto-calibration, preset configurations (L5 - Rules)          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

BALANCING LOOP B2: TRUST EROSION
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│    False Positives → Instructor Skepticism → System Ignored → Value Lost   │
│                                                                             │
│    SOLUTION: Conservative thresholds, FPR <5% as hard requirement          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

LEVERAGE POINTS:
├── L3 (Goals): Shift from "record" to "accelerate skill"
├── L6 (Information): Centralized training data for AI improvement
├── L9 (Delays): <100ms feedback latency
└── L5 (Rules): Auto-calibration, preset configs

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 9: VIETNAMESE MNEMONICS

```
LEARNING AIDS FOR T1
═══════════════════════════════════════════════════════════════════════════════

MNEMONIC 1: "PHÁT HIỆN" - 7 Lỗi T1 Phát Hiện
──────────────────────────────────────────────────────────────────────────────
P - Phản xạ giật (Flinch)
H - Hơi thở sai nhịp (Breathing)
Á - Ấn cò quá mạnh (Trigger jerk)
T - Tư thế không vững (Stance)
H - Hướng súng lệch (Alignment)
I - Ỉu vai (Shoulder dip)
Ệ - Êm tay không đủ (Follow-through)
N - Nháy mắt (Eye blink)

MNEMONIC 2: "CAMERA" - 6 Bước Vận Hành
──────────────────────────────────────────────────────────────────────────────
C - Cài đặt (Setup)
A - Alignment (Căn chỉnh)
M - Mapping (Ánh xạ vùng an toàn)
E - Enroll (Đăng ký xạ thủ)
R - Run (Chạy huấn luyện)
A - Analyze (Phân tích AAR)

MNEMONIC 3: "AI-95" - Ngưỡng Chất Lượng
──────────────────────────────────────────────────────────────────────────────
A - Accuracy ≥95% (Pose)
I - Inference <25ms
9 - 90% flinch detection
5 - <5% false positive

═══════════════════════════════════════════════════════════════════════════════
```

---

## PHẦN 10: DEVELOPMENT TIMELINE

```
VN-CAM-T1 ROADMAP (2026)
═══════════════════════════════════════════════════════════════════════════════

Q1 2026: PROTOTYPE (Weeks 1-13)
├── W1-4: Platform setup (Jetson, sensor, DeepStream)
├── W5-8: AI pipeline (MoveNet, TensorRT, 30fps)
├── W9-12: Behavior analysis (stability, flinch LSTM)
└── W13: Milestone - Working prototype

Q2 2026: PILOT (Weeks 14-26)
├── W14-16: Production design review
├── W17-20: Small batch (10 units)
├── W21-26: Pilot deployment (2 sites)
└── W26: Milestone - 90% flinch accuracy, user sat >4.0

Q3-Q4 2026: PRODUCTION (Weeks 27-52)
├── W27-34: Manufacturing ramp (50 units)
├── W35-44: Market launch (STD, PRO variants)
├── W45-52: Expansion (MAX variant, LOMAH integration)
└── W52: Milestone - 150+ units shipped

YEAR 1 TARGET:
├── Units: 150+
├── Revenue: $375,000
├── Pilot satisfaction: >4.0/5.0
└── Flinch detection: 90%+ accuracy

═══════════════════════════════════════════════════════════════════════════════
```

---

## Document Summary

**VN-CAM-T1 Key Value Propositions:**

1. **Real-Time Pre-Shot Feedback** - Detect errors BEFORE trigger pull (<100ms)
2. **AI-Powered Technique Analysis** - 17-point pose estimation, flinch detection
3. **LOMAH Integration** - Correlate pose with impact for root cause analysis
4. **Cost Leadership** - $2,700 vs $12,000-15,000 imports (60-80% savings)
5. **Indigenous Software** - Vietnamese language, local support, data sovereignty

**Framework Integration:**

| Framework | Application |
|-----------|-------------|
| D-M-I-R | Diagnosis (ODI) → Modeling (Architecture) → Intervention (Design) → Reflection (Test) |
| ODI | 16.0 EXTREME opportunity at feedback latency |
| Pahl-Beitz | Complete requirements list, systematic design |
| Systems Thinking | R1 (skill acceleration), B1/B2 (barriers), leverage at L3/L6/L9 |
| Meta-Learning | Vietnamese mnemonics, operator curriculum |

---

*"Một huấn luyện viên AI không bao giờ mệt mỏi, không bao giờ bỏ sót lỗi."*

*VN-CAM-T1: Nâng cao năng lực bắn súng của lực lượng vũ trang Việt Nam.*
