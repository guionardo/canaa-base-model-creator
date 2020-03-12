import unittest

from create_models.model_json_cache import get_model_json, set_model_json


class TestModelJsonCache(unittest.TestCase):

    def setUp(self):
        self.test_model = {
            "id": 0,
            "name": "User"
        }

    def test_get_set_model_json(self):
        self.assertTrue(set_model_json('dto', 'test', self.test_model))
        self.assertDictEqual(get_model_json('dto', 'test'), self.test_model)
