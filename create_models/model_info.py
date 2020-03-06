from create_models.utils import get_words


class ModelInfo:

    def __init__(self, line: str):
        '''
        Obtém informações da model (primeira linha do CSV)
        parametros_0200;parameters_0200;namespace_promax;namespace_ms
        '''
        (self._promax_model,
         self._ms_model,
         self._namespace_promax,
         self._namespace_ms) = get_words(line, 4)
        if self._namespace_promax and not self._namespace_ms:
            self._namespace_ms = self._namespace_promax
        print(str(self))

    @property
    def promax_model(self):
        return self._promax_model

    @property
    def ms_model(self):
        return self._ms_model

    @property
    def namespace_promax(self):
        return self._namespace_promax

    @property
    def namespace_ms(self):
        return self._namespace_ms

    def __str__(self):
        return str({"modelinfo":
                    {"promax_model": self.promax_model,
                     "ms_model": self.ms_model,
                     "namespace_promax": self.namespace_promax,
                     "namsepace_ms": self.namespace_ms}})
