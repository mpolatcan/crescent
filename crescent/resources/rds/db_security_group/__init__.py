from .db_security_group import DBSecurityGroup
from .ingress import Ingress


class DBSecurityGroupFactory:
    @staticmethod
    def Create(id: str): return DBSecurityGroup(id)

    @staticmethod
    def Ingress(): return Ingress()


__all__ = ["DBSecurityGroupFactory"]
