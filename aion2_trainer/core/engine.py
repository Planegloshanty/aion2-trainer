"""Core engine — owns the memory handle and drives all feature handlers."""
from __future__ import annotations

import time
from dataclasses import dataclass

from aion2_trainer.core.memory import MemoryReader
from aion2_trainer.core.registry import FeatureRegistry
from aion2_trainer.models.state import TrainerState
from aion2_trainer.services.config_service import ConfigService
from aion2_trainer.services.log_service import LogService


@dataclass
class TrainerEngine:
    pid: int
    registry: FeatureRegistry
    config: ConfigService
    log: LogService

    def __post_init__(self) -> None:
        self.mem = MemoryReader(self.pid)
        self.state = TrainerState()
        self._running = False

    def run(self, overlay: bool = True) -> None:
        self._running = True
        self.log.info("engine running, %d handlers registered", len(self.registry))
        tick = self.config.get_float("engine.tick_hz", 30.0)
        interval = 1.0 / max(tick, 1.0)
        while self._running:
            started = time.perf_counter()
            for handler in self.registry.active():
                try:
                    handler.tick(self.mem, self.state)
                except Exception as exc:  # noqa: BLE001
                    self.log.warn("handler %s failed: %s", handler.name, exc)
            if overlay:
                self.state.publish()
            elapsed = time.perf_counter() - started
            time.sleep(max(0.0, interval - elapsed))

    def shutdown(self) -> None:
        self._running = False
        self.mem.close()
        self.log.info("engine stopped")