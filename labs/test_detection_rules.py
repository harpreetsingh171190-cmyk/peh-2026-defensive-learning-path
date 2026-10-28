import unittest
from detection_rules import evaluate, matches, RULES


class RuleTests(unittest.TestCase):
    def test_matches(self):
        self.assertTrue(matches(RULES[0], {"event": "login_failure", "user": "x"}))
        self.assertFalse(matches(RULES[0], {"event": "login_success"}))

    def test_evaluate_counts(self):
        events = [{"event": "login_failure"}, {"event": "login_failure"}, {"event": "login_success"}]
        hits = evaluate(events)
        self.assertEqual(len(hits["R-001"]), 2)
        self.assertEqual(len(hits["R-002"]), 1)

    def test_no_events(self):
        self.assertEqual(evaluate([]), {})


if __name__ == "__main__":
    unittest.main()
