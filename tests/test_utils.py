import unittest

from create_models.utils import camel_to_snake, snake_to_camel, get_words, padr, created_by


class TestUtils(unittest.TestCase):

    def test_camel_to_snake(self):
        camel = 'BaseModel0202'
        snake = camel_to_snake(camel)
        self.assertEqual(snake, "base_model_0202")

    def test_snake_to_camel(self):
        snake = "base_model_0202"
        camel = snake_to_camel(snake)
        self.assertEqual(camel, "BaseModel0202")

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

    def test_padr(self):        
        self.assertEqual(padr('abc',10),'abc       ')
        self.assertEqual(padr('abc',0),'abc')

    def test_created_by(self):
        cb = created_by()
        self.assertTrue(cb[:10]=='# CREATED ')