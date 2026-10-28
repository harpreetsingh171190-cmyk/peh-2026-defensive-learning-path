#!/usr/bin/env python3
"""Consolidate SYNTHETIC findings (JSON) into one client-ready Markdown report.

Input is a JSON array of finding objects with at least: id, title, severity, asset, status.
Optional fields (summary, impact, remediation, evidence) are included when present. This
mirrors the fields in templates/finding-report-template.md so individual finding files can be
authored first and then merged for delivery. Offline; makes no network requests.
"""
import json
import sys
from pathlib import Path

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "informational": 4, "info": 4}


def severity_rank(finding):
    sev = str(finding.get("severity", "")).strip().lower()
    if sev not in SEVERITY_ORDER:
        raise ValueError(f"{finding.get('id', '?')}: unknown severity {sev!r}")
    return SEVERITY_ORDER[sev]


def load_findings(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("findings file must contain a JSON array")
    return sorted(data, key=lambda f: (severity_rank(f), f.get("id", "")))


def severity_counts(findings):
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "informational": 0}
    for f in findings:
        sev = str(f["severity"]).strip().lower()
        sev = "informational" if sev == "info" else sev
        counts[sev] += 1
    return counts


def render_summary_table(findings):
    counts = severity_counts(findings)
    lines = ["| Severity | Count |", "|---|---|"]
    lines += [f"| {sev.capitalize()} | {n} |" for sev, n in counts.items()]
    return "\n".join(lines)


def render_finding(f):
    lines = [f"## {f['id']}: {f['title']}", "", f"- Severity: {f['severity']}",
              f"- Asset: {f.get('asset', 'n/a')}", f"- Status: {f.get('status', 'open')}"]
    for heading, key in (("Summary", "summary"), ("Impact", "impact"),
                          ("Remediation", "remediation"), ("Evidence", "evidence")):
        if f.get(key):
            lines += ["", f"### {heading}", f[key]]
    return "\n".join(lines)


def render_report(findings, title="Security Assessment — Consolidated Findings"):
    parts = [f"# {title}", "", render_summary_table(findings), ""]
    parts += [render_finding(f) for f in findings]
    return "\n\n".join(parts) + "\n"


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("sample-findings.json")
    out = sys.argv[2] if len(sys.argv) > 2 else None
    report = render_report(load_findings(src))
    if out:
        Path(out).write_text(report, encoding="utf-8")
        print(f"wrote {out}")
    else:
        print(report)
