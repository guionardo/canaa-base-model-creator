from ..interfaces.metadata_container_interface import IMetadataContainer, MetadataContainerException
from ..model_creator import ModelCreator
from ..utils import get_file_extension
import os
import glob


class FolderContainer(IMetadataContainer):

    def get_metadata_files(self):
        return self.origin

    def validate_origin(self, origin):
        if os.path.isdir(origin):
            # Find csv files
            files = glob.glob(os.path.join(origin, '*.csv'))

            if len(files) > 0:
                self.origin = files
            else:
                raise MetadataContainerException(
                    "No .csv files found in {0}".format(origin))
        else:
            raise FileNotFoundError(origin)

    def get_model_creators(self):
        if not self._model_creators:
            self._model_creators = []
            for file in self.origin:
                mc = ModelCreator(
                    origin=file,
                    ignore_field_errors=self.ignore_field_errors,
                    just_validate=self.just_validate)
                if mc.is_ok:
                    self._model_creators.append(mc)

        return self._model_creators
