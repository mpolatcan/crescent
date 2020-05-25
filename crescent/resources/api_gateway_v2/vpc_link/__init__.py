from .vpc_link import VpcLink


class VpcLinkFactory:
    @staticmethod
    def Create(id: str): return VpcLink(id)


__all__ = ["VpcLinkFactory"]
