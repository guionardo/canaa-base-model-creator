import unittest

from create_models.model_info import ModelInfo


class TestModelInfo(unittest.TestCase):

    def test_model_info(self):
        mi = ModelInfo("parametros_0200;parameters_0200;")
        self.assertEqual(mi.promax_model, "parametros_0200")
        self.assertEqual(mi.ms_model, "parameters_0200")
