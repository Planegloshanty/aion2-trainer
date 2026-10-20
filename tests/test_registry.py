from aion2_trainer.core.registry import FeatureRegistry


class Dummy:
    name = "dummy"

    def __init__(self) -> None:
        self.on = False

    def enable(self) -> None:
        self.on = True

    def disable(self) -> None:
        self.on = False

    def tick(self, mem, state) -> None:
        pass


def test_register_and_toggle():
    reg = FeatureRegistry()
    d = Dummy()
    reg.register(d)
    reg.toggle("dummy", True)
    assert d.on is True
    assert len(list(reg.active())) == 1
    reg.toggle("dummy", False)
    assert d.on is False
    assert len(list(reg.active())) == 0
</final>