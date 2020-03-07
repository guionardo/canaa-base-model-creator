import os

from .create_dto import create_dto
from .create_ms_model import create_ms_model
from .create_promax_model import create_promax_model
from .model_creator import ModelCreator


def create_files(model: ModelCreator, destiny_folder: str):
    if not os.path.isdir(destiny_folder):
        raise FileNotFoundError(destiny_folder)

    destiny_folder = os.path.abspath(destiny_folder)

    namespace_promax = "" if not model.info.namespace_promax else model.info.namespace_promax
    namespace_ms = "" if not model.info.namespace_ms else model.info.namespace_ms

    promax_model_folder = os.path.join(
        destiny_folder, 'domain', 'models', 'promax', namespace_promax)
    promax_file = os.path.join(
        promax_model_folder, model.promax_model_file_name)

    ms_model_folder = os.path.join(
        destiny_folder, 'domain', 'models', 'microservice', namespace_ms)
    ms_file = os.path.join(ms_model_folder, model.ms_model_file_name)

    dto_folder = os.path.join(
        destiny_folder, 'domain', 'models', 'dtos', namespace_ms)
    dto_file = os.path.join(dto_folder, model.dto_file_name)

    if not os.path.isdir(promax_model_folder):
        os.makedirs(promax_model_folder)
    if not os.path.isdir(ms_model_folder):
        os.makedirs(ms_model_folder)
    if not os.path.isdir(dto_folder):
        os.makedirs(dto_folder)

    promax = create_promax_model(model)
    with open(promax_file, 'w') as f:
        f.write(promax)

    ms = create_ms_model(model)
    with open(ms_file, 'w') as f:
        f.write(ms)

    dto = create_dto(model)
    with open(dto_file, 'w') as f:
        f.write(dto)
