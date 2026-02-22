---
name: oc-eightctl
description: Control Eight Sleep smart beds, including temperature, alarms, and schedules. Use this skill to manage your Eight Sleep pod via the command line.
---

# Eight Sleep Control (eightctl)

This skill allows you to control your Eight Sleep pod using the `eightctl` command-line tool.

## When to Use

Use this skill when you need to programmatically or manually control your Eight Sleep pod from the command line. This is useful for automating your sleep environment, setting temperatures, and managing alarms.

## Installation

To use this skill, you first need to install the `eightctl` tool. You can do this using `go`:

```bash
go install github.com/steipete/eightctl/cmd/eightctl@latest
```

## Authentication

`eightctl` requires authentication with your Eight Sleep account. You can configure this in two ways:

1.  **Configuration File:** Create a file at `/home/ubuntu/.config/eightctl/config.yaml` with your email and password.
2.  **Environment Variables:** Set the `EIGHTCTL_EMAIL` and `EIGHTCTL_PASSWORD` environment variables.

## Quick Start

Here are some basic commands to get you started:

-   `eightctl status`: Check the current status of your pod.
-   `eightctl on`: Turn the pod on.
-   `eightctl off`: Turn the pod off.
-   `eightctl temp 20`: Set the temperature to 20.

## Common Tasks

`eightctl` can also manage alarms, schedules, and more:

-   **Alarms:** `eightctl alarm list|create|dismiss`
-   **Schedules:** `eightctl schedule list|create|update`
-   **Audio:** `eightctl audio state|play|pause`
-   **Base:** `eightctl base info|angle`
