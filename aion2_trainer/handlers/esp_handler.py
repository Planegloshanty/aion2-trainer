"""ESP / wallhack handler — reads entity list and pushes boxes to the overlay."""
from __future__ import annotations

from aion2_trainer.offsets.current import ENTITY_LIST, ENTITY_STRIDE, ENTITY_COUNT
from aion2_trainer.models.entities import EntitySnapshot
from aion2_trainer.models.state import TrainerState


class ESPHandler:
    name = "esp"

    def __init__(self) -> None:
        self.enabled = False
        self.max_distance = 300.0

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def tick(self, mem, state: TrainerState) -> None:
        if not self.enabled:
            return
        entities: list[EntitySnapshot] = []
        for i in range(ENTITY_COUNT):
            addr = ENTITY_LIST + i * ENTITY_STRIDE
            hp = mem.read_int(addr + 0x18)
            if hp <= 0:
                continue
            pos = mem.read_vec3(addr + 0x2C)
            kind = mem.read_int(addr + 0x04)
            entities.append(EntitySnapshot(index=i, hp=hp, pos=pos, kind=kind))
        state.entities = entities