---
name: oc-himalaya
description: "CLI to manage emails via IMAP/SMTP. Use `himalaya` to list, read, write, reply, forward, search, and organize emails from the terminal. Supports multiple accounts and message composition with MML (MIME Meta Language)."
---

# Himalaya Email CLI

Himalaya is a CLI email client that lets you manage emails from the terminal using IMAP, SMTP, Notmuch, or Sendmail backends.

## When to Use

- When you need to automate email workflows from the command line.
- For reading, composing, and managing emails in a terminal-based environment.
- When you need to integrate email functionality into shell scripts.

## When NOT to Use

- For viewing complex HTML emails, as it's a text-based client.
- If you require a graphical user interface for managing emails.

## Prerequisites

1.  Himalaya CLI installed. To install, run:

    ```shell
    curl -sSL https://raw.githubusercontent.com/pimalaya/himalaya/main/install.sh | sh
    ```

2.  A configuration file at `/home/ubuntu/.config/himalaya/config.toml`.
3.  IMAP/SMTP credentials configured.

## Configuration Setup

Run the interactive wizard to set up an account:

```shell
himalaya account configure
```

Or create `/home/ubuntu/.config/himalaya/config.toml` manually:

```toml
[accounts.personal]
email = "you@example.com"
display-name = "Your Name"
default = true

backend.type = "imap"
backend.host = "imap.example.com"
backend.port = 993
backend.encryption.type = "tls"
backend.login = "you@example.com"
backend.auth.type = "password"
backend.auth.cmd = "echo 'your-password'"  # Replace with a secure password management method

message.send.backend.type = "smtp"
message.send.backend.host = "smtp.example.com"
message.send.backend.port = 587
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "you@example.com"
message.send.backend.auth.type = "password"
message.send.backend.auth.cmd = "echo 'your-password'" # Replace with a secure password management method
```

## Common Operations

### List Folders

```shell
himalaya folder list
```

### List Emails

List emails in INBOX (default):

```shell
himalaya envelope list
```

### Read an Email

Read email by ID:

```shell
himalaya message read 42
```

### Write a New Email

```shell
cat << 'EOF' | himalaya template send
From: you@example.com
To: recipient@example.com
Subject: Test Message

Hello from Himalaya!
EOF
```
