from canaa_base import BaseModel


class RadioFrequenciaModel(BaseModel):

    def __init__(self, radiofrequencia: dict):
        super().__init__(incoming_data=radiofrequencia)

        self.utiliza_radio_frequencia: bool =\
            self.get_value('utiliza_radio_frequencia',
                           field_type=bool)
        self.utiliza_comodato: bool =\
            self.get_value('utiliza_comodato',
                           field_type=bool)
        self.utiliza_materiais: bool =\
            self.get_value('utiliza_materiais',
                           field_type=bool)
        self.numeracao_barril: bool =\
            self.get_value('numeracao_barril',
                           field_type=bool)
        self.considera_devolucao: bool =\
            self.get_value('considera_devolucao',
                           field_type=bool)

        self.permanencias: PermanenciasModel = \
            PermanenciasModel(self.get_value(field='permanencias',
                                             type=dict)).to_dict()
