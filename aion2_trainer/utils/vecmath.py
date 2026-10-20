from __future__ import annotations

import math


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def angle_to_target(cam: tuple[float, float, float],
                    target: tuple[float, float, float]) -> tuple[float, float]:
    dx = target[0] - cam[0]
    dy = target[1] - cam[1]
    dz = target[2] - cam[2]
    yaw = math.degrees(math.atan2(dy, dx))
    pitch = math.degrees(math.atan2(dz, math.hypot(dx, dy)))
    return yaw, pitch


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))