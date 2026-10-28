#!/usr/bin/env python3
"""Lightweight offline secret scanner for this repository (no network, standard library only).

Flags high-confidence credential patterns. Paths matching entries in `.secretscan-allow`
(one glob per line) are skipped; use that only for intentional lab data in upstream notes.
"""
import fnmatch
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERNS = {
    "AWS access key ID": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Private key block": re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b"),
    "Slack token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "Anthropic/OpenAI-style key": re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_\-]{32,}\b"),
}
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
TEXT_SUFFIXES = {".md", ".py", ".html", ".js", ".yml", ".yaml", ".json", ".jsonl", ".txt", ".csv", ".toml", ".cff", ".sh", ""}


def load_allow(root=ROOT):
    path = root / ".secretscan-allow"
    if not path.exists():
        return []
    return [l.strip() for l in path.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]


def scan_text(text):
    """Return a list of (label, line_number) findings for a block of text."""
    findings = []
    for number, line in enumerate(text.splitlines(), start=1):
        for label, pattern in PATTERNS.items():
            if pattern.search(line):
                findings.append((label, number))
    return findings


def scan_repo(root=ROOT):
    allow = load_allow(root)
    results = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES or any(fnmatch.fnmatch(rel, g) for g in allow):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        results.extend((rel, label, line) for label, line in scan_text(text))
    return results


if __name__ == "__main__":
    found = scan_repo()
    for rel, label, line in found:
        print(f"{rel}:{line}: possible {label}")
    print("No secrets detected" if not found else f"{len(found)} potential secret(s) found; remove and rotate them")
    sys.exit(1 if found else 0)
