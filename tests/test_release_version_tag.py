"""Regression tests for versioned release tag validation."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("release_version", ROOT / "scripts" / "release_version.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

class ReleaseVersionTagTests(unittest.TestCase):
    def test_accepted(self):
        for value in ("0.4.0", "0.4.0-alpha.4", "0.4.0-beta.2", "0.4.0-rc.1"):
            with self.subTest(value=value):
                self.assertIsNotNone(MOD.VERSION_RE.fullmatch(value))

    def test_rejected(self):
        for value in ("", "v0.4.0", "0.4", "0.4.0-rc", "0.4.0-nightly.1", "0.4.0-alpha.1;echo bad"):
            with self.subTest(value=value):
                self.assertIsNone(MOD.VERSION_RE.fullmatch(value))

if __name__ == "__main__":
    unittest.main()
