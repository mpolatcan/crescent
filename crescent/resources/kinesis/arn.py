from crescent.core import Arn


class KinesisArn(Arn):
    __SERVICE_KINESIS = "kinesis"

    def __new__(cls,
                suffix: str,
                partition: str = "aws",
                region: str = "",
                account_id: str = ""):
        return super(KinesisArn, cls).__new__(
            cls,
            service=cls.__SERVICE_KINESIS,
            suffix=suffix,
            partition=partition,
            region=region,
            account_id=account_id
        )

# -------------------------------------


class StreamArn(KinesisArn):
    __STREAM_ARN_SUFFIX = "stream/{}"

    def __new__(cls,
                stream_id: str,
                partition: str = "aws",
                region: str = "",
                account_id: str = ""):
        return super(StreamArn, cls).__new__(
            cls,
            suffix=cls.__STREAM_ARN_SUFFIX.format(stream_id),
            partition=partition,
            region=region,
            account_id=account_id
        )


# ----------------------------


class StreamConsumerArn(KinesisArn):
    __STREAM_CONSUMER_ARN_SUFFIX = "{}/{}/consumer/{}:{}"

    def __new__(cls,
                stream_type: str,
                stream_id: str,
                consumer_id: str,
                consumer_creation_timpstamps: str = "",
                partition: str = "aws",
                region: str = "",
                account_id: str = ""):
        return super(StreamConsumerArn, cls).__new__(
            cls,
            suffix=cls.__STREAM_CONSUMER_ARN_SUFFIX.format(
                stream_type, stream_id, consumer_id, consumer_creation_timpstamps
            ),
            partition=partition,
            region=region,
            account_id=account_id
        )
