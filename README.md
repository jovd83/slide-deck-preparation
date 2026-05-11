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
├── SKILL.md              # Agent skill definition
├── README.md             # This file
├── LICENSE               # MIT License
├── CHANGELOG.md          # Version history
├── assets/
│   └── template.md       # Output format template
├── references/
│   └── archetypes.md     # 50+ slide archetypes
└── scripts/
    └── validate_repo.py  # Repository validator
```

## Installation

Copy the `SKILL.md`, `assets/`, `references/`, and `scripts/` directory into your agent's skill registry.

## License

MIT
