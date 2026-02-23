---
name: local-seo-dominator
description: A 6-function meta-skill for local SEO competitive analysis. Use for keyword research, GBP analysis, competitor teardowns, schema audits, and content gap analysis using browser automation.
---

# Local SEO Dominator

This skill provides a suite of 6 powerful, browser-based functions for dominating local SEO by analyzing and outmaneuvering your competitors.

## The 6 Core Functions

When this skill is invoked, you MUST execute one of the following 6 functions based on the user's request. Each function leverages browser automation to gather live data.

1.  **Ahrefs Keyword Research**: Extracts top keywords, volume, and difficulty from a competitor's Ahrefs profile.
2.  **GBP Competitor Analysis**: Analyzes competitor Google Business Profile posts to build a data-driven posting plan.
3.  **Business & Competitor Teardown**: Extracts and compares services, locations, and strengths of your business vs. competitors.
4.  **GBP Content Gap Analysis**: Identifies keyword gaps in competitor GBP posts and generates high-impact posts for your business.
5.  **Full Schema Audit**: Audits a URL for all existing schema, identifies gaps, and generates missing JSON-LD.
6.  **Content Gap & Weakness Analysis**: Scans competitor sites to find content gaps and weaknesses, providing topics to cover.

## Execution Workflow

For any given local SEO task, you MUST follow this four-step execution process:

1.  **Identify the Core Function**: Determine which of the 6 core functions the user is requesting.
2.  **Gather Inputs**: Collect the necessary inputs from the user (e.g., competitor URLs, your website URL, target city).
3.  **Execute Browser Automation**: Use the browser tools (`browser_navigate`, `browser_scroll`, `browser_input`, etc.) to perform the analysis as described in the corresponding prompt template.
4.  **Deliver Actionable Output**: Provide the final output in the specified format (e.g., spreadsheet-ready data, JSON-LD schema, a list of content topics), ensuring it is ready to be implemented.

---

*This skill is a direct implementation of the 6 local SEO prompts. All detailed prompt templates are stored in the `references` directory.*
