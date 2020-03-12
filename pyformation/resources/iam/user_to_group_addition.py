from pyformation import PyformationResource


class UserToGroupAddition(PyformationResource):
    __TYPE = "AWS::IAM::UserToGroupAddition"

    def __init__(self, id: str):
        super(UserToGroupAddition, self).__init__(id, self.__TYPE)

    def GroupName(self, value: str):
        return self._set_property(self.GroupName.__name__, value)

    def Users(self, *value: str):
        return self._set_property(self.Users.__name__, list(value))
