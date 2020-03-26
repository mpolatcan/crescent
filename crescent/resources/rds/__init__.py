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


class Rds:
    class Cluster:
        Engine = Engine
        EngineVersion = EngineVersion
        EngineMode = EngineMode
        RestoreType = RestoreType
        Capacity = Capacity

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

    class Instance:
        EngineVersion = EngineVersion
        DBInstanceClass = DBInstanceClass

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

    class SecurityGroup:
        @staticmethod
        def DBSecurityGroup(id: str):
            return DBSecurityGroup(id)

        @staticmethod
        def DBSecurityGroupIngress(id: str):
            return DBSecurityGroupIngress(id)

        @staticmethod
        def Ingress():
            return Ingress()

    class OptionGroup:
        @staticmethod
        def OptionGroup(id: str):
            return OptionGroup(id)

        @staticmethod
        def OptionConfiguration():
            return OptionConfiguration()

        @staticmethod
        def OptionSetting():
            return OptionSetting()

    class SubnetGroup:
        @staticmethod
        def DBSubnetGroup(id: str):
            return DBSubnetGroup(id)

    class EventSubscription:
        SourceType = SourceType

        @staticmethod
        def EventSubscription(id: str):
            return EventSubscription(id)


__all__ = [
   "Rds"
]
