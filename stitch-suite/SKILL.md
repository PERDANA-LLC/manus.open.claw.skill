---
name: stitch-suite
description: "A comprehensive suite of tools and best practices for UI/UX design, prompt engineering, and frontend development, adapted from Google Labs' Stitch Skills. Includes modules for design systems (design-md), prompt enhancement, React components, Remotion videos, shadcn/ui, and iterative site building (stitch-loop)."
---

# Stitch Suite - Design & Development Toolkit

This skill is a consolidated and adapted version of the six skills from the Google Labs `stitch-skills` repository. It provides a comprehensive toolkit for UI/UX design, prompt engineering, and frontend development, focusing on the principles and knowledge base from the original skills.

## When to Use This Skill

Reference this skill when you need to:
-   Create a design system document (`DESIGN.md`).
-   Enhance a vague UI prompt into a detailed, actionable one.
-   Build React components with best practices.
-   Generate a video walkthrough of a UI using Remotion.
-   Work with `shadcn/ui` components.
-   Iteratively build a website using a loop-based approach.

## Core Modules

This suite contains the knowledge and workflows from the following six modules:

### 1. Design System (`design-md`)

**Goal:** Analyze a UI and generate a `DESIGN.md` file that documents its design system in natural language.

**Workflow:**
1.  **Analyze the UI:** Examine the visual elements of the UI (colors, fonts, spacing, components).
2.  **Consult Resources:** Read `/home/ubuntu/skills/stitch-suite/resources/design-md/README.md` for the full methodology.
3.  **Generate `DESIGN.md`:** Create a new markdown file following the structure outlined in the resource file. Describe the visual theme, color palette, typography, component stylings, and layout principles.

### 2. Enhance Prompt (`enhance-prompt`)

**Goal:** Transform a vague UI idea into a polished, detailed prompt optimized for AI generation.

**Workflow:**
1.  **Identify Vague Prompt:** Recognize when a user's request is too high-level (e.g., "make a cool dashboard").
2.  **Consult Resources:** Read `/home/ubuntu/skills/stitch-suite/resources/enhance-prompt/KEYWORDS.md` for a library of descriptive UI/UX terms.
3.  **Rewrite the Prompt:** Enhance the prompt by adding specificity, incorporating keywords from the resource file, defining a clear structure, and injecting design system context.

### 3. React Components (`react-components`)

**Goal:** Convert UI designs into well-structured, production-ready React components.

**Workflow:**
1.  **Consult Resources:** Before writing any code, review the following files:
    *   `/home/ubuntu/skills/stitch-suite/resources/react-components/architecture-checklist.md`
    *   `/home/ubuntu/skills/stitch-suite/resources/react-components/component-template.tsx`
    *   `/home/ubuntu/skills/stitch-suite/resources/react-components/style-guide.json`
2.  **Write the Component:** Follow the architecture checklist, use the component template as a starting point, and adhere to the style guide.
3.  **Validate:** Ensure the component is well-typed, decouples data, and follows project-specific constraints.

### 4. Remotion Videos (`remotion`)

**Goal:** Generate a professional video walkthrough of a UI project using Remotion.

**Workflow:**
1.  **Gather Assets:** Collect screenshots of the UI screens to be featured in the video.
2.  **Consult Resources:** Read `/home/ubuntu/skills/stitch-suite/resources/remotion/composition-checklist.md` and `/home/ubuntu/skills/stitch-suite/resources/remotion/screen-slide-template.tsx`.
3.  **Create Remotion Project:** Set up a new Remotion project and create compositions based on the templates and checklist.
4.  **Render Video:** Use Remotion to render the final video file.

### 5. shadcn/ui (`shadcn-ui`)

**Goal:** Provide expert guidance for integrating and building applications with `shadcn/ui` components.

**Workflow:**
1.  **Consult Resources:** This module is primarily knowledge-based. Refer to the following files:
    *   `/home/ubuntu/skills/stitch-suite/resources/shadcn-ui/component-catalog.md`
    *   `/home/ubuntu/skills/stitch-suite/resources/shadcn-ui/customization-guide.md`
    *   `/home/ubuntu/skills/stitch-suite/resources/shadcn-ui/migration-guide.md`
    *   `/home/ubuntu/skills/stitch-suite/resources/shadcn-ui/setup-guide.md`
2.  **Advise the User:** Use the information in these guides to answer user questions, provide code examples, and guide them through `shadcn/ui` integration.

### 6. Iterative Build Loop (`stitch-loop`)

**Goal:** Iteratively build a website using an autonomous loop pattern.

**Workflow:**
1.  **Consult Resources:** Understand the "baton system" by reading:
    *   `/home/ubuntu/skills/stitch-suite/resources/stitch-loop/baton-schema.md`
    *   `/home/ubuntu/skills/stitch-suite/resources/stitch-loop/site-template.md`
2.  **Implement the Loop:**
    a.  Create a `next-prompt.md` file to act as the "baton."
    b.  In each iteration, read the prompt from the baton file.
    c.  Generate the requested UI page.
    d.  Integrate the new page into the site structure.
    e.  Update the baton file with the prompt for the *next* page to be built.
