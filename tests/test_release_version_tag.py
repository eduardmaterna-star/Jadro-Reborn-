"""Regression tests for release version validation and CLI behavior."""
import importlib.util
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "release_version.py"
SPEC = importlib.util.spec_from_file_location("release_version", SCRIPT)
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

    def test_check_version_cli_accepts_prerelease(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--check-version", "0.4.0-alpha.6"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "0.4.0-alpha.6")

    def test_check_version_cli_rejects_injection(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--check-version", "0.4.0-alpha.1;echo bad"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("bad\n", result.stdout)

    def test_version_options_are_mutually_exclusive(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--version", "0.4.0", "--check-version", "0.4.0"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
