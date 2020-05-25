from .domain_name_configuration import DomainNameConfiguration
from .domain_name import DomainName


class DomainNameFactory:
    @staticmethod
    def Create(id: str): return DomainName(id)

    @staticmethod
    def DomainNameConfiguration(): return DomainNameConfiguration()


__all__ = ["DomainNameFactory"]
