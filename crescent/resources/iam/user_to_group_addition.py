from crescent.core import Resource, Validator


class UserToGroupAddition(Resource):
    __TYPE = "AWS::IAM::UserToGroupAddition"

    def __init__(self, id: str):
        super(UserToGroupAddition, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def GroupName(self, group_name: str):
        return self._set_property(self.GroupName.__name__, group_name)

    @Validator.validate(type=str)
    def Users(self, *users: str):
        return self._set_property(self.Users.__name__, list(users))
