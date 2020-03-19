import argparse
import os
import unittest

from cli.arguments import Arguments, print_help


class TestArguments(unittest.TestCase):

    def setUp(self):
        Arguments.clear()
        self.source = os.path.join('docs', 'example_descricao.csv')

    def tearDown(self):
        Arguments.clear()

    def test_singleton(self):
        c = Arguments.create('-d', ".")
        c2 = Arguments.create()
        self.assertEqual(c.destiny, c2.destiny)

    def test_create_from_parse(self):
        c = Arguments.create('-v')
        self.assertTrue(c.version)

    def test_version(self):
        c = Arguments.create('-v')
        self.assertEqual(c.validate(), 0)

    def test_example(self):
        c = Arguments.create('-e')
        self.assertEqual(c.validate(), 0)

    def test_help_error(self):
        self.assertEqual(print_help('not-found'), 0)

    def test_source_not_found(self):
        with self.assertRaises(Exception):
            Arguments.create('-s', 'file_not_found.csv')

    def test_empty_source(self):
        c = Arguments.create('--foo')
        self.assertEqual(c.validate(), 1)

    def test_source_without_destiny(self):
        with self.assertRaises(Exception):
            Arguments.create('-s', self.source)

    def test_destiny_not_found(self):
        with self.assertRaises(Exception):
            Arguments.create('-s', self.source, '-d', 'notfound')

    def test_origin_file_with_destiny(self):
        c = Arguments.create('-s', self.source, '-d', '.')
        self.assertEqual(c.validate(), 2)

    def test_origin_folder_with_destiny(self):
        c = Arguments.create('-s', 'docs', '-d', '.')
        self.assertEqual(c.validate(), 2)

    def test_origin_file_mask_with_destiny(self):
        c = Arguments.create(
            '-s', os.path.join('docs', 'example_d*.csv'), '-d', '.')
        self.assertEqual(c.validate(), 2)
