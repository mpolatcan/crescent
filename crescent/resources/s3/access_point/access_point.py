from crescent.core import Resource
from crescent.functions import AnyFn
from .public_access_block_configuration import PublicAccessBlockConfiguration
from .vpc_configuration import VpcConfiguration
from .constants import ResourceRequiredProperties
from typing import Union


class AccessPoint(Resource):
    __TYPE = "AWS::S3::AccessPoint"

    def __init__(self, id: str):
        super(AccessPoint, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.ACCESS_POINT
        )

    def Bucket(self, bucket: Union[str, AnyFn]):
        return self._set_property(self.Bucket.__name__, bucket)

    def CreationDate(self, creation_date: Union[str, AnyFn]):
        return self._set_property(self.CreationDate.__name__, creation_date)

    def Name(self, name: Union[str, AnyFn]):
        return self._set_property(self.Name.__name__, name)

    def NetworkOrigin(self, network_origin: Union[str, AnyFn]):
        return self._set_property(self.NetworkOrigin.__name__, network_origin)

    def Policy(self, policy: Union[dict, AnyFn]):
        return self._set_property(self.Policy.__name__, policy)

    def PolicyStatus(self, policy_status: Union[dict, AnyFn]):
        return self._set_property(self.PolicyStatus, policy_status)

    def PublicAccessBlockConfiguration(self, public_access_block_conf: PublicAccessBlockConfiguration):
        return self._set_property(self.PublicAccessBlockConfiguration.__name__, public_access_block_conf)

    def VpcConfiguration(self, vpc_conf: VpcConfiguration):
        return self._set_property(self.VpcConfiguration.__name__, vpc_conf)
