# Release Checklist

1. [ ] Update `VERSION`, `pyproject.toml`, `CITATION.cff` and add a `CHANGELOG.md` entry (all must match).
2. [ ] If modules changed: update `README.md` and the dashboard `moduleNames`, then run `make index`.
3. [ ] `make check` passes locally (tests, project gate, Markdown gate, secret scan, module index).
4. [ ] Open `dashboard/index.html` in a browser: progress, quiz, notes, export/import and the study report work.
5. [ ] `make release`; verify `SHA256SUMS` matches the archive.
6. [ ] Commit, tag `vX.Y.Z`, push the tag; confirm the release workflow publishes the archive.
7. [ ] Review CodeQL results and any Dependabot pull requests.
