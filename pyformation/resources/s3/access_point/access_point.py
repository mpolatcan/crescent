from pyformation.resources.shared import BaseCloudFormationResourceModel
from pyformation.resources.s3.bucket import PublicAccessBlockConfiguration
from pyformation.resources.s3.access_point import VpcConfiguration


class AccessPoint(BaseCloudFormationResourceModel):
    __TYPE = "AWS::S3::AccessPoint"
    __PROPERTY_BUCKET = "Bucket"
    __PROPERTY_CREATION_DATE = "CreationDate"
    __PROPERTY_NAME = "Name"
    __PROPERTY_NETWORK_ORIGIN = "NetworkOrigin"
    __PROPERTY_POLICY = "Policy"
    __PROPERTY_POLICY_STATUS = "PolicyStatus"
    __PROPERTY_PUBLIC_ACCESS_BLOCK_CONFIGURATION = "PublicAccessBlockConfiguration"
    __PROPERTY_VPC_CONFIGURATION = "VpcConfiguration"

    def __init__(self):
        super(AccessPoint, self).__init__(type=self.__TYPE)

    def bucket(self, value: str):
        return self._add_property_field(self.__PROPERTY_BUCKET, value)

    def creation_date(self, value: str):
        return self._add_property_field(self.__PROPERTY_CREATION_DATE, value)

    def name(self, value: str):
        return self._add_property_field(self.__PROPERTY_NAME, value)

    def network_origin(self, value: str):
        return self._add_property_field(self.__PROPERTY_NETWORK_ORIGIN, value)

    def policy(self, value: dict):
        return self._add_property_field(self.__PROPERTY_POLICY, value)

    def policy_status(self, value: dict):
        return self._add_property_field(self.__PROPERTY_POLICY_STATUS, value)

    def public_access_block_configuration(self, value: PublicAccessBlockConfiguration):
        return self._add_property_field(self.__PROPERTY_PUBLIC_ACCESS_BLOCK_CONFIGURATION, value.create())

    def vpc_configuration(self, value: VpcConfiguration):
        return self._add_property_field(self.__PROPERTY_VPC_CONFIGURATION, value.create())
