from .db_cluster_pg import DBClusterParameterGroup
from .constants import DBClusterParameterGroupEngineFamily


class DBClusterParameterGroupFactory:
    EngineFamily = DBClusterParameterGroupEngineFamily

    @staticmethod
    def Create(id: str): return DBClusterParameterGroup(id)


__all__ = ["DBClusterParameterGroupFactory"]
