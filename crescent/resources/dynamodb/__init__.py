from .table import Table
from .attribute_definition import AttributeDefinition
from .global_secondary_index import GlobalSecondaryIndex
from .key_schema import KeySchema
from .local_secondary_index import LocalSecondaryIndex
from .point_in_time_recovery_specification import PointInTimeRecoverySpecification
from .projection import Projection
from .provisioned_throughput import ProvisionedThroughput
from .sse_specification import SSESpecification
from .stream_specification import StreamSpecification
from .time_to_live_specification import TimeToLiveSpecification
from .constants import *


class DynamoDB:
    class Table:
        BillingMode = BillingMode
        AttributeType = AttributeType
        KeyType = KeyType
        ProjectionType = ProjectionType
        SSEType = SSEType
        StreamViewType = StreamViewType

        @staticmethod
        def Create(id: str): return Table(id)

        @staticmethod
        def AttributeDefinition(): return AttributeDefinition()

        @staticmethod
        def GlobalSecondaryIndex(): return GlobalSecondaryIndex()

        @staticmethod
        def KeySchema(): return KeySchema()

        @staticmethod
        def LocalSecondaryIndex(): return LocalSecondaryIndex()

        @staticmethod
        def PointInTimeRecoverySpecification(): return PointInTimeRecoverySpecification()

        @staticmethod
        def Projection(): return Projection()

        @staticmethod
        def ProvisionedThroughput(): return ProvisionedThroughput()

        @staticmethod
        def SSESpecification(): return SSESpecification()

        @staticmethod
        def StreamSpecification(): return StreamSpecification()

        @staticmethod
        def TimeToLiveSpecification(): return TimeToLiveSpecification()


__all__ = [
    "DynamoDB"
]