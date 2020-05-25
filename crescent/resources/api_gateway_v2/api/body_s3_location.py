from crescent.core import Model


class BodyS3Location(Model):
    def __init__(self):
        super(BodyS3Location, self).__init__()

    def Bucket(self, bucket: str):
        return self._set_field(self.Bucket.__name__, bucket)

    def Etag(self, etag: str):
        return self._set_field(self.Etag.__name__, etag)

    def Key(self, key: str):
        return self._set_field(self.Key.__name__, key)

    def Version(self, version: str):
        return self._set_field(self.Version.__name__, version)