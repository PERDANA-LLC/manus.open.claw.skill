---
name: client-acquisition-engine
description: Automates the entire client acquisition process for a digital marketing agency by finding, enriching, and engaging potential B2B clients using a predefined Manus skill stack.
---

# Client Acquisition Engine

This skill automates the process of generating leads for a digital marketing agency. It chains together several other Manus skills to create a complete, end-to-end client acquisition pipeline.

## Workflow

This skill operates in four distinct phases:

1.  **Phase 1: Prospecting.** The user provides an Ideal Customer Profile (ICP) as input (e.g., "SaaS companies with 50-200 employees"). The skill uses the `lead-research-assistant` skill to generate a broad list of companies that match this profile.

2.  **Phase 2: Enrichment & Qualification.** The skill takes the list of companies and uses the `local-lead-enricher` skill to find contact information for key decision-makers (CMO, CEO, etc.) and to filter out any low-quality prospects.

3.  **Phase 3: Outreach.** The skill uses the `mk-cold-email` skill to draft and send a personalized outreach sequence to the qualified decision-makers. The email templates will be stored as reference files within this skill.

4.  **Phase 4: Monitoring & Reporting.** The skill uses the `oc-google-workspace` skill to monitor the outreach email account for positive replies. When a positive reply is detected, it is parsed and added to a central CSV file in the user's Google Drive, effectively serving as the agency's CRM.

## Scripts

*   `scripts/run_pipeline.py`: The main Python script that orchestrates the four phases, calling each of the required Manus skills in sequence and passing the output of one phase as the input to the next.

## References

*   `references/b2b_email_templates.txt`: A collection of high-converting cold email templates for selling digital marketing services.
