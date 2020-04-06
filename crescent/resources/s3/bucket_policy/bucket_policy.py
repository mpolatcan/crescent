from crescent.core import Resource
from .constants import ResourceRequiredProperties


class BucketPolicy(Resource):
    __TYPE = "AWS::S3::BucketPolicy"

    def __init__(self, id: str):
        super(BucketPolicy, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.BUCKET_POLICY
        )

    def Bucket(self, bucket: str):
        return self._set_property(self.Bucket.__name__, bucket)

    def PolicyDocument(self, policy_document: dict):
        return self._set_property(self.PolicyDocument, policy_document)
