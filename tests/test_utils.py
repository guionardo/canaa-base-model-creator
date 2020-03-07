import unittest

from src.create_models.utils import camel_to_snake, snake_to_camel, get_words


class TestUtils(unittest.TestCase):

    def test_camel_to_snake(self):
        camel = 'BaseModel'
        snake = camel_to_snake(camel)
        self.assertEqual(snake, "base_model")

    def test_snake_to_camel(self):
        snake = "base_model"
        camel = snake_to_camel(snake)
        self.assertEqual(camel, "BaseModel")

    def test_get_words(self):
        w1, w2 = get_words("word1;word2", 2, ';')
        self.assertEqual(w1, 'word1')
        self.assertEqual(w2, 'word2')

        w1, w2 = get_words("word1;word2")
        self.assertEqual(w1, 'word1')
        self.assertEqual(w2, 'word2')

        w1, w2 = get_words("word1",2)
        self.assertEqual(w1, 'word1')
        self.assertIsNone(w2)
