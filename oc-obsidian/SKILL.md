---
name: oc-obsidian
description: Work with Obsidian vaults (plain Markdown notes) and automate via notesmd-cli.
---

# Obsidian

This skill allows you to interact with Obsidian vaults and notes using the `notesmd-cli` command-line tool. It enables you to search, create, update, and manage your notes from the command line.

## When to Use

- When you need to programmatically access or modify notes within an Obsidian vault.
- For automating note creation, such as capturing information from other sources and saving it to Obsidian.
- When you want to integrate Obsidian with other command-line tools and scripts.

## When NOT to Use

- If you need to edit the visual layout or settings of your Obsidian workspace. Use the Obsidian desktop application for that.
- For tasks that require a graphical user interface, such as interacting with Obsidian plugins that don't have command-line support.

## Installation

The `notesmd-cli` tool is required to use this skill. It can be installed from source using Go.

First, ensure you have Go installed:

```shell
sudo apt-get update && sudo apt-get install -y golang
```

Then, build and install `notesmd-cli`:

```shell
git clone https://github.com/yakitrak/notesmd-cli.git
cd notesmd-cli
go build -o notesmd-cli .
sudo install -m 755 notesmd-cli /usr/local/bin/
```

## Finding the Active Vault

Obsidian's configuration, including the list of vaults, is stored in a JSON file. On Linux, this file is typically located at:

- `$XDG_CONFIG_HOME/obsidian/obsidian.json`
- `~/.config/obsidian/obsidian.json`

You can inspect this file to find the paths to your vaults. The `notesmd-cli` tool can also help you manage a default vault.

## `notesmd-cli` Quick Start

### Set a Default Vault

Set a default vault to avoid specifying it with every command:

```shell
notesmd-cli set-default "<vault-folder-name>"
```

### Search for Notes

Search for notes by name or content:

```shell
# Search by note name (fuzzy search)
notesmd-cli search "query"

# Search within note content
notesmd-cli search-content "query"
```

### Create a Note

Create a new note, optionally with content:

```shell
notesmd-cli create "Folder/New Note Title" --content "This is the content of the new note."
```

### Move or Rename a Note

Safely move or rename a note, which also updates all links within the vault:

```shell
notesmd-cli move "old/path/to/note" "new/path/to/note"
```

### Delete a Note

Delete a note:

```shell
notesmd-cli delete "path/to/note"
```

For more detailed usage, you can always run `notesmd-cli --help`.
