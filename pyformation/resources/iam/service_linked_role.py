from pyformation.core import Resource, Validator


class ServiceLinkedRole(Resource):
    __TYPE = "AWS::IAM::ServiceLinkedRole"

    def __init__(self, id: str):
        super(ServiceLinkedRole, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def AWSServiceName(self, value: str):
        return self._set_property(self.AWSServiceName.__name__, value)

    @Validator.validate(type=str)
    def CustomSuffix(self, value: str):
        return self._set_property(self.CustomSuffix.__name__, value)

    @Validator.validate(type=str)
    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)