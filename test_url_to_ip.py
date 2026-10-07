import unittest

from url_to_ip import resolve_host


class ResolveHostTests(unittest.TestCase):
    def test_accepts_url(self):
        self.assertEqual(resolve_host("https://example.com/path?x=1"), "example.com")

    def test_accepts_hostname(self):
        self.assertEqual(resolve_host("example.com"), "example.com")

    def test_strips_path_from_plain_hostname(self):
        self.assertEqual(resolve_host("example.com/path"), "example.com")

    def test_strips_port_from_plain_hostname(self):
        self.assertEqual(resolve_host("example.com:8080"), "example.com")

    def test_handles_ipv6_literal(self):
        self.assertEqual(resolve_host("https://[::1]:8080"), "::1")

    def test_requires_value(self):
        with self.assertRaises(ValueError):
            resolve_host("   ")


if __name__ == "__main__":
    unittest.main()
