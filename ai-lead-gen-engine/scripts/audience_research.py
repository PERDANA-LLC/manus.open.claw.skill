#!/usr/bin/env python3
"""
AI Lead Generation Engine — Audience Research Script
Generates a comprehensive audience avatar and discovers where the audience
congregates online, using the OpenAI-compatible API.

Usage:
  python audience_research.py --product "<product/service description>" --niche "<niche/industry>"

Optional:
  --model <model_name>   (default: gpt-4.1-mini)
  --output <output_dir>  (default: ./lead_gen_output)
"""

import argparse
import json
import os
import sys
from datetime import datetime

try:
    from openai import OpenAI
except ImportError:
    print("Installing openai package...")
    os.system("sudo pip3 install openai -q")
    from openai import OpenAI


def call_llm(client, model, system_prompt, user_prompt, temperature=0.7):
    """Call the LLM and return the response text."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content


def step1_audience_avatar(client, model, product, niche):
    """Step 1: Generate a detailed audience avatar."""
    system_prompt = (
        "You are an expert market researcher and customer psychologist with 20+ years "
        "of experience building buyer personas for Fortune 500 companies and high-growth startups."
    )
    user_prompt = f"""Create a comprehensive Ideal Customer Avatar for the following:

**Product/Service:** {product}
**Niche/Industry:** {niche}

Produce a detailed avatar covering ALL of the following dimensions:

## Demographics
- Age range, gender distribution, income level, education, job title/role, company size

## Geographics
- Primary locations (countries, regions, city types), remote vs. in-office, timezone patterns

## Psychographics
- Values, beliefs, lifestyle, personality traits, risk tolerance, decision-making style

## Challenges & Pain Points
- Top 5 biggest frustrations, what keeps them up at night, failed solutions they've tried

## Goals & Aspirations
- What does success look like for them? Short-term and long-term goals

## Buying Behavior
- How they research purchases, who influences their decisions, budget authority, buying triggers, objections

## Content Consumption
- Preferred content formats (video, podcast, newsletter, blog), consumption times, devices

## Language & Messaging
- Words and phrases they use to describe their problems, emotional triggers, vocabulary patterns

Format the output as a structured Markdown document with clear sections and actionable detail."""

    return call_llm(client, model, system_prompt, user_prompt)


def step2_audience_hangouts(client, model, product, niche, avatar_summary):
    """Step 2: Discover where the target audience congregates online."""
    system_prompt = (
        "You are a digital marketing strategist specializing in audience intelligence "
        "and media buying. You have deep knowledge of online communities, newsletters, "
        "podcasts, influencers, and niche platforms across every industry."
    )
    user_prompt = f"""Based on this audience avatar, identify WHERE this target audience spends their time online.

**Product/Service:** {product}
**Niche/Industry:** {niche}
**Audience Avatar Summary:**
{avatar_summary}

For EACH category below, provide specific, real, named examples (not generic suggestions):

## 1. Newsletters They Subscribe To
- List 10-15 specific newsletters with estimated subscriber counts and topics
- Include both large and niche newsletters

## 2. Facebook Groups They Join
- List 10-15 specific Facebook groups with estimated member counts
- Note the activity level and engagement quality

## 3. Subreddits & Online Communities
- List 10-15 specific subreddits, Discord servers, Slack communities, or forums
- Include member counts and activity levels

## 4. Podcasts They Listen To
- List 10-15 specific podcasts with estimated listener counts
- Note the format and frequency

## 5. YouTube Channels & Influencers They Follow
- List 10-15 specific creators with subscriber counts
- Note content style and engagement rates

## 6. LinkedIn Groups & Thought Leaders
- List 10-15 specific LinkedIn groups or thought leaders
- Note follower counts and posting frequency

## 7. Industry Events & Conferences
- List 5-10 specific events (virtual and in-person)
- Note attendance size and ticket price range

## 8. Niche Platforms & Tools
- List 5-10 specific platforms, SaaS tools, or marketplaces they use daily

For each item, rate the **partnership potential** (High/Medium/Low) based on:
- Audience alignment with our target
- Accessibility for partnership deals
- Cost-effectiveness for lead generation

Format as a structured Markdown document with tables where appropriate."""

    return call_llm(client, model, system_prompt, user_prompt, temperature=0.8)


def step3_partnership_playbook(client, model, product, niche, hangouts_summary):
    """Step 3: Generate a partnership outreach strategy and playbook."""
    system_prompt = (
        "You are a business development expert specializing in media partnerships, "
        "newsletter sponsorships, community partnerships, and audience-access deals. "
        "You have brokered hundreds of successful partnerships for lead generation."
    )
    user_prompt = f"""Create a Partnership Outreach Playbook for lead generation based on these audience hangouts.

**Product/Service:** {product}
**Niche/Industry:** {niche}
**Audience Hangouts Identified:**
{hangouts_summary[:3000]}

Generate a complete playbook covering:

## 1. Partnership Prioritization Matrix
- Rank the top 15 partnership opportunities by: audience fit, cost, scalability, speed to results
- Create a priority tier (Tier 1: Start immediately, Tier 2: Next month, Tier 3: Quarter 2)

## 2. Outreach Templates
For each partnership type, provide a ready-to-send outreach message:
- Newsletter sponsorship pitch
- Facebook group collaboration pitch
- Podcast guest/sponsor pitch
- Influencer collaboration pitch
- Community partnership pitch

## 3. Deal Structures
- Common pricing models (CPM, CPA, flat fee, rev-share)
- Negotiation tactics and benchmarks
- Red flags to watch for

## 4. Tracking & Measurement
- KPIs to track for each partnership type
- UTM parameter strategy
- Attribution model recommendations

## 5. Scaling Strategy
- How to go from 1 partnership to 20+
- When to increase budget vs. diversify channels
- Automation opportunities

## 6. Budget Framework
- Suggested starting budget allocation across partnership types
- Expected CPL (cost per lead) ranges by channel
- ROI calculation template

Format as a structured Markdown document with actionable steps and templates."""

    return call_llm(client, model, system_prompt, user_prompt, temperature=0.7)


def main():
    parser = argparse.ArgumentParser(
        description="AI Lead Generation Engine — Audience Research & Partnership Discovery"
    )
    parser.add_argument("--product", required=True, help="Product or service description")
    parser.add_argument("--niche", required=True, help="Niche or industry")
    parser.add_argument("--model", default="gpt-4.1-mini", help="LLM model to use")
    parser.add_argument("--output", default="./lead_gen_output", help="Output directory")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    client = OpenAI()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print("=" * 60)
    print("  AI LEAD GENERATION ENGINE")
    print("=" * 60)
    print(f"  Product: {args.product}")
    print(f"  Niche:   {args.niche}")
    print(f"  Model:   {args.model}")
    print(f"  Output:  {args.output}")
    print("=" * 60)

    # Step 1: Audience Avatar
    print("\n[Step 1/3] Generating Audience Avatar...")
    avatar = step1_audience_avatar(client, args.model, args.product, args.niche)
    avatar_path = os.path.join(args.output, f"01_audience_avatar_{timestamp}.md")
    with open(avatar_path, "w") as f:
        f.write(f"# Audience Avatar\n\n**Product:** {args.product}\n**Niche:** {args.niche}\n**Generated:** {timestamp}\n\n---\n\n{avatar}")
    print(f"  ✅ Saved to {avatar_path}")

    # Step 2: Audience Hangouts
    print("\n[Step 2/3] Discovering Audience Hangouts...")
    hangouts = step2_audience_hangouts(client, args.model, args.product, args.niche, avatar)
    hangouts_path = os.path.join(args.output, f"02_audience_hangouts_{timestamp}.md")
    with open(hangouts_path, "w") as f:
        f.write(f"# Audience Hangouts & Online Presence\n\n**Product:** {args.product}\n**Niche:** {args.niche}\n**Generated:** {timestamp}\n\n---\n\n{hangouts}")
    print(f"  ✅ Saved to {hangouts_path}")

    # Step 3: Partnership Playbook
    print("\n[Step 3/3] Building Partnership Playbook...")
    playbook = step3_partnership_playbook(client, args.model, args.product, args.niche, hangouts)
    playbook_path = os.path.join(args.output, f"03_partnership_playbook_{timestamp}.md")
    with open(playbook_path, "w") as f:
        f.write(f"# Partnership Outreach Playbook\n\n**Product:** {args.product}\n**Niche:** {args.niche}\n**Generated:** {timestamp}\n\n---\n\n{playbook}")
    print(f"  ✅ Saved to {playbook_path}")

    # Generate Summary Report
    print("\n[Bonus] Generating Executive Summary...")
    summary_path = os.path.join(args.output, f"00_executive_summary_{timestamp}.md")
    with open(summary_path, "w") as f:
        f.write(f"""# AI Lead Generation — Executive Summary

**Product:** {args.product}
**Niche:** {args.niche}
**Generated:** {timestamp}

---

## Deliverables

| # | Document | Description |
|---|----------|-------------|
| 1 | `01_audience_avatar` | Detailed ideal customer avatar with demographics, psychographics, pain points |
| 2 | `02_audience_hangouts` | Where the target audience congregates online (newsletters, groups, podcasts, etc.) |
| 3 | `03_partnership_playbook` | Outreach templates, deal structures, and scaling strategy |

## Quick-Start Actions

1. Review the audience avatar and validate against your existing customers
2. Pick the top 5 highest-rated partnership opportunities from the hangouts report
3. Use the outreach templates from the playbook to contact publishers/owners
4. Track results using the UTM and attribution framework provided
5. Scale winning partnerships and cut underperformers after 2-4 weeks

---

*Generated by AI Lead Generation Engine — Based on Eric Beer's AI Lead Gen Strategy*
""")
    print(f"  ✅ Saved to {summary_path}")

    print("\n" + "=" * 60)
    print("  ✅ ALL STEPS COMPLETE")
    print(f"  📁 Output directory: {args.output}")
    print("=" * 60)

    return {
        "avatar_path": avatar_path,
        "hangouts_path": hangouts_path,
        "playbook_path": playbook_path,
        "summary_path": summary_path,
    }


if __name__ == "__main__":
    main()
