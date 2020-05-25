from crescent.core import Model


class DomainNameConfiguration(Model):
    def __init__(self):
        super(DomainNameConfiguration, self).__init__()

    def CertificateArn(self, certificate_arn: str):
        return self._set_field(self.CertificateArn.__name__, certificate_arn)

    def CertificateName(self, certificate_name: str):
        return self._set_field(self.CertificateName.__name__, certificate_name)

    def EndpointType(self, endpoint_type: str):
        return self._set_field(self.EndpointType.__name__, endpoint_type)

