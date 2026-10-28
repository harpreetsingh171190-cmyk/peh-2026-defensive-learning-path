#!/usr/bin/env python3
"""Project quality gate: numbering, README coverage, dashboard and version consistency. Offline."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
MODULE_FILE = re.compile(r"^(\d{2})\. .+\.md$")
LINK = re.compile(r"\]\((?:<([^>]+)>|([^)\s]+))\)")


def module_files(root=ROOT):
    found = {}
    for path in root.iterdir():
        match = MODULE_FILE.match(path.name)
        if match:
            found.setdefault(int(match.group(1)), []).append(path.name)
    return found


def check_numbering(modules):
    problems = []
    if not modules:
        return ["no module files found"]
    for number in range(1, max(modules) + 1):
        if number not in modules:
            problems.append(f"module {number:02d} is missing")
        elif len(modules[number]) > 1:
            problems.append(f"module {number:02d} has duplicate files: {modules[number]}")
    return problems


def readme_links(root=ROOT):
    text = (root / "README.md").read_text(encoding="utf-8")
    return {unquote(a or b).split("#")[0] for a, b in LINK.findall(text)}


def check_readme_coverage(modules, links):
    return [f"README does not link {name}" for names in modules.values() for name in names if name not in links]


def dashboard_module_count(root=ROOT):
    text = (root / "dashboard" / "index.html").read_text(encoding="utf-8")
    block = re.search(r"const moduleNames = \[(.*?)\];", text, re.S)
    return len(re.findall(r'^"', block.group(1), re.M)) if block else 0, text


def check_dashboard(modules, root=ROOT):
    count, text = dashboard_module_count(root)
    problems = []
    if count != max(modules):
        problems.append(f"dashboard lists {count} modules but highest module is {max(modules)}")
    claimed = re.search(r"(\d+) modules", text)
    if not claimed or int(claimed.group(1)) != max(modules):
        problems.append("dashboard header curriculum count does not match modules")
    return problems


def check_dashboard_offline(root=ROOT):
    text = (root / "dashboard" / "index.html").read_text(encoding="utf-8")
    problems = []
    if "Content-Security-Policy" not in text or "connect-src 'none'" not in text:
        problems.append("dashboard is missing the connect-src 'none' Content-Security-Policy")
    for token in ("fetch(", "XMLHttpRequest", "WebSocket(", "sendBeacon", "<script src", "<link rel=\"stylesheet\""):
        if token in text:
            problems.append(f"dashboard contains a network-capable construct: {token}")
    return problems


def check_versions(root=ROOT):
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    problems = []
    if f"## [{version}]" not in (root / "CHANGELOG.md").read_text(encoding="utf-8"):
        problems.append(f"CHANGELOG.md has no entry for {version}")
    if f'version = "{version}"' not in (root / "pyproject.toml").read_text(encoding="utf-8"):
        problems.append("pyproject.toml version differs from VERSION")
    if f"version: {version}" not in (root / "CITATION.cff").read_text(encoding="utf-8"):
        problems.append("CITATION.cff version differs from VERSION")
    return problems


def run(root=ROOT):
    modules = module_files(root)
    return (check_numbering(modules) + check_readme_coverage(modules, readme_links(root))
            + check_dashboard(modules, root) + check_dashboard_offline(root) + check_versions(root))


if __name__ == "__main__":
    issues = run()
    for issue in issues:
        print("FAIL:", issue)
    print("Project checks passed" if not issues else f"{len(issues)} problem(s)")
    sys.exit(1 if issues else 0)
