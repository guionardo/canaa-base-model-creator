import unittest
from cli.model_candidate import ModelCandidate


class TestModelCandidate(unittest.TestCase):

    def setUp(self):
        self.promax_namespace = 'testando'
        self.promax_name = 'teste'
        self.promax_fields = [("chave", "str"), ("descricao", "str")]
        self.ms_namespace = 'testing'
        self.ms_name = 'test'
        self.ms_fields = [('key', 'str'), ('description', 'str')]

    def test_init(self):
        mc = ModelCandidate(self.promax_namespace,
                            self.promax_name,
                            self.promax_fields,
                            self.ms_namespace,
                            self.ms_name,
                            self.ms_fields)

        mc.set_namespaces('testando', 'testing')
        definitions = mc.generate_model_definition()
        self.assertEqual(len(definitions), 3)

    def test_init_invalid_arguments(self):
        with self.assertRaises(Exception):
            ModelCandidate(self.promax_namespace,
                           '',
                           self.promax_fields,
                           self.ms_namespace,
                           self.ms_name,
                           self.ms_fields)

    def test_init_no_matching_fields(self):
        with self.assertRaises(Exception):
            ModelCandidate(self.promax_namespace,
                           self.promax_name,
                           self.promax_fields,
                           self.ms_namespace,
                           self.ms_name,
                           [])

    def test_init_invalid_field(self):
        with self.assertRaises(Exception):
            ModelCandidate(self.promax_namespace,
                           self.promax_name,
                           self.promax_fields,
                           self.ms_namespace,
                           self.ms_name,
                           [('key', 'str'), ('description', 'str', None)])
