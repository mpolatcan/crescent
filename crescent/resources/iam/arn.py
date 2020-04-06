from crescent.core import Arn


class IAMArn(Arn):
    __SERVICE_IAM = "iam"

    def __new__(cls, suffix: str, account_id: str = ""):
        return super(IAMArn, cls).__new__(
            cls, service=cls.__SERVICE_IAM, suffix=suffix, account_id=account_id
        )

# ------------------------------


class PolicyArn(IAMArn):
    __POLICY_ARN_SUFFIX = "policy/{}"

    def __new__(cls, policy_id: str, account_id: str = ""):
        return super(PolicyArn, cls).__new__(
            cls, suffix=cls.__POLICY_ARN_SUFFIX.format(policy_id), account_id=account_id
        )

# ----------------------------------


class UserArn(IAMArn):
    __USER_ARN_SUFFIX = "user/{}"

    def __new__(cls, user_id: str, account_id: str = ""):
        return super(UserArn, cls).__new__(
            cls, suffix=cls.__USER_ARN_SUFFIX.format(user_id), account_id=account_id
        )

# ----------------------------------


class GroupArn(IAMArn):
    __GROUP_ARN_SUFFIX = "group/{}"

    def __new__(cls, group_id: str, account_id: str = ""):
        return super(GroupArn, cls).__new__(
            cls, suffix=cls.__GROUP_ARN_SUFFIX.format(group_id), account_id=account_id
        )

# ----------------------------------


class RoleArn(IAMArn):
    __ROLE_ARN_SUFFIX = "role/{}"

    def __new__(cls, role_id: str, account_id: str = ""):
        return super(RoleArn, cls).__new__(
            cls, suffix=cls.__ROLE_ARN_SUFFIX.format(role_id), account_id=account_id
        )


# -----------------------------------

class InstanceProfileArn(IAMArn):
    __INSTANCE_PROFILE_ARN_SUFFIX = "instance-profile/{}"

    def __new__(cls, instance_profile_id: str, account_id: str = ""):
        return super(InstanceProfileArn, cls).__new__(
            cls, suffix=cls.__INSTANCE_PROFILE_ARN_SUFFIX.format(instance_profile_id), account_id=account_id
        )


# -----------------------------------


class ServerCertificateArn(IAMArn):
    __SERVER_CERTIFICATE_ARN_SUFFIX = "server-certificate/{}"

    def __new__(cls, certificate_id: str, account_id: str = ""):
        return super(ServerCertificateArn, cls).__new__(
            cls, suffix=cls.__SERVER_CERTIFICATE_ARN_SUFFIX.format(certificate_id), account_id=account_id
        )

# -----------------------------------


class SamlProviderArn(IAMArn):
    __SAML_PROVIDER_ARN_SUFFIX = "saml-provider/{}"

    def __new__(cls, provider_id: str, account_id: str = ""):
        return super(SamlProviderArn, cls).__new__(
            cls, suffix=cls.__SAML_PROVIDER_ARN_SUFFIX.format(provider_id), account_id=account_id
        )

# -----------------------------------


class OidcProviderArn(IAMArn):
    __OIDC_PROVIDER_ARN_SUFFIX = "oidc-provider/{}"

    def __new__(cls, provider_id: str, account_id: str = ""):
        return super(OidcProviderArn, cls).__new__(
            cls, suffix=cls.__OIDC_PROVIDER_ARN_SUFFIX.format(provider_id), account_id=account_id
        )

# ------------------------------------


class MfaArn(IAMArn):
    __MFA_ARN_SUFFIX = "mfa/{}"

    def __new__(cls, mfa_id: str, account_id: str = ""):
        return super(MfaArn, cls).__new__(
            cls, suffix=cls.__MFA_ARN_SUFFIX.format(mfa_id), account_id=account_id
        )


# -----------------------------------


class U2fArn(IAMArn):
    __U2F_ARN_SUFFIX = "u2f/{}"

    def __new__(cls, u2f_id: str, account_id: str = ""):
        return super(U2fArn, cls).__new__(
            cls, suffix=cls.__U2F_ARN_SUFFIX.format(u2f_id), account_id=account_id
        )

