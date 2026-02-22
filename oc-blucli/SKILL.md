---
name: oc-blucli
description: Control Bluesound/NAD audio players using the blu command-line tool. Use this skill for tasks involving device discovery, playback control (play, pause, stop), volume adjustment, and speaker grouping.
---

# BluOS CLI (blu)

This skill allows you to control Bluesound and NAD audio players that support the BluOS platform. It uses the `blu` command-line interface to interact with devices on your local network.

## When to Use

Use this skill when you need to automate control of Bluesound or NAD speakers. This includes:

- Playing, pausing, or stopping audio playback.
- Adjusting the volume.
- Grouping multiple speakers together.
- Discovering available devices on the network.
- Playing radio stations from TuneIn.

## Installation

The `blu` command-line tool is not installed by default. You must first install Go, and then install `blucli`.

To install Go and `blucli`, run the following commands:

```shell
sudo apt-get update && sudo apt-get install -y golang
go install github.com/steipete/blucli/cmd/blu@latest
```

This will install the `blu` binary to `~/go/bin`. You may need to add this directory to your `$PATH` to run the command directly.

```shell
export PATH=$PATH:$(go env GOPATH)/bin
```

## Usage

Once installed, you can use the `blu` command to control your devices.

### Device Discovery and Selection

First, discover the available devices on your network:

```shell
blu devices
```

This will list all players, their IDs, and names. To control a specific device, you can use the `--device` flag with its ID, name, or a previously set alias.

```shell
blu --device <id|name|alias> status
```

You can also set the `BLU_DEVICE` environment variable to avoid specifying the device for every command.

### Playback Control

-   **Check Status:** `blu status`
-   **Play:** `blu play`
-   **Pause:** `blu pause`
-   **Stop:** `blu stop`
-   **Set Volume:** `blu volume set 15`

### Grouping

You can group speakers to play audio in sync.

-   **Check Group Status:** `blu group status`
-   **Add a player to a group:** `blu group add <player_to_add>`
-   **Remove a player from a group:** `blu group remove <player_to_remove>`

### TuneIn Radio

You can search for and play TuneIn radio stations.

-   **Search:** `blu tunein search "NPR"`
-   **Play:** `blu tunein play "NPR"`

For scripting, it is recommended to use the `--json` flag to get structured output. Always confirm the target device before making changes to playback.
