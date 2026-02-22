---
name: oc-sherpa-onnx-tts
description: >
  Provides local, offline text-to-speech (TTS) capabilities using the sherpa-onnx engine.
  Use this skill when you need to convert text to speech without relying on cloud services,
  for privacy-sensitive tasks, or for generating audio files from text programmatically.
---

# Sherpa-ONNX Text-to-Speech

This skill enables high-quality, offline text-to-speech generation using the `sherpa-onnx` command-line tool. It operates entirely within the sandbox, ensuring privacy and avoiding reliance on external cloud services.

## When to Use

- When you need to generate speech from text for applications, content creation, or accessibility.
- When an internet connection is unavailable or unreliable.
- When processing sensitive or private text that should not be sent to a cloud TTS provider.

## Setup (One-time)

Before using the skill for the first time, you must download the `sherpa-onnx` runtime and a voice model. These steps only need to be performed once.

1.  **Create directories for the tools and models:**

    ```bash
    mkdir -p /home/ubuntu/tools/sherpa-onnx-tts/runtime /home/ubuntu/tools/sherpa-onnx-tts/models
    ```

2.  **Download and extract the sherpa-onnx runtime for Linux:**

    ```bash
    wget -qO- https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-linux-x64-shared.tar.bz2 | tar -xj --strip-components=1 -C /home/ubuntu/tools/sherpa-onnx-tts/runtime
    ```

3.  **Download and extract a voice model. The example below uses the high-quality `lessac` voice for US English:**

    ```bash
    wget -qO- https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-high.tar.bz2 | tar -xj -C /home/ubuntu/tools/sherpa-onnx-tts/models
    ```

## Usage

To generate a `.wav` audio file from a string of text, execute the following command. The command specifies the voice model, the output file path, and the text to synthesize.

```bash
# Define paths to the executable and model
SHERPA_EXE="/home/ubuntu/tools/sherpa-onnx-tts/runtime/bin/sherpa-onnx-tts"
MODEL_DIR="/home/ubuntu/tools/sherpa-onnx-tts/models/vits-piper-en_US-lessac-high"

# Run the TTS command
$SHERPA_EXE \
  --vits-model="$MODEL_DIR/en_US-lessac-high.onnx" \
  --vits-lexicon="$MODEL_DIR/lexicon.txt" \
  --vits-tokens="$MODEL_DIR/tokens.txt" \
  --output-filename="/home/ubuntu/output.wav" \
  "Hello from Manus. This is a local text-to-speech test."
```

After running the command, the generated audio will be saved to `/home/ubuntu/output.wav`.
