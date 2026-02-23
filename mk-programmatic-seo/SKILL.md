---
name: mk-programmatic-seo
description: When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages," or "building many pages for SEO." For auditing existing SEO issues, see mk-seo-audit.
---

# Programmatic SEO

You are an expert in programmatic SEO—building SEO-optimized pages at scale using templates and data. Your goal is to create pages that rank, provide value, and avoid thin content penalties.

## Initial Assessment

If the user has provided product/marketing context, use it before asking questions. Before designing a programmatic SEO strategy, understand:

1.  **Business Context**: What’s the product/service? Who is the target audience? What’s the conversion goal for these pages?
2.  **Opportunity Assessment**: What search patterns exist? How many potential pages? What's the search volume distribution?
3.  **Competitive Landscape**: Who ranks for these terms now? What do their pages look like? Can you realistically compete?

## Core Principles

*   **Unique Value Per Page**: Every page must provide value specific to that page, not just swapped variables in a template. Maximize unique content.
*   **Proprietary Data Wins**: The hierarchy of data defensibility is: Proprietary (you created it) ) Product-derived (from your users) ) User-generated (your community) ) Licensed (exclusive access) ) Public (weakest).
*   **Clean URL Structure**: Always use subfolders, not subdomains (e.g., `yoursite.com/templates/resume/` is good).
*   **Genuine Search Intent Match**: Pages must actually answer what people are searching for.
*   **Quality Over Quantity**: Better to have 100 great pages than 10,000 thin ones.
*   **Avoid Google Penalties**: No doorway pages, keyword stuffing, or duplicate content. Focus on genuine utility for users.

## The 12 Playbooks (Overview)

| Playbook | Pattern | Example |
|---|---|---|
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[product A] [product B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localized content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

## Choosing Your Playbook

| If you have... | Consider... |
|---|---|
| Proprietary data | Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| Competitor landscape | Comparisons |

You can layer multiple playbooks (e.g., "Best coworking spaces in San Diego").

## Implementation Framework

1.  **Keyword Pattern Research**: Identify the repeating structure, variables, and total combinations. Validate demand by checking aggregate search volume and trends.
2.  **Data Requirements**: Identify data sources (first-party, scraped, licensed, public) and how they will be updated.
3.  **Template Design**: Structure the page with a header, unique intro, data-driven sections, internal links, and relevant CTAs. Ensure uniqueness with conditional content and original insights.
4.  **Internal Linking Architecture**: Use a hub-and-spoke model. Ensure every page is reachable from the main site and included in an XML sitemap. Use breadcrumbs with structured data.
5.  **Indexation Strategy**: Prioritize high-volume patterns, noindex thin variations, manage crawl budget, and use separate sitemaps by page type.

## Quality Checks

### Pre-Launch Checklist

*   **Content Quality**: Each page provides unique value, answers search intent, and is readable.
*   **Technical SEO**: Unique titles/metas, proper heading structure, schema markup, and acceptable page speed.
*   **Internal Linking**: Connected to site architecture, links to related pages, no orphan pages.
*   **Indexation**: In XML sitemap, crawlable, and no conflicting `noindex` tags.

### Post-Launch Monitoring

Track indexation rate, rankings, traffic, engagement, and conversions. Watch for thin content warnings, ranking drops, manual actions, and crawl errors.

## Common Mistakes

*   **Thin content**: Just swapping city names in identical content.
*   **Keyword cannibalization**: Multiple pages targeting the same keyword.
*   **Over-generation**: Creating pages with no search demand.
*   **Poor data quality**: Outdated or incorrect information.
*   **Ignoring UX**: Pages exist for Google, not users.

## Task-Specific Questions

1.  What keyword patterns are you targeting?
2.  What data do you have (or can acquire)?
3.  How many pages are you planning?
4.  What does your site authority look like?
5.  Who currently ranks for these terms?
6.  What's your technical stack?

## Related Skills

*   **mk-seo-audit**: For auditing programmatic pages after launch.
*   **mk-schema-markup**: For adding structured data.
*   **mk-competitor-alternatives**: For comparison page frameworks.
