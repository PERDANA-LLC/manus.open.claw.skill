---
name: oc-model-usage-analysis
description: Analyzes and summarizes AI model cost and usage data from provider dashboards like OpenAI and Anthropic. Use when asked about spending, costs, or usage metrics for specific AI models.
---

# Model Usage Analysis

## Overview

This skill provides a structured workflow for retrieving, analyzing, and reporting on AI model usage and cost data directly from provider dashboards. Since direct CLI access to billing data (like the original OpenClaw skill's `codexbar` dependency) is not available or reliable in this environment, this skill guides the agent to use its browser to access the necessary information manually.

## When to Use

- When the user asks about their spending on AI models, such as "How much have I spent on GPT-4 this month?"
- When the user requests a breakdown of usage for different models, like "What has my Claude Sonnet vs. Opus usage been?"
- When you need to answer any question related to AI model cost, token counts, or usage trends.

## When NOT to Use

- Do not use this skill for real-time, programmatic cost tracking. It is designed for on-demand reporting by accessing web dashboards.
- Do not use if the user has provided a specific API or tool for cost analysis.

## Workflow

### 1. Identify the Provider and Dashboard

First, determine which AI provider the user is asking about (e.g., OpenAI, Anthropic, Google, etc.). Then, navigate to the appropriate usage dashboard.

- **OpenAI:** `https://platform.openai.com/usage`
- **Anthropic:** `https://console.anthropic.com/settings/usage`

Use the browser tool to visit the relevant URL. The browser should maintain your login state.

### 2. Extract Usage Data

Once on the dashboard page, the usage data is typically presented in a table or a series of charts. Use the browser's inspection or reading capabilities to extract the relevant data. Focus on:

- **Model Name:** The specific model being reported (e.g., `gpt-4-turbo`, `claude-3-opus-20240229`).
- **Usage Metrics:** Tokens (prompt, completion), requests, or other relevant units.
- **Cost:** The cost associated with the usage.
- **Timeframe:** Ensure you are looking at the correct date range (e.g., current billing cycle, last 30 days).

### 3. Summarize and Report

After extracting the data, synthesize it into a clear and concise summary for the user. If the user asks for a specific piece of information (e.g., the cost of a single model), provide that directly. If the request is more general, you can provide a summary table.

**Example Summary:**

> Based on your OpenAI usage report for the current billing cycle, here is a breakdown of your spending:
> - **gpt-4-turbo:** $45.67
> - **gpt-3.5-turbo:** $12.34
> - **Total:** $58.01
