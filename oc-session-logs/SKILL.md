---
name: oc-session-logs
description: Search and analyze your complete conversation history. Use this skill when a user references older conversations or asks about something that was said before.
---

# Session Logs

This skill provides a set of commands to search and analyze your complete conversation history, which is stored in local JSONL files.

## When to Use

Use this skill when the user asks about:
- Prior chats or conversations.
- Historical context that is not in your immediate memory.
- What was said or decided in a previous interaction.

## Setup

The query commands rely on `jq` for JSON processing and `ripgrep` (`rg`) for fast text search. Install them if they are not already available:

```shell
sudo apt-get update && sudo apt-get install -y jq ripgrep
```

## Session Log Location

Session logs are located in a directory specific to the agent. The exact path may vary, but a common location is `~/.manus/sessions/<agentId>/`. You will need to replace `<agentId>` with the actual ID of the running agent.

- **`sessions.json`**: An index file mapping session keys to session IDs.
- **`<session-id>.jsonl`**: The full conversation transcript for a single session.

## Structure

Each `.jsonl` file contains a series of JSON objects, one per line. Key fields include:

- `type`: "session" (for metadata) or "message".
- `timestamp`: ISO 8601 timestamp.
- `message.role`: "user", "assistant", or "toolResult".
- `message.content[]`: An array of content parts, which can include text or tool calls. For human-readable content, filter for `type == "text"`.

## Common Queries

Replace `<path-to-sessions>` with the actual path to the session log directory (e.g., `~/.manus/sessions/<agentId>/`).

### List all sessions by date and size

```shell
for f in <path-to-sessions>/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  size=$(ls -lh "$f" | awk '{print $5}')
  echo "$date $size $(basename $f)"
done | sort -r
```

### Extract user messages from a session

```shell
jq -r 'select(.message.role == "user") | .message.content[]? | select(.type == "text") | .text' <path-to-sessions>/<session-id>.jsonl
```

### Search for a keyword in assistant responses across all sessions

```shell
for f in <path-to-sessions>/*.jsonl; do
  echo "--- Searching in $f ---\n"
  jq -r 'select(.message.role == "assistant") | .message.content[]? | select(.type == "text") | .text' "$f" | rg -i "keyword"
done
```

### Search across ALL sessions for a phrase

```shell
rg -l "your search phrase" <path-to-sessions>/*.jsonl
```

### Tool usage breakdown for a session

```shell
jq -r '.message.content[]? | select(.type == "toolCall") | .name' <path-to-sessions>/<session-id>.jsonl | sort | uniq -c | sort -rn
```
