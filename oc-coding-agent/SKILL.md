---
name: oc-coding-agent
description: "Delegates coding tasks to interactive command-line coding agents like Codex, Claude, or Pi. Use this skill for building new features, refactoring large codebases, reviewing pull requests, or any iterative coding task that benefits from an AI agent with file system access."
---

# Coding Agent

This skill provides a framework for delegating complex coding tasks to interactive AI agents that run in the command line. It leverages background shell sessions to manage the agent's lifecycle, allowing for long-running tasks, monitoring, and interaction.

## When to Use

- **Building/Creating:** When you need to build new features, applications, or components from scratch.
- **Refactoring:** For large-scale code refactoring that involves multiple files and complex changes.
- **Pull Request Reviews:** To have an AI agent review a pull request by checking it out in a temporary, isolated directory.
- **Iterative Development:** For any coding task that requires file exploration, trial-and-error, and iterative refinement.

## When NOT to Use

- For simple, one-line code fixes where using the `file(action='edit', ...)` tool is more efficient.
- For simply reading or understanding code; use the `file(action='read', ...)` tool instead.

## The Pattern: Directory Scoping & Background Sessions

For any non-trivial coding task, the best practice is to run the coding agent in a specific working directory and as a background process. This provides focus and control.

1.  **Isolate the Workspace:** Always run the agent inside a dedicated project directory. This prevents it from accessing unrelated files and focuses its context.
2.  **Run in Background:** Use the `shell` tool with a `timeout` to start the agent process. The `timeout` allows the `exec` call to return immediately, making it a background task. Give the session a unique name to manage it later.
3.  **Monitor and Interact:** Use the session name to view output, send input, or terminate the agent as needed.

### Example Workflow

```python
# 1. Start the agent as a background process in a specific directory
# Use a short timeout to let the exec command return immediately.
print(default_api.shell(
    brief="Start the coding agent in the background",
    action='exec',
    session='coding-agent-snake-game',
    command='cd /home/ubuntu/snake-game && codex exec --full-auto \'Build a snake game\''
    timeout=5
))

# 2. Monitor the agent's progress by viewing the session output
print(default_api.shell(
    brief="Check the agent's log output",
    action='view',
    session='coding-agent-snake-game'
))

# 3. Interact with the agent if it prompts for input
# The '\n' is crucial to simulate pressing Enter.
print(default_api.shell(
    brief="Send input to the agent",
    action='send',
    session='coding-agent-snake-game',
    input='yes\n'
))

# 4. Terminate the agent if it gets stuck or needs to be stopped
print(default_api.shell(
    brief="Kill the agent process",
    action='kill',
    session='coding-agent-snake-game'
))
```

## Reviewing Pull Requests

To prevent the agent from accidentally modifying your main project, **always** clone the repository into a temporary directory before starting a review.

```bash
# 1. Create a temporary directory for the review
REVIEW_DIR=$(mktemp -d)

# 2. Clone the repo and check out the PR
git clone https://github.com/user/repo.git $REVIEW_DIR
cd $REVIEW_DIR && gh pr checkout 130

# 3. Start the agent in the temporary directory
# You would run this command via the shell tool
cd $REVIEW_DIR && codex review --base origin/main

# 4. Clean up the temporary directory after the review is complete
rm -rf $REVIEW_DIR
```

## Parallel Issue Fixing with `git worktree`

You can fix multiple issues in parallel by creating a separate `git worktree` for each issue. This creates a linked directory with a clean checkout of a specific branch, allowing you to run agents independently without interfering with each other.

```bash
# 1. Create worktrees for each issue branch
git worktree add -b fix/issue-78 /tmp/issue-78 main
git worktree add -b fix/issue-99 /tmp/issue-99 main

# 2. Launch a coding agent in each worktree as a background process
# (using the shell tool for each command)
cd /tmp/issue-78 && pnpm install && codex --yolo 'Fix issue #78: <description>. Commit and push.'
cd /tmp/issue-99 && pnpm install && codex --yolo 'Fix issue #99. Implement the approved edits and commit.'

# 3. Monitor the agents and create PRs once the work is done
cd /tmp/issue-78 && git push -u origin fix/issue-78
gh pr create --title "fix: ..." --body "..."

# 4. Clean up the worktrees
git worktree remove /tmp/issue-78
```

## Important Rules

1.  **Respect Tool Choice:** If the user asks for a specific agent (e.g., Codex), use that agent. Do not substitute without reason.
2.  **Don't Take Over:** If an agent fails or hangs, try restarting it or ask the user for direction. Do not silently start coding the solution yourself.
3.  **Be Patient:** Long-running coding tasks can be slow. Monitor the logs and avoid killing a session prematurely.
4.  **Keep the User Informed:** When running background tasks, send progress updates to the user at key milestones (e.g., task start, agent needs input, task completion, errors).
