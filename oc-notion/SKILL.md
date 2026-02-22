---
name: oc-notion
description: Use the Notion API to create and manage pages, databases, and blocks. This skill is for interacting with a Notion workspace programmatically when the user provides an API key.
---

# Notion API Skill

This skill provides instructions and command-line examples for interacting with the Notion API. It allows for the creation, retrieval, and management of pages, databases, and blocks within a Notion workspace.

## When to Use

- When the user wants to automate tasks in Notion, such as adding content, updating databases, or searching for information.
- When the user provides a Notion API key and asks to perform operations on their Notion data.
- For creating new pages, querying databases, or appending content to existing pages programmatically.

## When NOT to Use

- If the user has not provided a Notion API key. Do not solicit one; simply state that the capability is unavailable without it.
- For tasks that can be more easily accomplished through the Notion user interface, unless automation is specifically requested.

## Setup

To use this skill, a Notion API key is required. The user must provide this key. It should be stored in a secure file within the sandbox environment for the duration of the task.

1.  **Store the API Key**: When the user provides a key, save it to a file.

    ```shell
    mkdir -p /home/ubuntu/.config/notion
    echo "secret_YOUR_KEY_HERE" > /home/ubuntu/.config/notion/api_key
    ```

2.  **Share Access**: The user must ensure the Notion integration associated with the API key has been granted access to the specific pages or databases they want to interact with. This is done within the Notion UI via the "..." menu and selecting "Add connections".

## API Basics

All API requests must include an `Authorization` header with the API key and a `Notion-Version` header. This skill uses version `2022-06-28`.

```shell
NOTION_KEY=$(cat /home/ubuntu/.config/notion/api_key)
curl -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  --data '{"query": "My Page Title"}'
```

## Common Operations

Below are `curl` examples for common actions. Remember to replace placeholders like `{page_id}` and `{database_id}` with actual IDs.

### Search for Pages or Databases

```shell
curl -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  --data '{"query": "page or database title"}'
```

### Retrieve a Page

```shell
curl "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28"
```

### Retrieve Page Content (Blocks)

```shell
curl "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28"
```

### Create a Page in a Database

```shell
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  --data '{
    "parent": {"database_id": "YOUR_DATABASE_ID"},
    "properties": {
      "Name": {"title": [{"text": {"content": "New Item from API"}}]},
      "Status": {"select": {"name": "In Progress"}}
    }
  }'
```

### Query a Database

```shell
curl -X POST "https://api.notion.com/v1/databases/{database_id}/query" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  --data '{
    "filter": {"property": "Status", "select": {"equals": "Done"}}
  }'
```

### Add Blocks to a Page

```shell
curl -X PATCH "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  --data '{
    "children": [
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": [{"text": {"content": "This is a new paragraph added via the API."}}]}
      }
    ]
  }'
```
