from pyformation import PyformationModel


class CopyCommand(PyformationModel):
    def CopyOptions(self, value: str):
        return self._set_field(self.CopyOptions.__name__, value)

    def DataTableColumns(self, value: str):
        return self._set_field(self.DataTableColumns.__name__, value)

    def DataTableName(self, value: str):
        return self._set_field(self.DataTableName.__name__, value)
