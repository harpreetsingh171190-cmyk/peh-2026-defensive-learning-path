import unittest
from detect_auth_anomalies import find_anomalies, parse_ts


def ev(ts, kind, user="demo-a", src="192.0.2.1"):
    return {"_ts": parse_ts(ts), "event": kind, "user": user, "source": src}


class DetectorTests(unittest.TestCase):
    def test_flags_three_failures_then_success(self):
        events = [ev("2026-10-01T10:00:00Z", "login_failure"),
                  ev("2026-10-01T10:00:10Z", "login_failure"),
                  ev("2026-10-01T10:00:20Z", "login_failure"),
                  ev("2026-10-01T10:00:30Z", "login_success")]
        self.assertEqual(find_anomalies(events), [("demo-a", "192.0.2.1", 3)])

    def test_ignores_old_failures(self):
        events = [ev("2026-10-01T10:00:00Z", "login_failure")] * 3 + [ev("2026-10-01T11:00:00Z", "login_success")]
        self.assertEqual(find_anomalies(events), [])

    def test_ignores_two_failures(self):
        events = [ev("2026-10-01T10:00:00Z", "login_failure"),
                  ev("2026-10-01T10:00:05Z", "login_failure"),
                  ev("2026-10-01T10:00:10Z", "login_success")]
        self.assertEqual(find_anomalies(events), [])


if __name__ == "__main__":
    unittest.main()
