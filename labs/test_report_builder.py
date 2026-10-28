import unittest
from pathlib import Path

from report_builder import load_findings, render_report, severity_counts, severity_rank


class ReportBuilderTests(unittest.TestCase):
    def setUp(self):
        self.findings = load_findings(Path(__file__).with_name("sample-findings.json"))

    def test_sorted_by_severity(self):
        self.assertEqual([f["id"] for f in self.findings], ["F-001", "F-002", "F-003"])

    def test_severity_rank_rejects_unknown(self):
        with self.assertRaises(ValueError):
            severity_rank({"id": "X", "severity": "extreme"})

    def test_counts(self):
        counts = severity_counts(self.findings)
        self.assertEqual(counts["critical"], 1)
        self.assertEqual(counts["medium"], 1)
        self.assertEqual(counts["low"], 1)

    def test_report_contains_all_findings_and_table(self):
        report = render_report(self.findings)
        self.assertIn("| Critical | 1 |", report)
        for f in self.findings:
            self.assertIn(f["id"], report)


if __name__ == "__main__":
    unittest.main()
