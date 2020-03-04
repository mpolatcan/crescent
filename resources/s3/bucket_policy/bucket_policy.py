from resources.shared.base_cf_resource_model import BaseCloudFormationResourceModel


class BucketPolicy(BaseCloudFormationResourceModel):
    __TYPE = "AWS::S3::BucketPolicy"
    __PROPERTY_BUCKET = "Bucket"
    __PROPERTY_POLICY_DOCUMENT = "PolicyDocument"

    def __init__(self):
        super(BucketPolicy, self).__init__(type=self.__TYPE)

    def bucket(self, value: str):
        return self._add_property_field(self.__PROPERTY_BUCKET, value)

    def policy_document(self, value: dict):
        return self._add_property_field(self.__PROPERTY_POLICY_DOCUMENT, value)
