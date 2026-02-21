---
project: CORTEX-C2
phase: 1
type: standards_mapping
version: 1.0
created: 2026-02-12
status: draft
edition: RANGE STANDARD
standard_families: 12
total_clauses_mapped: 89
requirements_traced: 74
---

# STANDARDS MAPPING
## CORTEX-C2 RANGE STANDARD "TRƯỜNG BẮN" — AI-Driven Live-Fire Training Analytics
### Version: 1.0 | Date: 2026-02-12

---

> **Purpose:** Map all applicable cybersecurity, interoperability, software quality, data protection, and military standards to CORTEX RANGE STANDARD requirements. Defines specific compliance approaches, test methods, and acceptance criteria for a **software platform** product.
>
> **Key difference from hardware projects:** CORTEX RANGE is a software-only product. Environmental (MIL-STD-810H), EMC (MIL-STD-461G), and IP standards apply to the **edge server hardware** (COTS procurement) — not to CORTEX software itself. This standards mapping focuses on software-relevant standards.
>
> **Cross-reference:** [[requirements_list.md]] for detailed requirement definitions.
>
> **Classification:** UNCLASSIFIED

---

## 1. STANDARDS OVERVIEW

### 1.1 Applicable Standards Summary

| # | Standard | Title | Scope | Priority |
|---|----------|-------|-------|----------|
| 1 | **OWASP Top 10 (2021)** | Web Application Security Risks | Application-level security for web platform | Critical |
| 2 | **NIST CSF v2.0** | Cybersecurity Framework | Security posture across Govern/Identify/Protect/Detect/Respond/Recover | Critical |
| 3 | **IEC 62443** | Industrial Cybersecurity | Network-connected system security levels | Important |
| 4 | **DIS IEEE 1278.1** | Distributed Interactive Simulation | Live-Virtual-Constructive interoperability protocol | Critical |
| 5 | **CoT / MIL-PRF-49503** | Cursor on Target | Tactical Awareness Kit (TAK) integration protocol | Critical |
| 6 | **HLA IEEE 1516** | High Level Architecture | Federation-based simulation interoperability | Important |
| 7 | **ISO/IEC 25010:2023** | Software Quality Model | Quality characteristics: reliability, security, usability, performance | Important |
| 8 | **MIL-STD-882E** | System Safety | AI classification influence on training decisions | Important |
| 9 | **TCVN / Vietnamese Law** | National Standards & Cybersecurity Law | Vietnamese regulatory compliance | Critical |
| 10 | **WCAG 2.1 Level AA** | Web Content Accessibility | Accessibility for military users in field conditions | Optional |
| 11 | **OpenAPI 3.0 / JSON Schema** | API & Data Standards | API specification and CDM schema compliance | Important |
| 12 | **ISO/IEC 27001:2022** | Information Security Management | ISMS framework for training data protection | Optional |

### 1.2 Compliance Priority Matrix

| Priority | Definition | Standards |
|----------|-----------|-----------|
| **Critical** | Must comply for military deployment; non-negotiable for Vietnamese MoND acceptance | OWASP Top 10, NIST CSF, DIS IEEE 1278.1, CoT/TAK, TCVN/Vietnamese Law |
| **Important** | Required for credibility and interoperability; may use tailored compliance | IEC 62443, HLA IEEE 1516, ISO 25010, MIL-STD-882E, OpenAPI/JSON Schema |
| **Optional** | Best practice; enhances product competitiveness for international market | WCAG 2.1, ISO 27001 |

### 1.3 Software vs Hardware Standard Boundaries

| Domain | Standard Applied To | Responsible Party | Notes |
|--------|--------------------|--------------------|-------|
| **Application security** | CORTEX RANGE software | Workshop X Dev Team | This document |
| **Network security** | CORTEX deployment environment | Workshop X + IT Admin (S7) | This document |
| **Interoperability protocols** | CORTEX integration interfaces | Workshop X Dev Team | This document |
| **Data protection** | Training data at rest and in transit | Workshop X + Cybersecurity Officer (S13) | This document |
| **Edge server environmental** | COTS hardware (mini-PC/Jetson) | Hardware vendor | Use vendor-certified hardware (MIL-STD-810H optional for COTS) |
| **Edge server EMC** | COTS hardware | Hardware vendor | FCC/CE certification sufficient for indoor deployment |
| **Power supply safety** | COTS power adapter/UPS | Hardware vendor | IEC 62368-1 certified COTS |

> **Bottom line:** Workshop X is responsible for **software** and **data** standards. **Hardware** standards are satisfied by selecting appropriately certified COTS equipment.

---

## 2. OWASP TOP 10 (2021) — WEB APPLICATION SECURITY

### 2.1 Applicability Statement

CORTEX RANGE is a web application (React frontend + FastAPI backend + WebSocket + REST API) deployed on edge servers in Vietnamese military ranges. OWASP Top 10 is the internationally recognized baseline for web application security and maps directly to SEC-008 (MUST).

### 2.2 Risk Mapping

#### A01:2021 — Broken Access Control

| Parameter | Value |
|-----------|-------|
| **Risk** | Unauthorized user accesses another unit's training data or admin functions |
| **CORTEX Impact** | HIGH — training performance data is RESTRICTED; cross-unit data leakage unacceptable |
| **Mitigation** | Role-Based Access Control (SEC-003): 4 roles with granular permissions; server-side authorization on every API call; unit-scoped data access (user can only query their assigned unit's data) |
| **Test Method** | Automated SAST/DAST + manual penetration test |
| **Pass Criteria** | Zero access control bypass findings in penetration test |
| **Applicable Requirements** | [[requirements_list.md#SEC-003]] (RBAC), [[requirements_list.md#SEC-007]] (Audit logging) |
| **CORTEX Notes** | FastAPI dependency injection for auth middleware; every endpoint decorated with role check. Unit-level data isolation via database row-level security (PostgreSQL RLS policies). |

#### A02:2021 — Cryptographic Failures

| Parameter | Value |
|-----------|-------|
| **Risk** | Training data exposed in transit or at rest due to weak/missing encryption |
| **CORTEX Impact** | HIGH — soldier performance data, unit readiness metrics are sensitive |
| **Mitigation** | TLS 1.3 for all connections (SEC-004); AES-256 at rest (SEC-005); no plaintext credentials in config files; bcrypt/argon2 password hashing |
| **Test Method** | TLS configuration scan (testssl.sh); database encryption verification; code review for hardcoded secrets |
| **Pass Criteria** | TLS 1.3 enforced; no TLS 1.0/1.1; AES-256 at rest verified; zero hardcoded credentials |
| **Applicable Requirements** | [[requirements_list.md#SEC-004]] (TLS), [[requirements_list.md#SEC-005]] (AES-256), [[requirements_list.md#SEC-009]] (Personal data) |
| **CORTEX Notes** | Self-signed CA acceptable for air-gapped deployment (SEC-006); client browsers will show warning unless CA is installed on client devices. Provide setup script to install Workshop X root CA on range tablets. |

#### A03:2021 — Injection

| Parameter | Value |
|-----------|-------|
| **Risk** | SQL injection via REST API or WebSocket; command injection via sensor configuration |
| **CORTEX Impact** | CRITICAL — database contains all training data; injection could destroy records or exfiltrate |
| **Mitigation** | Parameterized queries only (SQLAlchemy ORM); input validation on all API endpoints (Pydantic models); no dynamic SQL construction; CSP headers for XSS prevention |
| **Test Method** | SAST (Bandit for Python); DAST (OWASP ZAP); SQLMap automated injection test; manual review of raw SQL queries |
| **Pass Criteria** | Zero injection vulnerabilities; all database queries via ORM parameterized |
| **Applicable Requirements** | [[requirements_list.md#SEC-008]] (OWASP Top 10) |
| **CORTEX Notes** | TimescaleDB (PostgreSQL) supports parameterized queries natively. FastAPI + Pydantic enforces type validation before data reaches handlers. WebSocket message payloads validated with JSON Schema before processing. |

#### A04:2021 — Insecure Design

| Parameter | Value |
|-----------|-------|
| **Risk** | Missing threat model; no abuse case analysis; authentication bypass by design |
| **CORTEX Impact** | MEDIUM — air-gapped deployment reduces external attack surface; insider threat is primary concern |
| **Mitigation** | Threat model documented (Phase 1); abuse cases for each user role; session timeout (SEC-002, 30 min idle); rate limiting on authentication endpoints |
| **Test Method** | Architecture review against STRIDE model; abuse case testing |
| **Pass Criteria** | Threat model covers all external interfaces; abuse cases documented for all roles |
| **Applicable Requirements** | [[requirements_list.md#SEC-002]] (Authentication), [[requirements_list.md#SEC-003]] (RBAC) |

#### A05:2021 — Security Misconfiguration

| Parameter | Value |
|-----------|-------|
| **Risk** | Default credentials, debug mode enabled, unnecessary services exposed, verbose error messages |
| **CORTEX Impact** | MEDIUM — edge server is single-tenant; misconfiguration mainly an insider risk |
| **Mitigation** | Hardened Docker container images (no default credentials, debug disabled); security checklist in deployment guide; automated security configuration scan at startup |
| **Test Method** | Configuration audit; port scan; service enumeration |
| **Pass Criteria** | Zero default credentials; no debug endpoints in production; only required ports open |
| **Applicable Requirements** | [[requirements_list.md#SEC-006]] (Air-gapped), [[requirements_list.md#SEC-010]] (Network segmentation) |
| **CORTEX Notes** | Docker Compose production profile with hardened settings. Startup self-test verifies security configuration and warns admin of issues. |

#### A06:2021 — Vulnerable and Outdated Components

| Parameter | Value |
|-----------|-------|
| **Risk** | Known CVEs in Python/React/PostgreSQL dependencies |
| **CORTEX Impact** | MEDIUM — air-gapped deployment means exploits require physical access, but outdated components accumulate risk |
| **Mitigation** | Quarterly dependency audit (MNT-001); `pip-audit` and `npm audit` in CI/CD; pin dependency versions; SBOM (Software Bill of Materials) for each release |
| **Test Method** | Automated CVE scan (Trivy on Docker images); manual review of critical dependencies |
| **Pass Criteria** | Zero critical/high CVEs in production dependencies at release time |
| **Applicable Requirements** | [[requirements_list.md#MNT-001]] (Quarterly updates), [[requirements_list.md#ARC-007]] (FOSS dependencies) |
| **CORTEX Notes** | Offline package mirror bundled in installation USB for air-gapped updates. SBOM published with each release per Executive Order 14028 best practice. |

#### A07:2021 — Identification and Authentication Failures

| Parameter | Value |
|-----------|-------|
| **Risk** | Weak passwords, session hijacking, missing multi-factor |
| **CORTEX Impact** | HIGH — unauthorized access to training data; impersonation of officer for false reports |
| **Mitigation** | Password policy ≥12 chars + complexity (SEC-002); JWT with short expiry (30 min idle); secure cookie flags (HttpOnly, Secure, SameSite); account lockout after 5 failed attempts |
| **Test Method** | Authentication bypass testing; session management testing; brute-force simulation |
| **Pass Criteria** | No authentication bypass; sessions expire correctly; lockout functions |
| **Applicable Requirements** | [[requirements_list.md#SEC-002]] (Authentication) |
| **CORTEX Notes** | Phase 1: local accounts with JWT. Phase 3+: LDAP/AD integration for enterprise environments. MFA deferred to Phase 3 (WISH). |

#### A08:2021 — Software and Data Integrity Failures

| Parameter | Value |
|-----------|-------|
| **Risk** | Unsigned software updates; CI/CD pipeline compromise; tampered training data |
| **CORTEX Impact** | HIGH — compromised update could modify scoring algorithms or exfiltrate data |
| **Mitigation** | Signed software packages (SHA-256 hash + GPG signature); verified Docker image digests; tamper-evident audit log (SEC-007); database integrity checks (QUA-010) |
| **Test Method** | Verify update signature validation; attempt unsigned update installation; audit log tamper test |
| **Pass Criteria** | System rejects unsigned/modified update packages; audit log detects tampering |
| **Applicable Requirements** | [[requirements_list.md#SEC-007]] (Audit logging), [[requirements_list.md#QUA-002]] (Zero data loss), [[requirements_list.md#QUA-010]] (Data integrity audit) |

#### A09:2021 — Security Logging and Monitoring Failures

| Parameter | Value |
|-----------|-------|
| **Risk** | Security events not logged; logs not retained; no alerting on suspicious activity |
| **CORTEX Impact** | MEDIUM — without logging, security incidents cannot be investigated |
| **Mitigation** | Structured JSON logging for all security events (SEC-007); append-only hash-chained log; ≥365 days retention; alerting on auth failures, privilege escalation, data export |
| **Test Method** | Verify log completeness (all login/logout, CRUD, config changes); verify tamper detection; test alert triggers |
| **Pass Criteria** | 100% of security-relevant events logged; hash chain validates; alerts fire within 60 seconds |
| **Applicable Requirements** | [[requirements_list.md#SEC-007]] (Audit logging), [[requirements_list.md#OPS-006]] (Log management), [[requirements_list.md#OPS-010]] (Monitoring alerts) |

#### A10:2021 — Server-Side Request Forgery (SSRF)

| Parameter | Value |
|-----------|-------|
| **Risk** | Attacker uses CORTEX server to access internal network resources |
| **CORTEX Impact** | LOW — air-gapped deployment limits SSRF impact; no internet-facing services |
| **Mitigation** | No user-controllable URL fetching in Phase 1; input validation on all external data sources; network segmentation (SEC-010) |
| **Test Method** | Attempt SSRF via any user-controllable input; verify URL validation |
| **Pass Criteria** | No SSRF vulnerabilities identified |
| **Applicable Requirements** | [[requirements_list.md#SEC-008]] (OWASP Top 10), [[requirements_list.md#SEC-010]] (Network segmentation) |

### 2.3 OWASP Compliance Summary

| OWASP Risk | CORTEX Impact | Mitigation Status | Test Phase | Est. Cost (USD) |
|------------|--------------|-------------------|------------|-----------------|
| A01 Broken Access Control | HIGH | Designed | Phase 1 | Included in pen test |
| A02 Cryptographic Failures | HIGH | Designed | Phase 1 | Included in pen test |
| A03 Injection | CRITICAL | Designed | Phase 1 | Included in pen test |
| A04 Insecure Design | MEDIUM | Phase 1 | Phase 1 | $2,000 (threat model) |
| A05 Security Misconfiguration | MEDIUM | Designed | Phase 1 | Included in pen test |
| A06 Vulnerable Components | MEDIUM | Process | Each release | $500/release (scan) |
| A07 Auth Failures | HIGH | Designed | Phase 1 | Included in pen test |
| A08 Data Integrity | HIGH | Designed | Phase 1 | Included in pen test |
| A09 Logging Failures | MEDIUM | Designed | Phase 1 | Included in pen test |
| A10 SSRF | LOW | Designed | Phase 1 | Included in pen test |
| **Penetration test (all)** | | | **Phase 1** | **$8,000** |

---

## 3. NIST CYBERSECURITY FRAMEWORK v2.0

### 3.1 Applicability Statement

NIST CSF v2.0 (released February 2024) provides the overarching cybersecurity governance framework for CORTEX RANGE. While not mandated by Vietnamese law specifically, NIST CSF is the internationally recognized defense-industry standard and aligns with Vietnamese Cybersecurity Law (2018) principles.

### 3.2 Function Mapping

#### GV — GOVERN (New in CSF v2.0)

| Subcategory | CORTEX Implementation | Requirements |
|-------------|----------------------|-------------|
| GV.OC — Organizational Context | Training data classification (RESTRICTED per SEC-001); military deployment context documented | [[requirements_list.md#SEC-001]] |
| GV.RM — Risk Management Strategy | Threat model documented; risk register maintained; quarterly review | SEC-012 |
| GV.SC — Supply Chain Risk | SBOM for all dependencies; FOSS-only (ARC-007); no single-vendor lock-in | [[requirements_list.md#ARC-007]] |

#### ID — IDENTIFY

| Subcategory | CORTEX Implementation | Requirements |
|-------------|----------------------|-------------|
| ID.AM — Asset Management | Edge server inventory; sensor inventory; software version tracking per range | [[requirements_list.md#OPS-003]] |
| ID.RA — Risk Assessment | OWASP threat model; AI classification risk per MIL-STD-882E | SEC-008, QUA-005 |

#### PR — PROTECT

| Subcategory | CORTEX Implementation | Requirements |
|-------------|----------------------|-------------|
| PR.AA — Identity Management | JWT authentication; RBAC 4 roles; session timeout 30 min; password ≥12 chars | [[requirements_list.md#SEC-002]], [[requirements_list.md#SEC-003]] |
| PR.DS — Data Security | TLS 1.3 in transit; AES-256 at rest; encrypted backups; personal data encryption | [[requirements_list.md#SEC-004]], [[requirements_list.md#SEC-005]], [[requirements_list.md#SEC-009]] |
| PR.PS — Platform Security | Hardened Docker containers; OWASP Top 10 compliance; signed updates | [[requirements_list.md#SEC-008]], [[requirements_list.md#DEP-002]] |
| PR.IR — Infrastructure Resilience | Air-gapped deployment; offline operation ≥30 days; automated backup | [[requirements_list.md#SEC-006]], [[requirements_list.md#HST-006]], [[requirements_list.md#OPS-004]] |

#### DE — DETECT

| Subcategory | CORTEX Implementation | Requirements |
|-------------|----------------------|-------------|
| DE.CM — Continuous Monitoring | System health dashboard; log monitoring; authentication failure alerts | [[requirements_list.md#OPS-003]], [[requirements_list.md#OPS-010]] |
| DE.AE — Adverse Event Analysis | Structured logging; hash-chained audit trail; anomaly alerting | [[requirements_list.md#SEC-007]], [[requirements_list.md#OPS-006]] |

#### RS — RESPOND

| Subcategory | CORTEX Implementation | Requirements |
|-------------|----------------------|-------------|
| RS.MA — Incident Management | Security incident response plan documented; admin notification; forensic log export | [[requirements_list.md#SEC-012]] |
| RS.AN — Incident Analysis | Searchable structured logs; exportable for investigation; ≥365 day retention | [[requirements_list.md#OPS-006]] |

#### RC — RECOVER

| Subcategory | CORTEX Implementation | Requirements |
|-------------|----------------------|-------------|
| RC.RP — Recovery Planning | Daily automated backup; configuration backup/restore; software rollback ≤5 min | [[requirements_list.md#OPS-004]], [[requirements_list.md#DEP-006]], [[requirements_list.md#DST-006]] |
| RC.CO — Recovery Communication | Admin alerted on recovery events; incident report template | OPS-010, SEC-012 |

### 3.3 NIST CSF Maturity Target

| CSF Function | Target Tier | Rationale |
|-------------|-------------|-----------|
| Govern | Tier 2 (Risk Informed) | Security policies documented; risk-based prioritization |
| Identify | Tier 2 | Asset inventory automated; risk assessment completed |
| Protect | Tier 3 (Repeatable) | Security controls standardized across all deployments |
| Detect | Tier 2 | Monitoring active; alerting configured; manual analysis |
| Respond | Tier 2 | Incident response plan exists; tested annually |
| Recover | Tier 3 | Automated backup; tested restore; rollback verified |

---

## 4. IEC 62443 — INDUSTRIAL CYBERSECURITY

### 4.1 Applicability

CORTEX RANGE connects edge servers to sensor networks (VN-LOMAH, cameras) and client devices (tablets, laptops) within a military range LAN. IEC 62443 provides the security level (SL) framework for this network-connected system.

### 4.2 Security Level Target

| Parameter | Value |
|-----------|-------|
| **Target SL** | SL-2: Protection against intentional violation using simple means, low resources, generic skills |
| **Rationale** | Air-gapped deployment eliminates remote attack vectors. Primary threat: insider with physical access (disgruntled soldier, careless admin). SL-2 is appropriate for isolated military LAN. |
| **Future target** | SL-3 when CORTEX connects to external networks (Phase 5 CLOUD/ENTERPRISE) |

### 4.3 Foundational Requirements (FR) Mapping

| FR | Requirement | SL-2 Implementation | CORTEX Requirements |
|----|------------|---------------------|---------------------|
| **FR 1** | Identification & Authentication | Username + password (≥12 chars); JWT tokens; 4 roles | SEC-002, SEC-003 |
| **FR 2** | Use Control | RBAC with unit-scoped data access; session timeout; least privilege | SEC-003, SEC-007 |
| **FR 3** | System Integrity | Signed software packages; hash-chained audit log; data integrity checks | SEC-007, QUA-002, QUA-010 |
| **FR 4** | Data Confidentiality | TLS 1.3 in transit; AES-256 at rest; encrypted personal data fields | SEC-004, SEC-005, SEC-009 |
| **FR 5** | Restricted Data Flow | Network segmentation — sensor VLAN isolated from admin VLAN; firewall rules | SEC-010 |
| **FR 6** | Timely Response to Events | Security alerting ≤60 seconds; structured logging; incident response plan | OPS-010, SEC-007, SEC-012 |
| **FR 7** | Resource Availability | ≥99.5% uptime; automated backup; UPS battery; graceful degradation | QUA-001, OPS-004, HST-007 |

### 4.4 Zone and Conduit Model

```
┌─────────────────────────────────────────────────────────────────┐
│ ZONE 1: SENSOR NETWORK (SL-1)                                   │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐                         │
│ │ VN-LOMAH │ │ VN-LOMAH │ │ VN-CAM   │ ← Sensor devices        │
│ │ Lane 1   │ │ Lane N   │ │ T1       │   (no auth, UDP/RTSP)   │
│ └────┬─────┘ └────┬─────┘ └────┬─────┘                         │
│      └──────────┬──┘            │                               │
│                 │               │                               │
│ ════════════════╪═══════════════╪═══════ CONDUIT C1             │
│                 │ (Ethernet     │        (Sensor→Server)        │
│                 │  1Gbps)       │                               │
├─────────────────┼───────────────┼───────────────────────────────┤
│ ZONE 2: EDGE SERVER (SL-2)     │                               │
│ ┌──────────────────────────────────────────────┐               │
│ │ CORTEX RANGE Edge Server                      │               │
│ │ ┌──────────┐ ┌──────────┐ ┌──────────┐       │               │
│ │ │ Ingestion│ │ Analytics│ │ Dashboard│       │               │
│ │ │ Service  │ │ Service  │ │ Service  │       │               │
│ │ └──────────┘ └──────────┘ └──────────┘       │               │
│ │ ┌──────────┐ ┌──────────┐ ┌──────────┐       │               │
│ │ │ API      │ │TimescaleDB│ │ AI Infer │       │               │
│ │ │ Gateway  │ │ (PG)     │ │ (ONNX)   │       │               │
│ │ └──────────┘ └──────────┘ └──────────┘       │               │
│ └──────────────────────────────────────────────┘               │
│                 │                                               │
│ ════════════════╪═══════════════════════ CONDUIT C2             │
│                 │ (WiFi 6 / Ethernet)    (Server→Clients)       │
│                 │ TLS 1.3 enforced                              │
├─────────────────┼───────────────────────────────────────────────┤
│ ZONE 3: CLIENT NETWORK (SL-1)                                   │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐                         │
│ │ Tablet   │ │ Laptop   │ │ Admin PC │ ← Client devices        │
│ │ (NCO)    │ │ (Officer)│ │ (IT)     │   (Browser + Auth)      │
│ └──────────┘ └──────────┘ └──────────┘                         │
└─────────────────────────────────────────────────────────────────┘
     ↕ NO CONNECTION ↕
 ┌───────────────────┐
 │ INTERNET / WAN    │ ← SEC-006: Air-gapped. No connection.
 └───────────────────┘
```

| Conduit | From → To | Protocol | Security | Requirements |
|---------|-----------|----------|----------|-------------|
| **C1** | Sensor → Server | UDP (LOMAH), RTSP (Camera), mDNS | Unencrypted (isolated VLAN); firewall allows only sensor protocols | SEC-010, INT-001, INT-002 |
| **C2** | Server → Clients | HTTPS (TLS 1.3), WSS (WebSocket Secure) | TLS 1.3 mandatory; JWT auth; role-based content | SEC-004, SEC-002, SEC-003 |

---

## 5. DIS IEEE 1278.1 — DISTRIBUTED INTERACTIVE SIMULATION

### 5.1 Applicability Statement

DIS (Distributed Interactive Simulation) is the mandatory interoperability standard for LVC (Live-Virtual-Constructive) training systems. Cubic SPEAR CDM uses DIS internally. All major CTCs (National Training Centers) use DIS. CORTEX RANGE must publish training events as DIS PDUs to integrate with existing military simulation infrastructure.

**Key finding from RE analysis:** DIS + CoT/TAK are must-support protocols. Cubic's SPEAR CDM is proprietary (18 formats) — CORTEX's open CDM + DIS export wins on interoperability.

### 5.2 Protocol Specification

| Parameter | Value |
|-----------|-------|
| **Standard** | IEEE 1278.1-2012 (DIS Application Protocols) |
| **Transport** | UDP multicast (default 239.1.2.3:3000) |
| **Byte Order** | Big-endian (network byte order) |
| **Protocol Version** | 7 (DIS v7, IEEE 1278.1-2012) |
| **Exercise ID** | Configurable per training session |
| **Library** | Open-DIS for Python (open-source, BSD license) |

### 5.3 PDU Mapping

| DIS PDU | Type | CORTEX Usage | Requirements |
|---------|------|-------------|-------------|
| **Entity State PDU** | 1 | Publish soldier position when TRACKER active (FUN-022, Phase 3) | [[requirements_list.md#INT-006]] |
| **Fire PDU** | 2 | Publish when shot detected by VN-LOMAH | [[requirements_list.md#INT-006]] |
| **Detonation PDU** | 3 | Publish shot impact position with target hit/miss | [[requirements_list.md#INT-006]] |
| **Data PDU** | 20 | Custom CORTEX training metrics (scores, grouping, technique classification) | [[requirements_list.md#INT-006]] |
| **Comment PDU** | 22 | Session events (start, end, pause, resume) | [[requirements_list.md#INT-006]] |
| **Start/Resume PDU** | 13 | Training session control synchronization | INT-006 |
| **Stop/Freeze PDU** | 14 | Training session control synchronization | INT-006 |

### 5.4 Entity Type Mapping

| Entity | DIS Entity Type (Kind.Domain.Country.Category) | Notes |
|--------|-----------------------------------------------|-------|
| Soldier (shooting) | 1.1.229.1 (Platform, Land, Vietnam, Other) | Entity ID = soldier database ID |
| Target (LOMAH panel) | 1.1.229.0 (Platform, Land, Vietnam, Other) | Lane number encoded in entity marking |
| Range facility | 5.1.229.0 (Cultural Feature, Land, Vietnam) | Static entity for range geolocation |
| Shot projectile | 2.1.229.0 (Munition, Anti-armor, Vietnam) | Fire PDU → Detonation PDU pair |

### 5.5 DIS Compliance Level

| Level | Description | CORTEX Target |
|-------|------------|---------------|
| **Level 1** | PDU generation and reception | Phase 2 MUST |
| **Level 2** | Dead reckoning compliance | Phase 3 WISH (for TRACKER movement) |
| **Level 3** | Full federation with HLA gateway | Phase 3-4 (via INT-010 HLA) |

### 5.6 Test Method

| Test | Method | Pass Criteria | Tool |
|------|--------|---------------|------|
| PDU format validation | Capture CORTEX DIS output; validate PDU structure | All PDUs parse correctly per IEEE 1278.1 | Wireshark DIS dissector |
| Entity enumeration | Verify entity types use valid enumerations | All entity types from SISO-REF-010 | Open-DIS validation tool |
| Multicast delivery | Multi-node test with ≥3 DIS receivers | All receivers see all PDUs within ≤100ms | Network analyzer |
| Interoperability | Connect CORTEX to VBS3 or JCATS via DIS | External system displays CORTEX entities | Partner system test |

| **Estimated cost** | **$3,000** (2 weeks development + 1 week testing) |

---

## 6. CoT / TAK — CURSOR ON TARGET / TEAM AWARENESS KIT

### 6.1 Applicability Statement

CoT (Cursor on Target) is the tactical data protocol used by ATAK (Android TAK) and WinTAK. TAK is widely adopted by Vietnamese SOF and allied forces. Mind Foundry SENTRY demonstrated TAK integration in <30 seconds. CORTEX RANGE must publish training data as CoT messages for display on TAK tactical maps.

### 6.2 Protocol Specification

| Parameter | Value |
|-----------|-------|
| **Standard** | MIL-PRF-49503 (Cursor on Target); TAK SDK |
| **Transport** | UDP multicast (SA, port 6969) or TCP to TAK Server (port 8089) |
| **Format** | XML (CoT schema) |
| **Library** | PyTAK (Python CoT library, open-source) or custom XML generator |

### 6.3 CoT Message Mapping

| CORTEX Event | CoT Type | CoT Attributes | Notes |
|-------------|----------|----------------|-------|
| **Active shooter** | `a-f-G-U-C` (friendly, ground, unit, combat) | lat, lon, hae, callsign=soldier_name | Shows shooters on TAK map |
| **Shot fired** | `b-m-p-s-p-i` (bits, mayday, point) | lat, lon + custom detail (score, grouping) | Shot event notification |
| **Range session active** | `b-t-f` (bits, target, freetext) | Session ID, exercise type, status | Range status on TAK |
| **Safety alert** | `b-a` (bits, alert) | Alert type, lane number, description | Safety events (ceasefire, medical) |
| **Training report** | `b-r-f-c` (bits, report, freetext, chat) | Summary metrics as CoT remarks | Post-session summary |

### 6.4 TAK Plugin Architecture

| Component | Description | Requirements |
|-----------|-------------|-------------|
| **CoT Generator** | Python service converting CDM events to CoT XML | [[requirements_list.md#INT-007]] |
| **TAK Server Connector** | Optional TCP connection to TAK Server for persistent data | INT-007 |
| **ATAK Plugin** | Android plugin for ATAK showing CORTEX training overlays | INT-007 (Phase 2) |
| **WinTAK Plugin** | Windows plugin for WinTAK in range control room | INT-007 (Phase 2) |

### 6.5 Test Method

| Test | Method | Pass Criteria | Tool |
|------|--------|---------------|------|
| CoT XML validation | Validate generated XML against CoT schema | All messages schema-valid | xmllint + CoT XSD |
| ATAK display | Send CoT from CORTEX; verify display on ATAK | Entities appear on map within ≤5 seconds | ATAK on Android device |
| TAK Server relay | Push CoT to TAK Server; verify relay to clients | All connected TAK clients receive updates | TAK Server + 3 clients |
| CoT content accuracy | Compare CoT lat/lon/data with source CDM | Position within ±1m; data matches 100% | Manual verification |

| **Estimated cost** | **$2,000** (1 week development + 1 week testing) |

---

## 7. HLA IEEE 1516 — HIGH LEVEL ARCHITECTURE

### 7.1 Applicability Statement

HLA is the standard for complex multi-domain simulation federations. Required for integration with CAE, Rheinmetall, and NATO constructive simulation systems. CORTEX RANGE implements HLA as a Phase 3 WISH requirement.

### 7.2 Specification

| Parameter | Value |
|-----------|-------|
| **Standard** | IEEE 1516-2010 (HLA Framework), IEEE 1516.1-2010 (Interface Spec), IEEE 1516.2-2010 (OMT) |
| **RTI** | Open-source RTI (OpenRTI or Portico); avoids proprietary RTI licensing |
| **FOM** | RPR-FOM v2.0 (Real-time Platform Reference FOM) — NATO standard for training |
| **Federate Name** | CORTEX-RANGE-{range_id} |

### 7.3 Object Model Mapping

| RPR-FOM Object | CORTEX CDM Source | Direction | Notes |
|----------------|-------------------|-----------|-------|
| Platform (Human) | SoldierProfile + PositionEvent | Publish | Soldier entity with position |
| WeaponFire | ShotEvent | Publish | Weapon fired interaction |
| MunitionDetonation | ShotEvent (impact) | Publish | Impact position and result |
| CustomInteraction: TrainingMetric | SessionProfile + analytics | Publish | CORTEX-specific FOM extension |

### 7.4 Test Method

| Test | Pass Criteria | Phase |
|------|---------------|-------|
| Federation join/resign | CORTEX federate joins/resigns cleanly | Phase 3 |
| Object publication | RPR-FOM objects visible to other federates | Phase 3 |
| Time management | Event-driven with timestamp order delivery | Phase 3 |
| CAE Rise interop | CAE Rise receives CORTEX training data | Phase 4 |

| **Estimated cost** | **$5,000** (3 weeks development + 2 weeks integration testing) |
| **Priority** | WISH — Phase 3+ |
| **Applicable Requirements** | [[requirements_list.md#INT-010]] |

---

## 8. ISO/IEC 25010:2023 — SOFTWARE QUALITY MODEL

### 8.1 Applicability

ISO 25010 defines 8 quality characteristics for software products. CORTEX RANGE uses this as a structured framework to ensure comprehensive quality coverage beyond functional requirements.

### 8.2 Quality Characteristic Mapping

| Characteristic | Sub-characteristic | CORTEX Requirement | Target | Verification |
|---------------|-------------------|-------------------|--------|-------------|
| **Functional Suitability** | Functional completeness | FUN-001 to FUN-024 | 100% of MUST implemented | D |
| | Functional correctness | QUA-003 (≤1mm error), QUA-004 (±0.5mm), QUA-007 | 100% accuracy | T |
| | Functional appropriateness | UXP-001 (≤4h training) | Task success rate ≥95% | D |
| **Performance Efficiency** | Time behavior | PER-001 (500 events/min), PER-002 (≤100ms) | Within specified limits | T |
| | Resource utilization | HST-001 (≤8GB RAM), HST-002 (≤60W) | Within hardware envelope | T |
| | Capacity | PER-003 (≥20 users), PER-008 (≥1000 events/s burst) | Load test verified | T |
| **Compatibility** | Co-existence | SEC-010 (network segmentation) | No interference with range systems | T |
| | Interoperability | INT-006 (DIS), INT-007 (TAK), INT-010 (HLA) | Protocol conformance tested | T |
| **Usability** | Learnability | UXP-001 (≤4h), UXP-002 (≤4h) | Measured in field trial | D |
| | Operability | UXP-003 (≤3 actions), UXP-005 (auto-recovery) | Task efficiency measured | D |
| | User interface aesthetics | UXD-001 to UXD-010 | User satisfaction ≥4/5 | D |
| | Accessibility | UXD-009 (color-blind), UXD-002 (sunlight) | WCAG 2.1 AA (optional) | I |
| **Reliability** | Maturity | QUA-001 (≥99.5% uptime) | Measured over ≥30 operating days | T |
| | Availability | QUA-001, HST-006 (offline ≥30 days) | Verified in field deployment | D |
| | Fault tolerance | UXP-005 (sensor recovery ≤10s), OPS-002 (≥8h unattended) | Fault injection test | T |
| | Recoverability | DST-006 (rollback ≤5 min), OPS-004 (daily backup) | Recovery test | D |
| **Security** | Confidentiality | SEC-004 (TLS), SEC-005 (AES-256), SEC-009 | Penetration test | T |
| | Integrity | QUA-002 (zero data loss), SEC-007 (audit), QUA-010 | Integrity verification | T |
| | Non-repudiation | SEC-007 (tamper-evident log) | Log chain validation | T |
| | Accountability | SEC-003 (RBAC), SEC-007 (audit) | Audit trail completeness | I |
| | Authenticity | SEC-002 (JWT auth) | Authentication test | T |
| **Maintainability** | Modularity | MOD-001 (plugin), MOD-002 (microservice) | Architecture review | A |
| | Reusability | ARC-006 (CDM), ARC-008 (API-first) | API coverage ≥90% | I |
| | Analysability | OPS-006 (structured logging), MNT-004 (self-diagnostics) | ≥90% issue diagnosis | D |
| | Modifiability | MOD-006 (feature flags), MOD-007 (migration) | Change impact analysis | A |
| | Testability | DEP-008 (CI/CD, ≥80% coverage) | Unit test coverage measured | I |
| **Portability** | Adaptability | ARC-009 (containers), HST-005 (K8s) | Runs on ARM + x86 | T |
| | Installability | DEP-001 (≤2h), DEP-002 (single command) | Installation time measured | D |
| | Replaceability | ARC-006 (open CDM), INT-011 (CDM export) | Data exportable in ≤1 hour | D |

---

## 9. MIL-STD-882E — SYSTEM SAFETY (AI CLASSIFICATION INFLUENCE)

### 9.1 Applicability

CORTEX RANGE includes AI-based coaching (FUN-012, FUN-015) and performance analytics (FUN-005, FUN-018) that influence training decisions. While CORTEX RANGE does not control weapons or make engagement decisions, its AI outputs influence:
- Qualification pass/fail recommendations
- Training resource allocation
- Soldier performance evaluations
- Unit readiness assessments

Misclassification could lead to: unqualified soldier deployed, training resources misallocated, or unjust performance evaluation.

### 9.2 Hazard Identification

| Hazard ID | Hazard | Severity | Probability | Risk Level | Mitigation |
|-----------|--------|----------|-------------|------------|------------|
| **H-R01** | AI misclassifies technique error → wrong coaching → reinforced bad habit | III (Marginal) | B (Probable) | Medium | Instructor override (FUN-017); AI confidence display; instructor feedback loop improves model |
| **H-R02** | False positive qualification prediction → soldier deployed without adequate skill | II (Critical) | D (Remote) | Medium | AI prediction is advisory only; official qualification still requires human-scored live-fire; QUA-008 (≥75% accuracy) |
| **H-R03** | Data corruption → incorrect performance records → wrong training decisions | III (Marginal) | D (Remote) | Low | QUA-002 (zero data loss); QUA-010 (integrity audit); SEC-007 (audit trail) |
| **H-R04** | Bias in AI training data → systematic underperformance assessment for certain weapon types | III (Marginal) | C (Occasional) | Medium | Balanced training dataset; per-weapon-type accuracy reporting; QUA-009 (confidence calibration) |
| **H-R05** | System outage during qualification exercise → lost scoring data → repeat exercise | IV (Negligible) | C (Occasional) | Low | QUA-001 (99.5% uptime); HST-007 (UPS backup); QUA-002 (zero data loss) |

### 9.3 Safety Design Requirements

| Requirement | Description | Applicable Hazard |
|-------------|-------------|-------------------|
| **SDR-R01** | All AI outputs shall display confidence score; no AI recommendation presented without confidence level | H-R01, H-R02, H-R04 |
| **SDR-R02** | Instructor/officer can override any AI classification/recommendation; override logged with reason | H-R01 |
| **SDR-R03** | AI predictions are advisory only — official qualification requires human authorization | H-R02 |
| **SDR-R04** | Per-weapon-type accuracy metrics reported; AI model accuracy monitored in production | H-R04 |
| **SDR-R05** | All scoring data buffered to non-volatile storage before session end acknowledgment | H-R03, H-R05 |

### 9.4 Software Criticality Level

| Parameter | Value |
|-----------|-------|
| **Software Criticality** | Level C — "Advisory output influencing training decisions" |
| **Rationale** | AI output is advisory; human operator makes all decisions; no autonomous action. Level C (not A/B) because: no weapon control, no autonomous engagement, no safety-critical real-time control. |
| **Equivalent** | Analogous to DO-178C DAL-D (no effect on safety) to DAL-C (major) — closer to DAL-D because operator override is always available |
| **Testing Rigor** | Statement coverage ≥80% for scoring engine; decision coverage for qualification logic; manual review of AI model training pipeline |

---

## 10. TCVN & VIETNAMESE LAW — NATIONAL COMPLIANCE

### 10.1 Vietnamese Cybersecurity Law (Luật An Ninh Mạng 2018, No. 24/2018/QH14)

| Article | Requirement | CORTEX Compliance | Requirements |
|---------|-------------|-------------------|-------------|
| **Art. 19** | Critical information system (CIS) protection | Military training system likely classified as CIS; requires security assessment | SEC-008, SEC-012 |
| **Art. 23** | Domestic data storage | Training data stored on-premises in Vietnam (edge server at range); no foreign cloud | SEC-006, HST-006 |
| **Art. 26** | Data classification and protection | Training performance data classified RESTRICTED; encrypted at rest and in transit | SEC-001, SEC-004, SEC-005 |
| **Art. 29** | Security incident reporting | Incident response plan includes reporting to MoND CERT | SEC-012 |
| **Art. 35** | Information system security audit | Annual security audit requirement for CIS | SEC-008 (pen test), MNT-001 (quarterly updates) |

### 10.2 Vietnamese Personal Data Protection (Decree 13/2023/NĐ-CP)

| Requirement | CORTEX Compliance | Requirements |
|-------------|-------------------|-------------|
| **Consent** | Soldier training data collected under military authority (consent implied by service); disclosure to unit commander per chain of command | SEC-001 |
| **Purpose limitation** | Data used only for training analytics; no secondary commercial use | SEC-001 |
| **Data minimization** | Collect only training-relevant data; no biometric data in Phase 1 | SEC-009 |
| **Storage limitation** | Configurable data retention (OPS-007); auto-archive after threshold | OPS-007 |
| **Security** | Encryption at rest/transit; RBAC; audit logging | SEC-004, SEC-005, SEC-003, SEC-007 |
| **Data subject rights** | Soldier can view own data (FUN-011); data deletion capability (SEC-009) | FUN-011, SEC-009 |
| **Cross-border transfer** | No cross-border transfer — all data on-premises in Vietnam | SEC-006 |

### 10.3 TCVN Standards

| TCVN | Title | IEC/ISO Equivalent | Applicability | Compliance Approach |
|------|-------|--------------------|--------------|---------------------|
| **TCVN 11930:2017** | Information technology — Security techniques — Information security management | ISO/IEC 27001:2013 | ISMS framework for CORTEX deployment | Align processes; formal certification optional |
| **TCVN 12482:2018** | Information security for web applications | OWASP alignment | Web application security for CORTEX dashboard | Covered by OWASP Top 10 compliance (Section 2) |
| **TCVN 7563:2005** | Information technology — Software product quality | ISO/IEC 9126 (predecessor to 25010) | Software quality model | Covered by ISO 25010 compliance (Section 8) |
| **TCVN 12480:2018** | Information security incident management | ISO/IEC 27035 | Security incident response | Covered by SEC-012 |
| **TCVN 11386:2016** | Electronic signature and digital certificate | Law on Electronic Transactions | Digital signature for qualification certificates (FUN-024) | Phase 2; use Vietnamese PKI |

### 10.4 Vietnamese MoND Standards (TBD)

| Standard | Status | Notes |
|----------|--------|-------|
| QĐ-BQP (MoND Decision) on military software | **TBD-004** | Vietnamese Ministry of National Defence may have internal standards for military software systems. Must consult with MoND IT department. |
| Vietnamese military data classification scheme | **TBD-008** | Confirm RESTRICTED level appropriate for training performance data. |
| Vietnamese military network security requirements | **TBD-004** | May specify additional network segmentation or encryption requirements. |

---

## 11. WCAG 2.1 — WEB CONTENT ACCESSIBILITY (OPTIONAL)

### 11.1 Applicability

WCAG 2.1 Level AA is an optional standard that improves usability for military users in challenging field conditions (bright sunlight, stress, fatigue, color vision deficiency).

### 11.2 Relevant Success Criteria

| WCAG Criterion | Level | CORTEX Implementation | Requirements |
|---------------|-------|----------------------|-------------|
| **1.4.3** Color contrast | AA | ≥4.5:1 contrast ratio for text; ≥3:1 for large text | UXD-002 (high-contrast mode) |
| **1.4.1** Use of color | A | Information not conveyed by color alone; shape/pattern used | UXD-009 (color-blind accessible) |
| **1.4.11** Non-text contrast | AA | UI components ≥3:1 contrast against background | UXD-002 |
| **2.5.5** Target size | AAA | Touch targets ≥44×44px | UXP-009 (touch-optimized) |
| **3.1.1** Language of page | A | `lang="vi"` attribute on HTML; Vietnamese content | UXP-004 (Vietnamese) |
| **2.1.1** Keyboard access | A | All functions accessible via keyboard (for laptop users) | — (implicit in web standards) |

### 11.3 Compliance Level

| Target | Rationale |
|--------|-----------|
| **WCAG 2.1 Level A** — Phase 1 | Basic accessibility; low effort; good practice |
| **WCAG 2.1 Level AA** — Phase 2+ (WISH) | Enhanced accessibility; requires dedicated effort for color contrast audit |

---

## 12. OpenAPI 3.0 / JSON SCHEMA — API & DATA STANDARDS

### 12.1 OpenAPI 3.0

| Parameter | Value |
|-----------|-------|
| **Standard** | OpenAPI Specification 3.0.3 (formerly Swagger) |
| **Applicability** | All CORTEX REST API endpoints (INT-004) |
| **Implementation** | FastAPI auto-generates OpenAPI 3.0 spec from Python type annotations + Pydantic models |
| **Documentation** | Interactive Swagger UI at `/docs`; ReDoc at `/redoc`; downloadable OpenAPI JSON at `/openapi.json` |
| **Versioning** | URL path versioning: `/api/v1/`, `/api/v2/` |
| **Applicable Requirements** | [[requirements_list.md#INT-004]], [[requirements_list.md#ARC-008]] |

### 12.2 JSON Schema (CDM)

| Parameter | Value |
|-----------|-------|
| **Standard** | JSON Schema Draft 2020-12 |
| **Applicability** | CORTEX CDM v1.0 specification (ARC-006) — 8 core objects |
| **Publication** | Open specification published as JSON Schema files in CORTEX repository |
| **Validation** | All CDM data validated against schema at ingestion; schema violations rejected with error |
| **Extension** | `additionalProperties` + `x-cortex-*` extension namespace for deployment-specific fields |
| **Applicable Requirements** | [[requirements_list.md#ARC-006]], [[requirements_list.md#MOD-003]], [[requirements_list.md#INT-011]] |

### 12.3 CDM Schema Objects

| Object | JSON Schema File | Key Fields | Validates |
|--------|-----------------|------------|-----------|
| ShotEvent | `shot_event.schema.json` | timestamp, lane_id, position_x_mm, position_y_mm, score, weapon_type | Every shot from VN-LOMAH |
| TechniqueEvent | `technique_event.schema.json` | timestamp, soldier_id, error_type, confidence, video_frame_ref | AI coaching output |
| PositionEvent | `position_event.schema.json` | timestamp, soldier_id, lat, lon, altitude, source | GPS/BLE tracker data |
| WeaponEvent | `weapon_event.schema.json` | timestamp, weapon_id, event_type (fire, reload, malfunction) | Weapon system integration |
| SoldierProfile | `soldier_profile.schema.json` | soldier_id, name, unit_id, rank, weapon_qualifications | Master soldier record |
| UnitProfile | `unit_profile.schema.json` | unit_id, name, parent_unit_id, strength, readiness_score | Unit hierarchy |
| SessionProfile | `session_profile.schema.json` | session_id, range_id, exercise_type, start_time, end_time, lanes | Training session metadata |
| ScenarioProfile | `scenario_profile.schema.json` | scenario_id, target_sequence, scoring_rules, time_limits | Exercise configuration |

---

## 13. COMPLIANCE STRATEGY

### 13.1 Compliance Approach Matrix

| Standard | Full Compliance | Tailored | Analysis | Self-Declaration |
|----------|----------------|----------|----------|-----------------|
| OWASP Top 10 | X (pen test) | | | |
| NIST CSF v2.0 | | X (Tier 2-3) | | |
| IEC 62443 SL-2 | | X (FRs only) | | |
| DIS IEEE 1278.1 | X (Level 1) | | | |
| CoT/TAK | X (basic) | | | |
| HLA IEEE 1516 | | X (Phase 3) | | |
| ISO 25010 | | | X | |
| MIL-STD-882E | | X (SW Level C) | X | |
| TCVN/Vietnamese Law | X | | | |
| WCAG 2.1 | | X (Level A) | | |
| OpenAPI 3.0 | X (auto-generated) | | | |
| JSON Schema | X (CDM) | | | |

### 13.2 Compliance Methods

| Method | Definition | When Used |
|--------|-----------|-----------|
| **Full Compliance** | Complete implementation per standard requirements, verified by test or audit | Critical standards; contractual requirements |
| **Tailored** | Selected clauses implemented; deviations documented and justified | Where full standard exceeds CORTEX scope |
| **Analysis** | Engineering analysis demonstrates compliance without formal testing | Where testing is impractical or standard is framework-oriented |
| **Self-Declaration** | Workshop X declares compliance based on internal assessment | Low-priority standards; competitive differentiator |

---

## 14. COMPLIANCE SCHEDULE

### 14.1 Phase-by-Phase Standards Activities

| Phase | Standards Activity | Deliverable |
|-------|-------------------|-------------|
| **Phase 1** | Standards mapping (this document); OWASP threat model; CDM JSON Schema v1.0; DIS/CoT implementation | Standards mapping; threat model; CDM schema files; DIS/CoT integration |
| **Phase 2** | Penetration test; MIL-STD-882E hazard analysis for AI; HLA design study; WCAG Level A audit | Pen test report; hazard analysis; HLA integration design; accessibility report |
| **Phase 3** | IEC 62443 SL-2 assessment; HLA implementation + test; NIST CSF gap analysis | SL-2 compliance report; HLA test report; CSF action plan |
| **Phase 4-5** | Annual security audit; TCVN compliance confirmation with MoND; ISO 27001 alignment (if required) | Annual audit report; TCVN compliance statement |

### 14.2 Timeline Estimate

| Activity | Start | Duration | End | Dependencies |
|----------|-------|----------|-----|-------------|
| Standards mapping | Phase 1 W1 | 1 week | Phase 1 W2 | None |
| CDM JSON Schema v1.0 | Phase 1 Sprint 1 | 2 weeks | Phase 1 Sprint 1 | ARC-006 definition |
| DIS implementation | Phase 2 Sprint 1 | 2 weeks | Phase 2 Sprint 2 | CDM + Open-DIS library |
| CoT/TAK implementation | Phase 2 Sprint 1 | 1 week | Phase 2 Sprint 2 | CDM + PyTAK library |
| OWASP pen test | Phase 1 Sprint 6 | 2 weeks | Phase 1 end | All Phase 1 features complete |
| MIL-STD-882E AI hazard analysis | Phase 2 Sprint 3 | 2 weeks | Phase 2 Sprint 4 | AI classification functional |
| HLA integration | Phase 3 | 3 weeks | Phase 3 | OpenRTI + RPR-FOM |
| IEC 62443 SL-2 assessment | Phase 3 | 2 weeks | Phase 3 | All security controls implemented |
| NIST CSF gap analysis | Phase 3 | 1 week | Phase 3 | All CSF controls implemented |
| Annual security audit | Phase 4+ | 2 weeks | Annual | Previous audit findings resolved |

---

## 15. COST ESTIMATES FOR STANDARDS COMPLIANCE

### 15.1 Total Compliance Cost Summary

| Standard | Est. Cost (USD) | Phase | Notes |
|----------|-----------------|-------|-------|
| OWASP Top 10 (pen test) | $8,000 | Phase 1 | External pentester or qualified internal |
| OWASP Top 10 (remediation) | $3,000 | Phase 1 | Developer time to fix findings |
| NIST CSF v2.0 (gap analysis + plan) | $2,000 | Phase 3 | Internal assessment with template |
| IEC 62443 SL-2 (assessment) | $4,000 | Phase 3 | External assessor or qualified internal |
| DIS IEEE 1278.1 (implementation + test) | $3,000 | Phase 2 | Open-DIS library; 2+1 weeks dev+test |
| CoT/TAK (implementation + test) | $2,000 | Phase 2 | PyTAK library; 1+1 weeks dev+test |
| HLA IEEE 1516 (implementation + test) | $5,000 | Phase 3 | OpenRTI; 3+2 weeks dev+test |
| ISO 25010 (quality analysis) | $1,000 | Phase 2 | Internal analysis using template |
| MIL-STD-882E (AI hazard analysis) | $3,000 | Phase 2 | Internal analysis; 2 weeks |
| TCVN compliance (legal review) | $2,000 | Phase 1-2 | Legal consultant for Cybersecurity Law |
| WCAG 2.1 (accessibility audit) | $1,000 | Phase 2 | Semi-automated (axe-core) + manual |
| OpenAPI/JSON Schema (CDM publish) | $1,000 | Phase 1 | Developer time for schema documentation |
| Annual security audit (ongoing) | $5,000/year | Phase 4+ | Annual pen test + vulnerability scan |
| **TOTAL (Phase 1-3)** | **$35,000** | | |
| **TOTAL (Annual ongoing)** | **$5,000/year** | | |

### 15.2 Cost Comparison with Hardware Standards

| | VN-CUAS-001 (Hardware) | CORTEX RANGE (Software) | Savings |
|--|------------------------|------------------------|---------|
| Environmental (MIL-STD-810H) | $63,500 | $0 (COTS hardware) | 100% |
| EMC (MIL-STD-461G) | $28,500 | $0 (COTS hardware) | 100% |
| IP67 (IEC 60529) | $2,500 | $0 (COTS hardware) | 100% |
| Battery (UN 38.3) | $10,000 | $0 (COTS power) | 100% |
| Safety (MIL-STD-882E) | $37,000 | $3,000 (SW only) | 92% |
| Reliability (MIL-HDBK-217F) | $40,000 | $0 (SW reliability via testing) | 100% |
| Cybersecurity | $15,000 | $19,000 (primary focus) | -27% |
| Interoperability | $0 | $10,000 (DIS/TAK/HLA) | N/A |
| Software quality | $30,000 | $5,000 | 83% |
| **TOTAL** | **$226,500** | **$35,000** | **85%** |

> **Key insight:** Software products have fundamentally different compliance costs. Hardware dominates VN-CUAS qualification budget; cybersecurity and interoperability dominate CORTEX RANGE budget. Total standards compliance is ~85% cheaper for software.

---

## 16. CROSS-REFERENCE: REQUIREMENTS TO STANDARDS

### 16.1 Requirement-to-Standard Traceability Matrix

| Requirement ID | Requirement Description | Standard | Clause/Section | Compliance Approach |
|----------------|------------------------|----------|----------------|---------------------|
| [[requirements_list.md#SEC-001]] | Data classification handling (RESTRICTED) | Vietnamese Cybersecurity Law Art. 26; NIST CSF GV.OC | Art. 26 | Full |
| [[requirements_list.md#SEC-002]] | JWT authentication, session timeout, password policy | OWASP A07; IEC 62443 FR1; NIST CSF PR.AA | A07, FR1 | Full |
| [[requirements_list.md#SEC-003]] | RBAC (4 roles, granular permissions) | OWASP A01; IEC 62443 FR2; NIST CSF PR.AA | A01, FR2 | Full |
| [[requirements_list.md#SEC-004]] | TLS 1.3 in transit | OWASP A02; IEC 62443 FR4; NIST CSF PR.DS | A02, FR4 | Full |
| [[requirements_list.md#SEC-005]] | AES-256 at rest | OWASP A02; IEC 62443 FR4; NIST CSF PR.DS | A02, FR4 | Full |
| [[requirements_list.md#SEC-006]] | Air-gapped deployment | Vietnamese Cybersecurity Law Art. 23; NIST CSF PR.IR | Art. 23 | Full |
| [[requirements_list.md#SEC-007]] | Tamper-evident audit logging | OWASP A09; IEC 62443 FR3; NIST CSF DE.AE | A09, FR3 | Full |
| [[requirements_list.md#SEC-008]] | OWASP Top 10 compliance | OWASP Top 10 (2021); TCVN 12482 | All A01-A10 | Full (pen test) |
| [[requirements_list.md#SEC-009]] | Personal data protection | Vietnamese Decree 13/2023; OWASP A02 | Decree 13 | Full |
| [[requirements_list.md#SEC-010]] | Network segmentation | IEC 62443 FR5; NIST CSF PR.IR | FR5 | Full |
| [[requirements_list.md#SEC-011]] | Backup encryption | OWASP A02; NIST CSF RC.RP | A02 | Full |
| [[requirements_list.md#SEC-012]] | Security incident response plan | Vietnamese Cybersecurity Law Art. 29; NIST CSF RS.MA | Art. 29 | Tailored |
| [[requirements_list.md#INT-004]] | REST API (OpenAPI 3.0) | OpenAPI 3.0.3 | Spec | Full (auto-gen) |
| [[requirements_list.md#INT-006]] | DIS IEEE 1278 output | IEEE 1278.1-2012 | PDU format | Full (Level 1) |
| [[requirements_list.md#INT-007]] | CoT/TAK plugin | MIL-PRF-49503; TAK SDK | CoT schema | Full |
| [[requirements_list.md#INT-010]] | HLA IEEE 1516 federate | IEEE 1516-2010 | RPR-FOM v2.0 | Tailored (Phase 3) |
| [[requirements_list.md#ARC-006]] | CDM v1.0 JSON Schema | JSON Schema Draft 2020-12 | Schema spec | Full |
| [[requirements_list.md#ARC-007]] | FOSS-only dependencies | NIST CSF GV.SC (supply chain) | GV.SC | Full |
| [[requirements_list.md#ARC-008]] | API-first architecture | OpenAPI 3.0.3 | Spec | Full (auto-gen) |
| [[requirements_list.md#QUA-001]] | ≥99.5% uptime | ISO 25010 Reliability | Availability | Analysis + Test |
| [[requirements_list.md#QUA-002]] | Zero data loss | IEC 62443 FR3; ISO 25010 Reliability | FR3, Recoverability | Test |
| [[requirements_list.md#QUA-003]] | Shot scoring accuracy ≤1mm | ISO 25010 Functional Correctness | Correctness | Test |
| [[requirements_list.md#QUA-005]] | AI coaching relevance ≥80% | MIL-STD-882E (H-R01); ISO 25010 | SDR-R01, SDR-R04 | Demo |
| [[requirements_list.md#QUA-006]] | AI classification accuracy ≥80% | MIL-STD-882E (H-R04); ISO 25010 | SDR-R04 | Test |
| [[requirements_list.md#UXD-002]] | Field-readable display | WCAG 2.1 (1.4.3, 1.4.11) | Color contrast | Inspection |
| [[requirements_list.md#UXD-009]] | Color-blind accessible | WCAG 2.1 (1.4.1) | Use of color | Inspection |
| [[requirements_list.md#UXP-001]] | Training time ≤4h | ISO 25010 Usability | Learnability | Demo |
| [[requirements_list.md#UXP-004]] | Vietnamese language | WCAG 2.1 (3.1.1) | Language of page | Inspection |
| [[requirements_list.md#UXP-009]] | Touch targets ≥44×44px | WCAG 2.1 (2.5.5) | Target size | Inspection |
| [[requirements_list.md#DEP-002]] | Single-command deployment | ISO 25010 Portability | Installability | Demo |
| [[requirements_list.md#OPS-003]] | System health monitoring | NIST CSF DE.CM | Continuous monitoring | Demo |
| [[requirements_list.md#OPS-004]] | Automated daily backup | NIST CSF RC.RP; IEC 62443 FR7 | RC.RP, FR7 | Test |
| [[requirements_list.md#OPS-006]] | Structured logging (JSON) | OWASP A09; NIST CSF DE.AE | A09 | Inspection |
| [[requirements_list.md#MNT-001]] | ≥4 updates/year | OWASP A06 (component hygiene) | A06 | Analysis |
| [[requirements_list.md#MNT-003]] | Backward data compatibility | ISO 25010 Maintainability | Modifiability | Test |
| [[requirements_list.md#MOD-001]] | Plugin architecture | ISO 25010 Maintainability | Modularity | Analysis |
| [[requirements_list.md#MOD-002]] | Microservice separation | ISO 25010 Maintainability | Modularity | Analysis |
| [[requirements_list.md#MOD-003]] | CDM extensibility | JSON Schema Draft 2020-12 | additionalProperties | Test |
| [[requirements_list.md#DST-003]] | Browser compatibility | WCAG 2.1 (general) | Cross-browser | Test |
| [[requirements_list.md#FUN-017]] | Instructor override of AI | MIL-STD-882E (SDR-R02) | H-R01 | Demo |

**Total requirements traced to standards: 74/157 (47%)** — remaining requirements are product-specific (not standard-driven) such as specific functional features, pricing, and schedule.

---

## 17. TBDs AND GAPS

### 17.1 Open TBDs

| TBD ID | Description | Owner | Target Resolution | Impact |
|--------|-------------|-------|-------------------|--------|
| **TBD-004** | TCVN software standards — which Vietnamese standards apply to military training software | S12 (Regulator) | Q2 2026 | May add requirements to SEC, QUA categories |
| **TBD-008** | Data classification confirmation — RESTRICTED vs INTERNAL for training performance data | S13 (Cybersecurity) | Phase 1 Sprint 4 | Determines SEC requirements stringency |
| **TBD-009** | Partner integration priority — DIS vs TAK: which protocol first? | S11 (Partners) | Phase 2 start | Affects INT-006 vs INT-007 priority |
| **TBD-015** | Vietnamese military network architecture — specific firewall/VLAN requirements for deployment | S7 (IT Admin) | Phase 1 Sprint 5 | Affects IEC 62443 zone model and SEC-010 |
| **TBD-016** | MoND cybersecurity audit requirements — frequency, scope, accreditor | S12 (Regulator), S13 (Cybersecurity) | Phase 2 | Affects annual compliance budget |
| **TBD-017** | DIS exercise parameters — exercise ID allocation for Vietnamese training system | S11 (Partners) | Phase 2 | Affects DIS configuration; use workshop-allocated range for initial |
| **TBD-018** | Vietnamese PKI for digital signatures — which CA for qualification certificates | S12 (Regulator) | Phase 2 | Affects FUN-024 implementation; TCVN 11386 compliance |

### 17.2 Standards Gaps

| Gap | Description | Risk | Mitigation |
|-----|-------------|------|------------|
| **No standard for ML training analytics validation** | No accepted standard for validating ML-based training analytics accuracy in military context | Medium — customer may question AI reliability | Define internal validation procedure: confusion matrix per technique type, instructor feedback loop, production accuracy monitoring. Reference NIST AI 100-1 (AI Risk Management Framework). |
| **No DIS PDU for acoustic shot scoring** | DIS has Fire and Detonation PDUs but no standard PDU for acoustic shot scoring metadata (grouping, technique error) | Low — solvable with standard Data PDU | Use Data PDU (type 20) with CORTEX-defined datum values for training metrics. Document and publish extension for potential standardization. |
| **No Vietnamese standard for military software deployment** | No TCVN equivalent of DO-178C or MIL-STD-498 for military software | Medium — deployment approval may require ad-hoc process | Document CORTEX development process aligned with ISO 12207 (software lifecycle). Propose to MoND as template for future Vietnamese defense software projects. |
| **CDM has no industry standard** | No equivalent of STANAG for live-fire training data models | Low — this is the innovation opportunity | CORTEX CDM is the first open live-fire training data model. Publish as open specification. Propose to SISO for standardization consideration. |

---

## 18. DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-12 | Engineering Design System | Initial release — 12 standard families, 89 clauses mapped, 74 requirements traced |

---

*This document will be updated as TBDs are resolved and Vietnamese MoND-specific requirements are clarified.*
*Cross-reference: [[requirements_list.md]] for full requirement definitions.*
*Cross-reference: [[stakeholder_analysis.md]] for stakeholder-to-standard relationships.*
*Classification: UNCLASSIFIED*
