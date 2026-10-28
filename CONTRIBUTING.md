# Contributing

Thanks for helping improve this course. Please read `ETHICS-AND-ACCEPTABLE-USE.md` first.

## Workflow
1. Fork and create a branch (`feature/short-name`).
2. Make focused changes. Keep modules numbered contiguously and update `README.md`,
   `dashboard/index.html` (`moduleNames`) and `CHANGELOG.md`.
3. Run the quality gates locally:
   ```bash
   make check      # compile, unit tests, project checks
   ```
4. Open a pull request using the template.

## Standards
- **Content:** defensive framing, authorization first, synthetic data, remediation and verification steps.
- **Python:** standard library only, offline by default, type-safe argument handling, unit tests for new logic.
- **Safety:** any script that touches a network must hard-restrict targets (see `labs/audit_local_headers.py`).
- **Docs:** clear headings, short paragraphs, checklists, no secrets.
- **Commits:** imperative mood, e.g. "Add module 87 on ...".

## Adding a module
Create `NN. Title.md` with Goal, Key ideas, Lab and Self-check sections, add it to the README
curriculum list and the dashboard list, and add any quiz questions with explanations.
