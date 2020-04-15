from crescent.core import Arn


class DeliveryStreamArn(Arn):
    __SERVICE_FIREHOSE = "firehose"
    __DELIVERY_STREAM_ARN_SUFFIX = "deliverystream/{}"

    def __new__(cls, delivery_stream_name: str, region: str = "", account_id: str = "", partition: str = "aws"):
        return super(DeliveryStreamArn, cls).__new__(cls,
                                                     service=cls.__SERVICE_FIREHOSE,
                                                     suffix=cls.__DELIVERY_STREAM_ARN_SUFFIX.format(delivery_stream_name),
                                                     region=region,
                                                     account_id=account_id,
                                                     partition=partition)
