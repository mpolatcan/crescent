from crescent.core import Resource, Validator
from .constants import AllowedValues


class AccessKey(Resource):
    __TYPE = "AWS::IAM::AccessKey"

    def __init__(self, id: str):
        super(AccessKey, self).__init__(id, self.__TYPE)

    @Validator.validate(type=int)
    def Serial(self, serial: int):
        return self._set_property(self.Serial.__name__, serial)

    @Validator.validate(type=str, allowed_values=AllowedValues.STATUS)
    def Status(self, status: str):
        return self._set_property(self.Status.__name__, status)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def Username(self, username: str):
        return self._set_property(self.Username.__name__, username)
