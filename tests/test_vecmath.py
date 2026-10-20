from aion2_trainer.utils.vecmath import angle_to_target, clamp, distance


def test_clamp_bounds():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(99, 0, 10) == 10


def test_angle_to_target_forward():
    yaw, pitch = angle_to_target((0, 0, 0), (1, 0, 0))
    assert abs(yaw) < 1e-6
    assert abs(pitch) < 1e-6


def test_distance():
    assert distance((0, 0, 0), (3, 4, 0)) == 5.0