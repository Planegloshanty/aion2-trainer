"""Aimbot handler — snaps the camera to the closest target within FOV."""
from __future__ import annotations

import math

from aion2_trainer.offsets.current import PLAYER_BASE, CAMERA_ANGLE
from aion2_trainer.models.state import TrainerState
from aion2_trainer.utils.vecmath import angle_to_target, clamp


class AimbotHandler:
    name = "aimbot"

    def __init__(self) -> None:
        self.enabled = False
        self.fov = 15.0
        self.smooth = 0.35
        self.bone = "head"

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def tick(self, mem, state: TrainerState) -> None:
        if not self.enabled or not state.entities:
            return
        cam = mem.read_vec3(CAMERA_ANGLE)
        best = None
        best_delta = self.fov
        for ent in state.entities:
            if ent.kind == 0:
                continue
            yaw, pitch = angle_to_target(cam, ent.pos)
            delta = math.hypot(yaw, pitch)
            if delta < best_delta:
                best_delta = delta
                best = (yaw, pitch)
        if best is None:
            return
        yaw = clamp(best[0], -180.0, 180.0)
        pitch = clamp(best[1], -89.0, 89.0)
        state.pending_aim = (yaw * self.smooth, pitch * self.smooth)