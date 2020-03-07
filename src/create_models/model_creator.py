import os
from collections import defaultdict
from datetime import datetime

import yaml

from .model_field import ModelField
from .model_info import ModelInfo
from .utils import camel_to_snake, snake_to_camel


class ModelCreator:

    def __init__(self, arquivo):
        if not os.path.exists(arquivo):
            raise FileNotFoundError(arquivo)

        self.fields = []
        self.info: ModelInfo = None
        self.pks = []
        self._imports = defaultdict(set)
        self._imports_dto = defaultdict(set)
        self._imports_ms = defaultdict(set)
        self._imports_promax = defaultdict(set)

        ext = os.path.splitext(arquivo)
        if len(ext) > 0:
            ext = ext[1].lower()
            if ext == '.csv':
                self.load_from_csv(arquivo)
            elif ext == '.yaml' or ext == '.yml':
                self.load_from_yaml(arquivo)

    @property
    def promax_model_file_name(self):
        if self.info:
            return camel_to_snake(self.info.promax_model)+"_model.py"
        return "undefined_promax_model.py"

    @property
    def ms_model_file_name(self):
        if self.info:
            return camel_to_snake(self.info.ms_model)+'_model.py'
        return "undefined_ms_model.py"

    @property
    def dto_file_name(self):
        if self.info:
            return camel_to_snake(self.info.ms_model)+'_dto.py'
        return "undefined_dto_model.py"

    def load_from_csv(self, file_name):
        has_head = False
        with open(file_name, 'r', encoding='utf-8') as f:
            for linha in f.readlines():
                if not has_head:
                    self.info = ModelInfo(linha)
                    has_head = True
                else:
                    self._add_field(ModelField(linha))

    def load_from_yaml(self, file_name):
        with open(file_name) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.info = ModelInfo(data)
            if "fields" in data:
                for field_data in data['fields']:
                    self._add_field(ModelField(field_data))

    def _add_field(self, field: ModelField):
        if field.ok:
            self.fields.append(field)
            if field.pk:
                self.pks.append(field)

            if 'datetime' in [field.type_promax, field.type_ms]:
                self._imports['datetime'].add('datetime')
            if 'time' in [field.type_promax, field.type_ms]:
                self._imports['datetime'].add('time')
            if 'date' in [field.type_promax, field.type_ms]:
                self._imports['datetime'].add('date')
            if not field.primitive_type:
                self._imports[self.info.namespace_ms +
                              '# TODO: CORRECT NAMESPACE #'].add(field.type_ms+'DTO')

    def imports(self):
        _imp = dict(self._imports)
        return [
            "from {0} import {1}".format(
                module, ", ".join(_imp[module]))
            for module in _imp
        ]
