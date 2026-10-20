"""Speed hack handler — writes to the movement speed multiplier."""
from __future__ import annotations

from aion2_trainer.offsets.current import PLAYER_BASE, SPEED_MULT


class SpeedHandler:
    name = "speed"

    def __init__(self) -> None:
        self.enabled = False
        self.multiplier = 1.0

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        if self.enabled:
            self._write(1.0)
        self.enabled = False

    def tick(self, mem, state) -> None:
        if not self.enabled:
            return
        self._write(self.multiplier)

    def _write(self, value: float) -> None:
        # actual write goes through the mem writer in engine
        pass