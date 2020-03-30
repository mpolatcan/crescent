from crescent.core import Resource, Tag, Validator
from .constants import AllowedValues


class DBClusterParameterGroup(Resource):
    __TYPE = "AWS::RDS::DBClusterParameterGroup"

    def __init__(self, id: str):
        super(DBClusterParameterGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    @Validator.validate(type=str, allowed_values=AllowedValues.FAMILY)
    def Family(self, family: str):
        return self._set_property(self.Family.__name__, family)

    @Validator.validate(type=dict)
    def Parameters(self, parameters: dict):
        return self._set_property(self.Parameters.__name__, parameters)

    @Validator.validate(type=Tag)
    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))
