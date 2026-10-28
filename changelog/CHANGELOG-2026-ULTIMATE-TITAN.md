# Changelog — 2026 Ultimate Titan

## Added
- Modules 73–78: SOC triage, log pipelines, purple-team detection validation, tabletop/crisis communication, safe security automation, and a final mastery review with a 90-day plan.
- `labs/detect_auth_anomalies.py` with unit tests (offline, synthetic data only).
- Dashboard now lists all 78 modules and 67 knowledge-check questions.
- CI workflow runs the new detector tests and lab.

## Features added in this update
- `labs/validate_events.py`: schema, UTC and documentation-IP validator for synthetic events (Module 74).
- `labs/risk_register.py` + `sample-risks.csv`: likelihood x impact ranking with bands (Modules 67/69).
- `labs/check_course_links.py`: offline README link checker (also runs in CI).
- `detect_auth_anomalies.py --csv` export option.
- Dashboard: module search filter and per-question explanations after grading.

## Features added in update 3
- Modules 79–80: security awareness/phishing resilience and home/small-office hardening (dashboard now lists 80).
- `labs/password_policy_check.py` and `labs/check_pinned_deps.py` with tests (offline).
- Dashboard: study streak and light/dark theme toggle.

## Features added in update 4
- Modules 81–82: encryption/secure data handling and governance/compliance basics (dashboard lists 82).
- `labs/integrity_check.py` (SHA-256 baseline/verify) with tests.
- Dashboard: flashcards (flip, next, random).

## Features added in update 5
- Modules 83–84: CVSS scoring/prioritization and secure logging architecture (dashboard lists 84).
- `GLOSSARY.md`: English security glossary.
- `labs/cvss_calculator.py` (CVSS v3.1 base scores) with tests.
- Dashboard: downloadable Markdown study report.

## Features added in update 6
- Modules 85–86: incident response playbooks and resilience/recovery drills (dashboard lists 86).
- `labs/detection_rules.py`: small rule engine over synthetic events, with tests.
- Dashboard: 10 more quiz questions (77 total) and a 25-minute focus timer.

## Safety
Synthetic data and owned/authorized labs only. The dashboard makes no network requests. The achievement page is a learning record, not an accreditation. Original TCM Security attribution is unchanged.
