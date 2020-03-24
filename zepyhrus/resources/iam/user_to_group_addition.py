from zepyhrus.core import Resource, Validator


class UserToGroupAddition(Resource):
    __TYPE = "AWS::IAM::UserToGroupAddition"

    def __init__(self, id: str):
        super(UserToGroupAddition, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern="[\w+=,.@-]+")
    def GroupName(self, value: str):
        return self._set_property(self.GroupName.__name__, value)

    @Validator.validate(type=str)
    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
