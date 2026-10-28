import unittest
import scan_secrets as ss


class ScannerTests(unittest.TestCase):
    def test_detects_private_key_header(self):
        header = "-----BEGIN " + "RSA PRIVATE KEY-----"
        self.assertEqual(ss.scan_text(header), [("Private key block", 1)])

    def test_detects_aws_style_id(self):
        fake = "AKIA" + "ABCDEFGHIJKLMNOP"
        self.assertEqual(ss.scan_text("id = " + fake)[0][0], "AWS access key ID")

    def test_ignores_normal_text(self):
        self.assertEqual(ss.scan_text("Rotate exposed credentials immediately."), [])

    def test_repository_is_clean(self):
        self.assertEqual(ss.scan_repo(), [])


if __name__ == "__main__":
    unittest.main()
