import unittest

from create_models.utils import camel_to_snake, snake_to_camel


class TestUtils(unittest.TestCase):

    def test_camel_to_snake(self):
        camel = 'BaseModel'
        snake = camel_to_snake(camel)
        self.assertEqual(snake, "base_model")

    def test_snake_to_camel(self):
        snake = "base_model"
        camel = snake_to_camel(snake)
        self.assertEqual(camel, "BaseModel")
