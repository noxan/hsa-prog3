from nose.tools import assert_equal

from shared.geometry import Point
from shared.nibble import Nibble
from shared.utils import movement_to_energy


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


class TestPoint(object):
    def test_init(self):
        p = Point(2,3)
        assert_equal(p._x, 2)
        assert_equal(p._y, 3)


class TestNibble(object):
    def test_init_default(self):
        n = Nibble()
        assert_equal(n._energy, 30)
        assert_equal(n._position._x, 0)
        assert_equal(n._position._y, 0)

    def test_init_custom(self):
        n = Nibble(Point(5, 10), 50)
        assert_equal(n._energy, 50)
        assert_equal(n._position._x, 5)
        assert_equal(n._position._y, 10)

    def test_move_vector(self):
        n = Nibble()
        n.move_vector(2,2)
        assert_equal(n._energy, 23)
        assert_equal(n._position._x, 2)
        assert_equal(n._position._y, 2)
