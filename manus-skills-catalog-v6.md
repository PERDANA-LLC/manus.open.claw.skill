# Manus Skill Catalog (v3.0)

**Version**: 3.0
**Last Updated**: March 1, 2026
**Total Skills**: 144

This catalog provides a comprehensive, skill-by-skill guide to every capability installed in your Manus environment. Each entry includes detailed instructions, trigger phrases, and example prompts to help you master the full power of Manus.

---

## 1. Video & Media Production

### 1.1 `remotion-best-practices`

- **How to Use**: This is your primary skill for any programmatic video creation using React and Remotion. When you have a Remotion project and need to implement a specific feature (like an animation, chart, or transition), this skill provides the domain-specific knowledge. It contains 37 rule files that act as a comprehensive knowledge base for Remotion development.
- **Trigger Phrases**: "remotion", "remotion project", "create a video in react", "programmatic video", "remotion animation", "remotion chart".
- **Example Prompt**: "*I'm working on a Remotion video and I need to add a smooth fade-in transition between two scenes. Can you show me the best way to do that and provide the code?*"

### 1.2 `remotion-best-practices` (stitch)

- **How to Use**: This is a specialized version of the Remotion skill, adapted from Google Labs' Stitch Skills. It's best used when you are working within the `stitch-suite` ecosystem for building complex, multi-component artifacts. It provides patterns that are optimized for the Stitch workflow.
- **Trigger Phrases**: "stitch suite remotion", "remotion video in stitch", "google labs stitch remotion".
- **Example Prompt**: "*I'm building an HTML artifact using the Stitch Suite and I want to embed a Remotion video component. How do I integrate it with the rest of my Stitch project?*"

### 1.3 `video-generator`

- **How to Use**: Use this skill for high-level, AI-driven video production. Instead of writing code, you describe the video you want (style, content, mood, length), and Manus will orchestrate AI tools to generate it. This is best for creative, non-programmatic video tasks.
- **Trigger Phrases**: "create a video", "make a short film", "generate a commercial", "AI video production", "cinematic video".
- **Example Prompt**: "*Generate a 30-second, high-energy commercial for a new sports drink. It should feature dynamic shots of athletes, upbeat music, and a powerful voiceover.*"

### 1.4 `oc-video-frames`

- **How to Use**: A simple utility for extracting specific frames from a video file. Provide the video file and the timestamp (or frame number) you want to extract. It uses `ffmpeg` in the background.
- **Trigger Phrases**: "extract a frame from this video", "get a thumbnail from this video", "save a snapshot from the video at 1:23".
- **Example Prompt**: "*I have a video file `~/Downloads/product_demo.mp4`. Can you extract a high-quality frame at the 45-second mark and save it as `thumbnail.png`?*"

### 1.5 `oc-openai-image-gen`

- **How to Use**: Your go-to skill for generating images from text prompts using OpenAI's DALL-E models. Be descriptive in your prompt, specifying the subject, style (e.g., "photorealistic", "anime", "impressionist"), composition, and any other details.
- **Trigger Phrases**: "generate an image of", "create a picture of", "dall-e image", "photorealistic image of".
- **Example Prompt**: "*Generate a photorealistic image of an astronaut riding a horse on Mars. The style should be epic and cinematic, with a detailed background of the Martian landscape.*"

### 1.6 `oc-nano-banana-pro`

- **How to Use**: This skill uses Google's Gemini Pro for advanced image generation and editing. It excels at complex compositions, multi-image editing, and understanding nuanced, descriptive prompts. Use this for more artistic or complex image tasks.
- **Trigger Phrases**: "gemini pro image", "edit this image using gemini", "create a complex image composition", "nano banana image".
- **Example Prompt**: "*Create an image of a serene Japanese garden. In the foreground, there's a stone lantern. In the background, I want to see Mount Fuji. Now, edit the image to make it look like it was painted in the Ukiyo-e style.*"

---

## 2. AI & Machine Learning

### 2.1 `ai-engineer`

- **How to Use**: This is a proactive, high-level skill for building entire AI-powered applications. Use it when you have a goal that requires a full system, such as a chatbot, a RAG pipeline, or an intelligent agent. It will guide the entire process from architecture to deployment.
- **Trigger Phrases**: "build an AI application", "create a RAG system", "develop an intelligent agent", "production-ready LLM app".
- **Example Prompt**: "*I want to build a production-ready RAG pipeline for our company's internal knowledge base. Let's use the `ai-engineer` skill to design and implement it.*"

### 2.2 `ai-agent-development`

- **How to Use**: This skill focuses specifically on the development workflow for autonomous agents and multi-agent systems. It provides patterns for using frameworks like CrewAI and LangGraph. Use it when you want to build an agent that can perform tasks independently.
- **Trigger Phrases**: "build an autonomous agent", "create a multi-agent system", "crewai agent", "langgraph workflow".
- **Example Prompt**: "*Let's build a research agent using CrewAI. It should be able to browse the web, read articles, and write a summary report on a given topic.*"

### 2.3 `ai-agents-architect`

- **How to Use**: This skill is for designing the high-level architecture of AI agents. It focuses on the theoretical aspects: tool use strategies, memory systems, planning algorithms, and multi-agent orchestration. Use it at the beginning of a project to lay a solid foundation.
- **Trigger Phrases**: "design an AI agent architecture", "agent memory system", "multi-agent orchestration plan", "tool use strategy for agent".
- **Example Prompt**: "*I need to design the architecture for a complex AI agent that will manage my calendar and emails. What is the best approach for its memory system and planning capabilities?*"

### 2.4 `llm-app-patterns`

- **How to Use**: This skill provides a library of production-ready patterns for common LLM application components. Use it when you are building a specific part of an LLM app and want to follow best practices, such as for a RAG pipeline, an agent architecture, or monitoring.
- **Trigger Phrases**: "llm app pattern", "rag pipeline best practices", "agent architecture pattern", "llmops monitoring".
- **Example Prompt**: "*I'm building a RAG pipeline. What is the best pattern for handling document chunking and embedding?*"

### 2.5 `prompt-engineering`

- **How to Use**: Your go-to skill for improving the quality of your prompts. Provide a prompt and a goal, and Manus will apply various techniques (e.g., chain-of-thought, few-shot learning, role-playing) to optimize it for better performance.
- **Trigger Phrases**: "improve this prompt", "prompt engineering", "optimize my prompt", "debug this prompt".
- **Example Prompt**: "*This prompt is not giving me the desired output. Can you help me re-engineer it for better accuracy and detail? Here is the prompt: ...*"

### 2.6 `prompt-economy-builder`

- **How to Use**: A meta-skill for building a business around digital products in the prompt economy. It covers everything from market research and prompt architecture to sales page copywriting and traffic generation. Use it when you want to monetize your prompting skills.
- **Trigger Phrases**: "build a prompt business", "sell prompts online", "prompt economy", "monetize my prompts".
- **Example Prompt**: "*I want to build a business selling high-quality prompts for marketers. Guide me through the process, from finding a niche to writing the sales page.*"

### 2.7 `elite-architect-council`

- **How to Use**: A powerful meta-skill for complex technical problems. It simulates a panel of 7 expert personas who recursively critique and refine a solution. Use it when you have a challenging coding or architecture task that requires multi-faceted analysis.
- **Trigger Phrases**: "elite architect council", "critique this architecture", "multi-faceted analysis of this code".
- **Example Prompt**: "*I've designed a new microservices architecture, but I'm concerned about security and scalability. Let's run it through the `elite-architect-council` for a thorough review.*"

### 2.8 `oc-gemini`

- **How to Use**: A direct interface to Google's Gemini models for quick, one-shot tasks like question-answering, summarization, or text generation within a Python environment. It's a utility skill for leveraging Gemini's power without a complex workflow.
- **Trigger Phrases**: "ask gemini", "summarize this with gemini", "gemini text generation".
- **Example Prompt**: "*Use Gemini to summarize the key points of this article: [URL].*"

---

## 3. Software Development — Frontend

### 3.1 `frontend-design`

- **How to Use**: Use this skill to generate high-quality, production-ready code for frontend components and pages. Describe the UI element you want, its style, and its functionality. It focuses on creating distinctive, polished designs.
- **Trigger Phrases**: "build a react component", "create a landing page design", "style this dashboard", "frontend UI design".
- **Example Prompt**: "*I need a beautiful, responsive hero section for my website. It should have a large headline, a call-to-action button, and a subtle background animation. Use a minimalist and modern style.*"

### 3.2 `ui-ux-pro-max`

- **How to Use**: This is your comprehensive UI/UX design assistant. It has a vast library of styles, palettes, fonts, and stacks. Use it for planning, building, reviewing, or refactoring any UI. It can provide code, design suggestions, or audit existing interfaces.
- **Trigger Phrases**: "ui/ux design", "choose a color palette", "find a font pairing", "review my UI code", "glassmorphism button".
- **Example Prompt**: "*I'm designing a new dashboard. I need a color palette, font pairing, and a layout for the main components. I'm using React and Tailwind CSS. I like the bento grid style.*"

### 3.3 `react-best-practices`

- **How to Use**: This skill contains performance optimization guidelines from Vercel Engineering. Use it when writing, reviewing, or refactoring React or Next.js code to ensure it's performant and follows modern best practices.
- **Trigger Phrases**: "react performance", "optimize my next.js app", "review my react code for best practices".
- **Example Prompt**: "*My Next.js app is loading slowly. Can you analyze the code and apply the `react-best-practices` to improve its performance?*"

### 3.4 `nextjs-app-router-patterns`

- **How to Use**: This skill is your expert guide to the Next.js App Router. Use it when you are implementing features like Server Components, streaming, parallel routes, or advanced data fetching patterns.
- **Trigger Phrases**: "next.js app router", "server components next.js", "parallel routes", "next.js data fetching".
- **Example Prompt**: "*I want to implement a parallel route in my Next.js 14 application to show a photo modal. Can you show me the correct file structure and code?*"

### 3.5 `nextjs-best-practices`

- **How to Use**: A focused skill on the core principles of the Next.js App Router, including Server Components, data fetching strategies, and routing patterns. It's a good starting point for any new Next.js project.
- **Trigger Phrases**: "next.js principles", "app router best practices", "server components data fetching".
- **Example Prompt**: "*What are the best practices for data fetching in Next.js Server Components? Should I use `fetch` or a library like SWR?*"

### 3.6 `tailwind-patterns`

- **How to Use**: This skill provides principles and patterns for Tailwind CSS v4. Use it when you are setting up a new project with Tailwind, creating a design token architecture, or using modern CSS features like container queries.
- **Trigger Phrases**: "tailwind css v4", "tailwind design tokens", "container queries tailwind".
- **Example Prompt**: "*I'm starting a new project with Tailwind CSS v4. How should I structure my `tailwind.config.js` file using the new CSS-first approach?*"

### 3.7 `zustand-store-ts`

- **How to Use**: Your go-to skill for creating state management stores in React using Zustand and TypeScript. It enforces best practices like separating state and actions and using the `subscribeWithSelector` middleware.
- **Trigger Phrases**: "zustand store", "react state management zustand", "global store with typescript".
- **Example Prompt**: "*Create a Zustand store for managing user authentication state in my React application. It should be written in TypeScript and use the `subscribeWithSelector` middleware.*"

### 3.8 `d3-viz`

- **How to Use**: Use this skill for creating complex, interactive data visualizations that go beyond standard charting libraries. Describe the data and the desired visualization (e.g., network diagram, geographic map, custom chart with animations).
- **Trigger Phrases**: "d3.js visualization", "interactive network graph", "custom svg chart", "d3 data viz".
- **Example Prompt**: "*I have a dataset of flight routes. I want to create an interactive geographic visualization using D3.js that shows the routes as arcs on a world map.*"

### 3.9 `algorithmic-art`

- **How to Use**: For creating generative or algorithmic art using p5.js. Describe the artistic concept you have in mind, such as flow fields, particle systems, or seeded randomness. The skill will generate original code to produce the artwork.
- **Trigger Phrases**: "algorithmic art", "generative art p5.js", "create art with code", "particle system animation".
- **Example Prompt**: "*Create a piece of algorithmic art using p5.js that generates a flow field with particles moving along the vectors. Use a Perlin noise algorithm for the field.*"

### 3.10 `web-artifacts-builder`

- **How to Use**: This skill is for building complex, multi-component HTML artifacts, especially for platforms like Claude.ai. It uses React, Tailwind CSS, and shadcn/ui. Use it when a simple, single-file HTML output is not sufficient.
- **Trigger Phrases**: "build a complex html artifact", "multi-component artifact", "shadcn/ui artifact".
- **Example Prompt**: "*I need to create an interactive HTML artifact that includes a sidebar for navigation, a main content area with tabs, and a modal dialog. Use the `web-artifacts-builder` with React and shadcn/ui.*"

### 3.11 `web-design-guidelines`

- **How to Use**: Use this skill to audit your UI code against established web design and accessibility guidelines. Ask it to "review my UI," "check accessibility," or "audit my design."
- **Trigger Phrases**: "review my ui", "check accessibility", "audit design", "review ux", "check my site against best practices".
- **Example Prompt**: "*Can you review the HTML and CSS for my login form and check it for accessibility issues and compliance with web design best practices?*"

### 3.12 `stitch-suite`

- **How to Use**: A comprehensive meta-skill from Google Labs for frontend development. It includes modules for design systems, prompt enhancement, React components, Remotion videos, and more. Invoke it when you want to use a battle-tested, integrated workflow for building UIs.
- **Trigger Phrases**: "stitch suite", "google labs stitch", "iterative site building", "stitch design system".
- **Example Prompt**: "*Let's build a new landing page using the iterative site building loop from the `stitch-suite` skill.*"

---

## 4. Software Development — Backend & Full-Stack

### 4.1 `senior-fullstack`

- **How to Use**: A high-level skill for building complete web applications. It covers the entire stack: React, Next.js, Node.js, GraphQL, and PostgreSQL. Use it to guide project scaffolding, code quality analysis, and architectural decisions.
- **Trigger Phrases**: "build a full-stack app", "senior fullstack guidance", "project scaffolding next.js postgresql".
- **Example Prompt**: "*I want to build a full-stack social media application. Guide me through the process using the `senior-fullstack` skill, from setting up the project to deploying it.*"

### 4.2 `python-pro`

- **How to Use**: This skill makes you an expert in modern Python (3.12+). Use it when you are writing Python code and want to leverage the latest features, async programming, performance optimizations, or tools like `uv`, `ruff`, and `pydantic`.
- **Trigger Phrases**: "python pro", "modern python features", "async python", "optimize python code", "pydantic model".
- **Example Prompt**: "*I have a synchronous Python script that is slow. Can you refactor it to use `asyncio` and modern Python features to improve its performance?*"

### 4.3 `python-fastapi-development`

- **How to Use**: Your go-to skill for building backend APIs with FastAPI. It provides patterns for async operations, SQLAlchemy integration, Pydantic models, authentication, and production-ready API design.
- **Trigger Phrases**: "fastapi backend", "python fastapi api", "sqlalchemy with fastapi", "fastapi authentication".
- **Example Prompt**: "*Build a secure REST API using FastAPI and SQLAlchemy for a blog platform. It needs endpoints for creating, reading, updating, and deleting posts, plus user authentication with JWT.*"

### 4.4 `database-architect`

- **How to Use**: A proactive skill for designing database systems from scratch. Use it at the beginning of a project to get expert advice on technology selection (SQL vs. NoSQL vs. TimeSeries), schema modeling, normalization, and migration planning.
- **Trigger Phrases**: "database architect", "design a database schema", "choose a database technology", "data modeling".
- **Example Prompt**: "*I'm building an e-commerce platform. As a `database-architect`, what database technology and schema would you recommend to handle products, customers, and orders at scale?*"

### 4.5 `api-design-principles`

- **How to Use**: Use this skill when designing or reviewing REST or GraphQL APIs. It provides principles for building intuitive, scalable, and maintainable APIs that developers will love to use.
- **Trigger Phrases**: "api design", "rest api best practices", "graphql schema design", "review my api spec".
- **Example Prompt**: "*I'm designing a new REST API. Can you review my OpenAPI specification and provide feedback based on the `api-design-principles`?*"

### 4.6 `api-documentation`

- **How to Use**: This skill automates the process of creating comprehensive API documentation. It can generate OpenAPI specs, create developer guides, and help you maintain your documentation over time.
- **Trigger Phrases**: "api documentation", "generate openapi spec", "create developer guide for api".
- **Example Prompt**: "*I have a FastAPI application. Can you generate a complete OpenAPI specification and a user-friendly developer guide for it?*"

### 4.7 `nextjs-supabase-auth`

- **How to Use**: A specialized skill for integrating Supabase authentication into a Next.js App Router project. It provides expert guidance on setting up the auth client, creating middleware for protected routes, and handling login/logout flows.
- **Trigger Phrases**: "supabase auth next.js", "next.js protected routes supabase", "supabase login middleware".
- **Example Prompt**: "*I need to add user authentication to my Next.js application using Supabase. Show me how to set up the auth helper and create a middleware to protect my dashboard route.*"

### 4.8 `supabase-automation`

- **How to Use**: This skill automates interactions with your Supabase project. It can manage database queries, tables, storage, edge functions, and execute raw SQL. It uses the Rube MCP (Composio) for secure and reliable automation.
- **Trigger Phrases**: "supabase automation", "run a query on supabase", "manage supabase storage", "execute sql on supabase".
- **Example Prompt**: "*I need to fetch all users from my Supabase `profiles` table who signed up in the last week. Use the `supabase-automation` skill to run the query and return the results.*"

### 4.9 `payment-integration`

- **How to Use**: A proactive, high-level skill for implementing payment processing. It handles checkout flows, subscriptions, webhooks, and PCI compliance for various processors like Stripe and PayPal.
- **Trigger Phrases**: "integrate payments", "set up subscriptions", "handle payment webhooks", "pci compliant checkout".
- **Example Prompt**: "*I need to add a payment system to my SaaS application. I want to offer monthly and yearly subscriptions. Guide me through the process using the `payment-integration` skill.*"

### 4.10 `stripe-integration`

- **How to Use**: A focused skill for implementing Stripe payments. Use it for building robust, PCI-compliant checkout flows, managing subscriptions, and handling Stripe webhooks.
- **Trigger Phrases**: "stripe integration", "stripe checkout", "stripe subscriptions", "stripe webhooks".
- **Example Prompt**: "*I want to integrate Stripe Checkout into my Next.js application. Provide the frontend and backend code for creating a checkout session and handling the success and cancel URLs.*"

---

## 5. Software Development — DevOps & Tooling

### 5.1 `vercel-deployment`

- **How to Use**: This skill provides expert knowledge for deploying Next.js applications to Vercel. It handles the configuration, build process, and deployment steps. Simply state your intent to deploy to Vercel.
- **Trigger Phrases**: "deploy to vercel", "vercel deployment", "host on vercel", "production deployment next.js".
- **Example Prompt**: "*I have finished developing my Next.js application, and now I want to deploy it to production on Vercel. Please guide me through the process.*"

### 5.2 `production-code-audit`

- **How to Use**: A powerful skill that autonomously performs a deep, line-by-line audit of an entire codebase. It understands architecture and patterns, then systematically refactors the code to a production-grade, professional quality, including optimizations. Use this for major code overhauls.
- **Trigger Phrases**: "audit my codebase", "production code audit", "refactor to production quality", "deep scan my code".
- **Example Prompt**: "*My project has grown quickly and the code quality has suffered. I need you to perform a `production-code-audit` to refactor the entire codebase to meet corporate-level professional standards.*"

### 5.3 `gsd-spec-driven-development`

- **How to Use**: This skill implements the "Get-Shit-Done" (GSD) framework for systematic, AI-assisted coding. Use it when you want to build a software project with a structured approach of planning, execution, and verification. It's ideal for building new features or entire projects from scratch.
- **Trigger Phrases**: "spec-driven development", "gsd framework", "build a project systematically", "atomic task execution".
- **Example Prompt**: "*Let's build a new feature for my app using `gsd-spec-driven-development`. We'll start by defining the specification, then move to atomic execution and verification.*"

### 5.4 `security-audit`

- **How to Use**: This skill provides a comprehensive security auditing workflow. It covers web application testing (XSS, SQLi), API security, penetration testing, and vulnerability scanning. Use it to identify and fix security weaknesses in your applications.
- **Trigger Phrases**: "security audit", "penetration test", "vulnerability scan", "harden my application security".
- **Example Prompt**: "*I need a thorough `security-audit` of my web application. Please check for common vulnerabilities like cross-site scripting and SQL injection, and provide a report with recommendations.*"

### 5.5 `oc-github`

- **How to Use**: Your primary interface for interacting with GitHub repositories via the `gh` command-line tool. It can manage issues, pull requests, check CI runs, and perform API queries. It's best for targeted, command-line-based GitHub operations.
- **Trigger Phrases**: "check github pr status", "create a github issue", "list ci runs", "review a pull request".
- **Example Prompt**: "*Can you check the status of pull request #123 in the `my-org/my-repo` repository and let me know if the CI checks have passed?*"

### 5.6 `oc-github-issues`

- **How to Use**: A specialized, autonomous skill for resolving GitHub issues. It fetches an issue, spawns a sub-agent to implement a fix, opens a pull request, and then monitors and addresses any review comments. It's a powerful tool for automated bug fixing.
- **Trigger Phrases**: "fix this github issue", "automate fixing issue #45", "resolve github issues".
- **Example Prompt**: "*There is a bug reported in issue #78 of my repository. Please use the `oc-github-issues` skill to autonomously fix it and open a pull request.*"

---

## 6. SEO & Search Optimization

### 6.1 `advanced-seo-suite`

- **How to Use**: A comprehensive meta-skill with 19 functions for all aspects of SEO. Use it for in-depth keyword research, competitor analysis, content optimization, schema markup, and rank tracking. It's your all-in-one SEO toolkit.
- **Trigger Phrases**: "advanced seo", "seo toolkit", "keyword research for my niche", "competitor seo analysis".
- **Example Prompt**: "*I'm launching a new blog about AI. Use the `advanced-seo-suite` to perform comprehensive keyword research and identify content gaps I can target.*"

### 6.2 `mk-seo-audit`

- **How to Use**: Use this skill when you suspect your website has technical or on-page SEO issues. Ask for an "SEO audit" or ask "why am I not ranking?". It will perform a comprehensive check and provide actionable recommendations.
- **Trigger Phrases**: "seo audit", "technical seo review", "on-page seo check", "why am I not ranking?".
- **Example Prompt**: "*My website traffic has been declining. Please perform a full `mk-seo-audit` to diagnose any issues with my site's SEO health and provide a plan to fix them.*"

### 6.3 `mk-ai-seo`

- **How to Use**: This skill focuses on optimizing your content to be cited and ranked by AI search engines like ChatGPT and Google's AI Overviews. Use it to adapt your content strategy for the new era of "Answer Engine Optimization."
- **Trigger Phrases**: "ai seo", "answer engine optimization", "optimize for chatgpt", "get cited by ai".
- **Example Prompt**: "*I want my articles to be used as a source in AI-generated answers. How can I optimize my content using the `mk-ai-seo` skill to increase my chances of being cited?*"

### 6.4 `mk-programmatic-seo`

- **How to Use**: Use this skill when you want to create hundreds or thousands of SEO-driven pages at scale by combining templates with data. This is ideal for creating location pages, directory pages, or comparison pages.
- **Trigger Phrases**: "programmatic seo", "create pages at scale", "seo template pages", "location pages seo".
- **Example Prompt**: "*I have a list of 1,000 cities. I want to create a unique landing page for each one targeting the keyword 'best pizza in [city]'. Let's use `mk-programmatic-seo` to build this.*"

### 6.5 `mk-schema-markup`

- **How to Use**: This skill helps you add, fix, or optimize structured data (JSON-LD) on your site. This helps search engines understand your content better and can result in rich snippets. Mention the type of schema you need (e.g., FAQ, Product, Review).
- **Trigger Phrases**: "schema markup", "structured data", "json-ld for my page", "add faq schema".
- **Example Prompt**: "*My product page is missing structured data. Can you add `Product` schema markup using JSON-LD to include the price, rating, and availability?*"

### 6.6 `local-seo-dominator`

- **How to Use**: A meta-skill focused on competitive analysis for local SEO. It uses browser automation to analyze Google Business Profiles, perform local keyword research, and identify content gaps against your local competitors.
- **Trigger Phrases**: "local seo analysis", "google business profile competitor", "local keyword research".
- **Example Prompt**: "*I run a local plumbing business. Use the `local-seo-dominator` to analyze my top 3 competitors on Google Maps and tell me how I can outrank them.*"

### 6.7 `mk-competitor-alternatives`

- **How to Use**: This skill helps you create high-intent landing pages that compare your product to your competitors. It supports various formats like "You vs. Competitor" or "Product Alternative" pages. This is a powerful strategy for capturing search traffic from users who are actively comparing solutions.
- **Trigger Phrases**: "competitor comparison page", "alternative to [competitor]", "[product] vs [competitor] page".
- **Example Prompt**: "*I want to create a landing page that targets people searching for 'Salesforce alternatives'. Use the `mk-competitor-alternatives` skill to research the top alternatives and create a comprehensive comparison page.*"

---

## 7. Marketing — Strategy & Growth

### 7.1 `mk-marketing-ideas`

- **How to Use**: Your go-to skill for brainstorming marketing strategies. It contains a library of 139 proven marketing approaches. Use it when you need inspiration or a structured set of ideas for how to grow your product.
- **Trigger Phrases**: "marketing ideas", "growth ideas", "how to market my product", "marketing tactics".
- **Example Prompt**: "*I've just launched a new mobile app for productivity. I need some creative `mk-marketing-ideas` to get my first 1,000 users.*"

### 7.2 `mk-marketing-psychology`

- **How to Use**: This skill applies psychological principles and mental models to your marketing. It contains a library of over 70 cognitive biases and behavioral science concepts. Use it to understand why people buy and to create more persuasive marketing campaigns.
- **Trigger Phrases**: "marketing psychology", "cognitive bias in marketing", "persuasion techniques", "consumer behavior".
- **Example Prompt**: "*I want to improve the copy on my pricing page. Apply some principles from `mk-marketing-psychology`, like the decoy effect or anchoring, to make the offer more compelling.*"


### 7.3 `mk-content-strategy`

- **How to Use**: Use this skill when you need to plan your content. It helps you decide what topics to write about, build a content calendar, and develop a strategy that drives traffic and generates leads.
- **Trigger Phrases**: "content strategy", "what should I write about?", "content ideas", "blog strategy", "content planning".
- **Example Prompt**: "*I'm launching a new blog for my SaaS product. Help me develop a `mk-content-strategy` with 20 topic ideas, a publishing schedule, and a plan for the first 3 months.*"

### 7.4 `mk-launch-strategy`

- **How to Use**: Use this skill when you are planning a product launch, feature announcement, or release. It covers phased launches, channel strategy, and building ongoing momentum.
- **Trigger Phrases**: "launch strategy", "product hunt launch", "feature release plan", "go-to-market strategy".
- **Example Prompt**: "*We're launching a new feature next month. Help me plan a phased `mk-launch-strategy` that includes a teaser campaign, a Product Hunt launch, and a follow-up email sequence.*"

### 7.5 `mk-pricing-strategy`

- **How to Use**: Get expert help with pricing decisions, packaging, and monetization. This skill covers pricing research, tier structure, freemium models, and willingness-to-pay analysis.
- **Trigger Phrases**: "pricing strategy", "pricing tiers", "freemium model", "how much should I charge?".
- **Example Prompt**: "*I'm not sure how to price my SaaS product. Use the `mk-pricing-strategy` skill to help me design a 3-tier pricing model with a freemium option.*"

### 7.6 `mk-referral-program`

- **How to Use**: Design and optimize a referral or affiliate program. This skill covers incentive structure, viral loop mechanics, and growth optimization.
- **Trigger Phrases**: "referral program", "affiliate program", "refer a friend", "viral loop".
- **Example Prompt**: "*I want to create a referral program for my app where users get a free month for each friend they refer. Help me design the program using `mk-referral-program`.*"

### 7.7 `mk-free-tool-strategy`

- **How to Use**: Plan and evaluate free tools for marketing purposes. This skill bridges engineering and marketing, helping you build calculators, generators, or interactive tools that attract leads.
- **Trigger Phrases**: "free tool for marketing", "engineering as marketing", "build a calculator for leads".
- **Example Prompt**: "*I want to build a free 'ROI Calculator' for my website to generate leads. Help me plan it using the `mk-free-tool-strategy` skill.*"

### 7.8 `mk-paid-ads`

- **How to Use**: Create, optimize, and scale paid advertising campaigns on Google Ads, Meta, and LinkedIn. This skill covers campaign strategy, audience targeting, ad copy, and performance optimization.
- **Trigger Phrases**: "paid ads", "ppc campaign", "google ads strategy", "meta ads", "linkedin ads".
- **Example Prompt**: "*I have a $5,000/month budget for paid ads. Help me create a `mk-paid-ads` strategy for Google Ads and Meta to drive signups for my SaaS product.*"

### 7.9 `mk-ad-creative`

- **How to Use**: Generate ad creative at scale. This skill helps you create headlines, descriptions, and full ad variations for any paid advertising platform, enforcing character limits.
- **Trigger Phrases**: "ad creative", "generate ad headlines", "bulk ad copy", "rsa headlines".
- **Example Prompt**: "*I need 15 headline variations and 5 description variations for my Google Responsive Search Ad campaign. Use the `mk-ad-creative` skill.*"

### 7.10 `mk-ab-test-setup`

- **How to Use**: Plan, design, or implement A/B tests and experiments. This skill helps you formulate hypotheses, define test parameters, and analyze results.
- **Trigger Phrases**: "a/b test", "split test", "experiment design", "test this change".
- **Example Prompt**: "*I want to test whether a green or blue CTA button converts better on my landing page. Help me set up the `mk-ab-test-setup` with proper hypothesis and sample size calculations.*"

### 7.11 `mk-analytics-tracking`

- **How to Use**: Set up, improve, or audit your analytics tracking implementation. This skill covers GA4, Google Tag Manager, conversion tracking, UTM parameters, and event tracking.
- **Trigger Phrases**: "analytics tracking", "set up ga4", "google tag manager", "conversion tracking", "utm parameters".
- **Example Prompt**: "*I just launched a new website and I need to set up analytics. Help me implement GA4 tracking with custom events for button clicks and form submissions using `mk-analytics-tracking`.*"

### 7.12 `mk-email-sequence`

- **How to Use**: Create or optimize email sequences, drip campaigns, and automated flows. This skill designs email strategies that nurture leads and drive conversions.
- **Trigger Phrases**: "email sequence", "drip campaign", "welcome email series", "nurture sequence", "onboarding emails".
- **Example Prompt**: "*I need a 7-email welcome sequence for new subscribers to my newsletter. Each email should build trust and lead to a product demo signup. Use the `mk-email-sequence` skill.*"

### 7.13 `mk-social-content`

- **How to Use**: Create, schedule, or optimize social media content for LinkedIn, Twitter/X, Instagram, TikTok, and Facebook. This skill covers content creation, repurposing, and platform-specific strategies.
- **Trigger Phrases**: "social media content", "linkedin post", "twitter thread", "content calendar", "social scheduling".
- **Example Prompt**: "*I have a new blog post. Help me repurpose it into a LinkedIn post, a Twitter thread, and an Instagram carousel using `mk-social-content`.*"

### 7.14 `mk-product-marketing-context`

- **How to Use**: Capture and maintain a central document that defines your product's positioning, target audience, messaging, and competitive landscape. This document is then used by other marketing skills to ensure consistency.
- **Trigger Phrases**: "product marketing context", "define my positioning", "marketing context document".
- **Example Prompt**: "*Before we start any marketing work, let's define my `mk-product-marketing-context`. My product is an AI-powered writing assistant for legal professionals.*"

### 7.15 `mk-churn-prevention`

- **How to Use**: Reduce customer churn by designing cancel flows, save offers, dunning processes, and proactive retention strategies. This skill covers both voluntary and involuntary churn.
- **Trigger Phrases**: "churn prevention", "cancel flow", "save offer", "dunning", "failed payment recovery", "retention strategy".
- **Example Prompt**: "*Our churn rate is too high. Help me design a `mk-churn-prevention` strategy that includes an optimized cancel flow with save offers and a dunning sequence for failed payments.*"

### 7.16 `viral-marketing-council`

- **How to Use**: A meta-skill that invokes a panel of 7 marketing legends (Alex Hormozi, Gary Vee, Russell Brunson, Dan Kennedy, Eugene Schwartz, Seth Godin, Ryan Deiss) to generate high-converting, viral-ready marketing content and strategies.
- **Trigger Phrases**: "viral marketing council", "marketing legends panel", "hormozi style offer".
- **Example Prompt**: "*I need to create a viral marketing campaign for my new online course. Activate the `viral-marketing-council` and let each expert weigh in on the strategy.*"

### 7.17 `micro-saas-launcher`

- **How to Use**: Expert guidance for launching small, focused SaaS products fast — the indie hacker approach. It covers idea validation, MVP development, pricing, launch strategies, and growing to profitability.
- **Trigger Phrases**: "micro saas", "indie hacker", "launch a small saas", "mvp development".
- **Example Prompt**: "*I have an idea for a micro-SaaS tool that automates invoice reminders. Help me validate the idea and plan the MVP using the `micro-saas-launcher` skill.*"

### 7.18 `theme-factory`

- **How to Use**: A toolkit for styling any artifact (slides, docs, reports, HTML pages) with a professional theme. It includes 10 pre-set themes with curated colors and fonts.
- **Trigger Phrases**: "apply a theme", "style this document", "theme factory", "professional theme".
- **Example Prompt**: "*I've created a slide deck, but it looks plain. Apply the 'Corporate Blue' theme from the `theme-factory` to make it look professional.*"

---

## 8. Marketing — Conversion & Optimization

### 8.1 `mk-page-cro`

- **How to Use**: Use this skill to optimize conversions on any marketing page. It analyzes your page's structure, copy, and design to identify friction points and provide actionable recommendations.
- **Trigger Phrases**: "cro", "conversion rate optimization", "this page isn't converting", "improve conversions on this page".
- **Example Prompt**: "*My pricing page has a high bounce rate. Can you perform a `mk-page-cro` analysis and tell me what's wrong and how to fix it?*"

### 8.2 `mk-signup-flow-cro`

- **How to Use**: Specifically designed to optimize signup, registration, and trial activation flows. It identifies drop-off points and reduces friction in the account creation process.
- **Trigger Phrases**: "signup flow optimization", "reduce signup dropoff", "registration friction", "free trial signup".
- **Example Prompt**: "*Only 20% of users who start our signup process actually complete it. Use `mk-signup-flow-cro` to analyze the flow and suggest improvements.*"

### 8.3 `mk-onboarding-cro`

- **How to Use**: This skill optimizes the post-signup experience. It focuses on getting users to their "aha moment" as quickly as possible, improving activation rates and time-to-value.
- **Trigger Phrases**: "onboarding optimization", "user activation", "first-run experience", "aha moment".
- **Example Prompt**: "*Users are signing up but not completing the onboarding. Help me redesign the first-run experience using `mk-onboarding-cro` to improve activation.*"

### 8.4 `mk-form-cro`

- **How to Use**: Optimizes non-signup forms like lead capture, contact forms, demo requests, and checkout forms. It analyzes field-level data to reduce friction and increase completion rates.
- **Trigger Phrases**: "form optimization", "improve form completion rate", "reduce form friction".
- **Example Prompt**: "*Our 'Request a Demo' form has a very low completion rate. Use `mk-form-cro` to analyze it and suggest improvements.*"

### 8.5 `mk-popup-cro`

- **How to Use**: Create or optimize popups, modals, overlays, slide-ins, and banners for conversion purposes. It covers exit-intent popups, email capture, and announcement banners.
- **Trigger Phrases**: "popup optimization", "exit intent popup", "email capture popup", "modal design".
- **Example Prompt**: "*I want to create an exit-intent popup that offers a 10% discount to visitors who are about to leave. Design it using `mk-popup-cro`.*"

### 8.6 `mk-paywall-upgrade-cro`

- **How to Use**: Create or optimize in-app paywalls, upgrade screens, and upsell modals. This skill focuses on converting free users to paid users at the moment they experience value.
- **Trigger Phrases**: "paywall optimization", "upgrade screen", "upsell modal", "convert free to paid".
- **Example Prompt**: "*I need to design an in-app upgrade screen that appears when a free user tries to access a premium feature. Use `mk-paywall-upgrade-cro` to make it compelling.*"

### 8.7 `similarweb-analytics`

- **How to Use**: Analyze any website using SimilarWeb traffic data. It provides traffic metrics, engagement stats, global rankings, traffic sources, and geographic distribution. It's great for competitive intelligence.
- **Trigger Phrases**: "similarweb analysis", "website traffic data", "competitor traffic analysis".
- **Example Prompt**: "*I want to understand how much traffic my competitor gets. Please run a `similarweb-analytics` analysis on their website and compare it to mine.*"

### 8.8 `oc-model-usage-analysis`

- **How to Use**: This skill analyzes and summarizes your AI model cost and usage data from provider dashboards like OpenAI and Anthropic. Use it to understand your spending and optimize your AI costs.
- **Trigger Phrases**: "ai model usage", "openai spending", "anthropic costs", "model usage analysis".
- **Example Prompt**: "*I want to understand how much I'm spending on OpenAI API calls. Please run an `oc-model-usage-analysis` and break down the costs by model.*"

---

## 9. Marketing — Content & Copywriting

### 9.1 `mk-copywriting`

- **How to Use**: This is your primary skill for generating marketing copy from scratch. Use it for any page on your website, from the homepage to feature pages. Provide the target audience, the goal of the page, and any key messages you want to convey.
- **Trigger Phrases**: "write copy for", "improve this copy", "rewrite this page", "marketing copy", "headline help", "cta copy".
- **Example Prompt**: "*I need to write the copy for a new landing page for my project management tool. The target audience is small business owners. The goal is to get them to sign up for a free trial. Please write a compelling headline, sub-headline, and three feature sections.*"

### 9.2 `mk-copy-editing`

- **How to Use**: Use this skill when you have existing copy that needs to be reviewed and improved. It performs a systematic, multi-pass edit to check for clarity, tone, grammar, and persuasiveness. It's like having a professional copy editor on call.
- **Trigger Phrases**: "edit this copy", "review my copy", "copy feedback", "proofread this", "polish this text".
- **Example Prompt**: "*I've written a draft of an email to announce our new feature. Can you please perform a `mk-copy-editing` pass on it to make it more impactful and error-free? Here is the draft: ...*"

### 9.3 `content-research-writer`

- **How to Use**: This skill is for creating high-quality, long-form content like blog posts and articles. It combines research, writing, and real-time feedback. It can help you conduct research, add citations, improve hooks, and iterate on outlines.
- **Trigger Phrases**: "write a blog post about", "research and write an article on", "content research writer", "long-form content".
- **Example Prompt**: "*I want to write a comprehensive blog post about the history of artificial intelligence. Use the `content-research-writer` to help me research the key milestones, find credible sources, and structure the article.*"

### 9.4 `docx`

- **How to Use**: Your go-to skill for working with professional Microsoft Word documents (.docx). It can create new documents, edit existing ones, work with tracked changes, add comments, and preserve complex formatting. It's essential for any professional document workflow.
- **Trigger Phrases**: "create a docx file", "edit this word document", "add tracked changes to this doc", "extract text from this docx".
- **Example Prompt**: "*I have a proposal in a .docx file. I need you to review it, add comments with your feedback in several sections, and turn on tracked changes for any edits you make.*"

### 9.5 `market-research-reports`

- **How to Use**: A powerful meta-skill for generating comprehensive, professional-grade market research reports (50+ pages). It mimics the style of top consulting firms like McKinsey and BCG, using LaTeX for formatting and integrating deep research and strategic analysis frameworks (SWOT, PESTLE, etc.).
- **Trigger Phrases**: "generate a market research report", "mckinsey style report", "in-depth market analysis".
- **Example Prompt**: "*I need to understand the global market for electric vehicles. Please generate a full `market-research-report` covering market size, key players, growth drivers, and a 5-year forecast.*"

### 9.6 `notebooklm`

- **How to Use**: This skill connects Manus to your Google NotebookLM notebooks. Use it to ask questions and get source-grounded, citation-backed answers from your own documents. You can ask it to query specific notebooks or add new sources to your library.
- **Trigger Phrases**: "query my notebooklm", "ask my documents in notebooklm", "add this source to notebooklm".
- **Example Prompt**: "*I have a NotebookLM library with all my research on quantum computing. Please query it and explain the concept of quantum superposition, citing the sources from my library.*"

### 9.7 `hermeneutical-cycle`

- **How to Use**: A specialized skill for in-depth, recursive Bible study. It uses the Hermeneutical Cycle framework, integrating with Strong's Concordance and a Christological lens. Use it for deep theological research or to study a biblical topic from the ground up.
- **Trigger Phrases**: "hermeneutical cycle", "deep bible study", "study this biblical topic", "recursive bible analysis".
- **Example Prompt**: "*I want to do a deep study on the concept of 'grace' in the New Testament. Please use the `hermeneutical-cycle` to analyze the relevant passages, consult Strong's Concordance for the original Greek words, and provide a summary of your findings.*"

---

## 10. Sales, Leads & Outreach

### 10.1 `lead-research-assistant`

- **How to Use**: This is your starting point for any lead generation effort. It analyzes your business and product, then searches for companies that fit your ideal customer profile. It provides not just a list of companies, but actionable contact strategies.
- **Trigger Phrases**: "find leads for my business", "prospecting assistant", "identify target companies", "lead research".
- **Example Prompt**: "*I have a new B2B SaaS product that helps with inventory management. Use the `lead-research-assistant` to identify 50 e-commerce companies in the fashion industry that could be good potential customers.*"

### 10.2 `local-lead-enricher`

- **How to Use**: After you have a list of potential leads (especially local businesses), use this skill to enrich that list with contact data (emails, phone numbers) and quality signals. It helps you qualify the leads sourced by `lead-research-assistant`.
- **Trigger Phrases**: "enrich this lead list", "find contact info for these companies", "qualify local leads".
- **Example Prompt**: "*I have a list of 50 local restaurants. I need you to enrich this list by finding the owner's name, email address, and a link to their menu for each one.*"

### 10.3 `ai-lead-gen-engine`

- **How to Use**: A powerful, 3-step AI engine for finding and reaching your target audience. It builds audience avatars, discovers where they congregate online (blogs, newsletters, forums), and then generates partnership outreach playbooks. It's a strategic tool for finding non-obvious marketing channels.
- **Trigger Phrases**: "ai lead gen engine", "find my audience online", "audience avatar", "partnership outreach playbook".
- **Example Prompt**: "*My target audience is indie game developers. Use the `ai-lead-gen-engine` to discover the top 10 newsletters and blogs they read, and then create an outreach plan for securing sponsorships.*"

### 10.4 `client-acquisition-engine`

- **How to Use**: An end-to-end, autonomous pipeline for client acquisition. It chains together four other skills (`lead-research-assistant`, `local-lead-enricher`, `mk-cold-email`, `oc-google-workspace`) to find leads, enrich them, send personalized cold emails, and track replies in a Google Drive CRM. It's a fully automated sales machine.
- **Trigger Phrases**: "client acquisition engine", "automate my sales outreach", "end-to-end lead generation".
- **Example Prompt**: "*Activate the `client-acquisition-engine`. My target is law firms with 10-50 employees in New York City. I want to send them a personalized cold email about my document management software.*"

### 10.5 `mk-cold-email`

- **How to Use**: Use this skill to write effective B2B cold emails and follow-up sequences that get replies. It covers all aspects of cold emailing: subject lines, opening lines, body copy, CTAs, and personalization at scale.
- **Trigger Phrases**: "write a cold email", "cold email sequence", "prospecting email template", "sales development email".
- **Example Prompt**: "*I need to write a 3-step cold email sequence to reach out to VPs of Marketing at SaaS companies. The goal is to book a demo for my new analytics tool. Please write the emails.*"

### 10.6 `linkedin-automator`

- **How to Use**: This skill automates your activity on LinkedIn to generate leads and build your network. It uses browser automation to send personalized DMs, create posts, and send strategic connection requests. You provide the strategy, and it executes.
- **Trigger Phrases**: "linkedin automation", "automate linkedin outreach", "send personalized dms on linkedin".
- **Example Prompt**: "*I want to connect with 50 project managers at tech companies on LinkedIn. Please send them a personalized connection request that mentions a mutual connection or interest.*"

### 10.7 `real-estate-lead-gen`

- **How to Use**: A specialized, automated pipeline for finding motivated seller leads for real estate agents. It can find FSBOs, expired listings, and pre-foreclosures in any US metro area, score them with AI, and deliver them to an agent's inbox.
- **Trigger Phrases**: "real estate leads", "find motivated sellers", "fsbo leads", "expired listing leads".
- **Example Prompt**: "*I'm a real estate agent in Austin, TX. Set up the `real-estate-lead-gen` pipeline to find me 10 new pre-foreclosure leads every week and email them to me.*"

### 10.8 `oc-xurl`

- **How to Use**: A command-line tool for interacting with the X (formerly Twitter) API. Use it to automate actions like posting tweets, sending DMs, searching for content, or managing followers. It requires you to have your X API credentials configured.
- **Trigger Phrases**: "post a tweet via api", "search twitter api", "send a dm on x", "xurl command".
- **Example Prompt**: "*I have a list of 10 quotes in a text file. Please use `oc-xurl` to schedule them to be posted as tweets, one every hour.*"

---

## 11. Business, Finance & Research

### 11.1 `investor-ready-planner`

- **How to Use**: A powerful meta-skill that acts as a McKinsey-level business consultant. It can build an entire investor-ready business plan, including market research, financial projections, a pitch deck, and a GTM strategy. Use it when you are preparing to raise funding.
- **Trigger Phrases**: "investor-ready business plan", "financial projections for startup", "create a pitch deck".
- **Example Prompt**: "*I need to prepare for a seed funding round. Use the `investor-ready-planner` to create a complete business plan and a 10-slide pitch deck for my AI-powered logistics company.*"

### 11.2 `startup-analyst`

- **How to Use**: A proactive skill for early-stage startup analysis. Use it to get expert help with market sizing (TAM/SAM/SOM), financial modeling, competitive analysis, and strategic planning. It's your co-founder for business strategy.
- **Trigger Phrases**: "startup analyst", "market sizing for my startup", "unit economics analysis", "competitive landscape".
- **Example Prompt**: "*As a `startup-analyst`, can you help me calculate the TAM, SAM, and SOM for my new vertical farming startup?*"

### 11.3 `stock-analysis`

- **How to Use**: Your primary tool for analyzing public companies and stocks. It can get company profiles, technical insights, price charts, insider holdings, and recent SEC filings. It provides a comprehensive overview for investment research.
- **Trigger Phrases**: "analyze this stock", "stock analysis for [ticker]", "company profile of [company]", "sec filings for [company]".
- **Example Prompt**: "*Please provide a complete `stock-analysis` for Apple (AAPL), including a price chart, a summary of their latest quarterly report, and any recent insider trading activity.*"

### 11.4 `wall-street-analyst`

- **How to Use**: A 10-function meta-skill for professional-grade investment analysis. It goes beyond `stock-analysis` to include DCF valuation, risk assessment, portfolio construction, and macroeconomic impact reports. Use it for deep, quantitative investment research.
- **Trigger Phrases**: "wall street analyst", "dcf valuation", "portfolio construction strategy", "quantitative stock analysis".
- **Example Prompt**: "*As a `wall-street-analyst`, please perform a Discounted Cash Flow (DCF) valuation for Microsoft (MSFT) and provide a recommendation based on the result.*"

### 11.5 `quant-trading-lab`

- **How to Use**: A 12-function meta-skill for quantitative finance and algorithmic trading. It covers advanced topics like time series forecasting, sentiment analysis, high-frequency trading (HFT), and reinforcement learning for trading. Use it to develop and backtest trading strategies.
- **Trigger Phrases**: "quantitative trading", "algorithmic trading strategy", "backtest a trading strategy", "mean reversion strategy".
- **Example Prompt**: "*I want to develop a pairs trading strategy for Google and Microsoft. Use the `quant-trading-lab` to analyze their historical price correlation and backtest the strategy over the last 5 years.*"

### 11.6 `deep-research`

- **How to Use**: This skill executes an autonomous, multi-step research process using the Google Gemini Deep Research Agent. It's ideal for complex topics that require synthesizing information from multiple sources. It takes longer (2-10 minutes) but produces a detailed, cited report.
- **Trigger Phrases**: "deep research on", "in-depth report on", "literature review of", "market analysis of".
- **Example Prompt**: "*Please conduct `deep-research` on the impact of quantum computing on cryptography and produce a detailed report with citations.*"

### 11.7 `internet-skill-finder`

- **How to Use**: Use this skill to discover new Agent Skills from verified GitHub repositories. If you need a capability that isn't currently installed, this skill can search for and recommend community-built skills.
- **Trigger Phrases**: "find a skill for", "search for skills", "discover new agent skills", "recommend a plugin for".
- **Example Prompt**: "*I need to work with Airtable. Can you use the `internet-skill-finder` to see if there is a Manus skill for interacting with the Airtable API?*"

### 11.8 `github-gem-seeker`

- **How to Use**: This skill searches GitHub for battle-tested, open-source solutions to common problems. Instead of reinventing the wheel, use this skill to find existing libraries or tools for tasks like file format conversion, media downloading, or web scraping.
- **Trigger Phrases**: "find a github library for", "open source tool for", "github gem seeker".
- **Example Prompt**: "*I need to convert a large number of HEIC images to JPEG. Use the `github-gem-seeker` to find a reliable, open-source command-line tool for this task.*"

### 11.9 `oc-goplaces`

- **How to Use**: A command-line tool for querying the Google Places API. Use it to find information about businesses and points of interest, including addresses, phone numbers, ratings, and reviews.
- **Trigger Phrases**: "find a place", "google places search", "reviews for [business]", "goplaces cli".
- **Example Prompt**: "*Find the top 3 highest-rated Italian restaurants within a 1-mile radius of the Empire State Building.*"

### 11.10 `oc-summarize`

- **How to Use**: A utility for getting a quick summary of text from various sources, including URLs, local files, and even YouTube videos (by extracting the transcript). It's perfect for getting the gist of a long document or video without reading the whole thing.
- **Trigger Phrases**: "summarize this article", "give me a summary of this pdf", "summarize this youtube video".
- **Example Prompt**: "*This YouTube video is an hour long. Can you please `oc-summarize` it for me so I can get the key takeaways in a few minutes? [URL]*"

---

## 12. Communication & Messaging

### 12.1 `oc-google-workspace`

- **How to Use**: Your primary interface for interacting with your Google Workspace account. It can manage Gmail, Google Calendar, and Google Drive. Use it to send emails, schedule events, or find files.
- **Trigger Phrases**: "send an email from my gmail", "create a google calendar event", "find a file in my google drive".
- **Example Prompt**: "*Please schedule a meeting with my team for tomorrow at 10 AM to discuss the Q3 roadmap. Send a Google Calendar invite to the following people: ...*"

### 12.2 `oc-himalaya`

- **How to Use**: A powerful command-line interface for managing your emails via IMAP/SMTP. It allows for advanced email workflows directly from the terminal, including searching, organizing, and composing messages with complex MIME types.
- **Trigger Phrases**: "himalaya email client", "manage email from terminal", "search my inbox via imap".
- **Example Prompt**: "*I need to find all emails from my boss in the last month that contain the word 'urgent'. Please use the `oc-himalaya` skill to search my inbox.*"

### 12.3 `oc-imessage`

- **How to Use**: This skill sends an iMessage or SMS by using the Gmail API to send a message to the recipient's phone number email gateway (e.g., 1234567890@txt.att.net). It will clarify to you that the message is being sent as an email.
- **Trigger Phrases**: "send an imessage to", "text my friend", "send an sms to".
- **Example Prompt**: "*Can you send a text to my wife saying I'm running late for dinner?*"

### 12.4 `oc-bluebubbles`

- **How to Use**: If you have a self-hosted BlueBubbles server, this skill allows you to send and manage iMessages directly. It supports texts, attachments, and tapback reactions. This provides a more native iMessage experience than `oc-imessage`.
- **Prerequisites**: A running BlueBubbles server and configured connection.
- **Trigger Phrases**: "send a bluebubbles message", "imessage via bluebubbles".
- **Example Prompt**: "*Send an iMessage to my group chat via BlueBubbles with a picture of my dog.*"

### 12.5 `oc-wacli`

- **How to Use**: A command-line interface for sending WhatsApp messages and searching your WhatsApp history. It requires a connection to your WhatsApp account.
- **Trigger Phrases**: "send a whatsapp message", "search my whatsapp history", "wacli".
- **Example Prompt**: "*Send a WhatsApp message to my project group saying that the meeting has been moved to 3 PM.*"

### 12.6 `oc-slack`

- **How to Use**: Your interface for interacting with your Slack workspace. It can send messages to channels or users, edit messages, react with emojis, and manage pins. It requires you to have the Slack integration configured.
- **Trigger Phrases**: "send a slack message", "post to the #general channel", "react to the last message in slack".
- **Example Prompt**: "*Please post an announcement in the #engineering channel on Slack that the new deployment is complete.*"

### 12.7 `oc-discord`

- **How to Use**: This skill allows you to interact with Discord, including sending messages to channels and managing server activities. It requires a configured Discord integration.
- **Trigger Phrases**: "send a discord message", "post in the discord announcements", "discord automation".
- **Example Prompt**: "*Send a welcome message to the newest member in our Discord server's #introductions channel.*"

### 12.8 `oc-voice-call`

- **How to Use**: This skill initiates an outbound voice call and delivers a spoken message using Twilio's Programmable Voice API. It's useful for notifications, alerts, or automated information delivery.
- **Prerequisites**: A configured Twilio account with API credentials.
- **Trigger Phrases**: "make a voice call", "send a spoken alert", "twilio voice call".
- **Example Prompt**: "*I need to send an urgent alert to our on-call engineer. Please initiate a `oc-voice-call` to their phone number and read the following message: 'Server CPU usage is at 95%. Please investigate immediately.'*"

### 12.9 `oc-google-tasks-and-reminders`

- **How to Use**: This skill uses the Google Calendar MCP integration to manage your tasks and reminders. You can ask it to create, list, or manage reminders that will then sync with your Google account.
- **Trigger Phrases**: "set a reminder", "create a google task", "what are my reminders for today?".
- **Example Prompt**: "*Please set a reminder for me to 'Call the doctor's office' tomorrow at 9 AM.*"

---

## 13. Automation & Operations — Productivity

### 13.1 `oc-notion`

- **How to Use**: This skill is your gateway to automating Notion. It can create and manage pages, databases, and blocks using the official Notion API. You can use it to build automated reporting dashboards, task managers, or content calendars directly in Notion.
- **Prerequisites**: A Notion integration token and the database/page IDs you want to interact with.
- **Trigger Phrases**: "notion automation", "create a notion page", "add to my notion database", "update notion page".
- **Example Prompt**: "*I have a new lead from a form submission. Please add a new entry to my 'Leads' database in Notion with the following information: Name, Email, and Company.*"

### 13.2 `oc-trello`

- **How to Use**: Automate your Trello workflows with this skill. It uses the Trello REST API to manage boards, lists, and cards. You can create new cards from emails, move cards between lists based on status changes, or generate reports from your boards.
- **Prerequisites**: A Trello API key and token.
- **Trigger Phrases**: "trello automation", "create a trello card", "move trello card to done", "get cards from my trello board".
- **Example Prompt**: "*When a customer support ticket is marked as 'resolved', I want to automatically move the corresponding Trello card from the 'In Progress' list to the 'Done' list.*"

### 13.3 `oc-obsidian`

- **How to Use**: This skill allows you to work with your Obsidian vault of plain Markdown notes. It uses the `notesmd-cli` to create, find, and modify notes. It's perfect for building a personal knowledge management system or a "second brain" that Manus can interact with.
- **Trigger Phrases**: "obsidian note", "search my obsidian vault", "create a new note in obsidian".
- **Example Prompt**: "*I just read an interesting article. Please create a new note in my Obsidian vault, title it with the article's name, and add a summary and a link to the original source.*"

### 13.4 `oc-local-notes`

- **How to Use**: A simple, file-based note-taking system within the agent's own file system. It's useful for jotting down temporary information, creating to-do lists, or saving text snippets during a task. It's less structured than Obsidian but always available.
- **Trigger Phrases**: "take a note", "create a local note", "search my local notes".
- **Example Prompt**: "*I'm getting a lot of information from this research. Please take a note of the following key statistics: ...*"

### 13.5 `oc-note-taking`

- **How to Use**: Similar to `oc-local-notes`, this is another simple, file-based system for managing notes in the sandbox. It provides a basic way to store and retrieve information when a more complex tool like Notion or Obsidian isn't needed.
- **Trigger Phrases**: "jot this down", "save this information as a note", "recall my note about".
- **Example Prompt**: "*Please save the user's feedback about the new UI design in a note for later review.*"

### 13.6 `oc-blogwatcher`

- **How to Use**: This skill monitors blogs and RSS/Atom feeds for new posts. You provide the URLs of the feeds you want to track, and it will notify you when new content is published. It uses the `blogwatcher` command-line tool.
- **Trigger Phrases**: "monitor this blog for updates", "watch this rss feed", "notify me of new posts from".
- **Example Prompt**: "*Please monitor the official Google AI blog and let me know whenever a new post is published. Summarize the post for me when it comes out.*"

### 13.7 `oc-coding-agent`

- **How to Use**: This skill delegates complex or iterative coding tasks to a specialized, interactive command-line coding agent like Codex, Claude, or Pi. Use it for building new features, refactoring large codebases, or any task that benefits from a conversational AI pair programmer.
- **Trigger Phrases**: "delegate this coding task", "start a coding agent session", "refactor this with an ai agent".
- **Example Prompt**: "*This is a complex refactoring task. Please delegate it to the `oc-coding-agent` to rewrite this legacy Java class into modern Python.*"

### 13.8 `oc-interactive-shell-sessions`

- **How to Use**: This is the standard way to manage long-running processes or interactive command-line tools. It allows you to start a process, send input to it, and view its output over time. It's essential for tasks like running web servers or interacting with REPLs.
- **Trigger Phrases**: "start an interactive session", "run this server in the background", "send input to this process".
- **Example Prompt**: "*Start a Python web server in an interactive shell session. Then, send a `curl` request to it from another session to verify it's running.*"

### 13.9 `oc-linux-gui-automation`

- **How to Use**: Use this skill to automate interactions with graphical user interfaces (GUIs) on Linux when no other API is available. It uses tools like `xdotool` to simulate mouse clicks, keyboard input, and window management. It's a last resort for automating legacy or desktop applications.
- **Trigger Phrases**: "automate this gui", "simulate a mouse click", "control a desktop application".
- **Example Prompt**: "*I need to automate data entry into a legacy desktop application that has no API. Please use `oc-linux-gui-automation` to open the app, navigate to the correct form, and input the data from this CSV file.*"

### 13.10 `oc-canvas`

- **How to Use**: This skill renders local HTML content in a web browser. Use it to display generated HTML files, create interactive web-based demos, or present data visualizations that you've created.
- **Trigger Phrases**: "display this html file", "render this html in the browser", "show me the web page".
- **Example Prompt**: "*I have generated an HTML report with interactive charts. Please display `report.html` using the `oc-canvas` skill so I can view it.*"

### 13.11 `oc-mcporter`

- **How to Use**: This is the primary skill for interacting with Model Context Protocol (MCP) servers. It uses the `manus-mcp-cli` utility to list and call tools provided by external services like Stripe or Google Calendar. It's the key to integrating Manus with other platforms.
- **Trigger Phrases**: "mcp tool", "call stripe api via mcp", "list google calendar tools".
- **Example Prompt**: "*Please use the `oc-mcporter` skill to list all the available tools on the `stripe` MCP server. Then, call the `create-customer` tool with the following details: ...*"

### 13.12 `oc-session-logs`

- **How to Use**: Use this skill to search your entire conversation history with Manus. If you need to recall something that was said in a previous session, this skill can find it for you.
- **Trigger Phrases**: "search my conversation history", "what did we talk about last week?", "find the message where I said".
- **Example Prompt**: "*Can you search our session logs and find the message where I gave you the API key for the weather service?*"

---

## 14. Automation & Operations — Smart Home & IoT

### 14.1 `oc-openhue`

- **How to Use**: Your command center for Philips Hue lights. It uses the OpenHue CLI to control lights, rooms, and scenes. You can turn lights on/off, change colors, adjust brightness, and activate scenes.
- **Prerequisites**: A configured Philips Hue Bridge on the local network.
- **Trigger Phrases**: "hue lights", "turn on the living room lights", "set the lights to blue", "activate the 'relax' scene".
- **Example Prompt**: "*It's getting dark. Please turn on the lights in the office and set them to a warm white color at 75% brightness.*"

### 14.2 `oc-sonos-cli`

- **How to Use**: Control your Sonos speakers from the command line. This skill can discover speakers, play/pause music, control the volume, and manage speaker groups.
- **Prerequisites**: Sonos speakers on the same local network.
- **Trigger Phrases**: "sonos", "play music on sonos", "group my sonos speakers", "volume up on the kitchen speaker".
- **Example Prompt**: "*Please play my 'Focus' playlist from Spotify on the office Sonos speaker and set the volume to 30%.*"

### 14.3 `oc-blucli`

- **How to Use**: This skill controls Bluesound and NAD audio players using the `blu` command-line tool. It supports device discovery, playback control, and speaker grouping.
- **Prerequisites**: Bluesound/NAD devices on the same local network.
- **Trigger Phrases**: "bluesound player", "control my nad amplifier", "blucli command".
- **Example Prompt**: "*Please discover the Bluesound players on my network and then start playing the 'Jazz Classics' playlist on the main living room player.*"

### 14.4 `oc-eightctl`

- **How to Use**: Manage your Eight Sleep smart bed with this skill. It can control the temperature of the pod, set alarms, and manage schedules.
- **Prerequisites**: An Eight Sleep account and configured credentials.
- **Trigger Phrases**: "eight sleep", "set the bed temperature", "eight sleep alarm".
- **Example Prompt**: "*It's almost bedtime. Please set my Eight Sleep pod to a temperature of -1 for the night.*"

### 14.5 `oc-camsnap`

- **How to Use**: This skill captures frames or short video clips from network-connected cameras that support RTSP or ONVIF protocols. It's useful for security monitoring or just checking in on a camera feed.
- **Prerequisites**: The RTSP/ONVIF URL and credentials for the camera.
- **Trigger Phrases**: "camera snapshot", "get a clip from my security camera", "camsnap".
- **Example Prompt**: "*Please take a snapshot from my front door camera and save it as `front_door.jpg`.*"

### 14.6 `oc-spotify-player`

- **How to Use**: Control your Spotify playback from the terminal using the `spotify_player` tool. It can search for songs, play/pause, skip tracks, and manage your queue.
- **Prerequisites**: A Spotify Premium account and configured credentials.
- **Trigger Phrases**: "spotify player", "play a song on spotify", "search spotify for".
- **Example Prompt**: "*Search for the song 'Bohemian Rhapsody' on Spotify and add it to my queue.*"

---

## 15. Automation & Operations — Media & Audio

### 15.1 `oc-openai-whisper`

- **How to Use**: This skill provides local, offline audio transcription using the OpenAI Whisper CLI. It's ideal for privacy-sensitive tasks as the audio file is processed entirely within the sandbox and never sent to an API.
- **Trigger Phrases**: "transcribe this audio locally", "offline transcription", "whisper cli".
- **Example Prompt**: "*I have a sensitive interview recorded as an MP3. Please use the `oc-openai-whisper` skill to transcribe it locally and save the text to a file.*"

### 15.2 `oc-openai-whisper-api`

- **How to Use**: This skill uses the official OpenAI Whisper API for cloud-based audio transcription. It's fast and highly accurate, making it a good choice for non-sensitive audio.
- **Prerequisites**: An OpenAI API key.
- **Trigger Phrases**: "transcribe this audio with whisper api", "openai transcription".
- **Example Prompt**: "*I have a recording of a meeting. Please transcribe it using the `oc-openai-whisper-api` for the highest accuracy.*"

### 15.3 `oc-sag`

- **How to Use**: This skill provides high-quality text-to-speech (TTS) using the ElevenLabs API, via a simple command-line tool called `sag`. It's great for generating voiceovers, creating audio clips, or giving Manus a voice.
- **Prerequisites**: An ElevenLabs API key.
- **Trigger Phrases**: "text to speech", "convert this text to audio", "elevenlabs tts", "sag command".
- **Example Prompt**: "*Please convert the following text into a natural-sounding audio file using the 'Rachel' voice from ElevenLabs: 'Welcome to the Manus AI podcast.'*"

### 15.4 `oc-sherpa-onnx-tts`

- **How to Use**: This skill provides local, offline text-to-speech using the sherpa-onnx engine. It's fast and works without an internet connection, making it ideal for privacy-sensitive tasks or generating audio in environments with no network access.
- **Trigger Phrases**: "local tts", "offline text to speech", "sherpa-onnx".
- **Example Prompt**: "*I need to generate an audio alert for a system that is offline. Please use `oc-sherpa-onnx-tts` to convert the text 'Warning: System offline' into a WAV file.*"

### 15.5 `oc-songsee`

- **How to Use**: This skill generates visual representations of audio files, such as spectrograms, mel spectrograms, and chromagrams. It's a tool for audio analysis, helping you "see" the frequency content of a sound.
- **Trigger Phrases**: "generate a spectrogram", "analyze this audio file visually", "songsee".
- **Example Prompt**: "*I have a recording of a bird call. Please use `oc-songsee` to generate a mel spectrogram so I can analyze its structure.*"

### 15.6 `oc-gifgrep`

- **How to Use**: A command-line tool for finding and processing GIFs. It can search providers like Tenor and Giphy, download GIFs, and even extract still frames or create sprite sheets from them.
- **Trigger Phrases**: "find a gif", "search for a gif about", "download a gif", "gifgrep".
- **Example Prompt**: "*Find a GIF of a cat typing on a keyboard and download it to my current directory.*"

---

## 16. Utilities & System

### 16.1 `skill-creator`

- **How to Use**: This is the master skill for creating or updating other skills. It provides a detailed, step-by-step guide to ensure that any new or modified skill is structured correctly and integrates properly with the Manus agent. **You MUST use this skill for any skill modification.**
- **Trigger Phrases**: "create a new skill", "update a skill", "improve a skill", "skill creator".
- **Example Prompt**: "*I want to create a new skill for interacting with the Hacker News API. Please guide me through the process using the `skill-creator`.*"

### 16.2 `oc-skill-creator`

- **How to Use**: An alternate version of the `skill-creator` skill. It provides the same function: guiding the user through the process of creating or updating skills.
- **Trigger Phrases**: (Same as `skill-creator`)
- **Example Prompt**: (Same as `skill-creator`)

### 16.3 `oc-skill-management`

- **How to Use**: This skill provides guidance on how to manage your installed skills. It explains how to list them, read their documentation, and use the `skill-creator` to make changes.
- **Trigger Phrases**: "manage my skills", "how do I see my skills?", "list all skills".
- **Example Prompt**: "*How can I see a list of all the marketing-related skills I have installed?*"

### 16.4 `oc-healthcheck`

- **How to Use**: This skill performs a security and risk assessment of the host environment. It can check firewall configurations, SSH hardening, software updates, and the overall security posture of the system.
- **Trigger Phrases**: "run a security health check", "system security audit", "check my firewall config".
- **Example Prompt**: "*Please perform a full `oc-healthcheck` on my system and report any potential security vulnerabilities or misconfigurations.*"

### 16.5 `oc-1password`

- **How to Use**: This skill helps you set up and use the 1Password command-line tool (`op`). It can guide you through signing in, enabling desktop app integration, and using `op` to read and inject secrets into your scripts and commands.
- **Trigger Phrases**: "1password cli", "setup 1password", "read a secret from 1password", "op command".
- **Example Prompt**: "*I need to use my OpenAI API key, which is stored in my 1Password vault. Please show me how to use the `op` command to inject it into an environment variable.*"

### 16.6 `oc-oracle`

- **How to Use**: This skill provides best practices for using the `oracle` command-line tool, which is used for bundling prompts and files to be sent to large language models. It covers engines, sessions, and file attachment patterns.
- **Trigger Phrases**: "oracle cli", "bundle files for llm", "oracle prompt".
- **Example Prompt**: "*I have a Python script and a CSV file. I want to send both to a language model for analysis. What is the best way to do this using the `oc-oracle` tool?*"

### 16.7 `oc-nano-pdf`

- **How to Use**: This skill allows you to make minor textual or layout edits to PDF files using natural language instructions. It's useful for quick fixes like correcting a typo or changing a date in a PDF document.
- **Trigger Phrases**: "edit this pdf", "change text in a pdf", "fix a typo in this pdf".
- **Example Prompt**: "*I have a PDF invoice, but the date is wrong. Can you please open `invoice.pdf` and change the date from '2025' to '2026'?*"

### 16.8 `oc-weather`

- **How to Use**: A simple utility to get the current weather and a forecast for any location. It uses `wttr.in` to provide a nicely formatted weather report in the terminal.
- **Trigger Phrases**: "what's the weather in", "weather forecast for", "is it going to rain today?".
- **Example Prompt**: "*What's the weather forecast for London for the next 3 days?*"

### 16.9 `oc-food-order`

- **How to Use**: This skill uses the `ordercli` command-line tool to quickly reorder a previous food order from Foodora or track the status of an active order.
- **Trigger Phrases**: "reorder my last foodora order", "track my food order", "foodora order status".
- **Example Prompt**: "*Please reorder my usual pizza from last Tuesday on Foodora.*"

### 16.10 `oc-ordercli`

- **How to Use**: The underlying command-line tool for `oc-food-order`. It can be used directly to check past Foodora orders and track active order status.
- **Trigger Phrases**: "ordercli", "check my foodora history".
- **Example Prompt**: "*Use `ordercli` to show me a list of my last 5 orders from Foodora.*"

### 16.11 `oc-things-3-unsupported`

- **How to Use**: This is an informational skill. It triggers when you ask to interact with the Things 3 to-do list application. It will inform you that this is not possible because Things 3 does not have a public API and its command-line tools are for macOS only.
- **Trigger Phrases**: "add a task to things 3", "connect to my things 3", "manage my things 3 list".
- **Example Prompt**: "*Can you add 'Buy milk' to my grocery list in Things 3?*"


---

## Category Summary

| Category | Skills | Key Capabilities |
|:---|:---:|:---|
| Video & Media Production | 6 | Remotion, AI video generation, image generation, frame extraction |
| AI & Machine Learning | 8 | LLM apps, RAG, agents, prompt engineering, Gemini |
| Frontend Development | 12 | React, Next.js, Tailwind, d3.js, UI/UX design, shadcn/ui |
| Backend & Full-Stack | 10 | Python, FastAPI, databases, APIs, Supabase, Stripe |
| DevOps & Tooling | 6 | Vercel, GitHub CI/CD, security audits, code quality |
| SEO & Search | 7 | Technical SEO, AI SEO, schema markup, local SEO, programmatic SEO |
| Marketing Strategy | 18 | Campaigns, launches, pricing, referrals, ads, email, social |
| Conversion Optimization | 8 | CRO, paywalls, popups, forms, signups, analytics |
| Content & Copywriting | 7 | Copy, editing, research writing, documents, reports |
| Sales & Outreach | 8 | Lead gen, cold email, LinkedIn, client acquisition, X/Twitter |
| Business & Finance | 10 | Investment analysis, trading, startups, deep research, places |
| Communication | 9 | Gmail, WhatsApp, iMessage, Slack, Discord, voice calls |
| Productivity Automation | 12 | Notion, Trello, Obsidian, MCP, coding agents, GUI automation |
| Smart Home & IoT | 6 | Hue, Sonos, Bluesound, Eight Sleep, cameras, Spotify |
| Media & Audio | 6 | Whisper transcription, TTS, spectrograms, GIFs |
| Utilities & System | 11 | Skill management, security, 1Password, PDF editing, weather |
| **Total** | **144** | |

---

*This catalog is auto-generated from the `/home/ubuntu/skills/` directory. To add new skills, use the `skill-creator` or `internet-skill-finder` skills.*
