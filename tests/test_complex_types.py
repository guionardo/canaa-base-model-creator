import unittest
import json
from cli.data_type.complex_types import parse_json_model


class TestComplexTypes(unittest.TestCase):

    def setUp(self):
        self.model = {
            "name": "str",
            "id": "int",
            "active": "bool"
        }
        self.json_model = json.dumps(self.model)

    def test_parse(self):
        fields = parse_json_model(self.json_model, "test")
        self.assertEqual(len(fields), 3)
