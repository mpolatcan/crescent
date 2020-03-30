from crescent.core import Model, Validator


class CopyCommand(Model):
    @Validator.validate(type=str)
    def CopyOptions(self, copy_options: str):
        return self._set_field(self.CopyOptions.__name__, copy_options)

    @Validator.validate(type=str)
    def DataTableColumns(self, data_table_cols: str):
        return self._set_field(self.DataTableColumns.__name__, data_table_cols)

    @Validator.validate(type=str, min_length=1)
    def DataTableName(self, data_table_name: str):
        return self._set_field(self.DataTableName.__name__, data_table_name)
