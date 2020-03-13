from pyformation.core import Resource, Validator


class EventSubscription(Resource):
    __TYPE = "AWS::RDS::EventSubscription"

    def __init__(self, id: str):
        super(EventSubscription, self).__init__(id, self.__TYPE)

    @Validator.validate(type=bool)
    def Enabled(self, value: bool):
        return self._set_property(self.Enabled.__name__, value)

    @Validator.validate(type=str)
    def EventCategories(self, *value: str):
        return self._set_property(self.EventCategories.__name__, list(value))

    @Validator.validate(type=str)
    def SnsTopicArn(self, value: str):
        return self._set_property(self.SnsTopicArn.__name__, value)

    @Validator.validate(type=str)
    def SourceIds(self, *value: str):
        return self._set_property(self.SourceIds.__name__, list(value))

    @Validator.validate(type=str)
    def SourceType(self, value: str):
        return self._set_property(self.SourceType.__name__, value)
