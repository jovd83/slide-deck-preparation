# Changelog

All notable changes to this project are documented here. The project follows Semantic Versioning where practical.

## [1.1.0] - 2026-05-12

### Changed

- Rewrote `SKILL.md` around a clearer AgentSkill contract, workflow, guardrails, output rules, and memory model.
- Reduced nonstandard frontmatter to Agent Skills compatible `name` and `description` fields.
- Reworked `assets/template.md` into a stricter, more auditable deck-outline contract.
- Clarified media and source verification statuses to avoid false claims of live verification.
- Expanded archetype selection guidance for better deck variety and audience fit.
- Rebuilt the README for GitHub readiness, installation clarity, scope boundaries, and development workflow.

### Added

- Added `agents/openai.yaml` UI metadata for compatible runtimes.
- Added stronger repository validation covering frontmatter, required resources, output template fields, archetype coverage, README claims, and eval structure.
- Added explicit memory architecture guidance distinguishing runtime memory, project-local memory, and out-of-scope shared memory.

## [1.0.0] - 2026-05-12

### Added

- Initial release of `slide-deck-preparation`.
- Structured workflow for converting source material into deck outlines.
- Slide archetype reference library.
- Markdown deck output template.
- Basic validation script and GitHub Actions workflow.
