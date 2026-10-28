import unittest
import module_index as mi


class IndexTests(unittest.TestCase):
    def test_reading_minutes_ignores_code_and_has_minimum(self):
        text = "word " * 400 + "\n```\n" + "code " * 5000 + "\n```\n"
        self.assertEqual(mi.reading_minutes(text), 3)
        self.assertEqual(mi.reading_minutes("word " * 1000), 5)
        self.assertEqual(mi.reading_minutes("tiny"), 3)

    def test_extract_goal(self):
        text = "# T\n\n## Goal\nLearn **safe** triage.\nSecond line.\n\nMore.\n\n## Next\nx"
        self.assertEqual(mi.extract_goal(text), "Learn safe triage. Second line.")
        self.assertEqual(mi.extract_goal("# T\nno goal"), "")

    def test_goal_truncated(self):
        self.assertTrue(mi.extract_goal("## Goal\n" + "a " * 300).endswith("…"))

    def test_apply_meta_is_idempotent(self):
        mods = [{"minutes": 5}, {"minutes": 7}]
        once = mi.apply_meta("x\nconst moduleNames = [\n];", mods)
        self.assertEqual(mi.apply_meta(once, mods), once)
        self.assertIn("const moduleMinutes = [5,7];", once)

    def test_repository_index_is_current(self):
        self.assertEqual(mi.check(), [])


if __name__ == "__main__":
    unittest.main()
