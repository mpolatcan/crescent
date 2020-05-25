from crescent.core import Resource
from .constants import ResourceRequiredProperties


class Model(Resource):
    __TYPE = "AWS::ApiGatewayV2::Model"

    def __init__(self, id: str):
        super(Model, self).__init__(
            id=id,
            type=self.__TYPE,
            required_properties=ResourceRequiredProperties.MODEL
        )

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def ContentType(self, content_type: str):
        return self._set_property(self.ContentType.__name__, content_type)

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def Name(self, name: str):
        return self._set_property(self.Name.__name__, name)

    def Schema(self, schema: dict):
        return self._set_property(self.Schema.__name__, schema)