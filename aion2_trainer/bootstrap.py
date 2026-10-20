"""Bootstrap layer — wires the trainer together and starts the UI loop."""
from __future__ import annotations

import argparse
import sys

from aion2_trainer.core.engine import TrainerEngine
from aion2_trainer.core.registry import FeatureRegistry
from aion2_trainer.handlers import load_all_handlers
from aion2_trainer.services.config_service import ConfigService
from aion2_trainer.services.log_service import LogService
from aion2_trainer.utils.process import find_aion2_process


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="aion2-trainer")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("--no-overlay", action="store_true", help="headless mode")
    parser.add_argument("--config", default="config/default.yaml")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.version:
        from aion2_trainer import __version__
        print(f"aion2-trainer {__version__}")
        return 0

    log = LogService()
    cfg = ConfigService(args.config)
    log.info("aion2-trainer starting, config=%s", args.config)

    pid = find_aion2_process()
    if pid is None:
        log.error("AION 2 process not found — launch the game first")
        return 1
    log.info("attached to aion2.exe pid=%d", pid)

    registry = FeatureRegistry()
    load_all_handlers(registry)
    engine = TrainerEngine(pid=pid, registry=registry, config=cfg, log=log)

    try:
        engine.run(overlay=not args.no_overlay)
    except KeyboardInterrupt:
        log.info("interrupted, shutting down")
    finally:
        engine.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())