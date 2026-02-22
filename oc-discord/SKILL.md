---
name: oc-discord
description: "Interact with the Discord platform to send messages, manage channels, and perform other actions. Use this skill for any task involving communication or automation on Discord."
---

# Discord Integration

This skill provides instructions for interacting with the Discord API using `curl` commands within the `shell` tool. To use this skill, you must first have a Discord Bot Token.

## Authentication

All API requests must include your Discord Bot Token in the `Authorization` header.

```bash
export DISCORD_BOT_TOKEN="YOUR_BOT_TOKEN_HERE"

# Verify token (optional)
curl -H "Authorization: Bot $DISCORD_BOT_TOKEN" https://discord.com/api/v10/users/@me
```

## When to Use

- When you need to send messages, announcements, or notifications to a Discord channel.
- When asked to read message history from a channel.
- When you need to manage Discord resources like channels, threads, or user roles.
- For automating moderation tasks or creating interactive components in Discord.

## Common Actions

Below are examples of how to perform common Discord actions using `curl`. Remember to replace placeholder values like `CHANNEL_ID`, `MESSAGE_ID`, etc., with actual IDs.

### Send a Message

To send a simple text message to a channel:

```bash
CHANNEL_ID="123456789012345678"
MESSAGE_CONTENT="Hello from Manus!"

curl -X POST -H "Content-Type: application/json" \
     -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
     -d "{\"content\": \"$MESSAGE_CONTENT\"}" \
     https://discord.com/api/v10/channels/$CHANNEL_ID/messages
```

### Read Channel Messages

To retrieve the last 10 messages from a channel:

```bash
CHANNEL_ID="123456789012345678"
LIMIT=10

curl -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
     "https://discord.com/api/v10/channels/$CHANNEL_ID/messages?limit=$LIMIT"
```

### Edit a Message

To edit a message you have already sent:

```bash
CHANNEL_ID="123456789012345678"
MESSAGE_ID="987654321098765432"
NEW_CONTENT="This is the corrected message."

curl -X PATCH -H "Content-Type: application/json" \
     -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
     -d "{\"content\": \"$NEW_CONTENT\"}" \
     https://discord.com/api/v10/channels/$CHANNEL_ID/messages/$MESSAGE_ID
```

### Delete a Message

To delete a specific message:

```bash
CHANNEL_ID="123456789012345678"
MESSAGE_ID="987654321098765432"

curl -X DELETE -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
     https://discord.com/api/v10/channels/$CHANNEL_ID/messages/$MESSAGE_ID
```

### Create a Thread

To start a new thread from an existing message:

```bash
CHANNEL_ID="123456789012345678"
MESSAGE_ID="987654321098765432"
THREAD_NAME="Discussion about the latest update"

curl -X POST -H "Content-Type: application/json" \
     -H "Authorization: Bot $DISCORD_BOT_TOKEN" \
     -d "{\"name\": \"$THREAD_NAME\"}" \
     https://discord.com/api/v10/channels/$CHANNEL_ID/messages/$MESSAGE_ID/threads
```
