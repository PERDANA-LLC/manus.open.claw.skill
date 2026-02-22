---
name: oc-goplaces
description: Query Google Places API (New) via the goplaces CLI for text search, place details, resolve, and reviews. Use for human-friendly place lookup or JSON output for scripts.
---

# goplaces

Modern Google Places API (New) CLI. Human output by default, `--json` for scripts.

## When to Use

Use this skill when you need to find information about places, such as restaurants, shops, or other points of interest. It can be used for both interactive queries and for scripting.

## Installation

This skill requires the `goplaces` CLI to be installed. You can install it with the following command:

```shell
sudo apt-get update && sudo apt-get install -y golang
go install github.com/steipete/goplaces/cmd/goplaces@latest
```

## Configuration

This skill requires a Google Places API key. You need to set the `GOOGLE_PLACES_API_KEY` environment variable to your API key.

```shell
export GOOGLE_PLACES_API_KEY="..."
```

## Common Commands

- Search for coffee shops that are open now, with a minimum rating of 4, and limit the results to 5:
  ```shell
  goplaces search "coffee" --open-now --min-rating 4 --limit 5
  ```
- Search for pizza restaurants within a 3km radius of a specific location:
  ```shell
  goplaces search "pizza" --lat 40.8 --lng -73.9 --radius-m 3000
  ```
- Get the details of a place, including reviews:
  ```shell
  goplaces details <place_id> --reviews
  ```
- Search for sushi restaurants and get the output in JSON format:
  ```shell
  goplaces search "sushi" --json
  ```
