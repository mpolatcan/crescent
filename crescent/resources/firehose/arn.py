from crescent.core import Arn


class DeliveryStreamArn(Arn):
    __SERVICE_FIREHOSE = "firehose"
    __DELIVERY_STREAM_ARN_SUFFIX = "deliverystream/{}"

    def __new__(cls, delivery_stream_name: str, partition: str = "aws", region: str = "", account_id: str = ""):
        return super(DeliveryStreamArn, cls).__new__(cls,
                                                     service=cls.__SERVICE_FIREHOSE,
                                                     suffix=cls.__DELIVERY_STREAM_ARN_SUFFIX.format(delivery_stream_name),
                                                     partition=partition,
                                                     region=region,
                                                     account_id=account_id)
