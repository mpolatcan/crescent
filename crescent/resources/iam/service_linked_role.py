from crescent.core import Resource, Validator


class ServiceLinkedRole(Resource):
    __TYPE = "AWS::IAM::ServiceLinkedRole"

    def __init__(self, id: str):
        super(ServiceLinkedRole, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str, min_length=1, max_length=128, pattern=r"[\w+=,.@-]+")
    def AWSServiceName(self, aws_service_name: str):
        return self._set_property(self.AWSServiceName.__name__, aws_service_name)

    @Validator.validate(type=str, min_length=1, max_length=64, pattern=r"[\w+=,.@-]+")
    def CustomSuffix(self, custom_suffix: str):
        return self._set_property(self.CustomSuffix.__name__, custom_suffix)

    @Validator.validate(type=str, max_length=1000, pattern=r"[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*")
    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)