from pyformation import PyformationResource


class BucketPolicy(PyformationResource):
    __TYPE = "AWS::S3::BucketPolicy"

    def __init__(self, id: str):
        super(BucketPolicy, self).__init__(id, self.__TYPE)

    def Bucket(self, value: str):
        return self._set_property(self.Bucket.__name__, value)

    def PolicyDocument(self, value: dict):
        return self._set_property(self.PolicyDocument, value)
