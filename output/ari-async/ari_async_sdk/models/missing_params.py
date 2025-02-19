# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.message import Message
from ari_async_sdk import util


class MissingParams(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, asterisk_id: str=None, type: str=None, params: List[str]=None):
        """MissingParams - a model defined in OpenAPI

        :param asterisk_id: The asterisk_id of this MissingParams.
        :param type: The type of this MissingParams.
        :param params: The params of this MissingParams.
        """
        self.openapi_types = {
            'asterisk_id': str,
            'type': str,
            'params': List[str]
        }

        self.attribute_map = {
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'params': 'params'
        }

        self._asterisk_id = asterisk_id
        self._type = type
        self._params = params

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MissingParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MissingParams of this MissingParams.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this MissingParams.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this MissingParams.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this MissingParams.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this MissingParams.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this MissingParams.

        Indicates the type of this message.

        :return: The type of this MissingParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MissingParams.

        Indicates the type of this message.

        :param type: The type of this MissingParams.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def params(self):
        """Gets the params of this MissingParams.

        A list of the missing parameters

        :return: The params of this MissingParams.
        :rtype: List[str]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this MissingParams.

        A list of the missing parameters

        :param params: The params of this MissingParams.
        :type params: List[str]
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")

        self._params = params
