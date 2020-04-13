from crescent.resources.firehose import DeliveryStreamArn
from .action import Action, AccessLevelAllActions
from typing import Union


class FirehoseAction(Action):
    __SERVICE_FIREHOSE = "firehose"

    def __init__(self, action_name, required_resource=None):
        super(FirehoseAction, self).__init__(self.__SERVICE_FIREHOSE, action_name, required_resource)

    def DeliveryStream(self, delivery_stream: Union[str, DeliveryStreamArn]):
        return self._set_resource(self.DeliveryStream.__name__, delivery_stream)


# ---------------------------

class FirehoseAccessLevelAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(FirehoseAccessLevelAllActions, self).__init__(access_level)

    def DeliveryStream(self, delivery_stream: Union[str, DeliveryStreamArn]):
        return [action.DeliveryStream(delivery_stream) for action in self._actions]


# ---------------------------


class Actions:
    class Write:
        @staticmethod
        def CreateDeliveryStream(): return FirehoseAction(Actions.Write.CreateDeliveryStream.__name__,
                                                          FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def DeleteDeliveryStream(): return FirehoseAction(Actions.Write.DeleteDeliveryStream.__name__,
                                                          FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def PutRecord(): return FirehoseAction(Actions.Write.PutRecord.__name__,
                                               FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def PutRecordBatch(): return FirehoseAction(Actions.Write.PutRecordBatch.__name__,
                                                    FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def StartDeliveryStreamEncryption(): return FirehoseAction(Actions.Write.StartDeliveryStreamEncryption.__name__,
                                                                   FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def StopDeliveryStreamEncryption(): return FirehoseAction(Actions.Write.StopDeliveryStreamEncryption.__name__,
                                                                  FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def TagDeliveryStream(): return FirehoseAction(Actions.Write.TagDeliveryStream.__name__,
                                                       FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def UntagDeliveryStream(): return FirehoseAction(Actions.Write.UntagDeliveryStream.__name__,
                                                         FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def UpdateDestination(): return FirehoseAction(Actions.Write.UpdateDestination.__name__,
                                                       FirehoseAction.DeliveryStream.__name__)

    class List:
        @staticmethod
        def DescribeDeliveryStream(): return FirehoseAction(Actions.List.DescribeDeliveryStream.__name__,
                                                            FirehoseAction.DeliveryStream.__name__)

        @staticmethod
        def ListDeliveryStreams(): return FirehoseAction(Actions.List.ListDeliveryStreams.__name__)

        @staticmethod
        def ListTagsForDeliveryStream(): return FirehoseAction(Actions.List.ListTagsForDeliveryStream.__name__,
                                                               FirehoseAction.DeliveryStream.__name__)

    @staticmethod
    def WriteAll(): return FirehoseAccessLevelAllActions(Actions.Write)

    @staticmethod
    def ListAll(): return FirehoseAccessLevelAllActions(Actions.List)
