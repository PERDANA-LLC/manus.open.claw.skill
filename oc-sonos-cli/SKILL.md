---
name: oc-sonos-cli
description: Control Sonos speakers on the local network. Use this skill to discover, get status, play, pause, control volume, and manage groups for Sonos devices.
---

# Sonos CLI Skill

This skill provides the capability to control Sonos speakers on the local network using the `sonoscli` tool.

## When to Use

Use this skill when you need to interact with Sonos speakers for tasks such as:
- Checking the status of a speaker.
- Playing, pausing, or stopping music.
- Adjusting the volume.
- Discovering all speakers on the network.
- Managing speaker groups.

## Installation

The `sonos` command-line tool is not pre-installed. To use this skill, you must first install Go and then the `sonoscli` package.

1.  **Install Go:**
    ```bash
    sudo apt-get update && sudo apt-get install -y golang-go
    ```

2.  **Install sonoscli:**
    ```bash
    go install github.com/steipete/sonoscli/cmd/sonos@latest
    ```

3.  **Update PATH:**
    The `sonos` binary will be installed in the Go binary path (e.g., `/home/ubuntu/go/bin`). Ensure this directory is in your `$PATH`.
    ```bash
    export PATH=$PATH:$(go env GOPATH)/bin
    ```

## Usage

All commands use the `sonos` executable. You can specify the target speaker by name (e.g., `--name "Kitchen"`) or IP address (e.g., `--ip 192.168.1.100`).

### Basic Commands

-   **Discover speakers:**
    ```bash
    sonos discover
    ```
-   **Get speaker status:**
    ```bash
    sonos status --name "Living Room"
    ```
-   **Control playback:**
    ```bash
    sonos play --name "Living Room"
    sonos pause --name "Living Room"
    ```
-   **Set volume:**
    ```bash
    sonos volume set 20 --name "Living Room"
    ```

### Advanced Commands

-   **Manage groups:**
    ```bash
    sonos group join --name "Kitchen" --master "Living Room"
    sonos group unjoin --name "Kitchen"
    ```
-   **Play favorites:**
    ```bash
    sonos favorites list
    sonos favorites open "My Playlist"
    ```

## Troubleshooting

### `sonos discover` - `no route to host`

If you encounter a `sendto: no route to host` error, it typically indicates a networking issue where the discovery packets (SSDP) are being blocked. This can be caused by:

-   A firewall on the host machine or network.
-   The sandboxed environment not having the correct network permissions or configuration to send multicast UDP packets.

Ensure the agent's execution environment has open access to the local network.

### `sonos discover` - `bind: operation not permitted`

This error suggests that the process does not have sufficient privileges to bind to the required network socket. This can happen if the agent is running in a highly restrictive sandbox that blocks network access. The environment must permit network operations for this skill to function.
