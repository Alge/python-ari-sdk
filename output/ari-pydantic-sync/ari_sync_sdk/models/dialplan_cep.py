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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class DialplanCEP(BaseModel):
    """
    Dialplan location (context/extension/priority)  # noqa: E501
    """
    app_data: StrictStr = Field(default=..., description="Parameter of current dialplan application")
    app_name: StrictStr = Field(default=..., description="Name of current dialplan application")
    context: StrictStr = Field(default=..., description="Context in the dialplan")
    exten: StrictStr = Field(default=..., description="Extension in the dialplan")
    priority: StrictInt = Field(default=..., description="Priority in the dialplan")
    __properties = ["app_data", "app_name", "context", "exten", "priority"]

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
    def from_json(cls, json_str: str) -> DialplanCEP:
        """Create an instance of DialplanCEP from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DialplanCEP:
        """Create an instance of DialplanCEP from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DialplanCEP.parse_obj(obj)

        _obj = DialplanCEP.parse_obj({
            "app_data": obj.get("app_data"),
            "app_name": obj.get("app_name"),
            "context": obj.get("context"),
            "exten": obj.get("exten"),
            "priority": obj.get("priority")
        })
        return _obj


