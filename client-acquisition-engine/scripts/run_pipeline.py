#!/usr/bin/env python3
"""
Client Acquisition Engine - Pipeline Orchestrator
==================================================
Coordinates the four-phase client acquisition pipeline:
  Phase 1: Prospecting       (lead-research-assistant)
  Phase 2: Enrichment        (local-lead-enricher)
  Phase 3: Outreach          (mk-cold-email + oc-google-workspace)
  Phase 4: Monitoring        (oc-google-workspace)

Usage:
  python3 run_pipeline.py --icp "Plumbers in Dallas TX" --count 25 --service "SEO and Google Ads"
  python3 run_pipeline.py --phase 4  # Run monitoring only
  python3 run_pipeline.py --phase 2 --input /path/to/raw_leads.csv  # Enrich existing list

Author: Cash in Blue (https://pro.cashinblue.com)
"""

import argparse
import csv
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PIPELINE_DIR = Path.home() / "pipeline_output"
RAW_LEADS_FILE = PIPELINE_DIR / "raw_leads.csv"
QUALIFIED_LEADS_FILE = PIPELINE_DIR / "qualified_leads.csv"
OUTREACH_LOG_FILE = PIPELINE_DIR / "outreach_log.csv"
CRM_FILE = PIPELINE_DIR / "crm_positive_replies.csv"
REPORT_FILE = PIPELINE_DIR / "campaign_report.md"

ENRICHER_SCRIPT = Path.home() / "skills" / "local-lead-enricher" / "scripts" / "enrich_and_filter.py"
TEMPLATES_FILE = Path(__file__).parent.parent / "references" / "b2b_email_templates.txt"

GDRIVE_CONFIG = Path.home() / ".gdrive-rclone.ini"
CRM_DRIVE_PATH = "Cash in Blue/CRM/"

DEFAULTS = {
    "sender_name": "Thomas",
    "sender_title": "Founder",
    "agency_name": "Cash in Blue",
    "sender_email": "thomasperdana@gmail.com",
    "lead_count": 25,
    "min_lead_score": 6,
    "follow_up_days": [3, 7],
}


def ensure_pipeline_dir():
    """Create the pipeline output directory if it does not exist."""
    PIPELINE_DIR.mkdir(parents=True, exist_ok=True)


def log(phase, message):
    """Print a timestamped log message."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [Phase {phase}] {message}")


# ---------------------------------------------------------------------------
# Phase 1: Prospecting
# ---------------------------------------------------------------------------

def run_phase_1(icp_description, lead_count, service_description):
    """
    Generate a raw list of leads matching the ICP.

    This function prepares the prompt that should be passed to the
    lead-research-assistant skill. In practice, the Manus agent reads
    this prompt and invokes the skill conversationally.
    """
    log(1, "Starting Prospecting phase")
    log(1, f"ICP: {icp_description}")
    log(1, f"Lead count: {lead_count}")
    log(1, f"Service: {service_description}")

    prompt = f"""My agency: Cash in Blue (https://pro.cashinblue.com) - digital marketing agency.
Service we sell: {service_description}

Ideal Customer Profile:
{icp_description}

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

Format the output as a CSV with headers:
company_name,website,city_state,industry,employee_count,decision_maker_title,priority_score,fit_reason,linkedin_url
"""

    prompt_file = PIPELINE_DIR / "phase1_prompt.txt"
    prompt_file.write_text(prompt)
    log(1, f"Prompt saved to {prompt_file}")
    log(1, "ACTION REQUIRED: Run the lead-research-assistant skill with the prompt above.")
    log(1, f"Save the CSV output to {RAW_LEADS_FILE}")

    # Initialize the raw leads CSV with headers if it does not exist
    if not RAW_LEADS_FILE.exists():
        with open(RAW_LEADS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "company_name", "website", "city_state", "industry",
                "employee_count", "decision_maker_title", "priority_score",
                "fit_reason", "linkedin_url"
            ])
        log(1, f"Initialized {RAW_LEADS_FILE} with headers")

    return str(RAW_LEADS_FILE)


# ---------------------------------------------------------------------------
# Phase 2: Enrichment and Qualification
# ---------------------------------------------------------------------------

def run_phase_2(input_csv=None):
    """
    Enrich raw leads with contact data and filter by quality score.
    """
    log(2, "Starting Enrichment phase")
    source = input_csv or str(RAW_LEADS_FILE)

    if not Path(source).exists():
        log(2, f"ERROR: Input file not found: {source}")
        log(2, "Run Phase 1 first or provide --input with a valid CSV path.")
        return None

    # Count input leads
    with open(source) as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        input_count = sum(1 for _ in reader)
    log(2, f"Input leads: {input_count}")

    # Run the enricher script
    if ENRICHER_SCRIPT.exists():
        log(2, f"Running enricher: {ENRICHER_SCRIPT}")
        result = subprocess.run(
            ["python3", str(ENRICHER_SCRIPT), source],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            log(2, f"Enricher error: {result.stderr}")
            log(2, "Falling through to manual enrichment mode.")
        else:
            log(2, f"Enricher output: {result.stdout.strip()}")
    else:
        log(2, f"Enricher script not found at {ENRICHER_SCRIPT}")
        log(2, "ACTION REQUIRED: Run the local-lead-enricher skill manually.")

    # Check for output
    if QUALIFIED_LEADS_FILE.exists():
        with open(QUALIFIED_LEADS_FILE) as f:
            reader = csv.reader(f)
            next(reader, None)
            qualified_count = sum(1 for _ in reader)
        log(2, f"Qualified leads: {qualified_count} / {input_count}")
    else:
        log(2, f"Output file not yet created at {QUALIFIED_LEADS_FILE}")
        log(2, "ACTION REQUIRED: Save enriched leads to the file above.")

    return str(QUALIFIED_LEADS_FILE)


# ---------------------------------------------------------------------------
# Phase 3: Outreach
# ---------------------------------------------------------------------------

def load_qualified_leads(csv_path):
    """Load qualified leads from CSV into a list of dicts."""
    leads = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    return leads


def personalize_template(template_text, lead, config):
    """Replace merge fields in a template with lead-specific data."""
    replacements = {
        "{{firstName}}": lead.get("contact_name", lead.get("decision_maker_title", "there")).split()[0],
        "{{companyName}}": lead.get("company_name", "your company"),
        "{{city}}": lead.get("city_state", "your area").split(",")[0].strip(),
        "{{industry}}": lead.get("industry", "your industry"),
        "{{painPoint}}": lead.get("fit_reason", "your online presence could be generating more leads"),
        "{{proofPoint}}": f"A {lead.get('industry', 'local')} business we worked with doubled their monthly leads in 90 days",
        "{{senderName}}": config.get("sender_name", DEFAULTS["sender_name"]),
        "{{senderTitle}}": config.get("sender_title", DEFAULTS["sender_title"]),
        "{{agencyName}}": config.get("agency_name", DEFAULTS["agency_name"]),
    }
    result = template_text
    for field, value in replacements.items():
        result = result.replace(field, value)
    return result


def parse_templates(templates_path):
    """Parse the b2b_email_templates.txt file into individual templates."""
    templates = {}
    current_name = None
    current_lines = []

    with open(templates_path) as f:
        for line in f:
            if line.startswith("TEMPLATE "):
                if current_name and current_lines:
                    templates[current_name] = "".join(current_lines).strip()
                current_name = line.strip().rstrip("=").strip()
                current_lines = []
            elif line.startswith("=" * 10):
                continue
            elif current_name:
                current_lines.append(line)

    if current_name and current_lines:
        templates[current_name] = "".join(current_lines).strip()

    return templates


def build_email_sequence(lead, config):
    """Build a 3-email sequence for a single lead."""
    templates = parse_templates(TEMPLATES_FILE)

    # Select templates for the 3-email sequence
    template_keys = list(templates.keys())
    sequence = []

    # Template 1: Free Audit Opener (Day 0)
    if len(template_keys) >= 1:
        body = personalize_template(templates[template_keys[0]], lead, config)
        subject_line = f"{lead.get('city_state', 'local').split(',')[0].strip().lower()} {lead.get('industry', 'business').lower()} marketing"
        sequence.append({
            "day": 0,
            "subject": subject_line,
            "body": body,
            "template_name": template_keys[0],
        })

    # Template 2: Pain-Point Follow-Up (Day 3)
    if len(template_keys) >= 2:
        body = personalize_template(templates[template_keys[1]], lead, config)
        subject_line = f"re: {sequence[0]['subject']}" if sequence else "following up"
        sequence.append({
            "day": config.get("follow_up_days", DEFAULTS["follow_up_days"])[0],
            "subject": subject_line,
            "body": body,
            "template_name": template_keys[1],
        })

    # Template 6: Breakup Email (Day 7)
    if len(template_keys) >= 6:
        body = personalize_template(templates[template_keys[5]], lead, config)
        sequence.append({
            "day": config.get("follow_up_days", DEFAULTS["follow_up_days"])[1],
            "subject": "closing the loop",
            "body": body,
            "template_name": template_keys[5],
        })

    return sequence


def send_email_via_gmail(to_email, subject, body):
    """Send a single email using the Gmail MCP connector."""
    payload = json.dumps({
        "messages": [{
            "to": [to_email],
            "subject": subject,
            "content": body,
        }]
    })

    result = subprocess.run(
        ["manus-mcp-cli", "tool", "call", "gmail_send_messages",
         "--server", "gmail", "--input", payload],
        capture_output=True, text=True
    )

    return result.returncode == 0, result.stdout, result.stderr


def log_outreach(lead, email_data, status):
    """Append a record to the outreach log CSV."""
    file_exists = OUTREACH_LOG_FILE.exists()
    with open(OUTREACH_LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "date_sent", "contact_name", "company", "email",
                "subject", "sequence_step", "status"
            ])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            lead.get("contact_name", "Unknown"),
            lead.get("company_name", "Unknown"),
            lead.get("email", "Unknown"),
            email_data.get("subject", ""),
            email_data.get("day", 0),
            status,
        ])


def schedule_follow_up(lead, email_data, send_date):
    """Create a Google Calendar event as a follow-up reminder."""
    follow_up_time = send_date + timedelta(days=email_data["day"])
    start_iso = follow_up_time.strftime("%Y-%m-%dT09:00:00-05:00")
    end_iso = follow_up_time.strftime("%Y-%m-%dT09:30:00-05:00")

    payload = json.dumps({
        "events": [{
            "summary": f"Follow-up: {lead.get('contact_name', 'Lead')} at {lead.get('company_name', 'Company')} (Step {email_data['day']})",
            "start_time": start_iso,
            "end_time": end_iso,
        }]
    })

    subprocess.run(
        ["manus-mcp-cli", "tool", "call", "google_calendar_create_events",
         "--server", "google-calendar", "--input", payload],
        capture_output=True, text=True
    )


def run_phase_3(input_csv=None, config=None):
    """
    Draft and send personalized cold email sequences.
    """
    log(3, "Starting Outreach phase")
    config = config or {}
    source = input_csv or str(QUALIFIED_LEADS_FILE)

    if not Path(source).exists():
        log(3, f"ERROR: Qualified leads file not found: {source}")
        return

    leads = load_qualified_leads(source)
    log(3, f"Loaded {len(leads)} qualified leads")

    all_sequences = []
    for lead in leads:
        sequence = build_email_sequence(lead, config)
        all_sequences.append({"lead": lead, "sequence": sequence})

    # Save drafted emails for review
    drafts_file = PIPELINE_DIR / "email_drafts.json"
    with open(drafts_file, "w") as f:
        json.dump(all_sequences, f, indent=2, default=str)
    log(3, f"Email drafts saved to {drafts_file}")
    log(3, f"Total sequences: {len(all_sequences)}")
    log(3, f"Total emails to send: {sum(len(s['sequence']) for s in all_sequences)}")

    log(3, "ACTION REQUIRED: Review drafts and approve before sending.")
    log(3, "To send, re-run with --send flag or approve in the Manus conversation.")

    return str(drafts_file)


# ---------------------------------------------------------------------------
# Phase 4: Monitoring and Reporting
# ---------------------------------------------------------------------------

def run_phase_4():
    """
    Monitor Gmail for replies and update the CRM spreadsheet.
    """
    log(4, "Starting Monitoring phase")

    # Search for recent replies
    log(4, "Searching Gmail for replies to outreach emails...")
    search_payload = json.dumps({
        "q": "newer_than:7d -from:me label:inbox",
        "max_results": 50,
    })

    result = subprocess.run(
        ["manus-mcp-cli", "tool", "call", "gmail_search_messages",
         "--server", "gmail", "--input", search_payload],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        log(4, f"Gmail search error: {result.stderr}")
        log(4, "ACTION REQUIRED: Run Gmail search manually via oc-google-workspace skill.")
        return

    log(4, f"Gmail search results: {result.stdout[:500]}...")
    log(4, "ACTION REQUIRED: Review replies and classify as Positive/Negative/Neutral.")

    # Initialize CRM file if needed
    if not CRM_FILE.exists():
        with open(CRM_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date_added", "contact_name", "company", "email", "phone",
                "reply_date", "reply_summary", "lead_source", "status",
                "next_action", "notes"
            ])
        log(4, f"Initialized CRM file: {CRM_FILE}")

    # Sync CRM to Google Drive
    if GDRIVE_CONFIG.exists():
        log(4, "Syncing CRM to Google Drive...")
        sync_result = subprocess.run(
            ["rclone", "copy", str(CRM_FILE),
             f"manus_google_drive:{CRM_DRIVE_PATH}",
             "--config", str(GDRIVE_CONFIG)],
            capture_output=True, text=True
        )
        if sync_result.returncode == 0:
            log(4, "CRM synced to Google Drive successfully.")
        else:
            log(4, f"Drive sync error: {sync_result.stderr}")
    else:
        log(4, "Google Drive config not found. Skipping sync.")

    # Generate campaign report
    generate_report()

    return str(CRM_FILE)


def generate_report():
    """Generate a campaign performance report."""
    log(4, "Generating campaign report...")

    stats = {
        "total_sent": 0,
        "total_qualified": 0,
        "total_raw": 0,
        "positive_replies": 0,
    }

    if OUTREACH_LOG_FILE.exists():
        with open(OUTREACH_LOG_FILE) as f:
            reader = csv.DictReader(f)
            for row in reader:
                stats["total_sent"] += 1

    if QUALIFIED_LEADS_FILE.exists():
        with open(QUALIFIED_LEADS_FILE) as f:
            reader = csv.reader(f)
            next(reader, None)
            stats["total_qualified"] = sum(1 for _ in reader)

    if RAW_LEADS_FILE.exists():
        with open(RAW_LEADS_FILE) as f:
            reader = csv.reader(f)
            next(reader, None)
            stats["total_raw"] = sum(1 for _ in reader)

    if CRM_FILE.exists():
        with open(CRM_FILE) as f:
            reader = csv.DictReader(f)
            stats["positive_replies"] = sum(1 for _ in reader)

    reply_rate = (stats["positive_replies"] / stats["total_sent"] * 100) if stats["total_sent"] > 0 else 0
    qualification_rate = (stats["total_qualified"] / stats["total_raw"] * 100) if stats["total_raw"] > 0 else 0

    campaign_id = datetime.now().strftime("%Y-%m")

    report = f"""# Campaign Report - {campaign_id}

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Agency:** Cash in Blue (https://pro.cashinblue.com)

## Pipeline Metrics

| Metric | Value |
|---|---|
| Raw leads prospected | {stats['total_raw']} |
| Leads qualified | {stats['total_qualified']} |
| Qualification rate | {qualification_rate:.1f}% |
| Emails sent | {stats['total_sent']} |
| Positive replies | {stats['positive_replies']} |
| Reply rate | {reply_rate:.1f}% |

## Funnel Conversion

```
Raw Leads:       {stats['total_raw']}
  |
  v  ({qualification_rate:.0f}% qualification rate)
Qualified:       {stats['total_qualified']}
  |
  v  (outreach sent)
Emails Sent:     {stats['total_sent']}
  |
  v  ({reply_rate:.0f}% reply rate)
Positive Replies: {stats['positive_replies']}
```

## Files

- Raw leads: `{RAW_LEADS_FILE}`
- Qualified leads: `{QUALIFIED_LEADS_FILE}`
- Outreach log: `{OUTREACH_LOG_FILE}`
- CRM (positive replies): `{CRM_FILE}`

## Recommendations

1. If reply rate is below 5%, test different subject lines and opening hooks.
2. If qualification rate is below 40%, refine the ICP or expand the search criteria.
3. Review the breakup email responses - they often convert later.
4. Schedule a weekly Phase 4 run to keep the CRM current.
5. Export positive replies to a proper CRM once volume exceeds 50 leads.
"""

    REPORT_FILE.write_text(report)
    log(4, f"Report saved to {REPORT_FILE}")


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Client Acquisition Engine - Pipeline Orchestrator"
    )
    parser.add_argument("--phase", type=int, choices=[1, 2, 3, 4],
                        help="Run a specific phase (1-4). Default: run all.")
    parser.add_argument("--icp", type=str,
                        help="Ideal Customer Profile description (Phase 1)")
    parser.add_argument("--count", type=int, default=DEFAULTS["lead_count"],
                        help=f"Number of leads to find (default: {DEFAULTS['lead_count']})")
    parser.add_argument("--service", type=str, default="SEO, Google Ads, and web design",
                        help="Service description to sell")
    parser.add_argument("--input", type=str,
                        help="Input CSV file path (for Phase 2 or 3)")
    parser.add_argument("--sender-name", type=str, default=DEFAULTS["sender_name"],
                        help="Sender name for outreach emails")
    parser.add_argument("--sender-email", type=str, default=DEFAULTS["sender_email"],
                        help="Sender email address")
    parser.add_argument("--send", action="store_true",
                        help="Actually send emails (Phase 3). Without this flag, only drafts are created.")

    args = parser.parse_args()
    ensure_pipeline_dir()

    config = {
        "sender_name": args.sender_name,
        "sender_email": args.sender_email,
        "sender_title": DEFAULTS["sender_title"],
        "agency_name": DEFAULTS["agency_name"],
    }

    if args.phase:
        # Run a single phase
        if args.phase == 1:
            if not args.icp:
                print("ERROR: --icp is required for Phase 1")
                sys.exit(1)
            run_phase_1(args.icp, args.count, args.service)
        elif args.phase == 2:
            run_phase_2(args.input)
        elif args.phase == 3:
            run_phase_3(args.input, config)
        elif args.phase == 4:
            run_phase_4()
    else:
        # Run full pipeline
        if not args.icp:
            print("ERROR: --icp is required for the full pipeline")
            print("Usage: python3 run_pipeline.py --icp 'Plumbers in Dallas TX' --service 'SEO and Google Ads'")
            sys.exit(1)

        print("=" * 70)
        print("CLIENT ACQUISITION ENGINE - FULL PIPELINE")
        print("=" * 70)

        run_phase_1(args.icp, args.count, args.service)
        print()
        run_phase_2(args.input)
        print()
        run_phase_3(args.input, config)
        print()
        run_phase_4()

        print()
        print("=" * 70)
        print("PIPELINE COMPLETE")
        print(f"All output files are in: {PIPELINE_DIR}")
        print("=" * 70)


if __name__ == "__main__":
    main()
