#!/usr/bin/env python3
"""Check response headers on loopback addresses only; no external scanning."""
from urllib.request import Request, build_opener, ProxyHandler
from urllib.parse import urlparse
import ipaddress
import sys

REQUIRED = {
    "content-security-policy": "Consider a restrictive CSP appropriate to the app.",
    "x-content-type-options": "Set X-Content-Type-Options: nosniff.",
    "referrer-policy": "Choose a Referrer-Policy suitable for the app.",
    "permissions-policy": "Limit browser features the app does not need.",
}

def validate_loopback_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("Use a complete http:// or https:// URL.")
    try:
        address = ipaddress.ip_address(parsed.hostname)
    except ValueError as exc:
        raise ValueError("Only literal loopback IP addresses are allowed (127.0.0.1 or ::1).") from exc
    if not address.is_loopback:
        raise ValueError("Safety guard: this tool only permits loopback targets.")
    return url

def audit(url: str) -> list[str]:
    safe_url = validate_loopback_url(url)
    request = Request(safe_url, headers={"User-Agent": "LocalSecurityLearningLab/1.0"})
    opener = build_opener(ProxyHandler({}))  # Never route local lab traffic through an environment proxy.
    with opener.open(request, timeout=3) as response:
        headers = {key.lower(): value for key, value in response.headers.items()}
    missing = []
    for header, advice in REQUIRED.items():
        if header not in headers:
            missing.append(f"MISSING {header}: {advice}")
        else:
            print(f"OK      {header}")
    return missing

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8765"
    try:
        findings = audit(target)
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
    for finding in findings:
        print(finding)
    print(f"\\nSummary: {len(findings)} header recommendation(s); review manually.")
