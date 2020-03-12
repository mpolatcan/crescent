from pyformation import PyformationResource
from .lifecycle_policy import LifecyclePolicy
from .efs_tag import ElasticFileSystemTag


class FileSystem(PyformationResource):
    __TYPE = "AWS::EFS::FileSystem"

    def __init__(self, id: str):
        super(FileSystem, self).__init__(id, self.__TYPE)

    def Encrypted(self, value: bool):
        return self._set_property(self.Encrypted.__name__, value)

    def FileSystemTags(self, *value: ElasticFileSystemTag):
        return self._set_property(self.FileSystemTags.__name__, list(value))

    def KmsKeyId(self, value: str):
        return self._set_property(self.KmsKeyId.__name__, value)

    def LifecyclePolicies(self, *value: LifecyclePolicy):
        return self._set_property(self.LifecyclePolicies.__name__, [lp.__to_dict__() for lp in list(value)])

    def PerformanceMode(self, value: str):
        return self._set_property(self.PerformanceMode.__name__, value)

    def ProvisionedThroughputInMibps(self, value: float):
        return self._set_property(self.ProvisionedThroughputInMibps.__name__, value)

    def ThroughputMode(self, value: str):
        return self._set_property(self.ThroughputMode.__name__, value)
