#!/usr/bin/env python3
"""Flag repeated login failures followed by a success in SYNTHETIC auth events.

Offline only: reads a local JSONL file, makes no network connections.
This is a teaching detector, not a production rule.
"""
import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def parse_ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_events(path):
    events = []
    with Path(path).open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
                event["_ts"] = parse_ts(event["timestamp"])
            except (json.JSONDecodeError, KeyError, ValueError) as exc:
                raise ValueError(f"line {number}: {exc}") from exc
            events.append(event)
    return sorted(events, key=lambda e: e["_ts"])


def find_anomalies(events, threshold=3, window_seconds=120):
    """Return (user, source, failures) where >= threshold failures precede a success within the window."""
    failures = defaultdict(list)
    findings = []
    for event in events:
        key = (event.get("user", "unknown"), event.get("source", "unknown"))
        if event.get("event") == "login_failure":
            failures[key].append(event["_ts"])
        elif event.get("event") == "login_success":
            recent = [t for t in failures[key] if (event["_ts"] - t).total_seconds() <= window_seconds]
            if len(recent) >= threshold:
                findings.append((key[0], key[1], len(recent)))
            failures[key].clear()
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", default=Path(__file__).with_name("sample-auth-events.jsonl"))
    parser.add_argument("--threshold", type=int, default=3)
    parser.add_argument("--csv", help="optional path to write findings as CSV")
    parser.add_argument("--window", type=int, default=120, help="seconds")
    args = parser.parse_args()
    findings = find_anomalies(load_events(args.file), args.threshold, args.window)
    for user, source, count in findings:
        print(f"REVIEW user={user} source={source} failures_before_success={count}")
    if args.csv:
        import csv
        with open(args.csv, "w", newline="", encoding="utf-8") as out:
            writer = csv.writer(out)
            writer.writerow(["user", "source", "failures_before_success"])
            writer.writerows(findings)
    print("Triage manually: confirm with the account owner before drawing conclusions.")


if __name__ == "__main__":
    main()
