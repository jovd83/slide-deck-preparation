# slide-deck-preparation

[![version](https://img.shields.io/badge/version-1.0.0-blue)](CHANGELOG.md)
[![status](https://img.shields.io/badge/status-stable--beta-f0ad4e)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)
[![Validate Skill](https://github.com/jovd83/slide-deck-preparation/actions/workflows/validate.yml/badge.svg)](https://github.com/jovd83/slide-deck-preparation/actions/workflows/validate.yml)

Convert raw content (URLs, blog posts, podcasts, papers, documents) into structured slide deck outlines.

## Overview

This skill extracts narratives, determines target audiences, plans chapters, assigns slide archetypes, and provides explicit source citations to prevent hallucinations. It ensures a highly structured, presentation-ready output.

## Repository Structure

```text
slide-deck-preparation/
├── SKILL.md              # Agent skill definition (Master Instructions)
├── README.md             # This file
├── LICENSE               # MIT License
├── CHANGELOG.md          # Version history
├── assets/
│   └── template.md       # High-fidelity output template
├── references/
│   └── archetypes.md     # 50+ slide archetypes for visual variety
├── sandboxes/            # 5x Production-grade reference decks
├── evals/                # Evaluation data and test cases
└── scripts/
    └── validate_repo.py  # CI/CD Repository validator
```

## Key Features

*   **Strategy Scorecard**: Calibrate storytelling, minimalism, and audience focus using a 0-10 scoring system.
*   **Refinement Loop**: Mandatory "Judge & Refine" phase for surgical second-pass improvements.
*   **Visual Motif Consistency**: Global motif definitions that provide a cohesive creative brief for downstream image agents.
*   **Verifiable Groundedness**: Every slide requires direct URL citations to prevent hallucinations.
*   **TED Anti-Pattern Audit**: Automated guardrails to avoid common presentation mistakes.

## Installation

### Modern (CLI)
Install directly via the `skills` CLI:
```bash
npx skills install jovd83/slide-deck-preparation
```

### Manual
Copy the `SKILL.md`, `assets/`, and `references/` directories into your agent's skill registry.

## CI/CD Validation

This repository uses GitHub Actions to ensure 100% template compliance. The `scripts/validate_repo.py` tool programmatically audits all sandboxes for metadata density and narrative logic.

## License

MIT
