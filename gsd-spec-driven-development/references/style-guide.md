# GSD Style Guide

This document explains how GSD documents are written for consistency across all artifacts.

## Core Philosophy

GSD is a **meta-prompting system** where every file is both implementation and specification. Files teach AI how to build software systematically. The system optimizes for:

| Principle | Description |
|-----------|-------------|
| Solo developer + AI workflow | No enterprise patterns, no team coordination |
| Context engineering | Manage context window deliberately |
| Plans as prompts | PLAN.md files are executable, not documents to transform |

---

## File Structure Conventions

### Slash Commands

Commands use YAML frontmatter followed by structured sections:

```yaml
---
name: gsd:command-name
description: One-line description
argument-hint: "<required>" or "[optional]"
---
```

Section order: `<objective>` → `<context>` → `<process>` → `<success_criteria>`

Commands are thin wrappers that delegate detailed logic to workflows.

### Workflows

No YAML frontmatter. Structure varies by workflow. Common tags include `<purpose>`, `<when_to_use>`, `<required_reading>`, `<process>`, and `<step>`.

### Templates

Most start with `# [Name] Template` header. Placeholder conventions use square brackets for user-filled content (`[Project Name]`) and curly braces for computed values (`{phase}-{plan}-PLAN.md`).

---

## XML Tag Conventions

### Semantic Containers Only

XML tags serve semantic purposes. Use Markdown headers for hierarchy within.

**Correct:**
```xml
<objective>
## Primary Goal
Build authentication system

## Success Criteria
- Users can log in
- Sessions persist
</objective>
```

**Incorrect:**
```xml
<section name="objective">
  <subsection name="primary-goal">
    <content>Build authentication system</content>
  </subsection>
</section>
```

### Task Structure

```xml
<task type="auto">
  <name>Task N: Action-oriented name</name>
  <files>src/path/file.ts, src/other/file.ts</files>
  <action>What to do, what to avoid and WHY</action>
  <verify>Command or check to prove completion</verify>
  <done>Measurable acceptance criteria</done>
</task>
```

---

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | kebab-case | `execute-phase.md` |
| Commands | `gsd:kebab-case` | `gsd:execute-phase` |
| XML tags | kebab-case | `<execution_context>` |
| Step names | snake_case | `name="load_project_state"` |
| Bash variables | CAPS_UNDERSCORES | `PHASE_ARG`, `PLAN_START_TIME` |
| Type attributes | colon separator | `type="checkpoint:human-verify"` |

---

## Language & Tone

### Imperative Voice

Use direct commands: "Execute tasks", "Create file", "Read STATE.md"

Avoid passive voice: "Execution is performed", "The file should be created"

### No Filler

Absent: "Let me", "Just", "Simply", "Basically", "I'd be happy to"

Present: Direct instructions, technical precision

### No Sycophancy

Absent: "Great!", "Awesome!", "Excellent!", "I'd love to help"

Present: Factual statements, verification results, direct answers

### Brevity with Substance

| Good | Bad |
|------|-----|
| "JWT auth with refresh rotation using jose library" | "Phase complete" |
| "POST /api/auth/login returns 200 with Set-Cookie" | "Authentication implemented" |

---

## Anti-Patterns to Avoid

### Enterprise Patterns (Banned)

These patterns are explicitly excluded from GSD:

| Pattern | Why Banned |
|---------|------------|
| Story points | Solo dev doesn't need estimation theater |
| Sprint ceremonies | No team to coordinate |
| RACI matrices | One person, one AI |
| Human dev time estimates | Use AI execution time instead |
| Change management processes | Ship fast, iterate |
| Documentation for documentation's sake | Only useful docs |

### Temporal Language (Banned in Implementation Docs)

Avoid: "We changed X to Y", "Previously", "No longer", "Instead of"

Use: Describe current state only

Exception: CHANGELOG.md, MIGRATION.md, git commits

### Generic XML (Banned)

Avoid: `<section>`, `<item>`, `<content>`

Use: Semantic purpose tags: `<objective>`, `<verification>`, `<action>`

### Vague Tasks (Banned)

| Vague | Specific |
|-------|----------|
| "Add authentication" | "Add JWT auth with refresh rotation using jose library, store in httpOnly cookie, 15min access / 7day refresh" |
| "Create the API" | "Create POST /api/projects endpoint accepting {name, description}, validates name length 3-50 chars, returns 201 with project object" |
| "Handle errors" | "Wrap API calls in try/catch, return {error: string} on 4xx/5xx, show toast via sonner on client" |

---

## Progressive Disclosure

Information flows through layers:

| Layer | Purpose | Example |
|-------|---------|---------|
| Command | High-level objective | "Should I use this?" |
| Workflow | Detailed process | "What happens?" |
| Template | Concrete structure | "What does output look like?" |
| Reference | Deep dive | "Why this design?" |

Each layer answers different questions. Don't duplicate information across layers.

---

## Commit Conventions

### Format

```
{type}({phase}-{plan}): {description}
```

### Types

| Type | Use |
|------|-----|
| `feat` | New feature |
| `fix` | Bug fix |
| `test` | Tests only (TDD RED) |
| `refactor` | Code cleanup (TDD REFACTOR) |
| `docs` | Documentation/metadata |
| `chore` | Config/dependencies |

### Rules

One commit per task during execution. Capture hash for SUMMARY.md. Atomic, traceable, revertable.
