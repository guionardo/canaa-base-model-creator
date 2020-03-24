import os
import unittest
from unittest.mock import Mock, patch

from cli.containers.get_creators import (
    _get_files_from_path, _get_masked_files, _get_model_creators,
    _get_unique_file, get_container_from_origin, get_creators,
    get_files_from_origin)
from cli.interfaces.metadata_container_interface import IMetadataContainer


class TestContainers(unittest.TestCase):

    def setUp(self):
        self.folder = 'docs'
        self.file = os.path.join('docs', 'example.csv')
        self.file_not_found = os.path.join('docs', 'example_not_found.csv')
        self.invalid_file = os.path.join('docs', 'example_not_found.error')
        self.masked_files = os.path.join('docs', 'example*.csv')
        self.masked_files_not_found = os.path.join('docs', 'examplees_*.csv')
        self.xlsx_file = os.path.join('docs', 'example.xlsx')
        self.xlsx_file_not_found = os.path.join(
            'docs', 'example_not_found.xlsx')
        self.xlsx_file_malformed = os.path.join(
            'docs', 'example_malformed.xlsx')

    # PATH CONTAINER

    def test_get_path_container(self):
        container = get_container_from_origin('docs', False, True)
        self.assertIsInstance(container, IMetadataContainer)

        creators = container.get_model_creators()
        self.assertEqual(len(creators), 3)

    def test_get_path_container_origin_not_found(self):
        with self.assertRaises(Exception):
            get_container_from_origin('docs_not_found', False, True)

    def test_get_path_container_no_files(self):
        with self.assertRaises(Exception):
            get_container_from_origin(os.path.join(
                'docs', 'empty_folder'), False, True)

    # UNIQUE FILE CONTAINER

    def test_get_unique_file_container(self):
        container = get_container_from_origin(self.file, False, True)
        self.assertIsInstance(container, IMetadataContainer)
        creators = container.get_model_creators()
        self.assertEqual(len(creators), 1)

    def test_get_unique_file_container_not_found(self):
        with self.assertRaises(Exception):
            get_container_from_origin(self.file_not_found, False, True)

    def test_get_unique_file_container_invalid_file(self):
        with self.assertRaises(Exception):
            get_container_from_origin(self.invalid_file, False, True)

    # MASKED FILES CONTAINER
    def test_get_masked_files_container(self):
        container = get_container_from_origin(self.masked_files, False, True)
        self.assertIsInstance(container, IMetadataContainer)
        creators = container.get_model_creators()
        self.assertEqual(len(creators), 3)

    def test_get_masked_files_container_no_files(self):
        with self.assertRaises(Exception):
            get_container_from_origin(self.masked_files_not_found, False, True)

    # XLSX CONTAINER

    def test_get_xlsx_container(self):
        container = get_container_from_origin(self.xlsx_file, False, True)
        self.assertIsInstance(container, IMetadataContainer)
        creators = container.get_model_creators()
        self.assertEqual(len(creators), 2)

    def test_get_xlsx_container_not_found(self):
        with self.assertRaises(Exception):
            get_container_from_origin(
                self.xlsx_file_not_found, False, True)

    def test_get_xlsx_container_malformed(self):
        container = get_container_from_origin(
            self.xlsx_file_malformed, False, True)

        creators = container.get_model_creators()
        self.assertEqual(len(creators), 2)

    # BASE INTERFACE
    def test_imetadata_container_invalid_origin(self):
        with self.assertRaises(Exception):
            IMetadataContainer(None, True, True)

    @patch('cli.interfaces.metadata_container_interface.IMetadataContainer.validate_origin', Mock())
    def test_imetadata_container_coverage(self):
        with self.assertRaises(Exception):
            IMetadataContainer.validate_origin.return_value = None
            get_container_from_origin('dummy', True, True)

        with self.assertRaises(Exception):
            get_container_from_origin(None, False, False)

        with self.assertRaises(Exception):
            get_files_from_origin(None)

        with self.assertRaises(Exception):
            get_files_from_origin('dummy')

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
