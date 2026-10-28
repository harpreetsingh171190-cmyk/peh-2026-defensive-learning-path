#!/usr/bin/env python3
"""CVSS v3.1 base-score calculator for study. Offline; scores vector strings only."""
import math
import sys

AV = {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2}
AC = {"L": 0.77, "H": 0.44}
UI = {"N": 0.85, "R": 0.62}
CIA = {"H": 0.56, "L": 0.22, "N": 0.0}
PR_U = {"N": 0.85, "L": 0.62, "H": 0.27}
PR_C = {"N": 0.85, "L": 0.68, "H": 0.5}


def roundup(value):
    integer = int(round(value * 100000))
    if integer % 10000 == 0:
        return integer / 100000.0
    return (math.floor(integer / 10000) + 1) / 10.0


def parse(vector):
    parts = vector.strip().split("/")
    if not parts or parts[0] != "CVSS:3.1":
        raise ValueError("vector must start with CVSS:3.1")
    metrics = dict(p.split(":", 1) for p in parts[1:])
    required = ("AV", "AC", "PR", "UI", "S", "C", "I", "A")
    missing = [m for m in required if m not in metrics]
    if missing:
        raise ValueError("missing metrics: " + ", ".join(missing))
    return metrics


def base_score(vector):
    m = parse(vector)
    changed = m["S"] == "C"
    if m["S"] not in ("U", "C"):
        raise ValueError("S must be U or C")
    try:
        pr = (PR_C if changed else PR_U)[m["PR"]]
        iss = 1 - (1 - CIA[m["C"]]) * (1 - CIA[m["I"]]) * (1 - CIA[m["A"]])
        exploit = 8.22 * AV[m["AV"]] * AC[m["AC"]] * pr * UI[m["UI"]]
    except KeyError as exc:
        raise ValueError(f"invalid metric value: {exc}") from exc
    impact = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15 if changed else 6.42 * iss
    if impact <= 0:
        return 0.0
    total = 1.08 * (impact + exploit) if changed else impact + exploit
    return roundup(min(total, 10))


def rating(score):
    if score == 0:
        return "None"
    return "Low" if score < 4 else "Medium" if score < 7 else "High" if score < 9 else "Critical"


if __name__ == "__main__":
    for vec in sys.argv[1:] or ["CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"]:
        score = base_score(vec)
        print(f"{score:.1f} {rating(score)}  {vec}")
    print("Base score only; add environmental context before prioritizing.")
