from pyformation.core import Model, Validator


class SchemaConfiguration(Model):
    @Validator.validate(type=str, pattern=r"^\S+$")
    def CatalogId(self, value: str):
        return self._set_field(self.CatalogId.__name__, value)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def DatabaseName(self, value: str):
        return self._set_field(self.DatabaseName.__name__, value)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def Region(self, value: str):
        return self._set_field(self.Region.__name__, value)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def RoleARN(self, value: str):
        return self._set_field(self.RoleARN.__name__, value)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def TableName(self, value: str):
        return self._set_field(self.TableName.__name__, value)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def VersionId(self, value: str):
        return self._set_field(self.VersionId.__name__, value)
