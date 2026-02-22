---
name: local-lead-enricher
description: Enriches a list of local businesses with contact data and quality signals, then filters the list based on predefined criteria. Use this skill to qualify leads sourced by `lead-research-assistant`.
---

# Local Lead Enricher

This skill takes a list of local businesses (e.g., from `lead-research-assistant`) and enriches it with contact data and quality signals. It then filters the list to produce a final, qualified lead list ready for outreach.

## When to Use This Skill

- After using `lead-research-assistant` to generate a raw list of local businesses.
- When you need to qualify a list of companies based on their online presence (website, reviews).
- To find contact information (owner name, email) for a list of local businesses.
- To automate the process of filtering a large prospect list down to a high-quality, actionable list.

## How to Use

This skill is designed to be used as part of a chain, typically after `lead-research-assistant`.

1.  **Input:** Provide a CSV file containing a list of business names and their locations (city, state).
2.  **Execution:** The skill will process the list and perform the enrichment and filtering steps.
3.  **Output:** The skill will output a new CSV file named `qualified_leads.csv` containing the enriched and filtered leads.

### Example Workflow

1.  `lead-research-assistant` -> `raw_leads.csv`
2.  `local-lead-enricher` (input: `raw_leads.csv`) -> `qualified_leads.csv`
3.  `oc-google-workspace` (input: `qualified_leads.csv`) -> Send outreach emails

## Instructions

When this skill is triggered, follow these steps:

1.  **Acknowledge the Input:** Confirm that you have received the input CSV file of business names and locations.
2.  **Run the Enrichment Script:** Execute the `enrich_and_filter.py` script located in the `scripts/` directory of this skill.

    ```bash
    python3 /home/ubuntu/skills/local-lead-enricher/scripts/enrich_and_filter.py /path/to/input.csv
    ```

3.  **Confirm Output:** Announce that the enrichment is complete and the `qualified_leads.csv` file has been created.
4.  **Suggest Next Steps:** Recommend using the `oc-google-workspace` skill to send outreach emails to the newly qualified leads.

## Bundled Resources

-   **`scripts/enrich_and_filter.py`**: The core Python script that performs the enrichment and filtering logic.
-   **`references/common_contact_pages.txt`**: A list of common URL paths for "Contact Us" or "About Us" pages to help the script find contact information more efficiently.
