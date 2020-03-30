from crescent.core import Arn


class _IAMArn(Arn):
    def __new__(cls, suffix: str, account_id: str = ""):
        return super(_IAMArn, cls).__new__(
            cls, service="iam", suffix=suffix, account_id=account_id
        )

# ------------------------------


class PolicyArn(_IAMArn):
    def __new__(cls, policy_id: str, account_id: str = ""):
        return super(PolicyArn, cls).__new__(
            cls, suffix="policy/{}".format(policy_id), account_id=account_id
        )

# ----------------------------------


class UserArn(_IAMArn):
    def __new__(cls, user_id: str, account_id: str = ""):
        return super(UserArn, cls).__new__(
            cls, suffix="user/{}".format(user_id), account_id=account_id
        )

# ----------------------------------


class GroupArn(_IAMArn):
    def __new__(cls, group_id: str, account_id: str = ""):
        return super(GroupArn, cls).__new__(
            cls, suffix="group/{}".format(group_id), account_id=account_id
        )

# ----------------------------------


class RoleArn(_IAMArn):
    def __new__(cls, role_id: str, account_id: str = ""):
        return super(RoleArn, cls).__new__(
            cls, suffix="role/{}".format(role_id), account_id=account_id
        )


# -----------------------------------


class ServerCertificateArn(_IAMArn):
    def __new__(cls, certificate_id: str, account_id: str = ""):
        return super(ServerCertificateArn, cls).__new__(
            cls, suffix="server-certificate/{}".format(certificate_id), account_id=account_id
        )

# -----------------------------------


class SamlProviderArn(_IAMArn):
    def __new__(cls, provider_id: str, account_id: str = ""):
        return super(SamlProviderArn, cls).__new__(
            cls, suffix="saml-provider/{}".format(provider_id), account_id=account_id
        )

# -----------------------------------


class OidcProviderArn(_IAMArn):
    def __new__(cls, provider_id: str, account_id: str = ""):
        return super(OidcProviderArn, cls).__new__(
            cls, suffix="oidc-provider/{}".format(provider_id), account_id=account_id
        )


