# Safety and permissions

MacBaram manages system-level fan, charging, and sleep controls. Those actions require more access than a normal document or media app.

## Local privileged service

MacBaram uses a local privileged service for supported system controls. The service is installed as part of the official, signed MacBaram package. Download the installer only from [the official download address](https://www.macbaram.com/download).

## Fail-closed behavior

MacBaram exposes a control only after the required capability is verified on the current Mac. Missing, unknown, or unsupported capability keeps that control unavailable. This is especially important across Mac models whose fan, battery, and power behavior differs.

## Returning toward macOS defaults

Disabling a control, quitting the app, or reaching a configured safety condition is designed to return the affected behavior toward macOS defaults where applicable. A user should still verify the resulting state before leaving an important workload unattended.

## Limits

MacBaram does not promise:

- a specific performance increase;
- a particular throttling outcome;
- a particular battery-lifespan result;
- uninterrupted work, networking, or power;
- protection from every heat, battery, storage, software, or hardware failure.

Keep adequate ventilation, use a suitable power source, maintain backups, and monitor important workloads. Never use MacBaram as the only safeguard for data or equipment.

## Diagnostic privacy

Do not publish full logs or raw diagnostic archives in GitHub issues. They may contain account, device, file-path, or network information. Follow [SUPPORT.md](../SUPPORT.md) for a safe report.
