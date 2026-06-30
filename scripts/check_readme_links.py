#!/usr/bin/env python3
"""Validate README markdown links point to existing root files and use matching labels."""

from __future__ import annotations

import re
import sys
from pathlib import Path


README_LINK_RE = re.compile(r"\[`([^`]+)`\]\(([^)]+)\)")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    readme_path = repo_root / "README.md"
    content = readme_path.read_text(encoding="utf-8")
    matches = README_LINK_RE.findall(content)

    if not matches:
        print("No markdown links found in README.md; skipping consistency checks.")
        return 0

    errors: list[str] = []
    for label, target in matches:
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = repo_root / target
        if not target_path.is_file():
            errors.append(f"Missing file target: `{target}`")
        if label != Path(target).name:
            errors.append(f"Label/target mismatch: label `{label}` != target `{target}`")

    if errors:
        print("README link consistency check failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("README link consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
