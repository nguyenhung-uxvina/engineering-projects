---
title: "BB-01 Project Overview"
title_vi: "Tổng quan dự án BB-01"
project: bb-01
type: overview
created: 2026-01-24
updated: 2026-01-29
status: active
phase: embodiment
gate: G2
tags: [lomah, acoustic, naval, target-system]
entities:
  - type: product
    name: BB-01-LOMAH
  - type: standard
    name: Điều-124-Bài-3
  - type: organization
    name: Vietnamese-Navy
metrics:
  gate_status: ready
  dfx_score: 90
  mtbf_hours: 551
---

# BB-01: Bia Huấn Luyện Bắn Trên Biển

> **Project Code**: VN-TARGET-BB01
> **Status**: Gate 2 Ready ✅
> **Version**: v1.3

---

## 🎯 Mission Statement

Develop a **floating naval target system** with automatic hit detection for infantry weapons training at sea, supporting the Vietnamese Navy's marksmanship qualification program.

---

## 📊 Project Summary

| Attribute | Value |
|-----------|-------|
| **Reference** | Điều 124, Bài 3: Bắn mục tiêu trên mặt nước |
| **Detection Method** | Acoustic impact detection |
| **Target Types** | 4 targets (2×7e + 1×6c + 1×số 10) |
| **Mounting Style** | Chain-suspended steel plates |
| **Budget R&D** | 350,000,000 VND |
| **Unit Cost Target** | ≤60,000,000 VND/bộ |

---

## 🏗️ System Overview

```
┌─────────────────────────────────────────────────┐
│                  TRƯỜNG BẮN                      │
│   ┌──────────────┐                              │
│   │    TRẠM      │          ≥500m               │
│   │   ĐIỀU       │◄────────────────────────────►│
│   │   KHIỂN      │                              │
│   └──────────────┘                              │
│                                                  │
│   ┌─────────────────────────────────────────┐   │
│   │           PHAO CATAMARAN                │   │
│   │    ┌──────────┐           ┌──────────┐  │   │
│   │    │  PHAO 1  │═══════════│  PHAO 2  │  │   │
│   │    └──────────┘  3.5-4.0m └──────────┘  │   │
│   │              Thả nổi tự do              │   │
│   └─────────────────────────────────────────┘   │
│                                                  │
│   ┌──────────────────────────────────────────┐  │
│   │              KHUNG BIA THÉP              │  │
│   │   ┌────┐  ┌────┐  ┌────┐  ┌────────┐    │  │
│   │   │ 7e │  │ 7e │  │ 6c │  │  SỐ 10 │    │  │
│   │   │    │  │    │  │    │  │ 75cm   │    │  │
│   │   └─┬──┘  └─┬──┘  └─┬──┘  └───┬────┘    │  │
│   │     │       │       │         │          │  │
│   │     ∿       ∿       ∿         ∿          │  │
│   │   XÍCH    XÍCH    XÍCH      XÍCH        │  │
│   │   (rung tự do cho acoustic detection)   │  │
│   └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 📋 Key Requirements (v1.3)

### Target Configuration
| ID | Requirement | Value |
|----|-------------|-------|
| TT.01 | Bia số 7e | Hình người đứng/di chuyển |
| TT.02 | Bia số 6c | Hình địch nằm bắn |
| TT.03 | Bia số 10 | "Tên địch bắn trung/đại liên" 75cm |
| TT.07 | Tổng số bia/cụm | 4 cái |

### Mounting (v1.3 Update)
| ID | Requirement | Value |
|----|-------------|-------|
| TMT.01 | Kiểu gắn bia | TREO BẰNG XÍCH |
| TMT.02 | Vị trí các bia | NGANG HÀNG |
| TMT.07 | Bia rung tự do | Có (critical for acoustic) |

### Acoustic Sensor
| ID | Requirement | Value |
|----|-------------|-------|
| AS.01 | Loại sensor | Microphone (MEMS/Electret) |
| AS.02-03 | Số microphone | 4-5 total |
| AS.06 | Dải tần số | 100 Hz - 20 kHz |
| AS.07 | SPL max | ≥140 dB |

### Ballistics
| ID | Requirement | Value |
|----|-------------|-------|
| B.01 | Khoảng cách bắn MIN | 150m |
| B.02 | Khoảng cách bắn MAX | 400m |
| B.03-05 | Calibers | 5.56, 7.62×39, 7.62×54R |

---

## 📁 Project Structure

```
bb-01/
├── README.md (this file)
├── requirements/
│   └── [[v1.3-summary]] ← Requirements extracted
├── research/
│   ├── [[acoustic-sensor-research]] ← Full D-M-I-R
│   └── [[acoustic-sensor-summary]] ← Executive summary
├── decisions/
│   └── [[log]] ← DEC-001, DEC-002
└── quality/
    ├── [[DfX-Review-MCU-Box]] ← Full analysis
    ├── [[DfX-Dashboard]] ← Issue tracking
    └── [[MTBF-Improvement-Plan]] ← DfR-001 fix
```

---

## 🔄 Change Log

| Version | Change | Reason |
|---------|--------|--------|
| v1.2→v1.3 | Bia số 10: Bia tròn → "Tên địch bắn trung/đại liên" | Đúng theo tài liệu |
| v1.2→v1.3 | Cách gắn bia: Chưa rõ → TREO BẰNG XÍCH | Theo hình thực tế |
| v1.2→v1.3 | Vị trí các bia: Chưa rõ → NGANG HÀNG | Yêu cầu mới |
| v1.2→v1.3 | Added kiểm tra xích định kỳ | Tránh gỉ/đứt |

---

## ⚠️ Critical Design Considerations

1. **Chain Mounting**: Bia PHẢI rung tự do để acoustic detection hoạt động
2. **Waterproofing**: IP65+ cho tất cả electronics
3. **Material**: Thép AR400+ không xuyên thủng
4. **Communication**: Wireless ≥500m đến trạm điều khiển

---

## 🔗 Related Projects

- [[domains/v-smash/README]] - V-SMASH (acoustic detection learnings may apply)
- MTB-20 - Naval platform integration

---

*Last updated: 2026-01-26*
*Following Pahl & Beitz Methodology*
