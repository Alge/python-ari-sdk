# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk import util


class DialplanCEP(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_data: str=None, app_name: str=None, context: str=None, exten: str=None, priority: int=None):
        """DialplanCEP - a model defined in OpenAPI

        :param app_data: The app_data of this DialplanCEP.
        :param app_name: The app_name of this DialplanCEP.
        :param context: The context of this DialplanCEP.
        :param exten: The exten of this DialplanCEP.
        :param priority: The priority of this DialplanCEP.
        """
        self.openapi_types = {
            'app_data': str,
            'app_name': str,
            'context': str,
            'exten': str,
            'priority': int
        }

        self.attribute_map = {
            'app_data': 'app_data',
            'app_name': 'app_name',
            'context': 'context',
            'exten': 'exten',
            'priority': 'priority'
        }

        self._app_data = app_data
        self._app_name = app_name
        self._context = context
        self._exten = exten
        self._priority = priority

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DialplanCEP':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DialplanCEP of this DialplanCEP.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_data(self):
        """Gets the app_data of this DialplanCEP.

        Parameter of current dialplan application

        :return: The app_data of this DialplanCEP.
        :rtype: str
        """
        return self._app_data

    @app_data.setter
    def app_data(self, app_data):
        """Sets the app_data of this DialplanCEP.

        Parameter of current dialplan application

        :param app_data: The app_data of this DialplanCEP.
        :type app_data: str
        """
        if app_data is None:
            raise ValueError("Invalid value for `app_data`, must not be `None`")

        self._app_data = app_data

    @property
    def app_name(self):
        """Gets the app_name of this DialplanCEP.

        Name of current dialplan application

        :return: The app_name of this DialplanCEP.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this DialplanCEP.

        Name of current dialplan application

        :param app_name: The app_name of this DialplanCEP.
        :type app_name: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")

        self._app_name = app_name

    @property
    def context(self):
        """Gets the context of this DialplanCEP.

        Context in the dialplan

        :return: The context of this DialplanCEP.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this DialplanCEP.

        Context in the dialplan

        :param context: The context of this DialplanCEP.
        :type context: str
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")

        self._context = context

    @property
    def exten(self):
        """Gets the exten of this DialplanCEP.

        Extension in the dialplan

        :return: The exten of this DialplanCEP.
        :rtype: str
        """
        return self._exten

    @exten.setter
    def exten(self, exten):
        """Sets the exten of this DialplanCEP.

        Extension in the dialplan

        :param exten: The exten of this DialplanCEP.
        :type exten: str
        """
        if exten is None:
            raise ValueError("Invalid value for `exten`, must not be `None`")

        self._exten = exten

    @property
    def priority(self):
        """Gets the priority of this DialplanCEP.

        Priority in the dialplan

        :return: The priority of this DialplanCEP.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DialplanCEP.

        Priority in the dialplan

        :param priority: The priority of this DialplanCEP.
        :type priority: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")

        self._priority = priority
