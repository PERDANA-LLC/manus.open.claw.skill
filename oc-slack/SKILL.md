---
name: oc-slack
description: A skill for interacting with Slack. Use this skill to send, edit, and delete messages, react to messages, manage pins in channels, and retrieve user information.
---

# Slack Integration

## Overview

This skill allows you to interact with the Slack API to perform various actions within your Slack workspace. To use this skill, you will need a Slack Bot token with the appropriate permissions.

## When to Use

- When you need to send messages to Slack channels or users.
- When you need to react to messages in a channel.
- When you want to pin or unpin important messages.
- When you need to fetch user information from your workspace.

## When NOT to Use

- For complex workflows that require real-time event handling. Consider building a dedicated Slack app for those use cases.
- If you do not have the necessary permissions to create a Slack app and generate a bot token.

## Setup

1.  **Create a Slack App:** Go to the [Slack API website](https://api.slack.com/apps) and create a new app in your workspace.
2.  **Add Permissions:** Under "OAuth & Permissions", add the following bot token scopes:
    - `chat:write`
    - `reactions:write`
    - `pins:write`
    - `users:read`
3.  **Install the App:** Install the app to your workspace to generate a "Bot User OAuth Token".
4.  **Set Environment Variable:** Store your token securely as an environment variable in your shell session:

    ```bash
    export SLACK_BOT_TOKEN="xoxb-your-token-here"
    ```

## Usage

All interactions are done via `curl` commands to the Slack API endpoints. You will need the `channelId` and `messageId` (timestamp) for most operations.

### Send a Message

```bash
curl -X POST -H "Authorization: Bearer $SLACK_BOT_TOKEN" -H "Content-type: application/json" --data '{
  "channel": "C12345678",
  "text": "Hello from Manus!"
}' https://slack.com/api/chat.postMessage
```

### React to a Message

```bash
curl -X POST -H "Authorization: Bearer $SLACK_BOT_TOKEN" -H "Content-type: application/json" --data '{
  "channel": "C12345678",
  "name": "white_check_mark",
  "timestamp": "1712023032.1234"
}' https://slack.com/api/reactions.add
```

### Pin a Message

```bash
curl -X POST -H "Authorization: Bearer $SLACK_BOT_TOKEN" -H "Content-type: application/json" --data '{
  "channel": "C12345678",
  "timestamp": "1712023032.1234"
}' https://slack.com/api/pins.add
```

## Ideas to try

- React with ✅ to mark completed tasks.
- Pin key decisions or weekly status updates to a channel.
- Send automated reminders or notifications to a channel.
