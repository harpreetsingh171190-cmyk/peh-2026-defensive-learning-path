import unittest
from password_policy_check import check, estimate_bits


class PolicyTests(unittest.TestCase):
    def test_short_and_common_rejected(self):
        problems = check("password123")
        self.assertTrue(any("shorter" in p for p in problems))
        self.assertTrue(any("common" in p for p in problems))

    def test_long_passphrase_ok(self):
        self.assertEqual(check("blue-river-lantern-42-demo"), [])

    def test_repetition(self):
        self.assertIn("too much repetition", check("aaaaaaaaaaaaaaaaaa"))

    def test_bits_increase_with_length(self):
        self.assertLess(estimate_bits("abcd"), estimate_bits("abcdefgh"))


if __name__ == "__main__":
    unittest.main()
