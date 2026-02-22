---
name: oc-github-issues
description: "Fetches GitHub issues, spawns sub-agents to implement fixes and open PRs, then monitors and addresses PR review comments. Use this skill to automate fixing issues in a GitHub repository."
---

# GitHub Issues Auto-Fixer

This skill automates fixing GitHub issues by orchestrating sub-agents to create and manage pull requests.

## When to Use

- To automate fixing bugs or implementing enhancements in a GitHub repository.
- When you have a list of issues that can be resolved by an AI agent.

## When NOT to Use

- For issues requiring complex architectural changes or deep codebase understanding.
- For repositories where you lack permissions to create branches and pull requests.

## Phase 1: Parse Arguments

Parse user arguments, with the primary argument being the `owner/repo` of the GitHub repository.

## Phase 2: Fetch Issues

Fetch open issues from the specified repository using the GitHub API. Filter issues by labels, milestones, and assignees.

**Example `curl` command:**

```bash
curl -s -H "Authorization: Bearer $GH_TOKEN" -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/{owner}/{repo}/issues?state=open"
```

## Phase 3: Present & Confirm

Display fetched issues in a table and prompt the user for confirmation on which issues to process.

## Phase 4: Pre-flight Checks

Perform these sequential checks before proceeding:

1.  **Dirty working tree:** Ensure no uncommitted changes exist.
2.  **Record base branch:** Store the current branch name.
3.  **Verify remote access:** Confirm the remote repository is accessible.
4.  **Verify GH_TOKEN:** Validate the `GH_TOKEN`.
5.  **Check for existing PRs:** Skip issues with already open pull requests.

## Phase 5: Spawn Sub-agents (Parallel)

For each confirmed issue, spawn a sub-agent in a background process to:

1.  **Create a new branch:** `git checkout -b fix/issue-{issue_number}`
2.  **Understand the issue:** Analyze the issue's title and body.
3.  **Implement the fix:** Modify the code to resolve the issue.
4.  **Commit and push:** Commit changes and push the branch.
5.  **Create a pull request:** Open a pull request to the base branch.

**Sub-agent prompt:**

```
You are a software engineer fixing a GitHub issue. Details:

- **Issue Title:** {issue_title}
- **Issue Body:** {issue_body}

Your task:

1.  Understand and implement the fix.
2.  Commit and push changes.
3.  Create a pull request.
```

## Phase 6: PR Review Handler

This phase monitors open PRs for review comments and spawns sub-agents to address them.

### Step 6.1: Discover PRs

Fetch all open PRs matching the `fix/issue-` branch pattern.

### Step 6.2: Fetch Review Comments

For each PR, fetch review comments via the GitHub API.

### Step 6.3: Analyze Comments

Determine if comments are actionable, skipping informational or resolved ones.

### Step 6.4: Spawn Review Fix Sub-agents

For each PR with actionable feedback, spawn a sub-agent to:

1.  Check out the PR branch.
2.  Implement requested changes.
3.  Commit and push updates.
4.  Reply to review comments.

## Final Summary

After all sub-agents complete their tasks, present a summary of results, including the status of each issue and links to the pull requests.
