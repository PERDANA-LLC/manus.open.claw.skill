---
name: linkedin-automator
description: Automates LinkedIn outreach and engagement. Use to send personalized DMs to connections, reply to messages, create posts, and send strategic connection requests. This skill uses browser automation to interact with the LinkedIn website.
---

# LinkedIn Automator

This skill automates LinkedIn outreach and engagement using browser automation. It can perform four core functions: sending personalized DMs to existing connections, replying to unread messages, creating content, and sending strategic connection requests.

## Workflow

This skill operates in a phase-based workflow. When triggered, first ask the user which of the four functions they want to perform. Then, proceed with the corresponding phase.

### Phase 1: Setup & Configuration (Run Once)

Before the first use, run a setup wizard to configure the user's profile, Ideal Customer Profile (ICP), and communication style. This information is stored in a central configuration file for all subsequent runs.

1.  **Check for Config:** Look for `/home/ubuntu/linkedin-automator/config.json`. If it doesn't exist, proceed with setup.
2.  **Gather Profile Info:** Ask the user for their name, company, role, and a brief bio.
3.  **Define ICP:** Ask the user to define their Ideal Customer Profile (job titles, industries, company sizes, keywords).
4.  **Define Voice:** Ask the user to describe their communication style (e.g., "casual and direct," "formal and professional").
5.  **Save Config:** Save all this information to `/home/ubuntu/linkedin-automator/config.json`.

### Phase 2: Choose a Function

Ask the user which of the following actions they want to take:

1.  **DM Connections:** Send personalized DMs to existing connections.
2.  **Answer DMs:** Reply to unread messages.
3.  **Create Post:** Generate a new LinkedIn post.
4.  **Connect with ICP:** Send new connection requests.

### Phase 3: Execute Function

Based on the user's choice, execute the corresponding sub-workflow.

#### A. DM Connections

1.  **Load Config:** Read the `config.json` file.
2.  **Navigate to Connections:** Use `browser_navigate` to go to `https://www.linkedin.com/mynetwork/invite-connect/connections/`.
3.  **Scrape Connections:** Scroll through the connections list and scrape the name and headline of each connection.
4.  **Filter by ICP:** Compare the scraped connections against the ICP criteria from `config.json`.
5.  **Generate Openers:** For each qualified connection, use the principles from `references/opener-patterns.md` to generate a personalized, 2-3 sentence opening message.
6.  **Get Approval:** Present each generated message to the user for approval before sending.
7.  **Send DMs:** Use browser automation to navigate to the messaging page for each approved connection and send the DM.
8.  **Track Outreach:** Log each sent DM in `/home/ubuntu/linkedin-automator/tracking/outreach_log.csv`.

#### B. Answer DMs

1.  **Load Config:** Read the `config.json` file.
2.  **Navigate to DMs:** Use `browser_navigate` to go to `https://www.linkedin.com/messaging/`.
3.  **Identify Unread:** Scrape the messaging inbox to identify unread conversations.
4.  **Read History:** For each unread conversation, click into it and read the full message history.
5.  **Generate Reply:** Use the principles from `references/dm-guidelines.md` and the user's defined voice to generate a contextual reply.
6.  **Get Approval:** Present each generated reply to the user for approval.
7.  **Send Reply:** Use `browser_input` to send the approved reply.
8.  **Track Replies:** Log each reply in `/home/ubuntu/linkedin-automator/tracking/dm_log.csv`.

#### C. Create Post

1.  **Load Config:** Read the `config.json` file.
2.  **Choose Template:** Ask the user to choose a post template from `references/post-templates.md` (e.g., Listicle, Story, Value Bomb).
3.  **Get Topic:** Ask the user for the core topic or idea for the post.
4.  **Generate Post:** Use the chosen template, the user's topic, and their defined voice to generate a complete LinkedIn post.
5.  **Get Approval:** Present the generated post to the user for edits and approval.
6.  **Post or Copy:** Ask the user if they want to post it directly via browser automation or copy the text to their clipboard.
7.  **Track Post:** Log the final post content in `/home/ubuntu/linkedin-automator/tracking/content_log.csv`.

#### D. Connect with ICP

1.  **Load Config:** Read the `config.json` file.
2.  **Navigate to Search:** Use `browser_navigate` to go to LinkedIn search.
3.  **Perform Search:** Use `browser_input` to enter the ICP keywords into the search bar and filter for "People."
4.  **Scrape Results:** Scroll through the search results and scrape the name, headline, and location of each person.
5.  **Filter and Approve:** Present the list of potential connections to the user for approval.
6.  **Send Requests:** For each approved person, navigate to their profile and click the "Connect" button. Optionally, add a personalized note based on their profile.
7.  **Track Connections:** Log each sent connection request in `/home/ubuntu/linkedin-automator/tracking/connections_log.csv`, being mindful of LinkedIn's weekly limits.

## Bundled Resources

- **`scripts/setup_wizard.py`**: A Python script to handle the initial configuration.
- **`references/`**: Contains the core logic and best practices adapted from the original repository for generating openers, replies, and posts.
- **`tracking/`**: A directory to store CSV logs of all outreach activities.
