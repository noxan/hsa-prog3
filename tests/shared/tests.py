from nose.tools import assert_equal

from shared.geometry import Point
from shared.utils import movement_to_energy, code_to_movement


class TestUtils(object):
    def test_movement_to_energy(self):
        assert_equal(movement_to_energy(0,0), 1)
        assert_equal(movement_to_energy(0,1), 2)
        assert_equal(movement_to_energy(0,2), 5)
        assert_equal(movement_to_energy(1,0), 2)
        assert_equal(movement_to_energy(1,1), 3)
        assert_equal(movement_to_energy(1,2), 6)
        assert_equal(movement_to_energy(2,0), 5)
        assert_equal(movement_to_energy(2,1), 6)
        assert_equal(movement_to_energy(2,2), 7)

    def test_code_to_movement(self):
        assert_equal(code_to_movement(0), (-2, 2))
        assert_equal(code_to_movement(4), (2, 2))
        assert_equal(code_to_movement(20), (-2, -2))
        assert_equal(code_to_movement(24), (2, -2))
        assert_equal(code_to_movement(12), (0,0))


class TestPoint(object):
    def test_init(self):
        p = Point(2,3)
        assert_equal(p._x, 2)
        assert_equal(p._y, 3)
