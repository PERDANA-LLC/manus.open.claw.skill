---
name: oc-nano-banana-pro
description: Generate or edit images using Gemini Pro. Use this skill for single or multi-image composition and editing.
---

# Nano Banana Pro (Gemini Pro Image)

This skill allows you to generate and edit images using the Gemini Pro image model. It is a direct interface to the model's capabilities, providing a straightforward way to create and modify visual content.

## When to Use

- When you need to generate a new image from a textual description.
- When you want to edit an existing image with specific instructions.
- When you need to combine multiple images into a single composite scene.

## When NOT to Use

- Do not use this skill for creating complex slide-based presentations. For that, use the `slides` tool with the `image` generation mode, which is specifically designed for creating visually stunning, image-based slides.

## Usage

The core functionality is provided by the `generate_image.py` script. The necessary environment, including API keys, is already configured in the Manus sandbox.

### Generate a New Image

To generate a new image, execute the following command. You can specify the prompt, the output filename, and the desired resolution.

```bash
python3.11 /home/ubuntu/skills/nano-banana-pro/scripts/generate_image.py --prompt "A futuristic cityscape at sunset" --filename "cityscape.png" --resolution 1K
```

### Edit an Existing Image

To edit an existing image, provide the path to the input image along with your editing instructions.

```bash
python3.11 /home/ubuntu/skills/nano-banana-pro/scripts/generate_image.py --prompt "Change the color of the car to red" --filename "red_car.png" -i "/path/to/original_car.png" --resolution 2K
```

### Multi-Image Composition

You can combine up to 14 images into a single scene. Provide the paths to all input images.

```bash
python3.11 /home/ubuntu/skills/nano-banana-pro/scripts/generate_image.py --prompt "Create a collage of these animals in a forest setting" --filename "forest_collage.png" -i cat.png -i dog.png -i bird.png
```

## Parameters

- `--prompt`: A textual description of the image to generate or the edits to perform.
- `--filename`: The name of the output image file.
- `-i` or `--input_image`: Path to one or more input images for editing or composition.
- `--resolution`: The resolution of the output image. Supported values are `1K` (default), `2K`, and `4K`.
