---
name: oc-openai-whisper
description: Provides the ability to transcribe audio files locally using the OpenAI Whisper CLI. Use this skill when you need to convert speech from an audio file into text without relying on an API.
---

# OpenAI Whisper (CLI)

This skill allows for local, high-quality speech-to-text transcription using OpenAI's Whisper models.

## When to Use

- When you need to transcribe an audio file (e.g., `.mp3`, `.wav`, `.m4a`) into text.
- When you need to translate a foreign language audio file into English text.
- When you prefer to run transcription locally for privacy or offline access.

## Installation

The `whisper` command-line tool is not installed by default. To use it, you must first install it using `pip`:

```shell
pip3 install -U openai-whisper
```

## Usage

The primary command is `whisper`, which takes the path to an audio file as input.

### Basic Transcription

To transcribe an audio file into a text file:

```shell
whisper /path/to/audio.mp3 --model medium --output_format txt --output_dir .
```

This will create an `audio.txt` file in the current directory.

### Translation

To translate an audio file into English and output subtitles:

```shell
whisper /path/to/audio.m4a --task translate --output_format srt
```

## Important Notes

- **Model Downloads**: The first time you run `whisper` with a specific model, it will be downloaded and cached in `~/.cache/whisper`.
- **Model Selection**: You can choose different models using the `--model` flag (e.g., `tiny`, `base`, `small`, `medium`, `large`). Smaller models are faster but less accurate; larger models are more accurate but slower.
- **Output Formats**: Various output formats are available, including `txt`, `vtt`, `srt`, `tsv`, and `json`.
