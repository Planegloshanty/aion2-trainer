from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EntitySnapshot:
    index: int
    hp: int
    pos: tuple[float, float, float]
    kind: int

    @property
    def is_player(self) -> bool:
        return self.kind == 1

    @property
    def is_npc(self) -> bool:
        return self.kind == 2