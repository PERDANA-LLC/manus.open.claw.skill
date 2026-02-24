---
name: advanced-seo-suite
description: A comprehensive 19-function SEO and GEO toolkit covering keyword research, competitor analysis, content optimization, schema markup, technical SEO, rank tracking, and AI citation optimization. Adapted from seo-geo-claude-skills.
---

# Advanced SEO Suite

A comprehensive SEO and GEO (Generative Engine Optimization) toolkit adapted from the `seo-geo-claude-skills` repository by Aaron He Zhu. This skill consolidates 20+ individual SEO skills into a single, powerful meta-skill for Manus, covering the full lifecycle of search engine optimization: Research, Build, Optimize, and Monitor.

## When to Use This Skill

Activate this skill when the user mentions any of the following: "SEO audit", "keyword research", "SERP analysis", "content optimization", "schema markup", "meta tags", "internal linking", "backlink analysis", "rank tracking", "GEO optimization", "AI citations", "content gaps", "competitor SEO", "technical SEO", "Core Web Vitals", "E-E-A-T", "domain authority", or "SEO report".

## Workflow

### Phase 1: Research (Understand the Landscape)

Before creating or optimizing content, research the competitive landscape.

**Function 1: Keyword Research.** Discover high-value keywords with search intent analysis, difficulty assessment, and content opportunity mapping. Reference: `references/keyword-intent-taxonomy.md`, `references/topic-cluster-templates.md`.

**Function 2: Competitor Analysis.** Analyze competitor SEO and GEO strategies including ranking keywords, content approaches, backlink profiles, and AI citation patterns. Reference: `references/battlecard-template.md`, `references/positioning-frameworks.md`.

**Function 3: Content Gap Analysis.** Identify content opportunities by finding topics and keywords competitors cover that you do not. Reference: `references/gap-analysis-frameworks.md`.

**Function 4: SERP Analysis.** Analyze search engine results pages to understand ranking factors, SERP features, user intent patterns, and AI overview triggers. Reference: `references/serp-feature-taxonomy.md`.

### Phase 2: Build (Create Optimized Content)

Create new content that is optimized for both traditional search engines and AI answer engines.

**Function 5: SEO Content Writing.** Write comprehensive, search-optimized content with proper heading hierarchy, keyword placement, internal linking suggestions, and readability optimization. Reference: `references/content-structure-templates.md`, `references/title-formulas.md`.

**Function 6: GEO Content Optimization.** Optimize content specifically for AI answer engines (ChatGPT, Perplexity, Google AI Overviews) by structuring content for citation, adding quotable statements, and implementing entity-rich formatting. Reference: `references/ai-citation-patterns.md`, `references/quotable-content-examples.md`.

**Function 7: Meta Tags Optimization.** Craft compelling title tags, meta descriptions, Open Graph tags, and Twitter cards that maximize click-through rates. Reference: `references/meta-tag-formulas.md`.

**Function 8: Schema Markup Generation.** Generate valid JSON-LD structured data for any content type (Article, FAQ, HowTo, Product, LocalBusiness, Organization, etc.). Reference: `references/schema-templates.md`, `references/validation-guide.md`.

### Phase 3: Optimize (Improve Existing Content)

Audit and improve existing pages and site architecture.

**Function 9: On-Page SEO Audit.** Score any page against 50+ on-page SEO factors including title tags, headings, content quality, keyword usage, images, and internal links. Reference: `references/scoring-rubric.md`.

**Function 10: Technical SEO Check.** Audit technical SEO factors including page speed, Core Web Vitals, mobile-friendliness, crawlability, indexing, robots.txt, and sitemap configuration. Reference: `references/http-status-codes.md`, `references/robots-txt-reference.md`.

**Function 11: Internal Linking Optimization.** Analyze and optimize internal link structure to improve page authority distribution, content silos, and site navigation. Reference: `references/link-architecture-patterns.md`.

**Function 12: Content Refreshing.** Identify and refresh declining content by detecting content decay signals and recommending specific updates. Reference: `references/content-decay-signals.md`.

### Phase 4: Monitor (Track and Report)

Set up ongoing monitoring and reporting for SEO performance.

**Function 13: Rank Tracking.** Track keyword rankings over time, detect position changes, and identify ranking trends. Reference: `references/tracking-setup-guide.md`.

**Function 14: Backlink Analysis.** Analyze backlink profiles, assess link quality, identify toxic links, and find link building opportunities. Reference: `references/link-quality-rubric.md`, `references/outreach-templates.md`.

**Function 15: Performance Reporting.** Generate comprehensive SEO performance reports with KPI tracking, trend analysis, and actionable recommendations. Reference: `references/kpi-definitions.md`, `references/report-templates.md`.

**Function 16: Alert Management.** Set up automated alerts for ranking changes, traffic drops, competitor movements, and technical issues. Reference: `references/alert-threshold-guide.md`.

### Cross-Cutting Functions

These functions apply across all phases.

**Function 17: Content Quality Audit (CORE-EEAT).** Score content against the 80-item CORE-EEAT benchmark covering Credibility, Originality, Readability, and Experience-Expertise-Authoritativeness-Trustworthiness. Reference: `references/core-eeat-benchmark.md`.

**Function 18: Domain Authority Audit (CITE).** Score domain authority using the 40-item CITE framework covering Credibility, Infrastructure, Trust, and Expertise. Reference: `references/cite-domain-rating.md`.

**Function 19: Entity Optimization.** Optimize for knowledge graph inclusion, entity disambiguation, and knowledge panel triggers. Reference: `references/entity-signal-checklist.md`, `references/knowledge-graph-guide.md`.

## Example Prompts

| Function | Example Prompt |
|---|---|
| Keyword Research | *"Do keyword research for a SaaS project management tool targeting small businesses"* |
| Competitor Analysis | *"Analyze the SEO strategy of competitor.com vs my site mysite.com"* |
| Content Gap Analysis | *"Find content gaps between my site and these 3 competitors"* |
| SERP Analysis | *"Analyze the SERP for 'best project management software' and tell me what it takes to rank"* |
| SEO Content Writing | *"Write an SEO-optimized article targeting 'remote team management tips'"* |
| GEO Content Optimization | *"Optimize this article to get cited by ChatGPT and Perplexity"* |
| Meta Tags | *"Write optimized title tags and meta descriptions for these 10 pages"* |
| Schema Markup | *"Generate FAQ and Article schema markup for my blog post"* |
| On-Page Audit | *"Run a full on-page SEO audit of mysite.com/pricing"* |
| Technical SEO | *"Check the technical SEO health of mysite.com"* |
| Internal Linking | *"Analyze and optimize the internal linking structure of my blog"* |
| Content Refresh | *"Which of my blog posts are declining and need a refresh?"* |
| Rank Tracking | *"Set up rank tracking for my top 20 keywords"* |
| Backlink Analysis | *"Analyze my backlink profile and find link building opportunities"* |
| Performance Report | *"Generate a monthly SEO performance report for my site"* |
| Alerts | *"Set up alerts for ranking drops on my top 10 keywords"* |
| CORE-EEAT Audit | *"Score this article against the CORE-EEAT benchmark"* |
| CITE Domain Audit | *"Run a CITE domain authority audit on mysite.com"* |
| Entity Optimization | *"How can I optimize my brand entity for the knowledge graph?"* |

## References

All 28 reference files are stored in the `references/` directory. They contain over 12,000 lines of expert SEO knowledge including scoring rubrics, templates, taxonomies, and best practices. When executing any function above, read the relevant reference files first.
