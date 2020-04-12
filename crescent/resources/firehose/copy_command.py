from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class CopyCommand(Model):
    def __init__(self):
        super(CopyCommand, self).__init__(
            min_length={self.DataTableName.__name__: 1},
            required_properties=ModelRequiredProperties.COPY_COMMAND
        )

    def CopyOptions(self, copy_options: Union[str, AnyFn]):
        return self._set_field(self.CopyOptions.__name__, copy_options)

    def DataTableColumns(self, data_table_cols: Union[str, AnyFn]):
        return self._set_field(self.DataTableColumns.__name__, data_table_cols)

    def DataTableName(self, data_table_name: Union[str, AnyFn]):
        return self._set_field(self.DataTableName.__name__, data_table_name)
