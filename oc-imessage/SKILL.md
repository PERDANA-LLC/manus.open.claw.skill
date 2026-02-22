---
name: oc-imessage
description: >
  Handles user requests to send iMessage or SMS by using the Gmail API. Use this skill when the user wants to send a text message, SMS, or iMessage. It clarifies to the user that the message will be sent as an email.

---

# Send iMessage / SMS via Email

This skill provides a way to fulfill user requests for sending iMessages or SMS messages by using email as the transport mechanism, as direct iMessage/SMS integration is not available in this environment.

## When to Use

- User explicitly asks to send an iMessage or SMS.
- User wants to send a message to a phone number, and email is an acceptable fallback.

## When NOT to Use

- For other messaging platforms like Telegram, Signal, WhatsApp, Discord, or Slack, use their respective tools or skills if available.
- When the user requires a native iMessage or SMS and is unwilling to use email as an alternative.

## Core Workflow

1.  **Acknowledge the Request**: Recognize the user's intent to send a text-based message (iMessage/SMS).
2.  **Clarify the Method**: Inform the user that the message will be sent as an email because native SMS/iMessage is not supported. For example: "I can send that message for you. Since I'm not on a mobile device, it will be sent as an email from your connected Gmail account. Is that okay?"
3.  **Gather Information**: Collect the recipient's contact information (email address) and the message content.
4.  **Send the Message**: Use the `gmail_send_messages` tool via the `manus-mcp-cli` to send the email.

## Example: Sending a Message

If the user says, "Text my wife at wife@example.com that I'm running late for dinner."

You would execute the following command:

```bash
manus-mcp-cli tool call gmail_send_messages --server gmail --input '{
  "messages": [
    {
      "to": ["wife@example.com"],
      "subject": "Message from Thomas",
      "content": "I\'m running late for dinner."
    }
  ]
}'
```

This command will trigger a confirmation step in the user interface before the email is actually sent, ensuring user consent.
