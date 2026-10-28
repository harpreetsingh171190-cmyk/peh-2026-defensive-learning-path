# Practical Ethical Hacking 2026 — Defensive Learning Path

[![Course Quality](https://github.com/harpreetsingh171190-cmyk/practical-ethical-hacking-course/actions/workflows/course-quality.yml/badge.svg)](https://github.com/harpreetsingh171190-cmyk/practical-ethical-hacking-course/actions/workflows/course-quality.yml)
[![CodeQL](https://github.com/harpreetsingh171190-cmyk/practical-ethical-hacking-course/actions/workflows/codeql.yml/badge.svg)](https://github.com/harpreetsingh171190-cmyk/practical-ethical-hacking-course/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Modules](https://img.shields.io/badge/modules-86-blue)](README.md#curriculum)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Course notes, offline labs and a study dashboard for **authorized, defensive-minded** security learning.
86 modules · 15+ offline lab scripts · assessments and templates · an offline progress dashboard.

> **Authorization first.** Practise only on systems you own or have explicit written permission to test.
> Read [ETHICS-AND-ACCEPTABLE-USE.md](ETHICS-AND-ACCEPTABLE-USE.md) before starting.

Based on [Practical Ethical Hacking: The Complete Course](https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course) by TCM Security (2023). See [NOTICE.md](NOTICE.md).

## Quick start

```bash
git clone <your-fork-url> && cd practical-ethical-hacking-course
make check                      # compile, unit tests, project quality gate
open dashboard/index.html       # offline tracker (or open it in any modern browser)
```

1. Read [LAB-SAFETY-AND-SETUP.md](LAB-SAFETY-AND-SETUP.md) and [SETUP-WINDOWS-LINUX-TERMUX-2026.md](SETUP-WINDOWS-LINUX-TERMUX-2026.md).
2. Follow the [12-week roadmap](LEARNING-ROADMAP-2026.md) or the [2026 update guide](2026-UPDATE-GUIDE.md).
3. Complete labs with synthetic data, record evidence, then take the assessments.

## Curriculum

### Foundations (modules 01–08)

| # | Module |
|:-:|---|
| 01 | [Introduction](01.%20Introduction.md) |
| 02 | [A day in the life of a pentester](02.%20A%20day%20in%20the%20life%20of%20a%20pentester.md) |
| 03 | [Effective notekeeping](03.%20Effective%20notekeeping.md) |
| 04 | [Networking Refresher](04.%20Networking%20Refresher.md) |
| 05 | [Setting up our lab](05.%20Setting%20up%20our%20lab.md) |
| 06 | [Intro to Linux](06.%20Intro%20to%20Linux.md) |
| 07 | [Intro to Python](07.%20Intro%20to%20Python.md) |
| 08 | [The Ethical Hacker Methodology](08.%20The%20Ethical%20Hacker%20Methodology.md) |

### Core Concepts in an Authorized Lab (modules 09–14)

| # | Module |
|:-:|---|
| 09 | [Info Gathering (Reconnaissance)](09.%20Info%20Gathering%20%28Reconnaissance%29.md) |
| 10 | [Scanning & Enumeration](10.%20Scanning%20%26%20Enumeration.md) |
| 11 | [Vulnerability Scanning with Nessus](11.%20Vulnerability%20Scanning%20with%20Nessus.md) |
| 12 | [Exploitation Basics](12.%20Exploitation%20Basics.md) |
| 13 | [Exploit Development](13.%20Exploit%20Development.md) |
| 14 | [Capstone](14.%20Capstone.md) |

### Active Directory (modules 15–22)

| # | Module |
|:-:|---|
| 15 | [Active Directory Overview](15.%20Active%20Directory%20Overview.md) |
| 16 | [Active Directory Lab Build](16.%20Active%20Directory%20Lab%20Build.md) |
| 17 | [Attacking Active Directory - Initial Attack Vectors](17.%20Attacking%20Active%20Directory%20-%20Initial%20Attack%20Vectors.md) |
| 18 | [Attacking Active Directory - Post-Compromise Enumeration](18.%20Attacking%20Active%20Directory%20-%20Post-Compromise%20Enumeration.md) |
| 19 | [Attacking Active Directory - Post-Compromise Attacks](19.%20Attacking%20Active%20Directory%20-%20Post-Compromise%20Attacks.md) |
| 20 | [We've Compromised the Domain - Now What](20.%20We%27ve%20Compromised%20the%20Domain%20-%20Now%20What.md) |
| 21 | [Additional Active Directory Attacks](21.%20Additional%20Active%20Directory%20Attacks.md) |
| 22 | [Active Directory Case Studies](22.%20Active%20Directory%20Case%20Studies.md) |

### Post-Exploitation, Web and Wireless (modules 23–26)

| # | Module |
|:-:|---|
| 23 | [Post Exploitation](23.%20Post%20Exploitation.md) |
| 24 | [Web Application Enumeration - Revisited](24.%20Web%20Application%20Enumeration%20-%20Revisited.md) |
| 25 | [Find & Exploit Common Web Vulnerabilities](25.%20Find%20%26%20Exploit%20Common%20Web%20Vulnerabilities.md) |
| 26 | [Wireless Penetration Testing](26.%20Wireless%20Penetration%20Testing.md) |

### Professional Practice (modules 27–28)

| # | Module |
|:-:|---|
| 27 | [Legal Documents and Report Writing](27.%20Legal%20Documents%20and%20Report%20Writing.md) |
| 28 | [Career Advice](28.%20Career%20Advice.md) |

### Modern Security Core (2026) (modules 29–34)

| # | Module |
|:-:|---|
| 29 | [Modern Web and API Security](29.%20Modern%20Web%20and%20API%20Security.md) |
| 30 | [Cloud, Containers and Supply Chain Security](30.%20Cloud%2C%20Containers%20and%20Supply%20Chain%20Security.md) |
| 31 | [AI Security and AI-Assisted Testing](31.%20AI%20Security%20and%20AI-Assisted%20Testing.md) |
| 32 | [Android Mobile Application Security](32.%20Android%20Mobile%20Application%20Security.md) |
| 33 | [Detection, Reporting and Professional Workflow](33.%20Detection%2C%20Reporting%20and%20Professional%20Workflow.md) |
| 34 | [2026 Capstone Project](34.%202026%20Capstone%20Project.md) |

### Secure Design, Detection and Governance (modules 35–47)

| # | Module |
|:-:|---|
| 35 | [Threat Modeling and Secure Design](35.%20Threat%20Modeling%20and%20Secure%20Design.md) |
| 36 | [Defensive Detection Engineering](36.%20Defensive%20Detection%20Engineering.md) |
| 37 | [Secure Software Supply Chain and SBOM](37.%20Secure%20Software%20Supply%20Chain%20and%20SBOM.md) |
| 38 | [Incident Response and Digital Evidence](38.%20Incident%20Response%20and%20Digital%20Evidence.md) |
| 39 | [Cloud Identity and Infrastructure Security](39.%20Cloud%20Identity%20and%20Infrastructure%20Security.md) |
| 40 | [Modern Security Portfolio and Interview Lab](40.%20Modern%20Security%20Portfolio%20and%20Interview%20Lab.md) |
| 41 | [Secure Coding and Code Review](41.%20Secure%20Coding%20and%20Code%20Review.md) |
| 42 | [Identity, Sessions and Passkeys](42.%20Identity%2C%20Sessions%20and%20Passkeys.md) |
| 43 | [Privacy Engineering and Data Minimization](43.%20Privacy%20Engineering%20and%20Data%20Minimization.md) |
| 44 | [Security Testing Automation and Regression](44.%20Security%20Testing%20Automation%20and%20Regression.md) |
| 45 | [Secure Configuration and Hardening](45.%20Secure%20Configuration%20and%20Hardening.md) |
| 46 | [Career, Certifications and Responsible Practice](46.%20Career%2C%20Certifications%20and%20Responsible%20Practice.md) |
| 47 | [Standards and Official References](47.%20Standards%20and%20Official%20References.md) |

### Cloud, Containers, AI, Response and Capstones (modules 48–72)

| # | Module |
|:-:|---|
| 48 | [Cloud Security Fundamentals](48.%20Cloud%20Security%20Fundamentals.md) |
| 49 | [Container and Software Supply-Chain Security](49.%20Container%20and%20Software%20Supply-Chain%20Security.md) |
| 50 | [AI and LLM Application Security](50.%20AI%20and%20LLM%20Application%20Security.md) |
| 51 | [Incident Response and Evidence Handling](51.%20Incident%20Response%20and%20Evidence%20Handling.md) |
| 52 | [Capstone — Authorized Security Assessment](52.%20Capstone%20%E2%80%94%20Authorized%20Security%20Assessment.md) |
| 53 | [API Security and Authorization Testing](53.%20API%20Security%20and%20Authorization%20Testing.md) |
| 54 | [Secure CI-CD and Release Engineering](54.%20Secure%20CI-CD%20and%20Release%20Engineering.md) |
| 55 | [Backup, Recovery and Ransomware Readiness](55.%20Backup%2C%20Recovery%20and%20Ransomware%20Readiness.md) |
| 56 | [Mobile App Security Fundamentals](56.%20Mobile%20App%20Security%20Fundamentals.md) |
| 57 | [Portfolio, Interview and Final Assessment](57.%20Portfolio%2C%20Interview%20and%20Final%20Assessment.md) |
| 58 | [Threat Intelligence and Vulnerability Prioritization](58.%20Threat%20Intelligence%20and%20Vulnerability%20Prioritization.md) |
| 59 | [Windows and Linux Hardening Baselines](59.%20Windows%20and%20Linux%20Hardening%20Baselines.md) |
| 60 | [Cloud IAM and Least Privilege Lab](60.%20Cloud%20IAM%20and%20Least%20Privilege%20Lab.md) |
| 61 | [Detection Engineering with Sigma and ATT&CK](61.%20Detection%20Engineering%20with%20Sigma%20and%20ATT%26CK.md) |
| 62 | [Security Review for AI Applications](62.%20Security%20Review%20for%20AI%20Applications.md) |
| 63 | [Kubernetes Security and Workload Isolation](63.%20Kubernetes%20Security%20and%20Workload%20Isolation.md) |
| 64 | [Secrets Management and Credential Lifecycle](64.%20Secrets%20Management%20and%20Credential%20Lifecycle.md) |
| 65 | [Threat Hunting with Hypothesis-Driven Queries](65.%20Threat%20Hunting%20with%20Hypothesis-Driven%20Queries.md) |
| 66 | [Secure Architecture Review and Abuse Cases](66.%20Secure%20Architecture%20Review%20and%20Abuse%20Cases.md) |
| 67 | [Security Metrics, Risk Register and Remediation Verification](67.%20Security%20Metrics%2C%20Risk%20Register%20and%20Remediation%20Verification.md) |
| 68 | [Zero Trust and Network Segmentation](68.%20Zero%20Trust%20and%20Network%20Segmentation.md) |
| 69 | [Vulnerability Management and Risk-Based Prioritization](69.%20Vulnerability%20Management%20and%20Risk-Based%20Prioritization.md) |
| 70 | [Secure AI Red Teaming and Evaluation](70.%20Secure%20AI%20Red%20Teaming%20and%20Evaluation.md) |
| 71 | [Digital Forensics Readiness and Chain of Custody](71.%20Digital%20Forensics%20Readiness%20and%20Chain%20of%20Custody.md) |
| 72 | [Final Capstone — Purple-Team Assessment and Executive Report](72.%20Final%20Capstone%20%E2%80%94%20Purple-Team%20Assessment%20and%20Executive%20Report.md) |

### Security Operations and Resilience (modules 73–86)

| # | Module |
|:-:|---|
| 73 | [Security Operations Center Fundamentals and Alert Triage](73.%20Security%20Operations%20Center%20Fundamentals%20and%20Alert%20Triage.md) |
| 74 | [Log Analysis and Security Data Pipelines](74.%20Log%20Analysis%20and%20Security%20Data%20Pipelines.md) |
| 75 | [Purple Teaming and Detection Validation](75.%20Purple%20Teaming%20and%20Detection%20Validation.md) |
| 76 | [Business Continuity, Tabletop Exercises and Crisis Communication](76.%20Business%20Continuity%2C%20Tabletop%20Exercises%20and%20Crisis%20Communication.md) |
| 77 | [Security Automation with Python Safely](77.%20Security%20Automation%20with%20Python%20Safely.md) |
| 78 | [Final Mastery Review and Continuous Learning Plan](78.%20Final%20Mastery%20Review%20and%20Continuous%20Learning%20Plan.md) |
| 79 | [Security Awareness and Phishing Resilience](79.%20Security%20Awareness%20and%20Phishing%20Resilience.md) |
| 80 | [Home and Small-Office Network Hardening](80.%20Home%20and%20Small-Office%20Network%20Hardening.md) |
| 81 | [Encryption and Secure Data Handling Basics](81.%20Encryption%20and%20Secure%20Data%20Handling%20Basics.md) |
| 82 | [Security Governance, Policy and Compliance Basics](82.%20Security%20Governance%2C%20Policy%20and%20Compliance%20Basics.md) |
| 83 | [Vulnerability Scoring and Prioritization with CVSS](83.%20Vulnerability%20Scoring%20and%20Prioritization%20with%20CVSS.md) |
| 84 | [Secure Logging and Monitoring Architecture](84.%20Secure%20Logging%20and%20Monitoring%20Architecture.md) |
| 85 | [Incident Response Playbooks and Runbooks](85.%20Incident%20Response%20Playbooks%20and%20Runbooks.md) |
| 86 | [Resilience Engineering and Recovery Drills](86.%20Resilience%20Engineering%20and%20Recovery%20Drills.md) |

## Guides, templates and assessments

| Resource | Purpose |
|---|---|
| [2026 Update Guide](2026-UPDATE-GUIDE.md) | Learning order, safe lab rules, freshness checklist |
| [Learning Roadmap](LEARNING-ROADMAP-2026.md) | Flexible 12-week plan |
| [Lab Safety and Setup](LAB-SAFETY-AND-SETUP.md) | Isolation, snapshots, data handling |
| [Setup guide](SETUP-WINDOWS-LINUX-TERMUX-2026.md) | Windows, Linux and Android Termux |
| [Quality checklist](CHECKLIST-2026.md) | Per-engagement quality and safety checks |
| [Security glossary](GLOSSARY.md) | Key terms |
| [Module index](docs/MODULE-INDEX.md) | Per-module reading time and goals (generated) |
| [Templates](templates/) | Scope, threat model, finding report, incident timeline, assessment report, daily plan |
| [Assessments](assessments/) | Knowledge check and practical assessment pack with rubric |

## Offline labs

All labs use the Python standard library, make no external network connections, and operate on synthetic data.

| Script | Purpose |
|---|---|
| `labs/audit_local_headers.py`, `labs/local_header_lab.py` | Loopback-only HTTP security-header check with a strict target guard |
| `labs/parse_auth_events.py` | Summarize synthetic authentication events |
| `labs/detect_auth_anomalies.py` | Flag repeated failures followed by a success (`--csv` export) |
| `labs/validate_events.py` | Validate schema, UTC timestamps and documentation-reserved IPs |
| `labs/detection_rules.py` | Minimal rule engine over synthetic events |
| `labs/risk_register.py` | Rank risks by likelihood × impact |
| `labs/cvss_calculator.py` | CVSS v3.1 base-score calculator |
| `labs/integrity_check.py` | SHA-256 baseline and verify for a folder |
| `labs/password_policy_check.py` | Toy passphrase-policy checker (use made-up examples only) |
| `labs/check_pinned_deps.py` | Flag unpinned dependencies |
| `labs/check_course_links.py` | Verify README links |

## Offline dashboard

`dashboard/index.html` tracks module completion, study sessions and streaks, reading-time estimates, per-module notes, quizzes with explanations and attempt history, flashcards, a focus timer, a lab journal and Markdown/JSON exports.
It makes **no network requests**; data stays in your browser's local storage. Export a backup regularly.
The achievement page is a self-study record, **not** a professional certification.

## Repository layout

```
.
├── NN. <module>.md        # curriculum modules
├── dashboard/             # offline study dashboard
├── labs/                  # offline lab scripts and tests
├── tools/                 # quality gates, secret scan, release builder
├── docs/                  # architecture notes
├── templates/ assessments/ changelog/
├── .github/               # CI, issue forms, PR template
└── LICENSE NOTICE.md SECURITY.md SUPPORT.md CONTRIBUTING.md CODE_OF_CONDUCT.md
└── CITATION.cff VERSION CHANGELOG.md ROADMAP.md FAQ.md Makefile pyproject.toml
```

## Quality gates

`make check` runs byte-compilation, all unit tests, `tools/check_markdown.py` (links and headings), `tools/scan_secrets.py`, `tools/module_index.py --check` and `tools/check_project.py`. The project gate verifies contiguous module numbering,
README coverage of every module, dashboard/module consistency, and version consistency across `VERSION`, `CHANGELOG.md`,
`pyproject.toml` and `CITATION.cff`. CI repeats these on Python 3.9–3.13 and syntax-checks the dashboard JavaScript.

## Contributing, security and conduct

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), [SUPPORT.md](SUPPORT.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [FAQ.md](FAQ.md), [ROADMAP.md](ROADMAP.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/RELEASE-CHECKLIST.md](docs/RELEASE-CHECKLIST.md).
Build a verifiable release archive with `make release`; enable local hooks with `pre-commit install`.
Release history is in [CHANGELOG.md](CHANGELOG.md).

## Maintenance note

This is learning material, not a claim that every original command or script has been audited on every 2026 platform.
Verify tool instructions against official documentation and keep labs isolated.

## License and attribution

Original 2026 additions are released under the [MIT License](LICENSE). Upstream course notes (units 01–28) are not relicensed; see [NOTICE.md](NOTICE.md).

## Credits

Original course notes based on TCM Security's Practical Ethical Hacking. 2026 supplementary modules, labs, tooling and dashboard maintained by HARPREETSING.
