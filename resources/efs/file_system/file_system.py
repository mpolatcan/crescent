from typing import List
from resources.shared import BaseCloudFormationResourceModel
from resources.efs.file_system.efs_tag import ElasticFileSystemTag
from resources.efs.file_system.lifecycle_policy import LifecyclePolicy


class FileSystem(BaseCloudFormationResourceModel):
    __TYPE = "AWS::EFS::FileSystem"
    __PROPERTY_ENCRYPTED = "Encrypted"
    __PROPERTY_FILE_SYSTEM_TAGS = "FileSystemTags"
    __PROPERTY_KMS_KEY_ID = "KmsKeyId"
    __PROPERTY_LIFECYCLE_POLICIES = "LifecyclePolicies"
    __PROPERTY_PERFORMANCE_MODE = "PerformanceMode"
    __PROPERTY_PROVISIONED_THROUGHPUT_IN_MIBPS = "ProvisionedThroughputInMibps"
    __PROPERTY_THROUGHPUT_MODE = "ThroughputMode"

    def encrypted(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ENCRYPTED, value)

    def file_system_tags(self, value: List[ElasticFileSystemTag]):
        return self._add_property_field(self.__PROPERTY_FILE_SYSTEM_TAGS, [
            efs_tag.create() for efs_tag in value
        ])

    def kms_key_id(self, value: str):
        return self._add_property_field(self.__PROPERTY_KMS_KEY_ID, value)

    def lifecycle_policies(self, value: LifecyclePolicy):
        return self._add_property_field(self.__PROPERTY_LIFECYCLE_POLICIES, value.create())

    def performance_mode(self, value: str):
        return self._add_property_field(self.__PROPERTY_PERFORMANCE_MODE, value)

    def provisioned_throughput_in_mibps(self, value: float):
        return self._add_property_field(self.__PROPERTY_PROVISIONED_THROUGHPUT_IN_MIBPS, value)

    def throughput_mode(self, value: str):
        return self._add_property_field(self.__PROPERTY_THROUGHPUT_MODE, value)
