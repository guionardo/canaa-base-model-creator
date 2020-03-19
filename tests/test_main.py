import os
import shutil
import sys
import unittest

import cli.main


class TestMain(unittest.TestCase):

    def __init__(self, method_name):
        super().__init__(method_name)
        self._args = sys.argv.copy()

        if os.path.isdir('domain'):
            shutil.rmtree('domain')

    def setUp(self):
        sys.argv = self._args[:1]
        cli.main._testing_args = ['-v']

    def tearDown(self):
        cli.main._testing_args = None
        sys.argv = self._args.copy()
