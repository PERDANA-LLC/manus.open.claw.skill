---
name: oc-local-notes
description: Create, read, search, and manage local notes as Markdown files. Use for jotting down information, creating to-do lists, saving text snippets, or managing simple text-based records within the agent's file system.
---

# Local Note-Taking

This skill provides a simple, file-based system for managing notes. All notes are stored as Markdown files in the `/home/ubuntu/notes` directory.

## When to Use

- When the user asks to "take a note," "write something down," "remember this," or "create a to-do list."
- For storing and retrieving simple text-based information.
- When a persistent, cross-platform note-taking solution is needed that doesn't rely on external services.

## Best Practices

- Before using the skill for the first time, create the notes directory: `mkdir -p /home/ubuntu/notes`
- Use descriptive, hyphenated filenames for notes (e.g., `my-shopping-list.md`).

## Creating and Appending to Notes

Use the `file` tool to create a new note or append to an existing one.

- **Create a new note:**
  ```bash
  file(
      action="write",
      path="/home/ubuntu/notes/new-note-title.md",
      text="# New Note Title\n\nThis is the content of my new note."
  )
  ```

- **Append to an existing note:**
  ```bash
  file(
      action="append",
      path="/home/ubuntu/notes/existing-note.md",
      text="\n- Added a new item to my list."
  )
  ```

## Listing Notes

Use the `shell` tool to list all available notes.

- **List all notes:**
  ```bash
  shell(action="exec", command="ls /home/ubuntu/notes")
  ```

## Reading Notes

Use the `file` tool to read the content of a specific note.

- **Read a note:**
  ```bash
  file(action="read", path="/home/ubuntu/notes/my-note.md")
  ```

## Searching Notes

Use the `match` tool with `grep` to search for text across all your notes.

- **Search for a keyword:**
  ```bash
  match(
      action="grep",
      scope="/home/ubuntu/notes/**/*.md",
      regex="keyword"
  )
  ```

## Deleting Notes

Use the `shell` tool to delete a note file.

- **Delete a note:**
  ```bash
  shell(action="exec", command="rm /home/ubuntu/notes/note-to-delete.md")
  ```
