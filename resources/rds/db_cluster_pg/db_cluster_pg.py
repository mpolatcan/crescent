from resources.shared import BaseCloudFormationResourceModel, Tag


class DBClusterParameterGroup(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::DBClusterParameterGroup"
    __PROPERTY_DESCRIPTION = "Description"
    __PROPERTY_FAMILY = "Family"
    __PROPERTY_PARAMETERS = "Parameters"
    __PROPERTY_TAGS = "Tags"

    def __init__(self):
        super(DBClusterParameterGroup, self).__init__(type=self.__TYPE)

    def description(self, value: str):
        return self._add_property_field(self.__PROPERTY_DESCRIPTION, value)

    def family(self, value: str):
        return self._add_property_field(self.__PROPERTY_FAMILY, value)

    def parameters(self, value: dict):
        return self._add_property_field(self.__PROPERTY_PARAMETERS, value)

    def tags(self, *value: Tag):
        return self._add_property_field(self.__PROPERTY_TAGS, [
            tag.create() for tag in list(value)
        ])
