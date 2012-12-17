from nose.tools import assert_equal

from shared.nibble import Nibble
from shared.world import World
from shared.geometry import Point


class TestNibble(object):
    def setup(self):
        self.world = World(20, 20)

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

    def test_move_code(self):
        n = Nibble('c', self.world)
        assert_equal(n._position._x, 0)
        assert_equal(n._position._y, 0)
        n.move_code(18)
        assert_equal(n._energy, 27)
        assert_equal(n._position._x, 1)
        assert_equal(n._position._y, 1)

    def test_compare_energy(self):
        a = Nibble('a', self.world)
        b = Nibble('b', self.world)
        assert_equal(a.compare_energy(b), 0)
        a.move(1,1)
        assert_equal(a.compare_energy(b), -1)
        b.move(2,2)
        assert_equal(a.compare_energy(b), 1)
