"""Pygame overlay — draws ESP boxes on top of the AION 2 window."""
from __future__ import annotations

import pygame

from aion2_trainer.models.state import TrainerState
from aion2_trainer.utils.projection import world_to_screen


class OverlayService:
    def __init__(self, width: int = 1920, height: int = 1080) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
        pygame.display.set_caption("aion2-trainer overlay")
        self.font = pygame.font.SysFont("consolas", 14)
        self.width = width
        self.height = height

    def draw(self, state: TrainerState) -> None:
        self.screen.fill((0, 0, 0, 0))
        for ent in state.entities:
            if not ent.is_player:
                continue
            sx, sy = world_to_screen(ent.pos, self.width, self.height)
            if sx < 0 or sy < 0:
                continue
            rect = pygame.Rect(sx - 20, sy - 60, 40, 100)
            pygame.draw.rect(self.screen, (255, 40, 40), rect, 2)
            label = self.font.render(f"{ent.hp}", True, (255, 255, 255))
            self.screen.blit(label, (sx - 10, sy - 78))
        pygame.display.flip()

    def close(self) -> None:
        pygame.quit()