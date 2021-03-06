from crescent.core.constants import get_values
from .arn import PolicyArn
from itertools import chain


class AwsManagedPolicy:
    class Iam:
        ACCESS_ADVISOR_READ_ONLY = PolicyArn("IAMAccessAdvisorReadOnly")
        ACCESS_ANALYZER_FULL_ACCESS = PolicyArn("IAMAccessAnalyzerFullAccess")
        ACCESS_ANALYZER_READ_ONLY = PolicyArn("IAMAccessAnalyzerReadOnlyAccess")
        FULL_ACCESS = PolicyArn("IAMFullAccess")
        READ_ONLY_ACCESS = PolicyArn("IAMReadOnlyAccess")
        SELF_MANAGE_SERVICE_SPECIFIC_CREDENTIALS = PolicyArn("IAMSelfManageServiceSpecificCredentials")
        USER_CHANGE_PASSWORD = PolicyArn("IAMUserChangePassword")
        USER_SSH_KEYS = PolicyArn("IAMUserSSHKeys")

    class Ecr:
        FULL_ACCESS = PolicyArn("AmazonEC2ContainerRegistryFullAccess")
        POWER_USER = PolicyArn("AmazonEC2ContainerRegistryPowerUser")
        READ_ONLY = PolicyArn("AmazonEC2ContainerRegistryReadOnly")

    class Efs:
        CLIENT_FULL_ACCESS = PolicyArn("AmazonElasticFileSystemClientFullAccess")
        CLIENT_READ_ONLY_ACCESS = PolicyArn("AmazonElasticFileSystemClientReadOnlyAccess")
        CLIENT_READ_WRITE_ACCESS = PolicyArn("AmazonElasticFileSystemClientReadWriteAccess")
        FULL_ACCESS = PolicyArn("AmazonElasticFileSystemFullAccess")
        READ_ONLY_ACCESS = PolicyArn("AmazonElasticFileSystemReadOnlyAccess")
        SERVICE_ROLE_POLICY = PolicyArn("AmazonElasticFileSystemServiceRolePolicy")

    class Firehose:
        FULL_ACCESS = PolicyArn("AmazonKinesisFirehoseFullAccess")
        READ_ONLY_ACCESS = PolicyArn("AmazonKinesisFirehoseReadOnlyAccess")

    class Kinesis:
        FULL_ACCESS = PolicyArn("AmazonKinesisFullAccess")
        READ_ONLY_ACCESS = PolicyArn("AmazonKinesisReadOnlyAccess")

    class Rds:
        BETA_SERVICE_ROLE_POLICY = PolicyArn("AmazonRDSBetaServiceRolePolicy")
        DATA_FULL_ACCESS = PolicyArn("AmazonRDSDataFullAccess")
        DIRECTORY_SERVICE_ACCESS = PolicyArn("AmazonRDSDirectoryServiceAccess")
        ENHANCED_MONITORING_ROLE = PolicyArn("AmazonRDSEnhancedMonitoringRole")
        FULL_ACCESS = PolicyArn("AmazonRDSFullAccess")
        PREVIEW_SERVICE_ROLE_POLICY = PolicyArn("AmazonRDSPreviewServiceRolePolicy")
        READ_ONLY_ACCESS = PolicyArn("AmazonRDSReadOnlyAccess")
        SERVICE_ROLE_POLICY = PolicyArn("AmazonRDSServiceRolePolicy")

    class S3:
        FULL_ACCESS = PolicyArn("AmazonS3FullAccess")
        READ_ONLY_ACCESS = PolicyArn("AmazonS3ReadOnlyAccess")

# -----------------------------------------------------------


class AccessKeyStatus:
    ACTIVE = "Active"
    INACTIVE = "Inactive"

# -----------------------------------------------------------


class _RequiredProperties:
    class PolicyModel:
        POLICY_DOCUMENT = "PolicyDocument"
        POLICY_NAME = "PolicyName"

    class LoginProfile:
        PASSWORD = "Password"

    class AccessKey:
        USERNAME = "Username"

    class InstanceProfile:
        ROLES = "Roles"

    class ManagedPolicy:
        POLICY_DOCUMENT = "PolicyDocument"

    class Policy:
        POLICY_DOCUMENT = "PolicyDocument"
        POLICY_NAME = "PolicyName"

    class Role:
        ASSUME_ROLE_POLICY_DOCUMENT = "AssumeRolePolicyDocument"

    class ServiceLinkedRole:
        AWS_SERVICE_NAME = "AWSServiceName"

    class UserToGroupAddition:
        GROUP_NAME = "GroupName"
        USERS = "Users"

# -----------------------------------------------------------


class ModelRequiredProperties:
    POLICY_MODEL = get_values(_RequiredProperties.PolicyModel)
    LOGIN_PROFILE = get_values(_RequiredProperties.LoginProfile)

# -----------------------------------------------------------


class ResourceRequiredProperties:
    ACCESS_KEY = get_values(_RequiredProperties.AccessKey)
    INSTANCE_PROFILE = get_values(_RequiredProperties.InstanceProfile)
    MANAGED_POLICY = get_values(_RequiredProperties.ManagedPolicy)
    POLICY = get_values(_RequiredProperties.Policy)
    ROLE = get_values(_RequiredProperties.Role)
    SERVICE_LINKED_ROLE = get_values(_RequiredProperties.ServiceLinkedRole)
    USER_TO_GROUP_ADDITION = get_values(_RequiredProperties.UserToGroupAddition)

# -----------------------------------------------------------


class AllowedValues:
    STATUS = get_values(AccessKeyStatus)
    MANAGED_POLICY_ARNS = list(chain.from_iterable([
        get_values(AwsManagedPolicy.Ecr),
        get_values(AwsManagedPolicy.Efs),
        get_values(AwsManagedPolicy.Firehose),
        get_values(AwsManagedPolicy.Iam),
        get_values(AwsManagedPolicy.Kinesis),
        get_values(AwsManagedPolicy.Rds),
        get_values(AwsManagedPolicy.S3)
    ]))
