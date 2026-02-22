---
name: oc-voice-call
description: "Initiate outbound voice calls using Twilio's Programmable Voice API. Use this skill to deliver spoken messages to users over the phone for notifications, alerts, or automated information delivery. It requires Twilio API credentials to be configured."
---

# Voice Call with Twilio

This skill enables the agent to make outbound voice calls and speak a message using the Twilio Programmable Voice API.

## When to Use

- When you need to send a voice notification to a phone number.
- For automated alerts where a spoken message is more effective than a text message.
- When a user explicitly asks to call a number and deliver a message.

## When NOT to Use

- For sending SMS/text messages. Use a dedicated SMS skill or tool for that.
- For complex interactive voice response (IVR) systems. This skill is for simple, one-way voice messages.
- If Twilio credentials are not available.

## Requirements

This skill requires the following environment variables to be set with your Twilio credentials:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_FROM_NUMBER`: A Twilio phone number you own, in E.164 format (e.g., +14155238886).

## Usage

To make a voice call, follow these steps:

1.  **Install the Twilio Python library:**

    ```bash
    pip3 install twilio
    ```

2.  **Create a Python script** to initiate the call. Save the following code to a file named `make_call.py`.

    ```python
    import os
    import sys
    from twilio.rest import Client

    def make_voice_call(to_number, message):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        from_number = os.environ.get("TWILIO_FROM_NUMBER")

        if not all([account_sid, auth_token, from_number]):
            print("Error: Twilio credentials are not configured in environment variables.")
            sys.exit(1)

        client = Client(account_sid, auth_token)

        try:
            call = client.calls.create(
                twiml=f'<Response><Say>{message}</Say></Response>',
                to=to_number,
                from_=from_number
            )
            print(f"Call initiated with SID: {call.sid}")
            return call.sid
        except Exception as e:
            print(f"Error making call: {e}")
            sys.exit(1)

    if __name__ == "__main__":
        if len(sys.argv) != 3:
            print("Usage: python3 make_call.py <to_number> \"Your message here\"")
            sys.exit(1)
        
        to_number = sys.argv[1]
        message = sys.argv[2]
        make_voice_call(to_number, message)

    ```

3.  **Execute the script** from the shell, providing the recipient's phone number and the message.

    ```bash
    python3 make_call.py "+15555550123" "Hello from your Manus agent. This is a test call."
    ```
