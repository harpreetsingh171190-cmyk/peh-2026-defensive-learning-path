import unittest
from risk_register import band, load_risks
from pathlib import Path


class RiskTests(unittest.TestCase):
    def test_bands(self):
        self.assertEqual((band(4), band(8), band(15)), ("low", "medium", "high"))

    def test_sorted_and_closed_excluded(self):
        risks = load_risks(Path(__file__).with_name("sample-risks.csv"))
        scores = [r["score"] for r in risks]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertNotIn("R4", [r["id"] for r in risks])


if __name__ == "__main__":
    unittest.main()
