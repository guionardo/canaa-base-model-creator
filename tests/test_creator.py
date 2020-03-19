import os
import unittest

from cli.create_files import create_files
from cli.model_creator import ModelCreator


class TestCreator(unittest.TestCase):

    def add_model(self, ns_pm, model_pm, ns_ms, model_ms):
        self.files.append(
            os.path.join('domain', 'models', 'dtos', ns_ms, model_ms+'_dto.py')
        )
        self.files.append(
            os.path.join('domain', 'models', 'microservice',
                         ns_ms, model_ms+'_model.py')
        )
        self.files.append(
            os.path.join('domain', 'models', 'promax',
                         ns_pm, model_pm+'_model.py')
        )

    def setUp(self):
        self.files = []
        self.add_model('promax_namespace', 'descricao',
                       'microservice_namespace', 'description')
        self.add_model('promax_namespace', 'promax_exemplo',
                       'microservice_namespace', 'microservice_example')

    def test_create_files(self):
        mc = ModelCreator("docs/example.csv", True, False)
        self.assertTrue(mc.is_ok)
        create_files(mc, ".")
        mc = ModelCreator("docs/example_descricao.csv", True, False)
        self.assertTrue(mc.is_ok)
        create_files(mc, ".")

        self.assertListEqual([os.path.isfile(x)
                              for x in self.files], [True for _ in self.files])
