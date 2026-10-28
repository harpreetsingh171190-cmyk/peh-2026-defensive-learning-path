#!/usr/bin/env python3
"""Parse the repository's synthetic JSONL authentication events; no network access."""
import json
from collections import Counter
from pathlib import Path

path = Path(__file__).with_name("sample-auth-events.jsonl")
counts = Counter()
with path.open(encoding="utf-8") as handle:
    for line_number, line in enumerate(handle, start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSON on line {line_number}: {exc}") from exc
        key = (event.get("user", "unknown"), event.get("source", "unknown"))
        counts[(key, event.get("event", "unknown"))] += 1

for (identity, event_type), count in sorted(counts.items()):
    user, source = identity
    print(f"user={user:12} source={source:15} event={event_type:14} count={count}")

print("\nReview repeated failures followed by success manually; this toy dataset is not a production detector.")
