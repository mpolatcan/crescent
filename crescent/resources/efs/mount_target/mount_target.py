from crescent.core import Resource
from crescent.functions import AnyFn
from .constants import ResourceRequiredProperties
from typing import Union


class MountTarget(Resource):
    __TYPE = "AWS::EFS::MountTarget"

    def __init__(self, id: str):
        super(MountTarget, self).__init__(
            id=id,
            type=self.__TYPE,
            max_length={self.SecurityGroups.__name__: 5},
            required_properties=ResourceRequiredProperties.MOUNT_TARGET
        )

    def FileSystemId(self, file_system_id: Union[str, AnyFn]):
        return self._set_property(self.FileSystemId.__name__, file_system_id)

    def IpAddress(self, ip_address: Union[str, AnyFn]):
        return self._set_property(self.IpAddress.__name__, ip_address)

    def SecurityGroups(self, *security_groups: Union[str, AnyFn]):
        return self._set_property(self.SecurityGroups.__name__, list(security_groups))

    def SubnetId(self, subnet_id: Union[str, AnyFn]):
        return self._set_property(self.SubnetId.__name__, subnet_id)
