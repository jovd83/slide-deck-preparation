---
name: slide-deck-preparation
description: "Convert raw content (URLs, articles, papers) into structured slide deck outlines. Extracts narratives, determines audience, plans chapters, assigns slide archetypes, and provides source citations."
metadata:
  dispatcher-category: analysis
  dispatcher-capabilities: slide-planning, narrative-extraction, content-structuring, archetype-assignment, source-citation, presentation-audit, strategic-scoring, narrative-enrichment, multimedia-injection
  dispatcher-accepted-intents: prepare_slide_deck, outline_presentation, draft_deck_structure, extract_presentation_narrative, audit_slide_deck, score_presentation, enrich_existing_slides, inject_storytelling_narrative
  dispatcher-input-artifacts: raw_content, urls, documents, articles, existing_slide_deck_markdown
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
> `%USERPROFILE%\.agents\skills\skill-dispatcher\log-dispatch.cmd --skill slide-deck-preparation --intent <intent> --model <model_name> --reason <reason>`

# Slide Deck Preparation

> **Author:** jovd83 | **Version:** 1.0.0 | **License:** MIT

This skill transforms unstructured input material (articles, papers, transcripts, URLs) into a highly structured, presentation-ready slide deck outline with a specific number of slides. It ensures strong narrative flow and includes explicit source citations to prevent hallucinations and enable Human-in-the-Loop (HiTL) verification.

## Prerequisites & Context

When you trigger this skill, ensure you have the raw content. If the user provides URLs or files, use the appropriate tools to read and extract the text before beginning the deck preparation.

## Step-by-Step Workflow

1. **Ingest and Analyze:**
   - Read all provided input materials (raw articles, URLs, or existing slide deck markdown).
   - Identify the core thesis, the implied target audience, and the primary goal of the content.

2. **Presentation Audit & Scoring (Capability 1):**
   - **Evaluate Existing Decks:** If the input is an existing deck, perform a deep audit against the **Strategy Scorecard** (0-10) using the criteria in `assets/template.md`.
   - **Identify Friction:** Pinpoint "Narrative Gaps" (where the story breaks) and "Visual Fatigue" points (where slides are too dense).
   - **Improvement Plan:** Generate a **Severity-Ranked Improvement Plan** focused on TED-style clarity and strategic impact. Document this in the `Revision History` section.

3. **Narrative Enrichment (Capability 2):**
   - **Inject Storytelling:** Add a "Storytelling Layer" to existing slides (e.g., introducing an overarching metaphor or a specific character journey).
   - **Multimedia Injection:** For every slide, suggest a "Pattern Break" using the **Mandatory Live Verification** protocol (verified YouTube/Vimeo clips).
   - **Visual Motif Alignment:** Update the `General Visual Motif` and `Avatar Hints` to ensure a consistent, premium aesthetic across the entire deck.

4. **Establish the Narrative & Structure (for New or Redone Decks):**
   - **MANDATORY HEADER:** You must generate a Deck Title, Subtitle, Target Audience, Goal, Narrative Arc, Key Takeaway, Number of Slides, Target Duration, Tone, Technical Level, Description, General Narrative, General Visual Motif, General Directions, Strategy Scorecard, Sources, and Source Summary. Use the exact labels from `assets/template.md`.
   - **General Narrative:** Define _how_ you will tell the story (e.g., "A journey from chaos to order," "A detective story uncovering a mystery").
   - **General Visual Motif:** Define the overarching visual theme (e.g., "A minimalist blueprint style with blueprint-blue accents"). Ensure all slide-level motifs are consistent with this.
   - **General Directions:** Provide guidance on avatar frequency (do not put the avatar on every single slide unless it's a character-driven story) and other delivery nuances.
   - **Strategy Scorecard:** Assign a score (0-10) to the following elements based on the deck's objectives:
     - _Storytelling_ (Facts structured as a narrative)
     - _Audience Focus_ (Value and clear takeaways)
     - _Minimalist Design_ (Uncluttered slides supporting the spoken word)
     - _Confident Delivery_ (Notes on body language/pauses)
     - _Single Clear Goal_ (One "North Star" message)
     - _Multimedia/Video_ (Pattern breaks)
     - _Interaction/Questions_ (Strategic engagement)
     - _Physical Props_ (Tangible demonstrations)
     - _Audience Activity_ (Re-energizing tasks)
   - _Note:_ For short presentations (<30m), pick only 1-2 interactive tools (Multimedia, Props, etc.) to avoid a "clown show" effect.

5. **Slide-by-Slide Authoring & Refinement:**
   - Determine how to divide the story across the exact `[[Amount]]` of slides requested by the user.
   - Assign a specific "Slide Archetype" to each slide to dictate its visual and rhetorical structure.
   - _Action:_ Read `references/archetypes.md` to select the most appropriate archetype and follow its structural template.

   - For each slide, write the Title, Subtitle, and Content (following the Archetype Template).
   - **VISUAL GUIDANCE (For Downstream Agents):**
     - **Visual Motif:** Define a specific visual metaphor or icon set (e.g., "A bridge connecting two silos").
     - **Key Labels:** List 1-5 words that MUST be rendered _on the slide_ as primary labels.
     - **Avatar Hint:** Suggest a pose/expression (e.g., "Avatar pointing at the bridge with a smile").
   - **EXPANDED EXPLANATION:** Every slide must include a **Detailed Logic & Speaker Notes** block.
     - **Full Explanation:** Provide a deep-dive paragraph into the slide's core message and general idea.
   - **CRITICAL:** Every slide must include a **References & Purpose** block.
     - **Source:** Provide the Full Name of the Paper/Article, Author/Organization, and a Direct URL.
     - **Purpose:** Explicitly state what the purpose of the slide is.
   - **MULTIMEDIA RESEARCH (Mandatory Live Verification):**
     - **DO NOT MARK AS VERIFIED WITHOUT A LIVE CHECK.** Claiming "Verified" for a link you haven't actively tested in the current session is a failure of this skill's integrity.
     - **PROCEDURE:** For every external link (YouTube, Vimeo, etc.), you MUST use a `browser_subagent` or `read_url_content` to confirm the video is active and matches the content description.
     - **LOGGING:** In the `Status` field, you must specify the verification method (e.g., `Verified active via browser_subagent on YYYY-MM-DD`).
     - If a link is dead, you MUST search for and verify a functional replacement before finalizing the deck.

6. **The Refinement Loop (Judge & Refine):**
   - **Phase 1: Self-Critique.** After the first draft, act as a "Judge." Review the deck against the Strategy Scorecard and TED Anti-Patterns.
   - **Phase 2: Document Improvements.** Fill out the `Revision History & Improvement Proposals` section in the metadata.
   - **Phase 3: Surgical Second Pass.** Re-write specific slides or metadata sections to address the critique (e.g., "Simplifying jargon on Slide 3" or "Aligning Slide 5 motif with the global theme").
   - **Final Check:** Ensure the `V2 Status` reflects that the improvements have been integrated.

7. **Self-Correction & Formatting:**
   - **Checklist:**
     - [ ] Does it have the exact slide count?
     - [ ] Is the Header complete (Goal, Narrative, Scorecard, Visual Motif, Sources, Summary, etc.)?
     - [ ] Does every slide have an Archetype, a clear Source, and a defined Purpose?
   - **Anti-Pattern Audit (TED Guidelines):**
     - **AVOID:** Taking too long to explain the topic; Orating vs. Talking; Self-importance; Jargon; Bullet point cramming; Lack of eye contact.
   - Present the final output using the exact structure defined in `assets/template.md`. Do not deviate from this layout.

## Examples

**Example 1: Preparing a 5-slide deck from a blog post**
_User Prompt:_ "Turn this article about the future of remote work into a 5-slide deck for middle management."
_Action:_

1. Analyze the article. Audience = Middle Management.
2. Structure 5 slides: Intro, Problem, Solution, Implementation, Conclusion.
3. Assign archetypes: 'The Big Thesis', 'Problem / Solution', 'Risk / Mitigation', 'The Roadmap', 'The Call to Action'.
4. Output using `assets/template.md`, citing specific paragraphs from the article in the HiTL section.

## Troubleshooting

- **Missing or Hallucinated Info:** If the user points out a hallucination, review the `HiTL Reference & Sources` block for that slide. If you cannot find a direct quote in the source text, remove or rewrite the slide content.
- **Wrong Number of Slides:** Ensure you explicitly count the slides during the "Slide Allocation" step to match the user's `[[Amount]]` exactly.
- **Vague Content:** If slides feel too generic, pick a more specific archetype from `references/archetypes.md` (e.g., switch from "General Point" to "Feature vs. Benefit" or "The Root Cause").

## Gotchas & Anti-Patterns

- **Lazy Verification:** **NEVER** mark a link as "Verified" if you haven't actively run a browser check in the current session. Link rot is the #1 cause of "Narrative Debt" in presentations.
- **The "Clown Show" Effect:** For presentations under 30 minutes, restrict yourself to **1-2 pattern breaks** (e.g., one video and one question). Over-indexing on props, activities, and media in a short briefing destroys authority.
- **Scorecard Inflation:** Do not give everything a 10/10. The Strategy Scorecard is a **diagnostic tool**, not a trophy. Use it to identify where the deck is "quiet" (e.g., low Interaction score) and calibrate accordingly.
- **Avatar Fatigue:** Unless the deck is a specific "Character Journey," avoid putting the avatar on more than 30% of the slides. In high-stakes briefings (e.g., SB-3), the avatar should only appear on transition or analysis slides.
- **Narrative Drift:** During the "Surgical Second Pass," ensure you don't overwrite the `General Narrative` intent. Refining a single slide should never break the overarching story arc.
- **Silent Dispatch:** Ensure every production-grade execution is logged via `%USERPROFILE%\.agents\skills\skill-dispatcher\log-dispatch.cmd`. Unlogged usage is invisible to the wallboard.
