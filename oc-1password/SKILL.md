---
name: oc-1password
description: Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in (single or multi-account), or reading/injecting/running secrets via op.
---

# 1Password CLI

This skill describes how to install and use the 1Password CLI (`op`) to manage secrets within the Manus environment.

## When to Use

- When you need to install the 1Password CLI for the first time.
- When you need to sign in to a 1Password account.
- When you need to retrieve, inject, or run applications with secrets from 1Password.

## Installation

To install the 1Password CLI on the Ubuntu 22.04 sandbox, use the following commands. These commands add the 1Password APT repository and install the `op` CLI.

```bash
curl -sS https://downloads.1password.com/linux/keys/1password.asc | sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/amd64 stable main' | sudo tee /etc/apt/sources.list.d/1password.list
sudo mkdir -p /etc/debsig/policies/AC2D62742012EA22
curl -sS https://downloads.1password.com/linux/debian/debsig/1password.pol | sudo tee /etc/debsig/policies/AC2D62742012EA22/1password.pol
sudo apt-get update && sudo apt-get install 1password-cli
```

After installation, verify it was successful:

```bash
op --version
```

## Workflow: Using Shell Sessions for Authentication

The Manus `shell` tool uses a fresh environment for each command. To maintain an authenticated `op` session, you must run all `op` commands within the same named shell session. This avoids repeated sign-in prompts.

1.  **Start a Session and Sign In**: Create a named session and use `op signin`. You may need to follow interactive prompts.

    ```bash
    # The first command creates the session 'op-session'
    op signin --account my.1password.com
    ```

2.  **Verify Authentication**: In the same session, confirm your identity.

    ```bash
    # Run in the same 'op-session'
    op whoami
    ```

3.  **Execute Commands**: Continue using the same session for all subsequent `op` commands.

    ```bash
    # Run in the same 'op-session'
    op vault list
    op read "op://vault/item/field"
    ```

If you have multiple accounts, use the `--account` flag or set the `OP_ACCOUNT` environment variable within the session.

## Guardrails

-   Never paste secrets directly into logs, code, or other files.
-   Prefer using `op run --` or `op inject` to provide secrets to scripts and applications rather than writing them to disk.
-   If a command returns an error indicating you are not signed in, re-run `op signin` within the same shell session.
