from crescent.core import Resource


class Deployment(Resource):
    __TYPE = "AWS::ApiGatewayV2::Deployment"

    def __init__(self, id: str):
        super(Deployment, self).__init__(id=id, type=self.__TYPE)

    def ApiId(self, api_id: str):
        return self._set_property(self.ApiId.__name__, api_id)

    def Description(self, description: str):
        return self._set_property(self.Description.__name__, description)

    def StageName(self, stage_name: str):
        return self._set_property(self.StageName.__name__, stage_name)
