class Arn(str):
    def __new__(cls, service: str, suffix: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(Arn, cls).__new__(cls, "arn:{}:{}:{}:{}:{}".format(partition, service, region, account_id, suffix))
