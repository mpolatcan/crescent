from pyformation import PyformationResource
from .public_access_block_configuration import PublicAccessBlockConfiguration
from .vpc_configuration import VpcConfiguration


class AccessPoint(PyformationResource):
    __TYPE = "AWS::S3::AccessPoint"

    def __init__(self, id: str):
        super(AccessPoint, self).__init__(id, self.__TYPE)

    def Bucket(self, value: str):
        return self._set_property(self.Bucket.__name__, value)

    def CreationDate(self, value: str):
        return self._set_property(self.CreationDate.__name__, value)

    def Name(self, value: str):
        return self._set_property(self.Name.__name__, value)

    def NetworkOrigin(self, value: str):
        return self._set_property(self.NetworkOrigin.__name__, value)

    def Policy(self, value: dict):
        return self._set_property(self.Policy.__name__, value)

    def PolicyStatus(self, value: dict):
        return self._set_property(self.PolicyStatus, value)

    def PublicAccessBlockConfiguration(self, value: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, value.__to_dict__())

    def VpcConfiguration(self, value: VpcConfiguration):
        return self._set_property(self.VpcConfiguration.__name__, value.__to_dict__())
