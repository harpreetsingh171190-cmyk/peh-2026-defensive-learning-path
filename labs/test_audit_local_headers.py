import unittest
from audit_local_headers import validate_loopback_url

class LoopbackGuardTests(unittest.TestCase):
    def test_accepts_ipv4_loopback(self):
        self.assertEqual(validate_loopback_url("http://127.0.0.1:8765"), "http://127.0.0.1:8765")

    def test_accepts_ipv6_loopback(self):
        self.assertEqual(validate_loopback_url("http://[::1]:8000"), "http://[::1]:8000")

    def test_rejects_external_ip(self):
        with self.assertRaises(ValueError):
            validate_loopback_url("http://192.0.2.1")

    def test_rejects_hostname(self):
        with self.assertRaises(ValueError):
            validate_loopback_url("https://example.com")

    def test_rejects_invalid_scheme(self):
        with self.assertRaises(ValueError):
            validate_loopback_url("ftp://127.0.0.1")

if __name__ == "__main__":
    unittest.main()
