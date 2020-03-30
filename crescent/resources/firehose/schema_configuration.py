from crescent.core import Model, Validator


class SchemaConfiguration(Model):
    @Validator.validate(type=str, pattern=r"^\S+$")
    def CatalogId(self, catalog_id: str):
        return self._set_field(self.CatalogId.__name__, catalog_id)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def DatabaseName(self, database_name: str):
        return self._set_field(self.DatabaseName.__name__, database_name)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def Region(self, region: str):
        return self._set_field(self.Region.__name__, region)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def TableName(self, table_name: str):
        return self._set_field(self.TableName.__name__, table_name)

    @Validator.validate(type=str, pattern=r"^\S+$")
    def VersionId(self, version_id: str):
        return self._set_field(self.VersionId.__name__, version_id)
