from typing import List
from resources.shared import BaseCloudFormationResourceModel


class EventSubscription(BaseCloudFormationResourceModel):
    __TYPE = "AWS::RDS::EventSubscription"
    __PROPERTY_ENABLED = "Enabled"
    __PROPERTY_EVENT_CATEGORIES = "EventCategories"
    __PROPERTY_SNS_TOPIC_ARN = "SnsTopicArn"
    __PROPERTY_SOURCE_IDS = "SourceIds"
    __PROPERTY_SOURCE_TYPE = "SourceType"

    def __init__(self):
        super(EventSubscription, self).__init__(type=self.__TYPE)

    def enabled(self, value: bool):
        return self._add_property_field(self.__PROPERTY_ENABLED, value)

    def event_categories(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_EVENT_CATEGORIES, value)

    def sns_topic_arn(self, value: str):
        return self._add_property_field(self.__PROPERTY_SNS_TOPIC_ARN, value)

    def source_ids(self, value: List[str]):
        return self._add_property_field(self.__PROPERTY_SOURCE_IDS, value)

    def source_type(self, value: str):
        return self._add_property_field(self.__PROPERTY_SOURCE_TYPE, value)
