# Contributing to aion2-trainer

Thanks for wanting to help. This is a hobbyist AION 2 trainer project — contributions
are welcome from anyone who has spent time reverse-engineering the AION 2 client or
just wants to improve the overlay.

## Ground rules

- Every PR must target a specific AION 2 client build (patch version in the PR title).
- Do not commit memory dumps, sig scans, or offset caches — they belong in `dumps/`
  and are gitignored.
- New features need a handler in `handlers/` and a matching test in `tests/`.
- Keep the trainer usable offline — no telemetry, no phoning home.

## Local setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m aion2_trainer
```

## Offset updates

When AION 2 patches, run `tools/sigscan.py` against the new `aion2.exe` and update
`offsets/current.json`. Attach the scan log to your PR.

## Code style

- Python 3.11+, type hints on public functions.
- No global state outside `models/state.py`.
- Feature handlers must be registered through `core/registry.py`.