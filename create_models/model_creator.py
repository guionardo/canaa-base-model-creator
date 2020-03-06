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

        self.pks = []
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f.readlines():
                if not has_head:
                    self.info = ModelInfo(linha)
                    has_head = True
                else:
                    field = ModelField(linha)
                    if field.ok:
                        self.fields.append(field)
                        if field.pk:
                            self.pks.append(field)

        self.promax_model_file_name = camel_to_snake(
            self.info.promax_model)+'_model.py'
        self.ms_model_file_name = camel_to_snake(
            self.info.ms_model)+'_model.py'
        self.dto_file_name = camel_to_snake(self.info.ms_model)+'_dto.py'

    def create_files(self, destiny_folder: str):
        if not os.path.isdir(destiny_folder):
            raise FileNotFoundError(destiny_folder)

        destiny_folder = os.path.abspath(destiny_folder)
        namespace_promax = "" if not self.info.namespace_promax else self.info.namespace_promax
        namespace_ms = "" if not self.info.namespace_ms else self.info.namespace_ms

        promax_model_folder = os.path.join(
            destiny_folder, 'domain', 'models', 'promax', namespace_promax)
        ms_model_folder = os.path.join(
            destiny_folder, 'domain', 'models', 'microservice', namespace_ms)
        dto_folder = os.path.join(
            destiny_folder, 'domain', 'models', 'dtos', namespace_ms)

        if not os.path.isdir(promax_model_folder):
            os.makedirs(promax_model_folder)
        if not os.path.isdir(ms_model_folder):
            os.makedirs(ms_model_folder)
        if not os.path.isdir(dto_folder):
            os.makedirs(dto_folder)

        promax = self.create_promax_model()
        promax_file = os.path.join(
            promax_model_folder, self.promax_model_file_name)
        with open(promax_file, 'w') as f:
            f.write(promax)

        dto = self.create_dto()
        dto_file = os.path.join(dto_folder, self.dto_file_name)
        with open(dto_file, 'w') as f:
            f.write(dto)

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
        linhas = ["from canaa_base import BaseModel", "", ""]

        linhas.append('class {0}DTO({0}Model):\n'.format(
            snake_to_camel(self.info.ms_model)))

        linhas.append('\tdef __init__(self, arg: {0}Model):'.format(
            snake_to_camel(self.info.promax_model)))

        linhas.append('\t\tsuper().__init__()')
        field: ModelField = None
        if len(self.pks) > 0:
            linhas.append('\t\tself.integration_fields = {')
            i = 0
            for field in self.pks:
                i += 1
                linhas.append('\t\t\t"{0}": {1},'.format(
                    field.field_ms, i
                ))
            linhas.append('\t\t}\n')

        for field in self.fields:
            linhas.append('\t\tself.{0} = arg.{1}'.format(
                field.field_ms,
                field.field_promax
            ))

        linhas.append('\n\n# CREATED BY MODEL_CREATOR IN ' +
                      str(datetime.now())+"\n")
        return "\n".join(linhas)
