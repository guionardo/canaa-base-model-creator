from datetime import datetime

from create_models.model_creator import ModelCreator
from create_models.model_field import ModelField
from create_models.utils import snake_to_camel


def create_promax_model(model: ModelCreator):
    linhas = ["from canaa_base import BaseModel", "", ""]

    arg = model.promax_model_file_name
    linhas.append('class {0}Model(BaseModel):\n'.format(
        snake_to_camel(model.info.promax_model)))

    linhas.append('\tdef __init__(self, ' + arg + ': dict):')
    linhas.append('\t\tsuper().__init__(' + arg + ')\n')

    imports = ["from canaa_base import BaseModel"]
    has_datetime, has_time, has_date = False, False, False
    field: ModelField = None
    for field in model.fields:
        has_datetime |= 'datetime' in [field.type_promax, field.type_ms]
        has_time |= 'time' in [field.type_promax, field.type_ms]
        has_date |= 'date' in [field.type_promax, field.type_ms]

        com = "\n\t\t# " + field.field_ms
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
        linhas.insert(0, "from datetime import " + (",".join(dt_imports)))

    linhas.append('\n\n# CREATED BY MODEL_CREATOR IN ' +
                  str(datetime.now()) + "\n")
    return "\n".join(linhas)
