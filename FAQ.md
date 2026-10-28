# Frequently Asked Questions

**Is this a certification course?** No. It is self-study material. The dashboard record is not an accreditation.

**Can I use the labs on real systems?** Only systems you own or have written authorization to test. The labs are designed for synthetic data and loopback targets.

**Does the dashboard send my data anywhere?** No. It has no network requests (enforced by a Content-Security-Policy and a CI check) and stores data in your browser. Export backups regularly.

**Why are some original notes unchanged?** Units 01–28 are upstream course notes; they are preserved with attribution. See [NOTICE.md](NOTICE.md).

**How do I run all checks?** `make check`. See [CONTRIBUTING.md](CONTRIBUTING.md).

**How do I build a release archive?** `make release` creates `dist/peh-2026-vX.Y.Z.zip` and `SHA256SUMS`.
