import os
import unittest

from create_models.file_converter import generate_yaml, validate_yaml
from create_models.model_creator import ModelCreator
from create_models.create_files import create_files

class TestCreator(unittest.TestCase):

    def test_create_files(self):
        mc = ModelCreator("docs/parametros-0200.csv")
        create_files(mc,".")

    def test_yaml(self):
        mc = ModelCreator("docs/parametros-0200.csv")
        yaml = generate_yaml(mc.info, mc.fields)
        if validate_yaml(yaml):
            with open('docs/parametros-0200.yaml', 'w') as f:
                f.write(yaml)

        mc = ModelCreator("docs/parametros-0200.yaml")
        self.assertIsInstance(mc, ModelCreator)
