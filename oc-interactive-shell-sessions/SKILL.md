---
name: oc-interactive-shell-sessions
description: Use the shell tool to manage long-running interactive sessions, send input to processes, and view their output. This is the standard way to handle interactive command-line tools and long-running background processes.
---

# Interactive Shell Sessions

The `shell` tool allows you to create and interact with persistent shell sessions. This is essential for running interactive command-line applications, managing long-running background processes, and scripting interactions with them. Each session is identified by a unique name.

## When to Use

- When you need to run a command-line tool that requires user input (e.g., answering prompts).
- When you need to start a long-running process (like a web server or a build task) and check on it later.
- When you need to send commands or data to a running process.
- When you want to view the output of a background process without stopping it.
- For tasks that would typically use `tmux` or `screen`.

## When NOT to Use

- For simple, non-interactive commands that finish quickly. Use a regular `shell('exec', ...)` call for those.
- When you just need to read or write a file. Use the `file` tool instead.

## Core Concepts

You interact with sessions using the `shell` tool's different actions:

- `exec`: Execute a new command. If you provide a new `session` name, it creates a new session. This is how you start a background process. Use a `timeout` for server-like commands that don't exit.
- `send`: Send text or keystrokes (like `\n` for Enter) to a process running in a session.
- `view`: See the current state and output of a session.
- `wait`: Wait for a process in a session to complete.
- `kill`: Terminate the process running in a session.

## Common Workflows

### Starting a Long-Running Process

To start a process (e.g., a development server) in the background, use `exec` with a unique session name and a short timeout. The timeout prevents the agent from waiting for the server to exit.

**Example:** Start a Python web server in a session named `web-server`.

```python
print(default_api.shell(
    brief="Start a simple web server in the background.",
    action='exec',
    session='web-server',
    command='python3 -m http.server 8080',
    timeout=5
))
```

### Checking the Output of a Session

Use the `view` action to see the latest output from the process running in the session.

```python
print(default_api.shell(
    brief="Check the output of the web server.",
    action='view',
    session='web-server'
))
```

### Interacting with a Process

Some command-line tools require interactive input. Use the `send` action to provide it. Always end your input with `\n` to simulate pressing the Enter key.

**Example:** Respond to a confirmation prompt.

```python
# The tool is waiting for a 'y/n' confirmation.
print(default_api.shell(
    brief="Confirm the action by sending 'y' and pressing Enter.",
    action='send',
    session='interactive-tool',
    input='y\n'
))
```

### Stopping a Session

When you are finished with a background process, you can terminate it using the `kill` action.

```python
print(default_api.shell(
    brief="Stop the web server.",
    action='kill',
    session='web-server'
))
```
