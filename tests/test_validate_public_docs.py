from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts/validate_public_docs.py"
SPEC = importlib.util.spec_from_file_location("validate_public_docs", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ForbiddenContentTests(unittest.TestCase):
    def labels(self, text: str) -> set[str]:
        return {
            label
            for label, pattern in VALIDATOR.FORBIDDEN_PATTERNS.items()
            if pattern.search(text)
        }

    def test_canonical_download_is_allowed(self) -> None:
        self.assertEqual(self.labels("https://www.macbaram.com/download"), set())

    def test_version_specific_package_is_rejected(self) -> None:
        labels = self.labels("https://www.macbaram.com/files/MacBaram-1.2.3.pkg")
        self.assertIn("version-specific package URL", labels)

    def test_technical_download_paths_are_rejected(self) -> None:
        self.assertIn("technical download path", self.labels("/downloads/latest.json"))

    def test_price_is_rejected(self) -> None:
        self.assertIn("duplicated dollar price", self.labels("Only $4.99"))

    def test_commercial_state_is_rejected(self) -> None:
        self.assertIn("duplicated commercial state", self.labels("A free trial is available"))

    def test_internal_path_is_rejected(self) -> None:
        self.assertIn("private local path", self.labels("/Users/example/private.log"))

    def test_secret_like_assignment_is_rejected(self) -> None:
        self.assertIn("token-like secret", self.labels("access_token = hidden"))

    def test_imac_support_claim_is_rejected(self) -> None:
        self.assertIn("iMac support claim", self.labels("iMac is fully supported"))

    def test_imac_boundary_is_allowed(self) -> None:
        self.assertEqual(self.labels("iMac support is not currently declared"), set())

    def test_marketing_cta_does_not_bypass_download_canonical(self) -> None:
        self.assertEqual(self.labels("Official Download: https://www.macbaram.com/download"), set())


if __name__ == "__main__":
    unittest.main()
