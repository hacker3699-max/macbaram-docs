# Contributing to the public documentation

MacBaram is closed-source software, but corrections to this public documentation are welcome.

## Suitable contributions

- Fix a broken link or unclear sentence.
- Report a contradiction between two public MacBaram pages.
- Clarify a verified compatibility or troubleshooting boundary.
- Improve accessibility or structure without changing product meaning.

## Not suitable for this repository

- Application source-code changes or reverse-engineered implementation details.
- Unreleased features, roadmap speculation, or approval-pending behavior.
- Prices, trial promises, sales status, or version-specific installer links.
- Logs, raw diagnostics, device identifiers, account or payment data, license data, credentials, or vulnerability details.

## Before opening a pull request

1. Link the public MacBaram page that supports a factual change.
2. Keep the smallest change that corrects the documentation.
3. Run `python3 scripts/validate_public_docs.py`.
4. Confirm that no sensitive or internal material is included.

A passing validation check does not approve a new product claim. Product availability and compatibility changes require MacBaram review before publication.
