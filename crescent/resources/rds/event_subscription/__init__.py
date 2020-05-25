from .event_subscription import EventSubscription
from .constants import EventCategories, SourceType


class EventSubscriptionFactory:
    EventCategories = EventCategories
    SourceType = SourceType

    @staticmethod
    def Create(id: str): return EventSubscription(id)


__all__ = ["EventSubscriptionFactory"]
