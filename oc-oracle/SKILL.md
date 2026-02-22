---
name: oc-oracle
description: Best practices for using the oracle CLI for prompt and file bundling, including engines, sessions, and file attachment patterns. Use this skill when you need to interact with language models from the command line, providing them with context from your local files.
---

# Using the `oracle` CLI

The `oracle` command-line tool allows you to bundle a prompt with selected files into a single request for a language model to process. This is useful for providing the model with the context of a codebase or other project files.

## Installation

To install the `oracle` CLI, use the following command:

```bash
sudo npm install -g @steipete/oracle
```

## Key Concepts

*   **Engines**: `oracle` can use different "engines" to interact with language models. The two main engines are `api` and `browser`. The `api` engine uses the `OPENAI_API_KEY` environment variable to make API calls, while the `browser` engine automates a web browser to interact with a model's web interface.
*   **Sessions**: Long-running tasks are saved as sessions, which you can list and reattach to. This is particularly useful for browser-based interactions that may take a long time. Sessions are stored in `/home/ubuntu/.oracle/sessions`.
*   **File Attachments**: You can attach files, directories, and globs to your prompt to provide context to the model. `oracle` has built-in rules for ignoring common directories like `node_modules` and honors `.gitignore` files.

## Common Commands

*   **Help**: `oracle --help`
*   **Dry Run (Preview)**: `oracle --dry-run summary -p "<task>" --file "src/**"`
*   **Browser-based Run**: `oracle --engine browser --model gpt-5.2-pro -p "<task>" --file "src/**"`
*   **List Sessions**: `oracle status --hours 72`
*   **Attach to Session**: `oracle session <id> --render`

## When to Use

*   When you want to ask a language model a question about a codebase and provide it with the relevant files.
*   When you need to perform a long-running interaction with a language model and want to be able to detach and reattach to the session.
*   When you want to experiment with different models and engines from the command line.

## When NOT to Use

*   For simple, one-shot questions that don't require any file context. Use the model's web interface directly for these.
*   If you need to process a very large number of files, as this can result in a very large and expensive prompt.
