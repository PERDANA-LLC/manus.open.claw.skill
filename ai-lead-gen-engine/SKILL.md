---
name: ai-lead-gen-engine
description: AI-powered lead generation engine that builds audience avatars, discovers where target audiences congregate online, and generates partnership outreach playbooks. Use when the user mentions "lead generation," "find my audience," "audience avatar," "customer avatar," "where does my audience hang out," "newsletter sponsorship," "partnership outreach," "media buying," "audience research," "lead gen strategy," or wants to find and reach potential customers through existing online communities and publishers. Based on Eric Beer's proven 3-step AI lead gen framework.
---

# AI Lead Generation Engine

A 3-step AI-powered lead generation system that transforms a product description into a complete audience acquisition strategy. Based on Eric Beer's framework: (1) define who your customer is, (2) find where they already gather online, (3) partner with those publishers to access their audience.

## When to Use

- User wants to find and reach their target audience
- User needs an ideal customer avatar / buyer persona
- User wants to discover newsletters, groups, podcasts, or communities their audience uses
- User wants partnership outreach templates for lead generation
- User is launching a product and needs an audience acquisition strategy

## Workflow

The skill follows a 3-step sequential process:

1. **Build Audience Avatar** — Use AI to create a detailed ideal customer profile (demographics, geographics, psychographics, pain points, buying behavior)
2. **Discover Audience Hangouts** — Use AI to identify specific newsletters, Facebook groups, subreddits, podcasts, influencers, and communities where the target audience congregates
3. **Generate Partnership Playbook** — Produce outreach templates, deal structures, scoring matrices, and a scaling strategy for partnering with publishers/owners

## Quick Start — Automated Script

Run the full pipeline with a single command:

```bash
python /home/ubuntu/skills/ai-lead-gen-engine/scripts/audience_research.py \
  --product "Description of the product or service" \
  --niche "Industry or niche" \
  --output ./lead_gen_output
```

This generates four Markdown files in the output directory:
- `00_executive_summary` — Overview and quick-start actions
- `01_audience_avatar` — Detailed ICP with all dimensions
- `02_audience_hangouts` — Specific communities, newsletters, podcasts ranked by partnership potential
- `03_partnership_playbook` — Outreach templates, deal structures, budget framework

Optional flags: `--model <model>` (default: `gpt-4.1-mini`)

## Manual Workflow (Step-by-Step)

Use this when the user wants interactive control or needs to customize each step.

### Step 1: Build the Audience Avatar

Ask the user for:
- Product/service description
- Target niche or industry
- Any existing customer data or assumptions

Then prompt the LLM to generate a comprehensive avatar covering: demographics, geographics, psychographics, challenges/pain points, goals, buying behavior, content consumption habits, and language patterns.

Validate the avatar with the user before proceeding.

### Step 2: Discover Audience Hangouts

Using the avatar from Step 1, prompt the LLM to identify **specific, named** examples across these categories:

| Category | Target Count | Key Data Points |
|----------|-------------|------------------|
| Newsletters | 10-15 | Name, subscriber count, sponsorship availability |
| Facebook Groups | 10-15 | Name, member count, activity level |
| Subreddits & Communities | 10-15 | Name, platform, member count |
| Podcasts | 10-15 | Name, listener count, format |
| Influencers & Creators | 10-15 | Name, platform, follower count |
| LinkedIn Groups/Leaders | 10-15 | Name, follower count |
| Events & Conferences | 5-10 | Name, attendance, cost |

Rate each by **partnership potential** (High/Medium/Low).

**Important:** After AI generation, use web search to verify and enrich the top recommendations with real, current data. AI may hallucinate specific names or subscriber counts.

### Step 3: Generate Partnership Playbook

Using hangouts from Step 2, generate:
1. **Priority matrix** — Tier 1/2/3 ranked by audience fit, cost, scalability
2. **Outreach templates** — Ready-to-send messages for each partnership type
3. **Deal structures** — Pricing models, negotiation benchmarks
4. **Tracking plan** — KPIs, UTM strategy, attribution
5. **Budget framework** — Allocation, expected CPL, ROI calculations

See `references/partnership_scoring.md` for the scoring matrix and deal structure benchmarks.
See `references/prompt_templates.md` for ready-to-use outreach message templates.

## Output Format

Use `templates/lead_gen_report.md` as the structural template for the final deliverable. Deliver as a single comprehensive Markdown document or as separate files per step.

## Bundled Resources

| Resource | Path | Purpose |
|----------|------|---------|
| Automated script | `scripts/audience_research.py` | Runs full 3-step pipeline via CLI |
| Prompt templates | `references/prompt_templates.md` | Deep-dive prompts and outreach message templates |
| Scoring guide | `references/partnership_scoring.md` | Partnership scoring matrix and deal structure benchmarks |
| Report template | `templates/lead_gen_report.md` | Structural template for the final report |

## Verification Checklist

Before delivering results, verify:
- [ ] Avatar includes all 8 dimensions (demographics, geographics, psychographics, pain points, goals, buying behavior, content consumption, language)
- [ ] Hangouts include specific named examples (not generic categories)
- [ ] Top recommendations have been web-searched for verification
- [ ] Partnership potential ratings are assigned
- [ ] Outreach templates are personalized to the user's product
- [ ] Budget framework includes realistic CPL estimates
