---
name: real-estate-lead-gen
description: Automated real estate lead generation pipeline that discovers, qualifies, and delivers seller leads to agents. Use when users want to find motivated sellers (FSBO, expired listings, price reductions, pre-foreclosures), score leads with AI, prospect for agent customers, set up Stripe monetization, or schedule recurring lead delivery via Gmail. Supports any US metro area.
---

# Real Estate Lead Generation Pipeline

Automated pipeline that discovers motivated seller leads, qualifies them with AI scoring, prospects for agent customers, monetizes via Stripe, and delivers results via Gmail on a recurring schedule.

## Overview

The pipeline has 6 stages executed in order:

1. **Configure** — Set target market, ICP, and scoring rubric
2. **Monetize** — Create Stripe products, pricing tiers, and payment links
3. **Discover** — Scan listing sites for motivated seller leads
4. **Qualify** — Score leads in parallel using weighted rubric
5. **Prospect** — Research and qualify target agent customers
6. **Automate** — Schedule recurring discovery and delivery

Determine which stages to run based on user request. For first-time setup, run all 6. For recurring execution, run stages 3-4 only.

## Stage 1: Configure

Create a working directory and configuration files.

```bash
mkdir -p ~/lead_gen_pipeline
```

Read the ICP template: `references/icp_template.md`. Customize for the user's target metro area by replacing placeholders (`{METRO}`, `{BOROUGH_LIST}`, `{NEIGHBORHOOD_LIST}`).

Save customized ICP to `~/lead_gen_pipeline/icp.md`.

Read the email templates: `references/email_templates.md`. Customize company name and metro area. Save to `~/lead_gen_pipeline/email_templates.md`.

**Scoring Rubric (always use these weights):**

| Factor | Weight | 10 = Best | 1 = Worst |
|--------|--------|-----------|----------|
| Motivation | 30% | Must sell (foreclosure, estate, divorce) | Just curious |
| Timeline | 25% | Within 30 days | No timeline |
| Property Value | 20% | $2M+ | Under $200K |
| Engagement | 15% | Responded / open house | No signals |
| Competition | 10% | No agent (FSBO) | Exclusive listing |

**Final Score** = (Motivation × 0.3) + (Timeline × 0.25) + (Value × 0.2) + (Engagement × 0.15) + (Competition × 0.1)

**Tiers:** HOT (8-10), WARM (5-7.9), NURTURE (1-4.9)

## Stage 2: Monetize

Use the Stripe MCP server to create products and pricing. Run these commands in order:

```
1. create_product: name="Real Estate Lead Intelligence — {METRO}"
2. create_price: Starter $149/mo recurring monthly
3. create_price: Starter $1,490/yr recurring yearly
4. create_price: Professional $299/mo recurring monthly
5. create_price: Professional $2,990/yr recurring yearly
6. create_price: Enterprise $599/mo recurring monthly
7. create_price: Enterprise $5,990/yr recurring yearly
8. create_payment_link: for each monthly price
9. create_coupon: name="FIRSTMONTH50", percent_off=50, duration="once"
```

Save all IDs and links to `~/lead_gen_pipeline/stripe_config.md`.

**Tier features:**

| Tier | Boroughs | Frequency | Leads/week |
|------|----------|-----------|------------|
| Starter $149/mo | 1 | Weekly digest | ~20 |
| Professional $299/mo | 3 | Daily + weekly | ~50 |
| Enterprise $599/mo | All | Real-time + daily + weekly | Unlimited |

## Stage 3: Discover

Scan multiple sources for each lead category. Adapt source URLs to the target metro.

**Category 1 — Price Reductions:** Browse the metro's primary listing site (StreetEasy for NYC, Redfin/Zillow for others) filtered by price drops > 5% in the last 14 days. Collect: address, neighborhood, type, price, drop amount, beds/baths/sqft, brokerage.

**Category 2 — FSBO:** Browse Zillow FSBO section filtered to the target metro. Collect: address, borough, price, beds/baths/sqft, notes.

**Category 3 — Expired/Long DOM:** Search for listings with 90+ days on market or recently expired. Collect: address, neighborhood, type, price, DOM, brokerage.

**Category 4 — Pre-Foreclosure:** Search for lis pendens, NOD filings, or pre-foreclosure listings in the metro. Collect: address, borough, estimated value, filing type.

Save all raw leads to `~/lead_gen_pipeline/daily_leads_raw.md` with date header and tables per category.

**Target: 20-50 raw leads per scan.**

## Stage 4: Qualify

Use the `map` tool to qualify all discovered leads in parallel.

**Prompt template for each lead:**

```
You are a real estate lead qualification specialist for the {METRO} market.

Lead to Qualify: {{input}}

Score using this weighted rubric (1-10 each):
- Motivation (30%): 10=must sell, 5=considering, 1=curious
- Timeline (25%): 10=30 days, 7=90 days, 4=6 months, 1=none
- Property Value (20%): 10=$2M+, 8=$1M-2M, 5=$500K-1M, 3=under $500K
- Engagement (15%): 10=responded, 7=open house, 5=active, 3=none
- Competition (10%): 10=no agent (FSBO), 7=expired, 3=has agent

Tasks:
1. Search online for the property to verify details
2. Research comparable recent sales in the neighborhood
3. Assess seller motivation from available signals
4. Calculate weighted final score (1-10)
5. Write a personalized 3-4 sentence outreach script
6. Classify: HOT (8-10), WARM (5-7.9), NURTURE (1-4.9)
```

**Output schema for map tool:**

| Field | Type | Description |
|-------|------|-------------|
| address | string | Full property address |
| lead_type | string | Price Reduction / FSBO / Expired / Pre-Foreclosure |
| estimated_value | string | Dollar amount |
| motivation_score | number | 1-10 |
| timeline_score | number | 1-10 |
| value_score | number | 1-10 |
| engagement_score | number | 1-10 |
| competition_score | number | 1-10 |
| final_score | number | 1.0-10.0 |
| tier | string | HOT / WARM / NURTURE |
| outreach_script | string | 3-4 sentence personalized script |
| key_signals | string | Comma-separated signals |

Save qualified leads sorted by score to `~/lead_gen_pipeline/daily_leads_qualified.md`.

## Stage 5: Prospect

Use the `map` tool to research target agents in parallel.

Identify 10 top-producing agents in the metro by searching for "top real estate agents {METRO} {YEAR}" and collecting names, brokerages, and specialties.

**Prompt template for each agent:**

```
Research this real estate agent as a potential customer for an automated
lead generation service that delivers AI-qualified seller leads daily.

Agent: {{input}}

Find: website, email, market focus, estimated annual volume, buying signals
(active marketing, growing team, high volume, awards, thought leadership).

Score purchase likelihood (1-10).
Write a 3-4 sentence outreach email referencing their specific achievements
and offering a free sample report. Service pricing: Starter $149/mo,
Professional $299/mo, Enterprise $599/mo.
```

**Output schema for map tool:**

| Field | Type | Description |
|-------|------|-------------|
| agent_name | string | Full name |
| brokerage | string | Company name |
| market_focus | string | Borough/neighborhoods |
| annual_volume | string | Dollar amount or Unknown |
| website | string | URL or Not found |
| email | string | Email or Not found |
| buying_signals | string | Comma-separated signals |
| purchase_likelihood | number | 1-10 |
| outreach_draft | string | Personalized email body |

Save to `~/lead_gen_pipeline/agent_prospects.md`.

## Stage 6: Automate

Schedule recurring tasks using the `schedule` tool.

**Daily lead scan (weekdays 7 AM):**

```
cron: "0 0 7 * * 1-5"
name: "Daily {METRO} Lead Discovery"
prompt: [Run stages 3-4 using files in ~/lead_gen_pipeline/]
```

The scheduled prompt should instruct Manus to:
1. Read ICP from `~/lead_gen_pipeline/icp.md`
2. Read email templates from `~/lead_gen_pipeline/email_templates.md`
3. Execute Stage 3 (Discover) for all categories
4. Execute Stage 4 (Qualify) using map tool
5. For HOT leads (8+), send alert via Gmail MCP using Template 1
6. Log activity to `~/lead_gen_pipeline/delivery_log.md`

## Sending Emails

Use the Gmail MCP server (`manus-mcp-cli tool call send_email --server gmail`) to deliver leads.

**HOT lead alert:** Send immediately when a lead scores 8+. Use Template 1 from email templates.

**Weekly digest:** Compile all qualified leads from the week into a summary table. Use Template 2 from email templates.

**Agent outreach:** Send personalized prospecting emails to agent prospects. Use Template 3 from email templates.

Always ask user for confirmation before sending emails (`confirm_browser_operation`).

## File Inventory

After full execution, the working directory contains:

| File | Purpose |
|------|--------|
| `icp.md` | Ideal Customer Profile and scoring rubric |
| `email_templates.md` | Email templates for alerts, digests, outreach |
| `stripe_config.md` | Stripe product IDs, prices, payment links |
| `daily_leads_raw.md` | Raw discovered leads (updated daily) |
| `daily_leads_qualified.md` | Scored and tiered leads (updated daily) |
| `agent_prospects.md` | Researched agent customers with outreach drafts |
| `delivery_log.md` | Audit log of all deliveries |
