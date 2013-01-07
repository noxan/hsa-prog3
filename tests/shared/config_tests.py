from nose.tools import assert_equal

from shared.config import ConfigManager


class TestConfigManager(object):
    def setup(self):
        self.c = ConfigManager("config.txt")

    def test_read(self):
        assert_equal(self.c.getConfig("runden"), 100)

    def test_write(self):
        self.c.setConfig("runden", 25)
        assert_equal(self.c.getConfig("runden"), 25)
