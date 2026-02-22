---
name: oc-nano-pdf
description: Edit PDF files using natural language instructions. Use this skill when the user asks to make specific textual or minor layout changes to a PDF document.
---

# Edit PDFs with Natural Language

This skill uses the `nano-pdf` command-line tool to apply edits to PDF documents based on natural language instructions.

## Installation

Before using the skill, ensure the `nano-pdf` tool is installed in the environment.

```shell
sudo pip3 install nano-pdf
```

## Usage

To edit a PDF, use the `nano-pdf edit` command, specifying the input file, the page number, and a quoted string describing the changes.

### Example

```shell
nano-pdf edit path/to/deck.pdf 1 "Change the title to 'Q3 Results' and fix the typo in the subtitle"
```

### Important Considerations

- **Page Indexing**: Page numbers can be either 0-based or 1-based depending on the tool's version. If an edit appears on the wrong page, try again with the page number adjusted by one.
- **Verification**: Always visually inspect the generated output PDF to confirm the edits were applied correctly before delivering the final result.
