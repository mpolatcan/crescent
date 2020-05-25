from crescent.core import Model


class RouteOverrides(Model):
    def __init__(self):
        super(RouteOverrides, self).__init__()

    def AuthorizationScopes(self, *authorization_scopes: str):
        return self._set_field(self.AuthorizationScopes.__name__, list(authorization_scopes))

    def AuthorizationType(self, authorization_type: str):
        return self._set_field(self.AuthorizationType.__name__, authorization_type)

    def AuthorizerId(self, authorizer_id: str):
        return self._set_field(self.AuthorizerId.__name__, authorizer_id)

    def OperationName(self, operation_name: str):
        return self._set_field(self.OperationName.__name__, operation_name)

    def Target(self, target: str):
        return self._set_field(self.Target.__name__, target)