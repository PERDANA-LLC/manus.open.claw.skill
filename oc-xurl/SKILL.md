---
name: oc-xurl
description: A CLI tool for making authenticated requests to the X (Twitter) API. Use this skill when you need to post tweets, reply, quote, search, read posts, manage followers, send DMs, upload media, or interact with any X API v2 endpoint.
---

# xurl — Agent Skill Reference

`xurl` is a CLI tool for the X API. It supports both **shortcut commands** (agent-friendly one-liners) and **raw curl-style** access to any v2 endpoint. All commands return JSON to stdout.

## When to Use
Use this skill to interact with the X (formerly Twitter) API. This includes:
- Posting, replying to, or deleting tweets.
- Searching for tweets with specific keywords, hashtags, or from certain users.
- Fetching user profiles, timelines, followers, or mentions.
- Liking, reposting, or bookmarking tweets.
- Sending and listing Direct Messages.
- Uploading media to be attached to tweets.

## Installation

The `xurl` command-line tool is required. Install it using `npm` via the `shell` tool.

```shell
npm install -g @xdevplatform/xurl
```

## Prerequisites & Authentication

Before using any command, you must be authenticated. The user is expected to have configured credentials manually. To check authentication status, run:

```shell
xurl auth status
```

### Secret Safety (Mandatory)

- **NEVER** read, print, or expose the `~/.xurl` configuration file.
- **NEVER** ask the user to paste credentials or tokens.
- **NEVER** use flags that expose secrets in commands: `--bearer-token`, `--consumer-key`, `--consumer-secret`, `--access-token`, `--token-secret`, `--client-id`, `--client-secret`.
- **NEVER** use `--verbose` / `-v` as it can expose sensitive headers/tokens.

## Quick Reference

| Action | Command |
|---|---|
| Post | `xurl post "Hello world!"` |
| Reply | `xurl reply POST_ID "Nice post!"` |
| Quote | `xurl quote POST_ID "My take"` |
| Delete a post | `xurl delete POST_ID` |
| Read a post | `xurl read POST_ID` |
| Search posts | `xurl search "QUERY" -n 10` |
| Who am I | `xurl whoami` |
| Look up a user | `xurl user @handle` |
| Home timeline | `xurl timeline -n 20` |
| Mentions | `xurl mentions -n 10` |
| Like | `xurl like POST_ID` |
| Unlike | `xurl unlike POST_ID` |
| Repost | `xurl repost POST_ID` |
| Undo repost | `xurl unrepost POST_ID` |
| Follow | `xurl follow @handle` |
| Unfollow | `xurl unfollow @handle` |
| Send DM | `xurl dm @handle "message"` |
| Upload media | `xurl media upload path/to/file.jpg` |
| Media status | `xurl media status MEDIA_ID` |

> **Note:** `POST_ID` can be a numeric ID or a full post URL. The leading `@` on usernames is optional.

## Common Workflows

### Post with an image

```shell
# 1. Upload the image and get the media_id from the response
xurl media upload photo.jpg

# 2. Post with the media_id
xurl post "Check out this photo!" --media-id MEDIA_ID
```

### Search and Engage

```shell
# 1. Search for relevant posts
xurl search "topic of interest" -n 10

# 2. Like an interesting post from the results
xurl like POST_ID_FROM_RESULTS

# 3. Reply to it
xurl reply POST_ID_FROM_RESULTS "Great point!"
```

## Raw API Access

For any X API v2 endpoint not covered by a shortcut, use raw, curl-style requests.

```shell
# GET request (default)
xurl /2/users/me

# POST with JSON body
xurl -X POST /2/tweets -d '''{"text":"Hello from Manus!"}'''

# DELETE request
xurl -X DELETE /2/tweets/TWEET_ID
```
