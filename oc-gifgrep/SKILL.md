---
name: oc-gifgrep
description: "Search GIF providers like Tenor and Giphy from the command line, download GIFs, and extract still frames or sprite sheets. Use this skill to find and process GIFs for inclusion in documents, presentations, or web content."
---

# gifgrep: GIF Search and Processing

This skill provides the `gifgrep` utility to find, download, and manipulate GIFs directly from the shell.

## When to Use

Use this skill when you need to programmatically find and process GIFs. For example:

- Finding a specific reaction GIF to include in a message or document.
- Downloading a set of GIFs based on a search query.
- Extracting a specific frame from a GIF as a static PNG image.
- Creating a sprite sheet from a GIF for quick previews.

## Installation

The `gifgrep` tool is not installed by default. Install it using `go`:

```bash
go install github.com/steipete/gifgrep/cmd/gifgrep@latest
```

This will place the `gifgrep` binary in the Go bin directory, which is in the system's `PATH`.

## Usage

`gifgrep` can be used to search, download, and process GIFs. API keys for Giphy or Tenor can be provided via environment variables for full access, though Tenor works with a demo key by default.

### Searching for GIFs

- **Interactive Search (TUI):** For an interactive terminal-based UI to browse results.
  ```bash
  gifgrep tui "your search query"
  ```

- **CLI Search:** To get a list of URLs or JSON data.
  ```bash
  # Get the top 3 GIF URLs for "cats"
  gifgrep cats --max 3 --format url

  # Get detailed JSON output for the first result
  gifgrep search --json "office handshake" | jq '.[0]'
  ```

### Downloading GIFs

Use the `--download` flag to save GIFs. They will be saved to the `/home/ubuntu/Downloads/` directory.

```bash
# Download the first GIF for the query "thumbs up"
gifgrep "thumbs up" --download --max 1
```

### Extracting Images

`gifgrep` can extract single frames (stills) or create a grid of frames (sheets).

- **Extract a Still Frame:** Get a single PNG frame from a GIF file, optionally at a specific timestamp.
  ```bash
  # Extract a frame from 1.5 seconds into the GIF
  gifgrep still ./path/to/your.gif --at 1.5s -o still.png
  ```

- **Create a Sprite Sheet:** Generate a single PNG grid of frames sampled from the GIF. This is useful for previews.
  ```bash
  # Create a sheet with 9 frames in 3 columns
  gifgrep sheet ./path/to/your.gif --frames 9 --cols 3 -o sheet.png
  ```
