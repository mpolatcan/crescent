from .stage import Stage


class StageFactory:
    @staticmethod
    def Create(id: str): return Stage(id)


__all__ = ["StageFactory"]
