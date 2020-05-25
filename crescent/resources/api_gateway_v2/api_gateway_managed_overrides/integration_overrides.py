from crescent.core import Model


class IntegrationOverrides(Model):
    def __init__(self):
        super(IntegrationOverrides, self).__init__()

    def Description(self, description: str):
        return self._set_field(self.Description.__name__, description)

    def IntegrationMethod(self, integration_method: str):
        return self._set_field(self.IntegrationMethod.__name__, integration_method)

    def PayloadFormatVersion(self, payload_format_version: str):
        return self._set_field(self.PayloadFormatVersion.__name__, payload_format_version)

    def TimeoutInMillis(self, timeout_in_millis: int):
        return self._set_field(self.TimeoutInMillis.__name__, timeout_in_millis)