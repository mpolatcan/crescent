from crescent.core import Arn


class KinesisArn(Arn):
    __SERVICE_KINESIS = "kinesis"

    def __new__(cls, suffix: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(KinesisArn, cls).__new__(cls,
                                              service=cls.__SERVICE_KINESIS,
                                              suffix=suffix,
                                              region=region,
                                              account_id=account_id,
                                              partition=partition)

# -------------------------------------


class StreamArn(KinesisArn):
    __STREAM_ARN_SUFFIX = "stream/{}"

    def __new__(cls, stream_id: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(StreamArn, cls).__new__(cls,
                                             suffix=cls.__STREAM_ARN_SUFFIX.format(stream_id),
                                             region=region,
                                             account_id=account_id,
                                             partition=partition)


# ----------------------------


class StreamConsumerArn(KinesisArn):
    __STREAM_CONSUMER_ARN_SUFFIX = "{}/{}/consumer/{}:{}"

    def __new__(cls, stream_type: str, stream_id: str, consumer_id: str, consumer_creation_timpstamps: str = "",
                region: str = "", account_id: str = "", partition: str = "aws"):
        return super(StreamConsumerArn, cls).__new__(cls,
                                                     suffix=cls.__STREAM_CONSUMER_ARN_SUFFIX.format(
                                                        stream_type, stream_id, consumer_id, consumer_creation_timpstamps
                                                     ),
                                                     region=region,
                                                     account_id=account_id,
                                                     partition=partition)

# ----------------------------


class ArnFactory:
    @staticmethod
    def StreamArn(stream_id: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return StreamArn(stream_id=stream_id, partition=partition, region=region, account_id=account_id)

    @staticmethod
    def StreamConsumerArn(stream_type: str, stream_id: str, consumer_id: str, consumer_creation_timpstamps: str = "",
                          partition: str = "aws", region: str = "", account_id: str = ""):
        return StreamConsumerArn(stream_type=stream_type,
                                 stream_id=stream_id,
                                 consumer_id=consumer_id,
                                 consumer_creation_timpstamps=consumer_creation_timpstamps,
                                 partition=partition,
                                 region=region,
                                 account_id=account_id)