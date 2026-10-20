"""Shared mutable state published to the overlay."""
from __future__ import annotations

from dataclasses import dataclass, field

from aion2_trainer.models.entities import EntitySnapshot


@dataclass
class TrainerState:
    entities: list[EntitySnapshot] = field(default_factory=list)
    pending_aim: tuple[float, float] | None = None
    pending_teleport: tuple[float, float, float] | None = None
    player_pos: tuple[float, float, float] = (0.0, 0.0, 0.0)
    fps: float = 0.0

    def publish(self) -> None:
        self.pending_aim = None