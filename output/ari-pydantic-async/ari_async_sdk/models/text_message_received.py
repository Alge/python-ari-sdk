# coding: utf-8

"""
    Asterisk ARI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import Field
from ari_async_sdk.models.endpoint import Endpoint
from ari_async_sdk.models.event import Event
from ari_async_sdk.models.text_message import TextMessage

class TextMessageReceived(Event):
    """
    TextMessageReceived
    """
    endpoint: Optional[Endpoint] = None
    message: TextMessage = Field(...)
    __properties = ["application", "timestamp", "asterisk_id", "type", "endpoint", "message"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TextMessageReceived:
        """Create an instance of TextMessageReceived from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of endpoint
        if self.endpoint:
            _dict['endpoint'] = self.endpoint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TextMessageReceived:
        """Create an instance of TextMessageReceived from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TextMessageReceived.parse_obj(obj)

        _obj = TextMessageReceived.parse_obj({
            "application": obj.get("application"),
            "timestamp": obj.get("timestamp"),
            "asterisk_id": obj.get("asterisk_id"),
            "type": obj.get("type"),
            "endpoint": Endpoint.from_dict(obj.get("endpoint")) if obj.get("endpoint") is not None else None,
            "message": TextMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None
        })
        return _obj


