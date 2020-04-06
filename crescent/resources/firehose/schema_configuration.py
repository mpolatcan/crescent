from crescent.core import Model
from .constants import ModelRequiredProperties


class SchemaConfiguration(Model):
    def __init__(self):
        super(SchemaConfiguration, self).__init__(
            pattern={self.CatalogId.__name__: r"^\S+$",
                     self.DatabaseName.__name__: r"^\S+$",
                     self.Region.__name__: r"^\S+$",
                     self.RoleARN.__name__: r"^\S+$",
                     self.TableName.__name__: r"^\S+$",
                     self.VersionId.__name__: r"^\S+$"},
            required_properties=ModelRequiredProperties.SCHEMA_CONFIGURATION
        )

    def CatalogId(self, catalog_id: str):
        return self._set_field(self.CatalogId.__name__, catalog_id)

    def DatabaseName(self, database_name: str):
        return self._set_field(self.DatabaseName.__name__, database_name)

    def Region(self, region: str):
        return self._set_field(self.Region.__name__, region)

    def RoleARN(self, role_arn: str):
        return self._set_field(self.RoleARN.__name__, role_arn)

    def TableName(self, table_name: str):
        return self._set_field(self.TableName.__name__, table_name)

    def VersionId(self, version_id: str):
        return self._set_field(self.VersionId.__name__, version_id)
