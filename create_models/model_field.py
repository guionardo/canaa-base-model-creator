from create_models.utils import get_words


class ModelField:

    TYPES = {
        "number": "int",
        "float": "float",
        "string": "str",
        "boolean": "bool",
        "str": "str",
        "bool": "bool",
        "date": "date",
        "datetime": "datetime",
        "time": "time"
    }

    def __init__(self, line: str):
        '''
        Obtém um campo da model
        campo_promax;tipo_promax;campo_ms;tipo_ms
        utiliza_robin_hood;boolean;uses_robin_hood
        ind_est_vendas;DescricaoModel;sales_state;DescriptionModel
        '''

        w = get_words(line, 5)

        self._field_promax, self._type_promax, self._field_ms, self._type_ms = w[:4]
        self._type_promax = self._validate_type(self._type_promax)
        self._type_ms = self._validate_type(self._type_ms)
        self._required = bool(w[4])

    @property
    def field_promax(self):
        return self._field_promax

    @property
    def type_promax(self):
        return self._type_promax

    @property
    def field_ms(self):
        return self._field_ms

    @property
    def type_ms(self):
        return self._type_ms

    @property
    def required(self):
        return self._required

    @property
    def ok(self):
        return self._field_promax and self._type_promax and self.field_ms

    @property
    def primitive_type(self):
        return self._type_promax in self.TYPES

    @classmethod
    def _validate_type(cls, tp: str):
        if tp is None:
            return None

        if tp.lower() in cls.TYPES:
            tp = cls.TYPES[tp.lower()]

        return tp
