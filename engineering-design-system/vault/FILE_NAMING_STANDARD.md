# 📁 FILE NAMING STANDARD
## Engineering Design System - Naming Convention

**Last Updated**: 2026-02-03
**Version**: 1.0

---

## 🎯 PURPOSE

Ensure all project files are easily identifiable regardless of:
- Where they are opened (file explorer, editor tabs, search results)
- How many projects are active simultaneously
- Whether files are viewed in or out of their folder context

---

## 📋 NAMING CONVENTION

### Standard Format

```
PROJECTCODE_##_filename.md
```

**Components**:
- `PROJECTCODE` = Project identifier (e.g., V-SMASH, RCWS-127-NAVAL)
- `##` = Two-digit phase number (00-99)
- `filename` = Descriptive name (lowercase with underscores)
- `.md` = Markdown extension

### Examples

```
✅ GOOD:
V-SMASH_01_requirements_list.md
V-SMASH_02_function_structure.md
RCWS-127-NAVAL_00_project_brief.md
VN-TARGET-BB01_03_morphological_matrix.md

❌ BAD (old format):
01_requirements_list.md          (no project code)
requirements_list_V-SMASH.md     (code at end, hard to scan)
V-SMASH-requirements-list.md     (no phase number)
```

---

## 📂 FILE NUMBERING SYSTEM

### Standard Deliverable Numbers

| Number | Deliverable | Phase |
|--------|-------------|-------|
| `00` | Project brief / overview | N/A |
| `01` | Requirements list | Phase 1 |
| `02` | Function structure | Phase 2 |
| `03` | Morphological matrix | Phase 2 |
| `04` | Concept evaluation (VDI 2225) | Phase 2 |
| `05` | Embodiment layout | Phase 3 |
| `06` | Detail drawings folder | Phase 4 |
| `07` | Verification plan | Phase 4 |
| `08` | Cost analysis | Phase 4 |
| `99` | Lessons learned | Closure |

### Supporting Files

Supporting files (references, calculations, etc.) should also use project prefix:

```
V-SMASH_fire_control_reference.txt
V-SMASH_ballistics_calculations.xlsx
RCWS-127-NAVAL_stabilization_analysis.pdf
```

---

## 🔗 WIKI-LINK FORMAT

### Internal Links (within same project)

```markdown
[[PROJECTCODE_##_filename|Display Text]]

Example:
See [[V-SMASH_01_requirements_list|Requirements List]] for details.
```

### Cross-Project Links

```markdown
[[../OTHER-PROJECT/PROJECTCODE_##_filename|Display Text]]

Example:
Related to [[../V-SMASH/V-SMASH_00_project_brief|V-SMASH Fire Control]]
```

---

## 📊 CURRENT PROJECT CODES

### Active Projects

| Project Code | Full Name | Category |
|--------------|-----------|----------|
| **V-SMASH** | 12.7mm C-UAS Fire Control System | Training & Simulation |
| **RCWS-127-NAVAL** | 12.7mm Naval RCWS System | Naval Systems |
| VN-TARGET-BB01 | Marine Target Detection | Naval Systems |
| VN-RESCUE-DRONE-001 | Smart Flying Buoy | Naval Systems |
| VN-RC-TX-001-D | Defense Radio Transmitter | Communication |
| VN-TUAV-DEMO-001 | Tactical UAV Demo | UAV & Aerial |
| BMT-01-HN | [Training Equipment] | Training |
| VN-B41SIM-001 | B41 Rocket Simulator | Training |
| VN-ADTS-001 | Air Defense Training System | Training |
| VN-ARTY-FOS-001 | Artillery FO Simulator | Training |
| VN-TARGET-DRONE-001 | Target Drone System | UAV & Aerial |
| VN-MORTAR-SIM-001 | Mortar Firing Simulator | Training |
| VN-MANPADS-TRAINER | MANPADS IR Trainer | Training |
| VN-NAVAL-GUNNERY | Naval Gunnery Trainer | Naval Systems |

---

## ✅ IMPLEMENTATION CHECKLIST

When creating a new project:

- [ ] Choose unique project code (check existing codes above)
- [ ] Create project folder: `vault/projects/PROJECTCODE/`
- [ ] Name all files with prefix: `PROJECTCODE_##_filename.md`
- [ ] Use wiki-links with full prefixed names
- [ ] Update this document with new project code
- [ ] Update PROJECT_INDEX.md

---

## 🔄 MIGRATION STATUS

### Completed

- ✅ V-SMASH (7 files renamed + links updated)
- ✅ RCWS-127-NAVAL (1 file renamed)

### Pending

All other projects still use old format (`##_filename.md`). Migrate as needed when active work begins on those projects.

---

## 📝 RATIONALE

**Benefits of prefix naming**:

1. **File Explorer**: Easy to scan and identify project at a glance
2. **Editor Tabs**: Tab labels show project code clearly
3. **Search Results**: Results show which project immediately
4. **Global Search**: Can search "V-SMASH" to find all related files
5. **Cross-Platform**: Works in Obsidian, VS Code, file managers, etc.
6. **Archive-Friendly**: Files retain identity even outside folder structure

**Why NOT suffix?**
- Harder to scan visually (code at end)
- Tab labels cut off important identifier
- Sorting puts all "01_" files together instead of grouping by project

**Why NOT folder-only?**
- Files lose context when opened in editor
- Search results don't show project
- Multiple tabs from different projects look identical

---

## 🎯 BEST PRACTICES

### DO:
- ✅ Always read this file before starting new project
- ✅ Use consistent project code across all files
- ✅ Update wiki-links when renaming
- ✅ Use descriptive filenames after the number
- ✅ Keep project codes SHORT (max 20 chars)

### DON'T:
- ❌ Change project code mid-project
- ❌ Use spaces in filenames (use underscores)
- ❌ Mix naming conventions within one project
- ❌ Forget to update wiki-links after rename
- ❌ Use generic codes like "PROJ1", "TEST"

---

*This standard ensures consistency across the Engineering Design System vault and enables efficient multi-project workflows.*
