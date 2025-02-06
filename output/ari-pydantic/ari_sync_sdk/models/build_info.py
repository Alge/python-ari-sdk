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

class BuildInfo(BaseModel):
    """
    Info about how Asterisk was built  # noqa: E501
    """
    var_date: StrictStr = Field(default=..., alias="date", description="Date and time when Asterisk was built.")
    kernel: StrictStr = Field(default=..., description="Kernel version Asterisk was built on.")
    machine: StrictStr = Field(default=..., description="Machine architecture (x86_64, i686, ppc, etc.)")
    options: StrictStr = Field(default=..., description="Compile time options, or empty string if default.")
    os: StrictStr = Field(default=..., description="OS Asterisk was built on.")
    user: StrictStr = Field(default=..., description="Username that build Asterisk")
    __properties = ["date", "kernel", "machine", "options", "os", "user"]

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
    def from_json(cls, json_str: str) -> BuildInfo:
        """Create an instance of BuildInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BuildInfo:
        """Create an instance of BuildInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BuildInfo.parse_obj(obj)

        _obj = BuildInfo.parse_obj({
            "var_date": obj.get("date"),
            "kernel": obj.get("kernel"),
            "machine": obj.get("machine"),
            "options": obj.get("options"),
            "os": obj.get("os"),
            "user": obj.get("user")
        })
        return _obj


