---
name: oc-google-tasks-and-reminders
description: Manage Google Calendar events, which can serve as tasks and reminders, using the Google Calendar MCP integration. Use this to create, list, and manage reminders that sync with the user's Google account.
---

# Google Tasks and Reminders

This skill allows the agent to interact with the user's Google Calendar to create, view, and manage events that function as tasks and reminders. It uses the `google-calendar` MCP server.

## When to Use

- When the user asks to create a reminder, to-do, or task with a specific date or time.
- When the user wants a reminder that syncs across their devices (assuming they use Google Calendar).
- To list upcoming events or reminders from their Google Calendar.

## When NOT to Use

- For complex project management (consider dedicated tools like Notion, Asana, or GitHub Issues).
- For internal, agent-only alerts that don't need to be on the user's calendar. Use internal scheduling mechanisms for that.

## Core Concepts

All operations are performed using the `manus-mcp-cli` shell command, targeting the `google-calendar` server.

- **Events as Reminders**: A Google Calendar event with a specific start and end time serves as a reminder.
- **Calendars as Lists**: Different Google Calendars can be used to organize reminders into lists (e.g., 'Work', 'Personal'). The `calendar_id` parameter is used to specify the target calendar. Use 'primary' for the default calendar.

## Common Commands

All commands follow this basic structure:
`$ manus-mcp-cli tool call <tool_name> --server google-calendar --input '<json_arguments>'`

### Create a Reminder

Use the `google_calendar_create_events` tool. A simple reminder is an event with a summary, start time, and end time.

```bash
# Add a reminder for "Buy milk" today at 5 PM
EVENT_JSON='''{
  "events": [
    {
      "summary": "Buy milk",
      "start_time": "2026-02-22T17:00:00-08:00",
      "end_time": "2026-02-22T17:30:00-08:00",
      "reminders": [15] # Reminder 15 minutes before
    }
  ]
}'''
manus-mcp-cli tool call google_calendar_create_events --server google-calendar --input "$EVENT_JSON"
```

### View Reminders

Use the `google_calendar_search_events` tool. Filter by time using `time_min` and `time_max`.

```bash
# View reminders for today
# Note: Adjust the RFC3339 timestamps to the current date.
manus-mcp-cli tool call google_calendar_search_events --server google-calendar --input '{
  "time_min": "2026-02-22T00:00:00-08:00",
  "time_max": "2026-02-22T23:59:59-08:00"
}'

# View all upcoming reminders (next 7 days)
manus-mcp-cli tool call google_calendar_search_events --server google-calendar --input '{
  "time_min": "2026-02-22T00:00:00-08:00"
}'
```

### Complete or Delete a Reminder

To "complete" a reminder, you delete the event from the calendar using the `google_calendar_delete_events` tool. You must first get the `event_id` by searching for the event.

```bash
# First, find the event to get its ID
manus-mcp-cli tool call google_calendar_search_events --server google-calendar --input '{"q": "Buy milk"}'

# Assuming the event_id from the search result is "abcdef123456"
manus-mcp-cli tool call google_calendar_delete_events --server google-calendar --input '{
  "events": [
    {
      "event_id": "abcdef123456"
    }
  ]
}'
```
