# CC-Mastery — CLAUDE.md

## Purpose
Learning project to master Claude Code features (Modules 1-12).
Curriculum details: [[CC_mastery_curriculum.md]]
Session progress: [[progress.md]]

## Progress
- **DONE**: Modules 1-12 ✅ ALL COMPLETE
  (CLAUDE.md Mastery, Context Management, Slash Commands, Resume/Continue/History, Planning Mode, Hooks, Subagents, Skills, MCP, SDK, GitHub Action, settings.json Tuning)
- **NEXT**: Apply mastery to defense projects (Human_Skills_AI workspace)
- Slash commands created: /checkpoint, /catchup, /pr (global, in `~/.claude/commands/`)

## Workflow Rules
1. **Always /catchup first** when resuming — read `progress.md` before doing anything
2. **Checkpoint before /clear** — never clear context without dumping state first. Use `/checkpoint`
3. **One module per session** — stay focused, don't context-bloat by loading multiple modules
4. **Update this file after each module** — keep Progress current so /catchup works
5. **Practice what you learn** — each module has exercises. Do them, don't just read

## Context Budget
- Don't embed the full curriculum here. Read [[CC_mastery_curriculum.md]] on-demand
- Don't embed progress details here. Read [[progress.md]] on-demand
- This file should stay under 50 lines

## Mistakes Not To Repeat
<!-- After every correction, tell Claude:
     "Update CLAUDE.md so you don't make that mistake again."
     Ruthlessly edit this section. Mistake rates drop over time. -->
- Never use /compact for context management, prefer /clear + /catchup (Module 2 lesson)
- Never create more than 5 slash commands, prefer improving CLAUDE.md instead (Module 3 lesson)
