import unittest
from validate_events import check_event, validate_file
from pathlib import Path

GOOD = {"timestamp": "2026-10-01T10:00:00Z", "event": "login_failure", "user": "demo-a", "source": "192.0.2.5"}


class ValidateTests(unittest.TestCase):
    def test_good_event(self):
        self.assertEqual(check_event(GOOD), [])

    def test_missing_field(self):
        bad = dict(GOOD); del bad["user"]
        self.assertIn("missing field: user", check_event(bad))

    def test_non_utc(self):
        self.assertIn("timestamp is not UTC", check_event({**GOOD, "timestamp": "2026-10-01T10:00:00+05:30"}))

    def test_public_ip_rejected(self):
        self.assertTrue(check_event({**GOOD, "source": "8.8.8.8"}))

    def test_sample_file_valid(self):
        self.assertEqual(validate_file(Path(__file__).with_name("sample-auth-events.jsonl")), [])


if __name__ == "__main__":
    unittest.main()
