from pyformation.resources.shared import BaseModel


class CopyCommand(BaseModel):
    __PROPERTY_COPY_OPTIONS = "CopyOptions"
    __PROPERTY_DATA_TABLE_COLUMNS = "DataTableColumns"
    __PROPERTY_DATA_TABLE_NAME = "DataTableName"

    def copy_options(self, value: str):
        return self._add_field(self.__PROPERTY_COPY_OPTIONS, value)

    def data_table_columns(self, value: str):
        return self._add_field(self.__PROPERTY_DATA_TABLE_COLUMNS, value)

    def data_table_name(self, value: str):
        return self._add_field(self.__PROPERTY_DATA_TABLE_NAME, value)
