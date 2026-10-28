import unittest
import check_project as cp


class ProjectGateTests(unittest.TestCase):
    def test_numbering_detects_gap_and_duplicate(self):
        self.assertEqual(cp.check_numbering({1: ["a"], 3: ["b"]}), ["module 02 is missing"])
        self.assertTrue(cp.check_numbering({1: ["a", "b"]})[0].startswith("module 01 has duplicate"))

    def test_readme_coverage(self):
        self.assertEqual(cp.check_readme_coverage({1: ["x.md"]}, {"x.md"}), [])
        self.assertEqual(len(cp.check_readme_coverage({1: ["x.md"]}, set())), 1)

    def test_repository_passes_gate(self):
        self.assertEqual(cp.run(), [])


if __name__ == "__main__":
    unittest.main()
