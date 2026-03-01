# Planning Reference

This document provides detailed guidance for the planning phase of GSD.

## Table of Contents

1. [Discovery Protocol](#discovery-protocol)
2. [Task Anatomy](#task-anatomy)
3. [Dependency Graphs](#dependency-graphs)
4. [PLAN.md Structure](#planmd-structure)
5. [Goal-Backward Methodology](#goal-backward-methodology)
6. [TDD Detection](#tdd-detection)

---

## Discovery Protocol

Discovery is MANDATORY unless you can prove current context exists.

### Level 0 — Skip
*Pure internal work, existing patterns only*
- ALL work follows established codebase patterns (grep confirms)
- No new external dependencies
- Pure internal refactoring or feature extension
- Examples: Add delete button, add field to model, create CRUD endpoint

### Level 1 — Quick Verification (2-5 min)
- Single known library, confirming syntax/version
- Low-risk decision (easily changed later)
- Action: Quick docs check, no RESEARCH.md needed

### Level 2 — Standard Research (15-30 min)
- Choosing between 2-3 options
- New external integration (API, service)
- Medium-risk decision
- Action: Route to research workflow, produces RESEARCH.md

### Level 3 — Deep Dive (1+ hour)
- Architectural decision with long-term impact
- Novel problem without clear patterns
- High-risk, hard to change later
- Action: Full research with RESEARCH.md

**Depth indicators:**
- Level 2+: New library not in package.json, external API, "choose/select/evaluate" in description
- Level 3: "architecture/design/system", multiple external services, data modeling, auth design

For niche domains (3D, games, audio, shaders, ML), suggest research before planning.

---

## Task Anatomy

Every task has four required fields:

### `<files>`
Exact file paths created or modified.
- ✅ Good: `src/app/api/auth/login/route.ts`, `prisma/schema.prisma`
- ❌ Bad: "the auth files", "relevant components"

### `<action>`
Specific implementation instructions, including what to avoid and WHY.
- ✅ Good: "Create POST endpoint accepting {email, password}, validates using bcrypt against User table, returns JWT in httpOnly cookie with 15-min expiry. Use jose library (not jsonwebtoken - CommonJS issues with Edge runtime)."
- ❌ Bad: "Add authentication", "Make login work"

### `<verify>`
How to prove the task is complete.
- ✅ Good: `npm test` passes, `curl -X POST /api/auth/login` returns 200 with Set-Cookie header
- ❌ Bad: "It works", "Looks good"

### `<done>`
Acceptance criteria — measurable state of completion.
- ✅ Good: "Valid credentials return 200 + JWT cookie, invalid credentials return 401"
- ❌ Bad: "Authentication is complete"

---

## Task Types

| Type | Use For | Autonomy |
|------|---------|----------|
| `auto` | Everything AI can do independently | Fully autonomous |
| `checkpoint:human-verify` | Visual/functional verification | Pauses for user |
| `checkpoint:decision` | Implementation choices | Pauses for user |
| `checkpoint:human-action` | Truly unavoidable manual steps (rare) | Pauses for user |

**Automation-first rule:** If AI CAN do it via CLI/API, AI MUST do it. Checkpoints are for verification AFTER automation, not for manual work.

---

## Task Sizing

### Context Budget Rules
- **Small task:** <10% context budget, 1-2 files, local scope
- **Medium task:** 10-20% budget, 3-5 files, single subsystem
- **Large task (SPLIT THIS):** >20% budget, many files, crosses boundaries

### Split Signals
Split into multiple plans when:
- >3 tasks in a plan
- >5 files per task
- Multiple subsystems touched
- Mixed concerns (API + UI + database in one plan)

### Estimating Context Per Task

| Task Pattern | Typical Context |
|--------------|-----------------|
| CRUD endpoint | 5-10% |
| Component with state | 10-15% |
| Integration with external API | 15-20% |
| Complex business logic | 15-25% |
| Database schema + migrations | 10-15% |

---

## Dependency Graphs

### Building Dependencies
1. Identify shared resources (files, types, APIs)
2. Determine creation order (types before implementations)
3. Group independent work into same wave
4. Sequential dependencies go to later waves

### Wave Assignment
- **Wave 1:** Foundation (types, schemas, utilities)
- **Wave 2:** Core implementations
- **Wave 3:** Integration and validation

### Vertical Slices vs Horizontal Layers
**Prefer vertical slices:** Each plan delivers a complete feature path.

```
✅ Vertical (preferred):
Plan 1: User registration (API + DB + validation)
Plan 2: User login (API + session + cookie)

❌ Horizontal (avoid):
Plan 1: All database models
Plan 2: All API endpoints
```

### File Ownership for Parallel Execution
Plans in the same wave MUST NOT modify the same files.

If two plans need the same file:
1. Move one to a later wave, OR
2. Split the file into separate modules

---

## PLAN.md Structure

```markdown
---
phase: {N}
plan: {M}
wave: {W}
depends_on: []
files_modified: []
autonomous: true
user_setup: []

must_haves:
  truths: []
  artifacts: []
---

# Plan {N}.{M}: {Descriptive Name}

<objective>
{What this plan accomplishes}

Purpose: {Why this matters}
Output: {What artifacts will be created}
</objective>

<context>
Load for context:
- .planning/PROJECT.md
- .planning/ARCHITECTURE.md (if exists)
- {relevant source files}
</context>

<tasks>

<task type="auto">
  <name>{Clear task name}</name>
  <files>{exact/file/paths.ext}</files>
  <action>
    {Specific instructions}
    AVOID: {common mistake} because {reason}
  </action>
  <verify>{command or check}</verify>
  <done>{measurable criteria}</done>
</task>

</tasks>

<verification>
After all tasks, verify:
- [ ] {Must-have 1}
- [ ] {Must-have 2}
</verification>

<success_criteria>
- [ ] All tasks verified
- [ ] Must-haves confirmed
</success_criteria>
```

### Frontmatter Fields

| Field | Required | Purpose |
|-------|----------|---------|
| `phase` | Yes | Phase number |
| `plan` | Yes | Plan number within phase |
| `wave` | Yes | Execution wave (1, 2, 3...) |
| `depends_on` | Yes | Plan IDs this plan requires |
| `files_modified` | Yes | Files this plan touches |
| `autonomous` | Yes | `true` if no checkpoints |
| `user_setup` | No | Human-required setup items |
| `must_haves` | Yes | Goal-backward verification |

### User Setup Section
When external services involved:

```yaml
user_setup:
  - service: stripe
    why: "Payment processing"
    env_vars:
      - name: STRIPE_SECRET_KEY
        source: "Stripe Dashboard -> Developers -> API keys"
    dashboard_config:
      - task: "Create webhook endpoint"
        location: "Stripe Dashboard -> Developers -> Webhooks"
```

Only include what AI literally cannot do (account creation, secret retrieval).

---

## Goal-Backward Methodology

**Forward planning asks:** "What should we build?"
**Goal-backward planning asks:** "What must be TRUE for the goal to be achieved?"

Forward planning produces tasks. Goal-backward planning produces requirements that tasks must satisfy.

### Process
1. **Define done state:** What is true when the phase is complete?
2. **Identify must-haves:** Non-negotiable requirements
3. **Decompose to tasks:** What steps achieve each must-have?
4. **Order by dependency:** What must exist before something else?
5. **Group into plans:** 2-3 related tasks per plan

### Must-Haves Structure
```yaml
must_haves:
  truths:
    - "User can log in with valid credentials"
    - "Invalid credentials are rejected with 401"
  artifacts:
    - "src/app/api/auth/login/route.ts exists"
    - "JWT cookie is httpOnly"
  key_links:
    - "Login endpoint validates against User table"
```

---

## TDD Detection

### When to Use TDD Plans

Detect TDD fit when:
- Complex business logic with edge cases
- Financial calculations
- State machines
- Data transformation pipelines
- Input validation rules

### TDD Heuristic

> Can you write `expect(fn(input)).toBe(output)` before writing `fn`?

Yes → TDD plan (one feature per plan)
No → Standard plan

### TDD Plan Structure

```markdown
---
phase: {N}
plan: {M}
type: tdd
wave: {W}
---

# TDD Plan: {Feature}

## Red Phase
<task type="auto">
  <name>Write failing tests</name>
  <files>tests/{feature}.test.ts</files>
  <action>Write tests for: {behavior}</action>
  <verify>npm test shows RED (failing)</verify>
  <done>Tests exist and fail for expected reasons</done>
</task>

## Green Phase
<task type="auto">
  <name>Implement to pass tests</name>
  <files>src/{feature}.ts</files>
  <action>Minimal implementation to pass tests</action>
  <verify>npm test shows GREEN (passing)</verify>
  <done>All tests pass</done>
</task>

## Refactor Phase
<task type="auto">
  <name>Clean up implementation</name>
  <files>src/{feature}.ts</files>
  <action>Improve code quality without changing behavior</action>
  <verify>npm test still GREEN</verify>
  <done>Code is clean, tests still pass</done>
</task>
```

### TDD Commits
- RED: `test({phase}-{plan}): add failing test for [feature]`
- GREEN: `feat({phase}-{plan}): implement [feature]`
- REFACTOR: `refactor({phase}-{plan}): clean up [feature]`
