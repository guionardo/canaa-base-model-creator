import unittest

from create_models.model_creator import ModelCreator
from create_models.create_files import create_files


class TestCreator(unittest.TestCase):

    def test_create_files(self):
        mc = ModelCreator("docs/example.csv", True, False)
        create_files(mc, ".")
        mc = ModelCreator("docs/example_descricao.csv", True, False)
        create_files(mc, ".")
   
