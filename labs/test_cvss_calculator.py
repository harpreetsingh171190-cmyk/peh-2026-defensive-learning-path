import unittest
from cvss_calculator import base_score, rating


class CvssTests(unittest.TestCase):
    def test_critical_network(self):
        self.assertEqual(base_score("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"), 9.8)

    def test_scope_changed(self):
        self.assertEqual(base_score("CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N"), 6.1)

    def test_no_impact_is_zero(self):
        self.assertEqual(base_score("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N"), 0.0)

    def test_rating_bands(self):
        self.assertEqual([rating(x) for x in (0, 3.9, 6.9, 8.9, 9.8)], ["None", "Low", "Medium", "High", "Critical"])

    def test_bad_vector(self):
        with self.assertRaises(ValueError):
            base_score("AV:N/AC:L")


if __name__ == "__main__":
    unittest.main()
