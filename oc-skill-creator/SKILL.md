---
name: oc-skill-creator
description: Guide for creating or updating skills that extend Manus via specialized knowledge, workflows, or tool integrations. For any modification or improvement request, MUST first read this skill and follow its update workflow instead of editing files directly.
---

# Skill Creator

This skill provides guidance for creating or updating skills that extend Manus's capabilities.

## Core Principles

- **Concise is Key**: Assume Manus is already smart. Only add non-obvious procedural knowledge, concise examples, and essential context. Avoid verbose explanations.
- **Set Appropriate Degrees of Freedom**: Match the level of specificity to the task's fragility. Use high-freedom text instructions for flexible tasks, and low-freedom scripts for fragile, deterministic operations.

## Anatomy of a Skill

A skill is a directory containing a `SKILL.md` file and optional resources.

```
skill-name/
├── SKILL.md (required)
└── resources/ (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation to be loaded into context as needed
    └── assets/           - Files for use in output (templates, icons, etc.)
```

### SKILL.md

- **Frontmatter (YAML)**: Contains `name` and `description`. The description is critical for triggering the skill and should clearly state what the skill does and when to use it.
- **Body (Markdown)**: Instructions for using the skill and its resources. This is loaded only after the skill is triggered.

### Bundled Resources

- **Scripts (`scripts/`)**: For reliable, repeatable tasks. Test scripts before including them.
- **References (`references/`)**: For detailed documentation, schemas, or API specifications. Keep `SKILL.md` lean by moving extensive documentation here.
- **Assets (`assets/`)**: For files used in the final output, like templates or boilerplate code.

## Skill Update Workflow

When a user requests a new skill or an improvement to an existing one, follow this workflow:

1.  **Understand the Goal**: Clarify the user's request with concrete examples. What should the skill do? What triggers it?
2.  **Plan the Skill Contents**: Identify what reusable resources (`scripts`, `references`, `assets`) are needed.
3.  **Create or Modify the Skill**:
    - Create a new directory for the skill (e.g., `/home/ubuntu/skills/{skill-name}`).
    - Write or update the `SKILL.md` file, following the principles above.
    - Add or modify any bundled resources.
4.  **Test the Skill**: Use the skill to perform a relevant task to ensure it works as expected.
5.  **Submit for Review**: Once the skill is working correctly, indicate that the new or updated skill is ready.

### Writing Guidelines

- Use imperative/infinitive form (e.g., "Create a file" not "Creates a file").
- Be concise and direct.
- Use the `/home/ubuntu/` directory for all file paths.
- Ensure shell commands are compatible with Ubuntu 22.04.
