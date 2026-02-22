---
name: oc-spotify-player
description: Use spotify_player to control Spotify playback and search from the terminal. This skill is for users who want to interact with Spotify from the command line.
---

# Spotify Player

This skill allows you to control Spotify from the terminal using the `spotify_player` command-line tool.

## When to Use

Use this skill when you want to:

- Search for tracks, albums, and artists on Spotify.
- Control Spotify playback (play, pause, next, previous).
- Connect to and manage Spotify devices.
- Like the currently playing track.

## Requirements

- A Spotify Premium account is required.
- `spotify_player` must be installed.

## Installation

1.  **Install dependencies:**

    ```shell
    sudo apt-get update && sudo apt-get install -y libssl-dev libasound2-dev libdbus-1-dev
    ```

2.  **Install Rust and Cargo:**

    ```shell
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source $HOME/.cargo/env
    ```

3.  **Install `spotify_player`:**

    ```shell
    cargo install spotify_player --locked
    ```

## Authentication

On the first run, you need to authenticate with your Spotify account:

```shell
spotify_player authenticate
```

This will open a browser window for you to log in to Spotify and grant permissions.

## Common Commands

-   **Search for a track:**

    ```shell
    spotify_player search "your query"
    ```

-   **Control playback:**

    ```shell
    spotify_player playback play
    spotify_player playback pause
    spotify_player playback next
    spotify_player playback previous
    ```

-   **Connect to a device:**

    ```shell
    spotify_player connect
    ```

-   **Like the current track:**

    ```shell
    spotify_player like
    ```

For a full list of commands and options, run `spotify_player --help`.
