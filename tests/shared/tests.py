from nose.tools import assert_equal

from shared.geometry import Point
from shared.nibble import Nibble


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
