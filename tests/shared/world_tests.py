from nose.tools import assert_equal, assert_true, assert_false

from shared.world import World


class TestWorld(object):
    def test_init(self):
        w = World(5, 5)
        assert_equal(w.get_width(), 5)
        assert_equal(w.get_height(), 5)

    def test_get(self):
        w = World(1, 1)
        assert_equal(w.get(0, 0), '.')

    def test_set_get_is_empty(self):
        w = World(1, 1)
        assert_true(w.is_empty(0, 0))
        w.set(0, 0, 'a')
        assert_equal(w.get(0, 0), 'a')
        assert_false(w.is_empty(0, 0))

    def test_is_empty(self):
        w = World(1, 1)
        assert_true(w.is_empty(0, 0))
