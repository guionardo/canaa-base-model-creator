from create_models.imports import Imports
import unittest


class TestImports(unittest.TestCase):

    def test_imports(self):
        imports = Imports()
        imports.add('datetime', 'datetime')
        imports.add('datetime', 'time')
        imports.add('canaa_base', 'BaseModel')

        code = imports.to_code()
        expected = 'from canaa_base import BaseModel\nfrom datetime import datetime, time\n\n'
        self.assertEqual(code, expected)
