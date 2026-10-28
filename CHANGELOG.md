# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/). Detailed historical release notes are kept in [`changelog/`](changelog/).

## [3.3.0] - 2026-10-28

### Added
- `templates/rules-of-engagement-template.md`: pre-engagement authorization document (scope, constraints, testing windows, stop-work trigger, sign-off).
- `templates/executive-summary-template.md`: non-technical, client-facing summary to pair with `SECURITY-ASSESSMENT-REPORT.md`.
- `labs/report_builder.py` (+ tests, `labs/sample-findings.json`): consolidates individual synthetic findings (as authored with `finding-report-template.md`) into one severity-sorted Markdown report.
- Dashboard: "Progress by section" breakdown (ten-module bands) and a "Export study plan (.ics)" button that turns remaining modules into a local calendar schedule — no network request, offline file download only.

## [3.2.0] - 2026-10-28

### Added
- `tools/module_index.py` and generated `docs/MODULE-INDEX.md`: per-module reading time, track and stated goal; a gate fails when it is stale (`make index` refreshes it).
- Dashboard: per-module reading-time estimates, estimated reading time remaining, and per-module notes (stored locally; included in the study report count).
- CodeQL analysis workflow (Python and JavaScript) and a weekly schedule.
- `docs/RELEASE-CHECKLIST.md`.

### Changed
- `make check`, CI and pre-commit now verify that the module index and dashboard metadata are current.

## [3.1.0] - 2026-10-28

### Added
- `tools/check_markdown.py`: Markdown hygiene gate (relative and root-relative links, H1 headings).
- `tools/scan_secrets.py`: offline high-confidence secret scanner with allow-list support.
- `tools/build_release.py`: reproducible release archive plus `SHA256SUMS`; `make release`.
- Release workflow (`.github/workflows/release.yml`) that re-runs gates, verifies the tag equals `VERSION`, and publishes the archive.
- `.pre-commit-config.yaml` with standard hooks and the project gates.
- `SUPPORT.md`, `ROADMAP.md`, `FAQ.md`, `docs/ARCHITECTURE.md`.
- Dashboard Content-Security-Policy (`connect-src 'none'`) and a gate that fails if the dashboard gains network calls.

### Changed
- CI runs the new gates on every push and pull request; `make check` runs them locally.

## [3.0.0] - 2026-10-28

### Added
- Professional project scaffolding: `LICENSE`, `NOTICE.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `ETHICS-AND-ACCEPTABLE-USE.md`, `CITATION.cff`, `VERSION`, `pyproject.toml`, `Makefile`, `.editorconfig`.
- GitHub issue forms, pull-request template and Dependabot configuration for Actions.
- `tools/check_project.py` quality gate: module numbering, README coverage, dashboard/module-count consistency, version consistency.
- CI matrix across Python 3.9–3.13, dashboard JavaScript syntax check, and project quality gate.
- Dashboard: accessibility improvements (skip link, visible focus), print stylesheet, quiz attempt history, version footer.

### Changed
- Dashboard module checklist now maps one-to-one to the 86 module files; the progress storage key moved to `v2`. Study sessions, journal and quiz scores migrate automatically; module completion ticks from older versions do not (their indexes did not match real modules) and must be re-marked.
- README rewritten as a structured, complete curriculum index.
- Historical changelogs moved to `changelog/`; README links updated.

## [2.x] - 2026-10
- Modules 73–86, defensive labs (anomaly detection, event validation, risk register, link checker, password policy, dependency pinning, integrity check, CVSS calculator, rule engine), dashboard search, flashcards, timer, study report and streaks.
- See `changelog/CHANGELOG-2026-ULTIMATE-TITAN.md`.

## [1.x] - 2026
- Original course notes plus modules 29–72 and the first offline dashboard.
- See the other files in `changelog/`.
