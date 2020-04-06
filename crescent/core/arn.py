class Arn(str):
    def __new__(cls,
                service,
                suffix,
                partition="aws",
                region="",
                account_id=""):
        return super(Arn, cls).__new__(
            cls, "arn:{}:{}:{}:{}:{}".format(
                partition,
                service,
                region,
                account_id,
                suffix
            )
        )
