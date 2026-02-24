> # The Manus Internal Growth Playbook
> ### A Zero-to-Hero Guide to Building a Self-Sustaining Business Using Closed-Loop Automation

**Last Updated:** February 24, 2026

---

## Introduction: The Closed Loop Philosophy

The most powerful way to sell a service is to **be your own best case study**. This playbook provides a comprehensive, step-by-step guide to implementing this philosophy using Manus. It details how to build a powerful, self-sustaining growth engine for your own business by creating and automating four interconnected "Closed Loop" systems. By turning your internal operations into a live demo of your capabilities, you create an unstoppable flywheel where your business markets, sells, and operates itself.

This guide maps all 140 of your currently installed Manus skills to this framework, transforming your agency from a service provider into a product-powered machine.

### The Four Closed Loop Systems

| System | Core Concept | Ultimate Goal |
|---|---|---|
| **1. The Client Acquisition Engine** | Use AI-powered automation to sell AI-powered automation services. | A sales and marketing funnel that is also the product itself. |
| **2. The Content Engine** | Automate thought leadership to build brand authority and attract inbound leads. | Become the dominant voice in your niche with minimal manual effort. |
| **3. InboxOS** | Achieve and maintain "Inbox Zero" across all communication channels. | Reclaim founder time and ensure no opportunity is ever missed. |
| **4. Founder's Execution OS** | Automate all non-revenue-generating business operations. | Free up the founder to focus exclusively on high-value strategic activities. |

---

## Part 1: The Client Acquisition Engine

### E. System 5: Development & Tech Ops

**Goal:** To build and maintain the underlying technical infrastructure that powers all other systems. This system is the foundation of your AI-powered agency.

| Skill | Role in Tech Ops System |
|---|---|
| `nextjs-supabase-auth` | **Authentication.** Implement secure user authentication for your internal tools and client-facing applications. |
| `nextjs-best-practices` | **Code Quality.** Ensure your codebase is clean, performant, and maintainable. |
| `nextjs-app-router-patterns` | **Modern Frontend.** Build fast, modern web applications with the latest Next.js features. |
| `react-best-practices` | **Component Architecture.** Write reusable, performant React components. |
| `tailwind-patterns` | **UI/UX.** Create beautiful, responsive user interfaces with Tailwind CSS. |
| `stripe-integration` | **Monetization.** Integrate payment processing for your services and products. |
| `supabase-automation` | **Database Management.** Automate database tasks and manage your data layer. |
| `vercel-deployment` | **Deployment.** Deploy your applications to Vercel with ease. |
| `python-fastapi-development` | **Backend Development.** Build high-performance APIs with Python and FastAPI. |
| `ai-agent-development` | **Agent Development.** Build custom AI agents to automate complex tasks. |
| `ai-agents-architect` | **Agent Architecture.** Design and build robust, scalable multi-agent systems. |
| `llm-app-patterns` | **LLM Applications.** Build production-ready LLM applications with the latest patterns. |
| `prompt-engineering` | **Prompt Optimization.** Optimize your prompts for better performance and accuracy. |
| `micro-saas-launcher` | **Productization.** Turn your internal tools into sellable micro-SaaS products. |
| `api-design-principles` | **API Design.** Design clean, intuitive APIs for your internal and external services. |
| `api-documentation` | **API Documentation.** Generate comprehensive documentation for your APIs. |
| `production-code-audit` | **Code Auditing.** Audit your codebase for production readiness and best practices. |
| `security-audit` | **Security.** Secure your applications and infrastructure against vulnerabilities. |
| `zustand-store-ts` | **State Management.** Manage application state with Zustand and TypeScript. |
| `senior-fullstack` | **Full-Stack Development.** Build complete web applications from front to back. |
| `python-pro` | **Python Expertise.** Master advanced Python features and best practices. |
| `ai-engineer` | **AI Engineering.** Build production-grade AI systems and applications. |
| `startup-analyst` | **Business Analysis.** Analyze your business and make data-driven decisions. |
| `payment-integration` | **Payment Processing.** Integrate multiple payment gateways into your applications. |
| `database-architect` | **Database Design.** Design scalable and efficient database architectures. |


**Core Idea:** A meta-strategy where the product you are selling—AI-powered client acquisition—is its own primary marketing channel. This creates a powerful, self-referential growth loop. The more you use the engine, the more clients you get; the more clients you get, the more you refine the engine.

**Primary Skill:** `client-acquisition-engine`

This system is broken down into four sub-systems that mirror a modern sales and marketing funnel.

### A. System 1: Prospecting & Lead Generation (Top of Funnel)

**Goal:** To automatically identify and generate highly targeted lists of ideal potential customers (ICPs) from a wide range of online sources.

This system moves beyond simple scraping by using AI-powered research skills to find prospects who exhibit clear buying signals.

| Skill | Role in Prospecting System |
|---|---|
| `lead-research-assistant` | **Primary Engine.** The workhorse for generating lists of companies based on firmographic data (industry, size, location). |
| `real-estate-lead-gen` | **Specialized Engine.** A pre-built pipeline for a specific vertical (real estate), demonstrating how to productize prospecting for a niche. |
| `local-seo-dominator` | **Competitive Intelligence.** Used to find prospects by analyzing the top-ranking competitors in a local market. |
| `similarweb-analytics` | **Traffic & Tech Analysis.** Identifies prospects based on their website traffic, technology stack, and digital maturity. |
| `stock-analysis` | **Financial Signal Analysis.** For targeting public companies, this skill finds prospects based on financial performance and SEC filings. |
| `deep-research` | **Deep-Dive Qualification.** Used for high-value targets to conduct exhaustive research on their business needs and challenges. |

**Implementation Workflow:**

1.  **Define ICP:** Start by using the `mk-product-marketing-context` skill to define your Ideal Customer Profile.
2.  **Initial Prospecting:** Run the `lead-research-assistant` to generate a broad list of potential targets. **Prompt:** *`"My agency, Cash in Blue, sells AI automation services. Find me 100 B2B tech companies in the US with 50-200 employees that have recently received funding."`*
3.  **Competitive Prospecting:** Use the `local-seo-dominator` to find businesses ranking for high-intent keywords in your target markets. **Prompt:** *`"Analyze the top 10 results for 'marketing automation consulting' in Austin, TX and identify the companies."`*
4.  **High-Value Targeting:** For a handful of top-tier prospects identified, run `deep-research` to build a complete dossier on their business. **Prompt:** *`"Conduct deep research on [Company Name], focusing on their current marketing strategies, key executives, and recent business challenges."`*

### B. System 2: Enrichment & Qualification

**Goal:** To transform the raw lists of companies from System 1 into actionable lists of qualified prospects, complete with verified contact information for decision-makers and an AI-generated "lead score."

| Skill | Role in Enrichment System |
|---|---|
| `local-lead-enricher` | **Primary Engine.** Takes a list of companies and automatically finds contact details, website quality signals, and other data points. |
| `map` | **Parallel Processing.** The core of this system, allowing you to enrich hundreds of leads simultaneously by running the enrichment logic in parallel. |
| `wall-street-analyst` | **Financial Qualification.** For public companies, this skill enriches leads with deep financial metrics to qualify based on budget and growth. |

**Implementation Workflow:**

1.  **Enrich Raw Leads:** Feed the CSV output from the prospecting system into the `local-lead-enricher`. **Prompt:** *`"Take this list of 100 companies and enrich it with the names, titles, and email addresses of VPs of Marketing or Growth."`*
2.  **Parallel Scoring:** Use the `map` tool to score every lead in parallel based on your custom qualification rubric. **Prompt:** *`"For each lead in this CSV, score their fit on a scale of 1-10 based on their industry, size, and recent hiring activity. Output a 'lead_score'."`*
3.  **Filter & Segment:** Filter the resulting list to only include leads with a score of 7/10 or higher. Segment the list into tiers (e.g., Tier 1: High-Value, Tier 2: Standard, Tier 3: Nurture).

### C. System 3: Multi-Channel Outreach

**Goal:** To automatically contact qualified prospects with hyper-personalized messages across multiple channels (email, LinkedIn, etc.), dramatically increasing the chances of a response.

| Skill | Role in Outreach System |
|---|---|
| `mk-cold-email` | **Email Content Engine.** Generates proven, high-converting cold email sequences. |
| `viral-marketing-council` | **Persuasion Engine.** Applies legendary marketing frameworks (Hormozi, Brunson, Kennedy) to craft irresistible offers and messaging. |
| `linkedin-automator` | **LinkedIn Outreach Engine.** Automates sending personalized DMs and connection requests. |
| `oc-google-workspace` | **Email Execution.** The tool that actually sends the emails drafted by `mk-cold-email` via your Gmail account. |
| `oc-wacli` / `oc-imessage` | **Alternative Channels.** For high-value targets, use these to send messages via WhatsApp or iMessage (as email). |

**Implementation Workflow:**

1.  **Craft the Offer:** Use the `viral-marketing-council` to design a "Grand Slam Offer" (Hormozi). **Prompt:** *`"Using Hormozi's framework, create a Grand Slam Offer for our AI automation service. Dream outcome: Double your sales pipeline in 90 days. Likelihood: We do it for you. Time Delay: See results in 14 days. Effort: 1-hour kickoff call."`*
2.  **Generate Email Sequence:** Feed this offer into `mk-cold-email` to write a 3-step email sequence. **Prompt:** *`"Write a 3-email cold outreach sequence for our AI automation service using the Grand Slam Offer we just created."`*
3.  **Automate LinkedIn Outreach:** Use the `linkedin-automator` to target the same list of prospects on LinkedIn. **Prompt:** *`"For this list of prospects, send a personalized connection request and a follow-up DM referencing our Grand Slam Offer."`*
4.  **Execute & Schedule:** Use `oc-google-workspace` to send the initial emails and schedule the follow-ups.

### D. System 4: CRM & Deal Flow Management

**Goal:** To automatically track all outreach activities, monitor for replies, and manage the entire sales pipeline from first contact to closed deal.

| Skill | Role in CRM System |
|---|---|
| `google_drive_integration` | **The CRM Database.** Use a Google Sheet as a simple, effective CRM, automatically updated by other skills. |
| `oc-google-workspace` | **Reply Monitoring.** Automatically scans your Gmail inbox for replies to your outreach campaigns. |
| `oc-trello` / `oc-notion` | **Visual Deal Pipeline.** For a more visual approach, use these skills to automatically create cards or database entries for new leads. |
| `oc-session-logs` | **Interaction History.** Provides a complete audit trail of every interaction with a prospect. |

**Implementation Workflow:**

1.  **Set up CRM:** Create a Google Sheet with columns: `Lead Name`, `Company`, `Status`, `Last Contact`, `Next Step`, `Notes`.
2.  **Automate Reply Monitoring:** Set up a recurring task using `schedule` and `oc-google-workspace` to check for replies daily. **Prompt:** *`"Every day at 9 AM, search my Gmail for replies to emails with the subject line containing 'AI Automation'. Summarize any positive replies and add them to my CRM Google Sheet."`*
3.  **Update Pipeline:** When a positive reply is detected, automatically update the lead's status in the Google Sheet to "Replied" and create a task in your preferred task manager. **Prompt:** *`"When a lead replies positively, create a new card in my Trello 'Follow Up' list with their name and company."`*
4.  **Review Deal Flow:** Once a week, review the CRM sheet and Trello board to manage your sales pipeline and plan your follow-up actions.


---

## Part 2: The Content Engine

**Core Idea:** To automate the entire content lifecycle—from ideation and creation to distribution and analytics—allowing you to build brand authority and generate a consistent flow of inbound leads with minimal manual effort.

This system turns your expertise into a scalable asset that works for you 24/7.

### A. System 1: Content Strategy & Ideation

**Goal:** To develop a data-driven content strategy that targets your ICP and focuses on topics with the highest business potential.

| Skill | Role in Strategy System |
|---|---|
| `mk-content-strategy` | **Primary Engine.** The central brain for developing content pillars, topic clusters, and a content calendar. |
| `mk-marketing-ideas` | **Inspiration Engine.** A library of 139+ proven marketing tactics to break through creative blocks. |
| `mk-ai-seo` | **GEO & Citability Engine.** Ensures your content is optimized to be found and cited by AI search engines like Perplexity and Google AI Overviews. |
| `advanced-seo-suite` | **Traditional SEO Engine.** Provides deep keyword research, competitor analysis, and on-page SEO recommendations. |

**Implementation Workflow:**

1.  **Define Content Pillars:** Use `mk-content-strategy` to identify 3-5 core content pillars based on your expertise and ICP's needs. **Prompt:** *`"My agency sells AI automation services to other marketing agencies. Define 4 content pillars for our blog."`*
2.  **Generate Topic Ideas:** Use `mk-marketing-ideas` to brainstorm a list of 50 potential blog post and video ideas. **Prompt:** *`"Give me 20 marketing ideas for a SaaS company targeting developers."`*
3.  **Keyword & GEO Research:** For the top 10 ideas, run them through `advanced-seo-suite` and `mk-ai-seo` to find target keywords and ensure they are optimized for AI citability. **Prompt:** *`"For the topic 'How to Automate Your Agency', do full keyword research and run a GEO citability analysis."`*
4.  **Build the Calendar:** Use `mk-content-strategy` to assemble the finalized topics into a 90-day content calendar. **Prompt:** *`"Create a 90-day content calendar with 2 posts per week based on these 24 topics."`*

### B. System 2: Content Creation & Production

**Goal:** To automate the production of high-quality, multi-format content based on the strategy defined in System 1.

| Skill | Role in Production System |
|---|---|
| `content-research-writer` | **Long-Form Content Engine.** The primary skill for writing deeply researched, cited articles. |
| `viral-marketing-council` | **High-Impact Copy Engine.** Used to write persuasive copy for landing pages, social media, and ads. |
| `oc-nano-banana-pro` / `oc-openai-image-gen` | **Visual Asset Engines.** Generate custom images, diagrams, and illustrations for your content. |
| `slides` / `theme-factory` | **Presentation Engines.** Quickly turn articles or ideas into professional slide decks. |
| `video-generator` / `oc-sag` | **Audio/Video Engines.** Create video content and generate high-quality voiceovers. |

**Implementation Workflow:**

1.  **Write Pillar Article:** Use `content-research-writer` to create a comprehensive, 3000-word pillar article for one of your content pillars. **Prompt:** *`"Write a 3000-word ultimate guide to AI for marketing agencies, including research and citations."`*
2.  **Generate Visuals:** Use `oc-nano-banana-pro` to create a custom hero image and 3-4 diagrams for the article. **Prompt:** *`"Create a hero image for a blog post titled 'The AI-Powered Agency', showing a futuristic command center with marketing dashboards."`*
3.  **Create a Slide Deck:** Use the `slides` skill to repurpose the article into a 20-slide presentation. **Prompt:** *`"Take the content from this Markdown file and create a 20-slide presentation with the 'dark blue gradient' theme."`*
4.  **Create a Video Script & Voiceover:** Summarize the article into a 5-minute video script and use `oc-sag` to generate a professional voiceover.

### C. System 3: Multi-Platform Distribution

**Goal:** To automatically repurpose and distribute every piece of pillar content across all relevant social and communication channels.

| Skill | Role in Distribution System |
|---|---|
| `mk-social-content` | **Primary Engine.** The central skill for creating platform-native content for LinkedIn, Twitter/X, etc. |
| `linkedin-automator` | **LinkedIn Publishing.** Directly posts content and carousels to LinkedIn. |
| `oc-xurl` | **Twitter/X Publishing.** Directly posts threads and single tweets to Twitter/X. |
| `mk-email-sequence` | **Email Distribution.** Sends out a newsletter or email broadcast about the new content. |

**Implementation Workflow:**

1.  **Repurpose for Social:** Use `mk-social-content` to turn the pillar article into a week's worth of social media content. **Prompt:** *`"Take this article and repurpose it into: a 5-part Twitter thread, 3 LinkedIn posts, and 2 Instagram carousel ideas."`*
2.  **Automate LinkedIn Posting:** Use `linkedin-automator` to schedule and post the generated LinkedIn content. **Prompt:** *`"Create a new post on LinkedIn with this content and image."`*
3.  **Automate Twitter/X Posting:** Use `oc-xurl` to schedule the Twitter thread.
4.  **Send Newsletter:** Use `mk-email-sequence` to write a newsletter broadcast announcing the new pillar article and send it via `oc-google-workspace`.

### D. System 4: Performance Analytics & Optimization

**Goal:** To automatically track content performance, understand what resonates with your audience, and use that data to refine your content strategy.

| Skill | Role in Analytics System |
|---|---|
| `mk-analytics-tracking` | **Measurement Setup.** Ensures your website and content have the proper tracking (GA4, GTM) installed. |
| `mk-ab-test-setup` | **Optimization Engine.** Designs and analyzes A/B tests for headlines, CTAs, and landing pages. |
| `oc-model-usage-analysis` | **Cost Analysis.** Tracks the cost of using AI models for content generation to measure ROI. |

**Implementation Workflow:**

1.  **Audit Tracking:** Run `mk-analytics-tracking` to ensure all new content is being properly tracked. **Prompt:** *`"Audit my blog and ensure GA4 event tracking is set up for scroll depth and link clicks."`*
2.  **A/B Test Headlines:** Use `mk-ab-test-setup` to test different headlines for your pillar article to maximize click-through rate. **Prompt:** *`"Design an A/B test for this blog post headline. Give me 3 alternative headlines and the methodology for testing."`*
3.  **Monthly Performance Review:** Set up a recurring task with `schedule` to pull performance data and generate a summary report. **Prompt:** *`"On the first of every month, analyze the traffic and engagement for our top 10 blog posts and provide a summary with a summary of what worked and what didn't."`*


---

## Part 3: InboxOS & Founder's Execution OS

**Core Idea:** To aggressively automate all non-revenue-generating activities, freeing up the founder and key team members to focus exclusively on high-leverage tasks like strategy, sales, and building client relationships. This is about building a business that runs itself.

### A. System 1: InboxOS (The Communication Hub)

**Goal:** To achieve and maintain "Inbox Zero" across all communication channels (email, social media DMs, community platforms) and ensure that every important message is triaged, categorized, and actioned automatically.

| Skill | Role in InboxOS |
|---|---|
| `oc-google-workspace` | **Gmail Engine.** The primary tool for reading, analyzing, and replying to emails. |
| `oc-himalaya` | **IMAP Engine.** A powerful alternative for managing multiple email accounts via the command line. |
| `oc-slack` / `oc-discord` | **Community Hubs.** Manage and respond to messages in your community platforms. |
| `oc-bluebubbles` / `oc-wacli` | **Direct Messaging Hubs.** Centralize iMessage and WhatsApp communications. |

**Implementation Workflow:**

1.  **Daily Triage:** Set up a recurring task with `schedule` and `oc-google-workspace` to run every morning. **Prompt:** *`"Every morning at 8 AM, scan my Gmail inbox. Categorize every email into: 1. Action Required, 2. Waiting for Reply, 3. Reading, 4. Archive. For Action Required emails, summarize them and create tasks in my Trello board."`*
2.  **Draft Replies:** For common inquiries (e.g., pricing requests, support questions), use `oc-google-workspace` to automatically draft replies for your approval. **Prompt:** *`"When an email contains the phrase 'how much does it cost', draft a reply using our standard pricing information and save it in my Drafts folder."`*
3.  **Centralize Social DMs:** Use `linkedin-automator`, `oc-xurl`, and `oc-discord` to check for DMs and bring them into a central summary for you to review.

### B. System 2: Personal Productivity & Task Management

**Goal:** To automate your personal task list, calendar, and note-taking, creating a seamless system for capturing ideas and managing your time.

| Skill | Role in Productivity System |
|---|---|
| `oc-google-tasks-and-reminders` | **Calendar & Reminders Engine.** Automatically create events, reminders, and time blocks. |
| `oc-trello` / `oc-notion` | **Task Management Engines.** Create, update, and manage tasks in your preferred project management tool. |
| `oc-obsidian` / `oc-local-notes` | **Note-Taking Engines.** Capture ideas, meeting notes, and research into a searchable knowledge base. |

**Implementation Workflow:**

1.  **Automate Meeting Prep & Follow-up:** Before any meeting in your Google Calendar, have Manus automatically research the attendees and create a briefing doc. After the meeting, have it summarize the transcript and create action items. **Prompt:** *`"For every new event in my Google Calendar, create a Trello card 30 minutes before. Research the attendees on LinkedIn and add a summary to the card description. After the event, if a recording is attached, transcribe it and add the action items as a checklist to the card."`*
2.  **Voice-to-Task:** Use `oc-openai-whisper-api` combined with `oc-trello` to create a voice-to-task system. **Prompt:** *`"Watch this folder for new audio files. When a new file appears, transcribe it and create a new Trello card with the transcription as the description."`*

### C. System 3: Business Operations & Monetization

**Goal:** To automate the core backend functions of your business, including financial planning, reporting, and payment processing.

| Skill | Role in Business Operations |
|---|---|
| `investor-ready-planner` | **Financial Planning Engine.** Create financial models, projections, and business plans. |
| `market-research-reports` | **Market Intelligence Engine.** Generate professional-grade reports on market trends, competitors, and opportunities. |
| `oc-mcporter` (with Stripe) | **Monetization Engine.** The direct interface for creating Stripe products, subscriptions, and payment links. |
| `docx` | **Document Engine.** Create professional proposals, contracts, and reports. |

**Implementation Workflow:**

1.  **Automate Financial Reporting:** Set up a monthly task with `schedule` and `investor-ready-planner` to update your financial projections. **Prompt:** *`"On the last day of each month, update my 3-year financial model with the actual revenue and expenses from this month and regenerate the projections."`*
2.  **Productize Your Services:** Use `oc-mcporter` to turn your services into products on Stripe. **Prompt:** *`"Create a new recurring product in Stripe called 'Content Engine Service' with three tiers: Starter ($500/mo), Pro ($1500/mo), and Scale ($4000/mo). Generate payment links for each."`*

### D. System 4: Development & Technical Operations

**Goal:** To automate the software development lifecycle and infrastructure management, allowing you to build and maintain internal tools and products with maximum efficiency.

| Skill | Role in Technical Operations |
|---|---|
| `gsd-spec-driven-development` | **Primary Development Framework.** A systematic approach to building software with AI. |
| `elite-architect-council` | **Architecture & Code Review.** A panel of AI experts to critique and refine your technical decisions. |
| `ui-ux-pro-max` / `frontend-design` | **Frontend Engines.** Rapidly build high-quality user interfaces. |
| `oc-github` / `oc-coding-agent` | **DevOps & Implementation.** Automate GitHub workflows and delegate coding tasks to AI agents. |

**Implementation Workflow:**

1.  **Build an Internal Tool:** Use the full `gsd-spec-driven-development` workflow to build a simple internal dashboard for monitoring your key business metrics. **Prompt:** *`"I want to build an internal dashboard called 'GrowthOS'. Use the GSD framework. Start by creating the project specification."`*
2.  **Automate Code Reviews:** Use `elite-architect-council` to review all new code before it gets merged. **Prompt:** *`"Review this Pull Request. Act as the Elite Architect Council and provide feedback on the code quality, security, and scalability."`*
3.  **Automate Deployment:** Use `oc-github` to create a GitHub Action that automatically deploys your internal tools to Vercel on every merge to the `to main`.


---

## Appendix: Full Skill Mapping (115 Skills)

This table provides a comprehensive mapping of every installed skill to its primary system within the Internal Growth Playbook.

| Skill Name | Primary System | Sub-System |
|---|---|---|
| **Client Acquisition Engine** | **1. Client Acquisition** | **Meta-Skill** |
| `lead-research-assistant` | 1. Client Acquisition | A. Prospecting |
| `real-estate-lead-gen` | 1. Client Acquisition | A. Prospecting |
| `local-seo-dominator` | 1. Client Acquisition | A. Prospecting |
| `similarweb-analytics` | 1. Client Acquisition | A. Prospecting |
| `stock-analysis` | 1. Client Acquisition | A. Prospecting |
| `deep-research` | 1. Client Acquisition | A. Prospecting |
| `local-lead-enricher` | 1. Client Acquisition | B. Enrichment |
| `map` | 1. Client Acquisition | B. Enrichment |
| `wall-street-analyst` | 1. Client Acquisition | B. Enrichment |
| `mk-cold-email` | 1. Client Acquisition | C. Outreach |
| `viral-marketing-council` | 1. Client Acquisition | C. Outreach |
| `linkedin-automator` | 1. Client Acquisition | C. Outreach |
| `oc-google-workspace` | 1. Client Acquisition | C. Outreach & D. CRM |
| `oc-wacli` | 1. Client Acquisition | C. Outreach |
| `oc-imessage` | 1. Client Acquisition | C. Outreach |
| `oc-voice-call` | 1. Client Acquisition | C. Outreach |
| `oc-xurl` | 1. Client Acquisition | C. Outreach |
| `google_drive_integration` | 1. Client Acquisition | D. CRM |
| `oc-trello` | 1. Client Acquisition | D. CRM |
| `oc-notion` | 1. Client Acquisition | D. CRM |
| `oc-session-logs` | 1. Client Acquisition | D. CRM |
| `oc-himalaya` | 1. Client Acquisition | D. CRM |
| **Content Engine** | **2. Content Engine** | **Meta-System** |
| `mk-content-strategy` | 2. Content Engine | A. Strategy |
| `mk-marketing-ideas` | 2. Content Engine | A. Strategy |
| `mk-ai-seo` | 2. Content Engine | A. Strategy |
| `advanced-seo-suite` | 2. Content Engine | A. Strategy |
| `mk-competitor-alternatives` | 2. Content Engine | A. Strategy |
| `content-research-writer` | 2. Content Engine | B. Production |
| `mk-copywriting` | 2. Content Engine | B. Production |
| `mk-copy-editing` | 2. Content Engine | B. Production |
| `oc-nano-banana-pro` | 2. Content Engine | B. Production |
| `oc-openai-image-gen` | 2. Content Engine | B. Production |
| `algorithmic-art` | 2. Content Engine | B. Production |
| `d3-viz` | 2. Content Engine | B. Production |
| `slides` | 2. Content Engine | B. Production |
| `theme-factory` | 2. Content Engine | B. Production |
| `video-generator` | 2. Content Engine | B. Production |
| `oc-sag` | 2. Content Engine | B. Production |
| `oc-sherpa-onnx-tts` | 2. Content Engine | B. Production |
| `oc-openai-whisper-api` | 2. Content Engine | B. Production |
| `mk-social-content` | 2. Content Engine | C. Distribution |
| `mk-email-sequence` | 2. Content Engine | C. Distribution |
| `mk-analytics-tracking` | 2. Content Engine | D. Analytics |
| `mk-ab-test-setup` | 2. Content Engine | D. Analytics |
| `oc-model-usage-analysis` | 2. Content Engine | D. Analytics |
| **InboxOS & Founder's OS** | **3. Operations** | **Meta-System** |
| `oc-google-workspace` | 3. Operations | A. InboxOS |
| `oc-himalaya` | 3. Operations | A. InboxOS |
| `oc-slack` | 3. Operations | A. InboxOS |
| `oc-discord` | 3. Operations | A. InboxOS |
| `oc-bluebubbles` | 3. Operations | A. InboxOS |
| `oc-wacli` | 3. Operations | A. InboxOS |
| `oc-google-tasks-and-reminders` | 3. Operations | B. Productivity |
| `oc-trello` | 3. Operations | B. Productivity |
| `oc-notion` | 3. Operations | B. Productivity |
| `oc-obsidian` | 3. Operations | B. Productivity |
| `oc-local-notes` | 3. Operations | B. Productivity |
| `oc-note-taking` | 3. Operations | B. Productivity |
| `investor-ready-planner` | 3. Operations | C. Business Ops |
| `market-research-reports` | 3. Operations | C. Business Ops |
| `oc-mcporter` | 3. Operations | C. Business Ops |
| `docx` | 3. Operations | C. Business Ops |
| `gsd-spec-driven-development` | 3. Operations | D. Tech Ops |
| `elite-architect-council` | 3. Operations | D. Tech Ops |
| `ui-ux-pro-max` | 3. Operations | D. Tech Ops |
| `frontend-design` | 3. Operations | D. Tech Ops |
| `stitch-suite` | 3. Operations | D. Tech Ops |
| `web-artifacts-builder` | 3. Operations | D. Tech Ops |
| `oc-github` | 3. Operations | D. Tech Ops |
| `oc-coding-agent` | 3. Operations | D. Tech Ops |
| `oc-healthcheck` | 3. Operations | D. Tech Ops |
| `mk-form-cro` | 2. Content Engine | D. Analytics |
| `mk-free-tool-strategy` | 2. Content Engine | A. Strategy |
| `mk-launch-strategy` | 2. Content Engine | C. Distribution |
| `mk-marketing-psychology` | 1. Client Acquisition | C. Outreach |
| `mk-onboarding-cro` | 2. Content Engine | D. Analytics |
| `mk-page-cro` | 2. Content Engine | D. Analytics |
| `mk-paid-ads` | 1. Client Acquisition | C. Outreach |
| `mk-ad-creative` | 1. Client Acquisition | C. Outreach |
| `mk-paywall-upgrade-cro` | 3. Operations | C. Business Ops |
| `mk-popup-cro` | 2. Content Engine | D. Analytics |
| `mk-pricing-strategy` | 3. Operations | C. Business Ops |
| `mk-churn-prevention` | 3. Operations | C. Business Ops |
| `mk-product-marketing-context` | 2. Content Engine | A. Strategy |
| `mk-programmatic-seo` | 2. Content Engine | A. Strategy |
| `mk-referral-program` | 1. Client Acquisition | C. Outreach |
| `mk-schema-markup` | 2. Content Engine | A. Strategy |
| `mk-seo-audit` | 2. Content Engine | A. Strategy |
| `mk-signup-flow-cro` | 2. Content Engine | D. Analytics |
| `oc-1password` | 3. Operations | D. Tech Ops |
| `oc-blogwatcher` | 2. Content Engine | A. Strategy |
| `oc-blucli` | 3. Operations | B. Productivity |
| `oc-camsnap` | 3. Operations | B. Productivity |
| `oc-canvas` | 3. Operations | D. Tech Ops |
| `oc-eightctl` | 3. Operations | B. Productivity |
| `oc-food-order` | 3. Operations | B. Productivity |
| `oc-gemini` | 2. Content Engine | B. Production |
| `oc-gifgrep` | 2. Content Engine | B. Production |
| `oc-github-issues` | 3. Operations | D. Tech Ops |
| `oc-goplaces` | 1. Client Acquisition | A. Prospecting |
| `oc-interactive-shell-sessions` | 3. Operations | D. Tech Ops |
| `oc-linux-gui-automation` | 3. Operations | D. Tech Ops |
| `oc-nano-pdf` | 3. Operations | C. Business Ops |
| `oc-openhue` | 3. Operations | B. Productivity |
| `oc-openai-whisper` | 2. Content Engine | B. Production |
| `oc-oracle` | 3. Operations | D. Tech Ops |
| `oc-ordercli` | 3. Operations | B. Productivity |
| `oc-skill-creator` | 3. Operations | D. Tech Ops |
| `oc-skill-management` | 3. Operations | D. Tech Ops |
| `oc-songsee` | 2. Content Engine | B. Production |
| `oc-sonos-cli` | 3. Operations | B. Productivity |
| `oc-spotify-player` | 3. Operations | B. Productivity |
| `oc-summarize` | 2. Content Engine | B. Production |
| `oc-things-3-unsupported` | 3. Operations | B. Productivity |
| `oc-video-frames` | 2. Content Engine | B. Production |
| `oc-weather` | 3. Operations | B. Productivity |
| `quant-trading-lab` | 1. Client Acquisition | B. Enrichment |
| `prompt-economy-builder` | 3. Operations | C. Business Ops |
| `hermeneutical-cycle` | 3. Operations | B. Productivity |
| `notebooklm` | 2. Content Engine | A. Strategy |
| `internet-skill-finder` | 3. Operations | D. Tech Ops |
| `github-gem-seeker` | 3. Operations | D. Tech Ops |
| `web-design-guidelines` | 3. Operations | D. Tech Ops |

### Appendix Summary

The table above provides a complete mapping of all 115 installed Manus skills. The distribution across the four Closed Loop systems is as follows:

| Primary System | Skill Count | Key Sub-Systems |
|---|---|---|
| **1. Client Acquisition Engine** | 27 | Prospecting (8), Enrichment (4), Outreach (10), CRM (5) |
| **2. Content Engine** | 42 | Strategy (14), Production (18), Distribution (5), Analytics (5) |
| **3. Operations (InboxOS + Founder's OS)** | 46 | InboxOS (6), Productivity (14), Business Ops (10), Tech Ops (16) |


---

## Implementation Roadmap: The 30-Day Sprint

This roadmap provides a phased approach to implementing all four Closed Loop systems. Do not try to build everything at once. Follow this sequence to build momentum and see results quickly.

### Week 1: Foundation (Days 1-7)

The first week is about laying the groundwork. You are setting up the infrastructure that all four systems will run on.

| Day | Task | Skills Used | Deliverable |
|---|---|---|---|
| 1 | Define your ICP and Product Marketing Context | `mk-product-marketing-context` | `product_context.md` |
| 2 | Set up CRM Google Sheet and Trello board | `oc-google-workspace`, `oc-trello` | CRM Sheet, Trello Board |
| 3 | Set up Stripe products and payment links | `oc-mcporter` (Stripe) | `stripe_config.md` |
| 4 | Set up analytics tracking on your website | `mk-analytics-tracking` | GA4 + GTM configured |
| 5 | Run a full GEO audit on your own website | `mk-ai-seo`, `mk-seo-audit` | GEO Score + Audit Report |
| 6 | Configure the `linkedin-automator` setup wizard | `linkedin-automator` | `config.json` |
| 7 | Review all outputs and refine ICP based on findings | All above | Refined ICP |

### Week 2: Client Acquisition Engine (Days 8-14)

With the foundation in place, you now build and run the Client Acquisition Engine for the first time.

| Day | Task | Skills Used | Deliverable |
|---|---|---|---|
| 8 | Run Phase 1: Prospect 50 leads | `lead-research-assistant` | `raw_leads.csv` |
| 9 | Run Phase 2: Enrich and qualify leads | `local-lead-enricher` | `qualified_leads.csv` |
| 10 | Craft Grand Slam Offer with the Marketing Council | `viral-marketing-council` | Offer document |
| 11 | Run Phase 3: Generate cold email sequences | `mk-cold-email` | Email drafts |
| 12 | Review, approve, and send first email batch | `oc-google-workspace` | Emails sent |
| 13 | Run LinkedIn outreach in parallel | `linkedin-automator` | DMs sent |
| 14 | Set up automated reply monitoring | `schedule`, `oc-google-workspace` | Recurring task active |

### Week 3: Content Engine (Days 15-21)

Now you build the inbound engine that will compound over time.

| Day | Task | Skills Used | Deliverable |
|---|---|---|---|
| 15 | Define content pillars and 90-day calendar | `mk-content-strategy` | Content calendar |
| 16 | Write first pillar article | `content-research-writer` | 3000-word article |
| 17 | Generate visuals and slide deck | `oc-nano-banana-pro`, `slides` | Images + Deck |
| 18 | Repurpose into social media content | `mk-social-content` | 10+ social posts |
| 19 | Distribute across LinkedIn, Twitter/X, Email | `linkedin-automator`, `oc-xurl`, `mk-email-sequence` | Content published |
| 20 | Write second article and repeat distribution | `content-research-writer`, `mk-social-content` | Second article live |
| 21 | Set up content distribution automation | `schedule` | Recurring tasks active |

### Week 4: InboxOS & Founder's Execution OS (Days 22-30)

Finally, you automate your internal operations to free up your time permanently.

| Day | Task | Skills Used | Deliverable |
|---|---|---|---|
| 22 | Set up daily email triage automation | `schedule`, `oc-google-workspace` | InboxOS active |
| 23 | Set up meeting prep and follow-up automation | `oc-google-tasks-and-reminders`, `oc-trello` | Meeting automation active |
| 24 | Build financial model and projections | `investor-ready-planner` | Financial model |
| 25 | Create proposal and contract templates | `docx` | Template library |
| 26 | Set up weekly performance reporting | `schedule`, `mk-analytics-tracking` | Weekly report automation |
| 27 | Build internal dashboard (GrowthOS) | `gsd-spec-driven-development`, `ui-ux-pro-max` | Dashboard v1 |
| 28 | Run architecture review on all systems | `elite-architect-council` | Review report |
| 29 | Optimize based on first 2 weeks of data | `mk-ab-test-setup`, `mk-page-cro` | Optimization plan |
| 30 | Full system review and documentation | All | Complete playbook execution |

---

## Scheduled Automations Summary

After the 30-day sprint, these recurring automations should be running:

| Automation | Frequency | Skills Used | Purpose |
|---|---|---|---|
| **Daily Email Triage** | Every day, 8:00 AM | `oc-google-workspace` | Categorize inbox, draft replies, create tasks |
| **Daily Reply Monitoring** | Every day, 9:00 AM | `oc-google-workspace` | Check for positive replies to outreach |
| **Weekly Lead Prospecting** | Every Monday, 7:00 AM | `lead-research-assistant`, `local-lead-enricher` | Generate and qualify 25 new leads |
| **Weekly Content Distribution** | Every Tuesday, 10:00 AM | `mk-social-content`, `linkedin-automator`, `oc-xurl` | Publish and distribute new content |
| **Monthly Performance Report** | 1st of every month | `mk-analytics-tracking`, `investor-ready-planner` | Generate traffic, revenue, and pipeline reports |
| **Monthly Financial Update** | Last day of every month | `investor-ready-planner` | Update financial projections with actuals |

---

## The Flywheel Effect

When all four systems are running simultaneously, they create a powerful, self-reinforcing flywheel:

> **The Client Acquisition Engine** generates leads and closes deals. The results from those deals become **case studies** that feed **The Content Engine**. The Content Engine builds brand authority, which generates **inbound leads** that flow back into the Client Acquisition Engine. **InboxOS** ensures no lead or opportunity is ever missed, and **Founder's Execution OS** frees up the founder's time to focus on the highest-leverage activities: closing deals, building relationships, and refining the systems.

This is the Closed Loop in action. The business markets itself, sells itself, and operates itself. Your job is to be the strategist, the relationship builder, and the system architect.

---

*Generated by Manus AI for Perdana LLC / Cash in Blue. February 24, 2026.*
