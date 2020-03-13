from pyformation.core import Resource, Validator


class AccessKey(Resource):
    __TYPE = "AWS::IAM::AccessKey"

    def __init__(self, id: str):
        super(AccessKey, self).__init__(id, self.__TYPE)

    @Validator.validate(type=int)
    def Serial(self, value: int):
        return self._set_property(self.Serial.__name__, value)

    @Validator.validate(type=str)
    def Status(self, value: str):
        return self._set_property(self.Status.__name__, value)

    @Validator.validate(type=str)
    def Username(self, value: str):
        return self._set_property(self.Username.__name__, value)
