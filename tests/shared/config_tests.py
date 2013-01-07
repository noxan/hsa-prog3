from nose.tools import assert_equal

from shared.config import ConfigManager


class TestConfigManager(object):
    def setup(self):
        self.c = ConfigManager("config.txt")

    def test_read_write(self):
        assert_equal(self.c.getConfig("runden"), '100')
        self.c.setConfig("runden", 25)
        assert_equal(self.c.getConfig("runden"), '25')
        self.c.setConfig("runden", 100) #reset
