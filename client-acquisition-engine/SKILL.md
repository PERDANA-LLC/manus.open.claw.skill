---
name: client-acquisition-engine
description: Automates end-to-end client acquisition for a digital marketing agency. Chains lead-research-assistant, local-lead-enricher, mk-cold-email, and oc-google-workspace into a four-phase pipeline (Prospect, Enrich, Outreach, Monitor) that discovers qualified leads, drafts personalized cold emails, sends them via Gmail, and logs positive replies to a Google Drive CRM spreadsheet.
---

# Client Acquisition Engine

Automates the complete client acquisition lifecycle for **Cash in Blue** (https://pro.cashinblue.com), a digital marketing agency serving local service businesses and B2B companies. The engine chains four Manus skills into a repeatable pipeline that can be triggered on-demand or scheduled to run at regular intervals.

## When to Use This Skill

- You want to find, qualify, and contact new prospects automatically.
- You need to build a pipeline of qualified leads for your digital marketing agency.
- You want to send personalized cold email sequences to decision-makers.
- You want to monitor replies and maintain a lightweight CRM in Google Drive.
- You mention "client acquisition," "lead pipeline," "outreach campaign," or "prospect engine."

## Prerequisites

The following Manus skills must be installed and enabled:

| Skill | Purpose |
|---|---|
| `lead-research-assistant` | Phase 1 - Discovers companies matching the ICP |
| `local-lead-enricher` | Phase 2 - Enriches leads with contact data and quality scores |
| `mk-cold-email` | Phase 3 - Drafts high-converting cold email sequences |
| `oc-google-workspace` | Phase 4 - Sends emails via Gmail and monitors replies |

Additionally, the following integrations must be connected in Manus Settings:

- **Gmail** MCP connector (for sending and monitoring emails)
- **Google Calendar** MCP connector (optional, for scheduling follow-ups)
- **Google Drive** via rclone (for CRM spreadsheet storage)

## How It Works

### Phase 1: Prospecting

**Goal:** Generate a raw list of companies that match the Ideal Customer Profile.

**Input required from user:**

- **ICP description** - e.g., "Plumbing companies in Dallas, TX with 5-50 employees"
- **Lead count** - Number of leads to find (default: 25)
- **Service to sell** - e.g., "SEO and Google Ads management"

**Steps:**

1. Read the user-provided ICP and service description.
2. Invoke the `lead-research-assistant` skill with the ICP parameters.
3. Instruct it to output results as a structured list with: Company Name, Website, Location, Industry, Employee Count, Decision Maker Title, Priority Score (1-10), and Why They Are a Good Fit.
4. Save the raw output to `/home/ubuntu/pipeline_output/raw_leads.csv`.

**Prompt to use for lead-research-assistant:**

```
My agency: Cash in Blue (https://pro.cashinblue.com) - digital marketing agency.
Service we sell: {user_service_description}

Ideal Customer Profile:
{user_icp_description}

Find me {lead_count} qualified leads. For each lead provide:
- Company Name
- Website URL
- City, State
- Industry
- Estimated employee count
- Decision maker title to target
- Priority score (1-10)
- Why they are a good fit (one sentence)
- LinkedIn URL of decision maker (if available)

Format the output as a CSV table I can save directly.
```

### Phase 2: Enrichment and Qualification

**Goal:** Enrich the raw leads with verified contact data and filter out low-quality prospects.

**Steps:**

1. Take the `raw_leads.csv` from Phase 1.
2. Invoke the `local-lead-enricher` skill by running its enrichment script:

```bash
python3 /home/ubuntu/skills/local-lead-enricher/scripts/enrich_and_filter.py /home/ubuntu/pipeline_output/raw_leads.csv
```

3. The script will output `qualified_leads.csv` with enriched fields: Owner/Contact Name, Email Address, Phone Number, Website Quality Score, Google Review Count, and Overall Lead Score.
4. Move the output to `/home/ubuntu/pipeline_output/qualified_leads.csv`.
5. Report the enrichment summary: total leads processed, leads that passed qualification, average lead score.

**Qualification Criteria (configurable):**

- Minimum lead score: 6/10
- Must have at least one contact method (email or phone)
- Website must be live and indexable
- Exclude leads already in the CRM spreadsheet (de-duplication)

### Phase 3: Outreach

**Goal:** Draft and send personalized cold email sequences to qualified leads.

**Steps:**

1. Read the `qualified_leads.csv` from Phase 2.
2. For each qualified lead, use the `mk-cold-email` skill to draft a 3-email sequence:
   - **Email 1 (Day 0):** The Value-First Opener - offers a free audit or free leads.
   - **Email 2 (Day 3):** The Pain-Point Follow-Up - addresses common struggles.
   - **Email 3 (Day 7):** The Breakup Email - respectful close with open door.
3. Use the email templates in `references/b2b_email_templates.txt` as the baseline.
4. Personalize each email using data from the enriched CSV: company name, contact first name, industry, city, and the "why they are a good fit" insight.
5. Present the drafted emails to the user for review before sending.
6. After user approval, send Email 1 for all leads using `oc-google-workspace`:

```bash
manus-mcp-cli tool call gmail_send_messages --server gmail --input '{
  "messages": [
    {
      "to": ["{lead_email}"],
      "subject": "{personalized_subject}",
      "content": "{personalized_body}"
    }
  ]
}'
```

7. Log each sent email to `/home/ubuntu/pipeline_output/outreach_log.csv` with columns: Date Sent, Lead Name, Company, Email, Subject, Sequence Step, Status.
8. Schedule follow-up emails (Email 2 and Email 3) by creating Google Calendar reminders:

```bash
manus-mcp-cli tool call google_calendar_create_events --server google-calendar --input '{
  "events": [
    {
      "summary": "Send follow-up to {contact_name} at {company}",
      "start_time": "{follow_up_datetime}",
      "end_time": "{follow_up_datetime_plus_30min}"
    }
  ]
}'
```

### Phase 4: Monitoring and Reporting

**Goal:** Monitor the Gmail inbox for positive replies and maintain a CRM in Google Drive.

**Steps:**

1. Search Gmail for replies to outreach emails:

```bash
manus-mcp-cli tool call gmail_search_messages --server gmail --input '{
  "q": "subject:(re:) newer_than:7d -from:me label:inbox",
  "max_results": 50
}'
```

2. Read each reply thread to classify the response:
   - **Positive:** Interested, wants to learn more, requests a call.
   - **Negative:** Not interested, unsubscribe request.
   - **Neutral:** Auto-reply, out of office.

3. For positive replies, extract: Contact Name, Company, Email, Reply Date, Reply Summary, and Suggested Next Action.

4. Append positive replies to the CRM spreadsheet in Google Drive:

```bash
# Create or update the CRM CSV
rclone copy /home/ubuntu/pipeline_output/crm_positive_replies.csv \
  manus_google_drive:"Cash in Blue/CRM/" \
  --config /home/ubuntu/.gdrive-rclone.ini
```

5. Generate a campaign performance report with metrics:
   - Total emails sent
   - Open rate estimate (based on replies)
   - Reply rate
   - Positive reply rate
   - Leads moved to CRM
   - Suggested optimizations for next campaign

6. Save the report to `/home/ubuntu/pipeline_output/campaign_report.md`.

## Running the Full Pipeline

To execute the complete pipeline, provide the following inputs:

```
Run the client acquisition engine with:
- ICP: {describe your ideal customer}
- Lead count: {number, default 25}
- Service: {what you are selling}
- Sender name: {your name, default "Thomas at Cash in Blue"}
- Sender email: {your email, default "thomasperdana@gmail.com"}
```

The engine will execute Phases 1 through 3 sequentially, presenting results at each checkpoint for your approval before proceeding. Phase 4 (monitoring) can be run separately at any time to check for replies.

## Running Individual Phases

You can run any phase independently:

- **"Run Phase 1 only"** - Just prospect and generate raw leads.
- **"Run Phase 2 with this CSV"** - Enrich an existing lead list.
- **"Run Phase 3 for these leads"** - Draft and send outreach for pre-qualified leads.
- **"Run Phase 4 / Check replies"** - Monitor inbox and update CRM.

## Pipeline Output Files

All pipeline artifacts are stored in `/home/ubuntu/pipeline_output/`:

| File | Description |
|---|---|
| `raw_leads.csv` | Unfiltered leads from Phase 1 |
| `qualified_leads.csv` | Enriched and filtered leads from Phase 2 |
| `outreach_log.csv` | Record of all emails sent in Phase 3 |
| `crm_positive_replies.csv` | Positive replies tracked as CRM entries |
| `campaign_report.md` | Performance metrics and optimization suggestions |

## CRM Spreadsheet Schema

The Google Drive CRM file (`Cash in Blue/CRM/crm_positive_replies.csv`) uses this schema:

| Column | Description |
|---|---|
| date_added | Date the lead was added to CRM |
| contact_name | Full name of the respondent |
| company | Company name |
| email | Email address |
| phone | Phone number (if available) |
| reply_date | Date of the positive reply |
| reply_summary | One-line summary of their reply |
| lead_source | Campaign identifier (e.g., "2026-02-plumbers-dallas") |
| status | Current status: New, Contacted, Meeting Scheduled, Proposal Sent, Won, Lost |
| next_action | Suggested follow-up action |
| notes | Free-text notes field |

## Email Templates

The skill includes pre-built email templates in `references/b2b_email_templates.txt`. These templates are optimized for selling digital marketing services (SEO, Google Ads, social media, web design) to local service businesses.

Each template uses merge fields: `{{firstName}}`, `{{companyName}}`, `{{city}}`, `{{industry}}`, `{{painPoint}}`, `{{proofPoint}}`.

## Configuration

Default settings can be overridden per-run:

| Setting | Default | Description |
|---|---|---|
| lead_count | 25 | Number of leads to prospect |
| min_lead_score | 6 | Minimum score to qualify (1-10) |
| email_sequence_length | 3 | Number of emails in the sequence |
| follow_up_gap_days | 3,7 | Days between follow-up emails |
| sender_name | Thomas at Cash in Blue | Display name on outreach emails |
| sender_email | thomasperdana@gmail.com | Gmail account for sending |
| crm_drive_path | Cash in Blue/CRM/ | Google Drive folder for CRM |
| campaign_id | auto-generated | Format: YYYY-MM-industry-city |

## Scripts

- `scripts/run_pipeline.py` - Main orchestration script that coordinates all four phases, manages file I/O between phases, handles error recovery, and generates the campaign report.

## References

- `references/b2b_email_templates.txt` - Six high-converting cold email templates for digital marketing services, covering multiple angles (free audit, pain-point, social proof, competitor gap, ROI calculator, breakup).

## Related Skills

- `lead-research-assistant` - Used in Phase 1 for prospecting.
- `local-lead-enricher` - Used in Phase 2 for enrichment and qualification.
- `mk-cold-email` - Used in Phase 3 for drafting email sequences.
- `oc-google-workspace` - Used in Phases 3-4 for sending emails and monitoring replies.
- `mk-email-sequence` - For post-acquisition nurture sequences (not cold outreach).
- `mk-copywriting` - For landing page copy to support outreach campaigns.
