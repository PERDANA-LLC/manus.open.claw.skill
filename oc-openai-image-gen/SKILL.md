---
name: oc-openai-image-gen
description: Generate images from text prompts using the OpenAI Images API (DALL-E 2, DALL-E 3, and next-gen GPT models). Use this skill for requests to create single or batch images, with control over model, size, quality, and style.
---

# OpenAI Image Generation

This skill provides a Python script to generate images from text prompts using various OpenAI models. It can create a batch of images from structured random prompts or a specific user-provided prompt and generates an HTML gallery for easy viewing.

## When to Use

- When the user asks to generate an image from a text description.
- For batch image generation requests.
- When the user specifies advanced parameters like image model (e.g., DALL-E 3), size, quality, or style (vivid/natural).

## Setup

The required Python script is located at `/home/ubuntu/skills/openai-image-gen/gen.py`. The `OPENAI_API_KEY` environment variable is required and is managed by the Manus environment.

## Usage

Execute the generation script from the shell. The script will create an output directory (e.g., `/home/ubuntu/tmp/openai-image-gen-XXXXXXXX`) containing the images, a `prompts.json` file, and an `index.html` gallery.

### Basic Generation

To generate a default set of images:

```bash
# The script path will need to be adjusted if the skill is installed elsewhere
python3 /home/ubuntu/skills/openai-image-gen/gen.py
```

After execution, use the `browser` tool to view the generated gallery:

```python
# The exact path will be in the output of the shell command
browser.browse(url="file:///home/ubuntu/tmp/openai-image-gen-20260222120000/index.html")
```

### Advanced Generation with Flags

You can customize the generation process using various flags.

**Specify a prompt and count:**
```bash
python3 /home/ubuntu/skills/openai-image-gen/gen.py --prompt "ultra-detailed studio photo of a lobster astronaut" --count 4
```

**Use DALL-E 3 with specific quality and size:**
```bash
python3 /home/ubuntu/skills/openai-image-gen/gen.py --model dall-e-3 --quality hd --size 1792x1024 --style vivid
```

**Use DALL-E 2:**
```bash
python3 /home/ubuntu/skills/openai-image-gen/gen.py --model dall-e-2 --size 512x512 --count 4
```

## Model-Specific Parameters

The script adapts to the capabilities of each model. Invalid parameter combinations will be ignored.

### Size
- **GPT image models** (`gpt-image-1`, `gpt-image-1.5`): `1024x1024`, `1536x1024`, `1024x1536`, or `auto` (default: `1024x1024`)
- **dall-e-3**: `1024x1024`, `1792x1024`, or `1024x1792` (default: `1024x1024`)
- **dall-e-2**: `256x256`, `512x512`, or `1024x1024` (default: `1024x1024`)

### Quality
- **GPT image models**: `auto`, `high`, `medium`, or `low` (default: `high`)
- **dall-e-3**: `hd` or `standard` (default: `standard`)
- **dall-e-2**: `standard` only

### Other Options
- **GPT image models** support `--background` (`transparent`, `opaque`) and `--output-format` (`png`, `jpeg`, `webp`).
- **dall-e-3** supports a `--style` parameter: `vivid` (hyper-real, dramatic) or `natural` (more natural looking).
- **dall-e-3** only supports generating 1 image at a time (`n=1`). The script automatically enforces this limit.
