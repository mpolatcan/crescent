from crescent.core import Arn


class RepositoryArn(Arn):
    def __new__(cls,
                repository_name,
                partition="aws",
                region="",
                account_id=""):
        return super(RepositoryArn, cls).__new__(
            cls,
            service="ecr",
            suffix="repository/{}".format(repository_name),
            partition=partition,
            region=region,
            account_id=account_id,
        )
