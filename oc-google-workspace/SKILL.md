---
name: oc-google-workspace
description: >
  Interact with Google Workspace services. Use this skill to manage Gmail, Google Calendar, and Google Drive. This skill does not support Google Contacts, Sheets, or Docs.
---

# Google Workspace

This skill allows you to interact with Google Workspace services like Gmail, Google Calendar, and Google Drive using the command line.

## When to Use

Use this skill when you need to perform actions on your Google Workspace account, such as:
- Searching for and reading emails in Gmail.
- Sending emails from your Gmail account.
- Searching, creating, updating, or deleting events in Google Calendar.
- Listing and searching for files in Google Drive.

## When NOT to Use

- Do not use this skill for managing Google Contacts, Google Sheets, or Google Docs, as these services are not supported.

## Gmail

Interact with Gmail using the `manus-mcp-cli` tool with the `gmail` server.

### Search for Messages

To search for messages, use the `gmail_search_messages` tool. You can use any valid Gmail search query.

```bash
# Search for the 10 most recent emails from the last 7 days
manus-mcp-cli tool call gmail_search_messages --server gmail --input '{"q": "newer_than:7d", "max_results": 10}'

# Search for emails from a specific sender
manus-mcp-cli tool call gmail_search_messages --server gmail --input '{"q": "from:no-reply@github.com"}'
```

### Read Threads

To read the content of one or more email threads, use the `gmail_read_threads` tool with the thread IDs obtained from a search.

```bash
# Read a single thread
manus-mcp-cli tool call gmail_read_threads --server gmail --input '{"thread_ids": ["<thread_id>"]}'
```

### Send Messages

To send an email, use the `gmail_send_messages` tool. This will prompt the user for confirmation before sending.

```bash
# Send a simple email
manus-mcp-cli tool call gmail_send_messages --server gmail --input '{
  "messages": [
    {
      "to": ["recipient@example.com"],
      "subject": "Hello from Manus",
      "content": "This is the body of the email."
    }
  ]
}'
```

## Google Calendar

Interact with Google Calendar using the `manus-mcp-cli` tool with the `google-calendar` server.

### Search for Events

To search for calendar events, use the `google_calendar_search_events` tool. You can specify a time range.

```bash
# Search for events in the primary calendar within a specific time range
manus-mcp-cli tool call google_calendar_search_events --server google-calendar --input '{
  "time_min": "2026-03-01T00:00:00Z",
  "time_max": "2026-03-10T00:00:00Z"
}'
```

### Create an Event

To create a new event, use the `google_calendar_create_events` tool.

```bash
# Create a new 1-hour event
manus-mcp-cli tool call google_calendar_create_events --server google-calendar --input '{
  "events": [
    {
      "summary": "Team Meeting",
      "start_time": "2026-03-05T10:00:00-07:00",
      "end_time": "2026-03-05T11:00:00-07:00",
      "attendees": ["team-member@example.com"]
    }
  ]
}'
```

## Google Drive

Interact with Google Drive using the `rclone` command-line tool. The Google Drive remote is pre-configured as `manus_google_drive`.

### List Files

To list files and directories in your Google Drive, use `rclone lsf`.

```bash
# List files in the root directory
rclone lsf manus_google_drive: --config /home/ubuntu/.gdrive-rclone.ini

# Recursively list all files in a specific folder
rclone lsf -R manus_google_drive:"My Documents" --config /home/ubuntu/.gdrive-rclone.ini
```

### Search for Files

To search for files, you can pipe the output of `rclone lsf` to `grep`.

```bash
# Search for files containing "report" in their name, across the entire drive
rclone lsf -R --files-only manus_google_drive: --config /home/ubuntu/.gdrive-rclone.ini | grep -i "report"
```
