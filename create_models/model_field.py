from create_models.utils import get_words


class ModelField:

    TYPES = {
        "int":"int",
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

    DEFAULT_VALUES = {
        "number": "0",
        "float": "0.0",
        "string": "None",
        "boolean": "False",
        "str": "None",
        "bool": "False",
        "date": "None",
        "datetime": "None",
        "time": "None"
    }

    def __init__(self, line: str):
        '''
        Obtém um campo da model
        campo_promax;tipo_promax;campo_ms;tipo_ms;extra_info
        utiliza_robin_hood;boolean;uses_robin_hood
        ind_est_vendas;DescricaoModel;sales_state;DescriptionModel
        '''

        self._field_promax: str = None
        self._field_ms: str = None
        self._type_promax: str = None
        self._type_ms: str = None
        self._required: bool = False
        self._pk: bool = False

        if isinstance(line, str):
            self.load_from_str(line)
        elif isinstance(line, dict):
            self.load_from_dict(line)
        elif isinstance(line, list):
            self.load_from_list(line)

        self._type_promax = self._validate_type(self._type_promax)
        self._type_ms = self._validate_type(self._type_ms)
        if not self._type_ms:
            self._type_ms = self._type_promax

    def load_from_str(self, line):
        (self._field_promax,
         self._type_promax,
         self._field_ms,
         self._type_ms,
         extra) = get_words(line, 5)
        self._required = extra and extra.lower() == 'required'
        self._pk = extra and extra.lower() == 'pk'

    def load_from_dict(self, data):
        pass

    def load_from_list(self, data):
        if len(data) == 5:
            (self._field_promax,
             self._type_promax,
             self._field_ms,
             self._type_ms,
             extra) = data
            self._required = extra and extra.lower() == 'required'
            self._pk = extra and extra.lower() == 'pk'

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
    def extra(self):
        if self._pk:
            return 'pk'
        elif self._required:
            return 'required'
        return ''

    @property
    def pk(self):
        return self._pk

    @property
    def ok(self):
        return self._field_promax and self._type_promax and self.field_ms

    @property
    def primitive_type(self):
        return self._type_promax in self.TYPES

    @property
    def default_value(self) -> str:
        if not self.primitive_type:
            return self.type_ms+'()'
        if self.type_ms in self.DEFAULT_VALUES:
            return self.DEFAULT_VALUES[self.type_ms]
        return 'None'

    @classmethod
    def _validate_type(cls, tp: str):
        if tp is None:
            return None

        if tp.lower() in cls.TYPES:
            tp = cls.TYPES[tp.lower()]

        return tp
