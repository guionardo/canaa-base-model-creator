import unittest

from cli.cache import get_cache


class TestCache(unittest.TestCase):

    def test_init(self):

        cache = get_cache()
        self.assertIsNotNone(cache)

    def test_set_get_value(self):
        cache = get_cache()

        cache.set_value('test', 'value_1', {"testing": True})
        value = cache.get_value('test', 'value_1')

        self.assertDictEqual(value, {"testing": True})
