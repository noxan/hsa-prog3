from nose.tools import assert_equal

from shared.geometry import Point


class TestPoint(object):
    def test_init(self):
        p = Point(2,3)
        assert_equal(p._x, 2)
        assert_equal(p._y, 3)

