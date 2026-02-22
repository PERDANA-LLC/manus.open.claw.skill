---
name: oc-gemini
description: Interact with Google Gemini large language models for one-shot Q&A, summaries, and text generation. Use this skill to leverage Gemini's capabilities within a Python environment.
---

# Google Gemini

This skill provides instructions for interacting with Google Gemini models using the pre-configured `openai` Python library in the Manus sandbox environment.

## When to Use

- When you need to perform one-shot question answering.
- When you need to summarize a piece of text.
- When you need to generate creative or technical text based on a prompt.
- When you need to interact with a powerful large language model for any text-based task.

## When NOT to Use

- Do not use this skill if you need to maintain a long-running conversational state. It is designed for single-turn, one-shot interactions.
- Do not use this for tasks that require a graphical user interface or web browser.

## How to Use

The sandbox is pre-configured with the necessary API keys (`OPENAI_API_KEY`) and endpoint settings to use Gemini models through an OpenAI-compatible API.

You can use the `openai` Python library to interact with the available Gemini models (`gemini-2.5-flash`, `gpt-4.1-mini`, `gpt-4.1-nano`).

### Example: One-shot Q&A

1.  Save the following Python code to a file (e.g., `ask_gemini.py`):

    ```python
    from openai import OpenAI

    client = OpenAI()

    completion = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    print(completion.choices[0].message.content)
    ```

2.  Execute the script from the shell:

    ```bash
    python3.11 ask_gemini.py
    ```

### Example: Summarizing Text

1.  Save the following Python code to a file (e.g., `summarize_text.py`):

    ```python
    from openai import OpenAI

    client = OpenAI()

    text_to_summarize = """
    The Industrial Revolution was the transition to new manufacturing processes in Europe
    and the United States, in the period from about 1760 to sometime between 1820 and 1840.
    This transition included going from hand production methods to machines, new chemical
    manufacturing and iron production processes, the increasing use of steam power and water
    power, the development of machine tools and the rise of the mechanized factory system.
    """

    completion = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Please summarize the following text in one sentence: {text_to_summarize}"}
        ]
    )

    print(completion.choices[0].message.content)
    ```

2.  Execute the script from the shell:

    ```bash
    python3.11 summarize_text.py
    ```
