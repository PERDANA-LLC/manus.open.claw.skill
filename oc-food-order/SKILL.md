---
name: oc-food-order
description: Reorders previous food orders from Foodora and tracks their status using the `ordercli` command-line tool. Use this skill to quickly reorder a past meal or get updates on an active order's ETA.
---

# Food Ordering via Foodora

This skill uses the `ordercli` tool to interact with the Foodora food delivery service. It allows you to list past orders, reorder them, and track the status of active orders.

## When to Use

- When the user asks to "order food" and implies a reorder of something they've had before.
- When the user wants to "reorder my usual" or "get the same thing as last time" from Foodora.
- When the user asks for the "status" or "ETA" of their current Foodora order.

## When NOT to Use

- For placing a new, customized order for the first time. This skill only supports reordering.
- For services other than Foodora.

## 1. Setup

The `ordercli` tool is required. These steps only need to be performed once.

### Install `ordercli`

1.  **Install Go:**
    ```bash
    sudo apt-get update && sudo apt-get install -y golang-go
    ```

2.  **Install the tool:**
    ```bash
    go install github.com/steipete/ordercli/cmd/ordercli@latest
    ```

3.  **Add to PATH:** Ensure the `ordercli` binary is accessible.
    ```bash
    export PATH=$PATH:$(go env GOPATH)/bin
    ```

### Configure `ordercli`

1.  **Set Country:** Find your country code and set it.
    ```bash
    ~/go/bin/ordercli foodora countries
    # Example for Austria:
    ~/go/bin/ordercli foodora config set --country AT
    ```

2.  **Log In:** Authenticate with your Foodora account. The recommended method is to import the session from an authenticated Chrome browser to avoid storing passwords.
    ```bash
    ~/go/bin/ordercli foodora session chrome --url https://www.foodora.at/ --profile "Default"
    ```

## 2. Find an Order to Reorder

- List the 10 most recent orders to find the one you want to reorder.
  ```bash
  ~/go/bin/ordercli foodora history --limit 10
  ```
- Get the details of a specific order using its `orderCode`.
  ```bash
  ~/go/bin/ordercli foodora history show <orderCode>
  ```

## 3. Reorder

### Step 3.1: Preview the Reorder

First, generate a preview of the reorder. This does **not** place the order but shows you the items and price.

```bash
~/go/bin/ordercli foodora reorder <orderCode>
```

### Step 3.2: Confirm and Place the Order

**CRITICAL:** Before running the next command, you MUST get explicit confirmation from the user (e.g., "Yes, place the order").

- Once confirmed, run the command with the `--confirm` flag.
  ```bash
  ~/go/bin/ordercli foodora reorder <orderCode> --confirm
  ```
- If the user has multiple saved addresses, you must ask which one to use and provide the `--address-id`.
  ```bash
  ~/go/bin/ordercli foodora reorder <orderCode> --confirm --address-id <id>
  ```

## 4. Track the Order

- Get the ETA and status of all active orders.
  ```bash
  ~/go/bin/ordercli foodora orders
  ```
- Watch an order for live updates.
  ```bash
  ~/go/bin/ordercli foodora orders --watch
  ```
- Get details for a single active order.
  ```bash
  ~/go/bin/ordercli foodora order <orderCode>
  ```
