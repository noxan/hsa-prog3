from nose.tools import assert_equal, assert_true, assert_false

from shared.map import Map


class TestMap(object):
    def test_init(self):
        m = Map(5, 5)
        assert_equal(m.get_width(), 5)
        assert_equal(m.get_height(), 5)

    def test_get(self):
        m = Map(1, 1)
        assert_equal(m.get(0, 0), '.')

    def test_set_get_is_empty(self):
        m = Map(1, 1)
        assert_true(m.is_empty(0, 0))
        m.set(0, 0, 'a')
        assert_equal(m.get(0, 0), 'a')
        assert_false(m.is_empty(0, 0))

    def test_is_empty(self):
        m = Map(1, 1)
        assert_true(m.is_empty(0, 0))
