from crescent.core import Arn


class _EfsArn(Arn):
    def __new__(cls,
                suffix,
                partition="aws",
                region="",
                account_id=""):
        return super(_EfsArn, cls).__new__(
            cls,
            service="efs",
            suffix=suffix,
            partition=partition,
            region=region,
            account_id=account_id
        )


class FileSystemArn(_EfsArn):
    def __new__(cls,
                file_system_id: str,
                partition: str = "aws",
                region: str = "",
                account_id: str = ""):
        return super(FileSystemArn, cls).__new__(
            cls,
            suffix="file-system/{}".format(file_system_id),
            partition=partition,
            region=region,
            account_id=account_id
        )


class AccessPointArn(_EfsArn):
    def __new__(cls,
                access_point_id: str,
                partition: str = "aws",
                region: str = "",
                account_id: str = ""):
        return super(AccessPointArn, cls).__new__(
            cls,
            suffix="access-point/{}".format(access_point_id),
            partition=partition,
            region=region,
            account_id=account_id
        )
