import unittest

from cli.model_info import ModelInfo


class TestModelInfo(unittest.TestCase):

    def setUp(self):
        self.ns_promax = 'parametros'
        self.ns_ms = 'parameters'
        self.model_promax = 'parametros_0200'
        self.model_ms = 'parameters_0200'

    def test_model_info_str(self):
        cvs_line = "{0}.{1};{2}.{3}".format(
            self.ns_promax,
            self.model_promax,
            self.ns_ms,
            self.model_ms
        )
        mi = ModelInfo(cvs_line)
        self.assertEqual(mi.namespace_promax, self.ns_promax)
        self.assertEqual(mi.namespace_ms, self.ns_ms)
        self.assertEqual(mi.promax_model, self.model_promax)
        self.assertEqual(mi.ms_model, self.model_ms)
        self.assertIsInstance(str(mi), str)

    def test_model_info_dict(self):
        info = {
            "model": {
                "promax": "{0}.{1}".format(self.ns_promax, self.model_promax),
                "ms": "{0}.{1}".format(self.ns_ms, self.model_ms)
            }
        }
        mi = ModelInfo(info)
        self.assertEqual(mi.namespace_promax, self.ns_promax)
        self.assertEqual(mi.namespace_ms, self.ns_ms)
        self.assertEqual(mi.promax_model, self.model_promax)
        self.assertEqual(mi.ms_model, self.model_ms)

    def test_model_info_dict_error(self):
        info = {}
        with self.assertRaises(Exception):
            ModelInfo(info)
