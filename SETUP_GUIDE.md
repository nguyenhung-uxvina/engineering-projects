# 📘 HƯỚNG DẪN THIẾT LẬP HỆ THỐNG
## Claude Code + Obsidian Engineering Design System

**Mục tiêu**: Thiết lập hệ thống hỗ trợ engineering design với:
- **Claude Code** làm AI engine (chạy local, truy cập file system)
- **Obsidian** làm knowledge vault (lưu trữ, liên kết, visualize)
- **Skills** theo Progressive Disclosure (load đúng lúc cần)

---

## 📋 TỔNG QUAN KIẾN TRÚC

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER (Local)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐         ┌─────────────────────────────┐   │
│  │   CLAUDE CODE   │◄───────►│        OBSIDIAN VAULT       │   │
│  │   (Terminal)    │  read/  │     (Markdown Files)        │   │
│  │                 │  write  │                             │   │
│  │  • Chạy tasks   │         │  • projects/                │   │
│  │  • Web search   │         │  • skills/                  │   │
│  │  • File ops     │         │  • templates/               │   │
│  │  • Scripts      │         │  • learning-journal/        │   │
│  └─────────────────┘         └─────────────────────────────┘   │
│           │                              ▲                      │
│           │                              │                      │
│           ▼                              │                      │
│  ┌─────────────────┐                     │                      │
│  │    SCRIPTS/     │                     │                      │
│  │    TOOLS        │─────────────────────┘                      │
│  │                 │     outputs to vault                       │
│  │  • VDI 2225     │                                            │
│  │  • Cost calc    │                                            │
│  │  • Reports      │                                            │
│  └─────────────────┘                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 BƯỚC 1: CÀI ĐẶT CLAUDE CODE

### 1.1 Cài đặt Claude Code CLI

```bash
# Mở Terminal (Mac/Linux) hoặc Command Prompt (Windows)

# Cài đặt qua npm
npm install -g @anthropic-ai/claude-code

# Hoặc nếu dùng yarn
yarn global add @anthropic-ai/claude-code

# Verify installation
claude --version
```

### 1.2 Cấu hình API Key

```bash
# Set API key (lấy từ console.anthropic.com)
claude config set api_key sk-ant-xxxxx

# Hoặc set environment variable
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### 1.3 Khởi tạo Claude Code trong project folder

```bash
# Navigate đến folder bạn muốn làm việc
cd ~/Documents/engineering-projects

# Khởi tạo Claude Code
claude init

# Điều này tạo ra:
# - .claude/ folder chứa config
# - CLAUDE.md file cho project instructions
```

---

## 📁 BƯỚC 2: THIẾT LẬP OBSIDIAN VAULT

### 2.1 Download và cài đặt Obsidian

```
1. Truy cập: https://obsidian.md/download
2. Download cho hệ điều hành của bạn
3. Cài đặt và chạy Obsidian
```

### 2.2 Tạo Vault mới

```
1. Mở Obsidian
2. Click "Create new vault"
3. Đặt tên: "Engineering-Design-System"
4. Chọn location: ~/Documents/engineering-projects/
5. Click "Create"
```

### 2.3 Cấu trúc thư mục Vault

Trong Obsidian, tạo cấu trúc thư mục sau:

```
Engineering-Design-System/        ← Obsidian Vault root
├── .obsidian/                    ← Obsidian config (auto-created)
├── CLAUDE.md                     ← Instructions cho Claude Code
├── SYSTEM.md                     ← System overview
├── QUICKSTART.md                 ← Quick reference
│
├── skills/                       ← Progressive Disclosure skills
│   ├── SKILL_overview.md
│   ├── SKILL_task_clarification.md
│   ├── SKILL_conceptual_design.md
│   ├── SKILL_embodiment_design.md
│   └── SKILL_dmir_learning.md
│
├── vault/
│   ├── projects/                 ← Từng dự án
│   │   ├── PROJECT_INDEX.md
│   │   ├── VN-TARGET-BB01/
│   │   ├── V-SMASH/
│   │   └── ... (other projects)
│   │
│   ├── templates/                ← Templates
│   │   ├── project_template.md
│   │   ├── requirements_template.md
│   │   └── weekly_reflection_template.md
│   │
│   ├── references/               ← Reference documents
│   │   ├── defense-standards.md
│   │   ├── vietnamese-suppliers.md
│   │   └── mil-std-mapping.md
│   │
│   └── learning-journal/         ← D-M-I-R reflections
│       ├── weekly/
│       └── monthly/
│
├── scripts/                      ← Python tools
│   ├── vdi2225_calculator.py
│   └── cost_calculator.py
│
└── assets/                       ← Images, diagrams
    └── diagrams/
```

### 2.4 Copy files từ output vào Vault

```bash
# Trong Terminal, copy files đã tạo vào Obsidian vault
cp -r ~/Downloads/engineering-design-system/* ~/Documents/engineering-projects/Engineering-Design-System/
```

---

## 📝 BƯỚC 3: TẠO CLAUDE.md (Project Instructions)

File này là **"system prompt"** cho Claude Code - nó sẽ đọc file này mỗi khi bạn chạy Claude trong folder này.

### 3.1 Tạo file CLAUDE.md trong vault root

```markdown
# CLAUDE.md - Engineering Design System Instructions

## Role
You are a defense systems engineering mentor specializing in Pahl & Beitz systematic design methodology with D-M-I-R (Diagnosis-Modeling-Intervention-Reflection) framework integration.

## Context
This is an Obsidian vault containing engineering design projects for Vietnamese defense/security products. You have access to read and write files in this vault.

## Progressive Disclosure Rules
1. **Always read** `skills/SKILL_overview.md` first for context
2. **Load on-demand** based on user request:
   - Phase 1 work → read `skills/SKILL_task_clarification.md`
   - Phase 2 work → read `skills/SKILL_conceptual_design.md`
   - Phase 3 work → read `skills/SKILL_embodiment_design.md`
   - Learning/reflection → read `skills/SKILL_dmir_learning.md`
3. **Never load all skills at once** - conserve context window

## Workflow Commands
When user says:
- "Tiếp tục [project]" → Read PROJECT_INDEX.md, find project, load context
- "Tạo dự án mới" → Use templates/project_template.md
- "Tạo requirements" → Load SKILL_task_clarification.md
- "Đánh giá concepts" → Run scripts/vdi2225_calculator.py
- "Weekly reflection" → Use templates/weekly_reflection_template.md

## File Operations
- Create new files in appropriate vault/projects/VN-XXX/ folders
- Use proper markdown formatting with Obsidian wiki-links [[like this]]
- Update PROJECT_INDEX.md when project status changes

## Language
- Technical content: English preferred for international standards
- Communication with user: Vietnamese or English based on user preference
- File names: English with underscores

## Quality Standards
- Requirements must be quantified with MUST/WISH classification
- VDI 2225 evaluations require minimum 70% score for defense products
- All designs must consider local content (target 60-75%)
```

---

## 🚀 BƯỚC 4: SỬ DỤNG CLAUDE CODE

### 4.1 Khởi động Claude Code

```bash
# Navigate to vault folder
cd ~/Documents/engineering-projects/Engineering-Design-System

# Start Claude Code
claude

# Claude sẽ tự động đọc CLAUDE.md và hiểu context
```

### 4.2 Session đầu tiên - Verify setup

```
You: Kiểm tra hệ thống đã setup đúng chưa

Claude: [Sẽ đọc CLAUDE.md, check folder structure, verify files]

Claude output:
✅ CLAUDE.md found - instructions loaded
✅ skills/ folder with 5 skill files
✅ vault/projects/ folder exists
✅ templates/ folder with 3 templates
✅ scripts/vdi2225_calculator.py available

Hệ thống sẵn sàng. Bạn muốn làm gì?
- "Tiếp tục [project]" - Load existing project
- "Tạo dự án mới" - Start new project
- "Weekly reflection" - D-M-I-R learning
```

### 4.3 Ví dụ: Tiếp tục dự án V-SMASH

```
You: Tiếp tục V-SMASH

Claude: [Reads PROJECT_INDEX.md]
        [Reads vault/projects/V-SMASH/ folder]
        [Loads SKILL_conceptual_design.md vì project đang ở Phase 2]

Claude output:
📂 V-SMASH - 12.7mm C-UAS Fire Control System
├── Status: Phase 2 - Conceptual Design v1.1
├── Last updated: [date]
└── Next action: Stakeholder review

Current deliverables:
- ✅ Requirements List complete
- ✅ Function Structure complete
- ✅ Morphological Matrix complete
- ✅ 5 concepts evaluated with VDI 2225
- 🔄 Stakeholder review pending

Bạn muốn:
1. Review concept evaluation results
2. Prepare stakeholder presentation
3. Move to Phase 3 (Embodiment Design)
```

### 4.4 Ví dụ: Tạo dự án mới

```
You: Tạo dự án mới: Hệ thống trinh sát biên giới tự động

Claude: [Reads templates/project_template.md]
        [Creates new folder: vault/projects/VN-BORDER-001/]
        [Loads SKILL_task_clarification.md]

Claude output:
📂 Created: VN-BORDER-001 - Hệ thống trinh sát biên giới tự động

Files created:
- vault/projects/VN-BORDER-001/00_project_brief.md
- Updated PROJECT_INDEX.md

Bắt đầu Phase 1: Task Clarification

Câu hỏi đầu tiên:
1. Ai là customer (đơn vị nào đặt hàng)?
2. Môi trường triển khai (rừng/núi/biển/đồng bằng)?
3. Budget dự kiến?
4. Timeline yêu cầu?
```

---

## 🔍 BƯỚC 5: OBSIDIAN FEATURES CHO ENGINEERING DESIGN

### 5.1 Cài đặt Obsidian Plugins hữu ích

```
Settings → Community Plugins → Browse

Recommended plugins:
1. Dataview - Query projects, create dashboards
2. Templater - Advanced templates
3. Excalidraw - Drawings và diagrams
4. Kanban - Project tracking boards
5. Calendar - Link daily notes với reflections
```

### 5.2 Tạo Dashboard với Dataview

Tạo file `DASHBOARD.md` trong vault root:

```markdown
# 📊 ENGINEERING DASHBOARD

## Active Projects by Phase

### Phase 1: Task Clarification
```dataview
TABLE status, next_action
FROM "vault/projects"
WHERE phase = 1
SORT file.mtime DESC
```

### Phase 2: Conceptual Design
```dataview
TABLE status, vdi_score
FROM "vault/projects"
WHERE phase = 2
SORT file.mtime DESC
```

## Recent Activity
```dataview
TABLE file.mtime as "Last Modified"
FROM "vault/projects"
SORT file.mtime DESC
LIMIT 10
```

## This Week's Learning
```dataview
LIST
FROM "vault/learning-journal/weekly"
WHERE file.ctime >= date(today) - dur(7 days)
```
```

### 5.3 Wiki-links giữa các documents

Trong Obsidian, sử dụng `[[wiki-links]]` để liên kết:

```markdown
## Requirements Traceability

Requirement REQ-001 được implement trong:
- [[05_embodiment_layout#Section-A|Embodiment Layout Section A]]
- Verified by [[07_verification_plan#TEST-001|Test Case 001]]

Related standards:
- [[references/mil-std-810|MIL-STD-810H Method 514]]
```

### 5.4 Graph View cho Project Relationships

```
1. Click "Open graph view" (icon bên trái)
2. Thấy visual connections giữa documents
3. Filter by folder để xem specific project
4. Identify orphan documents (không linked)
```

---

## 🔄 BƯỚC 6: DAILY WORKFLOW

### Morning Startup

```bash
# 1. Open Terminal
cd ~/Documents/engineering-projects/Engineering-Design-System

# 2. Start Claude Code
claude

# 3. Check status
You: Status hôm nay
```

### During Work Session

```
# Trong Claude Code terminal:

You: Tiếp tục VN-TARGET-BB01
[Claude loads context, shows status]

You: Tạo function structure
[Claude loads SKILL_conceptual_design.md, guides through process]
[Claude creates/updates files in vault]

# Đồng thời trong Obsidian:
# - Xem files được tạo/update real-time
# - Navigate với wiki-links
# - Visualize với graph view
```

### End of Day

```
You: Tổng kết hôm nay

Claude: [Summarizes work done]
        [Updates PROJECT_INDEX.md]
        [Suggests tomorrow's priorities]
```

### Weekly Reflection (Sunday)

```
You: Weekly reflection

Claude: [Loads SKILL_dmir_learning.md]
        [Creates vault/learning-journal/weekly/2026-W06-reflection.md]
        [Guides through D-M-I-R questions]
```

---

## ⚙️ BƯỚC 7: ADVANCED CONFIGURATIONS

### 7.1 Custom Scripts

Tạo thêm scripts cho specific tasks:

```bash
# scripts/cost_calculator.py
# scripts/local_content_analyzer.py
# scripts/requirements_validator.py
```

Chạy từ Claude Code:

```
You: Chạy cost analysis cho V-SMASH

Claude: [Runs scripts/cost_calculator.py với V-SMASH data]
        [Outputs results to vault/projects/V-SMASH/08_cost_analysis.md]
```

### 7.2 Obsidian Templates với Templater

```markdown
<%* 
// templates/requirement_entry.md
const req_id = await tp.system.prompt("Requirement ID (e.g., GEO-001):");
const category = await tp.system.suggester(
  ["Geometry", "Kinematics", "Forces", "Energy", "Material", "Signals", "Safety", "Ergonomics", "Production", "Quality", "Assembly", "Transport", "Operation", "Maintenance", "Costs", "Schedule"],
  ["Geometry", "Kinematics", "Forces", "Energy", "Material", "Signals", "Safety", "Ergonomics", "Production", "Quality", "Assembly", "Transport", "Operation", "Maintenance", "Costs", "Schedule"]
);
-%>

| <% req_id %> | [Description] | [Value] | MUST/WISH | A/I/T/D | [Source] | [Notes] |
```

### 7.3 Git Integration

```bash
# Initialize git trong vault
cd ~/Documents/engineering-projects/Engineering-Design-System
git init

# Create .gitignore
echo ".obsidian/workspace.json" >> .gitignore
echo ".obsidian/workspace-mobile.json" >> .gitignore

# Commit
git add .
git commit -m "Initial engineering design system setup"

# Optional: Push to private repo
git remote add origin git@github.com:username/engineering-design.git
git push -u origin main
```

---

## 🆘 TROUBLESHOOTING

### Claude Code không đọc được files

```bash
# Check permissions
ls -la ~/Documents/engineering-projects/Engineering-Design-System/

# Ensure Claude has access
claude config set workspace ~/Documents/engineering-projects/Engineering-Design-System
```

### Obsidian không refresh sau khi Claude tạo file

```
Settings → Files & Links → Enable "Detect all file extensions"
Settings → Editor → Enable "Auto-refresh"
```

### VDI 2225 script không chạy

```bash
# Ensure Python installed
python3 --version

# Run directly to test
cd scripts
python3 vdi2225_calculator.py --example
```

---

## 📌 QUICK REFERENCE CARD

```
┌────────────────────────────────────────────────────────────┐
│ CLAUDE CODE COMMANDS                                       │
├────────────────────────────────────────────────────────────┤
│ claude                    Start Claude Code                │
│ claude "message"          One-shot message                 │
│ claude --continue         Continue last conversation       │
│ Ctrl+C                    Exit Claude Code                 │
├────────────────────────────────────────────────────────────┤
│ IN-SESSION COMMANDS                                        │
├────────────────────────────────────────────────────────────┤
│ /help                     Show help                        │
│ /clear                    Clear conversation               │
│ /cost                     Show token usage                 │
├────────────────────────────────────────────────────────────┤
│ OBSIDIAN SHORTCUTS                                         │
├────────────────────────────────────────────────────────────┤
│ Cmd/Ctrl + O              Quick open file                  │
│ Cmd/Ctrl + P              Command palette                  │
│ Cmd/Ctrl + E              Toggle edit/preview              │
│ Cmd/Ctrl + G              Open graph view                  │
│ [[                        Start wiki-link                  │
└────────────────────────────────────────────────────────────┘
```

---

## ✅ SETUP CHECKLIST

- [ ] Claude Code installed và configured với API key
- [ ] Obsidian installed
- [ ] Vault created với đúng folder structure
- [ ] Files copied từ output vào vault
- [ ] CLAUDE.md created và configured
- [ ] Test Claude Code đọc được vault files
- [ ] Obsidian plugins installed (Dataview, Templater)
- [ ] First project loaded thành công
- [ ] Weekly reflection template tested

---

*Setup hoàn tất! Bắt đầu với: `claude` → "Tiếp tục [project]"*
