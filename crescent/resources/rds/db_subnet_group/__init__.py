from .db_subnet_group import DBSubnetGroup


class DBSubnetGroupFactory:
    @staticmethod
    def Create(id: str): return DBSubnetGroup(id)


__all__ = ["DBSubnetGroupFactory"]
