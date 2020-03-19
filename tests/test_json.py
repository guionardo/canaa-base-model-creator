import os
import unittest

from cli.create_ms_json import create_ms_json
from cli.create_promax_json import create_promax_json
from cli.model_creator import ModelCreator


class TestJSON(unittest.TestCase):

    def setUp(self):
        self.model = ModelCreator(os.path.join(
            'docs', 'example.csv'), False, False)
        self.model_desc = ModelCreator(os.path.join(
            'docs', 'example_descricao.csv'), False, False)
        self.destiny = os.path.join('docs', 'mock')

    def test_create_json_promax(self):
        create_promax_json(self.model_desc, self.destiny)
        create_promax_json(self.model, self.destiny)

    def test_create_json_ms(self):
        create_ms_json(self.model_desc, self.destiny)
        create_ms_json(self.model, self.destiny)
