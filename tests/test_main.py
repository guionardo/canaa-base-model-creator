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

    def test_exit(self):
        with self.assertRaises(Exception):
            cli.main.exit(0, Exception("Testing exception"))

    def test_version(self):
        self.assertFalse(cli.main.main())

    def test_process(self):
        cli.main._testing_args = [
            '-s', os.path.join('docs', 'example.csv'),
            '--just-validate']
        self.assertFalse(cli.main.main())
