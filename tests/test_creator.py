import unittest
import os
from create_models.model_creator import ModelCreator


class TestCreator(unittest.TestCase):

    def test_create_promax(self):

        mc = ModelCreator("docs/parametros-0200.csv")
        mc.create_files('.')
