---
name: oc-github
description: "GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, API queries. Use when: (1) checking PR status or CI, (2) creating/commenting on issues, (3) listing/filtering PRs or issues, (4) viewing run logs. NOT for: complex web UI interactions requiring manual browser flows, bulk operations across many repos, or when gh auth is not configured."
---

# GitHub Skill

This skill provides the capability to interact with GitHub repositories, issues, pull requests, and continuous integration (CI) workflows using the `gh` command-line interface (CLI). The `gh` tool is pre-installed and authenticated in the environment, so no setup is required.

## When to Use

Use this skill for tasks directly related to managing GitHub resources programmatically. Examples include:

- Checking the status, reviews, or merge readiness of a pull request.
- Viewing the status and logs of CI/CD workflow runs.
- Creating, closing, or commenting on issues.
- Creating or merging pull requests.
- Querying the GitHub API for specific repository data.
- Listing repositories, releases, or collaborators.

## When NOT to Use

Avoid using this skill for the following scenarios:

- **Local Git Operations**: For actions like `commit`, `push`, `pull`, or `branch`, use the `git` command directly in the shell.
- **Non-GitHub Repositories**: This skill is specific to GitHub and will not work with other platforms like GitLab or Bitbucket.
- **Cloning Repositories**: Use `git clone` for cloning repositories.
- **In-depth Code Review**: For detailed analysis of code changes or complex multi-file diffs, it is better to read the files directly and use dedicated editing tools.

## Common Commands

Below are examples of common `gh` commands. Remember to replace `owner/repo` with the appropriate repository owner and name.

### Pull Requests

```bash
# List pull requests in a repository
gh pr list --repo owner/repo

# Check the CI status for a specific pull request
gh pr checks 55 --repo owner/repo

# View the details of a pull request
gh pr view 55 --repo owner/repo

# Create a new pull request
gh pr create --title "feat: Implement new feature" --body "This PR adds the following functionality..."

# Merge a pull request
gh pr merge 55 --squash --repo owner/repo
```

### Issues

```bash
# List open issues in a repository
gh issue list --repo owner/repo --state open

# Create a new issue
gh issue create --title "Bug: The application crashes on startup" --body "Steps to reproduce..."

# Close an issue
gh issue close 42 --repo owner/repo
```

### CI/Workflow Runs

```bash
# List the 10 most recent workflow runs
gh run list --repo owner/repo --limit 10

# View the details of a specific workflow run
gh run view <run-id> --repo owner/repo

# View the logs for any failed steps in a run
gh run view <run-id> --repo owner/repo --log-failed

# Re-run any failed jobs in a workflow run
gh run rerun <run-id> --failed --repo owner/repo
```

### API Queries

You can use the `gh api` command to make direct calls to the GitHub REST API.

```bash
# Get the title, state, and author of a pull request
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# List the names of all labels in a repository
gh api repos/owner/repo/labels --jq '.[].name'

# Get repository statistics like stars and forks
gh api repos/owner/repo --jq '{stars: .stargazers_count, forks: .forks_count}'
```

## Advanced Usage

### JSON Output and Filtering

Most commands support the `--json` flag to produce structured output, which can be filtered using the `--jq` flag.

```bash
# List issue numbers and titles
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'

# List all mergeable pull requests
gh pr list --json number,title,state,mergeable --jq '.[] | select(.mergeable == "MERGEABLE")'
```

### PR Review Summary Template

This template generates a concise summary for a pull request review.

```bash
PR=55 REPO=owner/repo
echo "## PR #$PR Summary"
gh pr view $PR --repo $REPO --json title,body,author,additions,deletions,changedFiles \
  --jq '"**\(.title)** by @\(.author.login)\n\n\(.body)\n\n📊 +\(.additions) -\(.deletions) across \(.changedFiles) files"'
gh pr checks $PR --repo $REPO
```

## Important Notes

- Always specify the `--repo owner/repo` flag if you are not inside a local `git` repository directory.
- You can use full GitHub URLs directly with some commands, for example: `gh pr view https://github.com/owner/repo/pull/55`.
- Be mindful of API rate limits. For repeated queries, consider caching results using `gh api --cache 1h`.
