---
name: oc-skill-management
description: Provides guidance on how to manage, create, and update the agent's own skills. Use this skill when you need to discover new capabilities, or when the user asks to create a new skill or improve an existing one.
---

# Skill Management

This skill provides instructions for managing your own skills within the Manus environment. Unlike systems that use a command-line tool for skill installation, Manus manages skills as files in a dedicated directory.

## When to Use

- When you need to see what skills are currently available.
- When the user asks you to learn a new capability, create a new skill, or update an existing one.

## Discovering Skills

To see all the skills available to you, list the contents of the `/home/ubuntu/skills` directory.

```shell
ls -F /home/ubuntu/skills
```

Each subdirectory represents a skill. To understand what a skill does and how to use it, read its `SKILL.md` file.

```shell
cat /home/ubuntu/skills/some-skill/SKILL.md
```

## Creating and Updating Skills

To create a new skill or update an existing one, you MUST use the `skill-creator` skill. This skill provides a detailed workflow and instructions to ensure that any new or modified skill is structured correctly and integrates properly with the Manus agent.

To begin, read the instructions for the `skill-creator` skill:

```shell
cat /home/ubuntu/skills/skill-creator/SKILL.md
```

Follow the instructions provided in that skill to proceed with the creation or update process. Do not attempt to modify skill files directly without first consulting the `skill-creator` skill.
