from crescent.core import Resource, Validator
from .constants import AllowedValues, Conditions


class EventSubscription(Resource):
    __TYPE = "AWS::RDS::EventSubscription"

    def __init__(self, id: str):
        super(EventSubscription, self).__init__(id, self.__TYPE)

    @Validator.validate(type=bool)
    def Enabled(self, enabled: bool):
        return self._set_property(self.Enabled.__name__, enabled)

    @Validator.validate(type=str, conditions=Conditions.EVENT_CATEGORIES)
    def EventCategories(self, *event_categories: str):
        return self._set_property(self.EventCategories.__name__, list(event_categories))

    @Validator.validate(type=str)
    def SnsTopicArn(self, sns_topic_arn: str):
        return self._set_property(self.SnsTopicArn.__name__, sns_topic_arn)

    @Validator.validate(type=str, conditions=Conditions.SOURCE_IDS)
    def SourceIds(self, *source_ids: str):
        return self._set_property(self.SourceIds.__name__, list(source_ids))

    @Validator.validate(type=str, allowed_values=AllowedValues.SOURCE_TYPE)
    def SourceType(self, source_type: str):
        return self._set_property(self.SourceType.__name__, source_type)
