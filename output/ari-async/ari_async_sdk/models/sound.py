# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.format_lang_pair import FormatLangPair
from ari_async_sdk import util


class Sound(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, formats: List[FormatLangPair]=None, id: str=None, text: str=None):
        """Sound - a model defined in OpenAPI

        :param formats: The formats of this Sound.
        :param id: The id of this Sound.
        :param text: The text of this Sound.
        """
        self.openapi_types = {
            'formats': List[FormatLangPair],
            'id': str,
            'text': str
        }

        self.attribute_map = {
            'formats': 'formats',
            'id': 'id',
            'text': 'text'
        }

        self._formats = formats
        self._id = id
        self._text = text

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Sound':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Sound of this Sound.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def formats(self):
        """Gets the formats of this Sound.

        The formats and languages in which this sound is available.

        :return: The formats of this Sound.
        :rtype: List[FormatLangPair]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """Sets the formats of this Sound.

        The formats and languages in which this sound is available.

        :param formats: The formats of this Sound.
        :type formats: List[FormatLangPair]
        """
        if formats is None:
            raise ValueError("Invalid value for `formats`, must not be `None`")

        self._formats = formats

    @property
    def id(self):
        """Gets the id of this Sound.

        Sound's identifier.

        :return: The id of this Sound.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sound.

        Sound's identifier.

        :param id: The id of this Sound.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def text(self):
        """Gets the text of this Sound.

        Text description of the sound, usually the words spoken.

        :return: The text of this Sound.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Sound.

        Text description of the sound, usually the words spoken.

        :param text: The text of this Sound.
        :type text: str
        """

        self._text = text
