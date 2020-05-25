from .delivery_stream import DeliveryStreamFactory
from .arn import *


class Firehose:
    Arn = ArnFactory
    DeliveryStream = DeliveryStreamFactory


__all__ = ["Firehose", "DeliveryStreamArn"]
