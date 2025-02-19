# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from ari_async_sdk.models.base_model import Model
from ari_async_sdk.models.channel import Channel
from ari_async_sdk.models.event import Event
from ari_async_sdk import util


class ChannelDestroyed(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application: str=None, timestamp: date=None, asterisk_id: str=None, type: str=None, cause: int=None, cause_txt: str=None, channel: Channel=None):
        """ChannelDestroyed - a model defined in OpenAPI

        :param application: The application of this ChannelDestroyed.
        :param timestamp: The timestamp of this ChannelDestroyed.
        :param asterisk_id: The asterisk_id of this ChannelDestroyed.
        :param type: The type of this ChannelDestroyed.
        :param cause: The cause of this ChannelDestroyed.
        :param cause_txt: The cause_txt of this ChannelDestroyed.
        :param channel: The channel of this ChannelDestroyed.
        """
        self.openapi_types = {
            'application': str,
            'timestamp': date,
            'asterisk_id': str,
            'type': str,
            'cause': int,
            'cause_txt': str,
            'channel': Channel
        }

        self.attribute_map = {
            'application': 'application',
            'timestamp': 'timestamp',
            'asterisk_id': 'asterisk_id',
            'type': 'type',
            'cause': 'cause',
            'cause_txt': 'cause_txt',
            'channel': 'channel'
        }

        self._application = application
        self._timestamp = timestamp
        self._asterisk_id = asterisk_id
        self._type = type
        self._cause = cause
        self._cause_txt = cause_txt
        self._channel = channel

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChannelDestroyed':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ChannelDestroyed of this ChannelDestroyed.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application(self):
        """Gets the application of this ChannelDestroyed.

        Name of the application receiving the event.

        :return: The application of this ChannelDestroyed.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this ChannelDestroyed.

        Name of the application receiving the event.

        :param application: The application of this ChannelDestroyed.
        :type application: str
        """
        if application is None:
            raise ValueError("Invalid value for `application`, must not be `None`")

        self._application = application

    @property
    def timestamp(self):
        """Gets the timestamp of this ChannelDestroyed.

        Time at which this event was created.

        :return: The timestamp of this ChannelDestroyed.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ChannelDestroyed.

        Time at which this event was created.

        :param timestamp: The timestamp of this ChannelDestroyed.
        :type timestamp: date
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def asterisk_id(self):
        """Gets the asterisk_id of this ChannelDestroyed.

        The unique ID for the Asterisk instance that raised this event.

        :return: The asterisk_id of this ChannelDestroyed.
        :rtype: str
        """
        return self._asterisk_id

    @asterisk_id.setter
    def asterisk_id(self, asterisk_id):
        """Sets the asterisk_id of this ChannelDestroyed.

        The unique ID for the Asterisk instance that raised this event.

        :param asterisk_id: The asterisk_id of this ChannelDestroyed.
        :type asterisk_id: str
        """

        self._asterisk_id = asterisk_id

    @property
    def type(self):
        """Gets the type of this ChannelDestroyed.

        Indicates the type of this message.

        :return: The type of this ChannelDestroyed.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChannelDestroyed.

        Indicates the type of this message.

        :param type: The type of this ChannelDestroyed.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def cause(self):
        """Gets the cause of this ChannelDestroyed.

        Integer representation of the cause of the hangup

        :return: The cause of this ChannelDestroyed.
        :rtype: int
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this ChannelDestroyed.

        Integer representation of the cause of the hangup

        :param cause: The cause of this ChannelDestroyed.
        :type cause: int
        """
        if cause is None:
            raise ValueError("Invalid value for `cause`, must not be `None`")

        self._cause = cause

    @property
    def cause_txt(self):
        """Gets the cause_txt of this ChannelDestroyed.

        Text representation of the cause of the hangup

        :return: The cause_txt of this ChannelDestroyed.
        :rtype: str
        """
        return self._cause_txt

    @cause_txt.setter
    def cause_txt(self, cause_txt):
        """Sets the cause_txt of this ChannelDestroyed.

        Text representation of the cause of the hangup

        :param cause_txt: The cause_txt of this ChannelDestroyed.
        :type cause_txt: str
        """
        if cause_txt is None:
            raise ValueError("Invalid value for `cause_txt`, must not be `None`")

        self._cause_txt = cause_txt

    @property
    def channel(self):
        """Gets the channel of this ChannelDestroyed.


        :return: The channel of this ChannelDestroyed.
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelDestroyed.


        :param channel: The channel of this ChannelDestroyed.
        :type channel: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")

        self._channel = channel
