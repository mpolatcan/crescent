from .api_mapping import ApiMapping


class ApiMappingFactory:
    @staticmethod
    def Create(id: str): return ApiMapping(id)


__all__ = ["ApiMappingFactory"]
