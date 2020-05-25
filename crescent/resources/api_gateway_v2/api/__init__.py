from .body_s3_location import BodyS3Location
from .cors import Cors
from .api import Api
from .constants import BasePath


class ApiFactory:
    BasePath = BasePath

    @staticmethod
    def Create(id: str): return Api(id)

    @staticmethod
    def BodyS3Location(): return BodyS3Location()

    @staticmethod
    def Cors(): return Cors()


__all__ = ["ApiFactory"]
