import unittest
import os
from create_models.model_creator import ModelCreator


class TestCreator(unittest.TestCase):

    def test_create_promax(self):

        mc = ModelCreator("parametros-0200.csv")
        bm = mc.create_promax_model()
        promax_file = mc.promax_model_file_name+".py"
        with open(promax_file, 'w') as f:
            f.write(bm)
