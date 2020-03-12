from pyformation import PyformationModel


class SchemaConfiguration(PyformationModel):
    def CatalogId(self, value: str):
        return self._set_field(self.CatalogId.__name__, value)

    def DatabaseName(self, value: str):
        return self._set_field(self.DatabaseName.__name__, value)

    def Region(self, value: str):
        return self._set_field(self.Region.__name__, value)

    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    def TableName(self, value: str):
        return self._set_field(self.TableName.__name__, value)

    def VersionId(self, value: str):
        return self._set_field(self.VersionId.__name__, value)
