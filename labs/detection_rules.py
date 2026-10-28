#!/usr/bin/env python3
"""Tiny rule engine for SYNTHETIC events (Module 61/85 exercise). Offline, no network."""
import json
import sys
from pathlib import Path

RULES = [
    {"id": "R-001", "name": "Login failure", "match": {"event": "login_failure"}, "severity": "low"},
    {"id": "R-002", "name": "Login success", "match": {"event": "login_success"}, "severity": "info"},
]


def matches(rule, event):
    """True when every key/value in the rule's match dict equals the event's value."""
    return all(event.get(k) == v for k, v in rule["match"].items())


def evaluate(events, rules=RULES):
    hits = {}
    for event in events:
        for rule in rules:
            if matches(rule, event):
                hits.setdefault(rule["id"], []).append(event)
    return hits


def load(path):
    with Path(path).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("sample-auth-events.jsonl")
    results = evaluate(load(target))
    for rule in RULES:
        count = len(results.get(rule["id"], []))
        print(f"{rule['id']} {rule['name']:15} severity={rule['severity']:5} hits={count}")
    print("Rules are teaching examples; tune against your own synthetic data.")
