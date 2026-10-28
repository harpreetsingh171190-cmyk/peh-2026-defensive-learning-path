#!/usr/bin/env python3
"""Build a clean release archive plus SHA256SUMS. Offline, standard library only.

  python tools/build_release.py [OUTPUT_DIR]
Produces: peh-2026-vX.Y.Z.zip and SHA256SUMS in OUTPUT_DIR (default: dist/).
"""
import hashlib
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".git", "__pycache__", "dist", "node_modules", ".venv", ".idea", ".vscode"}
EXCLUDE_SUFFIXES = {".pyc", ".log", ".pem", ".key"}
EXCLUDE_NAMES = {".DS_Store", ".env", "study-report.md"}


def release_files(root=ROOT):
    files = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if not path.is_file() or any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if path.suffix in EXCLUDE_SUFFIXES or path.name in EXCLUDE_NAMES:
            continue
        files.append(rel)
    return files


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build(root=ROOT, out_dir=None):
    root = Path(root)
    out_dir = Path(out_dir) if out_dir else root / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    archive = out_dir / f"peh-2026-v{version}.zip"
    prefix = f"peh-2026-v{version}"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for rel in release_files(root):
            info = zipfile.ZipInfo(f"{prefix}/{rel.as_posix()}", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, (root / rel).read_bytes())
    sums = out_dir / "SHA256SUMS"
    sums.write_text(f"{sha256(archive)}  {archive.name}\n", encoding="utf-8")
    return archive, sums


if __name__ == "__main__":
    archive, sums = build(ROOT, sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"Built {archive}")
    print(sums.read_text(encoding="utf-8").strip())
