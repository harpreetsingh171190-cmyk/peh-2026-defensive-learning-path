#!/usr/bin/env python3
"""Flag unpinned dependencies in a requirements-style file (Module 37 exercise). Offline."""
import re
import sys
from pathlib import Path

PINNED = re.compile(r"^[A-Za-z0-9_.\-\[\]]+==[A-Za-z0-9_.\-+!]+$")


def unpinned(lines):
    out = []
    for number, line in enumerate(lines, start=1):
        text = line.split("#")[0].strip()
        if text and not text.startswith("-") and not PINNED.match(text):
            out.append((number, text))
    return out


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("sample-requirements.txt")
    found = unpinned(Path(target).read_text(encoding="utf-8").splitlines())
    for number, text in found:
        print(f"line {number}: not pinned to an exact version -> {text}")
    print("All dependencies pinned" if not found else f"{len(found)} unpinned; pin versions and review updates deliberately")
    sys.exit(1 if found else 0)
