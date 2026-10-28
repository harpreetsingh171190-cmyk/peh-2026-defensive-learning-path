import tempfile
import unittest
from pathlib import Path
from integrity_check import build_baseline, compare


class IntegrityTests(unittest.TestCase):
    def test_detects_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.txt").write_text("one")
            (root / "b.txt").write_text("two")
            base = build_baseline(root)
            (root / "a.txt").write_text("changed")
            (root / "b.txt").unlink()
            (root / "c.txt").write_text("new")
            result = compare(base, build_baseline(root))
            self.assertEqual(result, {"modified": ["a.txt"], "missing": ["b.txt"], "new": ["c.txt"]})

    def test_no_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "x").write_text("same")
            base = build_baseline(tmp)
            self.assertEqual(compare(base, build_baseline(tmp)), {"modified": [], "missing": [], "new": []})


if __name__ == "__main__":
    unittest.main()
