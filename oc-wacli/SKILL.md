---
name: oc-wacli
description: Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI. Use when asked to message someone on WhatsApp or to search/sync WhatsApp history.
---

# WhatsApp CLI (wacli)

This skill allows you to interact with WhatsApp from the command line using the `wacli` tool.

## When to Use

- When the user explicitly asks you to send a WhatsApp message to a third party.
- When the user asks to search their WhatsApp message history.
- When the user asks to sync their WhatsApp message history.

## When NOT to Use

- Do NOT use this skill for normal conversations with the user. This tool is for initiating contact with *other* people on the user's behalf.

## Safety

- Before sending a message, always confirm the recipient's phone number and the message content with the user.
- If any part of the request is ambiguous, ask for clarification before proceeding.

## Installation

`wacli` can be installed using `go`. First, ensure `go` is installed, then install `wacli`.

```bash
sudo apt-get update && sudo apt-get install -y golang
go install github.com/steipete/wacli/cmd/wacli@latest
```

The binary will be placed in `~/go/bin`. You may need to add this to your `$PATH`.

## Authentication and Sync

1.  **Authenticate**: Run `wacli auth`. This will display a QR code. You will need to instruct the user to scan this QR code with their WhatsApp mobile app (in Settings > Linked Devices > Link a Device).
2.  **Sync**: After authentication, `wacli` will perform an initial sync. To keep the connection alive and sync new messages, you can run `wacli sync --follow` in a background shell session.
3.  **Check Status**: Use `wacli doctor` to check the connection and authentication status.

## Usage

### Finding Chats and Messages

- **List Chats**: `wacli chats list --limit 20 --query "name or number"`
- **Search Messages in a Chat**: `wacli messages search "query" --limit 20 --chat <jid>`
- **Search Messages by Date**: `wacli messages search "invoice" --after 2025-01-01 --before 2025-12-31`

### Sending Messages

- **Send Text Message**: `wacli send text --to "+14155551212" --message "Hello! Are you free at 3pm?"`
- **Send to Group**: `wacli send text --to "1234567890-123456789@g.us" --message "Running 5 min late."`
- **Send File**: `wacli send file --to "+14155551212" --file /path/to/your/file.pdf --caption "Here is the agenda."`

### Notes

- **JIDs**: Chat identifiers (JIDs) for direct chats look like `<number>@s.whatsapp.net`, and group JIDs look like `<id>@g.us`. Use `wacli chats list` to find the correct JID.
- **Data Directory**: `wacli` stores its data in `/home/ubuntu/.wacli` by default.
- **JSON Output**: Use the `--json` flag for machine-readable output that can be parsed by scripts.
