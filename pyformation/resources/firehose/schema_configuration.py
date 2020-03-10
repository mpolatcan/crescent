from resources.shared import BaseModel


class SchemaConfiguration(BaseModel):
    __PROPERTY_CATALOG_ID = "CatalogId"
    __PROPERTY_DATABASE_NAME = "DatabaseName"
    __PROPERTY_REGION = "Region"
    __PROPERTY_ROLE_ARN = "RoleARN"
    __PROPERTY_TABLE_NAME = "TableName"
    __PROPERTY_VERSION_ID = "VersionId"

    def catalog_id(self, value: str):
        return self._add_field(self.__PROPERTY_CATALOG_ID, value)

    def database_name(self, value: str):
        return self._add_field(self.__PROPERTY_DATABASE_NAME, value)

    def region(self, value: str):
        return self._add_field(self.__PROPERTY_REGION, value)

    def role_arn(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)

    def table_name(self, value: str):
        return self._add_field(self.__PROPERTY_ROLE_ARN, value)

    def version_id(self, value: str):
        return self._add_field(self.__PROPERTY_VERSION_ID, value)
