#!/usr/bin/env python3
"""Validate SYNTHETIC security events (Module 74 exercise). Offline, no network."""
import ipaddress
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = ("timestamp", "event", "user", "source")
DOC_NETS = [ipaddress.ip_network(n) for n in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")]


def check_event(event):
    """Return a list of problems for one event dict (empty list = valid)."""
    problems = [f"missing field: {f}" for f in REQUIRED if f not in event]
    ts = event.get("timestamp")
    if ts is not None:
        try:
            parsed = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
            if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(None):
                problems.append("timestamp is not UTC")
        except ValueError:
            problems.append("timestamp is not ISO 8601")
    src = event.get("source")
    if src is not None:
        try:
            if not any(ipaddress.ip_address(src) in net for net in DOC_NETS):
                problems.append("source is not a documentation-reserved IP")
        except ValueError:
            problems.append("source is not an IP address")
    return problems


def validate_file(path):
    results = []
    with Path(path).open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                problems = check_event(json.loads(line))
            except json.JSONDecodeError:
                problems = ["invalid JSON"]
            if problems:
                results.append((number, problems))
    return results


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("sample-auth-events.jsonl")
    bad = validate_file(target)
    for number, problems in bad:
        print(f"line {number}: {'; '.join(problems)}")
    print("OK: all events valid" if not bad else f"{len(bad)} invalid line(s)")
    sys.exit(1 if bad else 0)
