---
name: slide-deck-preparation
description: "Convert raw content (URLs, articles, papers) into structured slide deck outlines. Extracts narratives, determines audience, plans chapters, assigns slide archetypes, and provides source citations."
metadata:
  dispatcher-category: analysis
  dispatcher-capabilities: slide-planning, narrative-extraction, content-structuring, archetype-assignment, source-citation
  dispatcher-accepted-intents: prepare_slide_deck, outline_presentation, draft_deck_structure, extract_presentation_narrative
  dispatcher-input-artifacts: raw_content, urls, documents, articles
  dispatcher-output-artifacts: slide_deck_outline, structured_narrative
  dispatcher-stack-tags: presentation, planning, content-strategy
  dispatcher-risk: low
  dispatcher-writes-files: false
  dispatcher-layer: execution
  dispatcher-lifecycle: active
  dispatcher-preferred-model: claude-sonnet-4-6
---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill slide-deck-preparation --intent <intent> --model <model_name> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# Slide Deck Preparation

> **Author:** jovd83 | **Version:** 1.0.0 | **License:** MIT

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![AgentSkills Standard](https://img.shields.io/badge/AgentSkills-Standard-green.svg)](https://agentskills.io)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)
[![Validate Skill](https://github.com/jovd83/slide-deck-preparation/actions/workflows/validate.yml/badge.svg)](https://github.com/jovd83/slide-deck-preparation/actions/workflows/validate.yml)

This skill transforms unstructured input material (articles, papers, transcripts, URLs) into a highly structured, presentation-ready slide deck outline with a specific number of slides. It ensures strong narrative flow and includes explicit source citations to prevent hallucinations and enable Human-in-the-Loop (HiTL) verification.

## Prerequisites & Context
When you trigger this skill, ensure you have the raw content. If the user provides URLs or files, use the appropriate tools to read and extract the text before beginning the deck preparation.

## Step-by-Step Workflow

1. **Ingest and Analyze:**
   - Read all provided input materials.
   - Identify the core thesis, the implied target audience, and the primary goal of the content.

2. **Establish the Narrative & Structure:**
   - Define the overarching Deck Title, Subtitle, and Description.
   - Formulate a clear "Narrative Arc" (how the story begins, develops, and concludes).
   - Create an Agenda divided into logical Chapters.

3. **Slide Allocation:**
   - Determine how to divide the story across the exact `[[Amount]]` of slides requested by the user.
   - Assign a specific "Slide Archetype" to each slide to dictate its visual and rhetorical structure. 
   - *Action:* Read `references/archetypes.md` to select the most appropriate archetype for each slide from the 50+ available options.

4. **Draft the Content:**
   - For each slide, write the Title, Subtitle, and Content (keep content concise, favoring bullet points over walls of text).
   - **CRITICAL:** Populate the `HiTL Reference & Sources` block for *every single slide*. Quote the exact source text or state where the information was derived from to ensure zero hallucinations.

5. **Format the Output:**
   - Present the final output using the exact structure defined in `assets/template.md`. Do not deviate from this layout.

## Examples

**Example 1: Preparing a 5-slide deck from a blog post**
*User Prompt:* "Turn this article about the future of remote work into a 5-slide deck for middle management."
*Action:* 
1. Analyze the article. Audience = Middle Management.
2. Structure 5 slides: Intro, Problem, Solution, Implementation, Conclusion.
3. Assign archetypes: 'The Big Thesis', 'Problem / Solution', 'Risk / Mitigation', 'The Roadmap', 'The Call to Action'.
4. Output using `assets/template.md`, citing specific paragraphs from the article in the HiTL section.

## Troubleshooting
- **Missing or Hallucinated Info:** If the user points out a hallucination, review the `HiTL Reference & Sources` block for that slide. If you cannot find a direct quote in the source text, remove or rewrite the slide content.
- **Wrong Number of Slides:** Ensure you explicitly count the slides during the "Slide Allocation" step to match the user's `[[Amount]]` exactly.
- **Vague Content:** If slides feel too generic, pick a more specific archetype from `references/archetypes.md` (e.g., switch from "General Point" to "Feature vs. Benefit" or "The Root Cause").
