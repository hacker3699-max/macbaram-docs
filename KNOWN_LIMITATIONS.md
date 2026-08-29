# Known limitations

This page records current public boundaries that are useful before installation or support. It is not a roadmap.

## Hardware support

- Intel Macs are unsupported.
- iMac support is not currently declared. Controls remain unavailable when the required capability cannot be verified.
- A fanless Mac has no fan control.
- A desktop Mac has no portable battery controls.
- A model-family name alone does not establish that every control is available; MacBaram checks the required capability on the current Mac.

## Workload continuity

Sleep prevention addresses normal system sleep while it is active. It cannot guarantee that an application, network connection, external service, power source, or workload will continue running.

At the user-configured low-battery threshold, MacBaram can release sleep prevention so macOS may return to its normal sleep behavior. That boundary can intentionally allow a long-running job to stop.

## Hardware outcomes

MacBaram provides controls and visibility. It does not promise a specific performance, throttling, temperature, battery-health, or hardware-lifespan result.

## Reporting a new limitation

Use a public issue only for a reproducible, non-sensitive behavior. Follow [SUPPORT.md](SUPPORT.md) and remove account, payment, license, device, path, and diagnostic information before posting.

This document is updated when a limitation is verified for the public release. Speculation and approval-pending work remain private.
