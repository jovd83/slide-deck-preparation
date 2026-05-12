---
name: slide-deck-preparation
description: Convert source material into grounded, presentation-ready slide deck outlines. Use when Codex needs to plan, audit, restructure, or enrich a presentation from URLs, articles, papers, transcripts, notes, documents, or an existing deck outline, with explicit audience framing, narrative arc, slide archetypes, speaker notes, visual guidance, and source citations.
---

# Slide Deck Preparation

Use this skill to turn source material into a rigorous slide deck blueprint, not a finished PowerPoint file. The output is a structured Markdown outline that downstream agents, designers, or presentation tools can convert into slides.

## Core Contract

Produce a deck outline that is:

- Grounded in the provided sources, with citations on every substantive slide.
- Sized to the exact slide count requested by the user, or to a clearly stated default when the user does not specify one.
- Designed for a specific audience, goal, tone, technical level, and presentation duration.
- Organized around one narrative arc and one key takeaway.
- Practical for slide production, with slide archetypes, visual motifs, key labels, and speaker notes.

Read `assets/template.md` before finalizing output. Read `references/archetypes.md` when selecting slide structures.

## Inputs

Accept any combination of:

- URLs, articles, papers, transcripts, notes, pasted text, or uploaded documents.
- Existing deck outlines that need audit, restructuring, or enrichment.
- User constraints such as slide count, audience, duration, tone, brand direction, citation style, or required sections.

If critical information is missing, make a conservative assumption and state it briefly. Ask a question only when the missing choice would materially change the deck, such as investor pitch versus technical training.

## Workflow

1. Ingest the material.
   - Extract the thesis, evidence, important claims, entities, constraints, and source provenance.
   - Separate source-backed facts from inference, recommendation, and creative framing.
   - For URLs or external media, verify only with tools that are actually available in the current environment. Do not claim live verification without performing it in the current session.

2. Define the presentation brief.
   - Set target audience, goal, key takeaway, tone, technical level, duration, and narrative arc.
   - If the user did not specify slide count, choose a fit-for-purpose count and explain the assumption in the header.
   - Choose a single visual system that can carry the full deck without visual drift.

3. Build the slide architecture.
   - Allocate the exact number of slides across opening, development, proof, implications, and close.
   - Select archetypes from `references/archetypes.md`; adapt names only when needed for clarity.
   - Keep each slide to one primary job. Split overloaded slides instead of hiding several ideas under one title.

4. Draft the deck outline.
   - Use the labels and structure in `assets/template.md`.
   - Include every required global field.
   - For each slide, include title, subtitle, archetype, visual motif, key labels, avatar/character guidance when useful, content, detailed logic, speaker notes, and references/purpose.
   - Keep on-slide content concise. Put nuance in speaker notes and detailed logic.

5. Ground and verify.
   - Cite the source for each factual claim or cluster of claims.
   - Mark unavailable or unverified sources honestly.
   - If media is suggested, include verification status as one of: `Verified in current session`, `Not verified - tool unavailable`, `Not verified - user-provided candidate`, or `Search query only`.
   - Never fabricate URLs, papers, quotes, authors, dates, statistics, or verification results.

6. Judge and refine.
   - Score the deck with the strategy scorecard in the template.
   - Identify narrative gaps, audience mismatch, weak evidence, slide overload, jargon, and visual inconsistency.
   - Apply a second pass before final output. Record the critique and improvements in the revision history section.

## Existing Deck Audits

When the user provides an existing deck or outline, preserve useful structure but evaluate it directly:

- Diagnose strategic fit, narrative clarity, audience value, evidence quality, design density, and delivery readiness.
- Rank findings by severity.
- Provide a revised outline when asked, or an improvement backlog when the user only wants review.
- Avoid rewriting brand voice, claims, or data unless the source material supports the change.

## Memory Model

Use runtime memory only for the current deck task: source notes, slide allocation, open questions, and draft critique.

Use project-local memory only when the user explicitly asks to maintain reusable deck preferences inside the project, such as approved audience personas, brand notes, recurring citation sources, or house archetype rules. Store that information in an auditable project file chosen by the user.

Do not promote runtime notes to persistent memory automatically. Do not write shared cross-agent memory from this skill. If broader reuse is needed, treat shared memory as an external integration boundary and ask the user before promoting stable information.

## Guardrails

- Do not present a deck outline as finished design, exported slides, or legal/financial/medical advice.
- Do not overuse interaction, props, media, or avatars. For short executive decks, one or two pattern breaks is usually enough.
- Do not inflate scorecards. Scores are diagnostic signals, not decoration.
- Do not cite a source that does not support the slide's claim.
- Do not make every slide use the same layout or visual metaphor.
- Do not bury the main conclusion until the end unless the user explicitly wants a mystery or reveal structure.

## Output Rules

Return only the deck outline unless the user asks for analysis, a critique, or implementation notes.

Before finalizing, check:

- Exact slide count matches the request.
- Header fields are complete.
- Every slide has one purpose, one archetype, and at least one source or an explicit note that the slide is recommendation/inference.
- Source and media verification statuses are honest.
- The narrative arc and visual motif remain consistent from first slide to last.
