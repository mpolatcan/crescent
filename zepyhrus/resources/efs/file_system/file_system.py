from zepyhrus.core import Resource, Validator
from .lifecycle_policy import LifecyclePolicy
from .efs_tag import ElasticFileSystemTag
from .constants import AllowedValues, RequiredProperties


class FileSystem(Resource):
    __TYPE = "AWS::EFS::FileSystem"

    def __init__(self, id: str):
        super(FileSystem, self).__init__(id, self.__TYPE)

    @Validator.validate(type=bool)
    def Encrypted(self, value: bool):
        return self._set_property(self.Encrypted.__name__, value)

    @Validator.validate(type=ElasticFileSystemTag)
    def FileSystemTags(self, *value: ElasticFileSystemTag):
        return self._set_property(self.FileSystemTags.__name__, list(value))

    @Validator.validate(type=str, min_length=1, max_length=2048)
    def KmsKeyId(self, value: str):
        return self._set_property(self.KmsKeyId.__name__, value)

    @Validator.validate(type=LifecyclePolicy, required_properties=RequiredProperties.LIFECYCLE_POLICY)
    def LifecyclePolicies(self, *value: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicies.__name__, [lp.__to_dict__() for lp in list(value)])

    @Validator.validate(type=str, allowed_values=AllowedValues.PERFORMANCE_MODE)
    def PerformanceMode(self, value: str):
        return self._set_property(self.PerformanceMode.__name__, value)

    @Validator.validate(type=float)
    def ProvisionedThroughputInMibps(self, value: float):
        return self._set_property(self.ProvisionedThroughputInMibps.__name__, value)

    @Validator.validate(type=str, allowed_values=AllowedValues.THROUGHPUT_MODE)
    def ThroughputMode(self, value: str):
        return self._set_property(self.ThroughputMode.__name__, value)
