from datetime import datetime

from .model_creator import ModelCreator
from .model_field import ModelField
from .utils import snake_to_camel


def create_ms_model(model: ModelCreator):
    linhas = [
        "from canaa_base import BaseModel",
        "",
        "",
        'class {0}Model(BaseModel):\n'.format(
            snake_to_camel(model.info.ms_model)),
        '\tdef __init__(self):',
        '\t\tself.integration_fields: dict = {}'
    ]

    for _import in model.imports():
        linhas.insert(0, _import)

    field: ModelField = None

    for field in model.fields:
        linhas.append('\t\tself.{0}: {1} = {2}'.format(
            field.field_ms,
            field.type_ms,
            field.default_value
        ))

    linhas.append('\n\n# CREATED BY MODEL_CREATOR IN ' +
                  str(datetime.now()) + "\n")
    return "\n".join(linhas)
