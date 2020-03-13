from pyformation.core import Model, Validator


class SchemaConfiguration(Model):
    @Validator.validate(type=str)
    def CatalogId(self, value: str):
        return self._set_field(self.CatalogId.__name__, value)

    @Validator.validate(type=str)
    def DatabaseName(self, value: str):
        return self._set_field(self.DatabaseName.__name__, value)

    @Validator.validate(type=str)
    def Region(self, value: str):
        return self._set_field(self.Region.__name__, value)

    @Validator.validate(type=str)
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=str)
    def TableName(self, value: str):
        return self._set_field(self.TableName.__name__, value)

    @Validator.validate(type=str)
    def VersionId(self, value: str):
        return self._set_field(self.VersionId.__name__, value)
