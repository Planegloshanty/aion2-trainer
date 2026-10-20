from __future__ import annotations

import psutil


def find_aion2_process() -> int | None:
    for proc in psutil.process_iter(["pid", "name"]):
        name = (proc.info.get("name") or "").lower()
        if name == "aion2.exe":
            return proc.info["pid"]
    return None


def is_elevated() -> bool:
    try:
        import ctypes
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False