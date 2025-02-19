# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.bridge import Bridge
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class BridgeDestroyed(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, bridge: Bridge=None):
        """BridgeDestroyed - a model defined in OpenAPI

        :param application: The application of this BridgeDestroyed.
        :param timestamp: The timestamp of this BridgeDestroyed.
        :param asterisk_id: The asterisk_id of this BridgeDestroyed.
        :param type: The type of this BridgeDestroyed.
        :param bridge: The bridge of this BridgeDestroyed.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'bridge': Bridge
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'bridge': 'bridge'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._bridge = bridge

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BridgeDestroyed':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BridgeDestroyed of this BridgeDestroyed.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this BridgeDestroyed.

        Name of the application receiving the event.

        :return: The application of this BridgeDestroyed.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this BridgeDestroyed.

        Name of the application receiving the event.

        :param application: The application of this BridgeDestroyed.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this BridgeDestroyed.

        Time at which this event was created.

        :return: The timestamp of this BridgeDestroyed.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BridgeDestroyed.

        Time at which this event was created.

        :param timestamp: The timestamp of this BridgeDestroyed.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this BridgeDestroyed.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this BridgeDestroyed.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this BridgeDestroyed.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this BridgeDestroyed.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this BridgeDestroyed.

        Indicates the type of this message.

        :return: The type of this BridgeDestroyed.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BridgeDestroyed.

        Indicates the type of this message.

        :param type: The type of this BridgeDestroyed.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def bridge(self):
        """Gets the bridge of this BridgeDestroyed.


        :return: The bridge of this BridgeDestroyed.
        :rtype: Bridge
        """
        return self._bridge

    @bridge.setter
    def bridge(self, bridge):
        """Sets the bridge of this BridgeDestroyed.


        :param bridge: The bridge of this BridgeDestroyed.
        :type bridge: Bridge
        """
        if bridge is None:
            raise ValueError("Invalid value for `bridge`, must not be `None`")

        self._bridge = bridge
