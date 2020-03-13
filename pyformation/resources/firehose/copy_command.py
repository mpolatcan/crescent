from pyformation.core import Model, Validator


class CopyCommand(Model):
    @Validator.validate(type=str)
    def CopyOptions(self, value: str):
        return self._set_field(self.CopyOptions.__name__, value)

    @Validator.validate(type=str)
    def DataTableColumns(self, value: str):
        return self._set_field(self.DataTableColumns.__name__, value)

    @Validator.validate(type=str)
    def DataTableName(self, value: str):
        return self._set_field(self.DataTableName.__name__, value)
