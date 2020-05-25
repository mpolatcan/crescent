from crescent.resources.rds.constants import EngineFamily
from .db_pg import DBParameterGroup


class DBParameterGroupFactory:
    EngineFamily = EngineFamily

    @staticmethod
    def Create(id: str): return DBParameterGroup(id)


__all__ = ["DBParameterGroupFactory"]
