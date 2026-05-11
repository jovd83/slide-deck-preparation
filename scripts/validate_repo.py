#!/usr/bin/env python3
"""Validation for the slide-deck-preparation repository."""

import sys
from pathlib import Path

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
    
    missing = []
    for f in required_files:
        if not (root / f).exists():
            missing.append(f)
            
    if missing:
        print("Error: Missing required files:")
        for f in missing:
            print(f"  - {f}")
        return 1
        
    print("Validation complete! All required files found.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
