import unittest
from check_pinned_deps import unpinned


class PinTests(unittest.TestCase):
    def test_flags_unpinned(self):
        self.assertEqual([n for n, _ in unpinned(["a==1.0", "b>=2", "c", "# note", ""])], [2, 3])

    def test_ignores_comments_and_options(self):
        self.assertEqual(unpinned(["-r other.txt", "x==1  # ok"]), [])


if __name__ == "__main__":
    unittest.main()
