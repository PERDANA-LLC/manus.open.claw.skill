---
name: oc-bluebubbles
description: >
  Use to send and manage iMessages via a self-hosted BlueBubbles server. It allows for sending texts, attachments, reactions (tapbacks), and managing messages.

---

# BlueBubbles iMessage Integration

## Overview

This skill enables interaction with iMessage through a self-hosted [BlueBubbles](https://bluebubbles.app/) server. It provides instructions for using `curl` to call the BlueBubbles API for sending messages, adding reactions, replying, and more. To use this skill, you must have a running BlueBubbles server and have the server URL and password available.

### When to Use

- When the user asks to send an iMessage.
- When you need to interact with iMessage conversations, such as sending reactions or replying to specific messages.
- When a task requires sending files or images via iMessage.

### When NOT to Use

- If the user has not provided credentials for a BlueBubbles server.
- For sending messages through other platforms like SMS, WhatsApp, or Telegram.

## Setup

Before using the commands below, ensure you have set the following environment variables with your BlueBubbles server details:

```bash
export BLUEBUBBLES_SERVER="http://your-server-address:port"
export BLUEBUBBLES_PASSWORD="your-password"
```

## Actions

The following examples demonstrate how to use `curl` to interact with the BlueBubbles API. The `target` can be a phone number in E.164 format (e.g., `+15551234567`), an email address, or a chat GUID.

### Send a Message

To send a simple text message:

```bash
curl -X POST "$BLUEBUBBLES_SERVER/api/v1/message/text" \
--header "Content-Type: application/json" \
--header "Authorization: $BLUEBUBBLES_PASSWORD" \
--data-raw '{
  "chatGuid": "iMessage;+;chat_guid_or_phone_number",
  "text": "Hello from Manus!"
}'
```

### Send a Message with an Effect

To send a message with an iMessage screen or bubble effect:

```bash
curl -X POST "$BLUEBUBBLES_SERVER/api/v1/message/text" \
--header "Content-Type: application/json" \
--header "Authorization: $BLUEBUBBLES_PASSWORD" \
--data-raw '{
  "chatGuid": "iMessage;+;chat_guid_or_phone_number",
  "text": "Wishes came true!",
  "effect": "shootingStar"
}'
```

### React to a Message (Tapback)

To add a reaction (like, love, laugh, etc.) to a specific message:

```bash
curl -X POST "$BLUEBUBBLES_SERVER/api/v1/message/react" \
--header "Content-Type: application/json" \
--header "Authorization: $BLUEBUBBLES_PASSWORD" \
--data-raw '{
  "chatGuid": "iMessage;+;chat_guid_or_phone_number",
  "messageGuid": "<message-guid>",
  "reaction": "love"
}'
```

### Send an Attachment

To send a file, first upload it to a temporary URL, then send the URL as the message content. Alternatively, you can use the BlueBubbles API to upload the attachment directly if it supports it.

```bash
# Assuming the file is at /home/ubuntu/photo.jpg
curl -X POST "$BLUEBUBBLES_SERVER/api/v1/message/attachment" \
--header "Authorization: $BLUEBUBBLES_PASSWORD" \
--form "attachment=@/home/ubuntu/photo.jpg" \
--form 'json="{\"chatGuid\": \"iMessage;+;chat_guid_or_phone_number\"}";type=application/json'
```
