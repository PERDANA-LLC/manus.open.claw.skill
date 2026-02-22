---
name: oc-blogwatcher
description: Monitors blogs and RSS/Atom feeds for updates using the blogwatcher command-line tool. Use this skill to track new posts from specified blogs or feeds.
---

# Blog Watcher

This skill provides the capability to monitor blogs and RSS/Atom feeds for new content using the `blogwatcher` command-line interface.

## Installation

To use this skill, the `blogwatcher` tool must be installed. As it is a Go program, the Go compiler must be installed first.

1.  **Install Go:**

    ```bash
    sudo apt-get update && sudo apt-get install -y golang
    ```

2.  **Install blogwatcher:**

    ```bash
    go install github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest
    ```

    This will install the `blogwatcher` binary to the Go bin directory. You may need to add the Go bin directory to your `$PATH`.

## Core Commands

-   **Add a blog to monitor:**

    ```bash
    blogwatcher add "Blog Name" <URL>
    ```

-   **List all monitored blogs:**

    ```bash
    blogwatcher blogs
    ```

-   **Scan for new articles:**

    ```bash
    blogwatcher scan
    ```

-   **List new articles:**

    ```bash
    blogwatcher articles
    ```

-   **Mark an article as read:**

    ```bash
    blogwatcher read <ARTICLE_ID>
    ```

-   **Mark all articles as read:**

    ```bash
    blogwatcher read-all
    ```

-   **Remove a blog:**

    ```bash
    blogwatcher remove "Blog Name"
    ```

## When to Use

-   When you need to monitor a blog or RSS/Atom feed for new posts.
-   When you want to get a list of recent articles from a specific set of sources.

## When NOT to Use

-   For websites that do not provide an RSS or Atom feed. In such cases, a browser-based scraping approach might be necessary.
-   If you need to analyze the content of the articles in-depth. This tool is for notification of new articles, not for content extraction.
