from collections import defaultdict
from datetime import datetime

from .model_creator import ModelCreator
from .model_field import ModelField
from .utils import snake_to_camel


def create_dto(model: ModelCreator):
    linhas = [
        "from canaa_base import BaseModel",
        "",
        "",
        'class {0}DTO({0}Model):\n'.format(
            snake_to_camel(model.info.ms_model)), '\tdef __init__(self, arg: {0}Model):'.format(
            snake_to_camel(model.info.promax_model)), '\t\tsuper().__init__()'
    ]

    field: ModelField = None
    if len(model.pks) > 0:
        linhas.append('\t\tself.integration_fields = {')
        i = 0
        for field in model.pks:
            i += 1
            linhas.append('\t\t\t"{0}": {1},'.format(
                field.field_ms, i
            ))
        linhas.append('\t\t}\n')

    _imp = defaultdict(set)

    for field in model.fields:
        if field.primitive_type:
            linhas.append('\t\tself.{0} = arg.{1}'.format(
                field.field_ms,
                field.field_promax
            ))
        else:
            class_name = snake_to_camel(field.field_ms)+'DTO'
            linhas.append('\t\tself.{0} = {1}(arg.{2}).to_dict()'.format(
                field.field_ms,
                class_name,
                field.field_promax
            ))
            _imp["domain.models.microservice.{0}.{1}".format(
                model.info.namespace_ms,
                field.field_ms+'_dto'
            )].add(class_name)

    _imp = dict(_imp)
    if len(_imp) > 0:
        _imp = [
            "from {0} import {1}".format(
                mod, ", ".join(_imp[mod]))
            for mod in _imp
        ]
        for imp in _imp:
            linhas.insert(0, imp)

    linhas.insert(0, 'from domain.models.microservice.{0}.{1} import {2}'.format(
        model.info.namespace_ms,
        model.info.ms_model,
        snake_to_camel(model.info.ms_model)
    ))
    linhas.insert(0, 'from domain.models.promax.{0}.{1} import {2}'.format(
        model.info.namespace_promax,
        model.info.promax_model,
        snake_to_camel(model.info.promax_model)
    ))

    linhas.append('\n\n# CREATED BY MODEL_CREATOR IN ' +
                  str(datetime.now()) + "\n")
    return "\n".join(linhas)
