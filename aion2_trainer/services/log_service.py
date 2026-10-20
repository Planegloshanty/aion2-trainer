from __future__ import annotations

import logging
import sys
from pathlib import Path


class LogService:
    def __init__(self, log_dir: str = "logs") -> None:
        Path(log_dir).mkdir(exist_ok=True)
        self._logger = logging.getLogger("aion2-trainer")
        self._logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        fh = logging.FileHandler(Path(log_dir) / "trainer.log", encoding="utf-8")
        fh.setFormatter(fmt)
        self._logger.addHandler(fh)

        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(fmt)
        self._logger.addHandler(ch)

    def info(self, msg: str, *args) -> None:
        self._logger.info(msg, *args)

    def warn(self, msg: str, *args) -> None:
        self._logger.warning(msg, *args)

    def error(self, msg: str, *args) -> None:
        self._logger.error(msg, *args)