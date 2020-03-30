from crescent.core import Resource, Validator


class BucketPolicy(Resource):
    __TYPE = "AWS::S3::BucketPolicy"

    def __init__(self, id: str):
        super(BucketPolicy, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Bucket(self, bucket: str):
        return self._set_property(self.Bucket.__name__, bucket)

    @Validator.validate(type=dict)
    def PolicyDocument(self, policy_document: dict):
        return self._set_property(self.PolicyDocument, policy_document)
