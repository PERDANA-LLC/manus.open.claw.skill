# Workflows Reference

This document provides detailed guidance for each GSD workflow command.

## Table of Contents

1. [/gsd:new-project](#gsdnew-project)
2. [/gsd:discuss-phase](#gsddiscuss-phase)
3. [/gsd:plan-phase](#gsdplan-phase)
4. [/gsd:execute-phase](#gsdexecute-phase)
5. [/gsd:verify-work](#gsdverify-work)
6. [/gsd:quick](#gsdquick)
7. [/gsd:debug](#gsddebug)

---

## /gsd:new-project

Initialize a new project through unified flow: questioning → research → requirements → roadmap.

### Process

1. **Setup**
   - Abort if project exists (check for `.planning/PROJECT.md`)
   - Initialize git repo if not exists
   - Detect existing code (brownfield detection)

2. **Brownfield Offer** (if existing code detected)
   - Offer to run `/gsd:map-codebase` first
   - Or skip and proceed with initialization

3. **Deep Questioning**
   - Ask: "What do you want to build?"
   - Follow the thread with intelligent follow-ups
   - Challenge vagueness, make abstract concrete
   - Surface assumptions, find edges
   
   **Context checklist:**
   - [ ] Vision — What does success look like?
   - [ ] Users — Who is this for?
   - [ ] Problem — What pain does it solve?
   - [ ] Scope — What's in, what's out?
   - [ ] Constraints — Technical, timeline, budget?
   - [ ] Prior art — What exists already?

4. **Write PROJECT.md**
   - Use template from `templates/project/PROJECT.md`
   - Status: FINALIZED

5. **Research Decision** (optional)
   - If unfamiliar technology or architectural decisions
   - Create `.planning/RESEARCH.md` with findings

6. **Define Requirements**
   - Generate from PROJECT.md
   - Use template from `templates/project/REQUIREMENTS.md`

7. **Create Roadmap**
   - 3-5 phases per milestone
   - Use template from `templates/project/ROADMAP.md`

8. **Initialize Remaining Files**
   - STATE.md, DECISIONS.md, JOURNAL.md, TODO.md
   - Create directories: phases/, templates/

9. **Initial Commit**
   ```bash
   git add .planning/
   git commit -m "chore: initialize GSD project"
   ```

### Output
- `.planning/PROJECT.md`
- `.planning/REQUIREMENTS.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`

---

## /gsd:discuss-phase

Capture implementation decisions before planning.

### When to Use
- Before `/gsd:plan-phase` for complex phases
- When phase description is vague
- When user has specific preferences

### Process

1. **Load Phase Context**
   - Read ROADMAP.md for phase description
   - Read PROJECT.md for overall context

2. **Identify Gray Areas**
   Based on what's being built:
   - **Visual features** → Layout, density, interactions, empty states
   - **APIs/CLIs** → Response format, flags, error handling, verbosity
   - **Content systems** → Structure, tone, depth, flow
   - **Organization tasks** → Grouping criteria, naming, duplicates

3. **Ask Targeted Questions**
   - For each gray area the user selects
   - Ask until satisfied

4. **Write CONTEXT.md**
   - Use template from `templates/phase/CONTEXT.md`
   - Save to `.planning/phases/{N}/{N}-CONTEXT.md`

### Output
- `.planning/phases/{N}/{N}-CONTEXT.md`

---

## /gsd:plan-phase

Research + plan + verify for a phase.

### Process

1. **Load Context**
   - PROJECT.md
   - ROADMAP.md (phase description)
   - CONTEXT.md (if exists from discuss-phase)
   - ARCHITECTURE.md (if exists)

2. **Research** (unless skipped)
   - Investigate how to implement this phase
   - Guided by CONTEXT.md decisions
   - Create RESEARCH.md

3. **Plan**
   - Decompose into 2-3 atomic task plans
   - Use template from `templates/phase/PLAN.md`
   - Build dependency graph
   - Assign execution waves

4. **Verify Plans**
   - Check plans against requirements
   - Loop until they pass verification

### Output
- `.planning/phases/{N}/{N}-RESEARCH.md`
- `.planning/phases/{N}/{N}-{M}-PLAN.md` (multiple)

---

## /gsd:execute-phase

Execute all plans in parallel waves, verify when complete.

### Process

1. **Load Plans**
   - Read all PLAN.md files for phase
   - Build execution order from waves and dependencies

2. **Execute in Waves**
   - Wave 1: All plans with `wave: 1`
   - Wait for completion
   - Wave 2: All plans with `wave: 2`
   - Continue until all waves complete

3. **Per-Plan Execution**
   - Fresh context per plan
   - Execute tasks sequentially
   - Apply deviation rules as needed
   - Atomic commit per task
   - Create SUMMARY.md

4. **Phase Verification**
   - Check all must-haves from all plans
   - Create VERIFICATION.md

### Output
- `.planning/phases/{N}/{N}-{M}-SUMMARY.md` (per plan)
- `.planning/phases/{N}/{N}-VERIFICATION.md`
- Git commits (one per task)

---

## /gsd:verify-work

Manual user acceptance testing.

### Process

1. **Extract Testable Deliverables**
   - From phase plans and summaries
   - What user should be able to do now

2. **Walk Through One at a Time**
   - "Can you log in with email?" Yes/no
   - If no, describe what's wrong

3. **Diagnose Failures**
   - Spawn debug agents to find root causes
   - Create verified fix plans

4. **Create UAT.md**
   - Document what passed/failed
   - Link to fix plans if issues found

### Output
- `.planning/phases/{N}/{N}-UAT.md`
- Fix plans if issues found

---

## /gsd:quick

Execute ad-hoc task with GSD guarantees.

### When to Use
- Bug fixes
- Small features
- Config changes
- One-off tasks
- Tasks that don't warrant full phase planning

### Process

1. **Validate Project Active**
   - Check ROADMAP.md exists

2. **Get Task Description**
   - Ask: "What do you want to do?"

3. **Create Quick Plan**
   - Simplified planning (no research, no verification)
   - Save to `.planning/quick/{NNN}-{slug}/PLAN.md`

4. **Execute**
   - Same execution rules as phase plans
   - Atomic commits

5. **Update STATE.md**
   - Add to Quick Tasks Completed table

6. **Commit Artifacts**
   ```bash
   git commit -m "docs(quick-{NNN}): {description}"
   ```

### Output
- `.planning/quick/{NNN}-{slug}/PLAN.md`
- `.planning/quick/{NNN}-{slug}/SUMMARY.md`
- Updated STATE.md

---

## /gsd:debug

Systematic debugging with persistent state.

### Process

1. **Describe Problem**
   - What's happening?
   - What should happen?
   - When does it occur?

2. **Gather Evidence**
   - Error messages
   - Logs
   - Reproduction steps

3. **Form Hypotheses**
   - Rank by likelihood
   - Test systematically

4. **Three-Strike Rule**
   - If 3 attempts fail
   - State dump
   - Fresh session with context

5. **Document Fix**
   - What was the root cause?
   - What was the fix?
   - How to prevent recurrence?

### Output
- Debug notes in STATE.md
- Fix commits if successful
