import unittest
import os

from cli.containers.get_creators import (_get_files_from_path, _get_masked_files,
                                         _get_model_creators, _get_unique_file,
                                         get_creators)


class TestContainers(unittest.TestCase):

    def test_get_files_from_path(self):
        files, error = _get_files_from_path('docs')
        self.assertEqual(len(files), 3)

    def test_get_masked_files(self):
        files, error = _get_masked_files(os.path.join('docs', '*.csv'))
        self.assertEqual(len(files), 2)

    def test_get_unique_file(self):
        creators = get_creators(os.path.join(
            'docs', 'example.csv'), False, True)
        self.assertEqual(len(creators), 1)

        files, error = _get_unique_file(os.path.join('docs', 'example.csv'))
        self.assertEqual(len(files), 1)

        files, error = _get_unique_file('not_exists.csv')
        self.assertIsNotNone(error)

        files, error = _get_unique_file('not_exists.txt')
        self.assertIsNotNone(error)

    def test_creators_bad_origin(self):
        with self.assertRaises(Exception):
            get_creators(None, False, False)

    def test_creators_masked(self):
        creators = get_creators(os.path.join('docs', '*.csv'), False, True)
        self.assertEqual(len(creators), 2)

    def test_creators_folder(self):
        creators = get_creators('docs', False, True)
        self.assertEqual(len(creators), 2)
