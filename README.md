# slide-deck-preparation

[![version](https://img.shields.io/badge/version-1.1.0-blue)](CHANGELOG.md)
[![status](https://img.shields.io/badge/status-production--ready-brightgreen)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Validate Skill](https://github.com/jovd83/slide-deck-preparation/actions/workflows/validate.yml/badge.svg)](https://github.com/jovd83/slide-deck-preparation/actions/workflows/validate.yml)

An AgentSkill for converting raw source material into grounded, presentation-ready slide deck outlines.

The skill helps an AI agent plan decks from articles, URLs, papers, transcripts, notes, documents, or existing deck outlines. It produces a structured Markdown blueprint with audience framing, narrative arc, slide-by-slide archetypes, visual guidance, speaker notes, and explicit source grounding.

## What This Skill Does

- Converts unstructured source material into a slide deck outline.
- Audits or improves existing deck outlines.
- Assigns slide archetypes for rhetorical and visual variety.
- Requires citations or grounding status for every substantive slide.
- Adds production-ready guidance for downstream design, image generation, presentation, or PowerPoint agents.
- Uses a second-pass critique loop to improve strategy, evidence quality, and narrative flow.

## What This Skill Does Not Do

- It does not export `.pptx` files by itself.
- It does not guarantee live URL or media verification unless the active agent environment has browsing or URL-reading tools.
- It does not store memory automatically.
- It does not replace legal, medical, financial, or compliance review for high-stakes material.

## Repository Structure

```text
slide-deck-preparation/
|-- SKILL.md                    # AgentSkill instructions and operating contract
|-- agents/openai.yaml          # Optional UI metadata for compatible runtimes
|-- assets/template.md          # Required deck outline output contract
|-- references/archetypes.md    # Slide archetype library
|-- evals/evals.json            # Example evaluation prompts and expectations
|-- scripts/validate_repo.py    # Repository and skill validation
|-- .github/workflows/          # CI validation workflow
|-- sandboxes/                  # Optional local sample outputs, ignored by default
`-- scratch/                    # Local experiments, ignored by default
```

Only `SKILL.md`, `assets/`, `references/`, and optionally `agents/` are needed for installation. `evals/` supports quality checks. `sandboxes/`, `scratch/`, and `dist/` are local development areas and are ignored by default.

## Installation

Install with a compatible Agent Skills CLI:

```bash
npx skills install jovd83/slide-deck-preparation
```

Manual installation:

1. Copy `SKILL.md`, `assets/`, `references/`, and `agents/` into your agent's skill registry.
2. Ensure the folder name is `slide-deck-preparation`.
3. Run validation:

```bash
python scripts/validate_repo.py
```

## Usage Examples

```text
Use $slide-deck-preparation to turn this article into a 7-slide board briefing for nontechnical executives.
```

```text
Use $slide-deck-preparation to audit this existing outline and propose a stronger 10-slide investor narrative.
```

```text
Use $slide-deck-preparation to create a 12-slide technical training deck from these notes. Keep citations explicit and flag unsupported claims.
```

## Output Contract

The final output is Markdown following `assets/template.md`. It includes:

- Presentation brief and assumptions.
- Strategy scorecard.
- Source summary.
- Revision history.
- Agenda.
- Exact slide count.
- Slide archetype, purpose, visual motif, labels, content, speaker notes, grounding, and optional media guidance for each slide.

## Memory and Integrations

The skill uses runtime memory for the current task only. Project-local memory, such as reusable brand or audience preferences, should be created only when the user explicitly requests it. Shared cross-agent memory is out of scope and should be handled through an external shared-memory skill or platform service.

Optional integrations include browsing, document extraction, presentation generation, image generation, and shared-memory tools. The skill is written so those integrations improve results but are not required for basic deck planning.

## Development

Run repository validation:

```bash
python scripts/validate_repo.py
```

Run the AgentSkill validator when available:

```bash
python %USERPROFILE%\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```

## License

MIT
