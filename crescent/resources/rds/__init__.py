from .db_cluster import *
from .db_cluster_pg import *
from .db_instance import *
from .db_pg import *
from .db_security_group import *
from .db_security_group_ingress import *
from .db_subnet_group import *
from .event_subscription import *
from .option_group import *
from .constants import EngineVersion, EngineFamily


class Rds:
    class DBCluster:
        Engine = DBClusterEngine
        EngineVersion = DBClusterEngineVersion
        EngineMode = EngineMode
        RestoreType = RestoreType
        Capacity = Capacity

        @staticmethod
        def Create(id: str):
            return DBCluster(id)

        @staticmethod
        def DBClusterRole():
            return DBClusterRole()

        @staticmethod
        def ScalingConfiguration():
            return ScalingConfiguration()

    class DBClusterParameterGroup:
        EngineFamily = DBClusterParameterGroupEngineFamily

        @staticmethod
        def Create(id: str):
            return DBClusterParameterGroup(id)

    class DBInstance:
        Engine = DBInstanceEngine
        EngineVersion = EngineVersion
        DBInstanceClass = DBInstanceClass
        MonitoringInterval = MonitoringInterval
        StorageType = StorageType

        @staticmethod
        def Create(id: str):
            return DBInstance(id)

        @staticmethod
        def DBInstanceRole():
            return DBInstanceRole()

        @staticmethod
        def ProcessorFeature():
            return ProcessorFeature()

    class DBParameterGroup:
        EngineFamily = EngineFamily

        @staticmethod
        def Create(id: str):
            return DBParameterGroup(id)

    class DBSecurityGroup:
        @staticmethod
        def Create(id: str):
            return DBSecurityGroup(id)

        @staticmethod
        def Ingress():
            return Ingress()

    class DBSecurityGroupIngress:
        @staticmethod
        def Create(id: str):
            return DBSecurityGroupIngress(id)

    class DBSubnetGroup:
        @staticmethod
        def Create(id: str):
            return DBSubnetGroup(id)

    class OptionGroup:
        @staticmethod
        def Create(id: str):
            return OptionGroup(id)

        @staticmethod
        def OptionConfiguration():
            return OptionConfiguration()

        @staticmethod
        def OptionSetting():
            return OptionSetting()

    class EventSubscription:
        EventCategories = EventCategories
        SourceType = SourceType

        @staticmethod
        def Create(id: str):
            return EventSubscription(id)


__all__ = [
   "Rds"
]
