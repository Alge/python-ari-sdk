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

from datetime import date

from pydantic import BaseModel, Field

class StatusInfo(BaseModel):
    """
    Info about Asterisk status  # noqa: E501
    """
    last_reload_time: date = Field(default=..., description="Time when Asterisk was last reloaded.")
    startup_time: date = Field(default=..., description="Time when Asterisk was started.")
    __properties = ["last_reload_time", "startup_time"]

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
    def from_json(cls, json_str: str) -> StatusInfo:
        """Create an instance of StatusInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatusInfo:
        """Create an instance of StatusInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatusInfo.parse_obj(obj)

        _obj = StatusInfo.parse_obj({
            "last_reload_time": obj.get("last_reload_time"),
            "startup_time": obj.get("startup_time")
        })
        return _obj


