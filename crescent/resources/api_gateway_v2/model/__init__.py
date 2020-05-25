from .model import Model


class ModelFactory:
    @staticmethod
    def Create(id: str): return Model(id)


__all__ = ["ModelFactory"]
