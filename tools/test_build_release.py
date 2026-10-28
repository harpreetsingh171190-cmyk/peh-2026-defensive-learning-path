import tempfile
import unittest
import zipfile
from pathlib import Path
import build_release as br


class ReleaseTests(unittest.TestCase):
    def make_tree(self, root):
        (root / "VERSION").write_text("9.9.9\n")
        (root / "keep.md").write_text("# keep")
        (root / "__pycache__").mkdir()
        (root / "__pycache__" / "x.pyc").write_bytes(b"x")
        (root / "secret.pem").write_text("nope")

    def test_excludes_junk_and_writes_checksum(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "src"
            root.mkdir()
            self.make_tree(root)
            archive, sums = br.build(root, Path(tmp) / "out")
            with zipfile.ZipFile(archive) as bundle:
                names = bundle.namelist()
            self.assertIn("peh-2026-v9.9.9/keep.md", names)
            self.assertFalse(any("pycache" in n or n.endswith(".pem") for n in names))
            self.assertTrue(sums.read_text().startswith(br.sha256(archive)))

    def test_build_is_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "src"
            root.mkdir()
            self.make_tree(root)
            a1, _ = br.build(root, Path(tmp) / "o1")
            a2, _ = br.build(root, Path(tmp) / "o2")
            self.assertEqual(br.sha256(a1), br.sha256(a2))


if __name__ == "__main__":
    unittest.main()
