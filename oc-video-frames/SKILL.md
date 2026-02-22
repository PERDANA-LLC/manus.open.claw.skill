---
name: oc-video-frames
description: Extract frames or short clips from videos using ffmpeg. Use this skill when you need to extract a single frame from a video, or create quick thumbnails for inspection.
---

# Video Frames (ffmpeg)

This skill allows you to extract a single frame from a video file using `ffmpeg`.

## When to Use

Use this skill when you need to:

- Extract a single frame from a video at a specific timestamp.
- Create a quick thumbnail from a video file.

## Installation

First, ensure `ffmpeg` is installed. If not, you can install it using `apt-get`:

```shell
sudo apt-get update && sudo apt-get install -y ffmpeg
```

## Usage

### Extracting the First Frame

To extract the very first frame of a video:

```shell
ffmpeg -i /path/to/video.mp4 -vf "select=eq(n\,0)" -q:v 3 /path/to/output.jpg
```

### Extracting a Frame at a Specific Timestamp

To extract a frame at a specific time (e.g., 10 seconds in):

```shell
ffmpeg -i /path/to/video.mp4 -ss 00:00:10 -vframes 1 /path/to/output.jpg
```

## Notes

- Prefer using the `--ss` (seek) option for extracting frames around a specific time.
- Use a `.jpg` extension for quick sharing and smaller file sizes.
- Use a `.png` extension for higher quality and crisp UI frames.
