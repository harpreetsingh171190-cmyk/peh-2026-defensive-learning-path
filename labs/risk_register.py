#!/usr/bin/env python3
"""Rank a SYNTHETIC risk register by likelihood x impact (Module 67/69 exercise)."""
import csv
import sys
from pathlib import Path


def band(score):
    return "high" if score >= 15 else "medium" if score >= 8 else "low"


def load_risks(path):
    risks = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            likelihood, impact = int(row["likelihood"]), int(row["impact"])
            if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
                raise ValueError(f"{row['id']}: likelihood and impact must be 1-5")
            score = likelihood * impact
            risks.append({**row, "score": score, "band": band(score)})
    return sorted((r for r in risks if r["status"] != "closed"), key=lambda r: -r["score"])


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("sample-risks.csv")
    for r in load_risks(target):
        print(f"{r['id']:4} score={r['score']:2} {r['band']:6} owner={r['owner']:10} {r['title']}")
