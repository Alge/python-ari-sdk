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
from ari_sync_sdk.models.bridge import Bridge
from ari_sync_sdk.models.channel import Channel
from ari_sync_sdk.models.event import Event

class ChannelEnteredBridge(Event):
    """
    ChannelEnteredBridge
    """
    bridge: Bridge = Field(...)
    channel: Optional[Channel] = None
    __properties = ["application", "timestamp", "asterisk_id", "type", "bridge", "channel"]

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
    def from_json(cls, json_str: str) -> ChannelEnteredBridge:
        """Create an instance of ChannelEnteredBridge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bridge
        if self.bridge:
            _dict['bridge'] = self.bridge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channel
        if self.channel:
            _dict['channel'] = self.channel.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChannelEnteredBridge:
        """Create an instance of ChannelEnteredBridge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChannelEnteredBridge.parse_obj(obj)

        _obj = ChannelEnteredBridge.parse_obj({
            "application": obj.get("application"),
            "timestamp": obj.get("timestamp"),
            "asterisk_id": obj.get("asterisk_id"),
            "type": obj.get("type"),
            "bridge": Bridge.from_dict(obj.get("bridge")) if obj.get("bridge") is not None else None,
            "channel": Channel.from_dict(obj.get("channel")) if obj.get("channel") is not None else None
        })
        return _obj


