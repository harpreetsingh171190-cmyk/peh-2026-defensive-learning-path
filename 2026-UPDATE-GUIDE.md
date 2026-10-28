# Practical Ethical Hacking — 2026 Update Guide

This update adds a modern learning path alongside the original course notes. It does **not** claim that every older command, screenshot, package version, or lab has been retested. Check current vendor documentation before using commands in a real environment.

## What's new in this 2026 learning path

- Modern web and API security: REST, GraphQL, authentication/authorization, rate limits, OAuth/OIDC, JWT handling, and API inventory.
- Cloud-native foundations: Docker/Compose, Kubernetes concepts, image and dependency scanning, secrets handling, least privilege, and software supply-chain security.
- AI-assisted security: using an LLM to explain logs and draft test cases while independently validating results; prompt injection, sensitive-data exposure, unsafe tool use, and model-output validation.
- Mobile application security: Android app components, permissions, exported activities, local storage, network security configuration, and safe dynamic analysis.
- Detection and response: logging, alert triage, evidence preservation, timeline creation, and writing actionable remediation.
- Modern workflow: Git, reproducible lab notes, Python virtual environments, dependency pinning, JSON/CSV output, and repeatable test reports.
- Responsible practice: written authorization, scope, rate limits, data handling, stop conditions, and cleanup.

## Recommended order

1. Complete the original networking, Linux, Python, methodology, and note-taking chapters.
2. Work through `29. Modern Web and API Security.md`.
3. Work through `30. Cloud, Containers and Supply Chain Security.md`.
4. Work through `31. AI Security and AI-Assisted Testing.md`.
5. Work through `32. Android Mobile Application Security.md`.
6. Work through `33. Detection, Reporting and Professional Workflow.md`.
7. Finish `34. 2026 Capstone Project.md`.

## Safe lab rules

- Only test systems you own or have explicit written permission to assess.
- Prefer intentionally vulnerable local applications, isolated VMs, and private Docker networks.
- Do not scan public IP ranges, school/work networks, neighbours' Wi-Fi, or third-party accounts without authorization.
- Use dummy accounts and synthetic data. Never put real passwords, API keys, tokens, personal data, or client evidence into public AI tools.
- Set explicit timeouts and request limits. Stop if a test affects availability or reaches out-of-scope systems.
- Keep a record of scope, commands, timestamps, findings, evidence, impact, and remediation.

## Version freshness checklist

Before running any install command or copying a tool command from older notes:
- Check the project's official documentation and release notes.
- Prefer supported packages from your distribution's repositories where practical.
- Confirm whether a tool uses a new command name or configuration format.
- Use a Python virtual environment for Python tools and avoid `sudo pip`.
- Pin versions for repeatable labs; update pins deliberately after testing.
- Verify container images and download checksums/signatures when available.
- Rebuild disposable labs from clean snapshots when exercises become inconsistent.

## Suggested official references

- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP API Security Project: https://owasp.org/www-project-api-security/
- OWASP Mobile Application Security: https://mas.owasp.org/
- OWASP GenAI Security Project: https://genai.owasp.org/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- MITRE ATT&CK: https://attack.mitre.org/
- CISA Secure by Design: https://www.cisa.gov/securebydesign
- Docker documentation: https://docs.docker.com/
- Kubernetes documentation: https://kubernetes.io/docs/
- Git documentation: https://git-scm.com/doc

These links are starting points, not a claim that every page or framework version is the newest release.
