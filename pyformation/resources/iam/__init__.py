from .access_key import AccessKey
from .group import Group
from .instance_profile import InstanceProfile
from .login_profile import LoginProfile
from .managed_policy import ManagedPolicy
from .policy import Policy
from .policy_model import PolicyModel
from .role import Role
from .service_linked_role import ServiceLinkedRole
from .user import User
from .user_to_group_addition import UserToGroupAddition


class IamFactory:
    @staticmethod
    def AccessKey(id: str):
        return AccessKey(id)

    @staticmethod
    def Group(id: str):
        return Group(id)

    @staticmethod
    def InstanceProfile(id: str):
        return InstanceProfile(id)

    @staticmethod
    def LoginProfile():
        return LoginProfile()

    @staticmethod
    def ManagedPolicy(id: str):
        return ManagedPolicy(id)

    @staticmethod
    def Policy(id: str):
        return Policy(id)

    @staticmethod
    def PolicyModel():
        return PolicyModel()

    @staticmethod
    def Role(id: str):
        return Role(id)

    @staticmethod
    def ServiceLinkedRole(id: str):
        return ServiceLinkedRole(id)

    @staticmethod
    def User(id: str):
        return User(id)

    @staticmethod
    def UserToGroupAddition(id: str):
        return UserToGroupAddition(id)


__all__ = [
    "IamFactory"
]