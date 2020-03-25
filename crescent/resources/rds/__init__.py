from .db_cluster import *
from .db_cluster_pg import *
from .db_instance import *
from .db_pg import *
from .db_security_group import *
from .db_security_group_ingress import *
from .db_subnet_group import *
from .event_subscription import *
from .option_group import *
from .constants import EngineVersion


class RdsFactory:
    class __ClusterFactory:
        engine = Engine
        engine_version = EngineVersion
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
        engine_version = EngineVersion

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
        source_type = SourceType

        @staticmethod
        def EventSubscription(id: str):
            return EventSubscription(id)

    cluster = __ClusterFactory
    instance = __InstanceFactory
    security_group = __SecurityGroupFactory
    option_group = __OptionGroupFactory
    subnet_group = __SubnetGroupFactory
    event_subscription = __EventSubscriptionFactory


rds = RdsFactory
rds_cluster = rds.cluster
rds_instance = rds.instance
rds_security_group = rds.security_group
rds_option_group = rds.option_group
rds_subnet_group = rds.subnet_group
rds_event_subscription = rds.event_subscription


__all__ = [
    "rds",
    "rds_cluster",
    "rds_instance",
    "rds_security_group",
    "rds_option_group",
    "rds_subnet_group",
    "rds_event_subscription"
]
