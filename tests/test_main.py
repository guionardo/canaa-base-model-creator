import os
import sys
import unittest

import create_models.main
from create_models.example import print_example

import shutil


class TestMain(unittest.TestCase):

    def __init__(self, method_name):
        super().__init__(method_name)
        self._args = sys.argv.copy()

        if os.path.isdir('domain'):
            shutil.rmtree('domain')

    def setUp(self):
        sys.argv = self._args[:1]
        create_models.main._testing_args = ['-v']

    def tearDown(self):
        create_models.main._testing_args = None
        sys.argv = self._args.copy()

    def test_example(self):
        create_models.main._testing_args = ['-e']
        self.assertTrue(create_models.main.main())

    def test_file_not_found(self):
        with self.assertRaises(Exception):
            create_models.main._testing_args = ['-s', 'inexistent_file.csv']
            create_models.main.main()

    def test_origin_empty(self):
        create_models.main._testing_args = ['--foo']
        self.assertFalse(create_models.main.main())

    def test_origin_folder_with_destiny(self):
        create_models.main._testing_args = ['-s', 'docs', '-d', '.']
        self.assertTrue(create_models.main.main())

    def test_origin_file_with_destiny(self):
        create_models.main._testing_args = [
            '-s', os.path.join('docs', 'example_descricao.csv'), '-d', '.']
        self.assertTrue(create_models.main.main())

    def test_origin_file_mask_with_destiny(self):
        create_models.main._testing_args = [
            '-s', os.path.join('docs', 'example_d*.csv'), '-d', '.']
        self.assertTrue(create_models.main.main())
