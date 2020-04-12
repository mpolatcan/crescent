from crescent.core import Resource
from crescent.functions import AnyFn
from .lifecycle_policy import LifecyclePolicy
from .efs_tag import ElasticFileSystemTag
from .constants import AllowedValues
from typing import Union


class FileSystem(Resource):
    __TYPE = "AWS::EFS::FileSystem"

    def __init__(self, id: str):
        super(FileSystem, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.KmsKeyId.__name__: 1},
            max_length={self.KmsKeyId.__name__: 2048},
            allowed_values={self.PerformanceMode.__name__: AllowedValues.PERFORMANCE_MODE,
                            self.ThroughputMode.__name__: AllowedValues.THROUGHPUT_MODE}
        )

    def Encrypted(self, encrypted: Union[bool, AnyFn]):
        return self._set_property(self.Encrypted.__name__, encrypted)

    def FileSystemTags(self, *tags: ElasticFileSystemTag):
        return self._set_property(self.FileSystemTags.__name__, list(tags))

    def KmsKeyId(self, kms_key_id: Union[str, AnyFn]):
        return self._set_property(self.KmsKeyId.__name__, kms_key_id)

    def LifecyclePolicies(self, *lifecycle_policies: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicies.__name__, list(lifecycle_policies))

    def PerformanceMode(self, performance_mode: Union[str, AnyFn]):
        return self._set_property(self.PerformanceMode.__name__, performance_mode)

    def ProvisionedThroughputInMibps(self, provisioned_throughput_in_mibs: Union[float, AnyFn]):
        return self._set_property(self.ProvisionedThroughputInMibps.__name__, provisioned_throughput_in_mibs)

    def ThroughputMode(self, throughtput_mode: Union[str, AnyFn]):
        return self._set_property(self.ThroughputMode.__name__, throughtput_mode)
