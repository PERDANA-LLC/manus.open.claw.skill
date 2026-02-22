---
name: oc-summarize
description: Summarizes text from various sources like URLs, local files, and YouTube videos. Use this skill to get a quick overview of an article, a document, or to extract a transcript from a video.
---

# Summarize Skill

This skill uses the `summarize` CLI tool to summarize content from URLs, local files, and YouTube links. It can also be used to extract video transcripts.

## When to Use

Use this skill when you need to perform any of the following actions:

- Get a quick summary of a web page or article.
- Summarize the content of a local text, Markdown, or PDF file.
- Get a summary or a transcript of a YouTube video.

Trigger phrases:
- "summarize this URL/article"
- "what’s this link/video about?"
- "transcribe this YouTube video"

## Installation

Before the first use, the `summarize` tool must be installed. Run the following command to download and install the pre-compiled binary for Linux.

```shell
SUMMARIZE_VERSION="1.1.0" # Check for the latest version on GitHub
ARCH="amd64"
OS="linux"

wget "https://github.com/steipete/summarize/releases/download/v${SUMMARIZE_VERSION}/summarize_${SUMMARIZE_VERSION}_${OS}_${ARCH}.tar.gz" -O /tmp/summarize.tar.gz

sudo tar -xzf /tmp/summarize.tar.gz -C /usr/local/bin/ summarize

rm /tmp/summarize.tar.gz
```

## Usage

The `summarize` tool requires an API key for a supported LLM provider. The Manus environment has `OPENAI_API_KEY` pre-configured, which can be used with OpenAI models.

### Basic Examples

- **Summarize a URL:**
  ```shell
  summarize "https://example.com" --model openai/gpt-4.1-mini
  ```

- **Summarize a local file:**
  ```shell
  summarize "/home/ubuntu/document.pdf" --model openai/gpt-4.1-mini
  ```

- **Summarize a YouTube video:**
  ```shell
  summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto
  ```

### Extracting YouTube Transcripts

To get a best-effort transcript from a YouTube video, use the `--extract-only` flag.

```shell
smarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto --extract-only
```

If a transcript is very long, provide a summary first and ask the user if they want to see the full text or a specific section.

### Useful Flags

- `--length <size>`: Control the summary length (`short`, `medium`, `long`, `xl`, or character count).
- `--json`: Output the result in JSON format for machine readability.
- `--extract-only`: For URLs, extract the main content without summarizing.
