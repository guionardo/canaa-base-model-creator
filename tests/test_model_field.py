import unittest

from create_models.model_field import ModelField


class TestModelField(unittest.TestCase):

    def test_model_field(self):
        mi = ModelField(
            "ind_est_vendas;DescricaoModel;sales_state; DescriptionModel;pk")
        self.assertEqual(mi.field_promax, "ind_est_vendas")
        self.assertEqual(mi.field_ms, "sales_state")
        self.assertEqual(mi.type_promax, "DescricaoModel")
        self.assertEqual(mi.type_ms, "DescriptionModel")
        self.assertTrue(mi.pk)
        self.assertTrue(mi.required)

    def test_model_field_error(self):
        with self.assertRaises(Exception):
            ModelField(None)

        with self.assertRaises(Exception):
            ModelField('')

    def test_model_field_without_type(self):
        mi = ModelField(
            "ind_est_vendas;int;sales_state")
        self.assertEqual(mi.field_promax, "ind_est_vendas")
        self.assertEqual(mi.type_promax, "int")
        self.assertEqual(mi.type_ms, "int")

    def test_valid_field_names(self):
        self.assertTrue(ModelField.is_valid_field_name('ind_est_vendas'))
        self.assertTrue(ModelField.is_valid_field_name('_abc_123'))
        self.assertFalse(ModelField.is_valid_field_name('123abc'))
        self.assertFalse(ModelField.is_valid_field_name('abc#-'))
