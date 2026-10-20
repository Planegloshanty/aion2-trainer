"""Teleport handler — one-shot writes to the player position vector."""
from __future__ import annotations

from aion2_trainer.offsets.current import PLAYER_BASE, PLAYER_POS


class TeleportHandler:
    name = "teleport"

    def __init__(self) -> None:
        self.enabled = False
        self.target: tuple[float, float, float] | None = None

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False
        self.target = None

    def set_target(self, x: float, y: float, z: float) -> None:
        self.target = (x, y, z)

    def tick(self, mem, state) -> None:
        if not self.enabled or self.target is None:
            return
        # write handled by engine writer; consume target
        state.pending_teleport = self.target
        self.target = None