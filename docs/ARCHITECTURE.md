# Architecture

## Components
| Component | Path | Notes |
|---|---|---|
| Curriculum | `NN. <title>.md` | One file per module, numbered contiguously |
| Offline dashboard | `dashboard/index.html` | Single file; vanilla JS; local storage; no network (CSP `connect-src 'none'`) |
| Labs | `labs/` | Standard library only; synthetic data; unit-tested |
| Quality gates | `tools/` | Project, Markdown, secret-scan and release tooling |
| Generated docs | `docs/MODULE-INDEX.md` | Built by `tools/module_index.py`; a gate fails if stale |
| CI | `.github/workflows/` | Matrix tests, gates, dashboard syntax check, tagged releases |

## Design principles
1. **Offline-first:** nothing requires an account or network access.
2. **Fail closed:** labs that could touch a network allow-list loopback targets only.
3. **Reproducible:** `make check` locally equals CI.
4. **Traceable:** `VERSION`, `CHANGELOG.md`, `pyproject.toml` and `CITATION.cff` must agree (enforced).

## Release flow
1. Update `VERSION`, `pyproject.toml`, `CITATION.cff`, `CHANGELOG.md`.
2. `make check && make release`.
3. Tag `vX.Y.Z` and push; the release workflow re-runs gates and publishes the archive with checksums.
