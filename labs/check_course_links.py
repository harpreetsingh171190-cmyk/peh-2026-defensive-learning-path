#!/usr/bin/env python3
"""Check that relative Markdown links in README.md point to files that exist. Offline."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\((?:<([^>]+)>|([^)\s]+))\)")


def broken_links(readme=ROOT / "README.md"):
    missing = []
    for angle, plain in LINK.findall(readme.read_text(encoding="utf-8")):
        target = (angle or plain).split("#")[0]
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (ROOT / unquote(target)).exists():
            missing.append(target)
    return missing


if __name__ == "__main__":
    bad = broken_links()
    for t in bad:
        print("BROKEN:", t)
    print("All README links OK" if not bad else f"{len(bad)} broken link(s)")
    sys.exit(1 if bad else 0)
