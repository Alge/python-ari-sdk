# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class ChannelUnhold(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, channel: Channel=None):
        """ChannelUnhold - a model defined in OpenAPI

        :param application: The application of this ChannelUnhold.
        :param timestamp: The timestamp of this ChannelUnhold.
        :param asterisk_id: The asterisk_id of this ChannelUnhold.
        :param type: The type of this ChannelUnhold.
        :param channel: The channel of this ChannelUnhold.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'channel': Channel
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'channel': 'channel'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._channel = channel

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChannelUnhold':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ChannelUnhold of this ChannelUnhold.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this ChannelUnhold.

        Name of the application receiving the event.

        :return: The application of this ChannelUnhold.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ChannelUnhold.

        Name of the application receiving the event.

        :param application: The application of this ChannelUnhold.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this ChannelUnhold.

        Time at which this event was created.

        :return: The timestamp of this ChannelUnhold.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ChannelUnhold.

        Time at which this event was created.

        :param timestamp: The timestamp of this ChannelUnhold.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this ChannelUnhold.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this ChannelUnhold.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this ChannelUnhold.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this ChannelUnhold.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this ChannelUnhold.

        Indicates the type of this message.

        :return: The type of this ChannelUnhold.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChannelUnhold.

        Indicates the type of this message.

        :param type: The type of this ChannelUnhold.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def channel(self):
        """Gets the channel of this ChannelUnhold.


        :return: The channel of this ChannelUnhold.
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelUnhold.


        :param channel: The channel of this ChannelUnhold.
        :type channel: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")

        self._channel = channel
