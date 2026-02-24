---
name: mk-ai-seo
description: "When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generative engine optimization,' 'LLM optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' or 'zero-click search.' This skill covers content optimization for AI answer engines, monitoring AI visibility, and getting cited as a source. For traditional technical and on-page SEO audits, see mk-seo-audit. For structured data implementation, see mk-schema-markup."
version: 2.0.0
author: zubair-trabzada, adapted by Manus
tags: [ai-seo, geo, llmo, aeo, generative-engine-optimization, answer-engine-optimization, ai-citations, ai-visibility]
---

# AI SEO & Generative Engine Optimization (GEO) Suite v2.0

This skill provides a comprehensive, executable toolkit for optimizing a website's visibility and citability within large language models (LLMs) and AI-powered answer engines. It has been upgraded with the full capabilities of the `geo-seo-claude` repository, transforming it from a knowledge base into a powerful auditing and implementation tool.

## Core Capabilities

This skill now operates through a series of specialized Python scripts and can run a full, automated GEO audit.

| # | Function | Description |
|---|---|---|
| 1 | **Full GEO Audit** | Runs all 11 sub-modules to generate a comprehensive GEO readiness score and a client-ready PDF report. |
| 2 | **AI Citability Scoring** | Analyzes content passages for their likelihood of being cited by an LLM using `citability_scorer.py`. |
| 3 | **AI Crawler Analysis** | Checks `robots.txt` for access rules for 14+ AI crawlers (GPTBot, ClaudeBot, etc.). |
| 4 | **Brand Mention Scanning** | Scans 7+ platforms (YouTube, Reddit, Wikipedia) for brand mentions using `brand_scanner.py`. |
| 5 | **Platform-Specific Optimization** | Provides tailored recommendations for ChatGPT, Perplexity, and Google AI Overviews. |
| 6 | **`llms.txt` Generation** | Creates and validates the emerging `llms.txt` standard file for AI crawler guidance using `llmstxt_generator.py`. |
| 7 | **GEO-Optimized Content Briefs** | Generates content briefs focused on creating citable, fact-rich answer blocks. |
| 8 | **GEO Schema Audit & Generation** | Audits and generates `Schema.org` structured data optimized for entity recognition by AI. |
| 9 | **GEO Technical Audit** | Audits technical SEO foundations critical for AI crawlers, such as server-side rendering. |
| 10 | **Client-Ready Reporting (MD)** | Generates a professional, client-facing GEO report in Markdown. |
| 11 | **Client-Ready Reporting (PDF)** | Generates a polished PDF report with charts and visualizations using `generate_pdf_report.py`. |

## How to Use

### Running a Full Audit

To perform a comprehensive GEO audit, use the following prompt:

> "Run a full GEO audit on `https://example.com`. I need a complete analysis of its AI search readiness, including citability, brand authority, content quality, technical foundations, and structured data. Provide a composite GEO Score and a prioritized action plan in a client-ready PDF report."

This will trigger a multi-step process that uses the Python scripts included in this skill:
1.  **Discovery**: Fetches the homepage using `fetch_page.py`, detects business type, and crawls the sitemap.
2.  **Parallel Analysis**: Launches 5 sub-agents to analyze AI Visibility (using `citability_scorer.py`, `brand_scanner.py`), Platform Optimization, Technical SEO, Content Quality, and Schema Markup.
3.  **Synthesis**: Aggregates scores and generates a composite GEO Score (0-100).
4.  **Report Generation**: Outputs a professional PDF report using `generate_pdf_report.py` with findings and recommendations.

### Running Individual Functions

You can also invoke specific functions:

-   **Citability Scoring**: *"Score the AI citability of this article: `[URL]` using the citability_scorer.py script."*
-   **AI Crawler Check**: *"Does `https://example.com/robots.txt` block GPTBot or PerplexityBot?"*
-   **`llms.txt` Generation**: *"Generate an `llms.txt` file for my website, `https://example.com`, using the llmstxt_generator.py script."*
-   **Schema Generation**: *"Generate `LocalBusiness` schema for my company based on the information on this page: `[URL]`"*

## Resources

This skill includes a rich set of executable resources:

-   **Python Scripts**: Located in `scripts/`, these tools perform the core analysis (e.g., `citability_scorer.py`, `brand_scanner.py`, `generate_pdf_report.py`).
-   **Schema Templates**: Located in `schema/`, these JSON-LD templates cover common entity types (`Organization`, `LocalBusiness`, `Product`, etc.).
-   **Reference Prompts**: The original agent and skill prompts from `geo-seo-claude` are stored in `references/` for advanced use cases.
