---
name: oc-note-taking
description: A simple, file-based system for creating, searching, and managing notes within the sandbox. Use this for storing temporary information, observations, logs, or drafts when a dedicated note-taking application is not available.
---

# File-Based Note Taking

This skill provides a simple, file-based system for managing notes directly within the Manus sandbox. Notes are stored as Markdown files in the `/home/ubuntu/notes/` directory. This approach ensures that notes are easily accessible, versionable, and can be manipulated with standard shell tools.

## When to Use

- To jot down temporary information, ideas, or observations during a task.
- To save outputs from commands or snippets of text from web browsing.
- To draft content or structure thoughts before creating a final document.
- When a task requires persistent storage of text that is not part of the final deliverable.

## When NOT to Use

- For complex, structured data (use a database or a structured file format like JSON or CSV).
- For managing sensitive information or credentials.
- When a dedicated, feature-rich note-taking application with a user interface is required.

## Getting Started

First, ensure the notes directory exists:

```bash
mkdir -p /home/ubuntu/notes
```

## Common Operations

### Create a Note

You can create a new note with a specific title or create a quick note with a timestamped filename.

**With a specific title:**
```bash
echo "# My Note Title\n\nThis is the initial content of my note." > /home/ubuntu/notes/my-note.md
```

**Create a quick, empty note:**
```bash
touch "/home/ubuntu/notes/$(date +%Y-%m-%d-%H-%M-%S)-quick-note.md"
```

### Read a Note

Use the `file` tool to read the content of a note.

```python
# Manus tool call
default_api.file(action="read", path="/home/ubuntu/notes/my-note.md")
```

### Append Text to a Note

Use the `file` tool with `action="append"` or the shell `>>` redirect to add content to an existing note.

```bash
echo "\nThis is additional content." >> /home/ubuntu/notes/my-note.md
```

### List All Notes

To see all the notes you have created:

```bash
ls -l /home/ubuntu/notes/
```

### Search Notes

Use the `match` tool with `action="grep"` to search for text across all your notes.

```python
# Manus tool call
default_api.match(action="grep", scope="/home/ubuntu/notes/**/*.md", regex="search term")
```
