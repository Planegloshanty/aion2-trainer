"""Handler loader — imports every feature module and registers it."""
from aion2_trainer.core.registry import FeatureRegistry

from aion2_trainer.handlers.esp_handler import ESPHandler
from aion2_trainer.handlers.aimbot_handler import AimbotHandler
from aion2_trainer.handlers.speed_handler import SpeedHandler
from aion2_trainer.handlers.teleport_handler import TeleportHandler


def load_all_handlers(registry: FeatureRegistry) -> None:
    for cls in (ESPHandler, AimbotHandler, SpeedHandler, TeleportHandler):
        registry.register(cls())
        registry.toggle(cls().name, False)