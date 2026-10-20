"""Feature handler registry with hot-toggle support."""
from __future__ import annotations

from typing import Iterable, Protocol


class Handler(Protocol):
    name: str

    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def tick(self, mem, state) -> None: ...


class FeatureRegistry:
    def __init__(self) -> None:
        self._handlers: dict[str, Handler] = {}
        self._enabled: set[str] = set()

    def register(self, handler: Handler) -> None:
        self._handlers[handler.name] = handler

    def toggle(self, name: str, on: bool) -> None:
        handler = self._handlers.get(name)
        if handler is None:
            return
        if on:
            handler.enable()
            self._enabled.add(name)
        else:
            handler.disable()
            self._enabled.discard(name)

    def active(self) -> Iterable[Handler]:
        for name in self._enabled:
            yield self._handlers[name]

    def __len__(self) -> int:
        return len(self._handlers)