from nose.tools import assert_equal

from shared.map import Map


class TestMap(object):
    def test_init(self):
        m = Map(5, 5)
        assert_equal(m.get_width(), 5)
        assert_equal(m.get_height(), 5)

