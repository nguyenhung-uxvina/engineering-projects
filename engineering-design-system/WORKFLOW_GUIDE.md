# ENGINEERING DESIGN SYSTEM WORKFLOW GUIDE
## Step-by-Step Process with User Approval Gates

**Version:** 2.0 (User-Approval-Gated)
**Date:** 2026-02-03

---

## 🎯 WORKFLOW PHILOSOPHY

**Key Principle:** **Never proceed to the next phase without explicit user approval.**

Each phase ends with a **GATE REVIEW** where:
1. Claude presents deliverables and findings
2. User reviews the work
3. User decides: **APPROVE** (proceed) or **REVISE** (iterate)
4. Only after approval does Claude move to the next phase

---

## 📋 COMPLETE WORKFLOW (5 Phases + 5 Gates)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ENGINEERING DESIGN WORKFLOW                          │
│                     (User-Approval-Gated)                               │
└─────────────────────────────────────────────────────────────────────────┘

PHASE 0: ODI ANALYSIS
├─ Duration: ~30-45 minutes
├─ Deliverables: Job map, outcome statements, opportunity scores
└─ Output: ODI analysis document

         ⬇️
    ┌─────────────────┐
    │   GATE 0        │ ← USER APPROVAL REQUIRED
    │   Review ODI    │    - Are the outcomes correct?
    │   Results       │    - Do segments make sense?
    └─────────────────┘    - Should we proceed?
         ⬇️ (if APPROVED)

PHASE 1: TASK CLARIFICATION
├─ Duration: ~45-60 minutes
├─ Deliverables: Requirements list, systems analysis, integration summary
└─ Output: 3 documents (requirements, systems, integration)

         ⬇️
    ┌─────────────────┐
    │   GATE 1        │ ← USER APPROVAL REQUIRED
    │   Review Req's  │    - Are requirements complete?
    │   & Systems     │    - Quantification ≥80%?
    └─────────────────┘    - Ready for concepts?
         ⬇️ (if APPROVED)

PHASE 2: CONCEPTUAL DESIGN
├─ Duration: ~45-60 minutes
├─ Deliverables: Function structure, morphological matrix, concepts, VDI 2225
└─ Output: Conceptual design document with selected concept

         ⬇️
    ┌─────────────────┐
    │   GATE 2        │ ← USER APPROVAL REQUIRED
    │   Concept       │    - Do you agree with selected concept?
    │   Selection     │    - VDI 2225 score ≥70%?
    └─────────────────┘    - Cost acceptable?
         ⬇️ (if APPROVED)

PHASE 3: EMBODIMENT DESIGN
├─ Duration: ~30-45 minutes
├─ Deliverables: Layout, DfX analysis, materials, thermal analysis
└─ Output: Embodiment design document

         ⬇️
    ┌─────────────────┐
    │   GATE 3        │ ← USER APPROVAL REQUIRED
    │   Embodiment    │    - Is the layout feasible?
    │   Review        │    - DfX priorities correct?
    └─────────────────┘    - Materials acceptable?
         ⬇️ (if APPROVED)

PHASE 4: DETAIL DESIGN
├─ Duration: ~30-45 minutes
├─ Deliverables: BOM, assembly instructions, verification plan
└─ Output: Detail design document

         ⬇️
    ┌─────────────────┐
    │   GATE 4        │ ← USER APPROVAL REQUIRED
    │   Production    │    - Is BOM complete?
    │   Readiness     │    - Cost target met?
    └─────────────────┘    - Ready for production?
         ⬇️ (if APPROVED)

✅ PROJECT COMPLETE - PRODUCTION READY
```

---

## 🚪 GATE REVIEW PROCESS

### At Each Gate, Claude Will:

1. **Summarize Phase Deliverables**
   - What was created
   - Key findings and decisions
   - Metrics achieved vs. targets

2. **Present Gate Checklist**
   - All gate criteria with ✅/❌ status
   - Any issues or concerns
   - Recommendations

3. **Ask for User Decision:**
   ```
   📋 GATE [N] REVIEW - USER DECISION REQUIRED

   ✅ All deliverables complete
   ✅ Gate criteria met

   Please review the [phase name] deliverables above.

   Choose one:
   A) ✅ APPROVE - Proceed to Phase [N+1]
   B) 🔄 REVISE - Iterate on current phase
   C) ⏸️ PAUSE - Stop here, resume later
   D) ❌ CANCEL - Abandon this project

   Your decision: [waiting for user input]
   ```

4. **Wait for User Input** (CRITICAL: Do NOT proceed without approval)

5. **Act Based on Decision:**
   - **APPROVE:** Move to next phase
   - **REVISE:** Ask what needs to change, iterate
   - **PAUSE:** Save state, provide resume instructions
   - **CANCEL:** Archive project, document learnings

---

## 📝 PHASE-BY-PHASE GUIDE

### PHASE 0: ODI ANALYSIS

**What Claude Does:**
1. Read existing project documentation (if option 2)
2. Define job executor and job-to-be-done
3. Create 8-step universal job map
4. Capture outcome statements (D-M-O format)
5. Calculate opportunity scores
6. Identify customer segments
7. Competitive benchmarking

**What User Reviews:**
- Are the job executors correct?
- Do the outcome statements reflect real customer pain?
- Are opportunity scores reasonable?
- Do customer segments make sense?

**Gate 0 Criteria:**
- [ ] Job executor identified
- [ ] Job-to-be-done defined (functional)
- [ ] Universal job map created (8 steps)
- [ ] ≥10 outcome statements captured
- [ ] Opportunity scores calculated
- [ ] ≥1 EXTREME opportunity (>15) identified
- [ ] Customer segments defined
- [ ] Competitive satisfaction benchmarks

**User Decision Point:** "Should we proceed to Phase 1 (Requirements)?"

---

### PHASE 1: TASK CLARIFICATION

**What Claude Does:**
1. **Requirements List:**
   - Map ODI outcomes to 16 P&B categories
   - Create 100+ requirements (target: ≥80% quantified)
   - Trace top outcomes to requirements
   - Map standards (MIL-STD, IEC, etc.)

2. **Systems Thinking:**
   - Create 2-4 Causal Loop Diagrams
   - Identify Meadows leverage points (L1-L12)
   - Generate systems-informed requirements
   - Cross-impact analysis

3. **Integration Summary:**
   - Show how ODI + Systems + P&B work together
   - Traceability matrix

**What User Reviews:**
- Are requirements complete (no missing critical ones)?
- Are quantification targets realistic?
- Do systems CLDs make sense?
- Are leverage points correctly identified?

**Gate 1 Criteria:**
- [ ] Requirements list complete (all 16 categories)
- [ ] Requirements quantified ≥80%
- [ ] Top 10 ODI outcomes mapped to requirements
- [ ] ≥2 Causal Loop Diagrams created
- [ ] ≥3 Leverage points identified
- [ ] Standards compliance planned
- [ ] No critical requirement conflicts

**User Decision Point:** "Should we proceed to Phase 2 (Conceptual Design)?"

---

### PHASE 2: CONCEPTUAL DESIGN

**What Claude Does:**
1. 5-step abstraction process (essential problem)
2. Function structure diagram (black box → detailed)
3. Morphological matrix (≥3 working principles per function)
4. Generate 3-5 concept variants
5. VDI 2225 evaluation (weighted by ODI scores)
6. Select concept (≥70% threshold)
7. Document selection rationale

**What User Reviews:**
- Do the concept variants make sense?
- Is the VDI 2225 scoring fair?
- Do you agree with the selected concept?
- Is the cost estimate acceptable?

**Gate 2 Criteria:**
- [ ] Abstraction process complete (5 steps)
- [ ] Function structure diagram created
- [ ] Morphological matrix (≥3 solutions per function)
- [ ] 3-5 concept variants generated
- [ ] VDI 2225 evaluation complete
- [ ] Selected concept scores ≥70%
- [ ] Selection rationale documented
- [ ] Cost estimate within target

**User Decision Point:** "Should we proceed to Phase 3 (Embodiment Design) with Concept [X]?"

---

### PHASE 3: EMBODIMENT DESIGN

**What Claude Does:**
1. Preliminary layout (form factor, modules)
2. DfX priority matrix (identify top 5 categories)
3. Apply DfX guidelines to design
4. Material selection (with justification)
5. Definitive layout (with dimensions)
6. Thermal/structural analysis (if applicable)
7. Modular architecture definition

**What User Reviews:**
- Is the layout feasible?
- Are DfX priorities correct for this product?
- Are material selections appropriate?
- Does the design meet all embodiment-determining requirements?

**Gate 3 Criteria:**
- [ ] Definitive layout with dimensions
- [ ] Materials selected and justified
- [ ] DfX review completed (≥5 categories)
- [ ] Mass budget verified (within target)
- [ ] Thermal/structural analysis complete
- [ ] Standards compliance planned
- [ ] Modular architecture defined
- [ ] Production feasibility confirmed

**User Decision Point:** "Should we proceed to Phase 4 (Detail Design)?"

---

### PHASE 4: DETAIL DESIGN

**What Claude Does:**
1. Complete Bill of Materials (BOM) with costs
2. Assembly instructions (step-by-step)
3. Verification plan (test procedures)
4. Standards compliance matrix
5. Manufacturing drawings list
6. Quality control procedures
7. Production readiness assessment

**What User Reviews:**
- Is the BOM complete?
- Is the cost estimate accurate?
- Are assembly instructions clear?
- Is the verification plan comprehensive?
- Are we ready for production pilot?

**Gate 4 Criteria:**
- [ ] Complete BOM (all line items)
- [ ] Cost estimate (manufacturing + selling price)
- [ ] Assembly instructions
- [ ] Verification plan (≥10 tests)
- [ ] Standards compliance matrix
- [ ] Production documentation list
- [ ] Tooling requirements identified
- [ ] Quality control procedures defined

**User Decision Point:** "Should we proceed to Pilot Production?"

---

## 🔄 ITERATION PROTOCOL

### If User Chooses "REVISE" at Any Gate:

**Claude Will Ask:**
```
🔄 REVISION REQUEST - What needs to change?

Please specify:
1. What is incorrect or incomplete?
2. What should be changed?
3. Any additional requirements or constraints?
4. Should I revise the entire phase or specific sections?

Your feedback: [waiting for user input]
```

**Then Claude Will:**
1. Make the requested changes
2. Update affected documents
3. Re-present the gate review
4. Ask for approval again

**Iteration Limit:** None - iterate until user is satisfied

---

## ⏸️ PAUSE & RESUME

### If User Chooses "PAUSE":

**Claude Will Provide:**
```
⏸️ PROJECT PAUSED AT GATE [N]

Project: [CODE] [NAME]
Current Phase: [PHASE NAME]
Status: [X]% complete overall

Resume Instructions:
1. Say: "Tiếp tục [CODE]" or "Resume [CODE]"
2. Claude will load project context
3. Continue from Gate [N] review

All work saved in:
vault/projects/[CODE]/

Last updated: [TIMESTAMP]
```

---

## 🎯 BEST PRACTICES

### For Users:

1. **Review Thoroughly at Each Gate**
   - Don't rush approvals
   - Check if outcomes/requirements match your understanding
   - Verify cost estimates are realistic
   - Ensure technical feasibility

2. **Provide Clear Feedback**
   - If revising, be specific about what needs to change
   - Explain the rationale for changes
   - Provide additional context if needed

3. **Use Pause When Needed**
   - Need to consult stakeholders? Pause.
   - Need more information? Pause.
   - Not sure about a decision? Pause.

4. **Ask Questions**
   - If anything is unclear, ask before approving
   - Request clarification on technical terms
   - Challenge assumptions if they seem wrong

### For Claude:

1. **Never Auto-Proceed**
   - Always wait for explicit user approval
   - Don't assume "silence = approval"
   - Ask again if user input is ambiguous

2. **Present Clear Gate Reviews**
   - Summarize deliverables concisely
   - Highlight key decisions made
   - Show metrics (target vs. achieved)
   - Make approval question explicit

3. **Be Ready to Iterate**
   - Accept revision requests gracefully
   - Ask clarifying questions if feedback is vague
   - Don't defend decisions - adapt to user needs

4. **Document All Decisions**
   - Record what was approved at each gate
   - Note any deviations from standard process
   - Track rationale for key decisions

---

## 📊 EXAMPLE GATE REVIEW (Gate 1)

```
═══════════════════════════════════════════════════════════════════════════
  📋 GATE 1 REVIEW - PHASE 1 COMPLETE
═══════════════════════════════════════════════════════════════════════════

PROJECT: VN-CAM-T1 "HUẤN LUYỆN VIÊN" (AI Training Coach)
PHASE 1 STATUS: ✅ Complete

─────────────────────────────────────────────────────────────────────────
DELIVERABLES:
─────────────────────────────────────────────────────────────────────────

✅ Requirements List: 143 requirements created
   - Demands: 130 (91%)
   - Wishes: 13 (9%)
   - Quantified: 138/143 (96.5%) ← Exceeds 80% target ✅

✅ Systems Thinking Analysis:
   - 4 Causal Loop Diagrams created
   - 6 Leverage points identified (L3, L4, L6, L9, L10, L11)
   - 5 systems-informed requirements added

✅ Integration Summary:
   - ODI outcomes → Systems leverage → Requirements
   - Traceability: 10 requirements trace to top 5 ODI outcomes

─────────────────────────────────────────────────────────────────────────
KEY FINDINGS:
─────────────────────────────────────────────────────────────────────────

🎯 Top Requirement (from T1-01, Opp: 16.0):
   R1001: AI processing latency ≤100ms

🎯 Critical Leverage Point:
   L6 (Information Flows): Real-time feedback accelerates skill loop

🎯 Cost Target:
   ≤$3,200 selling price (requirement R15006)

─────────────────────────────────────────────────────────────────────────
GATE 1 CHECKLIST:
─────────────────────────────────────────────────────────────────────────

✅ Requirements list complete (15 categories)
✅ Requirements quantified ≥80% (96.5% achieved)
✅ Top 10 ODI outcomes mapped to requirements
✅ ≥2 CLDs created (4 created)
✅ ≥3 Leverage points identified (6 identified)
✅ Standards compliance planned (MIL-STD-810H, IEC, etc.)
✅ No critical requirement conflicts

GATE 1 STATUS: ✅ PASS (7/7 criteria met)

─────────────────────────────────────────────────────────────────────────
RISKS IDENTIFIED:
─────────────────────────────────────────────────────────────────────────

⚠️ MEDIUM: AI latency requirement (≤100ms) is aggressive
   Mitigation: Jetson Orin Nano (40 TOPS) + TensorRT optimization

⚠️ LOW: Vietnamese shooter training dataset doesn't exist yet
   Mitigation: Need to collect ≥1000 samples (Phase 4+)

─────────────────────────────────────────────────────────────────────────
FILES CREATED:
─────────────────────────────────────────────────────────────────────────

📄 VN-CAM-T1_01_requirements_list.md (143 requirements)
📄 VN-CAM-T1_systems_analysis.md (4 CLDs, 6 leverage points)
📄 VN-CAM-T1_phase1_integration_summary.md

─────────────────────────────────────────────────────────────────────────
USER DECISION REQUIRED:
─────────────────────────────────────────────────────────────────────────

Please review the Phase 1 deliverables above.

Choose one:

A) ✅ APPROVE - Proceed to Phase 2 (Conceptual Design)
   → Claude will create function structure, morphological matrix,
      concept variants, and run VDI 2225 evaluation

B) 🔄 REVISE - Make changes to Phase 1
   → Specify what needs to change (requirements, systems analysis, etc.)

C) ⏸️ PAUSE - Stop here, resume later
   → Project saved, resume with "Tiếp tục VN-CAM-T1"

D) ❌ CANCEL - Abandon this project
   → Project archived with learnings documented

Your decision: [Waiting for your response...]
═══════════════════════════════════════════════════════════════════════════
```

---

## 📚 QUICK REFERENCE

### User Commands:

| Command | Action |
|---------|--------|
| **"A" or "APPROVE"** | Proceed to next phase |
| **"B" or "REVISE"** | Iterate on current phase |
| **"C" or "PAUSE"** | Save and stop |
| **"D" or "CANCEL"** | Abandon project |
| **"Tiếp tục [CODE]"** | Resume paused project |
| **"Status [CODE]"** | Check current phase and progress |

### Gate Summary:

| Gate | After Phase | Key Question |
|------|-------------|--------------|
| **Gate 0** | ODI Analysis | Are these the right customer outcomes? |
| **Gate 1** | Task Clarification | Are requirements complete and quantified? |
| **Gate 2** | Conceptual Design | Do we agree on the selected concept? |
| **Gate 3** | Embodiment Design | Is the layout feasible and DfX correct? |
| **Gate 4** | Detail Design | Are we ready for production pilot? |

---

**Last Updated:** 2026-02-03
**Version:** 2.0 (User-Approval-Gated Workflow)
**Status:** ✅ Active Process

**Note:** This workflow ensures user is in control at every major decision point, preventing wasted work from wrong assumptions or incorrect directions.
