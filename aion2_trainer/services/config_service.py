from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # fallback for minimal installs
    yaml = None


class ConfigService:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._data: dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        text = self.path.read_text(encoding="utf-8")
        if yaml is not None:
            self._data = yaml.safe_load(text) or {}
        else:
            self._data = {}

    def _lookup(self, dotted: str, default: Any) -> Any:
        node: Any = self._data
        for part in dotted.split("."):
            if not isinstance(node, dict) or part not in node:
                return default
            node = node[part]
        return node

    def get(self, key: str, default: Any = None) -> Any:
        return self._lookup(key, default)

    def get_float(self, key: str, default: float) -> float:
        try:
            return float(self._lookup(key, default))
        except (TypeError, ValueError):
            return default