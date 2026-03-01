---
phase: [N]
plan: [M]
wave: [W]
depends_on: []
files_modified: []
autonomous: true
user_setup: []

must_haves:
  truths: []
  artifacts: []
---

# Plan [N].[M]: [Descriptive Name]

<objective>
[What this plan accomplishes in 1-2 sentences]

**Purpose:** [Why this matters to the project]
**Output:** [What artifacts will be created]
</objective>

<context>
Load for context:
- .planning/PROJECT.md
- .planning/ARCHITECTURE.md (if exists)
- [relevant source files]
</context>

<tasks>

<task type="auto">
  <name>Task 1: [Action-oriented name]</name>
  <files>[exact/file/paths.ext]</files>
  <action>
    [Specific implementation instructions]
    
    AVOID: [common mistake] because [reason]
  </action>
  <verify>[command or check to prove completion]</verify>
  <done>[measurable acceptance criteria]</done>
</task>

<task type="auto">
  <name>Task 2: [Action-oriented name]</name>
  <files>[exact/file/paths.ext]</files>
  <action>
    [Specific implementation instructions]
  </action>
  <verify>[command or check]</verify>
  <done>[measurable criteria]</done>
</task>

</tasks>

<verification>
After all tasks, verify:
- [ ] [Must-have 1 from frontmatter]
- [ ] [Must-have 2 from frontmatter]
</verification>

<success_criteria>
- [ ] All tasks verified
- [ ] Must-haves confirmed
- [ ] No regressions introduced
</success_criteria>

---

## Plan Guidelines

### Task Count
- **2-3 tasks per plan** - More means split into multiple plans
- Each task should take 15-60 minutes to execute

### Task Specificity
- ✅ "Create POST /api/auth/login accepting {email, password}, validate with bcrypt, return JWT in httpOnly cookie"
- ❌ "Add authentication"

### Verification
- ✅ `curl -X POST localhost:3000/api/auth/login` returns 200 with Set-Cookie header
- ❌ "It works"

### Checkpoint Types (when needed)
```xml
<task type="checkpoint:human-verify">
  <what-built>Description of completed work</what-built>
  <how-to-verify>
    1. Step to verify
    2. What to check
  </how-to-verify>
  <resume-signal>Type "approved" to continue</resume-signal>
</task>

<task type="checkpoint:decision">
  <decision>What needs deciding</decision>
  <options>
    <option id="a"><name>Option A</name><pros>Benefits</pros><cons>Tradeoffs</cons></option>
    <option id="b"><name>Option B</name><pros>Benefits</pros><cons>Tradeoffs</cons></option>
  </options>
  <resume-signal>Select: [a | b]</resume-signal>
</task>
```
