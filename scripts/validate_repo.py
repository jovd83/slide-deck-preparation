#!/usr/bin/env python3
"""Validate the slide-deck-preparation AgentSkill repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "assets/template.md",
    "references/archetypes.md",
    "agents/openai.yaml",
    "evals/evals.json",
]

SKILL_REQUIRED_PHRASES = [
    "Read `assets/template.md`",
    "Read `references/archetypes.md`",
    "Memory Model",
    "Do not claim live verification",
    "Never fabricate URLs",
    "Exact slide count",
]

TEMPLATE_REQUIRED_FIELDS = [
    "Target Audience",
    "Goal",
    "Narrative Arc",
    "Key Takeaway",
    "Number of Slides",
    "Strategy Scorecard",
    "Assumptions",
    "Residual Risks",
    "Grounding Status",
    "Recommended External Media",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[PASS] {message}")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def validate_required_files() -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_FILES:
        if (ROOT / rel).exists():
            ok(f"Found {rel}")
        else:
            errors.append(f"Missing required file: {rel}")
            fail(errors[-1])
    return errors


def validate_skill_frontmatter() -> list[str]:
    errors: list[str] = []
    content = read("SKILL.md")
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", content, re.DOTALL)
    if not match:
        return ["SKILL.md must start with YAML frontmatter"]

    frontmatter = match.group("body")
    keys = re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, re.MULTILINE)
    if keys != ["name", "description"]:
        errors.append("SKILL.md frontmatter must contain only name and description in that order")

    if "name: slide-deck-preparation" not in frontmatter:
        errors.append("SKILL.md name must be slide-deck-preparation")

    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not description_match or len(description_match.group(1).strip().strip('"')) < 120:
        errors.append("SKILL.md description should be specific enough to trigger the skill reliably")

    for phrase in SKILL_REQUIRED_PHRASES:
        if phrase not in content:
            errors.append(f"SKILL.md missing required guidance: {phrase}")

    if errors:
        for error in errors:
            fail(error)
    else:
        ok("SKILL.md frontmatter and core guidance look good")
    return errors


def validate_template() -> list[str]:
    errors: list[str] = []
    content = read("assets/template.md")
    for field in TEMPLATE_REQUIRED_FIELDS:
        if field not in content:
            errors.append(f"Template missing field: {field}")

    slide_block_count = len(re.findall(r"^### Slide \[N\]", content, re.MULTILINE))
    if slide_block_count != 1:
        errors.append("Template should contain one reusable slide block")

    if errors:
        for error in errors:
            fail(error)
    else:
        ok("Output template includes required contract fields")
    return errors


def validate_archetypes() -> list[str]:
    errors: list[str] = []
    content = read("references/archetypes.md")
    archetype_count = len(re.findall(r"^\d+\.\s+\*\*", content, re.MULTILINE))
    if archetype_count < 30:
        errors.append(f"Expected at least 30 archetypes, found {archetype_count}")
    if "Selection rules" not in content:
        errors.append("Archetype reference should include selection rules")

    if errors:
        for error in errors:
            fail(error)
    else:
        ok(f"Archetype library includes {archetype_count} archetypes and selection rules")
    return errors


def validate_evals() -> list[str]:
    errors: list[str] = []
    data = json.loads(read("evals/evals.json"))
    if data.get("skill_name") != "slide-deck-preparation":
        errors.append("evals/evals.json has wrong skill_name")
    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < 3:
        errors.append("evals/evals.json should include at least three evals")
    else:
        for item in evals:
            for key in ["id", "name", "prompt", "expected_behaviors", "files"]:
                if key not in item:
                    errors.append(f"Eval {item.get('id', '<unknown>')} missing {key}")
            if "prompt" in item and "$slide-deck-preparation" not in item["prompt"]:
                errors.append(f"Eval {item.get('id', '<unknown>')} should invoke $slide-deck-preparation")

    if errors:
        for error in errors:
            fail(error)
    else:
        ok("Evaluation prompts are structured")
    return errors


def validate_openai_yaml() -> list[str]:
    errors: list[str] = []
    content = read("agents/openai.yaml")
    for phrase in [
        "interface:",
        'display_name: "Slide Deck Preparation"',
        'short_description: "Plan grounded presentation outlines"',
        "$slide-deck-preparation",
    ]:
        if phrase not in content:
            errors.append(f"agents/openai.yaml missing {phrase}")

    if errors:
        for error in errors:
            fail(error)
    else:
        ok("agents/openai.yaml includes UI metadata")
    return errors


def main() -> int:
    print("Validating slide-deck-preparation repository\n")
    errors: list[str] = []
    errors.extend(validate_required_files())

    if errors:
        print("\nValidation failed before content checks.")
        return 1

    errors.extend(validate_skill_frontmatter())
    errors.extend(validate_template())
    errors.extend(validate_archetypes())
    errors.extend(validate_evals())
    errors.extend(validate_openai_yaml())

    if errors:
        print(f"\nValidation failed with {len(errors)} issue(s).")
        return 1

    print("\nValidation complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
