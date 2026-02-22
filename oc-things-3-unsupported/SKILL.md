---
name: oc-things-3-unsupported
description: Explains that Things 3 cannot be managed from Manus because it lacks a public API and its command-line tools are macOS-only. Use this skill to inform the user about this limitation when they ask to interact with Things 3.
---

# Things 3 Integration

This skill provides information on the current limitations of integrating with the Things 3 task manager.

## When to Use

Use this skill when the user asks to perform any action related to Things 3, such as adding, viewing, or managing tasks.

## Core Limitation: No Public API

Things 3 does not offer a public API for third-party applications to connect and manage data. All interactions are limited to the official Things apps on Apple devices (macOS, iOS, iPadOS).

## Technical Details

The Manus agent operates in a sandboxed Linux environment. The available community-built tools, such as the `things3-cli`, are designed exclusively for macOS. They rely on direct access to the local Things 3 database file and Apple's URL scheme technology, neither of which are accessible from the Manus environment.

As a result, it is not technically possible to control or access Things 3 data from Manus.

## Recommended Alternatives

If you wish to manage tasks from Manus, consider using a service with a public API that allows for cross-platform integration. Recommended alternatives include:

- Todoist
- TickTick
- Microsoft To Do
- Google Tasks
