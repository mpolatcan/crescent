from .db_cluster import (
    DBCluster,
    DBClusterRole,
    ScalingConfiguration,
    Engine,
    EngineMode,
    RestoreType,
    Capacity
)
from .db_cluster_pg import DBClusterParameterGroup
from .db_instance import DBInstance, DBInstanceRole, ProcessorFeature
from .db_pg import DBParameterGroup
from .db_security_group import DBSecurityGroup, Ingress
from .db_security_group_ingress import DBSecurityGroupIngress
from .db_subnet_group import DBSubnetGroup
from .event_subscription import EventSubscription
from .option_group import OptionGroup, OptionConfiguration, OptionSetting


class RdsFactory:
    class __ClusterFactory:
        engine = Engine
        engine_mode = EngineMode
        restore_type = RestoreType
        capacity = Capacity

        @staticmethod
        def DBCluster(id: str):
            return DBCluster(id)

        @staticmethod
        def DBClusterParameterGroup(id: str):
            return DBClusterParameterGroup(id)

        @staticmethod
        def DBClusterRole():
            return DBClusterRole()

        @staticmethod
        def ScalingConfiguration():
            return ScalingConfiguration()

    class __InstanceFactory:
        @staticmethod
        def DBInstance(id: str):
            return DBInstance(id)

        @staticmethod
        def DBParameterGroup(id: str):
            return DBParameterGroup(id)

        @staticmethod
        def DBInstanceRole():
            return DBInstanceRole()

        @staticmethod
        def ProcessorFeature():
            return ProcessorFeature()

    class __SecurityGroupFactory:
        @staticmethod
        def DBSecurityGroup(id: str):
            return DBSecurityGroup(id)

        @staticmethod
        def DBSecurityGroupIngress(id: str):
            return DBSecurityGroupIngress(id)

        @staticmethod
        def Ingress():
            return Ingress()

    class __OptionGroupFactory:
        @staticmethod
        def OptionGroup(id: str):
            return OptionGroup(id)

        @staticmethod
        def OptionConfiguration():
            return OptionConfiguration()

        @staticmethod
        def OptionSetting():
            return OptionSetting()

    class __SubnetGroupFactory:
        @staticmethod
        def DBSubnetGroup(id: str):
            return DBSubnetGroup(id)

    class __EventSubscriptionFactory:
        @staticmethod
        def EventSubscription(id: str):
            return EventSubscription(id)

    cluster = __ClusterFactory
    instance = __InstanceFactory
    security_group = __SecurityGroupFactory
    option_group = __OptionGroupFactory
    subnet_group = __SubnetGroupFactory
    event_subscription = __EventSubscriptionFactory


__all__ = [
    "RdsFactory"
]
