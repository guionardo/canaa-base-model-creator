import glob
import os

from ..containers.metadata_folder_container import FolderContainer
from ..containers.metadata_xlsx_container import XLSXContainer
from ..interfaces.metadata_container_interface import \
    MetadataContainerException
from ..model_creator import ModelCreator
from ..utils import get_file_extension


def get_files_from_origin(origin: str):
    if not isinstance(origin, str) or not origin:
        raise MetadataContainerException('Invalid origin "{0}"'.format(origin))

    files = []
    error = None
    if '*' in origin or '?' in origin:
        files, error = _get_masked_files(origin)

    else:
        if os.path.isfile(origin):
            files, error = _get_unique_file(origin)

        elif os.path.isdir(origin):
            files, error = _get_files_from_path(origin)

        else:
            error = 'Origin not found in {0}'.format(origin)

    if error:
        raise MetadataContainerException(error)

    csv_files = [file for file in files
                 if get_file_extension(file) == '.csv']
    xlsx_files = [file for file in files
                  if get_file_extension(file) == '.xlsx']

    return csv_files, xlsx_files


def get_creators(origin: str, ignore_field_errors: bool, just_validate: bool) -> list:
    csv_files, xlsx_files = get_files_from_origin(origin)
    return _get_model_creators(csv_files, xlsx_files, ignore_field_errors, just_validate)


def is_valid_origin(origin: str) -> bool:
    creators = get_creators(origin, False, True)
    return len(creators) > 0


def _get_masked_files(origin):
    # masked files (.csv only)
    files = [file
             for file in glob.glob(origin)
             if get_file_extension(file) == '.csv']
    error = None if len(
        files) > 0 else 'No valid (.csv) files in {0}'.format(origin)

    return files, error


def _get_unique_file(origin):
    # get one file
    files = []
    error = None
    if get_file_extension(origin) in ['.csv', '.xlsx']:
        if os.path.isfile(origin):
            files = [origin]
        else:
            error = 'File not found {0}'.format(origin)

    else:

        error = 'No valid file (.csv or .xlsx) in {0}'.format(origin)

    return files, error


def _get_files_from_path(origin):
    # get files on folder
    files = [file for file in glob.glob(os.path.join(origin, '*.csv')) +
             glob.glob(os.path.join(origin, '*.xlsx')) if not os.path.basename(file).startswith('~')]
    error = None if len(
        files) > 0 else 'No valid (.csv or .xlsx) files in {0}'.format(origin)

    return files, error


def _get_model_creators(csv_files, xlsx_files, ignore_field_errors, just_validate):
    model_creators = []
    for csv_file in csv_files:
        mc = ModelCreator(csv_file, ignore_field_errors, just_validate)
        if mc.is_ok:
            model_creators.append(mc)

    for xlsx_file in xlsx_files:
        cnt = XLSXContainer(xlsx_file, ignore_field_errors, just_validate)
        for mc in cnt.get_model_creators():
            model_creators.append(mc)

    model_creators = ModelCreator.sorted_creators_list(model_creators)

    return model_creators
