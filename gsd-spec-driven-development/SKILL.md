---
name: gsd-spec-driven-development
description: Spec-driven development methodology for AI-assisted coding. Use when users want to build software projects systematically with planning, execution, and verification phases. Implements the Get-Shit-Done (GSD) framework for context engineering, atomic task execution, and quality-preserving workflows.
license: MIT
---

# GSD Spec-Driven Development

A lightweight, powerful meta-prompting and context engineering system for building software with AI assistance. This skill implements the Get-Shit-Done (GSD) methodology.

## Core Philosophy

GSD is designed for **solo developer + AI workflow**:
- No enterprise patterns (no sprint ceremonies, story points, RACI matrices)
- Plans ARE prompts (PLAN.md files are executable, not documents to transform)
- Context engineering (manage context window deliberately to prevent quality degradation)
- Aggressive atomicity (2-3 tasks per plan, fresh context per execution)

## When to Use This Skill

Use GSD when:
- Starting a new software project that needs structured planning
- Building features that span multiple files/systems
- Working on complex implementations that benefit from research first
- Wanting consistent, high-quality AI-assisted development

## Workflow Overview

```
/gsd:new-project → Deep questioning → SPEC.md (finalized)
/gsd:discuss-phase N → Clarify scope → CONTEXT.md
/gsd:plan-phase N → Research → PLAN.md files with XML tasks
/gsd:execute-phase N → Wave execution → Atomic commits
/gsd:verify-work N → Must-haves check → Evidence captured
/gsd:complete-milestone → Archive → Next milestone
```

## Quick Start

### 1. Initialize Project

Run `/gsd:new-project` to start. The system will:
1. Ask questions until it understands your idea completely
2. Research the domain (optional but recommended)
3. Extract v1/v2/out-of-scope requirements
4. Create phases mapped to requirements

**Creates:** `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`

### 2. Plan Phase

Run `/gsd:plan-phase 1` to plan the first phase. The system will:
1. Research how to implement this phase
2. Create 2-3 atomic task plans with XML structure
3. Verify plans against requirements

**Creates:** `{phase}-RESEARCH.md`, `{phase}-{N}-PLAN.md`

### 3. Execute Phase

Run `/gsd:execute-phase 1` to execute. The system will:
1. Run plans in waves (parallel where possible)
2. Use fresh context per plan
3. Create atomic commits per task
4. Verify against goals

**Creates:** `{phase}-{N}-SUMMARY.md`, `{phase}-VERIFICATION.md`

### 4. Repeat

Loop **discuss → plan → execute → verify** until milestone complete.

## File Structure

```
.planning/
├── PROJECT.md          # Project vision, always loaded
├── REQUIREMENTS.md     # Scoped v1/v2 requirements
├── ROADMAP.md          # Phases and progress
├── STATE.md            # Decisions, blockers, session memory
├── config.json         # Settings (mode, depth, profiles)
├── research/           # Domain research outputs
├── phases/             # Phase-specific artifacts
│   └── {N}/
│       ├── {N}-CONTEXT.md
│       ├── {N}-RESEARCH.md
│       ├── {N}-{M}-PLAN.md
│       └── {N}-{M}-SUMMARY.md
├── quick/              # Ad-hoc task artifacts
└── todos/              # Captured ideas for later
```

## Commands Reference

### Core Workflow
| Command | Purpose |
|---------|---------|
| `/gsd:new-project` | Initialize: questions → research → requirements → roadmap |
| `/gsd:discuss-phase [N]` | Capture implementation decisions before planning |
| `/gsd:plan-phase [N]` | Research + plan + verify for a phase |
| `/gsd:execute-phase <N>` | Execute all plans in parallel waves |
| `/gsd:verify-work [N]` | Manual user acceptance testing |
| `/gsd:complete-milestone` | Archive milestone, tag release |
| `/gsd:new-milestone` | Start next version |

### Navigation
| Command | Purpose |
|---------|---------|
| `/gsd:progress` | Show current position |
| `/gsd:help` | Show all commands |

### Phase Management
| Command | Purpose |
|---------|---------|
| `/gsd:add-phase` | Append phase to roadmap |
| `/gsd:insert-phase [N]` | Insert urgent work between phases |
| `/gsd:remove-phase [N]` | Remove future phase |

### Utilities
| Command | Purpose |
|---------|---------|
| `/gsd:quick` | Execute ad-hoc task with GSD guarantees |
| `/gsd:debug [desc]` | Systematic debugging |
| `/gsd:add-todo [desc]` | Capture idea for later |
| `/gsd:pause-work` | Create handoff when stopping |
| `/gsd:resume-work` | Restore from last session |

## Detailed References

For detailed implementation guidance, read these reference files:

- **Planning**: See [references/planning.md](references/planning.md) for task breakdown, dependency graphs, and PLAN.md structure
- **Execution**: See [references/execution.md](references/execution.md) for deviation rules, checkpoint protocols, and commit conventions
- **Templates**: See [templates/](templates/) for PROJECT.md, PLAN.md, and other document templates

## Context Engineering Rules

### Quality Degradation Curve

| Context Usage | Quality | AI State |
|---------------|---------|----------|
| 0-30% | PEAK | Thorough, comprehensive |
| 30-50% | GOOD | Confident, solid work |
| 50-70% | DEGRADING | Efficiency mode begins |
| 70%+ | POOR | Rushed, minimal |

**Rule:** Stop BEFORE quality degrades. Plans should complete within ~50% context.

### Task Sizing

- **Small task:** <10% context, 1-2 files
- **Medium task:** 10-20% context, 3-5 files
- **Large task (SPLIT THIS):** >20% context, many files

### Split Signals

Split into multiple plans when:
- More than 3 tasks in a plan
- More than 5 files per task
- Multiple subsystems touched
- Mixed concerns (API + UI + database in one plan)

## XML Task Format

Every task uses this structure:

```xml
<task type="auto">
  <name>Task N: Action-oriented name</name>
  <files>src/path/file.ts, src/other/file.ts</files>
  <action>
    What to do, what to avoid and WHY.
    Use jose library (not jsonwebtoken - CommonJS issues).
  </action>
  <verify>Command or check to prove completion</verify>
  <done>Measurable acceptance criteria</done>
</task>
```

### Task Types

| Type | Use For |
|------|---------|
| `auto` | Everything AI can do independently |
| `checkpoint:human-verify` | Visual/functional verification |
| `checkpoint:decision` | Implementation choices |
| `checkpoint:human-action` | Truly unavoidable manual steps (rare) |

## Commit Conventions

Format: `{type}({phase}-{plan}): {description}`

| Type | Use |
|------|-----|
| `feat` | New feature |
| `fix` | Bug fix |
| `test` | Tests only |
| `refactor` | Code cleanup |
| `docs` | Documentation |
| `chore` | Config/dependencies |

One commit per task. Atomic, traceable, revertable.

## Anti-Patterns to Avoid

- **Enterprise patterns:** Story points, sprint ceremonies, RACI matrices
- **Vague tasks:** "Add authentication" instead of specific implementation
- **Large plans:** More than 3 tasks per plan
- **Temporal language:** "We changed X to Y" (describe current state only)
- **Human time estimates:** Hours/days/weeks (use AI execution time)
