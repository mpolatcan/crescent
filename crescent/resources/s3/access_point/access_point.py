from crescent.core import Resource, Validator
from .public_access_block_configuration import PublicAccessBlockConfiguration
from .vpc_configuration import VpcConfiguration


class AccessPoint(Resource):
    __TYPE = "AWS::S3::AccessPoint"

    def __init__(self, id: str):
        super(AccessPoint, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Bucket(self, value: str):
        return self._set_property(self.Bucket.__name__, value)

    @Validator.validate(type=str)
    def CreationDate(self, value: str):
        return self._set_property(self.CreationDate.__name__, value)

    @Validator.validate(type=str)
    def Name(self, value: str):
        return self._set_property(self.Name.__name__, value)

    @Validator.validate(type=str)
    def NetworkOrigin(self, value: str):
        return self._set_property(self.NetworkOrigin.__name__, value)

    @Validator.validate(type=dict)
    def Policy(self, value: dict):
        return self._set_property(self.Policy.__name__, value)

    @Validator.validate(type=dict)
    def PolicyStatus(self, value: dict):
        return self._set_property(self.PolicyStatus, value)

    @Validator.validate(type=PublicAccessBlockConfiguration)
    def PublicAccessBlockConfiguration(self, value: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, value.__to_dict__())

    @Validator.validate(type=VpcConfiguration)
    def VpcConfiguration(self, value: VpcConfiguration):
        return self._set_property(self.VpcConfiguration.__name__, value.__to_dict__())
