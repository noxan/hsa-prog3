from nose.tools import assert_equal

from network.client import Client


class TestClient(object):
    def test_init(self):
        c = Client()
        assert_equal(c.host, "localhost")
        assert_equal(c.port, 10857)
