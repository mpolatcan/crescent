from .db_instance import DBInstance
from .db_instance_role import DBInstanceRole
from .processor_feature import ProcessorFeature
from .constants import DBInstanceEngine, DBInstanceClass, MonitoringInterval, StorageType
from crescent.resources.rds.constants import EngineVersion


class DBInstanceFactory:
    Engine = DBInstanceEngine
    EngineVersion = EngineVersion
    DBInstanceClass = DBInstanceClass
    MonitoringInterval = MonitoringInterval
    StorageType = StorageType

    @staticmethod
    def Create(id: str): return DBInstance(id)

    @staticmethod
    def DBInstanceRole(): return DBInstanceRole()

    @staticmethod
    def ProcessorFeature(): return ProcessorFeature()


__all__ = ["DBInstanceFactory"]
