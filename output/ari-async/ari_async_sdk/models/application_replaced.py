# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class ApplicationReplaced(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None):
        """ApplicationReplaced - a model defined in OpenAPI

        :param application: The application of this ApplicationReplaced.
        :param timestamp: The timestamp of this ApplicationReplaced.
        :param asterisk_id: The asterisk_id of this ApplicationReplaced.
        :param type: The type of this ApplicationReplaced.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApplicationReplaced':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApplicationReplaced of this ApplicationReplaced.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this ApplicationReplaced.

        Name of the application receiving the event.

        :return: The application of this ApplicationReplaced.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ApplicationReplaced.

        Name of the application receiving the event.

        :param application: The application of this ApplicationReplaced.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this ApplicationReplaced.

        Time at which this event was created.

        :return: The timestamp of this ApplicationReplaced.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ApplicationReplaced.

        Time at which this event was created.

        :param timestamp: The timestamp of this ApplicationReplaced.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this ApplicationReplaced.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this ApplicationReplaced.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this ApplicationReplaced.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this ApplicationReplaced.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this ApplicationReplaced.

        Indicates the type of this message.

        :return: The type of this ApplicationReplaced.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplicationReplaced.

        Indicates the type of this message.

        :param type: The type of this ApplicationReplaced.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
