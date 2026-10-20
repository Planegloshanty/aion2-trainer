# Security Policy

## Scope

This repository is an AION 2 trainer — a memory-reading and input-injection tool
for the Windows AION 2 client. It is intended **for educational purposes and
single-player / private-server use only**. Using it on official live servers will
get your account banned and is not supported.

## Reporting a vulnerability

If you find a security issue in the trainer itself (not in AION 2), open a private
security advisory on GitHub or email `sec@aion2-trainer.local`.

Please include:

- Trainer version (`python -m aion2_trainer --version`)
- AION 2 client build
- Steps to reproduce
- Whether the issue requires elevated privileges

## Anti-cheat notice

The trainer does **not** ship anti-cheat bypasses. If you are looking for a
bypass for AION 2's live anti-cheat, this is the wrong project — go file a
feature request and it will be closed.

## Supported versions

| Trainer | AION 2 build | Status |
|---------|--------------|--------|
| 0.9.x   | 2.4.x        | active |
| 0.8.x   | 2.3.x        | maintenance |