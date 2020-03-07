from create_models.utils import get_words


class ModelInfo:

    def __init__(self, line: str):
        """
        Obtém informações da model (primeira linha do CSV)
        namespace.promax_model_name;namespace.microservice_model_name

        {"model": {"promax": "namespace.promax_model_name", "ms": "namespace.microservice_model_name"}}
        """
        self._promax_model = None
        self._ms_model = None
        self._namespace_promax = None
        self._namespace_ms = None

        if isinstance(line, str):
            self.load_from_str(line)
        elif isinstance(line, dict):
            self.load_from_dict(line)
            
        self.validate_data()

    def validate_data(self):
        if self._promax_model and self._namespace_promax and self._ms_model and self._namespace_ms:
            return True
        raise ValueError("ModelInfo init error (invalid argument)")

    def load_from_str(self, line) -> (str, str):
        promax, ms = get_words(line, 2, ';')
        self.load(promax, ms)

    def load_from_dict(self, model_info):
        if "model" in model_info:
            model_data = model_info['model']
            if "promax" in model_data and "ms" in model_data:
                self.load(model_data['promax'], model_data['ms'])

    def load(self, promax, ms):
        promax_ns, promax_model = get_words(
            promax, 2, '.')
        ms_ns, ms_model = get_words(ms, 2, '.')
        if promax_ns and promax_model and ms_ns and ms_model:
            self._namespace_promax = promax_ns
            self._promax_model = promax_model
            self._namespace_ms = ms_ns
            self._ms_model = ms_model

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
        return str({"modelinfo": {
            "promax": self.namespace_promax+'.'+self.promax_model,
            "microservice": self.namespace_ms+"."+self.ms_model
        }})
