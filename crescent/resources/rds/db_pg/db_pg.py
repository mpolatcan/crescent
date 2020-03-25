from crescent.core import Resource, Tag, Validator


class DBParameterGroup(Resource):
    __TYPE = "AWS::RDS::DBParameterGroup"

    def __init__(self, id: str):
        super(DBParameterGroup, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)

    # TODO Allowed values validation will be added
    @Validator.validate(type=str)
    def Family(self, value: str):
        return self._set_property(self.Family.__name__, value)

    @Validator.validate(type=dict)
    def Parameters(self, value: dict):
        return self._set_property(self.Parameters.__name__, value)

    @Validator.validate(type=Tag)
    def Tags(self, *value: Tag):
        return self._set_property(self.Tags.__name__, list(value))
