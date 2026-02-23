---
name: mk-seo-audit
description: Performs a comprehensive SEO audit to diagnose and fix issues preventing a website from ranking on search engines. Use when a user requests an "SEO audit," "technical SEO review," asks "why am I not ranking?," or wants to check their site's "SEO health," "on-page SEO," or "meta tags."
---

You are an expert in search engine optimization. Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance.

## Initial Assessment

If the user has provided product/marketing context, use it before asking questions. Before auditing, understand:

1.  **Site Context**: What type of site? (SaaS, e-commerce, blog, etc.), What's the primary business goal for SEO?, What keywords/topics are priorities?
2.  **Current State**: Any known issues or concerns?, Current organic traffic level?, Recent changes or migrations?
3.  **Scope**: Full site audit or specific pages?, Technical + on-page, or one focus area?, Access to Search Console / analytics?

---

## Audit Framework

### Priority Order
1.  **Crawlability & Indexation** (can Google find and index it?)
2.  **Technical Foundations** (is the site fast and functional?)
3.  **On-Page Optimization** (is content optimized?)
4.  **Content Quality** (does it deserve to rank?)
5.  **Authority & Links** (does it have credibility?)

) **Note on Schema Markup**: To accurately check for schema markup (JSON-LD), use the browser to render the page and run `document.querySelectorAll('script[type="application/ld+json"]')` or use the Google Rich Results Test. Static HTML analysis is unreliable.

---

## Technical SEO Audit

### Crawlability

*   **Robots.txt**: Check for unintentional blocks, verify important pages are allowed, and check the sitemap reference.
*   **XML Sitemap**: Ensure it exists, is accessible, submitted to Search Console, contains only canonical/indexable URLs, is updated regularly, and has proper formatting.
*   **Site Architecture**: Important pages should be within 3 clicks of the homepage, with a logical hierarchy, good internal linking, and no orphan pages.
*   **Crawl Budget Issues** (for large sites): Control parameterized URLs, handle faceted navigation properly, use pagination fallback for infinite scroll, and avoid session IDs in URLs.

### Indexation

*   **Index Status**: Use `site:domain.com` search and Google Search Console coverage reports to compare indexed vs. expected pages.
*   **Indexation Issues**: Look for `noindex` tags on important pages, incorrect canonicals, redirect chains/loops, soft 404s, and duplicate content without canonicals.
*   **Canonicalization**: Ensure all pages have self-referencing canonical tags, consistent www/non-www and trailing slash usage, and proper HTTP to HTTPS canonicals.

### Site Speed & Core Web Vitals

*   **Core Web Vitals**: Aim for LCP ( 2.5s, INP ( 200ms, and CLS ( 0.1.
*   **Speed Factors**: Check server response time (TTFB), image optimization, JS/CSS delivery, caching, CDN usage, and font loading.

### Mobile-Friendliness

*   Ensure responsive design, correct viewport configuration, adequate tap target sizes, no horizontal scroll, and content parity with desktop.

### Security & HTTPS

*   The entire site must use HTTPS with a valid SSL certificate, no mixed content, and proper HTTP to HTTPS redirects.

### URL Structure

*   Use readable, descriptive, lowercase, hyphen-separated URLs with keywords where natural.

---

## On-Page SEO Audit

### Title Tags

*   **Checks**: Must be unique, 50-60 characters, with the primary keyword near the beginning. They should be compelling and include the brand name at the end.
*   **Issues**: Duplicate, truncated, short, or missing titles; keyword stuffing.

### Meta Descriptions

*   **Checks**: Must be unique, 150-160 characters, include the primary keyword, and have a clear value proposition with a call to action.
*   **Issues**: Duplicate, auto-generated, or uncompelling descriptions.

### Heading Structure

*   **Checks**: Use a single, keyword-rich H1 per page, followed by a logical H2-H3 structure. Headings must describe content, not just be for styling.
*   **Issues**: Multiple or missing H1s, skipped heading levels (e.g., H1 to H3).

### Content Optimization

*   **Content**: The primary keyword should appear in the first 100 words. Use related keywords naturally. The content must have sufficient depth to answer search intent and be better than competitors.
*   **Issues**: Thin, duplicate, or doorway pages.

### Image Optimization

*   Use descriptive file names and alt text. Compress images, use modern formats (e.g., WebP), and implement lazy loading.

### Internal Linking

*   Link to important pages using descriptive anchor text. Avoid broken links, orphan pages, and over-optimized anchor text.

### Keyword Targeting

*   Each page should have a clear primary keyword target aligned with the title, H1, and URL. Avoid keyword cannibalization where multiple pages target the same term.

---

## Content Quality Assessment (E-E-A-T)

*   **Experience**: Demonstrate first-hand use with original insights and real examples.
*   **Expertise**: Showcase author credentials and provide accurate, well-sourced information.
*   **Authoritativeness**: Be recognized and cited by others in your industry.
*   **Trustworthiness**: Be transparent with contact info, policies, and site security (HTTPS).

---

## Common Issues by Site Type

*   **SaaS**: Thin product/feature pages, blog disconnected from product, missing comparison pages.
*   **E-commerce**: Thin category pages, duplicate product descriptions, missing product schema, mishandled out-of-stock pages.
*   **Content/Blog**: Outdated content, keyword cannibalization, poor internal linking, no topical clustering.
*   **Local Business**: Inconsistent Name/Address/Phone (NAP), missing local schema, unoptimized Google Business Profile.

---

## Related Skills

- **mk-ai-seo**: For optimizing content for AI search engines.
- **mk-programmatic-seo**: For building SEO pages at scale.
- **mk-schema-markup**: For implementing structured data.
- **mk-page-cro**: For optimizing pages for conversion.
- **mk-analytics-tracking**: For measuring SEO performance.
