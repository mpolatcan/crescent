from pyformation.resources.shared import BaseModel
from pyformation.resources.s3.bucket import DataExport


class StorageClassAnalysis(BaseModel):
    __PROPERTY_DATA_EXPORT = "DataExport"

    def data_export(self, value: DataExport):
        return self._add_field(self.__PROPERTY_DATA_EXPORT, value)
