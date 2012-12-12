from nose.tools import assert_equal

from shared.nibble import Nibble
from shared.world import World
from shared.geometry import Point


class TestNibble(object):
    def setup(self):
        self.world = World(10, 10)

    def test_init_default(self):
        n = Nibble('a', self.world)
        assert_equal(n._energy, 30)
        assert_equal(n._position._x, 0)
        assert_equal(n._position._y, 0)

    def test_init_custom(self):
        n = Nibble('a', self.world, Point(5, 10), 50)
        assert_equal(n._energy, 50)
        assert_equal(n._position._x, 5)
        assert_equal(n._position._y, 10)

    def test_move(self):
        n = Nibble('a', self.world)
        n.move(2,2)
        assert_equal(n._energy, 23)
        assert_equal(n._position._x, 2)
        assert_equal(n._position._y, 2)

