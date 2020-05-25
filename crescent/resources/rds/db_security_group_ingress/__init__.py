from .db_security_group_ingress import DBSecurityGroupIngress


class DBSecurityGroupIngressFactory:
    @staticmethod
    def Create(id: str): return DBSecurityGroupIngress(id)


__all__ = ["DBSecurityGroupIngressFactory"]
