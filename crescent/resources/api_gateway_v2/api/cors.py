from crescent.core import Model


class Cors(Model):
    def __int__(self):
        super(Cors, self).__init__()

    def AllowCredentials(self, allow_credentials: bool):
        return self._set_field(self.AllowCredentials.__name__, allow_credentials)

    def AllowHeaders(self, *allow_headers: str):
        return self._set_field(self.AllowHeaders.__name__, list(allow_headers))

    def AllowMethods(self, *allow_methods: str):
        return self._set_field(self.AllowMethods.__name__, list(allow_methods))

    def AllowOrigins(self, *allow_origins: str):
        return self._set_field(self.AllowOrigins.__name__, list(allow_origins))

    def ExposeHeaders(self, *expose_headers: str):
        return self._set_field(self.ExposeHeaders.__name__, list(expose_headers))

    def MaxAge(self, max_age: int):
        return self._set_field(self.MaxAge.__name__, max_age)