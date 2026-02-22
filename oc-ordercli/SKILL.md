---
name: oc-ordercli
description: A command-line tool for checking past Foodora orders and tracking active order status. Use this skill to interact with the Foodora service for order management directly from the shell.
---

# ordercli

This skill provides instructions for using the `ordercli` command-line tool to manage Foodora orders.

## When to Use

Use this skill when you need to programmatically check the status of a Foodora order, view order history, or reorder a previous meal.

## Installation

The `ordercli` tool is not pre-installed. First, install Go, then install the tool.

```bash
sudo apt-get update && sudo apt-get install -y golang
go install github.com/steipete/ordercli/cmd/ordercli@latest
```

This will install the `ordercli` binary to `~/go/bin/`. You may need to use the full path `/home/ubuntu/go/bin/ordercli` to execute it.

## Initial Setup & Authentication

Foodora is protected by Cloudflare, which can make direct login difficult for an automated agent. The most reliable method is to use the browser to log in first and then import the session cookies into `ordercli`.

1.  **Use the browser tool** to navigate to `https://www.foodora.com` and perform a manual login.
2.  **Import the session** into `ordercli`. Replace `"Default"` with the appropriate Chrome profile name if needed.

    ```bash
    /home/ubuntu/go/bin/ordercli foodora session chrome --url https://www.foodora.at/ --profile "Default"
    ```

3.  **Set your country code**. Find your country code first, then set it.

    ```bash
    /home/ubuntu/go/bin/ordercli foodora countries
    /home/ubuntu/go/bin/ordercli foodora config set --country <YourCountryCode>
    ```

## Usage Examples

Once configured, you can use the following commands to manage your orders.

### Check Orders

-   **List active orders** (shows status and estimated arrival):

    ```bash
    /home/ubuntu/go/bin/ordercli foodora orders
    ```

-   **Get details for a specific active order**:

    ```bash
    /home/ubuntu/go/bin/ordercli foodora order <orderCode>
    ```

-   **View order history**:

    ```bash
    /home/ubuntu/go/bin/ordercli foodora history --limit 10
    ```

-   **Get full JSON details for a past order**:

    ```bash
    /home/ubuntu/go/bin/ordercli foodora history show <orderCode> --json
    ```

### Reordering

This feature adds items from a past order to your current cart. Always confirm the action.

-   **Add items from a past order to your cart**:

    ```bash
    /home/ubuntu/go/bin/ordercli foodora reorder <orderCode> --confirm
    ```
