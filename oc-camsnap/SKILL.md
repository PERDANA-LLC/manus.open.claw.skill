---
name: oc-camsnap
description: Capture frames or clips from RTSP/ONVIF cameras. Use this skill when you need to interact with network-connected cameras to get snapshots or video clips.
---

# Camsnap Skill

This skill allows you to interact with RTSP/ONVIF cameras to capture snapshots and video clips using the `camsnap` command-line tool.

## When to Use

Use this skill when you need to programmatically capture images or video from a security camera or any other camera that supports the RTSP or ONVIF protocols.

## Installation

First, ensure that `ffmpeg` is installed, as `camsnap` depends on it:

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```

Next, download and install the `camsnap` Debian package:

```bash
wget https://github.com/steipete/camsnap/releases/download/v0.0.8/camsnap_0.0.8_linux_amd64.deb
sudo dpkg -i camsnap_0.0.8_linux_amd64.deb
```

## Configuration

The configuration file for `camsnap` is located at `/home/ubuntu/.config/camsnap/config.yaml`. You can add a camera using the following command, which will create the configuration file if it doesn't exist:

```bash
camsnap add --name my-camera --host <camera-ip-address> --user <username> --pass <password>
```

## Usage

Here are some common `camsnap` commands:

- **Discover cameras on your network:**
  ```bash
  camsnap discover --info
  ```

- **Take a snapshot from a configured camera:**
  ```bash
  camsnap snap my-camera --out snapshot.jpg
  ```

- **Record a 5-second video clip:**
  ```bash
  camsnap clip my-camera --dur 5s --out clip.mp4
  ```

- **Check the status of your camera configuration:**
  ```bash
  camsnap doctor --probe
  ```
