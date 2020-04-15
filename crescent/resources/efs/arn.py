from crescent.core import Arn


class EfsArn(Arn):
    __SERVICE_EFS = "efs"

    def __new__(cls, suffix: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(EfsArn, cls).__new__(cls,
                                          service=cls.__SERVICE_EFS,
                                          suffix=suffix,
                                          partition=partition,
                                          region=region,
                                          account_id=account_id)

# ------------------------------------


class FileSystemArn(EfsArn):
    __FILE_SYSTEM_ARN_SUFFIX = "file-system/{}"

    def __new__(cls, file_system_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(FileSystemArn, cls).__new__(cls,
                                                 suffix=cls.__FILE_SYSTEM_ARN_SUFFIX.format(file_system_id),
                                                 partition=partition,
                                                 region=region,
                                                 account_id=account_id)

# ------------------------------------


class AccessPointArn(EfsArn):
    __ACCESS_POINT_ARN_SUFFIX = "access-point/{}"

    def __new__(cls, access_point_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(AccessPointArn, cls).__new__(cls,
                                                  suffix=cls.__ACCESS_POINT_ARN_SUFFIX.format(access_point_id),
                                                  partition=partition,
                                                  region=region,
                                                  account_id=account_id)
