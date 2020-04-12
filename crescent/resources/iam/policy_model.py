from crescent.core import Model
from crescent.functions import AnyFn
from .constants import ModelRequiredProperties
from typing import Union


class PolicyModel(Model):
    def __init__(self):
        super(PolicyModel, self).__init__(
            min_length={self.PolicyDocument.__name__: 1,
                        self.PolicyName.__name__: 1},
            max_length={self.PolicyDocument.__name__: 131072,
                        self.PolicyName.__name__: 128},
            pattern={self.PolicyDocument.__name__: r"[\u0009\u000A\u000D\u0020-\u00FF]+",
                     self.PolicyName.__name__: r"[\w+=,.@-]+"},
            required_properties=ModelRequiredProperties.POLICY_MODEL
        )

    def PolicyDocument(self, policy_document: Union[dict, AnyFn]):
        return self._set_field(self.PolicyDocument.__name__, policy_document)

    def PolicyName(self, policy_name: Union[str, AnyFn]):
        return self._set_field(self.PolicyName.__name__, policy_name)
