import os
from datetime import datetime

from .model_field import ModelField
from .model_info import ModelInfo
from .utils import camel_to_snake, snake_to_camel


class ModelCreator:

    def __init__(self, arquivo):
        if not os.path.exists(arquivo):
            raise FileNotFoundError(arquivo)

        has_head = False
        self.fields = []
        self.info: ModelInfo = None

        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f.readlines():
                if not has_head:
                    self.info = ModelInfo(linha)
                    has_head = True
                else:
                    field = ModelField(linha)
                    if field.ok:
                        self.fields.append(field)

        self.promax_model_file_name = camel_to_snake(self.info.promax_model)
        self.ms_model_file_name = camel_to_snake(self.info.ms_model)

    def create_files(self):
        
    def create_promax_model(self):
        linhas = ["from canaa_base import BaseModel", "", ""]

        arg = self.promax_model_file_name
        linhas.append('class {0}Model(BaseModel):\n'.format(
            snake_to_camel(self.info.promax_model)))

        linhas.append('\tdef __init__(self, '+arg+': dict):')
        linhas.append('\t\tsuper().__init__('+arg+')\n')

        imports = ["from canaa_base import BaseModel"]
        has_datetime, has_time, has_date = False, False, False
        field: ModelField = None
        for field in self.fields:
            has_datetime |= 'datetime' in [field.type_promax, field.type_ms]
            has_time |= 'time' in [field.type_promax, field.type_ms]
            has_date |= 'date' in [field.type_promax, field.type_ms]

            com = "\n\t\t# "+field.field_ms
            linhas.append(com)
            if field.primitive_type:
                campo = "\t\tself.{0}: {1} = \\\n\t\t\tself.get_value('{0}',field_type={1})".format(
                    field.field_promax,
                    field.type_promax
                )
            else:
                campo = "\t\tself.{0}: {1} = \\\n\t\t\t{1}(\n\t\t\t\tself.get_value('{0}',field_type=dict)).to_dict()".format(
                    field.field_promax,
                    field.type_promax
                )
            linhas.append(campo)

        dt_imports = []
        if has_datetime:
            dt_imports.append("datetime")
        if has_date:
            dt_imports.append("date")
        if has_time:
            dt_imports.append("time")

        if len(dt_imports) > 0:
            linhas.insert(0, "from datetime import "+(",".join(dt_imports)))

        linhas.append('\n\n# CREATED BY MODEL_CREATOR IN ' +
                      str(datetime.now())+"\n")
        return "\n".join(linhas)

    def create_dto(self):
