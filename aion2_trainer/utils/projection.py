from __future__ import annotations


def world_to_screen(pos: tuple[float, float, float],
                    width: int, height: int,
                    fov: float = 60.0) -> tuple[int, int]:
    x, _y, z = pos
    if z <= 0:
        return -1, -1
    scale = height / (2.0 * z * (fov / 90.0))
    return int(width / 2 + x * scale), int(height / 2 - z * scale)