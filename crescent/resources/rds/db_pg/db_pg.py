from crescent.core import Resource, Tag
from .constants import AllowedValues, ResourceRequiredProperties


class DBParameterGroup(Resource):
    __TYPE = "AWS::RDS::DBParameterGroup"

    def __init__(self, id: str):
        super(DBParameterGroup, self).__init__(
            id=id,
            type=self.__TYPE,
            allowed_values={self.Family.__name__: AllowedValues.FAMILY},
            required_properties=ResourceRequiredProperties.DB_PARAMETER_GROUP
        )

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def Family(self, family: str):
        return self._set_property(self.Family.__name__, family)

    def Parameters(self, parameters: dict):
        return self._set_property(self.Parameters.__name__, parameters)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
