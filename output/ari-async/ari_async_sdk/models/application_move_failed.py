# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class ApplicationMoveFailed(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, args: List[str]=None, channel: Channel=None, destination: str=None):
        """ApplicationMoveFailed - a model defined in OpenAPI

        :param application: The application of this ApplicationMoveFailed.
        :param timestamp: The timestamp of this ApplicationMoveFailed.
        :param asterisk_id: The asterisk_id of this ApplicationMoveFailed.
        :param type: The type of this ApplicationMoveFailed.
        :param args: The args of this ApplicationMoveFailed.
        :param channel: The channel of this ApplicationMoveFailed.
        :param destination: The destination of this ApplicationMoveFailed.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'args': List[str],
            'channel': Channel,
            'destination': str
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'args': 'args',
            'channel': 'channel',
            'destination': 'destination'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._args = args
        self._channel = channel
        self._destination = destination

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApplicationMoveFailed':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApplicationMoveFailed of this ApplicationMoveFailed.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this ApplicationMoveFailed.

        Name of the application receiving the event.

        :return: The application of this ApplicationMoveFailed.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ApplicationMoveFailed.

        Name of the application receiving the event.

        :param application: The application of this ApplicationMoveFailed.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this ApplicationMoveFailed.

        Time at which this event was created.

        :return: The timestamp of this ApplicationMoveFailed.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ApplicationMoveFailed.

        Time at which this event was created.

        :param timestamp: The timestamp of this ApplicationMoveFailed.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this ApplicationMoveFailed.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this ApplicationMoveFailed.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this ApplicationMoveFailed.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this ApplicationMoveFailed.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this ApplicationMoveFailed.

        Indicates the type of this message.

        :return: The type of this ApplicationMoveFailed.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplicationMoveFailed.

        Indicates the type of this message.

        :param type: The type of this ApplicationMoveFailed.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def args(self):
        """Gets the args of this ApplicationMoveFailed.

        Arguments to the application

        :return: The args of this ApplicationMoveFailed.
        :rtype: List[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ApplicationMoveFailed.

        Arguments to the application

        :param args: The args of this ApplicationMoveFailed.
        :type args: List[str]
        """
        if args is None:
            raise ValueError("Invalid value for `args`, must not be `None`")

        self._args = args

    @property
    def channel(self):
        """Gets the channel of this ApplicationMoveFailed.


        :return: The channel of this ApplicationMoveFailed.
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ApplicationMoveFailed.


        :param channel: The channel of this ApplicationMoveFailed.
        :type channel: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")

        self._channel = channel

    @property
    def destination(self):
        """Gets the destination of this ApplicationMoveFailed.


        :return: The destination of this ApplicationMoveFailed.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ApplicationMoveFailed.


        :param destination: The destination of this ApplicationMoveFailed.
        :type destination: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")

        self._destination = destination
