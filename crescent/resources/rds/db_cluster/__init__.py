from .db_cluster import DBCluster
from .db_cluster_role import DBClusterRole
from .scaling_configuration import ScalingConfiguration
from .constants import DBClusterEngine, DBClusterEngineVersion, EngineMode, RestoreType, Capacity


class DBClusterFactory:
    Engine = DBClusterEngine
    EngineVersion = DBClusterEngineVersion
    EngineMode = EngineMode
    RestoreType = RestoreType
    Capacity = Capacity

    @staticmethod
    def Create(id: str): return DBCluster(id)

    @staticmethod
    def DBClusterRole(): return DBClusterRole()

    @staticmethod
    def ScalingConfiguration(): return ScalingConfiguration()


__all__ = ["DBClusterFactory"]
