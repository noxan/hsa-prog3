from nose.tools import assert_equal

from shared.geometry import Point, WorldPoint
from shared.world import World


class TestPoint(object):
    def test_init(self):
        p = Point(2,3)
        assert_equal(p._x, 2)
        assert_equal(p._y, 3)

class TestWorldPoint(object):
    def setup(self):
        self.world = World(10, 10)

    def test_init(self):
        p = WorldPoint(self.world)
        assert_equal(p.get_x(), 0)
        assert_equal(p.get_y(), 0)

