#!/usr/bin/env python3
"""SHA-256 baseline and verify for a local folder (Module 81 exercise). Offline.

  python integrity_check.py baseline DIR OUT.json
  python integrity_check.py verify   DIR OUT.json
"""
import hashlib
import json
import sys
from pathlib import Path


def hash_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_baseline(folder):
    root = Path(folder)
    return {str(p.relative_to(root)): hash_file(p) for p in sorted(root.rglob("*")) if p.is_file()}


def compare(baseline, current):
    return {
        "modified": sorted(k for k in baseline if k in current and baseline[k] != current[k]),
        "missing": sorted(k for k in baseline if k not in current),
        "new": sorted(k for k in current if k not in baseline),
    }


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("baseline", "verify"):
        raise SystemExit(__doc__)
    mode, folder, store = sys.argv[1:]
    if mode == "baseline":
        Path(store).write_text(json.dumps(build_baseline(folder), indent=2), encoding="utf-8")
        print(f"Baseline saved to {store}")
    else:
        result = compare(json.loads(Path(store).read_text(encoding="utf-8")), build_baseline(folder))
        for kind, files in result.items():
            for name in files:
                print(f"{kind.upper()}: {name}")
        changed = any(result.values())
        print("Changes detected" if changed else "No changes")
        sys.exit(1 if changed else 0)
