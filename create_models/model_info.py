from create_models.utils import get_words


class ModelInfo:

    def __init__(self, line: str):
        '''
        Obtém informações da model (primeira linha do CSV)
        parametros_0200;parameters_0200;
        '''
        self._promax_model, self._ms_model = get_words(line, 2)

    @property
    def promax_model(self):
        return self._promax_model

    @property
    def ms_model(self):
        return self._ms_model
