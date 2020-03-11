import unittest
import create_models.main
import sys
from create_models.example import print_example
class TestMain(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)        
        self._args = sys.argv.copy()

    def setUp(self):        
        sys.argv = self._args[:1]

    def tearDown(self):
        create_models.main._testing_args=None
        sys.argv = self._args.copy()

    def test_example(self):        
        self.assertIsNotNone(print_example())

    def test_call(self):        
        create_models.main._testing_args = ['-e']
        create_models.main.main()


