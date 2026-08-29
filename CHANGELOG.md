# MacBaram public update notes

This file records user-visible changes after a MacBaram release is promoted to the official download channel. It is not generated from every internal commit, and it does not announce unreleased experiments or roadmap items.

The official installer remains available only from [https://www.macbaram.com/download](https://www.macbaram.com/download).

## [Unreleased]

No public changes are announced here until release promotion is complete.

## Release entry template

The template below is copied only after the released version, date, public behavior, and official download readback are verified. Empty sections are removed.

```markdown
## [VERSION] - YYYY-MM-DD

### Added
- New user-visible capability.

### Changed
- Existing behavior that changed.

### Fixed
- User-visible problem that was corrected.

### Operational
- A server-side or compatibility-policy change that materially affected user-visible behavior without a new installer.

### Safety
- Fail-closed, restore, permission, or safety-boundary change.

### Known limitations
- Confirmed limitation that remains in this release.
```

Release notes must describe observable behavior, not internal implementation claims. They must not add a version-specific installer URL, current price or commercial state, unsupported model claim, or unverified performance or lifespan result. A dated `Operational` entry may document a user-visible server-side or compatibility-policy change that does not require a new installer. It must not reveal payment, licensing, security, or customer details.
