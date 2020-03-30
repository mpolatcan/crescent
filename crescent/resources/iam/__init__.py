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
from .arn import (
    PolicyArn,
    GroupArn,
    RoleArn,
    UserArn,
    OidcProviderArn,
    SamlProviderArn
)
from .constants import AccessKeyStatus, AwsManagedPolicy


class Iam:
    AwsManagedPolicy = AwsManagedPolicy

    class AccessKey:
        Status = AccessKeyStatus

        @staticmethod
        def Create(id: str):
            return AccessKey(id)

    class Group:
        @staticmethod
        def Create(id: str):
            return Group(id)

    class InstanceProfile:
        @staticmethod
        def Create(id: str):
            return InstanceProfile(id)

    class ManagedPolicy:
        @staticmethod
        def Create(id: str):
            return ManagedPolicy(id)

    class Policy:
        @staticmethod
        def Create(id: str):
            return Policy(id)

    class Role:
        @staticmethod
        def Create(id: str):
            return Role(id)

    class ServiceLinkedRole:
        @staticmethod
        def Create(id: str):
            return ServiceLinkedRole(id)

    class User:
        @staticmethod
        def Create(id: str):
            return User(id)

        @staticmethod
        def LoginProfile():
            return LoginProfile()

    class UserToGroupAddition:
        @staticmethod
        def Create(id: str):
            return UserToGroupAddition(id)

    class Arn:
        @staticmethod
        def PolicyArn(policy_id: str, account_id: str = ""):
            return PolicyArn(policy_id, account_id)

        @staticmethod
        def GroupArn(group_id: str, account_id: str = ""):
            return GroupArn(group_id, account_id)

        @staticmethod
        def RoleArn(role_id: str, account_id: str = ""):
            return RoleArn(role_id, account_id)

        @staticmethod
        def UserArn(user_id: str, account_id: str = ""):
            return UserArn(user_id, account_id)

        @staticmethod
        def OidcProviderArn(provider_id: str, account_id: str = ""):
            return OidcProviderArn(provider_id, account_id)

        @staticmethod
        def SamlProviderArn(provider_id: str, account_id: str = ""):
            return SamlProviderArn(provider_id, account_id)

    @staticmethod
    def PolicyModel():
        return PolicyModel()


__all__ = [
    "Iam"
]
