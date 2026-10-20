"""Thin wrapper around pymem for reading the AION 2 client."""
from __future__ import annotations

import struct
from typing import Optional

from pymem import Pymem
from pymem.process import module_from_name


class MemoryReader:
    def __init__(self, pid: int) -> None:
        self.pm = Pymem()
        self.pm.open_process_from_id(pid)
        self.base = module_from_name(self.pm.process_handle, b"aion2.exe").lpBaseOfDll

    def read_int(self, offset: int) -> int:
        return self.pm.read_int(self.base + offset)

    def read_float(self, offset: int) -> float:
        return self.pm.read_float(self.base + offset)

    def read_ptr(self, offset: int) -> int:
        return self.pm.read_longlong(self.base + offset)

    def read_bytes(self, offset: int, size: int) -> bytes:
        return self.pm.read_bytes(self.base + offset, size)

    def read_vec3(self, offset: int) -> tuple[float, float, float]:
        raw = self.read_bytes(offset, 12)
        return struct.unpack("<fff", raw)

    def resolve_chain(self, base_offset: int, offsets: list[int]) -> Optional[int]:
        ptr = self.read_ptr(base_offset)
        for off in offsets[:-1]:
            if ptr == 0:
                return None
            ptr = self.pm.read_longlong(ptr + off)
        return ptr + offsets[-1] if ptr else None

    def close(self) -> None:
        try:
            self.pm.close_process()
        except Exception:
            pass