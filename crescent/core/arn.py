class Arn(str):
    def __new__(cls, service: str, suffix: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(Arn, cls).__new__(cls,
                                       "arn:{}:{}:{}:{}:{}".format(partition,
                                                                   service,
                                                                   region,
                                                                   account_id,
                                                                   suffix))
