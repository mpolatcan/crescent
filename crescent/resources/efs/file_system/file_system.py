from crescent.core import Resource, Validator
from .lifecycle_policy import LifecyclePolicy
from .efs_tag import ElasticFileSystemTag
from .constants import AllowedValues, ModelRequiredProperties


class FileSystem(Resource):
    __TYPE = "AWS::EFS::FileSystem"

    def __init__(self, id: str):
        super(FileSystem, self).__init__(id, self.__TYPE)

    @Validator.validate(type=bool)
    def Encrypted(self, encrypted: bool):
        return self._set_property(self.Encrypted.__name__, encrypted)

    @Validator.validate(type=ElasticFileSystemTag)
    def FileSystemTags(self, *tags: ElasticFileSystemTag):
        return self._set_property(self.FileSystemTags.__name__, list(tags))

    @Validator.validate(type=str, min_length=1, max_length=2048)
    def KmsKeyId(self, kms_key_id: str):
        return self._set_property(self.KmsKeyId.__name__, kms_key_id)

    @Validator.validate(type=LifecyclePolicy, required_properties=ModelRequiredProperties.LIFECYCLE_POLICY)
    def LifecyclePolicies(self, *lifecycle_policies: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicies.__name__, [lp.__to_dict__() for lp in list(lifecycle_policies)])

    @Validator.validate(type=str, allowed_values=AllowedValues.PERFORMANCE_MODE)
    def PerformanceMode(self, performance_mode: str):
        return self._set_property(self.PerformanceMode.__name__, performance_mode)

    @Validator.validate(type=float)
    def ProvisionedThroughputInMibps(self, provisioned_throughput_in_mibs: float):
        return self._set_property(self.ProvisionedThroughputInMibps.__name__, provisioned_throughput_in_mibs)

    @Validator.validate(type=str, allowed_values=AllowedValues.THROUGHPUT_MODE)
    def ThroughputMode(self, throughtput_mode: str):
        return self._set_property(self.ThroughputMode.__name__, throughtput_mode)
