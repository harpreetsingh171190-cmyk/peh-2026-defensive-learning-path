import tempfile
import unittest
from pathlib import Path
import check_markdown as cm


class MarkdownTests(unittest.TestCase):
    def test_detects_broken_and_accepts_root_relative(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "dir").mkdir()
            (root / "dir" / "file.py").write_text("x")
            (root / "a.md").write_text("# A\n[ok](/dir/file.py) [bad](missing.md) [web](https://example.com)")
            self.assertEqual(cm.broken_links(root), ["a.md: broken link -> missing.md"])

    def test_missing_h1(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "b.md").write_text("no heading here")
            self.assertEqual(cm.missing_h1(Path(tmp)), ["b.md: no level-1 heading"])

    def test_repository_passes(self):
        self.assertEqual(cm.run(), [])


if __name__ == "__main__":
    unittest.main()
