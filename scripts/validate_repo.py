#!/usr/bin/env python3
"""Validation for the slide-deck-preparation repository."""

import sys
import os
from pathlib import Path

# Import grading logic (re-implementing here for a standalone script)
def grade_deck(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    required_metadata = [
        "Target Duration", "Tone", "Technical Level", "Sources", "Source Summary",
        "General Narrative", "General Visual Motif", "Strategy Scorecard",
        "Revision History & Improvement Proposals"
    ]
    for meta in required_metadata:
        if f"**{meta}:**" not in content and f"{meta}:" not in content and f"### {meta}" not in content:
            issues.append(f"Missing Metadata: {meta}")

    scorecard_elements = ["Storytelling", "Audience Focus", "Minimalist Design", "Confident Delivery", "Single Clear Goal"]
    for elem in scorecard_elements:
        if elem not in content:
            issues.append(f"Missing Scorecard Element: {elem}")

    if "### Recommended External Media" in content:
        if "Status:" not in content and "**Status:**" not in content:
            issues.append("Missing External Media Verification Status")
        elif "browser_subagent" not in content and "read_url_content" not in content:
            issues.append("External Media Status missing verification method (browser_subagent/read_url_content)")

    if "http" not in content:
        issues.append("No verifiable URLs found in sources.")

    return issues

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    required_files = [
        "SKILL.md",
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "assets/template.md",
        "references/archetypes.md"
    ]
    
    errors = False
    
    print("Step 1: Checking required files...")
    for f in required_files:
        if not (root / f).exists():
            print(f"  [FAIL] Missing: {f}")
            errors = True
        else:
            print(f"  [PASS] Found: {f}")

    print("\nStep 2: Checking sandbox compliance...")
    sandbox_dir = root / "sandboxes"
    if sandbox_dir.exists():
        for filename in os.listdir(sandbox_dir):
            if filename.endswith(".md"):
                path = sandbox_dir / filename
                issues = grade_deck(path)
                if issues:
                    print(f"  [FAIL] {filename}:")
                    for issue in issues:
                        print(f"    - {issue}")
                    errors = True
                else:
                    print(f"  [PASS] {filename} is compliant.")
    else:
        print("  [SKIP] No sandboxes directory found.")

    if errors:
        print("\nValidation failed! Please fix the issues above.")
        return 1
        
    print("\nValidation complete! Repository is in a high-fidelity state.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
