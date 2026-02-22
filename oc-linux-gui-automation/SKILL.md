---
name: oc-linux-gui-automation
description: Automate graphical user interface (GUI) interactions on Linux using command-line tools like xdotool. Use for scripting repetitive UI tasks, controlling windows, and simulating user input when no other API is available.
---

# Linux GUI Automation

This skill provides instructions for automating user interface interactions on the Linux desktop. The primary tool for this is `xdotool`, a powerful command-line utility that can simulate keyboard input and mouse activity, and manage windows.

This is useful for scripting repetitive tasks, testing graphical applications, or controlling applications that do not provide a convenient command-line or API-based method of control.

## When to Use

- When you need to automate interactions with a graphical application that has no API.
- For scripting a sequence of clicks, keystrokes, and window management actions.
- To automate user input for testing or repetitive data entry.

## When NOT to Use

- When an application provides a dedicated API or CLI. Using the official API is always more reliable.
- For web automation. Use browser automation tools instead.
- When tasks can be accomplished through backend shell commands or file manipulation, which are more stable than GUI scripting.

## Setup

Before using `xdotool`, you must install it. It is available in the default Ubuntu repositories.

```shell
sudo apt-get update && sudo apt-get install -y xdotool
```

## Core `xdotool` Commands

`xdotool` allows you to chain multiple commands together in a single line.

### Mouse Control

- **Move the mouse:**
  ```shell
  xdotool mousemove 100 200
  ```

- **Click the left mouse button (button 1):**
  ```shell
  xdotool click 1
  ```

- **Move and click:**
  ```shell
  xdotool mousemove 100 200 click 1
  ```

- **Right-click (button 3):**
  ```shell
  xdotool click 3
  ```

### Keyboard Control

- **Type text:**
  ```shell
  xdotool type 'Hello, world!'
  ```

- **Press a key (like Enter or Tab):**
  ```shell
  xdotool key Return
  xdotool key Tab
  ```

- **Simulate key combinations (e.g., Ctrl+C):**
  ```shell
  xdotool key ctrl+c
  ```

### Window Management

`xdotool` can find and act on specific windows. You can search for windows by title, class, or process ID (PID).

- **Find a window by title and activate it:**
  ```shell
  xdotool search --name "Mozilla Firefox" windowactivate
  ```

- **Move a window to the top-left corner:**
  ```shell
  xdotool search --class "Gedit" windowmove 0 0
  ```

- **Get the ID of the currently active window:**
  ```shell
  xdotool getactivewindow
  ```

- **Type into a specific window without focusing it first:**
  ```shell
  xdotool type --window $(xdotool search --name "Untitled Document") "Typing in the background"
  ```

## Practical Examples

### Example 1: Automate Text Editor

This script opens `gedit`, types some text, and saves the file using keyboard shortcuts.

```shell
# Open gedit in the background
gedit &
# Wait for the window to appear
sleep 2

# Find the gedit window, activate it, type, and save
xdotool search --class "Gedit" windowactivate --sync \
  type 'This is an automated test.' \
  key ctrl+s

# Wait for the save dialog
sleep 1

# Type the filename and press Enter to save
xdotool type 'my-test-file.txt' key Return
```

### Example 2: Close a Specific Application

This script finds all windows belonging to the "Firefox" application and closes them gracefully.

```shell
# Get a list of all window IDs for Firefox
WINDOW_IDS=$(xdotool search --class "Firefox")

# Loop through each window and send the close command
for id in $WINDOW_IDS; do
  xdotool windowclose $id
done
```
