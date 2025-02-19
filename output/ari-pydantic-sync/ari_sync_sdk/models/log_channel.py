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



from pydantic import BaseModel, Field, StrictStr

class LogChannel(BaseModel):
    """
    Details of an Asterisk log channel  # noqa: E501
    """
    channel: StrictStr = Field(default=..., description="The log channel path")
    configuration: StrictStr = Field(default=..., description="The various log levels")
    status: StrictStr = Field(default=..., description="Whether or not a log type is enabled")
    type: StrictStr = Field(default=..., description="Types of logs for the log channel")
    __properties = ["channel", "configuration", "status", "type"]

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
    def from_json(cls, json_str: str) -> LogChannel:
        """Create an instance of LogChannel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LogChannel:
        """Create an instance of LogChannel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LogChannel.parse_obj(obj)

        _obj = LogChannel.parse_obj({
            "channel": obj.get("channel"),
            "configuration": obj.get("configuration"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj


