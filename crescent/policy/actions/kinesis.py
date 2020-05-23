from crescent.resources.kinesis import StreamArn, StreamConsumerArn
from .action import Action, AccessLevelAllActions
from typing import Union


class KinesisAction(Action):
    __SERVICE_KINESIS = "kinesis"

    def __init__(self, action_name, **definable_resources):
        super(KinesisAction, self).__init__(self.__SERVICE_KINESIS, action_name, **definable_resources)

    def Stream(self, stream: Union[str, StreamArn]):
        return self._set_resource(self.Stream.__name__, stream)

    def Consumer(self, consumer: Union[str, StreamConsumerArn]):
        return self._set_resource(self.Consumer.__name__, consumer)


# -----------------------------------------------

class KinesisAccessLevelAllActions(AccessLevelAllActions):
    def __init__(self, access_level):
        super(KinesisAccessLevelAllActions, self).__init__(access_level)

    def Stream(self, stream: Union[str, StreamArn]):
        return self._set_all_actions_resources(self.Stream.__name__, stream)

    def Consumer(self, consumer: Union[str, StreamConsumerArn]):
        return self._set_all_actions_resources(self.Consumer.__name__, consumer)


# -----------------------------------------------


class Actions:
    class Tagging:
        @staticmethod
        def AddTagsToStream(): return KinesisAction(Actions.Tagging.AddTagsToStream.__name__,
                                                    required=[KinesisAction.Stream.__name__])

        @staticmethod
        def RemoveTagsFromStream(): return KinesisAction(Actions.Tagging.RemoveTagsFromStream.__name__,
                                                         required=[KinesisAction.Stream.__name__])

    class Write:
        @staticmethod
        def CreateStream(): return KinesisAction(Actions.Write.CreateStream.__name__,
                                                 required=[KinesisAction.Stream.__name__])

        @staticmethod
        def DecreaseStreamRetentionPeriod(): return KinesisAction(Actions.Write.DecreaseStreamRetentionPeriod.__name__,
                                                                  required=[KinesisAction.Stream.__name__])

        @staticmethod
        def DeleteStream(): return KinesisAction(Actions.Write.DeleteStream.__name__,
                                                 required=[KinesisAction.Stream.__name__])

        @staticmethod
        def DeregisterStreamConsumer(): return KinesisAction(Actions.Write.DeregisterStreamConsumer.__name__,
                                                             required=[KinesisAction.Consumer.__name__])

        @staticmethod
        def DisableEnhancedMonitoring(): return KinesisAction(Actions.Write.DisableEnhancedMonitoring.__name__)

        @staticmethod
        def EnableEnhancedMonitoring(): return KinesisAction(Actions.Write.EnableEnhancedMonitoring.__name__)

        @staticmethod
        def IncreaseStreamRetentionPeriod(): return KinesisAction(Actions.Write.IncreaseStreamRetentionPeriod.__name__,
                                                                  required=[KinesisAction.Stream.__name__])

        @staticmethod
        def MergeShards(): return KinesisAction(Actions.Write.MergeShards.__name__,
                                                required=[KinesisAction.Stream.__name__])

        @staticmethod
        def PutRecord(): return KinesisAction(Actions.Write.PutRecord.__name__,
                                              required=[KinesisAction.Stream.__name__])

        @staticmethod
        def PutRecords(): return KinesisAction(Actions.Write.PutRecords.__name__,
                                               required=[KinesisAction.Stream.__name__])

        @staticmethod
        def RegisterStreamConsumer(): return KinesisAction(Actions.Write.RegisterStreamConsumer.__name__,
                                                           required=[KinesisAction.Consumer.__name__])

        @staticmethod
        def SplitShard(): return KinesisAction(Actions.Write.SplitShard.__name__,
                                               required=[KinesisAction.Stream.__name__])

        @staticmethod
        def UpdateShardCount(): return KinesisAction(Actions.Write.UpdateShardCount.__name__)

    class Read:
        @staticmethod
        def DescribeLimits(): return KinesisAction(Actions.Read.DescribeLimits.__name__)

        @staticmethod
        def DescribeStream(): return KinesisAction(Actions.Read.DescribeStream.__name__,
                                                   required=[KinesisAction.Stream.__name__])

        @staticmethod
        def DescribeStreamConsumer(): return KinesisAction(Actions.Read.DescribeStreamConsumer.__name__,
                                                           required=[KinesisAction.Consumer.__name__])

        @staticmethod
        def DescribeStreamSummary(): return KinesisAction(Actions.Read.DescribeStreamSummary.__name__,
                                                          required=[KinesisAction.Stream.__name__])

        @staticmethod
        def GetRecords(): return KinesisAction(Actions.Read.GetRecords.__name__,
                                               required=[KinesisAction.Stream.__name__])

        @staticmethod
        def GetShardIterator(): return KinesisAction(Actions.Read.GetShardIterator.__name__,
                                                     required=[KinesisAction.Stream.__name__])

        @staticmethod
        def ListTagsForStream(): return KinesisAction(Actions.Read.ListTagsForStream.__name__,
                                                      required=[KinesisAction.Stream.__name__])

        @staticmethod
        def UpdateShardCount(): return KinesisAction(Actions.Write.UpdateShardCount.__name__)

    class List:
        @staticmethod
        def ListShards(): return KinesisAction(Actions.List.ListShards.__name__)

        @staticmethod
        def ListStreamConsumers(): return KinesisAction(Actions.List.ListStreamConsumers.__name__)

        @staticmethod
        def ListStreams(): return KinesisAction(Actions.List.ListStreams.__name__)

    @staticmethod
    def TaggingAll(): return KinesisAccessLevelAllActions(Actions.Tagging)

    @staticmethod
    def WriteAll(): return KinesisAccessLevelAllActions(Actions.Write)

    @staticmethod
    def ReadAll(): return KinesisAccessLevelAllActions(Actions.Read)

    @staticmethod
    def ListAll(): return KinesisAccessLevelAllActions(Actions.List)

    All = "kinesis:*"
