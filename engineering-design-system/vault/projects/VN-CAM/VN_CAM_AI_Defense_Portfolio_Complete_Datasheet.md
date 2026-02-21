# VN-CAM AI DEFENSE CAMERA PORTFOLIO
## DANH MỤC SẢN PHẨM HỆ THỐNG CAMERA AI QUỐC PHÒNG

**Vietnam Defense Industry Corporation**  
**Viện Kỹ thuật Hải quân - Xưởng Sản xuất - Chế thử**

---

**Document Version:** 2.0  
**Date:** February 2026  
**Classification:** CONFIDENTIAL  
**Reference:** VN-CAM-SERIES-2026

---

## EXECUTIVE SUMMARY

Dòng sản phẩm VN-CAM là hệ sinh thái camera AI bản địa hóa đầu tiên của Việt Nam dành cho ứng dụng quốc phòng/an ninh. Với 7 sản phẩm trải dài từ huấn luyện bắn đạn thật đến giám sát biên giới và điều khiển hỏa lực, portfolio này mang lại:

| Chỉ số chiến lược | Giá trị |
|-------------------|---------|
| Tiết kiệm chi phí so với nhập khẩu | 60-90% |
| Tỷ lệ nội địa hóa | 55-95% |
| Thị trường tiềm năng/năm | $17-24M |
| Điểm hòa vốn | Năm 2, Q3 |
| Lợi nhuận năm thứ 3 | 30%+ |

**Vision Statement:** *"MẮT CỦA QUỐC PHÒNG VIỆT NAM"* - Hệ sinh thái camera AI bản địa mang lại độc lập chiến lược trong giám sát & an ninh.

---

## TABLE OF CONTENTS

1. [Product Portfolio Overview](#1-product-portfolio-overview)
2. [VN-CAM-T1 "HUẤN LUYỆN VIÊN"](#2-vn-cam-t1-huấn-luyện-viên)
3. [VN-CAM-B1 "LÍNH GÁC"](#3-vn-cam-b1-lính-gác)
4. [VN-CAM-S1 "BIÊN PHÒNG"](#4-vn-cam-s1-biên-phòng)
5. [VN-CAM-M1 "HẢI ÂU"](#5-vn-cam-m1-hải-âu)
6. [VN-CAM-D1 "DRONE EYE"](#6-vn-cam-d1-drone-eye)
7. [VN-CAM-W1 "CHIẾN BINH"](#7-vn-cam-w1-chiến-binh)
8. [VN-CAM-C1 "CHỈ HUY"](#8-vn-cam-c1-chỉ-huy)
9. [Platform Architecture](#9-platform-architecture)
10. [Integration Matrix](#10-integration-matrix)
11. [Implementation Roadmap](#11-implementation-roadmap)
12. [Cost Comparison Analysis](#12-cost-comparison-analysis)
13. [Appendices](#13-appendices)

---

## 1. PRODUCT PORTFOLIO OVERVIEW

### 1.1 Product Family Structure

```
VN-CAM PRODUCT FAMILY
├── Phase 1 (P1) - Foundation Products
│   ├── VN-CAM-T1 "HUẤN LUYỆN VIÊN" - AI Training Coach
│   └── VN-CAM-B1 "LÍNH GÁC" - Base Guardian
│
├── Phase 2 (P2) - Scale Products  
│   ├── VN-CAM-S1 "BIÊN PHÒNG" - Border Sentinel
│   ├── VN-CAM-M1 "HẢI ÂU" - Maritime Watch
│   └── VN-CAM-D1 "DRONE EYE" - UAV Payload
│
├── Phase 3 (P3) - Platform Products
│   ├── VN-CAM-W1 "CHIẾN BINH" - Weapon Sight
│   └── VN-CAM-C1 "CHỈ HUY" - Command Platform
│
└── Common Platform Architecture
    ├── AI Software Stack (100% Indigenous)
    ├── Compute Module Options (Jetson Family)
    ├── Sensor Modules (Interchangeable)
    └── Communication Modules (Multi-Protocol)
```

### 1.2 Portfolio Summary Table

| Product | Name | Price (USD) | Market/yr | Indigenous | Phase | Priority |
|---------|------|-------------|-----------|------------|-------|----------|
| VN-CAM-T1 | HUẤN LUYỆN VIÊN | $2,200-3,200 | 500 | 70% | P1 | ★★★★★ |
| VN-CAM-B1 | LÍNH GÁC | $1,800-4,500 | 2,000+ | 70% | P1 | ★★★★★ |
| VN-CAM-S1 | BIÊN PHÒNG | $10,000-18,000 | 200-500 | 65% | P2 | ★★★★☆ |
| VN-CAM-M1 | HẢI ÂU | $15,000-25,000 | 100-200 | 60% | P2 | ★★★★☆ |
| VN-CAM-D1 | DRONE EYE | $1,500-5,000 | 500+ | 65% | P2 | ★★★☆☆ |
| VN-CAM-W1 | CHIẾN BINH | $15,000-35,000 | 50-100 | 55% | P3 | ★★★☆☆ |
| VN-CAM-C1 | CHỈ HUY | $50,000+ | 20-50 | 95% | P3 | ★★★★☆ |

### 1.3 Strategic Positioning

```
                    HIGH CUSTOMIZATION
                           │
    VN-CAM-W1 ★           │           ★ VN-CAM-M1
    (Weapon Sight)        │           (Maritime)
                          │
    VN-CAM-S1 ★           │
    (Border)              │
                          │
LOW VOLUME ─────────────────────────────────────── HIGH VOLUME
                          │
                          │           ★ VN-CAM-D1
    VN-CAM-C1 ★           │           (Drone Eye)
    (Command)             │
                          │           ★ VN-CAM-T1
                          │           (Training)
                          │
                          │           ★ VN-CAM-B1
                          │           (Base Security)
                    LOW CUSTOMIZATION
```

---

## 2. VN-CAM-T1 "HUẤN LUYỆN VIÊN"
### AI Training Coach - Camera Huấn Luyện Thông Minh

**Product Code:** VN-CAM-T1  
**Category:** Infantry Combat Training  
**Priority:** P1 (Phase 1 Foundation)

### 2.1 Product Overview

**Mục đích:** Số hóa trường bắn, phân tích kỹ thuật xạ thủ, đảm bảo an toàn tuyệt đối

**Key Functions:**
- **Phân tích tư thế:** Theo dõi 17 điểm khung xương, chấm điểm độ ổn định
- **Giám sát an toàn:** Tự động phát hiện xâm nhập vùng nguy hiểm, kích hoạt ngừng bắn <0.5s
- **AAR (After Action Review):** Tự động cắt clip, đánh dấu lỗi, phát lại tức thì

### 2.2 Technical Specifications

#### 2.2.1 Sensor Module

| Component | Option 1 (Low Light) | Option 2 (High Detail) |
|-----------|---------------------|------------------------|
| Sensor | Sony IMX462 (2MP Starvis) | Sony IMX415 (8MP/4K) |
| Resolution | 1920×1080 @ 60fps | 3840×2160 @ 30fps |
| Sensitivity | 0.001 Lux (Color) | 0.01 Lux (Color) |
| Dynamic Range | 120dB WDR | 72dB HDR |
| Pixel Size | 2.9µm | 1.45µm |
| Use Case | Night/indoor training | Outdoor detailed analysis |

#### 2.2.2 Optics

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Lens Type | Motorized Varifocal | Remote focus/zoom |
| Focal Length | 2.8-12mm | 4× zoom range |
| Aperture | F1.6 | Low-light optimized |
| Field of View | 108°-33° (H) | Wide to narrow |
| IR Cut Filter | Auto Day/Night | ICR mechanism |
| Distortion | <3% | Barrel corrected |

#### 2.2.3 AI Processing Module

| Parameter | Specification | Verification |
|-----------|---------------|--------------|
| Processor | NVIDIA Jetson Orin Nano | D |
| AI Performance | 20-40 TOPS | T |
| Latency | <50ms (inference) | T |
| Memory | 8GB LPDDR5 | D |
| Storage | 64GB eMMC + SD slot | D |
| Power Consumption | <15W | T |

#### 2.2.4 AI Capabilities

| Function | Performance | Standard |
|----------|-------------|----------|
| Pose Detection | 17-point skeleton | OpenPose/MediaPipe |
| Person Detection | 95% @ 50m | COCO benchmark |
| Pose Classification | 8 shooting positions | Custom trained |
| Safety Zone Violation | <0.5s detection | Real-time |
| Shot Detection | Integration with LOMAH | External sync |
| Flinch Detection | Pre-trigger analysis | Proprietary algorithm |

#### 2.2.5 Connectivity & Interface

| Interface | Specification | Notes |
|-----------|---------------|-------|
| Network | Gigabit Ethernet (PoE+) | IEEE 802.3at |
| Video Output | RTSP, ONVIF Profile S | Streaming |
| Data Output | JSON/MQTT | Real-time telemetry |
| I/O | 2× Relay (NO/NC) | Alarm/trigger |
| Audio | 2-way (speaker/mic) | Coach communication |
| Sync | GPIO + PTP | LOMAH integration |

#### 2.2.6 Environmental

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Operating Temp | -10°C to +55°C | MIL-STD-810H Method 501/502 |
| Storage Temp | -40°C to +70°C | MIL-STD-810H |
| Humidity | 5-95% RH (non-condensing) | MIL-STD-810H Method 507 |
| Ingress Protection | IP66 | IEC 60529 |
| Vibration | 5-500Hz, 2G | MIL-STD-810H Method 514 |
| EMC | Class B | FCC Part 15, MIL-STD-461G |

#### 2.2.7 Physical

| Parameter | Specification |
|-----------|---------------|
| Housing Material | Aluminum die-cast (ADC12) |
| Finish | Powder coat (RAL 6031 Bronze Green) |
| Dimensions | 180×90×80mm (L×W×H) |
| Weight | 1.2kg (camera only) |
| Mounting | Wall/Pole (adjustable bracket) |
| Cable Entry | M20 gland, IP68 |

### 2.3 Configuration Options

| Config | Components | Price (USD) |
|--------|------------|-------------|
| T1-STD | Camera + Bracket + Basic AI | $2,200 |
| T1-PRO | + Speaker/Alarm + Advanced AI | $2,700 |
| T1-MAX | + LOMAH Integration + AAR Suite | $3,200 |

### 2.4 Integration with Defense Portfolio

```
VN-CAM-T1 INTEGRATION MAP
│
├── VN-SAMT-001 (Small Arms Simulator)
│   └── Provides: Pose validation, technique analysis
│
├── LOMAH System
│   └── Receives: Shot timing for correlation
│   └── Provides: Impact data for AAR
│
├── RAMS (Real-Time AI Marksmanship System)
│   └── Bi-directional: Shared AI models, combined feedback
│
└── VN-CAM-C1 (Command Platform)
    └── Provides: Telemetry, video streams, alerts
```

### 2.5 Standards Compliance

| Standard | Description | Status |
|----------|-------------|--------|
| MIL-STD-810H | Environmental Engineering | ✓ Compliant |
| MIL-STD-461G | EMC Requirements | ✓ Compliant |
| TCVN 6611 | Electrical Safety | ✓ Certified |
| TCVN 7568 | IP Rating | ✓ IP66 Verified |

### 2.6 Competitive Comparison

| Feature | VN-CAM-T1 | FATS/Meggitt | Cubic MILES |
|---------|-----------|--------------|-------------|
| AI Pose Analysis | ✓ | Limited | ✗ |
| Real-time Safety | <0.5s | 1-2s | N/A |
| Vietnamese Posture DB | ✓ | ✗ | ✗ |
| LOMAH Integration | Native | Custom | Custom |
| Price | $2,200-3,200 | $15,000+ | $12,000+ |
| Local Support | ✓ | ✗ | ✗ |

---

## 3. VN-CAM-B1 "LÍNH GÁC"
### Base Guardian - Camera An Ninh Căn Cứ

**Product Code:** VN-CAM-B1  
**Category:** Base/Perimeter Security  
**Priority:** P1 (Phase 1 Foundation)

### 3.1 Product Overview

**Mục đích:** Bảo vệ chủ động doanh trại, kho tàng, thay thế lính gác tại các điểm trọng yếu

**Key Functions:**
- **Bảo vệ chu vi:** Phát hiện xâm nhập hàng rào ảo, phân biệt người/động vật
- **Kiểm soát ra vào:** Nhận diện khuôn mặt, biển số quân sự/dân sự
- **Giám sát nhiệt:** Phát hiện mục tiêu ẩn trong bóng tối, sương mù, ngụy trang

### 3.2 Technical Specifications

#### 3.2.1 Visible (EO) Sensor

| Parameter | B1-FX/PT | B1-DU |
|-----------|----------|-------|
| Sensor | Sony IMX335 (5MP) | Sony IMX485 (8MP) |
| Resolution | 2592×1944 @ 25fps | 3840×2160 @ 30fps |
| WDR | 120dB | 130dB |
| Sensitivity | 0.005 Lux | 0.003 Lux |
| IR Illumination | 850nm, 50m range | 940nm (covert), 80m |

#### 3.2.2 Thermal Sensor (B1-TH, B1-DU variants)

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Detector | Uncooled VOx Microbolometer | FLIR/domestic |
| Resolution | 256×192 (standard) | 640×512 optional |
| Pixel Pitch | 12µm | Compact design |
| NETD | <50mK | High sensitivity |
| Spectral Range | 8-14µm | LWIR |
| Frame Rate | 25Hz | Export compliant |

#### 3.2.3 Detection Performance

| Target | EO (Day) | EO (Night+IR) | Thermal |
|--------|----------|---------------|---------|
| Person | 150m | 100m | 200m |
| Vehicle | 300m | 200m | 500m |
| Face Recognition | 30m | 20m | N/A |
| License Plate | 50m | 30m | N/A |

#### 3.2.4 AI Capabilities

| Function | Performance | Notes |
|----------|-------------|-------|
| Person Detection | 98% @ 100m | Deep learning |
| Vehicle Classification | 95% (8 classes) | Military/civilian |
| Face Recognition | 99.5% FAR<0.001% | VN face database |
| License Plate (VN) | 98% | Military+civilian formats |
| Intrusion Detection | <1s response | Virtual fence |
| Loitering Detection | Configurable dwell | 10-300 seconds |
| Person/Animal Discrimination | 97% | Reduce false alarms |

#### 3.2.5 PTZ Mechanism (B1-PT variant)

| Parameter | Specification |
|-----------|---------------|
| Pan Range | 360° continuous |
| Tilt Range | -20° to +90° |
| Pan Speed | 0.1-150°/s |
| Tilt Speed | 0.1-60°/s |
| Preset Accuracy | ±0.1° |
| Presets | 256 positions |
| Auto-Track | Speed matching to 30 km/h |

#### 3.2.6 Environmental

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Operating Temp | -20°C to +60°C | MIL-STD-810H |
| Humidity | 95% RH (condensing) | Tropical optimized |
| Ingress Protection | IP67 | Submersible 1m/30min |
| Vandal Resistance | IK10 | 20J impact |
| Wind Load | Grade 7 (17 m/s) | PTZ operational |
| Lightning Protection | 6kV surge | Direct/indirect |

### 3.3 Variant Matrix

| Variant | Sensor | PTZ | Use Case | Price (USD) |
|---------|--------|-----|----------|-------------|
| B1-FX | 5MP EO | Fixed | Wide FOV perimeter | $1,800 |
| B1-PT | 5MP EO | 360° | Area patrol, tracking | $3,500 |
| B1-TH | 256×192 Thermal | Fixed | Night/adverse weather | $2,800 |
| B1-DU | 8MP EO + 256×192 TH | PTZ | Premium full capability | $4,500 |

### 3.4 Power Options

| Option | Specification | Use Case |
|--------|---------------|----------|
| PoE+ | IEEE 802.3at (30W) | Standard installation |
| DC Input | 12V/24V DC (±25%) | Vehicle/battery |
| Solar Kit | 100W panel + 100Ah LiFePO4 | Remote sites |

### 3.5 Integration with Defense Portfolio

```
VN-CAM-B1 INTEGRATION MAP
│
├── VN-CAM-C1 (Command Platform)
│   └── Primary: VMS integration, alerting
│
├── Access Control Systems
│   └── Bi-directional: Face/plate verification
│
├── Perimeter Intrusion Detection (PIDS)
│   └── Trigger: Camera follows PIDS alarm
│
└── VN-CDS-001 (Combat Direction System)
    └── Optional: Base defense integration
```

---

## 4. VN-CAM-S1 "BIÊN PHÒNG"
### Border Sentinel - Camera Giám Sát Biên Giới

**Product Code:** VN-CAM-S1  
**Category:** Border/Strategic Surveillance  
**Priority:** P2 (Phase 2 Scale)

### 4.1 Product Overview

**Mục đích:** Giám sát biên giới, đường mòn, hoạt động tự chủ không cần lưới điện

**Key Functions:**
- **Giám sát tầm xa:** 3-5km giám sát liên tục ngày/đêm
- **Tự chủ năng lượng:** Solar + pin dự phòng 72 giờ
- **Truyền thông minh:** AI lọc dữ liệu, chỉ gửi cảnh báo qua 4G/vệ tinh

### 4.2 Technical Specifications

#### 4.2.1 EO Channel

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Sensor | Sony IMX485 (8MP/4K) | Starvis II |
| Optical Zoom | 30-50× motorized | High magnification |
| Digital Zoom | 16× (total 800×) | Enhanced detail |
| Focal Length | 6.5-325mm | Wide to telephoto |
| Aperture | F1.5-4.8 | Auto iris |
| Image Stabilization | Optical + Electronic | 3-axis compensation |

#### 4.2.2 Thermal Channel

| Parameter | Standard | Premium |
|-----------|----------|---------|
| Detector | FLIR Tau 2 (336×256) | FLIR Boson (640×512) |
| Pixel Pitch | 17µm | 12µm |
| NETD | <30mK | <20mK |
| Focal Length | 35mm (standard) | 50-100mm (long range) |
| Digital Zoom | 4× | 8× |

#### 4.2.3 DRI Performance (NATO Standard)

| Target | Detect | Recognize | Identify |
|--------|--------|-----------|----------|
| Person (EO) | 3 km | 1.5 km | 0.8 km |
| Person (TH) | 3 km | 1 km | 0.5 km |
| Vehicle (EO) | 6 km | 3 km | 1.5 km |
| Vehicle (TH) | 6 km | 2 km | 1 km |

#### 4.2.4 PTZ Mechanism

| Parameter | Specification |
|-----------|---------------|
| Pan Range | 360° continuous |
| Tilt Range | -45° to +90° |
| Pan Speed | 0.01-80°/s (precision mode) |
| Tilt Speed | 0.01-40°/s |
| Position Accuracy | ±0.02° |
| Pointing Stability | <50 µrad RMS |
| Wind Resistance | Grade 8 (20 m/s) operational |

#### 4.2.5 Power System (S1-SOLAR)

| Component | Specification |
|-----------|---------------|
| Solar Panel | 200-400W Mono-crystalline |
| Battery | LiFePO4 100-200Ah |
| MPPT Controller | 30A, 98% efficiency |
| Autonomy (no sun) | 72 hours continuous |
| Charge Time | 8 hours (0-80%) |
| Battery Life | >3000 cycles (80% DoD) |

#### 4.2.6 Communication

| Interface | Specification | Use Case |
|-----------|---------------|----------|
| 4G LTE | Dual-SIM failover | Primary link |
| Satellite | Iridium Certus (S1-SATCOM) | Remote/backup |
| WiFi | 802.11ac (AP mode) | Local maintenance |
| Ethernet | Gigabit (fiber optional) | Grid sites |

#### 4.2.7 Environmental

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Operating Temp | -20°C to +60°C | Extended range |
| Humidity | 95% RH | Tropical |
| Ingress Protection | IP67 | All-weather |
| Wind Load | 60 m/s survival | Extreme conditions |
| Lightning | 20kV surge protection | Direct strike |
| Altitude | 0-4000m | Border highlands |

### 4.3 Variant Matrix

| Variant | Configuration | Price (USD) |
|---------|---------------|-------------|
| S1-STD | EO+TH, Grid power | $10,000 |
| S1-SOLAR | + Solar power system | $14,000 |
| S1-SATCOM | + Satellite communication | $18,000 |
| S1-LRF | + Laser Rangefinder 5km | +$2,000 |

### 4.4 System Deployment Cost

| Coverage | Units | Equipment | Installation | Total/km |
|----------|-------|-----------|--------------|----------|
| Open border | 1 per 3km | $14,000 | $4,000 | $6,000/km |
| Forested | 1 per 1.5km | $14,000 | $5,000 | $12,700/km |
| **Comparison** | Import equivalent | | | $50,000-80,000/km |

---

## 5. VN-CAM-M1 "HẢI ÂU"
### Maritime Watch - Camera Giám Sát Biển

**Product Code:** VN-CAM-M1  
**Category:** Maritime/Naval Surveillance  
**Priority:** P2 (Phase 2 Scale)

### 5.1 Product Overview

**Mục đích:** Mắt của Biển Đông - chuyên dụng cho nhà giàn DK1, đảo tiền tiêu, tàu tuần tra

**Key Functions:**
- **Chống ăn mòn:** Bền bỉ trong môi trường phun muối, độ ẩm 100%
- **Phân loại tàu:** AI nhận diện tàu cá, tàu quân sự, tàu hàng. Đối sánh AIS (phát hiện "tàu tối")
- **Ổn định hình ảnh:** Chống rung cho gắn tàu tuần tra (M1-Ship)

### 5.2 Technical Specifications

#### 5.2.1 Corrosion Protection

| Component | Protection | Standard |
|-----------|------------|----------|
| Housing | Marine-grade Al 6061-T6 | MIL-A-8625 Type III |
| Coating | Military polyurethane | MIL-DTL-64159 |
| Fasteners | 316L Stainless Steel | ASTM A276 |
| Connectors | Hermetic sealed | MIL-DTL-38999 |
| Salt Spray | >500 hours | ASTM B117 |

#### 5.2.2 Sensor Performance

| Parameter | M1-P (Platform) | M1-S (Ship) | M1-C (Coastal) |
|-----------|-----------------|-------------|----------------|
| EO Resolution | 4K (8MP) | 4K (8MP) | 4K (8MP) |
| Optical Zoom | 30× | 40× | 50× |
| Thermal | 640×512 uncooled | 640×512 cooled | 640×512 cooled |
| NETD | <40mK | <25mK | <20mK |
| Detection (large ship) | 15 km | 20 km | 25 km |
| Detection (small boat) | 3 km | 5 km | 8 km |

#### 5.2.3 Stabilization (M1-S Ship Variant)

| Parameter | Specification |
|-----------|---------------|
| Type | 3-axis Gyro-stabilized |
| LOS Stability | <100 µrad RMS |
| Angular Rate | Up to 30°/s ship motion |
| Compensation | Roll ±30°, Pitch ±20° |
| Settling Time | <2 seconds |

#### 5.2.4 Maritime AI Capabilities

| Function | Performance | Notes |
|----------|-------------|-------|
| Vessel Detection | 95% @ 10km | Multiple targets |
| Vessel Classification | 8 classes, 90% accuracy | Military/civilian |
| AIS Correlation | Automatic matching | Dark vessel alert |
| Horizon Tracking | Auto-stabilize | Sea/sky line |
| Sea Clutter Reduction | Adaptive filtering | Wave noise |
| Wake Detection | Small boat tracking | IR channel |

#### 5.2.5 Environmental (Maritime-Specific)

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Operating Temp | -10°C to +55°C | MIL-STD-810H |
| Salt Fog | 720 hours continuous | MIL-STD-810H Method 509 |
| Humidity | 100% RH (condensing) | Tropical maritime |
| Ingress Protection | IP68 | 3m submersible |
| Shock | 40G, 11ms half-sine | Ship shock |
| Vibration | 20-2000Hz, 4G RMS | Ship vibration |

### 5.3 Variant Matrix

| Variant | Application | Features | Price (USD) |
|---------|-------------|----------|-------------|
| M1-P | Platform/Island | Solar, mesh network | $15,000 |
| M1-S | Ship-mounted | Gyro-stabilized | $25,000 |
| M1-C | Coastal station | Long-range optics, VTS | $18,000 |

### 5.4 Integration with Naval Systems

```
VN-CAM-M1 INTEGRATION MAP
│
├── VN-NGS-001 (Naval Gunnery Simulator)
│   └── Provides: Target tracking data for training
│
├── VN-CDS-001 (Combat Direction System)
│   └── Bi-directional: COP integration, fire control
│
├── VTS (Vessel Traffic Service)
│   └── Provides: AIS correlation, traffic monitoring
│
├── Target USV
│   └── Provides: Remote target observation
│
└── VN-CAM-C1 (Command Platform)
    └── Centralized: All maritime cameras
```

---

## 6. VN-CAM-D1 "DRONE EYE"
### UAV Payload - Module Camera Cho UAV

**Product Code:** VN-CAM-D1  
**Category:** UAV/UGV Payloads  
**Priority:** P2 (Phase 2 Scale)

### 6.1 Product Overview

**Mục đích:** Module camera nhẹ, thông minh cho UAV và UGV

**Key Functions:**
- **Trinh sát:** Chụp ảnh trên không, tự động khóa và theo dõi mục tiêu di động
- **Tối ưu băng thông:** AI xử lý tại chỗ, chỉ truyền metadata (tọa độ mục tiêu)
- **Hỗ trợ dẫn đường:** Hỗ trợ UAV hạ cánh chính xác hoặc UGV tránh vật cản

### 6.2 Technical Specifications

#### 6.2.1 Weight Budget

| Component | D1-EO | D1-DU | D1-AI |
|-----------|-------|-------|-------|
| Camera Assembly | 180g | 280g | 280g |
| Gimbal | 150g | 180g | 180g |
| AI Processor | - | - | 40g |
| Total Weight | 330g | 460g | 500g |
| Target Weight | <350g | <500g | <500g |

#### 6.2.2 Sensor Specifications

| Parameter | EO Only | Dual (EO+TH) |
|-----------|---------|--------------|
| EO Sensor | Sony IMX477 (12.3MP) | Sony IMX477 |
| EO Resolution | 4056×3040 @ 30fps | 4056×3040 @ 30fps |
| Thermal Sensor | - | FLIR Lepton 3.5 (160×120) |
| Thermal NETD | - | <50mK |

#### 6.2.3 Gimbal Performance

| Parameter | Specification |
|-----------|---------------|
| Axes | 3-axis stabilization |
| Control Range | Roll ±45°, Pitch -90° to +30°, Yaw ±320° |
| Angular Vibration | <0.01° RMS |
| Control Accuracy | ±0.01° |
| Slew Rate | 60°/s max |

#### 6.2.4 Interface & Communication

| Interface | Specification | Notes |
|-----------|---------------|-------|
| Flight Controller | MAVLink 2.0, UART | Standard UAV protocol |
| Video Out | HDMI, Ethernet (IP) | Dual output |
| Control | PWM, S.Bus, CAN | Gimbal control |
| Power Input | 10-26V DC | 2S-6S LiPo compatible |
| Power Consumption | <15W (peak 20W) | Battery optimized |

#### 6.2.5 AI Features (D1-AI variant)

| Function | Performance |
|----------|-------------|
| Object Detection | 20 classes, 90% @ 100m AGL |
| Object Tracking | Continuous lock, 10 targets |
| Geo-tagging | <5m CEP (with GPS) |
| Smart Compression | 10× bandwidth reduction |
| Landing Assist | <1m precision approach |

### 6.3 Variant Matrix

| Variant | Configuration | Weight | Price (USD) |
|---------|---------------|--------|-------------|
| D1-EO | EO camera + 3-axis gimbal | <350g | $1,500 |
| D1-DU | EO + Thermal + gimbal | <500g | $3,500 |
| D1-AI | Dual sensor + AI processor | <500g | $5,000 |

### 6.4 Integration with UAV Systems

```
VN-CAM-D1 INTEGRATION MAP
│
├── Target UAV
│   └── Payload for target identification
│
├── Transport (Cargo) Drone
│   └── Navigation and obstacle avoidance
│
├── VN-UAV-001 (UAV Training System)
│   └── Simulated payload for training
│
├── Tethered Drone
│   └── Persistent surveillance payload
│
└── Ground Control Station
    └── Real-time video and AI alerts
```

---

## 7. VN-CAM-W1 "CHIẾN BINH"
### Weapon Sight - Hệ Thống Ngắm Bắn Điện Quang

**Product Code:** VN-CAM-W1  
**Category:** Fire Control & Weapon Integration  
**Priority:** P3 (Phase 3 Platform)

### 7.1 Product Overview

**Mục đích:** Hệ thống ngắm điện quang tích hợp với súng máy, pháo, RCWS

**Key Functions:**
- **Hỗ trợ bắn:** Tự động tính đạn đạo, điểm ngắm trước cho mục tiêu di động
- **An toàn (HITL):** AI chỉ gợi ý và hỗ trợ, con người giữ quyền khai hỏa. Cơ chế khóa cứng phần cứng
- **Chống giật:** Chịu được giật liên tục của vũ khí 12.7mm+

### 7.2 Technical Specifications

#### 7.2.1 Optical Performance

| Parameter | W1-V (Vehicle) | W1-R (RCWS) | W1-N (Naval) |
|-----------|----------------|-------------|--------------|
| EO FOV | 40°×30° (wide) / 4°×3° (narrow) | 36°×27° / 3°×2.25° | 30°×22.5° / 2°×1.5° |
| Magnification | 1-12× continuous | 1-15× | 1-20× |
| Thermal | 640×512, 12µm | 640×512, 12µm | 1024×768, 10µm (cooled) |
| LRF Range | 50m - 3km | 50m - 5km | 100m - 10km |
| LRF Accuracy | ±3m | ±2m | ±1m |

#### 7.2.2 Ruggedness

| Parameter | Specification | Standard |
|-----------|---------------|----------|
| Shock Resistance | 500G, 11ms half-sine | MIL-STD-810H Method 516 |
| Vibration | 10-2000Hz, 7.7G RMS | MIL-STD-810H Method 514 |
| Recoil Cycles | >100,000 | 12.7mm equivalent |
| Operating Temp | -32°C to +52°C | MIL-STD-810H |
| Ingress Protection | IP67 | All-weather combat |

#### 7.2.3 Fire Control Computer

| Function | Performance |
|----------|-------------|
| Ballistic Calculation | <100ms update |
| Lead Angle (moving target) | Auto-computed |
| Crosswind Compensation | Integrated sensor |
| Zero Storage | 16 weapon profiles |
| Target Tracking | <0.5 mrad accuracy |

#### 7.2.4 Stabilization

| Parameter | Specification |
|-----------|---------------|
| Type | 2-axis (azimuth + elevation) |
| LOS Stability | <100 µrad RMS |
| Compensation | Platform motion up to 20°/s |
| Settling Time | <1 second |

#### 7.2.5 Safety Features (CRITICAL)

| Feature | Implementation |
|---------|----------------|
| Human-in-the-Loop | Hardware interlock required |
| Fire Inhibit | Physical disconnect |
| AI Role | Suggest only, no autonomous fire |
| Override | Manual at all times |
| Audit Log | All engagements recorded |

### 7.3 Variant Matrix

| Variant | Application | Price (USD) |
|---------|-------------|-------------|
| W1-V | Vehicle weapon station | $15,000 |
| W1-R | Remote Controlled Weapon Station | $20,000 |
| W1-N | Naval gun director | $35,000 |
| W1-A | Air Defense (AA tracking) | $25,000 |

### 7.4 Integration with Weapon Systems

```
VN-CAM-W1 INTEGRATION MAP
│
├── 12.7mm Remote Controlled Weapon Station
│   └── Primary: Fire control, tracking
│
├── Machine Gun Mount System
│   └── Optional: Upgraded sighting
│
├── VN-NGS-001 (Naval Gunnery Simulator)
│   └── Simulated integration
│
├── VN-MAT-001 (MANPADS Trainer)
│   └── Tracking subsystem
│
└── VN-CAM-C1 (Command Platform)
    └── Battle damage assessment
```

### 7.5 **CRITICAL SAFETY STATEMENT**

```
╔═══════════════════════════════════════════════════════════════════╗
║                    HUMAN-IN-THE-LOOP MANDATORY                      ║
║                                                                     ║
║  • AI CANNOT autonomously fire weapons under any circumstance       ║
║  • Hardware fire inhibit must be engaged by human operator          ║
║  • All AI suggestions require human confirmation                    ║
║  • System logs all engagements for accountability                   ║
║  • Compliant with CCW Protocol on Autonomous Weapons                ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 8. VN-CAM-C1 "CHỈ HUY"
### Command Platform - Nền Tảng Quản Lý Tập Trung

**Product Code:** VN-CAM-C1  
**Category:** Software Platform & C4ISR Integration  
**Priority:** P3 (Phase 3 Platform)

### 8.1 Product Overview

**Mục đích:** Phần mềm quản lý tập trung, đa nhiệm, bảo mật cao

**Key Functions:**
- **VMS:** Quản lý hàng nghìn camera trên bản đồ số (GIS)
- **AI Analytics:** Tổng hợp dữ liệu từ camera biên giới, nhận dạng mẫu hành vi, tái nhận diện qua camera
- **Bảo mật:** Truyền mã hóa, kiểm soát truy cập đa cấp, xác minh tính toàn vẹn dữ liệu

### 8.2 Technical Specifications

#### 8.2.1 Architecture

| Component | Specification |
|-----------|---------------|
| Architecture | Server-Client, Cluster support |
| Scalability | 64 - 10,000+ cameras |
| Redundancy | Active-passive failover |
| Database | PostgreSQL + TimescaleDB |
| OS | Linux (Hardened Ubuntu LTS) |

#### 8.2.2 Security

| Feature | Implementation |
|---------|----------------|
| Architecture | Zero-Trust |
| Transport | TLS 1.3 (mutual auth) |
| Data at Rest | AES-256 encryption |
| Authentication | Multi-factor, LDAP/AD |
| Access Control | Role-based (RBAC) |
| Audit | Complete logging, tamper-evident |

#### 8.2.3 AI Analytics Engine

| Function | Performance |
|----------|-------------|
| Cross-camera Tracking | Re-ID accuracy 85%+ |
| Pattern Recognition | Anomaly detection |
| Face Search | 1:N search in <1 second (100K faces) |
| License Plate Search | Full database in <0.5 second |
| Alert Correlation | Multi-sensor fusion |

#### 8.2.4 Integration Standards

| Standard | Description | Support |
|----------|-------------|---------|
| ONVIF | Camera interoperability | Profile S, T, G |
| CoT (Cursor-on-Target) | Tactical data exchange | MIL-STD-2525D |
| VMF | Variable Message Format | NATO standard |
| OGC | GIS services | WMS, WFS, WMTS |

#### 8.2.5 Modules

| Module | Function | Included |
|--------|----------|----------|
| VMS Core | Camera management (64-256) | Base package |
| AI Analytics | Cross-camera tracking, patterns | Optional |
| Alert Management | Real-time dashboard, escalation | Included |
| C4ISR Connector | COP feed, tactical integration | Optional |
| Mobile App | iOS/Android remote access | Included |
| Report Generator | Automatic reports, analytics | Optional |

### 8.3 Pricing Models

#### Option A: Perpetual License

| Component | Price (USD) |
|-----------|-------------|
| Base (64 cameras) | $50,000 |
| Per additional camera | $200 |
| Annual maintenance (15%) | Variable |
| AI Analytics module | $15,000 |
| C4ISR Connector | $10,000 |

**Example: 256 cameras**
- Base: $50,000
- Additional cameras: 192 × $200 = $38,400
- **Total: $88,400** + $13,260/year maintenance

#### Option B: Subscription

| Tier | Cameras | Price/month | Includes |
|------|---------|-------------|----------|
| Basic | Up to 64 | $800 | VMS + Alerts |
| Professional | Up to 256 | $2,500 | + AI Analytics |
| Enterprise | Unlimited | $5,000 | + C4ISR + Support |

### 8.4 Integration with Defense Portfolio

```
VN-CAM-C1 PLATFORM INTEGRATION
│
├── Camera Products
│   ├── VN-CAM-T1 (Training) → Training analytics
│   ├── VN-CAM-B1 (Base) → Security monitoring
│   ├── VN-CAM-S1 (Border) → Strategic surveillance
│   ├── VN-CAM-M1 (Maritime) → Naval domain awareness
│   ├── VN-CAM-D1 (Drone) → UAV video management
│   └── VN-CAM-W1 (Weapon) → Battle damage assessment
│
├── Training Systems
│   ├── LOMAH → Live-fire data integration
│   ├── RAMS → AI training analytics
│   └── VN-LVC-001 → LVC exercise data
│
└── Command Systems
    ├── VN-CDS-001 (Combat Direction) → Naval COP
    └── VN-CPX-001 (Command Post) → Joint COP
```

---

## 9. PLATFORM ARCHITECTURE

### 9.1 Shared Software Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │   T1    │  │   B1    │  │   S1    │  │   M1    │ ...    │
│  │ Training│  │ Security│  │ Border  │  │Maritime │        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
├─────────────────────────────────────────────────────────────┤
│                    AI MODEL LAYER (SHARED)                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │   Detection  │ │Classification│ │   Tracking   │        │
│  │   Models     │ │    Models    │ │   Algorithms │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
├─────────────────────────────────────────────────────────────┤
│                    FRAMEWORK LAYER                           │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │   TensorRT   │ │  DeepStream  │ │   GStreamer  │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
├─────────────────────────────────────────────────────────────┤
│                    OS/RUNTIME LAYER                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │    Linux     │ │     CUDA     │ │   JetPack    │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### 9.2 Compute Module Selection

| Product | Recommended Module | AI Performance | Power |
|---------|-------------------|----------------|-------|
| T1, B1 | Jetson Orin Nano | 20-40 TOPS | <15W |
| S1, M1 | Jetson Orin NX | 70-100 TOPS | <25W |
| D1 | Jetson Orin Nano (8GB) | 20 TOPS | <10W |
| W1 | Jetson Orin NX | 100 TOPS | <25W |
| C1 (Server) | Jetson AGX Orin | 275 TOPS | <60W |

### 9.3 Platform Benefits

| Benefit | Quantified Savings |
|---------|-------------------|
| R&D Cost Reduction | 40% (shared software) |
| Manufacturing Cost | 30% (volume components) |
| Time-to-Market | 50% faster for variants |
| Training Simplified | Single platform knowledge |
| Spare Parts | Reduced SKU count |

---

## 10. INTEGRATION MATRIX

### 10.1 VN-CAM to Defense Product Integration

| VN-CAM | LOMAH | RAMS | SAMT | NGS | MAT | LVC | CDS | USV | UAV |
|--------|-------|------|------|-----|-----|-----|-----|-----|-----|
| **T1** | ★★★ | ★★★ | ★★★ | ☆ | ☆ | ★★ | ☆ | ☆ | ☆ |
| **B1** | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ★★ | ☆ | ☆ |
| **S1** | ☆ | ☆ | ☆ | ☆ | ☆ | ★★ | ★★★ | ☆ | ☆ |
| **M1** | ☆ | ☆ | ☆ | ★★★ | ☆ | ★★ | ★★★ | ★★★ | ☆ |
| **D1** | ☆ | ☆ | ☆ | ☆ | ☆ | ★ | ★★ | ☆ | ★★★ |
| **W1** | ☆ | ☆ | ☆ | ★★★ | ★★★ | ★★ | ★★★ | ☆ | ☆ |
| **C1** | ★★ | ★★ | ★★ | ★★ | ★ | ★★★ | ★★★ | ★★ | ★★ |

**Legend:** ★★★ Native integration | ★★ Supported | ★ Possible | ☆ Not applicable

### 10.2 Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         VN-CAM-C1 (COMMAND)                          │
│   ┌───────────────────────────────────────────────────────────┐     │
│   │                    AI Analytics Engine                     │     │
│   │   Pattern Recognition │ Cross-Camera Track │ Alert Fusion  │     │
│   └───────────────────────────────────────────────────────────┘     │
│                              ▲                                       │
│   ┌──────────┐  ┌──────────┐  │  ┌──────────┐  ┌──────────┐        │
│   │   VMS    │  │   GIS    │  │  │  Alerts  │  │  Reports │        │
│   └──────────┘  └──────────┘  │  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────────┘
                               ▲
           ┌───────────────────┼───────────────────┐
           │                   │                   │
    ┌──────┴──────┐     ┌──────┴──────┐     ┌──────┴──────┐
    │   Border    │     │   Maritime  │     │   Training  │
    │   Domain    │     │   Domain    │     │   Domain    │
    │             │     │             │     │             │
    │  ┌───────┐  │     │  ┌───────┐  │     │  ┌───────┐  │
    │  │ S1-x  │  │     │  │ M1-x  │  │     │  │ T1-x  │  │
    │  └───────┘  │     │  └───────┘  │     │  └───────┘  │
    │  ┌───────┐  │     │  ┌───────┐  │     │  ┌───────┐  │
    │  │ B1-x  │  │     │  │ D1-x  │  │     │  │LOMAH  │  │
    │  └───────┘  │     │  └───────┘  │     │  └───────┘  │
    └─────────────┘     └─────────────┘     └─────────────┘
```

---

## 11. IMPLEMENTATION ROADMAP

### 11.1 Three-Year Plan

```
YEAR 1: FOUNDATION                           Investment: $500K
├── Q1-Q2: Core Development                  Revenue: $50K
│   ├── AI software stack
│   ├── Jetson integration
│   └── T1 prototype
│
├── Q3: Pilot Deployment                     Revenue: $100K
│   ├── 10× T1 at 2 ranges
│   ├── LOMAH integration
│   └── User feedback
│
└── Q4: Production Start                     Revenue: $50K
    ├── T1 production (50 units)
    ├── B1 prototype
    └── Manufacturing line

YEAR 2: SCALE                                Investment: $800K
├── Q1-Q2: Volume Production                 Revenue: $1.5M
│   ├── T1 scale (200 units)
│   ├── B1 production (500 units)
│   └── S1 development
│
├── Q3: Domain Expansion                     Revenue: $1.0M
│   ├── S1 pilot (northern border)
│   ├── M1 pilot (DK1)
│   └── D1 development
│
└── Q4: Market Growth                        Revenue: $0.5M
    ├── Export exploration
    └── Government contracts

YEAR 3: PLATFORM                             Investment: $600K
├── Q1-Q2: Platform Launch                   Revenue: $4.0M
│   ├── C1 platform release
│   ├── W1 development
│   └── C4ISR integration
│
└── Q3-Q4: Ecosystem Maturity                Revenue: $6.0M+
    ├── Export contracts (ASEAN)
    ├── Recurring platform revenue
    └── Service-based models

TOTAL 3-YEAR
├── Investment: $1.9M
├── Revenue: $13.2M
├── Break-even: Year 2, Q3
└── Year 3 Profit Margin: 30%+
```

### 11.2 Key Milestones

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| T1 prototype complete | Q2 Y1 | 85% AI accuracy |
| First 10 units deployed | Q3 Y1 | Customer acceptance |
| B1 production start | Q1 Y2 | 50 units/month capacity |
| S1 border pilot | Q3 Y2 | 72h autonomous operation |
| M1 naval qualification | Q4 Y2 | Salt spray test passed |
| C1 platform launch | Q1 Y3 | 256 camera management |
| First export order | Q2 Y3 | ASEAN customer signed |
| 1,000th unit shipped | Q4 Y3 | Production milestone |

---

## 12. COST COMPARISON ANALYSIS

### 12.1 Product-by-Product Comparison

| Product Type | VN-CAM | Import Equivalent | Import Price | Savings |
|--------------|--------|-------------------|--------------|---------|
| Training (T1) | $2,500 | FATS, Cubic | $15,000+ | **83%** |
| Base Security (B1) | $2,500 avg | Hikvision Pro/Axis | $4,000-8,000 | **40-70%** |
| Border (S1) | $14,000 | FLIR Ranger/Elbit | $60,000-80,000 | **77-82%** |
| Maritime (M1) | $20,000 avg | FLIR M-series/L3Harris | $50,000-80,000 | **60-75%** |
| UAV Payload (D1) | $3,500 avg | FLIR Vue Pro | $5,000 | **30%** |
| Weapon Sight (W1) | $25,000 avg | Elbit/Kongsberg RCWS | $100,000-120,000 | **75-79%** |
| Platform SW (C1) | $80,000 avg | Milestone/Genetec | $150,000-180,000 | **47-56%** |

**Average Portfolio Savings: 60-70%** vs. Western military-grade systems

### 12.2 Total Cost of Ownership (10-Year)

| Cost Factor | VN-CAM | Import | Savings |
|-------------|--------|--------|---------|
| Acquisition | $1.0M | $3.5M | $2.5M |
| Annual Maintenance | $50K | $200K | $150K/yr |
| Training | $30K | $100K | $70K |
| Spare Parts | $100K | $500K | $400K |
| Upgrades | $200K | $800K | $600K |
| **10-Year TCO** | **$1.83M** | **$6.9M** | **$5.07M (73%)** |

### 12.3 Strategic Value (Non-Quantifiable)

| Factor | VN-CAM Advantage |
|--------|------------------|
| Data Sovereignty | All data processed locally |
| No Export Controls | Freedom from ITAR/EAR |
| Vietnamese AI Optimization | Local faces, plates, vessels |
| Rapid Customization | Direct engineering access |
| Technology Transfer | Build local capability |
| Supply Chain Security | Reduced foreign dependency |

---

## 13. APPENDICES

### Appendix A: Standards Compliance Matrix

| Standard | Description | T1 | B1 | S1 | M1 | D1 | W1 | C1 |
|----------|-------------|----|----|----|----|----|----|----| 
| MIL-STD-810H | Environmental | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| MIL-STD-461G | EMC | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | - |
| MIL-STD-1275D | Vehicle Power | - | ✓ | - | - | - | ✓ | - |
| MIL-STD-704F | Aircraft Power | - | - | - | - | ✓ | - | - |
| STANAG 4586 | UAV Interop | - | - | - | - | ✓ | - | - |
| IEC 62443 | Cybersecurity | - | - | - | - | - | - | ✓ |
| TCVN 6611 | Electrical Safety | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### Appendix B: Mnemonics for Product Family

**VISION** - Strategy Mnemonic
- **V** - Volume products first (T1, B1 fund R&D)
- **I** - Indigenous software is the moat
- **S** - Simplify hardware, use COTS
- **I** - Integrate into platform ecosystem
- **O** - Optimize for Vietnam's actual needs
- **N** - Network effect: more cameras → better AI → more value

**T-B-S-M-D-W-C** - Product Sequence
- **T**raining → **B**ase → **S**ea (Border) → **M**aritime → **D**rone → **W**eapon → **C**ommand

### Appendix C: Glossary

| Term | Vietnamese | Definition |
|------|------------|------------|
| COTS | Sản phẩm thương mại sẵn có | Commercial Off-The-Shelf |
| DRI | Phát hiện-Nhận dạng-Định danh | Detection-Recognition-Identification |
| HITL | Con người trong vòng lặp | Human-In-The-Loop |
| LOS | Đường ngắm | Line of Sight |
| MTBF | Thời gian trung bình giữa các lần hỏng | Mean Time Between Failures |
| NETD | Chênh lệch nhiệt độ tương đương tiếng ồn | Noise Equivalent Temperature Difference |
| RCWS | Trạm vũ khí điều khiển từ xa | Remote Controlled Weapon Station |
| TCO | Tổng chi phí sở hữu | Total Cost of Ownership |
| TOPS | Nghìn tỷ phép tính mỗi giây | Tera Operations Per Second |

### Appendix D: Contact Information

```
╔═══════════════════════════════════════════════════════════════════╗
║              VIETNAM DEFENSE INDUSTRY CORPORATION                  ║
║                                                                    ║
║  Viện Kỹ thuật Hải quân - Xưởng Sản xuất - Chế thử               ║
║                                                                    ║
║  Email: sales@vndefense.gov.vn                                    ║
║  Tel: +84 24 1234 5678                                            ║
║  Website: www.vndefense.gov.vn                                    ║
║                                                                    ║
║  60-70% Cost Savings • Local Support & Maintenance                 ║
║  Vietnamese Platform Integration • Export-Ready Solutions          ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

**Document Control**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 2026 | VKTHQ | Initial release |
| 2.0 | Feb 2026 | VKTHQ + Claude | Complete technical specifications, integration matrix, cost analysis |

---

*Classification: CONFIDENTIAL*  
*Distribution: Authorized Personnel Only*  
*© 2026 Vietnam Defense Industry Corporation. All Rights Reserved.*
