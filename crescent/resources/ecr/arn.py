from crescent.core import Arn


class RepositoryArn(Arn):
    __SERVICE_ECR = "ecr"
    __REPOSITORY_ARN_SUFFIX = "repository/{}"

    def __new__(cls,
                repository_name: str,
                partition: str = "aws",
                region: str = "",
                account_id: str = ""):
        return super(RepositoryArn, cls).__new__(
            cls,
            service=cls.__SERVICE_ECR,
            suffix=cls.__REPOSITORY_ARN_SUFFIX.format(repository_name),
            partition=partition,
            region=region,
            account_id=account_id,
        )
