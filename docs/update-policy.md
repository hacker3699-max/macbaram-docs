# Update publication policy

MacBaram uses this repository as the durable public record of released, user-visible changes. The official website remains the only download and commercial source.

## Canonical record

[`CHANGELOG.md`](../CHANGELOG.md) is the canonical public update-note file. Ordinary documentation commits are not product releases and must not be interpreted as such.

GitHub Releases and Discussions are not currently used for product announcements. This avoids an empty community surface and avoids implying that GitHub hosts the MacBaram installer.

## Binary release note

A versioned entry is added only after all of the following are true:

1. the signed and notarized package has been promoted to the official production download channel;
2. the canonical `/download` route and public release manifest have been read back successfully;
3. the public version and date are verified;
4. each note describes a user-visible change that exists in that public build;
5. known public limitations and safety changes are included when applicable.

No version-specific package URL is published here.

## Operational note

A dated `Operational` entry may be added without a new binary when a server-side or compatibility-policy change materially changes public user behavior. It must not expose payment, licensing, customer, security, or internal implementation details.

## Corrections and withdrawals

Published history is not silently rewritten to hide an error. A material correction or withdrawn claim receives a dated note explaining the public effect. Sensitive details remain private.

## Future notification channels

After several real public releases have accumulated, notes-only GitHub Releases may be evaluated as an optional notification channel. They will be rejected if users mistake repository source archives for the MacBaram installer or if the duplicate release surface begins to drift from the changelog.
