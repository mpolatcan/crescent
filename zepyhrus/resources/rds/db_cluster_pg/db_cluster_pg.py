from zepyhrus.core import Resource, Tag, Validator


class DBClusterParameterGroup(Resource):
    __TYPE = "AWS::RDS::DBClusterParameterGroup"

    def __init__(self, id: str):
        super(DBClusterParameterGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    @Validator.validate(type=str)
    def Family(self, value: str):
        return self._set_property(self.Family.__name__, value)

    @Validator.validate(type=dict)
    def Parameters(self, value: dict):
        return self._set_property(self.Parameters.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
