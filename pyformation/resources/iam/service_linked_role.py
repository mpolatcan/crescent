from pyformation import PyformationResource


class ServiceLinkedRole(PyformationResource):
    __TYPE = "AWS::IAM::ServiceLinkedRole"

    def __init__(self, id: str):
        super(ServiceLinkedRole, self).__init__(id, self.__TYPE)

    def AWSServiceName(self, value: str):
        return self._set_property(self.AWSServiceName.__name__, value)

    def CustomSuffix(self, value: str):
        return self._set_property(self.CustomSuffix.__name__, value)

    def Description(self, value: str):
        return self._set_property(self.Description.__name__, value)