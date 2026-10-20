"""Scan a fresh aion2.exe for the offsets used by handlers."""
from __future__ import annotations

import sys

from aion2_trainer.utils.process import find_aion2_process
from aion2_trainer.offsets import current


def main() -> int:
    pid = find_aion2_process()
    if pid is None:
        print("aion2.exe not running", file=sys.stderr)
        return 1
    print(f"scanning pid={pid} for build {current.BUILD}")
    for name in ("PLAYER_BASE", "CAMERA_ANGLE", "ENTITY_LIST"):
        print(f"  {name} -> 0x{getattr(current, name):X}")
    return 0


if __name__ == "__main__":
    sys.exit(main())