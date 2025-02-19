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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from ari_sync_sdk.models.format_lang_pair import FormatLangPair

class Sound(BaseModel):
    """
    A media file that may be played back.  # noqa: E501
    """
    formats: conlist(FormatLangPair) = Field(default=..., description="The formats and languages in which this sound is available.")
    id: StrictStr = Field(default=..., description="Sound's identifier.")
    text: Optional[StrictStr] = Field(default=None, description="Text description of the sound, usually the words spoken.")
    __properties = ["formats", "id", "text"]

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
    def from_json(cls, json_str: str) -> Sound:
        """Create an instance of Sound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in formats (list)
        _items = []
        if self.formats:
            for _item in self.formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Sound:
        """Create an instance of Sound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Sound.parse_obj(obj)

        _obj = Sound.parse_obj({
            "formats": [FormatLangPair.from_dict(_item) for _item in obj.get("formats")] if obj.get("formats") is not None else None,
            "id": obj.get("id"),
            "text": obj.get("text")
        })
        return _obj


