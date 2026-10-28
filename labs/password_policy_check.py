#!/usr/bin/env python3
"""Offline passphrase-policy checker for training. Never enter real passwords; use made-up examples."""
import math
import string
import sys

COMMON = {"password", "123456", "qwerty", "letmein", "welcome", "admin", "iloveyou", "changeme"}


def estimate_bits(candidate):
    pool = 0
    pool += 26 if any(c.islower() for c in candidate) else 0
    pool += 26 if any(c.isupper() for c in candidate) else 0
    pool += 10 if any(c.isdigit() for c in candidate) else 0
    pool += 32 if any(c in string.punctuation for c in candidate) else 0
    return round(len(candidate) * math.log2(pool), 1) if pool else 0.0


def check(candidate, min_length=14):
    """Return a list of policy problems (empty = passes this toy policy)."""
    problems = []
    if len(candidate) < min_length:
        problems.append(f"shorter than {min_length} characters")
    if candidate.lower() in COMMON or any(w in candidate.lower() for w in COMMON):
        problems.append("contains a very common password")
    if len(set(candidate)) <= max(3, len(candidate) // 4):
        problems.append("too much repetition")
    return problems


if __name__ == "__main__":
    for sample in sys.argv[1:] or ["password123", "correct-horse-battery-staple-demo"]:
        issues = check(sample)
        print(f"{sample!r}: ~{estimate_bits(sample)} bits (rough upper bound) -> {'OK' if not issues else '; '.join(issues)}")
    print("Estimates ignore real-world guessing patterns. Prefer a password manager and passkeys.")
