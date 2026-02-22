---
name: oc-songsee
description: Generate spectrograms and feature-panel visualizations from audio with the songsee CLI. Use this skill to analyze audio files by creating spectrograms, mel spectrograms, chromagrams, and other visual representations from audio files like WAV or MP3.
---

# Songsee Skill

This skill provides the capability to generate various visual representations from audio files using the `songsee` command-line tool.

## When to Use

Use this skill when you need to perform audio analysis and visualization tasks, such as:
- Generating a spectrogram from an audio file (e.g., `track.mp3`).
- Creating a multi-panel visualization with different feature maps (e.g., spectrogram, mel, chroma, MFCC).
- Analyzing a specific time slice of an audio track.

## Installation

The `songsee` tool is not pre-installed. To use it, you must first install it by running the following shell commands:

1.  **Install Go:** `songsee` is a Go program, so you need to install Go first.
    ```bash
    sudo apt-get update && sudo apt-get install -y golang-go
    ```
2.  **Install songsee:** Use `go install` to download and build the tool.
    ```bash
    go install github.com/steipete/songsee@latest
    ```
3.  **Verify Installation:** The binary will be installed in `$HOME/go/bin`. You can call it using the full path.
    ```bash
    $HOME/go/bin/songsee --version
    ```

## Usage

Once installed, you can use `songsee` via the `shell` tool. It is recommended to use the full path `$HOME/go/bin/songsee` to avoid path issues.

### Quick Start Examples

-   **Generate a simple spectrogram:**
    ```bash
    $HOME/go/bin/songsee audio.mp3 -o spectrogram.jpg
    ```

-   **Create a multi-panel visualization:**
    ```bash
    $HOME/go/bin/songsee audio.mp3 --viz spectrogram,mel,chroma,hpss,selfsim,loudness,tempogram,mfcc,flux -o features.jpg
    ```

-   **Analyze a specific time slice:**
    ```bash
    $HOME/go/bin/songsee audio.mp3 --start 10.0 --duration 5.0 -o slice.png
    ```

-   **Process audio from stdin:**
    ```bash
    cat audio.mp3 | $HOME/go/bin/songsee - --format png -o from_stdin.png
    ```

### Common Flags

-   `--viz <list>`: A single visualization or a comma-separated list of visualizations to render. Can be repeated.
    -   *Available visualizations*: `spectrogram`, `mel`, `chroma`, `hpss`, `selfsim`, `loudness`, `tempogram`, `mfcc`, `flux`.
-   `--style <palette>`: Color palette for the visualization. 
    -   *Options*: `classic`, `magma`, `inferno`, `viridis`, `gray`.
-   `--width <pixels>` / `--height <pixels>`: Set the output image dimensions.
-   `--window <size>` / `--hop <size>`: Adjust FFT settings for analysis.
-   `--min-freq <hz>` / `--max-freq <hz>`: Set the frequency range for the analysis.
-   `--start <seconds>` / `--duration <seconds>`: Define a specific time segment to analyze.
-   `--format <type>`: Output image format (`jpg` or `png`).
-   `-o <path>`: Specify the output file path.

### Notes

-   `songsee` can natively decode WAV and MP3 files. For other formats, `ffmpeg` must be installed (`sudo apt-get install -y ffmpeg`).
-   When multiple `--viz` flags are used, the tool generates a grid of visualizations in a single image.
