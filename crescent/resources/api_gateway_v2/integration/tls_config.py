from crescent.core import Model


class TlsConfig(Model):
    def __init__(self):
        super(TlsConfig, self).__init__()

    def ServerNameToVerify(self, server_name_to_verify: str):
        return self._set_field(self.ServerNameToVerify.__name__, server_name_to_verify)
