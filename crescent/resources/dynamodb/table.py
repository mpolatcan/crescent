from crescent.core import Resource, Tag
from .attribute_definition import AttributeDefinition
from .global_secondary_index import GlobalSecondaryIndex
from .key_schema import KeySchema
from .local_secondary_index import LocalSecondaryIndex
from .point_in_time_recovery_specification import PointInTimeRecoverySpecification
from .provisioned_throughput import ProvisionedThroughput
from .sse_specification import SSESpecification
from .stream_specification import StreamSpecification
from .time_to_live_specification import TimeToLiveSpecification
from .constants import ModelRequiredProperties, AllowedValues


class Table(Resource):
    __TYPE = "AWS::DynamoDB::Table"

    def __init__(self, id: str):
        super(Table, self).__init__(
            id=id,
            type=self.__TYPE,
            min_length={self.TableName.__name__: 3,},
            max_length={self.TableName.__name__: 255},
            pattern={self.TableName.__name__: r"[a-zA-Z0-9_.-]+"},
            allowed_values={self.BillingMode.__name__: AllowedValues.BILLING_MODE},
            required_properties=ModelRequiredProperties.TABLE
        )

    def AttributeDefinitions(self, *attribute_definitions: AttributeDefinition):
        return self._set_property(self.AttributeDefinitions.__name__, list(attribute_definitions))

    def BillingMode(self, billing_mode: str):
        return self._set_property(self.BillingMode.__name__, billing_mode)

    def GlobalSecondaryIndexes(self, *global_secondary_indexes: GlobalSecondaryIndex):
        return self._set_property(self.GlobalSecondaryIndexes.__name__, list(global_secondary_indexes))

    def KeySchema(self, *key_schemas: KeySchema):
        return self._set_property(self.KeySchema.__name__, list(key_schemas))

    def LocalSecondaryIndexes(self, *local_secondary_indexes: LocalSecondaryIndex):
        return self._set_property(self.LocalSecondaryIndexes.__name__, list(local_secondary_indexes))

    def PointInTimeRecoverySpecification(self, pit_recovery_specification: PointInTimeRecoverySpecification):
        return self._set_property(self.PointInTimeRecoverySpecification.__name__, pit_recovery_specification)

    def ProvisionedThroughput(self, provisioned_throughput: ProvisionedThroughput):
        return self._set_property(self.ProvisionedThroughput.__name__, provisioned_throughput)

    def SSESpecification(self, sse_specification: SSESpecification):
        return self._set_property(self.SSESpecification.__name__, sse_specification)

    def StreamSpecification(self, stream_specification: StreamSpecification):
        return self._set_property(self.StreamSpecification.__name__, stream_specification)

    def TableName(self, table_name: str):
        return self._set_property(self.TableName.__name__, table_name)

    def Tags(self, *tags: Tag):
        return self._set_property(self.Tags.__name__, list(tags))

    def TimeToLiveSpecification(self, ttl_specification: TimeToLiveSpecification):
        return self._set_property(self.TimeToLiveSpecification.__name__, ttl_specification)