---
name: oc-trello
description: >
  Manage Trello boards, lists, and cards using the Trello REST API. Use this
  skill to integrate Trello operations into workflows, such as creating tasks,
  moving cards between lists, or retrieving board information.
---

# Trello Skill

This skill allows for interaction with the Trello API to manage boards, lists, and cards. It requires a Trello API key and a token for authentication.

## When to Use

- When you need to create, read, update, or delete Trello cards, lists, or boards.
- For automating project management tasks that involve Trello.
- When a user asks to interact with their Trello account.

## Setup

To use this skill, you must first configure your Trello API credentials. This involves obtaining an API key and a server-to-server token.

1.  **Get your API Key**: You can obtain your API key by logging into Trello and visiting the following URL: [https://trello.com/app-key](https://trello.com/app-key)
2.  **Generate a Token**: On the same page, click the link under "Token" to manually generate a token.
3.  **Set Environment Variables**: Set the following environment variables in the shell. For security, avoid hardcoding them in scripts.

    ```shell
    export TRELLO_API_KEY="your-api-key"
    export TRELLO_TOKEN="your-token"
    ```

4. **Install jq**: The following commands use `jq` to parse the JSON responses. You can install it with:

    ```shell
    sudo apt-get update && sudo apt-get install -y jq
    ```

## Usage

All commands use `curl` to interact with the Trello REST API. The API key and token are passed as query parameters.

### List Boards

Retrieve all boards associated with the account.

```shell
curl -s "https://api.trello.com/1/members/me/boards?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" | jq '.[] | {name, id}'
```

### List Lists in a Board

Retrieve all lists within a specified board. Replace `{boardId}` with the actual ID of the board.

```shell
curl -s "https://api.trello.com/1/boards/{boardId}/lists?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" | jq '.[] | {name, id}'
```

### List Cards in a List

Retrieve all cards within a specified list. Replace `{listId}` with the actual ID of the list.

```shell
curl -s "https://api.trello.com/1/lists/{listId}/cards?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" | jq '.[] | {name, id, desc}'
```

### Create a Card

Create a new card in a specified list. Replace `{listId}` with the target list's ID.

```shell
curl -s -X POST "https://api.trello.com/1/cards?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" \
  --data "idList={listId}" \
  --data "name=Card Title" \
  --data "desc=Card description"
```

### Move a Card to Another List

Move an existing card to a different list. Replace `{cardId}` and `{newListId}`.

```shell
curl -s -X PUT "https://api.trello.com/1/cards/{cardId}?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" \
  --data "idList={newListId}"
```

### Add a Comment to a Card

Add a comment to a specific card. Replace `{cardId}` with the card's ID.

```shell
curl -s -X POST "https://api.trello.com/1/cards/{cardId}/actions/comments?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" \
  --data "text=Your comment here"
```

### Archive a Card

Archive (close) a card. Replace `{cardId}` with the card's ID.

```shell
curl -s -X PUT "https://api.trello.com/1/cards/{cardId}?key=$TRELLO_API_KEY&token=$TRELLO_TOKEN" \
  --data "closed=true"
```
