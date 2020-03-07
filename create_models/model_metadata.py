import os


class ModelMetadata:
    """
    Metadata for model build

    Informations:
    * Promax model name
    * Microservice model name
    * Fields
    """

    def __init__(self, file_name):
        if not isinstance(file_name, str):
            raise AttributeError("Invalid file_name. Str type expected ({0}:{1})".format(file_name, type(file_name)))
        if not os.path.isfile(file_name):
            raise FileNotFoundError("File not found ({0})".format(file_name))


