---
name: oc-openai-whisper-api
description: Transcribes audio files using the OpenAI Whisper API. Use this skill when you need to convert speech from an audio file into text.
---

# OpenAI Whisper API Transcription

This skill provides instructions for transcribing audio files using the OpenAI Whisper API directly through `curl`.

## When to Use

Use this skill when you have an audio file (e.g., MP3, WAV, M4A) and need to get a text transcription of the speech it contains.

## Prerequisites

Ensure the `OPENAI_API_KEY` environment variable is set. This is pre-configured in the Manus environment, so no action is typically needed.

## Usage

To transcribe an audio file, use the following `shell` command. Replace `/path/to/your/audio.mp3` with the actual path to your audio file.

```bash
curl https://api.openai.com/v1/audio/transcriptions \\
  -H "Authorization: Bearer $OPENAI_API_KEY" \\
  -F file="@/path/to/your/audio.mp3" \\
  -F model="whisper-1"
```

The transcription result will be printed to standard output in JSON format.

### Saving Output to a File

To save the transcription to a text file, you can parse the JSON response. For example, using `jq`:

```bash
# First, ensure jq is installed if not present
# sudo apt-get update && sudo apt-get install -y jq

# Run the command and pipe the output to jq to extract the text
curl https://api.openai.com/v1/audio/transcriptions \\
  -H "Authorization: Bearer $OPENAI_API_KEY" \\
  -F file="@/path/to/your/audio.mp3" \\
  -F model="whisper-1" | jq -r '.text' > /home/ubuntu/transcription.txt
```

### Additional Parameters

You can add more parameters to the request by adding more `-F` fields to the `curl` command. For example, to specify the language:

```bash
curl https://api.openai.com/v1/audio/transcriptions \\
  -H "Authorization: Bearer $OPENAI_API_KEY" \\
  -F file="@/path/to/your/audio.mp3" \\
  -F model="whisper-1" \\
  -F language="en"
```

Refer to the [OpenAI API documentation](https://platform.openai.com/docs/api-reference/audio/createTranscription) for a full list of available parameters.
