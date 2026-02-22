---
name: oc-sag
description: Use the `sag` command-line tool for ElevenLabs text-to-speech (TTS) with a user experience similar to the macOS `say` command. This skill is ideal for generating voice responses, creating audio clips from text, and integrating high-quality TTS into workflows.
---

# sag

Use `sag` for ElevenLabs TTS with local playback.

## Installation

1.  **Download the binary:**

    ```shell
    wget https://github.com/steipete/sag/releases/download/v0.2.2/sag_0.2.2_linux_amd64.tar.gz
    ```

2.  **Extract and install:**

    ```shell
    tar -xvf sag_0.2.2_linux_amd64.tar.gz
    sudo mv sag /usr/local/bin/
    ```

## API Key

An ElevenLabs API key is required. Set it as an environment variable:

```shell
export ELEVENLABS_API_KEY="your_api_key_here"
```

## When to Use

- When you need to generate speech from text using ElevenLabs.
- For creating voice responses in a chat or assistant context.
- To convert text files or scripts into spoken audio.

## When NOT to Use

- If you need to use a different TTS provider, as this skill is specific to ElevenLabs.
- For complex SSML requirements not supported by the `sag` tool.

## Quick Start

-   `sag "Hello there"`
-   `sag speak -v "Roger" "Hello"`
-   `sag voices`
-   `sag prompting` (model-specific tips)

## Model Notes

-   Default: `eleven_v3` (expressive)
-   Stable: `eleven_multilingual_v2`
-   Fast: `eleven_flash_v2_5`

## Pronunciation + Delivery Rules

-   First fix: respell (e.g. "key-note"), add hyphens, adjust casing.
-   Numbers/units/URLs: `--normalize auto` (or `off` if it harms names).
-   Language bias: `--lang en|de|fr|...` to guide normalization.
-   v3: SSML `<break>` not supported; use `[pause]`, `[short pause]`, `[long pause]`.
-   v2/v2.5: SSML `<break time="1.5s" />` supported; `<phoneme>` not exposed in `sag`.

## v3 Audio Tags (put at the entrance of a line)

-   `[whispers]`, `[shouts]`, `[sings]`
-   `[laughs]`, `[starts laughing]`, `[sighs]`, `[exhales]`
-   `[sarcastic]`, `[curious]`, `[excited]`, `[crying]`, `[mischievously]`
-   Example: `sag "[whispers] keep this quiet. [short pause] ok?"`

## Voice Defaults

-   `ELEVENLABS_VOICE_ID` or `SAG_VOICE_ID`

Confirm voice + speaker before long output.

## Chat Voice Responses

When asked for a "voice" reply (e.g., "crazy scientist voice", "explain in voice"), generate an audio file and provide the path.

```shell
# Generate audio file
sag -v Clawd -o /home/ubuntu/voice-reply.mp3 "Your message here"
```

Then, you can provide the path to the user: `/home/ubuntu/voice-reply.mp3`

### Voice Character Tips:

-   Crazy scientist: Use `[excited]` tags, dramatic pauses `[short pause]`, vary intensity
-   Calm: Use `[whispers]` or slower pacing
-   Dramatic: Use `[sings]` or `[shouts]` sparingly

Default voice for Clawd: `lj2rcrvANS3gaWWnczSX` (or just `-v Clawd`)
