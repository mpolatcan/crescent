from crescent.core import Model
from .constants import ModelRequiredProperties


class CopyCommand(Model):
    def __init__(self):
        super(CopyCommand, self).__init__(
            min_length={self.DataTableName.__name__: 1},
            required_properties=ModelRequiredProperties.COPY_COMMAND
        )

    def CopyOptions(self, copy_options: str):
        return self._set_field(self.CopyOptions.__name__, copy_options)

    def DataTableColumns(self, data_table_cols: str):
        return self._set_field(self.DataTableColumns.__name__, data_table_cols)

    def DataTableName(self, data_table_name: str):
        return self._set_field(self.DataTableName.__name__, data_table_name)
