# Meadows Leverage Points Analyzer v2.0

Enhanced version with references, scripts, templates, and optimized triggers.

## What's New in v2.0

### 1. **Reference Library** (4 detailed guides)
Moved comprehensive examples from SKILL.md into separate reference files:
- **L1-L3-high-leverage.md**: Paradigms, goals, mental models with defense/software examples
- **L4-L6-mid-high-leverage.md**: Self-organization, rules, information flow patterns
- **L7-L9-mid-leverage-loops.md**: Reinforcing loops, balancing loops, delays with calculations
- **L10-L12-low-leverage.md**: Physical structure, buffers, parameters (what NOT to do first)

**Benefit**: SKILL.md is now 200 lines (was 500+), Claude loads only relevant examples when needed.

### 2. **System Dynamics Scripts** (3 Python calculators)
Quantify feedback loops and delays:

**feedback_loop_calculator.py** (L7 - Reinforcing Loops):
```bash
python scripts/feedback_loop_calculator.py --initial 1000 --gain 0.05 --periods 20
# Calculates: doubling time, severity, growth trajectory
# Use for: Technical debt spirals, skill accumulation, bug growth
```

**balancing_loop_tuner.py** (L8 - Balancing Loops):
```bash
python scripts/balancing_loop_tuner.py --target 1000 --current 1200 --strength 0.5 --delay 2
# Calculates: convergence time, oscillation, overshoot
# Use for: Inventory control, quality gates, schedule recovery
```

**delay_impact_calculator.py** (L9 - Delays):
```bash
python scripts/delay_impact_calculator.py --current-delay 30 --proposed-delay 1 --incidents 10
# Calculates: ROI of delay reduction, payback period, cost impact
# Use for: Bug feedback loops, manufacturing quality, learning systems
```

All scripts have **interactive mode** (just run without args) and comprehensive `--help`.

**Benefit**: Quantified recommendations, not just qualitative. ROI justification for interventions.

### 3. **Analysis Templates** (2 structured guides)
Pre-formatted templates for systematic analysis:

**template-organizational-system.md**: For teams, companies, departments, policy systems
- Sections: Goals, stocks/flows, feedback loops, leverage points, intervention strategy
- Built-in checklists and risk assessment

**template-technical-system.md**: For products, manufacturing, software, infrastructure  
- Sections: Specs, dynamics, loop quantification, technical risks, verification plan
- References to scripts for L7-L9 calculations

**Benefit**: Consistent, thorough analyses. Don't miss critical leverage points.

### 4. **Improved Trigger Description**
Enhanced skill trigger to capture more usage patterns:
- Added: "we keep fixing but it gets worse", "why isn't this working?"
- Expanded: Technical debt spirals, coordination issues, policy resistance
- Broader: Works with ANY complex adaptive system

**Benefit**: Skill triggers more reliably on relevant queries.

---

## File Structure

```
meadows-leverage-analyzer-v2/
├── SKILL.md                    # Main skill (lean, 200 lines)
├── references/                 # Detailed examples (load as needed)
│   ├── L1-L3-high-leverage.md         # Paradigms, goals (5KB)
│   ├── L4-L6-mid-high-leverage.md     # Rules, info flow (4KB)
│   ├── L7-L9-mid-leverage-loops.md    # Feedback loops (5KB)
│   └── L10-L12-low-leverage.md        # Physical, buffers (4KB)
├── scripts/                    # System dynamics calculators
│   ├── feedback_loop_calculator.py    # L7 - reinforcing loops
│   ├── balancing_loop_tuner.py        # L8 - balancing loops
│   └── delay_impact_calculator.py     # L9 - delay impact/ROI
└── assets/                     # Analysis templates
    ├── template-organizational-system.md
    └── template-technical-system.md
```

**Total**: ~18KB references (loaded selectively), ~8KB scripts, ~6KB templates

---

## Usage Guide

### Basic Usage (Conversational)

Just describe your system problem to Claude:

```
"Our software team keeps firefighting bugs. We added more QA but it got worse. 
Management wants to hire more developers. What should we do?"
```

Claude will:
1. Map the system (stocks, flows, goals)
2. Identify leverage points L1-L12
3. Rank by effectiveness
4. Recommend top 3-5 interventions
5. Warn about unintended consequences

### Advanced Usage (With Scripts)

**Example: Technical debt spiral**

1. Ask Claude to analyze system
2. Claude identifies reinforcing loop (L7)
3. Run calculator to quantify:
```bash
cd /path/to/skill/scripts
python feedback_loop_calculator.py

# Interactive prompts:
Initial value: 1000        # hours of tech debt
Gain per period: 0.05      # 5% growth per week
Periods: 20                # 20 weeks
External input: 0

# Output: Debt doubles every 14 weeks, CRITICAL severity
```

4. Claude uses calculation to justify intervention

**Example: Quality control oscillation**

1. Claude identifies weak balancing loop (L8)
2. Run tuner to diagnose:
```bash
python balancing_loop_tuner.py

# Interactive prompts:
Target value: 1000         # target inventory
Current value: 1200        # 20% over
Correction strength: 0.5   # moderate
Delay: 2                   # 2-week delay

# Output: Oscillates before settling, reduce strength to 0.4
```

3. Claude recommends tuning corrections strength

### Template-Based Analysis

For systematic, documented analyses:

```bash
# Copy template to your working directory
cp assets/template-organizational-system.md my-analysis.md

# Fill in sections systematically
# Use scripts to quantify L7-L9
# Document decisions and track interventions
```

---

## Comparison: v1 vs v2

| Feature | v1 | v2 |
|---------|----|----|
| SKILL.md size | 500 lines | 200 lines |
| Examples | All in SKILL.md | 4 reference files |
| Quantification | Manual estimates | 3 Python scripts |
| Templates | None | 2 structured templates |
| Context efficiency | Loads everything | Progressive disclosure |
| Worked examples | 3 inline | 3 inline + refs |
| Script integration | N/A | L7-L9 calculations |
| Trigger patterns | Basic | Comprehensive |

---

## Quick Start Testing

### Test 1: Software firefighting (original from v1)
```
Analyze this system: Our developers are always firefighting bugs instead of 
building features. Management keeps adding more developers but problem gets worse.
```

**Expected**: L3 (goals), L2 (Brooks' Law paradigm), L5 (incentives), L7 (death spiral)

### Test 2: With script usage
```
Analyze this system: Technical debt started at 1000 hours 6 months ago, 
growing 8% per month. How fast is this compounding?
```

**Expected**: Claude runs `feedback_loop_calculator.py` to show doubling time ~9 months

### Test 3: Request template
```
I need to do a thorough analysis of our manufacturing quality system. 
Give me a structured template to work through.
```

**Expected**: Claude provides `template-technical-system.md` with guidance

---

## Integration with Your Workflow

### With DMIR Framework
The skill naturally fits DMIR cycle (see SKILL.md):
- **Define**: L3 (goals), identify constraints
- **Model**: L7-L9 (loops), quantify with scripts
- **Intervene**: Target L1-L6 (high leverage)
- **Reflect**: L1-L2 (challenge paradigms)

### With Project Knowledge
Skill references `/mnt/project/Systems_Thinking_and_Constraint_Theory.md` for theoretical depth when needed.

### With Other Skills
- **engineering-systems-mapper**: Creates visual maps, this skill analyzes leverage
- **dmir-defense-systems-mentor**: Enterprise-scale DMIR, this skill for specific interventions
- **engineering-concept-evaluation-assistant**: Evaluates designs, this skill evaluates system changes

---

## Installation

1. Copy entire `meadows-leverage-analyzer-v2/` folder to your Claude skills directory
2. Skill will automatically trigger on relevant queries
3. Scripts require Python 3.7+ (no external dependencies)

---

## Best Practices

### Do:
✅ Start with conversational analysis (let Claude guide)
✅ Use scripts when Claude identifies L7-L9 (quantify for ROI)
✅ Use templates for documented, repeatable analyses
✅ Read references when designing specific interventions
✅ Share script outputs with stakeholders (concrete data)

### Don't:
❌ Jump to scripts before understanding system structure
❌ Load all references at once (let Claude choose relevant ones)
❌ Skip warnings section (unintended consequences are real)
❌ Ignore feasibility (L2 paradigm shift may not be realistic)
❌ Stop at L12 (parameters) when higher leverage points exist

---

## Iteration Roadmap

**Next enhancements** (for v3):
- Visual system diagrams (stocks/flows/loops)
- Case study library (10+ worked examples by domain)
- Integration with system dynamics modeling tools
- ROI calculator for combined interventions
- Quick reference card (1-page cheat sheet)

**Feedback welcome**: Test the skill, share what works/what doesn't!

---

## Credits

Based on:
- Donella Meadows' *Thinking in Systems* and *Leverage Points* essay
- Your project knowledge: Systems Thinking, D-M-I-R, TOC integration
- Real usage patterns from v1 testing

Built following skill-creator best practices:
- Progressive disclosure (references loaded selectively)
- Token efficiency (lean SKILL.md)
- Executable scripts (deterministic calculations)
- Reusable templates (consistency)

---

## Quick Reference

**When to use this skill**:
- Problem keeps recurring despite "fixes"
- Unintended consequences from interventions  
- Need to find high-impact intervention points
- Want to quantify system dynamics
- Analyzing organizational, technical, or process systems

**Skill triggers automatically on**:
- "where should I intervene?"
- "analyze this system"
- "we keep fixing but it gets worse"
- "root cause"
- "leverage points"
- Technical debt, coordination, quality problems

**Progressive disclosure**:
1. SKILL.md always loaded (200 lines, core workflow)
2. References loaded as needed (by leverage point level)
3. Scripts executed when quantification needed
4. Templates copied when systematic analysis requested

---

**Ready to use!** Try it with one of the test cases above.
