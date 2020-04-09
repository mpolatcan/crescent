from .fn import FnArrayValue


class GetAtt(FnArrayValue):
    def __init__(self):
        super(GetAtt, self).__init__(
            fn_name=GetAtt.__name__,
            field_order=[self.Resource.__name__, self.Attribute.__name__]
        )

    def Resource(self, resource_id: str):
        return self._set_field(self.Resource.__name__, resource_id)

    def Attribute(self, attribute: str):
        return self._set_field(self.Attribute.__name__, attribute)
