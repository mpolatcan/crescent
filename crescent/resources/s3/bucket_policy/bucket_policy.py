from crescent.core import Resource, Validator


class BucketPolicy(Resource):
    __TYPE = "AWS::S3::BucketPolicy"

    def __init__(self, id: str):
        super(BucketPolicy, self).__init__(id, self.__TYPE)

    @Validator.validate(type=str)
    def Bucket(self, value: str):
        return self._set_property(self.Bucket.__name__, value)

    @Validator.validate(type=dict)
    def PolicyDocument(self, value: dict):
        return self._set_property(self.PolicyDocument, value)
