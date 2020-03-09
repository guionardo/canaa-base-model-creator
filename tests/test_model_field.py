import unittest

from create_models.model_field import ModelField


class TestModelField(unittest.TestCase):

    def test_model_field(self):
        mi = ModelField(
            "ind_est_vendas;DescricaoModel;sales_state;DescriptionModel;")
        self.assertEqual(mi.field_promax, "ind_est_vendas")
        self.assertEqual(mi.field_ms, "sales_state")
        self.assertEqual(mi.type_promax, "DescricaoModel")
        self.assertEqual(mi.type_ms, "DescriptionModel")
