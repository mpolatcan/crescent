from crescent.core import Model


class JWTConfiguration(Model):
    def __init__(self):
        super(JWTConfiguration, self).__init__()

    def Audience(self, *audience: str):
        return self._set_field(self.Audience.__name__, list(audience))

    def Issuer(self, issuer: str):
        return self._set_field(self.Issuer.__name__, issuer)



