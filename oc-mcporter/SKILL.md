---
name: oc-mcporter
description: Interact with Model Context Protocol (MCP) servers using the `manus-mcp-cli` utility. Use this skill to list available tools on a configured server and to call those tools with specified arguments. This is the primary method for interacting with external services like Stripe or Google Calendar via MCP.
---

# MCPorter

This skill provides instructions for using the `manus-mcp-cli` utility to interact with Model Context Protocol (MCP) servers directly from the shell.

## When to Use

- When you need to interact with an external service that has a configured MCP server (e.g., `stripe`, `gmail`, `google-calendar`).
- To discover the available tools and their parameters for a specific MCP server.
- To execute a specific tool on an MCP server with JSON-formatted arguments.

## Core Commands

The primary interface is the `manus-mcp-cli` command, which is pre-installed and authenticated in the environment.

### List Tools

To see the available tools for a given server, use the `tool list` command. You must specify the server name.

```shell
manus-mcp-cli tool list --server <server_name>
```

**Example:**

```shell
manus-mcp-cli tool list --server stripe
```

### Call Tools

To execute a tool, use the `tool call` command. You must provide the tool name, the server name, and the arguments as a JSON string via the `--input` flag.

```shell
manus-mcp-cli tool call <tool_name> --server <server_name> --input '<json_arguments>'
```

**Example:**

```shell
# Call the 'create_customer' tool on the 'stripe' server
manus-mcp-cli tool call create_customer --server stripe --input '{"email": "customer@example.com", "name": "Jane Doe"}'
```

### Important Notes

- Tool arguments **MUST** be provided as a valid JSON string to the `--input` flag.
- The `--server` flag is mandatory for both listing and calling tools.
- Authentication (like OAuth) is handled automatically by the `manus-mcp-cli` wrapper when you first interact with a server.
