import unittest

from cli.data_type.primitive_types import (get_default_primitive_type_as_str,
                                           get_fake_primitive_type,
                                           get_type_class_from_str,
                                           get_type_from_str,
                                           is_primitive_type)
from datetime import datetime


class TestPrimitiveTypes(unittest.TestCase):

    def test_get_type_from_str(self):
        self.assertEqual('int', get_type_from_str('number'))
        self.assertEqual('float', get_type_from_str('decimal'))
        self.assertEqual('None', get_type_from_str('DescriptionModel'))

    def test_is_primitive_type(self):
        self.assertTrue(is_primitive_type('str'))
        self.assertFalse(is_primitive_type('DescriptionModel'))

    def test_get_type_class_from_str(self):
        self.assertEqual(int, get_type_class_from_str('number'))
        self.assertIsNone(get_type_class_from_str('DescriptionModel'))

    def test_get_default_primitive_type_as_str(self):
        self.assertEqual('0', get_default_primitive_type_as_str('int'))

    def test_get_fake_primitive_type_ms(self):
        int_fake = get_fake_primitive_type('int', False)
        str_fake = get_fake_primitive_type('str', False)
        date_fake = get_fake_primitive_type('date', False)
        datetime_fake = get_fake_primitive_type('datetime', False)
        time_fake = get_fake_primitive_type('time', False)
        float_fake = get_fake_primitive_type('float', False)
        bool_fake = get_fake_primitive_type('bool', False)
        self.assertIsInstance(int_fake, int)
        self.assertIsInstance(str_fake, str)
        self.assertIsInstance(date_fake, datetime)
        self.assertIsInstance(datetime_fake, datetime)
        self.assertIsInstance(time_fake, int)
        self.assertIsInstance(float_fake, float)
        self.assertIsInstance(bool_fake, bool)

    def test_get_fake_primitive_type_promax(self):
        int_fake = get_fake_primitive_type('int')
        str_fake = get_fake_primitive_type('str')
        date_fake = get_fake_primitive_type('date')
        datetime_fake = get_fake_primitive_type('datetime')
        time_fake = get_fake_primitive_type('time')
        float_fake = get_fake_primitive_type('float')
        bool_fake = get_fake_primitive_type('bool')
        self.assertIsInstance(int_fake, int)
        self.assertIsInstance(str_fake, str)
        self.assertIsInstance(date_fake, str)
        self.assertIsInstance(datetime_fake, str)
        self.assertIsInstance(time_fake, str)
        self.assertIsInstance(float_fake, float)
        self.assertIsInstance(bool_fake, bool)
